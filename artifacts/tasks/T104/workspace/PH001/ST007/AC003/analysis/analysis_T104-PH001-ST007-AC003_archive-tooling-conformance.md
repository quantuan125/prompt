---
artifact_type: 'ANALYSIS'
analysis_type: 'conformance_audit'
initiative_id: 'T104'
initiative_code: 'CWS'
phase: '1'
stream_id: 'T104-PH001-ST007'
activity_id: 'T104-PH001-ST007-AC003'
version: '1.0.0'
date: '2026-02-22'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
---

# ANALYSIS: T104 (CWS) / PH001 / ST007 / AC003 - Archive Tooling Conformance Audit

## I. Purpose

Conformance audit of existing `archive_manager.py` against Convention 8 (Archive Strategy) from proposal v3.3.0. This analysis serves as the primary input for AC003 (Archive Tooling Development) developer commission.

## II. Authority Surface

Convention 8 from `proposal_T104-PH001-ST002-AC000_directory-naming-convention.md` (v3.3.0, DR-11 Approved).

## III. Script Under Audit

`prompt/scripts/archive_manager.py`

- Built against older `general.md` standard
- Class-based implementation (`ArchiveManager`) with CLI interface
- Subcommands: `archive`, `list`, `clean`, `restore`, `next-version`

## IV. Conformance Matrix

Table columns: `Convention 8 Requirement | Spec Reference | archive_manager.py Status | Verdict | Gap ID`

| Requirement | Spec | Status | Verdict | Gap |
|:--|:--|:--|:--|:--|
| Mirror structure: archive path mirrors live path within initiative root (`<SID>/archive/<subpath>` matches `<SID>/<subpath>`) | Rule 1 | Uses centralized `prompt/archive/` with role-based subdirs (`roles/consultant/`, `config/`, `templates/`, `artifacts/`). Does NOT mirror per-initiative paths. | **FAIL** | GAP-001 |
| Version suffix `_v#.#.#` before `.md` extension | Rule 2 | Correctly implements: `f"{doc_path.stem}_v{version}{doc_path.suffix}"` | **PASS** | — |
| Live files: no version suffix in filename | Rule 3 | N/A (archive-only tool; does not modify live files) | **PASS** | — |
| Archive trigger: major version bump or governance request | Rule 4 | No enforcement — archives any file at any version. Trigger logic is caller responsibility. | **PASS** (by design) | — |
| Changelog co-archiving alongside parent with same version suffix | Rule 5 | Not implemented. No changelog detection or co-archiving logic. | **FAIL** | GAP-002 |
| Tooling CLI: `archive_artifact.py <path-to-live-file>` | Rule 6 | CLI uses `archive_manager.py archive --path <path> --version <ver>`. Name differs; interface differs (requires explicit `--version`). | **FAIL** | GAP-003 |
| Frontmatter version extraction (version from file's frontmatter `version` field) | Rule 2 (impl) | Requires explicit `--version` CLI argument. No frontmatter parsing. | **FAIL** | GAP-004 |
| Dry-run mode | Implied (per scaffold/migrate pattern) | Not implemented. All operations are live. | **FAIL** | GAP-005 |
| Copy (not move) live file to archive | Implicit | Correctly uses `shutil.copy2` | **PASS** | — |

## V. Gap Register

| Gap ID | Title | Severity | Description | Remediation |
|:--|:--|:--|:--|:--|
| GAP-001 | Non-conformant archive path resolution | Critical | Current path logic: `prompt/archive/roles/consultant/` (role-based, centralized). Required: `<SID>/archive/<mirrored-subpath>` (initiative-scoped, mirrored). The `archive_document()` method uses string-matching (`"prompt/" in str(doc_path)`) to select archive dirs — must be replaced with initiative-root detection + path mirroring. | Refactor `archive_document()` to: (1) detect initiative root from input path, (2) compute relative subpath, (3) construct `<initiative-root>/archive/<subpath>`. |
| GAP-002 | Missing changelog co-archiving | Low | Convention 8 Rule 5 requires changelog files archived alongside parent artifact with same version suffix. No implementation exists. | Add logic to detect companion `changelog_<stem>.md` file and archive it with same version suffix. |
| GAP-003 | CLI interface mismatch | Medium | Proposal names the script `archive_artifact.py` with positional `<path-to-live-file>` argument. Current script uses `archive_manager.py archive --path <path> --version <ver>`. Per client decision: keep the name `archive_manager.py`; but the CLI should support a simplified `archive <path>` invocation (version auto-extracted from frontmatter per GAP-004). | Retain `archive_manager.py` name. Add simplified `archive <path>` positional interface. Keep `--version` as optional override. Update proposal Section VIII script name reference from `archive_artifact.py` to `archive_manager.py`. |
| GAP-004 | No frontmatter version extraction | Medium | Convention 8 Rule 2 specifies "version from the file's frontmatter `version` field at time of archiving." Current implementation requires explicit `--version` argument. | Add YAML frontmatter parser. Extract `version` field from input file. Use as default; allow `--version` CLI override. |
| GAP-005 | No dry-run mode | Medium | All three sibling scripts (`migrate_initiative.py`, `validate_initiative_structure.py`, `scaffold_initiative.py`) support dry-run mode. `archive_manager.py` does not. | Add `--dry-run` flag. In dry-run mode: print planned operations without executing. Generate dry-run report consistent with sibling script reporting patterns. |

## VI. Archive Taxonomy - Two-Tier Model (Convention 8 Amendment)

Per client decision (SES002 consultation, 2026-02-22): Convention 8 should be amended to recognize two categories of archived files:

| Category | Description | Version Suffix | Example |
|:--|:--|:--|:--|
| **Versioned snapshot** | A prior version of a live file, preserved before a breaking change. The live file continues to evolve. | Required (`_v#.#.#`) | `sps_P-PROGRAM_v1.0.0.md` |
| **Deprecated artifact** | A file that is no longer active and has no live successor. Placed in archive to signal non-live status. | Not required | `changelog_roadmap_P-PROGRAM_phase0.md` |

Semantic rule: files in `archive/` WITHOUT a version suffix are implicitly deprecated. Files WITH a version suffix are historical version snapshots.

The `archive_manager.py` remediation (AC003-TK001) should support both categories:
- `archive <path>` - auto-detect version from frontmatter, apply `_v#.#.#` suffix (versioned snapshot)
- `archive <path> --deprecated` - copy to mirrored archive path without version suffix (deprecated artifact)

## VII. Proposal Amendment Required

AC003 must include a task to amend the proposal (v3.3.0 -> v3.4.0):
- Convention 8: Add two-tier archive model (versioned vs deprecated)
- Section VIII: Update script name from `archive_artifact.py` to `archive_manager.py`
- DR-24: Two-tier archive model approved (reference this SES002 consultation)

## VIII. Verdict

`archive_manager.py` is **non-conformant** with Convention 8 in its current state. Five gaps identified (1 critical, 2 medium, 1 medium, 1 low). The script requires substantive refactoring - specifically the path resolution logic (GAP-001) - before it can serve as the Convention 8 archive tool for ST007 and future initiative migrations.

AC003 scope should be: conformance remediation of `archive_manager.py` (not greenfield development), proposal v3.4.0 amendment, and test coverage.

