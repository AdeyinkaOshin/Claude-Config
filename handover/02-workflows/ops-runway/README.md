---
title: Ops runway session (/ops-runway) and the ops log
version: v1.0
last_updated: 2026-11-25
owner: Adeyinka Oshin
sources: logansherzog/Logan-VGG — CLAUDE.md, README.md, .claude/skills/ops-runway/SKILL.md, .claude/skills/work-run/SKILL.md, ops/log/ (format only), ops/openops-worker.md, station/README.md, git history
---

# Ops runway session (/ops-runway) and the ops log

> The Ops runway is the human-touch part of Logan Herzog's "AI Traffic Control"
> setup for VGG: calls, confirmations, follow-ups, bookings, chasing people.
> Logan's side (the "tower") decides which flights (tasks) go to Ops. Adeyinka
> works them in a Claude Code session on the `logansherzog/Logan-VGG` repo by
> typing `/ops-runway`. Claude walks through the Ops flights one at a time,
> drafts messages for Adeyinka to send personally, and writes one line per
> flight into a dated ops log file. The tower reads that log and updates the
> Station, so everyone can see what moved. This is the main daily working loop
> for whoever holds the Executive Assistant seat.

## 1. Purpose

Problem it solves: hundreds of open flights sit on the Station, and the Ops
ones need a person to make them happen. Without a routine, they go stale and
nobody upstream knows what was done.

"Done" for a session looks like:
- Every cleared Ops flight was either worked, skipped, or sent back to the tower.
- Each one has one line in today's `ops/log/YYYY-MM-DD.md` file.
- The log is committed and pushed, so the tower picks it up.
- Any messages are drafted and either sent by the EA personally or clearly
  marked "drafted, not sent".

## 2. When it runs

- **Trigger:** manual. The EA starts it whenever they sit down to work the
  queue. In practice the log history shows sessions every few working days,
  often more than once a day. **[TO CONFIRM: is there an expected cadence, e.g.
  every working day by 12:00 WAT?]**
- **How to start it:** in a Claude Code session opened on the Logan-VGG repo,
  type `/ops-runway`. These phrases also start it: "what's on my plate",
  "start my ops runway", "next ops task".
- **What happens downstream on a clock:** the tower's sweep reads the ops log
  and updates the Station. The skill says this happens on the hourly sweep.
  The git history shows the copy of ops logs onto `main` happening every few
  days, by Logan's side. See section 8 and
  [branches-and-pickup.md](branches-and-pickup.md).
- Time zone for log file names and timestamps: **Lagos time (WAT)**.

## 3. Who does what

