---
artifact_type: 'RESEARCH_BRIEF'
initiative_id: 'T102'
research_id: 'T102-RES-004'
version: '1.0.0'
iteration: '1'
date: '2026-02-09'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
---

# RESEARCH BRIEF: Issues & Risks Hosting Architecture (`T102-RES-004`)

## I. EXECUTIVE SUMMARY

**Context**: The T102 initiative currently hosts Issues & Risks (I&R) tables at three scope levels — Initiative (SPS Section 10), Epic (SPS Epic dossier subsections), and Feature (Request artifact Section H) — all conforming to `T102-STD-007` table schemas. However, `T102-STD-007` governs only the **schema and lifecycle enums** of I&R tables; it does not specify the **hosting architecture** (which artifacts should carry I&R sections, how items promote across scopes, or what content filtering rules determine whether an item belongs in I&R vs elsewhere). During the T102B AC002 re-review, the Client and LLM_Consultant identified that Feature-level I&R in Request artifacts creates process noise and governance clutter (Decision D2, `T102B-PH001-ST001-AC002-DEC002`), and elevated the hosting question to initiative-scoped research (Decision D6, `T102B-PH001-ST001-AC002-DEC006`). The disposition of Feature-level I&R in `request_T102B1-RST.md` (currently Section H, classified `[O]`) is blocked pending this research's findings — AC002.1 depends on the outcome of `T102-PH001-ST004-AC001`.

**Objective**: Determine the canonical Issues & Risks hosting architecture across the T102 artifact hierarchy (SPS, Request, Concept, dedicated register) and produce decision-ready recommendations for `T102-STD-007` amendments, cross-scope lifecycle rules, and content filtering criteria.

**Target Deliverable**: A structured research report consumed by `LLM_Consultant` for producing integration recommendations (recommendations-only; no clause-level STD drafting). The report will inform downstream AC002.1 remediation decisions and `T102-STD-007` delta list production.

---

## II. RESEARCH SCOPE & TOPICS

### Part A: Current State Analysis

#### Topic 1: I&R Hosting Inventory Across Scopes (`P1`)

**Objective**: Document the current I&R hosting pattern across all artifact scopes and identify structural inconsistencies.

**Context**: I&R tables exist at three scope levels but with varying population density and utility. The Initiative-level table has 7 issues and 4 risks; Epic-level tables range from 3-8 issues; Feature-level tables have 2 issues and 1 risk (`request_T102B1-RST.md`). No systematic inventory of this hosting pattern exists.

**Specific Questions**:
* Which SSOT artifacts currently host I&R sections, and at which PM scope levels (Initiative, Epic, Feature)?
* What is the population density of I&R items at each scope level (item count, resolution rate, staleness)?
* Are there any I&R items that appear duplicated or semantically overlapping across scope levels?
* Does the Concept artifact currently host any I&R tables? If not, what is the gap rationale?

**Deliverable**: Annotated I&R hosting inventory table with per-scope population metrics and duplication analysis.

#### Topic 2: `T102-STD-007` Gap Analysis (`P1`)

**Objective**: Identify what `T102-STD-007` currently governs vs what architectural decisions remain unspecified.

**Context**: `T102-STD-007` defines 9 clauses covering section naming, table schemas, status/priority enums, ID rules, resolution/mitigation notes requirements, and cross-scope promotion guidance. However, CLAUSE-009 (cross-scope promotion) uses SHOULD language and provides only a single promotion direction (Epic to Initiative). No clauses address hosting placement, content filtering, or lifecycle across more than two scope levels.

**Specific Questions**:
* Which aspects of I&R architecture are already governed by `T102-STD-007` clauses (schema, enums, IDs, notes)?
* Which aspects remain unspecified (placement decisions, content filtering, multi-scope lifecycle, de-duplication enforcement)?
* Does CLAUSE-009's promotion guidance scale to Initiative/Epic/Feature/Story hierarchies, or does it require extension?
* Are there conflicts or ambiguities between `T102-STD-007` and `T102-STD-003` (Explicit Inheritance Model) regarding I&R cross-scope referencing?

**Deliverable**: Gap matrix mapping `T102-STD-007` clauses to architectural questions, with "governed" vs "unspecified" classification per question.

#### Topic 3: Feature-Level I&R Utility Assessment (`P1`)

**Objective**: Evaluate the observed problems with Feature-level I&R hosting that triggered this research commission.

**Context**: Decision D2 (`T102B-PH001-ST001-AC002-DEC002`) removed I&R from Request based on "industry norms" and "LLM behavioral clutter risk." However, this decision has not been implemented — Section H remains in `request_T102B1-RST.md` (classified `[O]`), pending RES-004 findings. The research must evaluate the D2 rationale with evidence rather than assume the conclusion.

