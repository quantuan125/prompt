---
artifact_type: 'ANALYSIS'
planning_level: 'TASK'
initiative_id: 'T102'
initiative_code: 'CWD'
phase: '1'
stream_id: 'T102-PH001-ST001'
activity_id: 'T102-PH001-ST001-AC009'
sub_activity_id: 'T102-PH001-ST001-AC009.1'
task_id: 'AC009.1-TK003'
version: '0.2.0'
date: '2026-02-18'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
purpose: 'Hybrid internal+external second-opinion brief: summarize the current T102-STD-004 design state and the identified clause sequencing problem (adding new clauses inside substandard blocks) for external feedback prior to Gate review.'
governance_rules: 'prompt/templates/consultant/workspace/workspace_documentation_rules.md'
source_stream_plan: 'prompt/artifacts/tasks/T102/consultant/workspace/plan/plan_T102-PH001-ST001.md'
source_proposal: 'prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_PH001-ST001-AC009_std-004-redesign.md'
current_target_std: 'prompt/artifacts/tasks/T102/consultant/standards/standard_T102-STD-004_specification-standard-and-guideline.md'
current_target_id_standard: 'prompt/artifacts/tasks/T102/consultant/standards/T102-STD-005_id-specification-rules.md'
---

# ANALYSIS: AC009.1-TK003 - STD-004 Sequencing Second-Opinion Brief (Hybrid Internal + External References)

## I. Executive Summary

### A. Why this document exists
This analysis summarizes the current state of `T102-STD-004` (as implemented in AC009.1-TK002) and documents a specific design concern that emerged during QA: **how to add new main CLAUSEs into a substandard block (e.g., `T102-STD-004C`) without causing disruptive resequencing or reference drift**, given the current clause-ordering rules.

This artifact is intended for an external consultant to provide a second opinion on:
1) whether the current sequencing model is the right tradeoff for long-term maintainability, and
2) whether a design adjustment is warranted (and if so, what kind), without derailing Phase 1 objectives.

### B. Current Client position (from QA answers)
The Client has set these acceptance intentions for the near term:
- Gate scope: **STD-004-only** acceptance (external surfaces aligned later), consistent with AC009.1 scope in the stream plan.
- Evidence bar: **Approve recommendation** for a stronger evidence style (i.e., not purely narrative).
- Golden exemplar definition: **Document-only** (STD-004 itself is the golden exemplar; other surfaces evolve during ST002 and AC010).

### C. Core problem statement (sequencing)
`T102-STD-004` uses:
- substandards for grouping (A/B/C/D), and
- a single global sequence of main `CLAUSE-###` IDs across the whole `## Specification` section.

The concern is whether this global sequencing model creates unnecessary maintenance risk when:
- new clauses are added inside the middle of the spec (especially within one substandard),
- the spec is expected to remain a stable golden exemplar used to implement other STDs in ST002.

---

## II. Repo-Grounded Context

### A. Where the authoritative requirements live (Phase 1)
This brief is scoped to the Phase 1 combined standard-specification file model, where `T102-STD-004` is the authority for:
- required combined-file structure, and
- how to organize and reference clauses and subclauses.

Primary files in scope for this analysis:
- `prompt/artifacts/tasks/T102/consultant/standards/standard_T102-STD-004_specification-standard-and-guideline.md`
- `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-005_id-specification-rules.md`
- `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_PH001-ST001-AC009_std-004-redesign.md`
- `prompt/artifacts/tasks/T102/consultant/workspace/plan/plan_T102-PH001-ST001.md`

Secondary (context-only) surfaces referenced during review:
- `prompt/templates/consultant/standards/guideline_standard_specs.md`
- `prompt/templates/consultant/standards/template_standard_specs.md`
- `prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md`
- `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-009_governance-standards-specification.md`

### B. Current STD-004 structure (high-level)
`T102-STD-004` is structured as:
- `## Specification` (normative)
- `## Decision Record` (informative ADR annexes; current-first ordering)
- `## References`
- `## Provenance`

