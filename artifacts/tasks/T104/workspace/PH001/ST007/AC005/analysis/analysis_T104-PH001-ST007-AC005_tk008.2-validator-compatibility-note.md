---
artifact_type: 'ANALYSIS'
analysis_type: 'validator_compatibility_note'
initiative_id: 'T104'
initiative_code: 'CWS'
phase: '1'
stream_id: 'T104-PH001-ST007'
activity_id: 'T104-PH001-ST007-AC005'
task_id: 'T104-PH001-ST007-AC005-TK008.2'
version: '1.0.0'
date: '2026-03-12'
status: 'draft'
author: 'LLM_Developer'
decision_owner_role: 'Client'
source_plan: 'prompt/artifacts/tasks/T104/workspace/PH001/ST007/AC005/plan_T104-PH001-ST007-AC005.md'
---

# ANALYSIS: TK008.2 Validator Compatibility Note

## I. Summary

`validate_initiative_structure.py` is compatible with the canonical post-migration AC005 target structure after the bounded `TK008.*` validator remediations completed on `2026-03-12`.

Evidence basis:
- `TK008.1` strict live baseline against the current `T102` tree: `57` errors / `47` warnings
- `TK008.2` strict sandbox preflight against the migrated temp tree: `53` errors / `30` warnings

Compatibility conclusion:
- No unresolved validator-only blocker remains before `GATE-002`.
- The remaining preflight findings are attributable to known content debt or pre-existing gaps, not to validator inability to interpret the canonical target layout.

## II. Remediations Applied During TK008

The sandbox preflight initially surfaced two validator mismatches with the approved AC005 target structure:

1. Phase-level workspace type directories such as `workspace/PH000/raw/`, `workspace/PH000/analysis/`, and `workspace/PH001/snotes/` were being flagged as non-canonical stream directories.
2. Stream-level `communication/` files that legitimately include an AC token in the filename were being rejected by the UID-scope rule.

Both issues were fixed inside `TK008.*` by updating `prompt/scripts/validate_initiative_structure.py` and extending `prompt/scripts/tests/test_validate_initiative_structure.py`.

## III. Compatibility Assessment

The rerun strict sandbox validator report demonstrates that the validator now accepts the migrated AC005 structure without the earlier tooling-only false positives.

Observed result:
- The preflight report no longer contains the phase-level workspace directory warnings.
- The preflight report no longer contains the stream communication UID-placement error.
- The post-migration result set is smaller than baseline, which confirms the validator is reading the migrated structure coherently rather than inventing new layout failures.

Residual findings that remain after preflight fall into three buckets only:
- legacy raw transcript filenames that still violate the SES-token naming rule
- retained legacy files whose prefixes remain non-canonical after migration
- the already documented `T102-RES-009` missing brief gap surfaced by canonical research co-location

## IV. Constraints For TK012

- `TK012` must compare post-apply findings against the `TK008.3` allowlist contract, not against literal zero.
- The `T102-RES-009` missing brief gap must be treated as a documented pre-existing latent issue, not an AC005-caused regression.
- The validator output is now suitable to govern `TK012` acceptance, provided the post-apply run does not introduce findings outside the locked allowlist contract.

## V. References

- `prompt/scripts/output/T104-PH001-ST007-AC005/ac005b/validation_T104-PH001-ST007-AC005_tk008.1_pre-apply-baseline.md`
- `prompt/scripts/output/T104-PH001-ST007-AC005/ac005b/ledger_T104-PH001-ST007-AC005_tk008.1_pre-apply-findings.md`
- `prompt/scripts/output/T104-PH001-ST007-AC005/ac005b/validation_T104-PH001-ST007-AC005_tk008.2_post-migration-preflight.md`
- `prompt/scripts/output/T104-PH001-ST007-AC005/ac005b/ledger_T104-PH001-ST007-AC005_tk008.2_post-migration-preflight-findings.md`
- `prompt/scripts/validate_initiative_structure.py`
- `prompt/scripts/tests/test_validate_initiative_structure.py`
