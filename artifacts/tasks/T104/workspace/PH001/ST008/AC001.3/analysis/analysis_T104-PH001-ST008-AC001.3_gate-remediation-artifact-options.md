---
artifact_type: 'ANALYSIS'
analysis_type: 'assessment'
initiative_id: 'T104'
initiative_code: 'CWS'
phase: '1'
stream_id: 'T104-PH001-ST008'
activity_id: 'T104-PH001-ST008-AC001.3'
version: '1.0.0'
date: '2026-03-17'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.3/plan_T104-PH001-ST008-AC001.3.md'
purpose: 'Decision input assessing architecture options for where gate remediation implementation details should live, using live workspace patterns and external quality/remediation practice as grounding.'
---

# ANALYSIS: Gate Remediation Artifact Options (`T104-PH001-ST008-AC001.3`)

## I. EXECUTIVE SUMMARY

**Purpose**: Evaluate the architectural options for storing gate remediation implementation details in the workspace suite and produce a decision-ready recommendation.

**Scope**: This assessment reviews the current workspace artifact inventory, the live AC009 and T104 examples, and the tradeoffs between plan-only, verification-supplement, proposal-attached, dedicated-artifact, and hybrid patterns.

**Conclusion / Recommendation**: The recommended durable model is a **hybrid**: the plan remains the authority for tracked remediation work, while a separate dedicated remediation package holds implementation detail. As an interim rule, a supplementary `verification_*_revision-checklist` is acceptable for AC009 only, but it should not become the permanent standard by drift.

## II. SCOPE & INPUTS

**In scope**:
- Where remediation implementation details should live when discovered at a gate
- Role ownership, auditability, implementer usability, and drift resistance
- Compatibility with current workspace artifact taxonomy
- Interim handling rule for the current AC009 recycle loop

**Out of scope**:
- Editing workspace guidelines/templates in this cycle
- Finalizing file naming for a new dedicated artifact family
- Retroactively normalizing historical gate packages

**Inputs reviewed (repo-relative paths)**:
- `prompt/templates/consultant/workspace/workspace_documentation_rules.md`
- `prompt/templates/consultant/workspace/guideline_workspace_plan.md`
- `prompt/templates/consultant/workspace/guideline_workspace_verification.md`
- `prompt/templates/consultant/workspace/guideline_workspace_proposal.md`
- `prompt/templates/consultant/workspace/guideline_workspace_analysis.md`
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/analysis/analysis_P-PH000-ST001-AC009_external-review_gate-001-package.md`
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/verification/verification_P-PH000-ST001-AC009_gate-001_revision-checklist.md`
- `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC002/verification/verification_T104-PH001-ST008-AC002_gate-002_revision-checklist.md`
- `prompt/artifacts/tasks/T104/workspace/PH001/ST008/notes_T104-PH001-ST008.md`

## III. EVIDENCE / METHODOLOGY

**Method**:
- Compared the current workspace artifact inventory and role-boundary rules against live examples where remediation detail had to be carried at a gate.
- Evaluated each candidate architecture against the same criteria: role ownership, gate readability, implementer usability, audit integrity, anti-drift posture, compatibility with the current taxonomy, and migration cost.
- Used the AC009 and T104 ST008 live cases as the immediate test scenarios.

**Evidence notes**:
- The current repo already supports supplementary `revision-checklist` verification files, which makes them viable as an interim containment mechanism.
- The client has explicitly rejected `assessment` as the durable home of remediation implementation detail.
- The current plan guideline is strong for authority tracking but intentionally avoids embedding large implementation-detail payloads in the plan body.
- The proposal guideline is client-facing and therefore not the best durable surface for implementer-directed corrective-action detail.

## IV. FINDINGS / GAP REGISTER

| GAP ID | Category | Title | Description | Disposition | Downstream Target | Notes |
|:--|:--|:--|:--|:--|:--|:--|
| GAP-001 | workflow | No durable artifact contract exists for remediation implementation detail | The current suite can carry remediation details temporarily, but it does not yet define a stable final home for them separate from plans and client proposals. | `pending_decision` | `T104-PH001-ST008-AC001.3-GATE-001` | This is the core architecture decision for this sub-activity. |
| GAP-002 | workflow | Plan-only handling overloads planning surfaces | Plans are the authority for tracked work, but they are a poor long-form host for dense remediation implementation detail. | `resolved` | `T104-PH001-ST008-AC001.3-GATE-001` | Resolved in option comparison: not recommended as final model. |
| GAP-003 | workflow | Verification-supplement is useful but ownership-biased | Supplementary verification works as an interim handoff, but it centers the artifact under verification semantics and does not fully solve the broader workflow-model question. | `resolved` | `T104-PH001-ST008-AC001.3-GATE-001` | Acceptable interim model only. |
| GAP-004 | workflow | Proposal-attached remediation detail conflicts with client-facing posture | The gate-disposition proposal should explain the decision package to the client, not become the long-form remediation contract for implementers. | `resolved` | `T104-PH001-ST008-AC001.3-GATE-001` | Not recommended as final model. |

