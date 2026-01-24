---
artifact_type: 'ROADMAP'
initiative_id: 'T102'
phase: '0'
date: '2026-01-23'
version: '0.3.2'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
governance_rules: 'prompt/templates/consultant/workspace/workspace_documentation_rules.md'
template_reference: 'prompt/templates/consultant/workspace/template_workspace_roadmap.md'
reference_exemplar_1: 'prompt/artifacts/tasks/T104/T104A/workspace/roadmap/roadmap_T104A-ROADMAP_phase0.md'
reference_exemplar_2: 'prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_refactor-adr-004-005.md'
---

# ROADMAP: T102 (CWD) — Phase 0: Governance Realignment (STD + ADR)

## I. EXECUTIVE SUMMARY

**Purpose**: Standardize the long-term governance architecture for T102 to avoid “paired-document drift” and reduce Concept SSOT overload by separating:
- **Normative reference** (Standards / `STD`) vs
- **Decision rationale** (ADRs) vs
- **How-to guidance** (IG) vs
- **Integration coordination notes** (INT)

**Locked decisions (Client-approved)**:
- **Proceed with Option C**: Replace “governance as a GDR decision record” with **Standards** (`STD`) as a reference-style normative artifact family; keep ADRs as decision records.
- **Proceed with Option 2 (building on Option C)**: Split normative vs informative:
  - `STD` is normative (may use MUST/SHALL/SHOULD/MAY keywords).
  - `IG` is informative how-to guidance (no new obligations; recommendations only).
  - `INT` remains non-normative integration coordination notes.
- **Provenance** uses **repo-relative paths only** (no raw URLs).
- **Reference style**: Shorthand references are allowed in bodies; full references are required in dedicated References/Index sections.
- **STD allowed scopes**: `I/E/F` only (recommendation approved).
- **GDR token status**: Deprecate with an explicit migration window; do not delete immediately.

**Phase 0 objective**: Update the T102 governance spec drafts (ADR-004/ADR-005 proposal) to encode the decisions above, and define a migration/implementation sequence to later update the SSOT Concept compendium cleanly.

**Phase 0 exit milestone**: **Governance Realignment Draft Ready**
- Proposal ADRs updated to support `STD` and the new authority model (`STD` / `ADR` / `CLAUSE` / `IG` / `INT`).
- “GDR → STD” migration guidance defined (compatibility period + end-state).
- A follow-on execution plan for applying changes into Concept SSOT is ready.

---

## II. CONTEXT MATERIALS & INPUTS

**SPS SSOT (governance target; contains legacy `T102-GDR-*`)**:
- `prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md`

**Primary draft under active development (SSOT for draft iteration)**:
- `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_refactor-adr-004-005.md`

**Secondary draft (`planned`; STD creation + GDR→STD migration)**:
- `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_refactor_gdrs_into_std.md`

**SSOT Concept compendium (target of later replacement)**:
- `prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md`

**Roadmap structure exemplar (read-only)**:
- `prompt/artifacts/tasks/T104/T104A/workspace/roadmap/roadmap_T104A-ROADMAP_phase0.md`

**Workspace governance rules**:
- `prompt/templates/consultant/workspace/workspace_documentation_rules.md`

---

## III. PHASE 0 ROADMAP

**Scope constraint**: This roadmap defines the workstreams and sequencing. It does not force detailed redesign of DR body subheadings yet (explicitly deferred).

### Stream Register

| Stream | Name | Objective | Status | Owner | Execution Mode | Depends On | Start | Target | Completion | Key Deliverables |
|:------|:-----|:----------|:-------|:------|:--------------|:----------|:------|:-------|:-----------|:----------------|
| 1 | **Initialization of Workspace Artifacts** | Initialize Phase 0 artifacts: roadmap, notes, changelog | `planned` | LLM_Consultant | SEQUENTIAL | — | 2026-01-22 | 2026-01-22 | — | `roadmap_T102-CWD_phase0.md`, `notes_T102-CWD_phase0.md`, `changelog_roadmap_T102-CWD_phase0.md` |
| 2 | **Proposal Prep + Quick Fixes** | Consolidate quick fixes (ADR-004/005) + migrate full ADR bodies into the proposal draft | `planned` | LLM_Consultant | SEQUENTIAL | 1 | — | — | — | Updated `proposal_T102-CWD_refactor-adr-004-005.md` (bodies + fixes) |
| 3 | **STD Token Formalization (STD-009 + ADR-009)** | Initialize STD proposal draft and create the `STD` token governance baseline (`T102-STD-009` + paired `T102-ADR-009`) | `planned` | LLM_Consultant | SEQUENTIAL | 2 | — | — | — | `proposal_T102-CWD_refactor_gdrs_into_std.md` (initialized; includes STD-009 + ADR-009) |
| 4A | **ADR-004 Track (STD-004 + ADR-004 Update)** | Create `T102-STD-004` (replace `T102-GDR-004`) and update ADR-004 (except Spec then Spec) in the ADR proposal | `planned` | LLM_Consultant | PARALLEL | 3 | — | — | — | `proposal_T102-CWD_refactor_gdrs_into_std.md` (STD-004), updated ADR-004 (proposal), updated SPS references |
| 4B | **ADR-005 Track (STD-005 + ADR-005 Update)** | Create `T102-STD-005` (replace `T102-GDR-005`) and update ADR-005 (except Spec then Spec) in the ADR proposal | `planned` | LLM_Consultant | PARALLEL | 3 | — | — | — | `proposal_T102-CWD_refactor_gdrs_into_std.md` (STD-005), updated ADR-005 (proposal), updated SPS references |
| 5 | **Apply Updates Across SPS + Concept** | Apply ADR-004/ADR-005 changes to existing SPS Standards and Concept ADRs (reference updates + drift cleanup) | `planned` | LLM_Consultant | SEQUENTIAL | 4A, 4B | — | — | — | Updated `sps_T102-CONSULTANT.md` + updated `concept_T102-CONSULTANT.md` |
| 6 | **DR Body Template Redesign** | Redesign DR body template sections (Context/Decision/Consequences/etc.) | `planned` | Client | PARALLEL | 5 | — | — | — | Updated ADR-004 `CLAUSE-004` (future) |
| 7 | **Avoid Specification Overload (Concept)** | Define an index-based scalable system to avoid overloaded Concept “Specification” sections | `planned` | LLM_Consultant | PARALLEL | 5 | — | — | — | Concept structure proposal + migration guidance (future) |
| 8 | **Prevent ID Drift (Controls)** | Define enforceable controls for ID stability, referencing, and migration tolerance | `planned` | LLM_Consultant | PARALLEL | 5 | — | — | — | Control clauses + validator checklist (future) |

