---
artifact_type: 'SPS'
initiative_id: 'T102'
initiative_code: 'CDW'
version: '1.1.0'
date: '2025-08-16'
status: 'review'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
---

# SYNTHESIZED PROBLEM STATEMENT (SPS): Consultancy Development Workflow - T102

## I. EXECUTIVE SUMMARY

## II. TABLE OF CONTENTS
I. [Executive Summary](#i-executive-summary)
II. [Table of Contents](#ii-table-of-contents)
III. [Core Content](#iii-core-content)
    A. [Problem Definition](#a-problem-definition)
    B. [Key Specifications & Requirements](#b-key-specifications--requirements)
    C. [Governance & Assumptions](#c-governance--assumptions)
    D. [Open Issues & Risks](#d-open-issues--risks)
  E. [Exploratory Notes & Parking Lot](#e-exploratory-notes--parking-lot)
    F. [Project Glossary](#f-project-glossary)
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
The current system lacks a formalized, end-to-end workflow for transforming a client's raw, ambiguous idea into a set of validated, high-level solution concepts ready for architectural design. The existing `SPS` (exploratory) and `Request` (structured) artifacts were designed in isolation, creating operational friction, traceability gaps, and no clear path to solutioning. This forces the `LLM_Consultant` to perform poorly when asked to design concept-level solutions directly from an `SPS`, as there is no intermediate step to ground the problem in project reality or a final artifact to document the proposed solution concepts.

#### 2. The Desired Outcome
<!-- To implement a robust, three-stage consultancy workflow (`SPS` → `Request` → `Concept`) supported by a suite of integrated templates and procedural guidelines. This system will:

> [DISCREPANCY-WORKFLOW] Specifies a sequential flow ending in Concept. Align to "SPS → Request → Design" with Concept as a parallel, ongoing process across stages.
1.  Preserve the distinct philosophies of `SPS` (unconstrained problem exploration) and `Request` (grounded requirements analysis).
2.  Introduce a new `Concept` artifact to systematically explore and document high-level solutions.
3.  Ensure seamless, traceable, and partially-automated handoffs between each stage.
4.  Effectively manage LLM context windows and align with industry standards for requirements engineering.
5.  **Establish a robust Inheritance Model** to ensure clear, reference-based traceability across all artifacts. -->

#### 3. Business Case


### B. Initiative Considerations

<!-- This section contains governance factors that apply to ALL epics above, organized per industry standards (PRINCE2 PID, ISO 29148, BABOK v3). -->

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
<!-- Factors believed to be true but not yet confirmed. Can be adjustable but carry risk. Per BABOK v3 and ISO 29148, these represent unverified beliefs that inform our approach but carry risk if proven false. -->
- **T102-ASSUM-001 (LLM Generation)** — In v1, the **LLM_Consultant** acts as the generator for all artifacts as outputs with structural templates as inputs (no external automation required) during consultations. 
- **T102-ASSUM-002 (Template Adoption)** — Non-technical stakeholders will successfully adopt markdown/YAML toolchain for collaborative authoring


#### 3. Project Constraints
<!-- Non-negotiable restrictions or limitations on possible solutions. Per ISO 29148, these are boundaries that must be respected and cannot be changed within project scope. -->
* **T102-CON-001 (Format Requirements)** All artifacts SHALL remain Markdown files with YAML frontmatter; common editors/viewers are sufficient for authoring/review.
* **T102-CON-002 (Scope Limitation)** — No automation priority in v1; prioritize setting up workflows and standards first. 
* **T102-CON-003 (Documentation Standards)** — Follow `prompt_main.md` and `general.md` for template versioning, global structure and format; maintain change logs for traceability.
* **T102-CON-004 (No-Formal-Planning)** — This initiative SHALL NOT develop detailed project development plans, formal documentation artifacts, budget tracking, or timeline management systems; scope and quality are primary success criteria while cost/schedule considerations are deferred to external PM tools (ticktick) for operational tracking only.
* **T102-CON-005 (Changelog Separation)** — Changelog data SHALL NOT be embedded within source artifact files. Version history SHALL be maintained in dedicated changelog surfaces (e.g., changelog_<artifact>.md files or equivalent external mechanisms), linked from the source artifact. This constraint enables clean artifact readability, supports automated changelog tooling, and prevents drift between embedded and authoritative version records.
  External Reference: `T104-CON-005 (No Embedded Changelogs)` 

* **T102-CON-009 (Normative Keywords)** — Normative requirement keywords (MUST/SHALL/SHOULD/MAY) SHALL be interpreted per RFC 2119 and MUST be written in UPPERCASE to carry normative meaning.

#### 4. Success Criteria & Quality Goals
<!-- Measurable targets that define project success. Per ISO 29148, these must be verifiable, singular, and complete with clear success/failure criteria. -->
* **T102-QG-001 (Client Readability)** — Artifacts are understandable by non-technical stakeholders (aim ≥ "clear" on internal rubric).
* **T102-QG-002 (End-to-End Traceability)** — Every option/decision maps forward/backward across artifacts and into Planner hand-off.
* **T102-QG-003 (Low-Disruption Implementation)** — Prefer changes that minimize author retraining and document churn in v1; reserve stricter automation for v2.

#### 5. Dependencies 
<!-- External prerequisites and commitments. -->
* **T102-DEP-001 (Client Engagement)** — Client must provide decision-making commitment within 2-business-day Service Level Agreement (SLA) across all workflow gates
* **T102-DEP-002 (Planner Integration)** — Downstream LLM_Planner system must be capable of consuming standardized handoff schema
* **T102-DEP-003 (Role Definitions)** — Program-wide LLM role definitions (Consultant, Planner, Developer, Reviewer) SHALL be defined and maintained in `prompt/documentation/main/prompt_main.md` Section 3 ("Role Definitions"). All initiatives adopting the T102 consultancy workflow model SHALL reference this authoritative role catalog for:
- Role naming conventions
- Responsibility boundaries (RACI-style)
- Input/output contracts per role
- Escalation and handoff protocols

#### 6. Interfaces
<!-- Governance-level role/process touchpoints -->
* **T102-IF-001 (Planner Handoff)** — Consultancy Layer delivers an approved, minimal handoff bundle at the defined gate; Planner Layer acknowledges receipt and assumes ownership for planning. Payload fields and evidence are defined in dedicated workflows and artifact.
* **T102-IF-002 (Client Review)** — Client is the decision owner at gates; expected turnaround ≤ 2 business days; approval signals are recorded in the artifact per governance rules.
* **T102-IF-003 (Roles Collaboration)** — Defines Consultant–Planner relationship and how clarification is requested, response channels, and the boundary of change ownership post-handoff following `T102-DEP-003`.
* **T102-IF-004 (Co-authoring Consultancy)** — Client and Consultant co-author all Consultancy Layers workflows and documents. Define the working channels, meeting rhythm, who edits vs approves, and that the repo is the source of truth.

#### 7. Project Standards
<!-- Provide a single, auditable index of initiative-level standards that govern the initiative. -->

| STD ID | Title | Status | Owner | Effective | Supersedes | Adopts | Verification | Reference |
|:-------|:----------|:-------|:------|:----------|:-----------|:-------------------------|:------------|:----------|
| `T102-STD-001` | **Operating Model Standard** | `Proposed` | Client | — | `T102-GDR-001` | `T102-ADR-001 (Consultancy Operating Model)` | CI/Lint + Review MUST verify: workflow sequencing, authority/ownership rules, and approval gates align to the adopted spec. | `T102-STD-009 (Governance Standards Model)` |
| `T102-STD-002` | **Canonical Header Standard** | `Proposed` | Client | — | `T102-GDR-002` | `T102-ADR-002 (Canonical YAML Header)` | CI/Lint + Review MUST verify: artifact YAML headers conform to the adopted schema across SPS/Request/Concept/Design. | `T102-STD-009 (Governance Standards Model)` |
| `T102-STD-003` | **Inheritance Model Standard** | `Proposed` | Client | — | `T102-GDR-003` | `T102-ADR-003 (Explicit Inheritance Model)` | CI/Lint + Review MUST verify: explicit inheritance tables/ID references and variance handling conform to the adopted spec. | `T102-STD-009 (Governance Standards Model)` |
| `T102-STD-004` | **Decision Records Standard** | `Proposed` | Client | — | `T102-GDR-004` | `T102-ADR-004 (Decision Records Index)` | CI/Lint + Review MUST verify: correct index schemas, required body subheadings, and valid authority citations per adopted spec. | `T102-STD-009 (Governance Standards Model)` |
| `T102-STD-005` | **ID Governance Standard** | `Proposed` | Client | — | `T102-GDR-005` | `T102-ADR-005 (ID Specification & Rules)` | CI/Lint + Review MUST verify: valid IDs/tokens per adopted spec, correct formal vs. shorthand reference usage, and RFC2119 keyword constraints via `T102-CON-009`. | `T102-STD-009 (Governance Standards Model)`, `T102-CON-009 (Normative Keywords)` |
| `T102-STD-006` | **Research Workflow Standard** | `Proposed` | Client | — | `T102-GDR-006` | `T102-ADR-006 (Research Artifacts Index)` | CI/Lint + Review MUST verify: brief/report gating, indexing/traceability rules, and integration placement conform to the adopted spec. | `T102-STD-009 (Governance Standards Model)` |
| `T102-STD-007` | **LLM Quality Control** | `Proposed` | Client | — | `T102-GDR-007` | — | CI/Lint + Review MUST verify: source verification, human-in-the-loop review, traceability/logging, and disclosure safeguards are present per the standard (adopted spec intentionally deferred during migration). | `T102-STD-009 (Governance Standards Model)` |
| `T102-STD-008` | **Organisation Baseline Standard** | `Proposed` | Client | — | `T102-GDR-008` | `T102-ADR-008 (Organisation Baseline Standard)` | CI/Lint + Review MUST verify: a single initiative-level organisation baseline exists with stable actor-to-role mapping and governance ownership. | `T102-STD-009 (Governance Standards Model)` |
| `T102-STD-009` | **Governance Standards Model** | `Proposed` | Client | — | — | `T102-ADR-009 (Governance Standards Specification)` | CI/Lint + Review MUST verify: required STD fields, valid `Adopts`, and RFC2119 keyword constraint via `T102-CON-009`. | `T102-STD-005 (ID Governance Standard)`, `T102-CON-009 (Normative Keywords)` |


* **T102-STD-001 (Operating Model Standard)** — The project SHALL follow the consultancy operating model, approval gates, and decision precedence defined in the adopted normative specification.
  - **Minimum Viable Conformance**:
    1) SPS is governance-only and establishes initiative/epic governance boundaries (`T102-ADR-001-CLAUSE-001`).
    2) Request is requirements-only and MUST NOT embed decision records (`T102-ADR-001-CLAUSE-002`).
    3) Concept is the architecture decision workspace/ADR compendium (`T102-ADR-001-CLAUSE-003`).
    4) Design captures story-level decisions and records variances when deviating (`T102-ADR-001-CLAUSE-004`).

* **T102-STD-002 (Canonical Header Standard)** — All artifacts SHALL include a canonical YAML header that conforms to the adopted normative specification.
  - **Minimum Viable Conformance**:
    1) Use only the canonical header key set (and required scope keys when applicable) (`T102-ADR-002-CLAUSE-001`).
    2) Enforce canonical formats/enums for header values (e.g., IDs, status, dates, versions) (`T102-ADR-002-CLAUSE-002`).
    3) Provide canonical schema examples/reference as required (`T102-ADR-002-CLAUSE-003`).

* **T102-STD-003 (Inheritance Model Standard)** — Downstream artifacts SHALL implement explicit inheritance by ID referencing and variance handling as defined in the adopted normative specification.
  - **Minimum Viable Conformance**:
    1) Include the Inherited Considerations table using the required schema/columns (`T102-ADR-003-CLAUSE-001`).
    2) Follow precedence and document deviations as local variance ADRs (`T102-ADR-003-CLAUSE-002`).
    3) Apply delta-only authoring rules (do not restate upstream text; emphasize ≤5 critical inherited IDs) (`T102-ADR-003-CLAUSE-003`).

* **T102-STD-004 (Decision Records Standard)** — The project SHALL use the unified decision record index schemas, body templates, and linking rules defined in the adopted normative specification.
  - **Minimum Viable Conformance**:
    1) Use the standardized DR index schemas (GDR/ADR) and column definitions (`T102-ADR-004-CLAUSE-001`).
    2) Follow placement standards for DR indices across artifact families (`T102-ADR-004-CLAUSE-002`).
    3) Create/update DR entries using the defined workflow and body template (`T102-ADR-004-CLAUSE-003`, `T102-ADR-004-CLAUSE-004`).
    4) Maintain stable anchors per the anchor stability rules (`T102-ADR-004-CLAUSE-007`).

* **T102-STD-005 (ID Governance Standard)** — The project SHALL use the canonical ID schema, token taxonomy, and reference semantics defined in the adopted normative specification.
  - **Minimum Viable Conformance**:
    1) IDs MUST conform to the canonical schema and formatting rules (`T102-ADR-005-CLAUSE-001`).
    2) Tokens, taxonomy, and allowed scope usage MUST follow the canonical table (`T102-ADR-005-CLAUSE-002`).
    3) Precedence, inheritance directionality, and variance requirements MUST be followed (`T102-ADR-005-CLAUSE-003`).
    4) Formal vs shorthand reference usage MUST follow the reference semantics rules (`T102-ADR-005-CLAUSE-004`).

* **T102-STD-006 (Research Workflow Standard)** — Formal research artifacts SHALL be indexed and referenced using the Research Artifacts Index architecture defined in the adopted normative specification.
  - **Minimum Viable Conformance**:
    1) Use the `RES-###` ID pattern integration rules (`T102-ADR-006-CLAUSE-001`).
    2) Maintain the required research table schemas (local + Concept aggregation) (`T102-ADR-006-CLAUSE-002`).
    3) Apply placement decision criteria for inline vs indexed vs external research (`T102-ADR-006-CLAUSE-003`).
    4) Follow the index maintenance protocol (`T102-ADR-006-CLAUSE-004`).
    5) Reference research findings by `RES-###` IDs (link-don’t-duplicate) (`T102-ADR-006-CLAUSE-005`).

* **T102-STD-007 (LLM Quality Control)** — Any LLM-generated factual claims integrated into governance artifacts SHALL be validated using mandatory quality control safeguards (adopted canonical spec intentionally deferred during migration).
  - **Minimum Viable Conformance**:
    1) Verify factual claims against authoritative sources; unverified claims are excluded or clearly labeled as conjecture.
    2) Require human-in-the-loop review prior to governance integration, with an accountable named owner.
    3) Maintain traceability/logging for LLM usage (inputs, outputs, and methodology metadata) sufficient for auditability.
    4) Disclose LLM usage and enforce a rule that no governance obligation is accepted on LLM-only evidence without validation.
    5) Define escalation triggers for high-risk domains (e.g., legal/regulatory) requiring appropriate human expertise.

