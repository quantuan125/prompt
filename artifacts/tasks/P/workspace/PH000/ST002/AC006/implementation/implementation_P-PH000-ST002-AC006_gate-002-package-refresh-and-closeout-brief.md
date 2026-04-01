---
artifact_type: 'IMPLEMENTATION'
implementation_type: 'task_specification'
initiative_id: 'P'
initiative_code: 'PROGRAM'
phase: '0'
stream_id: 'P-PH000-ST002'
activity_id: 'P-PH000-ST002-AC006'
task_id: 'P-PH000-ST002-AC006-TK012.2'
version: '1.0.0'
date: '2026-04-01'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/plan_P-PH000-ST002-AC006.md'
execution_audience: 'assistant'
purpose: 'Bounded assistant-execution brief for the implicit TK012.2 closeout pass that refreshes the AC006 GATE-002 plan/proposal package before client disposition.'
---

# IMPLEMENTATION (Task Specification): AC006 GATE-002 Package Refresh And Closeout Brief

## I. PURPOSE & AUTHORITY

- Purpose: Specify the exact assistant-executed package-refresh work allowed inside implicit `TK012.2` scope after the external review and consultant assessment are complete.
- Authority chain: the AC006 plan defines `TK012.2` as the final consultant refresh lane -> the external review identifies the remaining package-state gaps -> the consultant assessment confirms those gaps should be closed without reopening implementation -> this brief defines HOW the assistant performs the bounded closeout pass.
- Audience: `LLM_Assistant`
- This artifact does NOT hold a GDR. It exists only to commission bounded assistant closeout work before the client reads the final package.
- The assistant must not widen scope beyond plan/proposal package refresh and closeout housekeeping.

## II. TASK SCOPE

- Governing plan task: `P-PH000-ST002-AC006-TK012.2`
- Trigger: the implementation package has passed `TK011`, the external review (`TK012.1`) is complete, and the consultant assessment has confirmed that only package-state normalization remains.
- Deliverable contract:
  - refreshed `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/proposal/proposal_P-PH000-ST002-AC006-GATE-002_execution-evidence-disposition.md`
  - refreshed `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/plan_P-PH000-ST002-AC006.md`
  - no changes to implementation deliverables, DEV-REPORTs, verification artifacts, or analysis bodies

## III. SPECIFICATION ITEMS

### SPEC-001 - Refresh the GATE-002 proposal into the final client reading set

| Field | Detail |
|:--|:--|
| Requirement Source | TK012.1 external review; TK012.2 consultant assessment; `guideline_workspace_proposal.md` |
| Target file(s) | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/proposal/proposal_P-PH000-ST002-AC006-GATE-002_execution-evidence-disposition.md` |
| Required end-state posture | The proposal reflects the post-review state and is the final client reading set for GATE-002. |
| Explicit non-target / do-not-change constraints | Do NOT record a client decision. Do NOT change GIR substance unless required to reflect existing evidence more accurately. Do NOT change implementation scope. |
| Validation check | Gate Package Index and Evidence Index both include the authoritative external review and consultant assessment; GDR remains `Client Decision: pending`. |
| Blocking ambiguity rule | If the proposal can only be refreshed by inventing a new GIR or changing the implementation boundary, stop and escalate. |
| Status | `open` |

#### Implementation Detail

1. Update the proposal frontmatter to add:
   - `analysis_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/analysis/analysis_P-PH000-ST002-AC006-GATE-002_external-review-and-downstream-readiness-assessment.md'`
   - `external_review_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/analysis/analysis_P-PH000-ST002-AC006-GATE-002_external-review.md'`
2. Refresh the Executive Summary so it states that the package now includes `TK012.1` and `TK012.2`.
3. Add the external review and consultant assessment to the Gate Package Index with appropriate client priority.
4. Add the same artifacts to the Evidence Index and designate the external review as the authoritative external review for this gate package.
5. Update Section V so the consultant recommendation reflects the post-review state:
   - recommendation should remain aligned to the current evidence
   - explicitly reference the verifier verdict from `TK011`
   - explicitly note whether the consultant assessment agrees with the external review
