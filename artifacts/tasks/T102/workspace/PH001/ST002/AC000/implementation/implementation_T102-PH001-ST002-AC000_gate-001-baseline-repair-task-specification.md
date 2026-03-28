---
artifact_type: 'IMPLEMENTATION'
implementation_type: 'task_specification'
initiative_id: 'T102'
initiative_code: 'CWD'
phase: '1'
stream_id: 'T102-PH001-ST002'
activity_id: 'T102-PH001-ST002-AC000'
task_id: 'T102-PH001-ST002-AC000 (GATE-001 baseline repair scope)'
version: '1.0.0'
date: '2026-03-28'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/plan_T102-PH001-ST002-AC000.md'
execution_audience: 'consultant'
purpose: 'Detailed implementation specification for the AC000 GATE-001 planning-baseline repair: make the activity plan internally consistent as a consultation-only gate package, normalize TK007 pathing, and align the ST002 stream stub before consultant-owned diagnostic deliverables are authored'
---

# IMPLEMENTATION (Task Specification): AC000 GATE-001 Baseline Repair

## I. PURPOSE & AUTHORITY

- **Purpose**: This artifact specifies the exact file mutations required to repair the AC000 planning baseline before any GATE-001 package authoring proceeds. The scope covers five logical actions: (S1) reframe AC000 so `TK006` is a diagnostic assessment input to `GATE-001` rather than a pre-gate mutation task; (S2) normalize the calibrated scope brief path into the `analysis/` directory and update all dependent references; (S3) align `TK007`, `TK008`, `TK009`, `GATE-001`, and `TK010` semantics with the approved two-gate model; (S4) mark `TK000` completed and normalize placeholder register cells; (S5) align the ST002 stream-plan AC000 stub with the repaired activity plan.
- **Authority chain**: The governing activity plan (`plan_T102-PH001-ST002-AC000.md`) authorizes the AC000 planning surface. This artifact specifies HOW the baseline repair is executed. Consultant-owned diagnostic deliverables (`TK001`-`TK009`) are authored only after this repair is executed and reviewed.
- **Audience**: `LLM_Consultant` (`execution_audience: consultant`). This is consultant-owned planning work delegated to a consultant-commissioned assistant. No developer execution or dev-report is involved.
- This artifact does NOT hold a GDR. Gate decisions remain in gate-disposition proposals.

## II. TASK SCOPE

- **Governing plan scope**: `T102-PH001-ST002-AC000` pre-GATE-001 planning-baseline repair
- **Trigger**: Task complexity exceeds plan-step capacity. Two plan surfaces must be edited with precise sequencing, dependency, path, and gate-semantics corrections. The activity plan contains multiple cross-referenced contradictions that must be repaired in one coherent changeset.
- **Deliverable contract**: (1) repaired AC000 activity plan, (2) aligned ST002 stream-plan AC000 stub, (3) no remaining blocking contradiction preventing consultant-owned GATE-001 package authoring.

## III. SPECIFICATION ITEMS

### SPEC-001 — Repair AC000 executive framing, task register, and changelog posture

| Field | Detail |
|:--|:--|
| Requirement Source | Approved Repair-First orchestration. AC000 currently states `GATE-001` is consultation-only while also encoding `TK006` as a pre-gate mutation and using non-canonical placeholder cells. |
| Target file(s) | `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/plan_T102-PH001-ST002-AC000.md` |
| Required end-state posture | Frontmatter version/date reflect the amendment; executive summary and objective distinguish GATE-001 assessment from GATE-002 implementation; task register uses `—` for empty placeholder cells; `TK000` is `completed` with a concise Action; `TK006` remains before `TK007` but is recast as a diagnostic assessment task; `TK007` depends on `TK006` as an assessment input, not a completed mutation; `GATE-001` remains consultation-only. |
| Explicit non-target / do-not-change constraints | Do NOT remove `TK006`. Do NOT alter the existence or order of `TK010`-`TK015` / `GATE-002`. Do NOT add `SES003`. Do NOT edit any standard file paths outside the two plan files. |
| Validation check | (1) frontmatter is `version: '2.1.0'` and `date: '2026-03-28'`; (2) task register shows `TK000` as `completed`; (3) `TK006` row name no longer says housekeeping mutation; (4) all empty `Depends On` / `Action` placeholders in the task register use `—`; (5) no task before `GATE-001` implies a required pre-gate STD mutation. |
| Blocking ambiguity rule | If the current AC000 plan differs materially from the text quoted below, stop and re-read the file before editing. Do not infer additional restructuring beyond the exact replacements in this artifact. |
| Status | `open` |