* **T102-STD-008 (Organisation Baseline Standard)** — The project SHALL maintain a single initiative-level organisation baseline with stable actor-to-role mapping and governance RACI as defined in the adopted normative specification.
  - **Minimum Viable Conformance**:
    1) Maintain canonical placement of the organisation baseline in the initiative SPS (`T102-ADR-008-CLAUSE-001`).
    2) Include the required Role Definitions table and Governance RACI using the mandated schemas (`T102-ADR-008-CLAUSE-002`).
    3) Follow the maintenance policy to avoid drift and unnecessary churn (`T102-ADR-008-CLAUSE-003`).

* **T102-STD-009 (Governance Standards Model)** — The project SHALL use `STD` as the authoritative registry token for enforceable standards, replacing `GDR`. Each `STD` item MUST: 
  (a) state a concise obligation and 
  (b) declare exactly one adopted canonical normative specification that contains the detailed rules. Rationale, trade-offs, and alternatives MUST be captured in `ADR` records, not inside `STD` bodies. 
  - **Minimum Viable Conformance**:
    1) `STD` semantics and scope MUST follow the defined token rules (`T102-ADR-009-CLAUSE-001`).
    2) `STD` adoption contract MUST be enforced (single canonical adopted spec) (`T102-ADR-009-CLAUSE-002`).
    3) `STD` precedence and variance requirements MUST be applied (`T102-ADR-009-CLAUSE-003`).
    4) `STD` index schema and authoring guidelines MUST be followed (`T102-ADR-009-CLAUSE-004`).
    5) Migration tolerance MUST be applied as specified (`T102-ADR-009-CLAUSE-005`).

#### 8. Project Guidances & Notes
<!-- Technical guidance for execution teams -->