| Person / role | Responsibility |
|---|---|
| Logan Herzog (the tower) | Decides which flights go to the Ops lane. Runs the sweep that mirrors the Station into the repo and reads ops logs back. Answers "back-to-tower" questions. Owns the repo and its rules. |
| Adeyinka Oshin (EA, Ops runway) | Runs `/ops-runway`. Works each flight, sends messages personally, confirms to Claude what was actually sent, pushes the log. Can also press **Land** / **Waiting** on the Station directly. |
| Claude (in the EA's session) | Reads the Station mirror, presents one flight at a time with next steps and drafts, runs named skills in draft mode, writes and pushes the ops log. Never sends anything. |
| Bunmi Akinyemiju (GCEO) | Source of most flights. Decisions that only Bunmi can make are sent back to the tower, not decided in the session. |
| Udeme and the calendar team | Do much of the booking and emailing that flights depend on; the EA chases and checks their work. |
| Uche (Chief of Staff) | Offered a deeper link between the tower and the Central Ops context system (see `ops/openops-worker.md` in the repo; still a placeholder). |

## 4. Before you start (prerequisites)

1. **Claude account with Claude Code**, able to open cloud sessions — see
   [../../01-setup/01-claude-account-and-cloud-sessions.md](../../01-setup/01-claude-account-and-cloud-sessions.md).
2. **GitHub access to `logansherzog/Logan-VGG`** (private). Logan must send
   the collaborator invite; Claude may not add collaborators without Logan's
   explicit yes. See [../../01-setup/02-github-setup.md](../../01-setup/02-github-setup.md).
3. **Read the repo's `CLAUDE.md` rules** (privacy, sender choice). Summary in
   [../../03-reference/logan-vgg-repo-map.md](../../03-reference/logan-vgg-repo-map.md)
   and [../../01-setup/05-claude-md-files.md](../../01-setup/05-claude-md-files.md).
4. **The skill is already in the repo** at `.claude/skills/ops-runway/SKILL.md`,
   so it loads automatically in any Claude Code session opened on the repo.
   Nothing to install.
5. **Your handle.** The skill and the work-request tool currently use the
   handle `adeyinka` (it also appears in `judgment/people.yaml`). A successor
   needs Logan to either keep that handle or add a new one and update the skill.
   **[TO CONFIRM: will the successor reuse the `adeyinka` handle or get their own?]**
6. **Station access** (the live Station is a private claude.ai page; its link
   is in `station/README.md`). Needed to press Land / Waiting yourself.
   **[TO CONFIRM: does Logan need to share the Station page with the successor separately?]**
7. **Connectors** for your own messages (Outlook, WhatsApp, Teams) are not
   needed by the skill itself, which only drafts. See
   [../../01-setup/03-connectors.md](../../01-setup/03-connectors.md).

## 5. Step by step

1. **Open a session on the repo.** Go to claude.ai/code (or the desktop app's
   Code tab), start a new session, and pick the `Logan-VGG` repository.
   The session clones the repo and starts on a fresh branch named
   `claude/<something>`. That is normal — see
   [branches-and-pickup.md](branches-and-pickup.md).
2. **Type `/ops-runway`.** Claude then, without being asked:
   - pulls the latest repo so the Station mirror is fresh;
   - reads `station/README.md` and checks the "Last mirrored" time. If it is
     more than 2 hours old, Claude warns that the list may be behind;
   - reads `station/flights.md` and collects every flight with lane **ops**
     and gate **cleared** (flights with gate **held** are skipped until the next
     tower run — see [../station-and-flights/flight-statuses.md](../station-and-flights/flight-statuses.md));
   - drops anything already logged as done in today's or yesterday's ops log;
   - runs a check for work requests filed for the EA's Claude
     (`python3 work/tools/work.py pending --me adeyinka`).
3. **Read the opening summary.** Claude shows how many Ops flights there are,
   how many are overdue / due today / waiting on someone, and the order:
   overdue first, then due today, then this week, then no date (oldest first).
   If there are work requests, it asks whether to do those first or after.
4. **Work one flight at a time.** For each flight Claude shows: code and title,
   owner, due date, rock (goal it serves), why it is here, what is already
   known (with source links), what "done" looks like, and 2–5 numbered next
   steps naming the person, the channel and what to say. If a message is
   needed, a ready-to-send draft is included.
   - If the flight names one of Bunmi's skills (pre-meeting brief, meeting
     artifacts, follow-up drafter, concept docs, week ahead, opportunity
     screener, OKR alignment, CEO review catch-up), step 1 will be "Run <skill>".
     Those skills live in `skills-bunmi/` and only ever draft. Anything external
     also goes to Ayomide for QA before it leaves.
   - If the flight needs a call only Logan or Bunmi can make, step 1 is
     "Send back to the tower".
5. **Answer the question Claude asks:** "Do it now, skip for later, or send
   back to the tower?"
6. **Send messages yourself.** Claude says "Draft ready. You send it." Copy the
   draft into your own email / WhatsApp / Teams and send it. Then tell Claude
   "sent" (or "done", "I messaged them"). Until you do, the log says
   "drafted, not sent".
7. **Correct anything wrong.** If a name or fact is wrong, say so; Claude puts
   the correction in the log line so the tower sees it.
8. **Claude writes the log line** to `ops/log/<today>.md` (creates the file if
   needed). One line per flight. Format and status words are in
   [ops-log-format.md](ops-log-format.md).
9. **Commits happen every 3 flights and at the end.** Claude commits only the
   `ops/log/` file with a message like `ops: <N> flights worked (<date>)` and
   pushes. If the push is rejected it pulls with rebase and pushes again. In a
   cloud session the push lands on the session's `claude/...` branch, not
   `main`.
10. **Work requests (if any).** Claude runs them through the work-run skill in
    interactive mode, one at a time ("Run it, skip for now, or decline?").
    Results go to `work/results/` on the branch `claude/work-adeyinka`, not in
    the ops log. Afterwards Claude switches back to `main` before more flights,
    so later log pushes do not end up on the work branch. Full detail in
    [../judgment-and-work-requests/README.md](../judgment-and-work-requests/README.md).
11. **End of session.** Claude gives a 4-line summary: counts of done /
    waiting / skipped / sent back, the next follow-up date, and anything urgent
    for Logan. It pushes the log a final time.
