---
artifact_type: 'ANALYSIS'
analysis_type: 'assessment'
initiative_id: 'T103'
initiative_code: 'ADRSS'
phase: '0'
stream_id: 'T103-PH000-ST000'
activity_id: 'T103-PH000-ST000-AC000'
version: '1.0.0'
date: '2026-03-22'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T103/workspace/plan/plan_T103-PH000.md'
purpose: 'Assessment of .agents/skills/claude-code/ skill for functional gaps, risks, and completeness against the proven .claude/skills/codex/ skill pattern'
assessment_scope: 'Cross-platform CLI skill parity and safety posture'
---

# ANALYSIS: Claude Code Skill Assessment (T103-PH000-ST000-AC000)

## I. EXECUTIVE SUMMARY

**Purpose**: Assess the Claude Code skill (`.agents/skills/claude-code/`) for functional completeness, safety posture, and behavioral parity against the battle-tested Codex skill (`.claude/skills/codex/`).

**Scope**: Full artifact set — SKILL.md, CLI reference, testing guide, validator script, and OpenAI metadata.

**Conclusion / Recommendation**: The skill is structurally sound and technically accurate. Command patterns, model/effort/permission mappings, and shell-neutral design all align with Claude Code CLI behavior. However, 12 gaps were identified across three severity tiers. A 4-batch remediation plan is recommended, prioritized by impact: behavioral parity first, safety second, then polish and validation hardening.

---

## II. SCOPE & INPUTS

**In scope**:
- `.agents/skills/claude-code/SKILL.md` (main skill definition)
- `.agents/skills/claude-code/references/claude-code-cli.md` (CLI flag reference)
- `.agents/skills/claude-code/references/claude-code-testing.md` (testing guide + manual matrix)
- `.agents/skills/claude-code/scripts/validate_claude_code_skill.py` (automated validator)
- `.agents/skills/claude-code/agents/openai.yaml` (Codex metadata)
- `.claude/skills/codex/SKILL.md` (reference skill for parity comparison)
- Claude Code CLI known behavior and sub-agent spawning patterns

**Out of scope**:
- T103 ADR-to-STD retargeting work (separate streams)
- Claude Code internal implementation or API behavior
- Codex CLI internal implementation
- Other `.agents/` or `.claude/` skills not named above

**Inputs reviewed (repo-relative paths)**:
- `.agents/skills/claude-code/SKILL.md`
- `.agents/skills/claude-code/references/claude-code-cli.md`
- `.agents/skills/claude-code/references/claude-code-testing.md`
- `.agents/skills/claude-code/scripts/validate_claude_code_skill.py`
- `.agents/skills/claude-code/agents/openai.yaml`
- `.claude/skills/codex/SKILL.md`

---

## III. EVIDENCE / METHODOLOGY

**Method**:
- Section-by-section comparison of Claude Code skill against Codex skill to identify structural and behavioral asymmetries
- Validation of command patterns against known Claude Code CLI flag surface (model aliases, effort levels, permission modes, output formats)
- Code review of `validate_claude_code_skill.py` for correctness and coverage gaps
- Assessment of safety posture for Codex-mediated invocations (resource caps, permission escalation, terminal handoff)
- Client-provided live Codex run transcript confirming basic print-mode flow works end-to-end

**Evidence notes**:
- Command templates in SKILL.md lines 61–94 match Claude Code CLI documentation for `claude`, `claude -p`, `claude -c`, `claude -r`, and structured output modes
- Model aliases (`sonnet`, `opus`, `opusplan`) and effort levels (`low`, `medium`, `high`, `max`) are correctly documented with appropriate constraints (max = Opus only)
- Permission modes (`plan`, `default`, `acceptEdits`, `dontAsk`, `bypassPermissions`) match CLI `--help` output per validator checks
- Validator script passes static and CLI surface checks (confirmed by testing guide documentation)
- Codex skill (`.claude/skills/codex/SKILL.md`) serves as the functional parity baseline — it has undergone multiple testing cycles and is confirmed working

---

## IV. FINDINGS / GAP REGISTER

> This is a lightweight tracking register (not gate verification findings).

