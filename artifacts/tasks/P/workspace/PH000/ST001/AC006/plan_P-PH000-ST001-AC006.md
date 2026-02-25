---
artifact_type: 'PLAN'
planning_level: 'ACTIVITY'
initiative_id: 'P'
initiative_code: 'PROGRAM'
phase: '0'
stream_id: 'P-PH000-ST001'
activity_id: 'P-PH000-ST001-AC006'
version: '1.3.0'
date: '2026-02-24'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
governance_rules: 'prompt/templates/consultant/workspace/workspace_documentation_rules.md'
procedural_guideline: 'prompt/templates/consultant/workspace/guideline_workspace_plan.md'
parent_plan: 'prompt/artifacts/tasks/P/workspace/PH000/ST001/plan_P-PH000-ST001.md'
---

# PLAN: Program Governance (PROGRAM) — Phase 0 / Stream ST001 / Activity P-PH000-ST001-AC006: Promote T102-STD-005 to P-STD-005 (Universal ID Specification)

## I. EXECUTIVE SUMMARY

**Purpose**: Promote `T102-STD-005` (ID Specification & Rules) to `P-STD-005` (Universal ID Specification) at Program scope. This promotion: (1) fixes stale references to superseded T102-STD-004 and T102-STD-009, (2) verifies pending amendments (ST005-AC005 deltas) are applied, (3) performs full content transfer with 1:1 CLAUSE re-identification, (4) authors timeline UID CLAUSEs (absorbing T104-STD-002 planned scope) directly into P-STD-005, (5) updates Tier 1 normative references across program-level artifacts, and (6) amends downstream plans that had planned work now absorbed.

**Non-goals**:
- This activity does not perform repo-wide remediation sweeps of existing `T102-STD-005-CLAUSE-*` references (these are covered by the alias window and migrated at next touch).
- This activity does not execute the full T102-PH001-ST002 baselining pipeline (a targeted pre-promotion audit is performed instead).
- This activity does not modify T102-STD-005 CLAUSE content beyond stale reference fixes and verified amendment application.

---

## II. ACTIVITY OUTLINE

**Activity ID**: `P-PH000-ST001-AC006`
**Objective**: Promote T102-STD-005 to P-STD-005 via fix-first/promote-clean methodology, absorbing T104-STD-002 timeline UID scope and T102-PH001-ST005-AC005 amendment scope.
**Execution Mode**: `SEQUENTIAL`
**Depends On**: `P-PH000-ST001-AC002` (completed)

**Context**:
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/plan_P-PH000-ST001.md`
- `prompt/artifacts/tasks/P/ssot/sps_P-PROGRAM.md`
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC006/plan_P-PH000-ST001-AC006.md`
- `prompt/artifacts/tasks/P/standard/standard_P-STD-005_universal-id-specification.md` (NEW)
- `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md`
- `prompt/artifacts/tasks/P/standard/P-STD-003_governance-standards-and-dr-index.md`
- `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-005_id-specification-rules.md`
- `prompt/artifacts/tasks/T104/workspace/PH001/ST002/plan_T104-PH001-ST002.md`
- `prompt/artifacts/tasks/T102/consultant/workspace/plan/plan_T102-PH001-ST005.md`
- `prompt/artifacts/tasks/T102/consultant/workspace/plan/plan_T102-PH001-ST002.md`
- `prompt/templates/consultant/standards/guideline_standard_specs.md`
- `prompt/skills/t102-adr-005-id-spec/SKILL.md`
- `prompt/documentation/adr_skills_catalog.md`

### Task Register

