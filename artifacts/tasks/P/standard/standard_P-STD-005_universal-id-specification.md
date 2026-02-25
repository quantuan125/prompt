# P-STD-005 — Universal ID Specification {#p-std-005-universal-id-specification}
## Specification

### Specification Index
| # | Substandard | CLAUSE ID | Title | Description |
|:--|:--|:--|:--|:--|
| 1 | P-STD-005A | P-STD-005-CLAUSE-001 | Canonical ID Schema | Defines the canonical ID regex schema and rendering rules. |
| 2 | P-STD-005A | P-STD-005-CLAUSE-002 | Taxonomy & Terminology | Defines ID categories, tokens, and allowed scope semantics. |
| 3 | P-STD-005A | P-STD-005-CLAUSE-003 | Precedence & Hierarchy | Defines inheritance directionality and precedence rules. |
| 4 | P-STD-005A | P-STD-005-CLAUSE-004 | Reference Semantics | Defines reference styles, requirements, and external reference rules. |
| 5 | P-STD-005A | P-STD-005-CLAUSE-005 | Category Semantics | Defines semantics, lifecycle rules, and constraints per token category. |
| 6 | P-STD-005A | P-STD-005-CLAUSE-006 | Content Quality | Defines content quality criteria and governance mapping for governed artifact types. |
| 7 | P-STD-005A | P-STD-005-CLAUSE-007 | ID Stability & Immutability | Defines anchor stability, ID immutability, and migration tolerance rules. |
| 8 | P-STD-005B | P-STD-005-CLAUSE-008 | Timeline UID Schema | Defines timeline UID regex patterns and composition rules. |
| 9 | P-STD-005B | P-STD-005-CLAUSE-009 | UID-vs-Seq Decoupling | Defines immutable UIDs and display-order decoupling rules. |
| 10 | P-STD-005B | P-STD-005-CLAUSE-010 | LINK Indirection System | Defines LINK-### pointer system for register indirection. |
| 11 | P-STD-005B | P-STD-005-CLAUSE-011 | Timeline File Naming | Defines file naming conventions derived from timeline UIDs. |

### P-STD-005A — Workscope ID Governance


1) **P-STD-005-CLAUSE-001 (Canonical ID Schema)**

   This CLAUSE defines the canonical ID regex schema and rendering rules.

   * **P-STD-005-CLAUSE-001A (Regex Patterns)** — All IDs MUST match one of these patterns:
     Patterns are written in PCRE-compatible syntax. IDs are case-sensitive; no normalization, percent-encoding, or case-folding is applied. Subclause suffixes per `P-STD-005-CLAUSE-005D` are structural extensions and are exempt from top-level pattern validation.
     Patterns MUST be checked in this order: 4 → 2 → 3 → 1; the first match determines the ID type.

     - **Pattern 1 (Initiative/Epic/Feature/Story Scope ID / SID)**: `^T\\d{3}(?:[A-Z]\\d*)?(?:-[A-Z0-9_]+)*$`
       - Examples: `T102`, `T102A`, `T102A1-S3`, `T102A-SPSST`

     - **Pattern 2 (Initiative/Epic/Feature/Story Tokenized ID)**: `^T\\d{3}(?:[A-Z]\\d*)?(?:-[A-Z0-9_]+)*-[A-Z]+-\\d{3}$`
       - Examples: `T102-QG-001`, `T102A1-NFR-005`, `T102A-SPSST-IG-002`

     - **Pattern 3 (Program Tokenized ID)**: `^P(?:-[A-Z0-9_]+)*-[A-Z]+-\\d{3}$`
       - Examples: `P-STD-001`, `P-CON-001`, `P-ADR-001`

     - **Pattern 4 (Timeline UID)**: `^(?:P|T\\d{3}(?:[A-Z]\\d*)?)-PH\\d{3}(?:-ST\\d{3}(?:-AC\\d{3}(?:\\.\\d+)?(?:-TK\\d{3})?)?)?(?:-(?:SES\\d{3}(?:-(?:DP|DEC|ACT|OQ)\\d{3})?|GATE-\\d{3}))?$`
       - Examples (Phase): `P-PH000`, `T104-PH001`
       - Examples (Stream): `P-PH000-ST001`, `T104-PH001-ST002`
       - Examples (Activity): `P-PH000-ST001-AC006`, `T104-PH001-ST002-AC000`
       - Examples (Sub-Activity): `T102-PH001-ST001-AC009.1`
       - Examples (Task): `T102-PH001-ST001-AC009.1-TK003`
       - Examples (Session): `P-PH000-ST001-AC006-SES003`
       - Examples (Gate): `P-PH000-ST001-AC006-GATE-002`
       - Examples (Session Item — DP): `P-PH000-ST001-AC006-SES003-DP001`
       - Examples (Session Item — DEC): `P-PH000-ST001-AC006-SES003-DEC001`
       - Examples (Session Item — ACT): `T104-PH001-ST002-SES001-ACT001`
       - Examples (Session Item — OQ): `P-PH000-ST001-AC006-SES003-OQ001`

     3-digit sequences (`001`–`999`) represent the maximum range per pattern. Exceeding the ceiling requires introducing a new token or scope segment; digit width MUST NOT be expanded.
     > *Informative*: These patterns define ID syntax and classification. General resolution (mapping IDs to artifact locations) is handled by `P-STD-005-CLAUSE-010 (LINK Indirection System)` for timeline entities and by file naming conventions in `P-STD-005-CLAUSE-011 (Timeline File Naming)`. A general-purpose resolution mechanism for workscope IDs is out of scope for this specification.

   * **P-STD-005-CLAUSE-001B (Markdown Construction & Title Constraints)** — Defines rendering format and title word-count constraints for ID references in Markdown.
     - Format: `* **<ID> (<Title>)** — <Description>`
     - Title Constraints:
       - **RIDs / IIDs / OIDs**: Target: 2 words; Min: 2 words; Max: 3 words.
       - **DRIDs / STDCIDs**: Target: 2–4 words; Min: 2 words; Max: 8 words.
       - Hyphenated compounds count as 1 word.
     - Description: concise statement of the rule/requirement/decision/guidance.


