---
title: GitHub setup
version: v1.0
last_updated: 2026-11-25
owner: Adeyinka Oshin
---

# 02 — GitHub setup

> GitHub is where the shared work lives: Logan's coordination repo, the Station
> mirror, the ops log, skills, and this handover pack. You need an account, access
> to two repos, and GitHub connected to Claude.

## 1. The repos

| Repo | Owner | Visibility | What it holds |
|---|---|---|---|
| `logansherzog/Logan-VGG` | Logan Herzog | **Private** | Coordination repo: Station, ops log, judgment queue, work requests, Bunmi's skills, build plans. See `../03-reference/logan-vgg-repo-map.md`. |
| `AdeyinkaOshin/Claude-Config` | Adeyinka Oshin | **Private** — keep it that way | WhatsApp gateway code + setup, and this handover pack (`handover/`). |

Never make either repo public, add collaborators, or copy files out without the owner's
explicit OK. Logan's repo `CLAUDE.md` makes this a hard rule.

## 2. Create a GitHub account

1. Go to <https://github.com/signup>. Use your work email.
2. Turn on two-factor authentication: **Settings → Password and authentication**.
3. Send your GitHub username to:
   - **Logan** — for an invite to `logansherzog/Logan-VGG`.
   - **The owner of `Claude-Config`** — for an invite there. **[TO CONFIRM: after
     handover, should the repo be transferred to a VGG organisation account instead?]**

## 3. Accept the invites

1. Open the email "… invited you to collaborate on …" and click **Accept**.
2. Open the repo in a browser to check you can see it.
3. You need **write** access (to push branches). Claude sessions push only to
   `claude/*` branches, never directly to `main`.

## 4. Connect GitHub to Claude

1. Go to <https://claude.ai/code>. If it asks you to connect GitHub, do it.
2. Install the **Claude GitHub App** on the repos when GitHub asks
   (<https://github.com/apps/claude/installations/select_target>). Choose
   "Only select repositories" and tick the two repos above.
3. Back in claude.ai/code, open the repo picker and check both repos appear.

If a repo doesn't appear, or a push fails with "permission denied", redo steps 3–4.
If a scheduled routine stops running, GitHub has probably disconnected: routines pause
for up to 72 hours and then switch off. Reconnect and turn the routine back on.

## 5. Branches — how work flows

```
claude/<session-name>  ──(commit + push by Claude)──►  GitHub
          │
          └── merged / copied into main  ──►  everyone sees it
```

- Each Claude session works on its own branch, e.g. `claude/admiring-cerf-tb34e7`.
- In `Logan-VGG`, the hourly "tower" job on Logan's side copies results (ops logs,
  feedback, work results) from `claude/*` branches into `main`. You don't merge by hand.
- In `Claude-Config` there is **no `main`**; the working branches are
  `claude/fervent-darwin-wmmctg` (WhatsApp gateway — Railway deploys from it) and
  `claude/admiring-cerf-tb34e7` (this handover pack). **[TO CONFIRM: create a `main`
  and merge both, so a newcomer has one obvious branch?]**

## 6. Everyday git words

| Word | Meaning |
|---|---|
| commit | A saved snapshot of changes with a message |
| push | Upload commits to GitHub |
| pull / fetch | Download the latest from GitHub |
| branch | A separate line of work |
| merge | Bring one branch's changes into another |
| PR (pull request) | A request to merge, with a review step. Claude only opens one when asked. |

You rarely type git commands yourself — ask Claude: "commit and push this",
"pull the latest main", "what changed this week?".

## 7. Checklist

- [ ] GitHub account with 2FA
- [ ] Access to both repos (write)
- [ ] Claude GitHub App installed on both
- [ ] Both repos show in the claude.ai/code picker

## Change history
| Version | Date | Change |
|---|---|---|
| v1.0 | 2026-11-25 | First written |
