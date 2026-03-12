# P-STD-004 — File Naming & Directory Convention {#p-std-004-file-naming-and-directory-convention}

## Specification

### Specification Index
| # | Substandard | CLAUSE ID | Title | Description |
|:--|:--|:--|:--|:--|
| 1 | P-STD-004A | P-STD-004-CLAUSE-001 | Initiative Root Structure | Defines canonical root directories for initiatives under `prompt/artifacts/tasks/`. |
| 2 | P-STD-004A | P-STD-004-CLAUSE-002 | Standard Placement | Defines placement and naming of combined standard-specification files. |
| 3 | P-STD-004A | P-STD-004-CLAUSE-003 | Timeline Hierarchy | Defines timeline-organized workspace placement rules and type subdirectories. |
| 4 | P-STD-004A | P-STD-004-CLAUSE-004 | Stream 0 Scoping | Defines `ST000` purpose and naming/placement rules. |
| 5 | P-STD-004A | P-STD-004-CLAUSE-005 | SSOT Organization | Defines self-similar `ssot/` composition across scope levels. |
| 6 | P-STD-004A | P-STD-004-CLAUSE-006 | Epic/Feature Structure | Defines self-similar epic/feature directory structure rules. |
| 7 | P-STD-004A | P-STD-004-CLAUSE-007 | Research Organization | Defines research directory structure and paired brief/report placement. |
| 8 | P-STD-004B | P-STD-004-CLAUSE-008 | File Naming Stems | Defines artifact prefix stems and naming pattern rules. |
| 9 | P-STD-004B | P-STD-004-CLAUSE-009 | Archive Strategy | Defines mirrored archive structure and versioned vs deprecated tiers. |

### P-STD-004A — Directory Structure & Placement

1) **P-STD-004-CLAUSE-001 (Initiative Root Structure)**

   Initiative roots under `prompt/artifacts/tasks/<SID>/` MUST follow a canonical root directory structure for SSOT, standards, research, timeline workspace, and archive.

   * **P-STD-004-CLAUSE-001A (Required root directories)** — Each initiative root MUST include (create on-demand where applicable): `ssot/`, `standard/`, `research/`, `workspace/`, and `archive/`.

   * **P-STD-004-CLAUSE-001B (Canonical skeleton)** — The initiative root structure SHOULD conform to this skeleton (illustrative):
     ```
     prompt/artifacts/tasks/<SID>/
     ├── ssot/
     ├── standard/
     ├── research/
     ├── workspace/
     └── archive/
     ```

   * **P-STD-004-CLAUSE-001C (On-demand creation rule)** — Subdirectories other than the root-level set in `P-STD-004-CLAUSE-001A` MAY be created on-demand when the first artifact requiring that directory is created.

   * **P-STD-004-CLAUSE-001D (Non-canonical roots for new initiatives)** — For new initiatives, root directories under `prompt/artifacts/tasks/<SID>/` SHOULD be limited to the canonical set in `P-STD-004-CLAUSE-001A`. If an additional root directory is introduced, it MUST be explicitly documented as an exception by governance at the initiative scope.

2) **P-STD-004-CLAUSE-002 (Standard Placement)**

   Combined standard-specification files MUST be placed and named according to the designated standards directory and standard filename format.

   * **P-STD-004-CLAUSE-002A (Designated directory)** — Combined standard-specification files MUST live under `prompt/artifacts/tasks/<SID>/standard/` for the relevant scope root (`P` for program standards; `T###...` for initiative-family standards).

   * **P-STD-004-CLAUSE-002B (Filename format)** — Standard files MUST use: `standard_<SID-STD>_<kebab-title>.md`.

   * **P-STD-004-CLAUSE-002C (Slug rules)** — `<kebab-title>` MUST be lowercase kebab-case; spaces MUST be replaced with `-`; repeated `-` MUST be collapsed; non-alphanumeric characters MUST be removed or replaced with `-`.

   * **P-STD-004-CLAUSE-002D (Legacy role-scoped roots)** — Legacy role-scoped root directories (e.g., `consultant/`, `planner/`, `developer/`, `reviewer/`, and legacy standards directories) MAY remain as read-only historical artifacts during migrations; new authoring MUST use `P-STD-004-CLAUSE-002A` and MUST NOT create new role-scoped root directories.

   * **P-STD-004-CLAUSE-002E (Downstream adoption by reference)** — Adopter initiatives SHALL adopt `P-STD-004` by reference as the normative authority for file naming and directory conventions under `prompt/artifacts/tasks/**`. Adopters MUST NOT duplicate or restate `P-STD-004` obligations in initiative-local plans; initiative-local documentation MAY link to relevant `P-STD-004` CLAUSE IDs for context.

