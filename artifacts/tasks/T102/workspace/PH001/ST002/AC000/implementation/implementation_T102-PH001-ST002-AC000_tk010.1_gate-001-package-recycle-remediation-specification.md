---
artifact_type: 'IMPLEMENTATION'
implementation_type: 'remediation_specification'
initiative_id: 'T102'
initiative_code: 'CWD'
phase: '1'
stream_id: 'T102-PH001-ST002'
activity_id: 'T102-PH001-ST002-AC000'
gate_id: 'T102-PH001-ST002-AC000-GATE-001'
task_id: 'T102-PH001-ST002-AC000-TK010.1'
version: '1.0.0'
date: '2026-03-28'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/plan_T102-PH001-ST002-AC000.md'
verification_reference: 'prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/analysis/analysis_T102-PH001-ST002-AC000-TK009_gate-001-external-review.md'
proposal_reference: 'prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/proposal/proposal_T102-PH001-ST002-AC000_gate-001-disposition.md'
purpose: 'Consultant-authored recycle remediation specification for repairing the AC000 Gate-001 package and planning surfaces before later re-presentation.'
---

# IMPLEMENTATION (Remediation Specification): AC000 Gate-001 Package Recycle Remediation

## I. PURPOSE & AUTHORITY
- Purpose: Specify the exact repo-tracked package repairs required to convert the current AC000 Gate-001 package into an active recycle/reassessment package that includes the new pre-gate seed artifact and preserves the existing external review as historical evidence.
- Authority chain: AC000 plan authorizes `TK010.1` -> this artifact specifies HOW the recycle remediation is executed -> consultant review accepts or rejects the assistant's output -> later sessions may commission fresh external review and client re-presentation.
- Audience: Assistant sub-agent executor for straightforward repo edits; main `LLM_Consultant` for review and recycle-loop control.
- This artifact does NOT hold a GDR. Gate decision authority remains in the Gate-001 gate-disposition proposal.
- Consultation-only exception note: this recycle loop has no reviewer-owned verification artifact. `verification_reference` is populated with the historical Gate-001 external review because it is the closest existing gate-quality surface that triggered the recycle posture.

## II. REMEDIATION SCOPE
- Gate: `T102-PH001-ST002-AC000-GATE-001`
- Trigger: Gate-001 recycle posture driven by consultant assessment plus client QA on package completeness, downstream seeding, and proposal/plan coherence.
- Governing plan task: `T102-PH001-ST002-AC000-TK010.1`
- Findings addressed:
  - `RC-001` Missing pre-gate developer-facing seed artifact positioning in the AC000 plan and Gate-001 package
  - `RC-002` Gate-001 proposal posture still reflects approval-oriented packaging instead of recycle/reassessment packaging
  - `RC-003` Current external review must remain unchanged but must be demoted to historical/outdated evidence in the refreshed package
  - `RC-004` ST002 stream-plan wording must no longer conflict with the AC000 recycle and seeded-downstream posture

## III. REMEDIATION ITEMS

### REM-001 — Reorder the AC000 plan and encode the recycle loop

| Field | Detail |
|:--|:--|
| Finding Reference | `RC-001`, `RC-002` |
| Revision Deliverable | Updated `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/plan_T102-PH001-ST002-AC000.md` |
| Expected Format | Task Register updates, detailed-section reordering, Gate-001 Recycle Re-entry Block, and changelog amendment |
| Acceptance Criteria | `TK010` is moved above `GATE-001`; `TK010.1`, `TK010.2`, and `TK010.3` are inserted immediately after `GATE-001`; `GATE-001` includes the required recycle fields; `TK011`-`TK015` remain later and blocked; the stale `TK008` action-path typo is corrected. |
| Resolution Status | `open` |

#### Implementation Detail

Apply these exact plan-level outcomes:
- `TK010` becomes the pre-gate seed task and depends on `TK009`
- `GATE-001` changes from passive planned gate text to an active recycle/reassessment gate section
- `TK010.1` = author remediation specification
- `TK010.2` = execute remediation per specification
- `TK010.3` = consultant review of remediation output and package refresh readiness
- `TK011`-`TK015` remain the later post-gate implementation-backed stack
- the plan must no longer say or imply that AC001-AC004 may begin from the current Gate-001 package
- changelog records the recycle-loop amendment and the new implementation artifacts

