---
artifact_type: 'PROCEDURAL_GUIDELINE'
domain: 'consultant_workspace'
topic: 'verification_authoring'
version: '1.7.0'
date: '2026-03-16'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
template_reference: 'prompt/templates/consultant/workspace/template_workspace_verification.md'
analysis_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST005/analysis/analysis_T104-PH001-ST005-AC005_verification-pattern-audit.md'
---

# Verification Procedural Guideline (Consultant Workspace)

## I. PURPOSE

This guideline defines the authoring rules and gate-oriented verification workflow for VERIFICATION workspace artifacts. It provides a standardized framework for independent cross-verification using an evidence-first methodology for implementation-backed gate reviews. This guideline is intended for all LLM roles involved in producing or consuming verification artifacts.

**Cross-reference**: See `guideline_workspace_plan.md §VI` for the structure of gates within plans.
**Status notice**: This is a dynamic Draft 1 (exemplar-derived); normative binding is deferred to T104H.

## II. ROLE BOUNDARY

The following roles interact with verification artifacts:

- **LLM_Reviewer** (preferred): Primary author of gate verification artifacts. Performs independent cross-verification using evidence-first methodology.
- **LLM_Consultant**: Permitted for implementation-backed commissioning assessments and readiness reviews. Consultation-only gate assessments belong in `ANALYSIS`, not `VERIFICATION`.
- **Client**: Decision owner. All gate decisions require Client approval signal, which is recorded in the proposal's Gate Decision Record (GDR) section.
- **LLM_Developer**: NOT an author of verification artifacts. Developer-produced evidence (dev-reports, execution logs) serves as verification INPUT, not verification itself.

Note: Role definitions are informative pending T101 (Role Standardization).

## III. VERIFICATION WORKFLOW

This workflow applies only when a gate reviews developer-mutated deliverables or other implementation-backed outputs. Consultation-only gates use `ANALYSIS` + `PROPOSAL` surfaces instead and MUST NOT produce `VERIFICATION` artifacts.

Verification follows a "TK-before-gate" pattern:

1. **Plan defines gate**: The gate appears in the task register with entry/exit criteria per `guideline_workspace_plan.md §VI.C`.
2. **Upstream implementation tasks complete**: All developer-owned tasks listed in the gate's entry criteria reach terminal status.
3. **DEV-REPORT is authored**: A developer-owned `DEV-REPORT` task captures the bounded implementation evidence and handoff package for review.
4. **Verification task starts**: A reviewer-owned task (e.g., `TK006`) in the task register is assigned to produce verification evidence. Gate status transitions to `in_progress`.
5. **Reviewer produces verification artifact**: Following this guideline's evidence rules (§V), findings schema (§VI), and template structure.
6. **Reviewer issues verdict**: One of the verdict values defined in §VIII.
7. **Client reviews**: Client examines the verification artifact (entry criteria assessment, findings, recommendation).
8. **Client issues decision**: Decision recorded in the `gate_disposition` proposal's Gate Decision Record (GDR). Gate status transitions per §VIII mapping.
9. **Downstream enforcement**: Tasks with `Depends On: GATE-###` MUST verify that the gate's `gate_disposition` proposal contains a populated GDR with APPROVE or APPROVE WITH CONDITIONS before starting.

**Mandatory Rule**: The separation of verification task (evidence production) from gate (decision) is mandatory. Verification evidence MUST NOT be produced as part of the gate event itself.

**Plan-level positioning**: In implementation-backed gates, the verification task SHOULD appear as part of the Gate-Readiness Stack — after the DEV-REPORT task and before the gate-disposition proposal task. Consultation-only gates omit verification entirely. For the full pattern, see `guideline_workspace_plan.md` §VI.L.

## IV. VERIFICATION PACKAGE

### A. Verification Package (Scope Decomposition)

- Complex gate reviews MAY be decomposed into multiple verification artifacts at the same gate.
- One artifact is designated **primary**; others are **supplementary**.
- Primary artifact: `verification_<activity-UID>_gate-###.md`
- Supplementary artifact: `verification_<activity-UID>_gate-###_<aspect>.md` (e.g., `_convention-compliance.md`, `_commissioning-readiness.md`)
- Frontmatter linking: Primary lists supplementary paths; supplementary references primary via `primary_verification` frontmatter key.
- The primary artifact contains the Gate Recommendation section. Supplementary artifacts contain aspect-specific findings that feed into the primary recommendation.
- When to decompose: When a gate review covers multiple independent verification dimensions (e.g., technical correctness + convention compliance + commissioning readiness).
- **Revision checklist use case**: When a `RECYCLE` verdict involves complex Situation A deficiencies where the primary verification's findings alone do not provide sufficient developer-actionable detail for rework execution, the reviewer SHOULD produce a supplementary verification file with aspect `revision-checklist` (e.g., `verification_<activity-UID>_gate-###_revision-checklist.md`). This supplementary file translates verification findings into developer-executable revision specifications.


