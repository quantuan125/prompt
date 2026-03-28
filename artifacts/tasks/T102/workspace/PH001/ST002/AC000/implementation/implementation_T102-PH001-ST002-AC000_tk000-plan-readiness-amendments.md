---
artifact_type: 'IMPLEMENTATION'
implementation_type: 'task_specification'
initiative_id: 'T102'
initiative_code: 'CWD'
phase: '1'
stream_id: 'T102-PH001-ST002'
activity_id: 'T102-PH001-ST002-AC000'
task_id: 'T102-PH001-ST002-AC000 (TK000: multi-file plan readiness scope)'
version: '1.0.0'
date: '2026-03-28'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/plan_T102-PH001-ST002-AC000.md'
execution_audience: 'consultant'
purpose: 'Detailed implementation specification for TK000 plan readiness amendments: Gate-Readiness Stack guideline amendment (external review step), activity plan template update, AC000 activity plan amendment (TK000 + TK009 + GATE-002 stack), stream plan conformance check, and workflow chain rules update'
---

# IMPLEMENTATION (Task Specification): TK000 — AC000 Plan Readiness Amendments

## I. PURPOSE & AUTHORITY

- **Purpose**: This artifact specifies the exact file mutations required for TK000 (Plan Readiness Assessment & Commission) of T102-PH001-ST002-AC000. The scope covers five logical actions: (S1) amending `guideline_workspace_plan.md` §VI.L to codify the mandatory external review step in both Gate-Readiness Stack sequences; (S2) amending `workspace_documentation_rules.md` §7.A and §8 to reflect the external review in canonical workflow chains and the ownership matrix; (S3) updating `template_workspace_plan_activity.md` to include the external review task in the Gate-Readiness Stack example; (S4) amending `plan_T102-PH001-ST002-AC000.md` to add TK000, TK009 (external review for GATE-001), and the full GATE-002 implementation-backed stack (TK010–TK015 + GATE-002); (S5) conformance-checking and amending `plan_T102-PH001-ST002.md` if the stream-level AC000 contract stub requires updates.
- **Authority chain**: The governing activity plan (`plan_T102-PH001-ST002-AC000.md`) authorizes this work at the TK000 task level. This artifact specifies HOW the amendments are performed. Execution evidence for this TK000 work is captured via the plan changelog entries themselves (consultant-owned planning work, no dev-report required).
- **Audience**: `LLM_Consultant` (`execution_audience: consultant`). This is consultant-owned planning and guideline amendment work. No developer execution or dev-report is required.
- This artifact does NOT hold a GDR. Gate decisions are recorded in gate_disposition proposals per `guideline_workspace_proposal.md` Section VII.

## II. TASK SCOPE

- **Governing plan task**: `T102-PH001-ST002-AC000-TK000` (to be added to the activity plan by SPEC-004)
- **Trigger**: Task complexity exceeds plan-step capacity. Five separate files must be mutated with precise cross-referencing, template compliance, guideline normative amendments, and Gate-Readiness Stack codification. The AC000 activity plan amendment alone requires authoring 9 new task/gate sections.
- **Deliverable contract**: (1) `guideline_workspace_plan.md` §VI.L amended with mandatory external review step; (2) `workspace_documentation_rules.md` §7.A and §8 amended with external review in workflow chains and ownership matrix; (3) `template_workspace_plan_activity.md` updated with external review task example; (4) `plan_T102-PH001-ST002-AC000.md` amended with TK000 + TK009 + GATE-002 stack; (5) `plan_T102-PH001-ST002.md` assessed and amended if needed.

## III. SPECIFICATION ITEMS

### SPEC-001 — Amend `guideline_workspace_plan.md` §VI.L (Gate-Readiness Stack: External Review Step)

| Field | Detail |
|:--|:--|
| Requirement Source | TK000 consultation session (2026-03-28): client established that gate-disposition → external review → gate is the mandatory pattern for all gates. Gap identified: §VI.L does not codify the external review step. |
| Target file(s) | `prompt/templates/consultant/workspace/guideline_workspace_plan.md` |
| Required end-state posture | §VI.L Implementation-Backed Sequence has 6 steps (external review as step 5); §VI.L Consultation-Only Sequence has 4 steps (external review as step 3); Ownership table has an external review row; Cross-Reference section references `guideline_workspace_analysis.md` §IV.B for external review authoring rules; version bumped to `1.20.0` |
| Explicit non-target / do-not-change constraints | Do NOT modify §VI.A–K, §VI.M, or any other section. Do NOT change the existing step numbering for steps that come before the external review insertion point. Do NOT alter the Purpose paragraph or the Task Register Placement paragraph. Do NOT modify the Rule paragraph under Consultation-Only Sequence except to add the external review rule. |
| Validation check | (1) Implementation-Backed Sequence lists 6 numbered steps with external review as step 5; (2) Consultation-Only Sequence lists 4 numbered steps with external review as step 3; (3) Ownership table has 8 rows (7 current + 1 new); (4) Cross-Reference section mentions external review; (5) frontmatter `version: '1.20.0'` and `date: '2026-03-28'` |
| Blocking ambiguity rule | If the current file version differs from v1.19.0, STOP and re-read the file before applying mutations. If §VI.L structure has changed from what is specified here, escalate. |
| Status | `open` |

#### Implementation Detail

**Step 1: Update frontmatter**

Change:
```yaml
version: '1.19.0'
date: '2026-03-26'
```
to:
```yaml
version: '1.20.0'
date: '2026-03-28'
```

**Step 2: Amend Implementation-Backed Sequence (lines 300–311)**

Replace the entire Implementation-Backed Sequence block (from `#### Implementation-Backed Sequence` through the line ending `...records the decision in the GDR.`) with:

```markdown
#### Implementation-Backed Sequence

Every gate that reviews developer-executed deliverables MUST be preceded by the following ordered task sequence in the plan's Task Register:

1. **Implementation tasks** — owned by `LLM_Developer` (or the implementation-responsible role). Produce the deliverables that the gate will review.

> **Note**: When a gate enters `RECYCLE` and remediation work requires detailed specification, a `remediation_specification` IMPLEMENTATION artifact SHOULD be authored to specify the corrective-action detail. The IMPLEMENTATION artifact is a formal task in the remediation loop, placed above the gate row per §VI.K. See `guideline_workspace_implementation.md` for authoring rules.

2. **DEV-REPORT task** — owned by `LLM_Developer`. Produces bounded execution evidence per `guideline_workspace_dev-report.md`. The dev-report is verification input, not verification itself.
3. **Verification task** — owned by `LLM_Reviewer`. Produces independent evidence-first verification per `guideline_workspace_verification.md`. Records the reviewer verdict in the verification artifact's Gate Recommendation section.
4. **Gate-disposition proposal task** — owned by `LLM_Consultant` (or `LLM_Planner`). Produces the `gate_disposition` proposal per `guideline_workspace_proposal.md`. Hosts the authoritative Gate Decision Record (GDR).
5. **External review task** — owned by `LLM_Subconsultant`. Produces an independent `external_review` analysis per `guideline_workspace_analysis.md` §IV.B. The external review serves as a second-opinion quality audit of the gate package — testing evidence integrity, role-boundary compliance, plan-guideline compliance, and downstream task readiness. The external review is advisory input to the main consultant; it does NOT override the gate-disposition proposal's GDR authority. The main `LLM_Consultant` MUST review the external review findings and incorporate them into a final assessment of the gate package before the gate proceeds to client disposition.
6. **Gate** — owned by `Client`. Consumes the gate package (including the external review) and records the decision in the GDR.
```

