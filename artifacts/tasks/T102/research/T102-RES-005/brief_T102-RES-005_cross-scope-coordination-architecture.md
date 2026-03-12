---
artifact_type: 'RESEARCH_BRIEF'
initiative_id: 'T102'
research_id: 'T102-RES-005'
version: '1.0.0'
iteration: '1'
date: '2026-02-09'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
---

# RESEARCH BRIEF: Cross-Scope Coordination Architecture (`T102-RES-005`)

## I. EXECUTIVE SUMMARY

**Context**: The T102 initiative uses multiple coordination mechanisms across workscopes (SPS, Request, Concept) including explicit inheritance tables (`T102-STD-003`), tokenized integration guidance (`INT` per `T102-STD-005-CLAUSE-005C`), and a dual-index research register architecture (`T102-STD-006`). In practice, coordination signals can degrade into static reminders and repeated table patterns (SPS bloat), while still failing to provide decision-ready, audit-friendly cross-scope alignment.

**Objective**: Evaluate candidate cross-scope coordination architectures and recommend a decision-ready approach for T102 that improves alignment, reduces drift and bloat, and preserves traceability under the `T102-STD-001` operating model. This research explicitly treats `T102-STD-003` as one candidate mechanism among alternatives and includes “Research Index Placement & Governance” as an absorbed subtopic via `T102-STD-006`.

**Target Deliverable**: A structured research report consumed by `LLM_Consultant` for producing integration recommendations (recommendations-only; no clause-level STD drafting). The report must include a neutral, multi-approach comparison rubric, an explicit recommendation with rationale, and an actionable delta list for impacted standards and SSOT responsibilities.

---

## II. RESEARCH SCOPE & TOPICS

### Part A: Current State Inventory & Problem Characterization

#### Topic 1: Coordination Surfaces Inventory (`P1`)

**Objective**: Enumerate where cross-scope coordination currently occurs across SSOT artifacts (SPS, Concept, Request) and characterize each surface’s intent vs observed use.

**Context**: Coordination appears in multiple forms (tables, registers, inline references, guidance tokens). Without an explicit inventory, proposals risk solving the wrong problem (e.g., “remove tables” vs “repair coordination system”).

**Specific Questions**:
* Which coordination surfaces exist today (Inherited Considerations tables, External Reference lines, INT items, Research registers, Notes patterns, etc.) and where are they hosted?
* For each surface, what is the intended role (decision authority, traceability, integration guidance, index) vs actual observed usage?
* Which surfaces are authoritative vs informative (normative vs non-normative), and is that boundary consistently respected?

**Deliverable**: A coordination surfaces inventory table with: surface name, hosting location(s), authority level, intended purpose, observed behavior, and known failure modes (bloat, drift, ambiguity, poor scanability).

#### Topic 2: `T102-STD-003` (Explicit Inheritance Model) Effectiveness Review (`P1`)

**Objective**: Evaluate whether `T102-STD-003` achieves cross-scope coordination goals in practice and identify the primary drivers of “bloat vs effectiveness” tension.

**Context**: The resequencing decision expands RES-005 from “inherited-considerations viability” into the broader question: is embedded inheritance-table coordination sufficient, or does T102 need a different architecture.

**Specific Questions**:
* Are Inherited Considerations tables being used per `T102-STD-003-CLAUSE-001/002/003` (delta-only, <=5 critical IDs, precedence/variance discipline)?
* What bloat patterns exist (repeated headings, low-signal empty tables, overly broad categories), and what is their cost (scanability, authoring overhead, LLM context)?
* Do embedded inheritance tables produce actionable coordination outcomes, or do they mostly restate that inheritance exists?

**Deliverable**: A gap analysis for `T102-STD-003` implementation (compliance + effectiveness), including a bloat taxonomy with concrete exemplars and root-cause hypotheses.

#### Topic 3: Token-Based Cross-Scope Coordination via `INT` (`P2`)

**Objective**: Evaluate whether `INT` (Integration Guidance) is an effective coordination mechanism for cross-scope alignment and what its limits are.

**Context**: `INT` is explicitly non-normative but is allowed to carry cross-scope coordination guidance. It also has a scoped exception for peer references at Feature/Story scope.

