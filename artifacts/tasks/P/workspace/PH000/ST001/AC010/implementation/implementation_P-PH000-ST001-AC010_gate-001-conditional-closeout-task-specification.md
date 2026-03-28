---
artifact_type: 'IMPLEMENTATION'
implementation_type: 'task_specification'
initiative_id: 'P'
initiative_code: 'PROGRAM'
phase: '0'
stream_id: 'P-PH000-ST001'
activity_id: 'P-PH000-ST001-AC010'
task_id: 'P-PH000-ST001-AC010-TK007.1'
version: '1.0.0'
date: '2026-03-28'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST001/AC010/plan_P-PH000-ST001-AC010.md'
execution_audience: 'consultant'
purpose: 'Exact consultant-owned execution contract for AC010 GATE-001 conditional closeout after the commissioned external review, without creating SES002 in this session.'
---

# IMPLEMENTATION (Task Specification): AC010 GATE-001 Conditional Closeout

## I. PURPOSE & AUTHORITY

- Purpose: Specify the exact consultant-owned package-surface execution required to close `P-PH000-ST001-AC010-GATE-001` on the `APPROVE WITH CONDITIONS` path after the commissioned external review identified the remaining governance-integrity drift.
- Authority chain: The AC010 plan retains tracked-work authority through `P-PH000-ST001-AC010-TK007.1` -> this artifact specifies HOW the bounded closeout edits are executed -> the Gate-001 proposal GDR remains the sole authoritative decision record.
- Audience: `LLM_Consultant` as the governing execution owner and the designated consultant-commissioned assistant as the bounded mutation executor for this closeout slice.
- Boundary: This artifact does NOT hold a GDR. Gate decisions remain exclusively in `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC010/proposal/proposal_P-PH000-ST001-AC010_gate-001_cross-standard-retrofit-disposition.md`.
- Deferred-notes rule: `SES002` and all notes-register work are explicitly out of scope for this session. This artifact MUST close the gate without creating or editing any `snotes_` or `notes_` file.

## II. TASK SCOPE

- Governing plan task: `P-PH000-ST001-AC010-TK007.1`
- Trigger: The commissioned external review concluded that the retrofit package is substantively sound but that the proposal and live planning surfaces overstate a clean unconditional approval because `TK006` is framed as reviewer-owned while the verification artifact is consultant-authored.
- Deliverable contract:
  - Updated `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC010/proposal/proposal_P-PH000-ST001-AC010_gate-001_cross-standard-retrofit-disposition.md`
  - Updated `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC010/plan_P-PH000-ST001-AC010.md`
  - Updated `prompt/artifacts/tasks/P/workspace/PH000/ST001/plan_P-PH000-ST001.md`

**Explicit non-target surfaces**
- Do NOT create `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC010/snotes/snotes_P-PH000-ST001-AC010-SES002.md`
- Do NOT edit `prompt/artifacts/tasks/P/workspace/PH000/ST001/notes_P-PH000-ST001.md`
- Do NOT edit `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC010/snotes/snotes_P-PH000-ST001-AC010-SES001.md`
- Do NOT edit `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC010/verification/verification_P-PH000-ST001-AC010_gate-001.md`
- Do NOT edit `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC010/analysis/analysis_P-PH000-ST001-AC010_external-review-gate-001-package.md`
- Do NOT edit `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC010/analysis/analysis_P-PH000-ST001-AC010-TK000_execution-readiness-assessment.md`
- Do NOT edit `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC010/dev-report/dev-report_P-PH000-ST001-AC010_cross-standard-retrofit.md`
- Do NOT edit `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC010/implementation/implementation_P-PH000-ST001-AC010_cross-standard-metadata-retrofit-task-specification.md`
- Do NOT edit `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md`
- Do NOT edit `prompt/artifacts/tasks/P/standard/standard_P-STD-002_program-status-standard.md`
- Do NOT edit `prompt/artifacts/tasks/P/standard/changelog/changelog_standard_P-STD-002.md`
- Do NOT edit `prompt/artifacts/tasks/P/standard/standard_P-STD-004_file-naming-and-directory-convention.md`
- Do NOT edit `prompt/artifacts/tasks/P/standard/standard_P-STD-005_universal-id-specification.md`