Within `## Specification`, there is:
- a `### Specification Index` table (navigation only)
- four substandard blocks: `T102-STD-004A`, `T102-STD-004B`, `T102-STD-004C`, `T102-STD-004D`

---

## III. Governing Clauses That Drive The Sequencing Behavior

### A. Clause ordering rule (the critical constraint)
The sequencing behavior is currently governed by:
- `T102-STD-004-CLAUSE-019A (Sequential numbering)`:
  - Main `CLAUSE` IDs MUST be sequential in the order they appear.
  - When substandards are used, numbering is continuous across substandard boundaries.
- `T102-STD-004-CLAUSE-019B (Subclause adjacency)`:
  - Subclauses must immediately follow their parent clause.

These rules imply that inserting a *new main clause* into the middle of the spec logically forces a renumbering of the subsequent main `CLAUSE-###` IDs (unless the clause is instead modeled as a subclause under an existing clause).

### B. Specification Index role (what it does and does not do)
The Specification Index is governed by `T102-STD-004-CLAUSE-002` and is defined as:
- a navigation index,
- listing main clauses only (no subclauses listed),
- placed immediately after `## Specification`.

Importantly, the index does not provide an alternate ID scheme and does not relax the `CLAUSE-019A` ordering rule. It helps readers locate content, but it does not solve "stable IDs under insertion."

### C. Migration tolerance (cost acknowledgment, not avoidance)
The spec already anticipates that resequencing can be costly:
- `T102-STD-004-CLAUSE-017B (One-time resequencing cost)` requires a controlled migration plan when clause IDs are resequenced.

This is relevant because the sequencing concern is primarily about whether resequencing should be expected as routine maintenance (and if so, how to minimize disruption), or treated as an exceptional event reserved for planned releases.

---

## IV. How Insertions Work Under The Current Model (Observed Implications)

### A. Adding a new requirement inside `T102-STD-004C` (main clause)
If a new requirement is truly a new top-level obligation (i.e., deserves a new main `CLAUSE-###`), then under `CLAUSE-019A`:
- inserting it into the `T102-STD-004C` block implies the subsequent clauses (possibly including those in `T102-STD-004D`) must be renumbered to preserve sequential order.

This has downstream consequences:
- Existing references to `T102-STD-004-CLAUSE-0XX` in other artifacts become stale.
- A controlled migration and reference update effort is required (even if "key surfaces only" are updated).

### B. Adding a new requirement as a subclause (non-disruptive numbering)
`T102-STD-005-CLAUSE-005D` allows an optional subclause suffix form:
- `<STD-ID>-CLAUSE-###<CAPITAL_LETTER>` (e.g., `T102-STD-004-CLAUSE-019C`)

Adding a new requirement as a subclause:
- preserves the parent clause ID (stable),
- avoids renumbering,
- but semantically treats the addition as detail under the parent clause (which may or may not match intent).

### C. Substandard references (categorization vs governance)
`T102-STD-004-CLAUSE-003F` states:
- substandard IDs (e.g., `T102-STD-004C`) and subclause IDs are structural elements,
- they MUST NOT appear as standalone entries in registries, taxonomy tables, or governance indexes (including the STD-005 taxonomy and the Specification Index),
- they MAY be cited in text for navigational precision.

This matters for the sequencing discussion because substandards are a categorization tool, but they are not intended to become new governed token classes.

---

## V. Tension Identified During QA (What Needs A Decision)

### A. The underlying tradeoff
The design tension is between:
- **Stable references** (minimize renumbering, preserve external citations), and
- **Clean categorization + sequencing** (keep each main obligation as its own main clause in the "right" substandard, rather than packing into subclauses).

The current spec implicitly prefers:
- clean clause structure + strict sequential ordering,
while providing:
- subclause expansion as a mechanism for finer structure (and potentially lower churn).

### B. Where the confusion arises
The confusion in practice is: when adding a new clause in `T102-STD-004C`, should authors:
1) append it as the next global clause number at the end of the spec (to preserve numbering), and rely on the Specification Index + substandard column for categorization, or
2) insert it where it belongs in the `T102-STD-004C` block and accept a renumbering migration, or
3) encode it as a subclause under an existing `004C` clause to avoid resequencing?

