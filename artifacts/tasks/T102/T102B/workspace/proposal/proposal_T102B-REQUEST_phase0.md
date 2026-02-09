---
artifact_type: 'PROPOSAL'
initiative_id: 'T102'
epic_id: 'T102B'
epic_code: 'REQUEST'
version: '1.0.0'
date: '2026-01-17'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T102/T102B/workspace/roadmap/roadmap_T102B-REQUEST_Phase0.md'
analysis_reference: 'prompt/artifacts/tasks/T102/T102B/workspace/analysis/analysis_T102B_epic-foundation-assessment.md'
governance_rules: 'prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md'
target_document: 'prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md'
target_section: 'III.C.2 (Epic: T102B)'
---

# PHASE 0 PROPOSAL: `T102B / REQUEST` — Epic Requirements & Governance

## I. EXECUTIVE SUMMARY

This proposal presents the Phase 0 consultancy outcomes for Epic `T102B (REQUEST — Request Workflow)` and serves as the working communication channel for E-ID development via Socratic dialogue (Subphase 2).

**Phase Scope**: Epic Requirements & Governance Development per `roadmap_T102B-REQUEST_Phase0.md` Subphase 2.

**Key Objectives**:
1. Develop all Epic Requirements (E-RIDs) across 6 categories: Assumptions (ASSUM), Constraints (CON), Quality Goals (QG), Dependencies (DEP), Interfaces (IF), Implementation Guidance (IG)
2. Develop Epic Governance Decision Records (E-GDRs) with paired Architectural Decision Records (E-ADRs)
3. Import and resolve Issues/Risks from research findings (T102B-RES-001, T102B-RES-002)
4. Obtain Client approval before SSOT implementation (SPS + Concept)

**Research Foundation**: This Phase integrates findings from:
- `T102B-RES-001` (Request Artifact Analysis) — External industry standards comparison (W1-W7 weaknesses, P1-P8 proposals, S1-S8 strengths)
- `T102B-RES-002` (Epic Foundation Assessment) — Internal foundation gap analysis (55 E-ID candidates identified)

**Critical Gaps Identified** (per analysis):
- **Gap 1**: T102B has 0 IF and 0 IG items (T102A baseline: 1 IF, 6 IGs)
- **Gap 2**: ID collision between SSOT Issue IDs and RES-001 Issue IDs
- **Gap 3**: Missing explicit interface contracts for SPS intake and Concept handoff
- **Gap 4**: 0 GDRs and 0 ADRs (4 GDR/ADR pairs recommended)

**Candidate Inventory Summary** (seeded from analysis):

| Category | Candidate Count | High Priority | Status |
|:---------|:----------------|:--------------|:-------|
| E-ASSUM | 3 | 2 | **CONFIRMED** (bodies in III.A; 1 removed as duplicate) |
| E-CON | 4 | 3 | **CONFIRMED** (bodies in III.B) |
| E-QG | 3 | 2 | **CONFIRMED** (bodies in III.C; 2 removed per inheritance) |
| E-DEP | 5 | 3 | **CONFIRMED** (bodies in III.D; 1 removed as duplicate) |
| E-IF | 3 | 2 | **CONFIRMED** (bodies in III.E) |
| E-IG | 6 | 4 | **CONFIRMED** (bodies in III.F) |
| E-GDR | 4 | 2 | Pending Dialogue |
| E-ADR | 4 | 3 | Pending Dialogue |
| E-ISSUE | 8 | 6 | Pending Resolution |
| E-RISK | 5 | 2 | Pending Mitigation |
| E-NOTE | 8 | 2 | Pending Extraction |
| **TOTAL** | **53** | **31** | 24 confirmed, 29 pending |

**Consultation Approach**: This proposal serves as a dynamic workspace for collaborative E-RID specification development through Socratic dialogue. Content will be developed incrementally through Activity 2.3-2.6, with full normative bodies populated before Client approval gate (Subphase 3).

**Recommended Dialogue Sequence** (per analysis):
1. **E-CON** — Establish non-negotiable boundaries before E-IG development
2. **E-IF** — Develop interface contracts (SPS intake, approval output, Concept handoff)
3. **E-IG** — Develop implementation guidance with operational rules + acceptance checks
4. **E-GDR/ADR** — Formalize governance decisions with paired specifications

---

## II. CANDIDATE INVENTORY (WORKING INDEX; NOT FULL BODIES)

<!-- PURPOSE: Single index of IDs we will validate; keep summaries to 1 line each. -->
<!-- STATUS VALUES: existing | research-suggested | dialogue-discovered | confirmed -->

### A. E-RIDs

#### 1. Assumptions (T102B-ASSUM-###)

| ID | Title | 1-line Summary | Source | Status | Spec Reference |
|:---|:------|:---------------|:-------|:-------|:---------------|
| `T102B-ASSUM-001` | **SPS Narrative Sufficiency** | SPS Feature provides sufficient narrative context to derive initial Request scope | SPS | confirmed | Section III.A |
| `T102B-ASSUM-002` | **RLITE Adoption** | Teams will choose RLITE for simple features rather than forcing Full Request | RES-001 P1 + RES-002 Topic 5 | confirmed | Section III.A |
| `T102B-ASSUM-003` | **Author Self-Assessment** | Authors can accurately self-assess feature complexity using IG-004 decision tree | RES-002 Topic 5 + Dialogue | confirmed | Section III.A |

#### 2. Constraints (T102B-CON-###)

| ID | Title | 1-line Summary | Source | Status | Spec Reference |
|:---|:------|:---------------|:-------|:-------|:---------------|
| `T102B-CON-001` | **No Custom Processors** | v1 Request tooling uses standard Markdown/YAML only; no custom parsers or validators | SSOT + T102-CON-001 extension | confirmed | Section III.B |
| `T102B-CON-002` | **No Story FR Mandate** | Story-level FRs SHALL NOT be mandatory at Request Phase; deferred to Concept/Design per SAFe Iteration Planning pattern | RES-001 W2/P2 + RES-002 Topic 5 | confirmed | Section III.B |
| `T102B-CON-003` | **Template Variant Boundary** | RLITE SHALL NOT expand into Full Request by accretion; variant boundary is governance-enforced | RES-001 P1 + RES-002 Topic 5 | confirmed | Section III.B |
| `T102B-CON-004` | **Decision Storage Boundary** | Request artifacts SHALL NOT embed ADR bodies; reference Concept canonical ADRs via ID citation per `T102-STD-003` | RES-001 W1 + RES-002 Topic 3 | confirmed | Section III.B |

#### 3. Quality Goals (T102B-QG-###)

| ID | Title | 1-line Summary | Source | Status | Spec Reference |
|:---|:------|:---------------|:-------|:-------|:---------------|
| `T102B-QG-001` | **Adoption Friction Reduction** | RLITE stays <200 lines and reduces authoring overhead for simple work | RES-001 W5/P1 + RES-002 Topic 5 | confirmed | Section III.C |
| `T102B-QG-002` | **No Duplication Overhead** | Avoid FR/IG duplication; requirements remain self-contained | RES-001 W1/P3 + RES-002 Topic 6 | confirmed | Section III.C |
| `T102B-QG-003` | **Artifact Completeness** | Mandatory sections validated before Request approval gate | RES-002 Topic 6 + Dialogue | confirmed | Section III.C |

#### 4. Dependencies (T102B-DEP-###)

