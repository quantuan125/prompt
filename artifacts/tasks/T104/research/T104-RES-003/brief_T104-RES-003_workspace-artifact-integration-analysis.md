---
artifact_type: 'RESEARCH_BRIEF'
initiative_id: 'T104'
initiative_code: 'CWS'
research_id: 'T104-RES-003'
title: 'Workspace Artifact Integration & Industry Benchmark Analysis'
version: '1.1.0'
iteration: '2'
date: '2026-03-13'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
parent_plan: 'prompt/artifacts/tasks/T104/workspace/PH001/ST008/plan_T104-PH001-ST008.md'
activity_reference: 'T104-PH001-ST008-AC002'
report_template: 'prompt/templates/researcher/template_research_report.md'
governance_rules: 'prompt/templates/consultant/workspace/workspace_documentation_rules.md'
---

# RESEARCH BRIEF: Workspace Artifact Integration & Industry Benchmark Analysis (T104-RES-003)

## I. EXECUTIVE SUMMARY

**Context**: T104 Phase 1 Stream ST008 (Vertical Guideline Integration & Documentation Rules Alignment) now needs a research commission that evaluates the consultant workspace from two equally important lenses: traditional SE/PM artifact-governance practice and LLM-agentic workspace operating patterns. ST005 produced Draft 1 guidelines and templates for 7 artifact types (PLAN, ROADMAP, NOTES, VERIFICATION, DEV-REPORT, ANALYSIS, PROPOSAL) through horizontal development — each developed independently. AC001 resolved one major cross-cutting inconsistency (GDR ownership), demonstrating that horizontal-only development creates integration gaps that must be systematically identified and resolved before the documentation rules can be finalized. Prior research `T104-RES-001` and the T104 SPS also establish deterministic retrieval and agentic automation as first-class initiative concerns, so this commission must not treat agentic considerations as a minor overlay.

**Objective**: Produce a research report that:
1. Benchmarks the T104 artifact inventory (7 in-scope types mapped to epics T104A, T104B, T104C, T104D, T104F, T104H, T104I) against both: (a) established SE/PM artifact-governance patterns, and (b) LLM-agentic workspace patterns for retrieval, context transfer, and multi-agent handoff.
2. Performs a detailed vertical integration audit across all 7 guideline files and their associated templates, identifying cross-cutting inconsistencies, role boundary contradictions, gate semantics misalignment, and cross-reference integrity failures.
3. Assesses SPS requirement coverage — mapping every SPS requirement (CON, QG, DEP, IF, STD, IG) to guideline coverage and identifying uncovered or ambiguously covered requirements.
4. Synthesizes findings into a high-level integration model suitable for incorporation into `workspace_documentation_rules.md`, explicitly reconciling traditional governance needs with agent-oriented retrievability, parseability, and handoff requirements.

**Target Deliverable**: A research report consumed by `LLM_Consultant` to:
- Provide the gap register required by AC002 success criteria (all 7 guideline files + all template files covered).
- Map each gap to a downstream action target and responsible role (seeding AC003 task register).
- Deliver industry-grounded recommendations for artifact workflow integration patterns across both traditional and agentic operating models.
- Produce an integration model draft for `workspace_documentation_rules.md` alignment in AC004.

**Scope Exclusions**: T104E (CHANGELOG Standardization) and T104G (COMMUNICATION Standardization) are explicitly **out of scope** for this research. Neither has Draft 1 guidelines or templates, and both are accepted as not requiring development at this stage.

---

## II. RESEARCH SCOPE & TOPICS

### Part A: Dual-Lens Benchmarking & Comparative Analysis

**Part A balance requirement**: Traditional SE/PM benchmarking and LLM-agentic benchmarking MUST receive materially comparable treatment. Part A is not complete if agentic analysis appears only as a sub-question or single rubric row.