Note: The word `SHOULD` in the existing first sentence ("Every gate that reviews developer-executed deliverables SHOULD be preceded") is changed to `MUST` to reflect the client's decision that the full stack including external review is mandatory.

**Step 3: Amend Consultation-Only Sequence (lines 313–323)**

Replace the entire Consultation-Only Sequence block (from `#### Consultation-Only Sequence` through the line ending `...quarantine the artifact.`) with:

```markdown
#### Consultation-Only Sequence

When all tasks before a gate are consultant-owned and no developer-mutated deliverable is being assessed, the gate MUST be preceded by this reduced sequence:

1. **Consultation tasks** — owned by `LLM_Consultant`. Produce the notes, analyses, plan amendments, and other decision-preparation artifacts that the gate will review.
2. **Gate-disposition proposal task** — owned by `LLM_Consultant` (or `LLM_Planner`). Produces the `gate_disposition` proposal per `guideline_workspace_proposal.md`. Hosts the authoritative Gate Decision Record (GDR).
3. **External review task** — owned by `LLM_Subconsultant`. Produces an independent `external_review` analysis per `guideline_workspace_analysis.md` §IV.B. The external review serves as a second-opinion quality audit of the gate package — testing evidence integrity, role-boundary compliance, plan-guideline compliance, and downstream task readiness. The external review is advisory input to the main consultant; it does NOT override the gate-disposition proposal's GDR authority. The main `LLM_Consultant` MUST review the external review findings and incorporate them into a final assessment of the gate package before the gate proceeds to client disposition.
4. **Gate** — owned by `Client`. Consumes the gate package (including the external review) and records the decision in the GDR.

Rule:
- Consultation-only gates MUST NOT introduce `DEV-REPORT` or `VERIFICATION` tasks unless the gate scope is expanded to review developer-mutated deliverables.
- If a consultation-only gate discovers premature downstream execution or a prematurely materialized concrete artifact, the governing gate remains open, the premature artifact is preserved but removed from active gate authority, and corrective consultant-owned tasks are inserted before the gate row to reclassify or quarantine the artifact.
```

Note: The word `SHOULD` in the existing first sentence is changed to `MUST`.

**Step 4: Amend Ownership table (lines 333–341)**

Replace the existing Ownership table with:

```markdown
| Stack Position | Fixed Owner | Artifact Type | Governing Guideline |
|:--|:--|:--|:--|
| Implementation tasks | `LLM_Developer` | Deliverables (per plan) | Plan (this guideline) |
| DEV-REPORT task | `LLM_Developer` | `DEV-REPORT` | `guideline_workspace_dev-report.md` |
| Verification task | `LLM_Reviewer` | `VERIFICATION` | `guideline_workspace_verification.md` |
| Consultation tasks | `LLM_Consultant` | `NOTES` / `ANALYSIS` / plan-owned deliverables | Respective artifact guidelines |
| Gate-disposition proposal task | `LLM_Consultant` | `PROPOSAL` (`gate_disposition`) | `guideline_workspace_proposal.md` |
| External review task | `LLM_Subconsultant` | `ANALYSIS` (`external_review`) | `guideline_workspace_analysis.md` §IV.B |
| IMPLEMENTATION task (where applicable) | `LLM_Consultant` | `IMPLEMENTATION` | `guideline_workspace_implementation.md` |
| Gate | `Client` | Decision (GDR) | `guideline_workspace_proposal.md` §VII |
```

**Step 5: Amend Cross-Reference section (lines 344–348)**

Replace the existing Cross-Reference section with:

```markdown
#### Cross-Reference

- For DEV-REPORT trigger and lifecycle rules, see `guideline_workspace_dev-report.md` §III.
- For verification workflow and implementation-backed gate rules, see `guideline_workspace_verification.md` §III.
- For gate-disposition proposal structure and GDR specification, see `guideline_workspace_proposal.md` §V.B and §VII.
- For external review authoring rules and gate-readiness scope requirements, see `guideline_workspace_analysis.md` §IV.B.
- For the workflow chain and role-to-artifact ownership matrix, see `workspace_documentation_rules.md` §7 and §8.
```

**Step 6: Add changelog entry**

Append a new row to the top of `prompt/templates/consultant/workspace/changelog/changelog_guideline_workspace_plan.md` (after the header row and separator, before the v1.18.0 row). Note: the current file starts at v1.18.0 as the first entry, preceded only by the header row and separator:

```markdown
| v1.19.0 | 2026-03-26 | Maintenance | Changelog continuity: this version was the prior release before v1.20.0. No changelog entry was captured at release time. |
| v1.20.0 | 2026-03-28 | Amendment | §VI.L Gate-Readiness Stack: Added mandatory external review step (`LLM_Subconsultant`) to both implementation-backed (step 5) and consultation-only (step 3) gate sequences. External review produces an independent `external_review` analysis that serves as advisory second-opinion input; main `LLM_Consultant` MUST review before gate proceeds. Changed sequence obligation from SHOULD to MUST. Added external review row to Ownership table. Added cross-reference to `guideline_workspace_analysis.md` §IV.B. Source: T102-PH001-ST002-AC000-TK000 consultation session (2026-03-28). |
```

---

### SPEC-002 — Amend `workspace_documentation_rules.md` §7.A Workflow Chains and §8 Ownership Matrix

| Field | Detail |
|:--|:--|
| Requirement Source | The external review step must be reflected in the canonical workflow chains (§7.A) and the role-to-artifact ownership matrix (§8) to maintain consistency with the `guideline_workspace_plan.md` §VI.L amendment. |
| Target file(s) | `prompt/templates/consultant/workspace/workspace_documentation_rules.md` |
| Required end-state posture | §7.A workflow chains include external review step in both implementation-backed and consultation-only variants; §8 ownership matrix includes `LLM_Subconsultant` external review row; version bumped to `3.7.0` |
| Explicit non-target / do-not-change constraints | Do NOT modify §1–6, §7.B–D, §9–11, or the changelog pointer in §12. Do NOT alter the conditional external-impact assessment step in §7.A. Do NOT change existing rows in §8 that are unrelated to the external review addition. |
| Validation check | (1) Implementation-backed chain includes `→ ANALYSIS (external_review) →` between PROPOSAL and SPS; (2) Consultation-only chain includes `→ ANALYSIS (external_review) →` between PROPOSAL and downstream; (3) §8 has a new row for external review with `LLM_Subconsultant`; (4) frontmatter `version: '3.7.0'` and `date: '2026-03-28'` |
| Blocking ambiguity rule | If the current file version differs from v3.6.0, STOP and re-read the file before applying mutations. |
| Status | `open` |

