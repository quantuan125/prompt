---
artifact_type: 'PLAN'
planning_level: 'STREAM'
initiative_id: 'P'
initiative_code: 'PROGRAM'
phase: '0'
stream_id: 'P-PH000-ST000'
version: '0.1.0'
date: '2026-02-05'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
governance_rules: 'prompt/templates/consultant/workspace/workspace_documentation_rules.md'
procedural_guideline: 'prompt/templates/consultant/workspace/guideline_workspace_plan.md'
parent_plan: 'prompt/artifacts/tasks/P/workspace/plan/plan_P-PH000.md'
raw_source:
  - 'prompt/artifacts/tasks/P/raw/PH000/ST000/raw_P-PH000-ST000-AC001-2026-02-05.txt'
---

# PLAN: Program Governance — P / Phase `PH000` / Stream `P-PH000-ST000`: Bootstrap Consultation + Program SPS Shell + Research Commission

## I. EXECUTIVE SUMMARY

**Purpose**: Convert the bootstrap consultation into a program planning spine, create the initial Program SPS shell, and register (but do not execute) the first program-scoped research commission (`P-RES-001`), which is blocked until `P-RES` is enabled at `P` scope.

**Status**: This stream remains `planned` until AC002 and AC003 complete.

---

## II. STREAM OUTLINE

**Stream ID**: `P-PH000-ST000`
**Execution Mode**: SEQUENTIAL
**Depends On**: —

**Context**:
- Raw transcript: `prompt/artifacts/tasks/P/raw/PH000/ST000/raw_P-PH000-ST000-AC001-2026-02-05.txt`
- Notes guideline: `prompt/templates/consultant/workspace/guideline_workspace_notes.md`
- Plan guideline: `prompt/templates/consultant/workspace/guideline_workspace_plan.md`
- SPS structural template: `prompt/templates/consultant/sps/sps_structural_template.md`

### Activity Register

| Activity | Activity ID | Name | Status | Owner | Depends On | Deliverable | Reference |
|:--|:--|:--|:--|:--|:--|:--|:--|
| AC001 | `P-PH000-ST000-AC001` | Program bootstrap consultation + decisions capture | `completed` | LLM_Consultant | — | `notes_P-PH000*.md` + `notes_P-PH000-ST000-AC001.md` | Raw transcript |
| AC002 | `P-PH000-ST000-AC002` | Create Program SPS shell (`sps_P-PROGRAM.md`) | `completed` | LLM_Consultant | AC001 | `prompt/artifacts/tasks/P/ssot/sps_P-PROGRAM.md` | SPS template |
| AC003 | `P-PH000-ST000-AC003` | Commission `P-RES-001` (PM tooling + orchestration status research) | `planned` | LLM_Consultant | ST001-AC001 | Planned brief/report paths only | `T102-STD-006` pattern |

---

## III. ACTIVITIES

#### Activity AC001: Program Bootstrap Consultation + Decisions Capture

**Activity ID**: `P-PH000-ST000-AC001`

**Purpose**: Capture the bootstrap consultation outcomes (decisions, actions, open questions) as toolable Notes and establish the program planning spine at the canonical program root.

**Deliverables**:
- `prompt/artifacts/tasks/P/workspace/notes/notes_P-PH000.md`
- `prompt/artifacts/tasks/P/workspace/notes/notes_P-PH000-ST000.md`
- `prompt/artifacts/tasks/P/workspace/notes/PH000/ST000/notes_P-PH000-ST000-AC001.md`

**Scope**:
- In scope: decision capture only (no `P-STD` bodies, no status artifact implementation).
- Excludes: any edits to adopter initiatives (e.g., `T104`).

**Task Register**:
| Task ID | Description | Status | Action |
|:--|:--|:--|:--|
| `P-PH000-ST000-AC001-TK001` | Register Stream ST000 notes surfaces (phase register + stream register) | `completed` | Notes register files created and linked in program plans |
| `P-PH000-ST000-AC001-TK002` | Capture consultation decisions in Activity Notes using DP/DEC/ACT/OQ tables | `completed` | `notes_P-PH000-ST000-AC001.md` created with structured tables and session entry |
| `P-PH000-ST000-AC001-TK003` | Relocate raw transcript to program raw directory and reference it canonically | `completed` | Raw moved to `prompt/artifacts/tasks/P/raw/PH000/ST000/` and referenced by Notes/Plans |

