---
artifact_type: 'PROPOSAL'
initiative_id: 'T104'
initiative_code: 'CWS'
activity_id: 'T104-PH001-ST002-AC000'
version: '2.0.0'
date: '2026-02-11'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T104/workspace/plan/plan_T104-PH001-ST002.md'
analysis_reference: 'prompt/artifacts/tasks/T104/workspace/analysis/analysis_T104-PH001-ST002-AC000_directory-structure-comparison.md'
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
| Notes (activity) | `notes_<SID>-PH###-ST###-AC###.md` | `notes_T104-PH001-ST001-AC000.md` |
| Notes (phase register) | `notes_<SID>-PH###.md` | `notes_T104-PH001.md` |
| Roadmap | `roadmap_<SID>-<CODE>.md` | `roadmap_T104-CWS.md` |
| Research brief | `brief_<SID>-RES-###_<topic>.md` | `brief_T104-RES-002_requirements-candidate.md` |
| Research report | `report_<SID>-RES-###_<topic>.md` | `report_T104-RES-002_requirements-candidate.md` |
| Raw transcript | `raw_<SID>-<context>_<date>_p#.{txt,md}` | `raw_T104-CWS_2026-01-31_p2.txt` |
| Proposal | `proposal_<context>_<topic>.md` | `proposal_T102-CWD_refactor-adr-004-005.md` |
| Analysis | `analysis_<context>_<topic>.md` | `analysis_T102B_epic-foundation-assessment.md` |
| Combined STD file | `<STD-ID>_<kebab-title>.md` | `T102-STD-004_specification-standard-and-guideline.md` |

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

Every initiative under `prompt/artifacts/tasks/<INIT>/` SHALL follow this canonical structure:

```
prompt/artifacts/tasks/<INIT>/
├── ssot/                            # Initiative SSOT (singletons)
│   ├── sps_<INIT>-<CODE>.md
│   └── concept_<INIT>-<CODE>.md
├── standard/                        # Combined standard-specification files
│   └── <STD-ID>_<kebab-title>.md
├── research/                        # Initiative-scoped research (by RES ID)
│   └── <INIT>-RES-###/
│       ├── brief_<INIT>-RES-###_<topic>.md
│       └── report_<INIT>-RES-###_<topic>.md
├── workspace/                       # Timeline-organized work
│   ├── roadmap_<INIT>-<CODE>.md     # Initiative roadmap (flat at workspace root)
│   ├── PH###/                       # Phase directory
│   │   ├── plan_<INIT>-PH###.md     # Phase plan (register)
│   │   ├── notes_<INIT>-PH###.md    # Phase notes register
│   │   ├── ST###/                   # Stream directory
│   │   │   ├── plan_<INIT>-PH###-ST###.md
│   │   │   ├── notes_<INIT>-PH###-ST###.md
│   │   │   ├── raw/                 # Stream-scoped raw transcripts
│   │   │   ├── proposal/            # Stream-scoped proposals (if any)
│   │   │   ├── analysis/            # Stream-scoped analyses (if any)
│   │   │   ├── communication/       # Stream-scoped handoff briefs (if any)
│   │   │   └── AC###/              # Activity directory
│   │   │       ├── notes_...-AC###.md
│   │   │       └── raw/            # Activity-scoped raw transcripts
│   │   └── ...
│   └── PH###/
│       └── ...
├── <EPIC>/                          # Epic subdirectory (see Convention 7)
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
- **Roadmap at workspace root** (DA-004 Option D): The initiative roadmap sits flat at `workspace/` root as the entry point for the timeline hierarchy.

### Convention 2: File Naming Stems
**Grounded in**: DA-005 (Option A recommended, score 3.70/4.0)

All artifact files MUST use a prefix stem matching the artifact type:

| Artifact Type | Prefix | Naming Pattern |
|:--|:--|:--|
| SPS | `sps_` | `sps_<SID>-<CODE>.md` |
| Concept | `concept_` | `concept_<SID>-<CODE>.md` |
| Request | `request_` | `request_<SID>.md` |
| Design | `design_` | `design_<SID>.md` |
| Plan (all levels) | `plan_` | `plan_<INIT>-PH###[-ST###[-AC###]].md` |
| Notes (all levels) | `notes_` | `notes_<INIT>-PH###[-ST###[-AC###]].md` |
| Roadmap | `roadmap_` | `roadmap_<INIT>-<CODE>.md` |
| Research brief | `brief_` | `brief_<INIT>-RES-###_<kebab-topic>.md` |
| Research report | `report_` | `report_<INIT>-RES-###_<kebab-topic>.md` |
| Raw transcript | `raw_` | `raw_<INIT>-<context>_<YYYY-MM-DD>_p#.{txt,md}` |
| Proposal | `proposal_` | `proposal_<context>_<kebab-topic>.md` |
| Analysis | `analysis_` | `analysis_<context>_<kebab-topic>.md` |
| Combined STD | `<STD-ID>_` | `<STD-ID>_<kebab-title>.md` |
| Handoff brief | `handoff_brief_` | `handoff_brief_<SID>-<CODE>.md` |

