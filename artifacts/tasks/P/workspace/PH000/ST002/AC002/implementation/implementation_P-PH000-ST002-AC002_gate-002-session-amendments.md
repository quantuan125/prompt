---
artifact_type: 'IMPLEMENTATION'
implementation_type: 'task_specification'
initiative_id: 'P'
initiative_code: 'PROGRAM'
phase: '0'
stream_id: 'P-PH000-ST002'
activity_id: 'P-PH000-ST002-AC002'
gate_id: 'P-PH000-ST002-AC002-GATE-002'
version: '1.0.0'
date: '2026-03-21'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST002/AC002/plan_P-PH000-ST002-AC002.md'
purpose: 'Session-level implementation specification for GATE-002 review completion: task specification authoring, proposal update, plan amendment, guideline cleanup, cross-initiative AC001.8 creation, and session notes.'
---

# IMPLEMENTATION (Task Specification): GATE-002 Session Amendments — P-PH000-ST002-AC002

## I. PURPOSE & AUTHORITY

- **Purpose**: Specify the exact file changes required to complete the GATE-002 review session for `P-PH000-ST002-AC002`. This covers: (1) authoring the Phase 1 developer-facing task specification for TK002–TK004, (2) populating the GATE-002 proposal consultant recommendation, (3) amending the AC002 activity plan with GATE-003 readiness stack and implementation spec references, (4) fixing the stale 7-state wording in `guideline_workspace_plan.md`, (5) creating the `T104-PH001-ST008-AC001.8` sub-activity plan and registering it in the ST008 stream plan, and (6) authoring AC002 SES002 session notes.
- **Authority chain**: The AC002 activity plan authorizes the gate review session → this artifact specifies HOW the session amendments are executed → dev-report or session notes record execution evidence.
- **Audience**: LLM_Developer or LLM_Consultant (session executor)
- This artifact does NOT hold a GDR. The GATE-002 decision is recorded in `proposal_P-PH000-ST002-AC002-GATE-002_design-decision-disposition.md`.

## II. TASK SCOPE

- **Governing gate**: `P-PH000-ST002-AC002-GATE-002`
- **Trigger**: GATE-002 independent package review identified: (a) GDR §V/§VI not populated, (b) GATE-003 missing readiness stack and required fields, (c) TK002–TK004 lack implementation specification reference, (d) `guideline_workspace_plan.md` stale 7-state wording, (e) process observations requiring tracked governance action under T104.
- **Deliverable contract**: All files listed in SPEC-001 through SPEC-007 updated or created; GATE-002 proposal ready for client decision.

## III. SPECIFICATION ITEMS

### SPEC-001 — Author Phase 1 Task Specification (TK002–TK004 Developer Spec)

