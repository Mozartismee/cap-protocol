# Pullback‑Mediated Context Alignment — CAP (Context Alignment Protocol)

**One‑line claim.** Turn cross‑domain “context alignment” from rhetoric into a structural, auditable object: if two domain‑specific reasoning traces pull back along an intermediate context **L** to a shared core structure, they align; otherwise we output a minimal counterexample.

**Method (compact).** Philosophical base in **Deleuze** (difference and becoming); technical field via **differential geometry** to model strata, flows, and boundaries; structural implementation by **category‑theoretic pullbacks** as the alignment criterion. We expose a minimal, model‑agnostic metric **LSC‑PB** (Layered Step Consistency — Pullback mediated).

## Quickstart
```bash
# 1) Run the demo (no external deps; uses stdlib only)
python3 scripts/run_demo.py

# 2) Inspect the generated report
cat artifacts/report.json
```
Expected: a deterministic score `s` and a `PASS` flag if `s ≥ 0.92`, plus environment, data checksum, and provenance.

## What the demo does (toy)
- Loads two tiny “domain” traces (C and D) and an intermediate context **L** from `data/example.json`.
- Normalizes both traces via L, computes a structural residual Δ and score `s = 1 − Δ`.
- Emits `artifacts/report.json` with: score, threshold, PASS/FAIL, SHA256 of data, and runtime info.

## Repository layout
- `scripts/run_demo.py` — one‑command demo; emits `artifacts/report.json`.
- `metrics/lsc_pb.py` — the minimal metric implementation (toy).
- `data/example.json` — two domain traces + the intermediate context L.
- `docs/overview.md` — 1‑page mapping: Deleuze → Diff‑Geo → Pullback.
- `LICENSE`, `.gitignore`.

## License
MIT

## Docs
- `docs/overview.md` — 1‑page mapping (Deleuze → Diff‑Geo → Pullback)
- `docs/cards/pullback_card.md` — Concept card (LSC‑PB)
- `docs/primer_deleuze.md` — Short primer
- `docs/cases/` — Two vignettes (math, public discourse)
- `docs/faq.md`, `docs/glossary.md`

## Further reading (curated)
- `docs/cards/Deleuze_CAP_Concept_Card.md` — Deleuze × CAP concept card (public-facing)
- `docs/cards/difference_triad_engine.md` — 差異三態引擎 概念卡（位移／偽裝／分歧）
- `docs/axioms/dr_axiomata_v3.md` — DR–Axiomata v3（公理與結構定律，Bourbaki 風格）
- `docs/notes/minimization_algorithm.md` — Automata minimization note（作為「等價折疊」直覺對照）
- `docs/reading/atp_mcsr_reading_priority.md` — 《千高原》× CAP 優先級閱讀清單


> Public note: The repository’s public surface is **English‑only**. Original Chinese materials are kept under `docs/zh/` with English abstracts in the corresponding folders.


> Note: **CAP = Context Alignment Protocol** (formerly: CAP). Public surface updated to CAP terminology.
