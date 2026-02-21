---
artifact_type: 'ANALYSIS'
initiative_id: 'T103'
phase: '0'
context: 'T103-PH000'
version: '1.0.0'
date: '2026-02-12'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
source_communication: 'prompt/artifacts/tasks/T103/workspace/communication/comm_T102-RES-006_skills-retargeting-integration.md'
source_proposal: 'prompt/artifacts/tasks/T104/workspace/PH001/ST002/AC000/proposal/proposal_T104-PH001-ST002-AC000_directory-naming-convention.md'
---

# Analysis: T103-PH000 Standards Retargeting Assessment

## I. PURPOSE

This analysis documents a comprehensive review of all existing T103 materials, assesses the integration impact of `T102-RES-006` (Skills System Retargeting to Standards Canonical Path), evaluates conformance gaps against the `P-STD-004` directory naming convention proposal, and establishes the factual basis for implementation planning within `T103-PH000`.

---

## II. EXECUTIVE SUMMARY

T103 (ADR Skills System) has completed Phases 0-2 of its original plan, delivering a working skills extraction and distribution architecture across three registered skills. A HIGH-priority communication from T102 (`comm_T102-RES-006`) now requires T103 to:

1. **Rename** all "ADR" references to "STD" throughout the skills system
2. **Retarget** extraction from Concept document to canonical standards files in `T102/consultant/standards/`
3. **Update** skill directory names, distribution paths (`.claude/`, `.codex/`), and documentation

Additionally, the `P-STD-004` directory naming convention proposal (from T104) introduces program-level structural standards that T103's existing workspace and file naming do not yet conform to.

This analysis inventories all affected artifacts, identifies conformance gaps, and maps the scope of required changes.

---

## III. CURRENT STATE OF T103

### A. Initiative Overview

| Attribute | Value |
|:--|:--|
| Initiative ID | T103 |
| Focus | ADR Skills System — Claude Code + Codex SSOT distribution |
| Current Phase | PH000 (original Phases 0-2 completed; Phase 3-4 planned) |
| Registered Skills | 3 (t102-adr-005-id-spec, t102-adr-004-drs-index, t102-adr-007-issues-risks-index) |
| Architecture | SSOT in `prompt/skills/`, Claude symlink, Codex mirror, registry-driven verification |

### B. Existing T103 Workspace Files

| File | Path | Naming Convention | Status |
|:--|:--|:--|:--|
| Main plan (Phases 0-2) | `T103/workspace/plan/plan_T103_adr-skills-system.md` | Legacy (pre-UID) | Phases 0-2 completed |
| Phase 3 plan | `T103/workspace/plan/plan_T103A1-ADRSS_phase3.md` | Legacy (pre-UID) | Draft |
| T102 communication | `T103/workspace/communication/comm_T102-RES-006_skills-retargeting-integration.md` | P-STD-004 conformant (`comm_` prefix) | Received |
| Screenshot | `T103/workspace/image/2026-01-02 18_09_58-image - File Explorer.png` | N/A (image) | Reference |

**Observation**: The two plan files use legacy naming patterns that predate the P-STD-004 convention. The communication file already follows the `comm_` prefix convention.

### C. Skills SSOT Structure (Current)

```
prompt/skills/
├── t102-adr-004-drs-index/
│   ├── SKILL.md
│   └── scripts/
│       ├── print_t102_adr_004.py
│       └── sync_to_codex_mirror.py
├── t102-adr-005-id-spec/
│   ├── SKILL.md
│   └── scripts/
│       ├── print_t102_adr_005.py
│       └── sync_to_codex_mirror.py
└── t102-adr-007-issues-risks-index/
    ├── SKILL.md
    └── scripts/
        ├── print_t102_adr_007.py
        └── sync_to_codex_mirror.py
```

**Key characteristics**:
- Directory names use `t102-adr-###` pattern (legacy ADR naming)
- SKILL.md frontmatter `name:` fields already use `t102-std-###` pattern (partially migrated)
- Print scripts target `concept_T102-CONSULTANT.md` (Concept document) as extraction source
- Print scripts search for anchors like `{#t102-adr-005-id-spec}` (ADR-style anchors)

### D. Shared Infrastructure Scripts

