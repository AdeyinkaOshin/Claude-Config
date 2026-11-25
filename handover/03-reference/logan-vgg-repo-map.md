---
title: Logan-VGG repo map
version: v1.0
last_updated: 2026-11-25
owner: Adeyinka Oshin
sources: logansherzog/Logan-VGG — README.md, CLAUDE.md, folder listing, git log (as of 2026-11-25)
---

# Logan-VGG repo map

`logansherzog/Logan-VGG` on GitHub is **Logan Herzog's private repo** for the
VGG build program and task management. It is shared with Logan's team by
direct collaborator invite. The EA works in it daily (mainly through
`/ops-runway`). Paths below are for finding things; **don't copy file contents
out of this repo** — its own rules forbid it.

## The repo's rules (from its `CLAUDE.md`) — summary

- **Stays private.** No visibility change, no collaborators added, no forks,
  no copying contents into any other repo, gist, artifact or public place,
  without Logan's explicit yes in that same conversation turn. Every time.
- **Some files are not vetted for sharing** even inside the team (a few build
  plans and samples are listed in `CLAUDE.md`). Treat them as internal.
- **Sender choice (Logan's own sessions only):** before any VGG email is sent
  or drafted, Claude asks which mailbox it comes from — Logan's VGG mailbox or
  the separate agent inbox — every message, no default; unattended routines
  never send. Teammates' sessions skip this and send from their own accounts
  under their policy file in `work/policies/`.
- **Free to do:** read anything, draft new files, commit and push, update
  `TASKS.md` and `README.md`, add build plans.
- **Ask Logan first:** visibility or collaborator changes, deleting someone
  else's files, history rewrites / force pushes, copying files elsewhere,
  removing `CLAUDE.md`.
- Related repos `logansherzog/vgg` and `logansherzog/claude-config` are even
  more sensitive and never go public.

More on CLAUDE.md files in general:
[../01-setup/05-claude-md-files.md](../01-setup/05-claude-md-files.md).
GitHub access: [../01-setup/02-github-setup.md](../01-setup/02-github-setup.md).

## Branch model in one paragraph

`main` is the official copy and is mostly written by Logan's account (the
tower). Claude Code cloud sessions and routines push to `claude/...` branches:
a random-named branch per interactive session (this is where `/ops-runway`
logs land), `claude/judgment-<handle>` for review routines, and
`claude/work-<handle>` for work-request runs. The tower **copies** the
relevant files from those branches onto `main` (it never merges them). Details:
[../02-workflows/ops-runway/branches-and-pickup.md](../02-workflows/ops-runway/branches-and-pickup.md).

## Folder by folder

