---
artifact_type: 'PROCEDURAL_GUIDELINE'
domain: 'consultant_sps'
topic: 'ssot_sps_authoring'
version: '1.0.0'
date: '2026-02-01'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
template_reference: 'prompt/templates/consultant/sps/sps_structural_template.md'
---

# SPS SSOT Authoring Guideline (Consultant SPS)

## I. PURPOSE

Define the authoring rules for the SPS SSOT artifact so it remains consistent, toolable, and aligned with the consultancy operating model.

This guideline is the single source of truth for authoring the SPS template. The SPS structural template MUST remain a clean structural skeleton (no authoring comments or instructional prose).

## II. ADR TOUCHPOINTS (HIGH-LEVEL)

The SPS template and this guideline are governed by the following ADRs (ADR-ID only; specs are evolving):

| SPS Section / Concern | Relevant ADR IDs |
| --- | --- |
| SPS role + artifact boundary (SPS vs Request vs Concept vs Design) | `T102-ADR-001` |
| Canonical YAML header patterns (identity, status, dates, enums) | `T102-ADR-002` |
| Inheritance model + Inherited Considerations tables | `T102-ADR-003` |
<!-- | Decision record index conventions (where referenced/linked) | `T102-ADR-004` | -->
| ID taxonomy, formatting, and reference semantics | `T102-ADR-005` |
| Research index conventions (RES tables + link-don’t-duplicate) | `T102-ADR-006` |
| Issues & Risks table conventions | `T102-ADR-007` |
| Organisation baseline (Role Definitions + RACI stability) | `T102-ADR-008` |
| Governance Standards Specification | `T102-ADR-009` |

## III. TEMPLATE RULES (LOCKED)

1) The structural template is `prompt/templates/consultant/sps/sps_structural_template.md`.
2) The template MUST contain:
   - the YAML frontmatter block, and
   - `## III. CORE CONTENT` and its subsections only.
3) The template MUST NOT contain:
   - HTML comments (`<!-- ... -->`),
   - inline authoring instructions (including italicized “how to” prompts),
   - embedded decision bodies (ADR/STD bodies) beyond section/table skeletons.
4) All authoring guidance and explanatory content MUST live in this guideline.

## IV. CORE CONTENT AUTHORING RULES

### A. Problem Definition

#### 1. The Problem

- Describe the current gap in plain language.
- Avoid solutions and architectural decisions (those belong downstream).

#### 2. The Desired Outcome

- Describe the target future state and what “done” means at initiative scope.
- Keep this outcome at governance level (not story acceptance criteria).

#### 3. Business Case

- State the value, urgency, and consequences of not acting.

### B. Initiative Considerations

This section contains governance factors that apply across the initiative.

#### How to add an item (workflow)

1) Pick the right subsection using the boundary rules.
2) Create an ID with the correct prefix and counter for the initiative scope.
3) Keep each item atomic; one idea per item.
4) Keep items short and scannable (rule of thumb: ≤ 25 words unless a table is required).
5) Use the quick test for ambiguous classification:
   - if within our control and mandatory: Constraint
   - if external commitment/contract: Dependency

Examples (illustrative):
- `IID-CON-###` — Review SLA within 2 business days.
- `IID-ASSUM-###` — Client will use Markdown/YAML editors for co-authoring.
- `IID-QG-###` — End-to-end traceability is preserved across artifacts.
- `IID-DEP-###` — Planner layer can consume the handoff schema.
- `IID-IG-###` — Approvals are recorded in body, not YAML.
- `IID-NOTE-###` — Consider consolidating validation logs at epic level.

#### Item boundary rules (classification rubric)

- Assumption: believed true, not yet confirmed.
- Constraint: non-negotiable restriction.
- Quality Goal: measurable success signal at initiative scope.
- Dependency: external prerequisite or commitment.
- Interface: explicit handoff contract or external-facing boundary.
- Implementation Guidance: internal “how we author/operate” rules.
- Notes: contextual items, questions, and parking lot items.

#### ID conventions (initiative scope)

Use stable initiative-level IDs with the following prefixes:

- `IID-ASSUM-###`
- `IID-CON-###`
- `IID-QG-###`
- `IID-DEP-###`
- `IID-IF-###`
- `IID-STD-###`
- `IID-IG-###`
- `IID-RES-###`
- `IID-NOTE-###`
- `IID-ISSUE-###`
- `IID-RISK-###`

#### 1. Organization & Responsibilities

- Maintain a stable Role Definitions mapping and Governance RACI.
- Treat this as the organisation baseline for the initiative.

#### 2. Project Assumptions

- Keep assumptions atomic and testable where possible.

#### 3. Project Constraints

- Constraints are non-negotiable within the initiative scope.

#### 4. Quality Goals

- Prefer measurable and verifiable goals (avoid subjective-only goals).

#### 5. Dependencies

- Use this for prerequisites and external commitments.