**Specific Questions**:
* Where is `INT` used today in T102, and what kinds of coordination problems does it address?
* What is the governance loop for graduating stable `INT` patterns into formal standards/ADRs (per `T102-STD-005-CLAUSE-005C`)?
* What failure modes occur when coordination is only guidance (no enforcement/audit mechanism)?

**Deliverable**: A concise assessment of `INT` suitability as a primary vs secondary coordination surface, with explicit “best-fit” use cases and “do not use” boundaries.

#### Topic 4: Research Index Placement as a Coordination Subsystem (`P1`)

**Objective**: Evaluate research artifacts indexing placement/governance (`T102-STD-006`) as a worked example of coordination architecture (local vs centralized, link-don’t-duplicate, maintenance protocol).

**Context**: Old RES-006 is collapsed into RES-005. Research indexing is now a required subtopic, not a separate commission.

**Specific Questions**:
* Does the current `T102-STD-006` dual-index architecture (SPS local tables + Concept aggregation register) function as intended?
* What are the tradeoffs between SPS-only, Concept-only, and dual-index for coordination, scanability, and drift risk?
* How should research indexing interact with other coordination surfaces (inheritance tables, INT items, Concept registers)?

**Deliverable**: A decision-ready comparison of research indexing placement options and governance implications, with a recommended placement strategy aligned to the broader coordination architecture recommendation.

---

### Part B: Architecture Options Evaluation (Multi-Approach, Neutral)

#### Topic 5: Candidate Coordination Architecture Families (`P1`)

**Objective**: Define and normalize the candidate architectures to enable fair comparison.

**Specific Questions**:
* What is the minimal definition of each architecture family and its governance contract?
* Where does each architecture place “coordination truth” (embedded in every artifact vs centralized registers vs guidance tokens vs hybrid)?
* What constitutes “success” for each architecture in T102’s operating model (what must get better vs what can remain imperfect)?

**Deliverable**: A short architecture “cards” set for each candidate:
1. Embedded coordination (inheritance tables per `T102-STD-003`)
2. Centralized coordination (Concept as coordination hub)
3. Token-based coordination (`INT` patterns as the primary coordination surface)
4. Hybrid coordination (explicitly defined combination with clear boundaries)

#### Topic 6: Options Comparison Rubric + Scoring Matrix (`P1`)

**Objective**: Produce a multi-approach comparison rubric that enables a decision-ready recommendation without premature lock-in.

**Rubric requirements**:
* Use the same criteria set across all candidate architectures.
* Prefer equal weighting unless a criterion is explicitly elevated by the Client in a later gate.
* Include both qualitative notes and a numeric score per criterion.

**Required comparison criteria (baseline)**:
* **Scanability** (executive readability; low noise)
* **LLM Context Cost** (token burden at scale; avoidance of redundant context)
* **Governance Traceability** (auditability, unambiguous authority boundaries)
* **Maintenance Burden** (ongoing update cost; drift risk)
* **Coordination Effectiveness** (does it actually change outcomes, not just document them)
* **Cross-Scope Directionality Safety** (respects `T102-STD-005-CLAUSE-003` directionality and exceptions)
* **Standards Interface Fit** (how much STD/ADR surface area needs to change; blast radius)

**Deliverable**: A comparison matrix with:
* Weighted score totals (weights stated explicitly)
* A short narrative “why” per score (no hand-wavy scoring)
* A sensitivity note: what recommendation changes if weights shift

#### Topic 7: Migration & Operating Model Impacts (`P2`)

**Objective**: Identify what must change operationally if T102 adopts the recommended coordination architecture.

**Specific Questions**:
* What changes are required to authoring workflows (who updates what, when, under which gates)?
* What are the minimum viable changes vs optional enhancements?
* What coordination responsibilities belong in SPS vs Concept vs Request under `T102-STD-001`?

**Deliverable**: A pragmatic migration plan outline (phased), including “do not break” invariants and a delta list for standards/interfaces (recommendations-only).

---

### Part C: Industry Benchmarking (Externally Cited)

#### Topic 8: Industry Practices for Traceability and Cross-Scope Coordination (`P1`)

**Objective**: Benchmark the candidate architecture families against external best practices for requirements traceability and coordination.

**Constraints**:
* Any “industry best practice” claim MUST be externally sourced and cited (no uncited assertions).
* Prefer primary standards/handbooks when feasible (e.g., ISO/IEEE); otherwise reputable secondary sources are acceptable.

