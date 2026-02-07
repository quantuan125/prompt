---
artifact_type: 'CONCEPT'
initiative_id: 'T102'
initiative_code: 'CONSULTANT'
version: '1.1.0'
date: '2026-01-09'
status: 'review'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
---

## III. CORE CONTENT

### A. Identity & Operating Rules
<!--
- Canonical header + links to governing GDRs/ADRs (inheritance table: "link-don't-duplicate").  <!-- T102-GDR-002/003/004/005
- Scope & boundaries (what lives in SPS vs Request vs Design); change log.
-->

### B.  Decision System (ADR Compendium)

#### 1. Initiative ADR Index

| ADR ID | Title | Authority STD | Status | Owner | Effective | Supersedes | Canonical Path |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `T102-ADR-001` | Consultancy Operating Model | — | Proposed | Client | 2025-09-18 | — | `prompt/artifacts/tasks/T102/consultant/standards/T102-ADR-001_consultancy-operating-model.md` |
| `T102-ADR-002` | Canonical YAML Header | — | Proposed | Client | 2025-09-14 | — | `prompt/artifacts/tasks/T102/consultant/standards/T102-ADR-002_canonical-yaml-header.md` |
| `T102-ADR-003` | Explicit Inheritance Model | — | Proposed | Client | 2025-09-14 | — | `prompt/artifacts/tasks/T102/consultant/standards/T102-ADR-003_explicit-inheritance-model.md` |
| `T102-ADR-004` | **Decision Records Index** | `T102-STD-004` | Proposed | Client | — | — | `prompt/artifacts/tasks/T102/consultant/standards/T102-ADR-004_decision-records-index.md` |
| `T102-ADR-005` | **ID Specification & Rules** | `T102-STD-005` | Proposed | Client | — | — | `prompt/artifacts/tasks/T102/consultant/standards/T102-ADR-005_id-specification-rules.md` |
| `T102-ADR-006` | Research Artifacts Index | — | Proposed | Client | 2025-10-12 | — | `prompt/artifacts/tasks/T102/consultant/standards/T102-ADR-006_research-artifacts-index.md` |
| `T102-ADR-007` | Issues & Risks Index | — | Proposed | Client | 2026-01-01 | — | `prompt/artifacts/tasks/T102/consultant/standards/T102-ADR-007_issues-risks-index.md` |
| `T102-ADR-008` | Organisation Baseline Index | — | Proposed | Client | 2026-01-12 | — | `prompt/artifacts/tasks/T102/consultant/standards/T102-ADR-008_organisation-baseline-index.md` |
| `T102-ADR-009` | Governance Standards Specification | `T102-STD-009` | Proposed | Client | — | — | `prompt/artifacts/tasks/T102/consultant/standards/T102-ADR-009_governance-standards-specification.md` |


* **T102-ADR-001 (Consultancy Operating Model)** {#t102-adr-001-consultancy-model}

  **Context.** Per `T102-GDR-001`, define the consultancy model using Double Diamond, aligned with ISO/IEC/IEEE 42010, IEEE 1016, ISO 29148, and BABOK v3. Current flow lacks traceability and role separation.

  **Decision.** Adopt a four‑stage workflow with clear handoffs and approvals:

    1) **SPS (Project Initiation Document)**
      - **Why**: Establish governance early; avoid scope creep/inversion
      - **What**: Initiative/epic governance with GDR Index; no solutions/technical ADRs
      - **Benefit**: Client retains strategic control

    2) **Request (Business/System Requirements)**
      - **Why**: Turn approved problems into testable requirements without solutions
      - **What**: Feature BRD/SRS with story AC; inherits SPS governance; no decision records
      - **Benefit**: Stable baseline for solution exploration

    3) **Concept (Architecture Description)**
      - **Why**: Compare options and secure approval before implementation
      - **What**: ADR compendium; criteria/matrices; C4 views; Design Log Register
      - **Benefit**: Evidence‑based selection with traceability

    4) **Design (Story Implementation Logs)**
      - **Why**: Capture story‑level implementation decisions with upstream traceability
      - **What**: Final solutions, integration notes, dependencies; ADR variances if deviating
      - **Benefit**: Detailed guidance with preserved audit trail
  
  **Specification**

    1) **T102-ADR-001-CLAUSE-001 (SPS Implementation)** 
      - Project Initiation Document (PID) structure with initiative/epic governance scope
      - Initiative Considerations framework: assumptions, constraints, quality goals, dependencies, implementation guidance, notes/parking lot
      - Initiative GDR Index for governance decision traceability
      - Epic dossier pattern: YAML identity, purpose/scope, governance table, inherited considerations table, quality goals, dependencies, feature register, epic GDR Index

    2) **T102-ADR-001-CLAUSE-002 (REQUEST Implementation)** 
      - Business Requirements Document (BRD) + System Requirements Specification (SRS) structure
      - Feature-scoped requirements with story-level acceptance criteria in Gherkin format
      - Inherited considerations table referencing governing SPS rules with delta-only additions
      - No embedded decision records (link to Concept ADRs only via canonical links)
      - Gate approval checkpoints before Detailed Design work authorization

    3) **T102-ADR-001-CLAUSE-003 (CONCEPT Implementation)** 
      - Architecture Description Document (ADD) serving as ADR compendium across initiative/epic/feature levels
      - Uniform ADR format: `Context→Decision→Specification→Consequences→Alternatives Considered→References` with repo-relative links
      - Design Log Register maintaining links-only to story-level implementation details
      - Initiative/Epic/Feature ADR indices with governance traceability to parent GDRs

    4) **T102-ADR-001-CLAUSE-004 (DESIGN Implementation)** 
      - Story-level design logs with final proposed solution, integration notes, dependencies, decision records
      - ADR variance documentation when deviating from upstream Concept framework decisions
      - Explicit traceability references to governing GDR/ADR hierarchy for change impact analysis
      - Ripple test documentation for cross-story coupling validation

  **Alternatives Considered**
    (a) All decisions in SPS — rejected (breaks governance vs. architecture separation; raises churn). 
    (b) Request as SAD‑lite — rejected (reintroduces inversion; duplicates Concept; conflicts with 29148 SRS role). 
    (c) Split Concept by scope (I/E/F) — deferred (more files; client prefers single compendium). 

  **Consequences**
    (+) Standardized workflow; less rework; predictable delivery
    (+) End‑to‑end traceability from problem to implementation
    (+) Industry‑aligned method improves conF-SIDence and adoption
    (-) Initial training needed for template adoption
    (±) Structure may slow early authoring but raises quality

  **References** 
  `T102-GDR-001 (Consultancy Operating Model Standard)`, 
  `T102-NOTE-003 (Industry Standards)`

  **Provenance** `sps_T102-CONSULTANT.md`

* **T102-ADR-002 (Canonical YAML Header)** {#t102-adr-002-yaml-header}
  **Context** Per `T102-GDR-002`, we need implementation of a unified YAML header schema across all consultancy artifacts. Current templates suffer     
  from inconsistent key definitions, enum variations, and parsing conflicts which has consequent to blocking future reliable automation and creating governance gaps in artifact identity management. 

  **Decision.** Implement the Canonical YAML Header through standardized schema definition and adoption specifications below:

    - **Why**: Eliminate header schema inconsistencies that block automation and create governance gaps
    - **What**: Unified YAML header specification with mandatory key set, format validation, and conformance requirements
    - **Benefit**: Enables reliable artifact parsing, consistent governance signals, and predictable automation development

  **Specification**
    1) **T102-ADR-002-CLAUSE-001 (Header Keys)**  
      The template SHALL begin with a valid **YAML header** containing only these core keys:  
      `artifact_type, initiative_id, (epic_id), (feature_id), (story_id), version, date, status, author, decision_owner_role, (dependencies)` where keys in parentheses are required when applicable (feature/story docs).

    2) **T102-ADR-002-CLAUSE-002 (Key Formats)**  
      The header keys SHALL conform to the following:  
      `artifact_type ∈ {SPS, REQUEST, CONCEPT, DESIGN, PLAN, PROPOSAL, REPORT, BRIEF, ROADMAP, LOG, ANALYSIS}`;  
      `initiative_id: ^T/d{3}$` (e.g., `T102`);  
      `epic_id: ^T/d{3}[A-Z]$` (e.g., `T102A`);  
      `feature_id: ^T/d{3}[A-Z]-[A-Z0-9_]+$` (e.g., `T102A-SPSST`);  
      `story_id: ^T/d{3}[A-Z]-[A-Z0-9_]+-S/d+$` (e.g., `T102A-SPSST-S1`);  
      `version`: SemVer; 
      `date`: ISO-8601 (YYYY-MM-DD);  
      `status ∈ {draft, review, approved, rework, deprecated}`;  
      `author ∈ {LLM_Consultant, LLM_Planner, LLM_Developer, LLM_Reviewer}`;  
      `decision_owner_role = Client`;  

    3) * **T102-ADR-002-CLAUSE-003 (Schema Examples)**  
    The template SHALL include canonical examples for SPS/REQUEST/CONCEPT headers and reference **header.schema.v1** (structure only; no enforcement in v1). 

  **Alternatives Considered:** 
  (a) **YAML-embedded approvals** (rejected): Creates parsing complexity and reduces human readability of approval signals; conflicts     
  with established body-based approval patterns
  (b) **Legacy key preservation** (rejected): Maintains existing inconsistencies including `task_id`/`prefix_id` variations; prevents     
automation standardization
  (c) **Extended header with automation fields** (deferred): Future v2 consideration; v1 focuses on minimal stable foundation

  **Consequences.**  
  (+) Consistent artifact identity and governance parsing across all consultancy layers
  (+) Reliable foundation for validation tools and automation development
  (+) Clear separation between machine-readable headers and human-readable approvals
  (+) Standardized artifact lineage tracking through structured ID hierarchy
  (±) Requires migration of existing artifacts with non-conforming headers
  (-) Body parsing still required for approval signals (design trade-off for readability)

  **References** 
  `T102-GDR-002 (Canonical Header Standard)`, 
  `T102-IG-005 (Canonical Header)`,
  `T102-CON-001 (Format Requirements)`, 
  `T102-QG-002 (End-to-End Traceability)`
  
  **Provenance** `design_T102A-SPSST-S1.md`

