---
artifact_type: 'PLAN'
planning_level: 'ACTIVITY'
initiative_id: '[INITIATIVE-ID]'
initiative_code: '[INITIATIVE-CODE]'
phase: '[PHASE-NUMBER]'
stream_id: '[INIT-PH###-ST###]'
activity_id: '[INIT-PH###-ST###-AC### or INIT-PH###-ST###-AC###.#]'
version: '1.1.0'
date: 'YYYY-MM-DD'
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
| v1.1.0 | YYYY-MM-DD | Amendment | Template updated to distinguish registered Tasks/Sub-Tasks from informal Steps and to show a dotted sub-task example. |
| v1.0.1 | YYYY-MM-DD | Amendment | Status guidance note updated to defer to `P-STD-002` canonical work-item states. |
| v1.0.0 | YYYY-MM-DD | Initial | Activity plan created |
