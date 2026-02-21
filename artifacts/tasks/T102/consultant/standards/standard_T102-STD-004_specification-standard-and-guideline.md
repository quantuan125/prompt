# T102-STD-004 — Specification Standard & Guideline
{#t102-std-004-specification-standard-and-guideline}

> **SUPERSEDED**: This standard has been promoted to **P-STD-001** (Program Governance Standard) as of 2026-02-20. See `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md`.
>
> **Alias Window (Active)**: Existing references to `T102-STD-004-CLAUSE-*` remain valid as aliases for `P-STD-001-CLAUSE-*` during the migration period. New authoring MUST reference `P-STD-001`. Alias support will be removed after a dedicated governance sync changeset.
>
> **This file is retained as a read-only historical artifact. Do not modify normative content.**

## Specification

### Specification Index
| # | Substandard | CLAUSE ID | Title | Description |
|:--|:--|:--|:--|:--|
| 1 | T102-STD-004A | T102-STD-004-CLAUSE-001 | Canonical File Structure | Defines required section order and semantics for combined standard-specification files. |
| 2 | T102-STD-004A | T102-STD-004-CLAUSE-002 | Specification Index | Requires a navigational index for standards with more than five clauses. |
| 3 | T102-STD-004A | T102-STD-004-CLAUSE-003 | Substandard Architecture | Defines substandard structure, membership, rendering, and non-token registration rules. |
| 4 | T102-STD-004A | T102-STD-004-CLAUSE-004 | Specification Lifecycle Stages | Defines lifecycle stages and formatting for specification status values. |
| 5 | T102-STD-004A | T102-STD-004-CLAUSE-005 | Authority Derivation & Conformance Coupling | Defines authority chain and conformance coupling for guideline/template derivatives. |
| 6 | T102-STD-004A | T102-STD-004-CLAUSE-006 | Anchor Stability | Defines anchor normalization, stability rules, and migration handling for title changes. |
| 7 | T102-STD-004A | T102-STD-004-CLAUSE-007 | Automation & Linting Checks | Defines recommended lint checks for required headings, indexes, and anchor rules. |
| 8 | T102-STD-004A | T102-STD-004-CLAUSE-008 | Normative Vocabulary Guidance | Defers normative keyword meanings to CON-009 and standardizes drafting vocabulary. |
| 9 | T102-STD-004B | T102-STD-004-CLAUSE-009 | STD Semantics & Scope | Defines STD token semantics, allowed scopes, and invalid usages. |
| 10 | T102-STD-004B | T102-STD-004-CLAUSE-010 | STD Canonical Specification | Defines Canonical Path semantics and incorporation-by-reference for STD specifications. |
| 11 | T102-STD-004B | T102-STD-004-CLAUSE-011 | STD Precedence & Variance | Defines precedence authority and how variances are documented and reviewed. |
| 12 | T102-STD-004B | T102-STD-004-CLAUSE-012 | STD Index Schema & Column Definitions | Defines STD Index schema and column semantics, including Canonical Path and Reference. |
| 13 | T102-STD-004B | T102-STD-004-CLAUSE-013 | STD Body Construction & Conciseness | Defines single-obligation discipline and conciseness requirements for STD bodies. |
| 14 | T102-STD-004B | T102-STD-004-CLAUSE-014 | STD Drift Controls & Lifecycle Coherence | Defines drift controls to keep specifications aligned with canonical sources. |
| 15 | T102-STD-004B | T102-STD-004-CLAUSE-015 | STD Placement & Directory Requirements | Defines standards directory placement rules and Canonical Path validity requirements. |
| 16 | T102-STD-004B | T102-STD-004-CLAUSE-016 | STD Status Management | Defines status enums and supersession metadata handling for STDs and combined files. |
| 17 | T102-STD-004B | T102-STD-004-CLAUSE-017 | Migration Tolerance | Defines alias windows and requirements for one-time resequencing migrations. |
| 18 | T102-STD-004C | T102-STD-004-CLAUSE-018 | CLAUSE Construction Requirements | Defines how to author clauses: format, titles, subclauses, and references. |
| 19 | T102-STD-004C | T102-STD-004-CLAUSE-019 | CLAUSE Ordering | Requires sequential clause numbering and adjacency of subclauses. |
| 20 | T102-STD-004C | T102-STD-004-CLAUSE-020 | Subclause Rendering | Requires bold subclause rendering and prohibits backtick-wrapped subclause format. |
| 21 | T102-STD-004C | T102-STD-004-CLAUSE-021 | Normative/Informative Boundary Hygiene | Defines rules preventing normative leakage into informative decision record sections. |
| 22 | T102-STD-004C | T102-STD-004-CLAUSE-022 | Referencing & Non-Duplication | Defines referencing patterns and prohibits redefining global CLAUSE semantics. |
| 23 | T102-STD-004D | T102-STD-004-CLAUSE-023 | ADR Index Schema | Defines ADR Index schema, ordering, and multiple ADR retention rules. |
| 24 | T102-STD-004D | T102-STD-004-CLAUSE-024 | ADR Entry Creation Workflow | Defines workflow for creating combined files and corresponding STD index entries. |
| 25 | T102-STD-004D | T102-STD-004-CLAUSE-025 | DR Body Template | Defines ADR body format, required subheadings, and per-section content requirements. |
| 26 | T102-STD-004D | T102-STD-004-CLAUSE-026 | Cross-Artifact Linking Patterns | Defines how combined files and indexes link without duplicating canonical specification. |
| 27 | T102-STD-004D | T102-STD-004-CLAUSE-027 | ADR Consequences Scope | States consequences belong only in ADR bodies; no separate STD consequences. |
| 28 | T102-STD-004D | T102-STD-004-CLAUSE-028 | References & Provenance | Requires References and Provenance sections and governs what each must contain. |
| 29 | T102-STD-004D | T102-STD-004-CLAUSE-029 | Decision Promotion Workflow | Defines when to promote content into STDs/CLAUSEs and preserve traceability. |

### T102-STD-004A — Core Structure & Lifecycle

1) **T102-STD-004-CLAUSE-001 (Canonical File Structure)**

   Every combined standard-specification file MUST conform to the canonical structure defined by the subclauses below.

   * **T102-STD-004-CLAUSE-001A (Required sections and order)** — Every combined file MUST contain these sections in order: (1) `# <STD-ID> — <Title>`, (2) `## Specification`, (3) `## Decision Record`, (4) `## References`, (5) `## Provenance`. The `## Specification` section MAY contain `###`-level substandard headings when the parent STD uses substandard architecture per `T102-STD-004-CLAUSE-003`.

   * **T102-STD-004-CLAUSE-001B (Section semantics)** — `## Specification` contains normative `CLAUSE` items (enforceable language MUST follow the controlled vocabulary defined in `T102-STD-004-CLAUSE-008`). `## Decision Record` contains ADR bodies with informative rationale (current ADR listed first, superseded ADRs following per `T102-STD-004-CLAUSE-023`). `## References` and `## Provenance` are STD-level sections governing the entire file.

   * **T102-STD-004-CLAUSE-001C (Anchor metadata lines)** — Non-heading metadata lines (e.g., explicit anchor lines in the form `{#anchor}`) MAY appear immediately after the `# <STD-ID> — <Title>` header and immediately after each ADR header line; this does not count as an additional required section.

