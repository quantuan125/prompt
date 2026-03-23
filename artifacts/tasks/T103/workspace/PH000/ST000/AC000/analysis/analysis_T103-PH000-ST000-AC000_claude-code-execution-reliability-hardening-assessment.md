---
artifact_type: 'ANALYSIS'
analysis_type: 'assessment'
initiative_id: 'T103'
initiative_code: 'ADRSS'
phase: '0'
stream_id: 'T103-PH000-ST000'
activity_id: 'T103-PH000-ST000-AC000'
task_id: 'T103-PH000-ST000-AC000-TK006.1'
version: '1.0.0'
date: '2026-03-23'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000/plan_T103-PH000-ST000-AC000.md'
purpose: 'Corrected factual baseline for the AC001.6 Claude Code orchestration incident and the post-GATE-002 execution-reliability hardening scope for AC000.'
assessment_scope: 'Incident timeline normalization, authorship clarification, duplicate-launch risk assessment, and downstream hardening scope definition.'
communication_reference: 'prompt/artifacts/tasks/T103/workspace/PH000/ST000/communication/comm_T104-PH001-ST008-AC001.6_claude-code-skill-external-review-execution-reliability.md'
source_analysis: 'prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/analysis/analysis_T104-PH001-ST008-AC001.6_downstream-readiness-second-opinion.md'
---

# ANALYSIS: Claude Code Execution Reliability Hardening Assessment (AC000)

## I. EXECUTIVE SUMMARY

**Purpose**: Correct the factual record for the AC001.6 Claude Code orchestration incident, distinguish runtime failure modes from artifact authorship, and define the post-`GATE-002` hardening scope that AC000 should commission next.

**Scope**: Reconstruct the 2026-03-22 AC001.6 execution timeline using the verified Codex and Claude runtime logs, the existing T104 downstream-readiness substitute analysis, the original T104 -> T103 communication artifact, and the current AC000 remediation package.

**Conclusion / Recommendation**: The original T104 -> T103 communication correctly identified a real reliability gap, but it overstated one point: the existence of the downstream-readiness artifact does not prove that Claude Code's direct repo-write path succeeded, and the cleanest explanation is not "Claude failed once." The verified sequence is that Codex launched a direct-authoring Claude run, declared failure too early, failed to clean up or dedupe the still-live work, launched additional Claude execution paths, and then later materialized the on-disk artifact itself. The downstream hardening target is therefore broader than direct-authoring guidance alone: AC000 now needs explicit single-flight execution control, patience / bounded polling rules, cleanup ownership for spawned Claude work, and artifact-provenance reporting rules before any further Codex-mediated Claude automation is treated as reliable.

### Client Summary

- The AC001.6 incident was real, but the original communication artifact was factually incomplete rather than wholly wrong.
- The on-disk downstream-readiness artifact was materialized by Codex fallback on 2026-03-22, not by a clean Claude direct-write success path.
- At least one separate Claude session still produced comparable analysis content, but it hit a write-permission gate and then a rate-limit event before completing the intended repo write.
- The operational defect was not only Claude runtime behavior; it was also Codex orchestration behavior.
- The most costly failure was lack of process ownership: background Claude runs kept consuming client-side Opus usage until the client manually killed them.
- The missing controls are single-flight execution, patience before declaring failure, explicit fallback gating, background-run cleanup, and provenance reporting.
- The original T104 -> T103 `comm_` should remain preserved for traceability, but this analysis is now the current factual baseline for downstream T103 work.
- AC000 should keep `GATE-002` scoped to acceptance of the already-implemented 2026-03-22 remediation package.
- Post-`GATE-002` hardening should remain inside AC000 as a new `GATE-003` lane, not a new activity.

## II. SCOPE & INPUTS

**In scope**:
- Reconstruction of the 2026-03-22 AC001.6 Claude Code execution incident
- Clarification of who produced content versus who created the final on-disk artifact
- Assessment of why duplicate background Claude runs occurred
- Definition of the next AC000 hardening scope after `GATE-002`

**Out of scope**:
- Re-opening the already-implemented 4-batch remediation accepted into the current `GATE-002` package
- Re-running Claude or Codex sessions
- Executing the downstream hardening changes in `.agents/skills/claude-code/` during this consultation package

**Inputs reviewed**:
- `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000/analysis/analysis_T103-PH000-ST000-AC000_claude-code-skill-review.md`
- `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000/implementation_T103-PH000-ST000-AC000_claude-code-skill-remediation.md`
- `prompt/artifacts/tasks/T103/workspace/PH000/ST000/communication/comm_T104-PH001-ST008-AC001.6_claude-code-skill-external-review-execution-reliability.md`
- `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/analysis/analysis_T104-PH001-ST008-AC001.6_downstream-readiness-second-opinion.md`
- `/home/quantuan125/.codex/log/codex-tui.log`
- `/home/quantuan125/.codex/sessions/2026/03/22/rollout-2026-03-22T17-35-35-019d151d-4fd5-72e0-a38d-59b317503251.jsonl`
- `/home/quantuan125/.claude/projects/-mnt-c-users-quant-onedrive-documents-purpose-crypto-perp/e1ada273-65da-44c7-a773-2bcf123ccb9e.jsonl`
- `/home/quantuan125/.claude/projects/-mnt-c-users-quant-onedrive-documents-purpose-crypto-perp/096deb59-a8fd-46ce-9a91-641d88c6c61a.jsonl`

