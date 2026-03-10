---
artifact_type: 'ANALYSIS'
analysis_type: 'readiness_assessment'
initiative_id: 'T104'
initiative_code: 'CWS'
phase: '1'
stream_id: 'T104-PH001-ST007'
activity_id: 'T104-PH001-ST007-AC005'
version: '2.2.0'
date: '2026-03-11'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
---

# ANALYSIS: T104 (CWS) / PH001 / ST007 / AC005 - T102 Directory Migration Readiness Assessment

## I. Purpose

Readiness assessment for AC005, focused on whether `prompt/artifacts/tasks/T102/**` is sufficiently understood to commission deterministic migration planning and execution under `P-STD-004`.

**v2.0.0 scope expansion**: This revision adds the authoritative file inventory and classification matrix (TK001 deliverable), per-artifact-family routing rules, execution mechanics specifications, and tooling compatibility assessment. It supersedes the v1.0.0 findings-only assessment and is designed to serve as the sole manifest-authoring authority for TK003–TK006.

## II. Authority Surface

- Normative authority: `prompt/artifacts/tasks/P/standard/standard_P-STD-004_file-naming-and-directory-convention.md`
- ID authority: `prompt/artifacts/tasks/P/standard/standard_P-STD-005_universal-id-specification.md`
- Status authority: `prompt/artifacts/tasks/P/standard/standard_P-STD-002_program-status-standard.md`
- Governance authority: `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md`
- Planning guideline: `prompt/templates/consultant/workspace/guideline_workspace_plan.md`
- Stream parent: `prompt/artifacts/tasks/T104/workspace/PH001/ST007/plan_T104-PH001-ST007.md`

## III. Current State Summary

- Total files under `T102/`: `277`
- Root distribution:
  - `consultant/`: `187` files (67.5% of total)
  - `planner/`: `4` files
  - `T102A/`: `18` files
  - `T102B/`: `54` files
  - `T102C/`: `14` files
- Root layout is non-canonical relative to `P-STD-004`:
  - role-scoped roots remain live (`consultant/`, `planner/`)
  - epic roots are inconsistent (`standards/`, `raw/`, `request/`, type-first workspace directories)
  - workspace conformance differs by epic: `T102B` is strongly type-first, `T102C` is partially timeline-first, `T102A` is minimal but non-self-similar

## IV. Readiness Findings

