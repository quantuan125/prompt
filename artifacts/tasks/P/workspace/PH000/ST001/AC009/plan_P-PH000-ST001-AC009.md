---
artifact_type: 'PLAN'
planning_level: 'ACTIVITY'
initiative_id: 'P'
initiative_code: 'PROGRAM'
phase: '0'
stream_id: 'P-PH000-ST001'
activity_id: 'P-PH000-ST001-AC009'
version: '2.1.0'
date: '2026-03-26'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
governance_rules: 'prompt/templates/consultant/workspace/workspace_documentation_rules.md'
procedural_guideline: 'prompt/templates/consultant/workspace/guideline_workspace_plan.md'
parent_plan: 'prompt/artifacts/tasks/P/workspace/PH000/ST001/plan_P-PH000-ST001.md'
---

# PLAN: P (PROGRAM) — Phase 0 / Stream ST001 / Activity AC009: Harden P-STD-001 (Research-Backed Metadata & Structure Governance)

## I. EXECUTIVE SUMMARY

**Purpose**: Harden `P-STD-001` using the approved `P-RES-003` research package by adding normative metadata-governance rules for combined standard files, self-aligning `P-STD-001` to those rules, and updating all derivative authoring surfaces that must stay conformant under `P-STD-001-CLAUSE-005B`.

**Non-goals**:
- This activity does not perform the cross-standard retrofit for `P-STD-002`, `P-STD-004`, or `P-STD-005`; that work belongs to `P-PH000-ST001-AC010`.
- This activity does not reopen research execution or commission new research unless a narrow drafting dispute requires spot validation.
- This activity does not execute repo-wide reference sweeps outside the defined derivative and Tier 1 blast radius.

---

## II. ACTIVITY OUTLINE

**Activity ID**: `P-PH000-ST001-AC009`
**Objective**: Lock AC009 as implementation-ready through an internal readiness package and gate, then convert the approved `P-RES-003` findings into concrete `P-STD-001` governance rules and aligned derivative artifacts before client review and AC010 handoff.
**Execution Mode**: `SEQUENTIAL`
**Depends On**: `P-PH000-ST004-AC003-GATE-002`

