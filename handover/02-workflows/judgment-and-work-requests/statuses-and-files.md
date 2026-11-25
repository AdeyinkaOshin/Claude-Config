# Statuses, verdicts, outcomes and action tiers

Quick reference. The authoritative definitions are in the Logan-VGG repo at
`judgment/README.md` and `work/README.md`; read those for the full file
layouts. Examples below are invented.

## Judgment items (`judgment/queue/`)

Key fields: id (`J-<nnnn>`), title, assignee (handle), status, priority
(high / normal / low), due, `rev` (revision number), `question` (the one line
to answer), outputs (files to judge), context, processed_feedback.

| Status | Meaning | Set by |
|---|---|---|
| `pending` | Waiting for the assignee | Tower |
| `in_review` | Someone is working it by hand (optional) | Assignee |
| `feedback_given` | Feedback exists for the current `rev` | Tower |
| `needs_more` | Re-opened with new info; `rev` went up | Tower |
| `resolved` | Done, no more judgment needed | Tower |

A good question is answerable in one line. "Thoughts?" gets nothing.

## Judgment feedback (`judgment/feedback/`)

One file per review round, never edited. Sections: Summary, Specific edits,
Rule to remember, Questions for the tower (only for `need_info`).

| Verdict | Meaning | Tower's usual next step |
|---|---|---|
| `on_track` | Ship it, maybe with small edits | Apply edits, land the flight, `resolved` |
| `adjust` | Right direction, specific changes needed | Apply edits; re-open (`needs_more`) or resolve |
| `stop` | Wrong direction or wrong time | Apply nothing; flight to the hold lane; flag to Logan |
| `need_info` | Can't judge without X | Add the missing thing; `needs_more` |

Confidence: high / medium / low.

## Work requests (`work/queue/`)

Key fields: id (`W-<nnnn>`), title, assignee, flight (Station code), status,
allowed (actions), connectors_needed, done_when, due, `revision`,
processed_results. Body: Brief, Steps, Context.

Status runs `pending` → `in_progress` → one of the outcomes below. Bumping
`revision` is the only thing that makes a request pending again.

## Work results (`work/results/`)

One file per run, append-only. Header: id, assignee, revision, outcome,
created, optional `waiting_on` and `blocked_on`. Sections: What was done,
Findings, Drafts created, Waiting on assignee, Next step.

| Outcome | Meaning | Station flight (via tower) |
|---|---|---|
| `succeeded` | `done_when` met | Land it |
| `partial` | Some done; rest waits on the assignee or someone else | Note |
| `blocked` | Missing connector, access or info (named) | Note |
| `failed` | Tried and errored | Back to inbound with reason |
| `declined` | The assignee said no | Back to inbound with reason |

## Action tiers (lowest to highest)

| Tier | Means |
|---|---|
| `read` | Search and read in the connectors |
| `draft` | Create drafts (email, Teams, draft invites). Nothing leaves. |
| `hold` | Private block on the assignee's own calendar, no attendees |
| `book` | Calendar event with attendees — sends invites, treated like sending |
| `send` | Send email or messages |

What actually runs = the stricter of the request's `allowed` and the
person's `work/policies/<handle>.yaml`. No policy file = read + draft.
Unattended routines never get `send`. Each policy also sets booking limits
(hours, time zone, maximum length, allowed attendee domains, no overlaps) —
read the person's policy file in the repo; don't copy it out.
