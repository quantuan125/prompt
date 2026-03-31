---
artifact_type: 'IMPLEMENTATION'
implementation_type: 'task_specification'
initiative_id: 'T102'
initiative_code: 'CWD'
phase: '1'
stream_id: 'T102-PH001-ST002'
activity_id: 'T102-PH001-ST002-AC000'
task_id: 'T102-PH001-ST002-AC000-TK010.6'
version: '1.0.0'
date: '2026-03-31'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/plan_T102-PH001-ST002-AC000.md'
execution_audience: 'assistant'
purpose: 'Gate-001 closure, downstream activation, and AC001 activity plan creation — delegated to a consultant-commissioned assistant executor after client approval of GATE-001.'
---

# IMPLEMENTATION (Task Specification): AC000 TK010.6 Gate-001 Closure And Downstream Activation

## I. PURPOSE & AUTHORITY

- Purpose: Formalize the exact file mutations required to close `GATE-001` with the client's `APPROVE` decision, unblock the AC000 downstream implementation path, activate AC001 at the stream level, and author the first-draft AC001 activity plan — so that TK011 execution and AC001 substantive work can each begin in separate downstream sessions.
- Authority chain: Client approves GATE-001 (SES005, 2026-03-31) → AC000 plan authorizes `TK010.6` → this artifact specifies HOW the gate closure, downstream unblocking, and AC001 activation are performed → a consultant-commissioned assistant executor performs the work on the main consultant's behalf.
- Audience: `LLM_Assistant` acting on the `LLM_Consultant`'s behalf. The executor MUST treat this artifact as the single authoritative specification for all mutations in scope. If any step is ambiguous or the target file's current state does not match the preconditions stated here, the executor MUST stop and escalate to the main consultant rather than inferring.
- This artifact does NOT hold a GDR. The gate decision is recorded in the proposal artifact per `guideline_workspace_proposal.md` §VII.
- This artifact does NOT authorize execution of `TK011` (STD-004 mutations) or any AC001 substantive tasks. Those are deferred to separate sessions.

## II. TASK SCOPE

- Governing plan task: `T102-PH001-ST002-AC000-TK010.6`
- Trigger: Client records `APPROVE` for GATE-001 (SES005, 2026-03-31). The recycle loop (TK010.1-TK010.5) is complete, the fresh external review (TK010.4) and proposal refresh (TK010.5) have been accepted, and the client has approved all four GIR dispositions at option (a).
- Deliverable contract:
  1. Recorded GDR in the Gate-001 proposal
  2. Updated AC000 plan with GATE-001 closed and TK010.6 registered
  3. TK011 unblocked (status changed to `ready`)
  4. First-draft AC001 activity plan created per `template_workspace_plan_activity.md`
  5. ST002 stream plan updated with AC001 activation and plan link

## III. SPECIFICATION ITEMS

### SPEC-001 — Record the GATE-001 GDR decision in the proposal

| Field | Detail |
|:--|:--|
| Requirement Source | Client GATE-001 approval decision (SES005, 2026-03-31) |
| Target file(s) | `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/proposal/proposal_T102-PH001-ST002-AC000_gate-001-disposition.md` |
| Required end-state posture | The GDR table in §VI reflects the client's approving decision with all fields populated. The four GIR disposition checkboxes in §III each show option `(a)` selected. The proposal version is bumped. |
| Explicit non-target / do-not-change constraints | Do NOT modify: §I Executive Summary, §II Gate Package (Index or Evidence Index), §IV Detailed Disposition Register prose, §V Consultant Gate Recommendation, §VII References. Only the GDR table fields, the four GIR checkbox rows in §III, and the §VIII Changelog are changed. |
| Validation check | (1) GDR `Client Decision` is `APPROVE`. (2) GDR `Gate Status After Decision` is `completed`. (3) GDR `Decision Date` is `2026-03-31`. (4) GDR `Decision Reference` is `snotes_T102-PH001-ST002-AC000-SES005.md`. (5) All four GIR rows in §III show `[x] (a)` selected with the other option cleared. (6) Proposal version is bumped to `v1.6.0`. (7) Changelog has a new entry. |
| Blocking ambiguity rule | If the GDR table structure does not match the precondition layout below, stop and escalate. Do not restructure the GDR table. |
| Status | `open` |

#### Implementation Detail

1. Open `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/proposal/proposal_T102-PH001-ST002-AC000_gate-001-disposition.md`.
2. Locate the `## Gate Decision Record` table in §VI. The current state of the table is:

   ```
   | Field | Value |
   |:--|:--|
   | Gate ID | `T102-PH001-ST002-AC000-GATE-001` |
   | Consultant Recommendation | `APPROVE WITH CONDITIONS` |
   | Client Decision | `pending` |
   | Gate Status After Decision | `pending` |
   | Conditions (if any) | `1. TK009 remains historical/outdated evidence only; 2. Immediate next stream-level development step after approval is ST002-AC001-TK001; 3. The separate AC000 implementation-backed path remains blocked until this same gate approval activates TK010 as the bounded execution contract for TK011-TK015; 4. Any further remediation beyond this package requires later client approval after consultant assessment.` |
   | Decided By | `Client` |
   | Decision Date | `YYYY-MM-DD` |
   | Decision Reference | `pending` |
   ```

3. Replace the four mutable fields with these exact values:
   - `Client Decision` → `APPROVE`
   - `Gate Status After Decision` → `completed`
   - `Decision Date` → `2026-03-31`
   - `Decision Reference` → `snotes_T102-PH001-ST002-AC000-SES005.md`

4. Leave all other GDR fields unchanged (Gate ID, Consultant Recommendation, Conditions, Decided By).

