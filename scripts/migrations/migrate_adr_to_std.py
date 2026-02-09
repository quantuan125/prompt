#!/usr/bin/env python3
import argparse
import difflib
import fnmatch
import re
from datetime import datetime
from pathlib import Path


ADR_ID_PATTERN = re.compile(r"^T\d{3}(?:[A-Z]\d*)?(?:-[A-Z0-9_]+)*-ADR-(\d{3})$")
STD_ID_PATTERN = re.compile(r"^T\d{3}(?:[A-Z]\d*)?(?:-[A-Z0-9_]+)*-STD-(\d{3})$")
TOKEN_REPLACEMENT_PATTERN = re.compile(r"^([^=]+)=(.+)$")

BUILTIN_EXCLUDE_GLOBS = (
    "**/scripts/output/**",
    "**/workspace/scripts/report_*.md",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Migrate combined ADR-based identifiers to STD-based identifiers, "
            "retitle standard artifacts, and perform governed anchor regenerations."
        )
    )
    parser.add_argument(
        "--old-adr-id",
        default=None,
        help="Source ADR ID (e.g., T102-ADR-004). Optional for retitle-only runs.",
    )
    parser.add_argument(
        "--new-std-id",
        default=None,
        help="Target STD ID (e.g., T102-STD-004). Optional for retitle-only runs.",
    )
    parser.add_argument(
        "--std-id",
        default=None,
        help="STD ID target used for anchor regeneration when ADR->STD ID migration is not requested.",
    )
    parser.add_argument("--retitle-from", default=None, help="Original title string to replace.")
    parser.add_argument("--retitle-to", default=None, help="Replacement title string.")
    parser.add_argument(
        "--regen-anchors-id-title",
        action="store_true",
        help="Regenerate anchors from lower(<ID> + <Title>) slug semantics.",
    )
    parser.add_argument(
        "--replace-token",
        action="append",
        default=[],
        help="Arbitrary token replacement in OLD=NEW form. May be passed multiple times.",
    )
    parser.add_argument("--root", default="prompt", help="Root directory to scan for markdown files")
    parser.add_argument(
        "--include-path",
        action="append",
        default=[],
        help="Restrict execution scope to these files/directories. May be passed multiple times.",
    )
    parser.add_argument(
        "--exclude-glob",
        action="append",
        default=[],
        help="Exclude markdown files matching this glob (relative to --root). May be passed multiple times.",
    )
    parser.add_argument(
        "--max-files-changed",
        type=int,
        default=None,
        help="Safety cap: fail execution when changed file count exceeds this value.",
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--dry-run", action="store_true", help="Preview changes only (default)")
    mode.add_argument("--apply", action="store_true", help="Apply changes in-place")
    parser.add_argument(
        "--report-path",
        default=None,
        help="Path to markdown report output (default: prompt/scripts/output/std_migration/report_*.md)",
    )
    return parser.parse_args()


def validate_ids(old_adr_id: str, new_std_id: str) -> None:
    old_match = ADR_ID_PATTERN.match(old_adr_id)
    new_match = STD_ID_PATTERN.match(new_std_id)
    if not old_match:
        raise ValueError(f"Invalid --old-adr-id format: {old_adr_id}")
    if not new_match:
        raise ValueError(f"Invalid --new-std-id format: {new_std_id}")
    if old_match.group(1) != new_match.group(1):
        raise ValueError(
            "Same-number mapping required: "
            f"{old_adr_id} -> {new_std_id} is invalid (numeric suffix mismatch)"
        )


def parse_token_replacements(raw_replacements: list[str]) -> list[tuple[str, str]]:
    parsed: list[tuple[str, str]] = []
    for replacement in raw_replacements:
        match = TOKEN_REPLACEMENT_PATTERN.match(replacement)
        if not match:
            raise ValueError(
                f"Invalid --replace-token value: {replacement}. "
                "Expected OLD=NEW format."
            )
        old_value = match.group(1)
        new_value = match.group(2)
        if not old_value:
            raise ValueError("Invalid --replace-token value: OLD token cannot be empty.")
        parsed.append((old_value, new_value))
    return parsed


def validate_args(args: argparse.Namespace) -> tuple[list[tuple[str, str]], str | None]:
    if bool(args.old_adr_id) != bool(args.new_std_id):
        raise ValueError("--old-adr-id and --new-std-id must be provided together.")
    if args.old_adr_id and args.new_std_id:
        validate_ids(args.old_adr_id.strip(), args.new_std_id.strip())

    if bool(args.retitle_from) != bool(args.retitle_to):
        raise ValueError("--retitle-from and --retitle-to must be provided together.")

    if args.max_files_changed is not None and args.max_files_changed <= 0:
        raise ValueError("--max-files-changed must be greater than zero.")

    token_replacements = parse_token_replacements(args.replace_token)
    target_std_id = args.new_std_id.strip() if args.new_std_id else None
    if args.std_id:
        provided_std_id = args.std_id.strip()
        if target_std_id and target_std_id != provided_std_id:
            raise ValueError("--std-id must match --new-std-id when both are supplied.")
        target_std_id = provided_std_id

    if args.regen_anchors_id_title and not target_std_id:
        raise ValueError(
            "--regen-anchors-id-title requires --std-id or --new-std-id."
        )

    has_operation = any(
        (
            bool(args.old_adr_id and args.new_std_id),
            bool(args.retitle_from and args.retitle_to),
            bool(args.regen_anchors_id_title),
            bool(token_replacements),
        )
    )
    if not has_operation:
        raise ValueError(
            "No transformation selected. Provide ID migration, retitle options, "
            "anchor regeneration, or token replacements."
        )

    return token_replacements, target_std_id


def slugify_id_title(identifier: str, title: str) -> str:
    value = f"{identifier} {title}".lower()
    value = value.replace("&", " and ")
    value = re.sub(r"[^a-z0-9\s-]", "", value)
    value = re.sub(r"[\s_]+", "-", value)
    value = re.sub(r"-{2,}", "-", value)
    return value.strip("-")


def apply_id_migration(text: str, old_adr_id: str, new_std_id: str, counts: dict[str, int]) -> str:
    updated = text

    updated, heading_count = re.subn(
        rf"(?m)^#\s+{re.escape(old_adr_id)}(\b.*)$",
        rf"# {new_std_id}\1",
        updated,
    )
    counts["heading_rewrites"] = heading_count

    old_clause = f"{old_adr_id}-CLAUSE-"
    new_clause = f"{new_std_id}-CLAUSE-"
    clause_count = updated.count(old_clause)
    if clause_count:
        updated = updated.replace(old_clause, new_clause)
    counts["clause_rewrites"] = clause_count

    updated, dr_body_count = re.subn(
        rf"(?m)^(\*\s+\*\*){re.escape(old_adr_id)}(\s+\()",
        rf"\1{new_std_id}-ADR-001\2",
        updated,
    )
    counts["dr_body_id_rewrites"] = dr_body_count

    updated, full_ref_count = re.subn(
        rf"`{re.escape(old_adr_id)}\s+\(([^`]+)\)`",
        rf"`{new_std_id} (\1)`",
        updated,
    )
    counts["full_reference_rewrites"] = full_ref_count

    updated, bare_ref_count = re.subn(
        rf"`{re.escape(old_adr_id)}`",
        rf"`{new_std_id}`",
        updated,
    )
    counts["bare_reference_rewrites"] = bare_ref_count

    old_slug = old_adr_id.lower()
    new_slug = new_std_id.lower()
    slug_count = updated.count(old_slug)
    if slug_count:
        updated = updated.replace(old_slug, new_slug)
    counts["legacy_slug_rewrites"] = slug_count

    updated, plain_id_count = re.subn(
        rf"(?<![A-Za-z0-9]){re.escape(old_adr_id)}(?![A-Za-z0-9])",
        new_std_id,
        updated,
    )
    counts["plain_id_rewrites"] = plain_id_count

    return updated


def apply_retitle(text: str, retitle_from: str, retitle_to: str, counts: dict[str, int]) -> str:
    title_count = text.count(retitle_from)
    counts["title_rewrites"] = title_count
    if not title_count:
        return text
    return text.replace(retitle_from, retitle_to)


def apply_token_replacements(
    text: str,
    token_replacements: list[tuple[str, str]],
    counts: dict[str, int],
) -> str:
    updated = text
    total = 0
    for old_value, new_value in token_replacements:
        replacement_count = updated.count(old_value)
        if replacement_count:
            updated = updated.replace(old_value, new_value)
            total += replacement_count
    counts["token_replacements"] = total
    return updated


def apply_anchor_regeneration(text: str, std_id: str, counts: dict[str, int]) -> str:
    updated = text
    top_anchor_count = 0
    dr_anchor_count = 0

    heading_match = re.search(rf"(?m)^#\s+{re.escape(std_id)}\s+[—-]\s+(.+)$", updated)
    if heading_match:
        heading_title = heading_match.group(1).strip()
        top_anchor = slugify_id_title(std_id, heading_title)
        top_anchor_pattern = re.compile(
            rf"(?m)(^#\s+{re.escape(std_id)}\s+[—-]\s+{re.escape(heading_title)}\s*$\n)\{{#[^}}\n]*\}}"
        )
        updated, top_anchor_count = top_anchor_pattern.subn(
            rf"\1{{#{top_anchor}}}",
            updated,
            count=1,
        )

    dr_anchor_pattern = re.compile(
        rf"(?m)^(\*\s+\*\*{re.escape(std_id)}-ADR-(\d{{3}})\s+\()([^)]+)(\)\*\*\s+)\{{#[^}}\n]*\}}"
    )

    def _replace_dr_anchor(match: re.Match) -> str:
        identifier = f"{std_id}-ADR-{match.group(2)}"
        decision_title = match.group(3).strip()
        anchor = slugify_id_title(identifier, decision_title)
        return f"{match.group(1)}{decision_title}{match.group(4)}{{#{anchor}}}"

    updated, dr_anchor_count = dr_anchor_pattern.subn(_replace_dr_anchor, updated)

    counts["top_anchor_regenerations"] = top_anchor_count
    counts["dr_anchor_regenerations"] = dr_anchor_count
    return updated


def transform_text(
    text: str,
    old_adr_id: str | None,
    new_std_id: str | None,
    retitle_from: str | None,
    retitle_to: str | None,
    token_replacements: list[tuple[str, str]],
    regen_anchors_id_title: bool,
    target_std_id: str | None,
) -> tuple[str, dict[str, int]]:
    counts: dict[str, int] = {}
    updated = text

    if old_adr_id and new_std_id:
        updated = apply_id_migration(updated, old_adr_id, new_std_id, counts)

    if retitle_from and retitle_to:
        updated = apply_retitle(updated, retitle_from, retitle_to, counts)

    if token_replacements:
        updated = apply_token_replacements(updated, token_replacements, counts)
    else:
        counts["token_replacements"] = 0

    if regen_anchors_id_title and target_std_id:
        updated = apply_anchor_regeneration(updated, target_std_id, counts)
    else:
        counts["top_anchor_regenerations"] = 0
        counts["dr_anchor_regenerations"] = 0

    return updated, counts


def read_text_with_fallback(path: Path) -> tuple[str, str] | tuple[None, None]:
    raw = path.read_bytes()
    for encoding in ("utf-8", "utf-8-sig", "latin-1"):
        try:
            return raw.decode(encoding), encoding
        except UnicodeDecodeError:
            continue
    return None, None


def default_report_path(old_adr_id: str | None, new_std_id: str | None) -> Path:
    base_dir = Path("prompt/scripts/output/std_migration")
    if old_adr_id and new_std_id:
        safe_old = old_adr_id.replace("-", "_")
        safe_new = new_std_id.replace("-", "_")
        return base_dir / f"report_{safe_old}_to_{safe_new}.md"
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return base_dir / f"report_std_migration_{timestamp}.md"


def resolve_include_paths(root: Path, include_args: list[str]) -> list[Path]:
    includes: list[Path] = []
    for value in include_args:
        candidate = Path(value).expanduser()
        if not candidate.is_absolute():
            candidate = Path.cwd() / candidate
        candidate = candidate.resolve()
        if not candidate.exists():
            raise FileNotFoundError(f"--include-path does not exist: {value}")
        if root not in candidate.parents and candidate != root:
            raise ValueError(
                f"--include-path must be within --root. include={candidate} root={root}"
            )
        includes.append(candidate)
    return includes


def is_included(path: Path, include_paths: list[Path]) -> bool:
    if not include_paths:
        return True
    for include_path in include_paths:
        if include_path.is_dir():
            if path == include_path or include_path in path.parents:
                return True
        elif path == include_path:
            return True
    return False


def is_excluded(path: Path, root: Path, exclude_globs: list[str], report_path: Path) -> bool:
    if path.resolve() == report_path.resolve():
        return True
    if path.name.startswith("raw_"):
        return True

    rel_path = path.relative_to(root).as_posix()
    for pattern in exclude_globs:
        if fnmatch.fnmatch(rel_path, pattern) or fnmatch.fnmatch(path.name, pattern):
            return True
    return False


def build_report(
    root: Path,
    apply_mode: bool,
    changed_items: list[dict],
    include_paths: list[Path],
    exclude_globs: list[str],
    skipped_include: int,
    skipped_excluded: int,
    skipped_encoding: int,
    max_files_changed: int | None,
) -> str:
    lines: list[str] = []
    lines.append("# Migration Report")
    lines.append("")
    lines.append(f"- Mode: {'apply' if apply_mode else 'dry-run'}")
    lines.append(f"- Root: `{root}`")
    lines.append(f"- Files changed: {len(changed_items)}")
    lines.append(f"- Files skipped (include filter): {skipped_include}")
    lines.append(f"- Files skipped (exclude rules): {skipped_excluded}")
    lines.append(f"- Files skipped (encoding): {skipped_encoding}")
    if max_files_changed is not None:
        lines.append(f"- Safety cap (`max-files-changed`): {max_files_changed}")
    if include_paths:
        lines.append("- Include paths:")
        for include_path in include_paths:
            lines.append(f"  - `{include_path}`")
    lines.append("- Exclude globs:")
    for pattern in exclude_globs:
        lines.append(f"  - `{pattern}`")
    lines.append("")

    if not changed_items:
        lines.append("No changes detected.")
        return "\n".join(lines) + "\n"

    lines.append("## Change Summary")
    lines.append("")
    for item in changed_items:
        lines.append(f"- `{item['path']}`")
        if item["rename_to"]:
            lines.append(f"  - rename: `{item['path']}` -> `{item['rename_to']}`")
        counts = item["counts"]
        for key in sorted(counts.keys()):
            if counts[key]:
                lines.append(f"  - {key}: {counts[key]}")

    lines.append("")
    lines.append("## Unified Diffs")
    lines.append("")
    for item in changed_items:
        lines.append(f"### `{item['path']}`")
        lines.append("")
        diff = item["diff"].strip()
        if diff:
            lines.append("```diff")
            lines.append(diff)
            lines.append("```")
        else:
            lines.append("_No textual diff (rename-only)._")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    args = parse_args()
    token_replacements, target_std_id = validate_args(args)

    old_adr_id = args.old_adr_id.strip() if args.old_adr_id else None
    new_std_id = args.new_std_id.strip() if args.new_std_id else None
    retitle_from = args.retitle_from.strip() if args.retitle_from else None
    retitle_to = args.retitle_to.strip() if args.retitle_to else None

    root = Path(args.root).resolve()
    if not root.exists():
        raise FileNotFoundError(f"Root path does not exist: {root}")

    report_path = Path(args.report_path) if args.report_path else default_report_path(old_adr_id, new_std_id)
    report_path = report_path.resolve()
    report_path.parent.mkdir(parents=True, exist_ok=True)

    include_paths = resolve_include_paths(root, args.include_path)
    exclude_globs = [*BUILTIN_EXCLUDE_GLOBS, *args.exclude_glob]

    changed_items: list[dict] = []
    skipped_include = 0
    skipped_excluded = 0
    skipped_encoding = 0

    markdown_files = sorted(root.rglob("*.md"))
    for path in markdown_files:
        if not is_included(path, include_paths):
            skipped_include += 1
            continue
        if is_excluded(path, root, exclude_globs, report_path):
            skipped_excluded += 1
            continue

        original, encoding = read_text_with_fallback(path)
        if original is None:
            skipped_encoding += 1
            continue

        transformed, counts = transform_text(
            original,
            old_adr_id,
            new_std_id,
            retitle_from,
            retitle_to,
            token_replacements,
            args.regen_anchors_id_title,
            target_std_id,
        )
        text_changed = transformed != original

        target_path = path
        rename_to: Path | None = None
        if old_adr_id and new_std_id and old_adr_id in path.name:
            rename_to = path.with_name(path.name.replace(old_adr_id, new_std_id))
            target_path = rename_to

        if not text_changed and rename_to is None:
            continue

        diff = "\n".join(
            difflib.unified_diff(
                original.splitlines(),
                transformed.splitlines(),
                fromfile=str(path),
                tofile=str(target_path),
                lineterm="",
            )
        )

        changed_items.append(
            {
                "path": str(path),
                "rename_to": str(rename_to) if rename_to else None,
                "counts": counts,
                "diff": diff,
                "transformed_text": transformed,
                "encoding": encoding,
            }
        )

    if args.max_files_changed is not None and len(changed_items) > args.max_files_changed:
        raise RuntimeError(
            f"Safety cap exceeded: changed={len(changed_items)} max={args.max_files_changed}. "
            "Re-run with narrower scope or higher cap."
        )

    if args.apply:
        for item in changed_items:
            source_path = Path(item["path"])
            transformed_text = item["transformed_text"]
            rename_to = item["rename_to"]
            encoding = item["encoding"]

            source_path.write_text(transformed_text, encoding=encoding)
            if rename_to:
                target = Path(rename_to)
                target.parent.mkdir(parents=True, exist_ok=True)
                if target.exists() and target != source_path:
                    raise FileExistsError(f"Refusing to overwrite existing target: {target}")
                source_path.rename(target)

    report = build_report(
        root,
        bool(args.apply),
        changed_items,
        include_paths,
        exclude_globs,
        skipped_include,
        skipped_excluded,
        skipped_encoding,
        args.max_files_changed,
    )
    report_path.write_text(report, encoding="utf-8")

    print(
        f"mode={'apply' if args.apply else 'dry-run'} "
        f"changed={len(changed_items)} "
        f"skipped_include={skipped_include} "
        f"skipped_excluded={skipped_excluded} "
        f"skipped_encoding={skipped_encoding}"
    )
    print(f"report={report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
