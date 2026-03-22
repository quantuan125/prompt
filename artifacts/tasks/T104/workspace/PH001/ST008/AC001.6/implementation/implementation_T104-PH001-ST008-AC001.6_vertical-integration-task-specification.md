---
artifact_type: 'IMPLEMENTATION'
implementation_type: 'task_specification'
initiative_id: 'T104'
initiative_code: 'CWS'
phase: '1'
stream_id: 'T104-PH001-ST008'
activity_id: 'T104-PH001-ST008-AC001.6'
task_id: 'T104-PH001-ST008-AC001.6-TK001'
version: '1.1.0'
date: '2026-03-22'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/plan_T104-PH001-ST008-AC001.6.md'
purpose: 'Preliminary vertical integration execution specification retained for AC001.6 lineage; downstream commissioning authority is superseded by later gate-specific and horizontal implementation artifacts.'
---

# IMPLEMENTATION (Task Specification): AC001.6 Phase 1 Vertical Integration Execution Specification

## I. PURPOSE & AUTHORITY

- **Purpose**: This artifact records the original Phase 1 execution framing for `T104-PH001-ST008-AC001.6`, covering the consultant-owned audit and gate-preparation work. The Phase 2 material remains preliminary expected scope only.
- **Authority chain**: Activity plan `T104-PH001-ST008-AC001.6` authorizes the work. This artifact is now a preliminary/context surface only. Downstream execution authority is governed by the finalized `GATE-001` proposal/GDR plus the later package-specific implementation artifacts (`TK003.4`, `TK003.5`, and the horizontal-development task specification).
- **Audience**: LLM_Consultant (Phase 1), LLM_Developer (Phase 2 only after GATE-001 and the later implementation specs), LLM_Reviewer (TK011)
- **This artifact does NOT hold a GDR.** Gate decisions are recorded in the gate-disposition proposals at `AC001.6/proposal/`.
- **Trigger**: Task complexity (TK002 multi-dimension audit + two-gate structure) exceeds plan-step capacity.

### Preliminary Authority Notice

- This artifact remains valid as historical planning context for the original AC001.6 framing.
- It is **not** the authoritative downstream commissioning surface after SES002-SES003, the external review, and the `TK003.4` / `TK003.5` package-normalization loop.
- When Phase 2 developer work is commissioned, the authoritative scope must be taken from:
  - the finalized `GATE-001` proposal/GDR,
  - `implementation_T104-PH001-ST008-AC001.6_gate-001-to-gate-002-orchestration-plan.md`,
  - `implementation_T104-PH001-ST008-AC001.6_horizontal-development-task-specification.md`,
  - the activity plan task register dependencies as normalized after remediation.
- Any conflict between this artifact and those later surfaces must be resolved in favor of the later surfaces.

---

## II. TASK SCOPE

- **Governing plan task**: `T104-PH001-ST008-AC001.6-TK001` (Activity plan creation - this spec feeds the Phase 1 authority surface and downstream package-preparation tasks)
- **Trigger**: AC001.3 GATE-002 closed with horizontal IMPLEMENTATION family delivery; full vertical integration and program-authority codification remain incomplete.
- **Deliverable contract**: See AC001.6 activity plan Task Register (TK001-TK003.5 and later gate-backed tasks), but treat this file as context-only for downstream commissioning once GATE-001 is normalized
- **Depends On**: `T104-PH001-ST008-AC001.3` (completed, GATE-002 approved 2026-03-20)

---

## III. CONTEXT & RATIONALE

AC001.3 delivered the IMPLEMENTATION artifact family **horizontally** — new surfaces (`guideline_workspace_implementation.md`, two templates) and three immediately adjacent vertical integration patches (plan, analysis, documentation rules). However:

1. Not all artifact family guidelines have been checked for IMPLEMENTATION cross-references
2. `P-STD-004` does not codify `implementation/` as an allowed activity-level subdirectory (CLAUSE-003D) and the prefix registry entry (CLAUSE-008A) needs verification
3. The structure validator rejects `implementation/` directories (`ACTIVITY_TYPE_DIRS` missing entry) and lacks prefix-to-directory alignment
4. The verification guideline still routes complex RECYCLE remediation through `revision-checklist` rather than the new `remediation_specification`
5. T104 SPS requirements (T104J-DEP-001, T104-CON-004, T104-QG-001) are not yet satisfied

**Decisions already approved** (from SES001 consultation):

