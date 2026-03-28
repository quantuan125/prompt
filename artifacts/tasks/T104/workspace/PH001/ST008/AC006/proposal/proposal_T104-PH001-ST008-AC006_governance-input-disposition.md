---
artifact_type: 'PROPOSAL'
initiative_id: 'T104'
initiative_code: 'CWS'
phase: '1'
stream_id: 'T104-PH001-ST008'
activity_id: 'T104-PH001-ST008-AC006'
task_id: 'T104-PH001-ST008-AC006-TK002'
version: '2.1.0'
date: '2026-03-28'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/plan_T104-PH001-ST008-AC006.md'
analysis_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/analysis/analysis_T104-PH001-ST008-AC006_implementation-governance-gap-analysis.md'
target_standards:
  - 'guideline_workspace_implementation.md'
  - 'template_workspace_implementation_task-specification.md'
  - 'template_workspace_implementation_remediation-specification.md'
  - 'guideline_workspace_analysis.md'
  - 'guideline_workspace_plan.md'
  - 'guideline_workspace_proposal.md'
  - 'guideline_workspace_notes.md'
  - 'workspace_documentation_rules.md'
purpose: 'Package the governance direction for implementation-spec precision, commissioning rules, authoritative-review selection, standards-input enforcement, same-gate QA tracking, and role-protocol distinction for client disposition before downstream implementation begins.'
---

# PROPOSAL: Standards Input — IMPLEMENTATION Governance Hardening

## I. PURPOSE

- **Proposal objective**: Approve the governance direction for eleven identified gaps so downstream implementation (TK004) can apply the approved rule changes to the eight target governance files.
- **Input scope**: Pre-implementation governance rules only. This proposal defines the conventions that must govern how IMPLEMENTATION artifacts are authored, reviewed, commissioned, and tracked, and how the assistant subagent role is formalized. It does not implement the rules — that is TK004 scope after `GATE-001` approval. CONV-022 (implementation artifact discoverability) has been resolved with TK001.1 comparative analysis findings recommending Option B (naming convention).
- **Target standards**: `guideline_workspace_implementation.md`, `template_workspace_implementation_task-specification.md`, `template_workspace_implementation_remediation-specification.md`, `guideline_workspace_analysis.md`, `guideline_workspace_plan.md`, `guideline_workspace_proposal.md`, `guideline_workspace_notes.md`, `workspace_documentation_rules.md`

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
| GAP-009 | workflow | CONV-012 governs SPEC structure but not the Implementation Detail prose block. Model-specific authoring patterns fail on non-authoring models. | Cross-model execution failures; assistant or developer subagents cannot reliably parse Implementation Detail authored by a different LLM. |
| GAP-010 | consistency | `execution_audience` flag is in frontmatter only — developer-facing and assistant-facing specs are indistinguishable at filesystem level. | Developer-facing specs (mandatory in gate packages, multi-role reviewed) cannot be easily identified or prioritized among ~18 consultant-scoped artifacts. |
| GAP-011 | consistency | Assistant subagent operates under consultant authority without a named role in §6. | No defined boundary rules, execution evidence requirements, or scope distinction from LLM_Developer. |

---

## III. PROPOSED CONVENTIONS

### A. Convention Set

