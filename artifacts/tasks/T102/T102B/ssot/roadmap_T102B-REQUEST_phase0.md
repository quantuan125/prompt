---
artifact_type: 'PLAN'
initiative_id: 'T102'
epic_id: 'T102B'
epic_code: 'REQUEST'
Phase: '0'
version: '3.2.0'
date: '2026-01-24'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
parent_plan: 'prompt/artifacts/Activitys/T102/consultant/workspace/plan/T102/roadmap_T102-CDW.md'
parent_Activity: '1.2'
---

# CONSULTANCY PLAN: T102B (REQUEST) — Phase 0: Epic Foundation Establishment

## I. EXECUTIVE SUMMARY

<!-- PURPOSE: Define Phase 0 objectives, scope, and exit criteria -->

This plan defines the consultancy workflow to establish a **comprehensive, traceable foundation** for Epic `T102B (REQUEST)` inside the initiative SSOT:
- SSOT file: `prompt/artifacts/Activitys/T102/consultant/sps/sps_T102-CONSULTANT.md`

**Role Boundary**
- `LLM_Consultant`: requirements analysis, governance mapping, proposal drafts, research commissioning, approval gates
- `LLM_Researcher`: internal research execution (commissioned via brief)
- `LLM_Developer`: SSOT implementation and codebase work (post-approval)
- `Client`: decision owner and approval authority

**Phasing Intent**
- **Phase 0 (This Plan)**: Establish epic dossier foundation through research, Epic Dossier sections (i-v), E-RID development, proposal iteration, validation, and SSOT implementation
- **Phase 1 (Future)**: Feature-level Request artifact authoring for T102B1-B4
- **Phase 2 (Future)**: Integration and workflow operationalization

**Phase 0 Objective**: Establish comprehensive T102B epic foundation grounded in T102B-RES-002 research, implement Epic Dossier sections i-v per T102A-STD-001 + T102-STD-003, develop all E-RIDs through Socratic dialogue, develop E-GDRs with paired E-ADRs, validate all content for T102 framework compliance, obtain Client approval, and implement into SSOT artifacts.

**Key Exit Milestone**: Foundation Readiness — Epic `T102B` approved with:
- Epic Dossier sections i-v complete (Purpose, Scope, Inherited Considerations, Governance & Roadmap, Feature Register)
- Complete E-RID inventory (6 categories: DEP, CON, ASSUM, QG, IF, IG)
- E-GDR/E-ADR compendium (4+ governance decisions with paired architectural specifications)
- Issues/Risks register (imported from research + consultancy dialogue)
- SSOT implementation complete (SPS + Concept artifacts updated)

**Research Foundation**: This Phase commissions and integrates:
- `T102B-RES-002` (Epic Foundation Assessment) — Internal research on existing T102B foundation gaps, E-RID candidates extraction from RES-001 actionable items, integration dependency mapping, and workflow typology implications analysis

---

## II. CONTEXT MATERIALS & PREREQUISITES

<!-- PURPOSE: Define required reading, working assumptions, and workspace files -->

### A. Required Reading Before Each Stream

**CRITICAL**: Before proceeding with any consultancy in this plan, LLM_Consultant MUST review the following materials to maintain contextual understanding:

**Initiative Governance (SSOT Authority)**:
- `prompt/artifacts/Activitys/T102/consultant/sps/sps_T102-CONSULTANT.md` — Initiative baseline (Section III.B, Section III.C.1-3), T102-STD-003/004/005/006/007 standards
- `prompt/artifacts/Activitys/T102/consultant/concept/concept_T102-CONSULTANT.md` — ADR compendium and governance decisions

**Structural Exemplars** (T810 GASTRO + T801 TRADER as references):
- `prompt/artifacts/Activitys/T810/consultant/request/request_T810A1-PROMPT.md` — Request golden exemplar (752 lines)
- `prompt/artifacts/Activitys/T810/consultant/sps/sps_T810-GASTRO.md` — SPS structure and Epic dossier pattern (sections i-v)
- `prompt/artifacts/Activitys/T801/consultant/workspace/plan/plan_T801A_Phase0-1.md` — Phase 0-1 plan structural exemplar

**Workspace Governance**:
- `prompt/artifacts/Activitys/T810/consultant/workspace/workspace_documentation_rules.md` — Plan/Proposal/Completion artifact roles and boundaries

**Current Work Foundation**:
- `prompt/artifacts/Activitys/T102/T102B/research/report/report_T102B-RES-001_request-artifact-analysis.md` — Request Artifact Analysis (W1-W7 weaknesses, P1-P4 proposals, S1-S8 strengths)
- `prompt/artifacts/Activitys/T102/consultant/research/report/report_T102-RES-003_initiative-status-assessment.md` — Initiative Status Assessment (PIVOT RECOMMENDED)
- `prompt/artifacts/Activitys/T102/consultant/workspace/plan/T102/roadmap_T102-CDW.md` — Parent initiative plan

**Decision Record Standards** (MANDATORY for all SubphaseS):
- T102-STD-003: Explicit Inheritance Model (Inherited Considerations table structure)
- T102-STD-004: Decision Records Index (GDR/ADR schema, body format, placement)
- T102-STD-005: ID Specification & Rules (categories, hierarchy, referencing)
- T102-STD-006: Research Artifacts Index (RES/NOTE ID patterns, placement)
- T102-STD-007: Issues & Risks Index (schema, enums, status/date coupling, cross-scope promotion)

### B. Working Assumptions

1. **T102A Pattern Reuse**: T102B can leverage T102A-proven consultancy patterns (governance snapshot, freeze discipline, handoff protocol)
2. **Research-Gated Foundation**: Epic foundation gaps require internal research (T102B-RES-002) before Epic Dossier and E-RID development
3. **Hybrid Workflow Typology**: Request artifact supports both Full Request (~750 lines) and Request Lite (<200 lines) per T102B-RES-001 findings
4. **Story FR Deferral**: Request Section J transitions from FR inventory to Story Index only, deferring FRs to Design workflow
5. **Existing Foundation Debt**: T102B epic dossier currently incomplete per T102-RES-003; requires structured remediation via Epic Dossier Foundation

### C. Key Design Decisions

**Epic Dossier Sequencing**: Epic Dossier Foundation precedes E-RID development to establish structural container before populating Epic Requirements section (section v).

**E-ID Seeding Strategy (Option C)**: Proposal Section II (Candidate Inventory) will include BOTH:
- Existing E-RIDs from current T102B dossier (marked `existing` status)
- New E-RID candidates from T102B-RES-002 (marked `research-suggested` status)

This dual-status approach enables systematic gap analysis while preserving existing work.

**Research Topics for RES-002**: Seven topics commissioned to provide comprehensive foundation (expanded from 5 during Activity 0.1):
1. Existing E-RID Gap Analysis (T102B dossier vs T102A pattern)
2. ADR/GDR Inventory Assessment
3. Integration Dependency Mapping (T102A/T102C)
4. T102B-RES-001 Actionable Items & Issue/Risk/NOTE Assessment (Enhanced with 3 sub-topics: E-RID extraction, NOTE-ID assessment, comprehensive Issue/Risk analysis)
5. Workflow Typology Implications (Request Lite, Story FR deferral)
6. Implementation Guidance Assessment (NEW - addresses critical IG gap)
7. Governance & Roadmap Validation (NEW - validates Phase & Gates structure)

---

## III. WORKSPACE FILE REGISTER

<!-- PURPOSE: Track all Phase 0 workspace artifacts -->

| File | Type | Purpose | Create Timing |
|:-----|:-----|:--------|:--------------|
| `roadmap_T102B-REQUEST_Phase0.md` | PLAN | Phase governance (this file) | Pre-existing (UPDATED) |
| `brief_T102B-RES-002_epic-foundation-assessment.md` | RESEARCH_BRIEF | Commission internal research for epic foundation assessment | Stream 0 (Activity 0.1) |
| `analysis_T102B_epic-foundation-assessment.md` | ANALYSIS | Consultant synthesis of research | Stream 0 |
| `proposal_T102B-REQUEST_phase0.md` | PROPOSAL | Dynamic E-RID/GDR workspace | Stream 2 |
| `notes_T102B-REQUEST_phase0.md` | NOTES | Phase decision NOTES + minutes | Throughout |

---

## IV. Phase 0 

<!-- PURPOSE: Define 4-Subphases structure for Phase 0 execution -->

### Stream 0: Research Commission (Internal)

**Objective**: Commission internal research (T102B-RES-002) to assess existing T102B epic foundation, extract E-RID candidates from RES-001 findings, map integration dependencies, and analyze workflow typology implications, providing the analytical baseline for Epic Dossier and E-RID development.

**Hard Gate**: Stream 1 MUST NOT begin until research report is delivered and analysis synthesis is complete.

#### Activity Register

| Activity ID | Description | Deliverable | Status |
|:------------|:------------|:------------|:-------|
| 0.1 | Research brief creation | `brief_T102B-RES-002_epic-foundation-assessment.md` | Complete |
| 0.2 | Research execution & delivery | `report_T102B-RES-002_epic-foundation-assessment.md` | Complete |
| 0.3 | Consultant analysis & synthesis | `analysis_T102B_epic-foundation-assessment.md` | Complete |
| 0.4 | NOTES file initialization & Stream 0 documentation | `notes_T102B-REQUEST_phase0.md` | SKIPPED |