**Specific Questions**:
* What are the observed problems with Feature-level I&R in Request artifacts (clutter, LLM context cost, governance overhead)?
* What do industry frameworks (ISO 29148, BABOK v3, SAFe) recommend regarding issues/risks placement in requirements-level documents vs project-level documents?
* Is the `[O]` (Optional) classification for Section H a sufficient mitigation, or does the section's mere presence create authoring overhead and LLM noise even when empty?
* What is the LLM context cost of carrying I&R tables in Feature-level Request artifacts at scale (e.g., 10+ features)?

**Deliverable**: Evidence-based assessment of Feature-level I&R utility with industry benchmarking and LLM context cost analysis.

---

### Part B: Architecture Options Evaluation

#### Topic 4: Hosting Options Comparison Matrix (`P1`)

**Objective**: Evaluate candidate hosting architectures for I&R across the artifact hierarchy.

**Context**: The plan identifies five candidate patterns: (a) SPS-only (Initiative+Epic), (b) SPS+Request (current three-tier), (c) SPS+Concept (Initiative+Epic in SPS; aggregated register in Concept), (d) hybrid with thresholds (Feature I&R only when complexity warrants), (e) dedicated register (standalone I&R artifact). Each pattern has tradeoffs against evaluation criteria.

**Specific Questions**:
* For each candidate pattern, what is the hosting surface (which artifacts carry I&R sections)?
* How does each pattern handle cross-scope promotion and de-duplication?
* What is the maintenance burden of each pattern (number of locations to update, synchronization risk)?
* Which pattern best aligns with the "link-don't-duplicate" principle of `T102-STD-003`?
* Which pattern optimizes LLM context loading for typical consultation workflows (SPS review, Request authoring, Concept decision-making)?

**Deliverable**: Weighted comparison matrix with per-pattern scores against evaluation criteria (see Section IX).

#### Topic 5: Lifecycle & Cross-Scope Promotion Rules (`P2`)

**Objective**: Define lifecycle state transitions and promotion/de-duplication rules for I&R items across scope levels.

**Context**: `T102-STD-007-CLAUSE-009` provides basic promotion guidance (Epic item becomes Initiative-impacting → create Initiative item and close/reference Epic item). This does not address: downward propagation (Initiative risk → Epic-level monitoring tasks), Feature-to-Epic promotion, or multi-scope item staleness detection.

**Specific Questions**:
* What lifecycle transitions are needed beyond the current scope (creation, status changes, cross-scope promotion, archival)?
* Should promotion be unidirectional (upward only) or bidirectional (upward promotion + downward monitoring)?
* How should de-duplication be enforced when the same concern appears at multiple scope levels?
* What staleness detection rules should apply (e.g., items OPEN > 90 days without status change)?

**Deliverable**: Lifecycle state diagram and promotion rules recommendation.

#### Topic 6: Content Filtering Criteria (`P2`)

**Objective**: Define rules for what qualifies as an Issue or Risk vs what belongs in other governance sections (assumptions, constraints, notes, dependencies).

**Context**: Current I&R tables contain items that may overlap with other governance categories — e.g., `T102-ISSUE-001 (Planner Handoff Schema)` could be classified as a dependency or an action item rather than an "issue." No explicit filtering rules exist to guide authors on when to create an I&R item vs when to use another governance surface.

**Specific Questions**:
* What distinguishes an Issue from a dependency, action item, or constraint in the T102 governance model?
* What distinguishes a Risk from an assumption or a noted concern?
* Should filtering rules be prescriptive (mandatory classification criteria) or advisory (guidance with author discretion)?
* How should borderline items be handled (e.g., dual-classification, escalation to Client)?

**Deliverable**: Content filtering decision tree with worked examples from existing T102 I&R inventory.

---

## III. CONSTRAINTS, ASSUMPTIONS & METHODOLOGY

### A. Constraints

* **Boundary**: Research is scoped to T102 initiative artifacts only. No external codebase or API analysis required.
* **STD-001 baseline status**: `T102-STD-001 (Consultancy Operating Model)` is in `Proposed` status and subject to revision based on RES-007 findings. This research treats `T102-STD-001` as a **reference baseline** (current model) rather than an immutable constraint. Recommendations MAY include feedback that feeds into `T102-STD-001` amendments, but the actual amendment is downstream work.
* **Recommendations-only**: Research outputs MUST NOT draft clause-level STD text. Outputs are recommendations and delta lists consumed by downstream integration activities.
* **No implementation**: Research MUST NOT modify SSOT artifacts (SPS, Request, Concept). Changes are executed downstream via AC002.1 and related activities.

### B. Assumptions