5. Locate the four GIR rows in §III (Disposition Summary Register). Each row currently shows:
   ```
   | GIR-001 | ... | `[ ] (a)` / `[ ] (b)` |
   ```
   Replace the `Client Decision` cell for each of the four GIR rows:
   - GIR-001: `[x] (a)` 
   - GIR-002: `[x] (a)` 
   - GIR-003: `[x] (a)` 
   - GIR-004: `[x] (a)` 

6. Update the proposal frontmatter:
   - `version` → `'1.6.0'`
   - `date` → `'2026-03-31'`
   - `status` → `'completed'`

7. Append to the §VIII Changelog table:

   ```
   | v1.6.0 | 2026-03-31 | Amendment | Recorded the client APPROVE decision for GATE-001. All four GIR dispositions accepted at option (a). GDR fields populated with decision date 2026-03-31 and reference to SES005 session notes. Proposal status changed to completed. |
   ```

---

### SPEC-002 — Amend AC000 plan to register TK010.6 and update GATE-001 to completed

| Field | Detail |
|:--|:--|
| Requirement Source | Client-commissioned post-gate closure task (SES005, 2026-03-31) |
| Target file(s) | `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/plan_T102-PH001-ST002-AC000.md` |
| Required end-state posture | (1) TK010.6 appears as a new registered task row in the Task Register, positioned after TK010.5 and before GATE-001. (2) GATE-001 row status is updated to `completed`. (3) A new detailed section for TK010.6 appears in §III after the TK010.5 section and before the GATE-001 section. (4) The GATE-001 detailed section's Gate Status in the Recycle Re-entry Block is updated to reflect the completed gate. (5) Plan version is bumped. |
| Explicit non-target / do-not-change constraints | Do NOT modify: any TK000-TK010.5 detailed sections, TK011-TK015 detailed sections, GATE-002 section, §IV Links Register. Only the Task Register, the new TK010.6 detailed section, the GATE-001 Recycle Re-entry Block `Gate Status` field, the plan frontmatter version/date, and the §V Changelog are changed. |
| Validation check | (1) Task Register contains a TK010.6 row between TK010.5 and GATE-001. (2) TK010.6 row shows `completed`, owner `LLM_Assistant`, depends on `GATE-001`. (3) GATE-001 row shows `completed`. (4) TK010.6 detailed section exists in §III. (5) GATE-001 Recycle Re-entry Block `Gate Status` is `completed`. (6) Plan version is `v2.8.0`. (7) Changelog has a new entry. |
| Blocking ambiguity rule | If the Task Register row count or column schema does not match the expected 9-column format (`Task | Task ID | Name | Status | Owner | Depends On | Target | Reference | Action`), stop and escalate. |
| Status | `open` |

#### Implementation Detail

1. Open `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/plan_T102-PH001-ST002-AC000.md`.

2. **Task Register amendment** — Locate the Task Register table in §II. Insert the following new row immediately after the TK010.5 row and before the GATE-001 row:

   ```
   | TK010.6 | `T102-PH001-ST002-AC000-TK010.6` | Execute GATE-001 closure, downstream activation, and AC001 plan creation | `completed` | LLM_Assistant | GATE-001 | AC000 plan + proposal + ST002 stream plan + new AC001 plan | `implementation/implementation_T102-PH001-ST002-AC000_tk010.6_gate-001-closure-and-downstream-activation-task-specification.md` | GATE-001 GDR recorded as APPROVE; TK011 unblocked; AC001 activity plan created; ST002 stream plan updated. |
   ```

3. **GATE-001 Task Register row update** — In the same Task Register, locate the GATE-001 row. Change:
   - `Status` from `` `in_progress` `` to `` `completed` ``
   - `Action` from the current value to: `Client approved GATE-001 (APPROVE) on 2026-03-31. All four GIR dispositions accepted at option (a). TK010 activated as bounded downstream execution contract for TK011-TK015.`

4. **New TK010.6 detailed section** — In §III (Tasks Detailed), insert the following new section. Place it immediately after the existing `### Task TK010.5` section and before the `### GATE-001` section:

   ```markdown
   ### Task TK010.6: Execute GATE-001 Closure, Downstream Activation, and AC001 Plan Creation

   **Task ID**: `T102-PH001-ST002-AC000-TK010.6`

   **Purpose**: Perform the post-approval administrative work to close GATE-001, unblock the AC000 downstream implementation path, activate AC001 at the stream level, and author the first-draft AC001 activity plan. This task is delegated to a consultant-commissioned assistant executor.

   **Deliverable**:
   - Recorded GDR in the Gate-001 proposal (APPROVE)
   - Updated AC000 plan with GATE-001 closed and TK010.6 registered
   - TK011 unblocked (status changed to `ready`)
   - First-draft AC001 activity plan at `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC001/plan_T102-PH001-ST002-AC001.md`
   - Updated ST002 stream plan with AC001 status and plan link

   **Scope**:
   - In scope: GDR recording; plan register updates; AC001 directory creation and first-draft plan authoring; stream-plan activation update
   - Out of scope: TK011 execution (STD-004 mutations); AC001 substantive task execution; any guideline edits

   **Inputs Required**:
   - `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/implementation/implementation_T102-PH001-ST002-AC000_tk010.6_gate-001-closure-and-downstream-activation-task-specification.md` — this governing specification
   - `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/proposal/proposal_T102-PH001-ST002-AC000_gate-001-disposition.md` — GDR target
   - `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/analysis/analysis_T102-PH001-ST002-AC000_calibrated-scope-brief.md` — AC001 focus input
   - `prompt/templates/consultant/workspace/template_workspace_plan_activity.md` — AC001 plan template
   - `prompt/templates/consultant/workspace/guideline_workspace_plan.md` — plan authoring rules

   **Steps**:
   1. Execute per `implementation_T102-PH001-ST002-AC000_tk010.6_gate-001-closure-and-downstream-activation-task-specification.md` SPEC-001 through SPEC-006 in the specified sequence.

   **Success Criteria**:
   - [ ] GDR records APPROVE with decision date 2026-03-31
   - [ ] GATE-001 status is `completed` in the AC000 plan
   - [ ] TK011 status is `ready` in the AC000 plan
   - [ ] AC001 activity plan exists at the specified path
   - [ ] ST002 stream plan shows AC001 as `ready` with plan link
   ```