* **T102-ADR-003 (Explicit Inheritance Model)** {#t102-adr-003-explicit-inheritance}
  **Context** Per `T102-GDR-003`, “delta-only” by habit does not avoid duplication and drift. This *mandates* explicit inheritance model. This ADR defines the **implementation contract** (tables, linking, precedence). 

  **Decision** Implement **Explicit ID Referencing** in addition to delta-only across all PM scopes:
    **Why**: Prevent rule duplication and governance drift that creates inconsistent decision authority and audit trail gaps across artifact hierarchy
    **What**: Each PM scope **implicitly inherits all higher-precedence rules** per the hierarchy (I-RIDs through S-ADRs) but **explicitly emphasizes only critical inherited items** via "Inherited Considerations" tables using ID references. All scopes record **only deltas/overrides** without restating upstream content verbatim. **Upstream scopes never reference downstream rules** - inheritance flows unidirectionally from higher or equal to lower precedence only.
    **Benefit**: Maintains single source of truth for governance while providing scannable inheritance visibility without verbose duplication

  **Specification**

    1) **T102-ADR-003-CLAUSE-001 (Table Contracts)** 
    Epic dossier from `sps` and relevant sections from `request`, `concept`, and `design` MUST include an **Inherited Considerations** table with EXACTLY these columns:
    `Source Artifact | Scope ID | Category | Inherited Rule IDs`  
      - Source Artifact: one of `{SPS, CONCEPT, REQUEST, DESIGN}`.
      - Scope ID: [I-SID|E-SID|F-SID|S-SID]
      - Use repo-relative anchors when available (e.g., `SPS#t102-gdr-003-inheritance-model`).
      - Category: one of `{Assumptions, Constraints, Quality Goals, Dependencies, Implementation Guides, Notes, Governances, Architecture}`   
      - Inherited Rule IDs: back-ticked list of `ID (Title)` tokens; **≤5 items**;

    2) **T102-ADR-003-CLAUSE-002 (Precedence)**
    **I-SID  > E-SID > F-SID >  S-SID**; variances require a local ADR that cites the parent.

    3) **T102-ADR-003-CLAUSE-003 (Authoring Rules)**
      - Do **not** restate parent text; list IDs only (delta-only).
      - Prefer the **most critical ≤5** inherited IDs for scanability.
      - Link by anchor; avoid raw URLs.
      - When deviating, create a **variance ADR** in the local artifact.
    

  **Consequences**
    (+) Short, scannable upstream references in every artifact; clean audit trail.  
    (+) Future validator can check presence/anchors without changing authoring flow.
    (±) Requires discipline to maintain ID-only references without restating parent content
    (-) Authors must navigate to parent artifacts to read full rule text when needed

  **Alternatives Considered** 
    (a) **Delta-only model** (rejected): Informal convention proved insufficient;

  **References** 
  `T102-GDR-003 (Inheritance Model Standard)`, 
  `T102-IG-010 (Inheritance Model)`, 
  `T102-NOTE-004 (Inheritance Philosophy)`

  **Provenance** `design_T102A-SPSST-S4.md`