## II.A FIXED EXECUTION TOKENS

- Gate decision date for this closeout is `2026-03-28`.
- Every file mutated under this artifact MUST use `2026-03-28` as its updated `date` field or changelog date.
- Where this artifact says "increment patch version", increase only the patch component of the live semantic version already present in the target file.
- The external-review artifact path is fixed and MUST be:
  - `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC010/analysis/analysis_P-PH000-ST001-AC010_external-review-gate-001-package.md`
- Because `SES002` is deferred, the Gate Decision Record MUST use this exact `Decision Reference` text:
  - `Inline client approval recorded in this GDR during the SES002-deferred closeout session.`

## II.B PREFLIGHT RULE

- Before editing any file, read every in-scope target named in this specification.
- Current repo state wins over stale assumptions, but only within the approved `APPROVE WITH CONDITIONS` closeout boundary defined here.
- If a target already satisfies the required end state, leave it unchanged and report it as verified.
- If a target partially satisfies the required end state, merge only the missing required deltas.
- If any target would require editing a protected non-target surface to complete the closeout, stop and escalate instead of expanding scope.

## III. SPECIFICATION ITEMS

### SPEC-001 — Update the Gate-001 proposal to the conditional-close posture

| Field | Detail |
|:--|:--|
| Requirement Source | Commissioned external review `GAP-001` and `GAP-002`; AC010 closeout direction approved for this session |
| Target file(s) | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC010/proposal/proposal_P-PH000-ST001-AC010_gate-001_cross-standard-retrofit-disposition.md` |
| Required end-state posture | The proposal records the external review as part of the gate package, recommends `APPROVE WITH CONDITIONS`, and contains a fully populated GDR that closes the gate without using `SES002` |
| Explicit non-target / do-not-change constraints | Do not create a second GIR; do not convert the package to `RECYCLE`; do not change the verification artifact; do not invent a notes-based decision reference |
| Validation check | Re-read frontmatter, Gate Package, `GIR-001`, Section V, and the GDR to confirm they all tell the same `APPROVE WITH CONDITIONS` story |
| Blocking ambiguity rule | If any live proposal text would require reopening the substantive retrofit evidence rather than correcting package posture, stop and escalate |
| Status | `open` |

#### Implementation Detail

1. In frontmatter:
   - increment the patch version from the live version
   - set `date: '2026-03-28'`
   - keep `status: 'draft'`
   - add:
     - `external_review_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST001/AC010/analysis/analysis_P-PH000-ST001-AC010_external-review-gate-001-package.md'`
2. In `## II. GATE PACKAGE`:
   - add a new Gate Package Index row immediately after the verification row:
     - Deliverable: `AC010 external review`
     - Producing Task: `TK007.1`
     - Status: `completed`
     - Acceptance: `accepted-provisional`
     - Client Priority: `Required`
     - Path: `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC010/analysis/analysis_P-PH000-ST001-AC010_external-review-gate-001-package.md`
   - add a matching Evidence Index row:
     - Evidence Type: `External Review`
     - Artifact: `AC010 gate package second-opinion review`
     - Path: `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC010/analysis/analysis_P-PH000-ST001-AC010_external-review-gate-001-package.md`
     - Notes: `Independent second-opinion review supporting the conditional-close posture`
3. In `## III. DISPOSITION SUMMARY REGISTER`, change the `GIR-001` Recommended Option cell to:
   - `(a) Approve with conditions: accept the retrofit package and close GATE-001 with the verification-ownership exception recorded explicitly`
