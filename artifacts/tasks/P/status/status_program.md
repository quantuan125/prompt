---
artifact_type: 'STATUS'
initiative_id: 'P'
schema_version: '1.0'
version: '<semver>'
date: '<YYYY-MM-DD>'
status: 'draft'
author: '<role>'
decision_owner_role: 'Client'
ledger_reference: 'prompt/artifacts/tasks/P/status/status_program.yaml'
---

# Program Status Narrative — P (PROGRAM)

> **Authority hierarchy**: The ledger (`status_program.yaml`) is authoritative. This narrative is derived. Any drift → correct the narrative.

---

## 1. Summary

<!-- DERIVED FROM LEDGER -->

_Populate from ledger top-level fields (`program_id`, `as_of`, `updated_by`) and a count/roll-up of entry statuses._

| Field | Value |
|:--|:--|
| Program | P |
| As Of | — |
| Updated By | — |
| Total Entries | — |
| Status Distribution | — |

---

## 2. Status

<!-- DERIVED FROM LEDGER -->

_Populate from `entries[].scope_uid`, `entries[].name`, `entries[].status`, `entries[].as_of`._

| Scope UID | Name | Status | As Of |
|:--|:--|:--|:--|
| — | — | — | — |

---

## 3. Health

<!-- DERIVED FROM LEDGER -->

_Populate from `entries[].health.overall` and `entries[].health.dimensions`._

| Scope UID | Overall | Time | Cost | Scope | Quality | Risk | Benefits |
|:--|:--|:--|:--|:--|:--|:--|:--|
| — | — | — | — | — | — | — | — |

---

## 4. Dependencies

<!-- DERIVED FROM LEDGER -->

_Populate from `entries[].dependencies[]` (CLAUSE-027). Surface open/critical and at-risk edges with resolution owners._

| From | To | Relationship | Criticality | Status | Owner |
|:--|:--|:--|:--|:--|:--|
| — | — | — | — | — | — |

---

## 5. Evidence

<!-- DERIVED FROM LEDGER -->

_Populate from `entries[].evidence[]` (CLAUSE-030). Show recent pointers for high-impact transitions._

| Scope UID | Type | Ref | Date | By | Summary |
|:--|:--|:--|:--|:--|:--|
| — | — | — | — | — | — |

---

## 6. Next Actions

<!-- DERIVED FROM LEDGER -->

_Populate from upcoming work items, readiness gates, and blockers surfaced in the ledger entries._

| Scope UID | Action | Owner | Target Date | Notes |
|:--|:--|:--|:--|:--|
| — | — | — | — | — |

---

## 7. Operational Update Protocol

_This section is NOT derived from the ledger. It is the governing protocol for maintaining this artifact set. All roles MUST follow it._

### 7.1 Agent-Role Binding Table

| P-STD-002 RACI Label | Workspace Agent Role | Typical Responsibilities |
|:--|:--|:--|
| Responsible | LLM_Developer, LLM_Consultant, LLM_Reviewer (context-dependent) | Execute routine non-terminal transitions when guards satisfied; attribute updates with `updated_by` |
| Accountable | Client | Execute terminal transitions (→ `completed`, → `cancelled`) and reopen transitions; resolve disputes |
| Consulted | LLM_Consultant | Advise on status assessments, health evaluations, dependency analysis |
| Informed | All roles | Receive stale-state notifications; review narrative summaries |

### 7.2 Update Trigger Points

Agents MUST update the ledger at each of the following trigger points:

1. **Activity status change** — any transition in the CLAUSE-005 status matrix.
2. **Gate closure** — GATE-### APPROVE/RECYCLE → update activity and dependent entry statuses.
3. **Blocker recorded or resolved** — transition to `blocked` or from `blocked` → `in_progress`.
4. **Deliberate pause or resume** — transition to `on_hold` or from `on_hold` → `ready`.
5. **Explicit deferral or reactivation** — transition to `deferred` or from `deferred` → `ready`; record target scope/cycle and next review date.
6. **Health reassessment trigger** — per CLAUSE-017: upon transition to `ready`/`in_progress`, upon entering `blocked`/`on_hold`/`deferred`, and at terminal transitions.
7. **Stale-state review cycle** — per CLAUSE-038: at least every 7 calendar days; `deferred` items re-evaluated within 30 days.

### 7.3 Terminal / Reopen Execution Rule

- The Accountable role (Client) executes terminal transitions (→ `completed`, → `cancelled`) and reopen transitions directly, or explicitly authorizes a named delegate to perform the update.
- Any delegated terminal/reopen update MUST record authorization evidence using the ledger evidence schema (`type`, `ref`, `date`, `by`, `summary`) so the approval trail is auditable per CLAUSEs 008, 030, 032, and 039.

### 7.4 Conflict Resolution Rule

- When conflicting updates occur, the most recent update remains authoritative until reviewed.
- Any dispute over the correct status MUST be escalated to the Client as Accountable role, and the resolution decision MUST be recorded as evidence (per CLAUSE-037).

### 7.5 Update Sequence

Perform ledger and narrative updates in this order (per CLAUSE-048):

1. Validate evidence (plan + notes + changed artifacts).
2. Update ledger entry (canonical source of truth).
3. Derive/update narrative sections 1–6 from ledger (derived surface).
4. Record `updated_by` and `last_updated` on the modified ledger entry.

---

## 8. Changelog

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v0.1.0 | <YYYY-MM-DD> | Initial | Structural skeleton authored per P-PH000-ST002-AC002-TK003. All sections present; sections 1–6 are placeholder-only pending AC003 population. Operational Update Protocol (§7) embedded verbatim from SPEC-002 (GIR-001(a)). |