**Context**:
- `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md`
- `prompt/templates/consultant/standards/guideline_standard_specs.md`
- `prompt/templates/consultant/standards/template_standard_specs.md`
- `prompt/AGENTS.md`
- `prompt/artifacts/tasks/P/ssot/sps_P-PROGRAM.md`
- `prompt/artifacts/tasks/P/workspace/PH000/ST004/AC003/analysis/analysis_P-PH000-ST004-AC003-TK003_content-sufficiency-assessment_P-RES-003.md`
- `prompt/artifacts/tasks/P/workspace/PH000/ST004/AC003/verification/verification_P-PH000-ST004-AC003_report-compliance-assessment_P-RES-003.md`
- `prompt/artifacts/tasks/P/workspace/PH000/ST004/AC003/proposal/proposal_P-PH000-ST004-AC003_gate-002_report-and-integration-disposition.md`
- `prompt/artifacts/tasks/P/workspace/PH000/ST004/AC003/analysis/analysis_P-PH000-ST004-AC003_external-review_gate-002-package.md`
- `prompt/artifacts/tasks/P/research/P-RES-003/report_P-RES-003_specification-metadata-governance-research.md`
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/analysis/analysis_P-PH000-ST001-AC009_external-review_gate-000-readiness-package.md`

### Task Register

| Task | Task ID | Name | Status | Owner | Depends On | Target | Reference | Action |
|:--|:--|:--|:--|:--|:--|:--|:--|:--|
| TK000 | `P-PH000-ST001-AC009-TK000` | Produce AC009 implementation-readiness package (assessment + gate-disposition proposal) | `completed` | LLM_Consultant | `P-PH000-ST004-AC003-GATE-002` | AC009 analysis + proposal package | Approved ST004 AC003 Gate-002 package | — |
| GATE-000 | `P-PH000-ST001-AC009-GATE-000` | Gate: Client accepts AC009 readiness package and unblocks drafting execution | `completed` | Client | TK000 | Pass/fail | `guideline_workspace_plan.md`, `guideline_workspace_proposal.md` | Client APPROVE (2026-03-15). GDR: `proposal_P-PH000-ST001-AC009-TK000_gate-000-readiness-disposition-package.md` v1.1.0. |
| TK001 | `P-PH000-ST001-AC009-TK001` | Ingest Gate-002 package and produce P-STD-001 amendment map | `completed` | LLM_Consultant | GATE-000 | Analysis artifact + drafting matrix | `P-RES-003` Gate-002 package | Amendment map authored at `analysis_P-PH000-ST001-AC009-TK001_p-std-001-amendment-map.md`. |
| TK002 | `P-PH000-ST001-AC009-TK002` | Draft metadata-governance amendments in `P-STD-001` | `completed` | LLM_Consultant | TK001 | `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md` | TK001 amendment map | Added metadata-governance clauses `031` through `036` and standardized the governing schema. |
| TK003 | `P-PH000-ST001-AC009-TK003` | Self-align `P-STD-001` to its new governance model | `completed` | LLM_Consultant | TK002 | `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md` | TK002 drafted CLAUSEs | Added frontmatter and normalized `References` / `Provenance` to the new model. |
| TK004 | `P-PH000-ST001-AC009-TK004` | Cascade derivative updates required by conformance coupling | `completed` | LLM_Consultant | TK003 | Guideline + template + AGENTS + SPS touchpoints | `P-STD-001-CLAUSE-005B` | Prompt-owned derivatives and `P-CON-003` aligned in the same changeset; see grouped dev-report. |
| TK005 | `P-PH000-ST001-AC009-TK005` | Produce verification and gate-readiness package | `completed` | LLM_Reviewer | TK004 | AC009 recycle / reassessment package | `guideline_workspace_verification.md` | Recycle loop completed; reassessment verification PASS (v1.1.0). |
| GATE-001 | `P-PH000-ST001-AC009-GATE-001` | Gate: Client acceptance of P-STD-001 metadata hardening package | `completed` | Client | TK005 | Pass/fail | `guideline_workspace_plan.md` §VI, `guideline_workspace_proposal.md` | Client APPROVE WITH CONDITIONS (2026-03-26). GDR: proposal v1.4.0. Conditions: (1) TK008 compliance remediation, (2) `TK009` through `TK013` plus `GATE-002` before AC010 handoff. |
| TK005.1 | `P-PH000-ST001-AC009-TK005.1` | Author Gate-001 remediation specification | `completed` | LLM_Consultant | GATE-001 | IMPLEMENTATION remediation spec | `guideline_workspace_implementation.md` | Create `implementation/implementation_P-PH000-ST001-AC009_gate-001-remediation-specification.md` and retire the temporary revision-checklist from live package use. |
| TK005.2 | `P-PH000-ST001-AC009-TK005.2` | Execute AC009 Gate-001 remediation changes | `completed` | LLM_Developer | TK005.1 | Remediated `P-STD-001` + derivative + package surfaces | TK005.1 remediation specification | Fix authority/reference/provenance/package gaps identified in the recycle loop. |
| TK005.3 | `P-PH000-ST001-AC009-TK005.3` | Produce recycle dev-report for the remediation pass | `completed` | LLM_Developer | TK005.2 | Recycle-pass dev-report | `guideline_workspace_dev-report.md` | Record remediation execution evidence for reviewer reassessment. |
| TK005.4 | `P-PH000-ST001-AC009-TK005.4` | Re-run Gate-001 verification after remediation | `completed` | LLM_Reviewer | TK005.3 | Refreshed Gate-001 verification artifact | `guideline_workspace_verification.md` | Reassess the same gate ID against the remediated package and implementation artifact. |
| TK005.5 | `P-PH000-ST001-AC009-TK005.5` | Refresh Gate-001 disposition proposal for re-presentation | `completed` | LLM_Consultant | TK005.4 | Updated Gate-001 proposal package | `guideline_workspace_proposal.md` | Replace temporary-handling language with IMPLEMENTATION-backed gate package language. |
| TK007 | `P-PH000-ST001-AC009-TK007` | Author Gate-001 compliance remediation spec + session notes (SES003) | `completed` | LLM_Consultant | GATE-001 | IMPLEMENTATION remediation spec + session notes | External review GAP-001 through GAP-005 | Authored SES003 session notes and the split-spec inputs later consolidated into the unified AC009 execution contract. |
| TK008 | `P-PH000-ST001-AC009-TK008` | Execute Gate-001 compliance remediation | `completed` | LLM_Consultant | TK007 | Updated proposal, AC009 plan, stream plan | `implementation_P-PH000-ST001-AC009_p-std-001-evolution-task-specification.md` | Normalized the live Gate-001 closeout package, removed stale `TK014` references from live authority surfaces, and locked the one-shot downstream package contract through `GATE-002`. |
| TK009 | `P-PH000-ST001-AC009-TK009` | Author P-STD-001 evolution task specification | `completed` | LLM_Consultant | GATE-001 | IMPLEMENTATION task spec | SES003 analysis findings | Authored `implementation_P-PH000-ST001-AC009_p-std-001-evolution-task-specification.md` as the unified execution contract for the remaining AC009 path. |
| TK010 | `P-PH000-ST001-AC009-TK010` | Execute P-STD-001 evolution amendments | `planned` | LLM_Developer | TK009 | Updated P-STD-001 + externalized changelog + updated guideline + template + AC010 plan | `implementation_P-PH000-ST001-AC009_p-std-001-evolution-task-specification.md` | — |
| TK011 | `P-PH000-ST001-AC009-TK011` | Dev-report for P-STD-001 evolution pass | `planned` | LLM_Developer | TK010 | DEV-REPORT | `guideline_workspace_dev-report.md` | — |
| TK012 | `P-PH000-ST001-AC009-TK012` | Verification for P-STD-001 evolution | `planned` | LLM_Reviewer | TK011 | VERIFICATION | `guideline_workspace_verification.md` | — |
| TK013 | `P-PH000-ST001-AC009-TK013` | Gate-002 disposition proposal | `planned` | LLM_Consultant | TK012 | PROPOSAL (gate_disposition) | `guideline_workspace_proposal.md` | — |
| GATE-002 | `P-PH000-ST001-AC009-GATE-002` | Gate: Client acceptance of P-STD-001 evolution amendments | `planned` | Client | TK013 | Pass/fail | `guideline_workspace_plan.md` §VI, `guideline_workspace_proposal.md` | — |
| TK006 | `P-PH000-ST001-AC009-TK006` | Prepare AC010 handoff and conformance boundary package | `planned` | LLM_Consultant | GATE-002 | AC010 handoff note / plan amendment inputs | Approved AC009 package | — |

---

## III. TASKS (DETAILED)

### Task TK000: Produce AC009 Implementation-Readiness Package

**Task ID**: `P-PH000-ST001-AC009-TK000`

**Purpose**: Convert this consultation into a formal AC009-local readiness package so downstream implementation begins from an approved, decision-complete execution contract rather than from implicit assumptions.

**Deliverables**:
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/analysis/analysis_P-PH000-ST001-AC009-TK000_activity-plan-readiness-assessment.md`
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/proposal/proposal_P-PH000-ST001-AC009-TK000_gate-000-readiness-disposition-package.md`

**Scope**:
- In scope:
  - Assess current AC009 plan readiness against the approved `P-RES-003` handoff package
  - Lock the execution boundary that `AC009` consumes `P-PH000-ST004-AC003-GATE-002` but does not mutate upstream ST004 / research artifacts
  - Lock derivative scope for this activity as `prompt-only`: `prompt/templates/consultant/standards/guideline_standard_specs.md`, `prompt/templates/consultant/standards/template_standard_specs.md`, `prompt/AGENTS.md`
  - Lock `prompt/artifacts/tasks/P/ssot/sps_P-PROGRAM.md` / `P-CON-003` clarification as an explicit AC009 target
  - Lock the `AC009` versus `AC010` scope boundary before drafting begins
- Out of scope:
  - Drafting or editing `P-STD-001`
  - Updating root `AGENTS.md`, `.claude/CLAUDE.md`, or role `CLAUDE_*` wrappers
  - Reopening `P-RES-003` report execution or editing ST004 gate artifacts

**Inputs Required**:
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/plan_P-PH000-ST001-AC009.md` - Current activity plan
- `prompt/artifacts/tasks/P/workspace/PH000/ST004/plan_P-PH000-ST004.md` - Upstream gate/source context
- `prompt/artifacts/tasks/P/workspace/PH000/ST004/AC003/proposal/proposal_P-PH000-ST004-AC003_gate-002_report-and-integration-disposition.md` - Authoritative upstream GDR
- `prompt/artifacts/tasks/P/workspace/PH000/ST004/AC003/analysis/analysis_P-PH000-ST004-AC003-TK003_content-sufficiency-assessment_P-RES-003.md` - Primary downstream intake surface
- `prompt/artifacts/tasks/P/workspace/PH000/ST004/AC003/analysis/analysis_P-PH000-ST004-AC003_external-review_gate-002-package.md` - Carry-forward enumeration surface
- `prompt/artifacts/tasks/P/research/P-RES-003/report_P-RES-003_specification-metadata-governance-research.md` - Evidence appendix

