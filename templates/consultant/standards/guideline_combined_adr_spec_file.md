---
artifact_type: 'PROCEDURAL_GUIDELINE'
domain: 'consultant_standards'
topic: 'combined_adr_spec_file_authoring'
version: '2.0.0'
date: '2026-02-06'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
template_reference: 'prompt/templates/consultant/standards/template_combined_adr_spec_file.md'
---

# Guideline: Combined ADR+Spec Files (Model D, Phase 1)

## I. PURPOSE

Define the Phase 1 authoring rules for **Model D (Combined ADR+Spec Files)** so:
- `T102C (CONCEPT)` can become an **index-only** navigation hub (no embedded ADR bodies), and
- ADR bodies (including their normative `Specification/CLAUSE`) live in stable, external combined files.

This guideline intentionally adopts a **minimal-migration** format to reduce Phase 1 governance churn.

The combined-file dual nature (Decision Record + Normative Specification in a single `ADR`-tokened file) is governed by `T102-ADR-004-CLAUSE-016 (Combined-File Dual Nature)`.

---

## II. LOCKED RULES (PH001)

### A. Canonical location `[per T102-ADR-004-CLAUSE-002]`

All combined ADR+Spec files live under:
- `prompt/artifacts/tasks/T102/consultant/standards/`

### B. File naming convention `[per T102-ADR-004-CLAUSE-001, CLAUSE-003]`

Format:
- `<ADR-ID>_<title-slug>.md`

Slug rules:
- lowercase
- spaces → `-`
- collapse multiple `-`
- remove non-alphanumeric characters (replace with `-`)

**Stability rule**:
- Filenames and paths MUST NOT change in Phase 1 (no renames/moves).

### C. Internal structure boundary (required) `[per T102-ADR-004-CLAUSE-016]`

Every combined file MUST include these headings, in this order:
1. `## Decision`
2. `## Specification`

---

## III. CONTENT RULES (MINIMAL MIGRATION)

### A. Decision section `[per T102-ADR-004-CLAUSE-004]`

Under `## Decision`, render the ADR body using the existing DR body structure (see `T102-ADR-004`), including:
- `Context`
- `Decision`
- `Alternatives Considered`
- `Consequences`
- `References`
- `Provenance`

### B. Specification section `[per T102-ADR-004-CLAUSE-005]`

Under `## Specification`, render the clause list exactly as a numbered list of `CLAUSE` items:
- `n) **<ADR-ID>-CLAUSE-### (<Title>)**`

Clause semantics and construction remain governed by `T102-ADR-005` (no new token types in Phase 1).

---

## IV. INDEXING RULES (CONCEPT ADR INDEX) `[per T102-ADR-004-CLAUSE-001]`

Concept ADR indexes MUST link to combined files using a **full repo-relative Canonical Path**:
- Example: `prompt/artifacts/tasks/T102/consultant/standards/T102-ADR-004_decision-records-index.md`

Phase 1 index granularity is the combined file as a whole (anchors are not required in the index).

---

## V. QUICK CHECKLIST (AUTHORING / REVIEW)

- [ ] File lives under `prompt/artifacts/tasks/T102/consultant/standards/`
- [ ] Filename matches `<ADR-ID>_<title-slug>.md`
- [ ] File contains `## Decision` and `## Specification` headings
- [ ] Clause IDs remain unchanged and sequential within the ADR
- [ ] Concept index row includes the full repo-relative `Canonical Path`
- [ ] All guideline rules cite their governing CLAUSE(s)

---

## VI. CONFORMANCE COUPLING `[per T102-ADR-004-CLAUSE-017]`

When `T102-ADR-004` CLAUSEs are added, modified, or deprecated, this guideline and its template MUST be updated in the same changeset to maintain conformance.

This guideline MUST NOT introduce normative rules that are not traceable to a governing CLAUSE in `T102-ADR-004`.

---

## VII. AUTHORITY CHAIN `[per T102-ADR-004-CLAUSE-017]`

This guideline is governed by `T102-ADR-004 (Decision Records Index)`.

The template (`prompt/templates/consultant/standards/template_combined_adr_spec_file.md`) is a derivative of this guideline and MUST conform to the structural requirements prescribed by governing CLAUSEs and this guideline.
