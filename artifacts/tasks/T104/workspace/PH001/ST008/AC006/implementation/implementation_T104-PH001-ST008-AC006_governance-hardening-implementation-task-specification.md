---
artifact_type: 'IMPLEMENTATION'
implementation_type: 'task_specification'
initiative_id: 'T104'
initiative_code: 'CWS'
phase: '1'
stream_id: 'T104-PH001-ST008'
activity_id: 'T104-PH001-ST008-AC006'
task_id: 'T104-PH001-ST008-AC006-TK003.1'
version: '1.1.0'
date: '2026-03-30'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/plan_T104-PH001-ST008-AC006.md'
execution_audience: 'developer'
purpose: 'Developer-facing execution specification for AC006 post-GATE-001 governance hardening across the eight target governance files identified in TK002.'
---

# IMPLEMENTATION (Task Specification): AC006 Governance Hardening Post-GATE-001 Developer Execution

## I. PURPOSE & AUTHORITY

- **Purpose**: This artifact specifies the complete HOW for TK004 after `T104-PH001-ST008-AC006-GATE-001` approval. It translates the approved AC006 governance direction into bounded file mutations across eight target governance surfaces.
- **Authority chain**: AC006 activity plan authorizes tracked work -> this artifact specifies HOW for `TK004` -> developer execution applies the approved governance changes -> DEV-REPORT and later verification record execution evidence.
- **Audience**: `LLM_Developer` is the primary consumer for execution. `LLM_Reviewer` is a secondary consumer for downstream verification. `LLM_Consultant` remains the commissioning authority only.
- **This artifact does NOT hold a GDR.** Gate decisions remain exclusively in `gate_disposition` proposals.
- **Execution boundary**: This artifact is included in the `GATE-001` package as a downstream commissioning surface, but it MUST NOT be executed until the client records `APPROVE` or `APPROVE WITH CONDITIONS` in the `GATE-001` GDR.

## II. TASK SCOPE

- **Governing plan task**: `T104-PH001-ST008-AC006-TK004`
- **Trigger**: The governance direction is already decision-ready, but the downstream implementation touches eight governance files and multiple cross-file conventions, exceeding plan-step capacity.
- **Deliverable contract**: Update the eight AC006 target governance files so they implement the approved conventions CONV-015 through CONV-023, without changing any non-target activity artifacts.
- **Write scope**:
  - `prompt/templates/consultant/workspace/guideline_workspace_implementation.md`
  - `prompt/templates/consultant/workspace/template_workspace_implementation_task-specification.md`
  - `prompt/templates/consultant/workspace/template_workspace_implementation_remediation-specification.md`
  - `prompt/templates/consultant/workspace/guideline_workspace_analysis.md`
  - `prompt/templates/consultant/workspace/guideline_workspace_plan.md`
  - `prompt/templates/consultant/workspace/guideline_workspace_proposal.md`
  - `prompt/templates/consultant/workspace/guideline_workspace_notes.md`
  - `prompt/templates/consultant/workspace/workspace_documentation_rules.md`

## III. SPECIFICATION ITEMS

### SPEC-001 — Amend `guideline_workspace_implementation.md` for CONV-015, CONV-018, CONV-019, and CONV-022

| Field | Detail |
|:--|:--|
| Requirement Source | AC006 TK002 approved governance direction for CONV-015, CONV-018, CONV-019, and CONV-022 |
| Target file(s) | `prompt/templates/consultant/workspace/guideline_workspace_implementation.md` |
| Required end-state posture | The implementation guideline explicitly enforces the execution-facing SPEC quality floor, the model-agnostic Implementation Detail authoring rules, the IMPLEMENTATION-mediated commissioning rule with the bounded exception, the `standards_input` authority boundary, and the forward-only naming convention split for developer-facing versus consultant/assistant-facing task specifications. |
| Explicit non-target / do-not-change constraints | Do NOT add a new IMPLEMENTATION subtype. Do NOT require retroactive migration of existing implementation artifacts. Do NOT change the RECYCLE-only trigger for `remediation_specification`. |
| Validation check | Verify the guideline contains explicit normative language for CONV-015, CONV-018, CONV-019, and CONV-022 and that the `task_specification` optional audience/frontmatter guidance is aligned with the naming convention and `LLM_Assistant` role model. |
| Blocking ambiguity rule | If any approved GATE-001 GIR changes the accepted governance posture for these conventions, STOP and align the rule text to the recorded GDR instead of the pre-gate draft wording. |
| Status | `open` |