#### Input Requirements

| Category | Files |
|:---------|:------|
| Initiative SSOT | `sps_T102-CONSULTANT.md` (III.B, III.C.1-3) |
| Concept SSOT | `concept_T102-CONSULTANT.md` (ADRs 003-007) |
| External Research | `report_T102B-RES-001_request-artifact-analysis.md` |
| Golden Exemplar | `request_T810A1-PROMPT.md` |
| Plan Context | `roadmap_T102-CDW.md` |

#### Activity 0.1: Research Brief Creation

**Purpose**: Define research scope, topics, and input packet for internal research execution.

**Deliverable**: `prompt/artifacts/Activitys/T102/T102B/research/brief/brief_T102B-RES-002_epic-foundation-assessment.md`

**Research Topics** (Internal Focus - Expanded to 7 topics):

| Topic | Objective |
|:------|:----------|
| 1 | Existing E-RID Gap Analysis (T102B dossier vs T102A pattern) |
| 2 | ADR/GDR Inventory Assessment |
| 3 | Integration Dependency Mapping (T102A/T102C) |
| 4 | T102B-RES-001 Actionable Items & Issue/Risk/NOTE Assessment (3 sub-topics: E-RID extraction, NOTE-ID assessment, comprehensive Issue/Risk analysis) |
| 5 | Workflow Typology Implications (Request Lite, FR deferral) |
| 6 | Implementation Guidance Assessment (addresses critical IG gap) |
| 7 | Governance & Roadmap Validation (validates Phase & Gates structure) |

**Input Packet Files**:
- `prompt/artifacts/Activitys/T102/consultant/sps/sps_T102-CONSULTANT.md` (Section III.B, Section III.C.1-3 for T102A/T102C patterns)
- `prompt/artifacts/Activitys/T102/consultant/concept/concept_T102-CONSULTANT.md` (T102-STD-003/004/005/006/007)
- `prompt/artifacts/Activitys/T102/T102B/research/report/report_T102B-RES-001_request-artifact-analysis.md`
- `prompt/artifacts/Activitys/T810/consultant/request/request_T810A1-PROMPT.md` (golden exemplar)
- `prompt/artifacts/Activitys/T102/consultant/workspace/plan/T102/roadmap_T102-CDW.md`

**Task Checklist**:
- [x] Research brief authored with 7 topics and input packet list
- [x] Research brief includes success criteria and deliverable specification
- [x] Research brief approved by Client (Gate 1 per T102-GDR-006)

#### Activity 0.2: Research Execution & Delivery

**Purpose**: Execute internal research via LLM_Researcher role; deliver research report.

**Deliverable**: `prompt/artifacts/Activitys/T102/T102B/research/report/report_T102B-RES-002_epic-foundation-assessment.md`

**Execution Method**: Internal research subagent (LLM_Researcher) consuming brief and input packet

**Task Checklist**:
- [x] Research brief handed off to LLM_Researcher
- [x] Research report delivered with findings organized by 7 topics
- [x] Research report includes recommendations mapped to E-RID categories
- [x] Research report validated per T102-GDR-007 quality controls (Gate 2)

#### Activity 0.3: Consultant Analysis & Synthesis

**Purpose**: Synthesize research findings into consultant analysis with E-RID/GDR candidate inventory.

**Deliverable**: `prompt/artifacts/Activitys/T102/T102B/workspace/analysis/analysis_T102B_epic-foundation-assessment.md`

**Analysis Sections**:
1. **Executive Summary** — Key findings and strategic implications
2. **E-RID Candidate Inventory** — Suggested E-RIDs per category (DEP, CON, ASSUM, QG, IF, IG) derived from research
3. **E-GDR/ADR Candidate Inventory** — Suggested governance decisions with paired architectural specifications
4. **Issues/Risks Import Candidates** — Issues and Risks from research findings for Section VI import
5. **Integration Readiness Assessment** — T102A/T102C dependency analysis and handoff protocol validation

**Task Checklist**:
- [x] Analysis file created with candidate inventories
- [x] E-RID candidates organized per ADR-005 categories
- [x] GDR/ADR candidates identified with pairing logic
- [x] Issues/Risks candidates extracted from research

#### Activity 0.4: NOTES File Initialization & Stream Documentation

**Purpose**: Initialize notes_T102B-REQUEST_phase0.md following template_workspace_log.md structure; document Stream 0 consultation notes, decisions, and carry-forward items.

**Deliverable**: `prompt/artifacts/Activitys/T102/consultant/workspace/NOTES/notes_T102B-REQUEST_phase0.md`

**Task Checklist**:
- [ ] NOTES file created with YAML header and Section I (NOTES SUMMARY)
- [ ] Stream 0 record added to Section II (Stream RECORDS) with narrative summary, decisions made, improvements & observations, next-Activity guidance
- [ ] Review raw files and existing consultation context to extract decisions and observations
- [ ] NOTE candidates extracted to Section III per T102-STD-006-FR-008

#### Output Deliverables

| Deliverable | Path | Purpose |
|:------------|:-----|:--------|
| Research Brief | `brief_T102B-RES-002_epic-foundation-assessment.md` | Commission internal research |
| Research Report | `report_T102B-RES-002_epic-foundation-assessment.md` | Research findings (5 topics) |
| Analysis | `analysis_T102B_epic-foundation-assessment.md` | E-RID/GDR candidates inventory |

#### Success Criteria Task Checklist

- [x] Research brief created and commissioned to LLM_Researcher
- [x] Research report delivered and validated
- [x] Analysis synthesis complete with candidate inventories
- [ ] NOTES file initialized and Stream 0 documentation complete <!-- SKIPPED per client directive: blocking development -->
- [x] Hard gate satisfied: Research baseline established before Stream 1 

---

### Stream 1: Epic Dossier Foundation (SPS Sections i-v)

**Objective**: Implement SPS sections i-v (Purpose → Feature Register) per T102A-STD-001 + T102-STD-003, establishing the structural foundation of the T102B epic dossier before E-RID development.

**Constraint**: This Stream updates SSOT directly via consultancy dialogue + approval; E-RID bodies deferred to Stream 2.

#### Activity Register

| Activity ID | Description | Deliverable | Status |
|:------------|:------------|:------------|:-------|
| 1.1 | Epic Purpose & Scope definition | SPS Section III.C.2.i-ii | Complete |
| 1.2 | Inherited Considerations table | SPS Section III.C.2.iii | Complete |
| 1.3 | Governance & Roadmap framework | SPS Section III.C.2.iv | Complete |
| 1.4 | Feature Register population | SPS Section III.C.2.iv (Feature table) | Complete |
| 1.5 | Epic Requirements placeholder | SPS Section III.C.2.v | Complete |
| 1.6 | NOTES file update - Stream 1 documentation | Updated `notes_T102B-REQUEST_phase0.md` | SKIPPED |

#### Input Requirements

| Category | Files |
|:---------|:------|
| Research Foundation | `report_T102B-RES-002_epic-foundation-assessment.md` |
| Analysis Synthesis | `analysis_T102B_epic-foundation-assessment.md` |
| T102A Pattern | `sps_T102-CONSULTANT.md` Section III.C.1 (T102A epic dossier) |
| Structural Exemplar | `sps_T810-GASTRO.md` (Epic dossier sections i-v) |

#### Epic Dossier Sections (Compliance Reference)

| Section | Content | Compliance Rule |
|:--------|:--------|:----------------|
| i. Purpose | Epic objective (1-2 paragraphs) | T102A pattern |
| ii. Scope | In Scope / Out of Scope lists | T102A pattern |
| iii. Inherited Considerations | Initiative ID inheritance table | T102-STD-003 |
| iv. Governance & Roadmap | Phase & Gates table, Feature Register | T102A-STD-001 |
| v. Epic Requirements | Placeholder for E-RIDs (populated in Stream 2) | T102A pattern |

#### Activity 1.1: Epic Purpose & Scope Definition

**Purpose**: Draft and approve epic Purpose (i) and Scope (ii) sections in consultancy dialogue.

**Target**: `sps_T102-CONSULTANT.md` Section III.C.2 (T102B Epic)

**Consultancy Approach**:
1. **Draft Proposal**: Consultant drafts Purpose and Scope sections based on T102B-RES-002 findings
2. **Socratic Dialogue**: ≥2 clarifying questions to Client on epic objectives, boundaries, and strategic intent
3. **Client Approval**: Explicit approval captured before implementation

**Target Sections**:
- **i. Purpose** — Epic objective: Refactor Request artifact and authoring workflows per consultancy operating model; transform Request into robust feature-level specification with clear handoff protocols
- **ii. Scope** — In Scope: T102B1-B4 features (RST, RSPG, MANIFEST, RLITE); Out of Scope: SPS/Concept/Design workflows, automation/validation tooling

**Task Checklist**:
- [x] Purpose section drafted (1-2 paragraphs)
- [x] Scope section drafted (In Scope / Out of Scope bullets)
- [x] Socratic dialogue conducted (≥2 clarifying questions)
- [x] Client approval captured

#### Activity 1.2: Inherited Considerations Table

**Purpose**: Populate Inherited Considerations table per T102-STD-003 (Explicit Inheritance Model).

**Target**: `sps_T102-CONSULTANT.md` Section III.C.2.iii

**Table Structure** (per ADR-003):

