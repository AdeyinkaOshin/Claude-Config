"""
Standalone WhatsApp -> Claude MCP gateway.

Wraps a WAHA (WhatsApp HTTP API) instance as MCP tools so Claude can send/read
WhatsApp messages and manage the phone pairing session. Speaks Streamable HTTP MCP,
so it plugs into Claude Code (.mcp.json / `claude mcp add`) as a custom connector.

Two services make up the full stack:
  1. WAHA        - the WhatsApp engine + QR pairing dashboard (Docker: devlikeapro/waha)
  2. this gateway - the thin MCP layer Claude actually talks to

Env vars this reads:
  WAHA_URL      - base URL of the WAHA service           (required)
  WAHA_API_KEY  - the X-Api-Key WAHA is protected with   (optional but recommended)
  WAHA_SESSION  - session name, default "default"
  GATEWAY_KEY   - if set, callers must send x-api-key: <this>  (protects the gateway)
  PORT          - bind port (Railway injects this)
"""

import os
import re
from datetime import datetime, timezone

import httpx
from starlette.responses import JSONResponse
from mcp.server.fastmcp import FastMCP

WAHA_URL = os.environ.get("WAHA_URL", "").rstrip("/")
WAHA_API_KEY = os.environ.get("WAHA_API_KEY")
WAHA_SESSION = os.environ.get("WAHA_SESSION", "default")
GATEWAY_KEY = os.environ.get("GATEWAY_KEY")
PORT = int(os.environ.get("PORT", "8000"))


# --------------------------------------------------------------------------- WAHA I/O
def _headers():
    h = {"Content-Type": "application/json"}
    if WAHA_API_KEY:
        h["X-Api-Key"] = WAHA_API_KEY
    return h


def waha_try(method, endpoint, data=None, params=None):
    """Call WAHA without raising on HTTP errors. Returns (status_code, body).

    WAHA moved its session routes between versions (legacy POST /sessions/start with a
    body vs POST /sessions/{name}/start), so callers must inspect the code and fall
    back rather than blow up on the first 404.
    """
    if not WAHA_URL:
        return 0, {"error": "WAHA_URL not configured"}
    url = f"{WAHA_URL}/api{endpoint}"
    try:
        with httpx.Client(timeout=60) as http:
            if method == "GET":
                r = http.get(url, headers=_headers(), params=params)
            elif method == "POST":
                r = http.post(url, headers=_headers(), json=data or {}, params=params)
            elif method == "DELETE":
                r = http.delete(url, headers=_headers(), params=params)
            else:
                raise ValueError(f"Unknown method: {method}")
    except Exception as e:
        return 0, {"error": str(e)}
    try:
        body = r.json() if r.text else {}
    except Exception:
        body = {"raw": r.text[:2000]}
    return r.status_code, body


def waha_status(session=None):
    _, body = waha_try("GET", f"/sessions/{session or WAHA_SESSION}")
    return body if isinstance(body, dict) else {}


def waha_start(session=None):
    """Start (creating first if needed) a WAHA session, across API versions."""
    name = session or WAHA_SESSION
    attempts = []

    st = waha_status(name)
    if st.get("status") == "WORKING":
        return {"session": name, "status": "WORKING", "action": "none",
                "message": "Session was already connected.", "me": st.get("me")}

    # NOWEB keeps no message store unless switched on at CREATE time -- without this,
    # whatsapp_get_messages 400s and re-pairing does not fix it. WAHA wants camelCase
    # "fullSync" here and silently drops "full_sync" despite its own error text.
    config = {"noweb": {"store": {"enabled": True, "fullSync": True}}}

    for label, method, endpoint, payload in [
        ("start", "POST", f"/sessions/{name}/start", {}),
        ("legacy_start", "POST", "/sessions/start", {"name": name, "config": config}),
        ("create", "POST", "/sessions", {"name": name, "start": True, "config": config}),
    ]:
        code, _ = waha_try(method, endpoint, payload)
        attempts.append({"route": label, "status_code": code})
        if code in (200, 201):
            break

    final = waha_status(name)
    status = final.get("status", "UNKNOWN")
    return {
        "session": name,
        "status": status,
        "me": final.get("me"),
        "attempts": attempts,
        "next_step": (
            "Connected." if status == "WORKING"
            else "Scan the QR: call whatsapp_get_qr, or open the WAHA dashboard, then on "
                 "the phone WhatsApp > Settings > Linked devices > Link a device."
            if status in ("SCAN_QR_CODE", "STARTING")
            else "Session did not reach WORKING. Check the WAHA service logs."
        ),
    }


