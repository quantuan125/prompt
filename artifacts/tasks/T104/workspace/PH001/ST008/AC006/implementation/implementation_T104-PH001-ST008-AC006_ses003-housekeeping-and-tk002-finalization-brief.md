---
artifact_type: 'IMPLEMENTATION'
implementation_type: 'task_specification'
initiative_id: 'T104'
initiative_code: 'CWS'
phase: '1'
stream_id: 'T104-PH001-ST008'
activity_id: 'T104-PH001-ST008-AC006'
task_id: 'T104-PH001-ST008-AC006 (multi-task scope: Phase A plan housekeeping + Phase B TK002 finalization)'
version: '1.0.0'
date: '2026-03-28'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/plan_T104-PH001-ST008-AC006.md'
execution_audience: 'consultant'
purpose: 'Execute Phase A (plan housekeeping — status updates, task renumbering, new TK003.1 scope, stream notes registration) and Phase B (TK002 v2.1.0 — resolve CONV-022 placeholder with TK001.1 Option B findings) so the AC006 pre-gate package is structurally ready for Phase C gate-readiness stack authoring.'
---

# IMPLEMENTATION (Task Specification): SES003 Housekeeping & TK002 Finalization

## I. PURPOSE & AUTHORITY

- **Purpose**: This artifact specifies the exact file mutations required to: (1) bring the AC006 activity plan task register into compliance with actual completion state and client-approved renumbering; (2) register SES002 and SES003 in the stream notes index; (3) resolve the CONV-022 placeholder in TK002 with TK001.1 findings; and (4) mark TK002 as completed.
- **Authority chain**: The governing activity plan (`plan_T104-PH001-ST008-AC006.md`) authorizes this work. Client approved the renumbering (TK002.1 → TK003.2) and implementation plan (Phases A+B) in SES003 consultation.
- **Audience**: `LLM_Consultant` (execution_audience: consultant). This is consultant-owned plan amendment and proposal finalization work. No developer execution or dev-report is required.
- This artifact does NOT hold a GDR. Gate decisions are recorded in gate_disposition proposals per `guideline_workspace_proposal.md` Section VII.

## II. TASK SCOPE

- **Governing plan task**: `T104-PH001-ST008-AC006` (multi-task scope: plan amendment + TK002 finalization)
- **Trigger**: SES003 consultation QA identified: (a) task register status drift (all rows show `planned` despite completed deliverables), (b) client-requested renumbering of TK002.1 → TK003.2 with structural resequencing, (c) missing stream notes registration for SES002 and SES003, (d) unresolved CONV-022 placeholder in TK002 now that TK001.1 is complete.
- **Deliverable contract**:
  1. Plan updated to v3.0.0 with corrected task register, renumbered gate-readiness stack, new TK003.1 (implementation spec seeding), and changelog entry
  2. Stream notes register updated to index SES002 and SES003
  3. TK002 updated to v2.1.0 with CONV-022 resolved, DEC-008 updated, TK001.1 reference added, and changelog entry
  4. TK002 marked as `completed` in the plan task register

## III. SPECIFICATION ITEMS

---

### SPEC-001 — Update Plan Task Register: Status Corrections

