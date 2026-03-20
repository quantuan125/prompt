---
artifact_type: 'PROPOSAL'
initiative_id: 'T104'
initiative_code: 'CWS'
phase: '1'
stream_id: 'T104-PH001-ST008'
activity_id: 'T104-PH001-ST008-AC001.4'
task_id: 'T104-PH001-ST008-AC001.4-TK004'
gate_id: 'T104-PH001-ST008-AC001.4-GATE-001'
version: '1.2.0'
date: '2026-03-20'
status: 'completed'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.4/plan_T104-PH001-ST008-AC001.4.md'
analysis_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.4/analysis/analysis_T104-PH001-ST008-AC001.4_gate-impact-classification-assessment.md'
external_review_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.4/analysis/analysis_T104-PH001-ST008-AC001.4-GATE-001_external-review.md'
purpose: 'Decision disposition package for GATE-001: Client approval of gate impact classification governance model'
consumers:
  - 'T104-PH001-ST008-AC001.4-GATE-001'
---

# PROPOSAL: Gate Disposition Package - Gate Impact Classification Governance Model (T104-PH001-ST008-AC001.4-GATE-001)

## I. EXECUTIVE SUMMARY

- **Context**: Assessment analysis (`TK003`) evaluated the governance gap where workspace rules handle internal gate recycle but lack provisions for external baseline change events. The analysis is grounded in five industry change-management frameworks (PRINCE2, Cooper Stage-Gate, PMI PMBOK 7, NASA NPR 7120.5, ISO 21502).
- **Goal at gate**: Client approval of the governance model — impact taxonomy, decision-boundary test, gate supersession mechanics, GDR extensions, analysis deprecation model, and Situation C disposition — so that guideline patches (TK005–TK008) and retroactive AC002 application guidance (TK009) may proceed.
- **Scope**: This gate approves the **governance model only**. It does not approve specific guideline wording (that is GATE-002 after implementation).

---

## II. GATE PACKAGE

### A. Gate Package Index

| Deliverable | Producing Task | Status | Acceptance | Client Priority | Path |
|:--|:--|:--|:--|:--|:--|
| AC001.4 Sub-Activity Plan | `TK001` | `completed` | `accepted` | Reference | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.4/plan_T104-PH001-ST008-AC001.4.md` |
| AC001.4 Consultation Session Notes (SES001) | `TK002` | `completed` | `accepted` | Reference | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.4/snotes/snotes_T104-PH001-ST008-AC001.4-SES001.md` |
| Gate Impact Classification Assessment Analysis | `TK003` | `completed` | `pending` | **Required** | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.4/analysis/analysis_T104-PH001-ST008-AC001.4_gate-impact-classification-assessment.md` |
| GATE-001 Gate-Disposition Proposal (this file) | `TK004` | `completed` | `pending` | **Required** | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.4/proposal/proposal_T104-PH001-ST008-AC001.4-GATE-001_gir-disposition-package.md` |
| GATE-001 External Review | `TK004.1` | `completed` | `pending` | **Required** | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.4/analysis/analysis_T104-PH001-ST008-AC001.4-GATE-001_external-review.md` |

### B. Evidence Index

| Evidence Type | Artifact | Path | Notes |
|:--|:--|:--|:--|
| Assessment Analysis | Gate Impact Classification Assessment | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.4/analysis/analysis_T104-PH001-ST008-AC001.4_gate-impact-classification-assessment.md` | Primary evidence — industry-grounded governance model with 7-scenario decision test |
| External Review | GATE-001 Package Review | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.4/analysis/analysis_T104-PH001-ST008-AC001.4-GATE-001_external-review.md` | Independent package review confirming GIR posture and package sufficiency for client disposition |
| Session Notes | AC001.4 SES001 (Consultation) | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.4/snotes/snotes_T104-PH001-ST008-AC001.4-SES001.md` | Consultation decisions DEC001–DEC008 establishing sub-activity scope and boundaries |
| Governing Plan | AC001.4 Sub-Activity Plan | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.4/plan_T104-PH001-ST008-AC001.4.md` | Task register and scope authority |
| Guideline (current) | Plan Guideline | `prompt/templates/consultant/workspace/guideline_workspace_plan.md` (v1.16.0) | §VI.K recycle rules — current internal-only scope |
| Guideline (current) | Proposal Guideline | `prompt/templates/consultant/workspace/guideline_workspace_proposal.md` (v1.5.0) | §VII GDR specification — current enum values |
| Guideline (current) | Verification Guideline | `prompt/templates/consultant/workspace/guideline_workspace_verification.md` (v1.7.0) | §VII Situation A/B rework paths |
| Guideline (current) | Workspace Documentation Rules | `prompt/templates/consultant/workspace/workspace_documentation_rules.md` (v3.0.0) | §7 workflow chain, §3 artifact type inventory |
| Exemplar (live) | P-PH000-ST002-AC002 Plan | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC002/plan_P-PH000-ST002-AC002.md` (v1.3.0) | Live exemplar of the governance gap — GATE-001 in recycle with external-impact hold |

