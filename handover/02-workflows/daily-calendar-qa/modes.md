# calendar-qa modes

The `calendar-qa` skill has five modes. Each run starts the same way: pull the `Logan-VGG`
repo, warn if the Station mirror is more than 2 hours old, then pick the mode.

## Which mode, which day (WAT)

| Day | Default mode | Phrase |
|---|---|---|
| Mon–Wed | Daily (morning and evening) | `daily calendar check`, `run my QA`, `check the calendar` |
| Thu | Plan (includes themes) | `plan the next 2 weeks`, `build the look-ahead`, `set the day themes` |
| Fri | Plan refresh + Friday score | `score the week` |
| Sat–Sun | Sunday check | `Sunday check` |

Start every phrase with `/calendar-qa` to be sure the skill loads. If you don't name a mode,
Claude picks by day or asks.

---

## Mode 0: Plan (Thursday, refreshed Friday)

Builds the 2-week look-ahead and the context file for the calendar team. Full guide:
[`../two-week-look-ahead/README.md`](../two-week-look-ahead/README.md).

## Mode 1: Daily (morning and evening)

**What it checks**

- **A. Requests from Bunmi.** Open "Bunmi calendar" flights on the Station, plus asks in
  the BA Calendar WhatsApp group not yet on the Station. Each one is checked against the
  calendar and marked **OK / wrong / not booked / stuck** (no movement for 2+ days). It checks
  date, time, people, length and place (full address).
- **B. Meetings that happened today** (evening run). Is the next meeting locked or
  requested? Sources: the meeting review folder's next-meeting and actions files, and the
  EA team mailbox (did Udeme's team send the "lock the next date" email? did the other side
  reply?). Bunmi's replies on EA mailbox threads count as requests too. No recording → "ask
  someone who was in the room". Clearly the last meeting → close it.
- **C. Upcoming meetings (next 3 working days).** Agenda (why, wanted outcome, what happened
  last time); one-page brief for key meetings; lengths; deep-work and flex blocks;
  information-only items set to "free"; no clashes; enough drive time; "why is this here?";
  "can be delegated → owner"; anything moved since last run was emailed properly and a
  stand-in or 5-minute drop-in was considered first.

**Output:** Fix with Udeme · I'll cover · Not on Station. Plus a draft note to Udeme.

**When to use the evening run:** after the day's meetings end, so next meetings can be
locked the same day. **[TO CONFIRM: agreed time for the evening run]**

## Mode 2: Thursday themes

1. Read the week focus (from the context file once live; otherwise Claude asks you).
2. Lay out each week in Bunmi's order: what the week is about → key days → each day's
   anchor → time blocks.
3. Propose a theme for every day of the next 2 weeks. See [`day-themes.md`](day-themes.md).
4. Slot by priority: capital and paying customers → new execs → direct reports and internal.
5. Work backwards: any big external meeting without internal prep 2–3 working days before
   is flagged.

**Output:** a 2-week theme grid and a note for Udeme. Adeyinka shares it.

## Mode 3: Sunday check

For each day in the next 2 weeks:

1. Top 3 meetings locked?
2. Day matches its theme?
3. Week at least 50% planned?
4. Every open Bunmi request (Station + backlog) has a slot?
5. Standing pattern met (banks / investment almost daily, new execs every other day)?
6. Every fixed point's working-backwards chain on track? Any step late? Any meeting 2–6
   weeks out whose book-by date falls this week?

**Output:** the 2 weeks in Bunmi's order, a fix list for Udeme with owner and a deadline of
**Monday morning**, and a 3-line summary Adeyinka can give Bunmi. If the plan isn't there
yet, Claude says so plainly: it's not done.

## Mode 4: Friday score

Compares the week's plan (from Sunday) with what happened. Details: [`scoring.md`](scoring.md).

**Output:** the score, the reason for each miss, booked on time vs late, one fix to try
next week, and a short note to Udeme.

---

## Every mode ends the same way

- Log lines appended to `ops/log/YYYY-MM-DD.md` and pushed. See [`log-format.md`](log-format.md).
- Four closing lines: how many OK, how many to fix with Udeme, how many Adeyinka covers, and
  the one thing Bunmi should know.
- Nothing is sent by Claude. Adeyinka sends.
