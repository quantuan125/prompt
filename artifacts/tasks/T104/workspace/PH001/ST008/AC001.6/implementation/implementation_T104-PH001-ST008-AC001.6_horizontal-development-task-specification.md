---
artifact_type: 'IMPLEMENTATION'
implementation_type: 'task_specification'
initiative_id: 'T104'
initiative_code: 'CWS'
phase: '1'
stream_id: 'T104-PH001-ST008'
activity_id: 'T104-PH001-ST008-AC001.6'
task_id: 'T104-PH001-ST008-AC001.6-TK003.3'
version: '1.0.0'
date: '2026-03-21'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/plan_T104-PH001-ST008-AC001.6.md'
purpose: 'Detailed execution specification for Phase 2 horizontal IMPLEMENTATION family amendments: session-scope shorthand rule, hybrid SPEC structure, DEV-REPORT backlink, and execution audience parametrization'
execution_audience: 'developer'
---

# IMPLEMENTATION (Task Specification): Phase 2 Horizontal IMPLEMENTATION Family Amendments

## I. PURPOSE & AUTHORITY

- **Purpose**: Specifies the HOW for horizontal IMPLEMENTATION family amendments approved at GATE-001. Covers four cross-cutting convention requests (CONV-012 through CONV-015) across session-scope shorthand, hybrid SPEC structure, DEV-REPORT backlink, and execution audience parametrization.
- **Authority chain**: Activity plan AC001.6 authorizes the work (TK003.3) -> This artifact specifies HOW -> DEV-REPORT records execution evidence (execution_audience: developer).
- **Audience**: LLM_Developer (primary executor).
- This artifact does NOT hold a GDR. Gate decisions (if applicable) are recorded in gate_disposition proposals.
- **Trigger**: SES002-SES003 QA consultation identified four cross-cutting gaps (GAP-001 through GAP-004) in the IMPLEMENTATION family's structural conventions, reference compliance, and cross-family linkage.

---

## II. TASK SCOPE

- **Governing plan task**: `T104-PH001-ST008-AC001.6-TK003.3`
- **Trigger**: Standards-input proposal (TK003.2) packages four convention requests (CONV-012 through CONV-015); this spec translates the approved conventions into executable SPEC items.
- **Deliverable contract**: 9 SPEC items across 4 GIR categories (GIR-008 through GIR-011).
- **Depends On**: TK003.2 (completed), GATE-001 (must approve before execution).

---

## III. CONTEXT & RATIONALE

AC001.3 delivered the IMPLEMENTATION family horizontally. AC001.6 Phase 1 vertical integration audit and SES002-SES003 QA consultation identified four horizontal gaps:

| Gap | Category | Convention |
|:--|:--|:--|
| GAP-001 | Reference Compliance | CONV-012: Session-scope shorthand rule |
| GAP-002 | Artifact Structure | CONV-013: Hybrid SPEC item structure |
| GAP-003 | Cross-Family Linkage | CONV-014: DEV-REPORT implementation reference backlink |
| GAP-004 | Role Parametrization | CONV-015: Execution audience parametrization |

The standards-input proposal (TK003.2) packages these as CONV-012 through CONV-015. This spec provides the detailed implementation HOW for each.

---

## IV. SPECIFICATION ITEMS

### SPEC-001 — Implement Session-Scope Shorthand Rule in Documentation Rules

| Field | Detail |
|:--|:--|
| Requirement Source | TK003.2 DEC-001; CONV-012 |
| Target | `prompt/templates/consultant/workspace/workspace_documentation_rules.md` §7.C |
| Acceptance Criteria | New rule exists in §7.C defining session-scope shorthand boundary; rule references P-STD-005-CLAUSE-004A; version bumped with changelog |
| Status | `open` |

#### Implementation Detail

Add a new rule to §7.C (Inter-Artifact Linkage Rules) after the existing rules table. The rule should state:

**Session-Scope Shorthand Rule**: Workspace artifact references to session items (DEC, DP, ACT, OQ) within the **same activity scope** MAY use session-scoped shorthand (e.g., `SES002-DEC001`). References to session items in a **different activity scope** MUST use the fully-qualified timeline UID (e.g., `T104-PH001-ST008-AC001.3-SES004-DEC002`) per `P-STD-005-CLAUSE-004A (Reference Styles)`.

Rationale note: The artifact's frontmatter establishes `activity_id`, providing implicit scope context for shorthand references within the same activity. Cross-activity references lack this context.

Version: Minor bump. Changelog: Record session-scope shorthand rule addition with source: T104-PH001-ST008-AC001.6-GATE-001.