2) **T102-STD-004-CLAUSE-002 (Specification Index)**

   Every combined standard-specification file with more than 5 CLAUSEs SHOULD include a Specification Index conforming to the subclauses below.

   * **T102-STD-004-CLAUSE-002A (Schema)** — The Specification Index MUST use the schema: `| # | Substandard | CLAUSE ID | Title | Description |`, where `#` is a sequential display number, `Substandard` identifies the domain grouping, and `Description` is a 1-line normative summary (~10-15 words).

   * **T102-STD-004-CLAUSE-002B (Placement)** — The Specification Index MUST appear immediately after the `## Specification` heading and before the first substandard section heading (or before the first CLAUSE if no substandards are used).

   * **T102-STD-004-CLAUSE-002C (Granularity)** — The Specification Index MUST list main CLAUSEs only. Subclauses MUST NOT be individually indexed (they are discoverable by navigating to the parent CLAUSE).

3) **T102-STD-004-CLAUSE-003 (Substandard Architecture)**

   When a parent STD organizes its specification into substandards, the substandard architecture MUST conform to the subclauses below.

   * **T102-STD-004-CLAUSE-003A (Definition)** — A substandard is an internal domain grouping within a parent STD combined file. Substandards organize CLAUSEs into coherent thematic domains for navigability and modular evolution.

   * **T102-STD-004-CLAUSE-003B (ID format)** — Substandard IDs MUST follow the format `<STD-ID><CAPITAL_LETTER>` (e.g., `T102-STD-004A`). CLAUSEs within a substandard use the parent STD-ID in their CLAUSE-ID (e.g., `T102-STD-004-CLAUSE-001`), NOT the substandard ID.

   * **T102-STD-004-CLAUSE-003C (Universal membership rule)** — Every CLAUSE in a substandard-enabled STD MUST belong to exactly one substandard. No CLAUSEs MAY exist outside substandard boundaries.

   * **T102-STD-004-CLAUSE-003D (Registration)** — Substandards are internal structure. They MUST NOT be registered as separate rows in external registries (SPS STD Index, Concept STD Index). The parent STD maintains a single registry entry with description updated to reflect substandard domains.

   * **T102-STD-004-CLAUSE-003E (Rendering)** — Each substandard MUST be rendered as a `###`-level heading under `## Specification`, using the format: `### <Substandard-ID> — <Domain Title>` (e.g., `### T102-STD-004A — Core Structure & Lifecycle`).

   * **T102-STD-004-CLAUSE-003F (Non-token status)** — Substandard IDs (e.g., `T102-STD-004A`) and subclause IDs (e.g., `T102-STD-004-CLAUSE-001A`) are internal structural elements. They MUST NOT appear as standalone entries in registries, taxonomy tables, or governance indexes (including the STD-005 taxonomy, SPS STD Index, Concept STD Index, or Specification Index). They MAY be cited in text for navigational precision but carry no independent governance lifecycle and are NOT independent tokens.

4) **T102-STD-004-CLAUSE-004 (Specification Lifecycle Stages)**

   Specification content MUST progress through the lifecycle stages defined below.

   * **T102-STD-004-CLAUSE-004A (Stage definitions)** — The following lifecycle stages apply to specification content: `draft` (initial authoring; subject to change without formal review), `proposed` (submitted for review; normative language present but not yet binding), `accepted` (binding; normative language enforceable within declared scope), `amended` (accepted content modified via governed change process; prior version superseded), `deprecated` (no longer binding; retained for historical reference).

   * **T102-STD-004-CLAUSE-004B (Status enum format)** — Lifecycle stage values MUST be rendered as lowercase strings wrapped in backticks (e.g., `proposed`, `accepted`, `deprecated`).