| Path | What lives there | Who writes it | Who uses it | Handover doc |
|---|---|---|---|---|
| `README.md` | Orientation: what's in the repo and how each role uses it | Logan (anyone may update) | Everyone, first read | — |
| `CLAUDE.md` | Rules every Claude session in the repo must follow (above) | Logan | Every Claude session (loaded automatically) | This page |
| `TASKS.md` | Live status per stakeholder; EA action items near the top; blockers needing exec decisions | Logan, EA, Claude sessions | EA (near-term work), Logan | [TO CONFIRM: is `TASKS.md` still maintained now that the Station exists?] |
| `.claude/skills/` | The five repo skills: `ops-runway`, `judgment-intake`, `judgment-review`, `work-intake`, `work-run`. Load automatically in sessions on this repo. | Logan | EA (`ops-runway`, `work-run`), execs' routines (`judgment-review`, `work-run`), tower (`*-intake`) | [ops-runway](../02-workflows/ops-runway/README.md), [judgment and work](../02-workflows/judgment-and-work-requests/README.md) |
| `.mcp.json` | Connector config for Logan's own mailbox in sessions on this repo | Logan | Logan's sessions | Not for the EA to change |
| `station/` | **Read-only mirror** of the Station: `README.md` (last-mirrored time + Station link), `flights.md` (index), `flights/<CODE>.md` (one per flight), `flight-plan.md`, `rocks.md` | Tower sweep only | EA via `/ops-runway`, all routines | [station-and-flights](../02-workflows/station-and-flights/README.md) |
| `ops/log/` | One file per day (`YYYY-MM-DD.md`, WAT) of Ops runway updates, one line per flight | EA's `/ops-runway` session (on `claude/*`), copied to `main` by the tower | Tower sweep → Station | [ops-log-format](../02-workflows/ops-runway/ops-log-format.md) |
| `ops/openops-worker.md` | Placeholder for a planned deeper link from the tower to the Central Ops context system (waiting on Uche) | Logan | Tower | [TO CONFIRM: any update from Uche since 5 Oct?] |
| `judgment/` | Judgment queue: `queue/`, `feedback/`, `people.yaml` (handles + lanes), `personas/` (reviewer cards), `tools/queue.py`, `examples/` (fictional), `smoke-test/`, `README.md`, `SETUP-FOR-EXECS.md`, `ROUTINE-PROMPT.md` | Queue, people, personas: tower. Feedback: reviewers' routines. | Tower, execs | [judgment and work](../02-workflows/judgment-and-work-requests/README.md) |
| `work/` | Work requests: `queue/`, `results/`, `policies/<handle>.yaml` (what each person's Claude may do), `setup/<handle>/` (per-person setup pack and routine prompt), `tools/work.py`, `README.md` | Queue, policies, setup: tower. Results: assignees' Claude. | Tower, assignees (Bunmi, EA) | [judgment and work](../02-workflows/judgment-and-work-requests/README.md) |
| `work/policies/external-qa.md` | Review rules for anything going outside VGG | Logan | Anyone running Bunmi's skills | [TO CONFIRM: which handover doc covers external QA?] |
| `skills-bunmi/` | Install pack for skills that run in Bunmi's own Claude (pre-meeting brief, meeting artifacts, follow-up drafter, concept docs, week ahead, opportunity screener, OKR alignment, CEO review catch-up), plus `.zip` installers | Logan | Bunmi's Claude; the EA runs them in draft mode when a flight names one | [TO CONFIRM: link to the handover docs for Bunmi's skills] |
| `skills-margaret/` | Skill install pack for another stakeholder | Logan | That stakeholder | Not in the EA's scope |
| `build-plans/` | One-page proposal per planned build, by stakeholder; `mined/` holds lower-confidence proposals | Logan | Stakeholders reviewing their plan; EA when chasing inputs | Some files flagged internal in `CLAUDE.md` |
| `edtech-council/` | One council's pipeline system working files | Logan | That council | Not in the EA's scope |
| `session-2026-09-23/`, `session-2026-09-24/` | Working files from two early work sessions (drafts, plans, logs) | Logan | Historical | Reference only |

## Commit messages you'll see in `git log`

| Pattern | Means |
|---|---|
| `station: mirror <N> flights (<UTC time>)` | Tower sweep refreshed the mirror |
| `ops/log: copy … logs from claude/* branches` / `ops: copy …` | Tower copied EA ops logs onto `main` |
| `ops: <N> flights worked (<date>)` | An `/ops-runway` session's own commit (on a `claude/*` branch) |
| `judgment-intake: …`, `judgment(<handle>): …` | Judgment loop (tower / reviewer) |
| `work-intake: …`, `work: file W-…`, `work(<handle>): …` | Work-request loop (tower / assignee) |
| `skills-bunmi: …` | Changes to Bunmi's skill pack |

## Gaps to confirm

- [TO CONFIRM: is `TASKS.md` still maintained now that the Station exists?]
- [TO CONFIRM: any update from Uche on the Central Ops context worker since 5 Oct?]
- [TO CONFIRM: which handover doc covers external QA (`work/policies/external-qa.md`)?]
- [TO CONFIRM: link to the handover docs for Bunmi's skills]
- [TO CONFIRM: will Logan invite the successor as a collaborator, and with push rights to branches only or to `main` too?]
