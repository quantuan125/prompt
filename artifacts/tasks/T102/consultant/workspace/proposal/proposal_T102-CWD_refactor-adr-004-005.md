---
artifact_type: 'PROPOSAL'
initiative_id: 'T102'
epic_id: 'T102-CONSULTANT'
version: '1.2.0'
date: '2026-01-21'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
---

# PROPOSAL: Refactor T102-ADR-004 and T102-ADR-005 (Golden Standards)

## I. PURPOSE
This proposal merges and harmonizes two refactor proposals into a single, copy/paste-ready artifact:
- `T102-ADR-004 (Decision Records Index)` refactor proposal
- `T102-ADR-005 (ID Specification & Rules)` refactor proposal

This merged proposal is intended to:
1) analyze the current `T102-ADR-004` and `T102-ADR-005` rule sets as implemented in `prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md`; and
2) propose refactors for both ADRs as “golden standards” going forward.

## II. CONTEXT & APPROACH
### Source Materials (Inputs, Not Modified)
- Current baseline (Concept ADR compendium):
  - `prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md`
    - `T102-ADR-004 (Decision Records Index)` body
    - `T102-ADR-005 (ID Specification & Rules)` body
- Existing standalone refactor proposals (kept unchanged):
  - `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CONSULTANT_refactor-adr-004.md`
  - `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CONSULTANT_refactor-adr-005.md`

### Merge Constraints (Authoring Rules)
1) The two existing proposal files remain unchanged.
2) Light rewriting is allowed outside each ADR’s **Draft Specification**.
3) Within each ADR’s **Draft Specification**:
   - remove `###` prefixes from rule-entry headings so each entry begins with `1)`, `2)`, etc.;
   - indent rule bodies so they are “tabbed under” the rule ID line (copy/paste-ready for Concept ADR **Specification** sections);
   - do not rewrite rule content beyond formatting-only changes;
   - remove the duplicated ADR-004 “13)” block (keep the more detailed version).

---

## III. PROBLEM STATEMENT

### T102-ADR-004 (Decision Records Index)
Current `T102-ADR-004` implementation suffers from schema drift across different artifacts (SPS/Request/Concept) and a blurry interface between Governance Policies (GDR) and Technical Decisions (ADR). There is also no formal contract for "Variance ADRs" when a feature must deviate from a standard.

### T102-ADR-005 (ID Specification & Rules)
Current `T102-ADR-005` definitions are overly verbose and repetitive. Specifically:
1.  **Redundant Taxonomy**: `FR-002 (Types)` and `FR-004 (Categories)` split closely related definitions (High-level types vs specific tokens) into separate, overlapping lookups.
2.  **Scattered Construction Rules**: ID patterns are split between `FR-001 (Scope)` and `FR-005 (Construction)`, making it harder to verify a single ID's validity.
3.  **Verbose Reference Rules**: `FR-006` describes reference logic with excessive prose.

---

## IV. BASELINE ANALYSIS (CURRENT IN `concept_T102-CONSULTANT.md`)

### T102-ADR-004 (Decision Records Index)
Observed patterns and gaps in the current `T102-ADR-004` body:
- The Concept baseline expresses ADR-004 specification clauses as `...-FR-###` items (legacy governance-clause labeling), while the refactor proposal formalizes `...-CLAUSE-###` clause semantics and cross-links to ADR-005’s `CLAUSE` semantics for precision.
- The baseline includes automation/linting guidance but does not define a variance ADR contract with explicit required fields (variance-from / rationale / scope impact / governance acceptance).
- Adoption/citation patterns (GDR adoption sentence / ADR authority sentence) exist but benefit from being standardized as normative patterns (to make automation and reviews reliable).
- There are known “copy/paste hazards” in downstream authoring due to inconsistent anchor/placement conventions and informal drift across artifacts.