5) **T102-STD-004-CLAUSE-005 (Authority Derivation & Conformance Coupling)**

   Derivative artifacts MUST maintain conformance with governing CLAUSEs per the subclauses below.

   * **T102-STD-004-CLAUSE-005A (Authority derivation chain)** — Authority flows downward: Specification (CLAUSEs) -> Guideline (informative) -> Template (derivative). A Guideline MUST cite the governing CLAUSE(s) it derives from. A Template MUST conform to structural requirements prescribed by governing CLAUSEs and Guideline.

   * **T102-STD-004-CLAUSE-005B (Conformance coupling rule)** — When a Specification CLAUSE is added, modified, or deprecated, all derivative artifacts (Guideline and Template) MUST be updated in the same changeset to maintain conformance.

   * **T102-STD-004-CLAUSE-005C (No normative leakage)** — Derivatives MUST NOT introduce normative rules that are not traceable to a governing CLAUSE.

   * **T102-STD-004-CLAUSE-005D (Derivative citation requirement)** — Each rule in a derivative artifact MUST include a citation to its governing CLAUSE(s) using the format `[per <CLAUSE-ID>]`.

6) **T102-STD-004-CLAUSE-006 (Anchor Stability)**

   Anchors MUST be lower-kebab derived from `<ID> + <Title>` and MUST satisfy the subclauses below.

   * **T102-STD-004-CLAUSE-006A (Normalization rules)** — Normalization MUST apply: spaces -> `-`; `&` -> `and`; strip punctuation; collapse repeated `-`. Result MUST be fully lowercase.

   * **T102-STD-004-CLAUSE-006B (Stability across moves/splits)** — Anchors MUST remain stable across file moves and splits.

   * **T102-STD-004-CLAUSE-006C (Title change migration)** — If Title changes, the old anchor MUST be kept unless an explicit migration is performed.

   * **T102-STD-004-CLAUSE-006D (Phase 1 stability contract)** — Combined-file names and canonical paths SHOULD remain stable after migration completion. Anchors extracted from Concept remain stable within their combined file.

7) **T102-STD-004-CLAUSE-007 (Automation & Linting Checks)**

   Authors SHOULD satisfy the automation and linting checks defined by the subclauses below.

   * **T102-STD-004-CLAUSE-007A (Required headings)** — Combined file contains `## Specification` and `## Decision Record` headings in that order.

   * **T102-STD-004-CLAUSE-007B (Nested ADR hygiene)** — Nested ADR body **Context** does not include a "Governed By" citation line.

   * **T102-STD-004-CLAUSE-007C (STD-level sections)** — Combined file contains STD-level `## References` and `## Provenance` headings.

   * **T102-STD-004-CLAUSE-007D (Index resolution)** — Every `Canonical Path` in an index resolves to an existing file under the designated standards directory per `T102-STD-004-CLAUSE-015`.

   * **T102-STD-004-CLAUSE-007E (Anchor derivation consistency)** — Anchors follow the derivation and stability rules defined in `T102-STD-004-CLAUSE-006`.

   * **T102-STD-004-CLAUSE-007F (Specification Index presence)** — Combined files with substandard architecture include a Specification Index per `T102-STD-004-CLAUSE-002`.

