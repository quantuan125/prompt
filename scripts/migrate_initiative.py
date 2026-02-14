#!/usr/bin/env python3
"""
Manifest-driven initiative migration tool.

This script executes deterministic move operations for an initiative and can
optionally rewrite repository path references based on the same manifest.
"""

from __future__ import annotations

import argparse
import difflib
import json
from dataclasses import dataclass
from pathlib import Path
import re
import shutil
from typing import Iterable


EXCLUDE_DIRS = {".git", "__pycache__", "node_modules", "venv", ".pytest_cache"}
DEFAULT_FILE_EXTENSIONS = {".md", ".py", ".json", ".sh", ".yaml", ".yml", ".txt"}


@dataclass(frozen=True)
class MoveOperation:
    source: str
    target: str


@dataclass(frozen=True)
class TokenRewrite:
    old: str
    new: str


@dataclass(frozen=True)
class MigrationManifest:
    moves: list[MoveOperation]
    rewrites: list[TokenRewrite]


def _ensure_relative(path_value: str, root: Path) -> Path:
    rel = Path(path_value)
    if rel.is_absolute():
        raise ValueError(f"Absolute paths are not allowed in manifest: {path_value}")
    resolved = (root / rel).resolve(strict=False)
    root_resolved = root.resolve(strict=False)
    if resolved != root_resolved and root_resolved not in resolved.parents:
        raise ValueError(f"Path escapes project root: {path_value}")
    return resolved


def _normalize_for_text(path_value: str) -> str:
    return path_value.replace("\\", "/").strip()


def load_manifest(manifest_path: Path) -> MigrationManifest:
    try:
        data = json.loads(manifest_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON manifest: {exc}") from exc

    move_items: list[MoveOperation] = []
    rewrite_items: list[TokenRewrite] = []

    if isinstance(data, list):
        for item in data:
            if not isinstance(item, dict):
                raise ValueError("Manifest list entries must be objects with from/to fields.")
            source = item.get("from")
            target = item.get("to")
            if not source or not target:
                raise ValueError("Each manifest move must include non-empty from/to values.")
            move_items.append(MoveOperation(source=source, target=target))
    elif isinstance(data, dict):
        operations = data.get("operations", [])
        if not isinstance(operations, list):
            raise ValueError("Manifest 'operations' must be a list.")
        for item in operations:
            if not isinstance(item, dict):
                raise ValueError("Manifest operations entries must be objects with from/to fields.")
            action = item.get("action", "move")
            if action != "move":
                continue
            source = item.get("from")
            target = item.get("to")
            if not source or not target:
                raise ValueError("Move operations must include non-empty from/to values.")
            move_items.append(MoveOperation(source=source, target=target))

        rewrites = data.get("reference_rewrites", [])
        if rewrites:
            if not isinstance(rewrites, list):
                raise ValueError("Manifest 'reference_rewrites' must be a list.")
            for item in rewrites:
                if not isinstance(item, dict):
                    raise ValueError("reference_rewrites entries must be objects with old/new fields.")
                old = item.get("old")
                new = item.get("new")
                if not old or not new:
                    raise ValueError("reference_rewrites entries must include non-empty old/new values.")
                rewrite_items.append(TokenRewrite(old=old, new=new))
    else:
        raise ValueError("Manifest root must be an object or list.")

    if not move_items:
        raise ValueError("Manifest has no move operations.")

    if not rewrite_items:
        rewrite_items = [TokenRewrite(old=m.source, new=m.target) for m in move_items]

    return MigrationManifest(moves=move_items, rewrites=rewrite_items)


def validate_moves(manifest: MigrationManifest, project_root: Path, allow_missing_sources: bool) -> list[str]:
    errors: list[str] = []
    seen_sources: set[str] = set()
    seen_targets: set[str] = set()

    resolved_sources: list[Path] = []
    resolved_targets: list[Path] = []

    for move in manifest.moves:
        if move.source == move.target:
            errors.append(f"Invalid move with identical source/target: {move.source}")
            continue
        if move.source in seen_sources:
            errors.append(f"Duplicate source in manifest: {move.source}")
        if move.target in seen_targets:
            errors.append(f"Duplicate target in manifest: {move.target}")
        seen_sources.add(move.source)
        seen_targets.add(move.target)

        try:
            source_path = _ensure_relative(move.source, project_root)
            target_path = _ensure_relative(move.target, project_root)
        except ValueError as exc:
            errors.append(str(exc))
            continue

        if not allow_missing_sources and not source_path.exists():
            errors.append(f"Source path does not exist: {move.source}")
        if target_path.exists():
            errors.append(f"Target path already exists: {move.target}")
        resolved_sources.append(source_path)
        resolved_targets.append(target_path)

    for i, source_a in enumerate(resolved_sources):
        for source_b in resolved_sources[i + 1 :]:
            if source_a in source_b.parents or source_b in source_a.parents:
                errors.append(
                    f"Overlapping move sources detected: {source_a.relative_to(project_root)} and "
                    f"{source_b.relative_to(project_root)}"
                )
    return errors


def execute_moves(
    manifest: MigrationManifest,
    project_root: Path,
    dry_run: bool,
) -> list[str]:
    logs: list[str] = []
    sorted_moves = sorted(manifest.moves, key=lambda item: len(item.source), reverse=True)
    for move in sorted_moves:
        source = _ensure_relative(move.source, project_root)
        target = _ensure_relative(move.target, project_root)
        if dry_run:
            logs.append(f"DRY RUN move: {move.source} -> {move.target}")
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(source), str(target))
        logs.append(f"APPLIED move: {move.source} -> {move.target}")
    return logs


