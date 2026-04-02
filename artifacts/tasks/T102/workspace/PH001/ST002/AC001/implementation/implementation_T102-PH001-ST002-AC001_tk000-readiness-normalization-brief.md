---
artifact_type: 'IMPLEMENTATION'
implementation_type: 'task_specification'
initiative_id: 'T102'
initiative_code: 'CWD'
phase: '1'
stream_id: 'T102-PH001-ST002'
activity_id: 'T102-PH001-ST002-AC001'
task_id: 'T102-PH001-ST002-AC001-TK000'
version: '1.0.0'
date: '2026-04-02'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC001/plan_T102-PH001-ST002-AC001.md'
execution_audience: 'assistant'
purpose: 'Bounded assistant-execution brief for formalizing AC001-TK000, exposing the AC001 upstream authority chain, and reconciling the ST002 stream-plan activation posture without reopening AC000 artifacts.'
---

# IMPLEMENTATION (Task Specification): AC001 TK000 Readiness Normalization Brief

## I. PURPOSE & AUTHORITY

- Purpose: Define the exact assistant-executed normalization pass required to convert the current AC001 readiness findings into a clean, commissionable planning posture before any substantive AC001 development begins.
- Authority chain: The AC001 readiness assessment concludes that the remaining problems are orchestration defects rather than missing AC001 task decomposition -> this brief specifies HOW the assistant formalizes `TK000` and reconciles the live planning surfaces -> the main consultant reviews the result before any later AC001 execution session is commissioned.
- Audience: `LLM_Assistant`
- Filename note: this is an assistant-scoped orchestration brief under `task_specification` with `execution_audience: 'assistant'`.
- This artifact does NOT hold a GDR. It exists only to commission bounded planning-surface normalization for AC001.
- If any required change would reopen AC000 decisions, alter AC000 artifacts, or expand AC001 substantive scope beyond readiness normalization, the assistant MUST stop and escalate.

## II. TASK SCOPE

- Governing plan task: `T102-PH001-ST002-AC001-TK000`
- Trigger: The AC001 readiness assessment found that the AC001 plan is already substantively complete for its original first-draft purpose, but the activity still lacks a formal `TK000` readiness lane, a full upstream authority chain in the AC001 plan, and a reconciled stream-level activation state.
- Deliverable contract:
  - refreshed `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC001/plan_T102-PH001-ST002-AC001.md`
  - refreshed `prompt/artifacts/tasks/T102/workspace/PH001/ST002/plan_T102-PH001-ST002.md`
  - no edits to AC000 artifacts
  - no edits to the AC000 -> AC001 communication artifact
  - no edits to the newly authored AC001 readiness assessment or this brief

## III. SPECIFICATION ITEMS

### SPEC-001 - Amend the AC001 activity plan to formalize TK000 and surface the full authority chain

| Field | Detail |
|:--|:--|
| Requirement Source | `analysis_T102-PH001-ST002-AC001-TK000_activity-plan-readiness-assessment.md`; `guideline_workspace_plan.md` task-register authority rules; approved user decision to formalize `AC001-TK000` |
| Target file(s) | `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC001/plan_T102-PH001-ST002-AC001.md` |
| Required end-state posture | The AC001 plan contains a new `TK000` readiness lane as the first registered task, `TK001` depends on `TK000`, the detailed `TK000` section exists, and the AC001 plan's Context and Links Register directly expose the full upstream authority chain needed for the next session. |
| Explicit non-target / do-not-change constraints | Do NOT change the overall AC001 activity title, objective, substantive `TK001`-`TK004` scope, gate design, or downstream deliverable contracts. Do NOT add `GATE-000`. Do NOT create new AC001 proposal, notes, or gate rows in this pass. |
| Validation check | (1) Task Register row count becomes 8 with `TK000` inserted before `TK001`. (2) `TK000` status is `` `completed` ``. (3) `TK001` `Depends On` is `TK000`. (4) `### Task TK000` exists in Section III. (5) Context includes the AC000 GDR/proposal, `TK010.6`, `SES005`, the handoff communication, the readiness assessment, and this implementation brief. (6) Links Register includes those same new authority surfaces. (7) Plan version is `1.1.0` and date is `2026-04-02`. |
| Blocking ambiguity rule | If the AC001 plan already contains a `TK000` row, or if adding `TK000` would require changing any AC001 substantive task beyond inserting the readiness dependency and backlinks, stop and escalate instead of inferring a broader refactor. |
| Status | `open` |

#### Implementation Detail

1. Open `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC001/plan_T102-PH001-ST002-AC001.md`.
2. Update frontmatter only as follows:
   - change `version` from `'1.0.0'` to `'1.1.0'`
   - change `date` from `'2026-03-31'` to `'2026-04-02'`
   - keep `status: 'draft'`
   - keep all other frontmatter keys unchanged
