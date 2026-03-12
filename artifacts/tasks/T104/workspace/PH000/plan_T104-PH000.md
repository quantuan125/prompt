---
artifact_type: 'PLAN'
planning_level: 'PHASE'
initiative_id: 'T104'
initiative_code: 'CWS'
phase: '0'
version: '2.0.0'
date: '2026-01-29'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
governance_rules: 'prompt/templates/consultant/workspace/workspace_documentation_rules.md'
template_reference: 'prompt/templates/consultant/workspace/template_workspace_roadmap.md'
procedural_guideline: 'prompt/templates/consultant/workspace/guideline_workspace_roadmap.md'
ssot_sps_target: 'prompt/artifacts/tasks/T104/ssot/sps_T104-CWS.md'
ssot_concept_target: 'prompt/artifacts/tasks/T104/ssot/concept_T104-CWS.md'
reference_exemplar_sps: 'prompt/artifacts/tasks/T102/ssot/sps_T102-CONSULTANT.md'
reference_exemplar_concept: 'prompt/artifacts/tasks/T102/ssot/concept_T102-CONSULTANT.md'
reference_exemplar_roadmap: 'prompt/artifacts/tasks/T104/T104A/ssot/roadmap_T104A-ROADMAP_phase0.md'
parent_roadmap: 'prompt/artifacts/tasks/T104/ssot/roadmap_T104-CWS.md'
---

# PLAN: T104 (CWS) — Phase 0: Initiative Scaffolding & Standards

## I. EXECUTIVE SUMMARY

**Purpose**: Deliver an initiative-level roadmap for `T104 (CWS)` that sets up governance and standardized consultant workspace frameworks, and that scaffolds SSOT deliverables (`SPS` + `CONCEPT`) for subsequent epic execution:
- `T104A (ROADMAP)`
- `T104B (NOTES)`
- `T104C (PROPOSAL)`
- `T104D (ANALYSIS)`
- `T104E (CHANGELOG)`
- `T104F (PLAN)`

**Phase 0 Objective**: Establish the minimum viable initiative scaffolding:
1) Create Phase 0 initiative roadmap + registers and lock terminology.
2) Commission end-to-end research (`T104-RES-001`) to validate workflow directionality and the epic set (T104A–T104E).
3) Create `T104` SSOT scaffolds in `prompt/artifacts/tasks/T104/ssot/` aligned to T102 ADR/GDR standards and exemplars.
4) Define epic scope boundaries and artifact role boundaries (Roadmap / Proposal / Notes / Changelog) for Phase 1+ work.

**Phase 0 Exit Milestone**: **T104 SSOT Scaffold Ready**
- T104-RES-001 delivered and synthesized (research report + consultant analysis).
- `sps_T104-CWS.md` skeleton exists with epic register (T104A–T104E) and governance snapshot placeholders.
- `concept_T104-CWS.md` skeleton exists with decision system placeholders aligned to T102 standards.
- Roadmap standard decisions captured and linked to initiative Notes (2026-01-16) and roadmap Changelog.

**Locked Decisions (Client-approved)**
- **SSOT location**: `prompt/artifacts/tasks/T104/ssot/` is the canonical location for T104 SSOT files.
- **Terminology**: Phase → Stream → Activity → Task.
- **Heading semantics**: `###` reserved for Stream; `####` reserved for Activity; Tasks are tracked under Activities (checklist and/or Task Register).
- **Notes prefix**: use `notes_...` (avoid `log_...` to reduce confusion/collision with `changelog_...`).
- **Changelog**: always a separate `changelog_...` file (not embedded).
- **Epic**: introduce `T104E (CHANGELOG)` (define standards only; no mass changelog migrations in Phase 0).
- **Roadmap authoring rules**: centralize roadmap authoring rules in `guideline_workspace_roadmap.md` and reference it from roadmaps (avoid per-roadmap drift).

---

## II. CONTEXT MATERIALS & PREREQUISITES

**SSOT exemplars (read-only; do not modify as part of T104)**:
- `prompt/artifacts/tasks/T102/ssot/sps_T102-CONSULTANT.md`
- `prompt/artifacts/tasks/T102/ssot/concept_T102-CONSULTANT.md`

**Roadmap exemplar (structure; read-only for Phase 0 decisions)**:
- `prompt/artifacts/tasks/T104/T104A/ssot/roadmap_T104A-ROADMAP_phase0.md`

**Workspace governance rules (referenced; planned for update in later streams)**:
- `prompt/templates/consultant/workspace/workspace_documentation_rules.md`

---

## III. PHASE 0: INITIATIVE SCAFFOLDING & STANDARDS ROADMAP

**Objective**: Build the T104 initiative backbone (SSOT + epic scaffolds) and codify artifact role boundaries and naming/heading rules that prevent drift.

**Roadmap Authoring Guideline (reference)**: `prompt/templates/consultant/workspace/guideline_workspace_roadmap.md`

### Parallelism & Dependencies Standard (Roadmap)

See `prompt/templates/consultant/workspace/guideline_workspace_roadmap.md` (Section V.B).

### Stream Register

