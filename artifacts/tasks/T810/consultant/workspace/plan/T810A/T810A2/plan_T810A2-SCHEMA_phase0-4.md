---
artifact_type: 'PLAN'
initiative_id: 'T810'
epic_id: 'T810A'
feature_id: 'T810A2'
feature_code: 'SCHEMA'
version: '1.0.0'
date: '2025-10-19'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
---

# CONSULTANCY PLAN: T810A2-SCHEMA (Patient Data Structures)

## I. EXECUTIVE SUMMARY

**Feature**: T810A2-SCHEMA (Patient Data Structures)
**Objective**: Develop complete Request document with foundational data architecture specifications for LLM_Gastro clinical tracking assistant
**Deliverables**:
1. Complete Request document (`request_T810A2-SCHEMA.md`) with 9 stories (S01-S09)
2. STABLE JSON patient profile template + schema specifications
3. DYNAMIC JSON tracking entry templates + controlled vocabularies
4. Integration specifications with T810A1-PROMPT feature

**Consultancy Model**: Living Document approach - Request document evolves iteratively through consultation phases as single source of truth

**Timeline**: Multi-session development with 4 coordination checkpoints

---

## II. STAKEHOLDERS & ROLES

| Role | Responsibilities | Availability |
|:-----|:----------------|:-------------|
| **Client** | Coordinator, decision owner, approvals | On-demand during consultation |
| **LLM_Consultant (T810A2)** | Sub-consultant for SCHEMA feature; proposals, requirements analysis, specifications | Primary driver - this role |
| **LLM_Consultant (T810A1)** | Main consultant for PROMPT feature; integration validation | Checkpoint coordination |
| **LLM_Consultant (T810A)** | Epic-level consultant; governance alignment | Governance review |
| **LLM_Researcher** | On-demand research for industry standards, external validation | Ad-hoc invocation |
| **LLM_Developer** | Implementation of JSON templates and integration | Phase 3 onwards |

### Communication Artifact Paths

**Consultant Handoffs** (Epic/Feature coordination):
- **Path**: `prompt/artifacts/tasks/T810/consultant/workspace/communication/consultant/`
- **Exemplar**: `handoff_brief_T810A1-PROMPT_epic-changes.md`
- **Purpose**: T810A2 consultant → T810A consultant communication for Epic governance proposals (e.g., T810A-ADR-002 adoption), integration validation, checkpoint coordination

**Developer Handoffs** (Implementation commissioning):
- **Path**: `prompt/artifacts/tasks/T810/consultant/workspace/communication/developer/`
- **Purpose**: T810A consultant → LLM_Developer communication for post-consultancy implementation handoff (Stable/Dynamic Schema templates, controlled vocabulary files, integration specifications)
- **Workflow**: T810A2 consultant develops deliverables → T810A consultant validates Epic governance compliance → T810A consultant creates developer handoff brief → LLM_Developer implementation (all in Phase 3)

### Document Governance & References

- **Document rules**: `prompt/artifacts/tasks/T810/consultant/workspace/workspace_documentation_rules.md`
- **Completion log (per-activity execution notes)**: `prompt/artifacts/tasks/T810/consultant/workspace/completion/T810A/T810A2/completion_T810A2-SCHEMA.md`
- **Plan/Proposal backups**: `plan_T810A2-SCHEMA_phase0-4.md`, `proposal_T810A2-SCHEMA_phase1.md` (pre-refactor content)

---

## III. CONTEXT & FOUNDATION

### A. Governing Artifacts

**Epic & Feature Documentation:**
- Epic dossier: `prompt/artifacts/tasks/T810/consultant/sps/sps_T810-GASTRO.md`
- Implementation standard & ADR index: `prompt/artifacts/tasks/T810/consultant/concept/concept_T810-GASTRO.md`
- Feature request (T810A2): `prompt/artifacts/tasks/T810/consultant/request/request_T810A2-SCHEMA.md`

**Templates & Governance Rules:**
- Templates & rules: `prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md`
- Concept governance: `prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md` (T102-ADR-004, T102-ADR-005)

**Handoff Brief**
- `prompt\artifacts\tasks\T810\consultant\workspace\communication\handoff_brief_T810A2-SCHEMA.md`

### B. Core Implementation Standards

#### B.1 T102-ADR-004 (Decision Records Index)

**Specification Summary:**

