---
artifact_type: 'ANALYSIS'
analysis_type: 'assessment'
initiative_id: 'P'
initiative_code: 'PROGRAM'
phase: '0'
stream_id: 'P-PH000-ST002'
activity_id: 'P-PH000-ST002-AC006'
task_id: 'P-PH000-ST002-AC006-TK001'
version: '1.0.0'
date: '2026-03-28'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/plan_P-PH000-ST002-AC006.md'
purpose: 'Three-domain gap audit of the current session-close skill, snotes closeout guidance, and client-facing briefing surface against the expanded AC006 boundary.'
---

# ANALYSIS: Session-Close Skill And Briefing Surface Gap Audit (`P-PH000-ST002-AC006`)

## I. EXECUTIVE SUMMARY

**Purpose**: Audit the current state of the session-close skill, snotes closeout guidance, and client-facing status review surfaces to establish the exact gap between the existing AC004 V1 baseline and the expanded AC006 boundary.
**Scope**: Three audit domains — (a) session-close skill operational gaps, (b) snotes closeout guidance gaps, (c) client-facing briefing surface gap. Includes authority-source mapping and lower-intelligence assistant support matrix.
**Conclusion / Recommendation**: Significant gaps exist in all three domains. The session-close skill is not operationally reachable (no symlinks), lacks lower-intelligence assistant scaffolding, and does not reference the snotes guideline. The snotes guidance surface exists in `guideline_workspace_notes.md` but is not referenced by any skill or reminder. The client-facing briefing surface does not exist at all — `status_program.md` serves as a system-of-record, not a decision surface. All three domains require distinct downstream work: skill rewrite (session-close), guideline integration (snotes), and a new artifact type (briefing dashboard).

### Client Summary

- The `session-close` skill file exists at `prompt/skills/session-close/SKILL.md` but **cannot be invoked or tested** because it has no symlinks to `.agents/skills/` or `.claude/skills/`.
- The skill contains only 5 closeout checks and 4 non-goals — it is a minimal V1 reminder surface with no guidance for snotes authoring, lower-intelligence assistant scaffolding, or session handoff pack creation.
- The `guideline_workspace_notes.md` guideline is comprehensive (273 lines, 8 sections, full template inventory) but **no skill or reminder surface references it**. Assistants would need to independently discover and read it.
- The `status_program.md` file contains **84 activity entries, a full health table (all unassessed), and the operational update protocol** — it is designed as a consultant system-of-record, not a client-facing session-continuity surface.
- A **separate briefing surface** is needed that filters to only `in_progress` and recently-changed activities with their latest session handoff packs.
- A gap exists in `guideline_workspace_proposal.md` regarding multi-feature gate proposal governance — captured as an open question for future governance work.

---

## II. SCOPE & INPUTS

**In scope**:
- Domain A: Session-close skill operational gaps (reachability, content completeness, authority references, lower-intelligence assistant support)
- Domain B: Snotes closeout guidance gaps (guideline coverage, skill integration, template reachability)
- Domain C: Client-facing briefing surface gap (existence, filtering requirements, placement options, relationship to status hierarchy)
- Authority-source mapping across all three domains
- Lower-intelligence assistant support matrix
- Multi-feature proposal governance gap identification

**Out of scope**:
- Direct edits to `prompt/skills/session-close/SKILL.md`
- Creating the briefing dashboard artifact
- Amending `guideline_workspace_proposal.md`
- Reopening or modifying AC004 decisions
- Any change to AC004's accepted V1 scope

**Inputs reviewed (repo-relative paths)**:
- `prompt/skills/session-close/SKILL.md`
- `prompt/skills/wrap-up/SKILL.md` (historical context only)
- `prompt/templates/consultant/workspace/guideline_workspace_notes.md`
- `prompt/artifacts/tasks/P/status/status_program.md`
- `prompt/artifacts/tasks/P/status/status_program.yaml`
- `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/proposal/proposal_P-PH000-ST002-AC004-TK003.8_session-close-standards-input.md`
- `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/analysis/analysis_P-PH000-ST002-AC006_readiness-and-gate-001-package-boundary-assessment.md`
- `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/plan_P-PH000-ST002-AC006.md`
- `.agents/skills/` directory listing
- `.claude/skills/` directory listing

**Assumed vs verified**:
- Verified: `session-close` skill file exists at `prompt/skills/session-close/SKILL.md`.
- Verified: `session-close` is NOT symlinked to `.agents/skills/` or `.claude/skills/` (confirmed via directory listing).
- Verified: `wrap-up` IS symlinked to both `.agents/skills/wrap-up` and `.claude/skills/wrap-up`.
- Verified: `status_program.md` contains 84 entries with all health dimensions `unassessed`.
- Verified: `guideline_workspace_notes.md` contains comprehensive authoring rules (273 lines, 8 sections, full template inventory).
- Verified: AC004 standards-input proposal (CONV-001 through CONV-006) defines the approved session-close convention.

