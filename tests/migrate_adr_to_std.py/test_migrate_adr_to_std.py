import importlib.util
import sys
from pathlib import Path

import pytest


def load_migration_module():
    module_path = Path("prompt/scripts/migrations/migrate_adr_to_std.py").resolve()
    spec = importlib.util.spec_from_file_location("migrate_adr_to_std", module_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Failed to load migration module spec from {module_path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.mark.unit
@pytest.mark.fast
def test_default_id_migration_rewrites_plain_text_occurrences() -> None:
    migration = load_migration_module()
    text = "Plain prose reference: T102-ADR-004 should be updated.\n"

    transformed, counts = migration.transform_text(
        text=text,
        old_adr_id="T102-ADR-004",
        new_std_id="T102-STD-004",
        retitle_from=None,
        retitle_to=None,
        token_replacements=[],
        regen_anchors_id_title=False,
        target_std_id=None,
    )

    assert "T102-STD-004 should be updated." in transformed
    assert "T102-ADR-004 should be updated." not in transformed
    assert counts["plain_id_rewrites"] == 1


@pytest.mark.unit
@pytest.mark.fast
def test_default_id_migration_uses_word_boundary_safe_plain_rewrite() -> None:
    migration = load_migration_module()
    text = "XT102-ADR-004Y T102-ADR-004 T102-ADR-004X\n"

    transformed, counts = migration.transform_text(
        text=text,
        old_adr_id="T102-ADR-004",
        new_std_id="T102-STD-004",
        retitle_from=None,
        retitle_to=None,
        token_replacements=[],
        regen_anchors_id_title=False,
        target_std_id=None,
    )

    assert "XT102-ADR-004Y" in transformed
    assert "T102-STD-004 " in transformed
    assert "T102-ADR-004X" in transformed
    assert counts["plain_id_rewrites"] == 1


@pytest.mark.unit
@pytest.mark.fast
def test_default_id_migration_keeps_structured_rewrites() -> None:
    migration = load_migration_module()
    text = (
        "`T102-ADR-004 (Decision Records Index)`\n"
        "`T102-ADR-004`\n"
        "T102-ADR-004-CLAUSE-001\n"
        "Also plain T102-ADR-004 here.\n"
    )

    transformed, counts = migration.transform_text(
        text=text,
        old_adr_id="T102-ADR-004",
        new_std_id="T102-STD-004",
        retitle_from=None,
        retitle_to=None,
        token_replacements=[],
        regen_anchors_id_title=False,
        target_std_id=None,
    )

    assert "`T102-STD-004 (Decision Records Index)`" in transformed
    assert "`T102-STD-004`" in transformed
    assert "T102-STD-004-CLAUSE-001" in transformed
    assert "Also plain T102-STD-004 here." in transformed
    assert counts["full_reference_rewrites"] == 1
    assert counts["bare_reference_rewrites"] == 1
    assert counts["clause_rewrites"] == 1
    assert counts["plain_id_rewrites"] == 1


@pytest.mark.unit
@pytest.mark.fast
def test_transform_without_id_migration_leaves_plain_text_unchanged() -> None:
    migration = load_migration_module()
    text = "No migration requested: T102-ADR-004 should remain untouched.\n"

    transformed, _counts = migration.transform_text(
        text=text,
        old_adr_id=None,
        new_std_id=None,
        retitle_from=None,
        retitle_to=None,
        token_replacements=[],
        regen_anchors_id_title=False,
        target_std_id=None,
    )

    assert transformed == text
