---
artifact_type: 'PLAN'
planning_level: 'ACTIVITY'
initiative_id: 'P'
initiative_code: 'PROGRAM'
phase: '0'
stream_id: 'P-PH000-ST001'
activity_id: 'P-PH000-ST001-AC003'
version: '0.1.0'
date: '2026-02-23'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
governance_rules: 'prompt/templates/consultant/workspace/workspace_documentation_rules.md'
parent_plan: 'prompt/artifacts/tasks/P/workspace/plan/plan_P-PH000-ST001.md'
---

# PLAN: P (PROGRAM) — Phase 0 / Stream ST001 / Activity AC003: Author P-STD-002 (Program Status Standard)

> **DRAFT — Not finalized.** Task register, CLAUSE domain mapping, and success criteria are subject to amendment after `P-PH000-ST004-AC001-GATE-003` (P-RES-001 integration sign-off). The structure and scope below reflect SES001 consultation decisions; detailed task decomposition will be refined once research recommendations are available.

## I. EXECUTIVE SUMMARY

**Purpose**: Author `P-STD-002` (Program Status Standard) as a program-wide status governance standard covering: canonical 7-state status vocabulary with transition rules, health/RAG assessment requirements, unified dependency visibility schema, evidence linkage protocol, update protocol with role accountability, and status artifact specification. This standard is a prerequisite for authoring the program status artifact in `P-PH000-ST002`.

**Non-goal**: This activity does not create `status_program.md` (deferred to P-PH000-ST002-AC002) or execute repo-wide guideline retrofits beyond the explicit cascade task (TK006).

---

## II. ACTIVITY OUTLINE

**Activity ID**: `P-PH000-ST001-AC003`
**Objective**: Produce a P-STD-001-conformant combined standard-specification file that establishes program-wide status governance semantics and is accepted by the Client.
**Execution Mode**: SEQUENTIAL
**Depends On**: `P-PH000-ST004-AC001` (P-RES-001 integration sign-off via GATE-003)

**Context**:
- `prompt/artifacts/tasks/P/standard/standard_P-STD-002_program-status-standard.md` (deliverable — to be created)
- `prompt/artifacts/tasks/P/ssot/sps_P-PROGRAM.md` (P-STD-002 row update)
- `prompt/templates/consultant/standards/guideline_standard_specs.md` (authoring rules)
- `prompt/templates/consultant/standards/template_standard_specs.md` (structural skeleton)
- `prompt/templates/consultant/workspace/guideline_workspace_plan.md` (cascade target)

### Task Register

| Task | Task ID | Name | Status | Owner | Depends On | Target | Reference | Action |
|:--|:--|:--|:--|:--|:--|:--|:--|:--|
| TK000 | `P-PH000-ST001-AC003-TK000` | Confirm sps_P P-CON-003 amendment applied | `planned` | LLM_Consultant | — | sps_P | DEC-003 | — |
| TK001 | `P-PH000-ST001-AC003-TK001` | Ingest P-RES-001 report recommendations and map to CLAUSE domains | `planned` | LLM_Consultant | ST004-AC001-GATE-003 | — | P-RES-001 report | — |
| TK002 | `P-PH000-ST001-AC003-TK002` | Draft P-STD-002 combined file: Specification section | `planned` | LLM_Consultant | TK001 | standard_P-STD-002_...md | template_standard_specs | — |
| TK003 | `P-PH000-ST001-AC003-TK003` | Draft P-STD-002-ADR-001 in Decision Record section | `planned` | LLM_Consultant | TK002 | standard_P-STD-002_...md | P-STD-001-CLAUSE-025 | — |
| TK004 | `P-PH000-ST001-AC003-TK004` | Validate P-STD-002 against P-STD-001 authoring rules | `planned` | LLM_Consultant | TK003 | — | guideline_standard_specs | — |
| GATE-001 | `P-PH000-ST001-AC003-GATE-001` | **Gate: Client acceptance of P-STD-002**. Entry: TK004 complete. Reviewer: Client. Exit: explicit acceptance recorded. | `planned` | Client | TK004 | — | — | — |
| TK005 | `P-PH000-ST001-AC003-TK005` | Update sps_P P-STD-002 row (status → `accepted`, canonical path, effective date) | `planned` | LLM_Consultant | GATE-001 | sps_P | P-STD-001-CLAUSE-012 | — |
| TK006 | `P-PH000-ST001-AC003-TK006` | Cascade P-STD-002 status enums to downstream guideline files | `planned` | LLM_Consultant | GATE-001 | guideline files | DEC-008 | — |