---

## III. DISPOSITION SUMMARY REGISTER

| GIR ID | Gap/Topic | Decision Area | Recommended Option | Execution Target | Blocking | Client Decision |
|:--|:--|:--|:--|:--|:--|:--|
| GIR-001 | Impact Classification Taxonomy | Plan guideline §VI | (a) Binary Internal/External with classification test | TK005 | Yes | |
| GIR-002 | Decision-Boundary Test | Plan guideline §VI | (a) Two-question test (origin + boundary change) | TK005 | Yes | |
| GIR-003 | Client Decision Enum: `SUPERSEDE` | Proposal guideline §VII.C | (a) Add `SUPERSEDE` to Client Decision enum | TK006 | Yes | |
| GIR-004 | Gate Status Enum: `superseded` | Plan guideline §VI.D + Proposal guideline §VII.C | (a) Add `superseded` as gate-specific status | TK005 + TK006 | Yes | |
| GIR-005 | GDR Lifecycle Extension | Proposal guideline §VII.D | (a) Add Step 4a external-impact assessment branch | TK006 | Yes | |
| GIR-006 | Analysis Deprecation Model | Workspace rules §7.C + analysis-authority surfaces | (a) Three-layer model (frontmatter + Evidence Index + Links Register) | TK007 | Yes | |
| GIR-007 | Verification Situation C | Verification guideline §VII | (a) No Situation C — external impacts handled at plan/proposal level | TK008 | No | |
| GIR-008 | Workflow Chain Extension | Workspace rules §7.A | (a) Add external-impact assessment step | TK007 | Yes | |
| GIR-009 | Retroactive AC002 Application | P-PH000-ST002-AC002 | (a) Gate supersession: close GATE-001, create GATE-002 with v1.2.0 baseline, renumber existing GATE-002 to GATE-003 | TK009 | Yes | |

---

## IV. DETAILED DISPOSITION REGISTER

### GIR-001 — Impact Classification Taxonomy

Context:
- Current §VI.K assumes all gate disruptions are internal review findings. No rule distinguishes external baseline changes from internal rework.
- Five industry frameworks unanimously distinguish internal rework from external baseline change (PRINCE2 exception vs. issue; Cooper recycle vs. re-scope; PMI corrective vs. baseline change; NASA KDP re-baselining; ISO 21502 baseline integrity).

Decision prompt:
- Should the workspace adopt a binary Internal/External impact classification?

| Option | Description |
|:--|:--|
| **(a) Binary classification [Recommended]** | Two categories: Internal (from gate's own review) and External (from outside gate's review scope). Simple, deterministic, consistent with all five industry frameworks. |
| (b) Graduated classification | Three or more categories (e.g., minor external, major external, regulatory). More granular but adds classification complexity with limited benefit at this workspace's maturity level. |

Recommendation:
- (a) — Binary is sufficient. The Decision-Boundary Test (GIR-002) provides the needed granularity within the External category.

Rationale:
- All five frameworks use a binary distinction at the classification level. Granularity comes from the response mechanism, not the classification itself.

Client Decision:
- `[ ] (a)` / `[ ] (b)` / `[ ] Override: _______`

---

### GIR-002 — Decision-Boundary Test

Context:
- Not all external impacts require the same response. A standard amendment that changes the gate's normative baseline (decision boundary change) is fundamentally different from one that updates an input document without changing what the gate is deciding (inputs-only change).

Decision prompt:
- Should the workspace adopt a two-question Decision-Boundary Test to determine gate response for external impacts?

| Option | Description |
|:--|:--|
| **(a) Two-question test [Recommended]** | Q1: "Did the event originate from this gate's own review?" (Internal/External). Q2 (if External): "Does it change the decision boundary?" (Supersede if yes; recycle if no). Simple, deterministic, covers all 7 scenarios. |
| (b) Per-scenario lookup table only | Enumerate each scenario with its response in a static table. No generalized test — practitioners look up their scenario. Risk: new scenarios not covered by the table fall through. |