#### Implementation Detail

1. Update the universal governance rules table so CONV-012 is split into a structural rule plus the explicit minimum-detail floor required by CONV-015.
2. Add a rule stating that every execution-facing SPEC item MUST contain: exact target file(s) or surfaces, required end-state posture, validation checks, explicit non-target constraints, and a blocking ambiguity rule.
3. Extend the Implementation Detail guidance so numbered, self-contained steps, explicit file/section locators, and direct if/then conditional wording are required for model-agnostic parsing.
4. Add the IMPLEMENTATION-mediated commissioning rule to the role-boundary or governance-rules section, including the bounded three-condition low-risk exception from TK002.
5. Elevate the standards-input boundary from advisory to explicit authority posture: consultation-only gates use `standards_input` as active authority, and premature concrete artifacts are lineage-only until downstream execution is authorized.
6. Add the forward-only naming convention rule: developer-facing artifacts retain `-task-specification`; consultant/assistant-scoped orchestration artifacts use the `-brief` suffix without creating a new subtype.
7. Update the optional `execution_audience` guidance so it recognizes `assistant` as the consultant-commissioned execution audience aligned to `LLM_Assistant`, while preserving `developer` as default and `consultant` for consultant-owned non-implementation work only.
8. Explicitly deprecate the `agentic_executor` enum value forward-only. New IMPLEMENTATION artifacts MUST use `assistant` (not `agentic_executor`) when execution is delegated to `LLM_Assistant`. Existing artifacts with `agentic_executor` are not retroactively relabeled. The amended enum in the §V.D optional fields table becomes: `'developer'` (default — `LLM_Developer` execution), `'assistant'` (consultant-commissioned `LLM_Assistant` execution), `'consultant'` (consultant-owned non-implementation work). Add a deprecation note immediately after the optional fields table: "> **Deprecated**: `agentic_executor` is no longer a valid value for new artifacts. Use `assistant` for all `LLM_Assistant`-targeted implementation specifications. Existing artifacts authored with `agentic_executor` before this convention are not retroactively relabeled."

### SPEC-002 — Amend `template_workspace_implementation_task-specification.md` for CONV-015 and CONV-022

| Field | Detail |
|:--|:--|
| Requirement Source | AC006 TK002 approved governance direction for CONV-015 and CONV-022 |
| Target file(s) | `prompt/templates/consultant/workspace/template_workspace_implementation_task-specification.md` |
| Required end-state posture | The task-specification template structurally prompts authors to include all CONV-015 minimum-detail fields and instructs future authors on the forward naming convention and model-agnostic Implementation Detail requirements. |
| Explicit non-target / do-not-change constraints | Do NOT convert the template into a mega-template covering new subtypes. Do NOT add retroactive migration instructions for existing artifacts. |
| Validation check | Verify the template's SPEC table explicitly names target file(s), end-state posture, non-target constraints, validation checks, and blocking ambiguity rule, and that the Implementation Detail instructions reflect the structured, numbered, model-agnostic rule set. |
| Blocking ambiguity rule | If the live implementation guideline has been updated differently before TK004 starts, STOP and align the template language to the approved guideline rather than re-inventing a second rule set. |
| Status | `open` |

#### Implementation Detail

1. Keep the frontmatter as `implementation_type: 'task_specification'` with `execution_audience: 'developer'` as the default exemplar.
2. Expand the template prose around Section III so future authors are prompted to produce the full CONV-015 metadata set rather than only freeform summaries.
3. Strengthen the `Implementation Detail` placeholder text so it explicitly requires numbered steps, file/section locators, direct mutation instructions, and explicit conditions.
4. Add a short note in the header or body reminding authors that consultant/assistant orchestration artifacts use the `-brief` filename convention even though they remain `task_specification` artifacts.

### SPEC-003 — Amend `template_workspace_implementation_remediation-specification.md` for CONV-015 cross-model detail requirements

