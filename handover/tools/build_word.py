#!/usr/bin/env python3
"""Build one Word (.docx) file per handover doc, mirroring the folder structure.

    python3 handover/tools/build_word.py

Output: handover-word/ next to handover/ (same subfolders, same names, .docx).
Links between docs are rewritten to point at the matching .docx files.
Old versions (_versions/) are not converted. Run after any doc change; the
weekly update task runs it too.
"""
import pathlib
import shutil
import subprocess
import sys
import tempfile

import docx
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt, RGBColor

HANDOVER = pathlib.Path(__file__).resolve().parent.parent
OUT = HANDOVER.parent / "handover-word"

LUA = r'''
function Link(el)
  local t = el.target
  if t:match("^https?:") or t:match("^mailto:") then return el end
  local path, anchor = t:match("^([^#]*)(#?.*)$")
  if path:match("%.md$") then
    path = path:gsub("%.md$", ".docx")
  elseif path:match("/$") then
    path = path .. "README.docx"
  end
  el.target = path .. anchor
  return el
end

function Meta(m)
  local bits = {}
  if m.version then table.insert(bits, "Version " .. pandoc.utils.stringify(m.version)) end
  if m.last_updated then table.insert(bits, "Last updated " .. pandoc.utils.stringify(m.last_updated)) end
  if m.owner then table.insert(bits, "Owner: " .. pandoc.utils.stringify(m.owner)) end
  if #bits > 0 then m.subtitle = table.concat(bits, "  ·  ") end
  m.sources = nil
  return m
end
'''


def set_borders(table):
    tblPr = table._tbl.tblPr
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), "single")
        el.set(qn("w:sz"), "4")
        el.set(qn("w:space"), "0")
        el.set(qn("w:color"), "BFBFBF")
        borders.append(el)
    tblPr.append(borders)
    # shade header row
    if table.rows:
        for cell in table.rows[0].cells:
            tcPr = cell._tc.get_or_add_tcPr()
            shd = OxmlElement("w:shd")
            shd.set(qn("w:val"), "clear")
            shd.set(qn("w:color"), "auto")
            shd.set(qn("w:fill"), "E8EEF4")
            tcPr.append(shd)


def polish(path):
    d = docx.Document(str(path))
    styles = d.styles
    for name, size in (("Normal", 10.5), ("Body Text", 10.5), ("First Paragraph", 10.5),
                       ("Compact", 10.5)):
        try:
            st = styles[name]
        except KeyError:
            continue
        st.font.name = "Calibri"
        st.font.size = Pt(size)
    for name in ("Title", "Heading 1", "Heading 2", "Heading 3"):
        try:
            st = styles[name]
        except KeyError:
            continue
        st.font.name = "Calibri"
        st.font.color.rgb = RGBColor(0x1F, 0x3A, 0x5F)
    for t in d.tables:
        set_borders(t)
    for p in d.paragraphs:
        if p.style.name == "Subtitle":
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            for r in p.runs:
                r.font.size = Pt(10)
                r.font.color.rgb = RGBColor(0x59, 0x59, 0x59)
    d.save(str(path))


def main() -> int:
    if not shutil.which("pandoc"):
        print("pandoc is not installed")
        return 1
    if OUT.exists():
        shutil.rmtree(OUT)
    with tempfile.NamedTemporaryFile("w", suffix=".lua", delete=False) as f:
        f.write(LUA)
        lua = f.name
    count = 0
    for md in sorted(HANDOVER.rglob("*.md")):
        rel = md.relative_to(HANDOVER)
        if rel.parts[0] == "_versions":
            continue
        dest = OUT / rel.with_suffix(".docx")
        dest.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(
            ["pandoc", str(md), "-f", "gfm+yaml_metadata_block", "-o", str(dest),
             "--lua-filter", lua, "--resource-path", str(md.parent)],
            check=True,
        )
        polish(dest)
        count += 1
    (OUT / "README.txt").write_text(
        "Word copies of the handover pack, one file per doc.\n"
        "Generated from handover/ by handover/tools/build_word.py - do not edit these;\n"
        "edit the .md files in handover/ and re-run the script.\n"
        "Start with README.docx.\n"
    )
    print(f"{count} Word files in {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
