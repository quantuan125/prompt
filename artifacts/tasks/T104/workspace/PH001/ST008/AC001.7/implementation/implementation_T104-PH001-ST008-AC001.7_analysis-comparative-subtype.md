---
artifact_type: 'IMPLEMENTATION'
implementation_type: 'task_specification'
initiative_id: 'T104'
initiative_code: 'CWS'
phase: '1'
stream_id: 'T104-PH001-ST008'
activity_id: 'T104-PH001-ST008-AC001.7'
task_id: 'T104-PH001-ST008-AC001.7-TK002'
version: '1.0.0'
date: '2026-03-21'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.7/plan_T104-PH001-ST008-AC001.7.md'
purpose: 'Detailed execution specification for AC001.7: introduce comparative_analysis subtype to the ANALYSIS artifact family guideline and template, then retroactively reclassify the AC001.6 comparative assessment'
---

# IMPLEMENTATION (Task Specification): AC001.7 ANALYSIS Comparative Subtype Expansion

## I. PURPOSE & AUTHORITY

- **Purpose**: This artifact specifies the complete HOW for introducing the `comparative_analysis` subtype to the ANALYSIS artifact family. It covers guideline amendments, template conditional section additions, and retroactive reclassification of the AC001.6 interim assessment artifact.
- **Authority chain**: Activity plan `T104-PH001-ST008-AC001.7` authorizes the work → this artifact specifies HOW → dev-report records execution → GATE-001 closes the activity.
- **Audience**: LLM_Developer (primary), LLM_Reviewer (TK006)
- **This artifact does NOT hold a GDR.** Gate decisions are recorded in the GATE-001 gate-disposition proposal.
- **Trigger**: AC001.6 SES002 consultation revealed that the existing `assessment` subtype is structurally insufficient for formal comparative analysis. The client approved creating a new `comparative_analysis` subtype with its own conditional template sections, evaluation criteria structure, and weighted scoring matrix requirements.

---

## II. TASK SCOPE

- **Governing plan task**: `T104-PH001-ST008-AC001.7-TK002` (guideline + template + reclassification implementation)
- **Trigger**: Structural gap in ANALYSIS taxonomy — no subtype enforces comparative analysis methodology (criteria weighting, scoring matrix, recommendation with scoring rationale).
- **Deliverable contract**: See AC001.7 activity plan Task Register (TK001–GATE-001)
- **Depends On**: `T104-PH001-ST008-AC001.6-TK003.1` (comparative analysis authored under interim `assessment` subtype)

---

## III. CONTEXT & RATIONALE

The ANALYSIS guideline (v1.5.0) defines five subtypes: `pattern_audit`, `research_synthesis`, `compliance_audit`, `assessment`, `external_review`. The `assessment` subtype's lifecycle position ("readiness, hardening, or options tradeoffs") loosely touches comparison but provides **no structural requirements** for:

1. **Options enumeration** — explicit listing of all candidates
2. **Evaluation criteria** — named dimensions with definitions
3. **Weighting** — relative importance of each criterion
4. **Scoring matrix** — each option graded against each criterion
5. **Recommendation with rationale** — traceable to scoring

Industry practice (INCOSE Trade Study, DoD AoA, Pugh Matrix, ADR pattern) universally treats comparative analysis as a distinct artifact class. Introducing `comparative_analysis` closes this governance gap.

**Decisions already approved** (from AC001.6 SES002):

| Decision | Detail |
|:--|:--|
| New subtype | `comparative_analysis` introduced to ANALYSIS taxonomy |
| Scope placement | New AC001.7 under ST008, NOT within AC001.6 |
| Interim handling | AC001.6 comparative assessment uses `assessment` with forward-reference note |
| Retroactive reclassification | AC001.6 artifact reclassified after AC001.7 delivers the subtype |

---

## IV. SPECIFICATION ITEMS

### SPEC-001 — Amend guideline_workspace_analysis.md §III (Taxonomy)

| Field | Detail |
|:--|:--|
| Requirement Source | AC001.6 SES002 client approval (Answer 3) |
| Target | `prompt/templates/consultant/workspace/guideline_workspace_analysis.md` |
| Implementation Detail | **§III ANALYSIS TYPE TAXONOMY (DEC001)**: Add `comparative_analysis` to the allowed values list. The updated list becomes: `pattern_audit`, `research_synthesis`, `compliance_audit`, `assessment`, `external_review`, `comparative_analysis`. Add a note after the list: "The `comparative_analysis` subtype was introduced by `T104-PH001-ST008-AC001.7` to address the structural gap in formal option comparison methodology. See §IV.B for lifecycle position." |
| Acceptance Criteria | `comparative_analysis` appears in the §III allowed values list; amendment source note present |
| Status | `open` |

