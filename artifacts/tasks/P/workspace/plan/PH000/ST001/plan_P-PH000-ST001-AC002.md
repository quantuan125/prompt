---
artifact_type: 'PLAN'
planning_level: 'ACTIVITY'
initiative_id: 'P'
initiative_code: 'PROGRAM'
phase: '0'
stream_id: 'P-PH000-ST001'
activity_id: 'P-PH000-ST001-AC002'
version: '0.2.0'
date: '2026-02-20'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
governance_rules: 'prompt/templates/consultant/workspace/workspace_documentation_rules.md'
procedural_guideline: 'prompt/templates/consultant/workspace/guideline_workspace_plan.md'
parent_plan: 'prompt/artifacts/tasks/P/workspace/plan/plan_P-PH000-ST001.md'
---

# PLAN: Program Governance (PROGRAM) — Phase 0 / Stream ST001 / Activity `P-PH000-ST001-AC002`: Author `P-STD-001` (Program Governance Standard)

## I. EXECUTIVE SUMMARY

**Purpose**: Establish `P-STD-001` as the program-authoritative standard by performing a full content promotion of `T102-STD-004` (Specification Standard & Guideline). All 29 CLAUSEs, 4 substandards, and 2 ADRs are transferred with 1:1 re-identification. A new `P-STD-001-CLAUSE-030` (Promotion/Demotion Lifecycle Governance) is authored. `T102-STD-004` is marked `superseded` with an alias window. Program-level guideline and template surfaces are aligned to `P-STD-001` authority.

**Non-goals**:
- This activity does not perform repo-wide remediation sweeps of existing `T102-STD-004-CLAUSE-*` references (these are covered by the alias window and migrated at next touch).
- This activity does not modify the contents of T102-STD-005 or any other T102 standard.

---

## II. ACTIVITY OUTLINE

**Activity ID**: `P-PH000-ST001-AC002`
**Objective**: Promote `T102-STD-004` to `P-STD-001` via full content transfer with 1:1 CLAUSE re-identification, add `CLAUSE-030` (Promotion/Demotion Lifecycle), mark `T102-STD-004` as `superseded` with alias window, and align program-level guideline/template ownership out of `T102` plans.
**Execution Mode**: `GATED-SEQUENTIAL`
**Depends On**: `P-PH000-ST001-AC001`, `T102-PH001-ST001-AC009.2-GATE-001`

**Context** (repo-relative paths expected to be touched by this activity):
- `prompt/artifacts/tasks/P/workspace/plan/plan_P-PH000-ST001.md`
- `prompt/artifacts/tasks/P/ssot/sps_P-PROGRAM.md`
- `prompt/artifacts/tasks/P/workspace/plan/PH000/ST001/plan_P-PH000-ST001-AC002.md`
- `prompt/artifacts/tasks/T102/consultant/workspace/plan/plan_T102-PH001-ST001.md`
- `prompt/artifacts/tasks/T102/consultant/standards/standard_T102-STD-004_specification-standard-and-guideline.md`
- `prompt/templates/consultant/standards/guideline_standard_specs.md`
- `prompt/templates/consultant/standards/template_standard_specs.md`

### Task Register

| Task | Task ID | Name | Status | Owner | Depends On | Target | Reference | Action |
|:--|:--|:--|:--|:--|:--|:--|:--|:--|
| TK001 | `P-PH000-ST001-AC002-TK001` | Create activity plan + wire navigation links | `completed` | LLM_Consultant | — | Plan + reference wiring | `guideline_workspace_plan.md` | Created activity plan and linked from P stream plan/SPS; rerouted T102 AC010 program-level surfaces (2026-02-19). |
| TK002 | `P-PH000-ST001-AC002-TK002` | Draft full promotion contract (content transfer scope + alias window + CLAUSE-030 spec + ADR-003 spec) | `planned` | LLM_Consultant | TK001 | Promotion contract (within this plan) | `T102-STD-005-CLAUSE-003A`, `analysis_P-PH000-ST001-AC002_promotion-methodology-comparison.md` | — |
| GATE-001 | `P-PH000-ST001-AC002-GATE-001` | Gate: Client approval of promotion contract + split boundary | `planned` | Client | TK002 | Pass/fail decision | `guideline_workspace_plan.md §VI` | — |
| TK003 | `P-PH000-ST001-AC002-TK003` | Author `P-STD-001` combined file (full 29-CLAUSE transfer + CLAUSE-030 + ADR-003) | `planned` | LLM_Consultant | GATE-001 | `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md` | `P-STD-001-CLAUSE-001A`, `P-STD-001-CLAUSE-018`, `P-STD-001-CLAUSE-025` | — |
| TK004 | `P-PH000-ST001-AC002-TK004` | Mark `T102-STD-004` as superseded + establish alias window | `planned` | LLM_Consultant | TK003 | `standard_T102-STD-004_specification-standard-and-guideline.md` | `T102-STD-005-CLAUSE-003A`, `T102-STD-005-CLAUSE-003B` | — |
| TK005 | `P-PH000-ST001-AC002-TK005` | Align program-level guideline + template to `P-STD-001` (migrate all CLAUSE refs, fix hardcoded paths, update authority chain) | `planned` | LLM_Consultant | TK003 | `prompt/templates/consultant/standards/` | `P-STD-001-CLAUSE-015A` (promoted), DEC006 | — |
| TK006 | `P-PH000-ST001-AC002-TK006` | Update Program SPS (`P-STD-001` row: status, canonical path, supersedes) | `planned` | LLM_Consultant | TK003 | `prompt/artifacts/tasks/P/ssot/sps_P-PROGRAM.md` | — | — |
| TK007 | `P-PH000-ST001-AC002-TK007` | Produce verification evidence for promotion + split completion | `planned` | LLM_Reviewer | TK004, TK005, TK006 | `prompt/artifacts/tasks/P/workspace/verification/` | Verification checklist (TBD) | — |

