---
artifact_type: "PLAN"
initiative_id: "T103A1"
epic_id: "T103A1-ADRSS"
version: "0.1.0"
date: "2026-01-14"
status: "draft"
author: "LLM_Consultant"
decision_owner_role: "Client"
---

# PLAN: T103A1 ADR Rules System — Phase 3 (Single Skill) + Phase 4 (Generator)

## I. EXECUTIVE SUMMARY

This plan defines the next evolution of the T103 ADR Skills System:

- **Phase 3**: Add a new *single* ADR rules skill named `t102-adr-rules-system` that can print one or more ADR blocks on demand (agentic, strict, SSOT-first), while keeping existing per-ADR skills unchanged during adoption.
- **Phase 4**: Introduce a generator workflow that derives the supported ADR registry from the Concept SSOT (start with registry generation only; later expand to docs/scaffolding after stronger testing).

**Non-goals**
- Phase 3 does **not** deprecate or remove existing ADR skills (`t102-adr-004-drs-index`, `t102-adr-005-id-spec`, `t102-adr-007-issues-risks-index`). Deprecation is deferred until the new single skill is validated in real usage.
- Phase 3 does **not** add broad “prompt-only” gates; scope gating is handled by the caller’s workflow, not by hard blocking in the skill.

---

## II. CONTEXT MATERIALS & CURRENT STATE (SSOT)

**Current system plan (Phase 0–2 history + current architecture)**:
- `prompt/artifacts/tasks/T103/workspace/plan/plan_T103_adr-skills-system.md`

**Concept SSOT (authoritative ADR text)**:
- `prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md`

**Shared scripts (Phase 2 deliverables)**:
- Extraction CLI: `prompt/scripts/skills/extract_adr.py`
- Extraction core: `prompt/scripts/skills/adr_extraction.py`
- Registry: `prompt/scripts/skills/adr_skills_registry.py`
- Verifier: `prompt/scripts/skills/verify_adr_skills.py`
- Codex mirror sync (all): `prompt/scripts/skills/sync_codex_mirrors.py`

**Active per-ADR skills (remain in use during Phase 3)**:
- `prompt/skills/t102-adr-004-drs-index/`
- `prompt/skills/t102-adr-005-id-spec/`
- `prompt/skills/t102-adr-007-issues-risks-index/`

---

## III. PHASE 3: SINGLE ADR RULES SKILL (t102-adr-rules-system)

**Objective**: Add `t102-adr-rules-system` as a single, agent-friendly skill that prints one or more ADR blocks with strict boundaries and minimal token overhead.

**Scope**
- Create a new SSOT skill at `prompt/skills/t102-adr-rules-system/` with:
  - `SKILL.md` (procedural, SSOT-first; does not restate ADR rules),
  - scripts that print ADR blocks via shared extraction logic.
- Keep current per-ADR skills unchanged and still “Active”.

**Key design constraints**
- **No implicit “print all”**: To avoid accidental context blowups, the CLI requires explicit selection (industry-standard “explicit is better than implicit” for tools that can output large content).
- Selection is by:
  - `--expected-anchor` (strict core selector), and
  - `--adr-id` (human convenience selector).
- Multi-ADR output is supported by passing multiple selectors; output uses a deterministic, low-token delimiter between blocks.

### Phase 3 Activities

#### Activity 3.1: Concept Path Normalization (Default Stability)

**Objective**: Ensure default extraction uses the current Concept SSOT path and does not rely on missing or archived files.

**Scope**:
- Align all default concept-path usage across extraction entrypoints to:
  - `prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md`
- Preserve `--concept-path` override for troubleshooting.

**Context**:
- Concept SSOT: `prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md`
- Shared extractor: `prompt/scripts/skills/extract_adr.py`
- Shared resolver: `prompt/scripts/skills/adr_extraction.py`

**Task List**:
1. Update shared extractor defaults to use the unversioned Concept SSOT path.
2. Update any remaining per-skill print entrypoints that hardcode a versioned concept path.
3. Add/adjust tests to ensure default path works and that `--concept-path` override remains supported.

**Success Criteria Checklist**:
- [x] Default concept path across extraction entrypoints resolves to `concept_T102-CONSULTANT.md`.
- [x] `--concept-path` override remains supported and tested.
- [x] No dependency on Concept files stored under `prompt/artifacts/tasks/T102/consultant/concept/archive/`.

---

