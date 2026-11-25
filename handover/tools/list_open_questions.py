#!/usr/bin/env python3
"""Collect every [TO CONFIRM: ...] in the pack into 03-reference/open-questions.md."""
import datetime, pathlib, re
ROOT = pathlib.Path(__file__).resolve().parent.parent
pat = re.compile(r"\[TO CONFIRM:?\s*([^\]]*)\]")
out = [f"# Open questions — [TO CONFIRM] items\n\nGenerated {datetime.date.today()} by "
       "`tools/list_open_questions.py`. Answer these, edit the doc, then re-run the script.\n"]
total = 0
for p in sorted(ROOT.rglob("*.md")):
    rel = p.relative_to(ROOT)
    if rel.parts[0] in ("_versions", "_templates") or rel.name == "open-questions.md":
        continue
    seen, items = set(), []
    for q in pat.findall(p.read_text()):
        q = " ".join(q.split())
        if q and q not in seen:
            seen.add(q); items.append(q)
    if items:
        total += len(items)
        out.append(f"\n## [{rel}]({'../' + str(rel)})\n")
        out += [f"- [ ] {q}" for q in items]
out.insert(1, f"\n**{total} open questions.**\n")
(ROOT / "03-reference" / "open-questions.md").write_text("\n".join(out) + "\n")
print(total)
