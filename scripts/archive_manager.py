#!/usr/bin/env python3
"""
Archive manager for initiative-scoped Convention 8 workflows.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import datetime
import json
import logging
from pathlib import Path
import re
import shutil
import sys
from typing import Any

from report_output import SCRIPTS_OUTPUT_ROOT, resolve_report_path


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

SEMVER_PATTERN = re.compile(r"^\d+\.\d+\.\d+$")
ARCHIVED_STEM_PATTERN = re.compile(r"_v\d+\.\d+\.\d+$")
FRONTMATTER_PATTERN = re.compile(r"\A---\s*\n(?P<frontmatter>.*?)\n---(?:\s*\n|\s*\Z)", re.DOTALL)
FRONTMATTER_VERSION_PATTERN = re.compile(
    r"^version\s*:\s*(?P<quote>['\"]?)(?P<value>[^'\"]+?)(?P=quote)\s*(?:#.*)?$"
)


@dataclass(frozen=True)
class ArchiveOperation:
    original_path: Path
    archive_path: Path
    version: str | None


class ArchiveManager:
    """
    Manage archive operations while preserving existing metadata sidecars.
    """

    def __init__(self, project_root: str | None = None):
        if project_root is None:
            self.project_root = Path(__file__).resolve().parents[2]
        else:
            self.project_root = Path(project_root).expanduser().resolve(strict=False)

    def _resolve_path(self, path_value: str | Path) -> Path:
        path = Path(path_value).expanduser()
        if path.is_absolute():
            return path.resolve(strict=False)
        return (Path.cwd() / path).resolve(strict=False)

    def _resolve_initiative_root(self, doc_path: Path, initiative_root: str | None) -> Path | None:
        if initiative_root:
            root = self._resolve_path(initiative_root)
            if doc_path != root and root not in doc_path.parents:
                raise ValueError(
                    f"Document path is outside initiative root: doc={doc_path}, initiative_root={root}"
                )
            return root

        for candidate in [doc_path.parent, *doc_path.parent.parents]:
            if (
                candidate.parent.name == "tasks"
                and candidate.parent.parent.name == "artifacts"
                and candidate.parent.parent.parent.name == "prompt"
            ):
                return candidate
        return None

    def _legacy_archive_dir(self, doc_path: Path) -> Path:
        normalized = doc_path.as_posix()
        if "prompt/" in normalized:
            return self.project_root / "prompt" / "archive"
        if "documentation/" in normalized:
            return doc_path.parent / "archive"
        return doc_path.parent / "archive"

    def _archive_dir_for_live_doc(self, doc_path: Path, initiative_root: Path | None) -> Path:
        if initiative_root is not None:
            relative = doc_path.relative_to(initiative_root)
            return initiative_root / "archive" / relative.parent
        return self._legacy_archive_dir(doc_path)

    def _build_archive_filename(self, doc_path: Path, deprecated: bool, version: str | None) -> str:
        if deprecated:
            return f"{doc_path.stem}{doc_path.suffix}"
        if version is None:
            raise ValueError("Internal error: versioned archive requires a version.")
        return f"{doc_path.stem}_v{version}{doc_path.suffix}"

    def _resolve_effective_version(
        self,
        doc_path: Path,
        provided_version: str | None,
        deprecated: bool,
    ) -> str | None:
        version = provided_version
        if version is None and not deprecated:
            version = self.extract_frontmatter_version(doc_path)
        if version is None and deprecated:
            return None
        if version is None:
            raise ValueError(
                "Version is required for versioned archive snapshots. "
                "Provide --version or include a frontmatter version field."
            )
        if not SEMVER_PATTERN.match(version):
            raise ValueError(f"Invalid version '{version}'. Expected semantic version format X.Y.Z.")
        return version

    def _build_archive_target(
        self,
        doc_path: Path,
        initiative_root: Path | None,
        deprecated: bool,
        provided_version: str | None,
        enforce_version: str | None = None,
    ) -> tuple[Path, str | None]:
        if ARCHIVED_STEM_PATTERN.search(doc_path.stem):
            raise ValueError(
                "Archive command expects a live file path, but the input appears already archived "
                f"(stem ends with _v#.#.#): {doc_path}"
            )

        effective_version = enforce_version
        if effective_version is None:
            effective_version = self._resolve_effective_version(
                doc_path=doc_path,
                provided_version=provided_version,
                deprecated=deprecated,
            )

        archive_filename = self._build_archive_filename(
            doc_path=doc_path,
            deprecated=deprecated,
            version=effective_version,
        )
        archive_dir = self._archive_dir_for_live_doc(doc_path=doc_path, initiative_root=initiative_root)
        return archive_dir / archive_filename, effective_version

    def _metadata_payload(
        self,
        original_path: Path,
        archive_path: Path,
        version: str | None,
        reason: str | None,
    ) -> dict[str, Any]:
        return {
            "original_path": str(original_path),
            "archive_path": str(archive_path),
            "version": version,
            "archived_date": datetime.now().isoformat(),
            "reason": reason or "Automated archiving",
            "file_size": original_path.stat().st_size,
            "original_modified": datetime.fromtimestamp(original_path.stat().st_mtime).isoformat(),
        }

    def _write_metadata_file(self, archive_path: Path, payload: dict[str, Any]) -> Path:
        metadata_path = archive_path.with_suffix(".metadata.json")
        metadata_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        return metadata_path

    def _write_archive_report(
        self,
        report_path: str,
        dry_run: bool,
        initiative_root: Path | None,
        deprecated: bool,
        operations: list[ArchiveOperation],
    ) -> Path:
        resolved_report = self._resolve_path(report_path)
        resolved_report.parent.mkdir(parents=True, exist_ok=True)

        lines: list[str] = [
            "# Archive Operation Report",
            "",
            f"- Mode: `{'dry-run' if dry_run else 'apply'}`",
            f"- Tier: `{'deprecated' if deprecated else 'versioned'}`",
            f"- Initiative root: `{initiative_root if initiative_root else 'none (legacy mode)'}`",
            f"- Operations: {len(operations)}",
            "",
            "## Planned Operations",
            "",
        ]
        for operation in operations:
            lines.append(f"- `{operation.original_path}` -> `{operation.archive_path}`")
            lines.append(f"  - version: `{operation.version}`")

        resolved_report.write_text("\n".join(lines), encoding="utf-8")
        return resolved_report

    def extract_frontmatter_version(self, doc_path: str | Path) -> str | None:
        path = self._resolve_path(doc_path)
        text = path.read_text(encoding="utf-8")

        match = FRONTMATTER_PATTERN.match(text)
        if not match:
            return None

        frontmatter = match.group("frontmatter")
        for line in frontmatter.splitlines():
            field_match = FRONTMATTER_VERSION_PATTERN.match(line.strip())
            if field_match:
                return field_match.group("value").strip()
        return None

    def archive_document(
        self,
        doc_path: str,
        version: str | None = None,
        reason: str | None = None,
        deprecated: bool = False,
        dry_run: bool = True,
        initiative_root: str | None = None,
        report_path: str | None = None,
    ) -> list[Path]:
        live_path = self._resolve_path(doc_path)
        if not live_path.exists():
            raise FileNotFoundError(f"Document not found: {live_path}")
        if not live_path.is_file():
            raise ValueError(f"Document path is not a file: {live_path}")

        resolved_initiative_root = self._resolve_initiative_root(live_path, initiative_root)
        main_archive_path, effective_version = self._build_archive_target(
            doc_path=live_path,
            initiative_root=resolved_initiative_root,
            deprecated=deprecated,
            provided_version=version,
        )
        operations = [ArchiveOperation(live_path, main_archive_path, effective_version)]

        changelog_path = live_path.with_name(f"changelog_{live_path.stem}.md")
        if changelog_path.exists() and changelog_path.is_file():
            changelog_archive_path, _ = self._build_archive_target(
                doc_path=changelog_path,
                initiative_root=resolved_initiative_root,
                deprecated=deprecated,
                provided_version=effective_version,
                enforce_version=effective_version,
            )
            operations.append(ArchiveOperation(changelog_path, changelog_archive_path, effective_version))

        if report_path:
            report = self._write_archive_report(
                report_path=report_path,
                dry_run=dry_run,
                initiative_root=resolved_initiative_root,
                deprecated=deprecated,
                operations=operations,
            )
            logger.info("Archive report written: %s", report)

        if dry_run:
            for operation in operations:
                logger.info("DRY RUN: %s -> %s", operation.original_path, operation.archive_path)
            return [operation.archive_path for operation in operations]

        archived_paths: list[Path] = []
        for operation in operations:
            operation.archive_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(operation.original_path, operation.archive_path)
            payload = self._metadata_payload(
                original_path=operation.original_path,
                archive_path=operation.archive_path,
                version=operation.version,
                reason=reason,
            )
            self._write_metadata_file(operation.archive_path, payload)
            logger.info("Archived %s -> %s", operation.original_path, operation.archive_path)
            archived_paths.append(operation.archive_path)
        return archived_paths

    def _archive_search_dirs(self) -> list[Path]:
        directories: list[Path] = [
            self.project_root / "prompt" / "archive",
            self.project_root / "documentation" / "archive",
        ]
        tasks_root = self.project_root / "prompt" / "artifacts" / "tasks"
        if tasks_root.exists():
            for item in tasks_root.iterdir():
                if item.is_dir():
                    directories.append(item / "archive")
        return directories

    def list_archives(self, doc_path: str | None = None) -> list[dict[str, Any]]:
        archives: list[dict[str, Any]] = []
        requested_path = self._resolve_path(doc_path) if doc_path else None

        for search_dir in self._archive_search_dirs():
            if not search_dir.exists():
                continue
            for metadata_file in search_dir.rglob("*.metadata.json"):
                try:
                    metadata = json.loads(metadata_file.read_text(encoding="utf-8"))
                except Exception as exc:
                    logger.error("Failed to read metadata %s: %s", metadata_file, exc)
                    continue

                if requested_path is not None:
                    original_path_raw = str(metadata.get("original_path", "")).strip()
                    try:
                        original_path = self._resolve_path(original_path_raw)
                    except Exception:
                        original_path = Path(original_path_raw)
                    if requested_path != original_path and str(requested_path) not in original_path_raw:
                        continue
                archives.append(metadata)

        archives.sort(key=lambda item: str(item.get("archived_date", "")), reverse=True)
        return archives

    def _version_archive_dir_for_doc(self, doc_path: Path, initiative_root: str | None) -> Path:
        resolved_initiative_root = self._resolve_initiative_root(doc_path, initiative_root)
        return self._archive_dir_for_live_doc(doc_path, resolved_initiative_root)

    def clean_old_archives(
        self,
        doc_path: str,
        keep_versions: int = 3,
        initiative_root: str | None = None,
    ) -> list[Path]:
        live_path = self._resolve_path(doc_path)
        archive_dir = self._version_archive_dir_for_doc(live_path, initiative_root)
        if not archive_dir.exists():
            return []

        pattern = re.compile(
            rf"^{re.escape(live_path.stem)}_v(\d+\.\d+\.\d+){re.escape(live_path.suffix)}$"
        )
        archived_versions: list[tuple[tuple[int, int, int], Path]] = []

        for file_path in archive_dir.glob(f"{live_path.stem}_v*{live_path.suffix}"):
            match = pattern.match(file_path.name)
            if not match:
                continue
            version_parts = tuple(int(part) for part in match.group(1).split("."))
            archived_versions.append((version_parts, file_path))

        if len(archived_versions) <= keep_versions:
            return []

        archived_versions.sort(key=lambda entry: entry[0])
        to_remove = archived_versions[:-keep_versions]

        removed_paths: list[Path] = []
        for _, file_path in to_remove:
            file_path.unlink()
            metadata_path = file_path.with_suffix(".metadata.json")
            if metadata_path.exists():
                metadata_path.unlink()
            removed_paths.append(file_path)
            logger.info("Removed old archive: %s", file_path)
        return removed_paths

    def restore_archive(self, archive_path: str, target_path: str | None = None) -> Path:
        archive_path_obj = self._resolve_path(archive_path)

        if not archive_path_obj.exists():
            raise FileNotFoundError(f"Archive not found: {archive_path_obj}")

        metadata_path = archive_path_obj.with_suffix(".metadata.json")
        if metadata_path.exists():
            metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
            original_path = self._resolve_path(str(metadata["original_path"]))
        else:
            logger.warning("No metadata found for %s, using fallback restoration", archive_path_obj)
            original_path = archive_path_obj.parent.parent / archive_path_obj.name

        restore_path = self._resolve_path(target_path) if target_path else original_path
        restore_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(archive_path_obj, restore_path)

        logger.info("Restored %s to %s", archive_path_obj, restore_path)
        return restore_path

    def get_next_version(
        self,
        doc_path: str,
        change_type: str = "minor",
        initiative_root: str | None = None,
    ) -> str:
        live_path = self._resolve_path(doc_path)
        archive_dir = self._version_archive_dir_for_doc(live_path, initiative_root)
        if not archive_dir.exists():
            return "1.0.0"

        pattern = re.compile(
            rf"^{re.escape(live_path.stem)}_v(\d+\.\d+\.\d+){re.escape(live_path.suffix)}$"
        )
        versions: list[tuple[int, int, int]] = []

        for file_path in archive_dir.glob(f"{live_path.stem}_v*{live_path.suffix}"):
            match = pattern.match(file_path.name)
            if not match:
                continue
            versions.append(tuple(int(part) for part in match.group(1).split(".")))

        if not versions:
            return "1.0.0"

        major, minor, patch = max(versions)
        if change_type == "major":
            return f"{major + 1}.0.0"
        if change_type == "minor":
            return f"{major}.{minor + 1}.0"
        return f"{major}.{minor}.{patch + 1}"


def create_cli_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Archive manager for convention-aligned repository artifacts.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python archive_manager.py archive prompt/artifacts/tasks/T104/ssot/sps_T104-CWS.md --apply
  python archive_manager.py archive --path prompt/artifacts/tasks/T104/ssot/sps_T104-CWS.md --version 2.0.0 --apply
  python archive_manager.py list --path prompt/artifacts/tasks/T104/ssot/sps_T104-CWS.md
  python archive_manager.py clean --path prompt/artifacts/tasks/T104/ssot/sps_T104-CWS.md --keep 2
  python archive_manager.py next-version --path prompt/artifacts/tasks/T104/ssot/sps_T104-CWS.md --type minor
""",
    )
    parser.add_argument("--project-root", help="Repository/project root path override.")

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    archive_parser = subparsers.add_parser("archive", help="Archive a document")
    archive_parser.add_argument("doc_path", nargs="?", help="Path to a live document to archive.")
    archive_parser.add_argument("--path", help="Deprecated alias for positional doc_path.")
    archive_parser.add_argument("--version", help="Semantic version override for versioned snapshots.")
    archive_parser.add_argument("--reason", help="Reason for archiving.")
    archive_parser.add_argument(
        "--initiative-root",
        help="Optional initiative root override (for mirrored archive resolution).",
    )
    archive_parser.add_argument(
        "--deprecated",
        action="store_true",
        help="Archive as deprecated artifact without _v#.#.# filename suffix.",
    )
    mode_group = archive_parser.add_mutually_exclusive_group()
    mode_group.add_argument("--dry-run", action="store_true", help="Preview archive operations (default).")
    mode_group.add_argument("--apply", action="store_true", help="Execute archive operations.")
    archive_parser.add_argument(
        "--report-path",
        help=(
            "Report output path (default: prompt/scripts/output/archive/report_archive_<doc>.md). "
            "Paths inside artifacts/tasks/ are rejected."
        ),
    )

    list_parser = subparsers.add_parser("list", help="List archives")
    list_parser.add_argument("--path", help="Filter results by original live document path.")

    clean_parser = subparsers.add_parser("clean", help="Clean old archive versions")
    clean_parser.add_argument("--path", required=True, help="Path to the live document.")
    clean_parser.add_argument("--keep", type=int, default=3, help="Number of versions to keep.")
    clean_parser.add_argument(
        "--initiative-root",
        help="Optional initiative root override (for mirrored archive resolution).",
    )

    restore_parser = subparsers.add_parser("restore", help="Restore an archive file")
    restore_parser.add_argument("--archive", required=True, help="Path to archived file.")
    restore_parser.add_argument("--target", help="Restore target path. Defaults to metadata original_path.")

    version_parser = subparsers.add_parser("next-version", help="Get next semantic version")
    version_parser.add_argument("--path", required=True, help="Path to the live document.")
    version_parser.add_argument(
        "--type",
        choices=["major", "minor", "patch"],
        default="minor",
        help="Version bump type.",
    )
    version_parser.add_argument(
        "--initiative-root",
        help="Optional initiative root override (for mirrored archive resolution).",
    )

    return parser

