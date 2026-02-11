---
artifact_type: 'PLAN'
planning_level: 'STREAM'
initiative_id: '[INITIATIVE-ID]'
initiative_code: '[INITIATIVE-CODE]'
phase: '[PHASE-NUMBER]'
stream_id: '[INIT-PH###-ST###]'
version: '1.0.0'
date: 'YYYY-MM-DD'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
governance_rules: 'prompt/templates/consultant/workspace/workspace_documentation_rules.md'
procedural_guideline: 'prompt/templates/consultant/workspace/guideline_workspace_plan.md'
parent_plan: '[path/to/phase/plan.md]'
---

# PLAN: [ID] ([CODE]) — Phase [#] / Stream [ST-ID]: [Stream Title]

## I. EXECUTIVE SUMMARY

**Purpose**: [1–3 sentences]

**Non-goal** (optional): [1–2 sentences]

---

## II. STREAM OUTLINE

**Stream ID**: `[INIT-PH###-ST###]`
**Objective**: [1–2 sentences]
**Execution Mode**: [PARALLEL\|SEQUENTIAL\|GATED]
**Depends On**: [— or prerequisite IDs]

**Context**:
- `[repo-relative path touched by this stream]`
- `[repo-relative path touched by this stream]`

### Activity Register

| Activity | Activity ID | Name | Status | Owner | Depends On | Deliverable | Reference |
|:--|:--|:--|:--|:--|:--|:--|:--|
| AC001 | `T###-PH###-ST###-AC###` | [Activity Name] | `planned` | LLM_Consultant | — | [Deliverable path(s)] | — |

---

<!--
Activities here are CONTRACT-LEVEL. Each includes Purpose, Deliverable, Scope, Task Register, and Success Criteria.
Implementation-level task decomposition belongs in standalone activity plans (see guideline_workspace_plan.md for trigger rule).
-->
## III. ACTIVITIES (HIGH-LEVEL)

#### Activity AC001: [Activity Title]

**Activity ID**: `T###-PH###-ST###-AC###`

**Purpose**: [Why this activity exists; what it unlocks]

**Deliverable**:
- `[path/to/deliverable.md]` — [Brief description]

**Scope**:
- In scope:
  - [Scope item]
- Out of scope:
  - [Scope item]

**Inputs Required** (optional):
- `[input path]` — [Why needed]

<!--
Tasks are the smallest registered unit. Steps (informal sub-bullets within tasks) are unregistered.
Status enums per guideline_workspace_plan.md §III.B.
-->
**Task Register**:

| Task ID | Description | Status | Action |
|:--|:--|:--|:--|
| `T###-PH###-ST###-AC###-TK001` | [Task description] | `planned` | — |

**Success Criteria Checklist**:
- [ ] [Criterion 1]
- [ ] [Criterion 2]

<!--
Role boundary:
  - LLM_Consultant authors contract-level intent (what + why)
  - LLM_Planner owns decomposition (how much)
  - LLM_Developer owns execution proof (how)
See T104-STD-001 CLAUSE-004 (pending).
-->

---

## IV. LINKS REGISTER

| Link Type | Target | Path |
|:--|:--|:--|
| Plan (this file) | [Stream Plan] | `[relative path]` |
| Plan | [Phase Plan] | `[relative path]` |
| Notes | [Stream Notes Register] | `[relative path]` |
| SSOT | [SPS] | `[relative path]` |
| SSOT | [Concept] | `[relative path]` |

---

## V. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | YYYY-MM-DD | Initial | Stream plan created |