5. **GATE-001 Recycle Re-entry Block update** — In the GATE-001 detailed section, locate the `Recycle Re-entry Block`. Change the `**Gate Status**` field from `` `in_progress` `` to `` `completed` ``.

6. **Plan frontmatter update**:
   - `version` → `'2.8.0'`
   - `date` → `'2026-03-31'`

7. **Changelog entry** — Append to the §V Changelog table:

   ```
   | v2.8.0 | 2026-03-31 | Amendment | Registered TK010.6 (GATE-001 closure, downstream activation, and AC001 plan creation) in the Task Register and detailed sections. Marked GATE-001 as completed after client APPROVE decision on 2026-03-31. Source: client SES005 approval; implementation artifact `implementation_T102-PH001-ST002-AC000_tk010.6_gate-001-closure-and-downstream-activation-task-specification.md`. |
   ```

---

### SPEC-003 — Unblock TK011 in the AC000 plan

| Field | Detail |
|:--|:--|
| Requirement Source | GATE-001 exit criteria: "AC000 post-GATE-001 implementation may begin only through TK011 executing against TK010" |
| Target file(s) | `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/plan_T102-PH001-ST002-AC000.md` |
| Required end-state posture | TK011 Task Register row shows `ready` instead of `blocked`. TK011 detailed section reflects readiness to begin in a separate session. |
| Explicit non-target / do-not-change constraints | Do NOT modify: TK011 detailed section content (Purpose, Deliverable, Scope, Inputs, Steps, Success Criteria). Do NOT modify TK012-TK015 or GATE-002 rows (they remain `blocked` pending TK011 completion). Only the TK011 Task Register `Status` cell and `Action` cell are changed. |
| Validation check | (1) TK011 row `Status` is `` `ready` ``. (2) TK011 row `Action` reflects the unblocking. (3) TK012-TK015 and GATE-002 remain `blocked`. |
| Blocking ambiguity rule | If TK011 row does not currently show `blocked`, stop and escalate — the precondition is not met. |
| Status | `open` |

#### Implementation Detail

1. This SPEC is applied to the same file as SPEC-002 (`plan_T102-PH001-ST002-AC000.md`) and MUST be performed in the same editing pass.

2. Locate the TK011 row in the Task Register. The current state is:
   ```
   | TK011 | `T102-PH001-ST002-AC000-TK011` | Execute implementation per TK010 downstream execution contract | `blocked` | LLM_Developer | GATE-001 | ... | ... | Blocked pending client approval at the same gate, which activates TK010 as the bounded downstream execution contract. |
   ```

3. Change the TK011 row fields:
   - `Status`: from `` `blocked` `` to `` `ready` ``
   - `Action`: from the current blocked text to: `Unblocked by GATE-001 APPROVE (2026-03-31). TK010 is now the active execution contract. Execution deferred to a separate session.`

4. Confirm that TK012 through TK015 and GATE-002 all still show `` `blocked` ``. Do NOT change them.

---

### SPEC-004 — Create AC001 activity directory structure

| Field | Detail |
|:--|:--|
| Requirement Source | Client direction (SES005) to create the AC001 activity plan immediately upon GATE-001 approval |
| Target file(s) | New directory: `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC001/` |
| Required end-state posture | The `AC001/` directory exists under `ST002/` with a valid activity plan file. The directory contains only the plan file at this stage (no `snotes/`, `analysis/`, `implementation/`, etc. directories until AC001 tasks begin producing artifacts). |
| Explicit non-target / do-not-change constraints | Do NOT create subdirectories for artifact types (analysis/, implementation/, etc.) — those are created when AC001 tasks produce artifacts. Do NOT create any files other than the activity plan. |
| Validation check | (1) Directory `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC001/` exists. (2) It contains exactly one file: `plan_T102-PH001-ST002-AC001.md`. (3) No other subdirectories or files exist in the directory. |
| Blocking ambiguity rule | If the `AC001/` directory already exists with content, stop and escalate — the precondition assumes it does not exist. |
| Status | `open` |

#### Implementation Detail

1. Create the directory: `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC001/`
2. The activity plan file is authored in SPEC-005 below and placed in this directory.
3. Do not create any other directories or files.

---

### SPEC-005 — Author the first-draft AC001 activity plan

| Field | Detail |
|:--|:--|
| Requirement Source | Client direction (SES005); `guideline_workspace_plan.md` §IV.D standalone activity plan trigger (>=5 tasks with gate stack); calibrated scope brief §VI.D AC001 focus guidance |
| Target file(s) | New file: `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC001/plan_T102-PH001-ST002-AC001.md` |
| Required end-state posture | A complete first-draft activity plan per `template_workspace_plan_activity.md` that translates the stream-plan AC001 stub into a full activity plan with: (a) four substantive tasks from the existing stream-plan stub expanded with calibrated-scope-brief detail, (b) a consultation-only gate-readiness stack (proposal + external review + gate), (c) proper input references to the AC000 diagnostic outputs, and (d) context listing all relevant files. |
| Explicit non-target / do-not-change constraints | Do NOT begin executing any AC001 tasks. Do NOT create artifact subdirectories. Do NOT modify the calibrated scope brief or any AC000 artifacts (except as specified in other SPEC items). Do NOT add tasks beyond what the stream-plan stub and gate-readiness stack require. |
| Validation check | (1) File exists at specified path. (2) Frontmatter matches the schema below. (3) Task Register contains exactly 7 rows: TK001-TK004 (substantive), TK005 (proposal), TK006 (external review), GATE-001. (4) Each task detailed section includes Purpose, Deliverable, Scope, Inputs Required, Steps, and Success Criteria. (5) GATE-001 section includes Entry Criteria, Reviewer, Exit Criteria, and links to planned proposal/review paths. (6) Changelog has initial entry. |
| Blocking ambiguity rule | If the stream-plan AC001 stub tasks (TK001-TK004) have been materially changed since v2.3.0 of the stream plan, stop and escalate — the task decomposition below assumes the v2.3.0 stub content. If the calibrated scope brief has been amended beyond v1.0.0, stop and escalate — the focus guidance below assumes v1.0.0 content. |
| Status | `open` |

