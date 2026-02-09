#!/usr/bin/env python3
import os
import sys
from pathlib import Path


def find_prompt_root(current_file: Path) -> Path:
    for parent in current_file.parents:
        if parent.name == "prompt":
            return parent
    raise RuntimeError("Unable to locate prompt/ root for compatibility wrapper.")


def main() -> int:
    current_file = Path(__file__).resolve()
    prompt_root = find_prompt_root(current_file)
    canonical_script = prompt_root / "scripts/migrations/migrate_adr_to_std.py"

    if not canonical_script.exists():
        raise FileNotFoundError(f"Canonical script not found: {canonical_script}")

    print(
        "[compat-wrapper] Delegating to canonical tool at "
        f"{canonical_script}",
        file=sys.stderr,
    )
    os.execv(sys.executable, [sys.executable, str(canonical_script), *sys.argv[1:]])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