**Rules**:
- Prefix is always lowercase followed by underscore.
- `<kebab-topic>` uses lowercase kebab-case.
- Markdown extension `.md` is mandatory.
- Plan/notes files use the timeline UID hierarchy (defined by T104-STD-002) as the naming stem after the prefix.
- **Unified prefix for plan/notes subtypes** (DA-005): Phase plans (registers) and stream/activity plans (content-rich) share the `plan_` prefix. The UID depth (`PH###` vs `PH###-ST###` vs `PH###-ST###-AC###`) and frontmatter `planning_level` encode the semantic distinction. T104-STD-001 will formalize mandatory sections per planning level.
- **`analysis_` prefix**: For ungated secondary research/synthesis artifacts. Distinct from `proposal_` which is gated for Client approval.

### Convention 3: Combined Standard-Specification File Placement

Per `T102-STD-004-CLAUSE-016`, combined standard-specification files:

- **Directory**: `prompt/artifacts/tasks/<INIT>/standard/` (initiative-scoped) or `prompt/artifacts/tasks/P/standard/` (program-scoped).
- **File name**: `<STD-ID>_<kebab-title>.md` (e.g., `T104-STD-001_planning-hierarchy.md`).
- **Internal structure**: Per `T102-STD-004-CLAUSE-016` (Specification → Decision Record → References → Provenance).

**Migration note**: T102's existing `consultant/standards/` directory is grandfathered. New T102 standards MAY be placed in `T102/standard/` if a migration is performed as part of a future restructuring stream.

### Convention 4: Timeline Hierarchy Rules
**Grounded in**: DA-001 (Option C) + DA-006 (Option B)

The `workspace/` directory uses a timeline-organized hierarchy:

```
workspace/
├── roadmap_<INIT>-<CODE>.md          # Initiative-level (flat at workspace root)
├── PH###/                            # Phase level
│   ├── plan_<INIT>-PH###.md          # Phase plan
│   ├── notes_<INIT>-PH###.md         # Phase notes register
│   └── ST###/                        # Stream level
│       ├── plan_<INIT>-PH###-ST###.md
│       ├── notes_<INIT>-PH###-ST###.md
│       ├── raw/                      # Stream raw transcripts
│       ├── proposal/                 # Stream proposals (if any)
│       ├── analysis/                 # Stream analyses (if any)
│       ├── communication/            # Stream communications (if any)
│       └── AC###/                    # Activity level
│           ├── notes_...-AC###.md
│           └── raw/                  # Activity raw transcripts
```

