---
artifact_type: 'RESEARCH_BRIEF'
initiative_id: 'T102'
research_id: 'T102-RES-006'
version: '2.0.0'
iteration: '2'
date: '2026-02-10'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
---

# RESEARCH BRIEF: Concept Role + Dynamic SSOT Registers (`T102-RES-006`)

## I. EXECUTIVE SUMMARY

**Context**: The `concept_T102-CONSULTANT.md` artifact has evolved beyond a pure “ADR compendium” into a candidate **initiative bridge / process manual** and **dynamic register surface** that can reduce SPS/Request bloat, improve cross-scope coordination, and provide stable navigation across standards, decisions, and work products. However, the current operating-model standard (`T102-STD-001`) still frames Concept primarily as an Architecture Description Document (ADD) / ADR compendium, creating an explicit mismatch between (a) intended use and (b) governed responsibilities. This research commission is required to clarify Concept’s authoritative role, define which register families belong there (and which do not), and produce decision-ready recommendations for operating-model and SSOT interface impacts.

**Dependency resolution (v2.0.0)**: Both upstream research dependencies are now resolved. `T102-RES-004` (Issues & Risks Architecture) recommends SPS-only I&R hosting as the **baseline** architecture, with Concept aggregation (pattern c) preserved as a **conditional enhancement** pending this research's viability verdict. `T102-RES-005` (Cross-Scope Coordination Architecture) recommends a **hybrid coordination architecture** — embedded minimum viable (STD-003) + centralized audit surface (Concept registers) + transient INT layer — which positions Concept as the initiative's coordination audit surface. These findings establish firm architectural inputs for this research rather than conditional assumptions.

**Objective**: Define the recommended Concept role and governance boundaries as a **dynamic SSOT registers hub** (including standards/decision indexing surfaces), evaluate multiple architecture options using a weighted rubric, and produce a delta-ready recommendations package for operating-model alignment (recommendations-only; no clause drafting).

**Target Deliverable**: A research report that (1) inventories current Concept/SPS coordination surfaces, (2) evaluates 3–5 alternative Concept architectures, and (3) recommends a Concept role model + register-family placement conventions (including conditional candidates), with explicit impacts mapped to `T102-STD-001`, `T102-STD-005`, `T102-STD-006`, and `T102-STD-007`.

The report must specifically evaluate Concept's viability as the coordination audit surface recommended by RES-005 and as the I&R aggregation surface conditionally deferred by RES-004 (pattern c).

---

## II. RESEARCH SCOPE & TOPICS

### Part A: Current State Inventory (Concept + SPS evidence) (`P1`)

#### Topic 1: Concept Inventory & Drift Audit (`P1`)
**Objective**: Establish the current Concept shape and determine what is “real” vs placeholder.
**Context**: Concept contains live indexes/registers (e.g., standards index, design register, research register) but also has placeholder sections. Without a current-state inventory, proposed Concept role changes risk circular reasoning.
**Specific Questions**:
* What sections are currently populated and used as SSOT navigation (STD index, research register, design register, etc.) vs placeholder/comment blocks?
* What existing sections already function as “dynamic registers surface” (even if not governed as such)?
* What known tooling/anchor dependencies exist (e.g., ADR extraction scripts) that could be impacted by restructuring?
* **[RES-005 Directive 4 — Drift detection]**: Can Concept host drift detection indicators (schema drift signals per RES-005 Finding 2, link integrity status per RES-005 Finding 4, staleness indicators per RES-004 Finding 1) as a register-level feature? What is the governance cost of maintaining drift detection in Concept vs relying on gate-time manual checks?
**Deliverable**: A current-state inventory table with: section/register name, location anchor, authority intent (normative vs informative), population status (active/placeholder), and known failure modes (drift, bloat, broken anchors).

