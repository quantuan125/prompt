---
artifact_type: 'NOTES'
notes_type: 'REGISTER_ACTIVITY'
initiative_id: '[INITIATIVE-ID]'
initiative_code: '[INITIATIVE-CODE]'
phase: '[PHASE-NUMBER]'
stream: '[ST###]'
activity_id: '[INIT-PH###-ST###-AC###]'
version: '1.0.0'
date: 'YYYY-MM-DD'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: '[path/to/activity/plan.md OR stream/plan.md]'
---

<!--
INDEX-ONLY: This file MUST NOT embed session bodies.
Activity registers are created when an activity has multiple sessions requiring separate indexing.
For single-session activities, the session notes file may be indexed directly from the stream notes register.
-->

# ACTIVITY NOTES REGISTER: [INIT] ([CODE]) — Phase [#] / Stream [ST###] / Activity [AC###]: [Activity Name]

## I. ACTIVITY SUMMARY

**Activity**: [AC###]
**Scope**: [1–2 lines]
**Status**: `[planned|in_progress|completed|deferred]`

---

## II. ACTIVITY-LEVEL SESSION NOTES REGISTER

| Session | Session ID | Title | Date | Notes File |
|:--|:--|:--|:--|:--|
| SES001 | `[INIT]-PH###-ST###-AC###-SES001` | [Session title] | YYYY-MM-DD | `[path/to/notes_<INIT>-PH###-ST###-AC###-SES###.md]` |

---

## III. LINKS (PRIMARY)

- Activity plan (or stream plan): `[path/to/plan_<INIT>-PH###-ST###-AC###.md OR plan_<INIT>-PH###-ST###.md]`
- Stream notes register: `[path/to/notes_<INIT>-PH###-ST###.md]`
- Notes guideline: `prompt/templates/consultant/workspace/guideline_workspace_notes.md`

---

## IV. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | YYYY-MM-DD | Initial | Activity notes register created |

