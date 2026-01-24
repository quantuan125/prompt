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

#### 4. Success Criteria & Quality Goals
<!-- Measurable targets that define project success. Per ISO 29148, these must be verifiable, singular, and complete with clear success/failure criteria. -->
* **T102-QG-001 (Client Readability)** — Artifacts are understandable by non-technical stakeholders (aim ≥ "clear" on internal rubric).
* **T102-QG-002 (End-to-End Traceability)** — Every option/decision maps forward/backward across artifacts and into Planner hand-off.
* **T102-QG-003 (Low-Disruption Implementation)** — Prefer changes that minimize author retraining and document churn in v1; reserve stricter automation for v2.

#### 5. Dependencies 
<!-- External prerequisites and commitments. -->
* **T102-DEP-001 (Client Engagement)** — Client must provide decision-making commitment within 2-business-day Service Level Agreement (SLA) across all workflow gates
* **T102-DEP-002 (Planner Integration)** — Downstream LLM_Planner system must be capable of consuming standardized handoff schema

#### 6. Interfaces
<!-- Governance-level role/process touchpoints -->
* **T102-IF-001 (Planner Handoff)** — Consultancy Layer delivers an approved, minimal handoff bundle at the defined gate; Planner Layer acknowledges receipt and assumes ownership for planning. Payload fields and evidence are defined in dedicated workflows and artifact.
* **T102-IF-002 (Client Review)** — Client is the decision owner at gates; expected turnaround ≤ 2 business days; approval signals are recorded in the artifact per governance rules.
* **T102-IF-003 (Roles Collaboration)** — Defines Consultant–Planner relationship and how clarification is requested, response channels, and the boundary of change ownership post-handoff.
* **T102-IF-004 (Co-authoring Consultancy)** — Client and Consultant co-author all Consultancy Layers workflows and documents. Define the working channels, meeting rhythm, who edits vs approves, and that the repo is the source of truth.

#### 7. Implementation Guidance
<!-- Technical guidance for execution teams -->

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

#### 8. Research & Notes

**Research**
| RES ID | Title | Summary | Linked To | Brief | Report |
|--------|-------|---------|-----------|-------|--------|
| `T102-RES-001` | **Research Integration Workflow** | Established three-tier placement strategy, LLM quality control framework, RES-### ID system; recommended dedicated Epic T102E for implementation | `T102-ISSUE-005`, `T102-GDR-006`, `T102-GDR-007` | [brief](../research/brief/brief_T102-CONSULTANT_research-integration-workflow.md) | [report](../research/report/report_T102-CONSULTANT_research-integration-workflow.md) |
| `T102-RES-002` | **Roadmap Viability** | Confirmed governance snapshot approach aligns with PRINCE2/PMI/SAFe standards; validated hybrid model with governance milestones in SPS and operational plans external | `T102A-GDR-001`, `T102C-GDR-003`, `T102C-GDR-005` | [brief](../research/brief/brief_T102-CONSULTANT_roadmap-viability.md) | [report](../research/report/report_T102-CONSULTANT_roadmap-viability.md) |
| `T102-RES-003` | **Initiative Status Assessment** | Assessed initiative status, bottlenecks, and documentation debt; identified YAML/header and register integrity gaps requiring follow-on hygiene work | `T102-GDR-002`, `T102-ISSUE-005` | [brief](../research/brief/brief_T102-RES-003_initiative-status-assessment.md) | [report](../research/report/report_T102-RES-003_initiative-status-assessment.md) |


**Notes**
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

#### 9. Initiative Governance Decisions

| GDR ID | Title | Status | Owner | Effective | Supersedes | Anchor |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `T102-GDR-001` | Operating Model Standard | Accepted | Client | 2025-09-07 | — | #t102-gdr-consultancy-model-standard |
| `T102-GDR-002` | Canonical Header Standard | Accepted | Client | 2025-09-14 | — | #t102-gdr-002-header-standard |
| `T102-GDR-003` | Inheritance Model Standard | Accepted | Client | 2025-09-14 | — | #t102-gdr-003-inheritance-standard |
| `T102-GDR-004` | Decision Records Standard | Accepted | 2025-09-18 | — | #t102-gdr-004-drs-index-standard |
| `T102-GDR-005` | ID Governance Standard | Accepted | Client | 2025-09-22 | — | #t102-gdr-005-id-governance |
| `T102-GDR-006` | Research Workflow Standard | Proposed | Client | 2025-10-05 | — | #t102-gdr-006-research-workflow |
| `T102-GDR-007` | LLM Quality Control | Proposed | Client | 2025-10-05 | — | #t102-gdr-007-llm-quality-control |
| `T102-GDR-008` | Organisation Baseline Standard | Proposed | Client | 2026-01-12 | — | #t102-gdr-008-organisation-baseline-standard |

