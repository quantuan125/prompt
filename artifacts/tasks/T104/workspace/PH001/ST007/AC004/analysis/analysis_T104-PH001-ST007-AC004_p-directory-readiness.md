---
artifact_type: 'ANALYSIS'
analysis_type: 'readiness_assessment'
initiative_id: 'T104'
initiative_code: 'CWS'
phase: '1'
stream_id: 'T104-PH001-ST007'
activity_id: 'T104-PH001-ST007-AC004'
version: '1.0.0'
date: '2026-02-22'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
---

# ANALYSIS: T104 (CWS) / PH001 / ST007 / AC004 - P Directory Migration Readiness Assessment

## I. Purpose

Readiness assessment of the P initiative directory for migration to convention-conformant structure. Enumerates all structural issues the developer must resolve during AC004 (Script Enhancement + P Directory Migration).

## II. Authority Surface

Proposal v3.3.0 (23 DRs approved). All conventions apply to P as a program-level initiative.

## III. Current State Summary

- Total files: 33 (26 `.md`, 7 `.txt`)
- Root directories present: `archive/`, `raw/`, `ssot/`, `standard/`, `workspace/`
- Root directories missing: `research/`
- Workspace layout: Hybrid (type-first at workspace root + partial timeline under `PH000/`)
- Convention conformance: Low - 7 type-first workspace directories, root-level `raw/`, naming inconsistencies

## IV. Issue Register

Table columns: `Issue ID | Category | Files Affected | Description | Convention Violated | Recommended Action`

| Issue ID | Category | Files | Description | Convention | Action |
|:--|:--|:--|:--|:--|:--|
| P-ISS-001 | Root-level `raw/` directory | 3 files | `P/raw/PH000/ST000/` and `P/raw/PH000/ST001/` exist at initiative root. Raw transcripts must be scoped under workspace timeline hierarchy. | Conv 3 | Move to `workspace/PH000/ST000/raw/` and `workspace/PH000/ST001/raw/` respectively. UID-scope rule determines AC-level placement where applicable. |
| P-ISS-002 | Type-first `workspace/notes/` | 8 files | Notes register files and session notes under `workspace/notes/PH000/ST000/` and `workspace/notes/PH000/ST001/`. Type-first grouping forbidden. | Conv 3 | Redistribute: stream/phase notes registers -> `workspace/PH000/` and `workspace/PH000/ST###/`. Session notes files -> `snotes_` rename (see P-ISS-006) + activity-level `snotes/`. |
| P-ISS-003 | Type-first `workspace/plan/` | 6 files | Plan files under `workspace/plan/` and `workspace/plan/PH000/ST001/`. | Conv 3 | Redistribute: phase plan -> `workspace/PH000/plan_P-PH000.md`. Stream plans -> `workspace/PH000/ST###/plan_P-PH000-ST###.md`. Activity plans -> `workspace/PH000/ST###/AC###/` where applicable. |
| P-ISS-004 | Type-first `workspace/raw/` | 4 files | Raw transcripts under `workspace/raw/PH000/ST001/`. | Conv 3 | Move to `workspace/PH000/ST001/raw/` or `workspace/PH000/ST001/AC###/raw/` per UID-scope rule. |
| P-ISS-005 | Type-first `workspace/proposal/`, `workspace/roadmap/`, `workspace/verification/`, `workspace/analysis/` | 7 files | Proposal (1), roadmap (1), verification (3), analysis (1) at workspace root using type-first layout. | Conv 3 | Redistribute to timeline paths. Verification files have AC002-scoped UIDs -> `AC002/verification/`. Roadmap -> `workspace/PH000/` or `ssot/` per DR-8. Proposal -> `workspace/PH000/ST001/proposal/` or `workspace/PH000/ST001/AC002/proposal/`. Analysis -> scoped by UID. |
| P-ISS-006 | Session notes `notes_` prefix | 5 files | `notes_P-PH000-ST001-AC002-SES001.md` through SES003 and `notes_P-PH000-ST001-AC004-SES001.md` use legacy `notes_` prefix for session notes. | DR-20 | Rename to `snotes_` prefix. Relocate to `snotes/` type subdirectories at activity level. |
| P-ISS-007 | Raw naming inconsistencies | 3 files | (a) `raw_P-PH000-ST000-AC001-2026-02-05.txt` - date instead of SES### token. (b) `raw_P-PH000-ST001_AC002_SES001.txt` - underscore separators. (c) `raw_P-PH000-ST001_AC002_SES002.txt` - underscore separators. | DR-10, Conv 2 | (a) Assign SES### token (SES001 if only session for that activity). (b)(c) Replace underscores with hyphens in UID tokens. |
| P-ISS-008 | Missing `research/` root directory | 0 | Validator requires `archive`, `research`, `ssot`, `standard`, `workspace` at initiative root. `research/` is absent. | Conv 1 | Create empty `research/` directory via scaffold or manifest `mkdir` operation. |
| P-ISS-009 | Missing `concept_` in SSOT | 0 | Validator requires both `sps_*.md` and `concept_*.md` in SSOT. P has `sps_P-PROGRAM.md` but no concept document. | Conv 1 | Create stub `concept_P-PROGRAM.md` with minimal frontmatter and placeholder content. Per client decision: pragmatic solution to pass validator. |
| P-ISS-010 | Archive deprecated file | 1 file | `archive/changelog_roadmap_P-PROGRAM_phase0.md` has no version suffix. This is a deprecated file (no live successor). | Conv 8 | **No action required**. Per two-tier archive model (SES002 client decision): deprecated files in `archive/` do not require version suffix. File is correctly placed. |
| P-ISS-011 | Verification files at workspace root | 3 files | `verification_P-PH000-ST001-AC002-GATE-002_tk005-supplement.md`, `verification_P-PH000-ST001-AC002_gate-002.md`, `verification_P-PH000-ST001-AC002_tk003-to-tk006.md`. All have AC002-scoped UIDs. | DR-22, Conv 4 | Move to `workspace/PH000/ST001/AC002/verification/`. |