2) **P-STD-005-CLAUSE-002 (Taxonomy & Terminology)**

   This CLAUSE defines ID categories, tokens, and allowed scope semantics.

   * **P-STD-005-CLAUSE-002A (Category Key & Allowed Scope Key)** — Defines the category and scope classification keys.

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

   * **P-STD-005-CLAUSE-002B (Token Table & Scope Semantics)** — Defines valid tokens, their allowed scopes, and usage semantics. Authors MUST select the most specific token available for the scope.

     | Category | Token | Name | Allowed Scope | Definition & Usage |
     |:---|:---|:---|:---|:---|
     | `SID` | `SCOPE` | **Project Management Scope** | P, I, E, F, S | Artifact Identifiers (e.g., `P`, `T102`, `T102A`). |
     | `RESID` | `RES` | **Research** | P, I, E, F | Commissioned research trace (Evidence). |
     | `RID` | `ASSUM` | **Assumption** | P, I, E, F | Unverified belief carrying risk. Must track validation status. |
     | `RID` | `CON` | **Constraint** | P, I, E, F | Non-negotiable boundary or limitation. |
     | `RID` | `QG` | **Quality Goal** | P, I, E | Initiative success metrics (e.g., traceability completeness, review turnaround). |
     | `RID` | `DEP` | **Dependency** | P, I, E | External condition, interface, asset, or approval required. |
     | `RID` | `IF` | **Interface** | P, I, E, F | Data/integration contract definition (contractual boundary). |
     | `RID` | `FR` | **Functional Requirement** | F, S | Testable system behavior (requirements language). |
     | `RID` | `NFR` | **Non-Functional Requirement** | F, S | Quality requirement expressed as testable metrics. |
     | `RID` | `STD` | **Standard** | P, I, E, F | Normative standards registry token. Enforceable obligations MUST be encoded in `STD` or in its adopted normative specification; governance rationale belongs in ADRs. |
     | `STDCID` | `CLAUSE` | **Standard Clause** | P, I, E, F | STD-internal clause ID used only within the parent STD combined file. Construction is `<STD-ID>-CLAUSE-###`; scope and authority derive from the parent STD. |
     | `DRID` | `ADR` | **Architectural Decision** | P, I, E, F, S | Technical implementation decision record. Construction MAY be standalone (`<SID>-ADR-###`) or STD-nested (`<STD-ID>-ADR-###`) per `P-STD-005-CLAUSE-005F`. |
     | `DRCID` | `CLAUSE` | **Decision Record Clause** `[LEGACY — migration to STDCID in progress; 12 files remain; resolved by Governance Sync Changeset "P-STD-005 Alias Removal"]` | P, I, E, F, S | Legacy ADR-internal clause ID used within the parent ADR (`<ADR-ID>-CLAUSE-###`) during migration alias windows per `P-STD-005-CLAUSE-003B`. |
     | `IID` | `IG` | **Implementation Guidance** | I, E, F | Informative how-to guidance: patterns, templates, and examples. MUST NOT introduce new obligations. Not a substitute for system requirements. |
     | `IID` | `INT` | **Integration Guidance** | I, E, F, S | Non-normative integration and cross-scope coordination guidance for external audiences; MUST NOT introduce new obligations. |
     | `OID` | `NOTE` | **Note** | I, E, F, S | Non-normative context; do not use for obligations. |
     | `OID` | `ISSUE` | **Issue** | I, E, F | Known gap requiring resolution. |
     | `OID` | `RISK` | **Risk** | I, E, F | Potential negative event requiring mitigation. |

     Timeline segment tokens (`PH`, `ST`, `AC`, `TK`, `SES`, `GATE`) and session item types (`DP`, `DEC`, `ACT`, `OQ`) are positional markers governed by `P-STD-005-CLAUSE-008`, not category tokens. They do not appear in this table.

   * **P-STD-005-CLAUSE-002C (Program Scope Rules)** — Defines rules specific to Program-scope (`P`) identifiers.
     - `P` denotes cross-initiative governance scope (program-level SSOT). `P-*` IDs MAY govern multiple initiatives.
     - Program IDs MUST use the `P-<TOKEN>-###` format per `P-STD-005-CLAUSE-001`.
     - Any ID MAY be **re-scoped** (promoted or demoted) across `P/I/E/F/S` when its applicability changes, subject to `P-STD-005-CLAUSE-003 (Precedence & Hierarchy)` and the re-scope contract in `P-STD-005-CLAUSE-003A`.