Recommendation:
- (a) — A generalized test is more robust than a fixed lookup table. The 7-scenario table serves as validation examples, not the primary decision mechanism.

Rationale:
- Cooper Stage-Gate and NASA NPR 7120.5 both use a generalized impact-assessment step rather than scenario enumeration.

Client Decision:
- `[ ] (a)` / `[ ] (b)` / `[ ] Override: _______`

---

### GIR-003 — Client Decision Enum: `SUPERSEDE`

Context:
- Current Client Decision values: `APPROVE`, `APPROVE WITH CONDITIONS`, `RECYCLE`, `REJECT`. None of these semantically match "the gate's baseline moved; close it and create a successor."
- `RECYCLE` implies same-gate reassessment (same question, better answer). `REJECT` implies failure. Neither is correct for external baseline change.

Decision prompt:
- Should `SUPERSEDE` be added to the Client Decision enum?

| Option | Description |
|:--|:--|
| **(a) Add `SUPERSEDE` [Recommended]** | New enum value with clear semantics: gate closed due to external baseline change, prior assessment preserved as historical, successor gate created. |
| (b) Overload `RECYCLE` with annotation | Use `RECYCLE` with a free-text annotation explaining the external-impact nature. Avoids enum change but creates semantic ambiguity — practitioners cannot distinguish internal recycle from external supersession by enum alone. |
| (c) Overload `REJECT` with annotation | Use `REJECT` with annotation. Semantically incorrect — rejection implies quality failure, which external impact is not. |

Recommendation:
- (a) — Clean enum semantics. `SUPERSEDE` is the correct term (used in PRINCE2, ISO document management, and contract law for exactly this concept).

Rationale:
- Overloading existing values creates classification ambiguity and makes automated tooling harder. A dedicated value is a bounded, low-cost extension.

Client Decision:
- `[ ] (a)` / `[ ] (b)` / `[ ] (c)` / `[ ] Override: _______`

---

### GIR-004 — Gate Status Enum: `superseded`

Context:
- Current gate status values: `planned`, `in_progress`, `completed`, `failed` (gate-only terminal per §VI.D).
- When `Client Decision = SUPERSEDE`, the gate needs a status that communicates "validly assessed but no longer current."

Decision prompt:
- Should `superseded` be added to the gate status enum?

| Option | Description |
|:--|:--|
| **(a) Add `superseded` as gate-specific status [Recommended]** | Parallel to `failed` being gate-only: `superseded` is gate-only and communicates that the gate's work was valid for its baseline but the baseline moved. Does not enter the general P-STD-002 work-item vocabulary. |
| (b) Reuse `cancelled` from P-STD-002 | Semantically imprecise — `cancelled` implies deliberate termination before completion, not completion-under-old-baseline. |

Recommendation:
- (a) — Gate-specific status, consistent with `failed` precedent. Clear semantics.

Rationale:
- `superseded` is not `cancelled` (which implies no completion) and not `failed` (which implies quality failure). It is a third terminal state specific to gates.

Client Decision:
- `[ ] (a)` / `[ ] (b)` / `[ ] Override: _______`

---

### GIR-005 — GDR Lifecycle Extension

Context:
- Current GDR lifecycle (§VII.D) has 7 steps, all assuming the gate's own review triggered any change. No step exists for external-impact assessment or supersession recording.

Decision prompt:
- Should the GDR lifecycle be extended with a Step 4a for external-impact assessment?

| Option | Description |
|:--|:--|
| **(a) Add Step 4a external-impact branch [Recommended]** | New lifecycle step: when external impact detected, perform classification → decision-boundary test → if boundary changed, record `SUPERSEDE` in GDR and create successor gate; if boundary unchanged, continue existing lifecycle with updated inputs. |
| (b) Handle externally via plan amendment only | No GDR lifecycle change — external impacts are handled entirely at the plan level with informal annotations. GDR records only the final decision without the external-impact trail. |

Recommendation:
- (a) — The GDR should be self-documenting. Recording the supersession decision in the GDR provides audit traceability at the decision surface, not just the plan surface.

Rationale:
- NASA NPR 7120.5 and ISO 21502 both record re-baselining decisions at the decision-point authority level, not only in project plans.

Client Decision:
- `[ ] (a)` / `[ ] (b)` / `[ ] Override: _______`

---

### GIR-006 — Analysis Deprecation Model