Under the current written rules, (1) is not compatible with strict "order they appear" sequentiality if the clause is physically located earlier, and (2)/(3) are the two compliant paths.

---

## VI. Questions For External Consultant (Second Opinion Request)

Please provide a recommendation on the following, considering both human usability and toolability:

1) Is global sequential clause numbering across substandards the best long-term tradeoff for a living standard intended to evolve?
2) If not, what alternative numbering model is most standard-like and least risky?
   - Keep global sequence but treat main insertions as "release events" (planned migrations).
   - Allow per-substandard numbering (sequence resets per substandard).
   - Reserve numeric ranges per substandard (e.g., 001-099 for 004A, 100-199 for 004B, etc.).
3) Given the intent that ST002 will replicate the pattern across other STDs, how should the standard express a clear authoring rule-of-thumb for:
   - when to add a new main clause vs a subclause,
   - how to handle inevitable insertions without creating repeated migration churn?

---

## VII. Hybrid Reference Bundle (Internal + External)

### A. Internal references reviewed in this consultation
- Stream plan (AC009.1 scope, TK002/TK003, Gate intent): `prompt/artifacts/tasks/T102/consultant/workspace/plan/plan_T102-PH001-ST001.md`
- Redesign proposal (substandard architecture, resequencing intent, merge rationale): `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_PH001-ST001-AC009_std-004-redesign.md`
- Current standard under discussion: `prompt/artifacts/tasks/T102/consultant/standards/standard_T102-STD-004_specification-standard-and-guideline.md`
  - Sequencing driver: `T102-STD-004-CLAUSE-019 (CLAUSE Ordering)`
  - Index semantics: `T102-STD-004-CLAUSE-002 (Specification Index)`
  - Non-token guardrail: `T102-STD-004-CLAUSE-003F (Non-token status)`
  - Resequencing/migration acknowledgment: `T102-STD-004-CLAUSE-017B (One-time resequencing cost)`
- ID and reference semantics: `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-005_id-specification-rules.md`
  - Subclause ID construction: `T102-STD-005-CLAUSE-005D (Specification Clause Semantics)`
  - Formal vs shorthand references: `T102-STD-005-CLAUSE-004 (Reference Semantics)`

### B. External references (reading list, to be independently verified by the external consultant)
These links were used in the consultation as comparative reading for "how major standards handle clause/subclause references and structure":
- ISO/IEC Directives, Part 2 (Drafting): https://share.ansi.org/isodocs/ISO_IEC_Directives_Part2.pdf
- IEEE Standards Style Manual: https://manualzilla.com/doc/5969892/ieee-standards-style-manual
- W3C Manual of Style: https://www.w3.org/guide/manual-of-style/
- W3C CSS spec markup guidance: https://www.w3.org/Style/spec-mark-up.en.html

Note: The external references above are included as a reading list to support independent review; they are not treated as normative inputs to T102 unless explicitly adopted via a governed decision and recorded in the appropriate T102 artifacts.

---

## VIII. Open Items (For Follow-Up After External Feedback)

1) Should `T102-STD-004` be amended to encode an explicit rule for "adding new obligations" (main clause vs subclause decision rubric)?
2) If a change in numbering model is desired, what is the lowest-risk migration path that preserves Phase 1 stability and avoids repeated churn during ST002?

---

## IX. External Consultant Second Opinion (AC009.1-TK003)

> **Completed**: 2026-02-18
> **Reviewer**: LLM_Consultant (external second-opinion role)
> **Scope**: Independent assessment of all design options for the STD-004 CLAUSE sequencing problem, with weighted criteria, scoring matrix, and final recommendation for Gate review.

---

### A. Validation of Internal Analysis

The internal analysis (Sections I–VIII) is technically accurate in its diagnosis. The governing CLAUSEs are correctly identified (CLAUSE-019A/B), the core tension (stable references vs. clean categorization) is the right lens, and the migration tolerance acknowledgment (CLAUSE-017B) is contextually relevant. Three material gaps are identified below.

