---
artifact_type: 'IMPLEMENTATION'
implementation_type: 'task_specification'
initiative_id: 'P'
initiative_code: 'PROGRAM'
phase: '0'
stream_id: 'P-PH000-ST002'
activity_id: 'P-PH000-ST002-AC004'
task_id: 'P-PH000-ST002-AC004-TK008'
version: '1.0.4'
date: '2026-03-28'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/plan_P-PH000-ST002-AC004.md'
execution_audience: 'agentic_executor'
purpose: 'Exact consultant-owned closeout execution contract for AC004 after GATE-003 approval, including authoritative decision recording through the designated assistant sub-agent, stale status reconciliation, session-note closeout capture, and minimum downstream-readiness alignment.'
---

# IMPLEMENTATION (Task Specification): AC004 Post-GATE-003 Closeout And Downstream Readiness

## I. PURPOSE & AUTHORITY
- Purpose: Specify the exact consultant-owned closeout work that finishes AC004 after an approving `GATE-003` decision and leaves the workspace ready to begin the next governed activity without status drift.
- Authority chain: The AC004 activity plan retains tracked-work authority -> this artifact specifies HOW the consultant-owned closeout is executed -> proposal GDR remains the sole decision record surface and notes/status/plan artifacts record the resulting closed state.
- Audience: Designated `GPT-5.4-Mini` `xhigh` assistant sub-agent acting on the consultant's behalf. This artifact remains consultant-authored authority, but all AC004 execution from this point forward is delegated through that assistant boundary.
- This artifact does NOT hold a GDR. Gate decisions remain exclusively in the `GATE-003` gate-disposition proposal.
- Execution authorization note: For this AC004 closeout cycle, the Client has explicitly authorized the designated assistant sub-agent to record the approving `GATE-003` decision on the consultant's behalf and then execute the remaining AC004 closeout work under this specification. The executor MUST use `APPROVE` as the only allowed client-decision value for this cycle.
- Routing rule: from this point forward, every AC004 closeout edit and any follow-on AC004 status-alignment edit MUST pass through the designated assistant sub-agent. The consultant may review, verify, or approve the resulting output, but MUST NOT bypass the assistant boundary for direct execution edits.

## II. TASK SCOPE
- Governing plan task: `P-PH000-ST002-AC004-TK008`
- Trigger: AC004 is at a clean pending `GATE-003` disposition state, and the Client has now authorized the assistant sub-agent to record the approving decision and complete the remaining authoritative closeout execution, including stale AC003 status correction and minimum downstream-readiness alignment.
- Deliverable contract:
  - Updated `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/proposal/proposal_P-PH000-ST002-AC004-GATE-003_first-operationalization-disposition.md`
  - Updated `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/plan_P-PH000-ST002-AC004.md`
  - New `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/snotes/snotes_P-PH000-ST002-AC004-SES010.md`
  - Updated `prompt/artifacts/tasks/P/workspace/PH000/ST002/notes_P-PH000-ST002.md`
  - Updated `prompt/artifacts/tasks/P/status/status_program.yaml`
  - Updated `prompt/artifacts/tasks/P/status/status_program.md`
  - Updated `prompt/artifacts/tasks/P/workspace/PH000/ST002/plan_P-PH000-ST002.md`
  - Updated `prompt/artifacts/tasks/P/workspace/PH000/plan_P-PH000.md`
  - Updated `prompt/artifacts/tasks/P/ssot/roadmap_P-PROGRAM_phase0.md`

## III. SPECIFICATION ITEMS

### SPEC-001 — Record the client-authorized approving GATE-003 decision as the first execution step

