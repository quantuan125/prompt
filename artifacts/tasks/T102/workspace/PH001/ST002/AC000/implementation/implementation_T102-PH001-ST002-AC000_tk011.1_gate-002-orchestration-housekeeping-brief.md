---
artifact_type: 'IMPLEMENTATION'
implementation_type: 'task_specification'
initiative_id: 'T102'
initiative_code: 'CWD'
phase: '1'
stream_id: 'T102-PH001-ST002'
activity_id: 'T102-PH001-ST002-AC000'
task_id: 'T102-PH001-ST002-AC000-TK011.1'
version: '1.0.0'
date: '2026-04-02'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/plan_T102-PH001-ST002-AC000.md'
execution_audience: 'assistant'
purpose: 'Bounded assistant-execution brief for the pre-TK011 orchestration housekeeping pass that amends recycle-lineage governance and aligns AC000 GATE-002 plan posture before developer execution starts.'
---

# IMPLEMENTATION (Task Specification): AC000 TK011.1 GATE-002 Orchestration Housekeeping Brief

## I. PURPOSE & AUTHORITY

- Purpose: Define the exact assistant-executed housekeeping work required before the AC000 implementation-backed `GATE-002` path begins so the recycle-lineage model, reviewer ownership, and gate package sequencing are encoded consistently.
- Authority chain: AC000 plan authorizes the `TK011`-`TK015` gate path -> the consultant determined that pre-execution orchestration hardening is required -> this brief specifies HOW the assistant performs the bounded governance and plan refresh pass -> the consultant reviews the output before commissioning the developer lane.
- Audience: `LLM_Assistant`
- Filename note: this is a consultant/assistant orchestration brief under `task_specification` with `execution_audience: 'assistant'`.
- This artifact does NOT hold a GDR. It exists only to commission bounded housekeeping updates before implementation starts.
- If any mismatch requires changing substantive AC000 implementation scope, the assistant MUST stop and escalate.

## II. TASK SCOPE

- Governing plan task: `T102-PH001-ST002-AC000-TK011.1`
- Trigger: the consultant has approved a recycle-lineage package model for implementation-backed gates and needs the governing rules plus AC000 plan posture aligned before `TK011` is commissioned to a developer worker.
- Deliverable contract:
  - refreshed workspace governance surfaces for recycle-lineage handling
  - refreshed AC000 activity plan reflecting the GATE-002 orchestration posture
  - no implementation execution, no DEV-REPORT authoring, no VERIFICATION authoring, and no proposal refresh

## III. SPECIFICATION ITEMS

### SPEC-001 - Amend workspace documentation rules for recycle-lineage package accumulation

| Field | Detail |
|:--|:--|
| Requirement Source | Consultant-approved GATE-002 orchestration update |
| Target file(s) | `prompt/templates/consultant/workspace/workspace_documentation_rules.md`; `prompt/templates/consultant/workspace/changelog/changelog_workspace_documentation_rules.md` |
| Required end-state posture | The canonical workflow chain and recyclable-loop evidence rules require new cycle-local DEV-REPORT and VERIFICATION artifacts for each same-gate recycle cycle, while preserving one primary gate-facing artifact per family. |
| Explicit non-target / do-not-change constraints | Do NOT change unrelated artifact families, ownership matrix entries unrelated to recycle handling, or supersession rules. |
| Validation check | `§7.A` and `§7.D` explicitly state that recycle cycles create supplementary `DEV-REPORT` and supplementary `VERIFICATION` artifacts; the old “version-bumped re-assessment as the only posture” wording is removed; changelog has a new entry. |
| Blocking ambiguity rule | If the update would require changing the fundamental same-gate identity rule, stop and escalate. Gate identity must remain unchanged. |
| Status | `open` |

#### Implementation Detail

1. In `workspace_documentation_rules.md` `§7.A Canonical Workflow Chain`, replace the implementation-backed recycle branch so it reads as a package-accumulation loop:
   - `... -> DEV-REPORT (primary) -> VERIFICATION (primary) -> [IMPLEMENTATION remediation_specification where RECYCLE] -> remediation deliverables -> DEV-REPORT (supplementary recycle cycle) -> VERIFICATION (supplementary recycle cycle) -> primary package refresh -> PROPOSAL ...`
2. In `§7.D Recyclable-Loop Evidence Accumulation and Handoff`, replace the current lineage rule that says VERIFICATION re-assessment is version-bumped rather than renamed.
3. Insert explicit lineage rules:
   - each recycle cycle creates a new supplementary `DEV-REPORT`
   - each recycle cycle creates a new supplementary `VERIFICATION`
   - the primary artifacts remain the gate-facing entry points
   - primary artifacts may be refreshed only to index, summarize, and link the new cycle artifacts
   - recycle-cycle evidence MUST NOT be overwritten or collapsed into a replacement artifact
4. Add one changelog row for the new version bump in `changelog_workspace_documentation_rules.md`.

