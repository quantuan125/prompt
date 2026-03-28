---
artifact_type: 'PLAN'
planning_level: 'ACTIVITY'
initiative_id: '[INITIATIVE-ID]'
initiative_code: '[INITIATIVE-CODE]'
phase: '[PHASE-NUMBER]'
stream_id: '[INIT-PH###-ST###]'
activity_id: '[INIT-PH###-ST###-AC### or INIT-PH###-ST###-AC###.#]'
version: '1.4.0'
date: '2026-03-28'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
governance_rules: 'prompt/templates/consultant/workspace/workspace_documentation_rules.md'
parent_plan: '[path/to/stream/plan.md]'
---

<!--
SKELETON / WORKING DRAFT:
  This template defines the structural units (Task as registered unit, optional dotted Sub-Task as registered decomposition, and Step as informal execution guidance).
  Full Planner-level decomposition rules are deferred to a future initiative.
-->

<!--
Trigger rule:
  A standalone activity plan SHOULD be created when:
    (a) the activity has >=5 tasks, OR
    (b) tasks require detailed step decomposition, OR
    (c) the activity scope exceeds what can be captured in the stream plan's contract-level section.
  See T104-STD-001 CLAUSE-006 (pending).
-->

# PLAN: [ID] ([CODE]) - Phase [#] / Stream [ST-ID] / Activity [AC-ID]: [Activity Title]

## I. EXECUTIVE SUMMARY

**Purpose**: [1-3 sentences]

**Non-goal** (optional): [1-2 sentences]

---

## II. ACTIVITY OUTLINE

**Activity ID**: `[INIT-PH###-ST###-AC### or INIT-PH###-ST###-AC###.#]`
**Objective**: [1-2 sentences]
**Execution Mode**: [PARALLEL|SEQUENTIAL|GATED]
**Depends On**: [- or prerequisite IDs]

**Context**:
- `[repo-relative path touched by this activity]`
- `[repo-relative path touched by this activity]`

