---
artifact_type: 'PROPOSAL'
initiative_id: 'T104'
initiative_code: 'CWS'
phase: '1'
stream_id: 'T104-PH001-ST007'
activity_id: 'T104-PH001-ST007-AC005'
task_id: 'T104-PH001-ST007-AC005-TK008.4'
version: '1.0.0'
date: '2026-03-12'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST007/AC005/plan_T104-PH001-ST007-AC005.md'
purpose: 'Execution-ready checkpoint and rollback capture contract for TK009 and TK010.'
---

# PROPOSAL: TK008.4 Checkpoint And Rollback Capture Contract

## I. Summary

This contract locks the required checkpoint timing, checkpoint contents, output locations, and rollback evidence for AC005 live execution.

Primary rollback rule:
- Any failure during `TK009` or `TK010` rolls back to the pre-`TK009` checkpoint.
- Manifest-emitted rollback files are required evidence and rollback aids, but they do not replace the full pre-`TK009` checkpoint.

## II. Pre-TK009 Checkpoint Timing

Capture the checkpoint:
- after `GATE-002` records an approving client decision
- before the first live `TK009` manifest command is started
- from the `prompt/` git repository root

No live filesystem mutation under `prompt/artifacts/tasks/T102/` may occur between checkpoint capture and the first `TK009` apply command.

## III. Required Checkpoint Contents

Checkpoint storage root:
- `prompt/scripts/output/T104-PH001-ST007-AC005/live-execution/pre-tk009-checkpoint/`

Required contents:
- `tree/`: a full byte-for-byte copy of `prompt/artifacts/tasks/T102/`
- `git_head.txt`: output of `git -C prompt rev-parse HEAD`
- `git_status.txt`: output of `git -C prompt status --short`
- `checkpoint_manifest.md`: a short manifest recording:
  - capture timestamp
  - operator
  - manifest bundle references used for live execution (`ac005a` manifests)
  - references to the `TK008.1` baseline and the `TK008.3` allowlist contract

## IV. Required Live-Pass Outputs

### TK009 root pass

Store outputs under:
- `prompt/scripts/output/T104-PH001-ST007-AC005/live-execution/tk009-root/`

Required files:
- root live-apply report
- root rollback manifest renamed to a stable file name
- command log with exit code and executed command line

### TK010 epic pass

Store outputs under:
- `prompt/scripts/output/T104-PH001-ST007-AC005/live-execution/tk010-epics/`

Required files per epic:
- `T102A/` live-apply report + rollback manifest + command log
- `T102B/` live-apply report + rollback manifest + command log
- `T102C/` live-apply report + rollback manifest + command log

## V. Rollback Decision Rule

Use the pre-`TK009` checkpoint as the primary rollback target if any of the following occurs:
- a manifest apply exits non-zero
- a completeness check fails
- post-pass spot checks show a partial or conflicting state
- any epic pass fails after the root pass has already mutated the live tree

The manifest rollback files must still be preserved even when the full checkpoint restore is used.

## VI. References

- `prompt/artifacts/tasks/T104/workspace/PH001/ST007/AC005/plan_T104-PH001-ST007-AC005.md`
- `prompt/scripts/output/T104-PH001-ST007-AC005/ac005a/index_T104-PH001-ST007-AC005_gate-001-package.md`
- `prompt/scripts/output/T104-PH001-ST007-AC005/ac005b/validation_T104-PH001-ST007-AC005_tk008.1_pre-apply-baseline.md`
- `prompt/artifacts/tasks/T104/workspace/PH001/ST007/AC005/proposal/proposal_T104-PH001-ST007-AC005-TK008.3_baseline-plus-allowlist-contract.md`