| Field | Detail |
|:--|:--|
| Requirement Source | AC004 `GATE-003` authority model, proposal-hosted GDR rules, and the current client instruction delegating decision recording to the assistant sub-agent on the consultant's behalf |
| Target file(s) | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/proposal/proposal_P-PH000-ST002-AC004-GATE-003_first-operationalization-disposition.md` |
| Required end-state posture | The live proposal GDR is updated from `pending` to `APPROVE` as the first AC004 execution action, using the client-authorized assistant-sub-agent path defined in this specification |
| Explicit non-target / do-not-change constraints | Do not use any decision state other than `APPROVE`; do not invent conditions; do not alter the consultant recommendation |
| Validation check | Before touching any other AC004 surface, confirm the proposal GDR now shows `Client Decision = APPROVE`, `Gate Status After Decision = completed`, `Decision Date = 2026-03-28`, and a non-pending decision reference |
| Blocking ambiguity rule | If the live GDR already records `RECYCLE`, `REJECT`, `SUPERSEDE`, or any non-approve state, stop and escalate immediately instead of overwriting it |
| Status | `open` |

#### Implementation Detail

- Open the live `GATE-003` proposal first.
- If the `## Gate Decision Record` still shows `Client Decision | pending`, update it to the authorized end state defined in this specification and then continue.
- If the live GDR already records `APPROVE`, treat SPEC-001 as already satisfied and continue.
- Do not continue on `APPROVE WITH CONDITIONS`; this task specification is for clean AC004 closeout after straight approval only.
- After the required GDR update, continue all remaining AC004 file edits through the designated assistant sub-agent boundary and then return the completed output for consultant review.

### SPEC-002 — Normalize the proposal body around the now-recorded approving decision

| Field | Detail |
|:--|:--|
| Requirement Source | AC004 `GATE-003` proposal, proposal GDR rules, and AC004 closeout plan authority |
| Target file(s) | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/proposal/proposal_P-PH000-ST002-AC004-GATE-003_first-operationalization-disposition.md` |
| Required end-state posture | The GDR records the approving client decision, the gate status becomes `completed`, and the proposal body no longer describes AC004 closeout as pending |
| Explicit non-target / do-not-change constraints | Do not alter the evidence stack or consultant recommendation beyond what is required to record the decision and downstream enforcement state |
| Validation check | The GDR shows `Client Decision = APPROVE`, `Gate Status After Decision = completed`, `Decision Date = 2026-03-28`, and a non-pending decision reference |
| Blocking ambiguity rule | If the client-approved decision reference is not available in the live repo context, stop and escalate instead of inventing a citation |
| Status | `open` |

#### Implementation Detail

- In the proposal GDR:
  - set or confirm `Client Decision` as `APPROVE`
  - set or confirm `Gate Status After Decision` as `completed`
  - keep `Conditions (if any)` as `—`
  - set or confirm `Decision Date` as `2026-03-28`
  - set `Decision Reference` to `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/snotes/snotes_P-PH000-ST002-AC004-SES010.md`
- In Section V downstream enforcement, remove the statement that AC005 and AC006 remain blocked until AC004 closes through `TK008`; replace it with wording that AC004 is implementation-accepted and closes through the authoritative closeout updates executed under `TK008`.
- Increment the patch version to `1.0.3` and keep `date: '2026-03-28'`.

### SPEC-003 — Close AC004 in its activity plan and preserve a clean audit trail

| Field | Detail |
|:--|:--|
| Requirement Source | AC004 plan authority, tracked-work completion rules, and gate exit semantics |
| Target file(s) | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/plan_P-PH000-ST002-AC004.md` |
| Required end-state posture | The new implementation-spec authoring task is recorded as completed, `GATE-003` is completed, `TK008` is completed, and the plan clearly states AC004 is closed with AC005 and AC006 released from the AC004 closeout blocker |
| Explicit non-target / do-not-change constraints | Do not reopen or renumber earlier historical AC004 tasks; do not delete superseded lineage references |
| Validation check | The task register, gate model, detailed task text, and changelog all tell the same post-closeout story |
| Blocking ambiguity rule | If the live plan already contains conflicting post-closeout task insertions, stop and escalate instead of merging incompatible histories |
| Status | `open` |

#### Implementation Detail

- Increment the patch version to `1.11.0` and keep `date: '2026-03-28'`.
- In the Task Register:
  - insert `TK007.3` immediately after `TK007.2` with status `completed`, owner `LLM_Consultant`, depends on `TK007.2`, target `implementation/`, reference `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/implementation/implementation_P-PH000-ST002-AC004_post-gate-003-closeout-and-downstream-readiness-task-specification.md`, and action summarizing authorship of the exact post-approval consultant closeout specification
  - change `GATE-003` so it depends on `TK007.3`
  - change `GATE-003` status from `in_progress` to `completed`
  - change `GATE-003` action so it records that the client approved the first operationalization slice on 2026-03-28 and the gate is now closed
  - change `TK008` status from `planned` to `completed`
  - change `TK008` depends-on value to `GATE-003`
  - change `TK008` action to summarize completion of proposal, notes, status, stream, phase, and roadmap closeout updates plus downstream release from the AC004 closeout blocker
