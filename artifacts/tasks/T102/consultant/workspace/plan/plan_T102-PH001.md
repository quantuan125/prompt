version: '0.17.0'
date: '2026-02-11'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
governance_rules: 'prompt/templates/consultant/workspace/workspace_documentation_rules.md'
procedural_guideline: 'prompt/templates/consultant/workspace/guideline_workspace_roadmap.md'
parent_plan: 'prompt/artifacts/tasks/T102/consultant/workspace/plan/plan_T102-PH001-ST000.md'
predecessor_roadmap: 'prompt/artifacts/tasks/T102/consultant/workspace/roadmap/plan_T102-PH000.md'
ssot_sps_target: 'prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md'
ssot_concept_target: 'prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md'
---

# PLAN: T102 (CWD) — Phase 1: Standards Baselining & Specification Modularization

## I. EXECUTIVE SUMMARY

**Purpose**: Establish a Phase 1 execution plan to (1) baseline the initiative standards system (`T102-STD-*`) already indexed in SPS and (2) resolve and execute the “Specification overload” problem by modularizing normative specifications while keeping ADRs lean and drift-resistant.

**Phase 1 objective**:
1) Resolve and formalize where “Specification” content lives (ADR vs external spec modules vs STD-layer) with explicit impact analysis on `T102-STD-004`, `T102-STD-005`, and `T102-STD-009`.
2) Create an enforceable, index-based linking approach so SSOT artifacts stay navigable (minimize token/context load) while preserving traceability.
3) Close baseline gaps in `T102-STD-001..009` adoption/verification expectations and align SSOT references.

**Entry criteria**:
- `T102-STD-*` index exists in SPS (“Project Standards”).
- `T102-STD-004`, `T102-STD-005`, and `T102-STD-009` exist in Concept.
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
9) **STD-contains-CLAUSE migration (Option C)**: Front-run Phase 2 target — CLAUSE reparented under `STD` as `STDCID`; golden exemplar rebuilt as `T102-STD-004`; section order reversed (`## Specification` first, `## Decision Record` second); alias window per CLAUSE-003B during transition; Phase 1 stability exception (governed rename); all other streams were blocked until ST001-AC006 completed (2026-02-08).
10) **Epic-level STD naming convention**: Epic-level ADRs use the same `nnn` number when migrating to STD (e.g., `T102B-STD-001` → `T102B-STD-001`). Consistent with initiative-level convention.
11) **ST002 sequencing (post-ST005 deferral)**: ST002 execution is deferred until all ST005 GATE-001 approvals are recorded. ST002 now operates on the post-amendment STD surface. A dedicated AC000 (ST005 Remediation Accounting & Scope Calibration) accounts for the out-of-sequence execution where ST005 ran before ST002.

## III. CONTEXT MATERIALS & PREREQUISITES

**Primary SSOT targets**:
- `prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md`
- `prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md`

**Phase 0 predecessor roadmap**:
- `prompt/artifacts/tasks/T102/consultant/workspace/roadmap/plan_T102-PH000.md`

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
| 1 | `T102-PH001-ST001` | Template Redesign + Spec Modularization (Merged ST006+ST007) | GATED | ST000 | `in_progress` | `plan_T102-PH001-ST001.md`; Model D decision locked; ADR Index schema + extraction inventory; governance deltas + packaging decision recorded + AC005: ADR-004 golden exemplar + AC006: STD-Contains-CLAUSE governance migration + AC007: STD-004 retitle + global reference propagation + migration script hardening + AC008: STD-004 self-compliance audit & exemplar hardening + AC009: Research-informed STD-004 formalization (depends on RES-007) |
| 2 | `T102-PH001-ST002` | T102-STD Baselining & Adoption Closure | PARALLEL | ST001, ST005 (all GATE-001) | `planned` | `plan_T102-PH001-ST002.md`; post-amendment baselining (adoption/verification gaps resolved); SSOT references aligned |
| 3 | `T102-PH001-ST003` | SSOT Refactor Rollout & Validation (Model D, Concept) | GATED | ST001 | `completed` | `prompt/artifacts/tasks/T102/consultant/workspace/plan/plan_T102-PH001-ST003.md`; Model D rollout executed + validation checklist evidence |
| 4 | `T102-PH001-ST004` | Initiative Research Commissioning | PARALLEL | — | `in_progress` | `plan_T102-PH001-ST004.md`; commission `T102-RES-004/005/006/007` (brief + report + integration recommendations) |
| 5 | `T102-PH001-ST005` | Standards Amendment Execution (Research-Driven) | GATED | ST004 (gate-level per AC); coordination with ST002 | `planned` | `plan_T102-PH001-ST005.md`; STD-007/003/006/001 clause amendments per research integration recommendations |
| 6 | `T102-PH001-ST006` | Option (c) Transition Execution (Concept I&R Aggregation + Hygiene) | GATED | ST005 (gate-level per AC) | `planned` | `plan_T102-PH001-ST006.md`; Concept hygiene + Concept I&R aggregation (pointers-only) + SPS pointer blocks + T102A owner brief |

