---
artifact_type: 'PROPOSAL'
initiative_id: 'T102'
epic_id: 'T102-PH001-ST001-AC007'
epic_code: 'CWD-AC007'
phase: '1'
version: '1.0.0'
date: '2026-02-08'
status: 'completed'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T102/consultant/workspace/plan/PH001/ST001/plan_T102-PH001-ST001-AC007.md'
analysis_reference: 'prompt/artifacts/tasks/T102/consultant/workspace/analysis/analysis_T102-CONSULTANT_adr-governance-review.md'
target_document: 'prompt/artifacts/tasks/T102/consultant/standards/standard_T102-STD-004_specification-standard-and-guideline.md'
target_section: 'TK008 Stage 2 Global Migration Execution + Verification'
---

# PROPOSAL: AC007 TK008 Stage 2 Migration Evidence (Global `prompt/` Execution)

## I. Executive Summary

This artifact records reproducible evidence for AC007 `TK008` completion:
- Stage 2 dry-run and apply executed using the canonical migration script.
- Global scope under `prompt/` used with locked exclusions (`raw_*`, output/report artifacts).
- Post-apply scans confirmed in-scope removal of legacy `T102-ADR-004` plain and clause references and legacy anchor tokens.
- AC007 plan/notes were finalized and normalized for closure.

## II. Execution Configuration

### A. Script

`prompt/scripts/migrations/migrate_adr_to_std.py`

### B. Transform Set

- ID migration: `T102-ADR-004` -> `T102-STD-004`
- Retitle: `Decision Records Standard` -> `Specification Standard & Guideline`
- Anchor regeneration: `--regen-anchors-id-title`
- Token replacements:
  - `t102-std-004-drs-standard=t102-std-004-specification-standard-and-guideline`
  - `t102-std-004-adr-001-decision-records-standard=t102-std-004-adr-001-specification-standard-and-guideline`
- Root: `prompt`
- Exclusions:
  - `**/raw_*`
  - `**/scripts/output/**`
  - `**/workspace/scripts/report_*.md`
- Safety cap: `--max-files-changed 400`

## III. Command Log (Reproducible)

### A. Dry-Run

```bash
python3 prompt/scripts/migrations/migrate_adr_to_std.py \
  --old-adr-id T102-ADR-004 \
  --new-std-id T102-STD-004 \
  --retitle-from "Decision Records Standard" \
  --retitle-to "Specification Standard & Guideline" \
  --regen-anchors-id-title \
  --replace-token "t102-std-004-drs-standard=t102-std-004-specification-standard-and-guideline" \
  --replace-token "t102-std-004-adr-001-decision-records-standard=t102-std-004-adr-001-specification-standard-and-guideline" \
  --root prompt \
  --exclude-glob "**/raw_*" \
  --exclude-glob "**/scripts/output/**" \
  --exclude-glob "**/workspace/scripts/report_*.md" \
  --dry-run \
  --max-files-changed 400 \
  --report-path prompt/scripts/output/std_migration/report_AC007_tk008_stage2_dry_run.md
```

**Observed output**:
- `mode=dry-run changed=125 skipped_include=0 skipped_excluded=16 skipped_encoding=0`
- report: `prompt/scripts/output/std_migration/report_AC007_tk008_stage2_dry_run.md`

### B. Apply

```bash
python3 prompt/scripts/migrations/migrate_adr_to_std.py \
  --old-adr-id T102-ADR-004 \
  --new-std-id T102-STD-004 \
  --retitle-from "Decision Records Standard" \
  --retitle-to "Specification Standard & Guideline" \
  --regen-anchors-id-title \
  --replace-token "t102-std-004-drs-standard=t102-std-004-specification-standard-and-guideline" \
  --replace-token "t102-std-004-adr-001-decision-records-standard=t102-std-004-adr-001-specification-standard-and-guideline" \
  --root prompt \
  --exclude-glob "**/raw_*" \
  --exclude-glob "**/scripts/output/**" \
  --exclude-glob "**/workspace/scripts/report_*.md" \
  --apply \
  --max-files-changed 400 \
  --report-path prompt/scripts/output/std_migration/report_AC007_tk008_stage2_apply.md
```

**Observed output**:
- `mode=apply changed=126 skipped_include=0 skipped_excluded=16 skipped_encoding=0`
- report: `prompt/scripts/output/std_migration/report_AC007_tk008_stage2_apply.md`

## IV. Verification Matrix