1) **T102-ADR-004-FR-001 (DR Index Schema)**
    `<GDR/ADR> ID | Title | Status | Owner | Effective | Supersedes | Anchor`
       -  `ID`: Pattern T102-GDR-### (initiative GDRs), T102-ADR-### (initiative ADRs), <E-ID>-ADR-### (epic), <F-ID>-ADR-### (feature)
       -  `Title`: Descriptive name using Title Case, 2-8 words maximum for readability
       -  `Status`: {Proposed, Accepted, Deprecated}
       -  `Owner`: Field for governance authority or implementation responsibility (typically "Client") 
       -  `Effective`: ISO-8601 date (YYYY-MM-DD) when decision becomes active
       -  `Supersedes`: List of superseded IDs or — for new decisions
       -  `Anchor:` Lower-kebab format of title, stable across potential file splits

    2) **T102-ADR-004-FR-002 (Decision Records Body)**
       - Placement: Construct directly below the `DR Index Schema` table.
       - Title format: Start the body with a single list item using this exact pattern:
         Examples:
         * **T102-GDR-004 (Decision Records Standard) — {#t102-gdr-004-drs-standard}**
         * **T102-ADR-004 (Decision Records Index) — {#t102-adr-004-drs-index}**
         Rules:
         - ID: literal token at start; Title: Title Case; Anchor: lower-kebab derived from title, prefixed with the ID in lower-kebab form.
         - Keep one space before the anchor block; include braces `{#...}` exactly.
       - Shared subheadings (use bold labels with trailing periods):
         - **Context:** Why this decision is needed; the gap it resolves.
         - **Decision:** What is adopted/changed and who owns it.
         - **Consequences:** Impacts using (+)/(±)/(-) bullets.
         - **References:** Canonical links/anchors to governing rules and related items.
       - ADR additions:
         - **Specification:** Functional requirements (FR-##), constraints, and acceptance notes.
         - **Alternatives Considered:** Rejected options with rationale.
         - **Provenance:** Evidence/design sources supporting the decision.

    3) **T102-ADR-004-FR-003 (Placement Standards)**
       - SPS artifacts: Section titled "<SCOPE> Governance Decisions" containing governance decisions only
       - Concept artifacts: Section titled "<SCOPE> Architectural Decisions" with mirror sections for Epic/Feature areas as needed
       - Consistency requirement: All placement follows established artifact section numbering without local deviations

    4) **T102-ADR-004-FR-004 (Entry Creation Workflow)** Add a new row to the appropriate index table, assign the next sequential ID, and create the matching body section using the required template. 

    5) **T102-ADR-004-FR-005 (Cross-Artifact Linking)**
       - **GDR → Decision (Adoption Statement).** If a GDR formally adopts or mandates an ADR, the adoption MUST be stated in **Decision** using this informal reference pattern (single line):
          + Pattern: "Adopt `<ADR-ID>`, <one-line rationale>..."
          + Example: "Adopt `T102-ADR-004` as the single, Client-owned standard for decision record schemas across artifacts."
       - **ADR → Context (Authority Citation).** If an ADR is governed by a GDR, the governing policy MUST be cited in **Context** using this informal reference pattern as the first sentence of Context:
          + Pattern: "Per `<GDR-ID>`, <one-line rationale>..."
          + Example: "Per `T102-GDR-004`, a unified DR schema is required to prevent drift."

    6) **T102-ADR-004-FR-006 (Anchor Title Stability)**
      - **Anchor & title stability.** Use lower-kebab anchors derived from Title; anchors remain stable across file moves/splits.

    7) **T102-ADR-004-FR-007 (Lifecycle Coherence)**
      When a GDR that is cited by ADRs changes **Status** or is **Superseded**, affected ADRs MUST:
         + update the **Context** authority sentence to the new governing GDR ID/title; and
         + add the prior GDR ID to **Supersedes/References** as appropriate.
         + Perform this update in the next modification to the ADR or in a dedicated “governance sync” change set.

    8) **T102-ADR-004-FR-008 (Status Management)**
      `Proposed → Accepted → Deprecated` lifecycle; document superseded IDs in the **Supersedes** column and, in body text where applicable.

    9) **T102-ADR-004-FR-009 (Precedence Hierarchy)**
      Initiative GDR > Initiative ADR > Epic ADR > Feature ADR > Story ADR for conflict resolution. (See `T102-ADR-003` and `T102-ADR-005` for details.)

    10) **T102-ADR-004-FR-010 (Automation Linting)**
       Authors SHOULD pass the following checks:
        - GDR body contains a **Decision** line matching regex: `` `^Adopt\s+`T[0-9]{3,}(?:[A-Z][0-9A-Z]*)?-ADR-[0-9]{3}`,\s+.+$` ``
        - ADR body **Context** starts with: `` `^Per\s+`T[0-9]{3,}(?:[A-Z][0-9A-Z]*)?-GDR-[0-9]{3}`,\s+.+$` ``

    11) **T102-ADR-004-FR-011 (Consequences Scope)**
        -  **GDR Consequences:** Policy/precedence impacts; compliance expectations; migration & rollout; automation/traceability effects. 
        -  **ADR Consequences:** Quality trade-offs; constraints introduced; operational effects; debt/risks.

    12) **T102-ADR-004-FR-012 (References & Provenance)**
      - **References** in both records include formal reference following `T102-ADR-005-FR-006`
      - **Provenance** store relevant file names only.

    13) **T102-ADR-004-FR-013 (Decision Promotion Workflow)** — Decision records SHOULD follow a staged lifecycle:
      14. **Research (RES)** — Use `RES-ID` to commission and document evidence, options, and empirical findings for a specific scope (Initiative/Epic/Feature).
      15. **Implementation Guidance (IG)** — Encode candidate implementation patterns as `F-IG-RID` at the appropriate scope (typically Feature); `IGs` MAY evolve as research is refined.
      16. **Decision Records (GDR/ADR)** — Promote stable, cross-cutting or long-lived patterns into formal GDR/ADR records when:
         - (a) The pattern affects multiple artifacts or features; or
         - (b) The pattern requires explicit governance (ownership, status, supersedes) beyond implementation detail.
      17. **Traceability** — ADR Specifications SHOULD reference governing `RES-IDs` and `F-IG-RIDs`  in **Provenance** and **References**, rather than duplicating detailed patterns.
      18. **Scope Guidance** — Epic-level ADRs SHOULD be used for cross-feature decisions (e.g., shared vocabularies, common JSON architectures). Feature-level ADRs SHOULD be reserved for significant, feature-local architectural decisions that cannot be reasonably governed at Epic scope. Routine implementation details MAY remain in IG F-RIDs without a dedicated ADR.

#### B.2 T102-ADR-005 (ID Specification & Rules)

**Specification Summary:**