| Field | Detail |
|:--|:--|
| Requirement Source | GATE-002 consultation: approved GIR-001(a), GIR-002(a), GIR-003(a) must be distilled into developer-facing specification; CONV-011 requires implementation artifact when task complexity exceeds plan-step capacity |
| Implementation Detail | See §III.A below for full content specification |
| Target file(s) | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC002/implementation/implementation_P-PH000-ST002-AC002_task-specification.md` (NEW) |
| Acceptance Criteria | File exists; frontmatter per `guideline_workspace_implementation.md` §V; contains SPEC items for TK002, TK003, TK004 with concrete schema/section/validation detail derived from approved GIR decisions and requirements analysis §V.C–§V.G |
| Status | `open` |

#### §III.A — Phase 1 Task Specification Content Requirements

The new `implementation_P-PH000-ST002-AC002_task-specification.md` MUST contain the following:

**Frontmatter**:
```yaml
artifact_type: 'IMPLEMENTATION'
implementation_type: 'task_specification'
initiative_id: 'P'
initiative_code: 'PROGRAM'
phase: '0'
stream_id: 'P-PH000-ST002'
activity_id: 'P-PH000-ST002-AC002'
gate_id: 'P-PH000-ST002-AC002-GATE-002'
version: '1.0.0'
date: '2026-03-21'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST002/AC002/plan_P-PH000-ST002-AC002.md'
purpose: 'Unified developer-facing task specification for TK002 (ledger skeleton), TK003 (narrative template), and TK004 (conformance validation), distilling approved GATE-002 GIR decisions into concrete implementation instructions.'
```

**SPEC-001 (TK002 — Author Ledger Skeleton)**:
- Target file: `prompt/artifacts/tasks/P/status/status_program.yaml`
- Create directory `prompt/artifacts/tasks/P/status/` if it does not exist
- Schema: Use the concrete ledger schema from implementation requirements analysis §V.C verbatim
- 8-state enum: `planned`, `ready`, `in_progress`, `blocked`, `on_hold`, `deferred`, `completed`, `cancelled`
- GIR-002(a) applied: `scope_uid` values use P-STD-005 timeline UID patterns (e.g., `P-PH000-ST001-AC003`); `scope_type` supports `initiative`, `phase`, `stream`, `activity` but v1 populates activity-level only
- GIR-003(a) applied: CLAUSE-024 (`schedule_relation`, `lag`) — EXCLUDED; CLAUSE-028 (`platform`, `run_id`) — EXCLUDED; CLAUSE-051 (`execution_refs[]`) — INCLUDED as empty array; CLAUSE-053 (`approval_policy`, `sandbox_mode`) — EXCLUDED
- MVAT per CLAUSE-054: every entry MUST include `status`, `as_of`, `updated_by`, `last_updated`, and `evidence` (1+ pointers for evidence-required transitions)
- Extension hooks: `extensions: {}` object + `x_` prefix convention per CLAUSE-046
- `schema_version: "1.0"` per CLAUSE-050
- Include 1 example skeleton entry (using a placeholder activity UID) to demonstrate the schema structure — leave all value fields as placeholders (`"<value>"`)
- Acceptance criteria: file exists at correct path; YAML is valid; all MVAT fields present; 8-state enum; GIR-003(a) inclusion/exclusion applied; P-STD-004 placement satisfied

**SPEC-002 (TK003 — Author Narrative Template)**:
- Target file: `prompt/artifacts/tasks/P/status/status_program.md`
- Frontmatter per requirements analysis §V.D: `artifact_type: 'STATUS'`, `initiative_id: 'P'`, `schema_version: '1.0'`, `ledger_reference` pointing to the YAML ledger
- 8 sections per §V.D: Summary, Status, Health, Dependencies, Evidence, Next Actions, Operational Update Protocol, Changelog
- GIR-001(a) applied: Operational Update Protocol section MUST embed the agent-role binding table from §V.E (4 RACI rows, 7 update triggers, terminal/reopen execution rule, conflict resolution rule, update sequence)
- Sections 1–6 carry `<!-- DERIVED FROM LEDGER -->` markers per CLAUSE-048 derivation rule
- Authority hierarchy statement: "The ledger (`status_program.yaml`) is authoritative. This narrative is derived. Any drift → correct the narrative."
- Acceptance criteria: file exists; all 8 sections present; binding table embedded in §7; authority hierarchy stated; P-STD-004 placement satisfied

**SPEC-003 (TK004 — Conformance Validation)**:
- Reference the §V.G structural/content conformance checklist from the requirements analysis
- Specify that TK004 validates TK002 + TK003 outputs against the checklist items listed under "Structural/content conformance (AC002 GATE-002 / AC003 GATE-002)" in §V.G
- Acceptance criteria: checklist items evaluated with evidence; failures identified with remediation

**Implementation Sequence**: SPEC-001 → SPEC-002 → SPEC-003 (sequential: ledger first, narrative derives from it, validation comes last)

**References**: Must reference the requirements analysis, P-STD-002, P-STD-005, the GATE-002 proposal (for GIR decisions), and the AC002 plan.

---

### SPEC-002 — Populate GATE-002 Proposal Consultant Recommendation

| Field | Detail |
|:--|:--|
| Requirement Source | `guideline_workspace_proposal.md` §VII.D step 1: Consultant Recommendation MUST be populated at authoring time |
| Implementation Detail | See exact changes below |
| Target file(s) | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC002/proposal/proposal_P-PH000-ST002-AC002-GATE-002_design-decision-disposition.md` |
| Acceptance Criteria | §V populated with APPROVE rationale; §VI GDR Consultant Recommendation = `APPROVE`; task specification added to Gate Package Index and Evidence Index; version bumped to v1.1.0 |
| Status | `open` |

