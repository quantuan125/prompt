---
artifact_type: 'PLAN'
planning_level: 'ACTIVITY'
initiative_id: 'P'
initiative_code: 'PROGRAM'
phase: '0'
stream_id: 'P-PH000-ST002'
activity_id: 'P-PH000-ST002-AC007'
version: '1.0.0'
date: '2026-04-02'
status: 'planned'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
governance_rules: 'prompt/templates/consultant/workspace/workspace_documentation_rules.md'
procedural_guideline: 'prompt/templates/consultant/workspace/guideline_workspace_plan.md'
parent_plan: 'prompt/artifacts/tasks/P/workspace/PH000/ST002/plan_P-PH000-ST002.md'
---

# PLAN: P (PROGRAM) - Phase 0 / Stream ST002 / Activity `P-PH000-ST002-AC007`: V1 Status System Operational Stabilization

## I. EXECUTIVE SUMMARY

**Purpose**: Address the V1 operational gaps identified during the AC006 GATE-002 review and the SES007 QA consultation. This activity stabilizes the already-delivered session-close skill (`prompt/skills/session-close/SKILL.md`) and briefing dashboard (`prompt/artifacts/tasks/P/status/briefing_program.md`) so the V1 status system operates reliably before AC005 commissions the T105 initiative for V2 productization.

**Non-goal**: Do not introduce new features, new derived surfaces, automation, scripts, browser/app UI, or next-step advisor skills. All such enhancements are explicitly deferred to T105 requirements governance. AC007 is strictly a stabilization pass for operational gaps in already-delivered V1 surfaces.

**Origin**: This activity was commissioned during SES007 (2026-04-02) after the client approved GATE-002 for AC006 and the consultant identified operational gaps that would cause V1 to silently degrade without intervention. The client approved the split-path approach: AC007 for V1 operational gaps, T105 (via AC005) for enhancements. See `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/snotes/snotes_P-PH000-ST002-AC006-SES007.md` for the full decision record.

---

## II. ACTIVITY OUTLINE

**Activity ID**: `P-PH000-ST002-AC007`
**Objective**: Stabilize the V1 status system by closing the four operational gaps identified during AC006 GATE-002 review: (1) session-close skill does not explicitly reference the briefing dashboard for reconciliation, (2) no staleness threshold or inclusion/exclusion rules govern the briefing, (3) the Active Work Briefing table lacks a scope-type ID column for filtering, and (4) the V1 three-file status architecture is not formally documented.
**Execution Mode**: `GATED`
**Depends On**: `P-PH000-ST002-AC006`

**Context**:
- `prompt/skills/session-close/SKILL.md`
- `prompt/artifacts/tasks/P/status/briefing_program.md`
- `prompt/artifacts/tasks/P/status/status_program.yaml`
- `prompt/artifacts/tasks/P/status/status_program.md`
- `prompt/artifacts/tasks/P/standard/standard_P-STD-002_program-status-standard.md`
- `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/plan_P-PH000-ST002-AC006.md`
- `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/snotes/snotes_P-PH000-ST002-AC006-SES007.md`
- `prompt/templates/consultant/workspace/guideline_workspace_plan.md`
- `prompt/templates/consultant/workspace/guideline_workspace_analysis.md`
- `prompt/templates/consultant/workspace/guideline_workspace_proposal.md`
- `prompt/templates/consultant/workspace/guideline_workspace_implementation.md`

### Task Register

