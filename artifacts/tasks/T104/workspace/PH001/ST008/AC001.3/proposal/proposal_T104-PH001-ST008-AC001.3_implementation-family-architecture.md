---
artifact_type: 'PROPOSAL'
initiative_id: 'T104'
initiative_code: 'CWS'
phase: '1'
stream_id: 'T104-PH001-ST008'
activity_id: 'T104-PH001-ST008-AC001.3'
task_id: 'T104-PH001-ST008-AC001.3-TK004.1'
version: '1.1.0'
date: '2026-03-19'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.3/plan_T104-PH001-ST008-AC001.3.md'
analysis_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.3/analysis/analysis_T104-PH001-ST008-AC001.3_remediation-artifact-type-comparison.md'
target_standards:
  - 'workspace_documentation_rules.md'
  - 'guideline_workspace_plan.md'
  - 'guideline_workspace_verification.md'
purpose: 'Standards-input proposal presenting the high-level architectural design for the IMPLEMENTATION artifact family, including subtype taxonomy, governance rules, vertical integration impacts, and a draft exemplar for client review at GATE-001.'
consumers:
  - 'T104-PH001-ST008-AC001.3-GATE-001'
---

# PROPOSAL: Standards Input - IMPLEMENTATION Artifact Family Architecture

## I. PURPOSE

- Proposal objective: Present the high-level architectural design for a new `IMPLEMENTATION` artifact family within the workspace suite, as input to the GATE-001 client decision on artifact model resolution.
- Input scope: Family definition, subtype taxonomy, governance rules, vertical integration impacts on `workspace_documentation_rules.md` and companion guidelines, draft exemplar, and non-remediation use case assessment. This proposal does not author the actual guideline or templates; that work is scoped to post-GATE-001 activities.
- Target standards: `workspace_documentation_rules.md` (section 3 artifact inventory, section 7 workflow chain, section 8 role matrix), `guideline_workspace_plan.md` (section 6 task step rules), `guideline_workspace_verification.md` (revision-checklist integration, deferred to future session).
- Relationship to gate-disposition proposal: This standards-input proposal is a companion artifact to `proposal_T104-PH001-ST008-AC001.3-GATE-001_gir-disposition-package.md`. It provides the architectural depth behind GIR-007 through GIR-011 in that proposal.

## II. CURRENT STATE SUMMARY

### A. Baseline

- The workspace suite currently has 9 artifact types registered in `workspace_documentation_rules.md` section 3: PLAN, ROADMAP, NOTES, ANALYSIS, VERIFICATION, PROPOSAL, DEV-REPORT, plus register/session variants for NOTES.
- The workflow chain defines two canonical sequences: implementation-backed and consultation-only.
- No existing artifact family is designed to hold detailed implementation specification between plan task authority and developer execution evidence.

### B. Problems / Gaps

| Gap ID | Category | Description | Impact |
|:--|:--|:--|:--|
| GAP-001 | workflow | No durable artifact contract for implementation detail between plan steps and dev-reports | Plan steps are intentionally lightweight; dense implementation detail has no formal home |
| GAP-002 | workflow | Live remediation artifact divergence across activities | AC009 uses verification-type checklist; AC003 uses analysis-type checklist; same purpose, different families |
| GAP-003 | workflow | Plan guideline section 6.L recycle-loop task placement conflicts with Directive B | Current rule places remediation tasks after the gate; Directive B requires them above |
| GAP-004 | governance | No standardized workflow for non-PASS gate outcomes beyond RECYCLE mechanics | Industry frameworks treat corrective-action records as distinct document types |
| GAP-005 | governance | Plan task steps lack a formal boundary rule when implementation detail exists elsewhere | Risk of drift between plan steps and any future implementation specification surface |

## III. PROPOSED CONVENTIONS

### A. Family Definition