---

## III. EVIDENCE / METHODOLOGY

**Method**:
- Read the session-close skill file and compared its content against the AC004 standards-input convention set.
- Listed the `.agents/skills/` and `.claude/skills/` directories to confirm symlink presence/absence.
- Read `guideline_workspace_notes.md` to assess whether it provides sufficient guidance for session-close-triggered snotes authoring.
- Read `status_program.md` (Sections 1, 2, 7) and `status_program.yaml` (top-level + sample entries) to assess client-facing usability.
- Compared the `wrap-up` skill's operational reachability (symlinked to both locations) against `session-close`.

**Commands run (if any)**:
```bash
ls -la .agents/skills/
ls -la .claude/skills/
ls -la prompt/skills/
```

**Evidence notes**:
- `.agents/skills/` contains a `wrap-up` symlink → `../../prompt/skills/wrap-up` but no `session-close` entry.
- `.claude/skills/` contains a `wrap-up` symlink → `../../prompt/skills/wrap-up` but no `session-close` entry.
- `prompt/skills/session-close/` directory exists with `SKILL.md` inside.
- The session-close skill's entire operational content is 5 closeout checks and 4 non-goals — approximately 24 lines of body content.
- `guideline_workspace_notes.md` defines 6 artifact types, 4 data schemas, 6 lifecycle rules, and 7 templates — none of which are referenced or summarized in the session-close skill.
- `status_program.md` Section 2 alone contains 84 rows. Section 3 (Health) contains another 84 rows, all `unassessed`. Section 7 (Operational Update Protocol) is a 50-line governance protocol. Total file size exceeds the 10,000 token read limit.

---

## IV. FINDINGS / GAP REGISTER

> This is a lightweight tracking register (not gate verification findings).

| GAP ID | Category | Title | Description | Disposition | Downstream Target | Notes |
|:--|:--|:--|:--|:--|:--|:--|
| GAP-001 | workflow | Session-close skill not operationally reachable | The skill file exists at `prompt/skills/session-close/SKILL.md` but has no symlinks to `.agents/skills/` or `.claude/skills/`. Unlike `wrap-up` (which is symlinked to both), `session-close` cannot be invoked or tested through normal skill resolution. | `deferred_to_TK007` | `P-PH000-ST002-AC006-TK007` | Symlink creation is an implementation task, not a planning task. The TK004 implementation spec must specify both symlinks explicitly. |
| GAP-002 | structure | Session-close skill lacks snotes guidance | The current skill contains 5 closeout checks focused on status-surface reconciliation. It provides no guidance on: creating `snotes_` session notes files, following `guideline_workspace_notes.md` section structure, populating DP/DEC/ACT/OQ tables, or writing the session handoff pack. | `deferred_to_TK004` | `P-PH000-ST002-AC006-TK004` | The implementation spec must specify snotes guidance as a required section of the hardened skill. |
| GAP-003 | references | Session-close skill does not reference notes guideline | The skill references `status_program.md` Section 7 and `wrap-up/SKILL.md` as context, but it does not reference `guideline_workspace_notes.md` — the authoritative source for snotes authoring rules, template inventory, and session file structure. | `deferred_to_TK004` | `P-PH000-ST002-AC006-TK004` | The hardened skill must reference the notes guideline explicitly. |
| GAP-004 | workflow | Session-close skill lacks lower-intelligence assistant scaffolding | The current skill assumes the executing assistant understands what "reconcile status surfaces" means and can independently navigate the status hierarchy. There is no step-by-step checklist, no explicit list of surfaces to check, and no conditional logic for "if you changed X, then also update Y". | `deferred_to_TK004` | `P-PH000-ST002-AC006-TK004` | The hardened skill must include explicit surface-check checklists and conditional reconciliation logic suitable for lower-intelligence assistants. |
| GAP-005 | references | Session-close skill authority chain is implicit | The skill does not explicitly state its authority source. Per AC004 CONV-001, the active gate-time authority is the AC004 standards-input proposal, not the live skill file. The skill should reference its authority chain so future editors know where the governing convention lives. | `deferred_to_TK004` | `P-PH000-ST002-AC006-TK004` | The hardened skill should include an authority-chain preamble. |
| GAP-006 | lifecycle | No client-facing briefing surface exists | `status_program.md` is a comprehensive system-of-record (84 entries, full health table, operational protocol). It is not designed for client-facing session-continuity use. The client needs a filtered view showing only `in_progress` and recently-changed activities with their latest session handoff packs. | `deferred_to_TK002` | `P-PH000-ST002-AC006-TK002` | This is the primary motivation for the briefing dashboard feature. TK002 comparative analysis will evaluate placement options. |
| GAP-007 | workflow | No mechanism to surface latest session handoff packs | The stream notes registers index sessions, but there is no surface that collects the most recent handoff pack per active activity into a single readable view. The client must manually navigate from `status_program.md` → stream plan → activity plan → notes register → session file → Section G handoff pack. | `deferred_to_TK005` | `P-PH000-ST002-AC006-TK005` | The briefing dashboard implementation spec should define how handoff pack pointers are surfaced. |
| GAP-008 | structure | Status program file exceeds usable read size | `status_program.md` exceeds 10,000 tokens. Even tooling cannot read it in a single pass. This is a structural indicator that the file serves too many audiences (system-of-record + client-facing + operational protocol). | `deferred_to_TK002` | `P-PH000-ST002-AC006-TK002` | Supports the case for a separate briefing surface rather than adding more sections to `status_program.md`. |
| GAP-009 | workflow | No cross-scope prioritization view | The status ledger contains entries across P, T102, and T104 but provides no mechanism for cross-initiative prioritization or dependency highlighting at the program level. The client identified this as a prerequisite for program-level planning consultation. | `deferred_to_TK002` | `P-PH000-ST002-AC006-TK002` | The briefing dashboard comparative analysis should evaluate whether cross-scope filtering is feasible in V1.1 or should be deferred to T105. |
| GAP-010 | references | Guideline_workspace_proposal.md multi-feature gap | The current proposal guideline does not address when a gate package spans features with existing authority sources and features requiring new authority. The SES002 consultation resolved this ad hoc (one briefing-only proposal; session-close relies on AC004 authority), but the pattern should be encoded. | `accepted_as_is` | Future governance activity (T104 or P-level) | Captured as open question `P-PH000-ST002-AC006-SES002-OQ002`. Not AC006 scope to fix. |