| ID | Title | 1-line Summary | Source | Status | Spec Reference |
|:---|:------|:---------------|:-------|:-------|:---------------|
| `T102B-DEP-001` | **SPS Intake Alignment** | SPS Feature bundle is the only Request intake | SSOT | confirmed | Section III.D |
| `T102B-DEP-002` | **Industry Standards** | Align requirements quality to ISO 29148 principles; references `T102-NOTE-003` | SSOT + T102-NOTE-003 | confirmed | Section III.D |
| `T102B-DEP-003` | **RLITE Depends On RST** | RLITE is a governed subset of RST architecture; T102B4 depends on T102B1 | RES-001 P1 + RES-002 Topic 5 | confirmed | Section III.D |
| `T102B-DEP-004` | **Concept Boundary Alignment** | Request remains requirements-only; decisions stored in Concept | RES-001 W1/W2 + RES-002 Topic 3 | confirmed | Section III.D |
| `T102B-DEP-005` | **Migration Discipline** | Structural changes require migration notes and compatibility plan | RES-001 RISK-004 + RES-002 Topic 4 | confirmed | Section III.D |

#### 5. Interfaces (T102B-IF-###)

| ID | Title | 1-line Summary | Source | Status | Spec Reference |
|:---|:------|:---------------|:-------|:-------|:---------------|
| `T102B-IF-001` | SPS Intake Contract | Define minimum SPS-provided inputs needed to start a Request | RES-002 Topic 3 + T102A-IF-001 | confirmed | Section III.E |
| `T102B-IF-002` | Approved Request Output | Define what constitutes an "Approved Request" and its evidence payload | RES-002 Topic 3 + Phase0 plan | confirmed | Section III.E |
| `T102B-IF-003` | Request Output Contract | Define required trace links and ID references for downstream ingestion (Design/Plan) | RES-002 Topic 3 + SSOT purpose | confirmed | Section III.E |

### B. E-DIDs

#### 1. Governance Standards (T102B-STD-###)

| ID | Title | 1-line Summary | Source | Status | Spec Reference |
|:---|:------|:---------------|:-------|:-------|:---------------|
| `T102B-STD-001` | Request Governance Snapshot Standard | Define what "Phase 0 complete" means for Request epic | T102A pattern + RES-002 Topic 2 | research-suggested | Section IV.A |
| `T102B-STD-002` | Workflow Typology Standard | Formalize when to use Full Request vs RLITE vs PR-only | RES-001 Topic 9 + RES-002 Topic 5 | research-suggested | Section IV.A |
| `T102B-STD-003` | Gate Evidence Standard | Make gate evidence expectations explicit (RPG-dependent) | SSOT risk + RES-002 Topic 2 | research-suggested | Section IV.A |
| `T102B-STD-004` | Section Classification Policy | Mandatory/Optional/Deferred sections become governance, not preference | RES-001 P4 + RES-002 Topic 2 | research-suggested | Section IV.A |

#### 2. Architectural Decisions (T102B-ADR-###)

| ID | Title | Authority STD | 1-line Summary | Source | Status | Spec Reference |
|:---|:------|:--------------|:---------------|:-------|:-------|:---------------|
| `T102B-STD-001` | Request Architecture Standard | `T102B-STD-001 (Request Governance Snapshot Standard)` | Defines the structural architecture of Request artifact family | RES-001 P1-P4 + RES-002 Topic 2 | research-suggested | Section IV.B |
| `T102B-STD-002` | Section Classification Standard | `T102B-STD-004 (Section Classification Policy)` | Implements mandatory/optional/deferred section schema | RES-001 P4 + RES-002 Topic 2 | research-suggested | Section IV.B |
| `T102B-STD-003` | Story FR Deferral Standard | `T102B-STD-002 (Workflow Typology Standard)` | Operationalizes deferral of story-level FRs beyond Request | RES-001 W2/P2 + RES-002 Topic 5 | research-suggested | Section IV.B |
| `T102B-STD-004` | Request Lite Specification | `T102B-STD-002 (Workflow Typology Standard)` | Defines RLITE structure + selection criteria | RES-001 P1 + RES-002 Topic 5 | research-suggested | Section IV.B |

---

### C. E-IIDs

#### 1. Implementation Guidance (T102B-IG-###)

| ID | Title | 1-line Summary | Source | Status | Spec Reference |
|:---|:------|:---------------|:-------|:-------|:---------------|
| `T102B-IG-001` | Section Classification | Authoring rules for Mandatory/Optional/Deferred sections | RES-001 P4 + RES-002 Topic 6 | confirmed | Section III.F |
| `T102B-IG-002` | FR/IG Consolidation | Eliminate duplication via a single "requirements-with-guidance" pattern | RES-001 W1/P3 + RES-002 Topic 6 | confirmed | Section III.F |
| `T102B-IG-003` | Story Index Deferral | Keep Story Index in Request; defer story-level FR bodies to Concept/Design | RES-001 W2/P2 + RES-002 Topic 6 | confirmed | Section III.F |
| `T102B-IG-005` | Gate Evidence Checklist | Gate evidence checklist pattern (what must exist to approve) | SSOT risk + RES-002 Topic 6 | confirmed | Section III.F |
| `T102B-IG-006` | Inheritance Referencing | Reference-only inheritance rules for Request artifacts (avoid repetition) | RES-001 W3/P5 + RES-002 Topic 6 | confirmed | Section III.F |
| `T102B-IG-007` | Handoff Routing | Informative validation checklist for Request downstream routing per IF-003 | Activity 3.5 + DEC-001 | confirmed | Section III.C.1 |

**Removed IG** (Activity 2.6 disposition):
- IG-004: Redundant with `T102B-STD-004-CLAUSE-004` and `T102B-STD-004-CLAUSE-005`; all references updated to point to ADR-004 directly

---

#### 2. Integration Guidance (T102B-INT-###)

| ID | Title | 1-line Summary | Source | Status | Spec Reference |
|:---|:------|:---------------|:-------|:-------|:---------------|
| `T102B-INT-001` | SPS→Request Intake Coordination | Non-normative guidance for SPS bundle validation and intake workflow | Activity 2.5 + T102B-IF-001 | confirmed | Section III.C.2 |
| `T102B-INT-002` | Request→Concept Handoff Coordination | Non-normative guidance for Request output packaging and Concept readiness | Activity 2.5 + T102B-IF-003 | confirmed | Section III.C.2 |
| `T102B-INT-003` | T102 IF Schema Coordination | Proposes unified IF table schema standardization for T102 consideration | Activity 2.6 + NOTE-008 | confirmed | Section III.C.2 |
| `T102B-INT-004` | T102 ADR vs IG Framework Coordination | Proposes ADR vs IG decision framework for T102 consideration | Activity 2.6 + NOTE-009 | confirmed | Section III.C.2 |
| `T102B-INT-005` | T102 IG Non-Normative Coordination | Proposes T102 clarify IG uses SHOULD/MAY language only | Activity 2.6 + NOTE-010 | confirmed | Section III.C.2 |
| `T102B-INT-006` | Category Promotion Coordination | Proposes cross-category promotion standard (NOTE→IG→ADR) for T102 | Activity 2.6 | confirmed | Section III.C.2 |

### D. E-OIDs

#### 1. Issues (T102B-ISSUE-###)

