---
artifact_type: 'PROCEDURAL_GUIDELINE'
domain: 'consultant_standards'
topic: 'standard_specs_authoring'
version: '3.0.0'
date: '2026-02-07'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
template_reference: 'prompt/templates/consultant/standards/template_standard_specs.md'
---

# Guideline: Standard Specs (STD+DR Combined Files)

## I. PURPOSE

Define authoring rules for the combined standard-specification model where:
- the normative standard specification is authored under `STD` scope, and
- the informative decision rationale is nested inside the same file as `<STD-ID>-ADR-001`.

The canonical combined-file contract is governed by `T102-STD-004-CLAUSE-016 (Combined-File Canonical Structure)`.

---

## II. LOCKED RULES (PH001)

### A. Canonical location `[per T102-STD-004-CLAUSE-002]`

All standard-spec files live under:
- `prompt/artifacts/tasks/T102/consultant/standards/`

### B. File naming convention `[per T102-STD-004-CLAUSE-001, CLAUSE-003]`

Format:
- `<STD-ID>_<title-slug>.md`

Slug rules:
- lowercase
- spaces → `-`
- collapse multiple `-`
- remove non-alphanumeric characters (replace with `-`)

### C. Canonical structure (required) `[per T102-STD-004-CLAUSE-016]`

Every combined file MUST include these headings, in this order:
1. `# <STD-ID> — <Title>`
2. `## Specification`
3. `## Decision Record`
4. `## References`
5. `## Provenance`

---

## III. CONTENT RULES

### A. Specification section `[per T102-STD-004-CLAUSE-005]`

Under `## Specification`, render clause items as:
- `n) **<STD-ID>-CLAUSE-### (<Title>)**`

All clause semantics remain governed by `T102-STD-005`.

### B. Decision Record section `[per T102-STD-004-CLAUSE-004]`

Under `## Decision Record`, the nested DR body MUST use:
- `* **<STD-ID>-ADR-001 (<Title>)** {#<anchor>}`
- Subheadings: `Context`, `Decision`, `Alternatives Considered`, `Consequences`

The nested DR is informative rationale and does not replace normative `CLAUSE` authority.

### C. References and Provenance `[per T102-STD-004-CLAUSE-012, CLAUSE-016]`

`## References` and `## Provenance` MUST remain STD-level sections and MUST NOT be nested under the DR body.

---

## IV. INDEXING RULES `[per T102-STD-004-CLAUSE-001]`

Concept indexes MUST link to standard-spec files using full repo-relative canonical paths.
- Example: `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-004_decision-records-standard.md`

---

## V. QUICK CHECKLIST (AUTHORING / REVIEW)

- [ ] File lives under `prompt/artifacts/tasks/T102/consultant/standards/`
- [ ] Filename matches `<STD-ID>_<title-slug>.md`
- [ ] File section order is `Specification` → `Decision Record` → `References` → `Provenance`
- [ ] Clause IDs are `<STD-ID>-CLAUSE-###` and sequential
- [ ] DR body ID is `<STD-ID>-ADR-001`
- [ ] Concept index row includes the full repo-relative `Canonical Path`
- [ ] All guideline rules cite their governing CLAUSE(s)

---

## VI. CONFORMANCE COUPLING `[per T102-STD-004-CLAUSE-017]`

When `T102-STD-004` CLAUSEs are added, modified, or deprecated, this guideline and its template MUST be updated in the same changeset to maintain conformance.

This guideline MUST NOT introduce normative rules that are not traceable to a governing CLAUSE in `T102-STD-004`.

---

## VII. AUTHORITY CHAIN `[per T102-STD-004-CLAUSE-017]`

This guideline is governed by `T102-STD-004 (Specification Standard & Guideline)`.

The template (`prompt/templates/consultant/standards/template_standard_specs.md`) is a derivative of this guideline and MUST conform to the structural requirements prescribed by governing CLAUSEs and this guideline.