| Task | Task ID | Name | Status | Owner | Depends On | Target | Reference | Action |
|:--|:--|:--|:--|:--|:--|:--|:--|:--|
| TK001 | `P-PH000-ST001-AC006-TK001` | Fix stale references in T102-STD-005 (T102-STD-004 → P-STD-001, T102-STD-009 → P-STD-001) | `completed` | LLM_Developer | — | `T102-STD-005_id-specification-rules.md` | Stale refs mapping (see plan) | All 7 stale references fixed via PR #8 |
| TK002 | `P-PH000-ST001-AC006-TK002` | Verify ST005-AC005 deltas (C1, C2, B1) are applied to T102-STD-005 | `completed` | LLM_Developer | TK001 | `T102-STD-005_id-specification-rules.md` | RES-005 Delta C, RES-006 Delta B | Deltas C1/C2/B1 verified as present |
| TK003 | `P-PH000-ST001-AC006-TK003` | Targeted self-compliance audit of T102-STD-005 against P-STD-001 | `completed` | LLM_Reviewer | TK002 | Analysis artifact | `P-STD-001` | Pre-promotion audit produced with 3 findings |
| GATE-001 | `P-PH000-ST001-AC006-GATE-001` | Gate: Client approval of pre-promotion T102-STD-005 state | `completed` | Client | TK003 | Pass/fail | — | Approved via GATE-001 `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC006/verification/verification_P-PH000-ST001-AC006_gate-001.md`|
| TK004 | `P-PH000-ST001-AC006-TK004` | Author promotion contract proposal (re-identification mapping + timeline UID CLAUSE text + alias window + Tier 1 ref update plan) | `completed` | LLM_Consultant | GATE-001 | Proposal artifact | `P-STD-001-CLAUSE-030`, `T102-STD-005-CLAUSE-003A` | Proposal produced |
| GATE-002 | `P-PH000-ST001-AC006-GATE-002` | Gate: Client approval of promotion contract | `completed` | Client | TK004 | Pass/fail | — | Approved via GATE-002 `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC006/verification/verification_P-PH000-ST001-AC006_gate-002.md` |
| TK004.1 | `P-PH000-ST001-AC006-TK004.1` | Revise promotion contract to add session sub-tokens (DP/DEC/ACT/OQ) to CLAUSE-008 and CLAUSE-001 | `completed` | LLM_Developer | GATE-002 | Revised proposal | `guideline_workspace_notes.md` §2.2 | Proposal revised to v1.1.0 |
| TK005 | `P-PH000-ST001-AC006-TK005` | Create P-STD-005 combined file (full content transfer + timeline UID CLAUSEs per contract) | `completed` | LLM_Developer | TK004.1 | `standard_P-STD-005_universal-id-specification.md` | Promotion contract | Created P-STD-005 combined file (11 CLAUSEs, 2 ADRs, substandard architecture); corrected Specification Index rows 6–7 per GATE-003 FINDING-001 (Situation A rework). |
| TK006 | `P-PH000-ST001-AC006-TK006` | Mark T102-STD-005 as superseded + establish alias window | `completed` | LLM_Developer | TK005 | `T102-STD-005_id-specification-rules.md` | `T102-STD-005-CLAUSE-003A/003B` | T102-STD-005 marked superseded with alias window notice and provenance entry. |
| TK007 | `P-PH000-ST001-AC006-TK007` | Update P-STD-001 references (T102-STD-005 → P-STD-005) | `completed` | LLM_Developer | TK005 | `standard_P-STD-001_program-governance-standard.md` | Tier 1 ref update | P-STD-001 External References and all ~21 in-body CLAUSE references updated; zero residual T102-STD-005 refs. |
| TK008 | `P-PH000-ST001-AC006-TK008` | Update Program SPS P-STD-005 row + remaining Tier 1 reference files | `completed` | LLM_Developer | TK005 | `sps_P-PROGRAM.md`, `P-STD-003`, guideline, skills, catalog | Tier 1 ref update | All 5 Tier 1 files updated (SPS, P-STD-003, guideline, skill, catalog); template no-op confirmed. |
| TK009 | `P-PH000-ST001-AC006-TK009` | Amend downstream plans (T104-ST002 AC002, T102-ST005 AC005, T102-ST002 STD-005 scope) | `completed` | LLM_Consultant | TK005 | 3 plan files | Absorption notes | 3 downstream plans amended: T104-ST002-AC002 cancelled, T102-ST005-AC005 cancelled, T102-ST002 scope carve-out. |
| TK010 | `P-PH000-ST001-AC006-TK010` | Produce verification evidence | `completed` | LLM_Reviewer | TK006, TK007, TK008, TK009 | Verification artifact | — | Verification evidence produced at verification_P-PH000-ST001-AC006_tk005-to-tk009.md. |
| GATE-003 | `P-PH000-ST001-AC006-GATE-003` | Gate: Client approval of completed promotion | `completed` | Client | TK010 | Pass/fail | — | FINDING-001 resolved (Specification Index row 6–7 title correction). Gate passed per verification_P-PH000-ST001-AC006_gate-003.md. |

---

## III. TASKS (DETAILED)

### Task TK001: Fix Stale References in T102-STD-005

**Task ID**: `P-PH000-ST001-AC006-TK001`

**Purpose**: Update all stale references to superseded standards (T102-STD-004, T102-STD-009) inside T102-STD-005 to point to their promoted program-level equivalents (P-STD-001).

**Deliverable**: Updated `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-005_id-specification-rules.md`

**Steps**:

1. Read `T102-STD-005_id-specification-rules.md` fully.

2. Apply the following replacements **in this exact order** (more specific first to avoid partial matches):

   **R1**: In CLAUSE-005D Construction section (lines ~198-203), update the 4 examples:
   - `T102-STD-004-CLAUSE-004A` → `P-STD-001-CLAUSE-004A` (2 occurrences — current format and legacy alias)
   - `T102-STD-004-CLAUSE-004` → `P-STD-001-CLAUSE-004` (2 occurrences — current format and legacy alias)

   **R2**: In CLAUSE-005D Scope & Validity Constraints (line ~220), replace the normative reference:
   - `T102-STD-004-CLAUSE-005 (Specification Clauses)` → `P-STD-001-CLAUSE-018 (CLAUSE Construction Requirements)`
   - NOTE: T102-STD-004-CLAUSE-005 was renumbered to P-STD-001-CLAUSE-018 during the P-STD-001 promotion. The implementer MUST verify this mapping by checking P-STD-001's Specification Index.

   **R3**: In CLAUSE-005F Construction section (line ~239), update the example:
   - `T102-STD-004-ADR-001` → `P-STD-001-ADR-001`

   **R4**: In CLAUSE-006 Quality Criteria (line ~261), update the normative reference:
   - `Follow /`T102-STD-004/` body structure strictly` → `Follow /`P-STD-001/` body structure strictly`

   **R5**: In CLAUSE-007 Legacy Standards Migration (line ~274), update the normative reference:
   - `T102-STD-009-CLAUSE-005 (Migration Tolerance)` → `P-STD-001-CLAUSE-017 (Migration Tolerance)`
   - NOTE: T102-STD-009 was merged into P-STD-001. T102-STD-009-CLAUSE-005 maps to P-STD-001-CLAUSE-017. The implementer MUST verify this mapping by checking P-STD-001's Specification Index.

   **R6**: In the `## References` section (line ~299), update:
   - `T102-STD-004 (Specification Standard & Guideline)` → `P-STD-001 (Program Governance Standard)`

   **R7**: In the `## References` section, add T102-STD-009 status note if not already present. Since T102-STD-009 was deprecated/merged into P-STD-001, either:
   - Remove the `T102-STD-009` reference line entirely (if one exists), OR
   - If no explicit T102-STD-009 reference exists, no action needed (the line ~274 reference was the only one, handled by R5)

3. Verify: search the file for any remaining `T102-STD-004` references. There should be ZERO.
4. Verify: search the file for any remaining `T102-STD-009` references. There should be ZERO.

