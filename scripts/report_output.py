"""Shared utility for --report-path resolution with smart defaults and workspace guards."""

from __future__ import annotations

from pathlib import Path
import sys
from typing import Callable


REPO_ROOT = Path(__file__).resolve().parents[2]
SCRIPTS_OUTPUT_ROOT = REPO_ROOT / "prompt/scripts/output"
WORKSPACE_FORBIDDEN = REPO_ROOT / "prompt/artifacts/tasks"


def resolve_report_path(
    explicit_path: str | None,
    default_fn: Callable[..., Path],
    *default_args,
) -> Path:
    """Resolve --report-path with smart default and workspace guard.

    Args:
        explicit_path: Value from args.report_path (None if not provided).
        default_fn: Callable returning the default Path.
        *default_args: Arguments forwarded to default_fn.

    Returns:
        Resolved, validated Path with parent directories created.

    Raises:
        SystemExit: If resolved path is inside prompt/artifacts/tasks/.
    """
    if explicit_path:
        report_path = Path(explicit_path).expanduser().resolve(strict=False)
    else:
        report_path = default_fn(*default_args).expanduser().resolve(strict=False)

    forbidden = WORKSPACE_FORBIDDEN.resolve()
    try:
        report_path.relative_to(forbidden)
        print(
            "ERROR: --report-path resolves inside prompt/artifacts/tasks/.\n"
            f"  Resolved: {report_path}\n"
            "  Script outputs must go to prompt/scripts/output/ or outside the workspace.\n"
            "  Hint: omit --report-path to use the auto-generated default.",
            file=sys.stderr,
        )
        raise SystemExit(1)
    except ValueError:
        pass

    report_path.parent.mkdir(parents=True, exist_ok=True)
    return report_path

