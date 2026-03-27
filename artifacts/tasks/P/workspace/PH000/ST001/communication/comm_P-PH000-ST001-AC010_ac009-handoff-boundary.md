---
artifact_type: 'COMMUNICATION'
from_initiative: 'P'
from_stream: 'P-PH000-ST001-AC009'
to_initiative: 'P'
to_owner: 'P ST001 AC010 consultant-owned commissioning flow'
date: '2026-03-27'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
target_role: 'P ST001 AC010 LLM_Consultant / future execution roles'
priority: 'HIGH'
subject: 'AC009 -> AC010 metadata retrofit handoff boundary and non-reopen contract'
source_analysis: 'prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/analysis/analysis_P-PH000-ST001-AC009-TK001_p-std-001-amendment-map.md'
---

# COMMUNICATION: AC009 -> AC010 — Metadata Retrofit Handoff Boundary

## I. PURPOSE

This communication freezes the downstream execution boundary for `P-PH000-ST001-AC010` after AC009 completed `GATE-002` and the approved `P-STD-001` evolution package.

The handoff goal is narrow and explicit: AC010 may retrofit the governed metadata structure of the existing P-level standards, but it must not reopen the AC009 design decisions that produced that metadata model.

---

## II. UPSTREAM AUTHORITY SURFACES

AC010 SHALL treat the following surfaces as the upstream authority set:
- `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md`
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/proposal/proposal_P-PH000-ST001-AC009_gate-002_p-std-001-evolution-disposition.md`
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/plan_P-PH000-ST001-AC009.md`
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/implementation/implementation_P-PH000-ST001-AC009_p-std-001-evolution-task-specification.md`

This communication is the AC009-local downstream briefing surface that packages those authorities for AC010 consumption. It does not replace the governing plan or proposal surfaces.

---

## III. REQUIRED AC010 USE

The following AC010 tasks SHALL include this communication as a context input:
- `P-PH000-ST001-AC010-TK000`
- future developer execution of `P-PH000-ST001-AC010-TK001` through `P-PH000-ST001-AC010-TK004`

Minimum usage rule:
- AC010 consultant-owned planning and specification work MUST read this communication before authoring downstream artifacts.
- Future AC010 developer execution MUST follow the implementation task specification commissioned from `TK000`; this communication remains the design-boundary input behind that specification.

---

## IV. EXACT RETROFIT CONTRACT

### A. In-Scope Retrofit Obligation

AC010 SHALL retrofit the following metadata-governance requirements into the existing target standards:
- `P-STD-001-CLAUSE-031` — governed YAML frontmatter
- `P-STD-001-CLAUSE-032` — current-state metadata authority split
- `P-STD-001-CLAUSE-034` — semver tracking and amendment history
- `P-STD-001-CLAUSE-035` — `## References` taxonomy and table schema
- `P-STD-001-CLAUSE-036` — `## Provenance` taxonomy and extensions, including `P-STD-001-CLAUSE-036G`

Target standards:
- `P-STD-002`
- `P-STD-004`
- `P-STD-005`

### B. Explicit Non-Reopen Rules

AC010 MUST NOT:
- modify `P-STD-001`
- modify normative `CLAUSE` body content inside `P-STD-002`, `P-STD-004`, or `P-STD-005`
- expand scope to include `P-STD-003`
- perform repo-wide sweeps beyond the bounded standards and SPS surfaces
- reinterpret `CLAUSE-036G`, Amendment History externalization, or the `References` versus `Provenance` authority split

### C. Structural Mapping Rule

Existing noncanonical metadata material in the target standards MUST be preserved by being remapped into the governed destinations below rather than deleted:
- current lifecycle posture -> `### Status`
- promotion / seed / supersession / gate-lineage pointers -> `### Lineage / Authority`
- dated change summaries -> `### Amendment History`
- materially used inputs -> `### Input Sources`

### D. SPS Follow-On Rule

AC010 MAY update `prompt/artifacts/tasks/P/ssot/sps_P-PROGRAM.md` only to keep the registration text aligned with the retrofitted standards. AC010 MUST NOT invent a new SPS schema to carry version fields that the current SPS standard index does not define.

---

## V. EXPECTED DOWNSTREAM PACKAGE SHAPE

Before any future developer execution begins, AC010 SHALL have:
1. a consultant-authored readiness assessment, and
2. a consultant-authored `IMPLEMENTATION` `task_specification`

Those two artifacts are the commissioning package for future execution of `TK001` through `TK004`.

---

## VI. REQUESTED AC010 OUTCOME

AC010 should leave the program standards suite in this posture:
- `P-STD-002`, `P-STD-004`, and `P-STD-005` all expose governed frontmatter
- each target standard uses canonical `## References` and `## Provenance` structure
- no AC009 design decisions are reopened during the retrofit
- the final AC010 gate package can cite this communication as the upstream boundary brief
