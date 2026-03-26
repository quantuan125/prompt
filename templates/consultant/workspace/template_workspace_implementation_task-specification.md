---
artifact_type: 'IMPLEMENTATION'
implementation_type: 'task_specification'
initiative_id: '{{INITIATIVE_ID}}'
initiative_code: '{{INITIATIVE_CODE}}'
phase: '{{PHASE}}'
stream_id: '{{STREAM_ID}}'
activity_id: '{{ACTIVITY_ID}}'
task_id: '{{TASK_ID}}'
version: '1.0.0'
date: '{{DATE}}'
status: 'draft'
author: '{{AUTHOR_ROLE}}'
decision_owner_role: 'Client'
plan_reference: '{{PLAN_PATH}}'
execution_audience: 'developer'
purpose: '{{PURPOSE}}'
---

# IMPLEMENTATION (Task Specification): {{TITLE}}

## I. PURPOSE & AUTHORITY
- Purpose: [what this task specification covers]
- Authority chain: Plan authorizes work (task_id) -> This artifact specifies HOW ->
  Dev-report records execution
- Audience: [LLM_Developer / designated agentic executor / LLM_Consultant when `execution_audience: 'consultant'`]
- This artifact does NOT hold a GDR. Gate decisions (if applicable) are recorded
  in gate_disposition proposals.

## II. TASK SCOPE
- Governing plan task: [task_id]
- Trigger: [task complexity rationale]
- Deliverable contract: [from plan]

## III. SPECIFICATION ITEMS

### SPEC-001 — [Title]

| Field | Detail |
|:--|:--|
| Requirement Source | [plan task step or amendment reference] |
| Target file(s) | [deliverable or changed surface] |
| Required end-state posture | [what must be true after implementation] |
| Explicit non-target / do-not-change constraints | [surfaces or changes that are out of bounds] |
| Validation check | [how the executor confirms completion] |
| Blocking ambiguity rule | [when to stop and escalate instead of inferring] |
| Status | `open` / `resolved` |

#### Implementation Detail

[detailed HOW]

[Repeat for each specification item]

## IV. IMPLEMENTATION SEQUENCE
[Recommended execution order]

## V. REFERENCES

| Document | Path |
|:--|:--|
| Governing Plan | [plan_reference] |

## VI. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