| ID | Category | Scope | Description | Authority / Planning Impact | Required Planning Response |
|:--|:--|:--|:--|:--|:--|
| `T102-READ-001` | Legacy root disposition | `T102/consultant/`, `T102/planner/` | Two live role-scoped roots remain at initiative root. `consultant/` is in active migration scope; `planner/` contains historical content that belongs under canonical archive placement. | `P-STD-004-CLAUSE-002D`, `CLAUSE-009A..G` | Lock root-level disposition rules before manifest authoring. AC005 must migrate `planner/` historical content into `T102/archive/deprecated/...` and remove the legacy root. |
| `T102-READ-002` | Epic root inconsistency | `T102A`, `T102B`, `T102C` | Epic roots do not share a self-similar canonical structure. Example patterns include `standards/`, `raw/`, `request/`, and root-scoped type-first workspace folders. | `P-STD-004-CLAUSE-005B`, `CLAUSE-006A` | Inventory each epic root separately and author epic-specific manifests after a shared classification pass. |
| `T102-READ-003` | Workspace heterogeneity | `T102A`, `T102B`, `T102C`, `consultant/workspace` | Workspace state is not uniform. `T102B` still uses type-first `plan/`, `notes/`, `proposal/`, `roadmap/`; `T102C` uses timeline paths but still contains legacy session-note naming; `consultant/workspace` contains large mixed-scope artifact sets. | `P-STD-004-CLAUSE-003A..J`, `CLAUSE-008D` | AC005 needs a readiness matrix by workspace subtype, not only a folder-to-folder mapping. |
| `T102-READ-004` | Request/design placement ambiguity | `consultant/request/`, `consultant/design/`, epic roots | Legacy request/design artifacts do not map cleanly to a non-canonical `request/` root under the standard. Epic-scoped request/design content belongs under epic `ssot/`. | `P-STD-004-CLAUSE-005B`, `CLAUSE-006A` | The AC005 plan must explicitly route request/design-like artifacts into epic `ssot/`; do not preserve or create new `request/` roots. |
| `T102-READ-005` | Research redistribution complexity | `consultant/research/**` | Research is split across `brief/` and `report/`, contains both root-scoped and epic-scoped identifiers, and includes legacy archive material. | `P-STD-004-CLAUSE-007A..C` | AC005 needs a per-RES classification table and clear rules for live vs archived research before manifest generation. |
| `T102-READ-006` | Archive/historical exception handling | `consultant/**/archive`, `planner/archive`, legacy flat archive files | Historical content exists in multiple pre-standard forms. Some artifacts may move into canonical archive tiers rather than into live surfaces. | `P-STD-004-CLAUSE-009A..G` | AC005 must distinguish live migration from historical archive normalization and encode both in the plan. |
| `T102-READ-007` | Validation acceptance ambiguity | `T102/**` | Literal `0` post-apply errors is not yet supportable without first defining whether AC005 includes all unrelated legacy cleanup. | Planning control issue | Use baseline-plus-allowlist acceptance: no new AC005-caused violations, plus a pre-locked residual allowlist recorded in the readiness package. |
| `T102-READ-008` | Evidence and rollback gap | AC005 execution package | The current stream-plan block has no locked rollback guarantee, no output-directory convention, and only one gate despite larger scope than AC004. | Planning control issue | AC005 must adopt AC004's two-gate evidence model and explicit rollback contract. |
| `T102-READ-009` | SPS/concept routing gap | `consultant/sps/`, `consultant/concept/` | Initiative SPS and concept are under `consultant/sps/` and `consultant/concept/` respectively. These are initiative-level SSOT artifacts and must route to `T102/ssot/` per `P-STD-004-CLAUSE-005A`. The v1.0.0 plan did not explicitly address this family. | `P-STD-004-CLAUSE-005A` | Lock SPS and concept routing to `T102/ssot/`. Archives within these directories route to `T102/archive/`. |
| `T102-READ-010` | `standards/` (plural) naming gap | `consultant/standards/`, `T102A/standards/`, `T102B/standards/` | Three locations use `standards/` (plural). `P-STD-004-CLAUSE-002A` requires `standard/` (singular). This is a directory-rename, not just a file-move. | `P-STD-004-CLAUSE-002A` | Lock the `standards/` → `standard/` rename rule. Each scope routes to its canonical `standard/` directory. |
| `T102-READ-011` | `consultant/external/` disposition gap | `consultant/external/` | Contains 1 file (`external_consultant_second-opinion_IandR-hosting-architecture_2026-02-10.md`). AC000-DEC002 reclassified `workspace/external/` as `analysis_` for T104, but T102 needs its own disposition. | `P-STD-004-CLAUSE-008A` (analysis prefix) | Reclassify as `analysis_` with `analysis_type: external_review` and route to the appropriate workspace timeline scope. |
| `T102-READ-012` | `consultant/workspace/scripts/` disposition gap | `consultant/workspace/scripts/` | Contains a legacy migration script (`migrate_adr_to_std.py`), its `__pycache__/`, and 2 migration reports. These are T102-specific tooling artifacts with no canonical `P-STD-004` placement. | No direct authority | Route the script to `prompt/scripts/migrations/` (existing pattern), route reports to workspace analysis or archive, delete `__pycache__/`. |
| `T102-READ-013` | Nested consultant archives | `consultant/**/archive/` (10+ directories) | At least 10 archive subdirectories exist within consultant (concept, design, request, sps, standards, research/brief, research/report, workspace/plan, workspace/proposal, workspace/roadmap). These must be reclassified under canonical `T102/archive/` tiers. | `P-STD-004-CLAUSE-009A..G` | All nested consultant archives route to canonical `T102/archive/versioned/` or `T102/archive/deprecated/` based on whether the archived content has a live successor. |
| `T102-READ-014` | Multi-manifest execution model gap | AC005 execution | TK003–TK006 produce 4 separate manifests. Existing `migrate_initiative.py` operates on single manifests. Plan must specify execution model. | Planning control issue | Individual manifest runs in locked dependency order (root first, then epics). Each manifest is a separate `migrate_initiative.py` invocation. |
| `T102-READ-015` | Rollback granularity gap | AC005 TK009/TK010 | Two sequential live-apply passes. Rollback target is ambiguous if the epic pass fails after the root pass succeeds. | Planning control issue | Checkpoint captured before TK009 (pre-root-apply). TK009 rollback manifest covers the root pass. TK010 rollback manifest covers the epic pass. Both roll back to pre-TK009 state if needed. |
| `T102-READ-016` | Cross-initiative reference scope gap | AC005 TK011 | AC004.1 demonstrated cross-initiative rewrites (20 files). T102 is referenced from T104 and P artifacts. | AC004.1 precedent | TK011 reference rewrite scope is cross-initiative: scan `prompt/**` for old T102 paths, not just `T102/**`. |
| `T102-READ-017` | Classification matrix schema gap | AC005 TK001 | The v1.0.0 plan does not specify classification matrix schema. Without a locked schema, the developer will improvise the format. | Planning control issue | Lock matrix schema before developer commissioning. |
| `T102-READ-018` | Activity plan template conformance gap | AC005 plan | The original AC005 activity plan did not follow `template_workspace_plan_activity.md`. Tasks lacked Scope, Steps, and per-task Deliverable fields, and `GATE-000` plus pre-`GATE-001` dry-run producer tasks were missing. | `guideline_workspace_plan.md §IV` | Resolved by AC005 plan v2.0.0: added `GATE-000`, detailed `TK003`–`TK012`, and explicit dry-run producer tasks before `GATE-001`. |

