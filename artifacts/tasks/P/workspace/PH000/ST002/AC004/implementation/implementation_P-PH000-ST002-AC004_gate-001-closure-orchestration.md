---
artifact_type: 'IMPLEMENTATION'
implementation_type: 'task_specification'
initiative_id: 'P'
initiative_code: 'PROGRAM'
phase: '0'
stream_id: 'P-PH000-ST002'
activity_id: 'P-PH000-ST002-AC004'
task_id: 'P-PH000-ST002-AC004-TK003.1'
gate_id: 'P-PH000-ST002-AC004-GATE-001'
version: '1.0.0'
date: '2026-03-24'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/plan_P-PH000-ST002-AC004.md'
execution_audience: 'consultant'
purpose: 'Deterministic gate-closure orchestration specification for P-PH000-ST002-AC004-GATE-001. Records the client APPROVE decision, resolves all assessment findings, promotes the canonical external review, aligns all summary surfaces, and prepares TK004 for commissioning in the next session.'
---

# IMPLEMENTATION (Task Specification): AC004 GATE-001 Closure Orchestration

## I. PURPOSE & AUTHORITY

- Purpose: Specify the exact orchestration steps to close AC004 `GATE-001` as `APPROVE`, resolve all five independent-assessment findings, align all downstream and summary surfaces, and leave TK004 unblocked for developer commissioning in the next session.
- Authority chain: The client's approval decision in this session authorizes this orchestration. The AC004 activity plan (`plan_P-PH000-ST002-AC004.md`) governs the gate lifecycle. `guideline_workspace_proposal.md` §VII.D governs GDR recording. This artifact specifies HOW the closure is executed.
- Audience: `LLM_Consultant` (primary executor in the current session). This is a consultant-orchestrated specification, not developer-owned implementation.
- This artifact does NOT hold a GDR. The gate decision is recorded in the gate-disposition proposal per `guideline_workspace_proposal.md` §VII.

## II. TASK SCOPE

- Governing plan context: `P-PH000-ST002-AC004-TK003.1` (correction pass) and `GATE-001` (gate lifecycle closure)
- Trigger: The corrected same-gate package has been independently assessed as decision-complete. The client has issued a straight `APPROVE` decision. The gate-closure orchestration requires coordinated updates across 8+ files spanning the proposal, activity plan, external review, implementation specification, three summary surfaces, and session notes.
- Deliverable contract:
  - Updated `proposal_P-PH000-ST002-AC004-GATE-001_operating-model-disposition.md` with approving GDR
  - Promoted `analysis_P-PH000-ST002-AC004_gate-001-external-review.md` (v2.0.0 replaces v1.1.0)
  - Updated `plan_P-PH000-ST002-AC004.md` with gate closure and Recycle Re-entry Block
  - Updated `implementation_P-PH000-ST002-AC004_first-operationalization-task-specification.md` with drift verification criteria
  - Updated `plan_P-PH000-ST002.md` (stream plan — approved posture)
  - Updated `plan_P-PH000.md` (phase plan — approved snapshot)
  - Updated `roadmap_P-PROGRAM_phase0.md` (roadmap — advanced milestone)
  - New `snotes_P-PH000-ST002-AC004-SES004.md` (approval decision trail)
  - Updated `notes_P-PH000-ST002.md` (SES004 registration)

## III. SPECIFICATION ITEMS

### SPEC-001 — Promote External Review to Canonical Path

| Field | Detail |
|:--|:--|
| Requirement Source | Independent assessment FINDING-1; `guideline_workspace_proposal.md` §V.B.B (Evidence Index integrity) |
| Output | Single canonical external review at `analysis_P-PH000-ST002-AC004_gate-001-external-review.md` containing v2.0.0 content |
| Acceptance Criteria | (1) The canonical path contains the v2.0.0 content. (2) The `_new` working file is removed. (3) No other artifact references the `_new` path. |
| Status | `open` |

#### Implementation Detail

