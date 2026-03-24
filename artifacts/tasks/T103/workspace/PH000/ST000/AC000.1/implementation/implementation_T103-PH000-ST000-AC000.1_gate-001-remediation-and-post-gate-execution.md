---
artifact_type: 'IMPLEMENTATION'
implementation_type: 'remediation_specification'
initiative_id: 'T103'
initiative_code: 'ADRSS'
phase: '0'
stream_id: 'T103-PH000-ST000'
activity_id: 'T103-PH000-ST000-AC000.1'
gate_id: 'T103-PH000-ST000-AC000.1-GATE-001'
task_id: 'T103-PH000-ST000-AC000.1-TK005.1'
version: '1.0.0'
date: '2026-03-24'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.1/plan_T103-PH000-ST000-AC000.1.md'
verification_reference: 'prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.1/verification/verification_T103-PH000-ST000-AC000.1_gate-001.md'
proposal_reference: 'prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.1/proposal/proposal_T103-PH000-ST000-AC000.1_gate-001_monitoring-and-testing-package.md'
purpose: 'Governed remediation specification for reconciling the AC000.1 Gate-001 package after external review and commissioning the concrete post-Gate-001 runtime-remediation execution lane through Gate-002.'
---

# IMPLEMENTATION (Remediation Specification): AC000.1 Gate-001 Reconciliation and Post-Gate Runtime Execution

## I. PURPOSE & AUTHORITY

- Purpose: Convert the external-review findings and client QA into an execution-ready correction package for the same `AC000.1-GATE-001` lane, then seed the downstream runtime-remediation execution path so Gate-001 approval closes the governance baseline without orphaning the actual monitoring/testing work.
- Authority chain: AC000.1 plan authorizes `TK005.1` -> this artifact specifies HOW -> developer execution evidence records `TK006..TK007` -> reviewer re-assesses via `TK008` -> consultant packages `TK009` -> Gate-002 hosts the client decision for the runtime-remediation lane.
- Audience: `LLM_Developer` (primary for `TK006..TK007`), `LLM_Reviewer` (re-assessment input for `TK008`), `LLM_Consultant` (proposal/package normalization for `TK009` and Gate-001/Gate-002 client presentation).
- This artifact does NOT hold a GDR. Gate decisions remain exclusively in the Gate-001 and Gate-002 proposal artifacts.

## II. REMEDIATION SCOPE

- Gate: `T103-PH000-ST000-AC000.1-GATE-001`
- Trigger: Independent external review identified governance/state drift in the Gate-001 package, and client QA directed that (a) the activity-plan register be reconciled before GDR recording and (b) the actual post-Gate-001 execution tasks be added now.
- Governing plan task: `T103-PH000-ST000-AC000.1-TK005.1`
- Trigger references:
  - `GAP-001` through `GAP-003` in `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.1/analysis/analysis_T103-PH000-ST000-AC000.1_gate-001-external-review.md`
  - Client QA in the current consultation session: register reconciliation required before GDR; post-Gate-001 execution lane must be added as part of the activity
  - `GAP-001` through `GAP-005` in `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.1/analysis/analysis_T103-PH000-ST000-AC000.1_claude-code-skill-post-gate-003-runtime-observations.md`

## III. REMEDIATION ITEMS

### REM-001 — Reconcile the AC000.1 Plan Register to the Real Gate-001 Package State

| Field | Detail |
|:--|:--|
| Trigger Reference | External review `GAP-001` |
| Revision Deliverable | Updated `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.1/plan_T103-PH000-ST000-AC000.1.md` |
| Expected Format | Activity-plan amendment with corrected task/gate statuses, outcome-based `Action` text, updated entry/exit criteria, and an explicit post-Gate-001 dependency chain |
| Acceptance Criteria | `TK002` through `TK005` and `TK005.1` are no longer shown as `planned`; `GATE-001` is no longer presented as not-yet-reached; the plan remains the authoritative surface for current Gate-001 posture |
| Resolution Status | `resolved` |

