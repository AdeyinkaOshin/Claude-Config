#!/usr/bin/env python3
"""Snapshot a handover doc, bump its version, and log the change.

Usage (run from anywhere):
    python3 handover/tools/new_version.py <doc.md> "<what changed>" [--major]

What it does:
1. Copies the doc as it is NOW into handover/_versions/<same path>/<name>--vX.Y--DATE.md
   (so the old way of doing things is never lost).
2. Bumps `version:` in the frontmatter (v1.2 -> v1.3, or v1.2 -> v2.0 with --major)
   and sets `last_updated:` to today.
3. Adds a row to the doc's "Change history" table.
4. Adds a line to handover/CHANGELOG.md.

Make your content edits FIRST or AFTER — either works — but run this once per change.
"""
import datetime
import pathlib
import re
import shutil
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent  # .../handover


def main() -> int:
    args = [a for a in sys.argv[1:] if a != "--major"]
    major = "--major" in sys.argv
    if len(args) != 2:
        print(__doc__)
        return 1
    doc = pathlib.Path(args[0]).resolve()
    note = args[1].strip()
    if not doc.is_file():
        print(f"not found: {doc}")
        return 1
    rel = doc.relative_to(ROOT)
    text = doc.read_text()
    today = datetime.date.today().isoformat()

    m = re.search(r"^version:\s*v(\d+)\.(\d+)", text, re.M)
    old = (int(m.group(1)), int(m.group(2))) if m else (1, 0)
    new = (old[0] + 1, 0) if major else (old[0], old[1] + 1)
    old_s, new_s = f"v{old[0]}.{old[1]}", f"v{new[0]}.{new[1]}"

    snap_dir = ROOT / "_versions" / rel.parent / rel.stem
    snap_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(doc, snap_dir / f"{rel.stem}--{old_s}--{today}.md")

    if m:
        text = re.sub(r"^version:\s*v\d+\.\d+", f"version: {new_s}", text, count=1, flags=re.M)
    if re.search(r"^last_updated:", text, re.M):
        text = re.sub(r"^last_updated:.*$", f"last_updated: {today}", text, count=1, flags=re.M)

    row = f"| {new_s} | {today} | {note} |"
    if "## Change history" in text:
        text = text.rstrip("\n") + "\n" + row + "\n"
    else:
        text = (text.rstrip("\n") + "\n\n## Change history\n| Version | Date | Change |\n"
                "|---|---|---|\n" + row + "\n")
    doc.write_text(text)

    log = ROOT / "CHANGELOG.md"
    entry = f"- **{today}** · `{rel}` {old_s} → {new_s} — {note}\n"
    lines = log.read_text().splitlines(keepends=True)
    marker = "<!-- new entries below this line -->"
    for i, line in enumerate(lines):
        if marker in line:
            lines.insert(i + 1, entry)
            break
    else:
        lines.append(entry)
    log.write_text("".join(lines))
    print(f"{rel}: {old_s} -> {new_s} (snapshot in _versions/)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
