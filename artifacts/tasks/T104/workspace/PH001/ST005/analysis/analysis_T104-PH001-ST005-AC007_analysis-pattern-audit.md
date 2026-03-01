---
artifact_type: 'ANALYSIS'
analysis_type: 'pattern_audit'
initiative_id: 'T104'
initiative_code: 'CWS'
phase: '1'
stream_id: 'T104-PH001-ST005'
activity_id: 'T104-PH001-ST005-AC007'
task_id: 'T104-PH001-ST005-AC007-TK001'
version: '1.0.0'
date: '2026-02-28'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST005/plan_T104-PH001-ST005.md'
---

# Analysis: Analysis Pattern Audit (T104-PH001-ST005-AC007-TK001)

## I. Purpose & Scope

**Purpose**: Audit existing analysis exemplars across the program and T104 initiative workspaces, extract common structural patterns, benchmark the existing template against those patterns, identify template gaps, and produce the design inputs needed to author `guideline_workspace_analysis.md` (TK002) and update `template_workspace_analysis.md` (TK003). Findings from this audit are to be resolved via Socratic consultation (TK001.1) before implementation proceeds.

**Scope**:
- **In scope**: All analysis artifacts under `P/` and `T104/` workspaces; the existing analysis template; `workspace_documentation_rules.md` artifact inventory; `guideline_workspace_plan.md` and `guideline_workspace_verification.md` for role boundary and findings schema reference; `T104-IG-002` linking chain; `T102-STD-006` research workflow standard.
- **Out of scope**: P-STD-004 formal naming alignment (Draft 2 via TK901); T104D epic normative analysis standards; T101 role formalization; implementation of TK002–TK004 (deferred to post-TK001.1 decisions).

**Inputs reviewed**:
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC006/analysis/analysis_P-PH000-ST001-AC006_pre-promotion-audit.md`
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/analysis/analysis_P-PH000-ST001-AC007_p-std-005-hardening-assessment.md`
- `prompt/artifacts/tasks/T104/workspace/PH001/ST002/AC000/analysis/analysis_T104-PH001-ST002-AC000_external-review.md`
- `prompt/artifacts/tasks/T104/workspace/PH001/ST001/AC002/analysis/analysis_T104-PH001-ST001-AC002-TK005_cross-reference-compliance.md`
- `prompt/templates/consultant/workspace/template_workspace_analysis.md` (existing template)
- `prompt/templates/consultant/workspace/guideline_workspace_verification.md` (role boundary + findings schema reference)
- `prompt/templates/consultant/workspace/workspace_documentation_rules.md`
- `prompt/artifacts/tasks/T104/ssot/sps_T104-CWS.md` (T104-IG-002 body)
- `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-006_research-artifacts-index.md`

---

## II. Exemplar Inventory

### A. Analysis Artifacts Reviewed

| # | Exemplar | Type | Author | Key Structural Sections |
|:--|:--|:--|:--|:--|
| 1 | `P-AC006_pre-promotion-audit` | Compliance audit | LLM_Reviewer | Executive Summary (verdict), Scope & Inputs, Checklist Results (tabular per P-STD-001 CLAUSE), Findings & Remediation Placement (blocking/non-blocking, F001–F003), Evidence (commands run) |
| 2 | `P-AC007_p-std-005-hardening-assessment` | Comprehensive assessment | LLM_Reviewer / LLM_Consultant | Compliance Audit tables (per CLAUSE, per substandard), Issues/Risks register, structural refactoring analysis, benchmarking, gap/issues/risk sections |
| 3 | `T104-ST002-AC000_external-review` | External independent review | External consultant mode | Engagement summary, methodology assessment, independent criteria re-grading (weighted tables), gaps/risks/tighten-up items, impact assessment, transition plan, overall verdict, clarifying questions |
| 4 | `T104-ST001-AC002-TK005_cross-reference-compliance` | Compliance verification | LLM_Consultant | Executive Summary (step results), Inputs, Step 1 (cross-reference checklist), Step 2 (ADR compliance table), Step 3 (traceability matrix + gap identification), Gap Register (structured fields), Remediation Evidence (commands + results), Next Steps, Links Register |

### B. Existing Template Assessment

The existing `template_workspace_analysis.md` is:

| Characteristic | Assessment |
|:--|:--|
| **Analysis type assumed** | Research synthesis only (Brief→Report→Analysis→Proposal chain) |
| **E-ID candidate focus** | Section V (E-ID Candidate Mapping) occupies ~60% of the template; not applicable to other analysis types |
| **Role boundary** | Hardcodes `author: 'LLM_Consultant'` — this is correct and should be retained as a canonical rule |
| **Section count** | 10 numbered sections (I–X) + Metadata |
| **Frontmatter keys** | Research-oriented: `research_id`, `research_brief`, `research_report`, `target_proposal` |
| **Evidence methodology** | No dedicated evidence section; minimal "Supporting Evidence" in Appendix C |
| **Scope & Inputs** | No equivalent section; "Source Material Summary" (Section II) is research-specific |
| **Findings / gap register** | No dedicated findings register; risk/opportunity tables in Section IV.C use E-ID candidate columns |
| **Downstream integration** | Section VII (Integration Roadmap) has 5 detailed steps specific to proposal seeding |
| **Links Register** | No dedicated references/links section |

---

## III. Pattern Extraction

### A. Convergent Patterns (Stable Across All Exemplars)

The following patterns appear consistently and should be codified in the guideline:

1. **Executive Summary with verdict/disposition** — All exemplars lead with a brief summary containing purpose, scope framing, and a conclusion or verdict. This is the "what and so what" before the detail.

2. **Scope & Inputs section** — Explicit listing of what is in-scope, out-of-scope, and an enumeration of reviewed/referenced artifacts. All four exemplars have this near the top.

3. **Evidence-grounded methodology** — All exemplars ground claims in specific evidence: file paths, command outputs, line numbers, grep results. General assertions without evidence do not appear in mature exemplars.

4. **Structured findings / gap registers** — When issues or gaps are identified, all exemplars use a register with structured fields (ID, category, description, disposition). IDs vary by exemplar (`F001`, `GAP-ADR7-001`, `FIND-CR-001`) but the structural pattern is consistent.

5. **References / Links Register** — Most exemplars close with a links table of all referenced artifacts using repo-relative paths.

6. **Changelog** — Present in more mature exemplars; standard for versioned artifacts.

### B. Divergent Patterns (Require Standardization via TK001.1)

| Pattern | Exemplar 1 (P-AC006) | Exemplar 2 (P-AC007) | Exemplar 3 (T104-ST002-AC000) | Exemplar 4 (T104-AC002-TK005) |
|:--|:--|:--|:--|:--|
| **Finding ID format** | `F001`, `F002`, `F003` | Inline in sections (no structured IDs) | `GAP-1`, `RISK-1`, `ITEM-1` | `GAP-ADR7-001`, `GAP-TRC-001` |
| **Analysis structure** | Checklist → Findings → Evidence | Tabular compliance + risk register | Grading matrix + narrative assessment | Step-based verification + gap register |
| **Downstream artifact** | Remediation during TK004/TK005 | Plan amendment + hardening tasks | Decision input (no binding handoff) | Remediation task (TK006) |
| **Author role** | LLM_Reviewer | LLM_Reviewer / LLM_Consultant | External consultant mode | LLM_Consultant |
| **Lifecycle position** | Pre-promotion gate | Post-promotion hardening | Pre-decision review | Mid-activity compliance check |

---

## IV. Gap Register

Gaps identified between the existing `template_workspace_analysis.md` and the observed exemplar patterns. All gaps are inputs for TK001.1 design decisions.