1. Read the full content of `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/analysis/analysis_P-PH000-ST002-AC004_gate-001-external-review_new.md` (v2.0.0).
2. Overwrite `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/analysis/analysis_P-PH000-ST002-AC004_gate-001-external-review.md` with the v2.0.0 content.
3. Delete the `_new` file.
4. No reference updates are needed in the proposal or other artifacts because they already point to the canonical (non-`_new`) path — the content at that path simply becomes v2.0.0.

### SPEC-002 — Update Proposal GDR and Resolve Housekeeping Findings

| Field | Detail |
|:--|:--|
| Requirement Source | Client APPROVE decision; `guideline_workspace_proposal.md` §VII.C and §VII.D step 4; Independent assessment FINDING-2 and FINDING-3 |
| Output | Updated `proposal_P-PH000-ST002-AC004-GATE-001_operating-model-disposition.md` with approving GDR and resolved housekeeping issues |
| Acceptance Criteria | (1) GDR records `Client Decision = APPROVE`, `Gate Status After Decision = completed`, correct Decision Date and Decision Reference. (2) Consultant Recommendation updated to `APPROVE`. (3) All six GIR Client Decision values updated to `approved`. (4) Duplicate h2 heading removed (FINDING-2). (5) Gate Package Index `Acceptance` values are consistent (FINDING-3). (6) Version bumped and changelog updated. |
| Status | `open` |

#### Implementation Detail

**Frontmatter changes:**
- `version`: `'1.1.0'` → `'1.2.0'`
- `date`: `'2026-03-24'` (unchanged)
- `status`: `'draft'` → `'completed'`
- `purpose`: Update to reflect the approved gate, not the recycle recording.

**Section I (Executive Summary):**
- Update the "Current gate state" bullet to reflect `APPROVE` on 2026-03-24 instead of the recycle narrative.
- Update the "Purpose of this version" bullet to reflect recording the approval decision.

**Section II.A (Gate Package Index):**
- Change `Acceptance` for all deliverables from `accepted-provisional` to `accepted` (FINDING-3 resolution — with gate approved, provisional status is no longer appropriate).

**Section III (Disposition Summary Register):**
- Update all six `Client Decision` cells from `same-gate reassessment pending` to `approved`.

**Section V (Consultant Gate Recommendation):**
- Update `Consultant recommendation` from `RECYCLE` to `APPROVE`.
- Update the "Conditions and/or deferrals" text to reflect that the recycle is resolved and the package is approved.
- Update the "Downstream enforcement" text to reflect that TK004 is now unblocked.

**Section VI (Gate Decision Record):**
- Remove the duplicate `## Gate Decision Record` h2 heading that follows `## VI. GATE DECISION RECORD (GDR)` (FINDING-2). Keep only the section-numbered heading.
- Update the GDR table:

| Field | New Value |
|:--|:--|
| Consultant Recommendation | `APPROVE` |
| Client Decision | `APPROVE` |
| Gate Status After Decision | `completed` |
| Conditions (if any) | `—` |
| Decision Date | `2026-03-24` |
| Decision Reference | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/snotes/snotes_P-PH000-ST002-AC004-SES004.md` |

- Update the prose below the GDR table to reflect the `APPROVE` state (remove the RECYCLE-specific blocking language).
- Update the "Same-Gate Re-Entry Basis" subsection: This can be retained as a historical record of what constituted the re-entry package, but the heading should be amended to indicate it is now a resolved historical record (e.g., "Same-Gate Re-Entry Basis (Resolved — Gate Approved)").

**Section VIII (Changelog):**
- Add a v1.2.0 entry recording the client APPROVE decision and housekeeping resolutions.

### SPEC-003 — Update Activity Plan with Gate Closure and Recycle Re-entry Block

| Field | Detail |
|:--|:--|
| Requirement Source | `guideline_workspace_proposal.md` §VII.D step 6; `guideline_workspace_plan.md` §VI.K; Independent assessment FINDING-4 |
| Output | Updated `plan_P-PH000-ST002-AC004.md` with `GATE-001` marked `completed` and a formal Recycle Re-entry Block |
| Acceptance Criteria | (1) `GATE-001` task register row status updated to `completed` with action text recording the approval. (2) A formal Recycle Re-entry Block with six required fields is present in the GATE-001 detailed section. (3) Version bumped and changelog updated. |
| Status | `open` |

#### Implementation Detail

**Frontmatter changes:**
- `version`: `'1.2.0'` → `'1.3.0'`

**Section II (Task Register):**
- `GATE-001` row: Update `Status` from `in_progress` to `completed`. Update `Action` text to record the approval decision with date and SES004 reference.
- `TK004` row: Remains `planned` (commissioning is for next session, not this one).

**GATE-001 Detailed Section (after the Entry Criteria / Exit Criteria):**
- Add a `#### Recycle Re-entry Block (Historical Record)` subsection containing the six required fields per `guideline_workspace_plan.md` §VI.K:

