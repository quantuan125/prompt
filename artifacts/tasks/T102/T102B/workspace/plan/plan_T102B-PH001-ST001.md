---
artifact_type: 'PLAN'
planning_level: 'STREAM'
initiative_id: 'T102'
epic_id: 'T102B'
epic_code: 'REQUEST'
phase: '1'
stream: '1'
stream_id: 'T102B-PH001-ST001'
feature_id: 'T102B1'
feature_code: 'RST'
version: '2.4.1'
date: '2026-02-10'
status: 'in_progress'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
governance_rules: 'prompt/templates/consultant/workspace/workspace_documentation_rules.md'
procedural_guideline: 'prompt/templates/consultant/workspace/guideline_workspace_roadmap.md'
parent_plan: 'prompt/artifacts/tasks/T102/T102B/workspace/plan/plan_T102B-PH001.md'
---

# PLAN: T102B (REQUEST) — Phase 1 / Stream `T102B-PH001-ST001`: RST Development (T102B1)

## I. EXECUTIVE SUMMARY

**Purpose**: Develop the normative Request Structural Template (RST) for feature T102B1, implementing T102B-RES-001 recommendations (P1-P4 proposals) and validating through self-hosting strategy.

**Stream Objective**: Produce an approved RST template validated via self-application to `request_T102B1-RST.md`, demonstrating template utility and completeness.

**Non-goal**: This stream does not develop RLITE (ST002), RSPG (ST003), or MANIFEST (ST004). Those are handled in subsequent streams.

**Locked constraint (from T102B-RES-001)**:
- Request artifact is **feature-level specification** (not story-level)
- Story-level FRs deferred to Design/Concept stage per P2 proposal
- Section classification (Mandatory/Optional/Deferred) required per P4 proposal

---

## II. STREAM DECISION SUMMARY

Decisions resolved during stream execution.

1) **Activity consolidation** (v2.0.0): AC002–AC005 (industry mapping, classification, FR/IG, Story Index) consolidated into single AC002 ("RST Specification Refinement") per `T102B-PH001-ST001-AC001-DEC008`. Design decisions are requirements refinements within the Request specification surface, not separate Design artifacts.
2) **Canonical Request section list** (2026-02-06): Treat `T102B-STD-002` Full Request Section List as canonical for RST; `request_T102B1-RST.md` v0.2 MUST be traceable to STD-002.
3) **Section classification schema** (2026-02-06): Ternary taxonomy (Mandatory/Optional/Deferred) per `T102B-STD-002-CLAUSE-001`. “Conditional” is NOT a classification type; applicability SHALL be expressed as validation rule(s).
4) **Section J redesign** (2026-02-06): Option A — Story Index only (navigation). Story Index is REQUIRED if `story_count > 1`. No story-level FR bodies/ACs in Request per `T102B-STD-003`.
5) **FR/IG merge pattern** (2026-02-06): FR with inline guidance (“requirements-with-guidance”) per `T102B-IG-002`.
6) **Industry standards mapping** (2026-02-06): Conceptual per-section mapping to ISO 29148, BABOK v3, SAFe documented in `proposal_T102B1-RST_non_normative.md` §IV. No clause-by-clause compliance matrix in Phase 1.
7) **Section G redesign** (2026-02-08): "Governance Decisions" → "Governance Standards" using STD index schema per `T102-STD-009-CLAUSE-004A`. GDR pattern deprecated at feature level.
8) **Section H removal** (2026-02-08): "Issues & Risks" removed from Request template. Feature-level items promoted to epic scope. Hosting architecture deferred to `T102-RES-004`.
9) **Feature Guidance & Notes section** (2026-02-08): New `### H. Feature Guidance & Notes [O]` inserted in Request. Hosts non-normative IID tokens (IG, INT, NOTE) under `####` subheadings.
10) **Acceptance Criteria relocation** (2026-02-08): Moved from `## IV.` major section to `### K.` under Core Content. STD-002 amended per D8/D12/D13.
11) **Canonical section list A-K** (2026-02-08): Full Request Core Content sections expanded from A-J to A-K. G renamed, H replaced, K added from former `## IV.`.
12) **Issues & Risks research** (2026-02-08): Hosting architecture elevated to `T102-RES-004` at initiative scope. New `T102-PH001-ST004` research stream commissioned per `T102-STD-006`.
13) **Unified RID schema** (2026-02-08): Section F tables standardized to `| ID | Title | Description | Reference | Verification | Status | Note |`. ASSUM retains lifecycle schema per `T102-STD-005-CLAUSE-005A` with added Reference column.

---

## III. STREAM OUTLINE

**Stream ID**: `T102B-PH001-ST001`
**Feature**: T102B1 (RST) — Request Structural Template
**Objective**: Develop the normative Request Structural Template per T102B-RES-001 recommendations, validated via self-hosting (Option C hybrid approach).
**Execution Mode**: GATED
**Depends On**: `T102B-PH001-ST000`
**Owner**: LLM_Consultant (Decision Owner: Client)

**Entry Criteria**: ST000 complete (plan files approved)
**Exit Milestone**: RST template approved; `request_T102B1-RST.md` retrofitted and validated

**Context (files this stream depends on)**:
- `prompt/artifacts/tasks/T102/T102B/workspace/plan/plan_T102B-PH001.md`
- `prompt/artifacts/tasks/T102/T102B/research/report/report_T102B-RES-001_request-artifact-analysis.md`
- `prompt/artifacts/tasks/T102/T102B/research/report/report_T102B-RES-002_epic-foundation-assessment.md`
- `prompt/artifacts/tasks/T102/consultant/request/request_T102A-SPSST.md` (guidance-only per DEC004)
- `prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md` (Initiative Governance & Problem Statement)
- `prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md` (Initiative Architecture & ADR Compendium)

### Activity Register