| Convention ID | Rule | Rationale | Authority Link |
|:--|:--|:--|:--|
| CONV-015 | Every execution-facing SPEC item MUST name at minimum: (a) exact target file(s)/surface(s), (b) required end-state posture, (c) validation checks, and (d) explicit non-target constraints. A SPEC item missing any of these four elements MUST be treated as draft-incomplete and MUST NOT be commissioned for execution. Additionally, when a SPEC item includes an `#### Implementation Detail` block, the detail MUST use a structured step format that is model-agnostic and independently parseable: each step MUST be numbered and self-contained; file mutations MUST use before/after code blocks with explicit file path and line/section locators; conditional logic MUST be expressed as explicit if/then rules, not embedded in prose. The Implementation Detail MUST be executable by any high-intelligence LLM model without requiring project-specific context beyond what is stated in the SPEC metadata table and the detail block itself. | The AC004 case showed that a SPEC with summary-level content passed external review unchallenged. A minimum-detail floor prevents under-specified SPECs from entering the execution pipeline. The cross-model authoring sub-rule ensures Implementation Detail is not authored in model-specific patterns that fail on non-authoring models. [Grounding: IEEE 29148 completeness/verifiability attributes; CMMI-DEV RD entry/exit criteria; PRINCE2 Work Package minimum content; AGENTIF benchmark — LLMs fail on dense multi-constraint specs; Claude Code context-amnesia — subagents start fresh, brief must be self-contained; Codex "single source of truth" — "Do not assume anything not written here"] | `guideline_workspace_implementation.md` §IV (amend CONV-012), `template_workspace_implementation_task-specification.md`, `template_workspace_implementation_remediation-specification.md` |
| CONV-016 | When an `external_review` analysis serves as a gate-readiness input and the gate package includes an IMPLEMENTATION artifact, the review MUST assess whether each execution-facing SPEC item meets the CONV-015 minimum-detail floor and is independently commissionable for the stated `execution_audience`. | The AC004 external review did not detect the vague implementation spec because per-SPEC commissionability was not a review requirement. [Grounding: Fagan Inspection — per-item checklist review; ISO/IEC 20246 — item-level examination; FDA 21 CFR 820.30(c) — per-design-input completeness; DO-178C §6.3 — per-requirement traceability; Claude Code PreToolUse hooks — per-action enforcement; CodeRabbit agentic validation — ~46% bug detection] | `guideline_workspace_analysis.md` §IV.B (`external_review` lifecycle) |
| CONV-017 | When a gate package contains multiple ANALYSIS artifacts of type `external_review`, the gate-disposition proposal MUST designate exactly one as the **authoritative external review** for that gate. Other review-like analyses are classified as supporting or historical evidence in the Evidence Index. | The AC004 package surfaced two external reviews without explicit authority ordering. The authoritative designation was resolved ad hoc in the QA assessment. [Grounding: ISO 9001 §7.5.3 — only approved current-revision documents in circulation; ISO 10007/IEEE 828 — configuration baseline as single reference; PRINCE2 CIR — status tracking; CrewAI hierarchical authority with `allowed_agents`] | `guideline_workspace_analysis.md` (new clause or §V.F), `guideline_workspace_proposal.md` §V.B (Evidence Index) |
| CONV-018 | When a consultant commissions governed delegated execution to `LLM_Developer`, `LLM_Assistant`, or a designated agentic execution role, the commissioning MUST be mediated through an IMPLEMENTATION artifact (`task_specification` or `remediation_specification`) that the governing plan task explicitly references. Commissioning MAY bypass IMPLEMENTATION mediation only when ALL three conditions are met: (a) change is confined to a single governance surface, (b) no downstream execution dependency exists, and (c) the delegating authority explicitly attests to low execution risk in the plan task's Action field. When the exception is claimed, the plan task's Action field MUST record the attestation (e.g., "Direct commission: single-surface, no dependency, low risk"). | The existing rules allow but do not require IMPLEMENTATION-mediated commissioning. Without this rule, governed execution could bypass the specification surface. The risk-based exception replaces the original count-based threshold ("fewer than three target files") with a three-condition test that scales governance formality with risk. [Grounding: PRINCE2 Work Package — formal authorization with mutual acceptance; ITIL SDP — formal handover; NIST AI RMF — proportional governance (formality scales with risk); AURA framework — risk-based scoring (0-30 auto-approve, 30-60 selective, 60+ escalate); Anthropic research — "too early to mandate specific interaction patterns"; Claude Code Agent tool — sole delegation channel; Codex+Agents SDK — PM-gated pipeline with file-based gating] | `guideline_workspace_implementation.md` §II, `workspace_documentation_rules.md` §6.A |
| CONV-019 | When a consultation-only gate is still deciding a convention or operational pattern, any pre-existing concrete implementation artifact for that scope MUST be reclassified as lineage-only in the gate package Evidence Index. The `standards_input` proposal MUST be the active pre-implementation authority surface. Authors MUST NOT treat the premature concrete artifact as active gate evidence. This elevates existing CONV-014 from SHOULD to MUST. | The AC004 case required explicit quarantine and reclassification of a pre-existing draft `SKILL.md`. The current SHOULD-level rule allowed ambiguity about whether the artifact was active or lineage-only. [Grounding: ISO 9001 §8.7 — nonconforming output segregation; CM baselines — unapproved = no authority; ITIL Release Mgmt — CAB as change authority boundary; Claude Code worktree isolation — draft contamination prevention] | `guideline_workspace_implementation.md` §VII.E, `guideline_workspace_proposal.md` §V.B and §V.D |
| CONV-020 | When same-gate QA or package-coherence defects are discovered after the gate package is assembled, the correction MUST be tracked through three surfaces: (a) plan task register (new sub-task or task status update), (b) session notes (correction session recorded per `guideline_workspace_notes.md`), and (c) gate-disposition proposal (evidence index refreshed to separate current from historical evidence). Silent amendment of live artifacts without cross-surface tracking is a governance violation. | The AC004 case required three correction sessions (SES005-SES007) with multiple plan amendments. Each was tracked ad hoc. A formal cross-surface tracking requirement prevents silent corrections. [Grounding: ISO 9001 §10.2 CAPA — documented nonconformity + actions + results; AS9100D §10.2 — most rigorous per-finding tracking; CMMI VER — defects tracked and analyzed; PRINCE2 Issue Register + Quality Register + CIR cross-referencing] | `guideline_workspace_plan.md` §VI (new clause), `guideline_workspace_notes.md` (same-gate session rule), `guideline_workspace_proposal.md` §V.B |
| CONV-021 | When a gate package defines both a consultant-only operational surface and a broader multi-role operational protocol, the gate-disposition proposal MUST explicitly state which scope each surface serves, using the labels **consultant-scoped** and **program-scoped**. The consultant-scoped surface MUST NOT be presented as if it governs all roles; the program-scoped protocol MUST NOT be restricted to consultant use only. | The AC004 case resolved the distinction between the reminder surface (consultant-only) and `status_program.md` Section 7 (broader role-based protocol) through session discussion rather than by rule. [Grounding: ISO 27001 Annex A 5.12/5.13 — classification + metadata-based labeling; RACI — exactly one Accountable per row; PRINCE2 Communication Management Approach — audience mapping; Claude Code tool allowlists/denylists per subagent role] | `workspace_documentation_rules.md` §7.A (new clause or amendment) |
| CONV-022 | The architectural distinction between developer-facing implementation specifications and assistant-facing implementation specifications MUST be resolved through a **naming convention** (Option B per TK001.1 comparative analysis, weighted score 83/100): developer-facing task specifications retain the existing `-task-specification` filename suffix; consultant/assistant-facing orchestration briefs MUST use a `-brief` filename suffix (e.g., `implementation_<scope-UID>_<topic>-brief.md`). Remediation specifications retain the existing `-remediation-specification` suffix and remain restricted to gate RECYCLE verdicts. The `remediation_specification` subtype scope is NOT expanded; pre-gate assistant corrections are governed through `task_specification` with appropriate `execution_audience` and the `-brief` naming convention. | TK001.1 evaluated four options against six weighted criteria (discoverability, governance cost, backward compatibility, template impact, LLM_Assistant alignment, remediation scope clarity). Option B scored 83/100 — highest overall. The naming convention resolves filesystem-level discoverability without new templates or subtype taxonomy changes. Structural identity finding (all implementation artifacts share identical SPEC structure regardless of audience) confirms the distinction is operational context, not document type — a naming convention correctly reflects this. [Grounding: ISO 9001 §7.5.3 — distinct document types distinguishable by identification scheme; PRINCE2 CIR — each product variant has distinct CI type; Claude Code role archetypes — structurally distinct agents; ISO 9001 §10.2 CAPA — corrections vs. corrective actions maps to remediation_specification vs. assistant pre-gate fixes] | `guideline_workspace_implementation.md` §IV (naming convention rule), `workspace_documentation_rules.md` §3 (filename pattern note). Analysis: `analysis_T104-PH001-ST008-AC006-TK001.1_implementation-artifact-architecture-assessment.md` |
| CONV-023 | The assistant subagent MUST be recognized as a named role (`LLM_Assistant`) in `workspace_documentation_rules.md` §6 with explicit boundary rules: (a) operates under LLM_Consultant authority with no independent decision-making; (b) does not produce DEV-REPORTs — execution evidence is captured in session notes or plan changelog; (c) consumes implementation artifacts with `execution_audience: 'consultant'` or `execution_audience: 'assistant'` (final audience label pending TK001.1); (d) is not part of the implementation-backed gate workflow — no VERIFICATION stage for assistant work; (e) is distinct from LLM_Developer, which owns `guideline_workspace_dev-report.md` and participates in the larger development workflow toward implementation-backed gates. The Role-to-Artifact Ownership Matrix (§8) MUST be updated to include `LLM_Assistant`. | The assistant subagent is not a named role in §6; it operates as an unnamed extension of LLM_Consultant. Unlike LLM_Developer, the assistant has no defined boundary rules, no execution evidence requirements, and no explicit scope distinction. [Grounding: Claude Code built-in role archetypes with distinct tool restrictions per subagent; CrewAI named role definitions (Manager, Worker, Researcher) with explicit delegation rules; Microsoft guidance — "roles have distinct tool access and explicit handoff artifacts so that disagreements can be resolved via evidence"] | `workspace_documentation_rules.md` §6 (new §6.F), §8 (ownership matrix update) |