| Field | Value |
|:--|:--|
| Gate Status | `completed` (was `in_progress` during recycle; now closed after approval) |
| Recycle Trigger | Original package was not decision-complete: cadence, ownership/evidence expectations, and reminder/helper-tooling boundaries were implicit despite being required by the AC004 plan contract. |
| Remediation Tasks | `TK003.1` — Correct recycled GATE-001 package with decision-complete operating-model amendments and refreshed external review. |
| Re-entry Criteria | Amended operating-model analysis, amended implementation task specification, refreshed independent external review, and SES003 recycle session notes must all be published. |
| Reassessment Rule | Same gate ID (`P-PH000-ST002-AC004-GATE-001`) reused; no derived gate created. Client re-dispositions the same GDR. |
| Downstream Block | `TK004` and all downstream tasks remained blocked until the GDR recorded an approving decision. Block lifted on 2026-03-24 after `APPROVE`. |

**Section V (Changelog):**
- Add a v1.3.0 entry recording the GATE-001 closure and Recycle Re-entry Block addition.

### SPEC-004 — Amend Implementation Task Specification with Drift Verification Criteria

| Field | Detail |
|:--|:--|
| Requirement Source | Independent assessment FINDING-5; v2.0.0 external review GAP-002 |
| Output | Updated `implementation_P-PH000-ST002-AC004_first-operationalization-task-specification.md` with a lightweight verification check in SPEC-001 |
| Acceptance Criteria | (1) SPEC-001 acceptance criteria include an explicit verification step for ledger-narrative non-drift. (2) Version bumped and changelog updated. |
| Status | `open` |

#### Implementation Detail

**Frontmatter changes:**
- `version`: `'1.1.0'` → `'1.2.0'`

**Section III, SPEC-001:**
- Amend the `Acceptance Criteria` cell to add: "After reconciliation, the executor must confirm that the narrative is fully derived from the reconciled ledger with no independent assertions or stale references that diverge from ledger truth."
- Optionally add a lightweight step to the Implementation Detail block: "After updating the ledger and re-deriving the narrative, perform a section-by-section comparison to confirm the narrative contains no independent status claims, stale activity references, or date/state values that diverge from the reconciled ledger."

**Section VI (Changelog):**
- Add a v1.2.0 entry recording the drift-verification amendment per GATE-001 approval.

### SPEC-005 — Align Stream Plan to Approved Gate State

| Field | Detail |
|:--|:--|
| Requirement Source | `guideline_workspace_proposal.md` §VII.D step 6; `guideline_workspace_plan.md` §III.C |
| Output | Updated `plan_P-PH000-ST002.md` reflecting GATE-001 approved posture |
| Acceptance Criteria | (1) Executive Summary and AC004 section reflect approved gate state and TK004 readiness. (2) Version bumped and changelog updated. |
| Status | `open` |

#### Implementation Detail

**Frontmatter changes:**
- `version`: `'1.7.0'` → `'1.8.0'`

**Section I (Executive Summary):**
- Update the "Current closure state" sentence. Replace the recycle/re-presentation language with: AC004 `GATE-001` has been approved on 2026-03-24; the operating model and first-slice execution contract are now approved for the bounded V1 rollout across `P`, `T102`, and `T104`. TK004 (first operationalization slice) is ready for developer commissioning.

**Section III, AC004 subsection:**
- Update `Planning Posture` to reflect the approved gate state and TK004 readiness for commissioning.

**Section IV (Changelog):**
- Add a v1.8.0 entry.

### SPEC-006 — Align Phase Plan to Approved Gate State

