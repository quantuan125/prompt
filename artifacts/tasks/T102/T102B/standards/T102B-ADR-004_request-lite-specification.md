# T102B-ADR-004 — Request Lite Specification

## Decision

* **T102B-ADR-004 (Request Lite Specification)**

  * **Context**
    Per `T102B-STD-002 (Workflow Typology Standard)`, simple features require a lightweight documentation path to reduce adoption friction. RLITE must remain <200 lines per `T102B-CON-003` while providing sufficient context for development.

  * **Decision**
    Define RLITE as a governed subset of `T102B1 (RST)` with mandatory sections only; include selection criteria for workflow routing.

  * **Alternatives Considered**
    - (a) Single heavyweight template for all features — rejected; adoption friction per `T102B-RES-001` W5; simple features over-documented.
    - (b) Completely separate RLITE template (not derived from RST) — rejected; creates drift risk and dual maintenance burden per `T102B-DEP-003`.
    - (c) PR-only for all lightweight changes — rejected as sole alternative; included as third workflow tier for trivial changes but insufficient for features needing minimal requirements documentation.

  * **Consequences**
    (+) Reduces authoring overhead for simple features per `T102B-QG-001`.
    (+) Clear selection criteria prevent workflow confusion.
    (+) Boundary enforcement prevents scope creep.
    (±) Requires author self-assessment accuracy per `T102B-ASSUM-003`.
    (-) Some simple features may be incorrectly routed to RLITE.

  * **References**
    `T102B-STD-002 (Workflow Typology Standard)`, `T102B-CON-003 (Template Variant Boundary)`, `T102B-QG-001 (Adoption Friction Reduction)`, `T102B-IG-004 (Request Lite Selection)`

  * **Provenance**
    - `prompt/artifacts/tasks/T102/T102B/research/report/report_T102B-RES-001_request-artifact-analysis.md`
    - `prompt/artifacts/tasks/T102/T102B/workspace/analysis/analysis_T102B_epic-foundation-assessment.md`

## Specification

1) **T102B-ADR-004-CLAUSE-001 (RLITE Scope Boundary)**
   - RLITE artifacts SHALL remain under 200 lines total per `T102B-CON-003`.
   - RLITE artifacts SHALL NOT expand by section accretion.
   - If scope exceeds boundary during authoring, escalate to Full Request per `T102B-IG-004`.

2) **T102B-ADR-004-CLAUSE-002 (RLITE Mandatory Sections)**
   - YAML Header (per MANIFEST schema).
   - Feature Purpose (1-2 paragraphs).
   - Inherited Considerations table (per `T102-ADR-003`).
   - Scope (In Scope / Out of Scope bullets).
   - Success Criteria (measurable outcomes).
   - Approval Gate section.

3) **T102B-ADR-004-CLAUSE-003 (RLITE Excluded Sections)**
   - Story Index (single-story or no-story features).
   - Detailed NFR section (inherit epic-level NFRs).
   - Extended stakeholder analysis.
   - Research/Evidence sections.

4) **T102B-ADR-004-CLAUSE-004 (Selection Criteria)**
   | Factor | Full Request | RLITE | PR-only |
   |:-------|:-------------|:------|:--------|
   | Story count | >3 stories | 1-3 stories | 0-1 stories |
   | Architectural impact | New patterns | Existing patterns | Trivial change |
   | Stakeholder visibility | High (cross-team) | Medium (team) | Low (developer) |
   | Complexity | High | Low-Medium | Trivial |

5) **T102B-ADR-004-CLAUSE-005 (Decision Tree Workflow)**
   Authors SHALL apply selection criteria per CLAUSE-004 using this decision workflow:
   1. **Assess story count threshold**: If >3 stories → Full Request; if 0-1 stories → consider PR-only
   2. **Assess architectural impact**: If new patterns/integrations → Full Request; if trivial change → consider PR-only
   3. **Assess stakeholder visibility**: If cross-team coordination required → Full Request
   4. **Apply complexity tiebreaker**: If uncertain after factor assessment, default to higher tier
   5. **Boundary enforcement**: If RLITE scope threatens to exceed 200 lines per `T102B-CON-003`, escalate to Full Request

   **Heuristics**:
   - If any single factor indicates Full Request, Full Request SHOULD be selected unless compelling justification exists
   - If uncertain between RLITE and Full Request, prefer Full Request to avoid future escalation
   - If feature is truly trivial (documentation update, config change), PR-only workflow MAY bypass Request entirely
   - Authors SHOULD document workflow selection rationale in Request frontmatter for audit trail
