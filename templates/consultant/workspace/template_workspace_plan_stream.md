---
artifact_type: 'PLAN'
planning_level: 'STREAM'
initiative_id: '[INITIATIVE-ID]'
initiative_code: '[INITIATIVE-CODE]'
phase: '[PHASE-NUMBER]'
stream_id: '[INIT-PH###-ST###]'
version: '1.0.1'
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

<!-- Use canonical P-STD-002 work-item states per guideline_workspace_plan.md §III.A. -->
| Activity | Activity ID | Name | Status | Owner | Depends On | Deliverable | Reference |
|:--|:--|:--|:--|:--|:--|:--|:--|
| AC001 | `T###-PH###-ST###-AC###` | [Activity Name] | `planned` | LLM_Consultant | — | [Deliverable(s) path(s)] | [Activity plan link or '—'] |

---

<!--
Activities here are CONTRACT-LEVEL.
  - If no standalone Activity Plan exists, include the Task Register here.
  - If a standalone Activity Plan exists, keep only the contract stub here (Purpose/Deliverable/Scope/Inputs + short Success Criteria summary) and omit the Task Register to avoid drift.
-->
## III. ACTIVITIES (HIGH-LEVEL)

### Activity AC001: [Activity Title]

**Activity ID**: `T###-PH###-ST###-AC###`

**Purpose**: [Why this activity exists; what it unlocks]

**Deliverable**:
- `[path/to/deliverable.md]` — [Brief description]

**Scope**:
- In scope:
  - [Scope item]
- Out of scope:
  - [Scope item]

**Activity Plan** (optional, recommended when detailed decomposition is needed):
- `[path/to/activity/plan.md]` — MUST match Activity Register `Reference` when present

**Inputs Required** (optional):
- `[input path]` — [Why needed]

<!--
Tasks are the smallest registered unit. Steps (informal sub-bullets within tasks) are unregistered.
Use canonical P-STD-002 work-item states per guideline_workspace_plan.md §III.B.

ANTI-DRIFT:
  - If `Activity Plan` is present (not `—`), DO NOT duplicate a full Task Register here.
  - Keep only the contract stub (Purpose/Deliverable/Scope/Inputs) + a short Success Criteria summary.
-->
**Task Register** (omit when Activity Plan exists):

| Task ID | Description | Status | Action |
|:--|:--|:--|:--|
| `T###-PH###-ST###-AC###-TK001` | [Task description] | `planned` | — |

**Success Criteria Checklist (summary)**:
- [ ] [Criterion 1]
- [ ] [Criterion 2]

<!--
Sub-Activities (AC00x.x):
  - Use only for remediation (parallel drift / higher-authority mandatory update) per guideline.
  - Sub-Activities are NOT listed in the Activity Register.
  - If a standalone plan exists, link it inline (no register row exists for sub-activities).
-->
#### Sub-Activity AC001.1: [Sub-Activity Title] (optional remediation)

**Trigger**: [parallel implementation drift | higher-authority mandatory update]

**Purpose**: [1–2 sentences]

**Sub-Activity Plan** (optional):
- `[path/to/sub-activity/plan.md]`

**Success Criteria Checklist (summary)**:
- [ ] [Criterion 1]

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
| v1.0.1 | YYYY-MM-DD | Amendment | Register comments updated to defer to `P-STD-002` canonical work-item states. |
| v1.0.0 | YYYY-MM-DD | Initial | Stream plan created |
