---
artifact_type: 'STANDARD'
initiative_id: 'P'
initiative_code: 'PROGRAM'
standard_id: 'P-STD-001'
version: '1.2.0'
date: '2026-03-26'
status: 'accepted'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
approval_date: '2026-02-22'
effective_date: '2026-02-22'
supersedes: 'T102-STD-004'
---

# P-STD-001 — Program Governance Standard {#p-std-001-program-governance-standard}

## Specification

### Specification Index
| # | Substandard | CLAUSE ID | Title | Description |
|:--|:--|:--|:--|:--|
| 1 | P-STD-001A | P-STD-001-CLAUSE-001 | Canonical File Structure | Defines required section order and semantics for combined standard-specification files. |
| 2 | P-STD-001A | P-STD-001-CLAUSE-002 | Specification Index | Requires a navigational index for standards with more than five clauses. |
| 3 | P-STD-001A | P-STD-001-CLAUSE-003 | Substandard Architecture | Defines substandard structure, membership, rendering, and non-token registration rules. |
| 4 | P-STD-001A | P-STD-001-CLAUSE-004 | Specification Lifecycle Stages | Defines lifecycle stages and formatting for specification status values. |
| 5 | P-STD-001A | P-STD-001-CLAUSE-005 | Authority Derivation & Conformance Coupling | Defines authority chain and conformance coupling for guideline/template derivatives. |
| 6 | P-STD-001A | P-STD-001-CLAUSE-006 | Anchor Stability | Defines anchor normalization, stability rules, and migration handling for title changes. |
| 7 | P-STD-001A | P-STD-001-CLAUSE-007 | Automation & Linting Checks | Defines recommended lint checks for required headings, indexes, and anchor rules. |
| 8 | P-STD-001A | P-STD-001-CLAUSE-008 | Normative Vocabulary Guidance | Defines the program-scope handling of normative drafting vocabulary and controlled keyword usage. |
| 9 | P-STD-001A | P-STD-001-CLAUSE-031 | Standard-File YAML Frontmatter | Defines the governed current-state metadata schema for combined standard files. |
| 10 | P-STD-001A | P-STD-001-CLAUSE-032 | Metadata Authority & Overlap Control | Splits machine-readable current-state metadata from historical provenance metadata. |
| 11 | P-STD-001B | P-STD-001-CLAUSE-009 | STD Semantics & Scope | Defines STD token semantics, allowed scopes, and invalid usages. |
| 12 | P-STD-001B | P-STD-001-CLAUSE-010 | STD Canonical Specification | Defines Canonical Path semantics and incorporation-by-reference for STD specifications. |
| 13 | P-STD-001B | P-STD-001-CLAUSE-011 | STD Precedence & Variance | Defines precedence authority and how variances are documented and reviewed. |
| 14 | P-STD-001B | P-STD-001-CLAUSE-012 | STD Index Schema & Column Definitions | Defines STD Index schema and column semantics, including Canonical Path and Reference. |
| 15 | P-STD-001B | P-STD-001-CLAUSE-013 | STD Body Construction & Conciseness | Defines single-obligation discipline and conciseness requirements for STD bodies. |
| 16 | P-STD-001B | P-STD-001-CLAUSE-014 | STD Drift Controls & Lifecycle Coherence | Defines drift controls to keep specifications aligned with canonical sources. |
| 17 | P-STD-001B | P-STD-001-CLAUSE-015 | STD Placement & Directory Requirements | Defines standards directory placement rules and Canonical Path validity requirements. |
| 18 | P-STD-001B | P-STD-001-CLAUSE-016 | STD Status Management | Defines status enums and supersession metadata handling for STDs and combined files. |
| 19 | P-STD-001B | P-STD-001-CLAUSE-017 | Migration Tolerance | Defines alias windows and requirements for one-time resequencing migrations. |
| 20 | P-STD-001B | P-STD-001-CLAUSE-030 | Standard Promotion & Demotion Lifecycle | Defines governance lifecycle for standard scope promotion and demotion. |
| 21 | P-STD-001B | P-STD-001-CLAUSE-033 | Derivative Metadata, Scope & Delegation | Defines lightweight metadata, precedence, and delegation rules for derivative instruction surfaces. |
| 22 | P-STD-001C | P-STD-001-CLAUSE-018 | CLAUSE Construction Requirements | Defines how to author clauses: format, titles, subclauses, and references. |
| 23 | P-STD-001C | P-STD-001-CLAUSE-019 | CLAUSE Ordering | Requires sequential clause numbering and adjacency of subclauses. |
| 24 | P-STD-001C | P-STD-001-CLAUSE-020 | Subclause Rendering | Requires bold subclause rendering and prohibits backtick-wrapped subclause format. |
| 25 | P-STD-001C | P-STD-001-CLAUSE-021 | Normative/Informative Boundary Hygiene | Defines rules preventing normative leakage into informative decision record sections. |
| 26 | P-STD-001C | P-STD-001-CLAUSE-022 | Referencing & Non-Duplication | Defines referencing patterns and prohibits redefining global CLAUSE semantics. |
| 27 | P-STD-001D | P-STD-001-CLAUSE-023 | ADR Index Schema | Defines ADR Index schema, ordering, and multiple ADR retention rules. |
| 28 | P-STD-001D | P-STD-001-CLAUSE-024 | ADR Entry Creation Workflow | Defines workflow for creating combined files and corresponding STD index entries. |
| 29 | P-STD-001D | P-STD-001-CLAUSE-025 | DR Body Template | Defines ADR body format, required subheadings, and per-section content requirements. |
| 30 | P-STD-001D | P-STD-001-CLAUSE-026 | Cross-Artifact Linking Patterns | Defines how combined files and indexes link without duplicating canonical specification. |
| 31 | P-STD-001D | P-STD-001-CLAUSE-027 | ADR Consequences Scope | States consequences belong only in ADR bodies; no separate STD consequences. |
| 32 | P-STD-001D | P-STD-001-CLAUSE-028 | References & Provenance | Requires References and Provenance sections and governs what each must contain. |
| 33 | P-STD-001D | P-STD-001-CLAUSE-029 | Decision Promotion Workflow | Defines when to promote content into STDs/CLAUSEs and preserve traceability. |
| 34 | P-STD-001D | P-STD-001-CLAUSE-034 | Version Tracking & Amendment History | Defines semver use and amendment-history retention for governed standard files. |
| 35 | P-STD-001D | P-STD-001-CLAUSE-035 | References Taxonomy & Schema | Defines the required references subsection taxonomy and row schema. |
| 36 | P-STD-001D | P-STD-001-CLAUSE-036 | Provenance Taxonomy & Extensions | Defines the minimum provenance subsection taxonomy and extension controls. |

### P-STD-001A — Core Structure & Lifecycle