* **T102-ADR-004 (Decision Records Index)** {#t102-adr-004-drs-index}

  * **Context** 
    Per `T102-STD-004 (Decision Records Standard)`, ADR schemas and anchors vary across artifacts, causing drift and blocking automation.

  * **Decision** 
    Implement a unified decision record index: one table schema, shared body subheadings, and consistent anchors/links across SPS/Request/Concept/Design. This ADR serves as the adopted normative specification for `T102-STD-004`.

  * **Specification**
    * **T102-ADR-004-CLAUSE-001 (DR Index Schemas)**
      - **ADR Index Schema**  
        `ADR ID | Title | Authority STD | Status | Owner | Effective | Supersedes | Anchor`

      - **Column Definitions**
        1. `ID`: ID construction MUST follow `T102-ADR-005` following general format: `<SID>-ADR-###`
        2. `Title`: Title Case, 2–3 words.
        3. `Status`: `{Proposed, Accepted, Deprecated}`.
        4. `Owner`: governance authority (typically `Client`) or implementation owner; if unknown use `—`.
        5. `Effective`: ISO-8601 date `YYYY-MM-DD`.
        6. `Supersedes`: list of superseded IDs or `—`.
        7. `Anchor`: lower-kebab anchor derived from Title; stable.
        8. `Authority STD`: the governing `STD` that applies to the ADR (or that adopts the ADR as the canonical normative spec). Use `—` if none.

    * **T102-ADR-004-CLAUSE-002 (Placement Standards)**
      - **SPS artifacts**: section titled `"<SCOPE> Governance Decisions"` containing governance decisions only.
      - **Concept artifacts**: section titled `"<SCOPE> Architectural Decisions"` with mirror subsections for Epic/Feature areas as needed.
      - **Consistency requirement**: placement MUST follow established artifact section numbering without local deviations.

    * **T102-ADR-004-CLAUSE-003 (Entry Creation Workflow)**
      To create a new ADR:
      1. Add a new row to the appropriate index table using the required schema per `T102-ADR-004-CLAUSE-001`.
      2. Assign the next sequential ID for that scope.
      3. Create the matching body entry below the index using `T102-ADR-004-CLAUSE-004` structure.
      4. Ensure References follow `T102-ADR-005`.

    * **T102-ADR-004-CLAUSE-004 (DR Body Template)**
      - **Structure**:
        - **Headings**: Main bold headings (e.g. `* **Context**`) MUST be preceded by two newlines.
        - **Body**: Content MUST start on a new line and INDENTED under the heading with no space in between.
      - **Format**: `* **<ID> (<Title>)** {#<anchor>}`
      - **Required Subheadings**:
        * **Context** [Why this decision is needed; the gap it resolves.]
        * **Decision** [What is adopted/changed and who owns it.]
        * **Specification** [Clause list using `CLAUSE` token type or software requirement clauses (if used in that ADR).]
        * **Alternatives** [Bulleted list of additional options considered with clear rejection rationales.]
        * **Consequences** [Impacts using `(+)`, `(±)`, `(-)` bullets.]
        * **References** [Canonical references/anchors per `T102-ADR-005`.]
        * **Provenance** [Bulleted list of evidence/design source repo-relative paths only.]


    * **T102-ADR-004-CLAUSE-005 (Specification Clauses)**
      **Purpose**  
      Standardize how ADR **Specification** sections are constructed using `CLAUSE` IDs, without duplicating global ID semantics.

      **Normative Reference**
      - `CLAUSE` token type construction and semantics MUST follow `T102-ADR-005-CLAUSE-005D (Specification Clause Semantics)`.

      **Specification Section Structure**
      Within an ADR body, the **Specification** subsection MUST be a list of clause items, each defined as:

      - Format: `n) **<CLAUSE-ID> (<Title>)**`, where `<CLAUSE-ID>` conforms to `T102-ADR-005-CLAUSE-005D`. 

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

    * **T102-ADR-004-CLAUSE-006 (Cross-Artifact Linking Patterns)**

      - **STD → Adoption (Adoption Statement).**  
        If a STD formally adopts/mandates an ADR or RID, the adoption MUST be stated as the first sentence of the STD body:  
        - Pattern: `The project SHALL use <ID>...` or similar normative adoption language declaring the adopted ID.
        - Example: `The project SHALL use `T102-ADR-004`, as the single Client-owned standard...`

      - **ADR → Context (Authority Citation).**  
        If an ADR is governed by a STD, the governing policy MUST be cited as the first sentence of **Context**:  
        - Pattern: `Per <STD-ID>, <one-line rationale>...`  
        - Example: ``Per `T102-STD-004`, a unified DR schema is required to prevent drift.``

    * **T102-ADR-004-CLAUSE-007 (Anchor Title Stability)**

      - Anchors MUST be lower-kebab derived from the Title.
      - Anchors MUST remain stable across file moves/splits.
      - If Title changes, keep the old anchor unless an explicit migration is performed.

    * **T102-ADR-004-CLAUSE-008 (Lifecycle Coherence)**

      When a STD cited by ADRs changes **Status** or is **Superseded**, affected ADRs MUST:
      - update the **Context** authority sentence to the new governing STD ID/title; and
      - add the prior STD ID to **Supersedes/References** as appropriate; and
      - perform this update in the next modification to the ADR or in a dedicated “governance sync” change set.

    * **T102-ADR-004-CLAUSE-009 (Status Management)**

      - Lifecycle: `Proposed → Accepted → Deprecated`
      - Superseded IDs MUST be captured in the **Supersedes** column and, where applicable, referenced in body text.

    * **T102-ADR-004-CLAUSE-010 (Precedence Conflicts Hierarchy)**

      For conflict resolution across DRIDs:
      `Initiative STD > Initiative ADR > Epic ADR > Feature ADR > Story ADR`

      See `T102-ADR-003` and `T102-ADR-005` for full hierarchy and directionality constraints.


    * **T102-ADR-004-CLAUSE-011 (Consequences Scope Requirements)**

      - **STD Consequences** SHOULD cover: policy/precedence impacts; compliance expectations; migration/rollout; automation/traceability effects.
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
      3. **Decision Records (STD/ADR)** — Promote stable, cross-cutting, or long-lived patterns into formal STD/ADR records when:
          - (a) The pattern affects multiple artifacts or features; or
          - (b) The pattern requires explicit governance (ownership, status, supersedes) beyond implementation detail.
      4. **Traceability** — ADR Specifications SHOULD reference governing research and guidance in **Provenance** and **References**, rather than duplicating detailed patterns.
      5. **Scope Guidance** —
          - Epic-level ADRs SHOULD be used for cross-feature decisions (e.g., shared vocabularies, common JSON architectures).
          - Feature-level ADRs SHOULD be reserved for significant, feature-local architectural decisions that cannot reasonably be governed at Epic scope.
          - Routine implementation details MAY remain in guidance without a dedicated ADR.


    * **T102-ADR-004-CLAUSE-015 (Automation & Linting Checks)**

      Authors SHOULD pass these checks:
      - STD body contains an **Adoption** statement matching normative patterns.
      - ADR body **Context** starts with:  
        `` `^Per\s+`T[0-9]{3,}(?:[A-Z][0-9A-Z]*)?-STD-[0-9]{3}`,\s+.+$` ``

  * **Alternatives**
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

* **T102-ADR-005 (ID Specification & Rules)** {#t102-adr-005-id-spec}

  * **Context** 
    Per `T102-STD-005 (ID Governance Standard)`, multiple artifact families use overlapping ID conventions (considerations, requirements, decisions) at different scopes. Without a single normative specification, authors improvise category tokens, anchors, and references, creating inconsistency and undermining inheritance, precedence, and verification.

  * **Decision** 
    Standardize ID patterns across Initiative, Epic, Feature, and Story scopes; define category tokens, sub-ID patterns, anchors, and referencing rules. This ADR is the single specification adopted by `T102-STD-005` as its normative specification.

  * **Specification**

    * **T102-ADR-005-CLAUSE-001 (Canonical ID Schema)**

      **Regex Patterns**: usage of all IDs SHALL match one of these patterns:

      - **Pattern 1 (Initiative/Epic/Feature/Story Scope ID / SID)**: `^T\d{3}(?:[A-Z]\d*)?(?:-[A-Z0-9_]+)*$`
        - Examples: `T102`, `T102A`, `T102A1-S3`, `T102A-SPSST`
      - **Pattern 2 (Initiative/Epic/Feature/Story Tokenized ID)**: `^T\d{3}(?:[A-Z]\d*)?(?:-[A-Z0-9_]+)*-[A-Z]+-\d{3}$`
        - Examples: `T102-QG-001`, `T102A1-NFR-005`, `T102A-SPSST-IG-002`
      - **Pattern 3 (Program Tokenized ID)**: `^P(?:-[A-Z0-9_]+)*-[A-Z]+-\d{3}$`
        - Examples: `P-STD-001`, `P-CON-001`, `P-ADR-001`

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
      - `P` (Program),
      - `I` (Initiative),
      - `E` (Epic),
      - `F` (Feature),
      - `S` (Story)

      **Program Scope (`P`)**
      - `P` denotes cross-initiative governance scope (program-level SSOT). `P-*` IDs MAY govern multiple initiatives.
      - Program IDs MUST use the `P-<TOKEN>-###` format per `T102-ADR-005-CLAUSE-001`.
      - Any ID MAY be **re-scoped** (promoted or demoted) across `P/I/E/F/S` when its applicability changes, subject to `T102-ADR-005-CLAUSE-003 (Precedence & Hierarchy)` and the re-scope contract in `T102-ADR-005-CLAUSE-003A`.

      Valid tokens are strictly defined by this table. Authors MUST select the most specific token available for the scope.

      | Category | Token | Name | Allowed Scope | Definition & Usage |
      |:---|:---|:---|:---|:---|
      | `SID` | `SCOPE` | **Project Management Scope** | P, I, E, F, S | Artifact Identifiers (e.g., `P`, `T102`, `T102A`). |
      | `RESID` | `RES` | **Research** | I, E, F | Commissioned research trace (Evidence). |
      | `RID` | `ASSUM` | **Assumption** | P, I, E, F | Unverified belief carrying risk. Must track validation status. |
      | `RID` | `CON` | **Constraint** | P, I, E, F | Non-negotiable boundary or limitation. |
      | `RID` | `QG` | **Quality Goal** | P, I, E | Initiative success metrics (e.g., traceability completeness, review turnaround). |
      | `RID` | `DEP` | **Dependency** | P, I, E | External condition, interface, asset, or approval required. |
      | `RID` | `IF` | **Interface** | P, I, E, F | Data/integration contract definition (contractual boundary). |
      | `RID` | `FR` | **Functional Requirement** | F, S | Testable system behavior (requirements language). |
      | `RID` | `NFR` | **Non-Functional Requirement** | F, S | Quality requirement expressed as testable metrics. |
      | `RID` | `STD` | **Standard** | P, I, E, F | Normative standards registry token. Enforceable obligations MUST be encoded in `STD` or in its adopted normative specification; governance rationale belongs in ADRs. |
      | `DRID` | `ADR` | **Architectural Decision** | P, I, E, F, S | Technical implementation decision record. |
      | `DRCID` | `CLAUSE` | **Decision Record Clause** | P, I, E, F, S | ADR-internal clause ID used only within the parent ADR. Scope and authority derive from the parent ADR only; rendering is defined by `T102-ADR-004-CLAUSE-005`. |
      | `IID` | `IG` | **Implementation Guidance** | I, E, F | Informative how-to guidance: patterns, templates, and examples. MUST NOT introduce new obligations. Not a substitute for system requirements. |
      | `IID` | `INT` | **Integration Guidance** | I, E, F, S | Non-normative integration and cross-scope coordination guidance for external audiences; MUST NOT introduce new obligations. |
      | `OID` | `NOTE` | **Note** | I, E, F, S | Non-normative context; do not use for obligations. |
      | `OID` | `ISSUE` | **Issue** | I, E, F | Known gap requiring resolution. |
      | `OID` | `RISK` | **Risk** | I, E, F | Potential negative event requiring mitigation. |

    * **T102-ADR-005-CLAUSE-003 (Precedence & Hierarchy)**

      **Directionality**: Inheritance flows downstream with scopes only.
      - Correct: Story references Feature; Feature references Epic; Epic references Initiative; Initiative references Program.
      - Incorrect: Higher scope references lower scope (except `INT` exception defined in `T102-ADR-005-CLAUSE-005C`).

      **Precedence Order** (Highest to Lowest):
      - Program > Initiative > Epic > Feature > Story

      **Category Precedence** (within same scope):
      `SID > RESID > RID > DRID (ADR) > DRCID > IID (IG > INT) > OID`

      **Evidence Conflict Rule**:
      If `RESID` contradicts a `RID` or `DRID`, it triggers a Review workflow (ISSUE + Change Decision). Evidence does not “silently override” obligations.

      **Variances**:
      Any downstream ID deviating from an upstream rule MUST cite the overridden ID explicitly in a “Variance ADR”.

      * **T102-ADR-005-CLAUSE-003A (Cross-Scope Re-scope / Promotion Contract)**
        This contract applies to ALL `RID` token types (e.g., `QG/CON/DEP/IF/STD/...`) and covers promotion/demotion across `P/I/E/F/S`.
        1. **When to Promote (Up-scope)**:
          - Promote when the obligation/constraint/goal is stable AND applies to multiple downstream scopes (e.g., `E-QG` becomes `I-QG`; `I-CON` becomes `P-CON`).
        2. **When to Demote (Down-scope)**:
          - Demote when a rule no longer holds broadly and becomes legitimately local (e.g., `I-IF` becomes `E-IF`).
        3. **Supersedes Requirement**:
          - The old ID MUST be marked as superseded by the new ID (via `Supersedes` metadata where available, or an explicit statement in-body if the artifact type lacks a table).
        4. **Reference Update Requirement**:
          - New authoring MUST reference the new ID.
          - Existing references SHOULD be migrated to the new ID in the next touch of the referencing artifact, or via a dedicated governance sync change set.
        5. **Split / Merge Cases**:
          - If one ID becomes multiple IDs (split), the old ID MUST supersede to a set of new IDs and document the split rationale in an ADR.
          - If multiple IDs become one ID (merge), the new ID MUST list all superseded IDs.

      * **T102-ADR-005-CLAUSE-003B (Alias Window for Re-scope Transitions)**
        - During a defined migration window, superseded IDs MAY be treated as aliases of their replacement IDs for lint/enforcement.
        - Alias support MUST be removed after the migration completion milestone/date.


    * **T102-ADR-005-CLAUSE-004 (Reference Semantics)**

      **Styles**:
      - **Short-hand (Inline):** `` `ID` `` (e.g., `T102-QG-001`, `T102B`)
      - **Full (Formal):** `` `ID (Title)` `` (e.g., `T102-QG-001 (Client Readability)`, `T102B (REQUEST)`)

      **Required Usage**:
      - In-body prose (within ID bodies): Short-hand preferred
      - Dedicated sections (References, Tables): Full references required

      **External Reference Line**:
      If a body references an ID from a different **scope root**, a standalone citation line SHALL appear at the bottom of that body.
      - Scope roots are:
        - Program root: `P` (e.g., `P-STD-001`)
        - Initiative-family roots: `T###...` (e.g., `T102`, `T104A`, etc.)
      - Trigger condition:
        - Any `P-*` reference inside a `T###...` body, OR
        - Any cross-initiative-family reference (e.g., `T104...` inside `T102...`), OR
        - Any cross-epic variant where your initiative treats prefixes as separate roots (e.g., `T102B...` inside `T102A...`).
      - Format: `External Reference:` followed by one or more full references (`` `ID (Title)` ``).
      - This line SHALL NOT be used for references within the same scope root.

      **Constraint**:
      Normative bodies MUST NOT reference `ISSUE` or `RISK` IDs inline. Issues/Risks capture the problem; RIDs/DRIDs capture the solution.

    * **T102-ADR-005-CLAUSE-005 (Category Semantics)**

      This clause provides a concise semantic overview. Tokens with lifecycle/exception behavior have dedicated subclauses. 

      * **T102-ADR-005-CLAUSE-005A (Assumption Lifecycle)**

        **Table Requirement**:
        Assumptions MUST be defined in a table structure preceding the list of ID bodies.

        **Schema**:
        `| ID | Title | Status | Validation Method | Timing | Owner | If Invalidated | CON Cross-Ref |`

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

      * **T102-ADR-005-CLAUSE-005C (Integration Guidance Rules)**

        **Role**:
        - External-facing integration guidance and cross-scope coordination guidance.
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
        - Style: Non‑normative and descriptive; do not restate formal rules or research verbatim; use back‑ticked IDs to reference STD/ADR/RES where helpful.
        - Conformance: Mirrors existing examples in SPS Section III.B.7.

        **Notes Authoring Guidelines**
        - Purpose: Capture lightweight, non‑commissioned insights aiding authoring and reader orientation without introducing governance or architectural decisions.
        - When to add a NOTE: contextual clarifications, philosophy, industry references, or early observations prior to commissioning research.
        - When NOT to use a NOTE: to summarize commissioned research (use RES with Brief/Report), to encode enforceable rules (use STD/ADR), or to duplicate upstream content (link via back‑ticked IDs instead).
        - Discipline: Keep short (≤200 words), scannable, and link‑don’t‑duplicate. If NOTE content becomes critical or frequently referenced, promote to `RES` (with brief/report) or to `STD/ADR` as appropriate. Maintain sequential NOTE numbering without retroactively altering meaning.

    * **T102-ADR-005-CLAUSE-006 (Content Quality)**

      **Quality Criteria**:
      - **RID**: Lead with a requirement statement when applicable (SHALL/SHOULD). No justification prose (put rationale in NOTE). Prefer one primary obligation per RID.
      - **IID-IG**: Informative how-to guidance; may include templates, pseudo-code, and examples; MUST NOT introduce new obligations.
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
      - **Legacy Standards Migration**: Migration tolerance for legacy governance standard identifiers is defined in `T102-ADR-009-CLAUSE-005 (Migration Tolerance)`.

  * **Alternatives**
    - Free-form, template-local ID schemes — rejected.
    - Enforcing full titles in all inline mentions — rejected.

  * **Consequences**
    (+) Predictable, machine-checkable IDs across artifacts.
    (+) Faster audits and safer cross-linking with stable anchors.
    (±) Requires discipline and small refactors for legacy items.

  * **References** 
    `T102-STD-005 (ID Governance Standard)`, 
    `T102-ADR-003 (Explicit Inheritance Model)`, 
    `T102-ADR-004 (Decision Records Index)`, 
    `T102-ADR-006 (Research Artifacts Index)`,
    `T102-CON-009 (Normative Keywords)`

  * **Provenance** 
    - `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_refactor-adr-004-005.md`

* **T102-ADR-006 (Research Artifacts Index)** {#t102-adr-006-research-index}

  **Context.** Per `T102-GDR-006 (Research Workflow Standard)`, formal research workflow requires architectural implementation specification for artifact indexing, placement strategies, and cross-scope traceability. External research (`T102-RES-001`) validated three-tier placement strategy (inline/appendix/external) and recommended hybrid index architecture: local indexes in SPS artifacts (Initiative/Epic/Feature-level) plus master aggregation register in Concept workspace. Current ad-hoc NOTE pattern created scalability concerns (`T102A-RISK-003`) without structured research governance.

  **Decision.** Implement hybrid Research Artifacts Index architecture with dual-layer indexing and standardized placement thresholds:

  - **Why:** Balance local context visibility (SPS sections) with initiative-wide research landscape aggregation (Concept master register) while maintaining "link-don't-duplicate" principle per `T102-ADR-003`.
  - **What:** Two-tier index structure: (1) Local Research tables in SPS artifacts at Initiative/Epic/Feature scope levels, (2) Aggregated Research Register in Concept Section E.3 consolidating all research with source traceability and markdown-linked artifacts.
  - **Benefit:** Enables scalable research commissioning without document bloat while providing comprehensive research visibility for decision-making and audit trails.

  **Specification**

    * **T102-ADR-006-CLAUSE-001 (RES ID Pattern Integration)**
       - Research ID pattern: `<SCOPE_ID>-RES-###` where `SCOPE_ID ∈ {T102, T102A, T102B, T102C, T102D, T102E, ...}`.
       - ID construction follows `T102-ADR-005 (ID Specification & Rules)` universal pattern.
       - Sequential numbering (001, 002, ...) within each scope level (Initiative, Epic, Feature).
       - Category definition: "RES — Research: Formally commissioned research with approved brief and validated report artifacts; traceable via Research Artifacts Index per `T102-ADR-006`".
       - Integration: `T102-ADR-005-CLAUSE-004 (ID Categories)` SHALL include the RES category and scope allowances.

    * **T102-ADR-006-CLAUSE-002 (Research Table Schema)**
       - **Local SPS Tables** (Initiative/Epic/Feature sections):
         - Placement: Section titled "Research & Notes" with subsections "Research" and "Notes".
         - Schema: `| Research ID | Title | Summary | Reference | Brief | Report |`.
         - Column alignment: left-aligned (`:---`).
       - **Concept Aggregation Register** (Section E.3):
         - Placement: `concept` document in Section E (Registers) → Subsection 3 (Research Artifacts Register).
         - Schema: `| Scope | Scope ID | Research ID | Title | Summary | Reference | Brief | Report | Source |`.
         - Column alignment: left-aligned (`:---`).
       - **Universal Column Specifications:**
         - Scope (Concept only): PM hierarchy level {Initiative, Epic, Feature}.
         - Scope ID (Concept only): Back-ticked scope identifier (e.g., `T102`, `T102A`).
         - Research ID: Back-ticked full RES-### identifier (e.g., `T102-RES-001`, `T102A-RES-001`).
         - Title: Bold-formatted descriptive name using `**Title Text**` (2–8 words recommended).
         - Summary: Executive summary (1–2 sentences, target <100 words).
         - Reference: Back-ticked, comma-separated list of consuming IDs (e.g., `T102-GDR-006`, `T102-ISSUE-005`).
         - Brief: Markdown link to research brief artifact with repo-relative path.
         - Report: Markdown link to research report artifact with repo-relative path.
         - Source (Concept only): Back-ticked repo-relative path to SPS section containing local research table (with section anchor), e.g., `../sps/sps_T102-CONSULTANT_v1.1.0.md#research--notes`.
       - **Artifact Filenames:**
         - Brief files SHALL follow: `brief_<SCOPE-SID>-<SCOPE-NAME>_<title>.md`.
         - Report files SHALL follow: `report_<SCOPE-SID>-<SCOPE-NAME>_<title>.md`.
         - Brief and Report for the same research SHALL share the same `<SCOPE-SID>-<SCOPE-NAME>_<title>` stem. Public links SHALL omit any `_i<n>` revision suffix.
       - **Templates:**
         - `prompt\templates\researcher\template_research_brief.md`
         - `prompt\templates\researcher\template_research_report.md`

    * **T102-ADR-006-CLAUSE-003 (Placement Decision Criteria)**
       - Inline Summary (<300 words): Brief research findings MAY be integrated directly into SPS body sections (Epic Notes, Implementation Guidance) when contextually essential.
       - Local Index Entry (mandatory for all formal research): All commissioned research with approved brief + validated report SHALL appear in the corresponding SPS scope's local Research table.
       - Concept Aggregation (mandatory for all formal research): Master Research Register in Concept Section E.3 SHALL consolidate all Initiative/Epic/Feature research.
       - External-Only (extensive research >3 pages): Research reports stored in dedicated `research/report/` directory; only summary and markdown links appear in indexes.
       - Threshold application: Research findings guide inline placement decisions; all formal research indexed in both SPS local tables and Concept register regardless of report size.

    * **T102-ADR-006-CLAUSE-004 (Index Maintenance Protocol)**
       - Synchronization approach: Manual verification; tooling deferred to future development per `T102-CON-002 (Minimal Automation)`.
       - Addition workflow: New research commissioned → (1) Create RES-### entry in appropriate SPS scope's local Research table, (2) Update Concept Research Register with aggregated entry including Scope/Scope ID/Source.
       - Update workflow: Research report revisions → Update Summary in both SPS local index and Concept register; update Brief/Report links to latest semantic version (vX.Y.Z) without `_i<n>` suffix; preserve version history through file system.
       - Deprecation workflow: Superseded research → Add inline note to Summary (e.g., "Superseded by T102-RES-004 addressing expanded scope"); maintain entry for audit trail; update Reference column to reflect current consuming IDs.
       - Verification cadence: Review synchronization at each epic handoff gate; escalate material drift to Client for resolution.

    * **T102-ADR-006-CLAUSE-005 (Cross-Artifact Referencing)**
       - Research findings SHALL be referenced via RES-### ID tokens in back-ticked format, never copy-pasted verbatim.
       - GDRs/ADRs consuming research SHALL cite RES-### in References sections using `RES-SID (Title)` when appropriate.
       - Issues/Risks resolved via research SHALL cite RES-### in resolution notes.
       - Feature/Story artifacts inheriting research context SHALL reference RES-### via Inherited Considerations tables per `T102-ADR-003` when critical to downstream scope.
       - Research brief/report MAY be linked using markdown link syntax when full artifact review needed; use RES-### ID for governance traceability.

    * **T102-ADR-006-CLAUSE-006 (Hybrid Pattern Scalability)**
       - Pattern applies uniformly across Initiative/Epic/Feature scopes with identical table schemas at each level.
       - Feature-level research (e.g., `T102A-SPSST-RES-001`) follows dual-indexing: local table in REQUEST artifact + aggregation in Concept register.
       - Story-level research deferred to future need assessment; if required, would follow same pattern with local table in DESIGN artifact.
       - Concept register remains single source of truth for initiative-wide research landscape; SPS/REQUEST local tables provide contextual proximity for authoring efficiency.

  **Alternatives Considered**
    (a) SPS‑only research indexing — rejected: no initiative‑wide aggregation visibility; manual cross‑Epic correlation; conflicts with Concept's dynamic workspace role per `T102-ADR-001`.
    (b) Concept‑only research register — rejected: eliminates local context in SPS artifacts; reduces executive readability per `T102-QG-001`.
    (c) Automated synchronization tooling — rejected: violates `T102-CON-002 (Minimal Automation)` v1 constraint; manual verification is sufficient at current scale.
    (d) Embedded research content — rejected: creates document bloat; `T102-RES-001` validated as anti‑pattern.

  **Consequences**
  (+) Scalable research commissioning without SPS document bloat via structured placement strategy.
  (+) Initiative‑wide research landscape visibility through Concept aggregation supporting decision‑making.
  (+) Maintains local context in SPS/REQUEST for executive readability per `T102-QG-001`.
  (+) Clear audit trail and traceability for LLM‑generated research per `T102-QG-004`.
  (+) Aligns with "link‑don't‑duplicate" principle per `T102-ADR-003` avoiding content drift.
  (+) Markdown links to Brief/Report enable one‑click artifact access for validation workflows.
  (±) Requires dual maintenance (SPS local + Concept register) introducing manual synchronization overhead.
  (±) Requires discipline in RES/NOTE ID assignment and updates across two locations.
  (±) Omitting `_i<n>` suffixes from links requires file naming discipline (semantic versioning only in public links).
  (-) Manual verification approach creates drift risk; periodic review cadence required.
  (-) Migration effort to refactor existing research NOTEs to RES‑### pattern where formal artifacts exist.

  **References**
  `T102-GDR-006 (Research Workflow Standard)`,
  `T102-GDR-007 (LLM Quality Control)`,
  `T102-ADR-003 (Explicit Inheritance Model)`,
  `T102-ADR-005 (ID Specification & Rules)`,
  `T102-CON-002 (Minimal Automation)`,
  `T102-QG-001 (Client Readability)`,
  `T102-QG-002 (End-to-End Traceability)`,
  `T102-QG-004 (Research Validation Quality)`,
  `T102-RES-001 (Research Integration Governance Research)`

  **Provenance**

* **T102-ADR-007 (Issues & Risks Index)** {#t102-adr-007-issues-risks-index}

  **Context.** Per `T102-QG-001` and `T102-QG-002`, open issues and risks must remain scannable and traceable across SSOT artifacts. The current SPS/Request ecosystem contains inconsistent “Issues & Risks” implementations (varying table schemas, status enums/casing, and missing resolution/mitigation notes), creating governance drift and blocking reliable cross-scope rollups and future validation/automation.

  **Decision.** Standardize the “Issues & Risks” structure across SSOT artifacts (SPS and Request at minimum) using the full SPS schema as the canonical exemplar, including required guidance comment blocks and required resolution/mitigation notes.

  **Specification**

    1) **T102-ADR-007-CLAUSE-001 (Section Naming & Placement)**
      - MUST be available for each scope and use the exact heading `Issues & Risks` across all artifacts.

    2) **T102-ADR-007-CLAUSE-002 (Issues Guidance & Enum)**
      - Issue `Status` values MUST be uppercase and backticked exactly as listed: OPEN, IN-REVIEW, RESOLVED, BLOCKED, DEFERRED
      - Issue `Priority` values MUST be title case and backticked exactly as listed: HIGH, MEDIUM, LOW

    3) **T102-ADR-007-CLAUSE-003 (Issues Table Schema)**
      - Issues table MUST use this exact column schema:
        `| ID | Title | Description | Owner | Status | Priority | Proposed Date | Resolution Notes |Resolution Date |`
      - `Proposed Date` and `Resolution Date` MUST be ISO-8601 (`YYYY-MM-DD`) or `—` if unknown/not applicable.
      - `Resolution Notes` MUST follow these coupling rules:
        - If `Status = OPEN`: `Resolution Notes = —` and `Resolution Date = —`.
        - If `Status = IN-REVIEW`: `Resolution Notes` MAY be populated (planned resolution); `Resolution Date = —`.
        - If `Status ∈ {RESOLVED, BLOCKED, DEFERRED}`: `Resolution Notes` MUST be populated and `Resolution Date` MUST be an ISO-8601 date (not `—`).

    4) **T102-ADR-007-CLAUSE-004 (Risks Guidance & Enum)**
      - Risk `Status` values MUST be uppercase and backticked exactly as listed: OPEN, MONITORED, MITIGATED, ACCEPTED, CLOSED
      - Risk `Priority` values MUST be title case and backticked exactly as listed: HIGH, MEDIUM, LOW.

    5) **T102-ADR-007-CLAUSE-005 (Risks Table Schema)**
      - Risks table MUST use this exact column schema:
        `| ID | Title | Description | Owner | Status | Priority | Proposed Date | Mitigation Notes |Mitigation Date |`
      - `Proposed Date` and `Mitigation Date` MUST be ISO-8601 (`YYYY-MM-DD`) or `—` if unknown/not applicable.
      - `Mitigation Notes` MUST follow these coupling rules:
        - If `Status = OPEN`: `Mitigation Notes = —` and `Mitigation Date = —`.
        - If `Status = MONITORED`: `Mitigation Notes` MAY be populated (planned mitigation / trigger conditions); `Mitigation Date = —`.
        - If `Status ∈ {MITIGATED, ACCEPTED, CLOSED}`: `Mitigation Notes` MUST be populated and `Mitigation Date` MUST be an ISO-8601 date (not `—`).

    6) **T102-ADR-007-CLAUSE-006 (ID Rules)**
      - IDs MUST follow `T102-ADR-005 (ID Specification & Rules)` category tokens: `ISSUE` and `RISK`.
      - IDs MUST be scoped and sequential using three digits: `<SCOPE_ID>-ISSUE-###` and `<SCOPE_ID>-RISK-###` (e.g., `T102-ISSUE-005`, `T102A-RISK-003`).
      - IDs MUST remain stable once created (no reuse, no renumbering).

    7) **T102-ADR-007-CLAUSE-007 (Resolution Notes Requirement)**
      - Resolution notes MUST be captured in the `Resolution Notes` column (not as a separate post-table block).
      - For Issues with `Status = IN-REVIEW`, `Resolution Notes` MAY contain a planned/proposed resolution.
      - For Issues with `Status ∈ {RESOLVED, BLOCKED, DEFERRED}`, `Resolution Notes` MUST include a resolution summary and MUST include back-ticked IDs for governing E-RIDs/E-DRs (and GDR/ADR/RES/NOTE where applicable).
      - Resolution notes MUST be written to support auditability and traceability (avoid vague statements like “fixed” without citing controlling IDs or evidence).

    8) **T102-ADR-007-CLAUSE-008 (Mitigation Notes Requirement)**
      - Mitigation notes MUST be captured in the `Mitigation Notes` column (not as a separate post-table block).
      - For Risks with `Status = MONITORED`, `Mitigation Notes` MAY contain a planned/proposed mitigation.
      - For Risks with `Status ∈ {MITIGATED, ACCEPTED, CLOSED}`, `Mitigation Notes` MUST include a mitigation/acceptance summary and MUST include back-ticked IDs for governing E-RIDs/E-DRs (and GDR/ADR/RES/NOTE where applicable).
      - Mitigation notes SHOULD remain concise and “link-don’t-duplicate”.

    9) **T102-ADR-007-CLAUSE-009 (Cross-Scope Promotion & De-duplication)**
      - If an Epic issue/risk becomes Initiative-impacting, authors SHOULD create a corresponding Initiative item (e.g., `T102-ISSUE-###`) and:
        - keep the Epic item scoped to the Epic, OR
        - close the Epic item with a Resolution Note that references the promoted Initiative item by back-ticked ID.
      - Avoid duplicating full narratives across scopes; prefer ID references and delta-only updates per `T102-ADR-003 (Explicit Inheritance Model)`.

  **Alternatives Considered**
    (a) Allow each artifact to define its own Issues/Risks schema — rejected: creates drift and blocks cross-scope review.
    (b) Minimal “ID | Description | Owner | Status” tables everywhere — rejected: loses priority/date fields and reduces governance usefulness for complex initiatives.

  **Consequences**
    (+) Consistent, executive-readable issues/risk logs across SPS and Request artifacts.
    (+) Higher-quality traceability and auditability via mandatory resolution/mitigation notes.
    (+) Easier future validation/automation due to deterministic schemas and enums.
    (±) Slightly higher authoring overhead due to required notes on closure/mitigation.
    (-) Requires migration effort to align legacy sections to the standard.

  **References**
  `T102-ADR-003 (Explicit Inheritance Model)`,
  `T102-ADR-005 (ID Specification & Rules)`,
  `T102-CON-001 (Format Requirements)`,
  `T102-IG-001 (Comment Blocks)`,
  `T102-IG-006 (Markdown Heading Terminology)`,
  `T102-QG-001 (Client Readability)`,
  `T102-QG-002 (End-to-End Traceability)`

  **Provenance** `sps_T102-CONSULTANT_v1.1.0.md` (Section III.B.9; Epic dossier “Epic Issues & Risks” exemplar)

