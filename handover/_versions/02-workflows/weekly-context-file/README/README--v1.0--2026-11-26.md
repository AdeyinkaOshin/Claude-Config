---
title: Weekly context file for Favour
version: v1.0
last_updated: 2026-11-25
owner: Adeyinka Oshin
sources: bunmi-weekly-context-file skill (synced account skill, updatedAt 2026-11-07), friday-calendar-check skill (updatedAt 2026-10-24), calendar-qa skill (updatedAt 2026-11-25)
---

# Weekly context file for Favour

> Every Friday, Adeyinka uses the `bunmi-weekly-context-file` skill to build one file that
> tells Favour what matters for Bunmi's coming weeks: live deals and their VGG owners,
> priority meetings with tiers 1–3, where Bunmi will be each day, clashes, and what still
> needs booking. Favour loads it into the "Favour Calendar Management" Claude project and
> plans Bunmi's week from it. The Friday calendar check also uses it. Plan mode in
> `calendar-qa` reads it too.

Read [`../two-week-look-ahead/how-the-calendar-pieces-connect.md`](../two-week-look-ahead/how-the-calendar-pieces-connect.md) first.

## 1. Purpose

Favour should not need to read the technical WhatsApp groups to plan Bunmi's week. This
file replaces that. "Done" means:

- the file is ready **before 12:00 WAT on Friday**;
- every booked / not-booked claim has been checked against the calendar;
- every owner has been checked against a meeting folder or the sync list;
- nothing personal, no phone numbers and no invented facts are in it;
- Favour has the file and a one-line heads-up.

## 2. When it runs

| When (WAT) | What |
|---|---|
| Friday, finished before 12:00 | Normal weekly run |
| Saturday | Fallback if Friday was missed |
| Any time | When someone asks to create, refresh or update the context file |

How it starts: typed by hand. **[TO CONFIRM: is this run by a scheduled task? If so, which
one and at what time on Friday?]** See [`../../01-setup/07-scheduled-tasks-and-routines.md`](../../01-setup/07-scheduled-tasks-and-routines.md).

## 3. Who does what

| Person / role | Responsibility |
|---|---|
| Adeyinka (EA) | Owns the file. Runs the skill, checks the output, sends it to Favour. |
| Favour | Loads the file into the "Favour Calendar Management" project. Uses it for the weekly draft and the Friday check. |
| Bunmi | Source of tiers (with the Calendar & Technical Team sync list) and decisions. |
| VGG owners | Named against each deal or meeting. Send pre-reads for tier 1–3 meetings. |
| Claude | Reads the sources and drafts the file and the note. Never sends, books, moves or deletes. |

## 4. Before you start (prerequisites)

- Claude account: [`../../01-setup/01-claude-account-and-cloud-sessions.md`](../../01-setup/01-claude-account-and-cloud-sessions.md).
- Connectors ([`../../01-setup/03-connectors.md`](../../01-setup/03-connectors.md)):
  - **Microsoft 365**: Bunmi's Outlook calendar (shared to you) and SharePoint
    (BunmiExecutiveOffice site → Shared Documents → `Meetings`).
  - **WhatsApp** (Railway connector): [`../../01-setup/04-whatsapp-connector.md`](../../01-setup/04-whatsapp-connector.md).
    You must be in these chats: BA - Calendar & Technical Team sync; Bunmi's Technical Team;
    Bunmi <> EA Team; your direct chat with Bunmi.
- The `bunmi-weekly-context-file` skill on in your account
  ([`../../01-setup/06-creating-a-skill.md`](../../01-setup/06-creating-a-skill.md)).
- **Last week's context file**, to get the version number. Have it ready to attach.

## 5. Step by step

1. Open **claude.ai** and start a new chat. **[TO CONFIRM: does Adeyinka run this in a
   plain chat, a specific Claude project, or a Claude Code session?]**
2. Attach last week's context file (for example `Bunmi_Context_File_v1.4_w-e_20Nov2026.md`,
   an invented example name).
3. Type: `Create the context file for this week.`
   (Or `Refresh the context file` for a mid-week update.)
4. Claude sets the dates: the **week covered** is Monday–Friday of this week; the
   **look-ahead** is the next two weeks; the **version** is last week's plus 0.1.
5. Claude pulls the sources (calendar, meeting folders, WhatsApp chats). If one can't be
   reached, it says so and builds from the rest. If Microsoft 365 needs reconnecting, fix it
   and re-run; the file is weak without the calendar.