| Gap ID | Category | Title | Description | TK001.1 Decision Needed |
|:--|:--|:--|:--|:--|
| GAP-001 | Type coverage | Analysis type diversity | Template assumes research-synthesis-only workflow. Exemplars show at least 4 distinct types: research synthesis, compliance audit, assessment/hardening, external review. | Define canonical type taxonomy and determine whether template handles all types via conditional sections or requires type-specific variants. |
| GAP-002 | Role boundary | Author role — RESOLVED | Template hardcodes `author: 'LLM_Consultant'`. This is correct. LLM_Consultant is ALWAYS the author of analysis artifacts regardless of analysis type. No change needed. | None — resolved by QA decision. |
| GAP-003 | Structure | Rigid single-type structure | Template's 10-section structure is research-specific. Compliance audits, assessments, and external reviews use fundamentally different structures (checklists, grading matrices, tabular audits). | Decide: single template with conditional sections (recommended, mirrors AC005 verification precedent), or multiple type-specific templates. |
| GAP-004 | Frontmatter | Frontmatter key mismatch | Template keys are research-oriented (`research_id`, `research_brief`, `research_report`, `target_proposal`). Exemplars use `target_standard`, `reference_standard`, `target_artifact`, `analysis_type`, `source_plan`. Only the AC005 pattern audit uses `analysis_type` as a discriminator. | Define canonical frontmatter key set: common keys + type-specific keys. Confirm `analysis_type` as mandatory discriminator. |
| GAP-005 | Conditional sections | E-ID mapping conditionality | Section V (E-ID Candidate Mapping) occupies ~60% of the template and applies only to research synthesis. Making it mandatory for all analysis types is incorrect. | Mark Section V as research-synthesis-only via a clear conditional marker (e.g., HTML comment). Determine what the equivalent section is for other types. |
| GAP-006 | Evidence | Missing evidence methodology | No dedicated evidence section. Only Appendix C ("Supporting Evidence") for key claims. Compliance exemplars consistently embed specific evidence (commands, file paths, line numbers) inline. | Add evidence/methodology section to common required sections. Define evidence requirements per analysis type. |
| GAP-007 | Scope framing | Missing Scope & Inputs section | Template opens with "Source Material Summary" (Section II), which is research-specific. All four exemplars have a universal Scope & Inputs section near the top. | Add Scope & Inputs as a common required section (Section II or integrated into executive summary). |
| GAP-008 | Findings | Gap/findings register pattern | Template uses Risk & Opportunity tables (Section IV.C) with E-ID candidate columns. Exemplars use structured findings/gap registers with IDs, categories, disposition tracking. These serve different purposes. | Define a common lightweight findings/gap register pattern for analysis artifacts. Decide whether it aligns with `guideline_workspace_verification.md §VI` (findings schema) or uses a lighter-weight convention. |
| GAP-009 | Downstream flow | Integration Roadmap over-specification | Section VII (Integration Roadmap, 5 steps) is deeply embedded in the research-synthesis→proposal seeding workflow. Other analysis types have different downstream flows (remediation, plan amendment, decision input). | Replace with a generic "Downstream Actions" section or make Section VII conditional. Define downstream flow patterns per type. |
| GAP-010 | Lifecycle | Linking chain scope | T104-IG-002's Brief→Report→Analysis→Proposal chain is correctly reflected by the template. However, this chain applies to research synthesis only. Other types don't follow this chain. | Guideline must distinguish: the T104-IG-002 chain governs research synthesis type only; other types have their own lifecycle positions. Cross-reference T102-STD-006 conventions for research synthesis explicitly. |

---

## V. Guideline Section Blueprint (TK002 Input — Preliminary)

The following sections are proposed for `guideline_workspace_analysis.md`. These are preliminary and subject to revision pending TK001.1 design decisions.

| # | Section | Content Summary | Key Gap(s) Addressed | Design Decision Needed? |
|:--|:--|:--|:--|:--|
| I | Purpose | Guideline scope: analysis artifact authoring for consultant workspace; dynamic Draft 1 caveat | — | No |
| II | Role Boundary | LLM_Consultant is the SOLE author of all analysis artifact types. No exceptions. | GAP-002 (resolved) | No |
| III | Analysis Types & Lifecycle | Type taxonomy (research synthesis, compliance audit, assessment/hardening, external review). Lifecycle per type: position in workflow, upstream trigger, downstream handoff. T104-IG-002 linking chain explicitly scoped to research synthesis type only. Cross-reference T102-STD-006 for research synthesis. | GAP-001, GAP-010 | Yes (type taxonomy + lifecycle) |
| IV | Common Required Sections | Universal sections for all types: Executive Summary, Scope & Inputs, Evidence/Methodology, References/Links Register, Changelog. | GAP-007, GAP-006 | Partial (evidence requirements per type) |
| V | Type-Specific Sections | Research synthesis: Section II (Source Material Summary), III (Key Findings), IV (Cross-Cutting Synthesis), V (E-ID Candidate Mapping), VI (Consultant Recommendations), VII (Integration Roadmap). Compliance audit: Checklist Results, Gap Register. Assessment: Tabular Audit, Issues/Risks. External review: Grading Matrix, Impact Assessment, Transition Recommendations. | GAP-003, GAP-005, GAP-009 | Yes (section requirements per type) |
| VI | Findings/Gap Register | Common lightweight findings schema (distinct from verification findings which carry gate-blocking semantics). When to use a findings register vs. inline findings. | GAP-008 | Yes (findings schema design) |
| VII | Evidence Rules | Evidence-first: claims grounded in specific evidence (file paths, commands, line numbers). Evidence methodology section placement and content requirements per type. | GAP-006 | Partial |
| VIII | Frontmatter Conventions | Common keys + type-specific keys. `analysis_type` as mandatory discriminator. Canonical key set per type. | GAP-004 | Yes (full key set) |
| IX | Naming Convention | File: `analysis_<context>_<kebab-topic>.md`. Directory: stream-level `analysis/` per P-STD-004-CLAUSE-003C and 003F (stream-only restriction for analysis). | P-STD-004 | No |
| X | Template Inventory | Reference to `template_workspace_analysis.md` | — | No |
| XI | Changelog | Version history | — | No |