### Activity Register

| Stream | Activity | Name | Status | Owner | Start | Target | Completion | Deliverable(s) |
|:-------|:---------|:-----|:-------|:------|:------|:-------|:-----------|:--------------|
| 1 | 1.1 | **Create Initiative Roadmap** | `planned` | LLM_Consultant | 2026-01-22 | 2026-01-23 | — | `prompt/artifacts/tasks/T102/consultant/workspace/roadmap/roadmap_T102-CWD_phase0.md` |
| 1 | 1.2 | **Create Initiative Notes (Session Record)** | `planned` | LLM_Consultant | — | — | — | `prompt/artifacts/tasks/T102/consultant/workspace/notes/notes_T102-CWD_phase0.md` |
| 1 | 1.3 | **Create Roadmap Changelog** | `planned` | LLM_Consultant | 2026-01-23 | 2026-01-23 | — | `prompt/artifacts/tasks/T102/consultant/workspace/roadmap/changelog_roadmap_T102-CWD_phase0.md` |
| 2 | 2.1 | **Quick Fix Consolidation (ADR-004/ADR-005)** | `complete` | LLM_Consultant | — | — | 2026-01-23 | `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_refactor-adr-004-005.md` |
| 2 | 2.2 | **Migrate Full ADR Bodies into Proposal** | `complete` | LLM_Consultant | — | — | 2026-01-23 | `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_refactor-adr-004-005.md` |
| 2 | 2.4 | **Consolidate ADR Proposal Structure + Content (Dual-ADR Alignment)** | `planned` | LLM_Consultant | — | — | — | `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_refactor-adr-004-005.md` |
| 3 | 3.1 | **Initialize `proposal_T102-CWD_refactor_gdrs_into_std.md`** | `planned` | LLM_Consultant | — | — | — | `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_refactor_gdrs_into_std.md` |
| 3 | 3.2 | **Draft `T102-STD-009` (STD Token Standard)** | `planned` | LLM_Consultant | — | — | — | `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_refactor_gdrs_into_std.md` |
| 3 | 3.3 | **Draft `T102-ADR-009` (STD Token Normative Spec)** | `planned` | LLM_Consultant | — | — | — | `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_refactor_gdrs_into_std.md` |
| 4A | 4A.1 | **Draft STD Index Schema + STD-004 Entry (Replace GDR-004)** | `planned` | LLM_Consultant | — | — | — | `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_refactor_gdrs_into_std.md` |
| 4A | 4A.2 | **Update SPS: Replace GDR-004 with STD-004** | `planned` | LLM_Consultant | — | — | — | `prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md` |
| 4A | 4A.3 | **Update ADR-004 Body (Except Specification)** | `planned` | LLM_Consultant | — | — | — | `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_refactor-adr-004-005.md` |
| 4A | 4A.4 | **Update ADR-004 Specification (Align to STD Model)** | `planned` | LLM_Consultant | — | — | — | `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_refactor-adr-004-005.md` |
| 4B | 4B.1 | **Draft STD-005 Entry (Replace GDR-005)** | `planned` | LLM_Consultant | — | — | — | `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_refactor_gdrs_into_std.md` |
| 4B | 4B.2 | **Update SPS: Replace GDR-005 with STD-005** | `planned` | LLM_Consultant | — | — | — | `prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md` |
| 4B | 4B.3 | **Update ADR-005 Body (Except Specification)** | `planned` | LLM_Consultant | — | — | — | `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_refactor-adr-004-005.md` |
| 4B | 4B.4 | **Update ADR-005 Specification (Token/Authority Rules)** | `planned` | LLM_Consultant | — | — | — | `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_refactor-adr-004-005.md` |
| 5 | 5.1 | **Apply ADR-004/ADR-005 Across SPS Standards** | `planned` | LLM_Consultant | — | — | — | `prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md` |
| 5 | 5.2 | **Apply ADR-004/ADR-005 Across Concept ADRs** | `planned` | LLM_Consultant | — | — | — | `prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md` |
| 6 | 6.1 | **Redesign DR Body Template Sections** | `planned` | Client | — | — | — | `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_refactor-adr-004-005.md` |
| 7 | 7.1 | **Define Concept Spec Index System** | `planned` | LLM_Consultant | — | — | — | `prompt/artifacts/tasks/T102/consultant/workspace/notes/notes_T102-CWD_phase0.md` |
| 8 | 8.1 | **Define Enforceable ID Drift Controls** | `planned` | LLM_Consultant | — | — | — | `prompt/artifacts/tasks/T102/consultant/workspace/notes/notes_T102-CWD_phase0.md` |

---

### Stream 1: Initialization of Workspace Artifacts

**Objective**: Initialize the Phase 0 workspace artifacts (Roadmap, Notes, Changelog) using the T104 exemplar structure so subsequent proposal and SSOT work can proceed with reduced drift risk.