8) **T102-STD-004-CLAUSE-008 (Normative Vocabulary Guidance)**

   Normative vocabulary in specification sections MUST conform to `T102-CON-009 (Normative Keywords)` and the subclauses below.

   * **T102-STD-004-CLAUSE-008A (Normative keywords authority)** — Normative requirement keywords MUST be interpreted per `T102-CON-009 (Normative Keywords)`. Keywords carrying normative meaning MUST be written in UPPERCASE.

   * **T102-STD-004-CLAUSE-008B (Drafting consistency)** — Authors SHOULD use BCP 14 primary vocabulary (`MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, `MAY`) and SHOULD avoid RFC 2119 synonyms (`SHALL`, `REQUIRED`, `RECOMMENDED`, `OPTIONAL`) in new normative text for drafting consistency.

### T102-STD-004B — STD Registry & Governance

9) **T102-STD-004-CLAUSE-009 (STD Semantics & Scope)**

   The `STD` token type MUST conform to the semantics and scope constraints defined by the subclauses below.

   * **T102-STD-004-CLAUSE-009A (Category)** — `STD` is a normative `RID` token representing an enforceable standard.

   * **T102-STD-004-CLAUSE-009B (Creation scope)** — `STD` MUST only be created at Program (`P`), Initiative (`I`), Epic (`E`), and Feature (`F`) scopes.

   * **T102-STD-004-CLAUSE-009C (Reference scope)** — Artifacts at any scope MAY reference `STD`.

   * **T102-STD-004-CLAUSE-009D (Invalid usage)** — `STD` MUST NOT be used for informative guidance (`IG`) or integration notes (`INT`).

10) **T102-STD-004-CLAUSE-010 (STD Canonical Specification)**

   Every `STD` entry MUST declare its canonical specification status per the subclauses below.

   * **T102-STD-004-CLAUSE-010A (Canonical Path semantics)** — Every STD Index entry MUST include a `Canonical Path` value. If the STD has a dedicated combined standard-specification file, `Canonical Path` MUST be the full repo-relative path to that file under the designated standards directory (per `T102-STD-004-CLAUSE-015A`). If the STD is registry-only (no dedicated spec file), `Canonical Path` MUST be `—`.

   * **T102-STD-004-CLAUSE-010B (Incorporation by reference)** — When `Canonical Path` is populated, the specification content at that path is incorporated by reference into the STD. The STD remains the authoritative RID-level handle; the combined file's `## Specification` section is the canonical normative text.

   * **T102-STD-004-CLAUSE-010C (No rationale duplication)** — STD bodies MUST NOT contain alternatives analysis or lengthy trade-offs. These MUST be captured in ADRs.

11) **T102-STD-004-CLAUSE-011 (STD Precedence & Variance)**

   Precedence and variance for STD-governed artifacts MUST follow the subclauses below.

   * **T102-STD-004-CLAUSE-011A (Precedence authority)** — Precedence rules for standards inheritance MUST follow `T102-STD-005-CLAUSE-003 (Precedence & Overrides)` as the governing authority.

   * **T102-STD-004-CLAUSE-011B (Variance definition)** — A variance is an explicit deviation from an upstream standard. Variance MUST be documented via a Decision Record (ADR) at the deviating scope or in a designated variance register.

   * **T102-STD-004-CLAUSE-011C (STD/CLAUSE/ADR variance scope)** — Variance MAY apply to: a full STD, a specific CLAUSE within a STD, or a Decision Record requirement. The variance record MUST cite the overridden upstream reference(s) and MUST define the replacement behavior.

   * **T102-STD-004-CLAUSE-011D (Variance lifecycle)** — Variance records MUST use lifecycle stages per `T102-STD-004-CLAUSE-004` and MUST be reviewed at least once per release cycle or major migration event.

12) **T102-STD-004-CLAUSE-012 (STD Index Schema & Column Definitions)**

   STD index tables MUST conform to the schema and column definitions defined by the subclauses below.

   * **T102-STD-004-CLAUSE-012A (STD Index Schema)** — Each scope MUST maintain a `STD` index table using this schema: `| STD ID | Title | Status | Owner | Effective | Supersedes | Canonical Path | Verification | Governed By | Reference |`

   * **T102-STD-004-CLAUSE-012B (Column definitions)** — `STD ID` MUST follow `T102-STD-005-CLAUSE-001`. `Title` MUST be bold and follow title constraints. `Status` MUST use lowercase backtick-wrapped enums per `T102-STD-004-CLAUSE-004B`. `Canonical Path` MUST be a full repo-relative path to the combined standard-specification file under the designated standards directory (per `T102-STD-004-CLAUSE-015A`), or `—` if the STD is registry-only (no dedicated spec file). Semantics governed by `T102-STD-004-CLAUSE-010`. `Effective` MUST be an ISO-8601 date `YYYY-MM-DD` or `—` if not yet set. `Verification` MUST describe (a) mechanism, (b) what is checked, and (c) pass/fail evidence. `Governed By` MUST list the governing basis (meta-governance). `Reference` MUST contain ONLY `RID`-category IDs per `T102-STD-005-CLAUSE-002` and MUST NOT include `DRID`/`CLAUSE` IDs.

   * **T102-STD-004-CLAUSE-012C (Phase 1 index granularity)** — Phase 1 index granularity is the combined file as a whole (no anchor addressing required in indexes).

13) **T102-STD-004-CLAUSE-013 (STD Body Construction & Conciseness)**

   STD bodies MUST conform to the construction and conciseness requirements defined by the subclauses below.

   * **T102-STD-004-CLAUSE-013A (Normative statement discipline)** — Each STD CLAUSE MUST express a single primary normative obligation. Compound obligations MUST be split into subclauses.

   * **T102-STD-004-CLAUSE-013B (Conciseness target)** — STD clause text SHOULD be concise and avoid duplicating globally-governed semantics (e.g., ID construction) unless a local override is required.

   * **T102-STD-004-CLAUSE-013C (Avoid structural redundancy)** — STD bodies SHOULD avoid duplicating content already present in the Specification Index (CLAUSE-002) or in governing upstream standards.

14) **T102-STD-004-CLAUSE-014 (STD Drift Controls & Lifecycle Coherence)**

   STD content MUST remain aligned with canonical specifications and governing STDs per the subclauses below.

   * **T102-STD-004-CLAUSE-014A (Canonical specification is authoritative)** — Where a STD Index entry includes a `Canonical Path`, the specification content at that canonical path is authoritative.

   * **T102-STD-004-CLAUSE-014B (Derivatives conformance)** — Derivative artifacts MUST be updated with governing CLAUSE changes per `T102-STD-004-CLAUSE-005`.

   * **T102-STD-004-CLAUSE-014C (Supersession coherence)** — When a STD is superseded or deprecated, downstream indexes and references SHOULD be updated to reflect the new authority.

   * **T102-STD-004-CLAUSE-014D (Avoid cross-file drift)** — Where possible, authority SHOULD be consolidated into a single canonical specification rather than duplicated across multiple governance files.

