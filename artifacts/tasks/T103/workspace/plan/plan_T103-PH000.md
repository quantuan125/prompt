---
artifact_type: 'PLAN'
planning_level: 'PHASE'
initiative_id: 'T103'
phase: '0'
version: '1.0.0'
date: '2026-02-12'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
analysis_reference: 'prompt/artifacts/tasks/T103/workspace/analysis/analysis_T103-PH000_standards-retargeting-assessment.md'
source_communication: 'prompt/artifacts/tasks/T103/workspace/communication/comm_T102-RES-006_skills-retargeting-integration.md'
naming_convention: 'prompt/artifacts/tasks/T104/workspace/proposal/proposal_T104-PH001-ST002-AC000_directory-naming-convention.md'
legacy_plans:
  - 'prompt/artifacts/tasks/T103/workspace/plan/plan_T103_adr-skills-system.md'
  - 'prompt/artifacts/tasks/T103/workspace/plan/plan_T103A1-ADRSS_phase3.md'
---

# Plan: T103-PH000 — Standards Retargeting & Skills System Update

## I. EXECUTIVE SUMMARY

### Purpose

This phase plan establishes the high-level implementation structure for retargeting the T103 ADR Skills System to align with the T102 STD-Contains-CLAUSE architecture. It consolidates the T102-RES-006 integration requirements and P-STD-004 conformance updates into a structured stream/activity breakdown within the existing T103-PH000 scope.

### Objectives

1. Rename all "ADR" references to "STD" across the skills system (files, symbols, documentation)
2. Retarget extraction from Concept document to canonical standards files in `T102/consultant/standards/`
3. Update skill directory names, distribution paths, and registry entries
4. Update documentation and verification infrastructure
5. Verify end-to-end extraction against canonical standards files

### Entry Criteria

- [ ] T102-RES-006 GATE-003 Client sign-off confirmed (or explicit T103 owner approval to proceed)
- [ ] Anchor markers verified in target STD files (or anchor addition plan confirmed)
- [ ] Analysis document reviewed and approved (`analysis_T103-PH000_standards-retargeting-assessment.md`)

### Exit Milestone

All three registered skills extract successfully from canonical standards files; verification script passes; documentation updated.

### Locked Decisions

| # | Decision | Rationale |
|:--|:--|:--|
| DEC-001 | Execute rename (ADR → STD) before retargeting extraction paths | Per T102 communication §V recommendation; mechanical rename first, behavioral change second |
| DEC-002 | Apply P-STD-004 file naming to all new T103 files | Program-level convention compliance |
| DEC-003 | Defer full workspace restructuring (timeline hierarchy) | T104-PH001-ST007 tooling not yet available; grandfathered approach |

---

## II. CONTEXT MATERIALS & PREREQUISITES

### Source Documents

| Document | Path | Relevance |
|:--|:--|:--|
| T102 Communication | `T103/workspace/communication/comm_T102-RES-006_skills-retargeting-integration.md` | Defines required changes |
| T103 Analysis | `T103/workspace/analysis/analysis_T103-PH000_standards-retargeting-assessment.md` | Full impact assessment |
| T103 Main Plan (legacy) | `T103/workspace/plan/plan_T103_adr-skills-system.md` | Prior phase 0-2 plan (completed) |
| T103 Phase 3 Plan (legacy) | `T103/workspace/plan/plan_T103A1-ADRSS_phase3.md` | Requires revision post-retargeting |
| P-STD-004 Proposal | `T104/workspace/proposal/proposal_T104-PH001-ST002-AC000_directory-naming-convention.md` | Naming convention standard |

### Relationship to Legacy Plans

This phase plan supersedes the Phase 0-2 completion tracking in `plan_T103_adr-skills-system.md` for the purpose of the retargeting work. The legacy plan documents historical Phase 0-2 delivery and remains valid as a record. The Phase 3 plan (`plan_T103A1-ADRSS_phase3.md`) is impacted and should be revised after this retargeting work completes.

---

## III. PHASE ROADMAP

### Stream Register

| Stream | ID | Name | Status | Owner | Depends On | Deliverable |
|:--|:--|:--|:--|:--|:--|:--|
| ST001 | T103-PH000-ST001 | Pre-Implementation Verification | `planned` | LLM_Consultant | Entry Criteria | Anchor verification report; extraction format assessment |
| ST002 | T103-PH000-ST002 | ADR-to-STD Rename | `planned` | LLM_Developer | ST001 | All files, symbols, and references renamed |
| ST003 | T103-PH000-ST003 | Extraction Retargeting | `planned` | LLM_Developer | ST002 | Extraction reads from canonical STD files |
| ST004 | T103-PH000-ST004 | Verification & Validation | `planned` | LLM_Developer | ST003 | All skills extract and verify successfully |
| ST005 | T103-PH000-ST005 | Documentation Update | `planned` | LLM_Consultant | ST004 | All documentation reflects STD naming and paths |