#### Implementation Detail

**Step 1: Update frontmatter**

Change:
```yaml
version: '3.6.0'
date: '2026-03-26'
```
to:
```yaml
version: '3.7.0'
date: '2026-03-28'
```

**Step 2: Amend §7.A workflow chains (lines 149–153)**

Replace the two workflow chain code blocks:

Current implementation-backed chain:
```
Implementation-backed:
`ROADMAP → PLAN → NOTES / ANALYSIS → [IMPLEMENTATION task_specification where needed] → implementation deliverables → DEV-REPORT → VERIFICATION → [IMPLEMENTATION remediation_specification where RECYCLE] → remediation deliverables → DEV-REPORT → VERIFICATION (re-assessment) → PROPOSAL (GDR where applicable) → SPS / downstream approved artifacts`
```

Replace with:
```
Implementation-backed:
`ROADMAP → PLAN → NOTES / ANALYSIS → [IMPLEMENTATION task_specification where needed] → implementation deliverables → DEV-REPORT → VERIFICATION → [IMPLEMENTATION remediation_specification where RECYCLE] → remediation deliverables → DEV-REPORT → VERIFICATION (re-assessment) → PROPOSAL (GDR where applicable) → ANALYSIS (external_review, LLM_Subconsultant) → SPS / downstream approved artifacts`
```

Current consultation-only chain:
```
Consultation-only:
`ROADMAP → PLAN → NOTES / ANALYSIS → PROPOSAL (GDR where applicable) → downstream approved artifacts`
```

Replace with:
```
Consultation-only:
`ROADMAP → PLAN → NOTES / ANALYSIS → PROPOSAL (GDR where applicable) → ANALYSIS (external_review, LLM_Subconsultant) → downstream approved artifacts`
```

**Step 3: Add a rule note after the workflow chains** (after the `Consultation-only:` chain, before the `**Conditional external-impact assessment step**:` block)

Insert:

```markdown

**External review step**:
The `ANALYSIS (external_review)` step is authored by `LLM_Subconsultant` as an independent second-opinion quality audit of the gate package. The external review is advisory input; it does NOT override the `PROPOSAL`-hosted GDR authority. The main `LLM_Consultant` MUST review the external review findings and incorporate them into a final assessment before the gate proceeds to client disposition. See `guideline_workspace_plan.md` §VI.L for the full Gate-Readiness Stack pattern.

```

**Step 4: Amend §8 Role-to-Artifact Ownership Matrix (lines 239–249)**

Add a new row to the ownership matrix table. Insert after the `ANALYSIS` row and before the `PROPOSAL` row:

Current `ANALYSIS` row:
```
| ANALYSIS | LLM_Consultant | Client / Consultant review as needed | Client when analysis drives approval | Consultant, Client |
```

Insert this new row immediately after:
```
| ANALYSIS (`external_review`) | LLM_Subconsultant | LLM_Consultant (mandatory review before gate) | Client via GDR (advisory input only) | Consultant, Client |
```

**Step 5: Add changelog entry**

Append a new row to the top of `prompt/templates/consultant/workspace/changelog/changelog_workspace_documentation_rules.md` (after the header row and separator, before the v3.5.0 row). Note: the current file starts at v3.5.0 as the most recent entry:

Insert before the v3.5.0 row:
```markdown
| v3.6.0 | 2026-03-26 | Maintenance | Changelog continuity: this version was the prior release before v3.7.0. No changelog entry was captured at release time. |
| v3.7.0 | 2026-03-28 | Amendment | §7.A: Added mandatory `ANALYSIS (external_review, LLM_Subconsultant)` step to both implementation-backed and consultation-only canonical workflow chains. Added external review step explanatory note. §8: Added `LLM_Subconsultant` external review row to role-to-artifact ownership matrix. Source: T102-PH001-ST002-AC000-TK000 consultation session (2026-03-28). |
```

---

### SPEC-003 — Update `template_workspace_plan_activity.md` (Gate-Readiness Stack Example)

| Field | Detail |
|:--|:--|
| Requirement Source | Template must reflect the amended Gate-Readiness Stack pattern from SPEC-001 so future activity plans use the correct task sequence. |
| Target file(s) | `prompt/templates/consultant/workspace/template_workspace_plan_activity.md` |
| Required end-state posture | Task Register example includes external review task row between gate-disposition and GATE; Tasks (Detailed) section includes external review task example; HTML comment guidance updated; version bumped to `1.4.0` |
| Explicit non-target / do-not-change constraints | Do NOT modify the frontmatter keys other than `version` and `date`. Do NOT alter the TK001/TK001.1 example tasks or the Activity Outline section. Do NOT change Section IV (Links Register). |
| Validation check | (1) Task Register has external review row between gate-disposition and GATE for both implementation-backed and consultation-only examples; (2) Tasks (Detailed) has an external review task section; (3) HTML comment mentions external review; (4) frontmatter `version: '1.4.0'` and `date: '2026-03-28'` |
| Blocking ambiguity rule | If the current file version differs from v1.3.0, STOP and re-read before applying mutations. |
| Status | `open` |

#### Implementation Detail

**Step 1: Update frontmatter**

Change:
```yaml
version: '1.3.0'
date: '2026-03-16'
```
to:
```yaml
version: '1.4.0'
date: '2026-03-28'
```

**Step 2: Update Task Register example (lines 63–70)**

Replace the existing Gate-Readiness Stack rows in the Task Register:

Current rows:
```markdown
| TK003 | `T###-PH###-ST###-AC###-TK003` | Produce dev-report for GATE-001 | `planned` | LLM_Developer | TK002 | `dev-report/` | `guideline_workspace_dev-report.md` | - |
| TK004 | `T###-PH###-ST###-AC###-TK004` | Produce GATE-001 verification | `planned` | LLM_Reviewer | TK003 | `verification/` | `guideline_workspace_verification.md` | - |
| TK005 | `T###-PH###-ST###-AC###-TK005` | Produce GATE-001 gate-disposition proposal | `planned` | LLM_Consultant | TK004 | `proposal/` | `guideline_workspace_proposal.md` | - |
| GATE-001 | `T###-PH###-ST###-AC###-GATE-001` | Gate: [description] | `planned` | Client | TK005 | Pass/fail | `guideline_workspace_plan.md` | - |
```

Replace with:
```markdown
| TK003 | `T###-PH###-ST###-AC###-TK003` | Produce dev-report for GATE-001 | `planned` | LLM_Developer | TK002 | `dev-report/` | `guideline_workspace_dev-report.md` | - |
| TK004 | `T###-PH###-ST###-AC###-TK004` | Produce GATE-001 verification | `planned` | LLM_Reviewer | TK003 | `verification/` | `guideline_workspace_verification.md` | - |
| TK005 | `T###-PH###-ST###-AC###-TK005` | Produce GATE-001 gate-disposition proposal | `planned` | LLM_Consultant | TK004 | `proposal/` | `guideline_workspace_proposal.md` | - |
| TK006 | `T###-PH###-ST###-AC###-TK006` | Produce GATE-001 external review | `planned` | LLM_Subconsultant | TK005 | `analysis/` | `guideline_workspace_analysis.md` | - |
| GATE-001 | `T###-PH###-ST###-AC###-GATE-001` | Gate: [description] | `planned` | Client | TK006 | Pass/fail | `guideline_workspace_plan.md` | - |
```

**Step 3: Update HTML comment for Gate-Readiness Stack (lines 136–143)**

Replace the existing HTML comment:

```html
<!--
Gate-Readiness Stack:
  When an activity includes a gate, the task register and detailed sections
  SHOULD follow the Gate-Readiness Stack pattern per guideline_workspace_plan.md §VI.L.
  Implementation-backed sequence: implementation tasks → DEV-REPORT → verification → gate-disposition → gate.
  Consultation-only sequence: consultant-owned preparatory tasks → gate-disposition → gate.
  Consultation-only gates omit both DEV-REPORT and verification.
-->
```

Replace with:

```html
<!--
Gate-Readiness Stack:
  When an activity includes a gate, the task register and detailed sections
  MUST follow the Gate-Readiness Stack pattern per guideline_workspace_plan.md §VI.L.
  Implementation-backed sequence: implementation tasks → DEV-REPORT → verification → gate-disposition → external review → gate.
  Consultation-only sequence: consultant-owned preparatory tasks → gate-disposition → external review → gate.
  Consultation-only gates omit both DEV-REPORT and verification.
  External review (LLM_Subconsultant) is mandatory for all gates.
-->
```

**Step 4: Add external review task section in Tasks (Detailed)**

Insert the following new section between the existing "Task TK005: Produce GATE-001 Gate-Disposition Proposal" section and the "GATE-001" section. Place it after the `---` separator that follows TK005's Success Criteria and before the `### GATE-001:` heading:

```markdown
### Task TK006: Produce GATE-001 External Review

**Task ID**: `T###-PH###-ST###-AC###-TK006`

**Purpose**: Produce an independent second-opinion quality audit of the gate package before client disposition.

**Deliverable**:
- `[external review path per guideline_workspace_analysis.md §VII]`

**Steps**:
1. Review the gate-disposition proposal and all evidence artifacts per `guideline_workspace_analysis.md` §IV.B
2. Assess evidence integrity, role-boundary compliance, plan-guideline compliance, and downstream task readiness
3. Record findings and recommendation in the external review analysis

**Success Criteria**:
- [ ] External review analysis exists with findings and recommendation
- [ ] Main `LLM_Consultant` has reviewed the external review findings

---