## III. EVIDENCE / METHODOLOGY

**Method**:
- Re-read the AC000 assessment and implementation surfaces to determine what the original T103 package did and did not scope.
- Reconstruct the AC001.6 incident timeline from Codex rollout logs, Codex UI logs, and local Claude session logs.
- Compare the runtime evidence to the narrative in the original T104 -> T103 communication artifact and the T104 downstream-readiness substitute analysis.
- Translate the verified incident into consultant-owned hardening requirements suitable for post-`GATE-002` developer execution.

**Commands run (representative)**:
```bash
git -C prompt status --short -- prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/analysis/analysis_T104-PH001-ST008-AC001.6_downstream-readiness-second-opinion.md
rg -n "apply_patch|analysis_T104-PH001-ST008-AC001.6_downstream-readiness-second-opinion" /home/quantuan125/.codex/log/codex-tui.log
sed -n '1,260p' /home/quantuan125/.codex/sessions/2026/03/22/rollout-2026-03-22T17-35-35-019d151d-4fd5-72e0-a38d-59b317503251.jsonl
sed -n '1,260p' /home/quantuan125/.claude/projects/-mnt-c-users-quant-onedrive-documents-purpose-crypto-perp/e1ada273-65da-44c7-a773-2bcf123ccb9e.jsonl
sed -n '1,260p' /home/quantuan125/.claude/projects/-mnt-c-users-quant-onedrive-documents-purpose-crypto-perp/096deb59-a8fd-46ce-9a91-641d88c6c61a.jsonl
```

**Evidence notes**:
- The target downstream-readiness artifact was still untracked in `prompt/`, which is consistent with local materialization during the 2026-03-22 session rather than a committed Claude-owned write path.
- `codex-tui.log` records an `apply_patch` `*** Add File:` for the downstream-readiness artifact at `2026-03-22T11:00:17Z`.
- The first delegated Codex subagent launched a direct-authoring Claude run at `2026-03-22T10:43:50Z`, then declared the path unreliable after bounded polling when the file was still absent.
- A separate Claude `plan`-mode session produced a concise read-only assessment, not a repo write.
- Another later Claude direct-authoring session generated substantive draft content, but the session hit an explicit write-permission request and then a rate-limit event before completing the intended file write.
- The client-side token waste came from duplicate or still-live Claude processes that Codex did not automatically tear down after changing execution strategy.

## IV. INCIDENT RECONSTRUCTION

### A. Verified timeline

1. On 2026-03-22 at `10:43:50Z`, Codex launched a direct-authoring Claude run targeted at the AC001.6 downstream-readiness artifact.
2. Codex polled for file existence, found no artifact yet, and treated the direct-authoring path as unreliable.
3. Codex then launched a fallback Claude `plan`-mode run that returned a concise assessment rather than a repo write.
4. A separate direct-authoring Claude session later generated full review content, but its write path did not complete because a write-permission request remained unresolved and the session then hit a rate-limit condition.
5. On 2026-03-22 at `11:00:17Z`, Codex materialized the final on-disk downstream-readiness artifact via `apply_patch`.

### B. Authorship clarification

- **Claude generated review content** in at least one later blocked session.
- **Claude did not complete the intended direct repo-write path** for the surviving on-disk artifact.
- **Codex created the final on-disk artifact** that now exists at the AC001.6 analysis path.

### C. Root failure pattern

The incident was a combined runtime and orchestration problem:
- Codex was too impatient about a still-live direct-authoring run.
- Codex had no single-flight protection for one target artifact / one active Claude attempt.
- Codex did not block fallback launch while prior Claude work was still live or unresolved.
- Codex did not own teardown of the Claude processes it had spawned.
- The skill guidance had no explicit provenance rule to distinguish content generation, file creation, and substitute artifact authorship.

## V. FINDINGS / GAP REGISTER

