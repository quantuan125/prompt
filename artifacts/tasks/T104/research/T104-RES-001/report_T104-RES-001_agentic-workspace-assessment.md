---
artifact_type: 'REPORT'
initiative_id: 'T104'
epic_id: 'T104'
research_id: 'T104-RES-001'
version: '1.0.0'
iteration: '1'
date: '2026-01-18'
status: 'draft'
author: 'LLM_Researcher'
decision_owner_role: 'Client'
---

# RESEARCH REPORT: Agentic Workspace Assessment (T104-RES-001)

## I. EXECUTIVE SUMMARY

**Context**: T104 Phase 0 Stream 2 commissions research to validate the end-to-end consultant workspace workflow (Roadmap/Notes/Proposal/Analysis/Changelog as workflow tools) while Streams 3–4 draft T104 SSOT scaffolds in parallel (scaffolding only). The immediate blocker is unclear and inconsistent boundaries between “workflow tools” vs “SSOT artifacts”, plus uncertainty whether the planned epic set (T104A–T104E) is correctly separated.  
**Primary reference**: `prompt/artifacts/tasks/T104/research/T104-RES-001/brief_T104-RES-001_agentic-workspace-assessment.md` (lines 22–33).

**Verdict**: **CONDITIONAL GO** — The Phase → Stream → Activity → Task roadmap model is already locked in T104, and the workflow-tool vs SSOT separation is achievable with forward-only standards. However, there is currently material governance/template drift (terminology + artifact role mismatch) that must be resolved before SSOT content merges to avoid duplication and drift.

**Key Findings**:
*   **Finding 1 (Governance Drift)**: `workspace_documentation_rules.md` currently defines Plan/Proposal/Completion roles and a Subphase-based heading hierarchy, which conflicts with T104’s locked Phase → Stream → Activity → Task semantics and its `notes_` policy. See `prompt/templates/consultant/workspace/workspace_documentation_rules.md` (lines 11–20, 58–65) and `prompt/artifacts/tasks/T104/workspace/PH000/plan_T104-PH000.md` (lines 43–49).
*   **Finding 2 (Template Drift)**: `template_workspace_notes.md` labels itself as `NOTES` but its guidance describes a “LOG” and “Subphases”, which is inconsistent with T104’s initiative NOTES usage (“session record”) and with the roadmap’s Open Question about whether to reuse the “log template pattern” for T104B. See `prompt/templates/consultant/workspace/template_workspace_notes.md` (lines 17–33, 44–60) and `prompt/artifacts/tasks/T104/workspace/PH000/plan_T104-PH000.md` (lines 356–358).
*   **Finding 3 (End-to-End Pipeline Gate)**: T104 Phase 0 Links Register declares a required pipeline of: Roadmap → Notes → Research Brief → Research Report → Consultant Analysis → SSOT scaffolds. This report satisfies the Research Report deliverable; the next gate artifact is the Consultant Analysis (`prompt/artifacts/tasks/T104/workspace/_unresolved/analysis_T104-RES-001_agentic-workspace-assessment.md`). See `prompt/artifacts/tasks/T104/workspace/PH000/plan_T104-PH000.md` (lines 336–343).
*   **Finding 4 (Boundary Clarity Exists in Templates)**: The Roadmap template includes explicit anti-drift boundaries (no RID/DR bodies; no execution logs; link to SSOT), and the Proposal/Analysis templates already express a workable separation: Proposal holds normative bodies (post-approval), Analysis is the synthesis bridge between Research and Proposal. See `prompt/templates/consultant/workspace/template_workspace_roadmap.md` (lines 23–37), `prompt/templates/consultant/workspace/template_workspace_proposal.md` (lines 21–30), `prompt/templates/consultant/workspace/template_workspace_analysis.md` (line 19).
*   **Finding 5 (Naming/Discoverability Inconsistencies)**: T104 initiative NOTES standard uses `notes_...` (lowercase) but a T104A note records a decision “`NOTES_` replaces `completion_`” (uppercase), and there are legacy artifacts elsewhere with suffix drift (e.g., `...phase0.md.md`). This indicates a toolability risk if standards are not made strict. See `prompt/artifacts/tasks/T104/workspace/PH000/notes_T104-PH000.md` (lines 26–30), `prompt/artifacts/tasks/T104/T104A/workspace/PH000/ST000/notes_T104A-PH000-ST000.md` (line 27), and `prompt/artifacts/tasks/T102/T102B/workspace/roadmap/changelog_roadmap_T102B-REQUEST_phase0.md.md` (filename).

**Candidate Deltas Summary (recommendations-only; for LLM_Consultant + Client decision)**:
- **Roadmap structure**: Keep Phase → Stream → Activity → Task; enforce that “Stream is a grouping label, not a gate” and define where gating evidence is captured (Roadmap registers + explicit Exit Evidence checklists). (See Topic 4.)
- **Notes policy**: Decide whether `NOTES` are “session records” (initiative-level) vs “decision log + meeting minutes” (subphase-level), then align `template_workspace_notes.md` language accordingly. (See Topic 2/4.)
- **Changelog policy**: Standardize changelog scope per artifact (delta-only) and minimum schema (overview table + bullet details), aligned with “Keep a Changelog” conventions. (See Topic 5/6.)
- **`workspace_documentation_rules.md`**: Align artifact role boundaries to Roadmap/Notes/Proposal/Analysis/Changelog (T104) and reconcile/retire Plan/Completion language (T810A2 legacy) where it conflicts. (See Topic 2.)

