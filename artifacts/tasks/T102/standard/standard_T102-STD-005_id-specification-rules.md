# T102-STD-005 — ID Specification & Rules

> **Superseded**: This standard has been superseded by `P-STD-005 (Universal ID Specification)` at Program scope.
>
> - Successor: `P-STD-005 (Universal ID Specification)` at `prompt/artifacts/tasks/P/standard/standard_P-STD-005_universal-id-specification.md`
> - Superseded on: 2026-02-23
> - Alias window: `T102-STD-005-CLAUSE-*` references MAY be treated as aliases for `P-STD-005-CLAUSE-*` during the defined migration window. Alias support is removed after the Governance Sync Changeset "P-STD-005 Alias Removal" is executed.

## Specification

1) **T102-STD-005-CLAUSE-001 (Canonical ID Schema)**

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
    - **DRIDs / STDCIDs / DRCIDs**: Target: 2–4 words; Min: 2 words; Max: 8 words.
     - Hyphenated compounds count as 1 word.
   - Description: concise statement of the rule/requirement/decision/guidance.

2) **T102-STD-005-CLAUSE-002 (Taxonomy & Terminology)**

   **Category Key**:
   - `SID` (Scope)
   - `RESID` (Research)
   - `RID` (Requirement)
   - `STDCID` (Standard Clause)
   - `DRID` (Decision Record)
   - `DRCID` (Decision Record Clause, legacy)
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
   - Program IDs MUST use the `P-<TOKEN>-###` format per `T102-STD-005-CLAUSE-001`.
   - Any ID MAY be **re-scoped** (promoted or demoted) across `P/I/E/F/S` when its applicability changes, subject to `T102-STD-005-CLAUSE-003 (Precedence & Hierarchy)` and the re-scope contract in `T102-STD-005-CLAUSE-003A`.

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
   | `STDCID` | `CLAUSE` | **Standard Clause** | P, I, E, F | STD-internal clause ID used only within the parent STD combined file. Construction is `<STD-ID>-CLAUSE-###`; scope and authority derive from the parent STD. |
   | `DRID` | `ADR` | **Architectural Decision** | P, I, E, F, S | Technical implementation decision record. Construction MAY be standalone (`<SID>-ADR-###`) or STD-nested (`<STD-ID>-ADR-###`) per `T102-STD-005-CLAUSE-005F`. |
   | `DRCID` | `CLAUSE` | **Decision Record Clause** `[LEGACY — migration to STDCID in progress]` | P, I, E, F, S | Legacy ADR-internal clause ID used within the parent ADR (`<ADR-ID>-CLAUSE-###`) during migration alias windows per `T102-STD-005-CLAUSE-003B`. |
   | `IID` | `IG` | **Implementation Guidance** | I, E, F | Informative how-to guidance: patterns, templates, and examples. MUST NOT introduce new obligations. Not a substitute for system requirements. |
   | `IID` | `INT` | **Integration Guidance** | I, E, F, S | Non-normative integration and cross-scope coordination guidance for external audiences; MUST NOT introduce new obligations. |
   | `OID` | `NOTE` | **Note** | I, E, F, S | Non-normative context; do not use for obligations. |
   | `OID` | `ISSUE` | **Issue** | I, E, F | Known gap requiring resolution. |
   | `OID` | `RISK` | **Risk** | I, E, F | Potential negative event requiring mitigation. |

3) **T102-STD-005-CLAUSE-003 (Precedence & Hierarchy)**

   **Directionality**: Inheritance flows downstream with scopes only.
   - Correct: Story references Feature; Feature references Epic; Epic references Initiative; Initiative references Program.
   - Incorrect: Higher scope references lower scope, except:
     - **INT scoped exception**: Feature/Story-scope `INT` items MAY reference peer Feature RIDs for coordination per `T102-STD-005-CLAUSE-005C (Integration Guidance Rules)`.
     - **Audit register exception**: Concept audit-surface registers MAY reference downstream artifact IDs for inventory/audit purposes when explicitly labeled **pointers-only** and **non-normative**. This exception MUST NOT be used to introduce upstream obligations, and it does not change inheritance/obligation directionality.

   **Precedence Order** (Highest to Lowest):
   - Program > Initiative > Epic > Feature > Story

   **Category Precedence** (within same scope):
   `SID > RESID > RID > STDCID > DRID > DRCID [legacy] > IID (IG > INT) > OID`

   **Evidence Conflict Rule**:
   If `RESID` contradicts a `RID` or `DRID`, it triggers a Review workflow (ISSUE + Change Decision). Evidence does not “silently override” obligations.

   **Variances**:
   Any downstream ID deviating from an upstream rule MUST cite the overridden ID explicitly in a “Variance ADR”.

   * **T102-STD-005-CLAUSE-003A (Cross-Scope Re-scope / Promotion Contract)**
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

   * **T102-STD-005-CLAUSE-003B (Alias Window for Re-scope Transitions)**
     - During a defined migration window, superseded IDs MAY be treated as aliases of their replacement IDs for lint/enforcement.
     - Alias support MUST be removed after the migration completion milestone/date.

