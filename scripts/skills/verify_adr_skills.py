#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

from adr_skills_registry import ADR_SKILLS, AdrSkillSpec


NEXT_ADR_HEADER_RE = re.compile(r"^\* \*\*T\d{3}[A-Z0-9-]*-ADR-\d{3}\b")
ACTIVE_SKILLS_SECTION_HEADER = "## Active Skills"
FRONTMATTER_NAME_RE = re.compile(r"^name:\s*(?P<name>\S+)\s*$", re.MULTILINE)


@dataclass(frozen=True)
class CheckResult:
    name: str
    ok: bool
    detail: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Verify ADR Skills System distribution + extraction behavior.\n"
            "Scope: registry-driven Active Skills.\n"
            "Default mode is read-only."
        )
    )
    parser.add_argument(
        "--drift-demo",
        action="store_true",
        help="Write temporary drift into the Codex mirror, prove detection, then restore parity.",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print additional diagnostics for troubleshooting.",
    )
    return parser.parse_args()


def find_repo_root(start: Path) -> Path:
    start = start.resolve()
    for candidate in [start, *start.parents]:
        if (candidate / "prompt").is_dir() and (candidate / ".codex").exists():
            return candidate
    raise RuntimeError("Could not locate repo root (expected `prompt/` and `.codex/`).")


