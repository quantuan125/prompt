---
artifact_type: 'BRIEF'
initiative_id: 'P'
research_id: 'P-RES-001'
version: '1.0.0'
iteration: '1'
date: '2026-02-24'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
---

# RESEARCH BRIEF: Status Standard Research (P-RES-001)

## I. EXECUTIVE SUMMARY

**Context**: `P-STD-002` (Program Status Standard) is planned as a broad-scope program-wide governance standard covering status vocabulary, health assessment, dependency visibility, evidence linkage, update protocol, and status artifact specification. An informal working note exists (`analysis_P-PH000-ST002_status-system-research.md`) proposing a dual-layer architecture (PSL + PSN), a 7-state enum, and an operating protocol — but all claims are internally reasoned without external benchmarking. Formal research is commissioned to produce an externally sourced evidence base that validates or challenges the current working model and provides decision-ready findings for P-STD-002 CLAUSE authoring.

**Objective**: Produce a decision-ready research report that benchmarks industry-standard program status governance patterns across 5 domains (status vocabulary, health assessment, dependency visibility, update protocol, status artifact specification) and delivers scored recommendations for each domain using a weighted evaluation rubric per `T102-STD-006-CLAUSE-008`.

**Target Deliverable**: Research report consumed by `P-PH000-ST001-AC003` (Author P-STD-002). Consumer: LLM_Consultant.

## II. RESEARCH SCOPE & TOPICS

### Part A: Status Vocabulary & Transition Governance

#### Topic 1: Industry Status Enum Benchmarking (Critical)
**Objective**: Benchmark canonical status enum sets used in mature program/project management frameworks and tooling.
**Context**: The current working model proposes a 7-state set (`planned`, `ready`, `in_progress`, `blocked`, `on_hold`, `completed`, `cancelled`). This has not been validated against external frameworks.
**Specific Questions**:
*   What canonical status enum sets do PMI/PMBOK 7, SAFe, PRINCE2, Azure DevOps, and Jira use for work item tracking at program and project levels?
*   How do these frameworks organize states into meta-categories (e.g., Proposed, InProgress, Resolved, Completed)?
*   Does the proposed 7-state set align with industry consensus, or are states missing or redundant?
*   How do frameworks distinguish between `blocked` (external impediment) and `on_hold` (deliberate suspension)?
**Deliverable**: Comparative matrix of enum sets across frameworks with gap analysis against the proposed 7-state set. Scored comparison per evaluation rubric (Section III.D).

#### Topic 2: State Machine Transition Rules (Critical)
**Objective**: Evaluate state machine transition rule patterns and guard conditions for program status governance.
**Context**: The proposed enum set lacks defined transition rules — which states can transition to which, and under what conditions.
**Specific Questions**:
*   What transition rule patterns do industry frameworks enforce (e.g., linear progression, selective backflow, terminal-state restrictions)?
*   What guard conditions are typically required for high-impact transitions (e.g., `in_progress` → `completed`, any state → `cancelled`)?
*   How do frameworks handle re-activation from terminal states (e.g., `completed` → `in_progress` for rework)?
*   Should transition rules differ by hierarchy level (program vs. initiative vs. activity)?
**Deliverable**: Recommended transition matrix with guard condition patterns for each transition.

### Part B: Health & RAG Assessment

#### Topic 3: RAG Threshold Frameworks (High)
**Objective**: Evaluate RAG (Red/Amber/Green) threshold frameworks and tolerance models for program health assessment.
**Context**: RAG assessment is widely used but threshold definitions vary. Without explicit thresholds, RAG becomes subjective. The seed analysis proposed tolerance-based thresholds but did not specify computation rules.
**Specific Questions**:
*   What threshold models do major frameworks use (quantitative percentage-based, qualitative rule-based, hybrid)?
*   How are tolerance bands defined (e.g., Green = 0-10% variance, Amber = 10-25%, Red = >25%)?
*   What dimensions are typically assessed (schedule, scope, quality, resource, risk)?
*   How do frameworks handle RAG override or escalation (e.g., a single Red dimension overrides overall status)?
**Deliverable**: Recommended threshold model with dimension definitions and escalation rules. Scored comparison per evaluation rubric (Section III.D).

#### Topic 4: Health Assessment Dimensions (High)
**Objective**: Evaluate which health assessment dimensions are standard for program-level governance.
**Context**: The seed analysis references health as a single field (`green`/`amber`/`red`). Industry frameworks typically disaggregate into multiple dimensions.
**Specific Questions**:
*   What is the industry-standard set of health dimensions for program-level tracking?
*   How are dimension-level assessments aggregated into an overall program health indicator?
*   Should dimensions be fixed (standard set) or configurable per initiative?
**Deliverable**: Recommended dimension set with aggregation rules.