| Field | Detail |
|:--|:--|
| Requirement Source | `guideline_workspace_plan.md` §III.B (phase plan as snapshot) |
| Output | Updated `plan_P-PH000.md` reflecting GATE-001 approved snapshot |
| Acceptance Criteria | (1) Activity Snapshot Index row for AC004 reflects approved gate posture. (2) Stream Register row for ST002 reflects approved posture. (3) As-Of date updated. (4) Version bumped and changelog updated. |
| Status | `open` |

#### Implementation Detail

**Frontmatter changes:**
- `version`: `'0.4.7'` → `'0.4.8'`

**Section III (Stream Register):**
- ST002 row: Update the `Status` description from recycle/correction language to approved gate posture. Keep `in_progress` as the stream status (AC004 is still executing; only GATE-001 is closed).

**Activity Snapshot Index:**
- Update `Activity Snapshot As-Of` date to `2026-03-24`.
- AC004 row: Keep `in_progress` but update the owner/status description if the snapshot shows the recycle posture.

**Section VI (Changelog):**
- Add a v0.4.8 entry.

### SPEC-007 — Align Roadmap to Approved Gate State

| Field | Detail |
|:--|:--|
| Requirement Source | Roadmap thin-spine rule; `guideline_workspace_roadmap.md` |
| Output | Updated `roadmap_P-PROGRAM_phase0.md` with advanced milestone |
| Acceptance Criteria | (1) Compact Delivery Snapshot "Next Milestone" for Program Status System advances from re-presentation to TK004 commissioning. (2) Version bumped and changelog updated. |
| Status | `open` |

#### Implementation Detail

**Frontmatter changes:**
- `version`: `'0.2.3'` → `'0.2.4'`

**Section III (Current Delivery Snapshot):**
- Program Status System row:
  - `Current State`: Update to reflect GATE-001 approved, operating model and first-slice execution contract accepted.
  - `Next Milestone`: Change from "Re-present AC004 GATE-001..." to "Commission and execute TK004 (first operationalization slice) under the approved AC004 operating model".

**Section VI (Changelog):**
- Add a v0.2.4 entry.

### SPEC-008 — Author SES004 Session Notes and Register

| Field | Detail |
|:--|:--|
| Requirement Source | `guideline_workspace_notes.md` §5.1 (JIT registration); `guideline_workspace_proposal.md` §VII.D step 4 (decision reference) |
| Output | (1) New `snotes_P-PH000-ST002-AC004-SES004.md`. (2) Updated `notes_P-PH000-ST002.md` with SES004 row. |
| Acceptance Criteria | (1) SES004 captures the APPROVE decision, all five finding resolutions, and TK004 commissioning readiness. (2) SES004 is registered JIT in the ST002 Activity Notes Register. (3) The SES004 path matches the Decision Reference in the GDR (SPEC-002). |
| Status | `open` |

#### Implementation Detail

**SES004 file** at `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/snotes/snotes_P-PH000-ST002-AC004-SES004.md`:

- Frontmatter: Follow existing SES003 pattern with `session: 'SES004'`, `session_id: 'P-PH000-ST002-AC004-SES004'`.
- Title: `ACTIVITY SESSION NOTES: P (PROGRAM) — PH000 / ST002 / AC004 / SES004 (GATE-001 Approval & Closure)`
- Agenda: (1) Record the formal GATE-001 APPROVE decision. (2) Resolve the five independent-assessment findings. (3) Align all summary surfaces to the approved posture. (4) Confirm TK004 readiness for next-session commissioning.
- Discussion Points (DP Table): Record the approval decision rationale and the five finding resolutions.
- Decisions Captured (DEC Table):
  - DEC001: Record `GATE-001` as `APPROVE` — straight approval with no conditions.
  - DEC002: Promote v2.0.0 external review to canonical path (FINDING-1 resolution).
  - DEC003: Include formal Recycle Re-entry Block as retrospective historical record (FINDING-4 resolution).
- Actions (ACT Table): Record the eight SPEC items and their completion status.
- Session Handoff Pack: TK004 is unblocked; next session should commission TK004 developer execution using `implementation_P-PH000-ST002-AC004_first-operationalization-task-specification.md`.

