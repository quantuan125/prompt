---
artifact_type: 'IMPLEMENTATION'
implementation_type: 'task_specification'
initiative_id: 'P'
initiative_code: 'PROGRAM'
phase: '0'
stream_id: 'P-PH000-ST002'
activity_id: 'P-PH000-ST002-AC003'
task_id: 'P-PH000-ST002-AC003-TK008..P-PH000-ST002-AC004-GATE-001'
version: '1.0.0'
date: '2026-03-23'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST002/AC003/plan_P-PH000-ST002-AC003.md'
execution_audience: 'consultant'
purpose: 'Consultant-owned orchestration specification for AC003 GATE-001 closeout, developer-owned package and planning activation work, reviewer verification over the full developer slice, and consultant-only session-note finalization.'
---

# IMPLEMENTATION (Task Specification): AC003 GATE-001 Closeout And AC004 Activation

## I. PURPOSE & AUTHORITY

- **Purpose**: Define the bounded orchestration HOW for closing AC003 `GATE-001`, activating AC004 planning, and preserving a clean consultant -> developer -> reviewer -> consultant execution boundary.
- **Authority chain**: The AC003 activity plan and approved consultant plan authorize this closeout slice -> this artifact specifies the exact role-owned execution model -> the developer worker executes Step 2 + Step 3 + Step 4 end-to-end -> the reviewer verifies the whole developer slice and drives recycle if needed -> the main consultant performs Step 5 only after convergence.
- **Audience**: Main `LLM_Consultant` as orchestrator and finalizer; delegated `LLM_Developer` as the sole mutation owner for Step 2 + Step 3 + Step 4; delegated `LLM_Reviewer` as the sole verifier for the whole developer slice.
- **Boundary**: This artifact does NOT hold a GDR. The authoritative gate decision remains in the AC003 `gate_disposition` proposal.

## II. TASK SCOPE

- **Governing closeout boundary**:
  - incorporate the external review into the live AC003 `GATE-001` package
  - record the Client `APPROVE` decision and update the plan-state surfaces that close AC003
  - activate AC004 planning by authoring its standalone activity plan with both a consultation gate and an implementation gate
  - defer consultant-only session notes and notes-register finalization until the developer and reviewer both confirm completion
- **Primary mutation outputs owned by the developer worker**:
  - `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC003/proposal/proposal_P-PH000-ST002-AC003-GATE-001_initial-population-acceptance-disposition.md`
  - `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC003/plan_P-PH000-ST002-AC003.md`
  - `prompt/artifacts/tasks/P/workspace/PH000/ST002/plan_P-PH000-ST002.md`
  - `prompt/artifacts/tasks/P/workspace/PH000/plan_P-PH000.md`
  - `prompt/artifacts/tasks/P/ssot/roadmap_P-PROGRAM_phase0.md`
  - `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/plan_P-PH000-ST002-AC004.md`
  - `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC003/dev-report/dev-report_P-PH000-ST002-AC003_gate-001-closeout-and-ac004-activation.md`
- **Primary verification output owned by the reviewer worker**:
  - `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC003/verification/verification_P-PH000-ST002-AC003_gate-001-closeout-and-ac004-activation.md`
- **Primary consultant-only finalization outputs**:
  - `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC003/snotes/snotes_P-PH000-ST002-AC003-SES001.md`
  - `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/snotes/snotes_P-PH000-ST002-AC004-SES001.md`
  - `prompt/artifacts/tasks/P/workspace/PH000/ST002/notes_P-PH000-ST002.md`
- **Hard boundaries**:
  - do NOT mutate `prompt/artifacts/tasks/P/status/status_program.yaml`
  - do NOT mutate `prompt/artifacts/tasks/P/status/status_program.md`
  - do NOT create a sub-consultant branch for this closeout slice

## III. SPECIFICATION ITEMS

### SPEC-001 — Consultant orchestration setup

| Field | Detail |
|:--|:--|
| Requirement Source | Approved consultant implementation plan for the closeout slice |
| Output | This task specification, worker assignments, and bounded write scopes |
| Acceptance Criteria | The orchestration spec names the developer-owned surfaces, reviewer-owned verification surface, consultant-only finalization surfaces, and the recycle-loop control posture |
| Status | `open` |