**Change 1 — Gate Package Index (§II.A)**: Add a new row after the AC002 Activity Plan row:
```
| Task Specification (TK002–TK004 Developer Spec) | `P-PH000-ST002-AC002` | `completed` | `pending` | Required | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC002/implementation/implementation_P-PH000-ST002-AC002_task-specification.md` |
```

**Change 2 — Evidence Index Primary Evidence (§II.B)**: Add a new row:
```
| IMPLEMENTATION | Task Specification (TK002–TK004) | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC002/implementation/implementation_P-PH000-ST002-AC002_task-specification.md` | Developer-facing implementation spec for approved GIR decisions |
```

**Change 3 — §V Gate Recommendation**: Replace the placeholder text with:
```
Consultant recommendation state:
- APPROVE

Basis:
- All remediation work from TK001.3–TK001.7 is complete and carries forward.
- GIR-001 through GIR-003 have been independently assessed against the v1.2.0 baseline and all three recommended options (a) are confirmed as sound.
- The task specification (implementation_P-PH000-ST002-AC002_task-specification.md) distills approved GIR decisions into concrete developer instructions for TK002–TK004.
- No blocking gaps remain. The deferred guideline wording cleanup (guideline_workspace_plan.md 7→8 state) is addressed in a parallel amendment and does not block this gate.

Downstream enforcement:
- `TK002` (Author ledger skeleton) and `TK003` (Author narrative template) MUST NOT begin until this gate records `APPROVE` or `APPROVE WITH CONDITIONS` in the GDR.
```

**Change 4 — §VI GDR table**: Update the following fields:
- `Consultant Recommendation`: change from `pending` to `APPROVE`
- All other GDR fields remain `pending` (awaiting client decision)

**Change 5 — Frontmatter**: Update `version` to `'1.1.0'` and `date` to `'2026-03-21'`

**Change 6 — Changelog**: Add:
```
| v1.1.0 | 2026-03-21 | Amendment | Populated consultant recommendation (APPROVE) in §V and §VI GDR. Added task specification to Gate Package Index and Evidence Index. Source: GATE-002 independent package review session. |
```

---

### SPEC-003 — Amend AC002 Activity Plan (GATE-003 Readiness Stack + Implementation Spec References)

| Field | Detail |
|:--|:--|
| Requirement Source | `guideline_workspace_plan.md` §VI.L (Gate-Readiness Stack), §VI.C (Gate-Disposition Proposal field), §IV.F / CONV-011 (plan-step boundary when IMPLEMENTATION exists) |
| Implementation Detail | See exact changes below |
| Target file(s) | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC002/plan_P-PH000-ST002-AC002.md` |
| Acceptance Criteria | TK002/TK003/TK004 reference implementation spec; TK005/TK006/TK007 added to task register; GATE-003 has `Gate-Disposition Proposal` field; version bumped to v1.5.0 |
| Status | `open` |

**Change 1 — Task Register**: Add three new rows between TK004 and GATE-003:
```
| TK005 | `P-PH000-ST002-AC002-TK005` | Produce DEV-REPORT for TK002–TK004 | `planned` | LLM_Developer | TK002, TK003, TK004 | `dev-report/` | `guideline_workspace_dev-report.md` | — |
| TK006 | `P-PH000-ST002-AC002-TK006` | Produce GATE-003 verification | `planned` | LLM_Reviewer | TK005 | `verification/` | `guideline_workspace_verification.md` | — |
| TK007 | `P-PH000-ST002-AC002-TK007` | Produce GATE-003 gate-disposition proposal | `planned` | LLM_Consultant | TK006 | `proposal/` | `guideline_workspace_proposal.md` | — |
```

**Change 2 — Task Register GATE-003 row**: Update `Depends On` from `TK004` to `TK007`.

**Change 3 — TK002 Detailed Section**: Add after existing Success Criteria:
```
**Implementation Specification**: `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC002/implementation/implementation_P-PH000-ST002-AC002_task-specification.md` (SPEC-001)
```

**Change 4 — TK003 Detailed Section**: Add after existing Success Criteria:
```
**Implementation Specification**: `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC002/implementation/implementation_P-PH000-ST002-AC002_task-specification.md` (SPEC-002)
```

**Change 5 — TK004 Detailed Section**: Add after existing Success Criteria:
```
**Implementation Specification**: `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC002/implementation/implementation_P-PH000-ST002-AC002_task-specification.md` (SPEC-003)
```

**Change 6 — GATE-003 Detailed Section**: Add field after `Exit Criteria`:
```
**Gate-Disposition Proposal**: `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC002/proposal/proposal_P-PH000-ST002-AC002-GATE-003_implementation-acceptance-disposition.md` (to be authored)
```

**Change 7 — Add TK005–TK007 + GATE-003 collapsed section** after TK004 detailed section and before the existing GATE-003 section:
```
### Tasks TK005–TK007 + GATE-003: Standard Implementation-Backed Gate Stack