| Script | Path | Purpose |
|:--|:--|:--|
| `extract_adr.py` | `prompt/scripts/skills/extract_adr.py` | CLI tool for single ADR block extraction |
| `adr_extraction.py` | `prompt/scripts/skills/adr_extraction.py` | Shared extraction library (anchor-based parsing) |
| `adr_skills_registry.py` | `prompt/scripts/skills/adr_skills_registry.py` | Central registry (`AdrSkillSpec` dataclass, 3 entries) |
| `verify_adr_skills.py` | `prompt/scripts/skills/verify_adr_skills.py` | Comprehensive verification system (567 lines) |
| `install_adr_skills_pre_commit_hook.py` | `prompt/scripts/skills/install_adr_skills_pre_commit_hook.py` | Git pre-commit hook installer |
| `sync_codex_mirrors.py` | `prompt/scripts/skills/sync_codex_mirrors.py` | Registry-driven bulk sync orchestrator |
| `sync_to_codex_mirror.py` | `prompt/scripts/skills/sync_to_codex_mirror.py` | Generic sync engine (SHA256-based parity) |

**Key characteristics**:
- All scripts use "adr" in filenames and internal naming
- `adr_extraction.py` uses `DEFAULT_CONCEPT_PATH` pointing to Concept document
- `adr_skills_registry.py` defines `AdrSkillSpec` dataclass and `ADR_SKILLS` constant
- `verify_adr_skills.py` contains the most complex logic (567 lines) with multiple verification checks
- All import paths reference `adr_extraction`, `adr_skills_registry` module names

### E. Documentation Files

| Document | Path | Purpose |
|:--|:--|:--|
| ADR Skills Catalog | `prompt/documentation/adr_skills_catalog.md` | Authoritative skill catalog (3 active, 2 planned) |
| Scripts Reference | `prompt/documentation/scripts/skills/adr_skills_scripts_reference.md` | Human-facing script documentation |
| Verification Runbook | `prompt/documentation/scripts/skills/adr_skills_verification_runbook.md` | Verification procedures and pass criteria |

### F. Distribution Points

| Distribution | Path Pattern | Status |
|:--|:--|:--|
| Claude Code | `.claude/skills/t102-adr-*` (symlinks) | Not currently created (`.claude/` does not exist) |
| Codex | `.codex/skills/t102-adr-*` (mirror dirs) | Not currently created (`.codex/` does not exist) |
| Git ignore | `.claude/` fully ignored; `.codex/skills/` tracked | Configured in `.gitignore` |

### G. Phase Completion Status

| Phase | Scope | Status | Evidence |
|:--|:--|:--|:--|
| Phase 0 | ADR-005 Skill Conversion | Completed | 16/16 success criteria marked `[x]` |
| Phase 1 | System Expansion (ADR-004, ADR-007) | Completed | 5/6 criteria marked `[x]`; Codex+Claude parity pending |
| Phase 2 | Script Generalization | Completed | 7/7 success criteria marked `[x]` |
| Phase 3 | Single Skill (multi-ADR selector) | Planned (draft) | Plan exists but not started |
| Phase 4 | Registry Generator | Planned | Outlined but no plan file |

---

## IV. T102-RES-006 INTEGRATION IMPACT ASSESSMENT

### A. Communication Summary

The communication (`comm_T102-RES-006`) identifies three required change categories:

1. **Change 1**: Rename "ADR" references to "STD" throughout the skills system
2. **Change 2**: Retarget extraction source from Concept to standards canonical path
3. **Change 3**: Update skill directory names and distribution paths

### B. Complete Affected File Inventory

The following inventory maps every file and component requiring modification, organized by change category.

#### Change 1: ADR-to-STD Renaming

**File renames required**:

| # | Current Path | Proposed Path |
|:--|:--|:--|
| 1 | `prompt/scripts/skills/extract_adr.py` | `prompt/scripts/skills/extract_std.py` |
| 2 | `prompt/scripts/skills/adr_extraction.py` | `prompt/scripts/skills/std_extraction.py` |
| 3 | `prompt/scripts/skills/adr_skills_registry.py` | `prompt/scripts/skills/std_skills_registry.py` |
| 4 | `prompt/scripts/skills/verify_adr_skills.py` | `prompt/scripts/skills/verify_std_skills.py` |
| 5 | `prompt/scripts/skills/install_adr_skills_pre_commit_hook.py` | `prompt/scripts/skills/install_std_skills_pre_commit_hook.py` |
| 6 | `prompt/scripts/skills/sync_codex_mirrors.py` | (No rename needed — generic name) |
| 7 | `prompt/scripts/skills/sync_to_codex_mirror.py` | (No rename needed — generic name) |
| 8 | `prompt/documentation/adr_skills_catalog.md` | `prompt/documentation/std_skills_catalog.md` |
| 9 | `prompt/documentation/scripts/skills/adr_skills_scripts_reference.md` | `prompt/documentation/scripts/skills/std_skills_scripts_reference.md` |
| 10 | `prompt/documentation/scripts/skills/adr_skills_verification_runbook.md` | `prompt/documentation/scripts/skills/std_skills_verification_runbook.md` |

