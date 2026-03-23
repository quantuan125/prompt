---
artifact_type: 'IMPLEMENTATION'
implementation_type: 'task_specification'
initiative_id: 'T104'
initiative_code: 'CWS'
phase: '1'
stream_id: 'T104-PH001-ST008'
activity_id: 'T104-PH001-ST008-AC001.9'
task_id: 'T104-PH001-ST008-AC001.9-TK001 through TK014'
version: '1.0.0'
date: '2026-03-23'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.9/plan_T104-PH001-ST008-AC001.9.md'
execution_audience: 'developer'
purpose: 'Task specification for AC001.9: Recyclable Loop Artifact Governance — codifying DEV-REPORT package taxonomy, VERIFICATION multi-report intake, sub-consultant traceability audit protocol, and recyclable-loop evidence handoff contract across the workspace governance suite.'
consumers:
  - 'T104-PH001-ST008-AC001.9-GATE-001'
  - 'T104-PH001-ST008-AC001.9-GATE-002'
---

# IMPLEMENTATION (Task Specification): AC001.9 Recyclable Loop Artifact Governance

## I. PURPOSE & AUTHORITY

- **Purpose**: This artifact specifies the full task decomposition for AC001.9, covering both the consultation phase (through GATE-001) and the implementation phase (through GATE-002). It addresses four identified governance gaps in the workspace artifact suite that were exposed during AC001.6 multi-wave orchestrated execution.
- **Authority chain**: AC001.9 activity plan authorizes tracked work -> This artifact specifies the HOW for each task -> DEV-REPORT records execution evidence -> VERIFICATION provides reviewer verdict -> PROPOSAL hosts GDR.
- **Audience**: LLM_Consultant (TK001–TK004, TK013), LLM_Developer (TK005–TK011), LLM_Reviewer (TK012), Client (GATE-001, GATE-002).
- **Boundary**: This artifact does NOT hold a GDR. Gate decisions are recorded in the respective `gate_disposition` proposals per `guideline_workspace_proposal.md` §VII.

## II. TASK SCOPE

- **Governing plan task**: `T104-PH001-ST008-AC001.9-TK001` through `TK014` (full activity lifecycle)
- **Trigger**: AC001.6 GATE-002 disposition (GIR-003) explicitly deferred the DEV-REPORT supplementary-taxonomy item as future governance work. The AC001.6 orchestration plan (TK003.5, SPEC-005 governance note) flagged DEV-REPORT package semantics as a future remediation candidate. Consultation during the current session (2026-03-23) identified three additional gaps beyond the DEV-REPORT taxonomy: VERIFICATION multi-report intake, sub-consultant traceability audit, and recyclable-loop evidence handoff.
- **Deliverable contract**: Amended `guideline_workspace_dev-report.md`, `guideline_workspace_verification.md`, target guideline for traceability audit protocol, `workspace_documentation_rules.md` §7, and supporting template(s).

## III. ACTIVITY CONTEXT

### A. Identified Gaps (From Consultation)

| Gap ID | Gap Area | Target Surface | Evidence Source |
|:--|:--|:--|:--|
| GAP-001 | DEV-REPORT package taxonomy | `guideline_workspace_dev-report.md` | AC001.6 orchestration plan SPEC-005 governance note; AC001.6 GATE-002 GIR-003 |
| GAP-002 | VERIFICATION multi-report intake | `guideline_workspace_verification.md` | AC001.6 TK011 received four DEV-REPORT artifacts with no reviewer intake protocol |
| GAP-003 | Sub-consultant traceability audit | Target TBD (analysis or verification guideline) | AC001.6 TK003.5 delegated sub-consultant integrity work with no codified protocol |
| GAP-004 | Recyclable-loop evidence handoff | `workspace_documentation_rules.md` §7 | Multi-cycle recyclable loops (developer -> reviewer -> consultant) lack explicit handoff contract in the workflow chain |

### B. Gate Model

- **GATE-001** (Consultation-only): Analysis + findings + gate-disposition proposal -> client approval of scope
- **GATE-002** (Implementation-backed): Full Gate-Readiness Stack per `guideline_workspace_plan.md` §VI.L

### C. Cross-Initiative Interface

AC001.9 (T104) produces the **artifact-level authoring rules** that `T103-PH000-ST000-AC001` (orchestration execution patterns) will reference as its normative baseline. The two activities share a design interface but are independently executable. AC001.9's artifact rules define *what* artifacts are produced; T103-AC001's draft specification defines *how* the orchestrator dispatches agents to produce them.

