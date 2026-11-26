---
title: Two-week look-ahead (calendar-qa Plan mode)
version: v1.1
last_updated: 2026-11-26
owner: Adeyinka Oshin
sources: calendar-qa skill (synced account skill, updatedAt 2026-11-25), Logan-VGG/skills-bunmi/week-ahead/SKILL.md, Logan-VGG/station/README.md, Logan-VGG/ops/log/ (format only)
---

# Two-week look-ahead (calendar-qa Plan mode)

> Every Thursday (refreshed Friday), Adeyinka uses the `calendar-qa` skill in **Plan mode**
> to build Bunmi's plan for the next 2 weeks. It produces two files: the **look-ahead**
> (for Bunmi and the team) and the **context for the calendar team** (what Udeme's team must
> book, in order). Bunmi's goal is to wake up, look at the calendar and go where it says.
> Bunmi's time is one of the most expensive things VGG has, so this plan is the foundation
> for everything else.

Read [`how-the-calendar-pieces-connect.md`](how-the-calendar-pieces-connect.md) first.

## 1. Purpose

Plan forward, not the day before. Meetings booked the day before fail because people have
already planned their week.

"Done" means the plan is **on the calendar**, not just written down:

- Every day in the next 2 weeks has a **theme** and an **anchor** meeting.
- Every day has its **top 3** meetings locked (or first in line to lock).
- Each week is at least **50% planned** (not full days).
- Every fixed point in the next 6 weeks has a dated "work backwards" chain.
- Every "to book" item has a reason and a wanted outcome.

Sending the look-ahead is activity. The week actually being on the calendar is the outcome.
Move to 3 weeks ahead once 2 weeks is consistent.

## 2. When it runs

| When (WAT) | What | How it starts |
|---|---|---|
| Thursday | Full Plan run: look-ahead, themes, team context file | Typed by hand: `/calendar-qa` then `plan the next 2 weeks` |
| Friday | Plan refresh: re-run and show only what changed since Thursday | Typed by hand: `/calendar-qa` then `plan the next 2 weeks` (say "Friday refresh") |
| Any day | On request | Same phrases, or `build the look-ahead`, `make the context file` |

If you type only `/calendar-qa`, the skill picks a mode by day: Thursday defaults to Plan,
Friday to Plan refresh plus score.

**[TO CONFIRM: is Plan mode run by hand each Thursday, or by a scheduled task? If scheduled,
which one and at what time?]** See [`../../01-setup/07-scheduled-tasks-and-routines.md`](../../01-setup/07-scheduled-tasks-and-routines.md).

## 3. Who does what

| Person / role | Responsibility |
|---|---|
| Adeyinka (EA) | Runs Plan mode. Sets the week focus. Checks and challenges the output. Shares the team context file with Udeme. Sends the cover note. |
| Udeme and the calendar team | Send the scheduling emails and book the meetings from the team context file. |
| Favour | Uses the weekly context file for the weekly draft (separate track, see the connections page). |
| Bunmi | Reads the 3-line summary. Sets priorities. Their direct instructions override everything. |
| Logan | Runs the Station and tower. Receives requests that are not yet on the Station. |
| Claude | Reads, plans and drafts. Never books, moves or sends. |

## 4. Before you start (prerequisites)

- A Claude account set up as in [`../../01-setup/01-claude-account-and-cloud-sessions.md`](../../01-setup/01-claude-account-and-cloud-sessions.md).
- GitHub access to the private `Logan-VGG` repo (Station mirror and `ops/log/`). See
  [`../../01-setup/02-github-setup.md`](../../01-setup/02-github-setup.md).
- Connectors, see [`../../01-setup/03-connectors.md`](../../01-setup/03-connectors.md):
  - **Microsoft 365**: Bunmi's Outlook calendar (shared to you), your Outlook (the EA team
    group mailbox lands here), SharePoint (BunmiExecutiveOffice site, `Meetings/` folders).
  - **WhatsApp** (Railway connector), to read the BA Calendar group. See
    [`../../01-setup/04-whatsapp-connector.md`](../../01-setup/04-whatsapp-connector.md).
- The `calendar-qa` skill turned on in your account. It is a synced account skill. To change
  it, see [`../../01-setup/06-creating-a-skill.md`](../../01-setup/06-creating-a-skill.md).
- Optional but better: the latest **weekly context file** (see
  [`../weekly-context-file/`](../weekly-context-file/README.md)).
- Know the **week focus** (for example, "banks" or "new execs"). If you don't, Claude will ask.

## 5. Step by step

1. **Open a Claude Code cloud session** at <https://claude.ai/code> on the `Logan-VGG` repo.
   This is where the skill can read the Station mirror and write the log.
   **[TO CONFIRM: does Adeyinka run this in Claude Code on `Logan-VGG`, or in a plain
   claude.ai chat? In a plain chat the Station check and the log step are skipped.]**
2. **Type:** `/calendar-qa plan the next 2 weeks`
3. Claude pulls the repo first. **Check:** if it says the Station mirror is more than 2 hours
   old, note it. Requests logged in the last hours may be missing.
4. Claude says which sources it could not reach (for example, Fireflies or the backlog file
   are still "requested"). **Check** the list. If Microsoft 365 or WhatsApp is missing,
   reconnect it and start again.
5. If Claude asks for the week focus, answer in one line.
   *Example (invented):* "Next week is about capital: banks and investors."
6. Claude gathers: the calendar for the next 2 weeks, open requests (Station + WhatsApp
   group), the backlog, next meetings owed from recent meeting review folders, and the
   weekly context file.