**Rules**:
- **Phase-level files** (plan, notes register) live directly inside `PH###/`.
- **Stream-level files** (plan, notes register) live inside `PH###/ST###/`.
- **Activity-level files** (notes) live inside `PH###/ST###/AC###/`.
- **Type subdirectories** (`raw/`, `proposal/`, `analysis/`, `communication/`) are created on-demand within the stream directory. Not all streams require all subdirectories.
- Roadmap is the sole initiative-level file at `workspace/` root.

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
<INIT>/ssot/
├── sps_<INIT>-<CODE>.md
└── concept_<INIT>-<CODE>.md
```

**Epic-level `ssot/`**:
```
<EPIC>/ssot/
├── sps_<EPIC>-<CODE>.md           (if epic has own SPS)
├── concept_<EPIC>-<CODE>.md       (if epic has own Concept)
├── request_<EPIC-SID>.md          (epic-scoped request spec)
└── design_<EPIC-SID>.md           (epic-scoped design spec)
```

**Feature-level `ssot/`**:
```
<FEATURE>/ssot/
└── request_<FEATURE-SID>.md       (feature-scoped request spec)
```

**Key principle**: `ssot/` is self-similar across scope levels. Request and design artifacts are SSOT-class specification surfaces and belong in `ssot/`, not in a separate `request/` directory.

### Convention 7: Epic & Feature Subdirectory Structure
**Grounded in**: DA-002 (Option C) — self-similar principle

Epic subdirectories (`<INIT>/<EPIC>/`) mirror the initiative-level structure:

```
<EPIC>/
├── ssot/                            # Epic SSOT (request, design, sps, concept)
├── standard/                        # Epic-scoped STD files (if any)
├── research/                        # Epic-scoped research (by RES ID)
│   └── <EPIC>-RES-###/
│       ├── brief_<EPIC>-RES-###_<topic>.md
│       └── report_<EPIC>-RES-###_<topic>.md
├── workspace/                       # Epic-scoped timeline workspace
│   ├── roadmap_<EPIC>-<CODE>.md     # Epic roadmap (if applicable)
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
<INIT>/
├── archive/
│   ├── ssot/
│   │   └── sps_<INIT>-<CODE>_v0.1.0.md
│   ├── standard/
│   │   └── <STD-ID>_<kebab-title>_v1.0.0.md
│   ├── research/
│   │   └── <INIT>-RES-###/
│   │       └── report_<INIT>-RES-###_<topic>_v1.0.0.md
│   └── workspace/
│       ├── roadmap_<INIT>-<CODE>_v1.0.0.md
│       └── PH###/
│           └── ST###/
│               └── plan_<INIT>-PH###-ST###_v1.0.0.md
```

**Archive Rules**:
1. **Mirror structure**: Archive mirrors the live directory structure exactly. The path from `archive/<subpath>` matches the path from `<INIT>/<subpath>`.
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
└── <SCOPE>-RES-###/
    ├── brief_<SCOPE>-RES-###_<topic>.md
    └── report_<SCOPE>-RES-###_<topic>.md
```

**Rules**:
- Brief and report for the same research ID are co-located in a single directory.
- Research lives at the scope level where it was commissioned (Initiative, Epic, or Feature).
- Initiative-scoped research: `<INIT>/research/<INIT>-RES-###/`
- Epic-scoped research: `<INIT>/<EPIC>/research/<EPIC>-RES-###/`
- Feature-scoped research: `<INIT>/<EPIC>/<FEATURE>/research/<FEATURE>-RES-###/`

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
- All plan/notes file naming using `<prefix>_<INIT>-PH###-ST###.md` pattern — already follows Convention 2.

### Requires Migration (future ST007)
- T104 workspace reorganization: move from type-first (`plan/`, `notes/`) to timeline-first (`PH###/ST###/`) per Convention 4.
- T104 `raw/` at initiative root: migrate to `workspace/PH###/ST###/raw/` per Convention 4.
- T104 legacy phase 0 files (`notes_T104-CWS_phase0.md`, etc.) — pre-UID naming.
- T104 standards directory: create `T104/standard/` for T104-STD-001/002/003 combined files.
- T104 research: reorganize from `research/brief/` + `research/report/` to `research/<RES-ID>/` per Convention 9.
- T102 role-scoped root: grandfathered, but new initiatives MUST NOT replicate.
- T102B `request/` at epic root: migrate to `T102B/ssot/` per Convention 6.

### New Directories Required (for T104 golden exemplar)
- `prompt/artifacts/tasks/T104/standard/` — for combined STD files (AC001-AC003 deliverables).
- `prompt/artifacts/tasks/T104/workspace/PH001/ST###/` — timeline directories per Convention 4.
- `prompt/artifacts/tasks/T104/archive/` — single archive per Convention 8.

---

## VII. SCAFFOLDING & TOOLING

**Implementation vehicle**: `T104-PH001-ST007` (Directory Restructuring).

Per program-level mandate, scaffolding and migration tooling SHALL be implemented as Python scripts. The following scripts are anticipated:

| Script | Purpose | Inputs |
|:--|:--|:--|
| `scaffold_initiative.py` | Generate canonical directory structure for a new initiative | Initiative ID, code, phase count, stream list |
| `migrate_initiative.py` | Reorganize existing initiative to conform to conventions (with dry-run mode) | Initiative root path, target convention version |
| `archive_artifact.py` | Copy a live file to its mirrored archive path with version suffix | Path to live file |
| `validate_structure.py` | Lint/validate an initiative directory against the convention | Initiative root path |

