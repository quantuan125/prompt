---
artifact_type: 'PLAN'
planning_level: 'PHASE'
initiative_id: 'T104'
initiative_code: 'CWS'
phase: '1'
date: '2026-03-04'
version: '1.8.0'
status: 'draft'
author: 'LLM_Developer'
decision_owner_role: 'Client'
governance_rules: 'prompt/templates/consultant/workspace/workspace_documentation_rules.md'
procedural_guideline: 'prompt/templates/consultant/workspace/guideline_workspace_plan.md'
parent_roadmap: 'prompt/artifacts/tasks/T104/ssot/roadmap_T104-CWS.md'
ssot_sps_target: 'prompt/artifacts/tasks/T104/ssot/sps_T104-CWS.md'
ssot_concept_target: 'prompt/artifacts/tasks/T104/ssot/concept_T104-CWS.md'
---

# PLAN: T104 (CWS) — Phase 1: Standards Foundation & Epic Enablement

## I. EXECUTIVE SUMMARY

**Purpose**: Codify initiative-level standards (planning hierarchy, UID convention, gate definition) and populate SPS requirements to create the contract surface that enables subconsultant epic development for T104A, T104B, T104F, and future epics.

**Phase 1 Objective**:
1) Populate SPS Section III.B with initiative-level requirements (CON, QG, DEP, ASSUM) per `T102-STD-005`.
2) Author initiative standards: `T104-STD-001` (Planning Hierarchy), `T104-STD-002` (Timeline UID Convention), `T104-STD-003` (Gate Definition).
3) Refactor planning artifacts migrated from Phase 0 (Streams 4A/5/6.1/7).
4) Enable subconsultants (T104A, T104B, T104F) via handoff briefs and epic roadmap placeholders.
5) Align templates and workspace documentation rules to the codified standards.

**Entry Criteria**:
- Phase 0 Streams 1-4 complete (confirmed).
- SPS and Concept scaffolds exist.

**Exit Milestone**: **Initiative Standards Baselined + Epic Subconsultants Briefed**

**Locked Decisions (from SES-002)**:
- `T104-PH001-ST000-SES002-DEC001`: Phase 1 plan with 6 streams as defined.
- `T104-PH001-ST000-SES002-DEC002`: SPS III.B.7 "Project Standards" for T104-STD-* bodies; Concept holds normative specs.
- `T104-PH001-ST000-SES002-DEC003`: T104-STD-003 (Gate Definition) approved for Stream 2.
- `T104-PH001-ST000-SES002-DEC004`: T104G (COMMUNICATION) epic registered; deferred beyond Phase 1.
- `T104-PH001-ST000-SES002-DEC005`: Phase 0 Streams 4A/5/6.1/7 migrated to Phase 1.
- `T104-PH001-ST000-SES002-DEC006`: Stream 2 follows `T102-STD-009` governance standards pattern.
- `T104-PH001-ST000-SES002-DEC007`: Subconsultant briefing uses `comm_` naming (supersedes the legacy `handoff_brief_` exemplar naming).
- `T104-PH001-ST002-SES001-DEC008`: T104-PH001-ST007 (Directory Restructuring) introduced as new implementation stream, gated on AC000 Client approval.

---

## II. CONTEXT MATERIALS & PREREQUISITES

**Phase 0 Plan (predecessor)**: `prompt/artifacts/tasks/T104/workspace/PH000/plan_T104-PH000.md`
**Stream Notes (SES-002)**: `prompt/artifacts/tasks/T104/workspace/PH001/ST000/notes_T104-PH001-ST000.md`
**T102-STD-009 Reference**: `prompt/artifacts/tasks/T102/workspace/PH000/proposal/proposal_T102-CWD_refactor_gdrs_into_std.md`
**T810 Exemplar (legacy handoff brief naming)**: `prompt/artifacts/tasks/T810/consultant/workspace/communication/handoff_brief_T810A2-SCHEMA.md`

---

## III. PHASE 1: STANDARDS FOUNDATION & EPIC ENABLEMENT

**Objective**: Build the initiative standards contract and enable subconsultant epic development.

### Stream Register

