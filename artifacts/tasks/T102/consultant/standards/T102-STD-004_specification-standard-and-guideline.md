# T102-STD-004 — Specification Standard & Guideline
{#t102-std-004-specification-standard-and-guideline}

## Specification

1) **T102-STD-004-CLAUSE-001 (DR Index Schemas)**

   - **ADR Index Schema**
     `ADR ID | Title | Authority STD | Status | Owner | Effective | Supersedes | Canonical Path`

   - **Column Definitions**
     1. `ID`: ID construction MUST follow `T102-STD-005` following general format: `<SID>-ADR-###`
     2. `Title`: Title Case, 2–3 words.
     3. `Status`: `{Proposed, Accepted, Deprecated}`.
     4. `Owner`: governance authority (typically `Client`) or implementation owner; if unknown use `—`.
     5. `Effective`: ISO-8601 date `YYYY-MM-DD`.
     6. `Supersedes`: list of superseded IDs or `—`.
     7. `Canonical Path`: full repo-relative path to the combined standard-specification file; MUST resolve to an existing file under the scope's designated standards directory.
     8. `Authority STD`: the governing `STD` that applies to the ADR (or that contains the ADR as a nested decision record). Use `—` if none.

   - Phase 1 index granularity is the combined file as a whole (no anchor addressing required in indexes).

2) **T102-STD-004-CLAUSE-002 (Placement Standards)**
   - **SPS artifacts**: section titled `"<SCOPE> Governance Decisions"` containing governance decisions only.
   - **Concept artifacts**: section titled `"<SCOPE> Architectural Decisions"` with mirror subsections for Epic/Feature areas as needed.
   - **Combined files**: full normative specifications and nested decision records live in combined standard-specification files under the scope's designated standards directory; SPS/Concept are index-only hubs referencing combined files via Canonical Path.
   - **Consistency requirement**: placement MUST follow established artifact section numbering without local deviations.

3) **T102-STD-004-CLAUSE-003 (Entry Creation Workflow)**
   To create a new ADR index entry:
   1. Add a new row to the appropriate index table using the required schema per `T102-STD-004-CLAUSE-001`.
   2. Assign the next sequential ID for that scope.
   3. Create a combined standard-specification file at the canonical path using the standard-specification template, applying CLAUSE entries under `## Specification` and DR body structure under `## Decision Record` per `T102-STD-004-CLAUSE-004`.
   4. Ensure References follow `T102-STD-005`.
   5. Populate the Canonical Path column in the index row with the full repo-relative path to the combined file.

4) **T102-STD-004-CLAUSE-004 (DR Body Template)**
   - **Structure**:
     - **Headings**: Main bold headings (e.g. `* **Context**`) MUST be preceded by two newlines.
     - **Body**: Content MUST start on a new line and INDENTED under the heading with no space in between.
   - **Format**: `* **<STD-ID>-ADR-### (<Title>)** {#<anchor>}`
   - **Required Subheadings**:
     * **Context** [Why this decision is needed; the gap it resolves.]
     * **Decision** [What is adopted/changed and who owns it.]
     * **Alternatives Considered** [Bulleted list of additional options considered with clear rejection rationales.]
     * **Consequences** [Impacts using `(+)`, `(±)`, `(-)` bullets.]
   - In combined standard-specification files, the DR body lives under `## Decision Record`. References and Provenance are STD-level sections.

5) **T102-STD-004-CLAUSE-005 (Specification Clauses)**

   **Purpose**
   Standardize how **Specification** sections are constructed using `CLAUSE` IDs, without duplicating global ID semantics.

   **Normative Reference**
   - `CLAUSE` token type construction and semantics MUST follow `T102-STD-005-CLAUSE-005D (Specification Clause Semantics)`.

   **Specification Section Structure**
   Within a combined standard-specification file, the **Specification** section MUST be a list of clause items, each defined as:

   - Format: `n) **<CLAUSE-ID> (<Title>)**`, where `<CLAUSE-ID>` conforms to `T102-STD-005-CLAUSE-005D`.

   In combined files, CLAUSEs live under `## Specification`, a peer section to `## Decision Record` (not nested within the DR body).

   **Clause Requirements**
   - Each clause MUST be a single primary normative statement (avoid compound obligations where feasible).
   - Each `CLAUSE` ID MUST conform to `T102-STD-005-CLAUSE-005D` (including enforceability and required normative language).
   - If additional detail is required, it SHOULD be provided as subclauses per `T102-STD-005-CLAUSE-005D`.
   - Clause Titles MUST follow the title conventions defined in `T102-STD-005-CLAUSE-001`.

   **Ordering**
   - `CLAUSE` IDs MUST be sequential in the order they appear within the Specification section (`001`, `002`, `003`, ...).
   - Subclauses MUST immediately follow their parent clause.

   **Markdown Subclause Rendering**
   - Subclauses SHOULD be rendered as nested bullet items under the parent clause and prefixed by their full CLAUSE-ID (e.g., `<STD-ID>-CLAUSE-002A`).

   **Referencing**
   - Other artifacts MAY reference specific Specification clauses using the formal format defined in `T102-STD-005-CLAUSE-004 (Reference Semantics)`, e.g.:
     `Reference:` `T102-STD-004-CLAUSE-005 (Specification Clauses)`

   **Non-Duplication Constraint**
   - `T102-STD-004` MUST NOT redefine the syntax, scope validity, or semantic authority of `CLAUSE` IDs; those are defined in `T102-STD-005-CLAUSE-005D`.

