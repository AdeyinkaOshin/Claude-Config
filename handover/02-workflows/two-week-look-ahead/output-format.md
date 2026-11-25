# Look-ahead output format

Plan mode writes two files. The exact layout lives in the `calendar-qa` skill (Plan mode,
step C). This page explains each part in plain English so you can check it.

## File 1: `Lookahead-<YYYY-MM-DD>.md` (for Bunmi and the team)

Sections, in order:

| Section | What it holds | What to check |
|---|---|---|
| Header | "Next 2 weeks", the dates, the cities | Dates and weekdays match |
| The 2 weeks in 3 lines | A summary Bunmi can read in 10 seconds | Would Bunmi know what the fortnight is for? |
| Week 1 / Week 2 | What the week is about, key days, then each day | Bunmi's order: week → key days → anchor → blocks |
| Each day | Theme · anchor · top 3 (locked / to book) · deep-work and flex blocks · prep needed | Every day has a theme and an anchor |
| Working backwards (next 6 weeks) | Each fixed point with its book-by, prep, documents, agenda and brief dates; on track or LATE | Late steps are flagged, not hidden |
| Gaps to close | Numbered, each with what to do. Late chain steps first. | Each gap has an action |

*Example day line (invented, for layout only):*

```
Tue 8 Dec | Theme: Capital / bank | Anchor: Bank partner review (locked)
   Top 3:  1. Bank partner review (locked)  2. Investor follow-up (to book)  3. New-exec check-in (locked)
   Blocks: deep work 08:00–09:00 · flex 16:00–17:00
   Prep:   internal prep for Thu's customer meeting
```

## File 2: `Context-for-calendar-team-<YYYY-MM-DD>.md` (for Udeme's team)

One page per week. This is the booking instruction sheet.

| Section | What it holds |
|---|---|
| Week focus and themes | One line, plus the theme for each day |
| Locked (don't move) | Meeting · day/time · why it matters |
| To book, in this order | Book-by date · who · why / wanted outcome · theme day to aim for · length (15/30/45) · Bunmi's slot only · agenda line for the invite · owner. Sorted by book-by date, earliest first. Late ones marked LATE. |
| Coming up (3–6 weeks) | Fixed points further out and the date their invite must go |
| Next meetings owed | From meetings already held: who · proposed window · the email to send |
| Prep meetings needed | Internal prep · before which meeting · by when |
| Rules for this week | Anything Bunmi said about how to handle a person or meeting |
| Open questions | Only what Adeyinka or Bunmi must decide |

Rules for this file:

- Every "to book" line has a reason and a wanted outcome. Unknown → Open questions.
- No family or personal detail. Show "held".
- No transcript text, no withheld items.

## Not the same as the weekly context file

The **context for the calendar team** (this page) tells Udeme's team what to book.
The **weekly context file** (see [`../weekly-context-file/`](../weekly-context-file/README.md))
tells Favour about deals, owners, tiers and where Bunmi is, for the weekly draft.
Different readers, different files.