---

## III. TASKS (DETAILED)

### Task TK000: Confirm sps_P P-CON-003 Amendment Applied

**Task ID**: `P-PH000-ST001-AC003-TK000`

**Purpose**: Pre-work verification that the P-CON-003 revision from SES001 has been applied to sps_P before AC003 execution begins.

**Deliverable**: Verification only — no artifact produced.

**Steps**:
1. Open `prompt/artifacts/tasks/P/ssot/sps_P-PROGRAM.md`
2. Confirm P-CON-003 title reads `(Artifact Format Governance)`
3. Confirm body has (A) and (B) sub-rules as specified in DEC-003
4. If not applied, escalate — this is a blocking prerequisite

**Success Criteria**:
- [ ] P-CON-003 revision confirmed in sps_P

---

### Task TK001: Ingest P-RES-001 Report Recommendations

**Task ID**: `P-PH000-ST001-AC003-TK001`

**Purpose**: Extract and map P-RES-001 research findings to P-STD-002 CLAUSE domains.

**Deliverable**: CLAUSE domain mapping (working document or inline in this plan as amendment).

**Inputs Required**:
- `prompt/artifacts/tasks/P/research/report/report_P-RES-001_status-standard-research.md` — Primary input
- P-RES-001 integration recommendations (GATE-003 approved)

**Planned CLAUSE domains (draft — subject to P-RES-001 findings)**:
- **P-STD-002A — Status Vocabulary**: Canonical 7-state enum (`planned`, `ready`, `in_progress`, `blocked`, `on_hold`, `completed`, `cancelled`), meta-categories, transition rules
- **P-STD-002B — Health Assessment**: RAG requirements, threshold framework, assessment dimensions
- **P-STD-002C — Dependency Visibility**: Typed schema (FS/SS/FF/SF), categorization (mandatory/resource/discretionary/external/cross-team), risk levels
- **P-STD-002D — Update Protocol**: Evidence linkage for terminal transitions, role accountability matrix, stale-state SLA placeholder (Phase 2)
- **P-STD-002E — Status Artifact**: Schema requirements, format permissions (per P-CON-003B), placement rules, update protocol

**Steps**:
1. Read accepted P-RES-001 report in full
2. For each CLAUSE domain above, extract: recommended approach, industry precedents cited, trade-offs, and specific field/enum/schema proposals
3. Document the mapping as an amendment to this plan (TK001 Action column)
4. Identify any gaps between research recommendations and the 5 CLAUSE domains above; propose domain additions if needed

**Success Criteria**:
- [ ] All P-RES-001 recommendations mapped to at least one CLAUSE domain
- [ ] No research recommendation is unaddressed

---

### Task TK002: Draft P-STD-002 Combined File — Specification Section

**Task ID**: `P-PH000-ST001-AC003-TK002`

**Purpose**: Author the normative Specification section of P-STD-002.

**Deliverable**: `prompt/artifacts/tasks/P/standard/standard_P-STD-002_program-status-standard.md`

**Inputs Required**:
- TK001 CLAUSE domain mapping (primary)
- `prompt/templates/consultant/standards/template_standard_specs.md` — Structural skeleton
- `prompt/templates/consultant/standards/guideline_standard_specs.md` — Authoring rules
- `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md` — Authority chain