6) **T102-STD-004-CLAUSE-006 (Cross-Artifact Linking Patterns)**

   - **STD Internal DR Pattern.**
     A combined standard-specification file MUST contain its decision record internally under `## Decision Record` using the nested ADR format from `T102-STD-004-CLAUSE-004`.

   - **Decision Record Context Pattern.**
     The nested ADR **Context** SHOULD state the motivating problem in narrative form and MAY use shorthand IDs for traceability.

   - **Context/References Boundary.**
     The nested ADR **Context** MUST NOT use a formal "Governed By" citation line. Formal citations belong in the STD-level `## References` section.

   - **Index → Combined File (Canonical Path Linkage).**
     Concept/SPS index tables link to combined files via full repo-relative Canonical Path (per `T102-STD-004-CLAUSE-001`); Phase 1 links at file granularity.

7) **T102-STD-004-CLAUSE-007 (Anchor Title Stability)**

   - Anchors MUST be lower-kebab derived from the Title.
   - Anchors MUST remain stable across file moves/splits.
   - If Title changes, keep the old anchor unless an explicit migration is performed.
   - Phase 1 stability contract: combined-file names and canonical paths SHOULD remain stable after migration completion. Anchors extracted from Concept remain stable within their combined file.

8) **T102-STD-004-CLAUSE-008 (Lifecycle Coherence)**

   When a governing STD changes **Status** or is **Superseded**, affected combined files MUST:
   - update the nested ADR **Context** wording to the current governance rationale as needed; and
   - add prior governing IDs to **References** as appropriate; and
   - perform this update in the next modification to the combined file or in a dedicated "governance sync" change set.

9) **T102-STD-004-CLAUSE-009 (Status Management)**

   - Lifecycle: `Proposed → Accepted → Deprecated`
   - Superseded IDs MUST be captured in the **Supersedes** column and, where applicable, referenced in body text.
   - For specification lifecycle stages governing CLAUSE content evolution, see `T102-STD-004-CLAUSE-017`.

10) **T102-STD-004-CLAUSE-010 (Precedence Conflicts Hierarchy)**

    For conflict resolution across DRIDs:
    `Initiative STD > Initiative ADR > Epic ADR > Feature ADR > Story ADR`

    See `T102-STD-003` and `T102-STD-005` for full hierarchy and directionality constraints.

11) **T102-STD-004-CLAUSE-011 (Consequences Scope Requirements)**

    - **STD Consequences** SHOULD cover: policy/precedence impacts; compliance expectations; migration/rollout; automation/traceability effects.
    - **ADR Consequences** SHOULD cover: quality trade-offs; constraints introduced; operational effects; debt/risks.

12) **T102-STD-004-CLAUSE-012 (References & Provenance)**

    - **References** MUST use the formal reference style defined in `T102-STD-005`.
    - **Provenance** MUST list relevant repo-relative paths (no raw URLs).

13) **T102-STD-004-CLAUSE-013 (Variance ADR Contract)**

    A "Variance ADR" is required when a downstream artifact MUST deviate from an upstream standard. It MUST include:
    - **Variance From:** list of overridden upstream IDs.
    - **Rationale:** technical/environment justification.
    - **Scope Impact:** what inheritance/automation breaks.
    - **Lifecycle:** MUST be `Accepted` via governance sign-off (Client or delegated authority).