### B. Re-assessment (Temporal Iteration)

- When rework is completed after a RECYCLE verdict, the existing verification artifact(s) are **version-bumped**, NOT replaced by new files.
- Re-assessment evidence is added in a new section or updates to existing sections, with the changelog recording the re-assessment.
- This is distinct from Verification Packages: packages are scope decomposition (parallel aspects); re-assessment is temporal iteration (sequential rework cycles).

**Rule**: Do NOT create supplementary files for re-assessment. Use version bumps. Do NOT use version bumps for scope decomposition. Use supplementary files.

## V. EVIDENCE RULES

### A. Evidence-First Methodology

- Reviewers MUST independently read/verify deliverable artifacts.
- Reviewers MUST NOT rely solely on producer claims (dev-reports, developer verification) without independent confirmation.
- Evidence-first means: read the artifact, run the check, record what was observed.
- Producer evidence (dev-reports, developer checklists) serves as navigation input, not as verification output.

### B. Evidence Set Section

- Every verification artifact MUST include an Evidence Set section (§II of template) listing all artifacts reviewed.
- Group by task/deliverable with repo-relative paths.
- Include governance references (plan, proposal, standards) used as the verification baseline.

### C. Per-Task Verification Tables

- Verification checklist MUST be organized by task or criterion group.
- Each group uses the table schema: `# | Check | Expected | Observed Evidence | Result`
- `Result` values: `PASS`, `FAIL`, `N/A`
- `Observed Evidence` MUST include specific evidence (line numbers, grep results, file paths), not general assertions.

## VI. FINDINGS SCHEMA

### A. Finding Types

| Type | Prefix | Definition | Severity Required? |
|:--|:--|:--|:--|
| **Finding** | `FINDING-###` | A non-conformance or deficiency requiring action | Yes |
| **Observation** | `OBS-###` | An informational item, process improvement suggestion, or non-blocking note | No (always informational) |

### B. Severity Taxonomy (for FINDING-### only)

| Severity | Definition | Gate Impact |
|:--|:--|:--|
| **Blocking** | Prevents gate passage. Must be resolved before PASS verdict. | Verdict = RECYCLE |
| **Major** | Significant quality or compliance gap. Should be resolved before gate passage unless explicitly waived. | May result in RECYCLE or CONDITIONAL PASS |
| **Moderate** | Quality improvement needed but does not block gate passage. | CONDITIONAL PASS (condition tracked) |
| **Low** | Minor quality item. May be deferred. | PASS or CONDITIONAL PASS |
| **Preventive** | Not a current defect but a risk that could cause future issues if unaddressed. | PASS (recommendation tracked) |

### C. Finding Required Fields

Each `FINDING-###` MUST include:

| Field | Content |
|:--|:--|
| Severity | One of: Blocking, Major, Moderate, Low, Preventive |
| Source | Where the finding was discovered (task check, section, artifact) |
| Description | What the issue is |
| Classification | Situation A (deliverable deficiency) or Situation B (scope gap) — per §VII |
| Required Action | What must be done to resolve |
| Owner | Developer (remediation) or Client (decision) |
| Resolution Status | `open`, `resolved`, `accepted` (deferred), `waived` |
| Resolution Date | Date when resolution was recorded (blank if open) |

### D. Observation Required Fields

Each `OBS-###` MUST include: Description, Context, Recommendation (optional).

## VII. GATE OUTCOME REWORK PATHS

### A. Situation A — Deliverable Deficiency

1. **Definition**: The requirement was correctly specified in the approved plan or standard, but the deliverable fails to meet it.
2. **Path**: Reviewer issues FINDING-### (Situation A). Developer performs rework.
3. **Handoff rule**: The verification artifact's findings register IS the rework handoff. No plan amendment required. No additional artifact needed. The developer reads the finding, understands the required action, and performs rework under the same task ID.