---

## IV. SPECIFICATION ITEMS

### SPEC-001 — Create AC001.9 Activity Plan

| Field | Detail |
|:--|:--|
| Requirement Source | `guideline_workspace_plan.md` §IV; stream plan registration rules §IV.D |
| Primary Inputs | This implementation specification; T104-PH001-ST008 stream plan; `guideline_workspace_plan.md` |
| Output | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.9/plan_T104-PH001-ST008-AC001.9.md` |
| Acceptance Criteria | Activity plan exists at canonical path with full task register matching the task decomposition in this specification; AC001.9 is registered in the ST008 stream plan activity register with a contract stub per §IV.D |
| Owner | LLM_Consultant |
| Task ID | `T104-PH001-ST008-AC001.9-TK001` |
| Status | `open` |

#### Implementation Detail

1. Instantiate the activity plan template (`template_workspace_plan_activity.md`) for `T104-PH001-ST008-AC001.9`.
2. Populate the activity outline:
   - **Activity ID**: `T104-PH001-ST008-AC001.9`
   - **Name**: Recyclable Loop Artifact Governance
   - **Objective**: Codify DEV-REPORT package taxonomy, VERIFICATION multi-report intake protocol, sub-consultant traceability audit protocol, and recyclable-loop evidence handoff contract across the workspace governance suite.
   - **Execution Mode**: `GATED`
   - **Depends On**: `T104-PH001-ST008-AC001.6` (completed; provides the exemplar evidence and deferred GIR-003 item)
3. Populate the task register with the full task decomposition (TK001–TK014 + GATE-001 + GATE-002) as specified in this artifact's §V (Implementation Sequence).
4. Register AC001.9 in the ST008 stream plan (`plan_T104-PH001-ST008.md`):
   - Add a row to the Activity Register after AC001.8
   - Add a contract stub in the Activities (High-Level) section with Purpose, Deliverable, Scope, Activity Plan link, and Success Criteria Checklist (summary)
   - Bump the stream plan version
5. Context section of the activity plan should reference:
   - `prompt/templates/consultant/workspace/guideline_workspace_dev-report.md`
   - `prompt/templates/consultant/workspace/guideline_workspace_verification.md`
   - `prompt/templates/consultant/workspace/guideline_workspace_analysis.md`
   - `prompt/templates/consultant/workspace/workspace_documentation_rules.md`
   - `prompt/templates/consultant/workspace/guideline_workspace_plan.md`
   - `prompt/templates/consultant/workspace/guideline_workspace_implementation.md`
   - `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/implementation/implementation_T104-PH001-ST008-AC001.6_gate-001-to-gate-002-orchestration-plan.md`
   - `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/proposal/proposal_T104-PH001-ST008-AC001.6-GATE-002_gir-disposition-package.md`
   - This implementation specification

---

### SPEC-002 — Produce AC001.9 SES001 Session Notes

| Field | Detail |
|:--|:--|
| Requirement Source | `guideline_workspace_notes.md` §1.6, §5.1 (JIT registration), §6 |
| Primary Inputs | Consultation conversation context (2026-03-23); this implementation specification |
| Output | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.9/snotes/snotes_T104-PH001-ST008-AC001.9-SES001.md` |
| Acceptance Criteria | Session notes file exists at canonical path following `template_workspace_notes_session_activity.md`; captures the consultation decisions, discussion points, and actions from the 2026-03-23 session that established AC001.9 scope; registered in the ST008 stream notes register (JIT per §5.1) |
| Owner | LLM_Consultant |
| Task ID | `T104-PH001-ST008-AC001.9-TK001` (bundled with SPEC-001) |
| Status | `open` |

#### Implementation Detail