14) **T102-STD-004-CLAUSE-014 (Decision Promotion Workflow)**

    Decision records SHOULD follow a staged lifecycle:
    1. **Research (RES)** — Use `RES-SID` to commission and document evidence, options, and empirical findings for a specific scope (Initiative/Epic/Feature).
    2. **Implementation Guidance (IG)** — Encode candidate implementation patterns at the appropriate scope (typically Feature); IGs MAY evolve as research is refined.
    3. **Decision Records (STD/ADR)** — Promote stable, cross-cutting, or long-lived patterns into formal STD/ADR records when:
        - (a) The pattern affects multiple artifacts or features; or
        - (b) The pattern requires explicit governance (ownership, status, supersedes) beyond implementation detail.
    4. **Traceability** — Specifications SHOULD reference governing research and guidance in **Provenance** and **References**, rather than duplicating detailed patterns.
    5. **Scope Guidance** —
        - Epic-level ADRs SHOULD be used for cross-feature decisions (e.g., shared vocabularies, common JSON architectures).
        - Feature-level ADRs SHOULD be reserved for significant, feature-local architectural decisions that cannot reasonably be governed at Epic scope.
        - Routine implementation details MAY remain in guidance without a dedicated ADR.

15) **T102-STD-004-CLAUSE-015 (Automation & Linting Checks)**

    Authors SHOULD pass these checks:
    - Combined file contains `## Specification` and `## Decision Record` headings in that order.
    - Nested ADR body **Context** does not include a "Governed By" citation line.
    - Combined file contains STD-level `## References` and `## Provenance` headings.
    - Every `Canonical Path` in an index resolves to an existing file.

16) **T102-STD-004-CLAUSE-016 (Combined-File Canonical Structure)**
    - In Phase 1, the governing file shape is a combined standard-specification file with one nested decision record.
    - Every combined file MUST contain exactly these sections in order:
      1. `# <STD-ID> — <Title>`
      2. `## Specification`
      3. `## Decision Record`
      4. `## References`
      5. `## Provenance`
    - `## Specification` contains normative `CLAUSE` items (enforceable language: SHALL/SHOULD/MUST/MAY).
    - `## Decision Record` contains one current nested ADR body (`<STD-ID>-ADR-###`) with informative rationale.
    - `## References` and `## Provenance` are STD-level sections governing the entire file.

17) **T102-STD-004-CLAUSE-017 (Specification Lifecycle & Authority Chain)**

    Specification Lifecycle Stages:
    - `Draft`: Initial authoring; content is subject to change without formal review.
    - `Proposed`: Content submitted for review; normative language present but not yet binding.
    - `Accepted`: Content is binding; normative language is enforceable within the declared scope.
    - `Amended`: Accepted content modified via a governed change process; prior version is superseded.
    - `Deprecated`: Content is no longer binding; retained for historical reference.

    Authority Derivation Chain:
    - Authority flows downward: Specification (CLAUSEs) → Guideline (informative) → Template (derivative).
    - A Guideline MUST cite the governing CLAUSE(s) it derives from.
    - A Template MUST conform to structural requirements prescribed by governing CLAUSEs and Guideline.

    Conformance Coupling Rule:
    - When a Specification CLAUSE is added, modified, or deprecated, all derivative artifacts
      (Guideline and Template) MUST be updated in the same changeset to maintain conformance.
    - Derivatives MUST NOT introduce normative rules that are not traceable to a governing CLAUSE.

## Decision Record

* **T102-STD-004-ADR-001 (Specification Standard & Guideline)** {#t102-std-004-adr-001-specification-standard-and-guideline}

  * **Context**
    The current governance surface is split between index artifacts and combined files, which creates a dual-surface authoring pattern that drifts over time and weakens consistency targets tied to `T102-QG-002`. A single canonical combined-file structure is needed so normative clauses and decision rationale remain co-located, machine-checkable, and reviewable.

  * **Decision**
    Adopt the standard-specification combined-file model with `## Specification` first and a nested informative ADR under `## Decision Record`. This file (`T102-STD-004`) is the golden exemplar defining clause structure, linkage patterns, and lifecycle controls for decision-record standards.

  * **Alternatives Considered**
    - Keep ADR-first combined structure and external adoption links — rejected due to ongoing dual-surface drift.
    - Split rationale into standalone ADR files for all standards — rejected for Phase 1 due to migration overhead and coordination risk.

  * **Consequences**
    (+) Clear authority boundary: Specification is normative; nested ADR is informative.
    (+) Single-file review surface improves consistency and auditability.
    (+) Enables deterministic migration and linting patterns for downstream rollout.
    (±) Requires coordinated updates to indexes, templates, and references in subsequent tasks.
    (-) Legacy ADR-based references require temporary alias handling during transition.

## References

`T102-QG-002 (Client Readability)`,
`T102-STD-005 (ID Specification & Rules)`,
`T102-IG-007 (ID Standard)`,
`T102-IG-008 (Decision Logging)`,
`T102-IG-009 (Traceability Framework)`,
`T102-STD-001 (Consultancy Operating Model Standard)`

## Provenance

- `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_refactor-adr-004-005.md`