**Context**:
- `prompt/artifacts/tasks/T102/consultant/workspace/roadmap/roadmap_T102-CWD_phase0.md`
- `prompt/artifacts/tasks/T102/consultant/workspace/notes/notes_T102-CWD_phase0.md`
- `prompt/artifacts/tasks/T102/consultant/workspace/roadmap/changelog_roadmap_T102-CWD_phase0.md`

**Scope**:
- Include: roadmap registers, stream/activity section contracts, and Open Questions hygiene.
- Include: creating/maintaining links to the existing notes and changelog artifacts.
- Exclude: modifying proposal drafts or SSOT content (Streams 2+).

#### Activity 1.1: Create Initiative Roadmap

**Purpose**: Create and maintain the Phase 0 roadmap as the coordination SSOT for Streams/Activities/Dependencies for T102 (CWD).

**Deliverable**: `prompt/artifacts/tasks/T102/consultant/workspace/roadmap/roadmap_T102-CWD_phase0.md`

**Task Register**:
| Task ID | Description | Status | Action |
|:--------|:------------|:-------|:-------|
| 1.1.1 | Refactor stream/activity registers to dependency standard | `planned` | — |
| 1.1.2 | Align Stream/Activity headings to register “Name” cells | `planned` | — |
| 1.1.3 | Add/maintain Links Register + Open Questions Register + Changelog pointer | `planned` | — |

**Success Criteria Checklist**:
- [ ] Stream Register includes `Execution Mode` and `Depends On`
- [ ] Activity Register follows exemplar structure and excludes dependency columns (with an explicit note)
- [ ] All Stream sections include `Objective` and `Scope`
- [ ] All Activities include `Purpose` and `Success Criteria Checklist`
- [ ] Activity `Deliverable` fields are repo-relative paths only
- [ ] Open Questions are up to date (no stale decisions)
- [ ] Checklist verified; Task Register updated (set `Status` to `complete` / `deffered` / `cancel`; set `Action` to a concise outcome)

#### Activity 1.2: Create Initiative Notes (Session Record)

**Purpose**: Capture Phase 0 consultation decisions, assumptions, and rationale as a lightweight session memory that references (not replaces) SSOT artifacts.

**Deliverable**: `prompt/artifacts/tasks/T102/consultant/workspace/notes/notes_T102-CWD_phase0.md`

**Task Register**:
| Task ID | Description | Status | Action |
|:--------|:------------|:-------|:-------|
| 1.2.1 | Create Phase 0 notes file (session record) | `planned` | — |
| 1.2.2 | Record Phase 0 decisions + rationale summary | `planned` | — |

**Success Criteria Checklist**:
- [ ] Notes file exists at the target path
- [ ] Notes references this roadmap for scope/sequence
- [ ] Notes use repo-relative paths for provenance references
- [ ] Checklist verified; Task Register updated (set `Status` to `complete` / `deffered` / `cancel`; set `Action` to a concise outcome)

#### Activity 1.3: Create Roadmap Changelog

**Purpose**: Keep roadmap edits traceable across Phase 0 without polluting the roadmap body with version deltas.

**Deliverable**: `prompt/artifacts/tasks/T102/consultant/workspace/roadmap/changelog_roadmap_T102-CWD_phase0.md`

**Task Register**:
| Task ID | Description | Status | Action |
|:--------|:------------|:-------|:-------|
| 1.3.1 | Create changelog file (roadmap-only changes) | `planned` | — |
| 1.3.2 | Add/maintain changelog entry for current roadmap update | `planned` | — |

**Success Criteria Checklist**:
- [ ] Changelog exists as a separate file
- [ ] Changelog contains an entry for this roadmap version update
- [ ] Changelog entries are repo-relative and scoped to roadmap changes only
- [ ] Checklist verified; Task Register updated (set `Status` to `complete` / `deffered` / `cancel`; set `Action` to a concise outcome)

---

### Stream 2: Proposal Prep + Quick Fixes

**Objective**: Stabilize the ADR-004/ADR-005 proposal draft with agreed quick fixes and a complete ADR body structure so later STD migration work builds on a consistent baseline.

**Context**:
- `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_refactor-adr-004-005.md`
- `prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md`

**Scope**:
- Include: quick fixes and drafting hygiene inside the ADR proposal file.
- Include: migrating ADR-004/ADR-005 to full ADR bodies (not Specification-only).
- Exclude: introducing `STD` token changes (Stream 3+).

#### Activity 2.1: Quick Fix Consolidation (ADR-004/ADR-005)

**Purpose**: Consolidate the known “quick fixes” for ADR-004 and ADR-005 without mixing in the larger STD migration decisions.

**Deliverable**: `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_refactor-adr-004-005.md`

**Task Register**:
| Task ID | Description | Status | Action |
|:--------|:------------|:-------|:-------|
| 2.1.1 | Fix 1-word clause titles violating ADR-005 title constraints | `complete` | Renamed `T102-ADR-005-CLAUSE-007` to `ID Stability & Immutability` |
| 2.1.2 | Ensure “Title” cells in index tables are bold | `complete` | Updated `ADR-004-CLAUSE-001` and `ADR-005-CLAUSE-005A` to use `**Title**` |
| 2.1.3 | Fix incorrect/ambiguous references (consistent shorthand-in-body policy) | `complete` | Updated references in `ADR-004-CLAUSE-003` and `ADR-005-CLAUSE-006` to use full IDs |
| 2.1.4 | Reduce drift risk by converting duplicated semantics into explicit cross-references (ADR-004 ↔ ADR-005) | `complete` | Ensured ADR-004 Body Template links to ADR-005 for Reference semantics |
| 2.1.5 | Align Provenance rule to repo-relative paths only | `complete` | Updated `ADR-004-CLAUSE-012` to mandate "repo-relative paths" |