### Part C: Dependency Visibility

#### Topic 5: Dependency Typing Schemas (Critical)
**Objective**: Evaluate dependency typing and categorization schemas for program-level dependency tracking.
**Context**: The working model proposes a unified schema using FS/SS/FF/SF typing with categorization (mandatory/resource/discretionary/external/cross-team). This needs external validation.
**Specific Questions**:
*   What dependency typing schemas do PMI/PMBOK, SAFe, and enterprise tooling use (FS/SS/FF/SF, lead/lag, mandatory vs. discretionary)?
*   What categorization taxonomies are standard (resource, technical, regulatory, cross-team)?
*   How are dependencies represented in machine-readable formats (adjacency lists, dependency matrices, inline metadata)?
*   What risk-level classification is applied to dependencies (critical path, near-critical, non-critical)?
**Deliverable**: Recommended dependency schema with typing, categorization, and representation format options. Scored comparison per evaluation rubric (Section III.D).

#### Topic 6: Cross-Initiative Dependency Models (High)
**Objective**: Evaluate how program-level dependency tracking relates to initiative-level dependencies.
**Context**: Program governance requires unified dependency visibility across initiatives. It is unclear whether P-STD-002 should mandate a single schema that all initiatives adopt, or define a program-level interface that initiatives surface dependencies into.
**Specific Questions**:
*   How do enterprise frameworks (SAFe Program Board, PRINCE2 Stage Plans) handle cross-team/cross-initiative dependency surfacing?
*   Is a unified schema or an interface-contract model more effective for multi-initiative programs?
*   What minimum dependency metadata must be surfaced at program level for effective orchestration?
**Deliverable**: Recommended model for cross-initiative dependency governance with trade-off analysis.

### Part D: Update Protocol & Evidence Governance

#### Topic 7: Evidence Linkage Patterns (Critical)
**Objective**: Evaluate evidence linkage patterns for status transitions, particularly terminal states.
**Context**: The working model requires evidence references for terminal transitions (e.g., `in_progress` → `completed`). The specific format, content requirements, and validation rules are not yet defined.
**Specific Questions**:
*   What constitutes valid evidence for terminal transitions in industry frameworks (approval records, test results, session notes, sign-off artifacts)?
*   How is evidence linked — inline references, separate evidence registers, or artifact metadata?
*   Should evidence requirements differ by transition type (terminal vs. non-terminal)?
*   What validation rules ensure evidence integrity (path resolution, date consistency, author attribution)?
**Deliverable**: Recommended evidence linkage pattern with content requirements and validation rules. Scored comparison per evaluation rubric (Section III.D).

#### Topic 8: Role Accountability Matrix (High)
**Objective**: Evaluate role-based accountability patterns for status update governance.
**Context**: The seed analysis proposed a 4-role matrix (Consultant/Planner/Developer/Reviewer) with domain-specific update responsibilities. This needs benchmarking against industry RACI models.
**Specific Questions**:
*   How do mature delivery organizations assign status update accountability (RACI, DACI, other models)?
*   Should status updates be role-restricted (only designated roles can update certain fields) or role-attributed (any role can update, with attribution tracking)?
*   What conflict resolution mechanisms exist when multiple roles update the same entity?
**Deliverable**: Recommended accountability model with role-field mapping.

#### Topic 9: Stale-State SLA Models (Medium)
**Objective**: Survey stale-state detection and SLA governance models for future Phase 2 use.
**Context**: Stale-state SLA governance is deferred to Phase 2 per planning decisions. The research should survey options to inform future work without producing normative recommendations for P-STD-002 v1.
**Specific Questions**:
*   What SLA models do enterprise tools use for stale-state detection (time-based thresholds, event-based triggers, cadence enforcement)?
*   What are typical threshold values (e.g., 48h/72h/7d for `in_progress` items without update)?
*   How are escalation paths defined (automated alerts, manager notification, status force-update)?
**Deliverable**: Survey of SLA models with applicability assessment. Informational only — not for P-STD-002 v1 CLAUSE authoring.

### Part E: Status Artifact Specification