## V. Disposition Locks for AC005 Planning

The following decisions are treated as locked for the AC005 planning package:

1. `consultant/` is absorbed into canonical T102 live structures and then removed.
2. `planner/` is historical content and is migrated during AC005 into canonical `T102/archive/deprecated/...` placement, then removed as a legacy root.
3. Request/design-like artifacts are routed into epic `ssot/`, not into new or preserved `request/` roots.
4. Research migration is inventory-driven by commissioning scope and RES identity; brief/report pairs must be co-located.
5. AC005 acceptance is `baseline + explicit allowlist`; the allowlist is authored before any live apply.
6. AC005 uses dry-run and post-apply gates with evidence emitted under `prompt/scripts/output/T104-PH001-ST007-AC005/`.
7. SPS and concept route to `T102/ssot/`; their archives route to `T102/archive/`. _(Added v2.0.0)_
8. `standards/` (plural) directories are renamed to `standard/` (singular) at all scope levels. _(Added v2.0.0)_
9. Nested consultant archives are reclassified under canonical `T102/archive/versioned/` or `T102/archive/deprecated/`. _(Added v2.0.0)_
10. Multi-manifest execution uses individual `migrate_initiative.py` runs per manifest in locked dependency order. _(Added v2.0.0)_
11. Cross-initiative reference rewrite scope: scan `prompt/**`, not just `T102/**`. _(Added v2.0.0)_

## VI. Authoritative File Inventory and Classification Matrix

### A. Classification Matrix Schema

| Column | Description |
|:--|:--|
| `file_path` | Repo-relative path to the live file |
| `root_origin` | Source root (`consultant`, `planner`, `T102A`, `T102B`, `T102C`) |
| `artifact_family` | Artifact type family (`sps`, `concept`, `standard`, `research_brief`, `research_report`, `request`, `design`, `plan`, `notes`, `snotes`, `raw`, `analysis`, `proposal`, `roadmap`, `communication`, `verification`, `external`, `script`, `archive`) |
| `epic_scope` | Epic affinity (`T102` root, `T102A`, `T102B`, `T102C`, or `cross-epic`) |
| `disposition` | Migration action (`live_move`, `archive_versioned`, `archive_deprecated`, `delete`, `exempt`) |
| `target_path` | Canonical target path under `P-STD-004` |
| `notes` | Classification rationale or special handling |

### B. Artifact Family Routing Rules

The following routing rules define the canonical target path for each artifact family. These rules are deterministic and are the manifest-authoring authority for TK003–TK006.

#### B.1 SSOT Artifacts

| Family | Source Pattern | Target Rule | Authority |
|:--|:--|:--|:--|
| SPS (live) | `consultant/sps/sps_T102-CONSULTANT.md` | `T102/ssot/sps_T102-CONSULTANT.md` | `P-STD-004-CLAUSE-005A` |
| SPS (archive) | `consultant/sps/archive/*` | `T102/archive/versioned/ssot/sps_*_v#.#.#.md` or `T102/archive/deprecated/ssot/*` | `P-STD-004-CLAUSE-009A..G` |
| Concept (live) | `consultant/concept/concept_T102-CONSULTANT.md` | `T102/ssot/concept_T102-CONSULTANT.md` | `P-STD-004-CLAUSE-005A` |
| Concept (archive) | `consultant/concept/archive/*` | `T102/archive/versioned/ssot/concept_*_v#.#.#.md` or `T102/archive/deprecated/ssot/*` | `P-STD-004-CLAUSE-009A..G` |

#### B.2 Standards

