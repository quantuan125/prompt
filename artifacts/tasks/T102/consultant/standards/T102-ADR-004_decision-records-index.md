# T102-ADR-004 — Decision Records Index

## Decision

* **T102-ADR-004 (Decision Records Index)** {#t102-adr-004-drs-index}

  * **Context**
    Per `T102-STD-004 (Decision Records Standard)`, ADR schemas and anchors vary across artifacts, causing drift and blocking automation.

  * **Decision**
    Implement a unified decision record index: one table schema, shared body subheadings, and consistent anchors/links across SPS/Request/Concept/Design. This ADR serves as the adopted normative specification for `T102-STD-004`.

  * **Alternatives Considered**
    (a) Combine GDR & ADR in a single DR index — rejected.

  * **Consequences**
    (+) One schema and body pattern; shared tooling and easier authoring
    (+) Stable anchors enable automation and cross-referencing
    (+) Clear governance vs. implementation separation with ADR additions
    (±) Migration effort for existing non-conforming records
    (-) Ongoing upkeep for instructional guidelines/examples

  * **References**
    `T102-STD-004 (Decision Records Standard)`,
    `T102-IG-007 (ID Standard)`,
    `T102-IG-008 (Decision Logging)`,
    `T102-IG-009 (Traceability Framework)`,
    `T102-STD-001 (Consultancy Operating Model Standard)`

  * **Provenance**
    - `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_refactor-adr-004-005.md`

## Specification

1) **T102-ADR-004-CLAUSE-001 (DR Index Schemas)**

   - **ADR Index Schema**
     `ADR ID | Title | Authority STD | Status | Owner | Effective | Supersedes | Canonical Path`

   - **Column Definitions**
     1. `ID`: ID construction MUST follow `T102-ADR-005` following general format: `<SID>-ADR-###`
     2. `Title`: Title Case, 2–3 words.
     3. `Status`: `{Proposed, Accepted, Deprecated}`.
     4. `Owner`: governance authority (typically `Client`) or implementation owner; if unknown use `—`.
     5. `Effective`: ISO-8601 date `YYYY-MM-DD`.
     6. `Supersedes`: list of superseded IDs or `—`.
     7. `Canonical Path`: full repo-relative path to the combined ADR+Spec file; MUST resolve to an existing file under the scope's designated standards directory.
     8. `Authority STD`: the governing `STD` that applies to the ADR (or that adopts the ADR as the canonical normative spec). Use `—` if none.

   - Phase 1 index granularity is the combined file as a whole (no anchor addressing required in indexes).

2) **T102-ADR-004-CLAUSE-002 (Placement Standards)**
   - **SPS artifacts**: section titled `"<SCOPE> Governance Decisions"` containing governance decisions only.
   - **Concept artifacts**: section titled `"<SCOPE> Architectural Decisions"` with mirror subsections for Epic/Feature areas as needed.
   - **Combined files**: full DR bodies and normative specifications live in combined ADR+Spec files under the scope's designated standards directory; SPS/Concept are index-only hubs referencing combined files via Canonical Path.
   - **Consistency requirement**: placement MUST follow established artifact section numbering without local deviations.

3) **T102-ADR-004-CLAUSE-003 (Entry Creation Workflow)**
   To create a new ADR:
   1. Add a new row to the appropriate index table using the required schema per `T102-ADR-004-CLAUSE-001`.
   2. Assign the next sequential ID for that scope.
   3. Create a combined ADR+Spec file at the canonical path using the combined-file template, applying DR body structure per CLAUSE-004 under `## Decision` and CLAUSE entries under `## Specification`.
   4. Ensure References follow `T102-ADR-005`.
   5. Populate the Canonical Path column in the index row with the full repo-relative path to the combined file.

4) **T102-ADR-004-CLAUSE-004 (DR Body Template)**
   - **Structure**:
     - **Headings**: Main bold headings (e.g. `* **Context**`) MUST be preceded by two newlines.
     - **Body**: Content MUST start on a new line and INDENTED under the heading with no space in between.
   - **Format**: `* **<ID> (<Title>)** {#<anchor>}`
   - **Required Subheadings**:
     * **Context** [Why this decision is needed; the gap it resolves.]
     * **Decision** [What is adopted/changed and who owns it.]
     * **Alternatives Considered** [Bulleted list of additional options considered with clear rejection rationales.]
     * **Consequences** [Impacts using `(+)`, `(±)`, `(-)` bullets.]
     * **References** [Canonical references/anchors per `T102-ADR-005`.]
     * **Provenance** [Bulleted list of evidence/design source repo-relative paths only.]
   - In combined ADR+Spec files (Model D), the DR body lives under `## Decision`. Specification is a peer `## Specification` section; see CLAUSE-005.