- In the Executive Summary, Objective, and Gate Model text:
  - replace pending-closeout wording with closed-state wording
  - state that AC004 is now closed after the approving `GATE-003` decision and `TK008` execution
  - state that AC005 and AC006 remain separate planned follow-on activities, but no longer blocked by AC004 closeout
- Add a detailed task section for `TK007.3` in the existing plan style and update the `TK008` detailed section so its deliverable and steps match the actual executed closeout scope instead of generic future intent.
- In the `GATE-003` section, keep the gate record for audit trail but update the Exit Criteria narrative to past tense through the changelog and task register rather than leaving the gate open.

### SPEC-004 — Publish the AC004 closeout session record and register it JIT

| Field | Detail |
|:--|:--|
| Requirement Source | Notes guideline JIT registration rules and AC004 closeout audit-trail requirements |
| Target file(s) | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/snotes/snotes_P-PH000-ST002-AC004-SES010.md`, `prompt/artifacts/tasks/P/workspace/PH000/ST002/notes_P-PH000-ST002.md` |
| Required end-state posture | One new AC004 activity session note captures the approving decision, closeout execution, stale-status correction, and downstream-readiness release; the ST002 notes register indexes it immediately |
| Explicit non-target / do-not-change constraints | Do not back-edit earlier session bodies into the new state; preserve SES009 as the pre-closeout preparation record |
| Validation check | The new session note follows the activity-session template order and the ST002 register contains a new AC004 SES010 row plus changelog entry |
| Blocking ambiguity rule | If `SES010` already exists with conflicting content, stop and escalate instead of overwriting it |
| Status | `open` |

#### Implementation Detail

- Create `snotes_P-PH000-ST002-AC004-SES010.md` as an activity-scoped session note titled for AC004 `GATE-003` approval, closeout completion, stale-status reconciliation, and downstream readiness release.
- The session note must explicitly capture:
  - client approval of `GATE-003`
  - execution of `TK008`
  - correction of stale AC003 status in the ledger/narrative
  - release of AC005 and AC006 from the AC004 closeout blocker
  - decision that AC006 remains planning-ready only and is not implementation-started in this AC004 closeout pass
- Update `notes_P-PH000-ST002.md`:
  - add a new AC004 `SES010` row in the Activity Notes Register
  - increment the patch version and keep `date: '2026-03-28'`
  - add a new changelog row at the top summarizing registration of AC004 closeout session `SES010`

### SPEC-005 — Repair the authoritative status surfaces and remove the stale AC004 closeout blocker

| Field | Detail |
|:--|:--|
| Requirement Source | Program status protocol Section 7, AC004 closeout findings, and stream/phase anti-drift rules |
| Target file(s) | `prompt/artifacts/tasks/P/status/status_program.yaml`, `prompt/artifacts/tasks/P/status/status_program.md`, `prompt/artifacts/tasks/P/workspace/PH000/ST002/plan_P-PH000-ST002.md`, `prompt/artifacts/tasks/P/workspace/PH000/plan_P-PH000.md`, `prompt/artifacts/tasks/P/ssot/roadmap_P-PROGRAM_phase0.md` |
| Required end-state posture | AC003 is corrected to `completed`, AC004 is shown as closed/completed where applicable, and broader summary surfaces no longer describe AC005/AC006 as blocked behind AC004 closeout |
| Explicit non-target / do-not-change constraints | Do not add AC006 internal gate-package detail to the broader surfaces; keep AC005 as a separate planned lane |
| Validation check | Ledger, narrative, stream plan, phase plan, and roadmap all tell the same post-closeout story with no lingering AC003/AC004 contradiction |
| Blocking ambiguity rule | If any summary surface has been changed independently to a conflicting next-activity posture, stop and escalate instead of inventing a merged milestone story |
| Status | `open` |

#### Implementation Detail

- In `status_program.yaml`:
  - change `P-PH000-ST002-AC003` from `planned` to `completed`
  - update its `as_of`, `updated_by`, and `last_updated` to the live closeout date and consultant author
  - update the evidence summary so it no longer cites the stream plan row as `planned`
  - change `P-PH000-ST002-AC004` from `in_progress` to `completed`
  - leave `P-PH000-ST002-AC005` and `P-PH000-ST002-AC006` as `planned`
  - keep the dependency edges from AC004 to AC005 and AC006 structurally present, but update downstream evidence summaries so they no longer imply an unresolved AC004 closeout blocker
- In `status_program.md`:
  - re-derive the affected sections from the updated ledger
  - ensure AC003 shows `completed`
  - ensure AC004 shows `completed`
  - keep AC005 and AC006 as `planned`
  - remove stale narrative wording that says AC005 and AC006 remain blocked behind AC004 closeout
- In `plan_P-PH000-ST002.md`, `plan_P-PH000.md`, and `roadmap_P-PROGRAM_phase0.md`:
  - replace any wording that says AC005 and AC006 are blocked behind AC004 closeout
  - update the AC004 posture from pending closeout to completed closeout
  - keep AC005 and AC006 as separate planned follow-on lanes
  - do not elevate AC006 to exclusive next milestone; keep the broader surfaces neutral at contract level

### SPEC-006 — Preserve AC006 implementation boundaries during the AC004 worker pass

| Field | Detail |
|:--|:--|
| Requirement Source | User orchestration directive and AC006 planning-only scope |
| Target file(s) | Protected non-target set: all `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/**` files, `prompt/skills/session-close/SKILL.md`, and any future AC006 proposal/implementation surface |
| Required end-state posture | The AC004 worker does not touch AC006 files or begin AC006 implementation work |
| Explicit non-target / do-not-change constraints | Treat all AC006 paths as read-only during this execution pass |
| Validation check | The changed-file list for the AC004 worker excludes every AC006 path |
| Blocking ambiguity rule | If any AC004 closeout step appears to require direct AC006 plan editing, stop and escalate to the consultant instead of widening the worker scope |
| Status | `open` |

#### Implementation Detail

- This worker pass ends after AC004 closeout surfaces are complete and reviewed.
- Do not create or edit AC006 analysis, proposal, implementation, or plan files during this pass.
- Do not change `prompt/skills/session-close/SKILL.md`; AC006 hardening is a separate phase authored directly by the consultant after AC004 review is accepted.

## IV. IMPLEMENTATION SEQUENCE
1. Read the live AC004 proposal, AC004 plan, ST002 notes register, status ledger, status narrative, stream plan, phase plan, and roadmap.
2. Apply `SPEC-001` as the gating preflight.
3. If preflight passes, apply `SPEC-002` through `SPEC-005` in order.
4. Re-read all changed files and confirm cross-reference integrity.
5. Return a concise execution summary listing every changed file and explicitly stating that no AC006 path was touched.

## V. REFERENCES

| Document | Path |
|:--|:--|
| Governing Plan | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/plan_P-PH000-ST002-AC004.md` |
| GATE-003 Proposal | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/proposal/proposal_P-PH000-ST002-AC004-GATE-003_first-operationalization-disposition.md` |
| Implementation Guideline | `prompt/templates/consultant/workspace/guideline_workspace_implementation.md` |
| Notes Guideline | `prompt/templates/consultant/workspace/guideline_workspace_notes.md` |
| Plan Guideline | `prompt/templates/consultant/workspace/guideline_workspace_plan.md` |
| Program Status Narrative | `prompt/artifacts/tasks/P/status/status_program.md` |

## VI. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.4 | 2026-03-28 | Amendment | Corrected the execution audience to the designated `GPT-5.4-Mini` `xhigh` assistant sub-agent boundary so AC004 closeout execution remains assistant-driven and the frontmatter now matches the body contract. |
| v1.0.3 | 2026-03-28 | Amendment | Corrected the task-specification header to `execution_audience=consultant` while preserving the designated assistant-sub-agent execution boundary for all AC004 closeout edits, and normalized the changelog sequence after the assistant-boundary clarification. |
| v1.0.2 | 2026-03-28 | Amendment | Clarified that every AC004 closeout edit and follow-on AC004 status-alignment edit routes through the designated assistant sub-agent, and made the consultant review boundary explicit after the assistant completes the required GDR update. |
| v1.0.1 | 2026-03-28 | Amendment | Recast the execution audience to the designated assistant sub-agent, made the client-authorized `APPROVE` recording explicit as the first execution step, and clarified that all remaining AC004 execution now proceeds only through the assistant boundary. |
| v1.0.0 | 2026-03-28 | Initial | Authored the exact consultant-owned execution contract for AC004 post-`GATE-003` closeout, authoritative decision recording, stale AC003 status reconciliation, session-note closeout capture, and minimum downstream-readiness alignment ahead of later AC006 planning work. |
