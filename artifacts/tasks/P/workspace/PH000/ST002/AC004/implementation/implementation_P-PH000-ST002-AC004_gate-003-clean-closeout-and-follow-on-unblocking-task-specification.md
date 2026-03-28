---
artifact_type: 'IMPLEMENTATION'
implementation_type: 'task_specification'
initiative_id: 'P'
initiative_code: 'PROGRAM'
phase: '0'
stream_id: 'P-PH000-ST002'
activity_id: 'P-PH000-ST002-AC004'
task_id: 'P-PH000-ST002-AC004-TK007.2'
version: '1.0.0'
date: '2026-03-28'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/plan_P-PH000-ST002-AC004.md'
execution_audience: 'agentic_executor'
purpose: 'Exact consultant-commissioned execution contract for AC004 Gate-003 package hygiene correction, proposal/verification alignment, and explicit closeout-task registration before client disposition and downstream activity planning.'
---

# IMPLEMENTATION (Task Specification): AC004 Gate-003 Clean Closeout And Follow-On Unblocking

## I. PURPOSE & AUTHORITY
- Purpose: Specify the exact consultant-commissioned execution needed to normalize the live AC004 `GATE-003` package, register explicit AC004 closeout authority in the activity plan, and leave the package ready for client disposition without reopening the implementation slice.
- Authority chain: AC004 plan retains tracked-work authority (`P-PH000-ST002-AC004-TK007.2`) -> this artifact specifies HOW the package-hygiene and closeout-preparation edits are executed -> the `GATE-003` proposal remains the sole client decision surface.
- Audience: Designated agentic executor acting on the consultant's behalf.
- This artifact does NOT hold a GDR. Gate decisions remain exclusively in the `GATE-003` gate-disposition proposal.

## II. TASK SCOPE
- Governing plan task: `P-PH000-ST002-AC004-TK007.2`
- Trigger: The live `GATE-003` package contains known package-hygiene defects and the AC004 activity plan still lacks explicit post-gate closeout tracking, so the closeout-preparation work exceeds plan-step capacity.
- Deliverable contract: Correct the live DEV-REPORT metadata and naming defects, update the verification/proposal/external-review stack to the corrected package shape, and amend the AC004 plan so closeout authority is explicit while `GATE-003` remains the active client milestone.

## III. SPECIFICATION ITEMS

### SPEC-001 — Normalize the DEV-REPORT metadata and canonical file name

| Field | Detail |
|:--|:--|
| Requirement Source | External review finding set, verification Finding-001, and `guideline_workspace_dev-report.md` naming/traceability rules |
| Target file(s) | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/dev-report/dev-report_P-PH000-ST002-AC004_first-operationalization-slice.md` (rename to dated canonical path and update body/frontmatter in place) |
| Required end-state posture | The AC004 DEV-REPORT uses the dated canonical filename, frontmatter `source_plan` points to the AC004 activity plan, and all self-references inside the report use the renamed path |
| Explicit non-target / do-not-change constraints | Do not alter the substantive implementation evidence narrative; do not change task scope, delivered target files, or author role; do not create a second DEV-REPORT |
| Validation check | The old file no longer exists, the renamed file exists, `source_plan` resolves to the AC004 plan path, and `rg -n "dev-report_P-PH000-ST002-AC004_first-operationalization-slice" prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004` returns no stale references inside the updated DEV-REPORT |
| Blocking ambiguity rule | If the live DEV-REPORT already has multiple dated or competing canonical filenames, stop and escalate instead of picking one |
| Status | `open` |

#### Implementation Detail

- Rename `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/dev-report/dev-report_P-PH000-ST002-AC004_first-operationalization-slice.md` to `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/dev-report/dev-report_P-PH000-ST002-AC004_first-operationalization-slice_2026-03-27.md`.
- In the renamed file:
  - increment the patch version from `1.0.0` to `1.0.1`
  - keep `date: '2026-03-27'`
  - change `source_plan` to `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/plan_P-PH000-ST002-AC004.md`
  - update every in-body file reference that still points to the old DEV-REPORT path so it points to the renamed canonical path
- Preserve the existing section structure, title, evidence content, and bounded execution narrative.

### SPEC-002 — Align verification and proposal package surfaces to the corrected DEV-REPORT shape

| Field | Detail |
|:--|:--|
| Requirement Source | External review assessment, verification evidence rules, and proposal package integrity rules |
| Target file(s) | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/verification/verification_P-PH000-ST002-AC004_gate-003.md`, `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/proposal/proposal_P-PH000-ST002-AC004-GATE-003_first-operationalization-disposition.md` |
| Required end-state posture | Verification and proposal both reference the renamed DEV-REPORT path, describe the two residual package-hygiene defects accurately, and keep `APPROVE WITH CONDITIONS` / `CONDITIONAL PASS` as the live gate posture |
| Explicit non-target / do-not-change constraints | Do not record a client decision; do not recycle the gate; do not change the substantive implementation verdict; do not add new GIR items |
| Validation check | Re-read both artifacts and confirm the DEV-REPORT path is updated everywhere, the defect count is two package-hygiene defects, and both artifacts still recommend a non-recycle approval posture |
| Blocking ambiguity rule | If either artifact already records a client `APPROVE`, `APPROVE WITH CONDITIONS`, or `RECYCLE` GDR state, stop and escalate instead of overwriting the decision record |
| Status | `open` |