| Decision | Detail |
|:--|:--|
| Scope placement | New AC001.6 under ST008 (NOT AC001.3 continuation) |
| Remediation architecture | Option B: `remediation_specification` replaces `revision-checklist` for complex RECYCLE. Hard deprecation with grandfathering of existing files |
| P-STD-004 authority | Program-level changes executed from AC001.6 with program-authority cross-reference note |
| GATE-001 granularity | Separate GIR items per gap category within a gate-disposition proposal |
| Audit scope | Includes live usage validation of existing IMPLEMENTATION artifacts |
| Architectural changes | Any architectural changes require a standards-input proposal subtype |
| Two-gate structure | Consultation-only GATE-001 (approve gap analysis) → implementation-backed GATE-002 (accept developer work) |

---

## IV. SPECIFICATION ITEMS — PHASE 1: CONSULTANT-OWNED → GATE-001

### SPEC-001 — Create AC001.6 Activity Plan + Stream Registration (TK001)

| Field | Detail |
|:--|:--|
| Requirement Source | SES001-DEC001; `guideline_workspace_plan.md` §IV.D |
| Template | `prompt/templates/consultant/workspace/template_workspace_plan_activity.md` |
| Output | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/plan_T104-PH001-ST008-AC001.6.md` |
| Implementation Detail | Instantiate the activity plan template with: `initiative_id: 'T104'`, `initiative_code: 'CWS'`, `phase: '1'`, `stream_id: 'T104-PH001-ST008'`, `activity_id: 'T104-PH001-ST008-AC001.6'`, `version: '1.0.0'`, `date: '2026-03-20'`, `parent_plan: 'prompt/artifacts/tasks/T104/workspace/PH001/ST008/plan_T104-PH001-ST008.md'`. Executive Summary: "Perform a definitive vertical integration audit of the IMPLEMENTATION artifact family across all workspace guidelines, program standards, and enforcement tooling, then implement all identified gaps." Non-goal: "This activity does not expand the IMPLEMENTATION family's two-subtype taxonomy or perform retroactive migration of existing remediation artifacts." Populate Task Register with TK001–GATE-002 sequence. Populate Links Register. Add changelog v1.0.0. |
| Concurrent Actions | (a) Add AC001.6 contract stub to `plan_T104-PH001-ST008.md` following the AC001.5 pattern (sub-activity section + Activity Register row). Bump stream plan version (minor). (b) Add AC001.6-SES001 row to `notes_T104-PH001-ST008.md` Activity Notes Register. Bump notes register version (minor). |
| Stream plan stub content | Trigger: AC001.3 GATE-002 approved but vertical integration incomplete. Purpose: definitive vertical integration audit then implement all gaps. Sub-Activity Plan link. Success Criteria: gap analysis exists, GATE-001 approves, all gaps implemented, GATE-002 closes. |
| Acceptance Criteria | Activity plan exists at canonical path; stream plan registers AC001.6 contract stub; notes register indexes SES001 |
| Status | `open` |

### SPEC-002 — Produce Vertical Integration Gap Analysis (TK002)

| Field | Detail |
|:--|:--|
| Requirement Source | SES001-DEC005; client comment |
| Template | `prompt/templates/consultant/workspace/guideline_workspace_analysis.md` |
| Output | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/analysis/analysis_T104-PH001-ST008-AC001.6_implementation-family-vertical-integration-audit.md` |
| Implementation Detail | Comprehensive ANALYSIS artifact covering six audit dimensions. See SPEC-002.A through SPEC-002.F below for dimension-level detail. |
| Acceptance Criteria | Findings table with columns (Finding ID, Dimension, Target File, Gap Description, Severity, Recommended Action). Each finding classified as architectural (→ standards-input proposal) or mechanical (→ direct implementation). Summary recommendation section. |
| Status | `open` |

**SPEC-002.A — Dimension A: Cross-Guideline Integration Audit**

Read each guideline and assess IMPLEMENTATION family references:

| Guideline | Version | Expected Integration | Gap? |
|:--|:--|:--|:--|
| `guideline_workspace_plan.md` | v1.16.0 | §IV.F (CONV-011) + §VI.L (gate-readiness stack) | None expected |
| `guideline_workspace_analysis.md` | v1.4.0 | §II (informative-only boundary) | None expected |
| `guideline_workspace_implementation.md` | v1.0.0 | N/A — this IS the family guideline | None expected |
| `guideline_workspace_verification.md` | v1.8.0 | Forward-ref to `remediation_specification` for complex RECYCLE; deprecation of `revision-checklist` | **Confirmed gap** |
| `guideline_workspace_dev-report.md` | v1.2.0 | Explicit IMPLEMENTATION-as-specification-input reference | **Potential gap — audit determines** |
| `guideline_workspace_proposal.md` | v1.6.0 | No reference needed (CONV-006 — by design) | None expected |
| `guideline_workspace_notes.md` | v1.1.0 | No reference needed (session records) | None expected |
| `guideline_workspace_roadmap.md` | v1.2.0 | No reference needed (thin-spine) | None expected |

**SPEC-002.B — Dimension B: workspace_documentation_rules.md Audit**

Check the following sections of `prompt/templates/consultant/workspace/workspace_documentation_rules.md` (v3.1.0):
- §3 Artifact Type Inventory: IMPLEMENTATION row completeness
- §4 Template Inventory: IMPLEMENTATION template registration
- §7.A Workflow Chain: verification→implementation handoff for complex RECYCLE
- §7.C Inter-Artifact Linkage: IMPLEMENTATION linkage rules
- §8 Role-to-Artifact Ownership Matrix: IMPLEMENTATION entries

**SPEC-002.C — Dimension C: P-Level Standards Audit**

| File | Check |
|:--|:--|
| `prompt/artifacts/tasks/P/standard/standard_P-STD-004_file-naming-and-directory-convention.md` | CLAUSE-003D: is `implementation/` in allowed activity-level subdirectories? CLAUSE-008A: is `implementation_` in prefix registry with complete naming pattern? |
| `prompt/artifacts/tasks/P/standard/standard_P-STD-005_universal-id-specification.md` | Is the `IID`/`IG` (Implementation Guidance) category distinct from the IMPLEMENTATION artifact family? Does this need clarification? |
| Any other P-STD files | Scan for IMPLEMENTATION references |

**SPEC-002.D — Dimension D: T104 SPS Initiative Considerations Audit**

Read `prompt/artifacts/tasks/T104/ssot/sps_T104-CWS.md` Section B and T104J epic entry. Check:
- T104-CON-004 (Prefix Discipline): Is `implementation_` prefix fully codified?
- T104-QG-001 (Deterministic Retrieval): Is retrieval blocked until validator accepts `implementation/`?
- T104J-DEP-001: Does it state P-STD-004 must codify `implementation_` and `<AC>/implementation/`? Is that now satisfied?
- T104J Feature Register FEAT-004 (IMPL-VERIF-LINK): Status `draft` — is verification-guideline linkage delivered or still pending?
- T104J-RISK-001 (Boundary ambiguity): Is mitigation complete across all relevant surfaces?

**SPEC-002.E — Dimension E: Validator & Test Suite Audit**

Read `prompt/scripts/validate_initiative_structure.py`:
- Check `ACTIVITY_TYPE_DIRS` for `"implementation"` entry
- Check `ACTIVITY_TYPE_PREFIX_ALIGNMENT` for `"implementation_"` → `"implementation"` mapping
- Check `ALLOWED_PREFIXES` for `"implementation_"` (expected present)
- Check `STREAM_TYPE_DIRS` for whether `implementation` is needed at stream level

Read `prompt/scripts/tests/test_validate_initiative_structure.py`:
- Check for existing `implementation`-related test cases

**SPEC-002.F — Dimension F: Live Usage Validation**

