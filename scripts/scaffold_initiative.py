#!/usr/bin/env python3
"""
Scaffold a convention-aligned initiative directory structure.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import re

from report_output import SCRIPTS_OUTPUT_ROOT, resolve_report_path


INITIATIVE_ID_PATTERN = re.compile(r"^[A-Z][A-Z0-9]*$")
STREAM_ID_PATTERN = re.compile(r"^ST\d{3}$")


@dataclass(frozen=True)
class ScaffoldPlan:
    root: Path
    epic_roots: list[Path]
    directories: list[Path]


def normalize_streams(raw_value: str) -> list[str]:
    stream_ids = [token.strip().upper() for token in raw_value.split(",") if token.strip()]
    if not stream_ids:
        raise ValueError("At least one stream ID is required.")
    invalid = [stream for stream in stream_ids if not STREAM_ID_PATTERN.match(stream)]
    if invalid:
        raise ValueError(f"Invalid stream IDs: {', '.join(invalid)}. Expected format ST###.")
    return sorted(set(stream_ids))


def normalize_epic_ids(raw_value: str) -> list[str]:
    epic_ids = [token.strip().upper() for token in raw_value.split(",") if token.strip()]
    if not epic_ids:
        raise ValueError("At least one epic ID is required when --epic-ids is provided.")
    invalid = [epic_id for epic_id in epic_ids if not INITIATIVE_ID_PATTERN.match(epic_id)]
    if invalid:
        raise ValueError(
            f"Invalid epic IDs: {', '.join(invalid)}. Expected format [A-Z][A-Z0-9]*."
        )
    return sorted(set(epic_ids))


def build_scaffold_plan(
    tasks_root: Path,
    initiative_id: str,
    phase_count: int,
    stream_ids: list[str],
    epic_ids: list[str] | None = None,
) -> ScaffoldPlan:
    initiative_root = tasks_root / initiative_id
    directories: list[Path] = [
        initiative_root,
        initiative_root / "archive",
        initiative_root / "research",
        initiative_root / "ssot",
        initiative_root / "standard",
        initiative_root / "workspace",
    ]
    for phase_index in range(1, phase_count + 1):
        phase_id = f"PH{phase_index:03d}"
        phase_root = initiative_root / "workspace" / phase_id
        directories.append(phase_root)
        for stream_id in stream_ids:
            directories.append(phase_root / stream_id)

    epic_roots: list[Path] = []
    for epic_id in epic_ids or []:
        epic_root = tasks_root / epic_id
        epic_roots.append(epic_root)
        directories.extend(
            [
                epic_root,
                epic_root / "archive",
                epic_root / "research",
                epic_root / "ssot",
                epic_root / "standard",
                epic_root / "workspace",
            ]
        )

    return ScaffoldPlan(root=initiative_root, epic_roots=epic_roots, directories=directories)


def write_report(plan: ScaffoldPlan, dry_run: bool, report_path: Path | None) -> None:
    if report_path is None:
        return
    report_path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Initiative Scaffold Report",
        "",
        f"- Initiative root: `{plan.root}`",
        f"- Epic roots: {len(plan.epic_roots)}",
        f"- Mode: `{'dry-run' if dry_run else 'apply'}`",
        f"- Directories planned: {len(plan.directories)}",
        "",
        "## Directories",
        "",
    ]
    lines.extend(f"- `{directory}`" for directory in plan.directories)
    report_path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create initiative directory scaffolding.")
    parser.add_argument("--initiative-id", required=True, help="Initiative ID, e.g. T104.")
    parser.add_argument(
        "--initiative-code",
        required=True,
        help="Human shorthand code (reserved for future metadata generation).",
    )
    parser.add_argument(
        "--tasks-root",
        default="prompt/artifacts/tasks",
        help="Root directory that contains initiative folders.",
    )
    parser.add_argument("--phase-count", type=int, default=1, help="Number of PH### folders to scaffold.")
    parser.add_argument(
        "--streams",
        default="ST000",
        help="Comma-separated stream IDs per phase, e.g. ST000,ST001,ST007.",
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--dry-run", action="store_true", help="Preview only (default).")
    mode.add_argument("--apply", action="store_true", help="Create directories.")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Allow merge mode when initiative/epic roots already exist in apply mode.",
    )
    parser.add_argument(
        "--epic-ids",
        default=None,
        help="Optional comma-separated epic IDs to scaffold root structures, e.g. T104A,T104B.",
    )
    parser.add_argument(
        "--report-path",
        default=None,
        help=(
            "Report output path (default: prompt/scripts/output/scaffold/<id>/report_<id>_scaffold.md). "
            "Paths inside artifacts/tasks/ are rejected."
        ),
    )
    return parser.parse_args()

def _default_report_path(initiative_id: str) -> Path:
    return SCRIPTS_OUTPUT_ROOT / "scaffold" / initiative_id / f"report_{initiative_id}_scaffold.md"


def main() -> int:
    args = parse_args()
    dry_run = not args.apply

    initiative_id = args.initiative_id.upper().strip()
    if not INITIATIVE_ID_PATTERN.match(initiative_id):
        print(f"❌ Invalid initiative ID: {initiative_id}")
        return 1
    if args.phase_count <= 0:
        print("❌ --phase-count must be greater than zero.")
        return 1
    if not args.initiative_code.strip():
        print("❌ --initiative-code cannot be empty.")
        return 1

    try:
        stream_ids = normalize_streams(args.streams)
    except ValueError as exc:
        print(f"❌ {exc}")
        return 1
    try:
        epic_ids = normalize_epic_ids(args.epic_ids) if args.epic_ids else None
    except ValueError as exc:
        print(f"❌ {exc}")
        return 1

    tasks_root = Path(args.tasks_root).resolve(strict=False)
    plan = build_scaffold_plan(
        tasks_root=tasks_root,
        initiative_id=initiative_id,
        phase_count=args.phase_count,
        stream_ids=stream_ids,
        epic_ids=epic_ids,
    )

    if plan.root.exists() and not dry_run and not args.force:
        print(f"❌ Initiative already exists at {plan.root}")
        return 1
    if not dry_run and not args.force:
        for epic_root in plan.epic_roots:
            if epic_root.exists():
                print(f"❌ Epic already exists at {epic_root} (use --force to merge)")
                return 1

    for directory in plan.directories:
        if dry_run:
            print(f"DRY RUN create: {directory}")
        else:
            directory.mkdir(parents=True, exist_ok=True)
            print(f"CREATED: {directory}")

    report_path = resolve_report_path(args.report_path, _default_report_path, initiative_id)
    write_report(plan=plan, dry_run=dry_run, report_path=report_path)

    print(
        f"✅ Scaffold {'previewed' if dry_run else 'created'} for {initiative_id}: "
        f"{len(plan.directories)} directories."
    )
    print(f"Report: {report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