| ID | Title | Description | Source | Priority | Status |
|:---|:------|:------------|:-------|:---------|:-------|
| `T102B-ISSUE-001` | YAML Keys Finalization | Finalize exact Request YAML key set & enums | SSOT | High | OPEN |
| `T102B-ISSUE-002` | Manifest Format Decision | Decide manifest format (`.json` vs `.md`) and storage path | SSOT | High | OPEN |
| `T102B-ISSUE-003` | Story Register Scope | Reduce story detail to Story Index; defer FRs downstream | SSOT + RES-001 W2 | High | OPEN |
| `T102B-ISSUE-004` | ID Collision With RES-001 | SSOT Issue IDs collide semantically with RES-001 Issue IDs; requires renumbering | RES-002 Topic 4 | High | OPEN |
| `T102B-ISSUE-005` | Missing IF Inventory | No explicit interface contracts exist for SPS intake or Concept handoff | RES-002 Topic 1/3 | High | OPEN |
| `T102B-ISSUE-006` | Missing IG Inventory | No implementation guidance exists to operationalize authoring rules | RES-002 Topic 1/6 | High | OPEN |
| `T102B-ISSUE-007` | Missing Phase & Gates Snapshot | SSOT Governance & Roadmap table was empty and misaligned with Phase 0 plan | RES-002 Topic 7 | High | RESOLVED |
| `T102B-ISSUE-008` | Feature Register Missing RLITE | T102B4 (RLITE) was missing from SSOT Feature Register | RES-002 Topic 7 | High | RESOLVED |

#### 2. Risks (T102B-RISK-###)

| ID | Title | Description | Source | Severity | Likelihood | Priority | Status |
|:---|:------|:------------|:-------|:---------|:-----------|:---------|:-------|
| `T102B-RISK-001` | Intake Drift | SPS Feature bundle may evolve without Request alignment checks | SSOT | High | Medium | High | OPEN |
| `T102B-RISK-002` | Gate Evidence Undefined | Approval criteria remain implicit without IG-005 | SSOT | Medium | High | Medium | OPEN |
| `T102B-RISK-003` | Documentation Trap | Story-level FRs at Request stage block MVP delivery | RES-001 RISK-001 | High | High | High | OPEN |
| `T102B-RISK-004` | Template Migration | Structural changes may break existing Request artifacts | RES-001 RISK-004 | Low | Medium | Low | OPEN |
| `T102B-RISK-005` | Workflow Undifferentiation | Heavyweight docs applied to lightweight changes without RLITE | RES-001 RISK-005 | Medium | Medium | Medium | OPEN |

#### 3. Notes (T102B-NOTE-###)

| ID | Title | Content Summary | Source | Disposition |
|:---|:------|:----------------|:-------|:------------|
| `T102B-NOTE-002` | Model-B Governance | Epic vs feature control pattern reminder | SPS | KEEP in Section III.D.3 |

**Removed NOTEs** (Activity 2.6 disposition):
- NOTE-001: Duplicates Epic Purpose in SPS Dossier
- NOTE-003: Should reference RES-001 directly (not standalone NOTE)
- NOTE-004: Duplicates `T102-NOTE-002 (Agent Compatibility)`
- NOTE-006: Duplicates ADR-003 rationale
- NOTE-011: Absorbed into `T102B-STD-004-CLAUSE-005 (Decision Tree Workflow)`

**Converted to INT** (Activity 2.6 cross-scope promotion):
- NOTE-008 → `T102B-INT-003 (T102 IF Schema Coordination)`
- NOTE-009 → `T102B-INT-004 (T102 ADR vs IG Framework Coordination)`
- NOTE-010 → `T102B-INT-005 (T102 IG Non-Normative Coordination)`

#### 4. Research (T102B-RES-###)

| ID | Title | Summary | Linked To | Brief | Report |
|:---|:------|:--------|:----------|:------|:-------|
| `T102B-RES-001` | Request Artifact Analysis | Industry standards comparison; W1-W7, P1-P8, S1-S8 | E-CON, E-IG, E-GDR, E-ADR | [brief](../../research/brief/brief_T102B-RES-001_request-artifact-analysis.md) | [report](../../research/report/report_T102B-RES-001_request-artifact-analysis.md) |
| `T102B-RES-002` | Epic Foundation Assessment | Internal gap analysis; 55 E-ID candidates | All E-IDs | [brief](../../research/brief/brief_T102B-RES-002_epic-foundation-assessment.md) | [report](../../research/report/report_T102B-RES-002_epic-foundation-assessment.md) |

---

## III. E-ID BODIES (NORMATIVE; POPULATED IN ACTIVITY 2.3)

<!-- PURPOSE: This section becomes the canonical spec during the phase. -->
<!-- Bodies populated via Socratic dialogue per category -->

### A. E-RID

#### 1. Assumptions (T102B-ASSUM-###)

* **ASSUM Validation Lifecycle Summary**

  <!-- PURPOSE: Track assumption validation per T102-STD-005-FR-009; follows T801A exemplar pattern -->

  | ID | Title | Status | Validation Method | Timing | Owner | If Invalidated | CON Cross-Ref |
  |:---|:------|:-------|:------------------|:-------|:------|:---------------|:--------------|
  | `T102B-ASSUM-001` | SPS Narrative Sufficiency | `Pending` | Pilot Request derivation from first 3 SPS Features | Feature T102B1 | LLM_Consultant | Escalate: Client provides additional narrative | — |
  | `T102B-ASSUM-002` | RLITE Adoption | `Pending` | RLITE adoption metrics post-v1 launch | Feature T102B4 | Client | Mitigate: strengthen IG-004 decision tree | `T102B-CON-003` |
  | `T102B-ASSUM-003` | Author Self-Assessment | `Pending` | Author feedback during pilot workflows | Feature T102B1/B4 | Client | Mitigate: enhance IG-004 decision criteria | — |

* **T102B-ASSUM-001 (SPS Narrative Sufficiency)** — `T102A (SPS)` Feature bundles provide sufficient narrative context (Purpose statement, Epic requirements, inherited initiative-level IDs) to derive initial Request scope and navigation structures. 

* **T102B-ASSUM-002 (RLITE Adoption)** — Teams will appropriately select RLITE workflow for simple features rather than defaulting to Full Request, thereby realizing adoption friction reduction per `T102B-QG-001`. 

* **T102B-ASSUM-003 (Author Self-Assessment)** — Authors can accurately self-assess feature complexity using `T102B-IG-004` decision criteria to select appropriate workflow (Full Request vs RLITE vs PR-only). 

#### 2. Constraints (T102B-CON-###)

* **T102B-CON-001 (No Custom Processors)** — Request artifacts in v1 SHALL use only standard Markdown rendering and YAML parsing; no custom preprocessors, validators, or template engines are permitted. This extends `T102-CON-001` by explicitly prohibiting tooling complexity beyond standard editors.
  External Reference: `T102-CON-001 (Format Requirements)`

* **T102B-CON-002 (No Story FR Mandate)** — Story-level Functional Requirements (FRs) SHALL NOT be mandatory at Request Phase per `T102B-RES-001` — W2, P2. Request artifacts MAY include a Story Index for navigation, but detailed story-level FR bodies and acceptance criteria SHALL be deferred to `T102D (DESIGN)` workflows. This constraint mitigates risk of Documentation Trap per SAFe Iteration Planning best practices.

* **T102B-CON-003 (Template Variant Boundary)** — `T102B4 (RLITE)` artifacts SHALL NOT expand beyond their defined scope (<200 lines) by accretion per `T102B-RES-001` — P1. Authors SHALL NOT add sections incrementally until RLITE becomes a de facto Full Request. Scope expansion requires explicit workflow transition via `T102B-IG-004` decision tree. This constraint prevents risk of workflow undifferentiation.

* **T102B-CON-004 (Decision Storage Boundary)** — Request artifacts SHALL NOT embed ADR body content. All architectural and governance decisions SHALL be stored canonically in Concept artifacts per `T102-STD-001` and `T102B-DEP-004`. Request artifacts MAY reference Concept ADRs via formal ID citation per `T102-STD-005`. This constraint eliminates content duplication and ensures single source of truth for decisions.
  External Reference: `T102-STD-001 (Consultancy Operating Model Standard)`, `T102-STD-003 (Explicit Inheritance Model)`, `T102-STD-005 (ID Specification & Rules)`