#### Topic 10: Artifact Format Options (High)
**Objective**: Evaluate format options for program status artifacts in light of `P-CON-003` (Artifact Format Governance).
**Context**: `P-CON-003(B)` now permits non-Markdown formats for programmatic execution artifacts when explicitly governed by a standard. The seed analysis proposed YAML for the Program Status Ledger (PSL). Trade-offs between YAML, JSON, Markdown with YAML frontmatter, and hybrid approaches need evaluation.
**Specific Questions**:
*   What are the trade-offs of YAML vs. JSON vs. Markdown-with-YAML-frontmatter for machine-readable status data?
*   How do enterprise tools represent status data at rest (structured files, database records, API payloads)?
*   Which format best supports agentic read/write workflows (LLM role updates)?
*   What are the risks of non-Markdown status artifacts in a primarily Markdown-governed ecosystem?
**Deliverable**: Scored format comparison using the evaluation rubric (Section III.D).

#### Topic 11: Artifact Cardinality (High)
**Objective**: Evaluate single-artifact vs. multi-artifact models for program status representation.
**Context**: The seed analysis proposes three artifacts (PSL YAML, PSN Markdown, Changelog). The ST002-AC001 informative schema described a single file. Industry practice varies.
**Specific Questions**:
*   What are the trade-offs of single-artifact (all-in-one) vs. dual-artifact (structured + narrative) vs. triple-artifact (structured + narrative + changelog) models?
*   How do enterprise systems separate structured status data from narrative status communication?
*   What is the minimum viable artifact set for a program with 2-5 active initiatives?
*   If multi-artifact, what is the authoritative source and what is derived?
**Deliverable**: Recommended artifact cardinality with authority hierarchy and trade-off analysis. Scored comparison per evaluation rubric (Section III.D).

---

## III. CONSTRAINTS, ASSUMPTIONS & METHODOLOGY

### A. Constraints
*   **Boundary**: Research is recommendations-only. No P-STD-002 CLAUSE text drafting. No status artifact implementation.
*   **Scope**: Program-level status governance only. Initiative-specific implementation details are out of scope.
*   **Output**: Research report per `prompt/templates/researcher/template_research_report.md`.

### B. Assumptions
*   **Working Model**: The current working model (7-state enum, unified dependency schema, evidence linkage as normative requirement) represents a strong preference with stated rationale from prior consultation. The researcher MAY challenge any element of the working model with sufficient externally sourced evidence. Challenges MUST be framed as alternative recommendations with explicit trade-off analysis, not as rejections.
*   **Seed Analysis**: `analysis_P-PH000-ST002_status-system-research.md` is an informal working note providing initial direction. It is NOT a formal research artifact and carries no normative authority.

### C. Methodology "Hierarchy of Truth"
1.  **External Industry Standards** (PMI/PMBOK, SAFe, PRINCE2, ISO, Azure DevOps, Jira) — Benchmarking Authority
2.  **Program SSOT Files** (`sps_P-PROGRAM.md` constraints, accepted standards) — Governance Context
3.  **Internal Seed Analysis** (`analysis_P-PH000-ST002_status-system-research.md`) — Informative Working Note Only
4.  **Session Transcripts / Planning Documents** — Traceability Context Only; No Normative Authority

### D. Evaluation Rubric (per `T102-STD-006-CLAUSE-008`)

All topics requiring comparative evaluation MUST apply the following weighted rubric:

| Dimension | Weight (1–5) | Description |
|:--|:--|:--|
| Program Fit | 5 | Aligns with the P governance model: multi-initiative, multi-role (Consultant/Planner/Developer/Reviewer), Markdown-primary ecosystem |
| Industry Alignment | 5 | Established practice in recognized PM frameworks (PMI, SAFe, PRINCE2) or enterprise tooling (Azure DevOps, Jira) |
| Agentic Operability | 3 | Machine-readable, deterministic for LLM agentic role workflows; supports automated read/write update sequences |
| Adoption Overhead | 3 | Migration cost and process burden to implement within the current artifact ecosystem (lower overhead = higher score) |
| Extensibility | 2 | Supports future growth (additional initiatives, Phase 2 features) without structural rework |

Per-option scores MUST use a 1–5 scale for each dimension. Weighted totals MUST be computed and presented.

---

## IV. CROSS-TOPIC INTEGRATION

*   **Integration 1**: How do transition rules (Topic 2) interact with evidence linkage requirements (Topic 7)? Which transitions require evidence, and does the transition matrix define evidence-required vs. evidence-optional paths?
*   **Integration 2**: How does artifact format choice (Topic 10) constrain or enable dependency representation (Topic 5)? Does a YAML ledger support typed dependency metadata more effectively than Markdown?
*   **Integration 3**: How does artifact cardinality (Topic 11) interact with the update protocol (Topics 7-8)? Does a multi-artifact model require a more complex update sequence?
*   **Gap Analysis**: What is missing in the seed analysis (`analysis_P-PH000-ST002_status-system-research.md`) to support all 5 CLAUSE domains? Identify specific gaps per domain.

---

