# Communication Brief: T903 Unified Reference Rewrite Tooling Request

**To**: T903 Initiative Consultant Owner  
**From**: LLM_Developer (T104 / ST007 implementation owner)  
**Date**: 2026-02-21  
**Subject**: Tooling request (Strategy B) — unified include/exclude-aware reference rewrite tool + registration in tools catalog  
**Priority**: High (recurring broken-link risk across initiatives)

---

## Context

During `T104-PH001-ST007-AC001.4` closeout (TK009), a scoped migration moved the authoritative T104 directory/naming proposal file:

- Old path: `prompt/artifacts/tasks/T104/workspace/PH001/ST002/proposal/proposal_T104-PH001-ST002-AC000_directory-naming-convention.md`
- New path: `prompt/artifacts/tasks/T104/workspace/PH001/ST002/AC000/proposal/proposal_T104-PH001-ST002-AC000_directory-naming-convention.md`

Because the live rewrite boundary was correctly limited to T104 scope during execution, **10 cross-initiative files** retained references to the old path (templates + P/T102/T103 artifacts). This is an expected and recurring outcome any time a bounded migration is performed.

TK009 addressed the immediate instance via bounded, scope-root-by-scope-root rewrites using the existing migrator, without rewriting evidence/output artifacts:

- Evidence commit: `2e1731d`
- Rewrite-only manifest + apply reports under: `prompt/scripts/output/T104-PH001-ST007-AC001/ac001.4/`

This pattern will recur across many initiatives. A durable, agent-safe tool is needed to prevent manual edits and to reduce future broken-link accumulation.

---

## Problem Statement

We need a **long-lived unified reference rewrite tool** that can safely update path references across `prompt/` (or subsets) while protecting audit/evidence artifacts by default.

Current tools:
- `prompt/scripts/migrate_initiative.py` can rewrite references, but it only supports a single `--scope-root` and does not provide an explicit include/exclude mechanism suitable for repo-wide reference repair (risk: rewriting `prompt/scripts/output/**` and other evidence surfaces if used broadly).
- `prompt/scripts/migrations/migrate_adr_to_std.py` demonstrates the right safety posture (include/exclude controls, max-files caps, auditable reporting), but is currently specialized to ADR/STD migrations.

---

## Request (Strategy B): New Unified Rewrite Tool

Commission a new script (recommended location):
- `prompt/scripts/rewrite_references.py`

### Functional Requirements

1. **Discovery + scan-only mode**
   - Scan a root directory (`--root prompt`) with deterministic ordering.
   - Output a report of occurrences for configured tokens (no mutation).

2. **Rewrite (mapping-driven)**
   - Support repeatable replacements:
     - `--replace-token OLD=NEW` (repeatable)
     - Optionally support `--replace-file mapping.json` for batch mappings.
   - Default: `--dry-run` unless `--apply` is explicitly set.

3. **Include / exclude controls (core requirement)**
   - `--include-path <path>` (repeatable) for precise targeting.
   - `--exclude-glob <glob>` (repeatable) for safety.
   - Strong safe defaults that protect audit/evidence surfaces:
     - Exclude `prompt/scripts/output/**`
     - Exclude `prompt/artifacts/**/verification/**`
     - Exclude `prompt/artifacts/**/dev-report/**`

4. **Blast-radius safety**
   - `--max-files-changed N` hard cap (default low, e.g. 50 or 100).
   - Fail closed if cap exceeded.

5. **Reporting**
   - Write a markdown report (per-file summary + unified diffs).
   - Optional JSON report for agentic workflows.

### Non-Functional Requirements
- Deterministic output (stable file ordering, stable diff sections).
- UTF-8 safety: skip non-UTF-8 files with an explicit report entry.
- Agent-friendly UX: concise console summary + report path.

---

## Acceptance Criteria

Demonstrate the tool on a known, already-validated mapping (from the T104 TK009 remediation):

- Replace:
  - `prompt/artifacts/tasks/T104/workspace/PH001/ST002/proposal/proposal_T104-PH001-ST002-AC000_directory-naming-convention.md`
  - with:
  - `prompt/artifacts/tasks/T104/workspace/PH001/ST002/AC000/proposal/proposal_T104-PH001-ST002-AC000_directory-naming-convention.md`

Expected outcomes:
- Dry-run reports exactly the expected edited files (10) in the intended scopes.
- Apply run updates exactly those files.
- Proof that excluded locations (especially `prompt/scripts/output/**`) are not modified.

---

## Tools Catalog Registration (Required)

After implementation, register the tool in:
- `prompt/documentation/tools_catalog.md`

Include:
- Purpose
- Key features (include/exclude, caps, dry-run, reports)
- Example usage (dry-run + apply)

---

## Notes

This tool should be treated as a general-purpose primitive for future migrations and cross-initiative repairs, enabling any LLM agent to perform safe, auditable reference remediation without manual editing.

