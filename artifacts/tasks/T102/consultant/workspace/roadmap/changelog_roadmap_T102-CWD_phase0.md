---
artifact_type: 'CHANGELOG'
initiative_id: 'T102'
initiative_code: 'CWD'
phase: '0'
target_artifact: 'prompt/artifacts/tasks/T102/consultant/workspace/roadmap/roadmap_T102-CWD_phase0.md'
version: '0.4.0'
date: '2026-01-24'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
---

# CHANGELOG

## Change History Overview

| Version | Date | Type | Summary |
|---------|------|------|---------|
| v0.4.0 | 2026-01-24 | Major | Completed Stream 3: Drafted `T102-STD-009` and `T102-ADR-009` baseline standards in the STD migration proposal |
| v0.3.2 | 2026-01-23 | Major | Added Authoring Guidelines section, standardized Task Register schema with `Action`, added Stream Context blocks, added Activity 2.4, and normalized status enums (`planned/deffered/complete/cancel`) |
| v0.3.1 | 2026-01-23 | Minor | Removed duplicated "Deliverable" column from Task Register tables and reordered sections |
| v0.3.0 | 2026-01-23 | Major | Inserted Stream 3 (STD-009/ADR-009 baseline), split parallel tracks into Stream 4A/4B, added Stream Objective/Scope and Activity Purpose/Success Criteria blocks, and marked OQ-001/OQ-002 complete |
| v0.2.0 | 2026-01-22 | Major | Refactored Stream/Activity registers to match T104 structure; added dependency columns; re-sequenced Streams 1–8; added Links/Open Questions registers |
| v0.1.0 | 2026-01-22 | Major | Initial Phase 0 roadmap created |

- **v0.4.0** (2026-01-24): Stream 3 Completion (STD Baseline)
  - Completed Activity 3.2: Drafted `T102-STD-009 (STD Token Standard)` in `proposal_T102-CWD_refactor_gdrs_into_std.md` with explicit Reference column and normative definition.
  - Completed Activity 3.3: Drafted `T102-ADR-009 (STD Token Normative Spec)` in `proposal_T102-CWD_refactor_gdrs_into_std.md` including full Specification clauses and Authoring Guidelines.
  - Updated Roadmap status for Stream 3 Activities to `completed`.

- **v0.3.2** (2026-01-23): Roadmap authoring hardening + proposal consolidation activity
  - Added `## IV. ROADMAP AUTHORING GUIDELINES` and migrated prior roadmap authoring comments into a dedicated normative section.
  - Standardized Stream/Activity/Task status enums to `planned` / `deffered` / `completed` / `cancelled` (wrapped in backticks in register tables).
  - Standardized all Activity Task Registers to include `Action` column with default `—`.
  - Added per-Stream `Context` blocks listing only repo-relative paths that Activities in the Stream touch.
  - Added Stream 2 Activity 2.4 for structure + content consolidation of `proposal_T102-CWD_refactor-adr-004-005.md` to ensure dual-ADR alignment under shared headings.
  - Renumbered post-roadmap sections to keep Links/Open Questions/Changelog after the new Authoring Guidelines section.

- **v0.3.1** (2026-01-23): Cleanup of duplicated table columns + layout refactor
  - Removed "Deliverable" column from Task Register indexes for each activity to reduce redundancy.
  - Added "**Task Register**:" heading above activity task tables.
  - Reordered activity sections: moved the Task Register block above the "**Success Criteria Checklist**:" within each activity for improved readability.

- **v0.3.0** (2026-01-23): Stream/Activity contract hardening + STD token baseline sequencing
  - Inserted Stream 3: `STD` token baseline work (`T102-STD-009` + `T102-ADR-009`) and initialization of `proposal_T102-CWD_refactor_gdrs_into_std.md`
  - Split the prior ADR tracks into explicit parallel streams: Stream 4A (ADR-004 track) and Stream 4B (ADR-005 track)
  - Added `Objective` and `Scope` blocks under each Stream heading
  - Added `Purpose` and `Success Criteria Checklist` under every Activity heading; standardized Activity deliverables to repo-relative path-only
  - Marked Open Questions `OQ-001` and `OQ-002` as complete (resolved)

- **v0.2.0** (2026-01-22): Refactored registers + sequencing
  - Added `Execution Mode` + `Depends On` columns to Stream Register and embedded the “Parallelism & Dependencies Standard” as a markdown comment
  - Added Activity Register (explicitly excludes `Execution Mode`/`Depends On` for now)
  - Re-sequenced Streams per client directive (Stream 1 initialization → Stream 2 prep → Stream 3/4 ADR tracks → Stream 5 apply → Streams 6–8 scaffold)
  - Replaced per-activity bullet task lists with Task Register tables
  - Added Links Register + Open Questions Register + Changelog pointer

- **v0.1.0** (2026-01-22): Initial roadmap created
  - Established Phase 0 intent for STD + ADR governance realignment