#### Topic 1: SE Workspace Artifact Taxonomy Benchmark (Critical)
**Objective**: Benchmark the T104 artifact inventory (7 in-scope types) against both traditional SE/PM artifact taxonomies and agentic workspace taxonomies to validate coverage, identify gaps, and assess whether T104 is coherent for both human-governed and agent-consumable workflows.
**Context**: T104 defines 7 artifact types for the consultant workspace: PLAN, ROADMAP, NOTES, ANALYSIS, PROPOSAL, VERIFICATION, DEV-REPORT. Each is mapped to a dedicated epic (T104A/B/C/D/F/H/I). The research must now answer two questions in parallel: whether this set is a coherent consultancy workspace by traditional standards, and whether it is a coherent workspace for deterministic agent retrieval, parsing, and coordination.
**Specific Questions**:
* Traditional Track 1: How do T104's 7 artifact types map to structured PM/governance artifact families (for example PRINCE2 and PMBOK-style management/lifecycle products)?
* Traditional Track 2: How do T104's 7 artifact types map to SE discovery/define and decision-record artifact families (for example PRD/BRD/SRS/design/RFC/ADR-style surfaces)?
* Agentic Track 1: Which T104 artifact types behave as deterministic retrieval surfaces, context packaging surfaces, or machine-consumable navigation spines for LLM agents?
* Agentic Track 2: Which artifact types are missing, overloaded, or poorly separated when evaluated as context-bearing handoff surfaces between multiple agents?
* Are there standard traditional or agentic workspace artifact types that T104 does not yet cover? If so, are they genuine future-epic candidates or better handled as conventions inside the existing 7 types?
* Are any T104 artifact types redundant with each other or with artifacts already governed by other initiatives (T102 SSOT artifacts: SPS, Request, Concept)?
**Deliverable**: Three outputs: (1) a traditional benchmark matrix, (2) an agentic benchmark matrix, and (3) a reconciliation note identifying where the two taxonomies agree, diverge, or require T104-specific tradeoffs.

#### Topic 2: Artifact Lifecycle & Workflow Patterns (Critical)
**Objective**: Research lifecycle models for each T104 artifact type across both human governance workflows and agentic operating workflows: how artifacts are created, authored, reviewed, approved, consumed, resumed, and retired.
**Context**: T104's current guidelines define individual artifact structures but do not yet codify the full end-to-end lifecycle from either a traditional governance perspective or an LLM-agent perspective. The revised research must therefore compare human-governed lifecycle expectations with agent-facing lifecycle expectations such as context packaging, resumability, and state recovery.
**Specific Questions**:
* Traditional Track 1: What are the recognized lifecycle stages for SE governance artifacts (for example Draft → Review → Approved → Active → Superseded → Archived)?
* Traditional Track 2: How do established frameworks define authoring ownership vs review ownership vs approval ownership for each artifact type?
* Agentic Track 1: What lifecycle states matter for agent-consumable artifacts (for example discoverable, loadable, current, superseded, resumable, archived)?
* Agentic Track 2: What context payload, metadata, and structural requirements are needed for an artifact to survive partial-context recovery, reassignment to another agent, or reuse in later sessions?
* Where do traditional artifact retirement criteria diverge from agentic retention/retrieval needs?
**Deliverable**: Two lifecycle models per artifact type: (1) traditional governance lifecycle and (2) agentic consumption lifecycle, followed by a reconciliation commentary for T104.

#### Topic 3: Cross-Artifact Integration & Handoff Patterns (High)
**Objective**: Compare how handoff chains, dependency relationships, and integration patterns work in traditional consultancy workflows versus LLM-agentic workflows, then define what T104 should codify as a hybrid model.
**Context**: T104 has an implicit artifact chain (for example PLAN defines work → DEV-REPORT logs execution → VERIFICATION validates → PROPOSAL packages for approval), but that chain is not formally defined in one place. The revised research must also examine how context handoff between agents changes the requirements for link surfaces, metadata, ownership boundaries, and restart behavior.
**Specific Questions**:
* Traditional Track 1: How do industry frameworks define inter-artifact dependency types (for example triggers, inputs, outputs, validation gates)?
* Traditional Track 2: What are the standard handoff patterns for plan → execution → verification → approval chains, including parallel workstreams?
* Agentic Track 1: How should context handoff between agents be modeled when different artifact types serve as navigation, working-state, validation, or approval surfaces?
* Agentic Track 2: What makes a handoff deterministic enough for another agent to resume work without hidden assumptions, stale context, or duplicated reasoning?
* Reconciliation: Where should T104 intentionally preserve human-oriented artifact behavior, and where should it optimize for agentic parseability, resumability, and drift resistance?
**Deliverable**: An integration pattern catalogue with both traditional and agentic handoff patterns, plus a reconciliation matrix: Pattern Family x Source Artifact x Target Artifact x Trigger Condition x Handoff Contract x T104 Implication.

### Part B: Internal Vertical Integration Audit

#### Topic 4: Cross-Reference & Linkage Integrity Audit (Critical)
**Objective**: Systematically audit all 7 guideline files and their associated templates for cross-reference accuracy — paths, section anchors, ID citations, and inter-guideline handoff definitions.
**Context**: Each guideline was developed independently in ST005 (horizontal development). AC001 already discovered one major cross-cutting issue (GDR normative duplication). The remaining guidelines have not been verified for cross-reference integrity. DEC014 from AC008 introduced inter-guideline handoff patterns that may not be consistently reflected across all guidelines.
**Specific Questions**:
* For each guideline: do all cross-references to other guidelines resolve to correct paths and section anchors?
* Are inter-guideline handoff definitions (e.g., plan guideline referencing verification guideline for gate execution) consistent in both directions?
* Do guidelines reference templates using correct, current paths?
* Are ID citations (e.g., `T104-CON-001`, `T102-STD-003`) used consistently and correctly across all guidelines?
* Post-AC001: are all references to GDR, gate semantics, and verification/proposal boundaries updated consistently across all 7 guidelines?
* Does `workspace_documentation_rules.md` accurately reflect the current state of all guideline cross-references?
**Deliverable**: A cross-reference integrity matrix: Source Guideline x Referenced Target x Reference Type (path/anchor/ID) x Resolution Status (OK/BROKEN/STALE/MISSING).