---

## II. METHODOLOGY AUDIT

**Scope Adherence**: Stayed within Phase 0 constraints (“define-standards only”; no migrations/refactors recommended as implementation tasks). Focused on evidence capture and boundary clarification.

**Source of Truth Audit**:
*   **Repo governance & standards**:
    *   `prompt/templates/consultant/workspace/workspace_documentation_rules.md`
    *   `prompt/templates/consultant/workspace/template_workspace_roadmap.md`
    *   `prompt/templates/consultant/workspace/template_workspace_notes.md`
    *   `prompt/templates/consultant/workspace/template_workspace_proposal.md`
    *   `prompt/templates/consultant/workspace/template_workspace_analysis.md`
    *   `prompt/templates/researcher/template_research_report.md`
*   **T104 initiative artifacts (current state)**:
    *   `prompt/artifacts/tasks/T104/workspace/PH000/plan_T104-PH000.md`
    *   `prompt/artifacts/tasks/T104/workspace/PH000/notes_T104-PH000.md`
    *   `prompt/artifacts/tasks/T104/workspace/roadmap/changelog_plan_T104-CWS_phase0.md`
    *   `prompt/artifacts/tasks/T104/research/T104-RES-001/brief_T104-RES-001_agentic-workspace-assessment.md`
    *   `prompt/artifacts/tasks/T104/T104A/ssot/roadmap_T104A-ROADMAP_phase0.md`
    *   `prompt/artifacts/tasks/T104/T104A/workspace/PH000/ST000/notes_T104A-PH000-ST000.md`
*   **Cross-initiative exemplars (role boundaries / changelog patterns)**:
    *   `prompt/artifacts/tasks/T801/consultant/workspace/proposal/T801A/proposal_T801A_phase1.md`
    *   `prompt/artifacts/tasks/T102/T102B/workspace/roadmap/changelog_roadmap_T102B-REQUEST_phase0.md.md`

**External references consulted** (web research):
*   Keep a Changelog (format + scope conventions): `https://keepachangelog.com/en/1.1.0/`
*   Atlassian Confluence templates (Decision / Meeting Notes patterns):
    *   Decision template: `https://www.atlassian.com/software/confluence/templates/decision`
    *   Meeting notes templates: `https://www.atlassian.com/software/confluence/templates/meeting-notes`
*   PRINCE2 “Manage by Stages” (staging/gating concept): `https://prince2.com/usa/prince2-methodology/manage-by-stages`

**Limitations**:
*   T104 SSOT scaffold files (`sps_T104-CWS.md`, `concept_T104-CWS.md`) are not yet present; findings related to SSOT integration are necessarily “interface-level” (where links/decisions should live), not “content-level”.
*   T104 Proposal/Analysis workspace artifacts do not yet exist; boundaries are inferred from templates + cross-initiative exemplars (e.g., T801A).

---

## III. TOPIC FINDINGS

### Topic 1: Artifact Inventory & Gap Map (P1)
**Objective**: Establish what exists today (templates + exemplars) and what is missing or contradictory for an end-to-end agentic consultant workflow.

#### A. Evidence & Forensics
*   **Source**: `prompt/artifacts/tasks/T104/workspace/PH000/plan_T104-PH000.md` (lines 332–348).
*   **Observation**: The T104 Phase 0 Links Register defines the minimum end-to-end artifact set and target locations, including Research Report + Analysis + SSOT scaffolds.

*   **Source**: `prompt/artifacts/tasks/T104/workspace/PH000/notes_T104-PH000.md` (lines 23–30, 52–57).
*   **Observation**: Notes explicitly state they are not SSOT and confirm separation of Notes vs Changelog, and `notes_...` naming to avoid collision with `changelog_...`.

#### B. Analysis
*   **Synthesis**: The initiative-level “tool chain” is already defined in Roadmap + Notes, but not all tool artifacts exist yet (Research Report and Analysis are the immediate missing links).
*   **Gap Analysis**:
    *   Declared deliverables exist: Roadmap, Notes, Roadmap Changelog, Research Brief.
    *   Declared deliverables missing: Research Analysis, SSOT scaffolds (expected later per Streams 3–4).
    *   Declared standards source is currently inconsistent: `workspace_documentation_rules.md` does not yet reflect the T104 tool chain.

**Artifact Inventory & Gap Matrix (current state snapshot)**:

| Artifact Type | Role | Minimum Mandatory Sections (as used in repo) | Canonical Location (T104) | Template Exists | T104 Instance Exists | Gaps / Contradictions (evidence pointers) |
| :--- | :--- | :--- | :--- | :---: | :---: | :--- |
| ROADMAP | Workflow tool | Exec Summary; Context; Phase streams/activities; Links Register; Open Questions; Changelog | `prompt/artifacts/tasks/T104/workspace/roadmap/` | ✅ `template_workspace_roadmap.md` | ✅ `plan_T104-CWS_phase0.md` | Governance rules still reference Plan/Subphase model (`workspace_documentation_rules.md` lines 11–20, 58–65) |
| NOTES | Workflow tool | Notes Summary; Session/Stream records; Decision table; Next guidance | `prompt/artifacts/tasks/T104/workspace/notes/` | ✅ `template_workspace_notes.md` | ✅ `notes_T104-CWS_phase0.md` | Notes template uses LOG/Subphase language (`template_workspace_notes.md` lines 17–33, 44–60) |
| CHANGELOG | Workflow tool | Overview table; per-version bullet deltas | Usually co-located with artifact (e.g., roadmap changelog in `workspace/roadmap/`) | ❌ (workspace changelog template not identified) | ✅ `changelog_plan_T104-CWS_phase0.md` | Naming normalization risk (legacy `...md.md` file elsewhere) |
| PROPOSAL | Workflow tool (normative within phase) | Exec Summary; Candidate inventory; full bodies; Issues/Risks; gate readiness | `prompt/artifacts/tasks/T104/workspace/proposal/` (implied by T104 scope + templates) | ✅ `template_workspace_proposal.md` | ❌ | T104-specific instance not yet present; boundary must be explicit per brief (brief lines 51–54) |
| ANALYSIS | Workflow tool (synthesis bridge) | Exec Summary; findings extraction; cross-cutting synthesis; mapping to proposals | `prompt/artifacts/tasks/T104/workspace/analysis/` (declared) | ✅ `template_workspace_analysis.md` | ❌ | Roadmap declares target analysis deliverable (`plan_T104-CWS_phase0.md` line 341) |
| RESEARCH_BRIEF | Research artifact | Brief per template (topics, input packet, constraints) | `prompt/artifacts/tasks/T104/research/brief/` | ✅ `template_research_brief.md` | ✅ `brief_T104-RES-001_agentic-workspace-assessment.md` | None observed |
| RESEARCH_REPORT | Research artifact | Exec Summary; Methodology; Topic Findings; Issues/Risks; Artifact Updates; Sources | `prompt/artifacts/tasks/T104/research/report/` | ✅ `template_research_report.md` | ✅ (this file) | None observed (template issues/risk schema aligned: `template_research_report.md` lines 60–71) |
| SPS | SSOT | Governance baseline + epic register + problem framing | `prompt/artifacts/tasks/T104/ssot/` | (SSOT template exists elsewhere; not assessed here) | ❌ | Roadmap declares target (`plan_T104-CWS_phase0.md` line 342) |
| CONCEPT | SSOT | ADR system placeholders + decision indices | `prompt/artifacts/tasks/T104/ssot/` | (SSOT template exists elsewhere; not assessed here) | ❌ | Roadmap declares target (`plan_T104-CWS_phase0.md` line 343) |

#### C. Governance Implication
*   **Decision Impact**: Before SSOT content merges, the artifact role boundary rules must be stable enough to prevent “Notes become specs” and “Roadmap becomes execution log” drift. The Roadmap template already encodes anti-drift boundaries; governance rules are the remaining alignment point. (See Topic 2.)
*   **Risk**: If the Research Report is treated as synthesis/proposal (instead of raw evidence), then the Analysis phase loses purpose and the “proposal approval gate” becomes ambiguous (brief requires Proposal approval before SSOT merge). See `prompt/artifacts/tasks/T104/research/T104-RES-001/brief_T104-RES-001_agentic-workspace-assessment.md` (lines 51–54).

---

### Topic 2: Tooling vs SSOT Role Boundaries (P1)
**Objective**: Define “what goes where” for workflow tools vs SSOT artifacts in a way that prevents duplication and drift.

#### A. Evidence & Forensics
*   **Source**: `prompt/templates/consultant/workspace/template_workspace_roadmap.md` (lines 23–37).
*   **Observation**: Roadmap boundaries are explicit: no RID/DR bodies; no execution logs; link to SSOT rather than duplicating content.

*   **Source**: `prompt/templates/consultant/workspace/template_workspace_proposal.md` (lines 21–30).
*   **Observation**: Proposal is framed as a “working index → full bodies” workspace where Sections III+ hold full normative bodies for approved IDs, and promotion to SSOT occurs upon gate approval.

*   **Source**: `prompt/templates/consultant/workspace/template_workspace_analysis.md` (line 19).
*   **Observation**: Analysis is explicitly positioned as synthesis between research and proposal, and is created after research report and before proposal updates.

*   **Source**: `prompt/templates/consultant/workspace/workspace_documentation_rules.md` (lines 11–20).
*   **Observation**: The governance rules file currently defines Plan/Proposal/Completion canonical sources (Roadmap = Plan; Execution history = Completion), which does not match T104’s Roadmap/Notes/Changelog naming and may not match current templates.

#### B. Analysis
*   **Synthesis**: Templates (Roadmap/Proposal/Analysis) already provide a coherent “what goes where” separation aligned with the brief’s intent, but `workspace_documentation_rules.md` is still written for an older Plan/Completion model (T810A2).
*   **Gap Analysis**:
    *   Current T104 intent: Roadmap/Notes/Changelog are workflow tools; SPS/Concept/Request are SSOT. (`prompt/artifacts/tasks/T104/research/T104-RES-001/brief_T104-RES-001_agentic-workspace-assessment.md` lines 49–55.)
    *   Current governance rules: Plan/Proposal/Completion. (`workspace_documentation_rules.md` lines 11–19.)
    *   Current Notes template: YAML artifact_type NOTES but narrative calls it a “LOG”, and uses “Subphases”. (`template_workspace_notes.md` lines 17–33, 44–60.)

**Candidate MUST / MUST NOT Boundary Rules (workflow tools vs SSOT)**  
*(These are presented as evidence-backed candidate rules for LLM_Consultant + Client to adopt/modify; they are intended to prevent duplication/drift per the brief.)*