**Steps**:
1. Copy `template_standard_specs.md` to deliverable path
2. Fill frontmatter: `artifact_type: 'STANDARD'`, `initiative_id: 'P'`, `std_id: 'P-STD-002'`, `governed_by: 'P-STD-001'`
3. Set heading: `# P-STD-002 — Program Status Standard`
4. Author `## Specification` with substandard headings per planned domains (P-STD-002A through P-STD-002E)
5. Author Specification Index per `P-STD-001-CLAUSE-002` (required if >5 CLAUSEs)
6. For each substandard, author CLAUSEs using `P-STD-002-CLAUSE-###` format per `P-STD-001-CLAUSE-018B`
7. Use `MUST`/`SHOULD`/`MAY` keywords per `P-STD-001-CLAUSE-008` (BCP 14 primary vocabulary)
8. Include subclauses where needed per `P-STD-001-CLAUSE-020`

**Success Criteria**:
- [ ] Combined file exists at canonical path
- [ ] Follows `P-STD-001-CLAUSE-001A` canonical structure (5 required sections in order)
- [ ] Specification Index present per `P-STD-001-CLAUSE-002`
- [ ] All CLAUSEs use `P-STD-002-CLAUSE-###` format
- [ ] Normative keywords follow `P-STD-001-CLAUSE-008`

---

### Task TK003: Draft P-STD-002-ADR-001

**Task ID**: `P-PH000-ST001-AC003-TK003`

**Purpose**: Author the embedded decision record capturing the rationale for P-STD-002 design choices.

**Deliverable**: `## Decision Record` section within `standard_P-STD-002_program-status-standard.md`

**Steps**:
1. Author `P-STD-002-ADR-001` body per `P-STD-001-CLAUSE-025` (DR Body Template)
2. Required subheadings: Context, Decision, Alternatives Considered, Consequences
3. Context MUST cite: P-RES-001 research findings, SES001 consultation decisions (DEC-001 through DEC-012), existing analysis file as seed
4. Decision MUST document: 7-state enum choice, unified dependency schema choice, evidence linkage normative requirement, stale-state SLA deferral
5. Alternatives MUST include: 3-state enum (minimal), initiative-specific dependency models, evidence linkage as informative-only
6. Consequences MUST include: guideline cascade requirement (positive), enum migration overhead (negative/neutral)

**Success Criteria**:
- [ ] P-STD-002-ADR-001 body present under `## Decision Record`
- [ ] Follows `P-STD-001-CLAUSE-025` template exactly
- [ ] Rationale traces to P-RES-001 and SES001 decisions

---

### Task TK004: Validate Against P-STD-001 Authoring Rules

**Task ID**: `P-PH000-ST001-AC003-TK004`

**Purpose**: Self-compliance audit of P-STD-002 against P-STD-001 and its derivative guideline.

**Steps**:
1. Check `P-STD-001-CLAUSE-001` (canonical file structure — 5 sections in order)
2. Check `P-STD-001-CLAUSE-002` (Specification Index present if >5 CLAUSEs)
3. Check `P-STD-001-CLAUSE-003` (substandard architecture — universal membership, rendering)
4. Check `P-STD-001-CLAUSE-006` (anchor stability — normalization rules)
5. Check `P-STD-001-CLAUSE-018` (CLAUSE construction — format, titles, subclauses)
6. Check `P-STD-001-CLAUSE-025` (DR body template)
7. Check `P-STD-001-CLAUSE-028` (References and Provenance sections)
8. Run checks from `guideline_standard_specs.md` locked rules

**Success Criteria**:
- [ ] All P-STD-001 lint checks pass per `P-STD-001-CLAUSE-007`
- [ ] No normative leakage into Decision Record per `P-STD-001-CLAUSE-021`

---

### Gate GATE-001: Client Acceptance of P-STD-002

**Gate ID**: `P-PH000-ST001-AC003-GATE-001`

**Entry Criteria**: TK004 complete (self-compliance audit passed)
**Reviewer**: Client
**Exit Criteria**: Explicit Client acceptance recorded with date. P-STD-002 status transitions from `draft` → `accepted`.

---

### Task TK005: Update sps_P P-STD-002 Row

**Task ID**: `P-PH000-ST001-AC003-TK005`

**Purpose**: Finalize the P-STD-002 registration in the program SPS.

