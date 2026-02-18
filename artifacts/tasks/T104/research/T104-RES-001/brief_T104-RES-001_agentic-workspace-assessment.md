---
artifact_type: 'RESEARCH_BRIEF'
initiative_id: 'T104'
initiative_code: 'CWS'
research_id: 'T104-RES-001'
title: 'Agentic Workspace Assessment'
version: '1.0.0'
iteration: '1'
date: '2026-01-18'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
roadmap_reference: 'prompt/artifacts/tasks/T104/workspace/PH000/plan_T104-PH000.md'
report_template: 'prompt/templates/researcher/template_research_report.md'
governance_rules: 'prompt/templates/consultant/workspace/workspace_documentation_rules.md'
---

# RESEARCH BRIEF: Agentic Workspace Assessment (T104-RES-001)

## I. EXECUTIVE SUMMARY

**Context**: T104 Phase 0 Stream 2 commissions research to validate the *end-to-end* consultant workspace workflow (Roadmap/Notes/Proposal/Analysis/Changelog as workflow tools) while Streams 3–4 draft T104 SSOT scaffolds (`sps_T104-CWS.md`, `concept_T104-CWS.md`) in parallel (scaffolding only). The immediate blocker is unclear and inconsistent boundaries between “workflow tools” vs “SSOT artifacts”, plus uncertainty whether the planned epic set (T104A–T104E) is correctly separated.

**Objective**: Produce evidence-backed recommendations (internal exemplars + external industry practices) that define:
1) what each T104 workspace artifact type is for (as an agentic workflow tool),
2) what SSOT artifacts are for (SPS/Concept/Request), and
3) what standards and scope boundaries T104 should lock next to safely proceed with SSOT scaffolding.

**Target Deliverable**: A research report consumed by `LLM_Consultant` to:
- propose grounded updates to workspace standards (including `workspace_documentation_rules.md` recommendations),
- confirm whether T104 should keep the epics `T104A–T104E` as currently scoped (recommendations only; verdict by LLM_Consultant + Client), and
- inform Phase 1 finalization decisions (Stream 3–4 scaffolding may proceed in parallel, but final standards/merges require review).

## II. RESEARCH SCOPE & TOPICS

### Part A: Current State (Internal Evidence)

#### Topic 1: Artifact Inventory & Gap Map (P1)
**Objective**: Establish what exists today (templates + exemplars) and what is missing or contradictory for a full agentic consultant workflow.
**Context**: The initiative is explicitly using multiple “workspace artifacts” (roadmap/notes/proposal/analysis/changelog) as tools to coordinate LLM roles and reduce drift, but the repo’s governance rules and headings are not fully aligned.
**Specific Questions**:
* What files currently exist (or are referenced as targets) for T104, and where do they live?
* Where are the current contradictions (e.g., headings hierarchy in `workspace_documentation_rules.md` vs T104 Phase → Stream → Activity → Task)?
* What minimum set of artifacts is required for the workflow to function end-to-end?
**Deliverable**: A matrix: Artifact Type × Purpose × Mandatory Sections × Location × Current State × Gaps.

#### Topic 2: Tooling vs SSOT Role Boundaries (P1)
**Objective**: Define “what goes where” for workflow tools vs SSOT artifacts in a way that prevents duplication and drift.
**Context**: For this initiative, roadmap/notes/proposal/analysis/changelog are intentionally used as workflow tools. SPS/Concept/Request are SSOT artifacts.
**Specific Questions**:
* For each tool artifact (Roadmap / Notes / Proposal / Analysis / Changelog), what content MUST it contain, and what MUST it NOT contain?
* **Proposal vs Analysis**: what is the boundary between “analysis/synthesis” and “proposal/specification”, and what is the approval-gate expectation? (**Rule**: proposals MUST be client-approved before merging into SSOT and/or implementation.)
* For SSOT artifacts (SPS / Concept / Request), what content MUST remain SSOT-only?
* What are the most common anti-patterns (duplication, embedding specs into notes, embedding operational tasks into SPS, etc.) and how should T104 guard against them?
**Deliverable**: A concise ruleset of MUST / MUST NOT statements per artifact type, with examples grounded in internal exemplars.

#### Topic 3: Naming, Location, and Discoverability Standards (P1)
**Objective**: Validate and recommend a consistent naming + directory standard for T104 artifacts that reduces confusion between “notes/logs” and “changelogs”.
**Context**: T104 is standardizing prefixes (e.g., `notes_` to avoid conflict with `changelog_`), but this needs to be justified and made consistent across future epics.
**Specific Questions**:
* Are the current prefixes (`roadmap_`, `notes_`, `changelog_`) sufficiently clear for humans and tools?
* Should there be any additional required metadata fields (YAML header keys) to improve toolability?
* What is the minimum discoverable directory layout for `prompt/artifacts/tasks/T104/{workspace,ssot,research}`?
**Deliverable**: A recommended naming + placement standard, including what a “Phase 0 file set” should look like for a new initiative.