---

## V. ASSESSMENT (READINESS / OPTIONS / TRADEOFFS)

### A. Current State Summary

**Domain A — Session-Close Skill:**
The current skill is a minimal V1 reminder surface created during AC004. It contains:
- 5 closeout checks (status change detection, reconciliation trigger, Section 7 protocol pointer, wrap-up historical context, manual-only posture)
- 4 non-goals (no wrap-up duplication, no hooks/scripts, no scope broadening, no general session management)
- No snotes guidance, no lower-intelligence assistant scaffolding, no authority-chain reference, no symlinks

The AC004 standards-input proposal (CONV-001 through CONV-006) defines the approved convention. The skill file is quarantined as "lineage only" per CONV-002 until TK004 operationalizes the approved convention.

**Domain B — Snotes Closeout Guidance:**
`guideline_workspace_notes.md` is comprehensive and well-structured:
- 6 artifact types (phase/stream/activity registers + phase/stream/activity session notes)
- 4 data schemas (DP, DEC, ACT, OQ tables)
- 6 lifecycle rules (JIT registration, plan amendment sessions, authority/corrective sessions)
- 7 templates (3 register + 3 session + directory conventions)

However, this guideline is not integrated into any skill or reminder surface. An assistant would need to independently discover and read it. The session-close skill does not mention it. The gap is not in the guideline's content but in its discoverability and integration.

**Domain C — Client-Facing Briefing Surface:**
No briefing surface exists. The client's current workflow requires reading `status_program.md` (500+ lines, 84 entries, all health dimensions unassessed) to understand what work is active. The client identified three specific needs:
1. **Session continuity**: "What did I work on last and where do I pick up?"
2. **Active work overview**: "What is `in_progress` right now across all initiatives?"
3. **Program-level planning input**: "What are the cross-scope dependencies and priorities?"

Need (1) maps to handoff pack surfacing. Need (2) maps to status filtering. Need (3) maps to dependency/priority highlighting and may extend beyond V1.1 scope.

### B. Authority-Source Mapping

| Surface | Authoritative Source | Relationship to Session-Close |
|:--|:--|:--|
| Session-close behavior | AC004 standards-input proposal (CONV-001–006) | Defines what the skill should do |
| Status reconciliation protocol | `status_program.md` Section 7 | Defines when and how status updates happen |
| Snotes authoring rules | `guideline_workspace_notes.md` | Defines how session notes are structured |
| Snotes templates | 7 templates listed in notes guideline §7 | Defines exact file structure |
| Status ledger | `status_program.yaml` | Canonical data source for any derived view |
| Status narrative | `status_program.md` (Sections 1–6) | Derived from ledger; current client reading surface |

