version: '0.6.0'
date: '2026-02-06'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
governance_rules: 'prompt/templates/consultant/workspace/workspace_documentation_rules.md'
procedural_guideline: 'prompt/templates/consultant/workspace/guideline_workspace_roadmap.md'
parent_plan: 'prompt/artifacts/tasks/T102/consultant/workspace/plan/plan_T102-PH001-ST000.md'
predecessor_roadmap: 'prompt/artifacts/tasks/T102/consultant/workspace/roadmap/roadmap_T102-CWD_phase0.md'
ssot_sps_target: 'prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md'
ssot_concept_target: 'prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md'
---

# PLAN: T102 (CWD) — Phase 1: Standards Baselining & Specification Modularization

## I. EXECUTIVE SUMMARY

**Purpose**: Establish a Phase 1 execution plan to (1) baseline the initiative standards system (`T102-STD-*`) already indexed in SPS and (2) resolve and execute the “Specification overload” problem by modularizing normative specifications while keeping ADRs lean and drift-resistant.

**Phase 1 objective**:
1) Resolve and formalize where “Specification” content lives (ADR vs external spec modules vs STD-layer) with explicit impact analysis on `T102-ADR-004`, `T102-ADR-005`, and `T102-ADR-009`.
2) Create an enforceable, index-based linking approach so SSOT artifacts stay navigable (minimize token/context load) while preserving traceability.
3) Close baseline gaps in `T102-STD-001..009` adoption/verification expectations and align SSOT references.

**Entry criteria**:
- `T102-STD-*` index exists in SPS (“Project Standards”).
- `T102-ADR-004`, `T102-ADR-005`, and `T102-ADR-009` exist in Concept.
- Phase 0 governance realignment direction is accepted (STD as normative reference; ADR as decision log).

**Exit milestone**: **Standards Baselined + Spec Modularization Design Decided + SSOT Rollout Started**

---

## II. PHASE 1 DECISION SUMMARY (LOCKED)

Decisions below are treated as authoritative for Phase 1 planning as of **2026-02-05** (evidence: ST001 AC001–AC004 close-out).

1) **Where-spec-lives model**: **Model D (Combined ADR+Spec Files)** is authoritative for Phase 1.
2) **Execution strategy (Phase 1)**: **Combined ADR+Spec Files**:
   - Each ADR’s body and its embedded `Specification/CLAUSE` content live in a **single dedicated file per ADR** (combined file).
   - Concept becomes the **index-only hub**; ADR indexes point to combined files by **repo-relative Canonical Path**.
   - Phase 1 index granularity is the combined file as a whole (no anchor addressing required in Phase 1 indexing).
3) **Canonical combined-file location (Phase 1)**: `prompt/artifacts/tasks/T102/consultant/standards/` (planned directory; populated during rollout).
4) **Phase 1 stability contract**:
   - Combined-file **names/paths MUST NOT change** in Phase 1 (no renames/moves).
   - Combined files MUST include a clear internal boundary: `## Decision` then `## Specification`.
5) **Index authority**: the authoritative ADR indexes live in **Concept** (Concept as index hub).
6) **Concept scope (Phase 1 minimum)**: populate **ADR Index(es)** with canonical paths; other Concept navigation surfaces may remain skeleton-only in Phase 1.
7) **Phase 2 architectural target (deferred)**: optionally separate ADR vs spec into dedicated artifacts and/or evolve toward native `STD-...-CLAUSE-...` addressing once governance stabilizes.
8) **Specification lifecycle**: Spec CLAUSEs follow a governed lifecycle (Draft→Proposed→Accepted→Amended→Deprecated). Authority flows downward: Spec (normative) → Guideline (informative) → Template (derivative). Changes always propagate from spec to derivatives, never the reverse.
9) **STD-contains-CLAUSE migration (Option C)**: Front-run Phase 2 target — CLAUSE reparented under `STD` as `STDCID`; golden exemplar rebuilt as `T102-STD-004`; section order reversed (`## Specification` first, `## Decision Record` second); alias window per CLAUSE-003B during transition; Phase 1 stability exception (governed rename); all other streams blocked until ST001-AC006 completes.

## III. CONTEXT MATERIALS & PREREQUISITES

**Primary SSOT targets**:
- `prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md`
- `prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md`

**Phase 0 predecessor roadmap**:
- `prompt/artifacts/tasks/T102/consultant/workspace/roadmap/roadmap_T102-CWD_phase0.md`

**Active governance proposals (Phase 0 outputs)**:
- `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_refactor-adr-004-005.md`
- `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_refactor_gdrs_into_std.md`