| Activity | Activity ID | Name | Status | Owner | Depends On | Deliverable |
|:--|:--|:--|:--|:--|:--|:--|
| AC001 | `T102B-PH001-ST001-AC001` | RST requirements analysis & initial request | `completed` | LLM_Consultant | ST000 | `request_T102B1-RST.md` (v0.1 lightweight) |
| AC002 | `T102B-PH001-ST001-AC002` | RST specification refinement | `completed` | LLM_Consultant | AC001 | `request_T102B1-RST.md` (v0.2.1 — decisions resolved) |
| AC002.1 | `T102B-PH001-ST001-AC002.1` | RST Specification Remediation | `completed` | LLM_Consultant | AC002 | `request_T102B1-RST.md` v0.3.0 + `T102B-STD-002` v2.0 + plan amendments + `plan_T102-PH001-ST004.md` |
| AC002.2 | `T102B-PH001-ST001-AC002.2` | RST Post-Amendment Conformance Gate | `planned` | LLM_Consultant | AC002.1 + `T102-PH001-ST005` | Conformance note + acceptance-level gate evidence |
| AC003 | `T102B-PH001-ST001-AC003` | RST template formalization | `planned` | LLM_Consultant | AC002.1 | `template_request_structural.md` |
| AC004 | `T102B-PH001-ST001-AC004` | RST self-validation & retrofit | `planned` | LLM_Consultant | AC003 | `request_T102B1-RST.md` (v1.0 full) |
| AC005 | `T102B-PH001-ST001-AC005` | Client approval gate | `planned` | Client | AC004 + AC002.2 | Approval statement |

---

## IV. ACTIVITIES

### Activity AC001: RST Requirements Analysis & Initial Request

**Activity ID**: `T102B-PH001-ST001-AC001`
**Status**: `completed`

**Purpose**: Analyze T102B-RES-001 & T102B-RES-002 findings, existing request exemplar, and Phase 0 E-RIDs to produce an initial lightweight `request_T102B1-RST.md` using an industry-standard SRS/BRD hybrid structure, establishing the baseline for iterative refinement.

**Deliverable**: `prompt/artifacts/tasks/T102/T102B/request/request_T102B1-RST.md` (v0.1 — lightweight, SRS/BRD hybrid)

**Scope**:
- In scope: Problem definition, scope boundaries, business objectives, stakeholders, inherited considerations, initial functional requirements for RST feature
- Out of scope: Template formalization (AC003), detailed design decisions (AC002)

**Inputs Required**:
- `report_T102B-RES-001_request-artifact-analysis.md`
- `report_T102B-RES-002_epic-foundation-assessment.md`
- `request_T102A-SPSST.md` (guidance-only per DEC004)
- T102B Phase 0 E-RIDs (CON, QG, DEP, IF, IG)
- T102B-STD-001 through STD-004

**Task Register**:

| Task ID | Description | Status | Action |
|:--|:--|:--|:--|
| T102B-PH001-ST001-AC001-TK001 | Extract RST problem statement from T102B-RES-001 (W1-W7 weaknesses as root cause) | `completed` | — |
| T102B-PH001-ST001-AC001-TK002 | Define RST scope boundaries (In Scope: template sections, classification, handoff; Out of Scope: RLITE, RSPG, MANIFEST) | `completed` | — |
| T102B-PH001-ST001-AC001-TK003 | Define RST business objectives aligned with T102B-QG-001 through QG-006 | `completed` | — |
| T102B-PH001-ST001-AC001-TK004 | Populate stakeholder table (Template Author, Request Author, Concept Author, Client) | `completed` | — |
| T102B-PH001-ST001-AC001-TK005 | Populate inherited considerations from T102B E-RIDs | `completed` | — |
| T102B-PH001-ST001-AC001-TK006 | Draft initial feature requirements (Section F) addressing P1-P4 proposals | `completed` | — |
| T102B-PH001-ST001-AC001-TK007 | Create `request_T102B1-RST.md` file using industry-standard SRS/BRD hybrid structure (not T102A-SPSST exemplar per DEC004) | `completed` | — |

**Success Criteria Checklist**:
- [x] `request_T102B1-RST.md` exists at correct path (`prompt/artifacts/tasks/T102/T102B/request/`)
- [x] Problem statement traces to T102B-RES-001 W1-W7 weaknesses
- [x] Scope explicitly includes P1-P4 proposal implementation
- [x] Business objectives map to T102B quality goals
- [x] Inherited considerations reference T102B E-RIDs by ID
- [x] Initial feature requirements address structural changes

---

### Activity AC002: RST Specification Refinement

**Activity ID**: `T102B-PH001-ST001-AC002`
**Status**: `completed`

**Purpose**: Refine the RST specification (within `request_T102B1-RST.md`) starting from the canonical Full Request section list defined by `T102B-STD-002`, and resolve the remaining specification decisions needed to produce `request_T102B1-RST.md` v0.2. This consolidated activity covers industry standards mapping, section classification design, FR/IG consolidation design, and Story Index design — previously planned as separate AC002–AC005 activities, consolidated per `T102B-PH001-ST001-AC001-DEC008`.

**Deliverable**: `prompt/artifacts/tasks/T102/T102B/request/request_T102B1-RST.md` (v0.2 — design decisions resolved)

**Scope**:
- In scope:
  - Industry standards mapping (ISO 29148, BABOK v3, SAFe alignment per RST section)
  - Section classification taxonomy (M/O/D) and per-section assignments per `T102B-STD-002`
  - Applicability rules that replace “Conditional” classification (e.g., Story Index required-if trigger)
  - FR/IG consolidation pattern selection and documentation (FR with inline guidance)
  - Section J disposition (Story Index navigation-only) and Story Index schema per `T102B-STD-003`
  - Canonical section list decision: STD-002 is authoritative; Request v0.2 MUST be traceable to it
  - Resolution of OQ001 (v0.1 structure sufficiency) and OQ002 (Story Index scope)