| Family | Source Pattern | Target Rule | Authority |
|:--|:--|:--|:--|
| Initiative standards (live) | `consultant/standards/T102-STD-*.md` | `T102/standard/T102-STD-*.md` (rename `standards/` → `standard/`; consider `standard_` prefix rename per `P-STD-004-CLAUSE-008A`) | `P-STD-004-CLAUSE-002A..C` |
| Initiative standards (already renamed) | `consultant/standards/standard_T102-STD-004_*.md` | `T102/standard/standard_T102-STD-004_*.md` | `P-STD-004-CLAUSE-002B` |
| Epic standards (T102C) | `consultant/standards/T102C-STD-001_*.md` | `T102C/standard/T102C-STD-001_*.md` | `P-STD-004-CLAUSE-006A` |
| Standards archive | `consultant/standards/archive/*` | `T102/archive/deprecated/standard/*` | `P-STD-004-CLAUSE-009C` |
| T102A standards | `T102A/standards/*` | `T102A/standard/*` (rename directory) | `P-STD-004-CLAUSE-002A` |
| T102B standards | `T102B/standards/*` | `T102B/standard/*` (rename directory) | `P-STD-004-CLAUSE-002A` |

**Note on `standard_` prefix**: Legacy T102 standard filenames use `T102-STD-###_kebab.md` without the `standard_` prefix. `P-STD-004-CLAUSE-008A` requires the `standard_` prefix. The file rename to add the prefix is in-scope for AC005 manifest authoring (except for `standard_T102-STD-004_*.md` which already conforms).

#### B.3 Research

| Family | Source Pattern | Target Rule | Authority |
|:--|:--|:--|:--|
| Initiative-scoped research (live briefs) | `consultant/research/brief/brief_T102-*.md` | `T102/research/<RES-ID>/brief_<RES-ID>_<kebab-topic>.md` | `P-STD-004-CLAUSE-007A..C` |
| Initiative-scoped research (live reports) | `consultant/research/report/report_T102-*.md` | `T102/research/<RES-ID>/report_<RES-ID>_<kebab-topic>.md` | `P-STD-004-CLAUSE-007A..C` |
| Epic-scoped research (T102A) | `consultant/research/brief/brief_T102A-SPS_*.md`, `consultant/research/report/report_T102A-SPS_*.md` | `T102A/research/<RES-ID>/brief_*.md`, `T102A/research/<RES-ID>/report_*.md` | `P-STD-004-CLAUSE-007B` |
| Epic-scoped research (T102B) | `T102B/research/brief/brief_T102B-RES-*.md`, `T102B/research/report/report_T102B-RES-*.md` | `T102B/research/<RES-ID>/brief_*.md`, `T102B/research/<RES-ID>/report_*.md` (co-locate by RES-ID) | `P-STD-004-CLAUSE-007A` |
| Epic-scoped research (T102C) | `consultant/research/brief/brief_T102C-CONCEPT_*.md`, `consultant/research/report/report_T102C-CONCEPT_*.md` | `T102C/research/<RES-ID>/brief_*.md`, `T102C/research/<RES-ID>/report_*.md` | `P-STD-004-CLAUSE-007B` |
| Research archives | `consultant/research/brief/archive/*`, `consultant/research/report/archive/*` | `T102/archive/versioned/research/*` or `T102/archive/deprecated/research/*` | `P-STD-004-CLAUSE-009A..G` |
| Non-standard research artifacts | `consultant/research/report/epic_consultancy_procedural_guideline.md`, `consultant/research/report/T102A/analysis_T102A-comparative.md` | Classify individually (analysis → workspace analysis; guideline → archive deprecated) | Manual classification |

**Research RES-ID Inventory** (live briefs/reports requiring co-location):

| Current Identifier | Canonical RES-ID | Scope | Brief | Report | Current Location | Status |
|:--|:--|:--|:--|:--|:--|:--|
| `T102-CONSULTANT` (concept-analysis) | **`T102-RES-008`** | T102 root | Yes | Yes | `consultant/research/brief/` + `consultant/research/report/` | **Assigned (SES002 amendment)** |
| `T102-CONSULTANT` (research-integration-workflow) | `T102-RES-001` | T102 root | Yes | Yes | `consultant/research/brief/` + `consultant/research/report/` | SPS-mapped; rename pending |
| `T102-CONSULTANT` (roadmap-viability) | `T102-RES-002` | T102 root | Yes | Yes | `consultant/research/brief/` + `consultant/research/report/` | SPS-mapped; rename pending |
| `T102-CONSULTANT` (request-analysis) | **`T102-RES-009`** | T102 root | No | Yes | `consultant/research/report/` | **Assigned (SES002 amendment); brief missing (documented gap)** |
| `T102-RES-003` | `T102-RES-003` | T102 root | Yes | Yes | `consultant/research/brief/` + `consultant/research/report/` | Conformant |
| `T102-RES-004` | `T102-RES-004` | T102 root | Yes | Yes | `consultant/research/brief/` + `consultant/research/report/` | Conformant |
| `T102-RES-005` | `T102-RES-005` | T102 root | Yes | Yes | `consultant/research/brief/` + `consultant/research/report/` | Conformant; concept register gap (resolved) |
| `T102-RES-006` | `T102-RES-006` | T102 root | Yes | Yes | `consultant/research/brief/` + `consultant/research/report/` | Conformant; concept register gap (resolved) |
| `T102-RES-007` | `T102-RES-007` | T102 root | Yes | Yes | `consultant/research/brief/` + `consultant/research/report/` | Conformant; concept register gap (resolved) |
| `T102A-SPS` (sps-workflow-optimization) | `T102A-RES-001` | T102A | Yes | Yes | `consultant/research/brief/` + `consultant/research/report/` | SPS-mapped; rename pending |
| `T102B-RES-001` | `T102B-RES-001` | T102B | Yes | Yes | `T102B/research/brief/` + `T102B/research/report/` | Conformant |
| `T102B-RES-002` | `T102B-RES-002` | T102B | Yes | Yes | `T102B/research/brief/` + `T102B/research/report/` | Conformant |
| `T102C-CONCEPT` (handoff-aggregation) | `T102C-RES-001` | T102C | Yes | Yes | `consultant/research/brief/` + `consultant/research/report/` | SPS-mapped; rename pending |

