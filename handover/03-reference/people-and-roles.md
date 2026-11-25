---
title: People and roles
version: v1.0
last_updated: 2026-11-25
owner: Adeyinka Oshin
sources: Logan-VGG repo README.md, judgment/people.yaml, judgment/README.md, work/README.md, work/policies/ (summarised); skill files calendar-qa, bunmi-weekly-context-file, friday-calendar-check, meeting-artifacts, vgg-logan-weekly-report, ops-runway, skills-bunmi/README.md, skills-margaret/README.md
---

# People and roles

> Who is who around the Executive Assistant role, and who checks, approves and sends
> what. Role-level only: no contact details. Find contact details in Outlook / Teams.

## 1. The people

| Person | Role | What they do in these workflows |
|---|---|---|
| **Bunmi Akinyemiju** | Group CEO (GCEO) of VGG | The principal. Posts requests in the WhatsApp calendar group, the Technical Team chat and EA threads. Gives final approval on anything that leaves in Bunmi's name. Is asked for judgment on strategic direction and anything that speaks for the company. Keeps a private do-not-name list (never copied anywhere). Sets the calendar standard (24 Nov 2026 walkthrough) that the calendar checks are built on. |
| **Adeyinka Oshin** (the role being handed over) | Executive Assistant to the GCEO; works the Ops runway | First-pass reviewer of everything Claude drafts for Bunmi. Quality assurance and backup for Bunmi's calendar (checks the calendar team's work, steps in when they are stretched). Builds the weekly context file and 2-week look-ahead. Works Station flights routed to Ops. Prepares the weekly report on Logan's workstream. Maintains the internal-domain list and the "Tier C" (strategic) list used by the meeting loop. The "context person": asked when a meeting has no recording. Judges "is this plan doable by the team this week". |
| **Udeme and the calendar team** | Scheduling team for Bunmi's calendar | Send the scheduling emails, book and move meetings. Receive Adeyinka's context file and fix lists. |
| **Favour** | Builds the weekly draft of Bunmi's schedule | Loads Adeyinka's context file into a Claude project ("Favour Calendar Management"), drafts the week, runs the Friday check, and decides what to change. |
| **Ayomide Adeosun** | Group Oil & Gas + Tech lead | Final QA on anything external-facing (tone, accuracy, "doesn't read like AI", format, signature block). Supplied the list of meeting document types and the reference documents for concept docs. Judges oil & gas go-to-market and Tech builds. |
| **Dorathy** | Sends on Bunmi's behalf | May send approved drafts as Bunmi, alongside Bunmi and the EA on duty. **[TO CONFIRM: Dorathy's exact role title.]** |
| **Logan Herzog** | AI implementation lead; "Traffic Controller" (the tower) | Runs the Station and the hourly tower sweep. Decides which flights go to which runway. Files judgment questions and work requests. Owns the Logan-VGG repo and the external-QA policy. Subject of the weekly report. Does not touch anyone else's credentials. |
| **Uche Ukonu** | Chief of Staff to the GCEO; Central Ops | Owns the group's operations systems (OpenOps, ProjectTrak) and the rules for what gets built. Checks the OKR routing key. Judges whether a build fits existing systems and data-handling rules. |
| **Omotola** | Central Ops | Receives the weekly report on Logan's workstream. **[TO CONFIRM: Omotola's role title.]** |
| **Banke Ajayi** | Central Ops, Regulated Ops lead | Has a separate fortnightly report direct to the GCEO (not produced by the weekly report skill). Co-leads org-wide AI trainings. |
| **Margaret Oduwole** | Executive at VigiPay (a VGG company) | User of two skills built for Margaret (executive documents; HR learning & development loop). **[TO CONFIRM: Margaret's role title, and whether the new person supports Margaret's skills.]** |
| **New executives** | Recently joined senior leaders | Bunmi wants to see them roughly every other day, in person where possible. Booked as "new execs and internal" on theme days. |
| **Subsidiary / entity leads** | Heads of VGG companies | Own deals and relationships ("VGG owner" in the context file); supply OKR files; send one-page pre-reads for their tier 1–3 meetings. |

## 2. Who reviews, approves and sends what

The general rule: **Claude drafts, people send.** Where two rules differ, the stricter wins.

| What | Drafted by | First check | Final check / approval | Who sends or books |
|---|---|---|---|---|
| Internal drafts for Bunmi (action lists, internal briefs, logistics notes) | Claude (meeting loop, other Bunmi skills) | Adeyinka | Adeyinka | Bunmi, Dorathy or the EA on duty |
| External-facing drafts (anyone outside VGG reads it, speaks for Bunmi/VGG, board/investor/regulator/government/press material) | Claude | Adeyinka | **Ayomide** (Adeyinka chases after 24h but never approves in Ayomide's place) | Bunmi, or Dorathy as Bunmi. External messages are always sent by a person. |
| Meeting review folders | `meeting-artifacts` (hourly in Bunmi's account) | Adeyinka | Ayomide for external drafts; approval recorded in the folder's status file, then the folder is moved out of `_Inbox` | — |
| 2-week look-ahead and team context file | `calendar-qa` Plan mode | Adeyinka | Adeyinka shares with Udeme | Calendar team books |
| Daily calendar fix list | `calendar-qa` | Adeyinka | — | Adeyinka passes to Udeme; calendar team fixes |
| Weekly context file | `bunmi-weekly-context-file` | Adeyinka (owner) | — | Adeyinka sends to Favour |
| Weekly schedule draft | Favour | `friday-calendar-check` finds problems | Favour decides changes; Bunmi's direct instruction always wins | Favour |
| Weekly report on Logan's workstream | `vgg-logan-weekly-report` | Adeyinka | **[TO CONFIRM: does Logan approve before submission?]** | Adeyinka submits to Central Ops |
| Judgment questions | Logan (tower) | — | The named reviewer gives a verdict | Nothing leaves the repo |
| Work requests run by someone's Claude | Logan files | — | The assignee says yes to the exact message | Unattended runs never send; Bunmi's Claude may never send |
| Ops runway messages | `ops-runway` drafts | Adeyinka | Adeyinka | Adeyinka sends personally |
| Emails from Logan's own instance | Claude | Logan picks the mailbox every time | Logan | Logan |
| OKR routing key | `okr-alignment` | Uche | Bunmi | — |

## 3. What Bunmi's Claude may do (policy summary)

Bunmi's policy file in the Logan-VGG repo (`work/policies/`) allows reading Outlook, the
calendar, Teams and Fireflies; drafting; private holds on Bunmi's own calendar; and booking
internal meetings only inside set limits (working hours in Lagos time, short length,
internal attendees only, no overlaps, never moving or cancelling). **Sending is never
allowed.** Anyone without a policy file gets read + draft only.

The external-QA policy (same folder) adds a list of topics Claude must not handle at all
(for example family, health, HR, legal instruments, money amounts, tax, politics, private
reflections, the do-not-name list, secrets). These are left out and marked "withheld" with
a code only.

## Gaps to confirm

- **[TO CONFIRM: Dorathy's exact role title.]**
- **[TO CONFIRM: Omotola's role title.]**
- **[TO CONFIRM: Margaret's role title, and whether the new person supports Margaret's skills.]**
- **[TO CONFIRM: does Logan approve the weekly report before submission?]**
- **[TO CONFIRM: who covers Adeyinka's first-pass review and calendar QA during the handover period.]**

## Change history

| Version | Date | Change |
|---|---|---|
| v1.0 | 2026-11-25 | First written |