**Success Criteria**:
- [ ] Zero residual `T102-STD-004` references in T102-STD-005
- [ ] Zero residual `T102-STD-009` references in T102-STD-005
- [ ] All replacement targets verified against P-STD-001 Specification Index
- [ ] No other content modified (only stale reference replacements)

---

### Task TK002: Verify ST005-AC005 Deltas Applied

**Task ID**: `P-PH000-ST001-AC006-TK002`

**Purpose**: Verify that the three pending amendments from T102-PH001-ST005-AC005 (Deltas C1, C2, B1) are already applied to T102-STD-005. Based on the current file content (read during SES001), these amendments appear to be present. If any are missing, apply them.

**Steps**:

1. Read `T102-STD-005_id-specification-rules.md` (post-TK001).

2. **Verify Delta C1 (INT promotion enforcement)** — Check CLAUSE-005C for the presence of:
   - "Promotion enforcement" rule: when an INT item is referenced as relied-upon policy in 2+ artifacts or across 2+ Epics, it MUST be promoted to RID/STD/ADR within the next governance review cycle
   - **Expected location**: CLAUSE-005C "Governance Loop" section
   - **Reference**: `analysis_T102-RES-005_cross-scope-coordination-architecture.md` Section III, Delta C1

3. **Verify Delta C2 (INT anti-pattern boundary)** — Check CLAUSE-005C for the presence of:
   - "Anti-pattern boundary": INT MUST NOT be used as a substitute for authoritative indices, registers, or enforceable obligations
   - **Expected location**: CLAUSE-005C "Governance Loop" section
   - **Reference**: `analysis_T102-RES-005_cross-scope-coordination-architecture.md` Section III, Delta C2

4. **Verify Delta B1 (Audit register exception)** — Check CLAUSE-003 for the presence of:
   - "Audit register exception": Concept audit-surface registers MAY reference downstream artifact IDs for inventory/audit purposes when explicitly labeled pointers-only and non-normative
   - **Expected location**: CLAUSE-003 "Directionality" section, as a bullet exception
   - **Reference**: `analysis_T102-RES-006_integration-impact.md` Section III, Delta B1

5. For each delta:
   - If PRESENT: Record "verified — already applied" in the task action
   - If MISSING: Apply the amendment text from the analysis artifact and record the change

**Success Criteria**:
- [ ] Delta C1 verified or applied
- [ ] Delta C2 verified or applied
- [ ] Delta B1 verified or applied
- [ ] T102-PH001-ST005-AC005 scope confirmed as absorbed

---

### Task TK003: Targeted Self-Compliance Audit

**Task ID**: `P-PH000-ST001-AC006-TK003`

**Purpose**: Verify that T102-STD-005 (post-TK001/TK002 fixes) conforms to P-STD-001's combined-file structure requirements before promotion.

**Steps**:

1. Read `T102-STD-005_id-specification-rules.md` (post-TK001/TK002).
2. Read `standard_P-STD-001_program-governance-standard.md` for structural reference.

3. Check against P-STD-001-CLAUSE-001A (Required sections and order):
   - [ ] `# T102-STD-005 — ID Specification & Rules` heading present
   - [ ] `## Specification` present
   - [ ] `## Decision Record` present
   - [ ] `## References` present
   - [ ] `## Provenance` present
   - [ ] Sections in correct order

4. Check against P-STD-001-CLAUSE-018B (CLAUSE format):
   - [ ] Each clause rendered as `n) **<CLAUSE-ID> (<Title>)**`
   - [ ] Subclauses rendered as `* **<CLAUSE-ID> (<Title>)** — <text>` per P-STD-001-CLAUSE-020A

5. Check against P-STD-001-CLAUSE-025 (DR Body Template):
   - [ ] ADR header format: `* **T102-STD-005-ADR-001 (<Title>)** {#anchor}`
   - [ ] Required subheadings: Context, Decision, Alternatives, Consequences
   - [ ] Note: Traceability subheading may be missing (it was added in P-STD-001-CLAUSE-025I which postdates T102-STD-005). Record as a finding for the promotion contract to address.

6. Check against P-STD-001-CLAUSE-002 (Specification Index):
   - [ ] With 7 CLAUSEs (>5), a Specification Index SHOULD be present per CLAUSE-002
   - [ ] If missing, record as a finding for the promotion contract to address

7. Check against P-STD-001-CLAUSE-028 (References & Provenance):
   - [ ] `## References` section contains governing standards as RID-category references
   - [ ] `## Provenance` section lists originating proposals/research

8. Produce a brief compliance report listing:
   - Conformant items (pass)
   - Non-conformant items to remediate during promotion (carry forward to TK004 promotion contract)
   - Items that need attention in the promotion contract but NOT pre-promotion fixes

**Deliverable**: Brief compliance assessment (can be inline in session notes or a separate analysis artifact at `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC006/analysis/analysis_P-PH000-ST001-AC006_pre-promotion-audit.md`)

**Success Criteria**:
- [ ] All P-STD-001 structural requirements checked
- [ ] Findings documented with remediation plan (in-promotion vs deferred)
- [ ] No blocking structural issues that prevent promotion

---

### GATE-001: Client Approval of Pre-Promotion T102-STD-005 State

**Entry Criteria**:
- TK001 complete (stale refs fixed)
- TK002 complete (deltas verified/applied)
- TK003 complete (compliance audit with findings documented)

**Reviewer**: Client

**Exit Criteria**:
- Client confirms T102-STD-005 is clean for promotion
- Client approves compliance findings and agrees with remediation plan

---

### Task TK004: Author Promotion Contract Proposal

**Task ID**: `P-PH000-ST001-AC006-TK004`

**Purpose**: Author a decision-complete promotion contract (like the P-STD-001 precedent) so that TK005 execution is fully mechanical.

**Deliverable**: `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC006/proposal/proposal_P-PH000-ST001-AC006_promotion-contract-t102-std-005-to-p-std-005.md`

