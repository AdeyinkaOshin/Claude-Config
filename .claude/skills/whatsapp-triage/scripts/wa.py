#!/usr/bin/env python3
"""Registry + cursor bookkeeping for the whatsapp-triage skill.

Keeps two files side by side in the skill directory:
  chats.json  - the tracked chats and their resolved WhatsApp ids (committed)
  state.json  - the last-seen timestamp per chat (local only, gitignored)

Splitting them means the expensive thing (resolving a chat name to an id) is
cached in git, while the per-run cursor stays out of the history.

Usage:
  wa.py plan                    what to fetch this run: id + `since_epoch` per chat
  wa.py resolve <key> <id> [--session S] [--label L]
  wa.py mark <key> <timestamp>  record the newest message seen for a chat
  wa.py add <key> <label> <match>
  wa.py reset [key]             forget cursors (all, or one chat)
"""
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHATS = os.path.join(HERE, "chats.json")
STATE = os.path.join(HERE, "state.json")


def load(path, default):
    try:
        with open(path) as f:
            return json.load(f)
    except FileNotFoundError:
        return default
    except json.JSONDecodeError as e:
        sys.exit(f"{path} is not valid JSON: {e}")


def save(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
        f.write("\n")


def registry():
    return load(CHATS, {"version": 1, "default_lookback_hours": 24, "chats": []})


def find(reg, key):
    for c in reg["chats"]:
        if c.get("key") == key:
            return c
    sys.exit(f"No chat with key {key!r}. Known keys: "
             + ", ".join(c.get("key", "?") for c in reg["chats"]))


def cmd_plan():
    reg = registry()
    state = load(STATE, {})
    lookback = int(reg.get("default_lookback_hours", 24)) * 3600
    floor = int(time.time()) - lookback
    plan = []
    for c in reg["chats"]:
        cursor = (state.get(c["key"]) or {}).get("last_timestamp")
        plan.append({
            "key": c["key"],
            "label": c.get("label"),
            "match": c.get("match"),
            "id": c.get("id"),
            "session": c.get("session"),
            "needs_resolve": not c.get("id"),
            # No cursor yet (first run, or fresh container) -> fall back to the
            # lookback window rather than dragging in the whole history.
            "since_epoch": cursor if cursor else floor,
            "since_source": "cursor" if cursor else "lookback",
            "limit": int(reg.get("max_messages_per_chat", 40)),
        })
    print(json.dumps({"plan": plan, "now": int(time.time())}, indent=2))


def cmd_resolve(key, chat_id, session=None, label=None):
    reg = registry()
    chat = find(reg, key)
    chat["id"] = chat_id
    if session:
        chat["session"] = session
    if label:
        chat["label"] = label
    save(CHATS, reg)
    print(f"{key} -> {chat_id}")


def cmd_mark(key, ts):
    """`ts` is the `next_cursor` the message tool handed back."""
    reg = registry()
    find(reg, key)
    state = load(STATE, {})
    ts = int(ts)
    prev = (state.get(key) or {}).get("last_timestamp") or 0
    state[key] = {"last_timestamp": max(ts, int(prev)), "checked_at": int(time.time())}
    save(STATE, state)
    print(f"{key} cursor -> {state[key]['last_timestamp']}")


def cmd_add(key, label, match):
    reg = registry()
    if any(c.get("key") == key for c in reg["chats"]):
        sys.exit(f"{key!r} is already tracked.")
    reg["chats"].append({"key": key, "label": label, "match": match,
                         "id": None, "session": None, "notes": ""})
    save(CHATS, reg)
    print(f"tracking {key} ({label})")


def cmd_reset(key=None):
    state = load(STATE, {})
    if key:
        state.pop(key, None)
    else:
        state = {}
    save(STATE, state)
    print("cursors reset" + (f" for {key}" if key else ""))


def main():
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    cmd, rest = args[0], args[1:]
    if cmd == "plan":
        cmd_plan()
    elif cmd == "resolve":
        if len(rest) < 2:
            sys.exit("usage: wa.py resolve <key> <id> [--session S] [--label L]")
        opts = {}
        i = 2
        while i < len(rest) - 1:
            if rest[i] in ("--session", "--label"):
                opts[rest[i].lstrip("-")] = rest[i + 1]
                i += 2
            else:
                i += 1
        cmd_resolve(rest[0], rest[1], opts.get("session"), opts.get("label"))
    elif cmd == "mark":
        if len(rest) != 2:
            sys.exit("usage: wa.py mark <key> <timestamp>")
        cmd_mark(rest[0], rest[1])
    elif cmd == "add":
        if len(rest) != 3:
            sys.exit("usage: wa.py add <key> <label> <match>")
        cmd_add(*rest)
    elif cmd == "reset":
        cmd_reset(rest[0] if rest else None)
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