#### 3. Quality Goals (T102B-QG-###)

* **T102B-QG-001 (Adoption Friction Reduction)** — `T102B4 (RLITE)` artifacts SHALL remain within size constraints per `T102B-CON-003` and reduce authoring overhead for simple features per `T102B-RES-001` — W5, P1. Adoption friction is measured by: (a) author time-to-complete, (b) RLITE vs Full Request selection ratio for eligible features.
  External Reference: `T102-QG-003 (Low-Disruption Implementation)`

* **T102B-QG-002 (No Duplication Overhead)** — Request artifacts SHALL avoid content duplication between FR sections and IG sections per `T102B-RES-001` — W1, P3. Requirements SHOULD be self-contained without requiring cross-reference to separate guidance documents for comprehension.

* **T102B-QG-003 (Artifact Completeness)** — Request artifacts SHALL pass completeness validation against section classification (mandatory sections populated) before Request approval gate. Completeness evidence includes: 
  (a) all mandatory sections contain substantive content, 
  (b) Inherited Considerations table populated per `T102-STD-003`, 
  (c) navigation structures (Story Index if applicable) populated.

#### 4. Dependencies (T102B-DEP-###)

* **T102B-DEP-001 (SPS Intake Alignment)** — Request workflow SHALL accept intake exclusively from `T102A (SPS)` Feature bundles per `T102-STD-001`. No Request artifact SHALL be initiated without a corresponding approved Feature entry in the `T102A1` Feature Register. The SPS Feature bundle provides: Feature ID, Purpose statement, Epic constraints, and inherited initiative-level IDs. This dependency is operationalized by `T102B-IF-001` and assumes `T102B-ASSUM-001`.
  External Reference: `T102-STD-001 (Consultancy Operating Model Standard)`

* **T102B-DEP-002 (Industry Standards)** — Request artifacts SHOULD align requirements quality to ISO 29148 principles for completeness, consistency, and verifiability. Industry standards referenced in `T102-NOTE-003` (ISO 29148, SAFe, BABOK v3) provide the quality baseline for Request content structure and requirements expression.
  External Reference: `T102-NOTE-003 (Industry Standards)`

* **T102B-DEP-003 (RLITE Depends On RST)** — Feature `T102B4 (RLITE)` is a governed subset of `T102B1 (RST)` architecture per `T102B-RES-001` — P1. RLITE SHALL NOT be developed until RST section classification decisions are complete. RLITE inherits RST mandatory section definitions and applies reduction rules per `T102B-IG-001`. This dependency establishes the `T102B1` → `T102B4` feature sequencing constraint for Phase 1.

* **T102B-DEP-004 (Concept Boundary Alignment)** — Request workflow operates within the requirements-only boundary. Request artifacts remain focused on WHAT is required; HOW decisions (architectural specifications) SHALL be stored in Concept artifacts. Request→Concept handoff transfers requirements for solution design; no design content returns to Request.
  External Reference: `T102-STD-001 (Consultancy Operating Model Standard)`, `T102-STD-003 (Explicit Inheritance Model)`

* **T102B-DEP-005 (Migration Discipline)** — Structural changes to Request templates or standards SHALL include migration notes documenting: 
(a) affected artifacts, 
(b) required updates, 
(c) compatibility approach (grandfather existing vs mandatory update). 
This dependency supports monitoring risks related to template migration.

#### 5. Interfaces (T102B-IF-###)

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
  | `inherited_considerations` | Section (TBD) | **Yes** | Per `T102-STD-003` |


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

### B. E-DRID
#### 1. Epic Governance Standards

| STD ID | Title | Status | Owner | Effective | Supersedes | Adopts | Verification | Reference |
|:-------|:------|:-------|:------|:----------|:-----------|:-------|:-------------|:----------|
| `T102B-STD-001` | **Request Governance Snapshot Standard** | Proposed | Client | — | — | `T102B-STD-001 (Request Architecture Standard)` | Review MUST verify: Phase 0 completion criteria checklist passed, Feature Register populated | `T102-STD-009 (Governance Standards Model)` |
| `T102B-STD-002` | **Workflow Typology Standard** | Proposed | Client | — | — | `T102B-STD-003 (Story FR Deferral Standard)`, `T102B-STD-004 (Request Lite Specification)` | Review MUST verify: workflow selection rationale documented, RLITE boundary (<200 lines) enforced | `T102-STD-009 (Governance Standards Model)` |
| `T102B-STD-003` | **Gate Evidence Standard** | Proposed | Client | — | — | — | Review MUST verify: gate evidence checklist items present, approval signature recorded | `T102-STD-009 (Governance Standards Model)` |
| `T102B-STD-004` | **Section Classification Policy** | Proposed | Client | — | — | `T102B-STD-002 (Section Classification Standard)` | Review MUST verify: section classification applied per adopted spec, mandatory sections populated | `T102-STD-009 (Governance Standards Model)` |

* **T102B-STD-001 (Request Governance Snapshot Standard)** — The project SHALL use `T102B-STD-001 (Request Architecture Standard)` as the specification for Request artifact family architecture, SPS intake alignment, and Phase 0 completion criteria. All Request workflow artifacts SHALL conform to the architecture standard before Feature design begins.
  - **Minimum Viable Conformance**:
    1) Request artifact family follows the hierarchical architecture (RST, RLITE, RPG, MANIFEST) per `T102B-STD-001-CLAUSE-001`.
    2) Inheritance model uses ID-reference-only with no content duplication per `T102B-STD-001-CLAUSE-002`.
    3) Phase 0 completion criteria satisfied before Feature design begins per `T102B-STD-001-CLAUSE-003`.
  External Reference: `T102-STD-001 (Operating Model Standard)`

* **T102B-STD-002 (Workflow Typology Standard)** — The project SHALL use `T102B-STD-003 (Story FR Deferral Standard)` and `T102B-STD-004 (Request Lite Specification)` as the specifications for Request workflow typology. Three workflow variants are established: Full Request, RLITE, and PR-only.
  - **Minimum Viable Conformance**:
    1) Story Index used for navigation; story-level FR bodies deferred to Design per `T102B-STD-003-CLAUSE-001`, `T102B-STD-003-CLAUSE-002`.
    2) RLITE artifacts remain under 200 lines and do not expand by accretion per `T102B-STD-004-CLAUSE-001`.
    3) RLITE contains mandatory sections only per the defined section list per `T102B-STD-004-CLAUSE-002`.
    4) Workflow selection follows the decision tree criteria per `T102B-STD-004-CLAUSE-004`, `T102B-STD-004-CLAUSE-005`.

* **T102B-STD-003 (Gate Evidence Standard)** — Request approval gates SHALL require documented evidence across four categories before an artifact is approved. The approver MUST record approval status, date, and role in artifact metadata. If any mandatory evidence item is incomplete, the author MUST either remediate or obtain a documented waiver with rationale before approval.
  - **Minimum Viable Conformance**:
    1) Governance evidence: inherited considerations populated, STD/ADR references valid.
    2) Content evidence: all mandatory sections populated, requirement statements testable.
    3) Structure evidence: YAML header complete, Story Index populated (if applicable).
    4) Process evidence: validation checklist passed, approver sign-off recorded.
    5) Authors SHOULD follow `T102B-IG-005` for detailed checklist items and remediation guidance.
  External Reference: `T102-STD-009 (Governance Standards Model)`

