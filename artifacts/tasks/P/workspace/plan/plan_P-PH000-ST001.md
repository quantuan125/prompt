---
artifact_type: 'PLAN'
planning_level: 'STREAM'
initiative_id: 'P'
initiative_code: 'PROGRAM'
phase: '0'
stream_id: 'P-PH000-ST001'
version: '0.1.3'
date: '2026-02-20'
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
| AC002 | `P-PH000-ST001-AC002` | Author `P-STD-001` (Full Promotion from T102-STD-004) | `in_progress` | LLM_Consultant | AC001 | `standard_P-STD-001_program-governance-standard.md` | `prompt/artifacts/tasks/P/workspace/plan/PH000/ST001/plan_P-PH000-ST001-AC002.md` |
| AC003 | `P-PH000-ST001-AC003` | Author `P-STD-002` + `P-ADR-002` (Program Status Standard) | `planned` | LLM_Consultant | AC001 | Planned standard + paired ADR | Program SSOT |
| AC004 | `P-PH000-ST001-AC004` | Author `P-STD-004` (File Naming & Directory Convention) | `planned` | LLM_Consultant | — | `prompt/artifacts/tasks/P/standard/standard_P-STD-004_file-naming-and-directory-convention.md` | `T102-STD-004-CLAUSE-001A`, `T102-STD-004-CLAUSE-025`, `T102-STD-005-CLAUSE-004`, `T104-PH001-ST002-AC000` (proposal v3.1.0) |
| AC005 | `P-PH000-ST001-AC005` | Align `P/standard/` naming to `standard_<STD-ID>_...` | `planned` | LLM_Developer | AC004 | Renamed `standard_P-STD-003_governance-standards-and-dr-index.md` + updated references | `P-STD-004` Convention 1 + `P` conformance |

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

#### Activity AC003: Author `P-STD-002` + `P-ADR-002` (Program Status Standard)

**Activity ID**: `P-PH000-ST001-AC003`

**Purpose**: Define the canonical program status standard and update protocol. This standard is a prerequisite for authoring the program status artifact in `P-PH000-ST002`.

**Note**: Bodies are planned; they are not authored as part of this changeset.

---

#### Activity AC004: Author `P-STD-004` (File Naming & Directory Convention)

**Activity ID**: `P-PH000-ST001-AC004`

**Purpose**: Author the program-level combined standard-specification file that codifies canonical directory structure and file naming conventions for all initiative directories under `prompt/artifacts/tasks/**`.

**Hard constraints**:
- `T102-STD-004` is the golden exemplar and governing authoring standard for this combined file.
- The combined file MUST follow the canonical combined-file structure defined by `T102-STD-004-CLAUSE-001A`:
  1) `# <STD-ID> — <Title>`
  2) `## Specification`
  3) `## Decision Record`
  4) `## References`
  5) `## Provenance`
- The `## Specification` section MUST author enforceable `CLAUSE` items consistent with `T102-STD-004-CLAUSE-018` and `T102-STD-005-CLAUSE-005D (Specification Clause Semantics)`.
- The `## Decision Record` section MUST contain a nested decision record using the `T102-STD-004-CLAUSE-025 (DR Body Template)` format (e.g., `P-STD-004-ADR-001`).
- Cross-scope and cross-initiative references inside normative bodies MUST follow `T102-STD-005-CLAUSE-004 (Reference Semantics)` (including the `External Reference:` line rule where applicable).

**Primary input (approved proposal seed)**:
- `prompt/artifacts/tasks/T104/workspace/PH001/ST002/proposal/proposal_T104-PH001-ST002-AC000_directory-naming-convention.md` (v3.1.0, 2026-02-18; include `verification_` and `dev-report_`)

**Deliverable**:
- `prompt/artifacts/tasks/P/standard/standard_P-STD-004_file-naming-and-directory-convention.md`

**Task Register**:
| Task ID | Description | Status | Action |
|:--|:--|:--|:--|
| `P-PH000-ST001-AC004-TK000` | Confirm and codify combined STD filename convention: `standard_<STD-ID>_<kebab-title>.md` (where `<STD-ID>` conforms to `T102-STD-005-CLAUSE-001`) | `planned` | — |
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

#### Activity AC005: Align `P/standard/` Naming to `standard_<STD-ID>_...`

**Activity ID**: `P-PH000-ST001-AC005`

**Purpose**: Remove program-level naming drift by aligning existing program combined standard-specification files to the `standard_<STD-ID>_<kebab-title>.md` naming convention adopted by `P-STD-004` Convention 1.

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
| v0.1.3 | 2026-02-20 | Amendment | AC002 transitioned to `in_progress`; rebranded to Full Promotion methodology; updated deliverable and scope to match amended activity plan |
| v0.1.0 | 2026-02-05 | Initial | Stream ST001 plan created to enable `P-RES` via T102 governance change and to plan `P-STD-001` / `P-STD-002` authoring |
| v0.1.1 | 2026-02-18 | Amendment | AC004 updated per Client QA: corrected governing `T102-STD-004` clause references, pinned proposal seed to v3.1.0, codified `standard_<STD-ID>_...` naming, added cross-initiative validation requirement, and recorded permanent grandfathering posture for legacy T102 `consultant/standards/` artifacts |
| v0.1.2 | 2026-02-19 | Amendment | Linked AC002 to a dedicated activity plan to promote `T102-STD-004` authoring model into `P-STD-001` and record the T102 AC010 split boundary |