#### Implementation Detail

1. Create the file `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC001/plan_T102-PH001-ST002-AC001.md` with the exact content specified below.

2. **Frontmatter** — Use these exact values:

   ```yaml
   ---
   artifact_type: 'PLAN'
   planning_level: 'ACTIVITY'
   initiative_id: 'T102'
   initiative_code: 'CWD'
   phase: '1'
   stream_id: 'T102-PH001-ST002'
   activity_id: 'T102-PH001-ST002-AC001'
   version: '1.0.0'
   date: '2026-03-31'
   status: 'draft'
   author: 'LLM_Consultant'
   decision_owner_role: 'Client'
   governance_rules: 'prompt/templates/consultant/workspace/workspace_documentation_rules.md'
   parent_plan: 'prompt/artifacts/tasks/T102/workspace/PH001/ST002/plan_T102-PH001-ST002.md'
   ---
   ```

3. **§I Executive Summary** — Use the following content:

   ```markdown
   # PLAN: T102 (CWD) - Phase 1 / Stream ST002 / Activity AC001: STD Adoption & Verification Gap Analysis (Post-Amendment)

   ## I. EXECUTIVE SUMMARY

   **Purpose**: Inventory the post-amendment `T102-STD-001..009` set against `P-STD-001` structural conformance requirements to produce a gap inventory and remediation checklist that AC002-AC004 consume as their primary input. This activity uses AC000's calibrated scope brief as the diagnostic baseline, focusing on residual gaps not already addressed by ST005.

   **Non-goal**: This activity does NOT perform structural remediation (that is downstream execution work governed by separate implementation specifications). It does NOT draft verification contracts (AC002 scope) or modify SSOT artifacts (AC004 scope). It produces the analytical foundation for those activities.
   ```

4. **§II Activity Outline** — Use the following content:

   ```markdown
   ---

   ## II. ACTIVITY OUTLINE

   **Activity ID**: `T102-PH001-ST002-AC001`
   **Objective**: Assess every T102 standard against P-STD-001 structural conformance requirements using the AC000 calibrated scope brief as the diagnostic baseline, flag remaining adoption/verification gaps not addressed by ST005, verify post-migration structural integrity, and identify surviving legacy references — producing a prioritized gap inventory and remediation checklist.
   **Execution Mode**: SEQUENTIAL
   **Depends On**: AC000 (GATE-001 approved 2026-03-31)

   **Context**:
   - `prompt/artifacts/tasks/T102/standard/standard_T102-STD-001_consultancy-operating-model.md`
   - `prompt/artifacts/tasks/T102/standard/standard_T102-STD-002_canonical-yaml-header.md`
   - `prompt/artifacts/tasks/T102/standard/standard_T102-STD-003_explicit-inheritance-model.md`
   - `prompt/artifacts/tasks/T102/standard/standard_T102-STD-004_specification-standard-and-guideline.md`
   - `prompt/artifacts/tasks/T102/standard/standard_T102-STD-005_id-specification-rules.md`
   - `prompt/artifacts/tasks/T102/standard/standard_T102-STD-006_research-artifacts-index.md`
   - `prompt/artifacts/tasks/T102/standard/standard_T102-STD-007_issues-risks-index.md`
   - `prompt/artifacts/tasks/T102/standard/standard_T102-STD-008_organisation-baseline-index.md`
   - `prompt/artifacts/tasks/T102/standard/standard_T102-STD-009_governance-standards-specification.md`
   - `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md`
   - `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/analysis/analysis_T102-PH001-ST002-AC000_calibrated-scope-brief.md`
   - `prompt/artifacts/tasks/T102/ssot/sps_T102-CONSULTANT.md`
   - `prompt/artifacts/tasks/T102/ssot/concept_T102-CONSULTANT.md`

   ### Task Register

   | Task | Task ID | Name | Status | Owner | Depends On | Target | Reference | Action |
   |:--|:--|:--|:--|:--|:--|:--|:--|:--|
   | TK001 | `T102-PH001-ST002-AC001-TK001` | P-STD-001 structural conformance deep-dive (all T102-STDs) | `planned` | LLM_Consultant | — | All `standard_T102-STD-*.md` files | AC000 calibrated scope brief §V.B | — |
   | TK002 | `T102-PH001-ST002-AC001-TK002` | Residual adoption/verification gap inventory (post-ST005) | `planned` | LLM_Consultant | TK001 | All `standard_T102-STD-*.md` files | AC000 calibrated scope brief §VI.D | — |
   | TK003 | `T102-PH001-ST002-AC001-TK003` | Post-migration structural integrity verification (ST003-migrated STDs) | `planned` | LLM_Consultant | TK001 | `STD-001`, `STD-003`, `STD-006`, `STD-007` | ST005 plan | — |
   | TK004 | `T102-PH001-ST002-AC001-TK004` | Legacy GDR/ADR-model reference identification | `planned` | LLM_Consultant | TK001 | All `standard_T102-STD-*.md` files | AC000 calibrated scope brief | — |
   | TK005 | `T102-PH001-ST002-AC001-TK005` | Produce GATE-001 gate-disposition proposal | `planned` | LLM_Consultant | TK004 | `proposal/` | `guideline_workspace_proposal.md` | — |
   | TK006 | `T102-PH001-ST002-AC001-TK006` | Produce GATE-001 external review | `planned` | LLM_Subconsultant | TK005 | `analysis/` | `guideline_workspace_analysis.md` §IV.B | — |
   | GATE-001 | `T102-PH001-ST002-AC001-GATE-001` | Gate: Client approval of AC001 gap analysis and remediation checklist | `planned` | Client | TK006 | Pass/fail | `guideline_workspace_plan.md` §VI | — |
   ```