<!--
Task Register:
  Tasks are the primary registered unit. Registered dotted Sub-Tasks (TK###.n) MAY be used when guideline_workspace_plan.md §IV.E criteria are met.
  Use canonical P-STD-002 work-item states per guideline_workspace_plan.md §III.B.
  A context-appropriate subset is allowed; do not invent local workspace status values.
-->
### Task Register

| Task | Task ID | Name | Status | Owner | Depends On | Target | Reference | Action |
|:--|:--|:--|:--|:--|:--|:--|:--|:--|
| TK001 | `T###-PH###-ST###-AC###-TK001` | [Task name] | `planned` | LLM_Developer | - | [Target] | - | - |
| TK001.1 | `T###-PH###-ST###-AC###-TK001.1` | [Sub-task name] | `planned` | LLM_Developer | TK001 | [Target] | - | - |
| TK002 | `T###-PH###-ST###-AC###-TK002` | [Last implementation task] | `planned` | LLM_Developer | TK001 | [Target] | - | - |
| TK003 | `T###-PH###-ST###-AC###-TK003` | Produce dev-report for GATE-001 | `planned` | LLM_Developer | TK002 | `dev-report/` | `guideline_workspace_dev-report.md` | - |
| TK004 | `T###-PH###-ST###-AC###-TK004` | Produce GATE-001 verification | `planned` | LLM_Reviewer (preferred future-state primary) / LLM_Consultant (currently authorized secondary) | TK003 | `verification/` | `guideline_workspace_verification.md` | - |
| TK005 | `T###-PH###-ST###-AC###-TK005` | Produce GATE-001 gate-disposition proposal | `planned` | LLM_Consultant | TK004 | `proposal/` | `guideline_workspace_proposal.md` | - |
| TK006 | `T###-PH###-ST###-AC###-TK006` | Produce GATE-001 external review | `planned` | LLM_Subconsultant | TK005 | `analysis/` | `guideline_workspace_analysis.md` | - |
| GATE-001 | `T###-PH###-ST###-AC###-GATE-001` | Gate: [description] | `planned` | Client | TK006 | Pass/fail | `guideline_workspace_plan.md` | - |

---

<!--
Tasks are the primary REGISTERED unit. Registered dotted Sub-Tasks MAY be used when tracked decomposition is required. Steps remain informal execution guidance only.
Steps have no ID pattern, no register row, and no directory implications.
-->
## III. TASKS (DETAILED)

### Task TK001: [Task Title]

**Task ID**: `T###-PH###-ST###-AC###-TK001`

**Purpose**: [Why this task exists]

**Deliverable**:
- [Deliverable artifact/path]

**Scope**:
- In scope:
  - [Scope item]
- Out of scope:
  - [Scope item]

**Inputs Required**:
- `[input path]` - [Why needed]

**Steps**:
1. [Step]
2. [Step]

**Success Criteria**:
- [ ] [Criterion 1]
- [ ] [Criterion 2]

---

### Task TK001.1: [Sub-Task Title]

**Task ID**: `T###-PH###-ST###-AC###-TK001.1`

**Purpose**: [Why this tracked decomposition exists]

**Deliverable**:
- [Deliverable artifact/path]

**Scope**:
- In scope:
  - [Scope item]
- Out of scope:
  - [Scope item]

**Inputs Required**:
- `[input path]` - [Why needed]

**Steps**:
1. [Step]
2. [Step]

**Success Criteria**:
- [ ] [Criterion 1]
- [ ] [Criterion 2]

---

<!--
Gate-Readiness Stack:
  When an activity includes a gate, the task register and detailed sections
  MUST follow the Gate-Readiness Stack pattern per guideline_workspace_plan.md §VI.L.
  Implementation-backed sequence: implementation tasks → DEV-REPORT → VERIFICATION → gate-disposition → external review → gate.
  Consultation-only sequence: consultant-owned preparatory tasks → gate-disposition → external review → gate.
  Consultation-only gates omit both DEV-REPORT and verification.
  External review (LLM_Subconsultant) is mandatory for all gates.
-->

### Task TK003: Produce Dev-Report for GATE-001

**Task ID**: `T###-PH###-ST###-AC###-TK003`

**Purpose**: Capture bounded implementation evidence for the gate review package.

**Deliverable**:
- `[dev-report path per guideline_workspace_dev-report.md §VII]`

**Steps**:
1. Record implementation outcomes for TK001–TK002
2. Produce validation evidence per `guideline_workspace_dev-report.md` §VI

**Success Criteria**:
- [ ] Dev-report exists with required sections per `guideline_workspace_dev-report.md` §V

---

### Task TK004: Produce GATE-001 Verification

**Task ID**: `T###-PH###-ST###-AC###-TK004`

**Purpose**: Produce independent verifier evidence for the gate review.

**Deliverable**:
- `[verification path per guideline_workspace_verification.md §XI]`

**Steps**:
1. Perform evidence-first verification per `guideline_workspace_verification.md` §V
2. Record verifier verdict in Gate Recommendation section

**Success Criteria**:
- [ ] Verification artifact exists with verifier verdict

---

### Task TK005: Produce GATE-001 Gate-Disposition Proposal

**Task ID**: `T###-PH###-ST###-AC###-TK005`

**Purpose**: Package the gate decision items and prepare the GDR for client disposition.

**Deliverable**:
- `[proposal path per guideline_workspace_proposal.md §IX]`

**Steps**:
1. Author gate-disposition proposal per `guideline_workspace_proposal.md` §V.B
2. Populate GDR fields in pending state per `guideline_workspace_proposal.md` §VII.D

**Success Criteria**:
- [ ] Gate-disposition proposal exists with GDR section in pending state

---

### Task TK006: Produce GATE-001 External Review

**Task ID**: `T###-PH###-ST###-AC###-TK006`

**Purpose**: Produce an independent second-opinion quality audit of the gate package before client disposition.

**Deliverable**:
- `[external review path per guideline_workspace_analysis.md §VII]`

**Steps**:
1. Review the gate-disposition proposal and all evidence artifacts per `guideline_workspace_analysis.md` §IV.B
2. Assess evidence integrity, role-boundary compliance, plan-guideline compliance, and downstream task readiness
3. Record findings and recommendation in the external review analysis

**Success Criteria**:
- [ ] External review analysis exists with findings and recommendation
- [ ] Main `LLM_Consultant` has reviewed the external review findings

---

### GATE-001: [Gate Title]

**Gate ID**: `T###-PH###-ST###-AC###-GATE-001`

**Entry Criteria**:
- TK001 through TK006 are completed
- Verification artifact exists with a verifier verdict
- Gate-disposition proposal exists with a populated GDR (pending state)
- External review analysis exists with findings reviewed by main `LLM_Consultant`

**Reviewer**: Client

**Exit Criteria**:
- Client records decision in the GDR per `guideline_workspace_proposal.md` §VII.D
- Gate status transitions per verdict/decision mapping

**Gate-Disposition Proposal**: `[repo-relative path to gate_disposition proposal]`
**External Review**: `[repo-relative path to external_review analysis]`

---

## IV. LINKS REGISTER

| Link Type | Target | Path |
|:--|:--|:--|
| Plan (this file) | [Activity Plan] | `[relative path]` |
| Plan | [Stream Plan] | `[relative path]` |
| Notes | [Activity Notes Register] | `[relative path]` |

---

## V. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.4.0 | 2026-03-28 | Amendment | Added mandatory external review task (`LLM_Subconsultant`) to Gate-Readiness Stack example in Task Register (TK006) and Tasks (Detailed). Updated HTML guidance comment. Updated GATE-001 entry criteria to include external review. Source: T102-PH001-ST002-AC000-TK000 consultation; `guideline_workspace_plan.md` §VI.L v1.20.0. |
| v1.3.0 | 2026-03-16 | Amendment | Updated Gate-Readiness Stack guidance comment to distinguish implementation-backed and consultation-only gate sequences. Consultation-only gates now explicitly omit DEV-REPORT and verification. Source: P-PH000-ST002-AC002 Gate 001 consultation. |
| v1.2.0 | 2026-03-15 | Amendment | Added Gate-Readiness Stack example (TK003 dev-report → TK004 verification → TK005 gate-disposition → GATE-001) to Task Register and Tasks (Detailed) sections. Added `Gate-Disposition Proposal` field to gate construct example. Source: T104-PH001-ST008-AC001.2; `guideline_workspace_plan.md` §VI.L. |
| v1.1.0 | YYYY-MM-DD | Amendment | Template updated to distinguish registered Tasks/Sub-Tasks from informal Steps and to show a dotted sub-task example. |
| v1.0.1 | YYYY-MM-DD | Amendment | Status guidance note updated to defer to `P-STD-002` canonical work-item states. |
| v1.0.0 | YYYY-MM-DD | Initial | Activity plan created |
