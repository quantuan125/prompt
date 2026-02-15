---
artifact_type: 'PROPOSAL'
initiative_id: 'T102'
initiative_code: 'CWD'
activity_id: 'T102-PH001-ST001-AC008'
task_id: 'T102-PH001-ST001-AC008-TK005'
version: '0.2.0'
date: '2026-02-14'
status: 'superseded'
superseded_by: 'prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_PH001-ST001-AC009_std-004-redesign.md'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T102/consultant/workspace/plan/plan_T102-PH001-ST001.md'
analysis_reference: 'prompt/artifacts/tasks/T102/consultant/workspace/analysis/analysis_T102-CWD_PH001-ST001-AC008_std-004-self-compliance-audit.md'
session_reference: 'prompt/artifacts/tasks/T102/consultant/workspace/notes/PH001/ST001/notes_T102-PH001-ST001-AC009-SES001.md'
res007_analysis_reference: 'prompt/artifacts/tasks/T102/consultant/workspace/analysis/analysis_T102-RES-007_standards-authoring-methodology-benchmarking.md'
target_files:
  - 'prompt/artifacts/tasks/T102/consultant/standards/T102-STD-004_specification-standard-and-guideline.md'
  - 'prompt/templates/consultant/standards/guideline_standard_specs.md'
  - 'prompt/templates/consultant/standards/template_standard_specs.md'
  - 'prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md'
---

> **SUPERSEDED**: This proposal has been superseded by `proposal_T102-CWD_PH001-ST001-AC009_std-004-redesign.md` (2026-02-15). The superseding proposal incorporates all R2 content plus STD-009 merge, substandard architecture, and full CLAUSE resequencing per AC009-GATE-001 QA review. See `notes_T102-PH001-ST001-AC009-SES002.md` for decisions.

# PROPOSAL: T102 (CWD) — PH001 / ST001 / AC008 — R2 Refactor Plan (STD-004 Exemplar Hardening)

## I. Executive Summary

- R2 approved (T102-PH001-ST001-AC008-SES001-DEC001): full subclause refactor for exemplar self-conformance
- Option B approved (T102-PH001-ST001-AC008-SES001-DEC002): STD-004 = combined file authoring standard
- RES-007 accepted for integration (ST004-AC004-GATE-003 passed 2026-02-14): apply R2-Enhanced enhancements (boundary hygiene, clause granularity discipline, vocabulary guidance)
- Scope: 4 target files (STD-004 + guideline + template + SPS MVC)
- Constraint: all 4 files updated in same changeset per CLAUSE-017

## II. R2 Design Principles

- Existing top-level CLAUSE IDs (001–017) remain stable; CLAUSE-018 is additive (no renumbering)
- Each CLAUSE gets one normative anchor statement (BCP 14 keywords preferred; see CLAUSE-016D)
- Additional requirements → explicitly labeled subclauses (CLAUSE-###A, B, C...)
- Procedural workflows rewritten as normative requirements
- ADR-era language (CLAUSE-001–004) refocused for combined file context
- SPS/Concept section-title prescriptions removed from CLAUSE-002 (→ STD-009 domain)

## III. Per-CLAUSE Specification

This section provides (a) the current clause text, (b) audit-identified issues, and (c) copy/paste-ready replacement text for the R2 refactor. Replace each clause block in the target STD with the corresponding proposed replacement text.

### CLAUSE-001 — DR Index Schemas

#### Current text (as-is)
```markdown

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
```

#### Issues identified
- Minor gap: Effective nullability not specified; designated standards directory not explicitly defined, creating derivative traceability risk.

#### Proposed replacement text (copy/paste-ready)
```markdown
1) **T102-STD-004-CLAUSE-001 (Combined File Index Schemas)**

   T102-STD-004-CLAUSE-001: Index tables that register combined standard-specification files MUST conform to subclauses `T102-STD-004-CLAUSE-001A` through `T102-STD-004-CLAUSE-001E`.

   - `T102-STD-004-CLAUSE-001A (Effective nullability)`
     - `Effective` MUST be an ISO-8601 date `YYYY-MM-DD` or `—` if not yet set.

   - `T102-STD-004-CLAUSE-001B (Designated standards directory definition — T102 Consultant)`
     - For the T102 consultant scope, the designated standards directory is `prompt/artifacts/tasks/T102/consultant/standards/`.

   - `T102-STD-004-CLAUSE-001C (ADR Index Schema)`
     - `ADR ID | Title | Authority STD | Status | Owner | Effective | Supersedes | Canonical Path`

   - `T102-STD-004-CLAUSE-001D (Column Definitions)`
     1. `ID`: ID construction MUST follow `T102-STD-005` following general format: `<SID>-ADR-###`.
     2. `Title`: Title Case, 2–3 words.
     3. `Status`: `{Proposed, Accepted, Deprecated}`.
     4. `Owner`: governance authority (typically `Client`) or implementation owner; if unknown use `—`.
     5. `Effective`: ISO-8601 date `YYYY-MM-DD` or `—` if not yet set. (See `T102-STD-004-CLAUSE-001A`.)
     6. `Supersedes`: list of superseded IDs or `—`.
     7. `Canonical Path`: full repo-relative path to the combined standard-specification file; MUST resolve to an existing file under the designated standards directory per `T102-STD-004-CLAUSE-001B`.
     8. `Authority STD`: the governing `STD` that applies to the ADR (or that contains the ADR as a nested decision record). Use `—` if none.

   - `T102-STD-004-CLAUSE-001E (Phase 1 index granularity)`
     - Phase 1 index granularity is the combined file as a whole (no anchor addressing required in indexes).
```

#### Subclauses introduced
- `T102-STD-004-CLAUSE-001A`
- `T102-STD-004-CLAUSE-001B`
- `T102-STD-004-CLAUSE-001C`
- `T102-STD-004-CLAUSE-001D`
- `T102-STD-004-CLAUSE-001E`

#### Rationale
- Aligns STD-004 with R2 (T102-PH001-ST001-AC008-SES001-DEC001) and Option B boundary (T102-PH001-ST001-AC008-SES001-DEC002) where applicable.
- Closes the CLAUSE-017 derivative traceability gap by ensuring directory/naming and structure rules are governed in STD-004.

### CLAUSE-002 — Placement Standards

#### Current text (as-is)
```markdown

2) **T102-STD-004-CLAUSE-002 (Placement Standards)**
   - **SPS artifacts**: section titled `"<SCOPE> Governance Decisions"` containing governance decisions only.
   - **Concept artifacts**: section titled `"<SCOPE> Architectural Decisions"` with mirror subsections for Epic/Feature areas as needed.
   - **Combined files**: full normative specifications and nested decision records live in combined standard-specification files under the scope's designated standards directory; SPS/Concept are index-only hubs referencing combined files via Canonical Path.
   - **Consistency requirement**: placement MUST follow established artifact section numbering without local deviations.