| Check ID | Verification Query | Expected | Result |
|:--|:--|:--|:--|
| `AC007-TK008-VER-001` | `rg -n "T102-ADR-004-CLAUSE-" prompt -g "*.md" -g "!**/raw_*" -g "!**/scripts/output/**" -g "!**/workspace/scripts/report_*.md"` | no matches | pass |
| `AC007-TK008-VER-002` | `rg -n "(?<![A-Za-z0-9])T102-ADR-004(?![A-Za-z0-9])" -P prompt -g "*.md" -g "!**/raw_*" -g "!**/scripts/output/**" -g "!**/workspace/scripts/report_*.md"` | no matches | pass |
| `AC007-TK008-VER-003` | `rg -n "t102-std-004-drs-standard|t102-std-004-adr-001-decision-records-standard" prompt -g "*.md" -g "!**/raw_*" -g "!**/scripts/output/**" -g "!**/workspace/scripts/report_*.md"` | no matches | pass |
| `AC007-TK008-VER-004` | `rg -n "T102-STD-004 \(Specification Standard & Guideline\)|t102-std-004-specification-standard-and-guideline|t102-std-004-adr-001-specification-standard-and-guideline" prompt -g "*.md" -g "!**/raw_*" -g "!**/scripts/output/**" -g "!**/workspace/scripts/report_*.md"` | positive matches | pass |

## V. AC007 Reports Register

| Report | Purpose | Path |
|:--|:--|:--|
| `report_AC007_stage1_dry_run.md` | Stage 1 dry-run (2-file scope) | `prompt/scripts/output/std_migration/report_AC007_stage1_dry_run.md` |
| `report_AC007_stage1_apply.md` | Stage 1 apply (2-file scope) | `prompt/scripts/output/std_migration/report_AC007_stage1_apply.md` |
| `report_AC007_tk007_adr005_dry_run.md` | TK007 ADR-005 validation dry-run | `prompt/scripts/output/std_migration/report_AC007_tk007_adr005_dry_run.md` |
| `report_AC007_tk007_adr005_apply.md` | TK007 ADR-005 validation apply | `prompt/scripts/output/std_migration/report_AC007_tk007_adr005_apply.md` |
| `report_AC007_tk007_analysis_review_dry_run.md` | TK007 analysis artifact check dry-run | `prompt/scripts/output/std_migration/report_AC007_tk007_analysis_review_dry_run.md` |
| `report_AC007_extra_analysis_adr004_to_std004_dry_run.md` | Additional analysis-target dry-run | `prompt/scripts/output/std_migration/report_AC007_extra_analysis_adr004_to_std004_dry_run.md` |
| `report_AC007_extra_analysis_adr004_to_std004_apply.md` | Additional analysis-target apply | `prompt/scripts/output/std_migration/report_AC007_extra_analysis_adr004_to_std004_apply.md` |
| `report_AC007_extra_notes_ac003_dry_run.md` | Additional AC003 notes dry-run | `prompt/scripts/output/std_migration/report_AC007_extra_notes_ac003_dry_run.md` |
| `report_AC007_extra_notes_ac003_apply.md` | Additional AC003 notes apply | `prompt/scripts/output/std_migration/report_AC007_extra_notes_ac003_apply.md` |
| `report_AC007_extra_notes_ac003_tokenfix_dry_run.md` | Additional AC003 token-focused dry-run | `prompt/scripts/output/std_migration/report_AC007_extra_notes_ac003_tokenfix_dry_run.md` |
| `report_AC007_extra_notes_ac003_tokenfix_apply.md` | Additional AC003 token-focused apply | `prompt/scripts/output/std_migration/report_AC007_extra_notes_ac003_tokenfix_apply.md` |
| `report_AC007_tk008_stage2_dry_run.md` | TK008 global Stage 2 dry-run | `prompt/scripts/output/std_migration/report_AC007_tk008_stage2_dry_run.md` |
| `report_AC007_tk008_stage2_apply.md` | TK008 global Stage 2 apply | `prompt/scripts/output/std_migration/report_AC007_tk008_stage2_apply.md` |

## VI. Residual Notes

- Historical/raw artifacts and generated reports are intentionally excluded from Stage 2 rewrite scope.
- Dry-run/apply changed counts differ by one file (`125` vs `126`); both runs remained under safety cap and passed verification checks.

## VII. Acceptance Statement

AC007 `TK008` is complete with reproducible evidence, and AC007 lifecycle is closed in plan and notes artifacts.