**Steps**:
1. In `sps_P-PROGRAM.md` STD Index, update P-STD-002 row:
   - Status: `planned` → `accepted`
   - Effective: `—` → acceptance date (ISO-8601)
   - Canonical Path: confirm correct path
   - Verification: update with final verification criteria
2. Add or update the P-STD-002 body paragraph below the STD Index (matching the P-STD-001 body pattern)
3. Version bump sps_P with changelog entry

**Success Criteria**:
- [ ] P-STD-002 row in STD Index shows `accepted` with effective date and canonical path
- [ ] P-STD-002 body paragraph added to sps_P

---

### Task TK006: Cascade Status Enums to Downstream Guideline Files

**Task ID**: `P-PH000-ST001-AC003-TK006`

**Purpose**: Update all downstream guideline files that reference status values to defer to or align with P-STD-002's canonical 7-state enum set and transition rules.

**Deliverable**: Updated guideline files with P-STD-002 references.

**Scope**:
- In scope: guideline files under `prompt/templates/consultant/workspace/` that hardcode status enums
- Out of scope: initiative-specific plan files (downstream adopters update on next touch); template files (update only if they hardcode enum values)

**Steps**:
1. **Identify all guideline files referencing status enums**:
   - Read `prompt/templates/consultant/workspace/guideline_workspace_plan.md` — §III.A (Stream/Activity register status enums) and §III.B (Task register status enums)
   - Search for other guideline files under `prompt/templates/consultant/workspace/` that reference `planned`, `in_progress`, `completed`, `cancelled`, `deferred`, or `failed`
   - Search `prompt/templates/consultant/workspace/guideline_workspace_notes.md` for status references
2. **Update `guideline_workspace_plan.md`**:
   - §III.A: Current text says status MUST be one of `planned`, `deferred`, `completed`, `cancelled`. Update to reference P-STD-002 as the canonical authority for status enums. Add note that register contexts may use a subset of the full 7-state set as appropriate, but MUST NOT introduce states not defined in P-STD-002.
   - §III.B: Current text says task status MUST be one of `planned`, `deferred`, `completed`, `cancelled`, `failed`. Apply same update pattern.
   - Add External Reference line for `P-STD-002 (Program Status Standard)` per `T102-STD-005-CLAUSE-004`
   - Version bump guideline with changelog entry
3. **Update other identified guideline files** (if any reference status values directly)
4. **Verify conformance**: Confirm no guideline file introduces status values not defined in P-STD-002

**Success Criteria**:
- [ ] `guideline_workspace_plan.md` references P-STD-002 as canonical status authority
- [ ] No guideline file introduces status states outside the P-STD-002 7-state enum
- [ ] All updated guideline files have changelog entries citing P-STD-002

---

## IV. LINKS REGISTER

| Link Type | Target | Path |
|:--|:--|:--|
| Plan (this file) | Activity Plan AC003 | `prompt/artifacts/tasks/P/workspace/plan/PH000/ST001/plan_P-PH000-ST001-AC003.md` |
| Plan | Stream Plan ST001 | `prompt/artifacts/tasks/P/workspace/plan/plan_P-PH000-ST001.md` |
| Plan | Research Stream ST004 | `prompt/artifacts/tasks/P/workspace/plan/plan_P-PH000-ST004.md` |
| Standard | P-STD-001 (authoring authority) | `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md` |
| Guideline | Standard specs guideline | `prompt/templates/consultant/standards/guideline_standard_specs.md` |
| Template | Standard specs template | `prompt/templates/consultant/standards/template_standard_specs.md` |
| Informal Input | Relocated analysis (seed) | `prompt/artifacts/tasks/P/workspace/PH000/ST002/analysis/analysis_P-PH000-ST002_status-system-research.md` |
| Evidence | SES001 Transcript | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/snotes/raw_P-PH000-ST001-AC003-SES001.txt` |

---

## V. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v0.1.0 | 2026-02-23 | Initial | Draft activity plan created from AC003-SES001 consultation. Task register and CLAUSE domains are draft; subject to amendment after P-RES-001 integration sign-off (P-PH000-ST004-AC001-GATE-003). Evidence: `raw_P-PH000-ST001-AC003-SES001.txt` |
