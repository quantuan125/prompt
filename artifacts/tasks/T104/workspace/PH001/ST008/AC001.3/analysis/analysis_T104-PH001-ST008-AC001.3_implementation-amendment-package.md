---
artifact_type: 'ANALYSIS'
analysis_type: 'assessment'
initiative_id: 'T104'
initiative_code: 'CWS'
phase: '1'
stream_id: 'T104-PH001-ST008'
activity_id: 'T104-PH001-ST008-AC001.3'
task_id: 'T104-PH001-ST008-AC001.3-TK005'
version: '1.0.0'
date: '2026-03-20'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.3/plan_T104-PH001-ST008-AC001.3.md'
gate_reference: 'T104-PH001-ST008-AC001.3-GATE-001'
proposal_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.3/proposal/proposal_T104-PH001-ST008-AC001.3-GATE-001_gir-disposition-package.md'
standards_input_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.3/proposal/proposal_T104-PH001-ST008-AC001.3_implementation-family-architecture.md'
purpose: 'Developer-ready implementation amendment package consolidating the approved Gate-001 Path B architecture into change-level specifications for TK006 (family surfaces) and TK007 (vertical integration). This artifact is the sole specification input for developer execution.'
consumers:
  - 'T104-PH001-ST008-AC001.3-TK006'
  - 'T104-PH001-ST008-AC001.3-TK007'
---

# ANALYSIS: IMPLEMENTATION Amendment Package — Developer-Ready Specification

## I. PURPOSE & AUTHORITY

**Purpose**: Consolidate the approved GATE-001 Path B architecture into a single, developer-ready change specification. This artifact is the primary input for TK006 and TK007.

**Authority chain**:
- **Decision authority**: Gate-001 GDR (`APPROVE`, 2026-03-19) — `proposal_T104-PH001-ST008-AC001.3-GATE-001_gir-disposition-package.md`
- **Architectural authority**: Standards-input proposal — `proposal_T104-PH001-ST008-AC001.3_implementation-family-architecture.md`
- **This artifact**: Translates the above into file-level change instructions. Does NOT hold decision authority or reopen approved GIR items.

**Audience**: `LLM_Developer` (TK006, TK007 execution)

---

## II. CHANGE PACKAGE OVERVIEW

### A. Task-to-Change Mapping

| Task | Scope | Files Created / Amended | Owner |
|:--|:--|:--|:--|
| TK006 | Create IMPLEMENTATION family authoring surfaces | **Create**: `guideline_workspace_implementation.md`, `template_workspace_implementation_remediation-specification.md`, `template_workspace_implementation_task-specification.md` | `LLM_Developer` |
| TK007 | Integrate IMPLEMENTATION into existing governance surfaces | **Amend**: `workspace_documentation_rules.md`, `guideline_workspace_plan.md`, `guideline_workspace_analysis.md` | `LLM_Developer` |

### B. Execution Sequence

TK006 MUST complete before TK007. TK007 patches reference surfaces that TK006 creates (e.g., the new guideline path appears in documentation-rules inventory).

---

## III. TK006 SPECIFICATION — IMPLEMENTATION FAMILY SURFACES

### A. File 1: `guideline_workspace_implementation.md`

**Path**: `prompt/templates/consultant/workspace/guideline_workspace_implementation.md`

**Pattern source**: Follow the structural pattern of `guideline_workspace_verification.md` and `guideline_workspace_dev-report.md` (single guideline governing the family).

**Required frontmatter**:

```yaml
artifact_type: 'PROCEDURAL_GUIDELINE'
domain: 'consultant_workspace'
topic: 'implementation_authoring'
version: '1.0.0'
date: '2026-03-20'
status: 'draft'
author: 'LLM_Developer'
decision_owner_role: 'Client'
template_reference: 'prompt/templates/consultant/workspace/README.md'
```

**Required sections**:

#### Section I: PURPOSE
- Define authoring rules for IMPLEMENTATION workspace artifacts.
- State that the family provides detailed implementation specification between plan task authority and developer execution evidence.
- Reference the two subtypes and their respective triggers.

