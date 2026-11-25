# Ops log format

Where: `ops/log/YYYY-MM-DD.md` in the Logan-VGG repo. One file per day, named
with the **Lagos (WAT) date**. Claude creates it if it doesn't exist.

Optional first line (recent files have it):

```
# Ops log, YYYY-MM-DD (Day)
```

Then one line per flight, appended after each flight is worked:

```
- <CODE> · <status> · <one line: what happened, next date if any> · <HH:MM WAT>
```

The separator is a middle dot with a space either side (` · `). Keep it exact:
the tower reads these lines by machine.

## Status words

| Status | Use when | What the tower does |
|---|---|---|
| `done` | The EA finished it. | Lands the flight on the Station on its next sweep. |
| `waiting` | The EA did their part; now waiting on someone. Name who and the follow-up date. | Shows interim progress on the Station. |
| `in_progress` | Partly done. Say which part is done and what is left. | Shows interim progress on the Station. |
| `skipped` | Not now. | Nothing; the flight comes back next session. |
| `back-to-tower` | Needs Logan's call. Write the question so it can be answered in one line (yes/no). | Logan answers or re-routes. |

## Invented examples (not real flights)

```
# Ops log, 2026-12-01 (Tue)

- VGG-0001 · done · Example: venue confirmed with the host's office for Thu 3 Dec 10:00 · 10:42 WAT
- VGG-0002 · waiting · Example: asked the calendar team to book; follow up Wed 2 Dec · 10:51 WAT
- VGG-0003 · in_progress · Example: invite sent by EA; location still missing · 11:05 WAT
- VGG-0004 · skipped · Example: not today · 11:06 WAT
- VGG-0005 · back-to-tower · Example: Is "Sam" the same person as on the earlier flight? Yes/no · 11:10 WAT
```

## Writing good lines

- One line only. Dates as "Thu 3 Dec", times in WAT.
- Say "drafted, not sent" until the EA confirms a message was actually sent.
- Put corrections the EA gives (a fixed name, new context) in the line.
- Never paste full messages, phone numbers or email addresses into the log.

## Lines from other skills

Other skills sometimes add one summary line to the same day's file, using the
skill name in place of a flight code (for example a calendar check summary).
Same separator, same time stamp at the end.
**[TO CONFIRM: does the tower sweep read or ignore these non-flight lines?]**

## Committing

Claude commits only the `ops/log/` folder, every 3 flights and at the end:

```
git add ops/log && git commit -m "ops: <N> flights worked (<date>)" && git push
```

If the push is refused: `git pull --rebase`, then push again.