**ROADMAP (workflow tool)**
- MUST define Phase → Stream → Activity → Task plan structure, registers, dependencies, and deliverables. (`plan_T104-CWS_phase0.md` lines 45–49, 71–77; `template_workspace_roadmap.md` lines 23–37)
- MUST link to SSOT artifacts via Links Register; MUST NOT embed SSOT bodies. (`template_workspace_roadmap.md` lines 29–33)
- MUST NOT become an execution log; execution narrative belongs in NOTES. (`template_workspace_roadmap.md` line 31)

**NOTES (workflow tool / session record)**
- MUST capture decisions + rationale + next guidance and remain non-normative. (`notes_T104-CWS_phase0.md` lines 23–24)
- SHOULD use a deterministic decision table with stable DEC-IDs. (`notes_T104-CWS_phase0.md` lines 50–57)
- MUST NOT act as SSOT for standards/specs; MUST reference Roadmap/SSOT instead. (`notes_T104-CWS_phase0.md` lines 23–24)
- External grounding (pattern only): meeting notes/decision log templates emphasize separation of “notes” from canonical spec artifacts. (Atlassian templates: `https://www.atlassian.com/software/confluence/templates/meeting-notes`, `https://www.atlassian.com/software/confluence/templates/decision`)

**PROPOSAL (workflow tool; normative during a phase, pending approval)**
- MUST hold normative bodies (e.g., full E-ID bodies) once approved within the phase; promotion to SSOT occurs after explicit approval gate. (`template_workspace_proposal.md` lines 21–30)
- MUST NOT be used as meeting minutes/decision log; that belongs in NOTES. (Implied by separation in templates + T104 NOTES role; see `template_workspace_notes.md` purpose block lines 17–33)

**ANALYSIS (workflow tool; synthesis bridge)**
- MUST synthesize research findings and map them to proposal/SSOT inputs; created after research report and before proposal updates. (`template_workspace_analysis.md` line 19)
- MUST NOT be treated as the canonical specification; proposal/SSOT remain the normative sources. (Implied by proposal workflow and analysis template positioning: `template_workspace_proposal.md` lines 21–30; `template_workspace_analysis.md` line 19)

**CHANGELOG (workflow tool; delta record per artifact)**
- MUST capture “what changed” in a specific artifact across versions and remain delta-only (not narrative minutes). (`changelog_plan_T104-CWS_phase0.md` lines 5–16; `notes_T104-CWS_phase0.md` lines 42–45)
- SHOULD use a consistent schema (overview table + detailed bullets), aligned with widely used changelog conventions. (Keep a Changelog: `https://keepachangelog.com/en/1.1.0/`)

**SSOT (SPS / CONCEPT / REQUEST)**
- MUST remain the canonical source for governance baseline, decisions, and requirements; workflow tools link to SSOT but do not replace it. (T104 Roadmap locked decisions: `plan_T104-CWS_phase0.md` lines 43–49; brief framing: `prompt/artifacts/tasks/T104/research/T104-RES-001/brief_T104-RES-001_agentic-workspace-assessment.md` lines 49–55)

#### C. Governance Implication
*   **Decision Impact**: T104 needs a stable mapping from prior Plan/Completion language to Roadmap/Notes/Changelog language (or a decision to keep the older model in parallel). Without this, downstream users can interpret templates inconsistently and duplicate normative content across artifacts.
*   **Risk**: If governance rules remain inconsistent, agent behavior will drift (e.g., placing execution history into Roadmaps, or placing specifications into Notes), reducing auditability and making SSOT merges risky.

---

### Topic 3: Naming, Location, and Discoverability Standards (P1)
**Objective**: Validate and recommend a consistent naming + directory standard for T104 artifacts that reduces confusion between “notes/logs” and “changelogs”.

#### A. Evidence & Forensics
*   **Source**: `prompt/artifacts/tasks/T104/workspace/roadmap/plan_T104-CWS_phase0.md` (lines 43–49).
*   **Observation**: Locked decisions include `notes_...` prefix, `changelog_...` as separate file, and SSOT location under `prompt/artifacts/tasks/T104/ssot/`.

*   **Source**: `prompt/artifacts/tasks/T104/T104A/workspace/PH000/ST000/notes_T104A-PH000-ST000.md` (line 27).
*   **Observation**: A decision log bullet states “`NOTES_` replaces `completion_`”, which is inconsistent with T104 initiative usage of `notes_...` (lowercase) and can introduce toolability ambiguity.

*   **Source**: `prompt/artifacts/tasks/T102/T102B/workspace/roadmap/changelog_roadmap_T102B-REQUEST_phase0.md.md` (filename).
*   **Observation**: Legacy double extension suggests filename normalization is necessary for discoverability and automated tooling (even if Phase 0 forbids mass migration).

#### B. Analysis
*   **Synthesis**: T104’s directory layout is already clear (`prompt/artifacts/tasks/T104/{workspace,ssot,research}`), but naming conventions need stricter normalization to prevent collisions (notes/log vs changelog) and tool parsing issues (case sensitivity and suffix drift).
*   **Gap Analysis**:
    *   Case drift (`notes_` vs `NOTES_`) and terminology drift (`NOTES` vs `LOG`) exists across artifacts/templates.
    *   Some manifests reference changelog files that do not exist, signaling repository-wide “changelog path integrity” gaps (see `prompt/templates/request/request_manifest.json` line 12).

