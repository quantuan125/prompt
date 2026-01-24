#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path


DEFAULT_CONCEPT_PATH = Path(
    "prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md"
)

EXPECTED_ANCHOR = "{#t102-adr-007-issues-risks-index}"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Print only the T102-ADR-007 (Issues & Risks Index) block from the Concept "
            "document, so agents can follow the latest Issues/Risks rules without loading the "
            "entire file."
        )
    )
    parser.add_argument(
        "--concept-path",
        default=str(DEFAULT_CONCEPT_PATH),
        help=f"Path to concept markdown (default: {DEFAULT_CONCEPT_PATH})",
    )
    return parser.parse_args()


def find_repo_root(start: Path) -> Path:
    start = start.resolve()
    for candidate in [start, *start.parents]:
        if (candidate / "prompt/scripts/skills/adr_extraction.py").exists():
            return candidate
    raise RuntimeError(
        "Could not locate repo root (expected prompt/scripts/skills/adr_extraction.py)."
    )


def main() -> int:
    args = parse_args()
    concept_path = Path(args.concept_path)

    try:
        repo_root = find_repo_root(Path(__file__))
        sys.path.insert(0, str(repo_root / "prompt/scripts/skills"))
        import adr_extraction  # noqa: PLC0415
    except Exception as exc:
        print(f"ERROR: Failed to load shared adr_extraction module: {exc}", file=sys.stderr)
        return 1

    try:
        concept_path = adr_extraction.resolve_concept_path(
            concept_path=concept_path,
            default_path=DEFAULT_CONCEPT_PATH,
        )
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    try:
        concept_text = adr_extraction.read_text(concept_path)
    except Exception as exc:
        print(f"ERROR: Failed to read {concept_path}: {exc}", file=sys.stderr)
        return 1

    try:
        sys.stdout.write(
            adr_extraction.extract_adr_block(
                concept_text=concept_text,
                expected_anchor=EXPECTED_ANCHOR,
            )
        )
    except Exception as exc:
        print(f"ERROR: Failed to extract ADR-007 block: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
