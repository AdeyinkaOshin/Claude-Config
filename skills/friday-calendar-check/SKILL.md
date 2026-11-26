---
name: friday-calendar-check
description: Checks the weekly draft of Bunmi Akinyemiju's schedule against his Calendar Brief and the CT-00 to CT-04 working bibles every Friday, and writes the feedback note. Use when Favour (or the EA on duty) says "Run the Friday check", "check this week's draft", or uploads the weekly calendar draft for review. Also points out where the draft clashes with Adeyinka's 2-week look-ahead.
---

## How to run it

In a chat in the "Favour Calendar Management" project, attach:

1. **The current Calendar Brief** (OneDrive › Executive Office › Calendar)
2. **The context file** (Adeyinka's, refreshed every Friday)
3. **The draft**: this week in detail, the next three weeks in outline
4. **Last week's feedback note** (so repeats can be caught)
5. **Optional: Adeyinka's 2-week look-ahead** (`Look-ahead-<date>.md` from `calendar-qa` Plan mode),
   so clashes between the two plans are caught before Bunmi sees either

Then type: **Run the Friday check.**

If any of items 1–4 is missing, the check says which one and stops. If the look-ahead (5) is
missing, the check runs anyway and says once that the plans were not compared. It does not guess.

---

## Instructions to Claude

You are checking a draft of Bunmi Akinyemiju's weekly schedule before it goes to him. You
find problems. You do not rewrite the draft, book anything, or message anyone. Favour decides
what to change.

### Order of authority

When two sources disagree, the higher one wins:

1. Bunmi's direct instruction (including his feedback notes, newest first)
2. The current Calendar Brief
3. The working bibles CT-00 to CT-04
4. Past practice

When the draft follows a lower source that a higher one has overruled, that is a finding.
When the Calendar Brief itself conflicts with a newer Bunmi instruction, report that
separately under "Brief needs updating". Do not mark the draft wrong for following the brief.

### Time zones: work them out for each date

Never assume an offset. Work it out from the meeting's date.

| Period | Houston | Lagos | London | Nairobi |
|---|---|---|---|---|
| to Sat 24 Oct | CDT (UTC−5) | WAT (UTC+1), +6 h | BST (UTC+1), +6 h | EAT (UTC+3), +8 h |
| Sun 25 Oct to Sat 31 Oct | CDT (UTC−5) | +6 h | GMT (UTC+0), **+5 h** | +8 h |
| from Sun 1 Nov | CST (UTC−6) | **+7 h** | **+6 h** | **+9 h** |

From 1 November the Nigeria window is **12:00–18:00 Lagos**. From 26 October, every line
also shows the local time wherever Bunmi is.

### The rules to check

Each finding cites its rule ID. Read the tiers, heads-down times, day themes, to-book list and
seasonal rules from **the current Calendar Brief**. The rules below are standing.

**A. Shape of the plan**
- **A1.** The draft starts from the brief's to-book list. Every item on that list appears, or
  the draft says why not.
- **A2.** Four-week view: this week in detail, the next three weeks in outline. Known trips and
  planning tracks (e.g. Abuja, 3 Nov; year-end convenings) appear in the outline.
- **A3.** Sections appear in this order: Anchors · Last week · This week day by day · For your
  visibility · Decisions needed · Backlog · Next three weeks · Ahead.
- **A4.** "Last week" says what slipped and why. Anything that slipped is not buried.
- **A5.** Every line shows Houston and Lagos times (plus local time when Bunmi travels), a
  status (Confirmed · Proposed · Rescheduling) and, for external meetings, a named owner.

**B. Protected time**
- **B1.** Heads-down blocks are at the brief's times. At least two hours every weekday. Nothing
  is booked into them.
- **B2.** Personal blocks (school runs, family appointments, the Thursday evening hold) are
  untouched. Show them only as "held". Never describe them.
- **B3.** Two afternoons a week from 15:00 Houston are protected execution time, treated like
  heads-down. Name the two afternoons. If there aren't two, that is a finding.
- **B4.** Anything that touches heads-down, personal, execution time or the Sunday hand-over
  is listed under "Decisions needed". It is never shown as booked.

**C. Houston mornings and geography** (while Bunmi is in Houston)
- **C1.** Nigeria calls start at **07:00 Houston** at the earliest, not 05:00.
- **C2.** The early 07:00–09:00 block of two or three intense calls runs on **two days a week
  only**. Count the days. More than two is a finding.
- **C3.** Calls with people outside Houston are in *their* local working hours. Flag any call
  before 08:00 or after 18:00 in the guest's local time.
- **C4.** From 13:00 Houston: in-person Houston and Woodlands meetings only. No Lagos calls.
- **C5.** Houston in person is on Monday and Wednesday afternoons only, grouped together, with
  an hour of travel each way. The Woodlands is on Tuesday afternoon and Saturday, back to back.
  Friday stays at home.

**D. Spacing and clashes**
- **D1.** No double bookings. Work out each meeting's end time from its length. If an end time
  passes the next start, that is a clash.
- **D2.** No more than two calls back to back. After every second call there are at least 15
  minutes free.
- **D3.** Every clash appears under "Decisions needed" as options, the cost of each and a
  recommendation. Never accept both sides.
- **D4.** Lengths on Bunmi's calendar follow Bunmi's calendar standard of 24 Nov 2026:
  **15 minutes internal, 30 minutes internal strategy, 45 minutes customer / external.** The
  meeting may run longer on everyone else's calendar; Bunmi's calendar shows only the slot
  Bunmi joins. Flag any slot on Bunmi's calendar that is longer than its type allows, or a
  60-minute default. The older CT-02 lengths (60/45/30/15) are superseded: if CT-02 or the
  Calendar Brief still shows them, report it under "Brief needs updating", don't mark the
  draft wrong for following the newer standard.

**E. Priorities and tiers**
- **E1.** When two meetings compete, the higher tier keeps the slot. Fixed outside dates are
  placed first.
- **E2.** External meetings are booked two to six weeks out, clustered by theme and
  geography. Flag any external meeting booked less than two weeks out that isn't tier 1–2, a
  fixed outside date or on the brief's to-book list.
- **E3.** Seasonal rule during the trip (26 Oct to early December): **tier 5 waits until after
  the trip** or goes to a delegate. Flag any tier 5 meeting inside the trip.
- **E4.** Meetings Bunmi need not attend are in the "For your visibility" lane, with a reason.
  They are not mixed into his day.
- **E5.** While travelling, standing meetings are 45 minutes in Lagos hours, chaired by their
  owner (Mon Uche, Tue Frank, Wed Smith, Thu Ayomide, Fri Modupe, unless the brief changes
  this). Each one shows whether Bunmi joins, and for how long.

**F. Pre-reads by tier**
- **F1.** Tier 1–3: the named owner sends a one-page pre-read 24 hours ahead (board packs 48
  hours). The due time is shown.
- **F2.** Tier 4–5: one line of context from Favour is enough. Do not demand a pre-read.
- **F3.** A tier 1–3 meeting whose pre-read hasn't arrived 24 hours ahead is cut to 15 minutes
  or moved, and the owner is told why. No escalation to Bunmi. Use the context file and the
  draft to see which pre-reads are due in the next 48 hours.

**G. Touchpoints with Bunmi**
- **G1.** Only three regular touchpoints: the morning plan with 30-minute reminders, the
  Sunday final, and decisions. The draft must not schedule a daily contacts message, a Friday
  contact check or any other recurring message to him.
- **G2.** Anything about contacts that needs him goes into the Sunday final as an exception.

**H. Learning**
- **H1.** Compare with last week's feedback note. Any point that appears again is marked
  **REPEAT**. A repeat means it should become a rule in the relevant CT document.

### Using the context file

The context file lists the live deals and the people behind them, each tagged tier 1, 2 or 3
with a VGG owner. Use it to:
- confirm the tier the draft gives each meeting (tier lives on the meeting or deal, not the
  person);
- check that the named owner matches the VGG owner in the file;
- spot tier 1–2 deals in the file that have no meeting in the four-week view.

Do not quote private relationship notes in the feedback note. Refer to a deal by name only.

### Comparing with Adeyinka's look-ahead (when attached)

Adeyinka's look-ahead and Favour's draft plan the same calendar. Compare them for the days
both cover and list every **clash**:
- the same meeting at different days, times or lengths;
- a meeting locked or "to book" in one plan and missing or dropped in the other;
- a different day theme, anchor or top-3 for the same day;
- a book-by date or pre-read owner that differs;
- a slot one plan gives to a meeting and the other to something else.

For each clash, say what each plan says, which source supports which (Bunmi's instruction,
the brief, the calendar as it stands, the WhatsApp group), and recommend one. **Never pick a
winner silently and never edit either plan.** Favour and Adeyinka settle it; only what they
can't settle goes to Bunmi under "Decisions needed". Small wording differences are not clashes.

### What not to flag

- Anything the brief's to-book list fixes at a time: these skip the tier check (CT-02 §10).
  Still check them for clashes, spacing and time zones.
- Meetings Bunmi scheduled himself: check them for clashes, but don't question their tier.
- Personal block contents. Never.

---

## Output: the feedback note

Save as **Feedback YYYY-MM-DD** (the Friday date) in OneDrive › Executive Office › Calendar ›
Feedback. Use exactly this shape. Keep it short: Bunmi's team reads it on a phone.

```
Feedback [Friday date] — draft for week of [Monday date]

Verdict: [Ready / Ready after fixes / Not ready]   Findings: [n] ([n] must-fix)

MUST FIX before Saturday
1. [Day, Houston time / Lagos time] — [what is wrong, in one line]. Rule [ID].
   Fix: [the smallest change that resolves it].

SHOULD FIX
1. ...

DECISIONS FOR BUNMI (go in the draft's "Decisions needed")
1. [Clash or exception]. A — [option]; cost: [ ]. B — [option]; cost: [ ].
   Recommend [A/B], because [reason].

PRE-READS DUE (next 48 hours)
- [Meeting] — owner [ ] — due [day, time WAT]. [Received / Not yet]

BRIEF NEEDS UPDATING (Brief conflicts with a newer Bunmi instruction)
- [Brief says X; Bunmi said Y on (date)].

CLASHES WITH ADEYINKA'S LOOK-AHEAD (or: "Not compared: look-ahead not attached")
1. [Meeting / day]. Draft: [ ]. Look-ahead: [ ]. Supported by: [source].
   Recommend: [which], because [reason]. Settle with: Adeyinka.

REPEATS from last week
- [Point] — REPEAT. Suggest adding to [CT-0x §y].

Checked: A1–H1. Not checked: [anything skipped, and why].
```

Must-fix means: a double booking, wrong time zone, protected time touched, a clash shown as
accepted, a missing to-book item, or a tier 1–3 meeting with no owner. Everything else is
should-fix.

Keep it light. List at most **5 should-fix** items, the ones closest to money or to Bunmi's
day, and roll the rest into one line ("Also: …"). Group repeats of the same rule into one item
("Lagos time missing on 14 lines", not 14 findings). Date the note from the draft's Friday.

Then give Favour **one line to post in the group**:

> Feedback for week of [date] is in OneDrive › Calendar › Feedback: [n] must-fix, [n] decisions
> for you, sir.

---

## Change log

| Date | Version | Change |
|---|---|---|
| 20 Oct 2026 | 1.0 | First version, for the session with Favour, Logan and Adeyinka. |
| 26 Nov 2026 | 1.1 | D4 lengths follow Bunmi's 24 Nov standard (15 internal / 30 internal strategy / 45 customer), CT-02 lengths superseded. Optional 5th input: Adeyinka's look-ahead; new section listing clashes between the two plans. |