#### Implementation Detail

**Step 1: Update frontmatter**

Change:
```yaml
version: '2.0.0'
date: '2026-03-28'
```
to:
```yaml
version: '2.1.0'
date: '2026-03-28'
```

**Step 2: Replace the Executive Summary purpose/non-goal block**

Replace:
```markdown
**Purpose**: Verify that ST005's research-driven CLAUSE amendments (from RES-004, RES-005, RES-006 integration analyses) were correctly applied to the four targeted T102-STDs; assess all T102-STD files against P-STD-001 structural conformance requirements; perform T102-STD-004 supersession housekeeping; and produce a calibrated scope brief that governs AC001-AC004 execution focus.

**Non-goal**: This activity does NOT perform structural remediation of T102-STDs (AC001 scope), draft verification contracts (AC002), or modify SSOT artifacts (AC004). The diagnostic and calibration work (TK001–TK007) is reviewed at GATE-001 (consultation-only). The bounded T102-STD-004 supersession housekeeping (TK006) and any content remediation seeded by GATE-001 findings are reviewed at GATE-002 (implementation-backed).
```
with:
```markdown
**Purpose**: Verify that ST005's research-driven CLAUSE amendments (from RES-004, RES-005, RES-006 integration analyses) were correctly applied to the four targeted T102-STDs; assess all T102-STD files against P-STD-001 structural conformance requirements; assess the current supersession posture of T102-STD-004 against the P-STD-001 baseline; and produce a calibrated scope brief that governs AC001-AC004 execution focus.

**Non-goal**: This activity does NOT perform structural remediation of T102-STDs (AC001 scope), draft verification contracts (AC002), or modify SSOT artifacts (AC004) before GATE-001. The diagnostic and calibration work (TK001–TK007) is reviewed at GATE-001 as a consultation-only gate. Any bounded T102-STD-004 housekeeping mutation and any content remediation seeded by GATE-001 findings remain post-GATE-001 implementation work and are reviewed at GATE-002.
```

**Step 3: Replace the Objective line**

Replace:
```markdown
**Objective**: Establish a verified content baseline and structural gap inventory for the T102-STD set (GATE-001); execute bounded supersession housekeeping and content remediation (GATE-002); and produce a calibrated scope brief that enables AC001-AC004 to proceed with precise focus.
```
with:
```markdown
**Objective**: Establish a verified content baseline, structural gap inventory, and supersession current-state assessment for the T102-STD set (GATE-001); then use the approved diagnostic package to drive bounded post-gate housekeeping and any in-scope content remediation at GATE-002.
```

**Step 4: Replace the entire Task Register table**