1) **P-STD-001-CLAUSE-001 (Canonical File Structure)**

   Every combined standard-specification file MUST conform to the canonical structure defined by the subclauses below.

   * **P-STD-001-CLAUSE-001A (Required sections and order)** — Every combined file MUST contain these sections in order: (1) `# <STD-ID> — <Title>`, (2) `## Specification`, (3) `## Decision Record`, (4) `## References`, (5) `## Provenance`. The `## Specification` section MAY contain `###`-level substandard headings when the parent STD uses substandard architecture per `P-STD-001-CLAUSE-003`.

   * **P-STD-001-CLAUSE-001B (Section semantics)** — `## Specification` contains normative `CLAUSE` items (enforceable language MUST follow the controlled vocabulary defined in `P-STD-001-CLAUSE-008`). `## Decision Record` contains ADR bodies with informative rationale (current ADR listed first, superseded ADRs following per `P-STD-001-CLAUSE-023`). `## References` and `## Provenance` are STD-level sections governing the entire file.

   * **P-STD-001-CLAUSE-001C (Frontmatter and anchor metadata lines)** — Governed YAML frontmatter MAY appear immediately before the `# <STD-ID> — <Title>` header per `P-STD-001-CLAUSE-031`. Non-heading metadata lines (e.g., explicit anchor lines in the form `{#anchor}`) MAY appear immediately after the title header and immediately after each ADR header line; neither pattern counts as an additional required section.

2) **P-STD-001-CLAUSE-002 (Specification Index)**

   Every combined standard-specification file with more than 5 CLAUSEs SHOULD include a Specification Index conforming to the subclauses below.

   * **P-STD-001-CLAUSE-002A (Schema)** — The Specification Index MUST use the schema: `| # | Substandard | CLAUSE ID | Title | Description |`, where `#` is a sequential display number, `Substandard` identifies the domain grouping, and `Description` is a 1-line normative summary (~10-15 words).

   * **P-STD-001-CLAUSE-002B (Placement)** — The Specification Index MUST appear immediately after the `## Specification` heading and before the first substandard section heading (or before the first CLAUSE if no substandards are used).

   * **P-STD-001-CLAUSE-002C (Granularity)** — The Specification Index MUST list main CLAUSEs only. Subclauses MUST NOT be individually indexed (they are discoverable by navigating to the parent CLAUSE).

3) **P-STD-001-CLAUSE-003 (Substandard Architecture)**

   When a parent STD organizes its specification into substandards, the substandard architecture MUST conform to the subclauses below.

   * **P-STD-001-CLAUSE-003A (Definition)** — A substandard is an internal domain grouping within a parent STD combined file. Substandards organize CLAUSEs into coherent thematic domains for navigability and modular evolution.

   * **P-STD-001-CLAUSE-003B (ID format)** — Substandard IDs MUST follow the format `<STD-ID><CAPITAL_LETTER>` (e.g., `P-STD-001A`). CLAUSEs within a substandard use the parent STD-ID in their CLAUSE-ID (e.g., `P-STD-001-CLAUSE-001`), NOT the substandard ID.

   * **P-STD-001-CLAUSE-003C (Universal membership rule)** — Every CLAUSE in a substandard-enabled STD MUST belong to exactly one substandard. No CLAUSEs MAY exist outside substandard boundaries.

   * **P-STD-001-CLAUSE-003D (Registration)** — Substandards are internal structure. They MUST NOT be registered as separate rows in external registries (SPS STD Index, Concept STD Index). The parent STD maintains a single registry entry with description updated to reflect substandard domains.

   * **P-STD-001-CLAUSE-003E (Rendering)** — Each substandard MUST be rendered as a `###`-level heading under `## Specification`, using the format: `### <Substandard-ID> — <Domain Title>` (e.g., `### P-STD-001A — Core Structure & Lifecycle`).

   * **P-STD-001-CLAUSE-003F (Non-token status)** — Substandard IDs (e.g., `P-STD-001A`) and subclause IDs (e.g., `P-STD-001-CLAUSE-001A`) are internal structural elements. They MUST NOT appear as standalone entries in registries, taxonomy tables, or governance indexes (including the P-STD-005 taxonomy, SPS STD Index, Concept STD Index, or Specification Index). They MAY be cited in text for navigational precision but carry no independent governance lifecycle and are NOT independent tokens.

4) **P-STD-001-CLAUSE-004 (Specification Lifecycle Stages)**

   Specification content MUST progress through the lifecycle stages defined below.

   * **P-STD-001-CLAUSE-004A (Stage definitions)** — The following lifecycle stages apply to specification content: `draft` (initial authoring; subject to change without formal review), `proposed` (submitted for review; normative language present but not yet binding), `accepted` (binding; normative language enforceable within declared scope), `amended` (accepted content modified via governed change process; prior version superseded), `deprecated` (no longer binding; retained for historical reference).

   * **P-STD-001-CLAUSE-004B (Status enum format)** — Lifecycle stage values MUST be rendered as lowercase strings wrapped in backticks (e.g., `proposed`, `accepted`, `deprecated`).

5) **P-STD-001-CLAUSE-005 (Authority Derivation & Conformance Coupling)**

   Derivative artifacts MUST maintain conformance with governing CLAUSEs per the subclauses below.

   * **P-STD-001-CLAUSE-005A (Authority derivation chain)** — Authority flows downward: Specification (CLAUSEs) -> Guideline (informative) -> Template (derivative). A Guideline MUST cite the governing CLAUSE(s) it derives from. A Template MUST conform to structural requirements prescribed by governing CLAUSEs and Guideline.

   * **P-STD-001-CLAUSE-005B (Conformance coupling rule)** — When a Specification CLAUSE is added, modified, or deprecated, all derivative artifacts (Guideline and Template) MUST be updated in the same changeset to maintain conformance.

   * **P-STD-001-CLAUSE-005C (No normative leakage)** — Derivatives MUST NOT introduce normative rules that are not traceable to a governing CLAUSE.

   * **P-STD-001-CLAUSE-005D (Derivative citation requirement)** — Each rule in a derivative artifact MUST include a citation to its governing CLAUSE(s) using the format `<CLAUSE-ID>`.

6) **P-STD-001-CLAUSE-006 (Anchor Stability)**

   Anchors MUST be lower-kebab derived from `<ID> + <Title>` and MUST satisfy the subclauses below.

   * **P-STD-001-CLAUSE-006A (Normalization rules)** — Normalization MUST apply: spaces -> `-`; `&` -> `and`; strip punctuation; collapse repeated `-`. Result MUST be fully lowercase.

   * **P-STD-001-CLAUSE-006B (Stability across moves/splits)** — Anchors MUST remain stable across file moves and splits.

   * **P-STD-001-CLAUSE-006C (Title change migration)** — If Title changes, the old anchor MUST be kept unless an explicit migration is performed.

   * **P-STD-001-CLAUSE-006D (Phase 1 stability contract)** — Combined-file names and canonical paths SHOULD remain stable after migration completion. Anchors extracted from Concept remain stable within their combined file.