| Field | Detail |
|:--|:--|
| Requirement Source | SES003 pre-GATE-001 gap assessment (PRE-G2): task register shows all tasks as `planned` despite completed deliverables |
| Target file(s) | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/plan_T104-PH001-ST008-AC006.md` |
| Required end-state posture | Task register rows for TK000, TK001, TK001.1 show `completed`; TK002 shows `in_progress` |
| Explicit non-target / do-not-change constraints | Do NOT modify any row below TK002 at this step. Do NOT modify any column other than `Status`. Do NOT modify any content outside the Task Register table. |
| Validation check | (1) TK000 Status = `completed`; (2) TK001 Status = `completed`; (3) TK001.1 Status = `completed`; (4) TK002 Status = `in_progress`; (5) All other rows remain `planned` |
| Blocking ambiguity rule | If any of TK000/TK001/TK001.1 already show a non-`planned` status, re-read the current state before overwriting |
| Status | `open` |

#### Implementation Detail

**Step 1: Replace the TK000 row (line 59) — change Status from `planned` to `completed`**

Find this exact line:
```markdown
| TK000 | `T104-PH001-ST008-AC006-TK000` | Record initial readiness and downstream-task assessment | `planned` | LLM_Consultant | `T104-PH001-ST008-AC001.8`, AC003 | `analysis/` | `guideline_workspace_analysis.md` | — |
```

Replace with:
```markdown
| TK000 | `T104-PH001-ST008-AC006-TK000` | Record initial readiness and downstream-task assessment | `completed` | LLM_Consultant | `T104-PH001-ST008-AC001.8`, AC003 | `analysis/` | `guideline_workspace_analysis.md` | — |
```

**Step 2: Replace the TK001 row (line 60) — change Status from `planned` to `completed`**

Find this exact line:
```markdown
| TK001 | `T104-PH001-ST008-AC006-TK001` | Produce governance gap analysis | `planned` | LLM_Consultant | TK000 | `analysis/` | `guideline_workspace_analysis.md` | — |
```

Replace with:
```markdown
| TK001 | `T104-PH001-ST008-AC006-TK001` | Produce governance gap analysis | `completed` | LLM_Consultant | TK000 | `analysis/` | `guideline_workspace_analysis.md` | — |
```

**Step 3: Replace the TK001.1 row (line 61) — change Status from `planned` to `completed`**

Find this exact line:
```markdown
| TK001.1 | `T104-PH001-ST008-AC006-TK001.1` | Produce implementation artifact architecture comparative analysis | `planned` | LLM_Consultant | TK001 | `analysis/` | `guideline_workspace_analysis.md` | — |
```

Replace with:
```markdown
| TK001.1 | `T104-PH001-ST008-AC006-TK001.1` | Produce implementation artifact architecture comparative analysis | `completed` | LLM_Consultant | TK001 | `analysis/` | `guideline_workspace_analysis.md` | — |
```

**Step 4: Replace the TK002 row (line 62) — change Status from `planned` to `in_progress`**

Find this exact line:
```markdown
| TK002 | `T104-PH001-ST008-AC006-TK002` | Produce standards-input proposal for governance changes | `planned` | LLM_Consultant | TK001, TK001.1 | `proposal/` | `guideline_workspace_proposal.md` | — |
```

Replace with:
```markdown
| TK002 | `T104-PH001-ST008-AC006-TK002` | Produce standards-input proposal for governance changes | `in_progress` | LLM_Consultant | TK001, TK001.1 | `proposal/` | `guideline_workspace_proposal.md` | — |
```

---

### SPEC-002 — Update Plan Task Register: Renumber TK002.1 → TK003.2 and Resequence Gate-Readiness Stack

| Field | Detail |
|:--|:--|
| Requirement Source | Client QA (SES003 Answer 1): "TK002.1 should actually be TK003.2 given that the external review artifact is only commissioned after the gate disposition proposal file is created." Client QA (SES003 Answer 1.1): TK003.1 must include the implementation spec artifact for downstream seeding. |
| Target file(s) | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/plan_T104-PH001-ST008-AC006.md` |
| Required end-state posture | Task register gate-readiness stack reads: TK003 (gate-disposition proposal, Depends On: TK002) → TK003.1 (produce TK004 implementation spec, Depends On: TK003) → TK003.2 (authoritative external review, Depends On: TK003.1) → TK003.3 (conditional same-gate hardening, Depends On: TK003.2) → GATE-001 (Depends On: TK003.3). TK002.1 row is removed. |
| Explicit non-target / do-not-change constraints | Do NOT modify TK000, TK001, TK001.1, TK002 rows (those were handled by SPEC-001). Do NOT modify TK004 through GATE-002 rows. Do NOT modify Section I (Executive Summary) or Section II preamble text. |
| Validation check | (1) No TK002.1 row exists in the table; (2) TK003 Depends On = `TK002`; (3) TK003.1 row exists with Name containing "implementation" and "task specification"; (4) TK003.2 row exists with Name containing "external review"; (5) TK003.3 row exists with Name containing "same-gate"; (6) GATE-001 Depends On = `TK003.3` |
| Blocking ambiguity rule | If the task register has already been partially renumbered, STOP and re-read the current state before applying |
| Status | `open` |

#### Implementation Detail

**Step 1: Remove the TK002.1 row and replace the TK003 and TK003.1 rows (lines 63–65)**

Find these three exact consecutive lines:
```markdown
| TK002.1 | `T104-PH001-ST008-AC006-TK002.1` | Produce authoritative external review of the GATE-001 package | `planned` | LLM_Consultant | TK002 | `analysis/` | `guideline_workspace_analysis.md` | — |
| TK003 | `T104-PH001-ST008-AC006-TK003` | Produce GATE-001 gate-disposition proposal | `planned` | LLM_Consultant | TK002.1 | `proposal/` | `guideline_workspace_proposal.md` | — |
| TK003.1 | `T104-PH001-ST008-AC006-TK003.1` | Perform conditional same-gate package hardening and evidence correction | `planned` | LLM_Consultant | TK003 | `analysis/`, `proposal/`, `plan/` | `guideline_workspace_plan.md` | — |
```

Replace with these four lines:
```markdown
| TK003 | `T104-PH001-ST008-AC006-TK003` | Produce GATE-001 gate-disposition proposal | `planned` | LLM_Consultant | TK002 | `proposal/` | `guideline_workspace_proposal.md` | — |
| TK003.1 | `T104-PH001-ST008-AC006-TK003.1` | Produce TK004 implementation task specification (`execution_audience: 'developer'`) | `planned` | LLM_Consultant | TK003 | `implementation/` | `guideline_workspace_implementation.md` | — |
| TK003.2 | `T104-PH001-ST008-AC006-TK003.2` | Produce authoritative external review of the GATE-001 package | `planned` | LLM_Consultant | TK003.1 | `analysis/` | `guideline_workspace_analysis.md` | — |
| TK003.3 | `T104-PH001-ST008-AC006-TK003.3` | Perform conditional same-gate package hardening and evidence correction | `planned` | LLM_Consultant | TK003.2 | `analysis/`, `proposal/`, `plan/` | `guideline_workspace_plan.md` | — |
```

