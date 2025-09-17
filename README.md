# Pullback-Mediated Context Alignment — CAP (Context Alignment Protocol)

**One-line claim.** Turn cross-domain “context alignment” from rhetoric into a structural, auditable object: if two domain-specific reasoning traces pull back along an intermediate context **L** to a shared core structure, they align; otherwise we output a minimal counterexample.

**Method (compact).** Philosophical base in **Deleuze** (difference and becoming); technical field via **differential geometry** to model strata, flows, and boundaries; structural implementation by **category-theoretic pullbacks** as the alignment criterion. Measurement layer uses **measure theory / functional analysis** to turn residuals and stability into computable, optimizable quantities; **differential topology** probes robustness under small deformations. We expose a minimal, model-agnostic metric **LSC-PB** (Layered Step Consistency — Pullback-mediated).

---

## Quickstart

```bash
# 1) Run the demo (no external deps; uses stdlib only)
python3 scripts/run_demo.py

# 2) Inspect the generated report
cat artifacts/report.json
```

**Expected:** a deterministic score `s` and a `PASS` flag if `s ≥ 0.92`, plus environment info, data checksum, and provenance.

---

## What the demo does (toy)

* Loads two tiny “domain” traces (C and D) and an intermediate context **L** from `data/example.json`.
* Normalizes both traces via **L**, computes a structural residual Δ, and scores `s = 1 − Δ`.
* Emits `artifacts/report.json` with: score, threshold, PASS/FAIL, SHA256 of data, runtime info, and the commit hash.

---

## Difference Triad (not water’s three states)

This project uses a **Difference Triad** to describe how “difference” shows up in cross-domain reasoning. It is operational, not physical:

* **Displacement** — the semantic role **moves across layers or domains** while the core inferential structure remains isomorphic after re-indexing.
  *Test:* pull back along **L** and check step-graph equivalence; residual stays low.

* **Disguise** — **surface variation masks similarity** (paraphrase, ornament, jargon). Rhetoric changes; structure doesn’t.
  *Test:* normalize via **L**; string-level changes vanish, structural steps persist.

* **Divergence** — **genuine structural fork**; no intermediate **L** yields a shared core.
  *Test:* the pullback square fails; we output a minimal counterexample instead of forcing alignment.

The triad guides failure modes: displacement and disguise should **PASS**; divergence should **FAIL** with a concrete witness.

---

## Metric (LSC-PB)

* **Name:** Layered Step Consistency — Pullback-mediated.
* **Input:** ⟨task `x`, domain contexts `C/D`, perturbation set `{pᵢ}`, model `M`, seed & env⟩
* **Output:** score `s ∈ [0,1]` + an audit bundle (normalized step sets per layer, conflicts, minimal counterexample if any).
* **Threshold (demo):** `PASS` if `s ≥ 0.92` and repeated runs (n=3) show stddev ≤ `1e-3`.

---

## Determinism & Repro

* **Environment lock:** Python minor version is fixed; the demo uses stdlib only.
* **Seed policy:** a single seed controls all pseudo-random choices; determinism is enforced in the demo.
* **Data lock:** inputs ship with SHA256; we verify before scoring and record checksums in `report.json`.

---

## Repository layout

* `scripts/run_demo.py` — one-command demo; emits `artifacts/report.json`.
* `metrics/lsc_pb.py` — minimal metric implementation (toy).
* `data/example.json` — two domain traces + the intermediate context **L**.
* `docs/overview.md` — 1-page map: Deleuze → Diff-Geo → Pullback → Metric.
* `LICENSE`, `.gitignore`.

---

## Docs

* `docs/overview.md` — 1-page mapping (Deleuze → Diff-Geo → Pullback → Metric)
* `docs/cards/pullback_card.md` — Concept card (LSC-PB)
* `docs/primer_deleuze.md` — Short primer
* `docs/cases/` — Two vignettes (mathematics, public discourse)
* `docs/faq.md`, `docs/glossary.md`

> Public note: the repository’s public surface is **English-only**. Original Chinese materials, if any, live under `docs/zh/` with English abstracts alongside.

---

## Further reading (curated)

* `docs/cards/Deleuze_CAP_Concept_Card.md` — Deleuze × CAP: public-facing concept card
* `docs/cards/difference_triad_engine.md` — **Difference Triad Engine** (Displacement / Disguise / Divergence)
* `docs/axioms/dr_axiomata_v3.md` — DR–Axiomata v3 (axioms & structural laws; Bourbaki-style)
* `docs/notes/minimization_algorithm.md` — Automata minimization as an intuition pump for “equivalence folding”
* `docs/reading/atp_cap_reading_priority.md` — *A Thousand Plateaus* × CAP prioritized reading list

---

**CAP = Context Alignment Protocol.**
