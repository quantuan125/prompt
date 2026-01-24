#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import shutil
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class FileMapping:
    source: Path
    destination: Path


def sha256_path(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def find_repo_root(start: Path) -> Path:
    start = start.resolve()
    for candidate in [start, *start.parents]:
        if (candidate / "prompt").is_dir() and (candidate / ".codex").exists():
            return candidate
    raise RuntimeError("Could not locate repo root (expected `prompt/` and `.codex/`).")


def ensure_destination_is_safe(dest_dir: Path) -> None:
    if dest_dir.exists() and dest_dir.is_symlink():
        raise RuntimeError(f"Refusing to sync into symlinked destination directory: {dest_dir}")
    if dest_dir.exists() and not dest_dir.is_dir():
        raise RuntimeError(f"Destination exists but is not a directory: {dest_dir}")


def build_mappings(ssot_dir: Path, dest_dir: Path, print_script: Path) -> list[FileMapping]:
    if not ssot_dir.is_dir():
        raise FileNotFoundError(f"SSOT directory not found: {ssot_dir}")

    ssot_skill_md = ssot_dir / "SKILL.md"
    if not ssot_skill_md.exists():
        raise FileNotFoundError(f"Missing required SSOT file: {ssot_skill_md}")

    if not print_script.exists():
        raise FileNotFoundError(f"Missing required SSOT print script: {print_script}")

    return [
        FileMapping(source=ssot_skill_md, destination=dest_dir / "SKILL.md"),
        FileMapping(
            source=print_script,
            destination=dest_dir / "scripts" / print_script.name,
        ),
    ]


def compute_diff(mappings: list[FileMapping]) -> list[str]:
    diffs: list[str] = []
    for mapping in mappings:
        if not mapping.source.exists():
            diffs.append(f"Missing source: {mapping.source}")
            continue
        if not mapping.destination.exists():
            diffs.append(f"Missing destination: {mapping.destination}")
            continue
        if sha256_path(mapping.source) != sha256_path(mapping.destination):
            diffs.append(f"Different content: {mapping.source} -> {mapping.destination}")
    return diffs


def sync_files(mappings: list[FileMapping]) -> None:
    for mapping in mappings:
        mapping.destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(mapping.source, mapping.destination)


def sync_to_codex_mirror(
    *,
    ssot_dir: Path,
    dest_dir: Path,
    print_script: Path,
    check: bool,
) -> int:
    ensure_destination_is_safe(dest_dir)

    mappings = build_mappings(ssot_dir=ssot_dir, dest_dir=dest_dir, print_script=print_script)

    diffs = compute_diff(mappings)
    if check:
        if diffs:
            print("Mirror differs from SSOT:")
            for diff in diffs:
                print(f"- {diff}")
            return 2
        print("Mirror matches SSOT.")
        return 0

    sync_files(mappings)
    diffs_after = compute_diff(mappings)
    if diffs_after:
        print("ERROR: Mirror still differs after sync:")
        for diff in diffs_after:
            print(f"- {diff}")
        return 1

    print(f"Synced SSOT -> {dest_dir.resolve()}")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Sync the SSOT skill under prompt/skills/… into a Codex-discoverable mirror directory "
            "under .codex/skills/…"
        )
    )
    parser.add_argument(
        "--skill-name",
        help="ADR skill name from the registry (preferred).",
    )
    parser.add_argument(
        "--ssot-dir",
        help="SSOT directory (escape hatch if --skill-name is not provided).",
    )
    parser.add_argument(
        "--dest-dir",
        help="Destination mirror directory (escape hatch if --skill-name is not provided).",
    )
    parser.add_argument(
        "--print-script",
        help=(
            "Path to the SSOT print script to mirror. If omitted with --ssot-dir, "
            "attempts to autodetect a single scripts/print_t102_adr_*.py."
        ),
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Do not write; exit non-zero if mirror differs from SSOT.",
    )
    return parser.parse_args()


def autodetect_print_script(ssot_dir: Path) -> Path:
    scripts_dir = ssot_dir / "scripts"
    matches = sorted(scripts_dir.glob("print_t102_adr_*.py"))
    if len(matches) != 1:
        raise RuntimeError(
            "Could not autodetect print script. "
            f"Expected exactly 1 match for {scripts_dir}/print_t102_adr_*.py, found {len(matches)}."
        )
    return matches[0]


def resolve_cli_targets(repo_root: Path, args: argparse.Namespace) -> tuple[Path, Path, Path]:
    if args.skill_name:
        from adr_skills_registry import ADR_SKILLS

        matches = [skill for skill in ADR_SKILLS if skill.skill_name == args.skill_name]
        if not matches:
            raise RuntimeError(f"Unknown --skill-name: {args.skill_name}")
        if len(matches) != 1:
            raise RuntimeError(f"Ambiguous --skill-name: {args.skill_name}")
        skill = matches[0]

        ssot_dir = repo_root / skill.ssot_dir
        dest_dir = repo_root / Path(args.dest_dir) if args.dest_dir else repo_root / skill.codex_mirror_dir
        print_script = repo_root / skill.extraction_script
        return ssot_dir, dest_dir, print_script

    if not args.ssot_dir or not args.dest_dir:
        raise RuntimeError("Provide --skill-name, or provide both --ssot-dir and --dest-dir.")

    ssot_dir = (repo_root / Path(args.ssot_dir)).resolve()
    dest_dir = (repo_root / Path(args.dest_dir)).resolve()
    if args.print_script:
        print_script = (repo_root / Path(args.print_script)).resolve()
    else:
        print_script = autodetect_print_script(ssot_dir)
    return ssot_dir, dest_dir, print_script


def main() -> int:
    args = parse_args()
    repo_root = find_repo_root(Path(__file__))
    ssot_dir, dest_dir, print_script = resolve_cli_targets(repo_root, args)
    return sync_to_codex_mirror(
        ssot_dir=ssot_dir,
        dest_dir=dest_dir,
        print_script=print_script,
        check=args.check,
    )


if __name__ == "__main__":
    raise SystemExit(main())