- Out of scope: Template file authoring (AC003), RLITE template (ST002), formal clause-by-clause compliance mapping

**Inputs Required**:
- AC001 deliverable (`request_T102B1-RST.md` v0.1)
- T102B-RES-001 (Section 5: Industry Standards Benchmark; W1-W7 weaknesses; P1-P4 proposals)
- T102B-RES-002 (E-RID candidates; governance gaps)
- `request_T102A-SPSST.md` (guidance-only — current Section F/J structure for analysis)
- T102B-STD-002 (Workflow Typology Standard)
- T102B-STD-004 (Section Classification Policy)
- `prompt/artifacts/tasks/T102/T102B/standards/T102B-STD-001_request-architecture-standard.md`
- `prompt/artifacts/tasks/T102/T102B/standards/T102B-STD-002_section-classification-standard.md`
- `prompt/artifacts/tasks/T102/T102B/standards/T102B-STD-003_story-fr-deferral-standard.md`
- `prompt/artifacts/tasks/T102/T102B/standards/T102B-STD-004_request-lite-specification.md`

**Execution Mode**: Consultation session (Socratic dialogue to resolve design decisions with Client)

**Task Register**:

| Task ID | Description | Status | Action |
|:--|:--|:--|:--|
| T102B-PH001-ST001-AC002-TK001 | Confirm canonical Full Request section list per `T102B-STD-002-CLAUSE-002` and define how RST expresses it (headings + traceability requirement) | `completed` | Request TOC (v0.2.1) mirrors STD-002-CLAUSE-002; traceability statement in Executive Summary |
| T102B-PH001-ST001-AC002-TK002 | Reconcile STD-002 internal inconsistency: replace "Conditional" with Optional + explicit applicability validation rule(s) | `completed` | STD-002 Alternatives rejects "Conditional"; Request encodes Story Index applicability rule (required-if `story_count > 1`) |
| T102B-PH001-ST001-AC002-TK003 | Define section classification taxonomy (M/O/D) and validation rules per `T102B-STD-002-CLAUSE-001` and `CLAUSE-004` | `completed` | Request TOC uses `[M]`/`[O]` markers; classification legend documented; STD-002-CLAUSE-001 defines categories |
| T102B-PH001-ST001-AC002-TK004 | Define Story Index disposition and rules per `T102B-STD-003`: navigation-only; required-if `story_count > 1`; schema includes Design Link placeholder | `completed` | Request Section J: navigation-only, `story_count = 4`, Design Link column present, deferral to T102D stated |
| T102B-PH001-ST001-AC002-TK005 | Define FR/IG consolidation pattern as FR with inline guidance per `T102B-IG-002` (normative vs guidance formatting rules) | `completed` | Requirements-with-guidance pattern documented in `proposal_T102B1-RST_non_normative.md` §III; no separate IG section in Request |
| T102B-PH001-ST001-AC002-TK006 | Review T102B-RES-001 industry standards analysis and existing v0.1 standard references | `completed` | Proposal §IV references RES-001 topics as evidence pointers per section |
| T102B-PH001-ST001-AC002-TK007 | Map STD-002 canonical sections to industry standard references (ISO 29148, BABOK v3, SAFe) at a conceptual level (no compliance matrix) | `completed` | Full mapping table in `proposal_T102B1-RST_non_normative.md` §IV covering A–J plus AC/Gate |
| T102B-PH001-ST001-AC002-TK008 | Define RLITE derivation feasibility check: confirm Mandatory subset aligns to `T102B-STD-004-CLAUSE-002` and can remain <200 lines per `CLAUSE-001` | `completed` | RLITE feasibility documented in `proposal_T102B1-RST_non_normative.md` §V; `[M]` markers enable derivation |
| T102B-PH001-ST001-AC002-TK009 | Update `request_T102B1-RST.md` with resolved AC002 decisions; restructure/annotate to be traceable to STD-002; version → v0.2 | `completed` | Request updated to v0.2.1; Amendment Log documents v0.2 and v0.2.1 changes; non-normative content separated to proposal |

**Success Criteria Checklist**:
- [x] STD-002 Full Request section list is treated as canonical (RST structure is traceable to STD-002)
- [x] Classification taxonomy is explicit and limited to M/O/D per STD-002 (no "C" type)
- [x] "Conditional" applicability is expressed as validation rule(s) (e.g., Story Index required-if) rather than taxonomy expansion
- [x] Story Index schema and deferral boundary documented per STD-003; trigger is `story_count > 1`
- [x] FR/IG consolidation pattern documented as FR with inline guidance per IG-002 (eliminates W1)
- [x] RLITE derivation feasibility check defined per STD-004 (<200 lines; mandatory subset)
- [x] Industry alignment documented per canonical section (ISO 29148, BABOK v3, SAFe)
- [x] `request_T102B1-RST.md` updated to v0.2 with all decisions reflected

---

### Activity AC002.1: RST Specification Remediation

**Activity ID**: `T102B-PH001-ST001-AC002.1`

**Purpose**: Apply structural corrections identified during AC002 client re-review (Session 2, 2026-02-08). Amend the governing STD-002 specification, restructure the Request artifact, register the T102-RES-004 research stream, and update downstream activity task registers. The accepted `T102-RES-004` integration analysis (2026-02-09) is treated as supporting evidence for the planned Section H disposition and cross-scope promotion steps.

**Deliverables**:
- `prompt/artifacts/tasks/T102/T102B/standards/T102B-STD-002_section-classification-standard.md` v2.0 (A-K section list + major section restructure + Changelog)
- `prompt/artifacts/tasks/T102/T102B/request/request_T102B1-RST.md` v0.3.0 (structural corrections)
- `prompt/artifacts/tasks/T102/consultant/workspace/plan/plan_T102-PH001.md` v0.7.0 (ST004 registration)
- `prompt/artifacts/tasks/T102/consultant/workspace/plan/plan_T102-PH001-ST004.md` (new research stream plan)

