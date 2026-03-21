---
artifact_type: 'IMPLEMENTATION'
implementation_type: 'task_specification'
initiative_id: 'T104'
initiative_code: 'CWS'
phase: '1'
stream_id: 'T104-PH001-ST008'
activity_id: 'T104-PH001-ST008-AC001.6'
task_id: 'T104-PH001-ST008-AC001.6-TK003.1'
version: '1.1.0'
date: '2026-03-21'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/plan_T104-PH001-ST008-AC001.6.md'
purpose: 'Detailed execution specification for AC001.6 supplementary consultant-owned tasks: comparative workflow assessment, recyclable prompt artifacts, plan/proposal amendments, and session notes'
execution_audience: 'consultant'
---

# IMPLEMENTATION (Task Specification): AC001.6 Supplementary Consultation Tasks

## I. PURPOSE & AUTHORITY

- **Purpose**: This artifact specifies the complete HOW for the supplementary consultant-owned tasks added to AC001.6 after the original TK001–TK003 sequence completed. These tasks address a client requirement for (a) a formal comparative assessment of the new IMPLEMENTATION workflow vs. the old `.claude/plans` workflow, (b) recyclable prompt artifacts for the IMPLEMENTATION authoring/execution pattern, and (c) corresponding plan and GATE-001 proposal amendments.
- **Authority chain**: Activity plan `T104-PH001-ST008-AC001.6` authorizes the work (TK003.1) → this artifact specifies HOW → session notes record execution evidence (execution_audience: consultant — no DEV-REPORT per guideline_workspace_dev-report.md §III.A).
- **Audience**: LLM_Developer (sub-agent execution), LLM_Consultant (orchestration)
- **This artifact does NOT hold a GDR.** Gate decisions are recorded in the GATE-001 gate-disposition proposal.
- **Trigger**: Client consultation (SES002) identified that the original TK001–TK003 sequence did not cover the comparative workflow assessment, recyclable prompt standardization, or the `.claude/plans` deprecation posture decision.

---

## II. TASK SCOPE

- **Governing plan task**: `T104-PH001-ST008-AC001.6-TK003.1` (to be added to plan via SPEC-005)
- **Trigger**: Client approved three recommendations during SES002 consultation: (1) split recyclable prompt into author/execute variants, (2) record comparative analysis as formal ANALYSIS artifact, (3) record deprecation posture as GIR-007 in GATE-001 proposal.
- **Deliverable contract**: See SPEC items below (6 deliverables)
- **Depends On**: TK003 (`completed`) — GATE-001 proposal exists and is amendable

---

## III. CONTEXT & RATIONALE

The original AC001.6 Phase 1 (TK001–TK003) delivered the vertical integration audit, standards-input proposal, and GATE-001 gate-disposition package. During the GATE-001 evaluation period, the client requested:

1. A formal comparative assessment between the new IMPLEMENTATION `task_specification` workflow and the old `.claude/plans` workflow, to validate that the IMPLEMENTATION family has accomplished its goal of replacing the ad-hoc plan pattern.
2. Recyclable prompt artifacts that standardize how consultants commission IMPLEMENTATION specs and how developers execute them.
3. A deprecation posture for `.claude/plans` in T104-governed activities, recorded as a GIR item in the GATE-001 proposal.

These are consultant-owned tasks that augment the GATE-001 evidence package without altering the Phase 2 developer scope.

---

## IV. SPECIFICATION ITEMS

### SPEC-001 — Author Comparative Analysis Artifact

