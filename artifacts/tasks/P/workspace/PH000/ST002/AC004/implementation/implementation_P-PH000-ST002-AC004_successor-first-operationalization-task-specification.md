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
date: '2026-03-26'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/plan_P-PH000-ST002-AC004.md'
execution_audience: 'developer'
purpose: 'Successor first-slice execution specification for AC004 TK004, replacing the historical wrap-up-based contract with the approved dedicated session-close convention and explicit per-surface execution detail.'
---

# IMPLEMENTATION (Task Specification): AC004 Successor First Operationalization Slice

## I. PURPOSE & AUTHORITY

- Purpose: Specify the exact downstream execution required to operationalize the successor AC004 baseline after `GATE-002` approval.
- Authority chain: The approved successor consultation plan for AC004 defines the restructure intent -> this artifact specifies HOW the developer executes TK004 -> the resulting dev-report, verification, and gate-disposition proposal hold the authoritative implementation evidence.
- Audience: `LLM_Developer` (primary executor). Secondary consumers: `LLM_Reviewer` and `Client` as package readers.
- This artifact does NOT hold a GDR. Gate decisions remain exclusively in gate-disposition proposals.
- This artifact replaces the historical wrap-up-based task specification as the active commissioning surface for AC004.
- The approved pre-implementation authority for session-close behavior is the session-close `standards_input` proposal. Any pre-existing concrete skill file is non-authoritative until TK004 operationalizes the approved convention.
- Execution under this artifact MUST NOT begin until `P-PH000-ST002-AC004-GATE-002` records approval.

## II. TASK SCOPE

- Governing plan task: `P-PH000-ST002-AC004-TK004`
- Trigger: The successor consultation gate selected a dedicated session-close convention and re-bound AC004 to the post-approval decision boundary. TK004 now executes against that approved successor baseline only.
- Deliverable contract:
  - Updated `prompt/artifacts/tasks/P/status/status_program.yaml`
  - Updated `prompt/artifacts/tasks/P/status/status_program.md`
  - Updated `prompt/artifacts/tasks/P/workspace/PH000/ST002/plan_P-PH000-ST002.md`
  - Updated `prompt/artifacts/tasks/P/workspace/PH000/plan_P-PH000.md`
  - Updated `prompt/artifacts/tasks/P/ssot/roadmap_P-PROGRAM_phase0.md`
  - Reconciled `prompt/skills/session-close/SKILL.md` aligned to the approved session-close standards-input proposal

**Explicit non-target surfaces**
- Do NOT edit root `AGENTS.md`
- Do NOT edit `prompt/AGENTS.md`
- Do NOT edit `prompt/skills/wrap-up/SKILL.md`
- Do NOT edit `prompt/artifacts/tasks/P/standard/standard_P-STD-002_program-status-standard.md`

## II.A EXECUTION TOKENS

- `<GATE_002_APPROVAL_DATE>` means the ISO date recorded in the `P-PH000-ST002-AC004-GATE-002` GDR when the Client approves the gate.
- `<TK004_EXECUTION_DATE>` means the ISO date on which the developer performs the TK004 edits. If TK004 is completed in one session, every file updated by TK004 MUST use the same `<TK004_EXECUTION_DATE>`.
- Where this artifact says "increment patch version", increase only the patch component of the live semantic version already present in the target file.

## II.B PREFLIGHT RULE

- Before editing any target file, read the current contents of every in-scope target named in this specification.
- Current repo state wins over stale draft assumptions, but only within the approved AC004 successor decision boundary.
- If a target file already satisfies the required end state, leave it unchanged and record it as verified.
- If a target file partially satisfies the required end state, merge only the missing required deltas.
- If the live file shape contradicts this specification in a way that changes the approved AC004 successor decision boundary, stop and escalate rather than inventing a merge strategy.

## III. SPECIFICATION ITEMS

### SPEC-001 - Reconcile authoritative stream-plan truth into the status ledger

| Field | Detail |
|:--|:--|
| Requirement Source | Approved AC004 successor package; `guideline_workspace_implementation.md` and `guideline_workspace_plan.md` successor-gate rules |
| Target file(s) | `prompt/artifacts/tasks/P/status/status_program.yaml` |
| Required end-state posture | AC004 is `in_progress` because `GATE-002` has already passed and TK004 is executing; `GATE-001` remains historical/superseded; `GATE-003` becomes the next client acceptance milestone; `AC005` remains planned and blocked behind AC004 |
| Explicit non-target / do-not-change constraints | Do not edit `status_program.md`, plan surfaces, AGENTS surfaces, or `P-STD-002` in this step |
| Validation check | Perform a ledger-first edit and then confirm the narrative can be derived from the ledger without contradiction |
| Blocking ambiguity rule | If the live ledger shape contradicts this end state, stop and escalate rather than inventing a merge strategy |
| Status | `open` |