#### Topic 5: Role Boundary & Gate Semantics Consistency Audit (Critical)
**Objective**: Audit role boundary definitions and gate/GDR semantics across all 7 guidelines for contradictions, gaps, or ambiguities — including validation of AC001 deliverables' integration.
**Context**: `workspace_documentation_rules.md` §6 defines high-level role boundaries (Consultant, Planner, Developer, Reviewer, Client). Each guideline may add role-specific rules within its domain. AC001 resolved GDR ownership (moving to proposal guideline), but the downstream effects on how each guideline references gates, verdicts, and reviewer boundaries need verification. `T104-DEP-006 (T102 Role Catalog)` establishes that role definitions must align with the T102 catalog.
**Specific Questions**:
* Does each guideline consistently define which role(s) author, review, and approve artifacts of that type?
* Are there contradictions in role boundary definitions between guidelines (e.g., one guideline allows Developer to author analysis while another restricts it)?
* Are gate semantics (entry criteria, exit criteria, verdict taxonomy: PASS/FAIL/PASS WITH DEFERRALS) used consistently across guidelines that reference gates?
* Post-AC001: does the GDR ownership resolution (proposal guideline as sole normative source) reflect consistently in all guidelines that previously referenced GDR?
* Are Situation A (Deliverable Deficiency) and Situation B (Scope Gap) rework paths defined consistently between the plan guideline and verification guideline?
* Does the TK-before-gate pattern (reviewer produces verification task before client-owned gate) appear consistently in all guidelines that reference gates?
**Deliverable**: A role boundary consistency matrix: Guideline x Role x Defined Boundary x Conflicts with Other Guidelines. A gate semantics consistency register: Guideline x Gate Concept Referenced x Definition Used x Consistency Status.

#### Topic 6: Template-Guideline Conformance Audit (High)
**Objective**: Verify that each template structurally matches its governing guideline's section requirements — identifying mismatches, missing sections, orphaned template content, and guideline requirements not reflected in templates.
**Context**: Templates are the instantiation surface for guidelines. If a guideline requires section X but the template omits it, authors will inconsistently add or skip that section. Conversely, if a template contains sections not mentioned in the guideline, the section's purpose and governance are ambiguous. In the revised brief, conformance should also consider whether templates expose enough metadata and structural predictability for reliable agent consumption.
**Specific Questions**:
* For each guideline-template pair: does the template contain all sections required by the guideline?
* Does the template contain sections not mentioned or governed by the guideline?
* Are template YAML frontmatter fields consistent with guideline requirements?
* For artifact types with multiple templates (PLAN: 3 levels; NOTES: 6 templates; PROPOSAL: 4 archetypes): are the template variants consistent with each other and with the governing guideline?
* Does each template include correct governance rule references (pointing to its guideline and `workspace_documentation_rules.md`)?
* Do templates expose enough stable frontmatter, naming, and section predictability for deterministic agent parsing and retrieval?
**Deliverable**: A template-guideline conformance matrix: Guideline Section x Template Section x Conformance Status (MATCH/MISSING-IN-TEMPLATE/ORPHAN-IN-TEMPLATE/MISMATCH).

### Part C: Workflow Integration & Documentation Rules Alignment

#### Topic 7: SPS Requirement Coverage Assessment (Critical)
**Objective**: Map every SPS requirement item (CON, QG, DEP, IF, STD, IG from `sps_T104-CWS.md` Section III.B) to specific guideline coverage, identifying uncovered requirements and requirements with ambiguous or partial coverage.
**Context**: The SPS defines initiative-level requirements that the guideline suite must collectively satisfy. No systematic mapping currently exists between SPS requirements and guideline implementations. `workspace_documentation_rules.md` is intended to serve as the integration surface that bridges SPS requirements to guideline implementations, but its current state (v2.6.0) predates several guideline deliveries and AC001 changes.
**Specific Questions**:
* For each SPS constraint (T104-CON-001 through T104-CON-005): which guideline(s) implement or enforce this constraint? Is enforcement explicit or implicit?
* For each SPS quality goal (T104-QG-001 through T104-QG-005): which guideline(s) address this quality goal? Is coverage complete or partial?
* For each SPS dependency (T104-DEP-001 through T104-DEP-006): which guideline(s) reflect this dependency? Are cross-references accurate?
* For each SPS interface (T104-IF-001 through T104-IF-005): which guideline(s) implement this interface? Is the implementation consistent with the SPS specification?
* For each SPS standard (T104-STD-001 through T104-STD-003): which guideline(s) align with this standard? Is alignment explicit?
* For each SPS implementation guidance (T104-IG-001, T104-IG-002): which guideline(s) operationalize this guidance?
* Are there SPS requirements with zero guideline coverage (genuine gaps)?
**Deliverable**: An SPS-to-guideline traceability matrix: SPS Requirement ID x Requirement Summary x Covering Guideline(s) x Coverage Type (Explicit/Implicit/Partial/None) x Gap Notes.