---

## III. TASKS (DETAILED)

### Task TK002: Draft Full Promotion Contract

**Task ID**: `P-PH000-ST001-AC002-TK002`

**Purpose**: Document the complete promotion contract so that TK003 execution is fully mechanical (no implementer decisions required).

**Deliverable**:
- A decision-complete promotion contract within this plan file enumerating: (i) source and target IDs, (ii) 1:1 CLAUSE re-identification mapping, (iii) new CLAUSE-030 specification, (iv) CLAUSE-015A variance, (v) alias window terms, (vi) ADR-003 decision record specification.

**Scope**:
- In scope:
  - Define full content transfer scope: all 29 CLAUSEs (CLAUSE-001 through CLAUSE-029), 4 substandards (A–D), 2 ADRs (ADR-001, ADR-002).
  - Specify new `P-STD-001-CLAUSE-030` (Promotion/Demotion Lifecycle Governance) content for Substandard B.
  - Specify new `P-STD-001-ADR-003` (Promotion Decision) content.
  - Define CLAUSE-015A variance: canonical directory is `prompt/artifacts/tasks/<SID>/standard/` (per DEC006; T102 `consultant/standards/` grandfathered).
  - Define alias window: scope covers all existing `T102-STD-004-CLAUSE-*` references; migration at next touch; alias support removed after dedicated governance sync changeset.
  - Define the "split boundary" for T102 AC010: program-level guideline/template owned by this activity; T102 AC010 retains SPS + STD-009 deprecation.
- Out of scope:
  - Repo-wide compliance enforcement or reference sweeps.

**Inputs Required**:
- `standard_T102-STD-004_specification-standard-and-guideline.md`
- `T102-STD-005_id-specification-rules.md` (CLAUSE-003A, CLAUSE-003B)
- `analysis_P-PH000-ST001-AC002_promotion-methodology-comparison.md`
- `sps_P-PROGRAM.md`

**Steps**:
1. Enumerate the complete CLAUSE re-identification mapping (29 CLAUSEs → 1:1).
2. Draft CLAUSE-030 normative text for Substandard B.
3. Draft ADR-003 body (Context, Decision, Alternatives, Consequences, Traceability).
4. Document CLAUSE-015A variance (directory + filename canonical forms).
5. Document alias window terms (scope, duration, migration rules).
6. Document AC010 split boundary.

**Success Criteria**:
- [ ] Promotion contract is decision-complete (no implementer decisions required for TK003).
- [ ] CLAUSE-030 text is normative-ready.
- [ ] ADR-003 body follows `P-STD-001-CLAUSE-025` template.
- [ ] CLAUSE-015A variance is explicit and grounded in DEC006.
- [ ] Alias window terms are explicit and reference T102-STD-005-CLAUSE-003B.

---

### Task TK003: Author P-STD-001 Combined File

**Task ID**: `P-PH000-ST001-AC002-TK003`

**Purpose**: Create the promoted program-level standard with full normative content.

**Deliverable**:
- `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md`

**Procedure** (see Step 3 of the implementation plan at `.claude/plans/plan_P-PH000-ST001-AC002-SES001_full-promotion-t102-std-004.md` for detailed instructions):
1. Copy full content of `standard_T102-STD-004_specification-standard-and-guideline.md`.
2. Perform systematic re-identification (all IDs, anchors, substandards).
3. Rewrite CLAUSE-015A for `<SID>/standard/` canonical form.
4. Insert CLAUSE-030 at end of Substandard B.
5. Add ADR-003 to Decision Record.
6. Update References with External Reference lines for T102-scoped IDs.
7. Rewrite Provenance with supersession lineage.