1) **T102-ADR-005-FR-001 (ID Scope)**
      - I-ID (initiative): `^T\d{3}$` (e.g., `T102`).
      - E-ID (epic): `^T\d{3}[A-Z]$` (e.g., `T102A`).
      - F-ID (feature): `^T\d{3}[A-Z]{3}$` (e.g., `T102A1`).
      - S-ID (story): `^T\d{3}[A-Z]{3}+-S\d+$` (e.g., `T102A1-S3`).

    2) **T102-ADR-005-FR-002 (ID Terminologies)**
      - Scope IDs: `I-ID`/`E-ID`/`F-ID`/`S-ID` are artifact identifiers (initiative/epic/feature/story), e.g., `I-ID = T102`, `F-ID = T102A1`.
      - Rule IDs: `I-RID`/`E-RID`/`F-RID`/`S-RID` are consideration/rule identifiers defined by category tokens at each scope (e.g., `T102-QG-02`, `T102A-NFR-002`).
      - Decision Record IDs: `I-GDR`/`E-GDR`/`F-GDR`/`S-GDR` denotes governance decisions; `I-ADR`/`E-ADR`/`F-ADR`/`S-ADR` denotes architecture decision at each scope. 
      - Usage guidance: Use `<SCOPE>-ID` when referring to artifact scope; use `<RULE>-ID` when referring to rule items; use `<SCOPE>-ADR/GDR` for decision records.

    3) **T102-ADR-005-FR-003 (Precedence & Directionality)**
      - Precedence: I-RIDs > I-GDRs > I-ADRs > E-RIDs > E-GDRs > E-ADRs > F-RIDs > F-GDRs > F-ADRs > S-RIDs > S-GDRs > S-ADRs.
      - Directionality: Upstream never references downstream. Lower/equal scopes MAY reference higher/equal scopes; higher MUST NOT reference lower. Variances MUST cite the overridden upstream item.
      - For the scoped exception related to Feature-level INT items, see `T102-ADR-005-FR-008 (INT Integration Exception)`.

    4) **T102-ADR-005-FR-004 (ID Categories)**
      - Token map and definitions:
        - DR Category:
          - `GDR` — Governance: Policy-level governance decision record.
          - `ADR` — Architecture: Architecture/implementation decision record.
        - Main Category:
          - `ASSUM` — Assumption: Items believed true but not yet verified; inform approach and risk.
          - `CON` — Constraint: Non‑negotiable boundary or limitation that must be respected.
          - `QG` — Quality Goal: Measurable outcome that defines success (verifiable, stable).
          - `DEP` — Dependency: External condition, interface, asset, or approval required.
          - `NOTE` — Note: Informational remark to aid context or authoring; non‑normative.
          - `RES` — Research: Formally commissioned research with approved brief and validated report artifacts; traceable via Research Artifacts Index per `T102-ADR-006`.
          - `ISSUE` — Open Issue: Known gap requiring decision or action; tracked to resolution.
          - `RISK` — Risk: Potential negative event with likelihood/impact; track mitigation/acceptance.
        - Sub Category
          - `FR` — Functional Requirement: Behavior the system must provide; testable acceptance.
          - `NFR` — Non‑Functional Requirement: Quality attribute (performance, security, etc.); testable.
          - `IF` — Interface: Data or integration interface definitions and contracts.
          - `IG` — Implementation Guidance: Normative authoring/process guidance (internal); not a design choice.
          - `INT` — Integration: Cross‑features/process integration guidance (external)
      - Allowed tokens by scope
        - Initiative/Epic (I‑ID/E‑ID): `ASSUM`, `CON`, `QG`, `DEP`, `IG`, `NOTE`, `RES`, `ISSUE`, `RISK`.
        - Feature (F‑ID): additive from Epic: `FR`, `NFR`, `IF`, `INT`, `CON`, `RES`.
        - Story (S‑ID): inherits Feature tokens.
      - Universal construction: `{SCOPE_ID}-{CATEGORY}-{NNN}` for all Rule IDs and Decision Record IDs.
      - ADR sub-IDs within a decision: append `-FR-{NNN}` (e.g., `T102-ADR-003-FR-001`).

    5) **T102-ADR-005-FR-005 (ID Title & Construction)**
      - General format: `* **<ID> (<Title>)** — <concise description>` 
      - Title: max 2-3 words 
      - Scope: Applies to I‑ID/E‑ID/F‑ID/S‑ID items when introduced; for ADRs/GDRs use the body title pattern in `T102-ADR-004`.
      - Examples:
        - **T102-QG-001 (Client Readability)** — Artifacts are understandable by non‑technical stakeholders (aim ≥ "clear" on internal rubric).
        - **T102A-DEP-001 (Planner Integration)** — Planner consumes Concept + referenced Design Logs; align handoff schema.
        - **T102A1-NFR-002 (Author Usability)** — Section names/order intuitive for non‑technical authors.
        - **T102A1-S3-FR-001 (Epic Dossier Schema)** — Epic block includes YAML header, standardized subsections, and Feature Register.
      - Relation to DRs: For the ADR/GDR body section heading, follow `T102-ADR-004-FR-002 (Decision Records Body)` for the exact list‑item title and anchor format.

    6) **T102-ADR-005-FR-006 (ID References)**
      - Formal (References subsections; Inherited Considerations tables): back‑ticked `ID (Title)` tokens, e.g., `T102-CON-001 (Format Requirements)`.
      - Informal (inline prose): flexible between formal reference and bare back‑ticked ID tokens, e.g., `T102-CON-001`.

    7)  **T102-ADR-005-FR-007 (Migration & Stability)**
      - Keep anchors stable when moving content; deprecate IDs via index when replaced. If titles change, anchors remain unchanged.

    8)  **T102-ADR-005-FR-008 (Integration Notes Exception)** — At Feature scope, `INT` (Integration) F-RIDs have a specialized role:
      - **Bottom-Up Influence**: Feature-level INT items operate primarily as bottom-up integration proposals feeding higher-scope governance (Epic GDRs/ADRs/IGs). They are not direct implementation specifications for Story behavior.
      - **Cross-Feature References Permitted**: INT F-RIDs MAY reference other Feature F-RIDs directly (e.g., `T810A1-NFR-009`, `T810A3-*`) when used as integration design notes for Epic coordination. This is a scoped exception to the general upstream-only directionality rule in `T102-ADR-005-FR-003`.
      - **Suggestive, Not Prescriptive**: INT items SHOULD describe ideal integration patterns (e.g., data flow, sequencing, dependency patterns) and SHOULD avoid embedding Story-level acceptance criteria or strict SHALL requirements. Prescriptive behavior MUST be expressed in higher-scope GDR/ADRs or in Feature-level `CON`/`IG` F-RIDs.
      - **Governance Loop**: Epic consultants SHOULD review INT items when evolving Epic-level E-RIDs/E-ADRs/E-GDRs and, once decisions are adopted, affected INT items SHOULD be updated to reference the new governance rather than acting as standalone sources of truth.

### C. Application to T810A2-SCHEMA

**F-ID Pattern**: `T810A2-SCHEMA` → F-RID construction: `T810A2-{CATEGORY}-{NNN}`

**Allowed F-RID Categories for T810A2:**
- `ASSUM`, `CON`, `QG`, `DEP`, `IG`, `NOTE`, `RES`, `ISSUE`, `RISK` (inherited from Epic)
- `FR`, `NFR`, `IF`, `INT`, `CON`, `RES` (feature-specific)

**F-RID Examples for T810A2:**
- `T810A2-NFR-001 (Token Efficiency)` — Stable Schema profile must be <200 tokens
- `T810A2-IF-001 (Stable Schema Loading Interface)` — Define session initialization loading pattern
- `T810A2-INT-001 (Probe Triggering Integration)` — Specify mandatory/optional field mapping for T810A1 integration
- `T810A2-CON-001 (Schema Complexity Constraint)` — Structured objects with metadata, balanced for maintainability
- `T810A2-DEP-001 (T810A1 Integration Dependency)` — Alignment with T810A1-IF-006, INT-004, NFR-009 required

**F-GDR/F-ADR Pattern** (if needed in future):
- `T810A2-GDR-001` (feature-level governance decision)
- `T810A2-ADR-001` (feature-level architectural decision)

### D. Feature Identity

**From Handoff Brief v1.0.0:**
- **Feature ID**: T810A2-SCHEMA
- **Feature Name**: Patient Data Structures
- **Parent Epic**: T810A-SYSTEM
- **Primary Purpose**: Define and specify all patient data structures, schemas, and vocabularies for LLM_Gastro system
- **Dependencies**: None (foundational feature)
- **Depended Upon By**: T810A1-PROMPT (primary), T810A3-REPORT (secondary)

### E. Core Architecture (from T810A-GDR-003)

**Stable/Dynamic Schema Split**:
- **Stable Schema (Patient Profile)**: Read-only, manually updated constant/stable data (demographics, conditions, medications, triggers, relievers)
- **Dynamic Schema (Tracking Entries)**: LLM-generated single entry per interaction (patient_state, meal, stool, sleep, etc.)

### F. Critical Design Decisions (from Handoff Brief v1.0.0)

1. **Template Annotation Approach**: HYBRID (Option C)
   - Minimal inline hints for complex/critical fields only
   - Clean structure for straightforward fields
   - Balance clarity and cleanliness

2. **Schema Complexity**: Structured objects with metadata, balanced for maintainability
   - NOT overcomplicated
   - Token efficiency prioritized

3. **Standards Source**: Cara Care application patterns as primary exemplar
   - Defer external/advanced standards for MVP

### H. Success Criteria

**T810A2-SCHEMA Request Development Complete When:**
- [ ] Complete Request document with 9 stories (S01-S09) fully specified
- [ ] All story functional requirements have Gherkin acceptance criteria
- [ ] Stable Schema schema fully documented with field types, constraints, categorization
- [ ] All 5 Dynamic Schema entry types (patient_state, meal, stool, sleep, flexible) fully documented
- [ ] **EXHAUSTIVE controlled vocabularies** provided for ALL categorical fields
- [ ] Integration patterns (Probe triggering, aggregation, initialization, conflict resolution) fully specified
- [ ] Validation and quality requirements documented
- [ ] No blocking dependencies on T810A1-PROMPT for Request completion
- [ ] Client approval obtained for T810A2-SCHEMA Request document