| GAP ID | Category | Title | Description | Disposition | Downstream Target | Notes |
|:--|:--|:--|:--|:--|:--|:--|
| GAP-001 | workflow | Factual baseline for the incident is split across incomplete artifacts | The original T104 -> T103 communication is directionally right but materially incomplete on artifact authorship and duplicate-run causality. | `resolved` | This analysis artifact | This analysis becomes the current AC000 factual baseline. |
| GAP-002 | workflow | Single-flight execution control is absent | Codex launched additional Claude execution paths for the same target scope before the prior path was definitively resolved. | `deferred_to_TK008` | Post-GATE-002 hardening implementation | Hardening must define one active Claude run per target artifact/session scope. |
| GAP-003 | workflow | Spawned-process ownership and cleanup are absent | Codex did not automatically tear down or explicitly hand off responsibility for background Claude processes after changing strategies. | `deferred_to_TK008` | Post-GATE-002 hardening implementation | This was the immediate cause of unnecessary client-side Opus usage. |
| GAP-004 | workflow | Premature failure classification is under-specified | The orchestration loop treated "file not present yet" as equivalent to definitive failure without a stronger bounded wait / blocked-state policy. | `deferred_to_TK008` | Post-GATE-002 hardening implementation | The missing control is patience plus state-aware fallback gating. |
| GAP-005 | consistency | Artifact provenance reporting is under-specified | Existing skill and communication surfaces do not distinguish "Claude produced content" from "Claude created the final file" from "consultant-authored substitute." | `deferred_to_TK008` | Post-GATE-002 hardening implementation | This gap created the later authorship confusion. |
| GAP-006 | workflow | Validation does not cover client-cost containment scenarios | The current testing posture validates command shapes and smoke behavior, but not duplicate-launch prevention, orphan-process handling, or explicit token-spend containment. | `deferred_to_TK008` | Post-GATE-002 hardening implementation | Future `GATE-003` evidence must cover this explicitly. |

## VI. ASSESSMENT (POST-GATE-002 HARDENING POSITION)

### A. Why the original 4-batch package should remain intact

The currently staged `GATE-002` package is still valid for what it claimed to do on 2026-03-22: improve baseline Claude Code skill parity, safety defaults, and validation coverage. The incident reviewed here surfaced an additional orchestration and runtime-control scope that was not part of the original gap set. The correct action is therefore to preserve the original package and add a new post-`GATE-002` hardening lane, not to retroactively pretend the original package had already solved this new class of failure.

### B. Recommended hardening boundary

The post-`GATE-002` hardening package should cover:
- execution-state ownership in the Claude Code skill workflow;
- explicit patience / bounded polling rules before classifying failure;
- no-fallback / no-duplicate-launch controls while a prior Claude run remains live;
- spawned-process cleanup or mandatory user-directed teardown behavior;
- direct-authoring reliability guidance versus consultant-write fallback guidance;
- artifact provenance / authorship reporting requirements;
- manual test scenarios for orphan processes, duplicate launches, slow runs, trust-prompt blocking, and client-cost containment.

## VII. DOWNSTREAM ACTIONS

| downstream_artifact_type | target_reference | trigger_condition | responsible_role | notes |
|:--|:--|:--|:--|:--|
| PLAN amendment | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000/plan_T103-PH000-ST000-AC000.md` | This assessment published | LLM_Consultant | Add the completed correction-analysis task and the post-`GATE-002` `GATE-003` hardening lane. |
| IMPLEMENTATION (task_specification) | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000/implementation/implementation_T103-PH000-ST000-AC000_claude-code-execution-reliability-hardening.md` | `GATE-002` records `APPROVE` or `APPROVE WITH CONDITIONS` | LLM_Consultant | Developer-facing hardening specification seeded from this analysis. |
| Skill update | `.agents/skills/claude-code/SKILL.md` | Post-`GATE-002` hardening execution commissioned | LLM_Developer | Add execution ownership, fallback gating, cleanup, provenance, and reliability guidance. |
| Reference and validation updates | `.agents/skills/claude-code/references/claude-code-cli.md`; `.agents/skills/claude-code/references/claude-code-testing.md`; `.agents/skills/claude-code/scripts/validate_claude_code_skill.py` | Post-`GATE-002` hardening execution commissioned | LLM_Developer | Extend runtime guidance, manual matrix coverage, and static checks for the new controls. |
| Historical traceability update | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/communication/comm_T104-PH001-ST008-AC001.6_claude-code-skill-external-review-execution-reliability.md` | This assessment published | LLM_Consultant | Preserve the original communication artifact with a minimal historical note and backlink. |

## VIII. REFERENCES / LINKS REGISTER

| Item | Reference |
|:--|:--|
| Governing activity plan | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000/plan_T103-PH000-ST000-AC000.md` |
| Original AC000 assessment | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000/analysis/analysis_T103-PH000-ST000-AC000_claude-code-skill-review.md` |
| Original AC000 remediation specification | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000/implementation_T103-PH000-ST000-AC000_claude-code-skill-remediation.md` |
| Historical T104 -> T103 communication | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/communication/comm_T104-PH001-ST008-AC001.6_claude-code-skill-external-review-execution-reliability.md` |
| T104 downstream-readiness substitute analysis | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/analysis/analysis_T104-PH001-ST008-AC001.6_downstream-readiness-second-opinion.md` |

## IX. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-03-23 | Initial | Corrected the factual baseline for the AC001.6 Claude Code orchestration incident, clarified artifact authorship versus content generation, recorded the duplicate-launch / orphan-process defect, and defined the post-`GATE-002` execution-reliability hardening scope for AC000. |
