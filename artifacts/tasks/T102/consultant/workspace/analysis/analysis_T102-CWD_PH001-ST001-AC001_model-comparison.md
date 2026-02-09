---
artifact_type: 'ANALYSIS'
planning_level: 'ACTIVITY'
initiative_id: 'T102'
initiative_code: 'CWD'
phase: '1'
stream_id: 'T102-PH001-ST001'
activity_id: 'T102-PH001-ST001-AC001'
version: '0.2.0'
date: '2026-02-04'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
purpose: 'Decision-ready comparison of Models A/B/C/D for normative specification placement (“where-spec-lives”) aligned to the target Concept-as-index SSOT role'
governance_rules: 'prompt/templates/consultant/workspace/workspace_documentation_rules.md'
parent_plan: 'prompt/artifacts/tasks/T102/consultant/workspace/plan/plan_T102-PH001-ST001.md'
---

# ANALYSIS: Phase 1 / ST001 / AC001 — “Where-Spec-Lives” Model Comparison (A/B/C/D)

## I. EXECUTIVE SUMMARY

### A. Decision to make (this activity)
Select the authoritative model for **where detailed, enforceable normative specification text lives**, while converting `T102C (CONCEPT)` into a **dynamic working index hub** that supports all SSOT artifacts (SPS/Request/etc.) without becoming bloated.

### B. Target state (locked by QA intent)
1) `T102C (CONCEPT)` functions as a **dynamic registry**:
   - indices + registers + canonical links (repo-relative canonical path),
   - cross-scope discovery for agents (“what exists, where it lives, what is authoritative”),
   - **no embedded long-form spec text** (including ADR bodies and their detailed `Specification/CLAUSE` content).
2) Phase 1 prioritizes **removing detail from Concept**; it does not require immediate separation of ADR narrative vs normative specs (co-location is permitted if it reduces operational complexity).

### C. Recommendation (proposed)
Adopt **Model D (Combined ADR+Spec Files)** as the authoritative “where-spec-lives” model for Phase 1:
1) Extract each ADR body (including its embedded `Specification/CLAUSE`) into a **single dedicated combined file per ADR**.
2) Register the combined files from Concept by **repo-relative canonical path** (index granularity is the whole file; no anchors required in Phase 1).
3) Defer ADR/spec separation to Phase 2 if/when ownership or automation needs require it.

This recommendation is aligned to:
- The Phase 1 goal (“Concept becomes index hub; no bloat including ADR bodies and their CLAUSES”).  
- The client constraint to reduce implementation complexity and file proliferation risk while achieving Concept de-bloating.  

### D. Key gating decision this recommendation depends on
The current system defines `CLAUSE` as **ADR-internal** (`T102-STD-005-CLAUSE-002` / `T102-STD-005-CLAUSE-005D`). Model D preserves that constraint by keeping `Specification/CLAUSE` content inside the ADR’s combined file (rather than attempting to introduce clause IDs in external spec modules in Phase 1).

This analysis assumes **no new token (e.g., `SPEC`) for Phase 1** and instead uses:
- **ADR Index rows** referencing canonical **file path** to the combined file (defined in AC002).

---

## II. DECISION FRAMING (WHY THIS IS HARD)

### A. The core conflict
- You want **Concept to be index-only** (no bloat; agent-friendly discovery).
- You want to avoid a Phase 1 structure that **explodes file count and linking rules**.
- But the current ID system encodes a strong rule: **`CLAUSE` is enforceable but ADR-internal**, which constrains “spec modularization” choices.

Therefore, the Phase 1 decision is not just “where text goes”; it is also “what is the stable, enforceable reference handle for the canonical spec text”:
- `STD` already exists as the handle (`T102-STD-009`).
- The adopted spec must be discoverable, stable, and referenceable at least by canonical path.

### B. What AC001 must output
A decision-ready comparison that:
1) scores Models A/B/C/D against explicit criteria; and
2) makes the **governance delta implications explicit** (especially `CLAUSE` semantics and adoption/linking contracts).

---

## III. AS-IS INVENTORY (EVIDENCE FROM CURRENT SSOT)

### A. What Concept currently contains (T102 SSOT today)
Source: `prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md`

- Size indicator: 1,267 lines (10,274 words).
- Contains full ADR bodies at Initiative scope and selected Epic scope bodies (not index-only).
- Contains significant embedded clause content:
  - `-CLAUSE-` appears ~123 times, concentrated in governance ADRs (`T102-STD-004`, `T102-STD-005`, `T102-STD-009`).

