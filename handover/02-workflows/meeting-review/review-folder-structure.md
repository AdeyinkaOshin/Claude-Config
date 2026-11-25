# Review folder structure

Part of the [meeting review workflow](README.md). Describes skill version **v1.4** (20 Nov 2026).
Source of truth: `Logan-VGG/skills-bunmi/meeting-artifacts/SKILL.md`, sections 2, 8, 9 and 10.

## Where it lives

All work in progress lives on the **BunmiExecutiveOffice** SharePoint site, under
**Shared Documents > `Meetings`**. The EA and Ayomide need edit access.

```
Meetings/
  _Inbox/                       new review folders, one per meeting, waiting for review
  Areas/<Area>/Meetings/        approved folders (moving a folder here = approval)
  _Backtest/                    output of a dry run (MODE: backtest). No Outlook drafts.
  _plaud/                       Plaud transcript exports saved by Bunmi or the EA, for in-person meetings
  _config/
    tier-c.md                   Tier C names (strategic people/deals). Kept by the EA. Names only, no amounts.
  _ledger.json                  one entry per calendar event and per recording. Stops double processing.
  _ledger.lock                  exists only while a run is in progress (a run stops if it is under 2 hours old)
  _runlog.md                    one block per run, even when there was nothing to do
```

**Private, not on the site.** `_Claude/` sits at the top of **Bunmi's own OneDrive** and is
shared with no one. It holds `do-not-name.md` (written by Bunmi) and, optionally, `People/`
notes. The skill reads it but never writes to it, copies it or names it in a file. Nobody
else holds a copy.

**Bunmi's Obsidian vault** is the long-term source of truth. Only approved content reaches it,
and only Bunmi applies it (from `05_vault_updates.md`). The cloud routine never touches the vault.

History note: up to v1.2 the skill was configured to write to Bunmi's OneDrive. v1.3 (13 Nov)
corrected this to the SharePoint site, where the meeting folders had lived since October.

## Folder name

```
YYYY-MM-DD_<Org-or-topic>_<Counterparty-surname>
```

- Date is the meeting date (Lagos time).
- External meeting: the other organisation, then the main counterpart's surname.
- Internal meeting: the topic, then the surname of the main other person.
- A withheld or do-not-name item never appears in a folder or file name.

## What is inside one folder

| File | What it is | Written when |
|---|---|---|
| `00_source.md` | Meeting title, date and time (Lagos and as recorded), who was in the room and when each joined/left, recording IDs, context files read, inputs not available, name corrections made. No transcript text. | Always |
| `00_transcript.md` | Full transcript copy for the record: speaker labels and timestamps, untidied. Withheld lines replaced with `[withheld: <code>]`. The tool's own summary left out. Names not corrected here. **Internal record only**: never pasted into a SUB/EXT file or attached to an email. | Always (from v1.4; older folders are backfilled, up to 10 per run, last 30 days) |
| `01_brief.md` | Context note, Executive Office version. Under 250 words: what this was, what was decided, what Bunmi promised (with timestamps), what they promised, open questions, not verified. | Always |
| `01_brief.SUB-<entity>.md` | Context note cut for a subsidiary team. | Only when the menu calls for it |
| `02_actions.md` | Table: Owner / Action / Due / Source (timestamp). Only real commitments. For Tier A meetings that already have an ops Meeting Report, it links that instead. | Always |
| `03_menu.md` | Table of documents this meeting needs: type, why (timestamp), reader, audiences, due, earlier version, drafted this run. Then "Promised out loud by Bunmi" and "Held" (what was not drafted and why). May say "No document needed". | Always, every tier |
| `03_followups/` | `email-<person>.md`, `whatsapp-<person>.md`, `next-meeting.md` (date, owner, agenda). Written by `followup-drafter`. | Tier B and C |
| `04_artifacts/<doc>/` | One subfolder per drafted document (see below). | When the tier allows |
| `05_vault_updates.md` | Proposed changes to People/ and deal notes in Bunmi's vault, for Bunmi to apply. | Tier C |
| `06_next-prebrief.md` | One-page first-draft pre-brief for Bunmi's next slot with the same people. | Only if Bunmi will be in the next meeting |
| `status.md` | Review state (see below). | Always |

### Inside `04_artifacts/<doc>/`

```
brief.md                                   what the document must do
critique.md                                the critique pass
status.md                                  status for this document
<Doc name> ©️2026.<variant>.v<n>.content.md   the draft text
<Doc name> ©️2026.<variant>.v<n>.docx|.pptx   the read copy (when concept-docs is used)
```

- `<variant>` is the audience: `EO`, `SUB-<entity>`, `EXT-<reader>`.
- `<n>` goes up on every real change. Each rebuild says what it built on.
- A new audience is a new variant, not a new version number.

## The three audience versions

One brief, up to three versions. Claude writes the Executive Office version first (it holds
everything) and then cuts down. It never writes the external version first and adds to it.

| Audience | Code | Who reads it | Holds | Leaves out |
|---|---|---|---|---|
| Executive Office | `EO` | Bunmi, Adeyinka, Ayomide, Dorathy, Uche | Full context: what was said, pushback, our position, our one ask, give and get, risks, the decision Bunmi must make | Only the must-not-handle items |
| Subsidiary team | `SUB-<entity>` | The entity lead and the people doing the work | What was agreed, what the team must do, by when, who owns it, what Bunmi promised on their behalf, next meeting | Bunmi's private read of people, other entities' deals, board/investor matters, anything withheld |
| External counterpart | `EXT-<reader>` | The named person on the other side | What we agreed, what we will send, what we need from them, next step with a date | Our internal position and fallback, internal owners' names (unless the contact), anything unverified |

Rules for every version:

- The top of each file states who it is for and who must not get it.
- **Room rule.** A SUB or EXT file only holds what was said while that reader's people were on
  the call. The EO file holds the whole meeting.
- More than one subsidiary in the meeting: one SUB file each. One entity's deal facts never go
  into another entity's file.
- Every EXT file is external-facing, so it always goes to Ayomide.
- No EXT file is written unless the do-not-name list was read. Otherwise the menu shows it as
  "held: do-not-name not checked".

## `status.md` fields

| Field | Meaning |
|---|---|
| `status` | `Draft` → `Reviewed` → `Approved` (or `Rejected`, with one line why) |
| `tier` / `tier_reason` | A, B or C, and why (one line) |
| `role` | Bunmi's role-day tag from the calendar event (CEO, COO, CFO, Governance, CBDO, Pipeline), or `not set` |
| `audiences` | e.g. `EO, SUB-<entity>, EXT-<reader>` |
| `external_facing` | `yes` or `no` — decides whether Ayomide must review |
| `area` | Proposed `Areas/` folder to move it to when approved |
| `withheld` | Count and codes only, e.g. `1 (money)` |
| `unverified` | Count of open `[[TBC]]` / `[unverified]` flags |
| `first_pass` | `Adeyinka Oshin, pending` → `Adeyinka Oshin, <date>` |
| `final_qa` | `Ayomide Adeosun, pending` → `Ayomide Adeosun, <date>`, or `not needed` when internal |

## Ledger statuses (`_ledger.json`)

`waiting_transcript`, `needs_split`, `unmatched`, `excluded:<code>`, `rescreen`, `in_review`,
`approved`, `drafts_created`, `rejected`. Excluded entries hold only the event ID, date and
code — no title. Setting an entry to `rescreen` makes the next run process it again under the
current rules (never for an entry "held on Bunmi's instruction").
