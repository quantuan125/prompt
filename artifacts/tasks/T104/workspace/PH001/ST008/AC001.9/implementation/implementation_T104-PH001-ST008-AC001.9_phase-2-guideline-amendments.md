---
artifact_type: 'IMPLEMENTATION'
implementation_type: 'task_specification'
initiative_id: 'T104'
initiative_code: 'CWS'
phase: '1'
stream_id: 'T104-PH001-ST008'
activity_id: 'T104-PH001-ST008-AC001.9'
task_id: 'T104-PH001-ST008-AC001.9-TK004'
version: '1.2.0'
date: '2026-03-25'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.9/plan_T104-PH001-ST008-AC001.9.md'
proposal_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.9/proposal/proposal_T104-PH001-ST008-AC001.9-GATE-001_gir-disposition-package.md'
execution_audience: 'developer'
purpose: 'Phase 2 task specification for AC001.9: exact guideline and template amendments for DEV-REPORT package taxonomy, VERIFICATION multi-report intake, sub-consultant traceability audit protocol, recyclable-loop evidence handoff rules, and the GATE-002 handoff package.'
---

# IMPLEMENTATION (Task Specification): AC001.9 Phase 2 Guideline Amendments

## I. PURPOSE & AUTHORITY

- **Purpose**: This artifact is the execution contract for AC001.9 Phase 2. It translates the client-approved `GATE-001` GIR package into exact file-level amendment instructions so the developer can implement the approved governance model without reopening scope or inventing additional design decisions.
- **Authority chain**: `GATE-001` approved GIR-001 through GIR-004 -> `TK004` authorizes the Phase 2 execution specification -> `TK005` through `TK010` execute and record evidence -> `TK011` verifies -> `TK012` packages the `GATE-002` decision surface.
- **Audience**: `LLM_Developer` is the primary execution owner for `TK005` through `TK010`. `LLM_Reviewer` consumes the `TK010` handoff during `TK011`. `LLM_Consultant` consumes the `TK010` and `TK011` outputs during `TK012`.
- **This artifact does NOT hold a GDR.** `GATE-002` decision authority remains exclusively in the `gate_disposition` proposal per `guideline_workspace_proposal.md`.
- **Boundary**: This artifact covers only the approved AC001.9 Phase 2 guideline/template package. It does not reopen `GATE-001`, does not alter the approved GIR decisions, and does not authorize unrelated governance refactors.

## II. TASK SCOPE

- **Governing plan task**: `T104-PH001-ST008-AC001.9-TK004`
- **Trigger**: `GATE-001` closed with `APPROVE` on 2026-03-24 and left `TK004` as the next consultant-owned boundary for converting the approved GIR package into a developer-executable amendment spec.
- **Deliverable contract**: Produce the exact guideline/template amendment package required to implement:
  - GIR-001 -> `prompt/templates/consultant/workspace/guideline_workspace_dev-report.md`
  - GIR-002 -> `prompt/templates/consultant/workspace/guideline_workspace_verification.md`
  - GIR-003 -> `prompt/templates/consultant/workspace/guideline_workspace_analysis.md`
  - GIR-004 -> `prompt/templates/consultant/workspace/workspace_documentation_rules.md`
  - Supporting template changes -> existing DEV-REPORT and VERIFICATION templates only
- **Phase 2 write scope**:
  - `prompt/templates/consultant/workspace/guideline_workspace_dev-report.md`
  - `prompt/templates/consultant/workspace/guideline_workspace_verification.md`
  - `prompt/templates/consultant/workspace/guideline_workspace_analysis.md`
  - `prompt/templates/consultant/workspace/workspace_documentation_rules.md`
  - `prompt/templates/consultant/workspace/changelog/changelog_guideline_workspace_dev-report.md`
  - `prompt/templates/consultant/workspace/changelog/changelog_guideline_workspace_verification.md`
  - `prompt/templates/consultant/workspace/changelog/changelog_guideline_workspace_analysis.md`
  - `prompt/templates/consultant/workspace/changelog/changelog_workspace_documentation_rules.md`
  - `prompt/templates/consultant/workspace/template_workspace_dev-report.md`
  - `prompt/templates/consultant/workspace/template_workspace_verification.md`
  - `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.9/dev-report/dev-report_T104-PH001-ST008-AC001.9_gate-002-handoff_<YYYY-MM-DD>.md`
  - `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.9/verification/verification_T104-PH001-ST008-AC001.9_gate-002.md`
  - `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.9/proposal/proposal_T104-PH001-ST008-AC001.9-GATE-002_gir-disposition-package.md`

## III. NON-NEGOTIABLE EXECUTION RULES

