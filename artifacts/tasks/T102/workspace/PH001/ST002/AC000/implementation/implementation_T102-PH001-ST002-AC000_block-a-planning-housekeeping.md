---
artifact_type: 'IMPLEMENTATION'
implementation_type: 'task_specification'
initiative_id: 'T102'
initiative_code: 'CWD'
phase: '1'
stream_id: 'T102-PH001-ST002'
activity_id: 'T102-PH001-ST002-AC000'
task_id: 'T102-PH001-ST002-AC000 (Block A: multi-task planning scope)'
version: '1.0.0'
date: '2026-03-27'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T102/workspace/PH001/ST002/plan_T102-PH001-ST002.md'
execution_audience: 'consultant'
purpose: 'Detailed implementation specification for Block A (Planning & Housekeeping) of the T102 development re-initialization: ST005 formal closure, ST002 stream plan amendment, and AC000 Activity Plan creation'
---

# IMPLEMENTATION (Task Specification): Block A -- T102 Re-Initialization Planning & Housekeeping

## I. PURPOSE & AUTHORITY

- **Purpose**: This artifact specifies the exact file mutations required for Block A of the T102 development re-initialization. Block A encompasses three logical actions: (A1) formally closing ST005 with implicit-gate-passage notation and verification deferral; (A2) amending ST002's stream plan to reflect P-STD-001 as the governing structural authority, fix compliance gaps, and expand AC000's contract scope; (A3) creating a standalone AC000 Activity Plan with full task decomposition for AC000 execution in the next session.
- **Authority chain**: The governing stream plan (`plan_T102-PH001-ST002.md`) authorizes this work at the AC000 activity level. This artifact specifies HOW the planning housekeeping is performed. Execution evidence for this Block A work is captured via the plan changelog entries themselves (consultant-owned planning work, no dev-report required).
- **Audience**: `LLM_Consultant` (execution_audience: consultant). This is consultant-owned planning and housekeeping work. No developer execution or dev-report is required.
- This artifact does NOT hold a GDR. Gate decisions are recorded in gate_disposition proposals per `guideline_workspace_proposal.md` Section VII.

## II. TASK SCOPE

- **Governing plan task**: `T102-PH001-ST002-AC000` (Block A subset -- planning and housekeeping only; Block B execution tasks are out of scope)
- **Trigger**: Task complexity exceeds plan-step capacity. Three separate files must be mutated/created with precise cross-referencing, template compliance, and normative baseline alignment. The AC000 Activity Plan creation alone requires detailed delta-extraction from ST005 into verification tasks.
- **Deliverable contract**: (1) ST005 plan formally closed; (2) ST002 stream plan amended for P-STD-001 alignment and compliance fixes; (3) AC000 standalone Activity Plan created and ready for next-session execution.

## III. SPECIFICATION ITEMS

### SPEC-001 -- Close ST005 Stream Plan (Frontmatter & Activity Register)

| Field | Detail |
|:--|:--|
| Requirement Source | Consultation session decision: ST005 was executed but housekeeping not performed; approved approach is to close with implicit gate passage and verification deferral to ST002-AC000 |
| Target file(s) | `prompt/artifacts/tasks/T102/workspace/PH001/ST005/plan_T102-PH001-ST005.md` |
| Required end-state posture | Frontmatter `status` is `completed`; Activity Register reflects execution reality; changelog documents closure rationale |
| Explicit non-target / do-not-change constraints | Do NOT modify Activity section bodies (Section IV task registers, success criteria, scope descriptions). These are preserved as historical planning detail that AC000 will reference for verification. Do NOT modify Section II (Stream Decision Summary), Section III (Stream Outline), or Section V-VI (Links Register, Open Questions). |
| Validation check | (1) Frontmatter `status: 'completed'`; (2) AC001-AC004 Activity Register `Status` = `completed`; (3) AC005 remains `cancelled`; (4) Changelog v3.4.0 entry exists with closure rationale |
| Blocking ambiguity rule | If the current file version differs from v3.2.0/v3.3.0 as read during this consultation, STOP and re-read the file before applying mutations |
| Status | `open` |

#### Implementation Detail

**Step 1: Update frontmatter**

Change line 10 from:
```yaml
status: 'draft'
```
to:
```yaml
status: 'completed'
```

**Step 2: Update Activity Register rows (Section III)**

The Activity Register table starts at line 83. Update `Status` column for AC001-AC004 rows:

| Activity | Current Status | New Status |
|:--|:--|:--|
| AC001 | `planned` | `completed` |
| AC002 | `planned` | `completed` |
| AC003 | `planned` | `completed` |
| AC004 | `planned` | `completed` |
| AC005 | `cancelled` | `cancelled` (no change) |

The exact table rows after mutation:

```markdown
| AC001 | `T102-PH001-ST005-AC001` | Amend `T102-STD-007` (Issues & Risks Index) | `completed` | LLM_Consultant | ST004-AC001 GATE-003 (passed 2026-02-09) | `T102-STD-007` v2.0.0 (Deltas 1-4 from RES-004) |
| AC002 | `T102-PH001-ST005-AC002` | Amend `T102-STD-003` (Explicit Inheritance Model) | `completed` | LLM_Consultant | ST004-AC002 GATE-003 (passed 2026-02-10) | `T102-STD-003` v2.0.0 (Deltas A1-A4 from RES-005) |
| AC003 | `T102-PH001-ST005-AC003` | Amend `T102-STD-006` (Research Artifacts Index) | `completed` | LLM_Consultant | ST004-AC002 GATE-003 (passed 2026-02-10) | `T102-STD-006` v2.0.0 (Deltas B1-B4 from RES-005) |
| AC004 | `T102-PH001-ST005-AC004` | Amend `T102-STD-001` (Consultancy Operating Model) | `completed` | LLM_Consultant | ST004-AC003 GATE-003 (passed 2026-02-10) | `T102-STD-001` amended (Deltas A1-A5 from RES-006; absorbs RES-005 D1-D2) |
| AC005 | `T102-PH001-ST005-AC005` | Amend `T102-STD-005` (ID Specification & Rules) | `cancelled` | LLM_Consultant | ST004-AC002 GATE-003 (passed 2026-02-10) | Scope absorbed into P-PH000-ST001-AC006 (P-STD-005 promotion); deltas verified as pre-promotion task (TK002). |
```

**Step 3: Add changelog entry**

Append a new row to the changelog table (Section VII, after the v3.3.0 row):

```markdown
| v3.4.0 | 2026-03-27 | Closure | Stream formally closed. AC001-AC004 statuses updated to `completed`. Gates were implicitly passed via execution; formal gate-disposition proposals were not authored. Amendments were applied without P-STD-001 structural conformance (P-STD-001 approved 2026-02-22, supersedes T102-STD-004). Content verification of amendment correctness is deferred to T102-PH001-ST002-AC000. Evidence: T102-PH001-ST002-AC000 consultation session (2026-03-27). |
```

---

### SPEC-002 -- Amend ST002 Stream Plan (Frontmatter Fixes)