* **T102B-STD-004 (Section Classification Policy)** — The project SHALL use `T102B-STD-002 (Section Classification Standard)` as the specification for Request section classification schema, ensuring artifact completeness per `T102B-QG-003`. Section classification is a governance decision, not author preference.
  - **Minimum Viable Conformance**:
    1) Three classification categories applied: Mandatory, Optional, Deferred per `T102B-STD-002-CLAUSE-001`.
    2) Full Request section list followed per canonical table per `T102B-STD-002-CLAUSE-002`.
    3) RLITE section list followed per canonical table per `T102B-STD-002-CLAUSE-003`.
    4) Validation rules enforced: empty mandatory sections fail gate per `T102B-STD-002-CLAUSE-004`.
  External Reference: `T102-STD-009 (Governance Standards Model)`


#### 2. Epic Architectural Decisions
| ADR ID | Title | Authority STD | Status | Owner | Effective | Supersedes | Canonical Path |
|:-------|:------|:--------------|:-------|:------|:----------|:-----------|:---------------|
| `T102B-STD-001` | **Request Architecture Standard** | `T102B-STD-001 (Request Governance Snapshot Standard)` | Proposed | LLM_Consultant | — | — | [T102B-STD-001](../../standards/T102B-STD-001_request-architecture-standard.md) |
| `T102B-STD-002` | **Section Classification Standard** | `T102B-STD-004 (Section Classification Policy)` | Proposed | LLM_Consultant | — | — | [T102B-STD-002](../../standards/T102B-STD-002_section-classification-standard.md) |
| `T102B-STD-003` | **Story FR Deferral Standard** | `T102B-STD-002 (Workflow Typology Standard)` | Proposed | LLM_Consultant | — | — | [T102B-STD-003](../../standards/T102B-STD-003_story-fr-deferral-standard.md) |
| `T102B-STD-004` | **Request Lite Specification** | `T102B-STD-002 (Workflow Typology Standard)` | Proposed | LLM_Consultant | — | — | [T102B-STD-004](../../standards/T102B-STD-004_request-lite-specification.md) |

