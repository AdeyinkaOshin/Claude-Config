# The hourly cycle (:00 tower, :30 people)

Cloud routines can't run more often than once an hour. So instead of one fast
loop there are two hourly loops, half an hour apart.

| Minute | Who | What happens |
|---|---|---|
| **:00** | Tower routine (Logan's account), cron `0 * * * *` | 1) Sweep: mirror the Station into `station/`, read ops logs. 2) `judgment-intake`: copy feedback from `claude/judgment-*`, apply it, resolve or re-open items, file new ones. 3) `work-intake`: copy results from `claude/work-*`, set statuses, file new requests, print the per-flight summary. Push to `main`. |
| **:30** | Each person's routine (e.g. Bunmi's "VGG hourly"), cron `30 * * * *` | 1) `judgment-review`: judge up to 5 pending items, push feedback to `claude/judgment-<handle>`. 2) `work-run` (routine mode): run up to 3 pending requests, push results to `claude/work-<handle>`. |

## Invented worked example (times WAT)

- 09:00 — tower files a judgment item for Bunmi ("Example: is this note safe
  to send to the board as-is?") and a work request ("Example: draft a reply to
  the venue thread").
- 09:30 — Bunmi's routine writes a feedback file (verdict `adjust`, with
  specific edits) and a result file (outcome `partial`: "draft in Bunmi's
  Outlook Drafts, waiting on Bunmi to send").
- 10:00 — tower copies both onto `main`, applies the edits, re-opens the
  judgment item at rev 2 with a tower note, marks the work request `partial`,
  and the Station flight gets a note.
- 10:30 — Bunmi's routine looks at rev 2 only (what changed). Verdict `on_track`.
- 11:00 — tower resolves the item; the flight lands.

One full round trip per hour. A run that starts late just picks up the other
side's work one cycle later; nothing breaks.

## Why staggered branches

- Each person's routine only ever adds files in its own folder, on its own
  `claude/<loop>-<handle>` branch, so it can't conflict with `main`.
- The tower **copies** those files onto `main` instead of merging. That keeps
  every commit on `main` authored by the tower, which is what lets the tower's
  routine keep pushing to `main`.
- A branch that touches anything outside its folder is skipped and flagged.

## Time zones

Routines run in each account's local time zone. Lagos (WAT, UTC+1) and US
Eastern differ by whole hours, so :00 and :30 line up. If someone ever sits in
a half-hour time zone, switch that person to :15 / :45.

## Faster than hourly

A **local** scheduled task in the Claude desktop app can run every few
minutes, but only while that computer is on and the app is open. Use only for
a crunch week; cloud is the default because it runs with the laptop closed.
See [../../01-setup/07-scheduled-tasks-and-routines.md](../../01-setup/07-scheduled-tasks-and-routines.md).

## Where the ops log fits

The EA's `/ops-runway` session is not on this clock. Its log is pushed when
the session runs and is picked up by the tower's sweep at a later :00. See
[../ops-runway/branches-and-pickup.md](../ops-runway/branches-and-pickup.md).