### B. Compatibility Notes

- **CONV-015** extends CONV-012 rather than replacing it. Existing SPEC items authored before this convention are not retroactively invalidated, but new SPEC items authored after approval MUST meet the minimum-detail floor.
- **CONV-016** adds a new assessment checkpoint to the external-review profile. Existing external reviews are not retroactively re-assessed, but future external reviews for gate packages containing IMPLEMENTATION artifacts MUST include the per-SPEC check.
- **CONV-017** applies to new gate packages only. Existing gate packages that have already passed are not affected.
- **CONV-018** introduces a risk-based three-condition exception model (single surface, no downstream dependency, explicit low-risk attestation) for the trivial-execution exception. This model ensures governance formality scales with risk (aligned with NIST AI RMF and AURA framework).
- **CONV-019** elevates CONV-014 from SHOULD to MUST. Existing premature artifacts are not retroactively deleted; they are reclassified as lineage-only.
- **CONV-020** does not retroactively require tracking for past same-gate corrections. It applies to corrections discovered after approval.
- **CONV-021** does not rename existing operational surfaces. It requires explicit scope labeling when both consultant-scoped and program-scoped surfaces coexist in the same gate package.
- **AC003 vertical-integration evidence (GAP-008)**: AC003's analysis-based implementation-spec pattern is acknowledged as a pre-IMPLEMENTATION-family artifact. It is not retroactively migrated by this proposal. The governance hardening ensures that future activities use IMPLEMENTATION `task_specification` as the canonical execution-specification surface. AC003's existing GATE-001 disposition (pending client decision) is not affected.
- **CONV-022** prescribes Option B (naming convention) per TK001.1 comparative analysis: developer-facing specs retain `-task-specification` suffix; consultant/assistant-facing specs use `-brief` suffix. Existing implementation artifacts are not retroactively renamed; the naming convention applies to new artifacts authored after approval. No new templates or subtypes are introduced. The `remediation_specification` subtype scope remains restricted to gate RECYCLE verdicts; pre-gate assistant corrections are governed through the naming convention + `execution_audience` flag.
- **CONV-023** introduces `LLM_Assistant` as a new named role. Existing artifacts authored with `execution_audience: 'consultant'` are not retroactively relabeled. The role boundary rules apply to new assistant-executed work after approval. The relationship between `LLM_Assistant` and `LLM_Developer` is explicitly non-overlapping: `LLM_Developer` owns DEV-REPORTs and participates in implementation-backed gate workflows; `LLM_Assistant` operates under consultant authority with session-note-level execution evidence only.

