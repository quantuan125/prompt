---
artifact_type: 'PLAN'
planning_level: 'PHASE'
initiative_id: 'T104'
initiative_code: 'CWS'
phase: '1'
version: '1.3.2'
date: '2026-02-05'
status: 'draft'
author: 'LLM_Developer'
decision_owner_role: 'Client'
governance_rules: 'prompt/templates/consultant/workspace/workspace_documentation_rules.md'
procedural_guideline: 'prompt/templates/consultant/workspace/guideline_workspace_plan.md'
parent_roadmap: 'prompt/artifacts/tasks/T104/workspace/roadmap/roadmap_T104-CWS.md'
ssot_sps_target: 'prompt/artifacts/tasks/T104/ssot/sps_T104-CWS.md'
ssot_concept_target: 'prompt/artifacts/tasks/T104/ssot/concept_T104-CWS.md'
---

# PLAN: T104 (CWS) — Phase 1: Standards Foundation & Epic Enablement

## I. EXECUTIVE SUMMARY

**Purpose**: Codify initiative-level standards (planning hierarchy, UID convention, gate definition) and populate SPS requirements to create the contract surface that enables subconsultant epic development for T104A, T104E, and future epics.

**Phase 1 Objective**:
1) Populate SPS Section III.B with initiative-level requirements (CON, QG, DEP, ASSUM) per `T102-ADR-005`.
2) Author initiative standards: `T104-STD-001` (Planning Hierarchy), `T104-STD-002` (Timeline UID Convention), `T104-STD-003` (Gate Definition).
3) Refactor planning artifacts migrated from Phase 0 (Streams 4A/5/6.1/7).
4) Enable subconsultants (T104A, T104E) via handoff briefs and epic roadmap placeholders.
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
- `T104-PH001-ST000-SES002-DEC006`: Stream 2 follows `T102-ADR-009` governance standards pattern.
- `T104-PH001-ST000-SES002-DEC007`: Subconsultant briefing uses `handoff_brief_` pattern (per T810 exemplar).

---

## II. CONTEXT MATERIALS & PREREQUISITES

**Phase 0 Plan (predecessor)**: `prompt/artifacts/tasks/T104/workspace/plan/plan_T104-PH000.md`
**Stream Notes (SES-002)**: `prompt/artifacts/tasks/T104/workspace/notes/notes_T104-PH001-ST000.md`
**T102-ADR-009 Reference**: `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_refactor_gdrs_into_std.md`
**T810 Exemplar (handoff brief)**: `prompt/artifacts/tasks/T810/consultant/workspace/communication/handoff_brief_T810A2-SCHEMA.md`

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
| 4 | `T104-PH001-ST004` | Epic Subconsultant Enablement | PARALLEL | ST002 | `planned` | Handoff briefs (T104A, T104E); epic roadmap placeholders |
| 5 | `T104-PH001-ST005` | Template & Rules Alignment | PARALLEL | ST002 | `planned` | workspace_documentation_rules.md + guideline + template updates |
| 6 | `T104-PH001-ST006` | Validation & Handoff | SEQUENTIAL | ST003, ST004, ST005 | `planned` | Validation checklist; Phase 1 exit sign-off |

### Activity Register