### B. Why this conflicts with the Phase 1 direction
The current Concept acts as both:
1) an **index/register** (tables), and
2) a **canonical spec container** (ADR bodies + clause-heavy specifications).

This dual role:
- increases drift risk (multiple “copies” of rules across artifacts),
- increases context-window pressure (agents must parse long bodies to find “what matters”),
- discourages modular growth (every new standard adds more embedded spec text to Concept).

---

## IV. EVALUATION CRITERIA (SCORING RUBRIC)

Models are evaluated against:
1) **Concept bloat avoidance**: Can Concept remain primarily indexes + links?
2) **Normativity clarity**: Is it obvious “what is enforceable” and where it lives?
3) **Drift resistance**: Does the model reduce duplication and paired-artifact drift?
4) **Traceability & precision**: Can consumers cite a specific obligation reliably (at least by stable canonical reference)?
5) **Compatibility with current `CLAUSE` semantics**: Does it require changing `CLAUSE` being ADR-internal?
6) **Compatibility with `T102-STD-009` adoption contract**: Does it preserve “STD adopts exactly one canonical spec”?
7) **Migration cost / risk**: How much churn and coordination is required in Phase 1?
8) **Tooling potential**: Does it enable future linting/automation without overhauling the system?

Scoring scale: **High / Medium / Low** (with short justification).

---

## V. MODEL DEFINITIONS (A/B/C/D, INTERPRETED FOR THE TARGET STATE)

### Model A — Hybrid ADR Shell
**Definition (from Stream plan)**: Keep ADR lean; keep `CLAUSE` list and primary normative statements inside ADR; link out-of-line detail modules.

**Interpretation for Phase 1 target**:
- Concept: index rows linking to ADRs and (optional) detail modules.
- ADRs: still contain the enforceable `CLAUSE` obligations.
- Detail modules: informative/supporting detail (non-normative), unless governance is changed.

### Model B — ADR Spec Modules + Index
**Definition (from Stream plan)**: Keep ADR as owner of `CLAUSE` but introduce a dedicated Specs Index and external spec modules to reduce Concept bloat.

**Interpretation for Phase 1 target**:
- Concept: index-only hub (ADR index + Specs Index + registers).
- ADRs: either (a) keep enforceable `CLAUSE` text and link to spec modules for detail, or (b) minimize `CLAUSE` and treat spec modules as canonical (requires governance delta).
- Spec modules: external modules discoverable via Specs Index.

### Model C — Standards-Doc Migration
**Definition (from Stream plan)**: Keep ADR lean; move normative specs out of ADR “Specification/CLAUSE” sections into STD-layer spec documents/modules, with explicit traceability strategy.

**Interpretation for Phase 1 target**:
- Concept: index-only hub (STD index mirrors + adopted spec links + ADR rationale index + registers).
- `STD`: authoritative standards handle; each adopts exactly one canonical spec.
- Adopted spec: the canonical normative text lives in dedicated spec document(s).
- ADRs: rationale/alternatives/consequences only; they do not carry the full spec.

### Model D — Combined ADR+Spec Files
**Definition (from Stream plan)**: Extract ADR bodies (including their embedded `Specification/CLAUSE`) into dedicated combined files (one per ADR) and register those files from Concept by canonical path.

**Interpretation for Phase 1 target**:
- Concept: index-only hub (ADR indexes + registers), linking to combined files by canonical path.
- Combined ADR+Spec file: contains both decision narrative and normative `Specification/CLAUSE` content with a clear internal structure boundary.
- Phase 2: separation of ADR vs spec is explicitly deferred unless governance/ownership/tooling needs require it.

---

## VI. COMPARISON MATRIX (A/B/C/D)

