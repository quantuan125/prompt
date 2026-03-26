---
artifact_type: 'IMPLEMENTATION'
implementation_type: 'task_specification'
initiative_id: 'P'
initiative_code: 'PROGRAM'
phase: '0'
stream_id: 'P-PH000-ST002'
activity_id: 'P-PH000-ST002-AC004'
task_id: 'P-PH000-ST002-AC004-TK003.2'
version: '1.0.0'
date: '2026-03-25'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/plan_P-PH000-ST002-AC004.md'
execution_audience: 'consultant'
purpose: 'Consultant-execution specification for restructuring AC004 from approved GATE-001 package to superseded GATE-001 plus successor GATE-002 package, authoring all successor consultation artifacts, and registering the AC001.10 governance-hardening follow-on activity.'
---

# IMPLEMENTATION (Task Specification): AC004 Gate Supersession and Successor Package

## I. PURPOSE & AUTHORITY

- Purpose: Specify the exact consultant-owned execution required to convert AC004 from the currently approved-but-now-invalid GATE-001 baseline into a superseded GATE-001 historical record plus a new successor consultation gate package under GATE-002, while also creating the follow-on governance activity AC001.10.
- Authority chain: The approved consultation plan for AC004 defines the restructure intent -> this artifact specifies HOW the consultant executes the restructure and successor-package authoring -> the resulting proposal GDRs hold the authoritative gate decisions.
- Audience: `LLM_Consultant` (primary executor). Secondary consumers: `LLM_Reviewer` and `Client` as package readers.
- This artifact does NOT hold a GDR. Gate decisions remain exclusively in gate-disposition proposals.
- This artifact governs one logical consultant-execution phase spanning AC004 `TK003.2` through `TK003.7` and the linked ST008 registration slice. That multi-task scope is allowed because all work shares the same decision-boundary change and successor-package objective.
- Execution under this artifact MUST NOT begin any developer-owned work (`TK004` onward) and MUST NOT mutate the status ledger or status narrative.

## II. TASK SCOPE

- Governing plan task: `P-PH000-ST002-AC004-TK003.2` as the umbrella registration point for the successor-package slice.
- Trigger: After straight approval of AC004 `GATE-001`, the client rejected the previously accepted `GIR-003` architectural direction, required a formal comparative analysis, and required a new developer-commissionable implementation specification. That changed the decision boundary after approval.
- Deliverable contract:
  - AC004 plan and summary-surface restructure from approved GATE-001 to superseded GATE-001 plus successor GATE-002
  - Formal supersession of the old GATE-001 proposal and analysis artifacts
  - New AC004 comparative analysis, session notes, successor operating-model analysis, successor developer-facing task specification, successor external review, and successor gate-disposition proposal
  - Registration of `T104-PH001-ST008-AC001.10` in the ST008 stream plan and creation of the full AC001.10 activity plan
- Explicit non-target surfaces:
  - Do NOT edit `prompt/artifacts/tasks/P/status/status_program.yaml`
  - Do NOT edit `prompt/artifacts/tasks/P/status/status_program.md`
  - Do NOT edit root `AGENTS.md`
  - Do NOT edit `prompt/AGENTS.md`
  - Do NOT amend `prompt/artifacts/tasks/P/standard/standard_P-STD-002_program-status-standard.md`
  - Do NOT create the future developer-owned AC004 DEV-REPORT, VERIFICATION, or GATE-003 proposal in this execution slice

## II.A CURRENT-STATE PREFLIGHT AND MERGE RULES

- Before applying any SPEC item, read the current contents of every target file named in that SPEC and compare repo reality against these instructions.
- This artifact is authoritative for the required end state, not for replaying stale intermediate version bumps or already-landed edits.
- If a target file already satisfies the required end state, record it as verified and leave it unchanged.
- If a target file partially satisfies the required end state, merge only the missing required deltas. Do NOT overwrite compliant content.
- If a target file contains unrelated user or prior-session changes outside this execution slice, preserve them unless they directly conflict with the required end state.
- For files that already advanced beyond the baseline assumed when this specification was first drafted, update only the missing successor-package content and any stale statements that contradict the approved AC004 supersession posture.
- Treat `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/snotes/snotes_P-PH000-ST002-AC004-SES005.md`, `prompt/artifacts/tasks/P/workspace/PH000/ST002/notes_P-PH000-ST002.md`, and `prompt/artifacts/tasks/T104/workspace/PH001/ST008/plan_T104-PH001-ST008.md` as likely pre-existing or partially updated surfaces. Verify first; do not recreate or replay obsolete version-history assumptions.
- If a current target surface conflicts with this specification in a way that changes the approved decision boundary rather than just the drafting baseline, stop and escalate instead of guessing.

## III. SPECIFICATION ITEMS

### SPEC-001 - Amend the AC004 activity plan to encode gate supersession and successor-gate sequencing

| Field | Detail |
|:--|:--|
| Requirement Source | Approved AC004 successor-package plan; `guideline_workspace_plan.md` §VI.M |
| Output | Updated AC004 activity plan with superseded GATE-001, new GATE-002, and renumbered GATE-003 |
| Acceptance Criteria | Plan frontmatter, executive summary, task register, detailed gate sections, links register, and changelog all reflect the successor-gate model with no stale straight-approval posture left in the live contract surface |
| Status | `open` |

#### Implementation Detail

Target file:
- `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/plan_P-PH000-ST002-AC004.md`

Apply all of the following exact changes:

1. Frontmatter:
- Update `version` from `1.3.0` to `1.4.0`
- Update `date` to `2026-03-25`
- Change `status` from `completed` to `in_progress`

2. Executive Summary:
- Replace the current straight-approval posture with this meaning:
  - `GATE-001` remains historically valid for the old baseline but is no longer the active approval basis.
  - The client later rejected the previously accepted wrap-up-based reminder/tooling direction.
  - AC004 is therefore in a post-approval decision-boundary change state and is being restructured into a superseded GATE-001 plus successor GATE-002 package.
  - Developer-owned execution is blocked pending the successor consultation gate.

3. Task Register changes:
- Keep `TK001`, `TK002`, `TK003`, and `TK003.1` as `completed` historical tasks.
- Change the `GATE-001` row to:
  - `Status`: `superseded`
  - `Action`: "Record `SUPERSEDE` decision on 2026-03-25 after post-approval decision-boundary change: client rejected the previously accepted wrap-up-based reminder/tooling direction, required comparative analysis, and required a new execution contract. Succeeded by `P-PH000-ST002-AC004-GATE-002`."