### SPEC-002 — Amend guideline_workspace_analysis.md §IV.B (Lifecycle Position)

| Field | Detail |
|:--|:--|
| Requirement Source | AC001.6 SES002 consultation — industry-standard lifecycle mapping |
| Target | `prompt/templates/consultant/workspace/guideline_workspace_analysis.md` |
| Implementation Detail | **§IV.B Non-research analysis types**: Add a new row to the lifecycle position table: `\| comparative_analysis \| Need to compare two or more options/approaches against weighted evaluation criteria to support an architectural or process decision \| Decision proposal (standards-input or gate-disposition); plan amendment; implementation task specification for the chosen option \|` |
| Acceptance Criteria | New row exists in the §IV.B lifecycle table with correct trigger and downstream handoff |
| Status | `open` |

### SPEC-003 — Amend guideline_workspace_analysis.md §VI.C (Frontmatter Keys)

| Field | Detail |
|:--|:--|
| Requirement Source | AC001.6 SES002 consultation — type-specific frontmatter needs |
| Target | `prompt/templates/consultant/workspace/guideline_workspace_analysis.md` |
| Implementation Detail | **§VI.C Type-specific optional keys**: Add a new entry: `- \`comparative_analysis\`: \`options_compared\` (list of option labels), \`evaluation_criteria\` (list of criterion names), \`recommended_option\` (label of the winning option)`. These are optional keys that aid discoverability and machine-readability of the comparative analysis artifact. |
| Acceptance Criteria | `comparative_analysis` entry exists in §VI.C with the three optional keys defined |
| Status | `open` |

### SPEC-004 — Amend template_workspace_analysis.md (Conditional Sections)

| Field | Detail |
|:--|:--|
| Requirement Source | AC001.6 SES002 consultation — structural requirements for comparative analysis |
| Target | `prompt/templates/consultant/workspace/template_workspace_analysis.md` |
| Implementation Detail | Add a new conditional section block after the `ASSESSMENT ONLY` block and before the `EXTERNAL_REVIEW ONLY` block. Insert the following template section with HTML comment marker `<!-- COMPARATIVE_ANALYSIS ONLY — omit for other analysis types -->`: **§V. COMPARATIVE ANALYSIS (TRADE STUDY)** with four required subsections: **A. Options Under Comparison** — Enumerated list of each option with brief description (use a table: `\| Option \| Label \| Description \|`). **B. Evaluation Criteria & Weighting** — Table: `\| Criterion \| Definition \| Weight (High/Medium/Low or numeric) \|`. Note: "At minimum, use ordinal weighting (High/Medium/Low). Numeric weighting (e.g., 1–5 or percentage) is preferred for complex decisions with >3 criteria." **C. Comparative Assessment Matrix** — Table: `\| Criterion \| Weight \| [Option A] \| [Option B] \| ... \| Notes \|`. Each cell should contain both a grade/score and a brief rationale. Note: "Grade options per criterion using a consistent scale (e.g., Strong/Adequate/Weak, or 1–5). Include a brief rationale in each cell — not just a score." **D. Recommendation** — "State the recommended option with a scoring-based rationale. Address dissenting considerations: where the non-recommended option(s) scored better and why those criteria were outweighed." |
| Acceptance Criteria | Conditional section exists with HTML comment marker; all four subsections (A–D) present; table schemas defined; weighting and grading guidance notes included |
| Status | `open` |

### SPEC-005 — Version Bump and Changelog for guideline_workspace_analysis.md

| Field | Detail |
|:--|:--|
| Requirement Source | Standard governance practice — version management |
| Target | `prompt/templates/consultant/workspace/guideline_workspace_analysis.md` |
| Implementation Detail | **Version**: Bump from v1.5.0 to v1.6.0 (minor — new subtype addition, no breaking changes). **Date**: `2026-03-21`. **Changelog entry**: `v1.6.0 \| 2026-03-21 \| Amendment \| Added \`comparative_analysis\` subtype to §III taxonomy, §IV.B lifecycle positions, and §VI.C frontmatter keys. Addresses the structural gap in formal option comparison methodology identified during AC001.6 SES002 consultation. Source: T104-PH001-ST008-AC001.7.` |
| Acceptance Criteria | Version is v1.6.0; date updated; changelog entry present with source reference |
| Status | `open` |

### SPEC-006 — Version Bump and Changelog for template_workspace_analysis.md