### Stream Details

---

#### ST001: Pre-Implementation Verification

**Objective**: Confirm that the target standards files contain the required anchor markers and assess whether the extraction algorithm needs adaptation for the STD file format.

**Execution Mode**: SEQUENTIAL (must complete before ST002)

**Activities**:

| Activity | ID | Name | Status | Deliverable |
|:--|:--|:--|:--|:--|
| AC001 | T103-PH000-ST001-AC001 | Anchor Marker Audit | `planned` | Verification of `{#t102-std-###-...}` anchors in each target STD file |
| AC002 | T103-PH000-ST001-AC002 | Extraction Format Assessment | `planned` | Analysis of STD file structure vs. current extraction algorithm expectations |
| AC003 | T103-PH000-ST001-AC003 | GATE-003 Status Confirmation | `planned` | Confirmation of T102-RES-006 Client sign-off status |

**Success Criteria**:
- [ ] Anchors confirmed present (or addition plan documented) in all 3 target STD files
- [ ] Extraction algorithm impact assessed (no change / minor adaptation / major rewrite)
- [ ] GATE-003 status confirmed

**Risks**:
- STD files may lack anchors entirely, requiring coordination with T102 to add them
- STD file structure may not support anchor-based extraction, requiring algorithm redesign

---

#### ST002: ADR-to-STD Rename

**Objective**: Execute a mechanical rename of all "ADR" references to "STD" across files, symbols, imports, and documentation. No behavioral changes in this stream.

**Execution Mode**: SEQUENTIAL (rename infrastructure scripts first, then skill directories, then documentation)

**Depends On**: ST001 (all pre-conditions verified)

**Activities**:

| Activity | ID | Name | Status | Deliverable |
|:--|:--|:--|:--|:--|
| AC001 | T103-PH000-ST002-AC001 | Rename Shared Infrastructure Scripts | `planned` | 5 renamed files in `prompt/scripts/skills/` |
| AC002 | T103-PH000-ST002-AC002 | Rename Internal Symbols | `planned` | All Python class names, constants, functions, imports updated |
| AC003 | T103-PH000-ST002-AC003 | Rename Skill SSOT Directories | `planned` | 3 skill directories renamed from `t102-adr-*` to `t102-std-*` |
| AC004 | T103-PH000-ST002-AC004 | Rename Per-Skill Print Scripts | `planned` | 3 print scripts renamed from `print_t102_adr_*` to `print_t102_std_*` |
| AC005 | T103-PH000-ST002-AC005 | Update Registry Entries | `planned` | All 3 registry entries updated with STD naming |
| AC006 | T103-PH000-ST002-AC006 | Update SKILL.md Files | `planned` | All 3 SKILL.md files updated with STD references and script paths |
| AC007 | T103-PH000-ST002-AC007 | Smoke Test (Rename Only) | `planned` | Import resolution verified; all scripts loadable without errors |

**Scope of rename** (file inventory from analysis §IV.B):
- 10 file renames (scripts + documentation)
- 3 directory renames (skill SSOT directories)
- 3 per-skill script renames
- 6+ internal symbol renames (class, constant, function, imports)
- All cross-references in documentation files

**Success Criteria**:
- [ ] All files renamed per inventory in analysis document
- [ ] All Python imports resolve correctly after rename
- [ ] No references to "adr_extraction", "adr_skills_registry", or "AdrSkillSpec" remain
- [ ] Verification script loads without import errors (functional checks deferred to ST004)

---

#### ST003: Extraction Retargeting

**Objective**: Update the extraction source from Concept document to canonical standards files. This involves behavioral changes to the extraction logic.

**Execution Mode**: SEQUENTIAL

**Depends On**: ST002 (rename complete)

**Activities**:

| Activity | ID | Name | Status | Deliverable |
|:--|:--|:--|:--|:--|
| AC001 | T103-PH000-ST003-AC001 | Update Extraction Module | `planned` | `std_extraction.py` reads from STD files; `DEFAULT_STD_DIR` replaces `DEFAULT_CONCEPT_PATH` |
| AC002 | T103-PH000-ST003-AC002 | Update Per-Skill Print Scripts | `planned` | Each `print_t102_std_*.py` targets its corresponding STD file |
| AC003 | T103-PH000-ST003-AC003 | Update CLI Tool | `planned` | `extract_std.py` supports STD file targeting |
| AC004 | T103-PH000-ST003-AC004 | Update Registry Source Mappings | `planned` | Registry entries map skills to specific STD file paths |
| AC005 | T103-PH000-ST003-AC005 | Adapt Extraction Algorithm (if needed) | `planned` | Extraction logic handles STD file structure (per ST001-AC002 assessment) |

