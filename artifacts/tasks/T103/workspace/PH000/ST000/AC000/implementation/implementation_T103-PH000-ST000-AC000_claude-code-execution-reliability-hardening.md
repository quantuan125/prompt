---
artifact_type: 'IMPLEMENTATION'
implementation_type: 'task_specification'
initiative_id: 'T103'
initiative_code: 'ADRSS'
phase: '0'
stream_id: 'T103-PH000-ST000'
activity_id: 'T103-PH000-ST000-AC000'
task_id: 'T103-PH000-ST000-AC000-TK008'
version: '1.0.0'
date: '2026-03-23'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000/plan_T103-PH000-ST000-AC000.md'
analysis_reference: 'prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000/analysis/analysis_T103-PH000-ST000-AC000_claude-code-execution-reliability-hardening-assessment.md'
execution_audience: 'developer'
purpose: 'Task specification for post-GATE-002 hardening of Codex-mediated Claude Code execution reliability, process ownership, and artifact provenance.'
---

# IMPLEMENTATION (Task Specification): Claude Code Execution Reliability Hardening

## I. PURPOSE & AUTHORITY

- **Purpose**: Detailed implementation specification for the post-`GATE-002` hardening package that addresses duplicate Claude launches, orphaned background runs, premature fallback behavior, and artifact-provenance ambiguity in Codex-mediated Claude Code usage.
- **Seed chain**:
  - Original baseline: `analysis_T103-PH000-ST000-AC000_claude-code-skill-review.md` -> `implementation_T103-PH000-ST000-AC000_claude-code-skill-remediation.md`
  - Incident hardening baseline: `analysis_T103-PH000-ST000-AC000_claude-code-execution-reliability-hardening-assessment.md` -> this implementation artifact
- **Authority boundary**: This artifact governs the future developer execution task `T103-PH000-ST000-AC000-TK008`. It does not reopen or replace the already-staged `GATE-002` package for the original 2026-03-22 remediation set.
- **Audience**: LLM_Developer (primary), LLM_Reviewer (downstream `GATE-003` consumer)
- This artifact does NOT hold a GDR. Gate decisions remain in proposal artifacts.

## II. TASK SCOPE

- **Governing analysis**: `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000/analysis/analysis_T103-PH000-ST000-AC000_claude-code-execution-reliability-hardening-assessment.md`
- **Trigger**: `GATE-002` records `APPROVE` or `APPROVE WITH CONDITIONS`, commissioning post-acceptance execution-reliability hardening inside AC000.
- **Deliverable contract**: Updated `.agents/skills/claude-code/SKILL.md`, updated Claude Code CLI reference, updated testing guide, and validator/test coverage aligned to the new reliability controls.
- **Execution posture**:
  - Preserve the original 4-batch remediation behavior unless it directly conflicts with the new reliability requirements.
  - Treat process ownership and client-cost containment as first-class requirements, not advisory notes.
  - Prefer rules that make failure explicit over rules that silently retry or spawn more work.

## III. SPECIFICATION ITEMS

### BATCH 1: Execution Ownership And State Control

---

### SPEC-001 - Add Explicit Single-Flight Execution Rule

| Field | Detail |
|:--|:--|
| Requirement Source | GAP-002 |
| Implementation Detail | Add a dedicated rule in `.agents/skills/claude-code/SKILL.md` stating that Codex must not launch a second Claude invocation for the same target artifact, task, or session scope while a prior Claude run remains live or unresolved. The rule must cover fresh runs, print-mode retries, fallback runs, and resume/continue flows. |
| Expected Format | Markdown subsection under a new execution-ownership or runtime-control section |
| Acceptance Criteria | The skill states one active Claude execution per target scope, forbids overlapping retries/fallbacks, and requires explicit resolution of the prior run before a new launch. |
| Status | `open` |

---

### SPEC-002 - Add Bounded Polling / Patience Rule Before Declaring Failure

| Field | Detail |
|:--|:--|
| Requirement Source | GAP-004 |
| Implementation Detail | Document that absence of an expected artifact during early polling is not by itself a definitive failure. Add a bounded wait / inspection sequence that distinguishes: still running, blocked on prompt/permission, completed with no artifact, and timed out. The rule must tell Codex to report uncertainty explicitly instead of silently re-routing immediately. |
| Expected Format | Ordered workflow bullets in `SKILL.md` |
| Acceptance Criteria | The skill defines a finite pre-failure inspection sequence and explicitly forbids equating "artifact not present yet" with definitive failure. |
| Status | `open` |

---

### SPEC-003 - Add No-Fallback-While-Live Rule

| Field | Detail |
|:--|:--|
| Requirement Source | GAP-002, GAP-004 |
| Implementation Detail | Add a rule that fallback modes (for example plan-mode second-opinion output or consultant-write substitute flow) may only begin after the prior Claude run is either completed, explicitly abandoned, or explicitly handed off to the user. |
| Expected Format | Guardrail bullet + workflow step |
| Acceptance Criteria | The skill forbids starting fallback work while the prior Claude process is still live or unresolved. |
| Status | `open` |

---

### SPEC-004 - Add Spawned-Process Ownership / Cleanup Rule

| Field | Detail |
|:--|:--|
| Requirement Source | GAP-003 |
| Implementation Detail | Add explicit language in `SKILL.md` that if Codex spawns a Claude process and then changes strategy, Codex must either (a) confirm the process ended, (b) surface that it is still live and ask the user for direction, or (c) explicitly hand off the still-live process to the user as an intentional takeover. Silent abandonment is forbidden. |
| Expected Format | New subsection in `SKILL.md` plus matching manual test scenario |
| Acceptance Criteria | The skill names process ownership as Codex's responsibility and forbids leaving background Claude work running without explicit disposition. |
| Status | `open` |