## V. Script Compatibility Issues

| Script | Issue | Required Enhancement |
|:--|:--|:--|
| `validate_initiative_structure.py` | Running against P pre-migration produces false-positive errors (type-first dirs, root raw, missing research). | `--profile pre-migration` flag to suppress known pre-migration violations. |
| `scaffold_initiative.py` | Hard-stops if initiative root already exists (line 131-132: `if plan.root.exists() and not dry_run: return 1`). Cannot merge scaffold into existing P directory. | `--force` flag for merge mode (skip existence check, create only missing dirs). |
| `scaffold_initiative.py` | No support for P-style "program initiative" (may lack epic support or phase-0 conventions). | `--epic-ids` flag if P has sub-epics; or confirm P has no sub-epics and standard scaffold suffices. |
| `migrate_initiative.py` | Works as-is (manifest-driven). No P-specific enhancements needed. | None. |

## VI. File-by-File Current->Target Mapping (Preview)

This section provides a preview mapping for all 33 files. The definitive manifest will be authored by the developer in AC004-TK004.

Total operations estimated:
- `mkdir` operations: ~15 (new timeline directories + type subdirectories)
- `move` operations: ~30 (most files need relocation from type-first to timeline)
- `rename` operations: ~8 (snotes_ prefix + raw naming fixes)
- `reference_rewrite` operations: ~30 (one per move/rename)
- `create` operations: 2 (concept stub + research dir)

## VII. Risk Assessment

| Risk ID | Description | Likelihood | Impact | Mitigation |
|:--|:--|:--|:--|:--|
| P-RISK-001 | Reference rewrite breadth: P files are referenced across T102, T104, and P workspaces | Medium | Medium | Scope `--scope-root` to `prompt/` for full-repo reference scan. Review dry-run diff report before live apply. |
| P-RISK-002 | Stream plan references inside P files use type-first paths (e.g., `workspace/plan/plan_P-PH000-ST001.md` in frontmatter `plan_reference` fields) | High | Low | Include frontmatter `plan_reference` and `register_reference` fields in reference rewrite rules. |
| P-RISK-003 | SES### token assignment ambiguity for date-based raw file | Low | Low | Assign SES001 (confirmed as only session for AC001 in ST000). Document in manifest. |

## VIII. Verdict

P directory is **non-conformant** across all major conventions (1, 2, 3, 4, 8). 11 issues identified. The migration is structurally similar to T104's AC001 migration but smaller in scale (33 files vs T104's ~80+). The existing `migrate_initiative.py` can handle the migration; validator and scaffold scripts need enhancement first (AC004-TK001/TK002 before TK003).