3. In `## II. ACTIVITY OUTLINE` -> `**Context**`, append these six new lines after the existing `concept_T102-CONSULTANT.md` entry:
   - `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/proposal/proposal_T102-PH001-ST002-AC000_gate-001-disposition.md`
   - `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/implementation/implementation_T102-PH001-ST002-AC000_tk010.6_gate-001-closure-and-downstream-activation-task-specification.md`
   - `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/snotes/snotes_T102-PH001-ST002-AC000-SES005.md`
   - `prompt/artifacts/tasks/T102/workspace/PH001/ST002/communication/comm_T102-PH001-ST002-AC000_to_AC001_gate-001-activation-gap-handoff.md`
   - `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC001/analysis/analysis_T102-PH001-ST002-AC001-TK000_activity-plan-readiness-assessment.md`
   - `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC001/implementation/implementation_T102-PH001-ST002-AC001_tk000-readiness-normalization-brief.md`
4. In the `### Task Register` table, insert this new row immediately before the current `TK001` row:

   ```
   | TK000 | `T102-PH001-ST002-AC001-TK000` | Assess AC001 readiness and normalize activation surfaces | `completed` | LLM_Consultant | — | AC001 plan + ST002 stream plan + readiness artifacts | `analysis/analysis_T102-PH001-ST002-AC001-TK000_activity-plan-readiness-assessment.md` | Readiness assessment authored; assistant normalization brief commissioned to formalize AC001 TK000 and reconcile stream-level activation posture. |
   ```

5. In the existing `TK001` row, change `Depends On` from `—` to `TK000`. Do not change any other `TK001` cell.
6. In `## III. TASKS (DETAILED)`, insert a new section immediately before the existing `### Task TK001` section:

   ```markdown
   ### Task TK000: Assess AC001 Readiness and Normalize Activation Surfaces

   **Task ID**: `T102-PH001-ST002-AC001-TK000`

   **Purpose**: Convert the current AC001 activation and planning ambiguity into a bounded readiness package before substantive AC001 analysis work begins. This task documents the current-state assessment, exposes the AC001 upstream authority chain locally, and commissions the exact normalization pass required to reconcile the live planning surfaces.

   **Deliverable**:
   - `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC001/analysis/analysis_T102-PH001-ST002-AC001-TK000_activity-plan-readiness-assessment.md`
   - `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC001/implementation/implementation_T102-PH001-ST002-AC001_tk000-readiness-normalization-brief.md`
   - Normalized AC001 activity plan and ST002 stream plan posture

   **Scope**:
   - In scope:
     - Assess current AC001 readiness against the approved AC000 Gate-001 package and the later AC000 -> AC001 defect handoff
     - Formalize AC001-local readiness governance through `TK000`
     - Reconcile the ST002 stream-plan AC001 activation state with the current AC001 plan reality
     - Surface the AC000 GDR, `TK010.6`, `SES005`, and handoff communication as explicit AC001 authority inputs
   - Out of scope:
     - Executing substantive AC001 tasks `TK001` through `TK004`
     - Reopening or editing any AC000 artifact
     - Adding a new gate or proposal lane for AC001 readiness

   **Inputs Required**:
   - `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC001/plan_T102-PH001-ST002-AC001.md` - governing activity plan being normalized
   - `prompt/artifacts/tasks/T102/workspace/PH001/ST002/plan_T102-PH001-ST002.md` - parent stream plan whose AC001 activation row must be reconciled
   - `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/proposal/proposal_T102-PH001-ST002-AC000_gate-001-disposition.md` - approved AC000 Gate-001 GDR and downstream sequencing authority
   - `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/implementation/implementation_T102-PH001-ST002-AC000_tk010.6_gate-001-closure-and-downstream-activation-task-specification.md` - original commissioning contract for the AC001 first-draft plan
   - `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/snotes/snotes_T102-PH001-ST002-AC000-SES005.md` - client decisions that authorized AC001 post-gate activation
   - `prompt/artifacts/tasks/T102/workspace/PH001/ST002/communication/comm_T102-PH001-ST002-AC000_to_AC001_gate-001-activation-gap-handoff.md` - cross-activity defect handoff and non-reopen boundary

   **Steps**:
   1. Author the AC001 readiness assessment documenting resolved versus still-open activation gaps.
   2. Author an assistant-scoped implementation brief that limits execution to AC001-plan normalization and ST002 stream-plan reconciliation.
   3. Execute the brief and then review the bounded output before commissioning `TK001`.

   **Success Criteria**:
   - [ ] Readiness assessment exists and records the current-state posture accurately
   - [ ] Assistant execution brief exists and is decision-complete for the normalization pass
   - [ ] AC001 plan exposes the full upstream authority chain needed for the next session
   - [ ] ST002 stream-plan AC001 row is reconciled to the live activation posture
   - [ ] No AC000 artifact is reopened or edited during this readiness pass
   ```