- **TK005** (`P-PH000-ST002-AC002-TK005`) — Produce DEV-REPORT for TK002–TK004 implementation evidence.
- **TK006** (`P-PH000-ST002-AC002-TK006`) — Produce GATE-003 verification.
- **TK007** (`P-PH000-ST002-AC002-TK007`) — Produce GATE-003 gate-disposition proposal.
```

**Change 8 — Links Register**: Add rows:
```
| IMPLEMENTATION | Task Specification (TK002–TK004) | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC002/implementation/implementation_P-PH000-ST002-AC002_task-specification.md` |
| IMPLEMENTATION | GATE-002 Session Amendments Spec | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC002/implementation/implementation_P-PH000-ST002-AC002_gate-002-session-amendments.md` |
```

**Change 9 — Frontmatter**: Update `version` to `'1.5.0'` and `date` to `'2026-03-21'`

**Change 10 — Changelog**: Add:
```
| v1.5.0 | 2026-03-21 | Amendment | Added GATE-003 readiness stack (TK005 DEV-REPORT, TK006 Verification, TK007 gate-disposition proposal) per guideline_workspace_plan.md §VI.L. Added Gate-Disposition Proposal field to GATE-003 per §VI.C. Added Implementation Specification references to TK002/TK003/TK004 per CONV-011. Added implementation artifacts to Links Register. Source: GATE-002 session review. |
```

---

### SPEC-004 — Fix guideline_workspace_plan.md (7-State → 8-State)

| Field | Detail |
|:--|:--|
| Requirement Source | P-STD-002 v1.2.0 added `deferred` as the 8th canonical state; `guideline_workspace_plan.md` §III.A and §III.B still reference "seven canonical states" |
| Implementation Detail | See exact changes below |
| Target file(s) | `prompt/templates/consultant/workspace/guideline_workspace_plan.md` |
| Acceptance Criteria | §III.A and §III.B reference 8 states including `deferred`; deferral guidance updated; version bumped; changelog entry |
| Status | `open` |

**Change 1 — §III.A** (line 38): Replace:
```
- Register rows MAY use a context-appropriate subset of the seven canonical states defined by `P-STD-002-CLAUSE-001`: `planned`, `ready`, `in_progress`, `blocked`, `on_hold`, `completed`, `cancelled`.
```
With:
```
- Register rows MAY use a context-appropriate subset of the eight canonical states defined by `P-STD-002-CLAUSE-001`: `planned`, `ready`, `in_progress`, `blocked`, `on_hold`, `deferred`, `completed`, `cancelled`.
```

**Change 2 — §III.A** (line 40): Replace:
```
- Deliberate deferral/pause MUST be represented as `on_hold`; unrecoverable work-item termination MUST be represented as `cancelled`.
```
With:
```
- Deliberate pause MUST be represented as `on_hold`; explicit deferral to a future cycle MUST be represented as `deferred` (per `P-STD-002-CLAUSE-009`); unrecoverable work-item termination MUST be represented as `cancelled`.
```

**Change 3 — §III.B** (line 45): Replace:
```
- Task Register `Status` values for program work items MUST use the same `P-STD-002` canonical lifecycle authority and MAY use a context-appropriate subset of the seven canonical states.
```
With:
```
- Task Register `Status` values for program work items MUST use the same `P-STD-002` canonical lifecycle authority and MAY use a context-appropriate subset of the eight canonical states.
```

**Change 4 — Version bump**: Update frontmatter `version` to next minor (check current version first) and `date` to `2026-03-21`.

**Change 5 — Changelog**: Add:
```
| v1.18.0 | 2026-03-21 | Maintenance | §III.A and §III.B: Updated canonical state count from seven to eight and added `deferred` to the enum list, aligning with P-STD-002 v1.2.0 (CLAUSE-001, CLAUSE-009). Revised deferral/pause guidance to distinguish `on_hold` (deliberate pause) from `deferred` (future-cycle deferral). Source: P-PH000-ST002-AC002 GATE-002 session review. |
```

---

### SPEC-005 — Create AC001.8 Sub-Activity Plan

| Field | Detail |
|:--|:--|
| Requirement Source | GATE-002 session identified two process observations requiring tracked governance: (1) `external_review` scope enhancement in `guideline_workspace_analysis.md` §IV.B, (2) CONV-010 clarification in `guideline_workspace_implementation.md` |
| Implementation Detail | See exact changes below |
| Target file(s) | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.8/plan_T104-PH001-ST008-AC001.8.md` (NEW) |
| Acceptance Criteria | Activity plan exists at canonical path; task register with implementation-backed gate stack; scope covers both process observations |
| Status | `open` |