### C. Lower-Intelligence Assistant Support Matrix

| Capability | Current Support | Required Support | Gap Severity |
|:--|:--|:--|:--|
| Invoke session-close skill | Not possible (no symlinks) | Must be invocable via normal skill resolution | **Critical** |
| Understand which surfaces to check | Implicit ("status surfaces") | Explicit checklist: ledger, narrative, stream plan, phase plan, roadmap | **High** |
| Know when to reconcile | Implicit ("if touched") | Explicit conditional: "if you changed any of [list], then [action]" | **High** |
| Create snotes file | Not guided | Step-by-step: template selection → frontmatter → sections A–H | **High** |
| Write session handoff pack | Not guided | Explicit structure with carry-forward items from ACT/OQ tables | **Medium** |
| Update notes register | Not guided | Explicit: which register, which table, what row to add | **Medium** |
| Authority chain awareness | Not documented in skill | Preamble stating: convention source → protocol source → guideline source | **Low** |

### D. Recommendation

1. **Session-close skill (TK004)**: The implementation spec must transform the 24-line reminder into a comprehensive prompt-assist skill with: authority-chain preamble, explicit surface-check checklist, conditional reconciliation logic, snotes authoring step-by-step, template references, and lower-intelligence assistant scaffolding. The skill-creator and writing-skills superpowers skill should be used for the rewrite.

2. **Briefing dashboard (TK002/TK003/TK005)**: A separate artifact is needed. The comparative analysis should evaluate at minimum: (a) separate file (`briefing_program.md`) in `status/`, (b) new section in `status_program.md`, (c) skill-generated output. The recommendation leans toward option (a) based on the structural finding that `status_program.md` already exceeds usable read size.

3. **Cross-scope prioritization (GAP-009)**: This is a legitimate need but may be beyond V1.1 scope. The TK002 comparative analysis should evaluate whether a minimal cross-scope filter is feasible or should be deferred to T105.

---

## VIII. DOWNSTREAM ACTIONS

| downstream_artifact_type | target_reference | trigger_condition | responsible_role | notes |
|:--|:--|:--|:--|:--|
| `analysis` | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/analysis/analysis_P-PH000-ST002-AC006_briefing-dashboard-comparative-assessment.md` | After TK001 completes | `LLM_Consultant` | TK002: Comparative analysis evaluating briefing dashboard placement, filtering, and derivation options. Uses GAP-006, GAP-007, GAP-008, GAP-009 as inputs. |
| `proposal` | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/proposal/proposal_P-PH000-ST002-AC006_briefing-dashboard-standards-input.md` | After TK002 completes | `LLM_Consultant` | TK003: Standards-input proposal for briefing dashboard conventions. |
| `implementation` | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/implementation/implementation_P-PH000-ST002-AC006_session-close-hardening-task-specification.md` | After TK001 completes | `LLM_Consultant` | TK004: Implementation spec for session-close skill rewrite. Uses GAP-001 through GAP-005 as inputs, with AC004 standards-input as authority. |
| `implementation` | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/implementation/implementation_P-PH000-ST002-AC006_briefing-dashboard-task-specification.md` | After TK003 completes | `LLM_Consultant` | TK005: Implementation spec for briefing dashboard creation. Uses GAP-006 through GAP-009 as inputs. |

---

## IX. REFERENCES / LINKS REGISTER

| Item | Reference |
|:--|:--|
| Plan | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/plan_P-PH000-ST002-AC006.md` |
| Decisions | AC004 standards-input: `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/proposal/proposal_P-PH000-ST002-AC004-TK003.8_session-close-standards-input.md` |
| Primary inputs | `prompt/skills/session-close/SKILL.md`; `prompt/templates/consultant/workspace/guideline_workspace_notes.md`; `prompt/artifacts/tasks/P/status/status_program.md`; `prompt/artifacts/tasks/P/status/status_program.yaml` |
| Readiness assessment | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/analysis/analysis_P-PH000-ST002-AC006_readiness-and-gate-001-package-boundary-assessment.md` |

---

## X. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-03-28 | Initial | Three-domain gap audit covering session-close skill operational gaps (GAP-001 through GAP-005), snotes closeout guidance integration gaps (GAP-002, GAP-003), client-facing briefing surface gap (GAP-006 through GAP-009), and the multi-feature proposal governance gap (GAP-010). Includes authority-source mapping and lower-intelligence assistant support matrix. |
