---
artifact_type: 'IMPLEMENTATION'
implementation_type: 'task_specification'
initiative_id: 'P'
initiative_code: 'PROGRAM'
phase: '0'
stream_id: 'P-PH000-ST002'
activity_id: 'P-PH000-ST002-AC002'
gate_id: 'P-PH000-ST002-AC002-GATE-002'
version: '1.0.0'
date: '2026-03-21'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST002/AC002/plan_P-PH000-ST002-AC002.md'
purpose: 'Unified developer-facing task specification for TK002 (ledger skeleton), TK003 (narrative template), and TK004 (conformance validation), distilling approved GATE-002 GIR decisions into concrete implementation instructions.'
---

# IMPLEMENTATION (Task Specification): Phase 1 Developer Spec — TK002 (Ledger Skeleton), TK003 (Narrative Template), TK004 (Conformance Validation) — P-PH000-ST002-AC002

## I. PURPOSE & AUTHORITY

- **Purpose**: Specify the exact implementation requirements for TK002 (Author Ledger Skeleton), TK003 (Author Narrative Template), and TK004 (Validate P-STD-002E Conformance). This unified specification distills the three approved GATE-002 GIR decisions (GIR-001, GIR-002, GIR-003) into concrete developer instructions for each task.
- **Authority chain**: The AC002 activity plan (`plan_P-PH000-ST002-AC002.md`) authorizes TK002–TK004 pending GATE-002 APPROVE → this artifact specifies HOW those tasks are executed → TK005 DEV-REPORT records execution evidence.
- **Audience**: LLM_Developer (primary executor of TK002, TK003, TK004)
- This artifact does NOT hold a GDR. The GATE-002 decision is recorded in `proposal_P-PH000-ST002-AC002-GATE-002_design-decision-disposition.md`.
- This specification is unified across TK002–TK004 because all three tasks share the same GIR design-decision boundary (GIR-001 through GIR-003 from GATE-002). Each task has a dedicated SPEC item below.

## II. TASK SCOPE

- **Governing plan tasks**: `P-PH000-ST002-AC002-TK002`, `P-PH000-ST002-AC002-TK003`, `P-PH000-ST002-AC002-TK004`
- **Trigger**: GATE-002 approved GIR-001(a) (agent-role binding), GIR-002(a) (P-STD-005 timeline UIDs + activity-only v1), and GIR-003(a) (optional field inclusion/exclusion). CONV-011 requires an IMPLEMENTATION artifact when task complexity exceeds plan-step capacity. This specification encodes all three GIR decisions as binding developer instructions.
- **Deliverable contract**:
  - TK002: `prompt/artifacts/tasks/P/status/status_program.yaml` — canonical YAML ledger skeleton
  - TK003: `prompt/artifacts/tasks/P/status/status_program.md` — derived Markdown narrative with embedded protocol
  - TK004: Conformance validation results — checklist evaluation with evidence

## III. SPECIFICATION ITEMS

### SPEC-001 — TK002: Author Ledger Skeleton

| Field | Detail |
|:--|:--|
| Requirement Source | AC002 plan TK002; GIR-001(a), GIR-002(a), GIR-003(a) approved at GATE-002; requirements analysis §V.C (Ledger Schema Specification) |
| Implementation Detail | See §III.A below |
| Expected Format | YAML file conformant to P-STD-002E CLAUSE-046 schema |
| Acceptance Criteria | File exists at correct path; YAML is valid; all MVAT fields present; 8-state enum; GIR-003(a) inclusion/exclusion applied; P-STD-004 placement satisfied |
| Status | `open` |

#### §III.A — Ledger Skeleton Implementation Detail

**Target file**: `prompt/artifacts/tasks/P/status/status_program.yaml`

**Directory creation**: Create directory `prompt/artifacts/tasks/P/status/` if it does not exist (GAP-006 resolution).

**Schema**: Use the concrete ledger schema from the implementation requirements analysis §V.C verbatim. The top-level structure MUST be:

```yaml
schema_version: "1.0"
program_id: "P"
as_of: "YYYY-MM-DD"
updated_by: "<actor>"
last_updated: "YYYY-MM-DD"

entries:
  - scope_uid: "<SID per P-STD-005>"
    scope_type: "<initiative|phase|stream|activity>"
    initiative_id: "<SID root>"
    name: "<human-readable name>"
    status: "<planned|ready|in_progress|blocked|on_hold|deferred|completed|cancelled>"
    as_of: "YYYY-MM-DD"
    updated_by: "<actor>"
    last_updated: "YYYY-MM-DD"
    health:
      overall: "<green|amber|red|unassessed>"
      dimensions:
        time: "<green|amber|red|unassessed>"
        cost: "<green|amber|red|unassessed>"
        scope: "<green|amber|red|unassessed>"
        quality: "<green|amber|red|unassessed>"
        risk: "<green|amber|red|unassessed>"
        benefits: "<green|amber|red|unassessed>"
    dependencies: []
    evidence: []
    aggregation_policy: ~
    execution_refs: []
    extensions: {}
```