```

**Step 5: Update GATE-001 section**

In the GATE-001 section, update the Entry Criteria to include the external review:

Replace:
```markdown
**Entry Criteria**:
- TK001 through TK005 are completed
- Verification artifact exists with a reviewer verdict
- Gate-disposition proposal exists with a populated GDR (pending state)
```

With:
```markdown
**Entry Criteria**:
- TK001 through TK006 are completed
- Verification artifact exists with a reviewer verdict
- Gate-disposition proposal exists with a populated GDR (pending state)
- External review analysis exists with findings reviewed by main `LLM_Consultant`
```

Also update the `Depends On` in the GATE-001 row if referenced elsewhere to depend on TK006 instead of TK005.

**Step 6: Update changelog**

Append to the Changelog table (Section V), before the existing v1.3.0 row:

```markdown
| v1.4.0 | 2026-03-28 | Amendment | Added mandatory external review task (`LLM_Subconsultant`) to Gate-Readiness Stack example in Task Register (TK006) and Tasks (Detailed). Updated HTML guidance comment. Updated GATE-001 entry criteria to include external review. Source: T102-PH001-ST002-AC000-TK000 consultation; `guideline_workspace_plan.md` §VI.L v1.20.0. |
```

---

### SPEC-004 — Amend `plan_T102-PH001-ST002-AC000.md` (Add TK000, TK009, GATE-002 Stack)

| Field | Detail |
|:--|:--|
| Requirement Source | TK000 readiness assessment findings: TK000 missing; external review task missing before GATE-001; no post-GATE-001 implementation-backed gate stack. |
| Target file(s) | `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/plan_T102-PH001-ST002-AC000.md` |
| Required end-state posture | Task Register includes TK000, TK009, TK010–TK015, GATE-002; Section III includes detailed task/gate sections for all new entries; GATE-001 depends on TK009; GATE-002 stack follows implementation-backed sequence; version bumped to `2.0.0` |
| Explicit non-target / do-not-change constraints | Do NOT modify the existing TK001–TK008 detailed task sections (Section III bodies). TK001–TK008 Task Register rows may only be modified to update `Depends On` where needed (TK001–TK006 depend on TK000). Do NOT modify Section I (Executive Summary) beyond updating the Non-goal to acknowledge GATE-002. Do NOT delete or rewrite the existing GATE-001 detailed section — only update its Entry Criteria and Depends On. |
| Validation check | (1) Task Register has 18 rows (TK000 + TK001–TK008 + TK009 + GATE-001 + TK010–TK015 + GATE-002); (2) GATE-001 `Depends On` = TK009; (3) TK009 `Depends On` = TK008; (4) TK010 `Depends On` = GATE-001; (5) GATE-002 `Depends On` = TK015; (6) Detailed sections exist for all new tasks/gates; (7) frontmatter `version: '2.0.0'` and `date: '2026-03-28'` |
| Blocking ambiguity rule | If the current file version differs from v1.0.0, STOP and re-read the file before applying mutations. If any new tasks have been added since v1.0.0, reconcile before applying. |
| Status | `open` |

#### Implementation Detail

**Step 1: Update frontmatter**

Change:
```yaml
version: '1.0.0'
date: '2026-03-27'
```
to:
```yaml
version: '2.0.0'
date: '2026-03-28'
```

**Step 2: Update Non-goal in Section I**

Replace:
```markdown
**Non-goal**: This activity does NOT perform structural remediation of T102-STDs (AC001 scope), draft verification contracts (AC002), or modify SSOT artifacts (AC004). It is a diagnostic and calibration pass only, except for the T102-STD-004 supersession housekeeping which is a bounded one-file mutation.
```

With:
```markdown
**Non-goal**: This activity does NOT perform structural remediation of T102-STDs (AC001 scope), draft verification contracts (AC002), or modify SSOT artifacts (AC004). The diagnostic and calibration work (TK001–TK007) is reviewed at GATE-001 (consultation-only). The bounded T102-STD-004 supersession housekeeping (TK006) and any content remediation seeded by GATE-001 findings are reviewed at GATE-002 (implementation-backed).
```

**Step 3: Replace the entire Task Register table**

Replace the existing Task Register table (all rows from `| TK001 |` through `| GATE-001 |`) with:

```markdown
| Task | Task ID | Name | Status | Owner | Depends On | Target | Reference | Action |
|:--|:--|:--|:--|:--|:--|:--|:--|:--|
| TK000 | `T102-PH001-ST002-AC000-TK000` | Plan Readiness Assessment & Commission | `in_progress` | LLM_Consultant | -- | Activity plan + guidelines | This session notes | -- |
| TK001 | `T102-PH001-ST002-AC000-TK001` | Verify STD-007 amendments (RES-004 Deltas 1-4 + RES-006 D1) | `planned` | LLM_Consultant | TK000 | `standard_T102-STD-007_issues-risks-index.md` | ST005-AC001 task descriptions | -- |
| TK002 | `T102-PH001-ST002-AC000-TK002` | Verify STD-003 amendments (RES-005 Deltas A1-A4) | `planned` | LLM_Consultant | TK000 | `standard_T102-STD-003_explicit-inheritance-model.md` | ST005-AC002 task descriptions | -- |
| TK003 | `T102-PH001-ST002-AC000-TK003` | Verify STD-006 amendments (RES-005 Deltas B1-B4 + RES-006 C1) | `planned` | LLM_Consultant | TK000 | `standard_T102-STD-006_research-artifacts-index.md` | ST005-AC003 task descriptions | -- |
| TK004 | `T102-PH001-ST002-AC000-TK004` | Verify STD-001 amendments (RES-006 Deltas A1-A5, absorbs RES-005 D1-D2) | `planned` | LLM_Consultant | TK000 | `standard_T102-STD-001_consultancy-operating-model.md` | ST005-AC004 task descriptions | -- |
| TK005 | `T102-PH001-ST002-AC000-TK005` | P-STD-001 structural gap assessment (all T102-STDs) | `planned` | LLM_Consultant | TK001, TK002, TK003, TK004 | All `standard_T102-STD-*.md` files | P-STD-001 | -- |
| TK006 | `T102-PH001-ST002-AC000-TK006` | T102-STD-004 supersession housekeeping | `planned` | LLM_Consultant | TK000 | `standard_T102-STD-004_specification-standard-and-guideline.md` | P-STD-001 `supersedes` field | -- |
| TK007 | `T102-PH001-ST002-AC000-TK007` | Produce calibrated scope brief for AC001-AC004 | `planned` | LLM_Consultant | TK001, TK002, TK003, TK004, TK005, TK006 | `analysis_T102-PH001-ST002-AC000_calibrated-scope-brief.md` | `guideline_workspace_analysis.md` | -- |
| TK008 | `T102-PH001-ST002-AC000-TK008` | Produce GATE-001 gate-disposition proposal | `planned` | LLM_Consultant | TK007 | `proposal/` | `guideline_workspace_proposal.md` | -- |
| TK009 | `T102-PH001-ST002-AC000-TK009` | Produce GATE-001 external review | `planned` | LLM_Subconsultant | TK008 | `analysis/` | `guideline_workspace_analysis.md` §IV.B | -- |
| GATE-001 | `T102-PH001-ST002-AC000-GATE-001` | Gate: Client approval of AC000 diagnostic deliverables | `planned` | Client | TK009 | Pass/fail | `guideline_workspace_plan.md` §VI.L | -- |
| TK010 | `T102-PH001-ST002-AC000-TK010` | Author implementation spec for post-GATE-001 remediation | `planned` | LLM_Consultant | GATE-001 | `implementation/` | `guideline_workspace_implementation.md` | -- |
| TK011 | `T102-PH001-ST002-AC000-TK011` | Execute implementation per spec (STD-004 supersession + GATE-001-seeded fixes) | `planned` | LLM_Developer | TK010 | Target STD files per spec | Implementation spec | -- |
| TK012 | `T102-PH001-ST002-AC000-TK012` | Produce GATE-002 dev-report | `planned` | LLM_Developer | TK011 | `dev-report/` | `guideline_workspace_dev-report.md` | -- |
| TK013 | `T102-PH001-ST002-AC000-TK013` | Produce GATE-002 verification | `planned` | LLM_Reviewer | TK012 | `verification/` | `guideline_workspace_verification.md` | -- |
| TK014 | `T102-PH001-ST002-AC000-TK014` | Produce GATE-002 gate-disposition proposal | `planned` | LLM_Consultant | TK013 | `proposal/` | `guideline_workspace_proposal.md` | -- |
| TK015 | `T102-PH001-ST002-AC000-TK015` | Produce GATE-002 external review | `planned` | LLM_Subconsultant | TK014 | `analysis/` | `guideline_workspace_analysis.md` §IV.B | -- |
| GATE-002 | `T102-PH001-ST002-AC000-GATE-002` | Gate: Client approval of AC000 implementation deliverables | `planned` | Client | TK015 | Pass/fail | `guideline_workspace_plan.md` §VI.L | -- |
```

**Step 4: Add TK000 detailed section**

Insert immediately after the `## III. TASKS (DETAILED)` heading and before the existing `### Task TK001:` section:

```markdown
### Task TK000: Plan Readiness Assessment & Commission

**Task ID**: `T102-PH001-ST002-AC000-TK000`

**Purpose**: Validate the AC000 activity plan is complete, guideline-conformant, and commission-ready before substantive tasks begin. Identify gaps, risks, and issues. Produce any required guideline amendments and plan amendments as part of this readiness pass.

**Deliverable**:
- Readiness assessment captured in session notes
- Guideline amendments (if required) per IMPLEMENTATION artifact
- Plan amendments applied to this activity plan

**Scope**:
- In scope: Plan completeness review; guideline conformance check against `guideline_workspace_plan.md`, `guideline_workspace_analysis.md`, `workspace_documentation_rules.md`; gap identification; plan amendment authoring
- Out of scope: Executing substantive tasks (TK001+); delivering analysis artifacts

**Inputs Required**:
- `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/plan_T102-PH001-ST002-AC000.md` v1.0.0 -- this plan
- `prompt/templates/consultant/workspace/guideline_workspace_plan.md` -- Gate-Readiness Stack rules
- `prompt/templates/consultant/workspace/guideline_workspace_analysis.md` -- analysis artifact rules
- `prompt/templates/consultant/workspace/workspace_documentation_rules.md` -- workflow chain and ownership rules
- `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/snotes/snotes_T102-PH001-ST002-AC000-SES001.md` -- prior session context

**Steps**:
1. Read and assess the activity plan against `guideline_workspace_plan.md` and `workspace_documentation_rules.md`
2. Identify gaps (missing TK000, missing external review step, missing GATE-002 stack)
3. Consult with client on findings and obtain decisions
4. Author IMPLEMENTATION artifact for plan amendments
5. Execute plan amendments per IMPLEMENTATION artifact
6. Mark TK000 as completed

**Success Criteria**:
- [ ] Plan readiness assessment completed and captured in session notes
- [ ] All identified gaps addressed or deferred with rationale
- [ ] Plan amended to include TK000, TK009, and GATE-002 stack
- [ ] Guideline amendments applied (if required)

---

```

