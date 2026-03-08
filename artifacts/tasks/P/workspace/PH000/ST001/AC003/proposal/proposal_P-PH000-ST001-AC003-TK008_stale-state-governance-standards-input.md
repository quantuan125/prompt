---
artifact_type: 'PROPOSAL'
initiative_id: 'P'
initiative_code: 'PROGRAM'
phase: '0'
stream_id: 'P-PH000-ST001'
activity_id: 'P-PH000-ST001-AC003'
task_id: 'P-PH000-ST001-AC003-TK008'
version: '1.0.0'
date: '2026-03-07'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/plan_P-PH000-ST001-AC003.md'
analysis_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/analysis/analysis_P-PH000-ST001-AC003-TK007_retention-policy-ownership-assessment.md'
external_review_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/analysis/analysis_P-PH000-ST001-AC003-GATE-001_external-review-industry-best-practices.md'
target_standards:
  - 'P-STD-002 — Program Status Standard'
purpose: 'Structured standards-input proposal to replace reserved P-STD-002-CLAUSE-038 with stale-state governance rules.'
---

# PROPOSAL: Standards Input - Stale-State Governance for P-STD-002 CLAUSE-038

## I. PURPOSE

- Proposal objective: define decision-ready stale-state governance conventions for replacing reserved `P-STD-002-CLAUSE-038`.
- Input scope: time-since-update thresholds, cadence-enforcement rules, and escalation behavior for stale status entries in active states.
- Target standards: `P-STD-002 — Program Status Standard`.

---

## II. CURRENT STATE SUMMARY

### A. Baseline

- `P-STD-002-CLAUSE-038` is currently reserved and contains no normative stale-state requirements.
- `P-STD-002-CLAUSE-017` already requires health reassessment on key transitions, but it does not govern what happens when no transition occurs for an extended period.
- The GATE-001 external review identified stale-state governance as `GAP-001` / `RISK-001` and recommended a tracked follow-on action rather than a gate blocker.
- TK007 recommends keeping evidence-retention duration outside `P-STD-002`; this proposal therefore focuses only on stale-state review and escalation, not evidence-retention ownership.

### B. Problems / Gaps

| Gap ID | Category | Description | Impact |
|:--|:--|:--|:--|
| GAP-001 | lifecycle | Active status entries can remain technically unchanged for too long because `CLAUSE-038` is still reserved. | Operational drift: a status can remain syntactically valid but no longer reflect current reality. |
| GAP-002 | workflow | `CLAUSE-017` only covers transition-triggered reassessment, so quiet-but-active work has no periodic freshness rule. | Teams can miss stalled work that never changes state. |
| GAP-003 | consistency | No escalation path exists when stale-state is detected. | Detection without a required response would create passive alerts rather than governed action. |

---

## III. PROPOSED CONVENTIONS

### A. Convention Set

| Convention ID | Rule | Rationale | Authority Link |
|:--|:--|:--|:--|
| CONV-001 | Stale-state governance applies to active non-terminal states: `ready`, `in_progress`, `blocked`, and `on_hold`. | These states represent live execution posture and therefore carry freshness risk when left unchanged. | `P-STD-002-CLAUSE-017`, `P-STD-002-CLAUSE-036`, `P-STD-002-CLAUSE-038` (target) |
| CONV-002 | Freshness is measured from `last_updated`, which already exists as a mandatory update-attribution field. | Reuses the existing protocol instead of adding a new timestamp surface. | `P-STD-002-CLAUSE-036` |
| CONV-003 | Recommended stale thresholds: `ready` = 7 days, `in_progress` = 7 days, `blocked` = 3 days, `on_hold` = 14 days. | This keeps the model simple, prioritizes blocker visibility, and stays conservative for an early governance version. | External patterns [1][2][3][4] plus P-RES-001 Topic 9 |
| CONV-004 | Stale detection SHOULD run on a fixed recurring cadence, at least weekly, and MAY run more frequently in automated environments. | Official platform patterns emphasize scheduled checks using cron or fixed-rate scheduling for age-based review [1][3]. | GitHub Actions schedule [1], Jira scheduled trigger [3] |
| CONV-005 | First stale detection requires notification to the Responsible and Accountable roles plus a request to refresh status, confirm exception, or record next action. | Industry stale workflows usually start with warning/notification before harder action [2][4]. | `P-STD-002-CLAUSE-034` to `P-STD-002-CLAUSE-037` |
| CONV-006 | If an item remains stale after the notification window, a formal review becomes mandatory and the Accountable role must decide whether to keep the state, move it, or document an exception. | Keeps state changes human-governed and avoids unsafe auto-transition behavior. | `P-STD-002-CLAUSE-035`, `P-STD-002-CLAUSE-037` |
| CONV-007 | Automatic state downgrade is NOT recommended for the baseline proposal; stale-state should trigger review, not force a transition. | `P-STD-002` already has guarded transitions and role restrictions; automatic downgrades would blur accountability. | `P-STD-002-CLAUSE-005`, `P-STD-002-CLAUSE-035` |
| CONV-008 | `planned`, `completed`, and `cancelled` are excluded from stale-state thresholds in the baseline proposal. | `planned` is planning backlog rather than active execution posture; terminal states do not need recurring freshness review. | Scope control for initial `CLAUSE-038` adoption |

