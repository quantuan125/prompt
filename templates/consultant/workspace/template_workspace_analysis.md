---
artifact_type: 'ANALYSIS'
analysis_type: '[pattern_audit|research_synthesis|compliance_audit|assessment|external_review]'
initiative_id: '[ID]'
initiative_code: '[CODE]'
phase: '[#]'
stream_id: '[UID]'
activity_id: '[UID]'
task_id: '[UID]'
gate_id: '[UID]'
version: '2.1.0'
date: 'YYYY-MM-DD'
status: 'draft'
# status options: 'draft' | 'active' | 'completed' | 'superseded'
# If 'superseded': add superseded_by key (below) and deprecation notice as first body line (see guideline_workspace_analysis.md §IX)
# superseded_by: '[repo-relative path to the successor artifact that assesses against the updated baseline]'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: '[path to plan file]'
purpose: '[1-line purpose]'
---

# ANALYSIS: [Title] ([scope-UID])

<!--
SINGLE-TEMPLATE RULE:
- This is the one canonical ANALYSIS template for all analysis types.
- Keep universal sections (I–IV).
- Remove non-applicable conditional blocks.

CONDITIONAL MARKER CONVENTION (DEC004):
- Use HTML comments at section boundaries.
- Example marker: place an HTML comment at the section header with text `RESEARCH_SYNTHESIS ONLY — omit for other analysis types`

SUPERSEDED ANALYSIS AUTHORING (see guideline_workspace_analysis.md §IX):
When this artifact is deprecated because the gate it supports was superseded:
1. Update frontmatter: set `status: 'superseded'` and add `superseded_by: '<path>'`
2. Add deprecation notice as the FIRST line of the body (after this comment block):
   > **SUPERSEDED**: This artifact was produced against [baseline X]. It has been superseded by [successor path] which assesses against [baseline Y]. This artifact is preserved for historical traceability only.
3. Bump the version and add a changelog entry.
4. Do NOT alter any body content — preserve the historical record unchanged.
-->

## I. EXECUTIVE SUMMARY

**Purpose**: [1–2 sentences]
**Scope**: [What this covers]
**Conclusion / Recommendation**: [One clear headline outcome]

---

## II. SCOPE & INPUTS

**In scope**:
- [Item]

**Out of scope**:
- [Item]

**Inputs reviewed (repo-relative paths)**:
- `[path]`

---

## III. EVIDENCE / METHODOLOGY

**Method**:
- [How claims were derived]

**Commands run (if any)**:
```bash
[command]
```

**Evidence notes**:
- [What the command/file check demonstrated]

---

## IV. FINDINGS / GAP REGISTER

> This is a lightweight tracking register (not gate verification findings).

| GAP ID | Category | Title | Description | Disposition | Downstream Target | Notes |
|:--|:--|:--|:--|:--|:--|:--|
| GAP-001 | [structure/naming/...] | [Title] | [What is wrong + evidence pointer] | [pending_decision/resolved/.../deferred_to_TK###] | [e.g., TK003] | [Notes] |

---

<!-- PATTERN_AUDIT ONLY — omit for other analysis types -->
## V. PATTERN AUDIT (PATTERN INVENTORY + TEMPLATE GAP ANALYSIS)

### A. Exemplars Reviewed
- `[path]` — [1-line why it matters]

### B. Pattern Extraction (What is stable?)
- [Pattern]

### C. Template/Guideline Gap Analysis (What must change?)
- [Gap]

### D. Downstream Decisions / Actions
See Section VIII (Downstream Actions).

---

<!-- COMPLIANCE_AUDIT ONLY — omit for other analysis types -->
## V. COMPLIANCE AUDIT (CHECKLIST RESULTS)

**Audit target**: `[path]`
**Baseline authority**: [standards/guidelines used]

| # | Criterion | Expected | Observed Evidence | Result |
|:--|:--|:--|:--|:--|
| 1 | [Rule] | [Expected] | [Observed] | [PASS/FAIL/OBS] |

---

<!-- ASSESSMENT ONLY — omit for other analysis types -->
## V. ASSESSMENT (READINESS / OPTIONS / TRADEOFFS)

### A. Current State Summary
- [Observation]

### B. Options
1) [Option A] — [tradeoffs]
2) [Option B] — [tradeoffs]

### C. Recommendation
- [What to do and why]

---

<!-- EXTERNAL_REVIEW ONLY — omit for other analysis types -->
## V. EXTERNAL REVIEW (INDEPENDENT ASSESSMENT)

**Engagement scope**: [What was requested]
**Materials reviewed**:
- `[path]`

### A. Strengths
- [Item]

### B. Concerns / Risks
- [Item]

### C. Recommendations
- [Item]

---

<!-- RESEARCH_SYNTHESIS ONLY — omit for other analysis types -->
## V. SOURCE MATERIAL SUMMARY

### A. Research Brief Context
**Research ID**: [RES-ID]
**Brief**: `[path]`

### B. Research Report Overview
**Report**: `[path]`

---

<!-- RESEARCH_SYNTHESIS ONLY — omit for other analysis types -->
## VI. KEY FINDINGS EXTRACTION

### Topic 1: [TOPIC TITLE]
**Research finding**: [summary]
**Consultant assessment**:
- **Significance**: [H/M/L]
- **Confidence**: [H/M/L]
**Actionable insights**:
- [Insight]

---

<!-- RESEARCH_SYNTHESIS ONLY — omit for other analysis types -->
## VII. E-ID CANDIDATE MAPPING

> This section seeds proposal work; keep ID/tooling constraints in mind.

| Candidate ID | Title | Source | Rationale | Priority |
|:--|:--|:--|:--|:--|
| [E-ASSUM-001] | [Title] | [Section ref] | [Why] | [H/M/L] |

---

<!-- RESEARCH_SYNTHESIS ONLY — omit for other analysis types -->
## VIII. INTEGRATION ROADMAP

1. [Step]
2. [Step]

---

<!-- NON-RESEARCH ONLY — omit for research_synthesis -->
## VIII. DOWNSTREAM ACTIONS

| downstream_artifact_type | target_reference | trigger_condition | responsible_role | notes |
|:--|:--|:--|:--|:--|
| [e.g., guideline] | `[path]` | [when] | [role] | [notes] |

---

## IX. REFERENCES / LINKS REGISTER

| Item | Reference |
|:--|:--|
| Plan | `[plan_reference]` |
| Decisions | `[decision/proposal path if applicable]` |
| Primary inputs | `[paths]` |

---

## X. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v2.1.0 | 2026-03-20 | Amendment | Frontmatter: added comment block documenting `status: 'superseded'` and `superseded_by` key usage with inline guidance on when to apply. Added `SUPERSEDED ANALYSIS AUTHORING` comment block with step-by-step instructions for deprecating an analysis artifact. Source: T104-PH001-ST008-AC001.4 GATE-001 (2026-03-20). |
| v2.0.0 | 2026-03-01 | Rewrite | Replaced research-synthesis-only template with single-template, multi-type structure using conditional sections; added `analysis_type`, universal Scope/Inputs + Evidence + GAP register, and non-research Downstream Actions. |