| Convention ID | Rule | Rationale | Authority Link |
|:--|:--|:--|:--|
| CONV-001 | A new artifact family `IMPLEMENTATION` SHALL be registered in `workspace_documentation_rules.md` section 3 with file prefix `implementation_` | Provides a dedicated, semantically clean home for implementation specification detail. Industry-aligned (ISO 9001 CAR, PRINCE2 Exception Plan, PMBOK Corrective Action Log). | Comparative analysis v2.0.0 section 6.I recommendation |
| CONV-002 | The `IMPLEMENTATION` family SHALL have exactly two subtypes in Draft 1: `remediation_specification` and `task_specification` | Covers both gate-remediation and proactive implementation use cases. Extensible to future subtypes without structural change. | SES004-DEC002 (option b approved) |
| CONV-003 | Each subtype SHALL have a dedicated template: `template_workspace_implementation_remediation-specification.md` and `template_workspace_implementation_task-specification.md` | Multi-template posture follows the PROPOSAL family pattern (per `guideline_workspace_proposal.md` section 3). | PROPOSAL archetype taxonomy precedent |
| CONV-004 | A single guideline `guideline_workspace_implementation.md` SHALL govern all subtypes | Consistent with the one-guideline-per-family pattern used by VERIFICATION, DEV-REPORT, ANALYSIS, PROPOSAL. | Workspace documentation rules section 5 pattern |
| CONV-005 | `IMPLEMENTATION` artifacts SHALL be placed in `<AC>/implementation/` directories (per P-STD-004 Convention 4, on-demand) | Follows the existing type-subdirectory pattern used by `verification/`, `proposal/`, `analysis/`, `dev-report/`. | P-STD-004-CLAUSE-003F |

### B. Subtype Taxonomy

#### 1. `remediation_specification`

| Attribute | Value |
|:--|:--|
| Trigger | Gate verdict of `RECYCLE` (any gate type: implementation-backed or consultation-only) |
| Purpose | Detailed implementation specification for flipping gate findings from RECYCLE to PASS |
| Author | `LLM_Consultant` |
| Consumer | `LLM_Developer` (execution), `LLM_Reviewer` (re-assessment input) |
| Template | `template_workspace_implementation_remediation-specification.md` |
| Lifecycle | Created after RECYCLE verdict -> consumed during remediation execution -> version-bumped if scope changes -> closed when gate re-assessment passes |
| Relationship to Verification Revision-Checklist | Complementary. Revision-checklist = "what the reviewer found needs fixing" (reviewer-owned). Remediation specification = "how to fix it in detail" (consultant-owned). The remediation specification MUST reference the governing verification's findings by ID. Open question: whether IMPLEMENTATION can replace the revision-checklist entirely (routed to future session per SES004-DEC006). |
| Relationship to Plan | Plan task register creates a remediation task (per section 6.K recycle re-entry block). The task's steps reference this artifact for detail. Plan retains authority; this artifact provides depth. |

#### 2. `task_specification`

| Attribute | Value |
|:--|:--|
| Trigger | Task complexity exceeds plan-step capacity (proactive, not remediation-driven) |
| Purpose | Detailed implementation specification for complex tasks where plan-level steps are insufficient for developer execution |
| Author | `LLM_Consultant` or `LLM_Planner` |
| Consumer | `LLM_Developer` (execution) |
| Template | `template_workspace_implementation_task-specification.md` |
| Lifecycle | Created during task planning or after plan amendment -> consumed during developer execution -> version-bumped if scope changes -> closed when task completes |
| Relationship to Plan | Plan task register references this artifact in the Action column or as a deliverable. Plan steps become high-level summaries pointing to this artifact for depth. |

### C. Governance Rules (Universal Across Subtypes)