**Step 5: Add TK009 detailed section**

Insert immediately after the existing `### Task TK008:` section (after its `---` separator) and before the existing `### GATE-001:` section:

```markdown
### Task TK009: Produce GATE-001 External Review

**Task ID**: `T102-PH001-ST002-AC000-TK009`

**Purpose**: Produce an independent second-opinion quality audit of the GATE-001 gate package before client disposition. The external review tests evidence integrity, role-boundary compliance, plan-guideline compliance, and downstream task readiness for post-GATE-001 work.

**Deliverable**:
- `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/analysis/analysis_T102-PH001-ST002-AC000-TK009_gate-001-external-review.md`

**Scope**:
- In scope: Review of TK008 gate-disposition proposal; review of TK007 calibrated scope brief; assessment of evidence integrity, role boundaries, plan compliance, and downstream readiness for GATE-002 stack
- Out of scope: Re-performing the content verification (TK001–TK004) or structural assessment (TK005); overriding the gate-disposition proposal's GDR authority

**Inputs Required**:
- `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/proposal/proposal_T102-PH001-ST002-AC000_gate-001-disposition.md` -- TK008 deliverable
- `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/analysis/analysis_T102-PH001-ST002-AC000_calibrated-scope-brief.md` -- TK007 deliverable
- `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/plan_T102-PH001-ST002-AC000.md` -- governing plan
- `prompt/templates/consultant/workspace/guideline_workspace_analysis.md` §IV.B -- external review authoring rules

**Steps**:
1. Read the gate-disposition proposal and all evidence artifacts referenced in its Evidence Index
2. Assess per `guideline_workspace_analysis.md` §IV.B external review scope requirements:
   - Evidence integrity: all expected artifacts exist, cross-links resolve, package references are internally consistent
   - Role-boundary compliance: no role produced an artifact outside its governed ownership boundary
   - Plan-guideline compliance: deliverables conform to governing guidelines
   - Downstream task readiness: post-GATE-001 tasks (TK010–TK015, GATE-002) are well-defined and actionable given the analysis findings
   - Absence of unauthorized downstream execution: no implementation work has been performed prematurely
3. Record findings and recommendation in the external review analysis artifact
4. Main `LLM_Consultant` reviews the external review findings and incorporates them into a final gate-package assessment

**Success Criteria**:
- [ ] External review analysis artifact exists at specified path
- [ ] All five assessment criteria are addressed (evidence integrity, role boundaries, plan compliance, downstream readiness, no premature execution)
- [ ] Main `LLM_Consultant` has reviewed and acknowledged the external review findings

---

```

**Step 6: Update existing GATE-001 detailed section**

In the existing GATE-001 section, update the Entry Criteria and Depends On:

Replace:
```markdown
**Entry Criteria**:
- TK001 through TK007 are completed (content verification, structural gap assessment, supersession housekeeping, calibrated scope brief)
- TK008 gate-disposition proposal exists with populated GDR in pending state
- Calibrated scope brief provides actionable per-AC guidance
```

With:
```markdown
**Entry Criteria**:
- TK001 through TK007 are completed (content verification, structural gap assessment, supersession housekeeping, calibrated scope brief)
- TK008 gate-disposition proposal exists with populated GDR in pending state
- TK009 external review analysis exists with findings reviewed by main `LLM_Consultant`
- Calibrated scope brief provides actionable per-AC guidance
```

Also update the Gate-Disposition Proposal line to add an External Review line after it:

After:
```markdown
**Gate-Disposition Proposal**: `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/proposal/proposal_T102-PH001-ST002-AC000_gate-001-disposition.md`
```

Add:
```markdown
**External Review**: `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/analysis/analysis_T102-PH001-ST002-AC000-TK009_gate-001-external-review.md`
```

**Step 7: Add GATE-002 stack detailed sections**

Insert after the existing GATE-001 section (after its `---` separator) and before `## IV. LINKS REGISTER`:

