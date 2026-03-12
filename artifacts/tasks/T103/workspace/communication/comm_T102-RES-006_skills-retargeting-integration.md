---
artifact_type: 'COMMUNICATION'
from_initiative: 'T102'
from_stream: 'T102-PH001-ST004-AC003'
to_initiative: 'T103'
to_owner: 'T103 LLM_Consultant'
date: '2026-02-10'
subject: 'T102-RES-006 Integration Impact — ADR Skills System Retargeting to Standards Canonical Path'
priority: 'HIGH'
source_analysis: 'prompt/artifacts/tasks/T102/workspace/PH000/analysis/analysis_T102-RES-006_integration-impact.md'
source_report: 'prompt/artifacts/tasks/T102/research/T102-RES-006/report_T102-RES-006_concept-role-dynamic-registers.md'
---

# COMMUNICATION: T102 → T103 — Skills System Retargeting to Standards Canonical Path

## I. PURPOSE

This communication informs the **T103 initiative owner** of a critical integration requirement arising from `T102-RES-006` (Concept Role + Dynamic SSOT Registers) research findings. The finding directly impacts the T103 ADR Skills System architecture and requires the T103 owner to incorporate the following changes into their planning.

---

## II. BACKGROUND

### What Happened

During the T102 Phase 1 research program (`T102-PH001-ST004`), three research commissions were completed:

1. **T102-RES-004** (Issues & Risks Architecture) — established SPS-only I&R hosting
2. **T102-RES-005** (Cross-Scope Coordination Architecture) — established hybrid coordination with Concept as audit surface
3. **T102-RES-006** (Concept Role + Dynamic SSOT Registers) — defined Concept as a "hub-first with thresholds" architecture

### The Key Finding (RES-006, Topic 4 + Finding 5)

The research confirmed that:

- **ADR extraction tooling** (`prompt/scripts/skills/extract_adr.py`) currently targets `concept_T102-CONSULTANT.md` as the ADR extraction surface (`DEFAULT_CONCEPT_PATH`)
- This **currently fails**: `ERROR: ADR start marker not found: {#t102-adr-005-id-spec}` — Concept does not contain ADR anchor markers
- The research evaluated two resolution paths and **recommends Path B: retarget extraction to canonical standards files**

### Why Path B Is Recommended

| Criterion | Path A (Restore anchors in Concept) | Path B (Retarget to standards files) |
|:--|:--|:--|
| Drift risk | Higher — two sources to maintain (Concept + standards files) | Lower — single canonical source |
| Alignment with "link-don't-duplicate" | Lower — requires embedding ADR bodies/anchors in Concept | Higher — Concept links to standards; extraction reads from canonical source |
| Consistency with T102 Model D migration | Lower — contradicts STD-Contains-CLAUSE architecture | Higher — aligns with combined ADR+Spec files in `standards/` |

---

## III. REQUIRED CHANGES FOR T103 PLANNING

The following changes are recommended for the T103 ADR Skills System. The T103 owner should plan these as activities within their own phase/stream structure.

### Change 1: Rename "ADR" References to "STD" Throughout the Skills System

**Rationale**: T102 Phase 1 (ST001, completed 2026-02-08) executed a governance migration from ADR-centric to STD-Contains-CLAUSE architecture. ADR bodies now live inside combined standard files (`T102-STD-###`). The "ADR Skills" naming is now a legacy artifact.

**Scope of rename** (inventory of affected files):

| Current Name/Path | Proposed Name/Path | File Type |
|:--|:--|:--|
| `prompt/scripts/skills/extract_adr.py` | `prompt/scripts/skills/extract_std.py` | Script |
| `prompt/scripts/skills/adr_extraction.py` | `prompt/scripts/skills/std_extraction.py` | Module |
| `prompt/scripts/skills/adr_skills_registry.py` | `prompt/scripts/skills/std_skills_registry.py` | Registry |
| `prompt/scripts/skills/verify_adr_skills.py` | `prompt/scripts/skills/verify_std_skills.py` | Verification |
| `prompt/scripts/skills/install_adr_skills_pre_commit_hook.py` | `prompt/scripts/skills/install_std_skills_pre_commit_hook.py` | Hook installer |
| `prompt/documentation/scripts/skills/adr_skills_scripts_reference.md` | `prompt/documentation/scripts/skills/std_skills_scripts_reference.md` | Documentation |
| `prompt/documentation/scripts/skills/adr_skills_verification_runbook.md` | `prompt/documentation/scripts/skills/std_skills_verification_runbook.md` | Documentation |
| `AdrSkillSpec` (class name) | `StdSkillSpec` | Python class |
| `ADR_SKILLS` (registry constant) | `STD_SKILLS` | Python constant |

