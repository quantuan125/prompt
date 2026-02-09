# Migration Report

- Mode: apply
- Root: `/mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt`
- Files changed: 1
- Files skipped (include filter): 820
- Files skipped (exclude rules): 0
- Files skipped (encoding): 0
- Safety cap (`max-files-changed`): 5
- Include paths:
  - `/mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt/artifacts/tasks/T102/consultant/standards/T102-STD-005_id-specification-rules.md`
- Exclude globs:
  - `**/scripts/output/**`
  - `**/workspace/scripts/report_*.md`

## Change Summary

- `/mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt/artifacts/tasks/T102/consultant/standards/T102-STD-005_id-specification-rules.md`
  - rename: `/mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt/artifacts/tasks/T102/consultant/standards/T102-STD-005_id-specification-rules.md` -> `/mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt/artifacts/tasks/T102/consultant/standards/T102-STD-005_id-specification-rules.md`
  - clause_rewrites: 26
  - dr_anchor_regenerations: 1
  - dr_body_id_rewrites: 1
  - heading_rewrites: 1
  - legacy_slug_rewrites: 1

## Unified Diffs

### `/mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt/artifacts/tasks/T102/consultant/standards/T102-STD-005_id-specification-rules.md`

```diff
--- /mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt/artifacts/tasks/T102/consultant/standards/T102-STD-005_id-specification-rules.md
+++ /mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt/artifacts/tasks/T102/consultant/standards/T102-STD-005_id-specification-rules.md
@@ -1,8 +1,8 @@
-# T102-STD-005 — ID Specification & Rules
+# T102-STD-005 — ID Specification & Rules
 
 ## Decision
 
-* **T102-STD-005 (ID Specification & Rules)** {#t102-std-005-id-spec}
+* **T102-STD-005-ADR-001 (ID Specification & Rules)** {#t102-std-005-adr-001-id-specification-and-rules}
 
   * **Context**
     Per `T102-STD-005 (ID Governance Standard)`, multiple artifact families use overlapping ID conventions (considerations, requirements, decisions) at different scopes. Without a single normative specification, authors improvise category tokens, anchors, and references, creating inconsistency and undermining inheritance, precedence, and verification.
@@ -32,7 +32,7 @@
 
 ## Specification
 
-1) **T102-STD-005-CLAUSE-001 (Canonical ID Schema)**
+1) **T102-STD-005-CLAUSE-001 (Canonical ID Schema)**
 
    **Regex Patterns**: usage of all IDs SHALL match one of these patterns:
 
@@ -51,7 +51,7 @@
      - Hyphenated compounds count as 1 word.
    - Description: concise statement of the rule/requirement/decision/guidance.
 
-2) **T102-STD-005-CLAUSE-002 (Taxonomy & Terminology)**
+2) **T102-STD-005-CLAUSE-002 (Taxonomy & Terminology)**
 
    **Category Key**:
    - `SID` (Scope)
@@ -72,8 +72,8 @@
 
    **Program Scope (`P`)**
    - `P` denotes cross-initiative governance scope (program-level SSOT). `P-*` IDs MAY govern multiple initiatives.
-   - Program IDs MUST use the `P-<TOKEN>-###` format per `T102-STD-005-CLAUSE-001`.
-   - Any ID MAY be **re-scoped** (promoted or demoted) across `P/I/E/F/S` when its applicability changes, subject to `T102-STD-005-CLAUSE-003 (Precedence & Hierarchy)` and the re-scope contract in `T102-STD-005-CLAUSE-003A`.
+   - Program IDs MUST use the `P-<TOKEN>-###` format per `T102-STD-005-CLAUSE-001`.
+   - Any ID MAY be **re-scoped** (promoted or demoted) across `P/I/E/F/S` when its applicability changes, subject to `T102-STD-005-CLAUSE-003 (Precedence & Hierarchy)` and the re-scope contract in `T102-STD-005-CLAUSE-003A`.
 
    Valid tokens are strictly defined by this table. Authors MUST select the most specific token available for the scope.
 
