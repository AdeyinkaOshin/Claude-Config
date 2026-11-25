# Document types the skill can draft

Part of the [meeting review workflow](README.md). The menu in each folder (`03_menu.md`) is
picked from these 19 types. This page is a summary only.

Full templates: `Logan-VGG/skills-bunmi/meeting-artifacts/templates.md`.
Long skeletons for the big external documents: `Logan-VGG/skills-bunmi/concept-docs/`.

- Types 1–16 are Ayomide's list (sent by Adeyinka on 5 Oct 2026).
- Types 17–19 were added because they show up in Bunmi's real documents.
- **Provisional** means there is no finished standalone VGG example yet. Drafts of these carry
  `structure: provisional` in `status.md` until Ayomide supplies an example.

## The 19 types

| # | Type | Use when | Length / format | Usual audiences | Structure |
|---|---|---|---|---|---|
| 1 | Concept Note | An institution head named a problem and VGG answers with a programme | A4 paper, ~6–10 pages | EXT (cover note for EO/SUB) | From a finished VGG document |
| 2 | Partnership / Commercial Proposal | Proposing a jointly governed platform or company to a public or quasi-public institution | 16:9 deck, 20–24 slides in 6 parts | EXT | From a reference document |
| 3 | Strategic Proposition / Executive Deck | Asking one capital provider (DFI, guarantor, pension fund, bank) to anchor a platform | 16:9 deck, 10–12 slides | EXT | From a reference document |
| 4 | Product / Solution Proposition | A large institution has a build need VGG can meet with a reusable product | 16:9 deck, 14–16 slides | EXT | From a reference document |
| 5 | Company / Capability Profile | Introducing a VGG company or platform | 16:9 deck, 8–10 slides | EXT | From a reference document |
| 6 | Pre-Brief / Meeting Brief | A next meeting Bunmi will attend was agreed | 1 page, due 24 h before | EO, SUB | From Bunmi's planning-pack format |
| 7 | Context Note / Intelligence Note | Every Tier B and C meeting (it is `01_brief.md`) | Under 250 words | EO, SUB | Fixed by the skill |
| 8 | Executive Brief / 1–2 Pager | Bring a senior person up to date, or reset how a team runs | A4, default 2 pages (ask before longer) | EO, sometimes SUB | From finished VGG documents |
| 9 | Decision Note / Recommendation Memo | One person or body must say yes or no | A4, 1 page (3 max with annex) | EO, sometimes SUB | **Provisional** |
| 10 | Opportunity Assessment / Business Case | Asking a customer's finance or operations lead to commit to a first step | 16:9 deck, 12 slides + appendix | EXT | From a reference document |
| 11 | Workplan / Roadmap | A partnership is scaling, a plan has 4–8 workstreams, or a working session must end in decisions | Deck, one page per workstream (30/60/90 days), or A4 agenda | EO, SUB, EXT when joint | From finished VGG documents |
| 12 | Legal / Transaction Structuring Brief | A governing body must approve a new legal or commercial structure | A4 paper, 12–20 pages, annexes | EXT | From a reference document. Never drafts contract wording; law-dependent points are flagged for counsel. |
| 13 | MoU / Agreement Brief | An MoU is about to be drafted and scope must be agreed first | A4, 2–4 pages, or 2 slides | EO (internal variant), EXT (counterparty variant) | **Provisional**. Intent only, no clause wording. |
| 14 | Stakeholder / Ecosystem Map | A deal has several parties and the reader must see who brings and gets what | 1–2 slides | EXT | **Provisional** |
| 15 | Customer / User Journey | The reader must follow one unit from start to cash | 1 slide or one section | EXT | **Provisional** |
| 16 | Funds Flow / Transaction Flow / Architecture Schematic | The reader must see how money, ownership or data moves | One diagram per slide | EXT | **Provisional**. No amounts unless cleared. |
| 17 | Q&A / Objection Prep | A principal will test a proposal next meeting (afterwards it becomes a replay) | A4, ~5 pages, 6–9 questions | EO, SUB | Added type |
| 18 | Strategy Framework / Vision Document | An institution needs a model to adopt, or Bunmi hands an ambition back as a plan | A4, 8–12 pages, or deck 24–30 slides | EXT | Added type |
| 19 | Meeting Notes and Action Tracker | A meeting set direction or assigned work (full form of the context note) | Notes + action table | EO, SUB | Added type |

For types 1–5, 10, 12, 14–16 and 18, the EO and SUB audiences get a short cover note only; the
document itself is the EXT version.

## How long documents are drafted

For the long external documents (types 1–5, 10, 12, 18) the skill writes the menu entry and a
`brief.md`, then runs the `concept-docs` skill for the draft, a critique pass and a read copy
(.docx or .pptx). If `concept-docs` is not installed, it drafts from the compact template, marks
it `structure: compact`, and says so in `status.md`.

## House rules for every type (summary)

- Argument order: the reframe, why this reader and why now, the gap, the model, proof, discipline,
  the bounded ask, the path, the close.
- Short sentences, British spelling, one takeaway per slide or section.
- The ask is small, dated and reversible, and says what it does not require.
- Anything not in the inputs is `[[TBC: what is needed]]`. Amounts are `[amount: Bunmi to fill]`
  unless they are in the inputs and cleared.
- No signature block, logo or copyright footer — Ayomide adds them.
- Templates carry structure and voice only. One deal's facts never move into another deal's document.

## Which types come up most

Not known yet. Every run logs the types on the menu (in `_runlog.md` and `learning-log.md`) so
the count can show which types to tune first. **[TO CONFIRM: has anyone reviewed the menu counts since the loop went live?]**
