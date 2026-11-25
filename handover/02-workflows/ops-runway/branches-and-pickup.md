# Branches: how the ops log reaches main and the Station

## The short version

- `main` is the shared, official copy of the Logan-VGG repo.
- A Claude Code **cloud** session (and every cloud routine) can always push to
  branches whose names start with `claude/`, but usually **cannot** push to
  `main`. `main` carries other people's commits, and cloud sessions are only
  allowed to push to it in narrow cases.
- So when you run `/ops-runway` in a cloud session, your log commit lands on
  the session's own branch, for example `claude/<adjective-name-xxxx>`
  (invented example: `claude/quiet-otter-ab12cd`).
- The tower (Logan's side) fetches those branches and **copies** the
  `ops/log/` files onto `main`. It copies rather than merges, so every commit
  on `main` stays authored by the tower and its own routine can keep pushing.
- After the copy, the sweep reads the log lines and updates the flights on the
  Station. The next mirror commit (`station: mirror N flights (<timestamp>)`)
  then shows the change in `station/`.

## Branch names you will see

| Branch | Written by | Contains |
|---|---|---|
| `main` | The tower (Logan's account) | Everything official: the Station mirror, copied ops logs, copied feedback and results, queue files |
| `claude/<random-name>` | Any interactive cloud session, including `/ops-runway` | Whatever that session committed — for ops sessions, only `ops/log/` |
| `claude/judgment-<handle>` | An exec's :30 routine | Only `judgment/feedback/` files |
| `claude/work-<handle>` | An assignee's :30 routine, or the work-request part of `/ops-runway` | Only `work/results/` files |

The tower refuses to copy from a `claude/judgment-*` or `claude/work-*`
branch that touches anything outside its own folder. That is the guardrail.

## What the git history shows (as of 25 Nov 2026)

- Mirror commits arrive in bursts: several an hour on busy days, then gaps of
  several days.
- Ops log copies onto `main` are made every few days, with messages like
  "ops/log: copy … logs from claude/* branches".

So "the tower picks it up within the hour" is the design, not always the
practice. **[TO CONFIRM: is the tower sweep currently hourly, and does it
fetch every `claude/*` branch automatically, or does Logan copy ops logs by
hand?]**

## If you have direct push rights to main

If Logan gives you push rights and you work from a local clone (not a cloud
session), `git push` goes straight to `main` and the next sweep sees it
without any copy step. Ask Logan before doing this; the repo's `CLAUDE.md`
treats history rewrites and force pushes as ask-first.
