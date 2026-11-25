---
title: Claude account, projects and cloud sessions
version: v1.0
last_updated: 2026-11-25
owner: Adeyinka Oshin
---

# 01 — Claude account, projects and cloud sessions

> Start here if you have never used Claude for this work. By the end you will have
> a Claude account on the VGG organisation, know the three places Claude is used
> (chat, Projects, Claude Code), and be able to start a cloud session on a GitHub repo.

## 1. Get the right account

1. Ask the VGG Claude admin to invite your **work email** to the VGG organisation on
   claude.ai. **[TO CONFIRM: who is the org admin today, and which plan (Team / Enterprise)?]**
2. Accept the invite email and sign in at <https://claude.ai>.
3. Check your plan includes **Claude Code** (needed for cloud sessions, routines and
   repo-based skills). Pro, Max, Team and Enterprise all include it.
4. In **Settings → Profile**, set your name and role so Claude has basic context.

## 2. The three places you will use Claude

| Where | What it is | Used for in this job |
|---|---|---|
| **claude.ai chat** | Normal chat. Account skills and connectors are available. | Quick drafts, running skills such as `/calendar-qa` or `/meeting-artifacts` by hand. |
| **claude.ai Projects** | A chat space with saved files and instructions. Every chat in the project sees them. | Favour's "Favour Calendar Management" project (Calendar Brief, context file, CT bibles). **[TO CONFIRM: list of other projects in use]** |
| **Claude Code (cloud)** at <https://claude.ai/code> | Claude working inside a copy of a GitHub repo, in a container in the cloud. Can read/write files, commit and push. | Everything in the `Logan-VGG` repo: `/ops-runway`, Station, judgment, work requests. Also this handover pack. |

Claude Code also exists as a desktop app (Mac/Windows, **Code** tab) and a terminal CLI.
The cloud version is the one used here because it runs with the laptop closed.

## 3. Start a cloud session on a repo

1. Connect GitHub first — see [`02-github-setup.md`](02-github-setup.md).
2. Go to <https://claude.ai/code>.
3. Pick the **repository** (e.g. `logansherzog/Logan-VGG` or `AdeyinkaOshin/Claude-Config`).
4. Pick the **environment** (see section 4). "Default" is fine to start.
5. Type what you want, e.g. `/ops-runway` or "update the handover docs".
6. Claude works on its own branch named `claude/<something>`. It commits and pushes
   there; it never pushes to `main` unless told to.

Things to know about cloud sessions:

- The container is **temporary**. Anything not committed and pushed is lost when the
  session ends. Always ask Claude to "commit and push" before you leave.
- Claude reads the repo's `CLAUDE.md` at the start of every session — that is how
  repo rules travel with the repo. See [`05-claude-md-files.md`](05-claude-md-files.md).
- Connectors you have turned on in claude.ai are available in the session too
  (subject to the environment's network rules).

## 4. Environments (network + secrets)

Each cloud session runs in an **environment** that controls:

- **Network access** — which websites the container may reach. Anything not allowed
  fails with a `403` from the proxy. This is why the WhatsApp gateway domain had to be
  added to the allowlist (see [`04-whatsapp-connector.md`](04-whatsapp-connector.md)).
- **Environment variables / secrets** — e.g. `GATEWAY_URL`, `GATEWAY_KEY`. Set these in
  the environment settings, **never** commit them to a repo.
- **Setup script** — commands that run when the container starts.

Change these at claude.ai/code → environment settings. **Changes only apply to new
sessions** — start a fresh session after editing.

## 5. Permissions and safety habits

- Claude asks before risky actions. Read the prompt before clicking Allow.
- House rule across every skill in this job: **Claude drafts, a human sends.** Claude
  never sends email/WhatsApp, books, moves or cancels meetings on its own.
- For Logan's repo, also read the sender-choice and publicity rules in its `CLAUDE.md`.

## 6. Checklist — you are set up when

- [ ] You can sign in to claude.ai with your work account
- [ ] You can open claude.ai/code and see the VGG repos in the picker
- [ ] You can see the account skills when you type `/` in a chat (see `../03-reference/skills-inventory.md`)
- [ ] You have opened the Favour Calendar Management project **[TO CONFIRM: access is granted by whom?]**

## Change history
| Version | Date | Change |
|---|---|---|
| v1.0 | 2026-11-25 | First written |
