# Feedback note format

Saved as **`Feedback YYYY-MM-DD`** (the Friday date) in OneDrive › Executive Office ›
Calendar › Feedback. Bunmi's team reads it on a phone, so it is short.

## Shape

```
Feedback [Friday date] — draft for week of [Monday date]

Verdict: [Ready / Ready after fixes / Not ready]   Findings: [n] ([n] must-fix)

MUST FIX before Saturday
1. [Day, local time / Lagos time] — [what is wrong, one line]. Rule [ID].
   Fix: [smallest change that resolves it].

SHOULD FIX
1. ...

DECISIONS FOR BUNMI (go in the draft's "Decisions needed")
1. [Clash or exception]. A — [option]; cost: [ ]. B — [option]; cost: [ ].
   Recommend [A/B], because [reason].

PRE-READS DUE (next 48 hours)
- [Meeting] — owner [ ] — due [day, time WAT]. [Received / Not yet]

BRIEF NEEDS UPDATING (Brief conflicts with a newer Bunmi instruction)
- [Brief says X; Bunmi said Y on (date)].

REPEATS from last week
- [Point] — REPEAT. Suggest adding to [CT-0x §y].

Checked: A1–H1. Not checked: [anything skipped, and why].
```

## Rules for the note

- **Must-fix** = double booking, wrong time zone, protected time touched, a clash shown as
  accepted, a missing to-book item, or a tier 1–3 meeting with no owner.
- Everything else is **should-fix**. At most **5** should-fix items (the ones closest to money
  or to Bunmi's day). The rest go in one "Also: …" line.
- Group repeats of the same rule ("Lagos time missing on 14 lines", not 14 findings).
- Dated from the draft's Friday.

## Example must-fix line (invented)

```
1. Tue, 10:00 local / 17:00 Lagos (invented offset) — two calls overlap by 15 minutes. Rule D1.
   Fix: move the second call to 10:45 local.
```

## The group post

After saving, Favour posts one line in the group:

> Feedback for week of [date] is in OneDrive › Calendar › Feedback: [n] must-fix, [n]
> decisions for you, sir.
