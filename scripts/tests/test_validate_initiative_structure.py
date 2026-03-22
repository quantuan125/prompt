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


def test_strict_mode_fails_on_warnings_only(tmp_path: Path) -> None:
    initiative_root = _create_base_initiative(tmp_path)
    _add_minimal_ssot(initiative_root)

    code, output = _run_validate(initiative_root, strict=True)
    assert code == 1
    assert "warnings: 1" in output.lower()
    assert "no phase directories found" in output.lower()


def test_non_strict_mode_allows_warnings_only(tmp_path: Path) -> None:
    initiative_root = _create_base_initiative(tmp_path)
    _add_minimal_ssot(initiative_root)

    code, output = _run_validate(initiative_root, strict=False)
    assert code == 0
    assert "warnings: 1" in output.lower()
    assert "no phase directories found" in output.lower()


def test_allows_phase_level_type_directories(tmp_path: Path) -> None:
    initiative_root = _create_base_initiative(tmp_path)
    _add_minimal_ssot(initiative_root)
    (initiative_root / "workspace/PH000/raw").mkdir(parents=True, exist_ok=True)
    (initiative_root / "workspace/PH000/analysis").mkdir(parents=True, exist_ok=True)
    (initiative_root / "workspace/PH001/snotes").mkdir(parents=True, exist_ok=True)
    (initiative_root / "workspace/PH001/raw").mkdir(parents=True, exist_ok=True)
    (initiative_root / "workspace/PH001/raw/raw_T104-PH001-SES001.txt").write_text(
        "phase raw",
        encoding="utf-8",
    )
    (initiative_root / "workspace/PH001/snotes/snotes_T104-PH001-SES001.md").write_text(
        "phase notes",
        encoding="utf-8",
    )
    (initiative_root / "workspace/PH001/ST001").mkdir(parents=True, exist_ok=True)

    code, output = _run_validate(initiative_root, strict=False)
    assert code == 0, output
    assert "non-canonical stream directory" not in output.lower()


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


def test_allows_snotes_and_activity_report_directories(tmp_path: Path) -> None:
    initiative_root = _create_base_initiative(tmp_path)
    _add_minimal_ssot(initiative_root)
    (initiative_root / "workspace/PH001/ST001/snotes").mkdir(parents=True, exist_ok=True)
    (initiative_root / "workspace/PH001/ST001/AC001/snotes").mkdir(parents=True, exist_ok=True)
    (initiative_root / "workspace/PH001/ST001/AC001/verification").mkdir(parents=True, exist_ok=True)
    (initiative_root / "workspace/PH001/ST001/AC001/dev-report").mkdir(parents=True, exist_ok=True)
    (initiative_root / "workspace/PH001/ST001/AC001/raw").mkdir(parents=True, exist_ok=True)
    (initiative_root / "workspace/PH001/ST001/AC001/snotes/snotes_T104-PH001-ST001-AC001-SES001.md").write_text(
        "session notes",
        encoding="utf-8",
    )
    (initiative_root / "workspace/PH001/ST001/AC001/verification/verification_T104-PH001-ST001-AC001_gate-001.md").write_text(
        "gate",
        encoding="utf-8",
    )
    (initiative_root / "workspace/PH001/ST001/AC001/dev-report/dev-report_T104-PH001-ST001-AC001_2026-02-20.md").write_text(
        "report",
        encoding="utf-8",
    )

    code, output = _run_validate(initiative_root)
    assert code == 0, output


def test_allows_activity_analysis_and_proposal_directories(tmp_path: Path) -> None:
    initiative_root = _create_base_initiative(tmp_path)
    _add_minimal_ssot(initiative_root)
    (initiative_root / "workspace/PH001/ST001/AC001/analysis").mkdir(parents=True, exist_ok=True)
    (initiative_root / "workspace/PH001/ST001/AC001/proposal").mkdir(parents=True, exist_ok=True)
    (initiative_root / "workspace/PH001/ST001/AC001/analysis/analysis_T104-PH001-ST001-AC001_scope.md").write_text(
        "analysis",
        encoding="utf-8",
    )
    (initiative_root / "workspace/PH001/ST001/AC001/proposal/proposal_T104-PH001-ST001-AC001_scope.md").write_text(
        "proposal",
        encoding="utf-8",
    )

    code, output = _run_validate(initiative_root)
    assert code == 0, output


def test_allows_activity_implementation_directory_and_prefix(tmp_path: Path) -> None:
    initiative_root = _create_base_initiative(tmp_path)
    _add_minimal_ssot(initiative_root)
    (initiative_root / "workspace/PH001/ST001/AC001/implementation").mkdir(parents=True, exist_ok=True)
    (
        initiative_root
        / "workspace/PH001/ST001/AC001/implementation/implementation_T104-PH001-ST001-AC001_scope.md"
    ).write_text(
        "implementation",
        encoding="utf-8",
    )

    code, output = _run_validate(initiative_root)
    assert code == 0, output