- Add these new rows immediately after `TK003.1` and before `TK004`:
  - `TK003.2` - `P-PH000-ST002-AC004-TK003.2` - "Produce comparative analysis for successor reminder/session-close architecture" - `completed` - `LLM_Consultant` - `GATE-001` - `analysis/` - `guideline_workspace_analysis.md` - action text stating the comparative analysis was authored and recommends the dedicated session-close skill path.
  - `TK003.3` - `P-PH000-ST002-AC004-TK003.3` - "Record supersession session notes and register updates" - `completed` - `LLM_Consultant` - `TK003.2` - `snotes/` - `guideline_workspace_notes.md` - action text stating SES005 was authored and ST002 notes register updated.
  - `TK003.4` - `P-PH000-ST002-AC004-TK003.4` - "Author successor operating-model analysis" - `completed` - `LLM_Consultant` - `TK003.2` - `analysis/` - `guideline_workspace_analysis.md` - action text stating the successor operating-model analysis was authored against the new baseline.
  - `TK003.5` - `P-PH000-ST002-AC004-TK003.5` - "Author successor first-operationalization task specification" - `completed` - `LLM_Consultant` - `TK003.4` - `implementation/` - `guideline_workspace_implementation.md` - action text stating the new developer-facing spec replaces the historical wrap-up-based spec as the active commissioning surface.
  - `TK003.6` - `P-PH000-ST002-AC004-TK003.6` - "Produce successor GATE-002 external review" - `completed` - `LLM_Consultant` - `TK003.5` - `analysis/` - `guideline_workspace_analysis.md` - action text stating the external review confirms per-SPEC commissionability and package sufficiency.
  - `TK003.7` - `P-PH000-ST002-AC004-TK003.7` - "Produce successor GATE-002 gate-disposition proposal" - `completed` - `LLM_Consultant` - `TK003.6` - `proposal/` - `guideline_workspace_proposal.md` - action text stating the successor package and pending GDR were authored.
  - `GATE-002` - `P-PH000-ST002-AC004-GATE-002` - "Gate: Client approval of successor AC004 operating model and first-slice execution package" - `planned` - `Client` - `TK003.7` - `GDR` - `guideline_workspace_proposal.md` - action `—`
- Rename the current implementation-backed `GATE-002` row to `GATE-003` and update:
  - `Task ID` -> `P-PH000-ST002-AC004-GATE-003`
  - `Name` -> "Gate: Client acceptance of the first operationalization slice"
  - `Depends On` remains `TK007`
  - `Reference` remains `guideline_workspace_proposal.md`
  - `Action` stays `Implementation acceptance is required before AC004 closes.`
- Change `TK004` to depend on `GATE-002`, not `GATE-001`
- Leave `TK005` through `TK007` dependency chain unchanged relative to `TK004`

4. Detailed section updates:
- Replace the current GATE-001 "Recycle Re-entry Block (Historical Record)" with a **Supersession Block** containing exactly these fields:
  - **Gate Status**: `superseded`
  - **Supersession Trigger**: "Post-approval decision-boundary change: the client rejected the previously accepted wrap-up-based reminder/tooling direction, required a formal comparative analysis, and required a new developer-commissionable implementation contract."
  - **Prior Assessment**: "Historically valid for the 2026-03-24 GATE-001 baseline. Preserved for audit trail only."
  - **Successor Gate**: `P-PH000-ST002-AC004-GATE-002`
  - **GDR Reference**: `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/proposal/proposal_P-PH000-ST002-AC004-GATE-001_operating-model-disposition.md`
  - **Governance Authority**: `guideline_workspace_plan.md` §VI.M and `guideline_workspace_proposal.md` §VII.D Step 4a
- Add detailed sections for `TK003.2` through `TK003.7` matching their task names and outputs.
- Add a new detailed gate section for `GATE-002` with:
  - **Gate ID**: `P-PH000-ST002-AC004-GATE-002`
  - **Type**: "Consultation-only successor gate"
  - **Entry Criteria**: `TK003.2` through `TK003.7` complete; successor proposal exists with pending GDR; old GATE-001 proposal and analyses superseded; successor package contains comparative analysis, successor operating-model analysis, successor implementation spec, successor external review, and SES005.
  - **Reviewer**: `Client`
  - **Exit Criteria**: client records `APPROVE` or `APPROVE WITH CONDITIONS` in the GATE-002 proposal GDR; downstream execution remains blocked until that happens.
  - **Gate-Disposition Proposal**: `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/proposal/proposal_P-PH000-ST002-AC004-GATE-002_operating-model-disposition.md`
- Rename the current implementation acceptance gate section from `GATE-002` to `GATE-003` and update its proposal path to `proposal_P-PH000-ST002-AC004-GATE-003_first-operationalization-disposition.md`

5. Links Register:
- Keep the old GATE-001 proposal, old external review, old operating-model analysis, and old first-operationalization task specification in the Links Register but annotate them in the `Target` label as `SUPERSEDED` or `historical only`
- Add these new rows:
  - Comparative analysis
  - SES005 session notes
  - Successor operating-model analysis
  - Successor implementation task specification
  - Successor GATE-002 external review
  - Successor GATE-002 proposal
  - AC001.10 activity plan

6. Changelog:
- Add `v1.4.0 | 2026-03-25 | Amendment | Restructured AC004 from approved GATE-001 to post-approval gate supersession. GATE-001 closed with SUPERSEDE, successor GATE-002 created, prior implementation acceptance gate renumbered to GATE-003, TK003.2-TK003.7 inserted, and the live package reoriented to the successor baseline. Source: AC004 SES005 and client-approved successor-package consultation.`

### SPEC-002 - Align the stream, phase, roadmap, and notes-register summary surfaces to the successor-gate posture

| Field | Detail |
|:--|:--|
| Requirement Source | AC004 successor-package plan; anti-drift rules in `guideline_workspace_plan.md` |
| Output | Updated ST002 stream plan, PH000 phase plan, roadmap, and ST002 notes register |
| Acceptance Criteria | No summary surface continues to claim that `TK004` is unblocked from the old GATE-001 approval; SES005 is indexed; all summary surfaces point to GATE-002 as the next milestone |
| Status | `open` |

#### Implementation Detail

Target files:
- `prompt/artifacts/tasks/P/workspace/PH000/ST002/plan_P-PH000-ST002.md`
- `prompt/artifacts/tasks/P/workspace/PH000/plan_P-PH000.md`
- `prompt/artifacts/tasks/P/ssot/roadmap_P-PROGRAM_phase0.md`
- `prompt/artifacts/tasks/P/workspace/PH000/ST002/notes_P-PH000-ST002.md`