* **T102-ADR-008 (Organisation Baseline Index)** {#t102-adr-008-org-baseline-index}

  **Context:** Per `T102-GDR-008 (Organisation Baseline Standard)`, the initiative requires a stable org baseline so epic governance snapshots can reference consistent actor labels and decision rights without duplication or drift.

  **Decision:** Adopt `T102-ADR-008` to standardize the structure and maintenance policy of the initiative-level `III.B` “Organization & Responsibilities” subsection.

  **Specification:**

    1) **T102-ADR-008-CLAUSE-001 (Canonical Placement)**
       - Each initiative SPS SHOULD include `III.B.1 Organization & Responsibilities` (baseline) as the canonical governance role mapping for the initiative.
       - Epics SHALL reference this baseline rather than duplicating it (see `T102A-ADR-001`).

    2) **T102-ADR-008-CLAUSE-002 (Required Content)**
       The baseline subsection SHALL contain, in this order:

       (a) **Role Definitions**
       - A single combined table that maps *actors* to conventional role titles and governance semantics.
       - The Role Definitions table SHALL use this exact schema:
         - `Actor | Role Title(s) | Decision Rights | Primary Responsibilities | Scope Notes`
       - `Role Title(s)` SHOULD use conventional PID/charter labels (e.g., Sponsor/Decision Owner, Project Manager, Product Lead, Technical Lead, Planner).
       - The table SHALL include every *actor label* referenced anywhere else in the initiative SPS (including all epic `##### iv. Governance & Roadmap` and `##### v. Feature Register` sections).
       - Minimum required actors (may be extended per initiative, but not omitted):
         - `Client`
         - `LLM_Consultant`
         - `LLM_Planner`
         - `LLM_Researcher`
         - `LLM_Developer`

       (b) **Governance RACI**
       - A RACI table with the exact column schema:
         - `Governance Activity | R (Responsible) | A (Accountable) | C (Consulted) | I (Informed)`
       - The table SHALL include, at minimum, these governance activities (row titles may be adapted, but intent must remain):
         - Approve Initiative baseline
         - Approve Epic baseline
         - Approve Feature baseline (Feature Request)
         - Approve cutover
       - Rows MAY be added for initiative-specific governance (e.g., “Approve architecture baseline”, “Approve data migration plan”), but SHOULD be kept stable and baseline-level.
       - RACI cells SHALL reference actors using the exact actor labels defined in the Role Definitions table above (no new actor labels introduced only inside the table).

    3) **T102-ADR-008-CLAUSE-003 (Maintenance Policy)**
       - Update the baseline only when roles/responsibilities materially change.
       - Treat baseline edits as governance changes; maintain traceability via proposal/completion references where applicable.

  **Alternatives Considered:**
  (a) Embed governance RACI inside each epic — rejected (duplication and drift).

  **Consequences:**
  (+) Reduces drift by enforcing a single baseline
  (+) Improves consistency across epics within an initiative
  (±) Requires initial discipline to keep epics delta-only

  **References:**
  `T102-GDR-008 (Organisation Baseline Standard)`,
  `T102-GDR-003 (Inheritance Model Standard)`,
  `T102-ADR-003 (Explicit Inheritance Model)`,
  `T102-ADR-004 (Decision Records Index)`,
  `T102-ADR-005 (ID Specification & Rules)`

  **Provenance:**
  - `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102A_governance_&_roadmap.md`

