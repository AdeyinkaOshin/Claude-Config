---
title: Troubleshooting — quick index
version: v1.0
last_updated: 2026-11-25
owner: Adeyinka Oshin
---

# Troubleshooting — quick index

| Problem | Likely cause | Where to look |
|---|---|---|
| Skill doesn't appear when typing `/` | Not uploaded to this account, or upload failed | `../01-setup/06-creating-a-skill.md` |
| Skill runs an old version | claude.ai copy older than the repo copy | Re-upload the latest `.zip` — `06-creating-a-skill.md` §5 |
| Repo missing from claude.ai/code picker | GitHub not connected / Claude GitHub App not on repo | `../01-setup/02-github-setup.md` §4 |
| Push "permission denied" | Invite not accepted or read-only access | `02-github-setup.md` §3 |
| Connector "failed to connect", 403, `ERR_PROXY_TUNNEL` | Host not on the environment's network allowlist | `../01-setup/03-connectors.md` §4 |
| WhatsApp tools missing or session not WORKING | Allowlist, env vars, or phone unlinked | `../01-setup/04-whatsapp-connector.md` §5 |
| Routine stopped running | GitHub disconnected (routines pause 72h then turn off) | `../01-setup/07-scheduled-tasks-and-routines.md` §5 |
| Routine "succeeded" but nothing happened | Green = finished, not = did work | Open the run, read the last message |
| Work lost after a session | Not committed + pushed before container ended | Always end with "commit and push" |
| Claude wants to send/book something | It must not without a yes to the exact item | Say no; ask for a draft |

## Change history
| Version | Date | Change |
|---|---|---|
| v1.0 | 2026-11-25 | First written |