```

#### Issues identified
- Minor gap: Prescribes SPS/Concept section titles inconsistent with current surfaces; canonical directory not explicitly governed in STD-004; boundary should be STD-009 domain.

#### Proposed replacement text (copy/paste-ready)
```markdown
2) **T102-STD-004-CLAUSE-002 (Placement Standards)**

   T102-STD-004-CLAUSE-002: Combined standard-specification files MUST be placed according to subclauses `T102-STD-004-CLAUSE-002A` through `T102-STD-004-CLAUSE-002C`.

   - `T102-STD-004-CLAUSE-002A (Designated standards directory requirement)`
     - Combined standard-specification files for the T102 consultant scope MUST live under the designated standards directory per `T102-STD-004-CLAUSE-001B`.

   - `T102-STD-004-CLAUSE-002B (Index-only hub boundary)`
     - Index artifacts (e.g., Concept/SPS indexes) MUST reference combined files via the `Canonical Path` column and MUST NOT embed the combined-file body as a substitute for that reference.

   - `T102-STD-004-CLAUSE-002C (Consistency requirement)`
     - Placement MUST follow established artifact section numbering without local deviations.
```

#### Subclauses introduced
- `T102-STD-004-CLAUSE-002A`
- `T102-STD-004-CLAUSE-002B`
- `T102-STD-004-CLAUSE-002C`

#### Rationale
- Aligns STD-004 with R2 (T102-PH001-ST001-AC008-SES001-DEC001) and Option B boundary (T102-PH001-ST001-AC008-SES001-DEC002) where applicable.
- Closes the CLAUSE-017 derivative traceability gap by ensuring directory/naming and structure rules are governed in STD-004.

### CLAUSE-003 — Entry Creation Workflow

#### Current text (as-is)
```markdown

3) **T102-STD-004-CLAUSE-003 (Entry Creation Workflow)**
   To create a new ADR index entry:
   1. Add a new row to the appropriate index table using the required schema per `T102-STD-004-CLAUSE-001`.
   2. Assign the next sequential ID for that scope.
   3. Create a combined standard-specification file at the canonical path using the standard-specification template, applying CLAUSE entries under `## Specification` and DR body structure under `## Decision Record` per `T102-STD-004-CLAUSE-004`.
   4. Ensure References follow `T102-STD-005`.
   5. Populate the Canonical Path column in the index row with the full repo-relative path to the combined file.
```

#### Issues identified
- Non-conformant: procedural imperatives lack explicit normative keywords; missing explicit governance for naming convention used by derivative guideline.

#### Proposed replacement text (copy/paste-ready)
```markdown
3) **T102-STD-004-CLAUSE-003 (Entry Creation Workflow)**

   T102-STD-004-CLAUSE-003: To create a new ADR index entry and its corresponding combined standard-specification file, authors MUST satisfy subclauses `T102-STD-004-CLAUSE-003A` through `T102-STD-004-CLAUSE-003F`.

   - `T102-STD-004-CLAUSE-003A (File Naming Convention)`
     - Combined standard-specification filenames MUST follow `<STD-ID>_<title-slug>.md` where `<title-slug>` is lowercase, spaces → `-`, non-alphanumeric characters removed/replaced with `-`, and repeated `-` collapsed.

   - `T102-STD-004-CLAUSE-003B (Create index row)`
     1. Authors MUST add a new row to the appropriate index table using the required schema per `T102-STD-004-CLAUSE-001`.

   - `T102-STD-004-CLAUSE-003C (Assign ID)`
     2. Authors MUST assign the next sequential ID for that scope.

   - `T102-STD-004-CLAUSE-003D (Create combined file)`
     3. Authors MUST create a combined standard-specification file at the canonical path using the standard-specification template, applying CLAUSE entries under `## Specification` and DR body structure under `## Decision Record` per `T102-STD-004-CLAUSE-004`.

   - `T102-STD-004-CLAUSE-003E (References conformance)`
     4. Authors MUST ensure References follow `T102-STD-005`.

   - `T102-STD-004-CLAUSE-003F (Canonical Path population)`
     5. Authors MUST populate the Canonical Path column in the index row with the full repo-relative path to the combined file.
```

#### Subclauses introduced
- `T102-STD-004-CLAUSE-003A`
- `T102-STD-004-CLAUSE-003B`
- `T102-STD-004-CLAUSE-003C`
- `T102-STD-004-CLAUSE-003D`
- `T102-STD-004-CLAUSE-003E`
- `T102-STD-004-CLAUSE-003F`

#### Rationale
- Aligns STD-004 with R2 (T102-PH001-ST001-AC008-SES001-DEC001) and Option B boundary (T102-PH001-ST001-AC008-SES001-DEC002) where applicable.
- Closes the CLAUSE-017 derivative traceability gap by ensuring directory/naming and structure rules are governed in STD-004.

### CLAUSE-004 — DR Body Template

#### Current text (as-is)
```markdown

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
```

#### Issues identified
- Conformant content but violates R2 single-statement discipline; requires decomposition into 004A–004D.

#### Proposed replacement text (copy/paste-ready)
```markdown
4) **T102-STD-004-CLAUSE-004 (DR Body Template)**

   T102-STD-004-CLAUSE-004: Nested ADR bodies in combined standard-specification files MUST conform to subclauses `T102-STD-004-CLAUSE-004A` through `T102-STD-004-CLAUSE-004D`.

   - `T102-STD-004-CLAUSE-004A (Format)`
     - Nested ADR header MUST be rendered as: `* **<STD-ID>-ADR-### (<Title>)** {#<anchor>}`.

   - `T102-STD-004-CLAUSE-004B (Required subheadings)`
     - Nested ADR body MUST include these subheadings:
       * **Context**
       * **Decision**
       * **Alternatives Considered**
       * **Consequences**

   - `T102-STD-004-CLAUSE-004C (Body formatting rules)`
     - Main bold headings (e.g. `* **Context**`) MUST be preceded by two newlines.
     - Content MUST start on a new line and INDENTED under the heading with no space in between.

   - `T102-STD-004-CLAUSE-004D (Section placement)`
     - In combined standard-specification files, the DR body MUST live under `## Decision Record`. References and Provenance are STD-level sections.