* **T102B-STD-001 (Request Architecture Standard)** {#t102b-std-001}
  * **Context**
    Per `T102B-STD-001 (Request Governance Snapshot Standard)`, a unified architecture is required for the Request artifact family to prevent structural drift and ensure consistent authoring.
  * **Decision**
    Define a hierarchical artifact architecture where `T102B1` is the canonical Request template defining all possible sections, `T102B4` is a governed subset of `T102B1` per `T102B-CON-003`, `T102B2` provides section prioritization guidance, and `T102B3` defines metadata schema.
  * **Specification**
    * **T102B-STD-001-CLAUSE-001 (Artifact Hierarchy)**
      - `T102B1 (RST)` is the canonical Request template defining all possible sections.
      - `T102B4 (RLITE)` is a governed subset of `T102B1` per `T102B-CON-003`.
      - `T102B2 (RPG)` provides section classification per `T102B-STD-002`.
      - `T102B3 (MANIFEST)` defines YAML header schema and metadata requirements.
    * **T102B-STD-001-CLAUSE-002 (Inheritance Model)**
      - Request artifacts SHALL inherit initiative-level IDs via Inherited Considerations table per `T102-STD-003`.
      - Request artifacts SHALL NOT duplicate content from SPS; reference via ID citation only per `T102B-IG-006`.
      - Request artifacts SHALL NOT embed ADR bodies per `T102B-CON-004`.
    * **T102B-STD-001-CLAUSE-003 (Phase 0 Completion Criteria)**
      - Epic Dossier sections i-v complete in SPS.
      - All E-RIDs confirmed (ASSUM, CON, QG, DEP, IF, IG categories).
      - All E-DRIDs confirmed (GDR/ADR pairs).
      - Feature Register populated with `T102B1-B4`.
  * **Alternatives**
    - (a) Separate BRD + SRS artifacts per industry pattern — rejected; increases artifact count and coordination overhead without proportional traceability benefit for this project's single-author workflow.
    - (b) Flat, non-hierarchical template set — rejected; no governance over RLITE/RST relationship, risking template drift.
  * **Consequences**
    - (+) Single architecture prevents template divergence.
    - (+) Clear inheritance model reduces content duplication.
    - (±) Requires Feature sequencing (`T102B1` before `T102B4`).
    - (-) Architecture changes require coordinated updates across all Features.
  * **References**
    `T102B-STD-001 (Request Governance Snapshot Standard)`, `T102-STD-003 (Explicit Inheritance Model)`, `T102B-CON-003 (Template Variant Boundary)`, `T102B-CON-004 (Decision Storage Boundary)`
  * **Provenance**
    - `prompt/artifacts/tasks/T102/T102B/workspace/analysis/analysis_T102B_epic-foundation-assessment.md`

* **T102B-STD-002 (Section Classification Standard)** {#t102b-std-002}
  * **Context**
    Per `T102B-STD-004 (Section Classification Policy)`, a unified section classification schema is required to ensure consistent artifact structure and enable completeness validation per `T102B-QG-003`.
  * **Decision**
    Define three classification categories (Mandatory, Optional, Deferred) and specify canonical section lists for Full Request and RLITE variants.
  * **Specification**
    * **T102B-STD-002-CLAUSE-001 (Classification Categories)**
      - **Mandatory**: Section MUST contain substantive content before approval gate.
      - **Optional**: Section MAY be omitted or contain placeholder text.
      - **Deferred**: Section content belongs in downstream artifacts; SHALL contain reference/placeholder only.
    * **T102B-STD-002-CLAUSE-002 (Full Request Section List)**
      | Section | Classification | Notes |
      |:--------|:---------------|:------|
      | YAML Header | Mandatory | Per MANIFEST schema |
      | Feature Purpose | Mandatory | 1-2 paragraphs |
      | Inherited Considerations | Mandatory | Per `T102-STD-003` |
      | Scope | Mandatory | In/Out bullets |
      | Stakeholder Analysis | Optional | For cross-team features |
      | Story Index | Conditional | Required if >1 story |
      | NFR Section | Optional | If feature-specific NFRs exist |
      | Research/Evidence | Optional | Link to RES artifacts |
      | Approval Gate | Mandatory | Checklist + sign-off |
    * **T102B-STD-002-CLAUSE-003 (RLITE Section List)**
      | Section | Classification | Notes |
      |:--------|:---------------|:------|
      | YAML Header | Mandatory | Per MANIFEST schema |
      | Feature Purpose | Mandatory | 1-2 paragraphs |
      | Inherited Considerations | Mandatory | Per `T102-STD-003` |
      | Scope | Mandatory | In/Out bullets |
      | Success Criteria | Mandatory | Measurable outcomes |
      | Approval Gate | Mandatory | Simplified checklist |
    * **T102B-STD-002-CLAUSE-004 (Validation Rules)**
      - Mandatory sections with empty content SHALL fail gate validation.
      - Optional sections MAY be omitted entirely (no placeholder required).
      - Deferred sections SHALL contain explicit deferral note with target artifact.
  * **Alternatives**
    - (a) Binary classification (Mandatory/Optional only) — rejected; insufficient granularity for deferred content that belongs in downstream artifacts.
    - (b) Four-tier classification (adding "Conditional") — rejected; "Conditional" overlaps with "Optional" for authoring purposes and adds complexity without clarity.
  * **Consequences**
    - (+) Enables automated completeness checking per `T102B-QG-003`.
    - (+) Clear section expectations reduce authoring ambiguity.
    - (+) Variant-specific lists support RLITE scope boundary.
    - (±) Section additions require ADR update.
    - (-) May not cover all edge case sections.
  * **References**
    `T102B-STD-004 (Section Classification Policy)`, `T102B-QG-003 (Artifact Completeness)`, `T102B-STD-004 (Request Lite Specification)`
  * **Provenance**
    - `prompt/artifacts/tasks/T102/T102B/research/report/report_T102B-RES-001_request-artifact-analysis.md`

* **T102B-STD-003 (Story FR Deferral Standard)** {#t102b-std-003}
  * **Context**
    Per `T102B-STD-002 (Workflow Typology Standard)`, story-level specification at Request stage is identified as an industry anti-pattern per SAFe guidance and `T102B-RES-001` W2 findings. Request artifacts need story navigation without detailed FR bodies.
  * **Decision**
    Define Story Index as the mechanism for story navigation in Request; defer detailed story-level FR bodies and acceptance criteria to `T102D (DESIGN)` workflows.
  * **Specification**
    * **T102B-STD-003-CLAUSE-001 (Story Index Structure)**
      - Request artifacts MAY include a Story Index for multi-story features.
      - Story Index SHALL contain: Story ID, Title, Purpose summary (1-2 sentences), Design Link (populated post-handoff).
      - Story Index SHALL NOT contain: Detailed FR bodies, acceptance criteria, implementation details.
    * **T102B-STD-003-CLAUSE-002 (Deferral Boundary)**
      - Story-level FRs (testable behavior per story) SHALL be deferred to Design phase.
      - Story-level acceptance criteria (Gherkin AC) SHALL be deferred to Design phase.
      - Feature-level scope (Story Index with purpose summaries) SHALL remain in Request.
    * **T102B-STD-003-CLAUSE-003 (Exceptions)**
      - Single-story features MAY include story-level FR in Request if complexity warrants Full Request workflow.
      - Exception requires explicit justification in Request Section Notes.
  * **Alternatives**
    - (a) Full story-level FRs at Request stage — rejected; SAFe anti-pattern per `T102B-RES-001` W2; creates documentation trap blocking MVP delivery.
    - (b) No story reference at all in Request — rejected; loses navigation structure for multi-story features; authors need story-level orientation.
  * **Consequences**
    - (+) Reduces documentation trap risk per `T102B-RISK-003`.
    - (+) Aligns with SAFe Iteration Planning best practices.
    - (+) Enables MVP delivery without blocking on story details.
    - (±) Requires clear handoff protocol to Design phase.
    - (-) Some stakeholders may expect story details in Request.
  * **References**
    `T102B-STD-002 (Workflow Typology Standard)`, `T102B-CON-002 (No Story FR Mandate)`, `T102B-IG-003 (Story Index Deferral)`, `T102B-RISK-003 (Documentation Trap)`
  * **Provenance**
    - `prompt/artifacts/tasks/T102/T102B/research/report/report_T102B-RES-001_request-artifact-analysis.md`

* **T102B-STD-004 (Request Lite Specification)** {#t102b-std-004}
  * **Context**
    Per `T102B-STD-002 (Workflow Typology Standard)`, simple features require a lightweight documentation path to reduce adoption friction. RLITE must remain <200 lines per `T102B-CON-003` while providing sufficient context for development.
  * **Decision**
    Define RLITE as a governed subset of `T102B1 (RST)` with mandatory sections only; include selection criteria for workflow routing.
  * **Specification**
    * **T102B-STD-004-CLAUSE-001 (RLITE Scope Boundary)**
      - RLITE artifacts SHALL remain under 200 lines total per `T102B-CON-003`.
      - RLITE artifacts SHALL NOT expand by section accretion.
      - If scope exceeds boundary during authoring, escalate to Full Request per `T102B-IG-004`.
    * **T102B-STD-004-CLAUSE-002 (RLITE Mandatory Sections)**
      - YAML Header (per MANIFEST schema).
      - Feature Purpose (1-2 paragraphs).
      - Inherited Considerations table (per `T102-STD-003`).
      - Scope (In Scope / Out of Scope bullets).
      - Success Criteria (measurable outcomes).
      - Approval Gate section.
    * **T102B-STD-004-CLAUSE-003 (RLITE Excluded Sections)**
      - Story Index (single-story or no-story features).
      - Detailed NFR section (inherit epic-level NFRs).
      - Extended stakeholder analysis.
      - Research/Evidence sections.
    * **T102B-STD-004-CLAUSE-004 (Selection Criteria)**
      | Factor | Full Request | RLITE | PR-only |
      |:-------|:-------------|:------|:--------|
      | Story count | >3 stories | 1-3 stories | 0-1 stories |
      | Architectural impact | New patterns | Existing patterns | Trivial change |
      | Stakeholder visibility | High (cross-team) | Medium (team) | Low (developer) |
      | Complexity | High | Low-Medium | Trivial |
    * **T102B-STD-004-CLAUSE-005 (Decision Tree Workflow)**
      Authors SHALL apply selection criteria per CLAUSE-004 using this decision workflow:
      1. **Assess story count threshold**: If >3 stories → Full Request; if 0-1 stories → consider PR-only
      2. **Assess architectural impact**: If new patterns/integrations → Full Request; if trivial change → consider PR-only
      3. **Assess stakeholder visibility**: If cross-team coordination required → Full Request
      4. **Apply complexity tiebreaker**: If uncertain after factor assessment, default to higher tier
      5. **Boundary enforcement**: If RLITE scope threatens to exceed 200 lines per `T102B-CON-003`, escalate to Full Request

      **Heuristics**:
      - If any single factor indicates Full Request, Full Request SHOULD be selected unless compelling justification exists
      - If uncertain between RLITE and Full Request, prefer Full Request to avoid future escalation
      - If feature is truly trivial (documentation update, config change), PR-only workflow MAY bypass Request entirely
      - Authors SHOULD document workflow selection rationale in Request frontmatter for audit trail
  * **Alternatives**
    - (a) Single heavyweight template for all features — rejected; adoption friction per `T102B-RES-001` W5; simple features over-documented.
    - (b) Completely separate RLITE template (not derived from RST) — rejected; creates drift risk and dual maintenance burden per `T102B-DEP-003`.
    - (c) PR-only for all lightweight changes — rejected as sole alternative; included as third workflow tier for trivial changes but insufficient for features needing minimal requirements documentation.
  * **Consequences**
    - (+) Reduces authoring overhead for simple features per `T102B-QG-001`.
    - (+) Clear selection criteria prevent workflow confusion.
    - (+) Boundary enforcement prevents scope creep.
    - (±) Requires author self-assessment accuracy per `T102B-ASSUM-003`.
    - (-) Some simple features may be incorrectly routed to RLITE.
  * **References**
    `T102B-STD-002 (Workflow Typology Standard)`, `T102B-CON-003 (Template Variant Boundary)`, `T102B-QG-001 (Adoption Friction Reduction)`, `T102B-IG-004 (Request Lite Selection)`
  * **Provenance**
    - `prompt/artifacts/tasks/T102/T102B/research/report/report_T102B-RES-001_request-artifact-analysis.md`
    - `prompt/artifacts/tasks/T102/T102B/workspace/analysis/analysis_T102B_epic-foundation-assessment.md`


### C. E-IID 

#### 1. Implementation Guidance (T102B-IG-###)

* **T102B-IG-001 (Section Classification)** — Request authors SHOULD apply the section classification schema defined in `T102B-STD-002` when authoring Request artifacts. This guidance provides the authoring workflow for applying classification rules; the canonical section lists, classification categories, and validation rules are specified in `T102B-STD-002`. Authors SHOULD consult `T102B-STD-002` for definitive section requirements per Request variant (Full Request vs RLITE).

* **T102B-IG-002 (FR/IG Consolidation)** — Request authors SHOULD avoid content duplication between Functional Requirements (FR) sections and Implementation Guidance (IG) sections per `T102B-QG-002`. The "requirements-with-guidance" pattern consolidates requirement statements with inline authoring hints rather than separating into parallel sections. Detailed implementation patterns belong in Feature-level IGs or ADRs, not in FR bodies.

* **T102B-IG-003 (Story Index Deferral)** — Request artifacts SHOULD include a Story Index for multi-story features, providing story identification and navigation structure. Story-level FR bodies and detailed acceptance criteria are deferred to `T102D (DESIGN)` workflows per `T102B-CON-002` and `T102B-STD-003`. The Story Index contains: Story ID, Title, Purpose summary, and Concept/Design link (populated post-handoff). This pattern mitigates Documentation Trap risk.
  Reference: `T102B-STD-003 (Story FR Deferral Standard)`

* **T102B-IG-005 (Gate Evidence Checklist)** — Authors SHOULD use the following checklist to prepare Request artifacts for approval gate per `T102B-STD-003`. Each category lists recommended evidence items; items marked **(Proposed Normative)** are candidates for future elevation to STD-003 MUST requirements.

  | Category | Evidence Items | Notes |
  |:---------|:---------------|:------|
  | **Governance** | Inherited Considerations populated; STD/ADR references valid; GDR→STD migration complete | **(Proposed Normative)**: Inherited Considerations validation |
  | **Content** | All mandatory sections contain substantive content; FR/NFR statements testable per ISO 29148 principles; no placeholder-only mandatory sections | **(Proposed Normative)**: Testable requirements check |
  | **Structure** | YAML header complete per MANIFEST schema; Story Index populated (if >1 story); section classification applied per `T102B-STD-002` | — |
  | **Process** | Validation checklist passed; approver sign-off recorded with role and date; workflow selection rationale documented in frontmatter | — |

  **Common Pitfalls**:
  - Inherited Considerations table left empty (copy from SPS Epic Dossier)
  - Story Index included for single-story features (omit per `T102B-STD-002-CLAUSE-003`)
  - Approval gate attempted without mandatory section content (run section classification check first)

  **Remediation Guidance**:
  - If governance evidence missing: review `T102B-IG-006` for inheritance referencing patterns
  - If content evidence missing: review section classification per `T102B-STD-002` for mandatory section list
  - If waiver needed: document rationale per `T102B-STD-003` waiver mechanism

  Reference: `T102B-STD-003 (Gate Evidence Standard)`, `T102B-QG-003 (Artifact Completeness)`

* **T102B-IG-006 (Inheritance Referencing)** — Request authors SHOULD use reference-only inheritance per `T102-STD-003`. Inherited initiative and epic-level IDs SHOULD be cited by ID reference in the Inherited Considerations table; content SHOULD NOT be duplicated from parent artifacts. When referencing inherited IDs in Request body text, use short-hand format per `T102-STD-005`. Full reference format is required only in dedicated Reference sections.
  External Reference: `T102-STD-003 (Explicit Inheritance Model)`, `T102-STD-005 (ID Specification & Rules)`

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

#### 2. Integration Guidance (T102B-INT-###)

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
  - Story-level detail deferred to Design phase per `T102B-CON-002` and `T102B-STD-003`

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

  External Reference: `T102-STD-005-CLAUSE-002 (Taxonomy & Terminology)`, `T102B-IF-001`, `T102B-IF-002`, `T102B-IF-003`

* **T102B-INT-004 (T102 ADR vs IG Framework Coordination)** — Non-normative coordination note proposing the ADR vs IG decision framework for T102 initiative consideration. This framework was adopted for T102B governance during Phase 0 consultation.

  **Proposed Framework** (for T102 adoption):
  - ADR required when: real decision with trade-offs, expensive to change later, cross-cutting impact
  - IG appropriate when: "how-to" guidance after decision set, low-risk/local, non-controversial
  - Red flag: IG with new normative constraint not in RID SHOULD be escalated to ADR or CON

  **T102B Adoption Evidence**:
  - T102B-STD-001 through ADR-004 represent real decisions (Options A/B/C considered)
  - T102B-IG-001 through IG-006 provide "how-to" referencing governing ADRs
  - IG bodies use SHOULD/MAY; MUST/SHALL reserved for ADR CLAUSE content

  **Compatibility Expectation**:
  - T102A/T102C MAY adopt this framework for consistency
  - T102 governance decision determines initiative-wide adoption

  External Reference: `T102-STD-005-CLAUSE-005B (Implementation Guidance Rules)`, `T102-STD-005-CLAUSE-005C (Integration Notes Rules)`, `T102B-NOTE-009`

* **T102B-INT-005 (T102 IG Non-Normative Coordination)** — Non-normative coordination note proposing that T102 initiative clarify IG items use SHOULD/MAY language only, with MUST/SHALL reserved for ADR Specification clauses.

  **Current State**:
  - T102-STD-005-CLAUSE-005B permits: "IG MAY use MUST/SHALL when defining authoring standards intended to be enforceable"
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

  External Reference: `T102-STD-005-CLAUSE-005B`, `T102B-NOTE-010`

* **T102B-INT-006 (Category Promotion Coordination)** — Non-normative coordination note proposing a cross-category promotion standard for informative items (NOTE/IG/INT) to normative items (RID/DRID). This addresses a governance gap identified during T102B Phase 0 consultation.

  **Governance Gap**:
  - `T102-STD-007-CLAUSE-009` defines cross-scope promotion (Epic→Initiative)
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

  External Reference: `T102-STD-007-CLAUSE-009 (Cross-Scope Promotion)`, `T102-STD-005-CLAUSE-002`

### D. E-OID

#### 1. Issues (T102B-ISSUE-###)


#### 2. Risks (T102B-RISK-###)


#### 3. Notes (T102B-NOTE-###)

* **T102B-NOTE-002 (Model-B Governance)** — Feature-level Requests keep specs small and parallelizable; the Epic provides overall control and is described in the SPS. 

---

## IV. ISSUES & RISKS REGISTER

### A. Issues

<!-- GUIDANCE:
Per T102-STD-007: OPEN => notes/date = `—`; closed statuses => date present
-->

| ID | Title | Description | Owner | Status | Priority | Proposed Date | Resolution Notes | Resolution Date |
|:---|:------|:------------|:------|:-------|:---------|:--------------|:-----------------|:----------------|
| `T102B-ISSUE-001` | YAML Keys Finalization | Finalize exact Request YAML key set & enums | Client | `OPEN` | `HIGH` | 2026-01-17 | — | — |
| `T102B-ISSUE-002` | Manifest Format Decision | Decide manifest format (`.json` vs `.md`) and storage path | Client | `OPEN` | `HIGH` | 2026-01-17 | — | — |
| `T102B-ISSUE-003` | Story Register Scope | Reduce story detail to Story Index; defer FRs downstream | Client | `IN-REVIEW` | `HIGH` | 2026-01-17 | Resolution framework established via `T102B-STD-003 (Story FR Deferral Standard)`; final Story Index template deferred to T102B1 Feature | — |
| `T102B-ISSUE-004` | ID Collision With RES-001 | SSOT Issue IDs (001-003) collide semantically with RES-001 Issue IDs; requires renumbering decision | Client | `OPEN` | `MEDIUM` | 2026-01-17 | — | — |
| `T102B-ISSUE-005` | Missing IF Inventory | No explicit interface contracts exist for SPS intake or Concept handoff | Client | `RESOLVED` | `HIGH` | 2026-01-17 | Addressed by Activity 2.3; see `T102B-IF-001 (SPS Intake Contract)`, `T102B-IF-002 (Approved Request Output)`, `T102B-IF-003 (Request Output Contract)` | 2026-01-20 |
| `T102B-ISSUE-006` | Missing IG Inventory | No implementation guidance exists to operationalize authoring rules | Client | `RESOLVED` | `HIGH` | 2026-01-17 | Addressed by Activity 2.3; see `T102B-IG-001` through `T102B-IG-006` in Proposal Section III.C | 2026-01-20 |
| `T102B-ISSUE-007` | Missing Phase & Gates Snapshot | SSOT Governance & Roadmap table was empty | LLM_Consultant | `RESOLVED` | `HIGH` | 2026-01-15 | Populated in Subphase 1 Activity 1.4 with Phase 0/1A/1B/2 structure | 2026-01-17 |
| `T102B-ISSUE-008` | Feature Register Missing RLITE | T102B4 (RLITE) was missing from SSOT Feature Register | LLM_Consultant | `RESOLVED` | `HIGH` | 2026-01-15 | T102B4 added in Subphase 1 Activity 1.5 with `in-discovery` status | 2026-01-17 |

### B. Risks

<!-- GUIDANCE:
Per T102-STD-007: OPEN => notes/date = `—`; closed statuses => date present
-->

| ID | Title | Description | Owner | Status | Priority | Proposed Date | Mitigation Notes | Mitigation Date |
|:---|:------|:------------|:------|:-------|:---------|:--------------|:-----------------|:----------------|
| `T102B-RISK-001` | Intake Drift | SPS Feature bundle may evolve without Request alignment checks; Request becomes stale | Client | `MONITORED` | `HIGH` | 2026-01-17 | Monitoring via `T102B-IF-001 (SPS Intake Contract)`, `T102B-INT-001 (SPS→Request Coordination)`; ongoing alignment checks required | — |
| `T102B-RISK-002` | Gate Evidence Undefined | Approval criteria remain implicit; inconsistent gate enforcement | Client | `MITIGATED` | `MEDIUM` | 2026-01-17 | Gate evidence framework established; see `T102B-STD-003 (Gate Evidence Standard)`, `T102B-IG-005 (Gate Evidence Checklist)`; operational enforcement deferred to Phase 1 RPG development | 2026-01-22 |
| `T102B-RISK-003` | Documentation Trap | Story-level FRs at Request stage block MVP delivery; over-specification | Client | `MONITORED` | `HIGH` | 2026-01-17 | Mitigated via `T102B-CON-002 (No Story FR Mandate)`, `T102B-STD-003 (Story FR Deferral Standard)`; ongoing monitoring required to prevent documentation creep | — |
| `T102B-RISK-005` | Workflow Undifferentiation | Heavyweight docs applied to lightweight changes; adoption friction | Client | `MONITORED` | `MEDIUM` | 2026-01-17 | Mitigated via `T102B-STD-004 (Request Lite Specification)`, `T102B-IG-004 (Request Lite Selection)`; ongoing monitoring for RLITE adoption patterns | — |

---

## V. OPEN QUESTIONS REGISTER

<!-- PURPOSE: Track blocking questions requiring Client decision -->

| OQ ID | Question | Context | Blocking | Owner | Status | Resolution |
|:------|:---------|:--------|:---------|:------|:-------|:-----------|
| `T102B-OQ-001` | ID Collision Resolution Approach | SSOT ISSUE-001-003 vs RES-001 ISSUE-001-003 have different meanings | E-ISSUE seeding | Client | OPEN | — |
| `T102B-OQ-002` | Story FR Deferral Exceptions | When (if ever) are story FRs mandatory at Request? | E-CON-002, E-IG-003 | Client | OPEN | — |
| `T102B-OQ-003` | RLITE Minimum Sections | What must RLITE contain vs what can be omitted? | E-ADR-004 | Client | OPEN | — |

---

## VI. APPROVAL GATE (CLIENT)

<!-- PURPOSE: Capture formal approval for Phase 0 scope -->

### Approval Scope

Upon completion of Subphase 3 validation, Client approval covers:

- [ ] Epic Dossier sections i-v (Purpose, Scope, Inherited Considerations, Governance & Roadmap, Feature Register)
- [ ] All E-RIDs approved (6 categories: ASSUM, CON, QG, DEP, IF, IG)
- [ ] All E-GDRs approved (4 governance decisions)
- [ ] All E-ADRs approved (4 architectural specifications paired with GDRs)
- [ ] All Issues resolved or deferred with rationale
- [ ] All Risks mitigated or accepted with rationale
- [ ] All Open Questions resolved or deferred with rationale

### Approval Statement

<!-- To be completed in Subphase 3 Activity 3.9 -->

**Approved By**: _______________
**Date**: _______________
**Scope Confirmation**: I approve the Phase 0 deliverables as specified above for SSOT implementation.

---

## VII. LINKS REGISTER

| Link Type | Target | Path |
|:----------|:-------|:-----|
| Plan | Phase 0 Roadmap | `../roadmap/roadmap_T102B-REQUEST_Phase0.md` |
| Analysis | RES-002 Synthesis | `../analysis/analysis_T102B_epic-foundation-assessment.md` |
| SPS | T102 Initiative SPS | `../../../consultant/sps/sps_T102-CONSULTANT.md` |
| Concept | T102 ADR Compendium | `../../../consultant/concept/concept_T102-CONSULTANT.md` |
| Research Brief (RES-001) | Request Artifact Analysis | `../../research/brief/brief_T102B-RES-001_request-artifact-analysis.md` |
| Research Report (RES-001) | Request Artifact Analysis | `../../research/report/report_T102B-RES-001_request-artifact-analysis.md` |
| Research Brief (RES-002) | Epic Foundation Assessment | `../../research/brief/brief_T102B-RES-002_epic-foundation-assessment.md` |
| Research Report (RES-002) | Epic Foundation Assessment | `../../research/report/report_T102B-RES-002_epic-foundation-assessment.md` |
| Exemplar | T801A Phase 1 Proposal | `../../../../T801/consultant/workspace/proposal/T801A/proposal_T801A_phase1.md` |
| Exemplar | T810A1 Request | `../../../../T810/consultant/request/request_T810A1-PROMPT.md` |

---

## VII-A. T102 DEPENDENCY TRACKING

<!-- PURPOSE: Document T102 initiative dependency status for Activity 2.8 compliance -->

### Dependency Status

| T102 Stream | Deliverable | Status | Compliance Notes |
|:------------|:------------|:-------|:-----------------|
| Stream 3 (STD Token) | `T102-STD-009`, `T102-STD-009` | Draft Available | T102B GDR→STD migration applied per ADR-009-CLAUSE-004 |
| Stream 4A (ADR-004) | `T102-STD-004`, ADR-004 Update | Draft Available | T102B ADR Index/Body format aligned per ADR-004-CLAUSE-001/006 |
| Stream 4B (ADR-005) | `T102-STD-005`, ADR-005 Update | Draft Available | T102B ID references use formal format per ADR-005-CLAUSE-004 |
| Stream 5 (SSOT) | SPS/Concept updates | Pending | T102B awaits T102 SSOT publication before Stream 3 validation |

### Migration Applied

- **Activity 2.8 Date**: 2026-01-25
- **Source Specs**: `proposal_T102-CWD_refactor_gdrs_into_std.md`, `proposal_T102-CWD_refactor-adr-004-005.md`
- **Items Migrated**: 4 GDR→STD (T102B-STD-001 through STD-004), 4 ADR authority citations updated
- **Cross-Reference Updates**: E-RID bodies referencing `T102-GDR-001` updated to `T102-STD-001`

---

## VIII. CHANGELOG

`prompt/artifacts/tasks/T102/T102B/workspace/proposal/changelog_proposal_T102B-REQUEST_phase0.md`


**END OF PROPOSAL**
