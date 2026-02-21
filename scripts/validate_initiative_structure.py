#!/usr/bin/env python3
"""
Validate initiative directory structure against ST007 conventions.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import re


PHASE_DIR_PATTERN = re.compile(r"^PH\d{3}$")
STREAM_DIR_PATTERN = re.compile(r"^ST\d{3}$")
ACTIVITY_DIR_PATTERN = re.compile(r"^AC\d{3}$")
AC_TOKEN_PATTERN = re.compile(r"(AC\d{3})")
RAW_FILE_PATTERN = re.compile(r"^raw_[A-Z0-9-]+-SES\d{3}\.(?:md|txt)$")
RESEARCH_DIR_PATTERN = re.compile(r"^[A-Z0-9-]+-RES-\d{3}$")
TYPE_FIRST_WORKSPACE_DIRS = {"plan", "notes", "roadmap", "analysis", "proposal", "external"}
WORKSPACE_ALLOWED_NON_PHASE_DIRS = {"_unresolved", "verification"}
STREAM_TYPE_DIRS = {"raw", "proposal", "analysis", "communication", "snotes"}
ACTIVITY_TYPE_DIRS = {"raw", "snotes", "verification", "dev-report"}
ALLOWED_PREFIXES = (
    "analysis_",
    "plan_",
    "notes_",
    "snotes_",
    "proposal_",
    "report_",
    "brief_",
    "raw_",
    "comm_",
    "changelog_",
    "standard_",
    "roadmap_",
    "sps_",
    "concept_",
    "verification_",
    "dev-report_",
)


@dataclass
class ValidationResult:
    errors: list[str]
    warnings: list[str]
    infos: list[str]

    def as_markdown(self, root: Path) -> str:
        lines: list[str] = []
        lines.append("# Initiative Structure Validation Report")
        lines.append("")
        lines.append(f"- Root: `{root}`")
        lines.append(f"- Errors: {len(self.errors)}")
        lines.append(f"- Warnings: {len(self.warnings)}")
        lines.append("")
        if self.errors:
            lines.append("## Errors")
            lines.extend(f"- {item}" for item in self.errors)
            lines.append("")
        if self.warnings:
            lines.append("## Warnings")
            lines.extend(f"- {item}" for item in self.warnings)
            lines.append("")
        if self.infos:
            lines.append("## Info")
            lines.extend(f"- {item}" for item in self.infos)
            lines.append("")
        return "\n".join(lines)


class InitiativeValidator:
    def __init__(self, root: Path, strict: bool) -> None:
        self.root = root
        self.strict = strict
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.infos: list[str] = []

    def validate(self) -> ValidationResult:
        self._validate_root()
        self._validate_ssot_contents()
        self._validate_no_root_raw()
        self._validate_no_type_first_dirs()
        self._validate_workspace_timeline()
        self._validate_research_layout()
        self._validate_file_prefixes()
        self._validate_raw_transcripts()
        self._validate_uid_scope_placement()
        return ValidationResult(errors=self.errors, warnings=self.warnings, infos=self.infos)

    def _validate_root(self) -> None:
        required = ("archive", "research", "ssot", "standard", "workspace")
        if not self.root.exists():
            self.errors.append(f"Initiative root does not exist: {self.root}")
            return
        for name in required:
            path = self.root / name
            if not path.exists() or not path.is_dir():
                self.errors.append(f"Missing required directory: {path}")

    def _validate_ssot_contents(self) -> None:
        ssot = self.root / "ssot"
        if not ssot.exists():
            return
        has_sps = any(path.name.startswith("sps_") for path in ssot.glob("*.md"))
        has_concept = any(path.name.startswith("concept_") for path in ssot.glob("*.md"))
        if not has_sps:
            self.errors.append("SSOT is missing required `sps_*.md` artifact.")
        if not has_concept:
            self.errors.append("SSOT is missing required `concept_*.md` artifact.")

    def _validate_no_root_raw(self) -> None:
        root_raw = self.root / "raw"
        if root_raw.exists():
            self.errors.append("Root raw/ directory is not allowed; raw must be scoped under workspace timeline.")

    def _validate_no_type_first_dirs(self) -> None:
        workspace = self.root / "workspace"
        if not workspace.exists():
            return
        for child in workspace.iterdir():
            if not child.is_dir():
                continue
            if child.name in TYPE_FIRST_WORKSPACE_DIRS:
                self.errors.append(
                    f"Workspace contains forbidden type-first directory: "
                    f"{child.relative_to(self.root)}"
                )

    def _validate_workspace_timeline(self) -> None:
        workspace = self.root / "workspace"
        if not workspace.exists():
            return
        phase_dirs = [
            item
            for item in workspace.iterdir()
            if item.is_dir() and item.name not in WORKSPACE_ALLOWED_NON_PHASE_DIRS
        ]
        if not phase_dirs:
            self.warnings.append("No phase directories found under workspace/.")
            return
        for phase_dir in phase_dirs:
            if not PHASE_DIR_PATTERN.match(phase_dir.name):
                self.warnings.append(f"Non-canonical phase directory: {phase_dir.relative_to(self.root)}")
                continue
            stream_dirs = [item for item in phase_dir.iterdir() if item.is_dir()]
            if not stream_dirs:
                self.warnings.append(f"Phase has no stream directories: {phase_dir.relative_to(self.root)}")
            for stream_dir in stream_dirs:
                if not STREAM_DIR_PATTERN.match(stream_dir.name):
                    self.warnings.append(
                        f"Non-canonical stream directory: {stream_dir.relative_to(self.root)}"
                    )
                    continue
                self._validate_stream_contents(stream_dir)

    def _validate_stream_contents(self, stream_dir: Path) -> None:
        for child in stream_dir.iterdir():
            if not child.is_dir():
                continue
            if child.name in STREAM_TYPE_DIRS:
                continue
            if ACTIVITY_DIR_PATTERN.match(child.name):
                self._validate_activity_contents(child)
                continue
            self.errors.append(
                f"Invalid activity/type directory under stream (expected AC### or known type dir): "
                f"{child.relative_to(self.root)}"
            )

    def _validate_activity_contents(self, activity_dir: Path) -> None:
        for child in activity_dir.iterdir():
            if not child.is_dir():
                continue
            if child.name in ACTIVITY_TYPE_DIRS:
                continue
            self.errors.append(
                f"Invalid type directory under activity (expected known type dir): "
                f"{child.relative_to(self.root)}"
            )

    def _validate_research_layout(self) -> None:
        research_root = self.root / "research"
        if not research_root.exists():
            return
        for child in research_root.iterdir():
            if not child.is_dir():
                self.warnings.append(f"Non-directory item under research/: {child.relative_to(self.root)}")
                continue
            if child.name in {"brief", "report"}:
                self.errors.append(
                    f"Legacy type-first research directory not allowed: {child.relative_to(self.root)}; "
                    "use research/<S-RES>/ with paired brief/report files."
                )
                continue
            if not RESEARCH_DIR_PATTERN.match(child.name):
                self.warnings.append(
                    f"Research directory does not follow <S-RES> convention: {child.relative_to(self.root)}"
                )
                continue
            has_brief = any(path.name.startswith("brief_") for path in child.glob("brief_*.md"))
            has_report = any(path.name.startswith("report_") for path in child.glob("report_*.md"))
            if not has_brief:
                self.errors.append(f"Research directory missing brief artifact: {child.relative_to(self.root)}")
            if not has_report:
                self.errors.append(f"Research directory missing report artifact: {child.relative_to(self.root)}")

    def _validate_file_prefixes(self) -> None:
        for file_path in self.root.rglob("*"):
            if not file_path.is_file():
                continue
            if file_path.suffix.lower() not in {".md", ".txt"}:
                continue
            file_name = file_path.name
            if file_name.startswith("."):
                continue
            if any(file_name.startswith(prefix) for prefix in ALLOWED_PREFIXES):
                continue
            if file_path.suffix.lower() == ".txt":
                self.errors.append(
                    f"Unrecognized .txt file prefix (expected canonical stem): {file_path.relative_to(self.root)}"
                )
            else:
                self.warnings.append(
                    f"Unrecognized markdown prefix (check convention): {file_path.relative_to(self.root)}"
                )

    def _validate_raw_transcripts(self) -> None:
        for file_path in self.root.rglob("raw_*"):
            if file_path.suffix.lower() not in {".md", ".txt"}:
                continue
            if not RAW_FILE_PATTERN.match(file_path.name):
                self.errors.append(
                    f"Raw transcript missing canonical SES token format: {file_path.relative_to(self.root)}"
                )

    def _validate_uid_scope_placement(self) -> None:
        workspace = self.root / "workspace"
        if not workspace.exists():
            return

        for file_path in workspace.rglob("*"):
            if not file_path.is_file():
                continue
            if file_path.suffix.lower() not in {".md", ".txt"}:
                continue

            token_match = AC_TOKEN_PATTERN.search(file_path.name)
            if not token_match:
                continue
            expected_activity = token_match.group(1)

            try:
                relative = file_path.relative_to(workspace)
            except ValueError:
                continue

            stream_index = None
            for idx, part in enumerate(relative.parts):
                if STREAM_DIR_PATTERN.match(part):
                    stream_index = idx
                    break
            if stream_index is None:
                continue

            activity_parts = [
                part
                for idx, part in enumerate(relative.parts)
                if idx > stream_index and ACTIVITY_DIR_PATTERN.match(part)
            ]

            if not activity_parts:
                self.errors.append(
                    "AC-scoped file is not placed under an activity directory "
                    f"(UID-scope rule): {file_path.relative_to(self.root)}"
                )
                continue

            actual_activity = activity_parts[0]
            if actual_activity != expected_activity:
                self.errors.append(
                    "AC-scoped file activity directory does not match UID token "
                    f"(expected {expected_activity}, found {actual_activity}): "
                    f"{file_path.relative_to(self.root)}"
                )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate initiative structure conventions.")
    parser.add_argument(
        "--initiative-root",
        required=True,
        help="Path to initiative root directory (e.g., prompt/artifacts/tasks/T104).",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat AC threshold warnings as hard errors.",
    )
    parser.add_argument(
        "--report-path",
        default=None,
        help="Optional markdown output report path.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.initiative_root).resolve(strict=False)
    validator = InitiativeValidator(root=root, strict=args.strict)
    result = validator.validate()
    report = result.as_markdown(root=root)
    print(report)

    if args.report_path:
        report_path = Path(args.report_path).resolve(strict=False)
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(report, encoding="utf-8")
        print(f"Report written to: {report_path}")

    if result.errors:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
