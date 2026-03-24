---
artifact_type: 'IMPLEMENTATION'
implementation_type: 'task_specification'
initiative_id: 'T104'
initiative_code: 'CWS'
phase: '1'
stream_id: 'T104-PH001-ST008'
activity_id: 'T104-PH001-ST008-AC001.9'
task_id: 'T104-PH001-ST008-AC001.9-TK003.1'
version: '1.0.0'
date: '2026-03-24'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.9/plan_T104-PH001-ST008-AC001.9.md'
execution_audience: 'developer'
purpose: 'Same-gate hardening specification for AC001.9 GATE-001: register TK003.1 under plan authority, normalize the lifecycle implementation specification, integrate the external review into the live gate package, and prepare the package for orchestrator review and same-session client closure.'
---

# IMPLEMENTATION (Task Specification): AC001.9 GATE-001 Package Hardening

## I. PURPOSE & AUTHORITY

- **Purpose**: This artifact specifies the HOW for hardening the AC001.9 `GATE-001` package without starting Phase 2. The scope is limited to same-gate package normalization, external-review integration, and closure-readiness.
- **Authority chain**: AC001.9 activity plan authorizes tracked work -> this artifact specifies HOW for `TK003.1` -> orchestrator review confirms spec compliance -> client decision is recorded in the proposal GDR.
- **Audience**: LLM_Developer (primary execution owner for the hardening edits), LLM_Consultant (orchestrator review and final closeout only).
- **This artifact does NOT hold a GDR.** Final `GATE-001` decision authority remains exclusively in the `gate_disposition` proposal.
- **Boundary**: Developer execution under this artifact MUST stop with a closure-ready package in `pending` state. The developer MUST NOT record final GDR approval fields and MUST NOT mark `GATE-001` passed.

## II. TASK SCOPE

- **Governing plan task**: `T104-PH001-ST008-AC001.9-TK003.1`
- **Trigger**: The external review now exists as part of the client-facing `GATE-001` evidence set, but the activity plan, the current lifecycle implementation specification, and the live proposal package do not yet encode that same-gate hardening state coherently.
- **Deliverable contract**: A plan-authorized, closure-ready `GATE-001` package containing the hardened proposal, the integrated external review, and corrected implementation-specification lineage, with the gate still pending orchestrator review and explicit client approval.
- **Write scope**:
  - `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.9/plan_T104-PH001-ST008-AC001.9.md`
  - `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.9/implementation/implementation_T104-PH001-ST008-AC001.9_recyclable-loop-artifact-governance.md`
  - `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.9/analysis/analysis_T104-PH001-ST008-AC001.9_gate-001-external-review.md`
  - `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.9/proposal/proposal_T104-PH001-ST008-AC001.9-GATE-001_gir-disposition-package.md`

## III. NON-NEGOTIABLE EXECUTION RULES

1. Treat this work as a **same-gate hardening pass**. Do NOT create a new gate ID.
2. Add a dotted sub-task `TK003.1` and place it immediately before `GATE-001` in the activity plan task register.
3. Keep all Phase 2 tasks (`TK004` through `GATE-002`) untouched except for dependency references that must now flow through `GATE-001` after `TK003.1`.
4. Do NOT create a VERIFICATION artifact. `GATE-001` remains consultation-only.
5. Do NOT close the GDR. Leave `Client Decision`, `Gate Status After Decision`, `Decision Date`, and `Decision Reference` pending for orchestrator closeout.
6. Work only inside the write scope listed above. Do not modify stream-plan, notes-register, or Phase 2 guideline/template files in this pass.

## IV. SPECIFICATION ITEMS

### SPEC-001 — Amend the AC001.9 activity plan for same-gate hardening

