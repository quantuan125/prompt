---
artifact_type: 'PLAN'
planning_level: 'ACTIVITY'
initiative_id: '[INITIATIVE-ID]'
initiative_code: '[INITIATIVE-CODE]'
phase: '[PHASE-NUMBER]'
stream_id: '[INIT-PH###-ST###]'
activity_id: '[INIT-PH###-ST###-AC### or INIT-PH###-ST###-AC###.#]'
version: '1.0.0'
date: 'YYYY-MM-DD'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
governance_rules: 'prompt/templates/consultant/workspace/workspace_documentation_rules.md'
parent_plan: '[path/to/stream/plan.md]'
---

<!--
SKELETON / WORKING DRAFT:
  This template defines the structural units (Task as registered unit, Step as informal sub-task execution unit).
  Full Planner-level decomposition rules are deferred to a future initiative.
-->

<!--
Trigger rule:
  A standalone activity plan SHOULD be created when:
    (a) the activity has ≥5 tasks, OR
    (b) tasks require detailed step decomposition, OR
    (c) the activity scope exceeds what can be captured in the stream plan's contract-level section.
  See T104-STD-001 CLAUSE-006 (pending).
-->

# PLAN: [ID] ([CODE]) — Phase [#] / Stream [ST-ID] / Activity [AC-ID]: [Activity Title]

## I. EXECUTIVE SUMMARY

**Purpose**: [1–3 sentences]

**Non-goal** (optional): [1–2 sentences]

---

## II. ACTIVITY OUTLINE

**Activity ID**: `[INIT-PH###-ST###-AC### or INIT-PH###-ST###-AC###.#]`
**Objective**: [1–2 sentences]
**Execution Mode**: [PARALLEL\|SEQUENTIAL\|GATED]
**Depends On**: [— or prerequisite IDs]

**Context**:
- `[repo-relative path touched by this activity]`
- `[repo-relative path touched by this activity]`

<!--
Task Register:
  Tasks are the smallest REGISTERED unit.
  Status enums per guideline_workspace_plan.md §III.B.
-->
### Task Register

| Task | Task ID | Name | Status | Owner | Depends On | Target | Reference | Action |
|:--|:--|:--|:--|:--|:--|:--|:--|:--|
| TK001 | `T###-PH###-ST###-AC###-TK001` | [Task name] | `planned` | LLM_Developer | — | [Target] | — | — |

---

<!--
Tasks are the smallest REGISTERED unit. Each Task MAY contain informal Steps (numbered sub-bullets) for execution guidance.
Steps have no ID pattern and are not registered.
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
- `[input path]` — [Why needed]

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
| v1.0.0 | YYYY-MM-DD | Initial | Activity plan created |