| Field | Detail |
|:--|:--|
| Requirement Source | Compliance findings F-01 (procedural_guideline), template compliance assessment |
| Target file(s) | `prompt/artifacts/tasks/T102/workspace/PH001/ST002/plan_T102-PH001-ST002.md` |
| Required end-state posture | Frontmatter `procedural_guideline` points to `guideline_workspace_plan.md`; `version` bumped; `date` updated |
| Explicit non-target / do-not-change constraints | Do NOT change `governance_rules`, `parent_plan`, `depends_on`, `initiative_id`, `initiative_code`, `phase`, `stream_id`, `author`, `decision_owner_role` |
| Validation check | (1) `procedural_guideline` value matches `prompt/templates/consultant/workspace/guideline_workspace_plan.md`; (2) `version` is `2.0.0`; (3) `date` is `2026-03-27` |
| Blocking ambiguity rule | If the current file version differs from v1.0.0/v1.1.0, STOP and re-read |
| Status | `open` |

#### Implementation Detail

Change frontmatter lines 14, 8, and 9 from:
```yaml
version: '1.0.0'
date: '2026-02-11'
...
procedural_guideline: 'prompt/templates/consultant/workspace/guideline_workspace_roadmap.md'
```
to:
```yaml
version: '2.0.0'
date: '2026-03-27'
...
procedural_guideline: 'prompt/templates/consultant/workspace/guideline_workspace_plan.md'
```

---

### SPEC-003 -- Amend ST002 Stream Plan (Fix Broken Path References)

| Field | Detail |
|:--|:--|
| Requirement Source | Compliance finding F-06: path `prompt/artifacts/tasks/T102/consultant/standards/` does not exist |
| Target file(s) | `prompt/artifacts/tasks/T102/workspace/PH001/ST002/plan_T102-PH001-ST002.md` |
| Required end-state posture | All references to the non-existent `consultant/standards/` path are replaced with the actual path `prompt/artifacts/tasks/T102/standard/` |
| Explicit non-target / do-not-change constraints | Do NOT modify any other paths or links in the document |
| Validation check | No occurrences of `consultant/standards/` remain in the file |
| Blocking ambiguity rule | If additional broken paths are discovered during execution, note them but do not fix paths not listed here without escalation |
| Status | `open` |

#### Implementation Detail

There are exactly 2 occurrences of the broken path in the current file:

**Occurrence 1 (AC000, line 92)**:
Change:
```
- All amended STD files under `prompt/artifacts/tasks/T102/consultant/standards/`
```
to:
```
- All amended STD files under `prompt/artifacts/tasks/T102/standard/`
```

**Occurrence 2 (AC001, line 125)**:
Change:
```
- All STD files under `prompt/artifacts/tasks/T102/consultant/standards/`
```
to:
```
- All STD files under `prompt/artifacts/tasks/T102/standard/`
```

---

### SPEC-004 -- Amend ST002 Stream Plan (Replace T102-STD-004 References with P-STD-001)

| Field | Detail |
|:--|:--|
| Requirement Source | P-STD-001 (v1.1.0, approved 2026-02-22) explicitly supersedes T102-STD-004. All normative baseline references in ST002 must be updated. |
| Target file(s) | `prompt/artifacts/tasks/T102/workspace/PH001/ST002/plan_T102-PH001-ST002.md` |
| Required end-state posture | All references to T102-STD-004 as the governing structural exemplar are updated to P-STD-001. Historical/contextual mentions of T102-STD-004 (e.g., in changelog, execution deviation acknowledgment) are preserved but annotated. |
| Explicit non-target / do-not-change constraints | Do NOT modify the changelog history entries (v0.1.0 through v1.1.0) -- these are historical records. Do NOT modify Section II (Stream Decision Summary) locked decisions. |
| Validation check | (1) No reference to "STD-004 exemplar" or "STD-004 golden exemplar" as a current baseline remains; (2) P-STD-001 is cited as the structural authority; (3) Historical/locked references are annotated, not deleted |
| Blocking ambiguity rule | If a T102-STD-004 reference is ambiguous (could be historical or current), preserve it with an annotation rather than replacing |
| Status | `open` |

#### Implementation Detail

**Change 1: Section I, Executive Summary -- Phase 1 decision dependencies (line 30-34)**

Change:
```markdown
- Model D (Combined STD+DR Files): STD bodies + embedded `Specification/CLAUSE` + nested `Decision Record` live in one combined file per STD under `prompt/artifacts/tasks/T102/consultant/standards/`.
- STD-contains-CLAUSE: the combined file **is** the STD; CLAUSEs use `STDCID` addressing (e.g., `T102-STD-004-CLAUSE-001`).
```
to:
```markdown
- Model D (Combined STD+DR Files): STD bodies + embedded `Specification/CLAUSE` + nested `Decision Record` live in one combined file per STD under `prompt/artifacts/tasks/T102/standard/`.
- STD-contains-CLAUSE: the combined file **is** the STD; CLAUSEs use `STDCID` addressing (e.g., `T102-STD-001-CLAUSE-001`). Structural authority is now governed by `P-STD-001` (supersedes `T102-STD-004`, effective 2026-02-22).
```

**Change 2: Section I, Executive Summary -- ST001-AC008 reference (line 34)**

Change:
```markdown
- ST001-AC008 (STD-004 self-compliance audit) SHOULD complete before ST002 execution to ensure the exemplar pattern is hardened.
```
to:
```markdown
- ST001-AC008 (STD-004 self-compliance audit) is historically noted. The exemplar authority is now `P-STD-001` (supersedes `T102-STD-004`, effective 2026-02-22). AC001 structural gap analysis will use `P-STD-001` as the conformance baseline.
```

**Change 3: Section IV, AC001 Scope (line 120)**

Change:
```markdown
- In scope: Gap analysis of all T102-STDs against STD-contains-CLAUSE model expectations; focus on residual gaps identified by AC000; verification that ST003-migrated STDs conform to the STD-004 exemplar pattern; identification of any STD-004 CLAUSE violations in the broader STD set.
```
to:
```markdown
- In scope: Gap analysis of all T102-STDs against `P-STD-001` structural conformance requirements (CLAUSE-001 canonical file structure, CLAUSE-018 CLAUSE construction, CLAUSE-031 frontmatter, CLAUSE-028 references/provenance); focus on residual gaps identified by AC000; identification of structural non-conformance in the broader T102-STD set.
```

**Change 4: Section IV, AC001 Inputs Required (lines 124-128)**

Change:
```markdown
- All STD files under `prompt/artifacts/tasks/T102/consultant/standards/`
- STD-004 golden exemplar (post-AC008 if available): `prompt/artifacts/tasks/T102/standard/standard_T102-STD-004_specification-standard-and-guideline.md`
```
to:
```markdown
- All STD files under `prompt/artifacts/tasks/T102/standard/`
- P-STD-001 (structural authority): `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md`
```

**Change 5: Section IV, AC001 Task Register (line 133)**