#### Topic 8: Documentation Rules Integration Model (Critical)
**Objective**: Synthesize findings from Topics 1–7 into a high-level integration model for `workspace_documentation_rules.md` that defines: complete artifact type inventory (all 7 in-scope types), workflow chains between artifact types, role-to-artifact ownership matrix, and inter-artifact linkage rules — suitable for initiative-level governance with detail deferred to respective epic development.
**Context**: `workspace_documentation_rules.md` (v2.6.0) currently defines §3 (Artifact Type Inventory), §5 (Guideline Inventory), §6 (Role Boundary Rules), and §8 (Anti-Drift Rules). However, it lacks: a formal workflow chain definition showing how artifacts flow through the consultancy lifecycle, an explicit role-to-artifact ownership matrix beyond prose boundaries, inter-artifact linkage rules beyond the general "Link Don't Duplicate" principle, and explicit agent-oriented rules for context packaging and deterministic consumption. The AC004 activity will use this integration model to consolidate the documentation rules with SPS alignment.
**Specific Questions**:
* Based on industry benchmarks (Topics 1–3) and internal audit findings (Topics 4–6): what is the recommended high-level workflow chain for the 7 in-scope artifact types?
* What is the recommended role-to-artifact ownership matrix (Author / Reviewer / Approver / Consumer per artifact type)?
* What inter-artifact linkage rules should `workspace_documentation_rules.md` codify at the initiative level (vs. deferring to individual guidelines)?
* What new sections or subsections should `workspace_documentation_rules.md` add to serve as the integration surface?
* Where should `workspace_documentation_rules.md` remain deliberately thin (pointer-only to guidelines) vs. where should it contain normative integration rules?
* How should the integration model accommodate DEV-REPORT (T104I) given its "dynamic/continuous development posture" per `T104I-IG-001`?
* What agent-oriented rules should be codified for context payloads, metadata sufficiency, retrieval predictability, and handoff boundaries?
**Deliverable**: A recommended integration model specification for `workspace_documentation_rules.md` including: proposed section structure, workflow chain diagram (textual), role-to-artifact matrix, inter-artifact linkage rule catalogue, explicit deferred-to-epic boundary markers, and agent-oriented operating rules.

---

## III. CONSTRAINTS, ASSUMPTIONS & METHODOLOGY

### A. Constraints
* **Scope boundary**: Only 7 artifact types are in scope (PLAN, ROADMAP, NOTES, ANALYSIS, PROPOSAL, VERIFICATION, DEV-REPORT). T104E (CHANGELOG) and T104G (COMMUNICATION) are explicitly excluded.
* **No SSOT modification**: This research produces a report only; it does not modify the SPS, guidelines, templates, or `workspace_documentation_rules.md`.
* **Candidate-only integration model**: The Topic 8 integration model is a recommendation for AC004 consumption, not a finalized specification.
* **Repo-first evidence**: All internal claims MUST cite specific repo files with repo-relative paths.
* **External grounding required**: External web research MUST be used for Part A topics (industry benchmarking). All "industry best practice" claims MUST be sourced with citations (framework name, edition/version, specific section/chapter where applicable). If external browsing is unavailable, state limitations explicitly.
* **Balanced benchmark requirement**: Part A MUST treat traditional and agentic benchmarking as co-equal lenses. Agentic analysis MUST NOT be collapsed into a single sub-question or isolated appendix.
* **AC001 post-condition**: All guidelines are assumed to reflect the AC001 deliverables (GDR ownership resolution). The research MUST verify this assumption in Topic 5.
* **Gap register completeness**: The gap register produced by this research MUST cover all 7 guideline files and all associated template files per AC002 success criteria.