#### C. Governance Implication
*   **Decision Impact**: Naming and location rules are foundational for toolability (agents locating the right artifact) and for “link-don’t-duplicate” discipline.
*   **Risk**: If naming is not normalized, automated referencing and retrieval (by agents) will become unreliable; humans will also misfile content (e.g., adding notes into changelog).

---

### Topic 4: Timeline Model and Heading Semantics (P1)
**Objective**: Validate the timeline hierarchy (Phase → Stream → Activity → Task), how it maps to governance gates, and how to prevent “Stream == gate” drift.

#### A. Evidence & Forensics
*   **Source**: `prompt/artifacts/tasks/T104/workspace/roadmap/plan_T104-CWS_phase0.md` (lines 45–47, 71–77).
*   **Observation**: Timeline semantics are locked; “Parallelism & Dependencies” standard defines `Execution Mode` and `Depends On` as enforceable constraints.

*   **Source**: `prompt/templates/consultant/workspace/template_workspace_roadmap.md` (lines 34–37, 86–93).
*   **Observation**: The Roadmap template encodes heading semantics (`###` Streams, `####` Activities) and dependency notation.

*   **Source**: `prompt/templates/consultant/workspace/workspace_documentation_rules.md` (lines 58–65).
*   **Observation**: Governance rules currently define `###` as “Subphase” for Plan artifacts, conflicting with the T104 Roadmap standard’s use of `###` as Stream.

#### B. Analysis
*   **Synthesis**: T104’s roadmap model is structurally coherent and toolable (tables + enforced headings). The remaining risk is cross-document semantic drift introduced by older “Plan/Subphase” standards and templates that still speak in Subphases.
*   **Gap Analysis**:
    *   Roadmap standard is locked in T104.
    *   Governance rules and Notes template still “pull” toward a Subphase model and/or “LOG” semantics.

**Phase/Stream/Activity/Task Mapping Table (headings → registers → gates → evidence)**:

| Timeline Level | Meaning | Markdown Semantics (T104) | Register Placement | Gate Point | Expected Evidence Location |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Phase | Primary governance “stage” boundary (initiative-level milestone) | In Roadmap: `#` title + Phase section under `## III. PHASE 0...` (see `plan_T104-CWS_phase0.md` lines 20, 67) | Stream Register + Activity Register | YES (Phase exit milestone / readiness) | Roadmap Exit Milestone bullets + linked artifacts (Research Report + Analysis + SSOT scaffolds) (`plan_T104-CWS_phase0.md` lines 37–41, 336–343) |
| Stream | Grouping label for related Activities (NOT a gate) | `### Stream X: ...` (`plan_T104-CWS_phase0.md` line 118+) and `###` reserved for Streams (`plan_T104-CWS_phase0.md` line 46; `template_workspace_roadmap.md` lines 34–37) | Stream Register row + Activity Register “Stream” column | NO (unless explicitly declared `Execution Mode = GATED`) | If gated, Roadmap Stream section “Exit Evidence” checklist (pattern from template: `template_workspace_roadmap.md` lines 115–117) |
| Activity | Work unit with a deliverable and success criteria | `#### Activity X.Y: ...` (`template_workspace_roadmap.md` line 119) | Activity Register row | SOMETIMES (local gate: success criteria checklist) | Activity Success Criteria checklist + deliverable link in Roadmap section |
| Task | Checklist execution items under an Activity | Checklist items under Activity | Not required in registers (optional) | NO | Notes (session record) and/or Completion evidence links (if used) |

**Anti-drift guardrail (candidate rule)**: “Stream is an organizational grouping, not a default approval gate.” If a Stream is intended to be a gate, it must declare `Execution Mode = GATED` and include explicit Exit Evidence in the Roadmap Stream section (template pattern: `template_workspace_roadmap.md` lines 115–117; dependency notation: `plan_T104-CWS_phase0.md` lines 71–77).

#### C. Governance Implication
*   **Decision Impact**: If “Stream is not a gate” is not explicitly reinforced in governance rules and Notes templates, downstream work may reintroduce “Subphase” as a hidden gate layer, confusing SSOT “Phase & Gates” mapping.
*   **Risk**: Ambiguous gate placement leads to premature SSOT merges or mis-sequenced work (e.g., starting SSOT authoring before research synthesis is complete).

---

### Topic 5: Update Cadence, Gates, and Evidence (P2)
**Objective**: Define update cadence and “exit evidence” rules for Roadmap/Notes/Changelog so SSOT scaffolding is not started prematurely.

#### A. Evidence & Forensics
*   **Source**: `prompt/artifacts/tasks/T104/workspace/roadmap/plan_T104-CWS_phase0.md` (lines 37–41).
*   **Observation**: Phase 0 Exit Milestone explicitly requires “T104-RES-001 delivered and synthesized (research report + consultant analysis)” prior to SSOT scaffold readiness.

*   **Source**: `prompt/artifacts/tasks/T104/workspace/roadmap/changelog_plan_T104-CWS_phase0.md` (lines 11–16).
*   **Observation**: Changelog entries are already being used to track structural updates (dependency notation, stream parallelism, template roadmap updates).