7) **P-STD-001-CLAUSE-007 (Automation & Linting Checks)**

   Authors SHOULD satisfy the automation and linting checks defined by the subclauses below.

   * **P-STD-001-CLAUSE-007A (Required headings)** — Combined file contains `## Specification` and `## Decision Record` headings in that order.

   * **P-STD-001-CLAUSE-007B (Nested ADR hygiene)** — Nested ADR body **Context** does not include a "Governed By" citation line.

   * **P-STD-001-CLAUSE-007C (STD-level sections)** — Combined file contains STD-level `## References` and `## Provenance` headings.

   * **P-STD-001-CLAUSE-007D (Index resolution)** — Every `Canonical Path` in an index resolves to an existing file under the designated standards directory per `P-STD-001-CLAUSE-015`.

   * **P-STD-001-CLAUSE-007E (Anchor derivation consistency)** — Anchors follow the derivation and stability rules defined in `P-STD-001-CLAUSE-006`.

   * **P-STD-001-CLAUSE-007F (Specification Index presence)** — Combined files with substandard architecture include a Specification Index per `P-STD-001-CLAUSE-002`.

   * **P-STD-001-CLAUSE-007G (Metadata consistency checks)** — Authors SHOULD verify that governed frontmatter fields, `## References`, and `## Provenance` conform to the structure and authority rules defined in `P-STD-001-CLAUSE-031` through `P-STD-001-CLAUSE-036`.

8) **P-STD-001-CLAUSE-008 (Normative Vocabulary Guidance)**

   Normative vocabulary in specification sections MUST follow the program-scope drafting contract defined by the subclauses below.

   * **P-STD-001-CLAUSE-008A (Program drafting vocabulary authority)** — Program standards MUST use the BCP 14 primary vocabulary set (`MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, `MAY`) as the authoritative drafting keywords for normative requirement statements. Keywords carrying normative meaning MUST be written in UPPERCASE.

   * **P-STD-001-CLAUSE-008B (Legacy equivalence note)** — Lower-scope vocabulary references such as `T102-CON-009` MAY be cited only as informative lineage context during migration or alias-window handling. They MUST NOT be presented as the unqualified steady-state normative authority for program-scope specification drafting.

   * **P-STD-001-CLAUSE-008C (Drafting consistency)** — Authors SHOULD avoid RFC 2119 synonym forms (`SHALL`, `REQUIRED`, `RECOMMENDED`, `OPTIONAL`) in new normative text unless a governing upstream adoption explicitly requires them.

9) **P-STD-001-CLAUSE-031 (Standard-File YAML Frontmatter)**

   Combined standard-specification files MUST declare current-state metadata in YAML frontmatter per the subclauses below.

   * **P-STD-001-CLAUSE-031A (Frontmatter placement)** — A governed YAML frontmatter block MUST appear immediately before the title heading of every combined standard-specification file.

   * **P-STD-001-CLAUSE-031B (Required fields)** — Standard-file frontmatter MUST include `artifact_type`, `initiative_id`, `initiative_code`, `standard_id`, `version`, `date`, `status`, `author`, and `decision_owner_role`.

   * **P-STD-001-CLAUSE-031C (Lifecycle-conditional fields)** — `approval_date` and `effective_date` MUST be present when the current lifecycle state makes them meaningful. `supersedes`, `superseded_by`, and `deprecation_date` MUST be present when the current lifecycle chain makes them meaningful.

   * **P-STD-001-CLAUSE-031D (Value constraints)** — `standard_id` MUST match the in-body standard identifier. `version` MUST follow the semver contract governed by `P-STD-001-CLAUSE-034`. `date` MUST be an ISO-8601 date in `YYYY-MM-DD` format. `status` MUST align to lifecycle values governed by `P-STD-001-CLAUSE-004`.

   * **P-STD-001-CLAUSE-031E (Scope boundary)** — Standard-file frontmatter MUST remain a compact current-state metadata layer. Historical notes, full process chronologies, and amendment narratives MUST NOT be stored in frontmatter.

10) **P-STD-001-CLAUSE-032 (Metadata Authority & Overlap Control)**

   Combined standard-specification files MUST keep machine-readable current-state metadata distinct from historical and lineage metadata per the subclauses below.

   * **P-STD-001-CLAUSE-032A (Current-state authority)** — YAML frontmatter is the authoritative location for current-state metadata values such as the active `version`, `date`, `status`, and lifecycle-chain fields governed by `P-STD-001-CLAUSE-031`.

   * **P-STD-001-CLAUSE-032B (History and lineage authority)** — `## Provenance` is the authoritative location for historical state transitions, lineage pointers, amendment summaries, and input-source traceability.

   * **P-STD-001-CLAUSE-032C (Overlap consistency rule)** — If a conceptual field appears in both frontmatter and `## Provenance`, the frontmatter value controls current state and the Provenance content MUST be written so it does not contradict that value.

   * **P-STD-001-CLAUSE-032D (No history in frontmatter)** — Amendment-history entries, seed-input inventories, and gate/process dossier detail MUST remain outside frontmatter and be expressed in `## Provenance` or in external process artifacts.

### P-STD-001B — STD Registry & Governance

9) **P-STD-001-CLAUSE-009 (STD Semantics & Scope)**

   The `STD` token type MUST conform to the semantics and scope constraints defined by the subclauses below.

   * **P-STD-001-CLAUSE-009A (Category)** — `STD` is a normative `RID` token representing an enforceable standard.

   * **P-STD-001-CLAUSE-009B (Creation scope)** — `STD` MUST only be created at Program (`P`), Initiative (`I`), Epic (`E`), and Feature (`F`) scopes.

   * **P-STD-001-CLAUSE-009C (Reference scope)** — Artifacts at any scope MAY reference `STD`.

   * **P-STD-001-CLAUSE-009D (Invalid usage)** — `STD` MUST NOT be used for informative guidance (`IG`) or integration notes (`INT`).

10) **P-STD-001-CLAUSE-010 (STD Canonical Specification)**

   Every `STD` entry MUST declare its canonical specification status per the subclauses below.

   * **P-STD-001-CLAUSE-010A (Canonical Path semantics)** — Every STD Index entry MUST include a `Canonical Path` value. If the STD has a dedicated combined standard-specification file, `Canonical Path` MUST be the full repo-relative path to that file under the designated standards directory (per `P-STD-001-CLAUSE-015A`). If the STD is registry-only (no dedicated spec file), `Canonical Path` MUST be `—`.

   * **P-STD-001-CLAUSE-010B (Incorporation by reference)** — When `Canonical Path` is populated, the specification content at that path is incorporated by reference into the STD. The STD remains the authoritative RID-level handle; the combined file's `## Specification` section is the canonical normative text.

   * **P-STD-001-CLAUSE-010C (No rationale duplication)** — STD bodies MUST NOT contain alternatives analysis or lengthy trade-offs. These MUST be captured in ADRs.

11) **P-STD-001-CLAUSE-011 (STD Precedence & Variance)**

   Precedence and variance for STD-governed artifacts MUST follow the subclauses below.

   * **P-STD-001-CLAUSE-011A (Precedence authority)** — Precedence rules for standards inheritance MUST follow `P-STD-005-CLAUSE-003 (Precedence & Overrides)` as the governing authority.

   * **P-STD-001-CLAUSE-011B (Variance definition)** — A variance is an explicit deviation from an upstream standard. Variance MUST be documented via a Decision Record (ADR) at the deviating scope or in a designated variance register.

   * **P-STD-001-CLAUSE-011C (STD/CLAUSE/ADR variance scope)** — Variance MAY apply to: a full STD, a specific CLAUSE within a STD, or a Decision Record requirement. The variance record MUST cite the overridden upstream reference(s) and MUST define the replacement behavior.

   * **P-STD-001-CLAUSE-011D (Variance lifecycle)** — Variance records MUST use lifecycle stages per `P-STD-001-CLAUSE-004` and MUST be reviewed at least once per release cycle or major migration event.