3) **P-STD-005-CLAUSE-003 (Precedence & Hierarchy)**

   **Precedence Order** (Highest to Lowest):
   - Program > Initiative > Epic > Feature > Story

   **Variances**:
   Any downstream ID deviating from an upstream rule MUST cite the overridden ID explicitly in a "Variance ADR".

   * **P-STD-005-CLAUSE-003A (Cross-Scope Re-scope / Promotion Contract)** — Governs promotion/demotion and required supersession/update mechanics for re-scoping across P/I/E/F/S.
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

   * **P-STD-005-CLAUSE-003B (Alias Window for Re-scope Transitions)** — Defines alias window allowance and removal requirement for re-scope migrations.
     - During a defined migration window, superseded IDs MAY be treated as aliases of their replacement IDs for lint/enforcement.
     - Alias support MUST be removed after the migration completion milestone/date.

   * **P-STD-005-CLAUSE-003C (Directionality Rules)** — Inheritance flows downstream with scopes only.
     - Correct: Story references Feature; Feature references Epic; Epic references Initiative; Initiative references Program.
     - Incorrect: Higher scope references lower scope, except:
       - **INT scoped exception**: Feature/Story-scope `INT` items MAY reference peer Feature RIDs for coordination per `P-STD-005-CLAUSE-005C (Integration Guidance Rules)`.
       - **Audit register exception**: Concept audit-surface registers MAY reference downstream artifact IDs for inventory/audit purposes when explicitly labeled **pointers-only** and **non-normative**. This exception MUST NOT be used to introduce upstream obligations, and it does not change inheritance/obligation directionality.

   * **P-STD-005-CLAUSE-003D (Category Precedence)** — Defines precedence within the same scope level.
     `SID > RESID > RID > STDCID > DRID > DRCID [legacy] > IID (IG > INT) > OID`

   * **P-STD-005-CLAUSE-003E (Evidence Conflict Rule)** — If `RESID` contradicts a `RID` or `DRID`, it triggers a Review workflow (ISSUE + Change Decision). Evidence does not "silently override" obligations.

4) **P-STD-005-CLAUSE-004 (Reference Semantics)**

   This CLAUSE defines reference styles, requirements, and external reference rules.

   * **P-STD-005-CLAUSE-004A (Reference Styles)** — Defines the two permitted reference formats.
     - **Short-hand (Inline):** `` `ID` `` (e.g., `T102-QG-001`, `T102B`)
     - **Full (Formal):** `` `ID (Title)` `` (e.g., `T102-QG-001 (Client Readability)`, `T102B (REQUEST)`)

   * **P-STD-005-CLAUSE-004B (Required Usage by Context)** — Defines when each reference style is required.
     - In-body prose (within ID bodies): Short-hand preferred
     - Dedicated sections (References, Tables): Full references required

   * **P-STD-005-CLAUSE-004C (External Reference Line)** — If a body references an ID from a different **scope root**, a standalone citation line MUST appear at the bottom of that body.
     - Scope roots are:
       - Program root: `P` (e.g., `P-STD-001`)
       - Initiative-family roots: `T###...` (e.g., `T102`, `T104A`, etc.)
     - Trigger condition:
       - Any `P-*` reference inside a `T###...` body, OR
       - Any cross-initiative-family reference (e.g., `T104...` inside `T102...`), OR
       - Any cross-epic variant where your initiative treats prefixes as separate roots (e.g., `T102B...` inside `T102A...`).
     - Format: `External Reference:` followed by one or more full references (`` `ID (Title)` ``).
     - This line MUST NOT be used for references within the same scope root.

   * **P-STD-005-CLAUSE-004D (Normative Body Constraint)** — Normative bodies MUST NOT reference `ISSUE` or `RISK` IDs inline. Issues/Risks capture the problem; RIDs/DRIDs capture the solution.