* **Implementation Guidance**
  * **T102-IG-001 (Comment Blocks)** — All structural templates should include markdown explanatory comments with industry standard references for section and subsections definitions.
  * **T102-IG-002 (Asset Management)** — Maintain consistent file paths under `prompt/templates/consultant/*` with canonical repo referencing.
  * **T102-IG-003 (Metadata Architecture)** — *Standard* docs keep **body metadata**; *Artifact* docs (SPS, Request, Concept) use **YAML header**.
  * **T102-IG-004 (Integration Testing)** — Verify each template change with downstream artifact compatibility before release.
  * **T102-IG-005 (Canonical Header)** — All artifacts should use the same identity/governance header keys & enums.
  * **T102-IG-006 (Markdown Heading Terminology)** — Markdown heading levels SHALL follow standardized terminology across all consultancy artifacts: Title (#), Major Section (##), Main Section (###), Subsections (####), Subheadings (#####). Canonical definitions maintained in `general.md` for cross-repo consistency per `T102-CON-003`
  * **T102-IG-007 (ID Standard)** — Initiative/Epic/Feature/Story IDs follow agreed standardized ID patterns and terminology for traceability.
  * **T102-IG-008 (Decision Logging)** — Governance decisions (policy/authority) logged as GDRs in stable governance document; architecture/implementation decisions logged as ADRs in a dynamic workspace document. 
  * **T102-IG-009 (Traceability Framework)** — Use **42010** viewpoints (document architecture; workflow/hand-off) to maintain traceability across workflows and their corresponding artifacts.
  * **T102-IG-010 (Inheritance Model)** — A formal inheritance model must be defined to ensure lower-level scopes such as **Epics, Features and Stories** from downstream artifacts can explicitly reference and inherit governance from higher-level scope such as Initiative Rules from upstream artifact, moving beyond the current 'delta-only' approach.

* **Notes**
  * **T102-NOTE-001 (Architectural Philosophy)** — The artifact workflow is a deliberate implementation of the Double Diamond design model. The consultancy layer is structured around three stable document types, sequenced for clarity and control, and supported by a dynamic workspace that contextualizes decisions across all project scopes:

  1. **Governance Document:** Establishes initiative- and epic-level objectives, policies, and scope boundaries.
  2. **Specification Document:** Captures feature-level requirements and acceptance criteria derived from governance.
  3. **Design Description:** Documents story-level intent and solution requirements to enable delivery.

  In parallel, a **dynamic workspace** continuously aggregates exploration, decisions, and linkages across all project-management scopes. This workspace maintains coherence and traceability without introducing additional approval gates. The workflow sequence is governance → specification → design description, with the dynamic workspace operating continuously to inform and connect the stable documents.

  * **T102-NOTE-002 (Agent Compatibility)** — Claude Code & Agentic CLI environment constraints favor focused, well-structured documents over large, complex artifacts. This technical reality reinforces the philosophical preference for separate but linked workflows.

  * **T102-NOTE-003 (Industry Standards)** — The proposed architecture aligns with established industry frameworks and standards, which should be used as a reference during implementation:
    - **Design Council:** The Double Diamond Model (Discover/Define → Develop/Deliver).
    - **ISO/IEC/IEEE 42010:** Architecture descriptions (stakeholder concerns, viewpoints, architecture frameworks).
    - **IEEE 1016:** Software design descriptions (design viewpoints, stakeholder concerns, design view organization).
    - **ISO/IEC/IEEE 29148:** Requirements Engineering (for traceability and change control).
    - **IIBA BABOK v3:** Separation of Elicitation & Collaboration vs. Requirements Analysis.
    - **SAFe:** Hierarchy mapping from Feature Hypothesis (≈SPS) to Capability/Feature (≈Request).
    - **ISO/IEC/IEEE 24765, IEEE Std 15288 & 12207, INCOSE Requirements Management Primer:** For consistent terminology, lifecycle alignment, and change-impact templates.

  * **T102-NOTE-004 (Inheritance Model Philosophy)** — The "Explicit ID Referencing" model is built on the principle of **"Implicit Inheritance, Explicit Emphasis."** This means that while all governance rules are automatically inherited downstream, authors are required to explicitly list the most contextually critical rules in the `Inherited Considerations` table. This approach strikes a deliberate balance: it avoids the ambiguity of a purely instructional model and the verbosity of having to list every single inherited ID. By using keyword hints instead of full descriptions, it enhances author readability and context without creating duplicate content or risking informational drift from the single source of truth in the parent artifact.

#### 9. Research 

| Research ID | Title | Summary | Reference | Brief | Report |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `T102-RES-001` | **Research Integration Workflow** | Established three-tier placement strategy, LLM quality control framework, RES-### ID system; recommended dedicated Epic T102E for implementation | `T102-ISSUE-005`, `T102-GDR-006`, `T102-GDR-007` | [brief](../research/brief/brief_T102-CONSULTANT_research-integration-workflow.md) | [report](../research/report/report_T102-CONSULTANT_research-integration-workflow.md) |
| `T102-RES-002` | **Roadmap Viability** | Confirmed governance snapshot approach aligns with PRINCE2/PMI/SAFe standards; validated hybrid model with governance milestones in SPS and operational plans external | `T102A-GDR-001`, `T102C-GDR-003`, `T102C-GDR-005` | [brief](../research/brief/brief_T102-CONSULTANT_roadmap-viability.md) | [report](../research/report/report_T102-CONSULTANT_roadmap-viability.md) |
| `T102-RES-003` | **Initiative Status Assessment** | Assessed initiative status, bottlenecks, and documentation debt; identified YAML/header and register integrity gaps requiring follow-on hygiene work | `T102-GDR-002`, `T102-ISSUE-005` | [brief](../research/brief/brief_T102-RES-003_initiative-status-assessment.md) | [report](../research/report/report_T102-RES-003_initiative-status-assessment.md) |


#### 10. Issues & Risks
<!-- Use this log to track items requiring action or monitoring. -->

**Issues**
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Resolution Notes | Resolution Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `T102-ISSUE-001` | Planner Handoff Schema | Define a canonical Planner hand-off schema and handoff protocol to the Detailed Design & Planning layer (selected option, per-story `ready_to_plan`, GDR list, asset refs). | Client | `OPEN` | `MEDIUM` | 2025-10-05 | — | — |
| `T102-ISSUE-002` | Central Header Reference | Publish a central header reference (v1.0.0) in one repo location and link all templates to it. | Client | `OPEN` | `MEDIUM` | 2025-10-05 | — | — |
| `T102-ISSUE-003` | Multi-Rater Scoring Policy | Finalize multi-rater scoring policy write-up (criteria rationales, tie-break rule) for reuse across epics. | Client | `OPEN` | `MEDIUM` | 2025-10-05 | — | — |
| `T102-ISSUE-004` | IDs Promotion Protocol | Define process for promoting IDs to higher PM scope level across workflows in Consultancy Layers.  | Client | `OPEN` | `MEDIUM` | 2025-10-05 | — | — |
| `T102-ISSUE-005` | Research Integration Pattern | Define and standardize the integration of research findings within PID-lite documents through research `T102-RES-001 (Research Integration Workflow)` | Client | `OPEN` | `HIGH` | 2025-10-05 | — | — |
| `T102-ISSUE-006` | Traceability Hygiene | Restore traceability integrity by retrofitting missing YAML headers (11/32 non-archive artifacts) to enable reliable graph navigation and validation. | Client | `OPEN` | `HIGH` | 2026-01-13 | — | — |
| `T102-ISSUE-007` | Register Link Integrity | Resolve “ghost artifacts” and broken register links (register entries pointing to non-existent targets) to restore navigability across SSOT artifacts. | Client | `OPEN` | `MEDIUM` | 2026-01-13 | — | — |

**Risks**
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Mitigation Notes | Mitigation Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `T102-RISK-001` | Divergence Risk | Divergence risk between Standard vs Artifact metadata patterns during rollout. | Client | `MONITORED` | `MEDIUM` | 2025-10-05 | — | — |
| `T102-RISK-002` | Review SLA Slippage | Review SLA slippage (2-day target) could delay gates across epics. | Client | `MONITORED` | `MEDIUM` | 2025-10-05 | — | — |
| `T102-RISK-003` | Architectural Drift | Uncoordinated, story-level design efforts may lead to an incoherent or suboptimal feature architecture if a feature-level framework is not established first. | Client | `MONITORED` | `MEDIUM` | 2025-10-05 | — | — |
| `T102-RISK-004` | Template Migration | Changes to the template/standards may require updates to existing SSOT files or a “grandfathering” policy, otherwise adoption friction and inconsistency may occur. | Client | `MONITORED` | `LOW` | 2026-01-13 | Monitor scope of changes; prefer “grandfather existing, apply to new” policy; track impacts via `T102-RES-003` and `T102B-RES-001`. | — |

### C. Epics & Breakdown

#### 0. Initiative WBS Map
<!-- PURPOSE: A high-level structural index of the project's scope. It shows the hierarchy only and should be kept synchronized with the Epic/Feature sections below. It does not contain operational details like status or owners. -->

| Level | PM Type | ID | Name |
| :--- | :--- | :--- | :--- |
| 1 | Initiative | T102 | Consultancy Layer Architecture |
| 2 | Epic | T102A | SPS Workflow Implementation |
| 3 | Feature | T102A-SPSST | SPS Structural Template |
| 3 | Feature | T102A-SPSPG | SPS Procedural Guideline |
| 3 | Feature | T102A-MANIFEST | SPS Manifest |
| 2 | Epic | T102B | Request Workflow Implementation |
| 3 | Feature | T102B-RST | Request Structural Template |
| 3 | Feature | T102B-RPG | Request Procedural Guideline |
| 3 | Feature | T102B-REQUEST_MANIFEST | Request Manifest |
| 2 | Epic | T102C | Concept Workflow Implementation |
| 3 | Feature | T102C-CST | Concept Structural Template |
| 3 | Feature | T102C-CPG | Concept Procedural Guideline |
| 3 | Feature | T102C-CONCEPT_MANIFEST | Concept Manifest |

---

#### 1. `T102A` Epic: `SPS` - SPS Workflow 
<!-- PURPOSE: This block is a dossier for a major capability. It inherits global rules from Section III-B but adds its own specific scope, goals, and controls. -->

```yaml
epic_id: 'T102A'
epic_code: 'SPS'
epic_title: 'Synthesized Problem Statement Workflow'
epic_type: 'existing'        # new | existing | general
epic_status: 'review'        # draft | review | approved | deprecated
epic_owner: 'LLM_Consultant' # Role or named owner
```

##### i. Purpose
<!-- PURPOSE: State the primary goal and outcome of this Epic in 1-2 paragraphs. -->
To refactor and formalize the **SPS (Synthesized Problem Statement)** artifact and its authoring workflows per the consultancy operating model (`T102-GDR-001`). This Epic will transform the SPS into a robust, client-friendly Project Initiation Document (PID) that establishes initiative and epic-level governance, ensuring clear problem definition, governance traceability, and structured handoffs to the downstream Request workflow.

##### ii. Scope
<!-- PURPOSE: Define the explicit boundaries of this Epic. -->

* **In Scope:**
  *   The **structural template** for the SPS artifact (SPSST) with section definitions, instructional comments, and industry-standard references per `T102-IG-001`.
  *   The **procedural guideline** for authoring an SPS (SPSPG) covering workflow steps, section authoring rules, and validation checklists.
  *   The **versioning and manifest helper** for the SPS (SPS_MANIFEST) supporting template lineage and adoption tracking.
  *   Development and validation using this SPS document (`sps_T102-CONSULTANT.md`) as the working exemplar for all future SPS workflows and artifacts.
* **Out of Scope:**
  *   The structure and process for downstream artifacts: `Request` (T102B), `Concept` (T102C), and `Design` (T102D) workflows.
  *   Validation tooling, template automation, or migration scripts per `T102-CON-002 (Scope Limitation)`.


##### iii. Inherited Considerations

| Source Artifact | Source ID | Category | Inherited Rule IDs |
| :-------------- | :-------- | :------- | :----------------- |
| SPS | T102 | Constraints | `T102-CON-001 (Format Requirements)`, `T102-CON-002 (Scope Limitation)`, `T102-CON-003 (Documentation Standards)` |
| SPS | T102 | Quality Goals | `T102-QG-001 (Client Readability)`, `T102-QG-002 (End-to-End Traceability)`, `T102-QG-003 (Low-Disruption Implementation)` |
| SPS | T102 | Interfaces | `T102-IF-004 (Co-authoring Consultancy)` |
| SPS | T102 | Implementation Guidance | `T102-IG-001 (Comment Blocks)`, `T102-IG-002 (Asset Management)`, `T102-IG-003 (Metadata Architecture)`, `T102-IG-005 (Canonical Header)`, `T102-IG-010 (Inheritance Model)` |
| SPS | T102 | Governance | `T102-GDR-001 (Operating Model Standard)`, `T102-GDR-002 (Canonical Header Standard)`, `T102-GDR-003 (Inheritance Model Standard)`, `T102-GDR-004 (Decision Records Standard)`, `T102-STD-005 (ID Governance Standard)` |

##### iv. Governance & Roadmap

**Scope & Ownership**
- Owner: Epic Lead (`LLM_Consultant`)
- Decision Owner: `Client`
- Support: `LLM_Researcher`, `LLM_Developer`, `LLM_Planner`
- Org baseline (RACI): see `III.B.1 (Organization & Responsibilities)`

**Phase & Gates**
| Phase | Title | Intent | Key Exit Milestone | Duration Band | Gate Approver (A) | Phase Lead (R) | Plan Link |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Foundation | Complete epic definition & baseline establishment | Foundation Readiness: Epic `T102A` approved with stable E-IDs and GDRs; SPSST design baseline complete and validated through iterative consultancy | 2-3w | `Client` | `LLM_Consultant` | — |
| 2 | Template Design | Develop & validate `T102A-SPSST` structural template | Template Validation: SPSST enables functional SPS creation; this document (`sps_T102-CONSULTANT.md`) serves as validated working exemplar | 3-4w | `Client` | `LLM_Consultant` | — |
| 3 | Process Design | Develop `T102A-SPSPG` procedural guideline | Process Usability: SPSPG enables consistent, client-friendly SPS authoring; authoring workflow integrates with downstream Request handoff per `T102-GDR-001` | 2-3w | `Client` | `LLM_Consultant` | — |
| 4 | Integration | Develop `T102A-MANIFEST` & package validation | Package Completeness: MANIFEST enables template versioning, lineage tracking, and adoption measurement; all features pass integration checklist | 1-2w | `Client` | `LLM_Consultant` | — |

**References**
- External PM Tracking: ticktick (client PM tool)

##### v. Feature Register
<!-- [Status ∈ {proposed,in-discovery,in-request,approved,in-concept,in-delivery,done,parked}. Canonical Link = repo-relative Request path.] -->

| ID | Code | Title | Purpose | Feature Lead (R) | Status | Canonical Link (Request) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `T102A1` | `SPSST` | SPS Structural Template | Refactor the core SPS template for clarity & governance. | `LLM_Consultant` | `in-request` | `.../request/request_T102A-SPSST_T102_v1.0.0.md` |
| `T102A2` | `SPSPG` | SPS Procedural Guideline | Define the authoring workflow & controls for the SPS. | `LLM_Consultant` | `proposed` | — |
| `T102A3` | `MANIFEST` | SPS Manifest | Define a helper artifact for versioning and lineage. | `LLM_Consultant` | `proposed` | — |

##### vi. Epic Requirements

* **Assumptions**
  <!-- Factors believed to be true but not yet confirmed. Can be adjustable but carry risk. -->
  * **T102A-ASSUM-001 (Co-author Workflow)** — LLM_Consultant and Client will co-author SPS as outlined in `T102-IF-004`; SPSPG design prioritizes LLM-oriented phase/gate workflow while SPSST focuses on human-oriented linear section structure.


* **Constraints**
  <!-- Non-negotiable restrictions or limitations on possible solutions. -->
  * **T102A-CON-001 (Instructional Dual-Purpose)** — SPSST instructional comments SHALL serve dual purpose: (a) guide human authors with WHAT/WHY context, (b) provide source material for SPSPG HOW extraction. Comment structure must balance readability with extraction clarity per `T102A-IG-001`.
  * **T102A-CON-002 (Validation Mandate)** — SPSST SHALL include Section VI validation checklist organized by section; SPSPG SHALL include validation checklist 
    organized by phase/gate. Checklist content detailed in respective feature Request artifacts.
  * **T102A-CON-003 (Phase-Section Decoupling)** — SPSPG phase/gate workflow MAY deviate from SPSST linear section order to support non-linear consultancy patterns validated by industry best practices (BABOK iterative requirements elaboration, PMI flexible charter authoring, research documented in `T102A-NOTE-006`). Sections may be authored out-of-order per phase requirements using recommended sequence: WHY (Problem/Purpose) → WHAT (Scope/Epics) → HOW (Governance/Approach) → REFINE (Risks/Assumptions).
  * **T102A-CON-004 (Governance Freeze Discipline)** — SPS SHALL establish governance baseline via stakeholder sign-off (Section VII) at end of discovery phase to prevent infinite refinement loop. Post-baseline emergent governance items SHALL follow controlled change process distinguishing Initiative/Epic-level changes (require client-approved SPS version update) from Feature/Story-level items (defer to REQUEST/CONCEPT/DESIGN with explicit traceability to deferred decisions log).


* **Quality Goals**
  <!-- PURPOSE: Define the Epic's specific business objectives and the measurable goals that prove success. -->
  * **T102A-QG-001 (Template Usability)** — A new author can complete the SPS template with less than 30 minutes of external guidance using SPSST structure and SPSPG procedural workflow.
  * **T102A-QG-002 (Version Synchronization)** — SPSST and SPSPG version pairs tracked by MANIFEST ensure no version drift; v1.0 SPS workflows require matching template versions per `T102A-IG-003`.
  * **T102A-QG-003 (Handoff Quality)** — SPS artifacts completed using SPSST/SPSPG meet industry-standard handoff readiness when:
      (a) Approved by decision owner with documented sign-off (name/date per Section VII),
      (b) Contain complete and coherent problem statement, scope, and governance context for REQUEST intake,
      (c) Pass validation checklist with 10 readiness criteria: stakeholder approval, clear objectives & scope, requirements overview, assumptions/constraints documentation, risk identification, stakeholder engagement, governance decisions recorded, quality review completion, version baseline with traceability IDs, and explicit planner acknowledgment of handoff receipt.
  * **T102A-QG-004 (Structural Completeness)** — SPSST structural baseline SHALL include all industry-standard PID-lite sections benchmarked against PRINCE2/PMI frameworks: Problem Definition, Business Case, Stakeholders & Roles, Assumptions/Constraints, Quality Goals, Scope Breakdown (Epics), Governance Decisions, Risks/Issues, and Approval/Sign-off. Section naming and ordering SHALL align with content purpose per research crosswalk analysis.

* **Dependencies**
  <!-- PURPOSE: List items this Epic relies on and contracts it must honor -->
  * **T102A-DEP-001 (SPSPG Source Dependency)** — SPSPG extraction from SPSST instructional comments requires SPSST Section III structure finalization. Phase/gate workflow development cannot begin until SPSST structural baseline approved.
  * **T102A-DEP-002 (MANIFEST Tracking Dependency)** — MANIFEST version tracking mechanism depends on `T102-GDR-002 (Canonical Header Standard)` compliance for YAML header schema consistency.
  * **T102A-DEP-003 (REQUEST Integration)** — SPS handoff to REQUEST depends on CONCEPT workflow integration protocols per `T102-GDR-001 (Operating Model Standard)`. Post-SPS-baseline emergent governance items SHALL follow controlled change process to prevent infinite refinement loop: Initiative/Epic-level governance changes require client-approved SPS version update; Feature/Story-level governance defers to REQUEST/CONCEPT/DESIGN with explicit traceability.

* **Interfaces**
  <!-- Governance-level role/process touchpoints -->
  * **T102A-IF-001 (SPS Output Contract)** — SPS SHALL provide to REQUEST:
      (a) Initiative & Epic-level IDs/GDRs/ADRs for feature inheritance per `T102-GDR-003`,
      (b) Inherited Considerations index with explicit ID references (no content duplication),
      (c) Governance & Roadmap with Feature Register containing canonical IDs and Purpose statements,
      (d) Handoff readiness evidence: completed validation checklist (Section VI), stakeholder sign-off (Section VII), baselined version (v1.0+), and explicit planner acknowledgment per `T102-IF-001` two-way handshake protocol.

* **Implementation Guidance**
  <!-- PURPOSE: Define epic-specific implementation patterns and technical conventions -->
  * **T102A-IG-001 (Roadmap & Governance Management)** — Epic information described in `SPS` SHALL include a "Roadmap & Governance" section with feature registers, phase sequence governance milestones, and success checkpoints. Detailed operational PM(WBS, sprints, tasks) maintained in external tools (ticktick) with traceability links to governance artifacts.
  * **T102A-IG-002 (Phase-Gate Workflow Pattern)** — SPSPG organizes consultancy by phases with explicit gates, referencing SPSST sections as source material. Phase sequence may differ from SPSST section order per `T102A-CON-003`. Each phase concludes with gate approval before proceeding.
  * **T102A-IG-003 (Version Pairing Mechanism)** — MANIFEST tracks SPSST↔SPSPG version pairs using YAML pairing schema. v1.0 SPS workflows require matching template versions (e.g., SPSST v1.0.0 ↔ SPSPG v1.0.0). Structural changes to SPSST trigger SPSPG review per pairing rules.
  * **T102A-IG-004 (Instructional Comment Pattern)** — SPSST instructional comments follow two-block pattern: `<!-- PURPOSE: [WHY this section exists] -->` + `<!-- GUIDANCE: [WHAT belongs here] -->`. PURPOSE blocks inform SPSPG phase rationale; GUIDANCE blocks inform validation checklists.
  * **T102A-IG-005 (Stakeholder Documentation)** — SPSST SHALL include explicit Stakeholders & Roles section (recommended placement: Section III.B or Executive Summary) listing key participants with decision authority, responsibilities, and collaboration interfaces. Minimum stakeholders: Client (Decision Owner/Sponsor), LLM_Consultant (Author/Epic Lead), LLM_Planner (Downstream Consumer). Aligns with PRINCE2 PID "Organisation and Governance" and PMI Charter "Stakeholders and Roles" sections.
  * **T102A-IG-006 (Validation Checklist Architecture)** — SPSST Section VI validation checklist SHALL implement 10-point industry-standard handoff readiness criteria organized by quality dimension: 
      (1) Governance Quality (approvals, decisions), 
      (2) Content Quality (objectives, scope, requirements), 
      (3) Structural Quality (IDs, traceability, completeness), 
      (4) Process Quality (stakeholder engagement, planner acceptance). Each criterion includes pass/fail indicator and evidence requirement.


##### vii. Epic Research & Notes
<!-- PURPOSE: Provide background, drivers, and key research findings that inform this Epic's direction. -->

**Research**

| Research ID | Title | Summary | Reference | Brief | Report |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `T102A-RES-001` | **SPS Workflow Optimization** | Validated emergent governance freeze, handoff criteria, procedural workflows; established 10-point readiness checklist | `T102A-ISSUE-002`, `T102A-ISSUE-003`, `T102A-GDR-002` | [brief](../research/brief/brief_T102A-SPS_sps-workflow-optimization.md) | [report](../research/report/report_T102A-SPS_sps-workflow-optimization.md) |

**Notes**

* **T102A-NOTE-001 (Rejection of Rigid v1.0 Structure)** — Previous templates were too technical and brittle. The new structure must be topic-driven and reflect the natural flow of a consultative conversation.
* **T102A-NOTE-002 (Architectural Model)** — The SPS represents a single "Initiative/Project" This Initiative describes the Epics needed to create the following Features described such as template (`SPSST`) and process (`SPSPG`). 
* **T102A-NOTE-003 (SPS Document Classification)** — We find that the current SPS document mirror more the Project Initiation Document (PID) than Discovery Brief.
* **T102A-NOTE-004 (Industry Standards Alignment)** — Research of PRINCE2 PID standards (2025) confirms our approach aligns with project definition, management approaches, and living document characteristics. ISO/IEC/IEEE 29148:2018 requirements engineering principles emphasize that requirements must be "necessary, appropriate, unambiguous, complete, singular, feasible, verifiable, correct, and conforming." BABOK v3 provides clear distinction between assumptions (factors believed true but unconfirmed) and constraints (restrictions/limitations on solutions), supporting our need for better categorization in Initiative Considerations to reduce cognitive load and improve clarity.

##### viii. Epic Governance Decisions

| GDR ID | Title | Status | Owner | Effective | Supersedes | Anchor |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `T102A-GDR-001` | Governance Snapshot Standard | Proposed | Client | 2025-09-26 | — | #t102-gdr-006-roadmap & Governance |
| `T102A-GDR-002` | Governance Freeze Standard | Proposed | Client | 2025-10-05 | — | #t102a-gdr-002-governance-freeze |

* **T102A-GDR-001 (Governance Snapshot Standard) {#t102a-gdr-001-governance-snapshot}**
  **Context** External research and internal standards indicate governance documents should present a milestone-level roadmap while keeping operational details external. The initiative prohibits formal planning artifacts in-repo according to `T102-CON-004`. To preserve governance oversight, each SPS Epic needs a concise, standardized **Governance & Roadmap** snapshot with links to external PM tools and Concept ADRs. This follows existing governance/ADR conventions and placement rules.
  **Decision** Adopt `T102A-ADR-001 (Governance Snapshot Framework)` as mandatory epic section structure. All epics SHALL include governance snapshot with phase sequence, milestones, and success checkpoints; detailed plans remain external in PM tools according to `T102A-CON-001`
  **Consequences**
  (+) Aligns with PRINCE2/PMI/SAFe industry standards for PID/Charter documents
  (+) Provides executive visibility into epic progress without operational detail overhead
  (+) Standardizes epic roadmap presentation across all initiatives
  (±) Requires epic authors to maintain governance-level milestone awareness
  **References**
  `T102A-CON-001 (Roadmap & Governance Management)`,
  `T102-QG-003 (Low-Disruption Implementation)`,
  `T102-CON-001 (Format Requirements)`,
  `T102A-NOTE-005 (Governance Snapshot Research)`


* **T102A-GDR-002 (Governance Freeze Standard) {#t102a-gdr-002-governance-freeze}**
  **Context** SPS epic consultancy creates continuous discovery of new Initiative/Epic-level governance items (GDRs, IGs, IDs), creating infinite refinement loop that blocks REQUEST handoff. Without formal baseline trigger and controlled change process, SPS remains perpetually "in progress" per `T102A-ISSUE-002`. Research validation via `T102A-NOTE-006` confirms industry standards (PRINCE2 PID sponsor approval, PMI Charter stakeholder sign-off, SAFe LPM epic approval gates) use formal freeze mechanisms to separate discovery phase from execution phase while managing emergent governance via change control.
  **Decision** Adopt formal governance baseline standard with four-component framework:
    (1) Baseline Trigger: SPS governance baseline SHALL be established via stakeholder sign-off (Section VII) with decision owner approval (name/date). Sign-off confirms Initiative/Epic-level governance (Section III.B-C) is sufficiently complete for REQUEST intake per `T102A-QG-003` handoff readiness criteria and `T102-IF-001` two-way handshake protocol.
    (2) Change Control Process: Post-baseline emergent governance items SHALL follow controlled disposition per layered hierarchy:
      - Initiative/Epic-Level Changes (new GDRs, IGs, or material scope modifications): Require client-approved SPS version update with amendment log (Section V.A) and updated stakeholder sign-off. Version increments to next minor (v1.1, v1.2) or major (v2.0) per change magnitude.
      - Feature/Story-Level Governance (implementation decisions, detailed requirements): Defer to REQUEST/CONCEPT/DESIGN workflows with explicit traceability via deferred decisions log (see component 4 below). No SPS version update required.
    (3) GDR Kanban Workflow: Epic Governance Decisions SHALL function as governance decision Kanban aligned with SAFe LPM approval workflows. GDR status progression: Proposed → In Review → Accepted → Deprecated. Status transitions require client approval with effective date logging. Index provides governance snapshot visibility without operational detail overhead per `T102A-IG-001`.
    (4) Deferred Decisions Log: When Feature/Story-level governance emerges during SPS epic work but belongs downstream, SHALL be logged in Epic Notes (Section vi) with deferred-to artifact reference (REQUEST/CONCEPT/DESIGN) and traceability ID. Downstream artifacts inherit via `T102-GDR-003 (Inheritance Model Standard)`, preventing governance loss while maintaining scope boundaries.
  **Consequences**
  (+) Prevents infinite SPS refinement loop; enables clear discovery-to-execution transition
  (+) Aligns with PRINCE2/PMI/SAFe industry baseline and change control best practices
  (+) Provides client-controlled governance freeze authority via stakeholder sign-off gate
  (+) Distinguishes Initiative/Epic governance (freeze in SPS) from Feature/Story decisions (defer downstream)
  (+) GDR Kanban provides governance visibility and audit trail per `T102-QG-002`
  (±) Requires disciplined change control adherence; post-baseline SPS updates require formal approval
  (±) Client must balance "sufficiently complete" baseline vs "perfect" baseline (research confirms 80% threshold acceptable)
  (-) Initial adoption overhead to establish baseline discipline; author training on change control process
  **References**
  `T102A-ISSUE-002 (Emergent Governance Freeze)`,
  `T102A-CON-004 (Governance Freeze Discipline)`,
  `T102A-QG-003 (Handoff Quality)`,
  `T102A-DEP-003 (REQUEST Integration)`,
  `T102A-IF-001 (SPS Output Contract)`,
  `T102-GDR-001 (Operating Model Standard)`,
  `T102-GDR-003 (Inheritance Model Standard)`,
  `T102-IF-001 (Planner Handoff)`,
  `T102-IF-002 (Client Review)`,
  `T102A-NOTE-006 (Workflow Research Validation)`


##### ix. Epic Issues & Risks
<!-- PURPOSE: A log for open issues and risks that are specific to this Epic's success. -->

**Issues**
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Resolution Notes | Resolution Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `T102A-ISSUE-001` | Approved Epics Label | Confirm exact label for `Approved Epics` list in SPS body. | Client | `RESOLVED` | `LOW` | 2025-10-04 | Resolved via terminology decision: Use "Approved Epics" label per YAML 'approved'. Definitive tracking in YAML header. | 2025-10-05 |
| `T102A-ISSUE-002` | Emergent Governance Freeze | New Initiative-level GDRs/IGs emerge during SPS epic consultancy, preventing epic freeze for REQUEST handoff. | Client | `RESOLVED` | `HIGH` | 2025-10-04 | Resolved `T102A-NOTE-006`. Established `T102A-CON-004` (sign-off baseline). `T102A-GDR-002` formalizes freeze. | 2025-10-05 |
| `T102A-ISSUE-003` | Handoff Readiness Criteria | No industry-validated handoff quality gates for SPS→REQUEST completion. | Client | `RESOLVED` | `HIGH` | 2025-10-04 | Resolved `T102A-NOTE-006`. Criteria incorporated into `T102A-QG-003` (10-point readiness) & `T102A-IG-006`. | 2025-10-05 |

**Risks**
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Mitigation Notes | Mitigation Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `T102A-RISK-001` | Author Reversion | Authors may revert to old SPS habits if SPSPG phase/gate workflow unclear or validation checklists incomplete. | Client | `MONITORED` | `MEDIUM` | 2025-10-04 | Mitigated by `T102A-ASSUM-001` (LLM focus) & `T102A-CON-002` checklists. `T102-IG-001` guides authors. | — |
| `T102A-RISK-002` | Version Drift | SPSST structural changes may not propagate to SPSPG, causing template version drift and workflow inconsistency. | Client | `MONITORED` | `MEDIUM` | 2025-10-04 | Mitigated by `T102A-IG-003` (Version Pairing) & `T102-CON-002` discipline. `T102-QG-003` deferral. | — |
| `T102A-RISK-003` | Document Bloat | Single SPS hosting Initiative and Epic-level governance may exceed manageable size or LLM context limits. | Client | `MONITORED` | `MEDIUM` | 2025-10-04 | Validated `T102A-NOTE-006` (appendices). Escalate `T102-ISSUE-005` if needed. Defer refactor `T102-QG-003`. | — |
| `T102A-RISK-004` | SPS→REQUEST Integration Failure | CONCEPT workflow integration patterns between SPS and REQUEST unclear until concrete test implementation. | Client | `MONITORED` | `MEDIUM` | 2025-10-04 | Addressed via `T102A-DEP-003`, `T102A-ISSUE-002` freeze. `T102-GDR-001` confirms parallel approach. | — |

##### x. Epic Changelog
<!-- PURPOSE: A lightweight audit trail for material changes within this Epic. -->

* **2025-08-26** — Initial creation of Epic structure based on v1.1.0 SPS template design.
* **2025-10-05** — Phase 1 Foundation completion: External research integration (`T102A-NOTE-006`) resolving `T102A-ISSUE-002/003`; finalized all Epic Requirements (QG, DEP, IF, ASSUM, CON, IG) with industry-validated specifications; established `T102A-GDR-002` (Governance Freeze Standard); completed Issues & Risks tables with resolution notes; epic status advanced to `review` pending client approval for Phase 2 SPSST development.

#### 2. `T102B` Epic: `REQUEST` - Request Workflow 
```yaml
epic_id: 'T102B'
epic_code: 'REQUEST'
epic_title: 'Request Workflow'
epic_type: 'existing'
epic_status: 'draft'
epic_owner: 'LLM_Consultant'
```

##### i. Purpose
Establish a consistent, client-friendly **Request** workflow that transforms each approved **SPS Feature** into a feature-scoped **BRD→SRS** specification with **feature-level acceptance criteria**. The Request artifact serves as the stable requirements baseline between problem definition (SPS) and solution exploration (Concept/Design), supporting the consultancy operating model sequence: **SPS → Request → Design**, with Concept operating as a dynamic workspace throughout.

The Epic delivers structural templates, procedural guidelines, and lineage metadata to ensure clear handoffs to either detailed design (Concept/Design) or direct implementation planning, depending on feature complexity and Client requirements.

##### ii. Scope

* **In Scope:**
  * Structural template defining the normative Request artifact structure with section classification (mandatory/optional/deferred)
  * Procedural guideline covering authoring workflows, section rules, validation checklists, and gate criteria
  * Manifest schema for Request metadata and lineage tracking across SPS→Request→Concept
  * Lightweight Request variant for simple features to reduce documentation overhead
  * Interface contracts for SPS intake, approval output, and downstream handoff
  * Implementation guidance for section authoring, story index patterns, and workflow selection criteria

* **Out of Scope:**
  * SPS artifact structure and authoring rules (T102A scope)
  * Concept artifact structure and ADR aggregation (T102C scope)
  * Design artifact and story-level implementation records (T102D scope)
  * Validation tooling, template automation, or migration scripts
  * Story-level functional requirement bodies (deferred to Concept/Design per industry patterns)

##### iii. Inherited Considerations

| Source Artifact | Source ID | Category | Inherited Rule IDs |
| :-------------- | :-------- | :------- | :----------------- |
| SPS | T102 | Assumptions | `T102-ASSUM-001 (LLM Generation)` |
| SPS | T102 | Constraints | `T102-CON-001 (Format Requirements)`, `T102-CON-003 (Documentation Standards)` |
| SPS | T102 | Quality Goals | `T102-QG-002 (End-to-End Traceability)` |
| SPS | T102 | Dependencies | `T102-DEP-001 (Client Engagement)`, `T102-DEP-002 (Planner Integration)` |
| SPS | T102 | Implementation Guidance | `T102-IG-005 (Canonical Header)`, `T102-IG-007 (ID Standard)` |
| SPS | T102 | Governance | `T102-STD-001 (Operating Model Standard)`, `T102-STD-003 (Inheritance Model Standard)`, `T102-STD-005 (ID Governance Standard)` |

##### iv. Governance & Roadmap

**Scope & Ownership**
- Owner: Epic Lead (`LLM_Consultant`)
- Decision Owner: `Client`
- Support: `LLM_Researcher`, `LLM_Developer`, `LLM_Planner`
- Org baseline (RACI): see `III.B.1 (Organization & Responsibilities)`

**Phase & Gates**
| Phase | Title | Intent | Key Exit Milestone | Duration Band | Gate Approver (A) | Phase Lead (R) | Plan Link |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 0 | **Foundation** | Epic dossier establishment & research integration | Foundation Readiness: T102B approved with stable E-IDs; RES-001/RES-002 integrated | — | `Client` | `LLM_Consultant` | [roadmap_T102B-REQUEST_phase0.md](../T102B/workspace/roadmap/roadmap_T102B-REQUEST_phase0.md) |
| 1A | **Template Design** | Develop structural templates; T102B1 (RST) + T102B4 (RLITE) in parallel | Template Validation: RST and RLITE specifications approved; T810A1 serves as exemplar | — | `Client` | `LLM_Consultant` | TBD |
| 1B | **Guideline Design** | Develop procedural guidelines; T102B2 (RPG) + T102B3 (MANIFEST) in parallel | Guideline Validation: RPG and MANIFEST specifications approved | — | `Client` | `LLM_Consultant` | TBD |
| 2 | **Integration** | Validate SPS→Request→Design/Plan workflow | Package Completeness: End-to-end workflow demonstrated | — | `Client` | `LLM_Consultant` | TBD |

**References**
- Master Initiative Roadmap: [roadmap_T102-CWD.md](../workspace/plan/T102/roadmap_T102-CWD.md)
- External PM Tracking: ticktick (client PM tool)

##### v. Feature Register

| ID | Code | Title | Purpose | Feature Lead (R) | Status | Canonical Link (Request) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `T102B1` | `RST` | **Request Structural Template** | Define normative Request artifact structure with section classification | `LLM_Consultant` | `in-discovery` | — |
| `T102B2` | `RPG` | **Request Procedural Guideline** | Define authoring workflow, gate criteria, and validation checklists | `LLM_Consultant` | `proposed` | — |
| `T102B3` | `MANIFEST` | **Request Manifest** | Define Request metadata and SPS→Request→Concept lineage tracking | `LLM_Consultant` | `proposed` | — |
| `T102B4` | `RLITE` | **Request Lite** | Define streamlined Request variant for simple features | `LLM_Consultant` | `in-discovery` | — |

##### vi. Epic Requirements

* **Assumptions**
  * **ASSUM Validation Lifecycle Summary**

    | ID | Title | Status | Validation Method | Timing | Owner | If Invalidated | CON Cross-Ref |
    |:---|:------|:-------|:------------------|:-------|:------|:---------------|:--------------|
    | `T102B-ASSUM-001` | SPS Narrative Sufficiency | `Pending` | Pilot Request derivation from first 3 SPS Features | Feature T102B1 | LLM_Consultant | Escalate: Client provides additional narrative | — |
    | `T102B-ASSUM-002` | RLITE Adoption | `Pending` | RLITE adoption metrics post-v1 launch | Feature T102B4 | Client | Mitigate: strengthen IG-004 decision tree | `T102B-CON-003` |
    | `T102B-ASSUM-003` | Author Self-Assessment | `Pending` | Author feedback during pilot workflows | Feature T102B1/B4 | Client | Mitigate: enhance IG-004 decision criteria | — |

  * **T102B-ASSUM-001 (SPS Narrative Sufficiency)** — `T102A (SPS)` Feature bundles provide sufficient narrative context (Purpose statement, Epic requirements, inherited initiative-level IDs) to derive initial Request scope and navigation structures.

  * **T102B-ASSUM-002 (RLITE Adoption)** — Teams will appropriately select RLITE workflow for simple features rather than defaulting to Full Request, thereby realizing adoption friction reduction per `T102B-QG-001`.

  * **T102B-ASSUM-003 (Author Self-Assessment)** — Authors can accurately self-assess feature complexity using `T102B-IG-004` decision criteria to select appropriate workflow (Full Request vs RLITE vs PR-only).

* **Constraints**
  * **T102B-CON-001 (No Custom Processors)** — Request artifacts in v1 SHALL use only standard Markdown rendering and YAML parsing; no custom preprocessors, validators, or template engines are permitted. This extends `T102-CON-001` by explicitly prohibiting tooling complexity beyond standard editors.
    External Reference: `T102-CON-001 (Format Requirements)`

  * **T102B-CON-002 (No Story FR Mandate)** — Story-level Functional Requirements (FRs) SHALL NOT be mandatory at Request Phase per `T102B-RES-001` — W2, P2. Request artifacts MAY include a Story Index for navigation, but detailed story-level FR bodies and acceptance criteria SHALL be deferred to `T102D (DESIGN)` workflows. This constraint mitigates risk of Documentation Trap per SAFe Iteration Planning best practices.

  * **T102B-CON-003 (Template Variant Boundary)** — `T102B4 (RLITE)` artifacts SHALL NOT expand beyond their defined scope (<200 lines) by accretion per `T102B-RES-001` — P1. Authors SHALL NOT add sections incrementally until RLITE becomes a de facto Full Request. Scope expansion requires explicit workflow transition via `T102B-IG-004` decision tree. This constraint prevents risk of workflow undifferentiation.

  * **T102B-CON-004 (Decision Storage Boundary)** — Request artifacts SHALL NOT embed ADR body content. All architectural and governance decisions SHALL be stored canonically in Concept artifacts per `T102-STD-001` and `T102B-DEP-004`. Request artifacts MAY reference Concept ADRs via formal ID citation per `T102-ADR-005`. This constraint eliminates content duplication and ensures single source of truth for decisions.
    External Reference: `T102-STD-001 (Consultancy Operating Model Standard)`, `T102-ADR-003 (Explicit Inheritance Model)`, `T102-ADR-005 (ID Specification & Rules)`

* **Quality Goals**
  * **T102B-QG-001 (Adoption Friction Reduction)** — `T102B4 (RLITE)` artifacts SHALL remain within size constraints per `T102B-CON-003` and reduce authoring overhead for simple features per `T102B-RES-001` — W5, P1. Adoption friction is measured by: (a) author time-to-complete, (b) RLITE vs Full Request selection ratio for eligible features.
    External Reference: `T102-QG-003 (Low-Disruption Implementation)`

  * **T102B-QG-002 (No Duplication Overhead)** — Request artifacts SHALL avoid content duplication between FR sections and IG sections per `T102B-RES-001` — W1, P3. Requirements SHOULD be self-contained without requiring cross-reference to separate guidance documents for comprehension.

  * **T102B-QG-003 (Artifact Completeness)** — Request artifacts SHALL pass completeness validation against section classification (mandatory sections populated) before Request approval gate. Completeness evidence includes:
    (a) all mandatory sections contain substantive content,
    (b) Inherited Considerations table populated per `T102-ADR-003`,
    (c) navigation structures (Story Index if applicable) populated.

* **Dependencies**
  * **T102B-DEP-001 (SPS Intake Alignment)** — Request workflow SHALL accept intake exclusively from `T102A (SPS)` Feature bundles per `T102-STD-001`. No Request artifact SHALL be initiated without a corresponding approved Feature entry in the `T102A1` Feature Register. The SPS Feature bundle provides: Feature ID, Purpose statement, Epic constraints, and inherited initiative-level IDs. This dependency is operationalized by `T102B-IF-001` and assumes `T102B-ASSUM-001`.
    External Reference: `T102-STD-001 (Consultancy Operating Model Standard)`

  * **T102B-DEP-002 (Industry Standards)** — Request artifacts SHOULD align requirements quality to ISO 29148 principles for completeness, consistency, and verifiability. Industry standards referenced in `T102-NOTE-003` (ISO 29148, SAFe, BABOK v3) provide the quality baseline for Request content structure and requirements expression.
    External Reference: `T102-NOTE-003 (Industry Standards)`

  * **T102B-DEP-003 (RLITE Depends On RST)** — Feature `T102B4 (RLITE)` is a governed subset of `T102B1 (RST)` architecture per `T102B-RES-001` — P1. RLITE SHALL NOT be developed until RST section classification decisions are complete. RLITE inherits RST mandatory section definitions and applies reduction rules per `T102B-IG-001`. This dependency establishes the `T102B1` → `T102B4` feature sequencing constraint for Phase 1.

  * **T102B-DEP-004 (Concept Boundary Alignment)** — Request workflow operates within the requirements-only boundary. Request artifacts remain focused on WHAT is required; HOW decisions (architectural specifications) SHALL be stored in Concept artifacts. Request→Concept handoff transfers requirements for solution design; no design content returns to Request.
    External Reference: `T102-STD-001 (Consultancy Operating Model Standard)`, `T102-ADR-003 (Explicit Inheritance Model)`

  * **T102B-DEP-005 (Migration Discipline)** — Structural changes to Request templates or standards SHALL include migration notes documenting:
    (a) affected artifacts,
    (b) required updates,
    (c) compatibility approach (grandfather existing vs mandatory update).
    This dependency supports monitoring risks related to template migration.

* **Interfaces**
  * **T102B-IF-001 (SPS Intake Contract)** — Request workflow SHALL accept intake exclusively from `T102A (SPS)` Feature bundles per `T102B-DEP-001`. The SPS Feature bundle provides the minimum inputs required to initiate a Request artifact: Feature identification, purpose narrative, epic constraints, and inherited initiative-level IDs. Request authors SHALL NOT derive requirements from sources outside the approved SPS Feature bundle.

    | Field | Location | Required | Description |
    |:------|:-------|:---------|:------------|
    | `feature_id` | SPS Feature Register | **Yes** | Canonical F-SID (e.g., `T102B1`) |
    | `feature_code` | SPS Feature Register | **Yes** | Short code (e.g., `RST`) |
    | `purpose_statement` | SPS Feature Register | **Yes** | 1-2 sentence feature intent |
    | `epic_constraints` | SPS Epic vi (Constraints) | **Yes** | E-CON IDs applicable to feature |
    | `inherited_ids` | SPS Epic iii | **Yes** | Inherited Considerations table |
    | `story_notes` | SPS Epic vi (Notes) | No | Optional preliminary story hints |

    External Reference: `T102A-IF-001 (SPS Output Contract)`

  * **T102B-IF-002 (Approved Request Output)** — An "Approved Request" is defined as a Request artifact that has passed the Request approval gate per `T102B-STD-003` with documented evidence. The output payload provides the evidence bundle required for downstream Concept ingestion or direct Plan handoff. Approval evidence SHALL be captured in the artifact metadata and validation checklist.

    | Field | Location | Required | Description |
    |:------|:---------|:---------|:------------|
    | `request_id` | YAML header | **Yes** | Request artifact identifier |
    | `approval_status` | YAML header | **Yes** | Enum: `draft`, `review`, `approved` |
    | `approval_date` | YAML header | **Yes** | ISO date of approval |
    | `approver_role` | YAML header | **Yes** | Decision owner role (e.g., `Client`) |
    | `validation_checklist` | Section VI | **Yes** | All mandatory items passed |
    | `story_index` | Section (TBD) | Conditional | Required for multi-story features |
    | `inherited_considerations` | Section (TBD) | **Yes** | Per `T102-ADR-003` |

  * **T102B-IF-003 (Request Output Contract)** — Request artifacts SHALL provide trace links and ID references required for downstream ingestion (Design or Plan). The output contract ensures downstream workflows can ingest feature-level requirements without content duplication. Request SHALL NOT embed decision content; architectural decisions referenced in Request SHALL have canonical bodies in Concept per `T102B-CON-004` and `T102-STD-001`.

    | Field | Direction | Required | Description |
    |:------|:----------|:---------|:------------|
    | `request_path` | Request→Concept | **Yes** | Repo-relative path to approved Request |
    | `feature_id` | Request→Concept | **Yes** | F-SID for Concept Feature ADR index |
    | `f_rid_list` | Request→Concept | **Yes** | List of F-RIDs (FR, NFR, IF, IG) defined in Request |
    | `adr_references` | Request→Concept | Conditional | E-ADR/F-ADR IDs referenced (not embedded) |
    | `story_index` | Request→Concept | Conditional | Story IDs for Concept Design Log coordination |

    **Routing Rules** (normative):
    An approved Request SHALL route to one of the following downstream workflows based on feature characteristics:

    | Condition | Route To | Rationale |
    |:----------|:---------|:----------|
    | Feature requires architectural decisions or ADR development | Request→Concept | Concept provides ADR specification before Design |
    | Feature requires design-level story specification only | Request→Design | Direct handoff when no new ADRs needed |
    | Feature is operationally scoped (process/guideline only) | Request→Plan | Direct handoff for procedural implementation |

    Routing determination SHALL be documented in the Request approval gate evidence per `T102B-STD-003`. If routing is ambiguous, the default route SHALL be Request→Concept. For informative handoff validation guidance, see `T102B-IG-007`.

    External Reference: `T102-STD-001 (Consultancy Operating Model Standard)`


##### vii. Epic Standards

| STD ID | Title | Status | Owner | Effective | Supersedes | Adopts | Verification | Reference |
|:-------|:------|:-------|:------|:----------|:-----------|:-------|:-------------|:----------|
| `T102B-STD-001` | **Request Governance Snapshot Standard** | Proposed | Client | — | — | `T102B-ADR-001 (Request Architecture Standard)` | Review MUST verify: Phase 0 completion criteria checklist passed, Feature Register populated | `T102-STD-009 (Governance Standards Model)` |
| `T102B-STD-002` | **Workflow Typology Standard** | Proposed | Client | — | — | `T102B-ADR-003 (Story FR Deferral Standard)`, `T102B-ADR-004 (Request Lite Specification)` | Review MUST verify: workflow selection rationale documented, RLITE boundary (<200 lines) enforced | `T102-STD-009 (Governance Standards Model)` |
| `T102B-STD-003` | **Gate Evidence Standard** | Proposed | Client | — | — | — | Review MUST verify: gate evidence checklist items present, approval signature recorded | `T102-STD-009 (Governance Standards Model)` |
| `T102B-STD-004` | **Section Classification Policy** | Proposed | Client | — | — | `T102B-ADR-002 (Section Classification Standard)` | Review MUST verify: section classification applied per adopted spec, mandatory sections populated | `T102-STD-009 (Governance Standards Model)` |

* **T102B-STD-001 (Request Governance Snapshot Standard)** — The project SHALL use `T102B-ADR-001 (Request Architecture Standard)` as the specification for Request artifact family architecture, SPS intake alignment, and Phase 0 completion criteria. All Request workflow artifacts SHALL conform to the architecture standard before Feature design begins.
  - **Minimum Viable Conformance**:
    1) Request artifact family follows the hierarchical architecture (RST, RLITE, RPG, MANIFEST) per `T102B-ADR-001-CLAUSE-001`.
    2) Inheritance model uses ID-reference-only with no content duplication per `T102B-ADR-001-CLAUSE-002`.
    3) Phase 0 completion criteria satisfied before Feature design begins per `T102B-ADR-001-CLAUSE-003`.
  External Reference: `T102-STD-001 (Operating Model Standard)`