**Step 2: Update the GATE-001 row (line 66) — change Depends On from `TK003.1` to `TK003.3`**

Find this exact line:
```markdown
| GATE-001 | `T104-PH001-ST008-AC006-GATE-001` | Gate: Client approval of governance direction | `planned` | Client | TK003.1 | GDR | `guideline_workspace_proposal.md` | — |
```

Replace with:
```markdown
| GATE-001 | `T104-PH001-ST008-AC006-GATE-001` | Gate: Client approval of governance direction | `planned` | Client | TK003.3 | GDR | `guideline_workspace_proposal.md` | — |
```

---

### SPEC-003 — Update Plan §III Detailed Task Sections: Remove TK002.1, Update TK003, Add TK003.1, Add TK003.2, Renumber TK003.1 → TK003.3, Update GATE-001

| Field | Detail |
|:--|:--|
| Requirement Source | Structural consequence of SPEC-002 renumbering — §III detailed task sections must match the task register |
| Target file(s) | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/plan_T104-PH001-ST008-AC006.md` |
| Required end-state posture | §III contains: (a) no TK002.1 section; (b) TK003 section with Depends On updated to TK002 and scope updated to include TK001.1 in Gate Package Index; (c) new TK003.1 section for implementation spec; (d) new TK003.2 section (former TK002.1 content with updated ID/dependencies); (e) TK003.3 section (former TK003.1 content with updated ID/dependencies); (f) GATE-001 entry criteria updated |
| Explicit non-target / do-not-change constraints | Do NOT modify TK000, TK001, TK001.1, TK002 detailed sections. Do NOT modify TK004 through GATE-002 detailed sections. |
| Validation check | (1) Search for "TK002.1" in §III returns zero matches outside of historical references; (2) TK003 section has "Depends On: TK002" in its inputs; (3) TK003.1 section exists with "implementation task specification" in purpose; (4) TK003.2 section exists with "authoritative external review" in purpose; (5) TK003.3 section exists with "same-gate" in purpose; (6) GATE-001 entry criteria reference TK003.3 |
| Blocking ambiguity rule | If any of the detailed sections have already been modified, STOP and re-read the current state before applying |
| Status | `open` |

#### Implementation Detail

**Step 1: Remove the entire TK002.1 detailed section (lines 235–269)**

Find and remove the entire block starting with:
```markdown
### Task TK002.1: Produce Authoritative External Review of the GATE-001 Package
```

And ending just before:
```markdown
### Task TK003: Produce GATE-001 Gate-Disposition Proposal
```

Remove the entire block (lines 235–270, inclusive of the blank line before TK003).

**Step 2: Replace the TK003 detailed section (lines 271–303)**

Find the entire section starting with:
```markdown
### Task TK003: Produce GATE-001 Gate-Disposition Proposal

**Task ID**: `T104-PH001-ST008-AC006-TK003`

**Purpose**: Present the governance direction for client approval before implementation work starts.

**Deliverable**:
- `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/proposal/proposal_T104-PH001-ST008-AC006-GATE-001_governance-disposition.md`

**Scope**:
- In scope:
  - Gate Package Index covering TK000, TK001, TK002, and TK002.1
  - Evidence Index separating primary evidence from supporting / historical evidence
  - Pending GDR authoring for the governance package
- Out of scope:
  - Guideline or template edits

**Inputs Required**:
- `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/analysis/analysis_T104-PH001-ST008-AC006-TK000_initial-readiness-and-downstream-assessment.md`
- `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/analysis/analysis_T104-PH001-ST008-AC006_implementation-governance-gap-analysis.md`
- `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/proposal/proposal_T104-PH001-ST008-AC006_governance-input-disposition.md`
- `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/analysis/analysis_T104-PH001-ST008-AC006_gate-001-package-authoritative-external-review.md`

**Steps**:
1. Package the governance direction for client disposition.
2. Make TK000 the first deliverable in the Gate Package Index.
3. Populate the GDR in pending state and identify the authoritative external review in the evidence set.

**Success Criteria**:
- [ ] The `GATE-001` proposal exists with a pending GDR
- [ ] TK000 is included in the Gate Package Index and Evidence Index
- [ ] The authoritative external review is explicitly named in the package
```

Replace with:
```markdown
### Task TK003: Produce GATE-001 Gate-Disposition Proposal

**Task ID**: `T104-PH001-ST008-AC006-TK003`

**Purpose**: Present the governance direction for client approval before implementation work starts. This is the first task in the GATE-001 gate-readiness stack per `guideline_workspace_plan.md` §VI.L (consultation-only variant).

**Deliverable**:
- `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/proposal/proposal_T104-PH001-ST008-AC006-GATE-001_governance-disposition.md`

**Scope**:
- In scope:
  - Gate Package Index covering TK000, TK001, TK001.1, TK002, TK003.1 (implementation spec), and TK003.2 (external review)
  - Evidence Index separating primary evidence from supporting / historical evidence
  - Pending GDR authoring for the governance package
- Out of scope:
  - Guideline or template edits