5) **P-STD-005-CLAUSE-005 (Category Semantics)**

   This clause provides a concise semantic overview. Tokens with lifecycle/exception behavior have dedicated subclauses. 

   * **P-STD-005-CLAUSE-005A (Assumption Lifecycle)** — Defines assumption table schema and lifecycle requirements.

     **Table Requirement**:
     Assumptions MUST be defined in a table structure preceding the list of ID bodies.

     **Schema**:
     `| ID | Title | Status | Validation Method | Timing | Owner | If Invalidated | CON Cross-Ref |`

     **Enum**:
     - Status: `{Pending, Validated, Invalidated, Modified}`

     **Lifecycle Requirements**:
     - Each ASSUM SHOULD specify a testable validation method and responsible party.
     - Each ASSUM MUST specify an invalidation response using one of:
       - `Fallback`, `Escalation`, `Mitigation` (short, actionable)
     - “Invalidated” assumptions trigger an automatic Issue or Scope Change logic (ISSUE + Change Decision).

   * **P-STD-005-CLAUSE-005B (Implementation Guidance Rules)** — Defines IG semantics, constraints, and scope granularity.

     **Normative Standard**:
     - IG MAY use MUST/SHALL when defining implementation and authoring standards intended to be enforceable.
     - IG MUST NOT be used to express software behavior requirements; use `FR`/`NFR`/`CON` for system requirements.

     **Role**:
     - Detailed patterns, pseudo-code, templates, examples, and internal process guidance.
     - Expands on governing RIDs/DRIDs with implementable standards without duplicating upstream requirements text.

     **Scope Granularity**:
     - **Initiative/Epic Scope**: Focus on high-level patterns, templates, and principles.
     - **Feature/Story Scope**: Focus on specific implementation details, code examples, and procedural steps.

   * **P-STD-005-CLAUSE-005C (Integration Guidance Rules)** — Defines INT semantics, non-normative constraints, and governance promotion loop.

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

   * **P-STD-005-CLAUSE-005D (Specification Clause Semantics)** — Defines CLAUSE construction rules and authority semantics.

     **Role**  
     Define the allowed construction, subclause construction, and semantics of `CLAUSE` IDs for STD-internal specification clauses (`STDCID`) and legacy ADR-internal clause aliases (`DRCID`).

     **Construction**
     - Current format (STDCID): `<STD-ID>-CLAUSE-###`. e.g. `P-STD-001-CLAUSE-004`
     - Legacy alias format (DRCID): `<ADR-ID>-CLAUSE-###`. e.g. `T102-ADR-004-CLAUSE-001`
     - `###` is a 3-digit sequence local to the parent artifact (starts at `001`).
     - Optional subclause suffix:
       - Current: `<STD-ID>-CLAUSE-###<CAPITAL_LETTER>` (e.g. `P-STD-001-CLAUSE-004A`)
       - Legacy alias: `<ADR-ID>-CLAUSE-###<CAPITAL_LETTER>` (e.g. `P-STD-001-CLAUSE-004A`)

     **Semantics**
     - `CLAUSE` IDs represent **enforceable Specification clauses** and MUST be written as normative statements (`MUST`/`SHALL`).
     - Non-normative guidance MUST use `IG`/`INT`/`NOTE` (not `CLAUSE`).
     - A `CLAUSE` ID has **no independent precedence** outside its parent authority envelope:
       - `Authority(<STD-ID>-CLAUSE-###) = Authority(<STD-ID>)`
       - During migration alias windows, `Authority(<ADR-ID>-CLAUSE-###) = Authority(<STD-ID>-CLAUSE-###)` when mapped as an alias per `P-STD-005-CLAUSE-003B`.

     > *Informative — Migration Note*: Legacy `DRCID` constructions (`<ADR-ID>-CLAUSE-###`) MAY be treated as aliases during a defined migration window per `P-STD-005-CLAUSE-003B`. New authoring MUST use `STDCID` construction (`<STD-ID>-CLAUSE-###`).

     **Scope & Validity Constraints**
     - `CLAUSE` IDs MUST NOT be created as standalone items outside a parent STD/ADR body.
     - `CLAUSE` IDs MUST NOT be used to represent system requirements or non-normative guidance.
     - References to `CLAUSE` IDs MUST follow `P-STD-005-CLAUSE-004 (Reference Semantics)` and MAY be used for precise cross-document traceability.
     - Rendering of Specification sections (including ordered-list and subclause formatting) MUST follow `P-STD-001-CLAUSE-018 (CLAUSE Construction Requirements)`.

   * **P-STD-005-CLAUSE-005E (Notes Structure Semantics)** — Defines NOTE structure semantics and authoring discipline.
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

   * **P-STD-005-CLAUSE-005F (Standard Decision Record Semantics)** — Defines nested standard decision record construction, semantics, and lifecycle.

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

