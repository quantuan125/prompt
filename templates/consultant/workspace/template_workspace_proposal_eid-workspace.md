---
artifact_type: 'PROPOSAL'
initiative_id: '[ID]'
initiative_code: '[CODE]'
phase: '[#]'
stream_id: '[SID-PH###-ST###]'
activity_id: '[SID-PH###-ST###-AC###]'
task_id: '[SID-PH###-ST###-AC###-TK###]'
version: '1.0.0'
date: 'YYYY-MM-DD'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: '[path to governing plan]'
analysis_reference: '[path to driving analysis, if applicable]'
target_document: '[path to target SSOT/standard, if applicable]'
target_section: '[section anchor, if applicable]'
purpose: 'E-ID workspace proposal for iterative candidate development'
---

# PROPOSAL: E-ID Workspace - [Scope/Title]

## I. EXECUTIVE SUMMARY

- Proposal purpose: [1-2 lines]
- Target outcome: [what this proposal unlocks]
- Current status: [draft / under_review / approved]

---

## II. CANDIDATE INVENTORY (WORKING INDEX)

Use this as the authoritative working index during consultation.

### A. Candidate Register

| Candidate ID | Category | Title | Source | Status | Body Ref | Notes |
|:--|:--|:--|:--|:--|:--|:--|
| [ID-001] | [type] | [title] | [source] | proposed | [III.A] | [note] |

Status values:
- `proposed`
- `existing`
- `rejected`
- `deferred`

---

## III. CANDIDATE BODIES / NORMATIVE DRAFT CONTENT

Write full bodies only for candidates that are `proposed` or `existing`.

### A. [Candidate ID] - [Title]

Context:
- [why this candidate exists]

Draft body:
- [full candidate text]

Consequences:
- (+) [positive]
- (+/-) [tradeoff]
- (-) [cost/risk]

---

## IV. DECISION RECORD INDEX AND BODIES (WHEN APPLICABLE)

Include this section only when the proposal introduces or updates DR artifacts.

### A. Decision Record Index

| DR ID | Type | Title | Status | Owner | Effective | Notes |
|:--|:--|:--|:--|:--|:--|:--|
| [DR-001] | [GDR/ADR] | [title] | proposed | Client | YYYY-MM-DD | [note] |

### B. Decision Record Bodies

#### [DR-001] [Title]

Context:
- [problem statement]

Decision:
- [decision statement]

Consequences:
- (+) [positive]
- (+/-) [tradeoff]
- (-) [negative]

---

## V. REFERENCES

| Document | Path |
|:--|:--|
| Governing Plan | `[plan_reference]` |
| Input Analysis | `[analysis_reference]` |
| Target Document | `[target_document]` |

---

## VI. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | YYYY-MM-DD | Initial | Initial template instantiation. |