| Field | Detail |
|:--|:--|
| Requirement Source | Standard governance practice — version management |
| Target | `prompt/templates/consultant/workspace/template_workspace_analysis.md` |
| Implementation Detail | **Version**: Bump from v2.1.0 to v2.2.0 (minor — new conditional section, no breaking changes). **Date**: `2026-03-21`. **Changelog entry**: `v2.2.0 \| 2026-03-21 \| Amendment \| Added COMPARATIVE_ANALYSIS conditional section (§V) with Options Under Comparison, Evaluation Criteria & Weighting, Comparative Assessment Matrix, and Recommendation subsections. Source: T104-PH001-ST008-AC001.7.` |
| Acceptance Criteria | Version is v2.2.0; date updated; changelog entry present |
| Status | `open` |

### SPEC-007 — Retroactively Reclassify AC001.6 Comparative Assessment

| Field | Detail |
|:--|:--|
| Requirement Source | AC001.6 SES002 client approval (Answer 1 — interim classification with future reclassification) |
| Target | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/analysis/analysis_T104-PH001-ST008-AC001.6_implementation-vs-claude-plans-comparative-assessment.md` |
| Implementation Detail | **Frontmatter**: Change `analysis_type: 'assessment'` to `analysis_type: 'comparative_analysis'`. Add optional keys: `options_compared: ['IMPLEMENTATION task_specification', '.claude/plans workflow']`, `evaluation_criteria: ['requirements_traceability', 'acceptance_criteria', 'authority_chain', 'separation_of_concerns', 'change_control', 'discoverability', 'authoring_cost']`, `recommended_option: 'IMPLEMENTATION task_specification'`. **Body**: Remove the forward-reference note about interim classification (it is no longer interim). If the §V section was authored as "ASSESSMENT" heading, rename to "COMPARATIVE ANALYSIS (TRADE STUDY)" and verify subsections match the new template structure (Options Under Comparison, Evaluation Criteria & Weighting, Comparative Assessment Matrix, Recommendation). If structural gaps exist vs. the new template, add the missing subsections. **Version**: Bump with changelog entry noting reclassification source: AC001.7. |
| Acceptance Criteria | `analysis_type` is `comparative_analysis`; optional frontmatter keys present; forward-reference note removed; body heading updated; version bumped |
| Status | `open` |

---

## V. IMPLEMENTATION SEQUENCE

```
Phase 1 (Developer-owned — guideline + template amendments)
  SPEC-001  Amend guideline §III (taxonomy)
  SPEC-002  Amend guideline §IV.B (lifecycle position)
  SPEC-003  Amend guideline §VI.C (frontmatter keys)
  SPEC-005  Guideline version bump + changelog
  SPEC-004  Amend template (conditional sections)
  SPEC-006  Template version bump + changelog
  SPEC-007  Retroactively reclassify AC001.6 artifact
```

**Parallelism note**: SPEC-001 through SPEC-003 target the same file and MUST be applied in sequence (or as a single edit pass). SPEC-005 is applied after SPEC-001–003. SPEC-004 and SPEC-006 target the template file and are independent of the guideline edits. SPEC-007 depends on SPEC-004 completing (needs the new template structure to validate against).

**Recommended execution**: Single developer session applying all specs in one pass per target file.

---

## VI. TARGET FILES REGISTER

| # | File Path | Authority | Change Type | Confirmed? |
|:--|:--|:--|:--|:--|
| 1 | `prompt/templates/consultant/workspace/guideline_workspace_analysis.md` | T104 | Amend (§III, §IV.B, §VI.C, version) | Yes |
| 2 | `prompt/templates/consultant/workspace/template_workspace_analysis.md` | T104 | Amend (conditional section, version) | Yes |
| 3 | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/analysis/analysis_T104-PH001-ST008-AC001.6_implementation-vs-claude-plans-comparative-assessment.md` | T104 | Amend (reclassification) | Yes |

---

## VII. REFERENCES

| Document | Path |
|:--|:--|
| Governing Plan | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.7/plan_T104-PH001-ST008-AC001.7.md` |
| Analysis Guideline (current) | `prompt/templates/consultant/workspace/guideline_workspace_analysis.md` |
| Analysis Template (current) | `prompt/templates/consultant/workspace/template_workspace_analysis.md` |
| AC001.6 Comparative Assessment (reclassification target) | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/analysis/analysis_T104-PH001-ST008-AC001.6_implementation-vs-claude-plans-comparative-assessment.md` |
| AC001.6 SES002 Notes (decision source) | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/snotes/snotes_T104-PH001-ST008-AC001.6-SES002.md` |
| Implementation Guideline | `prompt/templates/consultant/workspace/guideline_workspace_implementation.md` |

---

## VIII. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-03-21 | Initial | Task specification for AC001.7: ANALYSIS `comparative_analysis` subtype expansion. Covers guideline amendments (§III taxonomy, §IV.B lifecycle, §VI.C frontmatter), template conditional section addition, and retroactive reclassification of AC001.6 comparative assessment. Source: AC001.6 SES002 consultation decisions. |