**Success Criteria Checklist**:
- [x] 1-word clause titles are eliminated where prohibited
- [x] Index table “Title” cells are bold where required
- [x] Incorrect/ambiguous references are corrected (per shorthand/full reference policy)
- [x] Duplicated semantics (ADR-004 ↔ ADR-005) are reduced via explicit cross-references
- [x] Provenance statements use repo-relative paths only
- [ ] Checklist verified; Task Register updated (set `Status` to `complete` / `deffered` / `cancel`; set `Action` to a concise outcome)

#### Activity 2.2: Migrate Full ADR Bodies into Proposal

**Purpose**: The ADR drafts in the proposal MUST include full ADR structures (not Specification-only) extracted from `concept_T102-CONSULTANT.md`, to prevent drift during later SSOT applies.

**Deliverable**: `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_refactor-adr-004-005.md`

**Task Register**:
| Task ID | Description | Status | Action |
|:--------|:------------|:-------|:-------|
| 2.2.1 | Add ADR headings (Context/Decision/Specification/Alternatives/Consequences/References/Provenance) | `complete` | Migrated headers from Concept SSOT for ADR-004 and ADR-005 |
| 2.2.2 | Ensure References sections use full reference formatting | `complete` | Verified all references use `ID (Title)` format |
| 2.2.3 | Keep Provenance as repo-relative paths only | `complete` | Set Provenance to `proposal_T102-CWD_refactor-adr-004-005.md` |

**Success Criteria Checklist**:
- [x] ADR-004 includes full body headings (Context/Decision/Specification/Alternatives/Consequences/References/Provenance)
- [x] ADR-005 includes full body headings (Context/Decision/Specification/Alternatives/Consequences/References/Provenance)
- [x] References sections use full reference formatting consistently
- [x] Provenance sections are repo-relative paths only
- [ ] Checklist verified; Task Register updated (set `Status` to `complete` / `deffered` / `cancel`; set `Action` to a concise outcome)

#### Activity 2.4: Consolidate ADR Proposal Structure + Content (Dual-ADR Alignment)

**Purpose**: Consolidate `proposal_T102-CWD_refactor-adr-004-005.md` so shared `##/###` headings apply to both ADR-004 and ADR-005, and duplicated prose is merged to a canonical source to reduce drift while preserving core meaning.

**Deliverable**: `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_refactor-adr-004-005.md`

**Task Register**:
| Task ID | Description | Status | Action |
|:--------|:------------|:-------|:-------|
| 2.4.1 | Build a “section map” (inventory) of current `##/###` structure for ADR-004 vs ADR-005 | `complete` | Inventory completed; mapped shared sections (Problem, Baseline, Changes, Specs) |
| 2.4.2 | Refactor structure so every shared `##` contains explicit subheadings for both ADRs (no single-ADR-only content at shared heading levels) | `complete` | Refactored into unified I-VII structure with ADR-specific subheaders |
| 2.4.3 | Define merge methodology: canonical block + explicit references (no copy/paste twins) | `complete` | Adopted unified sections for meta-commentary; distinct blocks for specs |
| 2.4.4 | Consolidate duplicated content: choose canonical phrasing and mark the alternate text as deprecated with a short note + reference | `complete` | Consolidated overlapping analysis and purpose statements |
| 2.4.5 | Verify “core content unchanged”: confirm consolidation is meaning-preserving; record any unavoidable wording deltas explicitly | `complete` | Verified draft specifications were moved without semantic change |

**Success Criteria Checklist**:
- [x] Shared `##/###` headings include explicit ADR subheadings: `### T102-ADR-004 (...)` and `### T102-ADR-005 (...)`
- [x] Duplicated semantics are expressed once and referenced elsewhere (no parallel narrative blocks)
- [x] Near-duplicates are merged using canonical phrasing; deprecated alternates are explicitly marked
- [x] Core meaning is preserved (no new rules introduced; no obligations removed)
- [x] Checklist verified; Task Register updated (set `Status` to `complete` / `deffered` / `cancel`; set `Action` to a concise outcome)

---

### Stream 3: STD Token Formalization (STD-009 + ADR-009)

**Objective**: Establish the `STD` artifact family baseline and its paired normative spec pattern via `T102-STD-009` + `T102-ADR-009`, so downstream STD-004/STD-005 work has a stable contract.

**Context**:
- `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_refactor_gdrs_into_std.md`
- `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_refactor-adr-004-005.md`

**Scope**:
- Include: initialization of the STD migration proposal file, plus baseline `STD` index schema and lifecycle placeholders.
- Include: `T102-STD-009` (standard describing STD governance) and `T102-ADR-009` (paired normative spec for `STD` token).
- Exclude: migrating any existing GDRs to STDs (Streams 4A/4B+).

#### Activity 3.1: Initialize `proposal_T102-CWD_refactor_gdrs_into_std.md`

**Purpose**: Initialize the dedicated proposal draft using `proposal_T102-CWD_refactor-adr-004-005.md` as examplar used to refactor legacy GDRs into STDs and to introduce the STD artifact baseline.

**Deliverable**: `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_refactor_gdrs_into_std.md`

**Task Register**:
| Task ID | Description | Status | Action |
|:--------|:------------|:-------|:-------|
| 3.1.1 | Create proposal file skeleton with headings and scope | `complete` | Created proposal skeleton with Purpose/Scope, Context inputs, STD Index Schema placeholder, and repo-relative provenance. |
| 3.1.2 | Add “Parallelism & Dependencies” notes relevant to STD migration (if needed) | `complete` | Added Phase 0 dependency notes (Stream 2 → Stream 3 → Streams 4A/4B → Stream 5). |