---

## IV. PHASE BREAKDOWN

### **PHASE 0: FOUNDATION & FRAMING**

**Duration**: 1-2 hours
**Objective**: Establish high-level problem framing and feature solution framework BEFORE establishing any F-RIDs

#### Activities

**Activity 0.1: High-Level Problem Framing**
- Propose content for Section III.A (Feature Solution Framework) following T810A1 structural pattern
- Define decision criteria & weights for schema design evaluation
- Document problem recap & constraints

**Activity 0.2: Source & Scope**
- Propose content for Section III.B (Source & Scope)
- Define in-scope vs out-of-scope boundaries
- Establish repository paths and deliverable targets

**Activity 0.3: Business Objectives & Success Signals**
- Propose content for Section III.C (Business Objectives & Success Signals)
- Define primary objectives for T810A2 feature
- Establish qualitative success signals for MVP

**Activity 0.4: Stakeholder Identification**
- Update Section III.D (Stakeholders) with T810A2-specific roles
- Define responsibility matrix (decision owner, primary users, consumers)

#### Deliverables

- [ ] Section III.A-III.D drafted and proposed in Request document
- [ ] Client review and approval of high-level framing

#### Gate 0: Foundation Approval

**Criteria**: Client confirms high-level problem framing, scope boundaries, and success signals are accurate

**Blocking Issues**: None identified

---

### **PHASE 1: FOUNDATIONAL REQUIREMENTS (F-RIDs)**

**Duration**: 3-5 hours (extended for consultation engagement)
**Objective**: Collaboratively establish and validate foundational requirements (F-RIDs) for Section III.E - III.M before detailed Story specifications.
**Status**: ✅ COMPLETE — Foundational F-RIDs agreed (ASSUM, DEP, NFR, IF, CON, IG, INT); IC table working draft; research dependency RES-001 registered.

**Key outcomes**:
- Template format: YAML with HYBRID minimal comments; null-before-probe enforced; 100% schema-defined keys (CON-005); Cara Care vocabulary authority proposed (Epic ADR).
- Quality/scope: Vocabulary completeness required for all categorical fields; qualitative NFR validation accepted for MVP; manual workflows acceptable for MVP.
- Integration posture: INT items defined for probe triggering, aggregation, session initialization, conflict handling, and forward compatibility.

**Primary risks/dependencies**:
- Controlled vocabulary completeness and validation drift risks; RES-001 research critical.
- Epic coordination needed for vocabulary authority and validation drift (Phase 3.4).

**Pointers**:
- Per-activity completion notes: `completion_T810A2-SCHEMA.md` (Phase 1).
- Normative F-RID bodies: `proposal_T810A2-SCHEMA_phase1.md` (Sections II–XII) and `request_T810A2-SCHEMA.md`.
- Legacy detail (pre-refactor): `plan_T810A2-SCHEMA_phase0-4.md`.

#### Activities (scope)
- **Activity 1.0**: Epic governance context review; IC table working draft.
- **Activity 1.1**: IC table rule-set and architecture category (E-ADRs) established.
- **Activity 1.2**: ASSUM deltas finalized (7 items).
- **Activity 1.3**: DEP deltas finalized (5 items); Epic integration model set.
- **Activity 1.4**: NFRs finalized (5 items) with qualitative validation posture.
- **Activity 1.5**: IF contracts finalized (4 items); interface responsibility matrix.
- **Activity 1.6**: CON finalized (5 items); validation drift escalated to Epic.
- **Activity 1.7**: IG finalized (7 items); YAML template format & annotation density set.
- **Activity 1.8**: INT finalized (5 items); integration protocol defined.
- **Activity 1.9**: Research & Notes captured; RES-001 marked CRITICAL.
- **Activity 1.10**: Checkpoint 1 Preparation — Holistic F-RID validation (T102-ADR-005 compliance, Epic governance alignment, issue resolution); IC table finalization; handoff brief to T810A Epic consultant; approval package assembly.

#### Deliverables
- F-RID set across ASSUM/DEP/NFR/IF/CON/IG/INT/NOTE/RES (40 items total).
- Working draft IC table (to be finalized at Checkpoint 1).
- Traceability matrices and clarifying questions (see Proposal).

#### Checkpoint 1: F-RID Review & Approval

**Target**: 5-7 hours from Phase 1 kickoff (extended for consultation engagement)  
**Participants**: Client, LLM_Consultant (T810A2), LLM_Consultant (T810A - Epic), LLM_Developer

**Review Criteria (condensed)**:
- F-RID categories complete; IC table includes Architecture (E-ADRs).
- No direct feature-to-feature citations; Epic governance references only.
- ID construction per T102-ADR-005; clear E-RID/E-ADR → F-RID expansion logic.
- Research & Notes documented; feasibility confirmed by Epic consultant + Developer.

**Communication Brief Deliverables (if needed)**:
- Brief to LLM_Developer (implementation requirements, schema specs, integration patterns).
- Brief to LLM_Researcher (scope/questions for RES-001).

**Approval Gate**: Client/Epic consultant approve foundational F-RIDs and research scope; authorize transition to Phase 2.  
**Blocking Issues**: _____________________________________________________________

---

### **PHASE 2: SCHEMA DEVELOPMENT & VALIDATION**

**Duration**: 4-6 hours
**Objective**: Develop complete Story specifications (S01-S09) for Section III.J with exhaustive schemas and controlled vocabularies

**Phase 2 Proposal Artifact** (to be created):
- `prompt/artifacts/tasks/T810/consultant/workspace/proposal/T810A/T810A2/proposal_T810A2-SCHEMA_phase2.md` — Phase 2 normative specification (Stories & examples); Activity 2.0 forms the foundation section.

---

#### Activity 2.0: Template Drafting & Deliverable Examples

**Purpose**: Draft structurally clean, minimal example artifacts for all Phase 2 deliverables BEFORE specific Story development to give the Client a concrete starting point for Story-level design (not final specifications).

**STATUS**: **PENDING** — Prerequisites: PHASE 1 complete (✅)

**CRITICAL REQUIREMENT**: Per client directive (Activity 1.7 COMMENT 2), this activity SHALL be completed at start of Phase 2 BEFORE any Story specification design. Template drafts provide concrete reference examples that inform Story-level FR specifications.

**NOTE**: Activity 2.0 outputs are intentionally non-exhaustive, "representative-but-serious" drafts. Stories S01–S08 will refine and complete the specifications using these examples as a foundation.

**Template Drafting Scope**:

**1. YAML Template Examples** (per `T810A2-IG-002`):
- **Stable Schema Template**: Draft example YAML template with:
  - Top-level comment block (purpose: patient profile schema, type: Stable Schema, usage: read-only LLM access)
  - Field definitions with minimal annotation (70-80% no comments, 20-30% short directive comments on complex fields, applied as guidelines rather than strict quotas)
  - Constant fields: `age`, `sex` with value sets
  - Stable fields: `conditions`, `medications`, `triggers`, `relievers`, `allergies`, `notes` with controlled vocabularies
  - Native `#` comments demonstrating HYBRID annotation approach
  - Token budget: target ≤ 1,000 tokens per `T810A2-NFR-001`