| GAP ID | Category | Title | Description | Disposition | Downstream Target | Notes |
|:--|:--|:--|:--|:--|:--|:--|
| GAP-001 | workflow | Missing Critical Evaluation section | Codex skill (lines 39–61) teaches Claude to treat Codex as a colleague, push back on wrong claims, and frame disagreements as discussions. Claude Code skill has no symmetric guidance for Codex evaluating Claude's output. | `pending_decision` | Batch 1 / SPEC-001 | Tier 1 — functional gap |
| GAP-002 | workflow | No formalized follow-up loop | Codex skill uses `AskUserQuestion` at model selection, post-run confirmation, and resume decisions. Claude Code skill says "ask which model" but never specifies the mechanism. | `pending_decision` | Batch 1 / SPEC-002 | Tier 1 — functional gap |
| GAP-003 | workflow | No peer AI identification pattern | Codex skill has explicit template for Claude to identify itself when resuming a Codex session. Claude Code skill lacks a symmetric pattern for Codex identifying itself to Claude. | `pending_decision` | Batch 1 / SPEC-003 | Tier 1 — functional gap; client confirmed importance |
| GAP-004 | structure | Missing quick-reference table | Codex skill has a concise use-case → sandbox-mode → flags table (lines 26–32). Claude Code skill relies on prose and code blocks only. Tables are easier for models to route against. | `pending_decision` | Batch 3 / SPEC-007 | Tier 3 — usability |
| GAP-005 | workflow | Thin error handling | Codex skill has a dedicated Error Handling section with explicit rules (stop on non-zero, ask permission for dangerous flags, summarize warnings). Claude Code skill buries "report the failure" in a single guardrail bullet. | `pending_decision` | Batch 4 / SPEC-011 | Tier 1 — functional gap |
| GAP-006 | workflow | Interactive mode terminal handoff under-specified | Skill allows fresh interactive mode where Claude Code takes the terminal. No documentation of what happens to Codex's session, how Codex regains control, or whether interactive mode is feasible from Codex's sandbox. | `pending_decision` | Batch 2 / SPEC-005 | Tier 2 — risk area |
| GAP-007 | workflow | No default safety caps for print mode | Reference doc and testing guide use `--max-turns 1 --max-budget-usd 0.25` for smoke tests, but SKILL.md never recommends defaults for Codex-mediated print invocations. Runaway sessions are a resource risk. | `pending_decision` | Batch 2 / SPEC-004 | Tier 2 — risk area; client approved `--max-turns 5 --max-budget-usd 1.00` |
| GAP-008 | workflow | No working directory (`-C`) guidance | Codex skill includes `-C, --cd <DIR>` in command assembly. Claude Code skill and its reference doc do not address running Claude Code against a different directory. | `pending_decision` | Batch 2 / SPEC-006 | Tier 2 — risk area |
| GAP-009 | workflow | Session naming not recommended | Reference mentions `--name "<session-name>"` but workflow never suggests using it. For resume flows, named sessions are much more usable than opaque IDs. | `pending_decision` | Batch 3 / SPEC-008 | Tier 3 — polish |
| GAP-010 | workflow | `--append-system-prompt` not addressed | Powerful lever for Codex to pass context to Claude Code (e.g., peer AI context, task background). Not explored in skill workflow. | `pending_decision` | Batch 3 / SPEC-009 | Tier 3 — polish |
| GAP-011 | workflow | `--fork-session` not in workflow | Mentioned in reference but never surfaced in decision flow. Useful when Codex wants to branch a Claude session without losing the original. | `pending_decision` | Batch 3 / SPEC-010 | Tier 3 — polish |
| GAP-012 | consistency | Validator variable naming duplication | `validate_claude_code_skill.py` line 291: `shell_notes` is assigned `extract_section(skill_markdown, "Command Patterns")` — same section as `command_patterns` on line 290. Variable name is semantically misleading. Works because Shell Notes is a subsection of Command Patterns. | `pending_decision` | Batch 4 / SPEC-012 | Tier 3 — code quality |

---

## V. ASSESSMENT (READINESS / OPTIONS / TRADEOFFS)

### A. Current State Summary

- **Technical accuracy**: HIGH — command patterns, flag surfaces, and model/effort/permission mappings are correct
- **Testing infrastructure**: STRONG — validator script (687 lines) with static, CLI, and live smoke stages; manual Codex matrix with 17 scenarios and scoring rubric
- **Behavioral completeness**: MODERATE — core invocation flows work, but interaction patterns (follow-up, evaluation, error handling) are under-specified compared to the proven Codex skill
- **Safety posture**: MODERATE — permission mode guidance is solid, but missing resource caps and interactive mode documentation create risk
- **Shell coverage**: HIGH — explicit WSL, bash, cmd, and PowerShell handling with platform-specific notes