---

### SPEC-002 — Add Shorthand Cross-Reference Note to Implementation Guideline

| Field | Detail |
|:--|:--|
| Requirement Source | TK003.2 DEC-001; CONV-012 |
| Target | `prompt/templates/consultant/workspace/guideline_workspace_implementation.md` §IV or §V |
| Acceptance Criteria | Concise note referencing `workspace_documentation_rules.md` §7.C for Requirement Source reference format; no duplication of the full rule |
| Status | `open` |

#### Implementation Detail

Add a concise cross-reference note to §IV (Governance Rules) table or §V (Frontmatter Specification) section. The note should state:

"Requirement Source references in SPEC items follow the session-scope shorthand rule defined in `workspace_documentation_rules.md` §7.C. Within the same activity scope, session-scoped shorthand (e.g., `SES002-DEC001`) is permitted. Cross-activity references require fully-qualified timeline UIDs per `P-STD-005-CLAUSE-004A`."

This is a link-don't-duplicate reference, not a full rule restatement.

---

### SPEC-003 — Restructure task_specification Template to Hybrid Format

| Field | Detail |
|:--|:--|
| Requirement Source | TK003.2 DEC-002; CONV-013 |
| Target | `prompt/templates/consultant/workspace/template_workspace_implementation_task-specification.md` |
| Acceptance Criteria | SPEC item structure uses metadata table + separate `#### Implementation Detail` prose section; Implementation Detail is NOT inside a table cell; template is a valid instantiation pattern |
| Status | `open` |

#### Implementation Detail

Restructure the `## III. SPECIFICATION ITEMS` section of the template. Replace the current table-only SPEC item pattern:

**Current pattern** (to be replaced):
```markdown
### SPEC-001 — [Title]

| Field | Detail |
|:--|:--|
| Requirement Source | [plan task step or amendment reference] |
| Implementation Detail | [detailed HOW] |
| Expected Format | [schema, structure, output format] |
| Acceptance Criteria | [what defines completion] |
| Status | `open` / `resolved` |
```

**New hybrid pattern**:
```markdown
### SPEC-001 — [Title]

| Field | Detail |
|:--|:--|
| Requirement Source | [P-STD-005 compliant ID: plan task UID, session DEC/DP UID, or guideline section reference] |
| Template | [template path if creating a new artifact] |
| Target | [target file path if amending an existing artifact] |
| Output | [output file path for new artifacts] |
| Acceptance Criteria | [brief, testable completion criteria] |
| Status | `open` / `resolved` |

#### Implementation Detail

[Structured prose with subsections, lists, code blocks as needed. This is the specification body -- the HOW that the developer reads and executes.]
```

Notes on the new pattern:
- `Template`, `Target`, and `Output` are conditional fields -- include whichever are applicable (Template + Output for new artifacts, Target for amendments, or both if an amendment uses a template reference).
- The `Expected Format` field from the old template is absorbed into the Implementation Detail prose.
- The `Requirement Source` placeholder now includes P-STD-005 guidance.
- Add `execution_audience` to the frontmatter template placeholders (optional field, after `purpose`).

Version the template appropriately. No changelog needed (templates do not have changelogs by convention -- but check if this one does and follow the existing pattern).

---

### SPEC-004 — Restructure remediation_specification Template to Hybrid Format

| Field | Detail |
|:--|:--|
| Requirement Source | TK003.2 DEC-002; CONV-013 |
| Target | `prompt/templates/consultant/workspace/template_workspace_implementation_remediation-specification.md` |
| Acceptance Criteria | Same hybrid structure as SPEC-003; SPEC item pattern uses metadata table + prose Implementation Detail |
| Status | `open` |

#### Implementation Detail

Apply the same structural change as SPEC-003. Read the current `remediation_specification` template and restructure its SPEC item section to use the hybrid format. The remediation-specification template may have different metadata fields (e.g., `Finding Reference` instead of `Requirement Source`). Preserve the subtype-specific fields while applying the hybrid structural pattern.

Keep any remediation-specific frontmatter fields (e.g., `gate_id`, `verification_reference`, `proposal_reference`) that distinguish this template from `task_specification`.

---

### SPEC-005 — Update Implementation Guideline §III with Hybrid SPEC Item Description

| Field | Detail |
|:--|:--|
| Requirement Source | TK003.2 DEC-002; CONV-013 |
| Target | `prompt/templates/consultant/workspace/guideline_workspace_implementation.md` §III |
| Acceptance Criteria | §III describes the hybrid SPEC item structure; mentions metadata table + prose Implementation Detail as the canonical format |
| Status | `open` |

