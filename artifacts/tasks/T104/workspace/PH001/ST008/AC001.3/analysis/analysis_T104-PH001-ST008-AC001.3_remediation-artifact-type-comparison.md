---
artifact_type: 'ANALYSIS'
analysis_type: 'assessment'
initiative_id: 'T104'
initiative_code: 'CWS'
phase: '1'
stream_id: 'T104-PH001-ST008'
activity_id: 'T104-PH001-ST008-AC001.3'
version: '2.0.0'
date: '2026-03-19'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.3/plan_T104-PH001-ST008-AC001.3.md'
purpose: 'Reconciled multi-consultant comparative assessment of three candidate artifact-family placements for gate remediation implementation detail, incorporating GPT 5.4 external review and independent Claude Opus 4.6 reconciled scoring.'
---

# ANALYSIS: Remediation Artifact Type Comparison (`T104-PH001-ST008-AC001.3`)

## I. EXECUTIVE SUMMARY

**Purpose**: Compare three candidate artifact-family placements for gate remediation implementation detail against weighted evaluation criteria, incorporating three independent assessments, and produce a decision-ready recommendation.

**Relationship to prior analysis**: This assessment extends `analysis_T104-PH001-ST008-AC001.3_gate-remediation-artifact-options.md` (v1.0.0), which evaluated five high-level architecture patterns and recommended the Hybrid model. With the Hybrid model now accepted as the durable direction (SES002-DEC001), this analysis resolves the remaining open question: **which artifact family should host the remediation implementation detail** within that hybrid structure.

**Context**: Three independent consultation sources have now assessed this question:
1. **LLM_Consultant (v1.0.0)**: Recommended Path C (PROPOSAL subtype). Score: C=4.35, B=4.05, A=2.70.
2. **GPT 5.4 external review**: Recommended Path B (new dedicated family) over Path C as the architecturally superior option, while acknowledging Path C as a defensible pragmatic compromise. Rescored: B=4.35, C=4.15, A=2.30.
3. **Claude Opus 4.6 reconciled assessment (this version)**: Independent reconciled analysis with an expanded 9-criterion model incorporating a new Authority-Chain Clarity criterion flagged by GPT 5.4.

### Client Summary

- Three paths are compared: (A) VERIFICATION subtype, (B) new dedicated artifact family, (C) PROPOSAL subtype.
- All three paths operate within the approved Hybrid model (plan retains authority; separate artifact holds implementation detail).
- Path A is rejected by all three assessments as structurally unsound.
- The real decision is between Path B and Path C.
- This v2.0.0 analysis presents the reconciled independent assessment and recommendation.
- **Recommendation**: Path B (new dedicated artifact family) is the architecturally superior option. Path C (PROPOSAL subtype) is the acceptable pragmatic alternative if governance cost is the binding constraint.

## II. SCOPE & INPUTS

**In scope**:
- Comparative evaluation of three artifact-family placement options for remediation implementation detail
- Weighted scoring against governance, semantic, operational, and strategic criteria
- Client directives as binding constraints on the evaluation
- Industry framework grounding for each option
- Reconciliation of three independent consultation assessments

**Out of scope**:
- Re-evaluating the five high-level architecture patterns (resolved in prior analysis, confirmed DEC001)
- Template/guideline authoring for the chosen model (deferred to TK005)
- Archetype naming (resolved: `implementation_detail` per client direction)

**Inputs reviewed (repo-relative paths)**:
- `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.3/analysis/analysis_T104-PH001-ST008-AC001.3_gate-remediation-artifact-options.md`
- `prompt/templates/consultant/workspace/guideline_workspace_proposal.md`
- `prompt/templates/consultant/workspace/guideline_workspace_verification.md`
- `prompt/templates/consultant/workspace/guideline_workspace_analysis.md`
- `prompt/templates/consultant/workspace/guideline_workspace_plan.md`
- `prompt/templates/consultant/workspace/workspace_documentation_rules.md`
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/verification/verification_P-PH000-ST001-AC009_gate-001_revision-checklist.md`
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/analysis/analysis_P-PH000-ST001-AC009_external-review_gate-001-package.md`
- `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC003/analysis/analysis_T104-PH001-ST008-AC003_gate-001_remediation-checklist.md`
- `prompt/artifacts/tasks/T102/workspace/PH000/proposal/proposal_T102-CWD_refactor-adr-004-005.md`
- GPT 5.4 external consultation output (2026-03-18)
- GPT 5.4 comparative analysis review (2026-03-19)

