---
artifact_type: 'PROCEDURAL_GUIDELINE'
domain: 'consultant_workspace'
topic: 'analysis_authoring'
version: '1.7.0'
date: '2026-03-24'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
template_reference: 'prompt/templates/consultant/workspace/template_workspace_analysis.md'
decision_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST005/proposal/proposal_T104-PH001-ST005-AC007-TK001.1_gir-disposition-package.md'
plan_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST005/plan_T104-PH001-ST005.md'
---

# Analysis Procedural Guideline (Consultant Workspace)

## I. PURPOSE

Define authoring rules for **ANALYSIS** workspace artifacts so they are:
- consistent across analysis types,
- evidence-grounded and auditable,
- clearly separated from gate VERIFICATION semantics,
- compatible with program naming/placement authority (`P-STD-004`) and ID/reference rules (`P-STD-005`).

This guideline is Draft 1 (exemplar-derived). It is intended as the binding authoring rule set for consultant workspace analysis artifacts until superseded by a future analysis standardization epic.

---

## II. ROLE BOUNDARY (LOCKED)

- **LLM_Consultant** is the **sole author** of ANALYSIS artifacts.
- **LLM_Reviewer** authors VERIFICATION artifacts; verification findings are gate-oriented and may be blocking.
- **Client** is the decision owner for gates and proposal acceptance; client decisions are recorded in Gate Decision Records (GDRs) inside proposal artifacts where applicable.

**Boundary rule**: ANALYSIS artifacts may contain findings/gaps and downstream recommendations, and may feed consultation-only gate packages as consultant-authored inputs. They MUST NOT be written as VERIFICATION artifacts and MUST NOT claim gate closure.

**IMPLEMENTATION boundary**: When an `IMPLEMENTATION` artifact exists for the same scope (task or gate remediation), ANALYSIS artifacts retain their informative/advisory role. ANALYSIS findings and recommendations MAY inform the IMPLEMENTATION specification, but the ANALYSIS artifact MUST NOT duplicate implementation-level specification detail that belongs in the IMPLEMENTATION artifact. The ANALYSIS artifact remains consultant-owned synthesis; the IMPLEMENTATION artifact provides developer-facing specification depth.

---

## III. ANALYSIS TYPE TAXONOMY (DEC001)

Every analysis artifact MUST declare `analysis_type` in frontmatter. Allowed values:
- `pattern_audit`
- `research_synthesis`
- `compliance_audit`
- `assessment`
- `external_review`
- `comparative_analysis`

The `comparative_analysis` subtype was introduced by `T104-PH001-ST008-AC001.7` to address the structural gap in formal option comparison methodology. See §IV.B for lifecycle position.

**Single-template rule (DEC002)**: There is exactly one template (`template_workspace_analysis.md`). Type-specific sections are included/excluded via in-template conditional markers (DEC004).

---

## IV. LIFECYCLE POSITIONS (DEC008, DEC011)

### A. `research_synthesis` (scoped linking chain)

`T104-IG-002 (Research Linking)` applies **only** to `research_synthesis`:
Brief → Report → Analysis → Proposal/SPS.

Minimum lifecycle rules:
1. Research brief and report exist and are linked by a RES ID (per `T102-STD-006` and `P-STD-004` research naming patterns).
2. The analysis synthesizes the report and produces recommendations / mappings for downstream proposal or SSOT updates.
3. The analysis references research evidence by ID/section (link, don’t duplicate).

### B. Non-research analysis types (Draft 1 preliminary)

These lifecycle positions are **Draft 1 preliminary** and SHOULD be refined as more exemplars accumulate:

| analysis_type | Typical upstream trigger | Typical downstream handoff |
|:--|:--|:--|
| `pattern_audit` | Need to standardize a template/guideline surface; exemplar drift detection | Guideline/template authoring tasks; plan updates; potential proposal for decisions |
| `compliance_audit` | Need to check an artifact against standards/guidelines | Remediation tasks; for implementation-backed gates, follow-on VERIFICATION artifact (not inside analysis) |
| `assessment` | Need to evaluate readiness, hardening, or options tradeoffs | Remediation roadmap, decisions/proposals, implementation tasks |
| `comparative_analysis` | Need to compare two or more options/approaches against weighted evaluation criteria to support an architectural or process decision | Decision proposal (standards-input or gate-disposition); plan amendment; implementation task specification for the chosen option |
| `external_review` | Third-party assessment requested; may be transcript-converted. When an `external_review` serves as a gate-readiness input for a consultation-only or implementation-backed gate, the review scope SHOULD include downstream task readiness and plan-guideline compliance for post-gate work. | Consultation-only decision package for client; transition plan and risk register |

**Gate boundary reminder**:
- Implementation-backed gates use VERIFICATION as the reviewer evidence surface.
- Consultation-only gates MAY use ANALYSIS artifacts, including `external_review`, as package inputs to a `gate_disposition` proposal.
- In both cases, ANALYSIS artifacts MUST NOT claim gate closure or replace the proposal-hosted GDR.

---

## V. REQUIRED STRUCTURE (DEC005, DEC009, DEC013)

All analysis types MUST include these universal sections, in order:
1) **Executive Summary**
2) **Scope & Inputs**
3) **Evidence / Methodology**
4) **Findings / GAP Register** (may be empty if no gaps)

Then include the type-specific sections (conditional).

### A. Executive Summary (Audience-Awareness Rule)

Every analysis artifact MUST include an Executive Summary as the first body section.

When an analysis is consumed at a gate — specifically, when it feeds a `gate_disposition` proposal as `analysis_reference` — the Executive Summary MUST include a **Client Summary** subsection.

**Client Summary requirements**:
- Written at a level the `decision_owner_role` (typically Client) can act on without reading the full artifact body.
- Covers: what was found, what it means for the project, and what decisions are needed at the gate.
- Length: 5–10 bullet points recommended. Keep concise; the full analysis body provides depth.
- MUST NOT introduce findings or recommendations not present in the analysis body.

**Non-gate analysis**: When an analysis is not consumed at a gate (e.g., internal consultant working artifact), the Executive Summary follows normal authoring conventions without the Client Summary subsection requirement.

### B. Scope & Inputs

Scope & Inputs MUST:
- declare in-scope and out-of-scope boundaries,
- enumerate all primary inputs (repo-relative paths),
- state what is assumed vs verified (if applicable).

### C. Evidence / Methodology

Evidence / Methodology MUST:
- state how claims were derived (file reads, searches, manual checks),
- include commands run (if any) and what they demonstrated,
- avoid evidence-free claims.

### D. Findings / GAP Register (DEC006, DEC012)

Analysis findings MUST use a lightweight GAP register (not verification findings), with bounded dispositions.

**Table schema (required)**:
`| GAP ID | Category | Title | Description | Disposition | Downstream Target | Notes |`

**Category**: recommended values `{structure, consistency, naming, references, lifecycle, workflow, other}`.

**Disposition enum (bounded) (DEC012)**:
- `pending_decision`
- `resolved`
- `superseded`
- `accepted_as_is`
- `deferred_to_TK###` (e.g., `deferred_to_TK004`)

**Non-gate semantics**:
- GAPs are tracking items. They are not “blocking” in the verification sense.
- If something is gate-blocking, it MUST be escalated into a VERIFICATION finding at the relevant gate.

### E. Downstream Actions (DEC013)

All non-research analysis types MUST include a **Downstream Actions** section with a minimal required field set (table or bullets are acceptable). Required fields:
- `downstream_artifact_type`
- `target_reference`
- `trigger_condition`
- `responsible_role`
- `notes`

`research_synthesis` uses the template’s Integration Roadmap section instead (DEC007).

---

## VI. FRONTMATTER CONVENTIONS (DEC003)

### A. Common required keys