1. Create the session notes file using `template_workspace_notes_session_activity.md`.
2. Title: `ACTIVITY SESSION NOTES: T104 (CWS) — PH001 / ST008 / AC001.9 / SES001 (Recyclable Loop Artifact Governance — Scope Consultation)`
3. Capture the following from the consultation record:
   - **Agenda**: (a) Assessment of DEV-REPORT/VERIFICATION gaps for recyclable orchestration loops, (b) Initiative boundary decision (T104 vs T103), (c) AC001.9 scope definition, (d) T103-AC001 scope definition, (e) Gate model confirmation
   - **Discussion Points**:
     - DP001: Four governance gaps identified (DEV-REPORT package taxonomy, VERIFICATION multi-report intake, sub-consultant traceability audit, recyclable-loop evidence handoff)
     - DP002: Two-concern decomposition — artifact-level rules (T104 AC001.9) vs orchestration execution patterns (T103 AC001)
     - DP003: AC001.9 gate model — dual-gate (consultation-only GATE-001 + implementation-backed GATE-002)
     - DP004: T103-AC001 planning level — activity under ST000 with consultation-only single gate
   - **Decisions**:
     - DEC001: Approve two-concern decomposition (Concern A -> AC001.9 in T104, Concern B -> T103-AC001) — Status: `Confirmed`, Owner: Client
     - DEC002: AC001.9 picks up the GIR-003 deferral from AC001.6 GATE-002 — Status: `Confirmed`, Owner: Client
     - DEC003: AC001.9 uses dual-gate model (consultation-only GATE-001 + implementation-backed GATE-002) — Status: `Confirmed`, Owner: Client
     - DEC004: T103-AC001 at activity level under ST000 with consultation-only single gate; draft specification only, normative binding deferred to T103-PH001 — Status: `Confirmed`, Owner: Client
     - DEC005: Sub-consultant traceability/integrity examination codification belongs in AC001.9 (artifact-level rules) — Status: `Confirmed`, Owner: Client
     - DEC006: Analysis artifacts and session notes are specified as SPEC items within implementation specifications for assistant execution — Status: `Confirmed`, Owner: Client
   - **Actions**:
     - ACT001: Produce AC001.9 implementation specification (this artifact) — Owner: LLM_Consultant, Status: `completed`
     - ACT002: Produce T103-AC001 implementation specification — Owner: LLM_Consultant, Status: `completed`
     - ACT003: Execute AC001.9 plan creation (SPEC-001) — Owner: LLM_Consultant, Status: `pending`
     - ACT004: Execute T103-AC001 plan creation — Owner: LLM_Consultant, Status: `pending`
   - **Open Questions**: None remaining at session close
   - **Handoff**: Implementation specifications produced; assistant to execute SPEC items sequentially per §V
4. Register the session in the ST008 stream notes register per JIT rule (§5.1). If the stream notes register (`notes_T104-PH001-ST008.md`) exists, add a row. If it does not exist, create it using `template_workspace_notes_register_stream.md`.

---

### SPEC-003 — Produce Recyclable Loop Artifact Governance Gap Analysis

| Field | Detail |
|:--|:--|
| Requirement Source | `guideline_workspace_analysis.md` §III (`assessment` type), §V |
| Primary Inputs | AC001.6 orchestration plan; AC001.6 GATE-002 disposition; `guideline_workspace_dev-report.md`; `guideline_workspace_verification.md`; `workspace_documentation_rules.md`; raw session evidence from AC001.6 execution |
| Output | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.9/analysis/analysis_T104-PH001-ST008-AC001.9_recyclable-loop-artifact-governance-gaps.md` |
| Acceptance Criteria | Analysis artifact exists at canonical path following `template_workspace_analysis.md`; `analysis_type: 'assessment'`; contains GAP register with GAP-001 through GAP-004 (minimum); includes Assessment section (§V.B) with current state summary, options, and recommendations per gap; includes Downstream Actions section (§VIII) mapping each gap to a target surface, responsible role, and trigger condition |
| Owner | LLM_Consultant |
| Task ID | `T104-PH001-ST008-AC001.9-TK002` |
| Status | `open` |

#### Implementation Detail

1. Create the analysis artifact using `template_workspace_analysis.md`.
2. Frontmatter:
   - `artifact_type: 'ANALYSIS'`
   - `analysis_type: 'assessment'`
   - `initiative_id: 'T104'`
   - `initiative_code: 'CWS'`
   - `phase: '1'`
   - `stream_id: 'T104-PH001-ST008'`
   - `activity_id: 'T104-PH001-ST008-AC001.9'`
   - `task_id: 'T104-PH001-ST008-AC001.9-TK002'`
   - `plan_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.9/plan_T104-PH001-ST008-AC001.9.md'`
   - `purpose: 'Assessment of recyclable-loop artifact governance gaps across the workspace governance suite, identifying DEV-REPORT package taxonomy, VERIFICATION multi-report intake, sub-consultant traceability audit, and recyclable-loop evidence handoff deficiencies.'`