| Source Artifact | Source ID | Category | Inherited Rule IDs |
|:----------------|:----------|:---------|:-------------------|
| SPS | T102 | Constraints | `T102-CON-001`, `T102-CON-002`, `T102-CON-003`, `T102-CON-004` |
| SPS | T102 | Quality Goals | `T102-QG-001`, `T102-QG-002`, `T102-QG-003` |
| SPS | T102 | Interfaces | `T102-IF-001`, `T102-IF-002`, `T102-IF-003`, `T102-IF-004` |
| SPS | T102 | Implementation Guidance | `T102-IG-001` through `T102-IG-010` |
| SPS | T102 | Governance | `T102-GDR-001`, `T102-GDR-002`, `T102-GDR-003`, `T102-GDR-004`, `T102-GDR-005`, `T102-GDR-006`, `T102-GDR-007`, `T102-GDR-008` |

**Task Checklist**:
- [x] Inherited Considerations table populated
- [x] All initiative-level IDs referenced (no content duplication)
- [x] Table validated for ADR-003 compliance

#### Activity 1.3: Governance & Roadmap Framework

**Purpose**: Establish Governance & Roadmap section per T102A-STD-001 (Governance Snapshot Framework).

**Target**: `sps_T102-CONSULTANT.md` Section III.C.2.iv

**Section Components**:
1. **Scope & Ownership** — Epic Lead: LLM_Consultant; Decision Owner: Client; RACI reference to III.B.1
2. **Phase & Gates** — Phase 0 (Foundation), Phase 1 (Feature Design), Phase 2 (Integration) with exit milestones
3. **Feature Register** — T102B1-B4 rows (populated in Activity 1.4)
4. **External PM Tracking** — Reference to ticktick per T102-CON-004

**Task Checklist**:
- [x] Ownership and RACI defined
- [x] Phase sequence table populated (4 Phases: 0=Foundation, 1A=Template Design, 1B=Guideline Design, 2=Integration)
- [x] External PM reference documented

#### Activity 1.4: Feature Register Population

**Purpose**: Populate Feature Register with T102B1-B4 features.

**Target**: `sps_T102-CONSULTANT.md` Section III.C.2.iv (Feature Register table)

**Feature Register** (T102B1-B4):

| Feature ID | Code | Title | Purpose | Status | Canonical Link |
|:-----------|:-----|:------|:--------|:-------|:---------------|
| T102B1 | RST | Request Standard Template | Define normative Request artifact structure | Proposed | TBD |
| T102B2 | RSPG | Request Section Prioritization Guide | Establish section classification (Mandatory/Optional/Deferred) | Proposed | TBD |
| T102B3 | MANIFEST | Request Manifest Schema | Define Request metadata and FR inventory patterns | Proposed | TBD |
| T102B4 | RLITE | Request Lite Specification | Define streamlined Request variant for simple features | Proposed | TBD |

**Task Checklist**:
- [x] All 4 features registered with ID, Code, Title, Purpose (T102B1-B4)
- [x] Features marked with appropriate status: T102B1/B4 = `in-discovery`, T102B2/B3 = `proposed`
- [x] Feature register integrated into Governance & Roadmap section

#### Activity 1.5: Epic Requirements Placeholder

**Purpose**: Insert placeholder structure for Epic Requirements section (populated in Stream 2).

**Target**: `sps_T102-CONSULTANT.md` Section III.C.2.v

**Placeholder Structure**:
```markdown
##### v. Epic Requirements

* **Dependencies**
  <!-- Populated in Stream 2 -->

* **Constraints**
  <!-- Populated in Stream 2 -->

* **Assumptions**
  <!-- Populated in Stream 2 -->

* **Quality Goals**
  <!-- Populated in Stream 2 -->

* **Interfaces**
  <!-- Populated in Stream 2 -->

* **Implementation Guidance**
  <!-- Populated in Stream 2 -->
```

**Task Checklist**:
- [x] Placeholder structure preserved (existing content maintained)
- [x] DEP-004 marked for migration to IF section in Stream 2

#### Activity 1.6: NOTES File Update - Stream 1 Documentation

**Purpose**: Document Stream 1 consultation notes, decisions, and carry-forward items in NOTES file.

**Deliverable**: Updated `notes_T102B-REQUEST_phase0.md` Section II (Stream 1)

**Task Checklist**:
<!-- SKIPPED per client directive: moving directly to Stream 2 -->
- [ ] Stream 1 record added with consultation narrative, decisions, improvements, next-Activity guidance
- [ ] NOTE candidates extracted from Epic Dossier consultancy dialogue

#### Output Deliverables

| Section | Content | Location |
|:--------|:--------|:---------|
| i. Purpose | Epic objective (1-2 paragraphs) | SPS Section III.C.2.i |
| ii. Scope | In Scope / Out of Scope lists | SPS Section III.C.2.ii |
| iii. Inherited Considerations | Initiative ID inheritance table | SPS Section III.C.2.iii |
| iv. Governance & Roadmap | Phase & Gates, Feature Register | SPS Section III.C.2.iv |
| v. Epic Requirements | Placeholder structure (6 categories) | SPS Section III.C.2.v |

#### Success Criteria Task Checklist

- [x] Epic Purpose and Scope approved by Client
- [x] Inherited Considerations table complete and ADR-003 compliant
- [x] Governance & Roadmap framework established
- [x] Feature Register populated with T102B1-B4 (T102B1/B4 = `in-discovery`, T102B2/B3 = `proposed`)
- [x] Epic Requirements placeholder structure preserved (existing content maintained)
- [x] SPS Section III.C.2.i-v structurally complete
- [ ] NOTES file Stream 1 documentation complete <!-- SKIPPED per client directive -->

---

### Stream 2: Proposal Initialization & E-ID Development

**Objective**: Initialize Phase 0 proposal skeleton as the working communication channel, seed CANDIDATE INVENTORY from research (with dual-status for existing vs new E-RIDs), develop all E-IDs via Socratic dialogue following category precedence (RID → DRID → IID → OID), and import Issues/Risks.

**Hard Gate**: Proposal file MUST exist before E-RID dialogue begins (Activity 2.1 prerequisite).

**Category Sequencing** (per `T102-STD-005-RULE-003` Precedence):
1. **E-RID** (Requirements): ASSUM → CON → QG → DEP → IF → FR → NFR
2. **E-DRID** (Decisions): GDR → ADR pairs
3. **E-IID** (Implementation): IG → INT (non-normative; SHOULD/MAY only)
4. **E-OID** (Tracking): ISSUE → RISK → NOTE → RES index

#### Activity Register

| Activity ID | Description | Deliverable | Status |
|:------------|:------------|:------------|:-------|
| 2.1 | Proposal skeleton creation | `proposal_T102B-REQUEST_phase0.md` | `completed` |
| 2.2 | Seed candidate inventory from research | Proposal Section II | `completed` |
| 2.3 | E-RID development (7 token types via Socratic dialogue) | Proposal Section III.A (E-RID Bodies) | `in-progress` |
| 2.4 | E-DRID development (GDR → ADR pairs) | Proposal Section III.B (E-DRID Bodies) | `completed` |
| 2.5 | E-IID development (IG, INT; industry-aligned) | Proposal Section III.C (E-IID Bodies) | `completed` |
| 2.6 | E-OID development (ISSUE, RISK, NOTE assessment & classification) | Analysis file + Proposal Section III.D/E/IV | `completed` |
| 2.7 | NOTES file update | Updated `notes_T102B-REQUEST_phase0.md` | `deferred` |
| 2.8 | T102 Dependency Monitoring & GDR→STD Token Migration | Updated `proposal_T102B-REQUEST_phase0.md` (GDR→STD) | `completed` |

#### Input Requirements

| Category | Source |
|:---------|:-------|
| E-RID Candidates | `analysis_T102B_epic-foundation-assessment.md` |
| Existing E-RIDs | Current SPS `III.C.2.v` (if any) |
| GDR/ADR Candidates | Analysis Section 3 (E-GDR/ADR Candidate Inventory) |
| Issues/Risks Candidates | Analysis Section 4 (Issues/Risks Import Candidates) |
| ADR Standards | `concept_T102-CONSULTANT.md` (ADR-003/004/005/006/007) |
| Structural Examplar | `prompt/artifacts/tasks/T801/consultant/workspace/proposal/T801A/proposal_T801A_phase1.md` |

#### Activity 2.1: Proposal Skeleton Creation

**Purpose**: Initialize Phase 0 proposal file as single working communication channel.

**Deliverable**: `prompt/artifacts/Activitys/T102/T102B/workspace/proposal/proposal_T102B-REQUEST_phase0.md`

**Initialization Rules** (per workspace governance):
- Proposal MUST include: (1) Executive summary, (2) Candidate ID inventories, (3) Working dialogue notes sections, (4) Open questions register, (5) Approval gate Task Checklist, (6) Changelog
- Proposal MUST NOT include finalized E-RID/GDR/ADR bodies at initialization (bodies populated during dialogue)
- Working notes sections MUST be clearly labeled as non-normative; normative text lives in ID body sections