Every analysis artifact MUST include at minimum:
- `artifact_type: 'ANALYSIS'`
- `analysis_type: '<one of the enum values>'`
- `version`, `date`, `status`
- `author: 'LLM_Consultant'`
- `decision_owner_role: 'Client'`
- `initiative_id` (e.g., `T104` or `P`)

### B. Common recommended keys

When applicable, include:
- `initiative_code`
- `phase`, `stream_id`, `activity_id`, `task_id`, `gate_id`
- `plan_reference` (repo-relative path to the governing plan)
- `purpose` (1-line)

### C. Type-specific optional keys (examples)

- `research_synthesis`: `research_id`, `research_brief`, `research_report`, `target_proposal`, `target_sps`
- `compliance_audit`: `target_artifact`, `reference_standard` (and/or list), `audit_scope`
- `assessment`: `target_artifact`, `assessment_scope`
- `comparative_analysis`: `options_compared`, `evaluation_criteria`, `recommended_option`
- `external_review`: `source_file`, `converted_on`
- `pattern_audit`: `inputs_reviewed` (list) or a short `analysis_reference` pointer set

**Policy**: Optional keys MAY be added per analysis type as needed, but authors MUST NOT omit the common required keys.

---

## VII. NAMING & PLACEMENT (P-STD-004, P-STD-005)

### A. Filename pattern

Analysis artifacts MUST follow `P-STD-004-CLAUSE-008A`:
- `analysis_<scope-UID>_<kebab-topic>.md`

`<scope-UID>` MUST be a timeline UID (or other allowed scope UID) per `P-STD-005-CLAUSE-001A (Pattern 4)` and `P-STD-004-CLAUSE-008H`.

### B. Directory placement

Placement MUST follow `P-STD-004-CLAUSE-003F`:
- If `<scope-UID>` contains `-AC###`, place under `workspace/PH###/ST###/AC###/analysis/`.
- Otherwise, place under `workspace/PH###/ST###/analysis/`.

### C. Analysis vs research report boundary

Per `P-STD-004-CLAUSE-008E`, `analysis_` artifacts MUST NOT be treated as research reports and MUST NOT replace `report_` artifacts in the formal research brief/report pairing.

---

## VIII. TEMPLATE INVENTORY

- **Template**: `prompt/templates/consultant/workspace/template_workspace_analysis.md`
- **What**: Single ANALYSIS template with conditional sections for all `analysis_type` values.
- **When**: Use for all new analysis artifacts.
- **How**: Copy the template, set frontmatter keys (including `analysis_type`), keep universal sections, then remove non-applicable conditional blocks.

---

## IX. SUPERSEDED ANALYSIS ARTIFACTS

This section governs how ANALYSIS artifacts are deprecated when a gate is superseded due to an external baseline change. The rules here implement Layer 1 of the three-layer deprecation model (see `workspace_documentation_rules.md` §7.C for the full model).

### A. When Supersession Applies

An ANALYSIS artifact must be deprecated when:
1. The gate it supports has been superseded (`Client Decision = SUPERSEDE` per `guideline_workspace_proposal.md` §VII.C), AND
2. The artifact was produced against the **prior** normative baseline (not the successor baseline).

ANALYSIS artifacts produced against the **successor** baseline carry forward as-is and do NOT require deprecation.

### B. Frontmatter Requirements for Superseded Analysis

When an ANALYSIS artifact is superseded, update its frontmatter:

```yaml
status: 'superseded'
superseded_by: '<repo-relative path to the successor artifact>'
```

- `status: 'superseded'` replaces the prior `status` value (e.g., `draft`, `active`, `completed`).
- `superseded_by` points to the artifact that assesses the same scope against the updated normative baseline.
- Both keys are required when the artifact is superseded. `superseded_by` MUST NOT be left blank.

### C. Deprecation Notice Format (Required)

A deprecation notice MUST be added as the **first line of the body** (immediately after the frontmatter block, before the `# ANALYSIS:` heading):

```
> **SUPERSEDED**: This artifact was produced against [baseline X]. It has been superseded by [successor artifact path] which assesses against [baseline Y]. This artifact is preserved for historical traceability only.
```

