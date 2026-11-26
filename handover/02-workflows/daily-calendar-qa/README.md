---
title: Daily calendar QA (calendar-qa skill)
version: v1.1
last_updated: 2026-11-26
owner: Adeyinka Oshin
sources: calendar-qa skill (synced account skill, updatedAt 2026-11-25), Logan-VGG/station/README.md, Logan-VGG/station/flight-plan.md (skim), Logan-VGG/ops/log/ (format only), ops-runway log format
---

# Daily calendar QA (calendar-qa skill)

> Bunmi asked (25 Nov 2026) for Adeyinka to be quality assurance and backup for Udeme on
> everything Bunmi posts in the WhatsApp calendar group. Udeme and the calendar team send
> the emails and book. Adeyinka, using the `calendar-qa` skill, checks that the booking is
> complete and correct, follows up with Udeme on anything stuck, and covers when Udeme is
> out or overloaded. The skill has five modes: Plan, Daily, Thursday themes, Sunday check
> and Friday score. Plan mode has its own folder: [`../two-week-look-ahead/`](../two-week-look-ahead/README.md).

Read [`../two-week-look-ahead/how-the-calendar-pieces-connect.md`](../two-week-look-ahead/how-the-calendar-pieces-connect.md) first.

## 1. Purpose

Bunmi measures outcomes, not activity. The calendar being right is "done". Sending a
message is not.

Definition of done (from the skill):

1. Nothing Bunmi asks for in the WhatsApp group gets dropped.
2. Every day has a theme, so Bunmi knows what the day is for.
3. The next 2 weeks are planned: each day's top 3 locked, each week at least 50% planned.
4. Every external meeting has a purpose, a wanted outcome and context from last time.
5. Every meeting that happened has a next date locked or requested (or is clearly the last).
6. The weekly score (% of planned meetings that happened as planned) goes up.

All checks come from Bunmi's calendar standard. Summary: [`bunmi-calendar-standard.md`](bunmi-calendar-standard.md).

## 2. When it runs

| Day (WAT) | Mode | Phrase to type |
|---|---|---|
| Mon–Wed, morning and evening | Daily | `/calendar-qa daily calendar check` (or `run my QA`, `check the calendar`) |
| Thursday | Plan (includes themes) / Thursday themes | `/calendar-qa plan the next 2 weeks` or `/calendar-qa set the day themes` |
| Friday | Plan refresh + Friday score | `/calendar-qa score the week` |
| Saturday–Sunday | Sunday check | `/calendar-qa Sunday check` |

If you type only `/calendar-qa`, Claude picks the mode by day as above, or asks.
Details of each mode: [`modes.md`](modes.md).

**[TO CONFIRM: are any of these runs started by a scheduled task? The 25 Nov log shows a
morning daily run at 11:55 WAT; it is not clear if that was by hand. Agree fixed times for
the morning and evening runs.]** See [`../../01-setup/07-scheduled-tasks-and-routines.md`](../../01-setup/07-scheduled-tasks-and-routines.md).
Note: a scheduled run can draft and log, but must never send.

## 3. Who does what

| Person / role | Responsibility |
|---|---|
| Adeyinka (EA) | Runs the QA. Checks Claude's findings. Sends the fix list to Udeme. Covers items Udeme can't get to. Raises requests "not on the Station" with Logan. |
| Udeme and the calendar team | Send scheduling emails. Book, move and confirm meetings. Act on the fix list. |
| Bunmi | Posts requests in the BA Calendar WhatsApp group. Sets the week focus. |
| Logan | Runs the Station and tower. Picks up the `ops/log/` lines within the hour. |
| Claude | Reads, checks, drafts. Never books, moves, accepts, declines or sends. |

## 4. Before you start (prerequisites)

- Claude account and Claude Code cloud sessions: [`../../01-setup/01-claude-account-and-cloud-sessions.md`](../../01-setup/01-claude-account-and-cloud-sessions.md).
- Access to the private `Logan-VGG` repo: [`../../01-setup/02-github-setup.md`](../../01-setup/02-github-setup.md).
  The skill reads `station/flights.md` (workstream "Bunmi calendar") and writes to `ops/log/`.
- Connectors ([`../../01-setup/03-connectors.md`](../../01-setup/03-connectors.md)):
  - **Microsoft 365**: Bunmi's Outlook calendar (shared to you); your Outlook. Mail sent to
    the EA team group mailbox lands in your inbox. The skill
    already knows how to search it. SharePoint for the meeting review folders.
  - **WhatsApp** (Railway connector) for the BA Calendar group:
    [`../../01-setup/04-whatsapp-connector.md`](../../01-setup/04-whatsapp-connector.md).
- The `calendar-qa` skill on in your account. To update it:
  [`../../01-setup/06-creating-a-skill.md`](../../01-setup/06-creating-a-skill.md).

Sources still marked "requested" in the skill (Bunmi's Fireflies, Bunmi's notes vault, the
`Planning/` folder, the backlog file): the skill skips checks that need them and says so
once. When access arrives, tell Claude (for example "I have access to the context file") so
it updates the skill's source table.

## 5. Step by step (Daily mode)

Other modes follow the same pattern. See [`modes.md`](modes.md).

1. Open a **Claude Code cloud session** at <https://claude.ai/code> on the `Logan-VGG` repo.
   **[TO CONFIRM: confirm this is where Adeyinka runs it, rather than a plain claude.ai chat.]**