**Internal symbol renames required**:

| Symbol Type | Current | Proposed | File(s) |
|:--|:--|:--|:--|
| Dataclass | `AdrSkillSpec` | `StdSkillSpec` | `adr_skills_registry.py` → `std_skills_registry.py` |
| Constant | `ADR_SKILLS` | `STD_SKILLS` | `adr_skills_registry.py` → `std_skills_registry.py` |
| Import | `from adr_extraction import ...` | `from std_extraction import ...` | Multiple scripts |
| Import | `from adr_skills_registry import ...` | `from std_skills_registry import ...` | Multiple scripts |
| Field | `adr_id` (in registry) | `std_id` | Registry entries |
| Function | `extract_adr_block()` | `extract_std_block()` | `adr_extraction.py` → `std_extraction.py` |
| Variable | `DEFAULT_CONCEPT_PATH` | `DEFAULT_STD_DIR` | `adr_extraction.py` → `std_extraction.py` |
| Docstrings | All "ADR" references | "STD" equivalents | All renamed files |

#### Change 2: Extraction Source Retargeting

| Component | Current Behavior | Required Behavior |
|:--|:--|:--|
| `DEFAULT_CONCEPT_PATH` in extraction module | Points to `concept_T102-CONSULTANT.md` | **Remove**; replace with `DEFAULT_STD_DIR` pointing to `prompt/artifacts/tasks/T102/consultant/standards/` |
| `resolve_concept_path()` function | Searches for concept files with version fallback | Replace with `resolve_std_file()` that maps STD ID to canonical file |
| Anchor-based extraction logic | Searches for `{#t102-adr-###-...}` markers in Concept | Searches for equivalent markers in individual STD files |
| Per-skill print scripts | All target Concept document | Each targets its corresponding `T102-STD-###_*.md` file |

**Per-skill extraction retargeting**:

| Skill | Current Script | Current Anchor | Target STD File | New Anchor |
|:--|:--|:--|:--|:--|
| t102-adr-005-id-spec | `print_t102_adr_005.py` | `{#t102-adr-005-id-spec}` | `T102-STD-005_id-specification-rules.md` | `{#t102-std-005-id-spec}` |
| t102-adr-004-drs-index | `print_t102_adr_004.py` | `{#t102-adr-004-drs-index}` | `standard_T102-STD-004_specification-standard-and-guideline.md` | `{#t102-std-004-drs-index}` |
| t102-adr-007-issues-risks-index | `print_t102_adr_007.py` | `{#t102-adr-007-issues-risks-index}` | `T102-STD-007_issues-risks-index.md` | `{#t102-std-007-issues-risks-index}` |

**Extraction logic changes required**:
- The current `adr_extraction.py` extracts a single list-item block from the Concept document using anchor markers. The new `std_extraction.py` must extract content from individual standards files. This is a **behavioral change** — the extraction algorithm must be revised to handle a different document structure (combined STD files vs. Concept list-item blocks).
- Each STD file uses a combined Specification-Decision Record structure (per T102-STD-004-CLAUSE-016), not the indented list-item format currently expected by the extraction logic.

#### Change 3: Directory and Distribution Path Updates

**Skill SSOT directory renames**:

| Current | Proposed |
|:--|:--|
| `prompt/skills/t102-adr-005-id-spec/` | `prompt/skills/t102-std-005-id-spec/` |
| `prompt/skills/t102-adr-004-drs-index/` | `prompt/skills/t102-std-004-drs-index/` |
| `prompt/skills/t102-adr-007-issues-risks-index/` | `prompt/skills/t102-std-007-issues-risks-index/` |

**Per-skill script renames**:

| Current | Proposed |
|:--|:--|
| `print_t102_adr_005.py` | `print_t102_std_005.py` |
| `print_t102_adr_004.py` | `print_t102_std_004.py` |
| `print_t102_adr_007.py` | `print_t102_std_007.py` |

**Distribution path updates**:

| Distribution | Current Path Pattern | Proposed Path Pattern |
|:--|:--|:--|
| Claude symlinks | `.claude/skills/t102-adr-*` | `.claude/skills/t102-std-*` |
| Codex mirrors | `.codex/skills/t102-adr-*` | `.codex/skills/t102-std-*` |

**Registry entry updates**:

| Field | Current (example: ADR-005) | Proposed |
|:--|:--|:--|
| `skill_name` | `t102-adr-005-id-spec` | `t102-std-005-id-spec` |
| `adr_id` / `std_id` | `ADR-005` | `STD-005` |
| `expected_anchor` | `{#t102-adr-005-id-spec}` | `{#t102-std-005-id-spec}` |
| `ssot_dir` | `prompt/skills/t102-adr-005-id-spec` | `prompt/skills/t102-std-005-id-spec` |
| `claude_link` | `.claude/skills/t102-adr-005-id-spec` | `.claude/skills/t102-std-005-id-spec` |
| `codex_mirror_dir` | `.codex/skills/t102-adr-005-id-spec` | `.codex/skills/t102-std-005-id-spec` |
| `extraction_script` | `...print_t102_adr_005.py` | `...print_t102_std_005.py` |
| `codex_sync_script` | `...t102-adr-005-id-spec/scripts/sync_to_codex_mirror.py` | `...t102-std-005-id-spec/scripts/sync_to_codex_mirror.py` |

### C. Dependency Assessment

| Dependency | Status | Impact on T103 |
|:--|:--|:--|
| T102 STD-Contains-CLAUSE migration (PH001-ST001-AC006) | `completed` (2026-02-08) | Combined standard files exist at canonical path |
| T102 STD migration rollout (PH001-ST003) | `completed` | All 16 STD files present in `T102/consultant/standards/` |
| T102-RES-006 GATE-003 (Client sign-off) | `pending` | Communication recommends actioning **after** GATE-003 approval |
| Anchor markers in STD files | **Unknown** | Must verify that `{#t102-std-###-...}` anchors exist in target STD files |

### D. Risk Factors

| # | Risk | Severity | Notes |
|:--|:--|:--|:--|
| R1 | STD files may not contain expected anchor markers | HIGH | Extraction will fail if anchors are missing; the same failure that prompted this retargeting |
| R2 | Extraction logic assumes Concept list-item block format | MEDIUM | STD files use combined Specification-DR structure; extraction algorithm must be adapted |
| R3 | GATE-003 not yet approved | MEDIUM | Starting implementation before Client sign-off on T102-RES-006 may require rework |
| R4 | Phase 3 plan (multi-ADR selector) becomes stale | LOW | Phase 3 plan references Concept-based extraction; must be revised or superseded |
| R5 | SKILL.md content references to ADR anchors | LOW | SKILL.md files instruct agents to run print scripts; instructions need updating |

---

## V. P-STD-004 CONFORMANCE ASSESSMENT

### A. T103 Workspace Structure Gaps

The `P-STD-004` directory naming convention proposal establishes standards that T103's current workspace does not fully conform to.

| Convention | Requirement | T103 Current State | Conformance |
|:--|:--|:--|:--|
| Conv. 1 (Root Structure) | `ssot/`, `standard/`, `research/`, `workspace/` at initiative root | Only `workspace/` exists | Partial |
| Conv. 2 (File Naming Stems) | `plan_<SID>-PH###[-ST###].md` | Legacy naming (`plan_T103_adr-skills-system.md`) | Non-conformant |
| Conv. 2 (Analysis prefix) | `analysis_<context>_<kebab-topic>.md` | No analysis files existed prior to this document | N/A (new) |
| Conv. 2 (Communication prefix) | `comm_<SID>-<CODE>.md` | `comm_T102-RES-006_skills-retargeting-integration.md` | Conformant |
| Conv. 4 (Timeline Hierarchy) | `workspace/PH###/ST###/` | `workspace/plan/`, `workspace/communication/` (type-first) | Non-conformant |
| Conv. 8 (Archive Strategy) | Single `archive/` with mirrored structure | No archive directory | Non-conformant |

### B. File Naming Convention Application to New T103 Files

Per P-STD-004 Convention 2, new T103 artifacts should follow these naming patterns:

| Artifact Type | P-STD-004 Pattern | T103 Application |
|:--|:--|:--|
| Phase plan | `plan_T103-PH000.md` | Phase 0 plan (if created) |
| Stream plan | `plan_T103-PH000-ST###.md` | Stream plan for retargeting work |
| Analysis | `analysis_T103-PH000_<kebab-topic>.md` | This document |
| Notes | `notes_T103-PH000-ST###.md` | Stream notes (if created) |