# ----------------------------------------------------------------- chat helpers
def _chat_id(chat: str) -> str:
    """Normalise anything the caller might pass into a WAHA chatId.

    Accepts a bare phone number, a group id, or an already-qualified JID. WhatsApp
    phone numbers top out at 15 digits, so a longer id (or one with the `-` of a
    legacy group id) is a group and belongs on `@g.us`, not `@c.us`.
    """
    c = (chat or "").strip()
    if "@" in c:
        return c
    digits = re.sub(r"[^\d-]", "", c)
    if not digits:
        return c
    if "-" in digits or len(digits) > 15:
        return f"{digits}@g.us"
    return f"{digits}@c.us"


def _iso(ts):
    try:
        return datetime.fromtimestamp(int(ts), tz=timezone.utc).isoformat()
    except Exception:
        return None


def _flat_id(value):
    """WAHA returns ids as a plain string (NOWEB) or {_serialized: ...} (WEBJS)."""
    if isinstance(value, dict):
        return value.get("_serialized") or value.get("id") or value.get("user")
    return value


def _slim_message(m):
    """Drop WAHA's `_data` blob, keeping only what triage actually reads.

    A raw message is ~40 lines of protocol envelope around one line of text; pulling
    a few chats at full fidelity would burn the context this is meant to save.
    """
    if not isinstance(m, dict):
        return m
    data = m.get("_data") if isinstance(m.get("_data"), dict) else {}
    key = data.get("key") if isinstance(data.get("key"), dict) else {}
    out = {
        "id": m.get("id"),
        "timestamp": m.get("timestamp"),
        "time": _iso(m.get("timestamp")),
        "fromMe": m.get("fromMe"),
        "from": _flat_id(m.get("from")),
        "body": m.get("body"),
    }
    # In a group, `from` is the group -- the human is `participant`.
    participant = _flat_id(m.get("participant") or key.get("participant"))
    if participant:
        out["participant"] = participant
    sender = m.get("notifyName") or data.get("pushName")
    if sender:
        out["senderName"] = sender
    if m.get("hasMedia"):
        out["hasMedia"] = True
        media = m.get("media") or {}
        if isinstance(media, dict) and media.get("mimetype"):
            out["mediaType"] = media.get("mimetype")
    reply_to = m.get("replyTo")
    if isinstance(reply_to, dict):
        out["replyTo"] = {"id": reply_to.get("id"), "body": reply_to.get("body")}
    return {k: v for k, v in out.items() if v is not None}


def _slim_chat(c):
    if not isinstance(c, dict):
        return {"id": c}
    cid = _flat_id(c.get("id")) or _flat_id(c.get("chatId"))
    name = (
        c.get("name")
        or c.get("subject")
        or (c.get("groupMetadata") or {}).get("subject")
        or c.get("pushName")
        or c.get("notifyName")
    )
    out = {"id": cid, "name": name, "isGroup": bool(cid and str(cid).endswith("@g.us"))}
    last = c.get("lastMessage")
    if isinstance(last, dict):
        out["lastMessage"] = _slim_message(last)
        ts = last.get("timestamp")
        if ts:
            out["lastMessageAt"] = _iso(ts)
    elif c.get("timestamp"):
        out["lastMessageAt"] = _iso(c.get("timestamp"))
    return out


def _collect_chats(session, limit, force_groups=False):
    """Pull the chat list, tolerating WAHA's several shapes of chat endpoint.

    `force_groups` also queries the groups route and merges it in, for the case where
    the chat list came back fine but simply did not carry the group being looked for.
    """
    chats, tried = [], []
    seen = set()

    def absorb(body):
        added = 0
        items = body if isinstance(body, list) else (body or {}).get("data")
        if not isinstance(items, list):
            return 0
        for item in items:
            slim = _slim_chat(item)
            if slim.get("id") and slim["id"] in seen:
                continue
            if slim.get("id"):
                seen.add(slim["id"])
            chats.append(slim)
            added += 1
        return added

    for label, endpoint, params in [
        ("overview", f"/{session}/chats/overview", {"limit": limit, "offset": 0}),
        ("chats", f"/{session}/chats", {"limit": limit, "offset": 0}),
        ("legacy_chats", "/chats", {"session": session, "limit": limit}),
        ("groups", f"/{session}/groups", {"limit": limit, "offset": 0}),
    ]:
        # `groups` is the last resort: engines differ on whether groups appear in the
        # chat list at all, so it is only queried when nothing else produced them.
        if label == "groups" and chats and not force_groups:
            break
        code, body = waha_try("GET", endpoint, params=params)
        tried.append({"route": label, "status_code": code})
        if code == 200:
            absorb(body)
            if label != "groups" and chats and not force_groups:
                break
    return chats, tried