| Field | Detail |
|:--|:--|
| Requirement Source | SES002-DEC004; SES002-DP002 |
| Template | `prompt/templates/consultant/workspace/template_workspace_analysis.md` |
| Output | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/analysis/analysis_T104-PH001-ST008-AC001.6_implementation-vs-claude-plans-comparative-assessment.md` |
| Implementation Detail | **Subtype**: `assessment` (interim — will be retroactively reclassified to `comparative_analysis` when AC001.7 delivers the new subtype). **Frontmatter**: `artifact_type: 'ANALYSIS'`, `analysis_type: 'assessment'`, `initiative_id: 'T104'`, `initiative_code: 'CWS'`, `phase: '1'`, `stream_id: 'T104-PH001-ST008'`, `activity_id: 'T104-PH001-ST008-AC001.6'`, `task_id: 'T104-PH001-ST008-AC001.6-TK003.1'`, `version: '1.0.0'`, `date: '2026-03-21'`, `status: 'draft'`, `author: 'LLM_Consultant'`, `decision_owner_role: 'Client'`, `plan_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/plan_T104-PH001-ST008-AC001.6.md'`, `purpose: 'Comparative assessment of IMPLEMENTATION task_specification workflow vs. legacy .claude/plans workflow for developer-execution precision'`. **§I Executive Summary**: State that the IMPLEMENTATION artifact family demonstrably outperforms the legacy `.claude/plans` pattern across 7 industry-standard criteria. Include Client Summary subsection (this feeds a gate). **§II Scope & Inputs**: In scope: structural comparison, developer-executability assessment, industry standard alignment. Out of scope: ANALYSIS taxonomy expansion (deferred to AC001.7). Inputs: `implementation_T104-PH001-ST008-AC001.6_vertical-integration-task-specification.md`, `.claude/plans/plan_T104-PH001-ST008-AC001.6_implementation-family-vertical-integration.md`, `guideline_workspace_implementation.md`. **§III Evidence/Methodology**: Side-by-side structural analysis across 8 dimensions (location, format, frontmatter, authority chain, traceability, conditional logic, acceptance criteria, requirement source). Developer-executability test against the "EXACTLY as outlined" recycle prompt pattern. Industry-standard mapping (IEEE 830, CMMI Level 3, TOGAF ADM, ISO 10007, Agile INVEST). **§IV Findings/GAP Register**: GAP-001 (workflow, `pending_decision`): The old `.claude/plans` pattern lacks governed traceability, per-item acceptance criteria, and formal authority chain. GAP-002 (lifecycle, `pending_decision`): No recyclable prompt exists for the IMPLEMENTATION execution workflow. GAP-003 (lifecycle, `pending_decision`): No deprecation posture decision exists for `.claude/plans` in governed work. **§V Assessment section**: Options Under Comparison: Option A (old `.claude/plans`), Option B (new IMPLEMENTATION `task_specification`). Evaluation Criteria (7 dimensions from the SES002 analysis): requirements traceability, acceptance criteria, authority chain, separation of concerns, change control, discoverability, authoring cost. Use the comparative matrix from the SES002 consultation as the core content. Recommendation: Option B wins on 5/7 criteria; Option A wins only on authoring cost and speed-to-first-draft. **§VIII Downstream Actions**: (1) `prompt_implementation-author.md` and `prompt_implementation-execute.md` creation → SPEC-002/003; (2) GATE-001 GIR-007 deprecation posture → SPEC-006. **Note**: Add a forward-reference note in the body: "This artifact uses `assessment` subtype as an interim classification. AC001.7 will introduce the `comparative_analysis` subtype, at which point this artifact's `analysis_type` will be reclassified." |
| Acceptance Criteria | ANALYSIS artifact exists at canonical path; uses `assessment` subtype with forward-reference note; covers all 7 evaluation criteria from SES002; Client Summary subsection present; GAP register populated |
| Status | `open` |

### SPEC-002 — Author Recyclable Prompt: Implementation Author

| Field | Detail |
|:--|:--|
| Requirement Source | SES002-DEC001 |
| Output | `prompt/templates/consultant/workspace/prompt/prompt_implementation-author.md` |
| Implementation Detail | Create the directory `prompt/templates/consultant/workspace/prompt/` if it does not exist. Author the prompt file with the client-provided recyclable prompt text (commissioning an IMPLEMENTATION `task_specification` artifact), incorporating the five improvements approved in SES002: (1) add `purpose` to frontmatter checklist, (2) add `Trigger` field mention for conditional SPEC items, (3) add Target Files Register (§V equivalent) mention, (4) explicit "Do NOT create a file in `.claude/plans/`" directive, (5) correct path template. The file should be authored as a standalone prompt that a consultant can copy-paste or reference when commissioning a `task_specification`. **Format**: Markdown file with `prompt_` prefix. No YAML frontmatter (this is a recyclable prompt, not a governed artifact). Include a brief header comment explaining the purpose and when to use this prompt. |
| Acceptance Criteria | File exists at canonical path; contains the full recyclable prompt text; includes all five approved improvements; directory `prompt/` exists |
| Status | `open` |

### SPEC-003 — Author Recyclable Prompt: Implementation Execute

