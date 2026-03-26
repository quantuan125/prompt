---
artifact_type: 'IMPLEMENTATION'
implementation_type: 'task_specification'
initiative_id: 'P'
initiative_code: 'PROGRAM'
phase: '0'
stream_id: 'P-PH000-ST001'
activity_id: 'P-PH000-ST001-AC009'
task_id: 'P-PH000-ST001-AC009-TK009'
version: '2.0.0'
date: '2026-03-26'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/plan_P-PH000-ST001-AC009.md'
execution_audience: 'multi_role'
purpose: 'Single SSOT implementation contract for the remaining AC009 execution path from TK008 through TK013. Covers live Gate-001 closeout corrections, P-STD-001 evolution implementation, exact TK011 dev-report content, exact TK012 verification content, and exact TK013 gate-disposition proposal content.'
---

# IMPLEMENTATION (Unified Execution Contract): AC009 Gate-001 Closeout + P-STD-001 Evolution + GATE-002 Package Delivery

## I. PURPOSE & AUTHORITY

- Purpose: Provide one execution contract for all remaining AC009 work needed to present `GATE-002`. This artifact now governs the unimplemented `TK008` live closeout corrections, the `TK010` P-STD-001 evolution amendments, the exact `TK011` dev-report file, the exact `TK012` verification file, and the exact `TK013` gate-disposition proposal file.
- Authority chain: `GATE-001` APPROVE WITH CONDITIONS authorizes the downstream closeout path -> this artifact is the single SSOT for `TK008` through `TK013` execution detail -> `TK013` hosts the pending `GATE-002` GDR -> Client decides `GATE-002`.
- Historical split-contract note: the older `implementation_P-PH000-ST001-AC009_gate-001-compliance-remediation.md` artifact is retained only as historical/reference traceability. Execution authority has been consolidated into this file.
- Supersession rule: if any instruction in the historical remediation artifact conflicts with this file, this file controls.
- Audience: `LLM_Consultant`, `LLM_Developer`, and `LLM_Reviewer`, with role assignment to be orchestrated separately in the next session.
- This artifact does NOT hold a GDR. Gate decision authority remains exclusively in the GATE-002 gate-disposition proposal.

## II. EXECUTION BOUNDARY

- Governing plan range: `TK008` through `TK013` under `P-PH000-ST001-AC009`.
- Live authority surfaces to update during `TK008`:
  - `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/proposal/proposal_P-PH000-ST001-AC009_gate-001_metadata-hardening-disposition.md`
  - `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/plan_P-PH000-ST001-AC009.md`
  - `prompt/artifacts/tasks/P/workspace/PH000/ST001/plan_P-PH000-ST001.md`
- Exact `TK010` execution surfaces:
  - `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md`
  - `prompt/artifacts/tasks/P/standard/changelog/changelog_standard_P-STD-001.md`
  - `prompt/templates/consultant/standards/guideline_standard_specs.md`
  - `prompt/templates/consultant/standards/template_standard_specs.md`
  - `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC010/plan_P-PH000-ST001-AC010.md`
- Exact downstream package artifacts to author:
  - `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/dev-report/dev-report_P-PH000-ST001-AC009_p-std-001-evolution.md`
  - `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/verification/verification_P-PH000-ST001-AC009_gate-002.md`
  - `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/proposal/proposal_P-PH000-ST001-AC009_gate-002_p-std-001-evolution-disposition.md`
- Historical surfaces that MUST NOT be rewritten in this pass:
  - `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/snotes/snotes_P-PH000-ST001-AC009-SES003.md`
  - `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/analysis/analysis_P-PH000-ST001-AC009_external-review_gate-001-reassessment-package.md`
  - any prior verification, analysis, or dev-report artifact created for historical Gate-001 evidence
- Locked decisions:
  - Do NOT create `TK014`. All stale references MUST be normalized to `TK009` through `TK013` plus `GATE-002`.
  - Do NOT reopen the approved SES003 decisions on `CLAUSE-036G`, Amendment History externalization, or the `Decision Record` versus `Provenance` architecture.
  - Do NOT expand AC010 beyond the approved structure-only conformance retrofit.
  - Do NOT treat AC010 plan creation as authorization to start AC010 execution before AC009 `GATE-002` closes and `TK006` is later completed.
- One-shot authoring rule:
  - if a governed file already exists, replace the exact section(s) named below with the exact content provided below,
  - if a governed file does not exist, create it with the exact content provided below,
  - do not summarize,
  - do not paraphrase,
  - do not substitute "per guideline" for actual file content,
  - do not improvise missing details.

## III. EXACT `TK010` EXECUTION DETAIL

### SPEC-001 — Add CLAUSE-036G to P-STD-001 (Externalized Amendment Changelog)

| Field | Detail |
|:--|:--|
| Requirement Source | SES003 client QA (Amendment History bloat concern) + consultant recommendation |
| Output | New subclause `P-STD-001-CLAUSE-036G` under `P-STD-001-CLAUSE-036` |
| Acceptance Criteria | CLAUSE-036G defines the externalized changelog option with threshold, retention, and pointer rules; subclause follows existing CLAUSE-036 subclauses (after 036F) |
| Status | `open` |

#### Implementation Detail

**File**: `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md`

**Insert** the following subclause immediately after the `P-STD-001-CLAUSE-036F` bullet (after current line 490, before `## Decision Record`):

```markdown

   * **P-STD-001-CLAUSE-036G (Externalized amendment changelog)** — When `### Amendment History` inline entries exceed five, the full version-indexed changelog SHOULD be externalized to a dedicated file at `<SID>/standard/changelog/changelog_standard_<SID-STD>.md`. The inline `### Amendment History` subsection MUST retain the three most recent versioned entries and MUST include a blockquote pointer line in the format `> Full version history: \`<repo-relative-path-to-changelog>\`` placed immediately after the `### Amendment History` heading and before the retained inline entries. The externalized changelog file MUST use tabular format with schema `| Version | Date | Type | Summary |` and MUST contain the complete version history including pre-baseline entries.
```

**Update** the Specification Index table: No change required. Per `P-STD-001-CLAUSE-002C`, subclauses are not individually indexed. CLAUSE-036 row already covers all subclauses.

---

### SPEC-002 — Update P-STD-001 Amendment History (Externalized Changelog Pattern)

| Field | Detail |
|:--|:--|
| Requirement Source | Self-alignment: P-STD-001 must conform to its own new CLAUSE-036G |
| Output | Updated `### Amendment History` subsection in P-STD-001 with compact inline + pointer |
| Acceptance Criteria | Three most recent entries retained inline; pointer to externalized file present; all entries exist in the externalized file |
| Status | `open` |

