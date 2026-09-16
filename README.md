# Claude-Config

Configuration for connecting Claude to external services.

## WhatsApp connector

Two services on Railway put WhatsApp behind an MCP connector Claude can call:

```
Your phone  <--QR-->  WAHA  <--HTTP-->  Gateway (this repo)  <--MCP-->  Claude
```

- `gateway/server.py` — the MCP gateway (wraps WAHA's HTTP API as Claude tools)
- `Procfile` / `requirements.txt` at the repo root — so Railway deploys this repo
  with no extra settings; both just point into `gateway/`
- `.mcp.json.example` — how Claude Code connects if you self-host. Copy it to
  `.mcp.json` once the gateway is deployed; it reads `GATEWAY_URL` and `GATEWAY_KEY`
  from the environment, so **no secret is ever committed here**. It is kept as
  `.example` so an unset `GATEWAY_URL` doesn't throw a config error every session.
- `SETUP.md` — the full walkthrough, including troubleshooting
- `CLOUD-NOTES.md` — extra steps that apply when driving this from a Claude Code
  cloud session (egress allowlist, in particular)

### Deploy checklist

1. **WAHA** — Railway → New Project → Deploy a Docker Image → `devlikeapro/waha`.
   Variables: `WAHA_API_KEY`, `WHATSAPP_DEFAULT_ENGINE=NOWEB`. Generate a domain.
2. **Gateway** — Railway → New → Deploy from GitHub repo → this repo.
   Under **Settings → Source**, set the branch to `claude/fervent-darwin-wmmctg`
   (this repo has no `main`).
   Variables: `WAHA_URL`, `WAHA_API_KEY` (same value as step 1), `WAHA_SESSION=default`,
   `GATEWAY_KEY`. Generate a domain.
3. **Pair** — open the WAHA domain, start the `default` session, scan the QR from
   WhatsApp → Settings → Linked devices.
4. **Connect Claude** — set `GATEWAY_URL` and `GATEWAY_KEY` as environment variables
   where Claude runs, then the `whatsapp` server in `.mcp.json` comes up automatically.

Verified locally: the gateway boots, rejects requests without the `x-api-key`
header (401), completes the MCP handshake, and lists its tools.

Tools exposed: `whatsapp_check_session`, `whatsapp_start_session`,
`whatsapp_restart_session`, `whatsapp_get_qr`, `whatsapp_send_message`,
`whatsapp_get_messages`, `whatsapp_list_sessions`, `whatsapp_list_chats`,
`whatsapp_get_chat_messages`.

`whatsapp_list_chats` resolves a chat *name* to the id the other tools need, and
`whatsapp_get_chat_messages` reads any chat — 1:1, group, or community group — and
strips WAHA's protocol envelope so a catch-up costs a fraction of the context.
The older `whatsapp_get_messages` stays as-is for raw 1:1 reads.

## Skills

`.claude/skills/whatsapp-triage/` — checks the tracked WhatsApp chats and reports the
tasks in them. It resolves each chat name to an id once (cached in `chats.json`), then
fetches only messages newer than the last run (`state.json`, gitignored). Ask Claude to
"check WhatsApp" in a session started from this repo. To use it from anywhere, copy the
directory to `~/.claude/skills/whatsapp-triage`.

Edit `chats.json` to follow a different set of chats — or let the skill do it with
`scripts/wa.py add`.