12) **P-STD-001-CLAUSE-012 (STD Index Schema & Column Definitions)**

   STD index tables MUST conform to the schema and column definitions defined by the subclauses below.

   * **P-STD-001-CLAUSE-012A (STD Index Schema)** — Each scope MUST maintain a `STD` index table using this schema: `| STD ID | Title | Status | Owner | Effective | Supersedes | Canonical Path | Verification | Governed By | Reference |`

   * **P-STD-001-CLAUSE-012B (Column definitions)** — `STD ID` MUST follow `P-STD-005-CLAUSE-001`. `Title` MUST be bold and follow title constraints. `Status` MUST use lowercase backtick-wrapped enums per `P-STD-001-CLAUSE-004B`. `Canonical Path` MUST be a full repo-relative path to the combined standard-specification file under the designated standards directory (per `P-STD-001-CLAUSE-015A`), or `—` if the STD is registry-only (no dedicated spec file). Semantics governed by `P-STD-001-CLAUSE-010`. `Effective` MUST be an ISO-8601 date `YYYY-MM-DD` or `—` if not yet set. `Verification` MUST describe (a) mechanism, (b) what is checked, and (c) pass/fail evidence. `Governed By` MUST list the governing basis (meta-governance). `Reference` MUST contain ONLY `RID`-category IDs per `P-STD-005-CLAUSE-002` and MUST NOT include `DRID`/`CLAUSE` IDs.

   * **P-STD-001-CLAUSE-012C (Phase 1 index granularity)** — Phase 1 index granularity is the combined file as a whole (no anchor addressing required in indexes).

13) **P-STD-001-CLAUSE-013 (STD Body Construction & Conciseness)**

   STD bodies MUST conform to the construction and conciseness requirements defined by the subclauses below.

   * **P-STD-001-CLAUSE-013A (Normative statement discipline)** — Each STD CLAUSE MUST express a single primary normative obligation. Compound obligations MUST be split into subclauses.

   * **P-STD-001-CLAUSE-013B (Conciseness target)** — STD clause text SHOULD be concise and avoid duplicating globally-governed semantics (e.g., ID construction) unless a local override is required.

   * **P-STD-001-CLAUSE-013C (Avoid structural redundancy)** — STD bodies SHOULD avoid duplicating content already present in the Specification Index (CLAUSE-002) or in governing upstream standards.

14) **P-STD-001-CLAUSE-014 (STD Drift Controls & Lifecycle Coherence)**

   STD content MUST remain aligned with canonical specifications and governing STDs per the subclauses below.

   * **P-STD-001-CLAUSE-014A (Canonical specification is authoritative)** — Where a STD Index entry includes a `Canonical Path`, the specification content at that canonical path is authoritative.

   * **P-STD-001-CLAUSE-014B (Derivatives conformance)** — Derivative artifacts MUST be updated with governing CLAUSE changes per `P-STD-001-CLAUSE-005`.

   * **P-STD-001-CLAUSE-014C (Supersession coherence)** — When a STD is superseded or deprecated, downstream indexes and references SHOULD be updated to reflect the new authority.

   * **P-STD-001-CLAUSE-014D (Avoid cross-file drift)** — Where possible, authority SHOULD be consolidated into a single canonical specification rather than duplicated across multiple governance files.

15) **P-STD-001-CLAUSE-015 (STD Placement & Directory Requirements)**

   Combined standard-specification files MUST be placed according to the subclauses below.

   * **P-STD-001-CLAUSE-015A (Designated standards directory)** — Combined standard-specification files MUST live under the designated standards directory: `prompt/artifacts/tasks/<SID>/standard/`. File naming MUST follow `standard_<SID-STD>_<kebab-title>.md`.

> *Informative*: T102's existing `consultant/standards/` directory is grandfathered per `proposal_T104-PH001-ST002-AC000` Convention 3. New initiatives MUST use `<SID>/standard/`.

   * **P-STD-001-CLAUSE-015B (Initiative-nonspecific directory rule)** — The designated directory MUST use `<SID>` placeholder in standards documentation and templates (not initiative-specific hardcoding), to ensure portability across initiatives.

   * **P-STD-001-CLAUSE-015C (Canonical Path validity)** — `Canonical Path` values MUST be full repo-relative paths that resolve to an existing file under the designated standards directory.

16) **P-STD-001-CLAUSE-016 (STD Status Management)**

   Status and supersession metadata for combined files MUST be maintained per the subclauses below.

   * **P-STD-001-CLAUSE-016A (Status enums)** — STD status values MUST use lifecycle stage enums per `P-STD-001-CLAUSE-004A` and MUST be rendered per `P-STD-001-CLAUSE-004B`.

   * **P-STD-001-CLAUSE-016B (Supersedes metadata)** — Supersession MUST be captured using the `Supersedes` field in the relevant index (STD Index or ADR Index). `Supersedes` MUST list superseded IDs or `—`.

   * **P-STD-001-CLAUSE-016C (Deprecation semantics)** — Deprecated STDs remain referenceable for history, but MUST NOT be treated as binding authority. Index entries SHOULD cite the superseding STD.

17) **P-STD-001-CLAUSE-017 (Migration Tolerance)**

   Migration from legacy governance identifiers MUST follow the subclauses below.

   * **P-STD-001-CLAUSE-017A (Alias window tolerance)** — During a governed alias window, legacy references MAY appear for compatibility, but new or updated normative references MUST use the current identifier forms.

   * **P-STD-001-CLAUSE-017B (One-time resequencing cost)** — When CLAUSE IDs are resequenced as a one-time migration, a controlled migration plan MUST exist and be executed to update key references.

   * **P-STD-001-CLAUSE-017C (No silent drift)** — After a migration, stale references MUST be treated as defects and SHOULD be fixed in the earliest feasible changeset.

18) **P-STD-001-CLAUSE-030 (Standard Promotion & Demotion Lifecycle)**

   A combined standard-specification surface MAY be promoted to a higher governance scope (e.g., Initiative → Program) or deprecated when its applicability changes. This clause defines the governance lifecycle for such transitions.

   * **P-STD-001-CLAUSE-030A (Promotion Eligibility)** — A standard is eligible for scope promotion when: (1) its normative content is stable (no open structural amendments in progress), and (2) it applies to, or is adopted by, multiple downstream scopes.

   * **P-STD-001-CLAUSE-030B (Promotion Process)** — A scope promotion MUST satisfy the following process: (1) A promotion contract MUST be drafted documenting: (i) the source standard ID, (ii) the target standard ID at the higher scope, (iii) the re-identification mapping for all CLAUSEs, substandards, and ADRs, (iv) any variances introduced at the new scope, (v) alias window terms per `P-STD-001-CLAUSE-030C`. (2) The promotion contract MUST pass a Client approval gate before execution. (3) The target standard MUST receive the full normative content of the source standard, re-identified to the new scope per `P-STD-005-CLAUSE-003A`. (4) The source standard MUST be marked `superseded` with a pointer to the target standard. (5) The promotion event MUST be recorded as an ADR in the target standard's Decision Record section.

   * **P-STD-001-CLAUSE-030C (Alias Window)** — Per `P-STD-005-CLAUSE-003B`, during a defined migration period, superseded CLAUSE IDs (e.g., `T102-STD-004-CLAUSE-001`) MAY be treated as aliases for the promoted CLAUSE IDs (e.g., `P-STD-001-CLAUSE-001`). Alias support MUST be removed after the migration completion milestone, which MUST be defined in the promotion contract.

   * **P-STD-001-CLAUSE-030D (Deprecation)** — A program-level standard MAY be deprecated when it is no longer applicable to any active scope. The standard status MUST be changed to `deprecated`. All adopters MUST be notified via a governance changeset. Deprecated standards MUST NOT be referenced by new authoring.

   * **P-STD-001-CLAUSE-030E (Promotion Record)** — Each promotion event MUST produce: (1) an ADR in the target standard documenting the promotion decision, (2) a supersession notice in the source standard, (3) updates to the relevant SPS STD Index rows (source → `superseded`; target → `draft` or `accepted`).