**Steps**:
1. Author the `assessment` analysis artifact capturing the current AC009 readiness gaps, accepted consultation decisions, and downstream actions needed to make AC009 implementation-ready.
2. Author the `gate_disposition` proposal that converts the assessment findings into client-facing GIR decisions for `GATE-000`.
3. Ensure the proposal's GDR is the authoritative unblocker for `TK001` through `TK006`.
4. Record the explicit execution defaults adopted in consultation:
   - `TK000` owns the readiness package
   - `P-PH000-ST004-AC003-GATE-002` is the full upstream dependency reference
   - `prompt-only` derivative instruction-surface scope applies to AC009
   - `P-CON-003` clarification remains in AC009 scope
   - upstream ST004 / `P-RES-003` artifacts are consumed, not edited

**Success Criteria**:
- [ ] AC009 readiness assessment exists at the canonical path
- [ ] AC009 `GATE-000` proposal exists at the canonical path
- [ ] The proposal GDR is the explicit downstream unblock rule for `TK001`
- [ ] All scope-boundary decisions required for implementation are locked in AC009-local artifacts

---

### GATE-000: Client Acceptance Of The AC009 Readiness Package

**Gate ID**: `P-PH000-ST001-AC009-GATE-000`

**Entry Criteria**:
- `TK000` complete
- AC009 readiness assessment and gate-disposition proposal both exist
- Proposal includes a populated `## Gate Decision Record` section for `P-PH000-ST001-AC009-GATE-000`

**Reviewer**: Client

**Exit Criteria**:
- Client records `APPROVE` or `APPROVE WITH CONDITIONS` in the proposal GDR
- `TK001` through `TK006` are unblocked to proceed under the approved readiness contract

---

### Task TK001: Ingest Gate-002 Package and Produce P-STD-001 Amendment Map

**Task ID**: `P-PH000-ST001-AC009-TK001`

**Purpose**: Convert the approved Gate-002 package into a drafting-ready amendment map so `P-STD-001` hardening begins from a controlled scope, not from raw report rereading.