**Note**: All 13 research identifiers now have canonical `<SCOPE>-RES-###` assignments. 4 were already mapped in the SPS register (rename during TK009/TK010). 2 were newly assigned in the SES002 amendment: `T102-RES-008` (concept-analysis) and `T102-RES-009` (request-analysis). 5 register gaps in `concept_T102-CONSULTANT.md` have been resolved (RES-005..009 rows added). See addendum analysis: `prompt/artifacts/tasks/T104/workspace/PH001/ST007/AC005/analysis/analysis_T104-PH001-ST007-AC005_res-id-canonicalization.md`.

#### B.4 Request/Design Artifacts

| Family | Source Pattern | Target Rule | Authority |
|:--|:--|:--|:--|
| Request (live, epic-scoped) | `consultant/request/request_T102A-SPSST.md` | `T102A/ssot/request_T102A-SPSST.md` | `P-STD-004-CLAUSE-005B`, SES001-DEC004 |
| Request (T102B live) | `T102B/request/request_T102B1-RST.md` | `T102B/ssot/request_T102B1-RST.md` | `P-STD-004-CLAUSE-005B`, SES001-DEC004 |
| Request archives | `consultant/request/archive/*` | `T102/archive/versioned/ssot/*` or `T102A/archive/versioned/ssot/*` | `P-STD-004-CLAUSE-009B` |
| Design (live, epic-scoped) | `consultant/design/design_T102A-SPSST-S*.md` | `T102A/ssot/design_T102A-SPSST-S*.md` | `P-STD-004-CLAUSE-005B`, SES001-DEC004 |
| Design archives | `consultant/design/archive/*` | `T102A/archive/versioned/ssot/*` or `T102A/archive/deprecated/ssot/*` | `P-STD-004-CLAUSE-009B..C` |

#### B.5 Workspace Artifacts (consultant/workspace → T102/workspace)

