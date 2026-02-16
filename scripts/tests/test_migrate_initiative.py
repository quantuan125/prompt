from __future__ import annotations

import json
from pathlib import Path

from conftest import MIGRATE_SCRIPT, run_script, write_manifest


def _setup_repo(tmp_path: Path) -> tuple[Path, Path]:
    project_root = tmp_path / "repo"
    prompt_root = project_root / "prompt"
    prompt_root.mkdir(parents=True, exist_ok=True)
    return project_root, prompt_root


def test_apply_generates_rollback_and_removes_empty_source_dirs(tmp_path: Path) -> None:
    project_root, prompt_root = _setup_repo(tmp_path)
    source_file = prompt_root / "artifacts/tasks/T104/workspace/plan/legacy.md"
    source_file.parent.mkdir(parents=True, exist_ok=True)
    source_file.write_text("legacy", encoding="utf-8")

    manifest_path = project_root / "manifest.json"
    write_manifest(
        manifest_path,
        operations=[
            {
                "action": "move",
                "from": "prompt/artifacts/tasks/T104/workspace/plan/legacy.md",
                "to": "prompt/artifacts/tasks/T104/workspace/PH001/ST001/plan_legacy.md",
            }
        ],
    )

    report_path = project_root / "reports/apply.md"
    result = run_script(
        [
            "python3",
            str(MIGRATE_SCRIPT),
            "--manifest",
            str(manifest_path),
            "--project-root",
            str(project_root),
            "--apply",
            "--report-path",
            str(report_path),
        ]
    )
    assert result.returncode == 0, result.stderr or result.stdout

    rollback_path = report_path.parent / "rollback_manifest.json"
    assert rollback_path.exists(), "expected rollback manifest next to report output"
    rollback_payload = json.loads(rollback_path.read_text(encoding="utf-8"))
    assert rollback_payload.get("operations"), "rollback manifest must contain reverse operations"

    assert not source_file.parent.exists(), "empty source directory should be removed after apply"


def test_dry_run_report_uses_post_move_paths_for_rewrite_diffs(tmp_path: Path) -> None:
    project_root, prompt_root = _setup_repo(tmp_path)
    source_file = prompt_root / "docs/legacy.md"
    source_file.parent.mkdir(parents=True, exist_ok=True)
    source_file.write_text("see prompt/docs/legacy.md", encoding="utf-8")

    manifest_path = project_root / "manifest.json"
    write_manifest(
        manifest_path,
        operations=[
            {
                "action": "move",
                "from": "prompt/docs/legacy.md",
                "to": "prompt/docs/new.md",
            }
        ],
        rewrites=[{"old": "prompt/docs/legacy.md", "new": "prompt/docs/new.md"}],
    )

    report_path = project_root / "reports/dry-run.md"
    result = run_script(
        [
            "python3",
            str(MIGRATE_SCRIPT),
            "--manifest",
            str(manifest_path),
            "--project-root",
            str(project_root),
            "--dry-run",
            "--report-path",
            str(report_path),
        ]
    )
    assert result.returncode == 0, result.stderr or result.stdout
    report = report_path.read_text(encoding="utf-8")
    assert "prompt/docs/new.md" in report, "dry-run rewrite diff should reflect post-move file path"


def test_apply_skips_non_utf8_reference_files_without_modifying_bytes(tmp_path: Path) -> None:
    project_root, prompt_root = _setup_repo(tmp_path)
    source_file = prompt_root / "docs/legacy.md"
    source_file.parent.mkdir(parents=True, exist_ok=True)
    source_file.write_text("see prompt/docs/legacy.md", encoding="utf-8")

    binary_target = prompt_root / "notes/binary.txt"
    binary_target.parent.mkdir(parents=True, exist_ok=True)
    original_bytes = b"\xff\xfe\x00 prompt/docs/legacy.md \xff"
    binary_target.write_bytes(original_bytes)

    manifest_path = project_root / "manifest.json"
    write_manifest(
        manifest_path,
        operations=[
            {
                "action": "move",
                "from": "prompt/docs/legacy.md",
                "to": "prompt/docs/new.md",
            }
        ],
        rewrites=[{"old": "prompt/docs/legacy.md", "new": "prompt/docs/new.md"}],
    )

    result = run_script(
        [
            "python3",
            str(MIGRATE_SCRIPT),
            "--manifest",
            str(manifest_path),
            "--project-root",
            str(project_root),
            "--apply",
        ]
    )
    assert result.returncode == 0, result.stderr or result.stdout
    assert binary_target.read_bytes() == original_bytes, "non-UTF8 file should be skipped, not rewritten"
