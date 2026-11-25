---
title: CLAUDE.md and Markdown files
version: v1.0
last_updated: 2026-11-25
owner: Adeyinka Oshin
---

# 05 — CLAUDE.md and Markdown (.md) files

## 1. What a Markdown file is

`.md` files are plain text with light formatting. Almost everything in this job is
Markdown: skills, logs, setup guides, this handover pack. GitHub and Claude both
display them nicely.

| You type | You get |
|---|---|
| `# Title` / `## Section` | Headings |
| `**bold**`, `*italic*` | **bold**, *italic* |
| `- item` | Bullet list |
| `1. step` | Numbered list |
| `[text](path/or/url)` | A link |
| `` `code` `` | `code` |
| `- [ ] task` | A checkbox |
| `\| a \| b \|` rows | A table |

The block between `---` lines at the top of a file is **frontmatter**: key/value data
like `name:`, `description:`, `version:`. Skills need it (see `06-creating-a-skill.md`);
the handover docs use it for version and date.

## 2. What CLAUDE.md is

A file named `CLAUDE.md` at the top of a repo is read by Claude **at the start of every
session** in that repo. It's the place for standing rules that must travel with the repo.

Examples in use:

- **`Logan-VGG/CLAUDE.md`** (Logan's) — the hard rules for that repo:
  - The repo is **private**; no visibility change, collaborators, forks or copying
    content out without Logan's per-action approval.
  - A list of files not vetted for public release.
  - **Sender choice**: on Logan's own instance, Claude asks *every time* which mailbox an
    email goes from (Logan's VGG Outlook or the AgentMail inbox). No default.
  - What Claude may do freely (read, draft, commit, update `TASKS.md`) vs. must ask first.
  Read the file itself; this is only a summary.
- **`Claude-Config/CLAUDE.md`** — tells every session to keep this handover pack current
  (see `../03-reference/how-this-pack-stays-updated.md`).

## 3. How to write a good CLAUDE.md

1. Start with one line on what the repo is and who owns it.
2. Put **hard rules** first, in plain words, with "never / always / ask first".
3. Say what Claude may do freely — otherwise it asks about everything.
4. Point to other files rather than repeating them ("full process: `judgment/README.md`").
5. Keep it short. If it's longer than ~2 screens, move detail into linked files.
6. Commit it. Changes apply to the **next** session.

## 4. Other places instructions live

| Where | Scope |
|---|---|
| `CLAUDE.md` in a repo | Every session in that repo |
| A skill's `SKILL.md` | Only when that skill runs |
| A claude.ai **Project**'s instructions | Every chat in that project |
| Personal preferences (claude.ai Settings → Profile) | All your chats |
| A routine's prompt | Each run of that routine |

## Change history
| Version | Date | Change |
|---|---|---|
| v1.0 | 2026-11-25 | First written |