## V. ASSESSMENT (READINESS / OPTIONS / TRADEOFFS)

### A. Current State Summary

- The workspace suite has strong separation between plan authority, reviewer verification, consultant proposal, and consultant analysis.
- None of the current artifact families is a perfect fit for durable remediation implementation detail discovered at a gate.
- AC009 needs immediate corrective-action detail, but the long-term standard should not be set ad hoc inside that one gate package.

### B. Options

1. **Plan-only model**
- Remediation implementation details live only in the activity plan.
- Strength: strongest authority linkage.
- Weakness: bloats plans, mixes tracking with execution detail, poor LLM retrieval ergonomics.
- Assessment: reject as durable model.

2. **Supplementary verification model**
- Use `verification_*_revision-checklist` as the standard home.
- Strength: already supported, reviewer-handoff-friendly, auditable.
- Weakness: over-anchors the pattern under verification semantics even when the detail is broader than reviewer findings.
- Assessment: acceptable interim model; weak as the permanent answer.

3. **Proposal-attached annex model**
- Attach remediation detail to the gate-disposition proposal.
- Strength: one package for the client.
- Weakness: wrong audience, client-facing surface becomes overloaded, weak implementer ergonomics.
- Assessment: reject as durable model.

4. **Dedicated remediation artifact family**
- Introduce a separate artifact family specifically for remediation implementation detail.
- Strength: cleanest semantic fit and audience targeting.
- Weakness: requires new taxonomy, naming rule, template, guideline, and migration posture.
- Assessment: strong candidate, but higher governance cost.

5. **Hybrid model**
- Keep the plan as the formal tracked-work authority.
- Use a separate remediation package artifact for detailed corrective-action implementation.
- Permit a temporary supplementary verification checklist where no dedicated family yet exists.
- Strength: best balance of authority, usability, auditability, and anti-drift control.
- Weakness: requires one more explicit contract between plan and remediation package.
- Assessment: recommended.

### C. Recommendation

- **Recommended durable direction**: Option 5, hybrid model.
- **Recommended interim rule**: until the dedicated remediation package model is formally implemented, a supplementary `verification_*_revision-checklist` may be used as a temporary containment surface when the client explicitly approves that posture.
- **Reason**: the hybrid model preserves plan authority while avoiding plan bloat, avoids turning the proposal into an implementer spec, and creates a clean path to a future dedicated artifact family if the client approves that later.

## VIII. DOWNSTREAM ACTIONS

| downstream_artifact_type | target_reference | trigger_condition | responsible_role | notes |
|:--|:--|:--|:--|:--|
| PROPOSAL | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.3/proposal/proposal_T104-PH001-ST008-AC001.3-GATE-001_gir-disposition-package.md` | Options analysis complete | LLM_Consultant | Convert the recommendation into explicit client architecture options and interim-rule language. |
| PLAN | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.3/plan_T104-PH001-ST008-AC001.3.md` | Gate-001 decision approved | LLM_Consultant | Use the approved model to drive the follow-on amendment-input task. |
| GUIDELINE / RULES INPUT | `prompt/templates/consultant/workspace/workspace_documentation_rules.md` | AC001.3 Gate-001 approves a durable model | LLM_Consultant | Deferred by design from this cycle. |
| GUIDELINE / RULES INPUT | `prompt/templates/consultant/workspace/guideline_workspace_plan.md` | AC001.3 Gate-001 approves a durable model | LLM_Consultant | Follow-on amendment only; no direct edit in this cycle. |
| GUIDELINE / RULES INPUT | `prompt/templates/consultant/workspace/guideline_workspace_verification.md` | AC001.3 Gate-001 approves a durable model | LLM_Consultant | Follow-on amendment only; no direct edit in this cycle. |

## IX. REFERENCES / LINKS REGISTER

| Item | Reference |
|:--|:--|
| AC001.3 Plan | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.3/plan_T104-PH001-ST008-AC001.3.md` |
| Workspace Documentation Rules | `prompt/templates/consultant/workspace/workspace_documentation_rules.md` |
| Plan Guideline | `prompt/templates/consultant/workspace/guideline_workspace_plan.md` |
| Verification Guideline | `prompt/templates/consultant/workspace/guideline_workspace_verification.md` |
| Proposal Guideline | `prompt/templates/consultant/workspace/guideline_workspace_proposal.md` |
| Analysis Guideline | `prompt/templates/consultant/workspace/guideline_workspace_analysis.md` |
| AC009 External Review | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/analysis/analysis_P-PH000-ST001-AC009_external-review_gate-001-package.md` |
| AC009 Temporary Revision Checklist | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/verification/verification_P-PH000-ST001-AC009_gate-001_revision-checklist.md` |
| T104 AC002 Revision Checklist Example | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC002/verification/verification_T104-PH001-ST008-AC002_gate-002_revision-checklist.md` |

## X. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-03-17 | Initial | Assessed five architecture options for storing gate remediation implementation detail. Recommended a hybrid durable model (plan authority + separate remediation package), while allowing temporary supplementary revision-checklist usage as an interim rule. |