#### Topic 2: SPS/Request “Bloat Drivers” and Candidate Offload Surfaces (`P1`)
**Objective**: Characterize where coordination noise and duplication occur today, and which parts are best handled by Concept.
**Context**: Multiple commissioned research topics touch Concept (RES-004 I&R hosting; RES-005 coordination architecture). RES-006 must isolate the Concept-specific residual decision space without duplicating those reports.
**Specific Questions**:
* What recurring coordination patterns exist in SPS (e.g., repeated registers, repeated narrative reminders, repeated inheritance scaffolding) that could be moved to an index/register model?
* Which “register-like” content is currently embedded in SPS/Request but would be better as (a) a Concept register, (b) a dedicated external register artifact, or (c) left in place?
* What is the LLM context cost and scanability cost of leaving these surfaces distributed?
**Deliverable**: A bloat-driver taxonomy with at least 5 concrete exemplars and a recommended “offload candidate” list (Concept vs other).

---

### Part B: Concept Role Model + Authority Boundaries (`P1`)

#### Topic 3: Concept Role Model (Process Manual + Hub) vs Alternatives (`P1`)
**Objective**: Define candidate role models for Concept and their authority boundaries.
**Context**: Consultation direction frames Concept as an initiative bridge analogous to an “AGENTS.md” for the initiative, but with structured registers and indexes. RES-005 further establishes that Concept should serve as the initiative's **coordination audit surface** — hosting cross-scope inventories, register aggregations, and drift detection indexes — within a hybrid coordination architecture (Finding 5, scored 27/35). This role is not fully aligned with `T102-STD-001-CLAUSE-003` (which frames Concept as ADD/ADR compendium) and requires an explicit operating-model compatibility recommendation. The evaluation must treat "coordination audit surface" as a first-class role component alongside the existing "process manual / bridge" framing.
**Specific Questions**:
* What does “process manual / initiative bridge / coordination audit surface” mean operationally: what is authoritative, what is informative, and what is strictly excluded?
* **[RES-005 Directive 1 — Audit surface role]**: How should Concept be framed given RES-005's hybrid coordination recommendation: (a) ADR/ADD-first with coordination registers as secondary, (b) hub-first with indexes + selected registers + coordination audit surface as co-primary, (c) index-only navigation surface (evaluate whether this is still viable given the audit surface requirement)?
* What is the minimal viable Concept role that fulfills both the "process manual / bridge" function AND the "coordination audit surface" function recommended by RES-005?
**Deliverable**: A role model definition with explicit authority tiers and a “what belongs / does not belong” boundary list.

