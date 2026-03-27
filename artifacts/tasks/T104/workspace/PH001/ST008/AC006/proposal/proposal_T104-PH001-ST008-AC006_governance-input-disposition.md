---
artifact_type: 'PROPOSAL'
initiative_id: 'T104'
initiative_code: 'CWS'
phase: '1'
stream_id: 'T104-PH001-ST008'
activity_id: 'T104-PH001-ST008-AC006'
task_id: 'T104-PH001-ST008-AC006-TK002'
version: '1.0.0'
date: '2026-03-27'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/plan_T104-PH001-ST008-AC006.md'
analysis_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/analysis/analysis_T104-PH001-ST008-AC006_implementation-governance-gap-analysis.md'
target_standards:
  - 'guideline_workspace_implementation.md'
  - 'template_workspace_implementation_task-specification.md'
  - 'guideline_workspace_analysis.md'
  - 'guideline_workspace_plan.md'
  - 'guideline_workspace_proposal.md'
  - 'guideline_workspace_notes.md'
  - 'workspace_documentation_rules.md'
purpose: 'Package the governance direction for implementation-spec precision, commissioning rules, authoritative-review selection, standards-input enforcement, same-gate QA tracking, and role-protocol distinction for client disposition before downstream implementation begins.'
---

# PROPOSAL: Standards Input — IMPLEMENTATION Governance Hardening

## I. PURPOSE

- **Proposal objective**: Approve the governance direction for eight identified gaps so downstream implementation (TK004) can apply the approved rule changes to the seven target governance files.
- **Input scope**: Pre-implementation governance rules only. This proposal defines the conventions that must govern how IMPLEMENTATION artifacts are authored, reviewed, commissioned, and tracked. It does not implement the rules — that is TK004 scope after `GATE-001` approval.
- **Target standards**: `guideline_workspace_implementation.md`, `template_workspace_implementation_task-specification.md`, `guideline_workspace_analysis.md`, `guideline_workspace_plan.md`, `guideline_workspace_proposal.md`, `guideline_workspace_notes.md`, `workspace_documentation_rules.md`

---

## II. CURRENT STATE SUMMARY

### A. Baseline

The workspace governance suite (v3.6.0 rules, v1.19.0 plan guideline, v1.9.0 analysis guideline, v1.9.0 proposal guideline, v1.4.0 implementation guideline) already provides:
- IMPLEMENTATION artifact family with two subtypes (`remediation_specification`, `task_specification`)
- CONV-012 hybrid SPEC structure (metadata table + prose `Implementation Detail`)
- CONV-013 `execution_audience` distinction
- CONV-014 `standards_input` boundary (guidance-level)
- Gate-Readiness Stack with consultation-only and implementation-backed variants
- External-review scope requirements for gate-readiness input
- Role boundaries with consultant authorship and developer execution separation
- Gate Package Index and Evidence Index structure in `gate_disposition` proposals

### B. Problems / Gaps

| Gap ID | Category | Description | Impact |
|:--|:--|:--|:--|
| GAP-001 | workflow | CONV-012 defines SPEC structure but no minimum-detail floor. Summary-level SPECs pass unchallenged. | Developer receives ambiguous specifications; execution quality depends on inference rather than explicit authority. |
| GAP-002 | workflow | External reviews do not assess per-SPEC commissionability for downstream execution. | Vague or incomplete SPECs survive gate review; QA catches failures only after gate approval. |
| GAP-003 | lifecycle | No rule designates one authoritative external review when a gate package contains multiple review-like analyses. | Client cannot determine which review is the definitive gate-readiness signal; ad hoc resolution required per gate. |
| GAP-004 | consistency | Consultant-to-executor commissioning is allowed but not required to flow through an IMPLEMENTATION artifact. | Governed delegated execution could bypass the specification surface designed to ensure execution quality. |
| GAP-005 | workflow | `standards_input` boundary for premature concrete artifacts is SHOULD-level with no enforcement mechanism. | Premature concrete artifacts can surface as active gate evidence without triggering a governance violation. |
| GAP-006 | workflow | Same-gate QA correction is tracked ad hoc with no cross-surface tracking requirement. | Corrections to plan, notes, and proposal surfaces can diverge or be silently folded into live artifacts. |
| GAP-007 | consistency | No rule distinguishes consultant-only operational surfaces from broader multi-role protocol surfaces. | Operational scope confusion between consultant-scoped and program-wide surfaces. |
| GAP-008 | consistency | AC003 still uses analysis-based implementation-spec pattern while IMPLEMENTATION family is canonical. | Cross-family inconsistency persists as live vertical-integration evidence. |