```

#### Subclauses introduced
- `T102-STD-004-CLAUSE-004A`
- `T102-STD-004-CLAUSE-004B`
- `T102-STD-004-CLAUSE-004C`
- `T102-STD-004-CLAUSE-004D`

#### Rationale
- Aligns STD-004 with R2 (T102-PH001-ST001-AC008-SES001-DEC001) and Option B boundary (T102-PH001-ST001-AC008-SES001-DEC002) where applicable.

### CLAUSE-005 — Specification Clauses

#### Current text (as-is)
```markdown

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
```

#### Issues identified
- Non-conformant structurally under its own single-statement discipline; overloaded; must be simplified into explicit subclauses.

#### Proposed replacement text (copy/paste-ready)
```markdown
5) **T102-STD-004-CLAUSE-005 (Specification Clauses)**

   T102-STD-004-CLAUSE-005: The `## Specification` section of a combined standard-specification file MUST be constructed using clause items as defined by subclauses `T102-STD-004-CLAUSE-005A` through `T102-STD-004-CLAUSE-005G`.

   - `T102-STD-004-CLAUSE-005A (Normative reference)`
     - `CLAUSE` token type construction and semantics MUST follow `T102-STD-005-CLAUSE-005D (Specification Clause Semantics)`.

   - `T102-STD-004-CLAUSE-005B (Clause item format)`
     - Each clause item MUST be rendered as: `n) **<CLAUSE-ID> (<Title>)**`.
     - `<CLAUSE-ID>` MUST conform to `T102-STD-005-CLAUSE-005D`.

	   - `T102-STD-004-CLAUSE-005C (Clause construction requirements)`
	     - Each clause MUST be a single primary normative statement (avoid compound obligations where feasible).
	     - If a parent clause would otherwise contain multiple distinct obligations, those obligations MUST be decomposed into named subclauses (e.g., `...-CLAUSE-###A`, `...-CLAUSE-###B`) per `T102-STD-005-CLAUSE-005D`.
	     - If additional detail is required (and does not introduce additional obligations), it SHOULD be provided as subclauses per `T102-STD-005-CLAUSE-005D`.
	     - Clause Titles MUST follow the title conventions defined in `T102-STD-005-CLAUSE-001`.

   - `T102-STD-004-CLAUSE-005D (Ordering rules)`
     - `CLAUSE` IDs MUST be sequential in the order they appear within the Specification section (`001`, `002`, `003`, ...).
     - Subclauses MUST immediately follow their parent clause.

   - `T102-STD-004-CLAUSE-005E (Markdown subclause rendering)`
     - Subclauses SHOULD be rendered as nested bullet items under the parent clause and prefixed by their full CLAUSE-ID (e.g., `<STD-ID>-CLAUSE-002A`).

   - `T102-STD-004-CLAUSE-005F (Referencing)`
     - Other artifacts MAY reference specific Specification clauses using the formal format defined in `T102-STD-005-CLAUSE-004 (Reference Semantics)`.

   - `T102-STD-004-CLAUSE-005G (Non-duplication constraint)`
     - `T102-STD-004` MUST NOT redefine the syntax, scope validity, or semantic authority of `CLAUSE` IDs; those are defined in `T102-STD-005-CLAUSE-005D`.
```

#### Subclauses introduced
- `T102-STD-004-CLAUSE-005A`
- `T102-STD-004-CLAUSE-005B`
- `T102-STD-004-CLAUSE-005C`
- `T102-STD-004-CLAUSE-005D`
- `T102-STD-004-CLAUSE-005E`
- `T102-STD-004-CLAUSE-005F`
- `T102-STD-004-CLAUSE-005G`

#### Rationale
- Aligns STD-004 with R2 (T102-PH001-ST001-AC008-SES001-DEC001) and Option B boundary (T102-PH001-ST001-AC008-SES001-DEC002) where applicable.

### CLAUSE-006 — Cross-Artifact Linking Patterns

#### Current text (as-is)
```markdown

6) **T102-STD-004-CLAUSE-006 (Cross-Artifact Linking Patterns)**

   - **STD Internal DR Pattern.**
     A combined standard-specification file MUST contain its decision record internally under `## Decision Record` using the nested ADR format from `T102-STD-004-CLAUSE-004`.

   - **Decision Record Context Pattern.**
     The nested ADR **Context** SHOULD state the motivating problem in narrative form and MAY use shorthand IDs for traceability.

   - **Context/References Boundary.**
     The nested ADR **Context** MUST NOT use a formal "Governed By" citation line. Formal citations belong in the STD-level `## References` section.

   - **Index → Combined File (Canonical Path Linkage).**
     Concept/SPS index tables link to combined files via full repo-relative Canonical Path (per `T102-STD-004-CLAUSE-001`); Phase 1 links at file granularity.
