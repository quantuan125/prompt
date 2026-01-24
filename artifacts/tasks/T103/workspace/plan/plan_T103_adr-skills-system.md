---
artifact_type: 'PLAN'
initiative_id: 'T102'
epic_id: 'T102-SKILLS'
version: '1.0.0'
date: '2026-01-02'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
---

# PLAN: T103 ADR Skills System — Claude Code Conversion & Expansion

## I. EXECUTIVE SUMMARY

This plan defines the conversion of existing Codex skill `t102-adr-005-id-spec` to a shared SSOT and establishes a scalable ADR skills system so **both Claude Code and Codex** enforce the same T102 governance across prompt artifacts.

**SSOT file**: `prompt/skills/t102-adr-005-id-spec/` (SSOT location)
**Distribution (Claude Code)**: `.claude/skills/t102-adr-005-id-spec` (symlink → SSOT)
**Distribution (Codex CLI)**: `.codex/skills/t102-adr-005-id-spec` (direct directory mirror of SSOT; see Activity 0.6)
**Existing source**: `.codex/skills/t102-adr-005-id-spec/` (preserve by renaming to legacy before Codex mirror install)

**Role boundary**
- `LLM_Consultant`: Requirements analysis, plan development, architectural guidance
- `LLM_Developer`: Implementation of skill conversion, file operations, testing
- `Client`: Decision owner and approval authority

**Phasing intent**
- **Phase 0**: Establish SSOT and symlink distribution for **Claude Code + Codex**; establish ADR Skills Catalog foundation
- **Phase 1** (future): Expand system with additional ADR skills (ADR-007, ADR-004, ADR-003, ADR-002)
- **Phase 2** (future): Generalize extraction script for multi-ADR support

---

## II. CONTEXT MATERIALS & PREREQUISITES

### A. Required Reading Before Implementation

**Initiative Governance**:
- `prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md` — T102-ADR-005 (ID Specification & Rules) source
- `documentation/general.md` — Master governance document

**Existing Implementation** (Codex version):
- `.codex/skills/t102-adr-005-id-spec/SKILL.md` — Current skill content
- `.codex/skills/t102-adr-005-id-spec/scripts/print_t102_adr_005.py` — Extraction script

**Claude Code Skills Documentation**:
- https://code.claude.com/docs/en/skills — Official skills documentation
- Superpowers writing-skills framework: `~/.claude/plugins/cache/superpowers-marketplace/superpowers/4.0.3/skills/writing-skills/SKILL.md`

**Plan Exemplar** (structure reference):
- `prompt/artifacts/tasks/T801/consultant/workspace/plan/plan_T801A_phase0-1.md` — Planning document structural template

### B. Working Assumptions

1. **SSOT Architecture**: `prompt/skills/` serves as single source of truth; Claude Code receives via symlink; Codex CLI uses a directory mirror (temporary)
2. **Codex Preservation**: Existing `.codex/skills/t102-adr-005-id-spec/` is preserved by renaming to a legacy copy before installing the SSOT-backed Codex directory
3. **Project Scope**: Skill operates at project level (`.claude/skills/`) for team-wide governance enforcement
4. **Extraction Script Stability**: `print_t102_adr_005.py` requires no modifications; only path references change
5. **Catalog Foundation**: ADR Skills Catalog created in Phase 0 with extensibility for future ADR skills

### C. Key Design Decisions

**SSOT Location**: `prompt/skills/` chosen to:
- Align with prompt artifact governance scope
- Maintain proximity to source concept document
- Enable future ADR skills co-location
- Separate from tool-specific directories (`.claude/`, `.codex/`)

**Symlink Strategy (Claude Code)**: One-way symlink distribution from `.claude/skills/` to `prompt/skills/`:
- Avoids duplication
- Maintains single maintenance point
- Works on WSL/Linux environments
- Git tracks symlinks via `.gitattributes`

**Codex Integration (Known Limitation + Temporary Adapter)**:
- Codex CLI skill discovery is known to not reliably follow directory symlinks under `.codex/skills/`.
- Phase 0 therefore uses a **Codex mirror directory** (copy-based) that is kept in sync with SSOT via a local script (Activity 0.6).

---

## III. PHASE 0: ADR-005 SKILL CONVERSION (IMMEDIATE)

**Objective**: Convert existing Codex `t102-adr-005-id-spec` skill to a shared SSOT with Claude Code symlink distribution and a Codex mirror adapter, establish ADR Skills Catalog, and validate functionality.

**Constraint**: Phase 0 MUST preserve existing `.codex/skills/t102-adr-005-id-spec/` by renaming to a legacy copy prior to installing the SSOT-backed Codex mirror directory.

### Phase 0 Activities

#### Activity 0.1: SSOT Establishment

**Purpose**: Create SSOT location and populate with Codex skill content

##### Task 0.1.1: Create SSOT directory structure
```bash
mkdir -p prompt/skills/t102-adr-005-id-spec/scripts
```

##### Task 0.1.2: Copy skill content to SSOT
**Source**: `.codex/skills/t102-adr-005-id-spec/`
**Destination**: `prompt/skills/t102-adr-005-id-spec/`

Copy:
- `SKILL.md` → `prompt/skills/t102-adr-005-id-spec/SKILL.md`
- `scripts/print_t102_adr_005.py` → `prompt/skills/t102-adr-005-id-spec/scripts/print_t102_adr_005.py`

**Verification**:
- [ ] SSOT directory exists with correct structure
- [ ] Both files copied successfully
- [ ] File permissions preserved (script executable)

---

#### Activity 0.2: Claude Code + Codex Adaptation

**Purpose**: Update SSOT `SKILL.md` for Claude Code compatibility, keep Codex compatibility, and add `allowed-tools` optimization

##### Task 0.2.1: Update script path reference in SSOT SKILL.md

**File**: `prompt/skills/t102-adr-005-id-spec/SKILL.md`

**Line 27 change**:
```diff
- `python .codex/skills/t102-adr-005-id-spec/scripts/print_t102_adr_005.py`
+ `python3 prompt/skills/t102-adr-005-id-spec/scripts/print_t102_adr_005.py`
```

##### Task 0.2.2: Add allowed-tools to YAML frontmatter

**File**: `prompt/skills/t102-adr-005-id-spec/SKILL.md`

**Frontmatter update**:
```yaml
---
name: t102-adr-005-id-spec
description: Use when working with files under prompt/ and you need to construct, validate, or reference RIDs (I-RID, E-RID, F-RID, S-RID) governed by T102-ADR-005, including category tokens (ASSUM, CON, QG, DEP, NOTE, RES, ISSUE, RISK, IF, FR, NFR, IG, INT) and formal reference formatting.
allowed-tools: Bash, Read, Grep, Glob
---
```

**Benefit**: Claude won't ask permission to run extraction script or read files.

**Verification**:
- [ ] Script path updated to `prompt/skills/...`
- [ ] `allowed-tools` field added to frontmatter
- [ ] YAML syntax valid (spaces, not tabs)

---

#### Activity 0.3: Symlink Creation (Claude Code)

**Purpose**: Create one-way symlink from Claude Code skills directory to SSOT

##### Task 0.3.1: Create symlink
```bash
ln -s ../../prompt/skills/t102-adr-005-id-spec .claude/skills/t102-adr-005-id-spec
```

##### Task 0.3.2: Configure Git for symlink tracking

**File**: `.gitattributes`

**Add**:
```
*.md text
.claude/skills/** symlink
```

**Verification**:
- [ ] Symlink created successfully
- [ ] `ls -la .claude/skills/t102-adr-005-id-spec` shows symlink → `../../prompt/skills/t102-adr-005-id-spec`
- [ ] `.gitattributes` configured for symlink tracking

---

#### Activity 0.4: Functional Testing

**Purpose**: Verify skill triggers correctly and extraction script works from new path