| Field | Detail |
|:--|:--|
| Requirement Source | SES002-DEC001 |
| Output | `prompt/templates/consultant/workspace/prompt/prompt_implementation-execute.md` |
| Implementation Detail | Author the execution-variant recyclable prompt for commissioning a developer/assistant to execute an existing IMPLEMENTATION `task_specification`. Core directive: "Please perform the implementation as EXACTLY as outlined in this IMPLEMENTATION artifact at `<implementation_artifact_path>`. Read the artifact and all referenced context materials before beginning execution. Execute each SPEC-### item in the specified IMPLEMENTATION SEQUENCE order. For each SPEC item, verify the Acceptance Criteria before proceeding to the next. Record all changes in a DEV-REPORT artifact per `guideline_workspace_dev-report.md`." Include parameterized placeholders: `<implementation_artifact_path>`. Include a note that this prompt replaces the old `.claude/plans` recycle pattern for T104-governed activities. **Format**: Same as SPEC-002 — markdown with `prompt_` prefix, no YAML frontmatter, brief header comment. |
| Acceptance Criteria | File exists at canonical path; contains the full execution recyclable prompt; parameterized path placeholder present; DEV-REPORT instruction present |
| Status | `open` |

### SPEC-004 — Amend AC001.6 Activity Plan with TK003.1

| Field | Detail |
|:--|:--|
| Requirement Source | SES002-DP007 |
| Target | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/plan_T104-PH001-ST008-AC001.6.md` |
| Implementation Detail | **Task Register**: Insert `TK003.1` row between TK003 and GATE-001: `TK003.1 \| T104-PH001-ST008-AC001.6-TK003.1 \| Supplementary consultation tasks: comparative assessment, recyclable prompts, plan/proposal amendments \| completed \| LLM_Consultant \| TK003 \| analysis/, prompt/, plan, proposal \| guideline_workspace_analysis.md, guideline_workspace_implementation.md \| Comparative analysis authored, prompt artifacts created, plan amended, GATE-001 proposal amended with GIR-007`. **§III Tasks (Detailed)**: Add a new task section for TK003.1 with Purpose, Deliverable (6 items), Scope, Steps, Success Criteria. **§IV Links Register**: Add rows for the comparative analysis artifact and the two prompt files. **Version**: Bump to v1.1.0. **Changelog**: Record TK003.1 addition with source: SES002 consultation. |
| Acceptance Criteria | TK003.1 exists in task register; detailed task section exists; links register updated; version bumped to v1.1.0 |
| Status | `open` |

### SPEC-005 — Amend GATE-001 Proposal with GIR-007 and Updated Package Index

| Field | Detail |
|:--|:--|
| Requirement Source | SES002-DEC003 |
| Target | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/proposal/proposal_T104-PH001-ST008-AC001.6-GATE-001_gir-disposition-package.md` |
| Implementation Detail | **§2 Package Index**: Add row for the comparative analysis artifact: `Analysis \| AC001.6 IMPLEMENTATION vs .claude/plans Comparative Assessment \| prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/analysis/analysis_T104-PH001-ST008-AC001.6_implementation-vs-claude-plans-comparative-assessment.md`. Add row for supplementary implementation spec: `Implementation \| AC001.6 Supplementary Consultation Tasks Specification \| prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/implementation/implementation_T104-PH001-ST008-AC001.6_supplementary-consultation-tasks.md`. **§4 Gate Issues**: Add GIR-007 section: **Category**: Process. **Source**: SES002 comparative assessment. **Decision Request**: Approve the deprecation posture that `.claude/plans/` is deprecated for T104-governed activities where an IMPLEMENTATION artifact exists. It remains available for ad-hoc work outside governed initiatives. **If approved**: (a) `workspace_documentation_rules.md` §7.A gains a note stating the IMPLEMENTATION artifact is the canonical specification surface; (b) `guideline_workspace_implementation.md` §VII.A gains a note that `.claude/plans` is the legacy workaround superseded by IMPLEMENTATION artifacts for governed work. These two patches are added to Phase 2 scope. **Version**: Bump to v1.1.0. **Changelog**: Record GIR-007 addition and package index update. |
| Acceptance Criteria | GIR-007 exists in §4; package index includes comparative analysis and supplementary spec; version bumped to v1.1.0 |
| Status | `open` |

### SPEC-006 — Author Session Notes (SES002)