**Raw consultation transcript reference (design rationale source)**:
- `prompt/artifacts/tasks/T102/consultant/raw/raw_p2.md`

---

## IV. PHASE 1: STANDARDS BASELINING & SPECIFICATION MODULARIZATION

### Stream Register

| Stream | ID | Name | Execution Mode | Depends On | Status | Key Deliverables |
|:--|:--|:--|:--|:--|:--|:--|
| 0 | `T102-PH001-ST000` | Phase Planning & Consultation QA | SEQUENTIAL | — | `planned` | `plan_T102-PH001.md` (this file) + Stream plan files registered |
| 1 | `T102-PH001-ST001` | Template Redesign + Spec Modularization (Merged ST006+ST007) | GATED | ST000 | `in_progress` | `plan_T102-PH001-ST001.md`; Model D decision locked; ADR Index schema + extraction inventory; governance deltas + packaging decision recorded + AC005: ADR-004 golden exemplar + AC006: STD-Contains-CLAUSE governance migration |
| 2 | `T102-PH001-ST002` | T102-STD Baselining & Adoption Closure | PARALLEL | ST001 | `planned` | `plan_T102-PH001-ST002.md`; STD adoption/verification gaps resolved; SSOT references aligned (including ADR-009 exemplar reconciliation) |
| 3 | `T102-PH001-ST003` | SSOT Refactor Rollout & Validation (Model D, Concept) | GATED | ST001 | `planned` | `prompt/artifacts/tasks/T102/consultant/workspace/plan/plan_T102-PH001-ST003.md`; Model D rollout executed + validation checklist evidence |

**Gates (Phase 1)**:
- **No SSOT refactor rollout work** begins until `T102-PH001-ST001-AC002` (ADR Index schema + extraction conventions), `T102-PH001-ST001-AC003` (governance deltas + bounded rollout changeset plan), `T102-PH001-ST001-AC005` (golden exemplar accepted), and `T102-PH001-ST001-AC006` (STD-Contains-CLAUSE governance migration) are completed.
- `T102-PH001-ST001-AC004` (packaging decision) is recorded as: rollout execution occurs in **ST003**.
- **All streams (ST002, ST003) are blocked** until ST001-AC006 completes (STD-contains-CLAUSE migration must land first).

### Activity Register (Phase-level)

| Stream | Activity | Activity ID | Name | Status | Owner | Depends On | Deliverable |
|:--|:--|:--|:--|:--|:--|:--|:--|
| 1 | AC001 | `T102-PH001-ST001-AC001` | Comparative design analysis (Models A/B/C/D) | `completed` | LLM_Consultant | — | Decision-ready comparison + recommendation |
| 1 | AC002 | `T102-PH001-ST001-AC002` | ADR Index Schema + Extraction Conventions (Model D) | `completed` | LLM_Consultant | AC001 | Proposed index schema + conventions + extraction inventory |
| 1 | AC003 | `T102-PH001-ST001-AC003` | Prerequisite governance deltas (Concept-scoped) | `completed` | LLM_Consultant | AC001, AC002 | Delta list + bounded rollout plan + verification checklist |
| 1 | AC004 | `T102-PH001-ST001-AC004` | Rollout packaging decision (activate ST003) | `completed` | Client | AC003 | Stream split decision recorded + ST003 activated |
| 1 | AC005 | `T102-PH001-ST001-AC005` | T102-ADR-004 Redesign & Golden Exemplar | `completed` | LLM_Consultant | AC004 | Extracted + redesigned ADR-004 combined file as golden exemplar; comprehensive CLAUSE update (all 15); aligned guideline + template; spec lifecycle meta-clauses added |
| 1 | AC006 | `T102-PH001-ST001-AC006` | STD-Contains-CLAUSE Governance Migration | `in_progress` | LLM_Consultant | AC005 | T102-STD-004 golden exemplar rebuilt; ADR-005 CLAUSE-002/005D updated; Concept STD Index created; guideline/template v3.0.0; migration script tested |
| 2 | AC001 | `T102-PH001-ST002-AC001` | STD adoption & verification gap analysis | `planned` | LLM_Consultant | — | Gap report + remediation checklist |
| 2 | AC002 | `T102-PH001-ST002-AC002` | STD adoption contract normalization | `planned` | LLM_Consultant | AC001 | Updated STD adoption pointers + deferral rules |
| 2 | AC003 | `T102-PH001-ST002-AC003` | SSOT alignment (SPS + Concept reference hygiene) | `planned` | LLM_Consultant | AC002 | SSOT reference alignment changeset plan |
| 3 | AC001 | `T102-PH001-ST003-AC001` | Execute Concept STD extraction (Model D rollout) | `planned` | LLM_Developer | ST001-AC006 | Combined STD files created + Concept indexes normalized + migration script applied |
| 3 | AC002 | `T102-PH001-ST003-AC002` | Validation & handoff | `planned` | LLM_Consultant | AC001 | Completed validation checklist + closure note |