* **T102-GDR-001 (Operating Model Standard) {#t102-gdr-001-consultancy-model-standard}**
  **Context** Workflow inversion and blurred roles across SPS/Request/Concept/Design caused duplicated decisions, anchor drift, and rework. A unified operating model with explicit approvals and precedence is required: SPS = initiative & epic governance, Request = feature requirements only; Design = story‑level implementation records; Concept = ADR compendium for option evaluation and selection across PM-levels. 
  **Decision** Adopt `T102-ADR-001 (Consultancy Operating Model)` and establish a four-tier consultancy workflows and artifacts hierarchy with clear governance authority:
  - **Workflow Sequencing**: The canonical consultancy sequence is SPS  → Request → Design. Concept is a parallel, dynamic workspace for ADRs and registers that spans all stages. Per‑story Design logs are optional. 
  - **Governance Authority**: Client owns all approval gates and trade-off decisions
  - **Artifact Ownership**: LLM_Consultant authors and own all artifacts. 
  - **Decision Precedence**: Initiative GDR > Initiative ADR > Epic ADR > Feature ADR > Story ADR
  - **Handoff Protocol**: Each tier requires explicit approval before downstream work begins
  **Consequences.**
  (+) Clear decision authority and accountability chain across all consultancy work
  (+) Eliminates governance ambiguity and artifact ownership conflicts
  (+) Enables consistent audit trail and compliance verification
  (±) Requires discipline in maintaining hierarchical decision precedence
  **References.** 
  `T102-CON-001 (Format Requirements)`; 
  `T102-QG-002 (End-to-End Traceability)`; 
  `T102-DEP-004 (Handoff Protocol)`; 
  `T102-IG-005 (Canonical Header)`; 
  `T102-IG-009 (Traceability Framework)`;
  `T102-NOTE-03 (Industry Standards)`


* **T102-GDR-002 (Canonical Header Standard) {#t102-gdr-002-header-standard}**
  **Context.** We need a single, auditable and consistent source for **artifact identity & governance keys** across all artifact types (SPS/Request/Concept/Design). Drift emerges when templates restate keys locally.
  **Decision.** Adopt `T102-ADR-002 (Canonical YAML Header)` as the mandatory header spec for all artifacts (SPS/REQUEST/CONCEPT/DESIGN). Ownership = Client; changes logged via this GDR. 
  **Consequences.** 
  (+) Eliminates header schema drift across all consultancy artifacts
  (+) Establishes single source of truth for artifact identity and governance keys
  (+) Enables future predictable validation and automation development
  (+) Clear governance authority and change control for header evolution
  (±) Requires discipline to maintain conformance without local schema drift
  (-) Initial migration effort for existing artifacts with non-conforming headers
  **References.** 
  `T102-IG-005 (Canonical Header)`, 
  `T102-CON-001 (Format Requirements)`, 
  `T102-QG-002 (End-to-End Traceability)`

* **T102-GDR-003 (Inheritance Model Standard) {#t102-gdr-003-inheritance-standard}**
  * **Context** “Delta-only” by convention proved too weak; duplication/drift appeared across consultancy workflows and their corresponding artifacts. An **explicit inheritance** rule is required.
  * **Decision** Adopt `T102-ADR-003 (Explicit Inheritance Model)` as the **inheritance model** across all Project Management scopes with structured tables and expliticit IDs references.
  * **Consequences** Clear SoT in SPS; downstream brevity without ambiguity; enables validator rules for presence of inherited IDs.
  * **References** `T102-IG-010 (Inheritance Model)`, `T102-NOTE-04 (Inheritance Philosophy)`.;

* **T102-GDR-004 (Decision Records Standard) {#t102-gdr-004-drs-standard}**
  **Context.** ADR/GDR formats and anchors vary across artifacts, causing drift and blocking automation.
  **Decision.** Adopt `T102-ADR-004 (Decision Records Index)` as the single, Client-owned standard for decision record schemas across SPS/Request/Concept/Design.
  **Consequences.**
  (+) One schema and anchor pattern; prevents drift and ensures auditability
  (+) Enables automation and consistent traceability across layers
  (+) Aligns with decision precedence model
  (±) Client approval required for schema changes
  (-) Migrate existing non-conforming records
  **References.** 
  `T102-IG-007 (ID Standard)`, 
  `T102-IG-008 (Decision Logging)`, 
  `T102-QG-002 (End-to-End Traceability)`, 
  `T102-DEP-004 (Handoff Protocol)`

* **T102-GDR-005 (ID Governance Standard) {#t102-gdr-005-id-governance}**
  **Context.** As artifacts scale, ID patterns for considerations, requirements, and decisions diverge (titles, anchors, categories), creating ambiguity and broken traceability. Existing standards govern headers, inheritance, and decision indices but do not fully constrain ID construction and usage across scopes.
  **Decision.** Adopt `T102-ADR-005 (ID Specification & Rules)` as the authoritative standard for ID construction, categorization, anchors, and referencing semantics across SPS/Request/Concept/Design. Enforce scope ID regex baselines (IID/EID/FID/SID), category tokens and sub-ID forms (e.g., `-FR-##`), formal vs. informal reference rules, and the Inherited Considerations table contract. Precedence and one-way inheritance apply; variances require a local ADR.
  **Consequences.**
  (+) Eliminates ID drift; improves auditability and automation readiness
  (+) Stabilizes anchors and cross-links across all artifacts
  (±) Small author training and migration for legacy IDs
  (-) Requires updates to any non-conforming anchors/IDs
  **References.** 
  `T102-CON-001 (Format Requirements)`, 
  `T102-QG-002 (End-to-End Traceability)`, 
  `T102-GDR-002 (Canonical Header Standard)`, 
  `T102-GDR-003 (Inheritance Model Standard)`, 
  `T102-GDR-004 (Decision Records Standard)`,


* **T102-GDR-006 (Research Workflow Standard) {#t102-gdr-006-research-workflow}**
  **Context.** Ad-hoc research commissioning created scalability concerns: document bloat from embedded NOTEs (`T102A-RISK-003`), undefined quality gates enabling unverified LLM content integration, and traceability gaps violating `T102-QG-002`. External research (`T102-RES-003`) validated industry patterns (PRINCE2/PMI/SAFe/ISO 29148/BABOK v3) supporting formal research workflows with standard templates, validation checkpoints, and structured integration.
  **Decision.** Adopt formal research workflow standard across all consultancy phases (SPS/REQUEST/CONCEPT/DESIGN). All significant uncertainties or knowledge gaps SHALL be addressed via commissioned research following standardized process: (1) Research Brief approval before execution (Gate 1), (2) Research Report validation before governance integration (Gate 2), (3) Research findings indexed using `RES-###` ID pattern with traceable references per `T102-QG-002` (End-to-End Traceability), (4) LLM-generated research subject to mandatory human verification per `T102-QG-004` (Research Validation Quality). Implementation specifics delegated to Epic `T102E` with structural standards defined in `T102-ADR-006 (Research Artifacts Index)` per consultancy operating model separation of governance (GDR) vs architecture (ADR).
  **Consequences.**
  (+) Prevents document bloat via structured placement strategy (inline/appendix/external) balancing `T102-QG-001 (Client Readability)` with maintainability
  (+) Establishes repeatable, auditable research process with clear quality gates preventing unverified content integration
  (+) Aligns with industry PID best practices (PRINCE2 annexes, PMI Charter references, SAFe lean documentation)
  (±) Requires procedural guideline updates (SPSPG, RPG, CPG) and team training on new templates/workflows
  (-) Initial migration effort for existing research NOTEs to `RES-###` pattern
  **References.**
  `T102-ISSUE-005 (Research Integration Pattern)`,
  `T102-QG-001 (Client Readability)`,
  `T102-QG-002 (End-to-End Traceability)`,
  `T102-QG-004 (Research Validation Quality)`,
  `T102-CON-001 (Format Requirements)`,
  `T102-IG-011 (Research Artifact Standards)`,
  `T102-RES-003 (Research Integration Governance Research)`

* **T102-GDR-007 (LLM Quality Control) {#t102-gdr-007-llm-quality-control}**
  **Context.** ChatGPT Deep Research (5-10 min turnaround per `T102-DEP-003`) currently lacks quality controls despite critical risks: 20-30% hallucination rate (academic surveys), traceability gaps, bias/incompleteness, automation bias, security concerns. Real-world case (NY lawyers sanctioned for ChatGPT fake citations) demonstrates governance failure consequences. `T102-ASSUM-003` accepts deferred validation for v1, leveraging LLM_Consultant filtering, but Client acknowledges risks requiring mitigation framework.
  **Decision.** Adopt LLM Research Quality Control framework with mandatory safeguards: 
  (1) Source verification — all LLM factual claims validated against authoritative sources before acceptance; unverified content excluded or marked "conjecture", 
  (2) Human-in-the-loop review — Gate 2 validation checklist (factual accuracy, completeness, clarity) performed by named human owner before governance integration, 
  (3) Traceability & logging — all LLM interactions logged as project records; research reports include methodology with source list; metadata for model version/prompts/generation timestamp, 
  (4) Transparency & disclosure — LLM usage disclosed in research methodology; precedence rule that no GDR/requirement accepted on LLM-only evidence without validation, 
  (5) Risk mitigation mechanisms — RAG (retrieval-augmented generation) preferred; chain-of-thought prompting; diverse data sources enumeration; escalation triggers for legal/regulatory content requiring human expert.
  **Consequences.**
  (+) Mitigates hallucination risk from critical (20-30%) to manageable levels via verification
  (+) Maintains audit trail for governance compliance (EU AI Act, ISO frameworks alignment)
  (+) Establishes "trust but verify" culture preventing automation bias
  (+) Preserves LLM efficiency (5-10 min) while ensuring governance quality
  (±) Requires human review overhead (~30-60 min validation per report)
  (-) Initial team training on cognitive biases and verification techniques
  **References.**
  `T102-ISSUE-005 (Research Integration Pattern)`,
  `T102-DEP-003 (LLM Research Agent)`,
  `T102-ASSUM-003 (Research Validation Deferral)`,
  `T102-QG-002 (End-to-End Traceability)`,
  `T102-RES-003 (Research Integration Governance Research)`

* **T102-GDR-008 (Organisation Baseline Standard) {#t102-gdr-008-organisation-baseline-standard}**
  **Context.** Organization responsibilities are referenced across initiative and epic dossiers; without a stable baseline, actor labels drift and governance ownership becomes ambiguous.
  **Decision.** Adopt `T102-ADR-008 (Organisation Baseline Standard)`, to mandate a single initiative-level `III.B.1 Organization & Responsibilities` baseline with a stable actor-to-role mapping and governance RACI.
  **Consequences.**
  (+) Keeps actor labels consistent across epics and feature registers
  (+) Enables governance snapshots to stay stable while plans evolve
  (±) Requires occasional baseline updates when the operating model changes
  **References.**
  `T102-GDR-003 (Inheritance Model Standard)`, `T102-GDR-001 (Operating Model Standard)`


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
| SPS | T102 | Governance | `T102-GDR-001 (Operating Model Standard)`, `T102-GDR-002 (Canonical Header Standard)`, `T102-GDR-003 (Inheritance Model Standard)`, `T102-GDR-004 (Decision Records Standard)`, `T102-GDR-005 (ID Governance Standard)` |

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

| RES ID | Title | Summary | Linked To | Brief | Report |
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
| SPS | T102 | Governance | `T102-GDR-001 (Operating Model Standard)`, `T102-GDR-003 (Inheritance Model Standard)`, `T102-GDR-005 (ID Governance Standard)` |

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
  <!-- Factors believed to be true but not yet confirmed. Can be adjustable but carry risk. -->
  * **T102B-ASSUM-001:** Each SPS Feature provides enough narrative to derive initial FRs and propose first-pass ACs in workshop.;

* **Constraints**
  <!-- Non-negotiable restrictions or limitations on possible solutions. -->
  * **T102B-CON-001:** **No custom Markdown processors** in v1 (keep authoring/rendering simple and portable).

* **Quality Goals**
  <!-- PURPOSE: Define the Epic's specific business objectives and the measurable goals that prove success. -->
  * **T102B-QG-001 (Testability):** 100% of Requests contain **one consolidated AC section per Story** in valid Gherkin.;
  * **T102B-QG-002 (Traceability):** 100% of FRs map to Story IDs and appear in the AC register; each Request links back to its SPS Feature and forward to Concept.;
  * **T102B-QG-003 (Review SLA):** Initial review cycle to decision (approve/rework) closes within ≤ 2 business days for pilot features.
  * **T102B-QG-004 (Header Consistency):** All Requests use canonical YAML header keys and repo-relative links;

* **Dependencies**
  <!-- PURPOSE: List items this Epic relies on and contracts it must honor -->
  * **T102B-DEP-001 (SPS Intake Alignment):** Final **T102A-SPSST** fields must align to Request intake; SPS Feature bundle (ID, Purpose, assumptions/constraints refs) is the **only** intake.
  * **T102B-DEP-002 (Industry Standards):** Align to **ISO/IEC/IEEE 29148** for requirements quality and traceability.;
  * **T102B-DEP-003 (Portfolio Standards):** Conform to `prompt_main.md` and `documentation/general.md` for section ordering, YAML keys, and versioning.

* **Interfaces**
  <!-- Governance-level role/process touchpoints -->
  * **T102B-DEP-004 (Interfaces):**
  <!-- NOTE: This content to be migrated to T102B-IF-001/002/003 in Subphase 2 Activity 2.3 -->
  - **Input:** SPS Feature bundle (ID, Purpose, optional story notes, Initiative considerations).
  - **Output:** **Approved Request** (as defined by `T102B-RPG` gate criteria) consumable by Concept/Design or direct PLAN handoff.

* **Implementation Guidance**
  <!-- PURPOSE: Define epic-specific implementation patterns and technical conventions -->

##### vii. Epic Research & Notes
<!-- PURPOSE: Provide background, drivers, and key research findings that inform this Epic's direction. -->

**Research**
| RES ID | Title | Summary | Linked To | Brief | Report |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `T102B-RES-001` | **Request Artifact Analysis** | External comparison of Request artifact against industry standards; recommends Request Lite, deferring story-level FRs to Design, and reducing FR/IG duplication | `T102B-ISSUE-003`, `T102B1` | [brief](../research/brief/brief_T102B-RES-001_request-artifact-analysis.md) | [report](../research/report/report_T102B-RES-001_request-artifact-analysis.md) |

**Notes**
* **T102B-NOTE-001 (Epic Purpose):** The primary challenge this Epic addresses is the "one-shot" solutioning problem, where passing a `Request` directly to planning results in solutions filled with unvalidated assumptions. LLM context limitations also hinder iterative design over multiple sessions. The `Concept` workflow solves this by creating a **Single Source of Truth** that acts as a dynamic workspace. This artifact supports a **top-down, component-based (Story-by-Story)** design process, where the client is the primary orchestrator, approving each block before proceeding. This approach differs from traditional SAD/GDR documents, which are often static and monolithic, by prioritizing conversational iteration and explicit, granular client approval.
* **T102B-NOTE-002 (Model-B Governance):** Feature-level Requests keep specs small and parallelizable; the Epic provides overall control and is described in the SPS.;
* **T102B-NOTE-003 (Industry Alignment):** Double-Diamond separation (SPS=Define, Request/Concept=Develop/Deliver) reduces premature solutioning; ACs live at **story** granularity.;
* **T102B-NOTE-004 (Agent Compatibility):** Focused, linked artifacts perform better in constrained LLM contexts than monoliths.;
##### viii. Epic Governance Decisions

| GDR ID | Title | Status | Scope | Related Req/Rules | Link |
| :--- | :--- | :--- | :--- | :--- | :--- |

##### ix. Epic Issues & Risks

**Issues**
| ID | Title | Description | Owner | Status |
| :--- | :--- | :--- | :--- | :--- |
| `T102B-ISSUE-001` | YAML Keys Finalization | Finalize the exact Request YAML key set & enums (align with `prompt_main.md`). | Client | Open |
| `T102B-ISSUE-002` | Manifest Format Decision | Decide manifest format (`.json` vs `.md`) and storage path. | Client | Open |
| `T102B-ISSUE-003` | Story Register Scope | The current `Stories & Specification` section may be too detailed, forcing premature work. Investigate reducing its depth in favor of a lighter "Story Register." | Client | Open |

**Risks**
| ID | Title | Description | Owner | Status |
| :--- | :--- | :--- | :--- | :--- |
| `T102B-RISK-001` | Intake Drift | Drift between SPSST intake fields and RST sections causing rework. | Client | Monitored |
| `T102B-RISK-002` | Gate Evidence Undefined | Gate approval evidence undefined until RPG finalized; may delay handoffs. | Client | Monitored |

##### x. Epic Changelog

* **2025-08-31** — Initial T102B Epic skeleton created; set Model-B hybrid, feature-level Requests, R2 handoff to Concept. (Sources: SPS template notes, gates, and WBS map.)

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
| SPS | T102 | Governances | `T102-GDR-001 (Operating Model Standard)`, `T102-GDR-002 (Canonical Header Standard)`, `T102-GDR-004 (Decision Records Standard)`, `T102-GDR-005 (ID Governance Standard)`, `T102-GDR-006 (Governance Snapshot Standard)` |

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

| RES ID | Title | Summary | Linked To | Brief | Report |
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
| RES ID | Title | Summary | Linked To | Brief | Report |
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
| RES ID | Title | Summary | Linked To | Brief | Report |
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