```

#### Issues identified
- Conformant content but benefits from subclause naming for lintability and R2 discipline.

#### Proposed replacement text (copy/paste-ready)
```markdown
6) **T102-STD-004-CLAUSE-006 (Cross-Artifact Linking Patterns)**

   T102-STD-004-CLAUSE-006: Combined standard-specification files MUST satisfy the cross-artifact linking patterns defined by subclauses `T102-STD-004-CLAUSE-006A` through `T102-STD-004-CLAUSE-006D`.

   - `T102-STD-004-CLAUSE-006A (STD internal DR pattern)`
     - A combined standard-specification file MUST contain its decision record internally under `## Decision Record` using the nested ADR format from `T102-STD-004-CLAUSE-004`.

   - `T102-STD-004-CLAUSE-006B (Decision record context pattern)`
     - The nested ADR **Context** SHOULD state the motivating problem in narrative form and MAY use shorthand IDs for traceability.

   - `T102-STD-004-CLAUSE-006C (Context/References boundary)`
     - The nested ADR **Context** MUST NOT use a formal "Governed By" citation line. Formal citations belong in the STD-level `## References` section.

   - `T102-STD-004-CLAUSE-006D (Index → combined file linkage)`
     - Concept/SPS index tables MUST link to combined files via full repo-relative Canonical Path (per `T102-STD-004-CLAUSE-001`); Phase 1 links at file granularity.
```

#### Subclauses introduced
- `T102-STD-004-CLAUSE-006A`
- `T102-STD-004-CLAUSE-006B`
- `T102-STD-004-CLAUSE-006C`
- `T102-STD-004-CLAUSE-006D`

#### Rationale
- Aligns STD-004 with R2 (T102-PH001-ST001-AC008-SES001-DEC001) and Option B boundary (T102-PH001-ST001-AC008-SES001-DEC002) where applicable.

### CLAUSE-007 — Anchor Title Stability

#### Current text (as-is)
```markdown

7) **T102-STD-004-CLAUSE-007 (Anchor Title Stability)**

   - Anchors MUST be lower-kebab derived from the Title.
   - Anchors MUST remain stable across file moves/splits.
   - If Title changes, keep the old anchor unless an explicit migration is performed.
   - Phase 1 stability contract: combined-file names and canonical paths SHOULD remain stable after migration completion. Anchors extracted from Concept remain stable within their combined file.
```

#### Issues identified
- Non-conformant: derivation rule contradicts deployed anchor scheme (ID + Title); must be amended.

#### Proposed replacement text (copy/paste-ready)
```markdown
7) **T102-STD-004-CLAUSE-007 (Anchor Title Stability)**

   T102-STD-004-CLAUSE-007: Anchors MUST be lower-kebab derived from `<ID> + <Title>` and MUST satisfy subclauses `T102-STD-004-CLAUSE-007A` through `T102-STD-004-CLAUSE-007D`.

   - `T102-STD-004-CLAUSE-007A (Normalization rules)`
     - Normalization MUST apply: spaces → `-`; `&` → `and`; strip punctuation; collapse repeated `-`.

   - `T102-STD-004-CLAUSE-007B (Stability across moves/splits)`
     - Anchors MUST remain stable across file moves/splits.

   - `T102-STD-004-CLAUSE-007C (Title change migration)`
     - If Title changes, keep the old anchor unless an explicit migration is performed.

   - `T102-STD-004-CLAUSE-007D (Phase 1 stability contract)`
     - Phase 1 stability contract: combined-file names and canonical paths SHOULD remain stable after migration completion. Anchors extracted from Concept remain stable within their combined file.
```

#### Subclauses introduced
- `T102-STD-004-CLAUSE-007A`
- `T102-STD-004-CLAUSE-007B`
- `T102-STD-004-CLAUSE-007C`
- `T102-STD-004-CLAUSE-007D`

#### Rationale
- Aligns STD-004 with R2 (T102-PH001-ST001-AC008-SES001-DEC001) and Option B boundary (T102-PH001-ST001-AC008-SES001-DEC002) where applicable.

### CLAUSE-008 — Lifecycle Coherence

#### Current text (as-is)
```markdown

8) **T102-STD-004-CLAUSE-008 (Lifecycle Coherence)**

   When a governing STD changes **Status** or is **Superseded**, affected combined files MUST:
   - update the nested ADR **Context** wording to the current governance rationale as needed; and
   - add prior governing IDs to **References** as appropriate; and
   - perform this update in the next modification to the combined file or in a dedicated "governance sync" change set.
```

#### Issues identified
- Conformant intent; refactor into anchor + subclauses for R2 consistency.

#### Proposed replacement text (copy/paste-ready)
```markdown
8) **T102-STD-004-CLAUSE-008 (Lifecycle Coherence)**

   T102-STD-004-CLAUSE-008: When a governing STD changes **Status** or is **Superseded**, affected combined files MUST satisfy subclauses `T102-STD-004-CLAUSE-008A` through `T102-STD-004-CLAUSE-008C`.

   - `T102-STD-004-CLAUSE-008A (Context sync)`
     - Combined files MUST update the nested ADR **Context** wording to the current governance rationale as needed.

   - `T102-STD-004-CLAUSE-008B (Reference sync)`
     - Combined files MUST add prior governing IDs to **References** as appropriate.

   - `T102-STD-004-CLAUSE-008C (Timing)`
     - Combined files MUST perform this update in the next modification to the combined file or in a dedicated "governance sync" change set.
```

#### Subclauses introduced
- `T102-STD-004-CLAUSE-008A`
- `T102-STD-004-CLAUSE-008B`
- `T102-STD-004-CLAUSE-008C`

#### Rationale
- Aligns STD-004 with R2 (T102-PH001-ST001-AC008-SES001-DEC001) and Option B boundary (T102-PH001-ST001-AC008-SES001-DEC002) where applicable.

### CLAUSE-009 — Status Management

#### Current text (as-is)
```markdown

9) **T102-STD-004-CLAUSE-009 (Status Management)**

   - Lifecycle: `Proposed → Accepted → Deprecated`
   - Superseded IDs MUST be captured in the **Supersedes** column and, where applicable, referenced in body text.
   - For specification lifecycle stages governing CLAUSE content evolution, see `T102-STD-004-CLAUSE-017`.