**Inputs Required**:
- `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/analysis/analysis_T104-PH001-ST008-AC006-TK000_initial-readiness-and-downstream-assessment.md`
- `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/analysis/analysis_T104-PH001-ST008-AC006_implementation-governance-gap-analysis.md`
- `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/analysis/analysis_T104-PH001-ST008-AC006-TK001.1_implementation-artifact-architecture-assessment.md`
- `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/proposal/proposal_T104-PH001-ST008-AC006_governance-input-disposition.md`

**Steps**:
1. Package the governance direction for client disposition.
2. Make TK000 the first deliverable in the Gate Package Index.
3. Include TK001.1 comparative analysis in the Gate Package Index and Evidence Index.
4. Populate the GDR in pending state. Note: the authoritative external review (TK003.2) and implementation spec (TK003.1) will be added to the package after they are produced.

**Success Criteria**:
- [ ] The `GATE-001` proposal exists with a pending GDR
- [ ] TK000 and TK001.1 are included in the Gate Package Index and Evidence Index
- [ ] The gate package structure anticipates TK003.1 (implementation spec) and TK003.2 (external review) as subsequent additions
```

**Step 3: Replace the TK003.1 detailed section (lines 304–334) with three new sections: TK003.1, TK003.2, TK003.3**

Find the entire section starting with:
```markdown
### Task TK003.1: Perform Conditional Same-Gate Package Hardening and Evidence Correction

**Task ID**: `T104-PH001-ST008-AC006-TK003.1`
```

And ending just before:
```markdown
### GATE-001: Client Approval of Governance Direction
```

Replace the entire TK003.1 section with these three sections:

```markdown
### Task TK003.1: Produce TK004 Implementation Task Specification

**Task ID**: `T104-PH001-ST008-AC006-TK003.1`

**Purpose**: Author the consultant-owned implementation task specification (`execution_audience: 'developer'`) that commissions TK004 downstream developer execution under GATE-001 authority. This artifact seeds the post-GATE-001 implementation path and is included in the GATE-001 gate package per CONV-018 (governed delegated execution must be mediated through an IMPLEMENTATION artifact).

**Deliverable**:
- `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/implementation/implementation_T104-PH001-ST008-AC006_governance-hardening-implementation-task-specification.md`

**Scope**:
- In scope:
  - Specify the exact guideline/template/rules mutations approved at GATE-001 for TK004 developer execution
  - Define SPEC items covering all eight target governance files identified in TK002
  - Set `execution_audience: 'developer'` per `guideline_workspace_implementation.md` CONV-013
  - Include in the GATE-001 gate package as a consultant-authored commissioning artifact
- Out of scope:
  - Executing the mutations (that is TK004 developer-owned scope)
  - Producing the DEV-REPORT (that is TK005 developer-owned scope)

**Inputs Required**:
- `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/proposal/proposal_T104-PH001-ST008-AC006-GATE-001_governance-disposition.md` (approved governance direction)
- `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/proposal/proposal_T104-PH001-ST008-AC006_governance-input-disposition.md` (CONV-015 through CONV-023)
- `prompt/templates/consultant/workspace/guideline_workspace_implementation.md`
- `prompt/templates/consultant/workspace/template_workspace_implementation_task-specification.md`

**Steps**:
1. Read the approved governance direction from the GATE-001 proposal (once GDR records approval).
2. Translate each approved convention (CONV-015 through CONV-023) into SPEC items targeting the correct guideline/template/rules section.
3. Author the implementation artifact with `execution_audience: 'developer'` and CONV-015-compliant SPEC items (exact target files, end-state posture, validation checks, non-target constraints).
4. Add the implementation artifact to the GATE-001 gate package Evidence Index.

**Success Criteria**:
- [ ] The implementation artifact exists with `execution_audience: 'developer'`
- [ ] Each approved convention maps to at least one SPEC item
- [ ] All SPEC items meet the CONV-015 minimum-detail floor
- [ ] The artifact is referenced in the GATE-001 gate package

### Task TK003.2: Produce Authoritative External Review of the GATE-001 Package

**Task ID**: `T104-PH001-ST008-AC006-TK003.2`

**Purpose**: Produce the single authoritative external review for the consultation-only `GATE-001` package. This review assesses the complete gate package including the gate-disposition proposal (TK003) and the implementation task specification (TK003.1).

**Deliverable**:
- `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/analysis/analysis_T104-PH001-ST008-AC006_gate-001-package-authoritative-external-review.md`

**Scope**:
- In scope:
  - Downstream task readiness for the post-`GATE-001` path
  - Plan-guideline compliance of the consultant-owned pre-gate package
  - Evidence integrity and package coherence
  - Role-boundary compliance
  - Per-SPEC commissionability assessment of the TK003.1 implementation artifact (per CONV-016)
  - Confirmation that no unauthorized downstream execution or premature concrete-artifact authority is being normalized
- Out of scope:
  - Developer execution of TK004
  - Mutating the package during the review itself

