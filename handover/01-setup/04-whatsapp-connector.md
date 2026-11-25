---
title: WhatsApp connector
version: v1.0
last_updated: 2026-11-25
owner: Adeyinka Oshin
sources: Claude-Config/SETUP.md, Claude-Config/CLOUD-NOTES.md, Claude-Config/README.md
---

# 04 — WhatsApp connector

> WhatsApp has no official Claude connector. We run two small services on
> **Railway** that make it look like one. This page is the summary; the full,
> tested walkthrough is in [`../../SETUP.md`](../../SETUP.md) and the cloud-specific
> gotchas are in [`../../CLOUD-NOTES.md`](../../CLOUD-NOTES.md).

```
Phone  <--QR-->  WAHA (WhatsApp engine)  <--HTTP-->  Gateway (gateway/server.py)  <--MCP-->  Claude
```

## 1. What you need

- The phone with the WhatsApp number Claude will act as
- A Railway account (sign in with GitHub). **[TO CONFIRM: whose Railway account /
  billing? Handover must transfer it.]**
- Access to the `Claude-Config` repo

## 2. Steps (summary)

1. **Deploy WAHA** — Railway → New Project → Deploy a Docker Image → `devlikeapro/waha`.
   Variables: `WAHA_API_KEY` (long random string), `WHATSAPP_DEFAULT_ENGINE=NOWEB`.
   Settings → Networking → Generate Domain → this is `WAHA_URL`.
2. **Deploy the gateway** — Railway → New → Deploy from GitHub repo → `Claude-Config`.
   Settings → Source → branch `claude/fervent-darwin-wmmctg` (the repo has no `main`).
   Variables: `WAHA_URL`, `WAHA_API_KEY` (same as step 1), `WAHA_SESSION=default`,
   `GATEWAY_KEY` (a second random string). Generate Domain → this is `GATEWAY_URL`.
   Generate keys with: `python3 -c "import secrets; print(secrets.token_hex(24))"`
3. **Pair the phone** — open `WAHA_URL`, start session `default`, Link with QR code.
   On the phone: WhatsApp → Settings → Linked devices → Link a device → scan.
   (Use the dashboard, not `whatsapp_get_qr` — that returns text, not a scannable image.)
4. **Connect Claude**
   - Cloud session / Claude Code: copy `.mcp.json.example` to `.mcp.json`; set
     `GATEWAY_URL` and `GATEWAY_KEY` as **environment variables** in the environment settings.
   - Cloud only: add both Railway domains to the environment **network allowlist**.
     Start a fresh session afterwards.
5. **Verify** — ask Claude: "Check my WhatsApp session" → `WORKING`. Then send a test
   message to your own number (approve it first), and read the last 5 messages back.

## 3. Tools Claude gets

`whatsapp_check_session`, `whatsapp_start_session`, `whatsapp_restart_session`,
`whatsapp_get_qr`, `whatsapp_list_chats`, `whatsapp_get_chat_messages`,
`whatsapp_get_messages`, `whatsapp_list_sessions`, `whatsapp_send_message`.

## 4. Running costs and upkeep

- WAHA must run **continuously**. If it sleeps, the phone unlinks and you re-pair. Use a
  Railway plan that stays up — this is the one recurring cost.
- WhatsApp unlinks devices if the phone is offline too long. Keep the phone online.

## 5. Troubleshooting (short)

| Symptom | Fix |
|---|---|
| Tools missing / 403 at the proxy | Domain not on the environment allowlist, or no fresh session since adding it |
| 401 unauthorized | `x-api-key` header doesn't match `GATEWAY_KEY` |
| Session `STARTING` / `FAILED` | `whatsapp_restart_session`; then check WAHA logs in Railway |
| 400 about the message store | `whatsapp_restart_session` (recreates with store on) |
| Phone unlinked | Re-pair from the WAHA dashboard |

## 6. Rules

- Claude shows the exact message and waits for a yes before any send.
- It's WhatsApp Web under the hood — no bulk or cold messaging, or the number gets flagged.
- Keys live only in Railway and environment settings. Never in the repo, never in chat.

## Change history
| Version | Date | Change |
|---|---|---|
| v1.0 | 2026-11-25 | First written from SETUP.md + CLOUD-NOTES.md |
