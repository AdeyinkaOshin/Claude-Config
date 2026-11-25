---
title: The Station and its flights mirror
version: v1.0
last_updated: 2026-11-25
owner: Adeyinka Oshin
sources: logansherzog/Logan-VGG — station/README.md, station/flight-plan.md, station/rocks.md, station/flights.md and station/flights/ (structure only), .claude/skills/ops-runway/SKILL.md, .claude/skills/work-intake/SKILL.md, git history
---

# The Station and its flights mirror

> The **Station** is Logan Herzog's live task board for VGG: a private
> claude.ai page where every task ("flight") has an owner, a lane, a due date
> and a goal ("rock"). The tower (Logan's side) copies the Station into the
> `station/` folder of the Logan-VGG repo so that Claude sessions and routines
> can read it. That copy is the **mirror**. The EA reads the mirror (mostly
> through `/ops-runway`), never edits it, and feeds updates back through the
> ops log or by pressing buttons on the Station itself.

## 1. Purpose

Gives everyone, people and Claude sessions alike, one shared view of all open
work, who owns it and which goal it serves. "Done" for this workflow means: the
EA can find any flight, understand its state, and get an update back onto the
Station the same day.

## 2. When it runs

- **Mirror refresh:** done by the tower's sweep. Designed to be hourly. The
  git history shows commits named `station: mirror <N> flights (<UTC
  timestamp>)`, often several an hour on busy days, with gaps of days between
  bursts. **[TO CONFIRM: what schedule the sweep is on now, and whether it runs
  on Logan's machine or as a cloud routine.]**
- **Reading it:** any time — automatically at the start of `/ops-runway`, or
  by asking Claude in a session on the repo ("show me VGG-0000" — example).
- **Updating it:** after every ops session (via the ops log), or instantly with
  the Station's **Land** and **Waiting** buttons.
- Timestamps in the mirror are **UTC** (ending in `Z`). WAT is UTC+1.

## 3. Who does what

| Person / role | Responsibility |
|---|---|
| Logan Herzog (tower) | Owns the Station. Routes flights to lanes, holds or clears them, runs the sweep that mirrors the Station into the repo and applies ops logs, judgment feedback and work results. |
| Adeyinka Oshin (EA) | Works the **ops** lane. Reads the mirror, never edits it. Lands or marks flights waiting on the Station, or via the ops log. |
| Claude sessions and routines | Read the mirror. The ops-runway, judgment and work-run skills all treat `station/` as read-only. |
| Uche | Owns the Central Ops context system the tower may consult before clearing flights (see `ops/openops-worker.md`; placeholder). |

## 4. Before you start (prerequisites)

- GitHub access to the private Logan-VGG repo:
  [../../01-setup/02-github-setup.md](../../01-setup/02-github-setup.md).
- A Claude Code session able to open the repo:
  [../../01-setup/01-claude-account-and-cloud-sessions.md](../../01-setup/01-claude-account-and-cloud-sessions.md).
- Access to the live Station page. Its link is at the top of
  `station/README.md` and in the ops-runway skill. **[TO CONFIRM: is it shared
  per person by Logan, and what can the EA do on it besides Land / Waiting?]**
- Know the repo rules in `CLAUDE.md` (summary in
  [../../03-reference/logan-vgg-repo-map.md](../../03-reference/logan-vgg-repo-map.md)).

## 5. Step by step

**A. Check how fresh the mirror is**
1. Open `station/README.md` in the repo (GitHub web or a Claude session).
2. Read the line "Last mirrored: <timestamp>". Convert from UTC to WAT (+1 hour).
3. If it is more than 2 hours old, treat the list as possibly behind and tell
   Logan. `/ops-runway` does this check for you.

**B. Find flights**
1. `station/flights.md` is the index: one table row per flight with Code,
   Title, Owner, Lane, Gate, Workstream, Due, Rock, Approval.
2. Each code links to `station/flights/<CODE>.md`, the full flight: a short
   header block (code, title, owner, lane, gate, workstream, due, rock,
   approval, source, updated), then `## Brief`, `## Context` (source links),
   and sometimes `## Draft (not sent)`.
3. To find yours, ask Claude in a session: "list ops-lane flights that are
   cleared, overdue first" — or just run `/ops-runway`.
4. What the lane / gate / approval values mean:
   [flight-statuses.md](flight-statuses.md).

**C. Understand the goals**
1. `station/flight-plan.md` — the destination and the 1-year plan items.
2. `station/rocks.md` — a table of rocks (quarterly goals) with status
   (on_track / off_track), owner, due, and counts of open and landed flights.
   A flight's `rock` field points at one of these.

**D. Send updates back**
1. Normal route: work the flight in `/ops-runway`; the log line
   (`done`, `waiting`, `in_progress`, `skipped`, `back-to-tower`) goes to the
   tower, which updates the Station. See
   [../ops-runway/README.md](../ops-runway/README.md).
2. Fast route: open the Station page and press **Land** (finished) or
   **Waiting** yourself.
3. Work-request results come back through the tower's work-intake run, which
   turns each result into land / note / back-to-inbound on the flight. See
   [../judgment-and-work-requests/README.md](../judgment-and-work-requests/README.md).
4. Never edit files in `station/` to change a flight — the next mirror
   overwrites them, and the skills forbid it.

**E. Raise a new flight**
- New asks you spot (for example from Bunmi's WhatsApp groups) go to Logan /
  the Station, not into `station/`. **[TO CONFIRM: how should the EA add a new
  flight — on the Station page directly, a message to Logan, or a
  back-to-tower line?]**

## 6. Output — what you get and where it goes

| Item | Where | Notes |
|---|---|---|
| Flight index | `station/flights.md` | Header shows total count. |
| One file per flight | `station/flights/<CODE>.md` | Landed flights older than 14 days are dropped from the per-flight files. |
| Goals | `station/flight-plan.md`, `station/rocks.md` | Read-only. |
| Mirror freshness | `station/README.md` | "Last mirrored" in UTC. |
| Updates from the EA | `ops/log/` → tower → Station | See ops-runway docs. |

## 7. Review and approval rules

- `station/` is **read-only** for everyone except the tower's sweep.
- Flights often contain names, meeting details and deal context. **Do not copy
  flight contents outside the Logan-VGG repo** (no pasting into other repos,
  public docs, artifacts or chats with people outside the team). This is a
  hard rule in the repo's `CLAUDE.md`.
- The mirror already masks addresses in context links; keep it that way —
  don't add contact details in logs or results.
- A `## Draft (not sent)` section in a flight is a draft only. Nothing is sent
  without the right person's explicit yes.

## 8. Common problems and fixes

| Symptom | Fix |
|---|---|
| Mirror is days old | The sweep hasn't run. Tell Logan. Use the Station page for the true state. |
| Flight count jumps up or down by ~100 between mirrors | Normal: landed flights older than 14 days get dropped from (or kept in) the per-flight files depending on the sweep setting. |
| A flight file is missing for a code in the index | Probably an old landed flight whose file was dropped. Check the Station. |
| A flight shows gate `held` | It clears at the next tower run. Don't work it yet. |
| You edited `station/` by mistake | Don't commit it. Ask Claude to discard the change (`git checkout -- station/`). |
| Station and mirror disagree | The Station page wins; the mirror is a copy. |

## 9. Gaps to confirm

- **[TO CONFIRM: what schedule the sweep is on now, and whether it runs on Logan's machine or as a cloud routine.]**
- **[TO CONFIRM: is the Station shared per person by Logan, and what can the EA do on it besides Land / Waiting?]**
- **[TO CONFIRM: how should the EA add a new flight — on the Station page directly, a message to Logan, or a back-to-tower line?]**
- Lane / gate / approval meanings marked in [flight-statuses.md](flight-statuses.md).

## Change history

| Version | Date | Change |
|---|---|---|
| v1.0 | 2026-11-25 | First written |