---

## III. PROPOSED CONVENTIONS

### A. Convention Set
 
| Convention ID | Rule | Rationale | Authority Link |
|:--|:--|:--|:--|
| CONV-015 | Every execution-facing SPEC item MUST name at minimum: (a) exact target file(s)/surface(s), (b) required end-state posture, (c) validation checks, and (d) explicit non-target constraints. A SPEC item missing any of these four elements MUST be treated as draft-incomplete and MUST NOT be commissioned for execution. | The AC004 case showed that a SPEC with summary-level content passed external review unchallenged. A minimum-detail floor prevents under-specified SPECs from entering the execution pipeline. | `guideline_workspace_implementation.md` §IV (amend CONV-012) |
| CONV-016 | When an `external_review` analysis serves as a gate-readiness input and the gate package includes an IMPLEMENTATION artifact, the review MUST assess whether each execution-facing SPEC item meets the CONV-015 minimum-detail floor and is independently commissionable for the stated `execution_audience`. | The AC004 external review did not detect the vague implementation spec because per-SPEC commissionability was not a review requirement. | `guideline_workspace_analysis.md` §IV.B (`external_review` lifecycle) |
| CONV-017 | When a gate package contains multiple ANALYSIS artifacts of type `external_review`, the gate-disposition proposal MUST designate exactly one as the **authoritative external review** for that gate. Other review-like analyses are classified as supporting or historical evidence in the Evidence Index. | The AC004 package surfaced two external reviews without explicit authority ordering. The authoritative designation was resolved ad hoc in the QA assessment. | `guideline_workspace_analysis.md` (new clause or §V.F), `guideline_workspace_proposal.md` §V.B (Evidence Index) |
| CONV-018 | When a consultant commissions governed delegated execution to `LLM_Developer` or a designated agentic execution role, the commissioning MUST be mediated through an IMPLEMENTATION artifact (`task_specification` or `remediation_specification`) that the governing plan task explicitly references. Direct commissioning through plan steps alone is permitted only for trivial execution where the plan step itself provides sufficient specification depth (fewer than three target files and no cross-surface coordination). | The existing rules allow but do not require IMPLEMENTATION-mediated commissioning. Without this rule, governed execution could bypass the specification surface. | `guideline_workspace_implementation.md` §II, `workspace_documentation_rules.md` §6.A |
| CONV-019 | When a consultation-only gate is still deciding a convention or operational pattern, any pre-existing concrete implementation artifact for that scope MUST be reclassified as lineage-only in the gate package Evidence Index. The `standards_input` proposal MUST be the active pre-implementation authority surface. Authors MUST NOT treat the premature concrete artifact as active gate evidence. This elevates existing CONV-014 from SHOULD to MUST. | The AC004 case required explicit quarantine and reclassification of a pre-existing draft `SKILL.md`. The current SHOULD-level rule allowed ambiguity about whether the artifact was active or lineage-only. | `guideline_workspace_implementation.md` §VII.E, `guideline_workspace_proposal.md` §V.B and §V.D |
| CONV-020 | When same-gate QA or package-coherence defects are discovered after the gate package is assembled, the correction MUST be tracked through three surfaces: (a) plan task register (new sub-task or task status update), (b) session notes (correction session recorded per `guideline_workspace_notes.md`), and (c) gate-disposition proposal (evidence index refreshed to separate current from historical evidence). Silent amendment of live artifacts without cross-surface tracking is a governance violation. | The AC004 case required three correction sessions (SES005-SES007) with multiple plan amendments. Each was tracked ad hoc. A formal cross-surface tracking requirement prevents silent corrections. | `guideline_workspace_plan.md` §VI (new clause), `guideline_workspace_notes.md` (same-gate session rule), `guideline_workspace_proposal.md` §V.B |
| CONV-021 | When a gate package defines both a consultant-only operational surface and a broader multi-role operational protocol, the gate-disposition proposal MUST explicitly state which scope each surface serves, using the labels **consultant-scoped** and **program-scoped**. The consultant-scoped surface MUST NOT be presented as if it governs all roles; the program-scoped protocol MUST NOT be restricted to consultant use only. | The AC004 case resolved the distinction between the reminder surface (consultant-only) and `status_program.md` Section 7 (broader role-based protocol) through session discussion rather than by rule. | `workspace_documentation_rules.md` §7.A (new clause or amendment) |