| Stream | Name | Objective | Status | Owner | Execution Mode | Depends On | Start | Target | Completion | Key Deliverables |
|:------|:-----|:----------|:-------|:------|:--------------|:----------|:------|:-------|:-----------|:----------------|
| 1 | **Initialization & Scope Lock** | Initialize Phase 0 artifacts; lock naming/terminology decisions | `completed` | LLM_Consultant | SEQUENTIAL | — | 2026-01-16 | 2026-01-17 | 2026-01-17 | `plan_T104-CWS_phase0.md`, `notes_T104-CWS_phase0.md`, `changelog_roadmap_T104-CWS_phase0.md` |
| 2 | **Research Commission (End-to-End)** | Commission research to validate agentic consultant workflow across Roadmap/Notes/Proposal/Analysis/Changelog (runs in parallel with SSOT/epic scaffolding; informs Phase 1 finalization) | `completed` | LLM_Consultant | PARALLEL | 1 | 2026-01-18 | 2026-01-24 | 2026-01-24 | `brief_T104-RES-001_agentic-workspace-assessment.md`, `report_T104-RES-001_agentic-workspace-assessment.md`, `analysis_T104-RES-001_agentic-workspace-assessment.md` |
| 3 | **SSOT Scaffolding (T104)** | Draft T104 SSOT skeletons aligned to T102 standards (scaffolding only) | `completed` | LLM_Consultant | PARALLEL | 1 | — | — | — | `sps_T104-CWS.md`, `concept_T104-CWS.md` |
| 4 | **Epic Scaffolds (A–E)** | Draft epic register + dossier placeholders inside T104 SSOT (scaffolding only) | `completed` | LLM_Consultant | SEQUENTIAL | 3 | 2026-01-27 | 2026-01-27 | 2026-01-27 | Epic register + dossier placeholders (T104A–T104E) |
| 5 | **Artifact Role Standards** | Define Roadmap/Proposal/Notes/Changelog boundaries and minimum contracts (define standards only) | `planned` | LLM_Consultant | PARALLEL | 3 | — | — | — | T104 artifact role standards (SSOT references) |
| 6 | **Template Alignment** | Align roadmap authoring rules and template surfaces to the locked Phase → Stream → Activity model (plan deltas for `workspace_documentation_rules.md`; keep templates toolable) | `planned` | LLM_Consultant | PARALLEL | 1 | 2026-01-18 | — | — | `template_workspace_roadmap.md` (update), `guideline_workspace_roadmap.md` (new), delta checklist for `workspace_documentation_rules.md` |
| 7 | **Validation & Handoff** | Validate internal consistency and produce adoption guidance | `planned` | LLM_Consultant | SEQUENTIAL | 2, 3, 4, 5, 6 | — | — | — | Validation notes + adoption checklist |

---

### Activity Register

