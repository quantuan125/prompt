<!--
Script Reference: ADR Skills (registry-driven Active Skills)
-->

# ADR Skills Script Reference

This page documents the scripts humans may need to run or troubleshoot for the ADR Skills System.

Scope is registry-driven (see `prompt/scripts/skills/adr_skills_registry.py`).

## 1) Skill extraction scripts (shared core + per-skill wrappers)

### Shared extractor entrypoint (recommended for debugging)

**Script**: `prompt/scripts/skills/extract_adr.py`

**Intent**:
- Print **only** the relevant ADR block from the Concept file (strict, bounded).
- Avoid loading the entire concept document (to prevent rule “bleed” from other ADRs).

**Usage (by ADR ID, registry-resolved)**:
- `python3 prompt/scripts/skills/extract_adr.py --adr-id ADR-005`

**Usage (by explicit anchor, strict)**:
- `python3 prompt/scripts/skills/extract_adr.py --expected-anchor "{#t102-std-005-id-spec}"`

**Optional input override**:
- `python3 prompt/scripts/skills/extract_adr.py --adr-id ADR-005 --concept-path path/to/concept.md`

### Per-skill wrapper scripts (stable entrypoints)

Each ADR skill ships its own extraction wrapper under `prompt/skills/<skill>/scripts/print_*.py`.
These wrappers preserve stable, per-skill entrypoints while delegating extraction to the shared core.

Example (ADR-005):
- **Script**: `prompt/skills/t102-std-005-id-spec/scripts/print_t102_adr_005.py`

**Intent**:
- Print **only** the relevant ADR block from the Concept file.
- Avoid loading the entire concept document (to prevent rule “bleed” from other ADRs).

**Usage**:
- `python3 prompt/skills/<skill>/scripts/print_*.py`
- `python3 prompt/skills/<skill>/scripts/print_*.py --concept-path path/to/concept.md`

**Inputs**:
- `--concept-path` (optional): defaults to `prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md`

**Boundary behavior (expected)**:
- The output includes the expected ADR anchor line for that skill (defined in the verifier registry).
- The output stops before the next ADR header list item (so adjacent ADRs are excluded).

**Common failure modes**:
1. “start marker not found”
   - Cause: the anchor `{#t102-std-005-id-spec}` was renamed/moved in the Concept file.
   - Fix: update the anchor constant in the script or restore the anchor in the Concept document.
2. “empty block”
   - Cause: anchor was found but the region extracted is blank (usually a formatting change).
   - Fix: update the “next ADR header” regex or the Concept formatting.

## 2) Codex mirror sync scripts (shared core + per-skill wrappers)

### Shared sync entrypoint (recommended for automation)

**Script**: `prompt/scripts/skills/sync_to_codex_mirror.py`

**Intent**:
- Sync a single SSOT skill under `prompt/skills/<skill>/` into a Codex-discoverable mirror directory under `.codex/skills/<skill>/`.
- Designed to be used both directly (CLI) and by per-skill wrapper scripts.

**Usage (check-only, drift detection)**:
- `python3 prompt/scripts/skills/sync_to_codex_mirror.py --skill-name t102-std-005-id-spec --check`

**Usage (sync / repair drift)**:
- `python3 prompt/scripts/skills/sync_to_codex_mirror.py --skill-name t102-std-005-id-spec`

### Per-skill wrapper scripts (stable entrypoints)

Each ADR skill ships its own Codex mirror sync script under `prompt/skills/<skill>/scripts/sync_to_codex_mirror.py`.
These wrappers preserve stable, per-skill entrypoints while delegating sync logic to the shared core.

Example (ADR-005):
- **Script**: `prompt/skills/t102-std-005-id-spec/scripts/sync_to_codex_mirror.py`

**Intent**:
- Keep Codex’s `.codex/skills/t102-std-005-id-spec/` mirror directory in sync with SSOT under `prompt/skills/t102-std-005-id-spec/`.
- Codex CLI does not reliably consume symlinks under `.codex/skills/`, so this uses a real directory.

**What is copied (current scope)**:
- `prompt/skills/<skill>/SKILL.md` → `.codex/skills/<skill>/SKILL.md`
- `prompt/skills/<skill>/scripts/print_*.py` → `.codex/skills/<skill>/scripts/print_*.py`

**Usage (sync)**:
- `python3 prompt/skills/<skill>/scripts/sync_to_codex_mirror.py`

**Usage (check-only)**:
- `python3 prompt/skills/<skill>/scripts/sync_to_codex_mirror.py --check`

**Exit codes**:
- `0`: mirror matches SSOT (or sync succeeded and parity is confirmed)
- `1`: sync attempted but parity is still not achieved
- `2`: `--check` detected drift (mirror differs from SSOT)

**Safety constraints**:
- Refuses to sync if the destination directory is a symlink (prevents “sync into link” foot-guns).

**Drift meaning**:
- The Codex mirror differs from SSOT (most commonly: SSOT changed but mirror was not refreshed).

**How to resolve drift**:
1. Run the sync script (no `--check`).
2. Re-run with `--check` to confirm PASS.

## 3) Sync all Codex mirrors (registry-driven, write)

**Script**: `prompt/scripts/skills/sync_codex_mirrors.py`

**Intent**:
- Sync SSOT → Codex mirrors for every skill listed in the registry.

**Usage**:
- `python3 prompt/scripts/skills/sync_codex_mirrors.py`
- `python3 prompt/scripts/skills/sync_codex_mirrors.py --verbose`

## 4) ADR skills verification entrypoint (recommended)

**Script**: `prompt/scripts/skills/verify_adr_skills.py`

**Intent**:
- Provide one human-friendly command to verify ADR Skills distribution and extraction behavior.

**Usage**:
- `python3 prompt/scripts/skills/verify_adr_skills.py`
- `python3 prompt/scripts/skills/verify_adr_skills.py --drift-demo`

## 5) Optional commit-time enforcement hook installer

**Script**: `prompt/scripts/skills/install_adr_skills_pre_commit_hook.py`

**Usage**:
- `python3 prompt/scripts/skills/install_adr_skills_pre_commit_hook.py --install`
- `python3 prompt/scripts/skills/install_adr_skills_pre_commit_hook.py --uninstall`