Apply these exact changes:

1. `plan_P-PH000-ST002.md`
- Update frontmatter `version` to `1.9.0`, `date` to `2026-03-25`
- Replace the Executive Summary sentence claiming "AC004 GATE-001 closed with straight APPROVE ... TK004 unblocked" with:
  - "AC004 entered post-approval gate supersession on 2026-03-25 after a decision-boundary change invalidated the previously approved wrap-up-based reminder/tooling direction. Historical GATE-001 is preserved as superseded. The active milestone is successor consultation `P-PH000-ST002-AC004-GATE-002`; `TK004` remains blocked pending that gate."
- In the Activity Register, keep `AC004` status `in_progress` but change its Deliverable summary to "Superseded GATE-001 historical record plus successor GATE-002 readiness package and downstream GATE-003 implementation path"
- Leave `AC005` blocked/planned
- Add a changelog row `v1.9.0 | 2026-03-25 | Amendment | Replaced the old AC004 straight-approval posture with post-approval gate supersession. ST002 now points to successor GATE-002 as the active milestone; TK004 is blocked again pending successor consultation approval.`

2. `plan_P-PH000.md`
- Update frontmatter `version` to `0.4.9`, `date` to `2026-03-25`
- In the Stream Register ST002 row, replace "AC004 GATE-001 closed ... TK004 unblocked" with "AC004 GATE-001 superseded after post-approval decision-boundary change; successor consultation GATE-002 is the active milestone; implementation remains blocked"
- Update `Activity Snapshot As-Of` to `2026-03-25`
- Keep AC004 snapshot `in_progress` but revise the name/summary posture to successor-package preparation
- Add changelog row `v0.4.9 | 2026-03-25 | Housekeeping | Refreshed the PH000 snapshot after AC004 post-approval gate supersession. ST002 now reflects successor consultation GATE-002 as the active milestone and re-blocks TK004 until successor approval.`

3. `roadmap_P-PROGRAM_phase0.md`
- Update frontmatter `version` to `0.2.5`, `date` to `2026-03-25`
- In `CURRENT DELIVERY SNAPSHOT`, replace the Program Status System row with:
  - **Current State**: "AC004 historical GATE-001 is superseded after a post-approval decision-boundary change. The active package is successor consultation GATE-002."
  - **Next Milestone**: "Approve AC004 successor GATE-002 package before re-commissioning TK004"
- Add changelog row `v0.2.5 | 2026-03-25 | Amendment | Replaced the old AC004 straight-approval milestone with post-approval gate supersession. The roadmap now points to successor GATE-002 rather than immediate TK004 commissioning.`

4. `notes_P-PH000-ST002.md`
- Verify whether frontmatter already shows `version: '1.10.0'` and `date: '2026-03-25'`; if not, update it to that state
- Ensure the Activity Notes Register contains this row:
  - `AC004 | P-PH000-ST002-AC004-SES005 | AC004 Gate Supersession, Successor GATE-002 Commissioning & AC001.10 Trigger Capture | prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/snotes/snotes_P-PH000-ST002-AC004-SES005.md`
- Ensure the changelog contains row `v1.10.0 | 2026-03-25 | Amendment | Registered AC004 activity session P-PH000-ST002-AC004-SES005 for post-approval gate supersession, successor GATE-002 commissioning, and AC001.10 governance-trigger capture.`
- If both the register row and changelog row are already present and correct, leave the file unchanged.

### SPEC-003 - Convert the old GATE-001 proposal into the governed superseded historical record

| Field | Detail |
|:--|:--|
| Requirement Source | `guideline_workspace_proposal.md` §VII.C-§VII.D |
| Output | Superseded GATE-001 proposal with updated GDR and successor linkage |
| Acceptance Criteria | Proposal frontmatter, deprecation notice, and GDR reflect `SUPERSEDE`; the body remains otherwise historical |
| Status | `open` |

#### Implementation Detail

Target file:
- `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/proposal/proposal_P-PH000-ST002-AC004-GATE-001_operating-model-disposition.md`

Apply only the following changes:

1. Frontmatter:
- `version`: `1.3.0`
- `date`: `2026-03-25`
- `status`: `superseded`
- add `superseded_by: 'prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/proposal/proposal_P-PH000-ST002-AC004-GATE-002_operating-model-disposition.md'`

2. Add this deprecation notice as the first body line:
> **SUPERSEDED**: This gate-disposition proposal was produced against the 2026-03-24 AC004 `GATE-001` baseline that still accepted the wrap-up-based reminder/tooling direction. `GATE-001` has been closed with `Client Decision: SUPERSEDE` due to a post-approval decision-boundary change requiring a comparative analysis and a new execution contract. This proposal is preserved as the historical `GATE-001` record. The successor gate package is at `proposal_P-PH000-ST002-AC004-GATE-002_operating-model-disposition.md`.

3. Update the GDR only:
- `Consultant Recommendation`: `SUPERSEDE`
- `Client Decision`: `SUPERSEDE`
- `Gate Status After Decision`: `superseded`
- `Conditions (if any)`: `Successor gate: P-PH000-ST002-AC004-GATE-002. Trigger: post-approval decision-boundary change after client rejection of the previously accepted wrap-up-based reminder/tooling direction; comparative analysis and new implementation contract required.`
- `Decision Date`: `2026-03-25`
- `Decision Reference`: `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/snotes/snotes_P-PH000-ST002-AC004-SES005.md`

4. Changelog:
- Add `v1.3.0 | 2026-03-25 | Amendment | Recorded Client Decision SUPERSEDE and Gate Status superseded after post-approval decision-boundary change. Frontmatter marked superseded with successor proposal backlink. Body preserved as historical record.`

Do not rewrite GIR reasoning, Evidence Index prose, or historical summary text beyond the required deprecation notice and GDR change.

### SPEC-004 - Convert the old GATE-001 analysis artifacts into governed superseded historical records

| Field | Detail |
|:--|:--|
| Requirement Source | `guideline_workspace_analysis.md` §IX |
| Output | Superseded old external review and old operating-model analysis |
| Acceptance Criteria | Each analysis file has `status: superseded`, `superseded_by`, required deprecation notice, minor version bump, and no substantive body rewrites |
| Status | `open` |

#### Implementation Detail