6. Keep the GDR in pending posture:
   - `Client Decision: pending`
   - `Gate Status After Decision: pending`
   - `Decision Date: —`
   - `Decision Reference: pending`

### SPEC-002 - Normalize the AC006 plan to the current execution state

| Field | Detail |
|:--|:--|
| Requirement Source | TK012.1 GAP-001 and GAP-002; TK012.2 consultant assessment; `guideline_workspace_plan.md` |
| Target file(s) | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/plan_P-PH000-ST002-AC006.md` |
| Required end-state posture | The task register and detailed sections reflect the live state through TK012.2 package readiness without recording a client GATE-002 decision. |
| Explicit non-target / do-not-change constraints | Do NOT add new task rows. Do NOT alter completed GATE-001 history. Do NOT mark GATE-002 as completed. |
| Validation check | TK007-TK012.2 rows reflect the current state with concise action trails; detailed `TK010.1` dependency text matches the task-register row. |
| Blocking ambiguity rule | If mojibake or formatting drift prevents a safe localized edit, patch only the exact affected rows/fields and do not rewrite unrelated sections. |
| Status | `open` |

#### Implementation Detail

1. Update task-register rows for:
   - `TK007`, `TK008`, `TK009`, `TK010`, `TK010.1`, `TK011`, `TK012`, `TK012.1`, `TK012.2`
2. Use status values that match the actual current state:
   - completed for tasks whose artifacts now exist
   - keep `GATE-002` pending
3. Replace placeholder action text on those rows with concise evidence-bearing outcomes.
4. In the detailed `TK010.1` section, replace `Depends On: TK010.1` with `Depends On: TK009, TK010`.
5. Update any detailed task sections whose deliverable text or posture must reflect the now-completed artifacts, but keep edits tightly localized.

### SPEC-003 - Validate final package integrity after refresh

| Field | Detail |
|:--|:--|
| Requirement Source | TK012.1/TK012.2 package-refresh posture |
| Target file(s) | proposal + plan refreshed above |
| Required end-state posture | The plan and proposal describe the same current gate-readiness state and the final reading set is internally consistent. |
| Explicit non-target / do-not-change constraints | Do NOT rerun implementation work. Do NOT modify DEV-REPORT, VERIFICATION, or ANALYSIS bodies. |
| Validation check | Cross-check proposal references, plan task states, and GDR pending posture. |
| Blocking ambiguity rule | If a mismatch cannot be resolved without changing previously-authored evidence bodies, stop and escalate. |
| Status | `open` |

#### Implementation Detail

1. Re-read the refreshed proposal and plan top to bottom.
2. Confirm:
   - proposal indexes include `TK012.1` and `TK012.2`
   - proposal references point to real files
   - task-register states for `TK007` through `TK012.2` match the live artifact state
   - `GATE-002` remains pending
3. Run a targeted `git diff --check` over the refreshed proposal and plan.
4. If validation fails, fix only the specific inconsistency and rerun the validation check.

## IV. IMPLEMENTATION SEQUENCE

1. Refresh the proposal.
2. Normalize the plan.
3. Run the final package-integrity validation.
4. Hand the refreshed package back to the consultant for final review and client presentation.

## V. REFERENCES

| Document | Path |
|:--|:--|
| Governing Plan | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/plan_P-PH000-ST002-AC006.md` |
| External Review | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/analysis/analysis_P-PH000-ST002-AC006-GATE-002_external-review.md` |
| Consultant Assessment | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/analysis/analysis_P-PH000-ST002-AC006-GATE-002_external-review-and-downstream-readiness-assessment.md` |
| Gate Proposal | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/proposal/proposal_P-PH000-ST002-AC006-GATE-002_execution-evidence-disposition.md` |

## VI. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-04-01 | Initial | Authored the bounded assistant-closeout brief for the implicit TK012.2 package-refresh pass covering proposal refresh, plan normalization, and final package-integrity validation before client disposition. |