Context:
- Consultation DEC005 approved a three-layer deprecation model: (1) frontmatter `superseded` status + deprecation notice, (2) Evidence Index historical subsection, (3) plan Links Register annotation.

Decision prompt:
- Should the three-layer model be codified as the standard analysis artifact deprecation mechanism?

| Option | Description |
|:--|:--|
| **(a) Three-layer model [Recommended]** | Layer 1: Frontmatter `status: 'superseded'` + `superseded_by` key + deprecation notice. Layer 2: Evidence Index moves superseded items to `Historical Evidence` subsection. Layer 3: Plan Links Register adds `superseded` annotation. Self-documenting at all three surfaces. |
| (b) Frontmatter-only | Only mark `status: 'superseded'` in frontmatter. Simpler but Evidence Index and Links Register remain ambiguous. |

Recommendation:
- (a) — Full three-layer model. Each layer serves a different audience (artifact reader, gate reviewer, plan navigator). The cost is low (3 update points per deprecation event).

Rationale:
- Consistent with the workspace's "Link Don't Duplicate" principle (T104-CON-001): each surface links to the successor rather than duplicating the deprecation status.

Client Decision:
- `[ ] (a)` / `[ ] (b)` / `[ ] Override: _______`

---

### GIR-007 — Verification Situation C

Context:
- Verification guideline §VII defines Situation A (deliverable deficiency) and Situation B (scope gap). Both assume internal origin.
- Assessment analysis recommends **no Situation C** because external impacts are not verification findings — they are plan-level events.

Decision prompt:
- Should a Situation C (external impact) be added to the verification guideline's rework taxonomy?

| Option | Description |
|:--|:--|
| **(a) No Situation C [Recommended]** | External impacts are classified and resolved at the plan/proposal level, not the verification level. If an external impact occurs during verification, the verification pauses and escalates to the plan. No change to verification guideline rework paths. |
| (b) Add Situation C | New rework path for external baseline change. Risk: mixes verification-level concerns (deliverable quality) with plan-level concerns (baseline validity), making the verification guideline responsible for scope beyond its design. |

Recommendation:
- (a) — Keep verification focused on implementation quality. External impacts belong at the plan/proposal governance layer.

Rationale:
- Verification guideline's scope statement (§I) explicitly covers "implementation-backed gate reviews." External baseline changes are a governance concern, not an implementation-quality concern.

Client Decision:
- `[ ] (a)` / `[ ] (b)` / `[ ] Override: _______`

---

### GIR-008 — Workflow Chain Extension

Context:
- Workspace documentation rules §7.A defines two workflow chain variants (implementation-backed and consultation-only). Neither includes an external-impact assessment step.

Decision prompt:
- Should the workflow chain include an external-impact assessment step?

| Option | Description |
|:--|:--|
| **(a) Add external-impact assessment step [Recommended]** | Add a conditional branch in §7.A: when an external event affects a gate's normative baseline, an impact assessment step (using the classification test from GIR-001/GIR-002) precedes the gate disposition. This is a conditional step, not a mandatory one for every gate. |
| (b) No workflow chain change | Handle external impacts entirely within plan amendments and session notes. Workflow chain remains unchanged. Risk: the canonical workflow chain becomes incomplete — practitioners don't see external-impact handling as part of the governed process. |

Recommendation:
- (a) — The workflow chain should be complete. An external-impact assessment is a conditional step that activates only when an external event is detected.

Rationale:
- ISO 21502 explicitly includes change assessment as a workflow step, not an ad-hoc process.

Client Decision:
- `[ ] (a)` / `[ ] (b)` / `[ ] Override: _______`

---

### GIR-009 — Retroactive AC002 Application

Context:
- `P-PH000-ST002-AC002-GATE-001` is in a same-gate recycle loop with a HOLD annotation. The trigger was `P-STD-002 v1.2.0` (external standard amendment), not an internal review finding. Under the proposed governance model, this is a decision-boundary external impact requiring gate supersession.

Decision prompt:
- Should the AC002 gate be restructured from RECYCLE to SUPERSEDE using the approved governance model?

| Option | Description |
|:--|:--|
| **(a) Gate supersession [Recommended]** | Close GATE-001 with `SUPERSEDE`. Create GATE-002 for v1.2.0 baseline. Renumber existing GATE-002 (implementation acceptance) to GATE-003. Deprecate superseded analysis artifacts. Full mechanics detailed in TK009 application guidance (post-GATE-001 approval). |
| (b) Continue same-gate recycle | Keep the current RECYCLE treatment and assess against v1.2.0 under the same gate. Semantically incorrect under the proposed model but avoids gate restructure complexity. |