**Success Criteria Checklist**:
- [x] File exists at the target path
- [x] File contains a clear purpose statement and scope boundaries
- [x] File includes the STD Index Schema (table) above bodies
- [x] File includes provenance as repo-relative paths only
- [x] Checklist verified; Task Register updated (set `Status` to `complete` / `deffered` / `cancel`; set `Action` to a concise outcome)

#### Activity 3.2: Draft `T102-STD-009` (STD Token Standard)

**Purpose**: Define the `STD` artifact family baseline (index schema + lifecycle fields + relationship to ADR/RID/IG/INT) as a normative Standard entry.

**Deliverable**: `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_refactor_gdrs_into_std.md`

**Task Register**:
| Task ID | Description | Status | Action |
|:--------|:------------|:-------|:-------|
| 3.2.1 | Add STD Index Schema table above bodies | `planned` | — |
| 3.2.2 | Draft `T102-STD-009` row and body | `planned` | — |

**Success Criteria Checklist**:
- [ ] STD Index Schema table exists and matches the approved column set
- [ ] `T102-STD-009` is defined using the canonical ID schema formatting
- [ ] `T102-STD-009` explicitly references its adopted normative spec (`T102-ADR-009`)
- [ ] Empty fields use `—` where values are intentionally deferred
- [ ] Checklist verified; Task Register updated (set `Status` to `complete` / `deffered` / `cancel`; set `Action` to a concise outcome)

#### Activity 3.3: Draft `T102-ADR-009` (STD Token Normative Spec)

**Purpose**: Create the paired normative spec ADR that defines the enforceable rules for the `STD` token (authority model and references back to ADR-004/ADR-005).

**Deliverable**: `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_refactor_gdrs_into_std.md`

**Task Register**:
| Task ID | Description | Status | Action |
|:--------|:------------|:-------|:-------|
| 3.3.1 | Draft ADR-009 body headings + minimal content | `planned` | — |
| 3.3.2 | Draft ADR-009 Specification rules for the STD token | `planned` | — |

**Success Criteria Checklist**:
- [ ] `T102-ADR-009` exists and follows the full ADR body template (not Specification-only)
- [ ] ADR-009 Specification references ADR-004 and ADR-005 for shared mechanisms (no duplicated semantics)
- [ ] ADR-009 clearly distinguishes normative (STD) vs informative (IG/INT/NOTE)
- [ ] Checklist verified; Task Register updated (set `Status` to `complete` / `deffered` / `cancel`; set `Action` to a concise outcome)

---

### Stream 4A: ADR-004 Track (STD-004 + ADR-004 Update)

**Objective**: Create `T102-STD-004` and update ADR-004 (body then Specification) to align with the STD governance model without duplicating ADR-005 responsibilities.

**Context**:
- `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_refactor_gdrs_into_std.md`
- `prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md`
- `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_refactor-adr-004-005.md`

**Scope**:
- Include: defining STD-004, updating ADR-004 draft (proposal), and updating SPS references from GDR-004 to STD-004.
- Exclude: applying changes across Concept (Stream 5).

#### Activity 4A.1: Draft STD Index Schema + STD-004 Entry (Replace GDR-004)

**Purpose**: Define Standards (`STD`) as reference-style, indexed governance items, and create `T102-STD-004` as the replacement for `T102-GDR-004`.

**Deliverable**: `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_refactor_gdrs_into_std.md`

**Task Register**:
| Task ID | Description | Status | Action |
|:--------|:------------|:-------|:-------|
| 4A.1.1 | Create STD index schema in the STD proposal (if missing) | `planned` | — |
| 4A.1.2 | Draft `T102-STD-004` entry mapping to ADR-004 (row + body) | `planned` | — |
| 4A.1.3 | Ensure `Adopts (Normative Spec)` references `T102-ADR-004` using full reference format in index contexts | `planned` | — |

**Success Criteria Checklist**:
- [ ] STD Index Schema exists above bodies (if not already present from Stream 3)
- [ ] `T102-STD-004` row + body exist and map to ADR-004 as the adopted normative spec
- [ ] Empty STD fields use `—` when values are intentionally deferred
- [ ] Checklist verified; Task Register updated (set `Status` to `complete` / `deffered` / `cancel`; set `Action` to a concise outcome)

#### Activity 4A.2: Update SPS: Replace GDR-004 with STD-004

**Purpose**: Apply the GDR→STD refactor into the SPS SSOT by replacing `T102-GDR-004` references with `T102-STD-004`, while preserving migration tolerance and provenance.

**Deliverable**: `prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md`

**Task Register**:
| Task ID | Description | Status | Action |
|:--------|:------------|:-------|:-------|
| 4A.2.1 | Replace `T102-GDR-004` references with `T102-STD-004` | `planned` | — |
| 4A.2.2 | Preserve provenance by pointing to the STD proposal path | `planned` | — |

**Success Criteria Checklist**:
- [ ] `T102-GDR-004` references are replaced with `T102-STD-004` where appropriate
- [ ] Provenance references point to repo-relative proposal paths only
- [ ] Migration tolerance language is preserved (do not hard-delete legacy references unless explicitly required)
- [ ] Checklist verified; Task Register updated (set `Status` to `complete` / `deffered` / `cancel`; set `Action` to a concise outcome)

#### Activity 4A.3: Update ADR-004 Body (Except Specification)

**Purpose**: Update ADR-004 narrative body sections to reflect “STD adopts normative spec” semantics (Option C) without duplicating ADR-005 specification responsibilities.

**Deliverable**: `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_refactor-adr-004-005.md`

**Task Register**:
| Task ID | Description | Status | Action |
|:--------|:------------|:-------|:-------|
| 4A.3.1 | Replace “GDR adopts ADR” patterns with “STD adopts normative spec” patterns | `planned` | — |
| 4A.3.2 | Keep ADR-004 Spec responsibility split aligned to ADR-005 via explicit references | `planned` | — |