| Stream | Activity | Name | Status | Owner | Execution Mode | Depends On | Start | Target | Completion | Deliverable(s) |
|:-------|:---------|:-----|:-------|:------|:--------------|:----------|:------|:-------|:-----------|:--------------|
| 1 | 1.1 | **Create Initiative Phase Plan (Phase 0)** | `completed` | LLM_Consultant | SEQUENTIAL | — | 2026-01-16 | 2026-01-17 | 2026-01-17 | `prompt/artifacts/tasks/T104/workspace/PH000/plan_T104-PH000.md` |
| 1 | 1.2 | **Create Initiative Notes (Session Record)** | `completed` | LLM_Consultant | SEQUENTIAL | 1.1 | 2026-01-16 | 2026-01-17 | 2026-01-17 | `prompt/artifacts/tasks/T104/workspace/PH000/notes_T104-PH000.md` |
| 1 | 1.3 | **Create Roadmap Changelog** | `completed` | LLM_Consultant | SEQUENTIAL | 1.1 | 2026-01-17 | 2026-01-17 | 2026-01-17 | `prompt/artifacts/tasks/T104/archive/changelog_roadmap_T104-CWS_phase0.md` |
| 2 | 2.1 | **Research Brief Creation (T104-RES-001)** | `completed` | LLM_Consultant | PARALLEL | 1.1 | 2026-01-18 | 2026-01-18 | 2026-01-18 | `prompt/artifacts/tasks/T104/research/T104-RES-001/brief_T104-RES-001_agentic-workspace-assessment.md` |
| 2 | 2.2 | **Research Execution & Report Delivery (T104-RES-001)** | `completed` | LLM_Researcher | SEQUENTIAL | 2.1 | 2026-01-18 | 2026-01-18 | 2026-01-18 | `prompt/artifacts/tasks/T104/research/T104-RES-001/report_T104-RES-001_agentic-workspace-assessment.md` |
| 2 | 2.3 | **Consultant Analysis & Synthesis (T104-RES-001)** | `completed` | LLM_Consultant | SEQUENTIAL | 2.2 | 2026-01-24 | 2026-01-24 | 2026-01-24 | `prompt/artifacts/tasks/T104/workspace/_unresolved/analysis_T104-RES-001_agentic-workspace-assessment.md` |
| 2 | 2.4 | **Notes Update (Stream 2 Decision Capture)** | `deffered` | LLM_Consultant | SEQUENTIAL | 2.3 | — | — | — | `prompt/artifacts/tasks/T104/workspace/PH000/notes_T104-PH000.md` (update) |
| 3 | 3.1 | **Draft `sps_T104-CWS.md` Skeleton (incl. SPS III.A)** | `completed` | LLM_Consultant | PARALLEL | 1.1 | 2026-01-26 | 2026-01-26 | 2026-01-26 | `prompt/artifacts/tasks/T104/ssot/sps_T104-CWS.md` |
| 3 | 3.2 | **Draft `concept_T104-CWS.md` Skeleton** | `completed` | LLM_Consultant | PARALLEL | 1.1 | 2026-01-26 | 2026-01-26 | 2026-01-26 | `prompt/artifacts/tasks/T104/ssot/concept_T104-CWS.md` |
| 3 | 3.3 | **Align SSOT Scaffolds to T102 ADR/GDR Contracts** | `completed` | LLM_Consultant | PARALLEL | 3.1, 3.2 | 2026-01-26 | 2026-01-26 | 2026-01-26 | SSOT section placeholders + references to T102 ADRs |
| 4 | 4.1 | **Add Epic Register (T104A–T104E) into SPS** | `completed` | LLM_Consultant | PARALLEL | 3.1 | 2026-01-27 | 2026-01-27 | 2026-01-27 | SPS epic register rows + ownership notes |
| 4 | 4.2 | **Define Epic Artifact Responsibilities (A–E)** | `completed` | LLM_Consultant | PARALLEL | 4.1 | 2026-01-27 | 2026-01-27 | 2026-01-27 | SPS epic dossier placeholders (what each epic must produce) |
| 5 | 5.1 | **Define Notes vs Changelog Semantics** | `planned` | LLM_Consultant | PARALLEL | 3.1 | — | — | — | Standard statements (MUST/MUST NOT) referenced by SSOT |
| 5 | 5.2 | **Define Naming + Prefix Policy (T104)** | `planned` | LLM_Consultant | PARALLEL | 5.1 | — | — | — | Standard naming rules (incl. `notes_` vs `changelog_`) |
| 5 | 5.3 | **Define Minimum Changelog Standard (T104E)** | `planned` | LLM_Consultant | PARALLEL | 5.1 | — | — | — | Changelog template rules (define-only) |
| 6 | 6.1 | **Plan Updates to `workspace_documentation_rules.md`** | `planned` | LLM_Consultant | PARALLEL | 1.1 | — | — | — | Delta checklist recorded in this roadmap |
| 6 | 6.2 | **Update `template_workspace_roadmap.md` (Dependency Notation + Structure)** | `completed` | LLM_Consultant | PARALLEL | 1.1 | 2026-01-18 | 2026-01-18 | 2026-01-18 | `prompt/templates/consultant/workspace/template_workspace_roadmap.md` (update) |
| 6 | 6.3 | **Extract Roadmap Authoring Guidelines (procedural)** | `completed` | LLM_Consultant | PARALLEL | 6.2 | 2026-01-24 | 2026-01-24 | 2026-01-24 | `prompt/templates/consultant/workspace/guideline_workspace_roadmap.md` |
| 7 | 7.1 | **Validate Internal References + Readiness** | `planned` | LLM_Consultant | SEQUENTIAL | 2, 3, 4, 5, 6 | — | — | — | Validation checklist outcomes |

---

### Stream 1: Initialization & Scope Lock

#### Activity 1.1: Create Initiative Phase Plan (Phase 0)

**Purpose**: Create the initiative-level Phase 0 roadmap with registers and locked decisions.

**Deliverable**: `prompt/artifacts/tasks/T104/workspace/PH000/plan_T104-PH000.md`

**Task List**:
1. Establish Phase → Stream → Activity → Task structure and heading semantics (`###` Stream; `####` Activity).
2. Include Stream Register and Activity Register (incl. `Execution Mode` + `Depends On` columns; Start/Target/Completion columns).
3. Define Phase 0 streams that scaffold SSOT and epic responsibilities.

**Success Criteria Checklist**:
- [x] File exists at the target path
- [x] Uses Phase → Stream → Activity → Task terminology
- [x] `###` headings used only for Streams
- [x] `####` headings used only for Activities
- [x] Stream Register includes Start/Target/Completion columns
- [x] Stream Register includes `Execution Mode` + `Depends On` columns
- [x] Activity Register includes Start/Target/Completion columns
- [x] Activity Register includes `Execution Mode` + `Depends On` columns

#### Activity 1.2: Create Initiative Notes (Session Record)

**Purpose**: Capture consultation outcomes and decisions for Phase 0 session(s) as `notes_...`.

**Deliverable**: `prompt/artifacts/tasks/T104/workspace/PH000/notes_T104-PH000.md`

**Scope**:
- Cover the decisions confirmed for `2026-01-16` (consultation session record).
- Notes MUST NOT act as the source of truth for standards; it references the roadmap/SSOT targets.