* **T102-ADR-009 (Governance Standards Specification)** {#t102-adr-009-governance-standards-spec}

  * **Context**

    The current `GDR` + `ADR` pairing encourages duplicated narrative (policy and rationale) and creates drift over time. A dedicated standards registry mechanism is required so normative obligations can be indexed and governed independently from decision rationale. This ADR defines the introduction and semantics of `STD` and is adopted by `T102-STD-009`.

  * **Decision**

    Establish `STD` as a normative Requirement ID (`RID`) token used to register enforceable standards and to decouple “what must be followed” from “why the choice was made”. `STD` items govern downstream artifacts via precedence rules in `T102-ADR-005`. Normative keyword interpretation is governed by `T102-CON-009`.

  * **Specification**

    * **T102-ADR-009-CLAUSE-001 (Semantics & Scope)**

      - **Category**: `STD` is a normative `RID` token representing an enforceable standard.
      - **Creation Scope**: `STD` MUST only be created at Program (`P`), Initiative (`I`), Epic (`E`), and Feature (`F`) scopes.
      - **Reference Scope**: Artifacts at any scope MAY reference `STD`.
      - **Invalid Usage**: `STD` MUST NOT be used for informative guidance (`IG`) or integration notes (`INT`).

    * **T102-ADR-009-CLAUSE-002 (Adoption Contract)**

      - **Single Canonical Adopted Spec**: Every `STD` entry MUST declare exactly one `Adopts` reference.
      - **Incorporation by Reference**: The adopted normative specification is incorporated by reference into the `STD`. The `STD` remains the authoritative RID-level handle; the adopted spec is the canonical text.
      - **No Rationale Duplication**: `STD` bodies MUST NOT contain alternatives analysis or lengthy trade-offs. These MUST be captured in ADRs.

    * **T102-ADR-009-CLAUSE-003 (Precedence & Variance)**

      - **Precedence**: `STD` is a `RID` and therefore takes precedence over `DRID` items per `T102-ADR-005-CLAUSE-003`.
      - **Non-Contradiction Rule**: ADRs and lower-scope artifacts MUST NOT contradict applicable `STD` obligations.
      - **Variance Contract**: Any exception MUST be recorded as a Variance ADR and MUST cite the overridden `STD` ID.

    * **T102-ADR-009-CLAUSE-004 (STD Authoring Requirements)**

      - `STD` index schemas MUST follow `T102-ADR-009-CLAUSE-004A`.
      - `STD` index column guidelines MUST follow `T102-ADR-009-CLAUSE-004B`.
      - `STD` body construction MUST follow `T102-ADR-009-CLAUSE-004C`.
      - `STD` body conciseness targets MUST follow `T102-ADR-009-CLAUSE-004D`.
      - `STD` drift controls MUST follow `T102-ADR-009-CLAUSE-004E`.

      * **T102-ADR-009-CLAUSE-004A (STD Index Schema)**

        - **STD Index Requirement**: Each scope MUST maintain a `STD` index table using this schema:
          `| STD ID | Title | Status | Owner | Effective | Supersedes | Adopts | Verification | Governed By | Reference |`

      * **T102-ADR-009-CLAUSE-004B (STD Index Column Guidelines)**

        - `STD ID`: MUST follow `T102-ADR-005-CLAUSE-001`.
        - `Title`: MUST be bold and follow `T102-ADR-005-CLAUSE-001` title constraints.
        - `Adopts`: MUST contain exactly one full reference to the canonical adopted normative specification.
        - `Verification`: MUST describe (a) mechanism (CI/Lint/Review), (b) what is checked, and (c) pass/fail evidence.
        - `Governed By`:
          - MUST list the governing basis used to author and maintain the STD (meta-governance) such as program governance (`P-*`) once established.
          - SHOULD include the minimal set of always-applicable governance sources (do not overload).
          - Items in `Governed By` are treated as **authoring/control obligations** (i.e., “these rules apply when producing/maintaining this STD”).
        - `Reference`:
          - MUST be treated as **supporting / traceability** references only (not “governing” and not “adoption”).
          - MUST contain ONLY `RID`-category IDs (e.g., `STD/CON/QG/DEP/IF/...`) per `T102-ADR-005-CLAUSE-002`.
          - MUST NOT include `DRID`/`CLAUSE` IDs; those belong in `Governed By` (if governing) or inside the adopted spec itself.
          - References MUST obey `T102-ADR-005-CLAUSE-003` directionality (no higher-scope STD referencing lower-scope IDs except permitted `INT` exception patterns).

      * **T102-ADR-009-CLAUSE-004C (STD Body Construction)**

        - **Primary Obligation Sentence (required)**:
          - Format: `* **<SID>-STD-### (<Title>)** — <Normative obligation sentence>`
          - The obligation sentence MUST answer “WHAT must be true” at a stable, scope-wide level.
        - **Minimum Viable Conformance (MVC) (recommended; max 5 items)**:
          - MVC provides the minimum stable “WHAT” checkpoints required to conform, without restating the full adopted specification.
          - MVC items MUST be written as an ordered list (e.g., `1)` ...).
          - MVC items SHOULD cite adopted-spec clause IDs where possible (e.g., `T102-ADR-003-CLAUSE-001`).
          - MVC items MUST NOT introduce new obligations beyond the adopted specification; if a mismatch occurs, the adopted specification remains canonical.

      * **T102-ADR-009-CLAUSE-004D (STD Conciseness)**

        - STD bodies SHOULD target <200 words when feasible (excluding tables), aligning with `T102-ADR-005-CLAUSE-006 (Content Quality)`.
        - Pragmatic migration exception: if `Adopts = —` is explicitly intentional, the STD body MAY extend (target ≤300 words) to remain actionable until a canonical adopted spec is available.

      * **T102-ADR-009-CLAUSE-004E (Drift Controls)**

        - STD bodies MUST avoid duplicating detailed rules; the adopted normative specification is the single canonical source of truth.
        - If an adopted specification is updated in a way that changes conformance expectations, the corresponding STD body (including MVC) MUST be updated in the same change set.
        - When `STD` bodies are copied into SSOT artifacts (e.g., `sps`), those SSOT copies MUST be updated in the same change set whenever the authoritative STD body changes.

    * **T102-ADR-009-CLAUSE-005 (Migration Tolerance)**

      - **Alias Window**: During migration, legacy `GDR` IDs MAY be treated as aliases of their replacement `STD` IDs for enforcement.
      - **No New GDR**: New `GDR` creation MUST be blocked after the migration cutoff milestone/date.
      - **Sunset**: Alias support MUST be removed after the migration completion milestone/date.

  * **Alternatives Considered**

    - **Keep GDR + ADR pairing** — rejected due to predictable narrative duplication and drift.
    - **Make ADR the only DRID and place all standards in ADR** — rejected because it collapses normative reference and rationale, reintroducing “spec overload”.
    - **Adopt Option B immediately (separate standard docs)** — deferred to reduce migration complexity; planned as the next evolution once `STD` registry stabilizes.

  * **Consequences**

    (+) Establishes a stable standards registry (`STD`) and separates “rules” from “reasons”.
    (+) Reduces duplication by requiring standards to adopt canonical specs rather than restating them.
    (+) Enables stronger lint/CI validation through uniform STD index schema and adoption contract.
    (±) Requires clear author training on where obligations vs rationale belong.
    (-) Introduces additional artifacts (STD + adopted spec + ADR rationale) that must be maintained with disciplined linkage.

  * **References**

    `T102-STD-009 (Governance Standards Model)`,
    `T102-STD-005 (ID Governance Standard)`,
    `T102-CON-009 (Normative Keywords)`

#### 2. Epic ADR Index

##### i. `T102A` Epic: `SPS` — Synthesized Problem Statement Workflow

| ADR ID | Title | Authority STD | Status | Owner | Effective | Supersedes | Canonical Path |
|:-------|:------|:--------------|:-------|:------|:----------|:-----------|:---------------|
| `T102A-ADR-001` | Governance & Roadmap Snapshot | — | Proposed | Client | 2026-01-11 | — | `prompt/artifacts/tasks/T102/consultant/standards/T102A-ADR-001_governance-roadmap-snapshot.md` |
| `T102A-ADR-002` | Feature Register Index | — | Proposed | Client | 2026-01-11 | — | `prompt/artifacts/tasks/T102/consultant/standards/T102A-ADR-002_feature-register-index.md` |

* **T102A-ADR-001 (Governance & Roadmap Snapshot) — {#t102a-adr-001-governance-roadmap-snapshot}**

  **Context:** Per `T102A-GDR-001 (Governance Snapshot Standard)`, each Epic in an SPS must include a concise governance & roadmap snapshot that preserves traceability into living plans without importing operational planning detail into the SPS.

  **Decision:** Adopt `T102A-ADR-001`, establish a single, mandatory structure and maintenance policy for every Epic subsection titled **“Governance & Roadmap”**.

  **Specification:**

    1) **T102A-ADR-001-CLAUSE-001 (Canonical Placement & Title)**
       - Each Epic dossier SHALL include a subsection titled exactly: `##### iv. Governance & Roadmap`.
       - The subsection SHALL appear after `Inherited Considerations` and before `Feature Register` in the Epic dossier skeleton.

    2) **T102A-ADR-001-CLAUSE-002 (Section Structure)**
       The section SHALL contain, in this order:
       - **Scope & Ownership**
       - **Phase & Gates** (table; indicative; no fixed dates)
       - **References**

    3) **T102A-ADR-001-CLAUSE-003 (Scope & Ownership Rules)**
       - Scope & Ownership SHALL name the Decision Owner and the Epic Lead at minimum.
       - If present, Initiative Lead, Research Authority, and Technical Authority MAY be listed for clarity.
       - Scope & Ownership SHOULD include a single baseline reference line pointing to the initiative-level Org baseline (see `T102-ADR-008`).

    4) **T102A-ADR-001-CLAUSE-004 (Baseline Alignment)**
       - The initiative-level **Organization & Responsibilities** SHALL be defined in `III.B` and treated as the canonical source of truth (see `T102-ADR-008 (Organisation Baseline Standard)`).
       - The Epic dossier SHALL NOT duplicate baseline RACI. Instead, the Epic’s Governance & Roadmap section SHALL:
         - reference the baseline, and
         - express epic-specific execution signals via the **Phase & Gates** table (Phase Lead and gate exits).

    5) **T102A-ADR-001-CLAUSE-005 (Org & Responsibilities Boundaries)**
       - Org & Responsibilities SHALL map responsibilities only for governance events (phase/baseline approvals and handoffs).
       - Org & Responsibilities SHALL NOT include story/task-level responsibility assignment.
       - Feature lead/ownership remains a Feature Register concern (governed by `T102A-ADR-002`).

    6) **T102A-ADR-001-CLAUSE-006 (Phase & Gates Contract)**
       The **Phase & Gates** table SHALL use this exact schema:
       - `Phase | Title | Intent | Key Exit Milestone | Duration Band | Gate Approver (A) | Phase Lead (R) | Plan Link`
       Fill rules:
       - `Phase`: numeric phase sequence starting at 0.
       - `Title`: short, Title Case with **bold heading**; stable across minor plan revisions.
       - `Intent`: one sentence describing purpose; governance-level, not task-level.
       - `Key Exit Milestone`: one sentence describing the approval-ready exit signal (evidence-linked where possible).
       - `Duration Band`: optional band (e.g., “1–2 sessions”); SHALL be `—` if unknown.
       - `Gate Approver (A)`: the Decision Owner role for phase exit (typically `Client`).
       - `Phase Lead (R)`: the accountable coordinator for producing the exit package (typically `LLM_Consultant`).
       - `Plan Link`: repo-relative link to the plan artifact governing that phase; MAY be shared across phases, but SHOULD be split per phase over time.

    7) **T102A-ADR-001-CLAUSE-007 (Operational Boundaries)**
       - Governance & Roadmap SHALL NOT contain sprint calendars, capacity plans, or WBS task breakdown.
       - Story-level acceptance criteria belong in Feature Requests and Stories, not in the Phase & Gates table.

    8) **T102A-ADR-001-CLAUSE-008 (References Semantics)**
       - References SHOULD link to the external PM tracking system (if used) and evidence artifacts for gate completion (proposals/completions/validation notes).
       - References SHOULD include evidence links for checkpoint completion when available (proposal approvals, completion artifacts, validation notes).
       - References SHOULD NOT duplicate plan links already present in the Phase & Gates table.

    9) **T102A-ADR-001-CLAUSE-009 (Maintenance Policy)**
       - The Governance & Roadmap snapshot SHALL be updated only when a phase gate is approved or when a material governance baseline change occurs.
       - Day-to-day schedule drift remains in plan artifacts / external PM tools referenced from the snapshot.

  **Alternatives Considered:**
  (a) Embed operational plans inside SPS — rejected (creates churn and breaks governance snapshot intent).
  (b) Remove roadmap/checkpoints from SPS entirely — rejected (reduces governance visibility and weakens handoff oversight).

  **Consequences:**
  (+) Separates stable governance snapshot from living plans while preserving traceability.
  (+) Reduces role confusion by splitting “owner roster” from “gate responsibilities”.
  (+) Enables consistent epic governance reporting across initiatives.
  (±) Requires discipline: only update the snapshot at gates/baseline changes.
  (-) Some existing epics may require refactor to align with the baseline/delta model.

  **References:**
  `T102A-GDR-001 (Governance Snapshot Standard)`,
  `T102A-GDR-002 (Governance Freeze Standard)`,
  `T102-ADR-004 (Decision Records Index)`,
  `T102-ADR-005 (ID Specification & Rules)`,
  `T102-ADR-008 (Organisation Baseline Standard)`,
  `T102A-ADR-002 (Feature Register Index)`,
  `T102-RES-002 (Roadmap Viability)`,
  `T102A-RES-001 (SPS Workflow Optimization)`

  **Provenance**
  `concept_T102-CONSULTANT.md`
  `report_T102-CONSULTANT_roadmap-viability.md`
  `report_T102A-SPS_sps-workflow-optimization.md`