**Deliverables**:
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/analysis/analysis_P-PH000-ST001-AC009-TK001_p-std-001-amendment-map.md`
- A drafting matrix mapping each adopted research finding to a target `P-STD-001` governance domain

**Scope**:
- In scope:
  - Intake of the approved report, synthesis analysis, verification verdict, and Gate-002 GDR from `P-PH000-ST004-AC003-GATE-002`
  - Explicit capture of low-severity verification carry-forwards
  - Explicit resolution of external review carry-forwards:
    - Verification FINDING-001 (template section deviation): Accept as brief-driven per OBS-003; record disposition
    - Verification FINDING-002 (ISSUE-004 staleness): Record in the amendment map whether the condition is administratively resolved; do not edit the upstream report artifact in AC009
    - Verification FINDING-003 (undocumented issue/risk transitions): Capture as drafting hygiene / traceability guidance for AC009-local work products; do not edit the upstream report artifact in AC009
    - Analysis GAP-001 through GAP-004: Incorporate into amendment map where they affect drafting scope
  - Explicit intake statement that AC009 consumes, but does not mutate, the approved ST004 / `P-RES-003` package
  - Resolution of the known research cautions from GAP-001 through GAP-004 where needed for drafting
  - Drafting boundary definition between `AC009` and `AC010`
- Out of scope:
  - Editing `P-STD-001`
  - Creating final clause text
  - Retrofitting other standards

**Inputs Required**:
- `prompt/artifacts/tasks/P/workspace/PH000/ST004/AC003/proposal/proposal_P-PH000-ST004-AC003_gate-002_report-and-integration-disposition.md` - Authoritative gate decision package
- `prompt/artifacts/tasks/P/workspace/PH000/ST004/AC003/analysis/analysis_P-PH000-ST004-AC003-TK003_content-sufficiency-assessment_P-RES-003.md` - Primary research synthesis and integration surface
- `prompt/artifacts/tasks/P/workspace/PH000/ST004/AC003/analysis/analysis_P-PH000-ST004-AC003_external-review_gate-002-package.md` - External review with enumerated carry-forward items and AC009 intake obligations
- `prompt/artifacts/tasks/P/workspace/PH000/ST004/AC003/verification/verification_P-PH000-ST004-AC003_report-compliance-assessment_P-RES-003.md` - Reviewer verdict and low-severity findings
- `prompt/artifacts/tasks/P/research/P-RES-003/report_P-RES-003_specification-metadata-governance-research.md` - Deep evidence appendix

**Steps**:
1. Read the approved Gate-002 package in dependency order: proposal, synthesis analysis, verification, then report.
2. Process the external review's GAP register (GAP-001 through GAP-005) and resolve or record each item in the amendment map:
   - GAP-001 (FINDING-001 template deviation): Record as accepted_as_is with OBS-003 justification
   - GAP-002 (FINDING-002 staleness): Record current administrative state for AC009 intake without editing ST004 artifacts
   - GAP-003 (FINDING-003 hygiene): Convert to AC009-local drafting / traceability guidance
   - GAP-004 (carry-forward specificity): Use the external review as the enumeration surface; confirm all items captured
   - GAP-005 (TK004 SPS registration): Confirm TK004 executed or flag if still pending
3. Produce an amendment map covering:
   - YAML/frontmatter governance
   - Version and amendment tracking
   - `## Provenance` taxonomy
   - `## References` taxonomy and table schema
   - Metadata authority/delineation rules
   - Agentic derivative governance boundary
3. Record every verification carry-forward item and every research caution that still matters to drafting.
4. Explicitly state which items become `AC010` retrofit work rather than `AC009` design work.
5. Summarize any narrow questions that must be revalidated before drafting continues.

**Success Criteria**:
- [ ] Amendment map exists at the canonical path
- [ ] Every adopted research domain is mapped to a concrete drafting target
- [ ] Verification carry-forward items are explicitly recorded
- [ ] All external review carry-forward items (GAP-001 through GAP-005) explicitly resolved or recorded
- [ ] `AC009` versus `AC010` boundary is explicit and enforceable

---

### Task TK002: Draft Metadata-Governance Amendments in `P-STD-001`

**Task ID**: `P-PH000-ST001-AC009-TK002`

**Purpose**: Author the new or amended `P-STD-001` normative content required to govern metadata structure for combined standard files and repo-owned derivatives.

**Deliverable**:
- Updated `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md`

**Scope**:
- In scope:
  - Draft CLAUSE-level governance for YAML/frontmatter
  - Draft CLAUSE-level governance for version and amendment tracking
  - Draft CLAUSE-level governance for `## Provenance`
  - Draft CLAUSE-level governance for `## References`
  - Draft authority and delineation rules between machine-readable and human-readable metadata
  - Draft bounded governance for agentic derivative surfaces where the research supports it
- Out of scope:
  - Retrofitting other standards to the new model
  - Non-metadata refactors unrelated to `P-RES-003`

**Inputs Required**:
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/analysis/analysis_P-PH000-ST001-AC009-TK001_p-std-001-amendment-map.md` - Drafting map and carry-forward items
- `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md` - Current governance surface
- `prompt/templates/consultant/standards/guideline_standard_specs.md` - Derivative alignment context
- `prompt/templates/consultant/standards/template_standard_specs.md` - Derivative alignment context

**Steps**:
1. Identify the exact `P-STD-001` sections, indexes, and clause ranges that need amendment or insertion.
2. Draft the metadata-governance model so it stays lightweight and traceable to the research findings.
3. Ensure each new rule clearly distinguishes:
   - current-state metadata,
   - historical/lineage metadata,
   - references metadata,
   - derivative/agentic authority metadata.
4. Preserve internal consistency with existing `P-STD-001` governance patterns, indexes, and decision-record structure.
5. Record traceability from each new governance area back to the amendment map and research package.

**Success Criteria**:
- [ ] `P-STD-001` contains the complete metadata-governance rule set approved by the amendment map
- [ ] Drafted rules remain within the research-supported scope
- [ ] Drafted rules are traceable to `P-RES-003` findings
- [ ] No `AC010` retrofit work is silently absorbed into `AC009`

---

### Task TK003: Self-Align `P-STD-001` to Its New Governance Model

**Task ID**: `P-PH000-ST001-AC009-TK003`

**Purpose**: Ensure the meta-standard follows the metadata rules it has just imposed on other combined standard files.

**Deliverable**:
- Self-aligned `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md`

**Scope**:
- In scope:
  - Add or normalize the file's own frontmatter
  - Restructure `## References` and `## Provenance` as required
  - Normalize version/amendment-history handling
  - Update affected indexes, cross-references, and internal traceability