**8-state enum** (GIR-001(a) + P-STD-002-CLAUSE-001): The `status` field MUST accept exactly these values: `planned`, `ready`, `in_progress`, `blocked`, `on_hold`, `deferred`, `completed`, `cancelled`.

**GIR-002(a) applied** (`scope_uid` naming):
- `scope_uid` values MUST use P-STD-005 timeline UID patterns (e.g., `P-PH000-ST001-AC003`)
- `scope_type` supports `initiative`, `phase`, `stream`, `activity` but AC003 v1 populates activity-level only
- Do NOT populate with real data in the skeleton; all value fields remain as placeholders

**GIR-003(a) applied** (optional field inclusion/exclusion):
- CLAUSE-024 (`schedule_relation`, `lag`) — **EXCLUDED** (no schedule data in plans)
- CLAUSE-028 (`platform`, `run_id`, etc.) — **EXCLUDED** (no CI/CD integration)
- CLAUSE-051 (`execution_refs[]`) — **INCLUDED** as empty array (low-cost audit alignment)
- CLAUSE-053 (`approval_policy`, `sandbox_mode`) — **EXCLUDED** (no execution posture metadata)

**MVAT fields** (per CLAUSE-054): Every entry MUST include:
- `status`
- `as_of`
- `updated_by`
- `last_updated`
- `evidence` (1+ pointers required for evidence-required transitions; empty array `[]` in skeleton)

**Extension hooks** (per CLAUSE-046):
- `extensions: {}` object present on every entry
- `x_` prefix convention reserved for custom extension fields

**Schema version** (per CLAUSE-050): Top-level `schema_version: "1.0"` required.

**Example skeleton entry**: Include 1 example entry using placeholder activity UID to demonstrate schema structure. All value fields remain as placeholders:

```yaml
  - scope_uid: "<P-PH000-ST001-AC003>"
    scope_type: "<activity>"
    initiative_id: "<P>"
    name: "<human-readable activity name>"
    status: "<planned|ready|in_progress|blocked|on_hold|deferred|completed|cancelled>"
    as_of: "<YYYY-MM-DD>"
    updated_by: "<actor>"
    last_updated: "<YYYY-MM-DD>"
    health:
      overall: "<green|amber|red|unassessed>"
      dimensions:
        time: "<green|amber|red|unassessed>"
        cost: "<green|amber|red|unassessed>"
        scope: "<green|amber|red|unassessed>"
        quality: "<green|amber|red|unassessed>"
        risk: "<green|amber|red|unassessed>"
        benefits: "<green|amber|red|unassessed>"
    dependencies: []
    evidence: []
    aggregation_policy: ~
    execution_refs: []
    extensions: {}
```

**Dependency edge sub-schema** (per CLAUSE-019; for reference when populating `dependencies[]` in AC003):
```yaml
- from_id: "<upstream scope_uid>"
  to_id: "<downstream scope_uid>"
  relationship: "<depends_on|blocks>"
  category: "<internal|external>"
  criticality: "<critical|near_critical|non_critical>"
  owner: "<resolution owner>"
  status: "<open|at_risk|resolved>"
  evidence: []
```

**Evidence pointer sub-schema** (per CLAUSE-030; for reference):
```yaml
- type: "<note|pr|build|test_result|decision|session|sign_off|check|workflow_run|execution_trace>"
  ref: "<repo-relative path, stable ID, or URL>"
  date: "YYYY-MM-DD"
  by: "<actor identifier>"
  summary: "<1-line description>"
```

**P-STD-004 placement**: File MUST be created at `prompt/artifacts/tasks/P/status/status_program.yaml`. The `status/` directory is the P-STD-004 canonical placement per CLAUSE-047 (path locked in AC001 §A).

---

### SPEC-002 — TK003: Author Narrative Template

| Field | Detail |
|:--|:--|
| Requirement Source | AC002 plan TK003; GIR-001(a) approved at GATE-002; requirements analysis §V.D (Narrative Structure Specification), §V.E (Agent-Role Binding Specification) |
| Implementation Detail | See §III.B below |
| Expected Format | Markdown file with YAML frontmatter, 8 required sections, and embedded Operational Update Protocol |
| Acceptance Criteria | File exists at correct path; all 8 sections present; binding table embedded in §7; authority hierarchy stated; P-STD-004 placement satisfied |
| Status | `open` |

