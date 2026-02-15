---
artifact_type: 'PROPOSAL'
initiative_id: 'T102'
initiative_code: 'CWD'
activity_id: 'T102-PH001-ST001-AC009'
sub_activity_id: 'T102-PH001-ST001-AC009.1'
task_id: 'AC009.1-TK001'
version: '0.1.0'
date: '2026-02-15'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T102/consultant/workspace/plan/plan_T102-PH001-ST001.md'
session_reference: 'prompt/artifacts/tasks/T102/consultant/workspace/notes/PH001/ST001/notes_T102-PH001-ST001-AC009-SES002.md'
raw_transcript_reference: 'prompt/artifacts/tasks/T102/consultant/raw/PH001/ST001/raw_T102-PH001-ST001-AC009-SES002.txt'
supersedes: 'prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_PH001-ST001-AC008_r2-refactor-plan.md'
target_files:
  - 'prompt/artifacts/tasks/T102/consultant/standards/T102-STD-004_specification-standard-and-guideline.md'
  - 'prompt/artifacts/tasks/T102/consultant/standards/T102-STD-009_governance-standards-specification.md'
  - 'prompt/templates/consultant/standards/guideline_standard_specs.md'
  - 'prompt/templates/consultant/standards/template_standard_specs.md'
  - 'prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md'
---

# PROPOSAL: T102 (CWD) — PH001 / ST001 / AC009 — STD-004 Comprehensive Redesign (STD-009 Merge + Substandard Architecture)

## I. Executive Summary

This proposal supersedes the prior R2 Refactor Plan (`proposal_T102-CWD_PH001-ST001-AC008_r2-refactor-plan.md` v0.2.0) and constitutes the primary deliverable of sub-activity AC009.1-TK001.

**What changed**: AC009-GATE-001 QA review identified systemic issues in the prior R2 proposal requiring a fundamental structural redesign rather than incremental correction. Three rounds of consultation dialogue produced 18 decisions that collectively mandate:

1. **STD-009 merger into STD-004** (SES002-DEC001) — Absorb all 5 STD-009 CLAUSEs to eliminate drift and context loss for agentic LLM authors
2. **Substandard architecture** (SES002-DEC002/DEC003) — Introduce 4 substandards (T102-STD-004A/B/C/D) with every CLAUSE belonging to a substandard (IEEE "General clause" pattern)
3. **Full CLAUSE resequencing** (SES002-DEC002) — Upfront structural investment; R2 stability promise superseded by gate review decision
4. **Multiple ADRs in-file** (SES002-DEC004) — Current-first ordering; ADR-001 preserved for audit trail; prepares for Phase 2 ADR extraction
5. **CLAUSE-013 full removal** (SES002-DEC005) — Variance ADR Contract reassessed during T102-STD-005 work (ST002)
6. **All QA corrections applied** — Subclause bold format (DEC015), status enum lowercase (DEC008), initiative-nonspecific directory (DEC009), per-subheading content requirements (DEC010), vocabulary reference to CON-009 (DEC012), precedence scoping (DEC013), consequences ADR-only (DEC014), promotion scope reduction (DEC011)

**Scope**: 5 target files (STD-004 + STD-009 deprecation + guideline + template + SPS). Implementation gated on client approval (AC009.1-GATE-001).

**All 18 SES002 decisions** (DEC001–DEC018) are referenced throughout this proposal. Full decision register: `notes_T102-PH001-ST001-AC009-SES002.md`.

---

## II. Architecture Design

### II.A. Substandard Architecture

**Definition**: A substandard is an internal domain grouping within a parent STD combined file. Substandards organize CLAUSEs into coherent thematic domains to improve navigability, reduce cognitive load, and support modular evolution — without creating separate files or separate registry entries.

**ID format**: `<STD-ID><CAPITAL_LETTER>` (e.g., `T102-STD-004A`, `T102-STD-004B`).

**Fundamental rule**: Every CLAUSE MUST belong to exactly one substandard. No floating CLAUSEs exist outside substandards (SES002-DEC003). Cross-cutting concerns (file structure, lifecycle, vocabulary) live in a dedicated "Core" substandard (T102-STD-004A), following the IEEE "General clause" pattern.

**Industry precedent**:

| Standard Body | Modularization Pattern | Cross-Cutting Handling |
|:--|:--|:--|
| ISO (e.g., 27001) | "Parts" (Part 1, Part 2...) | Each part has own Scope, Terms. No floating clauses. |
| IEEE (e.g., 802.x) | Numbered clauses with "General" clause first | Cross-cutting provisions in dedicated "General" clause |
| W3C (e.g., CSS modules) | Named modules | Common definitions in "base" module |
| RFC (e.g., TLS 1.3) | Self-contained documents | Each RFC includes own "Conventions" and "Overview" |

**Universal pattern**: Every module/part is self-contained. Cross-cutting concerns live in a dedicated "General" or "Core" module — never as floating items outside the modular structure.

**Domain allocation**:

| Substandard | Domain | Absorbs From | Key CLAUSEs |
|:--|:--|:--|:--|
| **T102-STD-004A** | **Core Structure & Lifecycle** | STD-004 CLAUSE-016 (structure), CLAUSE-017 (lifecycle/authority), CLAUSE-015 (automation), CLAUSE-007 (anchors) + new Specification Index + new Substandard Architecture | Canonical file structure, specification index, substandard architecture definition, lifecycle stages, authority derivation, conformance coupling, anchor stability, automation/linting, normative vocabulary guidance |
| **T102-STD-004B** | **STD Registry & Governance** | All STD-009 CLAUSEs (001-005) + STD-004 CLAUSE-001 (index schemas partially), CLAUSE-002 (placement), CLAUSE-008 (lifecycle coherence), CLAUSE-009 (status management), CLAUSE-010 (precedence, revised) | STD semantics/scope, adoption contract, precedence/variance (STD-scoped), STD index schema, column definitions, body construction, conciseness, drift controls, placement/directory, status management, migration tolerance |
| **T102-STD-004C** | **Specification Authoring** | STD-004 CLAUSE-005 (specification clauses), CLAUSE-018 (boundary hygiene) | CLAUSE construction requirements, ordering, subclause rendering, normative/informative boundary hygiene, referencing patterns, non-duplication constraint |
| **T102-STD-004D** | **Decision Record Authoring** | STD-004 CLAUSE-001 (ADR index schema), CLAUSE-003 (entry creation), CLAUSE-004 (DR body), CLAUSE-006 (linking), CLAUSE-011 (consequences ADR-only), CLAUSE-012 (references/provenance), CLAUSE-014 (promotion, reduced scope) | ADR index schema, entry creation workflow, DR body template (with per-subheading content/format subclauses), cross-artifact linking, consequences scope (ADR-only), references/provenance, decision promotion workflow (STD/CLAUSE/ADR-scoped) |

**Reading flow rationale**: Core (file structure and cross-cutting rules) -> STD Registry (how to manage standards) -> Specification Authoring (how to write CLAUSEs) -> Decision Record Authoring (how to write ADRs). Each substandard is self-contained and references others only via CLAUSE cross-references.

**Registration**: Substandards are internal structure within T102-STD-004. They are NOT separate SPS rows. The SPS maintains a single row for T102-STD-004 with description updated to reflect the substandard domains.

---

### II.B. STD-009 Merge Plan

**Rationale** (SES002-DEC001): STD-009 and STD-004 govern closely related concerns (how to manage standards vs how to write them), and maintaining them separately causes:
- Extreme drift and context loss for agentic LLM authors
- Hallucination of content between related STD/CLAUSE/ADR tokens (e.g., "Canonical Path" referenced but not present in STD-004)
- Redundant cross-referencing that increases cognitive load

**CLAUSE mapping** (STD-009 -> merged STD-004):

| STD-009 CLAUSE | Title | Target Substandard | New CLAUSE ID | Disposition |
|:--|:--|:--|:--|:--|
| STD-009-CLAUSE-001 | Semantics & Scope | T102-STD-004B | CLAUSE-009 | Absorbed directly |
| STD-009-CLAUSE-002 | Adoption Contract | T102-STD-004B | CLAUSE-010 | Absorbed directly |
| STD-009-CLAUSE-003 | Precedence & Variance | T102-STD-004B | CLAUSE-011 (combined with old CLAUSE-010) | Merged with precedence revision per DEC013 |
| STD-009-CLAUSE-004 | STD Authoring Requirements (+ subclauses 004A-E) | T102-STD-004B | CLAUSE-012, CLAUSE-013, CLAUSE-014 | Split into: Index Schema (004A/B), Body Construction (004C/D), Drift Controls (004E) |
| STD-009-CLAUSE-005 | Migration Tolerance | T102-STD-004B | CLAUSE-017 | Absorbed directly |

**STD-009 supersession record**:
- SPS STD Index: T102-STD-009 row status -> `deprecated`, add `Supersedes: —`, note `Superseded by T102-STD-004`
- STD-009 combined file: status -> `deprecated`; add supersession notice pointing to T102-STD-004
- File archival/deletion: ST002 scope (not AC009.1)

**SPS reference update targets**: All 8 STD rows citing `T102-STD-009 (Governance Standards Model)` in their `Reference` column (STD-001 through STD-008) MUST be updated to reference `T102-STD-004 (Specification Standard & Guideline)`.