Replace the current Task Register table with:
```markdown
| Task | Task ID | Name | Status | Owner | Depends On | Target | Reference | Action |
|:--|:--|:--|:--|:--|:--|:--|:--|:--|
| TK000 | `T102-PH001-ST002-AC000-TK000` | Plan Readiness Assessment & Commission | `completed` | LLM_Consultant | `—` | Activity plan + guidelines | This session notes | Baseline repaired for consultation-only GATE-001 packaging; TK006 reframed as diagnostic assessment input and pathing normalized. |
| TK001 | `T102-PH001-ST002-AC000-TK001` | Verify STD-007 amendments (RES-004 Deltas 1-4 + RES-006 D1) | `planned` | LLM_Consultant | TK000 | `standard_T102-STD-007_issues-risks-index.md` | ST005-AC001 task descriptions | `—` |
| TK002 | `T102-PH001-ST002-AC000-TK002` | Verify STD-003 amendments (RES-005 Deltas A1-A4) | `planned` | LLM_Consultant | TK000 | `standard_T102-STD-003_explicit-inheritance-model.md` | ST005-AC002 task descriptions | `—` |
| TK003 | `T102-PH001-ST002-AC000-TK003` | Verify STD-006 amendments (RES-005 Deltas B1-B4 + RES-006 C1) | `planned` | LLM_Consultant | TK000 | `standard_T102-STD-006_research-artifacts-index.md` | ST005-AC003 task descriptions | `—` |
| TK004 | `T102-PH001-ST002-AC000-TK004` | Verify STD-001 amendments (RES-006 Deltas A1-A5, absorbs RES-005 D1-D2) | `planned` | LLM_Consultant | TK000 | `standard_T102-STD-001_consultancy-operating-model.md` | ST005-AC004 task descriptions | `—` |
| TK005 | `T102-PH001-ST002-AC000-TK005` | P-STD-001 structural gap assessment (all T102-STDs) | `planned` | LLM_Consultant | TK001, TK002, TK003, TK004 | All `standard_T102-STD-*.md` files | P-STD-001 | `—` |
| TK006 | `T102-PH001-ST002-AC000-TK006` | Assess T102-STD-004 supersession current state & residual housekeeping scope | `planned` | LLM_Consultant | TK000 | `standard_T102-STD-004_specification-standard-and-guideline.md` | P-STD-001 `supersedes` field + current file state | `—` |
| TK007 | `T102-PH001-ST002-AC000-TK007` | Produce calibrated scope brief for AC001-AC004 | `planned` | LLM_Consultant | TK001, TK002, TK003, TK004, TK005, TK006 | `analysis/analysis_T102-PH001-ST002-AC000_calibrated-scope-brief.md` | `guideline_workspace_analysis.md` | `—` |
| TK008 | `T102-PH001-ST002-AC000-TK008` | Produce GATE-001 gate-disposition proposal | `planned` | LLM_Consultant | TK007 | `proposal/` | `guideline_workspace_proposal.md` | `—` |
| TK009 | `T102-PH001-ST002-AC000-TK009` | Produce GATE-001 external review | `planned` | LLM_Subconsultant | TK008 | `analysis/` | `guideline_workspace_analysis.md` §IV.B | `—` |
| GATE-001 | `T102-PH001-ST002-AC000-GATE-001` | Gate: Client approval of AC000 diagnostic deliverables | `planned` | Client | TK009 | Pass/fail | `guideline_workspace_plan.md` §VI.L | `—` |
| TK010 | `T102-PH001-ST002-AC000-TK010` | Author implementation spec for post-GATE-001 remediation | `planned` | LLM_Consultant | GATE-001 | `implementation/` | `guideline_workspace_implementation.md` | `—` |
| TK011 | `T102-PH001-ST002-AC000-TK011` | Execute implementation per spec (STD-004 supersession + GATE-001-seeded fixes) | `planned` | LLM_Developer | TK010 | Target STD files per spec | Implementation spec | `—` |
| TK012 | `T102-PH001-ST002-AC000-TK012` | Produce GATE-002 dev-report | `planned` | LLM_Developer | TK011 | `dev-report/` | `guideline_workspace_dev-report.md` | `—` |
| TK013 | `T102-PH001-ST002-AC000-TK013` | Produce GATE-002 verification | `planned` | LLM_Reviewer | TK012 | `verification/` | `guideline_workspace_verification.md` | `—` |
| TK014 | `T102-PH001-ST002-AC000-TK014` | Produce GATE-002 gate-disposition proposal | `planned` | LLM_Consultant | TK013 | `proposal/` | `guideline_workspace_proposal.md` | `—` |
| TK015 | `T102-PH001-ST002-AC000-TK015` | Produce GATE-002 external review | `planned` | LLM_Subconsultant | TK014 | `analysis/` | `guideline_workspace_analysis.md` §IV.B | `—` |
| GATE-002 | `T102-PH001-ST002-AC000-GATE-002` | Gate: Client approval of AC000 implementation deliverables | `planned` | Client | TK015 | Pass/fail | `guideline_workspace_plan.md` §VI.L | `—` |
```

**Step 5: Add a new changelog row**

Insert above the existing `v2.0.0` row:
```markdown
| v2.1.0 | 2026-03-28 | Amendment | Repaired GATE-001 baseline for serialized consultant-owned package authoring. Reframed TK006 from pre-gate housekeeping mutation to supersession current-state assessment input. Normalized TK007 deliverable path into `analysis/`. Updated GATE-001 semantics to remain consultation-only while preserving post-gate implementation authority in TK010-TK015 / GATE-002. Marked TK000 completed and normalized register placeholder cells. Source: AC000 GATE-001 baseline-repair task specification (2026-03-28). |
```

### SPEC-002 — Repair AC000 detailed task and gate semantics

