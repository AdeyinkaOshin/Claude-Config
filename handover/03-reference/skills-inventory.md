---
title: Skills inventory
version: v1.1
last_updated: 2026-11-26
owner: Adeyinka Oshin
sources: /root/.claude/skills/synced/*/manifest.json and SKILL.md files (claude.ai account skills, manifest refreshed 2026-11-25 16:18 UTC); Logan-VGG repo paths .claude/skills/, skills-bunmi/, skills-margaret/ (READMEs and SKILL.md headers, git history)
---

# Skills inventory

> Every Claude skill in use around Adeyinka's role, where it lives, who uses it, how
> current it is, and which handover doc explains it. A **skill** is a packaged set of
> instructions Claude loads when a task matches it (see [glossary](glossary.md)).
> How to install or write one: [`../01-setup/06-creating-a-skill.md`](../01-setup/06-creating-a-skill.md).

## Where skills live (four places)

| Place | What it is | How it gets there | How to see what's there |
|---|---|---|---|
| **claude.ai account skills** | Skills switched on in Adeyinka's claude.ai account (Settings → Capabilities → Skills). They follow the account into claude.ai chats, Cowork and Claude Code cloud sessions. In a cloud session they are synced to `/root/.claude/skills/synced/<account-id>/<skill>/`, with a `manifest.json` listing each skill's `source` and `updatedAt`. In Claude Code they appear with the prefix `anthropic-skills:` | Uploaded as a `.zip` (custom ones arrive as `source: plugin`), or provided by Anthropic | Settings → Capabilities → Skills, or read the `manifest.json` in a cloud session |
| **Repo skills** | Skills committed to the Logan-VGG repo under `.claude/skills/`. Any Claude Code session opened in that repo gets them | `git pull` | `ls .claude/skills/` in the repo |
| **Bunmi's skills** | Skill folders in the Logan-VGG repo under `skills-bunmi/`, built for Bunmi's own Claude. Some have a ready-to-upload `.zip` next to the folder | Bunmi (or someone at Bunmi's machine) copies the folder to `~/.claude/skills/` or uploads the `.zip` in claude.ai | `skills-bunmi/README.md` |
| **Margaret's skills** | Skill folders + `.zip` packages in the Logan-VGG repo under `skills-margaret/`, built for Margaret (VigiPay) | Margaret uploads the `.zip` to a claude.ai project, or copies the folder for Claude Code | `skills-margaret/README.md` |

**Dates.** Account skills: the manifest `updatedAt`. Repo skills: the last commit or the
version line in the skill's header. The repo copy available here has history only back to
16 Oct 2026, so "≤ 16 Oct 2026" means "last changed on or before that date".

**Handover doc column.** Paths are relative to `handover/`. Folders marked were not yet
written when this table was made. **[TO CONFIRM: final folder names for the docs once the 02-workflows map exists.]**

---

## 1. Custom VGG skills

### 1a. In Adeyinka's claude.ai account (manifest `source: plugin`)

| Skill | What it does | Who uses it | Installed | Last updated | Handover doc |
|---|---|---|---|---|---|
| `calendar-qa` | Plans Bunmi's 2-week look-ahead and the context file for the calendar team, then checks the team's bookings daily / Thursday / Sunday / Friday; never books or sends. | Adeyinka | claude.ai account (synced) | 2026-11-25 | `02-workflows/two-week-look-ahead/`, `02-workflows/daily-calendar-qa/` |
| `bunmi-weekly-context-file` | Builds Bunmi's weekly context file (live deals, owners, tiers 1–3, where Bunmi is, what to book) from Outlook, SharePoint and WhatsApp. | Adeyinka builds it; Favour uses the output | claude.ai account (synced) | 2026-11-07 | `02-workflows/weekly-context-file/` |
| `friday-calendar-check` | Checks the weekly draft of Bunmi's schedule against the Calendar Brief and the CT-00 to CT-04 working bibles, and writes the feedback note. | Favour (or the EA on duty), in the "Favour Calendar Management" project | claude.ai account (synced) | 2026-10-24 | `02-workflows/friday-calendar-check/` |
| `meeting-artifacts` | After a meeting, turns the transcript into a review folder: context note, actions, menu of documents needed, and audience-specific drafts. Draft only. | Adeyinka (manual runs); Bunmi's account (scheduled) | claude.ai account (synced) — **this copy is v1.1**; the repo copy is v1.4 | 2026-10-15 (account copy) | `02-workflows/meeting-review/` |
| `vgg-logan-weekly-report` | Builds Logan's VGG-branded weekly Word status report for Central Ops from the "Logan AI" WhatsApp export and meeting transcripts. | Adeyinka | claude.ai account (synced) | 2026-10-05 | [`02-workflows/weekly-reports/`](../02-workflows/weekly-reports/README.md) |

**Decided 26 Nov 2026:** the account copy of `meeting-artifacts` is being replaced with the repo's v1.4 zip. `calendar-qa` and `friday-calendar-check` are now **v1.1** (26 Nov: clash check with Favour's draft; 24 Nov meeting lengths). Their editable source and upload zips live in `Claude-Config/skills/`.

### 1b. Repo skills (Logan-VGG `.claude/skills/`)

These run the "air traffic control" system (Station, judgment queue, work requests).

| Skill | What it does | Who uses it | Installed | Last updated | Handover doc |
|---|---|---|---|---|---|
| `ops-runway` | Walks through every Station flight routed to the Ops lane one at a time, with context and next steps, drafts messages, and logs outcomes to `ops/log/`. | Adeyinka | Logan-VGG repo | ≤ 16 Oct 2026 | `02-workflows/ops-runway/` |
| `judgment-intake` | Tower side: files judgment questions for senior people and acts on their feedback (resolve or re-open). Hourly at :00. | Logan (tower) | Logan-VGG repo | ≤ 16 Oct 2026 | `02-workflows/judgment-and-work-requests/` |
| `judgment-review` | Exec side: reviews judgment items assigned to that person and writes append-only feedback. Hourly at :30. | Bunmi and other reviewers (via their routines) | Logan-VGG repo | ≤ 16 Oct 2026 | `02-workflows/judgment-and-work-requests/` |
| `work-intake` | Tower side: files work requests for someone else's Claude and picks up their result reports. Hourly at :00. | Logan (tower) | Logan-VGG repo | ≤ 16 Oct 2026 | `02-workflows/judgment-and-work-requests/` |
| `work-run` | Assignee side: runs work requests with the assignee's own connectors within their policy; unattended runs never send. | Bunmi, Adeyinka (inside `ops-runway`) | Logan-VGG repo | ≤ 16 Oct 2026 | `02-workflows/judgment-and-work-requests/` |

### 1c. Bunmi's skills (Logan-VGG `skills-bunmi/`)

Install pack v1 dated 6 Oct 2026. The shared review rules (`_shared/external-qa.md`) were
last updated 9 Nov 2026. Adeyinka does the first-pass review on everything these produce;
Ayomide does final QA on anything external.

| Skill | What it does | Who uses it | Installed | Last updated | Handover doc |
|---|---|---|---|---|---|
| `meeting-artifacts` | Same after-meeting loop as above; v1.4 keeps the full transcript in each folder and runs as an hourly cloud routine in Bunmi's account, writing to the Executive Office SharePoint site. | Bunmi's account (scheduled); output reviewed by Adeyinka and Ayomide | Folder + `meeting-artifacts.zip` | 2026-11-20 (v1.4) | `02-workflows/meeting-review/` |
| `pre-meeting-brief` | Evening before: a short context note per meeting for all attendees, with a 3-line top for Bunmi; flags meetings 48h out with no agenda. | Bunmi; Adeyinka can run it on request | Folder only | ≤ 16 Oct 2026 | **[TO CONFIRM: is this in use, and which doc covers it?]** |
| `followup-drafter` | Drafts Bunmi's post-meeting WhatsApp follow-ups, team emails and next-meeting proposal; keep-warm mode for neglected contacts. | Called by `meeting-artifacts`; Adeyinka | Folder only | ≤ 16 Oct 2026 | `02-workflows/meeting-review/` |
| `concept-docs` | Drafts Bunmi's concept documents (teasers, profiles, business cases, partnership concepts) in VGG house style, ready for Ayomide's QA. | Called by `meeting-artifacts`; Adeyinka on request | Folder only | ≤ 16 Oct 2026 | **[TO CONFIRM]** |
| `okr-alignment` | Maps subsidiary OKRs to Group goals, scores alignment, drafts tighter OKRs and a routing key for prioritising tasks. | Bunmi (Uche checks the routing key) | Folder only | ≤ 16 Oct 2026 | **[TO CONFIRM]** |
| `opportunity-screener` | Screens inbound pitches and "can we research these guys?" forwards; recommends pursue / route / park / decline with a reply draft. | Bunmi; Adeyinka via `ops-runway` | Folder only | ≤ 16 Oct 2026 | **[TO CONFIRM]** |
| `week-ahead` | Sunday look-ahead of the next 7 days (plus 30/90-day headline), clashes, drive time, trip / city-day plans. | Bunmi; output for Adeyinka and the EA team | Folder only | ≤ 16 Oct 2026 | `02-workflows/two-week-look-ahead/` (overlaps with `calendar-qa` Plan mode) **[TO CONFIRM: is `week-ahead` still used now that `calendar-qa` Plan mode exists?]** |
| `ceo-review-catchup` | Repairs and schedules Bunmi's Weekly CEO Review in Bunmi's notes vault (backfills missing notes and trackers). | Bunmi | Folder only | ≤ 16 Oct 2026 | **[TO CONFIRM]** |
| `deal-handoff` | Turns a request that needs several VGG firms into a one-page hand-off, a first-reply draft and a register row with a clock; sweep mode for overdue hand-offs. | Bunmi's office | Folder + `deal-handoff.zip` | v1.0, 12 Oct 2026 | **[TO CONFIRM]** |
| `ghc-deal-brief` | Turns Bunmi's raw post-meeting deal thoughts into a structured brief for a portfolio MD group plus a private note; never posts. | Bunmi | Folder + `ghc-deal-brief.zip` | ≤ 16 Oct 2026 (based on a 12 Oct playbook) | **[TO CONFIRM]** |

**[TO CONFIRM: which of Bunmi's skills (other than `meeting-artifacts`) are actually installed and in use in Bunmi's Claude today.]**

### 1d. Margaret's skills (Logan-VGG `skills-margaret/`)

| Skill | What it does | Who uses it | Installed | Last updated | Handover doc |
|---|---|---|---|---|---|
| `executive-decision-pack` | Turns messy context into Margaret's executive documents (one-pagers, decision memos, deck plans, PMO weekly briefs, senior emails), one template per type; learns from corrections. | Margaret (VigiPay) | Folder + `executive-decision-pack.zip` | v2, 15 Oct 2026 | **[TO CONFIRM]** |
| `vigipay-ld-loop` | VigiPay HR's Learning & Development follow-up loop: who's due, drafted nudges and check-ins, reply scoring, quarterly report. | VigiPay HR (not yet live) | Folder + `vigipay-ld-loop.zip` | v0, 15 Oct 2026 (waiting on HR's process doc) | **[TO CONFIRM]** |

**[TO CONFIRM: did Margaret's v2 pack reach Margaret and get installed? The repo notes say the files still had to be sent by hand.]**

---

## 2. Anthropic skills (not VGG-built)

From the account manifest. `source: anthropic` = Anthropic's standard file skills;
`source: anthropic-example` = Anthropic example skills. They update automatically; you do
not maintain them.

| Skill | Source | What it does | Who uses it | Last updated | Handover doc |
|---|---|---|---|---|---|
| `morning` | anthropic-example | Renders your morning brief (your day as a drawing + Needs attention / Resolved) as an HTML artifact, or sets it up as a weekday scheduled task. | Adeyinka (own day); Bunmi has a copy in Bunmi's own account | 2026-09-14 | [`02-workflows/weekly-reports/`](../02-workflows/weekly-reports/README.md) |
| `docx` | anthropic | Create/read/edit Word files. Used under the hood by the weekly report. | Everyone | 2026-11-20 | — |
| `xlsx` | anthropic | Create/read/edit spreadsheets. | Everyone | 2026-11-16 | — |
| `pptx` | anthropic | Create/read/edit PowerPoint files. | Everyone | 2026-11-16 | — |
| `pdf` | anthropic | Read, merge, split, fill and create PDFs. | Everyone | 2026-11-06 | — |
| `docs` | anthropic-example | Claude Docs: editable, shareable documents in claude.ai. | Everyone | 2026-09-30 | — |
| `google-workspace` | anthropic-example | Rules for creating or changing Google Docs/Sheets/Slides. | Rarely (VGG is on Microsoft 365) | 2026-11-20 | — |
| `skill-creator` | anthropic-example | Create, edit and test skills. | Whoever maintains skills | 2026-11-23 | [`01-setup/06-creating-a-skill.md`](../01-setup/06-creating-a-skill.md) |
| `artifact-emulator` | anthropic-example | Lets Claude screenshot an artifact it made, in a cloud session. | Claude, automatically | 2026-11-16 | — |
| `import-memory` | anthropic-example | Import memory from another AI assistant. | Not used in the workflows | 2026-11-24 | — |

### Also visible in Claude Code cloud sessions (not part of the EA workflows)

Claude Code also lists its own built-in skills (e.g. code review, settings/hooks help,
artifact design) and organisation plugins (Canva, Figma, an "operations" plugin with
status-report / process-doc / runbook skills). None of the EA workflows depend on them.
**[TO CONFIRM: whether any of the Canva, Figma or operations plugin skills are used in Adeyinka's work.]**

## Gaps to confirm

- **[TO CONFIRM: final folder names for the docs once the 02-workflows map exists.]**
- **[TO CONFIRM: should the account copy of `meeting-artifacts` (v1.1) be replaced with the repo's v1.4 zip?]**
- **[TO CONFIRM: is `pre-meeting-brief` in use, and which doc covers it?]**
- **[TO CONFIRM: is `week-ahead` still used now that `calendar-qa` Plan mode exists?]**
- **[TO CONFIRM: which of Bunmi's skills (other than `meeting-artifacts`) are installed and in use today.]**
- **[TO CONFIRM: did Margaret's v2 pack reach Margaret and get installed?]**
- **[TO CONFIRM: handover docs for concept-docs, okr-alignment, opportunity-screener, ceo-review-catchup, deal-handoff, ghc-deal-brief and Margaret's skills — or are they out of scope for the new person?]**
- **[TO CONFIRM: whether any Canva, Figma or operations plugin skills are used.]**

## Change history

| Version | Date | Change |
|---|---|---|
| v1.0 | 2026-11-25 | First written |
| v1.1 | 2026-11-26 | calendar-qa and friday-calendar-check v1.1; sources now kept in Claude-Config/skills/ |
