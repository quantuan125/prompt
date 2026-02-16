from __future__ import annotations

from pathlib import Path

from conftest import VALIDATE_SCRIPT, run_script


def _create_base_initiative(tmp_path: Path) -> Path:
    initiative_root = tmp_path / "T104"
    for name in ("archive", "research", "ssot", "standard", "workspace"):
        (initiative_root / name).mkdir(parents=True, exist_ok=True)
    return initiative_root


def _add_minimal_ssot(initiative_root: Path) -> None:
    (initiative_root / "ssot/sps_T104-CWS.md").write_text("sps", encoding="utf-8")
    (initiative_root / "ssot/concept_T104-CWS.md").write_text("concept", encoding="utf-8")


def _run_validate(initiative_root: Path, strict: bool = True) -> tuple[int, str]:
    args = [
        "python3",
        str(VALIDATE_SCRIPT),
        "--initiative-root",
        str(initiative_root),
    ]
    if strict:
        args.append("--strict")
    result = run_script(args)
    return result.returncode, f"{result.stdout}\n{result.stderr}"


def test_flags_type_first_workspace_directories_as_errors(tmp_path: Path) -> None:
    initiative_root = _create_base_initiative(tmp_path)
    _add_minimal_ssot(initiative_root)
    (initiative_root / "workspace/plan").mkdir(parents=True, exist_ok=True)

    code, output = _run_validate(initiative_root)
    assert code == 1
    assert "type-first" in output.lower()


def test_requires_sps_and_concept_files_in_ssot(tmp_path: Path) -> None:
    initiative_root = _create_base_initiative(tmp_path)
    (initiative_root / "workspace/PH001/ST001").mkdir(parents=True, exist_ok=True)

    code, output = _run_validate(initiative_root)
    assert code == 1
    assert "ssot" in output.lower()
    assert "sps_" in output.lower()
    assert "concept_" in output.lower()


def test_flags_root_level_raw_directory(tmp_path: Path) -> None:
    initiative_root = _create_base_initiative(tmp_path)
    _add_minimal_ssot(initiative_root)
    (initiative_root / "workspace/PH001/ST001").mkdir(parents=True, exist_ok=True)
    (initiative_root / "raw").mkdir(parents=True, exist_ok=True)

    code, output = _run_validate(initiative_root)
    assert code == 1
    assert "raw/" in output.lower() or "root raw" in output.lower()


def test_validates_nested_activity_directory_naming(tmp_path: Path) -> None:
    initiative_root = _create_base_initiative(tmp_path)
    _add_minimal_ssot(initiative_root)
    (initiative_root / "workspace/PH001/ST001/AX001").mkdir(parents=True, exist_ok=True)

    code, output = _run_validate(initiative_root)
    assert code == 1
    assert "activity" in output.lower()
    assert "ac###" in output.lower() or "ac" in output.lower()


def test_flags_txt_files_with_unrecognized_prefix(tmp_path: Path) -> None:
    initiative_root = _create_base_initiative(tmp_path)
    _add_minimal_ssot(initiative_root)
    (initiative_root / "workspace/PH001/ST001").mkdir(parents=True, exist_ok=True)
    (initiative_root / "workspace/PH001/ST001/random_notes.txt").write_text("x", encoding="utf-8")

    code, output = _run_validate(initiative_root)
    assert code == 1
    assert ".txt" in output.lower()
    assert "prefix" in output.lower()


def test_allows_workspace_unresolved_staging_directory(tmp_path: Path) -> None:
    initiative_root = _create_base_initiative(tmp_path)
    _add_minimal_ssot(initiative_root)
    (initiative_root / "workspace/PH001/ST001").mkdir(parents=True, exist_ok=True)
    (initiative_root / "workspace/_unresolved").mkdir(parents=True, exist_ok=True)
    (initiative_root / "workspace/_unresolved/analysis_T104-RES-001_agentic-workspace-assessment.md").write_text(
        "staged",
        encoding="utf-8",
    )

    code, output = _run_validate(initiative_root)
    assert code == 0
    assert "non-canonical phase directory" not in output.lower()