#### §III.B — Narrative Template Implementation Detail

**Target file**: `prompt/artifacts/tasks/P/status/status_program.md`

**Frontmatter** (per requirements analysis §V.D):
```yaml
artifact_type: 'STATUS'
initiative_id: 'P'
schema_version: '1.0'
version: '<semver>'
date: 'YYYY-MM-DD'
status: 'draft'
author: '<role>'
decision_owner_role: 'Client'
ledger_reference: 'prompt/artifacts/tasks/P/status/status_program.yaml'
```

**Authority hierarchy statement** (CLAUSE-044 + CLAUSE-049): Place prominently near the top of the document body:
> "The ledger (`status_program.yaml`) is authoritative. This narrative is derived. Any drift → correct the narrative."

**8 required sections** (per requirements analysis §V.D + SES001-DEC005):

1. **Summary** — High-level program status overview (derived from ledger). Mark with `<!-- DERIVED FROM LEDGER -->`.
2. **Status** — Per-SID status table (derived from ledger entries). Mark with `<!-- DERIVED FROM LEDGER -->`.
3. **Health** — Per-SID health/RAG summary (derived from ledger `health` fields). Mark with `<!-- DERIVED FROM LEDGER -->`.
4. **Dependencies** — Cross-SID dependency roll-up: open critical, at-risk, resolution owners (derived from ledger `dependencies[]`, per CLAUSE-027). Mark with `<!-- DERIVED FROM LEDGER -->`.
5. **Evidence** — Recent evidence pointers for high-impact transitions (derived from ledger `evidence[]`). Mark with `<!-- DERIVED FROM LEDGER -->`.
6. **Next Actions** — Upcoming work items, readiness gates, blockers. Mark with `<!-- DERIVED FROM LEDGER -->`.
7. **Operational Update Protocol** — Agent-role binding, update triggers, update sequence. Embed the full binding table from §V.E (see below). This section is NOT derived — it is the governing protocol.
8. **Changelog** — Embedded changelog (per SES001-DEC006).

**`<!-- DERIVED FROM LEDGER -->` derivation rule** (CLAUSE-048): All content in sections 1–6 MUST carry this marker to signal derivation from the ledger. Manual edits that contradict the ledger are a drift violation (CLAUSE-049).

**GIR-001(a) — Operational Update Protocol section content** (embed verbatim from requirements analysis §V.E):

The Operational Update Protocol section MUST contain:

**Agent-Role Binding Table** (4 RACI rows):

| P-STD-002 RACI Label | Workspace Agent Role | Typical Responsibilities |
|:--|:--|:--|
| Responsible | LLM_Developer, LLM_Consultant, LLM_Reviewer (context-dependent) | Execute routine non-terminal transitions when guards satisfied; attribute updates with `updated_by` |
| Accountable | Client | Execute terminal transitions (→ `completed`, → `cancelled`) and reopen transitions; resolve disputes |
| Consulted | LLM_Consultant | Advise on status assessments, health evaluations, dependency analysis |
| Informed | All roles | Receive stale-state notifications; review narrative summaries |