@@ -90,19 +90,19 @@
    | `RID` | `NFR` | **Non-Functional Requirement** | F, S | Quality requirement expressed as testable metrics. |
    | `RID` | `STD` | **Standard** | P, I, E, F | Normative standards registry token. Enforceable obligations MUST be encoded in `STD` or in its adopted normative specification; governance rationale belongs in ADRs. |
    | `STDCID` | `CLAUSE` | **Standard Clause** | P, I, E, F | STD-internal clause ID used only within the parent STD combined file. Construction is `<STD-ID>-CLAUSE-###`; scope and authority derive from the parent STD. |
-   | `DRID` | `ADR` | **Architectural Decision** | P, I, E, F, S | Technical implementation decision record. Construction MAY be standalone (`<SID>-ADR-###`) or STD-nested (`<STD-ID>-ADR-###`) per `T102-STD-005-CLAUSE-005F`. |
-   | `DRCID` | `CLAUSE` | **Decision Record Clause** `[LEGACY — migration to STDCID in progress]` | P, I, E, F, S | Legacy ADR-internal clause ID used within the parent ADR (`<ADR-ID>-CLAUSE-###`) during migration alias windows per `T102-STD-005-CLAUSE-003B`. |
+   | `DRID` | `ADR` | **Architectural Decision** | P, I, E, F, S | Technical implementation decision record. Construction MAY be standalone (`<SID>-ADR-###`) or STD-nested (`<STD-ID>-ADR-###`) per `T102-STD-005-CLAUSE-005F`. |
+   | `DRCID` | `CLAUSE` | **Decision Record Clause** `[LEGACY — migration to STDCID in progress]` | P, I, E, F, S | Legacy ADR-internal clause ID used within the parent ADR (`<ADR-ID>-CLAUSE-###`) during migration alias windows per `T102-STD-005-CLAUSE-003B`. |
    | `IID` | `IG` | **Implementation Guidance** | I, E, F | Informative how-to guidance: patterns, templates, and examples. MUST NOT introduce new obligations. Not a substitute for system requirements. |
    | `IID` | `INT` | **Integration Guidance** | I, E, F, S | Non-normative integration and cross-scope coordination guidance for external audiences; MUST NOT introduce new obligations. |
    | `OID` | `NOTE` | **Note** | I, E, F, S | Non-normative context; do not use for obligations. |
    | `OID` | `ISSUE` | **Issue** | I, E, F | Known gap requiring resolution. |
    | `OID` | `RISK` | **Risk** | I, E, F | Potential negative event requiring mitigation. |
 
-3) **T102-STD-005-CLAUSE-003 (Precedence & Hierarchy)**
+3) **T102-STD-005-CLAUSE-003 (Precedence & Hierarchy)**
 
    **Directionality**: Inheritance flows downstream with scopes only.
    - Correct: Story references Feature; Feature references Epic; Epic references Initiative; Initiative references Program.
-   - Incorrect: Higher scope references lower scope (except `INT` exception defined in `T102-STD-005-CLAUSE-005C`).
+   - Incorrect: Higher scope references lower scope (except `INT` exception defined in `T102-STD-005-CLAUSE-005C`).
 
    **Precedence Order** (Highest to Lowest):
    - Program > Initiative > Epic > Feature > Story
@@ -116,7 +116,7 @@
    **Variances**:
    Any downstream ID deviating from an upstream rule MUST cite the overridden ID explicitly in a “Variance ADR”.
 
-   * **T102-STD-005-CLAUSE-003A (Cross-Scope Re-scope / Promotion Contract)**
+   * **T102-STD-005-CLAUSE-003A (Cross-Scope Re-scope / Promotion Contract)**
      This contract applies to ALL `RID` token types (e.g., `QG/CON/DEP/IF/STD/...`) and covers promotion/demotion across `P/I/E/F/S`.
      1. **When to Promote (Up-scope)**:
        - Promote when the obligation/constraint/goal is stable AND applies to multiple downstream scopes (e.g., `E-QG` becomes `I-QG`; `I-CON` becomes `P-CON`).
@@ -131,11 +131,11 @@
        - If one ID becomes multiple IDs (split), the old ID MUST supersede to a set of new IDs and document the split rationale in an ADR.
        - If multiple IDs become one ID (merge), the new ID MUST list all superseded IDs.
 