**Success Criteria Checklist**:
- [x] Notes file exists at target path
- [x] Decision capture uses stable IDs (DEC-0.S#-### style)
- [x] References point to the initiative roadmap and planned SSOT targets

#### Activity 1.3: Create Roadmap Changelog

**Purpose**: Create a separate changelog file for this initiative roadmap.

**Deliverable**: `prompt/artifacts/tasks/T104/archive/changelog_roadmap_T104-CWS_phase0.md`

**Success Criteria Checklist**:
- [x] Changelog is separate (not embedded)
- [x] Changelog includes v1.0.0 “initial creation” entry

---

### Stream 2: Research Commission (End-to-End Workflow Assessment)

**Objective**: Commission research to validate the end-to-end agentic consultant workflow for T104 and confirm whether the planned epic set (T104A–T104E) is necessary and well-scoped.

**Execution Note**: This stream runs in parallel with Streams 3–4 (scaffolding only) and informs Phase 1 finalization decisions.

#### Activity 2.1: Research Brief Creation (T104-RES-001 — Agentic Workspace Assessment)

**Purpose**: Define research scope, topics, and input packet for assessment of consultant workspace artifacts as workflow tools.

**Deliverable**: `prompt/artifacts/tasks/T104/research/T104-RES-001/brief_T104-RES-001_agentic-workspace-assessment.md`

**Required Brief Content (must be explicit)**:
- **Artifact Role Definitions (Tooling vs SSOT)**:
  - Explain Roadmap/Notes/Proposal/Analysis/Changelog as *agentic workflow tools* (planning, session memory, collaboration workspace, synthesis, version deltas).
  - Explain SPS/Concept/Request as *SSOT artifacts* (governance baseline, decision compendium, requirements baseline).
  - State “what goes where” as MUST / MUST NOT statements to reduce drift.
- **Decision question**: validate whether T104 should keep the epics T104A–T104E as currently scoped.

**Input Packet Files (required exemplars)**:
- `prompt/artifacts/tasks/T104/T104A/workspace/PH000/ST000/notes_T104A-PH000-ST000.md` (NOTES exemplar)
- `prompt/artifacts/tasks/T104/workspace/PH000/plan_T104-PH000.md` (PHASE PLAN exemplar)
- `prompt/artifacts/tasks/T801/consultant/workspace/proposal/T801A/proposal_T801A_phase1.md` (PROPOSAL exemplar)
- `prompt/artifacts/tasks/T102/T102B/workspace/roadmap/changelog_roadmap_T102B-REQUEST_phase0.md` (CHANGELOG exemplar)

**Task Checklist**:
- [x] Brief includes the “tooling vs SSOT” purpose section (explicit and concrete)
- [x] Brief includes research topics covering end-to-end pipeline viability (not a single-epic deep dive)
- [x] Brief includes success criteria and clear deliverable expectations

#### Activity 2.2: Research Execution & Report Delivery (T104-RES-001 — Agentic Workspace Assessment)

**Purpose**: Deliver a research report comparing internal exemplars + external industry practices, focusing on end-to-end pipeline viability and epic necessity.

**Deliverable**: `prompt/artifacts/tasks/T104/research/T104-RES-001/report_T104-RES-001_agentic-workspace-assessment.md`

**Report Minimum Sections**:
1. Executive summary (keep/modify/remove epics recommendation)
2. Internal exemplar assessment (strengths/weaknesses per artifact type)
3. External comparison (industry patterns for roadmap/notes/proposal/changelog separation)
4. Proposed deltas (what T104 should standardize next)
5. Risks/anti-drift safeguards

**Success Criteria Checklist**:
- [x] Explicit recommendation on whether T104A–T104E should remain as epics
- [x] Concrete guidance on role boundaries between workflow tools and SSOT artifacts

#### Activity 2.3: Consultant Analysis & Synthesis (T104-RES-001)

**Purpose**: Convert research findings into actionable initiative direction (what to standardize, what to defer, what to remove).

**Deliverable**: `prompt/artifacts/tasks/T104/workspace/_unresolved/analysis_T104-RES-001_agentic-workspace-assessment.md`

**Success Criteria Checklist**:
- [x] Clear “keep/change/remove” decisions for T104A–T104E scope (with rationale)
- [x] Mapped follow-on activities (which stream/activity numbers are affected)

#### Activity 2.4: Notes Update (Stream 2 Decision Capture)

**Purpose**: Record decisions and carry-forward items from Stream 2 into the initiative Phase 0 notes.

**Deliverable**: `prompt/artifacts/tasks/T104/workspace/PH000/notes_T104-PH000.md` (update)

---

### Stream 3: SSOT Scaffolding (T104)

**Objective**: Scaffold the T104 initiative SSOT artifacts following initiative setup standards.
**Execution Mode**: PARALLEL
**Depends On**: 1

**Context**:
- `prompt/artifacts/tasks/T104/ssot/sps_T104-CWS.md`
- `prompt/artifacts/tasks/T104/ssot/concept_T104-CWS.md`

**Constraints**:
- SSOT work in this stream is **scaffolding-only** (skeletons/placeholders; link-don’t-duplicate).
- Per Stream 2 analysis, do not merge new normative standards into SSOT until Stream 5 + Stream 6 alignment decisions are complete.

#### Activity 3.1: Draft `sps_T104-CWS.md` Skeleton (incl. SPS III.A)

**Purpose**: Create the T104 initiative SSOT scaffold following the structural intent of `sps_T102-CONSULTANT.md`.

**Status**: `completed`

**Deliverable**: `prompt/artifacts/tasks/T104/ssot/sps_T104-CWS.md`

**Scope**:
- In scope: SPS skeleton, epic register placeholders, SPS III.A Problem Definition (no solutions), links to roadmap and governance references.
- Excludes: writing/approving T104-specific ADR bodies; importing operational task detail into SSOT.

**Inputs Required**:
- `prompt/artifacts/tasks/T102/ssot/sps_T102-CONSULTANT.md` (structure exemplar; read-only)
- `prompt/artifacts/tasks/T104/workspace/_unresolved/analysis_T104-RES-001_agentic-workspace-assessment.md` (sequencing/gating guidance; read-only)

**Task Register**:
| Task ID | Description | Status | Action |
|:--------|:------------|:-------|:-------|
| 3.1.1 | Create SPS file with identity header + skeleton sections | `completed` | Created basic structure and headers |
| 3.1.2 | Add T104 epic register placeholder rows (T104A–T104E) | `completed` | Added Epic Register in Section III.C |
| 3.1.3 | Draft SPS III.A Problem Definition (problem + outcome; no solutions) | `completed` | Drafted Problem Definition based on T104 analysis |
| 3.1.4 | Add Governance & Roadmap snapshot links (link-only; no duplication) | `completed` | Linked via references |
| 3.1.5 | Add explicit references to governing T102 ADR/GDR sources (link-only) | `completed` | Linked via references |

**Success Criteria Checklist**:
- [x] SPS file exists at target path
- [x] SPS includes epic register placeholder rows (T104A–T104E)
- [x] SPS includes III.A Problem Definition without solutions
- [x] SPS includes a roadmap snapshot section that links to this roadmap (no embedded task detail)
- [x] SPS references governing T102 sources by link (no duplicated bodies)

#### Activity 3.2: Draft `concept_T104-CWS.md` Skeleton

**Purpose**: Create the T104 concept SSOT scaffold following the decision-system intent of `concept_T102-CONSULTANT.md`.

**Status**: `completed`

**Deliverable**: `prompt/artifacts/tasks/T104/ssot/concept_T104-CWS.md`

**Scope**:
- In scope: Concept skeleton, index placeholders, and placeholders for T104-specific decision records (no full bodies yet).
- Excludes: authoring full T104 ADR bodies before the Stream 5/6 alignment work is complete.

**Inputs Required**:
- `prompt/artifacts/tasks/T102/ssot/concept_T102-CONSULTANT.md` (structure exemplar; read-only)
- `prompt/artifacts/tasks/T104/workspace/_unresolved/analysis_T104-RES-001_agentic-workspace-assessment.md` (candidate decision topics; read-only)

**Task Register**:
| Task ID | Description | Status | Action |
|:--------|:------------|:-------|:-------|
| 3.2.1 | Create Concept file with identity header + skeleton sections | `completed` | Created basic structure and headers |
| 3.2.2 | Add decision record index placeholders aligned to T102 standards | `completed` | Added Index tables in Section III.B |
| 3.2.3 | Add placeholders for T104 decision records (artifact roles, naming, changelog) | `completed` | Placeholders established via table structures |

**Success Criteria Checklist**:
- [x] Concept file exists at target path
- [x] Concept includes index placeholders aligned to T102 decision record standards
- [x] Concept includes placeholders for T104 decision records (no full bodies yet)

#### Activity 3.3: Align SSOT Scaffolds to T102 ADR/GDR Contracts

**Purpose**: Ensure the SSOT skeletons are structurally compatible with governing T102 standards and are safe to expand without drift.

**Status**: `completed`

**Deliverable**: Alignment notes captured inside the SSOT scaffolds as link-only references and placeholders (no full bodies).

**Scope**:
- In scope: verify section naming/placement, index placeholders, and link contracts to governing standards.
- Excludes: governance rule or template edits (those belong to Stream 6).

**Inputs Required**:
- `prompt/artifacts/tasks/T102/ssot/sps_T102-CONSULTANT.md` (read-only)
- `prompt/artifacts/tasks/T102/ssot/concept_T102-CONSULTANT.md` (read-only)

**Task Register**:
| Task ID | Description | Status | Action |
|:--------|:------------|:-------|:-------|
| 3.3.1 | Confirm SSOT headings/sections align to T102 exemplars (structure-only) | `completed` | Validated headings against T102 |
| 3.3.2 | Add explicit “link-don’t-duplicate” notes where drift is likely | `completed` | Ensured placeholders are pointer-based |
| 3.3.3 | Verify SSOT placeholders exist for Streams 4–5 expected content | `completed` | Verified placeholders |

**Success Criteria Checklist**:
- [x] SSOT skeletons remain scaffolding-only (no embedded workflow logs/spec bodies)
- [x] SSOT skeletons contain clear placeholders for Stream 4–5 expansion
- [x] SSOT skeletons reference governing T102 sources by link (no duplicated bodies)

---

### Stream 4: Epic Scaffolds (A–E)

**Objective**: Draft epic register + dossier placeholders inside T104 SSOT so downstream work is traceable and governance-driven.
**Execution Mode**: SEQUENTIAL
**Depends On**: 3

**Context**:
- `prompt/artifacts/tasks/T104/ssot/sps_T104-CWS.md`

#### Activity 4.1: Add Epic Register (T104A–T104E) into SPS

**Purpose**: Declare the epic map for T104 so downstream work is traceable and governance-driven.

**Status**: `completed`

**Deliverable**: `prompt/artifacts/tasks/T104/ssot/sps_T104-CWS.md` (Epic register section)

**Scope**:
- In scope: epic register rows (T104A–T104E) with ownership and artifact responsibility pointers.
- Excludes: detailed epic execution plans (those belong in epic-specific roadmaps or later phases).

**Inputs Required**:
- `prompt/artifacts/tasks/T104/workspace/_unresolved/analysis_T104-RES-001_agentic-workspace-assessment.md` (epic keep/change recommendations; read-only)

**Task Register**:
| Task ID | Description | Status | Action |
|:--------|:------------|:-------|:-------|
| 4.1.1 | Add/verify epic register row placeholders for T104A–T104E | `completed` | Added structured dossier hierarchy |
| 4.1.2 | Add ownership notes for each epic (roles + decision authority) | `completed` | Included in YAML headers |
| 4.1.3 | Link epic rows to their workspace artifact targets (paths only) | `completed` | Included in Purpose/Scope sections |

**Success Criteria Checklist**:
- [x] SPS contains epic register entries for T104A–T104E
- [x] Each epic register entry includes ownership notes and target artifact paths
- [x] Entries are pointers/links only (no embedded specs)

#### Activity 4.2: Define Epic Artifact Responsibilities (A–E)

**Purpose**: Make it explicit what each epic must deliver (and what it must not) to prevent role overlap.

**Status**: `completed`

**Deliverable**: `prompt/artifacts/tasks/T104/ssot/sps_T104-CWS.md` (epic dossier placeholders)

**Scope**:
- In scope: dossier placeholders per epic (purpose, deliverables, boundaries, non-goals).
- Excludes: full artifact bodies (those remain in their respective workspace artifacts).

**Task Register**:
| Task ID | Description | Status | Action |
|:--------|:------------|:-------|:-------|
| 4.2.1 | Create dossier placeholders for each epic (T104A–T104E) | `completed` | Created structured dossiers with T102 hierarchy |
| 4.2.2 | Add explicit “MUST NOT” boundaries per epic to prevent overlap | `completed` | Added In Scope / Out of Scope boundaries |

**Success Criteria Checklist**:
- [x] SPS includes dossier placeholders for T104A–T104E
- [x] Each dossier includes explicit boundaries (what it must not contain)

---

### Stream 5: Artifact Role Standards

**Objective**: Define Roadmap/Proposal/Notes/Analysis/Changelog boundaries and minimum contracts to prevent drift before SSOT promotion.
**Execution Mode**: PARALLEL
**Depends On**: 3

**Context**:
- `prompt/artifacts/tasks/T104/ssot/sps_T104-CWS.md`
- `prompt/artifacts/tasks/T104/ssot/concept_T104-CWS.md`

#### Activity 5.1: Define Notes vs Changelog Semantics

**Purpose**: Eliminate ambiguity between “execution record” (notes) and “artifact version delta” (changelog).

**Status**: `planned`

**Deliverable**: T104 standard statements referenced by SSOT (location to be decided; expected to be recorded in SSOT Concept or an SSOT-referenced standard file).

**Scope**:
- In scope: MUST/MUST NOT rules for Notes vs Changelog; examples of allowed vs disallowed content.
- Excludes: retroactive migrations of legacy artifacts.

**Task Register**:
| Task ID | Description | Status | Action |
|:--------|:------------|:-------|:-------|
| 5.1.1 | Decide where standards will be recorded (Concept section vs dedicated standards file) | `planned` | — |
| 5.1.2 | Draft Notes semantics (session record; non-normative) | `planned` | — |
| 5.1.3 | Draft Changelog semantics (delta-only; per-artifact) | `planned` | — |
| 5.1.4 | Add MUST/MUST NOT rules + minimal examples | `planned` | — |

**Success Criteria Checklist**:
- [ ] Notes vs Changelog boundary is defined as MUST/MUST NOT rules
- [ ] Rules are referenced by SSOT (no duplication across multiple workflow tools)
- [ ] Define-only constraint is explicit (no migrations required in Phase 0)

#### Activity 5.2: Define Naming + Prefix Policy (T104)

**Purpose**: Prevent file-prefix drift and collisions across artifact types.

**Deliverable**: T104 naming standard statement(s), including:
- `roadmap_...`
- `proposal_...`
- `notes_...`
- `analysis_...`
- `changelog_<artifact>_...`

**Status**: `planned`

**Scope**:
- In scope: forward-only naming policy (prefix, casing, single extension, canonical directories).
- Excludes: bulk renames.

**Task Register**:
| Task ID | Description | Status | Action |
|:--------|:------------|:-------|:-------|
| 5.2.1 | Define canonical naming rules (lowercase prefixes; single `.md`) | `planned` | — |
| 5.2.2 | Define canonical directory locations per artifact type | `planned` | — |
| 5.2.3 | Define “legacy tolerance” guidance (no forced migrations in Phase 0) | `planned` | — |

**Success Criteria Checklist**:
- [ ] Naming rules are explicit and forward-only
- [ ] Canonical directories per artifact type are stated
- [ ] Legacy tolerance guidance is documented (no Phase 0 bulk migrations)

#### Activity 5.3: Define Minimum Changelog Standard (T104E)

**Purpose**: Define (only) what “good changelog” means for T104 artifacts (schema, minimum entries, scope, and non-goals).

**Status**: `planned`

**Deliverable**: Changelog standard statement(s) (no bulk migrations in Phase 0).

**Scope**:
- In scope: minimum changelog schema and entry expectations.
- Excludes: migrating old artifacts to the new schema.

**Task Register**:
| Task ID | Description | Status | Action |
|:--------|:------------|:-------|:-------|
| 5.3.1 | Define changelog minimum schema (overview table + detail bullets) | `planned` | — |
| 5.3.2 | Define entry requirements (version/date/type/summary) | `planned` | — |
| 5.3.3 | Define non-goals (no backfill migrations in Phase 0) | `planned` | — |

**Success Criteria Checklist**:
- [ ] Minimum changelog schema is defined
- [ ] Entry requirements are explicit
- [ ] Non-goals are explicit (define-only in Phase 0)

---

### Stream 6: Template Alignment (Parallel Standardization)

**Objective**: Ensure templates and governance guidance align with the locked Phase → Stream → Activity model and remain toolable.
**Execution Mode**: PARALLEL
**Depends On**: 1

**Context**:
- `prompt/templates/consultant/workspace/template_workspace_roadmap.md`
- `prompt/templates/consultant/workspace/workspace_documentation_rules.md`
- `prompt/templates/consultant/workspace/guideline_workspace_roadmap.md`
- `prompt/artifacts/tasks/T104/workspace/PH000/plan_T104-PH000.md`

#### Activity 6.1: Plan Updates to `workspace_documentation_rules.md`

**Purpose**: Define the required deltas so later edits are surgical and traceable.

**Status**: `planned`

**Deliverable**: Delta checklist recorded in this roadmap (do not implement here).

**Scope**:
- In scope: identify specific wording/structure conflicts and record an ordered delta checklist.
- Excludes: applying the changes to `workspace_documentation_rules.md` in this phase.

**Task Register**:
| Task ID | Description | Status | Action |
|:--------|:------------|:-------|:-------|
| 6.1.1 | Identify conflicts vs T104 locked heading semantics (Subphase vs Stream/Activity) | `planned` | — |
| 6.1.2 | Identify conflicts vs Notes semantics (`notes_` vs “LOG/Subphase”) | `planned` | — |
| 6.1.3 | Record delta checklist (ordered edits; no implementation) | `planned` | — |

**Success Criteria Checklist**:
- [ ] Delta checklist is explicit and ordered
- [ ] Checklist addresses heading semantics conflict and Notes semantics conflict
- [ ] No governance rules are changed in-place in Phase 0

#### Activity 6.2: Update `template_workspace_roadmap.md` (Dependency Notation + Structure)

**Purpose**: Ensure the roadmap template yields the canonical Phase/Stream/Activity/Task structure and dependency notation standard (parallel streams/activities).

**Status**: `completed`

**Deliverable**: `prompt/templates/consultant/workspace/template_workspace_roadmap.md` (update)

**Task Register**:
| Task ID | Description | Status | Action |
|:--------|:------------|:-------|:-------|
| 6.2.1 | Align template headings to `###` Stream / `####` Activity semantics | `completed` | Updated template heading semantics and examples |
| 6.2.2 | Add/register dependency notation fields (Execution Mode + Depends On) | `completed` | Updated template registers to include `Execution Mode` and `Depends On` |
| 6.2.3 | Add anti-drift boundaries (no execution logs; link to SSOT) | `completed` | Added/confirmed anti-drift guidance in template |

**Success Criteria Checklist**:
- [x] Template enforces Stream/Activity heading semantics
- [x] Template includes dependency notation fields
- [x] Template includes anti-drift boundaries

#### Activity 6.3: Extract Roadmap Authoring Guidelines (procedural)

**Purpose**: Standardize roadmap authoring rules in a single procedural guideline to avoid per-roadmap drift.

**Status**: `completed`

**Deliverable**: `prompt/templates/consultant/workspace/guideline_workspace_roadmap.md`

**Scope**:
- In scope: status enums, Task Register schema, Activity completion rule, Stream Context rule, dependency notation standard.
- Excludes: rewriting the roadmap template to embed the full guideline (defer to later work).

**Task Register**:
| Task ID | Description | Status | Action |
|:--------|:------------|:-------|:-------|
| 6.3.1 | Extract and consolidate roadmap authoring rules into a standalone file | `completed` | Created procedural guideline file and aligned it to current template semantics |
| 6.3.2 | Reference the procedural guideline from this roadmap | `completed` | Added `procedural_guideline` frontmatter and reference in Section III |

**Success Criteria Checklist**:
- [x] Procedural guideline file exists at target path
- [x] Roadmap references the guideline (avoid embedded authoring rules)

---

### Stream 7: Validation & Handoff

**Objective**: Validate internal references, naming, and contracts are consistent and ready for Phase 1 execution.
**Execution Mode**: SEQUENTIAL
**Depends On**: 2, 3, 4, 5, 6

**Context**:
- `prompt/artifacts/tasks/T104/workspace/PH000/plan_T104-PH000.md` (validation record)

#### Activity 7.1: Validate Internal References + Readiness

**Purpose**: Confirm all links, naming, and contracts are consistent and ready for Phase 1 execution.

**Status**: `planned`

**Deliverable**: Validation outcomes recorded in this roadmap.

**Scope**:
- In scope: link integrity checks, naming consistency checks, readiness checklist for Phase 1.
- Excludes: implementing missing artifacts (this is validation + handoff).

**Task Register**:
| Task ID | Description | Status | Action |
|:--------|:------------|:-------|:-------|
| 7.1.1 | Validate Links Register targets exist and are correctly named | `planned` | — |
| 7.1.2 | Validate register statuses follow the enum and are backticked | `planned` | — |
| 7.1.3 | Validate Stream 3+ includes Context + Scope + Task Registers + Success Criteria | `planned` | — |
| 7.1.4 | Record readiness outcome and any carry-forward items | `planned` | — |

**Success Criteria Checklist**:
- [ ] All Links Register targets exist (or are explicitly marked planned/deferred)
- [ ] Status enums are consistent and backticked across registers
- [ ] Stream 3+ structure is consistent (Context/Scope/Task Register/Success Criteria)
- [ ] Readiness outcome recorded for Phase 1 handoff

---

## IV. LINKS REGISTER

| Link Type | Target | Path |
|:----------|:-------|:-----|
| Plan (this file) | T104 Phase 0 Plan | `prompt/artifacts/tasks/T104/workspace/PH000/plan_T104-PH000.md` |
| Roadmap | T104 Master Roadmap | `prompt/artifacts/tasks/T104/ssot/roadmap_T104-CWS.md` |
| Notes | T104 Phase 0 Notes | `prompt/artifacts/tasks/T104/workspace/PH000/notes_T104-PH000.md` |
| Changelog | Roadmap Changelog | `prompt/artifacts/tasks/T104/archive/changelog_roadmap_T104-CWS_phase0.md` |
| Research (target) | T104-RES-001 Brief | `prompt/artifacts/tasks/T104/research/T104-RES-001/brief_T104-RES-001_agentic-workspace-assessment.md` |
| Research (target) | T104-RES-001 Report | `prompt/artifacts/tasks/T104/research/T104-RES-001/report_T104-RES-001_agentic-workspace-assessment.md` |
| Analysis (target) | T104-RES-001 Synthesis | `prompt/artifacts/tasks/T104/workspace/_unresolved/analysis_T104-RES-001_agentic-workspace-assessment.md` |
| SSOT (target) | T104 SPS | `prompt/artifacts/tasks/T104/ssot/sps_T104-CWS.md` |
| SSOT (target) | T104 Concept | `prompt/artifacts/tasks/T104/ssot/concept_T104-CWS.md` |
| Exemplar (read-only) | T102 SPS | `prompt/artifacts/tasks/T102/ssot/sps_T102-CONSULTANT.md` |
| Exemplar (read-only) | T102 Concept | `prompt/artifacts/tasks/T102/ssot/concept_T102-CONSULTANT.md` |
| Exemplar (read-only) | T104A Roadmap | `prompt/artifacts/tasks/T104/T104A/ssot/roadmap_T104A-ROADMAP_phase0.md` |
| Governance Rules | Workspace Rules | `prompt/templates/consultant/workspace/workspace_documentation_rules.md` |
| Roadmap Template | Template | `prompt/templates/consultant/workspace/template_workspace_roadmap.md` |
| Procedural Guideline | Roadmap Authoring Rules | `prompt/templates/consultant/workspace/guideline_workspace_roadmap.md` |

---

## V. OPEN QUESTIONS REGISTER

| ID | Topic | Question | Owner | Status | Proposed Date | Resolved Date |
|:---|:------|:---------|:------|:-------|:--------------|:-------------|
| OQ-001 | SSOT Authoring Scope | Should Phase 0 author T104-specific ADRs immediately, or keep placeholders only until Phase 1? | Client | Proposed | 2026-01-17 | — |
| OQ-002 | Notes Template | Should T104B define a `template_workspace_notes.md`, or reuse the existing log template pattern with renamed semantics? | Client | Proposed | 2026-01-17 | — |
| OQ-003 | Research Scope | Confirm whether T104-RES-001 should include recommendations about renaming existing T104A artifacts (or remain “forward-only” guidance). | Client | Proposed | 2026-01-17 | — |

---

## VI. CHANGELOG

`prompt/artifacts/tasks/T104/archive/changelog_roadmap_T104-CWS_phase0.md`