5. **§III Tasks (Detailed)** — Use the following content for each task:

   ```markdown
   ---

   ## III. TASKS (DETAILED)

   ### Task TK001: P-STD-001 Structural Conformance Deep-Dive (All T102-STDs)

   **Task ID**: `T102-PH001-ST002-AC001-TK001`

   **Purpose**: Perform a detailed per-STD structural conformance assessment against the six P-STD-001 clauses identified in AC000's calibrated scope brief (TK005), expanding from the brief's summary-level verdicts to actionable per-gap remediation specifications. AC000 TK005 produced the high-level gap inventory (met/partial/not_met per CLAUSE per STD). This task produces the detailed breakdown needed for AC002/AC003 to define verification contracts and checklists.

   **Deliverable**:
   - Detailed per-STD conformance assessment captured in an analysis artifact under `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC001/analysis/`

   **Scope**:
   - In scope: Deep-dive structural assessment of all 9 T102-STDs against:
     - `P-STD-001-CLAUSE-001` (Canonical File Structure)
     - `P-STD-001-CLAUSE-031` (Standard-File YAML Frontmatter) — including CLAUSE-031B required fields and CLAUSE-031C lifecycle-conditional fields
     - `P-STD-001-CLAUSE-018` (CLAUSE Construction Requirements)
     - `P-STD-001-CLAUSE-028` (References & Provenance) — including CLAUSE-028A (references taxonomy) and CLAUSE-028B (provenance taxonomy)
     - `P-STD-001-CLAUSE-034` (Version Tracking & Amendment History) — including CLAUSE-034D (pre-baseline history)
     - `P-STD-001-CLAUSE-004` (Specification Lifecycle Stages) — including deprecated/superseded posture for STD-004 and STD-005
   - In scope: Identifying, for each not_met or partial gap, the exact remediation action needed (e.g., "add frontmatter block with these fields", "restructure References into normative/informative subsections")
   - In scope: Prioritizing gaps using the calibrated scope brief's priority order: (1) universal YAML frontmatter, (2) universal Amendment History, (3) clause-format normalization for worst offenders (STD-002, STD-003, STD-006, STD-008), (4) lifecycle-state normalization
   - Out of scope: Performing remediation; drafting verification contracts (AC002); modifying any STD file

   **Inputs Required**:
   - `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/analysis/analysis_T102-PH001-ST002-AC000_calibrated-scope-brief.md` — §V.B structural gap inventory as the starting baseline
   - `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md` — structural authority for each assessed CLAUSE
   - All 9 files under `prompt/artifacts/tasks/T102/standard/standard_T102-STD-*.md`

   **Steps**:
   1. Read the calibrated scope brief §V.B gap inventory to understand the summary-level verdicts
   2. Read P-STD-001 to extract the detailed requirements for each of the six assessed CLAUSEs
   3. For each T102-STD file, perform a deep-dive assessment:
      a. For each CLAUSE assessed as `not_met` or `partial` by the calibrated scope brief, identify the exact gap (what is missing vs what is present)
      b. Specify the exact remediation action needed (what needs to be added, restructured, or normalized)
      c. Classify the remediation complexity (trivial: copy-paste template; moderate: restructure existing content; significant: requires content generation or cross-reference resolution)
   4. Produce a prioritized remediation register ordered by the calibrated scope brief's priority guidance
   5. Flag any gap where the remediation action is ambiguous or requires a client decision before proceeding

   **Success Criteria**:
   - [ ] All 9 T102-STDs have a detailed conformance assessment for each of the 6 P-STD-001 CLAUSEs
   - [ ] Every `not_met` or `partial` gap has an explicit remediation action specified
   - [ ] Gaps are prioritized using the calibrated scope brief's four-tier priority scheme
   - [ ] Ambiguous gaps are explicitly flagged for client decision

   ---

   ### Task TK002: Residual Adoption/Verification Gap Inventory (Post-ST005)

   **Task ID**: `T102-PH001-ST002-AC001-TK002`

   **Purpose**: Identify remaining adoption and verification gaps across the T102-STD set that were not addressed by ST005's research-driven amendments. ST005 focused on content amendments to STD-001, STD-003, STD-006, and STD-007. This task identifies gaps in the remaining five standards (STD-002, STD-004, STD-005, STD-008, STD-009) and any cross-cutting adoption gaps that affect the entire set.

   **Deliverable**:
   - Residual gap inventory appended to or cross-referenced from the TK001 analysis artifact

   **Scope**:
   - In scope: Identifying adoption contract gaps (e.g., standards that lack clear adoption/enforcement language); identifying verification expectation gaps (e.g., CLAUSEs that cannot be checked by any current method); identifying cross-cutting gaps that affect the entire T102-STD set beyond structural conformance
   - Out of scope: Defining verification contracts (AC002); performing remediation; re-analyzing ST005 amendment targets for content gaps (AC000 TK001-TK004 already confirmed all deltas as `present`)

   **Inputs Required**:
   - TK001 detailed conformance assessment
   - `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/analysis/analysis_T102-PH001-ST002-AC000_calibrated-scope-brief.md` — §VI.D focus guidance
   - All 9 files under `prompt/artifacts/tasks/T102/standard/standard_T102-STD-*.md`

   **Steps**:
   1. Read the TK001 assessment and the calibrated scope brief §VI.D
   2. For each T102-STD, assess whether an explicit adoption contract exists (e.g., who enforces the standard, what is the compliance expectation, what is the verification method)
   3. Identify CLAUSEs across all standards that lack any verification path (neither manual checklist nor automation candidate)
   4. Identify cross-cutting gaps: inconsistent terminology, missing cross-references between standards, orphaned legacy patterns
   5. Produce a categorized gap inventory: structural conformance (from TK001), adoption, verification, legacy/cross-cutting

   **Success Criteria**:
   - [ ] Residual gap inventory covers all 9 T102-STDs
   - [ ] Each gap is categorized (structural, adoption, verification, legacy/cross-cutting)
   - [ ] Remediation checklist is minimal and actionable (no speculative scope)

   ---

   ### Task TK003: Post-Migration Structural Integrity Verification (ST003-Migrated STDs)

   **Task ID**: `T102-PH001-ST002-AC001-TK003`

   **Purpose**: Verify that the four STDs amended by ST005 (STD-001, STD-003, STD-006, STD-007) maintain structural integrity after the research-driven content amendments. ST005 added new CLAUSEs and governance notes; this task checks whether those additions introduced structural inconsistencies (e.g., clause numbering gaps, broken cross-references, section ordering drift).

   **Deliverable**:
   - Post-migration integrity assessment appended to or cross-referenced from the TK001/TK002 analysis artifact

   **Scope**:
   - In scope: Checking clause numbering continuity in the four ST005-amended STDs; checking internal cross-references resolve correctly; checking that new CLAUSEs follow the same structural pattern as existing CLAUSEs in the same file; checking that governance notes added by ST005 are structurally consistent with the file's existing note patterns
   - Out of scope: Re-verifying content correctness of ST005 amendments (AC000 TK001-TK004 already confirmed all deltas as `present`); assessing non-amended STDs (TK001 covers structural assessment for all nine)

   **Inputs Required**:
   - TK001 detailed conformance assessment (for the four amended STDs)
   - `prompt/artifacts/tasks/T102/workspace/PH001/ST005/plan_T102-PH001-ST005.md` — original amendment plan for cross-reference
   - The four amended STD files

   **Steps**:
   1. For each of STD-001, STD-003, STD-006, STD-007:
      a. Check that CLAUSE numbering is sequential without gaps or duplicates
      b. Check that all internal cross-references (e.g., "see CLAUSE-00X") resolve to existing CLAUSEs
      c. Check that new CLAUSEs follow the structural format of their siblings in the same file
      d. Check that governance notes use consistent formatting and are placed in appropriate sections
   2. Record any structural integrity issues found
   3. Classify each issue as cosmetic (formatting), moderate (broken reference), or significant (missing clause, numbering collision)

   **Success Criteria**:
   - [ ] All 4 ST005-amended STDs have a structural integrity assessment
   - [ ] Any structural issues are classified by severity
   - [ ] No significant structural issues are left unrecorded

   ---

   ### Task TK004: Legacy GDR/ADR-Model Reference Identification

   **Task ID**: `T102-PH001-ST002-AC001-TK004`

   **Purpose**: Identify any surviving references to the legacy GDR or ADR authoring model across all nine T102 standards. The STD-contains-CLAUSE model replaced the earlier separate-ADR model; ST001/ST003 performed migrations. This task confirms whether any legacy patterns survived the migration and need cleanup.

   **Deliverable**:
   - Legacy reference inventory appended to or cross-referenced from the combined gap analysis artifact

   **Scope**:
   - In scope: Searching all 9 T102-STD files for: (a) references to standalone ADR files that no longer exist or have been absorbed; (b) GDR-model language that predates the STD-contains-CLAUSE model; (c) references to `T102-STD-004` as a governing standard rather than as a superseded/deprecated artifact; (d) any reference to `T102-STD-009` as a separate standard rather than as absorbed into STD-004
   - Out of scope: Performing cleanup; modifying any file

   **Inputs Required**:
   - All 9 files under `prompt/artifacts/tasks/T102/standard/standard_T102-STD-*.md`
   - `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md` — for supersession posture reference

   **Steps**:
   1. Search all 9 T102-STD files for patterns: `ADR-`, `GDR-`, `Decision Record` section references, `T102-STD-004` as governing authority, `T102-STD-009` as active standard
   2. For each match, classify as: (a) legitimate historical reference (e.g., embedded ADR in Decision Record section — these are part of the STD-contains-CLAUSE model and are correct); (b) stale reference to the legacy model (needs cleanup); (c) ambiguous (needs consultant assessment)
   3. Produce a legacy reference inventory with file, location, classification, and recommended action

   **Success Criteria**:
   - [ ] All 9 T102-STD files have been searched
   - [ ] Each identified reference is classified (legitimate, stale, ambiguous)
   - [ ] Recommended actions are stated for stale references

   ---

   ### Task TK005: Produce GATE-001 Gate-Disposition Proposal

   **Task ID**: `T102-PH001-ST002-AC001-TK005`

   **Purpose**: Package the AC001 gap analysis deliverables into a gate-disposition proposal for client review and approval. This is a consultation-only gate — no DEV-REPORT or VERIFICATION tasks are required.

   **Deliverable**:
   - `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC001/proposal/proposal_T102-PH001-ST002-AC001_gate-001-disposition.md`

   **Scope**:
   - In scope: Gate-disposition proposal per `guideline_workspace_proposal.md` §V.B; GDR in pending state; evidence index referencing TK001-TK004 analysis artifacts
   - Out of scope: Client decision recording (that happens at GATE-001)

   **Inputs Required**:
   - TK001-TK004 analysis deliverables (primary evidence)
   - `prompt/templates/consultant/workspace/guideline_workspace_proposal.md` §V.B and §VII

   **Steps**:
   1. Author gate-disposition proposal per `guideline_workspace_proposal.md` §V.B
   2. Evidence Index: reference TK001-TK004 analysis artifacts as primary evidence
   3. Disposition items: GIR for each major gap category (structural conformance, adoption, verification, legacy references) with recommended resolution posture for AC002-AC004 downstream consumption
   4. Populate GDR fields in pending state per `guideline_workspace_proposal.md` §VII.D

   **Success Criteria**:
   - [ ] Gate-disposition proposal exists with GDR section in pending state
   - [ ] Evidence Index references all TK001-TK004 deliverables
   - [ ] Disposition items cover all major gap categories with actionable recommendations

   ---

   ### Task TK006: Produce GATE-001 External Review

   **Task ID**: `T102-PH001-ST002-AC001-TK006`

   **Purpose**: Produce an independent second-opinion quality audit of the AC001 GATE-001 gate package before client disposition.

   **Deliverable**:
   - `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC001/analysis/analysis_T102-PH001-ST002-AC001-TK006_gate-001-external-review.md`

   **Scope**:
   - In scope: Review of TK005 gate-disposition proposal; review of TK001-TK004 analysis artifacts; assessment of evidence integrity, role boundaries, plan compliance, and downstream readiness for AC002-AC004
   - Out of scope: Re-performing the gap analysis; overriding the gate-disposition proposal's GDR authority

   **Inputs Required**:
   - `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC001/proposal/proposal_T102-PH001-ST002-AC001_gate-001-disposition.md` — TK005 deliverable
   - TK001-TK004 analysis artifacts
   - `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC001/plan_T102-PH001-ST002-AC001.md` — governing plan
   - `prompt/templates/consultant/workspace/guideline_workspace_analysis.md` §IV.B

   **Steps**:
   1. Read the gate-disposition proposal and all evidence artifacts referenced in its Evidence Index
   2. Assess per `guideline_workspace_analysis.md` §IV.B:
      - Evidence integrity: all expected artifacts exist, cross-links resolve, package is internally consistent
      - Role-boundary compliance: no role produced an artifact outside its governed ownership boundary
      - Plan-guideline compliance: deliverables conform to governing guidelines
      - Downstream task readiness: AC002-AC004 can proceed with the gap inventory as primary input
      - Absence of unauthorized downstream execution: no remediation work has been performed prematurely
   3. Record findings and recommendation in the external review analysis artifact
   4. Main `LLM_Consultant` reviews the external review findings

   **Success Criteria**:
   - [ ] External review analysis artifact exists at specified path
   - [ ] All five assessment criteria are addressed
   - [ ] Main `LLM_Consultant` has reviewed and acknowledged the external review findings

   ---

   ### GATE-001: Client Approval of AC001 Gap Analysis and Remediation Checklist

   **Gate ID**: `T102-PH001-ST002-AC001-GATE-001`

   **Entry Criteria**:
   - TK001 through TK006 are completed
   - TK005 gate-disposition proposal exists with populated GDR in pending state
   - TK006 external review analysis exists and has been reviewed by main `LLM_Consultant`

   **Reviewer**: Client

   **Exit Criteria**:
   - Client records decision in the GDR per `guideline_workspace_proposal.md` §VII.D
   - If APPROVE: AC002-AC004 may proceed using the gap inventory and remediation checklist as primary input
   - If APPROVE WITH CONDITIONS: conditions are recorded and govern AC002-AC004 scoping
   - If RECYCLE: remediation tasks are created per `guideline_workspace_plan.md` §VI.K

   **Gate-Disposition Proposal**: `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC001/proposal/proposal_T102-PH001-ST002-AC001_gate-001-disposition.md`
   **External Review**: `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC001/analysis/analysis_T102-PH001-ST002-AC001-TK006_gate-001-external-review.md`
   ```