* **T102A-ADR-002 (Feature Register Index) — {#t102a-adr-002-feature-register-index}**

  **Context:** Per `T102A-GDR-001 (Governance Snapshot Standard)`, each Epic dossier must be governance-readable while preserving traceability into living artifacts. Feature scope lists were previously embedded inside Governance & Roadmap, causing churn and mixing governance with scope inventory.

  **Decision:** Adopt `T102A-ADR-002` as the mandatory standard for Epic Feature Register placement, schema, and maintenance policy.

  **Specification:**

    1) **T102A-ADR-002-CLAUSE-001 (Canonical Placement & Title)**
       - Each Epic dossier SHALL include a subsection titled exactly: `##### v. Feature Register`.
       - The subsection SHALL appear after `Governance & Roadmap` and before `Epic Requirements`.

    2) **T102A-ADR-002-CLAUSE-002 (Table Contract)**
       The Feature Register table SHALL use this exact schema:
       - `ID | Code | Title | Description | Feature Lead (R) | Status | Canonical Link (Request)`
       Fill rules:
       - `ID`: the Feature scope identifier (e.g., `T801A1`).
       - `Code`: short feature code (e.g., `BACKEND`, `PROMPT`).
       - `Title`: human-readable feature name with **bold heading**.
       - `Description`: one sentence; scope-level, not design-level.
       - `Feature Lead (R)`: the responsible coordination role for the Feature (typically `LLM_Consultant`).
       - `Status`: one of the allowed status values (see `T102A-ADR-002-CLAUSE-003`).
       - `Canonical Link (Request)`: repo-relative link to the Feature Request artifact once created; SHALL be `—` prior to request creation.

    3) **T102A-ADR-002-CLAUSE-003 (Allowed Status Values; Minimal Set)**
       Feature Register status SHALL be one of:
       - `proposed`, `in-request`, `approved`, `in-build`, `done`, `deferred`, `dropped`

    4) **T102A-ADR-002-CLAUSE-004 (Status Transition Rules)**
       - `proposed → in-request`: when a Request artifact is created (draft).
       - `in-request → approved`: when the Decision Owner approves the Request.
       - `approved → in-build`: when implementation begins.
       - `in-build → done`: when acceptance evidence exists and is recorded.
       - `* → deferred`: Decision Owner explicitly defers.
       - `* → dropped`: Decision Owner explicitly removes from scope.

    5) **T102A-ADR-002-CLAUSE-005 (Change Control & Stability)**
       - Adding/removing a Feature row is a governance baseline change and MUST be traceable (proposal/completion reference).
       - Feature Register SHALL remain an index only; detailed requirements/design belong in Feature Request artifacts.

  **Alternatives Considered:**
  (a) Keep Feature Register inside Governance & Roadmap — rejected (increases churn; mixes scope inventory with governance snapshot).
  (b) Move Feature Register to Concept only — rejected (reduces visibility in the SSOT epic dossier).

  **Consequences:**
  (+) Keeps Governance & Roadmap stable while preserving scope visibility
  (+) Enforces traceability: each feature has a canonical Request link
  (±) Requires discipline to treat register changes as baseline events

  **References:**
  `T102A-GDR-001 (Governance Snapshot Standard)`,
  `T102-ADR-004 (Decision Records Index)`,
  `T102-ADR-005 (ID Specification & Rules)`,
  `T102-RES-002 (Roadmap Viability)`

  **Provenance:** None