Fill in:
- `[baseline X]`: The normative standard/version the artifact was produced against (e.g., `P-STD-002 v1.1.0`)
- `[successor artifact path]`: Repo-relative path to the successor artifact
- `[baseline Y]`: The normative standard/version the successor artifact is produced against (e.g., `P-STD-002 v1.2.0`)

### D. Version Bump and Changelog

When applying the superseded status:
- Bump the version (minor version increment, e.g., v1.0.0 → v1.1.0)
- Add a changelog entry explaining the supersession: which gate triggered it, which baseline changed, and what the successor artifact is

### E. Body Preservation Rule

The body content of a superseded ANALYSIS artifact MUST NOT be altered. Only the following changes are applied:
1. `status` frontmatter key updated to `superseded`
2. `superseded_by` frontmatter key added
3. Deprecation notice added as first body line
4. Version bumped and changelog entry added

The analysis content itself (findings, assessments, recommendations) is preserved unchanged as a historical record of work done under the prior baseline.

### F. Three-Layer Model Context

Layer 1 (this guideline, §IX) handles the artifact-level deprecation signal. The full deprecation model also requires:
- **Layer 2** (Evidence Index in successor gate-disposition proposal): Move superseded analysis from active evidence to `Historical Evidence` subsection with `SUPERSEDED` annotation. See `guideline_workspace_proposal.md` §V.B.
- **Layer 3** (Plan Links Register): Add or update the links register entry with `superseded` annotation. See `guideline_workspace_plan.md` §VI.M.

---

## X. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.7.0 | 2026-03-24 | Amendment | Expanded the `external_review` lifecycle position so gate-readiness inputs SHOULD assess downstream task readiness and plan-guideline compliance for post-gate work. Source: T104-PH001-ST008-AC001.8. |
| v1.6.0 | 2026-03-24 | Amendment | Added `comparative_analysis` to §III taxonomy, §IV.B lifecycle positions, and §VI.C frontmatter keys. Introduced the formal comparative-analysis subtype for weighted option comparison work. Source: T104-PH001-ST008-AC001.7. |
| v1.5.0 | 2026-03-20 | Amendment | Added §IX (Superseded Analysis Artifacts): when-to-apply rules, required frontmatter keys (`status: 'superseded'`, `superseded_by`), deprecation notice format, version-bump and changelog requirements, body-preservation rule, and three-layer model context (this guideline covers Layer 1; Layers 2–3 are in proposal guideline and workspace documentation rules). Source: T104-PH001-ST008-AC001.4 GATE-001 (2026-03-20). |
| v1.4.0 | 2026-03-20 | Amendment | Added IMPLEMENTATION boundary clarification in §II: ANALYSIS artifacts MUST NOT duplicate implementation-level specification detail when an IMPLEMENTATION artifact exists for the same scope. Source: T104-PH001-ST008-AC001.3-GATE-001 Path B approval. |
| v1.3.0 | 2026-03-16 | Amendment | Clarified the gate boundary for consultation-only workflows. ANALYSIS artifacts may now explicitly feed consultation-only gate packages as inputs, while VERIFICATION remains reserved for implementation-backed gates. Source: P-PH000-ST002-AC002 Gate 001 consultation. |
| v1.2.0 | 2026-03-15 | Amendment | Added §V.A (Executive Summary Audience-Awareness Rule): when an analysis feeds a gate_disposition proposal, the Executive Summary MUST include a Client Summary subsection written for the decision_owner_role. Existing §V subsections renumbered (A→B, B→C, C→D, D→E). |
| v1.1.0 | 2026-03-05 | Maintenance | Resolved legacy GDR ownership reference in §II (removed verification artifact as GDR host). |
| v1.0.0 | 2026-03-01 | Initial | Draft 1 authoring guideline for ANALYSIS artifacts. Encodes AC007 GATE-000 decisions (DEC001–DEC009, DEC011–DEC013) and aligns naming/placement guidance to `P-STD-004` and `P-STD-005`. |