#### Implementation Detail

- In `prompt/artifacts/tasks/P/status/status_program.yaml`, update the top-level fields `as_of`, `updated_by`, and `last_updated` to `<TK004_EXECUTION_DATE>`, `LLM_Developer`, and `<TK004_EXECUTION_DATE>`.
- In the existing entry with `scope_uid: P-PH000-ST002-AC004`:
  - change `status` from `planned` to `in_progress`
  - change `as_of` and `last_updated` to `<TK004_EXECUTION_DATE>`
  - keep `updated_by: LLM_Developer`
  - keep every health dimension as `unassessed`
  - keep the dependency edge from `P-PH000-ST002-AC003` to `P-PH000-ST002-AC004`, but change that dependency edge `status` from `open` to `resolved`
  - keep the existing plan-reference evidence item, update its `date` to `<TK004_EXECUTION_DATE>`, and change its summary to exactly `Source plan row for P-PH000-ST002-AC004 (status in_progress; raw depends_on: AC003)`
  - add a second evidence item after the plan-reference evidence using:
    - `type: decision`
    - `ref: prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/proposal/proposal_P-PH000-ST002-AC004-GATE-002_operating-model-disposition.md`
    - `date: <GATE_002_APPROVAL_DATE>`
    - `by: Client`
    - `summary: GATE-002 approved successor operating-model package; TK004 unblocked for manual-only consultant-led session-close V1 operationalization`
- Still in `status_program.yaml`, insert a new entry immediately after `P-PH000-ST002-AC004` for `scope_uid: P-PH000-ST002-AC005` with these exact field values and ordering:
  - `scope_type: activity`
  - `initiative_id: P`
  - `name: Commission Future Status-System Initiative (\`T105\` or next available ID)`
  - `status: planned`
  - `as_of: <TK004_EXECUTION_DATE>`
  - `updated_by: LLM_Developer`
  - `last_updated: <TK004_EXECUTION_DATE>`
  - `health.overall: unassessed`
  - every health dimension remains `unassessed`
  - one dependency edge from `P-PH000-ST002-AC004` to `P-PH000-ST002-AC005` with `relationship: depends_on`, `category: internal`, `criticality: critical`, `owner: LLM_Consultant`, `status: open`, and one evidence item whose summary is exactly `Dependency clause from source plan row for P-PH000-ST002-AC005: AC004`
  - one row-level evidence item whose summary is exactly `Source plan row for P-PH000-ST002-AC005 (status planned; raw depends_on: AC004)`
  - `aggregation_policy: null`
  - `execution_refs: []`
  - `extensions: {}`
- If `P-PH000-ST002-AC005` already exists when TK004 starts, do not create a duplicate. Update the existing row to exactly the state above.
- Do not add gate rows, task rows, or any `T105` / future-initiative activity beyond the single AC005 stub row.

### SPEC-002 - Re-derive the status narrative and Section 7 protocol from the reconciled ledger

| Field | Detail |
|:--|:--|
| Requirement Source | `guideline_workspace_implementation.md` and `guideline_workspace_notes.md` successor-handling rules |
| Target file(s) | `prompt/artifacts/tasks/P/status/status_program.md` |
| Required end-state posture | Sections 1-6 are derived from the reconciled ledger only; Section 7 explicitly distinguishes the consultant-only session-close skill from the broader role-based update protocol; explicit text states that wrap-up is not the governing reminder surface for AC004 V1 |
| Explicit non-target / do-not-change constraints | Do not mutate the ledger in this step; do not edit AGENTS surfaces or the status standard |
| Validation check | Confirm the narrative mirrors the ledger and that Section 7 names the approved session-close convention and its downstream operationalization target as the governing protocol surface |
| Blocking ambiguity rule | If the live narrative structure contradicts the requested end state, stop instead of partially merging competing guidance |
| Status | `open` |

#### Implementation Detail