##### ii. `T102B` Epic: `REQUEST` — Request Workflow

| ADR ID | Title | Authority STD | Status | Owner | Effective | Supersedes | Canonical Path |
|:-------|:------|:--------------|:-------|:------|:----------|:-----------|:---------------|
| `T102B-ADR-001` | **Request Architecture Standard** | `T102B-STD-001 (Request Governance Snapshot Standard)` | Proposed | LLM_Consultant | — | — | [T102B-ADR-001](../../standards/T102B-ADR-001_request-architecture-standard.md) |
| `T102B-ADR-002` | **Section Classification Standard** | `T102B-STD-004 (Section Classification Policy)` | Proposed | LLM_Consultant | — | — | [T102B-ADR-002](../../standards/T102B-ADR-002_section-classification-standard.md) |
| `T102B-ADR-003` | **Story FR Deferral Standard** | `T102B-STD-002 (Workflow Typology Standard)` | Proposed | LLM_Consultant | — | — | [T102B-ADR-003](../../standards/T102B-ADR-003_story-fr-deferral-standard.md) |
| `T102B-ADR-004` | **Request Lite Specification** | `T102B-STD-002 (Workflow Typology Standard)` | Proposed | LLM_Consultant | — | — | [T102B-ADR-004](../../standards/T102B-ADR-004_request-lite-specification.md) |

