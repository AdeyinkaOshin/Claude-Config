---
title: Friday calendar check
version: v1.1
last_updated: 2026-11-26
owner: Adeyinka Oshin
sources: friday-calendar-check skill (synced account skill, version 1.0 of 20 Oct 2026, updatedAt 2026-10-24), bunmi-weekly-context-file skill (updatedAt 2026-11-07), calendar-qa skill (updatedAt 2026-11-25)
---

# Friday calendar check

> Every Friday, Favour (or the EA on duty) writes a draft of Bunmi's schedule: the coming
> week in detail and the next three weeks in outline. Before it goes to Bunmi, the
> `friday-calendar-check` skill checks the draft against the Calendar Brief, the CT-00 to
> CT-04 working bibles and Adeyinka's weekly context file. It writes a short feedback note
> listing what must be fixed. Claude finds problems. It never rewrites the draft, books
> anything or messages anyone. Favour decides what to change.

Read [`../two-week-look-ahead/how-the-calendar-pieces-connect.md`](../two-week-look-ahead/how-the-calendar-pieces-connect.md) first.

## 1. Purpose

Catch mistakes in the weekly draft before Bunmi sees it: double bookings, wrong time zones,
protected time touched, missing to-book items, meetings with no owner, and repeats of last
week's mistakes. "Done" means a feedback note is saved, Favour has fixed the must-fix items
before Saturday, and repeats are turned into rules.

## 2. When it runs

| When (WAT) | What |
|---|---|
| Friday, after the weekly context file (ready by 12:00) and Favour's draft are done | Normal weekly check |
| Any time a new draft is uploaded | On request |

How it starts: typed by hand in Favour's project: `Run the Friday check.` (or
`check this week's draft`). **[TO CONFIRM: usual time on Friday the check is run, and the
deadline for must-fix items on Saturday.]**

## 3. Who does what

| Person / role | Responsibility |
|---|---|
| Favour (or EA on duty) | Writes the weekly draft. Runs the check. Makes the fixes. Posts the one-line note in the group. |
| Adeyinka | Supplies the weekly context file by Friday 12:00. Backs up Favour. **[TO CONFIRM: does Adeyinka review the feedback note before it is posted?]** |
| Bunmi | Receives the corrected draft. Decides on "Decisions for Bunmi". |
| Owners of tier 1–3 meetings | Send pre-reads 24 hours ahead (board packs 48 hours). |
| Claude | Checks and writes the feedback note. Never rewrites the draft, books or messages. |

## 4. Before you start (prerequisites)

- Claude account with access to the **"Favour Calendar Management"** Claude project. See
  [`../../01-setup/01-claude-account-and-cloud-sessions.md`](../../01-setup/01-claude-account-and-cloud-sessions.md).
  **[TO CONFIRM: who owns the project and how a new person is added to it.]**
- The `friday-calendar-check` skill on in your account
  ([`../../01-setup/06-creating-a-skill.md`](../../01-setup/06-creating-a-skill.md)).
- Access to OneDrive › Executive Office › Calendar (Calendar Brief) and its `Feedback`
  subfolder.