def run(
    args: list[str],
    *,
    cwd: Path,
    verbose: bool,
) -> subprocess.CompletedProcess[str]:
    if verbose:
        print(f"$ {' '.join(args)}")
    return subprocess.run(
        args,
        cwd=str(cwd),
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


def check_ssot(repo_root: Path, skill: AdrSkillSpec) -> CheckResult:
    ssot_dir = repo_root / skill.ssot_dir
    required = [
        ssot_dir / "SKILL.md",
        repo_root / skill.extraction_script,
        repo_root / skill.codex_sync_script,
    ]
    missing = [str(path) for path in required if not path.exists()]
    if missing:
        return CheckResult(
            name=f"{skill.skill_name}: SSOT structure",
            ok=False,
            detail="Missing required SSOT files:\n- " + "\n- ".join(missing),
        )
    return CheckResult(name=f"{skill.skill_name}: SSOT structure", ok=True, detail=str(ssot_dir))


def check_skill_frontmatter_name(repo_root: Path, skill: AdrSkillSpec) -> CheckResult:
    skill_md = repo_root / skill.ssot_dir / "SKILL.md"
    if not skill_md.exists():
        return CheckResult(
            name=f"{skill.skill_name}: Frontmatter name",
            ok=False,
            detail=f"Missing: {skill_md}",
        )

    text = skill_md.read_text(encoding="utf-8", errors="replace")

    match = FRONTMATTER_NAME_RE.search(text)
    if not match:
        return CheckResult(
            name=f"{skill.skill_name}: Frontmatter name",
            ok=False,
            detail="Missing required YAML frontmatter field: `name:`",
        )

    declared = match.group("name").strip()
    if declared != skill.skill_name:
        return CheckResult(
            name=f"{skill.skill_name}: Frontmatter name",
            ok=False,
            detail=f"SKILL.md declares name={declared!r}, expected {skill.skill_name!r}",
        )

    return CheckResult(
        name=f"{skill.skill_name}: Frontmatter name",
        ok=True,
        detail=f"name matches skill_name ({skill.skill_name})",
    )


def check_naming_conventions(skill: AdrSkillSpec) -> CheckResult:
    """
    Enforce strict name alignment:
    - skill_name must match directory/symlink/mirror basenames
    - skill paths must follow the canonical layout used across this repo
    """

    expected_ssot_dir = Path("prompt/skills") / skill.skill_name
    expected_claude_link = Path(".claude/skills") / skill.skill_name
    expected_codex_mirror_dir = Path(".codex/skills") / skill.skill_name

    mismatches: list[str] = []
    if skill.ssot_dir != expected_ssot_dir:
        mismatches.append(f"ssot_dir={skill.ssot_dir} (expected {expected_ssot_dir})")
    if skill.claude_link != expected_claude_link:
        mismatches.append(
            f"claude_link={skill.claude_link} (expected {expected_claude_link})"
        )
    if skill.codex_mirror_dir != expected_codex_mirror_dir:
        mismatches.append(
            f"codex_mirror_dir={skill.codex_mirror_dir} (expected {expected_codex_mirror_dir})"
        )

    extraction_skill_dir = skill.extraction_script.parents[1]
    if extraction_skill_dir != skill.ssot_dir:
        mismatches.append(
            f"extraction_script={skill.extraction_script} (expected under {skill.ssot_dir}/scripts/)"
        )

    sync_skill_dir = skill.codex_sync_script.parents[1]
    if sync_skill_dir != skill.ssot_dir:
        mismatches.append(
            f"codex_sync_script={skill.codex_sync_script} (expected under {skill.ssot_dir}/scripts/)"
        )

    if mismatches:
        return CheckResult(
            name=f"{skill.skill_name}: Naming conventions (strict)",
            ok=False,
            detail="Name/path mismatches:\n- " + "\n- ".join(mismatches),
        )
    return CheckResult(
        name=f"{skill.skill_name}: Naming conventions (strict)",
        ok=True,
        detail="All canonical paths match skill_name.",
    )


def check_claude_symlink(repo_root: Path, skill: AdrSkillSpec) -> CheckResult:
    link_path = repo_root / skill.claude_link
    ssot_dir = repo_root / skill.ssot_dir
    if not link_path.exists():
        return CheckResult(
            name=f"{skill.skill_name}: Claude distribution (symlink)",
            ok=False,
            detail=f"Missing: {link_path}",
        )
    if not link_path.is_symlink():
        return CheckResult(
            name=f"{skill.skill_name}: Claude distribution (symlink)",
            ok=False,
            detail=f"Expected symlink but found non-symlink: {link_path}",
        )
    resolved = link_path.resolve()
    if resolved != ssot_dir.resolve():
        return CheckResult(
            name=f"{skill.skill_name}: Claude distribution (symlink)",
            ok=False,
            detail=f"Symlink resolves to {resolved}, expected {ssot_dir.resolve()}",
        )
    return CheckResult(
        name=f"{skill.skill_name}: Claude distribution (symlink)",
        ok=True,
        detail=f"{link_path} -> {resolved}",
    )


def check_codex_mirror(repo_root: Path, skill: AdrSkillSpec) -> CheckResult:
    mirror_dir = repo_root / skill.codex_mirror_dir
    if not mirror_dir.exists():
        return CheckResult(
            name=f"{skill.skill_name}: Codex distribution (mirror)",
            ok=False,
            detail=f"Missing: {mirror_dir}",
        )
    if mirror_dir.is_symlink():
        return CheckResult(
            name=f"{skill.skill_name}: Codex distribution (mirror)",
            ok=False,
            detail=f"Expected real directory (not symlink): {mirror_dir}",
        )
    if not mirror_dir.is_dir():
        return CheckResult(
            name=f"{skill.skill_name}: Codex distribution (mirror)",
            ok=False,
            detail=f"Expected directory but found non-directory: {mirror_dir}",
        )
    required = [
        mirror_dir / "SKILL.md",
        mirror_dir / "scripts" / skill.extraction_script.name,
    ]
    missing = [str(path) for path in required if not path.exists()]
    if missing:
        return CheckResult(
            name=f"{skill.skill_name}: Codex distribution (mirror)",
            ok=False,
            detail="Missing required mirror files:\n- " + "\n- ".join(missing),
        )
    return CheckResult(
        name=f"{skill.skill_name}: Codex distribution (mirror)", ok=True, detail=str(mirror_dir)
    )


def check_adr_extraction(
    repo_root: Path, skill: AdrSkillSpec, *, verbose: bool
) -> CheckResult:
    script = repo_root / skill.extraction_script
    proc = run(["python3", str(script)], cwd=repo_root, verbose=verbose)
    if proc.returncode != 0:
        detail = "Extraction script failed.\n"
        if proc.stdout.strip():
            detail += f"\nSTDOUT:\n{proc.stdout}"
        if proc.stderr.strip():
            detail += f"\nSTDERR:\n{proc.stderr}"
        return CheckResult(
            name=f"{skill.skill_name}: Extraction ({skill.adr_id} only)",
            ok=False,
            detail=detail.strip(),
        )

    output = proc.stdout
    if skill.expected_anchor not in output:
        return CheckResult(
            name=f"{skill.skill_name}: Extraction ({skill.adr_id} only)",
            ok=False,
            detail=f"Output did not contain expected anchor: {skill.expected_anchor}",
        )

    header_lines = [line for line in output.splitlines() if NEXT_ADR_HEADER_RE.match(line)]
    if len(header_lines) > 1:
        return CheckResult(
            name=f"{skill.skill_name}: Extraction ({skill.adr_id} only)",
            ok=False,
            detail="Output appears to include multiple ADR header blocks:\n- "
            + "\n- ".join(header_lines),
        )
    if header_lines and skill.adr_id not in header_lines[0]:
        return CheckResult(
            name=f"{skill.skill_name}: Extraction ({skill.adr_id} only)",
            ok=False,
            detail=f"First ADR header in output was not {skill.adr_id}: {header_lines[0]}",
        )

    # Enforce "single ADR list-item block" invariant:
    # after the ADR bullet header, all non-empty lines must be indented
    # (2+ spaces or a tab). This prevents unintended trailing output
    # (e.g., subsequent headings/tables after the ADR list item ends).
    output_lines = output.splitlines()
    header_index: int | None = None
    for index, line in enumerate(output_lines):
        if NEXT_ADR_HEADER_RE.match(line):
            header_index = index
            break

    if header_index is None:
        return CheckResult(
            name=f"{skill.skill_name}: Extraction ({skill.adr_id} only)",
            ok=False,
            detail="Output did not contain a recognizable ADR header line.",
        )

    saw_body_line = False
    for line in output_lines[header_index + 1 :]:
        if not line.strip():
            continue
        if line.startswith("\t") or line.startswith("  "):
            saw_body_line = True
            continue
        return CheckResult(
            name=f"{skill.skill_name}: Extraction ({skill.adr_id} only)",
            ok=False,
            detail=(
                "Output contained unintended non-indented trailing content after the ADR header.\n"
                "Expected ADR blocks to be a single list item whose body lines are indented by 2+ spaces or a tab.\n"
                f"Offending line: {line}"
            ),
        )

    if not saw_body_line:
        return CheckResult(
            name=f"{skill.skill_name}: Extraction ({skill.adr_id} only)",
            ok=False,
            detail=(
                "Output did not contain any indented ADR body lines.\n"
                "Expected the ADR block to be a list item with a body indented by 2+ spaces or a tab."
            ),
        )

    return CheckResult(
        name=f"{skill.skill_name}: Extraction ({skill.adr_id} only)",
        ok=True,
        detail="Anchor present and extraction output is bounded to a single ADR list-item block.",
    )


def check_codex_mirror_parity(
    repo_root: Path, skill: AdrSkillSpec, *, verbose: bool
) -> CheckResult:
    script = repo_root / skill.codex_sync_script
    proc = run(["python3", str(script), "--check"], cwd=repo_root, verbose=verbose)
    if proc.returncode != 0:
        detail = "Mirror parity check failed (drift detected).\n"
        if proc.stdout.strip():
            detail += f"\nSTDOUT:\n{proc.stdout}"
        if proc.stderr.strip():
            detail += f"\nSTDERR:\n{proc.stderr}"
        return CheckResult(
            name=f"{skill.skill_name}: Codex mirror parity (sync --check)",
            ok=False,
            detail=detail.strip(),
        )
    return CheckResult(
        name=f"{skill.skill_name}: Codex mirror parity (sync --check)",
        ok=True,
        detail=proc.stdout.strip() or "Mirror matches SSOT.",
    )


def run_drift_demo(
    repo_root: Path, skill: AdrSkillSpec, *, verbose: bool
) -> list[CheckResult]:
    results: list[CheckResult] = []

    mirror_skill_md = repo_root / skill.codex_mirror_dir / "SKILL.md"
    sync_script = repo_root / skill.codex_sync_script

    if not mirror_skill_md.exists():
        return [
            CheckResult(
                name=f"{skill.skill_name}: Drift demo (setup)",
                ok=False,
                detail=f"Expected mirror file missing: {mirror_skill_md}",
            )
        ]

    original = mirror_skill_md.read_text(encoding="utf-8")
    try:
        mirror_skill_md.write_text(
            original + "\n# DRIFT-DEMO: temporary change\n", encoding="utf-8"
        )

        proc_check = run(["python3", str(sync_script), "--check"], cwd=repo_root, verbose=verbose)
        if proc_check.returncode == 0:
            results.append(
                CheckResult(
                    name=f"{skill.skill_name}: Drift demo (detect drift)",
                    ok=False,
                    detail="Expected --check to fail after introducing drift, but it passed.",
                )
            )
        else:
            results.append(
                CheckResult(
                    name=f"{skill.skill_name}: Drift demo (detect drift)",
                    ok=True,
                    detail=(proc_check.stdout.strip() or "Drift detected as expected."),
                )
            )

        proc_sync = run(["python3", str(sync_script)], cwd=repo_root, verbose=verbose)
        if proc_sync.returncode != 0:
            results.append(
                CheckResult(
                    name=f"{skill.skill_name}: Drift demo (sync restore)",
                    ok=False,
                    detail=(proc_sync.stderr.strip() or proc_sync.stdout.strip() or "Sync failed."),
                )
            )
        else:
            results.append(
                CheckResult(
                    name=f"{skill.skill_name}: Drift demo (sync restore)",
                    ok=True,
                    detail=(proc_sync.stdout.strip() or "Synced SSOT -> mirror."),
                )
            )

        proc_check2 = run(["python3", str(sync_script), "--check"], cwd=repo_root, verbose=verbose)
        if proc_check2.returncode != 0:
            results.append(
                CheckResult(
                    name=f"{skill.skill_name}: Drift demo (parity restored)",
                    ok=False,
                    detail=(proc_check2.stdout.strip() or proc_check2.stderr.strip() or "Parity check failed."),
                )
            )
        else:
            results.append(
                CheckResult(
                    name=f"{skill.skill_name}: Drift demo (parity restored)",
                    ok=True,
                    detail=(proc_check2.stdout.strip() or "Mirror matches SSOT."),
                )
            )
    finally:
        if mirror_skill_md.read_text(encoding="utf-8") != original:
            mirror_skill_md.write_text(original, encoding="utf-8")

    return results


def print_results(results: list[CheckResult]) -> None:
    for result in results:
        status = "PASS" if result.ok else "FAIL"
        print(f"[{status}] {result.name}")
        if result.detail.strip():
            for line in result.detail.strip().splitlines():
                print(f"  {line}")


def parse_active_skills_from_catalog(catalog_text: str) -> list[str]:
    lines = catalog_text.splitlines()
    active: list[str] = []

    in_active = False
    for raw in lines:
        line = raw.strip()
        if line == ACTIVE_SKILLS_SECTION_HEADER:
            in_active = True
            continue
        if in_active and line.startswith("## "):
            break
        if in_active and line.startswith("### "):
            active.append(line.removeprefix("### ").strip())
    return active


def check_registry_matches_catalog(repo_root: Path) -> list[CheckResult]:
    catalog_path = repo_root / "prompt/documentation/adr_skills_catalog.md"
    if not catalog_path.exists():
        return [
            CheckResult(
                name="Catalog alignment (Active Skills)",
                ok=False,
                detail=f"Missing catalog file: {catalog_path}",
            )
        ]

    catalog_text = catalog_path.read_text(encoding="utf-8", errors="replace")
    active = parse_active_skills_from_catalog(catalog_text)
    registry_names = [skill.skill_name for skill in ADR_SKILLS]

    missing_in_registry = [name for name in active if name not in registry_names]
    extra_in_registry = [name for name in registry_names if name not in active]

    results: list[CheckResult] = []
    if missing_in_registry:
        results.append(
            CheckResult(
                name="Catalog alignment (Active Skills): missing in registry",
                ok=False,
                detail="These Active Skills are not in the registry:\n- "
                + "\n- ".join(missing_in_registry),
            )
        )
    else:
        results.append(
            CheckResult(
                name="Catalog alignment (Active Skills): missing in registry",
                ok=True,
                detail="All Active Skills are present in the registry.",
            )
        )

    if extra_in_registry:
        results.append(
            CheckResult(
                name="Catalog alignment (Active Skills): extra in registry",
                ok=False,
                detail="These registry skills are not listed as Active Skills:\n- "
                + "\n- ".join(extra_in_registry),
            )
        )
    else:
        results.append(
            CheckResult(
                name="Catalog alignment (Active Skills): extra in registry",
                ok=True,
                detail="Registry contains only Active Skills.",
            )
        )

    return results


def main() -> int:
    args = parse_args()
    try:
        repo_root = find_repo_root(Path(__file__))
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    results: list[CheckResult] = []

    results.extend(check_registry_matches_catalog(repo_root))
    for skill in ADR_SKILLS:
        results.extend(
            [
                check_naming_conventions(skill),
                check_skill_frontmatter_name(repo_root, skill),
                check_ssot(repo_root, skill),
                check_claude_symlink(repo_root, skill),
                check_codex_mirror(repo_root, skill),
                check_adr_extraction(repo_root, skill, verbose=args.verbose),
                check_codex_mirror_parity(repo_root, skill, verbose=args.verbose),
            ]
        )

    if args.drift_demo:
        for skill in ADR_SKILLS:
            results.extend(run_drift_demo(repo_root, skill, verbose=args.verbose))
    else:
        results.append(
            CheckResult(
                name="Drift demo",
                ok=True,
                detail="SKIPPED (run with --drift-demo to execute).",
            )
        )

    print_results(results)

    failed = [result for result in results if not result.ok]
    if failed:
        print("\nSUMMARY: FAIL")
        return 1
    print("\nSUMMARY: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