#### Implementation Detail

**File**: `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md`

**Replace** the entire `### Amendment History` subsection (current lines 626-632) with the following exact content:

```markdown
### Amendment History

> Full version history: `prompt/artifacts/tasks/P/standard/changelog/changelog_standard_P-STD-001.md`

- v1.2.0 (2026-03-26): Added `CLAUSE-036G` (Externalized Amendment Changelog) enabling standards to externalize full version history to a dedicated changelog file while retaining compact inline summaries. Self-aligned `P-STD-001` to the new pattern.
- v1.1.0 (2026-03-20): Replaced lower-scope normative vocabulary authority with a program-scope drafting contract, refreshed `References` to a current-state authority set, and tightened the governed compact rendering for `Status` and `Lineage / Authority`.
- v1.0.0 (2026-03-16): Added metadata-governance clauses `031` through `036`, standardized frontmatter / References / Provenance governance, self-aligned `P-STD-001`, and aligned prompt-owned derivatives and `P-CON-003`.
```

---

### SPEC-003 — Update P-STD-001 Frontmatter and Input Sources

| Field | Detail |
|:--|:--|
| Requirement Source | Consequential update from SPEC-001 (normative addition = minor version bump per CLAUSE-034C) |
| Output | Updated frontmatter `version` and `date`; updated `### Input Sources` |
| Acceptance Criteria | Version is `1.2.0`; date is execution date; Input Sources includes this task specification |
| Status | `open` |

#### Implementation Detail

**File**: `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md`

**Update** frontmatter fields:
- `version: '1.2.0'`
- `date: '2026-03-26'`

**Append** the following line to the `### Input Sources` list (after line 642):

```markdown
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/implementation/implementation_P-PH000-ST001-AC009_p-std-001-evolution-task-specification.md`
```

---

### SPEC-004 — Create Externalized Changelog File for P-STD-001

| Field | Detail |
|:--|:--|
| Requirement Source | CLAUSE-036G (externalized changelog) + P-STD-001 self-alignment |
| Output | New file `prompt/artifacts/tasks/P/standard/changelog/changelog_standard_P-STD-001.md` |
| Acceptance Criteria | File contains the complete version history in tabular format; all current inline entries are represented; pre-baseline entries included |
| Status | `open` |

#### Implementation Detail

**Create** the directory `prompt/artifacts/tasks/P/standard/changelog/` if it does not exist.

**Create** the file `prompt/artifacts/tasks/P/standard/changelog/changelog_standard_P-STD-001.md` with the following exact content:

```markdown
# Changelog: P-STD-001 — Program Governance Standard

> Authoritative standard file: `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md`
>
> This changelog is governed by `P-STD-001-CLAUSE-036G`. The inline `### Amendment History` in the standard file retains the three most recent entries and points here for the complete history.

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.2.0 | 2026-03-26 | Amendment | Added `CLAUSE-036G` (Externalized Amendment Changelog) enabling standards to externalize full version history to a dedicated changelog file while retaining compact inline summaries. Self-aligned `P-STD-001` to the new pattern. Created this externalized changelog file. |
| v1.1.0 | 2026-03-20 | Amendment | Replaced lower-scope normative vocabulary authority with a program-scope drafting contract (`CLAUSE-008A`/`008B`/`008C`), refreshed `References` to a current-state authority set (`P-STD-004` and `P-STD-005` normative; `T102-CON-009` demoted to informative), and tightened the governed compact rendering for `Status` and `Lineage / Authority` (`CLAUSE-036C`). Evidence: AC009 recycle remediation pass (TK005.1-TK005.5). |
| v1.0.0 | 2026-03-16 | Amendment | Added metadata-governance clauses `CLAUSE-031` through `CLAUSE-036` (YAML frontmatter, metadata authority, derivative metadata, version tracking, references taxonomy, provenance taxonomy). Standardized frontmatter / References / Provenance governance. Self-aligned `P-STD-001` to the new metadata model. Aligned prompt-owned derivatives (`guideline_standard_specs.md`, `template_standard_specs.md`, `AGENTS.md`) and `P-CON-003`. Evidence: AC009 TK001-TK004 execution. |
| Pre-baseline | 2026-02-22 | Amendment | Amended `P-STD-001-CLAUSE-005D` to align derivative citation format with `P-STD-005-CLAUSE-004`; removed the legacy `[per <CLAUSE-ID>]` wrapper. |
| Pre-baseline | 2026-02-21 | Amendment | Amended `P-STD-001-CLAUSE-019A` to decouple display numbering from CLAUSE ID numbering for non-terminal substandard appends. |
| Pre-baseline | 2026-02-20 | Initial | Promoted `T102-STD-004` to `P-STD-001` with full in-file authority transfer. 29 CLAUSEs, 4 substandards, and 2 ADRs re-identified from T102 scope to Program scope. Evidence: `P-STD-001-ADR-003`. |
```

---

### SPEC-005 — Update Guideline §E (Provenance Taxonomy) with Externalized Changelog Guidance

| Field | Detail |
|:--|:--|
| Requirement Source | `P-STD-001-CLAUSE-005B` conformance coupling (CLAUSE-036G added) |
| Output | Updated `prompt/templates/consultant/standards/guideline_standard_specs.md` §III.E |
| Acceptance Criteria | §E includes externalized changelog option with threshold, retention, and pointer pattern; cites CLAUSE-036G |
| Status | `open` |

#### Implementation Detail

**File**: `prompt/templates/consultant/standards/guideline_standard_specs.md`

**Replace** the entire `### E. Provenance taxonomy` section (current lines 113-127) with the following exact content:

```markdown
### E. Provenance taxonomy `P-STD-001-CLAUSE-034`, `P-STD-001-CLAUSE-036`

`## Provenance` MUST contain:
- `### Status`
- `### Lineage / Authority`
- `### Amendment History`
- `### Input Sources`

Authoring boundary:
- `Status` complements, but does not override, current frontmatter state.
- `Lineage / Authority` holds promotion, supersession, and alias-window pointers.
- `Status` and `Lineage / Authority` SHOULD use compact key/value rendering when possible.
- `Amendment History` is concise and version-oriented; git remains the full diff authority.
- `Input Sources` lists only the lineage inputs materially used to author or amend the standard.