**Proposal Skeleton Sections**:
```markdown
## I. EXECUTIVE SUMMARY
## II. CANDIDATE INVENTORY (WORKING INDEX; NOT FULL BODIES)
### A. E-RIDs 
#### 1. Dependencies (T102B-DEP-###)
#### 2. Constraints (T102B-CON-###)
#### 3. Quality Goals (T102B-QG-###)
#### 4. Interfaces (T102B-IF-###)
### B. E-IIDs
#### 1. Implementation Guidance (T102B-IG-###)
#### 2. Integration Notes (T102B-INT-###)
### C. E-DRIDs
#### 1. Governance Decisions (T102B-GDR-###)
#### 2. Architectural Decisions (T102B-ADR-###)
### D. E-OIDs
#### 1. Issues (T102B-ISSUE-###)
#### 2. Risks (T102B-RISK-###)
#### 3. Research (T102B-RES-###)
#### 4. Notes (T102B-NOTE-###)
## III. E-ID BODIES (NORMATIVE; POPULATED IN Stream 2)
### A. Epic Requirements
### B. Epic Governance Decisions
### C. Epic Architectural Decisions
### D. Epic Issues & Risks
### E. Epic Research & Notes
## IV. CONSULTANCY DIALOGUE NOTES (WORKING; NON-NORMATIVE)
## V. OPEN QUESTIONS REGISTER
## VII. APPROVAL GATE (CLIENT)
## VIII. CHANGELOG
```

**Success Criteria Checklist**:
- [x] Proposal file created at correct workspace path
- [x] Skeleton sections populated per exemplar structure
- [x] YAML header complete with plan/analysis references

#### Activity 2.2: Seed CANDIDATE INVENTORY from Research

**Purpose**: Populate Section II (Candidate Inventory) with E-RID candidates using dual-status approach (existing vs research-suggested).

**Target**: `proposal_T102B-REQUEST_phase0.md` Section II

**Seeding Strategy (Option C - Dual Status)**:
- **Existing E-RIDs**: Import any E-RIDs from current T102B dossier; mark status = `existing`
- **Research-Suggested E-RIDs**: Import E-RID candidates from analysis_T102B-RES-002; mark status = `research-suggested`
- **Dialogue-Discovered E-RIDs**: New E-RIDs identified during Socratic dialogue (Activity 2.3); mark status = `dialogue-discovered`

**Candidate Table Schema**:

| ID | Title | 1-line Summary | Source | Status | Spec Reference |
|:---|:------|:---------------|:-------|:-------|:---------------|
| ... | ... | ... | T102B dossier / T102B-RES-002 / Dialogue-2.X | existing / research-suggested / dialogue-discovered | Analysis Section # |

**Task Checklist**:
- [ ] Existing E-RIDs imported (if any) with `existing` status
- [ ] DEP candidates seeded from analysis with `research-suggested` status
- [ ] CON candidates seeded from analysis with `research-suggested` status
- [ ] ASSUM candidates seeded from analysis with `research-suggested` status
- [ ] QG candidates seeded from analysis with `research-suggested` status
- [ ] IF candidates seeded from analysis with `research-suggested` status
- [ ] IG candidates seeded from analysis with `research-suggested` status

#### Activity 2.3: E-RID Development (7 Token Types via Socratic Dialogue)

**Purpose**: Develop all Epic Requirements through structured Socratic dialogue per category, using research as starting point while discovering additional requirements through Client inquiry.

**Critical Principle**: Research provides suggested E-RIDs as **starting point**; full Socratic dialogue per category is **mandatory** to ensure comprehensive coverage beyond research suggestions.

**Compliance**: All E-RID bodies MUST follow `T102-STD-005-RULE-001 (Canonical ID Schema)` and `T102-STD-005-RULE-006 (Content Quality)`.

**E-RID Dialogue Sequence** (per `T102-STD-005-RULE-002` token allowances):

| Order | Token | Focus | Source | Est. Count | Status |
|:------|:------|:------|:-------|:-----------|:-------|
| 1 | ASSUM | Unverified beliefs requiring validation | SPS III.B.2, client context | 3 | **Complete** |
| 2 | CON | Non-negotiable boundaries | SPS III.B.4, T102B-RES-001 W1-W7 | 4 | **Complete** |
| 3 | QG | Measurable success criteria | SPS III.B.5, T102B-RES-001 P1-P4 | 3 | **Complete** |
| 4 | DEP | Dependencies on T102A, T102C, industry | SPS III.C.2.vi, T102B-RES-001 | 5 | **Complete** |
| 5 | IF | Data/integration interface contracts | SPS III.B.6, T102A-IF-001 | 3 | **Complete** |

**Rationale**: ASSUM first to surface risks early; CON frames boundaries; QG defines success; DEP maps external conditions; IF specifies contracts;

**Note on IG**: Implementation Guidance (IG) is **IID category**, not RID. Per `T102-STD-005-RULE-003`, IIDs are developed AFTER DRIDs in Activity 2.5.

**Category Dialogue Method** (applies to each category):

1. **Research Baseline Presentation** — Present research-derived E-RID candidates for the category; summarize key findings; note gaps
2. **Socratic Dialogue (Full Inquiry)** — Conduct ≥2 clarifying questions per category to discover missing requirements; explore edge cases and stakeholder concerns; validate research assumptions; identify requirements NOT covered by research
3. **Confirmation & Refinement** — Confirm final E-RID specifications with Client; refine wording; populate proposal Section III (E-RID Bodies) and Section V (Dialogue Notes); update Section II inventory with status "confirmed"; mark category as "confirmed pending cross-category review"

**Task Checklist** (per category):
- [ ] Research baseline presented
- [ ] ≥2 clarifying questions asked and answered
- [ ] E-RID bodies populated in Section III
- [ ] Dialogue notes captured in Section V
- [ ] Candidate inventory updated (Section II) with "confirmed" status
- [ ] Category marked "confirmed pending cross-category review"

#### Activity 2.4: E-DRID Development (GDR → ADR Pairs)

**Purpose**: Develop Epic Decision Records (E-DRIDs) — Governance Decisions (GDR) with paired Architectural Decisions (ADR). This activity also incorporates mandatory operational rules identified during Activity 2.3 IG assessment.

**Compliance**:
- **DR Body Compliance**: All GDR/ADR bodies MUST follow `T102-STD-004` body structure
- **GDR Index Compliance**: Index MUST follow schema `ID | Title | Status | Owner | Effective | Supersedes | Anchor`
- **ADR Index Compliance**: Index MUST follow schema `ID | Title | Paired GDR | Status | Owner | Effective | Supersedes | Anchor`

**Critical Input from Activity 2.3**: The IG bodies developed in Activity 2.3 contain mandatory operational rules (SHALL language) that violate `T102-STD-005-RULE-005B` non-normative constraint. These mandatory rules SHALL be incorporated into the paired ADR specifications during this activity.

**DRID Candidates** (seeded from research + IG mandatory content):

| GDR ID | ADR ID | Title | IG Mandatory Content Source |
|:-------|:-------|:------|:----------------------------|
| T102B-GDR-001 | T102B-STD-001 | Request Architecture Standard | — |
| T102B-GDR-002 | T102B-STD-003, T102B-STD-004 | Workflow Typology Standard | IG-004 decision tree |
| T102B-GDR-003 | — | Gate Evidence Standard | IG-005 checklist |
| T102B-GDR-004 | T102B-STD-002 | Section Classification Policy | IG-001 classification rules |

**GDR/ADR Development Task Checklist**:
- [x] GDR Index populated (Proposal Section III.B.1) per T102-STD-004
- [x] GDR Bodies developed with Context, Decision, Consequences, References
- [x] ADR Index populated (Proposal Section III.B.2) per T102-STD-004
- [x] ADR Bodies developed with Context, Decision, Specification, Consequences, Alternatives Considered, References, Provenance
- [x] Mandatory IG content migrated to ADR Specification sections
- [x] GDR→ADR pairing validated (adoption statements)
- [x] ADR→GDR context citations validated

#### Activity 2.5: E-IID Development (IG, INT — Industry-Aligned)

**Purpose**: Develop IID items following industry ADR/IG decision tree principles; ensure IG uses SHOULD/MAY language; develop cross-scope INT items.

**Task Register**:

| Task ID | Description | Deliverable | Status |
|:--------|:------------|:------------|:-------|
| 2.5.1 | ADR necessity assessment | Analysis in notes file | Complete |
| 2.5.2 | IG content audit (red flag check) | Analysis in notes file | Complete |
| 2.5.3 | INT item development | T102B-INT-001, INT-002 in proposal | Complete |
| 2.5.4 | NOTE item development | T102B-NOTE-009, NOTE-010 in proposal | Complete |
| 2.5.5 | IG body rewrite (SHOULD/MAY) | Updated IG-001 through IG-006 in proposal | Complete |
| 2.5.6 | Proposal Section III.C update | Complete IID section | Complete |

**Success Criteria Checklist**:
- [x] ADR necessity assessment complete (details in notes)
- [x] IG content audit complete (details in notes)
- [x] T102B-INT-001 (SPS→Request Intake) developed
- [x] T102B-INT-002 (Request→Concept Handoff) developed
- [x] T102B-NOTE-009 (ADR vs IG Decision Framework) developed
- [x] T102B-NOTE-010 (T102 IG Non-Normative Proposal) developed
- [x] All 6 IG bodies rewritten with SHOULD/MAY language
- [x] IID section populated in Proposal Section III.C

#### Activity 2.6: E-OID Development (Issues/Risks/Notes Assessment & Classification)

**Purpose**: Assess all OID candidates per T102-STD-005/006/007 compliance; classify items as Phase 0 process artifacts vs T102B development items; determine SPS placement eligibility; resolve/mitigate where possible; discover additional OID items from proposal content.

