# CAP Alignment Methodology (text-first, tool-agnostic)

**Status:** Draft v0.1
**Audience:** Authors and reviewers working on cross-domain alignment inside this repo
**Purpose:** Turn “context alignment” from rhetoric into a repeatable, reviewable discipline at the language and structure level. No tooling required.

---

## 1. Scope and non-goals

**Scope.** How to decide whether two domain narratives align. Output is a textual verdict that can be audited.
**Non-goals.** No pipelines, scoring systems, CI, or file formats. No policy advice for any domain. This document stops at method.

---

## 2. Core principles

1. **Single Gate.** Alignment is decided in exactly one way: propose a **lens** $call it L$ that receives both sides; if both sides map into the same core under L, alignment holds; if not, produce a **minimal counterexample**. No third option.
2. **Fold precheck.** Before the gate, test for **folds**:

   * Inner fold: same side, regular context, small reformulations. Safe to proceed.
   * Outer fold: crossing a critical boundary. Do not force alignment; provide a counterexample path.
3. **Triad marking.** Every change is labeled:

   * `[G]` disguise: rephrasing without substance change.
   * `[V]` displacement: change of index, parameter, or viewpoint that preserves the object.
   * `[Disc]` divergence: real split that crosses a boundary and requires a counterexample or a new lens.
4. **Class of check.** State the checking class used: smooth, analytic, empirical, jet, or a mix. If using approximate alignment (a “halo”), name the error and the window of validity.
5. **Public audit.** Verdict must include a witness or a minimal counterexample. A naked score is not evidence.
6. **Language boundary discipline.** If language can still decide, do not formalize. Only after distinctions stabilize at the language level do we attempt a gate.

---

## 3. Workflow (seven short steps)

**S0. Segment a small fragment.** Pick a few lines from side A and side B. Describe what each tries to capture. No evaluation, only description.

**S1. Fold precheck.** List likely boundary crossings: description to prescription, structure to behavior, analogy to proof.

* If inner fold: proceed.
* If outer fold: stop alignment and craft a minimal counterexample.

**S2. Propose a lens L.** Give a tiny mapping table A→L and B→L. Only include necessary correspondences.

**S3. State invariants under L.** One to three items that remain stable under L: relation shape, direction of change, commutativity, order type.

**S4. Gate decision.**

* PASS: provide a one-line witness that shows the mapped cores coincide.
* FAIL: provide a one-line minimal counterexample that shows the mapping breaks and why it cannot be repaired.

**S5. Triad marking.** Append `[G]`, `[V]`, or `[Disc]` to each alignment sentence so the reader sees what moved.

**S6. Class note.** State the class of check and whether a halo was used. If halo, include the error statement.

---

## 4. Evidence types

* **Witness (alignment):** the lens L plus a short statement of the shared core or structure preserved under L.
* **Minimal counterexample (non-alignment):** a smallest scene where the proposed L fails and the failure is essential rather than cosmetic. Name the break point and why quick fixes do not repair it.

---

## 5. Cards and templates

**Lens Card**

* A→L: …
* B→L: …
* Invariants under L: … (1–3 lines)

**Alignment Sentence**

* Text: … `[G]` or `[V]` or `[Disc]`
* Rationale (optional, one line): …

**Counterexample Card**

* Scene: …
* Break point: …
* Why it is not repairable in this window: …

---

## 6. Acceptance criteria

Alignment holds only if all of the following are true.

* A reasonable lens L is stated and defended.
* The mapped cores under L coincide or are equivalent in the declared class.
* Changes are dominated by `[G]` and `[V]`. Any `[Disc]` is either quarantined with a counterexample or resolved by a new lens.
* The verdict includes a witness or a minimal counterexample.
* The class of check is declared. If a halo is used, the error and its window are explicit.

---

## 7. Known limits

* **Type gaps.** If the two sides live in incompatible kinds of objects, alignment is not viable.
* **Scale drift.** Mixing micro and macro without handling the bridge invalidates the witness.
* **Proxy illusions.** Same word, different observation. Verify observables, not labels.
* **Description to prescription.** Jumping from “is” to “ought” is an outer fold unless the lens includes a decision rule.
* **Halo limits.** Approximate alignment is not equality. State costs and bounds.
* **No extrapolation.** A verdict holds only on the fragment and class declared. Do not generalize without re-checking.

---

## 8. Reviewer checklist

* [ ] Fragment is small and clearly described on both sides.
* [ ] Fold precheck is explicit; outer folds are handled by counterexample.
* [ ] Lens L is stated with a minimal A→L and B→L table.
* [ ] Invariants under L are clear and few.
* [ ] Verdict is PASS with a witness or FAIL with a minimal counterexample.
* [ ] Sentences carry `[G]/[V]/[Disc]` tags where relevant.
* [ ] Class of check is stated; halo use, if any, includes an error statement.
* [ ] No extrapolation beyond the declared window.

---

## 9. Ultra-compact examples

**Epidemiology → mask policy**

* Lens L: intervention coverage and compliance as effective transmission control.
* Witness: when political polarization is absent, “policy strength” rephrases “intervention intensity” under L `[G]`.
* Counterexample: two districts with same coverage show opposite trends due to polarization `[Disc]`.

**Differential geometry “curvature” → microservice “tech debt”**

* Lens L: non-commuting update paths produce extra remediation work.
* Witness: in locally flat segments of the deployment graph, path order effects vanish `[V]`.
* Counterexample: dependency cycles force irreducible work regardless of route `[Disc]`.

**Entropy → portfolio diversification**

* Lens L: uncertainty quantification.
* Counterexample: high entropy can still carry high tail risk when a long-tail asset dominates CVaR `[Disc]`.
* Conditional witness: maximum entropy is a least-bias prior only under tail constraints `[V]`.

---

## 10. How to use this document

* Authors: run the seven steps, embed Lens and Counterexample Cards where needed, and keep sentences tagged.
* Reviewers: apply the checklist and request either a witness or a minimal counterexample when the gate is invoked.
* Maintainers: keep this methodology as the single source of truth for alignment decisions in text form.