15) **T102-STD-004-CLAUSE-015 (STD Placement & Directory Requirements)**

   Combined standard-specification files MUST be placed according to the subclauses below.

   * **T102-STD-004-CLAUSE-015A (Designated standards directory)** — Combined standard-specification files MUST live under the designated standards directory: `prompt/artifacts/tasks/<SID>/consultant/standards/`.

   * **T102-STD-004-CLAUSE-015B (Initiative-nonspecific directory rule)** — The designated directory MUST use `<SID>` placeholder in standards documentation and templates (not initiative-specific hardcoding), to ensure portability across initiatives.

   * **T102-STD-004-CLAUSE-015C (Canonical Path validity)** — `Canonical Path` values MUST be full repo-relative paths that resolve to an existing file under the designated standards directory.

16) **T102-STD-004-CLAUSE-016 (STD Status Management)**

   Status and supersession metadata for combined files MUST be maintained per the subclauses below.

   * **T102-STD-004-CLAUSE-016A (Status enums)** — STD status values MUST use lifecycle stage enums per `T102-STD-004-CLAUSE-004A` and MUST be rendered per `T102-STD-004-CLAUSE-004B`.

   * **T102-STD-004-CLAUSE-016B (Supersedes metadata)** — Supersession MUST be captured using the `Supersedes` field in the relevant index (STD Index or ADR Index). `Supersedes` MUST list superseded IDs or `—`.

   * **T102-STD-004-CLAUSE-016C (Deprecation semantics)** — Deprecated STDs remain referenceable for history, but MUST NOT be treated as binding authority. Index entries SHOULD cite the superseding STD.

17) **T102-STD-004-CLAUSE-017 (Migration Tolerance)**

   Migration from legacy governance identifiers MUST follow the subclauses below.

   * **T102-STD-004-CLAUSE-017A (Alias window tolerance)** — During a governed alias window, legacy references MAY appear for compatibility, but new or updated normative references MUST use the current identifier forms.

   * **T102-STD-004-CLAUSE-017B (One-time resequencing cost)** — When CLAUSE IDs are resequenced as a one-time migration, a controlled migration plan MUST exist and be executed to update key references.

   * **T102-STD-004-CLAUSE-017C (No silent drift)** — After a migration, stale references MUST be treated as defects and SHOULD be fixed in the earliest feasible changeset.

### T102-STD-004C — Specification Authoring

18) **T102-STD-004-CLAUSE-018 (CLAUSE Construction Requirements)**

   Specification CLAUSEs in combined standard-specification files MUST be constructed per the subclauses below.

   * **T102-STD-004-CLAUSE-018A (Normative reference)** — `CLAUSE` token semantics MUST follow `T102-STD-005-CLAUSE-005D (Specification Clause Semantics)`.

   * **T102-STD-004-CLAUSE-018B (Format)** — Within the `## Specification` section, each clause MUST be rendered as: `n) **<CLAUSE-ID> (<Title>)**`, where `<CLAUSE-ID>` conforms to `T102-STD-005-CLAUSE-005D`.

   * **T102-STD-004-CLAUSE-018C (Single-statement discipline)** — Each CLAUSE MUST be a single primary normative statement (avoid compound obligations where feasible). If additional detail is required, it SHOULD be provided as subclauses per `T102-STD-005-CLAUSE-005D`.

   * **T102-STD-004-CLAUSE-018D (Title conventions)** — CLAUSE Titles MUST follow the title conventions defined in `T102-STD-005-CLAUSE-001`.

   * **T102-STD-004-CLAUSE-018E (Non-duplication constraint)** — `T102-STD-004` MUST NOT redefine the syntax, scope validity, or semantic authority of `CLAUSE` IDs; those are defined in `T102-STD-005-CLAUSE-005D`.

19) **T102-STD-004-CLAUSE-019 (CLAUSE Ordering)**

   CLAUSE ordering within a combined standard-specification file MUST satisfy the subclauses below.

   * **T102-STD-004-CLAUSE-019A (Sequential numbering)** — `CLAUSE` IDs MUST be sequential within the parent STD in the order they appear across the Specification section (`001`, `002`, `003`, ...). When substandards are used, numbering is continuous across substandard boundaries. When adding a new CLAUSE to an existing substandard, the new CLAUSE MUST be appended after the last existing CLAUSE in that substandard's current block, using the next available global sequential number. Physical mid-substandard insertion that would require renumbering existing CLAUSE-IDs is PROHIBITED except during a governed release migration with a controlled migration plan per `T102-STD-004-CLAUSE-017`.

   * **T102-STD-004-CLAUSE-019B (Subclause adjacency)** — Subclauses MUST immediately follow their parent clause.

20) **T102-STD-004-CLAUSE-020 (Subclause Rendering)**

   Subclause rendering in combined standard-specification files MUST follow the subclauses below.

   * **T102-STD-004-CLAUSE-020A (Bold format requirement)** — Subclauses MUST be rendered as nested bullet items under the parent clause using the format: `* **<CLAUSE-ID> (<Title>)** — <normative statement>`. This follows the markdown construction defined in `T102-STD-005-CLAUSE-001`.

   * **T102-STD-004-CLAUSE-020B (Prohibited format)** — Subclauses MUST NOT use backtick-wrapped format (e.g., `` `T102-STD-004-CLAUSE-001A (Title)` ``). Backtick wrapping is reserved for inline code references, not for subclause rendering.

