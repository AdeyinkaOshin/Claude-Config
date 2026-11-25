# Flight fields, lanes, gates and statuses

Reference for reading `station/flights.md` and `station/flights/<CODE>.md` in
the Logan-VGG repo. Meanings marked **[TO CONFIRM]** are inferred from how the
skills use them and how often each value appears; check with Logan.

## Fields on every flight

| Field | Meaning |
|---|---|
| `code` | Flight ID, `VGG-<number>`. |
| `title` | One-line summary of the ask. |
| `owner` | Person accountable. Can be blank (unassigned). |
| `lane` | Which runway the flight is on (see below). |
| `gate` | Whether the tower has cleared it to be worked (see below). |
| `workstream` | Category; often `unclassified`. |
| `openops` | Link to the matching Central Ops (OpenOps) record, if any. |
| `due` | Due date, `YYYY-MM-DD`. |
| `rock` | ID of the quarterly goal it serves (see `station/rocks.md`). |
| `approval` | Approval state; `waiting` or blank. |
| `source` | Where the ask came from (e.g. a meeting transcript or a chat group, with date). |
| `updated` | When the mirror last wrote this flight (UTC). |

Body sections: `## Brief` (why it is here), `## Context` (source links),
optional `## Draft (not sent)`.

## Lanes

| Lane | Meaning | EA's role |
|---|---|---|
| `ops` | The Ops runway: human-touch work (calls, follow-ups, bookings, chasing). | **Yours.** Worked through `/ops-runway`. |
| `inbound` | New or returned flights waiting for the tower to route. Failed or declined work requests also come back here. | None, unless Logan routes it to ops. |
| `watching` | Flights being tracked, owned and moved by someone else. **[TO CONFIRM]** | Usually none; may chase if asked. |
| `claude` | Flights handled by a Claude routine or skill rather than a person. **[TO CONFIRM]** | None. |
| `hold` | Holding pattern: parked, e.g. after a reviewer said "stop". | None. |
| `landed` | Finished. | None. |

## Gates

| Gate | Meaning |
|---|---|
| `cleared` | Ready to work. `/ops-runway` only picks ops flights with this gate (or no gate). |
| `held` | New flight held for one tower run so judgment and the Central Ops check can land first. Shows as "clears at the next tower run". |
| `duplicate` | Marked as a duplicate of another flight. **[TO CONFIRM]** Don't work it. |

## Approval

| Value | Meaning |
|---|---|
| blank | No approval step pending. |
| `waiting` | Something on this flight is waiting for an approval (for example a send or a judgment call). **[TO CONFIRM: approval by whom — Logan's Approval Queue?]** |

## Ops log statuses (what the EA reports back)

`done`, `waiting`, `in_progress`, `skipped`, `back-to-tower`. Full definitions
in [../ops-runway/ops-log-format.md](../ops-runway/ops-log-format.md).
`waiting` and `in_progress` show on the Station as interim progress.

## Rock statuses

`on_track` / `off_track`, with owner, due date, open flights and landed
flights per rock, in `station/rocks.md`.