6) **P-STD-005-CLAUSE-006 (Content Quality)**

   This CLAUSE defines content quality criteria and governance mapping for governed artifact types.

   * **P-STD-005-CLAUSE-006A (Quality Criteria per Category)** — Defines quality expectations by artifact category.
     - **RID**: Lead with a requirement statement when applicable (MUST/SHOULD). No justification prose (put rationale in NOTE). Prefer one primary obligation per RID.
     - **IID-IG**: Informative how-to guidance; may include templates, pseudo-code, and examples; MUST NOT introduce new obligations.
     - **IID-INT**: Non-normative integration notes; MUST NOT introduce new obligations (see `P-STD-005-CLAUSE-005C`).
     - **DRID**: Follow `P-STD-001` body structure strictly.

   * **P-STD-005-CLAUSE-006B (Governance Mapping)** — In governance-focused artifacts, inner clauses SHOULD be named `CLAUSE` (e.g., `P-STD-005-CLAUSE-001`) to prevent confusion with Software Functional Requirements (`FR`). Legacy `...-FR-###` clause IDs inside governance ADRs are treated as clause IDs during migration. Migration status: active — legacy `FR-###` references remain in T102 workspace files; resolved by Governance Sync Changeset.

   * **P-STD-005-CLAUSE-006C (Conciseness Targets)** — RIDs target <200 words when feasible (excluding tables); IF schemas may exceed for clarity.

7) **P-STD-005-CLAUSE-007 (ID Stability & Immutability)**

   This CLAUSE defines anchor stability, ID immutability, and migration tolerance rules.

   * **P-STD-005-CLAUSE-007A (Anchor Stability)** — Anchors MUST remain stable even if Titles change slightly.

   * **P-STD-005-CLAUSE-007B (ID Immutability & No-Reuse)** — Once assigned, an ID is never reused. Deprecate it instead.

   * **P-STD-005-CLAUSE-007C (Migration Tolerance)** — Validators MAY allow legacy governance clause labels (e.g., `...-FR-###` inside governance ADRs) during migration, but new governance clauses MUST use `CLAUSE`.

     > *Informative*: The `RULE-###` intermediate format has been fully migrated to `CLAUSE`. Only `FR-###` → `CLAUSE` migration remains active in T102 legacy workspace files.

   * **P-STD-005-CLAUSE-007D (Legacy Standards Migration)** — Migration tolerance for legacy governance standard identifiers is defined in `P-STD-001-CLAUSE-017 (Migration Tolerance)`.

### P-STD-005B — Timeline UID Convention