- **Dynamic Schema Templates** (7 entry types): Draft example YAML templates for:
  - **REQUIRED** (MVP Core): `meal`, `stool`, `digestion`, `mental` — Lean draft templates with representative field specifications (non-exhaustive) to illustrate structure and key fields
  - **OPTIONAL** (MVP Extended): `sleep`, `medication`, `hydration` — Template structure only (Stories deferred per Activity 1.9 QA ANSWER 1)

**5. Coordination Brief & Combined SCHEMA Block (T810A1 Integration)**:
- Draft a combined Dynamic SCHEMA block (YAML) covering all REQUIRED entry types for use as a single LLM-facing template in T810A1 system prompt / Project Knowledge (MVP).
- Prepare a consultant-to-consultant handoff brief to T810A1-PROMPT subconsultant summarizing:
  - Stable SCHEMA MVP structure and file location.
  - Dynamic SCHEMA MVP structures and combined SCHEMA block intent.
  - Integration touchpoints with `T810A1-IF-006`, `T810A1-INT-004`, and `T810A1-INT-005`.
  - Known deltas between earlier "flexible schema" assumptions in T810A1 and `T810A2-CON-005` (fixed keys, governance-driven evolution).

**2. Controlled Vocabulary Catalog Examples** (per `T810A2-IG-003`):
- **Markdown Table Format**: Draft examples demonstrating:
  - Bristol Stool Chart scale (0-7) with semantic labels per `T810A-ADR-002-FR-001` enhancements
  - Symptom severity scales (1-5) with endpoint descriptions (pain, bloating, stress, mood)
  - Meal/stool metadata enumerated arrays per `T810A2-RES-001` Deliverable A (representative but not yet exhaustive)
  - Hybrid placement examples (embedded short lists vs external catalog references)

**3. Manual Workflow Documentation Examples** (per `T810A2-IG-004`):
- **Patient Instruction Templates**: Draft step-by-step guides for:
  - Dynamic Schema manual compilation (copy codeblocks → chronological array → save file)
  - File naming conventions (session organization pattern)
  - Project Knowledge upload procedure
  - JSON export format examples (NOT YAML)

**4. Field Classification Examples** (per `T810A2-IG-005`):
- **Mandatory/Optional Mapping Tables**: Draft categorization for REQUIRED entry types:
  - `meal`: mandatory (timestamp, items/ingredients), optional (metadata, pre_meal_prokinetics, notes)
  - `stool`: mandatory (timestamp, type Bristol 0-7), optional (metadata, confidence, notes)
  - `digestion`: mandatory (timestamp, tummy_pain 1-5, bloating 1-5), optional (notes)
  - `mental`: mandatory (timestamp, mood -2 to 2, stress 1-5), optional (notes)

**Deliverables** (stored in `prompt/roles/gastro/data/`):
- [ ] `template_stable_patient_schema.yaml` — Stable Schema draft template
- [ ] `template_dynamic_meal_example.yaml` — Meal entry draft template
- [ ] `template_dynamic_stool_example.yaml` — Stool entry draft template
- [ ] `template_dynamic_digestion_example.yaml` — Digestion entry draft template
- [ ] `template_dynamic_mental_example.yaml` — Mental entry draft template
- [ ] `template_dynamic_sleep_structure.yaml` — Sleep template structure (OPTIONAL type)
- [ ] `template_dynamic_medication_structure.yaml` — Medication template structure (OPTIONAL type)
- [ ] `template_dynamic_hydration_structure.yaml` — Hydration template structure (OPTIONAL type)
- [ ] `vocabulary_catalog_example.md` — Controlled vocabulary markdown examples
- [ ] `workflow_patient_instructions_example.md` — Manual workflow documentation
- [ ] `field_classification_mapping.md` — Mandatory/optional field tables for REQUIRED types
- [ ] `template_dynamic_tracking_schema.yaml` — Combined Dynamic SCHEMA block (REQUIRED entry types) for LLM-facing template
- [ ] `aggregation_mixed_array_example.json` — Aggregation pattern A (single mixed chronological array)
- [ ] `aggregation_per_type_arrays_example.json` — Aggregation pattern B (separate arrays per entry type)
- [ ] `aggregation_hybrid_index_example.json` — Aggregation pattern C (hybrid: entries array + per-type index)
- [ ] `handoff_brief_T810A2-SCHEMA_to_T810A1-PROMPT_phase2.md` — Coordination brief to T810A1 consultant (MVP SCHEMAs, aggregation options, integration guidance)

**Quality Criteria**:
- Templates SHOULD align with `T810A2-IG-002` format specification (YAML internal, JSON output, minimal annotation, token budget awareness) while prioritizing structurally clean, minimal examples.
- Vocabularies SHOULD follow `T810A2-IG-003` documentation standard (markdown tables, semantic anchors, hybrid placement) with representative-but-serious value sets.
- All examples SHOULD generally align with `T810A2-RES-001` recommendations (R1-R6) and Epic ADR-002-FR-001 enhancements, allowing deviations where needed for clarity at draft stage.
- Drafts provide sufficient visual/conceptual clarity to support Story-level FR development, but are not expected to be complete or exhaustive.

**Validation**:
- T810A2 consultant reviews drafts for Epic governance compliance
- Client reviews the draft artifacts and confirms they are a suitable starting point for detailed Story development before proceeding
- Drafts serve as a "design proposal by example" baseline for Activities 2.1-2.8 (to be refined and extended in each Story)
- Upon completion of Activity 2.0 and client review, add a structured Activity 2.0 entry to `completion_T810A2-SCHEMA.md` per workspace documentation rules
- Coordination handoff brief to T810A1-PROMPT consultant completed and aligned (no blocking integration issues for `T810A1-S05` before closing Activity 2.0)

**Coordination**:
- Activity 2.0 outputs provide the starting examples for Story S01-S08 FR specifications
- T810A consultant validates Epic governance alignment (T810A-ADR-002, T810A-GDR-002, T810A-IG-002/004/005/006)
- Template drafts enable concrete Story acceptance criteria to be written in Phase 2 while keeping Story-level specifications as the authoritative source

---

#### Activity 2.1: Story S01 — Stable Schema (Patient Profile) Schema

