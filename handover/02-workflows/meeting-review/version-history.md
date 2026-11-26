# Version history — meeting-artifacts skill

Part of the [meeting review workflow](README.md).

Sources: `git -C Logan-VGG log -- skills-bunmi/meeting-artifacts`, the "What changed" sections of
`Logan-VGG/skills-bunmi/meeting-artifacts/README.md` and `ROUTINE.md`, and `learning-log.md`.

**Note on the git record.** The local clone of `Logan-VGG` is shallow. The earliest commit it
shows for this folder is a bulk mirror commit on 16 Oct 2026, so the dates for v1.0 and v1.1
come from the skill's own file headers, not from git.

## Installed copy vs repo copy — they differ

| Copy | Version | Date |
|---|---|---|
| Repo: `Logan-VGG/skills-bunmi/meeting-artifacts/` and `meeting-artifacts.zip` | **v1.4** | 20 Nov 2026 |
| Installed in claude.ai (synced skill) | **v1.1** | 12 Oct 2026 |
| Cloud routine in Bunmi's account | Reads the repo on every run, so **v1.4** (routine prompt itself is labelled v1.3) | — |

The claude.ai copy is three versions behind. A manual run in claude.ai today follows v1.1 rules:
it skips whole meetings that are "mainly about" a sensitive topic, points at Bunmi's OneDrive,
and writes no `00_transcript.md`. Re-upload `meeting-artifacts.zip` from the repo to bring it to
v1.4. **Decided 26 Nov 2026:** replace the account copy with v1.4 — Adeyinka uploads
`skills-bunmi/meeting-artifacts.zip` (v1.4) to their claude.ai account (Settings → Capabilities →
Skills). **[TO CONFIRM: upload done? Then this line can say "account copy = v1.4".]**

## Versions

| Version | Date | Git commit(s) | What changed |
|---|---|---|---|
| v1.0 | 6 Oct 2026 | not in local history | First install pack of Bunmi's skills. Built from the 2 Oct build plan for the meeting loop (pre-meeting brief, meeting artifacts, follow-up drafter). Tiers, ledger, Fireflies/Plaud matching, drafts only. Planned to run on Bunmi's machine every 3 hours, writing to Bunmi's OneDrive. |
| v1.1 | 12 Oct 2026 | not in local history | All 16 of Ayomide's document types added, plus three more (19 total). A document **menu** after every meeting. **Audience versions** (EO / SUB / EXT) with the room rule. **Manual mode**, so it works in the Claude app with nothing connected. First-draft pre-brief for Bunmi's next slot, in the planning-pack format. Rules for garbled names and wrong speaker labels. After the first test run (12 Oct, one real internal meeting), five fixes: what Tier A drafts, where names can be matched from, folder names for internal meetings, actions that rest on a withheld reason, and pre-briefs for meetings Bunmi is not in. |
| v1.2 | 9 Nov 2026 (merged 13 Nov, PR #5) | `89e9281` | **Withhold lines, not meetings.** The old "mainly about" test had skipped 96 meetings by 9 Nov, mostly deal and investor meetings that only mentioned amounts or a named party. Now `money`, `hr`, `legal`, `tax`, `political` and `secret` are line-level only and the folder is always written. A whole meeting is skipped only if it is mainly family/health, Bunmi's own private session, the main other party is on the do-not-name list, or Bunmi said to hold it. New ledger status `rescreen` to re-process old exclusions. The shared rules file `_shared/external-qa.md` was updated to match. |
| v1.3 | 13 Nov 2026 (merged 13 Nov, PRs #5 and #6) | `de6cf71`, `c923287` | **Runs as a cloud routine in Bunmi's Claude account**, hourly 08:00–20:00 WAT, live from day one (new `ROUTINE.md` with setup steps and the exact prompt). Do-not-name list moved from the vault to `_Claude/` in Bunmi's own OneDrive, so cloud runs can draft external versions. Tier C vault notes are left in the folder for Bunmi; the cloud never writes to the vault. Plaud optional (connector, or exports in `Meetings/_plaud/`). If Fireflies or Microsoft 365 drops, an Outlook draft alert to the EA. Second commit the same day corrected storage to the **BunmiExecutiveOffice SharePoint site** (folders had lived there since October; the first v1.3 commit wrongly pointed at OneDrive). Zip rebuilt (it had still been v1.1). |
| v1.4 | 20 Nov 2026 | `85a4030` (merge `7181abc`) | Every folder keeps the **full transcript** in `00_transcript.md` (withheld lines still withheld; the tool's summary left out; internal only). Backfill of older folders: up to 10 per run, last 30 days. When the calendar has meetings but no recordings arrive, the run note says so and points to `Meetings/_plaud/`. Routine picks it up on its next run; nothing to reinstall. |

## Learning-log record

`Logan-VGG/skills-bunmi/meeting-artifacts/learning-log.md` (identical in the repo and the
claude.ai copy):

- **Standing preferences (approved):** none yet.
- **Entries:** one — 12 Oct 2026, Tier A, the first test run (by Logan's Claude). Types on the
  menu: 7, 7, 19. Types drafted: 7, 7. Use by Bunmi not yet reviewed.
- No reviewer edits have been logged yet. **[TO CONFIRM: have edits been made in review that were never logged? If so, log them so the skill can learn.]**

## Not yet tested (as of v1.4)

From the skill README: a Tier C meeting, an external (EXT) version, and the `concept-docs`
hand-off. The README also lists a scheduled cloud run as untested, though the README was last
updated after the routine was set up. **[TO CONFIRM: has the cloud routine completed real runs, and have any Tier C or EXT folders gone through review?]**

## Change history
| Version | Date | Change |
|---|---|---|
| v1.1 | 2026-11-26 | Account copy to be replaced with v1.4 |