**Internal reference updates**: All `import adr_extraction`, `from adr_skills_registry import ...`, and docstring references to "ADR" should be updated to "STD" equivalents.

### Change 2: Retarget Extraction Source from Concept to Standards Canonical Path

**Rationale**: ADR/STD bodies now live in canonical combined files at `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-###_*.md`. Extraction should read from these files directly, not from Concept.

**Specific changes**:

| Component | Current Behavior | Required Behavior |
|:--|:--|:--|
| `DEFAULT_CONCEPT_PATH` in `extract_adr.py` | Points to `concept_T102-CONSULTANT.md` | **Remove** — replace with `DEFAULT_STD_DIR` pointing to `prompt/artifacts/tasks/T102/consultant/standards/` |
| `expected_anchor` in registry entries | Searches for anchor in Concept | Searches for anchor in the corresponding `T102-STD-###` file |
| `adr_id` field in registry | `ADR-005`, `ADR-004`, `ADR-007` | Update to `STD-005`, `STD-004`, `STD-007` (or keep backward-compatible alias) |
| Per-skill extraction scripts (`print_t102_adr_###.py`) | Target Concept | Target corresponding standards file in `prompt/artifacts/tasks/T102/consultant/standards/` |

**Registry entry mapping** (current → updated):

| Current `skill_name` | Current `adr_id` | Target STD File | Expected New Anchor Pattern |
|:--|:--|:--|:--|
| `t102-adr-005-id-spec` | `ADR-005` | `T102-STD-005_id-specification-rules.md` | `{#t102-std-005-id-spec}` |
| `t102-adr-004-drs-index` | `ADR-004` | `T102-STD-004_decision-records-index.md` | `{#t102-std-004-drs-index}` |
| `t102-adr-007-issues-risks-index` | `ADR-007` | `T102-STD-007_issues-risks-index.md` | `{#t102-std-007-issues-risks-index}` |

### Change 3: Update Skill Directory Names and Distribution Paths

| Current Path | Proposed Path |
|:--|:--|
| `prompt/skills/t102-adr-005-id-spec/` | `prompt/skills/t102-std-005-id-spec/` |
| `prompt/skills/t102-adr-004-drs-index/` | `prompt/skills/t102-std-004-drs-index/` |
| `prompt/skills/t102-adr-007-issues-risks-index/` | `prompt/skills/t102-std-007-issues-risks-index/` |
| `.claude/skills/t102-adr-*` (symlinks) | `.claude/skills/t102-std-*` |
| `.codex/skills/t102-adr-*` (mirrors) | `.codex/skills/t102-std-*` |

---

## IV. INTEGRATION DEPENDENCIES

| Dependency | Status | Notes |
|:--|:--|:--|
| T102 STD-Contains-CLAUSE migration (PH001-ST001-AC006) | `completed` (2026-02-08) | Combined standard files exist in canonical path |
| T102 STD migration rollout (PH001-ST003) | `completed` | All 16 STD files migrated to `prompt/artifacts/tasks/T102/consultant/standards/` |
| T102-RES-006 GATE-003 (Client sign-off on integration recommendations) | `pending` | This communication should be actioned after GATE-003 approval |

---

## V. RECOMMENDED APPROACH FOR T103

1. **Plan these changes as a dedicated activity** within the T103 plan — this is a significant refactoring that touches scripts, registries, skill directories, symlinks, mirrors, and documentation
2. **Execute rename before retargeting** — rename "ADR" → "STD" first (mechanical), then update extraction source paths (behavioral change)
3. **Verify extraction works against new paths** — run the updated verification script against each registered STD skill to confirm extraction succeeds from the canonical standards files
4. **Update pre-commit hooks** if installed — ensure the hook references the renamed scripts

---

## VI. CONTACT

For questions about the T102 standards architecture, canonical paths, or RES-006 findings, contact the **T102 Initiative LLM_Consultant** (ST004 research program owner).

**Reference materials**:
- Research report: `prompt/artifacts/tasks/T102/research/T102-RES-006/report_T102-RES-006_concept-role-dynamic-registers.md`
- Integration analysis: `prompt/artifacts/tasks/T102/workspace/PH000/analysis/analysis_T102-RES-006_integration-impact.md`
- Stream plan: `prompt/artifacts/tasks/T102/workspace/PH001/ST004/plan_T102-PH001-ST004.md`