#### Implementation Detail

- In `verification_P-PH000-ST002-AC004_gate-003.md`:
  - increment the patch version to `1.0.1` and set `date` to `2026-03-28`
  - update the frontmatter `targets` entry and every body reference to the renamed DEV-REPORT path
  - revise the package-integrity section so the DEV-REPORT checks become: formatting `PASS`; canonical sections `PASS`; metadata/naming hygiene `FAIL`
  - replace the single finding with a package-hygiene finding that explicitly covers both:
    - broken `source_plan` pointer in the historical file state
    - non-compliant undated filename in the historical file state
  - keep the overall verdict `CONDITIONAL PASS`
  - update the conditions list so it requires carrying forward the corrected DEV-REPORT metadata and dated canonical filename together for any later refreshed evidence reuse or audit
- In `proposal_P-PH000-ST002-AC004-GATE-003_first-operationalization-disposition.md`:
  - increment the patch version to `1.0.1` and set `date` to `2026-03-28`
  - update every DEV-REPORT reference to the renamed path
  - update the verification summary and consultant conditions so the package now acknowledges both DEV-REPORT hygiene defects as one coordinated cleanup set
  - keep `Consultant Recommendation: APPROVE WITH CONDITIONS`
  - keep `Client Decision: pending`
  - keep downstream enforcement text stating AC005 remains blocked until AC004 closes

### SPEC-003 — Update the external review only as needed for the corrected package paths

| Field | Detail |
|:--|:--|
| Requirement Source | Commissioned external review preservation rule plus package-reference integrity |
| Target file(s) | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/analysis/analysis_P-PH000-ST002-AC004_external-review_gate-003-package-readiness-assessment.md` |
| Required end-state posture | The external review keeps its substantive independent assessment unchanged, but all DEV-REPORT references point to the renamed canonical path and any phrasing that implies the defects remain uncorrected is updated to historical-package wording |
| Explicit non-target / do-not-change constraints | Do not change the independent conclusion, recommendation, GIR assessments, or downstream-readiness judgment; do not add new findings that were not part of the commissioned external review |
| Validation check | `rg -n "first-operationalization-slice" ...external-review_gate-003-package-readiness-assessment.md` shows only the renamed DEV-REPORT path and historical-package wording |
| Blocking ambiguity rule | If preserving the independent review would require substantive conclusion changes, stop and escalate instead of rewriting the reviewer's judgment |
| Status | `open` |

#### Implementation Detail

- Increment the patch version to `1.0.1` and set `date` to `2026-03-28`.
- Update the frontmatter `dev_report_reference` and every in-body DEV-REPORT path to the renamed canonical path.
- Where the review currently says the defects "remain open" or are the live package's current state, revise the wording so it is historically accurate after the correction pass, for example by saying the review identified those defects in the package state it assessed and that they were non-blocking package-hygiene defects.
- Preserve the external review's original recommendation and independent posture.

### SPEC-004 — Register explicit AC004 closeout tracking in the activity plan

| Field | Detail |
|:--|:--|
| Requirement Source | `guideline_workspace_plan.md` tracked-work rules and AC004 `GATE-003` exit criteria |
| Target file(s) | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/plan_P-PH000-ST002-AC004.md` |
| Required end-state posture | The AC004 activity plan no longer ends effectively at `GATE-003`; it explicitly tracks the implementation-spec authoring, package-hygiene execution, and post-approval AC004 closeout / downstream-activation authority |
| Explicit non-target / do-not-change constraints | Do not mark AC004 `completed`; do not record a `GATE-003` client decision; do not open AC005 or AC006 inside the AC004 plan |
| Validation check | The task register contains `TK007.1`, `TK007.2`, and `TK008`; `GATE-003` depends on `TK007.2`; `TK008` depends on `GATE-003`; the gate model and detailed task text both state that AC004 closes only after the tracked closeout task completes |
| Blocking ambiguity rule | If the live AC004 plan already contains conflicting post-`GATE-003` tasks or a recorded client decision, stop and escalate instead of merging incompatible lifecycle stories |
| Status | `open` |

#### Implementation Detail