#### Implementation Detail

1. The main consultant authors this task specification before any delegated mutation begins.
2. The main consultant is the control plane for the slice:
   - commissions the developer worker first
   - commissions the reviewer worker only after the developer's initial handoff
   - routes recycle findings from reviewer to developer
   - blocks Step 5 until both workers confirm completion
3. Worker model:
   - developer worker: `gpt-5.4-mini`, reasoning `xhigh`
   - reviewer worker: `gpt-5.4`, reasoning `medium`
4. The developer owns all mutations in Step 2 + Step 3 + Step 4.
5. The reviewer owns verification of the entire developer slice and the verification artifact.
6. The consultant owns Step 5 only and does not bypass the reviewer verdict.

### SPEC-002 — Developer-owned execution wave for Step 2 + Step 3 + Step 4

| Field | Detail |
|:--|:--|
| Requirement Source | Consultant-approved closeout plan; AC003 proposal/package housekeeping needs; AC004 activation requirement |
| Output | Updated AC003 proposal and plan surfaces, activated AC004 activity plan, and developer handoff evidence |
| Acceptance Criteria | All Step 2 + Step 3 + Step 4 surfaces are updated coherently; AC004 dual-gate plan exists; status ledger and narrative remain untouched; developer DEV-REPORT exists |
| Status | `open` |

#### Implementation Detail

1. The developer worker owns one continuous mutation slice spanning:
   - external-review integration into the live AC003 gate package
   - AC003 `GATE-001` approval recording and plan-state closure updates
   - AC004 standalone plan authoring and activation-state updates
2. The developer must update the AC003 proposal to:
   - add `external_review_reference` in frontmatter
   - add the external review to the Evidence Index
   - preserve reviewer-verdict sourcing in the verification artifact only
   - record the Client `APPROVE` decision in the GDR using `2026-03-23`
3. The developer must update AC003 closure surfaces to a coherent approved state:
   - AC003 activity plan gate row and activity status
   - ST002 stream plan activity register and AC003/AC004 activity stubs
   - PH000 phase snapshot
   - P roadmap compact delivery snapshot
4. The developer must create the AC004 standalone activity plan with both future gates explicitly modeled:
   - `GATE-001`: consultation approval of the AC004 operating model
   - `GATE-002`: implementation acceptance after the first AC004 operationalization slice
5. The AC004 plan must encode the first implementation concern as the post-gate reconciliation of the accepted baseline, including the known `P-PH000-ST002-AC003` ledger-plan drift.
6. The developer must NOT:
   - finalize activity session notes
   - update the stream notes register
   - mutate the accepted status ledger or narrative
7. The developer must produce a DEV-REPORT for this closeout slice that summarizes:
   - files changed
   - approval-state transitions applied
   - AC004 plan architecture introduced
   - explicit confirmation that the status artifacts were left untouched

### SPEC-003 — Reviewer verification over the full developer slice

| Field | Detail |
|:--|:--|
| Requirement Source | Consultant-approved closeout plan; verification requirement for the whole developer slice |
| Output | Reviewer-owned verification artifact for the closeout and activation slice |
| Acceptance Criteria | Reviewer confirms package integrity across the full developer slice or returns recycle findings against that same bounded slice |
| Status | `open` |

#### Implementation Detail

1. After the developer worker completes the initial handoff, the consultant commissions one reviewer worker to verify the whole developer slice.
2. Reviewer scope is end-to-end across all developer-owned surfaces, not per-file spot checks only.
3. The reviewer must verify:
   - external review is linked correctly into the AC003 proposal package
   - GDR fields reflect the approved state consistently
   - AC003 closure is coherent across proposal, activity plan, stream plan, phase plan, and roadmap
   - AC004 activation is coherent across the new activity plan and upstream navigation surfaces
   - AC004 contains both a consultation gate and an implementation gate
   - the accepted status ledger and narrative were not mutated
   - the developer DEV-REPORT accurately reflects the slice
4. The reviewer records findings and verdict in the canonical closeout verification artifact.
5. If findings exist, the reviewer returns them to the consultant as one bounded recycle package covering the whole developer slice.