3) **P-STD-004-CLAUSE-003 (Timeline Hierarchy)**

   Workspace artifacts MUST be organized using a timeline hierarchy under `workspace/PH###/ST###/` with deterministic activity-scope directories and controlled type subdirectories.

   * **P-STD-004-CLAUSE-003A (Hierarchy)** — `workspace/` MUST be timeline-organized as `workspace/PH###/ST###/` containing activity-scope directories named `AC###/` and, when required, standalone sub-activity directories named `AC###.N/` (directory presence is governed by `P-STD-004-CLAUSE-003E` and `P-STD-004-CLAUSE-003G`).

   * **P-STD-004-CLAUSE-003B (Register placement)** — Phase-level plan and notes register files MUST live directly under `workspace/PH###/`. Stream-level plan and notes register files MUST live directly under `workspace/PH###/ST###/`.

   * **P-STD-004-CLAUSE-003C (Stream-level type subdirectories)** — Stream-level type subdirectories MUST be limited to: `raw/`, `snotes/`, `proposal/`, `analysis/`, `communication/`.

   * **P-STD-004-CLAUSE-003D (Activity-level type subdirectories)** — Activity-level type subdirectories MUST be limited to: `snotes/`, `raw/`, `verification/`, `dev-report/`, `proposal/`, `analysis/`.

   * **P-STD-004-CLAUSE-003E (AC directory trigger rule)** — An activity-scope directory matching the narrowest `AC` token used by associated live files MUST exist; UID identity is the sole trigger (file-count heuristics MUST NOT be used). Undotted activity scope uses `AC###/`; standalone sub-activity scope uses `AC###.N/`.

   * **P-STD-004-CLAUSE-003F (Scope-aligned placement for analysis/proposal)** — `analysis/` and `proposal/` directories MAY exist at stream level and activity level. Placement MUST match the `<scope-UID>` used in the artifact filename:
     - If `<scope-UID>` contains an `AC###.N` token, the artifact MUST be placed under `workspace/PH###/ST###/AC###.N/analysis/` or `workspace/PH###/ST###/AC###.N/proposal/` as appropriate.
     - If `<scope-UID>` contains an undotted `AC###` token, the artifact MUST be placed under `workspace/PH###/ST###/AC###/analysis/` or `workspace/PH###/ST###/AC###/proposal/` as appropriate.
     - Otherwise, the artifact MUST be placed under `workspace/PH###/ST###/analysis/` or `workspace/PH###/ST###/proposal/` as appropriate.

   * **P-STD-004-CLAUSE-003G (Sub-activity directory placement)** — Standalone sub-activity-scoped artifacts with dot-notation IDs (`AC###.N`) MUST use a dedicated sibling activity-scope directory at `workspace/PH###/ST###/AC###.N/` when authoring or relocating live artifacts. If that directory exists, all live sub-activity-scoped `plan_`, `analysis_`, `proposal_`, `verification_`, `dev-report_`, `raw_`, and `snotes_` artifacts MUST be placed there. Legacy parent placement under `workspace/PH###/ST###/AC###/` MAY remain only for backward-compatible historical artifacts and migration-transition reads.

   * **P-STD-004-CLAUSE-003H (Session notes placement)** — Session notes MUST be placed as follows:
     - Phase-scoped session notes (no `ST###`) → `workspace/PH###/snotes/`
     - Stream-scoped session notes (`ST###`, no `AC###`) → `workspace/PH###/ST###/snotes/`
     - Activity-scoped session notes (`AC###`) → `workspace/PH###/ST###/AC###/snotes/`

   * **P-STD-004-CLAUSE-003I (Illustrative workspace skeleton)** — The timeline workspace SHOULD conform to this skeleton (illustrative):
     ```
     workspace/
     └── PH###/
         ├── plan_<SID>-PH###.md
         ├── notes_<SID>-PH###.md
         ├── snotes/
         └── ST###/
             ├── plan_<SID>-PH###-ST###.md
             ├── notes_<SID>-PH###-ST###.md
             ├── raw/
             ├── snotes/
             ├── proposal/
             ├── analysis/
             ├── communication/
             ├── AC###/
                 ├── plan_...-AC###.md
                 ├── snotes/
                 ├── raw/
                 ├── proposal/
                 ├── analysis/
                 ├── verification/
                 └── dev-report/
             └── AC###.N/
                 ├── plan_...-AC###.N.md
                 ├── snotes/
                 ├── raw/
                 ├── proposal/
                 ├── analysis/
                 ├── verification/
                 └── dev-report/
     ```

   * **P-STD-004-CLAUSE-003J (Tooling conformance requirement)** — Validators and scaffolding/migration tools MUST treat the stream-level and activity-level type subdirectory sets as authoritative (including recognition of `snotes/`, `verification/`, and `dev-report/` per `P-STD-004-CLAUSE-003C` and `P-STD-004-CLAUSE-003D`). Tooling MUST recognize dedicated sibling `AC###.N/` directories as the canonical live placement for sub-activity-scoped artifacts and MAY accept parent `AC###/` placement only as a backward-compatible legacy path during migration.

