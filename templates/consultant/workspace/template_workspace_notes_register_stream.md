---
artifact_type: 'NOTES'
notes_type: 'REGISTER_STREAM'
initiative_id: '[INITIATIVE-ID]'
initiative_code: '[INITIATIVE-CODE]'
phase: '[PHASE-NUMBER]'
stream: '[ST###]'
version: '1.0.0'
date: 'YYYY-MM-DD'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: '[path/to/stream/plan.md]'
---

<!--
INDEX-ONLY: This file MUST NOT embed session bodies.
Register sessions and activity notes as they occur (JIT §5.1). Do NOT pre-register planned activities.
-->

# STREAM NOTES REGISTER: [INIT] ([CODE]) — Phase [#] / Stream [ST###]: [Stream Name]

## I. STREAM SUMMARY

**Stream**: [ST###]
**Scope**: [1–2 lines]
**Status**: `[planned|in_progress|completed|deferred]`

---

## II. STREAM-LEVEL SESSION NOTES REGISTER

| Session | Session ID | Title | Date | Notes File |
|:--|:--|:--|:--|:--|
| SES001 | `[INIT]-PH###-ST###-SES001` | [Session title] | YYYY-MM-DD | `[path/to/notes_<INIT>-PH###-ST###-SES###.md]` |

---

## III. ACTIVITY NOTES REGISTER

| Activity | Session ID | Name | Notes File |
|:--|:--|:--|:--|
| AC### | `[INIT]-PH###-ST###-AC###-SES###` | [Activity name] | `prompt/artifacts/tasks/[INIT]/workspace/PH###/ST###/notes_[INIT]-PH###-ST###-AC###-SES###.md` |

---

## IV. LINKS (PRIMARY)

- Stream plan: `[path/to/plan_<INIT>-PH###-ST###.md]`
- Phase plan: `[path/to/plan_<INIT>-PH###.md]`
- Phase notes register: `[path/to/notes_<INIT>-PH###.md]`
- Notes guideline: `prompt/templates/consultant/workspace/guideline_workspace_notes.md`

---

## V. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | YYYY-MM-DD | Initial | Stream notes register created |