| Stream | ID | Name | Execution Mode | Depends On | Status | Key Deliverables |
|:--|:--|:--|:--|:--|:--|:--|
| 0 | `T104-PH001-ST000` | Phase Planning & Consultation QA | SEQUENTIAL | PH000 | `completed` | Phase 1 plan file; SES-002 session record; notes guideline |
| 1 | `T104-PH001-ST001` | SPS Baseline (Migration + Consultation) | SEQUENTIAL | PH000 | `completed` | SPS aligned to new template; `T104-RES-002` commissioned; SPS III.B baseline populated + validated |
| 2 | `T104-PH001-ST002` | Initiative Standards Authoring | PARALLEL | ST001-AC000 | `planned` | T104-STD-001 (incl. role boundaries), T104-STD-002, T104-STD-003 + associated ADRs in Concept |
| 3 | `T104-PH001-ST003` | Planning Artifact Refactor | SEQUENTIAL | ST002 | `planned` | Migrate PH000 4A/5/6.1/7 scope; convert T104A roadmap to plan; update master roadmap |
| 4 | `T104-PH001-ST004` | Epic Subconsultant Enablement | PARALLEL | `T104-PH001-ST002-AC001` | `planned` | Communication briefs (comm_) for T104A/T104B/T104F; kickoff & placeholder registrations |
| 5 | `T104-PH001-ST005` | Template & Rules Alignment | PARALLEL | `T104-PH001-ST002-AC001` | `planned` | PLAN/ROADMAP/NOTES template + guideline alignment (working drafts); workspace_documentation_rules.md update |
| 6 | `T104-PH001-ST006` | Validation & Handoff | SEQUENTIAL | ST003, ST004, ST005, ST007 | `planned` | Validation checklist; Phase 1 exit sign-off |
| 7 | `T104-PH001-ST007` | Directory Restructuring (T104 + P + T102) | SEQUENTIAL | `T104-PH001-ST002-AC000` (Client-approved proposal) | `in_progress` | T104, P, T102 directories restructured; `consultant/` absorbed into T102 root |
| 8 | `T104-PH001-ST008` | Vertical Guideline Integration & Documentation Rules Alignment | SEQUENTIAL | `T104-PH001-ST005` | `planned` | Cross-guideline consistency resolution; `workspace_documentation_rules.md` aligned to SPS; supersedes ST005-AC004 |

### Activity Snapshot Index

**Activity Snapshot As-Of**: 2026-03-04

