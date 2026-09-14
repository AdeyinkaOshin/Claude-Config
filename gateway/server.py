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
        "chatId": f"{phone}@c.us",
        "text": message,
    })


@mcp.tool()
def whatsapp_get_messages(phone: str, limit: int = 10, download_media: bool = False) -> dict:
    """Read recent messages from a chat. `phone` is digits only, country code first."""
    return waha_request_json("GET", "/messages", params={
        "session": WAHA_SESSION,
        "chatId": f"{phone}@c.us",
        "limit": limit,
        "downloadMedia": download_media,
    })


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