| Field | Detail |
|:--|:--|
| Requirement Source | The detailed task sections still describe `TK006` as a mutation, `TK007` as confirming completed housekeeping, and `GATE-001` as depending on a mutation-backed diagnostic package. |
| Target file(s) | `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/plan_T102-PH001-ST002-AC000.md` |
| Required end-state posture | `TK006` is a consultant-owned current-state assessment task; `TK007` records supersession posture and residual implementation scope rather than completed housekeeping; `TK008` recommendation wording reflects diagnostic acceptance; `TK009` references the canonical TK007 path; `GATE-001` entry criteria are consultation-only; `TK010` treats TK006 mutation as post-gate implementation authority. |
| Explicit non-target / do-not-change constraints | Do NOT rewrite TK001-TK005 substantive verification logic. Do NOT change TK011-TK015. Do NOT add new tasks or new gates. |
| Validation check | (1) TK006 deliverable is no longer an updated standard file; (2) TK007 Section IV no longer says “confirmation of housekeeping completion”; (3) TK009 input path for TK007 matches the canonical `analysis/` path; (4) GATE-001 entry criteria no longer state that supersession housekeeping itself is completed; (5) TK010 still retains post-gate implementation authority for the actual mutation. |
| Blocking ambiguity rule | If any section titles or task IDs differ from the quoted blocks below, stop and re-read before editing. Keep the exact task order unchanged. |
| Status | `open` |

#### Implementation Detail

**Step 1: Replace the entire `TK006` section**

Replace the current `### Task TK006` block with:
```markdown
### Task TK006: Assess T102-STD-004 Supersession Current State & Residual Housekeeping Scope

**Task ID**: `T102-PH001-ST002-AC000-TK006`

**Purpose**: Assess the current supersession posture of `T102-STD-004` against the P-STD-001 baseline and record any residual housekeeping gap that must be executed after GATE-001. This is a diagnostic assessment task, not the mutation itself.

**Deliverable**:
- Supersession current-state assessment recorded in TK007's calibrated scope brief, including any residual housekeeping item that remains for post-GATE-001 implementation

**Scope**:
- In scope: Reading the current `T102-STD-004` file; comparing its supersession notice and posture to the AC000/GATE-002 intent; identifying residual housekeeping needed after GATE-001
- Out of scope: Mutating `T102-STD-004`; updating SPS/Concept indexes; deleting the file

**Inputs Required**:
- `prompt/artifacts/tasks/T102/standard/standard_T102-STD-004_specification-standard-and-guideline.md` -- current file state
- `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md` -- successor standard

**Steps**:
1. Read the current T102-STD-004 file
2. Assess whether the current file already contains a supersession notice and whether that notice matches the intended post-GATE-001 housekeeping posture
3. Record the current-state posture as one of: `already-present-and-acceptable`, `present-but-malformed`, or `missing`
4. Record any residual mutation requirement as explicit post-GATE-001 implementation scope for TK010/TK011
5. Note the SPS update requirement (T102-STD-004 row status change) as a deferred AC004 item

**Success Criteria**:
- [ ] Current supersession posture is explicitly assessed
- [ ] Any residual housekeeping requirement is identified for post-GATE-001 implementation
- [ ] SPS update requirement is noted as AC004 deferred item
```

**Step 2: Replace the `TK007` Deliverable, Inputs Required, Step 5, and Success Criteria text**

Within `### Task TK007`, make these exact replacements:

Replace:
```markdown
**Deliverable**:
- `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/analysis_T102-PH001-ST002-AC000_calibrated-scope-brief.md`
```
with:
```markdown
**Deliverable**:
- `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/analysis/analysis_T102-PH001-ST002-AC000_calibrated-scope-brief.md`
```

Replace:
```markdown
- TK006 supersession housekeeping status
```
with:
```markdown
- TK006 supersession current-state assessment and residual housekeeping scope
```

Replace Step 5:
```markdown
5. Section IV: T102-STD-004 Supersession Status -- confirmation of housekeeping completion + deferred SPS update
```
with:
```markdown
5. Section IV: T102-STD-004 Supersession Status -- current-state posture, residual housekeeping scope for TK010/TK011, and deferred SPS update
```

Replace the final two success-criteria bullets:
```markdown
- [ ] Structural gap inventory covers all 9 T102-STDs
- [ ] Per-AC focus guidance is actionable and specific
- [ ] Open issues (if any) are explicitly flagged
```
with:
```markdown
- [ ] Structural gap inventory covers all 9 T102-STDs
- [ ] T102-STD-004 supersession posture is assessed without implying pre-gate mutation completion
- [ ] Per-AC focus guidance is actionable and specific
- [ ] Open issues (if any) are explicitly flagged
```