| Family | Source Pattern | Target Rule | Authority |
|:--|:--|:--|:--|
| Plans (stream/phase level) | `consultant/workspace/plan/plan_T102-PH###*.md` | `T102/workspace/PH###/plan_T102-PH###.md` or `T102/workspace/PH###/ST###/plan_T102-PH###-ST###.md` | `P-STD-004-CLAUSE-003B` |
| Plans (activity level) | `consultant/workspace/plan/PH001/ST001/plan_T102-PH001-ST001-AC###*.md` | `T102/workspace/PH001/ST001/AC###/plan_T102-PH001-ST001-AC###.md` (or `AC###.N/` for sub-activities) | `P-STD-004-CLAUSE-003E..G` |
| Plan archive | `consultant/workspace/plan/archive/*` | `T102/archive/deprecated/workspace/*` or `T102/archive/versioned/workspace/*` | `P-STD-004-CLAUSE-009` |
| Notes registers | `consultant/workspace/notes/notes_T102-PH###*.md` | `T102/workspace/PH###/notes_T102-PH###.md` or `T102/workspace/PH###/ST###/notes_T102-PH###-ST###.md` | `P-STD-004-CLAUSE-003B` |
| Notes (activity-level, legacy `notes_` prefix with AC token) | `consultant/workspace/notes/PH001/ST001/notes_T102-PH001-ST001-AC###*.md` | Rename to `snotes_T102-PH001-ST001-AC###-SES###.md` if session-scoped, else keep as `notes_` register. Place under `T102/workspace/PH001/ST001/AC###/snotes/` or `T102/workspace/PH001/ST001/AC###/`. | `P-STD-004-CLAUSE-008D`, `CLAUSE-003H` |
| Proposals | `consultant/workspace/proposal/proposal_T102-*.md` | Route to `T102/workspace/PH###/ST###/proposal/` or `T102/workspace/PH###/ST###/AC###/proposal/` per scope UID | `P-STD-004-CLAUSE-003F` |
| Proposal archives | `consultant/workspace/proposal/archive/*` | `T102/archive/deprecated/workspace/*` | `P-STD-004-CLAUSE-009C` |
| Roadmaps | `consultant/workspace/roadmap/roadmap_T102-CDW.md` | `T102/ssot/roadmap_T102-CDW.md` | `P-STD-004-CLAUSE-005A` |
| Roadmap archives | `consultant/workspace/roadmap/archive/*` | `T102/archive/deprecated/ssot/*` or `T102/archive/versioned/ssot/*` | `P-STD-004-CLAUSE-009` |
| Analysis | `consultant/workspace/analysis/analysis_T102-*.md` | Route to `T102/workspace/PH###/ST###/analysis/` or `T102/workspace/PH###/ST###/AC###/analysis/` per scope UID | `P-STD-004-CLAUSE-003F` |
| Communication | `consultant/workspace/communication/PH001/ST004/comm_T102-*.md` | `T102/workspace/PH001/ST004/communication/comm_T102-*.md` | `P-STD-004-CLAUSE-003C`, `CLAUSE-008G` |
| Verification | `consultant/workspace/verification/verification_T102-*.md` | Route to `T102/workspace/PH001/ST001/AC###/verification/` per activity scope in filename | `P-STD-004-CLAUSE-003D` |
| Scripts | `consultant/workspace/scripts/migrate_adr_to_std.py` | `prompt/scripts/migrations/migrate_adr_to_std.py` (existing pattern) | No `P-STD-004` rule; follows existing repo convention |
| Script reports | `consultant/workspace/scripts/report_T102_ADR_004_*.md` | `T102/archive/deprecated/workspace/` (historical migration evidence) | `P-STD-004-CLAUSE-009C` |
| `__pycache__/` | `consultant/workspace/scripts/__pycache__/*` | Delete (build artifact, not versioned content) | N/A |

#### B.6 Raw Transcripts

| Family | Source Pattern | Target Rule | Authority |
|:--|:--|:--|:--|
| Consultant raw (timeline-scoped) | `consultant/raw/PH###/ST###/raw_T102-*.txt` | `T102/workspace/PH###/ST###/raw/raw_T102-*.txt` or `T102/workspace/PH###/ST###/AC###/raw/raw_T102-*.txt` per scope UID | `P-STD-004-CLAUSE-003C..D` |
| Consultant raw (PH000, no ST) | `consultant/raw/PH000/raw_T102-*.txt` | `T102/workspace/PH000/raw/raw_T102-*.txt` or classify to a stream | `P-STD-004-CLAUSE-003C` |
| T102A epic raw (root-level) | `T102A/raw/raw_T102A_epic_consultant_*.txt` | `T102A/workspace/PH000/raw/` (historical pre-phase content) | `P-STD-004-CLAUSE-003C` |
| T102A epic raw (timeline) | `T102A/raw/PH001/raw_T102A-PH001-SES001.txt` | `T102A/workspace/PH001/raw/raw_T102A-PH001-SES001.txt` or to stream-level raw | `P-STD-004-CLAUSE-003C` |
| T102B epic raw | `T102B/raw/PH###/...` | `T102B/workspace/PH###/ST###/raw/` per scope UID | `P-STD-004-CLAUSE-003C` |
| T102C epic raw | `T102C/raw/raw_T102C_*.txt` | `T102C/workspace/PH000/raw/` (historical pre-phase content) | `P-STD-004-CLAUSE-003C` |

#### B.7 Epic Workspace Artifacts