##### Task 0.4.1: Test extraction script
```bash
python3 prompt/skills/t102-adr-005-id-spec/scripts/print_t102_adr_005.py | head -20
```

**Expected output**: T102-ADR-005 block from concept document (starting with anchor `{#t102-adr-005-id-spec}`)

##### Task 0.4.2: Test skill discovery

**Action**: Restart Claude Code and verify skill appears in available skills list

**Expected**: Skill `t102-adr-005-id-spec` discoverable via description keywords (RID, ASSUM, CON, QG, etc.)

##### Task 0.4.3: Test skill triggering

**Test scenarios**:
1. **Trigger test**: Ask Claude to create a new RID in `prompt/artifacts/...`
   - Expected: Skill auto-triggers, runs script, extracts ADR-005

2. **Scope gate test**: Ask Claude to create RID in non-`prompt/` file
   - Expected: Skill stops and asks for confirmation

3. **Category token test**: Ask Claude to use invalid category (e.g., `REQ`)
   - Expected: Skill prevents and suggests valid token (e.g., `FR`)

4. **Reference format test**: Ask Claude to add formal reference
   - Expected: Uses backticked `ID (Title)` format

**Verification checklist**:
- [ ] Extraction script runs successfully from new path
- [ ] Skill appears in Claude Code skills list after restart
- [ ] Skill auto-triggers on RID work in `prompt/**`
- [ ] Scope gate prevents work outside `prompt/` directory
- [ ] Category token validation works correctly
- [ ] Reference formatting enforced

---

#### Activity 0.5: ADR Skills Catalog Creation

**Purpose**: Create catalog foundation for current and future ADR skills

##### Task 0.5.1: Create catalog file

**File**: `prompt/documentation/adr_skills_catalog.md`