### Part B: Workflow Model (How It Should Run)

#### Topic 4: Timeline Model and Heading Semantics (P1)
**Objective**: Validate the chosen timeline hierarchy (Phase → Stream → Activity → Task) and how it maps to governance gates and SSOT “Phase & Gates”.
**Context**: “Stream” is being used as an activity grouping layer (not a governance gate). The governance gate sits at the Phase level.
**Specific Questions**:
* What is the simplest rule to prevent “Stream == Subphase” from reappearing as a hidden gate layer?
* How should registers be structured (Stream Register vs Activity Register) to keep the roadmap readable and mechanically consistent?
* How should this map to SSOT governance tables that talk about “Phase & Gates”?
**Deliverable**: A mapping table: Phase/Stream/Activity/Task → headings → registers → gate points → required evidence.

#### Topic 5: Update Cadence, Gates, and Evidence (P2)
**Objective**: Define recommended update cadence and “exit evidence” rules for Roadmap/Notes/Changelog so SSOT scaffolding is not started prematurely.
**Context**: Stream 2 runs in parallel with Streams 3–4 (scaffolding only), but its outputs inform Phase 1 finalization. The research must specify what “done” means for proceeding with Phase 1 standards finalization and SSOT content merges.
**Specific Questions**:
* What evidence should be required to exit Stream 2 and start Stream 3?
* What belongs in Notes vs Changelog vs Roadmap updates, and when?
* What minimal “anti-drift” safeguards should be mandated?
**Deliverable**: A Stream 2 exit checklist + recommended cadence rules per artifact type.

#### Topic 6: Traceability & Indexing (P2)
**Objective**: Define how decisions, issues/risks, and references should be tracked across workflow tools and promoted into SSOT (if at all).
**Context**: T104 will follow T102 ADR standards, but needs a practical workflow for capturing and using those IDs from workspace tooling.
**Specific Questions**:
* Where should Issues/Risks be first discovered and recorded (report vs notes vs roadmap)?
* How should IDs be referenced to avoid duplication of normative content?
* What minimum cross-links should always exist between roadmap / notes / report / SSOT?
**Deliverable**: A recommended traceability policy (minimum links + where IDs live).

### Part C: Epic Set Validation (Directionality)

#### Topic 7: Epic Set Sanity Check — T104A–T104E (P1)
**Objective**: Recommend whether the planned epics are necessary and correctly separated:
- `T104A (ROADMAP)`
- `T104B (NOTES)`
- `T104C (PROPOSAL)`
- `T104D (ANALYSIS)`
- `T104E (CHANGELOG)`
**Context**: The goal is to define standards that support agentic workflows; the epic set must reflect real lifecycle separation, not redundant file types.
**Specific Questions**:
* Should any of these be merged, renamed, removed, or added (recommend only)?
* Which epic boundaries are required to prevent drift and enable consistent agent workflows?
* What minimum outputs should each epic be responsible for, and which should remain SSOT-only?
**Deliverable**: A “Keep / Merge / Remove / Add” recommendation table with rationale and impact on Stream 3 SSOT scaffolding.

---

## III. CONSTRAINTS, ASSUMPTIONS & METHODOLOGY

### A. Constraints
* **Define-standards only**: This research MUST NOT recommend mass migrations or bulk refactors as part of Phase 0. Proposals should be forward-looking standards and minimal deltas only.
* **Repo-first evidence**: Internal claims MUST cite specific repo files.
* **External grounding required**: External web research SHOULD be used to support recommendations (especially for changelog/meeting notes/decision log conventions and roadmap/planning practices). If external browsing is unavailable, state limitations explicitly and rely on internal exemplars + established standards already present in the repo.

### B. Assumptions
* T104 roadmaps use the timeline hierarchy **Phase → Stream → Activity → Task** with `###` as Stream and `####` as Activity.
* SSOT artifacts for T104 live under `prompt/artifacts/tasks/T104/ssot/`.
* Notes artifacts use `notes_...` (not `log_...`) to avoid confusion with `changelog_...`.

### C. Methodology “Hierarchy of Truth”
If sources conflict, the report MUST:
1) document the conflict,
2) explain tradeoffs,
3) recommend a resolution (do not silently override).

Recommended precedence for this initiative:
1. **Project governance standards already adopted** (T102 SSOT + ADR standards).
2. **Internal exemplars in this repo** (how the project actually operates today).
3. **External industry references** (PM/SE documentation practices) to justify improvements and reduce ambiguity.
4. **Templates** (intended structure; may be outdated and should be updated if necessary).

---

## IV. CROSS-TOPIC INTEGRATION

*   **Integration Question 1**: If we keep separate Roadmap + Notes + Changelog, what minimum linking rules prevent duplication and drift?
*   **Integration Question 2**: Which recommendations require SSOT updates (SPS/Concept), versus workspace tool updates (rules/templates)?
*   **Gap Analysis**: What minimum missing standards would block Stream 3 SSOT scaffolding?