##### iii. `T102C` Epic: `CONCEPT` — Concept Workflow

| ADR ID | Title | Authority STD | Status | Owner | Effective | Supersedes | Canonical Path |
|:-------|:------|:--------------|:-------|:------|:----------|:-----------|:---------------|
| `T102C-ADR-001` | Concept Architectural Framework | `T102C-GDR-001` | Proposed | — | 2025-09-28 | — | #t102c-adr-001-concept-framework |

* **T102C-ADR-001 (Concept Architectural Framework) {#t102c-adr-001-concept-framework}**

  **Context** Per accepted GDRs `T102C-GDR-003/005`, Concept requires comprehensive architectural specification for handoff authority and readiness aggregation. External research validates hybrid approach with centralized handoff locus and manual DoR-based status tracking. Current T102C-CST/CPG features need high-level architectural guidance to ensure industry-aligned implementation during Request development phase.

  **Decision** Implement Concept as Dynamic Workspace + Authoritative Handoff Framework through standardized architectural specification:

  - **Why**: Establish single source of truth for handoff authority while maintaining lean readiness visibility per industry best practices (SAFe, 42010, Team Topologies)
  - **What**: Eight-section Concept architecture with ADR compendium, handoff snapshot, and readiness aggregation capabilities following "link-don't-duplicate" principle
  - **Benefit**: Enables consistent handoff authority, reduces cognitive load, and provides Client orchestration visibility without automation overhead

  **Specification**

  1. **T102C-ADR-001-CLAUSE-001 (Core Architecture)** Concept artifacts SHALL implement eight-section structure: Identity & Operating Rules, Executive Context, Decision System (ADR Compendium), Readiness Snapshot, Handoff Snapshot, Registers, Integration & Interfaces, Governance per external research recommendations.
  2. **T102C-ADR-001-CLAUSE-002 (Handoff Authority)** Section V (Handoff Snapshot) SHALL serve as authoritative handoff locus containing: Package Manifest (immutable IDs/versions), Acceptance Signals (Client sign-off), Completeness Checklist (ADR accepted, FRs approved, risks linked), Links (SPS/Request/Design anchors, no copy-paste) per T102C-GDR-003.
  3. **T102C-ADR-001-CLAUSE-003 (Readiness Aggregation)** Section IV (Readiness Snapshot) SHALL implement manual YAML roll-up table with Initiative/Epic/Feature states, Ready markers at 80% DoR threshold, Client override capability, and "Top 3 blockers" visibility per T102C-GDR-005.
  4. **T102C-ADR-001-CLAUSE-004 (Implementation Deferral)** Detailed structural templates and procedural guidelines SHALL be specified within T102C-CST and T102C-CPG feature Request artifacts to maintain separation between architectural framework (Epic ADR) and implementation specification (Feature Request).

  **Alternatives Considered** 
  (a) Distributed handoff model (rejected): Research shows increased drift and unclear authority; conflicts with established single source of truth patterns 
  (b) Automated readiness tracking (rejected): Violates T102-CON-002 minimal automation constraint; adds complexity without proven v1 need 
  (c) Monolithic ADR specification (rejected): Creates premature implementation detail; conflicts with Epic/Feature separation per `T102-GDR-001`

  **Consequences** 
  (+) Industry-validated architecture aligned with SAFe, 42010, and Team Topologies best practices 
  (+) Clear handoff authority eliminates decision drift and cognitive load per research findings 
  (+) Maintains Epic/Feature boundary separation while providing comprehensive architectural guidance 
  (±) Requires disciplined adherence to "link-don't-duplicate" principle and manual readiness maintenance 
  (-) Implementation details deferred to Feature Request development phase

  **References** 
  `T102C-GDR-003 (Handoff Authority Standard)`, 
  `T102C-GDR-005 (Readiness Aggregation Standard)`, 
  `T102C-QG-001 (ADR Centralization)`, 
  `T102C-QG-003 (Template Reusability)`, 
  `T102C-DEP-001 (SPS Integration)`

  **Provenance** prompt/artifacts/tasks/T102/consultant/research/report/report_handoff-aggregation_T102C_v1.0.0_i1.md



#### 3. Feature ADR Index  
| ADR ID | Title | Authority STD | Status | Owner | Effective | Supersedes | Canonical Path |
|:-------|:------|:--------------|:-------|:------|:----------|:-----------|:---------------|
| `T102A-SPSST-ADR-0001` | Approvals in body | — | Accepted | Client | — | — | `prompt/artifacts/tasks/T102/consultant/standards/T102A-SPSST-ADR-0001_approvals-in-body.md` |

Legacy source link (pre-extraction): `../design/design_T102A-SPSST-S1.md#adr-0001`

### C. Readiness Snapshot (Lean, manual)
<!-- 
- **A. Roll-up Table** (Initiative/Epics/Features: State | Ready? | Top blockers | Next gate | Updated_at)
- **B. DoR Checklists (brief)** per tier (links to Request/Design for evidence)
- **C. Notes & Overrides** (Client approvals recorded with ID)
-->
### D. Handoff Snapshot (Authoritative)
<!-- 
- **A. Package Manifest** (immutable IDs, doc versions/SHAs)
- **B. Acceptance Signals** (Client sign-off, gate approvals)
- **C. Completeness Checklist** (ADR accepted; FRs approved; risks linked)
- **D. Links** (SPS/Request/Design anchors; no copy-paste)
-->
### E. Registers 
<!-- 
- Risks/Assumptions/Dependencies registers (pointer-based; no duplication)
-->
#### 1. Feature Register

#### 2. Design Register
| Epic ID | Feature ID | Story ID | Design Log | Status | Notes |
| :------ | :--------- | :------- | :--------- | :----- | :---- |
| T102A | T102A-SPSST | T102A-SPSST-S1 | ../design/design_T102A-SPSST-S1.md | review | … |
| T102A | T102A-SPSST | T102A-SPSST-S3 | ../design/design_T102A-SPSST-S3.md | review | … |
| T102A | T102A-SPSST | T102A-SPSST-S4 | ../design/design_T102A-SPSST-S4.md | review | … |

#### 3. Research Artifacts Register

| Scope | Scope ID | Research ID | Title | Summary | Reference | Brief | Report | Source |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Initiative | `T102` | `T102-RES-001` | **Research Integration Governance** | Established three-tier placement strategy, LLM quality control framework, RES-### ID system; recommended dedicated Epic T102E for implementation | `T102-ISSUE-005`, `T102-GDR-006`, `T102-GDR-007` | [brief](../research/brief/brief_T102-CONSULTANT_research-integration-workflow_v1.0.0.md) | [report](../research/report/report_T102-CONSULTANT_research-integration-workflow_v1.0.0.md) | `../sps/sps_T102-CONSULTANT_v1.1.0.md#research--notes` |
| Initiative | `T102` | `T102-RES-002` | **Roadmap Viability** | Confirmed governance snapshot approach aligns with PRINCE2/PMI/SAFe standards; validated hybrid model with governance milestones in SPS and operational plans external | `T102A-GDR-001`, `T102C-GDR-003`, `T102C-GDR-005` | [brief](../research/brief/brief_T102-CONSULTANT_roadmap-viability_v1.0.0.md) | [report](../research/report/report_T102-CONSULTANT_roadmap-viability_v1.0.0.md) | `../sps/sps_T102-CONSULTANT_v1.1.0.md#research--notes` |
| Epic | `T102A` | `T102A-RES-001` | **SPS Workflow Optimization** | Validated emergent governance freeze, handoff criteria, procedural workflows; established 10-point readiness checklist | `T102A-ISSUE-002`, `T102A-ISSUE-003`, `T102A-GDR-002` | [brief](../research/brief/brief_T102A-SPS_sps-workflow-optimization_v1.0.0.md) | [report](../research/report/report_T102A-SPS_sps-workflow-optimization_v1.0.0.md) | `../sps/sps_T102-CONSULTANT_v1.1.0.md#vi-epic-research--notes` |
| Epic | `T102C` | `T102C-RES-001` | **Handoff Aggregation** | Validated T102C-GDR-003 and T102C-GDR-005 handoff authority and readiness aggregation patterns | `T102C-GDR-003`, `T102C-GDR-005`, `T102C-NOTE-003` | [brief](../research/brief/brief_T102C-CONCEPT_handoff-aggregation_v1.0.0.md) | [report](../research/report/report_T102C-CONCEPT_handoff-aggregation_v1.0.0.md) | `../sps/sps_T102-CONSULTANT_v1.1.0.md#vi-epic-research--notes` |



### F. Integration & Interfaces
<!-- 
- Planner consumption notes (schema, payload outline), cross-traceability rules.
-->


### G. Governance

<!-- 
- Local GDRs for Concept (e.g., T102C-GDR-003/005 once accepted) + change control.
-->