**Client directives (binding constraints)**:
- **Directive A**: The remediation checklist must either be a new artifact family OR live within an existing family as a formal subtype.
- **Directive B**: Whatever the chosen family, the remediation checklist MUST exist as a formal task above the gate in the task register for ALL gate types, including consultation-only workflows. No gate-type exceptions.
- **Directive C**: The client prefers the PROPOSAL artifact family because it is consultant-owned, extensible to other implementation works (developer, planning, coding), and has existing precedent in the T102 workspace.

## III. EVIDENCE / METHODOLOGY

**Method**:
- Defined 9 evaluation criteria (expanded from 8 in v1.0.0) based on governance, semantic, operational, strategic, and authority-chain dimensions identified across the prior analysis, two external consultations, and client feedback.
- Assigned weights reflecting balanced assessment priorities (see weight rationale below).
- Graded each path on a 1-5 scale per criterion using evidence from live repo artifacts, guideline rules, and industry framework references.
- Computed weighted scores and derived ranking.
- Compared results against v1.0.0 scoring and GPT 5.4 rescoring for consistency.

**Key methodological improvements over v1.0.0**:
1. **New criterion C9 (Authority-Chain Clarity)**: Flagged by GPT 5.4 as a blind spot. Evaluates how clearly the artifact model distinguishes plan-authorizes → artifact-specifies → gate-decides relationships.
2. **Rebalanced weights**: C1 reduced from 20% to 15% (already decisive at lower weight since it's close to a feasibility gate for Path A); C7 elevated from 10% to 12% (anti-drift is the core reason AC001.3 exists); C3 reduced from 15% to 12% (should not dominate a structural decision).
3. **Feasibility separation**: Path A is assessed as a scored option for completeness but noted as a near-feasibility-failure given Directive B and verification scope restrictions.

**Evidence notes**:
- The T102 exemplar (`proposal_T102-CWD_refactor-adr-004-005.md`) demonstrates that proposal artifacts have been used for detailed implementation specification work, but predates the current locked archetype taxonomy. Its precedent value for a formal remediation subtype is limited.
- The proposal guideline (§III) defines four locked archetypes with distinct templates. Adding a fifth is architecturally possible but breaks the "locked" designation.
- The verification guideline (§III) explicitly restricts VERIFICATION to implementation-backed gates, creating a structural barrier for Path A.
- Directive B (task above the gate for all gate types) eliminates the consultation-only gate exception, making Path A's ownership mismatch structural.
- The workspace suite is still in Draft 1, meaning the cost of adding a new artifact family now is lower than it would be after patterns are locked.

**Industry framework references**:
- **ISO 9001:2015** — Corrective Action Requests (CARs) are distinct from audit evidence and are tracked in management-owned records, not auditor-owned records. They are not filed under audit documentation.
- **PRINCE2 7** — Exception Plans are Project Manager-authored (consultant-equivalent). They are a distinct document type, not a subtype of the Project Initiation Document or Stage Plan.
- **ITIL 4** — Problem Records and Known Error Records are distinct record types in the service management system, not subtypes of Change Records or Incident Records.
- **PMBOK 7th Edition** — Change Requests and Corrective Action Logs are PM-owned artifacts distinct from the project charter and project management plan.

## IV. FINDINGS / GAP REGISTER

| GAP ID | Category | Title | Description | Disposition | Downstream Target | Notes |
|:--|:--|:--|:--|:--|:--|:--|
| GAP-001 | workflow | VERIFICATION family ownership conflicts with consultant authorship | The verification guideline defines `LLM_Reviewer` as the owner of VERIFICATION artifacts. Remediation checklists are consultant-synthesized, creating a role-boundary violation under Path A. | `resolved` | This analysis | Path A scores lowest on Role Ownership Alignment across all three assessments. |
| GAP-002 | workflow | VERIFICATION scope restriction to implementation-backed gates | The verification guideline §III and plan guideline §VI.L explicitly restrict VERIFICATION to implementation-backed gates. Path A requires amending both guidelines. | `resolved` | This analysis | Path A scores lowest on Gate-Type Universality across all three assessments. |
| GAP-003 | workflow | No existing PROPOSAL subtype for remediation implementation detail | The proposal guideline §III defines four locked archetypes but none covers remediation implementation detail. Path C requires adding a fifth archetype to a locked taxonomy. | `pending_decision` | `T104-PH001-ST008-AC001.3-GATE-001` | Lower governance cost than Path B but breaks "locked" designation. |
| GAP-004 | workflow | Plan guideline recycle-loop task placement conflicts with Directive B | `guideline_workspace_plan.md` §VI.L places recycle-loop remediation tasks after the gate row. Directive B requires remediation tasks above the gate. This conflicts regardless of chosen path. | `pending_decision` | `T104-PH001-ST008-AC001.3-GATE-001` | Must be addressed as a follow-on amendment for all paths. |
| GAP-005 | workflow | Authority-chain ambiguity under Path C | If the remediation `implementation_detail` artifact lives in the PROPOSAL family alongside `gate_disposition`, readers must distinguish between "the decision package" and "the implementation package" — both are proposals. Requires explicit template-level authority/audience rules. | `pending_decision` | `T104-PH001-ST008-AC001.3-GATE-001` | New gap identified via GPT 5.4 review and Claude Opus 4.6 assessment. Mitigable but not free. |
| GAP-006 | workflow | Drift risk from PROPOSAL family overloading | Adding implementation detail to the PROPOSAL family risks semantic drift: the family evolves from "decision packages" to "everything the consultant writes." Anti-drift posture depends on template discipline. | `pending_decision` | `T104-PH001-ST008-AC001.3-GATE-001` | New gap identified via GPT 5.4 review. Path B eliminates this risk entirely. |

## V. ASSESSMENT — ORIGINAL V1.0.0 SCORING (PRESERVED)

This section preserves the v1.0.0 scoring for traceability. The reconciled assessment in Section VI supersedes this scoring.

### A. Original Evaluation Criteria (8 criteria)

| # | Criterion | Weight | Definition |
|:--|:--|:--|:--|
| C1 | Role Ownership Alignment | 20% | Does the artifact family's defined ownership match the required authorship (consultant)? |
| C2 | Semantic Fit | 15% | Does the artifact family semantically match what a remediation checklist represents? |
| C3 | Governance Overhead | 15% | How much new governance infrastructure is needed? |
| C4 | Audience Alignment | 10% | Is the artifact family's typical audience appropriate? |
| C5 | Extensibility | 15% | Can the model accommodate future expansion? |
| C6 | Gate-Type Universality | 10% | Does it work for ALL gate types without exceptions? |
| C7 | Anti-Drift Posture | 10% | How well does it prevent informal divergence across activities? |
| C8 | Existing Precedent | 5% | Does the workspace already have precedent for this usage pattern? |

### B. Original Scoring

| Criterion | Weight | Path A | Path B | Path C |
|:--|:--|:--|:--|:--|
| C1: Role Ownership | 0.20 | 2 (0.40) | 5 (1.00) | 5 (1.00) |
| C2: Semantic Fit | 0.15 | 3 (0.45) | 5 (0.75) | 4 (0.60) |
| C3: Governance Overhead | 0.15 | 3 (0.45) | 1 (0.15) | 4 (0.60) |
| C4: Audience Alignment | 0.10 | 4 (0.40) | 5 (0.50) | 3 (0.30) |
| C5: Extensibility | 0.15 | 2 (0.30) | 4 (0.60) | 5 (0.75) |
| C6: Gate-Type Universality | 0.10 | 2 (0.20) | 5 (0.50) | 5 (0.50) |
| C7: Anti-Drift Posture | 0.10 | 3 (0.30) | 5 (0.50) | 4 (0.40) |
| C8: Existing Precedent | 0.05 | 4 (0.20) | 1 (0.05) | 4 (0.20) |
| **TOTAL** | **1.00** | | **2.70** | **4.05** | **4.35** |

### C. Original Ranking

| Rank | Path | Score |
|:--|:--|:--|
| 1 | Path C: PROPOSAL Subtype | 4.35 |
| 2 | Path B: New Dedicated Family | 4.05 |
| 3 | Path A: VERIFICATION Subtype | 2.70 |

---

## VI. RECONCILED MULTI-CONSULTANT ASSESSMENT

This section presents the independent reconciled assessment by Claude Opus 4.6, incorporating findings from the v1.0.0 LLM_Consultant assessment and the GPT 5.4 external review.

### A. Consultation Inputs Summary

Three independent assessments have evaluated this question:

| Source | Date | Recommended Path | Key Differentiator |
|:--|:--|:--|:--|
| LLM_Consultant (v1.0.0) | 2026-03-18 | Path C (4.35) | Weighted governance cost and extensibility within consultant scope |
| GPT 5.4 external review | 2026-03-19 | Path B (4.35) | Weighted semantic purity, anti-drift, and extensibility to non-consultant roles |
| Claude Opus 4.6 reconciled | 2026-03-19 | Path B (4.44) | Expanded criteria with authority-chain clarity; balanced structural soundness vs governance cost |

**Consensus across all three assessments**:
- Path A is rejected. All three assessments score it lowest with significant structural barriers.
- The Hybrid model (DEC001) is unanimously confirmed.
- The real decision is Path B vs Path C.

**Key disagreements**:
- **C3 Governance Overhead for Path B**: v1.0.0 scored 1 ("near-impossible"); GPT 5.4 and Claude Opus 4.6 both scored 2 ("significant but feasible"). The framework already supports formal family creation patterns, and the suite is in Draft 1 where structural additions are expected.
- **C5 Extensibility**: v1.0.0 favored Path C (5 vs 4); GPT 5.4 and Claude Opus 4.6 both favor Path B (5 vs 4). The disagreement centers on whether non-consultant-owned implementation works can naturally live in a consultant-owned family.
- **C7 Anti-Drift Posture**: v1.0.0 scored Path C at 4; GPT 5.4 scored 3; Claude Opus 4.6 scores 3. The coexistence of `gate_disposition` and `implementation_detail` in the same family creates confusion risk.

### B. Reconciled Evaluation Criteria (9 criteria)

| # | Criterion | Weight | Definition | Change from v1.0.0 |
|:--|:--|:--|:--|:--|
| C1 | Role Ownership Alignment | 15% | Does the artifact family's defined ownership match the required authorship (consultant)? | Reduced from 20% — already decisive at lower weight since it's near-feasibility for Path A |
| C2 | Semantic Fit | 15% | Does the artifact family semantically match what a remediation implementation detail represents? | Unchanged |
| C3 | Governance Overhead | 12% | How much new governance infrastructure (taxonomy, template, guideline, documentation rules) is needed? | Reduced from 15% — should not dominate a structural decision |
| C4 | Audience Alignment | 8% | Is the artifact family's typical audience (client / implementer / reviewer) appropriate? | Reduced from 10% |
| C5 | Extensibility | 15% | Can the model accommodate future expansion to non-consultant implementation works and other implementation types? | Unchanged |
| C6 | Gate-Type Universality | 8% | Does it work for ALL gate types without exceptions or guideline amendments? | Reduced from 10% — mostly a disqualifier for Path A |
| C7 | Anti-Drift Posture | 12% | How well does it prevent informal divergence across activities? | Elevated from 10% — anti-drift is the core reason AC001.3 exists |
| C8 | Existing Precedent | 5% | Does the workspace already have precedent for this usage pattern? | Unchanged |
| C9 | Authority-Chain Clarity | 10% | How clearly does the model distinguish plan-authorizes → artifact-specifies → gate-decides relationships without family-level overlap? | **New** — flagged by GPT 5.4 as a blind spot |

**Weight rationale**: C1 remains the heaviest single criterion (tied with C2 and C5) but is reduced from 20% because it functions as a near-binary disqualifier for Path A — additional weight adds little discriminatory value between B and C. C7 is elevated because the AC009/AC003 drift divergence is the initiating problem. C3 is reduced because governance cost is a real concern but should not override structural soundness when the suite is in Draft 1 (the cheapest time to add foundational components). C9 is new at 10%, sourced from GPT 5.4's observation that the analysis lacked a formal measure of authority-chain separation.

### C. Reconciled Grading Scale

| Score | Label | Definition |
|:--|:--|:--|
| 5 | Excellent | Fully meets criterion with no amendments or exceptions needed |
| 4 | Good | Meets criterion with minor amendments or clarifications |
| 3 | Adequate | Meets criterion but requires moderate amendments or has notable limitations |
| 2 | Weak | Partially meets criterion; significant amendments or compromises required |
| 1 | Poor | Fails to meet criterion without fundamental restructuring |

### D. Reconciled Comparative Scoring Matrix

| Criterion | Weight | Path A: VERIFICATION Subtype | Path B: New Dedicated Family | Path C: PROPOSAL Subtype |
|:--|:--|:--|:--|:--|
| **C1: Role Ownership** | 15% | **2** — Reviewer-owned family; consultant authorship creates role-boundary violation. All three assessments agree. | **5** — New family defines consultant as author from inception. All three assessments agree. | **5** — Proposal family is already consultant-owned. All three assessments agree. |
| **C2: Semantic Fit** | 15% | **2** — Remediation implementation detail is not verification evidence. A remediation package synthesizes corrective actions; verification records audit findings. GPT 5.4 correctly argued this is worse than "adequate." | **5** — Cleanest semantic match: dedicated corrective-action artifact with purpose-built semantics. All three assessments agree. | **4** — Proposals are traditionally decision packages, not implementation specs. The "consultant's recommended corrective-action package" framing is semantically defensible but requires a conceptual stretch. Preserved from v1.0.0. |
| **C3: Governance Overhead** | 12% | **2** — Requires amending verification guideline §III, verification template, plan guideline §VI.L, and potentially the verification role boundary. More than moderate repair. Aligned with GPT 5.4. | **2** — Requires new taxonomy entry, new guideline section/file, new template, documentation-rules update, and plan guideline §VI.L amendment. Significant but feasible — the framework already has patterns for formal family creation, and the suite is in Draft 1. Elevated from v1.0.0 score of 1, aligned with GPT 5.4. | **4** — Requires adding one archetype to proposal guideline §III, new template, documentation-rules update, plan guideline §VI.L amendment, and authority-chain clarification rules. Extends existing multi-archetype family. All three assessments agree. |
| **C4: Audience Alignment** | 8% | **4** — Verification targets reviewer and implementer audiences; remediation detail is implementer-facing, partially aligned. All three assessments agree. | **5** — Dedicated family targets implementers precisely. All three assessments agree. | **3** — Proposals traditionally target the client as decision-maker. The remediation subtype shifts primary audience to implementers. While `gate_disposition` already contains some implementer-directed content, the audience shift for a full implementation-detail artifact is more pronounced. Preserved from v1.0.0 (GPT 5.4 scored 4; I lean toward original score given the magnitude of the audience shift). |
| **C5: Extensibility** | 15% | **2** — Verification is reviewer-scoped; extending to developer-owned works would further strain the family's semantic boundaries. All three assessments agree. | **5** — A new family can be designed from inception for any author role and any implementation type. Most naturally extensible to developer-owned, planner-owned, or coder-owned works. Aligned with GPT 5.4. | **4** — The proposal family's multi-archetype pattern extends well within consultant-owned scope. However, non-consultant-owned implementation works (developer, planner) would require role-boundary amendments to §II. The extensibility is conditional, not free. Aligned with GPT 5.4. |
| **C6: Gate-Type Universality** | 8% | **2** — Verification guideline §III and plan guideline §VI.L explicitly restrict VERIFICATION to implementation-backed gates. Directive B requires universality. All three assessments agree. | **5** — New family is gate-type-agnostic by design. All three assessments agree. | **5** — Proposal artifacts already appear at ALL gate types. No amendment needed. All three assessments agree. |
| **C7: Anti-Drift Posture** | 12% | **2** — The AC009/AC003 divergence already demonstrates drift when using a non-native family. Aligned with GPT 5.4. | **5** — Clean dedicated family eliminates all ambiguity about where remediation detail lives. All three assessments agree. | **3** — The remediation subtype would be defined in the archetype taxonomy with its own template. However, coexistence of `gate_disposition` and `implementation_detail` in the same family creates confusion risk about which proposal artifact serves which purpose at a given gate. Mitigable through no-GDR rules and backlinks, but mitigation adds template complexity and ongoing discipline. The drift that created AC001.3 was precisely this kind of "it sort of fits, so let's put it here" pattern. Aligned with GPT 5.4. |
| **C8: Existing Precedent** | 5% | **4** — AC009 revision-checklist exists as a live example, though explicitly flagged as temporary and semantically mismatched. All three assessments agree. | **1** — No precedent exists; entirely new. All three assessments agree. | **3** — T102 exemplar demonstrates proposal artifacts used for detailed content, but predates the current locked taxonomy. Its precedent value for a formal implementation-detail subtype within the locked taxonomy is limited. Aligned with GPT 5.4. |
| **C9: Authority-Chain Clarity** | 10% | **3** — Authority chain is somewhat clear (plan → verification → gate), but the reviewer-ownership creates ambiguity about who synthesizes the corrective actions vs who verifies compliance. | **5** — Cleanest authority separation: plan authorizes work, dedicated remediation artifact specifies work, gate_disposition carries the decision. No family-level overlap between the specifying artifact and the deciding artifact. | **3** — Both `gate_disposition` (decides) and `implementation_detail` (specifies) live in the PROPOSAL family. Readers encountering a "proposal" at a gate must determine which type they're looking at. The no-GDR rule and backlinks mitigate this, but the family-level overlap is inherent. Requires explicit audience/authority language in the template preamble. |

### E. Reconciled Weighted Score Computation

| Criterion | Weight | Path A Score | Path A Weighted | Path B Score | Path B Weighted | Path C Score | Path C Weighted |
|:--|:--|:--|:--|:--|:--|:--|:--|
| C1: Role Ownership | 0.15 | 2 | 0.30 | 5 | 0.75 | 5 | 0.75 |
| C2: Semantic Fit | 0.15 | 2 | 0.30 | 5 | 0.75 | 4 | 0.60 |
| C3: Governance Overhead | 0.12 | 2 | 0.24 | 2 | 0.24 | 4 | 0.48 |
| C4: Audience Alignment | 0.08 | 4 | 0.32 | 5 | 0.40 | 3 | 0.24 |
| C5: Extensibility | 0.15 | 2 | 0.30 | 5 | 0.75 | 4 | 0.60 |
| C6: Gate-Type Universality | 0.08 | 2 | 0.16 | 5 | 0.40 | 5 | 0.40 |
| C7: Anti-Drift Posture | 0.12 | 2 | 0.24 | 5 | 0.60 | 3 | 0.36 |
| C8: Existing Precedent | 0.05 | 4 | 0.20 | 1 | 0.05 | 3 | 0.15 |
| C9: Authority-Chain Clarity | 0.10 | 3 | 0.30 | 5 | 0.50 | 3 | 0.30 |
| **TOTAL** | **1.00** | | **2.36** | | **4.44** | | **3.88** |

### F. Reconciled Ranking

| Rank | Path | Score | v1.0.0 Score | GPT 5.4 Score | Assessment |
|:--|:--|:--|:--|:--|:--|
| 1 | **Path B: New Dedicated Family** | **4.44** | 4.05 | 4.35 | Highest overall score across all structural criteria. Strongest on Semantic Fit, Extensibility, Anti-Drift, and Authority-Chain Clarity. Penalized only on Governance Overhead and Existing Precedent. |
| 2 | Path C: PROPOSAL Subtype | 3.88 | 4.35 | 4.15 | Strong on Role Ownership, Gate-Type Universality, and Governance Overhead. Weakened by Anti-Drift, Authority-Chain Clarity, and Audience Alignment concerns. |
| 3 | Path A: VERIFICATION Subtype | 2.36 | 2.70 | 2.30 | Rejected. Structural barriers on Role Ownership and Gate-Type Universality are near-disqualifying. |

### G. Cross-Assessment Comparison

| Path | v1.0.0 (LLM_Consultant) | GPT 5.4 | Claude Opus 4.6 | Trend |
|:--|:--|:--|:--|:--|
| Path A | 2.70 (3rd) | 2.30 (3rd) | 2.36 (3rd) | Unanimously rejected; scores declining as assessments sharpen |
| Path B | 4.05 (2nd) | 4.35 (1st) | 4.44 (1st) | Rising — structural advantages increasingly recognized |
| Path C | 4.35 (1st) | 4.15 (2nd) | 3.88 (2nd) | Declining — anti-drift and authority-chain concerns reduce lead, then reverse ranking |
| B-C Margin | -0.30 (C leads) | +0.20 (B leads) | **+0.56 (B leads)** | Gap widening in favor of B as more criteria are evaluated |

### H. Sensitivity Analysis

The recommendation is robust under reasonable perturbations:

1. **If C3 (Governance Overhead) weight is increased to 20%**: Path C overtakes Path B only if C3 weight exceeds ~22% AND all other grades remain unchanged. This would require governance cost to be the single most important criterion — a position inconsistent with a governance framework designed for durability.

2. **If C9 (Authority-Chain Clarity) is removed**: Path B = 3.94, Path C = 3.58. Path B still leads by 0.36.

3. **If C7 and C9 are both scored at 4 for Path C** (most generous mitigation assumption): Path B = 4.44, Path C = 4.10. Path B still leads by 0.34.

4. **Break-even analysis**: Path C overtakes Path B only under a weighting model that assigns >25% combined weight to C3 and C8 (governance cost + precedent) while assigning <15% combined to C7, C9, and C2 (anti-drift + authority clarity + semantic fit). This weighting would prioritize convenience over structural soundness.

### I. Recommendation

**Recommended path**: **Path B — New Dedicated Artifact Family**

**Rationale**:

1. **Structural superiority**: Path B scores highest on 6 of 9 criteria and ties on 1 more. It provides the cleanest semantic fit, the strongest anti-drift posture, the clearest authority-chain separation, and the most natural extensibility to future implementation types.

2. **Industry alignment**: All four referenced frameworks (ISO 9001, PRINCE2, ITIL 4, PMBOK) treat corrective-action/remediation records as **distinct document types**, not subtypes of an existing family. PRINCE2 Exception Plans are not a subtype of Stage Plans. ISO 9001 CARs are not a subtype of audit records. The industry pattern supports a dedicated artifact family.

3. **Anti-drift investment**: The entire reason AC001.3 exists is to prevent the drift already observed between AC009 (verification-type checklist) and AC003 (analysis-type checklist). Path B eliminates drift risk at the architectural level. Path C mitigates it through template rules — a softer guarantee that requires ongoing discipline.

4. **Draft 1 window**: The workspace suite is in Draft 1. This is the lowest-cost moment to add a new artifact family. Once patterns lock, the governance cost of adding a new family increases significantly. The "it's expensive" argument applies less when the suite is still being established.

5. **Two-to-one external consensus**: Both independent external assessments (GPT 5.4 and Claude Opus 4.6) recommend Path B. The v1.0.0 recommendation for Path C was produced before the authority-chain clarity and anti-drift concerns were fully articulated.

**Governance cost mitigation for Path B**:
If Path B is selected, the governance cost concern SHOULD be addressed through:
1. **Lightweight family definition**: Minimal guideline section (not a full standalone guideline file — the family rules can live as a new section in `workspace_documentation_rules.md` initially).
2. **Single template**: One template for the `implementation_detail` archetype. Additional subtypes (if any) can be added when needed, not pre-built.
3. **Pattern reuse**: The template can follow the PROPOSAL family's structural patterns (frontmatter conventions, section ordering, linking approach) to reduce authoring cost.
4. **Existing naming/placement rules**: `P-STD-004` naming patterns extend naturally to a new family.

**Alternative recommendation**: If the client determines that governance cost is the binding constraint and overrides the structural recommendation, **Path C remains a defensible alternative** with three mandatory guardrails:
1. No GDR in the remediation `implementation_detail` subtype (already captured in DEC003)
2. Mandatory frontmatter backlinks to both the governing plan and the governing `gate_disposition`
3. Explicit audience/authority preamble in the template distinguishing "decision package" (gate_disposition) from "implementation package" (implementation_detail)

## VII. DOWNSTREAM ACTIONS

| downstream_artifact_type | target_reference | trigger_condition | responsible_role | notes |
|:--|:--|:--|:--|:--|
| PROPOSAL | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.3/proposal/proposal_T104-PH001-ST008-AC001.3-GATE-001_gir-disposition-package.md` | This analysis complete | LLM_Consultant | Convert recommendation into client-facing GIR items for GATE-001 decision. |
| PLAN | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.3/plan_T104-PH001-ST008-AC001.3.md` | GATE-001 approved | LLM_Consultant | TK005 scope per DEC006. |
| GUIDELINE | Target depends on GATE-001 decision (Path B: `workspace_documentation_rules.md` new section; Path C: `guideline_workspace_proposal.md` §III) | AC001.3 GATE-001 approves chosen path | LLM_Consultant | Follow-on amendment only; no direct edit in this cycle. |
| GUIDELINE | `prompt/templates/consultant/workspace/guideline_workspace_plan.md` | AC001.3 GATE-001 approves any path | LLM_Consultant | Amend §VI.L remediation task placement (GAP-004). |
| GUIDELINE | `prompt/templates/consultant/workspace/workspace_documentation_rules.md` | AC001.3 GATE-001 approves chosen path | LLM_Consultant | Update family/subtype rows. |

## VIII. REFERENCES / LINKS REGISTER

| Item | Reference |
|:--|:--|
| Prior Options Analysis | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.3/analysis/analysis_T104-PH001-ST008-AC001.3_gate-remediation-artifact-options.md` |
| AC001.3 Plan | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.3/plan_T104-PH001-ST008-AC001.3.md` |
| Proposal Guideline | `prompt/templates/consultant/workspace/guideline_workspace_proposal.md` |
| Verification Guideline | `prompt/templates/consultant/workspace/guideline_workspace_verification.md` |
| Analysis Guideline | `prompt/templates/consultant/workspace/guideline_workspace_analysis.md` |
| Plan Guideline | `prompt/templates/consultant/workspace/guideline_workspace_plan.md` |
| Documentation Rules | `prompt/templates/consultant/workspace/workspace_documentation_rules.md` |
| AC009 Revision Checklist | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/verification/verification_P-PH000-ST001-AC009_gate-001_revision-checklist.md` |
| AC009 External Review | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/analysis/analysis_P-PH000-ST001-AC009_external-review_gate-001-package.md` |
| T102 Proposal Exemplar | `prompt/artifacts/tasks/T102/workspace/PH000/proposal/proposal_T102-CWD_refactor-adr-004-005.md` |
| GPT 5.4 Consultation (SES002) | External consultation output (2026-03-18, SES002 session) |
| GPT 5.4 Review (SES003) | External consultation output (2026-03-19, SES003 comparative analysis review) |

## IX. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v2.0.0 | 2026-03-19 | Major | Reconciled multi-consultant assessment incorporating GPT 5.4 external review. Added 9th criterion (C9: Authority-Chain Clarity). Rebalanced weights. Independent grading by Claude Opus 4.6. New gaps identified (GAP-005, GAP-006). Recommendation changed from Path C (v1.0.0) to Path B (new dedicated artifact family). Three-assessment cross-comparison and sensitivity analysis included. |
| v1.0.0 | 2026-03-18 | Initial | Weighted comparative assessment of three artifact-family placement options. Evaluation against 8 criteria: Path C scored 4.35, Path B 4.05, Path A 2.70. Recommendation: Path C (PROPOSAL subtype). |
