---
artifact_type: 'ROADMAP'
initiative_id: 'T104'
epic_id: 'T104A'
epic_code: 'ROADMAP'
phase: '0'
version: '1.1.0'
date: '2026-01-16'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
governance_rules: 'prompt/templates/consultant/workspace/workspace_documentation_rules.md'
template_reference: 'prompt/templates/consultant/workspace/template_workspace_roadmap.md'
reference_exemplar_1: 'prompt/artifacts/tasks/T102/consultant/workspace/plan/T102B/plan_T102B-REQUEST_phase0.md'
reference_exemplar_2: 'prompt/artifacts/tasks/T801/consultant/workspace/plan/plan_T801A_phase0-1.md'
---

# ROADMAP: T104A (ROADMAP) — Phase 0: ROADMAP STANDARDIZATION

## I. EXECUTIVE SUMMARY

**Purpose**: Establish a standardized **workspace roadmap system** for `LLM_Consultant` work across multiple artifact types and directory structures, starting with a canonical ROADMAP structure and governance rules.

**Phase 0 Objective**: Define and implement the **ROADMAP standard** (structure + terminology + registers + heading rules) and use it to drive subsequent updates to:
- `prompt/templates/consultant/workspace/template_workspace_roadmap.md` (template refactor; will remain a template file, but standardized as a ROADMAP structure)
- `prompt/templates/consultant/workspace/workspace_documentation_rules.md` (governance rules update: Roadmap/Proposal/Log boundaries)

**Key Standard Decisions (locked)**:
- **Naming prefix**: `roadmap_` is the standard (replaces `plan_` going forward for T104 artifacts).
- **Artifact type**: YAML `artifact_type: 'ROADMAP'` (new).
- **Terminology**: **Phase → Stream → Activity → Task** (no “Subphase” in the standard).
- **Heading rule**: `###` is reserved for **Stream**; `####` is reserved for **Activity**.
- **Governance link**: reference `prompt/templates/consultant/workspace/workspace_documentation_rules.md` (do not use non-existent `T810` paths).
- **Execution history**: `log_...` replaces `completion_...` (Phase 0 defines the rules; template updates come later).
- **Constraint**: Do not modify `prompt/templates/consultant/workspace/template_workspace_log.md` in Phase 0.

**Role Boundaries**:
- `LLM_Consultant`: defines standards, authors roadmap/rules/templates, prepares handoff guidance
- `Client`: approval authority for standard decisions and final Phase 0 deliverables
- `T102B-Consultant`: downstream adopter (applies standardization to `plan_T102B` after T104 outputs are delivered)

**Phase 0 Exit Milestone**: **Roadmap Standard Ready**
- Canonical ROADMAP structure defined and validated
- Template + governance rules updates completed (as described in Streams 4 and 5)
- Handoff guidance prepared for downstream standardization work (T102B)

---

## II. CONTEXT MATERIALS & PREREQUISITES

**Primary targets for Phase 0 (to be modified later in this roadmap)**:
- `prompt/templates/consultant/workspace/template_workspace_roadmap.md`
- `prompt/templates/consultant/workspace/workspace_documentation_rules.md`

**Reference exemplars (read-only; do not modify as part of T104)**:
- `prompt/artifacts/tasks/T102/consultant/workspace/plan/T102B/plan_T102B-REQUEST_phase0.md`
- `prompt/artifacts/tasks/T801/consultant/workspace/plan/plan_T801A_phase0-1.md`

**Deferred (explicitly out of scope for Phase 0 changes)**:
- `prompt/templates/consultant/workspace/template_workspace_log.md` (do not edit in Phase 0)

---

## III. PHASE 0: STANDARDIZATION DELIVERY ROADMAP

**Objective**: Deliver Phase 0 outputs that standardize Roadmap structure and governance, enabling consistent consultant workflows and downstream adoption by other initiatives (e.g., T102B).

**Scope Constraint**: This ROADMAP file is the only artifact to be created immediately; modifications to templates/rules are planned as activities and executed later per this roadmap.

**Stream Register**

| Stream | Name | Objective | Status | Owner | Start | Target | Completion | Key Deliverables |
|:------|:-----|:----------|:-------|:------|:------|:-------|:-----------|:----------------|
| 1 | Initialization & Scope Lock | Initialize this roadmap and lock Phase 0 scope + decisions | In Progress | LLM_Consultant | 2026-01-15 | 2026-01-15 | — | `roadmap_T104A-ROADMAP_phase0.md` |
| 2 | Baseline Audit (Reference-Only) | Extract patterns + gaps from exemplars and templates | Planned | LLM_Consultant | — | — | — | Baseline findings (in this roadmap) |
| 3 | Roadmap Standard Definition | Define canonical Phase/Stream/Activity/Task structure and registers | Planned | LLM_Consultant | — | — | — | Standard spec (referenced in rules/template) |
| 4 | Template Refactor | Update `template_workspace_roadmap.md` to canonical ROADMAP structure | Planned | LLM_Consultant | — | — | — | Updated template |
| 5 | Governance Rules Update | Update `workspace_documentation_rules.md` to Roadmap/Proposal/Log | Planned | LLM_Consultant | — | — | — | Updated governance rules |
| 6 | Validation & Handoff | Validate consistency and prepare adoption guidance for T102B | Planned | LLM_Consultant | — | — | — | Validation checklist + handoff notes (in this roadmap) |