**Full file content**:

The plan MUST follow the AC001.7 exemplar structure (`plan_T104-PH001-ST008-AC001.7.md`) with:

- **Title**: `ANALYSIS & IMPLEMENTATION Guideline Micro-Amendments — external_review Scope & CONV-010 Clarification`
- **Purpose**: Address two process observations from the P-PH000-ST002-AC002 GATE-002 session: (1) amend `guideline_workspace_analysis.md` §IV.B to specify that `external_review` scope at a gate SHOULD include downstream task readiness assessment and plan-guideline compliance, and (2) amend `guideline_workspace_implementation.md` CONV-010 to clarify that "logical implementation scope" includes multi-task implementation phases sharing a common design-decision boundary.
- **Non-goal**: Does not modify any other ANALYSIS or IMPLEMENTATION subtype rules.
- **Activity ID**: `T104-PH001-ST008-AC001.8`
- **Depends On**: `T104-PH001-ST008-AC001.3` (IMPLEMENTATION guideline established)
- **Trigger**: P-PH000-ST002-AC002 GATE-002 session process observations

**Task Register** (6 rows):

| Task | Task ID | Name | Status | Owner | Depends On | Target | Reference | Action |
|:--|:--|:--|:--|:--|:--|:--|:--|:--|
| TK001 | `T104-PH001-ST008-AC001.8-TK001` | Create AC001.8 activity plan + register in ST008 stream plan | `completed` | LLM_Consultant | — | AC001.8 plan + ST008 stream plan | This plan file | AC001.8 plan authored; ST008 stream plan updated. |
| TK002 | `T104-PH001-ST008-AC001.8-TK002` | Implement guideline amendments | `planned` | LLM_Developer | TK001 | `guideline_workspace_analysis.md`, `guideline_workspace_implementation.md` | — | — |
| TK003 | `T104-PH001-ST008-AC001.8-TK003` | Produce DEV-REPORT | `planned` | LLM_Developer | TK002 | `dev-report/` | `guideline_workspace_dev-report.md` | — |
| TK004 | `T104-PH001-ST008-AC001.8-TK004` | Produce GATE-001 verification | `planned` | LLM_Reviewer | TK003 | `verification/` | `guideline_workspace_verification.md` | — |
| TK005 | `T104-PH001-ST008-AC001.8-TK005` | Produce GATE-001 gate-disposition proposal | `planned` | LLM_Consultant | TK004 | `proposal/` | `guideline_workspace_proposal.md` | — |
| GATE-001 | `T104-PH001-ST008-AC001.8-GATE-001` | Client acceptance of guideline micro-amendments | `planned` | Client | TK005 | Pass/fail | `guideline_workspace_plan.md` | — |

**TK002 Detailed Section** must specify:
- Scope: 2 files, 2 changes
- File 1: `guideline_workspace_analysis.md` §IV.B — add row or expand `external_review` lifecycle position to state: "When an `external_review` serves as a gate-readiness input for a consultation-only or implementation-backed gate, the review scope SHOULD include assessment of downstream task readiness and plan-guideline compliance for post-gate work."
- File 2: `guideline_workspace_implementation.md` CONV-010 — amend to: "One artifact per logical implementation scope. Logical implementation scope is scoped to a task-ID, a gate-remediation-cycle, or a multi-task implementation phase sharing a common design-decision boundary (e.g., tasks seeded by the same gate's GIR resolutions)."

**Links Register**: Link to this plan, ST008 stream plan, both target guidelines, and the P-PH000-ST002-AC002 session notes as trigger source.

---

### SPEC-006 — Register AC001.8 in ST008 Stream Plan