**Step 3: Replace `TK008` recommendation step text**

Within `### Task TK008`, replace Step 4:
```markdown
4. Consultant recommendation: APPROVE (if all content verification items are accounted for and structural gap inventory is complete) or APPROVE WITH CONDITIONS (if significant gaps require AC001 scope expansion)
```
with:
```markdown
4. Consultant recommendation: APPROVE (if the diagnostic package is complete and internally consistent) or APPROVE WITH CONDITIONS (if the package is complete but carries explicit downstream conditions such as priority structural remediation scope or post-gate housekeeping implementation)
```

**Step 4: Replace the `TK009` TK007 input path**

Replace:
```markdown
- `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/analysis/analysis_T102-PH001-ST002-AC000_calibrated-scope-brief.md` -- TK007 deliverable
```
with the identical canonical path shown below to ensure exact path consistency:
```markdown
- `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/analysis/analysis_T102-PH001-ST002-AC000_calibrated-scope-brief.md` -- TK007 deliverable
```

Note: this line currently already uses the target path. Leave it in place if unchanged after path normalization.

**Step 5: Replace the entire `GATE-001` Entry Criteria and Exit Criteria block**

Replace:
```markdown
**Entry Criteria**:
- TK001 through TK007 are completed (content verification, structural gap assessment, supersession housekeeping, calibrated scope brief)
- TK008 gate-disposition proposal exists with populated GDR in pending state
- TK009 external review analysis exists with findings reviewed by main `LLM_Consultant`
- Calibrated scope brief provides actionable per-AC guidance

**Reviewer**: Client

**Exit Criteria**:
- Client records decision in the GDR per `guideline_workspace_proposal.md` Section VII.D
- If APPROVE: AC001-AC004 may proceed using calibrated scope brief as primary input
- If APPROVE WITH CONDITIONS: conditions are recorded and addressed before AC001 begins
- If RECYCLE: remediation tasks are created per `guideline_workspace_plan.md` Section VI.K
```
with:
```markdown
**Entry Criteria**:
- TK001 through TK007 are completed (content verification, structural gap assessment, supersession current-state assessment, calibrated scope brief)
- TK008 gate-disposition proposal exists with populated GDR in pending state
- TK009 external review analysis exists with findings reviewed by main `LLM_Consultant`
- Calibrated scope brief provides actionable per-AC guidance without implying completion of post-gate implementation work

**Reviewer**: Client

**Exit Criteria**:
- Client records decision in the GDR per `guideline_workspace_proposal.md` Section VII.D
- If APPROVE: AC001-AC004 may proceed using the calibrated scope brief as primary diagnostic input; post-GATE-001 implementation authority remains governed by TK010-TK015 / GATE-002
- If APPROVE WITH CONDITIONS: conditions are recorded and govern downstream sequencing before AC001 begins or before post-gate implementation starts
- If RECYCLE: remediation tasks are created per `guideline_workspace_plan.md` Section VI.K
```

**Step 6: Replace the `TK010` purpose, scope, inputs, and step 2 text**

Within `### Task TK010`, make these exact replacements:

Replace:
```markdown
**Purpose**: Author a detailed implementation specification for the bounded implementation work authorized by GATE-001: T102-STD-004 supersession housekeeping (TK006 execution detail) and any content remediation items seeded by GATE-001 findings.
```
with:
```markdown
**Purpose**: Author a detailed implementation specification for the bounded implementation work authorized by GATE-001: any residual T102-STD-004 supersession housekeeping identified by TK006 and any content remediation items seeded by GATE-001 findings.
```

Replace:
```markdown
- In scope: Implementation specification for TK006 STD-004 mutation; implementation specification for any GATE-001-seeded content fixes within AC000 scope
```
with:
```markdown
- In scope: Implementation specification for any residual STD-004 mutation identified by TK006; implementation specification for any GATE-001-seeded content fixes within AC000 scope
```

Replace Step 2:
```markdown
2. Extract implementation items from the calibrated scope brief:
   - Unconditional: TK006 STD-004 supersession mutation (already detailed in current plan TK006)
   - Conditional: any content remediation items approved by GATE-001 for in-scope fixing
```
with:
```markdown
2. Extract implementation items from the calibrated scope brief:
   - Conditional-but-expected: any residual TK006 STD-004 housekeeping mutation explicitly identified by the GATE-001-approved diagnostic package
   - Conditional: any content remediation items approved by GATE-001 for in-scope fixing
```

