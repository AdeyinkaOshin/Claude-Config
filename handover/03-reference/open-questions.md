# Open questions — [TO CONFIRM] items

Generated 2026-11-26 by `tools/list_open_questions.py`. Answer these, edit the doc, then re-run the script.


**149 open questions.**


## [01-setup/01-claude-account-and-cloud-sessions.md](../01-setup/01-claude-account-and-cloud-sessions.md)

- [ ] who is the org admin today, and which plan (Team / Enterprise)?
- [ ] list of other projects in use
- [ ] access is granted by whom?

## [01-setup/02-github-setup.md](../01-setup/02-github-setup.md)

- [ ] after handover, should the repo be transferred to a VGG organisation account instead?
- [ ] create a `main` and merge both, so a newcomer has one obvious branch?

## [01-setup/03-connectors.md](../01-setup/03-connectors.md)

- [ ] which workflows use Notion?
- [ ] needed at all?
- [ ] exact menu name on the VGG plan; some plans call it "Integrations"

## [01-setup/04-whatsapp-connector.md](../01-setup/04-whatsapp-connector.md)

- [ ] whose Railway account / billing? Handover must transfer it.

## [01-setup/06-creating-a-skill.md](../01-setup/06-creating-a-skill.md)

- [ ] exact menu path on the VGG plan
- [ ] does the VGG org admin publish skills to everyone, or does each person upload?

## [01-setup/07-scheduled-tasks-and-routines.md](../01-setup/07-scheduled-tasks-and-routines.md)

- [ ] are any of these scheduled, or all run by hand?

## [02-workflows/daily-calendar-qa/README.md](../02-workflows/daily-calendar-qa/README.md)

- [ ] are any of these runs started by a scheduled task? The 25 Nov log shows a morning daily run at 11:55 WAT; it is not clear if that was by hand. Agree fixed times for the morning and evening runs.
- [ ] confirm this is where Adeyinka runs it, rather than a plain claude.ai chat.
- [ ] channel to Udeme: WhatsApp, Teams or email
- [ ] does Adeyinka send these to Bunmi, and on which chat?

## [02-workflows/daily-calendar-qa/bunmi-calendar-standard.md](../02-workflows/daily-calendar-qa/bunmi-calendar-standard.md)

- [ ] who updates the Calendar Brief and CT-02 to the new lengths?

## [02-workflows/daily-calendar-qa/day-themes.md](../02-workflows/daily-calendar-qa/day-themes.md)

- [ ] the current agreed theme list and which weekday gets which theme. Bunmi asked again on 24 Nov for themes to be on the calendar.

## [02-workflows/daily-calendar-qa/modes.md](../02-workflows/daily-calendar-qa/modes.md)

- [ ] agreed time for the evening run

## [02-workflows/daily-calendar-qa/scoring.md](../02-workflows/daily-calendar-qa/scoring.md)

- [ ] is the weekly score kept anywhere over time (a sheet or file), so the trend can be shown to Bunmi?

## [02-workflows/friday-calendar-check/README.md](../02-workflows/friday-calendar-check/README.md)

- [ ] usual time on Friday the check is run, and the deadline for must-fix items on Saturday.
- [ ] does Adeyinka review the feedback note before it is posted?
- [ ] who owns the project and how a new person is added to it.
- [ ] are these saved in the project's files, or must they be attached too? Where are the masters kept?
- [ ] is the note saved by hand from the chat, as a Word doc or as text?
- [ ] which WhatsApp group this line goes to.
- [ ] who updates the CT bibles and the Calendar Brief.
- [ ] how and when the draft reaches Bunmi
- [ ] owner
- [ ] who updates it once the current trip ends (early December)
- [ ] who updates the Calendar Brief and CT-02 to match?
- [ ] does Favour have the v1.1 skill in the Favour Calendar Management project, or does it need uploading to Favour's account too?

## [02-workflows/judgment-and-work-requests/README.md](../02-workflows/judgment-and-work-requests/README.md)

