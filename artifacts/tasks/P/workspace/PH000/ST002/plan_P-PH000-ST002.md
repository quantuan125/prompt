---
artifact_type: 'PLAN'
planning_level: 'STREAM'
initiative_id: 'P'
initiative_code: 'PROGRAM'
phase: '0'
stream_id: 'P-PH000-ST002'
version: '0.1.2'
date: '2026-02-26'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
governance_rules: 'prompt/templates/consultant/workspace/workspace_documentation_rules.md'
procedural_guideline: 'prompt/templates/consultant/workspace/guideline_workspace_plan.md'
parent_plan: 'prompt/artifacts/tasks/P/workspace/PH000/plan_P-PH000.md'
---

# PLAN: Program Governance — P / Phase `PH000` / Stream `P-PH000-ST002`: Program Status System (Planned)

## I. EXECUTIVE SUMMARY

**Purpose**: Plan the program-wide status artifact (schema + protocol + authoring workflow). This stream is planning-only in Phase `PH000` unless explicitly activated by the Decision Owner.

**Important constraint**: `prompt/artifacts/tasks/P/status/status_program.md` MUST NOT be created until `P-PH000-ST001-AC003` (Program Status Standard) is authored and accepted.

---

## II. STREAM OUTLINE

**Stream ID**: `P-PH000-ST002`
**Execution Mode**: SEQUENTIAL
**Depends On**: `P-PH000-ST001-AC003`

### Activity Register

| Activity | Activity ID | Name | Status | Owner | Depends On | Deliverable | Reference |
|:--|:--|:--|:--|:--|:--|:--|:--|
| AC001 | `P-PH000-ST002-AC001` | Define status artifact schema + update protocol (decision-complete) | `planned` | LLM_Consultant | — | Schema + protocol spec (this file) | Consultation outcomes |
| AC002 | `P-PH000-ST002-AC002` | Author `status_program.md` (deferred implementation activity) | `planned` | LLM_Consultant | ST001-AC003, AC001 | `prompt/artifacts/tasks/P/status/status_program.md` | `P-STD-002` |

---

## III. ACTIVITIES (PLANNED)

#### Activity AC001: Define Status Artifact Schema + Update Protocol (Decision-Complete)

**Activity ID**: `P-PH000-ST002-AC001`

**Purpose**: Lock the status artifact schema and update protocol so later implementation is mechanical and does not require further design decisions.

> **Informative Seed Note (SES001-DEC-002)**: The schema and protocol below are informative seed input only. The authoritative contract for status schema, enum governance, and update protocol resides in `P-STD-002` once accepted. `P-PH000-ST002-AC002` MUST reference `P-STD-002`, not this section, as the normative authority.

**Deliverable (spec)**: The schema and protocol below MUST be implemented exactly when AC002 is executed.

##### A) Status file home (locked)
- `prompt/artifacts/tasks/P/status/status_program.md`

##### B) Schema (locked)

**YAML frontmatter (minimum keys)**:
- `artifact_type: 'STATUS'`
- `initiative_id: 'P'`
- `version`, `date`, `status`, `author`, `decision_owner_role`
- `schema_version: '1.0.0'`

**Canonical payload (authoritative; machine-readable)**:
- `initiatives:` list of objects with fields:
  - `initiative_id` (e.g., `T104`)
  - `initiative_code` (e.g., `CWS`)
  - `phase` (e.g., `PH001`)
  - `streams:` list of `{stream_id, execution_mode, status, active_activity_id, depends_on, blockers}`
  - `last_updated` (ISO date)

**Optional human view**:
- A markdown table derived from the canonical YAML payload MAY be included, but MUST be explicitly labeled **“Derived / Non-authoritative”**.

##### C) Update protocol (locked)
1) Canonical truth is the YAML payload.
2) Agents update the status file after completing an Activity (include terminal checklist evidence elsewhere; status file remains summary-only).
3) Every update increments `last_updated` and appends a short entry to a status changelog section inside the status file.

##### D) Initial scope when AC002 is executed (locked)
- The initial `initiatives:` payload SHOULD include **only** `T102` and `T104` (minimal set).

**Task Register**:
| Task ID | Description | Status | Action |
|:--|:--|:--|:--|
| `P-PH000-ST002-AC001-TK001` | Encode the schema + protocol (this section) as decision-complete requirements | `planned` | — |

#### Activity AC002: Author `status_program.md` (Deferred Implementation Activity)

**Activity ID**: `P-PH000-ST002-AC002`

**Purpose**: Create the machine-readable status SSOT per AC001 schema and `P-STD-002`.

**Deliverable (planned; not created in this phase)**:
- `prompt/artifacts/tasks/P/status/status_program.md`

**Depends On**:
- `P-PH000-ST001-AC003` (Program Status Standard)
- `P-PH000-ST002-AC001` (Schema + update protocol locked)

> **Research Integration Note (2026-02-26)**: Combined P-RES-001 and P-RES-002 research findings confirm the seed schema concept (AC001) is architecturally valid but the implementation schema will be substantially richer. When AC002 is executed, the implementer MUST reference the accepted `P-STD-002` (specifically P-STD-002E) as the normative authority. The implementation schema will include: evidence pointers per status entry, 6-dimension health/RAG model, graph-first dependency edges, execution references (check run IDs, workflow run IDs), aggregation policy fields, and MVAT-compliant minimum entry fields. The dual-artifact model (canonical ledger + derived narrative) is confirmed.

---

## IV. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v0.1.2 | 2026-02-26 | Amendment | Added informative research integration note to AC002 section documenting combined P-RES-001 + P-RES-002 impact on implementation schema. No structural or dependency changes. Evidence: consultant session 2026-02-26. |
| v0.1.1 | 2026-02-23 | Amendment | AC001 schema annotated as informative seed only per SES001-DEC-002; authoritative contract deferred to P-STD-002. Evidence: `raw_P-PH000-ST001-AC003-SES001.txt` |
| v0.1.0 | 2026-02-05 | Initial | Stream ST002 plan created to lock status artifact schema/protocol and defer `status_program.md` authoring to a later activity |
