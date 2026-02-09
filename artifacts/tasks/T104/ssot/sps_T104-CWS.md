---
artifact_type: 'SPS'
initiative_id: 'T104'
initiative_code: 'CWS'
version: '1.0.1'
date: '2026-02-05'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
---

# SYNTHESIZED PROBLEM STATEMENT (SPS): Consultant Workspace Standard - T104

## I. EXECUTIVE SUMMARY

## II. TABLE OF CONTENTS
I. [Executive Summary](#i-executive-summary)
II. [Table of Contents](#ii-table-of-contents)
III. [Core Content](#iii-core-content)
    A. [Problem Definition](#a-problem-definition)
    B. [Key Specifications & Requirements](#b-key-specifications--requirements)
    C. [Epics & Breakdown](#c-epics--breakdown)
    D. [Project Glossary](#d-project-glossary)
IV. [Glossary](#iv-glossary)
V. [Appendix](#v-appendix)
VI. [Validation Checklist](#vi-validation-checklist)
VII. [Stakeholder Sign-off](#vii-stakeholder-sign-off)
VIII. [Next Steps](#viii-next-steps)
IX. [Changelog](#ix-changelog)

---

## III. CORE CONTENT

### A. Problem Definition

#### 1. The Problem
The current consultant workspace lacks a formalized, standardized scaffolding system. While `T102` established the consultancy workflow artifacts (`SPS`, `Request`, `Concept`), the supporting "workspace" tools—such as Roadmaps, Notes, Proposals, Analyses, and Changelogs—suffer from terminology drift, inconsistent naming conventions, and unclear boundaries between "tooling" and "SSOT". This ambiguity leads to misfiling of information (e.g., placing specs in session notes), duplication of governance rules, and nondeterministic file paths that hinder agentic retrieval and automation. Without a single source of truth for the *workspace itself*, maintenance becomes manual and error-prone.

#### 2. The Desired Outcome
To establish a robust `Consultant Workspace Standard (CWS)` initiative that formalizes the role, structure, and boundaries of all auxiliary workspace artifacts (`Roadmap`, `Notes`, `Proposal`, `Analysis`, `Changelog`). This system will:
1.  **Lock Naming & Terminology**: Enforce strict file naming, ID patterns, and heading semantics (Phase/Stream/Activity) across all initiatives.
2.  **Define Boundaries**: Clearly separate "Workflow Tools" (transient/operational) from "SSOT Artifacts" (normative/governance), using explicit MUST/MUST NOT rules.
3.  **Standardize Templates**: Provide toolable templates for each artifact type that align with the `T102` operating model.
4.  **Enable Deterministic Retrieval**: Ensure every artifact has a predictable location and internal structure to support future agentic automation.

#### 3. Business Case
Standardizing the consultant workspace directly reduces the "governance overhead" required to start and maintain new initiatives. By eliminating the need to re-decide folder structures, naming conventions, and artifact roles for every new task, we accelerate the "Time to First Value" for consultation. Furthermore, a predictable workspace structure is a prerequisite for reliable "Agentic Context Retrieval"—if agents cannot guess file paths deterministically, they cannot effectively assist with cross-file analysis or validation.

### B. Initiative Considerations

#### 1. Organization & Responsibilities
**Role Definitions**
| Actor | Role Title(s) | Decision Rights | Primary Responsibilities | Scope Notes |
| :--- | :--- | :--- | :--- | :--- |
| `Client` | **Decision Owner** | Approves baselines and cutover | Sets priorities; resolves scope conflicts; provides acceptance decisions | Initiative-wide |
| `LLM_Consultant` | **Technical Consultant, Project Manager, Product Lead** | Proposes baselines/requests; no final approval authority | Leads governance, requirements definition, and high-level project management; coordinates contributors; maintains SSOT coherence | Initiative/Epic/Feature (by assignment) |
| `LLM_Planner` | **Planner** | Authors implementation plans; no approval authority | Produces feature-level implementation plans and updates plan artifacts | Feature scope |
| `LLM_Researcher` | **Research Analyst** | No approval authority | Produces research, options, and trade-offs to support decisions | Initiative-wide |
| `LLM_Developer` | **Technical Lead, Lead Engineer** | No baseline approval authority; advises go/no-go | Implements changes; produces validation evidence; advises feasibility and architecture | Feature delivery |

**Governance RACI**
| Governance Activity | R (Responsible) | A (Accountable) | C (Consulted) | I (Informed) |
| :--- | :--- | :--- | :--- | :--- |
| Approve Initiative baseline | `LLM_Consultant` | `Client` | `LLM_Planner`, `LLM_Developer`, `LLM_Researcher` | — |
| Approve Epic baseline | `LLM_Consultant` | `Client` | `LLM_Planner`, `LLM_Developer`, `LLM_Researcher` | — |
| Approve Feature baseline | `LLM_Consultant` | `Client` | `LLM_Planner`, `LLM_Developer`, `LLM_Researcher` | — |
| Approve Feature implementation plan | `LLM_Planner` | `Client` | `LLM_Consultant`, `LLM_Developer` | `LLM_Researcher` |
| Approve cutover | `LLM_Developer` | `Client` | `LLM_Consultant`, `LLM_Planner` | `LLM_Researcher` |

#### 2. Project Assumptions
**ASSUM Validation Lifecycle Summary**

| ID | Title | Status | Validation Method | Timing | Owner | If Invalidated | CON Cross-Ref |
|:---|:------|:-------|:------------------|:-------|:------|:---------------|:--------------|
| `T104-ASSUM-001` | Planner Optionality | `Pending` | Validate via PH001 delivery: confirm ST001 + ST002 can be executed without mandatory planner role | PH001 | LLM_Consultant | Mitigation | `T104-CON-003` |
| `T104-ASSUM-002` | Forward-only Adoption | `Pending` | Validate via PH001–PH002: confirm standards adoption does not require bulk legacy migrations | PH001–PH002 | LLM_Consultant | Fallback | `T104-CON-003` |

* **T104-ASSUM-001 (Planner Optionality)** — LLM_Planner involvement is optional by default; involvement SHALL be triggered per-activity based on complexity thresholds codified in `T104-STD-001`. This assumption avoids overhead at current `T104` scale and aligns with the `T102` request-driven model. If invalidated (e.g., mandatory planner intermediary becomes necessary), mitigation involves updating `T104-STD-001` to mandate planner involvement for specified complexity bands.

* **T104-ASSUM-002 (Forward-only Adoption)** — Standards and naming conventions MAY be adopted forward-only without requiring immediate bulk migration of legacy artifacts. This assumption supports sustainable adoption and prevents scope creep from retroactive rename work. If invalidated (e.g., bulk migration becomes necessary for tooling compatibility), fallback involves scoping a dedicated migration activity under `T104E` or a successor initiative.

#### 3. Project Constraints

* **T104-CON-001 (Link Don't Duplicate)** — Artifacts SHALL link by ID or path rather than duplicating normative content across workflow tools and SSOT surfaces. Duplication creates drift risk; linking preserves single-source-of-truth integrity.
  External Reference: `T102-STD-003 (Explicit Inheritance Model)`

* **T104-CON-002 (Markdown Frontmatter)** — All governance artifacts SHALL remain Markdown files with YAML frontmatter. This constraint ensures toolability, schema validation, and consistent review workflows.
  External Reference: `T102-CON-001 (Markdown Frontmatter)`

* **T104-CON-003 (No Retroactive Migration)** — Retroactive bulk renames or migrations SHALL NOT be performed outside explicitly scoped refactor work. Authors SHALL prefer forward-only conformance to minimize churn and prevent scope creep.

* **T104-CON-004 (Prefix Discipline)** — Artifact files SHALL use deterministic type prefixes (e.g., roadmap_, plan_, notes_, changelog_, sps_, request_, concept_) to enable predictable retrieval by agents and humans. This constraint supports `T104-QG-001 (Deterministic Retrieval)`.
  - Note: This constraint is proposed for elevation to program-level (P-CON-###) pending client review.

* **T104-CON-005 (No Embedded Changelogs)** — Changelog data SHALL NOT be embedded within source artifact files. Version history SHALL be maintained in dedicated changelog_<artifact>.md files or equivalent external surfaces, linked from the source artifact. This constraint enables clean artifact readability and supports automated changelog tooling.
  - Note: This constraint is proposed for elevation to program-level (P-CON-###) pending client review.

#### 4. Quality Goals

* **T104-QG-001 (Deterministic Retrieval)** — Naming conventions and artifact placement SHALL enable deterministic retrieval by both agents and humans with minimal ambiguity. This is the primary quality goal for T104; all epics and standards serve this outcome.

* **T104-QG-002 (Traceability Integrity)** — Cross-artifact links and IDs SHALL support end-to-end traceability without duplication drift. Link integrity enables audit, navigation, and inheritance verification.
  External Reference: `T102-QG-002 (Traceability Integrity)`

* **T104-QG-003 (Client Readability)** — Governance artifacts SHALL remain executive-readable and scannable. Technical detail may be delegated to linked specifications, but summary surfaces must be accessible to decision-owners.
  External Reference: `T102-QG-001 (Client Readability)`
  
* **T104-QG-004 (Low Disruption)** — Adoption mechanisms SHOULD minimize author retraining and churn, particularly in early phases. Standards SHALL prefer incremental enforcement over disruptive bulk changes.
  External Reference: `T102-QG-003 (Low Disruption)`

* **T104-QG-005 (Thin Spine)** — The Roadmap SHALL remain pointer-based ("thin spine"), with execution detail residing in Plan and Notes artifacts. This prevents roadmap bloat and maintains scannability.

#### 5. Dependencies

* **T104-DEP-001 (T102 Standards Stack)** — T104 SHALL adopt ALL `T102` governance standards stack for ID governance, research workflow, decision records, inheritance model, and standards model. Adopted standards include: T102-STD-003/004/005/006/007/009. All `T104` IDs, research artifacts, STD entries, and decision records SHALL conform to the adopted T102 specifications.
  External Reference: `T102-STD-003 (Inheritance Model Standard)`, `T102-STD-004 (Specification Standard & Guideline)`, `T102-STD-005 (ID Governance Standard)`, `T102-STD-006 (Research Workflow Standard)`, `T102-STD-007 (LLM Quality Control)`, `T102-STD-009 (Governance Standards Model)`

* **T104-DEP-002 (Research Workflow)** — Formal research commissions SHALL follow `T102-STD-006` research workflow rules. Each research commission SHALL produce a brief and report, both indexed in SPS III.B.9 (Research) with standardized linking per the adopted specification.
  External Reference: `T102-STD-006 (Research Workflow Standard)`

* **T104-DEP-003 (Client Engagement)** — Decision-owner review cadence is an external dependency at phase gates and baseline approvals. T104 timeline assumptions depend on client availability for approval cycles per the program-level SLA.
  External Reference: `T102-DEP-001 (Client Engagement)`

* **T104-DEP-004 (Planner Integration)** — `T104` artifacts SHALL maintain compatibility with future planner system integration. Handoff schemas and plan structures SHOULD anticipate downstream consumption by `LLM_Planner`, even while planner involvement remains optional per `T104-ASSUM-001`.
  External Reference: `T102-DEP-002 (Planner Integration)`

* **T104-DEP-005 (Template Alignment)** — `T104` SPS structure and ID token scopes SHALL remain aligned to canonical `T102` standards. Authors SHALL NOT introduce initiative-local ID patterns or scope rules that conflict with adopted `T102` specifications.
  External Reference: `T102-STD-005 (ID Governance Standard)`

* **T104-DEP-006 (T102 Role Catalog)** — `T104` SHALL reference `T102-DEP-003` for program-wide role definitions. Role titles, decision rights, and responsibility boundaries used in `T104` governance SHALL align with the `T102` role catalog maintained in `prompt/documentation/main/prompt_main.md` Section 3.
  External Reference: `T102-DEP-003 (Role Definitions)`

#### 6. Interfaces

* **T104-IF-001 (Client Review)** — Gate approvals SHALL record decision-owner review signals using a consistent schema across plans and SSOT artifacts. The schema SHALL include: approval date, approver role, artifact reference, and explicit approval/rejection/deferral status.
  External Reference: `T102-IF-002 (Client Review)`

* **T104-IF-002 (Planner Handoff)** — A minimal handoff bundle interface SHALL be defined for transitions from consultancy artifacts to downstream planning. The bundle SHALL include: scope reference, baseline artifacts, open questions, and acknowledgment signal. Detailed schema is specified in `T104-STD-001`.
  External Reference: `T102-IF-001 (Planner Handoff)`

* **T104-IF-003 (Co-authoring Protocol)** — Co-authoring rhythm and repo-as-SSOT behavior SHALL be defined for consultant+client collaboration. The protocol SHALL specify: who may edit which artifacts, merge authority, and conflict resolution. Repo state is authoritative; out-of-repo artifacts are non-normative until merged.
  External Reference: `T102-IF-004 (Co-authoring Consultancy)`

* **T104-IF-004 (Status Reporting)** — A minimal status/reporting surface SHALL be defined to prevent ad-hoc "status in notes" drift. Status updates SHOULD reside in designated locations (e.g., Roadmap checklist, dedicated status section) rather than scattered across session notes. Cadence and format are specified in `T104-STD-003`.

* **T104-IF-005 (Role Collaboration)** — Collaboration boundaries between Consultant, Planner, and Developer roles SHALL be defined for change ownership and clarification loops. The boundary SHALL specify: who initiates changes, who approves, and escalation paths. Detailed boundaries are specified in `T104-STD-001`.
  External Reference: `T102-IF-003 (Roles Collaboration)`, `T102-DEP-003 (Role Definitions)`

#### 7. Project Standards

| STD ID | Title | Status | Owner | Effective | Supersedes | Adopts | Verification | Governed By | Reference |
|:-------|:------|:-------|:------|:----------|:-----------|:-------|:------------|:-----------|:----------|
| `T104-STD-001` | **Planning Hierarchy** | `planned` | LLM_Consultant | PH001-ST002 | — | — | Review: plan artifacts comply with hierarchy schema; CI: lint prefix/nesting | `T102-STD-009 (Governance Standards Specification)`, `T102-CON-009 (Normative Keywords)` | `T102-STD-005`, `T102-STD-009`, `T102-CON-009` |
| `T104-STD-002` | **UID Convention** | `planned` | LLM_Consultant | PH001-ST002 | — | `T102-STD-005 (ID Specification & Rules)` | CI: regex validation of IDs; Review: prefix compliance | `T102-STD-009 (Governance Standards Specification)`, `T102-CON-009 (Normative Keywords)` | `T102-STD-005`, `T102-CON-009` |
| `T104-STD-003` | **Gate Definition** | `planned` | LLM_Consultant | PH001-ST002 | — | — | Review: gate records exist with required fields; Checklist compliance | `T102-STD-009 (Governance Standards Specification)`, `T102-CON-009 (Normative Keywords)` | `T102-STD-009`, `T102-CON-009` |

**STD Bodies**

* **T104-STD-001 (Planning Hierarchy)** — All T104 planning artifacts SHALL follow the normative planning hierarchy (Phase → Stream → Activity → Task → Step) and role-boundary clauses. This standard establishes the structural rules for plan artifacts and the decision-rights model for Consultant, Planner, and Developer roles.
  - **Minimum Viable Conformance**:
    1. Plan artifacts use correct hierarchy nesting (no skipped levels).
    2. Role decision rights respected: Consultant (WHAT+WHY), Planner (HOW MUCH), Developer (HOW), aligned with `T104-DEP-006 (T102 Role Catalog)`.
    3. Execution mode (SEQUENTIAL/PARALLEL) and dependencies explicitly declared.
    4. Handoff acknowledgments recorded per CLAUSE-006.
    5. Planner optionality triggers follow CLAUSE-005 complexity thresholds per `T104-ASSUM-001 (Planner Optionality)`.
  - Note: `Adopts = —` is intentional until a canonical adopted spec is defined in ST002; see `T102-STD-009-CLAUSE-004D (STD Conciseness)`.

* **T104-STD-002 (UID Convention)** — All T104 artifact names, IDs, and link patterns SHALL conform to the deterministic naming and ID construction rules defined in the adopted specification.
  - **Minimum Viable Conformance**:
    1. IDs match canonical regex patterns per adopted spec CLAUSE-001.
    2. Artifact files use type-specific prefixes per `T104-CON-004`.
    3. Links use relative paths with stable anchors per adopted spec CLAUSE-004.
  - External Reference: `T102-STD-005 (ID Specification & Rules)`

* **T104-STD-003 (Gate Definition)** — All T104 phase gates SHALL define and record entry/exit criteria, evidence requirements, and approver signals. This standard establishes the gate schema for baseline approvals at Phase boundaries.
  - **Minimum Viable Conformance**:
    1. Each phase has defined entry criteria (required artifacts, predecessor completion).
    2. Each phase has defined exit criteria (approval signal, evidence record).
    3. Gate records captured per `T104-IF-001` schema.
    4. Escalation path defined for blocked gates.
    5. Approver role documented per `T102-IF-002` contract.
  - Note: `Adopts = —` is intentional until a canonical adopted spec is defined in ST002; see `T102-STD-009-CLAUSE-004D (STD Conciseness)`.

#### 8. Project Guidances & Notes

**Implementation Guidance**
* **T104-IG-001 (Links Register)** — Every Plan and Roadmap artifact SHALL include a Links Register section that explicitly enumerates primary cross-references (parent plan, notes, SSOT, research inputs). This register acts as the navigation spine for agentic and human retrieval and supports `T104-QG-005 (Thin Spine)`. Authors SHALL prefer stable relative paths and SHALL NOT embed duplicate content where a link suffices.

* **T104-IG-002 (Research Linking)** — Research commissions SHALL follow the Brief → Report → Analysis → Proposal/SPS linking chain. Each artifact links forward to its consumer and backward to its source. Authors SHALL NOT duplicate research findings into consuming artifacts; instead, they SHALL reference findings by ID and section. This guidance implements `T104-CON-001` and operationalizes `T104-DEP-002` for research artifacts.
  External Reference: `T102-STD-006 (Research Artifacts Index)`

**Integration Guidance**
* *No initiative-scope integration guidance items.* Integration guidance (`INT`) is recommended at Epic/Feature scope where specific artifact-to-artifact integration patterns apply. See `T104-NOTE-001` for scope clarification.

**Notes**
* **T104-NOTE-001 (INT Scope)** — At initiative scope, implementation guidance (`IG`) is preferred over integration guidance (`INT`). While `T102-STD-005` allows `INT` at all scopes, the initiative level typically lacks the artifact-to-artifact specificity that `INT` is designed to address. Epic and Feature scopes are the recommended homes for `INT` items.
External Reference: `T102-STD-005-CLAUSE-002`

* **T104-NOTE-002 (Plan Deferral)** — The activity plan template and formal step-level IDs (e.g., `T104-AC###-TK###-ST###`) are intentionally deferred to a future initiative alongside the LLM_Planner system. Phase 1 uses a skeleton plan structure without step-granularity identifiers. This deferral aligns with `T104-ASSUM-001`.

* **T104-NOTE-003 (Changelog Discipline)** — Changelog entries SHALL follow a delta-only style (consistent with "Keep a Changelog" convention). Entries record WHAT changed (version, date, type, summary) without narrative context or rationale. Rationale and context belong in Notes or Decision Records, not changelogs.

#### 9. Research

| Research ID | Title | Summary | Reference |
| :--- | :--- | :--- | :--- |
| `T104-RES-001` | **Agentic Workspace Assessment** | Assessed current workspace state, identified structural/naming drift and retrieval risks; informed SPS migration and AC002 consultation scope. | [brief](../research/brief/brief_T104-RES-001_agentic-workspace-assessment.md) \| [report](../research/report/report_T104-RES-001_agentic-workspace-assessment.md) \|
| `T104-RES-002` | **Requirements Candidate Research** | Inventoried SPS III.B gaps; proposed 42 candidate IDs across 12 categories; mapped T102 cross-dependencies; validated epic appropriateness; primary input for AC002 consultation. | [brief](../research/brief/brief_T104-RES-002_requirements-candidate-research.md) \| [report](../research/report/report_T104-RES-002_requirements-candidate-research.md) \|

#### 10. Issues & Risks

**Issues**

| ID | Title | Description | Owner | Status | Priority | Proposed Date | Resolution Notes | Resolution Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `T104-ISSUE-001` | Governance Rules Misalignment | `workspace_documentation_rules.md` defines Plan/Proposal/Completion roles conflicting with T104 Roadmap/Notes/Changelog semantics | LLM_Consultant | `OPEN` | `HIGH` | 2026-01-18 | — | — |
| `T104-ISSUE-002` | Notes Template Drift | Notes template uses LOG/Subphase semantics inconsistent with T104 initiative NOTES usage | LLM_Consultant | `OPEN` | `HIGH` | 2026-01-18 | — | — |
| `T104-ISSUE-003` | Naming Inconsistency | Case and suffix drift across artifacts undermines deterministic retrieval | LLM_Consultant | `OPEN` | `MEDIUM` | 2026-01-18 | — | — |
| `T104-ISSUE-004` | Missing Analysis Artifact | Analysis artifact coverage incomplete for research commissions; pattern needs standardization | LLM_Consultant | `IN-REVIEW` | `HIGH` | 2026-01-18 | RES-001 has companion analysis; standardize expectation via `T104-IG-002` | — |
| `T104-ISSUE-005` | INT Scope Mismatch | Initiative-scope INT appears in SPS template but is not recommended at initiative scope per governance guidance | LLM_Consultant | `RESOLVED` | `HIGH` | 2026-02-02 | Resolved via `T104-NOTE-001`; IG is preferred at initiative scope | 2026-02-03 |
| `T104-ISSUE-006` | DEP-003 Alignment | `T102-DEP-003 (Role Definitions)` is now confirmed defined in T102 SPS; T104 references aligned via `T104-DEP-006` | LLM_Consultant | `RESOLVED` | `MEDIUM` | 2026-02-02 | Confirmed `T102-DEP-003` exists in `sps_T102-CONSULTANT.md`; `T104-DEP-006` references it correctly | 2026-02-03 |
| `T104-ISSUE-007` | Changelog Constraint Elevation | `T104-CON-005 (No Embedded Changelogs)` is cross-cutting and may warrant program-level governance at T102-CON-###. Requires T102 SPS review and potential ADR. | LLM_Consultant | `OPEN` | `MEDIUM` | 2026-02-03 | — | — |

**Risks**

| ID | Title | Description | Owner | Status | Priority | Proposed Date | Mitigation Notes | Mitigation Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `T104-RISK-001` | Duplication Drift | Drift via content duplication across workflow tool artifacts undermines single-source-of-truth | LLM_Consultant | `MONITORED` | `HIGH` | 2026-01-18 | Mitigation: `T104-CON-001 (Link Don't Duplicate)`; ongoing monitoring required | — |
| `T104-RISK-002` | Hidden Gate Layer | Stream or subphase structures may be misused as hidden governance gates outside formal phase gate schema | LLM_Consultant | `MONITORED` | `MEDIUM` | 2026-01-18 | Mitigation: `T104-STD-001` hierarchy clauses; monitor during PH001 | — |
| `T104-RISK-003` | Retrieval Failures | Naming inconsistency causes agentic and human retrieval failures | LLM_Consultant | `MONITORED` | `MEDIUM` | 2026-01-18 | Mitigation: `T104-CON-004 (Prefix Discipline)` and `T104-QG-001 (Deterministic Retrieval)` | — |
| `T104-RISK-004` | Category Drift | Invalid initiative-scope INT IDs may enter SPS baseline if scope guidance is unclear | LLM_Consultant | `MITIGATED` | `HIGH` | 2026-02-02 | Mitigated by `T104-ISSUE-005` resolution and `T104-NOTE-001` | 2026-02-03 |
| `T104-RISK-005` | Consultation Overload | Unresolved governance conflicts may reduce AC002 decision quality and completeness | LLM_Consultant | `MONITORED` | `MEDIUM` | 2026-02-02 | Mitigation: structured task sequencing (TK001→TK002→TK003) and activity plan approach | — |

### C. Epics & Breakdown

#### 0. Initiative WBS Map

| Level | PM Type | ID | Name |
| :--- | :--- | :--- | :--- |
| 1 | Initiative | T104 | Consultant Workspace Standard |
| 2 | Epic | T104A | Roadmap Standardization |
| 2 | Epic | T104B | Notes Standardization |
| 2 | Epic | T104C | Proposal Standardization |
| 2 | Epic | T104D | Analysis Standardization |
| 2 | Epic | T104E | Changelog Standardization |
| 2 | Epic | T104F | Plan Standardization |
| 2 | Epic | T104G | Communication Standardization |

---

#### 1. `T104A` Epic: `ROADMAP` - Roadmap Standardization

```yaml
epic_id: 'T104A'
epic_code: 'ROADMAP'
epic_title: 'Roadmap Standardization'
epic_type: 'existing'
epic_status: 'draft'
epic_owner: 'LLM_Consultant'
```

##### i. Purpose
To standardize the **Roadmap** artifact (`roadmap_...`) as the primary orchestration tool for the agentic consultant workflow. This Epic will lock the Phase → Stream → Activity → Task hierarchy and establish the "Links Register" as the mandatory navigation spine for the workspace. It ensures that the Roadmap remains a high-level planning and dependency-tracking tool, explicitly separated from execution logging or normative specification storage.

##### ii. Scope

* **In Scope:**
    *   Defining the mandatory `Phase > Stream > Activity > Task` hierarchy and heading semantics.
    *   Establishing the "Links Register" schema as the workspace navigation spine.
    *   Defining the "Execution Mode" and "Depends On" notation standards.
    *   Standardizing the Roadmap file naming convention (`roadmap_<task>_<phase>.md`).
*   **Out of Scope:**
    *   **Execution Logs:** The Roadmap MUST NOT contain daily status updates, chat logs, or granular execution details (these belong in `Notes`).
    *   **Normative Specs:** The Roadmap MUST NOT store final requirements or governance rules (these belong in `SSOT` artifacts).

##### iii. Inherited Considerations

| Source Artifact | Source ID | Category | Inherited Rule IDs |
| :-------------- | :-------- | :------- | :----------------- |
| — | — | — | — |

##### iv. Governance & Roadmap

**Scope & Ownership**
- Owner: —
- Decision Owner: —
- Support: —
- Org baseline (RACI): —

**Phase & Gates**
| Phase | Title | Intent | Key Exit Milestone | Duration Band | Gate Approver (A) | Phase Lead (R) | Plan Link |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

**References**
- —

##### v. Feature Register

| ID | Code | Title | Purpose | Feature Lead (R) | Status | Canonical Link (Request) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |

##### vi. Epic Requirements

* **Assumptions**

  * **ASSUM Validation Lifecycle Summary**

    | ID | Title | Status | Validation Method | Timing | Owner | If Invalidated | CON Cross-Ref |
    |:---|:------|:-------|:------------------|:-------|:------|:---------------|:--------------|
    | — | — | — | — | — | — | — | — |

  * **T104A-ASSUM-001** —

* **Constraints**
  * **T104A-CON-001** —

* **Quality Goals**
  * **T104A-QG-001** —

* **Dependencies**
  * **T104A-DEP-001** —

* **Interfaces**
  * **T104A-IF-001** —

##### vii. Epic Standards

| STD ID | Title | Status | Owner | Effective | Supersedes | Adopts | Verification | Reference |
|:-------|:------|:-------|:------|:----------|:-----------|:-------|:-------------|:----------|

* **T104A-STD-001** —
  - **Minimum Viable Conformance**:
    1) —
    2) —

##### viii. Epic Development Guidances

* **Implementation Guidance**
  * **T104A-IG-001** —

* **Integration Guidance**
  * **T104A-INT-001** —

**Research**

| Research ID | Title | Summary | Reference | Brief | Report |
| :--- | :--- | :--- | :--- | :--- | :--- |

**Notes**
*   **2026-01-27**: Initial dossier scaffold created.

**Issues**
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Resolution Notes | Resolution Date |
|:---|:------|:------------|:------|:-------|:---------|:--------------|:-----------------|:----------------|

**Risks**
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Mitigation Notes | Mitigation Date |
|:---|:------|:------------|:------|:-------|:---------|:--------------|:-----------------|:----------------|

---

#### 2. `T104B` Epic: `NOTES` - Notes Standardization

```yaml
epic_id: 'T104B'
epic_code: 'NOTES'
epic_title: 'Notes Standardization'
epic_type: 'existing'
epic_status: 'draft'
epic_owner: 'LLM_Consultant'
```

##### i. Purpose
To standardize the **Notes** artifact (`notes_...`) as the designated surface for session continuity and non-normative decision capture. This Epic serves to eliminate ambiguity between "working notes" and "execution logs" or "changelogs." It establishes the Notes artifact as a place to record rationale, options explored, and session outcomes, ensuring that critical context is preserved without polluting the normative SSOT or the rigid Roadmap.

##### ii. Scope

*   **In Scope:**
    *   Defining the standard session entry format (Date, Context, Decisions, Next Steps).
    *   Standardizing the Notes file naming convention (`notes_<task>_<phase>.md`).
    *   Establishing the "link-don't-duplicate" contract with the Roadmap and SSOT.
*   **Out of Scope:**
    *   **Work Logs:** Notes MUST NOT be used as a "status update" stream (use the Roadmap checklist for status).
    *   **SSOT Storage:** Notes MUST NOT be the authoritative source for requirements or governance (these must be promoted to `SPS`/`Request`/`Concept`).
    *   **Version Deltas:** Notes MUST NOT act as a file changelog (use `Changelog`).

##### iii. Inherited Considerations

| Source Artifact | Source ID | Category | Inherited Rule IDs |
| :-------------- | :-------- | :------- | :----------------- |
| — | — | — | — |

##### iv. Governance & Roadmap

**Scope & Ownership**
- Owner: —
- Decision Owner: —
- Support: —
- Org baseline (RACI): —

**Phase & Gates**
| Phase | Title | Intent | Key Exit Milestone | Duration Band | Gate Approver (A) | Phase Lead (R) | Plan Link |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

**References**
- —

##### v. Feature Register

| ID | Code | Title | Purpose | Feature Lead (R) | Status | Canonical Link (Request) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |

##### vi. Epic Requirements

* **Assumptions**

  * **ASSUM Validation Lifecycle Summary**

    | ID | Title | Status | Validation Method | Timing | Owner | If Invalidated | CON Cross-Ref |
    |:---|:------|:-------|:------------------|:-------|:------|:---------------|:--------------|
    | — | — | — | — | — | — | — | — |

  * **T104B-ASSUM-001** —

* **Constraints**
  * **T104B-CON-001** —

* **Quality Goals**
  * **T104B-QG-001** —

* **Dependencies**
  * **T104B-DEP-001** —

* **Interfaces**
  * **T104B-IF-001** —

##### vii. Epic Standards

| STD ID | Title | Status | Owner | Effective | Supersedes | Adopts | Verification | Reference |
|:-------|:------|:-------|:------|:----------|:-----------|:-------|:-------------|:----------|

* **T104B-STD-001** —
  - **Minimum Viable Conformance**:
    1) —
    2) —

##### viii. Epic Development Guidances

* **Implementation Guidance**
  * **T104B-IG-001** —

* **Integration Guidance**
  * **T104B-INT-001** —

**Research**

| Research ID | Title | Summary | Reference | Brief | Report |
| :--- | :--- | :--- | :--- | :--- | :--- |

**Notes**
*   **2026-01-27**: Initial dossier scaffold created.

**Issues**
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Resolution Notes | Resolution Date |
|:---|:------|:------------|:------|:-------|:---------|:--------------|:-----------------|:----------------|

**Risks**
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Mitigation Notes | Mitigation Date |
|:---|:------|:------------|:------|:-------|:---------|:--------------|:-----------------|:----------------|

---

#### 3. `T104C` Epic: `PROPOSAL` - Proposal Standardization

```yaml
epic_id: 'T104C'
epic_code: 'PROPOSAL'
epic_title: 'Proposal Standardization'
epic_type: 'existing'
epic_status: 'draft'
epic_owner: 'LLM_Consultant'
```

##### i. Purpose
To standardize the **Proposal** artifact (`proposal_...`) as the normative "gate-check" document for approving work before it is promoted to the SSOT. This Epic defines the Proposal as a transient, approval-seeking surface that allows the Consultant to present a complete plan or set of changes for Client sign-off. It bridges the gap between exploration (Analysis) and codification (SSOT), ensuring that no significant change enters the permanent record without explicit authorization.

##### ii. Scope

*   **In Scope:**
    *   Defining the Proposal template structure (Context, Proposed Changes, Impact, Alternatives).
    *   Standardizing the Proposal file naming convention (`proposal_<task>_<phase>.md`).
    *   Establishing the approval gate mechanism (Client Sign-off section).
*   **Out of Scope:**
    *   **Permanent Spec:** The Proposal MUST NOT become a permanent reference document; once approved, its content must be merged into the `SSOT` or `Roadmap`.
    *   **Drafting Workspace:** The Proposal MUST NOT be used for raw exploration (use `Analysis` or `Notes`).

##### iii. Inherited Considerations

| Source Artifact | Source ID | Category | Inherited Rule IDs |
| :-------------- | :-------- | :------- | :----------------- |
| — | — | — | — |

##### iv. Governance & Roadmap

**Scope & Ownership**
- Owner: —
- Decision Owner: —
- Support: —
- Org baseline (RACI): —

**Phase & Gates**
| Phase | Title | Intent | Key Exit Milestone | Duration Band | Gate Approver (A) | Phase Lead (R) | Plan Link |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

**References**
- —

##### v. Feature Register

| ID | Code | Title | Purpose | Feature Lead (R) | Status | Canonical Link (Request) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |

##### vi. Epic Requirements

* **Assumptions**

  * **ASSUM Validation Lifecycle Summary**

    | ID | Title | Status | Validation Method | Timing | Owner | If Invalidated | CON Cross-Ref |
    |:---|:------|:-------|:------------------|:-------|:------|:---------------|:--------------|
    | — | — | — | — | — | — | — | — |

  * **T104C-ASSUM-001** —

* **Constraints**
  * **T104C-CON-001** —

* **Quality Goals**
  * **T104C-QG-001** —

* **Dependencies**
  * **T104C-DEP-001** —

* **Interfaces**
  * **T104C-IF-001** —

##### vii. Epic Standards

| STD ID | Title | Status | Owner | Effective | Supersedes | Adopts | Verification | Reference |
|:-------|:------|:-------|:------|:----------|:-----------|:-------|:-------------|:----------|

* **T104C-STD-001** —
  - **Minimum Viable Conformance**:
    1) —
    2) —

##### viii. Epic Development Guidances

* **Implementation Guidance**
  * **T104C-IG-001** —

* **Integration Guidance**
  * **T104C-INT-001** —

**Research**

| Research ID | Title | Summary | Reference | Brief | Report |
| :--- | :--- | :--- | :--- | :--- | :--- |

**Notes**
*   **2026-01-27**: Initial dossier scaffold created.

**Issues**
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Resolution Notes | Resolution Date |
|:---|:------|:------------|:------|:-------|:---------|:--------------|:-----------------|:----------------|

**Risks**
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Mitigation Notes | Mitigation Date |
|:---|:------|:------------|:------|:-------|:---------|:--------------|:-----------------|:----------------|

---

#### 4. `T104D` Epic: `ANALYSIS` - Analysis Standardization

```yaml
epic_id: 'T104D'
epic_code: 'ANALYSIS'
epic_title: 'Analysis Standardization'
epic_type: 'existing'
epic_status: 'draft'
epic_owner: 'LLM_Consultant'
```

##### i. Purpose
To standardize the **Analysis** artifact (`analysis_...`) as the synthesis bridge between raw research (`Brief`/`Report`) and actionable proposals (`Proposal`). This Epic ensures that research findings are not just "filed away" but are actively synthesized into consultant recommendations, architectural options, and trade-off assessments. It provides the "proof of work" and rationale that underpins subsequent Proposals.

##### ii. Scope

*   **In Scope:**
    *   Defining the Analysis template structure (Executive Summary, Findings Synthesis, Options, Recommendation).
    *   Standardizing the Analysis file naming convention (`analysis_<task>_<id>.md`).
    *   Establishing the linking pattern from `Research Report` -> `Analysis` -> `Proposal`.
*   **Out of Scope:**
    *   **Decision Authority:** The Analysis MUST NOT be treated as the final decision record (decisions belong in `SSOT` or `Client` approval).
    *   **Raw Data:** The Analysis MUST NOT contain raw research data (use `Research Report`).

##### iii. Inherited Considerations

| Source Artifact | Source ID | Category | Inherited Rule IDs |
| :-------------- | :-------- | :------- | :----------------- |
| — | — | — | — |

##### iv. Governance & Roadmap

**Scope & Ownership**
- Owner: —
- Decision Owner: —
- Support: —
- Org baseline (RACI): —

**Phase & Gates**
| Phase | Title | Intent | Key Exit Milestone | Duration Band | Gate Approver (A) | Phase Lead (R) | Plan Link |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

**References**
- —

##### v. Feature Register

| ID | Code | Title | Purpose | Feature Lead (R) | Status | Canonical Link (Request) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |

##### vi. Epic Requirements

* **Assumptions**

  * **ASSUM Validation Lifecycle Summary**

    | ID | Title | Status | Validation Method | Timing | Owner | If Invalidated | CON Cross-Ref |
    |:---|:------|:-------|:------------------|:-------|:------|:---------------|:--------------|
    | — | — | — | — | — | — | — | — |

  * **T104D-ASSUM-001** —

* **Constraints**
  * **T104D-CON-001** —

* **Quality Goals**
  * **T104D-QG-001** —

* **Dependencies**
  * **T104D-DEP-001** —

* **Interfaces**
  * **T104D-IF-001** —

##### vii. Epic Standards

| STD ID | Title | Status | Owner | Effective | Supersedes | Adopts | Verification | Reference |
|:-------|:------|:-------|:------|:----------|:-----------|:-------|:-------------|:----------|

* **T104D-STD-001** —
  - **Minimum Viable Conformance**:
    1) —
    2) —

##### viii. Epic Development Guidances

* **Implementation Guidance**
  * **T104D-IG-001** —

* **Integration Guidance**
  * **T104D-INT-001** —

**Research**

| Research ID | Title | Summary | Reference | Brief | Report |
| :--- | :--- | :--- | :--- | :--- | :--- |

**Notes**
*   **2026-01-27**: Initial dossier scaffold created.

**Issues**
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Resolution Notes | Resolution Date |
|:---|:------|:------------|:------|:-------|:---------|:--------------|:-----------------|:----------------|

**Risks**
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Mitigation Notes | Mitigation Date |
|:---|:------|:------------|:------|:-------|:---------|:--------------|:-----------------|:----------------|

---

#### 5. `T104E` Epic: `CHANGELOG` - Changelog Standardization

```yaml
epic_id: 'T104E'
epic_code: 'CHANGELOG'
epic_title: 'Changelog Standardization'
epic_type: 'existing'
epic_status: 'draft'
epic_owner: 'LLM_Consultant'
```

##### i. Purpose
To standardize the **Changelog** artifact (`changelog_...`) as a separate, delta-only record for tracking version history and material changes to workspace artifacts. This Epic aims to keep primary documents (like Roadmaps and SSOTs) clean and readable by offloading historical version data. It ensures that every major artifact has a clear, auditable history without cluttering the "current state" view.

##### ii. Scope

*   **In Scope:**
    *   Defining the Changelog schema (Version, Date, Type, Summary).
    *   Standardizing the Changelog file naming convention (`changelog_<artifact_name>.md`).
    *   Defining the "Define-Only" constraint (no retroactive mass migration in Phase 0).
*   **Out of Scope:**
    *   **Session Notes:** The Changelog MUST NOT contain meeting notes or rationale (use `Notes`).
    *   **Embedded Logs:** The Changelog MUST NOT be embedded within the source file (except as a link or brief summary).

##### iii. Inherited Considerations

| Source Artifact | Source ID | Category | Inherited Rule IDs |
| :-------------- | :-------- | :------- | :----------------- |
| — | — | — | — |

##### iv. Governance & Roadmap

**Scope & Ownership**
- Owner: —
- Decision Owner: —
- Support: —
- Org baseline (RACI): —

**Phase & Gates**
| Phase | Title | Intent | Key Exit Milestone | Duration Band | Gate Approver (A) | Phase Lead (R) | Plan Link |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

**References**
- —

##### v. Feature Register

| ID | Code | Title | Purpose | Feature Lead (R) | Status | Canonical Link (Request) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |

##### vi. Epic Requirements

* **Assumptions**

  * **ASSUM Validation Lifecycle Summary**

    | ID | Title | Status | Validation Method | Timing | Owner | If Invalidated | CON Cross-Ref |
    |:---|:------|:-------|:------------------|:-------|:------|:---------------|:--------------|
    | — | — | — | — | — | — | — | — |

  * **T104E-ASSUM-001** —

* **Constraints**
  * **T104E-CON-001** —

* **Quality Goals**
  * **T104E-QG-001** —

* **Dependencies**
  * **T104E-DEP-001** —

* **Interfaces**
  * **T104E-IF-001** —

##### vii. Epic Standards

| STD ID | Title | Status | Owner | Effective | Supersedes | Adopts | Verification | Reference |
|:-------|:------|:-------|:------|:----------|:-----------|:-------|:-------------|:----------|

* **T104E-STD-001** —
  - **Minimum Viable Conformance**:
    1) —
    2) —

##### viii. Epic Development Guidances

* **Implementation Guidance**
  * **T104E-IG-001** —

* **Integration Guidance**
  * **T104E-INT-001** —

**Research**

| Research ID | Title | Summary | Reference | Brief | Report |
| :--- | :--- | :--- | :--- | :--- | :--- |

**Notes**
*   **2026-01-27**: Initial dossier scaffold created.

**Issues**
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Resolution Notes | Resolution Date |
|:---|:------|:------------|:------|:-------|:---------|:--------------|:-----------------|:----------------|

**Risks**
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Mitigation Notes | Mitigation Date |
|:---|:------|:------------|:------|:-------|:---------|:--------------|:-----------------|:----------------|

---

#### 6. `T104F` Epic: `PLAN` - Plan Standardization

```yaml
epic_id: 'T104F'
epic_code: 'PLAN'
epic_title: 'Plan Standardization'
epic_type: 'new'
epic_status: 'draft'
epic_owner: 'LLM_Consultant'
```

##### i. Purpose
To standardize the **PLAN** artifact (`plan_...`) as the execution-level workflow tool that holds detailed coordination within a bounded scope (Phase/Stream/Activity), while keeping the Master ROADMAP thin and pointer-based.

##### ii. Scope

*   **In Scope:**
    *   Defining `artifact_type: PLAN` and its allowed `planning_level` values: `PHASE`, `STREAM`, `ACTIVITY`.
    *   Standardizing the `plan_...` prefix and canonical plan directory locations (forward-only for new plan content).
    *   Defining the minimum PLAN contract: required registers (where applicable), Activity section fields, and link integrity requirements.
*   **Out of Scope:**
    *   **Legacy Migrations:** No retroactive bulk renames or conversions of legacy plan/roadmap files outside the T104 initiative Phase 0 refactor scope.

##### iii. Inherited Considerations

| Source Artifact | Source ID | Category | Inherited Rule IDs |
| :-------------- | :-------- | :------- | :----------------- |
| — | — | — | — |

##### iv. Governance & Roadmap

**Scope & Ownership**
- Owner: —
- Decision Owner: —
- Support: —
- Org baseline (RACI): —

**Phase & Gates**
| Phase | Title | Intent | Key Exit Milestone | Duration Band | Gate Approver (A) | Phase Lead (R) | Plan Link |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

**References**
- —

##### v. Feature Register

| ID | Code | Title | Purpose | Feature Lead (R) | Status | Canonical Link (Request) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |

##### vi. Epic Requirements

* **Assumptions**

  * **ASSUM Validation Lifecycle Summary**

    | ID | Title | Status | Validation Method | Timing | Owner | If Invalidated | CON Cross-Ref |
    |:---|:------|:-------|:------------------|:-------|:------|:---------------|:--------------|
    | — | — | — | — | — | — | — | — |

  * **T104F-ASSUM-001** —

* **Constraints**
  * **T104F-CON-001** —

* **Quality Goals**
  * **T104F-QG-001** —

* **Dependencies**
  * **T104F-DEP-001** —

* **Interfaces**
  * **T104F-IF-001** —

##### vii. Epic Standards

| STD ID | Title | Status | Owner | Effective | Supersedes | Adopts | Verification | Reference |
|:-------|:------|:-------|:------|:----------|:-----------|:-------|:-------------|:----------|

* **T104F-STD-001** —
  - **Minimum Viable Conformance**:
    1) —
    2) —

##### viii. Epic Development Guidances

* **Implementation Guidance**
  * **T104F-IG-001** —

* **Integration Guidance**
  * **T104F-INT-001** —

**Research**

| Research ID | Title | Summary | Reference | Brief | Report |
| :--- | :--- | :--- | :--- | :--- | :--- |

**Notes**
*   **2026-01-29**: Epic scaffold added (T104F introduced).

**Issues**
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Resolution Notes | Resolution Date |
|:---|:------|:------------|:------|:-------|:---------|:--------------|:-----------------|:----------------|

**Risks**
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Mitigation Notes | Mitigation Date |
|:---|:------|:------------|:------|:-------|:---------|:--------------|:-----------------|:----------------|

---

#### 7. `T104G` Epic: `COMMUNICATION` - Communication Standardization

```yaml
epic_id: 'T104G'
epic_code: 'COMMUNICATION'
epic_title: 'Communication Standardization'
epic_type: 'new'
epic_status: 'draft'
epic_owner: 'LLM_Consultant'
```

##### i. Purpose
* —

##### ii. Scope

* **In Scope:**
  * —

* **Out of Scope:**
  * —

##### iii. Inherited Considerations

| Source Artifact | Source ID | Category | Inherited Rule IDs |
| :-------------- | :-------- | :------- | :----------------- |
| — | — | — | — |

##### iv. Governance & Roadmap

**Scope & Ownership**
- Owner: —
- Decision Owner: —
- Support: —
- Org baseline (RACI): —

**Phase & Gates**
| Phase | Title | Intent | Key Exit Milestone | Duration Band | Gate Approver (A) | Phase Lead (R) | Plan Link |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

**References**
- —

##### v. Feature Register

| ID | Code | Title | Purpose | Feature Lead (R) | Status | Canonical Link (Request) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |

##### vi. Epic Requirements

* **Assumptions**

  * **ASSUM Validation Lifecycle Summary**

    | ID | Title | Status | Validation Method | Timing | Owner | If Invalidated | CON Cross-Ref |
    |:---|:------|:-------|:------------------|:-------|:------|:---------------|:--------------|
    | — | — | — | — | — | — | — | — |

  * **T104G-ASSUM-001** —

* **Constraints**
  * **T104G-CON-001** —

* **Quality Goals**
  * **T104G-QG-001** —

* **Dependencies**
  * **T104G-DEP-001** —

* **Interfaces**
  * **T104G-IF-001** —

##### vii. Epic Standards

| STD ID | Title | Status | Owner | Effective | Supersedes | Adopts | Verification | Reference |
|:-------|:------|:-------|:------|:----------|:-----------|:-------|:-------------|:----------|

* **T104G-STD-001** —
  - **Minimum Viable Conformance**:
    1) —
    2) —

##### viii. Epic Development Guidances

* **Implementation Guidance**
  * **T104G-IG-001** —

* **Integration Guidance**
  * **T104G-INT-001** —

**Research**

| Research ID | Title | Summary | Reference | Brief | Report |
| :--- | :--- | :--- | :--- | :--- | :--- |

**Notes**
* —

**Issues**
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Resolution Notes | Resolution Date |
|:---|:------|:------------|:------|:-------|:---------|:--------------|:-----------------|:----------------|

**Risks**
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Mitigation Notes | Mitigation Date |
|:---|:------|:------------|:------|:-------|:---------|:--------------|:-----------------|:----------------|

---

### D. Project Glossary
*   **Workflow Tool**: An artifact used to manage the process of work (e.g., Roadmap, Notes), as opposed to defining the product (SSOT).
*   **SSOT Artifact**: An artifact that defines the authoritative state of the product or governance (e.g., SPS, Request, Concept).

---

## IV. GLOSSARY
<!-- Placeholder -->

---

## V. APPENDIX
<!-- Placeholder -->

---

## VI. VALIDATION CHECKLIST
- [ ] The artifact's YAML header is complete and syntactically correct.
- [ ] The Problem Definition (Section III-A) has received explicit client approval.
- [ ] All known open issues and risks have been logged in Section III-D.
- [ ] The 'Next Steps' section clearly defines the handoff to the Request workflow.

---

## VII. STAKEHOLDER SIGN-OFF
<!-- Placeholder -->

---

## VIII. NEXT STEPS
<!-- Placeholder -->

---

## IX. CHANGELOG
*   **v1.0.0**: Initial scaffolding created.
*   **v1.0.1**: TK006 SPS compliance remediation (ADR-007 enums/coupling, ADR-009 STD index schema, external references, traceability links).
