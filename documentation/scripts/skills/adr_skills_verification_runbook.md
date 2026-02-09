<!--
ADR Skills Verification Runbook
Scope: registry-driven Active Skills (see prompt/scripts/skills/adr_skills_registry.py)
-->

# ADR Skills Verification Runbook

## What “PASS” means

PASS means that for every skill listed in `prompt/scripts/skills/adr_skills_registry.py`:
- The **SSOT** skill exists under `prompt/skills/<skill-name>/` and is internally consistent.
- **Claude Code** consumes the SSOT via a **symlink** at `.claude/skills/<skill-name>`.
- **Codex CLI** consumes the skill via a **real mirror directory** at `.codex/skills/<skill-name>` (not a symlink).
- The extraction wrappers (built on the shared extractor core) print **only** the intended ADR block (anchor present, next ADR excluded).
- The Codex mirror can be validated for parity (`--check`) and repaired by syncing.

**Concept SSOT formatting invariant (extraction boundary):**
- ADR blocks in `concept_T102` are expected to be single Markdown list items: the ADR header is the bullet line, and the ADR body lines must be indented with **2+ spaces or a tab**.
- If verification flags unintended trailing output or missing indented body lines, treat it as a **Concept SSOT formatting drift** and fix the Concept markdown (do not relax the extractor to “guess”).

## Single entrypoint (recommended)

Run:
- `python3 prompt/scripts/skills/verify_adr_skills.py`

PASS looks like:
- The script prints a PASS summary (no FAILED checks).
- Exit code is `0`.

## Automated vs manual checks

Automated (by `verify_adr_skills.py`):
- SSOT structure checks
- Claude symlink checks
- Extraction sanity checks (per registry skill)
- Codex mirror directory checks
- Codex mirror parity checks (via each skill’s `sync_to_codex_mirror.py --check`)
- Catalog alignment checks (the Active Skills list must match the registry)

Manual (checked by the Client):
1. **Claude discovery**: the skill appears in Claude Code after restart/reload.
2. **Codex discovery**: the skill appears in Codex CLI after restart/reload.

## Drift demo (required, explicit invocation only)

This is intentionally NOT the default mode because it writes temporary changes to the Codex mirror.

Run:
- `python3 prompt/scripts/skills/verify_adr_skills.py --drift-demo`

PASS looks like:
- The script proves drift is detected (mirror check fails).
- The script syncs and restores parity.
- The script proves parity is restored (mirror check passes).

## Distribution architecture

All ADR skills share the same distribution architecture:
- SSOT: `prompt/skills/<skill-name>/`
- Claude: `.claude/skills/<skill-name>` → symlink to SSOT
- Codex: `.codex/skills/<skill-name>/` → mirror directory (synced from SSOT)

## Shared entrypoints (debugging / automation)

Per-skill wrappers are the stable entrypoints, but the shared entrypoints can be useful for debugging or scripting.

**Shared extractor**:
- `python3 prompt/scripts/skills/extract_adr.py --adr-id ADR-005`
- `python3 prompt/scripts/skills/extract_adr.py --expected-anchor "{#t102-std-005-id-spec}"`

**Shared mirror sync (single skill)**:
- `python3 prompt/scripts/skills/sync_to_codex_mirror.py --skill-name t102-std-005-id-spec --check`
- `python3 prompt/scripts/skills/sync_to_codex_mirror.py --skill-name t102-std-005-id-spec`

**Sync all mirrors (registry-driven)**:
- `python3 prompt/scripts/skills/sync_codex_mirrors.py`

## Commit-time enforcement (optional but recommended)

Goal: prevent “Codex mirror drift” from landing unnoticed.

Install the recommended `pre-commit` hook:
- `python3 prompt/scripts/skills/install_adr_skills_pre_commit_hook.py --install`

What it does:
1. Sync SSOT → Codex mirrors (registry-driven).
2. Run ADR skills verification (read-only checks, registry-driven).
3. Fail the commit if verification fails.

Uninstall (restores previous hook if backed up):
- `python3 prompt/scripts/skills/install_adr_skills_pre_commit_hook.py --uninstall`

## Adding a new ADR skill to verification (future)

1. Add the skill to **Active Skills** in `prompt/documentation/adr_skills_catalog.md`.
2. Add a matching entry to `prompt/scripts/skills/adr_skills_registry.py`.
3. Ensure the skill provides:
   - `prompt/skills/<skill>/SKILL.md`
   - `prompt/skills/<skill>/scripts/print_*.py`
   - `prompt/skills/<skill>/scripts/sync_to_codex_mirror.py`
4. Run: `python3 prompt/scripts/skills/verify_adr_skills.py` (and `--drift-demo` when required).
