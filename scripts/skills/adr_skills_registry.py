#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class AdrSkillSpec:
    """
    Registry entry for one ADR skill that is verified by prompt/scripts/skills/verify_adr_skills.py.

    Notes:
    - All paths are relative to the repo root returned by verify_adr_skills.find_repo_root().
    - This registry is intended to track "Active Skills" (not planned skills).
    """

    skill_name: str
    adr_id: str
    expected_anchor: str
    ssot_dir: Path
    claude_link: Path
    codex_mirror_dir: Path
    extraction_script: Path
    codex_sync_script: Path


ADR_SKILLS: tuple[AdrSkillSpec, ...] = (
    AdrSkillSpec(
        skill_name="t102-adr-005-id-spec",
        adr_id="ADR-005",
        expected_anchor="{#t102-adr-005-id-spec}",
        ssot_dir=Path("prompt/skills/t102-adr-005-id-spec"),
        claude_link=Path(".claude/skills/t102-adr-005-id-spec"),
        codex_mirror_dir=Path(".codex/skills/t102-adr-005-id-spec"),
        extraction_script=Path(
            "prompt/skills/t102-adr-005-id-spec/scripts/print_t102_adr_005.py"
        ),
        codex_sync_script=Path(
            "prompt/skills/t102-adr-005-id-spec/scripts/sync_to_codex_mirror.py"
        ),
    ),
    AdrSkillSpec(
        skill_name="t102-adr-004-drs-index",
        adr_id="ADR-004",
        expected_anchor="{#t102-adr-004-drs-index}",
        ssot_dir=Path("prompt/skills/t102-adr-004-drs-index"),
        claude_link=Path(".claude/skills/t102-adr-004-drs-index"),
        codex_mirror_dir=Path(".codex/skills/t102-adr-004-drs-index"),
        extraction_script=Path(
            "prompt/skills/t102-adr-004-drs-index/scripts/print_t102_adr_004.py"
        ),
        codex_sync_script=Path(
            "prompt/skills/t102-adr-004-drs-index/scripts/sync_to_codex_mirror.py"
        ),
    ),
    AdrSkillSpec(
        skill_name="t102-adr-007-issues-risks-index",
        adr_id="ADR-007",
        expected_anchor="{#t102-adr-007-issues-risks-index}",
        ssot_dir=Path("prompt/skills/t102-adr-007-issues-risks-index"),
        claude_link=Path(".claude/skills/t102-adr-007-issues-risks-index"),
        codex_mirror_dir=Path(".codex/skills/t102-adr-007-issues-risks-index"),
        extraction_script=Path(
            "prompt/skills/t102-adr-007-issues-risks-index/scripts/print_t102_adr_007.py"
        ),
        codex_sync_script=Path(
            "prompt/skills/t102-adr-007-issues-risks-index/scripts/sync_to_codex_mirror.py"
        ),
    ),
)