**Gates (Phase 1)**:
- **ST002 is deferred** until all ST005 GATE-001 approvals are recorded (`T102-PH001-SES001-DEC002`). ST002-AC000 is the first activity and inventories ST005 outcomes.
- **ST001-AC008** (STD-004 self-compliance audit) SHOULD complete before ST002 begins to ensure the exemplar pattern is hardened.
- **No SSOT refactor rollout work** begins until `T102-PH001-ST001-AC002` (ADR Index schema + extraction conventions), `T102-PH001-ST001-AC003` (governance deltas + bounded rollout changeset plan), `T102-PH001-ST001-AC005` (golden exemplar accepted), and `T102-PH001-ST001-AC006` (STD-Contains-CLAUSE governance migration) are completed. (Satisfied 2026-02-08.)
- `T102-PH001-ST001-AC004` (packaging decision) is recorded as: rollout execution occurs in **ST003**.
- **All streams (ST002, ST003) were blocked** until ST001-AC006 completed (STD-contains-CLAUSE migration must land first). (Unblocked 2026-02-08.)
- ST002-AC002-TK005 (ADR-009 exemplar reconciliation) is blocked until ST003-AC001 completes and delivers `T102-STD-009`.
- ST002-AC004 (SSOT alignment plan) depends on ST003-AC001 for the final STD file inventory.
- **ST005 activities are individually gated** on their corresponding ST004 research GATE-003 approvals:
  - ST005-AC001 depends on ST004-AC001 GATE-003 (passed 2026-02-09)
  - ST005-AC002 depends on ST004-AC002 GATE-003 (passed 2026-02-10)
  - ST005-AC003 depends on ST004-AC002 GATE-003 (passed 2026-02-10)
  - ST005-AC004 depends on ST004-AC003 GATE-003 (passed 2026-02-10)
  - ST005-AC005 depends on ST004-AC002 GATE-003 (passed 2026-02-10)
- ST005 has a coordination dependency (non-blocking) on ST002: amendments should align with ST002's normalized adoption/verification pattern.
- **ST001-AC009** depends on ST004-AC004 GATE-002 (RES-007 report accepted). AC009 integrates RES-007 findings into the existing R2 proposal before executing STD-004 formalization.
- **ST001-AC008 TK005/TK006** are superseded by AC009-TK004/TK005 respectively (see SES002-DEC005).
- **ST006 execution is gated on ST005 approvals**: any Concept I&R aggregation register implementation is treated as non-conformant until the required ST005 per-standard approvals (GATE-001) are recorded. (See: `plan_T102-PH001-ST006.md`.)

### Activity Register (Phase-level)