Locate all existing IMPLEMENTATION artifacts. Known paths:
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/implementation/implementation_P-PH000-ST001-AC009_gate-001-remediation-specification.md`
- `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.5/implementation/implementation_T104-PH001-ST008-AC001.5_consultant-recommendation-gdr.md`

Search for others: glob `prompt/**/implementation_*.md`

For each found artifact, check:
- Conformance to `guideline_workspace_implementation.md` frontmatter schema
- `implementation_type` value matches approved taxonomy (`remediation_specification` or `task_specification`)
- Template adherence
- Any guideline/template gaps surfaced by actual usage

### SPEC-003 — Author Standards-Input Proposal for Architectural Changes (TK002.1)

| Field | Detail |
|:--|:--|
| Requirement Source | SES001-DEC006 |
| Trigger | TK002 identifies architectural changes (expected: verification-guideline deprecation + forward-ref; documentation-rules workflow chain; dev-report integration boundary if confirmed) |
| Template | `prompt/templates/consultant/workspace/template_workspace_proposal_standards-input.md` |
| Output | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/proposal/proposal_T104-PH001-ST008-AC001.6_implementation-vertical-integration-architecture.md` |
| Implementation Detail | Package all ARCHITECTURAL findings from TK002 into a standards-input proposal. Include: Current State Summary (gap table, architectural findings only); Proposed Conventions (exact rule/wording for each architectural change); Decision Requests (one per architectural change); Impact and Risks (cross-reference effects). Expected architectural changes: (a) verification guideline deprecation rule for `revision-checklist` + forward-reference to `remediation_specification`; (b) documentation-rules workflow chain update for complex RECYCLE routing; (c) dev-report guideline IMPLEMENTATION-as-input reference if TK002 confirms gap. |
| Acceptance Criteria | Standards-input proposal exists at canonical path; all architectural findings from TK002 are covered; indexed in GATE-001 gate-disposition package |
| Status | `open` |

### SPEC-004 — Produce GATE-001 Gate-Disposition Proposal (TK003)

