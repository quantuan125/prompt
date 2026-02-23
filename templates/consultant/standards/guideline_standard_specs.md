---
artifact_type: 'PROCEDURAL_GUIDELINE'
domain: 'consultant_standards'
topic: 'standard_specs_authoring'
version: '5.0.0'
date: '2026-02-22'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
spec_reference: 'prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md'
template_reference: 'prompt/templates/consultant/standards/template_standard_specs.md'
---

# Guideline: Standard Specs (STD+DR Combined Files)

## I. PURPOSE

Define authoring rules for the combined standard-specification model where:
- the normative standard specification is authored under `STD` scope, and
- the informative decision rationale is nested inside the same file as `<STD-ID>-ADR-001`.

The canonical combined-file contract is governed by `P-STD-001-CLAUSE-001 (Canonical File Structure)`.

---

## II. LOCKED RULES (PH001)

### A. Canonical location `P-STD-001-CLAUSE-015A`

All standard-spec files live under:
- `prompt/artifacts/tasks/<SID>/standard/` (see P-STD-001-CLAUSE-015A for canonical placement)

### B. File naming convention `P-STD-001-CLAUSE-024A`

Format:
- `standard_<SID-STD>_<kebab-title>.md`

Slug rules:
- lowercase
- spaces → `-`
- collapse multiple `-`
- remove non-alphanumeric characters (replace with `-`)

### C. Canonical structure (required) `P-STD-001-CLAUSE-001`

Every combined file MUST include these headings, in this order:
1. `# <STD-ID> — <Title>`
2. `## Specification`
3. `## Decision Record`
4. `## References`
5. `## Provenance`

---

## III. CONTENT RULES

### A. Specification section `P-STD-001-CLAUSE-018B`

Under `## Specification`, render clause items as:
- `n) **<STD-ID>-CLAUSE-### (<Title>)**`

All clause semantics remain governed by `P-STD-005`.

### B. Decision Record section `P-STD-001-CLAUSE-025`

Under `## Decision Record`, the nested DR body MUST use:
- `* **<STD-ID>-ADR-001 (<Title>)** {#<anchor>}`
- Subheadings: `Context`, `Decision`, `Alternatives`, `Consequences`, `Traceability`

The nested DR is informative rationale and does not replace normative `CLAUSE` authority.

### C. References and Provenance `P-STD-001-CLAUSE-028`

`## References` and `## Provenance` MUST remain STD-level sections and MUST NOT be nested under the DR body.

---

## IV. INDEXING RULES `P-STD-001-CLAUSE-012`

Concept indexes MUST link to standard-spec files using full repo-relative canonical paths per `P-STD-001-CLAUSE-010A`, `P-STD-001-CLAUSE-026D`.
- Example: `prompt/artifacts/tasks/<SID>/standard/standard_<SID-STD>_<kebab-title>.md`

---

## V. QUICK CHECKLIST (AUTHORING / REVIEW)

- [ ] File lives under `prompt/artifacts/tasks/<SID>/standard/`
- [ ] Filename matches `<STD-ID>_<title-slug>.md`
- [ ] File section order is `Specification` → `Decision Record` → `References` → `Provenance`
- [ ] Clause IDs are `<STD-ID>-CLAUSE-###` and sequential
- [ ] DR body ID is `<STD-ID>-ADR-001`
- [ ] Concept index row includes the full repo-relative `Canonical Path`
- [ ] All guideline rules cite their governing CLAUSE(s)

> **Note — Deferred Topics**: This guideline is a quick-start authoring guide. For full rules on Specification Index authoring (`P-STD-001-CLAUSE-002`), substandard architecture (`P-STD-001-CLAUSE-003`), anchor stability (`P-STD-001-CLAUSE-006`), normative vocabulary (`P-STD-001-CLAUSE-008`), CLAUSE ordering (`P-STD-001-CLAUSE-019`), subclause rendering (`P-STD-001-CLAUSE-020`), normative/informative boundary (`P-STD-001-CLAUSE-021`), and promotion/demotion lifecycle (`P-STD-001-CLAUSE-030`), consult `P-STD-001` directly.

---

## VI. CONFORMANCE COUPLING `P-STD-001-CLAUSE-005B`

When `P-STD-001` CLAUSEs are added, modified, or deprecated, this guideline and its template MUST be updated in the same changeset to maintain conformance.

This guideline MUST NOT introduce normative rules that are not traceable to a governing CLAUSE in `P-STD-001`.

**Known derivative files** (blast radius when `P-STD-001` CLAUSEs change):
1. `prompt/templates/consultant/standards/guideline_standard_specs.md` (this file)
2. `prompt/templates/consultant/standards/template_standard_specs.md`
3. `prompt/artifacts/tasks/P/ssot/sps_P-PROGRAM.md` (STD Index rows — `P-STD-001-CLAUSE-014C`)
4. `prompt/AGENTS.md` (informative directive — best practice)

**Impact analysis practice** (informative): Before amending a CLAUSE, search for the specific CLAUSE-ID (e.g., `P-STD-001-CLAUSE-005D`) across all known derivative files to identify citations requiring update.

---

## VII. AUTHORITY CHAIN `P-STD-001-CLAUSE-005A`

This guideline is governed by `P-STD-001 (Program Governance Standard)`.

The template (`prompt/templates/consultant/standards/template_standard_specs.md`) is a derivative of this guideline and MUST conform to the structural requirements prescribed by governing CLAUSEs and this guideline.

---

## VIII. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v5.0.0 | 2026-02-22 | Major | Citation format migrated from the legacy per-wrapper form to `<CLAUSE-ID>` per amended `P-STD-001-CLAUSE-005D`. 4 mis-cited governing CLAUSEs corrected (III.A→018B, III.B→025, III.C→028, IV→012; II.B→024A). DR subheadings corrected to CLAUSE-025B (Alternatives, +Traceability). Deferred topics note added. Blast radius enumeration and impact analysis practice added to Section VI. (GATE-002 remediation pass 2) |
| v4.1.0 | 2026-02-21 | Fix | Naming format (II.B) corrected to match `P-STD-001-CLAUSE-015A` (`standard_<SID-STD>_<kebab-title>.md`). Governing citations corrected: II.A → CLAUSE-015A, VI → CLAUSE-005B, VII → CLAUSE-005A. (GATE-002 remediation) |
| v4.0.0 | 2026-02-20 | Major | Authority chain migrated from `T102-STD-004` to `P-STD-001` following full promotion (`P-STD-001-ADR-003`). All CLAUSE references updated. Hardcoded T102 paths replaced with `<SID>/standard/` portable form per `P-STD-001-CLAUSE-015A`. Pre-existing CLAUSE-016 mis-citations corrected to CLAUSE-001. |