### B. Compatibility Notes

- `CLAUSE-038` complements `CLAUSE-017`; it does not replace transition-triggered health reassessment.
- The proposed model uses existing `updated_by` / `last_updated` data and does not require a new artifact schema field for baseline adoption.
- Retention-policy ownership remains outside `P-STD-002` per TK007’s recommendation; stale-state review may require evidence or notes, but it does not set retention duration.

### C. Draft Replacement Text for `P-STD-002-CLAUSE-038`

```text
39) **P-STD-002-CLAUSE-038 (Stale-State Governance)**

   Status entries in active non-terminal states (`ready`, `in_progress`, `blocked`, `on_hold`) MUST be reviewed for staleness using the `last_updated` field.

   Minimum stale-state thresholds:
   - `ready`: 7 calendar days without update
   - `in_progress`: 7 calendar days without update
   - `blocked`: 3 calendar days without update
   - `on_hold`: 14 calendar days without update

   Stale-state review MUST run on a recurring schedule of at least once every 7 calendar days.

   When an entry is detected as stale:
   - the Responsible and Accountable roles MUST be notified;
   - the item MUST be reviewed and either refreshed, confirmed with an exception note, or transitioned to a more accurate state; and
   - if the stale condition remains unresolved through the next review interval, the Accountable role MUST record a resolution decision.

   Stale-state detection MUST NOT by itself force an automatic status transition in the baseline program implementation.

   This CLAUSE supplements transition-based health reassessment in `P-STD-002-CLAUSE-017`; it does not replace it.
```

---

## IV. DECISION REQUESTS

| Decision ID | Prompt | Options | Recommendation | Owner |
|:--|:--|:--|:--|:--|
| DEC-001 | What stale-threshold model should `CLAUSE-038` adopt? | (a) State-specific thresholds for `ready` / `in_progress` / `blocked` / `on_hold`; (b) one uniform threshold for all active states; (c) reserve trigger model only and defer numeric thresholds again | **(a)** | Client |
| DEC-002 | What should the escalation posture be when stale-state is detected? | (a) notification, then mandatory review, then accountable-role decision; (b) immediate accountable-role escalation with no warning stage; (c) automated state change after threshold breach | **(a)** | Client |
| DEC-003 | Should stale-state detection be allowed to auto-downgrade status in the baseline standard? | (a) no, keep transitions human-governed; (b) allow advisory suggested downgrade only; (c) allow automatic downgrade to `on_hold` or `blocked` | **(a)** | Client |

---

## V. IMPACT AND RISKS

### A. Impact Assessment

- Positive outcomes:
  - reduces the risk of operationally stale status entries by adding a recurring freshness rule;
  - reuses existing `last_updated` data and role-accountability model;
  - keeps the first version conservative by preferring review and escalation over automation-heavy state changes.
- Tradeoffs:
  - introduces recurring review overhead for active states;
  - may surface more “needs review” work than teams are currently used to handling;
  - threshold values will likely need tuning after observing real program cadence.

### B. Risks

| Risk ID | Description | Severity | Mitigation |
|:--|:--|:--|:--|
| RISK-001 | State-specific thresholds may still be too aggressive for some initiatives. | medium | Keep the proposal as standards input, not immediate amendment; allow later calibration by client decision. |
| RISK-002 | Teams may interpret stale detection as a hidden automatic transition rule. | medium | Draft text explicitly forbids automatic transition in the baseline proposal. |
| RISK-003 | Weekly scheduled reviews can fail silently if automation is misconfigured. | low | Require accountable-role review ownership and allow manual cadence checks where automation is unavailable [1][3]. |
| RISK-004 | `planned` items could be dragged into execution freshness policy unintentionally. | low | Baseline proposal excludes `planned` and keeps focus on active execution states only. |

---

## VI. REFERENCES

| Document | Path |
|:--|:--|
| Governing Plan | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/plan_P-PH000-ST001-AC003.md` |
| Supporting Analysis | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/analysis/analysis_P-PH000-ST001-AC003-TK007_retention-policy-ownership-assessment.md` |
| External Review | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/analysis/analysis_P-PH000-ST001-AC003-GATE-001_external-review-industry-best-practices.md` |
| Governing Standard | `prompt/artifacts/tasks/P/standard/standard_P-STD-002_program-status-standard.md` |
| Prior Research | `prompt/artifacts/tasks/P/research/P-RES-001/report_P-RES-001_status-standard-research.md` |

## Sources
- [1] GitHub Docs, Workflow syntax for GitHub Actions (`on.schedule`) — https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
- [2] GitHub `actions/stale` — https://github.com/actions/stale
- [3] Atlassian Support, Jira automation triggers — https://support.atlassian.com/cloud-automation/docs/jira-automation-triggers/
- [4] Atlassian Support, How to automatically send email notification to assignee if a ticket is not updated for a certain time — https://support.atlassian.com/jira/kb/how-to-automatically-send-email-notification-to-assignee-if-a-ticket-is-not-updated-for-a-certain-time/

---

## VII. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-03-07 | Initial | Initial TK008 standards-input proposal defining candidate stale-state thresholds, cadence, escalation path, and draft replacement text for `P-STD-002-CLAUSE-038`. |