- Out of scope:
  - Updating derivative files
  - Updating other standards

**Inputs Required**:
- Updated `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md` from TK002

**Steps**:
1. Compare the new governance rules to the current `P-STD-001` file state.
2. Apply the minimum structural and metadata changes required for self-conformance.
3. Verify that the file does not contradict its own new authority/delineation model.
4. Update indexes and provenance details where versioning or section structure changed.

**Success Criteria**:
- [ ] `P-STD-001` conforms to its own new metadata-governance rules
- [ ] Internal indexes and references remain coherent after self-alignment
- [ ] Self-alignment changes stay limited to the scope created by TK002

---

### Task TK004: Cascade Derivative Updates Required by Conformance Coupling

**Task ID**: `P-PH000-ST001-AC009-TK004`

**Purpose**: Apply the required derivative updates in the same changeset as the `P-STD-001` CLAUSE changes, per `P-STD-001-CLAUSE-005B`.

**Deliverables**:
- Updated `prompt/templates/consultant/standards/guideline_standard_specs.md`
- Updated `prompt/templates/consultant/standards/template_standard_specs.md`
- Updated `prompt/AGENTS.md`
- SPS/index touchpoint updates if required by the new `P-STD-001` structure

**Scope**:
- In scope:
  - Guideline updates traceable to new `P-STD-001` CLAUSEs
  - Template updates that encode the new structure
  - `prompt/AGENTS.md` updates needed to keep the prompt-repo authoring instructions current
  - Clarify `prompt/artifacts/tasks/P/ssot/sps_P-PROGRAM.md` `P-CON-003` so it points to the new `P-STD-001` schema and YAML-versus-Provenance authority rules
- Out of scope:
  - Repo-wide derivative sweeps outside the known blast radius
  - Root `AGENTS.md`, `.claude/CLAUDE.md`, and role `CLAUDE_*` wrappers (explicitly deferred from AC009)
  - Cross-standard conformance updates for `P-STD-002/004/005`

**Inputs Required**:
- Updated `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md` from TK003
- `prompt/templates/consultant/standards/guideline_standard_specs.md` - derivative authority surface
- `prompt/templates/consultant/standards/template_standard_specs.md` - derivative structure surface
- `prompt/AGENTS.md` - informative but expected prompt-repo directive surface
- `prompt/artifacts/tasks/P/ssot/sps_P-PROGRAM.md` - index/reference touchpoint

**Steps**:
1. Search for all derivative citations and guidance that rely on the amended `P-STD-001` CLAUSE set.
2. Update the guideline so every derivative rule remains traceable to governing CLAUSEs.
3. Update the template so the new metadata structure is baked into future authoring.
4. Update `prompt/AGENTS.md` where the authoring workflow or derivative references changed.
5. Amend `prompt/artifacts/tasks/P/ssot/sps_P-PROGRAM.md` `P-CON-003` so the YAML-frontmatter requirement points to the new `P-STD-001` schema and metadata authority split.
6. Record the deferred instruction-surface items for later work rather than silently omitting them from AC009 scope.

**Success Criteria**:
- [ ] Guideline and template are updated in the same changeset as `P-STD-001`
- [ ] Derivative guidance cites the correct governing CLAUSEs
- [ ] `prompt/AGENTS.md` remains consistent with the new prompt-repo authoring model
- [ ] `P-CON-003` is clarified to align with the new `P-STD-001` metadata model
- [ ] Deferred non-prompt instruction surfaces are explicitly recorded, not silently omitted

---

### Task TK005: Produce Verification and Gate-Readiness Package

**Task ID**: `P-PH000-ST001-AC009-TK005`

**Purpose**: Produce the reviewer-owned verification package needed to support client review of the completed hardening work.

