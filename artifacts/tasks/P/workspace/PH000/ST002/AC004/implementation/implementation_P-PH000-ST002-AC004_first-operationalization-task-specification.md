---
artifact_type: 'IMPLEMENTATION'
implementation_type: 'task_specification'
initiative_id: 'P'
initiative_code: 'PROGRAM'
phase: '0'
stream_id: 'P-PH000-ST002'
activity_id: 'P-PH000-ST002-AC004'
task_id: 'P-PH000-ST002-AC004-TK004'
version: '1.0.0'
date: '2026-03-23'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/plan_P-PH000-ST002-AC004.md'
execution_audience: 'developer'
purpose: 'Decision-complete first-slice execution specification for AC004 TK004, authored pre-gate so the client can review the downstream execution contract as part of the Gate-001 readiness package.'
---

# IMPLEMENTATION (Task Specification): AC004 First Operationalization Slice

## I. PURPOSE & AUTHORITY
- Purpose: Specify the exact downstream execution contract for AC004 TK004, covering the first bounded operationalization slice of the status system after AC003 acceptance.
- Authority chain: AC004 plan authorizes work through `P-PH000-ST002-AC004-TK004` -> this artifact specifies HOW -> DEV-REPORT and VERIFICATION record execution evidence.
- Audience: `LLM_Developer` (primary) and `LLM_Reviewer` (secondary consumer for verification context).
- This artifact does NOT hold a GDR. Gate decisions remain in AC004 gate-disposition proposals.
- Execution is blocked until `P-PH000-ST002-AC004-GATE-001` records an approving Client decision.

## II. TASK SCOPE
- Governing plan task: `P-PH000-ST002-AC004-TK004`
- Trigger: The first operationalization slice is too detailed for plan-level steps alone because it spans reconciliation logic, multiple planning surfaces, and explicit authority-order enforcement.
- Deliverable contract:
  - Updated `prompt/artifacts/tasks/P/status/status_program.yaml`
  - Updated `prompt/artifacts/tasks/P/status/status_program.md`
  - Updated ST002 / PH000 / roadmap surfaces required by the approved V1 rollout boundary
  - Any explicitly approved reminder or enforcement surfaces named by the operating-model approval

## III. SPECIFICATION ITEMS

### SPEC-001 - Reconcile the accepted AC003 baseline against live planning truth

| Field | Detail |
|:--|:--|
| Requirement Source | `P-PH000-ST002-AC004-TK004`; AC004 operating-model approval |
| Output | Updated status ledger and derived narrative |
| Acceptance Criteria | The first-slice updates apply the approved authority order and remove known AC003/AC004 drift without introducing new ledger-narrative drift. |
| Status | `open` |

#### Implementation Detail

Use the approved authority order from `GATE-001`:
- stream plan is authoritative for activity truth,
- phase plan is snapshot-only,
- roadmap is summary-only,
- ledger is authoritative over narrative within the status artifacts.

At minimum, reconcile the known AC003 / AC004 status drift captured during the AC003 external review and any directly related inconsistencies across the bounded V1 rollout surfaces. Update the ledger first, then re-derive the narrative so the narrative remains downstream of the ledger rather than an independent source.

### SPEC-002 - Encode the approved V1 rollout boundary on planning surfaces

| Field | Detail |
|:--|:--|
| Requirement Source | AC004 `GATE-001` package; bounded rollout decision |
| Output | Updated ST002 stream plan, PH000 phase plan, and roadmap references that reflect the accepted AC004 posture |
| Acceptance Criteria | Planning surfaces consistently reflect the approved AC004 execution posture for `P`, `T102`, and `T104` without over-expanding scope. |
| Status | `open` |

#### Implementation Detail

Only update the planning and summary surfaces that were explicitly approved as part of the bounded V1 rollout. Preserve thin-spine behavior at the roadmap layer. Do not extend the rollout beyond `P`, `T102`, and `T104` unless the approved gate package says so explicitly.

### SPEC-003 - Apply mandatory status-touchpoint and reminder/enforcement boundaries

| Field | Detail |
|:--|:--|
| Requirement Source | AC004 operating-model approval; AC004 TK004 contract |
| Output | Updated status-operating surfaces and any explicitly approved reminder/enforcement surfaces |
| Acceptance Criteria | Future-governed-work touchpoints are encoded on the approved surfaces, and no unapproved standards or automation expansions are introduced. |
| Status | `open` |

#### Implementation Detail

Apply only the touchpoints and reminder or enforcement boundaries explicitly approved at `GATE-001`. This slice may encode required update triggers, ownership notes, and approved reminder locations. It must not silently create new standards requirements, repo-wide automation, or cross-initiative retrofit work outside the approved V1 scope.

### SPEC-004 - Preserve the AC005 / future-initiative boundary

| Field | Detail |
|:--|:--|
| Requirement Source | AC004 scope boundary; AC005 successor stub |
| Output | Clean separation between V1 rollout execution and future V2 commissioning work |
| Acceptance Criteria | No future initiative is opened and no `sps_T105`-like surface is created during AC004 execution. |
| Status | `open` |

#### Implementation Detail

Do not select or open `T105` or any other future initiative ID during TK004. Do not create a new SPS home for the future status-system initiative. AC005 exists to hold that work after AC004 closes.

## IV. IMPLEMENTATION SEQUENCE

1. Confirm `GATE-001` approval and read the approved operating-model analysis and gate-disposition package.
2. Reconcile the authoritative stream-plan truth into the status ledger.
3. Re-derive and verify the status narrative from the reconciled ledger.
4. Apply the approved planning-surface and reminder-boundary updates for the bounded V1 rollout.
5. Produce execution evidence in the AC004 DEV-REPORT and hand off to verification.

## V. REFERENCES

| Document | Path |
|:--|:--|
| Governing Plan | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/plan_P-PH000-ST002-AC004.md` |
| AC004 Operating-Model Analysis | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/analysis/analysis_P-PH000-ST002-AC004_operating-model-and-reconciliation-policy.md` |
| AC004 GATE-001 Proposal | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/proposal/proposal_P-PH000-ST002-AC004-GATE-001_operating-model-disposition.md` |
| Status Ledger | `prompt/artifacts/tasks/P/status/status_program.yaml` |
| Status Narrative | `prompt/artifacts/tasks/P/status/status_program.md` |
| ST002 Stream Plan | `prompt/artifacts/tasks/P/workspace/PH000/ST002/plan_P-PH000-ST002.md` |
| PH000 Phase Plan | `prompt/artifacts/tasks/P/workspace/PH000/plan_P-PH000.md` |
| Program Roadmap | `prompt/artifacts/tasks/P/ssot/roadmap_P-PROGRAM_phase0.md` |
| Implementation Guideline | `prompt/templates/consultant/workspace/guideline_workspace_implementation.md` |

## VI. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-03-23 | Initial | Authored the AC004 first operationalization `task_specification` as a pre-gate readiness artifact so the client can review the bounded V1 execution contract before approving `GATE-001`. |