* **T102C maturity**: The Concept artifact (`concept_T102-CONSULTANT.md`) is underdeveloped (Section E Registers exist in skeleton form). Evaluating Concept as a hosting candidate is valid, but recommendations must note that T102C maturity is a prerequisite for any Concept-hosted pattern. RES-007 will provide the Concept viability assessment.
* **D2 not implemented**: Decision D2 (`T102B-PH001-ST001-AC002-DEC002` — remove I&R from Request) has NOT been executed. `request_T102B1-RST.md` Section H still contains Feature-level I&R tables. The research evaluates the three-tier hosting as the **current state** without assuming removal.
* **Scale projection**: The T102 initiative currently has 5 Epics and 1 Feature-level Request. Hosting architecture recommendations should account for projected scale (5-10 Features per Epic).

### C. Methodology "Hierarchy of Truth"

1. **SSOT Artifacts** (SPS, Request, Concept) — Highest Authority (current implementation reality)
2. **Standards** (`T102-STD-007`, `T102-STD-003`, `T102-STD-001`) — Secondary Authority (governing intent, noting `Proposed` status)
3. **Consultation Notes** (AC002 notes, D2/D6 decisions) — Tertiary Authority (decision rationale and context)
4. **Industry Standards** (ISO 29148, BABOK v3, SAFe, PRINCE2) — Reference Authority (external benchmarking for best practice claims)

---

## IV. CROSS-TOPIC INTEGRATION

* **Topic 1 → Topic 4**: The current state inventory (Topic 1) provides the baseline against which hosting options (Topic 4) are evaluated. Each option should be assessed as a delta from the current three-tier hosting.
* **Topic 2 → Topic 5**: The `T102-STD-007` gap analysis (Topic 2) identifies which lifecycle/promotion rules are already governed and which require new specification (Topic 5).
* **Topic 3 → Topic 4**: The Feature-level utility assessment (Topic 3) directly informs whether options retaining Feature-level I&R (option b, d) are viable or should be eliminated.
* **Topic 6 → Topic 1**: Content filtering criteria (Topic 6) may reclassify existing I&R items discovered in the inventory (Topic 1), potentially changing population metrics.
* **Interface with `T102-RES-007`**: This research evaluates Concept as an I&R hosting candidate (one register type among several). `T102-RES-007` evaluates Concept's overall role as a dynamic registers surface (I&R being one register type). The overlap zone (I&R in Concept) is intentional; reconciliation occurs at the integration recommendations stage (TK003).

---

## V. INPUT PACKET (CONTEXT MAP)

### A. Core Governance

* SSOT SPS: `prompt/artifacts/tasks/T102/ssot/sps_T102-CONSULTANT.md`
* SSOT Concept: `prompt/artifacts/tasks/T102/ssot/concept_T102-CONSULTANT.md`
* Stream Plan: `prompt/artifacts/tasks/T102/workspace/PH001/ST004/plan_T102-PH001-ST004.md`

### B. Standards (Authoritative)

* `prompt/artifacts/tasks/T102/standard/standard_T102-STD-007_issues-risks-index.md` — Primary standard under evaluation
* `prompt/artifacts/tasks/T102/standard/standard_T102-STD-003_explicit-inheritance-model.md` — Cross-scope referencing model
* `prompt/artifacts/tasks/T102/standard/standard_T102-STD-006_research-artifacts-index.md` — Research governance
* `prompt/artifacts/tasks/T102/standard/standard_T102-STD-001_consultancy-operating-model.md` — Operating model (reference baseline; `Proposed` status)
* `prompt/artifacts/tasks/T102/standard/standard_T102-STD-005_id-specification-rules.md` — ID construction rules

### C. Decision Evidence & Exemplars

* AC002 re-review notes (D2/D6/D7): `prompt/artifacts/tasks/T102/T102B/workspace/PH001/ST001/AC002/notes_T102B-PH001-ST001-AC002.md`
* Initiative-level I&R exemplar: `prompt/artifacts/tasks/T102/ssot/sps_T102-CONSULTANT.md` (Section III.B.10)
* Epic-level I&R exemplars:
  - T102A: `prompt/artifacts/tasks/T102/ssot/sps_T102-CONSULTANT.md` (Section III.C.1.ix)
  - T102B: `prompt/artifacts/tasks/T102/ssot/sps_T102-CONSULTANT.md` (Section III.C.2.x)
  - T102C: `prompt/artifacts/tasks/T102/ssot/sps_T102-CONSULTANT.md` (Section III.C.3.ix)
* Feature-level I&R exemplar: `prompt/artifacts/tasks/T102/T102B/ssot/request_T102B1-RST.md` (Section H)

### D. Anti-Patterns / Exclusions