| Field | Detail |
|:--|:--|
| Requirement Source | `guideline_workspace_plan.md` §IV.D — when a dedicated Activity Plan exists, the Stream plan MUST retain a minimal contract stub |
| Implementation Detail | See exact changes below |
| Target file(s) | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/plan_T104-PH001-ST008.md` |
| Acceptance Criteria | AC001.8 row in Activity Register; contract stub in §III; Links Register entry; version bumped; changelog entry |
| Status | `open` |

**Change 1 — Activity Register**: Add row after AC001.7:
```
| AC001.8 | `T104-PH001-ST008-AC001.8` | ANALYSIS & IMPLEMENTATION Guideline Micro-Amendments | `planned` | LLM_Consultant | `T104-PH001-ST008-AC001.3` | Updated `guideline_workspace_analysis.md`, `guideline_workspace_implementation.md` | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.8/plan_T104-PH001-ST008-AC001.8.md` |
```

**Change 2 — §III Activities**: Add contract stub section after AC001.7:
```
#### Sub-Activity AC001.8: ANALYSIS & IMPLEMENTATION Guideline Micro-Amendments

**Trigger**: P-PH000-ST002-AC002 GATE-002 session identified process gaps in `external_review` scope definition and CONV-010 logical implementation scope definition.

**Purpose**: Amend `guideline_workspace_analysis.md` §IV.B (external_review downstream task assessment scope) and `guideline_workspace_implementation.md` CONV-010 (multi-task implementation scope clarification).

**Sub-Activity Plan**:
- `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.8/plan_T104-PH001-ST008-AC001.8.md`

**Success Criteria Checklist (summary)**:
- [ ] `AC001.8` plan exists and is linked from the stream plan
- [ ] `external_review` scope enhancement added to `guideline_workspace_analysis.md` §IV.B
- [ ] CONV-010 clarification added to `guideline_workspace_implementation.md`
- [ ] GATE-001 (implementation-backed) closes with client approval
```

**Change 3 — Links Register**: Add:
```
| Sub-Activity Plan | AC001.8 ANALYSIS & IMPLEMENTATION Guideline Micro-Amendments | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.8/plan_T104-PH001-ST008-AC001.8.md` |
```

**Change 4 — Frontmatter**: Version bump (current v1.15.0 → v1.16.0), date to `2026-03-21`

**Change 5 — Changelog**: Add:
```
| v1.16.0 | 2026-03-21 | Amendment | Added Sub-Activity `AC001.8` under AC001 for ANALYSIS and IMPLEMENTATION guideline micro-amendments. Trigger: P-PH000-ST002-AC002 GATE-002 session identified process gaps in external_review scope and CONV-010 logical implementation scope. Registered activity plan and contract stub. |
```

---

### SPEC-007 — Author AC002 SES002 Session Notes

| Field | Detail |
|:--|:--|
| Requirement Source | `guideline_workspace_notes.md` — session notes required for consultation sessions with decisions |
| Implementation Detail | See exact changes below |
| Target file(s) | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC002/snotes/snotes_P-PH000-ST002-AC002-SES002.md` (NEW); `prompt/artifacts/tasks/P/workspace/PH000/ST002/notes_P-PH000-ST002.md` (register update) |
| Acceptance Criteria | Session notes exist; decisions recorded; registered in stream notes register |
| Status | `open` |

**Session notes content requirements**:

- **Session ID**: `P-PH000-ST002-AC002-SES002`
- **Title**: `GATE-002 Independent Package Review & Session Amendments`
- **Date**: `2026-03-21`

**Decisions to record**:

| Decision ID | Decision | Category | Status | Owner | Date | Rationale |
|:--|:--|:--|:--|:--|:--|:--|
| `P-PH000-ST002-AC002-SES002-DEC001` | GIR-001 Option (a) — Adopt §V.E agent-role binding table | Design | Confirmed | Client | 2026-03-21 | Binding table remains coherent fit for v1.2.0 8-state lifecycle model |
| `P-PH000-ST002-AC002-SES002-DEC002` | GIR-002 Option (a) — P-STD-005 timeline UIDs + activity-only v1 population | Design | Confirmed | Client | 2026-03-21 | Consistent with P-STD-005 and avoids over-scoping AC003 v1 |
| `P-PH000-ST002-AC002-SES002-DEC003` | GIR-003 Option (a) all rows — Exclude 024/028/053, include 051 empty | Design | Confirmed | Client | 2026-03-21 | Low-cost audit alignment for 051; others have no data source |
| `P-PH000-ST002-AC002-SES002-DEC004` | Single unified task_specification for TK002–TK004 rather than per-task | Design | Confirmed | Client | 2026-03-21 | Shared GIR decision boundary; avoids redundant overlapping specs |
| `P-PH000-ST002-AC002-SES002-DEC005` | Keep separate tracked tasks (TK002/TK003/TK004) with shared spec reference | Design | Confirmed | Client | 2026-03-21 | Preserves deliverable-level tracking granularity; plan ≠ roadmap |
| `P-PH000-ST002-AC002-SES002-DEC006` | Process observations (external_review scope, CONV-010) registered as T104-PH001-ST008-AC001.8 | Governance | Confirmed | Client | 2026-03-21 | Separate from AC002 scope; tracked under T104 governance stream |
| `P-PH000-ST002-AC002-SES002-DEC007` | Guideline cleanup (7→8 state) executed within this session as micro-task | Governance | Confirmed | Client | 2026-03-21 | Simple maintenance; touched file identified during gate review |