6. **§IV Links Register** — Use the following content:

   ```markdown
   ---

   ## IV. LINKS REGISTER

   | Link Type | Target | Path |
   |:--|:--|:--|
   | Plan (this file) | AC001 Activity Plan | `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC001/plan_T102-PH001-ST002-AC001.md` |
   | Plan | ST002 Stream Plan (parent) | `prompt/artifacts/tasks/T102/workspace/PH001/ST002/plan_T102-PH001-ST002.md` |
   | Plan (dependency) | AC000 Activity Plan | `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/plan_T102-PH001-ST002-AC000.md` |
   | Analysis (input) | AC000 Calibrated Scope Brief | `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/analysis/analysis_T102-PH001-ST002-AC000_calibrated-scope-brief.md` |
   | Standard (structural authority) | P-STD-001 Program Governance Standard | `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md` |
   | Plan (source) | ST005 Stream Plan (closed) | `prompt/artifacts/tasks/T102/workspace/PH001/ST005/plan_T102-PH001-ST005.md` |
   ```

7. **§V Changelog** — Use the following content:

   ```markdown
   ---

   ## V. CHANGELOG

   | Version | Date | Type | Summary |
   |:--|:--|:--|:--|
   | v1.0.0 | 2026-03-31 | Initial | AC001 Activity Plan created. Task decomposition: TK001 (P-STD-001 structural conformance deep-dive), TK002 (residual adoption/verification gap inventory), TK003 (post-migration structural integrity verification), TK004 (legacy GDR/ADR-model reference identification), TK005 (gate-disposition proposal), TK006 (external review), GATE-001 (consultation-only client approval). Source: AC000 GATE-001 approval (2026-03-31) and TK010.6 implementation specification. |
   ```