Change:
```markdown
| ST002-AC001-TK001 | Assess each T102-STD against STD-004 exemplar structural conformance (CLAUSE-016 file structure, CLAUSE-005 clause format, CLAUSE-012 references/provenance) | `planned` | — |
```
to:
```markdown
| ST002-AC001-TK001 | Assess each T102-STD against P-STD-001 structural conformance (P-STD-001-CLAUSE-001 canonical file structure, P-STD-001-CLAUSE-018 CLAUSE construction, P-STD-001-CLAUSE-031 frontmatter, P-STD-001-CLAUSE-028 references/provenance) | `planned` | — |
```

**Change 6: Section IV, AC002 Scope (line 154)**

Change:
```markdown
- In scope: Verification contract normalization across the post-amendment STD set; defining what "verification" means per CLAUSE type (structural, content, reference integrity); applying the pattern from STD-004's CLAUSE-015 (Automation & Linting Checks) as the exemplar.
```
to:
```markdown
- In scope: Verification contract normalization across the post-amendment STD set; defining what "verification" means per CLAUSE type (structural, content, reference integrity); applying the pattern from P-STD-001-CLAUSE-007 (Automation & Linting Checks) as the exemplar.
```

**Change 7: Section IV, AC002 Task Register (line 160)**

Change:
```markdown
| ST002-AC002-TK001 | Define verification contract schema using STD-004-CLAUSE-015 as exemplar pattern (structural checks, content checks, reference integrity checks) | `planned` | — |
```
to:
```markdown
| ST002-AC002-TK001 | Define verification contract schema using P-STD-001-CLAUSE-007 as exemplar pattern (structural checks, content checks, reference integrity checks) | `planned` | — |
```

**Change 8: Section V, Links Register (line 232)**

Change:
```markdown
| Standard (exemplar) | STD-004 golden exemplar | `prompt/artifacts/tasks/T102/standard/standard_T102-STD-004_specification-standard-and-guideline.md` |
```
to:
```markdown
| Standard (structural authority) | P-STD-001 Program Governance Standard | `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md` |
| Standard (superseded exemplar) | T102-STD-004 (superseded by P-STD-001, 2026-02-22) | `prompt/artifacts/tasks/T102/standard/standard_T102-STD-004_specification-standard-and-guideline.md` |
```

---

### SPEC-005 -- Amend ST002 Stream Plan (Fix Activity Heading Levels)

| Field | Detail |
|:--|:--|
| Requirement Source | Compliance finding F-05: Activity headings use `####` (h4) instead of `###` (h3) per stream plan template |
| Target file(s) | `prompt/artifacts/tasks/T102/workspace/PH001/ST002/plan_T102-PH001-ST002.md` |
| Required end-state posture | All Activity section headings under Section IV use `###` (h3) level |
| Explicit non-target / do-not-change constraints | Do NOT change the `## IV. ACTIVITIES` section heading itself (remains h2). Do NOT change heading text content. |
| Validation check | All Activity headings match pattern `### Activity AC0xx:` |
| Blocking ambiguity rule | None |
| Status | `open` |

#### Implementation Detail

There are exactly 5 Activity headings to fix:

| Line | Current | Required |
|:--|:--|:--|
| 74 | `#### Activity AC000: ST005 Remediation Accounting & Scope Calibration` | `### Activity AC000: ST005 Remediation Accounting & Scope Calibration` |
| 111 | `#### Activity AC001: STD Adoption & Verification Gap Analysis (Post-Amendment)` | `### Activity AC001: STD Adoption & Verification Gap Analysis (Post-Amendment)` |
| 145 | `#### Activity AC002: STD Verification Contract Normalization` | `### Activity AC002: STD Verification Contract Normalization` |
| 171 | `#### Activity AC003: STD Verification Expectations (Review Checklist)` | `### Activity AC003: STD Verification Expectations (Review Checklist)` |
| 193 | `#### Activity AC004: SSOT Alignment Plan (SPS + Concept)` | `### Activity AC004: SSOT Alignment Plan (SPS + Concept)` |

---

### SPEC-006 -- Amend ST002 Stream Plan (Add Reference Column & Update AC000 Contract Stub)

| Field | Detail |
|:--|:--|
| Requirement Source | Compliance finding F-02 (missing Reference column); expanded AC000 scope per consultation approval |
| Target file(s) | `prompt/artifacts/tasks/T102/workspace/PH001/ST002/plan_T102-PH001-ST002.md` |
| Required end-state posture | (1) Activity Register has `Reference` column per template; (2) AC000 contract stub reflects expanded scope (content verification + P-STD-001 structural gap + T102-STD-004 supersession housekeeping + calibrated scope brief); (3) AC000 depends_on updated to reflect ST005 implicit completion |
| Explicit non-target / do-not-change constraints | Do NOT modify AC001-AC004 contract stubs (those will be updated post-AC000 based on calibrated scope brief). Do NOT add standalone Activity Plan links for AC001-AC004 (those do not exist). |
| Validation check | (1) Activity Register has 8 columns including `Reference`; (2) AC000 row has path to Activity Plan; (3) AC000 depends_on reflects ST005 completed status |
| Blocking ambiguity rule | None |
| Status | `open` |

#### Implementation Detail

**Step 1: Replace Activity Register table (Section III, lines 62-68)**

Replace the entire Activity Register table with:

```markdown
| Activity | Activity ID | Name | Status | Owner | Depends On | Deliverable | Reference |
|:--|:--|:--|:--|:--|:--|:--|:--|
| AC000 | `T102-PH001-ST002-AC000` | ST005 Verification, P-STD-001 Gap Assessment & Scope Calibration | `planned` | LLM_Consultant | ST005 (completed 2026-03-27) | Calibrated scope brief (analysis artifact) for AC001-AC004 | `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/plan_T102-PH001-ST002-AC000.md` |
| AC001 | `T102-PH001-ST002-AC001` | STD adoption & verification gap analysis (post-amendment) | `planned` | LLM_Consultant | AC000 | Gap inventory + remediation checklist (against P-STD-001 conformance) | -- |
| AC002 | `T102-PH001-ST002-AC002` | STD verification contract normalization | `planned` | LLM_Consultant | AC001 | Consistent verification contract pattern across all T102-STDs | -- |
| AC003 | `T102-PH001-ST002-AC003` | STD verification expectations (review checklist) | `planned` | LLM_Consultant | AC002 | Standardized review-executable checklist per STD | -- |
| AC004 | `T102-PH001-ST002-AC004` | SSOT alignment plan (SPS + Concept) | `planned` | LLM_Consultant | AC002, AC003 | Bounded SSOT changeset plan + validation checklist | -- |
```

**Step 2: Replace AC000 Activity section (Section IV, starting at line 74)**

Replace the entire AC000 activity section (from `### Activity AC000:` through the `---` separator before AC001) with:

```markdown
### Activity AC000: ST005 Verification, P-STD-001 Gap Assessment & Scope Calibration

**Activity ID**: `T102-PH001-ST002-AC000`

**Purpose**: Verify that ST005's research-driven CLAUSE amendments were correctly applied to T102-STD-001, STD-003, STD-006, and STD-007; assess each T102-STD against P-STD-001 structural conformance requirements; perform T102-STD-004 supersession housekeeping; and produce a calibrated scope brief that AC001-AC004 consume as their primary input.

**Deliverable**: A calibrated scope brief analysis artifact (`analysis_T102-PH001-ST002-AC000_calibrated-scope-brief.md`) documenting:
1. Per-STD content verification results (ST005 delta coverage: present/missing/malformed)
2. Per-STD P-STD-001 structural gap inventory
3. T102-STD-004 supersession status
4. Calibrated scope guidance for AC001-AC004

**Scope**:
- In scope: Content verification of ST005 amendments against research deltas; P-STD-001 structural gap assessment; T102-STD-004 supersession housekeeping; calibrated scope brief production
- Excludes: Performing structural remediation (AC001 scope); drafting verification contracts (AC002 scope); SSOT updates (AC004 scope)

**Activity Plan**: `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/plan_T102-PH001-ST002-AC000.md`

**Success Criteria Checklist (summary)**:
- [ ] Per-STD content verification completed for STD-001, STD-003, STD-006, STD-007
- [ ] P-STD-001 structural gap inventory produced for all T102-STDs
- [ ] T102-STD-004 marked as superseded with forward reference to P-STD-001
- [ ] Calibrated scope brief produced with per-AC focus guidance
- [ ] Client approval via GATE-001
```

**Step 3: Update Section I cross-stream dependency callout (line 36)**

Change:
```markdown
> **Cross-stream dependency**: ST002-AC000 depends on all ST005 activities reaching GATE-001 approval. ST002-AC004 (SSOT alignment) must also account for ST006 outputs (Concept hygiene + I&R aggregation).
```
to:
```markdown
> **Cross-stream dependency**: ST005 was formally closed (v3.4.0, 2026-03-27) with gates implicitly passed. ST002-AC000 now verifies ST005 amendment content as its first task. ST002-AC004 (SSOT alignment) must also account for ST006 outputs (Concept hygiene + I&R aggregation) and T102-STD-004 supersession by P-STD-001.
```

---

### SPEC-007 -- Amend ST002 Stream Plan (Changelog Entry)

| Field | Detail |
|:--|:--|
| Requirement Source | All plan amendments require changelog documentation per `guideline_workspace_plan.md` |
| Target file(s) | `prompt/artifacts/tasks/T102/workspace/PH001/ST002/plan_T102-PH001-ST002.md` |
| Required end-state posture | Changelog has v2.0.0 entry documenting the P-STD-001 alignment amendment |
| Explicit non-target / do-not-change constraints | Do NOT modify existing changelog rows (v0.1.0 through v1.1.0) |
| Validation check | v2.0.0 row exists in changelog |
| Blocking ambiguity rule | None |
| Status | `open` |

#### Implementation Detail

Append a new row to the changelog table (Section VI, after the v1.1.0 row):

```markdown
| v2.0.0 | 2026-03-27 | Major Amendment | P-STD-001 alignment: replaced all T102-STD-004 exemplar references with P-STD-001 (supersedes T102-STD-004, effective 2026-02-22). Fixed broken path `consultant/standards/` to `standard/`. Fixed procedural_guideline frontmatter to guideline_workspace_plan.md. Fixed Activity heading levels (h4 to h3). Added Reference column to Activity Register. Expanded AC000 scope to include ST005 content verification, P-STD-001 structural gap assessment, and T102-STD-004 supersession housekeeping. Linked AC000 standalone Activity Plan. Updated cross-stream dependency note for ST005 formal closure. Evidence: T102-PH001-ST002-AC000 consultation session (2026-03-27). |
```

---

### SPEC-008 -- Create AC000 Standalone Activity Plan

| Field | Detail |
|:--|:--|
| Requirement Source | AC000 expanded scope triggers standalone Activity Plan creation per `guideline_workspace_plan.md` Section VIII.C (>=5 tasks, detailed step decomposition needed, scope exceeds contract-level) |
| Target file(s) | `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/plan_T102-PH001-ST002-AC000.md` (NEW file) |
| Required end-state posture | Complete Activity Plan per `template_workspace_plan_activity.md` (v1.3.0) with: full frontmatter; Executive Summary; Activity Outline with Task Register; Tasks (Detailed) sections for all tasks including consultation-only Gate-Readiness Stack; Links Register; Changelog |
| Explicit non-target / do-not-change constraints | Do NOT create any execution artifacts (analysis, notes, proposals) at this stage -- those are Block B deliverables. Do NOT pre-populate task Action columns (all remain `--`). |
| Validation check | (1) File exists at specified path; (2) Frontmatter complies with activity plan template; (3) Task Register has correct column schema per template; (4) All tasks have detailed sections; (5) Gate follows consultation-only sequence (no DEV-REPORT/VERIFICATION tasks); (6) Links Register references parent stream plan |
| Blocking ambiguity rule | If the template version has changed from v1.3.0, re-read the template before authoring |
| Status | `open` |

#### Implementation Detail

Create the file `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/plan_T102-PH001-ST002-AC000.md` with the following exact content:

```markdown
---
artifact_type: 'PLAN'
planning_level: 'ACTIVITY'
initiative_id: 'T102'
initiative_code: 'CWD'
phase: '1'
stream_id: 'T102-PH001-ST002'
activity_id: 'T102-PH001-ST002-AC000'
version: '1.0.0'
date: '2026-03-27'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
governance_rules: 'prompt/templates/consultant/workspace/workspace_documentation_rules.md'
parent_plan: 'prompt/artifacts/tasks/T102/workspace/PH001/ST002/plan_T102-PH001-ST002.md'
---

# PLAN: T102 (CWD) - Phase 1 / Stream ST002 / Activity AC000: ST005 Verification, P-STD-001 Gap Assessment & Scope Calibration

## I. EXECUTIVE SUMMARY

**Purpose**: Verify that ST005's research-driven CLAUSE amendments (from RES-004, RES-005, RES-006 integration analyses) were correctly applied to the four targeted T102-STDs; assess all T102-STD files against P-STD-001 structural conformance requirements; perform T102-STD-004 supersession housekeeping; and produce a calibrated scope brief that governs AC001-AC004 execution focus.

**Non-goal**: This activity does NOT perform structural remediation of T102-STDs (AC001 scope), draft verification contracts (AC002), or modify SSOT artifacts (AC004). It is a diagnostic and calibration pass only, except for the T102-STD-004 supersession housekeeping which is a bounded one-file mutation.

---

## II. ACTIVITY OUTLINE

**Activity ID**: `T102-PH001-ST002-AC000`
**Objective**: Establish a verified content baseline and structural gap inventory for the T102-STD set, enabling AC001-AC004 to proceed with precise, calibrated scope.
**Execution Mode**: SEQUENTIAL
**Depends On**: T102-PH001-ST005 (completed 2026-03-27, gates implicitly passed)

**Context**:
- `prompt/artifacts/tasks/T102/standard/standard_T102-STD-001_consultancy-operating-model.md`
- `prompt/artifacts/tasks/T102/standard/standard_T102-STD-003_explicit-inheritance-model.md`
- `prompt/artifacts/tasks/T102/standard/standard_T102-STD-006_research-artifacts-index.md`
- `prompt/artifacts/tasks/T102/standard/standard_T102-STD-007_issues-risks-index.md`
- `prompt/artifacts/tasks/T102/standard/standard_T102-STD-004_specification-standard-and-guideline.md`
- `prompt/artifacts/tasks/T102/standard/standard_T102-STD-002_canonical-yaml-header.md`
- `prompt/artifacts/tasks/T102/standard/standard_T102-STD-005_id-specification-rules.md`
- `prompt/artifacts/tasks/T102/standard/standard_T102-STD-008_organisation-baseline-index.md`
- `prompt/artifacts/tasks/T102/standard/standard_T102-STD-009_governance-standards-specification.md`
- `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md`
- `prompt/artifacts/tasks/T102/workspace/PH000/analysis/analysis_T102-RES-004_issues-risks-architecture.md`
- `prompt/artifacts/tasks/T102/workspace/PH000/analysis/analysis_T102-RES-005_cross-scope-coordination-architecture.md`
- `prompt/artifacts/tasks/T102/workspace/PH000/analysis/analysis_T102-RES-006_integration-impact.md`
- `prompt/artifacts/tasks/T102/workspace/PH001/ST005/plan_T102-PH001-ST005.md`

### Task Register

| Task | Task ID | Name | Status | Owner | Depends On | Target | Reference | Action |
|:--|:--|:--|:--|:--|:--|:--|:--|:--|
| TK001 | `T102-PH001-ST002-AC000-TK001` | Verify STD-007 amendments (RES-004 Deltas 1-4 + RES-006 D1) | `planned` | LLM_Consultant | -- | `standard_T102-STD-007_issues-risks-index.md` | ST005-AC001 task descriptions | -- |
| TK002 | `T102-PH001-ST002-AC000-TK002` | Verify STD-003 amendments (RES-005 Deltas A1-A4) | `planned` | LLM_Consultant | -- | `standard_T102-STD-003_explicit-inheritance-model.md` | ST005-AC002 task descriptions | -- |
| TK003 | `T102-PH001-ST002-AC000-TK003` | Verify STD-006 amendments (RES-005 Deltas B1-B4 + RES-006 C1) | `planned` | LLM_Consultant | -- | `standard_T102-STD-006_research-artifacts-index.md` | ST005-AC003 task descriptions | -- |
| TK004 | `T102-PH001-ST002-AC000-TK004` | Verify STD-001 amendments (RES-006 Deltas A1-A5, absorbs RES-005 D1-D2) | `planned` | LLM_Consultant | -- | `standard_T102-STD-001_consultancy-operating-model.md` | ST005-AC004 task descriptions | -- |
| TK005 | `T102-PH001-ST002-AC000-TK005` | P-STD-001 structural gap assessment (all T102-STDs) | `planned` | LLM_Consultant | TK001, TK002, TK003, TK004 | All `standard_T102-STD-*.md` files | P-STD-001 | -- |
| TK006 | `T102-PH001-ST002-AC000-TK006` | T102-STD-004 supersession housekeeping | `planned` | LLM_Consultant | -- | `standard_T102-STD-004_specification-standard-and-guideline.md` | P-STD-001 `supersedes` field | -- |
| TK007 | `T102-PH001-ST002-AC000-TK007` | Produce calibrated scope brief for AC001-AC004 | `planned` | LLM_Consultant | TK001, TK002, TK003, TK004, TK005, TK006 | `analysis_T102-PH001-ST002-AC000_calibrated-scope-brief.md` | -- | -- |
| TK008 | `T102-PH001-ST002-AC000-TK008` | Produce GATE-001 gate-disposition proposal | `planned` | LLM_Consultant | TK007 | `proposal/` | `guideline_workspace_proposal.md` | -- |
| GATE-001 | `T102-PH001-ST002-AC000-GATE-001` | Gate: Client approval of AC000 deliverables | `planned` | Client | TK008 | Pass/fail | `guideline_workspace_plan.md` | -- |

---

## III. TASKS (DETAILED)

### Task TK001: Verify STD-007 Amendments (RES-004 Deltas 1-4 + RES-006 D1)

**Task ID**: `T102-PH001-ST002-AC000-TK001`

**Purpose**: Verify that the 5 amendment items planned in ST005-AC001 are present and content-correct in the current `standard_T102-STD-007_issues-risks-index.md` file.

**Deliverable**:
- Per-delta verification result (present/missing/malformed) recorded in TK007's calibrated scope brief

**Scope**:
- In scope: Content verification of 5 specific amendment items against research delta specifications
- Out of scope: Structural conformance assessment (TK005 scope); CLAUSE drafting or remediation

**Inputs Required**:
- `prompt/artifacts/tasks/T102/standard/standard_T102-STD-007_issues-risks-index.md` -- current STD file to verify
- `prompt/artifacts/tasks/T102/workspace/PH000/analysis/analysis_T102-RES-004_issues-risks-architecture.md` v1.1.0 (Section III: Delta List) -- canonical delta definitions
- `prompt/artifacts/tasks/T102/workspace/PH000/analysis/analysis_T102-RES-006_integration-impact.md` v1.0.0 (Delta D1) -- supplementary delta
- `prompt/artifacts/tasks/T102/workspace/PH001/ST005/plan_T102-PH001-ST005.md` (Section IV, AC001) -- planned task descriptions as verification checklist

**Steps**:
1. Read the current `standard_T102-STD-007_issues-risks-index.md` file
2. For each of the following 5 items, verify presence and content-correctness:
   - **Delta 1 (CLAUSE-001 amendment)**: Check for explicit hosting default specification -- remove-by-default at Feature scope; mandatory at Initiative+Epic scopes; hybrid exception mechanism for complex/high-risk features
   - **Delta 2 (CLAUSE-009 extension)**: Check for Feature-to-Epic promotion rules (MUST when cross-scope impact); de-dup enforcement (highest-scope canonical); downward monitoring guidance referencing T102-STD-003
   - **Delta 3 (new CLAUSE-010)**: Check for Content Filtering Criteria clause with 6-step decision tree distinguishing Issue/Risk from ASSUM/CON/DEP/STD/ADR/IG/INT/NOTE; mandate filtering at Feature scope before approval gate; worked examples
   - **Delta 4 (new CLAUSE-011)**: Check for Staleness Detection Policy clause with 90-day threshold for OPEN/MONITORED items; review touch options; cadence alignment with initiative review cycles
   - **RES-006 Delta D1 (CLAUSE-001/009 interpretive guidance)**: Check for clarification that "must be available for each scope" means canonical tables exist in the scope's SSOT artifact; Concept aggregation is optional audit-surface enhancement
3. Record each item as `present` (content matches delta intent), `missing` (not found), or `malformed` (present but incorrect/incomplete)
4. Record any unexpected content not traceable to a planned delta

**Success Criteria**:
- [ ] All 5 amendment items have a verification result (present/missing/malformed)
- [ ] Any unexpected content is noted

---

### Task TK002: Verify STD-003 Amendments (RES-005 Deltas A1-A4)

**Task ID**: `T102-PH001-ST002-AC000-TK002`

**Purpose**: Verify that the 4 amendment items planned in ST005-AC002 are present and content-correct in the current `standard_T102-STD-003_explicit-inheritance-model.md` file.

**Deliverable**:
- Per-delta verification result recorded in TK007's calibrated scope brief

**Scope**:
- In scope: Content verification of 4 specific amendment items
- Out of scope: Structural conformance (TK005); CLAUSE remediation

**Inputs Required**:
- `prompt/artifacts/tasks/T102/standard/standard_T102-STD-003_explicit-inheritance-model.md` -- current STD file
- `prompt/artifacts/tasks/T102/workspace/PH000/analysis/analysis_T102-RES-005_cross-scope-coordination-architecture.md` v1.0.0 (Section III, Delta A) -- canonical delta definitions
- `prompt/artifacts/tasks/T102/workspace/PH001/ST005/plan_T102-PH001-ST005.md` (Section IV, AC002)

**Steps**:
1. Read the current `standard_T102-STD-003_explicit-inheritance-model.md` file
2. For each of the following 4 items, verify presence and content-correctness:
   - **Delta A1 (CLAUSE-001 schema enforcement)**: Check for mandated exact column names (`Source Artifact`, `Scope ID`, `Category`, `Inherited Rule IDs`) and exact category enum values (`Governances` not `Governance`); prohibition of ad-hoc column additions
   - **Delta A2 (CLAUSE-003 minimum viable rule)**: Check for "minimum viable embedded coordination" authoring guidance -- inherited tables at Feature scope SHOULD contain only critical upstream IDs; general-purpose "safety listing" identified as anti-pattern
   - **Delta A3 (new coordination boundary clause)**: Check for clause explicitly stating Inherited Considerations tables serve as "local emphasis layer" for scanability, NOT cross-scope coordination inventory; cross-scope belongs in Concept
   - **Delta A4 (CLAUSE-001 empty table disposition)**: Check for rule that table MAY be omitted with one-line note when no critical inherited IDs apply
3. Record each as present/missing/malformed
4. Note any unexpected content

**Success Criteria**:
- [ ] All 4 amendment items have a verification result
- [ ] Any unexpected content is noted

---

### Task TK003: Verify STD-006 Amendments (RES-005 Deltas B1-B4 + RES-006 C1)

**Task ID**: `T102-PH001-ST002-AC000-TK003`

**Purpose**: Verify that the 5 amendment items planned in ST005-AC003 are present and content-correct in the current `standard_T102-STD-006_research-artifacts-index.md` file.

**Deliverable**:
- Per-delta verification result recorded in TK007's calibrated scope brief

**Scope**:
- In scope: Content verification of 5 specific amendment items
- Out of scope: Structural conformance (TK005); CLAUSE remediation

**Inputs Required**:
- `prompt/artifacts/tasks/T102/standard/standard_T102-STD-006_research-artifacts-index.md` -- current STD file
- `prompt/artifacts/tasks/T102/workspace/PH000/analysis/analysis_T102-RES-005_cross-scope-coordination-architecture.md` v1.0.0 (Section III, Delta B) -- canonical delta definitions
- `prompt/artifacts/tasks/T102/workspace/PH000/analysis/analysis_T102-RES-006_integration-impact.md` v1.0.0 (Delta C1)
- `prompt/artifacts/tasks/T102/workspace/PH001/ST005/plan_T102-PH001-ST005.md` (Section IV, AC003)

**Steps**:
1. Read the current `standard_T102-STD-006_research-artifacts-index.md` file
2. For each of the following 5 items, verify presence and content-correctness:
   - **Delta B1 (CLAUSE-002 filename discipline)**: Check for mandate that Brief/Report links use canonical unversioned filenames; prohibition of versioned filename stems in public links
   - **Delta B2 (CLAUSE-002 source column repair)**: Check for rule that Concept master register Source column MUST reference current canonical SPS filename (not versioned)
   - **Delta B3 (CLAUSE-004 link integrity verification)**: Check for explicit link-integrity verification step in Index Maintenance Protocol
   - **Delta B4 (new Concept-as-master fallback clause)**: Check for fallback mode definition where Concept register is authoritative when dual-index drift controls cannot be enforced
   - **RES-006 Delta C1 (CLAUSE-004 drift indicators)**: Check for "Last Verified" (date) and "Link Status" (OK/BROKEN) columns in Concept master register schema
3. Record each as present/missing/malformed
4. Note any unexpected content

**Success Criteria**:
- [ ] All 5 amendment items have a verification result
- [ ] Any unexpected content is noted

---

### Task TK004: Verify STD-001 Amendments (RES-006 Deltas A1-A5, absorbs RES-005 D1-D2)

**Task ID**: `T102-PH001-ST002-AC000-TK004`

**Purpose**: Verify that the 5 amendment items planned in ST005-AC004 are present and content-correct in the current `standard_T102-STD-001_consultancy-operating-model.md` file.

**Deliverable**:
- Per-delta verification result recorded in TK007's calibrated scope brief

**Scope**:
- In scope: Content verification of 5 specific amendment items (which absorb/supersede RES-005 D1-D2)
- Out of scope: Structural conformance (TK005); CLAUSE remediation

**Inputs Required**:
- `prompt/artifacts/tasks/T102/standard/standard_T102-STD-001_consultancy-operating-model.md` -- current STD file
- `prompt/artifacts/tasks/T102/workspace/PH000/analysis/analysis_T102-RES-006_integration-impact.md` v1.0.0 (Section III, Delta A) -- canonical delta definitions
- `prompt/artifacts/tasks/T102/workspace/PH000/analysis/analysis_T102-RES-005_cross-scope-coordination-architecture.md` v1.0.0 (Section III, Delta D -- absorbed)
- `prompt/artifacts/tasks/T102/workspace/PH001/ST005/plan_T102-PH001-ST005.md` (Section IV, AC004)

**Steps**:
1. Read the current `standard_T102-STD-001_consultancy-operating-model.md` file
2. For each of the following 5 items, verify presence and content-correctness:
   - **Delta A1 (CLAUSE-003 Concept role redefinition)**: Check for comprehensive Concept role replacing "ADD/ADR compendium" with "initiative bridge / process manual + coordination audit surface + handoff authority surface"; references to T102C-STD-001 and T102-STD-006
   - **Delta A2 (CLAUSE-003 authority tiers)**: Check for three defined tiers -- (1) normative bodies, (2) authoritative snapshots, (3) audit registers (pointers-only)
   - **Delta A3 (CLAUSE-003 strict exclusions)**: Check for explicit list of what Concept MUST NOT host: full requirements bodies, full design bodies, duplicated research bodies, canonical I&R tables
   - **Delta A4 (new governance note: coordination responsibilities)**: Check for allocation -- SPS/Request = embedded minimum viable; Concept = cross-scope registers + audit + drift; INT = transient with mandatory promotion
   - **Delta A5 (new governance note: register families)**: Check for default families (STD index, Design register, Research register, Workscope/File registers, Readiness/Handoff snapshots) and conditional families (I&R aggregation, Overview assets, Expanded coordination) with threshold triggers
3. Record each as present/missing/malformed
4. Note any unexpected content

**Success Criteria**:
- [ ] All 5 amendment items have a verification result
- [ ] Any unexpected content is noted

---

### Task TK005: P-STD-001 Structural Gap Assessment (All T102-STDs)

**Task ID**: `T102-PH001-ST002-AC000-TK005`

**Purpose**: Assess every T102-STD file against P-STD-001's structural requirements to produce a per-STD structural gap inventory. This inventory becomes the primary input for AC001's structural remediation planning.

**Deliverable**:
- Per-STD structural gap inventory recorded in TK007's calibrated scope brief

**Scope**:
- In scope: Structural assessment of all 9 T102-STD files (STD-001 through STD-009) against P-STD-001 CLAUSEs
- Out of scope: Performing structural remediation (AC001 scope); content verification (TK001-TK004 scope)

**Inputs Required**:
- All 9 files under `prompt/artifacts/tasks/T102/standard/`
- `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md` -- structural authority

**Steps**:
1. Read P-STD-001 to establish the structural checklist. The minimum checklist items are:
   - **P-STD-001-CLAUSE-001 (Canonical File Structure)**: Does the file have the required sections in order? (Title, Specification, Decision Record, References, Provenance)
   - **P-STD-001-CLAUSE-031 (Standard-File YAML Frontmatter)**: Does the file have governed YAML frontmatter with required metadata fields?
   - **P-STD-001-CLAUSE-018 (CLAUSE Construction Requirements)**: Are CLAUSEs formatted per P-STD-001 requirements? (format, titles, subclauses, references)
   - **P-STD-001-CLAUSE-028 (References & Provenance)**: Do References and Provenance sections exist with required content?
   - **P-STD-001-CLAUSE-034 (Version Tracking & Amendment History)**: Is semver used and amendment history retained?
   - **P-STD-001-CLAUSE-004 (Specification Lifecycle Stages)**: Are lifecycle stages correctly applied?
2. Read each T102-STD file (STD-001 through STD-009) and assess against the checklist
3. For each STD, produce a gap summary: which P-STD-001 CLAUSEs are met, partially met, or not met
4. Flag critical gaps that would block downstream baselining work (AC001-AC004)

**Success Criteria**:
- [ ] All 9 T102-STD files assessed against P-STD-001 structural checklist
- [ ] Per-STD gap summary produced (met/partial/not-met per CLAUSE)
- [ ] Critical gaps flagged for AC001 prioritization

---

### Task TK006: T102-STD-004 Supersession Housekeeping

**Task ID**: `T102-PH001-ST002-AC000-TK006`

**Purpose**: Mark T102-STD-004 as superseded by P-STD-001 with appropriate forward reference and historical preservation. This is a bounded one-file mutation.

**Deliverable**:
- Updated `standard_T102-STD-004_specification-standard-and-guideline.md` with superseded status and forward reference

**Scope**:
- In scope: Adding supersession notice to T102-STD-004; updating ADR status if applicable
- Out of scope: SPS index updates (deferred to AC004); deleting the file (MUST NOT delete -- historical ADR rationale is preserved)

**Inputs Required**:
- `prompt/artifacts/tasks/T102/standard/standard_T102-STD-004_specification-standard-and-guideline.md` -- current file
- `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md` -- successor standard

**Steps**:
1. Read the current T102-STD-004 file
2. Add a supersession notice immediately after the title heading:
   ```
   > **SUPERSEDED**: This standard has been superseded by `P-STD-001` (Program Governance Standard), effective 2026-02-22. See `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md`. This file is preserved for historical ADR traceability only.
   ```
3. If YAML frontmatter exists, add or update `status: 'superseded'` and `superseded_by: 'prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md'`
4. If YAML frontmatter does not exist, the supersession notice in the body is sufficient
5. Do NOT modify ADR bodies, CLAUSE content, or any other section -- preserve as-is for historical reference
6. Note the SPS update requirement (T102-STD-004 row status change) as a deferred item for AC004

**Success Criteria**:
- [ ] Supersession notice is present in T102-STD-004
- [ ] File is NOT deleted
- [ ] ADR rationale chain is preserved intact
- [ ] SPS update requirement is noted as AC004 deferred item

---

### Task TK007: Produce Calibrated Scope Brief for AC001-AC004

**Task ID**: `T102-PH001-ST002-AC000-TK007`

**Purpose**: Synthesize TK001-TK006 findings into a single calibrated scope brief analysis artifact that provides per-AC focus guidance for the remaining ST002 activities.

**Deliverable**:
- `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/analysis_T102-PH001-ST002-AC000_calibrated-scope-brief.md`

**Scope**:
- In scope: Synthesis of all TK001-TK006 results; per-AC focus guidance; identification of priority gaps
- Out of scope: Authoring remediation plans (AC001 scope); drafting verification contracts (AC002)

**Inputs Required**:
- TK001-TK004 content verification results
- TK005 structural gap inventory
- TK006 supersession housekeeping status

**Steps**:
1. Create the analysis artifact following `template_workspace_analysis.md`
2. Section I: Executive Summary -- overall health of T102-STD set
3. Section II: Content Verification Results -- per-STD table (STD-001, STD-003, STD-006, STD-007) with per-delta status (present/missing/malformed)
4. Section III: P-STD-001 Structural Gap Inventory -- per-STD table (all 9 STDs) with per-CLAUSE conformance status (met/partial/not-met)
5. Section IV: T102-STD-004 Supersession Status -- confirmation of housekeeping completion + deferred SPS update
6. Section V: Calibrated Scope Guidance for AC001-AC004:
   - AC001 focus: which STDs have critical structural gaps; priority ordering for remediation
   - AC002 focus: which P-STD-001 CLAUSEs govern verification contracts
   - AC003 focus: which CLAUSEs are verifiable by checklist vs require automation
   - AC004 focus: SPS/Concept update items including T102-STD-004 supersession row update and P-STD-001 addition
7. Section VI: Open Issues -- any ambiguities or findings that require client input before AC001 proceeds

**Success Criteria**:
- [ ] Analysis artifact exists at specified path
- [ ] Content verification results cover all 19 delta items across 4 STDs
- [ ] Structural gap inventory covers all 9 T102-STDs
- [ ] Per-AC focus guidance is actionable and specific
- [ ] Open issues (if any) are explicitly flagged

---

### Task TK008: Produce GATE-001 Gate-Disposition Proposal

**Task ID**: `T102-PH001-ST002-AC000-TK008`

**Purpose**: Package the AC000 deliverables into a gate-disposition proposal for client review and approval. This is a consultation-only gate -- no DEV-REPORT or VERIFICATION tasks are required.

**Deliverable**:
- `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/proposal/proposal_T102-PH001-ST002-AC000_gate-001-disposition.md`

**Scope**:
- In scope: Gate-disposition proposal per `guideline_workspace_proposal.md` Section V.B; GDR in pending state
- Out of scope: Client decision recording (that happens at GATE-001)

**Inputs Required**:
- TK007 calibrated scope brief (primary evidence)
- `prompt/templates/consultant/workspace/guideline_workspace_proposal.md` Section VII -- GDR specification

**Steps**:
1. Author gate-disposition proposal per `guideline_workspace_proposal.md` Section V.B
2. Evidence Index: reference the calibrated scope brief as primary evidence
3. Populate GDR fields in pending state per `guideline_workspace_proposal.md` Section VII.D
4. Consultant recommendation: APPROVE (if all content verification items are accounted for and structural gap inventory is complete) or APPROVE WITH CONDITIONS (if significant gaps require AC001 scope expansion)

**Success Criteria**:
- [ ] Gate-disposition proposal exists with GDR section in pending state
- [ ] Evidence Index references the calibrated scope brief

---

### GATE-001: Client Approval of AC000 Deliverables

**Gate ID**: `T102-PH001-ST002-AC000-GATE-001`

**Entry Criteria**:
- TK001 through TK007 are completed (content verification, structural gap assessment, supersession housekeeping, calibrated scope brief)
- TK008 gate-disposition proposal exists with populated GDR in pending state
- Calibrated scope brief provides actionable per-AC guidance

**Reviewer**: Client

**Exit Criteria**:
- Client records decision in the GDR per `guideline_workspace_proposal.md` Section VII.D
- If APPROVE: AC001-AC004 may proceed using calibrated scope brief as primary input
- If APPROVE WITH CONDITIONS: conditions are recorded and addressed before AC001 begins
- If RECYCLE: remediation tasks are created per `guideline_workspace_plan.md` Section VI.K

**Gate-Disposition Proposal**: `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/proposal/proposal_T102-PH001-ST002-AC000_gate-001-disposition.md`

---

## IV. LINKS REGISTER

| Link Type | Target | Path |
|:--|:--|:--|
| Plan (this file) | AC000 Activity Plan | `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/plan_T102-PH001-ST002-AC000.md` |
| Plan | ST002 Stream Plan (parent) | `prompt/artifacts/tasks/T102/workspace/PH001/ST002/plan_T102-PH001-ST002.md` |
| Plan (source) | ST005 Stream Plan (closed) | `prompt/artifacts/tasks/T102/workspace/PH001/ST005/plan_T102-PH001-ST005.md` |
| Standard (structural authority) | P-STD-001 Program Governance Standard | `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md` |
| Analysis (input) | RES-004 integration analysis | `prompt/artifacts/tasks/T102/workspace/PH000/analysis/analysis_T102-RES-004_issues-risks-architecture.md` |
| Analysis (input) | RES-005 integration analysis | `prompt/artifacts/tasks/T102/workspace/PH000/analysis/analysis_T102-RES-005_cross-scope-coordination-architecture.md` |
| Analysis (input) | RES-006 integration analysis | `prompt/artifacts/tasks/T102/workspace/PH000/analysis/analysis_T102-RES-006_integration-impact.md` |
| Implementation | Block A task specification | `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/implementation/implementation_T102-PH001-ST002-AC000_block-a-planning-housekeeping.md` |

---

## V. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-03-27 | Initial | AC000 Activity Plan created. Task decomposition: TK001-TK004 (per-STD content verification), TK005 (P-STD-001 structural gap assessment), TK006 (T102-STD-004 supersession housekeeping), TK007 (calibrated scope brief), TK008 (gate-disposition proposal), GATE-001 (consultation-only client approval). Source: T102-PH001-ST002-AC000 consultation session (2026-03-27). |
```