---

## V. INPUT PACKET (CONTEXT MAP)

### A. Core Governance (SSOT Exemplars)
* SSOT SPS exemplar: `prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md`
* SSOT Concept exemplar: `prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md`

### B. T104 Internal Artifacts (Initiative Current State)
* Phase 0 Plan (initiative): `prompt/artifacts/tasks/T104/workspace/PH000/plan_T104-PH000.md`
* Notes (initiative): `prompt/artifacts/tasks/T104/workspace/PH000/notes_T104-PH000.md`

### C. Required Internal Exemplars (Workflow Tools)
* NOTES exemplar: `prompt/artifacts/tasks/T104/T104A/workspace/PH000/ST000/notes_T104A-PH000-ST000.md`
* PROPOSAL exemplar: `prompt/artifacts/tasks/T801/consultant/workspace/proposal/T801A/proposal_T801A_phase1.md`
* CHANGELOG exemplar: `prompt/artifacts/tasks/T102/T102B/workspace/roadmap/changelog_roadmap_T102B-REQUEST_phase0.md.md`

### D. Governing Workspace Rules & Templates
* Workspace rules: `prompt/templates/consultant/workspace/workspace_documentation_rules.md`
* Research brief template: `prompt/templates/researcher/template_research_brief.md`
* Research report template: `prompt/templates/researcher/template_research_report.md`

### E. External References (Recommended Starting Points)
* Changelog conventions:
  - Keep a Changelog — `https://keepachangelog.com/`
* Decision logging / decision records:
  - Atlassian DACI “Decision documentation” template — `https://www.atlassian.com/software/confluence/templates/decision`
* PM terminology (stages/phases) and gating patterns:
  - PRINCE2 “Manage by stages” overview — `https://www.prince2.org.uk/management-overview/`
  - PRINCE2 “Manage by stages” principle (reference) — `https://prince2.wiki/fr/principes/management-par-sequence/`

### F. Anti-Patterns / Exclusions
* **IGNORE**: `archive/` — do not use archived materials as current truth.

---

## VI. DELIVERABLE FORMAT REQUIREMENTS

The research report MUST use the standard template located at:
> `prompt/templates/researcher/template_research_report.md`

**Specific Mapping Instructions for this Brief**:
1. **Section I (Exec Summary)**: MUST end with a concise “recommendations-only” summary that identifies which changes are proposed for:
   - roadmap structure,
   - notes policy,
   - changelog policy,
   - and `workspace_documentation_rules.md`.
2. **Section III (Topic Findings)**: For each topic, include:
   - internal evidence (file references),
   - external references (if available),
   - and a practical recommendation that can be implemented in Stream 3+.
3. **Completeness**: Do NOT delete empty sections. If a topic has no findings, explicitly state “None”.

---

## VII. ISSUES & RISKS REGISTER (T102-STD-007)

The research report MUST include an “Issues & Risks” section that implements `T102-STD-007 (Issues & Risks Index)` exactly.

**Issues**
<!-- GUIDANCE:
Status = `OPEN, IN-REVIEW, RESOLVED, BLOCKED, DEFERRED`,
priority = `Low, Medium, High`
-->
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Resolution Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

**Risks**
<!-- GUIDANCE:
Status = `OPEN, MONITORED, MITIGATED, ACCEPTED, CLOSED`,
priority = `Low, Medium, High`
-->
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Mitigation Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

**ID Rules (T104 scope)**:
* IDs MUST use the scoped, sequential format: `T104-ISSUE-###` and `T104-RISK-###`.
* IDs MUST remain stable once created (no reuse, no renumbering).

---

## VIII. CRITICAL DEPENDENCIES (GOVERNANCE MAPPING)

Map findings to the governance artifacts Stream 3 is expected to draft.

*   **SPS (T104)**: Findings should inform `sps_T104-CWS.md` skeleton, including SPS Section III.A (problem framing) and the epic register (T104A–T104E).
*   **Concept (T104)**: Findings should inform candidate ADR topics for `concept_T104-CWS.md` (e.g., artifact role boundaries, changelog standard, roadmap structure rules).
*   **Workspace Rules**: Findings should identify concrete deltas for `workspace_documentation_rules.md` (recommend only; do not implement inside the report).

---

## IX. SUCCESS CRITERIA

* The brief and report clearly define “workflow tools vs SSOT” boundaries with MUST / MUST NOT rules.
* The report covers the end-to-end pipeline (not a single-epic deep dive) and includes both internal exemplar evidence and external grounding where possible.
* The report provides a clear recommendation on whether T104 should keep the epic set `T104A–T104E` as scoped (recommendations only).
* The report proposes concrete, implementable deltas for `workspace_documentation_rules.md` grounded in industry practices and internal evidence.