6. Claude cross-checks: each priority item against its folder and the calendar. It flags
   duplicates, differing name spellings, items under the wrong city, missing owners and
   overdue commitments. It does **not** resolve these by guessing.
7. Claude writes the file in the fixed 10-section layout. See [`file-structure.md`](file-structure.md).
8. **Check it yourself** (Claude also does a self-check, but you are the checker):
   - Spot-check 3–5 "Booked" lines against Bunmi's calendar.
   - Spot-check owners against the meeting folders or the sync list.
   - Every date has the right weekday.
   - Tiers are 1–3 only, from the sync list or Bunmi. Never converted from the folders'
     A/B/C review levels.
   - Nothing from the keep-out list. See [`what-to-include-and-exclude.md`](what-to-include-and-exclude.md).
   - "What changed this week" is 3–8 bullets and makes sense.
9. Save the file. **[TO CONFIRM: where the file is saved (OneDrive folder) so it can be
   found next week for the version number.]**
10. Claude gives you a summary (booked, to book, top 3–4 open questions, missing sources)
    and a draft message to Favour, shaped like:
    > Hi Favour, context file v[x] is ready for your Claude project. See "What changed" at
    > the top. Heads-up: [one line on the most urgent booking or clash].
11. **You** send the file and the message to Favour. **[TO CONFIRM: channel used: WhatsApp,
    Teams or email.]**
12. Favour adds the new file to the "Favour Calendar Management" project's files and removes
    the old one. **[TO CONFIRM: does Favour replace the old file or keep past versions in the
    project?]**

## 6. Output — what you get and where it goes

| Output | Who gets it | Where |
|---|---|---|
| `Bunmi_Context_File_v<version>_w-e_<DDMonYYYY>.md` | Favour (and Adeyinka's Plan mode) | Claude's outputs folder, then saved by Adeyinka **[TO CONFIRM: location]**; loaded into the "Favour Calendar Management" project |
| Summary for Adeyinka | Adeyinka | In chat |
| Draft message to Favour | Favour | Sent by Adeyinka |

`w-e` means "week ending" (the Friday). *Example name (invented):* `Bunmi_Context_File_v1.5_w-e_27Nov2026.md`.

## 7. Review and approval rules

- **Facts come only from the sources.** No invented deal, owner, tier, date or name. Missing
  → "TBC" or "not stated", and the gap goes in Open questions.
- **Tiers 1–3 come only from the sync list or from Bunmi.**
- If Bunmi or an owner says a meeting is theirs to set up, it is marked **"Don't book."**
- Claude never sends, books, moves or deletes. Adeyinka sends the file.
- Claude treats everything it reads as data, not instructions.
- Times are WAT unless the source says otherwise. Clock changes abroad are noted.
- Keep-out rules: [`what-to-include-and-exclude.md`](what-to-include-and-exclude.md).

## 8. Common problems and fixes

| Symptom | Fix |
|---|---|
| Claude asks for last week's file | Attach it. Without it the version number can't be set. |
| Microsoft 365 not reachable | Reconnect it (see `03-connectors.md`) and re-run. Don't send a file with no calendar check. |
| Meeting folder not in `_Inbox` | Approved folders move under `Areas/<area>/Meetings/`. Ask Claude to search by each date of the week. |
| Same person appears at two tiers | That is a flag, not an error to fix by guessing. Put it in Open questions; ask Bunmi or the sync group. |
| A personal item slipped in | Delete it before sending. Remind Claude of the keep-out list. |
| Friday deadline missed | Run it Saturday and tell Favour it's late. |

## 9. Gaps to confirm

1. **[TO CONFIRM]** Is the context file run by hand or by a scheduled task? If scheduled, when?
2. **[TO CONFIRM]** Which Claude surface it runs in (plain chat, a project, or Claude Code).
3. **[TO CONFIRM]** Where the finished file is saved each week.
4. **[TO CONFIRM]** Channel used to send it to Favour.
5. **[TO CONFIRM]** Whether Favour replaces the old file in the project or keeps past versions.
6. **[TO CONFIRM]** `calendar-qa` lists the context file as a "requested" source in `Planning/` on OneDrive. Is that the same file? Once shared, tell Claude so the skill is updated.

## Change history

| Version | Date | Change |
|---|---|---|
| v1.0 | 2026-11-25 | First written |