**Golden exemplar**: T104 will be restructured as the first conformant initiative during ST007 execution, using these scripts. The scripts will then be available for adoption by other initiatives.

**Script location**: `prompt/artifacts/tasks/P/workspace/scripts/` (program-level tooling) or `prompt/templates/consultant/workspace/scripts/` (template-level tooling). Location TBD during ST007 planning.

---

## VIII. DECISION REQUESTS

This proposal requests Client approval on the following:

| # | Decision | Recommendation | Analysis Reference |
|:--|:--|:--|:--|
| DR-1 | Adopt `standard/` (singular) as canonical standards directory | **Approved** | — |
| DR-2 | Deprecate role-scoped roots (e.g., `consultant/`) for new initiatives | **Approved** | — |
| DR-3 | Adopt timeline-organized workspace (cross-cutting + timeline hybrid) | Recommended | DA-001 Option C (score 3.55) |
| DR-4 | Register `P-STD-004` and `P-STD-005` as `planned` in SPS | **Approved** | — |
| DR-5 | Approve this proposal as input for P-STD-004 normative specification | Required for AC000 completion and ST007 gating | — |
| DR-6 | Self-similar SSOT at each scope level (request/design inside `<EPIC>/ssot/`) | Recommended | DA-002 Option C (score 3.85) |
| DR-7 | Research organized by RES ID, self-similar across scope levels | Recommended | DA-003 Option E (score 3.85) |
| DR-8 | Roadmap at workspace root (flat) | Recommended | DA-004 Option D (score 3.35) |
| DR-9 | Unified `plan_`/`notes_` prefix (differentiation via UID depth + frontmatter) | Recommended | DA-005 Option A (score 3.70) |
| DR-10 | Raw transcripts co-located under timeline hierarchy in workspace | Recommended | DA-006 Option B (score 3.55) |
| DR-11 | Single `archive/` with mirrored structure | **Approved** | DA-007 |
| DR-12 | Python scaffolding/migration scripts in ST007 | Recommended | — |
| DR-13 | `analysis_` artifact type for ungated secondary research/synthesis | Recommended | — |
| DR-14 | `workspace/proposal/` as canonical proposal directory | **Approved** | — |

---

## IX. REFERENCES

- `T102-STD-004-CLAUSE-016 (Combined-File Canonical Structure)`
- `T102-STD-005 (ID Specification & Rules)`
- `T104-PH001-ST002-SES001-DEC001` through `T104-PH001-ST002-SES001-DEC009` (stream readiness decisions)
- `P-STD-003 (Program Governance Standards & Decision Records Model)`
- `guideline_workspace_notes.md` (notes naming conventions)
- `guideline_workspace_plan.md` (plan authoring rules)

## X. PROVENANCE

- `prompt/artifacts/tasks/T104/workspace/plan/plan_T104-PH001-ST002.md` (AC000 activity definition)
- `prompt/artifacts/tasks/T104/workspace/notes/PH001/ST002/notes_T104-PH001-ST002-SES001.md` (readiness session)
- `prompt/artifacts/tasks/T104/workspace/analysis/analysis_T104-PH001-ST002-AC000_directory-structure-comparison.md` (comparative analysis)
- `prompt/artifacts/tasks/T102/consultant/standards/` (T102 STD naming exemplars)
- `prompt/artifacts/tasks/P/standard/` (P-level STD directory exemplar)
- `prompt/artifacts/tasks/P/ssot/sps_P-PROGRAM.md` (P-STD-004/005 registration target)

---

## XI. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-02-10 | Initial | Initial proposal with type-first workspace structure, 6 conventions |
| v2.0.0 | 2026-02-11 | Major | Restructured based on Client QA and comparative analysis (DA-001–DA-007). Key changes: (1) workspace moved from type-first to timeline-first (cross-cutting + timeline hybrid per DA-001); (2) SSOT self-similar at each scope level with request/design inside `ssot/` per DA-002; (3) research organized by RES ID with brief+report co-located, self-similar per DA-003; (4) roadmap at workspace root per DA-004; (5) unified plan/notes prefix retained per DA-005; (6) raw transcripts moved under workspace timeline per DA-006; (7) single archive with mirrored structure per DA-007; (8) added analysis artifact type; (9) added scaffolding/tooling section for ST007; (10) expanded epic/feature convention with self-similar principle; (11) added changelog |