---

**Activity Register**

| Stream | Activity ID | Title | Deliverable | Status | Owner | Start | Target | Completion |
|:-------|:------------|:------|:------------|:-------|:------|:------|:-------|:-----------|
| 1 | 1.1 | **Initialize Phase 0 Roadmap File** | Create `roadmap_T104A-ROADMAP_phase0.md` | In Progress | LLM_Consultant | 2026-01-15 | 2026-01-15 | — |
| 1 | 1.2 | **Confirm T104 Adoption + Directory Scope** | Updated Stream Register + Open Questions | Planned | LLM_Consultant | — | — | — |
| 2 | 2.1 | **Audit plan_T102B Structure (Reference Only)** | Baseline Findings (Section 2.A) | Planned | LLM_Consultant | — | — | — |
| 2 | 2.2 | **Audit plan_T801A Structure (Reference Only)** | Baseline Findings (Section 2.B) | Planned | LLM_Consultant | — | — | — |
| 2 | 2.3 | **Audit Template + Rules Mismatch** | Gap List (Section 2.C) | Planned | LLM_Consultant | — | — | — |
| 3 | 3.1 | **Define ROADMAP Minimum Required Sections** | Standard Definition (Section 3.A) | Planned | LLM_Consultant | — | — | — |
| 3 | 3.2 | **Define Register Schemas (Stream + Activity)** | Standard Definition (Section 3.B) | Planned | LLM_Consultant | — | — | — |
| 3 | 3.3 | **Define Artifact Boundaries (Roadmap / Proposal / Log)** | Standard Definition (Section 3.C) | Planned | LLM_Consultant | — | — | — |
| 4 | 4.1 | **Replace “Subphase” with “Stream”** | Updated template | Planned | LLM_Consultant | — | — | — |
| 4 | 4.2 | **Enforce ### = Stream and #### = Activity** | Updated template | Planned | LLM_Consultant | — | — | — |
| 4 | 4.3 | **Add Stream Register + Date Columns** | Updated template | Planned | LLM_Consultant | — | — | — |
| 4 | 4.4 | **Remove Competing Patterns** | Updated template | Planned | LLM_Consultant | — | — | — |
| 5 | 5.1 | **Update Artifact Roles (Roadmap / Proposal / Log)** | Updated rules | Planned | LLM_Consultant | — | — | — |
| 5 | 5.2 | **Update Heading Conventions** | Updated rules | Planned | LLM_Consultant | — | — | — |
| 5 | 5.3 | **Register Date Columns Requirement** | Updated rules | Planned | LLM_Consultant | — | — | — |
| 6 | 6.1 | **Validation Against Repo Reality** | Validation notes (in this roadmap) | Planned | LLM_Consultant | — | — | — |
| 6 | 6.2 | **Downstream Adoption Guidance (T102B Consultant)** | Handoff notes (in this roadmap) | Planned | LLM_Consultant | — | — | — |

---

### Stream 1: Initialization & Scope Lock

**Objective**: Initialize the Phase 0 ROADMAP and lock the scope boundaries and naming/structure decisions that govern all later streams.

**Hard Gate**: Stream 2 MUST NOT start until Stream 1 Activity 1.1 is complete (roadmap exists and is structurally compliant).

#### Activity 1.1: Initialize Phase 0 Roadmap File

**Purpose**: Create the canonical Phase 0 roadmap artifact that drives all subsequent standardization work.

**Deliverable**: `prompt/artifacts/tasks/T104/T104A/ssot/roadmap_T104A-ROADMAP_phase0.md`

**Inputs Required**:
- Governance rules reference: `prompt/templates/consultant/workspace/workspace_documentation_rules.md`
- Template reference: `prompt/templates/consultant/workspace/template_workspace_roadmap.md`
- Read-only exemplars: `plan_T102B-REQUEST_phase0.md`, `plan_T801A_phase0-1.md`

**Task List**:
1. Create roadmap file with YAML `artifact_type: 'ROADMAP'` and Phase 0 metadata.
2. Define Phase 0 streams and activities (Stream/Activity/Task structure).
3. Include Stream Register + Activity Register (Phase 0) with Start/Target/Completion columns and Stream column.
4. Capture scope constraints and deferred items explicitly.

