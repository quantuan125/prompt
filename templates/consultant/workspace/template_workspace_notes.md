<!--
DEPRECATED: This template has been superseded by per-type templates as of 2026-02-11.
See guideline_workspace_notes.md §7 (Template Inventory) for the full template inventory.
Replacements:
  - template_workspace_notes_register_phase.md
  - template_workspace_notes_register_stream.md
  - template_workspace_notes_register_activity.md
  - template_workspace_notes_session_phase.md
  - template_workspace_notes_session_stream.md
  - template_workspace_notes_session_activity.md
-->

---
artifact_type: 'NOTES'
initiative_id: '[INITIATIVE_ID]'
initiative_code: '[INITIATIVE_CODE]'
phase: '[PHASE_NUMBER]'
stream: '[STREAM_ID]'
version: '1.0.0'
date: 'YYYY-MM-DD'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: '[path/to/plan_file.md]'
---

# STREAM NOTES REGISTER: [INITIATIVE] — Phase [#] / Stream [ST###]

<!--
AUTHORING GUIDELINES
See: prompt/templates/consultant/workspace/guideline_workspace_notes.md
-->

## I. STREAM SUMMARY

**Stream**: [ST###]
**Scope**: [1–2 lines]
**Status**: `[planned|in_progress|completed|deferred]`

---

## II. STREAM-LEVEL SESSION NOTES REGISTER

| Session | Session ID | Title | Date | Notes File |
|:--|:--|:--|:--|:--|

---

## III. ACTIVITY NOTES REGISTER

| Activity | Session ID | Name | Status | Notes File |
|:--|:--|:--|:--|:--|
| AC### | `[INIT]-PH###-ST###-AC###-SES###` | [Activity name] | `[planned|in_progress|completed|deferred]` | `prompt/artifacts/tasks/[INIT]/workspace/PH###/ST###/notes_[INIT]-PH###-ST###-AC###-SES###.md` |