---

## VI. Template Update Blueprint (TK003 Input — Preliminary)

The following changes are proposed for `template_workspace_analysis.md`. These are preliminary and subject to revision pending TK001.1 design decisions.

| Change | Current State | Proposed State | Gap Addressed | Decision Needed? |
|:--|:--|:--|:--|:--|
| Add `analysis_type` frontmatter key | Not present | Mandatory: one of `research_synthesis`, `compliance_audit`, `assessment`, `external_review` | GAP-004 | Confirm type enum |
| Add type-specific frontmatter keys | Only research keys | Add: `target_standard`, `target_artifact`, `source_plan`, `reference_standard` as optional type-specific keys | GAP-004 | Confirm key list |
| Add Scope & Inputs section (universal) | Not present | New Section II (shift existing sections down) | GAP-007 | Placement |
| Mark E-ID mapping as conditional | Mandatory (Section V) | Add HTML comment: `<!-- RESEARCH SYNTHESIS ONLY — omit for other analysis types -->` | GAP-005 | Confirm marker convention |
| Add findings/gap register section | Only Risk/Opportunity tables (Section IV.C) | New section with lightweight findings register (ID, category, description, disposition) | GAP-008 | Register schema |
| Add evidence methodology section | Appendix C only | New universal section near top (after Scope & Inputs) | GAP-006 | Section placement |
| Replace / conditionalize Integration Roadmap | Section VII: 5-step research-specific roadmap | Either mark as `<!-- RESEARCH SYNTHESIS ONLY -->` or generalize to "Downstream Actions" with type-specific variants | GAP-009 | Approach decision |
| Add References / Links Register | Not present | New closing section (consistent with all exemplars) | Convergent pattern | No |
| Update Changelog | Section IX | Retain; add entry for this update | — | No |

---

## VII. Cross-Check Targets (TK004 Input)

The following cross-checks are required after TK002 and TK003 are complete:

| # | Cross-Check Target | What to Verify | Standard / Artifact |
|:--|:--|:--|:--|
| 1 | T102-STD-006 (Research Artifacts Index) | Guideline §III research synthesis lifecycle references correct T102-STD-006 CLAUSE IDs (CLAUSE-001 ID patterns, CLAUSE-002 table schemas, CLAUSE-005 cross-artifact referencing). No semantic drift. | `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-006_research-artifacts-index.md` |
| 2 | T104-IG-002 (Research Linking) | Guideline's research synthesis lifecycle matches the Brief→Report→Analysis→Proposal chain exactly. "No duplication; reference by ID and section" rule is reflected. | `prompt/artifacts/tasks/T104/ssot/sps_T104-CWS.md` (IG-002 body) |
| 3 | `guideline_workspace_verification.md §VI` | Analysis findings schema (guideline §VI) does not contradict verification findings schema. Analysis findings must be clearly distinguished as non-gate-blocking. | `prompt/templates/consultant/workspace/guideline_workspace_verification.md` |
| 4 | `workspace_documentation_rules.md` | After TK002/TK003 delivery: §3 ANALYSIS row description reflects delivered guideline scope; §4.F template entry is current; §5 ANALYSIS guideline entry updated from "(Draft 1 planned)" to delivered path. | `prompt/templates/consultant/workspace/workspace_documentation_rules.md` |
| 5 | `guideline_workspace_plan.md` | Analysis artifacts are confirmed as stream-level type subdirectory per P-STD-004-CLAUSE-003C/003F (stream-only restriction). No contradiction with plan guideline on stream-vs-activity scope. | `prompt/templates/consultant/workspace/guideline_workspace_plan.md` |

---

## VIII. Design Decisions Register (Pending TK001.1)

The following design decisions are open. They will be resolved via Socratic consultation in TK001.1. The session notes file (`snotes_T104-PH001-ST005-AC007-SES001.md`) will record the final decisions (DEC001+).

