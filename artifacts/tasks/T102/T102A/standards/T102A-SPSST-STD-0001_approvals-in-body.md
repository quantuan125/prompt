# T102A-SPSST-STD-0001 — Approvals in body

## Specification

1) **T102A-SPSST-STD-0001-CLAUSE-001 (Approval Signal Placement)**
   - SPS, Request, and Concept artifacts SHALL keep approval lists in artifact body sections, not in YAML frontmatter.

2) **T102A-SPSST-STD-0001-CLAUSE-002 (Header Scope Discipline)**
   - Canonical YAML headers SHALL contain artifact identity and metadata fields only.
   - YAML headers SHALL NOT contain approval arrays or gate-signoff payloads.

3) **T102A-SPSST-STD-0001-CLAUSE-003 (Standard vs Artifact Boundary)**
   - Standard/template documents MAY retain body metadata conventions.
   - Artifact documents (SPS, REQUEST, CONCEPT, DESIGN) SHALL use the canonical header and body-level approvals contract.

## Decision Record

* **T102A-SPSST-STD-0001-ADR-001 (Approvals in body)** {#t102a-spsst-std-0001-approvals-in-body}

  * **Context**
    Story `T102A-SPSST-S1` compared multiple header strategies and found that embedding approvals in YAML increased schema complexity and reduced human readability of governance signals.

  * **Decision**
    Adopt header v1.0.0 with a minimal cross-artifact schema and keep approvals in body sections. Preserve the standard/artifact split where standards remain body-oriented and artifacts carry canonical YAML headers.

  * **Alternatives Considered**
    - Encode approvals in YAML header fields.
    - Keep legacy key patterns (`task_id`, `prefix_id`) without standardization.
    - Expand header with additional extension keys in v1.

  * **Consequences**
    (+) Lightweight, stable parsing surface for tooling and handoffs.
    (+) Human-visible approvals remain clear in artifact body sections.
    (±) Validators must read both header and body for complete governance checks.
    (-) Requires discipline to prevent approval fields from reappearing in YAML.

## References

`T102A-SPSST-S1-FR-01 (Header presence & core keys)`,
`T102A-SPSST-S1-FR-02 (Key formats & enums)`,
`T102A-SPSST-S1-FR-03 (Canonical examples & reference)`

## Provenance

- `prompt/artifacts/tasks/T102/consultant/design/design_T102A-SPSST-S1.md`
- `prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md`