**Inputs Required**:
- `T102-STD-005_id-specification-rules.md` (post-TK001/TK002, source standard)
- `standard_P-STD-001_program-governance-standard.md` (structural exemplar + promotion lifecycle CLAUSEs)
- `proposal_P-PH000-ST001-AC002_promotion-contract-t102-std-004-to-p-std-001.md` (format precedent)
- `analysis_P-PH000-ST001-AC006_pre-promotion-audit.md` (TK003 compliance findings)
- T104 session decisions: `T104-PH001-ST000-SES001` (DEC003: Stable UIDs, DEC004: Initiative Phases, DEC005: LINK-### indirection)
- `plan_T104-PH001-ST002.md` AC002 section (timeline UID CLAUSE scope)

**The proposal MUST contain** (following the P-STD-001 precedent structure):

1. **CLAUSE Re-identification Mapping** (1:1 for existing 7 CLAUSEs):
   - `T102-STD-005-CLAUSE-001` → `P-STD-005-CLAUSE-001`
   - `T102-STD-005-CLAUSE-002` → `P-STD-005-CLAUSE-002`
   - `T102-STD-005-CLAUSE-003` → `P-STD-005-CLAUSE-003`
   - `T102-STD-005-CLAUSE-003A` → `P-STD-005-CLAUSE-003A`
   - `T102-STD-005-CLAUSE-003B` → `P-STD-005-CLAUSE-003B`
   - `T102-STD-005-CLAUSE-004` → `P-STD-005-CLAUSE-004`
   - `T102-STD-005-CLAUSE-005` → `P-STD-005-CLAUSE-005`
   - `T102-STD-005-CLAUSE-005A` → `P-STD-005-CLAUSE-005A`
   - `T102-STD-005-CLAUSE-005B` → `P-STD-005-CLAUSE-005B`
   - `T102-STD-005-CLAUSE-005C` → `P-STD-005-CLAUSE-005C`
   - `T102-STD-005-CLAUSE-005D` → `P-STD-005-CLAUSE-005D`
   - `T102-STD-005-CLAUSE-005E` → `P-STD-005-CLAUSE-005E`
   - `T102-STD-005-CLAUSE-005F` → `P-STD-005-CLAUSE-005F`
   - `T102-STD-005-CLAUSE-006` → `P-STD-005-CLAUSE-006`
   - `T102-STD-005-CLAUSE-007` → `P-STD-005-CLAUSE-007`
   - `T102-STD-005-ADR-001` → `P-STD-005-ADR-001`

2. **Ordered Replacement Rules** (R1–Rn, specific-first like P-STD-001):
   - R1: `T102-STD-005-CLAUSE-` → `P-STD-005-CLAUSE-`
   - R2: `T102-STD-005-ADR-` → `P-STD-005-ADR-`
   - R3: `T102-STD-005` (standalone) → `P-STD-005`
   - R4: `t102-std-005` (lowercase, anchors) → `p-std-005`
   - NOTE: R1-R4 are applied to the P-STD-005 combined file ONLY. The T102-STD-005 source file is NOT modified by these rules (it gets a supersession notice instead).

3. **Timeline UID CLAUSEs** (new content absorbed from T104-STD-002 scope):
   - Author normative text for new CLAUSEs to be inserted into P-STD-005 (appended after CLAUSE-007):
     - `P-STD-005-CLAUSE-008 (Timeline UID Schema)` — regex patterns for PH/ST/AC/TK entities
     - `P-STD-005-CLAUSE-009 (UID-vs-Seq Decoupling)` — UIDs never change; Seq is display order
     - `P-STD-005-CLAUSE-010 (LINK Indirection System)` — LINK-### for register deliverables
     - `P-STD-005-CLAUSE-011 (Timeline File Naming)` — file naming conventions derived from UIDs
   - **Authoring mandate (SES002-DEC002)**: The LLM_Consultant SHALL derive normative CLAUSE text from:
     - `T104-PH001-ST000-SES001` decisions (DEC003: Stable UIDs, DEC004: Initiative Phases, DEC005: LINK-### indirection)
     - `plan_T104-PH001-ST002.md` AC002 task descriptions (CLAUSE scope for UID Schema, UID-vs-Seq Decoupling, LINK Indirection, File Naming)
     - Observed plan/notes file naming patterns across T102 and T104 workspaces
   - The proposal file is the delivery surface; GATE-002 is the quality checkpoint. Any specification ambiguities that cannot be resolved from the available inputs above MUST be flagged as open questions in the proposal for client resolution at GATE-002.
   - The CLAUSEs MUST be authored in P-STD-001-CLAUSE-018B format with subclauses in CLAUSE-020A format.
   - **Session sub-token requirement (inline amendment, 2026-02-24)**: CLAUSE-008 MUST include a subclause for session-scoped item UIDs (DP, DEC, ACT, OQ) as defined in `guideline_workspace_notes.md` §2.2. Specifically:
     - A new `P-STD-005-CLAUSE-008J (Session Item UID)` subclause MUST define the composition pattern `<Session-UID>-<TYPE>###` where `<TYPE>` is one of `DP`, `DEC`, `ACT`, `OQ`.
     - `P-STD-005-CLAUSE-001` Pattern 4 regex MUST accommodate the optional `-<TYPE>###` suffix after `SES###`.
     - `P-STD-005-CLAUSE-008I (Composition rules)` MUST document that Session UIDs may be extended with session item type tokens.
     - Source: `guideline_workspace_notes.md` §2.2 (Item ID format: `[Session-Prefix]-[TYPE][###]`; types: DP, DEC, ACT, OQ; sequences reset per session).

4. **ADR-002 body** (promotion decision):
   - Authored in P-STD-001-CLAUSE-025A header format
   - With P-STD-001-CLAUSE-025B required subheadings (Context, Decision, Alternatives, Consequences, Traceability)
   - Consequences in (+)/(±)/(-) format per P-STD-001-CLAUSE-025G
   - Documents: promotion from T102-STD-005, absorption of T104-STD-002 scope, unification rationale

5. **ADR Index** (2 rows):
   - P-STD-005-ADR-002 (Promotion from T102-STD-005) — `accepted`
   - P-STD-005-ADR-001 (ID Specification & Rules) — `superseded`

6. **Specification Index** (if >5 CLAUSEs — with 11 CLAUSEs, required):
   - Schema per P-STD-001-CLAUSE-002A: `| # | Substandard | CLAUSE ID | Title | Description |`
   - **Substandard architecture mandate (SES002-DEC003)**: P-STD-005 SHALL use substandard architecture with at minimum two substandards:
     - **Substandard A**: Workscope ID Governance (existing CLAUSEs 001–007, transferred from T102-STD-005)
     - **Substandard B**: Timeline UID Schema (new CLAUSEs 008–011, absorbed from T104-STD-002 scope)
   - The exact substandard naming, any further subdivision, and the Specification Index table MUST be proposed in the promotion contract for client approval at GATE-002.

7. **Alias Window Terms**:
   - Scope: all `T102-STD-005-CLAUSE-*` references
   - Duration: until migration completion milestone (define)
   - Rules: per P-STD-001-CLAUSE-030C

8. **Supersession Notice Text** (for TK006 to insert into T102-STD-005)

9. **External References Table** (for P-STD-005's `## References` section):
   - List all referenced IDs with titles, scopes, and source paths

10. **Tier 1 Reference Update File List** with specific replacement instructions per file

11. **TK003 Compliance Findings Remediation** — how each finding from the pre-promotion audit is addressed in the promotion

12. **P-STD-001 back-reference update specification** — exact changes to P-STD-001's External References table and in-body refs

**Success Criteria**:
- [ ] Promotion contract follows the P-STD-001 contract precedent structure
- [ ] CLAUSE re-identification mapping is complete (all 7 + subclauses)
- [ ] Timeline UID CLAUSEs are normative-ready
- [ ] ADR-002 body follows P-STD-001-CLAUSE-025 format
- [ ] Specification Index is present (>5 CLAUSEs)
- [ ] Alias window terms are explicit
- [ ] Tier 1 reference update plan is bounded and file-specific
- [ ] P-STD-001 back-reference updates are specified

---

### GATE-002: Client Approval of Promotion Contract

**Entry Criteria**: TK004 deliverable complete

**Reviewer**: Client

**Exit Criteria**: Client approves contract; no blocking issues

---

### Task TK004.1: Revise Promotion Contract — Add Session Sub-Tokens

**Task ID**: `P-PH000-ST001-AC006-TK004.1`

**Purpose**: Address the scope gap identified at GATE-002: the promotion contract is missing session-scoped item UIDs (DP/DEC/ACT/OQ) as defined in `guideline_workspace_notes.md` §2.2. These tokens compose on top of Session UIDs and are foundational to the workspace notes ID system.

**Classification**: Situation B (Scope Gap) per `guideline_workspace_plan.md` §VI.G — the AC006 plan did not originally specify session sub-tokens; the developer faithfully implemented the plan as written.

**Deliverable**: Revised `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC006/proposal/proposal_P-PH000-ST001-AC006_promotion-contract-t102-std-005-to-p-std-005.md`

**Steps**:
1. **Update §VI (CLAUSE-001 amendment)** — Pattern 4 regex:
   - Replace the Pattern 4 regex to add optional session item suffix after `SES\\d{3}`:
   - Old: `^(?:P|T\\d{3}(?:[A-Z]\\d*)?)-PH\\d{3}(?:-ST\\d{3}(?:-AC\\d{3}(?:\\.\\d+)?(?:-TK\\d{3})?)?)?(?:-(?:SES\\d{3}|GATE-\\d{3}))?$`
   - New: `^(?:P|T\\d{3}(?:[A-Z]\\d*)?)-PH\\d{3}(?:-ST\\d{3}(?:-AC\\d{3}(?:\\.\\d+)?(?:-TK\\d{3})?)?)?(?:-(?:SES\\d{3}(?:-(?:DP|DEC|ACT|OQ)\\d{3})?|GATE-\\d{3}))?$`
   - Add session item examples:
     `- Examples (Session Item): \`P-PH000-ST001-AC006-SES003-DP001\`, \`P-PH000-ST001-AC006-SES003-DEC001\``

2. **Update §VII (CLAUSE-008)** — Add CLAUSE-008J subclause:
   - Insert after CLAUSE-008I:
   ```
   * **P-STD-005-CLAUSE-008J (Session Item UID)** — Session item UIDs MUST be expressed by appending `-<TYPE>###` to a Session UID, where `<TYPE>` is one of: `DP` (Discussion Point), `DEC` (Decision), `ACT` (Action), `OQ` (Open Question). Sequences (`###`) reset per session file per `guideline_workspace_notes.md` §2.2. Regex: `^(?:P|T\\d{3}(?:[A-Z]\\d*)?)-PH\\d{3}(?:-ST\\d{3}(?:-AC\\d{3}(?:\\.\\d+)?(?:-TK\\d{3})?)?)?-SES\\d{3}-(?:DP|DEC|ACT|OQ)\\d{3}$`. Examples: `P-PH000-ST001-AC006-SES003-DP001`, `T104-PH001-ST002-SES001-DEC001`, `P-PH000-ST001-AC006-SES003-ACT001`.
   ```

3. **Update §VII (CLAUSE-008I)** — Expand composition rules:
   - Old: `Qualifiers MUST NOT appear in the middle of the UID.`
   - New: `Session UIDs (\`SES\`) MAY be further extended with a session item type token (see CLAUSE-008J). Qualifiers and their extensions MUST NOT appear in the middle of the UID.`

4. **Bump version** to `v1.1.0` and add changelog entry referencing the plan amendment.

**Success Criteria**:
- [ ] CLAUSE-001 Pattern 4 regex accommodates `SES###-TYPE###` pattern
- [ ] CLAUSE-001 Pattern 4 examples include session item UIDs
- [ ] CLAUSE-008J subclause defines session item UID composition (DP/DEC/ACT/OQ)
- [ ] CLAUSE-008I updated to reference CLAUSE-008J
- [ ] Proposal changelog documents the revision
- [ ] No other normative content modified

---

### Task TK005: Create P-STD-005 Combined File

**Task ID**: `P-PH000-ST001-AC006-TK005`

**Purpose**: Execute the promotion contract mechanically.

**Deliverable**: `prompt/artifacts/tasks/P/standard/standard_P-STD-005_universal-id-specification.md`

**Steps** (following P-STD-001 precedent):
1. Create directory `prompt/artifacts/tasks/P/standard/` if it doesn't exist.
2. Copy the ENTIRE content of `T102-STD-005_id-specification-rules.md` into the new file at the target path.
2b. **RES token scope absorption (SES002-DEC004)**: In CLAUSE-002 (Taxonomy & Terminology), locate the `RES` row in the token table and update the `Allowed Scope` column from `I, E, F` to `P, I, E, F`. This absorbs the `P-PH000-ST001-AC001` RES scope change into the P-STD-005 content transfer. No other token table rows are modified.
3. Apply replacement rules R1–R4 **in order** per the promotion contract. Verify no external references (P-STD-001, T102-CON-009, T102-STD-003, T102-STD-006) were modified (these are External References and MUST remain unchanged).
4. Replace the main heading: `# P-STD-005 — Universal ID Specification {#p-std-005-universal-id-specification}`
5. Insert timeline UID CLAUSEs (CLAUSE-008 through CLAUSE-011) after CLAUSE-007, using exact text from the promotion contract.
6. Add Specification Index after the `## Specification` heading using the table from the promotion contract.
7. Replace the ADR Index with the corrected table from the promotion contract.
8. Insert ADR-002 body BEFORE ADR-001 body (current-first ordering per P-STD-001-CLAUSE-023C), using exact text from the promotion contract.
9. Replace the `## References` section with the External References table from the promotion contract.
10. Replace the `## Provenance` section with the promotion provenance template from the promotion contract.
11. Apply any TK003 compliance remediation items specified in the promotion contract.

**Success Criteria**:
- [ ] File at correct path
- [ ] 11 CLAUSEs present (7 transferred + 4 new timeline UID)
- [ ] CLAUSE rendering conforms to P-STD-001-CLAUSE-018B / CLAUSE-020A
- [ ] 2 ADRs present (ADR-001 superseded, ADR-002 accepted)
- [ ] ADR-002 placed first per CLAUSE-023C
- [ ] ADR-002 follows CLAUSE-025 format with (+)/(±)/(-) consequences
- [ ] ADR Index has exactly one accepted ADR
- [ ] Specification Index present with correct schema
- [ ] No residual T102-STD-005 self-references (only in Provenance/External References)
- [ ] External References table complete
- [ ] P-STD-001-CLAUSE-001A canonical structure followed
- [ ] RES token Allowed Scope updated to `P, I, E, F` (absorption of AC001 scope per SES002-DEC004)

---

### Task TK006: Mark T102-STD-005 as Superseded + Alias Window

**Task ID**: `P-PH000-ST001-AC006-TK006`

**Purpose**: Formally supersede the initiative-scoped standard.

**Deliverable**: Updated `T102-STD-005_id-specification-rules.md`

**Steps**:
1. Insert the supersession notice from the promotion contract immediately AFTER the main heading and BEFORE `## Specification`.
2. Do NOT modify any normative content. All 7 CLAUSEs and 1 ADR remain intact as historical record.
3. Add Provenance supersession entries at the bottom (append to or update existing Provenance section).

**Success Criteria**:
- [ ] Supersession notice present after heading
- [ ] All normative content preserved
- [ ] Alias window terms documented
- [ ] Provenance updated (Superseded By, Date, Promotion Decision)

---

### Task TK007: Update P-STD-001 References

**Task ID**: `P-PH000-ST001-AC006-TK007`

**Purpose**: Update the most critical downstream consumer (P-STD-001) to reference P-STD-005 instead of T102-STD-005.

**Deliverable**: Updated `standard_P-STD-001_program-governance-standard.md`

**Steps**:
1. Read P-STD-001 fully.
2. In the `## References` section (External References table):
   - Change `T102-STD-005` row: update ID to `P-STD-005`, Title to `Universal ID Specification`, Scope to `Program (P)`, Source Path to `prompt/artifacts/tasks/P/standard/standard_P-STD-005_universal-id-specification.md`
   - NOTE: This is now an internal reference (Program → Program), not a cross-scope reference. The table heading should reflect this if it currently says "External References (Cross-Scope)".

3. In the `## Specification` section, apply the following replacement throughout:
   - `T102-STD-005-CLAUSE-` → `P-STD-005-CLAUSE-`
   - `T102-STD-005` (standalone) → `P-STD-005`
   - IMPORTANT: Apply specific-first to avoid partial matches.
   - Expected ~21 replacements across CLAUSEs 003F, 009A-D, 011A, 012B, 018A-E, 019A, 020A, 022A-B, 023B, 024E, 028A, 029C, 030A-C.

4. In the `## Decision Record` section:
   - Update any T102-STD-005 references in ADR-003 Traceability and Consequences sections.

5. In the `## Provenance` section:
   - Update alias window note if it references T102-STD-005.

6. Verify: search for remaining `T102-STD-005` references. Only allowed in historical/traceability context (e.g., ADR-003 documenting the P-STD-001 promotion process which referenced T102-STD-005-CLAUSE-003A).

**Success Criteria**:
- [ ] External References table updated (P-STD-005, Program scope, correct path)
- [ ] All ~21 in-body normative CLAUSE references updated
- [ ] No inappropriate residual T102-STD-005 references
- [ ] File remains structurally valid

---

### Task TK008: Update Program SPS + Remaining Tier 1 Files

**Task ID**: `P-PH000-ST001-AC006-TK008`

**Purpose**: Update all remaining Tier 1 reference files.

**Steps**:

**8A — Program SPS** (`sps_P-PROGRAM.md`):
1. Update the `P-STD-005` row in STD Index:
   - `Status`: `planned` → `draft`
   - `Supersedes`: `—` → `T102-STD-005`
   - `Reference`: Update to `prompt/artifacts/tasks/P/standard/standard_P-STD-005_universal-id-specification.md`
   - `Verification`: Update as appropriate
2. Update the `P-STD-005` body text in Section III.B.8:
   - Update to reflect completed promotion (not "pending promotion")
   - Update External Reference line
3. Update `P-NOTE-001` if it references T102-STD-005.
4. Append changelog entry.

**8B — P-STD-003** (`P-STD-003_governance-standards-and-dr-index.md`):
1. Read file; locate T102-STD-005 references.
2. Replace with P-STD-005 equivalents.

**8C — Guideline** (`guideline_standard_specs.md`):
1. Read file; locate any T102-STD-005 references.
2. Replace with P-STD-005 equivalents.
3. Update changelog if modified.

**8D — Skill** (`skills/t102-adr-005-id-spec/SKILL.md`):
1. Read the skill file.
2. Update all T102-STD-005 references to P-STD-005.
3. Add a deprecation notice at the top of the skill file: `> **Deprecated**: This skill references `T102-STD-005` which has been superseded by `P-STD-005`. The skill directory name `t102-adr-005-id-spec` is retained for backward compatibility. See `prompt/artifacts/tasks/P/standard/standard_P-STD-005_universal-id-specification.md`.`
4. Do NOT rename the skill directory. Per SES002-DEC005, the skill is deprecated and directory renaming adds no value.

**8E — Skills Catalog** (`documentation/adr_skills_catalog.md`):
1. Read file; update T102-STD-005 references to P-STD-005.
2. Update skill name if renamed in 8D.

**Success Criteria**:
- [ ] SPS P-STD-005 row updated (status, supersedes, reference)
- [ ] SPS body text and notes updated
- [ ] P-STD-003 refs updated
- [ ] Guideline refs updated
- [ ] Skill file refs updated + deprecation notice added (directory retained per SES002-DEC005)
- [ ] Skills catalog updated

---

### Task TK009: Amend Downstream Plans

**Task ID**: `P-PH000-ST001-AC006-TK009`

**Purpose**: Update three downstream plans to reflect that their T102-STD-005-related scope has been absorbed into P-PH000-ST001-AC006.

**Steps**:

**9A — T104-PH001-ST002** (`plan_T104-PH001-ST002.md`):
1. Read file.
2. In the Activity Register, update AC002:
   - `Status`: `planned` → `cancelled`
   - Add `Action` column if not present, or update existing Action: `Scope absorbed into P-PH000-ST001-AC006; timeline UID content authored directly at Program scope as P-STD-005 CLAUSEs 008-011. OQ-PH1-001 invalidated.`
3. In the AC002 section body, add a note at the top:
   ```
   > **Absorption Notice**: This activity has been absorbed into `P-PH000-ST001-AC006` (Promote T102-STD-005 to P-STD-005). Timeline UID content is authored directly into P-STD-005 at Program scope. See `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC006/plan_P-PH000-ST001-AC006.md`.
   ```
4. Append changelog entry:
   ```
   | v1.5.0 | 2026-02-22 | Amendment | AC002 (Timeline UID Convention) cancelled: scope absorbed into P-PH000-ST001-AC006 (P-STD-005 promotion). Timeline UID CLAUSEs authored directly at Program scope. OQ-PH1-001 invalidated. Evidence: raw_P-PH000-ST001-AC006-SES001.txt |
   ```

**9B — T102-PH001-ST005** (`plan_T102-PH001-ST005.md`):
1. Read file.
2. In the Activity Register, update AC005:
   - `Status`: `planned` → `cancelled`
   - Update Action (if column exists) or add note: `Scope absorbed into P-PH000-ST001-AC006; deltas verified as pre-promotion task (TK002). T102-STD-005 amendments applied before promotion to P-STD-005.`
3. In the AC005 section body, add absorption notice:
   ```
   > **Absorption Notice**: This activity has been absorbed into `P-PH000-ST001-AC006` (Promote T102-STD-005 to P-STD-005). Deltas C1, C2, and B1 verified/applied as pre-promotion tasks. See `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC006/plan_P-PH000-ST001-AC006.md`.
   ```
4. Append changelog entry:
   ```
   | v3.3.0 | 2026-02-22 | Amendment | AC005 (Amend T102-STD-005) cancelled: scope absorbed into P-PH000-ST001-AC006 (P-STD-005 promotion). Deltas C1/C2/B1 verified as pre-promotion tasks. Evidence: raw_P-PH000-ST001-AC006-SES001.txt |
   ```

**9C — T102-PH001-ST002** (`plan_T102-PH001-ST002.md`):
1. Read file.
2. In the Executive Summary or Stream Outline, add a scoping note:
   ```
   > **Scope Carve-Out**: T102-STD-005-specific baselining scope has been absorbed into `P-PH000-ST001-AC006` (P-STD-005 promotion). AC000-AC004 activities continue for T102-STD-001, STD-003, STD-006, STD-007 (and STD-009 legacy). T102-STD-005 gap analysis, verification, and SSOT alignment are handled by the P-STD-005 promotion activity.
   ```
3. Append changelog entry:
   ```
   | v1.1.0 | 2026-02-22 | Amendment | STD-005-specific scope carved out: absorbed into P-PH000-ST001-AC006 (P-STD-005 promotion). AC000-AC004 continue for remaining T102-STDs. Evidence: raw_P-PH000-ST001-AC006-SES001.txt |
   ```

**Success Criteria**:
- [ ] T104-PH001-ST002 AC002 status = `cancelled` with absorption note
- [ ] T102-PH001-ST005 AC005 status = `cancelled` with absorption note
- [ ] T102-PH001-ST002 scoping note added for STD-005 carve-out
- [ ] All three changelogs updated with evidence reference

---

### Task TK010: Produce Verification Evidence

**Task ID**: `P-PH000-ST001-AC006-TK010`

**Purpose**: Document evidence that the promotion was executed per the contract.

**Deliverable**: `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC006/verification/verification_P-PH000-ST001-AC006_tk005-to-tk009.md`

**Steps**:
1. Create verification checklist covering all success criteria from TK005, TK006, TK007, TK008, TK009.
2. For each criterion, document pass/fail evidence.
3. Specifically verify:
   - P-STD-005 CLAUSE count (expected: 11 = 7 transferred + 4 new)
   - P-STD-005 ADR count (expected: 2 — ADR-001 superseded, ADR-002 accepted)
   - Zero residual T102-STD-005 self-references in P-STD-005 (except Provenance/External Refs)
   - P-STD-001 references updated (search for T102-STD-005 in P-STD-001)
   - SPS P-STD-005 row correct
   - T102-STD-005 supersession notice present
   - All three downstream plans amended
4. Confirm raw transcript existence: `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC006/raw/raw_P-PH000-ST001-AC006-SES001.txt`

**Success Criteria**:
- [ ] Verification checklist complete
- [ ] All TK005-TK009 success criteria verified with evidence

---

### GATE-003: Client Approval of Completed Promotion

**Entry Criteria**:
- TK005-TK010 deliverables complete
- Verification artifact exists

**Reviewer**: Client

**Exit Criteria**:
- All verification findings resolved
- Client approves completed promotion
- Activity P-PH000-ST001-AC006 may be marked `completed`

---

## IV. LINKS REGISTER

| Link Type | Target | Path |
|:--|:--|:--|
| Plan (this file) | AC006 Activity Plan | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC006/plan_P-PH000-ST001-AC006.md` |
| Plan | P Stream Plan | `prompt/artifacts/tasks/P/workspace/PH000/ST001/plan_P-PH000-ST001.md` |
| SSOT | Program SPS | `prompt/artifacts/tasks/P/ssot/sps_P-PROGRAM.md` |
| Reference | P-STD-001 (golden exemplar) | `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md` |
| Reference | T102-STD-005 (source standard) | `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-005_id-specification-rules.md` |
| Reference | P-STD-001 promotion contract (precedent) | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC002/proposal/proposal_P-PH000-ST001-AC002_promotion-contract-t102-std-004-to-p-std-001.md` |
| Reference | P-STD-001 promotion activity plan (precedent) | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC002/plan_P-PH000-ST001-AC002.md` |
| Reference | RES-005 analysis (delta source) | `prompt/artifacts/tasks/T102/consultant/workspace/analysis/analysis_T102-RES-005_cross-scope-coordination-architecture.md` |
| Reference | RES-006 analysis (delta source) | `prompt/artifacts/tasks/T102/consultant/workspace/analysis/analysis_T102-RES-006_integration-impact.md` |
| Reference | T104-PH001-ST002 plan (AC002 absorption) | `prompt/artifacts/tasks/T104/workspace/PH001/ST002/plan_T104-PH001-ST002.md` |
| Reference | T102-PH001-ST005 plan (AC005 absorption) | `prompt/artifacts/tasks/T102/consultant/workspace/plan/plan_T102-PH001-ST005.md` |
| Reference | T102-PH001-ST002 plan (scope carve-out) | `prompt/artifacts/tasks/T102/consultant/workspace/plan/plan_T102-PH001-ST002.md` |
| Evidence | SES001 raw transcript | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC006/raw/raw_P-PH000-ST001-AC006-SES001.txt` |
| Evidence | SES002 raw transcript | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC006/raw/raw_P-PH000-ST001-AC006-SES002.txt` |

---

## V. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-02-22 | Initial | Activity plan created per SES001 consultation. Fix-first/promote-clean methodology; absorbs T104-PH001-ST002-AC002, T102-PH001-ST005-AC005, and STD-005-specific scope from T102-PH001-ST002. Evidence: `raw_P-PH000-ST001-AC006-SES001.txt` |
| v1.1.0 | 2026-02-22 | Amendment | SES002 pre-commissioning amendments: TK004 — substandard architecture mandated (DEC003), hybrid authoring clarified for timeline UID CLAUSEs (DEC002); TK005 — RES token scope change absorbed from AC001 (DEC004); TK008-8D — skill directory retained as deprecated (DEC005). Evidence: `raw_P-PH000-ST001-AC006-SES002.txt` |
| v1.2.0 | 2026-02-24 | Amendment | Inline plan amendment: (1) added session sub-token requirement to TK004 Steps item 3 (DP/DEC/ACT/OQ per guideline_workspace_notes.md §2.2); (2) added TK004.1 sub-task for proposal revision; (3) updated TK005 Depends On from GATE-002 to TK004.1. Classification: Situation B (Scope Gap) per guideline_workspace_plan.md §VI.G. Source: Client QA at GATE-002 (2026-02-24). |
| v1.3.0 | 2026-02-24 | Amendment | GATE-003 resolution: corrected P-STD-005 Specification Index rows 6–7 (Content Quality, ID Stability & Immutability) per FINDING-001 (Situation A rework under TK005). Updated task register to terminal statuses per guideline_workspace_plan.md §IV.C. |
