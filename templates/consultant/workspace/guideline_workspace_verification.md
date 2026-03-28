---
artifact_type: 'PROCEDURAL_GUIDELINE'
domain: 'consultant_workspace'
topic: 'verification_authoring'
version: '1.11.0'
date: '2026-03-25'
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

- **LLM_Reviewer** (preferred future-state primary): Primary verifier for gate verification artifacts. Performs independent cross-verification using evidence-first methodology.
- **LLM_Consultant**: Currently authorized secondary verifier under the temporary operating model. May author implementation-backed commissioning assessments and readiness reviews when the consultant is independent of the implementation-producing task for that cycle. Consultation-only gate assessments belong in `ANALYSIS`, not `VERIFICATION`.
- **Client**: Decision owner. All gate decisions require Client approval signal, which is recorded in the proposal's Gate Decision Record (GDR) section.
- **LLM_Developer**: NOT an author of verification artifacts. Developer-produced evidence (dev-reports, execution logs) serves as verification INPUT, not verification itself.

Note: Role definitions are informative pending T101 (Role Standardization).

## III. VERIFICATION WORKFLOW

This workflow applies only when a gate reviews developer-mutated deliverables or other implementation-backed outputs. Consultation-only gates use `ANALYSIS` + `PROPOSAL` surfaces instead and MUST NOT produce `VERIFICATION` artifacts.

Verification follows a "TK-before-gate" pattern:

1. **Plan defines gate**: The gate appears in the task register with entry/exit criteria per `guideline_workspace_plan.md §VI.C`.
2. **Upstream implementation tasks complete**: All developer-owned tasks listed in the gate's entry criteria reach terminal status.
3. **DEV-REPORT is authored**: A developer-owned `DEV-REPORT` task captures the bounded implementation evidence and handoff package for review.
4. **Verification task starts**: A verifier-owned task (e.g., `TK006`) in the task register is assigned to produce verification evidence. The verifier role is the plan-authorized role for the current operating model. Gate status transitions to `in_progress`.
5. **Verifier produces verification artifact**: Following this guideline's evidence rules (§V), findings schema (§VI), and template structure.
6. **Verifier issues verdict**: One of the verdict values defined in §VIII.
7. **Client reviews**: Client examines the verification artifact (entry criteria assessment, findings, recommendation).
8. **Client issues decision**: Decision recorded in the `gate_disposition` proposal's Gate Decision Record (GDR). Gate status transitions per §VIII mapping.
9. **Downstream enforcement**: Tasks with `Depends On: GATE-###` MUST verify that the gate's `gate_disposition` proposal contains a populated GDR with APPROVE or APPROVE WITH CONDITIONS before starting.

**Mandatory Rule**: The separation of verification task (evidence production) from gate (decision) is mandatory. Verification evidence MUST NOT be produced as part of the gate event itself.

**Plan-level positioning**: In implementation-backed gates, the verification task SHOULD appear as part of the Gate-Readiness Stack — after the DEV-REPORT task and before the gate-disposition proposal task. Consultation-only gates omit verification entirely. The verifier role used for that task is the plan-authorized role for the current operating model. For the full pattern, see `guideline_workspace_plan.md` §VI.L.

## IV. VERIFICATION PACKAGE

### A. Verification Package (Scope Decomposition)

- Complex gate reviews MAY be decomposed into multiple verification artifacts at the same gate.
- One artifact is designated **primary**; others are **supplementary**.
- Primary artifact: `verification_<activity-UID>_gate-###.md`
- Supplementary artifact: `verification_<activity-UID>_gate-###_<aspect>.md` (e.g., `_convention-compliance.md`, `_commissioning-readiness.md`)
- Frontmatter linking: Primary lists supplementary paths; supplementary references primary via `primary_verification` frontmatter key.
- The primary artifact contains the Gate Recommendation section. Supplementary artifacts contain aspect-specific findings that feed into the primary recommendation.
- When to decompose: When a gate review covers multiple independent verification dimensions (e.g., technical correctness + convention compliance + commissioning readiness).
- **Revision checklist use case**: Existing `revision-checklist` supplementary files remain valid historical artifacts, and reviewers MAY still use a supplementary verification file with aspect `revision-checklist` for bounded checklist-style elaboration when no separate remediation specification is required. For new complex `RECYCLE` cases that require a developer-executable remediation plan, reviewers SHOULD route the detailed handoff through an `IMPLEMENTATION remediation_specification` instead.

Verification package decomposition is reviewer-side scope decomposition. DEV-REPORT package decomposition, as defined by the DEV-REPORT package taxonomy in `guideline_workspace_dev-report.md`, is producer-side evidence packaging. The two decompositions are independent and MUST NOT be conflated.


### B. Re-assessment (Temporal Iteration)

- When rework is completed after a RECYCLE verdict, the existing verification artifact(s) are **version-bumped**, NOT replaced by new files.
- Re-assessment evidence is added in a new section or updates to existing sections, with `prompt/templates/consultant/workspace/changelog/changelog_guideline_workspace_verification.md` recording the re-assessment.
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
- For multi-report packages, enumerate in this order: primary DEV-REPORT, supplementary DEV-REPORTs, other task deliverables, governance references.
- Include governance references (plan, proposal, standards) used as the verification baseline.

### C. Multi-Report DEV-REPORT Intake

1. Read the primary DEV-REPORT first.
2. Confirm whether the primary report is a consolidated package by checking `consolidated_from`.
3. Enumerate every supplementary DEV-REPORT referenced by the package.
4. Read each supplementary DEV-REPORT in the execution order implied by the package or implementation history.
5. Compare the primary DEV-REPORT Executive Summary, Traceability Matrix, and Handoff sections against the supplementary evidence set.
6. Record any mismatch, omission, or broken package linkage as a finding or observation.