Target files:
- `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/analysis/analysis_P-PH000-ST002-AC004_gate-001-external-review.md`
- `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/analysis/analysis_P-PH000-ST002-AC004_operating-model-and-reconciliation-policy.md`

For `analysis_P-PH000-ST002-AC004_gate-001-external-review.md`:
- update `version` to `2.1.0`
- update `date` to `2026-03-25`
- change `status` to `superseded`
- add `superseded_by: 'prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/analysis/analysis_P-PH000-ST002-AC004-GATE-002_external-review.md'`
- add deprecation notice:
  > **SUPERSEDED**: This external review assessed the 2026-03-24 AC004 `GATE-001` package that still carried the wrap-up-based reminder/tooling direction. It has been superseded by `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/analysis/analysis_P-PH000-ST002-AC004-GATE-002_external-review.md`, which assesses the successor GATE-002 package after the post-approval decision-boundary change. This artifact is preserved for historical traceability only.
- add changelog row `v2.1.0 | 2026-03-25 | Amendment | Marked as superseded after AC004 post-approval gate supersession. Added successor external-review backlink and required deprecation notice; body preserved.`

For `analysis_P-PH000-ST002-AC004_operating-model-and-reconciliation-policy.md`:
- update `version` to `1.2.0`
- update `date` to `2026-03-25`
- change `status` to `superseded`
- add `superseded_by: 'prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/analysis/analysis_P-PH000-ST002-AC004_successor-operating-model-and-reconciliation-policy.md'`
- add deprecation notice:
  > **SUPERSEDED**: This operating-model analysis supported the 2026-03-24 AC004 `GATE-001` baseline that still accepted the wrap-up-based reminder/tooling direction. It has been superseded by `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/analysis/analysis_P-PH000-ST002-AC004_successor-operating-model-and-reconciliation-policy.md`, which assesses the successor GATE-002 baseline after the post-approval decision-boundary change. This artifact is preserved for historical traceability only.
- add changelog row `v1.2.0 | 2026-03-25 | Amendment | Marked as superseded after AC004 post-approval gate supersession. Added successor operating-model-analysis backlink and required deprecation notice; body preserved.`

Do not alter the analytical bodies beyond the required notice and metadata changes.

### SPEC-005 - Create the new comparative analysis that selects the successor reminder/session-close architecture

| Field | Detail |
|:--|:--|
| Requirement Source | Client QA direction; approved AC004 successor-package plan |
| Output | New comparative analysis recommending the successor architecture |
| Acceptance Criteria | Artifact uses `analysis_type: comparative_analysis`, contains explicit weighting and scoring, and concludes with a single recommended option that is then consumed downstream |
| Status | `open` |

#### Implementation Detail

Create this new file:
- `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/analysis/analysis_P-PH000-ST002-AC004_session-close-reminder-architecture-comparative-assessment.md`

Required frontmatter:
- `artifact_type: 'ANALYSIS'`
- `analysis_type: 'comparative_analysis'`
- `initiative_id: 'P'`
- `initiative_code: 'PROGRAM'`
- `phase: '0'`
- `stream_id: 'P-PH000-ST002'`
- `activity_id: 'P-PH000-ST002-AC004'`
- `task_id: 'P-PH000-ST002-AC004-TK003.2'`
- `version: '1.0.0'`
- `date: '2026-03-25'`
- `status: 'draft'`
- `author: 'LLM_Consultant'`
- `decision_owner_role: 'Client'`
- `plan_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/plan_P-PH000-ST002-AC004.md'`
- `options_compared: 'wrap-up skill vs dedicated session-close skill vs non-skill protocol/tooling surface'`
- `evaluation_criteria: 'developer commissionability, auditability, bounded rollout fit, automation extensibility, AGENTS/standards spillover risk, reviewer verifiability'`
- `recommended_option: 'new dedicated session-close skill'`

Required body structure and exact decision logic:

1. Executive Summary:
- State that the old wrap-up-based direction was later rejected by the client.
- State that this analysis exists to choose the successor reminder/session-close surface for AC004 GATE-002.
- State the recommendation up front: `new dedicated session-close skill`.

2. Options compared:
- Option A: Continue using `prompt/skills/wrap-up/SKILL.md`
- Option B: Create `prompt/skills/session-close/SKILL.md` as a dedicated session-close reminder skill
- Option C: Keep reminder logic only in `status_program.md` Section 7 and avoid any skill surface

3. Evaluation criteria and weights:
- Developer commissionability: `25`
- Auditability: `20`
- Bounded rollout fit: `15`
- Automation extensibility: `15`
- AGENTS/standards spillover risk: `10`
- Reviewer verifiability: `15`

4. Comparative matrix:
- Score each option on a 1-5 scale using this exact scoring table:
  - Wrap-up skill: `2, 2, 3, 2, 3, 2`
  - Dedicated session-close skill: `5, 4, 4, 5, 4, 5`
  - Non-skill protocol only: `3, 5, 2, 3, 5, 4`
- Compute weighted totals and show that the dedicated session-close skill is the highest-scoring option.

5. Recommendation section:
- Recommend Option B exactly: create `prompt/skills/session-close/SKILL.md`
- State why Option A is rejected: it preserves the very architectural direction that the client rejected
- State why Option C is rejected: it weakens session-close execution prompting and makes the human reminder surface less explicit

6. Downstream implications:
- The successor operating-model analysis MUST treat `prompt/skills/session-close/SKILL.md` as the chosen reminder surface
- The successor developer-facing task specification MUST target that file, not `prompt/skills/wrap-up/SKILL.md`
- The old wrap-up-based implementation spec becomes historical-only context

### SPEC-006 - Record the supersession session notes and register them in the ST002 notes register

| Field | Detail |
|:--|:--|
| Requirement Source | Notes-register JIT rule; AC004 successor-package plan |
| Output | AC004 SES005 notes and ST002 notes-register entry |
| Acceptance Criteria | SES005 captures the decision-boundary change and successor-gate basis; ST002 notes register indexes SES005 |
| Status | `open` |

#### Implementation Detail

Create or amend as needed:
- `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/snotes/snotes_P-PH000-ST002-AC004-SES005.md`

Preflight rule:
- If `SES005` already exists, treat this SPEC as a verify-and-amend task. Preserve any compliant content already present and add only the missing required elements from this SPEC.

Required session title:
- `AC004 Gate Supersession, Successor GATE-002 Commissioning & AC001.10 Trigger Capture`