7. In `## IV. LINKS REGISTER`, add these new rows immediately after the existing `AC000 Activity Plan` row and before the current `Analysis (input)` row:
   - `| Proposal (upstream authority) | AC000 Gate-001 Disposition / GDR | \`prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/proposal/proposal_T102-PH001-ST002-AC000_gate-001-disposition.md\` |`
   - `| Implementation (upstream authority) | AC000 TK010.6 Activation Specification | \`prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/implementation/implementation_T102-PH001-ST002-AC000_tk010.6_gate-001-closure-and-downstream-activation-task-specification.md\` |`
   - `| Notes (upstream authority) | AC000 SES005 Gate-001 Approval Session | \`prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/snotes/snotes_T102-PH001-ST002-AC000-SES005.md\` |`
   - `| Communication | AC000 -> AC001 Activation Defect Handoff | \`prompt/artifacts/tasks/T102/workspace/PH001/ST002/communication/comm_T102-PH001-ST002-AC000_to_AC001_gate-001-activation-gap-handoff.md\` |`
   - `| Analysis | AC001 TK000 Readiness Assessment | \`prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC001/analysis/analysis_T102-PH001-ST002-AC001-TK000_activity-plan-readiness-assessment.md\` |`
   - `| Implementation | AC001 TK000 Readiness Normalization Brief | \`prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC001/implementation/implementation_T102-PH001-ST002-AC001_tk000-readiness-normalization-brief.md\` |`
8. In `## V. CHANGELOG`, insert this new row above the existing `v1.0.0` row:

   ```
   | v1.1.0 | 2026-04-02 | Amendment | Formalized `TK000` as the AC001 readiness and activation-normalization lane. Added AC000 Gate-001 authority backlinks (`proposal`, `TK010.6`, `SES005`, and handoff communication), linked the AC001 readiness assessment and assistant execution brief, and gated `TK001` on `TK000`. Source: AC001 TK000 readiness assessment and implementation brief. |
   ```

9. Do not modify any other AC001 plan content unless required to keep table formatting valid.

### SPEC-002 - Amend the ST002 stream plan to reconcile the AC001 activation posture

| Field | Detail |
|:--|:--|
| Requirement Source | `analysis_T102-PH001-ST002-AC001-TK000_activity-plan-readiness-assessment.md`; original AC000 `TK010.6` SPEC-006 activation intent |
| Target file(s) | `prompt/artifacts/tasks/T102/workspace/PH001/ST002/plan_T102-PH001-ST002.md` |
| Required end-state posture | The ST002 stream plan no longer contradicts itself about AC001 activation: the Activity Register row is `ready`, the `Reference` cell points to the AC001 plan, and the changelog reflects a normalization amendment layered on top of the already existing `v2.4.0` activation claim. |
| Explicit non-target / do-not-change constraints | Do NOT alter AC000, AC002, AC003, or AC004 content. Do NOT rewrite the AC001 section's substantive Purpose, Deliverable, Scope, Inputs Required, or Task Register. Do NOT remove the existing `v2.4.0` changelog row. |
| Validation check | (1) AC001 Activity Register row `Status` is `` `ready` ``. (2) AC001 row `Reference` is `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC001/plan_T102-PH001-ST002-AC001.md`. (3) AC001 section still includes the same `**Activity Plan**:` line and it matches the register reference. (4) Stream-plan version is `2.5.0` and date is `2026-04-02`. |
| Blocking ambiguity rule | If the AC001 Activity Register row no longer exists, or if reconciling the row would require changing any non-AC001 activity content, stop and escalate instead of inferring broader stream-plan surgery. |
| Status | `open` |

#### Implementation Detail

1. Open `prompt/artifacts/tasks/T102/workspace/PH001/ST002/plan_T102-PH001-ST002.md`.
2. Update frontmatter only as follows:
   - change `version` from `'2.4.0'` to `'2.5.0'`
   - change `date` from `'2026-03-31'` to `'2026-04-02'`
   - keep `status: 'draft'`
   - keep all other frontmatter keys unchanged
3. In `### Activity Register`, replace the AC001 row:

   From:
   ```
   | AC001 | `T102-PH001-ST002-AC001` | STD adoption & verification gap analysis (post-amendment) | `planned` | LLM_Consultant | AC000 | Gap inventory + remediation checklist (against P-STD-001 conformance) | -- |
   ```

   To:
   ```
   | AC001 | `T102-PH001-ST002-AC001` | STD adoption & verification gap analysis (post-amendment) | `ready` | LLM_Consultant | AC000 | Gap inventory + remediation checklist (against P-STD-001 conformance) | `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC001/plan_T102-PH001-ST002-AC001.md` |
   ```