12. **Make sure the tower sees it.** Claude will say updates reach the Station
    "within the hour". For an instant update, press **Land** (done) or
    **Waiting** on the Station yourself. If the log is on a `claude/...`
    branch, tell Logan the branch name. **[TO CONFIRM: should the EA always
    message Logan the branch name after a session, given copies to `main` are
    happening every few days rather than hourly?]**

## 6. Output — what you get and where it goes

| Output | Where | Who uses it |
|---|---|---|
| One line per flight worked | `ops/log/YYYY-MM-DD.md` (WAT date), first on the session's `claude/...` branch, later copied to `main` | The tower sweep, which updates each flight on the Station |
| Drafted messages | In the chat only (the EA copies and sends) | The EA |
| Work-request results | `work/results/` on `claude/work-adeyinka` | The tower's work-intake run |
| Back-to-tower questions | In the log line, written as a one-line yes/no question | Logan |
| End-of-session summary | In the chat | The EA; pass urgent items to Logan |

Other skills can also add a summary line to the same day's ops log (for
example, the calendar QA skill adds one line per check). Treat those as part
of the same file.

## 7. Review and approval rules

- **Claude never sends anything on the EA's behalf** — no email, Teams,
  WhatsApp or Slack. It drafts; the EA sends.
- **Never log "sent" until the EA confirms it.** Keep three things separate in
  each line: what the EA did, what is drafted and waiting, and what is waiting
  on others.
- **Never edit `station/`.** It is a read-only mirror rebuilt by the tower.
  Changes go through the Station itself or through the ops log.
- **Don't paste flight details anywhere outside this repo** (repo rule; see the
  repo map).
- **Work requests:** a message is sent only if the policy allows `send` *and*
  the EA has said yes to the exact message. With no policy file for the EA,
  only read + draft are allowed.
- **Sender choice rule** in the repo's `CLAUDE.md` (ask which mailbox each
  time) applies to Logan's own sessions. Teammates send from their own
  accounts under their policy file in `work/policies/`.
  **[TO CONFIRM: there is no policy file for the EA's handle yet — is read + draft the intended limit?]**
- When unsure or blocked: mark **back-to-tower** with a one-line question and
  move on. Don't guess.

## 8. Common problems and fixes

| Symptom | Fix |
|---|---|
| Claude says the mirror is more than 2 hours (or days) old | The tower hasn't run its sweep. Work the list anyway, but expect some flights already to be done. Tell Logan the mirror is stale. |
| A flight you finished yesterday shows up again | Yesterday's log may still be sitting on another `claude/...` branch, so this session can't see it. Tell Claude it's done; it will skip it. Ask Logan to copy the older log to `main`. |
| Push rejected | Claude retries after `git pull --rebase`. If it still fails, ask Claude to show the error; check your GitHub access ([../../01-setup/02-github-setup.md](../../01-setup/02-github-setup.md)). |
| Push went to `claude/...`, not `main` | Expected in cloud sessions. The tower copies logs from those branches. See [branches-and-pickup.md](branches-and-pickup.md). |
| After running work requests, the next log push went to `claude/work-adeyinka` | Claude should switch back to `main` first. Ask it to move the log commit back (`git checkout main && git pull --ff-only`, then re-add the log). |
| A flight is "held" | Held flights clear after the next tower run. Don't work them yet. |
| `/ops-runway` doesn't respond as a command | The session isn't opened on the Logan-VGG repo, or the repo didn't clone. Start a new session and pick the repo. |
| Station not updated hours after the session | Press Land / Waiting on the Station yourself and tell Logan the branch name. |

## 9. Gaps to confirm

- **[TO CONFIRM: is there an expected cadence, e.g. every working day by 12:00 WAT?]**
- **[TO CONFIRM: will the successor reuse the `adeyinka` handle or get their own?]** (The skill, `work.py` calls and `judgment/people.yaml` all use it; the skill text also uses the spelling "Adeyinke".)
- **[TO CONFIRM: does Logan need to share the Station page with the successor separately?]**
- **[TO CONFIRM: should the EA always message Logan the branch name after a session, given copies to `main` are happening every few days rather than hourly?]**
- **[TO CONFIRM: there is no policy file for the EA's handle yet — is read + draft the intended limit?]**

## Change history

| Version | Date | Change |
|---|---|---|
| v1.0 | 2026-11-25 | First written |