| Stream | Activity | Activity ID | Name | Status | Owner | Depends On | Deliverable |
|:--|:--|:--|:--|:--|:--|:--|:--|
| 1 | AC001 | `T102-PH001-ST001-AC001` | Comparative design analysis (Models A/B/C/D) | `completed` | LLM_Consultant | — | Decision-ready comparison + recommendation |
| 1 | AC002 | `T102-PH001-ST001-AC002` | ADR Index Schema + Extraction Conventions (Model D) | `completed` | LLM_Consultant | AC001 | Proposed index schema + conventions + extraction inventory |
| 1 | AC003 | `T102-PH001-ST001-AC003` | Prerequisite governance deltas (Concept-scoped) | `completed` | LLM_Consultant | AC001, AC002 | Delta list + bounded rollout plan + verification checklist |
| 1 | AC004 | `T102-PH001-ST001-AC004` | Rollout packaging decision (activate ST003) | `completed` | Client | AC003 | Stream split decision recorded + ST003 activated |
| 1 | AC005 | `T102-PH001-ST001-AC005` | T102-STD-004 Redesign & Golden Exemplar | `completed` | LLM_Consultant | AC004 | Extracted + redesigned ADR-004 combined file as golden exemplar; comprehensive CLAUSE update (all 15); aligned guideline + template; spec lifecycle meta-clauses added |
| 1 | AC006 | `T102-PH001-ST001-AC006` | STD-Contains-CLAUSE Governance Migration | `completed` | LLM_Consultant | AC005 | T102-STD-004 golden exemplar rebuilt; ADR-005 updated; Concept STD Index created; guideline/template v3.0.0; migration script validated; TK011 evidence recorded |
| 1 | AC007 | `T102-PH001-ST001-AC007` | STD-004 Retitle + Staged Script Execution Hardening | `completed` | LLM_Consultant | AC006 | STD-004 retitled; anchors regenerated; migration script relocated/hardened; Stage 1+2 global apply completed |
| 1 | AC008 | `T102-PH001-ST001-AC008` | STD-004 Self-Compliance Audit & Exemplar Hardening | `in_progress` | LLM_Consultant | AC007 | Self-compliance audit report + remediated STD-004 + derivative alignment verification |
| 1 | AC009 | `T102-PH001-ST001-AC009` | Research-Informed STD-004 Formalization | `planned` | LLM_Consultant | AC008, ST004-AC004 (GATE-002) | Revised R2 proposal + formalized STD-004 + derivatives + re-audit evidence |
| 2 | AC000 | `T102-PH001-ST002-AC000` | ST005 Remediation Accounting & Scope Calibration | `planned` | LLM_Consultant | All ST005 GATE-001 | ST005 delta coverage inventory + calibrated scope brief |
| 2 | AC001 | `T102-PH001-ST002-AC001` | STD adoption & verification gap analysis (post-amendment) | `planned` | LLM_Consultant | AC000 | Gap inventory + remediation checklist |
| 2 | AC002 | `T102-PH001-ST002-AC002` | STD verification contract normalization | `planned` | LLM_Consultant | AC001 | Consistent verification contract pattern |
| 2 | AC003 | `T102-PH001-ST002-AC003` | STD verification expectations (review checklist) | `planned` | LLM_Consultant | AC002 | Per-STD review-executable checklist |
| 2 | AC004 | `T102-PH001-ST002-AC004` | SSOT alignment plan (SPS + Concept) | `planned` | LLM_Consultant | AC002, AC003, ST006 | Bounded SSOT changeset plan + validation checklist |
| 3 | AC001 | `T102-PH001-ST003-AC001` | Execute STD Migration for Remaining Standards | `completed` | LLM_Developer | ST001-AC007 | 16 STD files migrated + Concept indexes normalized + inline bodies removed |
| 3 | AC002 | `T102-PH001-ST003-AC002` | Validation & Handoff | `completed` | LLM_Consultant | AC001 | Verification checklist evidence + closure note + ST002 unblock |
| 4 | AC001 | `T102-PH001-ST004-AC001` | Commission `T102-RES-004` (Issues & Risks Architecture) | `completed` | LLM_Consultant | — | Brief + report + integration recommendations |
| 4 | AC002 | `T102-PH001-ST004-AC002` | Commission `T102-RES-005` (Cross-Scope Coordination Architecture) | `completed` | LLM_Consultant | — | Brief + report + integration recommendations (absorbs Research Index Placement) |
| 4 | AC003 | `T102-PH001-ST004-AC003` | Commission `T102-RES-006` (Concept Role + Dynamic SSOT Registers) | `in_progress` | LLM_Consultant | AC001 (GATE-002), AC002 (GATE-002) | Brief + report + integration recommendations |
| 4 | AC004 | `T102-PH001-ST004-AC004` | Commission `T102-RES-007` (Standards Authoring Methodology Benchmarking) | `planned` | LLM_Consultant | — | Brief + report + integration recommendations (includes STD-004/STD-009 merger evaluation) |
| 5 | AC001 | `T102-PH001-ST005-AC001` | Amend `T102-STD-007` (Issues & Risks Index) | `planned` | LLM_Consultant | ST004-AC001 GATE-003 (passed) | `T102-STD-007` v2.0.0 (Deltas 1-4 from RES-004) |
| 5 | AC002 | `T102-PH001-ST005-AC002` | Amend `T102-STD-003` (Explicit Inheritance Model) | `planned` | LLM_Consultant | ST004-AC002 GATE-003 (passed) | `T102-STD-003` v2.0.0 (Deltas A1-A4 from RES-005) |
| 5 | AC003 | `T102-PH001-ST005-AC003` | Amend `T102-STD-006` (Research Artifacts Index) | `planned` | LLM_Consultant | ST004-AC002 GATE-003 (passed) | `T102-STD-006` v2.0.0 (Deltas B1-B4 from RES-005) |
| 5 | AC004 | `T102-PH001-ST005-AC004` | Amend `T102-STD-001` (Consultancy Operating Model) | `planned` | LLM_Consultant | ST004-AC003 GATE-003 (passed 2026-02-10) | `T102-STD-001` amended (Deltas A1-A5 from RES-006) |
| 5 | AC005 | `T102-PH001-ST005-AC005` | Amend `T102-STD-005` (ID Specification & Rules) | `planned` | LLM_Consultant | ST004-AC002 GATE-003 (passed) | `T102-STD-005` amended (Deltas C1-C2 from RES-005) |
| 6 | AC001 | `T102-PH001-ST006-AC001` | Concept Link-Integrity Hygiene (Registers) | `planned` | LLM_Consultant | — | Concept register links corrected + verification checklist evidence |
| 6 | AC002 | `T102-PH001-ST006-AC002` | Concept I&R Aggregation Register (Pointers-Only) | `planned` | LLM_Consultant | ST005-AC001/AC004/AC005 GATE-001 (required); ST005-AC003 GATE-001 (conditional) | Updated Concept with I&R aggregation register section |
| 6 | AC003 | `T102-PH001-ST006-AC003` | SPS Pointer Blocks to Concept I&R Aggregation | `planned` | LLM_Consultant | ST006-AC002 | Updated SPS with minimal pointer blocks (no duplicated canonical content) |
| 6 | AC004 | `T102-PH001-ST006-AC004` | T102A Owner Communication Brief (Option (c) Impacts) | `planned` | LLM_Consultant | — | Comm brief under `prompt/artifacts/tasks/T102/T102A/workspace/communication/` |
| 6 | AC005 | `T102-PH001-ST006-AC005` | Gate: Client Acceptance of Option (c) Transition Execution Output | `planned` | Client | AC001–AC004 | Acceptance record + ready-for-downstream confirmation |