| Convention ID | Rule | Rationale |
|:--|:--|:--|
| CONV-006 | `IMPLEMENTATION` artifacts SHALL NOT contain a GDR section. GDR remains exclusively in `gate_disposition` proposals. | Prevents GDR duplication and decision-authority confusion |
| CONV-007 | `IMPLEMENTATION` artifacts SHALL include mandatory frontmatter backlinks: `plan_reference`, `task_id` or `gate_id`, and triggering artifact reference (`verification_reference` or `proposal_reference` depending on subtype). | Authority-chain traceability |
| CONV-008 | `IMPLEMENTATION` artifacts SHALL include an explicit audience/authority preamble distinguishing them from plan authority and proposal decision authority. | Addresses authority-chain clarity concern (GAP-005 in comparative analysis) |
| CONV-009 | For gate remediation scenarios (`remediation_specification`), the `IMPLEMENTATION` artifact SHALL exist as a formal task above the gate in the task register per Directive B. | Directive B: uniform treatment across gate types |
| CONV-010 | One `IMPLEMENTATION` artifact per logical implementation scope (task-ID or gate-remediation-cycle scoping). Multiple related tasks within the same remediation cycle MAY share a single artifact. | Prevents artifact proliferation; task-ID scoping per client direction |
| CONV-011 | Plan task steps SHALL be described at high-level summary only when an `IMPLEMENTATION` artifact exists for that task. The plan step SHALL reference the artifact path. | Prevents drift between plan and implementation surfaces; per client direction |

### D. Three-Surface Authority Model

#### Gate remediation workflow

| Surface | Owner | Role | Content |
|:--|:--|:--|:--|
| Plan Task Register | LLM_Consultant/Planner | Authority | WHAT work is tracked, WHO owns it |
| IMPLEMENTATION artifact | LLM_Consultant | Specification | HOW to execute the work in detail |
| Verification Revision-Checklist | LLM_Reviewer | Evidence | WHAT the reviewer found wrong |
| Dev-Report | LLM_Developer | Execution evidence | WHAT was done |

#### Proactive task specification workflow

| Surface | Owner | Role | Content |
|:--|:--|:--|:--|
| Plan Task Register | LLM_Consultant/Planner | Authority | WHAT work is tracked, WHO owns it |
| IMPLEMENTATION artifact | LLM_Consultant/Planner | Specification | HOW to execute the work in detail |
| Dev-Report | LLM_Developer | Execution evidence | WHAT was done |

### E. Compatibility Notes

- The `IMPLEMENTATION` family follows the same structural patterns as existing families: dedicated prefix, type subdirectory, frontmatter conventions, guideline + template(s).
- The P-STD-004 naming rules extend naturally to the new family.
- The workspace suite is in Draft 1, the lowest-cost moment to add foundational components.
- Forward-only adoption: no retroactive migration of existing ad-hoc remediation artifacts (AC009 revision-checklist, AC003 remediation-checklist) is required. These remain valid as interim artifacts under their respective activities.

## IV. DECISION REQUESTS

| Decision ID | Prompt | Options | Recommendation | Owner |
|:--|:--|:--|:--|:--|
| DEC-001 | Confirm creation of the `IMPLEMENTATION` artifact family with the proposed family definition | (a) Accept (b) Modify | (a) | Client |
| DEC-002 | Confirm the two-subtype taxonomy: `remediation_specification` + `task_specification` | (a) Accept (b) Add subtypes (c) Modify | (a) | Client |
| DEC-003 | Confirm the 6 universal governance rules (CONV-006 through CONV-011) | (a) Accept (b) Modify specific rules | (a) | Client |
| DEC-004 | Confirm plan guideline integration: high-level-only steps when IMPLEMENTATION artifact exists (CONV-011) | (a) Accept (b) Modify | (a) | Client |
| DEC-005 | Route revision-checklist replacement question to future session | (a) Route to future (b) Resolve now | (a) | Client |
| DEC-006 | Confirm epic T104J (IMPLEMENTATION Standardization) registration in SPS upon GATE-001 approval | (a) Accept (b) Defer | (a) | Client |

## V. IMPACT AND RISKS

### A. Impact Assessment

- Positive outcomes: dedicated implementation detail surface, cleaner authority chain, less plan drift, reusable subtype taxonomy, easier downstream automation.
- Tradeoffs: one new family adds governance surface area, requires two templates and one guideline, and introduces a new cross-artifact backlink convention.

### B. Vertical Integration Sketch

#### `workspace_documentation_rules.md` section 3 - New Row