| Stream | Activity | Activity ID | Name | Status | Owner | Depends On | Deliverable |
|:--|:--|:--|:--|:--|:--|:--|:--|
| 0 | AC001 | `T104-PH001-ST000-AC001` | Conduct Phase 1 planning consultation (SES-002) and create phase plan | `completed` | LLM_Consultant | PH000 | `plan_T104-PH001.md`; notes SES-002 record |
| 0 | AC002 | `T104-PH001-ST000-AC002` | Update notes file (normalize Stream 0 notes naming + IDs) and create notes guideline | `completed` | LLM_Developer | AC001 | `notes_T104-PH001-ST000.md`; `guideline_workspace_notes.md` |
| 1 | AC000 | `T104-PH001-ST001-AC000` | SPS Structural Migration | `completed` | LLM_Developer | — | `sps_T104-CWS.md` aligned to updated SPS template |
| 1 | AC001 | `T104-PH001-ST001-AC001` | Commission `T104-RES-002` (Requirements Candidate Research) | `completed` | LLM_Consultant | — | `T104-RES-002` brief + report; SPS Research table entry |
| 1 | AC002 | `T104-PH001-ST001-AC002` | Initiative Considerations Consultation (cross-category) | `completed` | LLM_Consultant | AC000, AC001 | SPS III.B.2–11 populated (IID-level items); `notes_T104-PH001-ST001.md` |
| 1 | AC003 | `T104-PH001-ST001-AC003` | Consultation Outcome Validation | `completed` | LLM_Consultant | AC002 | Client-approved SPS III.B baseline; notes validation outcome |
| 2 | AC000 | `T104-PH001-ST002-AC000` | Folder + naming decisions (baseline) | `planned` | LLM_Consultant | ST001-AC000 | SPS (directory/file conventions); prerequisite for STD authoring |
| 2 | AC001 | `T104-PH001-ST002-AC001` | Author T104-STD-001 (Planning Hierarchy + Role Boundaries) | `planned` | LLM_Consultant | AC000 | SPS III.B.7 + Concept spec |
| 2 | AC002 | `T104-PH001-ST002-AC002` | Author T104-STD-002 (Timeline UID Convention) | `planned` | LLM_Consultant | AC000 | SPS III.B.7 + Concept spec |
| 2 | AC003 | `T104-PH001-ST002-AC003` | Author T104-STD-003 (Gate Definition Standard) | `planned` | LLM_Consultant | AC000 | SPS III.B.7 + Concept spec |
| 2 | AC004 | `T104-PH001-ST002-AC004` | Update epic dossier "iv. Governance & Roadmap" subsections | `planned` | LLM_Consultant | AC001, AC003 | SPS epic dossiers |
| 3 | AC001 | `T104-PH001-ST003-AC001` | Convert roadmap_T104A-ROADMAP_phase0.md to plan format | `planned` | LLM_Consultant | ST002 | Converted plan file |
| 3 | AC002 | `T104-PH001-ST003-AC002` | Update roadmap_T104-CWS.md with PH001 scope | `planned` | LLM_Consultant | AC001 | Master roadmap update |
| 3 | AC003 | `T104-PH001-ST003-AC003` | Mark PH000 Streams 5/6/7 as migrated (Phase 0 refactor items) | `planned` | LLM_Developer | — | `plan_T104-PH000.md` update |
| 4 | AC001 | `T104-PH001-ST004-AC001` | Create handoff brief for T104A subconsultant | `planned` | LLM_Consultant | ST002 | handoff_brief_T104A-ROADMAP.md |
| 4 | AC002 | `T104-PH001-ST004-AC002` | Create handoff brief for T104E subconsultant | `planned` | LLM_Consultant | ST002 | handoff_brief_T104E-CHANGELOG.md |
| 4 | AC003 | `T104-PH001-ST004-AC003` | Register epic roadmap placeholders in master roadmap | `planned` | LLM_Consultant | AC001, AC002 | roadmap_T104A, roadmap_T104E placeholders |
| 5 | AC001 | `T104-PH001-ST005-AC001` | Author `template_workspace_plan_phase.md` | `planned` | LLM_Consultant | ST002 | Phase plan template |
| 5 | AC002 | `T104-PH001-ST005-AC002` | Author `template_workspace_plan_stream.md` | `planned` | LLM_Consultant | AC001 | Stream plan template |
| 5 | AC003 | `T104-PH001-ST005-AC003` | Author `template_workspace_plan_activity.md` (skeleton) | `planned` | LLM_Consultant | AC002 | Activity plan skeleton template |
| 5 | AC004 | `T104-PH001-ST005-AC004` | Author `guideline_workspace_plan.md` | `planned` | LLM_Consultant | AC002 | Plan authoring guideline |
| 5 | AC005 | `T104-PH001-ST005-AC005` | Update `workspace_documentation_rules.md` | `planned` | LLM_Consultant | AC004 | Governance rules delta |
| 6 | AC001 | `T104-PH001-ST006-AC001` | Execute validation checklist | `planned` | LLM_Consultant | ST003, ST004, ST005 | Validation outcomes |
| 6 | AC002 | `T104-PH001-ST006-AC002` | Phase 1 exit sign-off | `planned` | Client | AC001 | Phase 1 closure |

