---
artifact_type: 'IMPLEMENTATION'
implementation_type: 'task_specification'
initiative_id: 'P'
initiative_code: 'PROGRAM'
phase: '0'
stream_id: 'P-PH000-ST001'
activity_id: 'P-PH000-ST001-AC009'
task_id: 'P-PH000-ST001-AC009-TK013'
version: '1.0.0'
date: '2026-03-27'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/plan_P-PH000-ST001-AC009.md'
execution_audience: 'agentic_executor'
purpose: 'Exact execution contract for clean Gate-002 closeout after the commissioned external review, including consultant-owned package-surface remediation and final proposal/GDR updates.'
---

# IMPLEMENTATION (Task Specification): AC009 Gate-002 Clean Closeout

## I. PURPOSE & AUTHORITY
- Purpose: Specify the exact consultant-commissioned execution needed to close `P-PH000-ST001-AC009-GATE-002` cleanly after the commissioned external review has identified the remaining package/readiness drifts.
- Authority chain: AC009 plan retains tracked-work authority (`P-PH000-ST001-AC009-TK013`) -> this artifact specifies HOW the clean closeout edits are executed -> the proposal GDR records the authoritative gate decision.
- Audience: Designated agentic executor acting on the consultant's behalf.
- This artifact does NOT hold a GDR. Gate decisions remain exclusively in the Gate-002 `gate_disposition` proposal.

## II. TASK SCOPE
- Governing plan task: `P-PH000-ST001-AC009-TK013`
- Trigger: Gate-002 closeout requires multiple coordinated consultant-owned package-surface edits that exceed plan-step capacity.
- Deliverable contract: Leave the current commissioned external review intact, remediate the live planning/package drift it identifies, record clean `APPROVE` in the Gate-002 proposal only, and leave `TK006` explicitly ready as the next step.

## III. SPECIFICATION ITEMS

### SPEC-001 — Update the AC009 activity plan to reflect the real Gate-002 closeout state

| Field | Detail |
|:--|:--|
| Requirement Source | Commissioned external review `GAP-001` and `GAP-002` |
| Target file(s) | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/plan_P-PH000-ST001-AC009.md` |
| Required end-state posture | `TK010` through `TK013` are `completed`; `GATE-002` reflects final approved closure; `TK006` is `ready`; `TK006` input authority points to the approved evolved `GATE-002` package rather than `GATE-001` |
| Explicit non-target / do-not-change constraints | Do not alter the substantive scope of `TK010` outputs; do not re-sequence the task register beyond what is needed for state accuracy |
| Validation check | `rg -n "TK010|TK011|TK012|TK013|GATE-002|TK006" prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/plan_P-PH000-ST001-AC009.md` confirms the updated statuses and wording |
| Blocking ambiguity rule | If any required status transition would contradict the already-authored Gate-002 proposal or the commissioned external review, stop and escalate instead of inferring a new lifecycle state |
| Status | `open` |

#### Implementation Detail

Update the AC009 task register so it tells the same story as the artifacts already in the workspace. `TK010`, `TK011`, `TK012`, and `TK013` must no longer remain at `planned`. `GATE-002` must show the final approved posture once the proposal GDR is updated. `TK006` must be left explicitly `ready` because it is the immediate next action after gate closure. In the detailed `TK006` section, replace the stale input wording that still points to the approved package from `GATE-001`; the authoritative input is the approved evolved package from `GATE-002`.

### SPEC-002 — Update the ST001 stream plan so AC010 links resolve cleanly

| Field | Detail |
|:--|:--|
| Requirement Source | Commissioned external review `GAP-003` |
| Target file(s) | `prompt/artifacts/tasks/P/workspace/PH000/ST001/plan_P-PH000-ST001.md` |
| Required end-state posture | The AC010 Activity Register row contains the live standalone plan path; the AC010 activity section no longer says `Activity Plan: TBD` and instead points to the already-authored plan file |
| Explicit non-target / do-not-change constraints | Do not change AC010 scope, dependency posture, or activity status; do not edit the AC010 activity plan itself |
| Validation check | `rg -n "AC010|Activity Plan" prompt/artifacts/tasks/P/workspace/PH000/ST001/plan_P-PH000-ST001.md` shows the live path and no `TBD` string for AC010 |
| Blocking ambiguity rule | If the stream plan contains multiple competing AC010 plan paths, stop and escalate instead of picking one |
| Status | `open` |

#### Implementation Detail

This is a discoverability and anti-drift correction only. The stream plan must surface the already-existing AC010 plan at the canonical locations required by the plan guideline. Leave AC010 `planned` and AC009 `in_progress`.

### SPEC-003 — Record the clean gate approval in the Gate-002 proposal only

| Field | Detail |
|:--|:--|
| Requirement Source | Commissioned external review conclusion + client instruction for clean Gate-002 closure |
| Target file(s) | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/proposal/proposal_P-PH000-ST001-AC009_gate-002_p-std-001-evolution-disposition.md` |
| Required end-state posture | The proposal retains one `GIR-001`; the consultant recommendation is clean `APPROVE`; the GDR records `Client Decision: APPROVE`, `Gate Status After Decision: completed`, `Conditions: —`, and a concrete SES005 decision reference |
| Explicit non-target / do-not-change constraints | Do not change the commissioned external review; do not create a second GIR; do not reframe this as `APPROVE WITH CONDITIONS` or `RECYCLE` |
| Validation check | Re-read the proposal GDR and recommendation sections to confirm the approval appears only here and that no residual conditions remain |
| Blocking ambiguity rule | If any source artifact still implies that approval should be recorded anywhere other than the proposal GDR, stop and escalate |
| Status | `open` |