8) **P-STD-005-CLAUSE-008 (Timeline UID Schema)**

   Timeline UIDs MUST be stable, immutable identifiers for execution management entities (Phase, Stream, Activity, Task) and for the governance qualifiers (Session, Gate) associated with those entities.
   3-digit sequences (`###`) in timeline tokens represent the range `001`–`999`. Exceeding this ceiling requires introducing a new scope segment; digit width MUST NOT be expanded.

   * **P-STD-005-CLAUSE-008A (Root token)** — A timeline UID root MUST be either `P` (Program) or an initiative root `T###` optionally with an epic suffix (e.g., `T102A`, `T102A1`). Regex: `^(?:P|T\\d{3}(?:[A-Z]\\d*)?)$`.

   * **P-STD-005-CLAUSE-008B (Phase UID)** — Phase UIDs MUST have the form `<ROOT>-PH###`. Regex: `^(?:P|T\\d{3}(?:[A-Z]\\d*)?)-PH\\d{3}$`. Examples: `P-PH000`, `T104-PH001`.

   * **P-STD-005-CLAUSE-008C (Stream UID)** — Stream UIDs MUST have the form `<ROOT>-PH###-ST###`. Regex: `^(?:P|T\\d{3}(?:[A-Z]\\d*)?)-PH\\d{3}-ST\\d{3}$`. Examples: `P-PH000-ST001`, `T104-PH001-ST002`.

   * **P-STD-005-CLAUSE-008D (Activity UID)** — Activity UIDs MUST have the form `<ROOT>-PH###-ST###-AC###`. Regex: `^(?:P|T\\d{3}(?:[A-Z]\\d*)?)-PH\\d{3}-ST\\d{3}-AC\\d{3}$`. Examples: `P-PH000-ST001-AC006`, `T104-PH001-ST002-AC000`.

   * **P-STD-005-CLAUSE-008E (Sub-Activity UID)** — Sub-activities MUST be expressed as a dotted suffix on the Activity token: `AC###.<n>`, where `<n>` is a positive integer. Regex: `^AC\\d{3}\\.\\d+$`. Example: `T102-PH001-ST001-AC009.1`.

   * **P-STD-005-CLAUSE-008F (Task UID)** — Task UIDs MUST have the form `<Activity-UID>-TK###` (where Activity-UID MAY include a dotted Sub-Activity). Regex: `^(?:P|T\\d{3}(?:[A-Z]\\d*)?)-PH\\d{3}-ST\\d{3}-AC\\d{3}(?:\\.\\d+)?-TK\\d{3}$`. Example: `T102-PH001-ST001-AC009.1-TK003`.

   * **P-STD-005-CLAUSE-008G (Session UID)** — Session UIDs MUST be expressed by appending `-SES###` to an Activity UID or Task UID. Regex (Activity session): `^(?:P|T\\d{3}(?:[A-Z]\\d*)?)-PH\\d{3}-ST\\d{3}-AC\\d{3}(?:\\.\\d+)?-SES\\d{3}$`. Regex (Task session): `^(?:P|T\\d{3}(?:[A-Z]\\d*)?)-PH\\d{3}-ST\\d{3}-AC\\d{3}(?:\\.\\d+)?-TK\\d{3}-SES\\d{3}$`. Example: `P-PH000-ST001-AC006-SES003`.

   * **P-STD-005-CLAUSE-008H (Gate UID)** — Gate UIDs MUST be expressed by appending `-GATE-###` to an Activity UID. Regex: `^(?:P|T\\d{3}(?:[A-Z]\\d*)?)-PH\\d{3}-ST\\d{3}-AC\\d{3}(?:\\.\\d+)?-GATE-\\d{3}$`. Example: `P-PH000-ST001-AC006-GATE-002`.

   * **P-STD-005-CLAUSE-008I (Composition rules)** — Timeline UID tokens MUST appear in this order: `PH` then `ST` then `AC` (optionally dotted), then optional `TK`, then optional qualifier (`SES` or `GATE`). Session UIDs (`SES`) MAY be further extended with a session item type token (see CLAUSE-008J). Qualifiers and their extensions MUST NOT appear in the middle of the UID.

   * **P-STD-005-CLAUSE-008J (Session Item UID)** — Session item UIDs MUST be expressed by appending `-<TYPE>###` to a Session UID, where `<TYPE>` is one of: `DP` (Discussion Point), `DEC` (Decision), `ACT` (Action), `OQ` (Open Question). Sequences (`###`) reset per session file per `guideline_workspace_notes.md` §2.2. Regex: `^(?:P|T\\d{3}(?:[A-Z]\\d*)?)-PH\\d{3}(?:-ST\\d{3}(?:-AC\\d{3}(?:\\.\\d+)?(?:-TK\\d{3})?)?)?-SES\\d{3}-(?:DP|DEC|ACT|OQ)\\d{3}$`. Examples: `P-PH000-ST001-AC006-SES003-DP001`, `T104-PH001-ST002-SES001-DEC001`, `P-PH000-ST001-AC006-SES003-ACT001`.

9) **P-STD-005-CLAUSE-009 (UID-vs-Seq Decoupling)**

   Timeline UIDs MUST be immutable and MUST NOT be renumbered or changed to accommodate insertion, reprioritization, or re-sequencing.

   * **P-STD-005-CLAUSE-009A (Immutability)** — Once assigned, a timeline UID MUST NOT change for the life of the referenced entity.
   * **P-STD-005-CLAUSE-009B (Seq is display-only)** — Display sequence numbers (e.g., ordering in a table) MUST be treated as presentation-only and MUST NOT be used as stable identifiers.
   * **P-STD-005-CLAUSE-009C (Insertion rule)** — New work inserted between existing work MUST receive a new UID; existing UIDs MUST remain unchanged.
   * **P-STD-005-CLAUSE-009D (Cross-reference stability)** — Artifacts that reference a timeline UID MUST NOT require updates solely due to reordering.