```

#### Issues identified
- Minor gap: status guidance present but Effective semantics not cross-referenced; refactor for R2 consistency.

#### Proposed replacement text (copy/paste-ready)
```markdown
9) **T102-STD-004-CLAUSE-009 (Status Management)**

   T102-STD-004-CLAUSE-009: Status and supersession metadata for combined files MUST be maintained per subclauses `T102-STD-004-CLAUSE-009A` through `T102-STD-004-CLAUSE-009C`.

   - `T102-STD-004-CLAUSE-009A (Lifecycle)`
     - Lifecycle: `Proposed → Accepted → Deprecated`.

   - `T102-STD-004-CLAUSE-009B (Supersedes handling)`
     - Superseded IDs MUST be captured in the **Supersedes** column and, where applicable, referenced in body text.

   - `T102-STD-004-CLAUSE-009C (Effective semantics)`
     - `Effective` semantics are governed by `T102-STD-004-CLAUSE-001A`.
     - For specification lifecycle stages governing CLAUSE content evolution, see `T102-STD-004-CLAUSE-017`.
```

#### Subclauses introduced
- `T102-STD-004-CLAUSE-009A`
- `T102-STD-004-CLAUSE-009B`
- `T102-STD-004-CLAUSE-009C`

#### Rationale
- Aligns STD-004 with R2 (T102-PH001-ST001-AC008-SES001-DEC001) and Option B boundary (T102-PH001-ST001-AC008-SES001-DEC002) where applicable.

### CLAUSE-010 — Precedence Conflicts Hierarchy

#### Current text (as-is)
```markdown

10) **T102-STD-004-CLAUSE-010 (Precedence Conflicts Hierarchy)**

    For conflict resolution across DRIDs:
    `Initiative STD > Initiative ADR > Epic ADR > Feature ADR > Story ADR`

    See `T102-STD-003` and `T102-STD-005` for full hierarchy and directionality constraints.
```

#### Issues identified
- Conformant; keep semantics; no change required beyond R2 formatting if desired.

#### Proposed replacement text (copy/paste-ready)
```markdown

10) **T102-STD-004-CLAUSE-010 (Precedence Conflicts Hierarchy)**

    T102-STD-004-CLAUSE-010: Precedence conflicts across DRIDs MUST be resolved using the hierarchy defined by subclauses `T102-STD-004-CLAUSE-010A` and `T102-STD-004-CLAUSE-010B`.

    - `T102-STD-004-CLAUSE-010A (Hierarchy)`
      - `Initiative STD > Initiative ADR > Epic ADR > Feature ADR > Story ADR`

    - `T102-STD-004-CLAUSE-010B (Reference)`
      - See `T102-STD-003` and `T102-STD-005` for full hierarchy and directionality constraints.
```

#### Subclauses introduced
- `T102-STD-004-CLAUSE-010A`
- `T102-STD-004-CLAUSE-010B`

#### Rationale
- Aligns STD-004 with R2 (T102-PH001-ST001-AC008-SES001-DEC001) and Option B boundary (T102-PH001-ST001-AC008-SES001-DEC002) where applicable.

### CLAUSE-011 — Consequences Scope Requirements

#### Current text (as-is)
```markdown

11) **T102-STD-004-CLAUSE-011 (Consequences Scope Requirements)**

    - **STD Consequences** SHOULD cover: policy/precedence impacts; compliance expectations; migration/rollout; automation/traceability effects.
    - **ADR Consequences** SHOULD cover: quality trade-offs; constraints introduced; operational effects; debt/risks.
```

#### Issues identified
- Conformant; keep semantics; no change required beyond R2 formatting if desired.

#### Proposed replacement text (copy/paste-ready)
```markdown

11) **T102-STD-004-CLAUSE-011 (Consequences Scope Requirements)**

    T102-STD-004-CLAUSE-011: Consequences sections SHOULD cover the scope defined by subclauses `T102-STD-004-CLAUSE-011A` and `T102-STD-004-CLAUSE-011B`.

    - `T102-STD-004-CLAUSE-011A (STD Consequences scope)`
      - **STD Consequences** SHOULD cover: policy/precedence impacts; compliance expectations; migration/rollout; automation/traceability effects.

    - `T102-STD-004-CLAUSE-011B (ADR Consequences scope)`
      - **ADR Consequences** SHOULD cover: quality trade-offs; constraints introduced; operational effects; debt/risks.
```

#### Subclauses introduced
- `T102-STD-004-CLAUSE-011A`
- `T102-STD-004-CLAUSE-011B`

#### Rationale
- Aligns STD-004 with R2 (T102-PH001-ST001-AC008-SES001-DEC001) and Option B boundary (T102-PH001-ST001-AC008-SES001-DEC002) where applicable.

### CLAUSE-012 — References & Provenance

#### Current text (as-is)
```markdown

12) **T102-STD-004-CLAUSE-012 (References & Provenance)**

    - **References** MUST use the formal reference style defined in `T102-STD-005`.
    - **Provenance** MUST list relevant repo-relative paths (no raw URLs).
```

#### Issues identified
- Minor structural gap: compound obligation (References + Provenance) should be decomposed into subclauses 012A/012B.

#### Proposed replacement text (copy/paste-ready)
```markdown
12) **T102-STD-004-CLAUSE-012 (References & Provenance)**

    T102-STD-004-CLAUSE-012: Combined files MUST satisfy the References and Provenance requirements defined by subclauses `T102-STD-004-CLAUSE-012A` and `T102-STD-004-CLAUSE-012B`.

    - `T102-STD-004-CLAUSE-012A (References)`
      - References MUST use the formal reference style defined in `T102-STD-005-CLAUSE-004 (Reference Semantics)`.

    - `T102-STD-004-CLAUSE-012B (Provenance)`
      - Provenance MUST list repo-relative paths (and MAY include higher-level narrative context).
```

#### Subclauses introduced
- `T102-STD-004-CLAUSE-012A`
- `T102-STD-004-CLAUSE-012B`

#### Rationale
- Aligns STD-004 with R2 (T102-PH001-ST001-AC008-SES001-DEC001) and Option B boundary (T102-PH001-ST001-AC008-SES001-DEC002) where applicable.

### CLAUSE-013 — Variance ADR Contract

#### Current text (as-is)
```markdown