-   * **T102-STD-005-CLAUSE-003B (Alias Window for Re-scope Transitions)**
+   * **T102-STD-005-CLAUSE-003B (Alias Window for Re-scope Transitions)**
      - During a defined migration window, superseded IDs MAY be treated as aliases of their replacement IDs for lint/enforcement.
      - Alias support MUST be removed after the migration completion milestone/date.
 
-4) **T102-STD-005-CLAUSE-004 (Reference Semantics)**
+4) **T102-STD-005-CLAUSE-004 (Reference Semantics)**
 
    **Styles**:
    - **Short-hand (Inline):** `` `ID` `` (e.g., `T102-QG-001`, `T102B`)
@@ -160,11 +160,11 @@
    **Constraint**:
    Normative bodies MUST NOT reference `ISSUE` or `RISK` IDs inline. Issues/Risks capture the problem; RIDs/DRIDs capture the solution.
 
-5) **T102-STD-005-CLAUSE-005 (Category Semantics)**
+5) **T102-STD-005-CLAUSE-005 (Category Semantics)**
 
    This clause provides a concise semantic overview. Tokens with lifecycle/exception behavior have dedicated subclauses. 
 
-   * **T102-STD-005-CLAUSE-005A (Assumption Lifecycle)**
+   * **T102-STD-005-CLAUSE-005A (Assumption Lifecycle)**
 
      **Table Requirement**:
      Assumptions MUST be defined in a table structure preceding the list of ID bodies.
@@ -181,7 +181,7 @@
        - `Fallback`, `Escalation`, `Mitigation` (short, actionable)
      - “Invalidated” assumptions trigger an automatic Issue or Scope Change logic (ISSUE + Change Decision).
 
-   * **T102-STD-005-CLAUSE-005B (Implementation Guidance Rules)**
+   * **T102-STD-005-CLAUSE-005B (Implementation Guidance Rules)**
 
      **Normative Standard**:
      - IG MAY use MUST/SHALL when defining implementation and authoring standards intended to be enforceable.
@@ -195,7 +195,7 @@
      - **Initiative/Epic Scope**: Focus on high-level patterns, templates, and principles.
      - **Feature/Story Scope**: Focus on specific implementation details, code examples, and procedural steps.
 
-   * **T102-STD-005-CLAUSE-005C (Integration Guidance Rules)**
+   * **T102-STD-005-CLAUSE-005C (Integration Guidance Rules)**
 
      **Role**:
      - External-facing integration guidance and cross-scope coordination guidance.
@@ -212,7 +212,7 @@
      **Governance Loop**:
      If an INT pattern is widely adopted or becomes policy, it SHOULD be promoted into Epic-level `RID` (e.g., `IF/CON`) and/or captured as an `ADR`, and the originating INT SHOULD be updated to reference the promoted governance.
 
-   * **T102-STD-005-CLAUSE-005D (Specification Clause Semantics)**
+   * **T102-STD-005-CLAUSE-005D (Specification Clause Semantics)**
 
      **Role**  
      Define the allowed construction, subclause construction, and semantics of `CLAUSE` IDs for STD-internal specification clauses (`STDCID`) and legacy ADR-internal clause aliases (`DRCID`).
@@ -230,19 +230,19 @@
      - Non-normative guidance MUST use `IG`/`INT`/`NOTE` (not `CLAUSE`).
      - A `CLAUSE` ID has **no independent precedence** outside its parent authority envelope:
        - `Authority(<STD-ID>-CLAUSE-###) = Authority(<STD-ID>)`
-       - During migration alias windows, `Authority(<ADR-ID>-CLAUSE-###) = Authority(<STD-ID>-CLAUSE-###)` when mapped as an alias per `T102-STD-005-CLAUSE-003B`.
+       - During migration alias windows, `Authority(<ADR-ID>-CLAUSE-###) = Authority(<STD-ID>-CLAUSE-###)` when mapped as an alias per `T102-STD-005-CLAUSE-003B`.
 
      **Migration Note**
