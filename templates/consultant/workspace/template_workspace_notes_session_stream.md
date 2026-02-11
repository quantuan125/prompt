---
artifact_type: 'NOTES'
notes_type: 'SESSION_STREAM'
initiative_id: '[INITIATIVE-ID]'
initiative_code: '[INITIATIVE-CODE]'
phase: '[PHASE-NUMBER]'
stream: '[ST###]'
session: '[SES###]'
version: '1.0.0'
date: 'YYYY-MM-DD'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
register_reference: '[path/to/stream/notes/register.md]'
plan_reference: '[path/to/stream/plan.md]'
raw_transcript_reference: '[path/to/raw/transcript OR —]'
---

<!--
Stream sessions capture cross-activity coordination within a stream. They MUST NOT duplicate activity-level decisions.
ID prefix rule: [INIT]-PH###-ST###-SES###-[TYPE][###]
-->

# STREAM SESSION NOTES: [INIT] ([CODE]) — PH### / ST### / SES### ([Title])

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
| `[INIT]-PH###-ST###-SES###-DP001` | [Topic] | [Outcome] | [Rationale] | [Evidence] |

---

## D. Decisions Captured (DEC Table)

| ID | Decision | Type | Status | Owner | Date | Rationale | Acceptance Signal | Evidence |
|:---|:---------|:-----|:-------|:------|:-----|:----------|:------------------|:---------|
| `[INIT]-PH###-ST###-SES###-DEC001` | [Decision] | [Type] | [Status] | Client | YYYY-MM-DD | [Rationale] | [Signal] | [Evidence] |

---

## E. Actions / Carry-Forward (ACT Table)

| ID | Action | Owner | Status |
|:---|:-------|:------|:-------|
| `[INIT]-PH###-ST###-SES###-ACT001` | [Action] | [Owner] | `pending` |

---

## F. Open Questions Register (OQ Table)

| ID | Topic | Question | Owner | Status | Needed By |
|:---|:------|:---------|:------|:-------|:----------|
| `[INIT]-PH###-ST###-SES###-OQ001` | [Topic] | [Question] | Client | Open | YYYY-MM-DD |

---

## G. Session Handoff Pack

- [Carry-forward note]

---

## H. Changelog

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | YYYY-MM-DD | Initial | Session notes created |

