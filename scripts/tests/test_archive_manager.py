from __future__ import annotations

from pathlib import Path

from conftest import ARCHIVE_SCRIPT, run_script


def _write_live_doc(doc_path: Path, version: str = "1.2.3") -> None:
    doc_path.parent.mkdir(parents=True, exist_ok=True)
    doc_path.write_text(
        "---\n"
        f"version: '{version}'\n"
        "---\n"
        "\n"
        "# Sample\n",
        encoding="utf-8",
    )


def test_dry_run_routes_versioned_archive_to_flat_tier(tmp_path: Path) -> None:
    project_root = tmp_path / "repo"
    live_doc = project_root / "prompt/artifacts/tasks/P/workspace/PH000/ST001/plan_P-PH000-ST001.md"
    _write_live_doc(live_doc)

    report_path = project_root / "reports/versioned.md"
    result = run_script(
        [
            "python3",
            str(ARCHIVE_SCRIPT),
            "--project-root",
            str(project_root),
            "archive",
            str(live_doc),
            "--initiative-root",
            str(project_root / "prompt/artifacts/tasks/P"),
            "--dry-run",
            "--report-path",
            str(report_path),
        ]
    )

    assert result.returncode == 0, result.stderr or result.stdout
    report = report_path.read_text(encoding="utf-8")
    assert "archive/versioned/plan_P-PH000-ST001_v1.2.3.md" in report
    assert "archive/workspace/PH000/ST001" not in report


def test_dry_run_routes_deprecated_archive_to_flat_tier_with_changelog_pair(tmp_path: Path) -> None:
    project_root = tmp_path / "repo"
    live_doc = project_root / "prompt/artifacts/tasks/P/workspace/PH000/ST001/plan_P-PH000-ST001.md"
    _write_live_doc(live_doc)
    changelog = live_doc.with_name("changelog_plan_P-PH000-ST001.md")
    changelog.write_text("# Changelog\n", encoding="utf-8")

    report_path = project_root / "reports/deprecated.md"
    result = run_script(
        [
            "python3",
            str(ARCHIVE_SCRIPT),
            "--project-root",
            str(project_root),
            "archive",
            str(live_doc),
            "--initiative-root",
            str(project_root / "prompt/artifacts/tasks/P"),
            "--deprecated",
            "--dry-run",
            "--report-path",
            str(report_path),
        ]
    )

    assert result.returncode == 0, result.stderr or result.stdout
    report = report_path.read_text(encoding="utf-8")
    assert "archive/deprecated/plan_P-PH000-ST001.md" in report
    assert "archive/deprecated/changelog_plan_P-PH000-ST001.md" in report
    assert "_v1.2.3" not in report