* **T102B-STD-002 (Workflow Typology Standard)** — The project SHALL use `T102B-ADR-003 (Story FR Deferral Standard)` and `T102B-ADR-004 (Request Lite Specification)` as the specifications for Request workflow typology. Three workflow variants are established: Full Request, RLITE, and PR-only.
  - **Minimum Viable Conformance**:
    1) Story Index used for navigation; story-level FR bodies deferred to Design per `T102B-ADR-003-CLAUSE-001`, `T102B-ADR-003-CLAUSE-002`.
    2) RLITE artifacts remain under 200 lines and do not expand by accretion per `T102B-ADR-004-CLAUSE-001`.
    3) RLITE contains mandatory sections only per the defined section list per `T102B-ADR-004-CLAUSE-002`.
    4) Workflow selection follows the decision tree criteria per `T102B-ADR-004-CLAUSE-004`, `T102B-ADR-004-CLAUSE-005`.

* **T102B-STD-003 (Gate Evidence Standard)** — Request approval gates SHALL require documented evidence across four categories before an artifact is approved. The approver MUST record approval status, date, and role in artifact metadata. If any mandatory evidence item is incomplete, the author MUST either remediate or obtain a documented waiver with rationale before approval.
  - **Minimum Viable Conformance**:
    1) Governance evidence: inherited considerations populated, STD/ADR references valid.
    2) Content evidence: all mandatory sections populated, requirement statements testable.
    3) Structure evidence: YAML header complete, Story Index populated (if applicable).
    4) Process evidence: validation checklist passed, approver sign-off recorded.
    5) Authors SHOULD follow `T102B-IG-005` for detailed checklist items and remediation guidance.
  External Reference: `T102-STD-009 (Governance Standards Model)`