**Success Criteria Checklist**:
- [ ] ADR-004 body includes full headings and uses consistent reference style rules
- [ ] “GDR adopts ADR” phrasing is replaced with “STD adopts normative spec” where applicable
- [ ] Any shared mechanics are referenced (not duplicated) from ADR-005 clauses
- [ ] Checklist verified; Task Register updated (set `Status` to `complete` / `deffered` / `cancel`; set `Action` to a concise outcome)

#### Activity 4A.4: Update ADR-004 Specification (Align to STD Model)

**Purpose**: Update ADR-004 Specification clauses so they are compatible with the STD governance model and cross-reference ADR-005 for ID/CLAUSE semantics.

**Deliverable**: `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_refactor-adr-004-005.md`

**Task Register**:
| Task ID | Description | Status | Action |
|:--------|:------------|:-------|:-------|
| 4A.4.1 | Align ADR-004 spec guidance to reference `STD` authority model | `planned` | — |
| 4A.4.2 | Ensure `CLAUSE`/DRCID rules remain cross-referenced to ADR-005 | `planned` | — |

**Success Criteria Checklist**:
- [ ] ADR-004 Specification references the STD governance model where applicable
- [ ] `CLAUSE`/DRCID rules remain cross-referenced to ADR-005 (avoid duplication)
- [ ] Clause formatting rules align with current drafting standards (bullet list + headings as specified)
- [ ] Checklist verified; Task Register updated (set `Status` to `complete` / `deffered` / `cancel`; set `Action` to a concise outcome)

---

### Stream 4B: ADR-005 Track (STD-005 + ADR-005 Update)

**Objective**: Create `T102-STD-005` and update ADR-005 (body then Specification) to reflect the authority model (Option 2) and the introduction of `STD`.

**Context**:
- `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_refactor_gdrs_into_std.md`
- `prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md`
- `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_refactor-adr-004-005.md`

**Scope**:
- Include: defining STD-005, updating ADR-005 draft (proposal), and updating SPS references from GDR-005 to STD-005.
- Exclude: applying changes across Concept (Stream 5).

#### Activity 4B.1: Draft STD-005 Entry (Replace GDR-005)

**Purpose**: Draft `T102-STD-005` as the replacement for `T102-GDR-005`, adopting ADR-005 as its normative specification and encoding enforcement expectations.

**Deliverable**: `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_refactor_gdrs_into_std.md`

**Task Register**:
| Task ID | Description | Status | Action |
|:--------|:------------|:-------|:-------|
| 4B.1.1 | Draft `T102-STD-005` entry mapping to ADR-005 | `planned` | — |
| 4B.1.2 | Ensure `Adopts (Normative Spec)` references `T102-ADR-005` using full reference format in index contexts | `planned` | — |

**Success Criteria Checklist**:
- [ ] `T102-STD-005` row + body exist and map to ADR-005 as adopted normative spec
- [ ] Empty STD fields use `—` where values are intentionally deferred
- [ ] Enforcement field references ADR-004 and ADR-005 as the conformance basis (as applicable)
- [ ] Checklist verified; Task Register updated (set `Status` to `complete` / `deffered` / `cancel`; set `Action` to a concise outcome)

#### Activity 4B.2: Update SPS: Replace GDR-005 with STD-005

**Purpose**: Apply the GDR→STD refactor into the SPS SSOT by replacing `T102-GDR-005` references with `T102-STD-005`, while preserving migration tolerance and provenance.

**Deliverable**: `prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md`

**Task Register**:
| Task ID | Description | Status | Action |
|:--------|:------------|:-------|:-------|
| 4B.2.1 | Replace `T102-GDR-005` references with `T102-STD-005` | `planned` | — |
| 4B.2.2 | Preserve provenance by pointing to the STD proposal path | `planned` | — |

**Success Criteria Checklist**:
- [ ] `T102-GDR-005` references are replaced with `T102-STD-005` where appropriate
- [ ] Provenance references point to repo-relative proposal paths only
- [ ] Migration tolerance language is preserved (do not hard-delete legacy references unless explicitly required)
- [ ] Checklist verified; Task Register updated (set `Status` to `complete` / `deffered` / `cancel`; set `Action` to a concise outcome)

#### Activity 4B.3: Update ADR-005 Body (Except Specification)

**Purpose**: Update ADR-005 body sections to reflect the authority model decision (Option 2) and the introduction of `STD` without duplicating ADR-004 responsibilities.

**Deliverable**: `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_refactor-adr-004-005.md`

**Task Register**:
| Task ID | Description | Status | Action |
|:--------|:------------|:-------|:-------|
| 4B.3.1 | Encode “Option 2” split: `STD` normative, `IG` informative, `INT` non-normative | `planned` | — |
| 4B.3.2 | Keep `STD` flexible (RID-style construction per ADR-005 canonical schema) | `planned` | — |

**Success Criteria Checklist**:
- [ ] ADR-005 body includes full headings and uses consistent reference style rules
- [ ] “Option 2” semantics are encoded: `STD` normative, `IG` informative, `INT` non-normative
- [ ] Any shared mechanics are referenced (not duplicated) from ADR-004 clauses
- [ ] Checklist verified; Task Register updated (set `Status` to `complete` / `deffered` / `cancel`; set `Action` to a concise outcome)

#### Activity 4B.4: Update ADR-005 Specification (Token/Authority Rules)

**Purpose**: Update ADR-005 Specification clauses to introduce the `STD` token and to formalize its authority model and migration from legacy `GDR`.

**Deliverable**: `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_refactor-adr-004-005.md`

**Task Register**:
| Task ID | Description | Status | Action |
|:--------|:------------|:-------|:-------|
| 4B.4.1 | Add `STD` token into taxonomy with scopes `I/E/F` | `planned` | — |
| 4B.4.2 | Deprecate `GDR` with explicit migration tolerance language | `planned` | — |