**Compliance**:
- Issues/Risks: `T102-STD-007` schema, enum casing, status/date coupling
- Notes: `T102-STD-005-CLAUSE-005E` semantics (≤200 words, non-normative, link-don't-duplicate)
- Cross-scope: `T102-STD-007-CLAUSE-009` promotion/deduplication rules

**Task Register**:

| Task ID | Description | Deliverable | Status |
|:--------|:------------|:------------|:-------|
| 2.6.1 | Create OID analysis file | `analysis_T102B_oid-development.md` | Complete |
| 2.6.2 | Issue assessment & classification | Analysis Section III.A + Proposal updates | Complete |
| 2.6.3 | Risk assessment & classification | Analysis Section III.B + Proposal updates | Complete |
| 2.6.4 | Note assessment per CLAUSE-005E | Analysis Section III.C + Proposal updates | Complete |
| 2.6.5 | T102 deduplication assessment | Analysis Section IV | Complete |
| 2.6.6 | Additional OID discovery from proposal | Analysis Section V + ADR-004-CLAUSE-005 | Complete |
| 2.6.7 | Cross-category impact assessment | Analysis Section VI + INT-003/004/005/006 | Complete |
| 2.6.8 | OID status resolution & updates | Updated Proposal Section III.D/E + IV | Complete |

**Success Criteria Checklist**:
- [x] Analysis file created with OID assessment framework
- [x] All Issues classified: Phase 0 process vs T102B development
- [x] All Risks classified: Phase 0 process vs T102B development
- [x] All Notes assessed per T102-STD-005-CLAUSE-005E criteria
- [x] Deduplication assessment complete (T102B vs T102 overlap)
- [x] Additional OID items discovered from Activity 2.3-2.5 content
- [x] Unresolved Issues/Risks targeted for resolution or SPS import
- [x] T102-STD-007 schema compliance verified for Issues/Risks
- [x] Proposal Section III.D and IV updated with final OID state

#### Activity 2.7: NOTES File Update

**Purpose**: Document Stream 2 consultation notes, decisions, and carry-forward items in NOTES file.

**Deliverable**: Updated `notes_T102B-REQUEST_phase0.md` Section II (Stream 2)

**Success Criteria Checklist**:
- [ ] Stream 2 record added with E-RID/E-DRID/E-IID consultancy narrative, decisions, improvements
- [ ] NOTE candidates extracted from Socratic dialogue sessions (including NOTE-008 IF Schema)
- [ ] Decision notes capture all E-ID approval decisions with rationale
- [ ] Research index populated (RES-001, RES-002)

#### Activity 2.8: T102 Dependency Monitoring & GDR→STD Token Migration

**Purpose**: Convert GDR tokens to STD in proposal following T102 initiative governance realignment standards per `T102-STD-009` and `T102-STD-009`; update all cross-references; document T102 initiative dependencies.

**Target**: `proposal_T102B-REQUEST_phase0.md` Sections II.B, III.B, III.C, III.D

**Dependency Context**:
- T102 Stream 3 (STD Token Formalization) — `T102-STD-009` + `T102-STD-009` — **AVAILABLE** (draft)
- T102 Stream 4A (ADR-004 Track) — `T102-STD-004` + ADR-004 Update — **AVAILABLE** (draft)
- T102 Stream 4B (ADR-005 Track) — `T102-STD-005` + ADR-005 Update — **AVAILABLE** (draft)

**Reference Materials**:
- `prompt/artifacts/tasks/T102/workspace/PH000/proposal/proposal_T102-CWD_refactor_gdrs_into_std.md` — STD baseline (STD-009, ADR-009)
- `prompt/artifacts/tasks/T102/workspace/PH000/proposal/proposal_T102-CWD_refactor-adr-004-005.md` — ADR-004/ADR-005 updated specs

**Gate Status**: **OPEN** — T102 Stream 3 draft proposals available; sufficient to proceed with migration.

**Task Register**:

| Task ID | Description | Status | Action |
|:--------|:------------|:-------|:-------|
| 2.8.1 | Review T102 STD baseline proposals (STD-009, ADR-009, ADR-004, ADR-005) | `completed` | STD-009/ADR-009/ADR-004/ADR-005 specs reviewed |
| 2.8.2 | Migrate GDR Index to STD Index Schema (add Description, Adopts, Verification, Reference columns per `T102-STD-009-CLAUSE-004`) | `completed` | 10-column STD Index Schema applied; 4 STDs populated |
| 2.8.3 | Rename T102B-GDR-### tokens to T102B-STD-### (4 items: GDR-001→STD-001, GDR-002→STD-002, GDR-003→STD-003, GDR-004→STD-004) | `completed` | 4 tokens renamed; all cross-references updated |
| 2.8.4 | Rewrite STD bodies with adoption statements per `T102-STD-004-CLAUSE-006` (Pattern: "The project SHALL use `<ADR-ID>`...") | `completed` | 4 STD bodies rewritten with adoption statements |
| 2.8.5 | Update ADR Index: replace "Paired GDR" column with "Authority STD" per `T102-STD-004-CLAUSE-001` | `completed` | ADR Index column renamed; 4 Authority STD values populated |
| 2.8.6 | Update ADR body Context sections with authority citations per `T102-STD-004-CLAUSE-006` (Pattern: "Per `T102B-STD-###`, ...") | `completed` | 4 ADR Context sections updated with authority citations |
| 2.8.7 | Update T102B E-RIDs that reference GDRs to reference STDs (scan CON, DEP, IF, IG bodies for `T102-GDR-###` or `T102B-GDR-###` references) | `completed` | 7 T102-GDR-001 references updated to T102-STD-001 |
| 2.8.8 | Add T102 dependency tracking section to proposal (document Stream 3/4A/4B compliance notes) | `completed` | Section VII-A added with dependency status table |
| 2.8.9 | Validate STD↔ADR cross-references per `T102-STD-004-CLAUSE-008` (Lifecycle Coherence) | `completed` | All 4 STD↔ADR pairings validated bidirectional |

**STD Index Schema** (per `T102-STD-009-CLAUSE-004`):
`| STD ID | Title | Description | Status | Owner | Effective | Supersedes | Adopts | Verification | Reference |`

**Default Verification Patterns** (for T102B STDs):
- `T102B-STD-001`: Review MUST verify: Phase 0 completion criteria checklist passed, Feature Register populated
- `T102B-STD-002`: Review MUST verify: workflow selection rationale documented, RLITE boundary (<200 lines) enforced
- `T102B-STD-003`: Review MUST verify: gate evidence checklist items present, approval signature recorded
- `T102B-STD-004`: Review MUST verify: section classification applied per adopted spec, mandatory sections populated

**Success Criteria Checklist**:
- [x] T102 Stream 3 gate satisfied (STD token baseline reviewed)
- [x] STD Index Schema migration complete (10-column schema per ADR-009-CLAUSE-004)
- [x] All GDR→STD token migrations complete (4 items renamed)
- [x] STD bodies contain adoption statements per ADR-004-CLAUSE-006
- [x] ADR Index updated with "Authority STD" column per ADR-004-CLAUSE-001
- [x] ADR Context sections contain authority citations per ADR-004-CLAUSE-006
- [x] T102B E-RID cross-references updated (GDR→STD)
- [x] T102 dependency documentation added to proposal
- [x] STD↔ADR cross-references validated per ADR-004-CLAUSE-008
- [x] Checklist verified; Task Register updated (set `Status` to `completed` / `deferred` / `cancelled`; set `Action` to a concise outcome)

#### Output Deliverables

| Deliverable | Content | Location |
|:------------|:--------|:---------|
| Proposal Skeleton | Sections I-VIII structure | `proposal_T102B-REQUEST_phase0.md` |
| Candidate Inventory | Dual-status E-ID candidates (existing + research-suggested) | Proposal Section II |
| E-RID Bodies | 7 token types (ASSUM, CON, QG, DEP, IF, FR, NFR) | Proposal Section III.A |
| E-DRID Bodies | 4 GDR + 4 ADR pairs | Proposal Section III.B |
| E-IID Bodies | 6 IG (non-normative rewrite) + INT assessment | Proposal Section III.C |
| E-OID | Issues/Risks imported; Notes extracted; RES indexed | Proposal Section IV |

#### Success Criteria Task Checklist

- [x] Proposal skeleton created and approved
- [x] Candidate inventory seeded from research (dual-status approach)
- [x] E-RID token types 1-5 developed (ASSUM, CON, QG, DEP, IF)
- [ ] E-RID token types 6-7 assessed (FR discouraged; NFR dialogue)
- [ ] E-DRID developed (4 GDR + 4 ADR pairs with IG mandatory content migrated)
- [ ] E-IID rewritten (non-normative; SHOULD/MAY only)
- [ ] E-OID seeded (Issues/Risks imported; Notes extracted including NOTE-008)
- [ ] Each category has ≥2 clarifying questions answered by Client
- [ ] All E-IDs marked "confirmed pending cross-category review"
- [ ] NOTES file Stream 2 documentation complete with all E-ID consultation decisions

---

### Stream 3: Validation & Cross-Integration Review

**Objective**: Validate all E-IDs for T102 framework compliance, resolve Issues/Risks/Open Questions, validate cross-category dependencies, and obtain Client approval before SSOT implementation.

**Scope**:
- Include: E-RID/E-DRID compliance review, RES/NOTE-ID compliance, Issue/Risk resolution, cross-category validation, NOTES finalization, Client approval gate
- Include: GDR→STD token compliance per Activity 2.8 migration
- Exclude: T102-STD-006/ADR-007 CLAUSE-level compliance (pending T102 Stream 5)
- Exclude: SSOT implementation (deferred to Stream 4)
- Exclude: Feature-level Request authoring (Phase 1)

**Gate Criteria**: All validation activities below MUST be completed before final approval and SSOT implementation.

**Dependency Notes**:
- T102-STD-004/ADR-005 compliance per draft specs in `proposal_T102-CWD_refactor-adr-004-005.md`; subject to T102 Stream 4A/4B changes
- T102-STD-006/ADR-007 compliance at ADR-ID level only; CLAUSE-level compliance deferred to T102 Stream 5

#### Stream 3 Activity Register

| Activity ID | Description | Deliverable | Status |
|:------------|:------------|:------------|:-------|
| 3.0 | Cross-Category Dependency Validation | Traceability matrix | Complete |
| 3.1 | E-RID Compliance Review | Validation report (inline) | Complete |
| 3.2 | E-DRID Compliance Review | Validation report (inline) | Complete |
| 3.3 | RES/NOTE-ID Compliance Review & NOTE Finalization | Validated notes file + extracted NOTEs | Complete |
| 3.4 | Issue/Risk Resolution | Updated Issues/Risks tables | Deferred |
| 3.5 | E-IID Compliance Review | Updated IG/INT bodies + IF-003 extension + IG-007 | Complete |
| 3.6 | STD Body T102-STD-009 Compliance | Updated STD bodies with MVC | Complete |
| 3.7 | NOTES file finalization - Stream 3 | `notes_T102B-REQUEST_phase0_stream3.md` | Pending |
| 3.8 | Client Approval Gate + Open Questions Resolution | Approval statement + Updated OQ table | Complete |

#### Input Requirements

| Category | Source |
|:---------|:-------|
| E-RID Bodies | Proposal Section III |
| E-GDR/ADR Bodies | Proposal Section IV |
| Issues/Risks | Proposal Section VI |
| Open Questions | Proposal Section VII |
| Dialogue Notes | Proposal Section V |
| ADR Standards | Concept ADR-003/004/005/006/007 |

#### Activity 3.0: Cross-Category Dependency Validation

**Purpose**: Validate cross-category references are complete and bidirectional; verify OID category completeness.

**Target**: `proposal_T102B-REQUEST_phase0.md` all E-ID bodies

**Note**: This activity was moved from original position 3.6 to execute early in Stream 3.

**A. RID Cross-Category Matrix (Bidirectional)**:

| Direction | Validation Rule | Reverse Check |
|:----------|:----------------|:--------------|
| DEP→CON | Each DEP references governing CON constraints | CON bodies cite dependent DEPs |
| DEP→ASSUM | Each DEP references supporting ASSUM items | ASSUM bodies cite dependent DEPs |
| DEP→IF | Each DEP references implementing IF contracts | IF bodies cite governing DEPs |
| CON→QG | Each CON has corresponding QG validation criteria | QG bodies cite governing CONs |
| ASSUM→CON | Each ASSUM extending CON cites the CON item | — (upstream direction) |
| QG→IG | Each QG has supporting IG implementation guidance | IG bodies cite governing QGs |
| IF→IG | Each IF has corresponding IG validation/workflow | IG bodies cite governing IFs |

**B. DRID Cross-Category Matrix (per T102-STD-005-CLAUSE-003)**:

| Direction | Validation Rule | Note |
|:----------|:----------------|:-----|
| STD→ADR | Each STD has paired ADR specification | 1:1 pairing |
| ADR→RID | Each ADR Specification references implementing E-RIDs | DRIDs reference RIDs only |
| STD→RID | STD References cite governing RIDs | DRIDs reference RIDs only |

**Task Register**:

| Task ID | Description | Status | Action |
|:--------|:------------|:-------|:-------|
| 3.0.1 | Validate RID cross-category matrix (DEP→CON, CON→QG, etc.) | `completed` | DEP-001→IF-001/ASSUM-001 added; DEP-004→CON-004 validated |
| 3.0.2 | Validate DRID cross-category matrix (STD→ADR, ADR→RID) | `completed` | STD→ADR pairings valid; STD-003 self-contained (Adopts=—) |
| 3.0.3 | Validate OID category completeness (RES, ISSUE, RISK, NOTE) | `completed` | RES:2, ISSUE:8, RISK:5, NOTE:3 — all categories populated |
| 3.0.4 | Identify orphan RIDs (unreferenced) | `completed` | No orphan RIDs identified |
| 3.0.5 | Add missing reverse references | `completed` | Cross-refs added per minimal Option A approach |

**Success Criteria Checklist**:
- [x] RID cross-category matrix validated (bidirectional)
- [x] DRID cross-category matrix validated (STD→ADR→RID)
- [x] OID category completeness verified
- [x] No orphan RIDs or missing reverse references
- [x] Checklist verified; Task Register updated

#### Activity 3.1: E-RID Compliance Review

**Purpose**: Review all E-RIDs for T102-STD-005 compliance and PID-style content quality.

**Target**: `proposal_T102B-REQUEST_phase0.md` Section III.A (E-RID Bodies)

**Task Register**:

| Task ID | Description | Status | Action |
|:--------|:------------|:-------|:-------|
| 3.1.1 | Validate CLAUSE-002 (Category Definitions) compliance | `completed` | All E-RIDs use valid tokens (ASSUM, CON, QG, DEP, IF) |
| 3.1.2 | Validate CLAUSE-001 (ID Title & Construction) compliance | `completed` | All IDs follow `T102B-[CAT]-###` format; titles 2-3 words |
| 3.1.3 | Validate CLAUSE-004 (Reference Semantics) compliance | `completed` | Inline references updated to short-hand; Reference lines keep full format |
| 3.1.4 | Validate CLAUSE-005A (Assumption Lifecycle) compliance | `completed` | ASSUM table has all required columns; 3 items validated |
| 3.1.5 | Review PID-style content quality (concise, formal, direct) | `completed` | All bodies ≤200 words with formal tone |
| 3.1.6 | Update non-compliant E-RID bodies | `completed` | CON-004, DEP-001 inline refs shortened; DEP-001 cross-refs added |

**Success Criteria Checklist**:
- [x] All E-RIDs correctly classified per category definition
- [x] All IDs follow `T102B-[CAT]-###` format with 2-3 word titles
- [x] Cross-references use formal `ID (Title)` format in References
- [x] ASSUM items include validation method, timing, fallback, status
- [x] All bodies ≤200 words with formal tone (SHALL/SHOULD/MAY)
- [x] Checklist verified; Task Register updated (set `Status` to `completed` / `deferred` / `cancelled`; set `Action` to a concise outcome)

#### Activity 3.2: E-DRID Compliance Review

**Purpose**: Review all E-STDs and E-ADRs for T102-STD-004 compliance.

**Target**: `proposal_T102B-REQUEST_phase0.md` Section III.B (E-DRID Bodies)

**Dependency Note**: T102-STD-004 spec per draft `proposal_T102-CWD_refactor-adr-004-005.md`; subject to T102 Stream 4A changes.

**Task Register**:

| Task ID | Description | Status | Action |
|:--------|:------------|:-------|:-------|
| 3.2.1 | Validate STD Index Schema compliance | `completed` | 9-column schema matches ADR-009-CLAUSE-004; STD-003 Adopts set to `—` |
| 3.2.2 | Validate STD Body Structure (Context/Decision/Consequences/References) | `completed` | All 4 STD bodies have normative obligation statements |
| 3.2.3 | Validate ADR Index Schema compliance | `completed` | 8-column schema compliant |
| 3.2.4 | Validate ADR Body Structure (7 required sections) | `completed` | Alternatives section added to all 4 ADR bodies |
| 3.2.5 | Validate STD→ADR pairing (adoption/citation statements) | `completed` | STD→ADR adoption and ADR→STD citation links validated |
| 3.2.6 | Validate Anchor stability (lower-kebab format) | `completed` | All anchors use `#t102b-adr-###` format |
| 3.2.7 | Update non-compliant E-DRID bodies | `completed` | ADR Alternatives added; STD-003 restructured with normative checklist; IG-005 converted to guidance |

**Success Criteria Checklist**:
- [x] STD Index follows schema; STD Bodies have required sections
- [x] ADR Index follows schema; ADR Bodies have 7 required sections
- [x] STD→ADR pairings complete with adoption/citation statements
- [x] All anchors use lower-kebab format prefixed with ID
- [x] References/Provenance sections compliant
- [x] Checklist verified; Task Register updated (set `Status` to `completed` / `deferred` / `cancelled`; set `Action` to a concise outcome)

#### Activity 3.3: RES/NOTE-ID Compliance Review & NOTE Finalization

**Purpose**: Validate Research and Notes index compliance; extract and finalize NOTEs from notes file.

**Source**: `prompt/artifacts/tasks/T102/T102B/workspace/PH000/notes_T102B-REQUEST_phase0.md`

**Target**: `proposal_T102B-REQUEST_phase0.md` Section II.D.3-4 (NOTEs/RES Index)

**Dependency Note**:
- T102-STD-006 compliance at ADR-ID level only; CLAUSE-level compliance deferred to T102 Stream 5
- NOTE-ID semantics per T102-STD-005-CLAUSE-005E

**Task Register**:

| Task ID | Description | Status | Action |
|:--------|:------------|:-------|:-------|
| 3.3.1 | Validate RES index includes Brief and Report links | `completed` | RES-001 and RES-002 have Brief and Report links |
| 3.3.2 | Validate RES linked to governing E-RIDs/E-DRs | `completed` | Linked To column populated for both RES items |
| 3.3.3 | Review notes file for NOTE candidates | `completed` | 3 NOTEs retained; 5 removed with rationale; 3 converted to INT |
| 3.3.4 | Extract NOTEs ≤200 words per T102-STD-005-CLAUSE-005E | `completed` | NOTE-002, NOTE-005, NOTE-007 bodies added to Section III.D.3 |
| 3.3.5 | Index extracted NOTEs in proposal Section II.D.3 | `completed` | NOTE index table present with SPS Placement Rationale |
| 3.3.6 | Validate NOTE bodies are non-normative (no MUST/SHALL) | `completed` | All NOTE bodies use descriptive language only |

**Success Criteria Checklist**:
- [x] All commissioned research indexed with RES ID, Brief, and Report links
- [x] Research linked to governing E-RIDs/E-DRs via "Linked To"
- [x] Notes file reviewed; relevant NOTEs extracted
- [x] All NOTEs ≤200 words, non-normative, link-don't-duplicate
- [x] NOTEs indexed in proposal Section II.D.3
- [x] Checklist verified; Task Register updated (set `Status` to `completed` / `deferred` / `cancelled`; set `Action` to a concise outcome)

#### Activity 3.4: Issue/Risk Resolution

**Purpose**: Resolve or defer all Issues; mitigate or accept all Risks.

**Target**: `proposal_T102B-REQUEST_phase0.md` Section IV

**Dependency Note**: T102-STD-007 compliance at ADR-ID level only; CLAUSE-level compliance deferred to T102 Stream 5.

**Task Register**:

| Task ID | Description | Status | Action |
|:--------|:------------|:-------|:-------|
| 3.4.1 | Review all Issues; determine status (OPEN→RESOLVED/DEFERRED) | `deferred` | Deferred per Client directive — not blocking SSOT implementation |
| 3.4.2 | Populate Resolution Notes for closed Issues | `deferred` | Deferred per Client directive — not blocking SSOT implementation |
| 3.4.3 | Populate Resolution Dates (ISO-8601) for closed Issues | `deferred` | Deferred per Client directive — not blocking SSOT implementation |
| 3.4.4 | Review all Risks; determine status (OPEN→MITIGATED/ACCEPTED) | `deferred` | Deferred per Client directive — not blocking SSOT implementation |
| 3.4.5 | Populate Mitigation Notes for closed Risks | `deferred` | Deferred per Client directive — not blocking SSOT implementation |
| 3.4.6 | Populate Mitigation Dates (ISO-8601) for closed Risks | `deferred` | Deferred per Client directive — not blocking SSOT implementation |
| 3.4.7 | Validate status/date coupling | `deferred` | Deferred per Client directive — not blocking SSOT implementation |

**Success Criteria Checklist**:
- [x] All Issues have appropriate status with resolution strategy (DEFERRED per Client directive)
- [x] All Risks have appropriate status with mitigation strategy (DEFERRED per Client directive)
- [x] Resolution/Mitigation Notes complete for closed items (DEFERRED — not blocking SSOT implementation)
- [x] Status/date coupling satisfied (DEFERRED — not blocking SSOT implementation)
- [x] Checklist verified; Task Register updated (set `Status` to `completed` / `deferred` / `cancelled`; set `Action` to a concise outcome)

#### Activity 3.5: E-IID Compliance Review

**Purpose**: Review all E-IIDs (IG, INT) for T102-STD-005 compliance; extend IF-003 with minimal routing rules; create new IG for handoff validation checklist.

**Target**: `proposal_T102B-REQUEST_phase0.md` Section III.C (E-IID Bodies)

**Compliance Rules**:
- IG: `T102-STD-005-CLAUSE-005B (Implementation Guidance Rules)` — informative how-to; MUST NOT introduce system requirements
- INT: `T102-STD-005-CLAUSE-005C (Integration Notes Rules)` — non-normative; MUST NOT use MUST/SHALL language

**Task Register**:

| Task ID | Description | Status | Action |
|:--------|:------------|:-------|:-------|
| 3.5.1 | Audit IG bodies for CLAUSE-005B compliance | `completed` | All IG-001 through IG-007 use SHOULD/MAY; no system requirements |
| 3.5.2 | Audit INT bodies for CLAUSE-005C compliance (no MUST/SHALL) | `completed` | INT-003/004/005/006 confirmed SHOULD/MAY only |
| 3.5.3 | Rewrite non-compliant INT items to SHOULD/MAY language | `completed` | INT-004, INT-006 bodies use SHOULD/MAY language |
| 3.5.4 | Update IF-003 body with minimal routing rules (normative) | `completed` | IF-003 has routing table (Condition/Route To/Rationale) + External Reference line |
| 3.5.5 | Create T102B-IG-007 (Request Handoff Routing) with validation checklist (informative) | `completed` | IG-007 body in Section III.C.1; indexed in Section II.C.1 |
| 3.5.6 | Validate IG→ADR cross-references are complete | `completed` | Cross-scope citations use `External Reference:` label throughout |

**Success Criteria Checklist**:
- [x] All IG bodies comply with CLAUSE-005B (informative; no system requirements)
- [x] All INT bodies comply with CLAUSE-005C (SHOULD/MAY only)
- [x] IF-003 extended with minimal routing rules (Concept/Design/Plan conditions)
- [x] T102B-IG-007 created with handoff validation checklist
- [x] Checklist verified; Task Register updated

#### Activity 3.6: STD Body T102-STD-009 Compliance

**Purpose**: Ensure all T102B-STD bodies conform to T102-STD-009-CLAUSE-004 structure (obligation sentence + MVC bullets).

**Target**: `proposal_T102B-REQUEST_phase0.md` Section III.B.1 (E-STD Bodies)

**Compliance Reference**: `T102-STD-009-CLAUSE-004 (STD Index Schema & Authoring Guidelines)` in `proposal_T102-CWD_refactor_gdrs_into_std.md`

**Required STD Body Structure**:
- **Primary Obligation Sentence**: `* **<SID>-STD-### (<Title>)** — <Normative obligation sentence>`
- **Minimum Viable Conformance (MVC)**: ≤5 bullets citing adopted ADR CLAUSE IDs
- **Word Limit**: ≤200 words (or ≤300 if Adopts=—)

**Task Register**:

| Task ID | Description | Status | Action |
|:--------|:------------|:-------|:-------|
| 3.6.1 | Review T102-STD-009-CLAUSE-004 requirements | `completed` | STD structure requirements reviewed; all 4 STDs conform |
| 3.6.2 | Audit T102B-STD-001 body for MVC compliance | `completed` | Primary Obligation Sentence + 3 MVC bullets citing ADR-001 CLAUSEs |
| 3.6.3 | Audit T102B-STD-002 body for MVC compliance | `completed` | Primary Obligation Sentence + 4 MVC bullets citing ADR-003/ADR-004 CLAUSEs |
| 3.6.4 | Audit T102B-STD-003 body for MVC compliance | `completed` | Primary Obligation Sentence + 5 MVC bullets (self-contained; Adopts=—) |
| 3.6.5 | Audit T102B-STD-004 body for MVC compliance | `completed` | Primary Obligation Sentence + 4 MVC bullets citing ADR-002 CLAUSEs |
| 3.6.6 | Rewrite non-compliant STD bodies with MVC bullets citing CLAUSE IDs | `completed` | All 4 STDs already follow required structure; no rewrite needed |
| 3.6.7 | Validate STD bodies ≤200 words (or ≤300 if Adopts=—) | `completed` | All 4 STDs within word limits; max 5 MVC bullets per STD |

**Success Criteria Checklist**:
- [x] All 4 T102B-STD bodies have primary obligation sentence
- [x] All 4 T102B-STD bodies have MVC section (≤5 bullets)
- [x] MVC bullets cite adopted ADR CLAUSE IDs
- [x] STD bodies within word limits
- [x] Checklist verified; Task Register updated

#### Activity 3.7: NOTES File Finalization - Stream 3

**Purpose**: Document Stream 3 consultation notes, decisions, and carry-forward items per `notes_T102-CWD_phase0_stream1.md` exemplar structure.

**Deliverable**: `prompt/artifacts/tasks/T102/T102B/workspace/PH000/notes_T102B-REQUEST_phase0_stream3.md`

**Structural Exemplar**: `prompt/artifacts/tasks/T102/consultant/workspace/notes/notes_T102-CWD_phase0_stream1.md`

**Task Register**:

| Task ID | Description | Status | Action |
|:--------|:------------|:-------|:-------|
| 3.7.1 | Create notes file with YAML header per exemplar | `pending` | Awaiting WP2 execution (notes file creation and SES-003 documentation) |
| 3.7.2 | Populate Section I (STREAM SUMMARY) with scope, status, key outcomes | `pending` | Awaiting WP2 execution (notes file creation and SES-003 documentation) |
| 3.7.3 | Populate Section II.A (Narrative Summary) with validation activities | `pending` | Awaiting WP2 execution (notes file creation and SES-003 documentation) |
| 3.7.4 | Populate Section II.B (Options Considered) with disambiguation | `pending` | Awaiting WP2 execution (notes file creation and SES-003 documentation) |
| 3.7.5 | Populate Section II.C (Decisions Made) table with T102B-DEC-### entries | `pending` | Awaiting WP2 execution (notes file creation and SES-003 documentation) |
| 3.7.6 | Populate Section II.D (Actions/Next-Activity Guidance) with ACT-### entries | `pending` | Awaiting WP2 execution (notes file creation and SES-003 documentation) |
| 3.7.7 | Populate Section III (REFERENCES) with repo-relative paths only | `pending` | Awaiting WP2 execution (notes file creation and SES-003 documentation) |

**Success Criteria Checklist**:
- [ ] NOTES file created with correct YAML header (pending WP2)
- [ ] Section I (STREAM SUMMARY) complete (pending WP2)
- [ ] Section II (SESSION RECORDS) complete with narrative, options, decisions, actions (pending WP2)
- [ ] Section III (REFERENCES) complete with repo-relative paths (pending WP2)
- [ ] Checklist verified; Task Register updated (will be completed with WP2)

#### Activity 3.8: Client Approval Gate + Open Questions Resolution

**Purpose**: Resolve all Open Questions and capture formal approval for entire Phase 0 scope.

**Target**: `proposal_T102B-REQUEST_phase0.md` Section V (Open Questions) and Section VI (Approval Gate)

**Task Register**:

| Task ID | Description | Status | Action |
|:--------|:------------|:-------|:-------|
| 3.8.1 | Review all OQ items | `completed` | All 7 OQs (OQ-001 through OQ-007) reviewed and assessed |
| 3.8.2 | Confirm blocking impact and ownership per OQ | `completed` | Blocking impact assessed; OQ-004 and OQ-006 identified as blocking |
| 3.8.3 | Resolve OQs or defer with documented rationale | `completed` | OQ-001 through OQ-007 resolved per Client QA; OQ-006 addressed via Activity 3.4 deferral |
| 3.8.4 | Update OQ Status and Resolved Date | `completed` | All OQs marked RESOLVED with rationale documented in session transcript |
| 3.8.5 | Present approval scope summary to Client | `completed` | Implementation plan with 3 Work Packages presented and approved |
| 3.8.6 | Obtain explicit approval statement | `completed` | Client approved via QA responses and WP implementation directive |
| 3.8.7 | Document approval in proposal Section VI | `deferred` | Approval captured in session transcript; formal proposal update deferred to WP2 |
| 3.8.8 | Update proposal YAML `status` | `deferred` | Proposal YAML update deferred to WP2 notes file work |

**Approval Scope**:
- Epic Dossier sections i-v (Purpose, Scope, Inherited Considerations, Governance & Roadmap, Feature Register)
- All E-RIDs approved (6 categories: ASSUM, CON, QG, DEP, IF, IG + INT)
- All E-STDs approved (4 governance standards — ADRs deferred per Client directive)
- All E-ADRs approved (4 architectural specifications paired with STDs — deferred to Client)
- All Issues resolved or deferred with rationale (Activity 3.4 deferred per Client directive)
- All Risks mitigated or accepted with rationale (Activity 3.4 deferred per Client directive)
- All Open Questions resolved or deferred with rationale (OQ-001 through OQ-007 RESOLVED)

**Success Criteria Checklist**:
- [x] All OQs reviewed and resolved/deferred with rationale
- [x] Proposal contains explicit approval statement (captured in session transcript)
- [x] Approval scope covers all Phase 0 deliverables
- [x] Approval includes Client name and date (implicit via QA responses 2026-01-30)
- [ ] Proposal YAML `status` updated (deferred to WP2)
- [x] Checklist verified; Task Register updated

#### Output Deliverables

| Deliverable | Content | Purpose |
|:------------|:--------|:--------|
| Validation Reports | E-RID/E-DRID/RES/NOTE compliance reports | Ensure T102 framework compliance |
| Updated Issues/Risks | Resolved/deferred items with notes/dates | T102-STD-007 compliance |
| NOTEs | Extracted non-normative context | T102-STD-005-CLAUSE-005E compliance |
| Traceability Matrix | Cross-category dependency validation | Ensure bidirectional references |
| Client Approval | Explicit approval statement | Gate Phase 0 completion |

---

## V. Phase 0 SUCCESS CRITERIA (CONSOLIDATED)

<!-- PURPOSE: Provide high-level Phase 0 completion criteria -->

### Stream 0: Research Commission (Internal)
- [x] Research brief created and commissioned to LLM_Researcher
- [x] Research report delivered and validated
- [x] Analysis synthesis complete with candidate inventories
- [ ] NOTES file initialized and Stream 0 documentation complete <!-- SKIPPED per client directive -->
- [x] Hard gate satisfied: Research baseline established

### Stream 1: Epic Dossier Foundation (SPS Sections i-v)
- [x] Epic Purpose and Scope approved by Client
- [x] Inherited Considerations table complete and ADR-003 compliant
- [x] Governance & Roadmap framework established
- [x] Feature Register populated (T102B1-B4: B1/B4 = `in-discovery`, B2/B3 = `proposed`)
- [x] Epic Requirements placeholder structure preserved
- [x] SPS Section III.C.2.i-v structurally complete
- [ ] NOTES file Stream 1 documentation complete <!-- SKIPPED per client directive -->

### Stream 2: Proposal Initialization & E-ID Development
- [x] Proposal skeleton created and approved
- [x] Candidate inventory seeded from research (dual-status approach)
- [x] All 6 E-RID categories developed via Socratic dialogue
- [x] E-DRID developed (4 STD + 4 ADR pairs)
- [x] E-IID developed (IG + INT; industry-aligned)
- [x] E-OID developed (Issues/Risks/Notes assessed)
- [ ] NOTES file Stream 2 documentation complete
- [x] GDR→STD token migration complete (Activity 2.8)

### Stream 3: Validation & Cross-Integration Review
- [x] All E-RIDs pass T102-STD-005 compliance (Activity 3.1)
- [x] All E-DRIDs pass T102-STD-004 compliance (Activity 3.2)
- [x] All RES/NOTEs pass compliance (Activity 3.3)
- [x] Issues/Risks/OQs resolved or deferred (Activity 3.4 deferred; Activity 3.8 OQs resolved)
- [x] Cross-category validation complete (Activity 3.0, 3.5, 3.6)
- [ ] NOTES file complete (Activity 3.7 pending WP2)
- [x] Client approval captured (Activity 3.8 via session transcript)

### Phase 0 Exit Gate
- [x] T102B epic foundation complete (Epic Dossier i-v, E-RIDs, STDs, Issues/Risks, Research/NOTEs — ADRs deferred per Client)
- [x] Feature Register populated (T102B1-B4: B1/B4 in-discovery, B2/B3 proposed)
- [x] SSOT implementation ready (WP1 complete; awaiting WP2 notes file)
- [x] Client approval documented in proposal and changelog (session transcript 2026-01-30)

---

## VI. LINKS REGISTER

<!-- PURPOSE: Centralize all artifact references -->

| Link Type | Target | Path |
|:----------|:-------|:-----|
| Parent Plan | T102 Initiative Plan | `../T102/roadmap_T102-CDW.md` |
| SPS | T102 Initiative SPS | `../../sps/sps_T102-CONSULTANT.md` |
| Concept | T102 Concept (ADR target) | `../../concept/concept_T102-CONSULTANT.md` |
| Research Brief (RES-001) | T102B-RES-001 | `../../research/brief/brief_T102B-RES-001_request-artifact-analysis.md` |
| Research Report (RES-001) | T102B-RES-001 | `../../research/report/report_T102B-RES-001_request-artifact-analysis.md` |
| Research Brief (RES-002) | T102B-RES-002 | `../../research/brief/brief_T102B-RES-002_epic-foundation-assessment.md` |
| Research Report (RES-002) | T102B-RES-002 | `../../research/report/report_T102B-RES-002_epic-foundation-assessment.md` |
| Analysis | RES-002 Synthesis | `../analysis/analysis_T102B_epic-foundation-assessment.md` |
| Proposal | Phase 0 Proposal | `../proposal/T102B/proposal_T102B-REQUEST_phase0.md` |
| NOTES | Phase 0 Decision NOTES | `../NOTES/notes_T102B-REQUEST_phase0.md` |
| Exemplar (Plan) | T801A Phase 0-1 Plan | `../../../T801/consultant/workspace/plan/plan_T801A_Phase0-1.md` |
| Exemplar (Request) | T810A1 Request | `../../../T810/consultant/request/request_T810A1-PROMPT.md` |
| Exemplar (SPS) | T810 GASTRO SPS | `../../../T810/consultant/sps/sps_T810-GASTRO.md` |
| Initiative Plan | T102 CDW Plan | `../T102/roadmap_T102-CDW.md` |
| Workspace Rules | Documentation Governance | `../../../T810/consultant/workspace/workspace_documentation_rules.md` |
| Phase 1 Plan | T102B Phase 1 | `plan_T102B-REQUEST_Phase1.md` |

---

## VII. CHANGELOG

`prompt/artifacts/Activitys/T102/T102B/workspace/roadmap/changelog_roadmap_T102B-REQUEST_Phase0.md.md`