**Gap 1 — Incomplete blast-radius framing.**

The analysis frames the concern as "inserting mid-sequence." The actual maintenance cost applies equally to **appending at the end of any non-final substandard**. Under the current allocation (A: 001–008, B: 009–017, C: 018–022, D: 023–029):

| Growth event | CLAUSEs requiring renumber | Blast radius |
|:--|:--|:--|
| Append 1 CLAUSE to T102-STD-004A | B (9) + C (5) + D (7) = **21** | Very high |
| Append 1 CLAUSE to T102-STD-004B | C (5) + D (7) = **12** | High |
| Append 1 CLAUSE to T102-STD-004C | D (7) = **7** | Medium |
| Append 1 CLAUSE to T102-STD-004D | **0** | None |

Only T102-STD-004D is a free growth zone. T102-STD-004B — the substandard most likely to evolve as governance requirements mature — carries the highest blast radius of the inner substandards. This asymmetry was not called out in the analysis.

**Gap 2 — Option 2 disqualification lacked precise diagnosis.**

The internal analysis notes per-substandard reset is incompatible with the current model but does not precisely articulate why. The fatal flaw: T102's CLAUSE-ID format uses the parent STD-ID prefix (`T102-STD-004-CLAUSE-001`), not the substandard ID. Per-substandard reset with this format produces globally ambiguous IDs — two CLAUSEs in different substandards share the same token. However, a variant resolves this by encoding the substandard directly into the CLAUSE-ID format (`T102-STD-004B-CLAUSE-001`). This variant is architecturally coherent and is evaluated independently as **Option 5** below.

**Gap 3 — A fourth option was omitted.**

None of the three options in Section V is a pure authoring-rule fix applied to the current numbering. There is a fourth path: amend CLAUSE-019A to require append-to-substandard-block-end only, with no upfront renumber, at the cost of non-contiguous IDs accumulating over time. Evaluated as **Option 4** below.

---

### B. Design Options — Full Enumeration with Examples

All examples use the same growth scenario: **adding one new CLAUSE to T102-STD-004B** (e.g., a new STD Versioning Policy obligation).

**Baseline (current state):**

```
T102-STD-004A — Core Structure & Lifecycle:   CLAUSE-001 … CLAUSE-008  (8 CLAUSEs)
T102-STD-004B — STD Registry & Governance:    CLAUSE-009 … CLAUSE-017  (9 CLAUSEs)
T102-STD-004C — Specification Authoring:      CLAUSE-018 … CLAUSE-022  (5 CLAUSEs)
T102-STD-004D — Decision Record Authoring:    CLAUSE-023 … CLAUSE-029  (7 CLAUSEs)
```

---

#### Option 1 — Keep Global Sequential; Treat Insertions as Release Events

**Mechanism**: New CLAUSEs are appended at the end of the target substandard's current block using the next sequential global number. All CLAUSEs in subsequent substandards shift. Renumbering is treated as a controlled migration scoped to planned release events.

**Rule changes required**: None. CLAUSE-017B (one-time resequencing cost) already provides acknowledgment; discipline is procedural (governance calendar).

**Example:**

```
Growth event: append new CLAUSE at end of T102-STD-004B block.

Before:
  T102-STD-004B: CLAUSE-009 … CLAUSE-017
  T102-STD-004C: CLAUSE-018 … CLAUSE-022
  T102-STD-004D: CLAUSE-023 … CLAUSE-029

After:
  T102-STD-004B: CLAUSE-009 … CLAUSE-017, CLAUSE-018  ← new
  T102-STD-004C: CLAUSE-019 … CLAUSE-023              ← shifted +1 (12 CLAUSEs renumbered)
  T102-STD-004D: CLAUSE-024 … CLAUSE-030              ← shifted +1

All references to CLAUSE-018 through CLAUSE-029 in all key surfaces must be updated.
```