---

## V. LINKS REGISTER

| Link Type | Target | Path |
|:--|:--|:--|
| Plan (this file) | T102 Phase 1 Plan | `prompt/artifacts/tasks/T102/consultant/workspace/plan/plan_T102-PH001.md` |
| Plan | Stream 1 Plan (PH001-ST001) | `prompt/artifacts/tasks/T102/consultant/workspace/plan/plan_T102-PH001-ST001.md` |
| Plan | Stream 2 Plan (PH001-ST002) | `prompt/artifacts/tasks/T102/consultant/workspace/plan/plan_T102-PH001-ST002.md` |
| Plan | Stream 3 Plan (PH001-ST003) | `prompt/artifacts/tasks/T102/consultant/workspace/plan/plan_T102-PH001-ST003.md` |
| Plan | Stream 4 Plan (PH001-ST004) | `prompt/artifacts/tasks/T102/consultant/workspace/plan/plan_T102-PH001-ST004.md` |
| Plan | Stream 5 Plan (PH001-ST005) | `prompt/artifacts/tasks/T102/consultant/workspace/plan/plan_T102-PH001-ST005.md` |
| Plan | Stream 6 Plan (PH001-ST006) | `prompt/artifacts/tasks/T102/consultant/workspace/plan/plan_T102-PH001-ST006.md` |
| Plan (parent) | T102 Master Plan | `prompt/artifacts/tasks/T102/consultant/workspace/plan/plan_T102-PH001-ST000.md` |
| Roadmap (predecessor) | Phase 0 Roadmap | `prompt/artifacts/tasks/T102/consultant/workspace/roadmap/plan_T102-PH000.md` |
| SSOT | T102 SPS | `prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md` |
| SSOT | T102 Concept | `prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md` |
| Evidence | SES001 decisions | `prompt/artifacts/tasks/T102/consultant/workspace/notes/PH001/notes_T102-PH001-SES001.md` |
| Raw | SES001 transcript | `prompt/artifacts/tasks/T102/consultant/raw/PH001/raw_T102-PH001-SES001.txt` |
| Proposal | ADR-004/ADR-005 Proposal | `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_refactor-adr-004-005.md` |
| Proposal | STD Migration Proposal | `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_refactor_gdrs_into_std.md` |
| Analysis | RES-006 integration analysis | `prompt/artifacts/tasks/T102/consultant/workspace/analysis/analysis_T102-RES-006_integration-impact.md` |
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
| v0.6.1 | 2026-02-08 | Completion | Marked AC006 as completed and closed ST001; unblocked ST002/ST003 |
| v0.7.0 | 2026-02-08 | Plan Amendment | Registered T102-PH001-ST004 (Initiative Research Commissioning) for T102-RES-004 (Issues & Risks Architecture); added 4 activities (brief, approval, report, integration); runs parallel with all other streams |
| v0.8.0 | 2026-02-08 | Amendment | Registered AC007 completion in ST001. Updated ST003 activity register to reflect major plan rewrite (v1.0.0). Added cross-stream dependency: ST002-AC002/AC004 depends on ST003-AC001. Added Phase 1 decision 10 (epic-level STD naming). |
| v0.9.0 | 2026-02-09 | Plan Amendment | Reframed ST004 as a research commissioning program stream; expanded commissioned initiative research to `T102-RES-004/005/006/007` and updated Phase-level Activity Register accordingly. |
| v0.10.0 | 2026-02-09 | Completion | ST003 closed: AC001 (`completed`) + AC002 (`completed`); Stream Register ST003 → `completed`; 17 STD files validated; ST002 dependencies unblocked; deferred P-STD-003 orphan refs noted in AC002 closure |
| v0.11.0 | 2026-02-09 | Plan Amendment | Resequenced ST004 research program: collapsed old `T102-RES-006` into expanded `T102-RES-005`, renumbered former `T102-RES-007` to `T102-RES-006`, and reduced ST004 activity rows from AC001-AC004 to AC001-AC003. |
| v0.12.0 | 2026-02-09 | Plan Amendment | Registered `T102-PH001-ST005` (Standards Amendment Execution, Research-Driven): 4 activities (AC001 STD-007 from RES-004, AC002-AC004 skeleton from RES-005/006); gate dependencies on ST004 per-AC GATE-003; coordination link with ST002; ST004-AC001 status aligned to `in_progress`. |
| v0.13.0 | 2026-02-10 | Update | ST004: AC001 → completed, AC002 → completed, AC003 → in_progress; ST004 stream → in_progress. ST005: populated AC002/AC003 skeletons from RES-005 deltas; registered new AC005 (STD-005, Deltas C1-C2 per DEC007); updated gate dependency notes (ST004-AC002 GATE-003 passed). |
| v0.14.0 | 2026-02-10 | Update | ST004-AC003 GATE-003 passed; ST005-AC004 gate dependency satisfied; RES-006 integration analysis added to Links; ST005 plan updated to v3.0.0 with AC004 fully populated |
| v0.15.0 | 2026-02-11 | Plan Amendment | Registered ST006 to execute Option (c) transition work (Concept hygiene + Concept I&R aggregation) gated on ST005 approvals; added ST006 activities and plan link. |
| v0.16.0 | 2026-02-11 | Plan Amendment | Reopened ST001 for AC008 (STD-004 self-compliance audit). Deferred ST002 to post-ST005 (DEC002); added ST002-AC000 (DEC003); heavy-amended ST002 AC001-AC004 (DEC004); added Phase decision 11 (ST002 sequencing). Evidence: `T102-PH001-SES001`. |
| v0.17.0 | 2026-02-11 | Plan Amendment | Added ST004-AC004 (Commission T102-RES-007 Standards Authoring Methodology Benchmarking); added ST001-AC009 (Research-Informed STD-004 Formalization) with cross-stream dependency on ST004-AC004 GATE-002; AC008 TK005/TK006 superseded. Evidence: `T102-PH001-ST001-AC008-SES002` DEC001–DEC005. |