- In `prompt/artifacts/tasks/P/status/status_program.md`, increment the frontmatter patch version, set `date` to `<TK004_EXECUTION_DATE>`, keep `author: LLM_Developer`, and leave `ledger_reference` unchanged.
- Re-derive Sections 1-6 directly from the post-edit ledger in `status_program.yaml`. Do not hand-edit only one table.
- In Section 1:
  - set `As Of` to `<TK004_EXECUTION_DATE>`
  - if no unrelated ledger entries changed since the current live baseline, the summary row MUST read `Total Entries | 83` and `Status Distribution | planned 52, in_progress 5, completed 26`
  - if unrelated entries changed before TK004 starts, recalculate the totals from the final ledger after only the required AC004/AC005 edits are applied
- In Section 2, ensure the `P-PH000-ST002-AC004` row shows `in_progress` with `As Of = <TK004_EXECUTION_DATE>`, and insert a new `P-PH000-ST002-AC005` row immediately after it with status `planned`.
- In Section 3, keep both `P-PH000-ST002-AC004` and `P-PH000-ST002-AC005` fully `unassessed`.
- In Section 5, ensure the evidence table includes:
  - a plan-reference row for `P-PH000-ST002-AC004` dated `<TK004_EXECUTION_DATE>` with summary `Source plan row for P-PH000-ST002-AC004 (status in_progress; raw depends_on: AC003)`
  - a decision-evidence row for `P-PH000-ST002-AC004` referencing the `GATE-002` proposal and summarizing the gate approval
  - a dependency-evidence row and a plan-reference row for `P-PH000-ST002-AC005`
- In Section 6, ensure:
  - `P-PH000-ST002-AC004` uses the action text `Continue active execution`
  - `P-PH000-ST002-AC005` uses the action text `Advance according to source plan`
  - the rationale text for `P-PH000-ST002-AC004` reflects `status in_progress` and no open upstream dependencies
  - the rationale text for `P-PH000-ST002-AC005` reflects one open upstream dependency
- In Section 7, insert one short paragraph immediately after the `7.1 Agent-Role Binding Table` that makes all of the following meaning constraints explicit:
  - `prompt/skills/session-close/SKILL.md` is a consultant-only closeout reminder surface for consultation-session ending work
  - it does not replace the Section 7 protocol
  - `LLM_Developer`, `LLM_Reviewer`, and `LLM_Consultant` remain bound by the same trigger-point rules when their work changes governed status surfaces
- In Section 7.2, add one final bullet after the numbered trigger list stating that consultant-led consultation-session closeout MAY use `prompt/skills/session-close/SKILL.md` as a reminder surface, but that reminder does not narrow the broader role binding in Section 7.1.
- Leave the `7.1 Agent-Role Binding Table` intact. Do not narrow the `Responsible` row to consultant only.
- Add a new changelog row at the top of Section 8 summarizing the TK004 operationalization update.

### SPEC-003 - Align planning and summary surfaces to the reconciled successor posture

| Field | Detail |
|:--|:--|
| Requirement Source | AC004 successor package plan and anti-drift rules in `guideline_workspace_plan.md` |
| Target file(s) | `prompt/artifacts/tasks/P/workspace/PH000/ST002/plan_P-PH000-ST002.md`; `prompt/artifacts/tasks/P/workspace/PH000/plan_P-PH000.md`; `prompt/artifacts/tasks/P/ssot/roadmap_P-PROGRAM_phase0.md` |
| Required end-state posture | ST002 stream plan, PH000 phase plan, and the phase-0 roadmap all reflect that `GATE-002` has passed, TK004 is in active execution, `GATE-003` is now the next client milestone, and AC005 remains blocked |
| Explicit non-target / do-not-change constraints | Do not change the status ledger in this step; do not create new gates; do not edit AGENTS surfaces |
| Validation check | All three summary surfaces must present the same post-GATE-002 successor posture, and no surface may still claim that `GATE-002` is pending or that TK004 is blocked awaiting approval |
| Blocking ambiguity rule | If any live summary surface still claims the old `GATE-001` approval unblocks TK004, stop and escalate rather than papering over the conflict |
| Status | `open` |

#### Implementation Detail