**Success Criteria**:
- [ ] Each print script extracts content from its target STD file
- [ ] `DEFAULT_STD_DIR` points to `prompt/artifacts/tasks/T102/consultant/standards/`
- [ ] No remaining references to `concept_T102-CONSULTANT.md` in extraction paths

---

#### ST004: Verification & Validation

**Objective**: Run end-to-end verification to confirm all skills extract and distribute correctly against the new STD-based architecture.

**Execution Mode**: SEQUENTIAL

**Depends On**: ST003 (retargeting complete)

**Activities**:

| Activity | ID | Name | Status | Deliverable |
|:--|:--|:--|:--|:--|
| AC001 | T103-PH000-ST004-AC001 | Run Updated Verification Script | `planned` | `verify_std_skills.py` passes all checks for all 3 skills |
| AC002 | T103-PH000-ST004-AC002 | Validate Extraction Output Quality | `planned` | Extracted content matches expected STD sections |
| AC003 | T103-PH000-ST004-AC003 | Validate Distribution Paths | `planned` | Claude symlinks and Codex mirrors functional with new paths |
| AC004 | T103-PH000-ST004-AC004 | Update Pre-Commit Hooks | `planned` | Hook references renamed scripts; hook installs and runs correctly |

**Success Criteria**:
- [ ] `verify_std_skills.py` exits with code 0 for all registered skills
- [ ] Extraction output for each skill contains expected standard content
- [ ] Claude symlinks resolve correctly (where applicable)
- [ ] Codex mirror sync completes without errors
- [ ] Pre-commit hook references updated scripts

---

#### ST005: Documentation Update

**Objective**: Update all documentation to reflect the STD-based architecture.

**Execution Mode**: Can run PARALLEL with ST004 for non-verification-dependent docs

**Depends On**: ST004 (verification passes)

**Activities**:

| Activity | ID | Name | Status | Deliverable |
|:--|:--|:--|:--|:--|
| AC001 | T103-PH000-ST005-AC001 | Update Skills Catalog | `planned` | `std_skills_catalog.md` reflects STD naming, paths, and extraction targets |
| AC002 | T103-PH000-ST005-AC002 | Update Scripts Reference | `planned` | `std_skills_scripts_reference.md` reflects all renamed scripts and new extraction paths |
| AC003 | T103-PH000-ST005-AC003 | Update Verification Runbook | `planned` | `std_skills_verification_runbook.md` reflects STD-based verification procedures |
| AC004 | T103-PH000-ST005-AC004 | Revise Phase 3 Plan | `planned` | `plan_T103A1-ADRSS_phase3.md` updated or superseded to align with STD architecture |

**Success Criteria**:
- [ ] All documentation files reference STD naming consistently
- [ ] No remaining "ADR" references in documentation (except historical/provenance contexts)
- [ ] Phase 3 plan revised to account for STD-based extraction

---

## IV. LINKS REGISTER

| # | Link Type | Source | Target | Notes |
|:--|:--|:--|:--|:--|
| L1 | Drives | `comm_T102-RES-006` | This plan | Communication defines required changes |
| L2 | Supports | `analysis_T103-PH000_standards-retargeting-assessment.md` | This plan | Analysis provides impact inventory |
| L3 | Constrains | `proposal_T104-PH001-ST002-AC000_directory-naming-convention.md` | New T103 files | Naming convention compliance |
| L4 | Supersedes (partial) | This plan | `plan_T103_adr-skills-system.md` | For retargeting scope only; legacy plan remains as historical record |
| L5 | Impacts | This plan | `plan_T103A1-ADRSS_phase3.md` | Phase 3 must be revised post-retargeting |
| L6 | Depends On | ST001-AC003 | T102-RES-006 GATE-003 | External dependency |

---

## V. OPEN QUESTIONS REGISTER

| # | Question | Owner | Status | Resolution |
|:--|:--|:--|:--|:--|
| OQ-001 | Do target STD files contain `{#t102-std-###-...}` anchor markers? | LLM_Consultant | `open` | To be verified in ST001-AC001 |
| OQ-002 | Does the combined STD file structure require extraction algorithm changes? | LLM_Developer | `open` | To be assessed in ST001-AC002 |
| OQ-003 | Is T102-RES-006 GATE-003 approved? | T102 Owner | `open` | External dependency; to be confirmed in ST001-AC003 |
| OQ-004 | Should Phase 3 be revised or superseded by a new plan? | T103 Owner (Client) | `open` | Decision needed after retargeting completes |
| OQ-005 | Should T103 adopt full timeline workspace hierarchy or defer to program tooling? | T103 Owner (Client) | `open` | Current recommendation: defer per DEC-003 |

---

## VI. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-02-12 | Initial | Initial phase plan for T103-PH000 standards retargeting; 5 streams defined (Pre-Implementation Verification, ADR-to-STD Rename, Extraction Retargeting, Verification & Validation, Documentation Update); grounded in T103 analysis and T102-RES-006 communication |