### B. Strengths (What's Working Well)

1. **Testing infrastructure** is significantly more rigorous than the Codex skill — automated validator, manual matrix with scoring rubric, release gate criteria
2. **Shell-neutral design** with explicit WSL, bash, cmd, PowerShell coverage and platform-specific quoting guidance
3. **Permission mode taxonomy** is well-mapped to Claude Code's actual modes with clear safety defaults
4. **Guardrail specificity** — the "sonnet + max" mismatch stop and "bypassPermissions" refusal are precise behavioral boundaries
5. **OpenAI metadata** correctly disables implicit invocation (`allow_implicit_invocation: false`)
6. **Reference architecture** — separating CLI reference from skill workflow from testing guide is clean and maintainable

### C. Options for Remediation

**Option A: Full 4-batch remediation (Recommended)**
- Closes all 12 gaps in priority order
- Maintains parity with Codex skill's interaction depth
- Adds safety caps and documentation for risk areas
- Estimated scope: SKILL.md (~80 lines added), CLI reference (~5 lines), testing guide (~10 lines), validator (~30 lines)
- Tradeoff: Larger change surface; requires batch-by-batch review

**Option B: Minimal remediation (Batches 1–2 only)**
- Closes the 8 highest-impact gaps (Tier 1 + Tier 2)
- Defers polish and validation hardening
- Tradeoff: Skill remains functional but less ergonomic; validator drift risk

**Option C: No change**
- Skill works for basic print-mode flows as demonstrated
- Tradeoff: Codex has no guidance for evaluating Claude's output, no follow-up protocol, no safety caps; risk of silent resource consumption

### D. Recommendation

**Option A (Full 4-batch remediation)** is recommended. The skill's testing infrastructure is already mature enough to validate the changes efficiently, and the Codex skill demonstrates that all 12 gaps are solvable patterns (not novel design work).

**Client decision**: Option A approved (DEC001).

---

## VIII. DOWNSTREAM ACTIONS

| downstream_artifact_type | target_reference | trigger_condition | responsible_role | notes |
|:--|:--|:--|:--|:--|
| IMPLEMENTATION (task_specification) | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000/implementation_T103-PH000-ST000-AC000_claude-code-skill-remediation.md` | This analysis completed | LLM_Consultant | 4-batch specification with SPEC items per gap |
| Skill update | `.agents/skills/claude-code/SKILL.md` | Batch 1–3 execution | LLM_Developer | Primary edit target |
| Reference update | `.agents/skills/claude-code/references/claude-code-cli.md` | Batch 2 execution (add `-C` flag) | LLM_Developer | Minor addition |
| Testing guide update | `.agents/skills/claude-code/references/claude-code-testing.md` | Batch 4 execution | LLM_Developer | New manual matrix scenarios |
| Validator update | `.agents/skills/claude-code/scripts/validate_claude_code_skill.py` | Batch 4 execution | LLM_Developer | Fix line 291; add new static checks |

---

## IX. REFERENCES / LINKS REGISTER

| Item | Reference |
|:--|:--|
| Plan | `prompt/artifacts/tasks/T103/workspace/plan/plan_T103-PH000.md` |
| Session notes | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000/snotes/snotes_T103-PH000-ST000-AC000-SES001.md` |
| Subject skill | `.agents/skills/claude-code/SKILL.md` |
| Reference skill (parity baseline) | `.claude/skills/codex/SKILL.md` |
| CLI reference | `.agents/skills/claude-code/references/claude-code-cli.md` |
| Testing guide | `.agents/skills/claude-code/references/claude-code-testing.md` |
| Validator script | `.agents/skills/claude-code/scripts/validate_claude_code_skill.py` |
| OpenAI metadata | `.agents/skills/claude-code/agents/openai.yaml` |

---

## X. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-03-22 | Initial | Assessment of Claude Code skill for cross-platform CLI invocation. 12 gaps identified across 3 tiers (5 functional, 3 risk, 4 polish). Option A (full 4-batch remediation) recommended and approved by client. |
