---
artifact_type: 'PROPOSAL'
proposal_type: 'STANDARDS_INPUT'
initiative_id: 'T104'
initiative_code: 'CWS'
phase_id: 'PH001'
stream_id: 'ST008'
activity_id: 'T104-PH001-ST008-AC001.6'
task_id: 'T104-PH001-ST008-AC001.6-TK003.2'
date: '2026-03-21'
version: '1.0.0'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
analysis_reference: '---'
external_review_reference: '---'
target_standards:
  - 'T104 workspace governance suite'
  - 'guideline_workspace_implementation.md'
  - 'workspace_documentation_rules.md'
  - 'guideline_workspace_dev-report.md'
purpose: 'Standards-input proposal packaging horizontal IMPLEMENTATION family amendments identified during AC001.6 SES002-SES003 QA consultation for GATE-001 disposition'
---

# Standards-Input Proposal: AC001.6 Horizontal IMPLEMENTATION Development Amendments

## I. PURPOSE

- **Proposal objective**: Package the horizontal development amendments identified during AC001.6 SES002--SES003 QA into explicit standards-input requests for GATE-001 disposition.
- **Input scope**: IMPLEMENTATION family guideline, templates, and cross-family linkage (dev-report, documentation rules). Excludes vertical integration gaps (covered by the companion proposal `proposal_T104-PH001-ST008-AC001.6_implementation-vertical-integration-architecture.md`).
- **Target standards**: T104 workspace governance suite -- specifically `guideline_workspace_implementation.md`, `workspace_documentation_rules.md`, and `guideline_workspace_dev-report.md`.

---

## II. CURRENT STATE SUMMARY

### A. Baseline

The IMPLEMENTATION family was delivered horizontally in AC001.3 and vertically integrated during AC001.6 Phase 1 (TK001--TK003). During the SES002--SES003 QA consultation cycle, four cross-cutting gaps were identified that affect the IMPLEMENTATION family's usability, traceability, and cross-family linkage. These are horizontal amendments -- they affect the family's structural conventions rather than its vertical placement across guideline surfaces.

### B. Problems / Gaps

| Gap ID | Category | Description | Impact |
|:--|:--|:--|:--|
| GAP-001 | Reference Compliance | `Requirement Source` field in IMPLEMENTATION SPEC items uses informal session references (e.g., "SES002 client approval (Answer 1)") instead of P-STD-005 compliant IDs (e.g., `SES002-DEC001`). No governance rule defines the shorthand boundary. | Non-traceable requirement sources; inconsistent reference format across artifacts; external reviewers cannot navigate to source decisions. |
| GAP-002 | Artifact Structure | `Implementation Detail` content is constrained inside a markdown table cell. Dense specification text (~1000+ chars) loses formatting, line breaks, and nested structures. Industry practice (IEEE 830, BDD, INCOSE) separates metadata from specification body. | Developer/agent executing "EXACTLY as outlined" must parse a wall of text in a constrained visual format. Reduces execution precision -- the stated goal of the IMPLEMENTATION family. |
| GAP-003 | Cross-Family Linkage | No structural backlink exists from DEV-REPORT to IMPLEMENTATION. The implementation guideline §VII.C mentions the relationship in prose, but dev-report guideline has no `implementation_reference` frontmatter field. The linkage is asymmetric and unenforceable. | The authority chain (Plan --> Implementation --> Dev-Report) breaks at the Implementation --> Dev-Report link. Traceability gap for gate reviewers. |
| GAP-004 | Role Parametrization | `task_specification` subtype serves both developer-executed and consultant-executed work, but the template and guideline do not distinguish the execution audience. The authority chain statement (dev-report vs. session notes as evidence surface) must be manually adjusted per artifact. | Incorrect downstream linkage (e.g., consultant-executed spec referencing DEV-REPORT that will never be produced). Confusion for executing agents about evidence surface expectations. |

---

## III. PROPOSED CONVENTIONS

### CONV-012: Session-Scope Shorthand Rule

- **Rule**: Workspace artifact references to session items (DEC, DP, ACT, OQ) within the SAME activity scope MAY use session-scoped shorthand (e.g., `SES002-DEC001`). References to session items in a DIFFERENT activity scope MUST use the fully-qualified timeline UID (e.g., `T104-PH001-ST008-AC001.3-SES004-DEC002`) per `P-STD-005-CLAUSE-004A`.
- **Rationale**: The artifact's frontmatter already establishes `activity_id`, making the full prefix redundant within the artifact body. Cross-activity references lack this implicit scope context.
- **Authority Link**: `P-STD-005-CLAUSE-004A (Reference Styles)`, `workspace_documentation_rules.md` §7.C

### CONV-013: Hybrid SPEC Item Structure

- **Rule**: IMPLEMENTATION SPEC items SHALL use a two-part structure: (1) metadata table containing Requirement Source, Template/Target, Output, Acceptance Criteria, and Status; (2) a separate `#### Implementation Detail` section below the table containing structured prose with headings, lists, and code blocks as needed.
- **Rationale**: Industry practice (IEEE 830, BDD, INCOSE) separates metadata from specification body. Dense specification text loses formatting fidelity inside markdown table cells, reducing execution precision.
- **Authority Link**: `guideline_workspace_implementation.md` §III

### CONV-014: DEV-REPORT Implementation Reference Backlink

- **Rule**: When implementation work is governed by an IMPLEMENTATION artifact, the DEV-REPORT SHOULD include an `implementation_reference` frontmatter field containing the repo-relative path to the governing IMPLEMENTATION artifact. The DEV-REPORT Traceability Matrix SHOULD map deliverables back to SPEC item IDs when applicable.
- **Rationale**: Completes the Plan --> Implementation --> Dev-Report authority chain with structural enforcement rather than prose-only description.
- **Authority Link**: `guideline_workspace_dev-report.md` §IV, `guideline_workspace_implementation.md` §VII.C