**Deliverable**:
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/verification/verification_P-PH000-ST001-AC009_gate-001.md`

**Inputs Required**:
- Final `P-STD-001` output from TK004
- AC009 amendment-map analysis
- Relevant derivative files updated in TK004
- `prompt/templates/consultant/workspace/guideline_workspace_verification.md`

**Steps**:
1. Verify `P-STD-001` changes against the approved AC009 scope.
2. Verify self-conformance and derivative conformance-coupling completeness.
3. Verify the `AC009`/`AC010` boundary has been respected.
4. Produce the verification artifact and gate recommendation.

**Success Criteria**:
- [ ] Verification artifact exists at the canonical path
- [ ] Scope, self-conformance, and derivative-coupling checks are evidenced
- [ ] Gate-001 reviewer verdict is recorded

---

### GATE-001: Client Acceptance of the `P-STD-001` Metadata Hardening Package

**Entry Criteria**:
- Initial review complete and recycle loop formally opened
- `TK005.1` through `TK005.5` complete for the active reassessment cycle
- Refreshed verification artifact exists and records the current reviewer verdict
- Current proposal package exists and hosts the authoritative GDR for the same gate ID

**Reviewer**: Client

**Exit Criteria**:
- Client approves or approves with conditions the completed metadata-governance hardening package
- Approved package becomes the authority surface for `AC010`

**Gate-Disposition Proposal**: `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/proposal/proposal_P-PH000-ST001-AC009_gate-001_metadata-hardening-disposition.md`

**Gate Resolution Block**:
- **Gate Status**: `completed`
- **Decision**: Client APPROVE WITH CONDITIONS (2026-03-26)
- **GDR Reference**: `proposal_P-PH000-ST001-AC009_gate-001_metadata-hardening-disposition.md` v1.4.0
- **Conditions**: (1) Complete TK008 compliance remediation (five administrative GAPs). (2) Complete the P-STD-001 evolution cycle (`TK009` through `TK013` + `GATE-002`) before AC010 handoff.
- **Prior Recycle History**: Gate-001 was recycled for authority/reference/provenance defects. Remediation tasks `TK005.1` through `TK005.5` completed the remediation pass. Reassessment verification returned PASS (v1.1.0). The reassessment external review (v1.0.0, 2026-03-25) confirmed all five original GAPs substantively closed and recommended APPROVE WITH CONDITIONS for five new administrative compliance items.
- **Downstream**: `TK006` (AC010 handoff) remains blocked until `GATE-002` records an approving GDR.

---

### Task TK007: Author Gate-001 Compliance Remediation Spec + Session Notes (SES003)

**Task ID**: `P-PH000-ST001-AC009-TK007`

**Purpose**: Record the SES003 consultation findings (independent assessment of external review, downstream readiness, P-STD-001 QA) and author the compliance remediation implementation specification for the five administrative GAPs identified by the reassessment external review.

**Deliverables**:
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/snotes/snotes_P-PH000-ST001-AC009-SES003.md`
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/implementation/implementation_P-PH000-ST001-AC009_gate-001-compliance-remediation.md`
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/implementation/implementation_P-PH000-ST001-AC009_p-std-001-evolution-task-specification.md`

**Steps**:
1. Author session notes recording the SES003 consultation analysis and client decisions.
2. Author the compliance remediation specification (this file) with exact implementation detail for each GAP.
3. Author the P-STD-001 evolution task specification with exact implementation detail for CLAUSE-036G and derivative updates.

**Success Criteria**:
- [ ] Session notes exist at the canonical path
- [ ] Compliance remediation spec exists with REM items for all five GAPs
- [ ] P-STD-001 evolution task spec exists with SPEC items for CLAUSE amendment, changelog, and derivatives

---

### Task TK008: Execute Gate-001 Compliance Remediation

**Task ID**: `P-PH000-ST001-AC009-TK008`

**Purpose**: Execute the live Gate-001 closeout corrections defined in the updated remediation specification, normalize the downstream task/gate contract, and prepare a coherent package path through `TK010` to `TK013` and `GATE-002`.

**Deliverables**:
- Updated `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/proposal/proposal_P-PH000-ST001-AC009_gate-001_metadata-hardening-disposition.md` (v1.4.0)
- Updated `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/plan_P-PH000-ST001-AC009.md` (v2.1.0)
- Updated `prompt/artifacts/tasks/P/workspace/PH000/ST001/plan_P-PH000-ST001.md` (v0.1.22)

**Steps**:
Execute per the implementation specification at `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/implementation/implementation_P-PH000-ST001-AC009_p-std-001-evolution-task-specification.md`.

**Success Criteria**:
- [ ] Proposal `GDR` uses the corrected downstream condition chain (`TK009` through `TK013` + `GATE-002`)
- [ ] Plan task register reflects the live post-closeout state for `TK007`, `TK008`, and `TK009`
- [ ] Plan `GATE-001` section no longer references `TK014`
- [ ] Plan `TK008` success criteria no longer reference `TK014`
- [ ] Stream plan live changelog wording no longer references `TK014`
- [ ] No live AC009/ST001 closeout surface in this chain requires the implementer to infer a missing task ID

---

### Task TK009: Author P-STD-001 Evolution Task Specification

**Task ID**: `P-PH000-ST001-AC009-TK009`

**Purpose**: Author the task specification for the P-STD-001 evolution amendments (CLAUSE-036G changelog externalization, derivative updates, AC010 plan).

**Deliverable**:
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/implementation/implementation_P-PH000-ST001-AC009_p-std-001-evolution-task-specification.md`

**Steps**:
1. Author the task specification with SPEC items for all P-STD-001 amendments, externalized changelog creation, derivative updates, and AC010 plan creation.

**Success Criteria**:
- [ ] Task specification exists with SPEC items covering all target files

---

### Task TK010: Execute P-STD-001 Evolution Amendments

**Task ID**: `P-PH000-ST001-AC009-TK010`

**Purpose**: Execute the P-STD-001 CLAUSE-036G amendment, create the externalized changelog, update derivatives, and create the AC010 activity plan.

**Deliverables**:
- Updated `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md` (v1.2.0)
- New `prompt/artifacts/tasks/P/standard/changelog/changelog_standard_P-STD-001.md`
- Updated `prompt/templates/consultant/standards/guideline_standard_specs.md` (v6.2.0)
- Updated `prompt/templates/consultant/standards/template_standard_specs.md`
- New `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC010/plan_P-PH000-ST001-AC010.md`

**Steps**:
Execute per the implementation specification at `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/implementation/implementation_P-PH000-ST001-AC009_p-std-001-evolution-task-specification.md`.

**Success Criteria**:
- [ ] P-STD-001 contains CLAUSE-036G with externalized changelog option
- [ ] Externalized changelog file exists at the canonical path with full version history
- [ ] Inline Amendment History retains three most recent entries plus pointer
- [ ] Guideline §E updated with externalized changelog guidance
- [ ] Template Provenance section updated with externalized changelog comment
- [ ] AC010 activity plan exists at the canonical path

---

### Task TK011: Dev-Report for P-STD-001 Evolution Pass

**Task ID**: `P-PH000-ST001-AC009-TK011`

**Purpose**: Produce bounded execution evidence for the P-STD-001 evolution amendments.

**Deliverable**:
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/dev-report/dev-report_P-PH000-ST001-AC009_p-std-001-evolution.md`