- The Evidence Set section MUST list the primary DEV-REPORT before any supplementary DEV-REPORTs.
- When a primary DEV-REPORT declares `consolidated_from`, the reviewer MUST verify that every referenced supplementary DEV-REPORT exists and is represented accurately in the primary report.
- The reviewer MUST NOT treat a consolidated DEV-REPORT as sufficient evidence if package completeness has not been checked.
- `Observed Evidence` entries MAY cite either the primary DEV-REPORT or a supplementary DEV-REPORT, but each citation MUST identify the specific artifact path and evidence location.

### D. Per-Task Verification Tables

- Verification checklist MUST be organized by task or criterion group.
- Each group uses the table schema: `# | Check | Expected | Observed Evidence | Result`
- `Result` values: `PASS`, `FAIL`, `N/A`
- `Observed Evidence` MUST include specific evidence (line numbers, grep results, file paths), not general assertions.
- A single checklist group MAY cite both a primary and one or more supplementary DEV-REPORTs when verifying consolidated package accuracy.

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

> **Scope note**: This section covers **internal rework paths** — Situation A (deliverable deficiency) and Situation B (scope gap) — both of which originate from the gate's own review process. External baseline changes (e.g., a standard amendment that alters the gate's normative baseline) are **not** verification findings and MUST NOT be classified as Situation A or Situation B. If an external baseline change is detected during a verification in progress, the reviewer MUST pause the verification and escalate to the plan level for impact classification per `guideline_workspace_plan.md` §VI.M. External impacts are resolved at the plan/proposal governance layer, not the verification layer.

### A. Situation A — Deliverable Deficiency

1. **Definition**: The requirement was correctly specified in the approved plan or standard, but the deliverable fails to meet it.
2. **Path**: Reviewer issues FINDING-### (Situation A). Developer performs rework.
3. **Handoff rule**: The verification artifact's findings register IS the rework handoff. No plan amendment required. No additional artifact needed. The developer reads the finding, understands the required action, and performs rework under the same task ID.

**Complex revision guidance**: When findings involve multiple deliverable deficiencies with specific format or schema requirements (e.g., missing matrices with defined column structures, missing lifecycle models with paired outputs), the findings register alone may not provide sufficient implementation detail. In such cases:
- The reviewer SHOULD trigger an `IMPLEMENTATION remediation_specification` authored per `guideline_workspace_implementation.md` to carry the developer-executable HOW for the remediation cycle.
- Existing or already-authored `revision-checklist` supplementary files remain grandfathered and MAY continue to be used where they already exist.
- A new supplementary `revision-checklist` MAY still be used as a bounded supporting checklist, but it is no longer the preferred primary handoff surface for new complex remediation planning.
- The primary verification remains the gate evidence and verdict surface. The remediation specification becomes the detailed developer handoff surface for the new complex cycle.


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

### A. Verifier Verdicts

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
| **APPROVE** | Accept gate outcomes. Gate closed. |
| **APPROVE WITH CONDITIONS** | Accept with conditions. Gate closed; conditions tracked. |
| **RECYCLE** | Agree rework needed. Gate stays open. |
| **REJECT** | Terminate gate. Work killed/redirected. |

**Rule**: Client MAY override the consultant recommendation (e.g., REJECT when consultant recommends APPROVE, if Client identifies concerns missed by both reviewer and consultant). Override MUST be documented with rationale in the GDR.

## IX. RE-ASSESSMENT VERSIONING

- After a RECYCLE verdict and completed rework, the verification artifact is **version-bumped** (e.g., v1.0.0 → v2.0.0 for major re-assessment).
- The dedicated changelog file records: re-assessment date, findings addressed, new verdict.
- New or updated findings sections are added/modified. Resolved findings have their Resolution Status updated to `resolved` with a Resolution Date.
- If the verification TASK methodology needs rework (not just the assessed deliverable), a sub-task (TK###.n) is created for the verification task, following `guideline_workspace_plan.md §VII` (Sub-Activity Rules).
- Re-assessment versioning applies to all artifacts in a Verification Package (primary + supplementary). Version bumps SHOULD be coordinated.
- Re-assessment remains tied to the same governing gate ID; `RECYCLE` does not create a new gate identity for the subsequent review cycle.

## X. GATE DECISION RECORD (GDR) — CROSS-REFERENCE

The Gate Decision Record (GDR) specification, lifecycle, and enforcement rules are defined in `guideline_workspace_proposal.md` §VII (Gate Semantics & Gate Decision Record).

The gate decision flow produces three distinct signals:
1. **Verifier Verdict** (in this artifact's Gate Recommendation section, §VIII): Evidence-based quality/compliance signal using verdict taxonomy (`PASS / CONDITIONAL PASS / PASS WITH DEFERRALS / RECYCLE / FAIL`). Recorded only in the verification artifact — NOT duplicated into the GDR.
2. **Consultant Recommendation** (in the proposal's GDR): Consolidated advisory signal synthesizing reviewer findings and GIR dispositions. Uses client decision taxonomy (`APPROVE / APPROVE WITH CONDITIONS / RECYCLE / REJECT`).
3. **Client Decision** (in the proposal's GDR): Authoritative closure signal. Client MAY override the consultant recommendation.

The verification artifact's role at a gate is to provide evidence and a verifier verdict. The GDR — which records the consultant's recommendation and the client's decision — is hosted in the `gate_disposition` proposal artifact, not in the verification artifact.

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

`prompt/templates/consultant/workspace/changelog/changelog_guideline_workspace_verification.md`
