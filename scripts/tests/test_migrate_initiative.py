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


def test_dry_run_reports_delete_operation_without_mutation(tmp_path: Path) -> None:
    project_root, prompt_root = _setup_repo(tmp_path)
    empty_dir = prompt_root / "artifacts/tasks/T104/workspace/PH001/ST007/devnote"
    empty_dir.mkdir(parents=True, exist_ok=True)

    manifest_path = project_root / "manifest.json"
    write_manifest(
        manifest_path,
        operations=[
            {
                "action": "delete",
                "path": "prompt/artifacts/tasks/T104/workspace/PH001/ST007/devnote",
            }
        ],
    )

    report_path = project_root / "reports/dry-run-delete.md"
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
    assert empty_dir.exists(), "dry-run should not remove directories"
    report = report_path.read_text(encoding="utf-8")
    assert "DRY RUN delete empty dir: prompt/artifacts/tasks/T104/workspace/PH001/ST007/devnote" in report


def test_dry_run_reports_file_delete_without_mutation(tmp_path: Path) -> None:
    project_root, prompt_root = _setup_repo(tmp_path)
    cache_file = (
        prompt_root
        / "artifacts/tasks/T104/consultant/workspace/scripts/__pycache__/migrate_adr_to_std.cpython-312.pyc"
    )
    cache_file.parent.mkdir(parents=True, exist_ok=True)
    cache_file.write_bytes(b"compiled")

    manifest_path = project_root / "manifest-file-delete.json"
    write_manifest(
        manifest_path,
        operations=[
            {
                "action": "delete",
                "path": (
                    "prompt/artifacts/tasks/T104/consultant/workspace/scripts/__pycache__/"
                    "migrate_adr_to_std.cpython-312.pyc"
                ),
            }
        ],
    )

    report_path = project_root / "reports/dry-run-file-delete.md"
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
    assert cache_file.exists(), "dry-run should not remove files"
    report = report_path.read_text(encoding="utf-8")
    assert (
        "DRY RUN delete file: "
        "prompt/artifacts/tasks/T104/consultant/workspace/scripts/__pycache__/"
        "migrate_adr_to_std.cpython-312.pyc"
    ) in report


def test_apply_deletes_file_and_cleans_up_empty_parent_directories(tmp_path: Path) -> None:
    project_root, prompt_root = _setup_repo(tmp_path)
    cache_dir = prompt_root / "artifacts/tasks/T104/consultant/workspace/scripts/__pycache__"
    cache_dir.mkdir(parents=True, exist_ok=True)
    cache_file = cache_dir / "migrate_adr_to_std.cpython-312.pyc"
    cache_file.write_bytes(b"compiled")

    manifest_path = project_root / "manifest-file-delete-apply.json"
    write_manifest(
        manifest_path,
        operations=[
            {
                "action": "delete",
                "path": (
                    "prompt/artifacts/tasks/T104/consultant/workspace/scripts/__pycache__/"
                    "migrate_adr_to_std.cpython-312.pyc"
                ),
            }
        ],
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
    assert not cache_file.exists(), "apply mode should remove delete-target files"
    assert not cache_dir.exists(), "empty __pycache__ directory should be pruned after file delete"
    assert not cache_dir.parent.exists(), "empty script directory should be pruned after file delete"


def test_apply_deletes_empty_directory_and_rejects_non_empty_delete_targets(tmp_path: Path) -> None:
    project_root, prompt_root = _setup_repo(tmp_path)
    empty_dir = prompt_root / "artifacts/tasks/T104/workspace/PH001/ST007/devnote"
    empty_dir.mkdir(parents=True, exist_ok=True)
    non_empty_dir = prompt_root / "artifacts/tasks/T104/workspace/PH001/ST007/devnote_non_empty"
    non_empty_dir.mkdir(parents=True, exist_ok=True)
    (non_empty_dir / "keep.txt").write_text("keep", encoding="utf-8")

    apply_manifest_path = project_root / "manifest-apply.json"
    write_manifest(
        apply_manifest_path,
        operations=[
            {
                "action": "delete",
                "path": "prompt/artifacts/tasks/T104/workspace/PH001/ST007/devnote",
            }
        ],
    )
    apply_result = run_script(
        [
            "python3",
            str(MIGRATE_SCRIPT),
            "--manifest",
            str(apply_manifest_path),
            "--project-root",
            str(project_root),
            "--apply",
        ]
    )
    assert apply_result.returncode == 0, apply_result.stderr or apply_result.stdout
    assert not empty_dir.exists(), "apply mode should remove empty delete targets"

    fail_manifest_path = project_root / "manifest-fail.json"
    write_manifest(
        fail_manifest_path,
        operations=[
            {
                "action": "delete",
                "path": "prompt/artifacts/tasks/T104/workspace/PH001/ST007/devnote_non_empty",
            }
        ],
    )
    fail_result = run_script(
        [
            "python3",
            str(MIGRATE_SCRIPT),
            "--manifest",
            str(fail_manifest_path),
            "--project-root",
            str(project_root),
            "--dry-run",
        ]
    )
    assert fail_result.returncode != 0, "non-empty delete targets must fail validation"
    assert "Delete directory is not empty" in (fail_result.stdout + fail_result.stderr)


def test_fails_when_manifest_rewrite_coverage_is_incomplete(tmp_path: Path) -> None:
    project_root, prompt_root = _setup_repo(tmp_path)
    source_file = prompt_root / "docs/legacy.md"
    source_file.parent.mkdir(parents=True, exist_ok=True)
    source_file.write_text("legacy", encoding="utf-8")

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
        rewrites=[{"old": "prompt/docs/other.md", "new": "prompt/docs/other-new.md"}],
    )

    result = run_script(
        [
            "python3",
            str(MIGRATE_SCRIPT),
            "--manifest",
            str(manifest_path),
            "--project-root",
            str(project_root),
            "--dry-run",
        ]
    )

    assert result.returncode != 0
    assert "Missing 1:1 reference rewrite for move operation" in (result.stdout + result.stderr)


def test_dry_run_supports_notes_to_snotes_rename_and_move(tmp_path: Path) -> None:
    project_root, prompt_root = _setup_repo(tmp_path)
    source_file = (
        prompt_root
        / "artifacts/tasks/T104/workspace/PH001/ST007/AC001/notes_T104-PH001-ST007-AC001-SES001.md"
    )
    source_file.parent.mkdir(parents=True, exist_ok=True)
    source_file.write_text("session notes", encoding="utf-8")

    manifest_path = project_root / "manifest.json"
    write_manifest(
        manifest_path,
        operations=[
            {
                "action": "mkdir",
                "path": "prompt/artifacts/tasks/T104/workspace/PH001/ST007/AC001/snotes",
            },
            {
                "action": "move",
                "from": "prompt/artifacts/tasks/T104/workspace/PH001/ST007/AC001/notes_T104-PH001-ST007-AC001-SES001.md",
                "to": "prompt/artifacts/tasks/T104/workspace/PH001/ST007/AC001/snotes/snotes_T104-PH001-ST007-AC001-SES001.md",
            },
        ],
        rewrites=[
            {
                "old": "prompt/artifacts/tasks/T104/workspace/PH001/ST007/AC001/notes_T104-PH001-ST007-AC001-SES001.md",
                "new": "prompt/artifacts/tasks/T104/workspace/PH001/ST007/AC001/snotes/snotes_T104-PH001-ST007-AC001-SES001.md",
            }
        ],
    )

    report_path = project_root / "reports/dry-run-snotes.md"
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
    assert "DRY RUN move" in report
    assert "snotes_T104-PH001-ST007-AC001-SES001.md" in report