**Success Criteria Checklist**:
- [ ] `STD` token is added to the taxonomy with scopes `I/E/F`
- [ ] `GDR` is deprecated with explicit migration tolerance language
- [ ] `IG` rules are updated to reflect “informative how-to” (no new obligations)
- [ ] `INT` remains non-normative with scoped coordination exception as applicable
- [ ] Checklist verified; Task Register updated (set `Status` to `complete` / `deffered` / `cancel`; set `Action` to a concise outcome)

---

### Stream 5: Apply Updates Across SPS + Concept

**Objective**: Apply the finalized ADR-004/ADR-005 and STD migration outputs into SPS and Concept SSOTs with minimal drift and clear provenance.

**Context**:
- `prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md`
- `prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md`

**Scope**:
- Include: reference updates, drift cleanup, and migration tolerance application.
- Exclude: redesigning DR body template headings (Stream 6) and concept spec index redesign (Stream 7).

#### Activity 5.1: Apply ADR-004/ADR-005 Across SPS Standards

**Purpose**: Apply the ADR-004/ADR-005 + STD migration rules across SPS so governance artifacts use consistent references and token semantics.

**Deliverable**: `prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md`

**Task Register**:
| Task ID | Description | Status | Action |
|:--------|:------------|:-------|:-------|
| 5.1.1 | Apply `STD` replacement patterns for legacy GDRs | `planned` | — |
| 5.1.2 | Normalize references (shorthand-in-body; full refs in dedicated reference sections) | `planned` | — |

**Success Criteria Checklist**:
- [ ] SPS replaces legacy GDR patterns with STD patterns where required
- [ ] SPS reference style matches policy (shorthand in bodies; full refs in dedicated sections)
- [ ] Provenance remains repo-relative and points to relevant proposal drafts
- [ ] Checklist verified; Task Register updated (set `Status` to `complete` / `deffered` / `cancel`; set `Action` to a concise outcome)

#### Activity 5.2: Apply ADR-004/ADR-005 Across Concept ADRs

**Purpose**: Apply ADR-004/ADR-005 drafting rules and updated reference semantics across Concept compendium ADRs to reduce drift and inconsistent clause references.

**Deliverable**: `prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md`

**Task Register**:
| Task ID | Description | Status | Action |
|:--------|:------------|:-------|:-------|
| 5.2.1 | Update Concept ADR references to align with updated ADR-004/ADR-005 | `planned` | — |
| 5.2.2 | Sweep for legacy clause/ID drift and correct per migration rules | `planned` | — |

**Success Criteria Checklist**:
- [ ] Concept ADR references align with updated ADR-004/ADR-005 semantics
- [ ] Legacy clause/ID drift is corrected per migration tolerance rules
- [ ] Provenance and References sections follow the shorthand/full reference policy
- [ ] Checklist verified; Task Register updated (set `Status` to `complete` / `deffered` / `cancel`; set `Action` to a concise outcome)

---

### Stream 6: DR Body Template Redesign

**Objective**: Redesign the DR body template (Context/Decision/Consequences/etc.) to reduce duplication and drift between governance artifacts.

**Context**:
- `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_refactor-adr-004-005.md`

**Scope**:
- Include: redesigning ADR-004 DR body template clauses and associated drafting rules.
- Exclude: applying redesigned templates to existing SSOT artifacts until explicitly scheduled.

#### Activity 6.1: Redesign DR Body Template Sections

**Purpose**: Redesign DR body section grammar (Context/Decision/Consequences/etc.) and clarify responsibilities to reduce paired-document drift risk.

**Deliverable**: `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_refactor-adr-004-005.md`

**Task Register**:
| Task ID | Description | Status | Action |
|:--------|:------------|:-------|:-------|
| 6.1.1 | Redesign DR body section grammar (Context/Decision/Consequences/etc.) | `planned` | — |

**Success Criteria Checklist**:
- [ ] Updated DR body template rules are defined as a delta (not scattered edits)
- [ ] Responsibilities are split cleanly to avoid duplicated semantics across ADRs
- [ ] References are used to prevent drift rather than copied prose
- [ ] Checklist verified; Task Register updated (set `Status` to `complete` / `deffered` / `cancel`; set `Action` to a concise outcome)

### Stream 7: Avoid Specification Overload (Concept)

**Objective**: Define an index-based model for Concept “Specification” content so Concept remains navigable and avoids becoming an implementation handbook.

**Context**:
- `prompt/artifacts/tasks/T102/consultant/workspace/notes/notes_T102-CWD_phase0.md`

**Scope**:
- Include: a proposal for spec-indexing and out-of-line spec files with stable links.
- Exclude: implementing the full migration until after Phase 0 governance stabilization.

#### Activity 7.1: Define Concept Spec Index System

**Purpose**: Propose a scalable concept spec index system to reduce “Specification overload” while retaining traceability.

**Deliverable**: `prompt/artifacts/tasks/T102/consultant/workspace/notes/notes_T102-CWD_phase0.md`

**Task Register**:
| Task ID | Description | Status | Action |
|:--------|:------------|:-------|:-------|
| 7.1.1 | Propose index-based concept structure to reduce spec overload | `planned` | — |

**Success Criteria Checklist**:
- [ ] A clear index/table proposal exists (columns, linking rules, stability rules)
- [ ] Proposal includes a drift-control mechanism (where normative vs informative lives)
- [ ] Proposal is compatible with ADR-005 reference semantics
- [ ] Checklist verified; Task Register updated (set `Status` to `complete` / `deffered` / `cancel`; set `Action` to a concise outcome)

### Stream 8: Prevent ID Drift (Controls)

**Objective**: Define enforceable controls that keep IDs stable, prevent reference drift, and make migrations explicit and auditable.