7. Claude builds each week in **Bunmi's order**: what the week is about → key days → each
   day's theme and anchor → top 3 per day → blocks. It works backwards from every fixed
   point in the next 6 weeks. See [`working-backwards-and-lead-times.md`](working-backwards-and-lead-times.md).
8. Claude shows you the **3-line summary, the clashes with Favour's plan, and the gap list
   first**. Read them before anything else. For the clash check, attach Favour's latest weekly
   draft (or tell Claude where it is). If it isn't available, Claude says "Not compared" and
   carries on. Settle each clash with Favour; don't change Favour's draft yourself.
9. **Check like Bunmi would** (this is the most important step):
   - For each meeting: why is it here? What does Bunmi want from it? If you can't answer,
     question it.
   - Is anything missing that should be there?
   - Is any meeting one that someone else should own? (Mark "can be delegated".)
   - Are personal or family blocks shown only as "held"?
   - Does every "to book" line have a reason and a wanted outcome? If not, it should be
     under "Open questions".
   Tell Claude what to change, one issue at a time.
10. Claude writes the two files. See [`output-format.md`](output-format.md). Save them (step
    in section 6).
11. Ask Claude: `Draft a short note to Udeme to go with the context file.` Read it. Edit if
    needed. **You** send it (WhatsApp or Teams) with the team context file attached.
12. Claude adds one line to `ops/log/<today>.md` and pushes it. **Check** the line looks like:
    `- calendar-qa · plan · <N> locked, <N> to book, <N> gaps · <HH:MM WAT>`
13. **Friday:** repeat with "Friday refresh". Claude shows only what changed since Thursday.
    Send Udeme only the changes.

## 6. Output — what you get and where it goes

| File | For | Where it goes |
|---|---|---|
| `Lookahead-<YYYY-MM-DD>.md` | Bunmi and the team | Adeyinka's OneDrive `Planning/` folder once shared. Until then Claude shows it in chat for you to save or paste. **[TO CONFIRM: final save location, and whether/how the look-ahead or its 3-line summary is sent to Bunmi]** |
| `Context-for-calendar-team-<YYYY-MM-DD>.md` | Udeme and the calendar team | Same folder. Adeyinka sends it to Udeme with the cover note. **[TO CONFIRM: channel used: WhatsApp, Teams or email]** |
| Cover note to Udeme | Udeme | Drafted by Claude, sent by Adeyinka |
| Log line | The tower (Logan) | `ops/log/YYYY-MM-DD.md` in `Logan-VGG`, pushed by Claude |

Layout of both files: [`output-format.md`](output-format.md).

## 7. Review and approval rules

- Adeyinka checks every look-ahead before it leaves. Adeyinka is "the quality checker and the
  quality giver": challenge Claude's output, don't pass it on.
- Claude **never** books, moves, accepts, declines or sends. Udeme's team books.
  Adeyinka sends notes.
- Claude never edits `station/` (read-only mirror). It only writes to `ops/log/`.
- No family or personal detail: show "held".
- No transcript text and no `[withheld: …]` items from meeting folders in either file.
- Do not paste calendar or flight details outside the private `Logan-VGG` repo or the agreed
  OneDrive folder.
- If a date differs between WhatsApp, the invite and the email, list every version. Don't
  pick one.
- Locked means locked. Before moving a locked meeting, ask: can someone represent Bunmi?
  Could Bunmi drop in for 5 minutes?

## 8. Common problems and fixes

| Symptom | Fix |
|---|---|
| "Station mirror is more than 2 hours old" | Carry on, but check the BA Calendar WhatsApp group by eye for new asks. Tell Logan if it stays stale. |
| Claude can't read Bunmi's calendar | Microsoft 365 connector needs reconnecting, or the calendar share has lapsed. See `03-connectors.md`. |
| Claude can't read WhatsApp | The WhatsApp session has dropped. See `04-whatsapp-connector.md`. |
| A "to book" line has no reason | Move it to Open questions. Ask the owner or Bunmi. Never guess a purpose. |
| A day has no anchor | Leave it on the gap list. Ask Adeyinka/Bunmi which meeting the day is built around. |
| Too much on the gap list | Late chain steps first. Then P1s with no slot. Fix one at a time. |
| Weekly context file not available | Plan still runs. Claude says which checks it skipped. Build the context file (see its folder) and re-run. |

## 9. Gaps to confirm

1. **[TO CONFIRM]** Is Plan mode run by hand each Thursday, or by a scheduled task? If scheduled, which one and when?
2. **[TO CONFIRM]** Claude Code on `Logan-VGG`, or plain claude.ai chat?
3. **[TO CONFIRM]** Final save location for both files (OneDrive `Planning/` share status), and whether/how the look-ahead or its 3-line summary reaches Bunmi.
4. **[TO CONFIRM]** Channel used to send the team context file to Udeme.
5. ~~How Favour's weekly draft and this look-ahead are reconciled~~ — decided 26 Nov: clashes are flagged by both skills and settled by Adeyinka and Favour (see `how-the-calendar-pieces-connect.md`). **[TO CONFIRM: where Favour's weekly draft is saved, so Claude can find it without it being attached]**
6. **[TO CONFIRM]** Is Bunmi's own `week-ahead` skill (Sunday 18:00, in `Logan-VGG/skills-bunmi/week-ahead/`) installed and in use? If yes, how does its output relate to this look-ahead?
7. **[TO CONFIRM]** Location of the P1/P2/P3 backlog file (proposed `Planning/Backlog.xlsx`, not yet created).

## Change history

| Version | Date | Change |
|---|---|---|
| v1.0 | 2026-11-25 | First written |
| v1.1 | 2026-11-26 | calendar-qa v1.1: Plan mode compares with Favour's draft |