---

### SPEC-006 — Update ST002 stream plan to activate AC001 and link the activity plan

| Field | Detail |
|:--|:--|
| Requirement Source | `guideline_workspace_plan.md` §IV.D canonical link location rule; AC001 activation after GATE-001 approval |
| Target file(s) | `prompt/artifacts/tasks/T102/workspace/PH001/ST002/plan_T102-PH001-ST002.md` |
| Required end-state posture | (1) The AC001 Activity Register row shows `ready` instead of `planned` and its `Reference` cell contains the path to the new activity plan. (2) The AC001 section in §IV includes an `**Activity Plan**:` link matching the register `Reference`. (3) The stream plan version is bumped. |
| Explicit non-target / do-not-change constraints | Do NOT modify: §I-§III content, AC000 Activity Register row or section, AC002-AC004 Activity Register rows or sections, §V Links Register entries (except adding a new AC001 plan link if needed), other §VI Changelog entries. Only the AC001 register row, the AC001 section, the frontmatter version/date, and the Changelog are changed. |
| Validation check | (1) AC001 Activity Register row `Status` is `` `ready` ``. (2) AC001 row `Reference` is `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC001/plan_T102-PH001-ST002-AC001.md`. (3) AC001 section in §IV contains `**Activity Plan**: prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC001/plan_T102-PH001-ST002-AC001.md`. (4) Stream plan version is `v2.4.0`. (5) Changelog has a new entry. |
| Blocking ambiguity rule | If the AC001 Activity Register row does not currently show `planned`, stop and escalate. If the AC001 section in §IV does not exist, stop and escalate. |
| Status | `open` |

