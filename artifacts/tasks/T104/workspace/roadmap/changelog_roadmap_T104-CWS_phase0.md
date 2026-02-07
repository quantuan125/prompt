# CHANGELOG

## Change History Overview

| Version | Date | Type | Summary |
|---------|------|------|---------|
| v1.3.0 | 2026-01-24 | Major | Standardized roadmap authoring structure (Stream 3+ Context/Scope/Task Registers/Success Criteria), extracted procedural guideline, and reconciled Stream 2 statuses (2.4 deferred) |
| v1.2.0 | 2026-01-18 | Major | Added dependency notation (Execution Mode/Depends On), clarified Stream parallelism, aligned RES-001 report naming, and updated template roadmap |
| v1.1.0 | 2026-01-17 | Major | Added T104-RES-001 research stream and reordered Phase 0 streams |
| v1.0.0 | 2026-01-17 | Major | Initial creation of T104 Phase 0 initiative roadmap |

- **v1.3.0** (2026-01-24): Standardized roadmap authoring structure and extracted procedural guideline
  - Standardized Stream/Activity register statuses to T102-style enums (`planned`, `deffered`, `completed`, `cancelled`) and wrapped statuses in backticks
  - Reconciled Stream 2 status to `completed` with Activity 2.4 explicitly `deffered` (client-directed)
  - Added Stream-level `Context` blocks and Activity-level `Scope` blocks for Streams 3–7
  - Replaced Stream 3 “Task List” with Task Registers and added Success Criteria checklists across Streams 3–7
  - Added missing Activity 3.3 body section (previously register-only)
  - Created `prompt/templates/consultant/workspace/guideline_workspace_roadmap.md` and referenced it from the roadmap (reduced embedded authoring rules)

- **v1.2.0** (2026-01-18): Added dependency notation (Execution Mode/Depends On), clarified Stream parallelism, aligned RES-001 report naming, and updated template roadmap
  - Added the “Parallelism & Dependencies Standard” block to the roadmap
  - Updated Stream Register + Activity Register schemas to include `Execution Mode` and `Depends On`
  - Clarified Stream 2 runs in parallel with Streams 3–4 (scaffolding only; research informs Phase 1 finalization)
  - Marked Activity 2.1 as Complete and aligned RES-001 report filename to `*_agentic-workspace-assessment.md`
  - Updated Stream 6 to include actual `template_workspace_roadmap.md` updates (parallel standardization)

- **v1.1.0** (2026-01-17): Added T104-RES-001 research stream and reordered Phase 0 streams
  - Added Stream 2 “Research Commission (End-to-End)” with hard gate before SSOT scaffolding
  - Updated Activity 3.1 to include SPS III.A (problem framing) in `sps_T104-CWS.md` skeleton scope
  - Updated registers and Links Register with planned research/analysis deliverables

- **v1.0.0** (2026-01-17): Initial creation of T104 Phase 0 initiative roadmap
  - Established Phase → Stream → Activity → Task structure and heading semantics
  - Locked decisions: SSOT location (`prompt/artifacts/tasks/T104/ssot/`), `notes_` prefix, separate `changelog_` files, add `T104E (CHANGELOG)`