### REM-002 — Refresh the Gate-001 proposal into recycle-package posture

| Field | Detail |
|:--|:--|
| Finding Reference | `RC-001`, `RC-002`, `RC-003` |
| Revision Deliverable | Updated `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/proposal/proposal_T102-PH001-ST002-AC000_gate-001-disposition.md` |
| Expected Format | Gate Package Index, Evidence Index, GIR register, consultant recommendation, recycle reassessment path, and changelog amendment |
| Acceptance Criteria | The proposal recommends `RECYCLE`; the Gate Package Index includes `TK010` and `TK010.1` as active package items; the current `TK009` external review is removed from active package items and retained only in the Evidence Index with an explicit historical/outdated note; recycle reassessment tasks are explicit; GDR client-decision fields remain pending. |
| Resolution Status | `open` |

#### Implementation Detail

Apply these exact proposal-level outcomes:
- `Consultant recommendation` becomes `RECYCLE`
- `GATE PACKAGE / Gate Package Index` contains active current-cycle items only:
  - AC000 activity plan
  - ST002 stream plan
  - calibrated scope brief
  - Gate-disposition proposal
  - `TK010` downstream-seed task specification
  - `TK010.1` recycle remediation specification
- `Evidence Index` retains the current `TK009` external review with wording equivalent to `historical/outdated pre-remediation review; retained for traceability only`
- `Recycle reassessment path` names `TK010.1`, `TK010.2`, and `TK010.3`
- `Downstream enforcement` states that no downstream execution begins from the current recycle package
- GDR values remain:
  - `Client Decision = pending`
  - `Gate Status After Decision = pending`
  - decision recording is not altered in this remediation cycle

### REM-003 — Align the ST002 stream plan to the recycle and seeded-downstream posture

| Field | Detail |
|:--|:--|
| Finding Reference | `RC-004` |
| Revision Deliverable | Updated `prompt/artifacts/tasks/T102/workspace/PH001/ST002/plan_T102-PH001-ST002.md` |
| Expected Format | Stream-plan stub refresh limited to AC000 / downstream sequencing language and changelog amendment |
| Acceptance Criteria | The ST002 stream plan no longer contradicts the AC000 recycle package by implying that current Gate-001 approval directly starts downstream execution; AC000 summary text acknowledges the pre-gate seed artifact and recycle loop; existing activity identities remain intact. |
| Resolution Status | `open` |

#### Implementation Detail

Apply these exact stream-level outcomes:
- keep the Activity Register identities `AC000`-`AC004` unchanged
- refresh AC000 deliverable wording so it references:
  - calibrated scope brief
  - Gate-001 recycle package
  - pre-gate downstream seed artifact
  - later GATE-002 implementation stack
- do not introduce new activities, new gates, or guideline changes
- do not claim AC001-AC004 are released for execution by the current recycle package

## IV. IMPLEMENTATION SEQUENCE
1. Read `TK010` and this `TK010.1` artifact together before editing any tracked file.
2. Edit the AC000 activity plan to encode `TK010`, the recycle loop, and corrected gate ordering.
3. Edit the Gate-001 proposal to switch from approval-oriented posture to recycle-package posture.
4. Edit the ST002 stream plan to remove the remaining sequencing contradiction.
5. Stop after the three tracked files above are updated. Do not create or edit any fresh external-review artifact in this cycle.

## V. REFERENCES

| Document | Path |
|:--|:--|
| Governing Plan | `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/plan_T102-PH001-ST002-AC000.md` |
| Historical External Review | `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/analysis/analysis_T102-PH001-ST002-AC000-TK009_gate-001-external-review.md` |
| Gate-Disposition Proposal | `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/proposal/proposal_T102-PH001-ST002-AC000_gate-001-disposition.md` |
| Downstream Seed Specification | `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/implementation/implementation_T102-PH001-ST002-AC000_tk010_gate-001-downstream-seed-task-specification.md` |
| Parent Stream Plan | `prompt/artifacts/tasks/T102/workspace/PH001/ST002/plan_T102-PH001-ST002.md` |

## VI. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-03-28 | Initial | Created the Gate-001 recycle remediation specification for AC000 `TK010.1`, defining the exact AC000 plan, Gate-001 proposal, and ST002 stream-plan repairs required before later external review and client re-presentation. |