**Deliverable**: A short, citation-backed benchmarking section mapping T102’s coordination needs to external practices and highlighting mismatches.

---

## III. CONSTRAINTS, ASSUMPTIONS & METHODOLOGY

### A. Constraints
* **Recommendations-only**: Do not draft STD clause text; do not modify SSOT artifacts in this research.
* **Neutral comparison**: Treat all architecture families with equal comparison rigor (`T102-PH001-ST004-AC002-DEC003`).
* **Citations required**: Externally sourced “industry best practice” claims must be cited.

### B. Assumptions
* `T102-STD-001` is treated as the operating model baseline (it is currently `Proposed`; recommendations must flag dependencies on its stability).
* T102’s governance posture prefers “link-don’t-duplicate” and stable IDs (`T102-STD-003`, `T102-STD-005`, `T102-STD-006`).

### C. Methodology: Hierarchy of Truth (Conflict Resolution)
1. **Standards** (`prompt/artifacts/tasks/T102/consultant/standards/T102-STD-00*.md`) and SSOT artifacts (SPS/Concept/Request) — highest authority.
2. **Plans** (`prompt/artifacts/tasks/T102/consultant/workspace/plan/*.md`) — intended work and gating.
3. **Notes** (`prompt/artifacts/tasks/T102/consultant/workspace/notes/**/*.md`) — consultation evidence summaries.
4. **Raw transcripts** (`prompt/artifacts/tasks/T102/consultant/raw/**/*.txt`) — evidence only; use to corroborate notes, not to override SSOT.

---

## IV. CROSS-TOPIC INTEGRATION

* **Integration Question 1**: If coordination is centralized (Concept hub), how is local context preserved without reintroducing bloat in SPS/Request?
* **Integration Question 2**: How does the chosen coordination architecture affect research indexing governance (`T102-STD-006`) and its drift risk?
* **Integration Question 3**: What coordination responsibilities must remain embedded (minimum viable) even if a centralized or hybrid model is recommended?

---

## V. INPUT PACKET (CONTEXT MAP)

### A. Core Governance
* Stream Plan: `prompt/artifacts/tasks/T102/workspace/PH001/ST004/plan_T102-PH001-ST004.md`
* Activity Notes (scope/amendment evidence): `prompt/artifacts/tasks/T102/workspace/PH001/ST004/AC002/notes_T102-PH001-ST004-AC002.md`
* Raw transcript (evidence): `prompt/artifacts/tasks/T102/workspace/PH001/ST004/AC000/raw/raw_T102-PH001-ST004_AC000_2026-02-09_p1.txt`
* T102-RES-004 analysis and synthesis: `prompt/artifacts/tasks/T102/workspace/PH000/analysis/analysis_T102-RES-004_issues-risks-architecture.md`

### B. Standards (Authoritative Inputs)
* `prompt/artifacts/tasks/T102/standard/standard_T102-STD-001_consultancy-operating-model.md`
* `prompt/artifacts/tasks/T102/standard/standard_T102-STD-003_explicit-inheritance-model.md`
* `prompt/artifacts/tasks/T102/standard/standard_T102-STD-005_id-specification-rules.md` (including `INT` semantics)
* `prompt/artifacts/tasks/T102/standard/standard_T102-STD-006_research-artifacts-index.md` (subtopic)
* `prompt/artifacts/tasks/T102/standard/standard_T102-STD-007_issues-risks-index.md` (report Issues & Risks section schema)

### C. SSOT Artifacts (Primary Evidence)
* SPS: `prompt/artifacts/tasks/T102/ssot/sps_T102-CONSULTANT.md`
  - Focus areas: “Inherited Considerations” patterns, “Research & Notes” patterns, and any `INT`/integration guidance usage.
* Concept: `prompt/artifacts/tasks/T102/ssot/concept_T102-CONSULTANT.md`
  - Focus areas: STD Index, Research Artifacts Register (E.3), and any register hosting patterns.

### D. Exemplars / Adjacent Work
* RES-004 brief (style baseline): `prompt/artifacts/tasks/T102/research/T102-RES-004/brief_T102-RES-004_issues-risks-architecture.md`