| Field | Detail |
|:--|:--|
| Requirement Source | AC006 TK002 approved governance direction for CONV-015 as applied to remediation specifications |
| Target file(s) | `prompt/templates/consultant/workspace/template_workspace_implementation_remediation-specification.md` |
| Required end-state posture | The remediation template's execution-facing sections enforce the same model-agnostic Implementation Detail discipline required of task specifications, without broadening the RECYCLE-only subtype trigger. |
| Explicit non-target / do-not-change constraints | Do NOT broaden the remediation subtype scope to pre-gate assistant corrections. Do NOT rename the subtype. |
| Validation check | Verify the remediation template includes explicit guidance for numbered, self-contained, model-agnostic Implementation Detail blocks and preserves the RECYCLE-specific context. |
| Blocking ambiguity rule | If any attempt to update this template would require changing the RECYCLE-only lifecycle, STOP and escalate because that change is outside the approved AC006 scope. |
| Status | `open` |

#### Implementation Detail

1. Mirror the model-agnostic Implementation Detail requirements from the task-specification template where they apply to remediation execution.
2. Preserve all remediation-specific backlinks (`gate_id`, `verification_reference`, `proposal_reference`) and the RECYCLE trigger.
3. Do not import the `-brief` naming rule into remediation artifacts; remediation artifacts retain `-remediation-specification` naming.

### SPEC-004 — Amend `guideline_workspace_analysis.md` for CONV-016 and CONV-017

| Field | Detail |
|:--|:--|
| Requirement Source | AC006 TK002 approved governance direction for CONV-016 and CONV-017 |
| Target file(s) | `prompt/templates/consultant/workspace/guideline_workspace_analysis.md` |
| Required end-state posture | The analysis guideline explicitly requires gate-consumed external reviews to assess downstream task readiness, plan-guideline compliance, evidence integrity, role-boundary compliance, unauthorized downstream execution absence, and per-SPEC commissionability whenever an IMPLEMENTATION artifact is in-package. It also requires gate packages with multiple external reviews to designate one authoritative review. |
| Explicit non-target / do-not-change constraints | Do NOT convert consultation-only external reviews into VERIFICATION artifacts. Do NOT weaken the consultant ownership boundary for ANALYSIS artifacts. |
| Validation check | Verify the `external_review` lifecycle description and any relevant required-structure sections explicitly encode both per-SPEC commissionability and authoritative-review selection behavior. |
| Blocking ambiguity rule | If the proposal guideline already governs a package-level behavior, STOP and keep the analysis guideline focused on review scope rather than duplicating proposal mechanics unnecessarily. |
| Status | `open` |

#### Implementation Detail

1. Expand the `external_review` lifecycle row so the downstream task readiness requirement explicitly includes per-SPEC commissionability when an IMPLEMENTATION artifact exists in the package.
2. Add wording clarifying that consultation-only gate reviews must also test package evidence integrity, role-boundary compliance, and absence of unauthorized downstream execution or premature concrete-artifact authority.
3. Add a new rule that when multiple `external_review` analyses exist, one must be designated as authoritative by the gate package, and other review-like analyses become supporting or historical evidence.

### SPEC-005 — Amend `guideline_workspace_plan.md` for CONV-020 and TK003.1 pre-gate positioning clarity

| Field | Detail |
|:--|:--|
| Requirement Source | AC006 TK002 approved governance direction for CONV-020 plus the AC006 gate-stack clarification recorded in SES003 |
| Target file(s) | `prompt/templates/consultant/workspace/guideline_workspace_plan.md` |
| Required end-state posture | The plan guideline explicitly requires same-gate corrections to be tracked across plan, notes, and proposal surfaces, and the consultation-only gate stack text supports inclusion of a downstream implementation specification in-package before client disposition when the gate is authorizing post-gate execution. |
| Explicit non-target / do-not-change constraints | Do NOT collapse consultation-only and implementation-backed gate models into one undifferentiated workflow. Do NOT require developer execution before client disposition. |
| Validation check | Verify the consultation-only gate guidance and same-gate correction language clearly support the AC006 pattern: proposal -> implementation task specification -> external review -> same-gate hardening -> client decision. |
| Blocking ambiguity rule | If the existing plan guideline already contains conflicting language about post-approval-only implementation specs, STOP and resolve that conflict explicitly instead of leaving competing interpretations in place. |
| Status | `open` |

#### Implementation Detail

1. Add or amend the same-gate correction clause so tracked corrections must be reflected in the plan task register, session-note trail, and proposal evidence index.
2. Clarify that a consultation-only gate MAY include a consultant-authored downstream implementation specification in the pre-gate package when the gate's purpose is to authorize governed post-gate execution.
3. Keep the gate identity stable for same-gate correction cycles and explicitly preserve historical lineage when package evidence is superseded.

