---
artifact_type: 'ANALYSIS'
analysis_type: 'external_review'
initiative_id: 'T104'
initiative_code: 'CWS'
phase: '1'
stream_id: 'T104-PH001-ST005'
activity_id: 'T104-PH001-ST005-AC007'
gate_id: 'T104-PH001-ST005-AC007-GATE-000'
version: '1.0.0'
date: '2026-03-01'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
engagement_scope: 'Independent review of GATE-000 decision disposition package (TK001.1) — DEC001–DEC009 assessment, recommendation validation, and gap/risk identification for downstream TK002–TK004 execution.'
target_artifact: 'prompt/artifacts/tasks/T104/workspace/PH001/ST005/proposal/proposal_T104-PH001-ST005-AC007-TK001.1_gir-disposition-package.md'
source_plan: 'prompt/artifacts/tasks/T104/workspace/PH001/ST005/plan_T104-PH001-ST005.md'
reference_standard: 'prompt/templates/consultant/workspace/guideline_workspace_verification.md'
plan_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST005/plan_T104-PH001-ST005.md'
---

# ANALYSIS: External Review — GATE-000 Decision Disposition Package (T104-PH001-ST005-AC007)

> **Exemplar note**: This artifact is the canonical structural exemplar for `analysis_type: external_review`. It demonstrates: (1) engagement summary, (2) scope & inputs, (3) evidence/methodology, (4) methodology assessment with independent re-grading, (5) independent assessment per decision, (6) gaps/risks register, (7) impact assessment, (8) downstream actions, (9) overall verdict, (10) references register. Authors of future `external_review` analysis artifacts should follow this structural pattern.

---

## I. EXECUTIVE SUMMARY

**Engagement**: Independent review of the GATE-000 decision disposition package produced by `T104-PH001-ST005-AC007-TK001.1`.

**Review Purpose**: Validate that all 9 design decisions (DEC001–DEC009) are correctly reasoned and appropriately scoped before the Client approves GATE-000 and authorises downstream execution of TK002–TK004. Additionally identify any gaps, risks, or unresolved items not captured in the proposal.

**Overall Verdict**: APPROVE — all 9 recommended resolutions are sound. No overrides required. Four secondary items (one DEC-level flag, three gap/risk items) warrant the Client's awareness but do not block approval.

**Key Findings**:
- DEC001–DEC009 recommendations align with the evidence from the TK001 pattern audit; no recommendation appears unsupported or under-argued.
- DEC006 (lightweight GAP-style findings schema) is the most consequential decision in the package; the recommendation correctly prevents analysis findings from inheriting verification's gate-blocking semantics.
- DEC007 (Integration Roadmap conditionality) creates a downstream obligation in TK002: a "Downstream Actions" section must be defined for non-research types. This is scoped but not yet specified.
- Three residual items not surfaced in the proposal pose risk to TK002–TK004 execution: (a) undefined lifecycle positions for non-research types, (b) unenumerated `Disposition` field values in DEC006's schema, and (c) absence of a proposal template cross-check in TK004's target list.

---

## II. ENGAGEMENT SUMMARY

**Reviewer Role**: Independent external consultant — no authorship stake in the proposal or the analysis pattern audit. Reviewing from first principles and external exemplar reference.

**Engagement Scope**:
- Review all 9 design decisions (DEC001–DEC009) in the GATE-000 disposition package.
- Assess whether recommended options are well-reasoned, whether alternatives were fairly characterised, and whether any superior option was overlooked.
- Identify gaps, risks, or unresolved design questions not surfaced in the DEC register.
- Provide an overall APPROVE / APPROVE WITH CONDITIONS / REJECT verdict for GATE-000.

**Engagement Posture**: No deference to internal convention. Assessment is grounded in: (a) direct evidence from the referenced artifacts, (b) the verification guideline's established findings schema (as the key differentiation baseline for DEC006), and (c) structural precedents from the AC005 verification pattern (as the claimed model for DEC002).

---

## III. SCOPE & INPUTS