### T102-ADR-005 (ID Specification & Rules)
Observed patterns and gaps in the current `T102-ADR-005` body:
- The Concept baseline defines scope, types, categories, and construction across many separate FR clauses, increasing cross-referencing overhead during authoring and review.
- The baseline uses `...-FR-###` as internal governance clause labels; the refactor proposal formalizes consolidated `...-CLAUSE-###` governance clauses and introduces explicit `CLAUSE` semantics for ADR **Specification** subclauses (to support precise cross-document traceability).
- Special-case logic (ASSUM lifecycle, INT exceptions, ISSUE/RISK constraints) is present but would benefit from consolidation into fewer, clearer rules while preserving enforceability.

---

## V. PROPOSED CHANGES

### T102-ADR-004 (Decision Records Index)
1. **Unified Index Schema**: Consolidate GDR and ADR indexing into a shared schema to enable universal automation and cross-referencing.
2. **Normative Adoption Logic**: Establish a formal "Adoption Statement" for GDRs to mandate RIDs (Requirements) or ADRs (Technically chosen paths), ensuring clear authority tracking.
3. **Variance ADR Contract**: Define a strict template for Variances to ensure deviations are documented with rationale, impact assessment, and explicit client approval.
4. **Decision Promotion Lifecycle**: Formalize the flow from Research (`RES`) to Implementation Guidance (`IG`) to formal Decision Records (`GDR/ADR`).

### T102-ADR-005 (ID Specification & Rules)
We propose reducing the 11 FRs to 7 consolidated rules without losing agentic precision:
1. **Consolidate Scope & Construction** (`FR-001` + `FR-005` -> `FR-001`): Combine regex patterns and markdown construction rules into a single "Identity & Schema" rule.
2. **Merge Taxonomy** (`FR-002` + `FR-004` -> `FR-002`): Merge "ID Types" and "Category Tokens" into a single lookup table mapping Token -> Category -> ID Type.
3. **Simplify Special Handling** (`FR-008, 009, 010` -> `FR-005`): Group all category-specific logic (Assumptions, Integration notes, Issues/Risks) into a consolidated "Semantics" rule.

---

## VI. DRAFT SPECIFICATIONS 

### Notes on Migration
- The Draft Specifications below are intentionally formatted to be copy/paste-ready into the **Specification** sections in `concept_T102-CONSULTANT.md`.
- Clause lines start with `* **<ID>...**`; clause bodies are tabbed under the clause line.
- ADR-004 contains the consolidated "Variance ADR Contract" (merged from duplicate proposals).
- ADR-005 implements the consolidated 7-rule set.

### T102-ADR-004 (Decision Records Index)