| Field | Detail |
|:--|:--|
| Requirement Source | `guideline_workspace_plan.md` §IV.E, §VI.D, §VI.K, §VI.L |
| Output | Updated `plan_T104-PH001-ST008-AC001.9.md` |
| Acceptance Criteria | `TK003.1` exists immediately before `GATE-001`; `GATE-001` depends on `TK003.1`; gate entry criteria require the hardened package; no Phase 2 task starts before `GATE-001` |
| Status | `open` |

#### Implementation Detail

- Add `TK003.1` to the Task Register with:
  - **Name**: Integrate external review and harden `GATE-001` package
  - **Status**: `planned`
  - **Owner**: `LLM_Developer`
  - **Depends On**: `TK003`
  - **Target**: `analysis/`, `proposal/`, `implementation/`, activity plan
  - **Reference**: this new implementation artifact
  - **Action**: `—`
- Move `GATE-001` to depend on `TK003.1`.
- Update the `GATE-001` entry-criteria bullets so they require:
  - `TK001` through `TK003.1` completed
  - consultation package contains plan, session notes, gap analysis, external review, hardened proposal, and pending GDR
- Add a detailed task section for `TK003.1` under `## III. TASKS (DETAILED)` with purpose, deliverables, scope, and success criteria aligned to SPEC-002 through SPEC-004 below.
- Update the Links Register to include:
  - the new `TK003.1` implementation artifact
  - the `GATE-001` external review analysis artifact
- Bump plan version and changelog to record the same-gate hardening pass.

### SPEC-002 — Normalize the existing AC001.9 lifecycle implementation specification

| Field | Detail |
|:--|:--|
| Requirement Source | Current package inconsistency identified by AC001.9 external review |
| Output | Updated `implementation_T104-PH001-ST008-AC001.9_recyclable-loop-artifact-governance.md` |
| Acceptance Criteria | No remaining `TK013`/`TK014` references; audience ownership matches actual task map; phase sequence ends at `TK012` plus `GATE-002` |
| Status | `open` |

#### Implementation Detail

- Correct the frontmatter `task_id` so it no longer implies nonexistent tasks.
- Correct Section I audience mapping so it matches the real plan:
  - Consultant: `TK001` through `TK004` and `TK012`
  - Developer: `TK005` through `TK010`
  - Reviewer: `TK011`
  - Client: `GATE-001`, `GATE-002`
- Correct Section II governing task range text.
- Correct SPEC-001 implementation detail text that currently tells the author to populate `TK001–TK014 + GATE-001 + GATE-002`.
- Re-read the full file and fix any other stale numbering or role-mapping references that contradict the actual sequence in Section V.
- Bump version/date/changelog to record the numbering and ownership normalization.

### SPEC-003 — Revise the AC001.9 external-review analysis to match the hardened package reality

| Field | Detail |
|:--|:--|
| Requirement Source | Same-gate hardening decision for `GATE-001` |
| Output | Updated `analysis_T104-PH001-ST008-AC001.9_gate-001-external-review.md` |
| Acceptance Criteria | Review still agrees with all four GIR recommendations, but now explicitly identifies proposal-package integration and broader implementation-spec drift as remaining hardening items; recommendation is approval-ready after hardening, not as-is |
| Status | `open` |

#### Implementation Detail

- Preserve the external review's substantive agreement with GIR-001 through GIR-004.
- Replace the “only two minor issues” framing with a fuller finding set that reflects current package reality:
  - external review not yet integrated into the live proposal package
  - implementation-spec inconsistency is broader than frontmatter only
  - T103 carry-forward remains informational, not blocking
- Update the Executive Summary, Findings / Gap Register, Concerns / Risks, Overall Gate Recommendation, Downstream Actions, References, and Changelog accordingly.
- The final recommendation in this artifact should be equivalent to:
  - governance model is sound
  - package is ready for client approval **after** same-gate hardening
  - hardening is not a Phase 2 scope expansion

### SPEC-004 — Revise the live GATE-001 proposal into the closure-ready package