4. In `## IV. ACTIVITIES` -> `### Activity AC001`, do not rewrite the section. Verify that the existing `**Activity Plan**:` line remains:

   ```
   **Activity Plan**: `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC001/plan_T102-PH001-ST002-AC001.md`
   ```

   If it differs, normalize only that line so it matches the Activity Register reference exactly.
5. In `## VI. CHANGELOG`, insert this new row above the existing `v2.4.0` row:

   ```
   | v2.5.0 | 2026-04-02 | Amendment | Reconciled the partially applied AC001 activation posture left by the 2026-03-31 stream amendment: the Activity Register now shows AC001 as `ready` and links the existing AC001 activity plan, matching the already-authored AC001 section and prior activation record. Source: AC001 TK000 readiness normalization brief. |
   ```

6. Do not modify any other stream-plan content.

### SPEC-003 - Validate the bounded normalization pass and stop

| Field | Detail |
|:--|:--|
| Requirement Source | Consultant execution boundary for `T102-PH001-ST002-AC001-TK000` |
| Target file(s) | Working tree validation only |
| Required end-state posture | The assistant verifies that only the intended tracked files changed and that no AC000 artifact or communication artifact was edited as part of this pass. |
| Explicit non-target / do-not-change constraints | Do NOT run any mutating formatter, code generator, or cleanup command. Do NOT edit files in response to validation output unless the brief explicitly authorizes it. |
| Validation check | `git -C prompt diff --name-only` shows only the AC001 activity plan and the ST002 stream plan among tracked-file edits created by the assistant execution step. |
| Blocking ambiguity rule | If validation shows any tracked-file edits outside the two intended plan files, stop and report them without attempting cleanup or reversion. |
| Status | `open` |

#### Implementation Detail

1. Run:
   ```bash
   git -C prompt diff --name-only
   ```
2. Confirm the output includes:
   - `artifacts/tasks/T102/workspace/PH001/ST002/AC001/plan_T102-PH001-ST002-AC001.md`
   - `artifacts/tasks/T102/workspace/PH001/ST002/plan_T102-PH001-ST002.md`
3. Confirm the output does not include:
   - any file under `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/`
   - `prompt/artifacts/tasks/T102/workspace/PH001/ST002/communication/comm_T102-PH001-ST002-AC000_to_AC001_gate-001-activation-gap-handoff.md`
   - the newly created AC001 readiness assessment
   - this implementation brief
4. In the final assistant report, include:
   - the list of tracked files changed
   - whether each SPEC item passed validation
   - any blocker or mismatch encountered
5. Stop after reporting. Do not continue into substantive AC001 task execution.

## IV. IMPLEMENTATION SEQUENCE

1. Execute `SPEC-001` first to formalize `TK000` and expose the AC001 authority chain locally.
2. Execute `SPEC-002` second to reconcile the ST002 stream-plan activation state with the already-authored AC001 plan.
3. Execute `SPEC-003` last to verify the bounded scope and then stop.

## V. REFERENCES

| Document | Path |
|:--|:--|
| Governing Plan | `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC001/plan_T102-PH001-ST002-AC001.md` |
| Readiness Assessment | `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC001/analysis/analysis_T102-PH001-ST002-AC001-TK000_activity-plan-readiness-assessment.md` |
| Parent Stream Plan | `prompt/artifacts/tasks/T102/workspace/PH001/ST002/plan_T102-PH001-ST002.md` |
| Upstream GDR / Proposal | `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/proposal/proposal_T102-PH001-ST002-AC000_gate-001-disposition.md` |
| Upstream Implementation Authority | `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/implementation/implementation_T102-PH001-ST002-AC000_tk010.6_gate-001-closure-and-downstream-activation-task-specification.md` |
| Upstream Session Notes | `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/snotes/snotes_T102-PH001-ST002-AC000-SES005.md` |
| Cross-Activity Handoff | `prompt/artifacts/tasks/T102/workspace/PH001/ST002/communication/comm_T102-PH001-ST002-AC000_to_AC001_gate-001-activation-gap-handoff.md` |

## VI. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-04-02 | Initial | Created the AC001 TK000 readiness normalization brief. Three SPEC items: SPEC-001 (formalize `TK000` and expose the full AC001 authority chain), SPEC-002 (reconcile the ST002 stream-plan AC001 activation posture), and SPEC-003 (validate bounded scope and stop). Source: AC001 TK000 readiness assessment. |
