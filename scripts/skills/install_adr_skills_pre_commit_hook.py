#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import stat
import sys
from pathlib import Path


HOOK_SENTINEL = "ADR_SKILLS_PRE_COMMIT_HOOK_v1"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Optional commit-time enforcement for the ADR Skills System.\n"
            "Installs a .git/hooks/pre-commit hook that syncs the Codex mirror then runs "
            "ADR skills verification."
        )
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--install", action="store_true", help="Install the pre-commit hook.")
    group.add_argument("--uninstall", action="store_true", help="Uninstall the pre-commit hook (restore backup if present).")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print actions without writing to disk.",
    )
    return parser.parse_args()


def find_repo_root(start: Path) -> Path:
    start = start.resolve()
    for candidate in [start, *start.parents]:
        if (candidate / ".git").is_dir() and (candidate / "prompt").is_dir():
            return candidate
    raise RuntimeError("Could not locate repo root (expected `.git/` and `prompt/`).")


def hook_contents() -> str:
    return f"""#!/usr/bin/env bash
set -euo pipefail

# {HOOK_SENTINEL}
# Auto-sync Codex mirror + verify ADR skills before allowing commit.

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"

python3 prompt/scripts/skills/sync_codex_mirrors.py >/dev/null
python3 prompt/scripts/skills/verify_adr_skills.py >/dev/null
"""


def make_executable(path: Path) -> None:
    mode = path.stat().st_mode
    path.chmod(mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)


def install_hook(repo_root: Path, *, dry_run: bool) -> int:
    hooks_dir = repo_root / ".git/hooks"
    hook_path = hooks_dir / "pre-commit"
    backup_path = None

    if hook_path.exists():
        existing = hook_path.read_text(encoding="utf-8", errors="replace")
        if HOOK_SENTINEL in existing:
            print(f"Already installed: {hook_path}")
            return 0
        timestamp = dt.datetime.now().strftime("%Y%m%d%H%M%S")
        backup_path = hooks_dir / f"pre-commit.adr-skills.bak-{timestamp}"
        print(f"Backing up existing hook: {hook_path} -> {backup_path}")
        if not dry_run:
            backup_path.write_text(existing, encoding="utf-8")

    print(f"Installing hook: {hook_path}")
    if not dry_run:
        hooks_dir.mkdir(parents=True, exist_ok=True)
        hook_path.write_text(hook_contents(), encoding="utf-8")
        make_executable(hook_path)

    if backup_path is not None:
        print("To restore the previous hook, run: --uninstall (restores the latest backup when possible).")
    return 0


def uninstall_hook(repo_root: Path, *, dry_run: bool) -> int:
    hooks_dir = repo_root / ".git/hooks"
    hook_path = hooks_dir / "pre-commit"
    if not hook_path.exists():
        print(f"No hook installed at: {hook_path}")
        return 0

    existing = hook_path.read_text(encoding="utf-8", errors="replace")
    if HOOK_SENTINEL not in existing:
        print(f"Refusing to uninstall: {hook_path} is not an ADR-skills-installed hook.")
        return 2

    backups = sorted(hooks_dir.glob("pre-commit.adr-skills.bak-*"))
    latest_backup = backups[-1] if backups else None

    if latest_backup is None:
        print(f"Removing hook: {hook_path}")
        if not dry_run:
            hook_path.unlink()
        return 0

    print(f"Restoring backup: {latest_backup} -> {hook_path}")
    if not dry_run:
        hook_path.write_text(latest_backup.read_text(encoding="utf-8"), encoding="utf-8")
        make_executable(hook_path)
    return 0


def main() -> int:
    args = parse_args()
    try:
        repo_root = find_repo_root(Path(__file__))
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    if args.install:
        return install_hook(repo_root, dry_run=args.dry_run)
    return uninstall_hook(repo_root, dry_run=args.dry_run)


if __name__ == "__main__":
    raise SystemExit(main())