4. In `## IV. DETAILED DISPOSITION REGISTER` under `GIR-001`:
   - replace the option table with:
     - `**(a) Approve With Conditions** | Accept the retrofit package as complete for the current scope and close GATE-001 while explicitly accepting the verification-ownership exception.`
     - `(b) Recycle | Reject gate closure and return the package for additional remediation despite the substantive package sufficiency.`
   - set `Recommendation:` to `(a)`
   - replace the rationale paragraph so it says the substantive retrofit package is acceptable, but the approval is conditioned on accepting the `TK006` verification-ownership drift identified by the external review
   - replace `Client Decision:` with:
     - `[x] (a)` / `[ ] (b)` / `[ ] Override: _______`
5. In `## V. CONSULTANT GATE RECOMMENDATION`:
   - change `Consultant recommendation:` to `APPROVE WITH CONDITIONS`
   - keep the reviewer verdict reference as `PASS`
   - change `Alignment:` from `Aligned` to `Partially aligned`
   - replace `Conditions and/or deferrals:` with exactly:
     - `Accepted verification-ownership exception: TK006 verification evidence is accepted for this gate even though the artifact was consultant-authored while the gate package framed TK006 as reviewer-owned. No further developer rework is required.`
   - replace the downstream enforcement bullets so they say:
     - the client decision is now recorded in the GDR below
     - AC010 is closed for current scope on the `APPROVE WITH CONDITIONS` path
     - no further AC010 implementation work is authorized under this gate closeout slice
6. In `## VI. GATE DECISION RECORD (GDR)` update the table to exactly:

| Field | Value |
|:--|:--|
| Gate ID | `P-PH000-ST001-AC010-GATE-001` |
| Consultant Recommendation | `APPROVE WITH CONDITIONS` |
| Client Decision | `APPROVE WITH CONDITIONS` |
| Gate Status After Decision | `completed` |
| Conditions (if any) | `Accepted verification-ownership exception: TK006 verification evidence is accepted for this gate even though the artifact was consultant-authored while the gate package framed TK006 as reviewer-owned; no further developer rework required.` |
| Decided By | `Client` |
| Decision Date | `2026-03-28` |
| Decision Reference | `Inline client approval recorded in this GDR during the SES002-deferred closeout session.` |

7. Replace the prose below the GDR so it no longer describes the gate as pending. It MUST say that:
   - the consultant recommendation is the consolidated advisory signal
   - the client decision has now been recorded
   - the closeout used the SES002-deferred inline decision-reference path approved for this session
8. In `## VII. REFERENCES`, add:
   - `| External Review | prompt/artifacts/tasks/P/workspace/PH000/ST001/AC010/analysis/analysis_P-PH000-ST001-AC010_external-review-gate-001-package.md |`
9. In `## VIII. CHANGELOG`, add a new top-row entry stating that:
   - the external review was indexed into the gate package
   - the consultant recommendation and GDR were updated to `APPROVE WITH CONDITIONS`
   - the gate was closed using the SES002-deferred inline-decision-reference path

### SPEC-002 — Update the AC010 activity plan to reflect conditional gate closure

| Field | Detail |
|:--|:--|
| Requirement Source | Governing plan closeout path for `TK007.1`; proposal GDR closure under `SPEC-001` |
| Target file(s) | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC010/plan_P-PH000-ST001-AC010.md` |
| Required end-state posture | `TK007.1` is `completed`, `GATE-001` is `completed`, `TK007` no longer implies a pending GDR, and the changelog records the conditional-close amendment |
| Explicit non-target / do-not-change constraints | Do not reopen `TK001` through `TK006`; do not add `SES002`; do not change the implementation history of the retrofit tasks |
| Validation check | `rg -n "TK007\\.1|GATE-001|pending client decision|APPROVE WITH CONDITIONS" .../plan_P-PH000-ST001-AC010.md` shows the final closeout posture and no stale pending wording |
| Blocking ambiguity rule | If the plan would need a new activity, new gate, or new remediation task to represent this closeout, stop and escalate rather than expanding the lifecycle model |
| Status | `open` |

#### Implementation Detail

1. In frontmatter:
   - increment the patch version from the live version
   - set `date: '2026-03-28'`
2. In the Task Register:
   - keep `TK007` `completed`, but replace its `Action` text with:
     - `Authored the baseline GATE-001 disposition package; the final conditional-close posture and recorded client decision were completed under TK007.1.`
   - change `TK007.1` from `in_progress` to `completed`
   - set the `TK007.1` `Action` text to:
     - `Executed the consultant-owned conditional-closeout alignment after external review, updated the proposal/GDR and planning surfaces, and preserved the deferred SES002 notes boundary.`
   - change `GATE-001` from `in_progress` to `completed`
   - set the `GATE-001` `Action` text to:
     - `Closed as APPROVE WITH CONDITIONS on 2026-03-28. The accepted condition is the TK006 verification-ownership exception; no further developer rework was required.`
3. In `### Task TK007`, replace the `Outcome` paragraph with:
   - `Completed. The baseline GATE-001 disposition package was authored under TK007. Final conditional-closeout alignment and the recorded client decision were completed under TK007.1.`