### B. Assumptions
* AC001 (GDR Ownership Resolution & Gate Semantics Alignment) is completed and its deliverables are merged into the guideline files.
* DEV-REPORT guideline (`guideline_workspace_dev-report.md`) and template (`template_workspace_dev-report.md`) exist and are available for audit at their canonical paths under `prompt/templates/consultant/workspace/`.
* The SPS (`sps_T104-CWS.md` v1.1.0) represents the current authoritative requirement set for T104.
* T102 standards adopted by T104 (per `T104-DEP-001`) represent stable external dependencies.
* `T104-RES-001` is a mandatory inherited context surface for the agentic half of this research, not optional background reading.
* `workspace_documentation_rules.md` v2.6.0 reflects all changes through AC001 but has not yet been updated for ST008 vertical integration findings.

### C. Methodology "Hierarchy of Truth"
If sources conflict, the report MUST:
1. Document the conflict.
2. Explain tradeoffs.
3. Recommend a resolution (do not silently override).

Recommended precedence for this research:
1. **SPS (`sps_T104-CWS.md`)** — Canonical authority for initiative requirements.
2. **T102 adopted standards** (T102-STD-003/004/005/006/007/009) — Binding governance specifications.
3. **Guidelines** (individual guideline files) — Normative rules for each artifact type.
4. **Templates** (individual template files) — Instantiation surfaces governed by guidelines.
5. **`workspace_documentation_rules.md`** — Integration surface; may lag behind guideline updates.
6. **AC001 deliverables** — Most recent normative changes (GDR ownership resolution).
7. **Industry frameworks** (PMBOK, PRINCE2, SAFe, IEEE 12207, etc.) — External validation and gap identification.

### D. Evaluation Rubric (per T102-STD-006-CLAUSE-008)

This research commissions comparative evaluation in Part A (Topics 1–3). The following balanced rubric MUST be applied when comparing T104 artifact types against both traditional and agentic framework equivalents.

| Dimension | Weight (1–5) | Description |
|:--|:--|:--|
| Coverage Completeness | 4 | Traditional lens: does the artifact type cover the purpose and content expected by the closest SE/PM equivalent? |
| Governance / Role Clarity | 4 | Traditional lens: are authoring, review, and approval responsibilities clearly and unambiguously defined? |
| Workflow Traceability | 4 | Traditional lens: can the artifact be traced through creation, consumption, and retirement inside a governed workflow? |
| Scalability | 3 | Traditional lens: does the artifact pattern scale across initiatives of varying size and complexity? |
| Deterministic Retrievability | 4 | Agentic lens: can LLM agents locate and retrieve the artifact deterministically using predictable naming and placement? |
| Parseability / Metadata Discipline | 4 | Agentic lens: is the artifact structured and annotated clearly enough for reliable machine parsing and context loading? |
| Handoff Determinism | 4 | Agentic lens: does the artifact support explicit, low-ambiguity handoff between agents without hidden assumptions? |
| Recovery / Drift Control | 3 | Agentic lens: can work resume safely after interruption while resisting duplication, stale state, or semantic drift? |

**Rubric Application**: Research report MUST apply this rubric to all Topics 1–3 comparisons, producing both traditional weighted totals and agentic weighted totals per artifact type. The report MUST then reconcile those totals in a short commentary for each artifact type. The rubric is NOT applicable to Part B (internal audit) or Part C (synthesis) topics.

---

## IV. CROSS-TOPIC INTEGRATION
*Force the researcher to synthesize, not just list facts.*

* **Integration Question 1**: How do the industry benchmark findings (Topics 1–3) validate or challenge the internal audit findings (Topics 4–6)? Where industry patterns diverge from T104's current implementation, is the divergence intentional (by design) or accidental (a gap)?
* **Integration Question 2**: How does the SPS requirement coverage assessment (Topic 7) relate to the cross-reference integrity audit (Topic 4)? Are SPS requirement gaps caused by missing guideline coverage, or by guidelines that cover the requirement but fail to reference the SPS item?
* **Integration Question 3**: How should the integration model (Topic 8) prioritize gap resolution? Which gaps from Topics 4–6 are systemic (require model-level changes to `workspace_documentation_rules.md`) vs. localized (require individual guideline fixes only)?
* **Integration Question 4**: Where do traditional lifecycle models (Topic 2) and agentic handoff patterns (Topic 3) converge or diverge with T104's role model (Consultant/Planner/Developer/Reviewer/Client)?
* **Integration Question 5**: Which traditional governance norms should T104 preserve as-is, and which should be adapted because an LLM-agentic environment imposes different constraints on retrieval, context transfer, and resumability?
* **Gap Analysis**: What is the minimum set of changes needed to `workspace_documentation_rules.md` to serve as a coherent integration surface for all 7 artifact types — given both internal audit findings and industry benchmark insights?

---

## V. INPUT PACKET (CONTEXT MAP)

### A. Core Governance (SSOT)
* T104 SPS: `prompt/artifacts/tasks/T104/ssot/sps_T104-CWS.md`
* T102 SPS (cross-reference): `prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md`
* T102 Concept (cross-reference): `prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md`