#### Section II: ROLE BOUNDARY (LOCKED)
- `LLM_Consultant` is the author for `remediation_specification` subtype.
- `LLM_Consultant` or `LLM_Planner` is the author for `task_specification` subtype.
- `LLM_Developer` is the primary consumer (execution).
- `LLM_Reviewer` is a secondary consumer for `remediation_specification` (re-assessment input).
- IMPLEMENTATION artifacts MUST NOT hold a GDR section. Gate decisions remain exclusively in `gate_disposition` proposals per `guideline_workspace_proposal.md` §VII. (CONV-006)

#### Section III: SUBTYPE TAXONOMY
- Enumerate exactly two subtypes for Draft 1:
  1. `remediation_specification` — Trigger: Gate verdict of `RECYCLE`. Purpose: detailed implementation specification for flipping gate findings from RECYCLE to PASS.
  2. `task_specification` — Trigger: Task complexity exceeds plan-step capacity. Purpose: detailed implementation specification for complex tasks.
- Each subtype has a dedicated template (CONV-003).
- State that additional subtypes require a future amendment; Draft 1 is capped at these two.

#### Section IV: GOVERNANCE RULES (UNIVERSAL)
Encode the six approved conventions:

| Convention | Rule |
|:--|:--|
| CONV-006 | IMPLEMENTATION artifacts SHALL NOT contain a GDR section |
| CONV-007 | Mandatory frontmatter backlinks: `plan_reference`, `task_id` or `gate_id`, and triggering artifact reference (`verification_reference` or `proposal_reference`) |
| CONV-008 | Mandatory audience/authority preamble in Section I distinguishing this artifact from plan authority and proposal decision authority |
| CONV-009 | For `remediation_specification`, the artifact SHALL exist as a formal task above the gate in the task register (Directive B) |
| CONV-010 | One artifact per logical implementation scope (task-ID or gate-remediation-cycle scoping) |
| CONV-011 | Plan task steps SHALL be high-level summary only when an IMPLEMENTATION artifact exists; the plan step SHALL reference the artifact path |

#### Section V: FRONTMATTER SPECIFICATION
- Required fields for all subtypes: `artifact_type` (`IMPLEMENTATION`), `implementation_type` (`remediation_specification` or `task_specification`), `initiative_id`, `initiative_code`, `phase`, `stream_id`, `activity_id`, `task_id`, `version`, `date`, `status`, `author`, `decision_owner_role`, `plan_reference`
- Additional required fields for `remediation_specification`: `gate_id`, `verification_reference`, `proposal_reference`
- Additional required fields for `task_specification`: (none beyond universal set)

#### Section VI: LIFECYCLE RULES
- `remediation_specification`: Created after RECYCLE verdict → consumed during remediation execution → version-bumped if scope changes → closed when gate re-assessment passes.
- `task_specification`: Created during task planning or after plan amendment → consumed during developer execution → version-bumped if scope changes → closed when task completes.

#### Section VII: RELATIONSHIP TO OTHER ARTIFACTS
- **Plan**: Plan retains tracked-work authority. IMPLEMENTATION provides specification depth. Plan steps reference the artifact path when one exists (CONV-011).
- **Verification**: For `remediation_specification`, the artifact references verification findings by ID. Complementary relationship: revision-checklist = "what needs fixing" (reviewer), remediation specification = "how to fix it" (consultant).
- **Dev-Report**: Developer execution evidence references the IMPLEMENTATION artifact as the specification input.
- **Proposal**: IMPLEMENTATION does not hold decision authority. Gate decisions remain in `gate_disposition` proposals.

#### Section VIII: TEMPLATE INVENTORY
- `template_workspace_implementation_remediation-specification.md`
- `template_workspace_implementation_task-specification.md`

#### Section IX: CHANGELOG

---

### B. File 2: `template_workspace_implementation_remediation-specification.md`

**Path**: `prompt/templates/consultant/workspace/template_workspace_implementation_remediation-specification.md`

**Content structure** (derived from standards-input proposal §V.G exemplar):

