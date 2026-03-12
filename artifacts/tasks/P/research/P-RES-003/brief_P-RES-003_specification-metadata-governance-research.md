---
artifact_type: 'BRIEF'
initiative_id: 'P'
research_id: 'P-RES-003'
version: '1.0.0'
iteration: '1'
date: '2026-03-12'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
---

# RESEARCH BRIEF: Specification Metadata Governance Research (P-RES-003)

## I. EXECUTIVE SUMMARY

**Context**: `P-STD-001` (Program Governance Standard) prescribes the canonical combined-file structure for standard-specification files (`## Specification` → `## Decision Record` → `## References` → `## Provenance`). However, P-STD-001 prescribes no normative subsection structure within `## References` or `## Provenance`, no YAML frontmatter schema for standard files, and no in-file version tracking mechanism. This has produced organic divergence across all four active P-STD standards: P-STD-001 uses a flat key-value Provenance table, P-STD-002 introduced `### Amendment History`, P-STD-004 added `### Seed Source` and `### Seed Decision Inputs`, and P-STD-005 developed `### Promotion` and `### Hardening` subsections — each improvised independently. None of the four P-STD files carry YAML frontmatter, despite workspace artifacts (plans, briefs, guidelines) consistently including it. Formal research is commissioned to produce an externally sourced evidence base grounding new P-STD-001 CLAUSEs that standardize specification document metadata governance.
An immediate governance tension also exists in `sps_P-PROGRAM.md`: `P-CON-003` already states that combined standard-specification files SHALL use YAML frontmatter, but no active P-STD standard file currently implements that requirement and no P-STD-001 CLAUSE defines the governing schema or authority model. The research must therefore benchmark best practice and determine whether SPS language should be retained as-is, clarified, or amended to align with the eventual P-STD-001 metadata governance model.

**Objective**: Produce a decision-ready research report benchmarking industry-standard specification metadata governance practices across 4 domains (frontmatter schemas, in-file version tracking, Provenance/References standardization, metadata delineation architecture) and deliver scored recommendations for each domain using a weighted evaluation rubric per `T102-STD-006-CLAUSE-008`.

**Target Deliverable**: Research report consumed by `P-PH000-ST001-AC009` (Harden P-STD-001). Consumer: LLM_Consultant.

## II. RESEARCH SCOPE & TOPICS

### Part A: Frontmatter Schema Governance (maps to new P-STD-001 CLAUSEs for YAML frontmatter)

#### Topic 1: Industry YAML/Frontmatter Metadata Schemas (Critical)
**Objective**: Benchmark how major standards bodies structure machine-readable metadata headers for specification documents.
**Context**: All four active P-STD standards lack YAML frontmatter, while workspace artifacts (plans, briefs, guidelines) consistently include YAML with `version`, `date`, `status`, `author` fields. No P-STD-001 CLAUSE prescribes YAML requirements for standard files. External benchmarking is needed to determine what fields are normative at the specification document level.
**Specific Questions**:
*   What metadata header schemas do W3C (Respec frontmatter), IETF RFC (RFC 7991 xml2rfc metadata / RFC header block), ISO (ISO Directives Part 2 document metadata), and IEEE PAR (Project Authorization Request metadata) use for specification documents?
*   What fields are universally present across these standards bodies (e.g., document ID, version, status, date, author)?
*   How do standards bodies distinguish between machine-parseable metadata (structured headers) and human-readable metadata (narrative preamble)?
*   What field validation rules or controlled vocabularies are applied to metadata fields (e.g., status enums, date formats)?
*   How should the findings inform the existing SPS requirement in `P-CON-003` that combined standard-specification files use YAML frontmatter, given the current absence of any implemented P-STD schema?
**Deliverable**: Comparative matrix of frontmatter schemas across all four standards bodies with field-by-field analysis. Scored comparison per evaluation rubric (Section III.D).