### B. Integration Target
* Workspace Documentation Rules: `prompt/templates/consultant/workspace/workspace_documentation_rules.md`

### C. Guideline Files (Primary Audit Targets)
* PLAN: `prompt/templates/consultant/workspace/guideline_workspace_plan.md`
* ROADMAP: `prompt/templates/consultant/workspace/guideline_workspace_roadmap.md`
* NOTES: `prompt/templates/consultant/workspace/guideline_workspace_notes.md`
* ANALYSIS: `prompt/templates/consultant/workspace/guideline_workspace_analysis.md`
* PROPOSAL: `prompt/templates/consultant/workspace/guideline_workspace_proposal.md`
* VERIFICATION: `prompt/templates/consultant/workspace/guideline_workspace_verification.md`
* DEV-REPORT: `prompt/templates/consultant/workspace/guideline_workspace_dev-report.md`

### D. Template Files (Secondary Audit Targets)
* PLAN templates (3):
  - `prompt/templates/consultant/workspace/template_workspace_plan_phase.md`
  - `prompt/templates/consultant/workspace/template_workspace_plan_stream.md`
  - `prompt/templates/consultant/workspace/template_workspace_plan_activity.md`
* ROADMAP template: `prompt/templates/consultant/workspace/template_workspace_roadmap.md`
* NOTES templates (7):
  - `prompt/templates/consultant/workspace/template_workspace_notes_register_phase.md`
  - `prompt/templates/consultant/workspace/template_workspace_notes_register_stream.md`
  - `prompt/templates/consultant/workspace/template_workspace_notes_register_activity.md`
  - `prompt/templates/consultant/workspace/template_workspace_notes_session_phase.md`
  - `prompt/templates/consultant/workspace/template_workspace_notes_session_stream.md`
  - `prompt/templates/consultant/workspace/template_workspace_notes_session_activity.md`
  - `prompt/templates/consultant/workspace/template_workspace_notes.md` (legacy/deprecated)
* ANALYSIS template: `prompt/templates/consultant/workspace/template_workspace_analysis.md`
* PROPOSAL templates (5):
  - `prompt/templates/consultant/workspace/template_workspace_proposal_eid-workspace.md`
  - `prompt/templates/consultant/workspace/template_workspace_proposal_gate-disposition.md`
  - `prompt/templates/consultant/workspace/template_workspace_proposal_promotion-contract.md`
  - `prompt/templates/consultant/workspace/template_workspace_proposal_standards-input.md`
  - `prompt/templates/consultant/workspace/template_workspace_proposal.md` (legacy/deprecated)
* VERIFICATION template: `prompt/templates/consultant/workspace/template_workspace_verification.md`
* DEV-REPORT template: `prompt/templates/consultant/workspace/template_workspace_dev-report.md`

### E. AC001 Deliverables (Post-condition Verification)
* GDR Ownership Assessment: `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001/analysis/analysis_T104-PH001-ST008-AC001_gdr-ownership-assessment.md`
* Gate Disposition Package: `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001/proposal/proposal_T104-PH001-ST008-AC001-TK001_gir-disposition-package.md`
* AC001 Activity Plan: `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001/plan_T104-PH001-ST008-AC001.md`

### F. Prior Research
* **Mandatory inherited context for agentic lens**:
  - `prompt/artifacts/tasks/T104/research/T104-RES-001/brief_T104-RES-001_agentic-workspace-assessment.md`
  - `prompt/artifacts/tasks/T104/research/T104-RES-001/report_T104-RES-001_agentic-workspace-assessment.md`
* T104-RES-001 Brief: `prompt/artifacts/tasks/T104/research/T104-RES-001/brief_T104-RES-001_agentic-workspace-assessment.md`
* T104-RES-001 Report: `prompt/artifacts/tasks/T104/research/T104-RES-001/report_T104-RES-001_agentic-workspace-assessment.md`
* T104-RES-002 Brief: `prompt/artifacts/tasks/T104/research/T104-RES-002/brief_T104-RES-002_requirements-candidate-research.md`
* T104-RES-002 Report: `prompt/artifacts/tasks/T104/research/T104-RES-002/report_T104-RES-002_requirements-candidate-research.md`

### G. Planning Context
* ST008 Stream Plan: `prompt/artifacts/tasks/T104/workspace/PH001/ST008/plan_T104-PH001-ST008.md`
* ST005 Stream Plan: `prompt/artifacts/tasks/T104/workspace/PH001/ST005/plan_T104-PH001-ST005.md`
* Phase 1 Plan: `prompt/artifacts/tasks/T104/workspace/PH001/plan_T104-PH001.md`