Externalized changelog option `P-STD-001-CLAUSE-036G`:
- When inline `### Amendment History` exceeds five entries, the full version-indexed changelog SHOULD be externalized to `<SID>/standard/changelog/changelog_standard_<SID-STD>.md`.
- The inline `### Amendment History` retains the three most recent versioned entries and a blockquote pointer line:
  ```
  > Full version history: `prompt/artifacts/tasks/<SID>/standard/changelog/changelog_standard_<SID-STD>.md`
  ```
- The externalized changelog file uses tabular format: `| Version | Date | Type | Summary |`
- The externalized file MUST contain the complete version history including pre-baseline entries.
```

---

### SPEC-006 — Update Guideline Frontmatter, Version, and Changelog

| Field | Detail |
|:--|:--|
| Requirement Source | Consequential update from SPEC-005 |
| Output | Updated guideline frontmatter and §VIII changelog |
| Acceptance Criteria | Version is `6.2.0`; changelog documents the CLAUSE-036G derivative update |
| Status | `open` |

#### Implementation Detail

**File**: `prompt/templates/consultant/standards/guideline_standard_specs.md`

**Update** frontmatter fields:
- `version: '6.2.0'`
- `date: '2026-03-26'`

**Prepend** to the `## VIII. CHANGELOG` table (before the v6.1.0 row):

```markdown
| v6.2.0 | 2026-03-26 | Amendment | Added externalized changelog option to §III.E (Provenance taxonomy) per new `P-STD-001-CLAUSE-036G`. Includes threshold (five inline entries), retention (three most recent inline), pointer pattern, and externalized file format. |
```

---

### SPEC-007 — Update Template Provenance Section with Externalized Changelog Comment

| Field | Detail |
|:--|:--|
| Requirement Source | `P-STD-001-CLAUSE-005B` conformance coupling |
| Output | Updated `prompt/templates/consultant/standards/template_standard_specs.md` Provenance section |
| Acceptance Criteria | Template includes informative comment about the externalized changelog option; default inline pattern unchanged |
| Status | `open` |

#### Implementation Detail

**File**: `prompt/templates/consultant/standards/template_standard_specs.md`

**Replace** the `### Amendment History` subsection within `## Provenance` (current lines 78-80) with the following exact content:

```markdown
### Amendment History

<!-- When inline entries exceed 5, externalize per CLAUSE-036G to: -->
<!-- <SID>/standard/changelog/changelog_standard_<SID-STD>.md -->
<!-- Then add pointer: > Full version history: `path/to/changelog` -->
<!-- and retain the 3 most recent versioned entries inline. -->

- v1.0.0 (YYYY-MM-DD): Initial authoring.
```

---

### SPEC-008 — Create AC010 Activity Plan

| Field | Detail |
|:--|:--|
| Requirement Source | SES003 client decision: "acceptable to start creating an AC010 dedicated activity plan based on our discussion of AC009" |
| Output | New file `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC010/plan_P-PH000-ST001-AC010.md` |
| Acceptance Criteria | Plan follows `guideline_workspace_plan.md`; scope matches stream plan contract stub; task register includes audit + retrofit + gate-readiness stack; success criteria align with stream plan |
| Status | `open` |

#### Implementation Detail

**Create** the directory `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC010/` if it does not exist.

**Create** the file `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC010/plan_P-PH000-ST001-AC010.md` with the following exact content:

```markdown
---
artifact_type: 'PLAN'
planning_level: 'ACTIVITY'
initiative_id: 'P'
initiative_code: 'PROGRAM'
phase: '0'
stream_id: 'P-PH000-ST001'
activity_id: 'P-PH000-ST001-AC010'
version: '1.0.0'
date: '2026-03-26'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
governance_rules: 'prompt/templates/consultant/workspace/workspace_documentation_rules.md'
procedural_guideline: 'prompt/templates/consultant/workspace/guideline_workspace_plan.md'
parent_plan: 'prompt/artifacts/tasks/P/workspace/PH000/ST001/plan_P-PH000-ST001.md'
---

# PLAN: P (PROGRAM) — Phase 0 / Stream ST001 / Activity AC010: Cross-Standard Conformance Pass (P-STD-001 Metadata CLAUSEs)

## I. EXECUTIVE SUMMARY

**Purpose**: Bring all existing P-STD standards (P-STD-002, P-STD-004, P-STD-005) into conformance with the P-STD-001 metadata governance CLAUSEs (CLAUSE-031 through CLAUSE-036, including CLAUSE-036G) authored and evolved in AC009. This is a structure-only retrofit — no normative CLAUSE content within the target standards is modified.

**Non-goals**:
- This activity does not modify P-STD-001 (completed and evolved in AC009).
- This activity does not modify normative CLAUSE content within P-STD-002, P-STD-004, or P-STD-005.
- This activity does not include P-STD-003 (deprecated placeholder — excluded per client direction).
- This activity does not perform repo-wide reference sweeps beyond Tier 1.

---

## II. ACTIVITY OUTLINE

**Activity ID**: `P-PH000-ST001-AC010`
**Objective**: Apply the P-STD-001 metadata governance model to all existing P-STD standards so the program-level standards suite is structurally conformant.
**Execution Mode**: `SEQUENTIAL`
**Depends On**: `P-PH000-ST001-AC009` (specifically `P-PH000-ST001-AC009-GATE-002` + `P-PH000-ST001-AC009-TK006`)

**Context**:
- `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md` (v1.2.0 — design authority)
- `prompt/artifacts/tasks/P/standard/standard_P-STD-002_program-status-standard.md` (target)
- `prompt/artifacts/tasks/P/standard/standard_P-STD-004_file-naming-and-directory-convention.md` (target)
- `prompt/artifacts/tasks/P/standard/standard_P-STD-005_universal-id-specification.md` (target)
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/analysis/analysis_P-PH000-ST001-AC009-TK006_ac010-handoff-boundary.md` (handoff boundary)
- `prompt/templates/consultant/standards/guideline_standard_specs.md` (authoring guide)
- `prompt/templates/consultant/standards/template_standard_specs.md` (structural template)

### Task Register