**Scope**:
- In scope: STD-002 amendment, Request section restructuring (G/H/K/F tables/TOC/Gate/Changelog), initiative plan ST004 registration, ST004 stream plan creation, SPS Issues/Risks promotion, AC003/AC004 task register updates
- Out of scope: AC002.1 does NOT execute AC004-deferred items (marker removal, Problem Statement rewrite, INT population, T102-RES-004 absorption), does not draft/modify `T102-STD-007` clause text (initiative-level downstream work), and does not perform post-ST005 conformance validation (handled in AC002.2).

**Inputs Required**:
- AC002 deliverable (`request_T102B1-RST.md` v0.2.1)
- Locked decisions D1-D13 from Session 2 consultation
- `T102-RES-004` integration analysis: `prompt/artifacts/tasks/T102/consultant/workspace/analysis/analysis_T102-RES-004_issues-risks-architecture.md` (accepted evidence, 2026-02-09)
- `T102-STD-009` (STD index schema reference)
- `T102-STD-005` (ID spec, NOTE structure, IID tokens)
- `T102-STD-006` (research commissioning workflow)
- Raw transcript: `prompt/artifacts/tasks/T102/T102B/raw/PH001/ST001/raw_T102B-PH001-ST001-AC002_2026-02-07_p2.txt`

**Execution Mode**: Development-mode (LLM_Developer applies corrections per implementation plan)

**Task Register**:

| Task ID | Description | Status | Action |
|:--|:--|:--|:--|
| TK001 | Amend `T102B-STD-002-CLAUSE-002`: Replace A-J section list with A-K per D12. G→"Governance Standards" (STD index, STD-009 ref). Remove H "Issues & Risks". Insert new H "Feature Guidance & Notes" (IID tokens: IG/INT/NOTE under `####`). I→"Research" (renamed from "Research & Notes"). Add K "Acceptance Criteria" (moved from `## IV.`). | `completed` | Updated `T102B-STD-002-CLAUSE-002` to A-K with revised G/H/I/K definitions. |
| TK002 | Amend `T102B-STD-002-CLAUSE-005`: Remove `## IV. Acceptance Criteria` from Full Request Major Sections table. Renumber: Approval Gate→IV (was V), Appendix→V (was VI). Add `## VI. Changelog` as Mandatory. Update Core Content note to reference A-K (was A-J). | `completed` | Full Request major sections updated to I–VI with mandatory changelog and explicit A-K core-content note. |
| TK003 | Add `## Changelog` section to `T102B-STD-002` with version history (v1.0.0 initial, v2.0.0 AC002.1 amendment) | `completed` | Added `## Changelog` section with `v1.0.0` and `v2.0.0` entries. |
| TK004 | Update `request_T102B1-RST.md` Section G: Replace "Governance Decisions" heading + GDR table with "Governance Standards" heading + STD index schema per `T102-STD-009-CLAUSE-004A` | `completed` | Section G replaced with Governance Standards section using STD index schema columns. |
| TK005 | Update `request_T102B1-RST.md`: Remove entire Section H "Issues & Risks" (heading, comment, Issues table, Risks table) | `completed` | Legacy feature-scoped Issues/Risks section removed from Request; replacement Section H added via TK006. |
| TK006 | Update `request_T102B1-RST.md`: Insert new `### H. Feature Guidance & Notes [O]` with `#### Implementation Guidance (IG)`, `#### Integration Guidance (INT)`, `#### Notes` subheadings. Place `T102B1-NOTE-001` in Notes subsection. | `completed` | New Section H inserted with IG/INT/Notes subheadings and `T102B1-NOTE-001` evidence note. |
| TK007 | Update `request_T102B1-RST.md` Section F: Standardize all RID tables to unified schema `| ID | Title | Description | Reference | Verification | Status | Note |`. ASSUM keeps CLAUSE-005A lifecycle schema with added Reference column. Migrate existing content to new columns. | `completed` | Section F tables migrated to unified RID schema; Assumptions table uses lifecycle schema plus Reference column. |
| TK008 | Update `request_T102B1-RST.md`: Remove free-form proposal pointer from Research section (moved to `T102B1-NOTE-001` in TK006). Rename `### I. Research & Notes` → `### I. Research`. | `completed` | Section I renamed to Research; free-form proposal pointer removed and captured in `T102B1-NOTE-001`. |
| TK009 | Update `request_T102B1-RST.md`: Remove `## IV. ACCEPTANCE CRITERIA` major section. Insert content as `### K. Acceptance Criteria [M]` at end of `## III. CORE CONTENT`. Update `T102B1-AC-002` to reference A-K. | `completed` | Acceptance Criteria moved under Core Content as Section K; `T102B1-AC-002` updated to A-K wording. |
| TK010 | Update `request_T102B1-RST.md`: Renumber `## V. APPROVAL GATE` → `## IV.`, `## VI. APPENDIX` → `## V.`. Add `## VI. CHANGELOG` with version history migrated from `### A. Amendment Log`. Clear Amendment Log content. Update Gate Checklist (remove STD-007 check, add STD-009 + Feature Guidance checks). Update Appendix References table. | `completed` | Major sections renumbered to IV/V/VI; changelog migrated; amendment log cleared; gate checklist and references table aligned to new structure. |
| TK011 | Update `request_T102B1-RST.md`: Update TOC to reflect A-K sections and renumbered major sections. Bump YAML version → v0.3.0, date → 2026-02-08. | `completed` | TOC updated to A-K + renumbered major sections; metadata updated to `version: 0.3.0` and `date: 2026-02-10`. |
| TK012 | Register `T102-PH001-ST004` (Initiative Research Commissioning) in `plan_T102-PH001.md`: Add to Stream Register (PARALLEL, `planned`), add activities to Phase-level Activity Register, add to Links Register, bump version, add changelog entry. | `completed` | Completed in `prompt/artifacts/tasks/T102/consultant/workspace/plan/plan_T102-PH001.md` (ST004 registered; date 2026-02-09) |
| TK013 | Create `plan_T102-PH001-ST004.md` stream plan file. Structure: YAML header, Executive Summary, Activity Register, Activity detail blocks, Links Register, Changelog. | `completed` | Completed in `prompt/artifacts/tasks/T102/consultant/workspace/plan/plan_T102-PH001-ST004.md` (date 2026-02-09) |
| TK014 | Promote `T102B1-ISSUE-001`, `T102B1-ISSUE-002`, `T102B1-RISK-001` to epic scope in SPS dossier (`sps_T102-CONSULTANT.md` T102B section). Verify current max ISSUE/RISK IDs before assigning sequential numbers. Add supersession notes referencing originating feature-level IDs. | `completed` | Added `T102B-ISSUE-009`, `T102B-ISSUE-010`, and `T102B-RISK-006` with supersession notes referencing the originating feature-level IDs. |
| TK015 | Update AC003 task register in this plan: Revise TK008 description (G→"Governance Standards" per STD-009). Change TK009 description (H→"Feature Guidance & Notes" with IG/INT/NOTE `####` instructions). Add TK017 ("Author Section K Acceptance Criteria template"). Update TK012 to reference A-K. Update TK014 to validate A-K completeness. | `completed` | AC003 register updated for G/H/K and A-K completeness language (including TK017 and revised section naming). |
| TK016 | Update AC004 task register in this plan: Add TK015 (`[M]`/`[O]` marker removal from request headings), TK016 (Problem Statement table→narrative), TK017 (INT items population in Section H), TK018 (T102-RES-004 report absorption; dependency resolved 2026-02-09). | `completed` | AC004 register includes TK015–TK018 deferred/remediation follow-up tasks. |