* **T102B-STD-004 (Section Classification Policy)** — The project SHALL use `T102B-ADR-002 (Section Classification Standard)` as the specification for Request section classification schema, ensuring artifact completeness per `T102B-QG-003`. Section classification is a governance decision, not author preference.
  - **Minimum Viable Conformance**:
    1) Three classification categories applied: Mandatory, Optional, Deferred per `T102B-ADR-002-CLAUSE-001`.
    2) Full Request section list followed per canonical table per `T102B-ADR-002-CLAUSE-002`.
    3) RLITE section list followed per canonical table per `T102B-ADR-002-CLAUSE-003`.
    4) Validation rules enforced: empty mandatory sections fail gate per `T102B-ADR-002-CLAUSE-004`.
  External Reference: `T102-STD-009 (Governance Standards Model)`

##### viii. Epic Development Guidances

* **Implementation Guidance**
  * **T102B-IG-001 (Section Classification)** — Request authors SHOULD apply the section classification schema defined in `T102B-ADR-002` when authoring Request artifacts. This guidance provides the authoring workflow for applying classification rules; the canonical section lists, classification categories, and validation rules are specified in `T102B-ADR-002`. Authors SHOULD consult `T102B-ADR-002` for definitive section requirements per Request variant (Full Request vs RLITE).

  * **T102B-IG-002 (FR/IG Consolidation)** — Request authors SHOULD avoid content duplication between Functional Requirements (FR) sections and Implementation Guidance (IG) sections per `T102B-QG-002`. The "requirements-with-guidance" pattern consolidates requirement statements with inline authoring hints rather than separating into parallel sections. Detailed implementation patterns belong in Feature-level IGs or ADRs, not in FR bodies.

  * **T102B-IG-003 (Story Index Deferral)** — Request artifacts SHOULD include a Story Index for multi-story features, providing story identification and navigation structure. Story-level FR bodies and detailed acceptance criteria are deferred to `T102D (DESIGN)` workflows per `T102B-CON-002` and `T102B-ADR-003`. The Story Index contains: Story ID, Title, Purpose summary, and Concept/Design link (populated post-handoff). This pattern mitigates Documentation Trap risk.
    Reference: `T102B-ADR-003 (Story FR Deferral Standard)`

  * **T102B-IG-005 (Gate Evidence Checklist)** — Authors SHOULD use the following checklist to prepare Request artifacts for approval gate per `T102B-STD-003`. Each category lists recommended evidence items; items marked **(Proposed Normative)** are candidates for future elevation to STD-003 MUST requirements.

    | Category | Evidence Items | Notes |
    |:---------|:---------------|:------|
    | **Governance** | Inherited Considerations populated; STD/ADR references valid; GDR→STD migration complete | **(Proposed Normative)**: Inherited Considerations validation |
    | **Content** | All mandatory sections contain substantive content; FR/NFR statements testable per ISO 29148 principles; no placeholder-only mandatory sections | **(Proposed Normative)**: Testable requirements check |
    | **Structure** | YAML header complete per MANIFEST schema; Story Index populated (if >1 story); section classification applied per `T102B-ADR-002` | — |
    | **Process** | Validation checklist passed; approver sign-off recorded with role and date; workflow selection rationale documented in frontmatter | — |

    **Common Pitfalls**:
    - Inherited Considerations table left empty (copy from SPS Epic Dossier)
    - Story Index included for single-story features (omit per `T102B-ADR-002-CLAUSE-003`)
    - Approval gate attempted without mandatory section content (run section classification check first)

    **Remediation Guidance**:
    - If governance evidence missing: review `T102B-IG-006` for inheritance referencing patterns
    - If content evidence missing: review section classification per `T102B-ADR-002` for mandatory section list
    - If waiver needed: document rationale per `T102B-STD-003` waiver mechanism

    Reference: `T102B-STD-003 (Gate Evidence Standard)`, `T102B-QG-003 (Artifact Completeness)`

  * **T102B-IG-006 (Inheritance Referencing)** — Request authors SHOULD use reference-only inheritance per `T102-ADR-003`. Inherited initiative and epic-level IDs SHOULD be cited by ID reference in the Inherited Considerations table; content SHOULD NOT be duplicated from parent artifacts. When referencing inherited IDs in Request body text, use short-hand format per `T102-ADR-005`. Full reference format is required only in dedicated Reference sections.
    External Reference: `T102-ADR-003 (Explicit Inheritance Model)`, `T102-ADR-005 (ID Specification & Rules)`

  * **T102B-IG-007 (Handoff Routing)** — Authors SHOULD use the following validation checklist when preparing approved Request artifacts for downstream handoff per `T102B-IF-003`. This checklist operationalizes the routing rules defined in IF-003 and supports gate evidence preparation per `T102B-STD-003`.

    **Pre-Handoff Validation Checklist** (informative):
    - [ ] Approval gate passed per `T102B-STD-003` (all mandatory evidence items confirmed)
    - [ ] Output payload fields populated per `T102B-IF-003` table (request_path, feature_id, f_rid_list, adr_references if applicable, story_index if applicable)
    - [ ] Routing determination documented (Concept / Design / Plan) with rationale
    - [ ] If routing to Concept: ADR reference list populated; Concept intake readiness confirmed
    - [ ] If routing to Design: story index populated; no outstanding ADR development needed
    - [ ] If routing to Plan: operational scope confirmed; no architectural dependencies

    **Routing Decision Guidance**:
    - Authors SHOULD assess whether the feature introduces new architectural patterns requiring ADR specification. If yes, route to Concept.
    - Authors SHOULD assess whether the feature scope is limited to story-level design. If yes and no new ADRs are needed, routing to Design MAY be appropriate.
    - Authors SHOULD default to Concept routing when uncertain per `T102B-IF-003` default rule.

    **Common Pitfalls**:
    - Routing to Design when undocumented ADR decisions exist (route to Concept instead)
    - Routing to Plan for features requiring design specification (route to Design instead)
    - Incomplete output payload (validate all IF-003 required fields before handoff)