### SPEC-003 — Align the ST002 stream-plan AC000 contract stub with the repaired activity plan

| Field | Detail |
|:--|:--|
| Requirement Source | The stream stub currently describes AC000 as performing supersession housekeeping directly and uses the non-canonical TK007 path. It must match the repaired activity plan. |
| Target file(s) | `prompt/artifacts/tasks/T102/workspace/PH001/ST002/plan_T102-PH001-ST002.md` |
| Required end-state posture | AC000 purpose/deliverable/scope/success criteria distinguish GATE-001 diagnostic assessment from GATE-002 implementation; the calibrated scope brief path is canonical and housed in `analysis/`; success criteria no longer imply that the supersession mutation itself must be complete at GATE-001. |
| Explicit non-target / do-not-change constraints | Do NOT alter AC001 or later activity sections. Do NOT change stream register rows outside the AC000 row unless necessary for path alignment in that row only. Do NOT change unrelated changelog entries. |
| Validation check | (1) AC000 stub purpose uses “assess current supersession posture” or equivalent diagnostic phrasing, not “perform housekeeping” at GATE-001; (2) the GATE-001 deliverable path points to `analysis/analysis_T102-PH001-ST002-AC000_calibrated-scope-brief.md`; (3) success criteria distinguish GATE-001 diagnostic acceptance from GATE-002 verified implementation. |
| Blocking ambiguity rule | If the AC000 stub text materially differs from the quoted text below, stop and re-read the stream plan. Keep the stream-plan amendment limited to AC000. |
| Status | `open` |

#### Implementation Detail

**Step 1: Update frontmatter**

Change:
```yaml
version: '2.1.0'
date: '2026-03-28'
```
to:
```yaml
version: '2.2.0'
date: '2026-03-28'
```

**Step 2: Replace the AC000 Purpose block**

Replace:
```markdown
**Purpose**: Verify that ST005's research-driven CLAUSE amendments were correctly applied to T102-STD-001, STD-003, STD-006, and STD-007; assess each T102-STD against P-STD-001 structural conformance requirements; perform T102-STD-004 supersession housekeeping; and produce a calibrated scope brief that AC001-AC004 consume as their primary input.
```
with:
```markdown
**Purpose**: Verify that ST005's research-driven CLAUSE amendments were correctly applied to T102-STD-001, STD-003, STD-006, and STD-007; assess each T102-STD against P-STD-001 structural conformance requirements; assess the current supersession posture of T102-STD-004 against the P-STD-001 baseline; and produce a calibrated scope brief that AC001-AC004 consume as their primary diagnostic input.
```

**Step 3: Replace the AC000 Deliverable block**

Replace:
```markdown
**Deliverable**:
- GATE-001 deliverable: A calibrated scope brief analysis artifact (`analysis_T102-PH001-ST002-AC000_calibrated-scope-brief.md`) documenting: (1) per-STD content verification results, (2) per-STD P-STD-001 structural gap inventory, (3) T102-STD-004 supersession status, (4) calibrated scope guidance for AC001-AC004.
- GATE-002 deliverable: Verified implementation of T102-STD-004 supersession housekeeping and any content remediation items seeded by GATE-001 findings.
```
with:
```markdown
**Deliverable**:
- GATE-001 deliverable: A calibrated scope brief analysis artifact (`analysis/analysis_T102-PH001-ST002-AC000_calibrated-scope-brief.md`) documenting: (1) per-STD content verification results, (2) per-STD P-STD-001 structural gap inventory, (3) T102-STD-004 supersession current-state assessment plus residual housekeeping scope, (4) calibrated scope guidance for AC001-AC004.
- GATE-002 deliverable: Verified implementation of any residual T102-STD-004 supersession housekeeping and any content remediation items seeded by GATE-001 findings.
```

**Step 4: Replace the AC000 Scope bullet**

Replace:
```markdown
- In scope: Content verification of ST005 amendments against research deltas; P-STD-001 structural gap assessment; T102-STD-004 supersession housekeeping; calibrated scope brief production
```
with:
```markdown
- In scope: Content verification of ST005 amendments against research deltas; P-STD-001 structural gap assessment; T102-STD-004 supersession current-state assessment for GATE-001 plus residual housekeeping handoff to GATE-002; calibrated scope brief production
```

**Step 5: Replace the AC000 Success Criteria Checklist**

