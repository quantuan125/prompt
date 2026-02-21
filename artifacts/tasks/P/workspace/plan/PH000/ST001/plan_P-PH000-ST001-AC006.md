---
artifact_type: 'PLAN'
planning_level: 'ACTIVITY'
initiative_id: 'P'
initiative_code: 'PROGRAM'
phase: '0'
stream_id: 'P-PH000-ST001'
activity_id: 'P-PH000-ST001-AC006'
version: '1.0.0'
date: '2026-02-22'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
governance_rules: 'prompt/templates/consultant/workspace/workspace_documentation_rules.md'
procedural_guideline: 'prompt/templates/consultant/workspace/guideline_workspace_plan.md'
parent_plan: 'prompt/artifacts/tasks/P/workspace/plan/plan_P-PH000-ST001.md'
---

# PLAN: Program Governance (PROGRAM) — Phase 0 / Stream ST001 / Activity P-PH000-ST001-AC006: Promote T102-STD-005 to P-STD-005 (Universal ID Specification)

## I. EXECUTIVE SUMMARY

**Purpose**: Promote `T102-STD-005` (ID Specification & Rules) to `P-STD-005` (Universal ID Specification) at Program scope. This promotion: (1) fixes stale references to superseded T102-STD-004 and T102-STD-009, (2) verifies pending amendments (ST005-AC005 deltas) are applied, (3) performs full content transfer with 1:1 CLAUSE re-identification, (4) authors timeline UID CLAUSEs (absorbing T104-STD-002 planned scope) directly into P-STD-005, (5) updates Tier 1 normative references across program-level artifacts, and (6) amends downstream plans that had planned work now absorbed.

**Non-goals**:
- This activity does not perform repo-wide remediation sweeps of existing `T102-STD-005-CLAUSE-*` references (these are covered by the alias window and migrated at next touch).
- This activity does not execute the full T102-PH001-ST002 baselining pipeline (a targeted pre-promotion audit is performed instead).
- This activity does not modify T102-STD-005 CLAUSE content beyond stale reference fixes and verified amendment application.

---

## II. ACTIVITY OUTLINE

**Activity ID**: `P-PH000-ST001-AC006`
**Objective**: Promote T102-STD-005 to P-STD-005 via fix-first/promote-clean methodology, absorbing T104-STD-002 timeline UID scope and T102-PH001-ST005-AC005 amendment scope.
**Execution Mode**: `SEQUENTIAL`
**Depends On**: `P-PH000-ST001-AC002` (completed)

**Context**:
- `prompt/artifacts/tasks/P/workspace/plan/plan_P-PH000-ST001.md`
- `prompt/artifacts/tasks/P/ssot/sps_P-PROGRAM.md`
- `prompt/artifacts/tasks/P/workspace/plan/PH000/ST001/plan_P-PH000-ST001-AC006.md`
- `prompt/artifacts/tasks/P/standard/standard_P-STD-005_universal-id-specification.md` (NEW)
- `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md`
- `prompt/artifacts/tasks/P/standard/P-STD-003_governance-standards-and-dr-index.md`
- `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-005_id-specification-rules.md`
- `prompt/artifacts/tasks/T104/workspace/PH001/ST002/plan_T104-PH001-ST002.md`
- `prompt/artifacts/tasks/T102/consultant/workspace/plan/plan_T102-PH001-ST005.md`
- `prompt/artifacts/tasks/T102/consultant/workspace/plan/plan_T102-PH001-ST002.md`
- `prompt/templates/consultant/standards/guideline_standard_specs.md`
- `prompt/skills/t102-adr-005-id-spec/SKILL.md`
- `prompt/documentation/adr_skills_catalog.md`

### Task Register