### SPEC-004 — Consultant recycle-loop control

| Field | Detail |
|:--|:--|
| Requirement Source | User directive that the consultant must monitor and orchestrate between reviewer and developer until both confirm completion |
| Output | Controlled recycle loop with stable scope and stable role boundaries |
| Acceptance Criteria | Any reviewer findings are routed back to the developer without changing the work boundary; reviewer re-assesses the same bounded slice; consultant does not proceed to Step 5 early |
| Status | `open` |

#### Implementation Detail

1. If the reviewer returns findings, the consultant:
   - interprets the findings against this task specification
   - routes exact remediation instructions back to the developer worker
   - keeps the write scope unchanged unless a genuine scope conflict is discovered
2. The developer remediates the bounded slice and refreshes the DEV-REPORT if needed.
3. The reviewer re-assesses the same slice and updates the verification artifact rather than creating a second unrelated review family.
4. The consultant repeats the loop until:
   - developer confirms all assigned surfaces are complete
   - reviewer confirms the full slice passes
5. The consultant may inspect artifacts for coherence during the loop but does not take over developer-owned mutations unless the worker fails irrecoverably.

### SPEC-005 — Consultant-only Step 5 finalization

| Field | Detail |
|:--|:--|
| Requirement Source | User directive that Step 5 begins only after developer and reviewer confirm completion |
| Output | Final AC003 and AC004 session-note lineage plus updated stream notes register |
| Acceptance Criteria | AC003 session notes reflect closure, AC004 session notes capture activation, and the stream notes register indexes the new AC004 session |
| Status | `open` |

#### Implementation Detail

1. The consultant begins Step 5 only after SPEC-002 and SPEC-003 have converged.
2. The consultant updates AC003 SES001 to record:
   - receipt and incorporation of the external review
   - Client `APPROVE` recorded in the GDR
   - AC003 closure state
   - handoff of the known drift into AC004
3. The consultant creates AC004 SES001 to record:
   - same-session activation of AC004 planning
   - rationale for the dual-gate architecture
   - first downstream implementation concerns
4. The consultant updates the ST002 stream notes register JIT to add the AC004 session note row.

## IV. IMPLEMENTATION SEQUENCE

1. Consultant authors this task specification.
2. Consultant commissions the developer worker for SPEC-002.
3. Developer updates all Step 2 + Step 3 + Step 4 surfaces and produces the closeout DEV-REPORT.
4. Consultant commissions the reviewer worker for SPEC-003.
5. Reviewer verifies the entire developer slice.
6. If needed, consultant runs SPEC-004 recycle loops between reviewer and developer until both confirm completion.
7. Only then does the consultant perform SPEC-005 finalization.

## V. REFERENCES

| Document | Path |
|:--|:--|
| Governing Plan | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC003/plan_P-PH000-ST002-AC003.md` |
| Existing AC003 Implementation Artifact | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC003/implementation/implementation_P-PH000-ST002-AC003_initial-backfill-and-gate-001-orchestration.md` |
| AC003 Gate Proposal | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC003/proposal/proposal_P-PH000-ST002-AC003-GATE-001_initial-population-acceptance-disposition.md` |
| External Review Analysis | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC003/analysis/analysis_P-PH000-ST002-AC003_gate-001-external-review.md` |
| Stream Plan | `prompt/artifacts/tasks/P/workspace/PH000/ST002/plan_P-PH000-ST002.md` |
| Phase Plan | `prompt/artifacts/tasks/P/workspace/PH000/plan_P-PH000.md` |
| Proposal Guideline | `prompt/templates/consultant/workspace/guideline_workspace_proposal.md` |
| Verification Guideline | `prompt/templates/consultant/workspace/guideline_workspace_verification.md` |
| Notes Guideline | `prompt/templates/consultant/workspace/guideline_workspace_notes.md` |

## VI. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-03-23 | Initial | Created the consultant-owned closeout orchestration task specification for AC003 `GATE-001` package amendment, developer-owned approval and AC004 activation work, reviewer verification across the full developer slice, consultant-controlled recycle loops, and consultant-only session-note finalization. |