| Criterion | Model A (Hybrid ADR Shell) | Model B (ADR Spec Modules + Index) | Model C (Standards-Doc Migration) | Model D (Combined ADR+Spec Files) |
|:--|:--|:--|:--|:--|
| 1) Concept bloat avoidance | **High** — Concept can be index-only if ADR bodies are moved out-of-line. | **High** — Concept becomes registry; modules external. | **High** — Concept becomes registry; canonical spec external. | **High** — Concept becomes registry; ADR bodies moved out-of-line into combined files. |
| 2) Normativity clarity | **Medium** — “Normative lives in ADR `CLAUSE`” is clear, but ADRs can become overloaded. | **Medium→High** — can be clear if module authority is explicit; otherwise risk of “shadow-specs”. | **High** — “Normative = adopted spec; rationale = ADR” is explicit. | **Medium→High** — normative is explicit via `CLAUSE`, but decision + spec co-locate; requires clear internal structure boundary (`## Decision` / `## Specification`). |
| 3) Drift resistance | **Medium** — ADRs still risk accumulating spec-like detail unless strongly constrained. | **High** — strong with an index + modularization, but depends on defining module authority clearly. | **High** — strongest separation: standards adopt a single canonical spec; ADR bodies stay lean; Concept is links-only. | **Medium→High** — removes Concept duplication; churn is contained to one combined file per ADR, but decision/spec edits share the same file. |
| 4) Traceability & precision | **High** — per-clause referencing exists via ADR `CLAUSE` IDs (ADR-internal). | **High (if ADR CLAUSE remains)** / **Medium (if modules lack IDs)** — depends on whether canonical obligations remain in ADR or move into modules. | **Medium→High** — can be strong if spec docs are anchor-addressable and indexed; may be weaker than `CLAUSE` IDs unless a clause-ID strategy is introduced later. | **High** — per-clause referencing remains via ADR `CLAUSE` IDs and the combined file’s canonical path is stable in Phase 1. |
| 5) Compatibility with current `CLAUSE` semantics | **High** — fully compatible (`CLAUSE` stays ADR-internal). | **High (if ADR keeps canonical obligations)** / **Low (if modules are canonical normative text)**. | **Medium** — compatible if adopted specs are referenced by anchor (no `CLAUSE` IDs); **Low** if clause IDs are required inside spec docs without changing governance. | **High** — preserves `CLAUSE` as ADR-internal while still moving content out of Concept. |
| 6) Compatibility with `T102-STD-009` adoption contract | **Medium** — standards can “adopt” ADRs, but ADRs are mixed-purpose (rules+rationale). | **Medium→High** — depends on whether modules become the adopted canonical spec (then high). | **High** — directly aligned: `STD` adopts canonical spec; ADRs hold trade-offs/rationale. | **Medium→High** — `STD.Adopts` can reference the combined file as the Phase 1 canonical artifact; later separation can improve alignment without breaking the Phase 1 objective. |
| 7) Migration cost / risk (Phase 1) | **Low→Medium** — easiest: move ADR bodies out of Concept and index them; minimal governance change. | **Medium** — requires defining and maintaining Specs Index and module lifecycle. | **Medium→High** — requires spec doc/module authoring rules and a clear indexing contract; often implies immediate separation and more files. | **Low→Medium** — primarily “extract and link”: move existing ADR bodies out of Concept into combined files and update indexes. |
| 8) Tooling potential | **Medium** — automation can validate ADR `CLAUSE` patterns, but modular spec detail is hard to validate if informal. | **High** — index enables validation of existence/anchors and lifecycle. | **High** — `STD` adoption contract + stable spec doc anchors create a strong validation surface for lint/review automation. | **Medium→High** — canonical path registry enables inventory and existence checks; Phase 2 can introduce richer validation once separation is adopted. |

---

## VII. REQUIRED GOVERNANCE DELTAS (BY MODEL)

### A. Common deltas (required for any model to satisfy the Phase 1 target state)
1) **Concept-as-index boundary**: define “Concept contains indexes/registers only; no long-form bodies” as a normative rule (likely as an adopted-spec rule under `STD` governance, or as an explicit clause under an ADR governing Concept).
2) **Canonical reference contract**: AC002 must define the standard reference unit for indexed artifacts (at minimum: repo-relative canonical path; anchors may be used where required, but are not mandatory under Model D Phase 1 whole-file granularity).
3) **Tombstones / deprecation**: if specs move, the index must preserve stable references (supersedes/tombstone rows).

### B. Model-specific deltas

#### Model A
- Enforce strict ADR conciseness:
  - ADR `Specification` MUST remain a short clause list; additional detail MUST be IG/INT/NOTE (non-normative).
- Risk: “detail modules” may become shadow-specs unless explicitly marked as non-normative.

#### Model B
- Must resolve the authority of spec modules:
  - **Option B1** (no governance delta): modules are informative only; enforceable obligations remain in ADR `CLAUSE`.
  - **Option B2** (governance delta): modules become canonical normative text; requires new clause/ID strategy (since `CLAUSE` is ADR-internal).

#### Model C
- Must define the canonical “adopted spec doc” contract:
  - Where spec docs live (path conventions),
  - Required internal structure (headings; anchor stability),
  - How Concept indexes them (schema + required columns).
- Must explicitly confirm the Phase 1 stance on clause IDs inside spec docs:
  - **Phase 1 default**: use path+anchor references (no `CLAUSE` token IDs in spec docs).
  - If later “clause IDs” are required, that becomes a governance delta to `T102-STD-005` (introduce a new token or broaden `CLAUSE` scope).