10) **P-STD-005-CLAUSE-010 (LINK Indirection System)**

   Registers MAY use `LINK-###` indirection to reference deliverables (especially long paths) without repeating full paths throughout the register body.

   * **P-STD-005-CLAUSE-010A (LINK construction)** — LINK IDs MUST use the form `LINK-###`. Regex: `^LINK-\\d{3}$`. Example: `LINK-004`.
   * **P-STD-005-CLAUSE-010B (Pointer-only semantics)** — LINK IDs are pointers-only and non-normative. They MUST NOT be used as a substitute for authoritative standards, indices, or enforceable obligations.
   * **P-STD-005-CLAUSE-010C (Mapping requirement)** — Each LINK referenced in a register MUST be defined in an associated Links section/table that maps `LINK-###` to a canonical repo-relative path.
   * **P-STD-005-CLAUSE-010D (Stability)** — LINK IDs SHOULD be stable within the register scope; when a path changes, the mapping SHOULD be updated without changing the LINK ID.

11) **P-STD-005-CLAUSE-011 (Timeline File Naming)**

   File naming SHOULD be derived from timeline UIDs to preserve determinism and traceability between plans, notes, raw transcripts, and gate evidence.

   * **P-STD-005-CLAUSE-011A (Plan files)** — Plan files MUST use: `plan_<Timeline-UID>.md` where `<Timeline-UID>` is `(<ROOT>-PH###[-ST###[-AC###]])`. Examples: `plan_P-PH000.md`, `plan_P-PH000-ST001.md`, `plan_P-PH000-ST001-AC006.md`.
   * **P-STD-005-CLAUSE-011B (Notes registers)** — Notes register/index files MUST use: `notes_<Timeline-UID>.md` (no `SES###` token). Example: `notes_T104-PH001-ST000.md`.
   * **P-STD-005-CLAUSE-011C (Session notes)** — Session notes files MUST use: `snotes_<Timeline-UID>-SES###.md` where the stem includes the Activity UID (and optional Task UID) followed by the session token. Example: `snotes_P-PH000-ST001-AC006-SES003.md`.
   * **P-STD-005-CLAUSE-011D (Raw transcripts)** — Raw transcripts MUST use: `raw_<Timeline-UID>-SES###.<ext>` where `<ext>` is `txt` or `md`. Example: `raw_P-PH000-ST001-AC006-SES001.txt`.
   * **P-STD-005-CLAUSE-011E (Verification evidence)** — Gate evidence files MUST use: `verification_<Activity-UID>_gate-###.md` where `gate-###` corresponds to the gate number for the activity. Example: `verification_P-PH000-ST001-AC006_gate-001.md`.

## Decision Record

### ADR Index
| ADR ID | Title | Status | Supersedes | Date |
|:--|:--|:--|:--|:--|
| P-STD-005-ADR-002 | Promotion from T102-STD-005 | `accepted` | ADR-001 | 2026-02-23 |
| P-STD-005-ADR-001 | ID Specification & Rules | `superseded` | — | 2026-02-23 |