Required session content:
- Agenda includes:
  - record that the previously approved GATE-001 package is being superseded rather than rejected
  - record the client rejection of the wrap-up-based direction
  - record the comparative-analysis requirement
  - record the successor gate and renumbered implementation gate
  - record the AC001.10 governance trigger
- Discussion points must include:
  - why this is a decision-boundary change rather than same-gate recycle
  - why the old approval remains historically valid
  - why a new developer-facing implementation spec is required
  - why AC001.10 is being created
- Decision table must include:
  - `DEC001`: Close `P-PH000-ST002-AC004-GATE-001` with `SUPERSEDE`
  - `DEC002`: Create successor consultation `P-PH000-ST002-AC004-GATE-002`
  - `DEC003`: Renumber implementation acceptance gate to `P-PH000-ST002-AC004-GATE-003`
  - `DEC004`: Adopt dedicated session-close skill as the recommended architecture for the successor package
  - `DEC005`: Register `T104-PH001-ST008-AC001.10` to harden IMPLEMENTATION-detail precision and external-review sufficiency rules
- Action register must point to the new files created under SPEC-005 through SPEC-011

Update the ST002 notes register exactly as defined in SPEC-002 item 4.

### SPEC-007 - Create the successor operating-model analysis for GATE-002

| Field | Detail |
|:--|:--|
| Requirement Source | AC004 successor-package plan; output of SPEC-005 |
| Output | Successor operating-model analysis against the new baseline |
| Acceptance Criteria | Analysis states the new baseline explicitly, carries forward valid prior decisions, replaces the old reminder/tooling choice, and defines the active GATE-002 decision set |
| Status | `open` |

#### Implementation Detail

Create:
- `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/analysis/analysis_P-PH000-ST002-AC004_successor-operating-model-and-reconciliation-policy.md`

Required frontmatter:
- same AC004 metadata shape as the old operating-model analysis
- `task_id: 'P-PH000-ST002-AC004-TK003.4'`
- `gate_id: 'P-PH000-ST002-AC004-GATE-002'`
- `version: '1.0.0'`
- `date: '2026-03-25'`
- `status: 'draft'`

Required body content:

1. Executive Summary:
- State that this is the successor operating-model assessment for GATE-002
- State that the only material decision-boundary change is the rejection of the old wrap-up-based reminder/tooling architecture and the requirement for a new developer-commissionable task spec
- State that source-of-truth order, reconciliation posture, V1 rollout boundary (`P`, `T102`, `T104`), and AC005 deferral all carry forward unchanged

2. Decision set:
- Decision 1: source-of-truth order remains stream plan -> phase plan snapshot -> roadmap summary -> status ledger -> derived narrative
- Decision 2: status cadence remains event-driven first with weekly stale-state floor
- Decision 3: ownership/evidence posture remains non-terminal attributed, terminal/reopen client-accountable and evidence-bearing
- Decision 4: reminder/session-close architecture changes from `wrap-up` to new dedicated `prompt/skills/session-close/SKILL.md`
- Decision 5: `status_program.md` Section 7 remains the governing operational protocol surface
- Decision 6: V1 rollout boundary remains limited to `P`, `T102`, and `T104`
- Decision 7: AC005/future initiative opening remains out of scope

3. Gap register:
- Include one resolved historical gap noting that the old package relied on a rejected wrap-up-based architecture
- Include one resolved structural gap noting that the successor package now contains a new comparative analysis and new task spec

4. Downstream actions:
- point to the new implementation task spec, new external review, new proposal, SES005, and AC001.10 follow-on

5. Conclusion:
- State that the package is decision-complete for successor consultation `GATE-002`

### SPEC-008 - Create the successor developer-facing first-operationalization task specification

| Field | Detail |
|:--|:--|
| Requirement Source | Client QA on implementation-detail insufficiency; output of SPEC-005 and SPEC-007 |
| Output | New developer-facing task specification that replaces the historical wrap-up-based spec as the active commissioning surface |
| Acceptance Criteria | Every SPEC is developer-commissionable without inference; the chosen dedicated session-close skill is built into the contract; no unresolved architecture choice remains |
| Status | `open` |

#### Implementation Detail

Create:
- `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/implementation/implementation_P-PH000-ST002-AC004_successor-first-operationalization-task-specification.md`

Required frontmatter:
- `artifact_type: 'IMPLEMENTATION'`
- `implementation_type: 'task_specification'`
- `initiative_id: 'P'`
- `initiative_code: 'PROGRAM'`
- `phase: '0'`
- `stream_id: 'P-PH000-ST002'`
- `activity_id: 'P-PH000-ST002-AC004'`
- `task_id: 'P-PH000-ST002-AC004-TK004'`
- `version: '1.0.0'`
- `date: '2026-03-25'`
- `status: 'draft'`
- `author: 'LLM_Consultant'`
- `decision_owner_role: 'Client'`
- `plan_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/plan_P-PH000-ST002-AC004.md'`
- `execution_audience: 'developer'`
- `purpose: 'Successor first-slice execution specification for AC004 TK004, replacing the historical wrap-up-based contract with the approved dedicated session-close skill model and explicit per-surface implementation detail.'`

Required body:

1. Purpose & Authority:
- state this replaces the historical wrap-up-based task spec as the active commissioning surface
- state execution is blocked until `P-PH000-ST002-AC004-GATE-002` records approval

2. Deliverable contract:
- updated `prompt/artifacts/tasks/P/status/status_program.yaml`
- updated `prompt/artifacts/tasks/P/status/status_program.md`
- updated `prompt/artifacts/tasks/P/workspace/PH000/ST002/plan_P-PH000-ST002.md`
- updated `prompt/artifacts/tasks/P/workspace/PH000/plan_P-PH000.md`
- updated `prompt/artifacts/tasks/P/ssot/roadmap_P-PROGRAM_phase0.md`
- new `prompt/skills/session-close/SKILL.md`

3. Explicit non-target surfaces:
- do not edit root `AGENTS.md`
- do not edit `prompt/AGENTS.md`
- do not edit `prompt/skills/wrap-up/SKILL.md`
- do not edit `prompt/artifacts/tasks/P/standard/standard_P-STD-002_program-status-standard.md`

4. SPEC items:

`SPEC-001 - Reconcile authoritative stream-plan truth into the status ledger`
- target: `status_program.yaml`
- implementation detail must explicitly list these authority rules:
  - AC004 successor GATE-002 becomes the active consultation milestone
  - GATE-001 is historical/superseded
  - GATE-003 is the future implementation acceptance gate
  - AC005 remains blocked