**Key risk**: Every growth event in B, C, or A triggers a migration sweep of downstream CLAUSEs and reference surfaces. Cost frequency scales with governance evolution pace.

---

#### Option 2 — Per-Substandard Reset with Parent STD-ID Prefix *(Disqualified)*

**Disqualification reason**: Using `T102-STD-004-CLAUSE-001` through `T102-STD-004-CLAUSE-009` in both T102-STD-004A and T102-STD-004B produces globally ambiguous IDs. CLAUSE-003B specifies that CLAUSEs use the parent STD-ID prefix; without substandard encoding, two CLAUSEs in different substandards share the same token. Structurally incompatible with the T102 ID model as currently specified.

The substandard-encoded variant that resolves this ambiguity is evaluated as **Option 5** below.

---

#### Option 3 — Numeric Range Reservation per Substandard *(Recommended)*

**Mechanism**: At initial design time, each substandard is allocated a reserved numeric range. New CLAUSEs are appended within that range. Ranges are sized for significant growth. CLAUSE IDs remain globally unique, retain the parent STD-ID prefix, and are monotonically increasing within each substandard's reserved block.

**Rule changes required**:
- CLAUSE-019A: change "sequential" → "monotonically increasing within each substandard's reserved range; new CLAUSEs MUST be appended at range-block end"
- New CLAUSE-019C: normative range allocation table

**Proposed range allocation:**

| Substandard | Domain | Current CLAUSEs | Reserved Range | Growth Room |
|:--|:--|:--|:--|:--|
| T102-STD-004A | Core Structure & Lifecycle | 001–008 (8) | **001–024** | 16 slots |
| T102-STD-004B | STD Registry & Governance | 009–017 (9) | **025–054** | 21 slots |
| T102-STD-004C | Specification Authoring | 018–022 (5) | **055–074** | 15 slots |
| T102-STD-004D | Decision Record Authoring | 023–029 (7) | **075–099** | 17 slots |

**Example:**

```
One-time upfront renumber:
  T102-STD-004A: CLAUSE-001 … CLAUSE-008   (unchanged — A stays in 001–024 range)
  T102-STD-004B: CLAUSE-025 … CLAUSE-033   (was 009–017; shifted into range 025–054)
  T102-STD-004C: CLAUSE-055 … CLAUSE-059   (was 018–022; shifted into range 055–074)
  T102-STD-004D: CLAUSE-075 … CLAUSE-081   (was 023–029; shifted into range 075–099)

Growth event: append new CLAUSE to T102-STD-004B.
  New CLAUSE assigned: CLAUSE-034 (next available in B's range 025–054)
  T102-STD-004B: CLAUSE-025 … CLAUSE-033, CLAUSE-034  ← new
  T102-STD-004C: CLAUSE-055 … CLAUSE-059               ← UNCHANGED
  T102-STD-004D: CLAUSE-075 … CLAUSE-081               ← UNCHANGED

Zero reference updates required outside T102-STD-004B.
```

**Cost**: One-time renumber of 21 CLAUSEs (A stays unchanged; B, C, D shift once into new ranges). All key surfaces updated once. No further renumbering for routine growth in any substandard thereafter.

---

#### Option 4 — Append-Only Authoring Rule (No Upfront Renumber)

**Mechanism**: Retain global sequential ID assignment. Amend CLAUSE-019A to prohibit physical mid-substandard insertion. New CLAUSEs always appended at the end of the target substandard's current block using the next available global number. No renumber today; non-contiguous IDs accumulate over time within substandards.

**Rule changes required**:
- CLAUSE-019A: add prohibition on mid-substandard insertion; require "append at substandard block end, next global ID"

**Example:**