**Success Criteria**:
- [ ] File at correct path: `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md`
- [ ] 30 CLAUSEs present (29 transferred + CLAUSE-030).
- [ ] 3 ADRs present (ADR-001, ADR-002 transferred + ADR-003 new).
- [ ] 4 substandards re-identified (P-STD-001A through P-STD-001D).
- [ ] No residual `T102-STD-004` self-references (only in Provenance/External References).
- [ ] CLAUSE-015A updated per DEC006.
- [ ] Follows `P-STD-001-CLAUSE-001A` canonical structure.

---

### Task TK004: Mark T102-STD-004 as Superseded + Alias Window

**Task ID**: `P-PH000-ST001-AC002-TK004`

**Purpose**: Formally supersede the initiative-scoped standard and establish migration mechanics.

**Deliverable**:
- Updated `standard_T102-STD-004_specification-standard-and-guideline.md` with supersession notice and alias window.

**Success Criteria**:
- [ ] Supersession notice added immediately after heading.
- [ ] All normative content preserved (read-only historical artifact).
- [ ] Alias window terms documented.

---

### Task TK005: Align program-level guideline + template to P-STD-001

**Task ID**: `P-PH000-ST001-AC002-TK005`

**Purpose**: Migrate downstream authoring surfaces to reference the new program-level authority.

**Deliverables**:
- Updated `guideline_standard_specs.md` (v3.0.0 → v4.0.0)
- Updated `template_standard_specs.md`

**Success Criteria**:
- [ ] Zero residual `T102-STD-004-CLAUSE-*` references in guideline.
- [ ] Zero hardcoded `T102` paths in guideline.
- [ ] Authority chain (Section VII) references `P-STD-001`.
- [ ] Template comment line references `P-STD-001-CLAUSE-*`.

---

### Task TK006: Update Program SPS

**Task ID**: `P-PH000-ST001-AC002-TK006`

**Purpose**: Register P-STD-001 as an active standard in the program SPS.

**Deliverable**:
- Updated `sps_P-PROGRAM.md` P-STD-001 row.

**Success Criteria**:
- [ ] Status updated from `planned` to `draft`.
- [ ] Canonical path populated.
- [ ] Supersedes column shows `T102-STD-004`.

---

### Task TK007: Produce Verification Evidence

**Task ID**: `P-PH000-ST001-AC002-TK007`

**Purpose**: Document evidence that the promotion was executed per the contract.

**Deliverable**:
- Verification artifact at `prompt/artifacts/tasks/P/workspace/verification/`.

**Success Criteria**:
- [ ] Promotion checklist complete.
- [ ] All success criteria for TK003–TK006 verified.

---

## IV. LINKS REGISTER

| Link Type | Target | Path |
|:--|:--|:--|
| Plan (this file) | AC002 Activity Plan | `prompt/artifacts/tasks/P/workspace/plan/PH000/ST001/plan_P-PH000-ST001-AC002.md` |
| Plan | P Stream Plan | `prompt/artifacts/tasks/P/workspace/plan/plan_P-PH000-ST001.md` |
| SSOT | Program SPS | `prompt/artifacts/tasks/P/ssot/sps_P-PROGRAM.md` |
| Reference | Analysis (promotion methodology) | `prompt/artifacts/tasks/P/workspace/analysis/analysis_P-PH000-ST001-AC002_promotion-methodology-comparison.md` |
| Reference | Session Notes (SES001) | `prompt/artifacts/tasks/P/workspace/notes/PH000/ST001/notes_P-PH000-ST001-AC002-SES001.md` |
| Reference | T102-STD-004 (source standard) | `prompt/artifacts/tasks/T102/consultant/standards/standard_T102-STD-004_specification-standard-and-guideline.md` |
| Reference | T102-STD-005 (ID specification / promotion rules) | `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-005_id-specification-rules.md` |
| Reference | T104 Directory Convention (DEC006 source) | `prompt/artifacts/tasks/T104/workspace/PH001/ST002/proposal/proposal_T104-PH001-ST002-AC000_directory-naming-convention.md` |

---

## V. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v0.2.0 | 2026-02-20 | Major | Amended for full promotion methodology (SES001-DEC001). Key changes: (1) Executive summary reframed from adopt-by-reference to full content transfer; (2) Task register expanded: TK002 now covers full promotion contract, TK003 covers 29-CLAUSE transfer + CLAUSE-030 + ADR-003, new TK004 for T102-STD-004 supersession, TK005 expanded for full guideline/template migration, new TK006 for SPS update, TK007 for verification; (3) All task detail sections rewritten; (4) Links register expanded with analysis, session notes, and T102-STD-005 references. Source: `notes_P-PH000-ST001-AC002-SES001.md` |
| v0.1.0 | 2026-02-19 | Initial | Activity plan created to promote `T102-STD-004` authoring model into `P-STD-001` and split program-level surfaces out of `T102-PH001-ST001-AC010` |