---

## IV. LINKS REGISTER

| Link Type | Target | Path |
|:--|:--|:--|
| Plan (this file) | T104 Phase 1 Plan | `prompt/artifacts/tasks/T104/workspace/plan/plan_T104-PH001.md` |
| Notes | Phase 1 Notes Register | `prompt/artifacts/tasks/T104/workspace/notes/notes_T104-PH001.md` |
| Roadmap | T104 Master Roadmap | `prompt/artifacts/tasks/T104/workspace/roadmap/roadmap_T104-CWS.md` |
| Plan | Phase 0 Plan | `prompt/artifacts/tasks/T104/workspace/plan/plan_T104-PH000.md` |
| Plan | Stream 0 Plan (PH001-ST000) | `prompt/artifacts/tasks/T104/workspace/plan/plan_T104-PH001-ST000.md` |
| Plan | Stream 1 Plan (PH001-ST001) | `prompt/artifacts/tasks/T104/workspace/plan/plan_T104-PH001-ST001.md` |
| Plan | Stream 2 Plan (PH001-ST002) | `prompt/artifacts/tasks/T104/workspace/plan/plan_T104-PH001-ST002.md` |
| Plan | Stream 5 Plan (PH001-ST005) | `prompt/artifacts/tasks/T104/workspace/plan/plan_T104-PH001-ST005.md` |
| Notes | Stream ST000 Notes | `prompt/artifacts/tasks/T104/workspace/notes/notes_T104-PH001-ST000.md` |
| Notes | Stream ST001 Notes | `prompt/artifacts/tasks/T104/workspace/notes/notes_T104-PH001-ST001.md` |
| SSOT | T104 SPS | `prompt/artifacts/tasks/T104/ssot/sps_T104-CWS.md` |
| SSOT | T104 Concept | `prompt/artifacts/tasks/T104/ssot/concept_T104-CWS.md` |
| Reference | T102-ADR-009 Proposal | `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_refactor_gdrs_into_std.md` |
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
| v1.0.0 | 2026-01-31 | Initial | Phase 1 plan created with 6 streams and activity registers per SES-002 consultation outcomes |
| v1.1.0 | 2026-02-01 | Update | Added Stream 0 (AC001-AC003); updated ID prefix ST041→ST000-SES### per notes guideline |
| v1.2.0 | 2026-02-02 | Update | Restructured Stream ST001 into AC000–AC003 (migration + RES commissioning + consultation + validation); removed ST000-AC003 per ST001 consultation |
| v1.3.0 | 2026-02-02 | Update | ST002 execution mode changed to PARALLEL, dependency relaxed to ST001-AC000; ST002-AC001 expanded with role boundaries; ST005 activity register replaced (5 activities: 3 templates + guideline + rules update); added ST005 plan link per SES002 consultation |
| v1.3.1 | 2026-02-05 | Complete | Marked ST001 AC002 `completed` (status propagation) and normalized `completed` → `completed` in Phase 1 registers |
| v1.3.2 | 2026-02-05 | Update | Eliminated Stream 0 ID drift: Stream 0 notes renamed to `notes_T104-PH001-ST000.md`, Stream 0 plan aligned to Phase 1 SSOT, and Stream 2 folder/naming decisions renumbered to `T104-PH001-ST002-AC000` |