21) **T102-STD-004-CLAUSE-021 (Normative/Informative Boundary Hygiene)**

   Combined standard-specification files MUST enforce a clear boundary between normative and informative content per the subclauses below.

   * **T102-STD-004-CLAUSE-021A (Normative section authority)** — The `## Specification` section is the authoritative normative surface of a combined file. The `## Decision Record` section is informative rationale and MUST NOT create new obligations.

   * **T102-STD-004-CLAUSE-021B (Informative section keyword hygiene)** — Informative sections (including `## Decision Record`) MUST NOT use BCP 14 keywords in uppercase (`MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, `MAY`) to express requirements. If an informative section needs to refer to a normative requirement, it MUST do so by citing the governing CLAUSE reference and/or quoting the normative text as a quotation.

   * **T102-STD-004-CLAUSE-021C (Normative/informative labeling rule)** — If any non-Specification section contains normative requirements, that section MUST be explicitly labeled as normative and the governing CLAUSE(s) MUST be identified.

   * **T102-STD-004-CLAUSE-021D (Derivative boundary alignment)** — Any derivative artifact that describes boundary hygiene expectations MUST cite this CLAUSE and MUST NOT introduce additional boundary rules beyond what is governed here.

22) **T102-STD-004-CLAUSE-022 (Referencing & Non-Duplication)**

   CLAUSE referencing and non-duplication MUST follow the subclauses below.

   * **T102-STD-004-CLAUSE-022A (CLAUSE referencing)** — Other artifacts MAY reference specific Specification CLAUSEs using the formal format defined in `T102-STD-005-CLAUSE-004 (Reference Semantics)`.

   * **T102-STD-004-CLAUSE-022B (Non-duplication constraint)** — Combined standard-specification files MUST NOT redefine the syntax, scope validity, or semantic authority of `CLAUSE` IDs; those are defined in `T102-STD-005-CLAUSE-005D`.

### T102-STD-004D — Decision Record Authoring

23) **T102-STD-004-CLAUSE-023 (ADR Index Schema)**

   ADR index tables within combined standard-specification files MUST conform to the subclauses below.

   * **T102-STD-004-CLAUSE-023A (ADR Index Schema)** — The ADR Index MUST use the schema: `| ADR ID | Title | Status | Supersedes | Date |`.

   * **T102-STD-004-CLAUSE-023B (Column definitions)** — `ADR ID` MUST follow `T102-STD-005-CLAUSE-005F` construction format (`<STD-ID>-ADR-###`). `Title` MUST follow title conventions per `T102-STD-005-CLAUSE-001`. `Status` MUST use lowercase backtick-wrapped enums per `T102-STD-004-CLAUSE-004B` (e.g., `accepted`, `superseded`). `Supersedes` MUST list superseded ADR IDs or `—`. `Date` MUST be ISO-8601 date `YYYY-MM-DD`.

   * **T102-STD-004-CLAUSE-023C (Current-first ordering)** — ADR bodies in the `## Decision Record` section MUST be ordered with the current (most recent `accepted`) ADR first, followed by superseded ADRs in reverse chronological order.

   * **T102-STD-004-CLAUSE-023D (Multiple ADRs in-file)** — Combined files MAY contain multiple ADR bodies (current + superseded). Superseded ADR bodies are retained for audit trail purposes. Only one ADR MAY have `accepted` status at any time; all others MUST be `superseded`.

24) **T102-STD-004-CLAUSE-024 (ADR Entry Creation Workflow)**

   To create a new combined standard-specification file and its corresponding index entry, authors MUST satisfy the subclauses below.

   * **T102-STD-004-CLAUSE-024A (File naming convention)** — Combined standard-specification filenames MUST follow `standard_<STD-ID>_<title-slug>.md` where `<title-slug>` is lowercase, spaces -> `-`, non-alphanumeric characters removed/replaced with `-`, and repeated `-` collapsed.

   * **T102-STD-004-CLAUSE-024B (Create index row)** — Authors MUST add a new row to the appropriate STD index table using the schema per `T102-STD-004-CLAUSE-012`.

   * **T102-STD-004-CLAUSE-024C (Assign ID)** — Authors MUST assign the next sequential STD ID for that scope.

   * **T102-STD-004-CLAUSE-024D (Create combined file)** — Authors MUST create a combined standard-specification file at the canonical path under the designated standards directory (per `T102-STD-004-CLAUSE-015A`) using the standard-specification template, applying CLAUSE entries under `## Specification` and DR body structure under `## Decision Record` per `T102-STD-004-CLAUSE-025`.

   * **T102-STD-004-CLAUSE-024E (References conformance)** — Authors MUST ensure References follow `T102-STD-005-CLAUSE-004 (Reference Semantics)`.

   * **T102-STD-004-CLAUSE-024F (Canonical Path population)** — Authors MUST populate the Canonical Path column (where applicable) in the index row with the full repo-relative path to the combined file.