#### Topic 4: Standards + Decisions Surface: “STD Compendium” and Indexing Conventions (`P1`)
**Objective**: Establish how standards and decision records are indexed and surfaced through Concept, consistent with `T102-STD-005`.
**Context**: In T102, decisions may be nested inside standards (STD-nested ADR annexes). The Concept surface therefore behaves as a standards/decisions navigation hub, not merely an ADR compendium.
**Specific Questions**:
* What is the canonical indexing strategy for: STD items, STD clauses, and nested decision record annexes (STD-ADR-###), and how should Concept present them?
* Where should canonical bodies live (Concept vs dedicated `standards/` files), and what “link-don’t-duplicate” rules apply?
* What is the recommended “minimum indexing surface” in Concept: Initiative STD index only, plus optional Epic/Feature STD indexes?
**Deliverable**: A recommended indexing convention package (tables + authoring rules) expressed as recommendations-only (no clause drafting), with compatibility notes for existing tables in Concept.

---

### Part C: Dynamic Register Families (evaluate, then recommend boundaries) (`P1` / `P2`)

**RES-005 Directive 2 context**: Each register family evaluated in Topics 5-9 MUST address how Concept-hosted registers interact with (a) embedded minimum viable snapshots in SPS/Request — the "local emphasis" boundary from RES-005 Delta A3, and (b) INT coordination guidance — the "promotion loop" boundary from RES-005 Delta C1. This ensures register-level recommendations are compatible with the accepted hybrid coordination architecture.

#### Topic 5: Workscope + File Registers (Navigation & Discovery) (`P1`)
**Objective**: Evaluate Concept as the place for “what exists” registers that support onboarding and context injection.
**Context**: Consultation direction includes workscope/file registers and directory outlines as candidate Concept content.
**Specific Questions**:
* What is the minimal register set needed (workscope register, file register, directory outline), and how should it be structured to stay maintainable?
* What belongs here vs in SPS vs in Plan artifacts?
* What update cadence and ownership rules minimize drift? Should workscope/file registers include drift detection columns (last-verified date, link integrity status) as recommended by RES-005's drift detection analysis?
**Deliverable**: A recommended register schema (table columns + example rows) and governance rules (update triggers, ownership, drift detection).

#### Topic 6: Research Registers (Interface with `T102-STD-006`) (`P1`)
**Objective**: Confirm how research artifacts should be indexed/aggregated in Concept and how that interacts with the broader Concept role.
**Context**: `T102-STD-006` defines a dual-index architecture (SPS local tables + Concept aggregation register). RES-006 should validate whether this remains fit-for-purpose as Concept expands.
**Specific Questions**:
* Does the `T102-STD-006` dual-index rule remain optimal under the recommended Concept role model?
* Are there governance/maintenance changes required (ownership, sync cadence, source links) to prevent drift?
* Should Concept be the authoritative research registry while SPS remains a contextual mirror, or vice versa?
**Deliverable**: Recommendations for research register placement conventions and maintenance protocol deltas (recommendations-only; no clause drafting).

#### Topic 7: Issues & Risks Registers in Concept (Conditional Candidate) (`P1`)
**Objective**: Evaluate whether Issues & Risks should be hosted/aggregated in Concept as a register family.
**Context**: `T102-RES-004` evaluates I&R hosting architecture and flags “I&R in Concept” as conditional on Concept-role viability; RES-006 must preserve that conditionality.
**Specific Questions**:
* **[RES-004 Directive 1 — Pattern (c) viability]**: RES-004 defers Concept I&R aggregation (pattern c, scored 19/25 equal to baseline pattern a) to this research. Evaluate whether Concept can serve as an I&R aggregation/dashboard surface: what would the structural design look like (cross-scope summary view, staleness indicators, promotion trails, cross-epic aggregation), what governance rules would apply, and what are the trade-offs vs SPS-only hosting (pattern a)?
* **[RES-004 Directive 3 — STD-007 interaction]**: If pattern (c) is adopted, what `T102-STD-007` amendment language is needed to define how Concept aggregation interacts with SPS canonical hosting? Specifically: how does a Concept aggregation layer satisfy the "must be available for each scope" reading of STD-007-CLAUSE-001 without violating `T102-STD-003` directionality? (Ref: RES-004 Topic 2 governance implication.)
* **[RES-004 Directive 4 — Staleness dashboard feasibility]**: Can Concept provide the cross-scope staleness visibility that RES-004 identified as needed (Finding 1: 98-128 day stale items across Initiative/Epic levels; Finding 5: proposed 90-day staleness threshold in CLAUSE-011)? What is the maintenance cost of a Concept-hosted staleness dashboard vs a purely SPS-based staleness review cadence?
* What are the conditional gating recommendations: under what initiative maturity or scale thresholds should Concept I&R aggregation be adopted vs deferred?
**Deliverable**: A viability verdict for I&R in Concept with structural design recommendations. The verdict MUST include: (a) an explicit GO/NO-GO/CONDITIONAL recommendation tied to RES-004 and RES-005 outcomes, (b) if GO: a register family placement recommendation — where I&R sits relative to other register families (STD indexes, research registers, workscope registers) and whether I&R aggregation is a separate Concept section or part of a unified register surface [RES-004 Directive 2], (c) if NO-GO: explicit rationale and what would need to change for viability.

#### Topic 8: Initiative Overview Assets (Diagrams, Directory Outlines) (`P2`)
**Objective**: Evaluate whether Concept should host high-level system diagrams and overview assets.
**Context**: Consultation direction includes “initiative-level system diagram” and directory outlines as core onboarding aids, but these assets can bloat Concept if not governed.
**Specific Questions**:
* Which asset types are allowed (system context diagram, high-level component diagram, directory outline), and what are the minimum viable forms (e.g., text-based diagrams, links)?
* What is the governance rule to prevent “diagram sprawl”?
* How do these assets align with scanability and LLM context constraints?
**Deliverable**: A governance rubric for including overview assets (when to include, acceptable formats, update triggers, ownership).

#### Topic 9: PM Link Surfaces (Plans/Roadmaps pointers) (`P2`)
**Objective**: Decide how Concept should link to planning/roadmap artifacts without collapsing artifact boundaries.
**Context**: Concept as initiative bridge may point to `plan/` and `roadmap/` artifacts, but those remain non-normative execution surfaces.
**Specific Questions**:
* What “pointers-only” pattern should be used to link plans/roadmaps without making Concept a planning log?
* What is the boundary between Concept’s readiness/handoff snapshots (if any) and Plan artifacts?
**Deliverable**: A recommended linking convention: where links live, what metadata is allowed, and explicit non-goals.

---

### Part D: Architecture Options + Recommendation (weighted rubric required) (`P1`)

#### Topic 10: Options Matrix (3–5 architectures) + Weighted Rubric (`P1`)
**Objective**: Produce a decision-ready comparison of Concept architectures and recommend a target role model.
**Context**: Prior coordination and hosting decisions (RES-004, RES-005) may materially change the best Concept architecture; this brief requires a neutral comparison rather than a foregone conclusion.
**Specific Questions**:
* What are the viable Concept architecture families?
  - (a) Index-only navigation surface
  - (b) Hub + indexes + selected registers (research + design + workscope/file)
  - (c) Hub + expanded registers (adds conditional I&R + overview assets + readiness/handoff snapshots)
  - (d) Dedicated registers (separate artifacts) with Concept as index/hub
  - (e) Hybrid thresholds (register families only when scale/complexity triggers apply)
* Which architecture best balances: scanability/readability, drift risk, governance authority clarity, LLM context cost, and maintenance burden?
* **[RES-005 Directive 3 — STD-001 deltas]**: RES-005 proposes STD-001 amendments: Delta D1 (Concept = ADD + coordination audit surface) and Delta D2 (coordination responsibilities mapping: SPS/Request = embedded minimum viable; Concept = cross-scope registers/inventories; INT = transient coordination). Should RES-006 (a) absorb and refine D1/D2 into a more comprehensive Concept role specification with register-level detail, or (b) confirm D1/D2 as-is and limit RES-006 STD-001 recommendations to register-family governance only? What additional `T102-STD-001` changes are required beyond D1/D2?
**Deliverable**: A weighted comparison matrix (scores + weight rationale) plus an explicit recommendation and consequences.

---

## III. CONSTRAINTS, ASSUMPTIONS & METHODOLOGY

### A. Constraints
* **Recommendations-only**: Do not draft clause-level STD text; produce deltas and recommendations.
* **Resolved dependencies (finalized brief)**: RES-004 and RES-005 reports are accepted and their integration analyses are treated as authoritative inputs. Specific ingestion directives from both analyses are incorporated into Topic-level scope (see Section IV). Recommendations that extend beyond resolved inputs MUST be explicitly flagged as RES-006-originated proposals.
* **GATE-001B finalization inputs**: The finalized brief requires both `analysis_T102-RES-004_issues-risks-architecture.md` (v1.1.0) and `analysis_T102-RES-005_cross-scope-coordination-architecture.md` (v1.0.0) as accepted dependency inputs. These are listed in Section V.D.
* **Link-don’t-duplicate**: Recommendations must preserve the non-duplication intent of cross-scope governance (`T102-STD-003`, `T102-STD-006`, `T102-STD-007`).
* **Directionality discipline**: Avoid architectures that implicitly require prohibited upstream-to-downstream references; explicitly use allowed exceptions only when governed (`T102-STD-005`).

### B. Assumptions (first-draft brief)
* **Concept role update likely required**: The recommended Concept role is expected to require an explicit alignment update to `T102-STD-001-CLAUSE-003` (recommendations-only; no drafting in this stream).
* **STD/decision indexing is core**: Concept will be evaluated as a standards/decisions navigation surface (STD compendium + indexes), not solely as an ADR compendium.
* **I&R in Concept is a viable candidate**: RES-004 recommends SPS-only I&R hosting as the baseline (pattern a), with Concept aggregation (pattern c) deferred as a conditional enhancement pending this research. RES-005 recommends Concept as the coordination audit surface in a hybrid architecture. Together, these establish I&R aggregation in Concept as a **viable candidate to be evaluated** — not merely a theoretical possibility. This research must produce a definitive viability verdict with structural design recommendations if viable.

### C. Methodology “Hierarchy of Truth”
Define how to resolve conflicts between sources:
1. **SSOT Artifacts** (`prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md`, `prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md`) — Highest authority for observed current-state behavior.
2. **Standards** (`prompt/artifacts/tasks/T102/consultant/standards/T102-STD-001_...`, `T102-STD-005`, `T102-STD-006`, `T102-STD-007`) — Normative constraints for role boundaries, IDs, and register schemas.
3. **Commissioned research outputs** (RES-004 report; RES-005 report when available) — Evidence and recommendations; do not silently override standards.
4. **Workspace notes + raw transcripts** — Evidence of intent and rationale; not normative for structure.

---

## IV. CROSS-TOPIC INTEGRATION

* **Integration Question 1 (from RES-005)**: Given the accepted hybrid coordination architecture (embedded minimum viable + Concept as centralized audit surface + transient INT), what is the minimum Concept register surface needed to fulfill the audit surface role without recreating bloat? How do Concept-hosted registers interact with (a) embedded minimum viable snapshots in SPS/Request (the "local emphasis" boundary from RES-005 Delta A3) and (b) INT coordination guidance (the "promotion loop" boundary from RES-005 Delta C1)?
* **Integration Question 2 (from RES-004)**: Given RES-004's SPS-only default I&R hosting, under what conditions does Concept provide I&R aggregation value beyond what SPS already delivers? What is the structural design for a Concept I&R aggregation layer (cross-scope summary view, staleness indicators, promotion trails, cross-epic aggregation) that adds value without duplicating SPS canonical data?
* **Integration Question 3 (dual-index coherence)**: How should the recommended Concept role avoid breaking the `T102-STD-006` dual-index research governance while still reducing SPS clutter? RES-005 identifies broken versioned filename references in Concept E.3 as a concrete drift failure — how does the recommended Concept role model prevent this class of failure across all register families?
* **Integration Question 4 (STD-001 coordination)**: RES-005 proposes STD-001 amendments (Deltas D1-D2) for Concept coordination role and responsibility mapping. Should RES-006 absorb and refine these into a comprehensive Concept role specification, or confirm them as-is if the coordination audit surface role is straightforward?

---

## V. INPUT PACKET (CONTEXT MAP)

### A. Core Governance
* Stream plan (gates + dependency model): `prompt/artifacts/tasks/T102/consultant/workspace/plan/plan_T102-PH001-ST004.md`
* Activity notes (evidence continuity): `prompt/artifacts/tasks/T102/consultant/workspace/notes/PH001/ST004/notes_T102-PH001-ST004-AC003.md`
* Evidence transcript (non-normative intent): `prompt/artifacts/tasks/T102/consultant/raw/PH001/ST004/raw_T102-PH001-ST004_AC000_2026-02-09_p1.txt`

### B. SSOT Artifacts (Authoritative Evidence)
* Concept: `prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md`
* SPS: `prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md`

### C. Standards (Authoritative Constraints)
* `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-001_consultancy-operating-model.md`
* `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-005_id-specification-rules.md`
* `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-006_research-artifacts-index.md`
* `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-007_issues-risks-index.md`

### D. Adjacent Research (Authoritative Dependency Inputs)
* RES-004 report: `prompt/artifacts/tasks/T102/consultant/research/report/report_T102-RES-004_issues-risks-architecture.md` v1.0.0
* RES-004 integration analysis: `prompt/artifacts/tasks/T102/consultant/workspace/analysis/analysis_T102-RES-004_issues-risks-architecture.md` v1.1.0 (Section VI: AC003 Brief Ingestion Directive — 4 points)
* RES-005 report: `prompt/artifacts/tasks/T102/consultant/research/report/report_T102-RES-005_cross-scope-coordination-architecture.md` v1.0.0
* RES-005 integration analysis: `prompt/artifacts/tasks/T102/consultant/workspace/analysis/analysis_T102-RES-005_cross-scope-coordination-architecture.md` v1.0.0 (Section V.B: AC003 Brief Ingestion Directive — 4 points)
* RES-005 brief (structural reference): `prompt/artifacts/tasks/T102/consultant/research/brief/brief_T102-RES-005_cross-scope-coordination-architecture.md` v1.0.0

### E. Anti-Patterns / Exclusions
* **IGNORE**: `prompt/artifacts/tasks/T102/**/archive/` — do not treat archived artifacts as authoritative exemplars.

---

## VI. DELIVERABLE FORMAT REQUIREMENTS

The research report MUST use the standard template located at:
> `prompt/templates/researcher/template_research_report.md`

**Specific Mapping Instructions for this Brief**:
1. **Section I (Exec Summary)**: State the recommended Concept role model and register-family placement approach, plus explicit operating-model alignment impacts (recommendations-only).
2. **Section III (Topic Findings)**:
   * **Topic 1 (Inventory)**: Provide the current-state inventory table (what exists vs placeholder) with drift/tooling notes.
   * **Topic 4 (STD/decision surface)**: Provide recommended indexing conventions for STD/CLAUSE/STD-ADR annexes, consistent with `T102-STD-005`.
   * **Topic 10 (Options Matrix)**: Provide the weighted rubric, scoring, and rationale; include at least 3 architectures and explicitly call out conditional dependencies.
   * **Topic 7 (I&R in Concept)**: Provide a definitive viability verdict with structural design recommendations. The verdict must be informed by resolved RES-004 inputs (SPS-only baseline, pattern c deferral) and RES-005 inputs (hybrid coordination, Concept as audit surface). Include register-family placement recommendation if GO.
3. **External claims**: Any “industry best practice” claims MUST be externally sourced and cited in the report.
4. **Completeness**: Do NOT delete empty sections. If a topic has no implications, explicitly state "None."

---

## VII. ISSUES & RISKS REGISTER (T102-STD-007)

The research report MUST include an “Issues & Risks” section that implements `T102-STD-007 (Issues & Risks Index)` exactly.

**Issues**
<!-- GUIDANCE:
Status = `OPEN, IN-REVIEW, RESOLVED, BLOCKED, DEFERRED`,
priority = `HIGH, MEDIUM, LOW`
-->
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Resolution Notes |Resolution Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `T102-RES-006-ISSUE-001` | ADR extraction tooling | ADR-print scripts fail due to missing Concept anchors; may reduce ability to mechanically validate I&R/ID rules during research | LLM_Consultant | `OPEN` | `MEDIUM` | 2026-02-09 | — | — |
| `T102-RES-006-ISSUE-002` | Scope overlap risk | RES-006 touches Concept implications also discussed in RES-004/RES-005; boundaries now clarified by ingestion directives but researcher must avoid re-evaluating settled decisions (SPS-only I&R baseline from RES-004; hybrid coordination architecture from RES-005) | LLM_Consultant | `OPEN` | `LOW` | 2026-02-09 | Boundaries clarified via 8 ingestion directive points absorbed into brief v2.0.0; priority downgraded from MEDIUM to LOW | — |

**Risks**
<!-- GUIDANCE:
Status = `OPEN, MONITORED, MITIGATED, ACCEPTED, CLOSED`,
priority = `HIGH, MEDIUM, LOW`
-->
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Mitigation Notes |Mitigation Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `T102-RES-006-RISK-001` | Unfalsifiable Concept hub | “Process manual” framing may expand scope beyond decision-ready evaluation, producing an unfalsifiable report | LLM_Consultant | `OPEN` | `MEDIUM` | 2026-02-09 | — | — |
| `T102-RES-006-RISK-002` | Dependency churn | RES-006 conclusions may change materially after RES-005 coordination architecture recommendations, forcing re-scope at GATE-001B | LLM_Consultant | `CLOSED` | `LOW` | 2026-02-09 | RES-004 and RES-005 reports accepted; integration analyses produced; all conditional boundaries resolved in brief v2.0.0 | 2026-02-10 |

**ID Rules**
* IDs MUST use the scoped, sequential format: `<SCOPE_ID>-ISSUE-###` and `<SCOPE_ID>-RISK-###` (e.g., `T102-RES-006-ISSUE-001`).
* IDs MUST remain stable once created (no reuse, no renumbering).

---

## VIII. CRITICAL DEPENDENCIES (GOVERNANCE MAPPING)

* **`T102-STD-001`**: Findings will determine whether `T102-STD-001-CLAUSE-003` requires an update to reflect Concept as a dynamic registers hub (recommendations-only).
* **`T102-STD-005`**: Findings will define indexing conventions for STD/CLAUSE/STD-ADR annexes and ensure register schemas respect ID directionality and category semantics.
* **`T102-STD-006`**: Findings may recommend adjustments to dual-index governance if Concept’s register scope expands.
* **`T102-STD-007`**: Conditional: if I&R is recommended to aggregate/host in Concept, findings must remain compatible with I&R schema, closure coupling rules, and cross-scope promotion guidance.
* **`T102-RES-004`**: Resolved input: SPS-only I&R hosting as baseline; pattern (c) Concept aggregation deferred to this research for viability verdict. Ingestion directives (4 points) absorbed into Topics 7, 8, and 10.
* **`T102-RES-005`**: Resolved input: hybrid coordination architecture with Concept as coordination audit surface. Ingestion directives (4 points) absorbed into Topics 1, 3, 5, and 10. STD-001 Deltas D1-D2 to be absorbed or refined.

---

## IX. SUCCESS CRITERIA

* Brief is approval-ready for `T102-PH001-ST004-AC003-GATE-001B` (finalized brief), with all conditional boundaries from v1.0.0 resolved using accepted RES-004 and RES-005 integration analyses.
* Brief requires a weighted options matrix (3-5 architectures) and a clear recommendation (not merely an inventory); all 5 candidate architectures from v1.0.0 are retained for neutral evaluation.
* Brief explicitly includes operating-model alignment analysis (`T102-STD-001`) as a required output, incorporating RES-005 Deltas D1-D2 as inputs to be absorbed or refined.
* I&R in Concept is evaluated as an explicit viable candidate with resolved inputs from RES-004 (SPS-only default + pattern c deferral) and RES-005 (hybrid coordination + Concept as audit surface).
* All 8 ingestion directive points (4 from RES-004 analysis Section VI, 4 from RES-005 analysis Section V.B) are traceable to specific Topic-level scope items.
