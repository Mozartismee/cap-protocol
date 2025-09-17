# From Difference to Decision: A Compact Framework for Context Alignment

**Subtitle:** Unifying philosophical distinctions, semantic invariants, and category-theoretic checks into a public, auditable workflow.

---

## Abstract

This document integrates four companion pieces into one operational narrative. We start from Deleuze’s triad of **Difference → Repetition → Identity** as a **minimal landing** and lift it into a **semantic engine** that detects identity illusions. We then **standardize** the semantics for portability and audit. Finally we implement **pullback-mediated alignment** as a structural decision procedure that either certifies alignment or returns a minimal counterexample. The result is a single pipeline that turns cross-domain rhetoric into testable commitments and reproducible checks.

---

## 0) Executive Summary

* **Problem:** Cross-domain prose often feels aligned while being structurally incompatible. We need a minimal standard by which claims must land in observable structure, and a decision procedure that yields either alignment or a counterexample.

* **Approach:** Fix a semantic pipeline

  $$
  \Phi_\kappa \;=\; q_\kappa \circ \rho \circ \mathrm{Obs}_\ast
  $$

  and extract a **Difference Triad** of invariants:

  * **Displacement** $V=\ker d\Phi_\kappa$
  * **Symmetry (Masquerade)** $\mathrm{Aut}_{\Phi_\kappa}$ promoted to a groupoid of local transports
  * **Discriminant** $\mathrm{Disc}(\Phi_\kappa)$ split by source: mechanism vs appearance vs policy

  Use these invariants to drive a category-theoretic **pullback gate**. If the iso-comma 2-pullback exists under declared embeddings, the two reasoning traces align. Otherwise produce the smallest useful counterexample.

* **Outcome:** A single, auditable workflow that goes from philosophical distinctions to runnable evaluation. It is frugal in definitions, explicit about scope, and instrumented for public audit.

---

## 1) Minimal Landing: Difference → Repetition → Identity

**Role in the stack:** Establish the smallest structure that turns the triad into testable content. This is the “law book” that the rest of the system references.

### 1.1 Meaning

Identity is not a vibe. It is a statement constrained by what survives the projection $\Phi_\kappa$. The triad $D_\kappa=(V,\mathrm{Aut}_{\Phi_\kappa},\mathrm{Disc})$ fixes three observable fields that make sameness and difference decidable in public.

### 1.2 Formal significance

* **Minimal public test:** A **fold** local model is the standard boundary scene. Claims of identity must pass the same fold model, so comparison is not cherry-picked.
* **Exactness skeleton:** Short exact sequences and a dynamic normal form provide a compact algebra of changes. They are simple to check and hard to fake.
* **Window discipline:** Results state an **operating window** $H_{\mathrm{reg}}$. This prevents regular conclusions from being misapplied to singular scenes.

### 1.3 One-line structure

* Fix $\Phi_\kappa$.
* Define $V,\mathrm{Aut}_{\Phi_\kappa},\mathrm{Disc}$ and the fold test.
* Publish the window $H_{\mathrm{reg}}$ with an explicit one-line criterion.

---

## 2) Identity-Illusion Semantics: Turning sameness into a diagnosis

**Role in the stack:** Lift the minimal landing into a **semantic engine** that can detect different kinds of “looks the same” and explain why.

### 2.1 Meaning

* **Groupoid symmetry:** Treat symmetries as local transports with composition. This handles locally swappable yet globally distinct semantics.
* **Jet augmentation:** Stabilize boundary behavior by tracking low-order changes. It prevents near-misses from being certified as matches.
* **Temporal and event view:** Record when and how semantic state jumps. Causality leaves marks.

### 2.2 Formal significance

* Makes illusions diagnosable: which symmetry, in which window, producing which failure mode.
* Keeps “almost aligned” under control via jet-level tolerance rather than hand-waving.

### 2.3 Interface to structure

Expose a **semantic compatibility** gate for alignment: $\rho$ and $\Phi_\kappa$ must be synchronized under declared windows. This is the only way in.

---

## 3) Triadic Projection Semantics: Standardization and portable audit

**Role in the stack:** Provide a **stable specification** so multiple teams can read, compare, and audit the same constructs without drift.

### 3.1 Meaning

* Naming is frozen: **Symmetry (Masquerade)** is the canonical label.
* Discriminant splits into sources: **mechanism**, **appearance**, **policy**.
* A **jet-audit** field is required in all reports.

### 3.2 Audit schema

Minimal JSON schema for public reporting:

```json
{
  "window": "H_reg",
  "V_kernel_rank": "int or expression",
  "symmetry_orbits": "description",
  "disc_sources": ["mechanism", "appearance", "policy"],
  "jet_order": 0,
  "stability": "local or global"
}
```

### 3.3 Why it matters

* Cross-paper comparability.
* Lower contribution friction for toy examples and counterexamples.
* Direct embedding into evaluation pipelines.

---

## 4) Pullback-Mediated Context Alignment: A decision procedure

**Role in the stack:** Provide the **machine** that decides alignment and produces witnesses.

### 4.1 Static check