25) **T102-STD-004-CLAUSE-025 (DR Body Template)**

   Nested ADR bodies in combined standard-specification files MUST conform to the subclauses below.

   * **T102-STD-004-CLAUSE-025A (Header format)** — Nested ADR header MUST be rendered as: `* **<STD-ID>-ADR-### (<Title>)** {#<anchor>}`.

   * **T102-STD-004-CLAUSE-025B (Required subheadings)** — Nested ADR body MUST include these subheadings: **Context**, **Decision**, **Alternatives**, **Consequences**, **Traceability**.

   * **T102-STD-004-CLAUSE-025C (Body formatting rules)** — Main bold headings (e.g., `* **Context**`) MUST be preceded by two newlines. Content MUST start on a new line and be indented under the heading with no space in between.

   * **T102-STD-004-CLAUSE-025D (Context requirements)** — Context MUST describe why the decision is needed and the gap it resolves.

   * **T102-STD-004-CLAUSE-025E (Decision requirements)** — Decision MUST state what is adopted/changed and who owns it.

   * **T102-STD-004-CLAUSE-025F (Alternatives requirements)** — Alternatives MUST be a bulleted list of options considered with clear rejection rationales.

   * **T102-STD-004-CLAUSE-025G (Consequences requirements)** — Consequences MUST be expressed using `(+)`, `(±)`, and `(-)` prefix bullets.

   * **T102-STD-004-CLAUSE-025H (STD-level boundary)** — In combined standard-specification files, the DR body lives under `## Decision Record`. References and Provenance are STD-level sections per `T102-STD-004-CLAUSE-028`.

   * **T102-STD-004-CLAUSE-025I (Traceability requirements)** — Each nested ADR body MUST include a **Traceability** subheading as a non-normative surface for timeline references. Timeline references MUST be listed as bullet items containing fully-qualified IDs (e.g., `T102-PH001-ST001-AC009.1-TK003`). Traceability MUST NOT contain lazy shorthand references (e.g., `AC009.1-TK003`, `SES###`, `SES###-DEC###`).

26) **T102-STD-004-CLAUSE-026 (Cross-Artifact Linking Patterns)**

   Combined standard-specification files MUST satisfy the cross-artifact linking patterns defined by subclauses below:

   * **T102-STD-004-CLAUSE-026A (STD internal DR pattern)** — A combined standard-specification file MUST contain its decision record internally under `## Decision Record` using the nested ADR format from `T102-STD-004-CLAUSE-025`.

   * **T102-STD-004-CLAUSE-026B (Decision Record context pattern)** — The nested ADR **Context** SHOULD state the motivating problem in narrative form and SHOULD NOT include timeline IDs. Timeline IDs belong under **Traceability** per `T102-STD-004-CLAUSE-025I`.

   * **T102-STD-004-CLAUSE-026C (Context/References boundary)** — The nested ADR **Context** SHOULD NOT contain a "Governed By" citation line. Governing references belong in `## References` per `T102-STD-004-CLAUSE-028`.

   * **T102-STD-004-CLAUSE-026D (Index Link Pattern)** — Index artifacts (SPS/Concept) SHOULD reference combined files via `Canonical Path` and MUST NOT duplicate the full normative specification body.

27) **T102-STD-004-CLAUSE-027 (ADR Consequences Scope)**

   Consequences sections in nested ADR bodies SHOULD cover the scope defined by CLAUSE-027A.

   * **T102-STD-004-CLAUSE-027A (ADR-only consequences)** — Consequences apply to the Decision Record scope only. STDs and CLAUSEs MUST NOT include separate "STD Consequences" sections; consequences belong in ADR bodies under `## Decision Record`.

28) **T102-STD-004-CLAUSE-028 (References & Provenance)**

   Combined files MUST satisfy the References and Provenance requirements defined by the subclauses below.

   * **T102-STD-004-CLAUSE-028A (References requirements)** — Every combined file MUST include a `## References` section listing governing standards, guidance, and quality gates as `RID`-category references per `T102-STD-005-CLAUSE-004`.

   * **T102-STD-004-CLAUSE-028B (Provenance requirements)** — Every combined file MUST include a `## Provenance` section listing the originating proposal(s), research, and/or decision sessions that produced the specification content.

29) **T102-STD-004-CLAUSE-029 (Decision Promotion Workflow)**

   Promotion of decision content into Standards SHOULD follow the subclauses below.

   * **T102-STD-004-CLAUSE-029A (STD promotion criteria)** — Authors SHOULD promote stable, cross-cutting, or long-lived patterns into formal `STD` records when: (a) the pattern affects multiple artifacts or features, or (b) the pattern requires explicit governance (ownership, status, supersedes) beyond implementation detail. When promoted, the `STD` MUST contain a nested ADR for rationale per `T102-STD-004-CLAUSE-025`.

   * **T102-STD-004-CLAUSE-029B (CLAUSE promotion)** — When a normative obligation in a combined file warrants addressable precision, it SHOULD be formalized as a named CLAUSE (or subclause) per `T102-STD-004-CLAUSE-018`.

   * **T102-STD-004-CLAUSE-029C (Traceability)** — Specifications SHOULD reference governing research and guidance in **Provenance** and **References** (per `T102-STD-004-CLAUSE-028`), rather than duplicating detailed patterns. Token-specific promotion workflows for `RES` and `IG` tokens are governed by `T102-STD-005`.

## Decision Record

### ADR Index
| ADR ID | Title | Status | Supersedes | Date |
|:--|:--|:--|:--|:--|
| T102-STD-004-ADR-002 | Combined Authoring & Governance Standard | `accepted` | ADR-001 | 2026-02-15 |
| T102-STD-004-ADR-001 | Specification Standard & Guideline | `superseded` | — | 2026-02-08 |