| Task | Task ID | Name | Status | Owner | Depends On | Target | Reference | Action |
|:--|:--|:--|:--|:--|:--|:--|:--|:--|
| TK000 | `P-PH000-ST001-AC010-TK000` | Metadata conformance audit of P-STD-002/004/005 | `planned` | LLM_Consultant | — | Gap inventory per CLAUSE-031 through CLAUSE-036 | P-STD-001 v1.2.0 + AC009 handoff | — |
| TK001 | `P-PH000-ST001-AC010-TK001` | Retrofit P-STD-002 (YAML + Provenance + References + Amendment History) | `planned` | LLM_Developer | TK000 | `standard_P-STD-002_program-status-standard.md` | TK000 audit findings | — |
| TK002 | `P-PH000-ST001-AC010-TK002` | Retrofit P-STD-004 (YAML + Provenance + References + Amendment History) | `planned` | LLM_Developer | TK000 | `standard_P-STD-004_file-naming-and-directory-convention.md` | TK000 audit findings | — |
| TK003 | `P-PH000-ST001-AC010-TK003` | Retrofit P-STD-005 (YAML + Provenance + References + Amendment History) | `planned` | LLM_Developer | TK000 | `standard_P-STD-005_universal-id-specification.md` | TK000 audit findings | — |
| TK004 | `P-PH000-ST001-AC010-TK004` | SPS row updates (version bump propagation) | `planned` | LLM_Developer | TK001, TK002, TK003 | `sps_P-PROGRAM.md` | Version changes from TK001-TK003 | — |
| TK005 | `P-PH000-ST001-AC010-TK005` | Dev-report for cross-standard retrofit | `planned` | LLM_Developer | TK004 | DEV-REPORT | `guideline_workspace_dev-report.md` | — |
| TK006 | `P-PH000-ST001-AC010-TK006` | Verification for cross-standard retrofit | `planned` | LLM_Reviewer | TK005 | VERIFICATION | `guideline_workspace_verification.md` | — |
| TK007 | `P-PH000-ST001-AC010-TK007` | Gate-001 disposition proposal | `planned` | LLM_Consultant | TK006 | PROPOSAL (gate_disposition) | `guideline_workspace_proposal.md` | — |
| GATE-001 | `P-PH000-ST001-AC010-GATE-001` | Gate: Client acceptance of cross-standard conformance retrofit | `planned` | Client | TK007 | Pass/fail | `guideline_workspace_plan.md` §VI | — |

---

## III. TASKS (DETAILED)

### Task TK000: Metadata Conformance Audit of P-STD-002/004/005

**Task ID**: `P-PH000-ST001-AC010-TK000`

**Purpose**: Audit all three target standards against the P-STD-001 metadata governance CLAUSEs to produce a precise gap inventory before retrofit execution.

**Deliverable**:
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC010/analysis/analysis_P-PH000-ST001-AC010-TK000_metadata-conformance-audit.md`

**Scope**:
- In scope:
  - Audit each target standard against CLAUSE-031 (YAML frontmatter), CLAUSE-032 (metadata authority), CLAUSE-034 (version tracking), CLAUSE-035 (references taxonomy), CLAUSE-036 (provenance taxonomy including CLAUSE-036G)
  - Identify which structural elements are present, missing, or non-conformant
  - Produce a per-standard gap table with specific remediation actions
- Out of scope:
  - Modifying P-STD-001
  - Modifying normative CLAUSE content within target standards
  - Assessing target standard normative quality

**Inputs Required**:
- `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md` (v1.2.0) — authoritative governance model
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/analysis/analysis_P-PH000-ST001-AC009-TK006_ac010-handoff-boundary.md` — handoff boundary and retrofit requirements
- Target standards (P-STD-002, P-STD-004, P-STD-005)

**Steps**:
1. Read each target standard and compare against CLAUSE-031 through CLAUSE-036 requirements.
2. For each standard, record: (a) frontmatter presence/completeness, (b) References taxonomy conformance, (c) Provenance taxonomy conformance, (d) Amendment History presence/format, (e) Input Sources presence.
3. Produce a consolidated gap table mapping each finding to the governing CLAUSE and a specific remediation action.

**Success Criteria**:
- [ ] Audit analysis exists at the canonical path
- [ ] All three target standards audited against all relevant CLAUSEs
- [ ] Gap table provides actionable remediation items per standard

---

### Task TK001: Retrofit P-STD-002

**Task ID**: `P-PH000-ST001-AC010-TK001`

**Purpose**: Apply the P-STD-001 metadata governance structure to P-STD-002 (Program Status Standard).

**Deliverable**:
- Updated `prompt/artifacts/tasks/P/standard/standard_P-STD-002_program-status-standard.md`

**Scope**:
- In scope: Add YAML frontmatter, normalize References subsections, normalize Provenance subsections, add version tracking
- Out of scope: Modifying normative CLAUSE content; adding or removing CLAUSEs

**Steps**:
1. Add governed YAML frontmatter per CLAUSE-031.
2. Normalize `## References` into `### Normative References` and `### Informative References` per CLAUSE-035.
3. Normalize `## Provenance` into `### Status`, `### Lineage / Authority`, `### Amendment History`, `### Input Sources` per CLAUSE-036.
4. Verify internal consistency after structural changes.

**Success Criteria**:
- [ ] P-STD-002 has valid YAML frontmatter per CLAUSE-031
- [ ] References section conforms to CLAUSE-035
- [ ] Provenance section conforms to CLAUSE-036
- [ ] No normative CLAUSE content modified

---

### Task TK002: Retrofit P-STD-004

**Task ID**: `P-PH000-ST001-AC010-TK002`

**Purpose**: Apply the P-STD-001 metadata governance structure to P-STD-004 (File Naming & Directory Convention).

**Deliverable**:
- Updated `prompt/artifacts/tasks/P/standard/standard_P-STD-004_file-naming-and-directory-convention.md`

**Scope**: Same as TK001, applied to P-STD-004.

**Steps**: Same as TK001, applied to P-STD-004.

**Success Criteria**: Same as TK001, applied to P-STD-004.

---

### Task TK003: Retrofit P-STD-005

**Task ID**: `P-PH000-ST001-AC010-TK003`

**Purpose**: Apply the P-STD-001 metadata governance structure to P-STD-005 (Universal ID Specification).

**Deliverable**:
- Updated `prompt/artifacts/tasks/P/standard/standard_P-STD-005_universal-id-specification.md`

**Scope**: Same as TK001, applied to P-STD-005.

**Steps**: Same as TK001, applied to P-STD-005.

**Success Criteria**: Same as TK001, applied to P-STD-005.

---

### Task TK004: SPS Row Updates

**Task ID**: `P-PH000-ST001-AC010-TK004`

**Purpose**: Update SPS entries if version changes occurred during TK001-TK003 retrofit.

**Deliverable**:
- Updated `prompt/artifacts/tasks/P/ssot/sps_P-PROGRAM.md` (if version bumps occurred)

**Steps**:
1. Check if TK001-TK003 resulted in version bumps for any target standard.
2. If yes, update the corresponding SPS STD Index rows.