### B. Compatibility Notes

- **CONV-015** extends CONV-012 rather than replacing it. Existing SPEC items authored before this convention are not retroactively invalidated, but new SPEC items authored after approval MUST meet the minimum-detail floor.
- **CONV-016** adds a new assessment checkpoint to the external-review profile. Existing external reviews are not retroactively re-assessed, but future external reviews for gate packages containing IMPLEMENTATION artifacts MUST include the per-SPEC check.
- **CONV-017** applies to new gate packages only. Existing gate packages that have already passed are not affected.
- **CONV-018** introduces a threshold test ("fewer than three target files and no cross-surface coordination") for the trivial-execution exception. This threshold is proposed as a starting point; the client may adjust it.
- **CONV-019** elevates CONV-014 from SHOULD to MUST. Existing premature artifacts are not retroactively deleted; they are reclassified as lineage-only.
- **CONV-020** does not retroactively require tracking for past same-gate corrections. It applies to corrections discovered after approval.
- **CONV-021** does not rename existing operational surfaces. It requires explicit scope labeling when both consultant-scoped and program-scoped surfaces coexist in the same gate package.
- **AC003 vertical-integration evidence (GAP-008)**: AC003's analysis-based implementation-spec pattern is acknowledged as a pre-IMPLEMENTATION-family artifact. It is not retroactively migrated by this proposal. The governance hardening ensures that future activities use IMPLEMENTATION `task_specification` as the canonical execution-specification surface. AC003's existing GATE-001 disposition (pending client decision) is not affected.

---

## IV. DECISION REQUESTS

| Decision ID | Prompt | Options | Recommendation | Owner |
|:--|:--|:--|:--|:--|
| DEC-001 | Should the minimum-detail floor (CONV-015) be enforced as a MUST for all new SPEC items after approval? | (a) MUST — all new SPECs must meet the four-element floor; (b) SHOULD — enforcement is advisory only; (c) MUST with a waiver mechanism for urgent patches | (a) — the AC004 failure demonstrated that advisory rules are insufficient for execution-quality control | Client |
| DEC-002 | Should per-SPEC commissionability assessment (CONV-016) be required for all external reviews covering gate packages with IMPLEMENTATION artifacts? | (a) Yes — mandatory for all such reviews; (b) Yes — mandatory but only for implementation-backed gates, not consultation-only; (c) No — advisory only | (a) — both gate types can surface IMPLEMENTATION artifacts, and per-SPEC commissionability is relevant whenever execution is downstream | Client |
| DEC-003 | Should exactly one authoritative external review be required per gate package (CONV-017)? | (a) Yes — mandatory single designation; (b) Yes — mandatory but only when more than one review-like analysis exists; (c) No — current ad hoc resolution is sufficient | (b) — the requirement is triggered by the multi-review condition; single-review packages need no designation | Client |
| DEC-004 | Should governed delegated execution require IMPLEMENTATION-mediated commissioning (CONV-018)? | (a) Yes — MUST for all governed delegation; (b) Yes — MUST with a trivial-execution exception; (c) No — current allowance-based rule is sufficient | (b) — the trivial-execution exception prevents over-governance for simple tasks while ensuring complex execution flows through the specification surface | Client |
| DEC-005 | Should CONV-014 be elevated from SHOULD to MUST (CONV-019)? | (a) Yes — MUST with lineage-only reclassification; (b) No — keep as SHOULD | (a) — the AC004 case demonstrated that SHOULD-level enforcement allowed premature artifacts to persist as ambiguously active | Client |
| DEC-006 | Should same-gate QA correction tracking be required across plan / notes / proposal surfaces (CONV-020)? | (a) Yes — MUST with three-surface tracking; (b) Yes — MUST but only plan and proposal (notes optional); (c) No — current ad hoc tracking is sufficient | (a) — all three surfaces must stay synchronized; omitting notes creates an invisible correction history | Client |
| DEC-007 | Should consultant-scoped versus program-scoped distinction be required in gate packages (CONV-021)? | (a) Yes — explicit scope labeling required; (b) No — current practice is sufficient | (a) — explicit labeling prevents operational scope confusion and reduces the risk of misapplying consultant-only surfaces to broader roles | Client |