**Steps**:
1. Record execution evidence per `guideline_workspace_dev-report.md`.

**Success Criteria**:
- [ ] Dev-report exists with traceability to TK009 task specification SPEC items

---

### Task TK012: Verification for P-STD-001 Evolution

**Task ID**: `P-PH000-ST001-AC009-TK012`

**Purpose**: Independent verification of the P-STD-001 evolution amendments against the task specification.

**Deliverable**:
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/verification/verification_P-PH000-ST001-AC009_gate-002.md`

**Steps**:
1. Verify per `guideline_workspace_verification.md`.

**Success Criteria**:
- [ ] Verification artifact exists with reviewer verdict

---

### Task TK013: Gate-002 Disposition Proposal

**Task ID**: `P-PH000-ST001-AC009-TK013`

**Purpose**: Author the gate-disposition proposal for GATE-002 client acceptance of the P-STD-001 evolution amendments.

**Deliverable**:
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/proposal/proposal_P-PH000-ST001-AC009_gate-002_p-std-001-evolution-disposition.md`

**Steps**:
1. Author per `guideline_workspace_proposal.md`.

**Success Criteria**:
- [ ] Gate-002 proposal exists with GDR section for client decision

---

### GATE-002: Client Acceptance of P-STD-001 Evolution Amendments

**Gate ID**: `P-PH000-ST001-AC009-GATE-002`

**Entry Criteria**:
- TK010 complete (P-STD-001 evolution amendments executed)
- TK011 complete (dev-report produced)
- TK012 complete (verification with reviewer verdict)
- TK013 complete (gate-disposition proposal with GDR)

**Reviewer**: Client

**Exit Criteria**:
- Client records `APPROVE` or `APPROVE WITH CONDITIONS` in the GATE-002 GDR
- Approved P-STD-001 (v1.2.0) becomes the final authority surface for AC010

**Gate-Disposition Proposal**: `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/proposal/proposal_P-PH000-ST001-AC009_gate-002_p-std-001-evolution-disposition.md`

### Task TK006: Prepare AC010 Handoff and Conformance Boundary Package

**Task ID**: `P-PH000-ST001-AC009-TK006`

**Purpose**: Freeze the design intent produced by AC009 and convert it into an explicit handoff surface for `AC010`, so the retrofit activity remains structure-only and does not reopen design decisions.

**Deliverable**:
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/analysis/analysis_P-PH000-ST001-AC009-TK006_ac010-handoff-boundary.md`

**Inputs Required**:
- Approved `P-STD-001` package from GATE-001
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/plan_P-PH000-ST001.md`

**Steps**:
1. List the exact metadata-governance requirements that `AC010` must retrofit into `P-STD-002`, `P-STD-004`, and `P-STD-005`.
2. Explicitly record what `AC010` must not reopen or redesign.
3. Capture any expected versioning or SPS follow-on work that the retrofit may trigger.

**Success Criteria**:
- [ ] AC010 handoff surface exists and is explicit
- [ ] Structural retrofit scope is separated from design-authoring scope
- [ ] No unresolved design decision is silently pushed into AC010

---

## IV. LINKS REGISTER

