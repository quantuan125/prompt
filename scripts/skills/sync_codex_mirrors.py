#!/usr/bin/env python3
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

from adr_skills_registry import ADR_SKILLS


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Sync SSOT -> Codex mirror for all ADR skills listed in the registry."
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print each sync command before running it.",
    )
    return parser.parse_args()


def find_repo_root(start: Path) -> Path:
    start = start.resolve()
    for candidate in [start, *start.parents]:
        if (candidate / ".git").is_dir() and (candidate / "prompt").is_dir():
            return candidate
    raise RuntimeError("Could not locate repo root (expected `.git/` and `prompt/`).")


def run(args: list[str], *, cwd: Path, verbose: bool) -> subprocess.CompletedProcess[str]:
    if verbose:
        print(f"$ {' '.join(args)}")
    return subprocess.run(
        args,
        cwd=str(cwd),
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


def main() -> int:
    args = parse_args()
    repo_root = find_repo_root(Path(__file__))

    failures: list[str] = []
    for skill in ADR_SKILLS:
        script = repo_root / skill.codex_sync_script
        proc = run(["python3", str(script)], cwd=repo_root, verbose=args.verbose)
        if proc.returncode != 0:
            detail = (proc.stderr.strip() or proc.stdout.strip() or "sync failed")
            failures.append(f"{skill.skill_name}: {detail}")

    if failures:
        print("ERROR: One or more Codex mirror syncs failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Synced SSOT -> Codex mirrors (registry-driven).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