---

## V. IMPACT AND RISKS

### A. Impact Assessment

- **Positive outcomes**:
  - SPEC items will have an enforceable quality floor, preventing under-specified execution commissions
  - External reviews will catch vague SPECs before gate approval rather than after
  - Gate packages will have clear authority ordering when multiple reviews exist
  - Governed delegated execution will always flow through a traceable specification surface
  - Premature concrete artifacts will be explicitly quarantined rather than ambiguously active
  - Same-gate corrections will be visible across all governance surfaces
  - Consultant-scoped versus program-scoped operational surfaces will be unambiguous

- **Tradeoffs**:
  - Additional authoring overhead for SPEC items (four required elements per SPEC)
  - Additional review scope for external reviews covering IMPLEMENTATION artifacts
  - Additional bookkeeping for same-gate corrections (three-surface tracking)
  - The trivial-execution threshold (CONV-018) introduces a judgment call that may need calibration

### B. Risks

| Risk ID | Description | Severity | Mitigation |
|:--|:--|:--|:--|
| RISK-001 | CONV-015 minimum-detail floor increases SPEC authoring time | Low | The four required elements (target files, end-state, validation, non-targets) are already present in well-authored SPECs; the rule formalizes existing best practice |
| RISK-002 | CONV-016 per-SPEC commissionability check increases external-review scope | Medium | The check is bounded to SPEC items in the gate package's IMPLEMENTATION artifact; it does not require reviewing the full codebase |
| RISK-003 | CONV-018 trivial-execution threshold may be too permissive or too restrictive | Low | The proposed threshold (fewer than three target files, no cross-surface coordination) can be adjusted after the first implementation cycle |
| RISK-004 | CONV-020 three-surface tracking increases same-gate correction overhead | Low | Same-gate corrections are inherently high-stakes and deserve explicit tracking; the overhead prevents more costly downstream discovery of silent amendments |

---

## VI. REFERENCES

| Document | Path |
|:--|:--|
| Governing Plan | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/plan_T104-PH001-ST008-AC006.md` |
| Supporting Analysis (TK001) | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/analysis/analysis_T104-PH001-ST008-AC006_implementation-governance-gap-analysis.md` |
| TK000 Readiness Assessment | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/analysis/analysis_T104-PH001-ST008-AC006-TK000_initial-readiness-and-downstream-assessment.md` |
| AC004 QA Assessment External Review | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/analysis/analysis_P-PH000-ST002-AC004_external-review_gate-002-package-qa-assessment.md` |
| AC004 Corrected External Review | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/analysis/analysis_P-PH000-ST002-AC004-GATE-002_external-review.md` |
| AC004 Implementation Spec | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/implementation/implementation_P-PH000-ST002-AC004_successor-first-operationalization-task-specification.md` |
| AC003 Plan | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC003/plan_T104-PH001-ST008-AC003.md` |
| Implementation Guideline | `prompt/templates/consultant/workspace/guideline_workspace_implementation.md` |
| Analysis Guideline | `prompt/templates/consultant/workspace/guideline_workspace_analysis.md` |
| Plan Guideline | `prompt/templates/consultant/workspace/guideline_workspace_plan.md` |
| Proposal Guideline | `prompt/templates/consultant/workspace/guideline_workspace_proposal.md` |
| Workspace Documentation Rules | `prompt/templates/consultant/workspace/workspace_documentation_rules.md` |

---

## VII. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-03-27 | Initial | Standards-input proposal authored for AC006-TK002. Seven conventions (CONV-015 through CONV-021) proposed across seven governance target files. Seven decision requests for client disposition. AC003 acknowledged as vertical-integration evidence. All conventions are pre-implementation governance rules to be approved at GATE-001 before downstream TK004 execution. |
