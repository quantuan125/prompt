# T102 ADR Skills Catalog

## Overview

Skills extracted from T102 Concept ADRs for automated governance compliance enforcement in prompt artifacts.

## Purpose

This catalog documents ADR-based skills, their triggering conditions, scope, distribution architecture, and maintenance procedures.

## Active Skills

### t102-std-005-id-spec

**Source STD:** P-STD-005 (Universal ID Specification)  
**SSOT Location:** `prompt/skills/t102-adr-005-id-spec/`  
**Claude Code Location:** `.claude/skills/t102-adr-005-id-spec` (symlink)  
**Codex Location:** `.codex/skills/t102-adr-005-id-spec` (mirror directory; maintained by sync script)  
**Status:** Deprecated (directory retained for backward compatibility)

**Purpose:** Enforce RID construction and referencing rules per P-STD-005

**Scope:** Files under `prompt/**` directory only

**Auto-triggers on:**
- RID construction (creating new I-RID, E-RID, F-RID, S-RID)
- RID validation (checking existing RIDs)
- RID referencing (formal/informal references)
- Category token usage (ASSUM, CON, QG, DEP, FR, NFR, IG, INT, NOTE, RES, ISSUE, RISK, IF)

**Manual trigger:** Mention "RID" or any category token while operating in `prompt/**` context

**What it does:**
- Uses `P-STD-005` as the authoritative surface for RID construction and referencing rules
- Validates category tokens and ID construction shape: `{SCOPE_ID}-{CATEGORY}-{NNN}`
- Enforces formal references using back-ticked `ID (Title)` tokens
- Blocks prohibited downstream references (precedence/directionality rules)

**Maintenance:**
- **SSOT:** `prompt/skills/t102-adr-005-id-spec/SKILL.md`
- **Script (legacy):** `prompt/skills/t102-adr-005-id-spec/scripts/print_t102_adr_005.py`
- **Codex Mirror Sync:** `prompt/skills/t102-adr-005-id-spec/scripts/sync_to_codex_mirror.py`
- **Updates:** Edit SSOT, then run the sync script to refresh the Codex mirror
- **Testing:** Re-run the skill verification script after updates

**Verification (current):**
- Runbook: `prompt/documentation/scripts/skills/adr_skills_verification_runbook.md`
- Script reference: `prompt/documentation/scripts/skills/adr_skills_scripts_reference.md`
- Entrypoint: `python3 prompt/scripts/skills/verify_adr_skills.py`

### t102-std-004-drs-index

**Source ADR:** T102-STD-004 (Decision Records Index)  
**SSOT Location:** `prompt/skills/t102-std-004-drs-index/`  
**Claude Code Location:** `.claude/skills/t102-std-004-drs-index` (symlink)  
**Codex Location:** `.codex/skills/t102-std-004-drs-index` (mirror directory; maintained by sync script)  
**Status:** Active

**Purpose:** Apply the normative DR Index schema + DR body requirements per T102-STD-004

**Scope:** Files under `prompt/**` directory only

**Auto-triggers on:**
- Creating/updating Decision Records Index tables (GDR/ADR index schema)
- Creating/updating Decision Record body sections (required headings, anchors)
- Cross-artifact linking patterns (adoption statements / authority citations)

**Manual trigger:** Mention "ADR-004", "Decision Records Index", "DR Index", or "DR body" while operating in `prompt/**` context

**What it does (procedural; SSOT-first):**
- Runs extraction script to load the latest ADR-004 block (only) from the Concept document
- Treats the printed ADR-004 output as normative (no paraphrase)
- When ADR-004 requires RID-style formal references governed by ADR-005, explicitly invokes the ADR-005 skill workflow (print ADR-005 and apply its rules)

**Maintenance:**
- **SSOT:** `prompt/skills/t102-std-004-drs-index/SKILL.md`
- **Script:** `prompt/skills/t102-std-004-drs-index/scripts/print_t102_adr_004.py`
- **Codex Mirror Sync:** `prompt/skills/t102-std-004-drs-index/scripts/sync_to_codex_mirror.py`
- **Updates:** Edit SSOT, then run the sync script to refresh the Codex mirror

**Verification (current):**
- Runbook: `prompt/documentation/scripts/skills/adr_skills_verification_runbook.md`
- Script reference: `prompt/documentation/scripts/skills/adr_skills_scripts_reference.md`
- Entrypoint: `python3 prompt/scripts/skills/verify_adr_skills.py`

### t102-std-007-issues-risks-index

**Source ADR:** T102-STD-007 (Issues & Risks Index)  
**SSOT Location:** `prompt/skills/t102-std-007-issues-risks-index/`  
**Claude Code Location:** `.claude/skills/t102-std-007-issues-risks-index` (symlink)  
**Codex Location:** `.codex/skills/t102-std-007-issues-risks-index` (mirror directory; maintained by sync script)  
**Status:** Active

**Purpose:** Apply the normative Issues & Risks section/table standard per T102-STD-007

**Scope:** Files under `prompt/**` directory only

**Auto-triggers on:**
- Creating/updating an “Issues & Risks” section in a `prompt/**` artifact
- Creating/updating Issues or Risks tables (schema, enums, and closure requirements)
- Cross-scope promotion/de-duplication of issues/risks

**Manual trigger:** Mention "ADR-007", "Issues & Risks", "Issues table", or "Risks table" while operating in `prompt/**` context

**What it does (procedural; SSOT-first):**
- Runs extraction script to load the latest ADR-007 block (only) from the Concept document
- Treats the printed ADR-007 output as normative (no paraphrase)
- When ADR-007 requires ID construction or RID formal references governed by ADR-005 (e.g., `ISSUE` / `RISK` IDs), explicitly invokes the ADR-005 skill workflow (print ADR-005 and apply its rules)

**Maintenance:**
- **SSOT:** `prompt/skills/t102-std-007-issues-risks-index/SKILL.md`
- **Script:** `prompt/skills/t102-std-007-issues-risks-index/scripts/print_t102_adr_007.py`
- **Codex Mirror Sync:** `prompt/skills/t102-std-007-issues-risks-index/scripts/sync_to_codex_mirror.py`
- **Updates:** Edit SSOT, then run the sync script to refresh the Codex mirror

**Verification (current):**
- Runbook: `prompt/documentation/scripts/skills/adr_skills_verification_runbook.md`
- Script reference: `prompt/documentation/scripts/skills/adr_skills_scripts_reference.md`
- Entrypoint: `python3 prompt/scripts/skills/verify_adr_skills.py`

## Planned Skills

### Candidates

| Skill Name | Source ADR | Priority | Status | Rationale |
|------------|------------|----------|--------|-----------|
| `t102-std-003-inheritance` | T102-STD-003 | Low | Planned | Enforce Explicit Inheritance Model (Inherited Considerations tables) |
| `t102-std-002-yaml-header` | T102-STD-002 | Low | Planned | Validate Canonical YAML Header (schema, format, conformance) |

---

## SSOT Architecture

**Source Location (SSOT):** `prompt/skills/`  
**Distribution:** 
- Claude Code uses symlinks from `.claude/skills/` to `prompt/skills/`
- Codex uses a mirror directory under `.codex/skills/` maintained by the sync script
**Rationale:** Maintain once, consume everywhere (link for Claude, mirror for Codex)

**Maintenance Workflow:**
1. Edit SSOT file in `prompt/skills/[skill-name]/SKILL.md`
2. Run sync script to refresh the Codex mirror
3. Claude Code reads via symlink; Codex reads via mirror
4. Restart Claude Code / reload Codex session as needed
5. Validate extraction scripts after Concept formatting changes