**Notes register update** at `prompt/artifacts/tasks/P/workspace/PH000/ST002/notes_P-PH000-ST002.md`:

- Add a row to Section III (Activity Notes Register):
  - `| AC004 | P-PH000-ST002-AC004-SES004 | GATE-001 Approval & Closure | prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/snotes/snotes_P-PH000-ST002-AC004-SES004.md |`
- Bump version to `1.9.0` and add a changelog entry.

## IV. IMPLEMENTATION SEQUENCE

Execution order with dependency annotations:

| Order | SPEC | Target File(s) | Dependency |
|:--|:--|:--|:--|
| 1 | SPEC-001 | External review (`analysis/`) | None — can start immediately |
| 2 | SPEC-008 (notes only) | `snotes_P-PH000-ST002-AC004-SES004.md` | None — SES004 path is deterministic; author the file so the GDR can reference it |
| 3 | SPEC-002 | Proposal (`proposal/`) | Needs SES004 path from SPEC-008 |
| 4 | SPEC-004 | Implementation task spec (`implementation/`) | Independent of SPEC-002 but logically parallel |
| 5 | SPEC-003 | Activity plan | After SPEC-002 (GDR is the authoritative gate decision) |
| 6 | SPEC-005 | Stream plan | After SPEC-003 (activity plan is SSOT for activity truth) |
| 7 | SPEC-006 | Phase plan | After SPEC-005 (phase plan snapshots stream plan) |
| 8 | SPEC-007 | Roadmap | After SPEC-005 (roadmap is summary-only) |
| 9 | SPEC-008 (register) | Notes register | After all other SPECs are complete (register captures final state) |

**Parallelization notes:**
- SPEC-001, SPEC-004, and SPEC-008 (notes file) are independent and can be executed in parallel.
- SPEC-002 depends on SPEC-008 (SES004 path) but the path is deterministic, so they can be executed in parallel if the executor uses the known path.
- SPEC-005, SPEC-006, and SPEC-007 are sequential in authority order but the changes are independent in content, so they can be executed in parallel by an experienced executor who understands the thin-spine/snapshot distinction.

## V. REFERENCES

| Document | Path |
|:--|:--|
| Governing Plan | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/plan_P-PH000-ST002-AC004.md` |
| Gate-Disposition Proposal | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/proposal/proposal_P-PH000-ST002-AC004-GATE-001_operating-model-disposition.md` |
| External Review (canonical) | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/analysis/analysis_P-PH000-ST002-AC004_gate-001-external-review.md` |
| External Review (v2.0.0 source) | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/analysis/analysis_P-PH000-ST002-AC004_gate-001-external-review_new.md` |
| Operating-Model Analysis | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/analysis/analysis_P-PH000-ST002-AC004_operating-model-and-reconciliation-policy.md` |
| First Operationalization Task Spec | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/implementation/implementation_P-PH000-ST002-AC004_first-operationalization-task-specification.md` |
| SES003 Recycle Notes | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/snotes/snotes_P-PH000-ST002-AC004-SES003.md` |
| Stream Plan | `prompt/artifacts/tasks/P/workspace/PH000/ST002/plan_P-PH000-ST002.md` |
| Phase Plan | `prompt/artifacts/tasks/P/workspace/PH000/plan_P-PH000.md` |
| Roadmap | `prompt/artifacts/tasks/P/ssot/roadmap_P-PROGRAM_phase0.md` |
| Notes Register | `prompt/artifacts/tasks/P/workspace/PH000/ST002/notes_P-PH000-ST002.md` |
| Proposal Guideline | `prompt/templates/consultant/workspace/guideline_workspace_proposal.md` |
| Plan Guideline | `prompt/templates/consultant/workspace/guideline_workspace_plan.md` |
| Notes Guideline | `prompt/templates/consultant/workspace/guideline_workspace_notes.md` |

## VI. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-03-24 | Initial | Authored the AC004 GATE-001 closure orchestration task specification. Eight SPEC items covering external review promotion, proposal GDR approval recording, activity plan gate closure with Recycle Re-entry Block, implementation task spec drift-verification amendment, three summary-surface alignments, and session notes with register update. |