4) **P-STD-004-CLAUSE-004 (Stream 0 Scoping)**

   Each phase SHOULD include a planning/consultation QA stream `ST000`, and Stream 0 artifacts MUST follow the same placement and naming conventions as other streams.

   * **P-STD-004-CLAUSE-004A (Directory)** — Stream 0 MUST be placed at `workspace/PH###/ST000/`.

   * **P-STD-004-CLAUSE-004B (Naming)** — Stream 0 plan and notes register files MUST use: `plan_<SID>-PH###-ST000.md` and `notes_<SID>-PH###-ST000.md`.

5) **P-STD-004-CLAUSE-005 (SSOT Organization)**

   SSOT artifacts MUST be placed under `ssot/` and SHOULD follow a self-similar structure across Initiative, Epic, and Feature scopes.

   * **P-STD-004-CLAUSE-005A (Initiative SSOT)** — Initiative SSOT MUST be placed at `<SID>/ssot/` and MUST contain the initiative SPS and Concept. Additional governance singletons (e.g., roadmap) MAY be placed in `ssot/` when defined by the relevant standards.

   * **P-STD-004-CLAUSE-005B (Epic SSOT)** — Epic SSOT MUST be placed at `<SID>/<EID>/ssot/` and SHOULD contain epic-scoped request/design artifacts when applicable. Additional SSOT singletons MAY be added on-demand subject to governing standards.

   * **P-STD-004-CLAUSE-005C (Feature SSOT)** — Feature SSOT MUST be placed at `<SID>/<EID>/<FEATURE>/ssot/` and SHOULD contain feature-scoped request artifacts when applicable.

6) **P-STD-004-CLAUSE-006 (Epic/Feature Structure)**

   Epic and Feature subdirectories MUST mirror the parent directory structure as a self-similar (fractal) pattern.

   * **P-STD-004-CLAUSE-006A (Epic self-similarity)** — Epic directories `<SID>/<EID>/` MUST be permitted to contain the same root directories as the initiative root (`ssot/`, `standard/`, `research/`, `workspace/`, `archive/`) created on-demand.

   * **P-STD-004-CLAUSE-006B (Feature recursion)** — Feature directories under an epic MUST be permitted to recursively mirror epic structure where needed.

7) **P-STD-004-CLAUSE-007 (Research Organization)**

   Research artifacts MUST be organized by research ID with brief and report co-located at the scope where the research was commissioned.

   * **P-STD-004-CLAUSE-007A (Co-location rule)** — For a given research ID, the brief and report MUST be co-located under a single directory `research/<RES-ID>/`.

   * **P-STD-004-CLAUSE-007B (Scope placement)** — Research MUST be placed at the commissioning scope:
     - Initiative: `<SID>/research/<S-RES>/`
     - Epic: `<SID>/<EID>/research/<EID>-RES-###/`
     - Feature: `<SID>/<EID>/<FEATURE>/research/<FEATURE>-RES-###/`

   * **P-STD-004-CLAUSE-007C (Illustrative skeleton)** — The research directory SHOULD follow this skeleton (illustrative):
     ```
     research/
     └── <RES-ID>/
         ├── brief_<RES-ID>_<kebab-topic>.md
         └── report_<RES-ID>_<kebab-topic>.md
     ```

### P-STD-004B — File Naming & Archival

