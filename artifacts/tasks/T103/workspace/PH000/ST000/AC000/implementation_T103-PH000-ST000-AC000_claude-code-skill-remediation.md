---
artifact_type: 'IMPLEMENTATION'
implementation_type: 'task_specification'
initiative_id: 'T103'
initiative_code: 'ADRSS'
phase: '0'
stream_id: 'T103-PH000-ST000'
activity_id: 'T103-PH000-ST000-AC000'
task_id: 'T103-PH000-ST000-AC000-TK003'
version: '1.1.0'
date: '2026-03-23'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000/plan_T103-PH000-ST000-AC000.md'
analysis_reference: 'prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000/analysis/analysis_T103-PH000-ST000-AC000_claude-code-skill-review.md'
session_reference: 'prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000/snotes/snotes_T103-PH000-ST000-AC000-SES001.md'
purpose: 'Task specification for 4-batch remediation of the Claude Code skill to close 12 identified gaps'
---

# IMPLEMENTATION (Task Specification): Claude Code Skill Remediation

## I. PURPOSE & AUTHORITY

- **Purpose**: Detailed implementation specification for remediating 12 identified gaps in the Claude Code skill (`.agents/skills/claude-code/`), organized into 4 sequentially ordered batches.
- **Authority chain**: Assessment analysis identifies gaps (GAP-001 through GAP-012) → Client approves remediation scope (SES001-DEC001) → This artifact specifies HOW → Dev-report records execution.
- **Seed analysis**: `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000/analysis/analysis_T103-PH000-ST000-AC000_claude-code-skill-review.md` is the direct assessment seed for this implementation artifact. The 4-batch remediation scope in this file is intentionally limited to the gap set identified there; later execution-reliability hardening is commissioned separately by the post-incident AC000 assessment.
- **Audience**: LLM_Developer (primary consumer for execution)
- This artifact does NOT hold a GDR. Gate decisions (if applicable) are recorded in gate_disposition proposals.

## II. TASK SCOPE

- **Governing analysis**: `analysis_T103-PH000-ST000-AC000_claude-code-skill-review.md`
- **Trigger**: Assessment identified 12 gaps (5 functional, 3 risk, 4 polish) against the proven Codex skill baseline
- **Deliverable contract**: Updated `.agents/skills/claude-code/SKILL.md`, minor updates to CLI reference, testing guide, and validator script
- **Key decisions**:
  - SES001-DEC001: 4-batch remediation approved
  - SES001-DEC002: Peer AI identification uses model name (symmetric with Codex skill)
  - SES001-DEC003: Default safety caps `--max-turns 5`, `--max-budget-usd 1.00`
  - SES001-DEC004: Safety caps appear directly in Quick Reference table
- **Commissioning clarifications**:
  - Validator coverage for this package includes all newly introduced sections: Critical Evaluation, Following Up, Error Handling, and Quick Reference.
  - Validator hardening for this package checks section existence and required content, not strict section ordering.
  - Interactive-mode live testing remains desirable but is not a Gate-001 readiness blocker; Batch 2 must still document terminal handoff behavior.

## III. SPECIFICATION ITEMS

### BATCH 1: Core Behavioral Parity (GAP-001, GAP-002, GAP-003)

---

### SPEC-001 — Add "Critical Evaluation of Claude Output" Section

