---
artifact_type: 'IMPLEMENTATION'
implementation_type: 'task_specification'
initiative_id: 'T103'
initiative_code: 'ADRSS'
phase: '0'
stream_id: 'T103-PH000-ST000'
activity_id: 'T103-PH000-ST000-AC001'
task_id: 'T103-PH000-ST000-AC001-TK003'
version: '1.0.0'
date: '2026-03-23'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC001/plan_T103-PH000-ST000-AC001.md'
purpose: 'Draft consultant-audience execution specification for orchestrator-agent dispatch patterns covering agent assignment, context management, wave boundaries, recycle re-entry, and sub-consultant integrity dispatch.'
execution_audience: 'consultant'
---

# IMPLEMENTATION (Task Specification): T103-PH000-ST000-AC001 Draft Orchestration Execution Patterns

## I. PURPOSE & AUTHORITY

- **Purpose**: Define the draft execution-level orchestration patterns that the main consultant can use when moving from plan authority into delegated multi-role execution.
- **Authority chain**: The AC001 activity plan remains the tracked-work authority -> this artifact defines the execution HOW for consultant orchestration -> downstream worker packages and gate proposals consume these patterns operationally.
- **Audience**: Main LLM_Consultant as orchestrator; delegated developer, reviewer, and sub-consultant workers as role-specific consumers of the orchestrator's briefing package.
- **Boundary**: This is a draft-only operational specification. It does not amend governed workspace guidelines or create a new formal `implementation_type`.
- **Trigger**: AC001 assessment confirmed that the workspace has repeatable orchestration needs but no codified execution protocol for dispatch, context, wave control, recycle re-entry, or sub-consultant integrity dispatch.

## II. EXECUTION POSTURE

- The consultant remains responsible for orchestration boundaries even when delegated workers author the underlying artifacts.
- Artifact-level recyclable-loop rules continue to come from T104 AC001.9 and the existing workspace governance suite.
- This document operationalizes those rules for the consultant's execution layer and must be read as draft guidance pending T103 PH001 binding work.

## III. DRAFT SPECIFICATION ITEMS

### SPEC-D001 - Agent Dispatch Model

| Field | Detail |
|:--|:--|
| Requirement Source | `EGAP-001`; AC001 assessment recommendation |
| Primary Inputs | AC001 assessment; AC001.6 orchestration exemplar; activity plan role boundaries |
| Output | Standard dispatch model for consultant, developer, reviewer, and sub-consultant workers |
| Acceptance Criteria | Role/model/effort/write-scope selection rules are explicit and the consultant can decide when to dispatch each worker role without inventing local policy |

#### Implementation Detail

Use the following dispatch table structure whenever the consultant orchestrates delegated execution:

| Role | Agent Type | Model | Effort | Write Scope | Ownership |
|:--|:--|:--|:--|:--|:--|
| Main consultant | Current main context | n/a | n/a | No direct implementation writes during orchestrated runs | Orchestration only |
| Developer worker | Worker/sub-agent | Selected for task complexity | Selected for task complexity | Explicit disjoint file list or bounded artifact scope | Developer-owned implementation and DEV-REPORT authoring |
| Reviewer worker | Worker/sub-agent | Higher-quality review model | Medium or high | Review artifacts only; no implementation writes | Independent verification and recycle findings |
| Sub-consultant worker | Worker/sub-agent | Consultant-quality reasoning model | High | Consultant-owned package/pre-gate surfaces | Integrity/tracing review and consultant-owned package work |

Dispatch rules:
- Use a developer worker when the task produces developer-owned artifacts or file mutations.
- Use a reviewer worker only after a bounded developer wave has produced reviewable evidence.
- Use a sub-consultant worker for consultant-owned package assembly, traceability review, proposal authoring, or plan-amendment support during recycle.
- Parallel workers are allowed only when write scopes are disjoint and the consultant can preserve clean evidence boundaries.

### SPEC-D002 - Context Management Protocol

| Field | Detail |
|:--|:--|
| Requirement Source | `EGAP-002`; SES001 consultation findings |
| Primary Inputs | AC001 assessment; AC001.6 orchestration exemplar; relevant plan/implementation/proposal surfaces |
| Output | Minimum context-injection protocol for each delegated worker role |
| Acceptance Criteria | The consultant can assemble a role-specific briefing pack without overloading or under-specifying worker context |

#### Implementation Detail

The consultant must provide a role-specific context pack rather than a generic full-history dump.

Minimum briefing content by role:
- **Developer worker**: governing plan excerpt, relevant implementation specification, explicit write scope, expected deliverable path, success criteria, and current recycle state if applicable.
- **Reviewer worker**: governing gate/task excerpt, artifact paths under review, DEV-REPORT path(s), verification baseline, and any prior recycle findings that remain in scope.
- **Sub-consultant worker**: activity-level purpose, evidence index, role-boundary matrix, applicable audit criteria, and the proposal or integrity output expected from the run.

Context rules:
- Include the minimal quoted scope needed for execution; reference stable artifacts by path instead of inlining their full contents.
- Re-inject context whenever a recycle verdict changes the operative scope, evidence version, or expected worker output.
- Do not rely on prior chat continuity alone to carry plan authority, artifact paths, or role boundaries.

### SPEC-D003 - Wave Boundary Management

| Field | Detail |
|:--|:--|
| Requirement Source | `EGAP-003`; AC001.6 wave DEV-REPORT model |
| Primary Inputs | AC001 assessment; AC001.6 orchestration plan; current gate-readiness stack rules |
| Output | Draft protocol for partitioning work into waves and advancing across review boundaries |
| Acceptance Criteria | The consultant can state when a wave starts, when it is complete, and when the next wave or recycle loop may begin |

#### Implementation Detail