**Update Trigger Points** (7 triggers — when agents MUST update the ledger):
1. Activity status change (any transition in the CLAUSE-005 matrix)
2. Gate closure (GATE-### APPROVE/RECYCLE → activity and dependent status updates)
3. Blocker recorded or resolved (→ `blocked` or `blocked` → `in_progress`)
4. Deliberate pause or resume (→ `on_hold` or `on_hold` → `ready`)
5. Explicit deferral or reactivation (→ `deferred` or `deferred` → `ready`) with target scope/cycle and next review date
6. Health reassessment trigger (per CLAUSE-017: transition to `ready`/`in_progress`, entering `blocked`/`on_hold`/`deferred`, terminal)
7. Stale-state review cycle (per CLAUSE-038: at least every 7 calendar days, with `deferred` items re-evaluated within 30 days)

**Terminal / Reopen Execution Rule**:
- The Accountable role (Client) executes terminal transitions and reopen transitions directly, or explicitly authorizes a named delegate to perform the update.
- Any delegated terminal/reopen update MUST record authorization evidence using the ledger evidence schema (`type`, `ref`, `date`, `by`, `summary`) so the approval trail is auditable per CLAUSEs 008, 030, 032, and 039.

**Conflict Resolution Rule** (per CLAUSE-037):
- When conflicting updates occur, the most recent update remains authoritative until reviewed.
- Any dispute over the correct status MUST be escalated to the Client as Accountable role, and the resolution decision MUST be recorded as evidence.

**Update Sequence** (per CLAUSE-048):
1. Validate evidence (plan + notes + changed artifacts)
2. Update ledger entry (canonical)
3. Derive/update narrative sections from ledger (derived)
4. Record `updated_by` and `last_updated` on the modified entry

**P-STD-004 placement**: File MUST be created at `prompt/artifacts/tasks/P/status/status_program.md`.

---

### SPEC-003 — TK004: Conformance Validation

| Field | Detail |
|:--|:--|
| Requirement Source | AC002 plan TK004; requirements analysis §V.G (Conformance Validation Checklist) — specifically the "Structural/content conformance (AC002 GATE-002 / AC003 GATE-002)" checklist block |
| Implementation Detail | See §III.C below |
| Expected Format | Validation results artifact documenting each checklist item with pass/fail evidence |
| Acceptance Criteria | All structural conformance checklist items evaluated with evidence; failures identified with remediation guidance; no unaddressed failures |
| Status | `open` |

#### §III.C — Conformance Validation Implementation Detail

**Scope**: TK004 validates TK002 + TK003 outputs against the structural/content conformance checklist from requirements analysis §V.G. The checklist items under "Structural/content conformance (AC002 GATE-002 / AC003 GATE-002)" are the binding validation surface:

**Checklist items to evaluate**:
- [ ] P, T102, T104 SID entries present at activity-level granularity (note: v1 skeleton uses placeholder — confirm schema supports population)
- [ ] All entries satisfy MVAT (CLAUSE-054): `status`, `as_of`, `updated_by`, `last_updated`, evidence pointers
- [ ] Health dimensions present (may be `unassessed`)
- [ ] Dependency edges use correct schema (CLAUSE-019 fields)
- [ ] Evidence pointers use correct schema (CLAUSE-030 fields)
- [ ] Narrative sections 1–6 are derivable from ledger (CLAUSE-048 compliance)
- [ ] No drift between ledger and narrative (CLAUSE-049)
- [ ] `schema_version` field present (CLAUSE-050)

**Validation method**: For each checklist item, record:
- **Item**: the checklist statement
- **Evidence**: file path + field/section that was checked
- **Result**: PASS / FAIL / NOT-APPLICABLE
- **Notes**: any remediation guidance if FAIL

**Dependency**: TK004 MUST NOT begin until both TK002 and TK003 are complete (per AC002 plan task register Depends On).

**Output format**: The validation results may be embedded in the TK005 DEV-REPORT or produced as a standalone validation checklist artifact. The preferred form for DEV-REPORT inclusion is a structured checklist table with pass/fail per item and a summary verdict.

---

## IV. IMPLEMENTATION SEQUENCE

Execution order is dependency-driven:

1. **SPEC-001 (TK002)** — Author ledger skeleton first. Creates the canonical YAML file. No dependencies (other than GATE-002 APPROVE recorded).
2. **SPEC-002 (TK003)** — Author narrative template after TK002 exists. Narrative is derived from the ledger structure; the ledger skeleton informs the narrative's section content and derivation markers.
3. **SPEC-003 (TK004)** — Validate conformance last. Requires both TK002 and TK003 to be complete before evaluation can proceed.

## V. REFERENCES

| Document | Path |
|:--|:--|
| Governing Plan (AC002) | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC002/plan_P-PH000-ST002-AC002.md` |
| GATE-002 Proposal (GIR decisions) | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC002/proposal/proposal_P-PH000-ST002-AC002-GATE-002_design-decision-disposition.md` |
| Implementation Requirements Analysis | `prompt/artifacts/tasks/P/workspace/PH000/ST002/analysis/analysis_P-PH000-ST002_status-system-implementation-requirements.md` |
| P-STD-002 (Program Status Standard) | `prompt/artifacts/tasks/P/standard/standard_P-STD-002_program-status-standard.md` |
| P-STD-005 (Universal ID Specification) | `prompt/artifacts/tasks/P/standard/standard_P-STD-005_universal-id-specification.md` |

## VI. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-03-21 | Initial | Unified developer-facing task specification for TK002 (ledger skeleton), TK003 (narrative template), and TK004 (conformance validation). Distills approved GATE-002 GIR decisions (GIR-001 agent-role binding, GIR-002 P-STD-005 UIDs, GIR-003 optional field scope) into concrete implementation instructions. Source: GATE-002 independent package review session. |
