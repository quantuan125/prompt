---
artifact_type: 'PLAN'
initiative_id: 'T901'
epic_id: 'T903A'
epic_code: 'CONV'
version: '1.0.0'
date: '2026-01-11'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
---

# CONSULTANCY PLAN: `T903A` Epic Foundation Establishment (`CONV`)

## I. EXECUTIVE SUMMARY

This plan defines the consultancy workflow to establish a **governance foundation** for Epic `T903A (CONV)` — Conversation Constructor — bringing it into alignment with the T801 governance exemplar standard.

**Primary Deliverable**: SSOT governance file `sps_T901-TOOLS_v1.0.0.md` with Epic `T903A` dossier

**Role Boundary**
- `LLM_Consultant`: requirements analysis, governance mapping, material organization, approval gates
- `LLM_Developer`: SSOT implementation and any codebase work (post-approval)
- `Client`: decision owner and approval authority

**Phase 0 Objectives**
1. Establish proper directory structure per T801 exemplar
2. Create SPS governance file with T903A epic dossier
3. Organize and document all existing materials
4. Map existing technical phases to governance roadmap
5. Prepare foundation for Phase 1 (E-RID development)

---

## II. CONTEXT MATERIALS & PREREQUISITES

### A. Required Reading Before Phase 0 Execution

**External Initiative Governance**:
- `prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md` — Initiative-wide Governance for Development & Planning
- `prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md` — Initiative-wide Architectural Framework for Implementation

**Structural Exemplars** (T801 as reference):
- `prompt/artifacts/tasks/T801/consultant/sps/sps_T801-TRADER.md` — SPS structure and Epic dossier pattern
- `prompt/artifacts/tasks/T801/consultant/workspace/plan/plan_T801A_phase0-1.md` — Plan structure exemplar

**Current T903 Materials**:
- `prompt/artifacts/tasks/T903/T903B_i2.md` — Current technical implementation status
- `prompt/artifacts/tasks/T903/consultant/workspace/analysis/analysis_T903A-CONV_initiative-status-research.md` — Status analysis

**Implementation Artifacts**:
- `prompt/scripts/conversation_reconstructor.py` — Main script
- `prompt/scripts/conversation_parsers/` — Parser architecture
- `prompt/documentation/scripts/tools/conversation_constructor_guide.md` — User documentation

### B. Working Assumptions

1. **Initiative Hierarchy**: T903A operates under Initiative T901 (TOOLS) as parent initiative
2. **Technical Progress**: ~60-70% technical implementation complete; governance foundation missing
3. **Backward Compatibility**: Existing technical artifacts preserved; governance layer added
4. **Client Decision Authority**: All governance decisions require explicit Client approval

### C. Role Boundaries

**LLM_Consultant Responsibilities (Phase 0)**:
| Scope | Description | Example |
|:------|:------------|:--------|
| **Directory Organization** | Create compliant folder structure | `consultant/workspace/plan/` |
| **Material Migration** | Move existing files to proper locations | `T903B_i2.md` → `plan/` |
| **SPS Drafting** | Draft initiative/epic governance structure | Feature Register, Phase Roadmap |
| **Gap Analysis** | Document what's needed for Phase 1 | E-RID placeholders |

**LLM_Developer Responsibilities (Post-Approval)**:
| Scope | Description | Example |
|:------|:------------|:--------|
| **SSOT Implementation** | Insert approved content into governance files | SPS population |
| **Technical Migration** | Test location changes (if approved) | `tests/` → `prompt/tests/` |

---

## III. PHASE 0: GOVERNANCE FOUNDATION ESTABLISHMENT

**Objective**: Create proper governance structure for T903A (CONV) epic so downstream phases can proceed with traceable requirements and decisions.

**Constraint**: Phase 0 MUST NOT make technical implementation changes; governance layer only.

### Planned Activities

---

#### Activity 0.1: Directory Structure Creation

**Purpose**: Establish T801-compliant directory hierarchy for T903 governance artifacts.

**Target**: `prompt/artifacts/tasks/T903/`

**Task List**:

##### Task 0.1.1: Create Governance Directories
- [x] Create `consultant/sps/` for SPS governance file
- [x] Create `consultant/concept/` for future ADR compendium
- [x] Create `consultant/workspace/plan/` for phase plans
- [x] Create `consultant/workspace/analysis/` for analysis files

##### Task 0.1.2: Create Supporting Directories
- [ ] Create `consultant/workspace/proposal/` for future proposals
- [ ] Create `research/brief/` for future research briefs
- [ ] Create `research/report/` for future research reports
- [ ] Create `raw/` for archived/raw conversation exports

**Success Criteria Checklist**:
- [x] `consultant/sps/` directory exists
- [x] `consultant/workspace/plan/` directory exists
- [x] `consultant/workspace/analysis/` directory exists
- [ ] All directories follow T801 exemplar pattern

---

#### Activity 0.2: Material Organization