### C. Enforcement Modalities

Each convention above can be enforced through two complementary channels. TK004 implementation SHOULD design for both:

| Channel | Mechanism | Applicable Conventions | Notes |
|:--|:--|:--|:--|
| **Human-mediated** | Review checklists, gate-package inspection, external-review scope requirements, consultant/reviewer judgment | All (CONV-015 through CONV-023) | Aligns with traditional standards: Fagan Inspection checklists, ISO 20246 review types, PRINCE2 Work Package acceptance, ISO 9001 CAPA documentation |
| **Deterministic / agentic** | Hooks (PreToolUse approve/deny), sandboxes (workspace-write isolation), tool restrictions (per-subagent allowlists/denylists), frontmatter validation (schema checks), worktree isolation (draft contamination prevention) | CONV-015 (metadata field validation), CONV-018 (attestation field in plan Action column), CONV-019 (frontmatter status check), CONV-022 (naming convention enforcement), CONV-023 (role-identity injection via AGENTS.md) | Aligns with agentic patterns: Claude Code hooks (21 lifecycle events, 4 handler types), Codex sandboxing (read-only/workspace-write/danger modes), CodeRabbit agentic validation |

Not all conventions are equally amenable to deterministic enforcement. CONV-016 (per-SPEC commissionability) and CONV-017 (authoritative review designation) are primarily judgment-based and rely on human-mediated enforcement. CONV-015 metadata validation and CONV-018 attestation are the strongest candidates for deterministic enforcement via hooks or schema validation.