Given embeddings $F: \mathcal{A}\hookrightarrow \mathcal{L}$ and $G: \mathcal{B}\hookrightarrow \mathcal{L}$ and two step-graphs $A\in\mathcal{A}$, $B\in\mathcal{B}$, form the iso-comma 2-pullback in $\mathcal{L}$.

* **Exists:** aligned up to declared equivalence.
* **Fails:** output a minimal counterexample diagram.

### 4.2 Dynamic gate

Only run the static check if **semantic compatibility** holds: the two traces agree on $\Phi_\kappa$ under the stated window. This prevents garbage-in from yielding misleading structure.

### 4.3 Soft alignment

When a strict pullback is too brittle, lift to a **Profunctor Halo** that preserves the same audit fields and yields graded alignment without pretending equality.

### 4.4 Audit ledger

```json
{
  "claim_id": "string",
  "gate": "pullback | halo",
  "window": "H_reg",
  "witness": "diagram-hash-or-pointer",
  "counterexample": "optional",
  "notes": "≤120 chars"
}
```

---

## 5) Minimal examples

### 5.1 Two-line fold example

* Scene A: perturb wording, hold evidence constant.
* Scene B: perturb evidence, hold wording constant.
  Pass if the step-graphs fold to the same normal form under declared symmetries. Otherwise report which discriminant source fired.

### 5.2 Pullback picture

One picture and one sentence per paper:

* **Picture:** the 2-pullback square with embeddings and projections labeled.
* **Sentence:** “Alignment holds if and only if this limit exists in $\mathcal{L}$ under the semantic gate.”

---

## 6) Roadmap and landing plan

### 6.1 Short term

* **CAP core library:**
  `cap.core` for pullback checks and counterexamples.
  `cap.halo` for profunctor-graded alignment.
  `cap.audit` for the JSON ledger.

* **Fold test kit:** Tiny Python package that runs the fold scene and emits the triad fields plus pass or counterexample.

* **Spec linter:** A command that scans Markdown or LaTeX for window declarations, triad fields, and naming discipline.

### 6.2 Medium term

* **Metamorphic testing harness for LLM pipelines:** Automate wording and evidence perturbations, score Layered Semantic Consistency under pullback (LSC-PB), and publish audit artifacts.

* **Event visualization:** Timeline view that highlights semantic jumps, alignment breaks, and repairs.

* **Teaching pack:** One-page glossary, one toy math vignette, one public-discourse vignette, both fold-checked and pullback-checked.

### 6.3 Principles that govern all code

* Single time source injected from the top layer.
* Separation of I/O and core logic.
* All claims carry a window, a gate, and a ledger entry.

---

## 7) Reader’s guide to provenance

This integrated note compresses four roles into one narrative:

* **Minimal Landing** fixes the invariants and the fold test.
* **Semantic Engine** diagnoses identity illusions and manages near-equivalences.
* **Standardization** freezes names and audit fields for portability.
* **Pullback Machine** decides alignment and returns witnesses.

The pieces overlap by design around the same pipeline $\Phi_\kappa$ and the same triad. That overlap is an interface, not redundancy.

---

## 8) Glossary

* **$\mathrm{Obs}_\ast$:** Observation functor from behaviors to observables.
* **$\rho$:** Semantic reducer that compresses observables into forms.
* **$q_\kappa$:** Contextual projection determined by scope $\kappa$.
* **$\Phi_\kappa$:** The composed semantic projection $q_\kappa\circ\rho\circ\mathrm{Obs}_\ast$.
* **$V=\ker d\Phi_\kappa$:** Displacement directions invisible to $\Phi_\kappa$.
* **$\mathrm{Aut}_{\Phi_\kappa}$:** Symmetry groupoid of local transports preserving $\Phi_\kappa$.
* **$\mathrm{Disc}(\Phi_\kappa)$:** Discriminant, split into mechanism, appearance, policy sources.
* **$H_{\mathrm{reg}}$:** Stated operating window where regularity assumptions hold.
* **Pullback gate:** Iso-comma 2-pullback under declared embeddings, guarded by semantic compatibility.
* **Profunctor Halo:** Soft alignment device replacing hard equality with graded preservation.

---

## 9) Minimal interface sketch

```bash
# 1) Run fold on two reasoning traces
cap-fold --scene A.json --scene B.json --window H_reg --out fold_report.json

# 2) Check alignment under the pullback gate
cap-align --left A.steps --right B.steps --emb L.json --gate pullback --out audit.json

# 3) Produce a teaching diagram with ledger
cap-viz --audit audit.json --diagram out.svg
```

---

## 10) Commitments and limits

* The system never claims more than it can audit. Every conclusion carries a window.
* When pullback fails, a counterexample is produced rather than a euphemism.
* The semantic gate prevents structural checks from laundering incompatible content.

---

### One-page takeaway

Identity that matters is what survives $\Phi_\kappa$. The triad $(V,\mathrm{Aut},\mathrm{Disc})$ turns that statement into public invariants. Standardize the fields, then let pullbacks do the judging. If they do not exist, learn from the smallest counterexample.