8) **P-STD-004-CLAUSE-008 (File Naming Stems)**

   Artifact filenames MUST use registered prefix stems and conform to deterministic naming patterns.

   * **P-STD-004-CLAUSE-008A (Prefix registry)** — Artifact files MUST use one of the following prefix stems and naming patterns:
     | Artifact Type | Prefix | Naming Pattern |
     |:--|:--|:--|
     | SPS | `sps_` | `sps_<SID>-<CODE>.md` |
     | Concept | `concept_` | `concept_<SID>-<CODE>.md` |
     | Request | `request_` | `request_<SID>.md` |
     | Design | `design_` | `design_<SID>.md` |
     | Roadmap | `roadmap_` | `roadmap_<SID>-<CODE>.md` |
     | Plan (timeline-derived) | `plan_` | Governed by `P-STD-005-CLAUSE-011` |
     | Notes register/index (timeline-derived) | `notes_` | Governed by `P-STD-005-CLAUSE-011` |
     | Session notes (timeline-derived) | `snotes_` | Governed by `P-STD-005-CLAUSE-011` |
     | Raw transcript (timeline-derived) | `raw_` | Governed by `P-STD-005-CLAUSE-011` |
     | Verification (gate evidence) | `verification_` | Governed by `P-STD-005-CLAUSE-011` |
     | Developer report | `dev-report_` | `dev-report_<activity-UID>_<kebab-topic>_<date>.md` (date = `YYYY-MM-DD`) |
     | Proposal | `proposal_` | `proposal_<scope-UID>_<kebab-topic>.md` |
     | Analysis | `analysis_` | `analysis_<scope-UID>_<kebab-topic>.md` |
     | Communication | `comm_` | `comm_<scope-UID>_<kebab-topic>.md` |
     | Research brief | `brief_` | `brief_<RES-ID>_<kebab-topic>.md` |
     | Research report | `report_` | `report_<RES-ID>_<kebab-topic>.md` |
     | Combined standard | `standard_` | `standard_<SID-STD>_<kebab-title>.md` |

     *Informative*: Within `P-STD-005-CLAUSE-011`, the relevant subclauses are: `P-STD-005-CLAUSE-011A` (plan files), `P-STD-005-CLAUSE-011B` (notes registers), `P-STD-005-CLAUSE-011C` (session notes), `P-STD-005-CLAUSE-011D` (raw transcripts), `P-STD-005-CLAUSE-011E` (verification evidence).

     *Informative*: `dev-report_` is timeline-scoped but uses a date suffix; it is intentionally not governed by `P-STD-005-CLAUSE-011`.

   * **P-STD-004-CLAUSE-008B (Prefix formatting)** — Prefix stems MUST be lowercase and MUST end with `_`.

   * **P-STD-004-CLAUSE-008C (Topic formatting)** — `<kebab-topic>` (and `<kebab-title>`) MUST be lowercase kebab-case.

   * **P-STD-004-CLAUSE-008D (Notes vs session-notes split)** — `notes_` MUST be reserved for register/index files (no `SES###`). Any file containing a `SES###` token MUST use the `snotes_` prefix.

   * **P-STD-004-CLAUSE-008E (Analysis vs report boundary)** — `report_` MUST be reserved for formal research artifacts paired with a `brief_` under a research ID directory. `analysis_` MUST be reserved for ungated workspace synthesis and comparison artifacts and MUST NOT be treated as a research report.

   * **P-STD-004-CLAUSE-008F (Verification scope restriction)** — `verification_` files MUST be created only at gate events and MUST use the gate number in the filename (per `P-STD-005-CLAUSE-011E`).

   * **P-STD-004-CLAUSE-008G (Communication placement rule)** — Communication artifacts SHOULD be placed at the recipient’s workspace path (inbox model) under the stream-level `communication/` directory.

   * **P-STD-004-CLAUSE-008H (`<scope-UID>` definition)** — In this standard’s naming patterns, `<scope-UID>` MUST be either: (a) a timeline UID per `P-STD-005-CLAUSE-001A (Pattern 4)`, or (b) a workscope ID per `P-STD-005-CLAUSE-001A (Patterns 1–3)`. `<scope-UID>` SHOULD identify the narrowest applicable scope. If `<scope-UID>` contains an `AC###` token, placement MUST conform to `P-STD-004-CLAUSE-003F`.