- The files to attach (1–4 required, 5 optional):
  1. **The current Calendar Brief** (OneDrive › Executive Office › Calendar)
  2. **The weekly context file** (Adeyinka's, refreshed every Friday). See
     [`../weekly-context-file/`](../weekly-context-file/README.md).
  3. **The draft**: this week in detail, next three weeks in outline
  4. **Last week's feedback note**, so repeats can be caught
  5. *Optional:* **Adeyinka's 2-week look-ahead** (from `calendar-qa` Plan mode). With it, the
     note gets a "Clashes with Adeyinka's look-ahead" section. Without it, the check still runs.
- The CT-00 to CT-04 working bibles. **[TO CONFIRM: are these saved in the project's files,
  or must they be attached too? Where are the masters kept?]**

## 5. Step by step

1. Open **claude.ai** → **Projects** → **Favour Calendar Management** → start a **new chat**.
2. Attach the four files listed in section 4.
3. Type exactly: `Run the Friday check.`
4. If any of the four files is missing, Claude names it and **stops**. It does not guess.
   Attach the missing file and type the phrase again.
5. Claude checks the draft against the rules A1 to H1. Summary:
   [`rules-checklist.md`](rules-checklist.md). The order of authority is:
   Bunmi's direct instruction (newest first) → Calendar Brief → CT-00 to CT-04 → past practice.
6. Claude writes the feedback note in a fixed shape. See [`feedback-note-format.md`](feedback-note-format.md).
7. **Check the note:**
   - Verdict (Ready / Ready after fixes / Not ready) and the count of findings make sense.
   - Each must-fix item names a day and time and a rule ID. Look it up in the draft: is it real?
   - Time zones: the check works out the offset for each date. Spot-check one line yourself.
   - No personal block contents, no private relationship notes.
   - No more than 5 should-fix items; repeats grouped.
8. Save the note as **`Feedback YYYY-MM-DD`** (the Friday date) in OneDrive › Executive
   Office › Calendar › Feedback. **[TO CONFIRM: is the note saved by hand from the chat, as a
   Word doc or as text?]**
9. Fix the draft. Put every clash and exception under the draft's "Decisions needed", with
   options, costs and a recommendation.
10. Claude gives one line to post in the group. Shape:
    > Feedback for week of [date] is in OneDrive › Calendar › Feedback: [n] must-fix,
    > [n] decisions for you, sir.
    **Favour** posts it. **[TO CONFIRM: which WhatsApp group this line goes to.]**
11. For anything marked **REPEAT**, add it as a rule in the named CT document, so it doesn't
    come back. **[TO CONFIRM: who updates the CT bibles and the Calendar Brief.]**
12. If the note has a "Brief needs updating" section, send it to whoever owns the Calendar
    Brief.

## 6. Output — what you get and where it goes

| Output | Where | Who |
|---|---|---|
| Feedback note `Feedback YYYY-MM-DD` | OneDrive › Executive Office › Calendar › Feedback | Saved by Favour |
| One-line group post | The calendar WhatsApp group **[TO CONFIRM]** | Posted by Favour |
| Corrected draft | To Bunmi as the Sunday final **[TO CONFIRM: how and when the draft reaches Bunmi]** | Favour |
| REPEAT items | Added to CT-00 to CT-04 | **[TO CONFIRM: owner]** |

## 7. Review and approval rules

- Claude **does not** rewrite the draft, book anything or message anyone.
- Must-fix = double booking, wrong time zone, protected time touched, a clash shown as
  accepted, a missing to-book item, or a tier 1–3 meeting with no owner. Everything else is
  should-fix.
- If the Calendar Brief conflicts with a newer Bunmi instruction, the draft is **not** marked
  wrong for following the brief. The conflict goes under "Brief needs updating".
- Never flag personal block contents. Show them only as "held".
- Don't quote private relationship notes from the context file. Refer to a deal by name only.
- Meetings Bunmi scheduled personally: check for clashes only, don't question their tier.
- Items fixed at a time by the brief's to-book list skip the tier check but are still checked
  for clashes, spacing and time zones.
- Only three regular touchpoints with Bunmi: morning plan with 30-minute reminders, the
  Sunday final, and decisions. The draft must not add other recurring messages.

## 8. Common problems and fixes

| Symptom | Fix |
|---|---|
| Claude stops and says a file is missing | Attach it. The check never guesses. |
| Context file not ready | Ask Adeyinka. It should be ready by Friday 12:00 (Saturday fallback). |
| Time zone findings look wrong | The skill has a dated table of offsets for the travel period. After the trip ends or clocks change, the table must be updated in the skill. **[TO CONFIRM: who updates it once the current trip ends (early December)]** |
| Length findings clash with what Bunmi said on 24 Nov | Known conflict: see section 9. Treat Bunmi's newer instruction as the authority and log "Brief needs updating". |
| Same issue every week | It's a REPEAT. Turn it into a rule in the CT document. |
| Note is too long | Ask Claude to keep 5 should-fix items max and group repeats ("Lagos time missing on 14 lines"). |

## 9. Gaps to confirm

1. **[TO CONFIRM]** Usual time on Friday the check runs; deadline for must-fix fixes on Saturday.
2. **[TO CONFIRM]** Does Adeyinka review the note before it is posted?
3. **[TO CONFIRM]** Who owns the "Favour Calendar Management" project and how a new person is added.
4. **[TO CONFIRM]** Are CT-00 to CT-04 in the project's files or attached each time? Where are the masters?
5. **[TO CONFIRM]** How the feedback note is saved (by hand? Word or text?).
6. **[TO CONFIRM]** Which WhatsApp group the one-line post goes to.
7. **[TO CONFIRM]** How and when the corrected draft (Sunday final) reaches Bunmi.
8. **[TO CONFIRM]** Who updates the CT bibles and the Calendar Brief.
9. **[TO CONFIRM]** Who updates the skill's time-zone table after the current travel period ends.
10. ~~Meeting lengths~~ — decided 26 Nov: skill v1.1 uses the 24 Nov standard (15/30/45). **[TO CONFIRM: who updates the Calendar Brief and CT-02 to match?]**
11. ~~Which plan wins~~ — decided 26 Nov: neither silently; clashes are listed and settled by Favour and Adeyinka. **[TO CONFIRM: does Favour have the v1.1 skill in the Favour Calendar Management project, or does it need uploading to Favour's account too?]**

## Change history

| Version | Date | Change |
|---|---|---|
| v1.0 | 2026-11-25 | First written |
| v1.1 | 2026-11-26 | Skill v1.1: 24 Nov meeting lengths; optional look-ahead input and clash section |