- Increment the patch version to `1.10.1` and set `date` to `2026-03-28`.
- In the Task Register:
  - insert `TK007.1` after `TK007` with status `completed`, owner `LLM_Consultant`, depends on `TK007`, target `implementation/`, reference `guideline_workspace_implementation.md`, and action summarizing authorship of this exact clean-closeout task specification
  - insert `TK007.2` after `TK007.1` with status `completed`, owner `LLM_Consultant / agentic_executor`, depends on `TK007.1`, target `dev-report/`, `verification/`, `proposal/`, `analysis/`, `implementation/`, `plan/`, reference this new implementation artifact path, and action summarizing execution of package-hygiene corrections plus explicit closeout-task registration
  - change `GATE-003` so it depends on `TK007.2` rather than `TK007`
  - add `TK008` after `GATE-003` with status `planned`, owner `LLM_Consultant`, depends on `GATE-003`, target `proposal/`, `implementation/`, `snotes/`, `notes/`, `plan/`, and reference `guideline_workspace_plan.md`; its action must say AC004 closes only after the approving `GATE-003` decision is recorded and authoritative closeout / downstream-activation updates are completed
- Update the Executive Summary, Objective, and Gate Model text only as needed so the live story becomes:
  - the corrected `GATE-003` package is now the active client-disposition surface
  - explicit post-approval closeout work remains tracked in `TK008`
  - AC005 stays blocked until `TK008` completes
- Add detailed task sections for `TK007.1`, `TK007.2`, and `TK008` using the existing plan style.

### SPEC-005 — Preserve out-of-scope execution surfaces during this closeout-preparation pass

| Field | Detail |
|:--|:--|
| Requirement Source | Consultant orchestration rule for this pass |
| Target file(s) | Protected non-target set: `prompt/artifacts/tasks/P/status/status_program.yaml`, `prompt/artifacts/tasks/P/status/status_program.md`, `prompt/artifacts/tasks/P/workspace/PH000/ST002/plan_P-PH000-ST002.md`, `prompt/artifacts/tasks/P/workspace/PH000/plan_P-PH000.md`, `prompt/artifacts/tasks/P/ssot/roadmap_P-PROGRAM_phase0.md`, `prompt/skills/session-close/SKILL.md`, all AC005/AC006 paths |
| Required end-state posture | None of the protected surfaces are modified during this execution pass |
| Explicit non-target / do-not-change constraints | Treat all protected surfaces as read-only for this task specification |
| Validation check | Review the changed-file list and confirm only the named in-scope AC004 files plus this implementation artifact appear |
| Blocking ambiguity rule | If any protected surface seems to require mutation to finish this pass, stop and escalate instead of widening scope |
| Status | `open` |

#### Implementation Detail

- This pass is limited to live `GATE-003` package hygiene and explicit AC004 closeout tracking.
- Do not update status ledger/narrative surfaces, stream/phase plans, roadmap, session-close skill, or any future-initiative planning surface.
- Do not create `AC005`, `AC006`, `comm_`, `T105`, or other follow-on artifacts in this execution pass.

## IV. IMPLEMENTATION SEQUENCE
1. Read the current AC004 DEV-REPORT, verification, proposal, external review, and activity plan in full.
2. Execute `SPEC-001` so the DEV-REPORT path and metadata are canonical first.
3. Execute `SPEC-002` so verification and proposal align to the corrected DEV-REPORT shape.
4. Execute `SPEC-003` to preserve the commissioned external review while updating package references.
5. Execute `SPEC-004` to register the explicit closeout-task stack in the AC004 plan.
6. Run the validation checks for all SPEC items.
7. Return a concise execution summary listing the exact changed files and any unresolved ambiguities.

## V. REFERENCES

| Document | Path |
|:--|:--|
| Governing Plan | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/plan_P-PH000-ST002-AC004.md` |
| GATE-003 Proposal | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/proposal/proposal_P-PH000-ST002-AC004-GATE-003_first-operationalization-disposition.md` |
| GATE-003 Verification | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/verification/verification_P-PH000-ST002-AC004_gate-003.md` |
| Commissioned External Review | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/analysis/analysis_P-PH000-ST002-AC004_external-review_gate-003-package-readiness-assessment.md` |
| Live DEV-REPORT (historical pre-fix path) | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/dev-report/dev-report_P-PH000-ST002-AC004_first-operationalization-slice.md` |
| DEV-REPORT Guideline | `prompt/templates/consultant/workspace/guideline_workspace_dev-report.md` |
| Implementation Guideline | `prompt/templates/consultant/workspace/guideline_workspace_implementation.md` |
| Plan Guideline | `prompt/templates/consultant/workspace/guideline_workspace_plan.md` |

## VI. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-03-28 | Initial | Authored the exact agentic execution contract for AC004 `GATE-003` package hygiene correction, proposal/verification alignment, commissioned external-review path normalization, and explicit post-gate closeout tracking before downstream activity planning. |