#### Topic 2: Mandatory vs Optional Field Taxonomies (High)
**Objective**: Evaluate how standards bodies categorize metadata fields by obligation level and lifecycle stage.
**Context**: Specification documents pass through lifecycle stages (draft, review, accepted, deprecated). Different fields may be required at different stages (e.g., `author` required at draft, `approval_date` required only at accepted). The program needs to understand whether P-STD-001 should prescribe lifecycle-stage-aware field requirements.
**Specific Questions**:
*   How do standards bodies define mandatory vs optional vs conditional metadata fields?
*   Do field requirements change by document lifecycle stage (e.g., working draft vs candidate recommendation vs final standard)?
*   What is the industry approach to extensibility — do schemas allow custom/additional fields beyond the normative set?
*   How do standards bodies handle metadata field deprecation when schema versions evolve?
**Deliverable**: Recommended field taxonomy with obligation levels and lifecycle-stage mapping.

### Part B: In-File Version Tracking (maps to new P-STD-001 CLAUSEs for version history)

#### Topic 3: Version Tracking Patterns (Critical)
**Objective**: Evaluate in-file version tracking mechanisms versus VCS-only approaches across standards bodies.
**Context**: P-STD-001, P-STD-004, and P-STD-005 have no in-file changelog. P-STD-002 organically introduced an informal `### Amendment History` under Provenance, but it is not governed by any CLAUSE. The question is whether in-file version tracking is a recognized standard practice or whether VCS (git) history is sufficient.
**Specific Questions**:
*   What in-file version tracking patterns do standards bodies use (changelog sections, amendment registers, revision history tables, errata sheets)?
*   How do standards bodies that use VCS (e.g., W3C with GitHub-hosted specs) reconcile in-file version history with commit history?
*   What schema/format do amendment registers typically follow (date, version, author, change type, description)?
*   What is the minimum viable version tracking mechanism for a small-scale specification ecosystem (4-6 active standards)?
**Deliverable**: Scored comparison of version tracking approaches (in-file changelog, amendment register, VCS-only, hybrid). Scored per evaluation rubric (Section III.D).

#### Topic 4: Semantic Versioning in Specification Governance (High)
**Objective**: Evaluate how standards bodies version specification documents and what triggers version increments.
**Context**: The program currently uses semver-style versioning (`v1.0.0`, `v2.1.0`) on workspace artifacts but has no governed versioning convention for P-STD standard files. Standards bodies use diverse versioning models (semver, RFC sequential numbering, edition-based, dated snapshots).
**Specific Questions**:
*   What versioning models do W3C, IETF, ISO, and IEEE use for specification documents?
*   What events trigger version increments in each model (editorial fix, normative change, structural reorganization)?
*   How do standards bodies distinguish between editorial/non-normative changes and substantive/normative changes in version numbering?
*   Is semver appropriate for specification documents, or do standards bodies prefer alternative models?
**Deliverable**: Recommended versioning model with increment trigger definitions and trade-off analysis.

### Part C: Provenance & References Standardization (maps to P-STD-001 CLAUSE hardening for existing sections)

#### Topic 5: Provenance Subsection Taxonomy (Critical)
**Objective**: Evaluate what subsection categories within a specification's provenance/history section are normative across standards bodies, and whether companion authoring documents prescribe this structure.
**Context**: The four active P-STD standards each invented their own `## Provenance` subsection pattern: P-STD-001 uses a flat key-value table; P-STD-002 uses Status + Amendment History + Activity Plan; P-STD-004 uses Status + Seed Source + Activity Plan + Seed Decision Inputs; P-STD-005 uses Promotion + Input Sources + Hardening. The template (`template_standard_specs.md`) prescribes only `## Provenance` with a placeholder dash — no subsection structure is defined. This is the root cause of observed drift.
**Specific Questions**:
*   What provenance/history subsection categories do standards bodies define as normative (e.g., status, authority/ownership, amendment history, input sources, supersession chain)?
*   How do standards bodies handle lifecycle-variant provenance (e.g., a promoted standard vs a seed-based standard vs a hardened standard) — is there a single normative schema that accommodates all lifecycle patterns, or do different document types have different provenance requirements?
*   What is the minimum normative set of provenance subsections that a meta-standard should prescribe?
*   Do standards bodies prescribe provenance/history subsection structure in their companion authoring guides (e.g., W3C Process Document, IETF RFC 7322 "RFC Style Guide", ISO Directives Part 2)? If so, how prescriptively?
**Deliverable**: Recommended normative Provenance subsection taxonomy that accommodates all observed lifecycle patterns (seed-based, promotion-based, hardening-based). Scored comparison per evaluation rubric (Section III.D).