| Task | Task ID | Name | Status | Owner | Depends On | Target | Reference | Action |
|:--|:--|:--|:--|:--|:--|:--|:--|:--|
| TK001 | `P-PH000-ST001-AC006-TK001` | Fix stale references in T102-STD-005 (T102-STD-004 → P-STD-001, T102-STD-009 → P-STD-001) | `planned` | LLM_Developer | — | `T102-STD-005_id-specification-rules.md` | Stale refs mapping (see plan) | — |
| TK002 | `P-PH000-ST001-AC006-TK002` | Verify ST005-AC005 deltas (C1, C2, B1) are applied to T102-STD-005 | `planned` | LLM_Developer | TK001 | `T102-STD-005_id-specification-rules.md` | RES-005 Delta C, RES-006 Delta B | — |
| TK003 | `P-PH000-ST001-AC006-TK003` | Targeted self-compliance audit of T102-STD-005 against P-STD-001 | `planned` | LLM_Reviewer | TK002 | Analysis artifact | `P-STD-001` | — |
| GATE-001 | `P-PH000-ST001-AC006-GATE-001` | Gate: Client approval of pre-promotion T102-STD-005 state | `planned` | Client | TK003 | Pass/fail | — | — |
| TK004 | `P-PH000-ST001-AC006-TK004` | Author promotion contract proposal (re-identification mapping + timeline UID CLAUSE text + alias window + Tier 1 ref update plan) | `planned` | LLM_Consultant | GATE-001 | Proposal artifact | `P-STD-001-CLAUSE-030`, `T102-STD-005-CLAUSE-003A` | — |
| GATE-002 | `P-PH000-ST001-AC006-GATE-002` | Gate: Client approval of promotion contract | `planned` | Client | TK004 | Pass/fail | — | — |
| TK005 | `P-PH000-ST001-AC006-TK005` | Create P-STD-005 combined file (full content transfer + timeline UID CLAUSEs per contract) | `planned` | LLM_Developer | GATE-002 | `standard_P-STD-005_universal-id-specification.md` | Promotion contract | — |
| TK006 | `P-PH000-ST001-AC006-TK006` | Mark T102-STD-005 as superseded + establish alias window | `planned` | LLM_Developer | TK005 | `T102-STD-005_id-specification-rules.md` | `T102-STD-005-CLAUSE-003A/003B` | — |
| TK007 | `P-PH000-ST001-AC006-TK007` | Update P-STD-001 references (T102-STD-005 → P-STD-005) | `planned` | LLM_Developer | TK005 | `standard_P-STD-001_program-governance-standard.md` | Tier 1 ref update | — |
| TK008 | `P-PH000-ST001-AC006-TK008` | Update Program SPS P-STD-005 row + remaining Tier 1 reference files | `planned` | LLM_Developer | TK005 | `sps_P-PROGRAM.md`, `P-STD-003`, guideline, skills, catalog | Tier 1 ref update | — |
| TK009 | `P-PH000-ST001-AC006-TK009` | Amend downstream plans (T104-ST002 AC002, T102-ST005 AC005, T102-ST002 STD-005 scope) | `planned` | LLM_Consultant | TK005 | 3 plan files | Absorption notes | — |
| TK010 | `P-PH000-ST001-AC006-TK010` | Produce verification evidence | `planned` | LLM_Reviewer | TK006, TK007, TK008, TK009 | Verification artifact | — | — |
| GATE-003 | `P-PH000-ST001-AC006-GATE-003` | Gate: Client approval of completed promotion | `planned` | Client | TK010 | Pass/fail | — | — |

---

## III. TASKS (DETAILED)

### Task TK001: Fix stale references in T102-STD-005
**Task ID**: `P-PH000-ST001-AC006-TK001`
**Purpose**: Update stale references to superseded standards before promotion.
**Deliverable**: Updated `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-005_id-specification-rules.md`.

### Task TK002: Verify ST005-AC005 deltas applied
**Task ID**: `P-PH000-ST001-AC006-TK002`
**Purpose**: Verify/apply Deltas C1, C2, B1 in T102-STD-005.
**Deliverable**: Verification evidence in task action and updated source if needed.

### Task TK003: Targeted self-compliance audit
**Task ID**: `P-PH000-ST001-AC006-TK003`
**Purpose**: Validate source structure against `P-STD-001` before promotion.
**Deliverable**: `prompt/artifacts/tasks/P/workspace/analysis/analysis_P-PH000-ST001-AC006_pre-promotion-audit.md` (or equivalent notes evidence).

### GATE-001: Client approval of pre-promotion state
**Gate ID**: `P-PH000-ST001-AC006-GATE-001`
**Entry Criteria**: TK001, TK002, TK003 complete.
**Exit Criteria**: Client confirms source is clean for promotion.

### Task TK004: Author promotion contract proposal
**Task ID**: `P-PH000-ST001-AC006-TK004`
**Purpose**: Produce decision-complete contract for mechanical execution.
**Deliverable**: `prompt/artifacts/tasks/P/workspace/proposal/proposal_P-PH000-ST001-AC006_promotion-contract-t102-std-005-to-p-std-005.md`.