```markdown
---
artifact_type: 'IMPLEMENTATION'
implementation_type: 'remediation_specification'
initiative_id: '{{INITIATIVE_ID}}'
initiative_code: '{{INITIATIVE_CODE}}'
phase: '{{PHASE}}'
stream_id: '{{STREAM_ID}}'
activity_id: '{{ACTIVITY_ID}}'
gate_id: '{{GATE_ID}}'
task_id: '{{TASK_ID}}'
version: '1.0.0'
date: '{{DATE}}'
status: 'draft'
author: '{{AUTHOR_ROLE}}'
decision_owner_role: 'Client'
plan_reference: '{{PLAN_PATH}}'
verification_reference: '{{VERIFICATION_PATH}}'
proposal_reference: '{{PROPOSAL_PATH}}'
purpose: '{{PURPOSE}}'
---

# IMPLEMENTATION (Remediation Specification): {{TITLE}}

## I. PURPOSE & AUTHORITY
- Purpose: [what this remediation specification covers]
- Authority chain: Plan authorizes work (task_id) -> This artifact specifies HOW ->
  Dev-report records execution -> Verification re-assesses
- Audience: LLM_Developer (primary), LLM_Reviewer (re-assessment input)
- This artifact does NOT hold a GDR. Gate decision is recorded in the
  gate_disposition proposal.

## II. REMEDIATION SCOPE
- Gate: [gate_id]
- Trigger: RECYCLE verdict from [verification_reference]
- Governing plan task: [task_id]
- Findings addressed: [list of FINDING-### IDs from verification]

## III. REMEDIATION ITEMS

### REM-001 — [Title]

| Field | Detail |
|:--|:--|
| Finding Reference | [FINDING-### from verification] |
| Implementation Detail | [detailed HOW] |
| Expected Format | [schema, structure, output format] |
| Acceptance Criteria | [what reviewer checks during re-assessment] |
| Resolution Status | `open` / `resolved` |

[Repeat for each remediation item]

## IV. IMPLEMENTATION SEQUENCE
[Recommended execution order]

## V. REFERENCES

| Document | Path |
|:--|:--|
| Governing Plan | [plan_reference] |
| Verification | [verification_reference] |
| Gate-Disposition Proposal | [proposal_reference] |

## VI. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
```

---

### C. File 3: `template_workspace_implementation_task-specification.md`

**Path**: `prompt/templates/consultant/workspace/template_workspace_implementation_task-specification.md`

**Content structure** (parallel to remediation-specification, adapted for proactive tasks):

```markdown
---
artifact_type: 'IMPLEMENTATION'
implementation_type: 'task_specification'
initiative_id: '{{INITIATIVE_ID}}'
initiative_code: '{{INITIATIVE_CODE}}'
phase: '{{PHASE}}'
stream_id: '{{STREAM_ID}}'
activity_id: '{{ACTIVITY_ID}}'
task_id: '{{TASK_ID}}'
version: '1.0.0'
date: '{{DATE}}'
status: 'draft'
author: '{{AUTHOR_ROLE}}'
decision_owner_role: 'Client'
plan_reference: '{{PLAN_PATH}}'
purpose: '{{PURPOSE}}'
---

# IMPLEMENTATION (Task Specification): {{TITLE}}

## I. PURPOSE & AUTHORITY
- Purpose: [what this task specification covers]
- Authority chain: Plan authorizes work (task_id) -> This artifact specifies HOW ->
  Dev-report records execution
- Audience: LLM_Developer (primary)
- This artifact does NOT hold a GDR. Gate decisions (if applicable) are recorded
  in gate_disposition proposals.

## II. TASK SCOPE
- Governing plan task: [task_id]
- Trigger: [task complexity rationale]
- Deliverable contract: [from plan]

## III. SPECIFICATION ITEMS

### SPEC-001 — [Title]

| Field | Detail |
|:--|:--|
| Requirement Source | [plan task step or amendment reference] |
| Implementation Detail | [detailed HOW] |
| Expected Format | [schema, structure, output format] |
| Acceptance Criteria | [what defines completion] |
| Status | `open` / `resolved` |

[Repeat for each specification item]

## IV. IMPLEMENTATION SEQUENCE
[Recommended execution order]

## V. REFERENCES

| Document | Path |
|:--|:--|
| Governing Plan | [plan_reference] |

## VI. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
```

---

## IV. TK007 SPECIFICATION — VERTICAL INTEGRATION PATCHES

