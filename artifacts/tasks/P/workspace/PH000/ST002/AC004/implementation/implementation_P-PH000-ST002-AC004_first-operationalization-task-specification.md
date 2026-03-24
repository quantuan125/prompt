---
artifact_type: 'IMPLEMENTATION'
implementation_type: 'task_specification'
initiative_id: 'P'
initiative_code: 'PROGRAM'
phase: '0'
stream_id: 'P-PH000-ST002'
activity_id: 'P-PH000-ST002-AC004'
task_id: 'P-PH000-ST002-AC004-TK004'
version: '1.2.0'
date: '2026-03-24'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/plan_P-PH000-ST002-AC004.md'
execution_audience: 'developer'
purpose: 'Decision-complete first-slice execution specification for AC004 TK004, amended after the GATE-001 recycle decision so the client-reviewed contract names the approved operating surfaces, cadence model, reminder surface, and conditional-approval handling.'
---

# IMPLEMENTATION (Task Specification): AC004 First Operationalization Slice

## I. PURPOSE & AUTHORITY
- Purpose: Specify the exact downstream execution contract for AC004 TK004, covering the first bounded operationalization slice of the status system after AC003 acceptance.
- Authority chain: AC004 plan authorizes work through `P-PH000-ST002-AC004-TK004` -> this artifact specifies HOW -> DEV-REPORT and VERIFICATION record execution evidence.
- Audience: `LLM_Developer` (primary) and `LLM_Reviewer` (secondary consumer for verification context).
- This artifact does NOT hold a GDR. Gate decisions remain in AC004 gate-disposition proposals.
- Execution is blocked until `P-PH000-ST002-AC004-GATE-001` records an approving Client decision.
- If `GATE-001` records `APPROVE WITH CONDITIONS`, this artifact MUST be amended by `LLM_Consultant` to incorporate those conditions before TK004 execution begins.

## II. TASK SCOPE
- Governing plan task: `P-PH000-ST002-AC004-TK004`
- Trigger: The first operationalization slice is too detailed for plan-level steps alone because it spans reconciliation logic, multiple planning surfaces, explicit authority-order enforcement, and named reminder-surface boundaries.
- Deliverable contract:
  - Updated `prompt/artifacts/tasks/P/status/status_program.yaml`
  - Updated `prompt/artifacts/tasks/P/status/status_program.md`, including Section 7 operational protocol where required by the approved AC004 operating model
  - Updated ST002 / PH000 / roadmap surfaces required by the approved V1 rollout boundary
  - Updated `prompt/skills/wrap-up/SKILL.md` as the approved session-close reminder surface, if that surface requires bounded wording changes to encode the approved V1 reminder
- Explicit non-target surfaces:
  - Do NOT amend root `AGENTS.md`
  - Do NOT amend `prompt/AGENTS.md`
  - Do NOT amend `prompt/artifacts/tasks/P/standard/standard_P-STD-002_program-status-standard.md`

## III. SPECIFICATION ITEMS

### SPEC-001 - Reconcile the accepted AC003 baseline against live planning truth

| Field | Detail |
|:--|:--|
| Requirement Source | `P-PH000-ST002-AC004-TK004`; AC004 operating-model approval |
| Output | Updated status ledger and derived narrative |
| Acceptance Criteria | The first-slice updates apply the approved authority order and remove known AC003/AC004 drift without introducing new ledger-narrative drift. After reconciliation, the executor must confirm that the narrative is fully derived from the reconciled ledger with no independent assertions or stale references that diverge from ledger truth. |
| Status | `open` |

#### Implementation Detail

Use the approved authority order from `GATE-001`:
- stream plan is authoritative for activity truth,
- phase plan is snapshot-only,
- roadmap is summary-only,
- ledger is authoritative over narrative within the status artifacts.

At minimum, reconcile the known AC003 / AC004 status drift captured during the AC003 external review and any directly related inconsistencies across the bounded V1 rollout surfaces. Update the ledger first, then re-derive the narrative so the narrative remains downstream of the ledger rather than an independent source. 

After updating the ledger and re-deriving the narrative, perform a section-by-section comparison to confirm the narrative contains no independent status claims, stale activity references, or date/state values that diverge from the reconciled ledger.

### SPEC-002 - Encode the approved V1 rollout boundary on planning and summary surfaces

| Field | Detail |
|:--|:--|
| Requirement Source | AC004 `GATE-001` package; bounded rollout decision |
| Output | Updated ST002 stream plan, PH000 phase plan, and roadmap references that reflect the accepted AC004 execution posture |
| Acceptance Criteria | Planning surfaces consistently reflect the approved AC004 execution posture for `P`, `T102`, and `T104` without over-expanding scope. |
| Status | `open` |