### CONV-015: Execution Audience Parametrization

- **Rule**: `task_specification` artifacts MAY include an optional `execution_audience` frontmatter field with values `'developer'` or `'consultant'`. When `execution_audience` is `'developer'`, the downstream evidence surface is DEV-REPORT. When `execution_audience` is `'consultant'`, the downstream evidence surface is session notes (no DEV-REPORT is produced per `guideline_workspace_dev-report.md` §III.A). When omitted, `'developer'` is the default.
- **Rationale**: The IMPLEMENTATION artifact's structural shape (SPEC items, acceptance criteria, implementation sequence) is identical regardless of executing role. Only the downstream evidence surface changes. A frontmatter field resolves this without taxonomy expansion.
- **Authority Link**: `guideline_workspace_implementation.md` §III.B, §V

### B. Compatibility Notes

- Existing IMPLEMENTATION artifacts authored before these conventions are grandfathered. They do not require retroactive amendment.
- CONV-012 applies retroactively only to artifacts remediated as part of the current AC001.6 cycle (e.g., the supplementary spec TK003.1r).
- CONV-013 is a forward-looking template change; existing table-only SPEC items remain valid.

---

## IV. DECISION REQUESTS

### DEC-001: Session-Scope Shorthand Rule

- **Prompt**: Approve CONV-012 for codification in `workspace_documentation_rules.md` §7.C and cross-referenced in `guideline_workspace_implementation.md`.
- **Options**:
  - (a) Approve as stated.
  - (b) Require fully-qualified IDs everywhere (no shorthand).
  - (c) Allow shorthand at stream scope (broader than activity scope).
- **Recommendation**: (a)
- **Owner**: Client

### DEC-002: Hybrid SPEC Item Structure

- **Prompt**: Approve CONV-013 for amendment of both IMPLEMENTATION templates and guideline §III.
- **Options**:
  - (a) Approve hybrid structure (table + prose).
  - (b) Keep table-only structure with rendering guidance.
  - (c) Move entirely to prose (no metadata table).
- **Recommendation**: (a)
- **Owner**: Client

### DEC-003: DEV-REPORT Implementation Reference

- **Prompt**: Approve CONV-014 for amendment of dev-report guideline §IV, dev-report template, and implementation guideline §VII.C.
- **Options**:
  - (a) Approve `implementation_reference` as SHOULD (recommended).
  - (b) Approve as MUST (mandatory).
  - (c) Defer to dev-report-specific activity.
- **Recommendation**: (a)
- **Owner**: Client

### DEC-004: Execution Audience Parametrization

- **Prompt**: Approve the mechanism for distinguishing developer-executed vs consultant-executed task specifications.
- **Options**:
  - (a) **New subtype** (`consultation_specification`) -- new subtype in taxonomy, dedicated template, dedicated trigger. Precedent: TOGAF separates ABBs from SBBs. Pro: clean type boundary. Con: taxonomy expansion, third template, fragments structurally similar artifacts.
  - (b) **Parametric field** (`execution_audience` frontmatter) -- single `task_specification` subtype with optional field driving authority chain. Precedent: IEEE 830 uses same SRS format for different audiences. Pro: minimal change, existing template reused. Con: authority chain becomes conditional.
  - (c) **Guidance-only** -- no schema change, add a note to guideline §III.B. Pro: simplest. Con: weakest enforcement.
- **Recommendation**: (b) -- the SPEC item structure is identical; only the downstream evidence surface changes. This is a parametric variation, not a structural one.
- **Owner**: Client

---

## V. IMPACT AND RISKS

### A. Impact Assessment

- **Positive outcomes**: Completes the IMPLEMENTATION family's cross-family linkage chain; improves execution precision via hybrid SPEC structure; resolves P-STD-005 compliance gap in Requirement Source references; parametrizes execution audience without taxonomy expansion.
- **Tradeoffs**: Template changes (CONV-013) require re-familiarization by authors; existing specs (TK003.1) are grandfathered under old format.

### B. Risks

| Risk ID | Description | Severity | Mitigation |
|:--|:--|:--|:--|
| RISK-001 | If Option A (DEC-004) is selected by external review, scope expands to new subtype + template -- this should be a separate activity (AC001.8) per the AC001.7 precedent (SES002-DP005). | Low | Client has already selected Option B in SES003. Record all options in this proposal for external review visibility. |

---

## VI. REFERENCES

| Document | Path |
|:--|:--|
| Governing Plan | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/plan_T104-PH001-ST008-AC001.6.md` |
| Companion Standards-Input Proposal (Vertical) | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/proposal/proposal_T104-PH001-ST008-AC001.6_implementation-vertical-integration-architecture.md` |
| SES002 Session Notes | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/snotes/snotes_T104-PH001-ST008-AC001.6-SES002.md` |
| Implementation Guideline | `prompt/templates/consultant/workspace/guideline_workspace_implementation.md` |
| Documentation Rules | `prompt/templates/consultant/workspace/workspace_documentation_rules.md` |
| Dev-Report Guideline | `prompt/templates/consultant/workspace/guideline_workspace_dev-report.md` |
| Dev-Report Template | `prompt/templates/consultant/workspace/template_workspace_dev-report.md` |

---

## VII. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-03-21 | Initial | Standards-input proposal for horizontal IMPLEMENTATION family amendments (CONV-012 through CONV-015). Covers session-scope shorthand rule, hybrid SPEC item structure, DEV-REPORT implementation reference backlink, and execution audience parametrization. Source: SES002--SES003 QA consultation. |