| Stream | Activity | Activity ID | Name | Status (snapshot) | Owner | Source (Stream Plan) |
|:--|:--|:--|:--|:--|:--|:--|
| 0 | AC001 | `T104-PH001-ST000-AC001` | Conduct Phase 1 planning consultation (SES-002) and create phase plan | `completed` | LLM_Consultant | `prompt/artifacts/tasks/T104/workspace/PH001/ST000/plan_T104-PH001-ST000.md` |
| 0 | AC002 | `T104-PH001-ST000-AC002` | Update notes file (normalize Stream 0 notes naming + IDs) and create notes guideline | `completed` | LLM_Developer | `prompt/artifacts/tasks/T104/workspace/PH001/ST000/plan_T104-PH001-ST000.md` |
| 0 | AC003 | `T104-PH001-ST000-AC003` | Plan amendment: align ST002/ST003/ST004/ST005 to support T104A/B/F parallel work | `completed` | LLM_Consultant | `prompt/artifacts/tasks/T104/workspace/PH001/ST000/plan_T104-PH001-ST000.md` |
| 1 | AC000 | `T104-PH001-ST001-AC000` | SPS Structural Migration | `completed` | LLM_Developer | `prompt/artifacts/tasks/T104/workspace/PH001/ST001/plan_T104-PH001-ST001.md` |
| 1 | AC001 | `T104-PH001-ST001-AC001` | Commission `T104-RES-002` (Requirements Candidate Research) | `completed` | LLM_Consultant | `prompt/artifacts/tasks/T104/workspace/PH001/ST001/plan_T104-PH001-ST001.md` |
| 1 | AC002 | `T104-PH001-ST001-AC002` | Initiative Considerations Consultation (cross-category) | `completed` | LLM_Consultant | `prompt/artifacts/tasks/T104/workspace/PH001/ST001/plan_T104-PH001-ST001.md` |
| 1 | AC003 | `T104-PH001-ST001-AC003` | Consultation Outcome Validation | `completed` | LLM_Consultant | `prompt/artifacts/tasks/T104/workspace/PH001/ST001/plan_T104-PH001-ST001.md` |
| 2 | AC000 | `T104-PH001-ST002-AC000` | Folder + naming decisions (baseline) | `planned` | LLM_Consultant | `prompt/artifacts/tasks/T104/workspace/PH001/ST002/plan_T104-PH001-ST002.md` |
| 2 | AC001 | `T104-PH001-ST002-AC001` | Author T104-STD-001 (Planning Hierarchy + Role Boundaries) | `planned` | LLM_Consultant | `prompt/artifacts/tasks/T104/workspace/PH001/ST002/plan_T104-PH001-ST002.md` |
| 2 | AC002 | `T104-PH001-ST002-AC002` | Author T104-STD-002 (Timeline UID Convention) | `planned` | LLM_Consultant | `prompt/artifacts/tasks/T104/workspace/PH001/ST002/plan_T104-PH001-ST002.md` |
| 2 | AC003 | `T104-PH001-ST002-AC003` | Author T104-STD-003 (Gate Definition Standard) | `planned` | LLM_Consultant | `prompt/artifacts/tasks/T104/workspace/PH001/ST002/plan_T104-PH001-ST002.md` |
| 3 | AC001 | `T104-PH001-ST003-AC001` | Convert roadmap_T104A-ROADMAP_phase0.md to plan format | `planned` | LLM_Consultant | `prompt/artifacts/tasks/T104/workspace/PH001/ST003/plan_T104-PH001-ST003.md` |
| 3 | AC002 | `T104-PH001-ST003-AC002` | Update roadmap_T104-CWS.md with PH001 scope | `planned` | LLM_Consultant | `prompt/artifacts/tasks/T104/workspace/PH001/ST003/plan_T104-PH001-ST003.md` |
| 3 | AC003 | `T104-PH001-ST003-AC003` | Mark PH000 Streams 5/6/7 as migrated (Phase 0 refactor items) | `planned` | LLM_Developer | `prompt/artifacts/tasks/T104/workspace/PH001/ST003/plan_T104-PH001-ST003.md` |
| 3 | AC004 | `T104-PH001-ST003-AC004` | Update critical epic dossiers (T104A/T104B/T104F) sections i–v only | `planned` | LLM_Consultant | `prompt/artifacts/tasks/T104/workspace/PH001/ST003/plan_T104-PH001-ST003.md` |
| 4 | AC001 | `T104-PH001-ST004-AC001` | Create communication brief (comm_) for T104A subconsultant | `planned` | LLM_Consultant | `prompt/artifacts/tasks/T104/workspace/PH001/ST004/plan_T104-PH001-ST004.md` |
| 4 | AC002 | `T104-PH001-ST004-AC002` | Create communication brief (comm_) for T104B subconsultant | `planned` | LLM_Consultant | `prompt/artifacts/tasks/T104/workspace/PH001/ST004/plan_T104-PH001-ST004.md` |
| 4 | AC003 | `T104-PH001-ST004-AC003` | Create communication brief (comm_) for T104F subconsultant | `planned` | LLM_Consultant | `prompt/artifacts/tasks/T104/workspace/PH001/ST004/plan_T104-PH001-ST004.md` |
| 4 | AC004 | `T104-PH001-ST004-AC004` | Kickoff & placeholder registrations (critical epics) | `planned` | LLM_Consultant | `prompt/artifacts/tasks/T104/workspace/PH001/ST004/plan_T104-PH001-ST004.md` |
| 5 | AC001 | `T104-PH001-ST005-AC001` | PLAN Templates + Guideline Package | `planned` | LLM_Consultant | `prompt/artifacts/tasks/T104/workspace/PH001/ST005/plan_T104-PH001-ST005.md` |
| 5 | AC002 | `T104-PH001-ST005-AC002` | ROADMAP Template + Guideline Alignment | `planned` | LLM_Consultant | `prompt/artifacts/tasks/T104/workspace/PH001/ST005/plan_T104-PH001-ST005.md` |
| 5 | AC003 | `T104-PH001-ST005-AC003` | NOTES Templates + Guideline Alignment | `planned` | LLM_Consultant | `prompt/artifacts/tasks/T104/workspace/PH001/ST005/plan_T104-PH001-ST005.md` |
| 5 | AC004 | `T104-PH001-ST005-AC004` | Workspace Documentation Rules Rewrite | `planned` | LLM_Consultant | `prompt/artifacts/tasks/T104/workspace/PH001/ST005/plan_T104-PH001-ST005.md` |
| 6 | AC001 | `T104-PH001-ST006-AC001` | Execute validation checklist | `planned` | LLM_Consultant | `prompt/artifacts/tasks/T104/workspace/PH001/ST006/plan_T104-PH001-ST006.md` |
| 6 | AC002 | `T104-PH001-ST006-AC002` | Phase 1 exit sign-off | `planned` | Client | `prompt/artifacts/tasks/T104/workspace/PH001/ST006/plan_T104-PH001-ST006.md` |
| 7 | AC001 | `T104-PH001-ST007-AC001` | Script Development & Migration Execution (T104) | `completed` | LLM_Developer | `prompt/artifacts/tasks/T104/workspace/PH001/ST007/plan_T104-PH001-ST007.md` |
| 7 | AC002 | `T104-PH001-ST007-AC002` | Verification and cross-reference validation | `planned` | LLM_Developer | `prompt/artifacts/tasks/T104/workspace/PH001/ST007/plan_T104-PH001-ST007.md` |
| 7 | AC003 | `T104-PH001-ST007-AC003` | Archive tooling development | `planned` | LLM_Developer | `prompt/artifacts/tasks/T104/workspace/PH001/ST007/plan_T104-PH001-ST007.md` |
| 7 | AC004 | `T104-PH001-ST007-AC004` | Script Enhancement + P Directory Migration | `planned` | LLM_Developer | `prompt/artifacts/tasks/T104/workspace/PH001/ST007/plan_T104-PH001-ST007.md` |
| 7 | AC005 | `T104-PH001-ST007-AC005` | T102 Directory Migration | `planned` | LLM_Developer | `prompt/artifacts/tasks/T104/workspace/PH001/ST007/plan_T104-PH001-ST007.md` |
| 8 | AC001 | `T104-PH001-ST008-AC001` | GDR Ownership Resolution & Gate Semantics Alignment | `planned` | LLM_Consultant | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/plan_T104-PH001-ST008.md` |
| 8 | AC002 | `T104-PH001-ST008-AC002` | Vertical Integration Analysis (Research Commissioning) | `planned` | LLM_Consultant | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/plan_T104-PH001-ST008.md` |
| 8 | AC003 | `T104-PH001-ST008-AC003` | Cross-Guideline Gap Resolution (Development) | `planned` | LLM_Consultant | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/plan_T104-PH001-ST008.md` |
| 8 | AC004 | `T104-PH001-ST008-AC004` | Documentation Rules Consolidation & SPS Alignment | `planned` | LLM_Consultant | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/plan_T104-PH001-ST008.md` |
| 8 | AC005 | `T104-PH001-ST008-AC005` | Validation & Internal Review Gate | `planned` | LLM_Reviewer | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/plan_T104-PH001-ST008.md` |

---

## IV. LINKS REGISTER

| Link Type | Target | Path |
|:--|:--|:--|
| Plan (this file) | T104 Phase 1 Plan | `prompt/artifacts/tasks/T104/workspace/PH001/plan_T104-PH001.md` |
| Notes | Phase 1 Notes Register | `prompt/artifacts/tasks/T104/workspace/PH001/notes_T104-PH001.md` |
| Roadmap | T104 Master Roadmap | `prompt/artifacts/tasks/T104/ssot/roadmap_T104-CWS.md` |
| Plan | Phase 0 Plan | `prompt/artifacts/tasks/T104/workspace/PH000/plan_T104-PH000.md` |
| Plan | Stream 0 Plan (PH001-ST000) | `prompt/artifacts/tasks/T104/workspace/PH001/ST000/plan_T104-PH001-ST000.md` |
| Plan | Stream 1 Plan (PH001-ST001) | `prompt/artifacts/tasks/T104/workspace/PH001/ST001/plan_T104-PH001-ST001.md` |
| Plan | Stream 2 Plan (PH001-ST002) | `prompt/artifacts/tasks/T104/workspace/PH001/ST002/plan_T104-PH001-ST002.md` |
| Plan | Stream 3 Plan (PH001-ST003) | `prompt/artifacts/tasks/T104/workspace/PH001/ST003/plan_T104-PH001-ST003.md` |
| Plan | Stream 4 Plan (PH001-ST004) | `prompt/artifacts/tasks/T104/workspace/PH001/ST004/plan_T104-PH001-ST004.md` |
| Plan | Stream 5 Plan (PH001-ST005) | `prompt/artifacts/tasks/T104/workspace/PH001/ST005/plan_T104-PH001-ST005.md` |
| Plan | Stream 7 Plan (PH001-ST007) | `prompt/artifacts/tasks/T104/workspace/PH001/ST007/plan_T104-PH001-ST007.md` |
| Plan | Stream 8 Plan (PH001-ST008) | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/plan_T104-PH001-ST008.md` |
| Notes | Stream ST000 Notes | `prompt/artifacts/tasks/T104/workspace/PH001/ST000/notes_T104-PH001-ST000.md` |
| Notes | Stream ST001 Notes | `prompt/artifacts/tasks/T104/workspace/PH001/ST001/notes_T104-PH001-ST001.md` |
| SSOT | T104 SPS | `prompt/artifacts/tasks/T104/ssot/sps_T104-CWS.md` |
| SSOT | T104 Concept | `prompt/artifacts/tasks/T104/ssot/concept_T104-CWS.md` |
| Reference | T102-STD-009 Proposal | `prompt/artifacts/tasks/T102/workspace/PH000/proposal/proposal_T102-CWD_refactor_gdrs_into_std.md` |
| Reference | T810 Handoff Brief Exemplar | `prompt/artifacts/tasks/T810/consultant/workspace/communication/handoff_brief_T810A2-SCHEMA.md` |
| Governance Rules | Workspace Rules | `prompt/templates/consultant/workspace/workspace_documentation_rules.md` |
| Procedural Guideline | Plan Authoring Rules | `prompt/templates/consultant/workspace/guideline_workspace_plan.md` |