5) **T102-ADR-004-CLAUSE-005 (Specification Clauses)**

   **Purpose**
   Standardize how ADR **Specification** sections are constructed using `CLAUSE` IDs, without duplicating global ID semantics.

   **Normative Reference**
   - `CLAUSE` token type construction and semantics MUST follow `T102-ADR-005-CLAUSE-005D (Specification Clause Semantics)`.

   **Specification Section Structure**
   Within an ADR, the **Specification** section MUST be a list of clause items, each defined as:

   - Format: `n) **<CLAUSE-ID> (<Title>)**`, where `<CLAUSE-ID>` conforms to `T102-ADR-005-CLAUSE-005D`.

   In combined files (Model D), CLAUSEs live under `## Specification`, a peer section to `## Decision` (not nested within the DR body).

   **Clause Requirements**
   - Each clause MUST be a single primary normative statement (avoid compound obligations where feasible).
   - Each `CLAUSE` ID MUST conform to `T102-ADR-005-CLAUSE-005D` (including enforceability and required normative language).
   - If additional detail is required, it SHOULD be provided as subclauses per `T102-ADR-005-CLAUSE-005D`.
   - Clause Titles MUST follow the title conventions defined in `T102-ADR-005-CLAUSE-001`.

   **Ordering**
   - `CLAUSE` IDs MUST be sequential in the order they appear within the ADR Specification section (`001`, `002`, `003`, ...).
   - Subclauses MUST immediately follow their parent clause.

   **Markdown Subclause Rendering**
   - Subclauses SHOULD be rendered as nested bullet items under the parent clause and prefixed by their full CLAUSE-ID (e.g., `<ADR-ID>-CLAUSE-002A`).

   **Referencing**
   - Other artifacts MAY reference specific ADR Specification clauses using the formal format defined in `T102-ADR-005-CLAUSE-004 (Reference Semantics)`, e.g.:
     `Reference:` `T102-ADR-004-CLAUSE-005 (Specification Clauses)`

   **Non-Duplication Constraint**
   - `T102-ADR-004` MUST NOT redefine the syntax, scope validity, or semantic authority of `CLAUSE-IDs`; those are defined in `T102-ADR-005-CLAUSE-005D`.

6) **T102-ADR-004-CLAUSE-006 (Cross-Artifact Linking Patterns)**

   - **STD → Adoption (Adoption Statement).**
     If a STD formally adopts/mandates an ADR or RID, the adoption MUST be stated as the first sentence of the STD body:
     - Pattern: `The project SHALL use <ID>...` or similar normative adoption language declaring the adopted ID.
     - Example: `The project SHALL use `T102-ADR-004`, as the single Client-owned standard...`

   - **ADR → Context (Authority Citation).**
     If an ADR is governed by a STD, the governing policy MUST be cited as the first sentence of **Context**:
     - Pattern: `Per <STD-ID>, <one-line rationale>...`
     - Example: ``Per `T102-STD-004`, a unified DR schema is required to prevent drift.``

   - **Index → Combined File (Canonical Path Linkage).**
     Concept/SPS index tables link to combined files via full repo-relative Canonical Path (per CLAUSE-001); Phase 1 links at file granularity.

7) **T102-ADR-004-CLAUSE-007 (Anchor Title Stability)**

   - Anchors MUST be lower-kebab derived from the Title.
   - Anchors MUST remain stable across file moves/splits.
   - If Title changes, keep the old anchor unless an explicit migration is performed.
   - Phase 1 stability contract: combined-file names and canonical paths MUST NOT change in Phase 1. Anchors extracted from Concept remain stable within their combined file.

8) **T102-ADR-004-CLAUSE-008 (Lifecycle Coherence)**

   When a STD cited by ADRs changes **Status** or is **Superseded**, affected ADRs MUST:
   - update the **Context** authority sentence to the new governing STD ID/title; and
   - add the prior STD ID to **Supersedes/References** as appropriate; and
   - perform this update in the next modification to the ADR or in a dedicated "governance sync" change set.