- acceptance requires ledger-first edit and narrative derivation check

`SPEC-002 - Re-derive the status narrative and Section 7 protocol from the reconciled ledger`
- target: `status_program.md`
- implementation detail must require:
  - Section 1-6 derived from ledger only
  - Section 7 operational protocol updated to reference `prompt/skills/session-close/SKILL.md`
  - explicit text that wrap-up is not the governing reminder surface for AC004 V1

`SPEC-003 - Align planning and summary surfaces to the reconciled successor posture`
- targets:
  - `plan_P-PH000-ST002.md`
  - `plan_P-PH000.md`
  - `roadmap_P-PROGRAM_phase0.md`
- implementation detail must say exactly:
  - ST002 stream plan points to active successor GATE-002 package and blocks TK004 until approval
  - phase plan snapshot reflects AC004 as in progress under successor consultation
  - roadmap next milestone is successor GATE-002 approval, not immediate execution

`SPEC-004 - Create the dedicated session-close skill`
- target: `prompt/skills/session-close/SKILL.md`
- exact required purpose:
  - remind the session executor at closeout to verify whether status surfaces were affected
  - direct them to reconcile status if lifecycle, gate, dependency, or stale-state triggers were touched
  - point to `status_program.md` Section 7 as the governing protocol
- exact non-goal:
  - do not duplicate wrap-up responsibilities
  - do not create repo-wide automation

`SPEC-005 - Preserve AC005/future-initiative boundary`
- state that no `T105` or future initiative file may be created during TK004

7. Commissionability hardening requirements:
- The successor developer-facing task specification MUST be written so a developer sub-agent can execute it without inferring missing decisions.
- For each SPEC item in the successor developer-facing task specification, include all of the following subfields explicitly:
  - `Target file(s)`
  - `Required end-state posture`
  - `Explicit non-target / do-not-change constraints`
  - `Validation check`
  - `Blocking ambiguity rule` stating that the executor must stop rather than invent behavior if the live file shape contradicts the specified end state
- The successor developer-facing task specification MUST include an explicit preflight rule that current repo state wins over stale draft assumptions, but only within the approved AC004 successor decision boundary.
- The successor developer-facing task specification MUST include an end-of-artifact commissionability checklist confirming:
  - every target file is named exactly
  - every required posture change is explicit
  - every prohibited edit surface is explicit
  - the session-close skill fully replaces the wrap-up skill for AC004 V1 reminder governance
  - no unresolved architecture choice remains
- The successor developer-facing task specification MUST NOT tell the developer to decide whether to edit `prompt/skills/wrap-up/SKILL.md`; it must state unequivocally that `wrap-up` is historical-only context and that `prompt/skills/session-close/SKILL.md` is the only approved reminder-surface target.

5. Implementation sequence:
- ledger first
- narrative second
- planning/summary surfaces third
- new session-close skill fourth
- dev-report handoff last

6. References:
- successor operating-model analysis
- comparative analysis
- successor GATE-002 external review
- successor GATE-002 proposal

### SPEC-009 - Create the successor GATE-002 external review

| Field | Detail |
|:--|:--|
| Requirement Source | Client QA regarding external-review insufficiency |
| Output | New external review that explicitly tests per-SPEC developer commissionability |
| Acceptance Criteria | Review evaluates the successor package, not the old package, and reaches a clear recommendation on whether GATE-002 is ready for client disposition |
| Status | `open` |

#### Implementation Detail

Create:
- `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/analysis/analysis_P-PH000-ST002-AC004-GATE-002_external-review.md`

Required frontmatter:
- `artifact_type: 'ANALYSIS'`
- `analysis_type: 'external_review'`
- `initiative_id: 'P'`
- `initiative_code: 'PROGRAM'`
- `phase: '0'`
- `stream_id: 'P-PH000-ST002'`
- `activity_id: 'P-PH000-ST002-AC004'`
- `gate_id: 'P-PH000-ST002-AC004-GATE-002'`
- `version: '1.0.0'`
- `date: '2026-03-25'`
- `status: 'draft'`
- `author: 'LLM_Consultant'`
- `decision_owner_role: 'Client'`
- `plan_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/plan_P-PH000-ST002-AC004.md'`
- `purpose: 'Independent external review of the successor AC004 GATE-002 package, including per-SPEC developer commissionability assessment and explicit confirmation that the implementation spec is part of the gate package.'`

Required assessment scope:
- confirm GATE-001 supersession handling is coherent
- confirm comparative analysis exists and recommendation is explicit
- confirm successor operating-model analysis consumes the chosen recommendation
- confirm successor implementation spec is part of the gate package and each SPEC is independently executable without inference
- confirm downstream tasks remain blocked until GATE-002 approval
- confirm AC001.10 registration is correctly framed as governance follow-on, not hidden implementation scope

Required findings model:
- include a gap register with one row per possible failure mode:
  - missing comparative analysis
  - unresolved architecture choice
  - implementation spec still ambiguous
  - old wrap-up assumption still active anywhere in live successor package
  - downstream tasks incorrectly unblocked

Required conclusion:
- recommend `APPROVE` only if all five checks pass
- otherwise recommend `RECYCLE`

### SPEC-010 - Create the successor GATE-002 gate-disposition proposal with clean primary evidence and segregated historical evidence

| Field | Detail |
|:--|:--|
| Requirement Source | `guideline_workspace_proposal.md` §V.B and supersession handling rules |
| Output | Successor GATE-002 proposal with pending GDR and split evidence model |
| Acceptance Criteria | Proposal presents only the successor-baseline artifacts as primary evidence, moves old package artifacts into Historical Evidence, and carries a pending GDR for client disposition |
| Status | `open` |

#### Implementation Detail

Create:
- `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/proposal/proposal_P-PH000-ST002-AC004-GATE-002_operating-model-disposition.md`

Required frontmatter:
- `artifact_type: 'PROPOSAL'`
- `initiative_id: 'P'`
- `initiative_code: 'PROGRAM'`
- `phase: '0'`
- `stream_id: 'P-PH000-ST002'`
- `activity_id: 'P-PH000-ST002-AC004'`
- `gate_id: 'P-PH000-ST002-AC004-GATE-002'`
- `version: '1.0.0'`
- `date: '2026-03-25'`
- `status: 'draft'`
- `author: 'LLM_Consultant'`
- `decision_owner_role: 'Client'`
- `plan_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/plan_P-PH000-ST002-AC004.md'`
- `analysis_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/analysis/analysis_P-PH000-ST002-AC004_successor-operating-model-and-reconciliation-policy.md'`
- `external_review_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/analysis/analysis_P-PH000-ST002-AC004-GATE-002_external-review.md'`
- `supersedes: 'prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/proposal/proposal_P-PH000-ST002-AC004-GATE-001_operating-model-disposition.md'`
- `purpose: 'Successor consultation gate disposition package for AC004 GATE-002 after post-approval supersession of GATE-001.'`