#### Implementation Detail

In §III (Subtype Taxonomy), under both §III.A (`remediation_specification`) and §III.B (`task_specification`), add or update the description of the SPEC item structure. Reference the hybrid format:

"Each SPEC item uses a two-part structure: a metadata table (Requirement Source, Template/Target, Output, Acceptance Criteria, Status) for quick-reference fields, followed by a separate `#### Implementation Detail` section containing structured prose for the specification body. Implementation Detail MUST NOT be placed inside the metadata table."

This may alternatively be placed in §IV (Governance Rules) as a new convention (e.g., the next available number in the guideline's own convention sequence). Choose the most natural placement based on the guideline's current structure.

---

### SPEC-006 — Add implementation_reference to Dev-Report Guideline

| Field | Detail |
|:--|:--|
| Requirement Source | TK003.2 DEC-003; CONV-014 |
| Target | `prompt/templates/consultant/workspace/guideline_workspace_dev-report.md` §IV |
| Acceptance Criteria | `implementation_reference` listed as a recommended (SHOULD) frontmatter field in §IV; traceability matrix SHOULD map to SPEC item IDs when applicable; version bumped with changelog |
| Status | `open` |

#### Implementation Detail

In §IV (Frontmatter Conventions), add `implementation_reference` to §IV.B (Common recommended keys) or §IV.C (Bounded optional keys). The field description:

`implementation_reference` -- Repo-relative path to the governing IMPLEMENTATION artifact, when one exists for the scope being reported. Include this field when the DEV-REPORT reports execution of work governed by an IMPLEMENTATION `task_specification` or `remediation_specification`.

Also add a note to §V.D (Traceability Matrix): "When an IMPLEMENTATION artifact governs the work, the Traceability Matrix SHOULD map each deliverable or change back to the relevant SPEC-### item ID from the governing specification."

Version: Minor bump. Changelog: Record implementation_reference addition with source: T104-PH001-ST008-AC001.6-GATE-001.

---

### SPEC-007 — Add implementation_reference to Dev-Report Template

| Field | Detail |
|:--|:--|
| Requirement Source | TK003.2 DEC-003; CONV-014 |
| Target | `prompt/templates/consultant/workspace/template_workspace_dev-report.md` |
| Acceptance Criteria | `implementation_reference` placeholder exists in template frontmatter |
| Status | `open` |

#### Implementation Detail

Add `implementation_reference: '[path to governing IMPLEMENTATION artifact, if applicable]'` to the template's frontmatter section, after `source_plan`. This is an optional field -- the placeholder should indicate conditionality.

---

### SPEC-008 — Add Implementation-to-Dev-Report Backlink Guidance

| Field | Detail |
|:--|:--|
| Requirement Source | TK003.2 DEC-003; CONV-014 |
| Target | `prompt/templates/consultant/workspace/guideline_workspace_implementation.md` §VII.C |
| Acceptance Criteria | §VII.C explicitly states that DEV-REPORT SHOULD include `implementation_reference` frontmatter when governed by an IMPLEMENTATION artifact |
| Status | `open` |

#### Implementation Detail

Update §VII.C (Dev-Report) to strengthen the prose description. Current text: "Developer execution evidence references the IMPLEMENTATION artifact as the specification input."

Replace or supplement with: "Developer execution evidence references the IMPLEMENTATION artifact as the specification input. When an IMPLEMENTATION artifact governs the work, the DEV-REPORT SHOULD include an `implementation_reference` frontmatter field per `guideline_workspace_dev-report.md` §IV, and its Traceability Matrix SHOULD map deliverables back to SPEC item IDs."

---

### SPEC-009 — Add execution_audience Field to Implementation Guideline and Template

| Field | Detail |
|:--|:--|
| Requirement Source | TK003.2 DEC-004; CONV-015 |
| Target | `prompt/templates/consultant/workspace/guideline_workspace_implementation.md` §III.B + §V; `prompt/templates/consultant/workspace/template_workspace_implementation_task-specification.md` |
| Acceptance Criteria | `execution_audience` described in guideline §III.B and listed in §V frontmatter specification; template includes `execution_audience` placeholder; authority chain guidance explains conditional evidence surface |
| Status | `open` |

#### Implementation Detail

Three changes:

**1. Guideline §III.B** (`task_specification` subsection): Add a note after the existing content:

> When `execution_audience` is `'consultant'`, the authority chain terminates at session notes as the evidence surface. No DEV-REPORT is produced (per `guideline_workspace_dev-report.md` §III.A). The specification items remain structurally identical; only the downstream evidence surface changes. When omitted, `'developer'` is the default.

**2. Guideline §V.C** (Additional Required Fields -- `task_specification`): Change "None beyond the universal set" to:

| Field | Value / Description |
|:--|:--|
| `execution_audience` | (Optional) `'developer'` (default) or `'consultant'`. Determines downstream evidence surface: developer -> DEV-REPORT; consultant -> session notes. |

**3. Template frontmatter**: Add `execution_audience: '{{EXECUTION_AUDIENCE}}'` after the `purpose` field placeholder. Add a comment: `# Optional. Values: 'developer' (default) or 'consultant'. Determines evidence surface.`

---

## V. IMPLEMENTATION SEQUENCE

```
SPEC-001  Implement session-scope shorthand rule (workspace_documentation_rules.md)
SPEC-002  Add shorthand cross-reference (guideline_workspace_implementation.md)
SPEC-003  Restructure task_specification template to hybrid format
SPEC-004  Restructure remediation_specification template to hybrid format
SPEC-005  Update implementation guideline §III with hybrid description
SPEC-006  Add implementation_reference to dev-report guideline
SPEC-007  Add implementation_reference to dev-report template
SPEC-008  Add implementation-to-dev-report backlink guidance (implementation guideline)
SPEC-009  Add execution_audience field (implementation guideline + template)
```

**Parallelism note**: SPEC-001 and SPEC-002 are independent. SPEC-003, SPEC-004, and SPEC-005 are independent of each other but all modify templates/guideline (coordinate to avoid conflicts). SPEC-006, SPEC-007, and SPEC-008 are independent. SPEC-009 is independent. All may execute in parallel within a single developer session.

**Consolidation note**: SPEC-002, SPEC-005, SPEC-008, and SPEC-009 all target `guideline_workspace_implementation.md`. These SHOULD be executed as a single coordinated pass over the file to avoid version conflicts.

---

## VI. TARGET FILES REGISTER

| # | File Path | Authority | Change Type | GIR | Confirmed? |
|:--|:--|:--|:--|:--|:--|
| 1 | `prompt/templates/consultant/workspace/workspace_documentation_rules.md` | T104 | Amend (§7.C session-scope shorthand rule) | GIR-008 | Yes |
| 2 | `prompt/templates/consultant/workspace/guideline_workspace_implementation.md` | T104 | Amend (§IV/V shorthand note + §III hybrid description + §VII.C backlink + §III.B/V execution_audience) | GIR-008, GIR-009, GIR-010, GIR-011 | Yes |
| 3 | `prompt/templates/consultant/workspace/template_workspace_implementation_task-specification.md` | T104 | Amend (hybrid SPEC structure + execution_audience placeholder) | GIR-009, GIR-011 | Yes |
| 4 | `prompt/templates/consultant/workspace/template_workspace_implementation_remediation-specification.md` | T104 | Amend (hybrid SPEC structure) | GIR-009 | Yes |
| 5 | `prompt/templates/consultant/workspace/guideline_workspace_dev-report.md` | T104 | Amend (§IV implementation_reference + §V.D SPEC traceability) | GIR-010 | Yes |
| 6 | `prompt/templates/consultant/workspace/template_workspace_dev-report.md` | T104 | Amend (implementation_reference placeholder) | GIR-010 | Yes |

---

## VII. REFERENCES

| Document | Path |
|:--|:--|
| Governing Plan | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/plan_T104-PH001-ST008-AC001.6.md` |
| Standards-Input Proposal (source) | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/proposal/proposal_T104-PH001-ST008-AC001.6_implementation-horizontal-development-amendments.md` |
| Implementation Guideline | `prompt/templates/consultant/workspace/guideline_workspace_implementation.md` |
| Dev-Report Guideline | `prompt/templates/consultant/workspace/guideline_workspace_dev-report.md` |
| Documentation Rules | `prompt/templates/consultant/workspace/workspace_documentation_rules.md` |
| SES003 Session Notes | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/snotes/snotes_T104-PH001-ST008-AC001.6-SES003.md` |

---

## VIII. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-03-21 | Initial | Task specification for Phase 2 horizontal IMPLEMENTATION family amendments (TK003.3). Covers 9 SPEC items across 4 GIR categories (GIR-008 through GIR-011). Uses hybrid SPEC item format (metadata table + prose Implementation Detail) as first exemplar. Source: TK003.2 standards-input proposal + SES002-SES003 consultation decisions. |