```
Baseline: current state (001–029).

Growth event 1: append new CLAUSE to T102-STD-004B.
  New CLAUSE assigned: CLAUSE-030 (next global after 029)
  T102-STD-004B: CLAUSE-009 … CLAUSE-017, CLAUSE-030  ← new (non-contiguous gap: 018–029 belong to C/D)
  T102-STD-004C: CLAUSE-018 … CLAUSE-022               ← UNCHANGED
  T102-STD-004D: CLAUSE-023 … CLAUSE-029               ← UNCHANGED

Growth event 2: append another CLAUSE to T102-STD-004B.
  New CLAUSE assigned: CLAUSE-031
  T102-STD-004B: CLAUSE-009 … CLAUSE-017, CLAUSE-030, CLAUSE-031

Over time, T102-STD-004B reference landscape:
  "see CLAUSE-009 through CLAUSE-017 and CLAUSE-030 through CLAUSE-034"
  Non-contiguous, scattered ID sequences within the substandard.
```

**Limitation**: Option 4 avoids a renumber today but produces non-contiguous, scattered ID sequences within substandards over time. Option 4 is Option 3 applied incrementally — it reaches the same practical functional outcome, but via worse intermediate states and without a predictable allocation map for authors or linting tools.

---

#### Option 5 — Substandard-Prefixed CLAUSE IDs (Substandard as Referenceable Token)

**Mechanism**: Substandard IDs become first-class referenceable tokens (citeable, backtick-wrapped). Each substandard owns an independent CLAUSE sequence with its ID embedded in the CLAUSE prefix (`T102-STD-004B-CLAUSE-001`). This directly resolves the ambiguity that disqualified Option 2 by encoding the substandard in the token itself.

**Rule changes required** (significant):
- CLAUSE-003B: update CLAUSE-ID format from `<STD-ID>-CLAUSE-###` to `<SUBSTD-ID>-CLAUSE-###`
- CLAUSE-003D: update to permit substandard IDs as governed citable tokens
- CLAUSE-003F: update "non-token" classification to allow backtick wrapping and per-substandard CLAUSE sequences
- CLAUSE-019A: replace global sequential rule with per-substandard sequential rule
- T102-STD-005 taxonomy (CLAUSE-002): add `SUBSTD` token class or explicit note for substandard ID reference forms
- All 29 existing CLAUSE IDs renamed; all key surfaces updated

**Example:**

```
After full rename (all CLAUSEs):
  T102-STD-004A: T102-STD-004A-CLAUSE-001 … T102-STD-004A-CLAUSE-008
  T102-STD-004B: T102-STD-004B-CLAUSE-001 … T102-STD-004B-CLAUSE-009
  T102-STD-004C: T102-STD-004C-CLAUSE-001 … T102-STD-004C-CLAUSE-005
  T102-STD-004D: T102-STD-004D-CLAUSE-001 … T102-STD-004D-CLAUSE-007

Growth event: append new CLAUSE to T102-STD-004B.
  New CLAUSE: T102-STD-004B-CLAUSE-010 (next in B's own sequence)
  T102-STD-004C: T102-STD-004C-CLAUSE-001 … T102-STD-004C-CLAUSE-005  ← UNCHANGED
  T102-STD-004D: T102-STD-004D-CLAUSE-001 … T102-STD-004D-CLAUSE-007  ← UNCHANGED

Zero cross-substandard impact. Perfect isolation.
```

**Important — two separable sub-decisions within Option 5:**

The client's question contains two distinct decisions that can be evaluated and adopted independently:

| Sub-decision | Governing rule change | Cost |
|:--|:--|:--|
| Allow `` `T102-STD-004B` `` backtick-wrapped in text citations | Amend CLAUSE-003F only | **Very low** — formatting convention; no ID changes |
| Change CLAUSE-ID format to substandard-prefixed | Amend CLAUSE-003B, 003D, 003F, 019A + STD-005 + rename all 29 CLAUSEs | **Very high** — full architectural change |

CLAUSE-003F already permits substandard citation in text ("MAY be cited in text for navigational precision"). Backtick wrapping is an additive, zero-governance-impact formatting improvement compatible with any numbering model.

---

### C. Assessment Criteria and Weights