### C. Migration Consideration

The existing T103 plan files (`plan_T103_adr-skills-system.md`, `plan_T103A1-ADRSS_phase3.md`) use legacy naming. A full workspace migration to P-STD-004 conventions could be scoped as part of this retargeting effort or deferred to a dedicated restructuring activity. Given that T104 itself has not yet migrated to timeline-organized workspace (that is planned for T104-PH001-ST007), it is pragmatic to:

1. **Apply P-STD-004 file naming conventions to all new files** created within T103
2. **Defer full workspace restructuring** (timeline hierarchy) until the program-level migration tooling from T104-PH001-ST007 is available
3. **Maintain existing files** in their current locations as grandfathered legacy artifacts

---

## VI. IMPACT ON T103 PHASE 3-4 PLANS

The existing Phase 3 plan (`plan_T103A1-ADRSS_phase3.md`) defines a multi-ADR selector skill (`t102-adr-rules-system`) that:

- Targets the Concept document for extraction
- Uses ADR-style naming throughout
- Assumes Concept contains ADR anchor markers

**Assessment**: Phase 3 as currently planned is **incompatible** with the T102-RES-006 retargeting. The Phase 3 plan must be either:
1. **Revised** to align with STD-based extraction from standards files, or
2. **Superseded** by a new plan that incorporates both the retargeting and the multi-STD selector concept

Phase 4 (Registry Generator) is outlined only and can be adapted without conflict.

---

## VII. SUMMARY OF FINDINGS

### Scope Dimensions

| Dimension | Count |
|:--|:--|
| Files requiring rename | 10 (scripts) + 3 (documentation) + 3 (skill directories) |
| Files requiring internal content changes | ~15+ (all scripts, SKILL.md files, documentation) |
| Python symbols requiring rename | 6+ (classes, constants, functions, imports) |
| Registry entries requiring update | 3 (all registered skills) |
| Distribution paths requiring update | 6 (3 Claude + 3 Codex) |
| Print scripts requiring behavioral change | 3 (retarget from Concept to STD files) |
| Extraction library requiring algorithm change | 1 (`adr_extraction.py` → `std_extraction.py`) |
| Existing plans requiring revision | 1 (`plan_T103A1-ADRSS_phase3.md`) |
| SKILL.md files requiring content update | 3 (all skills) |

### Recommended Execution Sequence

Per the T102 communication's recommended approach:

1. **Rename first** (ADR → STD): Mechanical rename of files, symbols, and references
2. **Retarget second**: Update extraction source paths and adapt extraction logic
3. **Verify third**: Run updated verification script against canonical standards files
4. **Update hooks fourth**: Ensure pre-commit hooks reference renamed scripts

### Critical Pre-Conditions

1. **GATE-003 approval**: T102-RES-006 Client sign-off should be confirmed before implementation
2. **Anchor verification**: Confirm that `{#t102-std-###-...}` anchors exist (or will be added) in target STD files
3. **Extraction format analysis**: Assess whether STD file structure supports the current anchor-based extraction algorithm or requires algorithmic changes

---

## VIII. REFERENCES

- `prompt/artifacts/tasks/T103/workspace/communication/comm_T102-RES-006_skills-retargeting-integration.md` (T102 integration communication)
- `prompt/artifacts/tasks/T103/workspace/plan/plan_T103_adr-skills-system.md` (T103 main plan, Phases 0-2)
- `prompt/artifacts/tasks/T103/workspace/plan/plan_T103A1-ADRSS_phase3.md` (T103 Phase 3 plan)
- `prompt/artifacts/tasks/T104/workspace/PH001/ST002/AC000/proposal/proposal_T104-PH001-ST002-AC000_directory-naming-convention.md` (P-STD-004 input)
- `prompt/artifacts/tasks/T102/consultant/standards/` (T102 canonical standards files)
- `prompt/scripts/skills/` (T103 shared infrastructure scripts)
- `prompt/skills/` (T103 skills SSOT directory)
- `prompt/documentation/adr_skills_catalog.md` (skills catalog)

---

## IX. PROVENANCE

- Source research conducted: 2026-02-12
- All T103 workspace files, scripts, skills, and documentation reviewed in full
- All T102 standards files (16 files) reviewed for context
- T104 P-STD-004 proposal (v3.0.0) reviewed for naming convention compliance
- T104 workspace plan directory reviewed as structural exemplar