---

## V. LINKS REGISTER

| Link Type | Target | Path |
|:--|:--|:--|
| Plan (this file) | T102 Phase 1 Plan | `prompt/artifacts/tasks/T102/consultant/workspace/plan/plan_T102-PH001.md` |
| Plan | Stream 1 Plan (PH001-ST001) | `prompt/artifacts/tasks/T102/consultant/workspace/plan/plan_T102-PH001-ST001.md` |
| Plan | Stream 2 Plan (PH001-ST002) | `prompt/artifacts/tasks/T102/consultant/workspace/plan/plan_T102-PH001-ST002.md` |
| Plan | Stream 3 Plan (PH001-ST003) | `prompt/artifacts/tasks/T102/consultant/workspace/plan/plan_T102-PH001-ST003.md` |
| Plan (parent) | T102 Master Plan | `prompt/artifacts/tasks/T102/consultant/workspace/plan/plan_T102-PH001-ST000.md` |
| Roadmap (predecessor) | Phase 0 Roadmap | `prompt/artifacts/tasks/T102/consultant/workspace/roadmap/roadmap_T102-CWD_phase0.md` |
| SSOT | T102 SPS | `prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md` |
| SSOT | T102 Concept | `prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md` |
| Proposal | ADR-004/ADR-005 Proposal | `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_refactor-adr-004-005.md` |
| Proposal | STD Migration Proposal | `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_refactor_gdrs_into_std.md` |
| Governance Rules | Workspace Rules | `prompt/templates/consultant/workspace/workspace_documentation_rules.md` |
| Procedural Guideline | Roadmap Authoring Rules | `prompt/templates/consultant/workspace/guideline_workspace_roadmap.md` |

---

## VI. OPEN QUESTIONS REGISTER

| ID | Topic | Question | Owner | Status | Proposed Date | Resolved Date |
|:--|:--|:--|:--|:--|:--|:--|
| OQ-PH001-001 | Spec Placement | Where is the canonical normative specification stored (ADR vs external spec modules vs STD-layer docs), and what remains inside ADR bodies? | Client | Resolved | 2026-02-02 | 2026-02-03 |
| OQ-PH001-002 | Index Authority | Which SSOT owns the authoritative ADR indexes (SPS vs Concept), and is the other a roll-up mirror? | Client | Resolved | 2026-02-02 | 2026-02-05 |
| OQ-PH001-003 | ID Strategy | With Model D selected, what reference mechanism preserves traceability while respecting `CLAUSE` as ADR-internal? (Phase 1: repo-relative Canonical Path to combined ADR+Spec files; Phase 2 target: optional separation and/or native `STD-CLAUSE` addressing.) | Client | Resolved | 2026-02-02 | 2026-02-05 |

---

## VII. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v0.1.0 | 2026-02-02 | Initial | Phase 1 plan created; registers ST001 (merged ST006+ST007), ST002, and conditional rollout stream placeholder |
| v0.2.0 | 2026-02-04 | Update | Recorded Model C + “Collapsed Stack Lite” Phase 1 decisions; marked ST001-AC001 complete; resolved Phase-level open questions |
| v0.3.0 | 2026-02-05 | Update | Aligned Phase 1 plan to Model D; marked ST001 complete (AC001–AC004); activated ST003 (depends on ST001 only) to enable ST002+ST003 parallel execution |
| v0.4.0 | 2026-02-06 | Plan Amendment | Added AC005 (ADR-004 Redesign & Golden Exemplar) to ST001 via plan amendment; updated ST003 gate dependency from AC004→AC005; added spec lifecycle decision to Phase 1 decision summary |
| v0.5.0 | 2026-02-06 | Completion | Marked Stream ST001 and Activity AC005 as completed; standards system baselining initiated |
| v0.6.0 | 2026-02-06 | Plan Amendment | Reopened ST001 (`completed` → `in_progress`); added AC006 (STD-Contains-CLAUSE Governance Migration); added decision 9 (Option C migration); updated gates — ST002/ST003 blocked until AC006 completes; ST003 dependency updated from AC005 → AC006 |