Wave partitioning must be based on dependency boundaries, write-scope disjointness, or thematic coherence. A wave is complete only when:
1. The delegated producer has finished the assigned bounded scope.
2. Any required DEV-REPORT for that wave exists.
3. The consultant has enough evidence to hand the wave to an independent reviewer.

Wave advancement protocol:
1. Commission a bounded developer wave.
2. Wait for the producer evidence package.
3. Dispatch reviewer against that wave.
4. If reviewer passes, either advance to the next wave or, if final, move to consolidated packaging.
5. If reviewer recycles, pause downstream waves and enter recycle re-entry for the same wave boundary.

Where artifact-level rules require supplementary and consolidated evidence, the consultant must preserve that distinction operationally rather than collapsing wave evidence into one opaque handoff.

### SPEC-D004 - Recycle Re-Entry Execution

| Field | Detail |
|:--|:--|
| Requirement Source | `EGAP-004`; current plan/verification recycle semantics |
| Primary Inputs | AC001 assessment; `guideline_workspace_plan.md`; `guideline_workspace_verification.md` |
| Output | Draft consultant protocol for same-gate recycle re-entry after reviewer findings |
| Acceptance Criteria | The consultant can re-enter the loop without inventing local control rules or losing evidence lineage |

#### Implementation Detail

Recycle handling sequence:
1. Receive the reviewer verdict and findings package.
2. Classify the issue using the current Situation A / Situation B framing from the workspace verification rules.
3. If the issue is a deliverable deficiency within approved scope, re-brief the relevant producer on the same bounded scope plus the findings.
4. If the issue is a scope gap, route through the appropriate consultant-owned amendment/remediation surface before re-dispatching implementation.
5. Re-dispatch the reviewer against the updated evidence package after remediation completes.

Lineage rules:
- Keep the same gate identity during recycle.
- Preserve the chain of producer evidence, reviewer findings, and updated artifacts across cycles.
- Re-brief with the prior findings explicitly attached; do not assume the new worker will infer them from history.

### SPEC-D005 - Sub-Consultant Integrity Dispatch

| Field | Detail |
|:--|:--|
| Requirement Source | `EGAP-005`; SES001 interface decision with T104 AC001.9 |
| Primary Inputs | AC001 assessment; gate package evidence; T104 artifact-level integrity/audit rules where applicable |
| Output | Draft trigger and context protocol for post-loop integrity/traceability dispatch |
| Acceptance Criteria | The consultant can decide when to dispatch a sub-consultant and what audit package the worker must consume and return |

#### Implementation Detail

Trigger the sub-consultant after the recyclable implementation/review loop is substantively complete and before final gate packaging. The sub-consultant briefing pack must include:
- The activity or gate purpose
- The governing plan and relevant implementation references
- The evidence index covering producer and reviewer artifacts
- The role-boundary expectations for the audit
- The expected consultant-owned output path or proposal surface

Expected output contract:
- Confirm whether the evidence chain is complete and traceable
- Identify any missing handoff or ownership boundary
- Provide a concise integrity assessment that the main consultant can incorporate into the final gate package

This trigger is the execution-layer companion to any artifact-level traceability audit rules authored elsewhere.

## IV. NON-INTERRUPTION / CONTROL RULES

- The main consultant should remain orchestration-only during multi-role runs unless the activity explicitly authorizes direct artifact work.
- Do not interrupt active workers except for tool/runtime failure, scope change, or a decision-boundary issue that invalidates the current run.
- Re-enter only at control boundaries: worker completion, reviewer verdict, recycle classification, sub-consultant audit completion, or explicit client decision.
- Preserve disjoint write scopes for parallel producers.
- Close stale workers after their bounded phase is complete to avoid accidental context carry-over.
- Treat the governing plan, implementation specification, and proposal surfaces as the source of truth; do not let ad-hoc chat improvisation replace those authority surfaces.

## V. DECISION TESTS

| Situation | Pattern | Reference |
|:--|:--|:--|
| Single-task, single-agent execution | No orchestration pattern needed beyond direct execution | — |
| Multi-task execution with one producer wave | Use agent dispatch plus context management | `SPEC-D001`, `SPEC-D002` |
| Multi-wave execution with bounded review between waves | Add wave boundary management | `SPEC-D003` |
| Same-gate recycle after reviewer findings | Add recycle re-entry protocol | `SPEC-D004` |
| Gate packaging after recyclable implementation/review loop | Add sub-consultant integrity dispatch | `SPEC-D005` |

This specification is draft-only for operational use. Normative binding into `guideline_workspace_implementation.md` or `workspace_documentation_rules.md` is deferred to T103-PH001.

## VI. REFERENCES

| Document | Path |
|:--|:--|
| Governing plan | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC001/plan_T103-PH000-ST000-AC001.md` |
| Driving assessment | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC001/analysis/analysis_T103-PH000-ST000-AC001_orchestration-execution-pattern-assessment.md` |
| Draft-specification authority | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC001/implementation/implementation_T103-PH000-ST000-AC001_orchestration-execution-pattern-draft-spec.md` |
| AC001.6 orchestration exemplar | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/implementation/implementation_T104-PH001-ST008-AC001.6_gate-001-to-gate-002-orchestration-plan.md` |
| SES001 consultation transcript | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC001/raw/raw_T103-PH000-ST000-AC001-SES001.txt` |
| Claude orchestration evidence | `raw_P-PH000-ST002-AC002_SES003.txt` |
| Codex orchestration evidence | `raw_T103-PH000-ST000-AC000-SES004.md` |

## VII. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-03-23 | Initial | Authored the draft consultant-audience orchestration execution patterns covering dispatch, context, wave boundaries, recycle re-entry, and sub-consultant integrity dispatch for T103 AC001. |
