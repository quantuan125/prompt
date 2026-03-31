---
artifact_type: 'IMPLEMENTATION'
implementation_type: 'task_specification'
initiative_id: 'P'
initiative_code: 'PROGRAM'
phase: '0'
stream_id: 'P-PH000-ST002'
activity_id: 'P-PH000-ST002-AC006'
task_id: 'P-PH000-ST002-AC006-TK006.2'
version: '1.0.0'
date: '2026-03-31'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/plan_P-PH000-ST002-AC006.md'
execution_audience: 'assistant'
purpose: 'Assistant-executed post-review refresh brief for the AC006 GATE-001 proposal package so the client-facing reading set reflects completed TK006.1 and TK006.2 evidence before client disposition.'
---

# IMPLEMENTATION (Task Specification): AC006 GATE-001 Proposal Refresh Brief

## I. PURPOSE & AUTHORITY
- Purpose: Govern the exact proposal-refresh edits required after completion of `TK006.1` and `TK006.2` so the live AC006 `GATE-001` package becomes the correct client-facing reading set.
- Authority chain: The AC006 plan defines `TK006.2` as the consultant-owned readiness assessment -> the completed `TK006.1` and `TK006.2` analyses establish the final pre-presentation package findings -> this artifact specifies HOW the assistant refreshes the proposal package -> the consultant reviews the assistant output before any client presentation.
- Audience: `LLM_Assistant`
- Filename note: This is an assistant-scoped orchestration artifact using the `-brief` filename convention while retaining `implementation_type: 'task_specification'`.
- This artifact does NOT hold a GDR. The proposal file being refreshed still holds the authoritative Gate Decision Record, and client decision fields remain pending in this execution slice.

## II. TASK SCOPE
- Governing plan task: `P-PH000-ST002-AC006-TK006.2`
- Trigger: `TK006.1` and `TK006.2` are now complete, and both analyses conclude that the remaining blocker is stale proposal packaging rather than substantive package insufficiency.
- Deliverable contract:
  - refreshed `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/proposal/proposal_P-PH000-ST002-AC006-GATE-001_session-close-and-briefing-disposition.md`
  - no edits to the AC006 plan
  - no edits to either new analysis artifact
  - no GDR client decision recorded

## III. SPECIFICATION ITEMS

### SPEC-001 - Refresh proposal frontmatter and executive summary to the post-review package state

| Field | Detail |
|:--|:--|
| Requirement Source | `TK006.1` external review; `TK006.2` consultant assessment; `guideline_workspace_proposal.md` frontmatter and gate-disposition structure rules |
| Target file(s) | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/proposal/proposal_P-PH000-ST002-AC006-GATE-001_session-close-and-briefing-disposition.md` |
| Required end-state posture | The proposal frontmatter and Executive Summary describe the current post-review package state rather than the original pre-review TK006 base package. |
| Explicit non-target / do-not-change constraints | Do NOT change the proposal archetype. Do NOT change the gate ID, activity ID, or governing plan reference. Do NOT add any client decision outcome. |
| Validation check | Frontmatter contains `external_review_reference`; Executive Summary no longer says `TK006.1` and `TK006.2` are deferred next-session work. |
| Blocking ambiguity rule | If the current proposal already contains additional unreviewed edits beyond the live reviewed baseline, stop and escalate instead of merging assumptions into this refresh pass. |
| Status | `open` |

#### Implementation Detail

1. Open the proposal file and update frontmatter only as follows:
   - change `version` from `1.0.0` to `1.1.0`
   - change `date` from `2026-03-30` to `2026-03-31`
   - keep `status: 'draft'`
   - keep `analysis_reference` unchanged
   - add `external_review_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/analysis/analysis_P-PH000-ST002-AC006-GATE-001_external-review.md'`
2. In `## I. EXECUTIVE SUMMARY`, rewrite the third bullet (`Scope`) so it states that the proposal now packages the completed review lane through `TK006.2` and is the refreshed client-facing reading set for the same gate.
3. Keep the first two bullets conceptually intact, but update their wording where needed so the package is described as post-review rather than base-package-only.
4. Do not add new frontmatter keys other than `external_review_reference`.

