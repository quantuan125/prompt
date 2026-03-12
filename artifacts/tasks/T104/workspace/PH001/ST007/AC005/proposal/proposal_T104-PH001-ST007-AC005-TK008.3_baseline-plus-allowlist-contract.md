---
artifact_type: 'PROPOSAL'
initiative_id: 'T104'
initiative_code: 'CWS'
phase: '1'
stream_id: 'T104-PH001-ST007'
activity_id: 'T104-PH001-ST007-AC005'
task_id: 'T104-PH001-ST007-AC005-TK008.3'
version: '1.0.0'
date: '2026-03-12'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST007/AC005/plan_T104-PH001-ST007-AC005.md'
analysis_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST007/AC005/analysis/analysis_T104-PH001-ST007-AC005_tk008.2-validator-compatibility-note.md'
purpose: 'Authoritative baseline-plus-allowlist acceptance contract for TK012 post-apply validation.'
---

# PROPOSAL: TK008.3 Baseline-Plus-Allowlist Contract

## I. Summary

This artifact defines the only residual validator findings that may remain acceptable after AC005 live apply.

Reference evidence:
- strict live baseline (`TK008.1`): `57` errors / `47` warnings
- strict sandbox preflight (`TK008.2`): `53` errors / `30` warnings

Acceptance rule for `TK012`:
- Any post-apply finding outside the allowlist below is an AC005 regression.
- Any allowlisted finding that appears with a higher count than allowed is an AC005 regression.
- Any baseline finding listed in Section IV as expected-to-clear must not recur post-apply.

## II. Comparison Rules

### R-001 Exact-match rule

Use the full validator message verbatim when the allowlist row specifies `match_mode = exact`.

### R-002 Basename-match rule

Use `severity + finding-family + basename(file_path_in_message)` when the allowlist row specifies `match_mode = basename`.

This rule exists because AC005 intentionally relocates many files into canonical targets while preserving their legacy filenames. Under this rule:
- the path portion may change
- the severity and validator family must stay the same
- the basename must stay the same

### R-003 Latent-gap exception

One post-migration error was not expressible in the live baseline because the pre-migration tree lacked canonical `research/<RES-ID>/` directories. That finding is allowlisted only because it is already documented as a pre-existing gap in AC005 readiness evidence.

## III. Allowlist Register

| Allowlist ID | Baseline Reference | Preflight Reference | Severity | Match Mode | Max Count | Allowed Residual | Rationale |
|:--|:--|:--|:--|:--|--:|:--|:--|
| `ALW-001` | `ERR-006` through `ERR-057` | `PERR-002` through `PERR-053` | `error` | `basename` | 52 | Raw transcript SES-token naming failures after relocation into canonical `workspace/**/raw/` targets | AC005 relocates these files but does not rename the historical raw artifacts. |
| `ALW-002` | `WRN-004`, `WRN-009` through `WRN-017`, `WRN-019` through `WRN-033`, `WRN-043` through `WRN-047` | `PWRN-001` through `PWRN-030` | `warning` | `basename` | 30 | Retained legacy-prefix markdown files that stay non-canonical after migration | AC005 normalizes placement, not every historical filename family. |
| `ALW-003` | `N/A - latent pre-existing gap` | `PERR-001` | `error` | `exact` | 1 | `Research directory missing brief artifact: research\T102-RES-009` | This gap is documented in AC005 readiness evidence and Gate-001 completeness material as pre-existing missing content. |

## IV. Findings Expected To Clear

The following `TK008.1` baseline findings are not allowlisted and must not appear after live apply:

- `ERR-001` through `ERR-005`: missing canonical root directories
- `WRN-001` through `WRN-003`: T102A standard filename-prefix warnings
- `WRN-005` through `WRN-008`: T102B standard filename-prefix warnings
- `WRN-018`: external review file warning
- `WRN-034` through `WRN-042`: root and T102C standard filename-prefix warnings

## V. TK012 Decision Rule

`TK012` passes only if all three statements hold:

1. Every post-apply finding matches exactly one allowlist row.
2. No allowlist row exceeds its `Max Count`.
3. None of the findings listed in Section IV recur.

If any statement fails, the result must be recorded as an AC005 regression requiring client review before `GATE-003`.

## VI. References

- `prompt/scripts/output/T104-PH001-ST007-AC005/ac005b/validation_T104-PH001-ST007-AC005_tk008.1_pre-apply-baseline.md`
- `prompt/scripts/output/T104-PH001-ST007-AC005/ac005b/ledger_T104-PH001-ST007-AC005_tk008.1_pre-apply-findings.md`
- `prompt/scripts/output/T104-PH001-ST007-AC005/ac005b/validation_T104-PH001-ST007-AC005_tk008.2_post-migration-preflight.md`
- `prompt/scripts/output/T104-PH001-ST007-AC005/ac005b/ledger_T104-PH001-ST007-AC005_tk008.2_post-migration-preflight-findings.md`
- `prompt/artifacts/tasks/T104/workspace/PH001/ST007/AC005/analysis/analysis_T104-PH001-ST007-AC005_tk008.2-validator-compatibility-note.md`
- `prompt/artifacts/tasks/T104/workspace/PH001/ST007/AC005/analysis/analysis_T104-PH001-ST007-AC005_t102-directory-readiness.md`
