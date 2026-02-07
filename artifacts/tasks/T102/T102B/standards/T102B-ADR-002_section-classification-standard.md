# T102B-ADR-002 — Section Classification Standard

## Decision

* **T102B-ADR-002 (Section Classification Standard)**

  * **Context**
    Per `T102B-STD-004 (Section Classification Policy)`, a unified section classification schema is required to ensure consistent artifact structure and enable completeness validation per `T102B-QG-003`.

  * **Decision**
    Define three classification categories (Mandatory, Optional, Deferred) and specify canonical section lists for Full Request and RLITE variants.

  * **Alternatives Considered**
    - (a) Binary classification (Mandatory/Optional only) — rejected; insufficient granularity for deferred content that belongs in downstream artifacts.
    - (b) Four-tier classification (adding "Conditional") — rejected; "Conditional" overlaps with "Optional" for authoring purposes and adds complexity without clarity.

  * **Consequences**
    (+) Enables automated completeness checking per `T102B-QG-003`.
    (+) Clear section expectations reduce authoring ambiguity.
    (+) Variant-specific lists support RLITE scope boundary.
    (±) Section additions require ADR update.
    (-) May not cover all edge case sections.

  * **References**
    `T102B-STD-004 (Section Classification Policy)`, `T102B-QG-003 (Artifact Completeness)`, `T102B-ADR-004 (Request Lite Specification)`

  * **Provenance**
    - `prompt/artifacts/tasks/T102/T102B/research/report/report_T102B-RES-001_request-artifact-analysis.md`

## Specification

1) **T102B-ADR-002-CLAUSE-001 (Classification Categories)**
   - **Mandatory**: Section MUST contain substantive content before approval gate.
   - **Optional**: Section MAY be omitted or contain placeholder text.
   - **Deferred**: Section content belongs in downstream artifacts; SHALL contain reference/placeholder only.

2) **T102B-ADR-002-CLAUSE-002 (Full Request Section List)**
   This table classifies sections under the major **Core Content** wrapper only. Major section structure (YAML + major `##` sections) is specified in CLAUSE-005.
   | Section | Classification | Notes |
   |:--------|:---------------|:------|
   | A. Problem Definition | Mandatory | Problem + desired outcome |
   | B. Scope | Mandatory | In/Out bullets |
   | C. Business Objectives | Mandatory | Include success signals; benefit hypothesis encouraged |
   | D. Stakeholders | Optional | Required for cross-team features; may be role-based or persona-based |
   | E. Inherited Considerations | Mandatory | Per `T102-ADR-003` (Explicit Inheritance Model) table contract |
   | F. Feature Requirements | Mandatory | Includes assumptions/constraints/FR/NFR/interfaces (as applicable) |
   | G. Governance Decisions | Optional | DR index only; Request SHALL NOT embed ADR bodies per `T102B-CON-004` |
   | H. Issues & Risks | Optional | Per `T102-ADR-007` schema |
   | I. Research & Notes | Optional | Link to RES artifacts; include industry alignment mapping |
   | J. Story Index | Optional | Required if `story_count > 1` per CLAUSE-004 |

3) **T102B-ADR-002-CLAUSE-003 (RLITE Section List)**
   This table classifies items under the major **Core Content** wrapper only. Major section structure (YAML + major `##` sections) is specified in CLAUSE-005.
   | Section | Classification | Notes |
   |:--------|:---------------|:------|
   | Inherited Considerations | Mandatory | Per `T102-ADR-003` |
   | Scope | Mandatory | In/Out bullets |
   | Success Criteria | Mandatory | Measurable outcomes |

4) **T102B-ADR-002-CLAUSE-004 (Validation Rules)**
   - Mandatory sections with empty content SHALL fail gate validation.
   - Optional sections MAY be omitted entirely (no placeholder required).
   - Deferred sections SHALL contain explicit deferral note with target artifact.
   - Major section structure (YAML + major `##` sections) SHALL follow CLAUSE-005.
   - Story Index applicability rule: if `story_count > 1`, Section J (Story Index) SHALL be present and populated.
     - Definition: `story_count` is the number of Story rows in the Story Index table (excluding the header row).

5) **T102B-ADR-002-CLAUSE-005 (Major Section Structure — Documentation Standards)**
   Per `T102-CON-003 (Documentation Standards)`, major section structure SHALL follow `prompt/documentation/main/prompt_main.md`.
   - This ADR’s section lists (CLAUSE-002/003) intentionally classify **Core Content** only.
   - **Additive convention (T102B Request-family artifacts)**: Major `##` section headings SHALL use **Capital Roman numerals** (e.g., `## I. ...`, `## II. ...`) as shown in the tables below. This convention is additive to the heading rules in `prompt_main.md`.
   - YAML Header is required front matter and is not a `##` heading.

   **Full Request — Major Sections**
   | Major Section | Classification | Notes |
   |:--------------|:---------------|:------|
   | YAML Header | Mandatory | Front matter (not a `##` heading); per MANIFEST schema |
   | `## I. Executive Summary` | Mandatory | Feature purpose (1–2 paragraphs) + problem/outcome framing |
   | `## II. Table of Contents` | Optional | Recommended for Full Request readability |
   | `## III. Core Content` | Mandatory | Wrapper containing CLAUSE-002 sections |
   | `## IV. Acceptance Criteria` | Mandatory | Feature-level ACs only (no story-level AC bodies) |
   | `## V. Approval Gate` | Mandatory | Checklist + sign-off (evidence per `T102B-STD-003`) |
   | `## VI. Appendix` | Optional | Amendments, references, validation checklist, and other supporting info |

   **RLITE — Major Sections**
   | Major Section | Classification | Notes |
   |:--------------|:---------------|:------|
   | YAML Header | Mandatory | Front matter (not a `##` heading); per MANIFEST schema |
   | `## I. Executive Summary` | Mandatory | Feature purpose (1–2 paragraphs) + problem/outcome framing |
   | `## II. Core Content` | Mandatory | Wrapper containing CLAUSE-003 items |
   | `## III. Approval Gate` | Mandatory | Simplified checklist |
