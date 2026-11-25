# Log format (ops/log)

The calendar QA writes to the ops log in the private `Logan-VGG` repo, in the same format as
the `ops-runway` skill. The tower (Logan's hourly sweep) reads it and updates the Station.

- **File:** `ops/log/YYYY-MM-DD.md`, using the Lagos date. One file per day. Lines are appended.
- **Never edit `station/`.** It's a read-only mirror. The log is how updates get back to the Station.
- **Commit and push only `ops/log/`** at the end of the run.

## One line per Station flight checked

```
- <CODE> · <done|waiting|in_progress|skipped|back-to-tower> · <what was found / next date> · <HH:MM WAT>
```

## One summary line per run

```
- calendar-qa · <mode> · <N> checked, <N> to fix, <N> covered by Adeyinka · <HH:MM WAT>
```

Plan mode uses:

```
- calendar-qa · plan · <N> locked, <N> to book, <N> gaps · <HH:MM WAT>
```

*Example (invented):*

```
- VGG-XXX (placeholder code) · waiting · Invite has no location; asked Udeme to add full address · 18:10 WAT
- calendar-qa · daily (evening) · 12 checked, 3 to fix, 1 covered by Adeyinka · 18:10 WAT
```

Status words: **done** (on the calendar and right), **waiting** (someone else must act),
**in_progress** (partly done), **skipped** (not checked this run), **back-to-tower** (not a
calendar job; send back to Logan).
