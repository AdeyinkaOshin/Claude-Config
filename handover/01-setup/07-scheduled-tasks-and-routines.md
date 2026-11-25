---
title: Scheduled tasks and routines
version: v1.0
last_updated: 2026-11-25
owner: Adeyinka Oshin
---

# 07 — Scheduled tasks and routines

> A **routine** (also called a scheduled task) is a Claude session that starts by itself
> on a schedule, does a job, and stops. It's how the hourly judgment/work loop and the
> weekly handover update run without anyone pressing a button.

## 1. Routines in this job

| Routine | When (WAT) | Where it runs | What it does | Doc |
|---|---|---|---|---|
| Judgment + work run (exec side) | Hourly at :30 | Each exec's account, on `Logan-VGG` | `/judgment-review` then `/work-run` | `../02-workflows/judgment-and-work-requests/` |
| Tower intake (Logan side) | Hourly at :00 | Logan's account | `/judgment-intake`, `/work-intake`, Station mirror | same |
| Handover pack update | Fridays 15:4x | Adeyinka's account, on `Claude-Config` | Updates these docs from the week's changes | `../03-reference/how-this-pack-stays-updated.md` |
| Calendar QA / context file / meeting loop | **[TO CONFIRM: are any of these scheduled, or all run by hand?]** | | | `../02-workflows/` |

## 2. Create a routine

1. Go to <https://claude.ai/code/routines> → **New routine**.
2. **Name** — short and clear, e.g. `Judgment review`.
3. **Instructions** — the prompt. Write it as a complete standalone instruction (every run
   starts fresh). Ready-made prompts: `Logan-VGG/judgment/ROUTINE-PROMPT.md`,
   `Logan-VGG/work/setup/bunmi/ROUTINE-PROMPT.md`.
4. **Repository** — the repo it works in.
5. **Environment** — Default unless it needs extra network hosts.
6. **Trigger** — Schedule. The form offers Hourly/Daily/Weekly. For an exact minute
   (e.g. :30), open Claude Code and type `/schedule update`, pick the routine, and ask for a
   cron like `30 * * * *`. Or ask Claude in a session to "create a scheduled task" with the
   time and time zone — it can set the cron directly.
7. **Connectors** — switch on only what the job needs.
8. **Create**, then click **Run now** once and read the result.

## 3. Cron in one minute

`minute hour day-of-month month day-of-week`, e.g.

| Cron | Means |
|---|---|
| `30 * * * *` | Every hour at :30 |
| `0 8 * * 1-5` | 08:00 weekdays |
| `47 15 * * 5` | 15:47 on Fridays |

Prefix with `CRON_TZ=Africa/Lagos ` so times are WAT. Avoid exactly :00/:30 for
non-hourly jobs — busy times can be delayed.

## 4. Rules for unattended runs

- **Routines never send.** They draft and report "waiting on <person> to send".
- They never move or cancel calendar items.
- They commit to their own `claude/*` branch.
- Limits: cloud routines run at most hourly, with a daily cap per account.

## 5. When a routine misbehaves

| Symptom | Fix |
|---|---|
| Hasn't run for days | GitHub disconnected → reconnect at claude.ai/code, re-enable the routine |
| Green tick, nothing happened | Open the run and read the last message — green only means it finished |
| Push failed | Repo access or GitHub App missing — see `02-github-setup.md` |
| Connector "blocked" | Connector not turned on for the routine, or host not on the network allowlist |

## Change history
| Version | Date | Change |
|---|---|---|
| v1.0 | 2026-11-25 | First written |