- In `prompt/artifacts/tasks/P/workspace/PH000/ST002/plan_P-PH000-ST002.md`:
  - increment the patch version and set `date` to `<TK004_EXECUTION_DATE>`
  - in Executive Summary `Current closure state`, replace the pre-approval paragraph with text stating that `GATE-002` passed on `<GATE_002_APPROVAL_DATE>`, `TK004` is now active, `GATE-003` is the next milestone, and AC005 remains blocked until AC004 closes
  - in the Activity Register row for `AC004`, keep status `in_progress` but change the deliverable description so it no longer says `GATE-002 readiness package`; it MUST say that the approved `GATE-002` record is historical approval evidence and that `GATE-003` is the active downstream acceptance path
  - in the Activity Register row for `AC005`, keep status `planned` and keep the post-AC004 commissioning-stub wording
  - in the later `Activity AC004` subsection, replace the `Planning Posture` sentence so it matches the same post-approval state: `GATE-002` approved, `TK004` active, `GATE-003` next, AC005 blocked
  - add a new changelog row at the top stating that TK004 began after `GATE-002` approval and that the active milestone advanced to `GATE-003`
- In `prompt/artifacts/tasks/P/workspace/PH000/plan_P-PH000.md`:
  - increment the patch version and set `date` to `<TK004_EXECUTION_DATE>`
  - in the Stream Register row for `P-PH000-ST002`, replace the current `GATE-002` pre-approval wording with text that states `GATE-002` is approved, TK004 is active, and `GATE-003` is the next client milestone
  - keep the Activity Snapshot rows for `P-PH000-ST002-AC004` and `P-PH000-ST002-AC005` as `in_progress` and `planned` respectively
  - add a new changelog row at the top reflecting the same `GATE-002 approved -> TK004 active -> GATE-003 next` transition
- In `prompt/artifacts/tasks/P/ssot/roadmap_P-PROGRAM_phase0.md`:
  - increment the patch version and set `date` to `<TK004_EXECUTION_DATE>`
  - in the `Program Status System` row of the compact delivery snapshot, replace the `active package is successor consultation GATE-002` sentence with text stating that `GATE-002` approved the successor operating model and that TK004 / `GATE-003` are now the active implementation and acceptance path
  - replace the `Next Milestone` text with `Complete AC004 TK004 and present GATE-003 acceptance package`
  - add a new changelog row at the top summarizing the shift from successor consultation approval to active implementation
- Do not change stream IDs, phase IDs, activity IDs, or unrelated initiative rows in these three files.

### SPEC-004 - Operationalize the approved session-close convention into the dedicated skill

| Field | Detail |
|:--|:--|
| Requirement Source | Session-close standards-input proposal, SES006 corrective session, and successor comparative analysis |
| Target file(s) | `prompt/skills/session-close/SKILL.md` |
| Required end-state posture | The skill matches the approved standards-input convention exactly: consultant-only closeout reminder, manual-only, no hooks/scripts, no duplication of wrap-up, and explicit pointer to `status_program.md` Section 7 as the governing protocol |
| Explicit non-target / do-not-change constraints | Do not duplicate wrap-up responsibilities; do not create repo-wide automation; do not edit `prompt/skills/wrap-up/SKILL.md` |
| Validation check | Confirm the resulting skill conforms to the approved standards-input proposal and is the only approved reminder-surface target for AC004 V1 after execution |
| Blocking ambiguity rule | If there is any divergence between the approved standards-input proposal and the live draft skill, stop and escalate rather than inferring intent from the premature historical file |
| Status | `open` |

#### Implementation Detail

- In `prompt/skills/session-close/SKILL.md`, replace the live frontmatter/body with a consultant-only session-close skill that preserves the file name and high-level purpose but makes the following end state explicit:
  - the `description` line states that the skill is for consultant-led consultation-session closeout and status-surface verification
  - the opening paragraph states that the skill is used only when the acting role is `LLM_Consultant` and the session being closed is a governed consultation session
  - the closeout checklist remains limited to:
    - checking whether `status_program.yaml`, `status_program.md`, the stream plan, the phase plan, the roadmap, or a gate-disposition surface changed
    - reconciling status surfaces if lifecycle, gate, dependency, or stale-state triggers were touched
    - using `prompt/artifacts/tasks/P/status/status_program.md` Section 7 as the governing protocol
  - add one checklist item stating that this skill is a manual reminder surface only and MUST NOT be implemented through hooks, scripts, or repo-wide automation in AC004 V1
  - keep the wrap-up skill reference, but state that `prompt/skills/wrap-up/SKILL.md` is historical-only context and not the governing AC004 reminder surface
- Preserve the `## Non-goals` section, but ensure it contains all four constraints explicitly:
  - do not duplicate wrap-up responsibilities
  - do not create hooks, scripts, or repo-wide automation
  - do not broaden this skill beyond consultant-led consultation-session closeout
  - do not broaden this skill into general session management beyond status-surface verification and reconciliation
