---
artifact_type: 'PROPOSAL'
initiative_id: 'T104'
initiative_code: 'CWS'
activity_id: 'T104-PH001-ST002-AC000'
version: '3.3.0'
date: '2026-02-20'
status: 'approved'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST002/plan_T104-PH001-ST002.md'
analysis_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST002/AC000/analysis/analysis_T104-PH001-ST002-AC000_directory-structure-comparison.md'
external_review_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST002/AC000/analysis/analysis_T104-PH001-ST002-AC000_external-review.md'
session_reference:
  - 'prompt/artifacts/tasks/T104/workspace/PH001/ST002/snotes/snotes_T104-PH001-ST002-SES002.md'
  - 'prompt/artifacts/tasks/T104/workspace/PH001/ST007/AC001/snotes/snotes_T104-PH001-ST007-AC001-SES006.md'
target_standards:
  - 'P-STD-004 (File Naming & Directory Convention)'
  - 'P-STD-005 (Universal ID Specification)'
---

# Proposal: Directory & File Naming Convention (P-STD-004 Input)

## I. PURPOSE

This proposal establishes the canonical directory structure and file naming conventions for initiative artifacts under `prompt/artifacts/tasks/`. It serves as the primary input for `P-STD-004 (File Naming & Directory Convention)` and documents the combined standard-specification file placement convention required by `T102-STD-004-CLAUSE-016`.

**Analysis scope**: T102 and T104 directories (golden exemplars per `T104-PH001-ST002-SES001-DEC002`). Other initiative directories (T103, T300, T801, T810) are future validation targets.