#### Implementation Detail

Use the proposal as the sole clean-approval surface. Keep the package narrative aligned with the commissioned external review: the remaining drift was package-readiness only, the remediation has been completed, and clean closure is now appropriate. Do not alter the external review to mirror the final approval.

### SPEC-004 — Create SES005 and update the ST001 notes register

| Field | Detail |
|:--|:--|
| Requirement Source | Proposal GDR requires a concrete decision reference; session-based decision recording is the existing workspace pattern |
| Target file(s) | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/snotes/snotes_P-PH000-ST001-AC009-SES005.md`, `prompt/artifacts/tasks/P/workspace/PH000/ST001/notes_P-PH000-ST001.md` |
| Required end-state posture | SES005 records the commissioned external review, the package remediation execution, the clean client `APPROVE`, and the fact that `TK006` is the exact next step; the ST001 notes register indexes SES005 under AC009 |
| Explicit non-target / do-not-change constraints | Do not rewrite prior session notes; do not invent new gate conditions not present in the proposal |
| Validation check | SES005 exists, is indexed in the stream notes register, and is cited by the Gate-002 proposal GDR |
| Blocking ambiguity rule | If the decision reference format needed by the proposal becomes unclear, stop and escalate instead of inventing a new notes pattern |
| Status | `open` |

#### Implementation Detail

Use the existing AC009 session-notes pattern. The session note should make clear that the external review remained unchanged after commissioning, that the clean approval was recorded only in the proposal, and that `TK006` is now ready as the immediate next action.

### SPEC-005 — Preserve all commissioned evidence outside the approved write set

| Field | Detail |
|:--|:--|
| Requirement Source | Consultant orchestration rule for this session |
| Target file(s) | Non-target set: commissioned external review, existing Gate-002 verification, `P-STD-001`, changelog, standard-authoring guideline/template, AC010 activity plan |
| Required end-state posture | None of these files are modified during execution |
| Explicit non-target / do-not-change constraints | Treat these files as read-only evidence surfaces for this pass |
| Validation check | Review the changed-file list and confirm none of the protected files appear |
| Blocking ambiguity rule | If any protected file seems to require edits to complete the package, stop and escalate rather than mutating it |
| Status | `open` |

#### Implementation Detail

This pass is package closeout only. Do not reopen implementation-backed evidence or standard-side outputs.

## IV. IMPLEMENTATION SEQUENCE
1. Read the commissioned external review in full.
2. Update the AC009 activity plan per `SPEC-001`.
3. Update the ST001 stream plan per `SPEC-002`.
4. Update the Gate-002 proposal per `SPEC-003`.
5. Create SES005 and update the ST001 notes register per `SPEC-004`.
6. Run the validation checks from all SPEC items.
7. Return a concise execution summary with the exact changed-file list for consultant review.

## V. REFERENCES

| Document | Path |
|:--|:--|
| Governing Plan | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/plan_P-PH000-ST001-AC009.md` |
| Commissioned External Review | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/analysis/analysis_P-PH000-ST001-AC009_external-review_gate-002-package.md` |
| Gate-002 Proposal | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/proposal/proposal_P-PH000-ST001-AC009_gate-002_p-std-001-evolution-disposition.md` |
| Gate-002 Verification | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/verification/verification_P-PH000-ST001-AC009_gate-002.md` |
| ST001 Stream Plan | `prompt/artifacts/tasks/P/workspace/PH000/ST001/plan_P-PH000-ST001.md` |
| ST001 Notes Register | `prompt/artifacts/tasks/P/workspace/PH000/ST001/notes_P-PH000-ST001.md` |

## VI. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-03-27 | Initial | Authored the exact agentic execution contract for clean AC009 Gate-002 closeout after the commissioned external review. Covers AC009/ST001 planning-surface remediation, proposal-only clean approval recording, SES005 creation, and protected non-target constraints. |
