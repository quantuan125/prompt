#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Sync the SSOT skill under prompt/skills/… into a Codex-discoverable mirror directory "
            "under .codex/skills/…"
        )
    )
    parser.add_argument(
        "--dest-dir",
        default=".codex/skills/t102-adr-005-id-spec",
        help="Destination mirror directory (default: .codex/skills/t102-adr-005-id-spec)",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Do not write; exit non-zero if mirror differs from SSOT.",
    )
    return parser.parse_args()


def find_repo_root(start: Path) -> Path:
    start = start.resolve()
    for candidate in [start, *start.parents]:
        if (candidate / "prompt/scripts/skills/sync_to_codex_mirror.py").is_file():
            return candidate
    raise RuntimeError(
        "Could not locate repo root (expected `prompt/scripts/skills/sync_to_codex_mirror.py`)."
    )


def main() -> int:
    args = parse_args()
    repo_root = find_repo_root(Path(__file__))

    sys.path.insert(0, str(repo_root / "prompt/scripts/skills"))
    import sync_to_codex_mirror as shared_sync

    ssot_dir = Path(__file__).resolve().parents[1]
    print_script = ssot_dir / "scripts/print_t102_adr_005.py"
    dest_dir = (repo_root / Path(args.dest_dir)).resolve()
    return shared_sync.sync_to_codex_mirror(
        ssot_dir=ssot_dir,
        dest_dir=dest_dir,
        print_script=print_script,
        check=args.check,
    )


if __name__ == "__main__":
    raise SystemExit(main())