**Success Criteria**:
- [ ] SPS rows reflect current versions for all retrofitted standards

---

### Task TK005: Dev-Report for Cross-Standard Retrofit

**Task ID**: `P-PH000-ST001-AC010-TK005`

**Purpose**: Produce bounded execution evidence for the retrofit pass.

**Deliverable**:
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC010/dev-report/dev-report_P-PH000-ST001-AC010_cross-standard-retrofit.md`

**Steps**:
1. Record execution evidence per `guideline_workspace_dev-report.md`.

**Success Criteria**:
- [ ] Dev-report exists with traceability to audit findings and retrofit actions

---

### Task TK006: Verification for Cross-Standard Retrofit

**Task ID**: `P-PH000-ST001-AC010-TK006`

**Purpose**: Independent verification that all target standards conform to P-STD-001 metadata governance CLAUSEs after retrofit.

**Deliverable**:
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC010/verification/verification_P-PH000-ST001-AC010_gate-001.md`

**Steps**:
1. Verify per `guideline_workspace_verification.md`.
2. Check each target standard against CLAUSE-031 through CLAUSE-036.
3. Verify no normative CLAUSE content was modified.

**Success Criteria**:
- [ ] Verification artifact exists with reviewer verdict

---

### Task TK007: Gate-001 Disposition Proposal

**Task ID**: `P-PH000-ST001-AC010-TK007`

**Purpose**: Author the gate-disposition proposal for client acceptance of the cross-standard conformance retrofit.

**Deliverable**:
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC010/proposal/proposal_P-PH000-ST001-AC010_gate-001_cross-standard-retrofit-disposition.md`

**Steps**:
1. Author per `guideline_workspace_proposal.md`.

**Success Criteria**:
- [ ] Gate-001 proposal exists with GDR section for client decision

---

### GATE-001: Client Acceptance of Cross-Standard Conformance Retrofit

**Gate ID**: `P-PH000-ST001-AC010-GATE-001`

**Entry Criteria**:
- TK001-TK003 complete (all target standards retrofitted)
- TK004 complete (SPS updated)
- TK005 complete (dev-report)
- TK006 complete (verification with reviewer verdict)
- TK007 complete (gate-disposition proposal with GDR)

**Reviewer**: Client

**Exit Criteria**:
- Client records `APPROVE` or `APPROVE WITH CONDITIONS` in the GATE-001 GDR
- All P-STD standards are structurally conformant to P-STD-001 metadata governance

**Gate-Disposition Proposal**: `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC010/proposal/proposal_P-PH000-ST001-AC010_gate-001_cross-standard-retrofit-disposition.md`

---

## IV. DEPENDENCY NOTES

- **AC009 GATE-002** must record an approving GDR before AC010 execution begins.
- **AC009 TK006** (handoff boundary document) provides the explicit design-authority freeze for AC010. The handoff surface defines exactly which CLAUSE requirements AC010 must retrofit and what AC010 must not reopen.
- This activity does not modify any T102 or T104 artifacts.

---

## V. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-03-26 | Initial | Created AC010 activity plan for cross-standard conformance pass. Defines audit, per-standard retrofit, SPS update, and gate-readiness stack. Scope: structure-only conformance of P-STD-002, P-STD-004, P-STD-005 to P-STD-001 metadata governance CLAUSEs (CLAUSE-031 through CLAUSE-036G). Evidence: SES003 consultation + AC009 stream plan contract stub. |
```

## IV. UNIFIED IMPLEMENTATION SEQUENCE

1. Execute the `TK008` live closeout corrections in Section V so the live Gate-001 proposal, AC009 plan, and ST001 stream plan stop pointing to a split-contract or stale `TK014` path.
2. Execute the `TK010` implementation items in Section III exactly as written.
3. Author the `TK011` dev-report from Section VI.
4. Author the `TK012` verification artifact from Section VII.
5. Author the `TK013` gate-disposition proposal from Section VIII.
6. Confirm every checklist item in Section IX before presenting `GATE-002`.

## V. EXACT `TK008` LIVE GATE-001 CLOSEOUT CORRECTIONS

### REM-001 - Update the Gate-001 Proposal to Remove the Stale `TK014` Reference

| Field | Detail |
|:--|:--|
| Revision Deliverable | Corrected Gate-001 proposal live GDR wording |
| Acceptance Criteria | Proposal no longer references `TK014`; live GDR condition chain reads `TK009-TK013 + GATE-002` |
| Resolution Status | `open` |

#### Implementation Detail

**File**: `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/proposal/proposal_P-PH000-ST001-AC009_gate-001_metadata-hardening-disposition.md`

**Update** frontmatter fields to:

```markdown
version: '1.4.0'
date: '2026-03-26'
```

**Replace** the entire `## VI. Gate Decision Record (GDR)` section with the following exact content:

```markdown
## VI. Gate Decision Record (GDR)

| Field | Value |
|:--|:--|
| Gate ID | `P-PH000-ST001-AC009-GATE-001` |
| Consultant Recommendation | `APPROVE` |
| Client Decision | `APPROVE WITH CONDITIONS` |
| Gate Status After Decision | `completed` |
| Conditions (if any) | (1) Complete TK008: correct five administrative compliance GAPs (GDR field naming, plan register status, gate construct field, section title, stream plan status). (2) Complete P-STD-001 evolution cycle (`TK009` through `TK013` + `GATE-002`) before AC010 handoff. |
| Decided By | Client |
| Decision Date | 2026-03-26 |
| Decision Reference | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/analysis/analysis_P-PH000-ST001-AC009_external-review_gate-001-reassessment-package.md` v1.0.0 + SES003 independent consultant assessment |
```

**Replace** the entire `## VIII. Changelog` section with the following exact content:

```markdown
## VIII. Changelog

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.4.0 | 2026-03-26 | Correction | Corrected the live Gate-001 GDR condition chain to remove the stale `TK014` reference and align the approved downstream path to `TK009` through `TK013` plus `GATE-002`. No change to the approved Gate-001 decision itself. |
| v1.3.0 | 2026-03-26 | Gate decision | Recorded client APPROVE WITH CONDITIONS decision. Renamed §V to `Consultant Gate Recommendation` with explicit alignment statement per guideline v1.8.0 §V.B/§VII.B. Updated GDR: `Reviewer Verdict` field renamed to `Consultant Recommendation: APPROVE` per §VII.C three-signal model. Recorded conditions, decision date, and decision reference. Updated downstream enforcement to reference GATE-002. |
| v1.2.0 | 2026-03-20 | Reassessment | Refreshed the Gate-001 package after the recycle remediation pass. Replaced the temporary revision-checklist with the governed remediation-specification IMPLEMENTATION artifact, added recycle dev-report evidence, removed the obsolete temporary-handling GIR, and updated the recommendation to `APPROVE` based on the remediated package and refreshed reviewer PASS verdict. |
| v1.1.0 | 2026-03-17 | Amendment | Added consultant external review and temporary revision-checklist to the Gate-001 package. |
| v1.0.0 | 2026-03-17 | Initial | Authored Gate-001 disposition package for the original metadata-hardening acceptance gate. |
```

