# Communication Brief: T903 Canonical Path Tooling Request

**To**: LLM_Developer / Tooling Owner  
**From**: LLM_Consultant  
**Date**: 2026-02-04  
**Subject**: Tooling request — validate + rewrite `Canonical Path` entries for Model D indexes  
**Priority**: High (blocks safe future path migrations)

---

## Context

Phase 1 (`T102-PH001-ST001`) adopted **Model D (Combined ADR+Spec Files)**. Concept becomes an index-only hub and indexes link to external combined files using a `Canonical Path` column pointing to stable repo-relative paths under:
- `prompt/artifacts/tasks/T102/consultant/standards/`

This creates a predictable future maintenance problem: if paths must be migrated (directory reshapes, consolidation, Phase 2 separation), manual global edits are error-prone and drift-inducing.

---

## Problem Statement

We need tooling that can:
1) **Validate** that every indexed `Canonical Path` exists and matches expected conventions, and
2) **Rewrite** canonical paths safely when a mapping is applied (e.g., directory rename), producing an auditable report.

This is required so agentic LLM workflows can update paths quickly and safely without introducing broken links or inconsistent schemas.

---

## Requirements (Functional)

1) **Index discovery**
   - Scan known SSOT artifacts (at minimum: `prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md`) for ADR index tables containing `Canonical Path`.
   - Identify table schema and locate the `Canonical Path` column.

2) **Validation**
   - For each `Canonical Path`, check that the referenced file exists.
   - Detect duplicate `Canonical Path` values within the same index table.
   - Detect rows missing `Canonical Path` or using non-repo-relative values.

3) **Rewrite (mapping-driven)**
   - Accept a deterministic mapping (e.g., old prefix → new prefix).
   - Provide `--dry-run` output listing `old → new` per row, with counts and a summary.
   - Apply rewrites only when validation passes (or explicitly overridden with a flag).

4) **Reporting**
   - Emit a report of all changes (row identifier + old path + new path).
   - Emit a list of unresolved paths and the reason (missing file, ambiguous mapping, schema mismatch).

---

## Requirements (Non-functional)

- Deterministic output (stable ordering).
- Safe-by-default (dry-run first).
- Minimal configuration (single entrypoint).
- Agent-friendly: concise summary + machine-readable report option (JSON).

---

## Acceptance Criteria

- Demonstrate a dry-run on `concept_T102-CONSULTANT.md` producing:
  - total rows scanned, total valid, total missing, total duplicates, total rewrites proposed
- Demonstrate a real rewrite run (on a test mapping) producing:
  - updated file(s)
  - change report with `old → new` per edited row

---

## Notes

This tooling request is intentionally narrow (ADR index `Canonical Path`) but should be extensible to other indexes that adopt Canonical Path conventions later.