**Success Criteria Checklist**:
- [ ] File exists at the target path and is readable
- [ ] Uses **Phase → Stream → Activity → Task** terminology (no “Subphase”)
- [ ] `###` headings used only for **Stream**
- [ ] `####` headings used only for **Activity**
- [ ] Stream Register present with Start/Target/Completion columns
- [ ] Activity Register includes a Stream column

#### Activity 1.2: Confirm T104 Adoption + Directory Scope

**Purpose**: Lock the directory naming rule change scope to T104 only and avoid accidental global folder renames.

**Deliverable**: Updated Stream Register rows (4/5/6) and Open Questions section (Section V).

**Task List**:
1. Confirm T104-only directory naming rule: `workspace/roadmap/` folder is standard within T104.
2. Confirm no changes to non-T104 directory naming patterns (out of scope).
3. Confirm Phase 0 does not touch `template_workspace_log.md`.

**Success Criteria Checklist**:
- [ ] “T104-only directory rename” constraint is explicitly stated and unambiguous
- [ ] Phase 0 exclusions are explicitly stated (no log template edits)

---

### Stream 2: Baseline Audit (Reference-Only)

**Objective**: Extract what works and what breaks across current exemplars/templates so the new ROADMAP standard is grounded in repo reality.

#### Activity 2.1: Audit `plan_T102B` Structure (Reference Only)

**Purpose**: Identify which structures are worth standardizing and which are “initiative-specific”.

**Task List**:
1. Extract the minimal repeatable ROADMAP pattern (registers, gates, deliverable tables).
2. Identify drift risks (e.g., duplicate checklists) to avoid encoding into the standard.
3. Record findings in this roadmap (Stream 2 Baseline Findings).

**Success Criteria Checklist**:
- [ ] Baseline findings include “adopt / avoid / optional” recommendations
- [ ] No edits performed on the reference exemplar

#### Activity 2.2: Audit `plan_T801A` Structure (Reference Only)

**Purpose**: Reuse stable patterns that are already proven in the repo.

**Task List**:
1. Identify stable activity block patterns and register usage.
2. Identify what is too verbose/initiative-specific to standardize.

**Success Criteria Checklist**:
- [ ] Baseline findings include reusable structural patterns
- [ ] No edits performed on the reference exemplar

#### Activity 2.3: Audit Template + Rules Mismatch

**Purpose**: Identify where templates currently produce non-standard or ambiguous structures.

**Task List**:
1. List competing structures inside `template_workspace_roadmap.md` that must be removed.
2. Identify rule conflicts (e.g., heading hierarchy vs desired `####` for Activity).
3. Produce a concrete “delta checklist” for Streams 4 and 5.

**Success Criteria Checklist**:
- [ ] A single canonical structure is clearly defined as the target end state
- [ ] Each mismatch has a mapped fix location (template vs rules)

---

### Stream 3: Roadmap Standard Definition

**Objective**: Define the canonical ROADMAP structure (Phase/Stream/Activity/Task), required registers, status vocabulary, and scope boundaries between Roadmap/Proposal/Log.

#### Activity 3.1: Define ROADMAP Minimum Required Sections

**Task List**:
1. Define required sections: Executive Summary, Context, Phase section, Links Register, Open Questions, Changelog.
2. Define what is explicitly forbidden in a Roadmap (e.g., full RID/DR bodies; long narrative execution logs).

**Success Criteria Checklist**:
- [ ] Required sections list is complete and unambiguous
- [ ] Forbidden content list prevents Roadmap drift into Proposal/Log territory

#### Activity 3.2: Define Register Schemas (Stream + Activity)

**Task List**:
1. Define Stream Register schema and required columns.
2. Define Activity Register schema and required columns.
3. Ensure Activity Register includes a Stream column.
4. Define status vocabulary (recommended: Planned / In Progress / Complete / Blocked / Deferred).

**Success Criteria Checklist**:
- [ ] Both register schemas include Start/Target/Completion columns
- [ ] Status vocabulary is short and consistent

#### Activity 3.3: Define Artifact Boundaries (Roadmap / Proposal / Log)

**Task List**:
1. Define the “single source of truth” for normative specs (Proposal/Request).
2. Define what Log captures (decisions + minutes + next-session guidance) and what it must not capture (full spec bodies).
3. Define Roadmap’s role (gates + ordering + deliverables) with minimal narrative.

**Success Criteria Checklist**:
- [ ] Boundary rules are written as “MUST / MUST NOT” statements
- [ ] Log replaces Completion explicitly in the rules (but log template remains unchanged in Phase 0)

---

### Stream 4: Template Refactor (Deferred Implementation)

**Objective**: Update `template_workspace_roadmap.md` so it generates a canonical ROADMAP structure (single pattern; no competing variants).

#### Activity 4.1: Replace “Subphase” with “Stream”

