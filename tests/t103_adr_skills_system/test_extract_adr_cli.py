import subprocess
import sys
import importlib.util
from pathlib import Path

import pytest


def load_adr_skills_registry():
    module_path = Path("prompt/scripts/skills/adr_skills_registry.py").resolve()
    spec = importlib.util.spec_from_file_location("adr_skills_registry", module_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Failed to load registry module spec from {module_path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.mark.unit
@pytest.mark.fast
class TestExtractAdrCli:
    def test_default_concept_path_prefers_unversioned_ssot_when_present(
        self, tmp_path: Path
    ) -> None:
        concept_dir = tmp_path / "prompt/artifacts/tasks/T102/consultant/concept"
        concept_dir.mkdir(parents=True, exist_ok=True)

        (concept_dir / "concept_T102-CONSULTANT.md").write_text(
            "\n".join(
                [
                    "* **T102-ADR-005 (ID Specification & Rules) {#t102-adr-005-id-spec}**",
                    "",
                    "  **Context** From SSOT.",
                    "",
                ]
            )
            + "\n",
            encoding="utf-8",
        )
        (concept_dir / "concept_T102-CONSULTANT_v9.9.9.md").write_text(
            "\n".join(
                [
                    "* **T102-ADR-005 (ID Specification & Rules) {#t102-adr-005-id-spec}**",
                    "",
                    "  **Context** From versioned fallback.",
                    "",
                ]
            )
            + "\n",
            encoding="utf-8",
        )

        cli_path = Path("prompt/scripts/skills/extract_adr.py").resolve()
        proc = subprocess.run(
            [
                sys.executable,
                str(cli_path),
                "--expected-anchor",
                "{#t102-adr-005-id-spec}",
            ],
            cwd=str(tmp_path),
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )

        assert proc.returncode == 0, proc.stderr
        assert "From SSOT." in proc.stdout

    def test_extracts_by_expected_anchor(self, tmp_path: Path) -> None:
        concept_path = tmp_path / "concept.md"
        concept_path.write_text(
            "\n".join(
                [
                    "# Concept",
                    "",
                    "* **T102-ADR-005 (ID Specification & Rules) {#t102-adr-005-id-spec}**",
                    "",
                    "  **Context** Something.",
                    "",
                    "* **T102-ADR-006 (Other) {#t102-adr-006-other}**",
                    "",
                    "  **Context** Other.",
                    "",
                ]
            )
            + "\n",
            encoding="utf-8",
        )

        cli_path = Path("prompt/scripts/skills/extract_adr.py")
        proc = subprocess.run(
            [
                sys.executable,
                str(cli_path),
                "--expected-anchor",
                "{#t102-adr-005-id-spec}",
                "--concept-path",
                str(concept_path),
            ],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )

        assert proc.returncode == 0, proc.stderr
        assert "{#t102-adr-005-id-spec}" in proc.stdout

    def test_extracts_by_adr_id(self, tmp_path: Path) -> None:
        concept_path = tmp_path / "concept.md"
        concept_path.write_text(
            "\n".join(
                [
                    "# Concept",
                    "",
                    "* **T102-ADR-005 (ID Specification & Rules) {#t102-adr-005-id-spec}**",
                    "",
                    "  **Context** Something.",
                    "",
                ]
            )
            + "\n",
            encoding="utf-8",
        )

        cli_path = Path("prompt/scripts/skills/extract_adr.py")
        proc = subprocess.run(
            [
                sys.executable,
                str(cli_path),
                "--adr-id",
                "ADR-005",
                "--concept-path",
                str(concept_path),
            ],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )

        assert proc.returncode == 0, proc.stderr
        assert "{#t102-adr-005-id-spec}" in proc.stdout

    def test_default_concept_path_falls_back_to_latest_version(
        self, tmp_path: Path
    ) -> None:
        concept_dir = (
            tmp_path / "prompt/artifacts/tasks/T102/consultant/concept"
        )
        concept_dir.mkdir(parents=True, exist_ok=True)

        (concept_dir / "concept_T102-CONSULTANT_v1.0.1.md").write_text(
            "\n".join(
                [
                    "* **T102-ADR-005 (ID Specification & Rules) {#t102-adr-005-id-spec}**",
                    "",
                    "  **Context** Something.",
                    "",
                ]
            )
            + "\n",
            encoding="utf-8",
        )
        (concept_dir / "concept_T102-CONSULTANT_v1.2.0.md").write_text(
            "\n".join(
                [
                    "* **T102-ADR-005 (ID Specification & Rules) {#t102-adr-005-id-spec}**",
                    "",
                    "  **Context** Something newer.",
                    "",
                ]
            )
            + "\n",
            encoding="utf-8",
        )

        cli_path = Path("prompt/scripts/skills/extract_adr.py").resolve()
        proc = subprocess.run(
            [
                sys.executable,
                str(cli_path),
                "--expected-anchor",
                "{#t102-adr-005-id-spec}",
            ],
            cwd=str(tmp_path),
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )

        assert proc.returncode == 0, proc.stderr
        assert "Something newer." in proc.stdout

    def test_print_t102_adr_005_wrapper_falls_back_to_latest_version(
        self, tmp_path: Path
    ) -> None:
        concept_dir = tmp_path / "prompt/artifacts/tasks/T102/consultant/concept"
        concept_dir.mkdir(parents=True, exist_ok=True)

        (concept_dir / "concept_T102-CONSULTANT_v1.2.0.md").write_text(
            "\n".join(
                [
                    "* **T102-ADR-005 (ID Specification & Rules) {#t102-adr-005-id-spec}**",
                    "",
                    "  **Context** Something newer.",
                    "",
                ]
            )
            + "\n",
            encoding="utf-8",
        )

        wrapper_path = Path(
            "prompt/skills/t102-adr-005-id-spec/scripts/print_t102_adr_005.py"
        ).resolve()
        proc = subprocess.run(
            [sys.executable, str(wrapper_path)],
            cwd=str(tmp_path),
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )

        assert proc.returncode == 0, proc.stderr
        assert "Something newer." in proc.stdout

    def test_print_t102_adr_004_wrapper_falls_back_to_latest_version(
        self, tmp_path: Path
    ) -> None:
        concept_dir = tmp_path / "prompt/artifacts/tasks/T102/consultant/concept"
        concept_dir.mkdir(parents=True, exist_ok=True)

        (concept_dir / "concept_T102-CONSULTANT_v1.2.0.md").write_text(
            "\n".join(
                [
                    "* **T102-ADR-004 (Decision Records Index) {#t102-adr-004-drs-index}**",
                    "",
                    "  **Context** Something newer.",
                    "",
                ]
            )
            + "\n",
            encoding="utf-8",
        )

        wrapper_path = Path(
            "prompt/skills/t102-adr-004-drs-index/scripts/print_t102_adr_004.py"
        ).resolve()
        proc = subprocess.run(
            [sys.executable, str(wrapper_path)],
            cwd=str(tmp_path),
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )

        assert proc.returncode == 0, proc.stderr
        assert "Something newer." in proc.stdout

    def test_print_t102_adr_007_wrapper_falls_back_to_latest_version(
        self, tmp_path: Path
    ) -> None:
        concept_dir = tmp_path / "prompt/artifacts/tasks/T102/consultant/concept"
        concept_dir.mkdir(parents=True, exist_ok=True)

        (concept_dir / "concept_T102-CONSULTANT_v1.2.0.md").write_text(
            "\n".join(
                [
                    "* **T102-ADR-007 (Issues & Risks Index) {#t102-adr-007-issues-risks-index}**",
                    "",
                    "  **Context** Something newer.",
                    "",
                ]
            )
            + "\n",
            encoding="utf-8",
        )

        wrapper_path = Path(
            "prompt/skills/t102-adr-007-issues-risks-index/scripts/print_t102_adr_007.py"
        ).resolve()
        proc = subprocess.run(
            [sys.executable, str(wrapper_path)],
            cwd=str(tmp_path),
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )

        assert proc.returncode == 0, proc.stderr
        assert "Something newer." in proc.stdout

    def test_extracts_by_expected_anchor_for_all_registry_skills(
        self, tmp_path: Path
    ) -> None:
        registry = load_adr_skills_registry()

        cli_path = Path("prompt/scripts/skills/extract_adr.py")
        for skill in registry.ADR_SKILLS:
            concept_path = tmp_path / f"{skill.skill_name}.md"
            concept_path.write_text(
                "\n".join(
                    [
                        "# Concept",
                        "",
                        f"* **T102-{skill.adr_id} (Title) {skill.expected_anchor}**",
                        "",
                        "  **Context** Something.",
                        "",
                    ]
                )
                + "\n",
                encoding="utf-8",
            )

            proc = subprocess.run(
                [
                    sys.executable,
                    str(cli_path),
                    "--expected-anchor",
                    skill.expected_anchor,
                    "--concept-path",
                    str(concept_path),
                ],
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=False,
            )

            assert proc.returncode == 0, proc.stderr
            assert skill.expected_anchor in proc.stdout

    def test_fails_when_anchor_missing(self, tmp_path: Path) -> None:
        concept_path = tmp_path / "concept.md"
        concept_path.write_text(
            "\n".join(
                [
                    "# Concept",
                    "",
                    "* **T102-ADR-999 (Other) {#t102-adr-999-other}**",
                    "",
                    "  **Context** Something.",
                    "",
                ]
            )
            + "\n",
            encoding="utf-8",
        )

        cli_path = Path("prompt/scripts/skills/extract_adr.py")
        proc = subprocess.run(
            [
                sys.executable,
                str(cli_path),
                "--expected-anchor",
                "{#t102-adr-005-id-spec}",
                "--concept-path",
                str(concept_path),
            ],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )

        assert proc.returncode != 0
        assert "start marker not found" in proc.stderr.lower()

    def test_fails_when_body_has_no_indented_lines(self, tmp_path: Path) -> None:
        concept_path = tmp_path / "concept.md"
        concept_path.write_text(
            "\n".join(
                [
                    "# Concept",
                    "",
                    "* **T102-ADR-005 (ID Specification & Rules) {#t102-adr-005-id-spec}**",
                    "",
                    "**Context** Not indented.",
                    "",
                ]
            )
            + "\n",
            encoding="utf-8",
        )

        cli_path = Path("prompt/scripts/skills/extract_adr.py")
        proc = subprocess.run(
            [
                sys.executable,
                str(cli_path),
                "--expected-anchor",
                "{#t102-adr-005-id-spec}",
                "--concept-path",
                str(concept_path),
            ],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )

        assert proc.returncode != 0
        assert "indented body lines" in proc.stderr.lower()

    def test_does_not_include_non_indented_trailing_content(self, tmp_path: Path) -> None:
        concept_path = tmp_path / "concept.md"
        concept_path.write_text(
            "\n".join(
                [
                    "# Concept",
                    "",
                    "* **T102-ADR-005 (ID Specification & Rules) {#t102-adr-005-id-spec}**",
                    "",
                    "  **Context** Something.",
                    "",
                    "# Trailing Heading",
                    "",
                    "More stuff.",
                    "",
                ]
            )
            + "\n",
            encoding="utf-8",
        )

        cli_path = Path("prompt/scripts/skills/extract_adr.py")
        proc = subprocess.run(
            [
                sys.executable,
                str(cli_path),
                "--expected-anchor",
                "{#t102-adr-005-id-spec}",
                "--concept-path",
                str(concept_path),
            ],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )

        assert proc.returncode == 0, proc.stderr
        assert "# Trailing Heading" not in proc.stdout
