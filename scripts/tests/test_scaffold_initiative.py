from __future__ import annotations

from pathlib import Path

from conftest import SCAFFOLD_SCRIPT, run_script


def test_dry_run_does_not_create_directories(tmp_path: Path) -> None:
    tasks_root = tmp_path / "tasks"
    tasks_root.mkdir(parents=True, exist_ok=True)

    result = run_script(
        [
            "python3",
            str(SCAFFOLD_SCRIPT),
            "--initiative-id",
            "T999",
            "--initiative-code",
            "TEST",
            "--tasks-root",
            str(tasks_root),
            "--phase-count",
            "1",
            "--streams",
            "ST000,ST007",
            "--dry-run",
        ]
    )
    assert result.returncode == 0, result.stderr or result.stdout
    assert not (tasks_root / "T999").exists()


def test_apply_creates_expected_structure(tmp_path: Path) -> None:
    tasks_root = tmp_path / "tasks"
    tasks_root.mkdir(parents=True, exist_ok=True)

    result = run_script(
        [
            "python3",
            str(SCAFFOLD_SCRIPT),
            "--initiative-id",
            "T999",
            "--initiative-code",
            "TEST",
            "--tasks-root",
            str(tasks_root),
            "--phase-count",
            "2",
            "--streams",
            "ST000,ST007",
            "--apply",
        ]
    )
    assert result.returncode == 0, result.stderr or result.stdout

    expected_dirs = [
        tasks_root / "T999/archive",
        tasks_root / "T999/research",
        tasks_root / "T999/ssot",
        tasks_root / "T999/standard",
        tasks_root / "T999/workspace/PH001/ST000",
        tasks_root / "T999/workspace/PH001/ST007",
        tasks_root / "T999/workspace/PH002/ST000",
        tasks_root / "T999/workspace/PH002/ST007",
    ]
    for path in expected_dirs:
        assert path.is_dir(), f"expected scaffold directory: {path}"
