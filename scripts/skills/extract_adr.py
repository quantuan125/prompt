#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import adr_extraction
from adr_skills_registry import ADR_SKILLS


DEFAULT_CONCEPT_PATH = Path(
    "prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Print a single ADR list-item block from the Concept document (strict, bounded)."
    )
    selector = parser.add_mutually_exclusive_group(required=True)
    selector.add_argument(
        "--expected-anchor",
        help="Expected anchor string, e.g. {#t102-adr-005-id-spec}",
    )
    selector.add_argument(
        "--adr-id",
        help="ADR ID convenience selector (registry-resolved), e.g. ADR-005",
    )
    parser.add_argument(
        "--concept-path",
        default=str(DEFAULT_CONCEPT_PATH),
        help=f"Path to concept markdown (default: {DEFAULT_CONCEPT_PATH})",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        concept_path = adr_extraction.resolve_concept_path(
            concept_path=Path(args.concept_path),
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
        expected_anchor = args.expected_anchor
        if expected_anchor is None:
            matches = [skill for skill in ADR_SKILLS if skill.adr_id == args.adr_id]
            if not matches:
                known = ", ".join(sorted({skill.adr_id for skill in ADR_SKILLS}))
                raise ValueError(
                    f"Unknown --adr-id {args.adr_id!r}. Known values: {known}"
                )
            expected_anchor = matches[0].expected_anchor

        sys.stdout.write(
            adr_extraction.extract_adr_block(
                concept_text=concept_text, expected_anchor=expected_anchor
            )
        )
    except Exception as exc:
        print(
            f"ERROR: Failed to extract ADR block: {exc}\n"
            "This script is intentionally strict (no fallback). If the Concept format changed, "
            "update the marker/regex.\n",
            file=sys.stderr,
        )
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
