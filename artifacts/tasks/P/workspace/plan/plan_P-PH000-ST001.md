---
artifact_type: 'PLAN'
planning_level: 'STREAM'
initiative_id: 'P'
initiative_code: 'PROGRAM'
phase: '0'
stream_id: 'P-PH000-ST001'
version: '0.1.6'
date: '2026-02-23'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
governance_rules: 'prompt/templates/consultant/workspace/workspace_documentation_rules.md'
procedural_guideline: 'prompt/templates/consultant/workspace/guideline_workspace_plan.md'
parent_plan: 'prompt/artifacts/tasks/P/workspace/plan/plan_P-PH000.md'
---

# PLAN: Program Governance — P / Phase `PH000` / Stream `P-PH000-ST001`: Program Standards + ID Governance Enablement (Planned)

## I. EXECUTIVE SUMMARY

**Purpose**: Plan the program-level standards authoring stream and the prerequisite ID-governance change required to make `P-RES-###` legal at Program scope (`P`).

**Hard dependency**: `T102-STD-005` token table currently restricts `RES` to `I, E, F`. Enabling `P-RES` requires a planned change in `prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md`.

---

## II. STREAM OUTLINE

**Stream ID**: `P-PH000-ST001`
**Execution Mode**: SEQUENTIAL
**Depends On**: `P-PH000-ST000-AC001`

### Activity Register

| Activity | Activity ID | Name | Status | Owner | Depends On | Deliverable | Reference |
|:--|:--|:--|:--|:--|:--|:--|:--|
| AC001 | `P-PH000-ST001-AC001` | Amend ID governance to allow `P-RES-###` | `planned` | LLM_Consultant | — | Planned T102 change (RES token Allowed Scope) | `T102-STD-005` |
| AC002 | `P-PH000-ST001-AC002` | Author `P-STD-001` (Full Promotion from T102-STD-004) | `completed` | LLM_Consultant | AC001 | `standard_P-STD-001_program-governance-standard.md` | `prompt/artifacts/tasks/P/workspace/plan/PH000/ST001/plan_P-PH000-ST001-AC002.md` |
| AC003 | `P-PH000-ST001-AC003` | Author `P-STD-002` (Program Status Standard) | `planned` | LLM_Consultant | AC001, `P-PH000-ST004-AC001` | `standard_P-STD-002_program-status-standard.md` | `prompt/artifacts/tasks/P/workspace/plan/PH000/ST001/plan_P-PH000-ST001-AC003.md` |
| AC004 | `P-PH000-ST001-AC004` | Author `P-STD-004` (File Naming & Directory Convention) | `planned` | LLM_Consultant | — | `prompt/artifacts/tasks/P/standard/standard_P-STD-004_file-naming-and-directory-convention.md` | `T102-STD-004-CLAUSE-001A`, `T102-STD-004-CLAUSE-025`, `T102-STD-005-CLAUSE-004`, `T104-PH001-ST002-AC000` (proposal v3.1.0) |
| AC005 | `P-PH000-ST001-AC005` | Align `P/standard/` naming to `standard_<SID-STD>_...` | `planned` | LLM_Developer | AC004 | Renamed `standard_P-STD-003_governance-standards-and-dr-index.md` + updated references | `P-STD-004` Convention 1 + `P` conformance |
| AC006 | `P-PH000-ST001-AC006` | Promote T102-STD-005 to P-STD-005 (Universal ID Specification) | `planned` | LLM_Consultant | AC002 | `standard_P-STD-005_universal-id-specification.md` | `prompt/artifacts/tasks/P/workspace/plan/PH000/ST001/plan_P-PH000-ST001-AC006.md` |

---

## III. ACTIVITIES (PLANNED)

#### Activity AC001: Amend ID Governance to Allow `P-RES-###`

**Activity ID**: `P-PH000-ST001-AC001`