**Inputs Required**:
- `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/analysis/analysis_T104-PH001-ST008-AC006-TK000_initial-readiness-and-downstream-assessment.md`
- `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/analysis/analysis_T104-PH001-ST008-AC006_implementation-governance-gap-analysis.md`
- `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/analysis/analysis_T104-PH001-ST008-AC006-TK001.1_implementation-artifact-architecture-assessment.md`
- `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/proposal/proposal_T104-PH001-ST008-AC006_governance-input-disposition.md`
- `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/proposal/proposal_T104-PH001-ST008-AC006-GATE-001_governance-disposition.md`
- `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/implementation/implementation_T104-PH001-ST008-AC006_governance-hardening-implementation-task-specification.md`
- `prompt/templates/consultant/workspace/guideline_workspace_analysis.md`
- `prompt/templates/consultant/workspace/guideline_workspace_plan.md`

**Steps**:
1. Review the live AC006 consultant-owned package (including TK003 proposal and TK003.1 implementation spec) against the governing guidance.
2. Assess per-SPEC commissionability of the TK003.1 implementation artifact per CONV-016.
3. Name this review as the single authoritative external review for the `GATE-001` package.
4. Record any residual gaps requiring same-gate correction before client disposition.

**Success Criteria**:
- [ ] One authoritative external review exists for the package
- [ ] Downstream readiness and plan-guideline compliance are explicitly assessed
- [ ] Per-SPEC commissionability of the TK003.1 implementation spec is assessed
- [ ] Any required same-gate corrections are explicitly identified

### Task TK003.3: Perform Conditional Same-Gate Package Hardening and Evidence Correction

**Task ID**: `T104-PH001-ST008-AC006-TK003.3`

**Purpose**: If same-gate QA or package-coherence defects are found after TK003.2 (authoritative external review), apply tracked consultant-owned corrections under the same gate rather than silently folding them into live artifacts.

**Deliverable**:
- Updated `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/proposal/proposal_T104-PH001-ST008-AC006-GATE-001_governance-disposition.md`
- Updated supporting AC006 analysis / plan / implementation surfaces as required by the same-gate correction

**Scope**:
- In scope:
  - Same-gate package hardening
  - Evidence-index correction
  - Explicit tracking of any added session / package / plan amendments required before client disposition
- Out of scope:
  - Any post-`GATE-001` implementation execution

**Inputs Required**:
- TK003 gate-disposition proposal
- TK003.1 implementation task specification
- TK003.2 authoritative external review

**Steps**:
1. Invoke this task only if package QA or coherence defects remain after TK003.2.
2. Apply the minimum tracked same-gate corrections required to restore package integrity.
3. Keep the same gate identity and preserve historical lineage explicitly.

**Success Criteria**:
- [ ] If invoked, the corrections are tracked through plan / notes / package surfaces
- [ ] The gate identity remains unchanged
- [ ] The package is coherent for client disposition
```

**Step 4: Update the GATE-001 detailed section (lines 336–352)**

Find:
```markdown
### GATE-001: Client Approval of Governance Direction

**Gate ID**: `T104-PH001-ST008-AC006-GATE-001`

**Entry Criteria**:
- TK000 through TK003 are complete
- TK003.1 is completed or cancelled
- The gate-disposition proposal exists with a pending GDR
- One authoritative external review is explicitly identified in the package
```

Replace with:
```markdown
### GATE-001: Client Approval of Governance Direction

**Gate ID**: `T104-PH001-ST008-AC006-GATE-001`

**Entry Criteria**:
- TK000 through TK003.2 are complete
- TK003.3 is completed or cancelled
- The gate-disposition proposal exists with a pending GDR
- One authoritative external review (TK003.2) is explicitly identified in the package
- The TK004 implementation task specification (TK003.1) is included in the gate package
```

**Step 5: Update the TK000 Success Criteria (line 111) — fix stale TK002.1 reference**

Find:
```markdown
- [ ] The analysis provides clear downstream actions feeding TK001, TK002, TK002.1, and TK003
```

Replace with:
```markdown
- [ ] The analysis provides clear downstream actions feeding TK001, TK002, and TK003
```

---

### SPEC-004 — Update Plan Frontmatter and Changelog

| Field | Detail |
|:--|:--|
| Requirement Source | Structural consequence of SPEC-001/002/003 — plan version and changelog must reflect the amendment |
| Target file(s) | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/plan_T104-PH001-ST008-AC006.md` |
| Required end-state posture | Frontmatter version = `3.0.0`; changelog contains a v3.0.0 entry describing the renumbering and status updates |
| Explicit non-target / do-not-change constraints | Do NOT modify any frontmatter field other than `version` and `date`. Do NOT modify existing changelog rows. |
| Validation check | (1) Frontmatter `version: '3.0.0'`; (2) Frontmatter `date: '2026-03-28'`; (3) Changelog contains v3.0.0 row as the last entry |
| Blocking ambiguity rule | None — this SPEC depends on SPEC-001/002/003 completing first |
| Status | `open` |

#### Implementation Detail

**Step 1: Update frontmatter version (line 9)**

Find:
```yaml
version: '2.0.0'
```

Replace with:
```yaml
version: '3.0.0'
```

**Step 2: Append changelog entry after the v2.0.0 row (after line 473)**