9) **P-STD-004-CLAUSE-009 (Archive Strategy)**

   Each scope root (initiative, and optionally epic) MUST maintain an `archive/` directory that preserves prior versions and deprecated artifacts using a two-tier archive model.

   * **P-STD-004-CLAUSE-009A (Tier directories)** — `archive/` MUST contain the tier directories `archive/versioned/` and `archive/deprecated/` (created on-demand).

   * **P-STD-004-CLAUSE-009B (Versioned snapshot tier)** — Historical snapshots of live files MUST be stored under `archive/versioned/` and MUST append `_v#.#.#` before `.md`. The version MUST be the artifact’s frontmatter `version` at archive time (or an explicit governance override).

   * **P-STD-004-CLAUSE-009C (Deprecated artifact tier)** — Archived files representing deprecated artifacts (no active live successor) MAY be stored under `archive/deprecated/` without a `_v#.#.#` suffix.

   * **P-STD-004-CLAUSE-009D (Live files)** — Live files MUST NOT include a version suffix in the filename; versioning is tracked in artifact metadata and changelogs.

   * **P-STD-004-CLAUSE-009E (Archive trigger)** — Artifacts SHOULD be archived when they undergo a major version bump (v1→v2) or when explicitly requested by governance.

   * **P-STD-004-CLAUSE-009F (Changelog pairing)** — `changelog_*.md` files, if present, MUST be archived alongside their parent artifact using the same tier rules and tier directory as the parent artifact.

   * **P-STD-004-CLAUSE-009G (Tooling)** — Archive operations SHOULD be implemented via the program archive tool (`prompt/scripts/archive_manager.py`), which MUST copy the file into the correct tier directory using the selected archive tier.

## Decision Record

| ADR ID | Title | Status | Supersedes | Date |
|:--|:--|:--|:--|:--|
| `P-STD-004-ADR-001` | Proposal Seed Adoption | `accepted` | — | 2026-02-27 |

* **P-STD-004-ADR-001 (Proposal Seed Adoption)** {#p-std-004-adr-001-proposal-seed-adoption}

  * **Context**
    A single program-level authority is required for deterministic artifact placement and naming across initiatives under `prompt/artifacts/tasks/`. The approved directory and naming conventions exist as proposal material; this ADR records the seed-first promotion of that approved content into a combined standard-specification file so downstream work can reference a normative surface.

  * **Decision**
    Seed `P-STD-004` by structurally promoting the approved proposal conventions into normative CLAUSEs as `draft`. The seed operation is format/structure promotion only (descriptive → normative), with no intended semantic drift. Future changes are applied directly as `P-STD-004` amendments rather than retroactively modifying the seed proposal.

  * **Alternatives**
    * Amend the proposal instead of promoting to a STD — rejected (proposal is approved input; STDs are the normative surface).
    * Perform migrations first, then write the STD — rejected (migrations require an authority surface to validate against).
    * Keep conventions initiative-scoped — rejected (cross-initiative consistency requires a program-level standard).

  * **Consequences**
    (+) Establishes a single authoritative program standard for file/directory conventions.
    (+) Enables downstream migrations and validators to target a stable, normative reference surface.
    (±) Some legacy structures remain grandfathered during migration windows.
    (-) Requires careful amendment governance to avoid drift between conventions, tooling, and existing artifacts.

  * **Traceability**
    * `P-PH000-ST001-AC004-TK001` (Seed task)
    * `P-PH000-ST001-AC004-SES001` (Verification/dev-report consultation input set)
    * `T104-PH001-ST002-AC000` (Approved proposal source)
    * `T104-PH001-ST007-AC001-SES006` (Placement amendments for verification/dev-report)

## References

### External References (Cross-Scope)
| ID | Title | Scope | Source Path |
|:--|:--|:--|:--|
| P-STD-001 | Program Governance Standard | Program (P) | `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md` |
| P-STD-005 | Universal ID Specification | Program (P) | `prompt/artifacts/tasks/P/standard/standard_P-STD-005_universal-id-specification.md` |
| T104-PH001-ST002-AC000 | Directory & File Naming Convention Proposal | Initiative-family (T104) | `prompt/artifacts/tasks/T104/workspace/PH001/ST002/AC000/proposal/proposal_T104-PH001-ST002-AC000_directory-naming-convention.md` |
| T102-CON-009 | Normative Keywords | Initiative-family (T102) | `prompt/artifacts/tasks/T102/ssot/concept_T102-CONSULTANT.md` |

## Provenance

### Status
- `draft` (seeded from approved proposal; GATE-001 passed 2026-02-27; GATE-002 dispositions approved 2026-03-01; pending GATE-003 acceptance review)

### Seed Source
- Proposal v3.4.0: `prompt/artifacts/tasks/T104/workspace/PH001/ST002/AC000/proposal/proposal_T104-PH001-ST002-AC000_directory-naming-convention.md`

### Activity Plan
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC004/plan_P-PH000-ST001-AC004.md`

### Seed Decision Inputs
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC004/snotes/snotes_P-PH000-ST001-AC004-SES001.md`
- `prompt/artifacts/tasks/T104/workspace/PH001/ST007/AC001/snotes/snotes_T104-PH001-ST007-AC001-SES006.md`
