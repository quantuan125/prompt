---
artifact_type: 'PROPOSAL'
initiative_id: 'T102'
epic_id: 'T102B'
feature_id: 'T102B1'
feature_code: 'RST'
version: '0.1.0'
date: '2026-02-06'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
source_request: 'prompt/artifacts/tasks/T102/T102B/request/request_T102B1-RST.md'
---

# PROPOSAL: RST (T102B1) — Non-Normative Notes & Analysis

## I. EXECUTIVE SUMMARY

This proposal contains **non-normative** content that was originally drafted during AC002 and has been intentionally moved out of the feature-level Request specification (`request_T102B1-RST.md`) to keep the Request focused on the canonical section structure and requirements per `T102B-ADR-002`.

## II. MOVED CONTENT INDEX

Moved from `request_T102B1-RST.md` into this proposal:
- Requirements-with-Guidance Pattern (authoring pattern explanation)
- Industry Alignment Mapping (Conceptual)
- RLITE Derivation Feasibility Check (Informative)
- Appendix additions (Validation Checklist, Next Steps)

---

## III. REQUIREMENTS-WITH-GUIDANCE PATTERN (AUTHORING)

RST uses the “requirements-with-guidance” pattern per `T102B-IG-002`:
- **Normative requirements** SHALL be stated using requirements language (e.g., SHALL/SHOULD) and written so the requirement is understandable without separate “Implementation Guidance” sections.
- **Inline authoring guidance** MUST be clearly marked as guidance (e.g., `Guidance:` prefix or HTML comment blocks) and MUST NOT introduce new obligations beyond the associated requirement statement.
- If guidance becomes enforceable policy, it SHOULD be promoted into a governing `STD/ADR` (or into an explicit `FR/NFR/CON`) rather than living indefinitely as free-form prose.

---

## IV. INDUSTRY ALIGNMENT MAPPING (CONCEPTUAL)

This mapping is intentionally conceptual (no clause-by-clause compliance matrix in Phase 1). Evidence is captured in `T102B-RES-001`.

| RST Section | ISO 29148 (conceptual) | BABOK v3 (conceptual) | SAFe (conceptual) | Evidence (internal) |
|:-----------|:------------------------|:----------------------|:------------------|:--------------------|
| I. Executive Summary | Purpose + overview | Business need framing | Feature intent + benefit framing | `T102B-RES-001` Topics 1–3 |
| A. Problem Definition | Problem/purpose context | Problem statement | “Just enough” feature context | `T102B-RES-001` Topic 3; W1–W7 |
| B. Scope | Scope definition | Scope definition | Feature boundaries | `T102B-RES-001` Topic 1 |
| C. Business Objectives | Success criteria | Goals/objectives/outcomes | Benefit hypothesis + success signals | `T102B-RES-001` Topic 3; Proposal P6 |
| D. Stakeholders | Stakeholder needs framing | Stakeholder analysis | Stakeholder alignment | `T102B-RES-001` Topic 2 |
| E. Inherited Considerations | Traceability emphasis | Governance trace to upstream constraints | Epic→Feature linkage | `T102-ADR-003`, `T102-ADR-005` |
| F. Feature Requirements | Requirements specification | Requirements definition | Feature-level requirements | `T102B-RES-001` Topics 1–3 |
| G. Governance Decisions | Decision record indexing | Governance governance/rationale capture | Guardrails against “waterfall artifact” drift | `T102B-RES-001` Topic 4 (S4); `T102B-CON-004` |
| H. Issues & Risks | Risk/issue management | Issue/risk log | Visibility for adoption/friction risks | `T102B-RES-001` Topic 5 (W1–W7); `T102-ADR-007` |
| I. Research & Notes | Evidence linkage | Evidence/assumptions trace | Lightweight evidence pointers | `T102B-RES-001` methodology + sources |
| J. Story Index | Requirements allocation (navigation only) | Decomposition/navigation | Feature→Story navigation (no story FR bodies) | `T102B-RES-001` Topic 3; `T102B-ADR-003` |
| IV. Acceptance Criteria | Verification criteria | Success measures | Feature AC expectations | `T102B-RES-001` Topic 3 |
| V. Approval Gate | Gate evidence + sign-off | Governance checkpoint | Feature-level “done” for Request stage | `T102B-STD-003`; `T102B-ADR-002-CLAUSE-004` |

---

## V. RLITE DERIVATION FEASIBILITY CHECK (INFORMATIVE)

- RLITE is a governed subset of RST per `T102B-ADR-004-CLAUSE-002` (mandatory sections only).
- Boundary target: RLITE artifacts remain <200 lines per `T102B-ADR-004-CLAUSE-001`; if the mandatory subset cannot meet the boundary, escalate to Full Request per `T102B-ADR-004-CLAUSE-005`.
- RST supports derivation by using `[M]` markers for mandatory sections and keeping optional sections fully omittable (no placeholder required).

---

## VI. REQUEST APPENDIX ADDITIONS (PROCESS / CHECKLISTS)

### A. Validation Checklist

- [x] Problem statement traces to T102B-RES-001 weaknesses (W1-W7)
- [x] Scope explicitly includes P1-P4 proposal implementation
- [x] Business objectives map to T102B quality goals
- [x] Inherited considerations emphasize Initiative + Epic rule IDs (no upstream text restatement)
- [x] Inherited considerations table schema follows `T102-ADR-003-CLAUSE-001`
- [x] Feature requirements address structural changes
- [x] Story Index applicability rule documented (required-if `story_count > 1`)
- [x] Issues & Risks section follows `T102-ADR-007` schema/enums
- [ ] Client approval obtained

### B. Next Steps

**Downstream Consumer**: Stream ST001 (AC003–AC005)

**Implementation Path**:
1. AC003: RST template formalization — author `prompt/templates/request/request_structural_template.md`
2. AC004: RST self-validation & retrofit — retrofit this Request toward v1.0 full conformance
3. AC005: Client approval gate — obtain approval statement and close ST001