* **Integration Guidance**
  * **T102B-INT-001 (SPS→Request Coordination)** — Non-normative guidance for coordinating Request artifact development with SPS Feature bundle constraints. Authors initiating Request workflows SHOULD validate SPS Feature bundle completeness before starting. This guidance operationalizes the interface contract defined in `T102B-IF-001`.

    **Intake Validation Checklist** (recommended):
    - SPS Feature purpose statement is clear and actionable (not vague vision)
    - Epic constraints inherited into Request are understood and achievable
    - Story hints from SPS (if any) align with assessed feature complexity
    - Feature ID and code are confirmed in SPS Feature Register

    **Coordination Patterns**:
    - If SPS requires amendment during Request development, authors SHOULD notify Client and document in Request Issues register (not via SPS change request)
    - Authors SHOULD use `T102B-IG-004` decision criteria to assess feature complexity relative to SPS scope signals
    - If SPS scope signals misalign with Request complexity assessment, authors SHOULD escalate to Client before proceeding

    **Compatibility Expectations**:
    - SPS Feature bundle format per `T102A-IF-001` is stable; Request intake relies on this contract
    - Changes to SPS Feature Register schema SHOULD be coordinated with T102B epic owners

    External Reference: `T102A-IF-001 (SPS Output Contract)`, `T102B-IF-001 (SPS Intake Contract)`, `T102B-ASSUM-001 (SPS Narrative Sufficiency)`, `T102B-RISK-001 (Intake Drift)`

  * **T102B-INT-002 (Request→Concept Coordination)** — Non-normative guidance for coordinating Concept architecture development with approved Request artifacts. This guidance operationalizes the interface contract defined in `T102B-IF-003` and supports Request→Concept boundary alignment per `T102B-DEP-004`.

    **Handoff Timing**:
    - Concept intake SHOULD begin once Request reaches "approved" gate per `T102B-IF-002`
    - Pre-approval coordination MAY occur for complex features requiring early architectural exploration

    **Handoff Packaging**:
    - Request output payload per `T102B-IF-003`: request_path, feature_id, f_rid_list, adr_references (conditional), story_index (conditional)
    - Validation checklist completion status per `T102B-IG-005`
    - Inherited Considerations table for Concept traceability

    **Story Index Mapping**:
    - Request Story Index (if present) maps to Concept Design Log Register entries
    - Story-level detail deferred to Design phase per `T102B-CON-002` and `T102B-ADR-003`

    **Change Control**:
    - Post-Concept-approval Request changes SHOULD be coordinated with T102C epic owners
    - New RIDs added post-handoff MAY trigger new Concept ADRs or existing ADR variance

    **Compatibility Expectations**:
    - Concept intake expects Request output per `T102B-IF-003` contract
    - Request authors SHOULD NOT assume Concept readiness criteria beyond this contract until T102C formalizes intake specification

    Reference: `T102B-IF-002 (Approved Request Output)`, `T102B-IF-003 (Request Output Contract)`, `T102B-DEP-004 (Concept Boundary Alignment)`, `T102B-CON-002 (No Story FR Mandate)`

  * **T102B-INT-003 (T102 IF Schema Coordination)** — Non-normative coordination note proposing unified IF table schema standardization for T102 initiative consideration. This proposal emerged from T102B Phase 0 consultation and addresses schema variance across epic IF definitions.

    **Proposed IF Table Schema** (for T102 consideration):
    | Column | Purpose | Format |
    |:-------|:--------|:-------|
    | Field | Data element name | PascalCase identifier |
    | Location/Direction | Source→Target or storage location | `<artifact> → <artifact>` |
    | Required | Mandatory vs optional | `Required` / `Optional` / `Conditional` |
    | Description | Field semantics | 1-2 sentences |

    **Rationale**:
    - T102A-IF-001, T102B-IF-001/002/003 use varying table schemas
    - Standardization enables cross-epic IF validation
    - Aligns with `T102-QG-002 (End-to-End Traceability)`

    **Compatibility Expectation**:
    - T102B IF definitions adopt this schema
    - T102A/T102C MAY adopt via future consultation
    - T102 governance decision determines initiative-wide adoption

    External Reference: `T102-ADR-005-CLAUSE-002 (Taxonomy & Terminology)`, `T102B-IF-001`, `T102B-IF-002`, `T102B-IF-003`

  * **T102B-INT-004 (T102 ADR vs IG Framework Coordination)** — Non-normative coordination note proposing the ADR vs IG decision framework for T102 initiative consideration. This framework was adopted for T102B governance during Phase 0 consultation.

    **Proposed Framework** (for T102 adoption):
    - ADR required when: real decision with trade-offs, expensive to change later, cross-cutting impact
    - IG appropriate when: "how-to" guidance after decision set, low-risk/local, non-controversial
    - Red flag: IG with new normative constraint not in RID SHOULD be escalated to ADR or CON

    **T102B Adoption Evidence**:
    - T102B-ADR-001 through ADR-004 represent real decisions (Options A/B/C considered)
    - T102B-IG-001 through IG-006 provide "how-to" referencing governing ADRs
    - IG bodies use SHOULD/MAY; MUST/SHALL reserved for ADR CLAUSE content

    **Compatibility Expectation**:
    - T102A/T102C MAY adopt this framework for consistency
    - T102 governance decision determines initiative-wide adoption

    External Reference: `T102-ADR-005-CLAUSE-005B (Implementation Guidance Rules)`, `T102-ADR-005-CLAUSE-005C (Integration Notes Rules)`, `T102B-NOTE-009`

  * **T102B-INT-005 (T102 IG Non-Normative Coordination)** — Non-normative coordination note proposing that T102 initiative clarify IG items use SHOULD/MAY language only, with MUST/SHALL reserved for ADR Specification clauses.

    **Current State**:
    - T102-ADR-005-CLAUSE-005B permits: "IG MAY use MUST/SHALL when defining authoring standards intended to be enforceable"
    - This permissiveness creates ambiguity on IG vs ADR authority boundaries

    **Proposed Clarification** (for T102 consideration):
    - IG SHOULD use SHOULD/MAY language for guidance patterns
    - IG SHOULD NOT introduce constraints beyond governing RID/ADR
    - Enforceable standards requiring MUST/SHALL SHOULD be ADR CLAUSE content
    - IG MAY reference ADR clauses for normative authority (link-don't-duplicate)

    **T102B Adoption Evidence**:
    - T102B-IG-001 through IG-006 rewritten with SHOULD/MAY language
    - Normative rules migrated to ADR Specification sections
    - Drift risk reduced via clear authority boundary

    **Compatibility Expectation**:
    - T102A/T102C MAY adopt this clarification for consistency
    - T102 governance decision determines initiative-wide adoption

    External Reference: `T102-ADR-005-CLAUSE-005B`, `T102B-NOTE-010`

  * **T102B-INT-006 (Category Promotion Coordination)** — Non-normative coordination note proposing a cross-category promotion standard for informative items (NOTE/IG/INT) to normative items (RID/DRID). This addresses a governance gap identified during T102B Phase 0 consultation.

    **Governance Gap**:
    - `T102-ADR-007-CLAUSE-009` defines cross-scope promotion (Epic→Initiative)
    - No standard exists for cross-category promotion (NOTE→IG→ADR)

    **Proposed Promotion Path** (for T102 consideration):
    | From | To | Trigger | Governance Action |
    |:-----|:---|:--------|:------------------|
    | NOTE | IG | Pattern becomes enforced | Create IG referencing NOTE provenance |
    | NOTE | RES | Research validation required | Commission research; NOTE becomes Brief input |
    | IG | ADR CLAUSE | IG contains decision with trade-offs | Promote to ADR; deprecate IG |
    | INT | RID (IF/CON) | Coordination becomes contractual | Create RID; update INT to reference |

    **Red Flag Test**:
    - If informative item (NOTE/IG/INT) contains constraint not in RID, promotion SHOULD be considered
    - If informative item is frequently referenced for normative authority, promotion SHOULD be considered

    **Compatibility Expectation**:
    - T102B applies this pattern for Phase 0 OID assessment
    - T102 governance decision determines initiative-wide adoption

    External Reference: `T102-ADR-007-CLAUSE-009 (Cross-Scope Promotion)`, `T102-ADR-005-CLAUSE-002`

##### ix. Epic Research & Notes

**Research**
| Research ID | Title | Summary | Reference | Brief | Report |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `T102B-RES-001` | **Request Artifact Analysis** | External comparison of Request artifact against industry standards; recommends Request Lite, deferring story-level FRs to Design, and reducing FR/IG duplication | E-CON, E-IG, E-GDR, E-ADR | [brief](../T102B/research/brief/brief_T102B-RES-001_request-artifact-analysis.md) | [report](../T102B/research/report/report_T102B-RES-001_request-artifact-analysis.md) |
| `T102B-RES-002` | **Epic Foundation Assessment** | Internal gap analysis; 55 E-ID candidates | All E-IDs | [brief](../T102B/research/brief/brief_T102B-RES-002_epic-foundation-assessment.md) | [report](../T102B/research/report/report_T102B-RES-002_epic-foundation-assessment.md) |

**Notes**
* **T102B-NOTE-002 (Model-B Governance)** — Feature-level Requests keep specs small and parallelizable; the Epic provides overall control and is described in the SPS.

##### x. Epic Issues & Risks

**Issues**
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Resolution Notes | Resolution Date |
|:---|:------|:------------|:------|:-------|:---------|:--------------|:-----------------|:----------------|
| `T102B-ISSUE-001` | YAML Keys Finalization | Finalize exact Request YAML key set & enums | Client | `OPEN` | `HIGH` | 2026-01-17 | — | — |
| `T102B-ISSUE-002` | Manifest Format Decision | Decide manifest format (`.json` vs `.md`) and storage path | Client | `OPEN` | `HIGH` | 2026-01-17 | — | — |
| `T102B-ISSUE-003` | Story Register Scope | Reduce story detail to Story Index; defer FRs downstream | Client | `IN-REVIEW` | `HIGH` | 2026-01-17 | Resolution framework established via `T102B-ADR-003 (Story FR Deferral Standard)`; final Story Index template deferred to T102B1 Feature | — |
| `T102B-ISSUE-004` | ID Collision With RES-001 | SSOT Issue IDs (001-003) collide semantically with RES-001 Issue IDs; requires renumbering decision | Client | `OPEN` | `MEDIUM` | 2026-01-17 | — | — |
| `T102B-ISSUE-005` | Missing IF Inventory | No explicit interface contracts exist for SPS intake or Concept handoff | Client | `RESOLVED` | `HIGH` | 2026-01-17 | Addressed by Activity 2.3; see `T102B-IF-001 (SPS Intake Contract)`, `T102B-IF-002 (Approved Request Output)`, `T102B-IF-003 (Request Output Contract)` | 2026-01-20 |
| `T102B-ISSUE-006` | Missing IG Inventory | No implementation guidance exists to operationalize authoring rules | Client | `RESOLVED` | `HIGH` | 2026-01-17 | Addressed by Activity 2.3; see `T102B-IG-001` through `T102B-IG-006` in Proposal Section III.C | 2026-01-20 |
| `T102B-ISSUE-007` | Missing Phase & Gates Snapshot | SSOT Governance & Roadmap table was empty | LLM_Consultant | `RESOLVED` | `HIGH` | 2026-01-15 | Populated in Subphase 1 Activity 1.4 with Phase 0/1A/1B/2 structure | 2026-01-17 |
| `T102B-ISSUE-008` | Feature Register Missing RLITE | T102B4 (RLITE) was missing from SSOT Feature Register | LLM_Consultant | `RESOLVED` | `HIGH` | 2026-01-15 | T102B4 added in Subphase 1 Activity 1.5 with `in-discovery` status | 2026-01-17 |

**Risks**
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Mitigation Notes | Mitigation Date |
|:---|:------|:------------|:------|:-------|:---------|:--------------|:-----------------|:----------------|
| `T102B-RISK-001` | Intake Drift | SPS Feature bundle may evolve without Request alignment checks; Request becomes stale | Client | `MONITORED` | `HIGH` | 2026-01-17 | Monitoring via `T102B-IF-001 (SPS Intake Contract)`, `T102B-INT-001 (SPS→Request Coordination)`; ongoing alignment checks required | — |
| `T102B-RISK-002` | Gate Evidence Undefined | Approval criteria remain implicit; inconsistent gate enforcement | Client | `MITIGATED` | `MEDIUM` | 2026-01-17 | Gate evidence framework established; see `T102B-STD-003 (Gate Evidence Standard)`, `T102B-IG-005 (Gate Evidence Checklist)`; operational enforcement deferred to Phase 1 RPG development | 2026-01-22 |
| `T102B-RISK-003` | Documentation Trap | Story-level FRs at Request stage block MVP delivery; over-specification | Client | `MONITORED` | `HIGH` | 2026-01-17 | Mitigated via `T102B-CON-002 (No Story FR Mandate)`, `T102B-ADR-003 (Story FR Deferral Standard)`; ongoing monitoring required to prevent documentation creep | — |
| `T102B-RISK-005` | Workflow Undifferentiation | Heavyweight docs applied to lightweight changes; adoption friction | Client | `MONITORED` | `MEDIUM` | 2026-01-17 | Mitigated via `T102B-ADR-004 (Request Lite Specification)`, `T102B-IG-004 (Request Lite Selection)`; ongoing monitoring for RLITE adoption patterns | — |

#### 3. `T102C` Epic: `CONCEPT` — Conceptual Solution Workflow
```yaml
epic_id: 'T102C'
epic_code: 'CONCEPT'
epic_title: 'Concept Workflow'
epic_type: 'new'
epic_status: 'draft'
epic_owner: 'LLM_Consultant'
```

##### i. Purpose  
To establish and deliver a comprehensive Concept workflow that operates as a dynamic, parallel workspace across all consultancy stages (SPS → Request → Design). This Epic will formalize the Concept artifact family as the definitive ADR compendium and decision register, maintaining coherence and traceability without introducing additional approval gates. It enables continuous aggregation of exploration, decisions, and linkages across all project-management scopes, aligned with industry standards.

##### ii. Scope

* **In Scope:**
  - The **structural template** (CST) defining the dynamic workspace framework for cross-scope ADR management and decision aggregation
  - The **procedural guideline** (CPG) covering authoring workflows, client collaboration patterns, and traceability maintenance
  - The manifest framework for lineage tracking and integration with stable consultancy documents
  - Design Log Register framework for maintaining links-only references to detailed design decisions
  - Integration protocols for operating in parallel with SPS, Request, and Design workflows
* **Out of Scope:**
  - Sequential approval gates or workflow dependencies (Concept operates continuously, not sequentially)
  - Story-level implementation details and design logs (owned by Epic T102D)
  - Stable requirements document authoring processes (covered in Epics T102A and T102B)
  - Validation tooling and automation beyond template and process definition

##### iii. Inherited Considerations

| Source Artifact | Source ID | Category | Inherited Rule IDs (with hints) |
| :--- | :--- | :--- | :--- |
| SPS | T102 | Assumptions | `T102-ASSUM-001 (LLM Generation)` |
| SPS | T102 | Constraints | `T102-CON-001 (Format Requirements)`, `T102-CON-003 (Documentation Standards)` |
| SPS | T102 | Quality Goals | `T102-QG-001 (Client Readability)`, `T102-QG-002 (End-to-End Traceability)` |
| SPS | T102 | Dependencies | `T102-DEP-002 (Planner Integration)`, `T102-DEP-003 (Role Definitions)` |
| SPS | T102 | Implementation Guides | `T102-IG-005 (Canonical Header)`, `T102-IG-009 (Traceability Framework)`, `T102-IG-010 (Inheritance Model)` |
| SPS | T102 | Governances | `T102-GDR-001 (Operating Model Standard)`, `T102-GDR-002 (Canonical Header Standard)`, `T102-GDR-004 (Decision Records Standard)`, `T102-STD-005 (ID Governance Standard)`, `T102-GDR-006 (Governance Snapshot Standard)` |

##### iv. Governance & Roadmap

**Scope & Ownership**
- Owner: Epic Lead (LLM_Consultant)
- Decision Owner: Client
- This section provides milestone-level oversight for governance. Detailed plans maintained in external PM tools (ticktick) and Concept ADR index.
- Org baseline (RACI): see `III.B.1 (Organization & Responsibilities)`

**Phase & Gates**
| Phase | Title | Intent | Key Exit Milestone | Duration Band | Gate Approver (A) | Phase Lead (R) | Plan Link |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Foundation | Complete epic definition & research integration | Foundation Readiness: Epic `T102C` approved with stable E-IDs/GDRs/ADRs; research performed and findings integrated | 2-3w | `Client` | `LLM_Consultant` | — |
| 2 | Template Design | Develop `T102C-CST` structural template | Template Validation: CST creates functional concept document, tested with initiative scenario | 3-4w | `Client` | `LLM_Consultant` | — |
| 3 | Process Design | Develop `T102C-CPG` procedural guideline | Process Usability: CPG enables non-technical authoring, integrates with SPS/Request workflows | 2-3w | `Client` | `LLM_Consultant` | — |
| 4 | Integration | Develop `T102C-MANIFEST` & integration testing | Package Completeness: MANIFEST enables template reuse, all features pass integration checklist | 1-2w | `Client` | `LLM_Consultant` | — |

**References**
- External PM Tracking: ticktick (client PM tool)
- Concept ADR Index: `concept_T102#iii-a-initiative-solution-framework`
- Research Basis: `T102A-NOTE-005 (Governance Snapshot Research)`

##### v. Feature Register
<!-- [Status ∈ {proposed,in-discovery,in-request,approved,in-concept,in-delivery,done,parked}. Canonical Link = repo-relative Request path.] -->

| ID | Code | Title | Purpose | Feature Lead (R) | Status | Canonical Link (Request) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `T102C1` | `CST` | Concept Structural Template | Define shell & registers for Concept | `LLM_Consultant` | `in-delivery` | `.../concept/concept_T102C-CST.md` |
| `T102C2` | `CPG` | Concept Procedural Guide | Define gates C0/C1/C2 & authoring norms | `LLM_Consultant` | `proposed` | `.../concept/concept_T102C-CPG.md` |
| `T102C3` | `MANIFEST` | Concept Manifest | Minimal lineage metadata to Planner | `LLM_Consultant` | `proposed` | `.../concept/concept_manifest.json` |

##### vi. Epic Requirements

* **Assumptions**
  <!-- Factors believed to be true but not yet confirmed. Can be adjustable but carry risk. -->
  * **T102C-ASSUM-001 (Document Size)** — Single Concept document can contain cross-PM ADRs without becoming unmanageable
  * **T102C-ASSUM-002 (Context Access)** — LLM_Consultant can effectively correlate information between Concept and stable documents during authoring

* **Constraints**
  <!-- Non-negotiable restrictions or limitations on possible solutions. -->
  * **T102C-CON-001 (ADR Authority)** — Dynamic workspace must not override established GDRs from SPS; variances require explicit citation per `T102-ADR-003`
  * **T102C-CON-002 (Integration Stability)** — Changes to Concept structure must not break existing workflow handoffs during active development

* **Quality Goals**
  <!-- PURPOSE: Define the Epic's specific business objectives and the measurable goals that prove success. -->
  * **T102C-QG-001 (ADR Centralization)** — All Initiative/Epic/Feature ADRs are aggregated and accessible through the dynamic workspace with stable cross-references
  * **T102C-QG-002 (Cross Traceability)** — All fragmented Request/Design artifacts maintain bidirectional links through the Concept register
  * **T102C-QG-003 (Template Reusability)** — Concept structural template supports multiple initiatives with minimal customization effort

* **Dependencies**
  <!-- PURPOSE: List items this Epic relies on and contracts it must honor -->
  * **T102C-DEP-001 (SPS Integration)** — Concept inherits and references all Initiative-level GDRs/ADRs from SPS without duplication
  * **T102C-DEP-002 (Request Coordination)** — Feature-level ADR placement requires coordination protocol with T102B to prevent decision drift
  * **T102C-DEP-003 (Design Sync)** — Design Log Register maintenance depends on T102D providing canonical link updates
  * **T102C-DEP-004 (LLM Context)** — Dynamic workspace effectiveness depends on LLM_Consultant's ability to maintain context across stable and dynamic documents

* **Interfaces**
  <!-- Governance-level role/process touchpoints -->

* **Implementation Guidance**
  <!-- PURPOSE: Define epic-specific implementation patterns and technical conventions -->

##### vii. Epic Research & Notes
<!-- PURPOSE: Provide background, drivers, and key research findings that inform this Epic's direction. -->

**Research**

| Research ID | Title | Summary | Reference | Brief | Report |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `T102C-RES-001` | **Handoff Aggregation** | Validated `T102C-GDR-003` and `T102C-GDR-005` handoff authority and readiness aggregation patterns | `T102C-GDR-003`, `T102C-GDR-005` | [brief](../research/brief/brief_T102C-CONCEPT_handoff-aggregation.md) | [report](../research/report/report_T102C-CONCEPT_handoff-aggregation.md) |


**Notes**

* **T102C-NOTE-001 (Original Context)** — The primary challenge this Epic addresses is the "one-shot" solutioning problem, where passing a `Request` directly to planning results in solutions filled with unvalidated assumptions. LLM context limitations also hinder iterative design over multiple sessions. The `Concept` workflow solves this by creating a **Single Source of Truth** that acts as a dynamic workspace. This artifact supports a **top-down, component-based (Story-by-Story)** design process, where the client is the primary orchestrator, approving each block before proceeding. This approach differs from traditional SAD/GDR documents, which are often static and monolithic, by prioritizing conversational iteration and explicit, granular client approval.
  
* **T102C-NOTE-002 (Proposed Artifact Consolidation)** — To resolve workflow friction, the `Concept` artifact should be merged with the `Design` artifact's function, becoming the single "Story Design Workspace".

<!-- > [DISCREPANCY-WORKFLOW] Conflates Concept and Design. In the intended model, Design is the third stage and Concept remains a parallel, dynamic process; avoid merging their functions. -->

##### viii. Epic Governance Decisions
<!-- Provide a single, auditable index of epic-level governance decisions that guide governance, artifacts, and gates across the epic. -->

| GDR ID | Title | Status | Owner | Effective | Supersedes | Anchor |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `T102C-GDR-001` | Artifact Boundary Standard | Proposed | Client | 2025-09-28 | — | #t102c-gdr-001-artifact-boundary |
| `T102C-GDR-002` | Document Scaling Deferral | Proposed | Client | 2025-09-28 | — | #t102c-gdr-002-scaling-deferral |
| `T102C-GDR-003` | Handoff Authority Standard | Accepted | Client | 2025-09-28 | — | #t102c-gdr-003-handoff-authority |
| `T102C-GDR-004` | Decision Canonicalization Standard | Proposed | Client | 2025-09-28 | — | #t102c-gdr-004-decision-canonicalization |
| `T102C-GDR-005` | Readiness Aggregation Standard | Accepted | Client | 2025-09-28 | — | #t102c-gdr-005-readiness-aggregation |

* **T102C-GDR-001 (Artifact Boundary Standard) {#t102c-gdr-001-artifact-boundary}**
  **Context:** Architectural evolution from Feature-scoped to multi-PM-scope Concept created boundary ambiguity between Request (BRD/SRS) and Concept (ADD) artifacts, risking decision duplication and authority confusion.
  **Decision:** Adopt existing `T102-ADR-003/004/005` framework as authoritative boundary specification: Request = stable requirements (zero embedded ADRs), Concept = dynamic decision workspace (canonical ADR repository), with traceability via ID referencing not content duplication.
  **Consequences:**
  (+) Eliminates decision storage ambiguity between Request and Concept artifacts
  (+) Leverages proven inheritance and canonicalization frameworks
  (+) Maintains clear artifact ownership without authority conflicts
  (±) Requires disciplined adherence to link-don't-duplicate principle
  References:
  `T102-ADR-003 (Explicit Inheritance Model)`,
  `T102-ADR-004 (Decision Records Index)`,
  `T102-ADR-005 (ID Specification & Usage Rules)`,
  `T102C-QG-002 (Cross Traceability)`

* **T102C-GDR-002 (Document Scaling Deferral) {#t102c-gdr-002-scaling-deferral}**
  **Context:** Concept centralization creates potential LLM context window limitations but v1 prioritizes human client experience over agent efficiency; premature splitting could fragment decision coherence.
  **Decision:** Defer document split criteria and auxiliary artifact patterns to v2 scope while monitoring document size impacts; maintain centralized approach in v1 with optimization reserved for next version.
  **Consequences:**
  (+) Maintains decision coherence for human stakeholders in v1
  (+) Avoids premature optimization without proven need
  (+) Allows learning from v1 usage patterns to inform v2 splitting strategies
  (±) Accepts known LLM efficiency constraints in favor of human usability
  (-) May require later architectural refactoring if growth exceeds manageable limits
  **References:** 
  `T102-CON-002 (Scope Limitation)`, 
  `T102-QG-003 (Low-Disruption Implementation)`

* **T102C-GDR-003 (Handoff Authority Standard) {#t102c-gdr-003-handoff-authority}**
  **Context:** Multi-artifact consultancy layer requires clear handoff authority to LLM_Planner. External research validates centralized handoff patterns reduce drift and provide clear accountability, with industry preference for single source of truth approaches per SAFe/42010/ADR best practices.
  **Decision:** Adopt Concept as authoritative handoff locus standard: Concept SHALL maintain the single Handoff Snapshot section that assembles links to approved SPS/Request/Design items, proves readiness via DoR-based checklist, and stamps version IDs for immutability. Request and Design artifacts reference handoff status from Concept only.
  **Consequences:**
  (+) Single accountable handoff authority eliminates drift and cognitive load per industry patterns
  (+) Aligns with established T102C-GDR-001/004 boundaries (Concept=decisions, Request=requirements)
  (+) Supports 42010 coherent architecture description principles
  (±) Requires disciplined "link-don't-duplicate" adherence and snapshot maintenance
  **References:**
  `T102C-GDR-001 (Artifact Boundary Standard)`,
  `T102C-GDR-004 (Decision Canonicalization Standard)`,
  `T102-DEP-002 (Planner Integration)`,
  `T102C-DEP-001 (SPS Integration)`,
  `T102C-QG-002 (Cross Traceability)`

* **T102C-GDR-004 (Decision Canonicalization Standard) {#t102c-gdr-004-decision-canonicalization}**
  **Context:** Multi-scope ADR management requires canonical storage location to prevent decision drift and ensure single source of truth across PM scopes.
  **Decision:** Adopt `T102-ADR-004` as authoritative decision canonicalization standard: ALL ADRs (Initiative/Epic/Feature) stored in Concept with references from Request/Design artifacts; Story-level ADRs remain in Design Log per `T102D` scope.
  **Consequences:**
  (+) Establishes single source of truth for all architectural decisions
  (+) Eliminates decision duplication between Request and Concept artifacts
  (+) Enables consistent audit trail across all PM scopes
  (±) Requires strict adherence to reference-only pattern in downstream artifacts
  **References:** 
  `T102-ADR-004 (Decision Records Index)`, 
  `T102-GDR-001 (Operating Model Standard)`, 
  `T102C-QG-001 (ADR Centralization)`

* **T102C-GDR-005 (Readiness Aggregation Standard) {#t102c-gdr-005-readiness-aggregation}**
  **Context:** Complex PM hierarchy requires lean readiness visibility for handoff orchestration. External research validates manual DoR-based aggregation with traffic-light status as industry standard for v1 implementations, avoiding automation overhead while providing human decision-maker visibility.
  **Decision:** Adopt manual YAML readiness snapshot standard: Concept SHALL maintain Readiness Snapshot section with Initiative/Epic/Feature roll-up table showing state/ready status/top blockers, using DoR-derived entry criteria with 80% threshold and Client override capability. No automation required in v1 scope.
  **Consequences:**
  (+) Lean human-first visibility aligned with SAFe Portfolio/ART Kanban patterns
  (+) Satisfies minimal automation from `T102-CON-002` and low-disruption from `T102-QG-003`.
  (+) Provides Client orchestration visibility without cognitive overload per Team Topologies guidance
  (±) Requires manual weekly cadence maintenance
  (-) Not live dashboard; automation deferred to v2
  **References:**
  `T102-CON-002 (Scope Limitation)`,
  `T102-QG-003 (Low-Disruption Implementation)`,
  `T102-DEP-003 (Role Definitions)`,
  `T102C-ASSUM-001 (Document Size)`

##### ix. Epic Issues & Risks

**Issues**
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Resolution Notes | Resolution Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `T102C-ISSUE-001` | Boundary Definition | Concept ADRs vs Request feature-level decision boundaries during T102B/T102C integration. | Client | `RESOLVED` | `LOW` | 2025-09-27 | Applied `T102C-GDR-001` framework establishing Request=stable requirements, Concept=dynamic ADR workspace | 2025-09-28 |
| `T102C-ISSUE-002` | Document Threshold | Criteria for when Concept document requires splitting or auxiliary artifacts. | Client | `DEFERRED` | `MEDIUM` | 2025-09-27 | Structured deferral to v2 scope per `T102C-GDR-002` with monitoring; v1 maintains centralized approach - | - |
| `T102C-ISSUE-003` | Handoff Authority | Determine T102C as authoritative source for final handoff package to LLM_Planner. | Client | `RESOLVED` | `HIGH` | 2025-09-27 | External research validated Concept as authoritative handoff locus per `T102C-GDR-003` industry standards | 2025-09-28 |
| `T102C-ISSUE-004` | ADR Location | Canonical storage location for decision criteria and solution options during T102C development. | Client | `RESOLVED` | `MEDIUM` | 2025-09-27 | `T102C-GDR-004` framework establishes Concept as canonical ADR source with Request references-only | 2025-09-28 |
| `T102C-ISSUE-005` | Readiness Tracking | Define how Concept aggregates story/feature readiness for handoff without prescribing low-level YAML. | Client | `RESOLVED` | `HIGH` | 2025-09-27 | External research validated manual YAML readiness snapshot per `T102C-GDR-005` with DoR-based aggregation | 2025-09-28 |

**Risks**
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Mitigation Notes | Mitigation Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `T102C-RISK-001` | Context Overload | LLM_Consultant cannot effectively manage stable/dynamic document updates simultaneously, causing drift or omissions. Future document splitting considerations remain open if context bloat becomes critical for agent performance. | Client | `MITIGATED` | `MEDIUM` | 2025-09-27 | MITIGATED through `T102C-GDR-001` boundary separation and "link-don't-duplicate" principle. External research validated this approach. | 2025-09-28 |
| `T102C-RISK-002` | Decision Authority Confusion | ADRs stored in Concept become disconnected from governing GDRs, creating unclear decision authority and conflicts. | Client | `MITIGATED` | `LOW` | 2025-09-27 | MITIGATED through `T102C-GDR-004` canonical storage standard and `T102-ADR-003` explicit inheritance model. | 2025-09-28 |
| `T102C-RISK-003` | Integration Complexity | Cross-epic integration requirements (T102B/T102D) create development dependencies that delay epic completion. | Client | `MITIGATED` | `LOW` | 2025-09-27 | MITIGATED through completed `T102C` governance framework providing stable foundation. `T102B` and `T102D` epics can reference T102C. | 2025-09-28 | 

##### x. Epic Changelog

* **2025-09-11** — Re-cast T102C under new Epic template; added links-only Epic Governance Decisions.
* **2025-09-28** — Major update with stable E-IDs followed the establishment of E-GDRs; resolve all T102C issues & risks via external research integration. 

---

#### 4. `T102D` Epic: `DESIGN` - Design Log Workflow 
```yaml
epic_id: 'T102D'
epic_code: 'DESIGN'
epic_title: 'Design Log Workflow'
epic_type: 'new'
epic_status: 'draft'
epic_owner: 'LLM_Consultant'
```

##### i. Purpose
Establish a **story-level Design Log** artifact family that is optional for Consultancy Layer (used when clients want to dive deeper) and authoritative for DDP. Each Design Log aggregates **Final Proposed Solution, Integration Notes, Dependencies, Decision Record (ADR), Traceability, and Ripple Test Notes** per story. 

<!-- > [DISCREPANCY-WORKFLOW] Frames Design as optional for Consultancy Layer. In the intended workflow, Design is the third stage following SPS and Request (with Concept running in parallel). -->

##### ii. Scope

* **In Scope:** Design Structural Template (DST), Design Procedural Guideline (DPG), Design Manifest (DMA); Story ADR pattern; canonical links from Concept §III-B register.
* **Out of Scope:** Feature-level framework (owned by Concept §III-A); Request content/gates.


##### iii. Inherited Considerations

| Source Artifact | Source ID | Category | Inherited Rule IDs |
| :--- | :--- | :--- | :--- |
| SPS | T102 | Constraints | `T102-CON-001 (Markdown+YAML)`, `T102-CON-003 (Doc standards)` |
| SPS | T102 | Quality Goals | `T102-QG-002 (End-to-End Traceability)` |
| SPS | T102 | Dependencies | `T102-DEP-002 (Planner Integration)`, `T102-DEP-003 (Role Definitions)` |
| SPS | T102 | Implementation Guides | `T102-IG-005 (Canonical Header)`, `T102-IG-007 (ID Standard)`, `T102-IG-010 (Inheritance Model)` |

##### iv. Governance & Roadmap

**Scope & Ownership**
- Owner: Epic Lead (`LLM_Consultant`)
- Decision Owner: `Client`
- Org baseline (RACI): see `III.B.1 (Organization & Responsibilities)`

**Phase & Gates**
| Phase | Title | Intent | Key Exit Milestone | Duration Band | Gate Approver (A) | Phase Lead (R) | Plan Link |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

**References**

##### v. Feature Register
<!-- [Status ∈ {proposed,in-discovery,in-request,approved,in-concept,in-delivery,done,parked}. Canonical Link = repo-relative Request path.] -->

| ID | Code | Title | Purpose | Feature Lead (R) | Status | Canonical Link (Request) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `T102D-DST` | `DST` | Design Structural Template | Define the per-story design log shell | `LLM_Consultant` | `proposed` | `.../design/design_T102D-DST.md` |
| `T102D-DPG` | `DPG` | Design Procedural Guideline | Authoring cadence, log rules, approvals | `LLM_Consultant` | `proposed` | `.../design/design_T102D-DPG.md` |
| `T102D-MANIFEST` | `MANIFEST` | Design Manifest | Minimal lineage for planner ingestion | `LLM_Consultant` | `proposed` | `.../design/design_manifest.json` |

##### vi. Epic Requirements

* **Assumptions**
  <!-- Factors believed to be true but not yet confirmed. Can be adjustable but carry risk. -->
  * `T102D-ASSUM-01` — Stories may proceed without a Design Log when the Concept framework is sufficient.

* **Constraints**
  <!-- Non-negotiable restrictions or limitations on possible solutions. -->
  * `T102D-CON-01` — No duplication of Concept’s feature-level decisions.

* **Quality Goals**
  <!-- PURPOSE: Define the Epic's specific business objectives and the measurable goals that prove success. -->
  * `T102D-QG-01 (Completeness)` Each Design Log includes: Integration Notes, Story-local Dependencies, Final Proposed Solution, Decision Record, Traceability, Ripple Tests;
  * `T102D-QG-02 (Traceability)` 100% Design ADRs link back to Request FR/Story IDs and forward to code/tests (when available).
  * `T102D-QG-03 (Diff-Friendliness)` Changes are small, merge-safe, and chronologically indexed.

* **Dependencies**
  <!-- PURPOSE: List items this Epic relies on and contracts it must honor -->
  * `T102D-DEP-01` — Consumes Concept §III-B “Design Log Register (links-only)”.
  * `T102D-DEP-02` — Emits Planner-friendly manifest (IDs & anchors);

* **Interfaces**
  <!-- Governance-level role/process touchpoints -->

* **Implementation Guidance**
  <!-- PURPOSE: Define epic-specific implementation patterns and technical conventions -->

##### vii. Epic Research & Notes
<!-- PURPOSE: Provide background, drivers, and key research findings that inform this Epic's direction. -->

**Research**
| Research ID | Title | Summary | Reference | Brief | Report |
| :--- | :--- | :--- | :--- | :--- | :--- |

**Notes**
* `T102D-NOTE-01` — During Consultancy, Design Log use is **optional**; in DDP it becomes the primary story-design record (ownership split documented in SPSPG).
* `T102D-NOTE-02` — Keep ADR bodies in Design (story scope); Concept carries links-only.

##### viii. Epic Governance Decisions

| GDR ID | Title | Status | Owner | Effective | Supersedes | Anchor |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |

##### ix. Epic Issues & Risks

**Issues**
| ID               | Description                                                  | Owner           | Status    |
| :--------------- | :----------------------------------------------------------- | :-------------- | :-------- |
| `T102D-ISSUE-01` | Define canonical “Decision Record” summary format per story. | LLM_Consultant | Open      |

**Risks**
| ID               | Description                                                  | Owner           | Status    |
| :--------------- | :----------------------------------------------------------- | :-------------- | :-------- |
| `T102D-RISK-01`  | Risk of duplication if authors paste feature decisions here. | Governance      | Monitored |

##### x. Epic Changelog

* **2025-09-11** — Initial T102D Epic added; optional Consultancy use, DDP-primary ownership clarified.


#### 6. `T102F` Epic: `GENERAL` - General & System Integration

```yaml
epic_id: 'T102E'
epic_code: 'GENERAL'
epic_title: 'General & System Integration'
epic_type: 'general'
epic_status: 'draft'
epic_owner: 'LLM_Consultant'
```

##### i. Purpose

##### ii. Scope

##### iii. Inherited Considerations

##### iv. Governance & Roadmap

**Scope & Ownership**
- Owner: Epic Lead (`LLM_Consultant`)
- Decision Owner: `Client`
- Org baseline (RACI): see `III.B.1 (Organization & Responsibilities)`

**Phase & Gates**
| Phase | Title | Intent | Key Exit Milestone | Duration Band | Gate Approver (A) | Phase Lead (R) | Plan Link |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

**References**

##### v. Feature Register
<!-- [Status ∈ {proposed,in-discovery,in-request,approved,in-concept,in-delivery,done,parked}. Canonical Link = repo-relative Request path.] -->

| ID | Code | Title | Purpose | Feature Lead (R) | Status | Canonical Link (Request) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |

##### vi. Epic Requirements

* **Assumptions**
  <!-- Factors believed to be true but not yet confirmed. Can be adjustable but carry risk. -->

* **Constraints**
  <!-- Non-negotiable restrictions or limitations on possible solutions. -->

* **Quality Goals**
  <!-- PURPOSE: Define the Epic's specific business objectives and the measurable goals that prove success. -->

* **Dependencies**
  <!-- PURPOSE: List items this Epic relies on and contracts it must honor -->

* **Interfaces**
  <!-- Governance-level role/process touchpoints -->

* **Implementation Guidance**
  <!-- PURPOSE: Define epic-specific implementation patterns and technical conventions -->

##### vii. Epic Research & Notes
<!-- PURPOSE: Provide background, drivers, and key research findings that inform this Epic's direction. -->

**Research**
| Research ID | Title | Summary | Reference | Brief | Report |
| :--- | :--- | :--- | :--- | :--- | :--- |

**Notes**

##### viii. Epic Governance Decisions

| GDR ID | Title | Status | Owner | Effective | Supersedes | Anchor |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |

##### ix. Epic Issues & Risks

**Issues**
| ID | Title | Description | Owner | Status |
| :--- | :--- | :--- | :--- | :--- |

**Risks**
| ID | Title | Description | Owner | Status |
| :--- | :--- | :--- | :--- | :--- |

##### x. Epic Changelog

### D. Project Glossary

*   **SPS Artifact:** The first artifact in the consultancy workflow, focused on exploratory problem discovery (Discover phase).
*   **Request Artifact:** The second artifact, focused on structured problem decomposition and grounding against project context (Define phase).
*   **Concept Artifact:** The third and final artifact in the consultancy workflow, focused on solution exploration and selection (Develop/Deliver phase). It translates the "what" from the `Request` into potential "how" options.

<!-- > [DISCREPANCY-WORKFLOW] Labels Concept as the "third and final" artifact. For the intended model, Concept should be described as a parallel, continuous process spanning SPS, Request, and Design; Design is the third stage. -->

## IV. GLOSSARY

---

## V. APPENDIX 

### A. Amendment Log
| Date | Change Requester | Affected Req. ID | Summary of Change |
| :--- | :--- | :--- | :--- |
| 2025-08-01 | Client | Initial | Initial SPS creation |

---

## VI. VALIDATION CHECKLIST

- [x] The artifact's YAML header is complete and syntactically correct.
- [x] The Problem Definition (Section III-A) has received explicit client approval.
- [ ] All known open issues and risks have been logged in Section III-D.
- [ ] The 'Next Steps' section clearly defines the handoff to the Request workflow.

---

## VII. STAKEHOLDER SIGN-OFF

By signing off, stakeholders agree that the problems and requirements detailed in this document accurately reflect the desired work. Architectural and implementation design will be based on the contents of this artifact.

*   **Client:** _________________________ (Name, Date)
*   **Consultant:** _________________________ (Name, Date)

---


## VIII. NEXT STEPS

**Primary Stakeholder & Decision Owner:** `Client` 

**Downstream Consumer:** `LLM_Consultant` 

**Action:** Upon this Epic being 'Approved', the `LLM_Consultant` is authorized to process each `Epic` that has an individual status of 'Approved'. For each approved `Epic`, ingest its content (Purpose, Features, and relevant Global Considerations from Section III-C) to populate a new, dedicated `request` artifact for detailed analysis and requirement decomposition.

---

## IX. CHANGELOG

*   **v1.1.0:** Initial SPS creation documenting the problem of linking two templates.