#### B. Analysis
*   **Synthesis**: The Roadmap already defines the gate condition and the intended separation of concerns: Roadmap for plan/registers, Notes for session record, Changelog for deltas, Research Report for evidence, Analysis for synthesis.
*   **Gap Analysis**:
    *   Cadence rules (when each artifact is updated) are not yet expressed in governance rules; they are implied in the Roadmap and Notes.

**Stream 2 Exit Checklist (candidate; for Phase 0 gate evidence)**:
- [x] Research Brief exists and is linked from Roadmap Links Register (`plan_T104-CWS_phase0.md` lines 339–340; `prompt/artifacts/tasks/T104/research/T104-RES-001/brief_T104-RES-001_agentic-workspace-assessment.md` lines 13–15)
- [x] Research Report delivered at `prompt/artifacts/tasks/T104/research/T104-RES-001/report_T104-RES-001_agentic-workspace-assessment.md` (`plan_T104-CWS_phase0.md` line 340)
- [ ] Consultant Analysis delivered at `prompt/artifacts/tasks/T104/workspace/_unresolved/analysis_T104-RES-001_agentic-workspace-assessment.md` (`plan_T104-CWS_phase0.md` line 341)
- [x] Report includes MUST/MUST NOT boundary candidates (Topic 2) and Phase/Stream/Activity mapping table (Topic 4)
- [x] Report includes Issues/Risks tables in `T102-STD-007` schema (Section IV; template: `template_research_report.md` lines 60–71)
- [x] Report includes an epic-set sanity table (Topic 7) and identifies any boundary overlaps (Notes vs Changelog vs Analysis)

**Update Cadence Rules (candidate; “who updates what when”)**

| Artifact | Update Trigger | Update Owner | Notes |
| :--- | :--- | :--- | :--- |
| ROADMAP | Scope/sequence changes; register updates; gate status changes | LLM_Consultant | Keep operational detail out; record deltas in changelog |
| NOTES | Each consultation session / decision point | LLM_Consultant + Client | Session record + decisions + next guidance |
| CHANGELOG | Every version bump of the associated artifact | LLM_Consultant | Delta-only; keep narrative minutes out |
| RESEARCH_BRIEF | When scope changes (commissioning iteration) | LLM_Consultant | Researcher consumes latest brief |
| RESEARCH_REPORT | Per brief iteration / when findings materially change | LLM_Researcher | Evidence-first; avoid proposal-level prescriptions |
| ANALYSIS | After report delivery; before proposal/SSOT updates | LLM_Consultant | Synthesis + recommendations belong here (template intent) |

**External grounding (gating concept)**: PRINCE2 “Manage by Stages” emphasizes gated progression (do not proceed to the next stage without sufficient control/evidence), which aligns with keeping “gate evidence” explicit in Roadmaps rather than diffuse across Notes/Changelogs. (Reference: `https://prince2.com/usa/prince2-methodology/manage-by-stages`)

#### C. Governance Implication
*   **Decision Impact**: The gating model (what must exist before moving forward) should remain centralized in Roadmaps and be referenced from Notes/Changelog to avoid divergent “what is done” interpretations.
*   **Risk**: If Notes or Changelog become the de facto gate evidence source, the Roadmap loses authority as a coordination tool.

---

### Topic 6: Traceability & Indexing (P2)
**Objective**: Define how decisions, issues/risks, and references should be tracked across workflow tools and promoted into SSOT (if at all).