**STD-009 ADR-001 preservation**: STD-009-ADR-001 rationale is NOT carried into T102-STD-004. Its content is absorbed into T102-STD-004-ADR-002 Context section (noting the merge history). The original STD-009 file is retained as a deprecated artifact for historical reference.

---

### II.C. ADR Storage Architecture

**Design** (SES002-DEC004): Multiple ADRs in-file with ADR Index.

**ADR Index schema**:

| ADR ID | Title | Status | Supersedes | Date |
|:--|:--|:--|:--|:--|
| T102-STD-004-ADR-002 | Combined Authoring & Governance Standard | `accepted` | ADR-001 | 2026-02-15 |
| T102-STD-004-ADR-001 | Specification Standard & Guideline | `superseded` | — | 2026-02-08 |

**Ordering**: Current ADR listed first (readers encounter active decision immediately). Superseded ADRs follow in reverse chronological order.

**Rationale for multiple ADRs in-file (vs update-in-place)**:
- Git history is unreliable for governance audit (force push, squash, migration can destroy history)
- Phase 2 envisions separating decision records into dedicated paths — having ADR bodies already in-file provides clean extraction source
- Full audit trail visible without tooling (supports T102-QG-001 Client Readability)
- Aligns with Michael Nygard's original ADR pattern: decisions are immutable records

**STD-005-CLAUSE-005F amendment** (flagged as INT-003): The current constraint ("only one current nested ADR at a time") needs revision to: "only one `accepted` ADR; `superseded` ADRs are retained for audit purposes." This amendment is flagged for ST002 or self-amendment in the merged STD-004.

---

### II.D. Specification Index

**Schema** (SES002-DEC006):

| # | Substandard | CLAUSE ID | Title | Description |
|:--|:--|:--|:--|:--|

**Placement**: Immediately after `## Specification` heading, before the first substandard section heading.

**Content**: Main CLAUSEs only (subclauses are NOT indexed individually). The `#` column provides sequential display numbering for quick counting. The `Substandard` column enables domain grouping at a glance. The `Description` column contains a 1-line normative summary (~10-15 words).

**Governing CLAUSE**: T102-STD-004-CLAUSE-002 (new; within T102-STD-004A).

---

### II.E. Canonical File Structure (Revised)

Updated section order incorporating substandards:

```
# T102-STD-004 — Specification Standard & Guideline
{#t102-std-004-specification-standard-and-guideline}

## Specification

### Specification Index
[CLAUSE register table]

### T102-STD-004A — Core Structure & Lifecycle
[CLAUSEs 001-008]

### T102-STD-004B — STD Registry & Governance
[CLAUSEs 009-017]

### T102-STD-004C — Specification Authoring
[CLAUSEs 018-022]

### T102-STD-004D — Decision Record Authoring
[CLAUSEs 023-029]

## Decision Record

### ADR Index
[ADR register table — current-first ordering]

* T102-STD-004-ADR-002 (current)
  [full body]

* T102-STD-004-ADR-001 (superseded)
  [full body preserved]

## References

## Provenance
```

---

## III. CLAUSE Register (Full Resequencing)

This is the master allocation map that drives the per-CLAUSE specifications in Section IV.

| Old ID | New ID | Substandard | New Title | Disposition |
|:--|:--|:--|:--|:--|
| CLAUSE-016 | **CLAUSE-001** | T102-STD-004A | Canonical File Structure | Revised (minus vocabulary subclause; substandard sections added) |
| _(new)_ | **CLAUSE-002** | T102-STD-004A | Specification Index | New (DEC006) |
| _(new)_ | **CLAUSE-003** | T102-STD-004A | Substandard Architecture | New (DEC002/DEC003) |
| CLAUSE-017 (part) | **CLAUSE-004** | T102-STD-004A | Specification Lifecycle Stages | Revised (extracted from CLAUSE-017) |
| CLAUSE-017 (part) | **CLAUSE-005** | T102-STD-004A | Authority Derivation & Conformance Coupling | Revised (extracted from CLAUSE-017; conformance coupling) |
| CLAUSE-007 | **CLAUSE-006** | T102-STD-004A | Anchor Stability | Revised (ID+Title derivation rule) |
| CLAUSE-015 | **CLAUSE-007** | T102-STD-004A | Automation & Linting Checks | Revised (updated for substandard structure) |
| CLAUSE-016D | **CLAUSE-008** | T102-STD-004A | Normative Vocabulary Guidance | Revised (references T102-CON-009 per DEC012) |
| STD-009-CLAUSE-001 | **CLAUSE-009** | T102-STD-004B | STD Semantics & Scope | Absorbed from STD-009 |
| STD-009-CLAUSE-002 | **CLAUSE-010** | T102-STD-004B | STD Adoption Contract | Absorbed from STD-009 |
| CLAUSE-010 + STD-009-CLAUSE-003 | **CLAUSE-011** | T102-STD-004B | STD Precedence & Variance | Merged + revised (reference STD-005-CLAUSE-003; expand for STD/CLAUSE/ADR per DEC013) |
| CLAUSE-001 (partial) + STD-009-CLAUSE-004A/B | **CLAUSE-012** | T102-STD-004B | STD Index Schema & Column Definitions | Merged (STD index schema + column definitions) |
| STD-009-CLAUSE-004C/D | **CLAUSE-013** | T102-STD-004B | STD Body Construction & Conciseness | Absorbed from STD-009 |
| CLAUSE-008 + STD-009-CLAUSE-004E | **CLAUSE-014** | T102-STD-004B | STD Drift Controls & Lifecycle Coherence | Merged (drift controls + lifecycle coherence) |
| CLAUSE-002 | **CLAUSE-015** | T102-STD-004B | STD Placement & Directory Requirements | Revised (initiative-nonspecific per DEC009) |
| CLAUSE-009 | **CLAUSE-016** | T102-STD-004B | STD Status Management | Revised (lowercase backtick enums per DEC008) |
| STD-009-CLAUSE-005 | **CLAUSE-017** | T102-STD-004B | Migration Tolerance | Absorbed from STD-009 |
| CLAUSE-005 (core) | **CLAUSE-018** | T102-STD-004C | CLAUSE Construction Requirements | Revised (single-statement discipline; normative reference) |
| CLAUSE-005 (ordering) | **CLAUSE-019** | T102-STD-004C | CLAUSE Ordering | Revised (sequential within parent STD) |
| CLAUSE-005 (rendering) | **CLAUSE-020** | T102-STD-004C | Subclause Rendering | Revised (bold format per DEC015; NOT backtick-wrapped) |
| CLAUSE-018 | **CLAUSE-021** | T102-STD-004C | Normative/Informative Boundary Hygiene | Kept (from R2-Enhanced; RES-007 boundary hygiene) |
| CLAUSE-005 (referencing + non-dup) | **CLAUSE-022** | T102-STD-004C | Referencing & Non-Duplication | Revised (referencing patterns + non-duplication constraint) |
| CLAUSE-001 (ADR parts) | **CLAUSE-023** | T102-STD-004D | ADR Index Schema | Revised (multiple ADRs in-file per DEC004; current-first ordering) |
| CLAUSE-003 | **CLAUSE-024** | T102-STD-004D | ADR Entry Creation Workflow | Revised (normative MUST statements; file naming convention) |
| CLAUSE-004 | **CLAUSE-025** | T102-STD-004D | DR Body Template | Revised (per-subheading content + format subclauses per DEC010) |
| CLAUSE-006 | **CLAUSE-026** | T102-STD-004D | Cross-Artifact Linking Patterns | Revised (subclauses for each pattern) |
| CLAUSE-011 | **CLAUSE-027** | T102-STD-004D | ADR Consequences Scope | Revised (ADR-only; "STD Consequences" removed per DEC014) |
| CLAUSE-012 | **CLAUSE-028** | T102-STD-004D | References & Provenance | Revised (subclauses for each) |
| CLAUSE-014 | **CLAUSE-029** | T102-STD-004D | Decision Promotion Workflow | Revised (scope reduced to STD/CLAUSE/ADR per DEC011) |

**CLAUSEs removed** (not carried to any substandard):

| Original CLAUSE | Reason | Disposition |
|:--|:--|:--|
| CLAUSE-013 (Variance ADR Contract) | Migrated to STD-005 scope (SES002-DEC005) | Documented in STD-005 integration issues (INT-001) |

**Total**: 29 CLAUSEs across 4 substandards (original 17 + 1 new CLAUSE-018 - 1 removed CLAUSE-013 + 5 from STD-009 + 2 new architectural CLAUSEs + splits from multi-concern CLAUSEs = 29).

---

## IV. Per-CLAUSE Specification

### T102-STD-004A — Core Structure & Lifecycle

---

#### CLAUSE-001: Canonical File Structure

**New ID**: `T102-STD-004-CLAUSE-001`
**Source**: Old CLAUSE-016 (Combined-File Canonical Structure), minus vocabulary subclause (moved to CLAUSE-008)
**Reasoning**: Canonical file structure is the foundational cross-cutting concern — it defines the shape every combined file MUST take. Placing it first in the Core substandard establishes the structural contract before any domain-specific CLAUSEs. Substandard sections added to the required structure per DEC002.

**Anchor normative statement**:

T102-STD-004-CLAUSE-001: Every combined standard-specification file MUST conform to the canonical structure defined by subclauses CLAUSE-001A through CLAUSE-001C.

**Subclauses**:

- **T102-STD-004-CLAUSE-001A (Required sections and order)** — Every combined file MUST contain these sections in order: (1) `# <STD-ID> — <Title>`, (2) `## Specification`, (3) `## Decision Record`, (4) `## References`, (5) `## Provenance`. The `## Specification` section MAY contain `###`-level substandard headings when the parent STD uses substandard architecture per CLAUSE-003.

- **T102-STD-004-CLAUSE-001B (Section semantics)** — `## Specification` contains normative `CLAUSE` items (enforceable language MUST follow the controlled vocabulary defined in CLAUSE-008). `## Decision Record` contains ADR bodies with informative rationale (current ADR listed first, superseded ADRs following per CLAUSE-023). `## References` and `## Provenance` are STD-level sections governing the entire file.

- **T102-STD-004-CLAUSE-001C (Anchor metadata lines)** — Non-heading metadata lines (e.g., explicit anchor lines in the form `{#anchor}`) MAY appear immediately after the `# <STD-ID> — <Title>` header and immediately after each ADR header line; this does not count as an additional required section.

---

#### CLAUSE-002: Specification Index

**New ID**: `T102-STD-004-CLAUSE-002`
**Source**: New (per SES002-DEC006)
**Reasoning**: With 29 CLAUSEs across 4 substandards, a navigational index is essential. The schema provides domain grouping at a glance via the Substandard column. Main CLAUSEs only — subclauses are discoverable by navigating to the parent CLAUSE.

**Anchor normative statement**:

T102-STD-004-CLAUSE-002: Every combined standard-specification file with more than 5 CLAUSEs SHOULD include a Specification Index conforming to subclauses CLAUSE-002A through CLAUSE-002C.

**Subclauses**:

- **T102-STD-004-CLAUSE-002A (Schema)** — The Specification Index MUST use the schema: `| # | Substandard | CLAUSE ID | Title | Description |`, where `#` is a sequential display number, `Substandard` identifies the domain grouping, and `Description` is a 1-line normative summary (~10-15 words).

- **T102-STD-004-CLAUSE-002B (Placement)** — The Specification Index MUST appear immediately after the `## Specification` heading and before the first substandard section heading (or before the first CLAUSE if no substandards are used).

- **T102-STD-004-CLAUSE-002C (Granularity)** — The Specification Index MUST list main CLAUSEs only. Subclauses MUST NOT be individually indexed (they are discoverable by navigating to the parent CLAUSE).

---

#### CLAUSE-003: Substandard Architecture

**New ID**: `T102-STD-004-CLAUSE-003`
**Source**: New (per SES002-DEC002/DEC003)
**Reasoning**: Substandards are a structural innovation that requires explicit governance. This CLAUSE defines what a substandard is, how it is identified, and the universal rule that every CLAUSE must belong to one. Following the IEEE "General clause" pattern, cross-cutting concerns live in a dedicated Core substandard rather than floating outside the modular structure.

**Anchor normative statement**:

T102-STD-004-CLAUSE-003: When a parent STD organizes its specification into substandards, the substandard architecture MUST conform to subclauses CLAUSE-003A through CLAUSE-003E.

**Subclauses**:

- **T102-STD-004-CLAUSE-003A (Definition)** — A substandard is an internal domain grouping within a parent STD combined file. Substandards organize CLAUSEs into coherent thematic domains for navigability and modular evolution.

- **T102-STD-004-CLAUSE-003B (ID format)** — Substandard IDs MUST follow the format `<STD-ID><CAPITAL_LETTER>` (e.g., `T102-STD-004A`). CLAUSEs within a substandard use the parent STD-ID in their CLAUSE-ID (e.g., `T102-STD-004-CLAUSE-001`), NOT the substandard ID.

- **T102-STD-004-CLAUSE-003C (Universal membership rule)** — Every CLAUSE in a substandard-enabled STD MUST belong to exactly one substandard. No CLAUSEs MAY exist outside substandard boundaries.

- **T102-STD-004-CLAUSE-003D (Registration)** — Substandards are internal structure. They MUST NOT be registered as separate rows in external registries (SPS STD Index, Concept STD Index). The parent STD maintains a single registry entry with description updated to reflect substandard domains.

- **T102-STD-004-CLAUSE-003E (Rendering)** — Each substandard MUST be rendered as a `###`-level heading under `## Specification`, using the format: `### <Substandard-ID> — <Domain Title>` (e.g., `### T102-STD-004A — Core Structure & Lifecycle`).

---

#### CLAUSE-004: Specification Lifecycle Stages

**New ID**: `T102-STD-004-CLAUSE-004`
**Source**: Old CLAUSE-017A (Specification Lifecycle Stages)
**Reasoning**: Lifecycle stages are a cross-cutting concern that applies to all CLAUSEs regardless of domain. Extracted from the former compound CLAUSE-017 to satisfy single-statement discipline.

**Anchor normative statement**:

T102-STD-004-CLAUSE-004: Specification content MUST progress through the lifecycle stages defined below.

**Subclauses**:

- **T102-STD-004-CLAUSE-004A (Stage definitions)** — The following lifecycle stages apply to specification content: `draft` (initial authoring; subject to change without formal review), `proposed` (submitted for review; normative language present but not yet binding), `accepted` (binding; normative language enforceable within declared scope), `amended` (accepted content modified via governed change process; prior version superseded), `deprecated` (no longer binding; retained for historical reference).

- **T102-STD-004-CLAUSE-004B (Status enum format)** — Lifecycle stage values MUST be rendered as lowercase strings wrapped in backticks (e.g., `proposed`, `accepted`, `deprecated`).

---

#### CLAUSE-005: Authority Derivation & Conformance Coupling

**New ID**: `T102-STD-004-CLAUSE-005`
**Source**: Old CLAUSE-017B/C/D (Authority Derivation Chain, Conformance Coupling Rule, No Normative Leakage)
**Reasoning**: Authority chain and conformance coupling are the enforcement mechanisms ensuring derivatives remain aligned with governing CLAUSEs. Extracted from former CLAUSE-017 for single-statement discipline.

**Anchor normative statement**:

T102-STD-004-CLAUSE-005: Derivative artifacts MUST maintain conformance with governing CLAUSEs per subclauses CLAUSE-005A through CLAUSE-005D.

**Subclauses**:

- **T102-STD-004-CLAUSE-005A (Authority derivation chain)** — Authority flows downward: Specification (CLAUSEs) -> Guideline (informative) -> Template (derivative). A Guideline MUST cite the governing CLAUSE(s) it derives from. A Template MUST conform to structural requirements prescribed by governing CLAUSEs and Guideline.

- **T102-STD-004-CLAUSE-005B (Conformance coupling rule)** — When a Specification CLAUSE is added, modified, or deprecated, all derivative artifacts (Guideline and Template) MUST be updated in the same changeset to maintain conformance.

- **T102-STD-004-CLAUSE-005C (No normative leakage)** — Derivatives MUST NOT introduce normative rules that are not traceable to a governing CLAUSE.

- **T102-STD-004-CLAUSE-005D (Derivative citation requirement)** — Each rule in a derivative artifact MUST include a citation to its governing CLAUSE(s) using the format `[per <CLAUSE-ID>]`.

---

#### CLAUSE-006: Anchor Stability

**New ID**: `T102-STD-004-CLAUSE-006`
**Source**: Old CLAUSE-007 (Anchor Title Stability), revised per AC008 audit
**Reasoning**: Anchor derivation rule corrected to match deployed scheme (ID + Title, not Title-only). Normalization rules made explicit.

**Anchor normative statement**:

T102-STD-004-CLAUSE-006: Anchors MUST be lower-kebab derived from `<ID> + <Title>` and MUST satisfy subclauses CLAUSE-006A through CLAUSE-006D.

**Subclauses**:

- **T102-STD-004-CLAUSE-006A (Normalization rules)** — Normalization MUST apply: spaces -> `-`; `&` -> `and`; strip punctuation; collapse repeated `-`. Result MUST be fully lowercase.

- **T102-STD-004-CLAUSE-006B (Stability across moves/splits)** — Anchors MUST remain stable across file moves and splits.

- **T102-STD-004-CLAUSE-006C (Title change migration)** — If Title changes, the old anchor MUST be kept unless an explicit migration is performed.

- **T102-STD-004-CLAUSE-006D (Phase 1 stability contract)** — Combined-file names and canonical paths SHOULD remain stable after migration completion. Anchors extracted from Concept remain stable within their combined file.

---

#### CLAUSE-007: Automation & Linting Checks

**New ID**: `T102-STD-004-CLAUSE-007`
**Source**: Old CLAUSE-015 (Automation & Linting Checks), updated for substandard structure
**Reasoning**: Updated check list to cover new structural requirements (specification index, substandard headings, ADR index, anchor derivation consistency).

**Anchor normative statement**:

T102-STD-004-CLAUSE-007: Authors SHOULD satisfy the automation and linting checks defined by subclauses CLAUSE-007A through CLAUSE-007F.

**Subclauses**:

- **T102-STD-004-CLAUSE-007A (Required headings)** — Combined file contains `## Specification` and `## Decision Record` headings in that order.

- **T102-STD-004-CLAUSE-007B (Nested ADR hygiene)** — Nested ADR body **Context** does not include a "Governed By" citation line.

- **T102-STD-004-CLAUSE-007C (STD-level sections)** — Combined file contains STD-level `## References` and `## Provenance` headings.