### SPEC-006 — Amend `guideline_workspace_proposal.md` for CONV-017, CONV-019, and CONV-020

| Field | Detail |
|:--|:--|
| Requirement Source | AC006 TK002 approved governance direction for CONV-017, CONV-019, and CONV-020 |
| Target file(s) | `prompt/templates/consultant/workspace/guideline_workspace_proposal.md` |
| Required end-state posture | The proposal guideline explicitly requires gate packages to designate one authoritative external review when multiple review-like analyses exist, preserves premature concrete artifacts as lineage-only when a standards-input proposal is the active pre-implementation authority surface, and requires evidence-index refresh when same-gate corrections occur. |
| Explicit non-target / do-not-change constraints | Do NOT change the GDR ownership model. Do NOT make consultation-only proposals substitute for downstream execution authorization. |
| Validation check | Verify the `gate_disposition` Gate Package section and the `standards_input` rules make authoritative-review designation, lineage-only treatment, and same-gate evidence refresh explicit. |
| Blocking ambiguity rule | If any package-behavior text would conflict with the analysis or plan guidelines, STOP and harmonize the surfaces rather than preserving contradictory package rules. |
| Status | `open` |

#### Implementation Detail

1. Update the Gate Package guidance so packages with more than one external review must name one authoritative review and classify others as supporting or historical evidence.
2. Strengthen the `standards_input` section so premature concrete artifacts are explicitly lineage-only during consultation-only gates.
3. Add wording that same-gate corrections require a refreshed Gate Package Index / Evidence Index separating current from historical evidence after the correction pass.

### SPEC-007 — Amend `guideline_workspace_notes.md` for same-gate correction session tracking

| Field | Detail |
|:--|:--|
| Requirement Source | AC006 TK002 approved governance direction for CONV-020 |
| Target file(s) | `prompt/templates/consultant/workspace/guideline_workspace_notes.md` |
| Required end-state posture | The notes guideline explicitly requires a new session note when same-gate correction changes package interpretation, evidence status, or readiness posture after a gate package has already been assembled. |
| Explicit non-target / do-not-change constraints | Do NOT rewrite historical session notes into new state. Do NOT treat notes as overriding the proposal-hosted GDR. |
| Validation check | Verify the notes lifecycle and authority sections explicitly prefer new corrective session notes over silent rewrite and tie those sessions to same-gate package correction. |
| Blocking ambiguity rule | If any proposed text would imply that notes outrank the proposal-hosted GDR, STOP and restate the rule as traceability only. |
| Status | `open` |

#### Implementation Detail

1. Expand the corrective-session guidance so same-gate package corrections explicitly require a new session note when the gate remains open but the package baseline changes.
2. Keep the notes boundary intact: notes record decision trail and correction history, but they do not replace the proposal-hosted GDR.
3. Reference the plan/proposal surfaces so the correction trail remains cross-linked rather than isolated inside notes only.

### SPEC-008 — Amend `workspace_documentation_rules.md` for CONV-018, CONV-021, CONV-022, and CONV-023

| Field | Detail |
|:--|:--|
| Requirement Source | AC006 TK002 approved governance direction for CONV-018, CONV-021, CONV-022, and CONV-023 |
| Target file(s) | `prompt/templates/consultant/workspace/workspace_documentation_rules.md` |
| Required end-state posture | The workspace rules explicitly define governed delegated execution commissioning through IMPLEMENTATION artifacts, distinguish consultant-scoped versus program-scoped operational surfaces, recognize the forward naming convention for developer-facing versus assistant/consultant implementation artifacts, and formalize `LLM_Assistant` as a named role with bounded ownership rules. |
| Explicit non-target / do-not-change constraints | Do NOT reassign DEV-REPORT ownership away from `LLM_Developer`. Do NOT treat `LLM_Assistant` as a replacement for `LLM_Developer`. Do NOT require retroactive renaming of existing artifacts. |
| Validation check | Verify the workspace rules show explicit commissioning protocol, scope labels for operational surfaces, a forward naming rule note, and a narrow `LLM_Assistant` role definition plus ownership-matrix treatment. |
| Blocking ambiguity rule | If adding `LLM_Assistant` would require revising unrelated role families or historical activities beyond the bounded AC006 scope, STOP and keep the change limited to the explicit boundary and ownership rules approved at GATE-001. |
| Status | `open` |

#### Implementation Detail