### BATCH 2: Direct-Authoring Reliability And Provenance

---

### SPEC-005 - Add Direct Artifact Authoring Reliability Posture

| Field | Detail |
|:--|:--|
| Requirement Source | GAP-004, GAP-005 |
| Implementation Detail | Extend `SKILL.md` and `.agents/skills/claude-code/references/claude-code-cli.md` with a dedicated direct-authoring posture that distinguishes: read-only print-mode review, print-mode direct authoring, TTY-backed authoring, and consultant-write fallback. Document that direct authoring may be unreliable when trust prompts, permission prompts, or blocked writes occur. |
| Expected Format | New runtime guidance section in `SKILL.md` plus CLI-reference note |
| Acceptance Criteria | Both surfaces distinguish supported direct-authoring patterns from fallback patterns and name the relevant failure modes. |
| Status | `open` |

---

### SPEC-006 - Add Artifact Provenance / Authorship Reporting Rule

| Field | Detail |
|:--|:--|
| Requirement Source | GAP-005 |
| Implementation Detail | Add a rule in `SKILL.md` requiring Codex to distinguish among: Claude produced content only, Claude successfully wrote the artifact, Codex wrote the artifact from Claude output, and consultant-authored substitute artifact. Include at least one short example statement for each case. |
| Expected Format | Markdown bullets with short examples |
| Acceptance Criteria | The skill explicitly forbids ambiguous success claims and provides provenance-aware reporting language. |
| Status | `open` |

---

### SPEC-007 - Add Trust-Prompt / Blocked-State Handling Guidance

| Field | Detail |
|:--|:--|
| Requirement Source | GAP-003, GAP-004 |
| Implementation Detail | Extend `.agents/skills/claude-code/references/claude-code-cli.md` with blocked-state guidance for workspace trust prompts, write-permission prompts, and unresolved session branches. The guidance must describe when to wait, when to surface user action as required, and when to stop rather than retry. |
| Expected Format | Short troubleshooting subsection in the CLI reference |
| Acceptance Criteria | The reference includes blocked-state handling rules that align with the new `SKILL.md` ownership and fallback posture. |
| Status | `open` |

### BATCH 3: Validation, Testing, And Gate Evidence

---

### SPEC-008 - Extend Manual Matrix For Reliability Incidents

| Field | Detail |
|:--|:--|
| Requirement Source | GAP-006 |
| Implementation Detail | Add manual Codex-mediated matrix scenarios to `.agents/skills/claude-code/references/claude-code-testing.md` for: duplicate-launch prevention, still-live process handoff, slow-run patience, trust-prompt blocking, and authorship/provenance reporting. Each scenario must state the expected non-destructive behavior and the expected user-facing summary. |
| Expected Format | New rows in the Manual Codex Matrix |
| Acceptance Criteria | The testing guide includes explicit scenarios covering client-cost containment and process ownership. |
| Status | `open` |

---

### SPEC-009 - Extend Static Validation For New Reliability Sections

| Field | Detail |
|:--|:--|
| Requirement Source | SPEC-001 through SPEC-007 |
| Implementation Detail | Update `.agents/skills/claude-code/scripts/validate_claude_code_skill.py` to verify the presence of the new execution-ownership, fallback/provenance, and blocked-state guidance sections or anchors. Keep live validation expectations conservative: the validator may confirm static presence and smoke surfaces, but it must not claim to prove duplicate-process cleanup automatically. |
| Expected Format | Python static-check additions plus any needed messaging changes |
| Acceptance Criteria | Static checks fail when the new reliability guidance is absent and pass when present; the validator does not overclaim automation coverage. |
| Status | `open` |

## IV. IMPLEMENTATION SEQUENCE

1. **Batch 1** (SPEC-001 through SPEC-004): Add execution ownership, patience, no-fallback, and cleanup rules to `SKILL.md`.
2. **Batch 2** (SPEC-005 through SPEC-007): Add direct-authoring reliability, provenance, and blocked-state guidance to `SKILL.md` and the CLI reference.
3. **Batch 3** (SPEC-008 through SPEC-009): Extend the manual testing matrix and validator coverage for the new runtime controls.
4. Run the validator after each batch and package explicit notes about what remains manual-only evidence for `GATE-003`.

## V. REFERENCES

| Document | Path |
|:--|:--|
| Governing Plan | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000/plan_T103-PH000-ST000-AC000.md` |
| Incident Hardening Assessment | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000/analysis/analysis_T103-PH000-ST000-AC000_claude-code-execution-reliability-hardening-assessment.md` |
| Original Remediation Specification | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000/implementation_T103-PH000-ST000-AC000_claude-code-skill-remediation.md` |
| Subject Skill | `.agents/skills/claude-code/SKILL.md` |
| CLI Reference | `.agents/skills/claude-code/references/claude-code-cli.md` |
| Testing Guide | `.agents/skills/claude-code/references/claude-code-testing.md` |
| Validator Script | `.agents/skills/claude-code/scripts/validate_claude_code_skill.py` |

## VI. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-03-23 | Initial | Post-`GATE-002` task specification for Claude Code execution-reliability hardening. Defines execution ownership, patience, fallback gating, cleanup, provenance, and validation expectations for the downstream hardening package. |