| Field | Detail |
|:--|:--|
| Requirement Source | SES001-DEC007 |
| Template | `prompt/templates/consultant/workspace/template_workspace_proposal_gate-disposition.md` |
| Output | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/proposal/proposal_T104-PH001-ST008-AC001.6-GATE-001_gir-disposition-package.md` |
| Implementation Detail | Separate GIR items per gap category: GIR-001 (verification guideline changes), GIR-002 (documentation rules workflow chain), GIR-003 (P-STD-004 directory and prefix codification), GIR-004 (validator and test suite alignment), GIR-005+ (any additional gaps from TK002). Each GIR: recommended option, alternative if any, rationale. GDR in pending state with `consultant_recommendation` field populated. Index analysis artifact and standards-input proposal in the gate package. |
| Acceptance Criteria | Gate-disposition proposal exists; all gap categories covered in separate GIRs; GDR in pending state |
| Status | `open` |

---

## V. SPECIFICATION ITEMS — PHASE 2: EXPECTED DEVELOPER-OWNED FOLLOW-ON

**Important**: Phase 2 tasks are determined by finalized `GATE-001` approval and later normalization artifacts. The specs below remain a **preliminary expected scope** based on SES001-era research only. Executing assistants MUST treat them as context unless the scope is reaffirmed by the normalized plan, the finalized `GATE-001` proposal/GDR, and the later AC001.6 implementation artifacts.

These items are not the final authority surface for developer execution. They are retained as expected follow-on slices until the gate-backed implementation specs and plan dependencies confirm them.

### SPEC-005 — Implement Verification Guideline Changes (TK004)

| Field | Detail |
|:--|:--|
| Requirement Source | SES001-DEC002; GATE-001 GIR-001 |
| Target | `prompt/templates/consultant/workspace/guideline_workspace_verification.md` (currently v1.8.0) |
| Implementation Detail | **§IV.A (Situation A — Deliverable Deficiency)**: Add deprecation notice: "For complex RECYCLE cases requiring detailed remediation planning, authors SHOULD use `IMPLEMENTATION remediation_specification` (see `guideline_workspace_implementation.md`). The `revision-checklist` supplementary file remains permitted for simple scope-decomposition but is NOT the recommended surface for complex remediation specification in new work." Add grandfathering clause: "Existing `revision-checklist` files (e.g., AC009, AC002) are grandfathered and do not require migration." **§VII.A (if exists — Supplementary Files)**: Update to reflect the deprecation and new routing. |
| Version | Minor bump (e.g., v1.9.0) |
| Changelog | Record the deprecation and forward-reference with source: `T104-PH001-ST008-AC001.6-GATE-001` |
| Acceptance Criteria | Deprecation notice exists for complex cases; forward-reference to `remediation_specification` present; grandfathering clause present; version bumped |
| Status | `open` |

### SPEC-006 — Implement workspace_documentation_rules.md Changes (TK005)

| Field | Detail |
|:--|:--|
| Requirement Source | GATE-001 GIR-002 |
| Target | `prompt/templates/consultant/workspace/workspace_documentation_rules.md` (currently v3.1.0) |
| Implementation Detail | **§7.A Workflow Chain**: Update the complex-RECYCLE routing to show: VERIFICATION (findings) → IMPLEMENTATION remediation_specification (remediation plan) → developer execution → DEV-REPORT → re-assessment VERIFICATION. Ensure the handoff from verification findings to implementation specification is explicit and traceable. |
| Version | Minor bump |
| Changelog | Record workflow chain update with source |
| Acceptance Criteria | Complex RECYCLE handoff chain is explicit in §7.A; no contradiction with existing workflow chain entries |
| Status | `open` |

### SPEC-007 — Implement P-STD-004 Changes (TK006)

| Field | Detail |
|:--|:--|
| Requirement Source | GATE-001 GIR-003; SES001-DEC003 |
| Target | `prompt/artifacts/tasks/P/standard/standard_P-STD-004_file-naming-and-directory-convention.md` |
| Implementation Detail | **CLAUSE-003D**: Add `implementation/` to the allowed activity-level type subdirectories list alongside `snotes/`, `raw/`, `verification/`, `dev-report/`, `proposal/`, `analysis/`. **CLAUSE-008A**: Verify `implementation_` entry exists with complete naming pattern. If missing or incomplete, add: `\| Implementation \| implementation_ \| implementation_<activity-UID>_<kebab-topic>.md \|`. Add program-authority cross-reference note: "Amendment source: T104-PH001-ST008-AC001.6". |
| Version | Appropriate version bump with changelog entry |
| Acceptance Criteria | `implementation/` in CLAUSE-003D allowed list; `implementation_` in CLAUSE-008A with complete naming pattern |
| Status | `open` |

### SPEC-008 — Implement P-STD-005 Changes (TK006.1 — conditional)

| Field | Detail |
|:--|:--|
| Requirement Source | GATE-001 GIR (if approved) |
| Trigger | Only if TK002 confirms the `IID`/`IG` vs IMPLEMENTATION disambiguation is needed and GATE-001 approves |
| Target | `prompt/artifacts/tasks/P/standard/standard_P-STD-005_universal-id-specification.md` |
| Implementation Detail | Add disambiguation note clarifying that `IID` category with `IG` token (Implementation Guidance) is an informative guidance family, distinct from the `IMPLEMENTATION` workspace artifact family governed by `guideline_workspace_implementation.md` and `P-STD-004`. |
| Acceptance Criteria | Disambiguation note exists; no ambiguity between IG token and IMPLEMENTATION artifact family |
| Status | `open` (conditional) |

### SPEC-009 — Implement Dev-Report Guideline Changes (TK007 — conditional)

| Field | Detail |
|:--|:--|
| Requirement Source | GATE-001 GIR (if approved) |
| Trigger | Only if TK002 confirms gap and GATE-001 approves |
| Target | `prompt/templates/consultant/workspace/guideline_workspace_dev-report.md` (currently v1.2.0) |
| Implementation Detail | Add explicit reference to IMPLEMENTATION artifacts as specification input when one exists. In §II or appropriate section: "When an IMPLEMENTATION artifact exists for the scope being reported, the DEV-REPORT SHOULD reference it as the specification input and trace deliverables back to the specification." |
| Version | Minor bump with changelog entry |
| Acceptance Criteria | IMPLEMENTATION-as-input reference exists; version bumped |
| Status | `open` (conditional) |

### SPEC-010 — Implement Validator Changes (TK008)

| Field | Detail |
|:--|:--|
| Requirement Source | GATE-001 GIR-004 |
| Target | `prompt/scripts/validate_initiative_structure.py` |
| Implementation Detail | (a) Add `"implementation"` to `ACTIVITY_TYPE_DIRS` set (currently around line 28). (b) Add `"implementation_": "implementation"` to `ACTIVITY_TYPE_PREFIX_ALIGNMENT` dict (currently around lines 29–31). (c) Verify `"implementation_"` is already in `ALLOWED_PREFIXES` tuple (expected at line ~47 — do not duplicate). (d) Check `STREAM_TYPE_DIRS` — `implementation` is likely NOT needed at stream level; confirm and leave unchanged unless TK002 finds otherwise. |
| Acceptance Criteria | `implementation` in `ACTIVITY_TYPE_DIRS`; `implementation_` → `implementation` in `ACTIVITY_TYPE_PREFIX_ALIGNMENT`; no `ALLOWED_PREFIXES` duplication |
| Status | `open` |

### SPEC-011 — Implement Test Changes (TK009)

| Field | Detail |
|:--|:--|
| Requirement Source | GATE-001 GIR-004 |
| Target | `prompt/scripts/tests/test_validate_initiative_structure.py` |
| Implementation Detail | Add the following test cases: (a) `implementation/` directory accepted at activity level; (b) `implementation_` prefix accepted and aligned to `implementation/` directory via `ACTIVITY_TYPE_PREFIX_ALIGNMENT`; (c) regression test confirming existing directory validations still pass. Run full test suite: `cd prompt && python -m pytest scripts/tests/test_validate_initiative_structure.py -v`. All tests must pass before TK010 DEV-REPORT can begin. |
| Acceptance Criteria | All three new test cases exist; full test suite passes with no regressions |
| Status | `open` |

### SPEC-012 — Produce DEV-REPORT (TK010)

| Field | Detail |
|:--|:--|
| Requirement Source | `guideline_workspace_dev-report.md` |
| Output | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/dev-report/dev-report_T104-PH001-ST008-AC001.6_implementation-vertical-integration.md` |
| Implementation Detail | Record all file changes from TK004–TK009 with before/after version numbers. Include cross-validation checklist mapping each change back to its GATE-001 GIR item. Record test execution results (pytest output). Flag any deviations from the approved GATE-001 scope. |
| Acceptance Criteria | DEV-REPORT covers all governed-file changes; cross-validation checklist maps to GATE-001 GIR items; test results included |
| Status | `open` |