### REM-002 - Update the AC009 Plan to Reflect the Post-TK008 Live State

| Field | Detail |
|:--|:--|
| Revision Deliverable | Corrected AC009 plan register, gate wording, and downstream success criteria |
| Acceptance Criteria | `TK007`, `TK008`, and `TK009` show completed state; no live AC009 plan surface references `TK014`; `TK006` remains blocked on `GATE-002` |
| Resolution Status | `open` |

#### Implementation Detail

**File**: `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/plan_P-PH000-ST001-AC009.md`

**Update** frontmatter fields to:

```markdown
version: '2.1.0'
date: '2026-03-26'
```

**Replace** the entire `### Task Register` block with the following exact content:

```markdown
### Task Register

| Task | Task ID | Name | Status | Owner | Depends On | Target | Reference | Action |
|:--|:--|:--|:--|:--|:--|:--|:--|:--|
| TK000 | `P-PH000-ST001-AC009-TK000` | Produce AC009 implementation-readiness package (assessment + gate-disposition proposal) | `completed` | LLM_Consultant | `P-PH000-ST004-AC003-GATE-002` | AC009 analysis + proposal package | Approved ST004 AC003 Gate-002 package | — |
| GATE-000 | `P-PH000-ST001-AC009-GATE-000` | Gate: Client accepts AC009 readiness package and unblocks drafting execution | `completed` | Client | TK000 | Pass/fail | `guideline_workspace_plan.md`, `guideline_workspace_proposal.md` | Client APPROVE (2026-03-15). GDR: `proposal_P-PH000-ST001-AC009-TK000_gate-000-readiness-disposition-package.md` v1.1.0. |
| TK001 | `P-PH000-ST001-AC009-TK001` | Ingest Gate-002 package and produce P-STD-001 amendment map | `completed` | LLM_Consultant | GATE-000 | Analysis artifact + drafting matrix | `P-RES-003` Gate-002 package | Amendment map authored at `analysis_P-PH000-ST001-AC009-TK001_p-std-001-amendment-map.md`. |
| TK002 | `P-PH000-ST001-AC009-TK002` | Draft metadata-governance amendments in `P-STD-001` | `completed` | LLM_Consultant | TK001 | `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md` | TK001 amendment map | Added metadata-governance clauses `031` through `036` and standardized the governing schema. |
| TK003 | `P-PH000-ST001-AC009-TK003` | Self-align `P-STD-001` to its new governance model | `completed` | LLM_Consultant | TK002 | `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md` | TK002 drafted CLAUSEs | Added frontmatter and normalized `References` / `Provenance` to the new model. |
| TK004 | `P-PH000-ST001-AC009-TK004` | Cascade derivative updates required by conformance coupling | `completed` | LLM_Consultant | TK003 | Guideline + template + AGENTS + SPS touchpoints | `P-STD-001-CLAUSE-005B` | Prompt-owned derivatives and `P-CON-003` aligned in the same changeset; see grouped dev-report. |
| TK005 | `P-PH000-ST001-AC009-TK005` | Produce verification and gate-readiness package | `completed` | LLM_Reviewer | TK004 | AC009 recycle / reassessment package | `guideline_workspace_verification.md` | Recycle loop completed; reassessment verification PASS (v1.1.0). |
| GATE-001 | `P-PH000-ST001-AC009-GATE-001` | Gate: Client acceptance of P-STD-001 metadata hardening package | `completed` | Client | TK005 | Pass/fail | `guideline_workspace_plan.md` §VI, `guideline_workspace_proposal.md` | Client APPROVE WITH CONDITIONS (2026-03-26). GDR: proposal v1.4.0. Conditions: (1) TK008 compliance remediation, (2) `TK009` through `TK013` plus `GATE-002` before AC010 handoff. |
| TK005.1 | `P-PH000-ST001-AC009-TK005.1` | Author Gate-001 remediation specification | `completed` | LLM_Consultant | GATE-001 | IMPLEMENTATION remediation spec | `guideline_workspace_implementation.md` | Created `implementation_P-PH000-ST001-AC009_gate-001-remediation-specification.md` v1.0.0. |
| TK005.2 | `P-PH000-ST001-AC009-TK005.2` | Execute AC009 Gate-001 remediation changes | `completed` | LLM_Developer | TK005.1 | Remediated `P-STD-001` + derivative + package surfaces | TK005.1 remediation specification | Fixed authority/reference/provenance/package gaps per REM-001 through REM-005. |
| TK005.3 | `P-PH000-ST001-AC009-TK005.3` | Produce recycle dev-report for the remediation pass | `completed` | LLM_Developer | TK005.2 | Recycle-pass dev-report | `guideline_workspace_dev-report.md` | Recorded remediation execution evidence at `dev-report_P-PH000-ST001-AC009_gate-001-recycle-remediation.md`. |
| TK005.4 | `P-PH000-ST001-AC009-TK005.4` | Re-run Gate-001 verification after remediation | `completed` | LLM_Reviewer | TK005.3 | Refreshed Gate-001 verification artifact | `guideline_workspace_verification.md` | Reassessed same gate ID; verdict PASS. Updated `verification_P-PH000-ST001-AC009_gate-001.md` to v1.1.0. |
| TK005.5 | `P-PH000-ST001-AC009-TK005.5` | Refresh Gate-001 disposition proposal for re-presentation | `completed` | LLM_Consultant | TK005.4 | Updated Gate-001 proposal package | `guideline_workspace_proposal.md` | Refreshed proposal to v1.2.0 with APPROVE recommendation based on remediated package and PASS verdict. |
| TK007 | `P-PH000-ST001-AC009-TK007` | Author Gate-001 compliance remediation spec + session notes (SES003) | `completed` | LLM_Consultant | GATE-001 | IMPLEMENTATION remediation spec + session notes | External review GAP-001 through GAP-005 | Authored SES003 session notes and the split-spec inputs later consolidated into the unified AC009 execution contract. |
| TK008 | `P-PH000-ST001-AC009-TK008` | Execute Gate-001 compliance remediation | `completed` | LLM_Consultant | TK007 | Updated proposal, AC009 plan, stream plan | `implementation_P-PH000-ST001-AC009_p-std-001-evolution-task-specification.md` | Normalized the live Gate-001 closeout package, removed stale `TK014` references from live authority surfaces, and locked the one-shot downstream package contract through `GATE-002`. |
| TK009 | `P-PH000-ST001-AC009-TK009` | Author P-STD-001 evolution task specification | `completed` | LLM_Consultant | GATE-001 | IMPLEMENTATION task spec | SES003 analysis findings | Authored `implementation_P-PH000-ST001-AC009_p-std-001-evolution-task-specification.md` as the unified execution contract for the remaining AC009 path. |
| TK010 | `P-PH000-ST001-AC009-TK010` | Execute P-STD-001 evolution amendments | `planned` | LLM_Developer | TK009 | Updated P-STD-001 + externalized changelog + updated guideline + template + AC010 plan | `implementation_P-PH000-ST001-AC009_p-std-001-evolution-task-specification.md` | — |
| TK011 | `P-PH000-ST001-AC009-TK011` | Dev-report for P-STD-001 evolution pass | `planned` | LLM_Developer | TK010 | DEV-REPORT | `guideline_workspace_dev-report.md` | — |
| TK012 | `P-PH000-ST001-AC009-TK012` | Verification for P-STD-001 evolution | `planned` | LLM_Reviewer | TK011 | VERIFICATION | `guideline_workspace_verification.md` | — |
| TK013 | `P-PH000-ST001-AC009-TK013` | Gate-002 disposition proposal | `planned` | LLM_Consultant | TK012 | PROPOSAL (gate_disposition) | `guideline_workspace_proposal.md` | — |
| GATE-002 | `P-PH000-ST001-AC009-GATE-002` | Gate: Client acceptance of P-STD-001 evolution amendments | `planned` | Client | TK013 | Pass/fail | `guideline_workspace_plan.md` §VI, `guideline_workspace_proposal.md` | — |
| TK006 | `P-PH000-ST001-AC009-TK006` | Prepare AC010 handoff and conformance boundary package | `planned` | LLM_Consultant | GATE-002 | AC010 handoff note / plan amendment inputs | Approved AC009 package | — |
```