**Purpose**: Enable `P-RES-###` IDs by updating the `RES` token Allowed Scope to include `P` in the canonical `T102-STD-005` token table.

**Planned deliverable (explicit target)**:
- Update the `RES` row in the token table inside `prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md`:
  - Allowed Scope: `I, E, F` → `P, I, E, F`

**Planned verification**:
- Confirm `P-RES-001` conforms to `T102-STD-005-CLAUSE-001` Pattern 3: `^P(?:-[A-Z0-9_]+)*-[A-Z]+-\\d{3}$`

**Scope note (SES002-DEC004)**: The RES Allowed Scope change within the `T102-STD-005` CLAUSE-002 token table is absorbed into `P-PH000-ST001-AC006-TK005` (P-STD-005 content transfer). Post-AC006, the authoritative token table resides in `P-STD-005`. AC001's remaining scope is limited to updating the concept file token table reference in `concept_T102-CONSULTANT.md`, if still required. No changes to AC001 status or task register at this time.

**Task Register**:
| Task ID | Description | Status | Action |
|:--|:--|:--|:--|
| `P-PH000-ST001-AC001-TK001` | Locate canonical `T102-STD-005` token table and the `RES` row | `planned` | — |
| `P-PH000-ST001-AC001-TK002` | Update `RES` Allowed Scope to include `P` | `planned` | — |
| `P-PH000-ST001-AC001-TK003` | Validate references and patterns remain consistent after the change | `planned` | — |

#### Activity AC002: Author `P-STD-001` (Full Promotion from T102-STD-004)

**Activity ID**: `P-PH000-ST001-AC002`

**Purpose**: Establish `P-STD-001` as the program-authoritative standard by performing a full content promotion of `T102-STD-004` (Specification Standard & Guideline).

**Deliverable (contract stub)**:
- Activity plan (SSOT task register): `prompt/artifacts/tasks/P/workspace/plan/PH000/ST001/plan_P-PH000-ST001-AC002.md`
- Promoted standard: `standard_P-STD-001_program-governance-standard.md`

**Scope**:
- In scope: promotion contract + `P-STD-001` full content transfer (29 CLAUSEs + CLAUSE-030) + T102-STD-004 supersession + reroute program-level surfaces out of `T102-PH001-ST001-AC010`.
- Out of scope: repo-wide sweeps and bulk retrofit work across all initiatives.

**Activity Plan**: `prompt/artifacts/tasks/P/workspace/plan/PH000/ST001/plan_P-PH000-ST001-AC002.md`

**Success Criteria Checklist (summary)**:
- [ ] P-STD-001 authored via full content transfer with 1:1 CLAUSE re-identification
- [ ] T102-STD-004 marked superseded with alias window
- [ ] Program-level guideline/template ownership is not executed under a `T102` plan (split recorded)
- [ ] Navigation pointers resolve (P stream plan + P SPS)

#### Activity AC003: Author `P-STD-002` (Program Status Standard)

**Activity ID**: `P-PH000-ST001-AC003`

**Purpose**: Author `P-STD-002` as a broad-scope program-wide status governance standard. Covers: canonical 7-state status vocabulary + transition rules, health/RAG assessment, unified dependency visibility schema, evidence linkage protocol, update protocol, and status artifact specification. This standard is a prerequisite for authoring the program status artifact in `P-PH000-ST002`.

**Deliverable (contract stub)**:
- Activity plan (SSOT task register): `prompt/artifacts/tasks/P/workspace/plan/PH000/ST001/plan_P-PH000-ST001-AC003.md`
- Standard: `prompt/artifacts/tasks/P/standard/standard_P-STD-002_program-status-standard.md`

**Scope**:
- In scope: 7-state enum governance (DEC-004) + transition rules + health/RAG assessment + unified dependency schema (DEC-006) + evidence linkage (DEC-005) + update protocol + status artifact spec + guideline cascade (DEC-008)
- Out of scope: authoring `status_program.md` (deferred to ST002-AC002); repo-wide initiative plan retrofits (downstream adopters update on next touch)