### SPEC-013 — Produce GATE-002 Verification (TK011)

| Field | Detail |
|:--|:--|
| Requirement Source | `guideline_workspace_verification.md` |
| Output | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/verification/verification_T104-PH001-ST008-AC001.6_gate-002.md` |
| Implementation Detail | Independently verify each change against the approved GATE-001 GIR items. Check for cross-surface consistency (no contradictions between amended guidelines). Verify validator passes with new changes. Record findings with severity classification (Situation A or B). Produce verdict: PASS / PASS WITH DEFERRALS / RECYCLE. |
| Acceptance Criteria | Verification covers all GATE-001 approved GIR items; findings clearly classified; verdict recorded |
| Status | `open` |

### SPEC-014 — Produce GATE-002 Gate-Disposition Proposal (TK012)

| Field | Detail |
|:--|:--|
| Requirement Source | `guideline_workspace_proposal.md` |
| Output | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/proposal/proposal_T104-PH001-ST008-AC001.6-GATE-002_gir-disposition-package.md` |
| Implementation Detail | Package DEV-REPORT and VERIFICATION into client-facing acceptance surface. GIR items map 1:1 to GATE-001 approved items (showing implementation status for each). GDR in pending state for client decision. |
| Acceptance Criteria | Gate-disposition proposal exists; GIR items correspond to GATE-001 approved scope; GDR pending |
| Status | `open` |

---

## VI. IMPLEMENTATION SEQUENCE

```
Phase 1 (Consultant-owned)
  SPEC-001  TK001   Create AC001.6 plan + stream registration
  SPEC-002  TK002   Vertical integration gap analysis (6 dimensions)
  SPEC-003  TK002.1 Standards-input proposal for architectural changes
  SPEC-004  TK003   GATE-001 gate-disposition proposal
              ── GATE-001 (Client decision) ──

Phase 2 (Developer-owned, scope confirmed by GATE-001)
  SPEC-005  TK004   Verification guideline changes
  SPEC-006  TK005   Documentation rules changes
  SPEC-007  TK006   P-STD-004 changes
  SPEC-008  TK006.1 P-STD-005 changes (conditional)
  SPEC-009  TK007   Dev-report guideline changes (conditional)
  SPEC-010  TK008   Validator changes
  SPEC-011  TK009   Test changes (depends on TK008)
  SPEC-012  TK010   DEV-REPORT
  SPEC-013  TK011   GATE-002 verification (Reviewer)
  SPEC-014  TK012   GATE-002 gate-disposition proposal
              ── GATE-002 (Client decision) ──
```

**Parallelism note**: TK004–TK009 (Phase 2 implementation tasks) may be executed in parallel within a single developer session. TK010 (DEV-REPORT) depends on all of TK004–TK009 completing. TK011 (Verification) depends on TK010.

---

## VII. TARGET FILES REGISTER

