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

### Deploy checklist

1. **WAHA** — Railway → New Project → Deploy a Docker Image → `devlikeapro/waha`.
   Variables: `WAHA_API_KEY`, `WHATSAPP_DEFAULT_ENGINE=NOWEB`. Generate a domain.
2. **Gateway** — Railway → New → Deploy from GitHub repo → this repo.
   Variables: `WAHA_URL`, `WAHA_API_KEY` (same value as step 1), `WAHA_SESSION=default`,
   `GATEWAY_KEY`. Generate a domain.
3. **Pair** — open the WAHA domain, start the `default` session, scan the QR from
   WhatsApp → Settings → Linked devices.
4. **Connect Claude** — set `GATEWAY_URL` and `GATEWAY_KEY` as environment variables
   where Claude runs, then the `whatsapp` server in `.mcp.json` comes up automatically.

Tools exposed: `whatsapp_check_session`, `whatsapp_start_session`,
`whatsapp_restart_session`, `whatsapp_get_qr`, `whatsapp_send_message`,
`whatsapp_get_messages`, `whatsapp_list_sessions`.