```markdown
### Task TK010: Author Implementation Spec for Post-GATE-001 Remediation

**Task ID**: `T102-PH001-ST002-AC000-TK010`

**Purpose**: Author a detailed implementation specification for the bounded implementation work authorized by GATE-001: T102-STD-004 supersession housekeeping (TK006 execution detail) and any content remediation items seeded by GATE-001 findings.

**Deliverable**:
- `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/implementation/implementation_T102-PH001-ST002-AC000_gate-001-remediation.md`

**Scope**:
- In scope: Implementation specification for TK006 STD-004 mutation; implementation specification for any GATE-001-seeded content fixes within AC000 scope
- Out of scope: Structural remediation (AC001 scope); SSOT updates (AC004 scope)

**Inputs Required**:
- GATE-001 GDR (approved) -- authorizes implementation scope
- TK007 calibrated scope brief -- identifies what needs fixing
- `prompt/templates/consultant/workspace/guideline_workspace_implementation.md` -- implementation artifact rules

**Steps**:
1. Read GATE-001 GDR to confirm approved scope and any conditions
2. Extract implementation items from the calibrated scope brief:
   - Unconditional: TK006 STD-004 supersession mutation (already detailed in current plan TK006)
   - Conditional: any content remediation items approved by GATE-001 for in-scope fixing
3. Author implementation specification per `guideline_workspace_implementation.md` with exact SPEC items

**Success Criteria**:
- [ ] Implementation spec exists with SPEC items for all approved remediation work
- [ ] Each SPEC item has target files, end-state posture, validation checks, and blocking ambiguity rules

---

### Task TK011: Execute Implementation Per Spec

**Task ID**: `T102-PH001-ST002-AC000-TK011`

**Purpose**: Execute the implementation specification produced by TK010: perform the STD-004 supersession mutation and any GATE-001-seeded content fixes.

**Deliverable**:
- Mutated STD file(s) per implementation spec

**Scope**:
- In scope: File mutations specified in the TK010 implementation spec
- Out of scope: Any mutations not specified in the implementation spec

**Inputs Required**:
- TK010 implementation spec -- execution authority
- Target STD files as specified

**Steps**:
1. Read the implementation spec
2. Execute each SPEC item in the specified sequence
3. Validate each mutation against the SPEC item's validation check

**Success Criteria**:
- [ ] All SPEC items executed
- [ ] All validation checks pass

---

### Task TK012: Produce GATE-002 Dev-Report

**Task ID**: `T102-PH001-ST002-AC000-TK012`

**Purpose**: Capture bounded implementation evidence for the GATE-002 review package.

**Deliverable**:
- `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/dev-report/dev-report_T102-PH001-ST002-AC000_gate-002.md`

**Steps**:
1. Record implementation outcomes for TK011
2. Produce validation evidence per `guideline_workspace_dev-report.md` §VI
3. Include `implementation_reference` pointing to TK010 implementation spec

**Success Criteria**:
- [ ] Dev-report exists with required sections per `guideline_workspace_dev-report.md` §V
- [ ] Traceability matrix maps deliverables back to SPEC item IDs

---

### Task TK013: Produce GATE-002 Verification

**Task ID**: `T102-PH001-ST002-AC000-TK013`

**Purpose**: Produce independent reviewer evidence for the GATE-002 review.

**Deliverable**:
- `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/verification/verification_T102-PH001-ST002-AC000_gate-002.md`

**Steps**:
1. Read the dev-report (TK012) and implementation spec (TK010)
2. Perform evidence-first verification per `guideline_workspace_verification.md` §V
3. Verify each SPEC item's end-state posture against actual file state
4. Record reviewer verdict in Gate Recommendation section

**Success Criteria**:
- [ ] Verification artifact exists with reviewer verdict
- [ ] Each SPEC item's validation check is independently confirmed

---

### Task TK014: Produce GATE-002 Gate-Disposition Proposal

**Task ID**: `T102-PH001-ST002-AC000-TK014`

**Purpose**: Package the GATE-002 decision items and prepare the GDR for client disposition.

**Deliverable**:
- `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/proposal/proposal_T102-PH001-ST002-AC000_gate-002-disposition.md`

**Steps**:
1. Author gate-disposition proposal per `guideline_workspace_proposal.md` §V.B
2. Evidence Index: reference the dev-report (TK012), verification (TK013), and implementation spec (TK010) as primary evidence
3. Populate GDR fields in pending state per `guideline_workspace_proposal.md` §VII.D

**Success Criteria**:
- [ ] Gate-disposition proposal exists with GDR section in pending state
- [ ] Evidence Index references dev-report, verification, and implementation spec

---

### Task TK015: Produce GATE-002 External Review

**Task ID**: `T102-PH001-ST002-AC000-TK015`

**Purpose**: Produce an independent second-opinion quality audit of the GATE-002 gate package before client disposition.

**Deliverable**:
- `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/analysis/analysis_T102-PH001-ST002-AC000-TK015_gate-002-external-review.md`

**Scope**:
- In scope: Review of TK014 gate-disposition proposal; review of TK012 dev-report and TK013 verification; assessment of evidence integrity, role boundaries, plan compliance, and downstream readiness for AC001–AC004
- Out of scope: Re-performing the verification (TK013); overriding the gate-disposition proposal's GDR authority

**Inputs Required**:
- `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/proposal/proposal_T102-PH001-ST002-AC000_gate-002-disposition.md` -- TK014 deliverable
- `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/dev-report/dev-report_T102-PH001-ST002-AC000_gate-002.md` -- TK012 deliverable
- `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/verification/verification_T102-PH001-ST002-AC000_gate-002.md` -- TK013 deliverable
- `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/plan_T102-PH001-ST002-AC000.md` -- governing plan
- `prompt/templates/consultant/workspace/guideline_workspace_analysis.md` §IV.B -- external review authoring rules

**Steps**:
1. Read the gate-disposition proposal and all evidence artifacts
2. Assess per `guideline_workspace_analysis.md` §IV.B:
   - Evidence integrity
   - Role-boundary compliance
   - Plan-guideline compliance
   - Downstream task readiness (AC001–AC004 can proceed with calibrated scope brief + verified STD mutations)
   - Absence of unauthorized downstream execution
3. Record findings and recommendation
4. Main `LLM_Consultant` reviews external review findings

**Success Criteria**:
- [ ] External review analysis artifact exists at specified path
- [ ] All five assessment criteria are addressed
- [ ] Main `LLM_Consultant` has reviewed and acknowledged findings

---

### GATE-002: Client Approval of AC000 Implementation Deliverables

**Gate ID**: `T102-PH001-ST002-AC000-GATE-002`

**Entry Criteria**:
- TK010 implementation spec exists and was executed (TK011)
- TK012 dev-report captures execution evidence
- TK013 verification artifact exists with reviewer verdict
- TK014 gate-disposition proposal exists with populated GDR in pending state
- TK015 external review analysis exists with findings reviewed by main `LLM_Consultant`

**Reviewer**: Client

**Exit Criteria**:
- Client records decision in the GDR per `guideline_workspace_proposal.md` §VII.D
- If APPROVE: AC001–AC004 may proceed using calibrated scope brief + verified STD mutations as primary inputs
- If APPROVE WITH CONDITIONS: conditions are recorded and addressed before AC001 begins
- If RECYCLE: remediation tasks are created per `guideline_workspace_plan.md` §VI.K

**Gate-Disposition Proposal**: `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/proposal/proposal_T102-PH001-ST002-AC000_gate-002-disposition.md`
**External Review**: `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/analysis/analysis_T102-PH001-ST002-AC000-TK015_gate-002-external-review.md`

---

```

**Step 8: Update Links Register (Section IV)**

Add the following rows to the Links Register table:

```markdown
| Implementation | TK000 task specification | `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/implementation/implementation_T102-PH001-ST002-AC000_tk000-plan-readiness-amendments.md` |
| Guideline (amended) | Plan guideline v1.20.0 | `prompt/templates/consultant/workspace/guideline_workspace_plan.md` |
| Guideline (amended) | Documentation rules v3.7.0 | `prompt/templates/consultant/workspace/workspace_documentation_rules.md` |
```

**Step 9: Add changelog entry**

Append a new row to the Changelog table (Section V):

```markdown
| v2.0.0 | 2026-03-28 | Major Amendment | TK000 plan readiness amendments. Added TK000 (Plan Readiness Assessment). Added TK009 (GATE-001 external review, LLM_Subconsultant). Updated GATE-001 to depend on TK009. Added full GATE-002 implementation-backed stack: TK010 (implementation spec), TK011 (execution), TK012 (dev-report), TK013 (verification), TK014 (gate-disposition), TK015 (external review), GATE-002. Updated TK001–TK006 to depend on TK000. Updated Non-goal to acknowledge two-gate model. Source: T102-PH001-ST002-AC000-TK000 consultation session (2026-03-28); IMPLEMENTATION artifact `implementation_T102-PH001-ST002-AC000_tk000-plan-readiness-amendments.md`. |
```

---

### SPEC-005 — Assess and Amend `plan_T102-PH001-ST002.md` (Stream Plan AC000 Contract Stub)