**Target**: `prompt/templates/consultant/workspace/template_workspace_roadmap.md`

**Success Criteria Checklist**:
- [ ] Template uses Stream terminology consistently (no “Subphase”)

#### Activity 4.2: Enforce `###` = Stream and `####` = Activity

**Success Criteria Checklist**:
- [ ] Template never uses `####` for anything other than Activity
- [ ] Registers and sub-sections use bold labels instead of headings

#### Activity 4.3: Add Stream Register + Date Columns

**Success Criteria Checklist**:
- [ ] Stream Register present in template
- [ ] Activity Register schema includes Start/Target/Completion

#### Activity 4.4: Remove Competing Patterns

**Success Criteria Checklist**:
- [ ] Template provides a single canonical Phase/Stream/Activity/Task pattern

---

### Stream 5: Governance Rules Update (Deferred Implementation)

**Objective**: Update governance rules to reflect **Roadmap / Proposal / Log** and the Phase/Stream/Activity/Task + heading conventions.

#### Activity 5.1: Update Artifact Roles (Roadmap / Proposal / Log)

**Target**: `prompt/templates/consultant/workspace/workspace_documentation_rules.md`

**Success Criteria Checklist**:
- [ ] Rules define Roadmap/Proposal/Log without overlap
- [ ] Rules explicitly state: log replaces completion

#### Activity 5.2: Update Heading Conventions

**Success Criteria Checklist**:
- [ ] Rules enforce `###` reserved for Stream and `####` reserved for Activity
- [ ] Rules describe how to represent Tasks (lists inside Activity)

#### Activity 5.3: Register Date Columns Requirement

**Success Criteria Checklist**:
- [ ] Rules require Start/Target/Completion for Stream + Activity registers

---

### Stream 6: Validation & Handoff (Deferred Implementation)

**Objective**: Validate the new standard is usable, and prepare guidance for downstream adoption (e.g., T102B consultant updates).

#### Activity 6.1: Validation Against Repo Reality

**Task List**:
1. Confirm the canonical ROADMAP template can represent Phase/Stream/Activity/Task patterns and can map legacy “Subphase” groupings into Streams where needed (without special cases).
2. Confirm date columns and status vocabulary remain usable and non-noisy.

**Success Criteria Checklist**:
- [ ] Validation notes list any residual mismatches and the recommended resolution

#### Activity 6.2: Downstream Adoption Guidance (T102B Consultant)

**Task List**:
1. Provide a short “migration checklist” for converting plan-like files to roadmap structure.
2. Clarify what is *not* required (avoid churn) vs what is mandatory (headings/registers/links).

**Success Criteria Checklist**:
- [ ] Handoff notes are actionable and minimize downstream rework

---

## IV. LINKS REGISTER

| Link Type | Target | Path |
|:----------|:-------|:-----|
| Roadmap (this file) | T104A Phase 0 | `prompt/artifacts/tasks/T104/T104A/ssot/roadmap_T104A-ROADMAP_phase0.md` |
| Log | Roadmap Log | `prompt/artifacts/tasks/T104/T104A/workspace/roadmap/log_roadmap_T104A-ROADMAP_phase0.md` |
| Changelog | Roadmap Changelog | `prompt/artifacts/tasks/T104/T104A/archive/changelog_roadmap_T104A-ROADMAP_phase0.md` |
| Workspace Rules | Governance Rules | `prompt/templates/consultant/workspace/workspace_documentation_rules.md` |
| Workspace Template | Plan/Roadmap Template | `prompt/templates/consultant/workspace/template_workspace_roadmap.md` |
| Reference Exemplar | T102B Phase 0 Plan (read-only) | `prompt/artifacts/tasks/T102/consultant/workspace/plan/T102B/plan_T102B-REQUEST_phase0.md` |
| Reference Exemplar | T801A Phase 0-1 Plan (read-only) | `prompt/artifacts/tasks/T801/consultant/workspace/plan/plan_T801A_phase0-1.md` |

---

## V. OPEN QUESTIONS REGISTER

| ID | Topic | Question | Owner | Status | Proposed Date | Resolved Date |
|:---|:------|:---------|:------|:-------|:--------------|:-------------|
| OQ-001 | Epic Code | Confirm `epic_code` for T104A should be `CWF` (or another token) | Client | Proposed | 2026-01-15 | — |
| OQ-002 | Status Vocabulary | Confirm the canonical status set (Planned/In Progress/Complete/Blocked/Deferred) | Client | Proposed | 2026-01-15 | — |
| OQ-003 | T104-only Directory Rule | Confirm whether only folder names change for T104 (no repo-wide folder refactors) | Client | Proposed | 2026-01-15 | — |

---

## VI. CHANGELOG

`prompt/artifacts/tasks/T104/T104A/archive/changelog_roadmap_T104A-ROADMAP_phase0.md`