| Artifact Type | File Prefix | Purpose | Template | Guideline |
|:--|:--|:--|:--|:--|
| IMPLEMENTATION | `implementation_` | Detailed implementation specification: remediation specifications (gate RECYCLE response), task specifications (complex implementation detail) | `template_workspace_implementation_<subtype>.md` | `guideline_workspace_implementation.md` |

#### `workspace_documentation_rules.md` section 7 - Workflow Chain Updates

- Implementation-backed (updated):
  `ROADMAP -> PLAN -> NOTES / ANALYSIS -> implementation deliverables -> DEV-REPORT -> VERIFICATION -> [IMPLEMENTATION where RECYCLE] -> PROPOSAL (GDR) -> SPS / downstream`
- Consultation-only (updated):
  `ROADMAP -> PLAN -> NOTES / ANALYSIS -> [IMPLEMENTATION where needed] -> PROPOSAL (GDR) -> downstream`
- Proactive task specification:
  `ROADMAP -> PLAN -> [IMPLEMENTATION task_specification] -> implementation deliverables -> DEV-REPORT -> VERIFICATION -> PROPOSAL (GDR) -> downstream`
- New inter-artifact linkage rule:
  `IMPLEMENTATION provides detailed specification depth; it does not hold work authority (that belongs to PLAN) or decision authority (that belongs to PROPOSAL GDR)`

#### `workspace_documentation_rules.md` section 8 - Role-to-Artifact Ownership Matrix - New Row

| Artifact Type | Author | Reviewer | Approver / Decision Owner | Primary Consumer |
|:--|:--|:--|:--|:--|
| IMPLEMENTATION | LLM_Consultant (remediation_specification); LLM_Consultant or LLM_Planner (task_specification) | Reviewer consumes as re-assessment input | Client where gated | Developer, Reviewer |

### C. Non-Remediation Use Case Assessment

- `task_specification` is required because some execution work exceeds plan-step capacity but is not tied to gate remediation.
- The subtype supports complex proactive work without forcing every detailed implementation sequence through a remediation framing.
- This keeps the family useful outside gate recovery while preserving a single governance model.

### D. Revised Comparative Impact

| Criterion | Path B (revised) | Path C (revised) | Change from v2.0.0 |
|:--|:--|:--|:--|
| C4: Audience Alignment | 5 (unchanged) | 2 (was 3) | Three audience profiles in PROPOSAL family |
| C5: Extensibility | 5 (unchanged) | 3 (was 4) | Developer/planner-facing subtypes strain PROPOSAL's client-facing posture |
| C7: Anti-Drift Posture | 5 (unchanged) | 2 (was 3) | Three additional subtypes -> severe drift risk |
| C9: Authority-Chain Clarity | 5 (unchanged) | 2 (was 3) | 4+ archetypes in PROPOSAL makes authority chain unreadable |
| Estimated totals | 4.44 | ~3.40 (was 3.88) | B-C gap widens from 0.56 to ~1.04 |

### E. Downstream Implementation Requirements

| Work Item | Scope | Where | Status |
|:--|:--|:--|:--|
| TK005 (existing, scope expanded) | Prepare amendment package inputs: family definition, subtype taxonomy, template sketches, guideline outline, documentation rules row, plan guideline section 6.L amendment, analysis informative-only rule | AC001.3 | `planned` |
| New Activity in ST008 | Author `guideline_workspace_implementation.md` + 2 subtype templates + cross-check against all authority surfaces (following ST005 AC006/AC007/AC008 pattern) | ST008 | `planned` (post-GATE-001) |
| Epic T104J registration | Register IMPLEMENTATION Standardization epic in SPS | `sps_T104-CWS.md` | Administrative action upon GATE-001 approval |
| Plan guideline amendment | section 6.L + section 4 step rules | `guideline_workspace_plan.md` | `planned` (post-GATE-001) |
| Documentation rules update | section 3/7/8 | `workspace_documentation_rules.md` | `planned` (post-GATE-001) |

### F. T104J Epic Scaffold

#### Epic Header