- **T102-STD-004-CLAUSE-007D (Index resolution)** — Every `Canonical Path` in an index resolves to an existing file under the designated standards directory per CLAUSE-015.

- **T102-STD-004-CLAUSE-007E (Anchor derivation consistency)** — Anchors follow the derivation and stability rules defined in CLAUSE-006.

- **T102-STD-004-CLAUSE-007F (Specification Index presence)** — Combined files with substandard architecture include a Specification Index per CLAUSE-002.

---

#### CLAUSE-008: Normative Vocabulary Guidance

**New ID**: `T102-STD-004-CLAUSE-008`
**Source**: Old CLAUSE-016D (Normative vocabulary guidance), revised per SES002-DEC012
**Reasoning**: Per DEC012, vocabulary guidance MUST reference `T102-CON-009` directly rather than redefining keyword families. Removes the incorrect implication that SHALL is a separate vocabulary from RFC 2119.

**Anchor normative statement**:

T102-STD-004-CLAUSE-008: Normative vocabulary in specification sections MUST conform to subclauses CLAUSE-008A through CLAUSE-008C.

**Subclauses**:

- **T102-STD-004-CLAUSE-008A (Normative keywords reference)** — Normative requirement keywords MUST be interpreted per `T102-CON-009 (Normative Keywords)` and RFC 2119. Keywords carrying normative meaning MUST be written in UPPERCASE.