After the existing v2.0.0 changelog row, append:
```markdown
| v3.0.0 | 2026-03-28 | Major | SES003 plan amendment: (a) Updated task register statuses — TK000, TK001, TK001.1 marked `completed`, TK002 marked `in_progress`. (b) Renumbered gate-readiness stack per client QA — removed TK002.1, updated TK003 Depends On to TK002, inserted new TK003.1 (produce TK004 implementation task specification with `execution_audience: 'developer'`), renumbered former TK002.1 to TK003.2 (authoritative external review, Depends On: TK003.1), renumbered former TK003.1 to TK003.3 (conditional same-gate hardening, Depends On: TK003.2), updated GATE-001 Depends On to TK003.3. (c) Updated §III detailed task sections to match renumbered register. (d) Updated GATE-001 entry criteria to include TK003.1 implementation spec and reference TK003.2/TK003.3. |
```

---

### SPEC-005 — Register SES002 and SES003 in Stream Notes Register

| Field | Detail |
|:--|:--|
| Requirement Source | SES003 pre-GATE-001 gap assessment (PRE-G3): SES002 not registered; SES003 also unregistered. JIT registration per `guideline_workspace_notes.md` §5.1 |
| Target file(s) | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/notes_T104-PH001-ST008.md` |
| Required end-state posture | Activity Notes Register (§III) contains two new rows for AC006-SES002 and AC006-SES003, inserted at the top of the table (most recent first) |
| Explicit non-target / do-not-change constraints | Do NOT modify any existing register rows. Do NOT modify the version or date in frontmatter (that is a separate housekeeping concern outside this SPEC scope). Do NOT modify §I or §II. |
| Validation check | (1) Row for `T104-PH001-ST008-AC006-SES002` exists in the Activity Notes Register; (2) Row for `T104-PH001-ST008-AC006-SES003` exists; (3) Both rows appear above the existing AC006-SES001 row; (4) Notes File paths are repo-relative and correct |
| Blocking ambiguity rule | If SES002 or SES003 rows already exist, do NOT duplicate them |
| Status | `open` |

#### Implementation Detail

**Step 1: Insert two rows at the top of the Activity Notes Register table, immediately after the header row**

Find:
```markdown
| Activity | Session ID | Name | Notes File |
|:--|:--|:--|:--|
| AC006 | `T104-PH001-ST008-AC006-SES001` | AC006 Promotion, Baseline Readiness Assessment & GATE-001 Package Structuring | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/snotes/snotes_T104-PH001-ST008-AC006-SES001.md` |
```

Replace with:
```markdown
| Activity | Session ID | Name | Notes File |
|:--|:--|:--|:--|
| AC006 | `T104-PH001-ST008-AC006-SES003` | TK001.1 Comparative Analysis, Pre-GATE-001 Readiness Assessment & Plan Amendment | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/snotes/snotes_T104-PH001-ST008-AC006-SES003.md` |
| AC006 | `T104-PH001-ST008-AC006-SES002` | Research Integration, Governance Hardening, and Plan Amendment | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/snotes/snotes_T104-PH001-ST008-AC006-SES002.md` |
| AC006 | `T104-PH001-ST008-AC006-SES001` | AC006 Promotion, Baseline Readiness Assessment & GATE-001 Package Structuring | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/snotes/snotes_T104-PH001-ST008-AC006-SES001.md` |
```

**Step 2: Update the stream notes register version**

Find:
```yaml
version: '2.17.0'
date: '2026-03-27'
```

Replace with:
```yaml
version: '2.18.0'
date: '2026-03-28'
```

---

### SPEC-006 — Update TK002 Proposal: Resolve CONV-022 Placeholder with TK001.1 Option B Findings

| Field | Detail |
|:--|:--|
| Requirement Source | TK001.1 comparative analysis complete — Option B (naming convention) recommended with weighted score 83/100. CONV-022 placeholder must be resolved before TK002 can be marked `completed`. |
| Target file(s) | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/proposal/proposal_T104-PH001-ST008-AC006_governance-input-disposition.md` |
| Required end-state posture | (a) CONV-022 rule text updated with Option B naming convention specifics; (b) CONV-022 compatibility note updated to name Option B; (c) DEC-008 updated with specific Option B recommendation; (d) TK001.1 added to References §VI.A; (e) §I Purpose updated to remove "deferred" language; (f) version = v2.1.0 with changelog entry |
| Explicit non-target / do-not-change constraints | Do NOT modify any convention other than CONV-022. Do NOT modify any DEC other than DEC-008. Do NOT modify §II (Current State Summary), §V (Impact and Risks), or §VI.B (External Standards References). |
| Validation check | (1) CONV-022 rule text contains "naming convention" and "-brief suffix"; (2) DEC-008 recommendation references "Option B" and "TK001.1"; (3) TK001.1 path appears in §VI.A; (4) Version = `2.1.0` |
| Blocking ambiguity rule | If TK002 version is already above 2.0.0, STOP and re-read |
| Status | `open` |

#### Implementation Detail

**Step 1: Update §I Purpose — remove CONV-022 deferral language (line 33)**

Find:
```markdown
- **Input scope**: Pre-implementation governance rules only. This proposal defines the conventions that must govern how IMPLEMENTATION artifacts are authored, reviewed, commissioned, and tracked, and how the assistant subagent role is formalized. It does not implement the rules — that is TK004 scope after `GATE-001` approval. One architectural question (CONV-022: implementation artifact discoverability) is deferred to TK001.1 comparative analysis with a placeholder decision request (DEC-008).
```