**Success Criteria Checklist**:
- [x] STD-002 amended to v2.0 with A-K canonical section list and updated major sections
- [x] STD-002 has `## Changelog` section
- [x] Request v0.3.0 reflects all structural corrections (G renamed, H removed/replaced, F standardized, K added, Changelog added, TOC/Gate updated)
- [x] T102-PH001-ST004 registered in initiative plan with stream plan file created
- [x] Promoted Issues/Risks recorded in SPS dossier with supersession notes
- [x] AC003/AC004 task registers updated to reflect amended section structure

---

### Activity AC002.2: RST Post-Amendment Conformance Gate

**Activity ID**: `T102B-PH001-ST001-AC002.2`

**Purpose**: Provide a hard-gated conformance pass that executes **after** `T102-PH001-ST005` clause amendments are approved, ensuring T102B RST artifacts remain aligned to the amended initiative-level standards (notably `T102-STD-003`, `T102-STD-006`, and `T102-STD-005` INT constraints). This activity exists because AC002.1 remediation was completed prior to final ST005 drafting, and therefore requires an explicit post-amendment verification checkpoint.

**Deliverables**:
- `prompt/artifacts/tasks/T102/T102B/workspace/notes/PH001/ST001/notes_T102B-PH001-ST001-AC002.2.md` (conformance note + evidence)

**Scope**:
- In scope: Validate that template/retrofit guidance and affected Request surfaces are compatible with amended standards; record evidence; issue narrowly scoped follow-up deltas for AC003/AC004 (or downstream remediation) if needed.
- Out of scope: Drafting the amended standards (ST005 scope) and broad SSOT rollout into SPS/Concept (initiative-level downstream work).

**Hard gate dependency** (acceptance-level): This activity MUST NOT execute until the relevant ST005 activities are approved (per-AC GATE-001), at minimum:
- `T102-PH001-ST005-AC002` (amend `T102-STD-003`)
- `T102-PH001-ST005-AC003` (amend `T102-STD-006`)
- `T102-PH001-ST005-AC005` (amend `T102-STD-005`, as applicable)

**Inputs Required** (analysis-first evidence):
- `analysis_T102-RES-005_cross-scope-coordination-architecture.md` (accepted evidence, 2026-02-10)
- `analysis_T102-RES-006_integration-impact.md` (accepted evidence, 2026-02-10)
- Amended standards outputs from `T102-PH001-ST005` (final versions approved via per-AC GATE-001)
- Current T102B artifacts: `T102B-STD-002`, `request_T102B1-RST.md`, and the AC003 template artifact (once created)

**Task Register**:

| Task ID | Description | Status | Action |
|:--|:--|:--|:--|
| TK001 | Record T102-PH001-ST005 amendment versions used for validation (STD-003, STD-006, STD-005) and gate evidence (approval dates) | `planned` | — |
| TK002 | Validate/adjust Section E expectations against amended `T102-STD-003` (exact schema + “minimum viable embedded coordination” rule) | `planned` | — |
| TK003 | Validate/adjust research indexing expectations against amended `T102-STD-006` (filename discipline + source pointers + link integrity protocol) | `planned` | — |
| TK004 | Validate INT usage constraints relevant to Section H “Feature Guidance & Notes” against amended `T102-STD-005` (promotion loop + anti-pattern boundaries) | `planned` | — |
| TK005 | Record conformance evidence and any follow-up remediation items (execute vs defer) | `planned` | — |

**Success Criteria Checklist**:
- [ ] Conformance note recorded with ST005 versions + evidence
- [ ] Any required follow-up deltas identified and dispositioned (execute vs defer)

---

### Activity AC003: RST Template Formalization

**Activity ID**: `T102B-PH001-ST001-AC003`