| Link Type | Target | Path |
|:--|:--|:--|
| External Review | GATE-000 Package Assessment | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/analysis/analysis_P-PH000-ST001-AC009_external-review_gate-000-readiness-package.md` |
| Plan (this file) | AC009 Activity Plan | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/plan_P-PH000-ST001-AC009.md` |
| Plan | ST001 Stream Plan | `prompt/artifacts/tasks/P/workspace/PH000/ST001/plan_P-PH000-ST001.md` |
| Readiness Analysis | AC009 TK000 Assessment | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/analysis/analysis_P-PH000-ST001-AC009-TK000_activity-plan-readiness-assessment.md` |
| Analysis | AC009 TK001 Amendment Map | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/analysis/analysis_P-PH000-ST001-AC009-TK001_p-std-001-amendment-map.md` |
| Readiness Proposal | AC009 GATE-000 Disposition | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/proposal/proposal_P-PH000-ST001-AC009-TK000_gate-000-readiness-disposition-package.md` |
| IMPLEMENTATION | Gate-001 Remediation Specification | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/implementation/implementation_P-PH000-ST001-AC009_gate-001-remediation-specification.md` |
| DEV-REPORT | TK001-TK004 Implementation | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/dev-report/dev-report_P-PH000-ST001-AC009_tk001-tk004-implementation_2026-03-16.md` |
| Session Notes | AC009 SES001 | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/snotes/snotes_P-PH000-ST001-AC009-SES001.md` |
| Upstream Proposal | AC003 Gate-002 Disposition | `prompt/artifacts/tasks/P/workspace/PH000/ST004/AC003/proposal/proposal_P-PH000-ST004-AC003_gate-002_report-and-integration-disposition.md` |
| Upstream Analysis | P-RES-003 Integration Package | `prompt/artifacts/tasks/P/workspace/PH000/ST004/AC003/analysis/analysis_P-PH000-ST004-AC003-TK003_content-sufficiency-assessment_P-RES-003.md` |
| Upstream Verification | Report Compliance Assessment | `prompt/artifacts/tasks/P/workspace/PH000/ST004/AC003/verification/verification_P-PH000-ST004-AC003_report-compliance-assessment_P-RES-003.md` |
| External Review | Gate-002 Package Assessment | `prompt/artifacts/tasks/P/workspace/PH000/ST004/AC003/analysis/analysis_P-PH000-ST004-AC003_external-review_gate-002-package.md` |
| Proposal | Gate-001 Recycle / Reassessment Package | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/proposal/proposal_P-PH000-ST001-AC009_gate-001_metadata-hardening-disposition.md` |
| Verification | Gate-001 Reviewer Verification | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/verification/verification_P-PH000-ST001-AC009_gate-001.md` |
| External Review | GATE-001 Reassessment Package Assessment | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/analysis/analysis_P-PH000-ST001-AC009_external-review_gate-001-reassessment-package.md` |
| Session Notes | AC009 SES003 | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/snotes/snotes_P-PH000-ST001-AC009-SES003.md` |
| IMPLEMENTATION | Gate-001 Compliance Remediation | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/implementation/implementation_P-PH000-ST001-AC009_gate-001-compliance-remediation.md` |
| IMPLEMENTATION | P-STD-001 Evolution Task Specification | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/implementation/implementation_P-PH000-ST001-AC009_p-std-001-evolution-task-specification.md` |
| DEV-REPORT | P-STD-001 Evolution | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/dev-report/dev-report_P-PH000-ST001-AC009_p-std-001-evolution.md` |
| Verification | Gate-002 Reviewer Verification | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/verification/verification_P-PH000-ST001-AC009_gate-002.md` |
| Proposal | Gate-002 P-STD-001 Evolution Disposition | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/proposal/proposal_P-PH000-ST001-AC009_gate-002_p-std-001-evolution-disposition.md` |
| Plan | AC010 Activity Plan | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC010/plan_P-PH000-ST001-AC010.md` |

---

## V. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v2.1.0 | 2026-03-26 | Correction | Closed the live Gate-001 closeout drift after the v2.0.0 structural amendment. Marked `TK007`, `TK008`, and `TK009` as completed to match the artifacts already authored, corrected stale `TK014` references in the live Gate-001 closeout path, and preserved `TK010` through `TK013` plus `GATE-002` as the remaining downstream stack before `TK006`. |
| v2.0.0 | 2026-03-26 | Gate decision + plan amendment | Recorded client APPROVE WITH CONDITIONS for `GATE-001` (2026-03-26). Updated `TK005` and `TK005.1` through `TK005.5` to `completed`. Registered `TK007` through `TK013` plus `GATE-002` for the P-STD-001 evolution cycle. Added `GATE-002` section (P-STD-001 evolution acceptance). Updated `TK006` dependency from `GATE-001` to `GATE-002`. Added `Gate-Disposition Proposal` field to the `GATE-001` construct (GAP-003). Updated Links Register with new artifact entries. Major version bump for structural task/gate additions. Evidence: SES003 consultation + reassessment external review v1.0.0. |
| v1.5.0 | 2026-03-20 | Recycle amendment | Converted `GATE-001` into an active recycle/reassessment loop. Marked `TK005` and `GATE-001` as `in_progress`, added `TK005.1` through `TK005.5` as formal remediation/reassessment subtasks, added the required Recycle Re-entry Block, and registered the new Gate-001 remediation specification artifact. |
| v1.4.0 | 2026-03-16 | Implementation | Marked `TK001` through `TK004` completed after AC009 metadata-governance execution. Added the TK001 amendment map and grouped TK001-TK004 dev-report to the Links Register. |
| v1.3.0 | 2026-03-15 | Gate closure | Updated task register: TK000 → `completed`, GATE-000 → `completed` with GDR reference. Added external review analysis to Context and Links Register. Evidence: GATE-000 GDR (proposal v1.1.0), external review v1.0.0. |
| v1.2.0 | 2026-03-15 | Readiness packaging | Added `TK000` + `GATE-000` for AC009 implementation readiness. Locked AC009 to consume `P-PH000-ST004-AC003-GATE-002` without mutating upstream research artifacts, narrowed derivative instruction-surface scope to prompt-owned surfaces, made `P-CON-003` clarification explicit in `TK004`, and added AC009-local readiness analysis/proposal/session-note artifacts. |
| v1.1.0 | 2026-03-13 | Amendment | Added external review analysis as formal TK001 input. Enhanced TK001 scope with explicit verification carry-forward items (FINDING-001/002/003) and analysis GAPs. Added carry-forward resolution step and success criterion. Evidence: Gate-002 external review (2026-03-13). |
| v1.0.0 | 2026-03-13 | Initial | Created the standalone AC009 activity plan to convert the approved `P-RES-003` package into `P-STD-001` metadata-governance hardening, derivative conformance updates, verification packaging, and AC010 handoff. |