## V. INPUT PACKET (CONTEXT MAP)

### A. Core Governance
*   SSOT: `prompt/artifacts/tasks/P/ssot/sps_P-PROGRAM.md`
*   Plan (research stream): `prompt/artifacts/tasks/P/workspace/plan/plan_P-PH000-ST004.md`
*   Plan (consumer activity): `prompt/artifacts/tasks/P/workspace/plan/PH000/ST001/plan_P-PH000-ST001-AC003.md`
*   Authoring authority: `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md`

### B. Informal Seed (Non-Authoritative)
*   `prompt/artifacts/tasks/P/workspace/PH000/ST002/analysis/analysis_P-PH000-ST002_status-system-research.md` — Informal working note; pre-brief seed. NOT a formal research artifact.

### C. Informative Planning Context
*   `prompt/artifacts/tasks/P/workspace/plan/plan_P-PH000-ST002.md` — ST002 stream plan; AC001 schema is informative seed only.
*   `prompt/artifacts/tasks/P/workspace/plan/plan_P-PH000-ST001.md` — ST001 stream plan; AC003 scope and dependencies.

### D. Standards & Templates
*   `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-006_research-artifacts-index.md` — Research commissioning standard
*   `prompt/templates/researcher/template_research_report.md` — Report template

### E. Anti-Patterns / Exclusions
*   **IGNORE**: `plan_P-PH000-ST002.md` AC001 schema section as normative input — it is informative seed only per session notes.
*   **IGNORE**: Session-scoped DEC tokens (e.g., DEC-004, DEC-005) as normative constraints — they are traceability pointers only.

---

## VI. DELIVERABLE FORMAT REQUIREMENTS

The research report MUST use the standard template located at:
> `prompt/templates/researcher/template_research_report.md`

**Specific Mapping Instructions for this Brief**:
1.  **Section I (Exec Summary)**: Must include a GO/NO-GO/PIVOT verdict on the current working model (7-state enum, unified dependency schema, evidence linkage normative). Must list top 3 key findings.
2.  **Section III (Topic Findings)**:
    *   Each topic MUST include Evidence & Forensics (with external source citations), Analysis (synthesis + gap analysis), and Governance Implication (P-STD-002 CLAUSE domain impact).
    *   Topics requiring comparative evaluation (Topics 1, 3, 5, 7, 10, 11) MUST include scored comparison tables using the evaluation rubric from Section III.D.
3.  **Section V (Artifact Updates)**: Must map findings to P-STD-002 substandard domains (P-STD-002A through P-STD-002E) as an integration recommendations package.
4.  **Completeness**: Do NOT delete empty sections. If a topic has no implications for a particular area, explicitly state "None".

---

## VII. ISSUES & RISKS REGISTER (T102-STD-007)

**Issues**

| ID | Title | Description | Owner | Status | Priority | Proposed Date | Resolution Notes | Resolution Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

**Risks**

| ID | Title | Description | Owner | Status | Priority | Proposed Date | Mitigation Notes | Mitigation Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

**ID Rules**
*   IDs MUST use the scoped, sequential format: `P-RES-001-ISSUE-###` and `P-RES-001-RISK-###`.
*   IDs MUST remain stable once created (no reuse, no renumbering).

---

## VIII. CRITICAL DEPENDENCIES (E-RID MAPPING)

*   **P-STD-002A** (Status Vocabulary): Topics 1-2 findings will define the canonical enum set and transition rules.
*   **P-STD-002B** (Health Assessment): Topics 3-4 findings will define RAG thresholds and health dimensions.
*   **P-STD-002C** (Dependency Visibility): Topics 5-6 findings will define the dependency typing schema and cross-initiative model.
*   **P-STD-002D** (Update Protocol): Topics 7-9 findings will define evidence linkage, role accountability, and stale-state governance.
*   **P-STD-002E** (Status Artifact): Topics 10-11 findings will define artifact format and cardinality.

---

## IX. SUCCESS CRITERIA

*   All 11 topics addressed with findings supported by externally sourced evidence (external framework citations required for each topic).
*   Evaluation rubric (Section III.D) applied consistently across all comparative topics (Topics 1, 3, 5, 7, 10, 11) with scored comparison tables and weighted totals per `T102-STD-006-CLAUSE-008`.
*   Integration recommendations map each finding to at least one P-STD-002 CLAUSE domain (P-STD-002A through P-STD-002E).
*   Gap analysis identifies specific shortfalls in the seed analysis per CLAUSE domain.
*   No P-STD-002 CLAUSE text drafted (recommendations-only boundary respected).
*   Issues and risks identified during research are registered per `T102-STD-007` schema.