| Criterion | Weight | Rationale |
|:--|:--|:--|
| **Reference stability** | High | Stale CLAUSE-IDs in key surfaces are the explicit trigger for this review. ST002 will replicate the pattern across 8+ STDs, multiplying future migration cost with each deferred decision. |
| **Authoring simplicity** | High | Agentic LLM authors are the primary user. ID verbosity and complex authoring rules create hallucination and non-conformance risk at scale. |
| **Standard alignment** | Medium | T102 is an internal standard. Pattern credibility matters for consistency and LLM training signal; compliance is not a hard requirement. |
| **Toolability / lintability** | Medium | Automation checks already exist (CLAUSE-007). Rules must be machine-verifiable; toolability directly supports the lint-driven conformance model. |
| **Migration cost (timing)** | Medium | Timing is critical: cost of changing NOW (pre-ST002, STD-004 only) is far lower than post-ST002 (all STD reference surfaces live). Deferral compounds cost. |
| **Navigability** | Low | Already substantially addressed by the Specification Index (CLAUSE-002) and substandard headings. Residual navigability differences between options are minor. |

---

### D. Weighted Decision Matrix

| Criterion | Weight | Option 1 — Release events | ~~Option 2~~ | **Option 3 — Range reservation** | Option 4 — Append-only rule | Option 5 — Substandard-prefixed IDs |
|:--|:--|:--|:--|:--|:--|:--|
| Reference stability | **High** | LOW-MED: every non-final substandard growth triggers migration sweep | — | **HIGH**: zero disruption to other substandards after upfront renumber | MED: no renumber now; non-contiguous IDs accumulate | **VERY HIGH**: per-substandard isolation; no cross-substandard impact ever |
| Authoring simplicity | **High** | HIGH: one number space, no range map | — | **MED-HIGH**: range map needed; append rule is simple | HIGH: simple append rule, no range map | **LOW-MED**: longer IDs; new token class governance; harder for LLMs to construct reliably |
| Standard alignment | Medium | HIGH: ISO/IEEE global sequential | — | MED: RFC-style range reservation (pragmatic) | MED: non-contiguous IDs not standard-like | **MED-HIGH**: resembles ISO Parts per-part sequencing |
| Toolability | Medium | HIGH | — | **HIGH**: range boundaries are lint-checkable | MED: non-contiguous IDs complicate lint | MED: per-substandard validation rules add complexity |
| Migration cost | Medium | LOW: defer pain; no change now | — | MED: one renumber now (21 CLAUSEs; B, C, D; key surfaces once) | **LOW**: no renumber today | VERY HIGH: rename all 29 CLAUSEs + 5 CLAUSE amendments + STD-005 taxonomy + all surfaces |
| Navigability | Low | MED: Index provides categorization | — | HIGH: ID range signals domain | MED-HIGH: Index works; IDs eventually scattered | HIGH: ID prefix directly signals domain |
| **OVERALL** | | **MED** | **DISQUALIFIED** | **HIGH** | **MED-HIGH** | **MED** |

---

### E. Final Recommendation

**Adopt Option 3 (Numeric Range Reservation), implemented now, with amendments to CLAUSE-019A and a new CLAUSE-019C.**

**Rationale — timing is the decisive factor.**
The window for a low-cost structural fix is open now. STD-004 is implemented but ST002 has not started. The one-time renumber (21 CLAUSEs; A stays unchanged) is contained to a single file and its key surfaces. Every release event under Option 1, or every growth event under Option 4, becomes progressively more expensive once ST002 is live and reference surfaces have multiplied. Option 3 absorbs the cost once; all other options spread it across time and grow it.

**Why not Option 5.**
Option 5 achieves the highest possible reference stability but introduces costs that exceed its marginal benefit over Option 3:
- **ID verbosity**: `T102-STD-004B-CLAUSE-001` is substantially longer than `T102-STD-004-CLAUSE-025`. In a system where CLAUSE IDs are embedded extensively in text and tooling, verbosity increases LLM hallucination and non-conformance risk.
- **Governance cascade**: Making substandard IDs first-class tokens requires changes to 5 governing CLAUSEs across two standards (STD-004 and STD-005), creating a larger blast radius than the original STD-009 merge.
- **Boundary erosion**: If substandards become governed token-class entities with independent CLAUSE sequences, the distinction between "substandard of STD-004" and "STD-004B as its own standard" weakens. This conflicts with the consolidation rationale of SES002-DEC001 (which merged STD-009 into STD-004 specifically to prevent drift and context loss).