def test_flags_implementation_prefix_when_misplaced_under_wrong_activity_type_directory(tmp_path: Path) -> None:
    initiative_root = _create_base_initiative(tmp_path)
    _add_minimal_ssot(initiative_root)
    (initiative_root / "workspace/PH001/ST001/AC001/analysis").mkdir(parents=True, exist_ok=True)
    (
        initiative_root
        / "workspace/PH001/ST001/AC001/analysis/implementation_T104-PH001-ST001-AC001_scope.md"
    ).write_text(
        "misplaced implementation",
        encoding="utf-8",
    )

    code, output = _run_validate(initiative_root)
    assert code == 1
    assert "expected `implementation/` for `implementation_`" in output


def test_allows_dotted_sub_activity_directories(tmp_path: Path) -> None:
    initiative_root = _create_base_initiative(tmp_path)
    _add_minimal_ssot(initiative_root)
    (initiative_root / "workspace/PH001/ST001/AC001.1/analysis").mkdir(parents=True, exist_ok=True)
    (
        initiative_root
        / "workspace/PH001/ST001/AC001.1/analysis/analysis_T104-PH001-ST001-AC001.1_scope.md"
    ).write_text(
        "analysis",
        encoding="utf-8",
    )

    code, output = _run_validate(initiative_root)
    assert code == 0, output


def test_allows_dotted_sub_activity_uid_under_parent_activity_directory(tmp_path: Path) -> None:
    initiative_root = _create_base_initiative(tmp_path)
    _add_minimal_ssot(initiative_root)
    (initiative_root / "workspace/PH001/ST001/AC001/analysis").mkdir(parents=True, exist_ok=True)
    (
        initiative_root
        / "workspace/PH001/ST001/AC001/analysis/analysis_T104-PH001-ST001-AC001.1_scope.md"
    ).write_text(
        "analysis",
        encoding="utf-8",
    )

    code, output = _run_validate(initiative_root)
    assert code == 0, output


def test_flags_ac_scoped_file_outside_activity_directory(tmp_path: Path) -> None:
    initiative_root = _create_base_initiative(tmp_path)
    _add_minimal_ssot(initiative_root)
    (initiative_root / "workspace/PH001/ST001").mkdir(parents=True, exist_ok=True)
    (initiative_root / "workspace/PH001/ST001/notes_T104-PH001-ST001-AC001-SES001.md").write_text(
        "misplaced",
        encoding="utf-8",
    )

    code, output = _run_validate(initiative_root)
    assert code == 1
    assert "uid-scope rule" in output.lower()


def test_flags_ac_scoped_file_when_activity_token_mismatch(tmp_path: Path) -> None:
    initiative_root = _create_base_initiative(tmp_path)
    _add_minimal_ssot(initiative_root)
    (initiative_root / "workspace/PH001/ST001/AC002").mkdir(parents=True, exist_ok=True)
    (initiative_root / "workspace/PH001/ST001/AC002/notes_T104-PH001-ST001-AC001-SES001.md").write_text(
        "mismatch",
        encoding="utf-8",
    )

    code, output = _run_validate(initiative_root)
    assert code == 1
    assert "does not match uid token" in output.lower()


def test_flags_legacy_gate_token_in_verification_filename(tmp_path: Path) -> None:
    initiative_root = _create_base_initiative(tmp_path)
    _add_minimal_ssot(initiative_root)
    verification_dir = initiative_root / "workspace/PH001/ST001/AC001/verification"
    verification_dir.mkdir(parents=True, exist_ok=True)
    (
        verification_dir / "verification_T104-PH001-ST001-AC001-GATE-001_review.md"
    ).write_text("legacy gate token", encoding="utf-8")

    code, output = _run_validate(initiative_root)
    assert code == 1
    assert "legacy" in output.lower()
    assert "gate" in output.lower()


def test_allows_canonical_gate_token_with_suffix_in_verification_filename(tmp_path: Path) -> None:
    initiative_root = _create_base_initiative(tmp_path)
    _add_minimal_ssot(initiative_root)
    verification_dir = initiative_root / "workspace/PH001/ST001/AC001/verification"
    verification_dir.mkdir(parents=True, exist_ok=True)
    (
        verification_dir / "verification_T104-PH001-ST001-AC001_gate-001_review.md"
    ).write_text("canonical gate token", encoding="utf-8")

    code, output = _run_validate(initiative_root)
    assert code == 0, output


def test_does_not_require_gate_token_for_non_gate_verification_artifact(tmp_path: Path) -> None:
    initiative_root = _create_base_initiative(tmp_path)
    _add_minimal_ssot(initiative_root)
    verification_dir = initiative_root / "workspace/PH001/ST001/AC001/verification"
    verification_dir.mkdir(parents=True, exist_ok=True)
    (
        verification_dir / "verification_T104-PH001-ST001-AC001-TK001.1_readiness-review.md"
    ).write_text("non-gate verification artifact", encoding="utf-8")

    code, output = _run_validate(initiative_root)
    assert code == 0, output


def test_allows_ac_scoped_communication_file_under_stream_directory(tmp_path: Path) -> None:
    initiative_root = _create_base_initiative(tmp_path)
    _add_minimal_ssot(initiative_root)
    communication_dir = initiative_root / "workspace/PH001/ST001/communication"
    communication_dir.mkdir(parents=True, exist_ok=True)
    (
        communication_dir / "comm_T104-PH001-ST001-AC001_to_LLM_Reviewer_status.md"
    ).write_text("stream communication", encoding="utf-8")

    code, output = _run_validate(initiative_root)
    assert code == 0, output