4. In `### Task TK007.1`, replace the `Outcome` paragraph with:
   - `Completed. The consultant-owned conditional-closeout alignment updated the proposal, closed the gate on the APPROVE WITH CONDITIONS path, and reconciled the live plan surfaces without creating SES002 in this session.`
   - change all four success-criteria checkboxes to `[x]`
5. In `### GATE-001`:
   - keep the same entry criteria plus `TK007.1`
   - keep the same reviewer
   - replace the exit criteria bullets with:
     - `Client records APPROVE WITH CONDITIONS in the GATE-001 GDR`
     - `The accepted condition explicitly captures the TK006 verification-ownership exception`
     - `All P-STD standards remain structurally conformant to P-STD-001 metadata governance`
   - add one sentence after the Gate-Disposition Proposal line:
     - `This gate is now closed on the APPROVE WITH CONDITIONS path recorded in the proposal GDR dated 2026-03-28.`
6. In `## IV. DEPENDENCY NOTES`, replace `TK001 through TK007.1` text if needed so it states the activity is now closed for current scope rather than still commissioned/in progress.
7. In `## V. CHANGELOG`, add a new top-row entry summarizing:
   - `TK007.1` completed
   - `GATE-001` closed as `APPROVE WITH CONDITIONS`
   - the SES002-deferred inline-decision-reference path was used for this session

### SPEC-003 — Update the ST001 stream plan so AC010 is fully closed

| Field | Detail |
|:--|:--|
| Requirement Source | AC010 closeout state after `SPEC-001` and `SPEC-002` |
| Target file(s) | `prompt/artifacts/tasks/P/workspace/PH000/ST001/plan_P-PH000-ST001.md` |
| Required end-state posture | The AC010 activity row is `completed`, the deliverable summary is past-tense and gate-package oriented, and the activity stub no longer says execution remains deferred |
| Explicit non-target / do-not-change constraints | Do not alter AC009; do not introduce new P-STD-001 work; do not touch any other activity unless required for AC010 state consistency |
| Validation check | `rg -n "AC010|deferred|APPROVE WITH CONDITIONS|completed" .../plan_P-PH000-ST001.md` confirms the final AC010 posture |
| Blocking ambiguity rule | If closing AC010 would require simultaneous edits to unrelated stream activities, stop and escalate rather than broadening the scope |
| Status | `open` |

#### Implementation Detail

1. In frontmatter:
   - increment the patch version from the live version
   - set `date: '2026-03-28'`
2. In the Activity Register AC010 row:
   - change `Status` from `in_progress` to `completed`
   - replace the Deliverable summary with:
     - `Consultant-owned commissioning package (`TK000`) + completed cross-standard metadata retrofit package + Gate-001 closed as APPROVE WITH CONDITIONS`
3. In the `#### Activity AC010` contract stub:
   - keep the existing activity plan link
   - replace any future-tense or deferred execution wording in Scope / dependency notes / summary bullets with wording that says:
     - consultant-owned commissioning work is complete
     - downstream retrofit execution is complete
     - Gate-001 is closed as `APPROVE WITH CONDITIONS`
     - no further AC010 work is active in the current scope