| Field | Detail |
|:--|:--|
| Requirement Source | `guideline_workspace_plan.md` §IV.D requires that when a dedicated Activity Plan exists, the Stream plan retains a minimal contract stub. The AC000 contract stub in the stream plan must be assessed for consistency with the amended activity plan. |
| Target file(s) | `prompt/artifacts/tasks/T102/workspace/PH001/ST002/plan_T102-PH001-ST002.md` |
| Required end-state posture | AC000 contract stub accurately reflects the two-gate model and amended deliverable scope; Success Criteria Checklist summary acknowledges GATE-002; version bumped |
| Explicit non-target / do-not-change constraints | Do NOT modify AC001–AC004 sections. Do NOT modify Sections I–III (Executive Summary, Stream Decision Summary, Stream Outline) beyond what is needed for AC000 consistency. Do NOT modify the Activity Register row for AC000 beyond updating the `Deliverable` column if needed. |
| Validation check | (1) AC000 section mentions both GATE-001 and GATE-002; (2) Success Criteria Checklist includes implementation-backed gate; (3) version bumped; (4) changelog entry added |
| Blocking ambiguity rule | If the current file version differs from v2.0.0, STOP and re-read the file before applying mutations. |
| Status | `open` |

#### Implementation Detail

**Step 1: Update frontmatter**

Change:
```yaml
version: '2.0.0'
date: '2026-03-27'
```
to:
```yaml
version: '2.1.0'
date: '2026-03-28'
```

**Step 2: Assess and amend AC000 contract stub (Section IV, Activity AC000)**

The current AC000 section (lines 74–98) includes:
- Purpose ✓ (no change needed)
- Deliverable: currently references only the calibrated scope brief. Add acknowledgment of the implementation deliverable reviewed at GATE-002.

Replace the Deliverable block:

Current:
```markdown
**Deliverable**: A calibrated scope brief analysis artifact (`analysis_T102-PH001-ST002-AC000_calibrated-scope-brief.md`) documenting:
1. Per-STD content verification results (ST005 delta coverage: present/missing/malformed)
2. Per-STD P-STD-001 structural gap inventory
3. T102-STD-004 supersession status
4. Calibrated scope guidance for AC001-AC004
```

Replace with:
```markdown
**Deliverable**:
- GATE-001 deliverable: A calibrated scope brief analysis artifact (`analysis_T102-PH001-ST002-AC000_calibrated-scope-brief.md`) documenting: (1) per-STD content verification results, (2) per-STD P-STD-001 structural gap inventory, (3) T102-STD-004 supersession status, (4) calibrated scope guidance for AC001-AC004.
- GATE-002 deliverable: Verified implementation of T102-STD-004 supersession housekeeping and any content remediation items seeded by GATE-001 findings.
```

**Step 3: Amend Success Criteria Checklist (summary)**

Current:
```markdown
**Success Criteria Checklist (summary)**:
- [ ] Per-STD content verification completed for STD-001, STD-003, STD-006, STD-007
- [ ] P-STD-001 structural gap inventory produced for all T102-STDs
- [ ] T102-STD-004 marked as superseded with forward reference to P-STD-001
- [ ] Calibrated scope brief produced with per-AC focus guidance
- [ ] Client approval via GATE-001
```

Replace with:
```markdown
**Success Criteria Checklist (summary)**:
- [ ] Per-STD content verification completed for STD-001, STD-003, STD-006, STD-007
- [ ] P-STD-001 structural gap inventory produced for all T102-STDs
- [ ] Calibrated scope brief produced with per-AC focus guidance
- [ ] Client approval of diagnostic deliverables via GATE-001 (consultation-only)
- [ ] T102-STD-004 supersession housekeeping implemented and verified
- [ ] Client approval of implementation deliverables via GATE-002 (implementation-backed)
```

**Step 4: Add changelog entry**

Append a new row to the Changelog table (Section VI):

```markdown
| v2.1.0 | 2026-03-28 | Amendment | AC000 contract stub updated to reflect two-gate model (GATE-001 consultation-only + GATE-002 implementation-backed). Deliverable section expanded. Success Criteria Checklist updated. Source: T102-PH001-ST002-AC000-TK000 plan readiness amendments. |
```

---

## IV. IMPLEMENTATION SEQUENCE

The recommended execution order is:

```
SPEC-001 (guideline_workspace_plan.md §VI.L amendment)
  → SPEC-002 (workspace_documentation_rules.md §7.A and §8 amendment)
    → SPEC-003 (template_workspace_plan_activity.md update)
      → SPEC-004 (plan_T102-PH001-ST002-AC000.md amendment)
        → SPEC-005 (plan_T102-PH001-ST002.md stream plan check)
```

Rationale:
- SPEC-001 establishes the normative authority (guideline) that SPEC-003 and SPEC-004 reference.
- SPEC-002 aligns the companion rules document with the guideline amendment.
- SPEC-003 aligns the template with the guideline.
- SPEC-004 applies the plan amendments under the authority of the amended guideline.
- SPEC-005 is a conformance check that depends on SPEC-004's final state.

SPEC-001 and SPEC-002 are independent and MAY be executed in parallel. SPEC-003 depends on SPEC-001. SPEC-004 depends on SPEC-001. SPEC-005 depends on SPEC-004.

## V. REFERENCES

| Document | Path |
|:--|:--|
| Governing Plan | `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/plan_T102-PH001-ST002-AC000.md` |
| Stream Plan | `prompt/artifacts/tasks/T102/workspace/PH001/ST002/plan_T102-PH001-ST002.md` |
| Plan Guideline | `prompt/templates/consultant/workspace/guideline_workspace_plan.md` |
| Documentation Rules | `prompt/templates/consultant/workspace/workspace_documentation_rules.md` |
| Activity Plan Template | `prompt/templates/consultant/workspace/template_workspace_plan_activity.md` |
| Analysis Guideline | `prompt/templates/consultant/workspace/guideline_workspace_analysis.md` |
| Implementation Guideline | `prompt/templates/consultant/workspace/guideline_workspace_implementation.md` |
| Block A Implementation (exemplar) | `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/implementation/implementation_T102-PH001-ST002-AC000_block-a-planning-housekeeping.md` |
| Plan Guideline Changelog | `prompt/templates/consultant/workspace/changelog/changelog_guideline_workspace_plan.md` |
| Documentation Rules Changelog | `prompt/templates/consultant/workspace/changelog/changelog_workspace_documentation_rules.md` |

## VI. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-03-28 | Initial | TK000 plan readiness amendments implementation specification created. 5 SPEC items: SPEC-001 (guideline §VI.L external review step), SPEC-002 (documentation rules §7.A/§8 alignment), SPEC-003 (activity plan template update), SPEC-004 (AC000 activity plan amendment with TK000 + TK009 + GATE-002 stack), SPEC-005 (stream plan contract stub update). Source: T102-PH001-ST002-AC000-TK000 consultation session (2026-03-28). |