Recommendation:
- (a) — The AC002 case is the canonical exemplar of the governance gap. Applying the correct model retroactively validates the governance framework and serves as the reference implementation for future external-impact events.

Rationale:
- The consultation (SES001 DEC002) already established forward amendment as the application method. The remediation work (TK001.3–TK001.7) was completed against the v1.2.0 baseline, so it carries forward into the successor gate package. The restructure is mechanical, not a scope change.

Client Decision:
- `[ ] (a)` / `[ ] (b)` / `[ ] Override: _______`

---

## V. GATE RECOMMENDATION

Recommendation state:
- `N/A — decision gate`

Conditions and/or deferrals:
- Recommended client posture: `APPROVE WITH CONDITIONS`.
- Condition 1: GIR-006 implementation MUST use widened `TK007` coverage across `workspace_documentation_rules.md`, `guideline_workspace_analysis.md`, and `template_workspace_analysis.md`.
- GIR-007 (Situation C) is non-blocking — TK008 proceeds regardless of the decision, documenting either "no change" rationale or the Situation C addition.

Downstream enforcement:
- TK005–TK009 MUST NOT begin until this gate's GDR records `Client Decision = APPROVE` or `APPROVE WITH CONDITIONS`.
- If `APPROVE WITH CONDITIONS`: conditions will be incorporated into TK005–TK009 scope as appropriate.
- If specific GIR items are overridden: TK005–TK009 scope adjusts to implement the client's selected options.

---

## VI. GATE DECISION RECORD (GDR)

## Gate Decision Record

| Field | Value |
|:--|:--|
| Gate ID | `T104-PH001-ST008-AC001.4-GATE-001` |
| Consultant Recommendation | `APPROVE WITH CONDITIONS` |
| Client Decision | `APPROVE` |
| Gate Status After Decision | `completed` |
| Conditions (if any) | Condition 1 (from consultant recommendation, accepted by client): GIR-006 implementation MUST use widened TK007 coverage across `workspace_documentation_rules.md`, `guideline_workspace_analysis.md`, and `template_workspace_analysis.md`. |
| Decided By | Client |
| Decision Date | 2026-03-20 |
| Decision Reference | Client approval issued inline during AC001.4 consultation session (2026-03-20). All 9 GIR items approved with recommended option (a). TK009 owner reassigned from LLM_Consultant to LLM_Developer per client direction. |

---

## VII. REFERENCES

| Document | Path |
|:--|:--|
| Governing Plan | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.4/plan_T104-PH001-ST008-AC001.4.md` |
| Input Analysis | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.4/analysis/analysis_T104-PH001-ST008-AC001.4_gate-impact-classification-assessment.md` |
| External Review | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.4/analysis/analysis_T104-PH001-ST008-AC001.4-GATE-001_external-review.md` |
| Consultation Session Notes | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.4/snotes/snotes_T104-PH001-ST008-AC001.4-SES001.md` |
| Parent Stream Plan | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/plan_T104-PH001-ST008.md` |

---

## VIII. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.2.0 | 2026-03-20 | Gate Closure | GATE-001 closed. GDR updated to `guideline_workspace_proposal.md` v1.6.0 schema: `Reviewer Verdict` replaced with `Consultant Recommendation: APPROVE WITH CONDITIONS`. Client Decision recorded as `APPROVE` (all 9 GIR items option (a)). Gate Status set to `completed`. TK009 owner reassignment noted in Decision Reference. Proposal status set to `completed`. |
| v1.1.0 | 2026-03-20 | Update | Added `external_review_reference` and integrated the GATE-001 external review into the package/evidence indexes. Clarified GIR-006 execution target to the widened `TK007` coverage and updated the gate recommendation from unconditional readiness to `APPROVE WITH CONDITIONS` based on the package review. |
| v1.0.0 | 2026-03-20 | Initial | Gate-disposition proposal for GATE-001 (governance model approval). 9 GIR items: GIR-001 (impact taxonomy), GIR-002 (decision-boundary test), GIR-003 (Client Decision `SUPERSEDE`), GIR-004 (gate status `superseded`), GIR-005 (GDR lifecycle Step 4a), GIR-006 (three-layer deprecation model), GIR-007 (no Situation C), GIR-008 (workflow chain extension), GIR-009 (retroactive AC002 gate supersession). All recommended options are (a). |