| Field | Detail |
|:--|:--|
| Requirement Source | GAP-001; Codex skill lines 39–61 |
| Implementation Detail | Add a new section after "Output Handling" in SKILL.md. Mirror the Codex skill's structure: (1) Guidelines subsection — trust own knowledge when confident, research disagreements, remember knowledge cutoffs, don't defer blindly; (2) "When Claude is Wrong" subsection — state disagreement, provide evidence, optionally resume Claude session for peer discussion, frame as discussion not correction, let user decide. Adapt language from Claude-specific to Codex-specific perspective (i.e., Codex evaluating Claude's claims). |
| Expected Format | Markdown section with subsections matching Codex skill's "Critical Evaluation" pattern |
| Acceptance Criteria | Section exists in SKILL.md; covers trust-own-knowledge, research-disagreements, knowledge-cutoffs, and don't-defer-blindly guidelines; includes "When Claude is Wrong" procedure |
| Status | `open` |

---

### SPEC-002 — Add "Following Up" Section with AskUserQuestion Protocol

| Field | Detail |
|:--|:--|
| Requirement Source | GAP-002; Codex skill lines 34–37 |
| Implementation Detail | Add a new section after "Output Handling" (or after Critical Evaluation if SPEC-001 is placed there). Include: (1) "After every `claude` command, immediately use `AskUserQuestion` to confirm next steps, collect clarifications, or decide whether to continue/resume." (2) "When continuing or resuming, restate the chosen model, effort, and permission mode when proposing follow-up actions." (3) Update "Choose The Model" step to explicitly say "Ask the user (via `AskUserQuestion`) which model to run" instead of the current generic "ask which model to use." |
| Expected Format | Markdown section with bullet points |
| Acceptance Criteria | Section exists; `AskUserQuestion` is named as the mechanism; post-run follow-up and parameter restatement are documented |
| Status | `open` |

---

### SPEC-003 — Add Peer AI Identification Pattern

| Field | Detail |
|:--|:--|
| Requirement Source | GAP-003; SES001-DEC002; Codex skill lines 53–58 |
| Implementation Detail | Within the "When Claude is Wrong" subsection of Critical Evaluation (SPEC-001), add an explicit template for Codex identifying itself when sending a follow-up to Claude Code. Pattern: `claude -c -p --model <MODEL> --effort <EFFORT> --permission-mode plan "This is Codex (<your current model name>) following up. I disagree with [X] because [evidence]. What's your take on this?"`. Include note: "Identify yourself as Codex so Claude knows it's a peer AI discussion. Use your actual model name (e.g., the model you are currently running as)." |
| Expected Format | Code block with template + explanatory note, embedded within Critical Evaluation section |
| Acceptance Criteria | Template exists with model-name self-identification; uses `-c -p` for print-mode continuation; framed as peer discussion |
| Status | `open` |

---

### BATCH 2: Safety Defaults & Risk Mitigation (GAP-006, GAP-007, GAP-008)

---

### SPEC-004 — Add Default Safety Caps for Print Mode

| Field | Detail |
|:--|:--|
| Requirement Source | GAP-007; SES001-DEC003 |
| Implementation Detail | (1) In the "Command Patterns" section, update the print-mode templates to include `--max-turns 5 --max-budget-usd 1.00` as recommended defaults. Show them in the template but note they are overridable. (2) Add a brief note: "For Codex-mediated print-mode invocations, include `--max-turns 5 --max-budget-usd 1.00` by default to prevent runaway sessions. Override these values when the user explicitly requests a longer or more expensive run." |
| Expected Format | Updated code block templates + explanatory note |
| Acceptance Criteria | Print-mode command templates include `--max-turns` and `--max-budget-usd`; defaults are `5` and `1.00` respectively; documented as overridable |
| Status | `open` |

---

### SPEC-005 — Clarify Interactive Mode Terminal Handoff

| Field | Detail |
|:--|:--|
| Requirement Source | GAP-006 |
| Implementation Detail | In "Choose The Run Mode", add a note under the interactive mode bullet: "Interactive mode transfers terminal control from Codex to Claude Code. Codex cannot intervene or capture output during an interactive session. If uncertain whether the user needs an interactive session, default to print mode and inform the user they can run `claude` directly for interactive use." This is documentation, not a functional block. |
| Expected Format | Indented note or sub-bullet under the interactive mode entry |
| Acceptance Criteria | Interactive mode entry documents terminal handoff implications; recommends print-mode default when uncertain |
| Status | `open` |

---

### SPEC-006 — Add Working Directory (`-C`) Guidance

| Field | Detail |
|:--|:--|
| Requirement Source | GAP-008 |
| Implementation Detail | (1) In SKILL.md "Command Patterns" section, add a new template: `claude -p -C <DIR> --model <MODEL> --effort <EFFORT> --permission-mode <MODE> --max-turns 5 --max-budget-usd 1.00 "<PROMPT>"`. (2) In the workflow or a brief note: "If the task targets a different directory than the current working directory, use `-C <DIR>` to set Claude's working directory." (3) In `references/claude-code-cli.md`, add `-C, --cd <DIR>` to the "Extra Session Controls" section with description: "Set Claude's working directory." |
| Expected Format | New command template in SKILL.md; new entry in CLI reference |
| Acceptance Criteria | `-C <DIR>` pattern documented in both SKILL.md and CLI reference; usage guidance present |
| Status | `open` |

---

### BATCH 3: Usability & Polish (GAP-004, GAP-009, GAP-010, GAP-011)

---

### SPEC-007 — Add Quick Reference Table

| Field | Detail |
|:--|:--|
| Requirement Source | GAP-004; SES001-DEC004 |
| Implementation Detail | Add a "Quick Reference" table after the "Workflow" section and before the detailed decision sections. Table columns: Use case, Run mode, Key flags. Rows should cover: one-shot query, read-only analysis, edits needed, continue latest, resume named session, interactive takeover, different directory. Include default safety caps directly in the flag values per DEC004. |
| Expected Format | Markdown table matching the structure proposed in the consultation |
| Acceptance Criteria | Table exists with 7 rows covering all primary use cases; safety caps visible in relevant rows; table is self-contained (no "see section X" references for critical values) |
| Status | `open` |

Table content (from approved consultation):

| Use case | Run mode | Key flags |
|---|---|---|
| One-shot query | Print | `-p --max-turns 5 --max-budget-usd 1.00` |
| Read-only analysis | Print + plan | `-p --permission-mode plan --max-turns 5 --max-budget-usd 1.00` |
| Edits needed | Print + acceptEdits | `-p --permission-mode acceptEdits --max-turns 5 --max-budget-usd 1.00` |
| Continue latest | Continue-print | `-c -p` |
| Resume named session | Resume | `-r "<SESSION>"` |
| Interactive takeover | Fresh | (no `-p`; warn about terminal handoff) |
| Different directory | Any + `-C` | `-C <DIR>` plus other flags |

---

### SPEC-008 — Add Session Naming Recommendation

| Field | Detail |
|:--|:--|
| Requirement Source | GAP-009 |
| Implementation Detail | Add a brief note in the workflow or after the Command Patterns section: "When starting a session you expect to resume later, use `--name "<descriptive-name>"` to make it easier to reference with `-r`. Example: `claude --name 'architecture-review' --model opus ...`" |
| Expected Format | Bullet point or short subsection |
| Acceptance Criteria | `--name` usage is recommended for resumable sessions; example provided |
| Status | `open` |

---

### SPEC-009 — Surface `--append-system-prompt` for Context Passing

| Field | Detail |
|:--|:--|
| Requirement Source | GAP-010 |
| Implementation Detail | Add a brief note (1–2 sentences) in the workflow or as a tip: "To pass Codex-side context to Claude Code, use `--append-system-prompt '<text>'` to add background information to Claude's system prompt. Useful for providing task context, constraints, or peer AI identity." |
| Expected Format | Bullet point |
| Acceptance Criteria | `--append-system-prompt` is mentioned as an available context-passing mechanism |
| Status | `open` |

---

### SPEC-010 — Surface `--fork-session` for Session Branching

| Field | Detail |
|:--|:--|
| Requirement Source | GAP-011 |
| Implementation Detail | Add alongside the resume command patterns: "Use `--fork-session` when resuming to create a new branch of the conversation without modifying the original session." |
| Expected Format | Inline note near resume patterns |
| Acceptance Criteria | `--fork-session` is documented near resume patterns with a brief explanation of its purpose |
| Status | `open` |

---

### BATCH 4: Validation & Error Handling (GAP-005, GAP-012)

---

### SPEC-011 — Add Dedicated "Error Handling" Section

| Field | Detail |
|:--|:--|
| Requirement Source | GAP-005; Codex skill lines 62–65 |
| Implementation Detail | Add a new "Error Handling" section in SKILL.md (after Output Handling or after Following Up). Include: (1) "Stop and report failures whenever `claude --version` or a `claude` command exits non-zero; request direction before retrying." (2) "If `claude` is not found on PATH, report clearly and do not retry." (3) "When output includes warnings or partial results, summarize them and ask how to adjust using `AskUserQuestion`." (4) "If a command times out, report the timeout and suggest reducing scope or adding tighter `--max-turns`." |
| Expected Format | Markdown section with bullet points mirroring Codex skill's Error Handling structure |
| Acceptance Criteria | Dedicated section exists; covers non-zero exit, missing CLI, warnings/partial results, and timeouts |
| Status | `open` |

---

### SPEC-012 — Fix Validator Variable Naming and Add New Static Checks

| Field | Detail |
|:--|:--|
| Requirement Source | GAP-012; new sections from SPEC-001, SPEC-002, SPEC-007, SPEC-011 |
| Implementation Detail | (1) Fix line 291 in `validate_claude_code_skill.py`: rename `shell_notes` to correctly extract from the Shell Notes subsection or rename the variable to `command_patterns_and_shell_notes` to reflect what it actually extracts. (2) Add static checks for new sections: verify "Critical Evaluation" section exists, verify "Following Up" section exists, verify "Error Handling" section exists, verify Quick Reference table exists. (3) Add a check that `--max-turns` appears in at least one print-mode command template. |
| Expected Format | Python code changes in `validate_claude_code_skill.py` |
| Acceptance Criteria | Line 291 variable is correctly named or reassigned; new static checks pass when sections are present and fail when absent; `--max-turns` check passes; section-order validation is not required |
| Status | `open` |

---

### SPEC-013 — Add New Manual Test Matrix Scenarios

| Field | Detail |
|:--|:--|
| Requirement Source | SPEC-001, SPEC-004, SPEC-006 (new behaviors need test coverage) |
| Implementation Detail | Add to the "Manual Codex Matrix" in `references/claude-code-testing.md`: (1) **Peer AI disagreement**: Codex runs Claude, disagrees with the result, and resumes with self-identification. Expected: Codex uses the peer AI template and identifies itself by model name. (2) **Budget cap behavior**: Run a print-mode task and observe `--max-turns` / `--max-budget-usd` in the assembled command. Expected: defaults present unless user overrides. (3) **Different directory**: Use `-C <DIR>` to target Claude at a different directory. Expected: command includes `-C` and Claude operates in the specified directory. |
| Expected Format | New rows in the Manual Codex Matrix table |
| Acceptance Criteria | 3 new scenarios added; each has Codex prompt and expected behavior columns filled |
| Status | `open` |

## IV. IMPLEMENTATION SEQUENCE

Batches are sequentially ordered. Each batch should be reviewed before proceeding to the next.

1. **Batch 1** (SPEC-001, SPEC-002, SPEC-003): Core Behavioral Parity
   - Edit `.agents/skills/claude-code/SKILL.md` only
   - Adds ~40 lines (Critical Evaluation section, Following Up section, peer AI template)

2. **Batch 2** (SPEC-004, SPEC-005, SPEC-006): Safety Defaults & Risk Mitigation
   - Edit `.agents/skills/claude-code/SKILL.md` (primary)
   - Edit `.agents/skills/claude-code/references/claude-code-cli.md` (add `-C` entry)
   - Updates command templates and adds ~20 lines

3. **Batch 3** (SPEC-007, SPEC-008, SPEC-009, SPEC-010): Usability & Polish
   - Edit `.agents/skills/claude-code/SKILL.md` only
   - Adds Quick Reference table (~15 lines) and 3 brief notes (~5 lines each)

4. **Batch 4** (SPEC-011, SPEC-012, SPEC-013): Validation & Error Handling
   - Edit `.agents/skills/claude-code/SKILL.md` (Error Handling section)
   - Edit `.agents/skills/claude-code/scripts/validate_claude_code_skill.py` (fix + new checks)
   - Edit `.agents/skills/claude-code/references/claude-code-testing.md` (new matrix rows)

**Post-execution**: Run `python3 .agents/skills/claude-code/scripts/validate_claude_code_skill.py` after each batch to confirm no regressions. Run `--live-smoke` after Batch 4.

## V. REFERENCES

| Document | Path |
|:--|:--|
| Governing Plan | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000/plan_T103-PH000-ST000-AC000.md` |
| Assessment Analysis | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000/analysis/analysis_T103-PH000-ST000-AC000_claude-code-skill-review.md` |
| Session Notes | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000/snotes/snotes_T103-PH000-ST000-AC000-SES001.md` |
| Subject Skill | `.agents/skills/claude-code/SKILL.md` |
| Reference Skill (parity baseline) | `.claude/skills/codex/SKILL.md` |
| CLI Reference | `.agents/skills/claude-code/references/claude-code-cli.md` |
| Testing Guide | `.agents/skills/claude-code/references/claude-code-testing.md` |
| Validator Script | `.agents/skills/claude-code/scripts/validate_claude_code_skill.py` |

## VI. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.1.0 | 2026-03-23 | Amendment | Made the seed lineage explicit in-body: this implementation artifact is directly seeded from `analysis_T103-PH000-ST000-AC000_claude-code-skill-review.md`, and later execution-reliability hardening is intentionally scoped to a separate post-incident package. |
| v1.0.0 | 2026-03-22 | Initial | Task specification for 4-batch Claude Code skill remediation. 13 SPEC items across 4 batches (Core Behavioral Parity, Safety Defaults, Usability & Polish, Validation & Error Handling). Source: SES001-DEC001 through DEC004. |
