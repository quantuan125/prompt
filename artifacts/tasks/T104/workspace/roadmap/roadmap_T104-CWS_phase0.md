---
artifact_type: 'ROADMAP'
initiative_id: 'T104'
initiative_code: 'CWS'
phase: '0'
version: '1.2.0'
date: '2026-01-18'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
governance_rules: 'prompt/templates/consultant/workspace/workspace_documentation_rules.md'
template_reference: 'prompt/templates/consultant/workspace/template_workspace_roadmap.md'
ssot_sps_target: 'prompt/artifacts/tasks/T104/ssot/sps_T104-CWS.md'
ssot_concept_target: 'prompt/artifacts/tasks/T104/ssot/concept_T104-CWS.md'
reference_exemplar_sps: 'prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md'
reference_exemplar_concept: 'prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md'
reference_exemplar_roadmap: 'prompt/artifacts/tasks/T104/T104A/workspace/roadmap/roadmap_T104A-ROADMAP_phase0.md'
---

# ROADMAP: T104 (CWS) — Phase 0: Initiative Scaffolding & Standards

## I. EXECUTIVE SUMMARY

**Purpose**: Deliver an initiative-level roadmap for `T104 (CWS)` that sets up governance and standardized consultant workspace frameworks, and that scaffolds SSOT deliverables (`SPS` + `CONCEPT`) for subsequent epic execution:
- `T104A (ROADMAP)`
- `T104B (NOTES)`
- `T104C (PROPOSAL)`
- `T104D (ANALYSIS)`
- `T104E (CHANGELOG)`

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
- **Heading semantics**: `###` reserved for Stream; `####` reserved for Activity; Tasks are checklist items under Activities.
- **Notes prefix**: use `notes_...` (avoid `log_...` to reduce confusion/collision with `changelog_...`).
- **Changelog**: always a separate `changelog_...` file (not embedded).
- **Epic**: introduce `T104E (CHANGELOG)` (define standards only; no mass changelog migrations in Phase 0).

---

## II. CONTEXT MATERIALS & PREREQUISITES

**SSOT exemplars (read-only; do not modify as part of T104)**:
- `prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md`
- `prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md`

**Roadmap exemplar (structure; read-only for Phase 0 decisions)**:
- `prompt/artifacts/tasks/T104/T104A/workspace/roadmap/roadmap_T104A-ROADMAP_phase0.md`

**Workspace governance rules (referenced; planned for update in later streams)**:
- `prompt/templates/consultant/workspace/workspace_documentation_rules.md`

---

## III. PHASE 0: INITIATIVE SCAFFOLDING & STANDARDS ROADMAP

**Objective**: Build the T104 initiative backbone (SSOT + epic scaffolds) and codify artifact role boundaries and naming/heading rules that prevent drift.

**Parallelism & Dependencies Standard (Roadmap)**
- **Execution Mode**:
  - `PARALLEL`: may be executed concurrently (subject to `Depends On`).
  - `SEQUENTIAL`: intended ordering signal (still enforce via `Depends On` if required).
  - `GATED`: requires explicit exit evidence before dependent work starts (use `Depends On` + an “Exit Evidence” checklist in the Stream).
- **Depends On**: comma-separated list of prerequisite **Stream IDs** and/or **Activity IDs** (e.g., `1`, `1.1`, `2.2`). Use `—` if none.
- **Rule**: `Depends On` is the enforceable constraint; `Execution Mode` is the coordination intent.

### Stream Register