| Family | Source Pattern | Target Rule | Authority |
|:--|:--|:--|:--|
| T102A workspace (type-first plan/) | `T102A/workspace/plan/plan_T102A-PH###*.md` | `T102A/workspace/PH###/plan_T102A-PH###.md` or `T102A/workspace/PH###/ST###/plan_T102A-PH###-ST###.md` | `P-STD-004-CLAUSE-003B` |
| T102A workspace (type-first notes/) | `T102A/workspace/notes/*` | Route per timeline UID to `T102A/workspace/PH###/notes_*.md` or `T102A/workspace/PH###/ST###/notes_*.md` or `T102A/workspace/PH###/ST###/AC###/snotes/snotes_*.md` | `P-STD-004-CLAUSE-003B..H` |
| T102A workspace (communication/) | `T102A/workspace/communication/comm_T102A_*.md` | `T102A/workspace/PH001/ST###/communication/comm_T102A_*.md` (scope-aligned) | `P-STD-004-CLAUSE-003C` |
| T102B workspace (type-first plan/) | `T102B/workspace/plan/plan_T102B-PH###*.md` | `T102B/workspace/PH###/plan_T102B-PH###.md` or stream level | `P-STD-004-CLAUSE-003B` |
| T102B workspace (type-first notes/) | `T102B/workspace/notes/*` | Route per timeline UID | `P-STD-004-CLAUSE-003B..H` |
| T102B workspace (type-first analysis/) | `T102B/workspace/analysis/analysis_T102B_*.md` | `T102B/workspace/PH###/ST###/analysis/` per scope | `P-STD-004-CLAUSE-003F` |
| T102B workspace (type-first proposal/) | `T102B/workspace/proposal/*` | `T102B/workspace/PH###/ST###/proposal/` or `T102B/workspace/PH###/ST###/AC###/proposal/` per scope | `P-STD-004-CLAUSE-003F` |
| T102B workspace (type-first roadmap/) | `T102B/workspace/roadmap/roadmap_T102B-*.md` | `T102B/ssot/roadmap_T102B-*.md` | `P-STD-004-CLAUSE-005B` |
| T102C workspace (already timeline) | `T102C/workspace/PH###/*` | Mostly conformant; verify `notes_` vs `snotes_` split and `communication/` placement | `P-STD-004-CLAUSE-003..008D` |
| T102C workspace (communication/) | `T102C/workspace/communication/comm_T102-RES-006_*.md` | `T102C/workspace/PH001/ST###/communication/comm_T102-RES-006_*.md` (scope-aligned) | `P-STD-004-CLAUSE-003C` |

#### B.8 Planner Root

| Family | Source Pattern | Target Rule | Authority |
|:--|:--|:--|:--|
| Planner archive content | `planner/archive/*.md` (4 files) | `T102/archive/deprecated/planner/*.md` | `P-STD-004-CLAUSE-009C`, SES001-DEC002 |

#### B.9 Special Cases

| Item | Source | Disposition | Rationale |
|:--|:--|:--|:--|
| `consultant/external/external_consultant_second-opinion_*.md` | `consultant/external/` | Reclassify as `analysis_` per T104 AC000-DEC002 precedent; route to `T102/workspace/PH001/ST###/analysis/` | `T102-READ-011` |
| `consultant/workspace/scripts/__pycache__/*` | `consultant/workspace/scripts/` | Delete | Build artifact |
| `consultant/research/report/epic_consultancy_procedural_guideline.md` | `consultant/research/report/` | Archive deprecated (not a research report; legacy guideline) | `P-STD-004-CLAUSE-008E` |
| `consultant/research/report/T102A/analysis_T102A-comparative.md` | `consultant/research/report/T102A/` | Reclassify as `analysis_`; route to `T102A/workspace/PH###/ST###/analysis/` | `P-STD-004-CLAUSE-008E` |
| `consultant/research/report/T102A/archive/analysis_T102A-comparative_v1.0.0.md` | `consultant/research/report/T102A/archive/` | `T102A/archive/versioned/workspace/analysis_T102A-comparative_v1.0.0.md` | `P-STD-004-CLAUSE-009B` |
| `T102B/workspace/roadmap/changelog_roadmap_T102B-REQUEST_phase0.md.md` | `T102B/workspace/roadmap/` | Fix double `.md.md` extension; archive to `T102B/archive/deprecated/ssot/` | Filename error |
| `T102B/workspace/notes/notes_T102B-REQUEST_phase0.md` / `notes_T102B-REQUEST_phase0_stream3.md` | `T102B/workspace/notes/` | Route to `T102B/workspace/PH000/` (legacy phase0 content) | AC000-DEC005 precedent |

## VII. Execution Mechanics Specification

### A. Multi-Manifest Execution Model

Manifests SHALL be executed as individual `migrate_initiative.py` invocations in this locked order:

1. **TK003 manifest** (root redistribution): `consultant/` absorption scaffolding + `planner/` archive relocation
2. **TK004 manifest** (T102A): epic structural normalization
3. **TK005 manifest** (T102B): epic structural normalization + type-first workspace conversion
4. **TK006 manifest** (T102C): epic structural normalization + cleanup

Each manifest is a standalone JSON file under `prompt/scripts/output/T104-PH001-ST007-AC005/ac005.1/`.

### B. Rollback Granularity

- **Pre-apply checkpoint**: Captured immediately before TK009 (before any live changes). This is the primary rollback target.
- **TK009 rollback manifest**: Emitted during root redistribution pass. Can revert root-level changes independently.
- **TK010 rollback manifest**: Emitted during epic manifest pass. Can revert epic-level changes independently.
- **Rollback policy**: If TK010 fails, the rollback target is the pre-TK009 checkpoint (full rollback), not the intermediate post-TK009 state. This avoids partial migration states.