**Supporting analysis**: All structural design decisions are grounded in comparative assessments documented in the companion analysis file (see `analysis_reference` in frontmatter). Each convention references the relevant Design Assessment (DA-###) that provides the weighted criteria matrix and industry research backing.

---

## II. ANALYSIS: CURRENT STATE (T102 + T104)

### A. Directory Structures Observed

**T102 (Initiative-level, with epic nesting)**:
```
prompt/artifacts/tasks/T102/
├── consultant/                     # Role-scoped artifact root (LEGACY)
│   ├── raw/                        # Raw transcripts
│   ├── concept/                    # Concept SSOT (with archive/)
│   ├── sps/                        # SPS SSOT (with archive/)
│   ├── request/                    # Request specs (with archive/)
│   ├── design/                     # Design artifacts (with archive/)
│   ├── research/                   # Research artifacts
│   │   ├── brief/                  # Research briefs
│   │   └── report/                 # Research reports
│   ├── standards/                  # Combined standard-specification files
│   └── workspace/                  # Active workspace
│       ├── notes/                  # Working notes
│       ├── proposal/               # Proposal artifacts
│       │   └── archive/
│       └── scripts/                # Utility scripts
├── T102A/                          # Epic A
│   └── raw/
├── T102B/                          # Epic B (REQUEST)
│   ├── raw/PH###/ST###/            # Hierarchical raw
│   ├── standards/                  # Epic-scoped STD files
│   ├── research/brief/, report/    # Epic-scoped research
│   ├── request/                    # Epic-scoped request spec
│   └── workspace/
│       ├── plan/
│       ├── notes/PH###/ST###/
│       ├── proposal/
│       ├── roadmap/
│       └── analysis/
├── T102C/                          # Epic C
│   └── raw/
└── planner/archive/                # Planner role artifacts
```

**T104 (Initiative-level, simpler structure)**:
```
prompt/artifacts/tasks/T104/
├── raw/                            # Raw transcripts (flat + PH###/ST###/)
├── ssot/                           # SSOT (sps + concept)
├── research/                       # Research artifacts
│   ├── brief/
│   └── report/
├── workspace/                      # Active workspace
│   ├── plan/                       # Plans (flat + PH###/ST###/)
│   ├── notes/                      # Notes (flat + PH###/ST###/ + ST000/)
│   ├── roadmap/                    # Roadmap files
│   ├── analysis/                   # Analysis documents
│   └── proposal/                   # Proposal artifacts
├── T104A/                          # Epic A
│   ├── raw/
│   └── workspace/
│       ├── roadmap/
│       └── notes/
└── (future epics: T104B, T104F, etc.)
```

**P (Program-level)**:
```
prompt/artifacts/tasks/P/
├── raw/PH###/ST###/                # Raw transcripts
├── ssot/                           # Program SPS
├── standard/                       # Program-level combined files
├── workspace/
│   ├── plan/
│   ├── notes/PH###/ST###/
│   └── roadmap/
└── archive/
```

### B. File Naming Patterns Observed

| Artifact Type | Pattern | Examples |
|:--|:--|:--|
| SPS | `sps_<SID>-<CODE>.md` | `sps_T104-CWS.md`, `sps_P-PROGRAM.md` |
| Concept | `concept_<SID>-<CODE>.md` | `concept_T104-CWS.md` |
| Plan (phase) | `plan_<SID>-PH###.md` | `plan_T104-PH001.md`, `plan_P-PH000.md` |
| Plan (stream) | `plan_<SID>-PH###-ST###.md` | `plan_T104-PH001-ST002.md` |
| Plan (activity) | `plan_<SID>-PH###-ST###-AC###.md` | (planned per STD-001) |
| Notes (stream register) | `notes_<SID>-PH###-ST###.md` | `notes_T104-PH001-ST001.md` |
| Notes (activity) | `notes_<SID>-PH###-ST###-AC###.md` | `notes_T104-PH001-ST001-AC000-SES001.md` |
| Notes (phase register) | `notes_<SID>-PH###.md` | `notes_T104-PH001.md` |
| Roadmap | `roadmap_<SID>-<CODE>.md` | `roadmap_T104-CWS.md` |
| Research brief | `brief_<SID>-RES-###_<topic>.md` | `brief_T104-RES-002_requirements-candidate.md` |
| Research report | `report_<SID>-RES-###_<topic>.md` | `report_T104-RES-002_requirements-candidate.md` |
| Raw transcript | `raw_<SID>-<context>_<date>_p#.{txt,md}` | `raw_T104-CWS_2026-01-31_p2.txt` |
| Proposal | `proposal_<context>_<topic>.md` | `proposal_T102-CWD_refactor-adr-004-005.md` |
| Analysis | `analysis_<context>_<topic>.md` | `analysis_T102B_epic-foundation-assessment.md` |
| Combined STD file | `<SID-STD>_<kebab-title>.md` | `standard_T102-STD-004_specification-standard-and-guideline.md` |

### C. Key Drift Points Identified

1. **T102 role-scoped root** (`consultant/`) vs **T104 flat root**: T102 uses `consultant/` as the primary artifact root, placing SSOT, standards, and research under it. T104 places SSOT, research, and workspace directly under the initiative root.

2. **Standards directory naming**: T102 uses `consultant/standards/` (plural). P uses `standard/` (singular). T104 has no standards directory yet.

3. **Legacy naming**: Some T104 files use pre-Phase-1 naming (e.g., `notes_T104-CWS_phase0.md`) that predates the UID convention.

4. **Hierarchical vs flat notes/plans**: Both T102B and T104 use `PH###/ST###/` subdirectories for activity-level files, but stream-register-level files sit at the root of `notes/` or `plan/`.

5. **Research organization**: Brief and report are separated into `brief/` and `report/` subdirectories, splitting paired artifacts.

6. **Raw transcript placement**: Currently at initiative root, separate from the workspace files they correspond to.

---

## III. PROPOSED CONVENTIONS

### Convention 1: Initiative Root Directory Structure
**Grounded in**: DA-001 (Option C recommended, score 3.55/4.0)

Every initiative under `prompt/artifacts/tasks/<SID>/` SHALL follow this canonical structure:

```
prompt/artifacts/tasks/<SID>/
├── ssot/                            # Initiative SSOT (singletons)
│   ├── sps_<SID>-<S-CODE>.md
│   ├── concept_<SID>-<S-CODE>.md
│   └── roadmap_<SID>-<S-CODE>.md     # Initiative roadmap (governance singleton)
├── standard/                        # Combined standard-specification files
│   └── standard_<SID-STD>_<kebab-title>.md
├── research/                        # Initiative-scoped research (by RES ID)
│   └── <S-RES>/
│       ├── brief_<S-RES>_<topic>.md
│       └── report_<S-RES>_<topic>.md
├── workspace/                       # Timeline-organized work
│   ├── PH###/                       # Phase directory
│   │   ├── plan_<SID>-PH###.md     # Phase plan (register)
│   │   ├── notes_<SID>-PH###.md    # Phase notes register
│   │   ├── snotes/                  # Phase-scoped session notes (if any)
│   │   ├── ST###/                   # Stream directory
│   │   │   ├── plan_<SID>-PH###-ST###.md
│   │   │   ├── notes_<SID>-PH###-ST###.md
│   │   │   ├── raw/                 # Stream-scoped raw transcripts
│   │   │   ├── snotes/              # Stream-scoped session notes (if any)
│   │   │   ├── proposal/            # Stream-scoped proposals (if any)
│   │   │   ├── analysis/            # Stream-scoped analyses (if any)
│   │   │   ├── communication/       # Stream-scoped communications (if any)
│   │   │   └── AC###/               # Activity directory (UID-scope trigger rule)
│   │   │       ├── plan_...-AC###[.N].md # Standalone activity/sub-activity plans (DEC006)
│   │   │       ├── snotes/           # Activity-scoped session notes (if any)
│   │   │       ├── raw/              # Activity-scoped raw transcripts
│   │   │       ├── verification/     # Activity gate records (if applicable)
│   │   │       └── dev-report/       # Activity developer reports (if applicable)
│   │   └── ...
│   └── PH###/
│       └── ...
├── <EID>/                          # Epic subdirectory (see Convention 7)
│   └── ...                          # Self-similar structure
└── archive/                         # Single archive with mirrored structure
    └── ...                          # Mirrors live structure (see Convention 8)
```

**Key design decisions**:
- **Timeline-organized workspace** (DA-001 Option C): `workspace/` uses timeline hierarchy (`PH###/ST###/AC###/`) rather than type-first grouping. This provides maximum context locality — plan, notes, raw, proposal, and analysis for a stream all live in the same directory.
- **Cross-cutting root directories**: `ssot/`, `standard/`, and `research/` remain at initiative root as cross-cutting concerns (not timeline-scoped).
- **`standard/`** (singular, not `standards/`): consistent with `P/standard/`.
- **Role-scoped roots deprecated**: `consultant/`, `planner/` roots are deprecated for new initiatives. Existing T102 `consultant/` structure is grandfathered.
- **Raw transcripts co-located** (DA-006 Option B): `raw/` lives inside the timeline hierarchy under `workspace/`, not at initiative root.
- **Roadmap inside SSOT** (DA-004 Option B, revised per SES002-DEC001): The initiative roadmap sits alongside SPS and Concept in `ssot/` as a governance singleton. This reflects the roadmap's nature as an authoritative specification of intent (infrequently updated, broadly referenced). Final roadmap placement will be re-evaluated when T104A (Roadmap Standardization) defines the roadmap artifact type (see `T104-ISSUE-008`).

### Convention 2: File Naming Stems
**Grounded in**: DA-005 (Option A recommended, score 3.70/4.0)

All artifact files MUST use a prefix stem matching the artifact type:

| Artifact Type | Prefix | Naming Pattern |
|:--|:--|:--|
| SPS | `sps_` | `sps_<SID>-<CODE>.md` |
| Concept | `concept_` | `concept_<SID>-<CODE>.md` |
| Request | `request_` | `request_<SID>.md` |
| Design | `design_` | `design_<SID>.md` |
| Plan (all levels) | `plan_` | `plan_<SID>-PH###[-ST###[-AC###]].md` |
| Notes Register / Index | `notes_` | `notes_<SID>-PH###[-ST###[-AC###]].md` |
| Session Notes | `snotes_` | `snotes_<SID>-PH###[-ST###[-AC###]]-SES###.md` |
| Roadmap | `roadmap_` | `roadmap_<SID>-<CODE>.md` |
| Research brief | `brief_` | `brief_<S-RES>_<kebab-topic>.md` |
| Research report | `report_` | `report_<S-RES>_<kebab-topic>.md` |
| Raw transcript | `raw_` | `raw_<timeline-UID>-SES###.{txt,md}` |
| Proposal | `proposal_` | `proposal_<context>_<kebab-topic>.md` |
| Analysis | `analysis_` | `analysis_<context>_<kebab-topic>.md` |
| Combined STD | `standard_` | `standard_<SID-STD>_<kebab-title>.md` |
| Communication | `comm_` | `comm_<SID>-<CODE>.md` |
| Verification | `verification_` | `verification_<activity-UID>_gate-###.md` |
| Developer Report | `dev-report_` | `dev-report_<activity-UID>_<date>.md` |

**Rules**:
- Prefix is always lowercase followed by underscore.
- `<kebab-topic>` uses lowercase kebab-case.
- Markdown extension `.md` is mandatory.
- Plan/notes files use the timeline UID hierarchy (defined by T104-STD-002) as the naming stem after the prefix.
- **Notes prefix split** (per `T104-PH001-ST007-AC001-SES005-DEC003`): `notes_` is reserved for register/index notes (no `SES###` token). All session notes files (any file with a `SES###` token) MUST use `snotes_`. Session notes files MUST use a title containing `SESSION NOTES`. Register/index files MUST use a title containing `NOTES REGISTER`. Initial rollout scope is T104 only; cross-initiative adoption is deferred to a program-level `P-STD-004` migration activity.
- **Unified prefix for plan/notes subtypes** (DA-005): Phase plans (registers) and stream/activity plans (content-rich) share the `plan_` prefix. The UID depth (`PH###` vs `PH###-ST###` vs `PH###-ST###-AC###`) and frontmatter `planning_level` encode the semantic distinction. T104-STD-001 will formalize mandatory sections per planning level.
- **`analysis_` vs `report_` boundary**: `report_` is a formal research artifact, always paired with `brief_`, commissioned via T102-STD-006 research workflow, and indexed in SPS III.B.9. `analysis_` is an ungated workspace artifact for ad-hoc synthesis/comparison, not paired with a brief, and not indexed in the SPS research section.
- **`raw_` naming convention** (revised per SES002-DEC002): Raw transcript filenames MUST include the session token (`SES###`) as part of the timeline UID to enable deterministic raw-to-notes traceability. The date component is removed; the SES### token provides sufficient temporal scoping. Example: `raw_T104-PH001-ST002-AC000-SES002.txt`.
- **`comm_` prefix** (per SES002-DEC003): Communication files use the `comm_` prefix (replacing the prior `handoff_brief_` convention). Communication artifacts are primarily used to pass messages between workscope owners (higher to lower scope). Files are placed at the **recipient's** workspace path following an inbox model (e.g., `T104A/workspace/communication/`). Full specification deferred to T104G (Communication Standardization) epic.
- **`verification_` scope** (per SES001-DEC001, DEC003, DEC007): `verification_` is a gated, post-completion quality record produced at activity gate checkpoints. It contains a verdict (PASS / CONDITIONAL APPROVE / FAIL) and a compliance score, and may block downstream work until pre-conditions are resolved. `verification_` files are ONLY produced at gate events (not mid-activity). Naming: `verification_<activity-UID>_gate-###.md` where `gate-###` corresponds to the gate number defined in the stream/activity plan per `guideline_workspace_plan.md §VI.B`. Author: `LLM_Reviewer OR LLM_Consultant` (pending T101 role standardization). This type is semantically distinct from `analysis_` (which is ungated, mid-stream, and produces recommendations rather than verdicts); the two SHALL NOT be merged. A `guideline_workspace_verification.md` companion guideline (planned) will specify the full authoring rules.
- **`dev-report_` scope** (per SES001-DEC006): `dev-report_` is a developer-produced implementation summary authored at the end of a developer activity, documenting task execution, evidence produced, and commits. Detailed authoring rules are deferred to later phases. Current naming pattern: `dev-report_<activity-UID>_<date>.md` (date = `YYYY-MM-DD` execution date). Author: `LLM_Developer` (informative; pending T101).

### [INFORMATIVE] Role-to-Artifact Ownership (Pending T101)

> **Note**: The following table represents the intended future-state role boundaries. It is **informative only** and SHALL NOT be treated as normative until `T101` (Role Standardization) formally defines the role model. Current practice: a single LLM agentic role may produce any artifact type.

| Artifact Type(s) | Intended Author Role |
|:--|:--|
| `proposal_`, `analysis_`, `notes_` | LLM_Consultant |
| `plan_` | LLM_Planner |
| `verification_` | LLM_Reviewer |
| `dev-report_` | LLM_Developer |

*Role definitions and triggering conditions will be standardized by the `T101` initiative.*

### Convention 3: Combined Standard-Specification File Placement

Per `T102-STD-004-CLAUSE-016`, combined standard-specification files:

- **Directory**: `prompt/artifacts/tasks/<SID>/standard/` (initiative-scoped) or `prompt/artifacts/tasks/P/standard/` (program-scoped).
- **File name**: `standard_<SID-STD>_<kebab-title>.md` (e.g., `T104-STD-001_planning-hierarchy.md`).
- **Internal structure**: Per `T102-STD-004-CLAUSE-016` (Specification → Decision Record → References → Provenance).

**Migration note**: T102's existing `consultant/standards/` directory is grandfathered. New T102 standards MAY be placed in `T102/standard/` if a migration is performed as part of a future restructuring stream.

### Convention 4: Timeline Hierarchy Rules
**Grounded in**: DA-001 (Option C) + DA-006 (Option B)

The `workspace/` directory uses a timeline-organized hierarchy:

```
workspace/
├── PH###/                            # Phase level
│   ├── plan_<SID>-PH###.md          # Phase plan
│   ├── notes_<SID>-PH###.md         # Phase notes register
│   └── ST###/                        # Stream level
│       ├── plan_<SID>-PH###-ST###.md
│       ├── notes_<SID>-PH###-ST###.md
│       ├── raw/                      # Stream raw transcripts
│       ├── snotes/                   # Stream-scoped session notes (if any)
│       ├── proposal/                 # Stream proposals (if any)
│       ├── analysis/                 # Stream analyses (if any)
│       ├── communication/            # Stream communications (if any)
│       └── AC###/                    # Activity level (UID-scope trigger rule)
│           ├── plan_...-AC###[.N].md # Standalone activity/sub-activity plans (DEC006)
│           ├── snotes/               # Activity-scoped session notes (if any)
│           ├── raw/                  # Activity raw transcripts
│           ├── verification/         # Activity gate records (if applicable)
│           └── dev-report/           # Activity developer reports (if applicable)
```

**Rules**:
- **Phase-level files** (plan, notes register) live directly inside `PH###/`.
- **Stream-level files** (plan, notes register) live inside `PH###/ST###/`.
- **Activity-level files** (notes) live inside `PH###/ST###/AC###/`.
- **Stream-level type subdirectories** (`raw/`, `snotes/`, `proposal/`, `analysis/`, `communication/`) are created on-demand within the stream directory. Not all streams require all subdirectories.
- **Activity-level type subdirectories** (`snotes/`, `raw/`, `verification/`, `dev-report/`) are created on-demand within the `AC###/` directory. `verification/` and `dev-report/` are placed at activity level because GATEs and developer reports are activity-scoped (per `guideline_workspace_plan.md §VI.B`).
- **AC/ directory trigger (UID-scope; replaces 2+ file threshold)** (per `T104-PH001-ST007-AC001-SES005-DEC002`): An `AC###/` subdirectory SHALL be created when any associated file’s UID contains an `AC###` token. The file-count threshold heuristic (formerly 2+) is retired; UID identity is the sole trigger.
- **Sub-activity plan placement rule** (per `T104-PH001-ST007-AC001-SES005-DEC006`): Sub-activity plans with dot-notation IDs (`AC###.N`) are versioned iterations of the parent activity plan and SHALL be placed inside the parent `AC###/` directory (e.g., `plan_T104-PH001-ST007-AC001.2.md` → `PH001/ST007/AC001/plan_T104-PH001-ST007-AC001.2.md`).
- **Session notes placement rule** (per `T104-PH001-ST007-AC001-SES005-DEC005`):
  - Phase-scoped session notes (`snotes_...` without `ST###`) → `PH###/snotes/`
  - Stream-scoped session notes (`snotes_...` with `ST###` and no `AC###`) → `ST###/snotes/`
  - Activity-scoped session notes (`snotes_...` with `AC###`) → `ST###/AC###/snotes/`
- **`verification/` subdirectory**: Created on-demand within the `AC###/` activity directory when gate-type verification files are produced for that activity. GATEs are activity-scoped per `guideline_workspace_plan.md §VI.B`; verification evidence is co-located with the activity it governs. Verification files are produced post-completion at gate checkpoints (see Convention 2 `verification_` scope rule).
- **`dev-report/` subdirectory**: Created on-demand within the `AC###/` activity directory when developer implementation reports are produced. Developer reports are authored at activity completion; co-location with the activity preserves context locality. Detailed authoring rules deferred to later phases.
  - **Validator note (tooling conformance)**: `prompt/scripts/validate_initiative_structure.py` MUST recognise `snotes/` as a valid type subdirectory at both stream and activity levels, `verification/` and `dev-report/` as valid activity-level type subdirectories, and `snotes_`, `verification_`, and `dev-report_` as valid file prefixes. This is a tooling conformance requirement; the convention already permits these directories/prefixes.

### Convention 5: Stream 0 Naming & ID Scoping

- Stream 0 (`ST000`) is the planning/consultation QA stream for each phase.
- Stream 0 files follow the same naming convention: `plan_T104-PH001-ST000.md`, `notes_T104-PH001-ST000.md`.
- Stream 0 directory: `workspace/PH001/ST000/`.
- IDs within Stream 0 use the standard prefix: `T104-PH001-ST000-SES###`, `T104-PH001-ST000-AC###`.
- This is consistent with `guideline_workspace_notes.md` §2.1.

### Convention 6: SSOT Scope Organization
**Grounded in**: DA-002 (Option C recommended, score 3.85/4.0)

The `ssot/` directory contains authoritative specification surfaces. At each scope level (Initiative, Epic, Feature), the `ssot/` directory holds the specification artifacts appropriate to that scope:

**Initiative-level `ssot/`**:
```
<SID>/ssot/
├── sps_<SID>-<S-CODE>.md
├── concept_<SID>-<S-CODE>.md
└── roadmap_<SID>-<S-CODE>.md
```

**Epic-level `ssot/`**:
```
<EID>/ssot/
├── sps_<EID>-<E-CODE>.md           (optional — trigger conditions TBD per SES002-DEC004)
├── concept_<EID>-<E-CODE>.md       (optional — trigger conditions TBD per SES002-DEC004)
├── request_<EID>.md          (epic-scoped request spec, when applicable)
├── design_<EID>.md           (epic-scoped design spec, when applicable)
└── roadmap_<EID>-<E-CODE>.md       (epic roadmap, when applicable)
```

**Feature-level `ssot/`**:
```
<FEATURE>/ssot/
└── request_<FID>.md       (feature-scoped request spec)
```

**Key principle**: `ssot/` is self-similar across scope levels. Request and design artifacts are SSOT-class specification surfaces and belong in `ssot/`, not in a separate `request/` directory.

**Epic SSOT composition** (per SES002-DEC004): Initiative-level `ssot/` contains `sps_`, `concept_`, and `roadmap_` (required). Epic-level `ssot/` contains `request_` (when applicable) and **optionally** `sps_`/`concept_` (trigger conditions to be defined as T102B and T104 epic development matures). Feature-level `ssot/` contains `request_` (when applicable). The self-similar structure is preserved; mandatory content at each level will be codified when sufficient epic development evidence exists.

### Convention 7: Epic & Feature Subdirectory Structure
**Grounded in**: DA-002 (Option C) — self-similar principle

Epic subdirectories (`<SID>/<EID>/`) mirror the initiative-level structure:

```
<EID>/
├── ssot/                            # Epic SSOT (request, design, sps, concept, roadmap)
├── standard/                        # Epic-scoped STD files (if any)
├── research/                        # Epic-scoped research (by RES ID)
│   └── <EID>-RES-###/
│       ├── brief_<EID>-RES-###_<topic>.md
│       └── report_<EID>-RES-###_<topic>.md
├── workspace/                       # Epic-scoped timeline workspace
│   ├── PH###/
│   │   └── ST###/
│   │       ├── plan_...
│   │       ├── notes_...
│   │       ├── raw/
│   │       ├── proposal/
│   │       └── analysis/
├── <FEATURE>/                       # Feature subdirectory (recursive)
│   ├── ssot/                        # Feature SSOT
│   ├── research/                    # Feature research
│   └── workspace/                   # Feature workspace
└── archive/                         # Epic archive
```

**Rules**:
- Epic mirrors initiative. Feature mirrors epic. The structure is fractal (self-similar).
- Not all subdirectories are required — create on-demand.
- Epic `ssot/` houses `request_`, `design_`, and optionally `sps_`, `concept_` files.
- Feature `ssot/` typically only houses `request_` files.

### Convention 8: Archive Strategy
**Grounded in**: DA-007 (Client-approved direction)

A single `archive/` directory at initiative root (and optionally at epic root) mirrors the live structure:

```
<SID>/
├── archive/
│   ├── ssot/
│   │   └── sps_<SID>-<CODE>_v0.1.0.md
│   ├── standard/
│   │   └── standard_<SID-STD>_<kebab-title>_v1.0.0.md
│   ├── research/
│   │   └── <S-RES>/
│   │       └── report_<S-RES>_<topic>_v1.0.0.md
│   └── workspace/
│       ├── roadmap_<SID>-<CODE>_v1.0.0.md
│       └── PH###/
│           └── ST###/
│               └── plan_<SID>-PH###-ST###_v1.0.0.md
```

**Archive Rules**:
1. **Mirror structure**: Archive mirrors the live directory structure exactly. The path from `archive/<subpath>` matches the path from `<SID>/<subpath>`.
2. **Version suffix**: Archived files MUST append `_v#.#.#` before the `.md` extension. The version comes from the file's frontmatter `version` field at time of archiving.
3. **Live files**: Live (current) files do NOT have a version suffix in their filename. The version is tracked in frontmatter only.
4. **Archive trigger**: A file is archived when it undergoes a major version bump (v1→v2) or when explicitly requested by governance. Minor/patch bumps are tracked in frontmatter + changelog only.
5. **Changelog files**: `changelog_<stem>.md` files, if they exist, are archived alongside their parent artifact using the same version suffix.
6. **Tooling**: Archive operations SHALL be implemented via Python script (per program mandate): `archive_artifact.py <path-to-live-file>` copies the file to the mirrored archive path with version suffix.

### Convention 9: Research Organization
**Grounded in**: DA-003 (Option E recommended, score 3.85/4.0)

Research artifacts are organized by research ID with brief and report co-located:

```
research/
└── <<SID>-RES>/
    ├── brief_<<SID>-RES>_<topic>.md
    └── report_<<SID>-RES>_<topic>.md
```

**Rules**:
- Brief and report for the same research ID are co-located in a single directory.
- Research lives at the scope level where it was commissioned (Initiative, Epic, or Feature).
- Initiative-scoped research: `<SID>/research/<S-RES>/`
- Epic-scoped research: `<SID>/<EID>/research/<EID>-RES-###/`
- Feature-scoped research: `<SID>/<EID>/<FEATURE>/research/<FEATURE>-RES-###/`

---

## IV. P-STD-004 REGISTRATION RECOMMENDATION

The following registration is recommended for `sps_P-PROGRAM.md` Section III.B.7:

**STD Index Row**:
| STD ID | Title | Status | Owner | Effective | Supersedes | Adopts | Verification | Reference |
|:--|:--|:--|:--|:--|:--|:--|:--|:--|
| `P-STD-004` | File Naming & Directory Convention | `planned` | LLM_Consultant | TBD | — | — | Review: initiative dirs conform to naming/directory rules; CI: lint file prefixes + directory structure | `T104-PH001-ST002-AC000` (proposal input) |

**STD Body** (concise normative statement for SPS III.B.7):

> All initiative directories under `prompt/artifacts/tasks/` SHALL follow standardized file naming prefixes and directory structure conventions. This standard will codify deterministic artifact placement to support agentic retrieval and cross-initiative consistency.

**Note**: The full normative specification will be authored as a combined standard-specification file (`P-STD-004_file-naming-directory-convention.md`) once this proposal is approved and promoted. Minimum viable conformance is TBD pending Client approval of this proposal.

---

## V. P-STD-005 REGISTRATION RECOMMENDATION

Per `T104-PH001-ST002-SES001-DEC005` and `T104-PH001-ST002-SES001-DEC006`:

**STD Index Row**:
| STD ID | Title | Status | Owner | Effective | Supersedes | Adopts | Verification | Reference |
|:--|:--|:--|:--|:--|:--|:--|:--|:--|
| `P-STD-005` | Universal ID Specification | `planned` | LLM_Consultant | TBD | — | — | CI: regex validation of all IDs; Review: scope/token compliance | `T102-STD-005`, `T104-STD-002` (promotion sources) |

**STD Body** (concise normative statement for SPS III.B.7):

> All program and initiative artifacts SHALL conform to a unified ID specification governing scope IDs, tokenized IDs, timeline entity UIDs, and file naming derivations. This standard will unify workscope rules (currently `T102-STD-005`) and timeline rules (currently `T104-STD-002`) into a single program-level normative specification. `P-STD-003 (Governance Standards Model)` will serve as an extension of this standard for `STD` token-type specifics.

**Unification intent**: `P-STD-005` will inherit ALL CLAUSEs from `T102-STD-005` + `T104-STD-002`. Once authored, both source standards will be deprecated via `T102-STD-005-CLAUSE-003A (Cross-Scope Re-scope / Promotion Contract)`.

---

## VI. IMPACT ASSESSMENT

### Conformant (no changes needed)
- T104 `ssot/` (sps + concept at initiative root) — already follows Convention 6.
- P `ssot/`, `standard/`, `workspace/` — already follows proposed conventions.
- All plan/notes file naming using `<prefix>_<SID>-PH###-ST###.md` pattern — already follows Convention 2.

### Requires Migration (future ST007)
- T104 workspace reorganization: move from type-first (`plan/`, `notes/`) to timeline-first (`PH###/ST###/`) per Convention 4.
- T104 `raw/` at initiative root: migrate to `workspace/PH###/ST###/raw/` per Convention 4.
- T104 legacy phase 0 files (`notes_T104-CWS_phase0.md`, etc.) — pre-UID naming.
- T104 standards directory: create `T104/standard/` for T104-STD-001/002/003 combined files.
- T104 research: reorganize from `research/brief/` + `research/report/` to `research/<S-RES>/` per Convention 9.
- T102 role-scoped root: grandfathered, but new initiatives MUST NOT replicate.
- T102B `request/` at epic root: migrate to `T102B/ssot/` per Convention 6.

### New Directories Required (for T104 golden exemplar)
- `prompt/artifacts/tasks/T104/standard/` — for combined STD files (AC001-AC003 deliverables).
- `prompt/artifacts/tasks/T104/workspace/PH001/ST###/` — timeline directories per Convention 4.
- `prompt/artifacts/tasks/T104/archive/` — single archive per Convention 8.

---

## VII. IDENTIFIED RISKS

The following risks were identified during external review (SES002) and confirmed by Client. Registration targets are noted; actual registration is a separate action.

| Risk ID | Title | Scope | Description | Registration Target | Mitigation |
|:--|:--|:--|:--|:--|:--|
| T104-RISK-006 | Path depth and LLM token cost | T104 | Deepest canonical path reaches 11 directory levels; long paths consume disproportionate LLM tokens | `sps_T104-CWS.md` | Defer Feature-level nesting until concrete demand; scaffold scripts reduce manual path construction |
| T104-RISK-007 | Activity-level directory proliferation | T104 | Creating AC/ directories for every activity produces near-empty directories | `sps_T104-CWS.md` | AC/ threshold rule (2+ files); codify in P-STD-004 |
| P-RISK-001 | T102 grandfathering creates permanent dual-pattern | P | T102 `consultant/` structure is grandfathered indefinitely; creates two incompatible patterns | `sps_P-PROGRAM.md` | Sunset milestone when T102 enters next phase after current active epics complete |
| P-RISK-002 | P-STD-004 scope creep from T104-driven design | P | Proposal designed from T104 perspective but targets P-level standards; T104-specific choices may get baked in | `sps_P-PROGRAM.md` | P-STD-004 MUST validate against minimum 2 additional initiatives before `effective` status |

**Issue:**

| Issue ID | Title | Scope | Description | Registration Target |
|:--|:--|:--|:--|:--|
| T104-ISSUE-008 | Roadmap placement provisional | T104 | Roadmap moved to `ssot/` per SES002-DEC001, but final placement deferred to T104A (Roadmap Standardization) epic development. Current decision is provisional. | `sps_T104-CWS.md` |

---

## VIII. SCAFFOLDING & TOOLING

**Implementation vehicle**: `T104-PH001-ST007` (Directory Restructuring).

Per program-level mandate, scaffolding and migration tooling SHALL be implemented as Python scripts. The following scripts are anticipated:

| Script | Purpose | Inputs |
|:--|:--|:--|
| `scaffold_initiative.py` | Generate canonical directory structure for a new initiative | Initiative ID, code, phase count, stream list |
| `migrate_initiative.py` | Reorganize existing initiative to conform to conventions (with dry-run mode) | Initiative root path, target convention version |
| `archive_artifact.py` | Copy a live file to its mirrored archive path with version suffix | Path to live file |
| `validate_structure.py` | Lint/validate an initiative directory against the convention | Initiative root path |

**Golden exemplar**: T104 will be restructured as the first conformant initiative during ST007 execution, using these scripts. The scripts will then be available for adoption by other initiatives.

**Pending tooling updates (SES005 GAP-005)**:
- `prompt/scripts/validate_initiative_structure.py` MUST recognise `dev-report/`, `verification/`, and `snotes/` as valid type subdirectories under `ST###/`.
- `prompt/scripts/validate_initiative_structure.py` MUST recognise `snotes_` as the canonical session-notes prefix.
- `prompt/scripts/migrate_initiative.py` MUST implement the UID-scope trigger rule for `AC###/` directory creation and enforce the `snotes/` placement rules when migrating session notes.

**Companion guideline (planned)**: `guideline_workspace_verification.md` — a verification-specific authoring guideline (analogous to `guideline_workspace_plan.md` and `guideline_workspace_notes.md`) defining the required content sections, severity schema, verdict semantics, and naming rules for `verification_` artifacts. This guideline is a prerequisite for any agent or role producing verification files. Authoring to be completed as part of P-STD-004 or as a companion workspace template session.

**Script location**: `prompt/artifacts/tasks/P/workspace/scripts/` (program-level tooling) or `prompt/templates/consultant/workspace/scripts/` (template-level tooling). Location TBD during ST007 planning.

---

## IX. DECISION REQUESTS

This proposal requests Client approval on the following:

| # | Decision | Recommendation | Analysis Reference |
|:--|:--|:--|:--|
| DR-1 | Adopt `standard/` (singular) as canonical standards directory | **Approved** | — |
| DR-2 | Deprecate role-scoped roots (e.g., `consultant/`) for new initiatives | **Approved** | — |
| DR-3 | Adopt timeline-organized workspace (cross-cutting + timeline hybrid) | **Approved** | DA-001 Option C (score 3.55) |
| DR-4 | Register `P-STD-004` and `P-STD-005` as `planned` in SPS | **Approved** | — |
| DR-5 | Approve this proposal as input for P-STD-004 normative specification | **Approved** | — |
| DR-6 | Self-similar SSOT at each scope level (epic SPS/Concept optional, trigger TBD) | **Approved** (amended per SES002-DEC004) | DA-002 Option C (score 3.85) |
| DR-7 | Research organized by RES ID, self-similar across scope levels | **Approved** | DA-003 Option E (score 3.85) |
| DR-8 | Roadmap inside `ssot/` (changed from workspace root) | **Approved** (amended per SES002-DEC001; provisional — defer to T104A via `T104-ISSUE-008`) | DA-004 Option B (score 3.30; revised) |
| DR-9 | Unified `plan_`/`notes_` prefix (differentiation via UID depth + frontmatter) | **Approved** | DA-005 Option A (score 3.70) |
| DR-10 | Raw transcripts co-located under timeline; naming tightened to include SES### | **Approved** (amended per SES002-DEC002) | DA-006 Option B (score 3.55) |
| DR-11 | Single `archive/` with mirrored structure | **Approved** | DA-007 |
| DR-12 | Python scaffolding/migration scripts in ST007 | **Approved** | — |
| DR-13 | `analysis_` artifact type (boundary with `report_` clarified) | **Approved** (amended per SES002-DP009) | — |
| DR-14 | `workspace/proposal/` as canonical proposal directory | **Approved** | — |
| DR-15 | AC/ directory trigger: UID-scope replaces 2+ file count threshold | **Approved** (amended per `T104-PH001-ST007-AC001-SES005-DEC002`) | — |
| DR-16 | Register `verification_` as a canonical artifact type in Convention 2; add `verification/` to Convention 4 type subdirectories; restrict scope to gate events only | **Approved** | SES001-DEC001–DEC007; industry research (CMMI VER, IEEE 1012, DSDM Timebox Review Record) |
| DR-17 | Register `dev-report_` as a canonical artifact type in Convention 2 at high/surface level; add `dev-report/` to Convention 4 type subdirectories; detailed authoring rules deferred | **Approved** | SES001-DEC006 |
| DR-18 | AC/ directory trigger rule revised: UID-scope replaces 2-file count threshold (SES005-DEC002) | **Approved** | `T104-PH001-ST007-AC001-SES005` |
| DR-19 | Sub-activity plan placement rule formalized (SES005-DEC006) | **Approved** | `T104-PH001-ST007-AC001-SES005` |
| DR-20 | `snotes_` prefix for session notes; supersedes `T104-PH001-SES001-DEC003` (SES005-DEC003) | **Approved** | `T104-PH001-ST007-AC001-SES005` |
| DR-21 | `snotes/` type subdirectory added at phase/stream/activity level (SES005-DEC005) | **Approved** | `T104-PH001-ST007-AC001-SES005` |
| DR-22 | `verification/` and `dev-report/` moved from stream-level to activity-level type subdirectories in Convention 4 (SES006-DEC002, SES006-DEC003) | **Approved** | `T104-PH001-ST007-AC001-SES006` |
| DR-23 | `notes_...-AC###.md` removed from Convention 4 AC###/ tree; Activity Notes Register placement governed by notes guideline (SES006-DEC001) | **Approved** | `T104-PH001-ST007-AC001-SES006` |

---

## X. REFERENCES

- `T102-STD-004-CLAUSE-016 (Combined-File Canonical Structure)`
- `T102-STD-005 (ID Specification & Rules)`
- `T104-PH001-ST002-SES001-DEC001` through `T104-PH001-ST002-SES001-DEC009` (stream readiness decisions)
- `P-STD-003 (Program Governance Standards & Decision Records Model)`
- `guideline_workspace_notes.md` (notes naming conventions)
- `guideline_workspace_plan.md` (plan authoring rules)

## XI. PROVENANCE

- `prompt/artifacts/tasks/T104/workspace/PH001/ST002/plan_T104-PH001-ST002.md` (AC000 activity definition)
- `prompt/artifacts/tasks/T104/workspace/PH001/ST002/snotes/snotes_T104-PH001-ST002-SES001.md` (readiness session)
- `prompt/artifacts/tasks/T104/workspace/PH001/ST002/snotes/snotes_T104-PH001-ST002-SES002.md` (SES002: external review assessment + decision finalization)
- `prompt/artifacts/tasks/T104/workspace/PH001/ST002/AC000/raw/raw_T104-PH001-ST002-AC000-SES002.txt` (SES002 raw transcript)
- `prompt/artifacts/tasks/T104/workspace/PH001/ST002/AC000/analysis/analysis_T104-PH001-ST002-AC000_external-review.md` (external consultant review)
- `prompt/artifacts/tasks/T104/workspace/PH001/ST002/AC000/analysis/analysis_T104-PH001-ST002-AC000_directory-structure-comparison.md` (comparative analysis)
- `prompt/artifacts/tasks/T102/consultant/standards/` (T102 STD naming exemplars)
- `prompt/artifacts/tasks/P/standard/` (P-level STD directory exemplar)
- `prompt/artifacts/tasks/P/ssot/sps_P-PROGRAM.md` (P-STD-004/005 registration target)

---

## XII. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-02-10 | Initial | Initial proposal with type-first workspace structure, 6 conventions |
| v2.0.0 | 2026-02-11 | Major | Restructured based on Client QA and comparative analysis (DA-001–DA-007). Key changes: (1) workspace moved from type-first to timeline-first (cross-cutting + timeline hybrid per DA-001); (2) SSOT self-similar at each scope level with request/design inside `ssot/` per DA-002; (3) research organized by RES ID with brief+report co-located, self-similar per DA-003; (4) roadmap at workspace root per DA-004; (5) unified plan/notes prefix retained per DA-005; (6) raw transcripts moved under workspace timeline per DA-006; (7) single archive with mirrored structure per DA-007; (8) added analysis artifact type; (9) added scaffolding/tooling section for ST007; (10) expanded epic/feature convention with self-similar principle; (11) added changelog |
| v3.0.0 | 2026-02-11 | Major | Finalized based on external review assessment + Client QA (SES002). Key changes: (1) roadmap moved from workspace root to ssot/ per DA-004 revision (SES002-DEC001); (2) raw naming tightened to raw_<timeline-UID>-SES###.{txt,md} (SES002-DEC002); (3) handoff_brief_ replaced with comm_ prefix (SES002-DEC003); (4) epic SPS/Concept made optional with trigger TBD (SES002-DEC004); (5) AC/ directory threshold of 2+ files added (SES002-DEC005); (6) analysis_ vs report_ boundary clarified; (7) risks section added (T104-RISK-006/007, P-RISK-001/002); (8) T104-ISSUE-008 registered for roadmap placement deferral to T104A; (9) all DRs approved |
| v3.1.0 | 2026-02-18 | Amendment | Registered two new artifact types at Convention 2: (1) `verification_` (gate-type quality record, post-completion, gate-only scope, `verification_<activity-UID>_gate-###.md` pattern, `verification/` stream-level type subdirectory); (2) `dev-report_` (developer implementation report, high/surface-level only, detailed design deferred, `dev-report_<activity-UID>_<date>.md` pattern, `dev-report/` stream-level type subdirectory). Added informative role-to-artifact ownership table (deferred to T101). Added `guideline_workspace_verification.md` as planned companion deliverable. Added DR-16 (verification_) and DR-17 (dev-report_). Source: P-PH000-ST001-AC004-SES001 consultation. |
| v3.2.0 | 2026-02-19 | Amendment | Five amendments from SES005 GATE-002 QA: (1) DR-15 replaced with UID-scope trigger; (2) sub-activity plan placement rule added; (3) `snotes_` prefix introduced for session notes (supersedes `T104-PH001-SES001-DEC003`); (4) `snotes/` type subdir added at phase/stream/activity level; (5) validator conformance requirements documented for `dev-report/` + `verification/` + `snotes/` and `snotes_`. DRs DR-18 through DR-21 added. DR-16 and DR-17 confirmed `Approved`. Source: `T104-PH001-ST007-AC001-SES005` (2026-02-19). |
| v3.3.0 | 2026-02-20 | Amendment | Three amendments from SES006 AC001.4 readiness review: (1) `notes_...-AC###.md` removed from Convention 4 AC###/ tree — Activity Notes Register is optional and governed by notes guideline (DR-23); (2) `verification/` and `dev-report/` moved from stream-level to activity-level type subdirectories in Convention 4 (DR-22) — GATEs are activity-scoped per `guideline_workspace_plan.md §VI.B`; (3) Convention 4 stream-level type dir list narrowed to `raw/`, `snotes/`, `proposal/`, `analysis/`, `communication/`; activity-level list added as `snotes/`, `raw/`, `verification/`, `dev-report/`; validator note updated. `plan_...-AC###[.N].md` added to AC###/ tree for sub-activity plan visibility. Source: `snotes_T104-PH001-ST007-AC001-SES006.md` (2026-02-20). |