- [ ] are the :00 tower routine and Bunmi's :30 routine switched on right now? The repo shows no judgment activity since October and one work request (filed 20 Nov) with no result yet.
- [ ] is the EA expected to set up or babysit Bunmi's routine, or only Logan?
- [ ] should the EA (or successor) have their own :30 routine for judgment and work requests, or only run them interactively inside `/ops-runway`?
- [ ] will there be a policy file for the EA's handle, and which connectors and actions will it lend?

## [02-workflows/meeting-review/README.md](../02-workflows/meeting-review/README.md)

- [ ] Is the routine actually created and switched on in Bunmi's account today, and when did it last run successfully? Check `Meetings/_runlog.md`.
- [ ] Is there a fixed time of day for the `_Inbox` review, and is a SharePoint alert set on `Meetings/_Inbox`?
- [ ] After handover, does the new EA take over first pass and the "Approved" call for internal folders, and should `FIRST_PASS` in the skill config be changed to the new person's name?
- [ ] link to the account/seat setup doc once written
- [ ] who grants SharePoint access to the new EA?
- [ ] whose claude.ai account holds the v1.1 copy, and who will re-upload v1.4?
- [ ] does `_Claude/do-not-name.md` exist in Bunmi's OneDrive yet?
- [ ] does `tier-c.md` exist, and is it current?
- [ ] which subsidiary email domains count as internal?
- [ ] in practice, who writes learning-log entries into the repo — the EA, or Logan from notes the EA sends?
- [ ] how is Ayomide told a folder is ready — SharePoint alert, WhatsApp, email?
- [ ] how Bunmi/Dorathy are told drafts are ready, and who pastes the WhatsApp texts.
- [ ] exact export steps in Fireflies and Plaud, and what file format the EA normally uses.
- [ ] in manual runs, how are the files moved from the chat into SharePoint — download and upload by hand, or by Claude through the Microsoft 365 connector?
- [ ] for a folder made by a manual run, does the EA create the Outlook draft by hand, or does the routine pick it up once moved?
- [ ] who checks Bunmi's Drafts folder for this alert, since it is never sent?
- [ ] should the older `work/policies/external-qa.md` be updated or removed so there is only one version?
- [ ] who besides Bunmi can open Bunmi's routines page?
- [ ] who is allowed to edit `_ledger.json`, and how (it is a JSON file — easy to break)?
- [ ] Is the routine created and switched on in Bunmi's account today, and when did it last run successfully?
- [ ] After handover, does the new EA take over first pass and internal approval, and should `FIRST_PASS` in the skill config change to the new person's name? Today the routine requires `first_pass` to name Adeyinka.
- [ ] Link to the Claude account/seat setup doc once written.
- [ ] Who grants the new EA edit access to `Meetings/` on the BunmiExecutiveOffice SharePoint site?
- [ ] Whose claude.ai account holds the v1.1 copy of the skill, and who will re-upload v1.4?
- [ ] Does `_Claude/do-not-name.md` exist in Bunmi's OneDrive yet?
- [ ] Does `Meetings/_config/tier-c.md` exist, and is it current?
- [ ] Which subsidiary email domains count as internal?
- [ ] Who writes learning-log entries into the repo — the EA, or Logan from notes the EA sends?
- [ ] How is Ayomide told a folder is ready for final QA?
- [ ] How are Bunmi/Dorathy told approved drafts are in Outlook, and who pastes WhatsApp texts?
- [ ] Exact export steps for a full transcript in Fireflies and Plaud, and the usual file format.
- [ ] In manual runs, how do files get from the chat into SharePoint?
- [ ] For a manually made folder, who creates the Outlook draft once approved?
- [ ] Who checks Bunmi's Drafts folder for the "connector down" alert?
- [ ] Who besides Bunmi can open Bunmi's routines page to pause or re-run the loop?
- [ ] Who may edit `_ledger.json` to set `rescreen`, and how?
- [ ] Should the older `work/policies/external-qa.md` be updated or removed?
- [ ] The eight open defaults in SKILL.md section 3 (D1–D8: provisional structures for five types, Executive Brief length, audiences, which types to tune, Bunmi's own AI context, "our signatures", when the next pre-brief is drafted, first pass without a Claude seat) and the hourly schedule — have any been answered?
- [ ] `pre-meeting-brief` and `followup-drafter` still point to Bunmi's OneDrive and the vault for storage and the do-not-name list, while `meeting-artifacts` v1.3+ uses the SharePoint site and `_Claude/` in OneDrive. Are those two skills due an update?
- [ ] Has anyone reviewed the document-type menu counts since the loop went live?
- [ ] Have review edits been made that were never logged in `learning-log.md`?
- [ ] Has the cloud routine completed real runs, and have any Tier C or EXT folders gone through review?

## [02-workflows/meeting-review/document-types.md](../02-workflows/meeting-review/document-types.md)

- [ ] has anyone reviewed the menu counts since the loop went live?

## [02-workflows/meeting-review/version-history.md](../02-workflows/meeting-review/version-history.md)

- [ ] upload done? Then this line can say "account copy = v1.4".
- [ ] have edits been made in review that were never logged? If so, log them so the skill can learn.
- [ ] has the cloud routine completed real runs, and have any Tier C or EXT folders gone through review?

## [02-workflows/ops-runway/README.md](../02-workflows/ops-runway/README.md)

- [ ] is there an expected cadence, e.g. every working day by 12:00 WAT?
- [ ] will the successor reuse the `adeyinka` handle or get their own?
- [ ] does Logan need to share the Station page with the successor separately?
- [ ] should the EA always message Logan the branch name after a session, given copies to `main` are happening every few days rather than hourly?
- [ ] there is no policy file for the EA's handle yet — is read + draft the intended limit?

## [02-workflows/ops-runway/branches-and-pickup.md](../02-workflows/ops-runway/branches-and-pickup.md)

- [ ] is the tower sweep currently hourly, and does it fetch every `claude/*` branch automatically, or does Logan copy ops logs by hand?

## [02-workflows/ops-runway/ops-log-format.md](../02-workflows/ops-runway/ops-log-format.md)

- [ ] does the tower sweep read or ignore these non-flight lines?

## [02-workflows/station-and-flights/README.md](../02-workflows/station-and-flights/README.md)

- [ ] what schedule the sweep is on now, and whether it runs on Logan's machine or as a cloud routine.
- [ ] is it shared per person by Logan, and what can the EA do on it besides Land / Waiting?
- [ ] how should the EA add a new flight — on the Station page directly, a message to Logan, or a back-to-tower line?
- [ ] is the Station shared per person by Logan, and what can the EA do on it besides Land / Waiting?

## [02-workflows/station-and-flights/flight-statuses.md](../02-workflows/station-and-flights/flight-statuses.md)

- [ ] approval by whom — Logan's Approval Queue?

## [02-workflows/two-week-look-ahead/README.md](../02-workflows/two-week-look-ahead/README.md)

- [ ] is Plan mode run by hand each Thursday, or by a scheduled task? If scheduled, which one and at what time?
- [ ] does Adeyinka run this in Claude Code on `Logan-VGG`, or in a plain claude.ai chat? In a plain chat the Station check and the log step are skipped.
- [ ] final save location, and whether/how the look-ahead or its 3-line summary is sent to Bunmi
- [ ] channel used: WhatsApp, Teams or email
- [ ] where Favour's weekly draft is saved, so Claude can find it without it being attached

## [02-workflows/two-week-look-ahead/how-the-calendar-pieces-connect.md](../02-workflows/two-week-look-ahead/how-the-calendar-pieces-connect.md)

- [ ] who sends it and at what time

## [02-workflows/weekly-context-file/README.md](../02-workflows/weekly-context-file/README.md)

- [ ] does Adeyinka run this in a plain chat, a specific Claude project, or a Claude Code session?
- [ ] where the file is saved (OneDrive folder) so it can be found next week for the version number.
- [ ] channel used: WhatsApp, Teams or email.
- [ ] does Favour replace the old file or keep past versions in the project?
- [ ] location
- [ ] should it move to Friday morning to meet the 12:00 Friday deadline?

## [02-workflows/weekly-reports/README.md](../02-workflows/weekly-reports/README.md)

- [ ] which day and time (WAT) the report is due to Central Ops — end of Friday, or Monday morning?
- [ ] is a recurring weekday scheduled task already set up in Adeyinka's account, and at what time WAT?
- [ ] does Logan review the report before it goes to Central Ops?
- [ ] the skill is in Adeyinka's account — will it be shared to the new person's account, or re-uploaded?
- [ ] what the "Logan AI" chat is (a 1:1 with Logan or a group), and whether the new person will be added to it.
- [ ] which Fireflies/Otter account the transcripts come from and whether the new person has access.
- [ ] where the mandate document is stored.
- [ ] how it is submitted (email or Teams), to whom exactly in Central Ops, and where the weekly copies are filed (SharePoint/OneDrive folder).
- [ ] filing location and whether Logan gets a copy.
- [ ] whether internal build codes are acceptable in a report that only goes to Central Ops.
- [ ] which day and time (WAT) the weekly report is due to Central Ops — end of Friday, or Monday morning?
- [ ] is a recurring weekday morning-brief scheduled task already set up in Adeyinka's account, and at what time WAT?
- [ ] does Logan review the weekly report before it goes to Central Ops?
- [ ] the weekly report skill is in Adeyinka's account — will it be shared to the new person's account, or re-uploaded?
- [ ] what the "Logan AI" WhatsApp chat is (a 1:1 with Logan or a group), and whether the new person will be added to it.
- [ ] where the Execution Support Mandate document is stored.
- [ ] how the report is submitted (email or Teams), to whom in Central Ops, and where weekly copies are filed.

## [03-reference/glossary.md](../03-reference/glossary.md)

- [ ] …

## [03-reference/logan-vgg-repo-map.md](../03-reference/logan-vgg-repo-map.md)

- [ ] is `TASKS.md` still maintained now that the Station exists?
- [ ] any update from Uche since 5 Oct?
- [ ] which handover doc covers external QA?
- [ ] link to the handover docs for Bunmi's skills
- [ ] any update from Uche on the Central Ops context worker since 5 Oct?
- [ ] which handover doc covers external QA (`work/policies/external-qa.md`)?
- [ ] will Logan invite the successor as a collaborator, and with push rights to branches only or to `main` too?

## [03-reference/people-and-roles.md](../03-reference/people-and-roles.md)

- [ ] Dorathy's exact role title.
- [ ] Omotola's role title.
- [ ] Margaret's role title, and whether the new person supports Margaret's skills.
- [ ] does Logan approve before submission?
- [ ] does Logan approve the weekly report before submission?
- [ ] who covers Adeyinka's first-pass review and calendar QA during the handover period.

## [03-reference/skills-inventory.md](../03-reference/skills-inventory.md)

- [ ] final folder names for the docs once the 02-workflows map exists.
- [ ] is this in use, and which doc covers it?
- [ ] is `week-ahead` still used now that `calendar-qa` Plan mode exists?
- [ ] which of Bunmi's skills (other than `meeting-artifacts`) are actually installed and in use in Bunmi's Claude today.
- [ ] did Margaret's v2 pack reach Margaret and get installed? The repo notes say the files still had to be sent by hand.
- [ ] whether any of the Canva, Figma or operations plugin skills are used in Adeyinka's work.
- [ ] should the account copy of `meeting-artifacts` (v1.1) be replaced with the repo's v1.4 zip?
- [ ] is `pre-meeting-brief` in use, and which doc covers it?
- [ ] which of Bunmi's skills (other than `meeting-artifacts`) are installed and in use today.
- [ ] did Margaret's v2 pack reach Margaret and get installed?
- [ ] handover docs for concept-docs, okr-alignment, opportunity-screener, ceo-review-catchup, deal-handoff, ghc-deal-brief and Margaret's skills — or are they out of scope for the new person?
- [ ] whether any Canva, Figma or operations plugin skills are used.