#### Implementation Detail

1. Open `prompt/artifacts/tasks/T102/workspace/PH001/ST002/plan_T102-PH001-ST002.md`.

2. **Activity Register amendment** — Locate the Activity Register table in §III. Find the AC001 row. The current state is:

   ```
   | AC001 | `T102-PH001-ST002-AC001` | STD adoption & verification gap analysis (post-amendment) | `planned` | LLM_Consultant | AC000 | Gap inventory + remediation checklist (against P-STD-001 conformance) | -- |
   ```

   Replace this row with:

   ```
   | AC001 | `T102-PH001-ST002-AC001` | STD adoption & verification gap analysis (post-amendment) | `ready` | LLM_Consultant | AC000 | Gap inventory + remediation checklist (against P-STD-001 conformance) | `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC001/plan_T102-PH001-ST002-AC001.md` |
   ```

   Changes: `Status` from `` `planned` `` to `` `ready` ``; `Reference` from `--` to the activity plan path.

3. **AC001 section amendment** — Locate the `### Activity AC001` section in §IV. Add the following line immediately after the existing `**Deliverable**:` paragraph and before the `**Scope**:` paragraph:

   ```
   **Activity Plan**: `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC001/plan_T102-PH001-ST002-AC001.md`
   ```

4. **Stream plan frontmatter update**:
   - `version` → `'2.4.0'`
   - `date` → `'2026-03-31'`

5. **Changelog entry** — Append to the §VI Changelog table:

   ```
   | v2.4.0 | 2026-03-31 | Amendment | Activated AC001 after GATE-001 approval (2026-03-31): updated AC001 Activity Register status from `planned` to `ready`, linked the new AC001 activity plan, and added Activity Plan path to the AC001 section. Source: TK010.6 implementation specification. |
   ```

---

## IV. IMPLEMENTATION SEQUENCE

The executor MUST perform the SPEC items in the following order. SPEC-002 and SPEC-003 target the same file and MUST be performed in the same editing pass. SPEC-004 and SPEC-005 are logically sequential (directory before file).

1. **SPEC-001** — Record the GATE-001 GDR decision in the proposal. This is the foundational act; all other SPEC items depend on this decision being recorded.
2. **SPEC-002 + SPEC-003** — Amend the AC000 plan: register TK010.6, close GATE-001, and unblock TK011. These target the same file and should be performed together.
3. **SPEC-004** — Create the AC001 directory structure.
4. **SPEC-005** — Author the AC001 activity plan in the new directory.
5. **SPEC-006** — Update the ST002 stream plan to activate AC001 and link the plan.

After step 5, the executor MUST stop. Do NOT begin executing TK011 or any AC001 tasks. Those are deferred to separate sessions.

## V. REFERENCES

| Document | Path |
|:--|:--|
| Governing Plan | `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/plan_T102-PH001-ST002-AC000.md` |
| Gate-Disposition Proposal (GDR target) | `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/proposal/proposal_T102-PH001-ST002-AC000_gate-001-disposition.md` |
| Calibrated Scope Brief (AC001 input) | `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/analysis/analysis_T102-PH001-ST002-AC000_calibrated-scope-brief.md` |
| ST002 Stream Plan | `prompt/artifacts/tasks/T102/workspace/PH001/ST002/plan_T102-PH001-ST002.md` |
| Activity Plan Template | `prompt/templates/consultant/workspace/template_workspace_plan_activity.md` |
| Plan Guideline | `prompt/templates/consultant/workspace/guideline_workspace_plan.md` |
| Implementation Guideline | `prompt/templates/consultant/workspace/guideline_workspace_implementation.md` |
| TK010 Downstream Execution Contract | `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/implementation/implementation_T102-PH001-ST002-AC000_tk010_gate-001-downstream-seed-task-specification.md` |
| External Review (active) | `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/analysis/analysis_T102-PH001-ST002-AC000-TK010.4_gate-001-recycle-external-review.md` |

## VI. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-03-31 | Initial | Created the TK010.6 gate-001 closure and downstream activation task specification. Six SPEC items: SPEC-001 (GDR recording), SPEC-002 (AC000 plan amendment with TK010.6 registration and GATE-001 closure), SPEC-003 (TK011 unblocking), SPEC-004 (AC001 directory creation), SPEC-005 (AC001 activity plan authoring), SPEC-006 (ST002 stream plan activation). Source: client SES005 approval of GATE-001 and commissioning of post-gate closure work. |
