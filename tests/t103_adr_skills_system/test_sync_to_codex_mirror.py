import importlib.util
import sys
from pathlib import Path

import pytest


def load_sync_module():
    module_path = Path("prompt/scripts/skills/sync_to_codex_mirror.py").resolve()
    spec = importlib.util.spec_from_file_location("sync_to_codex_mirror", module_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Failed to load sync module spec from {module_path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.mark.unit
@pytest.mark.fast
def test_check_fails_on_drift(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    ssot_dir = tmp_path / "prompt/skills/t102-adr-005-id-spec"
    mirror_dir = tmp_path / ".codex/skills/t102-adr-005-id-spec"

    (ssot_dir / "scripts").mkdir(parents=True, exist_ok=True)
    mirror_dir.mkdir(parents=True, exist_ok=True)
    (mirror_dir / "scripts").mkdir(parents=True, exist_ok=True)

    ssot_skill_md = ssot_dir / "SKILL.md"
    ssot_print = ssot_dir / "scripts/print_t102_adr_005.py"
    ssot_skill_md.write_text("ssot-skill\n", encoding="utf-8")
    ssot_print.write_text("print('ssot')\n", encoding="utf-8")

    (mirror_dir / "SKILL.md").write_text("mirror-skill\n", encoding="utf-8")
    (mirror_dir / "scripts/print_t102_adr_005.py").write_text(
        "print('ssot')\n", encoding="utf-8"
    )

    sync = load_sync_module()
    rc = sync.sync_to_codex_mirror(
        ssot_dir=ssot_dir,
        dest_dir=mirror_dir,
        print_script=ssot_print,
        check=True,
    )

    captured = capsys.readouterr()
    assert rc != 0
    assert "Mirror differs from SSOT:" in captured.out


@pytest.mark.unit
@pytest.mark.fast
def test_sync_restores_parity(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    ssot_dir = tmp_path / "prompt/skills/t102-adr-005-id-spec"
    mirror_dir = tmp_path / ".codex/skills/t102-adr-005-id-spec"

    (ssot_dir / "scripts").mkdir(parents=True, exist_ok=True)
    mirror_dir.mkdir(parents=True, exist_ok=True)
    (mirror_dir / "scripts").mkdir(parents=True, exist_ok=True)

    ssot_skill_md = ssot_dir / "SKILL.md"
    ssot_print = ssot_dir / "scripts/print_t102_adr_005.py"
    ssot_skill_md.write_text("ssot-skill\n", encoding="utf-8")
    ssot_print.write_text("print('ssot')\n", encoding="utf-8")

    (mirror_dir / "SKILL.md").write_text("drifted\n", encoding="utf-8")
    (mirror_dir / "scripts/print_t102_adr_005.py").write_text(
        "print('ssot')\n", encoding="utf-8"
    )

    sync = load_sync_module()

    rc_sync = sync.sync_to_codex_mirror(
        ssot_dir=ssot_dir,
        dest_dir=mirror_dir,
        print_script=ssot_print,
        check=False,
    )
    captured_sync = capsys.readouterr()
    assert rc_sync == 0
    assert "Synced SSOT ->" in captured_sync.out

    rc_check = sync.sync_to_codex_mirror(
        ssot_dir=ssot_dir,
        dest_dir=mirror_dir,
        print_script=ssot_print,
        check=True,
    )
    captured_check = capsys.readouterr()
    assert rc_check == 0
    assert "Mirror matches SSOT." in captured_check.out


@pytest.mark.unit
@pytest.mark.fast
def test_refuses_sync_when_destination_is_symlink(tmp_path: Path) -> None:
    ssot_dir = tmp_path / "prompt/skills/t102-adr-005-id-spec"
    (ssot_dir / "scripts").mkdir(parents=True, exist_ok=True)
    ssot_print = ssot_dir / "scripts/print_t102_adr_005.py"
    (ssot_dir / "SKILL.md").write_text("ssot-skill\n", encoding="utf-8")
    ssot_print.write_text("print('ssot')\n", encoding="utf-8")

    codex_parent = tmp_path / ".codex/skills"
    codex_parent.mkdir(parents=True, exist_ok=True)

    target_dir = tmp_path / "real_mirror_dir"
    target_dir.mkdir(parents=True, exist_ok=True)

    mirror_link = codex_parent / "t102-adr-005-id-spec"
    try:
        mirror_link.symlink_to(target_dir, target_is_directory=True)
    except (OSError, NotImplementedError) as exc:
        pytest.skip(f"symlinks not supported in this environment: {exc}")

    sync = load_sync_module()
    with pytest.raises(RuntimeError, match="Refusing to sync into symlinked destination directory"):
        sync.sync_to_codex_mirror(
            ssot_dir=ssot_dir,
            dest_dir=mirror_link,
            print_script=ssot_print,
            check=False,
        )