def _resolve_chat(chat, session):
    """Turn whatever `chat` is into a chatId. Returns (chat_id, name, candidates).

    An id or phone number passes straight through. A name is looked up, so a caller
    who only knows a chat by its title does not have to list chats first. Ambiguity is
    handed back as candidates rather than guessed at -- picking the wrong chat here
    means reading, or worse replying into, the wrong conversation.
    """
    c = (chat or "").strip()
    if not c:
        return None, None, []
    if "@" in c or re.fullmatch(r"[\d\-+ ]+", c):
        return _chat_id(c), None, []

    chats, _ = _collect_chats(session, 200, force_groups=True)
    q = c.lower()
    exact = [x for x in chats if str(x.get("name") or "").lower() == q]
    hits = exact or [x for x in chats if q in str(x.get("name") or "").lower()]
    if len(hits) == 1:
        return hits[0].get("id"), hits[0].get("name"), []
    return None, None, hits


# --------------------------------------------------------------------------- MCP tools
mcp = FastMCP("whatsapp", host="0.0.0.0", port=PORT)


@mcp.tool()
def whatsapp_check_session(session: str = "") -> dict:
    """Check if the WhatsApp session is active and authenticated (status WORKING)."""
    return waha_status(session or None)


@mcp.tool()
def whatsapp_start_session(session: str = "") -> dict:
    """Start the WhatsApp session (creates it if missing). SCAN_QR_CODE means a human
    must scan a QR from the phone (use whatsapp_get_qr). Call this first whenever another
    WhatsApp tool fails with a session-status error."""
    return waha_start(session or None)


@mcp.tool()
def whatsapp_restart_session(session: str = "") -> dict:
    """Restart the session (stop then start). Use when stuck in STARTING or FAILED."""
    target = session or WAHA_SESSION
    code, _ = waha_try("POST", f"/sessions/{target}/stop", {})
    if code not in (200, 201):
        waha_try("POST", "/sessions/stop", {"name": target})
    return waha_start(target)


@mcp.tool()
def whatsapp_get_qr(session: str = "") -> dict:
    """Get the pairing QR for a session in SCAN_QR_CODE state so it can be linked to the
    phone. A QR only exists while the session is in SCAN_QR_CODE; run whatsapp_start_session
    first. Expires in ~60s -- call again for a fresh one."""
    target = session or WAHA_SESSION
    code, body = waha_try("GET", f"/{target}/auth/qr", params={"format": "raw"})
    if code != 200:
        code, body = waha_try("GET", "/screenshot", params={"session": target})
    if code != 200:
        return {
            "error": "Could not retrieve a QR code.",
            "status_code": code,
            "detail": body,
            "session_status": waha_status(target).get("status"),
            "hint": "A QR only exists in SCAN_QR_CODE state. Run whatsapp_start_session first, "
                    "or open the WAHA dashboard and scan there.",
        }
    return {
        "session": target,
        "qr": body,
        "instructions": "On the phone: WhatsApp > Settings > Linked devices > Link a device, "
                        "then scan this code. Expires in ~60s.",
    }


@mcp.tool()
def whatsapp_send_message(phone: str, message: str) -> dict:
    """Send a WhatsApp text message. `phone` is digits only, country code first, no + or
    spaces (e.g. 2348012345678)."""
    return waha_request_json("POST", "/sendText", {
        "session": WAHA_SESSION,
        "chatId": _chat_id(phone),
        "text": message,
    })


@mcp.tool()
def whatsapp_get_messages(phone: str, limit: int = 10, download_media: bool = False) -> dict:
    """Read recent messages from a 1:1 chat, raw. `phone` is digits only, country code
    first. For groups, communities, or a chat you only know by name, use
    whatsapp_get_chat_messages instead -- it takes any chat id and returns far less noise."""
    return waha_request_json("GET", "/messages", params={
        "session": WAHA_SESSION,
        "chatId": _chat_id(phone),
        "limit": limit,
        "downloadMedia": download_media,
    })


@mcp.tool()
def whatsapp_list_chats(query: str = "", limit: int = 100, session: str = "") -> dict:
    """List chats -- 1:1, groups and community groups -- with their ids, so a chat known
    only by name can be resolved to the id the other tools need. `query` filters by name
    (case-insensitive substring); leave it empty to see everything. Resolve a name once and
    reuse the id: this scans the whole chat list, the message tools do not."""
    target = session or WAHA_SESSION
    chats, tried = _collect_chats(target, max(limit, 100))
    if not chats:
        return {"session": target, "chats": [], "attempts": tried,
                "hint": "No chats came back. Check the session is WORKING "
                        "(whatsapp_check_session) and that its store is enabled."}

    q = (query or "").strip().lower()
    if not q:
        return {"session": target, "count": len(chats), "chats": chats[:limit]}

    def match(items):
        return [c for c in items
                if q in str(c.get("name") or "").lower()
                or q in str(c.get("id") or "").lower()]

    matches = match(chats)
    if not matches:
        # The name may be a group the chat list left out -- ask for groups explicitly.
        chats, tried = _collect_chats(target, max(limit, 100), force_groups=True)
        matches = match(chats)
    out = {"session": target, "query": query, "count": len(matches), "chats": matches[:limit]}
    if not matches:
        out["hint"] = "No name matched. Try a shorter or different fragment."
        out["available_names"] = sorted(
            {str(c.get("name")) for c in chats if c.get("name")}
        )[:100]
    return out


