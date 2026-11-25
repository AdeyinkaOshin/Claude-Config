# How the calendar pieces connect

Bunmi's calendar work is four linked workflows. Each one feeds the next. Read this
first, then the README in each folder.

| Workflow | Folder | Skill | Who runs it |
|---|---|---|---|
| Weekly context file | [`../weekly-context-file/`](../weekly-context-file/README.md) | `bunmi-weekly-context-file` | Adeyinka |
| 2-week look-ahead (Plan mode) | [`./`](README.md) | `calendar-qa` (Plan mode) | Adeyinka |
| Friday calendar check | [`../friday-calendar-check/`](../friday-calendar-check/README.md) | `friday-calendar-check` | Favour (or the EA on duty) |
| Daily calendar QA | [`../daily-calendar-qa/`](../daily-calendar-qa/README.md) | `calendar-qa` (Daily, Thursday, Sunday, Friday modes) | Adeyinka |

## Two planning tracks feed one calendar

There are two people planning, with two different "context" files. Do not mix them up.

1. **Favour's track (the weekly draft for Bunmi).**
   Adeyinka builds the **weekly context file** (deals, owners, tiers 1–3, where Bunmi is,
   what to book). Favour loads it into the "Favour Calendar Management" Claude project and
   uses it, with the Calendar Brief, to write the **weekly draft** of Bunmi's schedule.
   The **Friday calendar check** then reviews that draft and writes a feedback note.
2. **Udeme's track (the booking work).**
   Adeyinka runs `calendar-qa` in **Plan mode**. It writes the **2-week look-ahead** and a
   separate **context for the calendar team** file. Udeme and the calendar team send the
   emails and book the meetings from it. **Daily calendar QA** then checks every day that the
   booking was done, and done right.

**[TO CONFIRM: how Favour's weekly draft and Adeyinka's 2-week look-ahead are reconciled.
Which one is the master plan if they disagree?]**

## The weekly rhythm (WAT)

```
Mon–Wed   Daily QA (morning + evening) ............ Adeyinka → fix list to Udeme
Thu       Plan mode: 2-week look-ahead + themes ... Adeyinka → context for calendar team → Udeme books
Fri       Weekly context file, ready by 12:00 ..... Adeyinka → Favour (loads into Favour's project)
Fri       Favour writes the weekly draft
Fri       Friday calendar check on the draft ...... Favour → feedback note (must-fix before Saturday)
Fri       Plan refresh (what changed) + week score  Adeyinka → note to Udeme
Sat       Context file fallback day if Friday was missed; must-fix items fixed
Sat–Sun   Sunday check on the next 2 weeks ........ Adeyinka → fix list for Udeme by Monday morning
Sun       Sunday final to Bunmi [TO CONFIRM: who sends it and at what time]
```

## How the data flows

```
Sources: Bunmi's Outlook calendar · EA team mailbox · meeting review folders (SharePoint)
         · WhatsApp calendar groups · Station flights ("Bunmi calendar" workstream)
           │
           ├──► Weekly context file ──► Favour's project ──► weekly draft ──► Friday check
           │                                                                 │
           │                                                      feedback note → Favour fixes
           │
           └──► Plan mode ──► 2-week look-ahead + context for calendar team ──► Udeme books
                                                                                  │
                         Daily QA / Sunday check / Friday score  ◄────────────────┘
                         (checks the real calendar; fix list → Udeme; log → ops/log/)
```

Plan mode reads the latest weekly context file too, if it is available. So the context file
is the shared base for both tracks.

## One rule across all four

Claude reads, checks and drafts. **Claude never books, moves, accepts, declines or sends.**
A person (Adeyinka, Favour or Udeme) does every send and every booking.