1. `TK005` through `TK010` MUST NOT start until the client/orchestrator explicitly approves this `TK004` artifact.
2. Do NOT modify any `GATE-001` artifact during Phase 2 execution. `GATE-001` is closed history.
3. Do NOT create a new artifact family, a new ANALYSIS type, or a new template path. Phase 2 MUST extend existing surfaces in place.
4. `GIR-003` is resolved in this artifact as an ANALYSIS-family implementation using the existing `analysis_type: 'compliance_audit'` subtype. Do NOT re-open the target-surface decision.
5. Do NOT change `workspace_documentation_rules.md` Section 6 role-boundary rules or Section 8 ownership matrix as part of `TK008`. `TK008` is limited to recyclable-loop evidence and handoff governance.
6. New normative rule text in guideline surfaces MUST use BCP 14 primary vocabulary (`MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, `MAY`) where normative statements are introduced or rewritten.
7. If any target file contains structure that prevents exact implementation of the steps below, stop and escalate. Do not improvise an alternate design.

## IV. SPECIFICATION ITEMS

### SPEC-001 — Implement DEV-REPORT Package Taxonomy (`TK005`)

| Field | Detail |
|:--|:--|
| Requirement Source | `GATE-001` GIR-001; approved `TK004` execution specification |
| Primary Inputs | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.9/proposal/proposal_T104-PH001-ST008-AC001.9-GATE-001_gir-disposition-package.md`; `prompt/templates/consultant/workspace/guideline_workspace_dev-report.md`; `prompt/templates/consultant/workspace/template_workspace_dev-report.md`; `prompt/templates/consultant/workspace/guideline_workspace_verification.md` |
| Write Scope | `prompt/templates/consultant/workspace/guideline_workspace_dev-report.md`; `prompt/templates/consultant/workspace/changelog/changelog_guideline_workspace_dev-report.md` |
| Output | Amended `guideline_workspace_dev-report.md` and dedicated changelog entry |
| Acceptance Criteria | The DEV-REPORT guideline defines an explicit primary/supplementary/consolidated package model, differentiates scope decomposition from temporal iteration, adds the package-linkage frontmatter contract, and adds the required cross-role linkage rules without creating a new template or artifact family. |
| Status | `open` |

#### Implementation Detail

1. In `guideline_workspace_dev-report.md`, inside `## III. TRIGGER & LIFECYCLE`, insert a new subsection immediately after the existing `### C. Consolidated / retroactive reports` with the exact heading:
   - `### D. DEV-REPORT Package Taxonomy (Scope Decomposition)`
2. In that new subsection, define exactly these four postures:
   - **Single-report posture**: one DEV-REPORT covers the full bounded execution slice and hands directly to review or gate packaging.
   - **Primary DEV-REPORT**: the single gate-facing producer-evidence surface for a multi-report package.
   - **Supplementary DEV-REPORT**: a bounded subordinate producer-evidence report for one implementation wave, slice, or recycle-cycle execution segment.
   - **Consolidated DEV-REPORT**: a primary DEV-REPORT that aggregates and links multiple supplementary DEV-REPORTs through frontmatter and body-level traceability.
3. The new subsection MUST include a decision table with the exact columns:
   - `| Posture | When To Use | Required Frontmatter Posture | Review / Gate Entry Point |`
4. Populate that table with exactly four rows:
   - `Single-report posture`
   - `Primary DEV-REPORT`
   - `Supplementary DEV-REPORT`
   - `Consolidated DEV-REPORT`
5. Add normative rules in `### D. DEV-REPORT Package Taxonomy (Scope Decomposition)` stating all of the following:
   - A multi-report DEV-REPORT package MUST contain exactly one primary DEV-REPORT.
   - Each supplementary DEV-REPORT MUST set `package_role: 'supplementary'`.
   - Each supplementary DEV-REPORT MUST set `primary_report` to the repo-relative path of its governing primary DEV-REPORT.
   - A primary DEV-REPORT in a multi-report package MUST set `package_role: 'primary'`.
   - A consolidated DEV-REPORT is a primary DEV-REPORT and MUST populate `consolidated_from` with every supplementary DEV-REPORT included in the package.
   - A single-report posture MUST NOT populate `primary_report`; it MAY omit `consolidated_from`; if `package_role` is present it MUST be `primary`.
6. Immediately after the new `### D`, insert a new subsection with the exact heading:
   - `### E. Scope Decomposition vs Temporal Iteration`
7. In `### E. Scope Decomposition vs Temporal Iteration`, include a decision table with the exact columns:
   - `| Question | If Yes | If No |`
8. That subsection MUST distinguish:
   - **Scope decomposition** -> create supplementary DEV-REPORTs beneath one primary report.
   - **Temporal correction of the same report scope** -> version-bump the existing report rather than creating a new supplementary report.
9. Renumber the current `### D. Relationship to plan and gates` subsection to:
   - `### F. Relationship to plan and gates`
10. In `## IV. FRONTMATTER CONVENTIONS`:
   - Add `package_role` under `### B. Common recommended keys`.
   - Add `primary_report` under `### C. Bounded optional keys`.
   - Update the `consolidated_from` bullet so it is explicitly scoped to a primary DEV-REPORT that consolidates supplementary reports or closes out a retroactive bounded slice.
11. Add normative frontmatter rules stating:
   - `package_role` allowed values are exactly `primary` and `supplementary`.
   - `primary_report` is permitted only on supplementary DEV-REPORTs.
   - `consolidated_from` is permitted only on primary DEV-REPORTs.
12. In `## VIII. TRACEABILITY, HANDOFF, & BOUNDARIES`, insert a new subsection after `### D. Notes / raw boundary` with the exact heading:
   - `### E. Multi-report package linkage`
13. In that new subsection, add exact linkage rules:
   - Supplementary DEV-REPORTs MUST link upward to the primary DEV-REPORT through `primary_report`.
   - Primary consolidated DEV-REPORTs MUST link downward to every supplementary DEV-REPORT through `consolidated_from`.
   - Verification and proposal surfaces SHOULD cite the primary DEV-REPORT first and use supplementary DEV-REPORTs as drill-down evidence. (Note: this SHOULD is intentional as a general DEV-REPORT guidance posture; the VERIFICATION guideline independently mandates the ordering for reviewer-owned Evidence Set sections via SPEC-002.)
14. Do not create or reference a new template in this task. Template changes belong only to `TK009`.
15. Add a changelog entry for AC001.9 describing the package taxonomy delivery.
16. The changelog row for this task MUST be written to:
   - `prompt/templates/consultant/workspace/changelog/changelog_guideline_workspace_dev-report.md`
   It MUST NOT be written into the pointer-only `## X. CHANGELOG` section in the main guideline file.

### SPEC-002 — Implement VERIFICATION Multi-Report DEV-REPORT Intake (`TK006`)

| Field | Detail |
|:--|:--|
| Requirement Source | `GATE-001` GIR-002; approved `TK004` execution specification |
| Primary Inputs | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.9/proposal/proposal_T104-PH001-ST008-AC001.9-GATE-001_gir-disposition-package.md`; `prompt/templates/consultant/workspace/guideline_workspace_verification.md`; `prompt/templates/consultant/workspace/guideline_workspace_dev-report.md`; `prompt/templates/consultant/workspace/template_workspace_verification.md` |
| Write Scope | `prompt/templates/consultant/workspace/guideline_workspace_verification.md`; `prompt/templates/consultant/workspace/changelog/changelog_guideline_workspace_verification.md` |
| Output | Amended `guideline_workspace_verification.md` and dedicated changelog entry |
| Acceptance Criteria | The VERIFICATION guideline explicitly governs how reviewers enumerate, sequence, and compare multi-report DEV-REPORT packages and makes the producer-package vs reviewer-package distinction explicit. |
| Status | `open` |

#### Implementation Detail

**Vocabulary note**: This SPEC item references DEV-REPORT package taxonomy terms (`primary DEV-REPORT`, `supplementary DEV-REPORT`, `consolidated_from`, `package_role`, `primary_report`) whose canonical definitions are established in SPEC-001. Implementers MUST use SPEC-001's exact terminology when authoring VERIFICATION-side rules that reference producer-package semantics.

1. In `guideline_workspace_verification.md`, append one paragraph to `### A. Verification Package (Scope Decomposition)` clarifying that:
   - VERIFICATION package decomposition is reviewer-side scope decomposition.
   - DEV-REPORT package decomposition (as defined by the DEV-REPORT package taxonomy in `guideline_workspace_dev-report.md`) is producer-side evidence packaging.
   - The two decompositions are independent and MUST NOT be conflated.
2. In `## V. EVIDENCE RULES`, insert a new subsection immediately after `### B. Evidence Set Section` with the exact heading:
   - `### C. Multi-Report DEV-REPORT Intake`
3. Renumber the current `### C. Per-Task Verification Tables` subsection to:
   - `### D. Per-Task Verification Tables`
4. In the new `### C. Multi-Report DEV-REPORT Intake`, add a mandatory reviewer intake sequence as a numbered list with exactly these steps:
   1. Read the primary DEV-REPORT first.
   2. Confirm whether the primary report is a consolidated package by checking `consolidated_from`.
   3. Enumerate every supplementary DEV-REPORT referenced by the package.
   4. Read each supplementary DEV-REPORT in the execution order implied by the package or implementation history.
   5. Compare the primary DEV-REPORT Executive Summary, Traceability Matrix, and Handoff sections against the supplementary evidence set.
   6. Record any mismatch, omission, or broken package linkage as a finding or observation.
5. Add exact rules in `### C. Multi-Report DEV-REPORT Intake` stating:
   - The Evidence Set section MUST list the primary DEV-REPORT before any supplementary DEV-REPORTs.
   - When a primary DEV-REPORT declares `consolidated_from`, the reviewer MUST verify that every referenced supplementary DEV-REPORT exists and is represented accurately in the primary report.
   - The reviewer MUST NOT treat a consolidated DEV-REPORT as sufficient evidence if package completeness has not been checked.
   - `Observed Evidence` entries MAY cite either the primary DEV-REPORT or a supplementary DEV-REPORT, but each citation MUST identify the specific artifact path and evidence location.
6. In `### B. Evidence Set Section`, add one bullet requiring grouped enumeration for multi-report packages using the order:
   - primary DEV-REPORT
   - supplementary DEV-REPORTs
   - other task deliverables
   - governance references
7. In the renumbered `### D. Per-Task Verification Tables`, add one sentence clarifying that a single checklist group MAY cite both a primary and one or more supplementary DEV-REPORTs when verifying consolidated package accuracy.
8. Do not add new frontmatter keys to the VERIFICATION guideline.
9. Add a changelog entry for AC001.9 describing the multi-report intake protocol.
10. The changelog row for this task MUST be written to:
   - `prompt/templates/consultant/workspace/changelog/changelog_guideline_workspace_verification.md`
   It MUST NOT be written into the pointer-only `## XIII. CHANGELOG` section in the main guideline file.

### SPEC-003 — Implement Sub-Consultant Traceability Audit Protocol in ANALYSIS (`TK007`)

| Field | Detail |
|:--|:--|
| Requirement Source | `GATE-001` GIR-003; approved `TK004` execution specification |
| Primary Inputs | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.9/proposal/proposal_T104-PH001-ST008-AC001.9-GATE-001_gir-disposition-package.md`; `prompt/templates/consultant/workspace/guideline_workspace_analysis.md`; `prompt/templates/consultant/workspace/template_workspace_analysis.md`; `prompt/templates/consultant/workspace/workspace_documentation_rules.md` |
| Write Scope | `prompt/templates/consultant/workspace/guideline_workspace_analysis.md`; `prompt/templates/consultant/workspace/changelog/changelog_guideline_workspace_analysis.md` |
| Output | Amended `guideline_workspace_analysis.md` and dedicated changelog entry |
| Acceptance Criteria | The ANALYSIS guideline explicitly routes recyclable-loop sub-consultant traceability audits to an existing analysis subtype, defines the trigger, required evidence set, required checklist criteria, and the downstream handoff posture into proposal packaging or remediation. |
| Status | `open` |

#### Implementation Detail

1. Implement GIR-003 in the ANALYSIS family using the existing `analysis_type: 'compliance_audit'` subtype. Do NOT add a new `analysis_type` enum value.
2. In `guideline_workspace_analysis.md`, in `## IV. LIFECYCLE POSITIONS`, add one sentence immediately after the non-research analysis-types table stating exactly:
   - Recyclable-loop sub-consultant traceability audits SHALL be authored as `analysis_type: 'compliance_audit'`.
3. In `## V. REQUIRED STRUCTURE`, insert a new subsection after `### E. Downstream Actions (DEC013)` with the exact heading:
   - `### F. Recyclable-Loop Traceability Audit Profile`
4. In that new subsection, define the audit trigger exactly as:
   - when a recyclable loop has completed a developer -> reviewer -> consultant cycle and a consultant-owned integrity check is required before gate packaging or before consultant recommendation synthesis.
5. In that new subsection, state that the minimum required evidence inputs are:
   - governing plan
   - governing IMPLEMENTATION artifact when one exists
   - active DEV-REPORT package
   - active VERIFICATION artifact when one exists
   - target proposal path or gate package reference when packaging is imminent
6. In that new subsection, require that the compliance checklist in the resulting audit artifact contain exactly these minimum criterion rows:
   - `Evidence integrity`
   - `Plan-authority compliance`
   - `Role-boundary compliance`
   - `Artifact-lineage completeness`
7. For each required criterion row, define what must be checked:
   - `Evidence integrity` -> all expected artifacts exist, cross-links resolve, and package references are internally consistent.
   - `Plan-authority compliance` -> every executed deliverable can be traced to an authorized plan task and, when applicable, to an IMPLEMENTATION SPEC item.
   - `Role-boundary compliance` -> no role produced an artifact outside its governed ownership boundary for the assessed cycle.
   - `Artifact-lineage completeness` -> version chains, package-linkage keys, handoff references, and gate-facing evidence trails are complete and navigable.
8. In `## VI. FRONTMATTER CONVENTIONS`, under `### C. Type-specific optional keys (examples)`, extend the `compliance_audit` bullet to include:
   - `audit_cycle`
   - `primary_dev_report`
   - `verification_reference`
   - `proposal_target`
9. In the new `### F. Recyclable-Loop Traceability Audit Profile`, add downstream handoff rules:
   - If the audit finds no governance gap, the Downstream Actions section SHOULD point to proposal packaging or gate evidence indexing.
   - If the audit finds a governance gap requiring execution work, the Downstream Actions section SHOULD point to a plan amendment or IMPLEMENTATION artifact rather than inventing verification findings.
   - The resulting ANALYSIS artifact MUST NOT claim gate closure and MUST NOT replace reviewer-owned VERIFICATION.
10. In `## VIII. TEMPLATE INVENTORY`, add one sentence clarifying that no new template is introduced and the existing ANALYSIS template's `COMPLIANCE_AUDIT` block remains the required surface for this audit profile.
11. Do not change the universal GAP register semantics. If a traceability audit has no gaps, the GAP register may be empty or explicitly record no gaps; it MUST NOT emit verification-style findings.
12. Add a changelog entry for AC001.9 describing the recyclable-loop traceability-audit profile.
13. The changelog row for this task MUST be written to:
   - `prompt/templates/consultant/workspace/changelog/changelog_guideline_workspace_analysis.md`
   It MUST NOT be written into the pointer-only `## X. CHANGELOG` section in the main guideline file.

### SPEC-004 — Implement Recyclable-Loop Evidence Accumulation and Handoff Contract (`TK008`)

| Field | Detail |
|:--|:--|
| Requirement Source | `GATE-001` GIR-004; approved `TK004` execution specification |
| Primary Inputs | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.9/proposal/proposal_T104-PH001-ST008-AC001.9-GATE-001_gir-disposition-package.md`; `prompt/templates/consultant/workspace/workspace_documentation_rules.md`; `prompt/templates/consultant/workspace/guideline_workspace_dev-report.md`; `prompt/templates/consultant/workspace/guideline_workspace_verification.md`; `prompt/templates/consultant/workspace/guideline_workspace_implementation.md` |
| Write Scope | `prompt/templates/consultant/workspace/workspace_documentation_rules.md`; `prompt/templates/consultant/workspace/changelog/changelog_workspace_documentation_rules.md` |
| Output | Amended `workspace_documentation_rules.md` and dedicated changelog entry |
| Acceptance Criteria | Section 7 of the workspace documentation rules explicitly governs recyclable-loop evidence accumulation, defines mandatory artifact handoff obligations at each boundary, and preserves same-gate recycle lineage without changing role-boundary sections. |
| Status | `open` |

#### Implementation Detail

**Vocabulary note**: This SPEC item references DEV-REPORT package taxonomy terms (`package_role`, `primary_report`, `consolidated_from`) whose canonical definitions are established in SPEC-001. Implementers MUST use SPEC-001's exact terminology when authoring handoff-matrix rows that reference producer-package frontmatter keys.

1. In `workspace_documentation_rules.md`, inside `## 7. WORKFLOW CHAIN AND HANDOFF CONTRACTS`, insert a new subsection after the existing `### C. Inter-Artifact Linkage Rules` block and before the next document-level separator with the exact heading:
   - `### D. Recyclable-Loop Evidence Accumulation and Handoff`
2. In that new subsection, add a mandatory rules block covering all of the following:
   - Each recycle cycle MUST produce cycle-local evidence rather than overwriting lineage.
   - Rework under the same gate MUST preserve the same gate identity.
   - Final gate packaging MUST preserve a navigable lineage from the active gate-facing evidence back to prior cycle evidence.
3. In that new subsection, add a handoff matrix with the exact columns:
   - `| Boundary | Required Outbound Artifact | Minimum Contents | Blocking Rule |`
4. Populate the handoff matrix with exactly these four rows:
   - `Developer -> Reviewer`
   - `Reviewer -> Consultant`
   - `Consultant -> Developer`
   - `Consultant -> Client`
5. The `Developer -> Reviewer` row MUST require:
   - a DEV-REPORT
   - `source_plan`
   - `implementation_reference` when an IMPLEMENTATION artifact exists
   - `package_role`, `primary_report`, and `consolidated_from` when a multi-report package exists
   - a traceability matrix and handoff section
6. The `Reviewer -> Consultant` row MUST require:
   - a VERIFICATION artifact
   - Evidence Set coverage of the active producer-evidence package
   - findings or explicit no-findings posture
   - a reviewer verdict
7. The `Consultant -> Developer` row MUST require:
   - an IMPLEMENTATION artifact when new execution detail is needed
   - explicit task/gate linkage
   - references to the controlling approved GIR package or the controlling verification findings, depending on the path
8. The `Consultant -> Client` row MUST require:
   - a PROPOSAL package
   - Gate Package Index
   - Evidence Index
   - consultant recommendation
   - GDR when the archetype is `gate_disposition`
9. In the new subsection, add a separate `Lineage rules` bullet list stating:
   - supplementary DEV-REPORTs accumulate across bounded execution slices within the same package
   - consolidated primary DEV-REPORTs point to supplementary reports through `consolidated_from`
   - VERIFICATION re-assessment remains same-gate and version-bumped rather than renamed to a new gate
   - proposal evidence indexes SHOULD surface current active evidence first and preserve historical evidence as lineage context rather than deleting it
10. Add a final explicit boundary sentence:
   - This subsection does not alter the consultant/developer/reviewer ownership model; it governs evidence flow and handoff obligations only.
11. Do not edit Section 6 or Section 8 in this task.
12. Add a changelog entry for AC001.9 describing the recyclable-loop evidence and handoff contract.
13. The changelog row for this task MUST be written to:
   - `prompt/templates/consultant/workspace/changelog/changelog_workspace_documentation_rules.md`
   It MUST NOT be written into the pointer-only `## 12. CHANGELOG` section in the main rules file.

### SPEC-005 — Update Existing Templates for the Approved Package Model (`TK009`)

| Field | Detail |
|:--|:--|
| Requirement Source | `TK005` through `TK008` outputs; approved `TK004` execution specification |
| Primary Inputs | Amended DEV-REPORT guideline; amended VERIFICATION guideline; existing DEV-REPORT and VERIFICATION templates |
| Write Scope | `prompt/templates/consultant/workspace/template_workspace_dev-report.md`; `prompt/templates/consultant/workspace/template_workspace_verification.md`; template-inventory wording in the amended DEV-REPORT and VERIFICATION guidelines if needed to describe changed template capability |
| Output | Updated existing templates only |
| Acceptance Criteria | The existing DEV-REPORT and VERIFICATION templates explicitly support the approved package model and reviewer intake workflow; no new template file is created; the ANALYSIS template remains unchanged. |
| Status | `open` |

#### Implementation Detail

1. In `template_workspace_dev-report.md` frontmatter, insert the following keys immediately before `consolidated_from`:
   - `package_role: '[primary | supplementary; omit only when the package model does not apply]'`
   - `primary_report: '[repo-relative path to the primary DEV-REPORT when this file is supplementary; omit otherwise]'`
2. Revise the `consolidated_from` comment line so it explicitly reads as the downward linkage from a consolidated primary DEV-REPORT to its supplementary DEV-REPORTs.
3. Do not add new body sections to the DEV-REPORT template. The existing Executive Summary, Traceability Matrix, and Handoff sections are sufficient.
4. In `template_workspace_verification.md`, replace the generic bullets in `## II. Evidence Set (Artifacts Reviewed)` with a deterministic grouping prompt that includes:
   - `Primary DEV-REPORT`
   - `Supplementary DEV-REPORTs (omit if not applicable)`
   - `Other task deliverables`
   - `Governance references`
5. In the `template_workspace_verification.md` `## III. Verification Checklist` introductory area, add one sentence stating that checklist groups MAY compare the primary DEV-REPORT against one or more supplementary DEV-REPORTs when verifying consolidated package accuracy.
6. Do not create a new ANALYSIS template and do not edit `template_workspace_analysis.md` in this task.
7. If a developer believes the ANALYSIS template must change to support GIR-003, stop and escalate rather than inventing a new template path or ad hoc structure.
8. If wording is added in the DEV-REPORT or VERIFICATION guideline template-inventory sections to describe the updated template capability, keep the same template paths and do not add a new inventory row.

### SPEC-006 — Produce the GATE-002 DEV-REPORT Handoff (`TK010`)

| Field | Detail |
|:--|:--|
| Requirement Source | `guideline_workspace_dev-report.md`; `TK005` through `TK009` completion; approved `TK004` execution specification |
| Primary Inputs | The amended guideline/template files from `TK005` through `TK009`; this `TK004` artifact |
| Write Scope | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.9/dev-report/dev-report_T104-PH001-ST008-AC001.9_gate-002-handoff_<YYYY-MM-DD>.md` |
| Output | One DEV-REPORT artifact for `GATE-002` handoff |
| Acceptance Criteria | A single primary DEV-REPORT is produced for `GATE-002`, it covers `TK005` through `TK009`, it references this implementation artifact, it records validation evidence for each amended surface, and it hands off cleanly to `TK011`. |
| Status | `open` |

#### Implementation Detail

1. Produce exactly one DEV-REPORT for AC001.9 `GATE-002`. Do NOT create supplementary DEV-REPORTs for this activity.
2. Use the canonical path:
   - `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.9/dev-report/dev-report_T104-PH001-ST008-AC001.9_gate-002-handoff_<YYYY-MM-DD>.md`
3. Populate DEV-REPORT frontmatter with all of the following:
   - `artifact_type: 'DEV-REPORT'`
   - `initiative_id: 'T104'`
   - `initiative_code: 'CWS'`
   - `phase: '1'`
   - `stream_id: 'T104-PH001-ST008'`
   - `activity_id: 'T104-PH001-ST008-AC001.9'`
   - `task_id: 'T104-PH001-ST008-AC001.9-TK010'`
   - `source_plan: 'prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.9/plan_T104-PH001-ST008-AC001.9.md'`
   - `implementation_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.9/implementation/implementation_T104-PH001-ST008-AC001.9_phase-2-guideline-amendments.md'`
   - `target_gate: 'T104-PH001-ST008-AC001.9-GATE-002'`
   - `package_role: 'primary'`
   - omit `primary_report`
   - omit `consolidated_from`
4. The DEV-REPORT `scope` value MUST describe the report as the consolidated implementation-evidence handoff for `TK005` through `TK009`.
5. In `## 2. IMPLEMENTATION LOG`, create one subsection per work item:
   - `TK005`
   - `TK006`
   - `TK007`
   - `TK008`
   - `TK009`
6. In `## 3. VALIDATION EVIDENCE`, include at minimum these `rg` verification commands or exact logical equivalents:
   - a command proving the DEV-REPORT guideline now contains the new package-taxonomy headings and linkage keys
   - a command proving the VERIFICATION guideline now contains the multi-report intake subsection
   - a command proving the ANALYSIS guideline now contains the recyclable-loop traceability-audit profile
   - a command proving `workspace_documentation_rules.md` now contains the recyclable-loop handoff subsection
   - a command proving the DEV-REPORT and VERIFICATION templates now contain the new prompt fields/instructions introduced by `TK009`
   - a command proving the four dedicated changelog files contain AC001.9 amendment rows for `TK005` through `TK008`
7. In `## 4. TRACEABILITY MATRIX`, include one row for each of:
   - `TK005`
   - `TK006`
   - `TK007`
   - `TK008`
   - `TK009`
   - `SPEC-001`
   - `SPEC-002`
   - `SPEC-003`
   - `SPEC-004`
   - `SPEC-005`
8. In `## 5. HANDOFF`, state the next owner as `LLM_Reviewer`, identify `TK011` as the next task, and list the exact files the reviewer must inspect.
9. If no automated tests exist for these guideline/template changes, state that explicitly in the validation interpretation instead of inventing test output.

### SPEC-007 — Reviewer Verification Contract for `TK011`

| Field | Detail |
|:--|:--|
| Requirement Source | `guideline_workspace_verification.md`; `TK010` handoff contract; approved `TK004` execution specification |
| Primary Inputs | `TK010` DEV-REPORT; all amended guideline/template files; approved `GATE-001` proposal |
| Write Scope | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.9/verification/verification_T104-PH001-ST008-AC001.9_gate-002.md` |
| Output | One `GATE-002` VERIFICATION artifact |
| Acceptance Criteria | The reviewer verifies the delivered guideline/template package against this `TK004` spec item set and produces an evidence-first verdict covering all four approved governance changes and the template updates. |
| Status | `open` |

#### Implementation Detail

1. The Evidence Set MUST include:
   - the `TK010` DEV-REPORT
   - this `TK004` implementation specification
   - the amended DEV-REPORT guideline
   - the amended VERIFICATION guideline
   - the amended ANALYSIS guideline
   - the amended `workspace_documentation_rules.md`
   - `prompt/templates/consultant/workspace/changelog/changelog_guideline_workspace_dev-report.md`
   - `prompt/templates/consultant/workspace/changelog/changelog_guideline_workspace_verification.md`
   - `prompt/templates/consultant/workspace/changelog/changelog_guideline_workspace_analysis.md`
   - `prompt/templates/consultant/workspace/changelog/changelog_workspace_documentation_rules.md`
   - the updated DEV-REPORT template
   - the updated VERIFICATION template
   - the approved `GATE-001` proposal
2. The Verification Checklist MUST contain at least these criterion groups:
   - `DEV-REPORT package taxonomy`
   - `VERIFICATION multi-report intake`
   - `ANALYSIS traceability-audit profile`
   - `Workflow-chain handoff contract`
   - `Template alignment`
3. The reviewer MUST verify that:
   - no new artifact family or new ANALYSIS type was introduced
   - the GIR-003 implementation used the existing ANALYSIS taxonomy
   - `TK009` did not create a new template path
   - the delivered wording did not expand scope beyond the approved GIR package
4. If the delivered package contains a proposal-guideline drift that would contaminate `GATE-002`, record it so `TK012` can correct the package before client review.

### SPEC-008 — Consultant Proposal Contract for `TK012`

| Field | Detail |
|:--|:--|
| Requirement Source | `guideline_workspace_proposal.md`; `TK011` verification output; approved `GATE-001` scope |
| Primary Inputs | `TK011` verification artifact; `TK010` DEV-REPORT; this `TK004` implementation specification; approved `GATE-001` proposal |
| Write Scope | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.9/proposal/proposal_T104-PH001-ST008-AC001.9-GATE-002_gir-disposition-package.md` |
| Output | One `GATE-002` gate-disposition proposal |
| Acceptance Criteria | The `GATE-002` proposal packages the full implementation-backed gate stack, uses only proposal-guideline-compliant gate-package vocabulary, maps GIR-001 through GIR-004 to delivered implementation evidence, and leaves the `GDR` pending client decision. |
| Status | `open` |

#### Implementation Detail

1. The `GATE-002` proposal MUST use the `gate_disposition` archetype and the exact ordered section structure required by `guideline_workspace_proposal.md`.
2. In the `Gate Package Index`, use only these `Client Priority` values:
   - `Required`
   - `Recommended`
   - `Reference`
3. Do NOT reuse the non-compliant `Primary` or `Review` priority labels from the AC001.9 `GATE-001` proposal.
4. The `Disposition Summary Register` and `Detailed Disposition Register` MUST preserve the four-change structure of `GIR-001` through `GIR-004`:
   - `GIR-001` -> DEV-REPORT package taxonomy delivered
   - `GIR-002` -> VERIFICATION intake protocol delivered
   - `GIR-003` -> ANALYSIS traceability-audit protocol delivered
   - `GIR-004` -> recyclable-loop evidence handoff contract delivered
5. The Evidence Index MUST include, at minimum:
   - this `TK004` implementation specification
   - the `TK010` DEV-REPORT
   - the `TK011` verification artifact
   - all four amended guideline files
   - the four dedicated guideline/rules changelog files updated by `TK005` through `TK008`
   - the updated templates
   - the approved `GATE-001` proposal as historical scope authority
6. The Consultant Gate Recommendation MUST explicitly state whether it aligns with or departs from the reviewer verdict in `TK011`.
7. The `GDR` MUST remain pending until the client records the `GATE-002` decision.

## V. TASK-TO-SPEC OVERVIEW

The following table maps each Phase 2 task to its governing SPEC item for developer orientation. Execution ordering and task dependencies are governed by the activity plan, not by this specification.

| Task | SPEC Item | Target Surface |
|:--|:--|:--|
| `TK005` | SPEC-001 | `guideline_workspace_dev-report.md` |
| `TK006` | SPEC-002 | `guideline_workspace_verification.md` |
| `TK007` | SPEC-003 | `guideline_workspace_analysis.md` |
| `TK008` | SPEC-004 | `workspace_documentation_rules.md` |
| `TK009` | SPEC-005 | `template_workspace_dev-report.md`, `template_workspace_verification.md` |
| `TK010` | SPEC-006 | `dev-report/` |
| `TK011` | SPEC-007 | `verification/` |
| `TK012` | SPEC-008 | `proposal/` |

## VI. REFERENCES

| Document | Path |
|:--|:--|
| Governing Plan | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.9/plan_T104-PH001-ST008-AC001.9.md` |
| Approved GATE-001 Proposal | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.9/proposal/proposal_T104-PH001-ST008-AC001.9-GATE-001_gir-disposition-package.md` |
| Gap Analysis | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.9/analysis/analysis_T104-PH001-ST008-AC001.9_recyclable-loop-artifact-governance-gaps.md` |
| External Review | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.9/analysis/analysis_T104-PH001-ST008-AC001.9_gate-001-external-review.md` |
| Lifecycle Task Specification | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.9/implementation/implementation_T104-PH001-ST008-AC001.9_recyclable-loop-artifact-governance.md` |
| DEV-REPORT Guideline | `prompt/templates/consultant/workspace/guideline_workspace_dev-report.md` |
| VERIFICATION Guideline | `prompt/templates/consultant/workspace/guideline_workspace_verification.md` |
| ANALYSIS Guideline | `prompt/templates/consultant/workspace/guideline_workspace_analysis.md` |
| Workspace Documentation Rules | `prompt/templates/consultant/workspace/workspace_documentation_rules.md` |
| IMPLEMENTATION Guideline | `prompt/templates/consultant/workspace/guideline_workspace_implementation.md` |
| DEV-REPORT Template | `prompt/templates/consultant/workspace/template_workspace_dev-report.md` |
| VERIFICATION Template | `prompt/templates/consultant/workspace/template_workspace_verification.md` |

## VII. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.2.0 | 2026-03-25 | Amendment | Closed the dedicated-changelog scope gap after orchestration-readiness review: added the four workspace changelog files to Phase 2 write scope, bound SPEC-001 through SPEC-004 changelog work to those exact files, and extended SPEC-006 through SPEC-008 so downstream DEV-REPORT, VERIFICATION, and GATE-002 proposal packaging explicitly validate and index the changelog evidence. |
| v1.1.0 | 2026-03-25 | Amendment | External review remediation: added `proposal_reference` frontmatter key for CONV-007 compliance, replaced §V execution-ordering constraints with an informational task-to-SPEC overview table (execution ordering is plan authority), added cross-SPEC vocabulary notes to SPEC-002 and SPEC-004 for self-containment, and clarified graduated SHOULD/MUST normative strength between SPEC-001 step 13 and SPEC-002 step 5. Source: external review of v1.0.0 implementation specification. |
| v1.0.0 | 2026-03-25 | Initial | Phase 2 task specification created for AC001.9 `TK004`. Converts the approved `GATE-001` GIR package into exact amendment instructions for the DEV-REPORT guideline, VERIFICATION guideline, ANALYSIS guideline, workspace documentation rules, existing templates, and the `GATE-002` handoff stack. |
