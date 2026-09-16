# Running this from a Claude Code cloud session

`SETUP.md` assumes claude.ai or a local machine. A Claude Code **cloud** session
differs in ways that will otherwise waste your time. Each item below was verified
in this repo or in a live cloud session — not taken on trust.

## 1. There is one gateway, `gateway/`

The kit ships exactly four files: `SETUP.md`, `gateway/server.py`,
`gateway/requirements.txt`, `gateway/Procfile`. There is **no `gateway-oauth/`**
and no OAuth, password-page, or `/qr` web-page code anywhere in it — the only
auth it has is the `x-api-key` header check in `server.py`.

If a document tells you to choose between `gateway/` and `gateway-oauth/`, it is
describing a different kit than this one. Check before acting on it.

## 2. Egress allowlist — the silent 403

Cloud sessions run behind a network egress proxy. Confirmed live: an outbound
request to a `*.up.railway.app` domain from this session fails with
`CONNECT tunnel failed, response 403`, and the proxy's own `noProxy` list covers
only package registries and internal ranges — no Railway.

So the gateway domain (and the WAHA domain, if you drive pairing through it) must
be added to the environment's egress allowlist under
claude.ai/code environment settings → networking.

**Allowlist changes need a fresh session.** If the `whatsapp` MCP server shows as
unreachable, or calls come back 403 *at the proxy*, that is the cause — not a bug
in the gateway.

This applies to the cloud only. The Claude Code desktop/CLI app talks to the
gateway directly and needs no allowlist entry.

## 3. Register the connector via `.mcp.json`

Copy `.mcp.json.example` to `.mcp.json`. It already uses `${GATEWAY_URL}` and
`${GATEWAY_KEY}`; set those as environment variables rather than committing the
literal key. Env expansion in `url` and `headers` is supported. Start a fresh
session for the `whatsapp_*` tools to load.

## 4. Pair the phone from the WAHA dashboard

`whatsapp_get_qr` calls WAHA with `format=raw`, so it returns the QR *payload as
text* — not something you can point a camera at. Pair from the WAHA dashboard
instead (`SETUP.md` Phase 3), then confirm with `whatsapp_check_session`.

## 5. WAHA must stay running

The phone stays linked only while the WAHA container runs continuously. If the
service sleeps, the device unlinks and you re-pair. Pick a Railway plan that
stays up — this is the one recurring cost in the stack.

## Done when

- WAHA green, session `default` = `WORKING`
- Gateway green, `/mcp` reachable, `x-api-key` enforced
- Both domains on the egress allowlist (cloud sessions only)
- `.mcp.json` present, fresh session shows the `whatsapp_*` tools
- A test message actually arrives on the phone