Replace:
```markdown
**Success Criteria Checklist (summary)**:
- [ ] Per-STD content verification completed for STD-001, STD-003, STD-006, STD-007
- [ ] P-STD-001 structural gap inventory produced for all T102-STDs
- [ ] T102-STD-004 marked as superseded with forward reference to P-STD-001
- [ ] Calibrated scope brief produced with per-AC focus guidance
- [ ] Client approval via GATE-001 (consultation-only diagnostic pack)
- [ ] Client approval via GATE-002 (implementation-backed remediation/housekeeping pack)
```
with:
```markdown
**Success Criteria Checklist (summary)**:
- [ ] Per-STD content verification completed for STD-001, STD-003, STD-006, STD-007
- [ ] P-STD-001 structural gap inventory produced for all T102-STDs
- [ ] T102-STD-004 supersession current state assessed and any residual housekeeping scope explicitly handed off to GATE-002
- [ ] Calibrated scope brief produced with per-AC focus guidance
- [ ] Client approval via GATE-001 (consultation-only diagnostic pack)
- [ ] Client approval via GATE-002 (implementation-backed remediation/housekeeping pack)
```

**Step 6: Add a changelog row**

Insert above the existing `v2.1.0` row:
```markdown
| v2.2.0 | 2026-03-28 | Amendment | Repaired AC000 contract stub to align with the AC000 GATE-001 baseline-repair amendment. Reframed T102-STD-004 work at GATE-001 as supersession current-state assessment plus residual housekeeping scope handoff to GATE-002. Normalized the calibrated scope brief path into `analysis/`. Source: AC000 GATE-001 baseline-repair task specification (2026-03-28). |
```

### SPEC-004 — Final validation and explicit non-target boundaries

| Field | Detail |
|:--|:--|
| Requirement Source | The worker must leave a clean, non-improvised planning baseline that the consultant can trust before authoring the gate package. |
| Target file(s) | Both repaired plan files only |
| Required end-state posture | No remaining blocking contradiction across AC000/ST002 regarding TK006 meaning, TK007 pathing, or GATE-001 consultation-only semantics. |
| Explicit non-target / do-not-change constraints | Do NOT create `SES003`. Do NOT create analysis/proposal/external-review artifacts. Do NOT touch any `prompt/artifacts/tasks/T102/standard/` files. Do NOT edit any guideline/template files. Do NOT modify unrelated dirty files already present in the worktree. |
| Validation check | Run a final readback over the edited sections and confirm: (1) AC000 Task Register, TK006, TK007, TK008, TK009, GATE-001, TK010, and changelog align; (2) ST002 AC000 stub purpose/deliverable/scope/success criteria align; (3) `analysis/analysis_T102-PH001-ST002-AC000_calibrated-scope-brief.md` is the only TK007 path variant remaining in the two edited files. |
| Blocking ambiguity rule | If the requested change appears to require creating any new artifact other than these two plan edits, stop. Those follow-on artifacts are out of scope for this worker execution. |
| Status | `open` |

#### Implementation Detail

After completing the edits in SPEC-001 through SPEC-003:

1. Re-read the two edited files.
2. Verify that there is no remaining language implying that STD-004 housekeeping itself must be complete before `GATE-001`.
3. Verify that the canonical TK007 deliverable path uses the `analysis/` directory in both files.
4. Verify that no unrelated file was edited.

## IV. IMPLEMENTATION SEQUENCE

1. Execute `SPEC-001` on the AC000 activity plan.
2. Execute `SPEC-002` on the AC000 detailed sections and gate text.
3. Execute `SPEC-003` on the ST002 stream stub.
4. Execute `SPEC-004` validation checks by re-reading both edited files.

## V. REFERENCES

| Document | Path |
|:--|:--|
| Governing Plan | `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/plan_T102-PH001-ST002-AC000.md` |
| Parent Stream Plan | `prompt/artifacts/tasks/T102/workspace/PH001/ST002/plan_T102-PH001-ST002.md` |
| Prior TK000 Task Spec | `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/implementation/implementation_T102-PH001-ST002-AC000_tk000-plan-readiness-amendments.md` |

## VI. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-03-28 | Initial | Created exact execution specification for the AC000 GATE-001 baseline repair: AC000 activity-plan sequencing repair, TK006 semantic reframe, TK007 path normalization, GATE-001 consultation-only clarification, and ST002 AC000 contract-stub alignment. |