**Purpose**: Migrate existing T903 artifacts to compliant locations and establish archive for original files.

**Target**: `prompt/artifacts/tasks/T903/`

**Task List**:

##### Task 0.2.1: Archive Original Task Files
- [ ] Move `T903A.md` to `raw/T903A_original.md`
- [ ] Move `T903B.md` to `raw/T903B_v1_original.md`
- [ ] Move `T903B_i2.md` to `raw/T903B_v2_original.md`
- [ ] Move `plan_prompt-script-conversation-constructor_T903B_i1.md` to `raw/`
- [ ] Move `plan_prompt-script-conversation-constructor_T903B_i2.md` to `raw/`

##### Task 0.2.2: Create Compliant Plan File
- [ ] Create `consultant/workspace/plan/plan_T903A_technical-phases_v1.0.0.md`
- [ ] Consolidate content from T903B_i2.md into compliant format
- [ ] Add YAML frontmatter per T801 standard
- [ ] Map existing phases to governance phase numbering

##### Task 0.2.3: Fixture Canonicalization (Optional)
- [ ] Decision: Designate canonical fixture location
- [ ] If `tests/prompt/fixtures/` is canonical: Archive `T903/conversation_samples/` to `raw/`
- [ ] If both retained: Document relationship in SPS

**Success Criteria Checklist**:
- [ ] All original files archived in `raw/` with clear naming
- [ ] Compliant plan file created in `consultant/workspace/plan/`
- [ ] Fixture location decision documented

---

#### Activity 0.3: SPS Governance File Creation

**Purpose**: Create the Single Source of Truth (SSOT) governance file for Initiative T901 with Epic T903A dossier.

**Target**: `prompt/artifacts/tasks/T903/consultant/sps/sps_T901-TOOLS_v1.0.0.md`

**Task List**:

##### Task 0.3.1: Create SPS Skeleton
- [ ] Create file with YAML frontmatter per T801 standard
- [ ] Add Executive Summary section
- [ ] Add Core Content section structure (III.A, III.B, III.C)

##### Task 0.3.2: Populate Initiative Considerations (III.B)
- [ ] Define Organization & Responsibilities (roles RACI)
- [ ] Document Project Assumptions
- [ ] Document Project Constraints
- [ ] Define Success Criteria placeholders
- [ ] Document Dependencies (existing parser architecture, tests)
- [ ] Define Interfaces (CLI contract, parser API)

##### Task 0.3.3: Create Epic T903A Dossier (III.C.1)
- [ ] Add epic YAML header (epic_id, epic_code, epic_title, status, owner)
- [ ] Write Purpose section (~1 paragraph + ≤3 bullets)
- [ ] Define Scope (In Scope / Out of Scope)
- [ ] Add Inherited Considerations references

##### Task 0.3.4: Populate Governance & Roadmap (III.C.1.iv)
- [ ] Define Scope & Ownership (Decision Owner, Epic Lead, Technical Authority)
- [ ] Create Feature Register table with T903A1–T903A7

| ID | Code | Name | Purpose | Owner | Status |
|:---|:-----|:-----|:--------|:------|:-------|
| `T903A1` | `DETECTION` | Format Detection | Auto-detection system | LLM_Developer | `complete` |
| `T903A2` | `STANDARD` | Standard JSON Parser | Google Gemini format | LLM_Developer | `complete` |
| `T903A3` | `COMPARISON` | Comparison JSON Parser | Multi-thread A/B testing | LLM_Developer | `complete` |
| `T903A4` | `PLAINTEXT` | Plain Text Log Parser | Claude Code session logs | LLM_Developer | `proposed` |
| `T903A5` | `CLI` | Command-Line Interface | User-facing CLI | LLM_Developer | `in-progress` |
| `T903A6` | `DOCS` | Documentation | User and developer guides | LLM_Developer | `proposed` |
| `T903A7` | `QA` | Quality Assurance | Testing and performance | LLM_Developer | `proposed` |

- [ ] Define Phase Sequence (mapping T903B technical phases to governance phases)

**Phase Sequence Mapping**:
| Governance Phase | Technical Phase | Name | Status |
|:-----------------|:----------------|:-----|:-------|
| Phase 0 | — | Governance Foundation | 🔄 In Progress |
| Phase 1 | T903B-1 | Architecture & TDD | ✅ Complete |
| Phase 2 | T903B-2,3,4 | Implementation (Detection, Parsing, CLI) | 🔄 ~70% |
| Phase 3 | T903B-5,6 | Documentation & QA | ❌ Pending |

- [ ] Define Success Checkpoints

##### Task 0.3.5: Add Epic Requirements Placeholders (III.C.1.v)
- [ ] Add Assumptions section with placeholder structure
- [ ] Add Constraints section with placeholder structure
- [ ] Add Quality Goals section with placeholder structure
- [ ] Add Dependencies section referencing existing implementation
- [ ] Add Interfaces section referencing CLI and parser API
- [ ] Add Implementation Guidance section referencing T903B