#### Topic 6: References Section Standardization (High)
**Objective**: Evaluate how standards bodies categorize and structure references within specification documents.
**Context**: P-STD-001 uses `### References (Internal + Cross-Scope: Program → Initiative T102)` — a unique heading. P-STD-002, P-STD-004, and P-STD-005 converged on `### External References (Cross-Scope)`. P-STD-001-CLAUSE-001 prescribes only `## References` at the top level without governing internal structure. Industry standards bodies have established reference categorization patterns (e.g., IETF's "Normative References" / "Informative References" split).
**Specific Questions**:
*   What reference categorization taxonomies do standards bodies use (normative vs informative, internal vs external, mandatory vs optional)?
*   How do IETF (RFC 7322), W3C (Respec), and ISO (ISO Directives Part 2) structure their reference sections?
*   What table schemas or list formats are standard for reference entries (ID, title, scope, path/URL, reference type)?
*   Should a meta-standard prescribe reference subsection headings, or is a single flat references section sufficient?
**Deliverable**: Recommended References section structure with categorization taxonomy. Scored comparison per evaluation rubric (Section III.D).

#### Topic 7: Cross-Artifact Traceability Metadata (High)
**Objective**: Evaluate how standards bodies embed traceability links to governing decisions, parent documents, and derivative artifacts within specification metadata.
**Context**: P-STD standards currently embed traceability in diverse ways — P-STD-001 has `Promotion Contract` and `Promotion Decision` fields in Provenance; P-STD-005 has `### Input Sources` and `### Hardening` with activity/gate references. No normative pattern exists for what traceability metadata belongs in a specification versus what belongs in external governance artifacts.
**Specific Questions**:
*   How do standards bodies link specifications to their governing decisions (e.g., W3C Director's decisions, IETF IESG approval, ISO ballot results)?
*   What traceability metadata do standards bodies embed within specifications versus track externally (e.g., in separate process documents)?
*   How are authority chains (parent standard → child standard → derivative guideline) represented in metadata?
*   What is the recommended boundary between traceability metadata (belongs in the spec) and governance process artifacts (belongs elsewhere)?
**Deliverable**: Recommended traceability metadata pattern with boundary definition for in-spec vs external tracking.

### Part D: Metadata Delineation Architecture (cross-cutting — synthesis)

#### Topic 8: Machine-Readable vs Human-Readable Delineation (Critical)
**Objective**: Evaluate how standards bodies resolve the overlap between machine-readable metadata (YAML frontmatter) and human-readable metadata (Provenance narrative), and define authoritative source rules.
**Context**: If P-STD standards adopt YAML frontmatter (e.g., `version: '1.2.0'`, `status: 'accepted'`) and also maintain a `## Provenance` section with version/status narrative, there is a potential for duplication, drift, and authority ambiguity. The program needs a clear delineation architecture that defines what belongs in each layer and which is authoritative when they overlap.
**Specific Questions**:
*   How do standards bodies that use both structured metadata headers and narrative preambles handle the overlap (e.g., W3C Respec with both JSON metadata and rendered header block)?
*   What are the industry patterns for "single source of truth" metadata — is the machine-readable header authoritative, with narrative derived from it, or vice versa?
*   What fields typically appear in both layers, and how is consistency enforced (derivation rules, linting, manual discipline)?
*   What is the recommended delineation for a Markdown-primary, git-versioned ecosystem: which fields belong in YAML frontmatter (machine-readable current state) versus Provenance (human-readable history trail)?
**Deliverable**: Recommended metadata delineation architecture with field-by-field placement rules, authority hierarchy, and consistency enforcement mechanism. Scored comparison per evaluation rubric (Section III.D).

#### Topic 9: Benchmark Current P-STD-001..005 State (High)
**Objective**: Audit the existing metadata state of all active P-STD standard files against the research findings from Topics 1–8, producing a per-file gap matrix.
**Context**: The research must not only identify industry best practices but also measure the distance between current state and recommended state. This topic directly produces the gap matrix that `P-PH000-ST001-AC009` (Harden P-STD-001) will consume to scope its CLAUSE drafting work.
**Specific Questions**:
*   For each of P-STD-001, P-STD-002, P-STD-004, and P-STD-005: what is the current metadata state across all four domains (frontmatter, version tracking, Provenance structure, References structure)?
*   Where does each file conform to or diverge from the recommended patterns identified in Topics 1–8?
*   What is the estimated structural change magnitude per file (minor amendment vs significant restructuring)?
*   Are there any existing patterns in the current P-STDs that are *better* than industry standard practice and should be preserved?
**Deliverable**: Per-file gap matrix with conformance assessment, divergence catalogue, and change magnitude estimate. Not scored — this is an audit topic, not a comparative evaluation.

---

## III. CONSTRAINTS, ASSUMPTIONS & METHODOLOGY

### A. Constraints
*   **Boundary**: Research is recommendations-only. No P-STD-001 CLAUSE text drafting. No structural changes to any P-STD file. No template/guideline file updates.
*   **Scope**: Forward-looking only — P-STD standard files as the subject. Legacy T102-STD metadata patterns are excluded from scope per `P-PH000-ST001-SES002-OQ002` resolution (migration context is documented in existing promotion contract artifacts and does not require external research).
*   **Retrofit Boundary**: The research produces "what should it look like" recommendations. Retrofit implementation (applying changes to P-STD files, template, guideline) is `P-PH000-ST001-AC009` (Harden P-STD-001) and `P-PH000-ST001-AC010` (Cross-Standard Conformance) scope.
*   **Output**: Research report per `prompt/templates/researcher/template_research_report.md`.
*   **Benchmark Set Lock**: The comparative benchmark set is fixed to W3C, IETF RFC, ISO, and IEEE PAR per `P-PH000-ST004-AC003-SES001-DEC002`. Supporting IEEE process/style documents MAY be cited as evidence, but the benchmark target remains IEEE PAR metadata governance.

### B. Assumptions
*   **P-STD-001 as Meta-Standard**: P-STD-001 is the governing authority for all specification metadata governance decisions. New CLAUSEs produced from this research will be authored into P-STD-001 as the normative surface.
*   **Markdown-Primary Ecosystem**: The program operates in a Markdown-primary, git-versioned, repo-native ecosystem. Recommendations must be practically implementable within this constraint.
*   **Four Active Standards**: P-STD-001, P-STD-002, P-STD-004, and P-STD-005 are the active standard files in scope. P-STD-003 is a deprecated placeholder and is excluded per `P-PH000-ST001-SES002-DEC001`.
*   **Template/Guideline Derivative Chain**: Any new P-STD-001 CLAUSEs will require conformance updates to `guideline_standard_specs.md` and `template_standard_specs.md` per `P-STD-001-CLAUSE-005 (Authority Derivation & Conformance Coupling)`. The research MAY recommend template/guideline structural changes as part of integration recommendations, but authoring those changes is AC009/AC010 scope.

### C. Methodology "Hierarchy of Truth"
1.  **External Standards Body Documentation** (W3C Process Document / Respec, IETF RFC 7991 / RFC 7322, ISO Directives Part 2, IEEE PAR materials, and supporting IEEE SA style/process documentation where needed) — Benchmarking Authority
2.  **Program SSOT Files** (`sps_P-PROGRAM.md` constraints, accepted standards, P-STD-001 current CLAUSEs) — Governance Context
3.  **Current P-STD File State** (P-STD-001..005 actual metadata structures) — Audit Subject
4.  **Session Transcripts / Planning Documents** — Traceability Context Only; No Normative Authority

### D. Evaluation Rubric (per `T102-STD-006-CLAUSE-008`)

All topics requiring comparative evaluation MUST apply the following weighted rubric:

| Dimension | Weight (1-5) | Description |
|:--|:--|:--|
| Program Fit | 5 | Aligns with the P governance model: multi-standard (4+ STDs), multi-role (Consultant/Planner/Developer/Reviewer), Markdown-primary, git-versioned ecosystem |
| Industry Alignment | 5 | Established practice in recognized standards bodies (W3C, IETF, ISO, IEEE) with documented specification governance |
| Agentic Operability | 4 | Machine-parseable metadata enabling deterministic LLM agentic workflows; supports automated field extraction, validation, and consistency checking |
| Adoption Overhead | 4 | Retrofit cost across 4 active P-STDs + template + guideline; migration complexity and process burden (lower overhead = higher score) |
| Extensibility | 2 | Supports future growth (additional standards, Phase 2 features, cross-initiative conformance) without schema rework |

Per-option scores MUST use a 1-5 scale for each dimension. Weighted totals MUST be computed and presented.

---

## IV. CROSS-TOPIC INTEGRATION
*Force the researcher to synthesize, not just list facts.*
*   **Integration 1 (Frontmatter ↔ Provenance Delineation)**: How do Topic 1 findings (frontmatter schemas) interact with Topic 8 findings (metadata delineation)? Which fields belong in YAML frontmatter vs Provenance narrative, and what is the authority hierarchy when both contain overlapping data (e.g., version, status)?
*   **Integration 2 (Version Tracking ↔ Provenance Placement)**: How does Topic 3 (version tracking patterns) interact with Topic 5 (Provenance subsection taxonomy)? Should the amendment history/changelog be a subsection of Provenance, a standalone section, or a YAML frontmatter array?
*   **Integration 3 (References ↔ Traceability)**: How does Topic 6 (references categorization) interact with Topic 7 (cross-artifact traceability)? Are governance decision links (authority chain, supersession) part of the References section, the Provenance section, or both?
*   **Integration 4 (SPS Constraint Alignment)**: How should Topic 1 (frontmatter schemas) and Topic 8 (metadata delineation) findings reconcile with `sps_P-PROGRAM.md` `P-CON-003`, which already requires YAML frontmatter for combined standard-specification files?
*   **Gap Analysis**: What metadata governance patterns are standard across W3C, IETF, ISO, and IEEE that the current P-STD ecosystem completely lacks? Identify specific gaps per domain (frontmatter, versioning, Provenance, References) and map each to a target P-STD-001 CLAUSE domain.

---

## V. INPUT PACKET (CONTEXT MAP)

### A. Core Governance
*   SSOT: `prompt/artifacts/tasks/P/ssot/sps_P-PROGRAM.md`
*   Plan (research stream): `prompt/artifacts/tasks/P/workspace/PH000/ST004/plan_P-PH000-ST004.md`
*   Plan (consumer activity): `prompt/artifacts/tasks/P/workspace/PH000/ST001/plan_P-PH000-ST001.md` (AC009 contract)
*   Authoring authority: `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md`
*   SPS constraint to reconcile: `prompt/artifacts/tasks/P/ssot/sps_P-PROGRAM.md` `P-CON-003` (combined standard-specification files SHALL use YAML frontmatter)

### B. Audit Subject Files (Current State)
*   `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md` — P-STD-001 (meta-standard; subject of hardening)
*   `prompt/artifacts/tasks/P/standard/standard_P-STD-002_program-status-standard.md` — P-STD-002 (evolved Provenance pattern: Status + Amendment History + Activity Plan)
*   `prompt/artifacts/tasks/P/standard/standard_P-STD-004_file-naming-and-directory-convention.md` — P-STD-004 (evolved Provenance pattern: Status + Seed Source + Activity Plan + Seed Decision Inputs)
*   `prompt/artifacts/tasks/P/standard/standard_P-STD-005_universal-id-specification.md` — P-STD-005 (evolved Provenance pattern: Promotion + Input Sources + Hardening)

### C. Derivative Files (Template/Guideline — Current State)
*   `prompt/templates/consultant/standards/guideline_standard_specs.md` — Current guideline (derivative of P-STD-001; prescribes no Provenance/References subsection structure)
*   `prompt/templates/consultant/standards/template_standard_specs.md` — Current template (derivative of P-STD-001; `## Provenance` is placeholder dash only)

### D. Standards & Templates
*   `prompt/artifacts/tasks/T102/standard/standard_T102-STD-006_research-artifacts-index.md` — Research commissioning standard
*   `prompt/artifacts/tasks/T102/standard/standard_T102-STD-007_issues-risks-index.md` — Issues & Risks register standard
*   `prompt/templates/researcher/template_research_report.md` — Report template

### E. Consultation Evidence
*   `prompt/artifacts/tasks/P/workspace/PH000/ST001/snotes/snotes_P-PH000-ST001-SES002.md` — Origin of P-RES-003 scope, DEC002/DEC003 (research grounding requirement), OQ002 (scope boundary resolution)

### F. Anti-Patterns / Exclusions
*   **IGNORE**: `T102-STD-004` (superseded source of P-STD-001) legacy metadata patterns — excluded per OQ002 resolution; migration context is documented in existing promotion contract artifacts
*   **IGNORE**: `P-STD-003` — deprecated placeholder per `P-PH000-ST001-SES002-DEC001`
*   **IGNORE**: Session-scoped DEC tokens as normative constraints — they are traceability pointers only

---

## VI. DELIVERABLE FORMAT REQUIREMENTS

The research report MUST use the standard template located at:
> `prompt/templates/researcher/template_research_report.md`

**Specific Mapping Instructions for this Brief**:
1.  **Section I (Exec Summary)**: Must include a GO/NO-GO/PIVOT verdict on whether the current organic Provenance/References patterns should be standardized (expected: GO). Must list top 3 key findings across the four research domains.
2.  **Section III (Topic Findings)**:
    *   Each topic MUST include Evidence & Forensics (with external standards body citations), Analysis (synthesis + gap analysis), and Governance Implication (P-STD-001 CLAUSE domain impact).
    *   Topics requiring comparative evaluation (Topics 1, 3, 5, 6, 8) MUST include scored comparison tables using the evaluation rubric from Section III.D.
    *   Topic 9 (Benchmark Current State) MUST produce a per-file gap matrix — not a scored comparison but a conformance audit.
3.  **Section V (Artifact Updates)**: Must map findings to P-STD-001 CLAUSE domains as an integration recommendations package, organized by target CLAUSE domain (see Section VIII).
    *   The package MUST explicitly state whether `sps_P-PROGRAM.md` `P-CON-003` should remain unchanged, be clarified, or be amended based on the research findings.
4.  **Completeness**: Do NOT delete empty sections. If a topic has no implications for a particular area, explicitly state "None".

---

## VII. ISSUES & RISKS REGISTER (T102-STD-007)

**Issues**

| ID | Title | Description | Owner | Status | Priority | Proposed Date | Resolution Notes | Resolution Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `P-RES-003-ISSUE-001` | ADR Index Inconsistency | ADR Index table (governed by `P-STD-001-CLAUSE-023`) is present in P-STD-001 and P-STD-005 but absent from P-STD-002 and P-STD-004. This is a Decision Record structural conformance issue, not a metadata governance issue — out of scope for P-RES-003 but flagged for AC009 hardening. | LLM_Consultant | DEFERRED | Medium | 2026-03-12 | Out of P-RES-003 scope; routed to AC009. | — |
| `P-RES-003-ISSUE-002` | SPS YAML Requirement Drift | `sps_P-PROGRAM.md` `P-CON-003` already requires YAML frontmatter for combined standard-specification files, but none of the active P-STD standard files implement YAML frontmatter and no P-STD-001 CLAUSE defines the required schema or authority model. Research output must determine whether this SPS requirement should be retained, clarified, or amended. | LLM_Consultant | OPEN | High | 2026-03-12 | To be resolved by P-RES-003 findings and routed into AC009 integration recommendations. | — |

**Risks**

| ID | Title | Description | Owner | Status | Priority | Proposed Date | Mitigation Notes | Mitigation Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `P-RES-003-RISK-001` | Retrofit Blast Radius | Normative metadata changes will require updates to 4 P-STD files + template + guideline + potentially SPS. If recommendations are too prescriptive, adoption overhead may delay AC009/AC010. | LLM_Consultant | OPEN | High | 2026-03-12 | Evaluation rubric weights Adoption Overhead at 4/5 to bias recommendations toward implementable patterns. Retrofit implementation is explicitly scoped to AC009/AC010, not P-RES-003. | — |
| `P-RES-003-RISK-002` | YAML-Provenance Authority Ambiguity | If both YAML frontmatter and Provenance narrative carry overlapping fields (version, status, date) without clear authority rules, this creates a new drift vector. | LLM_Consultant | OPEN | High | 2026-03-12 | Topic 8 (Metadata Delineation) directly addresses this with authority hierarchy recommendations. Integration 1 forces synthesis between Topics 1 and 8. | — |
| `P-RES-003-RISK-003` | Standards Body Practice May Not Scale Down | W3C, IETF, ISO, and IEEE operate at vastly larger scale than this program. Their metadata governance patterns may be over-engineered for a 4-6 standard ecosystem. | LLM_Consultant | OPEN | Medium | 2026-03-12 | Evaluation rubric weights Program Fit at 5/5 and Adoption Overhead at 4/5 to filter impractical recommendations. Topic 3 specifically asks for minimum viable version tracking for small-scale ecosystems. | — |

**ID Rules**
*   IDs MUST use the scoped, sequential format: `P-RES-003-ISSUE-###` and `P-RES-003-RISK-###`.
*   IDs MUST remain stable once created (no reuse, no renumbering).

---

## VIII. CRITICAL DEPENDENCIES (E-RID MAPPING)

*Map research findings to the specific governance artifacts they inform.*

*   **P-STD-001 (YAML Frontmatter — new CLAUSE domain)**: Topics 1-2 findings will define the normative YAML frontmatter schema for standard-specification files, including mandatory/optional field taxonomy and lifecycle-stage-aware requirements.
*   **P-STD-001 (Version Tracking — new CLAUSE domain)**: Topics 3-4 findings will define the in-file version tracking mechanism (format, placement, increment triggers) for standard-specification files.
*   **P-STD-001 (Provenance Structure — hardening of existing section)**: Topics 5, 7 findings will define the normative `## Provenance` subsection taxonomy, replacing the current placeholder-only prescription with a structured schema that accommodates all lifecycle patterns.
*   **P-STD-001 (References Structure — hardening of existing section)**: Topic 6 findings will define the normative `## References` subsection taxonomy, including reference categorization (normative vs informative, internal vs external).
*   **P-STD-001 (Metadata Delineation — new CLAUSE domain)**: Topic 8 findings will define the authority hierarchy and field placement rules between YAML frontmatter and Provenance narrative.
*   **sps_P-PROGRAM.md (`P-CON-003`)**: Topics 1 and 8 findings must explicitly assess whether the existing SPS YAML-frontmatter requirement remains valid as written or needs clarification/amendment to align with the finalized P-STD-001 governance model.
*   **guideline_standard_specs.md** (derivative): Integration recommendations will identify required conformance updates to the authoring guideline per `P-STD-001-CLAUSE-005 (Authority Derivation & Conformance Coupling)`.
*   **template_standard_specs.md** (derivative): Integration recommendations will identify required structural updates to the template to reflect new Provenance/References subsection schemas.

---

## IX. SUCCESS CRITERIA

*   All 9 topics addressed with findings supported by externally sourced evidence (standards body documentation citations required for Topics 1-8; Topic 9 uses internal audit evidence).
*   Evaluation rubric (Section III.D) applied consistently across all comparative topics (Topics 1, 3, 5, 6, 8) with scored comparison tables and weighted totals per `T102-STD-006-CLAUSE-008`.
*   Integration recommendations map each finding to at least one P-STD-001 CLAUSE domain (Frontmatter, Version Tracking, Provenance Structure, References Structure, Metadata Delineation).
*   Gap matrix (Topic 9) covers all four active P-STDs (P-STD-001, P-STD-002, P-STD-004, P-STD-005) with per-file conformance assessment.
*   Cross-topic integrations (Section IV) synthesized — not just listed facts but explicit delineation guidance for overlapping domains.
*   No P-STD-001 CLAUSE text drafted (recommendations-only boundary respected).
*   Retrofit implementation scoped to AC009/AC010, not embedded in research recommendations.
*   Issues and risks identified during research are registered per `T102-STD-007` schema.