* **T102-ADR-004 (Decision Records Index) {#t102-adr-004-drs-index}**

  **Context.** Per `T102-GDR-004 (Decision Records Standard)`, GDR/ADR schemas and anchors vary across artifacts, causing drift and blocking automation.

  **Decision.** Implement a unified decision record index: one table schema, shared body subheadings, and consistent anchors/links across SPS/Request/Concept/Design.

  **Specification**
    * **T102-ADR-004-CLAUSE-001 (DR Index Schemas)**
      - **GDR Index Schema**  
        `GDR ID | **Title** | Status | Owner | Effective | Supersedes | Anchor`

      - **ADR Index Schema**  
        `ADR ID | **Title** | Paired GDR | Status | Owner | Effective | Supersedes | Anchor`

      - **Column Definitions**
        1. `ID`: ID construction MUST follow `T102-ADR-005` following general format: `<SID>-<GDR/ADR>-###`
        2. `Title`: Title Case, 2–3 words.
        3. `Paired GDR` (ADR only): governing GDR ID (or `—` if none).
        4. `Status`: `{Proposed, Accepted, Deprecated}`.
        5. `Owner`: governance authority (typically `Client`) or implementation owner; if unknown use `—`.
        6. `Effective`: ISO-8601 date `YYYY-MM-DD`.
        7. `Supersedes`: list of superseded IDs or `—`.
        8. `Anchor`: lower-kebab anchor derived from Title; stable.

    * **T102-ADR-004-CLAUSE-002 (Placement Standards)**
      - **SPS artifacts**: section titled `"<SCOPE> Governance Decisions"` containing governance decisions only.
      - **Concept artifacts**: section titled `"<SCOPE> Architectural Decisions"` with mirror subsections for Epic/Feature areas as needed.
      - **Consistency requirement**: placement MUST follow established artifact section numbering without local deviations.

    * **T102-ADR-004-CLAUSE-003 (Entry Creation Workflow)**
      To create a new GDR/ADR:
      1. Add a new row to the appropriate index table using the required schema per `T102-ADR-004-CLAUSE-001`.
      2. Assign the next sequential ID for that scope.
      3. Create the matching body entry below the index using `T102-ADR-004-CLAUSE-004` structure.
      4. Ensure References follow `T102-ADR-005`.

    * **T102-ADR-004-CLAUSE-004 (DR Body Template)**

      - **Structure**:
        - **Headings**: Main bold headings (e.g. `* **Context**`) MUST be preceded by two newlines.
        - **Body**: Content MUST start on a new line, tabbed (indented) under the heading with no space in between.
      - **Format**: `* **<ID> (<Title>) {#<anchor>}**`
      - **Required Subheadings**:
        
        * **Context**
          - Why this decision is needed; the gap it resolves.
        
        * **Decision**
          - What is adopted/changed and who owns it.
        
        * **Consequences**
          - Impacts using `(+)`, `(±)`, `(-)` bullets.
        
        * **References**
          - Canonical references/anchors per `T102-ADR-005`.
      - **ADR additions** (ADR only):
        
        * **Specification**
          - Clause list using `CLAUSE` token type or software requirement clauses (if used in that ADR).
        
        * **Alternatives Considered**
          - Rejected options with rationale.
        
        * **Provenance**
          - Evidence/design source repo-relative paths only.

    * **T102-ADR-004-CLAUSE-005 (Specification Clauses)**

      **Purpose**  
      Standardize how ADR **Specification** sections are constructed using `DRCIDs`, without duplicating global ID semantics.

      **Normative Reference**
      - `CLAUSE` token type construction and semantics MUST follow `T102-ADR-005-CLAUSE-005D (Specification Clause Semantics)`.

      **Applicability**
      - This rule applies to **ADR only** (not GDR).

      **Specification Section Structure**
      Within an ADR body, the **Specification** subsection MUST be a list of clause items, each defined as:

      - Format: `n) **<DRCID> (<Title>)**`, where `<DRCID>` conforms to `T102-ADR-005-CLAUSE-005D`. 

      **Clause Requirements**
      - Each clause MUST be a single primary normative statement (avoid compound obligations where feasible).
      - Each DRCID clause MUST conform to `T102-ADR-005-CLAUSE-005D` (including enforceability and required normative language).
      - If additional detail is required, it SHOULD be provided as DRCID subclauses per `T102-ADR-005-CLAUSE-005D`.
      - Clause Titles MUST follow the title conventions defined in `T102-ADR-005-CLAUSE-001`.

      **Ordering**
      - CLAUSE-IDs MUST be sequential in the order they appear within the ADR Specification section (`001`, `002`, `003`, ...).
      - Subclauses MUST immediately follow their parent clause.

      **Markdown Subclause Rendering**
      - Subclauses SHOULD be rendered as nested bullet items under the parent clause and prefixed by their full DRCID (e.g., `<ADR-ID>-CLAUSE-002A`).

      **Referencing**
      - Other artifacts MAY reference specific ADR Specification clauses using the formal format defined in `T102-ADR-005-CLAUSE-004 (Reference Semantics)`, e.g.:  
        `Reference:` `T102-ADR-004-CLAUSE-005 (Specification Clauses)`

      **Non-Duplication Constraint**
      - `T102-ADR-004` MUST NOT redefine the syntax, scope validity, or semantic authority of `DRCIDs`; those are defined in `T102-ADR-005-CLAUSE-005D`.

    * **T102-ADR-004-CLAUSE-006 (Cross-Artifact Linking Patterns)**

      - **GDR → Decision (Adoption Statement).**  
        If a GDR formally adopts/mandates an ADR or RID, the adoption MUST be stated as the first sentence of **Decision**:  
        - Pattern: `Adopt <ID>, <one-line rationale>...`  
        - Example: `Adopt `T102-ADR-004`, as the single Client-owned standard for DR schemas across artifacts.`

      - **ADR → Context (Authority Citation).**  
        If an ADR is governed by a GDR, the governing policy MUST be cited as the first sentence of **Context**:  
        - Pattern: `Per <GDR-ID>, <one-line rationale>...`  
        - Example: ``Per `T102-GDR-004`, a unified DR schema is required to prevent drift.``

    * **T102-ADR-004-CLAUSE-007 (Anchor Title Stability)**

      - Anchors MUST be lower-kebab derived from the Title.
      - Anchors MUST remain stable across file moves/splits.
      - If Title changes, keep the old anchor unless an explicit migration is performed.

    * **T102-ADR-004-CLAUSE-008 (Lifecycle Coherence)**

      When a GDR cited by ADRs changes **Status** or is **Superseded**, affected ADRs MUST:
      - update the **Context** authority sentence to the new governing GDR ID/title; and
      - add the prior GDR ID to **Supersedes/References** as appropriate; and
      - perform this update in the next modification to the ADR or in a dedicated “governance sync” change set.

    * **T102-ADR-004-CLAUSE-009 (Status Management)**

      - Lifecycle: `Proposed → Accepted → Deprecated`
      - Superseded IDs MUST be captured in the **Supersedes** column and, where applicable, referenced in body text.

    * **T102-ADR-004-CLAUSE-010 (Precedence Conflicts Hierarchy)**

      For conflict resolution across DRIDs:
      `Initiative GDR > Initiative ADR > Epic ADR > Feature ADR > Story ADR`

      See `T102-ADR-003` and `T102-ADR-005` for full hierarchy and directionality constraints.


    * **T102-ADR-004-CLAUSE-011 (Consequences Scope Requirements)**

      - **GDR Consequences** SHOULD cover: policy/precedence impacts; compliance expectations; migration/rollout; automation/traceability effects.
      - **ADR Consequences** SHOULD cover: quality trade-offs; constraints introduced; operational effects; debt/risks.


    * **T102-ADR-004-CLAUSE-012 (References & Provenance)**

      - **References** MUST use the formal reference style defined in `T102-ADR-005`.
      - **Provenance** MUST list relevant repo-relative paths (no raw URLs).


    * **T102-ADR-004-CLAUSE-013 (Variance ADR Contract)**

      A “Variance ADR” is required when a downstream artifact MUST deviate from an upstream standard. It MUST include:
      - **Variance From:** list of overridden upstream IDs.
      - **Rationale:** technical/environment justification.
      - **Scope Impact:** what inheritance/automation breaks.
      - **Lifecycle:** MUST be `Accepted` via governance sign-off (Client or delegated authority).


    * **T102-ADR-004-CLAUSE-014 (Decision Promotion Workflow)**

      Decision records SHOULD follow a staged lifecycle:
      1. **Research (RES)** — Use `RES-SID` to commission and document evidence, options, and empirical findings for a specific scope (Initiative/Epic/Feature).
      2. **Implementation Guidance (IG)** — Encode candidate implementation patterns at the appropriate scope (typically Feature); IGs MAY evolve as research is refined.
      3. **Decision Records (GDR/ADR)** — Promote stable, cross-cutting, or long-lived patterns into formal GDR/ADR records when:
          - (a) The pattern affects multiple artifacts or features; or
          - (b) The pattern requires explicit governance (ownership, status, supersedes) beyond implementation detail.
      4. **Traceability** — ADR Specifications SHOULD reference governing research and guidance in **Provenance** and **References**, rather than duplicating detailed patterns.
      5. **Scope Guidance** —
          - Epic-level ADRs SHOULD be used for cross-feature decisions (e.g., shared vocabularies, common JSON architectures).
          - Feature-level ADRs SHOULD be reserved for significant, feature-local architectural decisions that cannot reasonably be governed at Epic scope.
          - Routine implementation details MAY remain in guidance without a dedicated ADR.


    * **T102-ADR-004-CLAUSE-015 (Automation & Linting Checks)**

      Authors SHOULD pass these checks:
      - GDR body contains a **Decision** line matching:  
        `` `^Adopt\s+`T[0-9]{3,}(?:[A-Z][0-9A-Z]*)?-ADR-[0-9]{3}`,\s+.+$` ``
      - ADR body **Context** starts with:  
        `` `^Per\s+`T[0-9]{3,}(?:[A-Z][0-9A-Z]*)?-GDR-[0-9]{3}`,\s+.+$` ``

  **Alternatives Considered.**
  (a) Combine GDR & ADR in a single DR index — rejected.

  **Consequences.**
  (+) One schema and body pattern; shared tooling and easier authoring
  (+) Stable anchors enable automation and cross-referencing
  (+) Clear governance vs. implementation separation with ADR additions
  (±) Migration effort for existing non-conforming records
  (-) Ongoing upkeep for instructional guidelines/examples

  **References.** 
  `T102-GDR-004 (Decision Records Standard)`, 
  `T102-IG-007 (ID Standard)`, 
  `T102-IG-008 (Decision Logging)`, 
  `T102-IG-009 (Traceability Framework)`, 
  `T102-GDR-001 (Consultancy Operating Model Standard)`

  **Provenance.** 
  - `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_refactor-adr-004-005.md`

### T102-ADR-005 (ID Specification & Rules)

* **T102-ADR-005 (ID Specification & Rules) {#t102-adr-005-id-spec}**

  **Context.** Per `T102-GDR-005 (ID Governance Standard)`, multiple artifact families use overlapping ID conventions (considerations, requirements, decisions) at different scopes. Without a single normative spec, authors improvise category tokens, anchors, and references, creating inconsistency and undermining inheritance, precedence, and verification.

  **Decision.** Standardize ID patterns across Initiative, Epic, Feature, and Story scopes; define category tokens, sub-ID patterns, anchors, and referencing rules. This ADR is the single specification adopted by `T102-GDR-005` as policy.

  **Specification**

    * **T102-ADR-005-CLAUSE-001 (Canonical ID Schema)**

      **Regex Patterns**: usage of all IDs SHALL match one of these two patterns: 
      - **Pattern 1 (Scope ID / SID)**: `^T\d{3}(?:[A-Z]\d*)?(?:-[A-Z0-9_]+)*$`
        - Examples: `T102`, `T102A`, `T102A1-S3`, `T102A-SPSST`
      - **Pattern 2 (Tokenized ID)**: `^T\d{3}(?:[A-Z]\d*)?(?:-[A-Z0-9_]+)*-[A-Z]+-\d{3}$`
        - Examples: `T102-QG-001`, `T102A1-NFR-005`, `T102A-SPSST-IG-002`

      **Markdown Construction**:
      - Format: `* **<ID> (<Title>)** — <Description>`
      - Title Constraints:
        - **RIDs / IIDs / OIDs**: Target: 2 words; Min: 2 words; Max: 3 words.
        - **DRIDs / DRCIDs**: Target: 2–4 words; Min: 2 words; Max: 8 words.
        - Hyphenated compounds count as 1 word.
      - Description: concise statement of the rule/requirement/decision/guidance.

    * **T102-ADR-005-CLAUSE-002 (Taxonomy & Terminology)**

      **Category Key**:
      - `SID` (Scope)
      - `RESID` (Research)
      - `RID` (Requirement)
      - `DRID` (Decision Record)
      - `DRCID` (Decision Record Clause)
      - `IID` (Implementation)
      - `OID` (Other)

      **Allowed Scope Key**:
      - `I` (Initiative), 
      - `E` (Epic), 
      - `F` (Feature), 
      - `S` (Story)

      Valid tokens are strictly defined by this table. Authors MUST select the most specific token available for the scope.

      | Category | Token | Name | Allowed Scope | Definition & Usage |
      |:---|:---|:---|:---|:---|
      | `SID` | `SCOPE` | **Project Management Scope** | I, E, F, S | Artifact Identifiers (e.g., `T102`, `T102A`, `T102A1-S3`). |
      | `RESID` | `RES` | **Research** | I, E, F | Commissioned research trace (Evidence). |
      | `RID` | `ASSUM` | **Assumption** | I, E, F | Unverified belief carrying risk. Must track validation status. |
      | `RID` | `CON` | **Constraint** | I, E, F | Non-negotiable boundary or limitation. |
      | `RID` | `QG` | **Quality Goal** | I, E | Initiative success metrics (e.g., traceability completeness, review turnaround). |
      | `RID` | `DEP` | **Dependency** | I, E | External condition, interface, asset, or approval required. |
      | `RID` | `IF` | **Interface** | I, E, F | Data/integration contract definition (contractual boundary). |
      | `RID` | `FR` | **Functional Requirement** | F, S | Testable system behavior (requirements language). |
      | `RID` | `NFR` | **Non-Functional Requirement** | F, S | Quality requirement expressed as testable metrics. |
      | `DRID` | `GDR` | **Governance Decision** | I, E, F | Policy-level decision record. Governs/frames downstream decisions. |
      | `DRID` | `ADR` | **Architectural Decision** | I, E, F, S | Technical implementation decision record. |
      | `DRCID` | `CLAUSE` | **Decision Record Clause** | I, E, F, S | ADR-internal clause ID used only within the parent ADR. Scope and authority derive from the parent ADR only; rendering is defined by `T102-ADR-004-CLAUSE-005`. |
      | `IID` | `IG` | **Implementation Guidance** | I, E, F | Normative implementation standards/guidance: patterns, templates, examples. May be enforced via lint/review. Not a substitute for system requirements. |
      | `IID` | `INT` | **Integration Notes** | E, F, S | Non-normative integration notes and cross-scope coordination guidance for external audiences; may carry compatibility expectations. |
      | `OID` | `NOTE` | **Note** | I, E, F, S | Non-normative context; do not use for obligations. |
      | `OID` | `ISSUE` | **Issue** | I, E, F | Known gap requiring resolution. |
      | `OID` | `RISK` | **Risk** | I, E, F | Potential negative event requiring mitigation. |

    * **T102-ADR-005-CLAUSE-003 (Precedence & Hierarchy)**

      **Directionality**: Inheritance flows downstream with scopes only.
      - Correct: Feature references Epic; Epic references Initiative.
      - Incorrect: Epic references Feature (except `INT` exception defined in `T102-ADR-005-CLAUSE-005C`).

      **Precedence Order** (Highest to Lowest):
      - Initiative > Epic > Feature > Story

      **Category Precedence** (within same scope):
      `SID > RESID > RID > DRID (GDR > ADR) > DRCID > IID (IG > INT) > OID`

      **Evidence Conflict Rule**:
      If `RESID` contradicts a `RID` or `DRID`, it triggers a Review workflow (ISSUE + Change Decision). Evidence does not “silently override” obligations.

      **Variances**:
      Any downstream ID deviating from an upstream rule MUST cite the overridden ID explicitly in a “Variance ADR”.


    * **T102-ADR-005-CLAUSE-004 (Reference Semantics)**

      **Styles**:
      - **Short-hand (Inline):** `` `ID` `` (e.g., `T102-QG-001`, `T102B`)
      - **Full (Formal):** `` `ID (Title)` `` (e.g., `T102-QG-001 (Client Readability)`, `T102B (REQUEST)`)

      **Required Usage**:
      - In-body prose (within ID bodies): Short-hand preferred
      - Dedicated sections (References, Tables): Full references required

      **External Reference Line**:
      If a body references an ID from a different scope prefix (e.g., `T102A` body referencing `T102B-...`), add a standalone line at the bottom:
      - `` `Reference:` `ID (Title)` ``  followed by one or more full references. (e.g. `Reference:` `T102B-CON-001 (Decision Storage Boundary)`)

      **Constraint**:
      Normative bodies MUST NOT reference `ISSUE` or `RISK` IDs inline. Issues/Risks capture the problem; RIDs/DRIDs capture the solution.

    * **T102-ADR-005-CLAUSE-005 (Category Semantics)**

      This clause provides a concise semantic overview. Tokens with lifecycle/exception behavior have dedicated subclauses. 

      * **T102-ADR-005-CLAUSE-005A (Assumption Lifecycle)**

        **Table Requirement**:
        Assumptions MUST be defined in a table structure preceding the list of ID bodies.

        **Schema**:
        `| ID | **Title** | Status | Validation Method | Timing | Owner | If Invalidated | CON Cross-Ref |`

        **Enum**:
        - Status: `{Pending, Validated, Invalidated, Modified}`

        **Lifecycle Requirements**:
        - Each ASSUM SHOULD specify a testable validation method and responsible party.
        - Each ASSUM SHALL specify an invalidation response using one of:
          - `Fallback`, `Escalation`, `Mitigation` (short, actionable)
        - “Invalidated” assumptions trigger an automatic Issue or Scope Change logic (ISSUE + Change Decision).

      * **T102-ADR-005-CLAUSE-005B (Implementation Guidance Rules)**

        **Normative Standard**:
        - IG MAY use MUST/SHALL when defining implementation and authoring standards intended to be enforceable.
        - IG MUST NOT be used to express software behavior requirements; use `FR`/`NFR`/`CON` for system requirements.

        **Role**:
        - Detailed patterns, pseudo-code, templates, examples, and internal process guidance.
        - Expands on governing RIDs/DRIDs with implementable standards without duplicating upstream requirements text.

        **Scope Granularity**:
        - **Initiative/Epic Scope**: Focus on high-level patterns, templates, and principles.
        - **Feature/Story Scope**: Focus on specific implementation details, code examples, and procedural steps.

      * **T102-ADR-005-CLAUSE-005C (Integration Notes Rules)**

        **Role**:
        - External-facing integration notes and cross-scope coordination guidance.
        - May include compatibility expectations and versioning considerations (as guidance), but not normative obligations.

        **Non-Normative Constraint**:
        - INT MUST NOT use MUST/SHALL language to impose requirements.
        - INT MAY use SHOULD/MAY language for recommendations.
        - Mandatory behavior MUST be captured via `RID` or adopted via `DRID`.

        **Scoped Exception**:
        At Feature/Story scope, INT items MAY reference other peer Feature RIDs directly for integration coordination. This is a scoped exception to upstream-only directionality.

        **Governance Loop**:
        If an INT pattern is widely adopted or becomes policy, it SHOULD be promoted into Epic-level `RID` (e.g., `IF/CON`) and/or captured as an `ADR`, and the originating INT SHOULD be updated to reference the promoted governance.

      * **T102-ADR-005-CLAUSE-005D (Specification Clause Semantics)**

        **Role**  
        Define the allowed construction, subclause construction, and semantics of `CLAUSE` (DRCID) IDs used for ADR-internal specification clauses.

        **Construction**
        - Format: `<ADR-ID>-CLAUSE-###`. e.g. `T102-ADR-004-CLAUSE-004`
        - `###` is a 3-digit sequence local to the parent ADR (starts at `001`).
        - Optional subclause suffix: `<ADR-ID>-CLAUSE-###<CAPITAL_LETTER>`. e.g. `T102-ADR-004-CLAUSE-004A`

        **Semantics**
        - `CLAUSE` (DRCID) IDs represent **enforceable Specification clauses** within an ADR and MUST be written as normative statements (`MUST`/`SHALL`).
        - Non-normative guidance MUST use `IG`/`INT`/`NOTE` (not `CLAUSE`).
        - A `CLAUSE` ID has **no independent precedence** outside its parent ADR:
          - `Authority(<ADR-ID>-CLAUSE-###) = Authority(<ADR-ID>)`

        **Scope & Validity Constraints**
        - `CLAUSE` IDs MUST NOT be created as standalone items outside an ADR body.
        - `CLAUSE` IDs MUST NOT be used to represent system requirements or non-normative guidance.
        - References to `CLAUSE` IDs MUST follow `T102-ADR-005-CLAUSE-004 (Reference Semantics)` and MAY be used for precise cross-document traceability.
        - Rendering of ADR **Specification** sections (including ordered-list and subclause formatting) MUST follow `T102-ADR-004-CLAUSE-005 (Specification Clauses)`.

      * **T102-ADR-005-CLAUSE-005E (Notes Structure Semantics)**
        **Notes Structure Schema**
        - Location: SPS "Research & Notes" → "Notes" subheading.
        - Structure: List item per NOTE beginning with `**<SID>-NOTE-### (<Title>)** — <body>` on a single line.
        - Body: Optional short paragraphs may follow for context; target ≤200 words total per NOTE.
        - Style: Non‑normative and descriptive; do not restate formal rules or research verbatim; use back‑ticked IDs to reference GDR/ADR/RES where helpful.
        - Conformance: Mirrors existing examples in SPS Section III.B.7.

        **Notes Authoring Guidelines**
        - Purpose: Capture lightweight, non‑commissioned insights aiding authoring and reader orientation without introducing governance or architectural decisions.
        - When to add a NOTE: contextual clarifications, philosophy, industry references, or early observations prior to commissioning research.
        - When NOT to use a NOTE: to summarize commissioned research (use RES with Brief/Report), to encode enforceable rules (use GDR/ADR), or to duplicate upstream content (link via back‑ticked IDs instead).
        - Discipline: Keep short (≤200 words), scannable, and link‑don’t‑duplicate. If NOTE content becomes critical or frequently referenced, promote to `RES` (with brief/report) or to `GDR/ADR` as appropriate. Maintain sequential NOTE numbering without retroactively altering meaning.

      * **T102-ADR-005-CLAUSE-006 (Content Quality)**

      **Quality Criteria**:
      - **RID**: Lead with a requirement statement when applicable (SHALL/SHOULD). No justification prose (put rationale in NOTE). Prefer one primary obligation per RID.
      - **IID-IG**: Normative implementation standards/guidance; may include templates, pseudo-code, examples; enforced via lint/review where feasible.
      - **IID-INT**: Non-normative integration notes; MUST NOT introduce new obligations (see `T102-ADR-005-CLAUSE-005C`).
      - **DRID**: Follow `T102-ADR-004` body structure strictly.

      **Governance Mapping**:
      In governance-focused artifacts, inner clauses SHOULD be named `CLAUSE` (e.g., `T102-ADR-005-CLAUSE-001`) to prevent confusion with Software Functional Requirements (`FR`). Legacy `...-FR-###` clause IDs inside governance ADRs are treated as clause IDs during migration.

      **Conciseness**:
      RIDs target <200 words when feasible (excluding tables); IF schemas may exceed for clarity.

    * **T102-ADR-005-CLAUSE-007 (ID Stability & Immutability)**

      - **Anchor Stability**: Anchors MUST remain stable even if Titles change slightly.
      - **Immutable IDs**: Once assigned, an ID is never reused. Deprecate it instead.
      - **Migration Tolerance**: Validators MAY allow legacy governance clause labels (e.g., `...-FR-###` inside governance ADRs) alongside `...-RULE-###` during migration, but new governance clauses SHOULD use `CLAUSE`.

  **Alternatives Considered.**
  - Free-form, template-local ID schemes — rejected.
  - Enforcing full titles in all inline mentions — rejected.

  **Consequences.**
  (+) Predictable, machine-checkable IDs across artifacts.
  (+) Faster audits and safer cross-linking with stable anchors.
  (±) Requires discipline and small refactors for legacy items.

  **References.** 
  `T102-GDR-005 (ID Governance Standard)`, 
  `T102-ADR-003 (Explicit Inheritance Model)`, 
  `T102-ADR-004 (Decision Records Index)`, 
  `T102-ADR-006 (Research Artifacts Index)`

  **Provenance.** 
  - `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_refactor-adr-004-005.md`

---

## VII. SUCCESS CRITERIA
* **Structure Alignment**: Shared ## headings apply to both ADR-004 and ADR-005.
* **Semantic Preservation**: Core rules and specifications are unchanged.
* **Clarity**: Duplicated authoring notes and problem statements are unified.
* **Migration Readiness**: Draft Specifications remain copy/paste ready for SSOT updates.