#### Implementation Detail

Update the AC000.1 activity plan before any Gate-001 GDR recording. The minimum correction set is:

1. Mark `TK002`, `TK003`, `TK004`, and `TK005` as `completed` with concise outcome-based `Action` text that points to the actual completed package state.
2. Register `TK005.1` as a consultant-owned pre-gate normalization task and mark it `completed` once this remediation artifact and the plan amendment both exist.
3. Change `GATE-001` to `in_progress`, not `planned`, because the gate package exists and is under client disposition rather than not-yet-reached.
4. Update `GATE-001` entry criteria so `TK005.1` is included explicitly.
5. Update `GATE-001` exit criteria so approval clearly commissions the downstream runtime-remediation lane instead of implying that AC000.1 ends at the governance baseline.

Do not treat the stale register as a cosmetic issue. It is the authoritative anti-drift surface under `guideline_workspace_plan.md`.

### REM-002 — Refresh the Gate-001 Client Package to Match the Correct Approval Semantics

| Field | Detail |
|:--|:--|
| Trigger Reference | External review `GAP-001`, `GAP-003`; client QA |
| Revision Deliverable | Updated `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.1/proposal/proposal_T103-PH000-ST000-AC000.1_gate-001_monitoring-and-testing-package.md` |
| Expected Format | Proposal amendment only; same gate ID; no new proposal subtype |
| Acceptance Criteria | Proposal explains that Gate-001 closes the governance baseline only, references the external review, and points to the registered post-Gate-001 execution lane instead of implying the activity ends at Gate-001 |
| Resolution Status | `open` |

#### Implementation Detail

Amend the Gate-001 proposal so its client-facing recommendation matches the corrected plan state:

1. Add the Gate-001 external review artifact to the Evidence Index and References.
2. Update the Executive Summary and GIR-001 rationale so the recommendation reflects the corrected package state: the register is reconciled, the downstream execution lane is registered, and approval closes the governance baseline only.
3. Preserve the upstream-boundary story: `GATE-003` stays closed.
4. Update `Downstream enforcement` so it explicitly states that `TK006` through `GATE-002` remain blocked until the Gate-001 GDR records `APPROVE` or `APPROVE WITH CONDITIONS`.
5. Do not claim that “the remaining work after this gate is client decision capture” because that is no longer true once the runtime-remediation lane is registered.

If all remediation work in REM-001 and REM-003 is completed before the proposal is refreshed, the Gate-001 recommendation may remain `APPROVE`. If not, the proposal must explain the residual condition precisely instead of hiding it.

### REM-003 — Register the Concrete Post-Gate-001 Execution Lane in the AC000.1 Plan

| Field | Detail |
|:--|:--|
| Trigger Reference | External review `GAP-003`; runtime-observations `GAP-001` through `GAP-005`; client QA |
| Revision Deliverable | Expanded AC000.1 plan with `TK006` through `GATE-002` |
| Expected Format | Task-register rows plus detailed task sections and canonical output paths |
| Acceptance Criteria | Post-Gate-001 work is no longer implicit; `TK006` through `TK009` and `GATE-002` exist with correct dependencies, owners, deliverables, and proposal path |
| Resolution Status | `resolved` |

#### Implementation Detail

Pre-register the downstream execution lane immediately after `GATE-001` in dependency order:

- `TK006` — developer execution of the runtime-remediation mutation set
- `TK007` — developer dev-report for the runtime-remediation lane
- `TK008` — reviewer verification for `AC000.1-GATE-002`
- `TK009` — consultant proposal for `AC000.1-GATE-002`
- `GATE-002` — client acceptance of the runtime-remediation execution package

Use the following canonical output paths:

- `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.1/dev-report/dev-report_T103-PH000-ST000-AC000.1_runtime-monitoring-and-testing-remediation_2026-03-24.md`
- `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.1/verification/verification_T103-PH000-ST000-AC000.1_gate-002_runtime-monitoring-and-testing-remediation.md`
- `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.1/proposal/proposal_T103-PH000-ST000-AC000.1_gate-002_runtime-monitoring-and-testing-remediation-acceptance.md`