4. In the dependency note section near the AC009/AC010 summary, replace the sentence:
   - `Consultant-owned commissioning work is now complete under TK000; downstream execution remains deferred to a later session.`
   - with:
   - `Consultant-owned commissioning, downstream retrofit execution, and Gate-001 closeout are now complete for AC010; the activity is closed for current scope.`
5. In `## V. CHANGELOG`, add a new top-row entry stating that:
   - AC010 is now `completed`
   - the stream summary reflects Gate-001 closure as `APPROVE WITH CONDITIONS`
   - evidence source is the AC010 plan closeout amendment and Gate-001 proposal GDR

### SPEC-004 — Preserve the deferred-notes boundary

| Field | Detail |
|:--|:--|
| Requirement Source | Client instruction for this session; `guideline_workspace_notes.md` deferral boundary |
| Target file(s) | All AC010 `snotes/` and stream/activity notes registers |
| Required end-state posture | No notes file or notes register is changed in this execution slice |
| Explicit non-target / do-not-change constraints | Do not create `SES002`; do not backfill its intent into `SES001`; do not change `notes_P-PH000-ST001.md` |
| Validation check | Changed-file list contains no path matching `/snotes/` and no `notes_*.md` file |
| Blocking ambiguity rule | If any closeout step seems to require a notes artifact to remain valid, stop and escalate rather than breaking the approved deferral boundary |
| Status | `open` |

#### Implementation Detail

This is a hard boundary. The assistant may cite the deferred-notes rule in its summary, but it must not solve the absence of `SES002` by creating any surrogate notes artifact.

### SPEC-005 — Preserve all substantive evidence surfaces

| Field | Detail |
|:--|:--|
| Requirement Source | Commissioned external review posture and consultant closeout boundary for this session |
| Target file(s) | Protected non-target set listed in Section II |
| Required end-state posture | The retrofit evidence and standards remain unchanged during this closeout |
| Explicit non-target / do-not-change constraints | Treat verification, analysis, dev-report, and all standard artifacts as read-only evidence surfaces |
| Validation check | Review the changed-file list and confirm that no protected non-target path appears |
| Blocking ambiguity rule | If any protected file appears necessary to edit for closeout, stop and escalate instead of mutating it |
| Status | `open` |

#### Implementation Detail

This pass is package closeout only. The assistant must not reopen the implementation-backed evidence or the standard-side outputs.

## IV. IMPLEMENTATION SEQUENCE

1. Read this implementation artifact in full before editing any target.
2. Update the Gate-001 proposal per `SPEC-001`.
3. Update the AC010 activity plan per `SPEC-002`.
4. Update the ST001 stream plan per `SPEC-003`.
5. Run validation checks for `SPEC-001` through `SPEC-005`, including `git -C prompt diff --check --` on the touched files.
6. Return a concise execution summary containing:
   - the exact changed-file list
   - whether any target was already compliant and left unchanged
   - the validation results

## V. REFERENCES

| Document | Path |
|:--|:--|
| Governing Plan | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC010/plan_P-PH000-ST001-AC010.md` |
| Gate-001 Proposal | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC010/proposal/proposal_P-PH000-ST001-AC010_gate-001_cross-standard-retrofit-disposition.md` |
| Commissioned External Review | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC010/analysis/analysis_P-PH000-ST001-AC010_external-review-gate-001-package.md` |
| Gate-001 Verification | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC010/verification/verification_P-PH000-ST001-AC010_gate-001.md` |
| AC010 Readiness Assessment | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC010/analysis/analysis_P-PH000-ST001-AC010-TK000_execution-readiness-assessment.md` |
| ST001 Stream Plan | `prompt/artifacts/tasks/P/workspace/PH000/ST001/plan_P-PH000-ST001.md` |

## VI. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-03-28 | Initial | Authored the exact consultant-owned execution contract for AC010 GATE-001 conditional closeout after the commissioned external review. Covers proposal/GDR alignment, AC010 and ST001 plan closure, preserved substantive evidence surfaces, and the explicit no-SES002 boundary for this session. |