### H. Standards & Governance
* T102-STD-006 (Research Artifacts Index): `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-006_research-artifacts-index.md`
* T102-STD-003 (Explicit Inheritance Model): `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-003_explicit-inheritance-model.md`
* T102-STD-005 (ID Specification): Load via `python3 prompt/skills/t102-adr-005-id-spec/scripts/print_t102_adr_005.py`
* Research Report Template: `prompt/templates/researcher/template_research_report.md`

### I. Anti-Patterns / Exclusions
* **IGNORE**: `archive/` directories — do not use archived materials as current truth.
* **IGNORE**: `template_workspace_notes.md` and `template_workspace_proposal.md` — legacy/deprecated templates; audit for redirect-only correctness, not content.
* **OUT OF SCOPE**: Any files related to T104E (CHANGELOG) or T104G (COMMUNICATION) epics.
* **DO NOT MODIFY**: Any file outside the research report output. This brief produces a report only.

---

## VI. DELIVERABLE FORMAT REQUIREMENTS

The research report MUST use the standard template located at:
> `prompt/templates/researcher/template_research_report.md`

**Specific Mapping Instructions for this Brief**:

1. **Section I (Exec Summary)**: MUST end with:
   - A gap register summary: total gaps identified, broken down by category (cross-reference / role boundary / gate semantics / template conformance / SPS coverage).
   - A dual-lens benchmark summary: key traditional alignment strengths, key agentic alignment strengths, key divergences, and recommended additions.

2. **Section III (Topic Findings)**: For each topic, include:
   - Internal evidence (file references with repo-relative paths).
   - External references (framework name, edition/version, specific section/chapter citations) for both traditional and agentic benchmark tracks where applicable.
   - Rubric scores (Part A topics only — per evaluation rubric in §III.D).
   - A practical recommendation tied to specific downstream actions (AC003 gap resolution or AC004 documentation rules updates).

3. **Gap Register (Part B synthesis)**: MUST use the following table format:
   | Gap ID | Category | Source Guideline | Target Guideline/Template | Description | Severity | Downstream Action | Responsible Role |
   |:--|:--|:--|:--|:--|:--|:--|:--|
   - Gap ID: Sequential `T104-RES-003-GAP-###`.
   - Category: One of `CROSS-REF`, `ROLE-BOUNDARY`, `GATE-SEMANTICS`, `TEMPLATE-CONFORMANCE`, `SPS-COVERAGE`, `AGENTIC-INTEGRATION`.
   - Severity: One of `Critical`, `High`, `Medium`, `Low`.
   - Downstream Action: Either `AC003` (individual guideline fix) or `AC004` (documentation rules integration).
   - Responsible Role: LLM_Consultant, LLM_Developer, or LLM_Reviewer.

4. **Industry Benchmark Scoring (Part A)**: MUST produce:
   - A traditional benchmark matrix with per-artifact-type traditional rubric scores and weighted totals.
   - An agentic benchmark matrix with per-artifact-type agentic rubric scores and weighted totals.
   - A reconciliation matrix: `Artifact Type x Traditional Recommendation x Agentic Recommendation x T104 Integration Implication x Downstream Action`.

5. **Integration Model (Topic 8)**: MUST include:
   - Proposed `workspace_documentation_rules.md` section structure (table of contents).
   - Textual workflow chain diagram showing artifact flow through consultancy lifecycle.
   - Role-to-artifact ownership matrix (Author / Reviewer / Approver / Consumer).
   - Inter-artifact linkage rule catalogue with explicit "codify here" vs. "defer to guideline" markers.
   - Agent-oriented operating rules covering metadata sufficiency, context payload expectations, retrieval predictability, and handoff boundaries.

6. **Completeness**: Do NOT delete empty sections. If a topic has no findings, explicitly state "None identified".

---

## VII. ISSUES & RISKS REGISTER (T102-STD-007)

The research report MUST include an "Issues & Risks" section that implements `T102-STD-007 (Issues & Risks Index)` exactly.

**Inherited from SPS (carry forward; update status if new evidence warrants)**:

**Issues**
<!-- GUIDANCE:
Status = `OPEN, IN-REVIEW, RESOLVED, BLOCKED, DEFERRED`,
priority = `Low, Medium, High`
-->
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Resolution Notes | Resolution Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `T104-ISSUE-001` | Governance Rules Misalignment | `workspace_documentation_rules.md` defines Plan/Proposal/Completion roles conflicting with T104 Roadmap/Notes/Changelog semantics | LLM_Consultant | `OPEN` | `High` | 2026-01-18 | — | — |
| `T104-ISSUE-002` | Notes Template Drift | Notes template uses LOG/Subphase semantics inconsistent with T104 initiative NOTES usage | LLM_Consultant | `OPEN` | `High` | 2026-01-18 | — | — |
| `T104-ISSUE-003` | Naming Inconsistency | Case and suffix drift across artifacts undermines deterministic retrieval | LLM_Consultant | `OPEN` | `Medium` | 2026-01-18 | — | — |
| `T104-ISSUE-004` | Missing Analysis Artifact | Analysis artifact coverage incomplete for research commissions; pattern needs standardization | LLM_Consultant | `IN-REVIEW` | `High` | 2026-01-18 | RES-001 has companion analysis; standardize expectation via `T104-IG-002` | — |