This is the forward traceability correction for the TK001 runtime gaps. Do not retro-edit the historical TK001 analysis just to change its `deferred_to_TK002` labels. Instead, make the forward authority surfaces unambiguous.

### REM-004 — Execute the Runtime-Remediation Mutation Set for TK006

| Field | Detail |
|:--|:--|
| Trigger Reference | Runtime-observations `GAP-001` through `GAP-005` |
| Revision Deliverable | Updated Claude Code skill/runtime surfaces plus execution evidence for `TK006` |
| Expected Format | Bounded code/documentation change set with developer evidence and direct validation output |
| Acceptance Criteria | The mutation set is limited to the declared runtime-remediation files, the CLI/runtime guidance matches observed behavior, and the validator/manual evidence surfaces cover the required gap scenarios |
| Resolution Status | `open` |

#### Implementation Detail

Treat the runtime-remediation mutation set as the following bounded file group unless execution proves another directly dependent Claude Code file must change:

| File | Why it is in scope |
|:--|:--|
| `.agents/skills/claude-code/SKILL.md` | Primary operator contract for runtime behavior, blocked-state handling, provenance, and working-directory guidance |
| `.agents/skills/claude-code/references/claude-code-cli.md` | Exact CLI reference that currently presents `-C` / `--cd` guidance |
| `.agents/skills/claude-code/references/claude-code-testing.md` | Testing/release contract for repeatable monitoring and validation coverage |
| `.agents/skills/claude-code/scripts/validate_claude_code_skill.py` | Static/local validator coverage for the changed contract |

Execution requirements for `TK006`:

1. Verify the live installed Claude CLI surface before editing any working-directory guidance. Do not preserve `-C` / `--cd` wording if the installed CLI in this environment rejects it.
2. Reconcile the operator guidance for slow or blocked write-enabled runs so the skill distinguishes:
   - live but silent;
   - blocked on user action;
   - completed with no artifact;
   - failed;
   - handed off to the user.
3. Strengthen provenance/authorship reporting so mixed Claude/Codex outcomes are described unambiguously.
4. Preserve explicit filesystem verification after write-enabled runs. The testing guide and any skill wording must still require on-disk confirmation rather than trusting CLI narration alone.
5. Expand the repeatable assurance posture in the testing guide and validator so the execution lane can produce more than a one-off anecdotal success report. At minimum, ensure the evidence contract covers:
   - CLI-surface compatibility for the documented working-directory pattern;
   - slow/still-live state classification;
   - blocked-state handling;
   - provenance wording;
   - filesystem verification after writes.

Do not widen this lane into unrelated Claude Code feature work. The target is runtime-remediation and repeatable assurance, not a redesign of the skill.

### REM-005 — Produce the Gate-002 Developer Evidence Package

| Field | Detail |
|:--|:--|
| Trigger Reference | `TK007` in the amended AC000.1 plan |
| Revision Deliverable | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.1/dev-report/dev-report_T103-PH000-ST000-AC000.1_runtime-monitoring-and-testing-remediation_2026-03-24.md` |
| Expected Format | `DEV-REPORT` following `guideline_workspace_dev-report.md` with `implementation_reference` set to this remediation specification |
| Acceptance Criteria | Dev-report exists at the canonical path, describes the bounded mutation set, records concrete validation commands/evidence, and maps outputs back to `REM-004` |
| Resolution Status | `open` |

#### Implementation Detail

Author the developer report after `TK006` is complete. The report must:

1. Use `source_plan` set to the amended AC000.1 activity plan.
2. Use `implementation_reference` set to this remediation specification.
3. Record the exact files changed under `TK006`.
4. Capture concrete command evidence for the validator and any bounded live/manual checks the execution lane performs.
5. Include a traceability matrix that maps the delivered mutation set and evidence surfaces back to `REM-004`.

### REM-006 — Re-Assess the Runtime-Remediation Lane at Gate-002

| Field | Detail |
|:--|:--|
| Trigger Reference | `TK008` in the amended AC000.1 plan |
| Revision Deliverable | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.1/verification/verification_T103-PH000-ST000-AC000.1_gate-002_runtime-monitoring-and-testing-remediation.md` |
| Expected Format | Gate verification following `guideline_workspace_verification.md` |
| Acceptance Criteria | Reviewer independently inspects the bounded mutation set, validates the developer evidence, and records a single Gate-002 verdict with findings if needed |
| Resolution Status | `open` |

