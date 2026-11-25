---
title: Glossary
version: v1.0
last_updated: 2026-11-25
owner: Adeyinka Oshin
sources: Logan-VGG repo station/README.md, judgment/README.md, work/README.md, work/policies/; skills calendar-qa, bunmi-weekly-context-file, friday-calendar-check, meeting-artifacts, ops-runway, morning, vgg-logan-weekly-report
---

# Glossary

> Terms you will meet in the skills, the Station and the team chats, in plain English.
> Grouped by topic; alphabetical within each group.

## A. Claude and its tools

| Term | Meaning |
|---|---|
| **Artifact** | A web page Claude publishes in claude.ai (private by default), e.g. the morning brief or the Station. |
| **CLAUDE.md** | A file of standing instructions at the top of a repo (or in your home folder) that Claude reads at the start of every session in that place. Each repo used here has one with hard rules (privacy, what needs approval). See [`../01-setup/05-claude-md-files.md`](../01-setup/05-claude-md-files.md). |
| **Claude Code** | The version of Claude that works in files and repos (on a computer or in a cloud session). Repo skills and routines run here. |
| **Claude project** | A workspace in claude.ai with its own files and instructions (e.g. Favour's calendar project, which holds the context file). |
| **Cloud session** | A Claude Code session running in a container on claude.ai rather than on your laptop. Outbound internet is limited to an allowlist. |
| **Connector** | A link that lets Claude read (and sometimes write to) another app: Microsoft 365 (Outlook mail, calendar, Teams, SharePoint/OneDrive), WhatsApp, Fireflies, etc. No connector = Claude can't see that data. See [`../01-setup/03-connectors.md`](../01-setup/03-connectors.md). |
| **Cowork** | claude.ai's desktop-style working mode where Claude uses your connectors and files; the morning brief can run here. |
| **MCP (Model Context Protocol)** | The standard that connectors are built on. An "MCP server" is the program that exposes an app's actions (search mail, read chat) as tools Claude can call. The WhatsApp connector is a small MCP server on Railway. |
| **Plugin** | A bundle that can carry skills, connectors and commands. Custom VGG skills uploaded to the account show as `source: plugin` in the skill manifest. |
| **Scheduled task / routine** | A Claude run that starts on a timer with a fixed prompt. "Routine" is the claude.ai cloud version (claude.ai/code/routines), at most hourly, runs with the laptop closed. A desktop scheduled task runs on your own machine while it's awake. Unattended runs never send anything. |
| **Skill** | A folder with a `SKILL.md` (instructions) and optional templates/scripts that Claude loads when your request matches its description, or when you type `/<skill-name>`. See [`skills-inventory.md`](skills-inventory.md). |
| **Slash command** | Typing `/name` (e.g. `/calendar-qa`, `/morning`) to start a skill directly. |
| **Trigger phrase** | The words in a skill's description that make Claude pick it up ("check the calendar", "run the Friday check"). |

## B. The Station ("air traffic control")

Logan's system for routing every task. The words are borrowed from aviation.

| Term | Meaning |
|---|---|
| **Station** | Logan's live task board (a claude.ai artifact). Every task is a flight. The Logan-VGG repo holds a read-only copy (the **Station mirror**, `station/`) refreshed hourly. Edit on the Station, never in the mirror. |
| **Flight** | One task on the Station, with a code (VGG-nnn), title, owner, lane, gate, workstream, due date, optional rock, a brief and source links. |
| **Flight plan** | The top-level destination and yearly goals the rocks and flights serve. |
| **Rock** | A big goal for the quarter/year (e.g. "N builds in daily use by year end"). Flights can be linked to a rock; the rocks table shows on-track/off-track and open/landed flight counts. |
| **Tower / Traffic Controller** | Logan (and Logan's hourly sweep routine) — decides where each flight goes. |
| **Tower sweep / heartbeat** | The tower's hourly run at :00 that refreshes the mirror, routes new flights, reads logs and lands finished flights. |
| **Lane** | Where a flight currently sits: `inbound` (new), `ops` (Ops runway), `watching`, `hold`, `claude` (for Claude to do), `landed` (done). |
| **Gate** | `held` (the tower keeps a new flight for one hourly run so judgment and checks can land first — don't work it yet) or `cleared` (ready to work). |
| **Runway** | A person's or team's work queue. The **Ops runway** is the human-touch work (calls, confirmations, follow-ups, bookings, chasing), worked by Adeyinka with the `ops-runway` skill. |
| **Land** | Mark a flight done. You can press **Land** (or **Waiting**) on the Station directly, or log it and the tower lands it within the hour. |
| **Ops log** | `ops/log/YYYY-MM-DD.md` in the repo (Lagos date): one line per flight worked (`done`, `waiting`, `in_progress`, `skipped`, `back-to-tower`) with the time in WAT. The tower reads it. |
| **Back to tower** | Sending a flight back to Logan because it needs Logan's decision; written as a one-line question. |
| **Workstream** | A label grouping flights (e.g. "Bunmi calendar"). |

## C. Judgment queue and work requests

| Term | Meaning |
|---|---|
| **Judgment queue** | `judgment/` in the repo. The tower asks a senior person a one-line question ("is this right?") as a file; that person's hourly routine at :30 writes a feedback file; the tower acts on it at :00. |
| **Verdict** | A reviewer's call: `on_track`, `adjust`, `stop` or `need_info`. |
| **Rev / revision** | A counter the tower bumps when it re-opens an item with new information (`needs_more`). |
| **Rule to remember** | The reusable lesson in a feedback file; repeated rules get built into skills. |
| **Append-only** | Feedback and result files are never edited or deleted; a new round is a new file. |
| **Work request** | `work/` in the repo. The tower asks someone's *Claude* to "go do this" with that person's own connectors; it writes back a short result summary. |
| **Action tiers (work requests)** | From lowest to highest: `read` < `draft` < `hold` (private block on own calendar) < `book` (event with attendees — counts as sending) < `send`. What runs is the stricter of the request and the person's **policy file** (`work/policies/<name>.yaml`). |
| **`claude/` branches** | Routines push to their own branch (e.g. `claude/judgment-<name>`, `claude/work-<name>`); the tower copies the new files to `main`. |
| **:00 / :30** | The two staggered hourly loops: tower at :00, each person's routine at :30. |

## D. Bunmi's calendar

| Term | Meaning |
|---|---|
| **Calendar standard** | The rules from Bunmi's calendar walkthrough with the EA team (24 Nov 2026), built into `calendar-qa`: outcomes not activity, plan 2 weeks ahead, every meeting has a reason, lock the next meeting the same day, theme days, measure every week. |
| **Calendar Brief** | Favour's reference document of Bunmi's tiers, protected times, day themes, to-book list and seasonal rules. Lives in the Executive Office OneDrive. |
| **CT-00 to CT-04 ("working bibles")** | The standing calendar rule documents that the Friday check cites (lengths, tiers, protected time…). |
| **Look-ahead** | The next 2 weeks planned out (from `calendar-qa` Plan mode): what each week is about, key days, each day's theme and anchor, top 3 meetings, work-backwards chains, gaps. (Bunmi's own `week-ahead` skill also makes a 7-day look-ahead.) |
| **Context file (weekly)** | Adeyinka's weekly file for Favour: live deals and owners with tiers 1–3, where Bunmi is each day, priority meetings to book, open questions. Ready by Friday 12:00 WAT. Versioned (v x.y). |
| **Context file for the calendar team** | A separate one-page-per-week file from `calendar-qa` Plan mode telling Udeme's team what is locked, what to book by when, and why. |
| **Day theme** | What a day is for, so related meetings cluster: capital/bank day, customer day, startup/portfolio day, real estate day, new execs and internal. |
| **Anchor** | The one meeting a day is built around. |
| **Top 3** | The three most important meetings in a day, locked first; everything else fits around them. A week is "planned" at ≥ 50%. |
| **Fixed point / working backwards** | A date that can't move (big meeting, trip, deadline). Plan back from it: brief the evening before, agenda 2 working days before, internal prep 2–3 working days before, documents ready, people briefed, invite sent by the **book-by date**. |
| **Book-by date / lead times** | Latest date to send an invite: external about 10 working days ahead, agreed follow-ups 5, internal 2. Booking later is "late". |
| **Locked** | On the calendar and holding. New things fit around it. |
| **Heads-down / protected time** | Blocks nobody books into (deep work, execution afternoons). |
| **Held** | How personal or family blocks are shown: the word "held", never any detail. |
| **Visibility-only ("free")** | Items put on the calendar as free with a colour, so they don't block time. |
| **Weekly score** | Friday: % of planned meetings that happened as planned, with a reason for each miss. |
| **BA Calendar group** | The WhatsApp group where Bunmi posts calendar requests. |
| **EA team mailbox** | A Microsoft 365 group mailbox for the EA team; its mail lands in Adeyinka's inbox. |

## E. Tiers — two different systems (do not mix them)

| Term | Meaning |
|---|---|
| **Tier 1–3 (to 5)** | **Priority** of a meeting or deal, set only by Bunmi or the Calendar & Technical Team sync list. 1 = must happen this week/visit; 2 = important, book after tier 1; 3 = book if there's room, owner can lead; 4–5 = lower, kept out of the context file. Tier 1–3 needs a one-page pre-read 24h ahead. Tier sits on the meeting/deal, not the person. |
| **Tier A / B / C** | **Review level** of a meeting in the meeting loop. A = internal only; B = partner or deal (any outside attendee or a priority deal); C = strategic (board, investors, government, regulators, anyone on the Tier C list). Decides what gets drafted. **Never convert A/B/C into 1/2/3.** |
| **Excluded** | Meetings the loop skips entirely (e.g. mainly family/health, private sessions, the do-not-name list). Only a ledger entry is kept. |

## F. The meeting loop

| Term | Meaning |
|---|---|
| **Meeting loop** | pre-meeting-brief (day before) → meeting → meeting-artifacts (after) → followup-drafter → review → drafts. |
| **Review folder** | One folder per meeting on the Executive Office SharePoint site, named `YYYY-MM-DD_<org-or-topic>_<counterparty>`, holding numbered files: source/transcript, brief, actions, menu of documents, follow-ups (incl. next meeting), drafts, next pre-brief, and a status file. New ones sit in `Meetings/_Inbox/` until approved and moved. |
| **Status file (`status.md`)** | Records tier, what was withheld, unverified count, and who reviewed and when. No names = not approved. |
| **Menu** | The list of documents a meeting needs, chosen from the document types list. |
| **Audiences (EO / SUB / EXT)** | Versions of a draft for the Executive Office, the subsidiary team, and the external counterpart. |
| **Withheld `[withheld: code]`** | A part left out because it touches a no-go topic (family, health, hr, legal, money, tax, political, private, named, secret). Only the code is shown. |
| **Do-not-name list** | Bunmi's private list of people/things never to name. Lives only in Bunmi's own notes. |
| **Internal domain list / Tier C list** | Adeyinka-maintained lists: which email domains count as VGG-internal, and which people/deals count as strategic. |
| **External-facing** | Anything an outside person will read, speaks for Bunmi/VGG outside, or is board/investor/regulator/government/press material. Needs Ayomide's final QA. |
| **Pre-read / one-page brief** | A one-page note before a key meeting: our outcome, the 3–4 things we want, who in VGG is the right expert. |

## G. Reports and other terms

| Term | Meaning |
|---|---|
| **Weekly report (Logan)** | The Monday–Friday Word report on Logan's workstream for Central Ops. See [`../02-workflows/weekly-reports/`](../02-workflows/weekly-reports/README.md). |
| **5-working-day blocker threshold** | The escalation trigger in the Execution Support Mandate: a blocker open 5 working days must be escalated. |
| **Morning brief** | Your own day on one page (Needs attention / Resolved), from the `morning` skill. |
| **Needs attention / Resolved** | The morning brief's two lists: things that cost you to ignore until tomorrow, and things that closed recently. |
| **Central Ops** | The group's central operations team (under the Chief of Staff), which runs the shared operations systems and receives the weekly report. |
| **Executive Office (EO)** | Bunmi's office: the EA team, calendar team and Chief of Staff. |
| **OpenOps / ProjectTrak** | Central Ops' operations and project tracking systems. |
| **Fireflies / Otter / Plaud** | Meeting recording and transcription tools. Fireflies is the main source for Bunmi's meetings. |
| **Vault** | Bunmi's private notes (Obsidian), used by some of Bunmi's skills. |
| **Skill Scout** | An early-October 2026 exercise that listed which tasks each exec wanted Claude skills for. |
| **WAT** | West Africa Time, UTC+1, no daylight saving (Africa/Lagos). All times in this pack are WAT unless stated. When Bunmi travels, other zones change on their own dates (e.g. US/UK clock changes), so the offset to Lagos changes. |
| **TBC / not stated** | In the context file: the sources don't say. Never guessed. |
| **[TO CONFIRM: …]** | In this handover pack: a fact not yet checked. |

## Change history

| Version | Date | Change |
|---|---|---|
| v1.0 | 2026-11-25 | First written |