**Process Observations**: Note the enhanced external_review prompt formulation as a process finding and reference AC001.8 as the downstream governance action.

**Notes Register Update**: Add row to `notes_P-PH000-ST002.md` §III Activity Notes Register:
```
| AC002 | `P-PH000-ST002-AC002-SES002` | GATE-002 Independent Package Review & Session Amendments | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC002/snotes/snotes_P-PH000-ST002-AC002-SES002.md` |
```
Version bump the notes register.

## IV. IMPLEMENTATION SEQUENCE

Recommended execution order (dependency-driven):

1. **SPEC-001** — Author Phase 1 task specification (no dependencies; creates a new file)
2. **SPEC-002** — Populate GATE-002 proposal (depends on SPEC-001 file existing for evidence index reference)
3. **SPEC-003** — Amend AC002 activity plan (depends on SPEC-001 file path for implementation spec references)
4. **SPEC-004** — Fix guideline_workspace_plan.md (independent; can run in parallel with SPEC-002/003 but sequenced here for clarity)
5. **SPEC-005** — Create AC001.8 sub-activity plan (independent of AC002 amendments)
6. **SPEC-006** — Register AC001.8 in ST008 stream plan (depends on SPEC-005 file existing)
7. **SPEC-007** — Author session notes + register update (last; captures all session decisions)

## V. REFERENCES

| Document | Path |
|:--|:--|
| Governing Plan (AC002) | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC002/plan_P-PH000-ST002-AC002.md` |
| GATE-002 Proposal | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC002/proposal/proposal_P-PH000-ST002-AC002-GATE-002_design-decision-disposition.md` |
| Implementation Requirements Analysis | `prompt/artifacts/tasks/P/workspace/PH000/ST002/analysis/analysis_P-PH000-ST002_status-system-implementation-requirements.md` |
| P-STD-002 | `prompt/artifacts/tasks/P/standard/standard_P-STD-002_program-status-standard.md` |
| P-STD-005 | `prompt/artifacts/tasks/P/standard/standard_P-STD-005_universal-id-specification.md` |
| Plan Guideline | `prompt/templates/consultant/workspace/guideline_workspace_plan.md` |
| Implementation Guideline | `prompt/templates/consultant/workspace/guideline_workspace_implementation.md` |
| Analysis Guideline | `prompt/templates/consultant/workspace/guideline_workspace_analysis.md` |
| Proposal Guideline | `prompt/templates/consultant/workspace/guideline_workspace_proposal.md` |
| Notes Guideline | `prompt/templates/consultant/workspace/guideline_workspace_notes.md` |
| ST008 Stream Plan | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/plan_T104-PH001-ST008.md` |
| AC001.7 Plan (exemplar) | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.7/plan_T104-PH001-ST008-AC001.7.md` |
| ST002 Notes Register | `prompt/artifacts/tasks/P/workspace/PH000/ST002/notes_P-PH000-ST002.md` |
| Notes Template (Activity Session) | `prompt/templates/consultant/workspace/template_workspace_notes_session_activity.md` |
| Task Specification Template | `prompt/templates/consultant/workspace/template_workspace_implementation_task-specification.md` |

## VI. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-03-21 | Initial | Session-level implementation specification for GATE-002 review completion. 7 SPEC items covering: Phase 1 task specification authoring, GATE-002 proposal consultant recommendation, AC002 plan amendment (GATE-003 readiness stack + implementation spec references), guideline 7→8 state fix, AC001.8 sub-activity creation and ST008 registration, and AC002 SES002 session notes. Source: GATE-002 independent package review consultation. |