19) **P-STD-001-CLAUSE-033 (Derivative Metadata, Scope & Delegation)**

   Repo-owned derivative instruction surfaces governed by this standard MUST use lightweight metadata and explicit delegation patterns per the subclauses below.

   * **P-STD-001-CLAUSE-033A (Derivative metadata baseline)** — When a repo-owned derivative instruction surface adopts governed metadata, it MUST use a lightweight header that includes `artifact_type`, `scope`, `applies_to`, `version`, `date`, and `authority`.

   * **P-STD-001-CLAUSE-033B (Delegation metadata)** — A derivative surface that primarily delegates to another body or wrapper MUST declare `delegates_to`. Non-wrapper derivative surfaces MUST NOT add `delegates_to` unless delegation is the file's primary purpose.

   * **P-STD-001-CLAUSE-033C (Nearest-scope precedence)** — For same-family derivative instruction surfaces, the nearest applicable scope SHOULD override broader same-family guidance unless the broader surface explicitly reserves authority.

   * **P-STD-001-CLAUSE-033D (No wrapper duplication)** — Wrapper files SHOULD point to, not duplicate, the authoritative behavioral body they delegate to.

### P-STD-001C — Specification Authoring

20) **P-STD-001-CLAUSE-018 (CLAUSE Construction Requirements)**

   Specification CLAUSEs in combined standard-specification files MUST be constructed per the subclauses below.

   * **P-STD-001-CLAUSE-018A (Normative reference)** — `CLAUSE` token semantics MUST follow `P-STD-005-CLAUSE-005D (Specification Clause Semantics)`.

   * **P-STD-001-CLAUSE-018B (Format)** — Within the `## Specification` section, each clause MUST be rendered as: `n) **<CLAUSE-ID> (<Title>)**`, where `<CLAUSE-ID>` conforms to `P-STD-005-CLAUSE-005D`.

   * **P-STD-001-CLAUSE-018C (Single-statement discipline)** — Each CLAUSE MUST be a single primary normative statement (avoid compound obligations where feasible). If additional detail is required, it SHOULD be provided as subclauses per `P-STD-005-CLAUSE-005D`.

   * **P-STD-001-CLAUSE-018D (Title conventions)** — CLAUSE Titles MUST follow the title conventions defined in `P-STD-005-CLAUSE-001`.

   * **P-STD-001-CLAUSE-018E (Non-duplication constraint)** — `P-STD-001` MUST NOT redefine the syntax, scope validity, or semantic authority of `CLAUSE` IDs; those are defined in `P-STD-005-CLAUSE-005D`.

21) **P-STD-001-CLAUSE-019 (CLAUSE Ordering)**

   CLAUSE ordering within a combined standard-specification file MUST satisfy the subclauses below.

   * **P-STD-001-CLAUSE-019A (Sequential numbering)** — `CLAUSE` IDs MUST be assigned using sequential global numbers within the parent STD (`001`, `002`, `003`, ...). When substandards are used, CLAUSE-ID assignment is continuous across substandard boundaries. When adding a new CLAUSE to an existing substandard, the new CLAUSE MUST be appended after the last existing CLAUSE in that substandard's current block, using the next available global sequential CLAUSE-ID. Physical mid-substandard insertion that would require renumbering existing CLAUSE-IDs is PROHIBITED except during a governed release migration with a controlled migration plan per `P-STD-001-CLAUSE-017`. The in-file display number prefix (`n)`) and the Specification Index `#` column MUST reflect physical position order (1, 2, …, *n*), which MAY differ from the CLAUSE-ID number when a CLAUSE has been appended to a non-terminal substandard.

   * **P-STD-001-CLAUSE-019B (Subclause adjacency)** — Subclauses MUST immediately follow their parent clause.

22) **P-STD-001-CLAUSE-020 (Subclause Rendering)**

   Subclause rendering in combined standard-specification files MUST follow the subclauses below.

   * **P-STD-001-CLAUSE-020A (Bold format requirement)** — Subclauses MUST be rendered as nested bullet items under the parent clause using the format: `* **<CLAUSE-ID> (<Title>)** — <normative statement>`. This follows the markdown construction defined in `P-STD-005-CLAUSE-001`.

   * **P-STD-001-CLAUSE-020B (Prohibited format)** — Subclauses MUST NOT use backtick-wrapped format (e.g., `` `P-STD-001-CLAUSE-001A (Title)` ``). Backtick wrapping is reserved for inline code references, not for subclause rendering.