### SPEC-002 - Refresh the Gate Package Index to completed post-review posture

| Field | Detail |
|:--|:--|
| Requirement Source | `TK006.1`; `TK006.2`; `guideline_workspace_proposal.md` Section V.B Gate Package Index rules |
| Target file(s) | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/proposal/proposal_P-PH000-ST002-AC006-GATE-001_session-close-and-briefing-disposition.md` |
| Required end-state posture | Section II.A shows the live post-review package, with `TK006.1` and `TK006.2` treated as completed package evidence and the previously authored consultant deliverables no longer described as pending placeholders. |
| Explicit non-target / do-not-change constraints | Do NOT remove any existing row from the table. Do NOT invent new deliverables. Do NOT change paths away from the existing governed artifact locations. |
| Validation check | `TK003`, `TK004`, `TK005`, `TK006`, `TK006.1`, and `TK006.2` are no longer shown as `planned`/`pending`; `TK006.1` and `TK006.2` are present as completed package items. |
| Blocking ambiguity rule | If any referenced artifact path does not exist at execution time, stop and escalate instead of silently deleting or renaming table rows. |
| Status | `open` |

#### Implementation Detail

1. In `## II. GATE PACKAGE` -> `### A. Gate Package Index`, keep the existing table structure and row order.
2. Update these row fields exactly:
   - `TK003` row -> `Status: completed`, `Acceptance: accepted`, `Client Priority: Required`
   - `TK004` row -> `Status: completed`, `Acceptance: accepted`, `Client Priority: Required`
   - `TK005` row -> `Status: completed`, `Acceptance: accepted`, `Client Priority: Required`
   - `TK006` row -> `Status: completed`, `Acceptance: accepted`, `Client Priority: Required`
   - `TK006.1` row -> `Status: completed`, `Acceptance: accepted`, `Client Priority: Required`
   - `TK006.2` row -> `Status: completed`, `Acceptance: accepted`, `Client Priority: Required`
3. Keep `TK000`, `TK001`, and `TK002` unchanged because they already reflect completed accepted evidence.
4. Do not relabel the table into primary/historical evidence; keep this proposal on its current table model.

### SPEC-003 - Refresh the Evidence Index and References to designate the authoritative external review and completed consultant assessment

| Field | Detail |
|:--|:--|
| Requirement Source | `TK006.1` external review findings GAP-001/GAP-002; `TK006.2` GAP-001; `guideline_workspace_proposal.md` rules for authoritative external review designation |
| Target file(s) | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/proposal/proposal_P-PH000-ST002-AC006-GATE-001_session-close-and-briefing-disposition.md` |
| Required end-state posture | The Evidence Index and References section no longer describe the review lane as future or optional; the proposal clearly names `TK006.1` as the authoritative external review and includes `TK006.2` as completed consultant evidence. |
| Explicit non-target / do-not-change constraints | Do NOT create a historical-evidence subsection in this proposal. Do NOT remove existing upstream evidence rows that still support the package. |
| Validation check | The Evidence Index notes for `TK006.1` and `TK006.2` describe them as completed package evidence, and Section VII no longer says `External Review (optional)`. |
| Blocking ambiguity rule | If more than one external-review artifact appears to compete for authority, stop and escalate instead of guessing which one is authoritative. |
| Status | `open` |

#### Implementation Detail

1. In `### B. Evidence Index`, update the `TK006.1 external review` row note from future/pending wording to: `Authoritative independent external review for the completed consultation-only gate package.`
2. Update the `TK006.2 consultant assessment` row note from future/pending wording to: `Consultant-owned assessment of the external review and current downstream readiness posture.`
3. Keep all other Evidence Index rows present unless a path is objectively wrong; this execution slice is not a broader evidence-pruning pass.
4. In `## VII. REFERENCES`, replace the `External Review (optional)` row with:
   - `Authoritative External Review | prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/analysis/analysis_P-PH000-ST002-AC006-GATE-001_external-review.md`
5. Add a new row immediately after it:
   - `Consultant Assessment | prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/analysis/analysis_P-PH000-ST002-AC006-GATE-001_external-review-and-downstream-readiness-assessment.md`
