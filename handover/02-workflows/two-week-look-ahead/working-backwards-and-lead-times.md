# Working backwards and lead times

Planning starts at the end, not at Monday morning. This is section 8 of Bunmi's calendar
standard (24 Nov 2026), as built into the `calendar-qa` skill.

## Fixed points

A fixed point is anything with a date that can't easily move: a big external meeting, a
trip, the retreat, a deadline, a deal milestone (for example a signing or a pilot start).

Plan mode lists every fixed point in the next **6 weeks** (not just 2). It finds them in:
action due dates in meeting review folders (`02_actions.md`), promised documents
(`03_menu.md`), Station flights with due dates, and Bunmi's replies in the EA team mailbox.

## The chain for each fixed point

```
Fixed point (date)
  ← brief to Bunmi            evening before
  ← agenda / one-pager sent   2 working days before
  ← internal prep meeting     2–3 working days before
  ← documents ready           before the prep meeting
  ← people briefed            whoever needs context first
  ← invite sent / slot locked the BOOK-BY date (see lead times)
```

- Steps inside the next 2 weeks go on the plan as a slot or a task with an owner.
- A step whose date has passed is **LATE**. It goes to the top of the gap list with the
  fastest fix: shorter prep, a stand-in, or moving the fixed point if it is flexible.
- Book-by dates for meetings 2–6 weeks out go into the team context file, so invites go out
  in time.

## Default lead times

Adeyinka can change these.

| Meeting | Invite sent / slot locked at least |
|---|---|
| External: capital, customer, partner, government | 10 working days before |
| External, follow-up already agreed in the last meeting | 5 working days before |
| New execs, direct reports, internal | 2 working days before |
| Office check-ins (15 min, in person) | Same week is fine |

Most "random" weeks come from booking after the book-by date. The Friday score checks this
(see [`../daily-calendar-qa/scoring.md`](../daily-calendar-qa/scoring.md)).

*Example (invented):* a customer meeting is fixed for Mon 14 Dec. Book-by is 10 working days
before (Mon 30 Nov). Internal prep goes Wed 9 or Thu 10 Dec. Agenda goes Thu 10 Dec. Brief
to Bunmi goes Sun 13 Dec evening. If today is Wed 2 Dec and no invite has gone, the invite
step is LATE.