### A. In Scope
- `proposal_T104-PH001-ST005-AC007-TK001.1_gir-disposition-package.md` — the primary review target (DEC001–DEC009, GDR)
- `analysis_T104-PH001-ST005-AC007_analysis-pattern-audit.md` — the upstream evidence source for all DEC decisions
- `template_workspace_analysis.md` — the existing artifact being updated (DEC002, DEC003, DEC004, DEC007, DEC009)
- `guideline_workspace_verification.md §VI` — findings schema baseline (DEC006)
- `plan_T104-PH001-ST005.md` — activity definitions, TK002–TK004 scope, gate criteria

### B. Out of Scope
- Draft 2 alignment to P-STD-004 (deferred by stream plan design)
- T104D epic analysis standards (normative; future)
- T102-STD-006 CLAUSE-level verification (TK004 scope)
- Internal review of the pattern audit methodology (TK001 is upstream; treated as given)

### C. Inputs Reviewed

| # | Artifact | Path | Role in Review |
|:--|:--|:--|:--|
| 1 | GATE-000 Proposal (primary) | `prompt/artifacts/tasks/T104/workspace/PH001/ST005/proposal/proposal_T104-PH001-ST005-AC007-TK001.1_gir-disposition-package.md` | Subject of review |
| 2 | TK001 Analysis Pattern Audit | `prompt/artifacts/tasks/T104/workspace/PH001/ST005/analysis/analysis_T104-PH001-ST005-AC007_analysis-pattern-audit.md` | Evidence base for all DECs |
| 3 | Existing Analysis Template | `prompt/templates/consultant/workspace/template_workspace_analysis.md` | Current-state baseline (DEC002–DEC009) |
| 4 | Verification Guideline | `prompt/templates/consultant/workspace/guideline_workspace_verification.md` | Findings schema differentiation (DEC006) |
| 5 | ST005 Stream Plan | `prompt/artifacts/tasks/T104/workspace/PH001/ST005/plan_T104-PH001-ST005.md` | TK002–TK004 scope, gate criteria |
| 6 | External Review Exemplar | `prompt/artifacts/tasks/T104/workspace/PH001/ST002/AC000/analysis/analysis_T104-PH001-ST002-AC000_external-review.md` | Structural precedent for this artifact type |

---

## IV. EVIDENCE & METHODOLOGY

**Approach**: Document-first independent assessment. Each DEC was evaluated by:
1. Reading the recommended option and all alternatives in the proposal.
2. Tracing the recommendation's rationale to specific evidence in the TK001 pattern audit (gap register, exemplar inventory, divergent patterns table).
3. Testing whether the rationale holds against the cited evidence or whether the evidence could equally support an alternative.
4. Assessing whether any option *outside* the presented set was more appropriate.

