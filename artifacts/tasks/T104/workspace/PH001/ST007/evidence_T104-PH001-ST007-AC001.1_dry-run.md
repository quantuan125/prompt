# AC001.1 Consolidated Execution Evidence

- Activity: `T104-PH001-ST007-AC001.1`
- Date: `2026-02-15`
- Manifest: `prompt/artifacts/tasks/T104/workspace/PH001/ST007/manifest_T104-PH001-ST007-AC001.json`

## TK009 Dry-Run

- Command: `python3 prompt/scripts/migrate_initiative.py --manifest prompt/artifacts/tasks/T104/workspace/PH001/ST007/manifest_T104-PH001-ST007-AC001.json --project-root . --dry-run --report-path prompt/artifacts/tasks/T104/workspace/PH001/ST007/report_dry-run.md`
- Result: `success`
- Summary: `60` move operations, `4` directory create operations, reference rewrite pass executed.
- Artifact: `prompt/artifacts/tasks/T104/workspace/PH001/ST007/report_dry-run.md`

## TK010 Temp-Copy Validation

- Method: copied `prompt/artifacts/tasks/T104/` into a temporary root, applied manifest in temp root, then validated with strict validator.
- Validation command: `python3 prompt/scripts/validate_initiative_structure.py --initiative-root <temp>/prompt/artifacts/tasks/T104 --strict --report-path prompt/artifacts/tasks/T104/workspace/PH001/ST007/report_temp-copy-validation.md`
- Result: `0` errors, `0` warnings.
- Artifacts:
  - `prompt/artifacts/tasks/T104/workspace/PH001/ST007/report_temp-copy-apply.md`
  - `prompt/artifacts/tasks/T104/workspace/PH001/ST007/report_temp-copy-validation.md`

## TK012 Live Apply

- Command: `python3 prompt/scripts/migrate_initiative.py --manifest prompt/artifacts/tasks/T104/workspace/PH001/ST007/manifest_T104-PH001-ST007-AC001.json --project-root . --apply --report-path prompt/artifacts/tasks/T104/workspace/PH001/ST007/report_live-apply.md`
- Result: `success`
- Summary: `60` move operations applied, `4` directory create operations applied, `71` files updated by rewrite pass.
- Rollback artifact: `prompt/artifacts/tasks/T104/workspace/PH001/ST007/rollback_manifest.json`
- Artifact: `prompt/artifacts/tasks/T104/workspace/PH001/ST007/report_live-apply.md`

## TK013 Post-Migration Validation and Old-Path Scan

- Validation command: `python3 prompt/scripts/validate_initiative_structure.py --initiative-root prompt/artifacts/tasks/T104 --strict --report-path prompt/artifacts/tasks/T104/workspace/PH001/ST007/report_post-migration-validation.md`
- Validation result: `0` errors, `0` warnings.
- Old-path scan result: no residual matches outside manifest/evidence files.
- Artifacts:
  - `prompt/artifacts/tasks/T104/workspace/PH001/ST007/report_post-migration-validation.md`
  - `prompt/artifacts/tasks/T104/workspace/PH001/ST007/report_no-old-paths-scan.md`

## Gate Outcome Snapshot

- `GATE-001`: satisfied by manifest + script hardening + passing tests.
- `GATE-002`: satisfied by dry-run + temp-copy validation evidence.
- Execution proceeded to live apply after gate evidence completion.
