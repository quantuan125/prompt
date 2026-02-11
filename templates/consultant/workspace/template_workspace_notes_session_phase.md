---
artifact_type: 'NOTES'
notes_type: 'SESSION_PHASE'
initiative_id: '[INITIATIVE-ID]'
initiative_code: '[INITIATIVE-CODE]'
phase: '[PHASE-NUMBER]'
session: '[SES###]'
version: '1.0.0'
date: 'YYYY-MM-DD'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
register_reference: '[path/to/phase/notes/register.md]'
plan_reference: '[path/to/phase/plan.md]'
raw_transcript_reference: '[path/to/raw/transcript OR —]'
---

<!--
Phase sessions capture cross-stream coordination. They MUST NOT duplicate stream-level or activity-level decisions.
ID prefix rule: [INIT]-PH###-SES###-[TYPE][###] (e.g., T104-PH001-SES001-DEC001)
-->

# PHASE SESSION NOTES: [INIT] ([CODE]) — PH### / SES### ([Title])

## A. Agenda / Topics

1. [Topic]
2. [Topic]

---

## B. Narrative Summary (Minutes-Style)

[Minutes-style summary.]

---

## C. Discussion Points (DP Table)

| ID | Topic | Outcome | Rationale | Evidence |
|:---|:------|:--------|:----------|:---------|
| `[INIT]-PH###-SES###-DP001` | [Topic] | [Outcome] | [Rationale] | [Evidence] |

---

## D. Decisions Captured (DEC Table)

| ID | Decision | Type | Status | Owner | Date | Rationale | Acceptance Signal | Evidence |
|:---|:---------|:-----|:-------|:------|:-----|:----------|:------------------|:---------|
| `[INIT]-PH###-SES###-DEC001` | [Decision] | [Type] | [Status] | Client | YYYY-MM-DD | [Rationale] | [Signal] | [Evidence] |

---

## E. Actions / Carry-Forward (ACT Table)

| ID | Action | Owner | Status |
|:---|:-------|:------|:-------|
| `[INIT]-PH###-SES###-ACT001` | [Action] | [Owner] | `pending` |

---

## F. Open Questions Register (OQ Table)

| ID | Topic | Question | Owner | Status | Needed By |
|:---|:------|:---------|:------|:-------|:----------|
| `[INIT]-PH###-SES###-OQ001` | [Topic] | [Question] | Client | Open | YYYY-MM-DD |

---

## G. Session Handoff Pack

- [Carry-forward note]

---

## H. Changelog

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | YYYY-MM-DD | Initial | Session notes created |