- Do not add examples, shell commands, automation snippets, or cross-role usage guidance to this skill.

### SPEC-005 - Preserve the AC005 / future-initiative boundary

| Field | Detail |
|:--|:--|
| Requirement Source | AC004 successor gate sequencing and AC005 stub rules |
| Target file(s) | All TK004 execution surfaces in scope of this task specification |
| Required end-state posture | No `T105` or future-initiative file is created during TK004; AC005 remains blocked and untouched |
| Explicit non-target / do-not-change constraints | Do not create or open any future V2 commissioning surface during TK004 |
| Validation check | Confirm the worktree contains no new future-initiative file or path created by this task |
| Blocking ambiguity rule | If any instruction implies opening AC005 or `T105`, stop instead of expanding scope |
| Status | `open` |

#### Implementation Detail

- During TK004, create or update only the six named target files in this specification.
- Do not create any `T105`, AC005 child-plan, future-initiative, automation, or follow-on commissioning artifact as part of TK004.
- `P-PH000-ST002-AC005` MAY exist only as the single planned stub already defined in the stream and phase planning surfaces and, after TK004, in the status ledger/narrative. No additional AC005 implementation surface is allowed.
- If any instruction seems to require opening the future initiative rather than preserving the stub, stop and escalate to the consultant instead of expanding scope.

## IV. COMMISSIONABILITY GUARANTEES

- Every SPEC item in this artifact names exact target files, required end-state posture, explicit non-target constraints, validation checks, and a blocking ambiguity rule.
- `prompt/skills/wrap-up/SKILL.md` is historical-only context for AC004 and is not an optional active target.
- `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/proposal/proposal_P-PH000-ST002-AC004-TK003.8_session-close-standards-input.md` is the governing source for session-close behavior at gate time.
- `prompt/skills/session-close/SKILL.md` is the downstream operationalization target for AC004 V1.
- `prompt/skills/session-close/SKILL.md` applies only to consultant-led consultation-session closeout, while `status_program.md` Section 7 remains broader and role-based.
- If any in-scope target contradicts these instructions, the executor must stop and escalate rather than infer missing decisions.

## V. IMPLEMENTATION SEQUENCE

1. Ledger first.
2. Narrative second.
3. Planning / summary surfaces third.
4. New session-close skill fourth.
5. Dev-report handoff last.

## V.A END-OF-ARTIFACT COMMISSIONABILITY CHECKLIST

- [ ] Every target file is named exactly.
- [ ] Every required posture change is explicit.
- [ ] Every prohibited edit surface is explicit.
- [ ] The session-close skill is explicitly consultant-only, manual-only, and non-automated.
- [ ] `status_program.md` Section 7 remains broader and role-based.
- [ ] No unresolved architecture choice remains.

## VI. REFERENCES

| Document | Path |
|:--|:--|
| Governing Plan | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/plan_P-PH000-ST002-AC004.md` |
| Successor Operating-Model Analysis | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/analysis/analysis_P-PH000-ST002-AC004_successor-operating-model-and-reconciliation-policy.md` |
| Comparative Analysis | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/analysis/analysis_P-PH000-ST002-AC004_session-close-reminder-architecture-comparative-assessment.md` |
| Session-Close Standards Input | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/proposal/proposal_P-PH000-ST002-AC004-TK003.8_session-close-standards-input.md` |
| Gate-002 QA Assessment | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/analysis/analysis_P-PH000-ST002-AC004_external-review_gate-002-package-qa-assessment.md` |
| Supporting Historical Review | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/analysis/analysis_P-PH000-ST002-AC004-GATE-002_external-review.md` |
| Successor GATE-002 Proposal | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/proposal/proposal_P-PH000-ST002-AC004-GATE-002_operating-model-disposition.md` |

## VII. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.2.0 | 2026-03-26 | Amendment | Rewrote the TK004 specification to exact file-state execution detail: post-GATE-002 ledger/narrative updates, consultant-only manual session-close skill operationalization, explicit planning-surface replacements, AC005 stub preservation, and concrete validation/escalation rules. |
| v1.1.0 | 2026-03-26 | Amendment | Reframed SPEC-004 around downstream operationalization of the approved session-close standards-input proposal instead of treating the pre-existing concrete skill as gate-time authority. |
| v1.0.0 | 2026-03-25 | Initial | Authored the successor first-operationalization task specification for AC004 TK004. Replaces the historical wrap-up-based commissioning surface with the dedicated session-close skill model and makes every SPEC item developer-commissionable without inference. |
