---
artifact_type: 'IMPLEMENTATION'
implementation_type: 'task_specification'
initiative_id: 'T103'
initiative_code: 'ADRSS'
phase: '0'
stream_id: 'T103-PH000-ST000'
activity_id: 'T103-PH000-ST000-AC000.1'
gate_id: 'T103-PH000-ST000-AC000.1-GATE-002'
version: '1.0.0'
date: '2026-03-24'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.1/plan_T103-PH000-ST000-AC000.1.md'
execution_audience: 'developer_subagent_then_consultant_review'
purpose: 'Task specification for refreshing the AC000.1 Gate-002 package, recording Gate-002 approval, closing AC000.1, and registering AC000.2 as the successor planning lane.'
---

# IMPLEMENTATION (Task Specification): AC000.1 Gate-002 Closeout and AC000.2 Registration

## I. PURPOSE & AUTHORITY

- **Purpose**: Define the exact documentation and governance changes required to (1) normalize the AC000.1 Gate-002 package, (2) record the Gate-002 client approval, (3) close AC000.1 with SES003, and (4) register AC000.2 as the successor planning sub-activity under AC000.
- **Authority chain**: Current AC000.1 Gate-002 package -> external review and consultant QA identify closeout and successor-planning needs -> this artifact specifies the bounded implementation set -> developer sub-agent executes the document package -> consultant reviews, recycles if needed, and accepts the final state.
- **Audience**: GPT-5.4 Mini `worker` sub-agent for the initial implementation slice; LLM_Consultant for final review, recycle control, and acceptance.
- This artifact does **not** host a GDR. Gate decisions remain exclusively in proposal artifacts.
- This lane is **documentation/governance only**. Claude Code runtime files are out of scope.

**Locked decisions driving this specification**:
- `T103-PH000-ST000-AC000.1-GATE-002` will be recorded as `APPROVE` on `2026-03-24`.
- `AC000.1` will close in this lane.
- `AC000.2` will be created now as a **planning-only** successor sub-activity.
- `AC000.2` execution details for manual matrices, reliability matrices, canary flows, and supervised monitoring are intentionally deferred to later consultation once the AC000.2 planning package exists.

## II. TASK SCOPE

- **Execution slice**:
  1. Refresh the current AC000.1 Gate-002 package before client decision recording.
  2. Record Gate-002 `APPROVE` and close AC000.1.
  3. Register AC000.2 as the successor planning lane.
- **Out of scope**:
  - `.agents/skills/claude-code/**`
  - validator or pytest changes
  - execution of AC000.2 manual/runtime test scenarios
  - reopening `T103-PH000-ST000-AC000-GATE-003`

**Target files (exhaustive write set)**:

| # | File | Change Class |
|:--|:--|:--|
| F1 | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.1/implementation/implementation_T103-PH000-ST000-AC000.1_gate-002-closeout-and-ac000.2-registration.md` | This specification; consultant-authored baseline |
| F2 | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.1/analysis/analysis_T103-PH000-ST000-AC000.1_gate-002-external-review.md` | Wording correction only |
| F3 | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.1/proposal/proposal_T103-PH000-ST000-AC000.1_gate-002_runtime-monitoring-and-testing-remediation-acceptance.md` | Gate package refresh + GDR recording |
| F4 | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.1/plan_T103-PH000-ST000-AC000.1.md` | Gate-002 closeout + AC000.2 handoff note |
| F5 | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.1/snotes/snotes_T103-PH000-ST000-AC000.1-SES003.md` | New AC000.1 closeout session notes |
| F6 | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.2/plan_T103-PH000-ST000-AC000.2.md` | New successor sub-activity plan |
| F7 | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.2/snotes/snotes_T103-PH000-ST000-AC000.2-SES001.md` | New AC000.2 opening session notes |
| F8 | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.2/analysis/analysis_T103-PH000-ST000-AC000.2_release-readiness-and-supervised-monitoring-assessment.md` | New AC000.2 assessment |
| F9 | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.2/implementation/implementation_T103-PH000-ST000-AC000.2_release-readiness-and-supervised-monitoring-commissioning.md` | New AC000.2 commissioning implementation artifact |
| F10 | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.2/proposal/proposal_T103-PH000-ST000-AC000.2_gate-001_release-readiness-and-supervised-monitoring-commissioning.md` | New AC000.2 Gate-001 proposal |
| F11 | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000/plan_T103-PH000-ST000-AC000.md` | Parent activity continuity update |
| F12 | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/plan_T103-PH000-ST000.md` | Stream-level handoff and register update |
| F13 | `prompt/artifacts/tasks/T103/workspace/plan/plan_T103-PH000.md` | Phase snapshot refresh |
| F14 | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/notes_T103-PH000-ST000.md` | JIT session registration for SES003 and AC000.2 SES001 |

## III. SPECIFICATION ITEMS

### SPEC-001 — Normalize the AC000.1 Gate-002 External Review Wording

| Field | Detail |
|:--|:--|
| Output | Updated `F2` |
| Acceptance Criteria | The analysis no longer claims fresh independent reruns by the external reviewer while preserving the same substantive recommendation |
| Status | `open` |

#### Implementation Detail

Update the wording in `F2` so the external review accurately states that it corroborated the existing reviewer reruns and evidence chain rather than performing fresh independent reruns itself.

Rules:
1. Keep the overall recommendation unchanged: `APPROVE` / no scope expansion.
2. Do not widen the analysis into new findings.
3. Preserve the identified non-blocking closeout carry-forward.

### SPEC-002 — Refresh the AC000.1 Gate-002 Proposal Package

| Field | Detail |
|:--|:--|
| Output | Updated `F3` |
| Acceptance Criteria | The proposal formally includes the Gate-002 external review, states AC000.1's bounded scope clearly, and remains aligned to reviewer verdict `PASS` |
| Status | `open` |

#### Implementation Detail

Update `F3` as follows:

1. Add `external_review_reference` frontmatter pointing to `F2`.
2. Add the Gate-002 external review to the Evidence Index and References.
3. Expand the Executive Summary and GIR-001 rationale so the client can understand:
   - what AC000.1 did cover;
   - what AC000.1 did not cover;
   - why Gate-002 approval is still justified.
4. Explicitly state that AC000.1 is a bounded runtime-remediation and evidence-packaging slice, not full platform-wide production certification.
5. Preserve the statement that `T103-PH000-ST000-AC000-GATE-003` remains closed.

### SPEC-003 — Record Gate-002 Approval in the GDR

| Field | Detail |
|:--|:--|
| Output | Updated `F3` |
| Acceptance Criteria | The Gate Decision Record is fully populated for `APPROVE` on `2026-03-24` and the rest of the proposal is consistent with that state |
| Status | `open` |

#### Implementation Detail

Populate the Gate-002 GDR in `F3` with:

- `Consultant Recommendation`: `APPROVE`
- `Client Decision`: `APPROVE`
- `Gate Status After Decision`: `completed`
- `Conditions (if any)`: `—`
- `Decided By`: `Client`
- `Decision Date`: `2026-03-24`
- `Decision Reference`: `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.1/snotes/snotes_T103-PH000-ST000-AC000.1-SES003.md`

Also update any pending client-decision surfaces inside the proposal so they are internally consistent with an approved and closed gate.

### SPEC-004 — Close AC000.1 in Its Activity Plan

| Field | Detail |
|:--|:--|
| Output | Updated `F4` |
| Acceptance Criteria | `GATE-002` is `completed`, Action is non-empty, and the plan clearly indicates AC000.1 is terminal and hands off future planning to AC000.2 |
| Status | `open` |

#### Implementation Detail

Update `F4` as follows:

1. Change `GATE-002` from `in_progress` to `completed`.
2. Replace the `Action` text so it records the Gate-002 approval on `2026-03-24` and states that AC000.1 is closed.
3. Update any detailed gate text and/or success criteria so the plan no longer implies additional AC000.1 execution remains.
4. Add links to:
   - `F2` Gate-002 external review
   - `F5` AC000.1 SES003
   - `F6` AC000.2 plan
5. Bump version/date/changelog coherently.

### SPEC-005 — Create AC000.1 SES003 Closeout Notes

| Field | Detail |
|:--|:--|
| Output | New `F5` |
| Acceptance Criteria | SES003 exists at the canonical activity-session path and records the external review incorporation, Gate-002 approval, AC000.1 closeout, and AC000.2 registration decision trail |
| Status | `open` |

#### Implementation Detail

Author `F5` per `guideline_workspace_notes.md` and the activity session template.

Minimum contents:
1. Agenda covering Gate-002 package normalization, approval recording, AC000.1 closure, and AC000.2 registration.
2. Discussion points capturing the client explanation of AC000.1 scope and the need for AC000.2.
3. Decisions confirming:
   - Gate-002 approved;
   - AC000.1 closed;
   - AC000.2 created as the successor planning lane.
4. Actions that close AC000.1 and hand off planning authority to AC000.2.
5. Handoff pack linking `F3`, `F4`, `F6`, `F8`, and `F10`.

### SPEC-006 — Create AC000.2 as a Planning-Only Successor Sub-Activity

| Field | Detail |
|:--|:--|
| Output | New `F6`, `F7`, `F8`, `F9`, `F10` |
| Acceptance Criteria | AC000.2 has a complete planning/governance package through Gate-001 pending client commissioning, and it does not prematurely claim execution of release-readiness work |
| Status | `open` |

#### Implementation Detail

Create the AC000.2 package with the following contract:

**AC000.2 purpose**
- Successor sub-activity focused on release-readiness and supervised monitoring planning for the Claude Code skill under Codex CLI.

**AC000.2 non-goal**
- This lane does not execute the manual Codex matrix, reliability incident matrix, or canary runtime program yet.

**AC000.2 task sequence**
- `TK001` — publish successor assessment
- `TK002` — publish commissioning implementation spec
- `TK003` — produce Gate-001 proposal
- `GATE-001` — client commissioning decision for the future AC000.2 execution lane

**Artifact contract**
- `F8` assessment must explain why AC000.1 was bounded and why AC000.2 is required.
- `F9` implementation artifact must define the future execution theme at a high level only and say detailed execution planning will follow after AC000.2 Gate-001.
- `F10` proposal must present AC000.2 as planning/commissioning only with a pending GDR.
- `F7` SES001 must record the opening planning decision trail for AC000.2.

### SPEC-007 — Update Parent AC000, Stream ST000, and Phase PH000 Surfaces

| Field | Detail |
|:--|:--|
| Output | Updated `F11`, `F12`, `F13` |
| Acceptance Criteria | All higher-level governance surfaces show AC000.1 completed, AC000.2 registered, AC000 still in progress, ST000 still in progress, and the phase snapshot refreshed |
| Status | `open` |

#### Implementation Detail

Update the parent surfaces as follows:

1. `F11` parent AC000 plan:
   - state that AC000.1 is completed;
   - keep AC000 `in_progress` because AC000.2 is now the successor sub-activity;
   - add links to the AC000.2 package.
2. `F12` stream plan:
   - update the AC000/AC000.1 narrative to reflect AC000.1 closeout;
   - add AC000.2 as the active successor sub-activity under AC000;
   - keep stream status coherent.
3. `F13` phase plan:
   - refresh the Activity Snapshot As-Of date;
   - ensure the snapshot and stream detail reflect the new state cleanly without duplicating detailed task authority.

### SPEC-008 — Update the ST000 Notes Register

| Field | Detail |
|:--|:--|
| Output | Updated `F14` |
| Acceptance Criteria | The notes register includes AC000.1 SES003 and AC000.2 SES001 only after those files exist, with version/date/changelog updated coherently |
| Status | `open` |

#### Implementation Detail

Update `F14` after `F5` and `F7` exist.

Rules:
1. Follow JIT registration only.
2. Keep existing unrelated register rows intact.
3. Update the AC000/AC000.1 entry and add an AC000.2 entry if needed for correct discoverability.
4. Record the changelog entry for this session’s notes registration work.

## IV. DEVELOPER SUB-AGENT OUTPUT CONTRACT

The developer sub-agent must return:

1. Exact files created and exact files modified.
2. A grouped summary for:
   - Step 1: Gate-002 package refresh
   - Step 2: Gate-002 approval + AC000.1 closeout
   - Step 3: AC000.2 registration
3. Any uncertainties or assumptions made while editing.
4. Explicit confirmation that `.agents/skills/claude-code/**` was untouched.

## V. CONSULTANT REVIEW AND RECYCLE RULE

The consultant must directly review every changed artifact for:

1. Internal consistency across `F2` through `F14`.
2. Compliance with:
   - `guideline_workspace_plan.md`
   - `guideline_workspace_proposal.md`
   - `guideline_workspace_notes.md`
3. Correct gate semantics:
   - AC000.1 Gate-002 closed
   - AC000.1 terminal
   - AC000.2 Gate-001 pending
4. Correct hierarchy semantics:
   - AC000 remains active because AC000.2 exists
   - AC000.2 is planning-only, not execution-complete

If any artifact is incorrect, incomplete, contradictory, or over-scoped:
- return the same bounded correction set to the same developer sub-agent;
- do not accept partial closeout;
- repeat until the package is fully coherent.

## VI. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-03-24 | Initial | Created the consultant-owned execution authority for AC000.1 Gate-002 closeout, AC000.1 SES003 recording, and AC000.2 successor planning registration. |
