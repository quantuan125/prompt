---
artifact_type: 'PROPOSAL'
initiative_id: '[ID]'
initiative_code: '[CODE]'
phase: '[#]'
stream_id: '[SID-PH###-ST###]'
activity_id: '[SID-PH###-ST###-AC###]'
task_id: '[SID-PH###-ST###-AC###-TK###]'
gate_id: '[SID-PH###-ST###-AC###-GATE-###]'
version: '1.1.0'
date: 'YYYY-MM-DD'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: '[path to governing plan]'
analysis_reference: '[path to driving analysis]'
external_review_reference: '[path if used]'
purpose: 'Decision disposition package for gate closure'
consumers:
  - '[gate id]'
---

# PROPOSAL: Gate Disposition Package - [Gate/Scope]

## I. EXECUTIVE SUMMARY

- Context: [source analysis and decision surface]
- Goal at gate: [decision objective]
- Scope: [what is in/out]

---

## II. EVIDENCE INDEX

| Evidence Type | Artifact | Path | Notes |
|:--|:--|:--|:--|
| Analysis | [name] | `[analysis path]` | [why relevant] |
| Plan | [name] | `[plan path]` | [dependency/gate rules] |

---

## III. DISPOSITION SUMMARY REGISTER

Use `GIR-###` identifiers.

| GIR ID | Gap/Topic | Decision Area | Recommended Option | Execution Target | Blocking | Client Decision |
|:--|:--|:--|:--|:--|:--|:--|
| GIR-001 | [gap] | [area] | (a) [option] | [TK###] | Yes | (a) |

---

## IV. DETAILED DISPOSITION REGISTER

### GIR-001 - [Title]

Context:
- [current state]

Decision prompt:
- [explicit question]

| Option | Description |
|:--|:--|
| **(a) [Recommended]** | [description] |
| (b) [Alternative] | [description] |

Recommendation:
- (a)

Rationale:
- [concise rationale]

Client Decision:
- `[ ] (a)` / `[ ] (b)` / `[ ] Override: _______`

---

## V. GATE RECOMMENDATION

Reviewer recommendation state:
- `PASS` / `CONDITIONAL PASS` / `PASS WITH DEFERRALS` / `RECYCLE` / `FAIL`

Conditions and/or deferrals:
- [enumerate or use `-`]

Recycle reassessment path (`RECYCLE` only):
- `Same Gate Reassessed: [GATE-ID]`
- `Required Remediation Tasks: [TK### / TK###.n list]`
- `Downstream Tasks Still Blocked: [task list]`

Downstream enforcement:
- [what may start only after GDR closure]

---

## VI. GATE DECISION RECORD (GDR)

## Gate Decision Record

| Field | Value |
|:--|:--|
| Gate ID | `[gate_id]` |
| Reviewer Verdict | `[PASS / CONDITIONAL PASS / PASS WITH DEFERRALS / RECYCLE / FAIL]` |
| Client Decision | `[APPROVE / APPROVE WITH CONDITIONS / RECYCLE / REJECT / pending]` |
| Gate Status After Decision | `[completed / in_progress / failed / pending]` |
| Conditions (if any) | `[enumerated list or "-"]` |
| Decided By | `Client` |
| Decision Date | `YYYY-MM-DD` |
| Decision Reference | `[session notes path, inline statement, or pending]` |

If `Client Decision = RECYCLE`:
- `Gate Status After Decision` MUST be `in_progress`
- `Conditions (if any)` MUST enumerate the remediation tasks and re-entry basis
- downstream `Depends On: GATE-###` tasks remain blocked until the same gate later records an approving decision

---

## VII. REFERENCES

| Document | Path |
|:--|:--|
| Governing Plan | `[plan_reference]` |
| Input Analysis | `[analysis_reference]` |
| External Review (optional) | `[external_review_reference]` |

---

## VIII. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.1.0 | 2026-03-12 | Amendment | Added explicit recycle reassessment path guidance to the Gate Recommendation section and added `Gate Status After Decision` plus RECYCLE-specific notes to the GDR section. |
| v1.0.0 | YYYY-MM-DD | Initial | Initial template instantiation. |