13) **T102-STD-004-CLAUSE-013 (Variance ADR Contract)**

    A "Variance ADR" is required when a downstream artifact MUST deviate from an upstream standard. It MUST include:
    - **Variance From:** list of overridden upstream IDs.
    - **Rationale:** technical/environment justification.
    - **Scope Impact:** what inheritance/automation breaks.
    - **Lifecycle:** MUST be `Accepted` via governance sign-off (Client or delegated authority).
```

#### Issues identified
- Conformant intent but contains multiple required elements; decompose into subclauses without semantic change.

#### Proposed replacement text (copy/paste-ready)
```markdown
13) **T102-STD-004-CLAUSE-013 (Variance ADR Contract)**

    T102-STD-004-CLAUSE-013: Variance artifacts MUST document variances using the contract defined by subclauses `T102-STD-004-CLAUSE-013A` through `T102-STD-004-CLAUSE-013D`.

    - `T102-STD-004-CLAUSE-013A (Variance From)`
      - A variance ADR MUST include a **Variance From** list of overridden upstream IDs.

    - `T102-STD-004-CLAUSE-013B (Rationale)`
      - A variance ADR MUST include a **Rationale** describing technical/environment justification.

    - `T102-STD-004-CLAUSE-013C (Scope Impact)`
      - A variance ADR MUST include a **Scope Impact** describing what inheritance/automation breaks.

    - `T102-STD-004-CLAUSE-013D (Lifecycle)`
      - A variance ADR lifecycle MUST be `Accepted` via governance sign-off (Client or delegated authority).
```

#### Subclauses introduced
- `T102-STD-004-CLAUSE-013A`
- `T102-STD-004-CLAUSE-013B`
- `T102-STD-004-CLAUSE-013C`
- `T102-STD-004-CLAUSE-013D`

#### Rationale
- Aligns STD-004 with R2 (T102-PH001-ST001-AC008-SES001-DEC001) and Option B boundary (T102-PH001-ST001-AC008-SES001-DEC002) where applicable.

### CLAUSE-014 — Decision Promotion Workflow

#### Current text (as-is)
```markdown

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
```

#### Issues identified
- Out-of-date framing: targets independent ADR as alternative endpoint; rewrite for STD-owns-ADR model; flag for potential migration to STD-009.

#### Proposed replacement text (copy/paste-ready)
```markdown
14) **T102-STD-004-CLAUSE-014 (Decision Promotion Workflow)**

    T102-STD-004-CLAUSE-014: Promotion of decision content from research and guidance into Standards SHOULD follow subclauses `T102-STD-004-CLAUSE-014A` through `T102-STD-004-CLAUSE-014E`.

    - `T102-STD-004-CLAUSE-014A (Research — RES)`
      - Authors SHOULD use `RES-SID` artifacts to commission and document evidence, options, and empirical findings for a specific scope (Initiative/Epic/Feature).

    - `T102-STD-004-CLAUSE-014B (Implementation Guidance — IG)`
      - Authors SHOULD encode candidate implementation patterns at the appropriate scope (typically Feature); IGs MAY evolve as research is refined.

    - `T102-STD-004-CLAUSE-014C (Standards — STD)`
      - Authors SHOULD promote stable, cross-cutting, or long-lived patterns into formal `STD` records when:
        - (a) the pattern affects multiple artifacts or features; or
        - (b) the pattern requires explicit governance (ownership, status, supersedes) beyond implementation detail.
      - When promoted, the `STD` MUST contain a nested ADR for rationale per `T102-STD-004-CLAUSE-004`.

    - `T102-STD-004-CLAUSE-014D (Traceability)`
      - Specifications SHOULD reference governing research and guidance in **Provenance** and **References**, rather than duplicating detailed patterns.

    - `T102-STD-004-CLAUSE-014E (Scope guidance)`
      - Epic-level ADRs SHOULD be used for cross-feature decisions (e.g., shared vocabularies, common architectures).
      - Feature-level ADRs SHOULD be reserved for significant, feature-local architectural decisions that cannot reasonably be governed at Epic scope.
      - Routine implementation details MAY remain in guidance without a dedicated ADR.

    Note: This workflow is a candidate for migration to `T102-STD-009` in ST002 once STD/registry boundaries are baselined.
```

#### Subclauses introduced
- `T102-STD-004-CLAUSE-014A`
- `T102-STD-004-CLAUSE-014B`
- `T102-STD-004-CLAUSE-014C`
- `T102-STD-004-CLAUSE-014D`
- `T102-STD-004-CLAUSE-014E`

#### Rationale
- Aligns STD-004 with R2 (T102-PH001-ST001-AC008-SES001-DEC001) and Option B boundary (T102-PH001-ST001-AC008-SES001-DEC002) where applicable.

### CLAUSE-015 — Automation & Linting Checks

#### Current text (as-is)
```markdown

15) **T102-STD-004-CLAUSE-015 (Automation & Linting Checks)**

    Authors SHOULD pass these checks:
    - Combined file contains `## Specification` and `## Decision Record` headings in that order.
    - Nested ADR body **Context** does not include a "Governed By" citation line.
    - Combined file contains STD-level `## References` and `## Provenance` headings.
    - Every `Canonical Path` in an index resolves to an existing file.
```

#### Issues identified
- Conformant but should be updated to cover anchor derivation and designated directory checks; refactor into subclauses.

#### Proposed replacement text (copy/paste-ready)
```markdown
15) **T102-STD-004-CLAUSE-015 (Automation & Linting Checks)**

    T102-STD-004-CLAUSE-015: Authors SHOULD satisfy the automation and linting checks defined by subclauses `T102-STD-004-CLAUSE-015A` through `T102-STD-004-CLAUSE-015E`.

    - `T102-STD-004-CLAUSE-015A (Required headings)`
      - Combined file contains `## Specification` and `## Decision Record` headings in that order.

    - `T102-STD-004-CLAUSE-015B (Nested ADR hygiene)`
      - Nested ADR body **Context** does not include a "Governed By" citation line.

    - `T102-STD-004-CLAUSE-015C (STD-level sections)`
      - Combined file contains STD-level `## References` and `## Provenance` headings.

    - `T102-STD-004-CLAUSE-015D (Index resolution)`
      - Every `Canonical Path` in an index resolves to an existing file under the designated standards directory per `T102-STD-004-CLAUSE-001B`.

    - `T102-STD-004-CLAUSE-015E (Anchor derivation consistency)`
      - Anchors follow the derivation and stability rules defined in `T102-STD-004-CLAUSE-007`.