4) **T102-STD-005-CLAUSE-004 (Reference Semantics)**

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

5) **T102-STD-005-CLAUSE-005 (Category Semantics)**

   This clause provides a concise semantic overview. Tokens with lifecycle/exception behavior have dedicated subclauses. 

   * **T102-STD-005-CLAUSE-005A (Assumption Lifecycle)**

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

   * **T102-STD-005-CLAUSE-005B (Implementation Guidance Rules)**

     **Normative Standard**:
     - IG MAY use MUST/SHALL when defining implementation and authoring standards intended to be enforceable.
     - IG MUST NOT be used to express software behavior requirements; use `FR`/`NFR`/`CON` for system requirements.

     **Role**:
     - Detailed patterns, pseudo-code, templates, examples, and internal process guidance.
     - Expands on governing RIDs/DRIDs with implementable standards without duplicating upstream requirements text.

     **Scope Granularity**:
     - **Initiative/Epic Scope**: Focus on high-level patterns, templates, and principles.
     - **Feature/Story Scope**: Focus on specific implementation details, code examples, and procedural steps.

   * **T102-STD-005-CLAUSE-005C (Integration Guidance Rules)**

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
     - **Promotion enforcement**: If an `INT` item is referenced as relied-upon policy in **2+ artifacts** or across **2+ Epics**, it MUST be promoted into an authoritative artifact within the **next governance review cycle**:
       - Promote to `RID` when the rule is an enforceable obligation/constraint/requirement.
       - Promote to `STD` when the rule is a generally applicable authoring/governance standard.
       - Promote to `ADR` when the rule is an architectural decision requiring rationale + alternatives.
     - The originating `INT` MUST be updated to reference the promoted authoritative ID and MUST NOT continue to serve as the policy source.
     - **Anti-pattern boundary**: `INT` MUST NOT be used as a substitute for authoritative indices, registers, or enforceable obligations.

   * **T102-STD-005-CLAUSE-005D (Specification Clause Semantics)**

     **Role**  
     Define the allowed construction, subclause construction, and semantics of `CLAUSE` IDs for STD-internal specification clauses (`STDCID`) and legacy ADR-internal clause aliases (`DRCID`).

     **Construction**
     - Current format (STDCID): `<STD-ID>-CLAUSE-###`. e.g. `P-STD-001-CLAUSE-004`
     - Legacy alias format (DRCID): `<ADR-ID>-CLAUSE-###`. e.g. `P-STD-001-CLAUSE-004`
     - `###` is a 3-digit sequence local to the parent artifact (starts at `001`).
     - Optional subclause suffix:
       - Current: `<STD-ID>-CLAUSE-###<CAPITAL_LETTER>` (e.g. `P-STD-001-CLAUSE-004A`)
       - Legacy alias: `<ADR-ID>-CLAUSE-###<CAPITAL_LETTER>` (e.g. `P-STD-001-CLAUSE-004A`)

     **Semantics**
     - `CLAUSE` IDs represent **enforceable Specification clauses** and MUST be written as normative statements (`MUST`/`SHALL`).
     - Non-normative guidance MUST use `IG`/`INT`/`NOTE` (not `CLAUSE`).
     - A `CLAUSE` ID has **no independent precedence** outside its parent authority envelope:
       - `Authority(<STD-ID>-CLAUSE-###) = Authority(<STD-ID>)`
       - During migration alias windows, `Authority(<ADR-ID>-CLAUSE-###) = Authority(<STD-ID>-CLAUSE-###)` when mapped as an alias per `T102-STD-005-CLAUSE-003B`.

     **Migration Note**
     - Legacy `DRCID` constructions (`<ADR-ID>-CLAUSE-###`) MAY be treated as aliases during a defined migration window per `T102-STD-005-CLAUSE-003B`.
     - New authoring MUST use `STDCID` construction (`<STD-ID>-CLAUSE-###`).

     **Scope & Validity Constraints**
     - `CLAUSE` IDs MUST NOT be created as standalone items outside a parent STD/ADR body.
     - `CLAUSE` IDs MUST NOT be used to represent system requirements or non-normative guidance.
     - References to `CLAUSE` IDs MUST follow `T102-STD-005-CLAUSE-004 (Reference Semantics)` and MAY be used for precise cross-document traceability.
     - Rendering of Specification sections (including ordered-list and subclause formatting) MUST follow `P-STD-001-CLAUSE-018 (CLAUSE Construction Requirements)`.

   * **T102-STD-005-CLAUSE-005E (Notes Structure Semantics)**
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

   * **T102-STD-005-CLAUSE-005F (Standard Decision Record Semantics)**

     **Construction**
     - Format: `<STD-ID>-ADR-###`. e.g. `P-STD-001-ADR-001`
     - `###` is a 3-digit sequence local to the parent STD and identifies the current decision-record annex.

     **Semantics**
     - A Standard Decision Record (`DRID`) is an informative rationale annex nested within its parent STD combined file.
     - Standard `CLAUSE` IDs remain the normative authority surface; the nested ADR documents rationale and governance history.
     - Authority is informative:
       - `Authority(<STD-ID>-ADR-###) = informative`

     **Lifecycle**
     - The nested ADR uses an update-in-place lifecycle within the parent STD file.
     - Superseded rationale versions MUST be tracked via changelog and/or git history rather than proliferating parallel current ADRs.

     **Constraint**
     - Each STD combined file MUST have only one current nested ADR at a time.