### A. Patch 1: `workspace_documentation_rules.md`

**Path**: `prompt/templates/consultant/workspace/workspace_documentation_rules.md`

#### Patch 1a: §3 Artifact Type Inventory — Add Row

Insert after the DEV-REPORT row:

| Artifact Type | File Prefix | Purpose | Template | Guideline |
|:--|:--|:--|:--|:--|
| IMPLEMENTATION | `implementation_` | Detailed implementation specification: remediation specifications (gate RECYCLE response), task specifications (complex implementation detail) | `prompt/templates/consultant/workspace/template_workspace_implementation_<subtype>.md` | `prompt/templates/consultant/workspace/guideline_workspace_implementation.md` |

#### Patch 1b: §4 Template Inventory — Add Section

Add after §4.G (PROPOSAL Templates):

```markdown
### H. IMPLEMENTATION Templates
- `prompt/templates/consultant/workspace/template_workspace_implementation_remediation-specification.md`
- `prompt/templates/consultant/workspace/template_workspace_implementation_task-specification.md`
```

#### Patch 1c: §5 Guideline Inventory — Add Entry

Add after PROPOSAL guideline entry:

```markdown
- IMPLEMENTATION: `prompt/templates/consultant/workspace/guideline_workspace_implementation.md`
```

#### Patch 1d: §7 Workflow Chain — Updates

**§7.A Implementation-backed chain** — update to:
```
ROADMAP → PLAN → NOTES / ANALYSIS → [IMPLEMENTATION task_specification where needed] → implementation deliverables → DEV-REPORT → VERIFICATION → [IMPLEMENTATION remediation_specification where RECYCLE] → PROPOSAL (GDR where applicable) → SPS / downstream approved artifacts
```

**§7.A Rules** — add:
```markdown
- `IMPLEMENTATION` provides detailed specification depth between plan task authority and developer execution. It does not hold work authority (PLAN) or decision authority (PROPOSAL GDR).
```

**§7.C Inter-Artifact Linkage Rules** — add row:

| Rule | Authority |
|:--|:--|
| `IMPLEMENTATION` provides detailed specification depth; it does not hold work authority (PLAN) or decision authority (PROPOSAL GDR) | Initiative-level |

#### Patch 1e: §8 Role-to-Artifact Ownership Matrix — Add Row

| Artifact Type | Author | Reviewer | Approver / Decision Owner | Primary Consumer |
|:--|:--|:--|:--|:--|
| IMPLEMENTATION | LLM_Consultant (`remediation_specification`); LLM_Consultant or LLM_Planner (`task_specification`) | Reviewer consumes as re-assessment input | Client where gated | Developer, Reviewer |

#### Patch 1f: Version bump

Bump version to `v3.0.0` (new artifact family = major change). Update changelog.

---

### B. Patch 2: `guideline_workspace_plan.md`

**Path**: `prompt/templates/consultant/workspace/guideline_workspace_plan.md`

#### Patch 2a: §IV — Add Plan-Step Boundary Rule

Add after §IV.E (Task Decomposition Rules) as new subsection §IV.F:

```markdown
### F. Plan-Step Boundary When IMPLEMENTATION Artifact Exists

When an `IMPLEMENTATION` artifact exists for a task:
- Plan task steps SHALL be described at high-level summary only.
- The plan step SHALL reference the `IMPLEMENTATION` artifact path for detail.
- This prevents content drift between plan and implementation surfaces.
- The plan retains tracked-work authority; the `IMPLEMENTATION` artifact provides specification depth.

Source: CONV-011 approved at T104-PH001-ST008-AC001.3-GATE-001.
```

#### Patch 2b: §VI.L Gate-Readiness Stack — Add IMPLEMENTATION Reference

In the Implementation-Backed Sequence section, add a note after item 1:

```markdown
> **Note**: When a gate enters `RECYCLE` and remediation work requires detailed specification, a `remediation_specification` IMPLEMENTATION artifact SHOULD be authored to specify the corrective-action detail. The IMPLEMENTATION artifact is a formal task in the remediation loop, placed above the gate row per §VI.K. See `guideline_workspace_implementation.md` for authoring rules.
```

In the Ownership table, add row:

| Stack Position | Fixed Owner | Artifact Type | Governing Guideline |
|:--|:--|:--|:--|
| IMPLEMENTATION task (where applicable) | `LLM_Consultant` | `IMPLEMENTATION` | `guideline_workspace_implementation.md` |

#### Patch 2c: Version bump

Bump version to `v1.16.0`. Update changelog.

---

### C. Patch 3: `guideline_workspace_analysis.md`

**Path**: `prompt/templates/consultant/workspace/guideline_workspace_analysis.md`

#### Patch 3a: §II Role Boundary — Add Informative-Only Clarification

After the existing boundary rule, add:

```markdown
**IMPLEMENTATION boundary**: When an `IMPLEMENTATION` artifact exists for the same scope (task or gate remediation), ANALYSIS artifacts retain their informative/advisory role. ANALYSIS findings and recommendations MAY inform the IMPLEMENTATION specification, but the ANALYSIS artifact MUST NOT duplicate implementation-level specification detail that belongs in the IMPLEMENTATION artifact. The ANALYSIS artifact remains consultant-owned synthesis; the IMPLEMENTATION artifact provides developer-facing specification depth.
```

#### Patch 3b: Version bump

Bump version to `v1.4.0`. Update changelog.

---

## V. CROSS-VALIDATION CHECKLIST

The developer SHOULD validate the following after completing TK006 and TK007:

| # | Check | Target |
|:--|:--|:--|
| 1 | `guideline_workspace_implementation.md` exists and encodes all six CONV rules | TK006 |
| 2 | Both subtype templates exist with correct frontmatter schemas | TK006 |
| 3 | `remediation_specification` template includes authority-preamble and finding-reference sections | TK006 |
| 4 | `task_specification` template includes authority-preamble and scope section | TK006 |
| 5 | `workspace_documentation_rules.md` §3 includes IMPLEMENTATION row | TK007 |
| 6 | `workspace_documentation_rules.md` §4 includes IMPLEMENTATION template entries | TK007 |
| 7 | `workspace_documentation_rules.md` §5 includes IMPLEMENTATION guideline entry | TK007 |
| 8 | `workspace_documentation_rules.md` §7 workflow chain references IMPLEMENTATION | TK007 |
| 9 | `workspace_documentation_rules.md` §8 role matrix includes IMPLEMENTATION row | TK007 |
| 10 | `guideline_workspace_plan.md` §IV.F plan-step boundary rule exists | TK007 |
| 11 | `guideline_workspace_plan.md` §VI.L includes IMPLEMENTATION reference | TK007 |
| 12 | `guideline_workspace_analysis.md` §II includes IMPLEMENTATION boundary | TK007 |
| 13 | No CONV rule is missing or contradicted across all surfaces | TK006 + TK007 |
| 14 | Version bumps and changelogs are consistent | TK006 + TK007 |

---

## VI. REFERENCES

| Document | Path |
|:--|:--|
| Governing Plan | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.3/plan_T104-PH001-ST008-AC001.3.md` |
| Gate-001 GDR | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.3/proposal/proposal_T104-PH001-ST008-AC001.3-GATE-001_gir-disposition-package.md` |
| Standards-Input Proposal | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.3/proposal/proposal_T104-PH001-ST008-AC001.3_implementation-family-architecture.md` |
| External Review | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.3/analysis/analysis_T104-PH001-ST008-AC001.3_external-review_gate-001-package.md` |
| Verification Guideline | `prompt/templates/consultant/workspace/guideline_workspace_verification.md` |
| Dev-Report Guideline | `prompt/templates/consultant/workspace/guideline_workspace_dev-report.md` |
| Plan Guideline | `prompt/templates/consultant/workspace/guideline_workspace_plan.md` |
| Analysis Guideline | `prompt/templates/consultant/workspace/guideline_workspace_analysis.md` |
| Documentation Rules | `prompt/templates/consultant/workspace/workspace_documentation_rules.md` |

## VII. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-03-20 | Initial | Developer-ready amendment package consolidating the approved Gate-001 Path B architecture into change-level specifications for TK006 (3 new family surfaces) and TK007 (3 vertical integration patches). Includes cross-validation checklist. |