**Depends On**: `P-PH000-ST004-AC001` (P-RES-001 research sign-off via GATE-003)

**Activity Plan**: `prompt/artifacts/tasks/P/workspace/plan/PH000/ST001/plan_P-PH000-ST001-AC003.md`

> **DRAFT — Not finalized.** Activity plan task register is subject to amendment after P-RES-001 integration sign-off (P-PH000-ST004-AC001-GATE-003). Evidence: `raw_P-PH000-ST001-AC003-SES001.txt`

**Success Criteria Checklist (summary)**:
- [ ] P-STD-002 authored as P-STD-001-conformant combined standard-specification file
- [ ] 7-state enum set + transition rules defined as normative CLAUSEs
- [ ] Unified dependency schema defined as normative CLAUSEs
- [ ] P-STD-002-ADR-001 exists under `## Decision Record`
- [ ] sps_P P-STD-002 row updated (status `accepted`, canonical path, effective date)
- [ ] Downstream guideline files updated to reference P-STD-002 enums (TK006)

---

#### Activity AC004: Author `P-STD-004` (File Naming & Directory Convention)

**Activity ID**: `P-PH000-ST001-AC004`

**Purpose**: Author the program-level combined standard-specification file that codifies canonical directory structure and file naming conventions for all initiative directories under `prompt/artifacts/tasks/**`.

**Hard constraints**:
- `T102-STD-004` is the golden exemplar and governing authoring standard for this combined file.
- The combined file MUST follow the canonical combined-file structure defined by `T102-STD-004-CLAUSE-001A`:
  1) `# <SID-STD> — <Title>`
  2) `## Specification`
  3) `## Decision Record`
  4) `## References`
  5) `## Provenance`
- The `## Specification` section MUST author enforceable `CLAUSE` items consistent with `T102-STD-004-CLAUSE-018` and `T102-STD-005-CLAUSE-005D (Specification Clause Semantics)`.
- The `## Decision Record` section MUST contain a nested decision record using the `T102-STD-004-CLAUSE-025 (DR Body Template)` format (e.g., `P-STD-004-ADR-001`).
- Cross-scope and cross-initiative references inside normative bodies MUST follow `T102-STD-005-CLAUSE-004 (Reference Semantics)` (including the `External Reference:` line rule where applicable).

**Primary input (approved proposal seed)**:
- `prompt/artifacts/tasks/T104/workspace/PH001/ST002/AC000/proposal/proposal_T104-PH001-ST002-AC000_directory-naming-convention.md` (v3.1.0, 2026-02-18; include `verification_` and `dev-report_`)
- `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md`
- `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-005_id-specification-rules.md`

**Deliverable**:
- `prompt/artifacts/tasks/P/standard/standard_P-STD-004_file-naming-and-directory-convention.md`