| Stream | Name | Objective | Status | Owner | Execution Mode | Depends On | Start | Target | Completion | Key Deliverables |
|:------|:-----|:----------|:-------|:------|:--------------|:----------|:------|:-------|:-----------|:----------------|
| 1 | **Initialization & Scope Lock** | Initialize Phase 0 artifacts; lock naming/terminology decisions | Complete | LLM_Consultant | SEQUENTIAL | — | 2026-01-16 | 2026-01-17 | 2026-01-17 | `roadmap_T104-CWS_phase0.md`, `notes_T104-CWS_phase0.md`, `changelog_roadmap_T104-CWS_phase0.md` |
| 2 | **Research Commission (End-to-End)** | Commission research to validate agentic consultant workflow across Roadmap/Notes/Proposal/Analysis/Changelog (runs in parallel with SSOT/epic scaffolding; informs Phase 1 finalization) | In Progress | LLM_Consultant | PARALLEL | 1 | 2026-01-18 | — | — | `brief_T104-RES-001_agentic-workspace-assessment.md`, `report_T104-RES-001_agentic-workspace-assessment.md` |
| 3 | **SSOT Scaffolding (T104)** | Draft T104 SSOT skeletons aligned to T102 standards (scaffolding only) | Planned | LLM_Consultant | PARALLEL | 1 | — | — | — | `sps_T104-CWS.md`, `concept_T104-CWS.md` |
| 4 | **Epic Scaffolds (A–E)** | Draft epic register + dossier placeholders inside T104 SSOT (scaffolding only) | Planned | LLM_Consultant | SEQUENTIAL | 3 | — | — | — | Epic register + dossier placeholders (T104A–T104E) |
| 5 | **Artifact Role Standards** | Define Roadmap/Proposal/Notes/Changelog boundaries and minimum contracts (define standards only) | Planned | LLM_Consultant | PARALLEL | 3 | — | — | — | T104 artifact role standards (SSOT references) |
| 6 | **Template Alignment** | Update `template_workspace_roadmap.md` to standardize Phase/Stream/Activity structure and dependency notation; plan deltas for `workspace_documentation_rules.md` | In Progress | LLM_Consultant | PARALLEL | 1 | 2026-01-18 | — | — | Updated `template_workspace_roadmap.md`; delta checklist for `workspace_documentation_rules.md` |
| 7 | **Validation & Handoff** | Validate internal consistency and produce adoption guidance | Planned | LLM_Consultant | SEQUENTIAL | 2, 3, 4, 5, 6 | — | — | — | Validation notes + adoption checklist |

---

### Activity Register