#### Implementation Detail

Update only the planning and summary surfaces explicitly approved as part of the bounded V1 rollout:
- `prompt/artifacts/tasks/P/workspace/PH000/ST002/plan_P-PH000-ST002.md`
- `prompt/artifacts/tasks/P/workspace/PH000/plan_P-PH000.md`
- `prompt/artifacts/tasks/P/ssot/roadmap_P-PROGRAM_phase0.md`

Preserve thin-spine behavior at the roadmap layer. Do not extend the rollout beyond `P`, `T102`, and `T104` unless the approved gate package says so explicitly.

### SPEC-003 - Apply the approved cadence, ownership/evidence, and reminder-boundary model

| Field | Detail |
|:--|:--|
| Requirement Source | AC004 operating-model approval; AC004 TK004 contract |
| Output | Updated status-operating surfaces and approved reminder surface |
| Acceptance Criteria | The approved event-driven cadence, attribution/evidence expectations, and bounded reminder model are encoded without introducing new standards requirements, AGENTS-layer rules, or repo-wide automation. |
| Status | `open` |

#### Implementation Detail

Apply the approved operating-model decisions as follows:
- Keep the governing operating protocol in `prompt/artifacts/tasks/P/status/status_program.md` Section 7.
- Use `prompt/skills/wrap-up/SKILL.md` as the only approved session-close reminder surface for AC004 V1.
- Encode the approved trigger model so future governed work in `P`, `T102`, and `T104` reconciles status on lifecycle changes, gate decisions, dependency changes, and stale-state review.
- Preserve the existing attribution/evidence model from `P-STD-002`: routine non-terminal updates remain attributed; terminal/reopen transitions remain Client-accountable and evidence-bearing.

This slice MUST NOT:
- create AC004-specific operating rules in `AGENTS.md` or `prompt/AGENTS.md`,
- amend `P-STD-002`,
- introduce repo-wide automation,
- expand the reminder model beyond the approved V1 boundary.

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

1. Confirm `GATE-001` approval state and read the approved operating-model analysis, external review, and gate-disposition package.
2. If `GATE-001 = APPROVE WITH CONDITIONS`, verify that this specification has been amended to reflect those conditions before execution starts.
3. Reconcile the authoritative stream-plan truth into the status ledger.
4. Re-derive and verify the status narrative from the reconciled ledger.
5. Apply the approved planning-surface updates and the bounded reminder-surface update for the V1 rollout.
6. Produce execution evidence in the AC004 DEV-REPORT and hand off to verification.

## V. REFERENCES

| Document | Path |
|:--|:--|
| Governing Plan | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/plan_P-PH000-ST002-AC004.md` |
| AC004 Operating-Model Analysis | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/analysis/analysis_P-PH000-ST002-AC004_operating-model-and-reconciliation-policy.md` |
| AC004 External Review | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/analysis/analysis_P-PH000-ST002-AC004_gate-001-external-review.md` |
| AC004 GATE-001 Proposal | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/proposal/proposal_P-PH000-ST002-AC004-GATE-001_operating-model-disposition.md` |
| Status Ledger | `prompt/artifacts/tasks/P/status/status_program.yaml` |
| Status Narrative | `prompt/artifacts/tasks/P/status/status_program.md` |
| ST002 Stream Plan | `prompt/artifacts/tasks/P/workspace/PH000/ST002/plan_P-PH000-ST002.md` |
| PH000 Phase Plan | `prompt/artifacts/tasks/P/workspace/PH000/plan_P-PH000.md` |
| Program Roadmap | `prompt/artifacts/tasks/P/ssot/roadmap_P-PROGRAM_phase0.md` |
| Wrap-Up Skill | `prompt/skills/wrap-up/SKILL.md` |
| Implementation Guideline | `prompt/templates/consultant/workspace/guideline_workspace_implementation.md` |

## VI. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.2.0 | 2026-03-24 | Amendment | Added explicit drift-verification criteria to SPEC-001 per GATE-001 approval findings. |
| v1.1.0 | 2026-03-24 | Amendment | Amended the AC004 first operationalization `task_specification` after the `GATE-001` recycle decision. Named the approved operating protocol and reminder surfaces, added the conditional-approval amendment rule, and constrained TK004 from pushing status-operating rules into AGENTS or standards surfaces. |
| v1.0.0 | 2026-03-23 | Initial | Authored the AC004 first operationalization `task_specification` as a pre-gate readiness artifact so the client can review the bounded V1 execution contract before approving `GATE-001`. |