**Content structure**:
```markdown
# T102 ADR Skills Catalog

## Overview
Skills extracted from T102 Concept ADRs for automated governance compliance enforcement in prompt artifacts.

## Purpose
This catalog documents all ADR-based skills, their triggering conditions, scope, and maintenance procedures.

## Active Skills

### t102-adr-005-id-spec

**Source ADR:** T102-ADR-005 (ID Specification & Rules)
**SSOT Location:** `prompt/skills/t102-adr-005-id-spec/`
**Claude Code Location:** `.claude/skills/t102-adr-005-id-spec` (symlink)
**Status:** Active

**Purpose:** Enforce RID construction and referencing rules per T102-ADR-005

**Scope:** Files under `prompt/**` directory only

**Auto-triggers on:**
- RID construction (creating new I-RID, E-RID, F-RID, S-RID)
- RID validation (checking existing RIDs)
- RID referencing (formal/informal references)
- Category token usage (ASSUM, CON, QG, DEP, FR, NFR, IG, INT, NOTE, RES, ISSUE, RISK, IF)

**Manual trigger:** Mention "RID" or any category token in prompt

**What it does:**
- Runs extraction script to get latest ADR-005 rules
- Validates category tokens per scope (I/E/F/S)
- Enforces ID construction pattern: `{SCOPE_ID}-{CATEGORY}-{NNN}`
- Ensures formal references use backticked `ID (Title)` format
- Blocks prohibited downstream references (precedence/directionality rules)

**Maintenance:**
- **SSOT:** `prompt/skills/t102-adr-005-id-spec/SKILL.md`
- **Script:** `prompt/skills/t102-adr-005-id-spec/scripts/print_t102_adr_005.py`
- **Updates:** Skill auto-reads latest ADR-005 from concept document; no manual sync needed
- **Testing:** Verify extraction script after concept document structural changes

**Last Updated:** 2026-01-02
**Version:** 1.0.0

---

## Planned Skills

### Phase 1 Candidates

| Skill Name | Source ADR | Priority | Status | Rationale |
|------------|------------|----------|--------|-----------|
| `t102-adr-007-issues-risks-index` | T102-ADR-007 | High | Planned | Enforce Issues & Risks Log Standard (schema, enums, resolution notes) |
| `t102-adr-004-drs-index` | T102-ADR-004 | Medium | Planned | Enforce Decision Records Index (GDR/ADR schema, body format, placement) |
| `t102-adr-003-inheritance` | T102-ADR-003 | Low | Planned | Enforce Explicit Inheritance Model (Inherited Considerations tables) |
| `t102-adr-002-yaml-header` | T102-ADR-002 | Low | Planned | Validate Canonical YAML Header (schema, format, conformance) |

**Note**: Priority based on:
- **High**: Recently added ADRs with immediate governance value (ADR-007)
- **Medium**: Foundational standards with clear validation rules (ADR-004)
- **Low**: Established patterns with lower violation risk (ADR-003, ADR-002)

### Phase 2 Enhancements

| Enhancement | Description | Status |
|-------------|-------------|--------|
| **Generalized extraction script** | Refactor `print_t102_adr_005.py` → `extract_adr.py --adr=T102-ADR-###` for reusability | Planned |
| **Codex mirror adapter (temporary)** | Maintain Codex-discoverable directory under `.codex/skills/` via SSOT → mirror sync script (see Activity 0.6) | Included (Phase 0) |
| **Codex symlink support (future)** | Replace mirror with symlink only when Codex CLI skill discovery reliably follows directory symlinks | Deferred |
| **Documentation integration** | Reference catalog in `documentation/general.md` and `prompt/documentation/prompt_main.md` | Deferred |

---

## Skill Development Workflow

When creating new ADR-based skills (follow Superpowers writing-skills TDD methodology):

### 1. RED Phase: Baseline Testing
- Create pressure scenarios WITHOUT skill
- Document exact agent violations (verbatim rationalizations)
- Identify patterns in failures

### 2. GREEN Phase: Minimal Skill Creation
- Write skill addressing specific baseline failures
- Design extraction script (if needed for token efficiency)
- Test skill with same scenarios
- Verify agent compliance

### 3. REFACTOR Phase: Close Loopholes
- Identify new rationalizations from testing
- Add explicit counters
- Build rationalization table
- Re-test until bulletproof

### 4. Documentation
- Update this catalog (Active Skills table)
- Document triggering conditions, scope, maintenance
- Add version and last-updated date

### 5. Deployment
- Place in SSOT location (`prompt/skills/[skill-name]/`)
- Create symlink to `.claude/skills/[skill-name]`
- Configure Git for symlink tracking
- Restart Claude Code for discovery

---

## SSOT Architecture

**Current Strategy:** Symlink SSOT (Option B from consultation)

**Source Location:** `prompt/skills/` (single source of truth)
**Distribution (Claude Code):** Symlinks from `.claude/skills/` to `prompt/skills/`  
**Distribution (Codex CLI):** SSOT mirror directories under `.codex/skills/` maintained by a local sync script (Activity 0.6)
**Git Handling:** Configured via `.gitattributes` for symlink tracking

**Rationale:**
- True SSOT (one file, many references)
- Zero duplication
- Maintain once, works everywhere
- Aligns with "link-don't-duplicate" principle per T102-ADR-003

**Maintenance Workflow:**
1. Edit SSOT file in `prompt/skills/[skill-name]/SKILL.md`
2. Changes automatically reflected via symlinks
3. Restart Claude Code to load updated content
4. Test functionality after updates

**Migration Notes:**
- Existing Codex skill (`.codex/skills/t102-adr-005-id-spec/`) preserved for reference
- Codex mirror adapter included in Phase 0 (temporary); symlink discovery is a known Codex limitation
- Future ADR skills follow same SSOT pattern

---

## References

- **Writing Skills Methodology**: `~/.claude/plugins/cache/superpowers-marketplace/superpowers/4.0.3/skills/writing-skills/SKILL.md`

- **Claude Code Skills Documentation**: https://code.claude.com/docs/en/skills
- **Codex Skills Documentation**: https://developers.openai.com/codex/skills/

- **T102 Concept Document**: `prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT_v*.md`
- **T102-ADR-005**: ID Specification & Rules (RID governance)
- **T102-ADR-003**: Explicit Inheritance Model ("link-don't-duplicate" principle)
```

**Verification**:
- [ ] Catalog file created at correct location
- [ ] Active Skills section documents t102-adr-005-id-spec completely
- [ ] Planned Skills tables populated with Phase 1/2 candidates
- [ ] Skill Development Workflow documented
- [ ] SSOT Architecture documented

---

#### Activity 0.6: Codex CLI Compatibility Adapter (Temporary)

**Purpose**: Ensure Codex CLI reliably discovers the ADR skill even when it does not follow directory symlinks under `.codex/skills/`.

**Approach (temporary)**: Maintain SSOT at `prompt/skills/…` and keep a **mirror copy** under `.codex/skills/t102-adr-005-id-spec/` using a local sync script.

##### Task 0.6.1: Restore Codex skill directory name (from legacy)

**Goal**: Ensure the Codex-discoverable directory is named `t102-adr-005-id-spec`.

**Steps**:
1. If `.codex/skills/t102-adr-005-id-spec` is a symlink, remove it.
2. Rename `.codex/skills/t102-adr-005-id-spec-legacy` → `.codex/skills/t102-adr-005-id-spec`.

**Verification**:
- [ ] `.codex/skills/t102-adr-005-id-spec/` exists as a real directory (not a symlink)
- [ ] `SKILL.md` exists inside that directory

##### Task 0.6.2: Add sync script (SSOT → Codex mirror)

**Goal**: Provide a deterministic, local way to keep Codex mirror content consistent with SSOT.

**Script location (recommended)**:
- `prompt/skills/t102-adr-005-id-spec/scripts/sync_to_codex_mirror.py`

**Script responsibilities**:
- Copy `prompt/skills/t102-adr-005-id-spec/SKILL.md` → `.codex/skills/t102-adr-005-id-spec/SKILL.md`
- Copy `prompt/skills/t102-adr-005-id-spec/scripts/print_t102_adr_005.py` → `.codex/skills/t102-adr-005-id-spec/scripts/print_t102_adr_005.py`
- Create destination folders if missing
- Optional safety: refuse to overwrite if destination is a symlink; emit clear errors

**Verification**:
- [ ] Running the script updates the Codex mirror files
- [ ] A diff between SSOT and mirror is empty after sync

##### Task 0.6.3: Define operational workflow (when to run sync)

**Workflow**:
- After any SSOT changes under `prompt/skills/t102-adr-005-id-spec/`, run the sync script.

**Verification**:
- [ ] Workflow documented (Activity 0.6.4) and repeatable

#### Activity 0.7: Phase 0 Verification & Sign-off 

**Goal**: Close Phase 0 by verifying all items in **“### Phase 0 Success Criteria (Checklist)”**, with special emphasis on the **Codex mirror sync script**, and then updating the ADR skills catalog so the system is maintainable.

**Reporting rule (source of truth)**:
- During Activity 0.7 implementation, the agent MUST mark items in **“### Phase 0 Success Criteria (Checklist)”** as follows:
  - Check the box (`[x]`) when the corresponding verification passes.
  - Leave unchecked (`[ ]`) when the verification fails or is blocked.
- Do not add PASS/FAIL notes into the plan file beyond the checkbox state.
- The agent’s final response (outside the plan file) MUST summarize any unchecked checklist items and the reason (failed verification vs manual pending).

##### Task 0.7.1: Verify SSOT structure (filesystem-level)

Run:
```bash
ls -la prompt/skills/t102-adr-005-id-spec prompt/skills/t102-adr-005-id-spec/scripts
```
PASS looks like:
- `prompt/skills/t102-adr-005-id-spec/SKILL.md` exists
- `prompt/skills/t102-adr-005-id-spec/scripts/print_t102_adr_005.py` exists
- `prompt/skills/t102-adr-005-id-spec/scripts/sync_to_codex_mirror.py` exists

##### Task 0.7.2: Verify Claude distribution (symlink)

Run:
```bash
ls -la .claude/skills/t102-adr-005-id-spec
```
PASS looks like:
- `.claude/skills/t102-adr-005-id-spec` is a symlink → `../../prompt/skills/t102-adr-005-id-spec`

##### Task 0.7.3: Verify ADR-005 extraction correctness (functional)

Run (avoid writing `__pycache__`):
```bash
python3 -B prompt/skills/t102-adr-005-id-spec/scripts/print_t102_adr_005.py | head -n 20
python3 -B prompt/skills/t102-adr-005-id-spec/scripts/print_t102_adr_005.py | rg -n "{#t102-adr-005-id-spec}"
python3 -B prompt/skills/t102-adr-005-id-spec/scripts/print_t102_adr_005.py | rg -n "^\\* \\*\\*T102-ADR-006" && exit 1 || echo "PASS: no ADR-006 header in output"
```
PASS looks like:
- Output contains `{#t102-adr-005-id-spec}`
- Output does **not** include the next ADR header (proves extraction is ADR‑005 only)

##### Task 0.7.4: Verify Codex distribution (mirror directory; not a symlink)

Run:
```bash
test -d .codex/skills/t102-adr-005-id-spec && test ! -L .codex/skills/t102-adr-005-id-spec && echo "PASS: Codex mirror is a real directory"
ls -la .codex/skills/t102-adr-005-id-spec
```
PASS looks like:
- `.codex/skills/t102-adr-005-id-spec/` exists as a real directory
- `SKILL.md` and `scripts/` exist under the mirror directory

##### Task 0.7.5: Verify Codex mirror sync script (required; includes drift demonstration)

**A) Baseline (no drift)**

Run:
```bash
python3 -B prompt/skills/t102-adr-005-id-spec/scripts/sync_to_codex_mirror.py --check
```
PASS looks like:
- Exit code `0`
- Output contains `Mirror matches SSOT.`

**B) Drift demonstration (required)**

Create drift by editing the **Codex mirror** (not SSOT), then prove the sync script detects and fixes it.

Run:
```bash
printf "\n# DRIFT_TEST: do not commit\n" >> .codex/skills/t102-adr-005-id-spec/SKILL.md
python3 -B prompt/skills/t102-adr-005-id-spec/scripts/sync_to_codex_mirror.py --check && exit 1 || echo "PASS: drift detected"
python3 -B prompt/skills/t102-adr-005-id-spec/scripts/sync_to_codex_mirror.py
python3 -B prompt/skills/t102-adr-005-id-spec/scripts/sync_to_codex_mirror.py --check
```
PASS looks like:
- `--check` fails when drift exists (non-zero)
- Running sync rewrites mirror and restores parity
- `--check` succeeds again after sync

##### Task 0.7.6: Manual discovery checks (required; performed by Client)

**Instruction (explicit)**: The two “Manual Discovery Confirmed” items in **“### Phase 0 Success Criteria (Checklist)”** are checked by the Client only. The agent MUST leave them unchecked until the Client confirms PASS.
1) **Claude Code discovery**

   - Action: Restart Claude Code; confirm `t102-adr-005-id-spec` appears in available skills.
   - PASS looks like: Skill is discoverable by name/description.

2) **Codex CLI discovery**
   - Action: Restart/reload Codex; confirm `t102-adr-005-id-spec` appears in the Codex skills list.
   - PASS looks like: Skill is discoverable and usable in Codex.

##### Task 0.7.7: Update ADR Skills Catalog (required)

Update `prompt/documentation/adr_skills_catalog.md` to:
- Document **Claude Code** distribution as a symlink to SSOT
- Document **Codex** distribution as a **mirror directory** maintained by `sync_to_codex_mirror.py` (not a symlink)
- Include the exact verification commands and PASS criteria from Tasks 0.7.1–0.7.6

#### Activity 0.8: ADR Skills Verification System + Script Documentation

**Goal**: Extend Phase 0 so the ADR Skills System has a dedicated, human-friendly verification system (not embedded inside the catalog), document scripts for human operation, and add **commit-time enforcement** so Codex mirror drift cannot land unnoticed.

**Scope (Phase 0)**:
- Covers `t102-adr-005-id-spec` only.
- **Explicit Phase 1 requirement**: Generalize this verification system to support additional ADR skills (ADR‑007/004/etc.) via a registry/pattern.

##### Task 0.8.1: Create dedicated verification runbook (human-friendly)

**Location**: `prompt/documentation/scripts/skills/`

**Deliverable**: Add an ADR skills verification runbook that explains:
- What “passing Phase 0” means (conceptual overview)
- What to run (single entrypoint) and what PASS looks like
- What is automated vs manual (e.g., discovery checks by Client)
- Where the SSOT lives and how distribution works (Claude symlink, Codex mirror)

##### Task 0.8.2: Create scripts-specific documentation (human usage)

**Location**: `prompt/documentation/scripts/skills/`

Document human-operable usage for:
- `prompt/skills/t102-adr-005-id-spec/scripts/print_t102_adr_005.py`
  - Intent (extract ADR‑005 only)
  - Inputs (`--concept-path`)
  - Expected boundary behavior (anchor present; next ADR excluded)
  - Common failure modes and remediation steps
- `prompt/skills/t102-adr-005-id-spec/scripts/sync_to_codex_mirror.py`
  - Intent (SSOT → Codex mirror)
  - `--check` behavior and exit codes
  - What files are copied and why
  - Safety constraints (refuse symlink destination)
  - Drift meaning and how to resolve

##### Task 0.8.3: Implement a single verification entrypoint script (ADR skills)

**Goal**: Provide one human-friendly command that validates Phase 0 end-to-end.

**Behavior (default: read-only)**:
- Verify SSOT structure
- Verify Claude distribution (symlink)
- Verify ADR‑005 extraction correctness
- Verify Codex distribution (mirror directory; not a symlink)
- Verify mirror parity via `sync_to_codex_mirror.py --check`

**Drift demo (required; but NOT default)**:
- Provide an explicit flag (e.g., `--drift-demo`) or separate demo command that:
  - Creates intentional drift in the Codex mirror
  - Proves `--check` detects drift
  - Runs sync to restore parity
  - Proves `--check` passes again

##### Task 0.8.4: Update ADR skills catalog to be a catalog (not a runbook)

**File**: `prompt/documentation/adr_skills_catalog.md`

**Goal**: Keep the catalog human-scannable and index-like.

Update to:
- Keep: skill purpose, triggers, scope, distribution architecture, pointers
- Replace embedded verification procedures with links to:
  - ADR skills verification runbook (Task 0.8.1)
  - Scripts documentation (Task 0.8.2)

##### Task 0.8.5: Commit-time enforcement (optional but recommended)

**Goal**: Enforce “no mirror drift lands” at commit time.

**Approach**:
- Provide an installer that sets up a `pre-commit` hook which:
  1) syncs SSOT → Codex mirror
  2) runs the verification entrypoint in check mode
  3) fails the commit if verification fails

**Notes**:
- Keep enforcement opt-in (installer-driven), but documented as recommended.
- Prefer no external dependencies in Phase 0 (avoid requiring third-party hook managers unless explicitly approved).

##### Task 0.8.6: Phase 0 re-signoff (post-extension)

**Goal**: Re-run Phase 0 verification using the new entrypoint, then finalize Phase 0 as complete.

**Verification**:
- [x] ADR skills verification runbook exists under `prompt/documentation/scripts/skills/`
- [x] Scripts documentation exists under `prompt/documentation/scripts/skills/`
- [x] Verification entrypoint runs and reports PASS for Phase 0 (without drift demo)
- [x] Drift demo works as documented (explicit invocation only)
- [x] Catalog points to the runbook/docs (instead of embedding verification procedures)

---

### Phase 0 Success Criteria (Checklist)

- [x] **SSOT Established**: `prompt/skills/t102-adr-005-id-spec/` contains SKILL.md and scripts/
- [x] **Adaptation Complete**: Script path updated, `allowed-tools` added
- [x] **Symlink Created**: `.claude/skills/t102-adr-005-id-spec` → `../../prompt/skills/...`
- [x] **Codex Mirror Established**: `.codex/skills/t102-adr-005-id-spec/` exists as a real directory (Codex-discoverable)
- [x] **Codex Mirror Sync Script Added**: local script syncs SSOT → `.codex/skills/t102-adr-005-id-spec/`
- [x] **Codex Mirror Sync Verified (Drift Demo)**: `--check` fails on drift; sync restores parity; `--check` passes again
- [x] **Git Configured**: `.gitattributes` tracks Claude Code symlinks correctly
- [x] **Extraction Validated (ADR-005 Only)**: anchor present; next ADR header excluded from output
- [x] **Agent Behavior Scenarios Validated (Manual)**: trigger, prompt-only gate, token validation, reference formatting
- [x] **Catalog Created**: `prompt/documentation/adr_skills_catalog.md` exists
- [x] **Catalog Updated (Codex Mirror + Verification)**: documents Claude symlink + Codex mirror + sync script + verification commands
- [x] **Codex Preserved**: prior Codex content preserved as `.codex/skills/t102-adr-005-id-spec-legacy` (or archived equivalent)
- [x] **Manual Discovery Confirmed (Claude Code)**: Client verified skill appears in Claude Code after restart
- [x] **Manual Discovery Confirmed (Codex CLI)**: Client verified skill appears in Codex after restart/reload

- [x] **ADR Skills Verification Runbook Added**: Dedicated verification runbook exists under `prompt/documentation/scripts/skills/`
- [x] **ADR Skills Scripts Documented**: Human-usable docs cover `print_t102_adr_005.py` and `sync_to_codex_mirror.py`
- [x] **ADR Skills Verification Entrypoint Added**: Single command/script verifies Phase 0 end-to-end (default read-only)
- [x] **Catalog Simplified**: `prompt/documentation/adr_skills_catalog.md` links to runbook/docs instead of embedding verification procedures
- [x] **Commit-time Enforcement Available (Optional)**: documented hook installer exists and is usable

## IV. PHASE 1: ADR SKILLS SYSTEM EXPANSION (FUTURE)

**Objective**: Extend ADR skills system with additional T102 ADRs, establish generalized patterns, and complete documentation integration.

**Constraint**: Phase 1 execution deferred pending Phase 0 completion and Client prioritization.

### Phase 1 Scope (Preview)

#### Activity 1.1: Verification System Generalization (Required)

**Objective**: Expand the Phase 0 verification system (built for `t102-adr-005-id-spec`) so it scales to additional ADR skills added in Phase 1 (ADR‑004/007/etc.).

**Registry format decision (Phase 1)**:
- Use a **Python registry module** to keep Phase 1 concise and rules-focused:
  - Minimal moving parts (no JSON parsing/schema design).
  - Can encode paths/expected anchors as typed constants.
  - Easy for verification entrypoint to import and iterate.

**Deliverables**:
- Update the **ADR skills verification runbook** under `prompt/documentation/scripts/skills/` to cover multiple skills (single place humans go for verification).
- Add a **Python registry file** under `prompt/scripts/skills/` (e.g., `adr_skills_registry.py`) defining the list of skills to verify (initially ADR-005 only; Phase 1 additions add entries).
- Update the **verification entrypoint** to load the registry and validate each skill (no hard-coded single-skill assumptions).
- Add per-skill verification sections (or a registry table) that includes:
  - SSOT location
  - Claude distribution mechanism
  - Codex distribution mechanism
  - Extraction script invocation and PASS criteria
  - Mirror parity checks (`--check`) and drift demo procedure (explicit invocation only)

**Acceptance criteria**:
- One command verifies all “Active Skills” in `prompt/documentation/adr_skills_catalog.md`.
- Adding a new ADR skill in Phase 1 requires only adding a new registry entry (not rewriting the verification system).

**Activity 1.1 Success Criteria (Checklist)**:

- [x] Registry module exists (`prompt/scripts/skills/adr_skills_registry.py`) and tracks only Active Skills.
- [x] Verification entrypoint is registry-driven (`prompt/scripts/skills/verify_adr_skills.py`) and has no single-skill hard-coding.
- [x] Catalog alignment enforced: Active Skills in `prompt/documentation/adr_skills_catalog.md` must match registry entries.
- [x] Default verification is read-only; drift demo is required but explicit invocation only (`--drift-demo`).
- [x] Drift demo works per registry skill (detect drift → sync restore → parity restored).
- [x] Sync-all helper exists (`prompt/scripts/skills/sync_codex_mirrors.py`) and is used by the commit-time hook.
- [x] Runbook + script reference updated for registry-driven multi-skill support (`prompt/documentation/scripts/skills/`).

---

#### Activity 1.2: Medium-Priority ADR Skill (ADR-004)

**Candidate**: `t102-adr-004-drs-index`
**Source**: T102-ADR-004 (Decision Records Index)
**Priority**: Medium (foundational standard, clear validation rules)
**Scope gate**: Files under `prompt/**` only

**Skill Scope (procedural; SSOT-first)**:
- Confirm the **scope gate**: target files are under `prompt/**`.
- Print ADR-004 via the extraction script and treat the printed ADR text as normative (do not paraphrase or restate rules in the skill).
- Apply ADR-004 rules while authoring or modifying:
  - Decision Records Index tables (GDR/ADR schema, placement)
  - Decision Record body sections (required headings/structure)
  - Cross-artifact linking and authority citation
  - Status lifecycle transitions (Proposed → Accepted → Deprecated)
- When RID-style formal references are required, explicitly invoke the ADR-005 skill workflow (print ADR-005 and apply its rules) rather than duplicating RID rules inside ADR-004.

**Source extraction boundary (strict)**:
- Extract exactly the block under:
  `* **T102-ADR-004 (Decision Records Index) {#t102-adr-004-drs-index}**`
- Stop at the next ADR header (do not include ADR-005 or anything after).

**Reference formatting (delegation; avoid drift)**:
- When ADR-004 requires RID-style formal references governed by ADR-005, do not restate those rules in the ADR-004 skill. Instead, explicitly invoke the ADR-005 skill workflow for formatting (print ADR-005 and apply its normative rules).

**Deliverables**:
- `prompt/skills/t102-adr-004-drs-index/SKILL.md`
- `prompt/skills/t102-adr-004-drs-index/scripts/print_t102_adr_004.py` (strict extraction script)
- Symlink: `.claude/skills/t102-adr-004-drs-index`
- Codex mirror: `.codex/skills/t102-adr-004-drs-index/` (real directory; Codex-discoverable)
- Codex mirror sync: `prompt/skills/t102-adr-004-drs-index/scripts/sync_to_codex_mirror.py` (SSOT → mirror; supports `--check`; mirror scope: `SKILL.md` + `print_t102_adr_004.py` only)
- Catalog update: Move `t102-adr-004-drs-index` into **Active Skills** in `prompt/documentation/adr_skills_catalog.md`

**Activity 1.2 Success Criteria (Checklist)**:
- [x] `prompt/skills/t102-adr-004-drs-index/SKILL.md` exists and includes the `prompt/**` scope gate and “print ADR-004 first” instruction, with explicit ADR-005 delegation when RID formatting is needed.
- [x] `prompt/skills/t102-adr-004-drs-index/scripts/print_t102_adr_004.py` extracts **only** ADR-004 (anchor `{#t102-adr-004-drs-index}` present; next ADR excluded).
- [x] `prompt/skills/t102-adr-004-drs-index/scripts/sync_to_codex_mirror.py` exists, supports `--check`, and mirrors only `SKILL.md` + `print_t102_adr_004.py`.
- [x] `.claude/skills/t102-adr-004-drs-index` is a symlink resolving to `prompt/skills/t102-adr-004-drs-index`.
- [x] `.codex/skills/t102-adr-004-drs-index/` exists as a real directory (not symlink) and matches SSOT after sync.
- [x] `prompt/scripts/skills/adr_skills_registry.py` includes an ADR-004 entry for `t102-adr-004-drs-index` with expected anchor `{#t102-adr-004-drs-index}`.
- [x] `prompt/documentation/adr_skills_catalog.md` uses `t102-adr-004-drs-index` as the planned name and lists ADR-004 in **Active Skills** when implemented.
- [x] `python3 prompt/scripts/skills/verify_adr_skills.py` passes with ADR-004 included.
- [x] `python3 prompt/scripts/skills/verify_adr_skills.py --drift-demo` passes with ADR-004 included.

---

#### Activity 1.3: High-Priority ADR Skill (ADR-007)

**Candidate**: `t102-adr-007-issues-risks-index`
**Source**: T102-ADR-007 (Issues & Risks Index)
**Priority**: High (recently added, immediate governance value)
**Scope gate**: Files under `prompt/**` only

**Core intent (procedural; SSOT-first)**:
- Apply `T102-ADR-007 (Issues & Risks Index)` as the single source of truth for:
  - Required Issues/Risks section naming/placement by artifact type
  - Issues/Risks table schemas (columns, ordering)
  - Status/priority enums and casing
  - Resolution/Mitigation coupling rules (notes + date requirements)
  - Cross-scope promotion/de-duplication guidance
- This activity intentionally avoids restating ADR-007 rules in skill docs (avoid drift). The skill must print ADR-007 and treat the printed output as normative.

**ADR-005 delegation (avoid drift)**:
- When ADR-007 requires ID construction or formal reference formatting governed by `T102-ADR-005` (e.g., `ISSUE` / `RISK` IDs and any RID formal references), do not restate those rules in the ADR-007 skill. Explicitly invoke the ADR-005 workflow (`t102-adr-005-id-spec`), print ADR-005, and apply its normative rules.

**Source extraction boundary (strict)**:
- Extract exactly the block under:
  `* **T102-ADR-007 (Issues & Risks Index) {#t102-adr-007-issues-risks-index}**`
- Stop at the next ADR header (do not include ADR-008 or anything after).

**Deliverables**:
- `prompt/skills/t102-adr-007-issues-risks-index/SKILL.md`
- `prompt/skills/t102-adr-007-issues-risks-index/scripts/print_t102_adr_007.py` (strict extraction script)
- Symlink: `.claude/skills/t102-adr-007-issues-risks-index`
- Codex mirror: `.codex/skills/t102-adr-007-issues-risks-index/` (real directory; Codex-discoverable)
- Codex mirror sync: `prompt/skills/t102-adr-007-issues-risks-index/scripts/sync_to_codex_mirror.py` (SSOT → mirror; supports `--check`; mirror scope: `SKILL.md` + `print_t102_adr_007.py` only)
- Catalog update: Add to Active Skills in `prompt/documentation/adr_skills_catalog.md`

**Implementation plan (high-level)**:
- Task 1.3.1: Confirm the ADR-007 anchor `{#t102-adr-007-issues-risks-index}` and validate the extraction stop condition (“next ADR header”).
- Task 1.3.2: Create SSOT skill directory and author `prompt/skills/t102-adr-007-issues-risks-index/SKILL.md` (prompt-only gate; procedural/SSOT-first; ADR-005 delegation instruction).
- Task 1.3.3: Implement `print_t102_adr_007.py` with strict extraction (anchor required; empty block fails; next ADR excluded).
- Task 1.3.4: Implement `sync_to_codex_mirror.py` with `--check` parity mode; mirror only `SKILL.md` + `print_t102_adr_007.py`.
- Task 1.3.5: Create `.claude/skills/t102-adr-007-issues-risks-index` symlink → SSOT.
- Task 1.3.6: Create/update `.codex/skills/t102-adr-007-issues-risks-index/` via the sync script (real directory, not symlink).
- Task 1.3.7: Add `t102-adr-007-issues-risks-index` to `prompt/scripts/skills/adr_skills_registry.py` (expected anchor `{#t102-adr-007-issues-risks-index}`).
- Task 1.3.8: Update `prompt/documentation/adr_skills_catalog.md` to list ADR-007 in **Active Skills** when implemented.
- Task 1.3.9: Run automated verification:
  - `python3 prompt/scripts/skills/verify_adr_skills.py`
  - `python3 prompt/scripts/skills/verify_adr_skills.py --drift-demo`

**Activity 1.3 Success Criteria (Checklist)**:
- [x] Skill slug matches the ADR anchor slug exactly: `t102-adr-007-issues-risks-index` (no variations allowed).
- [x] `prompt/skills/t102-adr-007-issues-risks-index/SKILL.md` exists and includes the `prompt/**` scope gate and “print ADR-007 first” instruction, with explicit ADR-005 delegation when ID/RID formatting is needed.
- [x] `prompt/skills/t102-adr-007-issues-risks-index/scripts/print_t102_adr_007.py` extracts **only** ADR-007 (anchor `{#t102-adr-007-issues-risks-index}` present; next ADR excluded).
- [x] `prompt/skills/t102-adr-007-issues-risks-index/scripts/sync_to_codex_mirror.py` exists, supports `--check`, and mirrors only `SKILL.md` + `print_t102_adr_007.py`.
- [x] `.claude/skills/t102-adr-007-issues-risks-index` is a symlink resolving to `prompt/skills/t102-adr-007-issues-risks-index`.
- [x] `.codex/skills/t102-adr-007-issues-risks-index/` exists as a real directory (not symlink) and matches SSOT after sync.
- [x] `prompt/scripts/skills/adr_skills_registry.py` includes an ADR-007 entry for `t102-adr-007-issues-risks-index` with expected anchor `{#t102-adr-007-issues-risks-index}`.
- [x] `prompt/documentation/adr_skills_catalog.md` lists ADR-007 in **Active Skills** and uses the canonical name `t102-adr-007-issues-risks-index`.
- [x] `python3 prompt/scripts/skills/verify_adr_skills.py` passes with ADR-007 included.
- [x] `python3 prompt/scripts/skills/verify_adr_skills.py --drift-demo` passes with ADR-007 included.

---

#### Activity 1.4: Skills & Parity Validation

**Objective**: Ensure both agents (Codex + Claude Code) consume the same SSOT skill set and that the ADR extraction output is clean and bounded (no unintended trailing content).

**Scope**: Registry-driven **Active Skills** (see `prompt/scripts/skills/adr_skills_registry.py`).

**Tasks (high-level)**:
- Task 1.4.1: Enforce distribution parity across agents:
  - Claude distribution: `.claude/skills/<skill>` is a symlink resolving to `prompt/skills/<skill>`
  - Codex distribution: `.codex/skills/<skill>/` is a real mirror directory (not a symlink)
- Task 1.4.2: Enforce clean ADR extraction boundaries:
  - Extraction must print the ADR header line (with expected anchor) and the ADR body only.
  - Extraction must not include unintended trailing sections (e.g., subsequent non-ADR headings/index tables).
  - ADR body lines are treated as a single Markdown list-item body: non-empty lines must be indented with **2+ spaces or a tab** (fail hard if this invariant is violated in the Concept SSOT).
- Task 1.4.2a: Enforce SSOT correctness for extraction targets:
  - For each Active Skill, the extraction output’s first line MUST match the ADR header line in the Concept SSOT that contains the expected anchor (anchor-driven extraction).
- Task 1.4.3: Update automated verification to detect unintended extraction output (generic rule; not hardcoded to one section name).
- Task 1.4.4: Ensure runbook documentation calls out the Concept SSOT formatting invariant (why indentation matters; how failures should be triaged).
- Task 1.4.5: Sync mirrors and run automated verification:
  - `python3 prompt/scripts/skills/verify_adr_skills.py`
  - `python3 prompt/scripts/skills/verify_adr_skills.py --drift-demo`
- Task 1.4.6 (Manual, Client): Discovery checks after restart/reload:
  - Claude Code: skill appears and is usable
  - Codex CLI: skill appears and is usable

**Activity 1.4 Success Criteria (Checklist)**:
- [x] Automated: `python3 prompt/scripts/skills/verify_adr_skills.py` passes.
- [x] Automated: `python3 prompt/scripts/skills/verify_adr_skills.py --drift-demo` passes.
- [x] Automated: For each Active Skill, extraction output contains only the intended ADR list-item block (no unintended trailing non-indented content).
- [x] Automated: For each Active Skill, the extraction output’s first line matches the Concept SSOT ADR header line containing the expected anchor.
- [x] Automated: Verifier fails if extraction includes any unintended non-indented trailing output (generic detection; no hardcoded section names).
- [x] Docs: Runbook documents the extraction invariant (ADR blocks are list items; body must be indented 2+ spaces or a tab; failures indicate Concept SSOT formatting drift).
- [x] Claude Code discovery check completed.
- [x] Codex CLI discovery check completed (manual, Client-verified: skills appear in Codex UI/list).

---

#### Activity 1.5: Documentation Integration

**Objective**: Reference ADR Skills Catalog in high-level documentation

**Files to update**:
- `documentation/general.md`: Add ADR Skills System section
- `prompt/documentation/prompt_main.md`: Add Skills Integration reference

**Content**: Brief overview + link to `prompt/documentation/adr_skills_catalog.md`

### Phase 1 Success Criteria

- [x] ADR-004 skill (`t102-adr-004-drs-index`) created and added to Active Skills catalog
- [x] ADR-007 skill created and added to Active Skills catalog
- [ ] Codex + Claude parity validated (post-additions)
- [ ] Verification system generalized for multi-skill support (runbook + entrypoint updated)
- [ ] Documentation integration complete
- [x] Catalog updated with new active skills
- [x] All Phase 1 skills pass `python3 prompt/scripts/skills/verify_adr_skills.py` and `python3 prompt/scripts/skills/verify_adr_skills.py --drift-demo`

---

## V. PHASE 2: SCRIPT GENERALIZATION

**Objective**: Remove per-skill script duplication (extraction + Codex mirror sync) while preserving the strict SSOT-first ADR block invariants already enforced by the Phase 1 verification system.

**Scope**:
- Applies only to ADR skills under filesystem prefix `prompt/` (SSOT at `prompt/skills/…`, system scripts at `prompt/scripts/skills/…`).
- Refactor-only: no skill generator tooling in Phase 2 (defer to Phase 3).
- Preserve stable per-skill entrypoints (Option A): each skill keeps its own `print_t102_adr_00X.py` and `sync_to_codex_mirror.py`, but those become thin wrappers around shared implementations.

**Context (existing Phase 1 assets to build on)**:
- Active skills SSOT: `prompt/skills/t102-adr-004-drs-index/`, `prompt/skills/t102-adr-005-id-spec/`, `prompt/skills/t102-adr-007-issues-risks-index/`
- Registry (SSOT wiring): `prompt/scripts/skills/adr_skills_registry.py`
- Verifier (strict invariants): `prompt/scripts/skills/verify_adr_skills.py`
- Codex mirror sync (all skills): `prompt/scripts/skills/sync_codex_mirrors.py`
- Optional commit-time enforcement installer: `prompt/scripts/skills/install_adr_skills_pre_commit_hook.py`
- Runbook + scripts reference: `prompt/documentation/scripts/skills/adr_skills_verification_runbook.md`, `prompt/documentation/scripts/skills/adr_skills_scripts_reference.md`

**TDD constraint (repo standard)**:
- Phase 2 script refactors MUST follow Red → Green → Refactor (one failing test at a time) per `AGENTS.md` and `documentation/testing/tdd/tdd_guard_quick_guide.md`.

### Phase 2 Activities

#### Activity 2.1: Shared ADR Extraction Script (Generalized)

**Objective**: Create a single shared extractor implementation that supports both:
- `--expected-anchor` (primary, strict, agent-oriented), and
- `--adr-id` (human convenience; resolved via registry).

**Scope**:
- Implement shared extraction under `prompt/scripts/skills/…`.
- Do not change ADR skill names or anchors (strict naming rule remains).
- Preserve existing extraction invariants (single ADR list-item block; indented body).

**Context**:
- Current per-skill extractors (examples):
  - `prompt/skills/t102-adr-005-id-spec/scripts/print_t102_adr_005.py`
  - `prompt/skills/t102-adr-004-drs-index/scripts/print_t102_adr_004.py`
  - `prompt/skills/t102-adr-007-issues-risks-index/scripts/print_t102_adr_007.py`
- Concept SSOT: `prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md`

**Task List**:
1. Add a shared extraction module + CLI, e.g.:
   - `prompt/scripts/skills/extract_adr.py` (CLI entrypoint)
   - `prompt/scripts/skills/adr_extraction.py` (shared implementation)
2. Implement strict extraction behavior identical to Phase 1:
   - Must find the ADR header line containing the expected anchor.
   - Must output only the ADR list-item block (header + indented body), stopping before non-indented content or next ADR header.
   - Must fail fast with actionable error messages (no fallback behavior).
3. Add concept path stability behavior:
   - Keep `--concept-path` override.
   - If default concept path does not exist, attempt a strict “latest version” lookup in the same directory (e.g., glob `concept_T102-CONSULTANT_v*.md`) and fail if ambiguous or missing.
4. Add TDD tests (new initiative-scoped location):
   - Create `prompt/tests/t103_adr_skills_system/` with unit tests for:
     - successful extraction by `--expected-anchor` for all registry skills (synthetic fixtures)
     - successful extraction by `--adr-id` (resolved via registry)
     - failure when anchor missing
     - failure when extraction would include non-indented trailing content
5. Update `pytest.ini` `testpaths` to include `prompt/tests` (in addition to existing `tests`) so Phase 2 tests are discoverable.

**Success Criteria Checklist**:
- [x] Shared extractor CLI exists (`prompt/scripts/skills/extract_adr.py`).
- [x] Shared extractor supports `--expected-anchor` (strict) and `--adr-id` (registry-resolved convenience).
- [x] Extraction invariant preserved (single ADR list-item block; indented body; no fallback).
- [x] `prompt/tests/t103_adr_skills_system/` created and tests run via `pytest`.
- [x] `pytest.ini` updated so `prompt/tests` is included in discovery.

---

#### Activity 2.2: Refactor Per-Skill Print Scripts (Thin Wrappers; Option A)

**Objective**: Keep stable per-skill entrypoints while removing duplicate extraction logic.

**Scope**:
- Refactor only the three existing skills (ADR-004, ADR-005, ADR-007).
- Do not change per-skill script names or paths.
- Do not change `SKILL.md` command lines unless required for parity (preferred: keep them stable).

**Context**:
- Shared extractor from Activity 2.1.
- Existing per-skill extractors under `prompt/skills/*/scripts/print_t102_adr_00X.py`.

**Task List**:
1. Refactor each `print_t102_adr_00X.py` to call the shared extractor implementation with:
   - a hardcoded `EXPECTED_ANCHOR = "{#...}"` (skill-specific), and
   - pass-through `--concept-path`.
2. Ensure output remains identical (including first line, and bounded extraction).
3. Add/extend tests to assert:
   - wrapper output contains the expected anchor
   - wrapper output begins with the same ADR header line as the Concept SSOT (anchor included)

**Success Criteria Checklist**:
- [x] `print_t102_adr_004.py` uses shared extractor (no duplicated parsing logic).
- [x] `print_t102_adr_005.py` uses shared extractor (no duplicated parsing logic).
- [x] `print_t102_adr_007.py` uses shared extractor (no duplicated parsing logic).
- [x] Verification remains green: `python3 prompt/scripts/skills/verify_adr_skills.py` passes.

---

#### Activity 2.3: Shared Codex Mirror Sync Implementation (Thin Wrappers; Option A)

**Objective**: Remove duplicated “SSOT → Codex mirror” sync logic while preserving per-skill sync entrypoints expected by the verifier and human workflows.

**Scope**:
- Create one shared sync implementation under `prompt/scripts/skills/…`.
- Refactor each per-skill `prompt/skills/<skill>/scripts/sync_to_codex_mirror.py` into a thin wrapper.
- Preserve `--check` semantics and safe-guard (refuse syncing into symlinked `.codex/skills/...` dirs).

**Context**:
- Existing per-skill sync scripts under:
  - `prompt/skills/t102-adr-004-drs-index/scripts/sync_to_codex_mirror.py`
  - `prompt/skills/t102-adr-005-id-spec/scripts/sync_to_codex_mirror.py`
  - `prompt/skills/t102-adr-007-issues-risks-index/scripts/sync_to_codex_mirror.py`
- Orchestrator: `prompt/scripts/skills/sync_codex_mirrors.py`
- Verifier parity check: `prompt/scripts/skills/verify_adr_skills.py` (calls per-skill `--check`)

**Task List**:
1. Add shared sync module + CLI helper, e.g.:
   - `prompt/scripts/skills/sync_to_codex_mirror.py` supporting:
     - `--skill-name` (registry-driven), and/or
     - `--ssot-dir` + `--dest-dir` (escape hatch for troubleshooting)
     - `--check`
2. Refactor per-skill sync scripts to delegate to the shared sync implementation while keeping their current interface stable.
3. Add unit tests using temp directories to validate:
   - `--check` fails on drift
   - sync restores parity
   - refuse-to-sync when destination is a symlink

**Success Criteria Checklist**:
- [x] Shared sync implementation exists under `prompt/scripts/skills/…`.
- [x] Per-skill `sync_to_codex_mirror.py` scripts are thin wrappers (no duplicated hashing/copy logic).
- [x] `python3 prompt/scripts/skills/sync_codex_mirrors.py` still works (registry-driven).
- [x] `python3 prompt/scripts/skills/verify_adr_skills.py --drift-demo` still passes.

---

#### Activity 2.4: CI Enforcement (GitHub Actions) — Mirror + Verification Gate

**Objective**: Replace local-only “pre-commit hook enforcement” with a repo-level CI gate that reliably fails PRs/commits when:
- Codex mirrors are stale relative to SSOT, or
- ADR extraction invariants break.

**Scope**:
- Add a GitHub Actions workflow under `.github/workflows/`.
- The CI must be read-only with respect to the repo: it may run sync for detection, but MUST fail if the working tree becomes dirty (i.e., mirrors were stale).
- Keep local hook script available only as an optional developer convenience (not the primary enforcement path).

**Context**:
- Verifier: `prompt/scripts/skills/verify_adr_skills.py` (registry-driven, strict invariants, parity checks via `--check`)
- Sync: `prompt/scripts/skills/sync_codex_mirrors.py` (writes mirrors)
- Registry: `prompt/scripts/skills/adr_skills_registry.py`

**Task List**:
1. Add workflow (example name: `adr-skills.yml`) to run on:
   - `pull_request`
   - `push` (default branch)
2. Workflow steps (high-level):
   - Checkout repo
   - Set up Python (match project baseline)
   - Run: `python3 prompt/scripts/skills/verify_adr_skills.py`
   - Run: `python3 prompt/scripts/skills/sync_codex_mirrors.py`
   - Fail if repo becomes dirty (CI is “read-only” in effect; sync is only used for detection), e.g.:
     - Stale mirror detection: `git diff --exit-code -- .codex/skills`
     - Full-tree safety check: `git diff --exit-code`
3. Ensure CI output is actionable (clear message: “mirrors are stale; run sync locally and commit the updated `.codex/skills/` mirror”).

**Success Criteria Checklist**:
- [x] GitHub Actions workflow exists under `.github/workflows/` and runs on PR + push.
- [x] CI fails if `python3 prompt/scripts/skills/verify_adr_skills.py` fails.
- [x] CI fails if `sync_codex_mirrors.py` produces changes under `.codex/skills/` (stale mirror detection).
- [x] CI fails if `sync_codex_mirrors.py` produces any other repo changes (full-tree clean check).
- [x] CI passes when mirrors are already in sync and verification passes.

---

#### Activity 2.5: Phase 2 Verification & Regression Gate (Pre-Docs)

**Objective**: Confirm Activities 2.1–2.4 are correct and stable before any documentation updates.

**Scope**:
- Automation-first verification run; uses the same contracts as CI.
- Includes a required manual discovery annotation (no screenshots or outputs recorded in the plan).
- No new tooling beyond repo-local Python + pytest + git.

**Context**:
- Verifier: `prompt/scripts/skills/verify_adr_skills.py`
- Registry: `prompt/scripts/skills/adr_skills_registry.py`
- Sync orchestrator: `prompt/scripts/skills/sync_codex_mirrors.py`
- Runbook: `prompt/documentation/scripts/skills/adr_skills_verification_runbook.md`

**Task List**:
1. Run baseline verification: `python3 prompt/scripts/skills/verify_adr_skills.py`
2. Run required drift demonstration: `python3 prompt/scripts/skills/verify_adr_skills.py --drift-demo`
3. Run initiative-scoped tests: `pytest -q prompt/tests/t103_adr_skills_system`
4. Validate mirror idempotency locally (allow other local changes; `.codex/skills` must remain clean):
   - Run: `python3 prompt/scripts/skills/sync_codex_mirrors.py`
   - Assert: `git diff --exit-code -- .codex/skills`
5. Manual discovery annotation (Client-run):
   - Codex CLI discovery: skills appear after reload/restart
   - Claude Code discovery: skills appear after reload/restart

**Success Criteria Checklist**:
- [x] `python3 prompt/scripts/skills/verify_adr_skills.py` passes (exit 0). (Verified locally: 2026-01-10)
- [x] `python3 prompt/scripts/skills/verify_adr_skills.py --drift-demo` passes (exit 0). (Verified locally: 2026-01-10)
- [x] `pytest -q prompt/tests/t103_adr_skills_system` passes. (Verified locally: 2026-01-10)
- [x] `python3 prompt/scripts/skills/sync_codex_mirrors.py` is idempotent for `.codex/skills` (`git diff --exit-code -- .codex/skills`). (Verified locally: 2026-01-10)
- [x] Catalog alignment is validated (covered by `verify_adr_skills.py`). (Verified locally: 2026-01-10)
- [x] Manual discovery annotation recorded: Codex CLI + Claude Code show the current Active Skills list.

**Manual discovery annotation (Client-run)**:
- Date/time:
- Codex CLI (after restart/reload): Skills list shows `t102-adr-004-drs-index`, `t102-adr-005-id-spec`, `t102-adr-007-issues-risks-index`
- Claude Code (after restart/reload): Skills list shows `t102-adr-004-drs-index`, `t102-adr-005-id-spec`, `t102-adr-007-issues-risks-index`

---

#### Activity 2.6: Documentation Updates (Post-Refactor)

**Objective**: Ensure humans can run, review, and troubleshoot the generalized scripts without reading code.

**Scope**:
- Documentation-only changes after Activities 2.1–2.3 are complete.
- Do not expand scope to non-ADR tooling; keep this tightly focused on ADR skills scripts + workflows.

**Context**:
- Scripts reference: `prompt/documentation/scripts/skills/adr_skills_scripts_reference.md`
- Verification runbook: `prompt/documentation/scripts/skills/adr_skills_verification_runbook.md`
- Catalog overview: `prompt/documentation/adr_skills_catalog.md`

**Task List**:
1. Update scripts reference to include the new shared extractor and sync implementations:
   - usage examples for `--expected-anchor` and `--adr-id`
   - usage examples for sync `--check` and full sync
2. Update runbook to reflect Phase 2 refactor behavior and failure modes.
3. Update catalog pointers if any commands or file paths changed (keep catalog high-level).

**Success Criteria Checklist**:
- [x] Scripts reference updated for shared extractor + shared sync (with concrete command examples).
- [x] Verification runbook updated to match the new internal architecture (wrappers + shared core).
- [x] No “T103/Phase 0 naming” leaks into user-facing documentation (docs refer to deliverables, not PM phases).

### Phase 2 Success Criteria

- [x] Shared extractor exists and supports `--expected-anchor` (strict) and `--adr-id` (convenience)
- [x] ADR-004/005/007 print scripts are thin wrappers around the shared extractor (stable entrypoints preserved)
- [x] Shared Codex mirror sync implementation exists; per-skill sync scripts are thin wrappers (stable entrypoints preserved)
- [x] Phase 2 tests exist under `prompt/tests/t103_adr_skills_system/` and run via `pytest`
- [x] `python3 prompt/scripts/skills/verify_adr_skills.py` and `python3 prompt/scripts/skills/verify_adr_skills.py --drift-demo` still pass
- [x] GitHub Actions CI gate added (fails on stale mirrors or verification failures)
- [x] Runbook + scripts reference updated to reflect the refactor

---

## VI. RISK ASSESSMENT

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| **Symlink breaks on Windows** | Medium | High | Test on WSL; Phase 0 targets WSL/Linux environments |
| **Script path wrong after move** | Low | High | Automated testing in Activity 0.4 catches this |
| **Skill doesn't auto-trigger** | Medium | Medium | CSO keywords already strong in description; monitor usage |
| **Git ignores symlinks** | Low | High | Explicit `.gitattributes` configuration in Task 0.3.2 |
| **Codex mirror drift** | Medium | Medium | Require running sync script after SSOT edits; add diff-based verification in Activity 0.6 |
| **Concept file relocated** | Low | Medium | Script uses configurable `--concept-path` argument |
| **SSOT/symlink confusion** | Medium | Low | Clear documentation in catalog; SSOT principle enforced |

---

## VII. DECISION LOG

### Decision 1: SSOT Location
**Question**: Where should the SSOT live?
**Options**: `.claude/skills/`, `prompt/skills/`, `prompt/tools/`
**Chosen**: `prompt/skills/`
**Rationale**: Aligns with prompt artifact governance scope; maintains proximity to source; enables future co-location

### Decision 2: Symlink Strategy
**Question**: One-way or bidirectional symlinks?
**Options**: One-way (.claude → prompt), bidirectional, managed duplication
**Chosen**: One-way symlink
**Rationale**: Simplest architecture; clear SSOT; no duplication; aligns with "link-don't-duplicate" principle

### Decision 3: Codex Integration Timing
**Question**: How should Codex consume SSOT skills given known symlink discovery limits?
**Options**: Symlink from `.codex/skills/` → SSOT, copy-based mirror from SSOT, or keep Codex-only source
**Chosen**: Copy-based mirror (temporary) via Activity 0.6
**Rationale**: Ensures Codex CLI reliably discovers the skill while preserving SSOT as the only edited source

### Decision 4: Documentation Integration Timing
**Question**: Update general.md and prompt_main.md in Phase 0?
**Options**: Include in Phase 0, defer to Phase 1
**Chosen**: Defer to Phase 1 (per Client comment)
**Rationale**: Phase 0 focuses on catalog creation; high-level docs updated after system proven

---

## VIII. CHANGELOG

- **v1.0.0** (2026-01-02): Initial plan creation
  - Phase 0: ADR-005 skill conversion with SSOT architecture
  - Phase 1: Future expansion (ADR-007, ADR-004, Codex integration, documentation)
  - Phase 2: Script generalization
  - ADR Skills Catalog established
  - Risk assessment and decision log included
