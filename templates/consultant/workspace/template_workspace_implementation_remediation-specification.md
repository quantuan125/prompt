---
artifact_type: 'IMPLEMENTATION'
implementation_type: 'remediation_specification'
initiative_id: '{{INITIATIVE_ID}}'
initiative_code: '{{INITIATIVE_CODE}}'
phase: '{{PHASE}}'
stream_id: '{{STREAM_ID}}'
activity_id: '{{ACTIVITY_ID}}'
gate_id: '{{GATE_ID}}'
task_id: '{{TASK_ID}}'
version: '1.0.0'
date: '{{DATE}}'
status: 'draft'
author: '{{AUTHOR_ROLE}}'
decision_owner_role: 'Client'
plan_reference: '{{PLAN_PATH}}'
verification_reference: '{{VERIFICATION_PATH}}'
proposal_reference: '{{PROPOSAL_PATH}}'
purpose: '{{PURPOSE}}'
---

# IMPLEMENTATION (Remediation Specification): {{TITLE}}

## I. PURPOSE & AUTHORITY
- Purpose: [what this remediation specification covers]
- Authority chain: Plan authorizes work (task_id) -> This artifact specifies HOW ->
  Dev-report records execution -> Verification re-assesses
- Audience: LLM_Developer (primary), LLM_Reviewer (re-assessment input)
- This artifact does NOT hold a GDR. Gate decision is recorded in the
  gate_disposition proposal.

## II. REMEDIATION SCOPE
- Gate: [gate_id]
- Trigger: RECYCLE verdict from [verification_reference]
- Governing plan task: [task_id]
- Findings addressed: [list of FINDING-### IDs from verification]

## III. REMEDIATION ITEMS

### REM-001 — [Title]

| Field | Detail |
|:--|:--|
| Finding Reference | [FINDING-### from verification] |
| Revision Deliverable | [what must be produced or changed] |
| Expected Format | [schema, structure, output format] |
| Acceptance Criteria | [what reviewer checks during re-assessment] |
| Resolution Status | `open` / `resolved` |

#### Implementation Detail

[detailed HOW]

[Repeat for each remediation item]

## IV. IMPLEMENTATION SEQUENCE
[Recommended execution order]

## V. REFERENCES

| Document | Path |
|:--|:--|
| Governing Plan | [plan_reference] |
| Verification | [verification_reference] |
| Gate-Disposition Proposal | [proposal_reference] |

## VI. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
