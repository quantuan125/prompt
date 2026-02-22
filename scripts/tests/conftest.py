from __future__ import annotations

import json
import subprocess
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
MIGRATE_SCRIPT = REPO_ROOT / "prompt/scripts/migrate_initiative.py"
VALIDATE_SCRIPT = REPO_ROOT / "prompt/scripts/validate_initiative_structure.py"
SCAFFOLD_SCRIPT = REPO_ROOT / "prompt/scripts/scaffold_initiative.py"
ARCHIVE_SCRIPT = REPO_ROOT / "prompt/scripts/archive_manager.py"


def write_manifest(path: Path, operations: list[dict], rewrites: list[dict] | None = None) -> None:
    payload: dict[str, object] = {"operations": operations}
    if rewrites is not None:
        payload["reference_rewrites"] = rewrites
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def run_script(args: list[str], cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        args,
        cwd=str(cwd or REPO_ROOT),
        text=True,
        capture_output=True,
        check=False,
    )