def _default_report_path(doc_stem: str) -> Path:
    return SCRIPTS_OUTPUT_ROOT / "archive" / f"report_archive_{doc_stem}.md"


def main() -> int:
    parser = create_cli_parser()
    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        return 1

    archive_manager = ArchiveManager(project_root=args.project_root)

    try:
        if args.command == "archive":
            doc_path = args.doc_path or args.path
            if not doc_path:
                raise ValueError(
                    "Missing document path. Use positional argument: "
                    "archive_manager.py archive <path-to-live-file>"
                )

            if args.path and not args.doc_path:
                print(
                    "Warning: --path is deprecated; use positional argument instead: "
                    "archive_manager.py archive <path-to-live-file>.",
                    file=sys.stderr,
                )
            if args.path and args.doc_path and args.path != args.doc_path:
                raise ValueError("Conflicting path inputs: positional doc_path and --path do not match.")

            dry_run = not args.apply
            report_path = resolve_report_path(args.report_path, _default_report_path, Path(doc_path).stem)
            archived_paths = archive_manager.archive_document(
                doc_path=doc_path,
                version=args.version,
                reason=args.reason,
                deprecated=args.deprecated,
                dry_run=dry_run,
                initiative_root=args.initiative_root,
                report_path=str(report_path),
            )
            if dry_run:
                print("✅ Dry-run complete. Planned archive targets:")
            else:
                print("✅ Archive complete:")
            for archived_path in archived_paths:
                print(f"  {archived_path}")
            return 0

        if args.command == "list":
            archives = archive_manager.list_archives(args.path)
            if archives:
                print(f"Found {len(archives)} archive(s):")
                for archive in archives:
                    version = archive.get("version")
                    version_label = version if version else "deprecated"
                    print(
                        f"  {archive.get('original_path')} v{version_label} "
                        f"({archive.get('archived_date', 'unknown-date')})"
                    )
            else:
                print("No archives found")
            return 0

        if args.command == "clean":
            removed = archive_manager.clean_old_archives(
                doc_path=args.path,
                keep_versions=args.keep,
                initiative_root=args.initiative_root,
            )
            print(f"✅ Removed {len(removed)} old archive(s)")
            for path in removed:
                print(f"  Removed: {path}")
            return 0

        if args.command == "restore":
            restore_path = archive_manager.restore_archive(args.archive, args.target)
            print(f"✅ Archive restored to: {restore_path}")
            return 0

        if args.command == "next-version":
            next_version = archive_manager.get_next_version(
                doc_path=args.path,
                change_type=args.type,
                initiative_root=args.initiative_root,
            )
            print(next_version)
            return 0

    except Exception as exc:
        logger.error("Command failed: %s", exc)
        print(f"❌ Command failed: {exc}")
        return 1

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