##### Task 0.3.6: Add Research & Notes Section (III.C.1.vi)
- [ ] Reference existing documentation: `conversation_constructor_guide.md`
- [ ] Reference existing implementation analysis: `analysis_T903A-CONV_initiative-status-research.md`
- [ ] Add notes on integration gaps identified

##### Task 0.3.7: Add Issues & Risks Placeholders (III.C.1.viii)
- [ ] Create Issues table with known issues from T903B_i2.md
- [ ] Create Risks table with identified risks

**Success Criteria Checklist**:
- [ ] SPS file created with valid YAML frontmatter
- [ ] Initiative structure (T901) defined
- [ ] Epic dossier (T903A) complete with all required sections
- [ ] Feature Register populated with T903A1–T903A7
- [ ] Phase roadmap maps to T903B technical phases
- [ ] E-RID placeholder sections ready for Phase 1

---

#### Activity 0.4: Analysis File Completion

**Purpose**: Ensure this plan's companion analysis file is complete and cross-referenced.

**Target**: `prompt/artifacts/tasks/T903/consultant/workspace/analysis/analysis_T903A-CONV_initiative-status-research.md`

**Task List**:

##### Task 0.4.1: Review and Finalize Analysis
- [x] Analysis file created with comprehensive status assessment
- [ ] Cross-reference with SPS upon creation
- [ ] Update Open Questions based on Client feedback

**Success Criteria Checklist**:
- [x] Analysis file exists at compliant location
- [ ] Analysis file cross-referenced from SPS Research & Notes section

---

#### Activity 0.5: Client Approval Gate

**Purpose**: Obtain formal Client approval before proceeding to Phase 1 (E-RID development).

**Target**: This plan and SPS file

**Task List**:

##### Task 0.5.1: Present Phase 0 Deliverables
- [ ] Present directory structure changes
- [ ] Present SPS governance file draft
- [ ] Present material organization plan

##### Task 0.5.2: Resolve Open Questions
From `analysis_T903A-CONV_initiative-status-research.md` Section VIII:

| Question | Client Decision | Impact |
|:---------|:----------------|:-------|
| Q1: Initiative hierarchy (T901.T903A vs standalone T903) | TBD | SPS naming |
| Q2: Test migration to `prompt/tests/` included in Phase 0? | TBD | Phase 0 scope |
| Q3: Fixture canonicalization approach | TBD | Maintenance |
| Q4: PlainTextLogParser priority | TBD | Phase 1/2 scope |

##### Task 0.5.3: Capture Approval Statement
- [ ] Add approval statement to SPS Section IX (Stakeholder Sign-Off)
- [ ] Update SPS status from `draft` to `approved`
- [ ] Update this plan status from `draft` to `approved`

**Success Criteria Checklist**:
- [ ] All Open Questions resolved or explicitly deferred
- [ ] Client approval captured in writing
- [ ] SPS and Plan statuses updated

---

### Phase 0 Success Criteria (Consolidated)

**Gate Criteria**: All items below MUST be checked before proceeding to Phase 1:

**Directory Structure (Activity 0.1)**:
- [x] All governance directories created
- [ ] Structure matches T801 exemplar pattern

**Material Organization (Activity 0.2)**:
- [ ] Original files archived in `raw/`
- [ ] Compliant plan file created
- [ ] Fixture location documented

**SPS Governance (Activity 0.3)**:
- [ ] SPS file created with valid structure
- [ ] Feature Register complete (T903A1–T903A7)
- [ ] Phase roadmap documented
- [ ] E-RID placeholders ready

**Analysis (Activity 0.4)**:
- [x] Analysis file complete
- [ ] Cross-referenced from SPS

**Client Approval (Activity 0.5)**:
- [ ] Open Questions resolved
- [ ] Formal approval captured

---

## IV. PHASE 1 PREVIEW: E-RID DEVELOPMENT

**Objective**: Develop Epic Requirements (E-RIDs) for T903A using structured inquiry, then implement into SPS after Client approval.

**Scope**: Define E-RIDs across categories:
- **ASSUM**: Assumptions about parser architecture, format detection accuracy, etc.
- **CON**: Constraints on backward compatibility, test infrastructure, etc.
- **QG**: Quality Goals for accuracy, performance, coverage, etc.
- **DEP**: Dependencies on existing parser implementation, pytest, etc.
- **IF**: Interfaces for CLI contract, parser API, output formats
- **IG**: Implementation Guidance for Phase 2 technical work

**Prerequisite**: Phase 0 complete with Client-approved SPS foundation.

---

## V. CHANGELOG

- **v1.0.0** (2026-01-11): Initial Phase 0 plan creation
  - Defined governance foundation establishment activities
  - Created Activity 0.1–0.5 with task breakdowns
  - Added success criteria checklists
  - Included Phase 1 preview