Required body:

1. Executive Summary:
- state that this is the successor gate to superseded GATE-001
- state that the successor package exists because the prior wrap-up-based direction was rejected after approval
- state that the recommendation carried forward by the package is the new dedicated session-close skill

2. Gate Package Index - Primary Evidence:
- include exactly these required rows:
  - comparative analysis
  - SES005 session notes
  - successor operating-model analysis
  - successor implementation task specification
  - successor external review
  - AC004 activity plan

3. Evidence Index - Primary Evidence:
- include the same active artifacts plus governing plan and stream summary surfaces as reference evidence

4. Evidence Index - Historical Evidence:
- include exactly these rows with `SUPERSEDED` or `historical only` notes:
  - old GATE-001 proposal
  - old GATE-001 external review
  - old operating-model analysis
  - old first-operationalization task specification

5. Disposition items:
- `GIR-001`: adopt the dedicated session-close skill architecture at `prompt/skills/session-close/SKILL.md`
- `GIR-002`: approve the successor operating-model baseline and source-of-truth order
- `GIR-003`: approve the successor developer-facing first-operationalization task specification as commissionable authority for TK004 after gate approval

6. Consultant Recommendation:
- set to `APPROVE`
- basis must cite the comparative analysis recommendation, the successor operating-model analysis, and the external review's no-blocker conclusion

7. GDR:
- `Consultant Recommendation`: `APPROVE`
- `Client Decision`: `pending`
- `Gate Status After Decision`: `pending`
- `Conditions (if any)`: `—`
- `Decision Date`: `—`
- `Decision Reference`: `pending`

### SPEC-011 - Register AC001.10 in the ST008 stream plan and create the full AC001.10 activity plan with explicit traceability to the client-approved trigger

| Field | Detail |
|:--|:--|
| Requirement Source | Client-approved governance follow-on direction; ST008 `AC001.x` sub-activity family pattern |
| Output | ST008 stream-plan registration plus full AC001.10 activity plan |
| Acceptance Criteria | AC001.10 exists as an explicit governance-hardening sub-activity whose purpose and trigger quote the client-approved three-part failure statement |
| Status | `open` |

#### Implementation Detail

Target files:
- `prompt/artifacts/tasks/T104/workspace/PH001/ST008/plan_T104-PH001-ST008.md`
- `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.10/plan_T104-PH001-ST008-AC001.10.md`

1. Amend `plan_T104-PH001-ST008.md`
- verify current frontmatter first; if the file is already at `version: '1.21.0'` and `date: '2026-03-25'`, do not replay the version bump
- add the following AC001.10 content only if it is not already present:
  - Activity Register row after `AC001.9`:
  - `AC001.10 | T104-PH001-ST008-AC001.10 | IMPLEMENTATION Spec Precision, External-Review Sufficiency & Post-Approval Gate Package Governance | planned | LLM_Consultant | T104-PH001-ST008-AC001.8 | AC001.10 activity plan, governance gap analysis, GATE-001 package, and downstream guideline/template hardening path | prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.10/plan_T104-PH001-ST008-AC001.10.md`
  - contract stub in the Activities section after `AC001.9` with:
  - Purpose: harden governance so a developer-facing implementation spec cannot be approved as part of a gate package unless it is actually included, structurally specific, and independently assessed for commissionability
  - Trigger text explicitly carrying forward the approved client rationale:
    - the implementation spec with execution audience developer was not truly part of the Gate-001 package before approval
    - `guideline_workspace_implementation.md` allowed vague `Implementation Detail`
    - the AC004 external review failed to recognize the missing/weak implementation spec and failed to assess the implementation details within each SPEC
  - changelog row `v1.21.0 | 2026-03-25 | Amendment | Added AC001.10 under the AC001.x governance family to harden IMPLEMENTATION-detail precision, external-review sufficiency, and post-approval gate-package governance. Trigger source: client-approved AC004 QA on missing implementation-spec inclusion, vague Implementation Detail allowance, and external-review insufficiency.`
- Do NOT remove or rewrite unrelated AC001.9 closeout changes already present in this file.

2. Create `plan_T104-PH001-ST008-AC001.10.md`

Required frontmatter:
- `artifact_type: 'PLAN'`
- `planning_level: 'ACTIVITY'`
- `initiative_id: 'T104'`
- `initiative_code: 'CWS'`
- `phase: '1'`
- `stream_id: 'T104-PH001-ST008'`
- `activity_id: 'T104-PH001-ST008-AC001.10'`
- `version: '1.0.0'`
- `date: '2026-03-25'`
- `status: 'draft'`
- `author: 'LLM_Consultant'`
- `decision_owner_role: 'Client'`
- `governance_rules: 'prompt/templates/consultant/workspace/workspace_documentation_rules.md'`
- `procedural_guideline: 'prompt/templates/consultant/workspace/guideline_workspace_plan.md'`
- `parent_plan: 'prompt/artifacts/tasks/T104/workspace/PH001/ST008/plan_T104-PH001-ST008.md'`

Required title:
- `IMPLEMENTATION Spec Precision, External-Review Sufficiency & Post-Approval Gate Package Governance`

Required Executive Summary:
- explicitly carry forward the approved client trigger in prose:
  - the implementation spec with execution audience `developer` was not part of the Gate-001 package before it was approved
  - `guideline_workspace_implementation.md` allows consultants to author vague `Implementation Detail`
  - `analysis_P-PH000-ST002-AC004_gate-001-external-review.md` did not detect the missing/weak implementation spec and did not assess per-SPEC implementation sufficiency
- state that AC001.10 exists to close those governance gaps permanently

Required task register:
- `TK001` - gap analysis for implementation-spec precision, external-review sufficiency, and IMPLEMENTATION-family supersession handling
- `TK002` - produce standards-input proposal for governance changes
- `TK003` - produce GATE-001 gate-disposition proposal
- `GATE-001` - client approval of governance direction
- `TK004` - implement approved guideline/template/rules changes
- `TK005` - DEV-REPORT
- `TK006` - verification
- `TK007` - GATE-002 gate-disposition proposal
- `GATE-002` - client acceptance of implemented governance changes