**Why not Option 4.**
Option 4 avoids a renumber today but produces non-contiguous CLAUSE-ID sequences within substandards over time (e.g., T102-STD-004B eventually references CLAUSE-009 through CLAUSE-017 and then CLAUSE-030 onward). This reduces lintability and authoring clarity, and provides no predictable allocation map. Option 4 is Option 3 applied incrementally — it eventually reaches the same functional state via progressively worse intermediate states.

**Separable sub-decision from Option 5 recommended for adoption regardless of numbering model.**
Amend CLAUSE-003F to explicitly allow backtick wrapping of substandard IDs when cited in text (e.g., `` `T102-STD-004B` ``). This is a zero-cost, zero-governance-impact formatting improvement that improves machine-parseability and reading clarity. CLAUSE-003F already permits substandard citation in text; backtick wrapping is purely additive.

---

### F. Proposed Amendments (Pending Client Approval)

If Option 3 is approved, three targeted amendments to T102-STD-004 are required.

**Amendment 1 — CLAUSE-019A: Sequential numbering → monotonically-increasing-within-range**

> *Current*: "`CLAUSE` IDs MUST be sequential within the parent STD in the order they appear across the Specification section (`001`, `002`, `003`, ...). When substandards are used, numbering is continuous across substandard boundaries."
>
> *Proposed*: "`CLAUSE` IDs MUST be monotonically increasing within each substandard's reserved range in the order they appear (per CLAUSE-019C). New CLAUSEs MUST be appended after the last CLAUSE in the target substandard's current range block. Physical insertion that would require renumbering existing CLAUSE-IDs is PROHIBITED except during a governed release migration with a controlled migration plan per CLAUSE-017."

**Amendment 2 — New CLAUSE-019C: Range Allocation Table (Normative)**

> *New subclause*: "Each substandard in a combined standard-specification file MUST declare a reserved CLAUSE-ID range at the time of initial design. For T102-STD-004, the reserved ranges are:
> - T102-STD-004A (Core Structure & Lifecycle): CLAUSE-001 through CLAUSE-024
> - T102-STD-004B (STD Registry & Governance): CLAUSE-025 through CLAUSE-054
> - T102-STD-004C (Specification Authoring): CLAUSE-055 through CLAUSE-074
> - T102-STD-004D (Decision Record Authoring): CLAUSE-075 through CLAUSE-099
>
> When a substandard's range has fewer than 5 unused IDs remaining, a range extension MUST be planned as a governed migration event per CLAUSE-017."

**Amendment 3 — CLAUSE-003F: Backtick wrapping permission (low-cost; recommended regardless)**

> *Current*: "They MAY be cited in text for navigational precision but carry no independent governance lifecycle and are NOT independent tokens."
>
> *Proposed*: "They MAY be cited in text for navigational precision and MAY be wrapped in backticks when cited inline (e.g., `` `T102-STD-004B` ``) to improve machine-parseability and reading clarity. They carry no independent governance lifecycle and are NOT independent tokens."

---

### G. Open Items (Post-Gate Follow-Up)

1. **Range allocation confirmation**: Does the Client confirm the proposed range sizes (A: 24 slots, B: 30 slots, C: 20 slots, D: 25 slots)? T102-STD-004B is intentionally widest given governance evolution likelihood.
2. **Renumber scope**: The upfront renumber affects 21 CLAUSEs (A stays 001–008; B: 009–017 → 025–033; C: 018–022 → 055–059; D: 023–029 → 075–081). Should this be scoped within AC009.1-TK002 (current implementation task) or as a separate follow-on task?
3. **CLAUSE-019C authoring rubric**: Should a main-clause-vs-subclause decision rubric also be drafted as part of the CLAUSE-019C additions in this Gate cycle, or deferred to ST002?