def discover_candidate_files(scope_root: Path, extensions: set[str]) -> Iterable[Path]:
    for root, dirs, files in __import__("os").walk(scope_root):
        dirs[:] = [name for name in dirs if name not in EXCLUDE_DIRS]
        for file_name in files:
            path = Path(root) / file_name
            if path.suffix in extensions:
                yield path


def apply_reference_rewrites(
    rewrites: list[TokenRewrite],
    project_root: Path,
    scope_root: Path,
    dry_run: bool,
    max_files_changed: int | None,
) -> tuple[int, list[str]]:
    changed_files = 0
    reports: list[str] = []
    ordered_rewrites = sorted(
        rewrites,
        key=lambda item: len(item.old),
        reverse=True,
    )

    normalized_pairs = [
        (re.compile(re.escape(_normalize_for_text(item.old))), _normalize_for_text(item.new))
        for item in ordered_rewrites
    ]

    for file_path in discover_candidate_files(scope_root, DEFAULT_FILE_EXTENSIONS):
        try:
            original = file_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            try:
                original = file_path.read_text(encoding="utf-8", errors="ignore")
            except OSError:
                continue
        except OSError:
            continue
        updated = original
        for pattern, replacement in normalized_pairs:
            updated = pattern.sub(replacement, updated)
        if updated == original:
            continue

        changed_files += 1
        if max_files_changed is not None and changed_files > max_files_changed:
            raise RuntimeError(
                f"Reference update exceeded max-files-changed={max_files_changed}. "
                f"Stopped after touching {changed_files} files."
            )

        diff = difflib.unified_diff(
            original.splitlines(),
            updated.splitlines(),
            fromfile=str(file_path.relative_to(project_root)),
            tofile=str(file_path.relative_to(project_root)),
            lineterm="",
        )
        reports.append("\n".join(diff))
        if not dry_run:
            file_path.write_text(updated, encoding="utf-8")
    return changed_files, reports


def create_report(
    manifest: MigrationManifest,
    move_logs: list[str],
    rewrite_files_changed: int,
    rewrite_diffs: list[str],
    dry_run: bool,
    report_path: Path | None,
) -> None:
    if report_path is None:
        return
    report_path.parent.mkdir(parents=True, exist_ok=True)
    lines: list[str] = []
    lines.append("# Initiative Migration Report")
    lines.append("")
    lines.append(f"- Mode: {'dry-run' if dry_run else 'apply'}")
    lines.append(f"- Move operations: {len(manifest.moves)}")
    lines.append(f"- Reference rewrite rules: {len(manifest.rewrites)}")
    lines.append(f"- Files changed by rewrites: {rewrite_files_changed}")
    lines.append("")
    lines.append("## Move Execution Log")
    lines.append("")
    for log_entry in move_logs:
        lines.append(f"- {log_entry}")
    lines.append("")
    lines.append("## Rewrite Diffs")
    lines.append("")
    if rewrite_diffs:
        for diff in rewrite_diffs:
            lines.append("```diff")
            lines.append(diff)
            lines.append("```")
            lines.append("")
    else:
        lines.append("_No reference rewrites needed._")
    report_path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Execute initiative migration operations from a manifest JSON file."
    )
    parser.add_argument("--manifest", required=True, help="Path to migration manifest JSON file.")
    parser.add_argument(
        "--project-root",
        default=".",
        help="Repository root used to resolve manifest relative paths.",
    )
    parser.add_argument(
        "--scope-root",
        default="prompt",
        help="Directory scanned for reference rewrites.",
    )
    parser.add_argument(
        "--skip-reference-updates",
        action="store_true",
        help="Skip reference rewrite pass.",
    )
    parser.add_argument(
        "--max-files-changed",
        type=int,
        default=500,
        help="Safety cap for rewrite-modified files.",
    )
    parser.add_argument(
        "--allow-missing-sources",
        action="store_true",
        help="Allow manifest source paths that do not exist at runtime.",
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--dry-run", action="store_true", help="Preview only (default).")
    mode.add_argument("--apply", action="store_true", help="Apply file moves and rewrites.")
    parser.add_argument(
        "--report-path",
        default=None,
        help="Optional markdown report output path.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    dry_run = not args.apply
    manifest_path = Path(args.manifest).resolve(strict=False)
    project_root = Path(args.project_root).resolve(strict=False)
    scope_root = (project_root / args.scope_root).resolve(strict=False)
    report_path = Path(args.report_path).resolve(strict=False) if args.report_path else None

    manifest = load_manifest(manifest_path)
    validation_errors = validate_moves(
        manifest=manifest,
        project_root=project_root,
        allow_missing_sources=args.allow_missing_sources,
    )
    if validation_errors:
        print("❌ Manifest validation failed:")
        for error in validation_errors:
            print(f" - {error}")
        return 1

    move_logs = execute_moves(manifest=manifest, project_root=project_root, dry_run=dry_run)

    changed_files = 0
    rewrite_diffs: list[str] = []
    if not args.skip_reference_updates:
        changed_files, rewrite_diffs = apply_reference_rewrites(
            rewrites=manifest.rewrites,
            project_root=project_root,
            scope_root=scope_root,
            dry_run=dry_run,
            max_files_changed=args.max_files_changed,
        )

    create_report(
        manifest=manifest,
        move_logs=move_logs,
        rewrite_files_changed=changed_files,
        rewrite_diffs=rewrite_diffs,
        dry_run=dry_run,
        report_path=report_path,
    )

    print(
        f"✅ Migration {'previewed' if dry_run else 'applied'}: "
        f"{len(manifest.moves)} moves, {changed_files} rewrite file updates."
    )
    if report_path:
        print(f"Report: {report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