Replace with:
```markdown
- **Input scope**: Pre-implementation governance rules only. This proposal defines the conventions that must govern how IMPLEMENTATION artifacts are authored, reviewed, commissioned, and tracked, and how the assistant subagent role is formalized. It does not implement the rules — that is TK004 scope after `GATE-001` approval. CONV-022 (implementation artifact discoverability) has been resolved with TK001.1 comparative analysis findings recommending Option B (naming convention).
```

**Step 2: Update CONV-022 rule text in the Convention Set table (line 83)**

Find the CONV-022 row in the §III.A convention table. The Rule cell currently reads:
```
The architectural distinction between developer-facing implementation specifications (which seed implementation-backed gate workflows and are reviewed by multiple roles) and assistant-facing implementation specifications (lightweight orchestration briefs reviewed only by the commissioning consultant) MUST be resolved through one of: (a) a naming convention distinguishing the two at the filesystem level, (b) a new IMPLEMENTATION subtype for assistant-scoped work, or (c) a combination of naming + subtype. The specific resolution is deferred to the TK001.1 comparative analysis; this convention reserves the requirement that a resolution MUST be adopted. Additionally, the `remediation_specification` subtype scope (currently restricted to gate RECYCLE verdicts) and its overlap with assistant-executed pre-gate corrections MUST be evaluated as a dimension of the same analysis.
```

Replace the CONV-022 Rule cell content with:
```
The architectural distinction between developer-facing implementation specifications and assistant-facing implementation specifications MUST be resolved through a **naming convention** (Option B per TK001.1 comparative analysis, weighted score 83/100): developer-facing task specifications retain the existing `-task-specification` filename suffix; consultant/assistant-facing orchestration briefs MUST use a `-brief` filename suffix (e.g., `implementation_<scope-UID>_<topic>-brief.md`). Remediation specifications retain the existing `-remediation-specification` suffix and remain restricted to gate RECYCLE verdicts. The `remediation_specification` subtype scope is NOT expanded; pre-gate assistant corrections are governed through `task_specification` with appropriate `execution_audience` and the `-brief` naming convention.
```

Replace the CONV-022 Rationale cell content with:
```
TK001.1 evaluated four options against six weighted criteria (discoverability, governance cost, backward compatibility, template impact, LLM_Assistant alignment, remediation scope clarity). Option B scored 83/100 — highest overall. The naming convention resolves filesystem-level discoverability without new templates or subtype taxonomy changes. Structural identity finding (all implementation artifacts share identical SPEC structure regardless of audience) confirms the distinction is operational context, not document type — a naming convention correctly reflects this. [Grounding: ISO 9001 §7.5.3 — distinct document types distinguishable by identification scheme; PRINCE2 CIR — each product variant has distinct CI type; Claude Code role archetypes — structurally distinct agents; ISO 9001 §10.2 CAPA — corrections vs. corrective actions maps to remediation_specification vs. assistant pre-gate fixes]
```

Replace the CONV-022 Authority Link cell content with:
```
`guideline_workspace_implementation.md` §IV (naming convention rule), `workspace_documentation_rules.md` §3 (filename pattern note). Analysis: `analysis_T104-PH001-ST008-AC006-TK001.1_implementation-artifact-architecture-assessment.md`
```

**Step 3: Update CONV-022 compatibility note (line 96)**

Find:
```markdown
- **CONV-022** does not prescribe a specific architectural resolution. It reserves the requirement that a resolution MUST be adopted, with the specific form determined by TK001.1. Existing implementation artifacts are not retroactively renamed or retyped; the resolution applies to new artifacts authored after approval. The remediation_specification scope evaluation does not expand that subtype's current trigger (gate RECYCLE verdict); it evaluates whether the gray zone of pre-gate assistant corrections needs its own mechanism or can be absorbed by the architectural distinction.
```

Replace with:
```markdown
- **CONV-022** prescribes Option B (naming convention) per TK001.1 comparative analysis: developer-facing specs retain `-task-specification` suffix; consultant/assistant-facing specs use `-brief` suffix. Existing implementation artifacts are not retroactively renamed; the naming convention applies to new artifacts authored after approval. No new templates or subtypes are introduced. The `remediation_specification` subtype scope remains restricted to gate RECYCLE verdicts; pre-gate assistant corrections are governed through the naming convention + `execution_audience` flag.
```

**Step 4: Update DEC-008 in the Decision Requests table (line 123)**

Find the DEC-008 row. Replace the Options cell content with:
```
(a) Yes — adopt Option B naming convention: developer-facing retain `-task-specification`, consultant/assistant-facing use `-brief` suffix (TK001.1 recommendation, score 83/100); (b) Yes — adopt Option C (new subtype) instead (TK001.1 score 63/100); (c) Yes — adopt Option D (combination) instead (TK001.1 score 63/100); (d) No — keep current `execution_audience` flag as sole discriminator (Option A, TK001.1 score 67/100)
```