**Task Register**:
| Task ID | Description | Status | Action |
|:--|:--|:--|:--|
| `P-PH000-ST001-AC004-TK000` | Confirm and codify combined STD filename convention: `standard_<SID-STD>_<kebab-title>.md` (where `<SID-STD>` conforms to `T102-STD-005-CLAUSE-001`) | `planned` | — |
| `P-PH000-ST001-AC004-TK001` | Extract normative conventions from proposal v3.1.0 into `P-STD-004` `## Specification` clauses (initiative root structure; timeline workspace rules; stems including `verification_` and `dev-report_`; raw naming; communication placement; AC directory threshold; archive strategy; research organization; epic/feature self-similarity) | `planned` | — |
| `P-PH000-ST001-AC004-TK002` | Author `P-STD-004-ADR-001` (Context/Decision/Alternatives/Consequences) capturing: (1) adoption of proposal v3.1.0 as seed; (2) forward-only adoption posture; (3) standards placement variance (use `standard/` going forward); (4) permanent grandfathering of legacy T102 `consultant/standards/` files and treatment as logically conformant to the `standard_` naming convention without renaming | `planned` | — |
| `P-PH000-ST001-AC004-TK003` | Validate `P-STD-004` conventions against at least 2 additional initiatives beyond T104 (e.g., `T102`, `T103`) before any `effective` claim, per `P-RISK-002` | `planned` | — |
| `P-PH000-ST001-AC004-TK004` | Ensure `P-STD-004` normative bodies follow `T102-STD-005-CLAUSE-004 (Reference Semantics)` when referencing IDs outside the `P` scope root (add `External Reference:` lines where required) | `planned` | — |
| `P-PH000-ST001-AC004-TK005` | Update program SPS `P-STD-004` index row to include Canonical Path once the combined file exists | `planned` | — |
| `P-PH000-ST001-AC004-TK006` | Define downstream adopter binding rule: initiatives SHALL adopt `P-STD-004` by reference and avoid duplicating directory/naming rules in local plans (link-don’t-duplicate) | `planned` | — |

**Success Criteria Checklist**:
- [ ] `standard_P-STD-004_...md` exists and follows `T102-STD-004-CLAUSE-001A` (combined-file canonical structure)
- [ ] `P-STD-004` `CLAUSE` IDs and rendering conform to `T102-STD-004-CLAUSE-018` and `T102-STD-005-CLAUSE-005D`
- [ ] `P-STD-004` clauses are enforceable and map directly to proposal v3.1.0 conventions (including `verification_` and `dev-report_`)
- [ ] `P-STD-004-ADR-001` exists under `## Decision Record` and records the standards placement variance + T102 permanent-grandfathering posture
- [ ] Cross-scope references inside normative bodies follow `T102-STD-005-CLAUSE-004 (Reference Semantics)` (including `External Reference:` lines where required)
- [ ] Program SPS `P-STD-004` row can be updated with a resolvable Canonical Path (planned)

---

#### Activity AC005: Align `P/standard/` Naming to `standard_<SID-STD>_...`

**Activity ID**: `P-PH000-ST001-AC005`

**Purpose**: Remove program-level naming drift by aligning existing program combined standard-specification files to the `standard_<SID-STD>_<kebab-title>.md` naming convention adopted by `P-STD-004` Convention 1.

**Deliverables (planned)**:
- Rename:
  - From: `prompt/artifacts/tasks/P/standard/P-STD-003_governance-standards-and-dr-index.md`
  - To: `prompt/artifacts/tasks/P/standard/standard_P-STD-003_governance-standards-and-dr-index.md`
- Update all cross-references to the new canonical path (e.g., `prompt/artifacts/tasks/P/ssot/sps_P-PROGRAM.md`).

**Task Register**:
| Task ID | Description | Status | Action |
|:--|:--|:--|:--|
| `P-PH000-ST001-AC005-TK001` | Identify all references to the existing `P-STD-003` canonical path | `planned` | — |
| `P-PH000-ST001-AC005-TK002` | Rename file to `standard_P-STD-003_...` and update references | `planned` | — |
| `P-PH000-ST001-AC005-TK003` | Verify no broken references remain for `P-STD-003` after rename | `planned` | — |

**Success Criteria Checklist**:
- [ ] No `P/standard/` files remain with legacy non-`standard_` naming (or exceptions are explicitly documented)
- [ ] `P` SPS references resolve to existing files (planned)

---

#### Activity AC006: Promote T102-STD-005 to P-STD-005 (Universal ID Specification)

**Activity ID**: `P-PH000-ST001-AC006`

**Purpose**: Promote `T102-STD-005` (ID Specification & Rules) to `P-STD-005` (Universal ID Specification) via fix-first/promote-clean methodology, absorbing T104-STD-002 timeline UID scope and pending T102-STD-005 amendments.