@mcp.tool()
def whatsapp_get_chat_messages(chat: str, limit: int = 25, since_epoch: int = 0,
                               since: int = 0, include_raw: bool = False,
                               download_media: bool = False, session: str = "") -> dict:
    """Read recent messages from ANY chat -- 1:1, group, or community group.

    `chat` takes a chat NAME, a phone number, a group id, or a full JID. A name that
    matches several chats comes back as `candidates` to choose from, rather than being
    guessed at. `since_epoch` is a unix timestamp in seconds: pass the `next_cursor`
    from the previous call to fetch only what arrived since, or 0 for the most recent
    messages. Output is trimmed to sender/time/body; set `include_raw` for full payloads."""
    target = session or WAHA_SESSION
    cutoff = int(since_epoch or since or 0)

    chat_id, chat_name, candidates = _resolve_chat(chat, target)
    if not chat_id:
        if candidates:
            return {"session": target, "query": chat, "needs_disambiguation": True,
                    "candidates": [{"id": c.get("id"), "name": c.get("name"),
                                    "isGroup": c.get("isGroup")} for c in candidates[:20]],
                    "hint": "Several chats match that name. Call again with the `id` of "
                            "the one you want."}
        return {"session": target, "query": chat,
                "error": f"No chat matched {chat!r}.",
                "hint": "Try a shorter fragment, run whatsapp_list_chats to see the "
                        "names, or check whether the chat is on another session."}

    params = {"limit": limit, "downloadMedia": download_media}
    if cutoff:
        params["filter.timestamp.gte"] = cutoff

    code, body = waha_try("GET", f"/{target}/chats/{chat_id}/messages", params=params)
    if code != 200:
        legacy = {"session": target, "chatId": chat_id, "limit": limit,
                  "downloadMedia": download_media}
        if cutoff:
            legacy["filter.timestamp.gte"] = cutoff
        code, body = waha_try("GET", "/messages", params=legacy)
    if code != 200:
        return {"error": f"WAHA returned {code}", "chatId": chat_id, "detail": body,
                "hint": "Check the id with whatsapp_list_chats; if this is a session-status "
                        "error, run whatsapp_start_session."}

    items = body if isinstance(body, list) else (body or {}).get("data") or []
    if not isinstance(items, list):
        items = []
    # WAHA versions differ on whether they honour the timestamp filter, so enforce it here.
    if cutoff:
        items = [m for m in items
                 if isinstance(m, dict) and int(m.get("timestamp") or 0) > cutoff]
    items.sort(key=lambda m: int((m or {}).get("timestamp") or 0))

    messages = items if include_raw else [_slim_message(m) for m in items]
    newest = max((int((m or {}).get("timestamp") or 0) for m in items), default=cutoff)
    out = {
        "session": target,
        "chatId": chat_id,
        "count": len(messages),
        # Feed this straight back as `since_epoch` next time.
        "next_cursor": newest,
        "messages": messages,
    }
    if chat_name:
        out["chatName"] = chat_name
    return out


@mcp.tool()
def whatsapp_list_sessions() -> dict:
    """List every WhatsApp session known to WAHA and its status."""
    _, body = waha_try("GET", "/sessions", params={"all": "true"})
    return body


def waha_request_json(method, endpoint, data=None, params=None):
    code, body = waha_try(method, endpoint, data=data, params=params)
    if code not in (200, 201):
        return {"error": f"WAHA returned {code}", "detail": body,
                "hint": "If this is a session-status error, run whatsapp_start_session."}
    return body


# --------------------------------------------------------------------------- auth + run
def main():
    app = mcp.streamable_http_app()

    if GATEWAY_KEY:
        from starlette.middleware.base import BaseHTTPMiddleware

        async def require_key(request, call_next):
            # Let OPTIONS preflight through; guard the MCP endpoint.
            if request.method != "OPTIONS" and request.url.path.rstrip("/").endswith("/mcp"):
                if request.headers.get("x-api-key") != GATEWAY_KEY:
                    return JSONResponse({"error": "unauthorized"}, status_code=401)
            return await call_next(request)

        app.add_middleware(BaseHTTPMiddleware, dispatch=require_key)

    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=PORT)


if __name__ == "__main__":
    main()