2. Type: `/calendar-qa daily calendar check`
3. Claude pulls the repo. **Check:** if it says the Station mirror is more than 2 hours old,
   note it and tell Logan if it stays stale.
4. Claude says which checks it skipped and why (missing sources).
5. **Morning run.** Claude:
   - lists open "Bunmi calendar" flights on the Station (skipping ones already logged done
     today or yesterday);
   - reads the BA Calendar WhatsApp group since the last run, and lists asks not yet on the
     Station;
   - checks each request against the calendar: **OK**, **wrong** (says what), **not booked**,
     or **stuck** (no movement in 2+ days). Date, time, people, length and place (full
     address, not just a venue name) are all checked;
   - checks the next 3 working days: agenda, lengths, deep-work and flex blocks, clashes,
     drive time, "why is this here?", "can be delegated", and any moves.
6. **Evening run.** As above, plus: for each meeting that happened today, is the next
   meeting locked or requested? Claude checks the meeting review folder and the EA team
   mailbox. If no next-meeting email went out, it flags it. For key meetings it offers a
   WhatsApp summary draft Bunmi can forward.
7. Claude shows the output:
   ```
   Fix with Udeme   numbered: what's wrong, which meeting/flight, what to do
   I'll cover       anything Udeme can't get to
   Not on Station   requests to raise with Logan
   ```
8. **Check each item.** Does it make sense? Is the finding true on the calendar? Ask Claude
   to walk the fixes **one at a time**, not as a dump.
9. Ask: `Draft the note to Udeme with the fix list.` Read it, edit it, and **you** send it.
10. For "Not on Station" items, tell Logan (or the tower) so they become flights.
11. For "I'll cover" items, do them yourself (you, not Claude, send the emails or book).
12. Claude appends lines to `ops/log/<today>.md` and pushes **only** `ops/log/`. Check the
    format matches [`log-format.md`](log-format.md).
13. Claude ends with four lines: how many OK, how many to fix with Udeme, how many you are
    covering, and the one thing Bunmi should know. Pass that one thing on if it matters.

## 6. Output — what you get and where it goes

| Output | Where it goes |
|---|---|
| Fix list (Fix with Udeme / I'll cover / Not on Station) | Shown in chat. Adeyinka sends the Udeme part. **[TO CONFIRM: channel to Udeme: WhatsApp, Teams or email]** |
| Note to Udeme (draft) | Adeyinka sends it |
| WhatsApp summary drafts for key meetings ("we agreed these 4 things") | To Bunmi to forward. **[TO CONFIRM: does Adeyinka send these to Bunmi, and on which chat?]** |
| Clashes with Favour's plan (Plan mode and Sunday check) | Shown in chat, at the top. Adeyinka settles each with Favour; unsettled ones go to Bunmi as decisions. |
| Thursday theme grid, Sunday fix list, Friday score | See [`modes.md`](modes.md), [`day-themes.md`](day-themes.md), [`scoring.md`](scoring.md) |
| Log lines | `ops/log/YYYY-MM-DD.md` in `Logan-VGG` (Lagos date). Tower reads them hourly. |

## 7. Review and approval rules

- **Never send, book or move.** Claude drafts; Adeyinka passes notes to Udeme or sends them.
- **Never edit `station/`.** It's a read-only mirror. Log in `ops/log/` only.
- Follow the `Logan-VGG` `CLAUDE.md`. Don't paste calendar or flight details outside the repo.
- Family and personal blocks show as "held", with no detail.
- Dates are checked against the source. If WhatsApp, the invite and the email disagree, flag
  all versions.
- One issue at a time when walking through fixes.
- Don't report a step as done because something was sent. Done = on the calendar.
- Adeyinka challenges Claude's output and the team's output. Something that doesn't make sense
  gets questioned, not passed on.

## 8. Common problems and fixes

| Symptom | Fix |
|---|---|
| Station mirror stale | Check WhatsApp by eye; tell Logan. Many "not on Station" items is a sign. |
| A meeting happened but has no review folder | Check again next run. After a day, ask someone who was in the room. |
| EA team mailbox search fails | It's a group, not a shared mailbox. The skill searches your own mailbox by recipient. If it tried another way, remind it. |
| Same item "stuck" day after day | Escalate: ask Udeme what is blocking. If Udeme can't move it, cover it yourself or ask Bunmi for help. |
| Too many findings | Fix the ones closest to Bunmi's next 3 days first. |
| Invite has a venue name but no full address | Mark "wrong". Ask Udeme to add the full address. |
| Claude invents a reason for a meeting | Stop. A reason must come from a source. Unknown → open question. |

## 9. Gaps to confirm

1. **[TO CONFIRM]** Are any modes run by a scheduled task? Agreed times for morning and evening daily runs.
2. **[TO CONFIRM]** Claude Code on `Logan-VGG` vs plain claude.ai chat.
3. **[TO CONFIRM]** Channel used to send the fix list to Udeme.
4. **[TO CONFIRM]** Who sends the "we agreed these 4 things" WhatsApp drafts to Bunmi, and how.
5. **[TO CONFIRM]** Where the Sunday 3-line summary goes and who gives it to Bunmi.
6. **[TO CONFIRM]** When Bunmi's Fireflies, notes vault, `Planning/` folder and backlog file become available (they unlock skipped checks).

## Change history

| Version | Date | Change |
|---|---|---|
| v1.0 | 2026-11-25 | First written |
| v1.1 | 2026-11-26 | calendar-qa v1.1: Sunday check covers clashes with Favour's draft |