| # | Decision Area | Options | Recommendation (preliminary) | Gap(s) |
|:--|:--|:--|:--|:--|
| DEC001 | Analysis type taxonomy | (a) 4 types as identified; (b) fewer types with broader definitions; (c) open-ended (no fixed taxonomy) | Option (a): 4 types as identified — research synthesis, compliance audit, assessment, external review | GAP-001 |
| DEC002 | Template approach | (a) Single template with conditional sections; (b) multiple type-specific templates | Option (a): single template with conditional sections — follows AC005 verification precedent, minimizes file count | GAP-003 |
| DEC003 | Frontmatter key set | (a) Common keys only + `analysis_type`; (b) full type-specific key sets defined per type | Option (a): common keys + `analysis_type` mandatory + optional type-specific keys registered in guideline | GAP-004 |
| DEC004 | E-ID mapping conditionality marker | (a) HTML comment `<!-- RESEARCH SYNTHESIS ONLY -->`; (b) guideline-only rule (no template marker); (c) separate sub-section with type label | Option (a): HTML comment — matches existing template convention for informational comments | GAP-005 |
| DEC005 | Evidence section placement | (a) Universal §II (after executive summary); (b) type-specific placement; (c) evidence embedded per-section only | Option (a): Universal §II — ensures evidence rules apply consistently across types | GAP-006 |
| DEC006 | Findings/gap register schema | (a) Mirror verification guideline §VI (FINDING-###, severity fields); (b) lighter-weight schema (GAP-###, category, description, disposition only) | Option (b): lighter-weight — analysis findings do not carry gate-blocking semantics and should not be confused with verification findings | GAP-008 |
| DEC007 | Integration Roadmap handling | (a) Mark Section VII as `<!-- RESEARCH SYNTHESIS ONLY -->`; (b) replace with generic "Downstream Actions" section with type-specific variants | Option (a): simpler change, preserves existing research synthesis content | GAP-009 |
| DEC008 | Linking chain scope statement | (a) State in guideline §III: T104-IG-002 applies to research synthesis only, with explicit scoping sentence; (b) reference T104-IG-002 globally without type scoping | Option (a): explicit scoping sentence avoids misapplication to non-research types | GAP-010 |

---

## IX. References

| Document | Path |
|:--|:--|
| ST005 Stream Plan | `prompt/artifacts/tasks/T104/workspace/PH001/ST005/plan_T104-PH001-ST005.md` |
| P-AC006 Pre-Promotion Audit | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC006/analysis/analysis_P-PH000-ST001-AC006_pre-promotion-audit.md` |
| P-AC007 P-STD-005 Hardening Assessment | `prompt/artifacts/tasks/P/workspace/PH000/ST001/analysis/analysis_P-PH000-ST001-AC007_p-std-005-hardening-assessment.md` |
| T104-ST002-AC000 External Review | `prompt/artifacts/tasks/T104/workspace/PH001/ST002/AC000/analysis/analysis_T104-PH001-ST002-AC000_external-review.md` |
| T104-ST001-AC002-TK005 Cross-Reference Compliance | `prompt/artifacts/tasks/T104/workspace/PH001/ST001/AC002/analysis/analysis_T104-PH001-ST001-AC002-TK005_cross-reference-compliance.md` |
| Existing Analysis Template | `prompt/templates/consultant/workspace/template_workspace_analysis.md` |
| Verification Guideline | `prompt/templates/consultant/workspace/guideline_workspace_verification.md` |
| Workspace Documentation Rules | `prompt/templates/consultant/workspace/workspace_documentation_rules.md` |
| T104 SPS (T104-IG-002 source) | `prompt/artifacts/tasks/T104/ssot/sps_T104-CWS.md` |
| T102-STD-006 Research Artifacts Index | `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-006_research-artifacts-index.md` |
| AC005 Pattern Audit (structural precedent) | `prompt/artifacts/tasks/T104/workspace/PH001/ST005/analysis/analysis_T104-PH001-ST005-AC005_verification-pattern-audit.md` |
| P-STD-004 File Naming & Directory Convention | `prompt/artifacts/tasks/P/standard/standard_P-STD-004_file-naming-and-directory-convention.md` |

---

## X. Changelog

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| 1.0.0 | 2026-02-28 | Initial | Draft 1. TK001 audit of 4 analysis exemplars + existing template. 10 gaps identified. Guideline/template blueprints and cross-check targets produced as TK002–TK004 inputs. Design decisions register populated as placeholder pending TK001.1 Socratic consultation. |