### GATE-002: Client approval of promotion contract
**Gate ID**: `P-PH000-ST001-AC006-GATE-002`
**Entry Criteria**: TK004 complete.
**Exit Criteria**: Client-approved contract with no blockers.

### Task TK005: Create combined P-STD-005
**Task ID**: `P-PH000-ST001-AC006-TK005`
**Deliverable**: `prompt/artifacts/tasks/P/standard/standard_P-STD-005_universal-id-specification.md`.

### Task TK006: Supersede T102-STD-005
**Task ID**: `P-PH000-ST001-AC006-TK006`
**Deliverable**: Supersession notice + alias terms in `T102-STD-005_id-specification-rules.md`.

### Task TK007: Update P-STD-001 references
**Task ID**: `P-PH000-ST001-AC006-TK007`
**Deliverable**: Updated `standard_P-STD-001_program-governance-standard.md` with `P-STD-005` references.

### Task TK008: Update Program SPS + Tier 1 files
**Task ID**: `P-PH000-ST001-AC006-TK008`
**Deliverable**: Updated `sps_P-PROGRAM.md`, `P-STD-003`, guideline, skill, catalog references.

### Task TK009: Amend downstream plans
**Task ID**: `P-PH000-ST001-AC006-TK009`
**Deliverable**: Amendments in T104 ST002, T102 ST005, T102 ST002 plans with absorption notes/changelog.

### Task TK010: Produce verification evidence
**Task ID**: `P-PH000-ST001-AC006-TK010`
**Deliverable**: `prompt/artifacts/tasks/P/workspace/verification/verification_P-PH000-ST001-AC006_tk005-to-tk009.md`.

### GATE-003: Client approval of completed promotion
**Gate ID**: `P-PH000-ST001-AC006-GATE-003`
**Entry Criteria**: TK005-TK010 completed and verified.
**Exit Criteria**: Client approves promotion completion.

---

## IV. LINKS REGISTER

| Link Type | Target | Path |
|:--|:--|:--|
| Plan (this file) | AC006 Activity Plan | `prompt/artifacts/tasks/P/workspace/plan/PH000/ST001/plan_P-PH000-ST001-AC006.md` |
| Plan | P Stream Plan | `prompt/artifacts/tasks/P/workspace/plan/plan_P-PH000-ST001.md` |
| SSOT | Program SPS | `prompt/artifacts/tasks/P/ssot/sps_P-PROGRAM.md` |
| Reference | P-STD-001 (golden exemplar) | `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md` |
| Reference | T102-STD-005 (source standard) | `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-005_id-specification-rules.md` |
| Reference | P-STD-001 promotion contract (precedent) | `prompt/artifacts/tasks/P/workspace/proposal/proposal_P-PH000-ST001-AC002_promotion-contract-t102-std-004-to-p-std-001.md` |
| Reference | P-STD-001 promotion activity plan (precedent) | `prompt/artifacts/tasks/P/workspace/plan/PH000/ST001/plan_P-PH000-ST001-AC002.md` |
| Reference | RES-005 analysis (delta source) | `prompt/artifacts/tasks/T102/consultant/workspace/analysis/analysis_T102-RES-005_cross-scope-coordination-architecture.md` |
| Reference | RES-006 analysis (delta source) | `prompt/artifacts/tasks/T102/consultant/workspace/analysis/analysis_T102-RES-006_integration-impact.md` |
| Reference | T104-PH001-ST002 plan (AC002 absorption) | `prompt/artifacts/tasks/T104/workspace/PH001/ST002/plan_T104-PH001-ST002.md` |
| Reference | T102-PH001-ST005 plan (AC005 absorption) | `prompt/artifacts/tasks/T102/consultant/workspace/plan/plan_T102-PH001-ST005.md` |
| Reference | T102-PH001-ST002 plan (scope carve-out) | `prompt/artifacts/tasks/T102/consultant/workspace/plan/plan_T102-PH001-ST002.md` |
| Evidence | SES001 raw transcript | `prompt/artifacts/tasks/P/workspace/raw/PH000/ST001/raw_P-PH000-ST001-AC006-SES001.txt` |

---

## V. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-02-22 | Initial | Activity plan created per SES001 consultation. Fix-first/promote-clean methodology; absorbs T104-PH001-ST002-AC002, T102-PH001-ST005-AC005, and STD-005-specific scope from T102-PH001-ST002. Evidence: `raw_P-PH000-ST001-AC006-SES001.txt` |