Replace the Recommendation cell content with:
```
(a) — TK001.1 comparative analysis evaluated all four options against six weighted criteria. Option B scores highest (83/100) because it resolves the primary discoverability gap at the lowest governance cost. All implementation artifacts share identical SPEC structure (GAP-TK1.1-002), confirming the distinction is operational context, not document type. A naming convention correctly reflects this structural identity. No new templates, no subtype taxonomy change, forward-only application.
```

**Step 5: Add TK001.1 reference to §VI.A Internal Workspace References table**

Find:
```markdown
| Supporting Analysis (TK001) | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/analysis/analysis_T104-PH001-ST008-AC006_implementation-governance-gap-analysis.md` |
```

Insert immediately after that row:
```markdown
| Supporting Analysis (TK001.1) | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/analysis/analysis_T104-PH001-ST008-AC006-TK001.1_implementation-artifact-architecture-assessment.md` |
```

**Step 6: Update frontmatter version and date**

Find:
```yaml
version: '2.0.0'
date: '2026-03-28'
```

Replace with:
```yaml
version: '2.1.0'
date: '2026-03-28'
```

**Step 7: Append changelog entry after the v2.0.0 row**

After the existing v2.0.0 changelog row, append:
```markdown
| v2.1.0 | 2026-03-28 | Minor | Resolved CONV-022 placeholder with TK001.1 comparative analysis findings: Option B (naming convention) adopted — developer-facing retain `-task-specification` suffix, consultant/assistant-facing use `-brief` suffix. Updated DEC-008 with specific Option B recommendation (score 83/100). Updated CONV-022 compatibility note. Added TK001.1 to §VI.A references. Removed deferral language from §I Purpose. Remediation specification scope confirmed as appropriately tight (RECYCLE-only). |
```

---

### SPEC-007 — Mark TK002 as Completed in Plan Task Register

| Field | Detail |
|:--|:--|
| Requirement Source | SPEC-006 completes TK002 deliverable. Task register must reflect completion. |
| Target file(s) | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/plan_T104-PH001-ST008-AC006.md` |
| Required end-state posture | TK002 Status = `completed` in the task register |
| Explicit non-target / do-not-change constraints | Do NOT modify any other task register row. This SPEC MUST be executed AFTER SPEC-006 completes. |
| Validation check | (1) TK002 Status = `completed` |
| Blocking ambiguity rule | If TK002 is not yet at `in_progress` (from SPEC-001), execute SPEC-001 first |
| Status | `open` |

#### Implementation Detail

**Step 1: Update TK002 row — change Status from `in_progress` to `completed`**

Find (this will be the state after SPEC-001 has been applied):
```markdown
| TK002 | `T104-PH001-ST008-AC006-TK002` | Produce standards-input proposal for governance changes | `in_progress` | LLM_Consultant | TK001, TK001.1 | `proposal/` | `guideline_workspace_proposal.md` | — |
```

Replace with:
```markdown
| TK002 | `T104-PH001-ST008-AC006-TK002` | Produce standards-input proposal for governance changes | `completed` | LLM_Consultant | TK001, TK001.1 | `proposal/` | `guideline_workspace_proposal.md` | — |
```

---

## IV. EXECUTION SEQUENCE

The SPECs have the following dependency order:

```
SPEC-001 (status corrections) ──┐
                                 ├── SPEC-004 (version/changelog) ── SPEC-007 (TK002 completed)
SPEC-002 (renumbering)     ─────┤
                                 │
SPEC-003 (§III sections)   ─────┘

SPEC-005 (stream notes)    ── independent, can run in parallel with all above

SPEC-006 (TK002 v2.1.0)   ── independent of plan SPECs, must complete before SPEC-007
```

**Recommended execution order**:
1. SPEC-001 + SPEC-005 (parallel — different files)
2. SPEC-002 (depends on SPEC-001 completing for consistent task register)
3. SPEC-003 (depends on SPEC-002 for correct section names)
4. SPEC-006 (independent — different file, can start after SPEC-001)
5. SPEC-004 (depends on SPEC-001/002/003)
6. SPEC-007 (depends on SPEC-004 + SPEC-006)

## V. REFERENCES

| Document | Path |
|:--|:--|
| Governing Plan | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/plan_T104-PH001-ST008-AC006.md` |
| TK002 Proposal | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/proposal/proposal_T104-PH001-ST008-AC006_governance-input-disposition.md` |
| TK001.1 Comparative Analysis | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/analysis/analysis_T104-PH001-ST008-AC006-TK001.1_implementation-artifact-architecture-assessment.md` |
| Stream Notes Register | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/notes_T104-PH001-ST008.md` |
| Implementation Guideline | `prompt/templates/consultant/workspace/guideline_workspace_implementation.md` |
| Plan Guideline | `prompt/templates/consultant/workspace/guideline_workspace_plan.md` |

## VI. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-03-28 | Initial | Implementation specification authored for SES003 Phase A (plan housekeeping — status corrections, gate-readiness stack renumbering, §III section updates, stream notes registration) and Phase B (TK002 v2.1.0 — CONV-022 resolution with Option B naming convention from TK001.1). Seven SPEC items covering two target files (plan, proposal) plus one ancillary file (stream notes register). Execution sequence defined with parallelization opportunities. |