### E. Anti-Patterns / Exclusions
* **IGNORE**: `prompt/artifacts/tasks/T102/**/archive/` — do not treat archived artifacts as authoritative exemplars.

---

## VI. DELIVERABLE FORMAT REQUIREMENTS

The research report MUST use the standard template located at:
> `prompt/templates/researcher/template_research_report.md`

**Specific Mapping Instructions for this Brief**:
1. **Section I (Exec Summary)**: State the recommended coordination architecture, the core rationale, and the standards/SSOT responsibilities impacted (recommendations-only).
2. **Topic Findings**:
   * **Topic 1 (Inventory)**: Provide a structured inventory table (surfaces, authority, drift risks).
   * **Topic 2 (STD-003 review)**: Provide compliance findings and an effectiveness/bloat analysis with concrete exemplars.
   * **Topic 6 (Rubric)**: Provide the comparison matrix, weights, and scoring rationale.
   * **Topic 8 (Industry benchmarking)**: Include explicit citations for all external claims.
3. **Completeness**: Do NOT delete empty sections. If a topic has no implications, explicitly state "None".

---

## VII. ISSUES & RISKS REGISTER (T102-STD-007)

The research report MUST include an “Issues & Risks” section that implements `T102-STD-007 (Issues & Risks Index)` exactly.

**Issues**
<!-- GUIDANCE:
Status = `OPEN, IN-REVIEW, RESOLVED, BLOCKED, DEFERRED`,
priority = `HIGH, MEDIUM, LOW`
-->
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Resolution Notes | Resolution Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `T102-RES-005-ISSUE-001` | Rubric fairness | Comparing architecture families may become biased if criteria/weights are adjusted post-hoc | LLM_Consultant | `OPEN` | `MEDIUM` | 2026-02-09 | — | — |

**Risks**
<!-- GUIDANCE:
Status = `OPEN, MONITORED, MITIGATED, ACCEPTED, CLOSED`,
priority = `HIGH, MEDIUM, LOW`
-->
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Mitigation Notes | Mitigation Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `T102-RES-005-RISK-001` | Scope overreach | “Coordination architecture” can expand into unrelated governance refactors; risk of an unfalsifiable brief | LLM_Consultant | `OPEN` | `MEDIUM` | 2026-02-09 | — | — |
| `T102-RES-005-RISK-002` | STD-001 baseline instability | `T102-STD-001` is `Proposed`; recommendations depending on its clauses may require revision if STD-001 changes | LLM_Consultant | `MONITORED` | `LOW` | 2026-02-09 | Flag findings that depend on STD-001 stability; prefer recommendations that are robust to minor operating-model wording shifts | — |
| `T102-RES-005-RISK-003` | Concept overlap | Centralized/hybrid options may overlap with `T102-RES-006` (Concept role + dynamic registers); integration-stage reconciliation may be needed | LLM_Consultant | `OPEN` | `LOW` | 2026-02-09 | — | — |

**ID Rules**
* IDs MUST use the scoped, sequential format: `<SCOPE_ID>-ISSUE-###` and `<SCOPE_ID>-RISK-###` (e.g., `T102-RES-005-ISSUE-001`).
* IDs MUST remain stable once created (no reuse, no renumbering).

---

## VIII. CRITICAL DEPENDENCIES (GOVERNANCE MAPPING)

* **`T102-STD-001`**: Findings must remain compatible with SPS/Request/Concept role boundaries; report must call out any recommended responsibility reallocations explicitly.
* **`T102-STD-003`**: Evaluation includes whether explicit inheritance tables remain the primary coordination mechanism, are narrowed, or are complemented by other surfaces.
* **`T102-STD-005`**: Evaluation includes `INT` viability and directionality constraints/exceptions; recommendations must not create unsafe upstream references.
* **`T102-STD-006`**: Research indexing placement/governance is a required subtopic; recommendations must provide an explicit placement strategy aligned with the chosen coordination architecture.

---

## IX. SUCCESS CRITERIA

* Produces a neutral, multi-approach comparison rubric and applies it consistently.
* Provides a clear recommendation with explicit tradeoffs and sensitivity notes.
* Includes externally cited benchmarking for all “industry best practice” claims.
* Produces a concrete delta list (recommendations-only) for standards/SSOT responsibilities impacted by the recommended coordination architecture.

