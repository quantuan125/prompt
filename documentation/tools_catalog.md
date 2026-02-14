# Project Script Catalog

This catalog provides a summary of utility scripts available for project maintenance, automation, and documentation management.

## Documentation Tools

### `update_doc.py`
**Location**: `scripts/update_doc.py`
**Purpose**: Automates the maintenance, versioning, and archiving of governed documentation files.
**Key Features**:
- Auto-archives current versions to an `archive/` directory.
- Updates `_change_history.md` files with semantic version entries.
- Supports dry-run validation and semantic versioning enforcement.
**Usage**:
```bash
python scripts/update_doc.py --doc-path "path/to/doc.md" --current-version "1.0.0" --new-version "1.1.0" --change-type "Minor" --summary "Add new features"
```

### `refactor_filenames.py`
**Location**: `scripts/refactor_filenames.py`
**Purpose**: Batch migrates versioned `.md` files to a "Stable Path" convention (no version in filename).
**Key Features**:
- Identifies latest version using semver and renames it to a stable path (e.g., `doc_v1.0.0.md` -> `doc.md`).
- Safely moves all versions to a local `archive/` directory without overwriting existing files.
- Recursively updates internal Markdown links and references to point to the new stable path.
- Includes a mandatory "Before -> After" audit log and defaults to `--dry-run`.
**Usage**:
```bash
python scripts/refactor_filenames.py --dry-run
```

### `migrate_adr_to_std.py`
**Location**: `prompt/scripts/migrations/migrate_adr_to_std.py`  
**Compatibility Wrapper**: `prompt/artifacts/tasks/T102/consultant/workspace/scripts/migrate_adr_to_std.py`  
**Purpose**: Performs governed ADR->STD migration updates, staged retitle operations, and anchor normalization with safety controls.
**Key Features**:
- Supports ID migration (`--old-adr-id` + `--new-std-id`) with same-number validation.
- Supports retitle rewrites (`--retitle-from` + `--retitle-to`) and governed anchor regeneration (`--regen-anchors-id-title`).
- Supports bounded execution (`--include-path`) and exclusion controls (`--exclude-glob`), with built-in protections for output/report artifacts.
- Supports arbitrary token replacements (`--replace-token OLD=NEW`) and blast-radius protection (`--max-files-changed`).
- Produces markdown change reports with per-file summaries and unified diffs.
**Usage (Stage 1 dry-run example)**:
```bash
python3 prompt/scripts/migrations/migrate_adr_to_std.py \
  --std-id T102-STD-004 \
  --retitle-from "Decision Records Standard" \
  --retitle-to "Specification Standard & Guideline" \
  --regen-anchors-id-title \
  --replace-token "t102-std-004-drs-standard=t102-std-004-specification-standard-and-guideline" \
  --replace-token "t102-std-004-adr-001-decision-records-standard=t102-std-004-adr-001-specification-standard-and-guideline" \
  --root prompt \
  --include-path prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md \
  --include-path prompt/artifacts/tasks/T102/consultant/standards/T102-STD-004_specification-standard-and-guideline.md \
  --dry-run \
  --max-files-changed 10 \
  --report-path prompt/scripts/output/std_migration/report_AC007_stage1_dry_run.md
```

### `migrate_initiative.py`
**Location**: `prompt/scripts/migrate_initiative.py`
**Purpose**: Executes manifest-driven initiative directory migrations with integrated reference rewriting.
**Key Features**:
- Loads full JSON manifest before execution (`operations` or list-form manifests).
- Supports safe dry-run mode by default and explicit `--apply` for live migration.
- Validates duplicate/overlapping moves, source existence, and target collisions before execution.
- Rewrites path references using manifest mappings with `--max-files-changed` safety cap.
- Emits optional markdown migration report with move logs and unified diffs.
**Usage**:
```bash
python3 prompt/scripts/migrate_initiative.py \
  --manifest prompt/scripts/output/t104_manifest.json \
  --project-root . \
  --dry-run \
  --report-path prompt/scripts/output/migration_report.md
```

### `scaffold_initiative.py`
**Location**: `prompt/scripts/scaffold_initiative.py`
**Purpose**: Generates a convention-aligned initiative folder skeleton under `prompt/artifacts/tasks/`.
**Key Features**:
- Creates baseline directories (`archive/`, `research/`, `ssot/`, `standard/`, `workspace/`).
- Scaffolds timeline hierarchy (`PH###/ST###`) for configurable phase count and stream set.
- Uses dry-run mode by default with optional markdown report output.
**Usage**:
```bash
python3 prompt/scripts/scaffold_initiative.py \
  --initiative-id T999 \
  --initiative-code DEMO \
  --phase-count 1 \
  --streams ST000,ST001 \
  --dry-run
```

### `validate_initiative_structure.py`
**Location**: `prompt/scripts/validate_initiative_structure.py`
**Purpose**: Validates initiative structures against ST007 conventions.
**Key Features**:
- Checks required top-level initiative directories.
- Validates timeline hierarchy (`workspace/PH###/ST###`).
- Verifies raw transcript naming includes `SES###`.
- Audits research directory naming by `RES` ID and applies AC directory threshold checks.
- Supports optional markdown report output and strict mode for AC threshold enforcement.
**Usage**:
```bash
python3 prompt/scripts/validate_initiative_structure.py \
  --initiative-root prompt/artifacts/tasks/T104 \
  --strict \
  --report-path prompt/scripts/output/validate_t104.md
```

---
*Last Updated: 2026-02-14*
