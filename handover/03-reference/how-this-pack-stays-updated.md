---
title: How this handover pack stays updated
version: v1.0
last_updated: 2026-11-25
owner: Adeyinka Oshin
---

# How this handover pack stays updated

The pack is only useful if it matches how the work is done **today**. Three things keep
it current.

## 1. The standing rule (every session)

`Claude-Config/CLAUDE.md` tells every Claude session in this repo:

> When you change a skill, workflow, routine or setup step — or the user describes a
> new way of doing something — update the matching doc in `handover/` in the same
> session, version it with `handover/tools/new_version.py`, and commit.

So if you improve something while working with Claude in this repo, say
"…and update the handover pack". Claude does the rest.

## 2. The weekly update (scheduled task)

A scheduled task runs **every Friday at 13:47 WAT** in a fresh Claude session. It:

1. Looks at what changed in the last 7 days:
   - commits in `logansherzog/Logan-VGG` (skills, `skills-bunmi/`, `.claude/skills/`,
     `station/`, `ops/`, `judgment/`, `work/`)
   - commits in `AdeyinkaOshin/Claude-Config` (gateway, setup docs)
   - account skills whose `updatedAt` changed (`~/.claude/skills/synced/*/manifest.json`)
2. For each real process change, updates the matching handover doc and runs
   `new_version.py` (old copy saved to `_versions/`, version bumped, CHANGELOG line added).
3. Adds any new skill to `03-reference/skills-inventory.md` and drafts a new workflow
   folder from `_templates/workflow-doc-template.md` if a new workflow appeared.
4. Commits to the `claude/admiring-cerf-tb34e7` branch of `Claude-Config` and pushes.
5. Writes a short summary of what it changed and which **[TO CONFIRM]** items are still open.

It never sends anything and never edits `Logan-VGG`.

To change the day/time or pause it: ask Claude in a cloud session ("update the handover
pack scheduled task to …") or edit it at claude.ai/code/routines.

## 3. Versions — how to see an old way of working

| Where | What |
|---|---|
| Top of each doc (`version:`, `last_updated:`) | Current version |
| Bottom of each doc ("Change history") | Every version of that doc |
| `handover/CHANGELOG.md` | All changes across the pack, newest first |
| `handover/_versions/<path>/<doc>--vX.Y--DATE.md` | A full copy of the doc as it was before each change |
| Git history | Everything, line by line (`git log -- handover/`) |

Version numbers: **v1.1, v1.2…** for an improvement or correction; **v2.0** when the
process changes in a way that makes the old steps wrong (use `--major`).

## 4. Doing it by hand

```bash
python3 handover/tools/new_version.py handover/02-workflows/meeting-review/README.md "Added Ayomide's QA step for external drafts"
```

Then edit the doc, commit and push.

## 5. Resolving [TO CONFIRM] items

Search the pack for `[TO CONFIRM` and answer them. When you replace one, version the doc
("Confirmed X"). The weekly run lists the ones still open.

## Change history
| Version | Date | Change |
|---|---|---|
| v1.0 | 2026-11-25 | First written |