6) **T102-STD-005-CLAUSE-006 (Content Quality)**

   **Quality Criteria**:
   - **RID**: Lead with a requirement statement when applicable (SHALL/SHOULD). No justification prose (put rationale in NOTE). Prefer one primary obligation per RID.
   - **IID-IG**: Informative how-to guidance; may include templates, pseudo-code, and examples; MUST NOT introduce new obligations.
   - **IID-INT**: Non-normative integration notes; MUST NOT introduce new obligations (see `T102-STD-005-CLAUSE-005C`).
   - **DRID**: Follow `P-STD-001` body structure strictly.

   **Governance Mapping**:
   In governance-focused artifacts, inner clauses SHOULD be named `CLAUSE` (e.g., `T102-STD-005-CLAUSE-001`) to prevent confusion with Software Functional Requirements (`FR`). Legacy `...-FR-###` clause IDs inside governance ADRs are treated as clause IDs during migration.

   **Conciseness**:
   RIDs target <200 words when feasible (excluding tables); IF schemas may exceed for clarity.

7) **T102-STD-005-CLAUSE-007 (ID Stability & Immutability)**

   - **Anchor Stability**: Anchors MUST remain stable even if Titles change slightly.
   - **Immutable IDs**: Once assigned, an ID is never reused. Deprecate it instead.
   - **Migration Tolerance**: Validators MAY allow legacy governance clause labels (e.g., `...-FR-###` inside governance ADRs) alongside `...-RULE-###` during migration, but new governance clauses SHOULD use `CLAUSE`.
   - **Legacy Standards Migration**: Migration tolerance for legacy governance standard identifiers is defined in `P-STD-001-CLAUSE-017 (Migration Tolerance)`.

## Decision Record

* **T102-STD-005-ADR-001 (ID Specification & Rules)** {#t102-std-005-adr-001-id-specification-and-rules}

  * **Context**
    Per `T102-STD-005 (ID Governance Standard)`, multiple artifact families use overlapping ID conventions (considerations, requirements, decisions) at different scopes. Without a single normative specification, authors improvise category tokens, anchors, and references, creating inconsistency and undermining inheritance, precedence, and verification.

  * **Decision**
    Standardize ID patterns across Initiative, Epic, Feature, and Story scopes; define category tokens, sub-ID patterns, anchors, and referencing rules. This ADR is the single specification adopted by `T102-STD-005` as its normative specification.

  * **Alternatives Considered**
    - Free-form, template-local ID schemes — rejected.
    - Enforcing full titles in all inline mentions — rejected.

  * **Consequences**
    (+) Predictable, machine-checkable IDs across artifacts.
    (+) Faster audits and safer cross-linking with stable anchors.
    (±) Requires discipline and small refactors for legacy items.

## References

`T102-STD-005 (ID Governance Standard)`,
`T102-STD-003 (Explicit Inheritance Model)`,
`P-STD-001 (Program Governance Standard)`,
`T102-STD-006 (Research Artifacts Index)`,
`T102-CON-009 (Normative Keywords)`

## Provenance

- `prompt/artifacts/tasks/T102/workspace/PH000/proposal/proposal_T102-CWD_refactor-adr-004-005.md`
- `prompt/artifacts/tasks/T102/ssot/concept_T102-CONSULTANT.md`
- `prompt/artifacts/tasks/T102/ssot/sps_T102-CONSULTANT.md`

| Superseded By | `P-STD-005` (Universal ID Specification) |
| Supersession Date | 2026-02-23 |
| Promotion Decision | `P-STD-005-ADR-002` |