**Purpose**: Author the normative Request Structural Template based on approved specifications from AC001-AC002.

**Deliverable**: `prompt/templates/request/request_structural_template.md`

**Scope**:
- In scope: Template structure, instructional comments, section classification markers, industry standard references
- Out of scope: RLITE template (ST002), procedural guideline (ST003)

**Inputs Required**:
- AC001 deliverable (`request_T102B1-RST.md` v0.1)
- AC002.1 deliverable (`request_T102B1-RST.md` v0.3.0 with structural remediation decisions)
- AC002 non-normative proposal (`prompt/artifacts/tasks/T102/T102B/workspace/proposal/T102B1/proposal_T102B1-RST_non_normative.md` — industry alignment mapping §IV, requirements-with-guidance pattern §III, RLITE feasibility §V)

**Execution Mode**: Hybrid — development-mode (LLM_Consultant drafts full template) → consultation review (Client reviews as single deliverable)

**Task Register**:

| Task ID | Description | Status | Action |
|:--|:--|:--|:--|
| T102B-PH001-ST001-AC003-TK001 | Create template YAML header schema | `planned` | — |
| T102B-PH001-ST001-AC003-TK002 | Author Section A (Problem Definition) with instructions | `planned` | — |
| T102B-PH001-ST001-AC003-TK003 | Author Section B (Scope) with instructions | `planned` | — |
| T102B-PH001-ST001-AC003-TK004 | Author Section C (Business Objectives) with instructions | `planned` | — |
| T102B-PH001-ST001-AC003-TK005 | Author Section D (Stakeholders) with instructions | `planned` | — |
| T102B-PH001-ST001-AC003-TK006 | Author Section E (Inherited Considerations) with instructions | `planned` | — |
| T102B-PH001-ST001-AC003-TK007 | Author Section F (Feature Requirements) using approved consolidated pattern | `planned` | — |
| T102B-PH001-ST001-AC003-TK008 | Author Section G (Governance Standards) per T102-STD-009 STD index schema with instructions | `planned` | — |
| T102B-PH001-ST001-AC003-TK009 | Author Section H (Feature Guidance & Notes) with IG/INT/NOTE #### subheading instructions | `planned` | — |
| T102B-PH001-ST001-AC003-TK010 | Author Section I (Research) with instructions | `planned` | — |
| T102B-PH001-ST001-AC003-TK011 | Author Section J per approved disposition (Story Index or removal) | `planned` | — |
| T102B-PH001-ST001-AC003-TK012 | Add section classification markers (M/O/D) per section (A-K) | `planned` | — |
| T102B-PH001-ST001-AC003-TK013 | Add industry standard references per section | `planned` | — |
| T102B-PH001-ST001-AC003-TK014 | Validate template structure completeness (A-K) | `planned` | — |
| T102B-PH001-ST001-AC003-TK015 | Correct AC003 notes file title from "Section Classification Design" to "RST Template Formalization" and populate session entries | `planned` | — |
| T102B-PH001-ST001-AC003-TK016 | Encode OQ-004 resolution in Section J template instructions: Design Link = TBD placeholder, resolved when T102D initiates | `planned` | — |
| T102B-PH001-ST001-AC003-TK017 | Author Section K (Acceptance Criteria) template with instructions (moved from former ## IV.) | `planned` | — |

**Success Criteria Checklist**:
- [ ] Template file exists at `prompt/templates/request/request_structural_template.md`
- [ ] YAML header schema defined with required keys
- [ ] All sections have instructional comments
- [ ] Section classification markers present (M/O/D)
- [ ] Industry standard references present per section
- [ ] FR/IG consolidation pattern implemented per AC002 decision
- [ ] Section J implements approved pattern per AC002 decision

---

### Activity AC004: RST Self-Validation & Retrofit

**Activity ID**: `T102B-PH001-ST001-AC004`

**Purpose**: Validate RST template by retrofitting `request_T102B1-RST.md` from remediated (v0.3.0) to full structure (v1.0), demonstrating template utility and completeness.

**Deliverable**: `prompt/artifacts/tasks/T102/T102B/request/request_T102B1-RST.md` (v1.0 — full structure)

**Scope**:
- In scope: Retrofit request to new template structure, validate all sections, document gaps/issues
- Out of scope: Other request artifacts

**Inputs Required**:
- AC002.1 deliverable (v0.3.0 request with structural remediation decisions)
- AC003 deliverable (RST template)

**Execution Mode**: Hybrid — development-mode (LLM_Consultant drafts) → consultation review (Client reviews)

**Task Register**:

| Task ID | Description | Status | Action |
|:--|:--|:--|:--|
| T102B-PH001-ST001-AC004-TK001 | Map v0.3.0 content to new template sections | `planned` | — |
| T102B-PH001-ST001-AC004-TK002 | Retrofit Section A (Problem Definition) | `planned` | — |
| T102B-PH001-ST001-AC004-TK003 | Retrofit Section B (Scope) | `planned` | — |
| T102B-PH001-ST001-AC004-TK004 | Retrofit Section C (Business Objectives) | `planned` | — |
| T102B-PH001-ST001-AC004-TK005 | Retrofit Section D (Stakeholders) | `planned` | — |
| T102B-PH001-ST001-AC004-TK006 | Retrofit Section E (Inherited Considerations) | `planned` | — |
| T102B-PH001-ST001-AC004-TK007 | Retrofit Section F (Feature Requirements) using consolidated pattern | `planned` | — |
| T102B-PH001-ST001-AC004-TK008 | Retrofit Section G (Governance Standards) | `planned` | — |
| T102B-PH001-ST001-AC004-TK009 | Retrofit Section H (Feature Guidance & Notes) | `planned` | — |
| T102B-PH001-ST001-AC004-TK010 | Retrofit Section I (Research) | `planned` | — |
| T102B-PH001-ST001-AC004-TK011 | Retrofit Section J per approved disposition | `planned` | — |
| T102B-PH001-ST001-AC004-TK012 | Validate all Mandatory sections complete | `planned` | — |
| T102B-PH001-ST001-AC004-TK013 | Document validation findings (gaps, issues, improvements) | `planned` | — |
| T102B-PH001-ST001-AC004-TK014 | Update request version to v1.0 | `planned` | — |
| T102B-PH001-ST001-AC004-TK015 | Remove `[M]`/`[O]`/`[D]` classification markers from Request `###` section headings (markers kept in template only) | `planned` | — |
| T102B-PH001-ST001-AC004-TK016 | Convert Problem Statement (Section A.1) from W1-W7 table to concise narrative paragraph with `T102B-RES-001` reference | `planned` | — |
| T102B-PH001-ST001-AC004-TK017 | Populate INT items (`T102B1-INT-001`, `T102B1-INT-002`) in Section H for cross-epic coordination (T102A alignment, T102B4 RLITE dependency) | `planned` | — |
| T102B-PH001-ST001-AC004-TK018 | Absorb `T102-RES-004` integration recommendations: verify Section H removal/promotion outcomes and document exception mechanism per `analysis_T102-RES-004_issues-risks-architecture.md` (dependency resolved 2026-02-09) | `planned` | — |

**Success Criteria Checklist**:
- [ ] All request content migrated to new template structure
- [ ] All Mandatory sections (M) complete
- [ ] Optional sections (O) populated where applicable
- [ ] Deferred sections (D) contain appropriate placeholders/references
- [ ] Validation findings documented
- [ ] Request version updated to v1.0
- [ ] Self-hosting demonstrates template utility

---

### Activity AC005: Client Approval Gate

**Activity ID**: `T102B-PH001-ST001-AC005`

**Purpose**: Obtain formal Client approval for RST template and validated request artifact.

**Deliverable**: Approval statement recorded in stream plan.

**Scope**:
- In scope: RST template approval, validated request approval, stream completion sign-off
- Out of scope: ST002-ST004 approval

**Task Register**:

| Task ID | Description | Status | Action |
|:--|:--|:--|:--|
| T102B-PH001-ST001-AC005-TK001 | Present RST template for Client review | `planned` | — |
| T102B-PH001-ST001-AC005-TK002 | Present validated request_T102B1-RST.md for Client review | `planned` | — |
| T102B-PH001-ST001-AC005-TK003 | Address Client feedback/questions | `planned` | — |
| T102B-PH001-ST001-AC005-TK004 | Obtain explicit approval statement | `planned` | — |
| T102B-PH001-ST001-AC005-TK005 | Record approval in stream plan | `planned` | — |
| T102B-PH001-ST001-AC005-TK006 | Update Feature Register status (T102B1 → approved) | `planned` | — |

**Success Criteria Checklist**:
- [ ] RST template approved by Client
- [ ] Validated request approved by Client
- [ ] Approval statement recorded with date
- [ ] Feature Register updated (T102B1 status = approved)
- [ ] Stream status updated to complete

---

## V. KEY DESIGN DECISIONS (PENDING)

Design decisions to be resolved during AC002 (RST Specification Refinement). Decisions confirmed during consultation SHOULD be treated as locked inputs for AC002 execution.

| Decision ID | Topic | Options | Recommendation | Status | Resolved In |
|:--|:--|:--|:--|:--|:--|
| DEC-T102B-PH001-ST001-001 | Section J redesign | (A) Story Index only, (B) Story Index + summary FRs, (C) Full deferral / removal | Option A per STD-003 | `confirmed` | Consultation (2026-02-06) |
| DEC-T102B-PH001-ST001-002 | FR/IG merge pattern | (A) Single section, (B) FR with inline guidance, (C) IG subsection | Option B per IG-002 | `confirmed` | Consultation (2026-02-06) |
| DEC-T102B-PH001-ST001-003 | Section classification taxonomy | (A) Binary M/O, (B) Ternary M/O/D | Option B per STD-002 | `confirmed` | Consultation (2026-02-06) |
| DEC-T102B-PH001-ST001-004 | “Conditional” applicability handling | (A) Add 4th type “C”, (B) Optional + applicability rule (e.g., required-if) | Option B (no “C”) | `confirmed` | Consultation (2026-02-06) |
| DEC-T102B-PH001-ST001-005 | Canonical Full Request section list | (A) A–J canonical, (B) STD-002 list canonical, (C) Hybrid | Option B (STD-002 list canonical; Request traceable) | `confirmed` | Consultation (2026-02-06) |

---

## VI. SUCCESS CRITERIA (Stream-level)

- [x] `request_T102B1-RST.md` v0.1 created (lightweight, SRS/BRD hybrid structure)
- [x] Industry standards alignment documented
- [x] Section classification (M/O/D) defined and applied
- [x] FR/IG consolidation design approved
- [x] Section J disposition decided
- [ ] Post-amendment conformance validated (AC002.2; hard-gated on `T102-PH001-ST005`)
- [ ] `template_request_structural.md` authored
- [ ] `request_T102B1-RST.md` retrofitted to v1.0 (full structure)
- [ ] Self-validation demonstrates template utility
- [ ] Client approval obtained
- [ ] Feature Register updated (T102B1 status = approved)

---

## VII. LINKS REGISTER

| Link Type | Target | Path |
|:--|:--|:--|
| Plan (this file) | Stream 1 Plan | `prompt/artifacts/tasks/T102/T102B/workspace/plan/plan_T102B-PH001-ST001.md` |
| Parent | Phase 1 Plan | `prompt/artifacts/tasks/T102/T102B/workspace/plan/plan_T102B-PH001.md` |
| Sibling | Stream 0 Plan | `prompt/artifacts/tasks/T102/T102B/workspace/plan/plan_T102B-PH001-ST000.md` |
| Sibling | Stream 2 Plan | `prompt/artifacts/tasks/T102/T102B/workspace/plan/plan_T102B-PH001-ST002.md` |
| Dependency | T102 Stream 5 Plan (ST005) | `prompt/artifacts/tasks/T102/consultant/workspace/plan/plan_T102-PH001-ST005.md` |
| Deliverable | RST Request | `prompt/artifacts/tasks/T102/T102B/request/request_T102B1-RST.md` |
| Deliverable | RST Template | `prompt/templates/request/request_structural_template.md` |
| Research | T102B-RES-001 | `prompt/artifacts/tasks/T102/T102B/research/report/report_T102B-RES-001_request-artifact-analysis.md` |
| Exemplar | T102A-SPSST Request | `prompt/artifacts/tasks/T102/consultant/request/request_T102A-SPSST.md` |
| SSOT | T102 SPS | `prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md` |
| SSOT | T102 Concept | `prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md` |
| Notes | AC001 Notes | `prompt/artifacts/tasks/T102/T102B/workspace/notes/PH001/ST001/notes_T102B-PH001-ST001-AC001.md` |
| Notes | AC002 Notes | `prompt/artifacts/tasks/T102/T102B/workspace/notes/PH001/ST001/notes_T102B-PH001-ST001-AC002.md` |
| Notes | AC002.2 Notes | `prompt/artifacts/tasks/T102/T102B/workspace/notes/PH001/ST001/notes_T102B-PH001-ST001-AC002.2.md` |
| Proposal | RST Non-Normative | `prompt/artifacts/tasks/T102/T102B/workspace/proposal/T102B1/proposal_T102B1-RST_non_normative.md` |
| Notes | AC002 Session 2 Transcript | `prompt/artifacts/tasks/T102/T102B/raw/PH001/ST001/raw_T102B-PH001-ST001-AC002_2026-02-07_p2.txt` |

---

## VIII. OPEN QUESTIONS REGISTER

| ID | Topic | Question | Owner | Status | Proposed Date | Resolved Date |
|:--|:--|:--|:--|:--|:--|:--|
| OQ-T102B-PH001-ST001-001 | Section J pattern | Which Story Index pattern best balances traceability and overhead reduction? | Client | Resolved | 2026-02-04 | 2026-02-06 |
| OQ-T102B-PH001-ST001-002 | FR/IG merge | Which consolidation pattern best eliminates duplication while preserving clarity? | Client | Resolved | 2026-02-04 | 2026-02-06 |
| OQ-T102B-PH001-ST001-003 | Classification granularity | Is ternary (M/O/D) sufficient or is quaternary (M/O/D/C) needed? | Client | Resolved | 2026-02-04 | 2026-02-06 |
| OQ-T102B-PH001-ST001-004 | T102D scope dependency | If `T102D (DESIGN)` is not started or not needed, what is the downstream target for Story Index "Design Link", and what is the minimal story-level scope boundary? | Client | Resolved | 2026-02-06 | 2026-02-07 |

**OQ-004 Resolution**: Design Link = TBD placeholder in RST template; formal resolution deferred to T102D initiation. AC003-TK016 encodes this in Section J template instructions.

---

## IX. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-02-04 | Initial | Stream 1 plan created; 8 activities defined with detailed task registers; design decisions pending resolution during execution |
| v2.0.0 | 2026-02-05 | Major Amendment | Consolidated AC002–AC005 into single AC002 ("RST Specification Refinement") per DEC008; renumbered AC006→AC003, AC007→AC004, AC008→AC005; marked AC001 completed; updated all registers, dependencies, and success criteria. Evidence: `notes_T102B-PH001-ST001-AC001.md` Session 2 (Plan Amendment) |
| v2.1.0 | 2026-02-06 | Amendment | Updated AC002 plan content to be standards-first (STD-002 canonical section list + traceability), locked consultation decisions (Section J, FR/IG, M/O/D taxonomy, "Conditional" remediation), and updated decision/OQ registers accordingly |
| v2.2.0 | 2026-02-07 | Amendment | Closed AC002: Activity Register → `completed`; all 9 tasks → `completed` with action summaries; success criteria ticked; OQ-004 resolved (Design Link = TBD). Updated AC003: added TK015 (notes title fix), TK016 (OQ-004 encoding); added proposal to Inputs Required; execution mode refined to dev-first then single-deliverable review. Updated stream-level success criteria, decision summary §6, and links register. |
| v2.3.0 | 2026-02-08 | Plan Amendment | AC002 re-review remediation: Registered AC002.1 subactivity (16 tasks); updated AC003 dependency (AC002→AC002.1); updated AC003 task register (TK008/TK009 revised, TK017 added for Section K); updated AC004 task register (TK015-TK018 added for deferred items); added decisions 7-13 to Stream Decision Summary |
| v2.3.1 | 2026-02-09 | Amendment | Post-RES-004 integration alignment: added integration analysis as AC002.1 input; marked AC002.1 TK012/TK013 completed with evidence; strengthened TK005/TK014 actions using accepted integration guidance; removed stale ST004 blocking language from AC004 TK018; renamed AC004 G/H tasks to match Governance Standards + Feature Guidance & Notes |
| v2.4.0 | 2026-02-10 | Completion | Closed AC002.1: updated `T102B-STD-002` to v2.0 (A-K + major section restructure + changelog), remediated `request_T102B1-RST.md` to v0.3.0, promoted feature Issues/Risks to epic scope in SPS with supersession notes, and completed AC003/AC004 register alignment for post-remediation execution. |
| v2.4.1 | 2026-02-10 | Plan Amendment | Registered AC002.2 as a post-ST005 conformance gate (analysis-first evidence) and added acceptance-level dependency from AC005 on AC002.2 to enforce hard-gated validation prior to final stream approval. |