| Task | Task ID | Name | Status | Owner | Depends On | Target | Reference | Action |
|:--|:--|:--|:--|:--|:--|:--|:--|:--|
| TK001 | `P-PH000-ST002-AC007-TK001` | V1 operational gap assessment | `planned` | LLM_Consultant | `P-PH000-ST002-AC006` | `analysis/` | `guideline_workspace_analysis.md` | â€” |
| TK002 | `P-PH000-ST002-AC007-TK002` | Stabilization scope proposal | `planned` | LLM_Consultant | TK001 | `proposal/` | `guideline_workspace_proposal.md` | â€” |
| GATE-001 | `P-PH000-ST002-AC007-GATE-001` | Gate: client approval of V1 stabilization scope | `planned` | Client | TK002 | `GDR` | `guideline_workspace_proposal.md` | â€” |
| TK003 | `P-PH000-ST002-AC007-TK003` | Execute approved V1 stabilization | `planned` | LLM_Developer | GATE-001 | `prompt/skills/session-close/`, `prompt/artifacts/tasks/P/status/` | `guideline_workspace_implementation.md` | â€” |
| TK004 | `P-PH000-ST002-AC007-TK004` | Verification and evidence package | `planned` | LLM_Consultant | TK003 | `verification/` | `guideline_workspace_verification.md` | â€” |
| GATE-002 | `P-PH000-ST002-AC007-GATE-002` | Gate: client acceptance of V1 stabilization output | `planned` | Client | TK004 | `GDR` | `guideline_workspace_proposal.md` | â€” |

**Gate Model**: GATE-001 is a consultation gate. No implementation begins until the client approves the stabilization scope. GATE-002 is an execution-evidence acceptance gate. AC007 closes only after the client accepts the stabilization output.

---

## III. TASKS (DETAILED)

### Task TK001: V1 Operational Gap Assessment

**Task ID**: `P-PH000-ST002-AC007-TK001`

**Purpose**: Formally document the four operational gaps identified during the AC006 GATE-002 review (SES007 QA) and assess whether any additional V1 gaps have emerged since AC006 delivery. Produce a bounded analysis artifact that defines the exact stabilization boundary.

**Deliverable**:
- `analysis/analysis_P-PH000-ST002-AC007_v1-operational-gap-assessment.md`

**Inputs Required**:
- `prompt/skills/session-close/SKILL.md`
- `prompt/artifacts/tasks/P/status/briefing_program.md`
- `prompt/artifacts/tasks/P/status/status_program.yaml`
- `prompt/artifacts/tasks/P/status/status_program.md`
- `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/snotes/snotes_P-PH000-ST002-AC006-SES007.md`
- `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/analysis/analysis_P-PH000-ST002-AC006-GATE-002_external-review-and-downstream-readiness-assessment.md`

**Scope**:
- In scope:
  - Formal gap register covering: (a) session-close skill missing briefing reconciliation, (b) no staleness/inclusion/exclusion governance for briefing, (c) missing scope-type column, (d) undocumented V1 architecture
  - Assessment of whether additional V1 gaps exist beyond the four already identified
  - Clear boundary statement distinguishing V1 stabilization from V2 enhancement
- Out of scope:
  - Proposing V2 features (next-step awareness, scripts, UI)
  - Modifying any delivered file
  - Reopening AC006 scope

**Success Criteria**:
- [ ] Gap register is explicit and file-grounded
- [ ] Each gap has a clear remediation target and acceptance criterion
- [ ] V1 vs V2 boundary is explicit
- [ ] No V2 enhancement items are included in the stabilization scope

### Task TK002: Stabilization Scope Proposal

**Task ID**: `P-PH000-ST002-AC007-TK002`

**Purpose**: Package the V1 stabilization scope for client disposition before any implementation begins. Present the four identified gaps as GIR items with recommended remediation paths.

**Deliverable**:
- `proposal/proposal_P-PH000-ST002-AC007-GATE-001_v1-stabilization-scope-disposition.md`

**Inputs Required**:
- `analysis/analysis_P-PH000-ST002-AC007_v1-operational-gap-assessment.md`

**Scope**:
- In scope:
  - GIR items for each approved stabilization gap
  - Clear implementation-spec commissioning path for post-GATE-001 execution
  - Explicit exclusion list for items deferred to T105
- Out of scope:
  - Implementation-spec authoring (that is post-GATE-001)
  - Any file modification outside the proposal

**Success Criteria**:
- [ ] Client can approve or reject each stabilization gap individually
- [ ] Exclusion list for T105-deferred items is explicit
- [ ] Downstream implementation path is defined

### GATE-001: Client Approval of V1 Stabilization Scope

**Gate ID**: `P-PH000-ST002-AC007-GATE-001`