23) **P-STD-001-CLAUSE-021 (Normative/Informative Boundary Hygiene)**

   Combined standard-specification files MUST enforce a clear boundary between normative and informative content per the subclauses below.

   * **P-STD-001-CLAUSE-021A (Normative section authority)** — The `## Specification` section is the authoritative normative surface of a combined file. The `## Decision Record` section is informative rationale and MUST NOT create new obligations.

   * **P-STD-001-CLAUSE-021B (Informative section keyword hygiene)** — Informative sections (including `## Decision Record`) MUST NOT use BCP 14 keywords in uppercase (`MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, `MAY`) to express requirements. If an informative section needs to refer to a normative requirement, it MUST do so by citing the governing CLAUSE reference and/or quoting the normative text as a quotation.

   * **P-STD-001-CLAUSE-021C (Normative/informative labeling rule)** — If any non-Specification section contains normative requirements, that section MUST be explicitly labeled as normative and the governing CLAUSE(s) MUST be identified.

   * **P-STD-001-CLAUSE-021D (Derivative boundary alignment)** — Any derivative artifact that describes boundary hygiene expectations MUST cite this CLAUSE and MUST NOT introduce additional boundary rules beyond what is governed here.

24) **P-STD-001-CLAUSE-022 (Referencing & Non-Duplication)**

   CLAUSE referencing and non-duplication MUST follow the subclauses below.

   * **P-STD-001-CLAUSE-022A (CLAUSE referencing)** — Other artifacts MAY reference specific Specification CLAUSEs using the formal format defined in `P-STD-005-CLAUSE-004 (Reference Semantics)`.

   * **P-STD-001-CLAUSE-022B (Non-duplication constraint)** — Combined standard-specification files MUST NOT redefine the syntax, scope validity, or semantic authority of `CLAUSE` IDs; those are defined in `P-STD-005-CLAUSE-005D`.

### P-STD-001D — Decision Record Authoring

25) **P-STD-001-CLAUSE-023 (ADR Index Schema)**

   ADR index tables within combined standard-specification files MUST conform to the subclauses below.

   * **P-STD-001-CLAUSE-023A (ADR Index Schema)** — The ADR Index MUST use the schema: `| ADR ID | Title | Status | Supersedes | Date |`.

   * **P-STD-001-CLAUSE-023B (Column definitions)** — `ADR ID` MUST follow `P-STD-005-CLAUSE-005F` construction format (`<STD-ID>-ADR-###`). `Title` MUST follow title conventions per `P-STD-005-CLAUSE-001`. `Status` MUST use lowercase backtick-wrapped enums per `P-STD-001-CLAUSE-004B` (e.g., `accepted`, `superseded`). `Supersedes` MUST list superseded ADR IDs or `—`. `Date` MUST be ISO-8601 date `YYYY-MM-DD`.

   * **P-STD-001-CLAUSE-023C (Current-first ordering)** — ADR bodies in the `## Decision Record` section MUST be ordered with the current (most recent `accepted`) ADR first, followed by superseded ADRs in reverse chronological order.

   * **P-STD-001-CLAUSE-023D (Multiple ADRs in-file)** — Combined files MAY contain multiple ADR bodies (current + superseded). Superseded ADR bodies are retained for audit trail purposes. Only one ADR MAY have `accepted` status at any time; all others MUST be `superseded`.

26) **P-STD-001-CLAUSE-024 (ADR Entry Creation Workflow)**

   To create a new combined standard-specification file and its corresponding index entry, authors MUST satisfy the subclauses below.

   * **P-STD-001-CLAUSE-024A (File naming convention)** — Combined standard-specification filenames MUST follow `standard_<STD-ID>_<title-slug>.md` where `<title-slug>` is lowercase, spaces -> `-`, non-alphanumeric characters removed/replaced with `-`, and repeated `-` collapsed.

   * **P-STD-001-CLAUSE-024B (Create index row)** — Authors MUST add a new row to the appropriate STD index table using the schema per `P-STD-001-CLAUSE-012`.

   * **P-STD-001-CLAUSE-024C (Assign ID)** — Authors MUST assign the next sequential STD ID for that scope.

   * **P-STD-001-CLAUSE-024D (Create combined file)** — Authors MUST create a combined standard-specification file at the canonical path under the designated standards directory (per `P-STD-001-CLAUSE-015A`) using the standard-specification template, including frontmatter governed by `P-STD-001-CLAUSE-031`, CLAUSE entries under `## Specification`, DR body structure under `## Decision Record` per `P-STD-001-CLAUSE-025`, and metadata sections conforming to `P-STD-001-CLAUSE-034` through `P-STD-001-CLAUSE-036`.

   * **P-STD-001-CLAUSE-024E (References conformance)** — Authors MUST ensure References follow `P-STD-005-CLAUSE-004 (Reference Semantics)`.

   * **P-STD-001-CLAUSE-024F (Canonical Path population)** — Authors MUST populate the Canonical Path column (where applicable) in the index row with the full repo-relative path to the combined file.

27) **P-STD-001-CLAUSE-025 (DR Body Template)**

   Nested ADR bodies in combined standard-specification files MUST conform to the subclauses below.

   * **P-STD-001-CLAUSE-025A (Header format)** — Nested ADR header MUST be rendered as: `* **<STD-ID>-ADR-### (<Title>)** {#<anchor>}`.

   * **P-STD-001-CLAUSE-025B (Required subheadings)** — Nested ADR body MUST include these subheadings: **Context**, **Decision**, **Alternatives**, **Consequences**, **Traceability**.

   * **P-STD-001-CLAUSE-025C (Body formatting rules)** — Main bold headings (e.g., `* **Context**`) MUST be preceded by two newlines. Content MUST start on a new line and be indented under the heading with no space in between.

   * **P-STD-001-CLAUSE-025D (Context requirements)** — Context MUST describe why the decision is needed and the gap it resolves.

   * **P-STD-001-CLAUSE-025E (Decision requirements)** — Decision MUST state what is adopted/changed and who owns it.

   * **P-STD-001-CLAUSE-025F (Alternatives requirements)** — Alternatives MUST be a bulleted list of options considered with clear rejection rationales.

   * **P-STD-001-CLAUSE-025G (Consequences requirements)** — Consequences MUST be expressed using `(+)`, `(±)`, and `(-)` prefix bullets.

   * **P-STD-001-CLAUSE-025H (STD-level boundary)** — In combined standard-specification files, the DR body lives under `## Decision Record`. References and Provenance are STD-level sections per `P-STD-001-CLAUSE-028`.

   * **P-STD-001-CLAUSE-025I (Traceability requirements)** — Each nested ADR body MUST include a **Traceability** subheading as a non-normative surface for timeline references. Timeline references MUST be listed as bullet items containing fully-qualified IDs (e.g., `T102-PH001-ST001-AC009.1-TK003`). Traceability MUST NOT contain lazy shorthand references (e.g., `AC009.1-TK003`, `SES###`, `SES###-DEC###`).

28) **P-STD-001-CLAUSE-026 (Cross-Artifact Linking Patterns)**

   Combined standard-specification files MUST satisfy the cross-artifact linking patterns defined by subclauses below:

   * **P-STD-001-CLAUSE-026A (STD internal DR pattern)** — A combined standard-specification file MUST contain its decision record internally under `## Decision Record` using the nested ADR format from `P-STD-001-CLAUSE-025`.

   * **P-STD-001-CLAUSE-026B (Decision Record context pattern)** — The nested ADR **Context** SHOULD state the motivating problem in narrative form and SHOULD NOT include timeline IDs. Timeline IDs belong under **Traceability** per `P-STD-001-CLAUSE-025I`.

   * **P-STD-001-CLAUSE-026C (Context/References boundary)** — The nested ADR **Context** SHOULD NOT contain a "Governed By" citation line. Governing references belong in `## References` per `P-STD-001-CLAUSE-028`.

   * **P-STD-001-CLAUSE-026D (Index Link Pattern)** — Index artifacts (SPS/Concept) SHOULD reference combined files via `Canonical Path` and MUST NOT duplicate the full normative specification body.

29) **P-STD-001-CLAUSE-027 (ADR Consequences Scope)**

   Consequences sections in nested ADR bodies SHOULD cover the scope defined by CLAUSE-027A.

   * **P-STD-001-CLAUSE-027A (ADR-only consequences)** — Consequences apply to the Decision Record scope only. STDs and CLAUSEs MUST NOT include separate "STD Consequences" sections; consequences belong in ADR bodies under `## Decision Record`.

30) **P-STD-001-CLAUSE-028 (References & Provenance)**

   Combined files MUST satisfy the References and Provenance requirements defined by the subclauses below.

   * **P-STD-001-CLAUSE-028A (References requirements)** — Every combined file MUST include a `## References` section structured per `P-STD-001-CLAUSE-035`.

   * **P-STD-001-CLAUSE-028B (Provenance requirements)** — Every combined file MUST include a `## Provenance` section structured per `P-STD-001-CLAUSE-036`.