| Field | Detail |
|:--|:--|
| Requirement Source | `guideline_workspace_notes.md` — session documentation requirement |
| Template | Session notes template (snotes pattern per existing SES001) |
| Output | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/snotes/snotes_T104-PH001-ST008-AC001.6-SES002.md` |
| Implementation Detail | Record SES002 consultation covering: (a) Comparative assessment of IMPLEMENTATION vs `.claude/plans` workflow; (b) Recyclable prompt split approval (author + execute variants); (c) `comparative_analysis` subtype decision — new AC001.7 under ST008, not within AC001.6; (d) Deprecation posture for `.claude/plans`; (e) Implementation spec authoring for both AC001.6 supplementary and AC001.7. **Decision table**: DEC001 (prompt split approved), DEC002 (comparative_analysis subtype introduced via AC001.7), DEC003 (deprecation posture: `.claude/plans` deprecated for governed work), DEC004 (interim `assessment` subtype for comparative analysis with future reclassification). **Register**: Add SES002 row to ST008 notes register `notes_T104-PH001-ST008.md`. |
| Acceptance Criteria | SES002 notes exist at canonical path; all four decisions recorded; ST008 notes register updated |
| Status | `open` |

---

## V. IMPLEMENTATION SEQUENCE

```
SPEC-001  Author comparative analysis artifact
SPEC-002  Create prompt directory + author prompt_implementation-author.md
SPEC-003  Author prompt_implementation-execute.md
SPEC-004  Amend AC001.6 plan (add TK003.1)
SPEC-005  Amend GATE-001 proposal (GIR-007 + package index)
SPEC-006  Author SES002 session notes + register
```

**Parallelism note**: SPEC-001, SPEC-002, and SPEC-003 are independent and may execute in parallel. SPEC-004 depends on SPEC-001 completing (to reference the artifact path). SPEC-005 depends on SPEC-001 and SPEC-004. SPEC-006 depends on all prior specs completing.

---

## VI. TARGET FILES REGISTER

| # | File Path | Authority | Change Type | Confirmed? |
|:--|:--|:--|:--|:--|
| 1 | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/analysis/analysis_T104-PH001-ST008-AC001.6_implementation-vs-claude-plans-comparative-assessment.md` | T104 | Create | Yes |
| 2 | `prompt/templates/consultant/workspace/prompt/prompt_implementation-author.md` | T104 | Create | Yes |
| 3 | `prompt/templates/consultant/workspace/prompt/prompt_implementation-execute.md` | T104 | Create | Yes |
| 4 | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/plan_T104-PH001-ST008-AC001.6.md` | T104 | Amend (TK003.1 + links) | Yes |
| 5 | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/proposal/proposal_T104-PH001-ST008-AC001.6-GATE-001_gir-disposition-package.md` | T104 | Amend (GIR-007 + package index) | Yes |
| 6 | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/snotes/snotes_T104-PH001-ST008-AC001.6-SES002.md` | T104 | Create | Yes |
| 7 | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/notes_T104-PH001-ST008.md` | T104 | Amend (SES002 register row) | Yes |

---

## VII. REFERENCES

| Document | Path |
|:--|:--|
| Governing Plan | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/plan_T104-PH001-ST008-AC001.6.md` |
| GATE-001 Proposal | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/proposal/proposal_T104-PH001-ST008-AC001.6-GATE-001_gir-disposition-package.md` |
| SES001 Notes | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/snotes/snotes_T104-PH001-ST008-AC001.6-SES001.md` |
| Original Task Spec | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/implementation/implementation_T104-PH001-ST008-AC001.6_vertical-integration-task-specification.md` |
| Old Workflow (comparand) | `.claude/plans/plan_T104-PH001-ST008-AC001.6_implementation-family-vertical-integration.md` |
| Analysis Guideline | `prompt/templates/consultant/workspace/guideline_workspace_analysis.md` |
| Analysis Template | `prompt/templates/consultant/workspace/template_workspace_analysis.md` |
| Implementation Guideline | `prompt/templates/consultant/workspace/guideline_workspace_implementation.md` |

---

## VIII. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.1.0 | 2026-03-21 | Amendment | Remediated per SES003 QA: P-STD-005 compliant Requirement Source references; added execution_audience: 'consultant' frontmatter field. Source: T104-PH001-ST008-AC001.6-SES003. |
| v1.0.0 | 2026-03-21 | Initial | Task specification for AC001.6 supplementary consultant-owned tasks (TK003.1). Covers comparative analysis artifact, recyclable prompt pair, plan/proposal amendments, and session notes. Source: SES002 consultation decisions. |
