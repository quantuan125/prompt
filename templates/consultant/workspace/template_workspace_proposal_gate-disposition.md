---
artifact_type: 'PROPOSAL'
initiative_id: '[ID]'
initiative_code: '[CODE]'
phase: '[#]'
stream_id: '[SID-PH###-ST###]'
activity_id: '[SID-PH###-ST###-AC###]'
task_id: '[SID-PH###-ST###-AC###-TK###]'
gate_id: '[SID-PH###-ST###-AC###-GATE-###]'
version: '1.0.0'
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
| Conditions (if any) | `[enumerated list or "-"]` |
| Decided By | `Client` |
| Decision Date | `YYYY-MM-DD` |
| Decision Reference | `[session notes path, inline statement, or pending]` |

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
| v1.0.0 | YYYY-MM-DD | Initial | Initial template instantiation. |