#### 6. Interfaces

- Use this for handoff contracts and cross-role/cross-artifact agreements.

#### 7. Project Standards

- Standards are the enforceable registry entries for initiative governance.
- Keep standard statements concise; deeper rationale belongs in ADRs (not in STD bodies).

**STD Index schema (locked)**

`STD ID | Title | Status | Owner | Effective | Supersedes | Adopts | Verification | Reference`

Rule of thumb:
- `Adopts` points to exactly one canonical specification document (ADR or equivalent) that contains detailed rules.
- `Reference` lists the upstream IDs this standard relies on (do not duplicate their body text).

Legacy note:
- Some older SPS drafts used `GDR` indices inside SPS. Under the current operating model, enforceable governance uses `STD`, and architectural decisions are canonized in Concept as ADRs. See `T102-ADR-001`, `T102-ADR-004`.

#### 8. Project Guidances & Notes

- Guidance is “how-to”; it should reference governing standards/decisions rather than re-declaring them, containing `IG` and `INT` items at IID level.

- Use notes for context and parking lot items that are not (yet) promoted into governance IDs.

#### 9. Research

- Research entries are links-first: index research by `RES` ID and link to brief/report artifacts.

#### 10. Issues & Risks

- Issues are current blockers/gaps requiring action.
- Risks are potential negative outcomes requiring monitoring or mitigation.

### C. Epics & Breakdown

This section is the initiative’s Work Breakdown Structure (WBS) at the Epic level.

#### Decomposition principles

- Decompose by deliverable/capability, not by activity or role.
- A Feature is specified within a single Request artifact (which may contain multiple Stories).
- The SPS remains free of story-level acceptance criteria; requirements live downstream.

#### Decomposition method (authoring cues)

1) Decomposition Principles
- Split by deliverable/capability, not by activity or role.
- Each Feature SHOULD name an Owner, declare Dependencies and Interfaces (prefer IDs), and include a short Purpose statement.

2) Readiness & Exit Signals (visibility only)
- Ready → Request (feature-level, tracked in SPS): Purpose clear; Owner set; Dependencies/Interfaces listed by ID.
- Ready → Concept (feature-level, tracked in SPS): Request approved (source of truth is the Request).
- SPS tracks these states; detailed criteria live in downstream artifacts.

3) Status taxonomy (feature-level tracking)
- `proposed`, `in-discovery`, `in-request`, `approved`, `in-concept`, `in-delivery`, `done`, `parked`

4) Link & ID discipline
- Prefer repo-relative paths and stable anchors.
- Cross-epic dependencies SHOULD reference IDs; optional brief free-text notes may follow in parentheses.

5) Change control (epic/feature scope)
- Any change to the Feature Register SHOULD include a short traceable note explaining what changed, why, and impact.

#### Readiness and exit signals (tracking only)

- SPS tracks readiness states at high level; detailed gate criteria live downstream.
- Use the Feature/Epic status fields consistently to prevent drift.

#### Status taxonomy (Feature and registers)

Use stable status enums (do not invent new values locally).

#### Link and ID discipline

- Prefer repo-relative links and stable anchors.
- Cross-epic dependencies SHOULD reference IDs; optional brief free-text may follow.

#### Change control (epic/feature scope)

- Any change to the Epic dossier or Feature Register SHOULD be treated as a governance-impacting change (documented and traceable).

#### Separator recommendation (`---`)

Use `---` as a visual delimiter:
- between the Initiative WBS Map and the first Epic dossier, and
- between Epic dossiers when multiple epics are present.

Rationale: it materially improves scanability with minimal token overhead and does not introduce semantic drift.

#### Epic dossier structure (T102B-aligned)

Each Epic dossier MUST include all subsections (including `#####` subheadings) as defined in the SPS template:

- Purpose
- Scope
- Inherited Considerations
- Governance & Roadmap
- Feature Register
- Epic Requirements (Assumptions, Constraints, Quality Goals, Dependencies, Interfaces)
- Epic Standards
- Epic Development Guidances (Implementation Guidance, Integration Guidance)
- Research
- Notes
- Issues
- Risks

Subsection intent (authoring semantics):
- Purpose: business-language outcome; avoid solutioning.
- Scope: explicit boundaries (in/out); prevent accretion.
- Inherited Considerations: ID-only inheritance emphasis; do not restate parent bodies.
- Governance & Roadmap: phase/gate snapshot and authoritative ownership/approval framing.
- Feature Register: list of Epic features with canonical links for downstream work.
- Epic Requirements: epic-scoped E-IDs; keep atomic; link to evidence or research IDs when needed.
- Epic Standards: enforceable standards adopting canonical specs; keep obligation concise.
- Epic Development Guidances: non-normative “how-to”; reference governing IDs.
- Research: index-only; link to briefs/reports.
- Notes: context and parking lot; groom regularly.
- Issues/Risks: tracked items with owners/status, kept current.