| Stream | Activity | Name | Status | Owner | Execution Mode | Depends On | Start | Target | Completion | Deliverable(s) |
|:-------|:---------|:-----|:-------|:------|:--------------|:----------|:------|:-------|:-----------|:--------------|
| 1 | 1.1 | **Create Initiative Roadmap** | Complete | LLM_Consultant | SEQUENTIAL | — | 2026-01-16 | 2026-01-17 | 2026-01-17 | `prompt/artifacts/tasks/T104/workspace/roadmap/roadmap_T104-CWS_phase0.md` |
| 1 | 1.2 | **Create Initiative Notes (Session Record)** | Complete | LLM_Consultant | SEQUENTIAL | 1.1 | 2026-01-16 | 2026-01-17 | 2026-01-17 | `prompt/artifacts/tasks/T104/workspace/notes/notes_T104-CWS_phase0.md` |
| 1 | 1.3 | **Create Roadmap Changelog** | Complete | LLM_Consultant | SEQUENTIAL | 1.1 | 2026-01-17 | 2026-01-17 | 2026-01-17 | `prompt/artifacts/tasks/T104/workspace/roadmap/changelog_roadmap_T104-CWS_phase0.md` |
| 2 | 2.1 | **Research Brief Creation (T104-RES-001)** | Complete | LLM_Consultant | PARALLEL | 1.1 | 2026-01-18 | 2026-01-18 | 2026-01-18 | `prompt/artifacts/tasks/T104/research/brief/brief_T104-RES-001_agentic-workspace-assessment.md` |
| 2 | 2.2 | **Research Execution & Report Delivery (T104-RES-001)** | Planned | LLM_Researcher | SEQUENTIAL | 2.1 | — | — | — | `prompt/artifacts/tasks/T104/research/report/report_T104-RES-001_agentic-workspace-assessment.md` |
| 2 | 2.3 | **Consultant Analysis & Synthesis (T104-RES-001)** | Planned | LLM_Consultant | SEQUENTIAL | 2.2 | — | — | — | `prompt/artifacts/tasks/T104/workspace/analysis/analysis_T104-RES-001_agentic-workspace-assessment.md` |
| 2 | 2.4 | **Notes Update (Stream 2 Decision Capture)** | Planned | LLM_Consultant | SEQUENTIAL | 2.3 | — | — | — | `prompt/artifacts/tasks/T104/workspace/notes/notes_T104-CWS_phase0.md` (update) |
| 3 | 3.1 | **Draft `sps_T104-CWS.md` Skeleton (incl. SPS III.A)** | Planned | LLM_Consultant | PARALLEL | 1.1 | — | — | — | `prompt/artifacts/tasks/T104/ssot/sps_T104-CWS.md` |
| 3 | 3.2 | **Draft `concept_T104-CWS.md` Skeleton** | Planned | LLM_Consultant | PARALLEL | 1.1 | — | — | — | `prompt/artifacts/tasks/T104/ssot/concept_T104-CWS.md` |
| 3 | 3.3 | **Align SSOT Scaffolds to T102 ADR/GDR Contracts** | Planned | LLM_Consultant | PARALLEL | 3.1, 3.2 | — | — | — | SSOT section placeholders + references to T102 ADRs |
| 4 | 4.1 | **Add Epic Register (T104A–T104E) into SPS** | Planned | LLM_Consultant | PARALLEL | 3.1 | — | — | — | SPS epic register rows + ownership notes |
| 4 | 4.2 | **Define Epic Artifact Responsibilities (A–E)** | Planned | LLM_Consultant | PARALLEL | 4.1 | — | — | — | SPS epic dossier placeholders (what each epic must produce) |
| 5 | 5.1 | **Define Notes vs Changelog Semantics** | Planned | LLM_Consultant | PARALLEL | 3.1 | — | — | — | Standard statements (MUST/MUST NOT) referenced by SSOT |
| 5 | 5.2 | **Define Naming + Prefix Policy (T104)** | Planned | LLM_Consultant | PARALLEL | 5.1 | — | — | — | Standard naming rules (incl. `notes_` vs `changelog_`) |
| 5 | 5.3 | **Define Minimum Changelog Standard (T104E)** | Planned | LLM_Consultant | PARALLEL | 5.1 | — | — | — | Changelog template rules (define-only) |
| 6 | 6.1 | **Plan Updates to `workspace_documentation_rules.md`** | Planned | LLM_Consultant | PARALLEL | 1.1 | — | — | — | Delta checklist recorded in this roadmap |
| 6 | 6.2 | **Update `template_workspace_roadmap.md` (Dependency Notation + Structure)** | Complete | LLM_Consultant | PARALLEL | 1.1 | 2026-01-18 | 2026-01-18 | 2026-01-18 | `prompt/templates/consultant/workspace/template_workspace_roadmap.md` (update) |
| 7 | 7.1 | **Validate Internal References + Readiness** | Planned | LLM_Consultant | SEQUENTIAL | 2, 3, 4, 5, 6 | — | — | — | Validation checklist outcomes |

---

### Stream 1: Initialization & Scope Lock

#### Activity 1.1: Create Initiative Roadmap

**Purpose**: Create the initiative-level Phase 0 roadmap with registers and locked decisions.

**Deliverable**: `prompt/artifacts/tasks/T104/workspace/roadmap/roadmap_T104-CWS_phase0.md`

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

**Deliverable**: `prompt/artifacts/tasks/T104/workspace/notes/notes_T104-CWS_phase0.md`

**Scope**:
- Cover the decisions confirmed for `2026-01-16` (consultation session record).
- Notes MUST NOT act as the source of truth for standards; it references the roadmap/SSOT targets.