---

## V. OPEN QUESTIONS REGISTER

| ID | Topic | Question | Owner | Status | Proposed Date | Resolved Date |
|:--|:--|:--|:--|:--|:--|:--|
| OQ-PH1-001 | UID Format Resolution | Resolve pending UID format decisions (S-0007 vs S-PH0-04A, global vs scoped task IDs) as part of T104-STD-002 authoring | LLM_Consultant | Proposed | 2026-01-31 | — |
| OQ-PH1-002 | Phase 0 Closure Formalization | Formalize Phase 0 exit criteria satisfaction and closure record | LLM_Developer | Proposed | 2026-01-31 | — |

---

## VI. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.8.0 | 2026-03-04 | Update | Added ST008 (Vertical Guideline Integration & Documentation Rules Alignment) to Stream Register and Activity Snapshot Index. ST008 supersedes ST005-AC004. 5 activities registered (AC001–AC005). Evidence: consultation session 2026-03-04. |
| v1.0.0 | 2026-01-31 | Initial | Phase 1 plan created with 6 streams and activity registers per SES-002 consultation outcomes |
| v1.1.0 | 2026-02-01 | Update | Added Stream 0 (AC001-AC003); updated ID prefix ST041→ST000-SES### per notes guideline |
| v1.2.0 | 2026-02-02 | Update | Restructured Stream ST001 into AC000–AC003 (migration + RES commissioning + consultation + validation); removed ST000-AC003 per ST001 consultation |
| v1.3.0 | 2026-02-02 | Update | ST002 execution mode changed to PARALLEL, dependency relaxed to ST001-AC000; ST002-AC001 expanded with role boundaries; ST005 activity register replaced (5 activities: 3 templates + guideline + rules update); added ST005 plan link per SES002 consultation |
| v1.3.1 | 2026-02-05 | Complete | Marked ST001 AC002 `completed` (status propagation) and normalized `completed` → `completed` in Phase 1 registers |
| v1.3.2 | 2026-02-05 | Update | Eliminated Stream 0 ID drift: Stream 0 notes renamed to `notes_T104-PH001-ST000.md`, Stream 0 plan aligned to Phase 1 SSOT, and Stream 2 folder/naming decisions renumbered to `T104-PH001-ST002-AC000` |
| v1.4.0 | 2026-02-09 | Update | Plan amendment: migrate dossier i–v updates from ST002→ST003 (critical epics); expand ST005 to include ROADMAP/NOTES alignment; expand ST004 to include T104B/T104F enablement and kickoff; add ST003/ST004 stream plan links |
| v1.5.0 | 2026-02-10 | Update | Added ST007 (Directory Restructuring) gated on ST002-AC000 Client approval; updated ST006 dependencies; recorded ST002 readiness consultation decisions |
| v1.6.0 | 2026-02-11 | Update | Updated ST005 activity register to consolidated 4-activity structure (SES001 plan amendment); links now target `plan_T104-PH001-ST005.md` v2.0.0 |
| v1.6.1 | 2026-02-21 | Update | Converted Phase Plan Activity Register to Activity Snapshot Index (anti-drift per guideline); propagated ST007 references post AC001.4 TK009 evidence commit `2e1731d` |
| v1.7.0 | 2026-02-21 | Update | ST007 scope expanded to T104 + P + T102; status corrected to `in_progress`; Activity Snapshot: AC001 → `completed`, AC003/AC004/AC005 rows added. |