**Evidence sources consulted**:
- Pattern audit §III.B (Divergent Patterns table) — for DEC001, DEC002, DEC003
- Pattern audit §IV (Gap Register, GAP-001–GAP-010) — for all DECs
- Pattern audit §VI (Template Update Blueprint) — for DEC003, DEC004, DEC007, DEC009
- Verification guideline §VI (FINDING-### schema, severity taxonomy, Situation A/B rules) — for DEC006
- Existing analysis template sections I–X — for DEC002, DEC003, DEC005, DEC007, DEC009
- ST005 stream plan AC007 task register — for TK002–TK004 scope expectations

**Confidence**: HIGH. All DEC decisions are traceable to concrete artifact evidence. No DEC relies on inference or assumption without cited support.

---

## V. METHODOLOGY ASSESSMENT

### A. What Was Done Well

The TK001.1 proposal is methodologically sound by external standards:

- **Option completeness**: Each DEC presents 3–4 distinct options with honest characterisation of trade-offs. No option is presented as a strawman solely to make the recommended option look better.
- **Rationale quality**: Recommendations are supported by specific pattern audit evidence (gap IDs, exemplar references), not by assertion alone.
- **Pre-selection transparency**: The proposal explicitly states that recommended options are "pre-checked for review speed" and that the authoritative signal is the GDR — this avoids the common failure mode of presenting pre-filled decisions as fait accompli.
- **Downstream traceability**: Each DEC maps to specific TK002/TK003/TK004 implementation targets. The proposal is execution-ready, not just advisory.
- **Semantic boundary clarity**: DEC006 correctly identifies the key conceptual boundary (analysis vs. verification findings authority). This is the most important design decision and it is handled with appropriate care.

### B. Methodological Concerns

#### Concern 1: DEC007 Creates an Unspecified Obligation

DEC007 recommends retaining the existing Integration Roadmap for research synthesis and states that "other types use a generic 'Downstream Actions' section." However, the proposal does not specify:
- What fields belong in this generic section
- Whether it varies by type (compliance audit → remediation checklist; assessment → hardening roadmap; pattern audit → decision seeding)
- Whether it is narrative, tabular, or checklist format

The recommended option (a) is still correct — minimal disruption is right for Draft 1. But TK002 must be aware this obligation exists. **Risk**: TK002 may under-specify the generic section if this expectation is not explicit.

**External re-assessment**: Option (b) — replacing the roadmap with a single generic section — is simpler than (a) and eliminates the conditional marker. I considered recommending (b) over (a), but decided against it: the existing research-synthesis roadmap is detailed and valuable; destroying it to simplify the template is a net loss. Option (a) is correct, with the flag that TK002 must define the generic "Downstream Actions" content.

#### Concern 2: DEC006 Disposition Field is Under-Specified

The lightweight GAP-### schema includes a `Disposition` field but neither the proposal nor the pattern audit enumerates allowed values. If `Disposition` is free-text, different analysis artifacts will record: "pending", "TBD", "resolved in TK002", "deferred", "handled by plan amendment" — all meaning different things. This undermines the structured tracking purpose.

**External re-assessment**: This is a TK002 implementation detail, not a proposal-level design decision. However, TK002 should define a bounded set of disposition values (e.g., `pending_decision`, `resolved`, `deferred_to_<task>`, `superseded`, `accepted_as_is`) to ensure cross-artifact consistency. Not a blocking item — acceptable as a known TK002 obligation.

#### Concern 3: Non-Research Type Lifecycle Positions Are Absent

DEC001 defines a 5-type taxonomy. DEC008 correctly scopes IG-002 to research synthesis only. But neither DEC nor the pattern audit defines the lifecycle positions for `compliance_audit`, `assessment`, `external_review`, or `pattern_audit`. TK002 will need to specify:
- What triggers each non-research type
- What each type's upstream artifact(s) are
- What the downstream handoff is

The `external_review` type (this artifact) demonstrates one lifecycle: prompted by a gate review need → produces a verdict and gap register → feeds downstream approval decision. But the pattern audit only has one exemplar for external_review, which makes the lifecycle definition somewhat speculative. **Risk**: TK002 may produce preliminary lifecycle definitions that require rapid revision as new exemplars emerge.

---

## VI. INDEPENDENT ASSESSMENT — DEC001–DEC009

### DEC001 — 5-Type Enum | **AGREE with (a)**

**Evidence check**: The pattern audit's §II.A exemplar inventory shows 4 distinct types from primary exemplars. The ST005 pattern audit itself uses `analysis_type: 'pattern_audit'` — a 5th type already in production. Rejecting `pattern_audit` (option b) would retroactively invalidate an authored artifact. The open-ended string (option c) provides no governance value.

**Alternative considered**: Whether `external_review` warrants a dedicated type or is better modelled as an authoring-mode modifier (e.g., `assessment` authored in external mode). The T104-ST002-AC000 exemplar shows a sufficiently distinct structure (independent criteria weighting, re-grading tables, transition plan, clarifying questions as a closing section) that a dedicated type is justified. No override.

**Verdict**: Confirm (a).

---

### DEC002 — Single Template with Conditional Sections | **AGREE with (a)**

**Evidence check**: The verification guideline precedent (AC005) is directly applicable — it uses one template with conditional markers, not per-type templates. The pattern audit §III.B shows 4+ distinct structures, but these can be accommodated via conditional markers without requiring 5 separate files.

**Alternative considered**: Option (c) hybrid (single base + appendices). Appendices would work but add complexity that conditional markers in-template handle more cleanly. No advantage over (a).

**Verdict**: Confirm (a).

---

### DEC003 — Common Keys + Optional Type-Specific Keys | **AGREE with (a)**

**Evidence check**: The pattern audit §IV GAP-004 correctly documents the key mismatch — existing keys (`research_id`, `research_brief`, `research_report`, `target_proposal`) are research-specific. The proposed common baseline + optional type-specific keys preserves traceability without forcing irrelevant keys on non-research types. Option (b) would produce 5 separate frontmatter schemas with high maintenance cost. Option (c) would strip traceability.

**Verdict**: Confirm (a).

---

### DEC004 — HTML Comment Conditional Markers | **AGREE with (a)**

**Evidence check**: The existing `template_workspace_analysis.md` already uses HTML comments for `<!-- PURPOSE: ... -->` inline guidance. This is established convention. Option (b) guideline-only rules are weaker — LLM authors cannot see them in context while writing. Option (c) subsection labels are verbose and pollute rendered output.

**Verdict**: Confirm (a).

---

### DEC005 — Universal Evidence Section Near Top | **AGREE with (a)**

**Evidence check**: All 4 pattern audit exemplars ground claims in specific evidence. The pattern audit §III.A convergent patterns explicitly lists "Evidence-grounded methodology" as pattern 3, appearing in all exemplars. Option (b) type-specific placement would mean some analysis types have no explicit evidence section — inconsistent with all observed practice. Option (c) embedded-only ignores the need for methodology transparency upfront.

**Verdict**: Confirm (a).

---

### DEC006 — Lightweight GAP-Style Findings Schema | **STRONGLY AGREE with (b)**

**Evidence check**: The verification guideline §VI defines `FINDING-###` with severity taxonomy (CRITICAL → NON-CONFORMANCE → ADVISORY) and Situation A/B gate-blocking semantics. An analysis `FINDING-CRITICAL` would falsely imply it blocks downstream execution — which analysis artifacts have no authority to do.

**Alternative considered**: Whether the schema should use `AN-GAP-###` (with `AN-` prefix) to distinguish from verification gaps, or plain `GAP-###`. Prefixing reduces collision risk in cross-artifact contexts but adds cognitive overhead for in-analysis use. Given that analysis artifacts are stream-scoped and unlikely to be in context alongside verification artifacts simultaneously, plain `GAP-###` is acceptable. Authors should be aware the `GAP-###` ID namespace is local to the analysis artifact.

**Key implementation flag for TK002**: The `Disposition` field requires enumerated values. Suggested values: `pending_decision`, `resolved`, `deferred_to_<task>`, `superseded`, `accepted_as_is`. Without this, the structured tracking benefit of the register is weakened.

**Verdict**: Confirm (b). Flag Disposition enumeration to TK002.

---

### DEC007 — Conditional Integration Roadmap | **AGREE with (a), with flag**

**Evidence check**: Pattern audit §II.B confirms the Integration Roadmap (5 steps, research-specific) is deeply embedded in the proposal seeding workflow. Marking it conditional preserves this value for research synthesis while excluding it for other types.

**Alternative considered**: Option (b) — replacing entirely with a generic "Downstream Actions" section — is simpler but destroys valuable research synthesis content. Not worth the disruption.

**Flag for TK002**: TK002 must define the content requirements for the generic "Downstream Actions" section that other types will use. Minimum expected fields: downstream artifact type, target file/task reference, handoff trigger condition, responsible role. Per-type guidance should address: compliance audit → remediation task reference; assessment → hardening/plan amendment; pattern audit → proposal gate seeding; external review → decision authority record.

**Verdict**: Confirm (a). TK002 must define "Downstream Actions" generic section explicitly.

---

### DEC008 — Scope IG-002 to Research Synthesis Only | **STRONGLY AGREE with (a)**

**Evidence check**: The T104-IG-002 Brief→Report→Analysis→Proposal chain is definitionally a research workflow. The pattern audit §II.B Divergent Patterns table confirms that non-research exemplars (compliance audit, assessment, external review) have different upstream triggers and downstream handoffs not covered by IG-002.

**Alternative considered**: Option (c) omitting IG-002 from the analysis guideline entirely. This would lose the benefit of the explicit cross-reference for research synthesis authors who need to know where the lifecycle chain is defined. Option (a) keeps the reference with correct scope.

**Verdict**: Confirm (a).

---

### DEC009 — Universal Scope & Inputs Section Near Top | **AGREE with (a)**

**Evidence check**: Pattern audit §III.A convergent pattern 2: "Scope & Inputs section — explicit listing of what is in-scope, out-of-scope, and an enumeration of reviewed/referenced artifacts. All four exemplars have this near the top." The current template's "Source Material Summary" (Section II) is research-specific and does not substitute for a universal scope framing.

**Verdict**: Confirm (a).

---

## VII. GAPS / RISKS REGISTER

| GAP ID | Category | Title | Description | Disposition | Downstream Target |
|:--|:--|:--|:--|:--|:--|
| GAP-001 | TK002 scope | Lifecycle positions undefined for non-research types | DEC008 scopes IG-002 to research synthesis, but no lifecycle positions are defined for `compliance_audit`, `assessment`, `external_review`, `pattern_audit`. TK002 must define these from limited exemplar evidence. | Accepted — TK002 must define preliminary lifecycle positions; mark as "Draft 1 — subject to revision as exemplars accumulate." | TK002 |
| GAP-002 | DEC006 schema | `Disposition` field values not enumerated | The lightweight GAP-### schema includes a `Disposition` field with no bounded value set. Free-text disposition undermines structured tracking. | Deferred to TK002 — enumerate: `pending_decision`, `resolved`, `deferred_to_<task>`, `superseded`, `accepted_as_is`. | TK002 |
| GAP-003 | TK004 scope | Proposal template missing from TK004 cross-check targets | TK004 cross-checks `T102-STD-006`, `T104-IG-002`, `guideline_workspace_verification.md`, `workspace_documentation_rules.md`, and `guideline_workspace_plan.md`. It does not include `template_workspace_proposal.md`. The analysis→proposal handoff (for research synthesis) depends on Section V of the analysis template feeding into the proposal's Candidate Inventory. Structural drift between these two templates could create handoff friction. | Pending decision — Client to confirm whether to add proposal template as TK004 target or defer to Draft 2. | TK004 or deferred |
| GAP-004 | DEC007 obligation | "Downstream Actions" generic section content not defined | DEC007 (a) commits to creating a generic "Downstream Actions" section for non-research types in TK002. No fields, format, or per-type variant guidance is specified in the proposal. TK002 may under-specify this section if the obligation is not made explicit. | Accepted — TK002 must define the section explicitly. See §V.B Concern 1 for field suggestions. | TK002 |

---

## VIII. IMPACT ASSESSMENT

### A. Impact on TK002 (Guideline Authoring)

DEC001–DEC009 collectively define TK002's scope as broader than a simple guideline authoring task. TK002 must produce:
- Role boundary (§ — LLM_Consultant sole author)
- 5-type taxonomy with enum and per-type lifecycle positions (DEC001, DEC008)
- Required common sections (DEC005, DEC009) and type-specific sections (DEC002, DEC007)
- Evidence rules (DEC005)
- Findings/gap register schema with enumerated Disposition values (DEC006 + GAP-002)
- Frontmatter conventions (DEC003)
- Downstream Actions section definition (GAP-004)
- Naming convention (stream-level analysis/ directory, P-STD-004-CLAUSE-003C/003F)
- Template inventory reference

**Assessment**: TK002 is the heaviest implementation task in AC007. Given the 5-type lifecycle requirement and the gap-filling obligations from GAP-001, GAP-002, and GAP-004, the client should expect TK002 output to be a substantial document (10+ sections). This is appropriate — the guideline is the normative authority for all future analysis artifacts.

### B. Impact on TK003 (Template Update)

DEC002–DEC009 require 8 distinct changes to `template_workspace_analysis.md`:
1. Add `analysis_type` to frontmatter (DEC001, DEC003)
2. Add optional type-specific keys (DEC003)
3. Add universal Scope & Inputs section (DEC009)
4. Add universal Evidence/Methodology section (DEC005)
5. Mark E-ID Candidate Mapping as `<!-- RESEARCH SYNTHESIS ONLY -->` (DEC004)
6. Add Findings/Gap Register section (DEC006)
7. Mark Integration Roadmap as conditional; add generic Downstream Actions section (DEC007)
8. Add References/Links Register (convergent pattern from pattern audit)

**Assessment**: TK003 is well-scoped. All changes are additive or conditional-marker insertions — no section deletion required. The existing template's Section I (Executive Summary), Sections III–IV (Key Findings, Cross-Cutting Synthesis), and Section VI (Consultant Recommendations) are retained as research-synthesis content.

### C. Impact on TK004 (Cross-Check)

The current TK004 target list covers 5 cross-check dimensions. GAP-003 proposes adding a 6th (`template_workspace_proposal.md`). If accepted, TK004 scope expands modestly. If deferred, a residual risk of handoff drift between analysis and proposal templates remains through Draft 2.

### D. Impact on Downstream AC007 Gate (GATE-001 / Draft 2)

GATE-001 (Draft 2, `P-PH000-ST001-AC004` dependency) is unaffected by any of the DEC decisions. All decisions are correctly scoped to Draft 1 (exemplar-derived, no P-STD-004 CLAUSE alignment required).

---

## IX. DOWNSTREAM ACTIONS

<!-- EXTERNAL REVIEW TYPE — downstream actions are decision authority records and transition recommendations, not proposal seeding -->

| Action | Owner | Priority | Trigger | Notes |
|:--|:--|:--|:--|:--|
| Record Client Decision in GDR (§V of proposal) | Client | IMMEDIATE | Upon approval | Set `Client Decision = APPROVE` or `APPROVE WITH CONDITIONS`; record Decision Date and Decision Reference |
| TK002: Define lifecycle positions for all 5 analysis types | LLM_Consultant | HIGH | TK002 start | Treat non-research lifecycle positions as "Draft 1 preliminary" — mark for revision as exemplars accumulate (GAP-001) |
| TK002: Enumerate `Disposition` field values for GAP-### schema | LLM_Consultant | HIGH | TK002 authoring | Define bounded value set; suggest: `pending_decision`, `resolved`, `deferred_to_<task>`, `superseded`, `accepted_as_is` (GAP-002) |
| TK002: Define "Downstream Actions" generic section | LLM_Consultant | HIGH | TK002 authoring | Define fields, format, and per-type guidance for non-research types (GAP-004) |
| Client decision: Add proposal template to TK004 targets? | Client | MEDIUM | Pre-TK004 | If yes, TK004 adds `template_workspace_proposal.md` cross-check; if no, defer to Draft 2 (GAP-003) |

---

## X. OVERALL VERDICT

**Verdict**: APPROVE

The GATE-000 disposition package is decision-ready. All 9 DEC recommendations are well-reasoned, evidence-grounded, and appropriately scoped for Draft 1. No recommendation warrants an override.

The four gap items (GAP-001 through GAP-004) are implementation-level obligations for TK002–TK004, not proposal-level design failures. They do not block approval. GAP-003 (proposal template cross-check) is the only item requiring a Client decision; the others are TK002 authoring obligations.

**Confidence level**: HIGH. The proposal was evaluated against all cited evidence sources; no claim was found unsupported.

**Conditions on approval**: None required. GAP items are tracked in §VII and actioned in §IX.

---

## XI. REFERENCES / LINKS REGISTER

| Document | Path |
|:--|:--|
| GATE-000 Proposal (primary review target) | `prompt/artifacts/tasks/T104/workspace/PH001/ST005/proposal/proposal_T104-PH001-ST005-AC007-TK001.1_gir-disposition-package.md` |
| TK001 Analysis Pattern Audit | `prompt/artifacts/tasks/T104/workspace/PH001/ST005/analysis/analysis_T104-PH001-ST005-AC007_analysis-pattern-audit.md` |
| ST005 Stream Plan | `prompt/artifacts/tasks/T104/workspace/PH001/ST005/plan_T104-PH001-ST005.md` |
| Existing Analysis Template | `prompt/templates/consultant/workspace/template_workspace_analysis.md` |
| Verification Guideline (§VI findings schema) | `prompt/templates/consultant/workspace/guideline_workspace_verification.md` |
| External Review Structural Precedent | `prompt/artifacts/tasks/T104/workspace/PH001/ST002/AC000/analysis/analysis_T104-PH001-ST002-AC000_external-review.md` |
| T104 SPS (T104-IG-002 source) | `prompt/artifacts/tasks/T104/ssot/sps_T104-CWS.md` |
| T102-STD-006 Research Artifacts Index | `prompt/artifacts/tasks/T102/standard/standard_T102-STD-006_research-artifacts-index.md` |

---

## XII. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-03-01 | Initial | External review of GATE-000 disposition package (DEC001–DEC009). Verdict: APPROVE. Four gap items identified (GAP-001–GAP-004). Structured as canonical `external_review` subtype exemplar. |