### SPEC-002 - Amend DEV-REPORT guidance for recycle-cycle supplementary evidence

| Field | Detail |
|:--|:--|
| Requirement Source | Consultant-approved recycle-lineage package model |
| Target file(s) | `prompt/templates/consultant/workspace/guideline_workspace_dev-report.md`; `prompt/templates/consultant/workspace/changelog/changelog_guideline_workspace_dev-report.md` |
| Required end-state posture | DEV-REPORT guidance treats same-gate recycle as a new bounded evidence slice that requires a supplementary report rather than a version bump of the prior cycle report. |
| Explicit non-target / do-not-change constraints | Do NOT change the author role, core required sections, or non-recycle single-report posture. |
| Validation check | `§III.D`, `§III.E`, and `§VIII.E` all encode the recycle supplementary-report rule consistently; changelog has a new entry. |
| Blocking ambiguity rule | If the change would break the primary/supplementary taxonomy, stop and escalate. The package taxonomy must remain the linkage model. |
| Status | `open` |

#### Implementation Detail

1. In `§III.D DEV-REPORT Package Taxonomy`, add a sentence that same-gate recycle remediation slices are bounded evidence segments and SHOULD be represented as supplementary DEV-REPORT artifacts beneath one primary gate-facing report.
2. In `§III.E Scope Decomposition vs Temporal Iteration`, change the rule so recycle remediation is not treated as ordinary temporal correction of the same report.
3. State explicitly:
   - version bumps are for corrections to the same report artifact
   - new recycle cycles produce new supplementary reports
4. In `§VIII.E Multi-report package linkage`, add recommended recycle frontmatter keys:
   - `recycle_gate_id`
   - `recycle_iteration`
   - `cycle_scope`
5. Keep `package_role`, `primary_report`, and `consolidated_from` unchanged as the required linkage model.
6. Add one changelog row in `changelog_guideline_workspace_dev-report.md`.

### SPEC-003 - Amend VERIFICATION guidance for same-gate supplementary re-assessment artifacts

| Field | Detail |
|:--|:--|
| Requirement Source | Consultant-approved recycle-lineage package model |
| Target file(s) | `prompt/templates/consultant/workspace/guideline_workspace_verification.md`; `prompt/templates/consultant/workspace/changelog/changelog_guideline_workspace_verification.md` |
| Required end-state posture | VERIFICATION guidance requires a new supplementary verification artifact per recycle cycle while preserving one primary gate-facing verification artifact for the overall gate package. |
| Explicit non-target / do-not-change constraints | Do NOT create derived gate IDs. Do NOT change verdict taxonomy. Do NOT remove the primary/supplementary package model. |
| Validation check | `§IV.A`, `§IV.B`, `§IX`, and `§XI` are aligned to the supplementary recycle-cycle rule; changelog has a new entry. |
| Blocking ambiguity rule | If the amendment would imply a new gate identity for a recycle cycle, stop and escalate. |
| Status | `open` |

#### Implementation Detail

1. In `§IV.A Verification Package`, add a rule that implementation-backed recycle cycles MAY accumulate supplementary verification artifacts under one primary verification artifact for the same gate.
2. In `§IV.B Re-assessment (Temporal Iteration)`, replace the current rule that same-gate rework version-bumps the existing verification artifact.
3. State explicitly:
   - new recycle cycles produce new supplementary verification artifacts
   - the primary verification remains the gate-facing verdict surface
   - version bumps are reserved for corrections inside one verification artifact, not for a new recycle cycle
4. In `§IX Re-assessment Versioning`, update the lifecycle text to match the new rule.
5. In `§XI Naming Convention`, preserve the current primary and supplementary naming patterns and add a note that recycle-cycle supplementary verification artifacts should use the aspect suffix to encode the cycle descriptor.
6. Add one changelog row in `changelog_guideline_workspace_verification.md`.

### SPEC-004 - Amend PLAN and PROPOSAL guidance for recycle-cycle package indexing

| Field | Detail |
|:--|:--|
| Requirement Source | Consultant-approved GATE-002 orchestration update |
| Target file(s) | `prompt/templates/consultant/workspace/guideline_workspace_plan.md`; `prompt/templates/consultant/workspace/changelog/changelog_guideline_workspace_plan.md`; `prompt/templates/consultant/workspace/guideline_workspace_proposal.md`; `prompt/templates/consultant/workspace/changelog/changelog_guideline_workspace_proposal.md` |
| Required end-state posture | Plan and proposal guidance explicitly allow dotted recycle-cycle tasking and require primary-first, supplementary-second evidence ordering in gate packages. |
| Explicit non-target / do-not-change constraints | Do NOT change the fixed Gate-Readiness Stack ordering or GDR ownership rules. |
| Validation check | `guideline_workspace_plan.md` and `guideline_workspace_proposal.md` both mention supplementary recycle-cycle evidence/indexing in the correct sections; both changelog files have new entries. |
| Blocking ambiguity rule | If the change would require a new proposal archetype or new gate subtype, stop and escalate. |
| Status | `open` |

