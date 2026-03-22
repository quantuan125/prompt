---
artifact_type: 'IMPLEMENTATION'
implementation_type: 'task_specification'
initiative_id: 'T104'
initiative_code: 'CWS'
phase: '1'
stream_id: 'T104-PH001-ST008'
activity_id: 'T104-PH001-ST008-AC001.6'
task_id: 'T104-PH001-ST008-AC001.6-TK003.4'
version: '1.0.0'
date: '2026-03-22'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/plan_T104-PH001-ST008-AC001.6.md'
purpose: 'High-level consultant-owned remediation specification to normalize the AC001.6 GATE-001 package before client disposition and before any downstream developer commissioning.'
---

# IMPLEMENTATION (Task Specification): AC001.6 GATE-001 Package Remediation

## I. PURPOSE & AUTHORITY

- **Purpose**: This artifact specifies the high-level remediation work needed to make the AC001.6 `GATE-001` package internally consistent, client-ready, and safe to hand forward into downstream implementation commissioning.
- **Authority chain**: AC001.6 plan remains the tracked-work authority -> this artifact specifies the package-normalization HOW -> revised gate-package artifacts become the client-facing evidence surface for disposition.
- **Audience**: LLM_Consultant (primary executor), Client (review consumer).
- **Boundary**: This artifact does NOT authorize Phase 2 developer implementation. It is a pre-commissioning normalization artifact for the gate package itself.
- **Trigger**: `analysis_T104-PH001-ST008-AC001.6-GATE-001_external-review.md` identified package-structure, linkage, and downstream-authority gaps that should be corrected before client disposition or, at minimum, encoded as gate conditions.

## II. TASK SCOPE

- **Governing plan task**: Proposed consultant follow-on `T104-PH001-ST008-AC001.6-TK003.4` (package remediation / normalization) pending explicit plan registration.
- **Trigger**: External review found five bounded package issues: proposal structure drift, missing gate-consumed Client Summary, incomplete post-SES003 package normalization, GIR-002 / GIR-010 enforcement mismatch, and downstream commissioning authority drift.
- **Deliverable contract**: Normalized proposal, normalized analysis/package metadata, normalized plan/gate dependency surfaces, and explicit client-facing recommendation posture.
- **Depends On**: `analysis_T104-PH001-ST008-AC001.6-GATE-001_external-review.md`

## III. CONTEXT & RATIONALE

The AC001.6 package is substantively strong, but the package-control surfaces evolved across TK003, TK003.1, TK003.2, and TK003.3 without a final normalization pass. The external review concludes that:

1. The client can disposition the substantive GIR set.
2. The package should not hand straight into developer commissioning without consultant-owned normalization.
3. The corrective work is bounded and does not require reopening the main architectural decisions.

This remediation artifact therefore focuses on package coherence, not on changing the approved technical direction.

## IV. SPECIFICATION ITEMS

### SPEC-001 — Normalize the GATE-001 Proposal to Current `gate_disposition` Contract

| Field | Detail |
|:--|:--|
| Requirement Source | External review GAP-001 |
| Target | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/proposal/proposal_T104-PH001-ST008-AC001.6-GATE-001_gir-disposition-package.md` |
| Acceptance Criteria | Proposal follows current `gate_disposition` section ordering; Section II contains both Gate Package Index and Evidence Index using the required schemas; frontmatter includes the appropriate external-review linkage; package navigation is client-ready |
| Status | `open` |

#### Implementation Detail

Restructure the proposal to align with `guideline_workspace_proposal.md` §V.B. The goal is not to change the GIR substance; it is to present the package in the current contract shape so the client can navigate the evidence cleanly. The Gate Package section should distinguish client-priority deliverables from the broader Evidence Index. The normalized package must expose the external review, SES003-driven artifacts, and any package items that directly support GIR-008 through GIR-011.

---

### SPEC-002 — Add the Missing Gate-Consumed Client Summary to the Vertical Audit

| Field | Detail |
|:--|:--|
| Requirement Source | External review GAP-002; `guideline_workspace_analysis.md` §V.A |
| Target | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/analysis/analysis_T104-PH001-ST008-AC001.6_implementation-family-vertical-integration-audit.md` |
| Acceptance Criteria | Executive Summary includes a `Client Summary` subsection that accurately restates the audit body without introducing new findings or recommendations |
| Status | `open` |

#### Implementation Detail

Add a concise client-facing digest to the vertical integration audit because it is consumed directly at the gate via `analysis_reference`. Keep the body findings unchanged. The remediation is presentational and navigational, not substantive.

---

### SPEC-003 — Normalize Plan and Gate Surfaces After TK003.1-TK003.3