#### Implementation Detail

The reviewer must not rely only on the dev-report summary. At minimum, `TK008` must independently verify:

1. The Claude Code skill, CLI reference, testing guide, and validator all tell the same story.
2. The working-directory guidance matches the actually verified CLI posture used during execution.
3. Slow-run / blocked-state / provenance / filesystem-verification guidance is present where it needs to be.
4. The execution evidence is repeatable enough to justify a Gate-002 client decision.

If findings arise, keep them bounded to the `AC000.1-GATE-002` execution lane. Do not reopen `GATE-003` unless the evidence truly contradicts the accepted hardening boundary.

### REM-007 — Package the Gate-002 Client Decision Set

| Field | Detail |
|:--|:--|
| Trigger Reference | `TK009` in the amended AC000.1 plan |
| Revision Deliverable | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.1/proposal/proposal_T103-PH000-ST000-AC000.1_gate-002_runtime-monitoring-and-testing-remediation-acceptance.md` |
| Expected Format | Gate-disposition proposal with pending GDR |
| Acceptance Criteria | Proposal packages the runtime-remediation execution evidence, aligns to the reviewer verdict, preserves the `GATE-003` boundary, and leaves the Gate-002 GDR ready for client decision |
| Resolution Status | `open` |

#### Implementation Detail

After verification, the consultant packages the Gate-002 proposal. The proposal must:

1. Present the runtime-remediation lane as the substantive execution follow-on to Gate-001.
2. Cite the amended plan, this remediation specification, the `TK007` dev-report, and the `TK008` verification artifact.
3. Preserve the statement that Gate-002 evaluates AC000.1 execution work, not the already-closed upstream hardening gate.

## IV. IMPLEMENTATION SEQUENCE

1. Treat `REM-001` and `REM-003` as the current-state baseline established by the plan amendment authored with this specification.
2. Complete `REM-002` next so the Gate-001 proposal matches the corrected approval semantics before client disposition.
3. After Gate-001 approval, execute `REM-004` as `TK006`.
4. Produce the developer evidence package in `REM-005`.
5. Re-assess the lane in `REM-006`.
6. Package Gate-002 client disposition in `REM-007`.

## V. REFERENCES

| Document | Path |
|:--|:--|
| Governing Plan | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.1/plan_T103-PH000-ST000-AC000.1.md` |
| Gate-001 Verification | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.1/verification/verification_T103-PH000-ST000-AC000.1_gate-001.md` |
| Gate-001 Proposal | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.1/proposal/proposal_T103-PH000-ST000-AC000.1_gate-001_monitoring-and-testing-package.md` |
| Gate-001 External Review | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.1/analysis/analysis_T103-PH000-ST000-AC000.1_gate-001-external-review.md` |
| Runtime Observations Analysis | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.1/analysis/analysis_T103-PH000-ST000-AC000.1_claude-code-skill-post-gate-003-runtime-observations.md` |
| Prior Gate-001 Task Specification | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.1/implementation/implementation_T103-PH000-ST000-AC000.1_post-gate-003-monitoring-governance.md` |

## VI. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-03-24 | Initial | Created the AC000.1 Gate-001 remediation specification to reconcile the stale Gate-001 governance package state after external review and to commission the concrete post-Gate-001 runtime-remediation execution lane through Gate-002. |