#### A. Evidence & Forensics
*   **Source**: `prompt/artifacts/tasks/T104/workspace/PH000/notes_T104-PH000.md` (lines 50–57).
*   **Observation**: Notes use stable DEC-IDs for decisions (DEC-0.S1-### style) and record decisions as a table (traceable, scannable).

*   **Source**: `prompt/templates/researcher/template_research_report.md` (lines 60–71).
*   **Observation**: Research reports must include Issues/Risks in the `T102-STD-007` schema (now aligned in the template).

#### B. Analysis
*   **Synthesis**: The project already uses a consistent pattern: structured tables for traceable IDs (DEC tables in Notes; Issues/Risks tables in Research/SSOT contexts). The key is to keep normative content out of the trace logs and rely on references.
*   **Gap Analysis**:
    *   There is not yet a single published “minimum cross-link policy” (e.g., Roadmap must link to Notes/Changelog/Research; Research must link back to Brief/Roadmap; SSOT must link to Roadmap but not duplicate operational detail). The Roadmap Links Register suggests the intended minimum set.

**Minimum Cross-Link Policy (candidate; “link-don’t-duplicate” safeguard)**:
- ROADMAP MUST include Links Register entries for Notes, Changelog, Research Brief/Report, Analysis, and SSOT targets. (Already present: `plan_T104-CWS_phase0.md` lines 332–348.)
- NOTES SHOULD reference the governing Roadmap and SSOT targets (already present: `notes_T104-CWS_phase0.md` line 11; plus “not SSOT” statement lines 23–24).
- RESEARCH REPORT SHOULD cite the Brief version and the governing commit hash (Section VI) and SHOULD cite file/line evidence for internal claims (Topic sections).
- ANALYSIS SHOULD reference both Research Brief and Research Report (analysis template requires both: `template_workspace_analysis.md` lines 11–13).
- SSOT artifacts SHOULD link back to Roadmap and reference (not copy) operational details (Roadmap intent: `plan_T104-CWS_phase0.md` lines 43–49).

**ID Placement (candidate policy)**:
- Decision IDs (DEC-*) are first captured in NOTES (session record), then (optionally) promoted into SSOT (Concept ADR/GDR) if they become governing policy. (Notes evidence: `notes_T104-CWS_phase0.md` lines 50–57.)
- Issues/Risks discovered during research should be captured in the Research Report (Section IV) with scoped, stable IDs (`T104-ISSUE-###`, `T104-RISK-###`), then (optionally) promoted into SSOT/initiative registers following the project’s cross-scope de-duplication approach.

#### C. Governance Implication
*   **Decision Impact**: A deterministic cross-link policy is the most lightweight anti-drift safeguard for an agentic workspace (agents can always traverse to canonical sources).
*   **Risk**: Without consistent cross-links, agents will “hallucinate” or infer where content lives and reintroduce duplication.

---

### Topic 7: Epic Set Sanity Check — T104A–T104E (P1)
**Objective**: Determine whether epics are necessary and correctly separated to reflect real workflow lifecycle separation.

#### A. Evidence & Forensics
*   **Source**: `prompt/artifacts/tasks/T104/workspace/roadmap/plan_T104-CWS_phase0.md` (lines 24–29, 43–49).
*   **Observation**: The initiative explicitly scopes epics by artifact type (Roadmap, Notes, Proposal, Analysis, Changelog) and locks “define standards only” for T104E (Changelog).

*   **Source**: `prompt/artifacts/tasks/T104/research/T104-RES-001/brief_T104-RES-001_agentic-workspace-assessment.md` (lines 97–109).
*   **Observation**: The brief requires a keep/merge/remove/add evaluation but notes that the final verdict is owned by LLM_Consultant + Client.

#### B. Analysis
*   **Synthesis**: The epic set is internally consistent with an “artifact role standards” initiative: each epic is a governance scope for one artifact role. The main risk is redundancy if the role boundaries are not clean (e.g., Notes vs Changelog vs Analysis).
*   **Gap Analysis**:
    *   Roadmap/Changelog patterns are already operational in T104.
    *   Notes exists at initiative-level but template language is not aligned (LOG/Subphase).
    *   Proposal/Analysis standards exist as templates, but T104-specific instances are not yet created in Phase 0.

**Keep / Merge / Remove / Add Table (candidate; verdict owned by LLM_Consultant + Client)**:

| Epic | Primary Scope | Keep/Merge/Remove/Add | Rationale (evidence-based) | Minimum Outputs (standards-only) |
| :--- | :--- | :--- | :--- | :--- |
| T104A (ROADMAP) | Roadmap structure + dependency notation + heading semantics | KEEP | Roadmap template already encodes anti-drift boundaries and heading semantics (`template_workspace_roadmap.md` lines 23–37) | Roadmap template + rules alignment notes |
| T104B (NOTES) | Notes/session record standard (decisions + minutes) | KEEP | Notes are explicitly non-SSOT and already used in T104 (`notes_T104-CWS_phase0.md` lines 23–24); template semantics need alignment (Topic 2) | Notes template semantics decision + ID rules |
| T104C (PROPOSAL) | Proposal/specification workflow standard | KEEP | Proposal template expresses “working index → full bodies” and explicit SSOT promotion gate (`template_workspace_proposal.md` lines 21–30) | Proposal template usage rules + approval gate statement |
| T104D (ANALYSIS) | Research synthesis standard (bridge research→proposal) | KEEP | Analysis template explicitly positions analysis after report and before proposal updates (`template_workspace_analysis.md` line 19) | Analysis template usage rules + mapping requirements |
| T104E (CHANGELOG) | Changelog standard (define-only) | KEEP | T104 already uses separate changelog files and defines T104E as “define standards only” (`plan_T104-CWS_phase0.md` lines 47–49) | Changelog schema and naming standard |

#### C. Governance Implication
*   **Decision Impact**: The epic set can be treated as a decomposition of “standards surfaces” to avoid monolithic governance changes; this supports incremental adoption.
*   **Risk**: If the epics are treated as “more documents to write” rather than “standards owners”, they may increase overhead without reducing drift.

---

### Topic 8: External Comparison (Industry Patterns)
**Objective**: Ground T104’s workflow-tool separation and changelog/notes practices against widely used industry conventions.

#### A. Evidence & Forensics
*   **Source**: Keep a Changelog — `https://keepachangelog.com/en/1.1.0/`
*   **Observation**: Changelogs are conventionally treated as artifact-scoped, versioned delta records (not meeting minutes), with a standard entry structure (overview + categorized changes).

*   **Source**: Atlassian Confluence templates — `https://www.atlassian.com/software/confluence/templates/meeting-notes` and `https://www.atlassian.com/software/confluence/templates/decision`
*   **Observation**: Industry templates separate “meeting notes” (discussion + actions) from “decisions” (structured decision log), reinforcing T104’s need to keep session records separate from artifact deltas and from canonical specs.

*   **Source**: PRINCE2 “Manage by Stages” — `https://prince2.com/usa/prince2-methodology/manage-by-stages`
*   **Observation**: Stage-based governance patterns emphasize explicit gates and evidence before progression, aligning with keeping gate evidence centralized (Roadmap) rather than diffuse.

#### B. Analysis
*   **Synthesis**: External patterns support T104’s intended separation:
    *   Changelog = delta-only record per artifact/version (not a narrative log).
    *   Notes/decision logs = session continuity + structured decisions (but not normative spec bodies).
    *   Governance gates should be explicit and evidence-backed, matching the Roadmap Exit Milestone model.
*   **Gap Analysis**: The main gap is not the direction of the T104 model; it is internal terminology/template drift that can cause teams/agents to blend these roles (Topic 2–4).

#### C. Governance Implication
*   **Decision Impact**: External conventions can be used as “tie-breakers” when internal sources conflict (e.g., Notes vs Changelog semantics), without requiring new tooling.
*   **Risk**: Over-adopting external conventions without mapping to existing repo practices can create unnecessary churn; this supports a forward-only, minimal-delta approach (Phase 0 constraint).

---

## IV. ISSUE & RISK REGISTER (T102-STD-007)

**Issues**
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Resolution Notes |Resolution Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `T104-ISSUE-001` | Governance rules misaligned with T104 artifact roles | `workspace_documentation_rules.md` defines Plan/Proposal/Completion and Subphase heading semantics that conflict with T104 Roadmap/Notes/Changelog roles and Phase→Stream→Activity model | LLM_Consultant | `OPEN` | `HIGH` | 2026-01-18 | — | — |
| `T104-ISSUE-002` | NOTES template uses LOG/Subphase semantics | `template_workspace_notes.md` artifact_type is NOTES but internal guidance calls it a LOG and structures content as Subphases, creating ambiguity for T104B NOTES scope | LLM_Consultant | `OPEN` | `HIGH` | 2026-01-18 | — | — |
| `T104-ISSUE-003` | Naming/toolability drift (case + suffix) | Evidence of inconsistent naming (`notes_` vs `NOTES_`) and legacy filename suffix drift (e.g., `...md.md`) threatens automated retrieval and human discoverability | LLM_Consultant | `OPEN` | `MEDIUM` | 2026-01-18 | — | — |
| `T104-ISSUE-004` | Missing T104 consultant analysis artifact | Roadmap declares the consultant analysis (`analysis_T104-RES-001_agentic-workspace-assessment.md`) as required Phase 0 exit evidence after report delivery | LLM_Consultant | `OPEN` | `HIGH` | 2026-01-18 | — | — |

**Risks**
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Mitigation Notes |Mitigation Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `T104-RISK-001` | Drift via duplication across tool artifacts | If artifact boundaries are not enforced, specs and decisions will be duplicated across Roadmap/Notes/Analysis/Proposal and later drift from SSOT | Client | `OPEN` | `HIGH` | 2026-01-18 | — | — |
| `T104-RISK-002` | Hidden gate layer reintroduced (Stream/Subphase) | If “Stream” starts being treated as a gate (or Subphase terminology persists), SSOT Phase & Gates mapping becomes ambiguous and sequencing breaks | Client | `OPEN` | `MEDIUM` | 2026-01-18 | — | — |
| `T104-RISK-003` | Tooling retrieval failures due to naming inconsistency | Case-sensitive and suffix-drift naming can break deterministic linking and agent retrieval, increasing hallucination/duplication risk | Client | `OPEN` | `MEDIUM` | 2026-01-18 | — | — |

---

## V. ARTIFACT UPDATES

| Artifact ID | Section | Action Required | Content Source |
| :--- | :--- | :--- | :--- |
| `workspace_documentation_rules.md` | Roles + heading semantics | Candidate alignment to T104 Roadmap/Notes/Proposal/Analysis/Changelog role boundaries and `###/####` semantics | See Topic 2.A, Topic 4.A |
| `template_workspace_notes.md` | PURPOSE + structure | Candidate alignment of NOTES semantics (session record vs decision log) and removal/rename of “LOG/Subphase” language if incompatible with T104 | See Topic 2.B, Topic 4.B |
| `sps_T104-CWS.md` | Governance snapshot placeholders | Ensure SSOT links to Roadmap/Notes/Research/Analysis without importing operational detail | See Topic 1.A, Topic 6.B |
| `concept_T104-CWS.md` | Candidate ADR placeholders | Candidate ADR topics: artifact role boundaries; changelog standard; heading semantics enforcement | See Topic 2.C, Topic 5.C |

---

## VI. SOURCE MATERIAL
*   **Brief Version**: `brief_T104-RES-001_agentic-workspace-assessment.md` v1.0.0 (2026-01-18)
*   **Code Commit/Tag**: `888fe41c4c8b106ff5a8e133a76fd94e971b146a`
*   **Files Cited**:
    *   `prompt/artifacts/tasks/T104/research/T104-RES-001/brief_T104-RES-001_agentic-workspace-assessment.md`
    *   `prompt/artifacts/tasks/T104/workspace/roadmap/plan_T104-CWS_phase0.md`
    *   `prompt/artifacts/tasks/T104/workspace/PH000/notes_T104-PH000.md`
    *   `prompt/artifacts/tasks/T104/workspace/roadmap/changelog_plan_T104-CWS_phase0.md`
    *   `prompt/artifacts/tasks/T104/T104A/workspace/PH000/ST000/notes_T104A-PH000-ST000.md`
    *   `prompt/templates/consultant/workspace/workspace_documentation_rules.md`
    *   `prompt/templates/consultant/workspace/template_workspace_roadmap.md`
    *   `prompt/templates/consultant/workspace/template_workspace_notes.md`
    *   `prompt/templates/consultant/workspace/template_workspace_proposal.md`
    *   `prompt/templates/consultant/workspace/template_workspace_analysis.md`
    *   `prompt/templates/researcher/template_research_report.md`