* **T102-STD-004-ADR-002 (Combined Authoring & Governance Standard)** {#t102-std-004-adr-002-combined-authoring-and-governance-standard}

  * **Context**
    T102-STD-004’s governance model evolved through self-compliance auditing, Client QA, and research benchmarking. The combined-file architecture and fine-grained subclause discipline were validated while drift risk across split governance surfaces was identified as a practical operational concern for agentic LLM authoring. The Client therefore chose to consolidate governance by merging STD-009 into STD-004, adopting a four-substandard architecture, retaining multiple in-file ADR bodies (current-first), and adding an append-only sequencing constraint to reduce future renumbering blast radius. Industry benchmarking in `T102-RES-007` informed the direction but did not override the Client’s drift-control decision.

  * **Decision**
    - Merge `T102-STD-009` into `T102-STD-004` and treat `T102-STD-009` as deprecated in dependent indexes (handled outside this sub-activity).
    - Organize `T102-STD-004` into four substandards: `T102-STD-004A`, `T102-STD-004B`, `T102-STD-004C`, `T102-STD-004D`.
    - Resequence and maintain a single global `CLAUSE` numbering sequence across all substandards (with append-only growth constraint in `T102-STD-004-CLAUSE-019A`).
    - Store multiple ADR bodies in-file under `## Decision Record`, ordered current-first per `T102-STD-004-CLAUSE-023C`, retaining superseded ADRs for audit trail.
    - Use `Canonical Path` (not `Adopts`) in the STD Index schema, and remove the redundant `Authority STD` column from the ADR Index schema.

  * **Alternatives**
    - Keep `T102-STD-004` and `T102-STD-009` separate with interface contracts — rejected due to persistent drift and context loss for agentic LLM authoring.
    - Keep flat `CLAUSE` numbering with informative domain headers — rejected because headers do not enforce membership and leave navigability partially unresolved.
    - Use numeric range reservation per substandard — rejected due to upfront overhead and per-STD range decisions at scale.

  * **Consequences**
    (+) Consolidated governance surface reduces drift risk and improves reviewability for agentic LLM authoring.
    (+) Substandard architecture improves navigability while preserving a single authoritative `CLAUSE` namespace.
    (+) Multiple ADR bodies in-file preserve audit trail and support a future extraction workflow.
    (±) Resequencing and schema changes have a non-trivial blast radius that must be managed through gated rollouts.
    (-) One-time reference breakage occurs from full `CLAUSE` resequencing and requires controlled migration planning.

  * **Traceability**
    - `T102-PH001-ST001-AC008`
    - `T102-PH001-ST001-AC008-SES001-DEC001`
    - `T102-PH001-ST001-AC009-GATE-001`
    - `T102-PH001-ST001-AC009-SES002-DEC001`
    - `T102-PH001-ST001-AC009-SES002-DEC002`
    - `T102-PH001-ST001-AC009-SES002-DEC004`
    - `T102-PH001-ST001-AC009-SES003-DEC002`
    - `T102-PH001-ST001-AC009-SES003-DEC007`
    - `T102-PH001-ST001-AC009.1-TK003`
    - `T102-PH001-ST001-AC009-INT-003`
    - `T102-PH001-ST001-AC009-INT-006`

* **T102-STD-004-ADR-001 (Specification Standard & Guideline)** {#t102-std-004-adr-001-specification-standard-and-guideline}

  * **Context**
    The current governance surface is split between index artifacts and combined files, which creates a dual-surface authoring pattern that drifts over time and weakens consistency targets tied to `T102-QG-001`. A single canonical combined-file structure is needed so normative clauses and decision rationale remain co-located, machine-checkable, and reviewable.

  * **Decision**
    Adopt the standard-specification combined-file model with `## Specification` first and a nested informative ADR under `## Decision Record`. This file (`T102-STD-004`) is the golden exemplar defining clause structure, linkage patterns, and lifecycle controls for decision-record standards.

  * **Alternatives**
    - Keep ADR-first combined structure and external adoption links — rejected due to ongoing dual-surface drift.
    - Split rationale into standalone ADR files for all standards — rejected for Phase 1 due to migration overhead and coordination risk.

  * **Consequences**
    (+) Clear authority boundary: Specification is normative; nested ADR is informative.
    (+) Single-file review surface improves consistency and auditability.
    (+) Enables deterministic migration and linting patterns for downstream rollout.
    (±) Requires coordinated updates to indexes, templates, and references in subsequent tasks.
    (-) Legacy ADR-based references require temporary alias handling during transition.

  * **Traceability**
    - `T102-PH001-ST001-AC005`
 
## References

`T102-QG-001 (Client Readability)`,
`T102-CON-009 (Controlled Vocabulary for Normative Language)`,
`T102-STD-005 (ID Specification & Rules)`,
`T102-IG-007 (ID Standard)`,
`T102-IG-008 (Decision Logging)`,
`T102-IG-009 (Traceability Framework)`,
`T102-STD-001 (Consultancy Operating Model Standard)`,
`T102-STD-009 (Governance Standards Specification)`

## Provenance

- `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_PH001-ST001-AC009_std-004-redesign.md`
- `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_PH001-ST001-AC009_1_tk003_std-004-clause-019-sequencing-amendment.md`

| Superseded By | `P-STD-001` (Program Governance Standard) |
| Supersession Date | 2026-02-20 |
| Promotion Decision | `P-STD-001-ADR-003` |