Required outputs named in the plan:
- `prompt/templates/consultant/workspace/guideline_workspace_implementation.md`
- `prompt/templates/consultant/workspace/template_workspace_implementation_task-specification.md`
- `prompt/templates/consultant/workspace/guideline_workspace_analysis.md`
- `prompt/templates/consultant/workspace/guideline_workspace_plan.md`
- `prompt/templates/consultant/workspace/guideline_workspace_proposal.md`
- `prompt/templates/consultant/workspace/workspace_documentation_rules.md`

Required success criteria:
- task-specification minimum detail rules become explicit and enforceable
- external-review guidance explicitly requires per-SPEC developer commissionability assessment
- post-approval gate-package insufficiency decision test distinguishes recycle vs reject vs supersede
- IMPLEMENTATION-family historical/supersession handling is explicitly governed

## IV. IMPLEMENTATION SEQUENCE

1. Amend the AC004 activity plan to encode supersession, new task rows, successor GATE-002, renumbered GATE-003, and updated links.
2. Align the ST002 stream plan, PH000 phase plan, roadmap, and ST002 notes register to the successor posture and register SES005.
3. Supersede the old GATE-001 proposal and both old GATE-001 analysis artifacts using only the governed supersession mechanics.
4. Create the new comparative analysis and SES005 session notes.
5. Create the successor operating-model analysis.
6. Create the successor developer-facing first-operationalization task specification.
7. Create the successor GATE-002 external review.
8. Create the successor GATE-002 gate-disposition proposal with Primary vs Historical Evidence split.
9. Register AC001.10 in the ST008 stream plan and create the full AC001.10 activity plan.
10. Re-read all new and amended files to confirm that the live package consistently points to successor GATE-002 and no live surface still treats the old wrap-up-based GATE-001 package as current authority.

## V. REFERENCES

| Document | Path |
|:--|:--|
| Governing Plan | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/plan_P-PH000-ST002-AC004.md` |
| Current AC004 Plan | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/plan_P-PH000-ST002-AC004.md` |
| Current ST002 Stream Plan | `prompt/artifacts/tasks/P/workspace/PH000/ST002/plan_P-PH000-ST002.md` |
| Current PH000 Phase Plan | `prompt/artifacts/tasks/P/workspace/PH000/plan_P-PH000.md` |
| Current Program Roadmap | `prompt/artifacts/tasks/P/ssot/roadmap_P-PROGRAM_phase0.md` |
| Current ST002 Notes Register | `prompt/artifacts/tasks/P/workspace/PH000/ST002/notes_P-PH000-ST002.md` |
| Historical GATE-001 Proposal | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/proposal/proposal_P-PH000-ST002-AC004-GATE-001_operating-model-disposition.md` |
| Historical GATE-001 External Review | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/analysis/analysis_P-PH000-ST002-AC004_gate-001-external-review.md` |
| Historical Operating-Model Analysis | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/analysis/analysis_P-PH000-ST002-AC004_operating-model-and-reconciliation-policy.md` |
| Historical First-Slice Task Specification | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/implementation/implementation_P-PH000-ST002-AC004_first-operationalization-task-specification.md` |
| ST008 Stream Plan | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/plan_T104-PH001-ST008.md` |
| AC002 Supersession Precedent | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC002/plan_P-PH000-ST002-AC002.md` |
| AC002 Successor Proposal Precedent | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC002/proposal/proposal_P-PH000-ST002-AC002-GATE-002_design-decision-disposition.md` |
| AC001.4 Application-Guidance Precedent | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.4/analysis/analysis_T104-PH001-ST008-AC001.4_retroactive-ac002-application-guidance.md` |
| Implementation Guideline | `prompt/templates/consultant/workspace/guideline_workspace_implementation.md` |

## VI. ORCHESTRATOR REVIEW CHECKLIST

The consultant-orchestrator MUST verify all of the following after execution and before treating this package as complete:

1. Current-state reconciliation:
- no instruction was satisfied by replaying stale version assumptions over already-updated files
- pre-existing compliant content in `SES005`, the ST002 notes register, and the ST008 stream plan was preserved

2. Live AC004 posture:
- the AC004 activity plan and summary surfaces treat `GATE-001` as superseded historical record, `GATE-002` as the active consultation milestone, and `GATE-003` as the downstream implementation-acceptance gate
- no live summary surface still claims that `TK004` is currently unblocked from the old `GATE-001` approval

3. Historical-artifact governance:
- the old `GATE-001` proposal and the two old `GATE-001` analyses are marked `superseded` with required backlinks and deprecation notices only
- their substantive historical bodies were not rewritten beyond governed supersession mechanics

4. Successor-package consistency:
- the comparative analysis, `SES005`, successor operating-model analysis, successor developer-facing task specification, successor external review, and successor `GATE-002` proposal all exist and point to the same successor baseline
- the live successor package consistently selects `prompt/skills/session-close/SKILL.md`
- the old wrap-up-based implementation spec is treated as historical-only context

5. Successor implementation-spec commissionability:
- every SPEC in the successor developer-facing task specification names exact target files, required end-state posture, explicit non-targets, and validation checks
- the successor developer-facing task specification leaves no unresolved architecture choice or file-target ambiguity for downstream developer execution

6. Follow-on governance registration:
- `T104-PH001-ST008-AC001.10` is registered with the approved three-part QA trigger and is clearly framed as governance follow-on rather than hidden implementation scope

7. Forbidden-surface compliance:
- no edits were made to `prompt/artifacts/tasks/P/status/status_program.yaml`
- no edits were made to `prompt/artifacts/tasks/P/status/status_program.md`
- no edits were made to root `AGENTS.md`
- no edits were made to `prompt/AGENTS.md`
- no edits were made to `prompt/artifacts/tasks/P/standard/standard_P-STD-002_program-status-standard.md`

8. Remediation classification rule:
- if review finds a missing or incorrect deliverable inside the approved scope, treat it as deliverable remediation and commission a bounded remediation pass
- if review finds that this specification itself left an authority gap or unresolved decision, amend this specification first and then commission the remediation pass against the amended authority

## VII. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-03-25 | Initial | Authored the consultant-execution task specification for AC004 post-approval gate supersession, successor GATE-002 package creation, and AC001.10 governance-hardening registration. Includes exact file-level instructions for plan/summary-surface alignment, governed supersession of historical artifacts, new successor-package artifact creation, nested successor developer-facing task-spec requirements, and AC001.10 activity-plan creation. |