---

## IV. DECISION REQUESTS

| Decision ID | Prompt | Options | Recommendation | Owner |
|:--|:--|:--|:--|:--|
| DEC-001 | Should the minimum-detail floor (CONV-015) be enforced as a MUST for all new SPEC items after approval? | (a) MUST — all new SPECs must meet the four-element floor; (b) SHOULD — enforcement is advisory only; (c) MUST with a waiver mechanism for urgent patches | (a) — the AC004 failure demonstrated that advisory rules are insufficient for execution-quality control | Client |
| DEC-002 | Should per-SPEC commissionability assessment (CONV-016) be required for all external reviews covering gate packages with IMPLEMENTATION artifacts? | (a) Yes — mandatory for all such reviews; (b) Yes — mandatory but only for implementation-backed gates, not consultation-only; (c) No — advisory only | (a) — both gate types can surface IMPLEMENTATION artifacts, and per-SPEC commissionability is relevant whenever execution is downstream | Client |
| DEC-003 | Should exactly one authoritative external review be required per gate package (CONV-017)? | (a) Yes — mandatory single designation; (b) Yes — mandatory but only when more than one review-like analysis exists; (c) No — current ad hoc resolution is sufficient | (b) — the requirement is triggered by the multi-review condition; single-review packages need no designation | Client |
| DEC-004 | Should governed delegated execution require IMPLEMENTATION-mediated commissioning (CONV-018)? | (a) Yes — MUST for all governed delegation with no exception; (b) Yes — MUST with a risk-based three-condition exception (single surface, no downstream dependency, explicit low-risk attestation); (c) No — current allowance-based rule is sufficient | (b) — the risk-based exception scales governance formality with risk (aligned with NIST AI RMF proportional governance and AURA framework), prevents over-governance for simple tasks while ensuring complex execution flows through the specification surface, and creates an audit trail via the plan task Action field attestation | Client |
| DEC-005 | Should CONV-014 be elevated from SHOULD to MUST (CONV-019)? | (a) Yes — MUST with lineage-only reclassification; (b) No — keep as SHOULD | (a) — the AC004 case demonstrated that SHOULD-level enforcement allowed premature artifacts to persist as ambiguously active | Client |
| DEC-006 | Should same-gate QA correction tracking be required across plan / notes / proposal surfaces (CONV-020)? | (a) Yes — MUST with three-surface tracking; (b) Yes — MUST but only plan and proposal (notes optional); (c) No — current ad hoc tracking is sufficient | (a) — all three surfaces must stay synchronized; omitting notes creates an invisible correction history | Client |
| DEC-007 | Should consultant-scoped versus program-scoped distinction be required in gate packages (CONV-021)? | (a) Yes — explicit scope labeling required; (b) No — current practice is sufficient | (a) — explicit labeling prevents operational scope confusion and reduces the risk of misapplying consultant-only surfaces to broader roles | Client |
| DEC-008 | Should the implementation artifact architecture be changed to improve discoverability of developer-facing vs. assistant-facing specs (CONV-022)? | (a) Yes — adopt Option B naming convention: developer-facing retain `-task-specification`, consultant/assistant-facing use `-brief` suffix (TK001.1 recommendation, score 83/100); (b) Yes — adopt Option C (new subtype) instead (TK001.1 score 63/100); (c) Yes — adopt Option D (combination) instead (TK001.1 score 63/100); (d) No — keep current `execution_audience` flag as sole discriminator (Option A, TK001.1 score 67/100) | (a) — TK001.1 comparative analysis evaluated all four options against six weighted criteria. Option B scores highest (83/100) because it resolves the primary discoverability gap at the lowest governance cost. All implementation artifacts share identical SPEC structure (GAP-TK1.1-002), confirming the distinction is operational context, not document type. A naming convention correctly reflects this structural identity. No new templates, no subtype taxonomy change, forward-only application. | Client |
| DEC-009 | Should the assistant subagent be recognized as a named role `LLM_Assistant` with explicit boundary rules (CONV-023)? | (a) Yes — named role with boundary rules in §6 and ownership matrix in §8; (b) No — keep as unnamed extension of LLM_Consultant | (a) — industry practice (CrewAI, Claude Code, Microsoft) requires named role identities with explicit delegation rules; the assistant subagent's operational pattern (no DEV-REPORT, session-note evidence, consultant-authority-only) is sufficiently distinct from LLM_Developer to warrant its own boundary definition | Client |