---

## IV. IMPLEMENTATION SEQUENCE

The following execution order MUST be followed due to cross-file dependencies:

| Order | SPEC | Action | Rationale |
|:--|:--|:--|:--|
| 1 | SPEC-001 | Close ST005 plan | Must be closed before ST002 can reference it as completed |
| 2 | SPEC-002 | Fix ST002 frontmatter | Frontmatter changes are independent of body changes |
| 3 | SPEC-003 | Fix ST002 broken paths | Path fixes must precede content amendments to avoid compounding errors |
| 4 | SPEC-005 | Fix ST002 heading levels | Structural fix before content amendments |
| 5 | SPEC-004 | Replace T102-STD-004 references with P-STD-001 | Content amendment after structural fixes |
| 6 | SPEC-006 | Update Activity Register and AC000 contract stub | Depends on AC000 Activity Plan path (SPEC-008) -- execute after confirming path |
| 7 | SPEC-008 | Create AC000 Activity Plan | Core deliverable; file content is self-contained |
| 8 | SPEC-007 | Add ST002 changelog entry | Last -- captures all amendments in a single changelog row |

**Post-execution validation**: After all 8 SPEC items are executed, the executor SHOULD verify:
1. ST005 plan frontmatter shows `status: 'completed'`
2. ST002 plan frontmatter shows `version: '2.0.0'`, `procedural_guideline` points to `guideline_workspace_plan.md`
3. No occurrences of `consultant/standards/` remain in ST002
4. All ST002 Activity headings use `###` (h3)
5. AC000 Activity Plan exists at `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/plan_T102-PH001-ST002-AC000.md`
6. AC000 Activity Plan Task Register has 9 rows (TK001-TK008 + GATE-001)