3. **Executive Summary**: Summarize the four governance gaps, their origin in AC001.6, and the recommended resolution approach. Include Client Summary subsection since this analysis feeds GATE-001.
4. **Scope & Inputs**:
   - In scope: DEV-REPORT multi-instance semantics, VERIFICATION reviewer intake protocol for wave DEV-REPORT stacks, sub-consultant post-loop integrity assessment protocol, recyclable-loop handoff contract in workflow chain
   - Out of scope: Orchestration execution patterns (T103-AC001), retroactive AC001.6 artifact rewriting, new artifact types
   - Inputs: List all guideline files, AC001.6 orchestration plan, AC001.6 GATE-002 disposition, AC001.6 wave DEV-REPORTs (as exemplars)
5. **Evidence / Methodology**: Guideline text review against AC001.6 execution evidence. For each gap, cite the specific guideline section that is silent or insufficient, and the specific AC001.6 artifact/execution pattern that exposed the gap.
6. **Findings / GAP Register**: Minimum four entries:

   | GAP ID | Category | Title | Description | Disposition | Downstream Target | Notes |
   |:--|:--|:--|:--|:--|:--|:--|
   | GAP-001 | workflow | DEV-REPORT package taxonomy | `guideline_workspace_dev-report.md` has no formal primary/supplementary/consolidated package model analogous to VERIFICATION §IV.A. AC001.6 invented a wave-DEV-REPORT + consolidated TK010 hybrid without guideline backing. | `pending_decision` | TK005 | Deferred from AC001.6 GATE-002 GIR-003 |
   | GAP-002 | workflow | VERIFICATION multi-report intake protocol | `guideline_workspace_verification.md` §V defines evidence rules for single DEV-REPORT intake. No protocol for reviewer navigation of a multi-report evidence set (e.g., four wave DEV-REPORTs + one consolidated). | `pending_decision` | TK006 | Exposed by AC001.6 TK011 |
   | GAP-003 | workflow | Sub-consultant traceability audit protocol | No guideline defines the trigger, schema, or evidence standard for a sub-consultant post-loop integrity assessment. AC001.6 delegated this informally to the sub-consultant with no codified contract. | `pending_decision` | TK007 | Exposed by AC001.6 TK003.5 orchestration |
   | GAP-004 | workflow | Recyclable-loop evidence handoff contract | `workspace_documentation_rules.md` §7 workflow chain defines single-pass handoff. Multi-cycle recyclable loops (developer -> reviewer -> consultant -> recycle) lack explicit handoff contract, evidence accumulation rules, and version-lineage tracking. | `pending_decision` | TK008 | Exposed by AC001.6 SPEC-005 multi-wave execution |