#### Activity 3.2: New Skill SSOT Scaffolding (t102-adr-rules-system)

**Objective**: Create the new skill in SSOT form, with minimal procedural instructions and stable scripts.

**Scope**:
- Create:
  - `prompt/skills/t102-adr-rules-system/SKILL.md`
  - `prompt/skills/t102-adr-rules-system/scripts/print_t102_adr_rules_system.py` (name can vary; keep stable once chosen)

**Context**:
- Skill catalog: `prompt/documentation/adr_skills_catalog.md`
- Shared extraction CLI: `prompt/scripts/skills/extract_adr.py`

**Task List**:
1. Write `SKILL.md` to:
   - instruct the agent to print required ADR blocks (SSOT-first),
   - avoid duplicating ADR text,
   - describe selector usage patterns (expected-anchor is core; adr-id is convenience),
   - describe multi-ADR delimiter rules for clean agent parsing.
2. Create the skill’s print script as a thin wrapper around shared extraction logic.
3. Wire Claude/Codex distribution following the existing system patterns (symlink for Claude; mirror for Codex).

**Success Criteria Checklist**:
- [ ] SSOT exists at `prompt/skills/t102-adr-rules-system/` with `SKILL.md` + scripts.
- [ ] The new print script delegates to shared extraction logic (no custom parsing).
- [ ] Distribution parity is documented for the new skill (Claude symlink; Codex mirror).

---

#### Activity 3.3: Multi-ADR Selection + Output Contract

**Objective**: Support printing multiple ADR blocks in one invocation with minimal context waste and deterministic segmentation.

**Scope**:
- Selector rules:
  - Require at least one selector: one or more `--expected-anchor` and/or `--adr-id`.
  - If both are provided, treat the union as the requested set (dedupe by anchor).
  - No implicit “print all”.
- Output rules:
  - Print each extracted ADR block verbatim.
  - Insert a low-token delimiter between blocks: `<!-- ADR-SPLIT -->`.

**Context**:
- Shared extractor: `prompt/scripts/skills/extract_adr.py`
- Registry: `prompt/scripts/skills/adr_skills_registry.py`

**Task List**:
1. Implement multi-selector parsing for the new skill wrapper script.
2. Dedupe blocks by `expected_anchor` so the output is stable regardless of selector type.
3. Add tests for:
   - single selector output (no delimiter),
   - multi-selector output (delimiter inserted between blocks only),
   - dedupe behavior.

**Success Criteria Checklist**:
- [ ] Printing multiple ADRs requires explicit selectors (no implicit “all”).
- [ ] Multi-ADR output uses `<!-- ADR-SPLIT -->` delimiter between blocks only.
- [ ] Dedupe by anchor is implemented and tested.

---

#### Activity 3.4: Verification & “Parallel Active Skill” Integration

**Objective**: Validate the new single skill without breaking current production usage of the existing per-ADR skills.

**Scope**:
- Extend verification so that:
  - existing per-ADR skills still pass, unchanged,
  - the new single skill is validated for multi-ADR correctness and concept-path stability.

**Context**:
- Verifier: `prompt/scripts/skills/verify_adr_skills.py`
- Catalog: `prompt/documentation/adr_skills_catalog.md`

**Task List**:
1. Add new verification checks for `t102-adr-rules-system`:
   - selector-required behavior,
   - output delimiter correctness,
   - correctness of extracted ADR blocks (header line contains expected anchors).
2. Ensure checks remain registry-driven and do not hardcode ADR section names.

**Success Criteria Checklist**:
- [ ] Existing per-ADR skills continue to pass verification unchanged.
- [ ] New single skill passes verification for multi-ADR behavior and delimiter correctness.
- [ ] Verification remains generic (no hardcoded ADR section names).

---

#### Activity 3.5: Documentation Updates (Phase 3)

**Objective**: Update catalog and scripts reference so humans know how to use the new skill safely.

**Scope**:
- Add `t102-adr-rules-system` to the catalog as “Active (Parallel)” until deprecation is approved.
- Add usage examples showing explicit selection and delimiter behavior.

**Context**:
- Catalog: `prompt/documentation/adr_skills_catalog.md`
- Scripts reference: `prompt/documentation/scripts/skills/adr_skills_scripts_reference.md`

**Task List**:
1. Update catalog with:
   - purpose + trigger guidance,
   - selector usage patterns,
   - coexistence note (existing skills remain active).