31) **P-STD-001-CLAUSE-029 (Decision Promotion Workflow)**

   Promotion of decision content into Standards SHOULD follow the subclauses below.

   * **P-STD-001-CLAUSE-029A (STD promotion criteria)** — Authors SHOULD promote stable, cross-cutting, or long-lived patterns into formal `STD` records when: (a) the pattern affects multiple artifacts or features, or (b) the pattern requires explicit governance (ownership, status, supersedes) beyond implementation detail. When promoted, the `STD` MUST contain a nested ADR for rationale per `P-STD-001-CLAUSE-025`.

   * **P-STD-001-CLAUSE-029B (CLAUSE promotion)** — When a normative obligation in a combined file warrants addressable precision, it SHOULD be formalized as a named CLAUSE (or subclause) per `P-STD-001-CLAUSE-018`.

   * **P-STD-001-CLAUSE-029C (Traceability)** — Specifications SHOULD reference governing research and guidance in **Provenance** and **References** (per `P-STD-001-CLAUSE-028`), rather than duplicating detailed patterns. Token-specific promotion workflows for `RES` and `IG` tokens are governed by `P-STD-005`.

32) **P-STD-001-CLAUSE-034 (Version Tracking & Amendment History)**

   Combined standard-specification files MUST track current version and concise amendment history per the subclauses below.

   * **P-STD-001-CLAUSE-034A (Semver contract)** — Standard files MUST use semver for the current `version` field stored in frontmatter.

   * **P-STD-001-CLAUSE-034B (Amendment history location)** — A concise `Amendment History` subsection MUST appear under `## Provenance` per `P-STD-001-CLAUSE-036`.

   * **P-STD-001-CLAUSE-034C (Increment triggers)** — Patch increments apply to editorial or metadata-only corrections. Minor increments apply to compatible normative additions or compatible structural refinements. Major increments apply to breaking governance changes, incompatible metadata-schema changes, or relocations that alter authoring expectations.

   * **P-STD-001-CLAUSE-034D (Legacy pre-baseline history)** — Historical events that predate governed semver adoption MAY be retained in `Amendment History` without a semver label, but they MUST be clearly marked as pre-baseline history.

33) **P-STD-001-CLAUSE-035 (References Taxonomy & Schema)**

   Combined standard-specification files MUST structure `## References` per the subclauses below.

   * **P-STD-001-CLAUSE-035A (Subsection taxonomy)** — `## References` MUST contain `### Normative References` and `### Informative References`.

   * **P-STD-001-CLAUSE-035B (Row schema)** — Each references table MUST use the schema `| ID | Title | Scope | Source Path |`.

   * **P-STD-001-CLAUSE-035C (Normative contents)** — `Normative References` MUST contain governing standards or other authorities required to interpret or apply the specification.

   * **P-STD-001-CLAUSE-035D (Informative contents)** — `Informative References` MUST contain supporting material, legacy context, or non-governing evidence that assists interpretation without changing authority.

   * **P-STD-001-CLAUSE-035E (Lineage boundary)** — Promotion contracts, seed-input inventories, and similar lineage pointers SHOULD live in `## Provenance` unless the cited artifact is also being used as a governing or supporting reference.

34) **P-STD-001-CLAUSE-036 (Provenance Taxonomy & Extensions)**

   Combined standard-specification files MUST structure `## Provenance` per the subclauses below.

   * **P-STD-001-CLAUSE-036A (Minimum subsection taxonomy)** — `## Provenance` MUST contain `### Status`, `### Lineage / Authority`, `### Amendment History`, and `### Input Sources`.

   * **P-STD-001-CLAUSE-036B (Status subsection)** — `Status` SHOULD capture the present accepted/draft posture in concise form using a compact table or similarly scannable governed structure. It MAY include approval/effective context that complements, but does not override, frontmatter.

   * **P-STD-001-CLAUSE-036C (Lineage / Authority subsection)** — `Lineage / Authority` MUST capture supersession, promotion, alias-window, or comparable authority-chain pointers relevant to the current specification. The subsection SHOULD prefer compact key/value rendering over narrative bullets when that keeps the authority chain clearer.

   * **P-STD-001-CLAUSE-036D (Amendment History subsection)** — `Amendment History` MUST record concise dated change summaries and SHOULD defer full diff detail to version control and process artifacts.

   * **P-STD-001-CLAUSE-036E (Input Sources subsection)** — `Input Sources` MUST list the proposals, analyses, session notes, research, or other concise lineage pointers that materially informed the specification. The list SHOULD be limited to materially used sources and SHOULD avoid carrying stale context that no longer informs the current state.

   * **P-STD-001-CLAUSE-036F (Extension control)** — Additional provenance subsections MAY be added only when they do not duplicate the minimum taxonomy and when a governing standard or approved activity explicitly requires them.

   * **P-STD-001-CLAUSE-036G (Externalized amendment changelog)** — When `### Amendment History` inline entries exceed five, the full version-indexed changelog SHOULD be externalized to a dedicated file at `<SID>/standard/changelog/changelog_standard_<SID-STD>.md`. The inline `### Amendment History` subsection MUST retain the three most recent versioned entries and MUST include a blockquote pointer line in the format `> Full version history: \`<repo-relative-path-to-changelog>\`` placed immediately after the `### Amendment History` heading and before the retained inline entries. The externalized changelog file MUST use tabular format with schema `| Version | Date | Type | Summary |` and MUST contain the complete version history including pre-baseline entries.

## Decision Record

### ADR Index
| ADR ID | Title | Status | Supersedes | Date |
|:--|:--|:--|:--|:--|
| P-STD-001-ADR-003 | Full Promotion from T102-STD-004 | `accepted` | ADR-002 | 2026-02-20 |
| P-STD-001-ADR-002 | Combined Authoring & Governance Standard | `superseded` | ADR-001 | 2026-02-15 |
| P-STD-001-ADR-001 | Specification Standard & Guideline | `superseded` | — | 2026-02-08 |

