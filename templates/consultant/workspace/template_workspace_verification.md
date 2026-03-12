---
artifact_type: 'VERIFICATION'
verification_type: '[GATE_REVIEW | commissioning_readiness | convention_compliance | ...]'
initiative_id: '[ID]'
initiative_code: '[CODE]'
phase: '[PH]'
stream_id: '[SID-PH###-ST###]'
activity_id: '[SID-PH###-ST###-AC###]'
gate_id: '[SID-PH###-ST###-AC###-GATE-###]'
version: '1.2.0'
date: '2026-03-12'
status: 'draft'
author: '[LLM_Reviewer | LLM_Consultant]'
decision_owner_role: 'Client'
target_plan: '[repo-relative path to activity or stream plan]'
targets:
  - '[repo-relative path to artifact being verified]'
primary_verification: '[repo-relative path — ONLY for supplementary artifacts; omit for primary]'
verification_scope: '[concise scope description]'
method: '[evidence-first methodology description]'
session_reference: '[repo-relative path to session notes, if applicable]'
---

# VERIFICATION: [GATE-ID]

## I. Scope & Method

**Scope**: [What is being verified — task range, deliverable set, gate entry criteria]

**Primary method (evidence-first)**:
1. [Step 1 — e.g., Read every deliverable artifact in full]
2. [Step 2 — e.g., Execute independent grep/search verification against each success criterion]
3. [Step 3 — e.g., Cross-reference specification indexes against actual content]
4. [...]

**Reviewer**: [Role — LLM_Reviewer or LLM_Consultant]
**Date**: YYYY-MM-DD

## II. Evidence Set (Artifacts Reviewed)

**Task deliverables**:
- `[repo-relative path]` ([description])
- `[repo-relative path]` ([description])

**Governance references**:
- `[repo-relative path]` ([description — plan, proposal, standard])

## III. Verification Checklist

### A. [Task/Criterion Group Name]

| # | Check | Expected | Observed Evidence | Result |
|:--|:--|:--|:--|:--|
| A1 | [What is being checked] | [Expected state] | [Specific evidence: line numbers, grep output, file paths] | **[PASS/FAIL]** |
| A2 | ... | ... | ... | ... |

### B. [Next Task/Criterion Group]

| # | Check | Expected | Observed Evidence | Result |
|:--|:--|:--|:--|:--|
| B1 | ... | ... | ... | ... |

## IV. Findings Register

<!-- If no findings: "No findings identified." -->

### FINDING-001 — [Short Title]

| Field | Detail |
|:--|:--|
| Severity | [Blocking / Major / Moderate / Low / Preventive] |
| Source | [Task check, section, artifact where identified] |
| Description | [What the issue is] |
| Classification | [Situation A (deliverable deficiency) / Situation B (scope gap)] |
| Required Action | [What must be done] |
| Owner | [Developer / Client] |
| Resolution Status | [open / resolved / accepted / waived] |
| Resolution Date | [YYYY-MM-DD or —] |

## V. Observations

<!-- If no observations: "No observations." -->

### OBS-001 — [Short Title]

[Description of the informational item, process improvement suggestion, or non-blocking note.]

## VI. Entry Criteria Assessment

| Entry Criterion | Status | Evidence |
|:--|:--|:--|
| [Criterion from gate definition] | **[MET / NOT MET]** | [Evidence reference] |
| ... | ... | ... |

## VII. Gate Recommendation

**Verdict**: **[PASS / CONDITIONAL PASS / PASS WITH DEFERRALS / RECYCLE / FAIL]**

**Rationale**:
- [Evidence point 1]
- [Evidence point 2]
- [...]

**Conditions** (if CONDITIONAL PASS):
- [Condition 1]
- [...]

**Deferrals** (if PASS WITH DEFERRALS):
- [Deferred item + owning activity/stream]
- [...]

**Reassessment Path** (RECYCLE only):
- `Same Gate Reassessed: [GATE-ID]`
- `Required Remediation Tasks: [TK### / TK###.n list]`
- `Downstream Tasks Still Blocked: [task list]`
- `Re-entry Basis: [what must be refreshed/resolved before re-review]`

> **Note**: The Gate Decision Record (GDR) is hosted in the `gate_disposition` proposal artifact, not in the verification artifact. See `guideline_workspace_proposal.md` §VII for GDR specification. The verification artifact's Gate Recommendation (above) provides the reviewer verdict that is consumed by the proposal's GDR.

## VIII. References

| Document | Path |
|:--|:--|
| [Document name] | `[repo-relative path]` |
| ... | ... |

## IX. Changelog

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.2.0 | 2026-03-12 | Amendment | Added `Reassessment Path` to the Gate Recommendation section for `RECYCLE` verdicts so the same-gate re-review path, remediation tasks, downstream block, and re-entry basis are explicit. |
| v1.1.0 | 2026-03-04 | Amendment | Removed §VIII (Gate Decision Record). GDR now hosted exclusively in gate_disposition proposals per `guideline_workspace_proposal.md` §VII. Added cross-reference note after Gate Recommendation section. Renumbered §IX→§VIII, §X→§IX. Source: T104-PH001-ST008-AC001 Option B approval. |
| v1.0.0 | YYYY-MM-DD | Initial | [Initial verification for GATE-###] |