#### Implementation Detail

1. In `guideline_workspace_plan.md` `§VI.K` and `§VI.L`, add a short clarification that same-gate recycle may register dotted sub-tasks such as `TK012.n` and `TK013.n` when new cycle-local evidence artifacts are produced under the same gate.
2. Keep the gate status rule unchanged: the gate remains `in_progress` until the latest cycle passes.
3. In `guideline_workspace_proposal.md` `§V.B Gate Package section specification`, add an evidence-ordering rule:
   - primary current-cycle package evidence first
   - supplementary recycle-cycle evidence second
   - historical/superseded evidence last
4. Add one changelog row to each changelog file.

### SPEC-005 - Align the AC000 plan to the approved GATE-002 orchestration posture

| Field | Detail |
|:--|:--|
| Requirement Source | Consultant-approved GATE-002 orchestration update; user QA direction that the main consultant is the reviewer and assistant housekeeping must be spec-governed |
| Target file(s) | `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/plan_T102-PH001-ST002-AC000.md` |
| Required end-state posture | The AC000 plan reflects the updated GATE-002 orchestration posture: assistant-governed housekeeping is recognized, the consultant is the active verifier for `TK013`, and TK012/TK013/TK014/TK015/GATE-002 all describe primary/supplementary recycle-cycle package handling. |
| Explicit non-target / do-not-change constraints | Do NOT change completed GATE-001 history. Do NOT edit the Gate-001 proposal. Do NOT mark any GATE-002 task completed. |
| Validation check | Task Register and detailed sections for `TK012`-`TK015` and `GATE-002` reflect the updated orchestration model; `TK013` owner is `LLM_Consultant`; no new downstream execution is falsely marked complete. |
| Blocking ambiguity rule | If aligning the plan requires inventing new implementation scope beyond package-governance and sequencing language, stop and escalate. |
| Status | `open` |

#### Implementation Detail

1. Update the `TK013` Task Register row owner from `LLM_Reviewer` to `LLM_Consultant`.
2. In the `TK012` detailed section:
   - keep the primary deliverable path unchanged
   - add a sentence that the first cycle produces the primary `DEV-REPORT` and any recycle cycle produces supplementary `DEV-REPORT` artifacts under the same gate package
   - state that all supplementary cycles remain under the same `GATE-002`
3. In the `TK013` detailed section:
   - state that the main `LLM_Consultant` performs the verification pass for this cycle
   - add that recycle cycles produce supplementary verification artifacts while the primary verification remains the gate-facing verdict surface
4. In the `TK014` detailed section:
   - state explicitly that proposal authoring may begin only after the latest verification cycle returns a non-`RECYCLE` verdict
   - state that the proposal Evidence Index must list primary evidence first, supplementary recycle-cycle evidence second, and historical evidence last
5. In the `TK015` detailed section:
   - keep the external-review role as `LLM_Subconsultant`
   - add that the external review consumes the authoritative primary package surfaces plus any linked supplementary recycle-cycle evidence
6. In the `GATE-002` detailed section:
   - update entry criteria text to allow the active primary `DEV-REPORT`/`VERIFICATION` package to include linked supplementary recycle-cycle artifacts when the gate has recycled
7. Add one changelog row describing the GATE-002 orchestration hardening update.

## IV. IMPLEMENTATION SEQUENCE

1. Amend `workspace_documentation_rules.md`.
2. Amend `guideline_workspace_dev-report.md`.
3. Amend `guideline_workspace_verification.md`.
4. Amend `guideline_workspace_plan.md` and `guideline_workspace_proposal.md`.
5. Amend the AC000 plan.
6. Re-read all touched files and confirm the recycle-lineage rule is stated consistently.
7. Stop and hand the output back to the main consultant for review before any developer execution begins.

## V. REFERENCES

| Document | Path |
|:--|:--|
| Governing Plan | `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/plan_T102-PH001-ST002-AC000.md` |
| Workspace Documentation Rules | `prompt/templates/consultant/workspace/workspace_documentation_rules.md` |
| DEV-REPORT Guideline | `prompt/templates/consultant/workspace/guideline_workspace_dev-report.md` |
| VERIFICATION Guideline | `prompt/templates/consultant/workspace/guideline_workspace_verification.md` |
| PLAN Guideline | `prompt/templates/consultant/workspace/guideline_workspace_plan.md` |
| PROPOSAL Guideline | `prompt/templates/consultant/workspace/guideline_workspace_proposal.md` |

## VI. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-04-02 | Initial | Authored the bounded assistant-housekeeping brief for the pre-TK011 orchestration hardening pass covering recycle-lineage governance amendments and AC000 GATE-002 plan alignment before developer execution. |
