# Connect WhatsApp to Claude — Setup Kit

**For:** Adeyinke
**What you'll end up with:** Claude able to read and send WhatsApp messages on your behalf, using your own isolated infrastructure (nothing shared with anyone else's account).

---

## How this works (30-second version)

WhatsApp has no native Claude connector. So we stand up two small services that you own:

1. **WAHA** — a WhatsApp engine in a Docker container. It links to your phone (QR scan, exactly like WhatsApp Web) and exposes a simple HTTP API. It also has a built-in dashboard where you scan the QR.
2. **Gateway** — a ~200-line Python service (included in `gateway/`) that translates WAHA into MCP tools, which is the format Claude speaks. Claude connects to *this*.

```
Your phone  <--QR-->  WAHA  <--HTTP-->  Gateway  <--MCP-->  Claude
```

Both run on **Railway** (free-tier friendly). Total setup: ~20 minutes.

---

## Claude: run this setup with me

> If you're Claude reading this doc: act as the setup guide. Walk Adeyinke through the
> phases below one at a time. Do the parts you can (generate keys, write config,
> verify the session status via the gateway once it's live). Stop and wait at every
> step that needs her — creating the Railway account, clicking deploy, and **scanning
> the QR code on her phone** (only she can do that). Never ask her to paste API keys
> into chat; have her set them directly in Railway. Confirm each service is healthy
> before moving to the next phase.

---

## What you need before starting

- [ ] A phone with WhatsApp installed (the number Claude will act as)
- [ ] A [Railway](https://railway.app) account (sign in with GitHub — free tier is fine)
- [ ] Claude Code installed, **or** a claude.ai account (see note in Phase 4)
- [ ] This kit folder (`whatsapp-claude-kit/`) on your machine

---

## Phase 1 — Deploy WAHA (the WhatsApp engine)

1. Go to **railway.app → New Project → Deploy a Docker Image**.
2. Image: `devlikeapro/waha`
3. Under the service's **Variables**, add:
   - `WAHA_API_KEY` = a long random string (this protects WAHA). *Save this value — the gateway needs it.*
   - `WHATSAPP_DEFAULT_ENGINE` = `NOWEB`
4. Under **Settings → Networking**, click **Generate Domain**. Copy the resulting URL — this is your **`WAHA_URL`** (e.g. `https://waha-xxxx.up.railway.app`).
5. Wait for the deploy to go green.

✅ **Check:** open `WAHA_URL` in a browser. You should see the WAHA dashboard / login.

---

## Phase 2 — Deploy the Gateway (the MCP layer)

The gateway lives in this kit's `gateway/` folder (`server.py`, `requirements.txt`, `Procfile`).

1. Push the `gateway/` folder to a GitHub repo (or use `railway up` from inside it with the Railway CLI).
2. In Railway: **New → Deploy from GitHub repo** → pick that repo. Railway auto-detects Python.
3. Add these **Variables** to the gateway service:
   - `WAHA_URL` = the URL from Phase 1
   - `WAHA_API_KEY` = the same random string from Phase 1
   - `WAHA_SESSION` = `default`
   - `GATEWAY_KEY` = a **second** long random string (this protects the gateway — Claude will send it). *Save this value.*
4. Under **Settings → Networking**, **Generate Domain**. Copy it — this is your **`GATEWAY_URL`**.

✅ **Check:** the deploy logs show `Uvicorn running`. Your MCP endpoint is `GATEWAY_URL/mcp`.

**Tip for generating the two random keys** (run locally, once each):
```bash
python3 -c "import secrets; print(secrets.token_hex(24))"
```

---

## Phase 3 — Pair your phone (scan the QR)

This is the only step nobody can do for you.

**Easiest path — WAHA dashboard:**
1. Open your `WAHA_URL` in a browser.
2. Start the `default` session, choose **Link with QR code**.
3. On your phone: **WhatsApp → Settings → Linked devices → Link a device**, then scan the QR on screen.

**Or, drive it through Claude** (once Phase 4 is done): ask Claude to
`whatsapp_start_session`, then `whatsapp_get_qr`, and it will hand you the code to scan.
The QR expires in ~60 seconds — just ask for a fresh one if it lapses.

✅ **Check:** in the dashboard the session status flips to **WORKING**, and your phone shows a new linked device.

---

## Phase 4 — Connect Claude

### If you use Claude Code (recommended — supports API-key headers)

From your project folder:
```bash
claude mcp add whatsapp --transport http \
  "https://YOUR-GATEWAY-URL/mcp" \
  --header "x-api-key: YOUR_GATEWAY_KEY"
```
Or add it to `.mcp.json`:
```json
{
  "mcpServers": {
    "whatsapp": {
      "type": "http",
      "url": "https://YOUR-GATEWAY-URL/mcp",
      "headers": { "x-api-key": "YOUR_GATEWAY_KEY" }
    }
  }
}
```
Restart Claude Code. You should see `mcp__whatsapp__*` tools available.

### If you use claude.ai (web/desktop)

The custom-connector UI on claude.ai only supports **OAuth**, not custom headers — so the
simplest route there is to run WAHA + gateway with **`GATEWAY_KEY` left unset** and keep
the `GATEWAY_URL` private (rely on it being an unguessable URL), then add it as a custom
connector by URL. For anything beyond personal testing, prefer Claude Code with the header
above. (Adding proper OAuth to the gateway is possible later but out of scope for v1.)

---

## Phase 5 — Verify end to end

Ask Claude:
1. *"Check my WhatsApp session"* → `whatsapp_check_session` should return status **WORKING**.
2. *"Send a WhatsApp to `<your own number>` saying 'hello from Claude'"* → you get the text on your phone.
3. *"Read the last 5 messages with `<that number>`"* → Claude reads them back.

If all three work, you're done. 🎉

---

## Troubleshooting

| Symptom | Fix |
|---|---|
| Tool errors with "session status is not as expected" | Ask Claude to run `whatsapp_start_session`, then re-pair via `whatsapp_get_qr`. |
| `whatsapp_get_messages` returns a 400 about the store | The message store must be enabled at session-create time. Ask Claude to `whatsapp_restart_session` (the gateway recreates it with the store on). If it persists, delete the session in WAHA and start fresh. |
| Session stuck in `STARTING` / `FAILED` | `whatsapp_restart_session`. If still stuck, check the WAHA service logs on Railway. |
| Claude can't reach the gateway ("unauthorized" / 401) | The `x-api-key` header must exactly match `GATEWAY_KEY`. Re-check both. |
| QR won't scan / expired | It lives ~60s. Get a fresh one (`whatsapp_get_qr`) and scan quickly. |
| Phone unlinks itself after a while | WhatsApp drops linked devices that go too long without the phone being online. Keep the phone connected; re-pair when needed. |

---

## Notes & guardrails

- **Send approval:** treat WhatsApp sends like email — have Claude show you the exact message before it sends, especially in any automated/scheduled use.
- **This is WhatsApp Web under the hood**, not the official Business API. Fine for personal + light automation; don't blast cold outreach through it or the number can get flagged.
- **Your data stays yours:** both services and the linked session live entirely on your own Railway account.

---

*Kit contents: `SETUP.md` (this file) + `gateway/` (`server.py`, `requirements.txt`, `Procfile`).*