**Success Criteria Checklist**:
- [x] Notes file exists at target path
- [x] Decision capture uses stable IDs (DEC-0.S#-### style)
- [x] References point to the initiative roadmap and planned SSOT targets

#### Activity 1.3: Create Roadmap Changelog

**Purpose**: Create a separate changelog file for this initiative roadmap.

**Deliverable**: `prompt/artifacts/tasks/T104/workspace/roadmap/changelog_roadmap_T104-CWS_phase0.md`

**Success Criteria Checklist**:
- [x] Changelog is separate (not embedded)
- [x] Changelog includes v1.0.0 “initial creation” entry

---

### Stream 2: Research Commission (End-to-End Workflow Assessment)

**Objective**: Commission research to validate the end-to-end agentic consultant workflow for T104 and confirm whether the planned epic set (T104A–T104E) is necessary and well-scoped.

**Execution Note**: This stream runs in parallel with Streams 3–4 (scaffolding only) and informs Phase 1 finalization decisions.

#### Activity 2.1: Research Brief Creation (T104-RES-001 — Agentic Workspace Assessment)

**Purpose**: Define research scope, topics, and input packet for assessment of consultant workspace artifacts as workflow tools.

**Deliverable**: `prompt/artifacts/tasks/T104/research/brief/brief_T104-RES-001_agentic-workspace-assessment.md`

**Required Brief Content (must be explicit)**:
- **Artifact Role Definitions (Tooling vs SSOT)**:
  - Explain Roadmap/Notes/Proposal/Analysis/Changelog as *agentic workflow tools* (planning, session memory, collaboration workspace, synthesis, version deltas).
  - Explain SPS/Concept/Request as *SSOT artifacts* (governance baseline, decision compendium, requirements baseline).
  - State “what goes where” as MUST / MUST NOT statements to reduce drift.
- **Decision question**: validate whether T104 should keep the epics T104A–T104E as currently scoped.

**Input Packet Files (required exemplars)**:
- `prompt/artifacts/tasks/T104/T104A/workspace/notes/notes_T104A-ROADMAP_phase0.md` (NOTES exemplar)
- `prompt/artifacts/tasks/T104/workspace/roadmap/roadmap_T104-CWS_phase0.md` (ROADMAP exemplar)
- `prompt/artifacts/tasks/T801/consultant/workspace/proposal/T801A/proposal_T801A_phase1.md` (PROPOSAL exemplar)
- `prompt/artifacts/tasks/T102/T102B/workspace/roadmap/changelog_roadmap_T102B-REQUEST_phase0.md` (CHANGELOG exemplar)

**Task Checklist**:
- [ ] Brief includes the “tooling vs SSOT” purpose section (explicit and concrete)
- [ ] Brief includes research topics covering end-to-end pipeline viability (not a single-epic deep dive)
- [ ] Brief includes success criteria and clear deliverable expectations

#### Activity 2.2: Research Execution & Report Delivery (T104-RES-001 — Agentic Workspace Assessment)

**Purpose**: Deliver a research report comparing internal exemplars + external industry practices, focusing on end-to-end pipeline viability and epic necessity.

**Deliverable**: `prompt/artifacts/tasks/T104/research/report/report_T104-RES-001_agentic-workspace-assessment.md`

**Report Minimum Sections**:
1. Executive summary (keep/modify/remove epics recommendation)
2. Internal exemplar assessment (strengths/weaknesses per artifact type)
3. External comparison (industry patterns for roadmap/notes/proposal/changelog separation)
4. Proposed deltas (what T104 should standardize next)
5. Risks/anti-drift safeguards

**Success Criteria Checklist**:
- [ ] Explicit recommendation on whether T104A–T104E should remain as epics
- [ ] Concrete guidance on role boundaries between workflow tools and SSOT artifacts

#### Activity 2.3: Consultant Analysis & Synthesis (T104-RES-001)

**Purpose**: Convert research findings into actionable initiative direction (what to standardize, what to defer, what to remove).

**Deliverable**: `prompt/artifacts/tasks/T104/workspace/analysis/analysis_T104-RES-001_agentic-workspace-assessment.md`

**Success Criteria Checklist**:
- [ ] Clear “keep/change/remove” decisions for T104A–T104E scope (with rationale)
- [ ] Mapped follow-on activities (which stream/activity numbers are affected)

#### Activity 2.4: Notes Update (Stream 2 Decision Capture)

**Purpose**: Record decisions and carry-forward items from Stream 2 into the initiative Phase 0 notes.

**Deliverable**: `prompt/artifacts/tasks/T104/workspace/notes/notes_T104-CWS_phase0.md` (update)

---

### Stream 3: SSOT Scaffolding (T104)

**Objective**: Scaffold the T104 initiative SSOT artifacts following initiative setup standards

#### Activity 3.1: Draft `sps_T104-CWS.md` Skeleton (incl. SPS III.A)

**Purpose**: Create the T104 initiative SSOT scaffold following the structural intent of `sps_T102-CONSULTANT.md`.

**Deliverable**: `prompt/artifacts/tasks/T104/ssot/sps_T104-CWS.md`

**Task List**:
1. Establish the SPS identity, governance baseline placeholders, and epic register for T104A–T104E.
2. Draft SPS **Section III.A** (Problem Definition) to define high-level problem framing and desired outcome for this initiative (no solutions).
3. Include a Governance & Roadmap snapshot section that links to this roadmap without importing operational detail.
4. Include explicit references to governing T102 ADRs where required (link, don’t duplicate).

#### Activity 3.2: Draft `concept_T104-CWS.md` Skeleton

**Purpose**: Create the T104 concept SSOT scaffold following the decision-system intent of `concept_T102-CONSULTANT.md`.

**Deliverable**: `prompt/artifacts/tasks/T104/ssot/concept_T104-CWS.md`

**Task List**:
1. Establish ADR index placeholders aligned to the T102 decision record standards.
2. Prepare placeholders for T104-specific ADRs that will define artifact role boundaries and changelog standards.

---

### Stream 4: Epic Scaffolds (A–E)

#### Activity 4.1: Add Epic Register (T104A–T104E) into SPS

**Purpose**: Declare the epic map for T104 so downstream work is traceable and governance-driven.

**Deliverable**: `prompt/artifacts/tasks/T104/ssot/sps_T104-CWS.md` (Epic register section)

#### Activity 4.2: Define Epic Artifact Responsibilities (A–E)

**Purpose**: Make it explicit what each epic must deliver (and what it must not) to prevent role overlap.

**Deliverable**: `prompt/artifacts/tasks/T104/ssot/sps_T104-CWS.md` (epic dossier placeholders)

---

### Stream 5: Artifact Role Standards

#### Activity 5.1: Define Notes vs Changelog Semantics

**Purpose**: Eliminate ambiguity between “execution record” (notes) and “artifact version delta” (changelog).

**Deliverable**: T104 standard statements referenced by SSOT (location to be decided during Stream 3).

#### Activity 5.2: Define Naming + Prefix Policy (T104)

**Purpose**: Prevent file-prefix drift and collisions across artifact types.

**Deliverable**: T104 naming standard statement(s), including:
- `roadmap_...`
- `proposal_...`
- `notes_...`
- `analysis_...`
- `changelog_<artifact>_...`

#### Activity 5.3: Define Minimum Changelog Standard (T104E)

**Purpose**: Define (only) what “good changelog” means for T104 artifacts (schema, minimum entries, scope, and non-goals).

**Deliverable**: Changelog standard statement(s) (no bulk migrations in Phase 0).

---

### Stream 6: Template Alignment (Parallel Standardization)

**Objective**: Ensure the roadmap template reflects the canonical Phase/Stream/Activity structure and includes the dependency notation standard (so parallel streams/activities are explicit and consistent).

#### Activity 6.1: Plan Updates to `workspace_documentation_rules.md`

**Purpose**: Define the required deltas so later edits are surgical and traceable.

**Deliverable**: Delta checklist recorded in this roadmap (do not implement here).

#### Activity 6.2: Update `template_workspace_roadmap.md` (Dependency Notation + Structure)

**Purpose**: Ensure the roadmap template yields the canonical Phase/Stream/Activity/Task structure and dependency notation standard (parallel streams/activities).

**Deliverable**: `prompt/templates/consultant/workspace/template_workspace_roadmap.md` (update)

---

### Stream 7: Validation & Handoff

#### Activity 7.1: Validate Internal References + Readiness

**Purpose**: Confirm all links, naming, and contracts are consistent and ready for Phase 1 execution.

**Deliverable**: Validation outcomes recorded in this roadmap.

---

## IV. LINKS REGISTER

| Link Type | Target | Path |
|:----------|:-------|:-----|
| Roadmap (this file) | T104 Phase 0 Roadmap | `prompt/artifacts/tasks/T104/workspace/roadmap/roadmap_T104-CWS_phase0.md` |
| Notes | T104 Phase 0 Notes | `prompt/artifacts/tasks/T104/workspace/notes/notes_T104-CWS_phase0.md` |
| Changelog | Roadmap Changelog | `prompt/artifacts/tasks/T104/workspace/roadmap/changelog_roadmap_T104-CWS_phase0.md` |
| Research (target) | T104-RES-001 Brief | `prompt/artifacts/tasks/T104/research/brief/brief_T104-RES-001_agentic-workspace-assessment.md` |
| Research (target) | T104-RES-001 Report | `prompt/artifacts/tasks/T104/research/report/report_T104-RES-001_agentic-workspace-assessment.md` |
| Analysis (target) | T104-RES-001 Synthesis | `prompt/artifacts/tasks/T104/workspace/analysis/analysis_T104-RES-001_agentic-workspace-assessment.md` |
| SSOT (target) | T104 SPS | `prompt/artifacts/tasks/T104/ssot/sps_T104-CWS.md` |
| SSOT (target) | T104 Concept | `prompt/artifacts/tasks/T104/ssot/concept_T104-CWS.md` |
| Exemplar (read-only) | T102 SPS | `prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md` |
| Exemplar (read-only) | T102 Concept | `prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md` |
| Exemplar (read-only) | T104A Roadmap | `prompt/artifacts/tasks/T104/T104A/workspace/roadmap/roadmap_T104A-ROADMAP_phase0.md` |
| Governance Rules | Workspace Rules | `prompt/templates/consultant/workspace/workspace_documentation_rules.md` |
| Roadmap Template | Template | `prompt/templates/consultant/workspace/template_workspace_roadmap.md` |

---

## V. OPEN QUESTIONS REGISTER

| ID | Topic | Question | Owner | Status | Proposed Date | Resolved Date |
|:---|:------|:---------|:------|:-------|:--------------|:-------------|
| OQ-001 | SSOT Authoring Scope | Should Phase 0 author T104-specific ADRs immediately, or keep placeholders only until Phase 1? | Client | Proposed | 2026-01-17 | — |
| OQ-002 | Notes Template | Should T104B define a `template_workspace_notes.md`, or reuse the existing log template pattern with renamed semantics? | Client | Proposed | 2026-01-17 | — |
| OQ-003 | Research Scope | Confirm whether T104-RES-001 should include recommendations about renaming existing T104A artifacts (or remain “forward-only” guidance). | Client | Proposed | 2026-01-17 | — |

---

## VI. CHANGELOG

`prompt/artifacts/tasks/T104/workspace/roadmap/changelog_roadmap_T104-CWS_phase0.md`
