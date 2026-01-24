from __future__ import annotations

import re
from pathlib import Path

NEXT_ADR_HEADER_RE = re.compile(r"^\* \*\*T\d{3}[A-Z0-9-]*-ADR-\d{3}\b")
CONCEPT_VERSION_RE = re.compile(
    r"^concept_T102-CONSULTANT_v(?P<major>\d+)\.(?P<minor>\d+)\.(?P<patch>\d+)\.md$"
)


def extract_adr_block(*, concept_text: str, expected_anchor: str) -> str:
    lines = concept_text.splitlines()

    start_index: int | None = None
    for index, line in enumerate(lines):
        if expected_anchor in line:
            start_index = index
            break

    if start_index is None:
        raise ValueError(f"ADR start marker not found: {expected_anchor}")

    end_index = len(lines)
    saw_body_line = False
    for index in range(start_index + 1, len(lines)):
        line = lines[index]

        if NEXT_ADR_HEADER_RE.match(line):
            end_index = index
            break

        if not line.strip():
            continue

        if line.startswith("\t") or line.startswith("  "):
            saw_body_line = True
            continue

        end_index = index
        break

    block_lines = lines[start_index:end_index]
    block = "\n".join(block_lines).strip("\n")
    if not block:
        raise ValueError("ADR extraction produced an empty block.")
    if not saw_body_line:
        raise ValueError(
            "ADR extraction did not include any indented body lines; "
            "expected the ADR block to be a list item with a body indented by 2+ spaces or a tab."
        )
    return block + "\n"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def resolve_concept_path(*, concept_path: Path, default_path: Path) -> Path:
    if concept_path.exists():
        return concept_path

    if concept_path != default_path:
        raise FileNotFoundError(f"Concept file not found: {concept_path}")

    parent = default_path.parent
    if not parent.is_dir():
        raise FileNotFoundError(
            f"Default concept directory not found: {parent} (from {default_path})"
        )

    candidates: list[tuple[tuple[int, int, int], Path]] = []
    for path in parent.glob("concept_T102-CONSULTANT_v*.md"):
        match = CONCEPT_VERSION_RE.match(path.name)
        if not match:
            continue
        version = (
            int(match.group("major")),
            int(match.group("minor")),
            int(match.group("patch")),
        )
        candidates.append((version, path))

    if not candidates:
        raise FileNotFoundError(
            f"Default concept file missing ({default_path}) and no versioned concept files found in {parent}"
        )

    max_version = max(version for version, _ in candidates)
    best = [path for version, path in candidates if version == max_version]
    if len(best) != 1:
        names = ", ".join(sorted(p.name for p in best))
        raise RuntimeError(
            f"Default concept file missing ({default_path}) and latest version is ambiguous: {names}"
        )
    return best[0]