**Replace** the entire `### GATE-001: Client Acceptance of the \`P-STD-001\` Metadata Hardening Package` section with the following exact content:

```markdown
### GATE-001: Client Acceptance of the `P-STD-001` Metadata Hardening Package

**Gate ID**: `P-PH000-ST001-AC009-GATE-001`

**Entry Criteria**:
- Initial review complete and recycle loop formally opened
- `TK005.1` through `TK005.5` complete for the active reassessment cycle
- Refreshed verification artifact exists and records the current reviewer verdict
- Current proposal package exists and hosts the authoritative GDR for the same gate ID

**Reviewer**: Client

**Exit Criteria**:
- Client approves or approves with conditions the completed metadata-governance hardening package
- Approved package becomes the authority surface for `AC010`

**Gate-Disposition Proposal**: `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/proposal/proposal_P-PH000-ST001-AC009_gate-001_metadata-hardening-disposition.md`

**Gate Resolution Block**:
- **Gate Status**: `completed`
- **Decision**: Client APPROVE WITH CONDITIONS (2026-03-26)
- **GDR Reference**: `proposal_P-PH000-ST001-AC009_gate-001_metadata-hardening-disposition.md` v1.4.0
- **Conditions**: (1) Complete TK008 compliance remediation (five administrative GAPs). (2) Complete the P-STD-001 evolution cycle (`TK009` through `TK013` + `GATE-002`) before AC010 handoff.
- **Prior Recycle History**: Gate-001 was recycled for authority/reference/provenance defects. Remediation tasks `TK005.1` through `TK005.5` completed the remediation pass. Reassessment verification returned PASS (v1.1.0). The reassessment external review (v1.0.0, 2026-03-25) confirmed all five original GAPs substantively closed and recommended APPROVE WITH CONDITIONS for five new administrative compliance items.
- **Downstream**: `TK006` (AC010 handoff) remains blocked until `GATE-002` records an approving GDR.
```

**Replace** the entire `### Task TK008: Execute Gate-001 Compliance Remediation` section with the following exact content:

```markdown
### Task TK008: Execute Gate-001 Compliance Remediation

**Task ID**: `P-PH000-ST001-AC009-TK008`

**Purpose**: Execute the live Gate-001 closeout corrections defined in the unified implementation contract, normalize the downstream task/gate contract, and prepare a coherent package path through `TK010` to `TK013` and `GATE-002`.

**Deliverables**:
- Updated `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/proposal/proposal_P-PH000-ST001-AC009_gate-001_metadata-hardening-disposition.md` (v1.4.0)
- Updated `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/plan_P-PH000-ST001-AC009.md` (v2.1.0)
- Updated `prompt/artifacts/tasks/P/workspace/PH000/ST001/plan_P-PH000-ST001.md` (v0.1.22)

**Steps**:
Execute per the implementation specification at `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/implementation/implementation_P-PH000-ST001-AC009_p-std-001-evolution-task-specification.md`.

**Success Criteria**:
- [ ] Proposal `GDR` uses the corrected downstream condition chain (`TK009` through `TK013` + `GATE-002`)
- [ ] Plan task register reflects the live post-closeout state for `TK007`, `TK008`, and `TK009`
- [ ] Plan `GATE-001` section no longer references `TK014`
- [ ] Plan `TK008` success criteria no longer reference `TK014`
- [ ] Stream plan live changelog wording no longer references `TK014`
- [ ] No live AC009/ST001 closeout surface in this chain requires the implementer to infer a missing task ID
```

**Replace** the entire `## V. CHANGELOG` section with the following exact content:

```markdown
## V. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v2.1.0 | 2026-03-26 | Correction | Closed the live Gate-001 closeout drift after the v2.0.0 structural amendment. Marked `TK007`, `TK008`, and `TK009` as completed to match the artifacts already authored, corrected stale `TK014` references in the live Gate-001 closeout path, and preserved `TK010` through `TK013` plus `GATE-002` as the remaining downstream stack before `TK006`. |
| v2.0.0 | 2026-03-26 | Gate decision + plan amendment | Recorded client APPROVE WITH CONDITIONS for `GATE-001` (2026-03-26). Updated `TK005` and `TK005.1` through `TK005.5` to `completed`. Registered `TK007` through `TK013` plus `GATE-002` for the P-STD-001 evolution cycle. Added `GATE-002` section (P-STD-001 evolution acceptance). Updated `TK006` dependency from `GATE-001` to `GATE-002`. Added `Gate-Disposition Proposal` field to the `GATE-001` construct (GAP-003). Updated Links Register with new artifact entries. Major version bump for structural task/gate additions. Evidence: SES003 consultation + reassessment external review v1.0.0. |
| v1.5.0 | 2026-03-20 | Recycle amendment | Converted `GATE-001` into an active recycle/reassessment loop. Marked `TK005` and `GATE-001` as `in_progress`, added `TK005.1` through `TK005.5` as formal remediation/reassessment subtasks, added the required Recycle Re-entry Block, and registered the new Gate-001 remediation specification artifact. |
| v1.4.0 | 2026-03-16 | Implementation | Marked `TK001` through `TK004` completed after AC009 metadata-governance execution. Added the `TK001` amendment map and grouped `TK001` through `TK004` dev-report to the Links Register. |
| v1.3.0 | 2026-03-15 | Gate closure | Updated task register: `TK000` -> `completed`, `GATE-000` -> `completed` with GDR reference. Added external review analysis to Context and Links Register. Evidence: `GATE-000` GDR (proposal v1.1.0), external review v1.0.0. |
| v1.2.0 | 2026-03-15 | Readiness packaging | Added `TK000` + `GATE-000` for AC009 implementation readiness. Locked AC009 to consume `P-PH000-ST004-AC003-GATE-002` without mutating upstream research artifacts, narrowed derivative instruction-surface scope to prompt-owned surfaces, made `P-CON-003` clarification explicit in `TK004`, and added AC009-local readiness analysis/proposal/session-note artifacts. |
| v1.1.0 | 2026-03-13 | Amendment | Added external review analysis as formal `TK001` input. Enhanced `TK001` scope with explicit verification carry-forward items (`FINDING-001` / `002` / `003`) and analysis GAPs. Added carry-forward resolution step and success criterion. Evidence: Gate-002 external review (2026-03-13). |
| v1.0.0 | 2026-03-13 | Initial | Created the standalone AC009 activity plan to convert the approved `P-RES-003` package into `P-STD-001` metadata-governance hardening, derivative conformance updates, verification packaging, and AC010 handoff. |
```

### REM-003 - Update the ST001 Stream Plan to Remove the Stale `TK014` Reference

| Field | Detail |
|:--|:--|
| Revision Deliverable | Corrected live ST001 stream-plan changelog wording |
| Acceptance Criteria | Stream plan no longer references `TK014` in its live AC009 closeout history |
| Resolution Status | `open` |

#### Implementation Detail

**File**: `prompt/artifacts/tasks/P/workspace/PH000/ST001/plan_P-PH000-ST001.md`

**Update** frontmatter fields to:

```markdown
version: '0.1.22'
date: '2026-03-26'
```

**Prepend** the following exact row to the `## V. CHANGELOG` table above the existing `v0.1.21` row:

```markdown
| v0.1.22 | 2026-03-26 | Correction | Normalized the live AC009 closeout wording in the stream-plan history to remove the stale `TK014` reference and align the stream record with AC009 plan v2.1.0 while keeping AC009 at `in_progress` pending `GATE-002`. Evidence: AC009 plan v2.1.0 + Gate-001 proposal v1.4.0. |
```

**Replace** the existing `v0.1.21` row with the following exact row:

```markdown
| v0.1.21 | 2026-03-26 | Housekeeping | AC009 status `planned` -> `in_progress` to reflect current execution state (`GATE-001` APPROVE WITH CONDITIONS, `TK007` through `TK013` plus `GATE-002` registered in AC009 plan v2.1.0). Evidence: AC009 plan v2.1.0 + reassessment external review v1.0.0. |
```

## IX. PRE-PRESENTATION CHECKLIST FOR `GATE-002`

The following conditions MUST be true before presenting `GATE-002` in the next session:

- [ ] The live Gate-001 proposal GDR uses the corrected downstream condition chain (`TK009` through `TK013` + `GATE-002`)
- [ ] The AC009 plan task register shows `TK007`, `TK008`, and `TK009` as completed
- [ ] The AC009 plan no longer contains any live `TK014` reference in its gate or downstream success criteria
- [ ] The ST001 stream plan no longer contains a live `TK014` reference in its AC009 closeout history
- [ ] `TK010` outputs exist exactly as specified in Section III
- [ ] `TK011` dev-report exists exactly as specified in Section VI
- [ ] `TK012` verification exists exactly as specified in Section VII
- [ ] `TK013` proposal exists exactly as specified in Section VIII
- [ ] `TK006` remains explicitly blocked pending an approving `GATE-002` GDR

## X. REFERENCES

| Document | Path |
|:--|:--|
| AC009 Activity Plan | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/plan_P-PH000-ST001-AC009.md` |
| ST001 Stream Plan | `prompt/artifacts/tasks/P/workspace/PH000/ST001/plan_P-PH000-ST001.md` |
| Gate-001 Reassessment External Review | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/analysis/analysis_P-PH000-ST001-AC009_external-review_gate-001-reassessment-package.md` |
| Gate-001 Proposal | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/proposal/proposal_P-PH000-ST001-AC009_gate-001_metadata-hardening-disposition.md` |
| Unified AC009 Execution Contract | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/implementation/implementation_P-PH000-ST001-AC009_p-std-001-evolution-task-specification.md` |
| Dev-Report Guideline | `prompt/templates/consultant/workspace/guideline_workspace_dev-report.md` |
| Verification Guideline | `prompt/templates/consultant/workspace/guideline_workspace_verification.md` |
| Proposal Guideline | `prompt/templates/consultant/workspace/guideline_workspace_proposal.md` |

## XI. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v2.0.0 | 2026-03-26 | Consolidation | Converted this artifact from a `TK009`-only task specification into the single AC009 execution SSOT for `TK008` through `TK013`. Imported the unimplemented live Gate-001 closeout corrections and exact downstream `TK011`/`TK012`/`TK013` file content from the historical remediation artifact, and rewired downstream references so future execution follows this file only. |
| v1.0.0 | 2026-03-26 | Initial | Authored P-STD-001 evolution task specification. Covers CLAUSE-036G (externalized amendment changelog), P-STD-001 self-alignment, externalized changelog file creation, guideline/template derivative updates, and AC010 activity plan creation. |