9) **T102-ADR-004-CLAUSE-009 (Status Management)**

   - Lifecycle: `Proposed → Accepted → Deprecated`
   - Superseded IDs MUST be captured in the **Supersedes** column and, where applicable, referenced in body text.
   - For specification lifecycle stages governing CLAUSE content evolution, see CLAUSE-017.

10) **T102-ADR-004-CLAUSE-010 (Precedence Conflicts Hierarchy)**

    For conflict resolution across DRIDs:
    `Initiative STD > Initiative ADR > Epic ADR > Feature ADR > Story ADR`

    See `T102-ADR-003` and `T102-ADR-005` for full hierarchy and directionality constraints.

11) **T102-ADR-004-CLAUSE-011 (Consequences Scope Requirements)**

    - **STD Consequences** SHOULD cover: policy/precedence impacts; compliance expectations; migration/rollout; automation/traceability effects.
    - **ADR Consequences** SHOULD cover: quality trade-offs; constraints introduced; operational effects; debt/risks.

12) **T102-ADR-004-CLAUSE-012 (References & Provenance)**

    - **References** MUST use the formal reference style defined in `T102-ADR-005`.
    - **Provenance** MUST list relevant repo-relative paths (no raw URLs).

13) **T102-ADR-004-CLAUSE-013 (Variance ADR Contract)**

    A "Variance ADR" is required when a downstream artifact MUST deviate from an upstream standard. It MUST include:
    - **Variance From:** list of overridden upstream IDs.
    - **Rationale:** technical/environment justification.
    - **Scope Impact:** what inheritance/automation breaks.
    - **Lifecycle:** MUST be `Accepted` via governance sign-off (Client or delegated authority).

14) **T102-ADR-004-CLAUSE-014 (Decision Promotion Workflow)**

    Decision records SHOULD follow a staged lifecycle:
    1. **Research (RES)** — Use `RES-SID` to commission and document evidence, options, and empirical findings for a specific scope (Initiative/Epic/Feature).
    2. **Implementation Guidance (IG)** — Encode candidate implementation patterns at the appropriate scope (typically Feature); IGs MAY evolve as research is refined.
    3. **Decision Records (STD/ADR)** — Promote stable, cross-cutting, or long-lived patterns into formal STD/ADR records when:
        - (a) The pattern affects multiple artifacts or features; or
        - (b) The pattern requires explicit governance (ownership, status, supersedes) beyond implementation detail.
    4. **Traceability** — ADR Specifications SHOULD reference governing research and guidance in **Provenance** and **References**, rather than duplicating detailed patterns.
    5. **Scope Guidance** —
        - Epic-level ADRs SHOULD be used for cross-feature decisions (e.g., shared vocabularies, common JSON architectures).
        - Feature-level ADRs SHOULD be reserved for significant, feature-local architectural decisions that cannot reasonably be governed at Epic scope.
        - Routine implementation details MAY remain in guidance without a dedicated ADR.

15) **T102-ADR-004-CLAUSE-015 (Automation & Linting Checks)**

    Authors SHOULD pass these checks:
    - STD body contains an **Adoption** statement matching normative patterns.
    - ADR body **Context** starts with:
      `` `^Per\s+`T[0-9]{3,}(?:[A-Z][0-9A-Z]*)?-STD-[0-9]{3}`,\s+.+$` ``
    - Combined file contains `## Decision` and `## Specification` headings in that order.
    - Every `Canonical Path` in an index resolves to an existing file.

16) **T102-ADR-004-CLAUSE-016 (Combined-File Dual Nature)**
    - In Phase 1, the `ADR` token denotes a combined Decision Record + Normative Specification file.
    - `## Decision` contains stable rationale content (Context, Decision, Alternatives Considered,
      Consequences, References, Provenance).
    - `## Specification` contains evolving normative content (CLAUSEs using enforceable language:
      SHALL, SHOULD, MUST, MAY).
    - The `ADR` token is retained for Phase 1 per the Model D stability contract; Phase 2 MAY
      introduce separate `SPEC` or `STD` artifact types.
    - Every combined ADR+Spec file MUST contain both `## Decision` and `## Specification` headings
      in that order.

17) **T102-ADR-004-CLAUSE-017 (Specification Lifecycle & Authority Chain)**

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