**Entry Criteria**:
- TK001 and TK002 are complete
- The stabilization scope is bounded and explicit
- The V2 exclusion list is explicit

**Exit Criteria**:
- Client records the decision in the GDR
- TK003 remains blocked unless the gate records an approving decision

**Gate-Disposition Proposal**: `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC007/proposal/proposal_P-PH000-ST002-AC007-GATE-001_v1-stabilization-scope-disposition.md`

### Task TK003: Execute Approved V1 Stabilization

**Task ID**: `P-PH000-ST002-AC007-TK003`

**Purpose**: Implement the client-approved stabilization items. Expected scope (subject to GATE-001 approval):
- Amend the session-close skill to add an explicit `briefing_program.md` reconciliation check
- Add staleness threshold (7-day rule per CLAUSE-038 alignment), inclusion rules (all `in_progress` activities appear), and exclusion rules (completed items move to Recent Movement for one cycle then drop off) to the briefing dashboard governance
- Add a `Scope` column to the Active Work Briefing table
- Author a formal V1 architecture note documenting the three-file relationship and update workflow

**Deliverable**:
- Updated `prompt/skills/session-close/SKILL.md`
- Updated `prompt/artifacts/tasks/P/status/briefing_program.md`
- Architecture documentation (location TBD based on GATE-001 approval)

**Scope**:
- In scope: Only the items approved at GATE-001
- Out of scope: Anything rejected at GATE-001 or anything on the T105 exclusion list

**Success Criteria**:
- [ ] Each approved gap is remediated in the target file(s)
- [ ] No unapproved changes are introduced
- [ ] All validation checks from the implementation spec are passing

### Task TK004: Verification and Evidence Package

**Task ID**: `P-PH000-ST002-AC007-TK004`

**Purpose**: Verify the TK003 implementation against the approved stabilization scope and produce the execution-evidence package for GATE-002 intake.

**Deliverable**:
- `verification/verification_P-PH000-ST002-AC007_gate-002.md`

**Scope**:
- In scope: Verification of all TK003 deliverables against GATE-001-approved scope
- Out of scope: Re-verifying AC006 deliverables

**Success Criteria**:
- [ ] All approved gaps verified as remediated
- [ ] No unapproved scope additions detected
- [ ] Verdict recorded

### GATE-002: Client Acceptance of V1 Stabilization Output

**Gate ID**: `P-PH000-ST002-AC007-GATE-002`

**Entry Criteria**:
- TK003 and TK004 are complete
- Verification verdict supports closure

**Exit Criteria**:
- Client records the decision in the GDR
- If APPROVE, AC007 closes and AC005 is unblocked
- If RECYCLE, remediation follows standard recycle-loop rules

**Gate-Disposition Proposal**: `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC007/proposal/proposal_P-PH000-ST002-AC007-GATE-002_v1-stabilization-output-disposition.md`

---

## IV. LINKS REGISTER

| Link Type | Target | Path |
|:--|:--|:--|
| Parent Plan | ST002 Stream Plan | `prompt/artifacts/tasks/P/workspace/PH000/ST002/plan_P-PH000-ST002.md` |
| Plan (this file) | AC007 Activity Plan | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC007/plan_P-PH000-ST002-AC007.md` |
| Upstream Activity | AC006 Activity Plan | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/plan_P-PH000-ST002-AC006.md` |
| Downstream Activity | AC005 Activity Plan | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC005/plan_P-PH000-ST002-AC005.md` |
| Origin Session | SES007 Session Notes | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/snotes/snotes_P-PH000-ST002-AC006-SES007.md` |
| Phase Plan | PH000 Phase Plan | `prompt/artifacts/tasks/P/workspace/PH000/plan_P-PH000.md` |

---

## V. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-04-02 | Initial | Created AC007 activity plan for V1 Status System Operational Stabilization. Defines bounded scope covering four operational gaps (session-close briefing check, staleness governance, scope-type column, V1 architecture documentation) with explicit T105 exclusion list. Commissioned during SES007 after AC006 GATE-002 approval. |