---

## V. IMPACT AND RISKS

### A. Impact Assessment

- **Positive outcomes**:
  - SPEC items will have an enforceable quality floor, preventing under-specified execution commissions
  - Implementation Detail blocks will be model-agnostic — executable by any high-intelligence LLM, not only the authoring model
  - External reviews will catch vague SPECs before gate approval rather than after
  - Gate packages will have clear authority ordering when multiple reviews exist
  - Governed delegated execution will always flow through a traceable specification surface
  - Premature concrete artifacts will be explicitly quarantined rather than ambiguously active
  - Same-gate corrections will be visible across all governance surfaces
  - Consultant-scoped versus program-scoped operational surfaces will be unambiguous
  - Developer-facing and assistant-facing implementation artifacts will be architecturally distinguishable (pending TK001.1 resolution form)
  - The assistant subagent will have a named role identity with explicit boundary rules, eliminating operational ambiguity
  - Conventions align with established industry standards (IEEE 29148, ISO 9001, CMMI, PRINCE2, NIST AI RMF), reducing institutional risk of governance divergence from recognized best practices

- **Tradeoffs**:
  - Additional authoring overhead for SPEC items (four required metadata elements + structured Implementation Detail format per SPEC)
  - Additional review scope for external reviews covering IMPLEMENTATION artifacts
  - Additional bookkeeping for same-gate corrections (three-surface tracking)
  - The risk-based trivial-execution threshold (CONV-018) introduces an attestation element requiring author judgment — consistent with Anthropic's finding that "it's too early to mandate specific interaction patterns" and AURA's recommendation for progressive automation
  - Architectural resolution for implementation artifact discoverability (CONV-022) may require template amendments and naming convention changes
  - Formal LLM_Assistant role (CONV-023) adds a fifth agent role to the governance suite, increasing the ownership matrix complexity

### B. Risks

| Risk ID | Description | Severity | Mitigation |
|:--|:--|:--|:--|
| RISK-001 | CONV-015 minimum-detail floor increases SPEC authoring time | Low | The four required elements (target files, end-state, validation, non-targets) are already present in well-authored SPECs; the rule formalizes existing best practice |
| RISK-002 | CONV-016 per-SPEC commissionability check increases external-review scope | Medium | The check is bounded to SPEC items in the gate package's IMPLEMENTATION artifact; it does not require reviewing the full codebase |
| RISK-003 | CONV-018 risk-based three-condition exception introduces an attestation element that requires author judgment | Low | The three conditions are independently verifiable (single surface — count check; no downstream dependency — dependency graph check; explicit attestation — Action field audit). Progressive automation through memory-based optimization (per AURA framework) can reduce human intervention frequency over time |
| RISK-004 | CONV-020 three-surface tracking increases same-gate correction overhead | Low | Same-gate corrections are inherently high-stakes and deserve explicit tracking; the overhead prevents more costly downstream discovery of silent amendments |
| RISK-005 | CONV-022 architectural resolution (pending TK001.1) may require template changes and naming convention updates that affect existing authoring patterns | Low | The resolution applies to new artifacts only (no retroactive migration). TK001.1 evaluates options before committing to a specific form |
| RISK-006 | CONV-023 `LLM_Assistant` role introduction adds governance surface area (§6 boundary rules, §8 ownership matrix) | Low | The role boundary is deliberately narrow (operates under consultant authority, no DEV-REPORT, session-note evidence only). The incremental governance surface is bounded to two sections |

---

## VI. REFERENCES

### A. Internal Workspace References

