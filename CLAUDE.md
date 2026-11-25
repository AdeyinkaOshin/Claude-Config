# Repo instructions for Claude sessions

This is Adeyinka Oshin's private config repo: the WhatsApp gateway (`gateway/`,
`SETUP.md`, `CLOUD-NOTES.md`) and the **handover pack** (`handover/`), which documents
every setup step and workflow so someone else can take the work over.

## Hard rules

- **This repo stays private.** Never change visibility, add collaborators, fork, or copy
  its contents anywhere public without Adeyinka's explicit approval in the current turn.
- **No secrets in files.** Keys (`GATEWAY_KEY`, `WAHA_API_KEY`, etc.) live in Railway and
  environment settings only.
- The handover pack describes processes. It must not contain: email addresses or phone
  numbers, meeting/deal/counterpart details, personal/family/health information about
  anyone, flight contents from the Station, internal build IDs or Build Router terms from
  Logan's repo, finance/compensation detail, or copies of files from `logansherzog/Logan-VGG`
  (point to their paths instead — that repo's `CLAUDE.md` forbids copying out).

## Keep the handover pack current — standing rule

Whenever, in this repo, you change or learn about a change to a skill, workflow, routine,
connector or setup step:

1. Find the matching doc in `handover/` (see `handover/README.md` for the map). If none
   fits, create one from `handover/_templates/workflow-doc-template.md` and add it to the map.
2. Run `python3 handover/tools/new_version.py <doc> "<what changed>"` (add `--major` if the
   old steps are now wrong). This snapshots the old version into `handover/_versions/`,
   bumps the version, and logs it in `handover/CHANGELOG.md`.
3. Make the edit. Keep steps concrete enough for a newcomer.
4. Unknown facts → write `[TO CONFIRM: question]` instead of guessing.
5. Commit and push.

## What Claude may do freely here

Read anything, edit and add files under `handover/`, commit and push to the working branch.

## Ask first

Visibility or collaborator changes, deleting files someone else added, force pushes,
changes to `gateway/` that affect the live Railway deployment.