1. Add explicit commissioning language stating that governed delegated execution to developer or assistant roles flows through an IMPLEMENTATION artifact unless the bounded low-risk exception is invoked and recorded.
2. Add labeling language that gate packages must distinguish consultant-scoped operational surfaces from broader program-scoped protocol surfaces.
3. Add a forward-only note in the artifact inventory or naming guidance that developer-facing implementation specs retain `-task-specification`, while consultant/assistant orchestration artifacts use `-brief`.
4. Add `LLM_Assistant` as a named role with bounded scope: consultant-authority execution only, no DEV-REPORT ownership, session-note evidence posture, and no substitution for developer-owned implementation-backed workflow steps.
5. Update the consultation-only workflow chain in §7.A to include an optional IMPLEMENTATION position. The current chain text is: `ROADMAP → PLAN → NOTES / ANALYSIS → PROPOSAL (GDR where applicable) → ANALYSIS (external_review, LLM_Subconsultant) → downstream approved artifacts`. Replace it with: `ROADMAP → PLAN → NOTES / ANALYSIS → [IMPLEMENTATION task_specification where post-gate execution is commissioned] → PROPOSAL (GDR where applicable) → ANALYSIS (external_review, LLM_Subconsultant) → downstream approved artifacts`. Add a clarifying note immediately below the amended chain: "The `[IMPLEMENTATION ...]` step is conditional: it applies only when the consultation-only gate authorizes governed post-gate execution through a commissioning artifact per CONV-018. When the consultation-only gate does not authorize downstream execution (e.g., pure governance-direction approval with no developer or assistant commissioning), this step is omitted."

## IV. IMPLEMENTATION SEQUENCE

1. Apply SPEC-001 first so the implementation guideline becomes the governing rule surface for the rest of the family changes.
2. Apply SPEC-002 and SPEC-003 next so both IMPLEMENTATION templates align with the approved execution-detail rules.
3. Apply SPEC-004 through SPEC-007 to harmonize the analysis, plan, proposal, and notes guidance around review scope and same-gate correction behavior.
4. Apply SPEC-008 last so the cross-family documentation rules reflect the already-updated artifact-family guidance and role-boundary decisions.
5. Produce the downstream DEV-REPORT only after all eight files are updated and verified against this specification.

## V. REFERENCES

| Document | Path |
|:--|:--|
| Governing Plan | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/plan_T104-PH001-ST008-AC006.md` |
| GATE-001 Proposal Package | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/proposal/proposal_T104-PH001-ST008-AC006-GATE-001_governance-disposition.md` |
| Standards-Input Proposal | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/proposal/proposal_T104-PH001-ST008-AC006_governance-input-disposition.md` |
| Comparative Analysis | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/analysis/analysis_T104-PH001-ST008-AC006-TK001.1_implementation-artifact-architecture-assessment.md` |
| Implementation Guideline | `prompt/templates/consultant/workspace/guideline_workspace_implementation.md` |
| Task Specification Template | `prompt/templates/consultant/workspace/template_workspace_implementation_task-specification.md` |
| Remediation Specification Template | `prompt/templates/consultant/workspace/template_workspace_implementation_remediation-specification.md` |
| Analysis Guideline | `prompt/templates/consultant/workspace/guideline_workspace_analysis.md` |
| Plan Guideline | `prompt/templates/consultant/workspace/guideline_workspace_plan.md` |
| Proposal Guideline | `prompt/templates/consultant/workspace/guideline_workspace_proposal.md` |
| Notes Guideline | `prompt/templates/consultant/workspace/guideline_workspace_notes.md` |
| Workspace Documentation Rules | `prompt/templates/consultant/workspace/workspace_documentation_rules.md` |

## VI. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.1.0 | 2026-03-30 | Amendment | Pre-commissioning gap remediation: SPEC-001 amended with step 8 (forward-only deprecation of `agentic_executor` enum value in favor of `assistant` per GAP-H1 from SES005 independent assessment). SPEC-008 amended with step 5 (consultation-only workflow chain in `workspace_documentation_rules.md` §7.A updated to include optional IMPLEMENTATION position per GAP-V1 from SES005 independent assessment). Both amendments approved by client on 2026-03-30. |
| v1.0.0 | 2026-03-30 | Initial | Developer-facing post-GATE-001 implementation task specification created for AC006. Maps the approved governance direction to eight bounded specification items covering all target governance files and explicitly keeps execution blocked until the client records a GATE-001 decision. |