| Field | Detail |
|:--|:--|
| Requirement Source | `guideline_workspace_proposal.md` §V.B, same-gate hardening requirements |
| Output | Updated `proposal_T104-PH001-ST008-AC001.9-GATE-001_gir-disposition-package.md` |
| Acceptance Criteria | Proposal frontmatter references the external review; Gate Package Index includes the external review; Evidence Index includes the external review; proposal reflects `TK003.1` same-gate hardening state; GDR remains pending |
| Status | `open` |

#### Implementation Detail

- Change proposal frontmatter `task_id` from `TK003` to `TK003.1`.
- Add `external_review_reference` frontmatter pointing to the AC001.9 external-review analysis.
- Update the Executive Summary so the package is described as the **hardened same-gate package** rather than the original `TK003` package only.
- Update Gate Package Index:
  - keep the original consultation artifacts
  - add the external review as a deliverable produced by `TK003.1`
  - relabel this proposal row so it is clearly the hardened same-gate package
- Update Evidence Index to include the external review as current primary evidence.
- Update the Consultant Gate Recommendation section so it references the integrated external review while keeping the gate consultation-only.
- Keep the GDR in pending state for developer execution. Do not write final client approval fields.
- Add references for:
  - the external review
  - the new `TK003.1` implementation artifact
- Bump version/date/changelog to record the same-gate hardening update.

### SPEC-005 — Produce a closure-ready developer handoff summary for the orchestrator

| Field | Detail |
|:--|:--|
| Requirement Source | Orchestrator review workflow for this session |
| Output | No new repo artifact; include in worker final report |
| Acceptance Criteria | Worker final message lists files changed, spec items completed, any unresolved issues, and explicit confirmation that the GDR was left pending |
| Status | `open` |

#### Implementation Detail

- In the worker's final report, list each changed file.
- State which SPEC items were completed.
- State whether any ambiguity or unresolved issue remains.
- Explicitly confirm:
  - no Phase 2 files were touched
  - no VERIFICATION artifact was created
  - `GATE-001` GDR was left pending for orchestrator closeout

## V. IMPLEMENTATION SEQUENCE

```
Same-Gate Hardening Pass
  SPEC-001  Amend AC001.9 activity plan for TK003.1
  SPEC-002  Normalize lifecycle implementation specification
  SPEC-003  Revise external-review analysis
  SPEC-004  Revise live GATE-001 proposal package
  SPEC-005  Return closure-ready handoff summary to orchestrator
```

**Execution note**: SPEC-001 through SPEC-004 are tightly coupled and SHOULD be executed in one bounded pass by a single developer. The orchestrator then performs review and final gate-close edits separately.

## VI. REFERENCES

| Document | Path |
|:--|:--|
| Governing Plan | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.9/plan_T104-PH001-ST008-AC001.9.md` |
| Existing Lifecycle Implementation Spec | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.9/implementation/implementation_T104-PH001-ST008-AC001.9_recyclable-loop-artifact-governance.md` |
| Gap Analysis | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.9/analysis/analysis_T104-PH001-ST008-AC001.9_recyclable-loop-artifact-governance-gaps.md` |
| External Review | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.9/analysis/analysis_T104-PH001-ST008-AC001.9_gate-001-external-review.md` |
| Live GATE-001 Proposal | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.9/proposal/proposal_T104-PH001-ST008-AC001.9-GATE-001_gir-disposition-package.md` |
| Implementation Guideline | `prompt/templates/consultant/workspace/guideline_workspace_implementation.md` |
| Plan Guideline | `prompt/templates/consultant/workspace/guideline_workspace_plan.md` |
| Proposal Guideline | `prompt/templates/consultant/workspace/guideline_workspace_proposal.md` |

## VII. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-03-24 | Initial | Task specification for AC001.9 same-gate hardening: register `TK003.1`, normalize the lifecycle implementation specification, revise the external review to match current package reality, and update the live `GATE-001` proposal into a closure-ready package while keeping the GDR pending for orchestrator closeout. |