```

#### Subclauses introduced
- `T102-STD-004-CLAUSE-015A`
- `T102-STD-004-CLAUSE-015B`
- `T102-STD-004-CLAUSE-015C`
- `T102-STD-004-CLAUSE-015D`
- `T102-STD-004-CLAUSE-015E`

#### Rationale
- Aligns STD-004 with R2 (T102-PH001-ST001-AC008-SES001-DEC001) and Option B boundary (T102-PH001-ST001-AC008-SES001-DEC002) where applicable.

### CLAUSE-016 — Combined-File Canonical Structure

#### Current text (as-is)
```markdown

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
```

#### Issues identified
- Minor gap: canonical structure wording may accidentally prohibit anchor metadata lines; add explicit MAY.

#### Proposed replacement text (copy/paste-ready)
```markdown
16) **T102-STD-004-CLAUSE-016 (Combined-File Canonical Structure)**

	    T102-STD-004-CLAUSE-016: In Phase 1, every combined standard-specification file MUST conform to the canonical structure defined by subclauses `T102-STD-004-CLAUSE-016A` through `T102-STD-004-CLAUSE-016D`.

    - `T102-STD-004-CLAUSE-016A (Required sections and order)`
      - Every combined file MUST contain exactly these sections in order:
        1. `# <STD-ID> — <Title>`
        2. `## Specification`
        3. `## Decision Record`
        4. `## References`
        5. `## Provenance`

	    - `T102-STD-004-CLAUSE-016B (Section semantics)`
	      - `## Specification` contains normative `CLAUSE` items (enforceable language MUST follow the controlled vocabulary defined in `T102-STD-004-CLAUSE-016D`).
	      - `## Decision Record` contains one current nested ADR body (`<STD-ID>-ADR-###`) with informative rationale.
	      - `## References` and `## Provenance` are STD-level sections governing the entire file.

	    - `T102-STD-004-CLAUSE-016C (Anchor metadata lines)`
	      - Non-heading metadata lines (e.g., explicit anchor lines in the form `{#anchor}`) MAY appear immediately after the `# <STD-ID> — <Title>` header and immediately after the nested ADR header line; this does not count as an additional required section.

	    - `T102-STD-004-CLAUSE-016D (Normative vocabulary guidance)`
	      - A single primary drafting vocabulary MUST be used within a given `STD` specification section.
	      - BCP 14 keywords (`MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, `MAY`) are the preferred primary vocabulary for Phase 1.
	      - Mixing RFC-style (`MUST`/`SHOULD`/`MAY`) and ISO/IEEE-style (`SHALL`/`SHOULD`/`MAY`) keywords within the same `STD` SHOULD be avoided unless explicitly justified as a legacy-compatibility exception.
```

#### Subclauses introduced
- `T102-STD-004-CLAUSE-016A`
- `T102-STD-004-CLAUSE-016B`
- `T102-STD-004-CLAUSE-016C`
- `T102-STD-004-CLAUSE-016D`

#### Rationale
- Aligns STD-004 with R2 (T102-PH001-ST001-AC008-SES001-DEC001) and Option B boundary (T102-PH001-ST001-AC008-SES001-DEC002) where applicable.
- Closes the CLAUSE-017 derivative traceability gap by ensuring directory/naming and structure rules are governed in STD-004.

### CLAUSE-017 — Specification Lifecycle & Authority Chain

#### Current text (as-is)
```markdown

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
```

#### Issues identified
- Minor gap: derivative traceability must be enforced; R2 must ensure directory + naming are governed in STD-004 to prevent normative leakage.

#### Proposed replacement text (copy/paste-ready)
```markdown
17) **T102-STD-004-CLAUSE-017 (Specification Lifecycle & Authority Chain)**

    T102-STD-004-CLAUSE-017: Specification lifecycle management and derivative authority MUST follow subclauses `T102-STD-004-CLAUSE-017A` through `T102-STD-004-CLAUSE-017D`.

    - `T102-STD-004-CLAUSE-017A (Specification lifecycle stages)`
      - `Draft`: Initial authoring; content is subject to change without formal review.
      - `Proposed`: Content submitted for review; normative language present but not yet binding.
      - `Accepted`: Content is binding; normative language is enforceable within the declared scope.
      - `Amended`: Accepted content modified via a governed change process; prior version is superseded.
      - `Deprecated`: Content is no longer binding; retained for historical reference.

    - `T102-STD-004-CLAUSE-017B (Authority derivation chain)`
      - Authority flows downward: Specification (CLAUSEs) → Guideline (informative) → Template (derivative).
      - A Guideline MUST cite the governing CLAUSE(s) it derives from.
      - A Template MUST conform to structural requirements prescribed by governing CLAUSEs and Guideline.

    - `T102-STD-004-CLAUSE-017C (Conformance coupling rule)`
      - When a Specification CLAUSE is added, modified, or deprecated, all derivative artifacts (Guideline and Template) MUST be updated in the same changeset to maintain conformance.

    - `T102-STD-004-CLAUSE-017D (No normative leakage)`
      - Derivatives MUST NOT introduce normative rules that are not traceable to a governing CLAUSE.
```

#### Subclauses introduced
- `T102-STD-004-CLAUSE-017A`
- `T102-STD-004-CLAUSE-017B`
- `T102-STD-004-CLAUSE-017C`
- `T102-STD-004-CLAUSE-017D`

#### Rationale
- Aligns STD-004 with R2 (T102-PH001-ST001-AC008-SES001-DEC001) and Option B boundary (T102-PH001-ST001-AC008-SES001-DEC002) where applicable.
- Closes the CLAUSE-017 derivative traceability gap by ensuring directory/naming and structure rules are governed in STD-004.

### CLAUSE-018 — Normative/Informative Boundary Hygiene (RES-007)

#### Current text (as-is)
- N/A (new clause proposed by RES-007 integration; introduced in AC009).

#### Issues identified
- **RES-007 Critical gap**: Combined-file architecture is industry-aligned, but boundary hygiene is underspecified, increasing the risk of normative language “leaking” into informative sections (especially the nested Decision Record) and into derivatives.

#### Proposed new clause text (copy/paste-ready)
```markdown
18) **T102-STD-004-CLAUSE-018 (Normative/Informative Boundary Hygiene)**

    T102-STD-004-CLAUSE-018: Combined standard-specification files MUST enforce a clear boundary between normative and informative content per subclauses `T102-STD-004-CLAUSE-018A` through `T102-STD-004-CLAUSE-018D`.

    - `T102-STD-004-CLAUSE-018A (Normative section authority)`
      - The `## Specification` section is the authoritative normative surface of a combined file.
      - The `## Decision Record` section is informative rationale and MUST NOT create new obligations.

    - `T102-STD-004-CLAUSE-018B (Informative section keyword hygiene)`
      - Informative sections (including `## Decision Record`) MUST NOT use BCP 14 keywords in uppercase (`MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, `MAY`) to express requirements.
      - If an informative section needs to refer to a normative requirement, it MUST do so by (a) citing the governing `CLAUSE` reference and/or (b) quoting the normative text as a quotation (e.g., in code formatting) and explicitly labeling it as a quote.

    - `T102-STD-004-CLAUSE-018C (Normative/informative labeling rule)`
      - If any non-Specification section contains normative requirements, that section MUST be explicitly labeled as normative and the governing CLAUSE(s) MUST be identified.

    - `T102-STD-004-CLAUSE-018D (Derivative boundary alignment)`
      - Any derivative artifact that describes boundary hygiene expectations MUST cite this CLAUSE and MUST NOT introduce additional boundary rules beyond what is governed here.
```

#### Subclauses introduced
- `T102-STD-004-CLAUSE-018A`
- `T102-STD-004-CLAUSE-018B`
- `T102-STD-004-CLAUSE-018C`
- `T102-STD-004-CLAUSE-018D`

#### Rationale
- Implements RES-007 “boundary hygiene” as an explicit governed contract, reducing drift and accidental normativity in combined files.

## IV. Derivative Update Specification

 This proposal requires updating derivatives in the same changeset as STD-004 per `T102-STD-004-CLAUSE-017`.

### A. Guideline (`prompt/templates/consultant/standards/guideline_standard_specs.md`)
- Update "Canonical location" citation to reference `T102-STD-004-CLAUSE-002` and `T102-STD-004-CLAUSE-002A`.
- Update "File naming convention" citation to reference `T102-STD-004-CLAUSE-003A` (and remove reliance on CLAUSE-001 for naming rules).
- Add boundary hygiene guidance for `## Decision Record` and cite `T102-STD-004-CLAUSE-018` (informative section keyword hygiene and “no new obligations” rule).
- Verify all other `[per ...]` citations remain valid after subclause introduction (CLAUSE-004, 005, 012, 016, 017).

### B. Template (`prompt/templates/consultant/standards/template_standard_specs.md`)
- Add an anchor metadata line placeholder after `# <STD-ID> — <Title>` to match `T102-STD-004-CLAUSE-016C` allowance (if the repo standardizes on explicit `{#...}` lines).
- Verify the required headings and order remain compliant with `T102-STD-004-CLAUSE-016A`.

### C. SPS MVC (`prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md`)
- Rewrite the STD-004 description to reflect Option B identity (combined-file authoring standard; STD-009 remains the registry standard).
- Rewrite MVC items to cite refocused CLAUSEs:
  1. Use combined file index schemas and column definitions (CLAUSE-001).
  2. Place combined files under the designated standards directory (CLAUSE-002).
  3. Create combined files using the workflow and DR body template (CLAUSE-003, CLAUSE-004).
  4. Maintain stable anchors per the anchor stability rules (CLAUSE-007).

## V. Deferred Items Cross-Reference

Deferred items are registered in the analysis artifact §X (DEFERRED ITEMS REGISTER → ST002). This proposal does not implement those changes.

## VI. Developer Execution Instructions

1. Edit STD-004 and apply the per-CLAUSE replacements in §III.
2. Edit guideline and update citations per §IV.A.
3. Edit template if needed per §IV.B.
4. Edit SPS and apply MVC rewrite per §IV.C.
5. Execute TK006 (self-compliance re-audit) after TK005 implementation.

All edits MUST be completed as a single changeset per `T102-STD-004-CLAUSE-017`.

## VII. Validation Checklist (Post-Implementation)

- [ ] Each CLAUSE in refactored STD-004 has exactly one anchor normative statement
- [ ] All subclauses use correct ID format (`T102-STD-004-CLAUSE-###X`)
- [ ] No CLAUSE uses procedural imperatives without normative keywords
- [ ] CLAUSE-007 anchor derivation rule matches deployed anchors in the file
- [ ] Guideline citations match refactored CLAUSE IDs (no broken `[per ...]` references)
- [ ] Template structural headings match CLAUSE-016
- [ ] SPS MVC items cite valid refocused CLAUSEs
- [ ] No normative rules in guideline without traceable governing CLAUSE (CLAUSE-017)
- [ ] Boundary hygiene is enforced: `## Decision Record` does not use BCP 14 keywords to introduce obligations (CLAUSE-018)
- [ ] Vocabulary guidance is followed (single primary drafting vocabulary per STD; CLAUSE-016D)
- [ ] File naming convention is explicitly governed in STD-004 (CLAUSE-017 gap closed)
- [ ] Designated standards directory is explicitly governed in STD-004 (CLAUSE-017 gap closed)