| Field | Value |
|:--|:--|
| epic_id | `T104J` |
| epic_code | `IMPLEMENTATION` |
| epic_title | `Implementation Standardization` |
| epic_type | `new` |
| epic_status | `draft` |
| epic_owner | `LLM_Consultant` |

#### Purpose and Scope

- Purpose: register the IMPLEMENTATION family as a governed workspace surface after GATE-001 approval.
- In scope: family definition, subtype taxonomy, templates, guideline, and vertical integration surfaces.
- Out of scope: retroactive migration of historic remediation artifacts, and any expansion beyond the approved two-subtype draft.

#### Inherited Considerations

- `T104J-ASSUM-001`: IMPLEMENTATION artifacts are expected at task or gate scope. If broader scope is needed, the subtype taxonomy may expand.
- `T104J-CON-001`: IMPLEMENTATION artifacts SHALL NOT hold work authority (PLAN) or decision authority (PROPOSAL GDR).
- `T104J-QG-001`: Every IMPLEMENTATION artifact MUST include mandatory frontmatter backlinks per CONV-007.

#### Governance and Roadmap

- `T104J-DEP-001`: `P-PH000-ST001-AC004` (P-STD-004): the `implementation_` prefix and `<AC>/implementation/` placement convention are expected to be codified. Draft 2 SHALL adopt P-STD-004 as authoritative.
- `T104J-IG-001`: Dynamic/Continuous Development Posture applies while the family is being introduced and stabilized.

#### Feature Register

| Feature ID | Feature | Status |
|:--|:--|:--|
| T104J-FEAT-001 | Family registration in workspace documentation rules | draft |
| T104J-FEAT-002 | Two subtype templates and shared guideline | draft |
| T104J-FEAT-003 | Plan boundary rule integration | draft |
| T104J-FEAT-004 | Verification guideline linkage for remediation specification | draft |

#### Epic Requirements

| ID | Requirement |
|:--|:--|
| T104J-IF-001 | Plan Task Register Interface: IMPLEMENTATION artifacts reference specific task IDs or gate IDs. |
| T104J-IF-002 | Verification Consumer Interface: For `remediation_specification`, the artifact references verification findings and is consumed during re-assessment. |
| T104J-RISK-001 | Boundary ambiguity with plan task steps must be controlled by CONV-011 and the plan guideline amendment. |

#### Epic Standards

- The epic must keep the family name distinct from the old `implementation_detail` wording.
- The epic must treat the two subtypes as the only Draft 1 normative shapes.

#### Epic Development Guidances

- Authors should prefer one shared guideline plus two subtype templates instead of duplicating governance rules in each subtype.
- Updates to the verification guideline remain deferred until the family exists and the live revision-checklist relationship can be reviewed in context.

#### Research, Notes, Issues, Risks

- Research: use the AC009 revision-checklist exemplar and the T104H/T104I epic structure as the baseline pattern.
- Notes: the epic should remain draft until GATE-001 approval.
- Issues: any new subtype request should be treated as a future amendment, not a Draft 1 expansion.
- Risks: boundary ambiguity and scope creep are the primary risks; both are mitigated by CONV-011 and the two-subtype cap.

### G. AC009 Draft Exemplar Appendix

#### Exemplar frontmatter sketch

**Important framing**: This appendix is illustrative only. The IMPLEMENTATION family is not yet formally defined. The exemplar shows what a `remediation_specification` artifact would look like if the family is approved.

| Field | Example |
|:--|:--|
| artifact_type | `IMPLEMENTATION` |
| implementation_type | `remediation_specification` |
| initiative_id | `P` |
| initiative_code | `PROGRAM` |
| phase | `0` |
| stream_id | `P-PH000-ST001` |
| activity_id | `P-PH000-ST001-AC009` |
| gate_id | `P-PH000-ST001-AC009-GATE-001` |
| task_id | `P-PH000-ST001-AC009-TK005` |
| version | `1.0.0` |
| date | `2026-03-19` |
| status | `draft` |
| author | `LLM_Consultant` |
| decision_owner_role | `Client` |
| plan_reference | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/plan_P-PH000-ST001-AC009.md` |
| verification_reference | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/verification/verification_P-PH000-ST001-AC009_gate-001_revision-checklist.md` |
| proposal_reference | `[gate_disposition proposal path]` |
| purpose | `Remediation specification for AC009 GATE-001 recycle - translates external-review findings into implementation-ready corrective-action detail.` |