* **IGNORE**: `prompt/artifacts/tasks/T102/*/archive/` — Do not read archived artifacts.
* **IGNORE**: `prompt/artifacts/tasks/T102/T102B/raw/` — Raw transcripts are not authoritative; use notes summaries only.
* **DO NOT TREAT AS STRUCTURAL EXEMPLAR**: `prompt/artifacts/tasks/T102/T102A/request/request_T102A-SPSST.md` — Per DEC004, this is guidance-only, not a structural model.

---

## VI. DELIVERABLE FORMAT REQUIREMENTS

The research report MUST use the standard template located at:
> `prompt/templates/researcher/template_research_report.md`

**Specific Mapping Instructions for this Brief**:

1. **Section I (Executive Summary)**: Summarize the recommended hosting architecture and its primary rationale in 2-3 sentences. State the recommended `T102-STD-007` delta scope.
2. **Section III (Topic Findings)**:
   * **Topic 1 (Inventory)**: Present as a structured table with per-scope population metrics.
   * **Topic 3 (Feature-Level Utility)**: Include explicit industry standard citations (ISO 29148, BABOK v3, SAFe) for all "best practice" claims.
   * **Topic 4 (Options Matrix)**: Present as a comparison matrix with weighted scores per evaluation criterion.
   * **Topic 5 (Lifecycle)**: Include a lifecycle state diagram (text-based).
   * **Topic 6 (Filtering)**: Include a decision tree with worked examples.
3. **Completeness**: Do NOT delete empty sections. If a topic has no implications, explicitly state "None."

---

## VII. ISSUES & RISKS REGISTER (T102-STD-007)

The research report MUST include an "Issues & Risks" section that implements `T102-STD-007 (Issues & Risks Index)` exactly.

**Issues**
<!-- GUIDANCE:
Status = `OPEN, IN-REVIEW, RESOLVED, BLOCKED, DEFERRED`,
priority = `Low, Medium, High`
-->
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Resolution Notes | Resolution Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

**Risks**
<!-- GUIDANCE:
Status = `OPEN, MONITORED, MITIGATED, ACCEPTED, CLOSED`,
priority = `Low, Medium, High`
-->
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Mitigation Notes | Mitigation Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `T102-RES-004-RISK-001` | RES-007 dependency | Concept hosting candidate evaluation depends on RES-007 viability findings; if RES-007 is delayed, Concept-related recommendations may be provisional | LLM_Consultant | `OPEN` | `MEDIUM` | 2026-02-09 | — | — |
| `T102-RES-004-RISK-002` | STD-001 baseline instability | `T102-STD-001` is in `Proposed` status; recommendations referencing operating model clauses may require revision if STD-001 changes | LLM_Consultant | `MONITORED` | `LOW` | 2026-02-09 | Treat STD-001 as reference baseline, not immutable constraint; flag recommendations that depend on STD-001 stability | — |

**ID Rules**
* IDs MUST use the scoped, sequential format: `<SCOPE_ID>-ISSUE-###` and `<SCOPE_ID>-RISK-###` (e.g., `T102-RES-004-ISSUE-001`).
* IDs MUST remain stable once created (no reuse, no renumbering).

---

## VIII. CRITICAL DEPENDENCIES (E-RID MAPPING)

* **`T102-STD-007`**: Topics 1, 2, 4, 5, 6 findings will define the delta list (new clauses or amended clauses) for hosting architecture, lifecycle rules, and content filtering.
* **`T102-STD-003`**: Topic 4 findings will clarify interface implications for cross-scope I&R referencing under the Explicit Inheritance Model.
* **`T102-STD-006`**: Topic 4 findings may surface interface implications if I&R registers are collocated with Research registers in Concept Section E.
* **`T102B-PH001-ST001-AC002.1`**: The recommended hosting option directly governs whether Feature-level I&R (Request Section H) is retained, removed, or made conditional — unblocking AC002.1 remediation.
* **`T102-RES-007`**: Overlap zone (I&R in Concept) requires reconciliation at integration recommendations stage.

---

## IX. SUCCESS CRITERIA

* All six Topics have findings with evidence citations (no unsupported assertions).
* Hosting options comparison matrix includes at least 4 candidate patterns scored against evaluation criteria.
* Evaluation criteria are weighted equally: (1) LLM context cost, (2) scanability/readability, (3) governance traceability, (4) maintenance burden, (5) cross-scope promotion clarity.
* All "industry best practice" claims cite external sources (ISO 29148, BABOK v3, SAFe, PRINCE2, or equivalent).
* `T102-STD-007` delta list is explicit (which clauses need amendment, which new clauses are recommended).
* Interface with `T102-RES-007` is explicitly bounded (what RES-004 covers vs what defers to RES-007).
* Feature-level I&R disposition recommendation is actionable for AC002.1 (clear retain/remove/conditional verdict with rationale).