* **P-STD-005-ADR-002 (Promotion from T102-STD-005)** {#p-std-005-adr-002-promotion-from-t102-std-005}

  * **Context**
    `T102-STD-005` was authored at Initiative scope but defines ID and governance rules used across Program-level and multi-initiative artifacts. As Program scope standards and cross-initiative workflow artifacts expand, retaining the authoritative ID specification at Initiative scope creates a scope-identity mismatch (e.g., Program artifacts using Program timeline UIDs that are not covered by the canonical schema), and increases the risk of inconsistent ID rules across initiatives.

    Timeline UID conventions (Phase/Stream/Activity/Task, plus Gate/Session qualifiers) were planned as an initiative-scoped standard (`T104-STD-002`) but are inherently cross-initiative and must be unified with the canonical ID schema to maintain mechanical lintability.

  * **Decision**
    Promote `T102-STD-005 (ID Specification & Rules)` to `P-STD-005 (Universal ID Specification)` via full content transfer with 1:1 CLAUSE re-identification per the approved promotion contract. Mark `T102-STD-005` as `superseded` and establish an alias window for `T102-STD-005-CLAUSE-*` references per the contract terms.

    Absorb the timeline UID scope by adding `P-STD-005-CLAUSE-008` through `P-STD-005-CLAUSE-011` and by amending `P-STD-005-CLAUSE-001` to incorporate timeline UID regex patterns (no exception-only treatment).

  * **Alternatives**
    * *Adopt-by-reference*: Keep `T102-STD-005` as authoritative and reference it from Program artifacts. Rejected: preserves scope-identity mismatch and fails to resolve canonical schema conflicts for Program timeline UIDs.
    * *Timeline-only standard*: Promote only timeline UID rules and keep the rest in `T102-STD-005`. Rejected: timeline UIDs and canonical schema must be unified to keep ID validation mechanical and consistent.
    * *Status quo*: No promotion. Rejected: ongoing drift risk and ambiguous authority boundary for cross-initiative governance.

  * **Consequences**
    (+) `P-STD-005` becomes the authoritative Program-level surface for ID rules and timeline UID conventions.
    (+) Program artifacts can reference a Program standard for both canonical ID schema and timeline UIDs, reducing ambiguity and drift.
    (±) Existing `T102-STD-005-CLAUSE-*` references migrate at next touch during the alias window; a governance sync changeset will remove alias support.
    (-) One-time promotion effort: transfer content, insert new CLAUSEs, update Tier 1 references, and mark the source as superseded.

  * **Traceability**
    * `P-PH000-ST001-AC006` (Promotion activity)
    * `P-PH000-ST001-AC006-GATE-001` (Source clean-for-promotion approval)
    * `P-PH000-ST001-AC006-SES002` (Substandard architecture + RES scope absorption decisions)
    * `P-PH000-ST001-AC006-SES003` (Canonical schema amendment mandate; expanded timeline UID scope; changeset-based alias end; Tier 1 lock)
    * `T104-PH001-ST000-SES001` (Stable UIDs; initiative phases; LINK indirection inputs)
    * `T104-PH001-ST002-AC002` (Timeline UID convention scope absorbed)
    * `T102-STD-005-CLAUSE-003A` (Promotion contract rules)
    * `T102-STD-005-CLAUSE-003B` (Alias window rules)

* **P-STD-005-ADR-001 (ID Specification & Rules)** {#p-std-005-adr-001-id-specification-and-rules}

  * **Context**
    Per `P-STD-005 (Universal ID Specification)`, multiple artifact families use overlapping ID conventions (considerations, requirements, decisions) at different scopes. Without a single normative specification, authors improvise category tokens, anchors, and references, creating inconsistency and undermining inheritance, precedence, and verification.

  * **Decision**
    Standardize ID patterns across Initiative, Epic, Feature, and Story scopes; define category tokens, sub-ID patterns, anchors, and referencing rules. This ADR is the single specification adopted by `P-STD-005` as its normative specification.

  * **Alternatives**
    - Free-form, template-local ID schemes — rejected.
    - Enforcing full titles in all inline mentions — rejected.

  * **Consequences**
    (+) Predictable, machine-checkable IDs across artifacts.
    (+) Faster audits and safer cross-linking with stable anchors.
    (±) Requires discipline and small refactors for legacy items.

  * **Traceability**
    - `T102-STD-005` (Source standard origin)
    - `P-PH000-ST001-AC006` (Promotion activity)

## References

### External References (Cross-Scope)
| ID | Title | Scope | Source Path |
|:--|:--|:--|:--|
| P-STD-001 | Program Governance Standard | Program (P) | `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md` |
| T102-STD-003 | Explicit Inheritance Model | Initiative (T102) | `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-003_explicit-inheritance-model.md` |
| T102-STD-005 | ID Specification & Rules (Superseded Source) | Initiative (T102) | `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-005_id-specification-rules.md` |
| T102-STD-006 | Research Artifacts Index | Initiative (T102) | `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-006_research-artifacts-index.md` |
| T102-CON-009 | Normative Keywords | Initiative (T102) | `prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md` |

## Provenance
### Promotion
- Promoted from: `T102-STD-005 (ID Specification & Rules)`
- Promotion activity: `P-PH000-ST001-AC006 (Promote T102-STD-005 to P-STD-005)`
- Promotion contract: `proposal_P-PH000-ST001-AC006_promotion-contract-t102-std-005-to-p-std-005.md`
- Alias window: active until Governance Sync Changeset "P-STD-005 Alias Removal" is executed (changeset-based end condition)

### Input Sources
- `T104-PH001-ST000-SES001 (Planning & Consultation QA Session)` — Inputs: Stable UIDs, Phases, LINK indirection
- `T104-PH001-ST002 (Standards Stream Plan)` — Input: Timeline UID scope
- `T104-PH001-ST002-AC000 (Directory & File Naming Convention Proposal)` — Approved naming convention

### Hardening
- Activity: `P-PH000-ST001-AC007 (Harden P-STD-005)`
- Changes: 6 SUBCLAUSE-SPLIT refactorings (R-001 through R-006), 15 LANGUAGE-EDIT fixes (R-007 through R-021), 14 GIR remediations. Zero RE-ARCHITECTURE changes; all 11 main CLAUSE IDs preserved.
- Analysis: `prompt/artifacts/tasks/P/workspace/PH000/ST001/analysis/analysis_P-PH000-ST001-AC007_p-std-005-hardening-assessment.md`
- GATE-001 verification: `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC007/verification/verification_P-PH000-ST001-AC007_gate-001.md`