### C. Reference Rewrite Scope

TK011 reference rewrite scope is **cross-initiative**: scan all files under `prompt/**` (excluding `prompt/scripts/output/`) for paths containing old T102 paths. This matches the AC004.1 precedent where 20 files across initiatives required rewriting.

### D. Classification Matrix Schema

The classification matrix for TK001 MUST use the schema defined in §VI.A. The matrix SHALL be delivered as a structured markdown table under `prompt/scripts/output/T104-PH001-ST007-AC005/ac005.1/` and SHALL cover every file under `prompt/artifacts/tasks/T102/**`.

## VIII. Tooling Compatibility Assessment

### A. `migrate_initiative.py`

- **Compatible**: single-manifest execution, move/rename operations, dry-run mode, rollback manifest emission, reference rewrite rules.
- **Assessment**: No known incompatibility with AC005 patterns. The multi-manifest model uses sequential individual invocations, which the tool already supports.
- **Risk**: If nested directory moves (e.g., `consultant/workspace/plan/PH001/ST001/` → `T102/workspace/PH001/ST001/`) require deep directory creation, verify that `mkdir -p` equivalent logic exists in the tool.

### B. `validate_initiative_structure.py`

- **Compatible**: `--strict` mode, prefix validation, directory structure checks.
- **Assessment**: The validator must recognize T102 canonical structure post-migration. Pre-migration baseline capture is needed for the allowlist model.
- **Risk**: T102 has initiative-scoped standards at `T102/standard/` AND epic-scoped standards at `T102A/standard/`, `T102B/standard/`, `T102C/standard/`. Verify the validator handles nested epic `standard/` directories correctly.

### C. `archive_manager.py`

- **Compatible**: two-tier archive model, initiative-scoped paths, dry-run mode.
- **Assessment**: The nested consultant archives (10+ directories) will generate a high volume of archive operations. These may be better handled as manifest move operations rather than individual `archive_manager.py` invocations, since the source files are already archived content being relocated, not live files being newly archived.

## IX. Planning Consequences

- AC005 should not remain as an inline stream-plan task register. _(Resolved: dedicated plan created v1.0.0)_
- A dedicated activity plan is required because AC005 exceeds the stream-plan contract-stub threshold and has multiple manifest families, gates, and rollback/evidence constraints. _(Resolved)_
- The first executable planning task is an authoritative inventory and classification pass. Manifest authoring is downstream of that pass, not a substitute for it. _(Resolved: this analysis v2.0.0 serves as TK001 deliverable)_
- The activity plan restructure requirement is now resolved by AC005 plan v2.0.0, which adds `GATE-000`, explicit dry-run producer tasks, and individual detailed sections for `TK003` through `TK012`. _(Resolved)_
- The TK002 gate disposition package is now complete and the Gate-000 GDR records `APPROVE`. _(Resolved)_
- All research identifiers now have canonical RES-ID assignments. The concept register has been updated with 5 new entries (RES-005..009). TK002 GIR-011 locks the canonicalization strategy. _(Resolved: SES002 amendment)_

## X. Verdict

As of v2.2.0, the **inventory and classification work (TK001) and migration contract work (TK002) are complete** within the AC005 planning package. The SES002 amendment resolved OQ001 (RES-ID canonicalization), Gate-000 is closed with an approving GDR, and the AC005 activity plan has been restructured to the activity-plan template with explicit `TK003` through `TK012` execution authority.

AC005 is now implementation-ready for developer commissioning from `TK003` onward.

## XI. Changelog

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v2.2.0 | 2026-03-11 | Amendment | Updated execution references to the rewritten AC005 task model (`TK007`/`TK008` dry-run, `TK009`/`TK010` live apply, `TK011` rewrite, `TK012` validation), marked the plan-structure and TK002 gate-package consequences as resolved, and updated the verdict to implementation-ready following Gate-000 closure and plan v2.0.0. |
| v2.1.0 | 2026-03-10 | Update | Resolved OQ001 (RES-ID canonicalization): updated RES-ID inventory table with canonical assignments for all 13 research identifiers; added cross-reference to addendum analysis; updated planning consequences and verdict. |
| v2.0.0 | 2026-03-10 | Major | Added authoritative file inventory and classification matrix (§VI), per-artifact-family routing rules (§VI.B), execution mechanics specification (§VII), tooling compatibility assessment (§VIII), and 10 new readiness findings (T102-READ-009 through T102-READ-018). Serves as TK001 deliverable. |
| v1.0.0 | 2026-03-09 | Initial | Initial readiness assessment with 8 findings, 6 disposition locks, and recommended activity-plan shape. |