**Context**:
- `prompt/artifacts/tasks/T102/consultant/workspace/notes/notes_T102-CWD_phase0.md`

**Scope**:
- Include: stability rules, migration tolerance strategy, and validator/checklist requirements.
- Exclude: implementing validators until a later engineering stream is scheduled.

#### Activity 8.1: Define Enforceable ID Drift Controls

**Purpose**: Define stability rules, migration tolerance, and enforceable validator checks to keep ID/reference semantics stable during refactors.

**Deliverable**: `prompt/artifacts/tasks/T102/consultant/workspace/notes/notes_T102-CWD_phase0.md`

**Task Register**:
| Task ID | Description | Status | Action |
|:--------|:------------|:-------|:-------|
| 8.1.1 | Define stability rules, migration tolerance, and validator checks | `planned` | — |

**Success Criteria Checklist**:
- [ ] Controls include “immutable IDs” and “stable anchors” principles
- [ ] Controls include explicit migration tolerance rules for legacy tokens
- [ ] Controls include enforceable checks (lint/review/automation) at a high level
- [ ] Checklist verified; Task Register updated (set `Status` to `complete` / `deffered` / `cancel`; set `Action` to a concise outcome)

---

## IV. ROADMAP AUTHORING GUIDELINES

**Status enums (Registers)**:
- Stream Register `Status` MUST be one of: `planned`, `deffered`, `complete`, `cancel`.
- Activity Register `Status` MUST be one of: `planned`, `deffered`, `complete`, `cancel`.
- In all register tables, `Status` values MUST be wrapped in backticks.

**Status enums (Task Registers)**:
- Task Register `Status` MUST be one of: `planned`, `deffered`, `complete`, `cancel`.
- In all Task Register tables, `Status` values MUST be wrapped in backticks.

**Task Register schema**:
- Every Activity MUST include a Task Register with columns: `Task ID | Description | Status | Action`.
- `Action` MUST be set to `—` when no action has started, and MUST be updated with a concise outcome statement when the task moves to `complete`, `deffered`, or `cancel`.
- Rule of thumb: treat `Status` as a lifecycle state; treat `Action` as the evidence trail.

**Activity completion rule**:
- An Activity is considered done only when its Success Criteria Checklist is verified and its Task Register rows are updated to an active terminal status (`complete`, `deffered`, or `cancel`) with a non-empty `Action` statement.

**Parallelism & Dependencies Standard (Roadmap)**:
- **Execution Mode**:
  - `PARALLEL`: may be executed concurrently (subject to `Depends On`).
  - `SEQUENTIAL`: intended ordering signal (still enforce via `Depends On` if required).
  - `GATED`: requires explicit exit evidence before dependent work starts (use `Depends On` + an “Exit Evidence” checklist in the Stream).
- **Depends On**: comma-separated list of prerequisite **Stream IDs** and/or **Activity IDs** (e.g., `1`, `1.1`, `2.2`). Use `—` if none.
- **Rule**: `Depends On` is the enforceable constraint; `Execution Mode` is the coordination intent.

**Activity Register note**:
- Activity Register intentionally excludes `Execution Mode` / `Depends On` columns for now (may be reintroduced later).

**Stream context rule**:
- Each Stream MUST include a `Context` block listing only repo-relative paths that its Activities touch.
- Section II lists general context inputs; do not duplicate non-touched paths in Stream Context blocks.

## V. LINKS REGISTER

| Link Type | Target | Path |
|:----------|:-------|:-----|
| Roadmap (this file) | T102 Phase 0 Roadmap | `prompt/artifacts/tasks/T102/consultant/workspace/roadmap/roadmap_T102-CWD_phase0.md` |
| Notes | T102 Phase 0 Notes | `prompt/artifacts/tasks/T102/consultant/workspace/notes/notes_T102-CWD_phase0.md` |
| Changelog | Roadmap Changelog | `prompt/artifacts/tasks/T102/consultant/workspace/roadmap/changelog_roadmap_T102-CWD_phase0.md` |
| SSOT | T102 SPS | `prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md` |
| SSOT | T102 Concept | `prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md` |
| Proposal (ADR specs) | ADR-004/ADR-005 Draft | `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_refactor-adr-004-005.md` |
| Proposal (GDR→STD) | STD Migration Draft | `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_refactor_gdrs_into_std.md` |
| Exemplar (read-only) | T104 Roadmap | `prompt/artifacts/tasks/T104/workspace/roadmap/roadmap_T104-CWS_phase0.md` |
| Exemplar (read-only) | T104 Notes | `prompt/artifacts/tasks/T104/workspace/notes/notes_T104-CWS_phase0.md` |
| Exemplar (read-only) | T104 Changelog | `prompt/artifacts/tasks/T104/workspace/roadmap/changelog_roadmap_T104-CWS_phase0.md` |
| Governance Rules | Workspace Rules | `prompt/templates/consultant/workspace/workspace_documentation_rules.md` |
| Roadmap Template | Template | `prompt/templates/consultant/workspace/template_workspace_roadmap.md` |

---

## VI. OPEN QUESTIONS REGISTER

| ID | Topic | Question | Owner | Status | Proposed Date | Resolved Date |
|:---|:------|:---------|:------|:-------|:--------------|:-------------|
| OQ-001 | Activity Register | Should Activity Register add Execution Mode/Depends On columns later for stricter gating? | Client | Complete | 2026-01-22 | 2026-01-23 |
| OQ-002 | STD Token Spec | Should the “STD token normative spec” be captured as a dedicated ADR ID, or embedded as clauses inside ADR-005? | Client | Complete | 2026-01-22 | 2026-01-23 |

---

## VII. CHANGELOG

`prompt/artifacts/tasks/T102/consultant/workspace/roadmap/changelog_roadmap_T102-CWD_phase0.md`