**Complex revision guidance**: When findings involve multiple deliverable deficiencies with specific format or schema requirements (e.g., missing matrices with defined column structures, missing lifecycle models with paired outputs), the findings register alone may not provide sufficient implementation detail. In such cases:
- The reviewer SHOULD produce a **supplementary verification file** (per §IV.A, aspect: `revision-checklist`) that translates each blocking finding into explicit revision items.
- Each revision item MUST include: (1) finding reference (link to FINDING-### in primary verification), (2) revision deliverable (what the developer must produce), (3) expected format (exact schema, columns, or structure — derived from the governing brief, plan, or standard), and (4) acceptance criteria (what the reviewer will check during re-assessment).
- The supplementary file is a scope decomposition artifact (§IV.A), NOT a re-assessment artifact (§IV.B). It is authored once alongside the primary verification and updated during re-assessment only to track resolution status.
- The primary verification remains the gate evidence and verdict surface. The supplementary revision checklist is a developer handoff surface.


### B. Situation B — Scope Gap

1. **Definition**: The deliverable is deficient because the upstream plan or standard failed to specify the necessary requirement or constraint.
2. **Path**: Reviewer issues FINDING-### (Situation B). Role owner amends the plan. Developer executes the amendment.
3. **Handoff rule**: The plan MUST be amended before the developer has authority to act. The verification artifact identifies the gap; the plan amendment provides the developer's formal work authority via a new tracked task or sub-task (`TK###` / `TK###.n`) per `guideline_workspace_plan.md §IV.E`. The verification artifact MUST reference the plan amendment.
4. **Recycle-loop rule**: When the governing gate verdict is `RECYCLE`, the plan amendment MUST attach the remediation work to the same gate's reassessment loop. The gate remains the same gate ID; the amendment does not create a derived gate ID for re-review.

### C. Cross-Boundary Handoff

When rework involves a different role owner or different stream than the original work, a communication brief (`comm_` prefix) MAY accompany the verification artifact or plan amendment to formally hand off rework to the new owner. This is OPTIONAL and used only when the ownership boundary is crossed.

### D. Decision Test Table

| Question | Answer | Situation | Handoff Mechanism | Plan Change? |
|:--|:--|:--|:--|:--|
| Did the plan specify this requirement? | Yes | A (Deficiency) | Verification finding only | No |
| Did the plan specify this requirement? | No | B (Scope Gap) | Plan amendment → sub-task (TK###.n) | Yes |
| Does rework cross ownership boundary? | Yes | A or B + Cross-boundary | `comm_` brief optional | Depends on A/B |

### E. Plan Authority Principle

**Situation B clarification**: The amendment mechanism for scope gaps follows `guideline_workspace_plan.md §IV.E`. The plan MAY introduce either a new tracked Task (`TK###`) or a dotted Sub-Task (`TK###.n`) depending on the decomposition need; neither creates task-level directory scope.

The plan is the developer's work authority. The verification artifact identifies WHAT needs rework and WHAT outcome is required. The plan authorizes HOW to do it and UNDER WHICH TASK. For Situation A, the plan already covers the scope (no amendment needed). For Situation B, the plan MUST be amended first.

## VIII. VERDICT TAXONOMY

### A. Reviewer Verdicts

| Verdict | Definition | Gate Status After |
|:--|:--|:--|
| **PASS** | All entry/exit criteria met. No blocking findings. | → `completed` (pending GDR) |
| **CONDITIONAL PASS** | All critical criteria met. Non-blocking conditions documented. | → `completed` (pending GDR; conditions tracked) |
| **PASS WITH DEFERRALS** | Criteria met for current scope. Intentional deferrals documented. | → `completed` (pending GDR; deferrals tracked) |
| **RECYCLE** | Blocking finding(s) identified. Rework required. Re-present at same gate. | → stays `in_progress` |
| **FAIL** | Terminal. Work abandoned or unrecoverable. | → `failed` |

**Rules**:
- Verdict MUST appear in the Gate Recommendation section of the verification artifact.
- Verdict MUST be one of the five enumerated values (no variants).
- CONDITIONAL PASS conditions MUST be enumerated in the Gate Recommendation.
- PASS WITH DEFERRALS deferrals MUST reference the owning activity/stream.
- RECYCLE recommendations MUST explicitly identify the same gate ID to be reassessed, the remediation task/sub-task set required before re-review, and the downstream tasks that remain blocked.

### B. Client Decisions (in GDR)

| Decision | Definition |
|:--|:--|
| **APPROVE** | Accept PASS verdict. Gate closed. |
| **APPROVE WITH CONDITIONS** | Accept with conditions. Gate closed; conditions tracked. |
| **RECYCLE** | Agree rework needed. Gate stays open. |
| **REJECT** | Terminate gate. Work killed/redirected. |

**Rule**: Client MAY override reviewer verdict (e.g., REJECT a PASS if Client identifies concerns the reviewer missed). Override MUST be documented with rationale in the GDR.

## IX. RE-ASSESSMENT VERSIONING

- After a RECYCLE verdict and completed rework, the verification artifact is **version-bumped** (e.g., v1.0.0 → v2.0.0 for major re-assessment).
- The changelog records: re-assessment date, findings addressed, new verdict.
- New or updated findings sections are added/modified. Resolved findings have their Resolution Status updated to `resolved` with a Resolution Date.
- If the verification TASK methodology needs rework (not just the assessed deliverable), a sub-task (TK###.n) is created for the verification task, following `guideline_workspace_plan.md §VII` (Sub-Activity Rules).
- Re-assessment versioning applies to all artifacts in a Verification Package (primary + supplementary). Version bumps SHOULD be coordinated.
- Re-assessment remains tied to the same governing gate ID; `RECYCLE` does not create a new gate identity for the subsequent review cycle.

## X. GATE DECISION RECORD (GDR) — CROSS-REFERENCE

The Gate Decision Record (GDR) specification, lifecycle, and enforcement rules are defined in `guideline_workspace_proposal.md` §VII (Gate Semantics & Gate Decision Record).

The verification artifact's role at a gate is to provide evidence and a reviewer verdict (§VIII Verdict Taxonomy, §VII Gate Recommendation template section). The GDR — which records the client's decision — is hosted in the `gate_disposition` proposal artifact, not in the verification artifact.

**Cross-reference**: For GDR field specification, lifecycle, and enforcement rules, see `guideline_workspace_proposal.md` §VII.C–E.

**Historical note**: Prior to v1.1.0, this guideline contained the full GDR specification in §X. That specification has been migrated to the proposal guideline to consolidate GDR ownership in the consultant-owned gate package per T104-PH001-ST008-AC001 Option B approval.

**Task decomposition clarification**: Any verification-driven task rework that needs new tracked authority follows `guideline_workspace_plan.md §IV.E` (Task Decomposition Rules), not the Sub-Activity rules in `§VII`.

## XI. NAMING CONVENTION

**File naming**:
- Primary: `verification_<activity-UID>_gate-###.md`
- Supplementary: `verification_<activity-UID>_gate-###_<aspect>.md`
- `<aspect>` is a kebab-case descriptor (e.g., `convention-compliance`, `commissioning-readiness`, `p-migration-readiness`)

**Directory placement**:
- `verification/` is an activity-level type subdirectory: `AC###/verification/`
- Per P-STD-004 Convention 4: created on-demand when gate verification files are produced

**Frontmatter conventions**:
- `gate_id`: Full gate UID (e.g., `T104-PH001-ST007-AC004-GATE-001`)
- `verification_type`: Descriptor (e.g., `GATE_REVIEW`, `commissioning_readiness`, `convention_compliance`)
- `primary_verification`: Repo-relative path to primary artifact (supplementary artifacts only)

## XII. TEMPLATE INVENTORY

- **Template**: `prompt/templates/consultant/workspace/template_workspace_verification.md`
- **What**: Defines the required structure for gate verification artifacts.
- **Why**: Ensures consistent section ordering, findings schemas, verdict formats, and GDR placement.
- **When**: Use when producing any gate verification artifact.
- **How**: Copy the template, fill in frontmatter, populate sections per this guideline's rules.

## XIII. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.7.0 | 2026-03-16 | Amendment | Clarified that VERIFICATION applies only to implementation-backed gates after developer work and DEV-REPORT handoff. Consultation-only gates now explicitly use `ANALYSIS` + `PROPOSAL` instead of `VERIFICATION`. Source: P-PH000-ST002-AC002 Gate 001 consultation. |
| v1.6.0 | 2026-03-15 | Amendment | §III: Added Gate-Readiness Stack cross-reference to `guideline_workspace_plan.md` §VI.L for plan-level positioning of verification tasks in the pre-gate sequence. Source: T104-PH001-ST008-AC001.2. |
| v1.5.0 | 2026-03-15 | Amendment | Added revision-checklist guidance to §IV.A and §VII.A. For complex Situation A deficiencies, reviewers SHOULD produce a supplementary verification file (aspect: revision-checklist) containing explicit revision items with finding references, expected formats, and acceptance criteria. |
| v1.4.0 | 2026-03-12 | Amendment | Clarified RECYCLE handling across §VII, §VIII, and §IX. Situation B plan amendments now attach remediation to the same gate's reassessment loop, RECYCLE recommendations must name the same gate/remediation/downstream block set, and re-assessment versioning explicitly preserves the original gate ID. |
| v1.2.0 | 2026-03-05 | Maintenance | Resolved legacy GDR ownership references in §II, §III, and §IV. Workflow and role boundaries now correctly identify the proposal artifact as the GDR host. |
| v1.1.0 | 2026-03-04 | Amendment | §X (GDR) replaced with cross-reference to `guideline_workspace_proposal.md` §VII. Full GDR specification (field set, lifecycle, enforcement) migrated to proposal guideline per T104-PH001-ST008-AC001 Option B approval. Verification artifact retains Gate Recommendation (§VII template section) for reviewer verdict; GDR now hosted exclusively in gate_disposition proposals. |
| v1.0.0 | 2026-02-25 | Initial | Draft 1 (exemplar-derived). Covers: role boundary, TK-before-gate workflow, verification package, evidence rules, findings schema, gate outcome rework paths (migrated from guideline_workspace_plan.md §VI.G), verdict taxonomy, re-assessment versioning, GDR, naming convention. Source: T104-PH001-ST005-AC005-SES001 consultation. |
```