| Document | Path |
|:--|:--|
| Governing Plan | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/plan_T104-PH001-ST008-AC006.md` |
| Supporting Analysis (TK001) | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/analysis/analysis_T104-PH001-ST008-AC006_implementation-governance-gap-analysis.md` |
| Supporting Analysis (TK001.1) | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/analysis/analysis_T104-PH001-ST008-AC006-TK001.1_implementation-artifact-architecture-assessment.md` |
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

### B. External Standards References

| Standard / Framework | Relevant Section | Applicable Conventions |
|:--|:--|:--|
| IEEE/ISO/IEC 29148:2018 | §5 (SRS content structure), quality attributes (completeness, verifiability, traceability) | CONV-015 |
| ISO 9001:2015 | §7.5.3 (documented information control), §8.7 (nonconforming outputs), §10.2 (CAPA) | CONV-017, CONV-019, CONV-020, CONV-022 |
| ISO 10007:2017 / IEEE 828-2012 | Configuration baseline, change authority, revision status | CONV-017 |
| ISO/IEC 20246:2017 | Work product reviews — item-level examination | CONV-016 |
| CMMI-DEV v1.3/v2.0 | Requirements Development (RD), Verification (VER) — entry/exit criteria, peer review defect tracking | CONV-015, CONV-020 |
| PRINCE2 7th Edition | Work Package authorization, Configuration Item Records, Issue Register, Communication Management Approach | CONV-015, CONV-017, CONV-018, CONV-020, CONV-021 |
| AS9100D | §10.2 — aerospace nonconformance tracking | CONV-020 |
| FDA 21 CFR 820.30 / Part 11 | Design input completeness, draft vs approved status | CONV-016, CONV-019 |
| DO-178C | §6.3 — per-requirement traceability, Table A-3 verification objectives | CONV-016 |
| ISO 27001:2022 | Annex A 5.12 (classification), 5.13 (labeling) | CONV-021 |
| NIST AI RMF 1.0 | GOVERN/MAP/MEASURE/MANAGE — proportional governance | CONV-018 |
| AURA Framework (arXiv 2510.15739) | Risk-based scoring: 0-30 auto-approve, 30-60 selective, 60+ escalate | CONV-018 |
| Claude Code | Subagents (context-amnesia), hooks (21 lifecycle events), worktree isolation, AGENTS.md role definitions | CONV-015, CONV-018, CONV-019, CONV-022, CONV-023 |
| Codex CLI | AGENTS.md, sandboxing (read-only/workspace-write/danger), PM-gated pipeline pattern | CONV-015, CONV-018, CONV-019 |
| CrewAI | Hierarchical authority, `allowed_agents`, named role definitions (Manager/Worker/Researcher) | CONV-017, CONV-023 |
| Anthropic Research (2025) | Measuring Agent Autonomy — 1-10 scale, oversight strategy shifts | CONV-018 |
| AGENTIF Benchmark (Tsinghua) | LLM failure modes on specification-heavy instructions | CONV-015 |

---

## VII. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-03-27 | Initial | Standards-input proposal authored for AC006-TK002. Seven conventions (CONV-015 through CONV-021) proposed across seven governance target files. Seven decision requests for client disposition. AC003 acknowledged as vertical-integration evidence. All conventions are pre-implementation governance rules to be approved at GATE-001 before downstream TK004 execution. |
| v2.0.0 | 2026-03-28 | Major | Industry-standard and agentic-environment grounding added to all convention rationales. CONV-015 expanded with cross-model Implementation Detail authoring sub-rule. CONV-018 revised from count-based to risk-based three-condition exception (NIST/AURA alignment). Two new conventions added: CONV-022 (implementation artifact architecture — pending TK001.1) and CONV-023 (LLM_Assistant role formalization). Two new decision requests: DEC-008 (CONV-022) and DEC-009 (CONV-023). Enforcement modalities section (§III.C) added for TK004 implementation guidance. External standards references (§VI.B) added. Impact assessment and risk register expanded. GAP-009, GAP-010, GAP-011 added to Problems/Gaps summary. Target standards expanded to include remediation-specification template. |
| v2.1.0 | 2026-03-28 | Minor | Resolved CONV-022 placeholder with TK001.1 comparative analysis findings: Option B (naming convention) adopted — developer-facing retain `-task-specification` suffix, consultant/assistant-facing use `-brief` suffix. Updated DEC-008 with specific Option B recommendation (score 83/100). Updated CONV-022 compatibility note. Added TK001.1 to §VI.A references. Removed deferral language from §I Purpose. Remediation specification scope confirmed as appropriately tight (RECYCLE-only). |