| # | File Path | Authority | Change Type | Phase | Confirmed? |
|:--|:--|:--|:--|:--|:--|
| 1 | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/plan_T104-PH001-ST008-AC001.6.md` | T104 | Create | 1 | Yes |
| 2 | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/plan_T104-PH001-ST008.md` | T104 | Amend (AC001.6 stub) | 1 | Yes |
| 3 | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/notes_T104-PH001-ST008.md` | T104 | Amend (register entry) | 1 | Yes |
| 4 | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/analysis/analysis_T104-PH001-ST008-AC001.6_implementation-family-vertical-integration-audit.md` | T104 | Create | 1 | Yes |
| 5 | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/proposal/proposal_T104-PH001-ST008-AC001.6_implementation-vertical-integration-architecture.md` | T104 | Create (standards-input) | 1 | Yes |
| 6 | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/proposal/proposal_T104-PH001-ST008-AC001.6-GATE-001_gir-disposition-package.md` | T104 | Create | 1 | Yes |
| 7 | `prompt/templates/consultant/workspace/guideline_workspace_verification.md` | T104 | Amend (deprecation + forward-ref) | 2 | Yes |
| 8 | `prompt/templates/consultant/workspace/workspace_documentation_rules.md` | T104 | Amend (workflow chain) | 2 | Yes |
| 9 | `prompt/artifacts/tasks/P/standard/standard_P-STD-004_file-naming-and-directory-convention.md` | Program (P) | Amend (CLAUSE-003D + 008A) | 2 | Yes |
| 10 | `prompt/scripts/validate_initiative_structure.py` | Program (P) | Code change | 2 | Yes |
| 11 | `prompt/scripts/tests/test_validate_initiative_structure.py` | Program (P) | Code change | 2 | Yes |
| 12 | `prompt/artifacts/tasks/P/standard/standard_P-STD-005_universal-id-specification.md` | Program (P) | Amend (conditional) | 2 | TBD by TK002 |
| 13 | `prompt/templates/consultant/workspace/guideline_workspace_dev-report.md` | T104 | Amend (conditional) | 2 | TBD by TK002 |
| 14 | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/dev-report/dev-report_T104-PH001-ST008-AC001.6_implementation-vertical-integration.md` | T104 | Create | 2 | Yes |
| 15 | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/verification/verification_T104-PH001-ST008-AC001.6_gate-002.md` | T104 | Create | 2 | Yes |
| 16 | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/proposal/proposal_T104-PH001-ST008-AC001.6-GATE-002_gir-disposition-package.md` | T104 | Create | 2 | Yes |

---

## VIII. REFERENCES

| Document | Path |
|:--|:--|
| Governing Plan | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/plan_T104-PH001-ST008-AC001.6.md` |
| AC001.3 Plan | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.3/plan_T104-PH001-ST008-AC001.3.md` |
| SES001 Session Notes | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/snotes/snotes_T104-PH001-ST008-AC001.6-SES001.md` |
| External Consultant Brief | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/communication/comm_T104-PH001-ST008-AC001.3_external-consultant-second-opinion_post-gate-002-scope-and-remediation-architecture.md` |
| ST008 Stream Plan | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/plan_T104-PH001-ST008.md` |
| ST008 Notes Register | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/notes_T104-PH001-ST008.md` |
| T104 SPS | `prompt/artifacts/tasks/T104/ssot/sps_T104-CWS.md` |
| Implementation Guideline | `prompt/templates/consultant/workspace/guideline_workspace_implementation.md` |
| Activity Plan Template | `prompt/templates/consultant/workspace/template_workspace_plan_activity.md` |
| Gate-Disposition Template | `prompt/templates/consultant/workspace/template_workspace_proposal_gate-disposition.md` |
| Standards-Input Template | `prompt/templates/consultant/workspace/template_workspace_proposal_standards-input.md` |
| Working Draft (external) | `.claude/plans/plan_T104-PH001-ST008-AC001.6_implementation-family-vertical-integration.md` |

---

## IX. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.1.0 | 2026-03-22 | Amendment | Reclassified this artifact as preliminary/context-only for downstream commissioning after the TK003.4/TK003.5 normalization loop. Added an explicit authority notice directing executors to the finalized GATE-001 package, orchestration plan, horizontal-development task specification, and normalized plan as the authoritative downstream surfaces. |
| v1.0.0 | 2026-03-20 | Initial | Task specification for AC001.6 full execution. Covers Phase 1 (consultant-owned vertical integration audit → GATE-001, SPEC-001 through SPEC-004) and Phase 2 (developer-owned implementation → GATE-002, SPEC-005 through SPEC-014). Source: SES001 consultation decisions. |