| Field | Detail |
|:--|:--|
| Requirement Source | External review GAP-003 |
| Target | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/plan_T104-PH001-ST008-AC001.6.md` |
| Acceptance Criteria | `GATE-001` dependency and entry criteria reflect all required pre-gate tasks; package-normalization task is registered if execution is authorized; downstream gate/implementation dependencies are internally coherent |
| Status | `open` |

#### Implementation Detail

Update the plan so the gate surface matches the actual package composition after SES003. This includes normalizing the gate dependency chain, reflecting the late-added consultant artifacts, and ensuring the plan does not imply that downstream work can start off stale or partially conditional authority. If the remediation is to be executed before disposition, register the remediation task explicitly in the plan.

---

### SPEC-004 — Harmonize GIR-002 and GIR-010 into One Explicit DEV-REPORT Traceability Posture

| Field | Detail |
|:--|:--|
| Requirement Source | External review GAP-004 |
| Target | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/proposal/proposal_T104-PH001-ST008-AC001.6-GATE-001_gir-disposition-package.md`; client-facing recommendation basis |
| Acceptance Criteria | The package explicitly states how GIR-002 and GIR-010 relate, and the client is not asked to approve two different enforcement strengths for the same linkage objective |
| Status | `open` |

#### Implementation Detail

Retain the substantive traceability goal. Clarify whether GIR-002 is the policy objective and GIR-010 is the bounded implementation mechanism, or whether both are intended to operate at the same normative strength. The preferred high-level resolution is: GIR-002 defines the problem and desired traceability outcome; GIR-010 defines the concrete bounded implementation shape using `implementation_reference` as a `SHOULD` field unless the client explicitly chooses a stronger `MUST` posture.

---

### SPEC-005 — Normalize Downstream Commissioning Authority Before Developer Handoff

| Field | Detail |
|:--|:--|
| Requirement Source | External review GAP-005 |
| Target | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/implementation/implementation_T104-PH001-ST008-AC001.6_vertical-integration-task-specification.md`; `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/plan_T104-PH001-ST008-AC001.6.md` |
| Acceptance Criteria | Downstream implementers can determine the authoritative Phase 2 scope without conflicting GIR mappings or invalid dependency assumptions; conditional tasks are handled conditionally in the plan |
| Status | `open` |

#### Implementation Detail

Normalize or explicitly downgrade the older vertical implementation specification so it cannot be misread as the final downstream authority surface. The package should make clear which implementation artifact governs which GIR cluster. Also normalize the plan so `TK010` and later work do not depend unconditionally on tasks that only execute when the gate explicitly approves those optional changes.

## V. IMPLEMENTATION SEQUENCE

```
SPEC-001  Normalize gate-disposition proposal structure and package indices
SPEC-002  Add gate-consumed Client Summary to vertical audit
SPEC-003  Normalize plan and gate surfaces after SES003
SPEC-004  Harmonize GIR-002 and GIR-010 traceability posture
SPEC-005  Normalize downstream commissioning authority before developer handoff
```

**Execution note**: SPEC-001, SPEC-002, and SPEC-003 may begin independently. SPEC-004 should be integrated while normalizing the proposal. SPEC-005 should complete before any downstream developer commissioning is authorized.

## VI. TARGET FILES REGISTER

| # | File Path | Authority | Change Type | Confirmed? |
|:--|:--|:--|:--|:--|
| 1 | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/proposal/proposal_T104-PH001-ST008-AC001.6-GATE-001_gir-disposition-package.md` | T104 | Amend | Yes |
| 2 | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/analysis/analysis_T104-PH001-ST008-AC001.6_implementation-family-vertical-integration-audit.md` | T104 | Amend | Yes |
| 3 | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/plan_T104-PH001-ST008-AC001.6.md` | T104 | Amend | Yes |
| 4 | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/implementation/implementation_T104-PH001-ST008-AC001.6_vertical-integration-task-specification.md` | T104 | Amend or reclassify-as-preliminary | Yes |

## VII. REFERENCES

| Document | Path |
|:--|:--|
| External review | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/analysis/analysis_T104-PH001-ST008-AC001.6-GATE-001_external-review.md` |
| Governing plan | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/plan_T104-PH001-ST008-AC001.6.md` |
| Gate proposal | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/proposal/proposal_T104-PH001-ST008-AC001.6-GATE-001_gir-disposition-package.md` |
| Vertical audit | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/analysis/analysis_T104-PH001-ST008-AC001.6_implementation-family-vertical-integration-audit.md` |
| Vertical implementation spec | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/implementation/implementation_T104-PH001-ST008-AC001.6_vertical-integration-task-specification.md` |
| Horizontal implementation spec | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/implementation/implementation_T104-PH001-ST008-AC001.6_horizontal-development-task-specification.md` |
| Proposal guideline | `prompt/templates/consultant/workspace/guideline_workspace_proposal.md` |
| Analysis guideline | `prompt/templates/consultant/workspace/guideline_workspace_analysis.md` |
| Plan guideline | `prompt/templates/consultant/workspace/guideline_workspace_plan.md` |
| Implementation guideline | `prompt/templates/consultant/workspace/guideline_workspace_implementation.md` |

## VIII. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-03-22 | Initial | High-level consultant-owned remediation specification for AC001.6 GATE-001 package normalization. Derived from the external review and focused on package completeness, client-facing clarity, and downstream commissioning readiness. |