2. Update scripts reference with concrete examples for:
   - `--expected-anchor`
   - `--adr-id`
   - multiple ADRs with delimiter.

**Success Criteria Checklist**:
- [ ] Catalog documents `t102-adr-rules-system` as “Active (Parallel)”.
- [ ] Scripts reference includes explicit multi-ADR usage patterns.
- [ ] Docs avoid PM naming leaks (refer to deliverables, not phase labels).

---

### Phase 3 Success Criteria

- [ ] `t102-adr-rules-system` exists and functions in parallel with existing per-ADR skills.
- [ ] Concept path defaults are stable and aligned to `concept_T102-CONSULTANT.md`.
- [ ] Multi-ADR printing requires explicit selection and uses deterministic `<!-- ADR-SPLIT -->` delimiter.
- [ ] Verification covers the new skill without breaking existing skills.
- [ ] Documentation updated for new skill usage and coexistence.

---

## IV. PHASE 4: REGISTRY GENERATOR (START WITH (A), EXPAND TO (B) LATER)

**Objective**: Reduce manual maintenance by generating the “supported ADR set” registry from the Concept SSOT while keeping runtime extraction deterministic and strict.

**Scope (Phase 4.A only)**:
- Generate/update only the registry data (e.g., `prompt/scripts/skills/adr_skills_registry.py` or a registry source file consumed by it).
- No automatic creation of new skill directories or docs in Phase 4.A.

**Planned expansion (Phase 4.B, after extensive testing)**:
- Expand generator responsibilities to include docs and/or scaffolding updates:
  - update `prompt/documentation/adr_skills_catalog.md`,
  - optionally scaffold per-ADR skill directories or update single-skill supported ADR lists.

### Phase 4 Activities

#### Activity 4.1: Registry Generator (Phase 4.A)

**Objective**: Generate registry entries from Concept SSOT in a deterministic and reviewable way.

**Scope**:
- Add a generator script under `prompt/scripts/skills/` that:
  - reads Concept SSOT,
  - extracts ADR IDs + anchors from the index/table and/or ADR headers,
  - writes registry output in a stable order.

**Context**:
- Concept SSOT: `prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md`
- Registry: `prompt/scripts/skills/adr_skills_registry.py`

**Task List**:
1. Define the generator’s input source in the Concept:
   - preferred: use the ADR index table (stable), with ADR header/anchor as verification.
2. Implement generation into a reviewable artifact (stable formatting and ordering).
3. Add tests:
   - deterministic output for fixed input fixtures,
   - failure on ambiguous/duplicate anchors.

**Success Criteria Checklist**:
- [ ] Generator exists and produces deterministic registry output.
- [ ] Generator is covered by tests (fixtures + ambiguity failures).
- [ ] Registry updates are reviewable (stable diff; stable ordering).

---

#### Activity 4.2: CI Gate for Generator Drift (Phase 4.A)

**Objective**: Prevent silent divergence between Concept SSOT and registry output.

**Scope**:
- Add CI that fails if:
  - generator output is stale relative to Concept SSOT, or
  - verification fails for the supported ADR set.

**Context**:
- Generator script (Activity 4.1)
- Verifier: `prompt/scripts/skills/verify_adr_skills.py`

**Task List**:
1. Add CI step to run generator in “check mode” (or generate then assert clean git tree).
2. Keep CI read-only in effect (fail if generation would change tracked files).

**Success Criteria Checklist**:
- [ ] CI fails on stale registry output relative to Concept SSOT.
- [ ] CI remains read-only in effect (no auto-commits).

---

#### Activity 4.3: Expansion Plan to Phase 4.B (Docs/Scaffolding) (Design-Only)

**Objective**: Define a safe path to expand generator responsibilities after Phase 4.A is proven stable.

**Scope**:
- Design-only: enumerate what “Phase 4.B” will generate, and what guardrails are required before enabling it.

**Task List**:
1. Specify the “Phase 4.B” generation targets (docs, scaffolds, catalog sections).
2. Define guardrails:
   - dry-run mode,
   - explicit allowlist of outputs,
   - mandatory snapshot tests.

**Success Criteria Checklist**:
- [ ] Phase 4.B scope and guardrails documented and approved before implementation.

---

### Phase 4 Success Criteria

- [ ] Registry generator exists (Phase 4.A) with deterministic output and tests.
- [ ] CI blocks stale registry generation (read-only in effect).
- [ ] Phase 4.B expansion is clearly specified with guardrails and deferred until proven safe.