- **T102-STD-004-CLAUSE-008B (Primary drafting vocabulary)** — A single primary drafting vocabulary MUST be used within a given STD specification section. BCP 14 keywords (`MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, `MAY`) are the preferred primary vocabulary for Phase 1.

- **T102-STD-004-CLAUSE-008C (Consistency rule)** — Mixing keyword styles within the same STD SHOULD be avoided unless explicitly justified as a legacy-compatibility exception.

---

### T102-STD-004B — STD Registry & Governance

---

#### CLAUSE-009: STD Semantics & Scope

**New ID**: `T102-STD-004-CLAUSE-009`
**Source**: Absorbed from STD-009-CLAUSE-001 (Semantics & Scope)
**Reasoning**: Defines the `STD` token type — its category, creation scope, reference scope, and invalid usage. Foundational for the entire registry domain.

**Anchor normative statement**:

T102-STD-004-CLAUSE-009: The `STD` token type MUST conform to the semantics and scope constraints defined by subclauses CLAUSE-009A through CLAUSE-009D.

**Subclauses**:

- **T102-STD-004-CLAUSE-009A (Category)** — `STD` is a normative `RID` token representing an enforceable standard.

- **T102-STD-004-CLAUSE-009B (Creation scope)** — `STD` MUST only be created at Program (`P`), Initiative (`I`), Epic (`E`), and Feature (`F`) scopes.

- **T102-STD-004-CLAUSE-009C (Reference scope)** — Artifacts at any scope MAY reference `STD`.

- **T102-STD-004-CLAUSE-009D (Invalid usage)** — `STD` MUST NOT be used for informative guidance (`IG`) or integration notes (`INT`).

---

#### CLAUSE-010: STD Adoption Contract

**New ID**: `T102-STD-004-CLAUSE-010`
**Source**: Absorbed from STD-009-CLAUSE-002 (Adoption Contract)
**Reasoning**: The adoption contract is the core mechanism linking a registry STD entry to its canonical normative specification. Preserved as-is from STD-009.

**Anchor normative statement**:

T102-STD-004-CLAUSE-010: Every `STD` entry MUST satisfy the adoption contract defined by subclauses CLAUSE-010A through CLAUSE-010C.

**Subclauses**:

- **T102-STD-004-CLAUSE-010A (Single canonical adopted spec)** — Every `STD` entry MUST declare exactly one `Adopts` reference.

- **T102-STD-004-CLAUSE-010B (Incorporation by reference)** — The adopted normative specification is incorporated by reference into the `STD`. The `STD` remains the authoritative RID-level handle; the adopted spec is the canonical text.

- **T102-STD-004-CLAUSE-010C (No rationale duplication)** — `STD` bodies MUST NOT contain alternatives analysis or lengthy trade-offs. These MUST be captured in ADRs.

---

#### CLAUSE-011: STD Precedence & Variance

**New ID**: `T102-STD-004-CLAUSE-011`
**Source**: STD-009-CLAUSE-003 (Precedence & Variance) + Old CLAUSE-010 (Precedence Conflicts Hierarchy), revised per SES002-DEC013
**Reasoning**: Per DEC013, precedence MUST reference `T102-STD-005-CLAUSE-003` for the full hierarchy and expand only for STD/CLAUSE/ADR tokens relevant to this standard. The mixed-scope hierarchy (Initiative STD > Epic ADR > ...) is removed in favor of a clean token-type hierarchy.

**Anchor normative statement**:

T102-STD-004-CLAUSE-011: Precedence and variance for STD-governed artifacts MUST follow subclauses CLAUSE-011A through CLAUSE-011D.

**Subclauses**:

- **T102-STD-004-CLAUSE-011A (Reference to full hierarchy)** — The full scope and category precedence hierarchy is defined in `T102-STD-005-CLAUSE-003 (Precedence & Hierarchy)`. This CLAUSE expands precedence specifically for STD-004-relevant tokens.

- **T102-STD-004-CLAUSE-011B (STD-scoped token hierarchy)** — Within the domain governed by this standard: `STD` (normative authority) > `CLAUSE` (inherits STD authority) > `ADR` (informative rationale). CLAUSEs derive their authority from the parent STD; ADRs are informative and MUST NOT override CLAUSE obligations.

- **T102-STD-004-CLAUSE-011C (Non-contradiction rule)** — ADRs and lower-scope artifacts MUST NOT contradict applicable `STD` obligations.

- **T102-STD-004-CLAUSE-011D (Variance contract)** — Any exception to an `STD` obligation MUST be recorded as a Variance ADR and MUST cite the overridden `STD` ID. The Variance ADR Contract requirements are governed by `T102-STD-005` (flagged for ST002 assessment; see INT-001).

---

#### CLAUSE-012: STD Index Schema & Column Definitions

**New ID**: `T102-STD-004-CLAUSE-012`
**Source**: STD-009-CLAUSE-004A (STD Index Schema) + STD-009-CLAUSE-004B (Column Guidelines) + Old CLAUSE-001 (partial — STD index aspects)
**Reasoning**: Merges the STD-specific index schema and column definitions from STD-009 with the index governance from old CLAUSE-001. ADR-specific index schema is now in CLAUSE-023 (T102-STD-004D).

**Anchor normative statement**:

T102-STD-004-CLAUSE-012: STD index tables MUST conform to the schema and column definitions defined by subclauses CLAUSE-012A through CLAUSE-012C.

**Subclauses**:

- **T102-STD-004-CLAUSE-012A (STD Index Schema)** — Each scope MUST maintain a `STD` index table using this schema: `| STD ID | Title | Status | Owner | Effective | Supersedes | Adopts | Verification | Governed By | Reference |`

- **T102-STD-004-CLAUSE-012B (Column definitions)** — `STD ID` MUST follow `T102-STD-005-CLAUSE-001`. `Title` MUST be bold and follow title constraints. `Status` MUST use lowercase backtick-wrapped enums per CLAUSE-004B. `Adopts` MUST contain exactly one full reference to the canonical adopted normative specification. `Effective` MUST be an ISO-8601 date `YYYY-MM-DD` or `—` if not yet set. `Verification` MUST describe (a) mechanism, (b) what is checked, and (c) pass/fail evidence. `Governed By` MUST list the governing basis (meta-governance). `Reference` MUST contain ONLY `RID`-category IDs per `T102-STD-005-CLAUSE-002` and MUST NOT include `DRID`/`CLAUSE` IDs.

- **T102-STD-004-CLAUSE-012C (Phase 1 index granularity)** — Phase 1 index granularity is the combined file as a whole (no anchor addressing required in indexes).

---

#### CLAUSE-013: STD Body Construction & Conciseness

**New ID**: `T102-STD-004-CLAUSE-013`
**Source**: Absorbed from STD-009-CLAUSE-004C (Body Construction) + STD-009-CLAUSE-004D (Conciseness)
**Reasoning**: Defines how STD bodies are authored — the primary obligation sentence format and the MVC pattern. Combined with conciseness targets for coherent authoring guidance.

**Anchor normative statement**:

T102-STD-004-CLAUSE-013: STD bodies MUST conform to the construction and conciseness requirements defined by subclauses CLAUSE-013A through CLAUSE-013C.

**Subclauses**:

- **T102-STD-004-CLAUSE-013A (Primary obligation sentence)** — STD bodies MUST include a primary obligation sentence in the format: `* **<SID>-STD-### (<Title>)** — <Normative obligation sentence>`. The obligation sentence MUST answer "WHAT must be true" at a stable, scope-wide level.

- **T102-STD-004-CLAUSE-013B (Minimum Viable Conformance)** — MVC items (recommended; max 5) MUST be written as an ordered list. MVC items SHOULD cite adopted-spec clause IDs where possible. MVC items MUST NOT introduce new obligations beyond the adopted specification.

- **T102-STD-004-CLAUSE-013C (Conciseness targets)** — STD bodies SHOULD target <200 words when feasible (excluding tables). Pragmatic exception: if `Adopts = —` is explicitly intentional, the STD body MAY extend (target <=300 words) to remain actionable.

---

#### CLAUSE-014: STD Drift Controls & Lifecycle Coherence

**New ID**: `T102-STD-004-CLAUSE-014`
**Source**: STD-009-CLAUSE-004E (Drift Controls) + Old CLAUSE-008 (Lifecycle Coherence)
**Reasoning**: Drift controls (from STD-009) and lifecycle coherence (from old STD-004) both address the same concern: keeping STD content aligned with its governing sources and adopted specs. Merging them eliminates redundancy.

**Anchor normative statement**:

T102-STD-004-CLAUSE-014: STD content MUST remain aligned with adopted specifications and governing STDs per subclauses CLAUSE-014A through CLAUSE-014D.

**Subclauses**:

- **T102-STD-004-CLAUSE-014A (No duplication)** — STD bodies MUST avoid duplicating detailed rules; the adopted normative specification is the single canonical source of truth.

- **T102-STD-004-CLAUSE-014B (Adopted spec sync)** — If an adopted specification is updated in a way that changes conformance expectations, the corresponding STD body (including MVC) MUST be updated in the same changeset.

- **T102-STD-004-CLAUSE-014C (SSOT sync)** — When `STD` bodies are copied into SSOT artifacts (e.g., `sps`), those SSOT copies MUST be updated in the same changeset whenever the authoritative STD body changes.

- **T102-STD-004-CLAUSE-014D (Governing STD coherence)** — When a governing STD changes status or is superseded, affected combined files MUST update the nested ADR Context wording, add prior governing IDs to References, and perform this update in the next modification or in a dedicated governance sync changeset.

---

#### CLAUSE-015: STD Placement & Directory Requirements

**New ID**: `T102-STD-004-CLAUSE-015`
**Source**: Old CLAUSE-002 (Placement Standards), revised per SES002-DEC009
**Reasoning**: Per DEC009, the designated standards directory MUST be initiative-nonspecific (`<SID>` placeholder, not hardcoded to T102). SPS/Concept section-title prescriptions removed (STD-004 governs combined file placement, not SSOT section titles).

**Anchor normative statement**:

T102-STD-004-CLAUSE-015: Combined standard-specification files MUST be placed according to subclauses CLAUSE-015A through CLAUSE-015C.

**Subclauses**:

- **T102-STD-004-CLAUSE-015A (Designated standards directory)** — Combined standard-specification files MUST live under the designated standards directory: `prompt/artifacts/tasks/<SID>/consultant/standards/`.

- **T102-STD-004-CLAUSE-015B (Index-only hub boundary)** — Index artifacts (e.g., Concept/SPS indexes) MUST reference combined files via the `Canonical Path` column and MUST NOT embed the combined-file body as a substitute for that reference.

- **T102-STD-004-CLAUSE-015C (Consistency requirement)** — Placement MUST follow established artifact section numbering without local deviations.

---

#### CLAUSE-016: STD Status Management

**New ID**: `T102-STD-004-CLAUSE-016`
**Source**: Old CLAUSE-009 (Status Management), revised per SES002-DEC008
**Reasoning**: Per DEC008, all status enums MUST be lowercase wrapped in backticks. Enum format now references CLAUSE-004B for consistency.

**Anchor normative statement**:

T102-STD-004-CLAUSE-016: Status and supersession metadata for combined files MUST be maintained per subclauses CLAUSE-016A through CLAUSE-016C.

**Subclauses**:

- **T102-STD-004-CLAUSE-016A (Lifecycle)** — Lifecycle: `proposed` -> `accepted` -> `deprecated`. Status enum values MUST conform to the format defined in CLAUSE-004B (lowercase, backtick-wrapped).

- **T102-STD-004-CLAUSE-016B (Supersedes handling)** — Superseded IDs MUST be captured in the **Supersedes** column and, where applicable, referenced in body text.

- **T102-STD-004-CLAUSE-016C (Effective semantics)** — `Effective` MUST be an ISO-8601 date `YYYY-MM-DD` or `—` if not yet set. For specification lifecycle stages governing CLAUSE content evolution, see CLAUSE-004.

---

#### CLAUSE-017: Migration Tolerance

**New ID**: `T102-STD-004-CLAUSE-017`
**Source**: Absorbed from STD-009-CLAUSE-005 (Migration Tolerance)
**Reasoning**: Migration tolerance mechanisms (alias windows, GDR blocking, sunset) are registry governance concerns. Absorbed unchanged from STD-009.

**Anchor normative statement**:

T102-STD-004-CLAUSE-017: Migration from legacy governance identifiers MUST follow subclauses CLAUSE-017A through CLAUSE-017C.

**Subclauses**:

- **T102-STD-004-CLAUSE-017A (Alias window)** — During migration, legacy `GDR` IDs MAY be treated as aliases of their replacement `STD` IDs for enforcement.

- **T102-STD-004-CLAUSE-017B (No new GDR)** — New `GDR` creation MUST be blocked after the migration cutoff milestone/date.

- **T102-STD-004-CLAUSE-017C (Sunset)** — Alias support MUST be removed after the migration completion milestone/date.

---

### T102-STD-004C — Specification Authoring

---

#### CLAUSE-018: CLAUSE Construction Requirements

**New ID**: `T102-STD-004-CLAUSE-018`
**Source**: Old CLAUSE-005 (Specification Clauses) — core construction requirements
**Reasoning**: CLAUSE construction is the fundamental authoring discipline. Separated from ordering and rendering concerns for single-statement clarity. Retains normative reference to STD-005-CLAUSE-005D and the single-statement discipline requirement.

**Anchor normative statement**:

T102-STD-004-CLAUSE-018: Specification CLAUSEs in combined standard-specification files MUST be constructed per subclauses CLAUSE-018A through CLAUSE-018E.

**Subclauses**:

- **T102-STD-004-CLAUSE-018A (Normative reference)** — `CLAUSE` token type construction and semantics MUST follow `T102-STD-005-CLAUSE-005D (Specification Clause Semantics)`.

- **T102-STD-004-CLAUSE-018B (Clause item format)** — Each clause item MUST be rendered as: `n) **<CLAUSE-ID> (<Title>)**`. `<CLAUSE-ID>` MUST conform to `T102-STD-005-CLAUSE-005D`.

- **T102-STD-004-CLAUSE-018C (Single-statement discipline)** — Each clause MUST be a single primary normative statement. If a parent clause contains multiple distinct obligations, those obligations MUST be decomposed into named subclauses per `T102-STD-005-CLAUSE-005D`.

- **T102-STD-004-CLAUSE-018D (Title conventions)** — Clause Titles MUST follow the title conventions defined in `T102-STD-005-CLAUSE-001`.

- **T102-STD-004-CLAUSE-018E (Non-duplication constraint)** — Combined standard-specification files MUST NOT redefine the syntax, scope validity, or semantic authority of `CLAUSE` IDs; those are defined in `T102-STD-005-CLAUSE-005D`.

---

#### CLAUSE-019: CLAUSE Ordering

**New ID**: `T102-STD-004-CLAUSE-019`
**Source**: Old CLAUSE-005 (Specification Clauses) — ordering rules
**Reasoning**: Ordering is a distinct concern from construction. CLAUSE IDs are sequential within the parent STD (not within each substandard), and subclauses immediately follow their parent.

**Anchor normative statement**:

T102-STD-004-CLAUSE-019: CLAUSE ordering within a combined standard-specification file MUST satisfy subclauses CLAUSE-019A and CLAUSE-019B.

**Subclauses**:

- **T102-STD-004-CLAUSE-019A (Sequential numbering)** — `CLAUSE` IDs MUST be sequential within the parent STD in the order they appear across the Specification section (`001`, `002`, `003`, ...). When substandards are used, numbering is continuous across substandard boundaries.

- **T102-STD-004-CLAUSE-019B (Subclause adjacency)** — Subclauses MUST immediately follow their parent clause.

---

#### CLAUSE-020: Subclause Rendering

**New ID**: `T102-STD-004-CLAUSE-020`
**Source**: Old CLAUSE-005 (Specification Clauses) — rendering rules, revised per SES002-DEC015
**Reasoning**: Per DEC015, all subclauses MUST use bold format per T102-STD-005-CLAUSE-001: `- **<CLAUSE-ID> (<Title>)** — <statement>`. The prior R2 proposal's backtick-wrapped format was a systemic rendering error that this CLAUSE explicitly corrects.

**Anchor normative statement**:

T102-STD-004-CLAUSE-020: Subclause rendering in combined standard-specification files MUST follow subclauses CLAUSE-020A and CLAUSE-020B.

**Subclauses**:

- **T102-STD-004-CLAUSE-020A (Bold format requirement)** — Subclauses MUST be rendered as nested bullet items under the parent clause using the format: `- **<CLAUSE-ID> (<Title>)** — <normative statement>`. This follows the markdown construction defined in `T102-STD-005-CLAUSE-001`.

- **T102-STD-004-CLAUSE-020B (Prohibited format)** — Subclauses MUST NOT use backtick-wrapped format (e.g., `` `T102-STD-004-CLAUSE-001A (Title)` ``). Backtick wrapping is reserved for inline code references, not for subclause rendering.

---

#### CLAUSE-021: Normative/Informative Boundary Hygiene

**New ID**: `T102-STD-004-CLAUSE-021`
**Source**: Old CLAUSE-018 (Normative/Informative Boundary Hygiene), from R2-Enhanced / RES-007
**Reasoning**: RES-007 identified boundary hygiene as a Critical gap. Combined-file architecture is industry-aligned but boundary contamination is already observable in derivatives. This CLAUSE prevents normative language from "leaking" into informative sections.

**Anchor normative statement**:

T102-STD-004-CLAUSE-021: Combined standard-specification files MUST enforce a clear boundary between normative and informative content per subclauses CLAUSE-021A through CLAUSE-021D.

**Subclauses**:

- **T102-STD-004-CLAUSE-021A (Normative section authority)** — The `## Specification` section is the authoritative normative surface of a combined file. The `## Decision Record` section is informative rationale and MUST NOT create new obligations.

- **T102-STD-004-CLAUSE-021B (Informative section keyword hygiene)** — Informative sections (including `## Decision Record`) MUST NOT use BCP 14 keywords in uppercase (`MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, `MAY`) to express requirements. If an informative section needs to refer to a normative requirement, it MUST do so by citing the governing CLAUSE reference and/or quoting the normative text as a quotation.

- **T102-STD-004-CLAUSE-021C (Normative/informative labeling rule)** — If any non-Specification section contains normative requirements, that section MUST be explicitly labeled as normative and the governing CLAUSE(s) MUST be identified.

- **T102-STD-004-CLAUSE-021D (Derivative boundary alignment)** — Any derivative artifact that describes boundary hygiene expectations MUST cite this CLAUSE and MUST NOT introduce additional boundary rules beyond what is governed here.

---

#### CLAUSE-022: Referencing & Non-Duplication

**New ID**: `T102-STD-004-CLAUSE-022`
**Source**: Old CLAUSE-005 (Specification Clauses) — referencing + non-duplication rules
**Reasoning**: Referencing patterns and the non-duplication constraint are complementary concerns — both govern how CLAUSEs relate to external standards and to each other.

**Anchor normative statement**:

T102-STD-004-CLAUSE-022: CLAUSE referencing and non-duplication MUST follow subclauses CLAUSE-022A and CLAUSE-022B.

**Subclauses**:

- **T102-STD-004-CLAUSE-022A (CLAUSE referencing)** — Other artifacts MAY reference specific Specification CLAUSEs using the formal format defined in `T102-STD-005-CLAUSE-004 (Reference Semantics)`.

- **T102-STD-004-CLAUSE-022B (Non-duplication constraint)** — Combined standard-specification files MUST NOT redefine the syntax, scope validity, or semantic authority of `CLAUSE` IDs; those are defined in `T102-STD-005-CLAUSE-005D`.

---

### T102-STD-004D — Decision Record Authoring

---

#### CLAUSE-023: ADR Index Schema

**New ID**: `T102-STD-004-CLAUSE-023`
**Source**: Old CLAUSE-001 (DR Index Schemas) — ADR-specific parts, revised per SES002-DEC004
**Reasoning**: Per DEC004, ADR storage uses multiple ADRs in-file with current-first ordering. The ADR Index schema records all ADRs (current + superseded) for audit trail visibility. This is the ADR-specific counterpart to CLAUSE-012 (STD Index Schema).

**Anchor normative statement**:

T102-STD-004-CLAUSE-023: ADR index tables within combined standard-specification files MUST conform to subclauses CLAUSE-023A through CLAUSE-023D.

**Subclauses**:

- **T102-STD-004-CLAUSE-023A (ADR Index Schema)** — The ADR Index MUST use the schema: `| ADR ID | Title | Status | Supersedes | Date |`.

- **T102-STD-004-CLAUSE-023B (Column definitions)** — `ADR ID` MUST follow `T102-STD-005-CLAUSE-005F` construction format (`<STD-ID>-ADR-###`). `Title` MUST follow title conventions per `T102-STD-005-CLAUSE-001`. `Status` MUST use lowercase backtick-wrapped enums per CLAUSE-004B (e.g., `accepted`, `superseded`). `Supersedes` MUST list superseded ADR IDs or `—`. `Date` MUST be ISO-8601 date `YYYY-MM-DD`.

- **T102-STD-004-CLAUSE-023C (Current-first ordering)** — ADR bodies in the `## Decision Record` section MUST be ordered with the current (most recent `accepted`) ADR first, followed by superseded ADRs in reverse chronological order.

- **T102-STD-004-CLAUSE-023D (Multiple ADRs in-file)** — Combined files MAY contain multiple ADR bodies (current + superseded). Superseded ADR bodies are retained for audit trail purposes. Only one ADR MAY have `accepted` status at any time; all others MUST be `superseded`.

---

#### CLAUSE-024: ADR Entry Creation Workflow

**New ID**: `T102-STD-004-CLAUSE-024`
**Source**: Old CLAUSE-003 (Entry Creation Workflow), revised for normative language
**Reasoning**: Converted procedural imperatives to explicit MUST requirements while preserving workflow structure. File naming convention made explicit as a governing subclause.

**Anchor normative statement**:

T102-STD-004-CLAUSE-024: To create a new combined standard-specification file and its corresponding index entry, authors MUST satisfy subclauses CLAUSE-024A through CLAUSE-024F.

**Subclauses**:

- **T102-STD-004-CLAUSE-024A (File naming convention)** — Combined standard-specification filenames MUST follow `<STD-ID>_<title-slug>.md` where `<title-slug>` is lowercase, spaces -> `-`, non-alphanumeric characters removed/replaced with `-`, and repeated `-` collapsed.

- **T102-STD-004-CLAUSE-024B (Create index row)** — Authors MUST add a new row to the appropriate STD index table using the schema per CLAUSE-012.

- **T102-STD-004-CLAUSE-024C (Assign ID)** — Authors MUST assign the next sequential STD ID for that scope.

- **T102-STD-004-CLAUSE-024D (Create combined file)** — Authors MUST create a combined standard-specification file at the canonical path under the designated standards directory (per CLAUSE-015A) using the standard-specification template, applying CLAUSE entries under `## Specification` and DR body structure under `## Decision Record` per CLAUSE-025.

- **T102-STD-004-CLAUSE-024E (References conformance)** — Authors MUST ensure References follow `T102-STD-005-CLAUSE-004 (Reference Semantics)`.

- **T102-STD-004-CLAUSE-024F (Canonical Path population)** — Authors MUST populate the Canonical Path column (where applicable) in the index row with the full repo-relative path to the combined file.

---

#### CLAUSE-025: DR Body Template

**New ID**: `T102-STD-004-CLAUSE-025`
**Source**: Old CLAUSE-004 (DR Body Template), enhanced per SES002-DEC010
**Reasoning**: Per DEC010, CLAUSE-004 (now CLAUSE-025) must specify per-subheading content requirements AND format — each subheading gets its own subclause with semantic + rendering requirements. This makes the template extensible for future subheading-specific schemas.

**Anchor normative statement**:

T102-STD-004-CLAUSE-025: Nested ADR bodies in combined standard-specification files MUST conform to subclauses CLAUSE-025A through CLAUSE-025H.

**Subclauses**:

- **T102-STD-004-CLAUSE-025A (Header format)** — Nested ADR header MUST be rendered as: `* **<STD-ID>-ADR-### (<Title>)** {#<anchor>}`.

- **T102-STD-004-CLAUSE-025B (Required subheadings)** — Nested ADR body MUST include these subheadings: **Context**, **Decision**, **Alternatives Considered**, **Consequences**.

- **T102-STD-004-CLAUSE-025C (Body formatting rules)** — Main bold headings (e.g., `* **Context**`) MUST be preceded by two newlines. Content MUST start on a new line and be indented under the heading with no blank line in between.

- **T102-STD-004-CLAUSE-025D (Section placement)** — In combined standard-specification files, the DR body MUST live under `## Decision Record`. References and Provenance are STD-level sections (per CLAUSE-001A).

- **T102-STD-004-CLAUSE-025E (Context content requirements)** — The **Context** subheading MUST state: the motivating problem and the gap the decision resolves. Context MAY use shorthand IDs for traceability but MUST NOT include a formal "Governed By" citation line (formal citations belong in `## References`).

- **T102-STD-004-CLAUSE-025F (Decision content requirements)** — The **Decision** subheading MUST state: what is adopted or changed, and who owns the decision.

- **T102-STD-004-CLAUSE-025G (Alternatives Considered content & format)** — The **Alternatives Considered** subheading MUST be a bulleted list. Each bullet MUST include the alternative and a clear rejection rationale.

- **T102-STD-004-CLAUSE-025H (Consequences content & format)** — The **Consequences** subheading MUST use `(+)`, `(±)`, `(-)` prefix bullets to categorize impacts. Consequences MUST cover stated impact categories relevant to the decision scope.

---

#### CLAUSE-026: Cross-Artifact Linking Patterns

**New ID**: `T102-STD-004-CLAUSE-026`
**Source**: Old CLAUSE-006 (Cross-Artifact Linking Patterns)
**Reasoning**: Each linking pattern is now a named subclause for lintability and precise reference.

**Anchor normative statement**:

T102-STD-004-CLAUSE-026: Combined standard-specification files MUST satisfy the cross-artifact linking patterns defined by subclauses CLAUSE-026A through CLAUSE-026D.

**Subclauses**:

- **T102-STD-004-CLAUSE-026A (STD internal DR pattern)** — A combined standard-specification file MUST contain its decision record internally under `## Decision Record` using the nested ADR format from CLAUSE-025.

- **T102-STD-004-CLAUSE-026B (Decision record context pattern)** — The nested ADR **Context** SHOULD state the motivating problem in narrative form and MAY use shorthand IDs for traceability.

- **T102-STD-004-CLAUSE-026C (Context/References boundary)** — The nested ADR **Context** MUST NOT use a formal "Governed By" citation line. Formal citations belong in the STD-level `## References` section.

- **T102-STD-004-CLAUSE-026D (Index to combined file linkage)** — Concept/SPS index tables MUST link to combined files via full repo-relative Canonical Path (per CLAUSE-012/CLAUSE-023); Phase 1 links at file granularity.

---

#### CLAUSE-027: ADR Consequences Scope

**New ID**: `T102-STD-004-CLAUSE-027`
**Source**: Old CLAUSE-011 (Consequences Scope Requirements), revised per SES002-DEC014
**Reasoning**: Per DEC014, "STD Consequences" is removed — STDs do not have consequences sections (this was STD-009 drift). This CLAUSE now applies only to ADR consequences within nested decision records.

**Anchor normative statement**:

T102-STD-004-CLAUSE-027: Consequences sections in nested ADR bodies SHOULD cover the scope defined by CLAUSE-027A.

**Subclauses**:

- **T102-STD-004-CLAUSE-027A (ADR Consequences scope)** — ADR **Consequences** SHOULD cover: quality trade-offs; constraints introduced; operational effects; debt/risks. The `(+)`, `(±)`, `(-)` prefix format defined in CLAUSE-025H MUST be used.

---

#### CLAUSE-028: References & Provenance

**New ID**: `T102-STD-004-CLAUSE-028`
**Source**: Old CLAUSE-012 (References & Provenance)
**Reasoning**: Subclauses separate the References and Provenance requirements for precision.

**Anchor normative statement**:

T102-STD-004-CLAUSE-028: Combined files MUST satisfy the References and Provenance requirements defined by subclauses CLAUSE-028A and CLAUSE-028B.

**Subclauses**:

- **T102-STD-004-CLAUSE-028A (References)** — References MUST use the formal reference style defined in `T102-STD-005-CLAUSE-004 (Reference Semantics)`.

- **T102-STD-004-CLAUSE-028B (Provenance)** — Provenance MUST list repo-relative paths (and MAY include higher-level narrative context). No raw URLs.

---

#### CLAUSE-029: Decision Promotion Workflow

**New ID**: `T102-STD-004-CLAUSE-029`
**Source**: Old CLAUSE-014 (Decision Promotion Workflow), revised per SES002-DEC011
**Reasoning**: Per DEC011, scope reduced to STD/CLAUSE/ADR tokens only. RES/IG token-specific promotion details belong in `T102-STD-005` (flagged as INT-002 for ST002).

**Anchor normative statement**:

T102-STD-004-CLAUSE-029: Promotion of decision content into Standards SHOULD follow subclauses CLAUSE-029A through CLAUSE-029C.

**Subclauses**:

- **T102-STD-004-CLAUSE-029A (STD promotion criteria)** — Authors SHOULD promote stable, cross-cutting, or long-lived patterns into formal `STD` records when: (a) the pattern affects multiple artifacts or features, or (b) the pattern requires explicit governance (ownership, status, supersedes) beyond implementation detail. When promoted, the `STD` MUST contain a nested ADR for rationale per CLAUSE-025.

- **T102-STD-004-CLAUSE-029B (CLAUSE promotion)** — When a normative obligation in a combined file warrants addressable precision, it SHOULD be formalized as a named CLAUSE (or subclause) per CLAUSE-018.

- **T102-STD-004-CLAUSE-029C (Traceability)** — Specifications SHOULD reference governing research and guidance in **Provenance** and **References** (per CLAUSE-028), rather than duplicating detailed patterns. Token-specific promotion workflows for `RES` and `IG` tokens are governed by `T102-STD-005`.

---

## V. ADR-002 (Rationale for Redesign)

This section drafts the full T102-STD-004-ADR-002 body that will replace ADR-001 as the current decision record.

### ADR Index (post-implementation)

| ADR ID | Title | Status | Supersedes | Date |
|:--|:--|:--|:--|:--|
| T102-STD-004-ADR-002 | Combined Authoring & Governance Standard | `accepted` | ADR-001 | 2026-02-15 |
| T102-STD-004-ADR-001 | Specification Standard & Guideline | `superseded` | — | 2026-02-08 |

### ADR-002 Body

* **T102-STD-004-ADR-002 (Combined Authoring & Governance Standard)** {#t102-std-004-adr-002-combined-authoring-and-governance-standard}

  * **Context**
    T102-STD-004 underwent significant evolution: from ADR-contains-CLAUSE to STD-contains-CLAUSE to R2 refactor to RES-007 integration. A self-compliance audit (AC008) identified systemic non-conformance: multi-obligation clauses without subclauses, anchor derivation mismatch, and derivative normative leakage. The R2 refactor (AC008-SES001-DEC001) addressed structural discipline but maintained STD-004/STD-009 separation.

    AC009-GATE-001 QA review revealed that the R2 proposal itself contained systemic issues: wrong subclause format (backtick-wrapped instead of bold), missing specification index, content reduction in CLAUSE-004, extreme drift between STD-004 and STD-009 causing hallucination in agentic LLM authoring, and scope misalignment across multiple CLAUSEs. The Client recommended merging STD-009 into STD-004 (SES002-DEC001) and introducing substandard architecture (SES002-DEC002) as the structural investment to resolve these issues comprehensively.

    Industry benchmarking (RES-007) validated the combined-file architecture and fine-grained subclause discipline while identifying boundary hygiene as a critical gap. The STD-004/STD-009 merge decision overrides the RES-007 recommendation to keep them separate, based on the Client's direct experience with agentic LLM drift — a practical concern that the research methodology did not specifically evaluate.

  * **Decision**
    Merge T102-STD-009 into T102-STD-004 and reorganize the merged content into 4 substandards: T102-STD-004A (Core Structure and Lifecycle), T102-STD-004B (STD Registry and Governance), T102-STD-004C (Specification Authoring), T102-STD-004D (Decision Record Authoring). Full CLAUSE resequencing with 29 CLAUSEs across the 4 substandards. Multiple ADRs in-file with current-first ordering. ADR-001 preserved as superseded for audit trail. STD-009 deprecated in SPS. Decision owner: Client.

  * **Alternatives Considered**
    - Keep STD-004/STD-009 separate with interface contracts (RES-007 recommendation) — rejected by Client due to persistent drift and context loss for agentic LLM. The interface approach requires LLM agents to reliably navigate cross-file boundaries, which has proven unreliable in practice.
    - Keep flat CLAUSE numbering with informative domain headers (Option A from SES002) — rejected in favor of substandards with full resequencing (upfront investment) because domain headers alone do not enforce CLAUSE membership and leave the navigability problem partially unsolved.
    - Allow floating CLAUSEs outside substandards for cross-cutting concerns — rejected per IEEE "General clause" pattern. A dedicated Core substandard (T102-STD-004A) holds cross-cutting CLAUSEs, maintaining the universal rule that every CLAUSE belongs to a substandard.
    - Update ADR in-place with git history for superseded versions — rejected due to git history unreliability (force push, squash, migration), non-navigability by non-technical stakeholders, and Phase 2 ADR extraction planning.

  * **Consequences**
    (+) Single file eliminates STD-004/STD-009 drift; agentic LLM context is consolidated.
    (+) Substandard architecture provides clear domain grouping for 29 CLAUSEs; navigability via Specification Index.
    (+) Multiple ADRs in-file preserve full audit trail; prepares for Phase 2 ADR extraction.
    (+) All QA corrections applied: bold subclause format, lowercase status enums, per-subheading content requirements, initiative-nonspecific directory, vocabulary reference to CON-009.
    (+) Industry-aligned boundary hygiene (CLAUSE-021) prevents normative leakage.
    (+-) Larger blast radius: all 8 SPS STD rows referencing STD-009 need updating; guideline/template/SPS derivatives updated in same changeset.
    (+-) STD-005-CLAUSE-005F needs amendment for multiple ADRs in-file (flagged as INT-003 for ST002).
    (-) Full CLAUSE resequencing breaks all existing CLAUSE references (one-time migration cost).
    (-) STD-009 deprecation requires Concept STD Index update and reference propagation (deferred to ST002).

---

## VI. Derivative Update Specification

### VI.A. Guideline (`prompt/templates/consultant/standards/guideline_standard_specs.md`)

All citation updates needed:

| Current Citation | Updated Citation | Reason |
|:--|:--|:--|
| `[per T102-STD-004-CLAUSE-002]` (canonical location) | `[per T102-STD-004-CLAUSE-015]` | Old CLAUSE-002 (Placement) resequenced to CLAUSE-015 |
| `[per T102-STD-004-CLAUSE-001, CLAUSE-003]` (file naming) | `[per T102-STD-004-CLAUSE-024A]` | File naming convention now explicit in CLAUSE-024A |
| `[per T102-STD-004-CLAUSE-016]` (canonical structure) | `[per T102-STD-004-CLAUSE-001]` | Old CLAUSE-016 (Canonical Structure) resequenced to CLAUSE-001 |
| `[per T102-STD-004-CLAUSE-005]` (specification section) | `[per T102-STD-004-CLAUSE-018]` | Old CLAUSE-005 (Spec Clauses) resequenced to CLAUSE-018 |
| `[per T102-STD-004-CLAUSE-004]` (decision record section) | `[per T102-STD-004-CLAUSE-025]` | Old CLAUSE-004 (DR Body Template) resequenced to CLAUSE-025 |
| `[per T102-STD-004-CLAUSE-012, CLAUSE-016]` (references/provenance) | `[per T102-STD-004-CLAUSE-028, CLAUSE-001]` | Old CLAUSE-012 resequenced to CLAUSE-028; old CLAUSE-016 to CLAUSE-001 |
| `[per T102-STD-004-CLAUSE-001]` (indexing) | `[per T102-STD-004-CLAUSE-023]` (ADR index) or `[per T102-STD-004-CLAUSE-012]` (STD index) | Old CLAUSE-001 split into CLAUSE-012 (STD) and CLAUSE-023 (ADR) |
| `[per T102-STD-004-CLAUSE-017]` (conformance coupling) | `[per T102-STD-004-CLAUSE-005]` | Old CLAUSE-017 resequenced to CLAUSE-005 |

Additional guideline changes:
- Update canonical directory to use `<SID>` placeholder per DEC009: `prompt/artifacts/tasks/<SID>/consultant/standards/`
- Add substandard architecture guidance (reference CLAUSE-003)
- Add boundary hygiene guidance (reference CLAUSE-021)
- Add ADR Index guidance (reference CLAUSE-023) for multiple ADRs in-file
- Add Specification Index guidance (reference CLAUSE-002) for navigational index

### VI.B. Template (`prompt/templates/consultant/standards/template_standard_specs.md`)

Structural changes:
- Add `### Specification Index` placeholder section after `## Specification`
- Add `### <STD-ID><X> — <Domain Title>` substandard heading placeholders (with note: "include only if substandard architecture is used")
- Add `### ADR Index` section under `## Decision Record` before the ADR body
- Update CLAUSE template to show bold subclause format: `- **<STD-ID>-CLAUSE-###A (<Title>)** — <statement>`
- Add anchor metadata line placeholder after `# <STD-ID> — <Title>` to match CLAUSE-001C

### VI.C. SPS (`prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md`)

**STD-004 row changes**:
- Update `Title`: **Specification Standard & Guideline** (no change — retitle deferred to ST002)
- Update `Adopts`: `—` -> update if self-adoption formalized
- Update `Verification`: rewrite to reference new CLAUSE structure: "CI/Lint + Review MUST verify: canonical combined-file structure (`CLAUSE-001`), specification index (`CLAUSE-002`), substandard architecture (`CLAUSE-003`), subclause format (`CLAUSE-020`), boundary hygiene (`CLAUSE-021`), and nested ADR records (`CLAUSE-023`, `CLAUSE-025`)."
- Update `Reference`: remove `T102-STD-009 (Governance Standards Model)` (now absorbed)

**STD-009 row changes**:
- Update `Status`: `proposed` -> `deprecated`
- Add note: "Superseded by T102-STD-004. All STD-009 CLAUSEs absorbed into T102-STD-004B."

**STD-004 body (MVC) rewrite**:
```
* **T102-STD-004 (Specification Standard & Guideline)** — The project SHALL use the combined standard-specification file model, substandard architecture, STD registry governance, and decision record authoring rules defined in the adopted normative specification.
  - **Minimum Viable Conformance**:
    1) Conform to canonical file structure and substandard headings (`T102-STD-004-CLAUSE-001`, `CLAUSE-003`).
    2) Follow STD index schema and column definitions (`T102-STD-004-CLAUSE-012`).
    3) Create/update combined files using the workflow and DR body template (`T102-STD-004-CLAUSE-024`, `CLAUSE-025`).
    4) Maintain stable anchors per the anchor stability rules (`T102-STD-004-CLAUSE-006`).
    5) Enforce normative/informative boundary hygiene (`T102-STD-004-CLAUSE-021`).
```

**STD-009 body update**:
```
* **T102-STD-009 (Governance Standards Model)** — `[deprecated]` Superseded by `T102-STD-004`. All STD registry governance CLAUSEs (semantics, adoption contract, precedence, authoring, migration) are absorbed into `T102-STD-004B (STD Registry & Governance)`.
```

**All other STD rows referencing STD-009**: Update `Reference` column from `T102-STD-009 (Governance Standards Model)` to `T102-STD-004 (Specification Standard & Guideline)`. Affects: STD-001, STD-002, STD-003, STD-005, STD-006, STD-007, STD-008 (7 rows), plus any T102B-STD rows.

---

## VII. STD-005 Integration Issues Register

These issues were identified during SES002 dialogue as impacting T102-STD-005 but outside AC009 scope. They are documented here for ST002 pickup with full context.

| # | Issue | STD-005 Impact | Source |
|:--|:--|:--|:--|
| INT-001 | CLAUSE-013 (Variance ADR Contract) removed from STD-004 | STD-005 must assess whether to absorb the Variance ADR Contract as a new clause (extends CLAUSE-003 variance mechanism with contract requirements: Variance From, Rationale, Scope Impact, Lifecycle) | SES002-DEC005 |
| INT-002 | CLAUSE-014 scope reduced to STD/CLAUSE/ADR tokens | STD-005 should assess absorbing RES/IG promotion workflow details into category semantics (CLAUSE-005 subclauses) | SES002-DEC011 |
| INT-003 | T102-STD-005-CLAUSE-005F amendment needed | "Only one current nested ADR" constraint needs revision to support multiple ADRs in-file (current + superseded audit trail). Amend to: "only one `accepted` ADR; `superseded` ADRs retained for audit" | SES002-DEC004 |
| INT-004 | Substandard token registration | STD-005-CLAUSE-002 taxonomy may need a `SUBSTD` entry or explicit note that substandards are internal STD structure and do NOT get separate token registration | SES002-DEC002/DEC003 |
| INT-005 | IGs in STD-004 References may be superseded | T102-IG-007, T102-IG-008, T102-IG-009 — need verification during ST002 whether these are still active or superseded by STD equivalents | SES002 Round 1 COMMENT 0.5 |

---

## VIII. Validation Checklist (Post-Implementation)

Comprehensive checklist covering all SES002 decisions:

**Substandard Structure Compliance**:
- [ ] 4 substandards present: T102-STD-004A, T102-STD-004B, T102-STD-004C, T102-STD-004D
- [ ] All 29 CLAUSEs allocated to a substandard (no floating CLAUSEs)
- [ ] Substandard headings use `###`-level under `## Specification`
- [ ] CLAUSE numbering is sequential across substandards (001-029)

**Format Compliance**:
- [ ] All subclauses use bold format: `- **<CLAUSE-ID> (<Title>)** — <statement>` (DEC015)
- [ ] No subclauses use backtick-wrapped format
- [ ] All status enums are lowercase wrapped in backticks: `proposed`, `accepted`, `deprecated` (DEC008)

**Content Compliance**:
- [ ] CLAUSE-025 (DR Body Template) includes per-subheading content + format subclauses (DEC010)
- [ ] CLAUSE-025G specifies: Alternatives Considered = bulleted list with rejection rationales
- [ ] CLAUSE-025H specifies: Consequences = `(+)`, `(±)`, `(-)` prefix bullets
- [ ] CLAUSE-008 (Normative Vocabulary) references `T102-CON-009` directly (DEC012)
- [ ] CLAUSE-011 (Precedence) references `T102-STD-005-CLAUSE-003` and expands for STD/CLAUSE/ADR (DEC013)
- [ ] CLAUSE-027 (Consequences) is ADR-only; no "STD Consequences" (DEC014)
- [ ] CLAUSE-029 (Promotion) scoped to STD/CLAUSE/ADR tokens only (DEC011)

**Structural Compliance**:
- [ ] Specification Index present with schema: `# | Substandard | CLAUSE ID | Title | Description` (DEC006)
- [ ] ADR Index present with current-first ordering (DEC004)
- [ ] ADR-001 preserved as `superseded` with full body (DEC004)
- [ ] ADR-002 present as `accepted` / current (DEC004)
- [ ] Designated directory is initiative-nonspecific: `prompt/artifacts/tasks/<SID>/consultant/standards/` (DEC009)

**Removal/Deprecation Compliance**:
- [ ] CLAUSE-013 (Variance ADR Contract) absent from all substandards (DEC005)
- [ ] STD-009 content fully absorbed into T102-STD-004B
- [ ] No changelog section added to STD-004 (DEC007)

**Derivative Compliance**:
- [ ] Guideline citations match resequenced CLAUSE IDs (no broken `[per ...]` references)
- [ ] Template structural headings match CLAUSE-001
- [ ] SPS STD-004 MVC items cite valid resequenced CLAUSEs
- [ ] SPS STD-009 row deprecated with supersession note
- [ ] All 7+ SPS STD rows with STD-009 reference updated to STD-004
- [ ] No normative rules in guideline without traceable governing CLAUSE (CLAUSE-005C)

---

## IX. Changelog

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v0.1.0 | 2026-02-15 | Initial | Comprehensive STD-004 redesign proposal (supersedes R2 proposal v0.2.0). Architecture: 4 substandards (T102-STD-004A/B/C/D), STD-009 merge, full CLAUSE resequencing (29 CLAUSEs), multiple ADRs in-file. 18 decisions from SES002. STD-005 integration issues (INT-001 through INT-005) documented for ST002. |