#### Model D
- Must define the canonical “combined file” contract:
  - Canonical directory path (Phase 1),
  - File naming convention,
  - Required internal structure boundary (`## Decision` / `## Specification`),
  - Phase 1 stability rules (paths/names MUST NOT change).
- Must define the ADR Index schema updates needed for external combined files:
  - Replace/extend “Anchor” semantics with a “Canonical Path” reference to the combined file (whole-file granularity).
- Must enumerate the extraction inventory (all ADRs to be extracted across Initiative/Epic/Feature scopes) to avoid partial migration drift.

---

## VIII. RECOMMENDATION (DECISION-READY)

### A. Recommended model: **Model D (Combined ADR+Spec Files)**
Model D is the best Phase 1 fit for the desired Concept role and the client’s complexity constraints:
- Concept becomes an **index/registry** rather than a container of detailed specs (ADR bodies + CLAUSES move out-of-line).
- Phase 1 avoids Model C’s dual-path separation overhead (separate ADR + spec files), while still enabling later separation.
- `CLAUSE` semantics remain intact (`CLAUSE` stays ADR-internal) without introducing a new token in Phase 1.

### B. Implementation stance for Phase 1 (tight scope)
This recommendation assumes Phase 1 will:
1) Treat **Concept as index-only** (register tables + links); any bodies are moved out-of-line and referenced.
2) Treat combined ADR+Spec files as the canonical Phase 1 containers for ADR bodies and their `Specification/CLAUSE` text, referenced by:
   - Concept ADR Index rows using **repo-relative canonical path** to the combined file (whole-file granularity).
3) Keep `CLAUSE` semantics unchanged in Phase 1:
   - `CLAUSE` remains ADR-internal per `T102-STD-005`,
   - no attempt is made to introduce clause IDs outside the ADR combined file in Phase 1.

This is “decision complete enough” to unblock AC002 (ADR Index schema + extraction conventions) without forcing an immediate new-token decision.

### C. Why not Model A or Model B as the primary choice
- Model A reduces Concept bloat, but it does not reduce the “ADR overload” risk and does not create a stable, explicit extraction convention for Phase 1.
- Model B is viable, but it requires an additional authority decision about whether modules are normative; that complexity is intentionally avoided in Phase 1.
- Model C is structurally strong, but it increases Phase 1 operational overhead (more files + dual-path linking rules) relative to the immediate goal of de-bloating Concept with minimal disruption.

---

## IX. DECISION GATE (WHAT THE CLIENT MUST APPROVE TO PROCEED)

To proceed to AC002 and AC003, this activity requires explicit Client confirmation of:
1) **Model selection**: Adopt Model D (Combined ADR+Spec Files) as the authoritative Phase 1 “where-spec-lives” model.
2) **Concept role boundary**: Concept is index/register only; canonical spec bodies do not live in Concept.
3) **Normativity boundary**:
   - Enforceable `Specification/CLAUSE` text remains ADR-internal, but is relocated into combined ADR+Spec files (out of Concept).
   - ADR decision narrative and spec content may remain co-located in Phase 1; separation is deferred.
4) **Traceability mechanism for Phase 1**:
   - “canonical reference = repo-relative canonical path” to combined ADR+Spec files (whole-file granularity; no anchors required in Phase 1).
5) **Token strategy**:
   - No new `SPEC` token in Phase 1 (explicitly deferred); revisit only if canonical-path traceability proves insufficient for later automation.

---

## X. REFERENCES (INTERNAL + EXTERNAL)

### A. Internal (T102 SSOT)
- Plan: `prompt/artifacts/tasks/T102/consultant/workspace/plan/plan_T102-PH001-ST001.md` (Activity `T102-PH001-ST001-AC001`)
- Concept SSOT: `prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md`
- SPS SSOT (STD index + adoption pointers): `prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md`
- Governance rules: `prompt/templates/consultant/workspace/workspace_documentation_rules.md`
- Key normative specs:
  - `T102-STD-004 (Decision Records Index)`
  - `T102-STD-005 (ID Specification & Rules)`
  - `T102-STD-009 (Governance Standards Specification)`

### B. External (industry grounding)
- MADR (Markdown Architectural Decision Records): `https://adr.github.io/madr/`
- arc42 — Architecture Decisions: `https://docs.arc42.org/section-9/`
- ISO/IEC/IEEE 42010:2011 (Architecture description): `https://ieeexplore.ieee.org/document/6129467`
- “Documenting Architecture Decisions” (Michael Nygard template, widely cited ADR baseline): `https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions`