**Risks**
<!-- GUIDANCE:
Status = `OPEN, MONITORED, MITIGATED, ACCEPTED, CLOSED`,
priority = `Low, Medium, High`
-->
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Mitigation Notes | Mitigation Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `T104-RISK-001` | Duplication Drift | Drift via content duplication across workflow tool artifacts undermines single-source-of-truth | LLM_Consultant | `MONITORED` | `High` | 2026-01-18 | Mitigation: `T104-CON-001 (Link Don't Duplicate)` | — |
| `T104-RISK-002` | Hidden Gate Layer | Stream or subphase structures may be misused as hidden governance gates outside formal phase gate schema | LLM_Consultant | `MONITORED` | `Medium` | 2026-01-18 | Mitigation: `T104-STD-001` hierarchy clauses | — |
| `T104-RISK-003` | Retrieval Failures | Naming inconsistency causes agentic and human retrieval failures | LLM_Consultant | `MONITORED` | `Medium` | 2026-01-18 | Mitigation: `T104-CON-004 (Prefix Discipline)` and `T104-QG-001 (Deterministic Retrieval)` | — |

**New items**: The researcher MUST add any newly identified issues/risks using sequential numbering continuing from `T104-ISSUE-009` and `T104-RISK-008` (accounting for items added post-RES-001 in the SPS).

**ID Rules (T104 scope)**:
* IDs MUST use the scoped, sequential format: `T104-ISSUE-###` and `T104-RISK-###`.
* IDs MUST remain stable once created (no reuse, no renumbering).

---

## VIII. CRITICAL DEPENDENCIES (GOVERNANCE MAPPING)

Map research findings to the specific governance artifacts and activities they inform:

* **AC003 (Cross-Guideline Gap Resolution)**: Topics 4, 5, 6 gap register findings directly seed AC003 task register. Each gap with `Downstream Action = AC003` becomes a candidate AC003 task.
* **AC004 (Documentation Rules Consolidation & SPS Alignment)**: Topics 7, 8 findings define AC004 scope. The integration model (Topic 8) is the primary design input for `workspace_documentation_rules.md` rewrite.
* **`workspace_documentation_rules.md`**: Topic 8 integration model proposes new/updated sections for AC004 implementation.
* **Individual guidelines**: Topics 4, 5, 6 may identify guideline-specific fixes required before AC004 can finalize the integration surface.
* **SPS alignment**: Topic 7 traceability matrix identifies SPS requirements that lack guideline coverage — informing whether gaps should be addressed in AC003 (individual guidelines) or AC004 (documentation rules as integration surface).
* **Epic dossier enrichment**: Topics 1, 2, 3 industry benchmark findings may inform future epic-level development (T104A through T104I) by providing industry-grounded patterns and lifecycle models.

---

## IX. SUCCESS CRITERIA

* The gap register covers all 7 guideline files and all associated template files (per AC002 success criteria from stream plan).
* Each gap has a downstream action target (`AC003` or `AC004`) and a responsible role.
* Part A uses the locked curated 4-track benchmark model: 2 traditional tracks and 2 agentic tracks.
* Industry benchmarking covers both traditional and agentic sources with specific citations; agentic benchmarking is not relegated to a single sub-question or appendix.
* Per-artifact-type traditional weighted totals and agentic weighted totals are produced for all 7 artifact types using the §III.D evaluation rubric.
* The report produces all three required Part A outputs: traditional benchmark matrix, agentic benchmark matrix, and reconciliation matrix.
* The SPS-to-guideline traceability matrix covers all SPS requirement items (CON-001–005, QG-001–005, DEP-001–006, IF-001–005, STD-001–003, IG-001–002).
* Cross-reference integrity audit identifies all broken, stale, or missing references across the 7 guidelines.
* Role boundary audit identifies all contradictions or ambiguities in role definitions across guidelines.
* Post-AC001 verification confirms GDR ownership resolution is consistently reflected across all affected guidelines.
* The integration model (Topic 8) is actionable as direct input to AC004 without requiring additional research and includes explicit agent-oriented governance rules.
* New issues/risks are surfaced if identified (not suppressed), continuing sequential numbering from SPS registers.
* The report is structured per `template_research_report.md` with all sections populated or explicitly marked "None identified".