**Functional Requirements** (T810A2-S01-FR-###):
- FR-001: Constant field specifications (age, sex with data types, constraints, value sets)
- FR-002: Stable field specifications (conditions, medications, triggers, relievers, allergies, notes)
- FR-003: Schema structure and data types (structured objects with metadata per client directive)
- FR-004: Token efficiency optimization (<200 tokens per profile)
- FR-005: Manual update workflow specification
- FR-006: Read-only access patterns for LLM consumption

**Acceptance Criteria**: Gherkin format (Given/When/Then) for ALL FRs

**Deliverables**:
- Complete Stable Schema schema with field definitions
- Controlled vocabularies for categorical fields (conditions, medications)
- Example Stable Schema template structure

#### Activity 2.2: Story S02 — Dynamic Schema Schema (patient_state)

**Functional Requirements** (T810A2-S02-FR-###):
- FR-001: Mental state fields (`mood` -2 to 2 scale with semantic labels, `stress` 1-5 scale with descriptions)
- FR-002: Digestion fields (`tummy_pain` 1-5 scale with descriptions, `bloating` 1-5 scale with descriptions)
- FR-003: Pain fields (headache, other_pain with controlled vocabularies)
- FR-004: Timestamp and metadata fields
- FR-005: Mandatory vs. optional field specifications
- FR-006: Probe triggering rules (which missing keys trigger clarifying questions)

**Acceptance Criteria**: Gherkin format for ALL FRs

**Deliverables**:
- Complete patient_state entry schema
- Exhaustive controlled vocabularies with semantic mappings:
  - mood: -2 → "awful", -1 → "low/frustrated", 0 → "so-so/neutral", 1 → "good/light", 2 → "very good/happy"
  - stress: 1 → "no stress", 2 → "low/relaxed", 3 → "moderate", 4 → "high/stressed", 5 → "extreme stress"
  - tummy_pain: 1 → "no pain", 2 → "mild discomfort", 3 → "moderate pain", 4 → "significant pain", 5 → "extreme pain"
  - bloating: 1 → "no bloating", 2 → "minimal", 3 → "moderate", 4 → "severe", 5 → "extreme bloating"

#### Activity 2.3: Story S03 — Dynamic Schema Schema (meal)

**Functional Requirements** (T810A2-S03-FR-###):
- FR-001: Core fields (time, items, fluids)
- FR-002: **Ingredients field** (array of ingredient strings - MANDATORY from Cara Care)
- FR-003: **Metadata field** (array: ["chili", "oily", "sweet", "light", ...] - MANDATORY from Cara Care)
- FR-004: Optional fields (pre_meal_prokinetics, notes, trigger_context)
- FR-005: Timestamp format specification
- FR-006: Mandatory vs. optional field specifications

**Acceptance Criteria**: Gherkin format for ALL FRs

**Deliverables**:
- Complete meal entry schema
- Exhaustive metadata vocabulary (culinary descriptors)
- Example meal entry template

#### Activity 2.4: Story S04 — Dynamic Schema Schema (stool)

**Functional Requirements** (T810A2-S04-FR-###):
- FR-001: **Type field** (1-7 integer with Bristol scale descriptions - MANDATORY from Cara Care)
- FR-002: **Metadata field** (array: ["urgent", "full_evacuation", "partial_evacuation", "mucus", "undigested_food", ...] - MANDATORY from Cara Care)
- FR-003: **Confidence field** (0.0-1.0 float for LLM image analysis - MANDATORY from Cara Care)
- FR-004: Additional fields (features, passage, completeness, wipe, trigger_context, notes)
- FR-005: Bristol scale semantic mapping (Type 1 → description, ..., Type 7 → description)
- FR-006: Mandatory vs. optional field specifications

**Acceptance Criteria**: Gherkin format for ALL FRs

**Deliverables**:
- Complete stool entry schema
- Exhaustive Bristol scale definitions (Types 1-7 with clinical descriptions)
- Exhaustive metadata vocabulary (passage descriptors, completeness indicators)
- Confidence interpretation guidelines

#### Activity 2.5: Story S05 — Dynamic Schema Schema (sleep)

**Functional Requirements** (T810A2-S05-FR-###):
- FR-001: Core fields (time, duration_hours)
- FR-002: Optional fields (quality, interruptions, notes)
- FR-003: Timestamp format specification
- FR-004: Mandatory vs. optional field specifications

**Acceptance Criteria**: Gherkin format for ALL FRs

**Deliverables**:
- Complete sleep entry schema
- Example sleep entry template

#### Activity 2.6: Story S06 — Schema Evolution Governance

**Purpose**: Define governance workflow for schema evolution (new entry types, controlled vocabulary VALUE expansion) per NOTE-004

**Functional Requirements** (T810A2-S06-FR-###):
- FR-001: Pre-specified flexible entry types (exercise, stress_event, medication_taken, supplements) with complete schemas
- FR-002: Controlled vocabulary VALUE expansion rules (NOT key structure modification per CON-005 and NOTE-004) — governance-driven schema updates, not runtime LLM inference
- FR-003: Schema evolution governance patterns (when to add new entry types via T810A2 feature updates)
- FR-004: Validation rules for new entry type specifications

**CRITICAL** (per NOTE-004): "Flexible schema" refers to controlled vocabulary VALUE expansion within existing key structures, NOT runtime key addition. CON-005 prohibits runtime flexible keys for MVP. New KEYS added only via T810A2 governance-driven schema updates (Story S06 workflow).

**Acceptance Criteria**: Gherkin format for ALL FRs

**Deliverables**:
- Complete entry type schemas (exercise, stress_event, medication_taken, supplements)
- Schema evolution governance workflow documentation
- Controlled vocabulary expansion guidelines (VALUE flexibility within schema-defined keys)

#### Activity 2.7: Story S07 — Controlled Vocabularies Register

**Functional Requirements** (T810A2-S07-FR-###):
- FR-001: Complete enumeration of ALL categorical fields across ALL entry types
- FR-002: Value set definitions with semantic mappings
- FR-003: Scale definitions (numeric → descriptive label mappings)
- FR-004: Vocabulary extensibility rules
- FR-005: LLM_Gastro vocabulary enforcement approach (prompt-engineering based per T810A1-CON-008)

**Acceptance Criteria**: Gherkin format for ALL FRs

**Deliverables**:
- Comprehensive controlled vocabulary register
- Semantic mapping tables for all scales
- Vocabulary governance rules

#### Activity 2.8: Story S08 — Integration Patterns

**Functional Requirements** (T810A2-S08-FR-###):
- FR-001: Probe triggering rules (mandatory/optional field mapping per entry type)
- FR-002: End-of-day aggregation format (collection of Dynamic Schema entries)
- FR-003: Session initialization pattern (Stable Schema + Dynamic Schema skeleton loading)
- FR-004: Conflict resolution examples (Stable Schema > ChatGPT Memory)
- FR-005: Field-to-question-type mapping for Probe phase (per T810A1 v1.1.0 update)

**Acceptance Criteria**: Gherkin format for ALL FRs

**Deliverables**:
- Mandatory/optional field mapping table per entry type
- Aggregation format specification
- Initialization sequence specification
- Conflict resolution examples
- Exemplar Probe questions for mandatory fields

#### Activity 2.9: Story S09 — Validation & Quality Requirements

**Functional Requirements** (T810A2-S09-FR-###):
- FR-001: Prompt-engineering validation rules (no programmatic validation per T810A1-CON-008)
- FR-002: Value set enforcement approach (S05 Execution Protocol + S08 Exemplars)
- FR-003: Error handling patterns for missing/invalid data
- FR-004: Data quality criteria for clinical utility
- FR-005: Schema validation specifications

**Acceptance Criteria**: Gherkin format for ALL FRs

**Deliverables**:
- Validation rule specifications
- Enforcement approach documentation
- Quality criteria definitions

#### Deliverables (Phase 2 Complete)

- [ ] Section III.J (Stories & Specification) completed with 9 stories (S01-S09)
- [ ] All stories have 3-7 functional requirements with F-ID pattern: T810A2-S##-FR-###
- [ ] All FRs have Gherkin acceptance criteria (Given/When/Then)
- [ ] Exhaustive controlled vocabularies for ALL categorical fields
- [ ] Semantic mapping tables for all numeric scales
- [ ] Integration pattern specifications aligned with T810A1

#### Checkpoint 2: Complete Schema Review

**Target**: 8-10 hours from kickoff
**Participants**: Client, LLM_Consultant (T810A2), LLM_Consultant (T810A1)

**Review Criteria**:
- All 9 stories complete with FRs and Gherkin ACs
- Controlled vocabularies exhaustive and aligned with Cara Care exemplar
- Integration patterns consistent with T810A1-PROMPT
- No missing mandatory fields or vocabularies
- Schema complexity balanced (structured but not overcomplicated)

**Approval Gate**: Client approves complete schema specifications; proceed to Phase 3

---

### **PHASE 3: IMPLEMENTATION OUTPUT & INTEGRATION**

**Duration**: 2-3 hours
**Objective**: Create actual JSON templates, finalize Request document, and validate integration with T810A1

**This phase expands beyond the original "PHASE 2: REQUEST DOCUMENT FINALIZATION" to include implementation artifacts**

#### Activity 3.1: Request Document Finalization

**Activity 3.1.1: Acceptance Criteria Register (Section III.K)**
- Compile summary table of all acceptance criteria from Stories S01-S09
- Format: `| ID | Title | AC Summary |`

**Activity 3.1.2: Open Issues & Risks (Section III.L)**
- Migrate risks from consultancy plan to Request document
- Log identified risks:
  - Template annotation decision validation
  - Controlled vocabulary completeness gaps
  - Schema complexity balance
  - Mandatory/optional field mapping edge cases
  - Timeline pressure risks

**Activity 3.1.3: YAML Header & Metadata**
- Complete frontmatter per T102-ADR-002
- Ensure all required keys present and valid

**Activity 3.1.4: Validation Checklist (Section VI)**
- Complete validation checklist items
- Verify traceability, completeness, consistency

#### Activity 3.2: Implementation Artifacts

**Activity 3.2.1: STABLE JSON Template Creation**
- **Path**: `prompt/roles/gastro/data/patient_profile_stable.json`
- **Content**: Template structure with:
  - Constant fields (age, sex)
  - Stable fields (conditions, medications, triggers, relievers, allergies, notes)
  - Structured objects with metadata per client directive
  - Inline annotations following HYBRID approach (minimal hints for complex fields)
  - Example values demonstrating correct format

**Activity 3.2.2: DYNAMIC JSON Template Creation**
- **Path**: `prompt/roles/gastro/data/tracking_templates/`
- **Templates**:
  - `template_patient_state.json` (mental, digestion, pain fields)
  - `template_meal.json` (ingredients, metadata, items, fluids)
  - `template_stool.json` (type, metadata, confidence, features)
  - `template_sleep.json` (time, duration_hours, notes)
  - `template_exercise.json` (flexible type)
  - `template_stress_event.json` (flexible type)
  - `template_medication_taken.json` (flexible type)
  - `template_supplements.json` (flexible type)
- **Content**: Each template includes:
  - Skeleton structure with all mandatory fields
  - Inline hints for complex fields (HYBRID approach)
  - Controlled vocabulary examples
  - Semantic scale mappings in comments

**Activity 3.2.3: Controlled Vocabulary Documentation**
- **Path**: `prompt/roles/gastro/data/controlled_vocabularies.md`
- **Content**: Master registry of ALL controlled vocabularies and semantic scale mappings
- **Format**: Markdown tables for easy LLM_Gastro consumption

#### Activity 3.3: T810A1 Integration Validation

**Activity 3.3.1: Integration Point Validation**
- Validate alignment with T810A1-IF-006 (Dynamic Schema Generation)
- Validate alignment with T810A1-INT-004 (Patient Data Architecture)
- Validate alignment with T810A1-INT-005 (Memory Review Protocol)
- Validate alignment with T810A1-NFR-009 (Probe Phase Enforcement)

**Activity 3.3.2: Integration Documentation**
- Document integration patterns in T810A1 Request (cross-reference to T810A2)
- Update T810A1 S05 (Execution Protocol) references to T810A2 templates
- Update T810A1 S04 (Knowledge Base) references to T810A2 data files

#### Activity 3.4: Epic Coordination — Validation Drift Risk

**Purpose**: Coordinate with T810A Epic consultant on cross-feature validation drift risk escalated from CON-003

**Context**: Per Activity 1.6 CON-003 analysis, validation drift risk (originally T810A1-ISSUE-004) has cross-feature impact affecting T810A1, T810A2, and T810A3. Risk requires Epic-level governance coordination rather than Feature-level Issue tracking.

**Coordination Tasks**:
- [ ] Document validation drift risk with Epic T810A consultant: (1) Risk description (value drift in Dynamic Schema due to no programmatic validation), (2) Cross-feature impact analysis (T810A1 enforcement, T810A2 specifications, T810A3 aggregation quality), (3) Mitigation approach (exhaustive T810A2 specifications + T810A1 prompt engineering)
- [ ] Determine Epic-level risk categorization: T810A-RISK-### vs. T810A-ISSUE-###
- [ ] Establish Epic governance response: (1) Accept risk for MVP per T810A-CON-004 platform constraint, (2) Document post-MVP validation enhancement path, (3) Define monitoring criteria for drift detection in empirical testing

**Deliverable**:
- [ ] Epic-level risk documented in T810A Epic governance (SPS or Concept)
- [ ] CON-003 traceability validated (references Epic-level risk tracking)

#### Deliverables (Phase 3 Complete)

- [ ] Request document finalized (all sections complete)
- [ ] STABLE JSON template created at `prompt/roles/gastro/data/patient_profile_stable.json`
- [ ] DYNAMIC JSON templates created at `prompt/roles/gastro/data/tracking_templates/*.json`
- [ ] Controlled vocabulary documentation created at `prompt/roles/gastro/data/controlled_vocabularies.md`
- [ ] Integration validation complete with T810A1-PROMPT
- [ ] No blocking integration issues identified

#### Checkpoint 3: Final Approval Gate

**Target**: 12-14 hours from kickoff
**Participants**: Client, LLM_Consultant (T810A2), LLM_Consultant (T810A1), LLM_Developer

**Review Criteria**:
- Request document complete and validated per Section VI checklist
- Implementation artifacts created and aligned with specifications
- Integration with T810A1 validated (no conflicts, no gaps)
- All controlled vocabularies exhaustive and correct
- Client satisfaction with deliverables

**Approval Gate**: Client approves T810A2-SCHEMA Request and implementation artifacts; proceed to formal handoff

---

### **PHASE 4: FORMAL HANDOFF**

**Duration**: 30 minutes
**Objective**: Deliver complete artifact package and transition to implementation

#### Activity 4.1: Handoff Brief Creation

**Deliverable**: `handoff_brief_T810A2-SCHEMA_to_Developer_v1.0.0.md`

**Content**:
- Executive summary of T810A2-SCHEMA deliverables
- Path references to all artifacts
- Integration notes for LLM_Developer
- Open issues requiring implementation attention
- Success criteria for implementation validation

#### Activity 4.2: Stakeholder Notifications

- Notify Client: T810A2-SCHEMA Request approved and ready for implementation
- Notify T810A1 Consultant: Integration validation complete
- Notify LLM_Developer: Implementation artifacts ready for consumption

#### Activity 4.3: Artifact Archival

- Ensure all artifacts committed to repository
- Update plan document status: `draft` → `completed`
- Update Request document status: `review` → `approved`

#### Deliverables (Phase 4 Complete)

- [ ] Handoff brief created and distributed
- [ ] All artifacts archived in repository
- [ ] Stakeholders notified
- [ ] T810A2-SCHEMA feature marked as complete (Request phase)

---

## V. RISKS & MITIGATIONS

| Risk ID | Risk Title | Description | Probability | Impact | Mitigation Strategy | Status |
|:--------|:-----------|:------------|:------------|:-------|:--------------------|:-------|
| T810A2-RISK-001 | Template Annotation Decision Delays | Risk that HYBRID approach needs validation with T810A1 consultant, delaying schema development | Medium | Medium | Front-load decision in Phase 0; use ad-hoc T810A1 consultation if needed; default to HYBRID per client preference | MONITORED |
| T810A2-RISK-002 | Controlled Vocabulary Incompleteness | Risk that Cara Care exemplar and example tracking JSON do not provide sufficient vocabulary coverage | Medium | High | Validate against both sources; flag gaps explicitly for client review; invoke LLM_Researcher for industry standards if approved | MONITORED |
| T810A2-RISK-003 | Schema Complexity Ambiguity | Risk that "structured but not overcomplicated" balance is subjective and requires iteration | Low | Medium | Use Cara Care UX as simplicity benchmark; validate at Checkpoint 1 (F-RID Review); default to simplest viable approach | MONITORED |
| T810A2-RISK-004 | Mandatory/Optional Field Mapping Gaps | Risk that Probe triggering rules require clinical judgment beyond available documentation | Medium | High | Cross-reference with T810A1-NFR-009; validate with T810A1 consultant at Checkpoint 2; document uncertainty explicitly | MONITORED |
| T810A2-RISK-005 | Timeline Pressure (12-14 hour target) | Risk that exhaustive vocabulary development exceeds time estimate | Medium | Medium | Prioritize exhaustive controlled vocabularies (core deliverable); defer edge case refinement if needed; extend timeline if client approves | ACCEPTED |
| T810A2-RISK-006 | Integration Validation Delays | Risk that T810A1 integration issues discovered late (Phase 3) require schema rework | Low | High | Early alignment in Phase 1 (F-RID validation); continuous traceability validation; Checkpoint 2 integration review | MITIGATED |
| T810A2-RISK-007 | Qualitative NFR Validation | MVP uses subjective acceptance criteria for NFRs (token efficiency, self-documentation, vocabulary completeness) without quantitative thresholds per NOTE-002; Story acceptance may lack measurable quality gates requiring post-MVP iteration | Medium | Medium | Accept qualitative criteria per client directive; document validation approach in Stories with understanding that criteria will be refined after implementation testing; plan post-MVP quantitative validation per NOTE-002 | ACCEPTED |

---

## VI. OPEN ISSUES

| Issue ID | Issue Title | Description | Owner | Status | Priority | Proposed Date | Target Resolution |
|:---------|:-----------|:------------|:------|:-------|:---------|:--------------|:------------------|
| T810A2-ISSUE-001 | Scale Semantic Mapping Completeness | Numeric scales (-2 to 2 for mood, 1-5 for stress/pain/bloating) require exhaustive semantic label mappings; Cara Care screenshots show natural language but backend values unclear | LLM_Consultant (T810A2) | OPEN | High | 2025-10-19 | Phase 2 (Activity 2.2, 2.4) |
| T810A2-ISSUE-002 | Stool Metadata Vocabulary Scope | "urgent, full_evacuation, partial_evacuation, mucus" examples provided but comprehensive list needed; example tracking JSON shows additional values ("undigested food", "oil") | LLM_Consultant (T810A2) | OPEN | High | 2025-10-19 | Phase 2 (Activity 2.4) |
| T810A2-ISSUE-003 | Meal Metadata Vocabulary Scope | "chili, oily, sweet, light" examples provided but comprehensive culinary descriptor list needed | LLM_Consultant (T810A2) | OPEN | Medium | 2025-10-19 | Phase 2 (Activity 2.3) |
| T810A2-ISSUE-004 | Structured Object Metadata Design | Client directive: "structured objects with metadata" but exact pattern unclear (nested objects vs. flat with metadata fields) | LLM_Consultant (T810A2) | OPEN | High | 2025-10-19 | Phase 1 (Activity 1.3) |

---

## VII. COORDINATION CHECKPOINTS

| Checkpoint | Phase | Target Timing | Participants | Review Focus | Approval Authority |
|:-----------|:------|:--------------|:-------------|:-------------|:-------------------|
| **Gate 0: Foundation Approval** | Phase 0 | 1-2 hours | Client, LLM_Consultant (T810A2) | Section III.A-III.D high-level framing | Client |
| **Checkpoint 1: F-RID Review** | Phase 1 | 3-4 hours | Client, LLM_Consultant (T810A2), LLM_Consultant (T810A1) | Section III.E-III.I foundational requirements; traceability validation | Client |
| **Checkpoint 2: Complete Schema Review** | Phase 2 | 8-10 hours | Client, LLM_Consultant (T810A2), LLM_Consultant (T810A1) | Section III.J stories; exhaustive vocabularies; integration patterns | Client |
| **Checkpoint 3: Final Approval Gate** | Phase 3 | 12-14 hours | Client, LLM_Consultant (T810A2), LLM_Consultant (T810A1), LLM_Developer | Request document finalization; implementation artifacts; integration validation | Client |

---

## VIII. NEXT ACTIONS

**Immediate Next Step**: Proceed with Phase 0 - Activity 0.1 (High-Level Problem Framing)

**Consultant Proposal**: Draft Section III.A-III.C content for `request_T810A2-SCHEMA.md` following T810A1 structural pattern

**Expected Output**: Proposed content for:
- Section III.A: Feature Solution Framework (decision criteria, problem recap, constraints)
- Section III.B: Source & Scope (in-scope, out-of-scope boundaries)
- Section III.C: Business Objectives & Success Signals (primary objectives, success criteria)

**Client Action**: Review and approve Phase 0 framing proposal

---

## IX. DOCUMENT METADATA

**Version History**:
- v1.0.0 (2025-10-19): Initial plan creation following client directive; 4 phases with coordination checkpoints; living document approach

**Status**: Draft - awaiting Client approval to proceed with Phase 0

**Related Artifacts**:
- Handoff Brief: `handoff_brief_T810A2-PATIENT_v1.1.0.md`
- Request Document: `request_T810A2-SCHEMA.md` (living document)
- T810A1 Request: `request_T810A1-PROMPT.md` (integration dependency)
- T810 SPS: `sps_T810-GASTRO.md` (governance parent)
- T102 Concept: `concept_T102-CONSULTANT.md` (structural governance)

---

**END OF PLAN DOCUMENT**