6. Leave the existing Governing Plan, Input Analysis, and Supporting Analysis rows intact.

### SPEC-004 - Refresh the consultant recommendation, deferral language, and GDR posture to the ready-for-client-review state

| Field | Detail |
|:--|:--|
| Requirement Source | `TK006.1` independent gate position; `TK006.2` consultant recommendation; gate-disposition GDR rules in `guideline_workspace_proposal.md` |
| Target file(s) | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/proposal/proposal_P-PH000-ST002-AC006-GATE-001_session-close-and-briefing-disposition.md` |
| Required end-state posture | Section V and Section VI present the current consultant position: the refreshed package is ready for client disposition on an `APPROVE WITH CONDITIONS` recommendation while client decision fields remain pending. |
| Explicit non-target / do-not-change constraints | Do NOT record a client decision. Do NOT mark the gate as completed. Do NOT start describing `TK007` or `TK008` as authorized. |
| Validation check | Section V no longer says `RECYCLE`; Section VI shows `Consultant Recommendation | APPROVE WITH CONDITIONS`, `Client Decision | pending`, and `Gate Status After Decision | pending`. |
| Blocking ambiguity rule | If the live proposal contains other unresolved package defects not identified by `TK006.1` and `TK006.2`, stop and escalate instead of broadening the recommendation logic on the fly. |
| Status | `open` |

#### Implementation Detail

1. In `## V. CONSULTANT GATE RECOMMENDATION`, replace `Consultant recommendation: - RECYCLE` with `Consultant recommendation: - APPROVE WITH CONDITIONS`.
2. Keep `Reviewer verdict alignment (implementation-backed gates only)` as `N/A - consultation-only gate`.
3. Replace the current `Conditions and/or deferrals` bullets with exactly these three bullets:
   - `The gate remains pending until the client records a decision in the GDR.`
   - `No post-gate execution may begin until the GDR records Client Decision = APPROVE or APPROVE WITH CONDITIONS.`
   - `After GATE-001 approval and before any later execution-evidence package is presented, the AC006 plan must be amended to register the execution-backed gate/readiness path toward GATE-002.`
4. Remove the current `Recycle reassessment path (`RECYCLE` only):` subsection entirely because the refreshed package is no longer being presented on a recycle posture.
5. Rewrite `Downstream enforcement` so it states that client disposition is now being requested from the refreshed package, but `TK007` and `TK008` remain blocked until an approving client decision is recorded.
6. In `## VI. GATE DECISION RECORD (GDR)`, update only these fields:
   - `Consultant Recommendation | APPROVE WITH CONDITIONS`
   - `Client Decision | pending`
   - `Gate Status After Decision | pending`
   - `Conditions (if any) | (1) The gate remains pending until the client records a decision in the GDR. (2) No post-gate execution may begin until the GDR records Client Decision = APPROVE or APPROVE WITH CONDITIONS. (3) After GATE-001 approval and before any later execution-evidence package is presented, the AC006 plan must be amended to register the execution-backed gate/readiness path toward GATE-002.`
7. Leave `Decided By`, `Decision Date`, and `Decision Reference` as pending-state fields.

### SPEC-005 - Refresh any lingering pre-review wording in the body without widening the package