#### Exemplar content structure

```markdown
# IMPLEMENTATION (Remediation Specification): GATE-001 Remediation - P-PH000-ST001-AC009

## I. PURPOSE & AUTHORITY
- Purpose: [what this remediation specification covers]
- Authority chain: Plan authorizes work (task_id) -> This artifact specifies HOW -> Dev-report records execution -> Verification re-assesses
- Audience: LLM_Developer (primary), LLM_Reviewer (re-assessment input)
- This artifact does NOT hold a GDR. Gate decision is recorded in the gate_disposition proposal.

## II. REMEDIATION SCOPE
- Gate: [gate_id]
- Trigger: RECYCLE verdict from [verification_reference]
- Governing plan task: [task_id]
- Findings addressed: [list of FINDING-### IDs from verification]

## III. REMEDIATION ITEMS
### REM-001 - [Title from REV-001]
| Field | Detail |
|:--|:--|
| Finding Reference | [link to FINDING-### in verification] |
| Implementation Detail | [detailed HOW - what the developer must do] |
| Expected Format | [exact schema, structure, output format] |
| Acceptance Criteria | [what the reviewer will check during re-assessment] |
| Resolution Status | `open` |

[Repeat for each remediation item - use 2-3 items from the AC009 revision-checklist to demonstrate the pattern]

## IV. IMPLEMENTATION SEQUENCE
[Recommended execution order for the remediation items]

## V. REFERENCES
[Standard references table]

## VI. CHANGELOG
[Standard changelog]
```

#### Key differences from the existing revision-checklist

| # | Difference |
|:--|:--|
| 1 | Different `artifact_type` (`IMPLEMENTATION` vs `VERIFICATION`) |
| 2 | Different author role boundary (consultant-owned vs reviewer-owned) |
| 3 | Different audience framing (developer-facing implementation spec vs reviewer-facing finding translation) |
| 4 | Mandatory authority-chain preamble in section I |
| 5 | Mandatory frontmatter backlinks to plan, verification, and proposal |
| 6 | No GDR section |

## VI. REFERENCES

| Document | Path |
|:--|:--|
| Governing Plan | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.3/plan_T104-PH001-ST008-AC001.3.md` |
| Supporting Analysis | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.3/analysis/analysis_T104-PH001-ST008-AC001.3_remediation-artifact-type-comparison.md` |
| AC009 Revision Checklist Exemplar | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/verification/verification_P-PH000-ST001-AC009_gate-001_revision-checklist.md` |
| SPS Registry | `prompt/artifacts/tasks/T104/ssot/sps_T104-CWS.md` |
| Gate-Disposition Proposal | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.3/proposal/proposal_T104-PH001-ST008-AC001.3-GATE-001_gir-disposition-package.md` |
| Verification Guideline | `prompt/templates/consultant/workspace/guideline_workspace_verification.md` |
| Plan Guideline | `prompt/templates/consultant/workspace/guideline_workspace_plan.md` |
| Documentation Rules | `prompt/templates/consultant/workspace/workspace_documentation_rules.md` |

## VII. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.1.0 | 2026-03-19 | Amendment | Expanded the standards-input proposal to the full IMPLEMENTATION family model. Added the revised comparative-impact table, downstream implementation requirements, complete T104J scaffold, and a detailed AC009 exemplar appendix. Normalized the live package language to the approved two-subtype architecture. |
| v1.0.0 | 2026-03-19 | Initial | Standards-input proposal for IMPLEMENTATION family architecture. Covers family definition, two-subtype taxonomy, governance rules, authority model, vertical integration sketch, non-remediation use cases, revised comparative impact, downstream requirements, T104J epic scaffold, and AC009 draft exemplar appendix. |