**Success Criteria Checklist**:
- [x] Activity Notes exist and conform to `guideline_workspace_notes.md`
- [x] Program raw transcript is stored under the program raw directory and linked by path

#### Activity AC002: Create Program SPS Shell (`sps_P-PROGRAM.md`)

**Activity ID**: `P-PH000-ST000-AC002`

**Purpose**: Create the initial Program SPS shell as the SSOT anchor point for future `P-STD-*` bodies and program-wide governance considerations.

**Deliverable**:
- `prompt/artifacts/tasks/P/ssot/sps_P-PROGRAM.md`

**Scope**:
- In scope: structural SPS shell only, following the SPS structural template.
- Excludes: authoring the full content for `P-STD-001` / `P-STD-002` bodies (planned in `P-PH000-ST001`).

**Inputs Required**:
- `prompt/templates/consultant/sps/sps_structural_template.md`

**Task Register**:
| Task ID | Description | Status | Action |
|:--|:--|:--|:--|
| `P-PH000-ST000-AC002-TK001` | Instantiate Program SPS using the structural template | `completed` | `sps_P-PROGRAM.md` created with required structure |
| `P-PH000-ST000-AC002-TK002` | Add placeholder Project Standards index entries for `P-STD-001` and `P-STD-002` | `completed` | `P-STD-001` and `P-STD-002` placeholder rows added to Project Standards table |

**Success Criteria Checklist**:
- [x] `sps_P-PROGRAM.md` exists and matches template structure
- [x] Project Standards section includes placeholders for `P-STD-001` and `P-STD-002`

#### Activity AC003: Commission `P-RES-001` (PM Tooling + Orchestration Status Research)

**Activity ID**: `P-PH000-ST000-AC003`

**Purpose**: Register the first program-scoped research commission to inform program status orchestration design and future automation candidates.

**Dependency (hard)**: This activity is blocked until `P-PH000-ST001-AC001` enables `P-RES-###` by updating the `RES` token allowed scope in `T102-STD-005`.

**Deliverables (planned; not created in this phase)**:
- `prompt/artifacts/tasks/P/research/brief/brief_P-RES-001_pm-tooling-status-orchestration.md`
- `prompt/artifacts/tasks/P/research/report/report_P-RES-001_pm-tooling-status-orchestration.md`

**Inputs Required**:
- `prompt/templates/researcher/template_research_brief.md`
- `prompt/templates/researcher/template_research_report.md`

**Task Register**:
| Task ID | Description | Status | Action |
|:--|:--|:--|:--|
| `P-PH000-ST000-AC003-TK001` | Define research purpose, deliverables, and scope (mirror T104 research commissioning rigor) | `planned` | — |
| `P-PH000-ST000-AC003-TK002` | Require Issues & Risks section in report per `T102-STD-007` | `planned` | — |

**Success Criteria Checklist**:
- [ ] Activity entry exists in the plan with clear dependency and planned deliverables

---

## IV. LINKS REGISTER

| Link Type | Target | Path |
|:--|:--|:--|
| Plan (this file) | Stream 0 Plan | `prompt/artifacts/tasks/P/workspace/plan/plan_P-PH000-ST000.md` |
| Parent Plan | Program Phase Plan | `prompt/artifacts/tasks/P/workspace/plan/plan_P-PH000.md` |
| Notes | Phase Notes Register | `prompt/artifacts/tasks/P/workspace/notes/notes_P-PH000.md` |
| Notes | Stream ST000 Notes | `prompt/artifacts/tasks/P/workspace/notes/notes_P-PH000-ST000.md` |
| SSOT (shell) | Program SPS | `prompt/artifacts/tasks/P/ssot/sps_P-PROGRAM.md` |
| Raw | Consultation Transcript | `prompt/artifacts/tasks/P/raw/PH000/ST000/raw_P-PH000-ST000-AC001-2026-02-05.txt` |

---

## V. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v0.1.0 | 2026-02-05 | Initial | Stream ST000 plan created with AC001 (decisions capture), AC002 (program SPS shell), and AC003 (planned research commission) |