| Field | Detail |
|:--|:--|
| Requirement Source | `TK006.1` and `TK006.2` finding that the remaining blocker is stale proposal wording |
| Target file(s) | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/proposal/proposal_P-PH000-ST002-AC006-GATE-001_session-close-and-briefing-disposition.md` |
| Required end-state posture | The proposal body reads as a coherent post-review package and contains no stale statements that the review lane is still future work. |
| Explicit non-target / do-not-change constraints | Do NOT rewrite GIR recommendations, options, or client decision prompts unless needed to remove stale pre-review wording. Do NOT add new GIRs. |
| Validation check | No remaining body text says `must be authored next session`, `pending next-session authoring`, or `optional` external review. |
| Blocking ambiguity rule | If removing stale wording would require a substantive rewrite of GIR logic rather than straightforward refresh, stop and escalate instead of redesigning the proposal. |
| Status | `open` |

#### Implementation Detail

1. Search the proposal body for these stale phrases or their exact equivalents:
   - `deferred to the next session`
   - `must be authored next session`
   - `pending next-session authoring`
   - `optional` external review
2. Replace each occurrence with wording that reflects the completed review lane and refreshed client-reading posture.
3. Keep GIR-001 through GIR-004 recommendations unchanged because both review artifacts agree with the current GIR set.
4. Keep the client decision checkboxes for each GIR blank and pending.

### SPEC-006 - Append a proposal changelog entry and run a bounded validation pass

| Field | Detail |
|:--|:--|
| Requirement Source | Proposal maintenance convention; need for a deterministic assistant closeout check |
| Target file(s) | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/proposal/proposal_P-PH000-ST002-AC006-GATE-001_session-close-and-briefing-disposition.md` |
| Required end-state posture | The proposal changelog records the refresh, and the assistant verifies that the refreshed package is internally consistent before handing it back to the consultant. |
| Explicit non-target / do-not-change constraints | Do NOT update the AC006 plan, notes, or analysis artifacts in this validation step. Do NOT stage, commit, or push anything. |
| Validation check | Changelog contains a new `v1.1.0` entry dated `2026-03-31`, and the final read-through confirms sections I, II, V, VI, and VII are mutually consistent. |
| Blocking ambiguity rule | If the refreshed proposal cannot be made internally consistent without editing files outside this proposal, stop and escalate instead of expanding the execution slice. |
| Status | `open` |

#### Implementation Detail

1. In `## VIII. CHANGELOG`, append this row above the existing `v1.0.0` row:

   `| v1.1.0 | 2026-03-31 | Amendment | Refreshed the AC006 GATE-001 proposal package after completion of TK006.1 and TK006.2, added the authoritative external-review reference, updated the package indexes to the post-review state, and changed the consultant recommendation from RECYCLE to APPROVE WITH CONDITIONS while keeping client decision fields pending. |`

2. After all proposal edits are complete, read the entire refreshed proposal top to bottom and verify all of the following:
   - frontmatter contains `external_review_reference`
   - Executive Summary describes the completed review lane
   - Gate Package Index no longer shows `TK006.1` or `TK006.2` as planned
   - Evidence Index and References no longer describe the external review as optional or future
   - Section V and the GDR in Section VI both use `APPROVE WITH CONDITIONS`
   - client decision fields remain pending
   - no file outside this proposal was edited
3. If all checks pass, stop and hand the refreshed proposal back to the consultant for review. Do not make any further package-maintenance edits.

## IV. IMPLEMENTATION SEQUENCE
1. Execute `SPEC-001` first so the proposal frontmatter and summary match the completed review lane.
2. Execute `SPEC-002` and `SPEC-003` next so the package indexes and references reflect current evidence.
3. Execute `SPEC-004` and `SPEC-005` after the indexes are current so the recommendation and body wording align to the refreshed package.
4. Execute `SPEC-006` last to append the changelog and run the bounded validation pass.

## V. REFERENCES

| Document | Path |
|:--|:--|
| Governing Plan | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/plan_P-PH000-ST002-AC006.md` |
| Gate Proposal To Refresh | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/proposal/proposal_P-PH000-ST002-AC006-GATE-001_session-close-and-briefing-disposition.md` |
| External Review | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/analysis/analysis_P-PH000-ST002-AC006-GATE-001_external-review.md` |
| Consultant Assessment | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/analysis/analysis_P-PH000-ST002-AC006-GATE-001_external-review-and-downstream-readiness-assessment.md` |
| Proposal Guideline | `prompt/templates/consultant/workspace/guideline_workspace_proposal.md` |
| Implementation Guideline | `prompt/templates/consultant/workspace/guideline_workspace_implementation.md` |

## VI. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-03-31 | Initial | Created the assistant-scoped AC006 proposal-refresh brief governing the exact post-review edits needed to convert the live GATE-001 proposal from pre-review recycle posture to a refreshed client-facing package with consultant recommendation APPROVE WITH CONDITIONS. |