-     - Legacy `DRCID` constructions (`<ADR-ID>-CLAUSE-###`) MAY be treated as aliases during a defined migration window per `T102-STD-005-CLAUSE-003B`.
+     - Legacy `DRCID` constructions (`<ADR-ID>-CLAUSE-###`) MAY be treated as aliases during a defined migration window per `T102-STD-005-CLAUSE-003B`.
      - New authoring MUST use `STDCID` construction (`<STD-ID>-CLAUSE-###`).
 
      **Scope & Validity Constraints**
      - `CLAUSE` IDs MUST NOT be created as standalone items outside a parent STD/ADR body.
      - `CLAUSE` IDs MUST NOT be used to represent system requirements or non-normative guidance.
-     - References to `CLAUSE` IDs MUST follow `T102-STD-005-CLAUSE-004 (Reference Semantics)` and MAY be used for precise cross-document traceability.
+     - References to `CLAUSE` IDs MUST follow `T102-STD-005-CLAUSE-004 (Reference Semantics)` and MAY be used for precise cross-document traceability.
      - Rendering of Specification sections (including ordered-list and subclause formatting) MUST follow `T102-STD-004-CLAUSE-005 (Specification Clauses)`.
 
-   * **T102-STD-005-CLAUSE-005E (Notes Structure Semantics)**
+   * **T102-STD-005-CLAUSE-005E (Notes Structure Semantics)**
      **Notes Structure Schema**
      - Location: SPS "Research & Notes" → "Notes" subheading.
      - Structure: List item per NOTE beginning with `**<SID>-NOTE-### (<Title>)** — <body>` on a single line.
@@ -256,7 +256,7 @@
      - When NOT to use a NOTE: to summarize commissioned research (use RES with Brief/Report), to encode enforceable rules (use STD/ADR), or to duplicate upstream content (link via back‑ticked IDs instead).
      - Discipline: Keep short (≤200 words), scannable, and link‑don’t‑duplicate. If NOTE content becomes critical or frequently referenced, promote to `RES` (with brief/report) or to `STD/ADR` as appropriate. Maintain sequential NOTE numbering without retroactively altering meaning.
 
-   * **T102-STD-005-CLAUSE-005F (Standard Decision Record Semantics)**
+   * **T102-STD-005-CLAUSE-005F (Standard Decision Record Semantics)**
 
      **Construction**
      - Format: `<STD-ID>-ADR-###`. e.g. `T102-STD-004-ADR-001`
@@ -275,21 +275,21 @@
      **Constraint**
      - Each STD combined file MUST have only one current nested ADR at a time.
 
-6) **T102-STD-005-CLAUSE-006 (Content Quality)**
+6) **T102-STD-005-CLAUSE-006 (Content Quality)**
 
    **Quality Criteria**:
    - **RID**: Lead with a requirement statement when applicable (SHALL/SHOULD). No justification prose (put rationale in NOTE). Prefer one primary obligation per RID.
    - **IID-IG**: Informative how-to guidance; may include templates, pseudo-code, and examples; MUST NOT introduce new obligations.
-   - **IID-INT**: Non-normative integration notes; MUST NOT introduce new obligations (see `T102-STD-005-CLAUSE-005C`).
+   - **IID-INT**: Non-normative integration notes; MUST NOT introduce new obligations (see `T102-STD-005-CLAUSE-005C`).
    - **DRID**: Follow `T102-STD-004` body structure strictly.
 
    **Governance Mapping**:
-   In governance-focused artifacts, inner clauses SHOULD be named `CLAUSE` (e.g., `T102-STD-005-CLAUSE-001`) to prevent confusion with Software Functional Requirements (`FR`). Legacy `...-FR-###` clause IDs inside governance ADRs are treated as clause IDs during migration.
+   In governance-focused artifacts, inner clauses SHOULD be named `CLAUSE` (e.g., `T102-STD-005-CLAUSE-001`) to prevent confusion with Software Functional Requirements (`FR`). Legacy `...-FR-###` clause IDs inside governance ADRs are treated as clause IDs during migration.
 
    **Conciseness**:
    RIDs target <200 words when feasible (excluding tables); IF schemas may exceed for clarity.
 
-7) **T102-STD-005-CLAUSE-007 (ID Stability & Immutability)**
+7) **T102-STD-005-CLAUSE-007 (ID Stability & Immutability)**
 
    - **Anchor Stability**: Anchors MUST remain stable even if Titles change slightly.
    - **Immutable IDs**: Once assigned, an ID is never reused. Deprecate it instead.
```