* **P-STD-001-ADR-003 (Full Promotion from T102-STD-004)** {#p-std-001-adr-003-full-promotion-from-t102-std-004}

  * **Context**
    `T102-STD-004` was authored at Initiative scope (T102) but governs a concern applicable to all initiatives program-wide: the combined standard-specification authoring model. As additional initiatives (T104, future) require conformance to the same authoring rules, having the authoritative standard at Initiative scope creates scope-identity misalignment, reference ambiguity, and development location confusion.

  * **Decision**
    Promote `T102-STD-004` to `P-STD-001` via full content transfer with 1:1 CLAUSE re-identification. Mark `T102-STD-004` as `superseded`. Establish an alias window per `P-STD-005-CLAUSE-003B` for existing references.

  * **Alternatives**
    * *Adopt-by-reference*: `P-STD-001` as thin wrapper incorporating `T102-STD-004` by normative reference. Rejected: creates two-hop reference pattern, scope-identity mismatch, principal-agent problem for development location. Scored 2.50 vs 4.60 in weighted analysis.
    * *Status quo*: No promotion; downstream consumers reference `T102-STD-004` directly. Rejected: `T102` prefix misleads about governance scope; no program-level authority surface exists.

  * **Consequences**
    (+) `P-STD-001` is the single authoritative surface for standard-specification authoring at Program scope.
    (+) All new references use `P-STD-001`; guideline/template authority chains updated from `T102-STD-004` to `P-STD-001`.
    (+) Future standard promotions (`P-STD-002` through `P-STD-005`) follow the precedent and process defined in `P-STD-001-CLAUSE-030`.
    (±) `T102-STD-004` becomes a read-only historical artifact (status: `superseded`); existing references migrate at next touch during the alias window.
    (-) One-time migration effort to re-identify 29 CLAUSEs, 4 substandards, and 2 ADRs; alias window required for transition.

  * **Traceability**
    * `P-PH000-ST001-AC002-SES001-DEC001` (Full Promotion methodology approval)
    * `P-PH000-ST001-AC002-SES001-DEC002` (1:1 CLAUSE renumbering + CLAUSE-030)
    * `P-PH000-ST001-AC002-SES001-DEC003` (CLAUSE-030 placement in Substandard B)
    * `P-PH000-ST001-AC002-SES001-DEC006` (CLAUSE-015A directory canonical form)
    * `analysis_P-PH000-ST001-AC002_promotion-methodology-comparison.md` (weighted criteria analysis)
    * `P-STD-005-CLAUSE-003A` (promotion contract rules)
    * `P-STD-005-CLAUSE-003B` (alias window rules)

* **P-STD-001-ADR-002 (Combined Authoring & Governance Standard)** {#p-std-001-adr-002-combined-authoring-and-governance-standard}

  * **Context**
    T102-STD-004’s governance model evolved through self-compliance auditing, Client QA, and research benchmarking. The combined-file architecture and fine-grained subclause discipline were validated while drift risk across split governance surfaces was identified as a practical operational concern for agentic LLM authoring. The Client therefore chose to consolidate governance by merging STD-009 into STD-004, adopting a four-substandard architecture, retaining multiple in-file ADR bodies (current-first), and adding an append-only sequencing constraint to reduce future renumbering blast radius. Industry benchmarking in `T102-RES-007` informed the direction but did not override the Client’s drift-control decision.

  * **Decision**
    - Merge `T102-STD-009` into `P-STD-001` and treat `T102-STD-009` as deprecated in dependent indexes (handled outside this sub-activity).
    - Organize `P-STD-001` into four substandards: `P-STD-001A`, `P-STD-001B`, `P-STD-001C`, `P-STD-001D`.
    - Resequence and maintain a single global `CLAUSE` numbering sequence across all substandards (with append-only growth constraint in `P-STD-001-CLAUSE-019A`).
    - Store multiple ADR bodies in-file under `## Decision Record`, ordered current-first per `P-STD-001-CLAUSE-023C`, retaining superseded ADRs for audit trail.
    - Use `Canonical Path` (not `Adopts`) in the STD Index schema, and remove the redundant `Authority STD` column from the ADR Index schema.

  * **Alternatives**
    - Keep `P-STD-001` and `T102-STD-009` separate with interface contracts — rejected due to persistent drift and context loss for agentic LLM authoring.
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

* **P-STD-001-ADR-001 (Specification Standard & Guideline)** {#p-std-001-adr-001-specification-standard-and-guideline}

  * **Context**
    The current governance surface is split between index artifacts and combined files, which creates a dual-surface authoring pattern that drifts over time and weakens consistency targets tied to `T102-QG-001`. A single canonical combined-file structure is needed so normative clauses and decision rationale remain co-located, machine-checkable, and reviewable.

  * **Decision**
    Adopt the standard-specification combined-file model with `## Specification` first and a nested informative ADR under `## Decision Record`. This file (`P-STD-001`) is the golden exemplar defining clause structure, linkage patterns, and lifecycle controls for decision-record standards.

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

### Normative References

| ID | Title | Scope | Source Path |
|:--|:--|:--|:--|
| `P-STD-005` | Universal ID Specification | Program (P) | `prompt/artifacts/tasks/P/standard/standard_P-STD-005_universal-id-specification.md` |
| `P-STD-004` | File Naming & Directory Convention | Program (P) | `prompt/artifacts/tasks/P/standard/standard_P-STD-004_file-naming-and-directory-convention.md` |

### Informative References

| ID | Title | Scope | Source Path |
|:--|:--|:--|:--|
| `T102-CON-009` | Controlled Vocabulary for Normative Language | Initiative (T102) | `prompt/artifacts/tasks/T102/ssot/sps_T102-CONSULTANT.md` |
| `P-RES-003` | Specification Metadata Governance Research | Program (P) | `prompt/artifacts/tasks/P/research/P-RES-003/report_P-RES-003_specification-metadata-governance-research.md` |
| `P-PH000-ST001-AC002` | P-STD-001 Promotion Methodology Comparison | Program (P) | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC002/analysis/analysis_P-PH000-ST001-AC002_promotion-methodology-comparison.md` |

## Provenance

### Status

| Field | Value |
|:--|:--|
| Current lifecycle posture | `accepted` |
| Approved | 2026-02-22 |
| Effective | 2026-02-22 |

### Lineage / Authority

| Field | Value |
|:--|:--|
| Supersedes | `T102-STD-004` (Specification Standard & Guideline) |
| Promotion contract | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC002/proposal/proposal_P-PH000-ST001-AC002_promotion-contract-t102-std-004-to-p-std-001.md` |
| Promotion decision | `P-STD-001-ADR-003` |
| Alias window | Active — existing `T102-STD-004-CLAUSE-*` references remain valid aliases until migration completion |
| Original authoring scope | `T102-PH001-ST001` |
| Original author | `LLM_Consultant` |

### Amendment History

> Full version history: `prompt/artifacts/tasks/P/standard/changelog/changelog_standard_P-STD-001.md`

- v1.2.0 (2026-03-26): Added `CLAUSE-036G` (Externalized Amendment Changelog) enabling standards to externalize full version history to a dedicated changelog file while retaining compact inline summaries. Self-aligned `P-STD-001` to the new pattern.
- v1.1.0 (2026-03-20): Replaced lower-scope normative vocabulary authority with a program-scope drafting contract, refreshed `References` to a current-state authority set, and tightened the governed compact rendering for `Status` and `Lineage / Authority`.
- v1.0.0 (2026-03-16): Added metadata-governance clauses `031` through `036`, standardized frontmatter / References / Provenance governance, self-aligned `P-STD-001`, and aligned prompt-owned derivatives and `P-CON-003`.

### Input Sources

- `prompt/artifacts/tasks/T102/workspace/PH001/ST001/AC009/proposal/proposal_T102-CWD_PH001-ST001-AC009_std-004-redesign.md`
- `prompt/artifacts/tasks/T102/workspace/PH001/ST001/AC009.1/proposal/proposal_T102-CWD_PH001-ST001-AC009.1_tk003_std-004-clause-019-sequencing-amendment.md`
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC002/analysis/analysis_P-PH000-ST001-AC002_promotion-methodology-comparison.md`
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC002/snotes/snotes_P-PH000-ST001-AC002-SES001.md`
- `prompt/artifacts/tasks/P/research/P-RES-003/report_P-RES-003_specification-metadata-governance-research.md`
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/analysis/analysis_P-PH000-ST001-AC009-TK001_p-std-001-amendment-map.md`
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/implementation/implementation_P-PH000-ST001-AC009_gate-001-remediation-specification.md`
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/implementation/implementation_P-PH000-ST001-AC009_p-std-001-evolution-task-specification.md`