**Deliverable (contract stub)**:
- Activity plan: `prompt/artifacts/tasks/P/workspace/plan/PH000/ST001/plan_P-PH000-ST001-AC006.md`
- Promoted standard: `prompt/artifacts/tasks/P/standard/standard_P-STD-005_universal-id-specification.md`

**Scope**:
- In scope: pre-promotion reference cleanup + amendment verification + self-compliance audit + promotion contract + full content transfer + timeline UID CLAUSEs + Tier 1 reference updates + downstream plan amendments.
- Out of scope: repo-wide T102-STD-005 reference sweeps (alias window governs); full T102-PH001-ST002 baselining pipeline.

**Activity Plan**: `prompt/artifacts/tasks/P/workspace/plan/PH000/ST001/plan_P-PH000-ST001-AC006.md`

**Success Criteria Checklist (summary)**:
- [ ] P-STD-005 authored via full content transfer with 1:1 CLAUSE re-identification + timeline UID CLAUSEs
- [ ] T102-STD-005 marked superseded with alias window
- [ ] P-STD-001 External References and in-body refs updated to P-STD-005
- [ ] Program SPS P-STD-005 row updated
- [ ] Downstream plans amended (T104-ST002-AC002, T102-ST005-AC005, T102-ST002 scope)

---

## IV. DEPENDENCY NOTES (DOWNSTREAM ADOPTERS)

- **T104 adoption/binding** (e.g., `T104-PH001-ST002-AC000`) is downstream work and SHOULD be treated as dependent on:
  - `P-PH000-ST001-AC002` (Program Governance Standard authoring) and
  - `P-PH000-ST001-AC003` (Program Status Standard authoring).
- **T104 directory restructuring (ST007)** SHOULD treat `P-STD-004` as the authority surface for directory/naming rules once authored and SHALL avoid duplicating normative content.
- This stream does not modify any `T104` artifacts.

---

## V. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v0.1.6 | 2026-02-23 | Amendment | AC003 enriched: deprecated `P-ADR-002` reference (now embedded P-STD-002-ADR-001 per P-STD-001); broad scope locked (DEC-001); dependency on P-PH000-ST004-AC001 added (DEC-007); standalone activity plan linked; contract stub replaces 2-line stub; guideline cascade scoped as TK006 (DEC-008). Evidence: `raw_P-PH000-ST001-AC003-SES001.txt` |
| v0.1.5 | 2026-02-22 | Amendment | AC002 status → `completed` (SES002-DEC001); AC001 scope note added — RES token STD change absorbed into AC006-TK005 (SES002-DEC004). Evidence: `raw_P-PH000-ST001-AC006-SES002.txt` |
| v0.1.4 | 2026-02-22 | Amendment | AC006 added: Promote T102-STD-005 to P-STD-005 (Universal ID Specification). Absorbs T104-PH001-ST002-AC002, T102-PH001-ST005-AC005, and STD-005-specific scope from T102-PH001-ST002. Evidence: `raw_P-PH000-ST001-AC006-SES001.txt` |
| v0.1.3 | 2026-02-20 | Amendment | AC002 transitioned to `in_progress`; rebranded to Full Promotion methodology; updated deliverable and scope to match amended activity plan |
| v0.1.0 | 2026-02-05 | Initial | Stream ST001 plan created to enable `P-RES` via T102 governance change and to plan `P-STD-001` / `P-STD-002` authoring |
| v0.1.1 | 2026-02-18 | Amendment | AC004 updated per Client QA: corrected governing `T102-STD-004` clause references, pinned proposal seed to v3.1.0, codified `standard_<SID-STD>_...` naming, added cross-initiative validation requirement, and recorded permanent grandfathering posture for legacy T102 `consultant/standards/` artifacts |
| v0.1.2 | 2026-02-19 | Amendment | Linked AC002 to a dedicated activity plan to promote `T102-STD-004` authoring model into `P-STD-001` and record the T102 AC010 split boundary |