7. **Assessment section** (§V.B):
   - **Current State Summary**: For each gap, describe what the current guideline says (or doesn't say) and what AC001.6 did as a workaround.
   - **Options**: For each gap, present at least two options (e.g., extend existing section vs. create new section; add to analysis guideline vs. verification guideline for GAP-003).
   - **Recommendation**: State the consultant's recommended option per gap with rationale.
8. **Downstream Actions**: Map each gap to the implementation task that will resolve it (TK005–TK008 or equivalent).

---

### SPEC-004 — Produce GATE-001 Gate-Disposition Proposal

| Field | Detail |
|:--|:--|
| Requirement Source | `guideline_workspace_proposal.md` §V.B, §VII; `guideline_workspace_plan.md` §VI.L (consultation-only sequence) |
| Primary Inputs | TK002 analysis artifact; AC001.9 activity plan |
| Output | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.9/proposal/proposal_T104-PH001-ST008-AC001.9-GATE-001_gir-disposition-package.md` |
| Acceptance Criteria | Gate-disposition proposal exists at canonical path; contains GIR items for each identified gap (minimum four); consultant recommendation populated; GDR pending client decision |
| Owner | LLM_Consultant |
| Task ID | `T104-PH001-ST008-AC001.9-TK003` |
| Depends On | TK002 |
| Status | `open` |

#### Implementation Detail

1. Create the gate-disposition proposal using the established pattern (see AC001.6 GATE-001 proposal as exemplar).
2. Build the gate package index referencing the TK002 analysis artifact and the activity plan.
3. Create GIR items (minimum):
   - **GIR-001**: DEV-REPORT package taxonomy — approve the recommended approach from TK002 analysis
   - **GIR-002**: VERIFICATION multi-report intake protocol — approve the recommended approach
   - **GIR-003**: Sub-consultant traceability audit protocol — approve the recommended approach and target guideline
   - **GIR-004**: Recyclable-loop evidence handoff contract — approve the recommended approach
4. Populate the consultant recommendation as `APPROVE`.
5. Leave the GDR pending client decision.

---

### SPEC-005 — GATE-001: Client Approval of Recyclable Loop Governance Scope

| Field | Detail |
|:--|:--|
| Requirement Source | `guideline_workspace_plan.md` §VI |
| Primary Inputs | TK003 gate-disposition proposal |
| Output | Client decision recorded in the GDR |
| Acceptance Criteria | GDR in the GATE-001 proposal records client decision; if `APPROVE`, Phase 2 implementation tasks are unblocked |
| Owner | Client |
| Gate ID | `T104-PH001-ST008-AC001.9-GATE-001` |
| Status | `open` |

#### Implementation Detail

Consultation-only gate. No DEV-REPORT or VERIFICATION required. Client reviews the gate package and records a decision in the GDR.

---

### SPEC-006 — Produce Implementation Specification for Phase 2

| Field | Detail |
|:--|:--|
| Requirement Source | `guideline_workspace_implementation.md` §III.B (`task_specification`); GATE-001 approved scope |
| Primary Inputs | GATE-001 approved proposal; TK002 analysis artifact |
| Output | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.9/implementation/implementation_T104-PH001-ST008-AC001.9_phase-2-guideline-amendments.md` |
| Acceptance Criteria | Implementation specification exists with SPEC items mapping to each GATE-001-approved GIR; each SPEC item provides developer-executable detail for the target guideline surface amendment |
| Owner | LLM_Consultant |
| Task ID | `T104-PH001-ST008-AC001.9-TK004` |
| Depends On | GATE-001 |
| Status | `open` |

#### Implementation Detail

1. Create a new `task_specification` IMPLEMENTATION artifact.
2. Translate each GATE-001-approved GIR into a SPEC item with:
   - Target file path
   - Exact section to amend or create
   - Required content structure (section headings, table schemas, rule text)
   - Acceptance criteria with verifiable checks
3. Include vertical integration items where amendments in one guideline require cross-references or updates in others.

---

### SPEC-007 — Implement DEV-REPORT Package Taxonomy

| Field | Detail |
|:--|:--|
| Requirement Source | GATE-001 GIR-001; Phase 2 implementation specification SPEC item |
| Primary Inputs | Phase 2 implementation specification; `guideline_workspace_dev-report.md` (current v1.3.0) |
| Output | Amended `guideline_workspace_dev-report.md` |
| Acceptance Criteria | New section defining primary/supplementary/consolidated DEV-REPORT package semantics; frontmatter linking rules for package relationships; scope decomposition vs temporal iteration distinction (parallel to VERIFICATION §IV); changelog entry referencing AC001.9 |
| Owner | LLM_Developer |
| Task ID | `T104-PH001-ST008-AC001.9-TK005` |
| Depends On | TK004 |
| Status | `open` |

#### Implementation Detail

Per Phase 2 implementation specification. The developer should follow the SPEC item exactly. Key design elements to codify:
- **Primary DEV-REPORT**: The main consolidated handoff package for a gate
- **Supplementary DEV-REPORT** (wave reports): Bounded execution evidence for a specific implementation slice within a multi-wave execution
- **Consolidated DEV-REPORT**: Packages multiple supplementary reports into a single gate-handoff surface using `consolidated_from` frontmatter
- Naming convention for supplementary reports
- Frontmatter linking between primary and supplementary
- When to use supplementary vs single report (decision test)

---

### SPEC-008 — Implement VERIFICATION Multi-Report Intake Protocol

| Field | Detail |
|:--|:--|
| Requirement Source | GATE-001 GIR-002; Phase 2 implementation specification SPEC item |
| Primary Inputs | Phase 2 implementation specification; `guideline_workspace_verification.md` (current v1.10.0) |
| Output | Amended `guideline_workspace_verification.md` |
| Acceptance Criteria | New subsection defining reviewer intake protocol for multi-report evidence sets; specifies how the Evidence Set section (§V.B) should enumerate wave reports; specifies navigation order and cross-reference requirements; changelog entry referencing AC001.9 |
| Owner | LLM_Developer |
| Task ID | `T104-PH001-ST008-AC001.9-TK006` |
| Depends On | TK004 |
| Status | `open` |

#### Implementation Detail

Per Phase 2 implementation specification. Key design elements:
- Reviewer Evidence Set section must enumerate all wave DEV-REPORTs and the consolidated report
- Reviewer should verify consolidated report accurately represents wave content
- Per-task verification tables may reference wave report evidence directly
- Navigation protocol: consolidated report as primary entry point, wave reports as drill-down

---

### SPEC-009 — Implement Sub-Consultant Traceability Audit Protocol

| Field | Detail |
|:--|:--|
| Requirement Source | GATE-001 GIR-003; Phase 2 implementation specification SPEC item |
| Primary Inputs | Phase 2 implementation specification; target guideline (TBD at GATE-001: `guideline_workspace_analysis.md` or `guideline_workspace_verification.md` or `workspace_documentation_rules.md`) |
| Output | Amended target guideline |
| Acceptance Criteria | New trigger/schema defining when a sub-consultant traceability audit is required; what criteria the audit validates (evidence integrity, plan-authority compliance, role-boundary compliance, artifact-lineage completeness); what evidence schema the audit produces; how the audit feeds into the gate-disposition proposal; changelog entry referencing AC001.9 |
| Owner | LLM_Developer |
| Task ID | `T104-PH001-ST008-AC001.9-TK007` |
| Depends On | TK004 |
| Status | `open` |

#### Implementation Detail

Per Phase 2 implementation specification. The target guideline surface will be determined at GATE-001 based on the TK002 analysis recommendations. Key design elements:
- **Trigger**: When a recyclable loop (developer -> reviewer -> consultant) completes a cycle and the sub-consultant is dispatched for integrity validation before gate packaging
- **Criteria**: Evidence integrity (all expected artifacts exist and are consistent), plan-authority compliance (all tasks executed under proper plan authority), role-boundary compliance (no role performed work outside its ownership matrix), artifact-lineage completeness (version chains, consolidated_from links, handoff references are traceable)
- **Output**: Structured assessment that feeds the gate-disposition proposal's evidence index
- **Relationship to VERIFICATION**: This is NOT a replacement for reviewer verification. The traceability audit is a consultant-owned integrity layer that validates the process, while VERIFICATION validates the deliverables.

---

### SPEC-010 — Implement Recyclable-Loop Evidence Handoff Contract

| Field | Detail |
|:--|:--|
| Requirement Source | GATE-001 GIR-004; Phase 2 implementation specification SPEC item |
| Primary Inputs | Phase 2 implementation specification; `workspace_documentation_rules.md` (current v3.3.0) |
| Output | Amended `workspace_documentation_rules.md` §7 |
| Acceptance Criteria | §7 workflow chain explicitly addresses multi-cycle recyclable loops; defines evidence accumulation rules across cycles; defines version-lineage tracking for recycled artifacts; changelog entry referencing AC001.9 |
| Owner | LLM_Developer |
| Task ID | `T104-PH001-ST008-AC001.9-TK008` |
| Depends On | TK004 |
| Status | `open` |

#### Implementation Detail

Per Phase 2 implementation specification. Key design elements:
- Extend the implementation-backed workflow chain variant to explicitly show the recyclable loop: `... DEV-REPORT -> VERIFICATION -> [RECYCLE] -> IMPLEMENTATION remediation_specification -> remediation deliverables -> DEV-REPORT -> VERIFICATION -> ...`
- Define evidence accumulation: each cycle produces its own DEV-REPORT (supplementary); the final cycle produces the consolidated DEV-REPORT
- Define version-lineage: VERIFICATION artifacts version-bump per `guideline_workspace_verification.md` §IX; DEV-REPORT supplementary reports accumulate; consolidated report references all
- Define handoff contract at each boundary: developer -> reviewer (DEV-REPORT handoff), reviewer -> consultant (verification finding handoff), consultant -> developer (remediation specification handoff)

---

### SPEC-011 — Create/Update Templates for New Artifact Patterns

| Field | Detail |
|:--|:--|
| Requirement Source | Phase 2 implementation specification; `guideline_workspace_dev-report.md` template inventory |
| Primary Inputs | Phase 2 implementation specification; existing templates |
| Output | Updated `template_workspace_dev-report.md` and/or new template(s) as needed |
| Acceptance Criteria | Template(s) reflect the new package taxonomy and any new sections introduced by TK005–TK008; template inventory sections in affected guidelines are updated |
| Owner | LLM_Developer |
| Task ID | `T104-PH001-ST008-AC001.9-TK009` |
| Depends On | TK005, TK006, TK007, TK008 |
| Status | `open` |

#### Implementation Detail

Per Phase 2 implementation specification. Scope will depend on the extent of guideline amendments. At minimum:
- Update `template_workspace_dev-report.md` frontmatter to include `consolidated_from` and package-relationship keys if the DEV-REPORT package taxonomy introduces them
- If the sub-consultant traceability audit protocol defines a new artifact pattern, create a dedicated template or extend the analysis template
- Update template inventory sections in all amended guidelines

---

### SPEC-012 — Produce DEV-REPORT for GATE-002

| Field | Detail |
|:--|:--|
| Requirement Source | `guideline_workspace_dev-report.md`; `guideline_workspace_plan.md` §VI.L |
| Primary Inputs | Implementation evidence from TK005–TK009 |
| Output | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.9/dev-report/dev-report_T104-PH001-ST008-AC001.9_gate-002-handoff_<YYYY-MM-DD>.md` |
| Acceptance Criteria | DEV-REPORT exists with bounded execution evidence covering TK005–TK009; includes implementation log, validation evidence, traceability matrix, and handoff to reviewer |
| Owner | LLM_Developer |
| Task ID | `T104-PH001-ST008-AC001.9-TK010` |
| Depends On | TK009 |
| Status | `open` |

#### Implementation Detail

Standard DEV-REPORT per `guideline_workspace_dev-report.md`. Single consolidated report is sufficient for AC001.9 since the implementation tasks form one cohesive package (guideline amendments + template updates). If the scope is large enough to warrant wave reports, the developer may use the newly codified DEV-REPORT package taxonomy from TK005 — which would serve as a self-referential first exemplar.

---

### SPEC-013 — Produce GATE-002 Verification

| Field | Detail |
|:--|:--|
| Requirement Source | `guideline_workspace_verification.md`; `guideline_workspace_plan.md` §VI.L |
| Primary Inputs | TK010 DEV-REPORT; amended guideline/template artifacts |
| Output | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.9/verification/verification_T104-PH001-ST008-AC001.9_gate-002.md` |
| Acceptance Criteria | Verification artifact exists with independent evidence-first review of all amended surfaces; reviewer verdict recorded |
| Owner | LLM_Reviewer |
| Task ID | `T104-PH001-ST008-AC001.9-TK011` |
| Depends On | TK010 |
| Status | `open` |

#### Implementation Detail

Standard GATE-002 verification per `guideline_workspace_verification.md`. The reviewer should verify:
- Each amended guideline section is internally consistent
- Cross-references between amended guidelines are correct
- New DEV-REPORT package taxonomy is consistent with existing VERIFICATION package taxonomy
- Template updates match guideline amendments
- `workspace_documentation_rules.md` §7 workflow chain amendments are consistent with companion guideline changes

---

### SPEC-014 — Produce GATE-002 Gate-Disposition Proposal

| Field | Detail |
|:--|:--|
| Requirement Source | `guideline_workspace_proposal.md` §V.B, §VII; `guideline_workspace_plan.md` §VI.L |
| Primary Inputs | TK011 verification artifact; TK010 DEV-REPORT; GATE-001 approved scope |
| Output | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.9/proposal/proposal_T104-PH001-ST008-AC001.9-GATE-002_gir-disposition-package.md` |
| Acceptance Criteria | Gate-disposition proposal exists with GIR items covering implementation completeness and verification outcome; consultant recommendation populated; GDR pending client decision |
| Owner | LLM_Consultant |
| Task ID | `T104-PH001-ST008-AC001.9-TK012` |
| Depends On | TK011 |
| Status | `open` |

#### Implementation Detail

Standard implementation-backed gate-disposition proposal. Follow the AC001.6 GATE-002 proposal as exemplar.

---

### SPEC-015 — GATE-002: Client Acceptance of Implementation

| Field | Detail |
|:--|:--|
| Requirement Source | `guideline_workspace_plan.md` §VI |
| Primary Inputs | TK012 gate-disposition proposal |
| Output | Client decision recorded in the GDR |
| Acceptance Criteria | GDR records client decision; if `APPROVE`, AC001.9 is closed |
| Owner | Client |
| Gate ID | `T104-PH001-ST008-AC001.9-GATE-002` |
| Status | `open` |

#### Implementation Detail

Implementation-backed gate. Client reviews the full gate package (DEV-REPORT + verification + proposal) and records a decision in the GDR.

---

## V. IMPLEMENTATION SEQUENCE

```
Phase 1 — Consultation (GATE-001)
  SPEC-001  TK001   Create AC001.9 activity plan + register in ST008 stream plan
  SPEC-002  TK001   Produce SES001 session notes (bundled with SPEC-001)
  SPEC-003  TK002   Produce recyclable-loop artifact governance gap analysis
  SPEC-004  TK003   Produce GATE-001 gate-disposition proposal
  SPEC-005  GATE-001  Client approval of scope

Phase 2 — Implementation (GATE-002)
  SPEC-006  TK004   Produce Phase 2 implementation specification
  SPEC-007  TK005   Implement DEV-REPORT package taxonomy
  SPEC-008  TK006   Implement VERIFICATION multi-report intake protocol
  SPEC-009  TK007   Implement sub-consultant traceability audit protocol
  SPEC-010  TK008   Implement recyclable-loop evidence handoff contract
  SPEC-011  TK009   Create/update templates
  SPEC-012  TK010   Produce DEV-REPORT for GATE-002
  SPEC-013  TK011   Produce GATE-002 verification
  SPEC-014  TK012   Produce GATE-002 gate-disposition proposal
  SPEC-015  GATE-002  Client acceptance
```

**Dependency chain**: TK001 -> TK002 -> TK003 -> GATE-001 -> TK004 -> {TK005, TK006, TK007, TK008} (parallel) -> TK009 -> TK010 -> TK011 -> TK012 -> GATE-002

---

## VI. RISKS

| Risk ID | Description | Mitigation |
|:--|:--|:--|
| R-001 | Cross-initiative dependency — AC001.9 artifact rules form the normative baseline for T103-AC001 orchestration patterns. If AC001.9 changes artifact schemas, T103-AC001 draft spec may need revision. | AC001.9 executed first; T103-AC001 output is draft-only so revision cost is low. |
| R-002 | Template proliferation — AC001.9 may introduce new templates. Each template adds governance surface area. | TK002 analysis should evaluate whether existing templates can be extended vs. new ones created. Prefer extension. |
| R-003 | Sub-consultant traceability audit target guideline uncertainty — GAP-003 target surface is TBD. | Resolved at GATE-001 based on TK002 analysis recommendations. |

---

## VII. REFERENCES

| Document | Path |
|:--|:--|
| Governing plan (to be created) | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.9/plan_T104-PH001-ST008-AC001.9.md` |
| ST008 stream plan | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/plan_T104-PH001-ST008.md` |
| AC001.6 orchestration plan | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/implementation/implementation_T104-PH001-ST008-AC001.6_gate-001-to-gate-002-orchestration-plan.md` |
| AC001.6 GATE-002 disposition | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/proposal/proposal_T104-PH001-ST008-AC001.6-GATE-002_gir-disposition-package.md` |
| DEV-REPORT guideline | `prompt/templates/consultant/workspace/guideline_workspace_dev-report.md` |
| VERIFICATION guideline | `prompt/templates/consultant/workspace/guideline_workspace_verification.md` |
| ANALYSIS guideline | `prompt/templates/consultant/workspace/guideline_workspace_analysis.md` |
| Documentation rules | `prompt/templates/consultant/workspace/workspace_documentation_rules.md` |
| IMPLEMENTATION guideline | `prompt/templates/consultant/workspace/guideline_workspace_implementation.md` |
| Plan guideline | `prompt/templates/consultant/workspace/guideline_workspace_plan.md` |
| T103-AC001 implementation specification | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC001/implementation/implementation_T103-PH000-ST000-AC001_orchestration-execution-pattern-draft-spec.md` |

---

## VIII. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-03-23 | Initial | Task specification for AC001.9: Recyclable Loop Artifact Governance. Covers full activity lifecycle from consultation (GATE-001) through implementation (GATE-002). Four governance gaps identified: DEV-REPORT package taxonomy, VERIFICATION multi-report intake, sub-consultant traceability audit, recyclable-loop evidence handoff. Produced from SES001 consultation (2026-03-23). |