## V. REFERENCES

| Document | Path |
|:--|:--|
| Governing Plan (ST002 Stream) | `prompt/artifacts/tasks/T102/workspace/PH001/ST002/plan_T102-PH001-ST002.md` |
| ST005 Stream Plan (closure target) | `prompt/artifacts/tasks/T102/workspace/PH001/ST005/plan_T102-PH001-ST005.md` |
| P-STD-001 (structural authority) | `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md` |
| Stream Plan Template | `prompt/templates/consultant/workspace/template_workspace_plan_stream.md` |
| Activity Plan Template | `prompt/templates/consultant/workspace/template_workspace_plan_activity.md` |
| Implementation Guideline | `prompt/templates/consultant/workspace/guideline_workspace_implementation.md` |
| Plan Guideline | `prompt/templates/consultant/workspace/guideline_workspace_plan.md` |
| Workspace Documentation Rules | `prompt/templates/consultant/workspace/workspace_documentation_rules.md` |

## VI. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-03-27 | Initial | Block A task specification created. 8 SPEC items covering ST005 closure (SPEC-001), ST002 amendments (SPEC-002 through SPEC-007), and AC000 Activity Plan creation (SPEC-008). Execution audience: consultant. Source: T102-PH001-ST002-AC000 consultation session (2026-03-27). |
