---
artifact_type: 'PLAN'
planning_level: 'ACTIVITY'
initiative_id: 'P'
initiative_code: 'PROGRAM'
phase: '0'
stream_id: 'P-PH000-ST001'
activity_id: 'P-PH000-ST001-AC003'
version: '0.3.2'
date: '2026-02-27'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
governance_rules: 'prompt/templates/consultant/workspace/workspace_documentation_rules.md'
parent_plan: 'prompt/artifacts/tasks/P/workspace/PH000/ST001/plan_P-PH000-ST001.md'
---

# PLAN: P (PROGRAM) — Phase 0 / Stream ST001 / Activity AC003: Author P-STD-002 (Program Status Standard)


## I. EXECUTIVE SUMMARY

**Purpose**: Author `P-STD-002` (Program Status Standard) as a program-wide status governance standard covering: canonical 7-state status vocabulary with transition rules, health/RAG assessment requirements, unified dependency visibility schema, evidence linkage protocol, update protocol with role accountability, and status artifact specification. This standard is a prerequisite for authoring the program status artifact in `P-PH000-ST002`.

**Non-goal**: This activity does not create `status_program.md` (deferred to P-PH000-ST002-AC002) or execute repo-wide guideline retrofits beyond the explicit cascade task (TK006).

---

## II. ACTIVITY OUTLINE

**Activity ID**: `P-PH000-ST001-AC003`
**Objective**: Produce a P-STD-001-conformant combined standard-specification file that establishes program-wide status governance semantics and is accepted by the Client.
**Execution Mode**: SEQUENTIAL
**Depends On**: `P-PH000-ST004-AC001` (P-RES-001 integration sign-off via GATE-003) + `P-PH000-ST004-AC002` (P-RES-002 integration sign-off via GATE-003)

**Context**:
- `prompt/artifacts/tasks/P/standard/standard_P-STD-002_program-status-standard.md` (deliverable — created)
- `prompt/artifacts/tasks/P/ssot/sps_P-PROGRAM.md` (P-STD-002 row update)
- `prompt/templates/consultant/standards/guideline_standard_specs.md` (authoring rules)
- `prompt/templates/consultant/standards/template_standard_specs.md` (structural skeleton)
- `prompt/templates/consultant/workspace/guideline_workspace_plan.md` (cascade target)
- `prompt/artifacts/tasks/P/workspace/PH000/ST004/analysis/analysis_P-PH000-ST004-AC001-TK003_integration-recommendations-P-RES-001.md` (P-RES-001 integration recommendations)
- `prompt/artifacts/tasks/P/workspace/PH000/ST004/analysis/analysis_P-PH000-ST004-AC002-TK003_integration-recommendations-P-RES-002.md` (P-RES-002 integration recommendations)
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/proposal/proposal_P-PH000-ST001-AC003-TK001_cdr-resolution.md` (CDR resolution proposal — TK001 deliverable)

### Task Register

| Task | Task ID | Name | Status | Owner | Depends On | Target | Reference | Action |
|:--|:--|:--|:--|:--|:--|:--|:--|:--|
| TK000 | `P-PH000-ST001-AC003-TK000` | Confirm sps_P P-CON-003 amendment applied | `completed` | LLM_Consultant | — | sps_P | DEC-003 | Verified in sps_P (P-CON-003 updated) |
| TK001 | `P-PH000-ST001-AC003-TK001` | Ingest P-RES-001 and P-RES-002 integration recommendations, map to CLAUSE domains, and produce CDR resolution proposal | `completed` | LLM_Consultant | ST004-AC001-GATE-003 + ST004-AC002-GATE-003 | proposal/ + AC003/analysis/ | P-RES-001 + P-RES-002 analyses | Client confirmed defaults (2026-02-27) |
| TK001.1 | `P-PH000-ST001-AC003-TK001.1` | Verify TK001 deliverables — CDR review and readiness assessment for TK002 | `completed` | LLM_Consultant | TK001 | AC003/verification/ | guideline_workspace_verification | CONDITIONAL PASS; APPROVE WITH CONDITIONS (2026-02-27) |
| TK002 | `P-PH000-ST001-AC003-TK002` | Draft P-STD-002 combined file: Specification section (54 CLAUSE themes across 5 domains) | `completed` | LLM_Consultant | TK001.1 | `prompt/artifacts/tasks/P/standard/standard_P-STD-002_program-status-standard.md` | `prompt/artifacts/tasks/P/standard/standard_P-STD-002_program-status-standard.md` | Authored P-STD-002 Specification (54 CLAUSEs) per TK002. Evidence: `dev-report_P-PH000-ST001-AC003_tk002-tk003-execution_2026-02-27.md` |
| TK003 | `P-PH000-ST001-AC003-TK003` | Draft P-STD-002-ADR-001 in Decision Record section (address 13 binding CDR decisions) | `completed` | LLM_Consultant | TK002 | `prompt/artifacts/tasks/P/standard/standard_P-STD-002_program-status-standard.md` | `prompt/artifacts/tasks/P/standard/standard_P-STD-002_program-status-standard.md` | Authored embedded `P-STD-002-ADR-001` per TK003. Evidence: `dev-report_P-PH000-ST001-AC003_tk002-tk003-execution_2026-02-27.md` |
| TK004 | `P-PH000-ST001-AC003-TK004` | Produce GATE-001 verification artifact (includes validation vs P-STD-001 authoring rules) | `completed` | LLM_Reviewer | TK003 | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/verification/verification_P-PH000-ST001-AC003_gate-001.md` | `prompt/templates/consultant/workspace/guideline_workspace_verification.md` | Verification complete (v1.0.1). Verdict: PASS. GDR: Client Decision pending. |
| GATE-001 | `P-PH000-ST001-AC003-GATE-001` | **Gate: Client acceptance of P-STD-002**. Entry: TK004 verification complete (verdict issued; GDR pending). Reviewer: Client. Exit: explicit acceptance recorded. | `planned` | Client | TK004 | — | — | — |
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

### Task TK001: Ingest Combined Research Recommendations and Produce CDR Resolution Proposal

**Task ID**: `P-PH000-ST001-AC003-TK001`

**Purpose**: Extract and map combined P-RES-001 and P-RES-002 research findings to P-STD-002 CLAUSE domains, and produce a CDR resolution proposal for Client confirmation.

**Deliverables**:
- Combined CLAUSE theme mapping with all 54 themes assigned to domain + theme IDs (A-#/B-#/C-#/D-#/E-#). Final `P-STD-002-CLAUSE-###` numbering is assigned in TK002.
- CDR resolution proposal: `prompt/artifacts/tasks/P/workspace/PH000/ST001/proposal/proposal_P-PH000-ST001-AC003-TK001_cdr-resolution.md`
- CLAUSE theme mapping artifact: `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/analysis/analysis_P-PH000-ST001-AC003-TK001_clause-theme-mapping.md`

**Inputs Required**:
- `prompt/artifacts/tasks/P/workspace/PH000/ST004/analysis/analysis_P-PH000-ST004-AC001-TK003_integration-recommendations-P-RES-001.md` — P-RES-001 integration recommendations (baseline: 41 CLAUSE themes, 9 decisions)
- `prompt/artifacts/tasks/P/workspace/PH000/ST004/analysis/analysis_P-PH000-ST004-AC002-TK003_integration-recommendations-P-RES-002.md` — P-RES-002 integration recommendations (complement: 13 CLAUSE themes, 4 decisions, combined synthesis)

**Combined CLAUSE domain totals**:
- **P-STD-002A — Status Vocabulary**: 11 CLAUSE themes (9 baseline + 2 P-RES-002: execution posture fields, manual-gate crosswalk)
- **P-STD-002B — Health Assessment**: 7 CLAUSE themes (6 baseline + 1 P-RES-002: allowed-failure health impact rule)
- **P-STD-002C — Dependency Visibility**: 11 CLAUSE themes (9 baseline + 2 P-RES-002: orchestration reference fields, category taxonomy extension)
- **P-STD-002D — Update Protocol**: 13 CLAUSE themes (9 baseline + 4 P-RES-002: repo-verifiable evidence, evidence type taxonomy extension, aggregation policy, silent allowed-failure prohibition)
- **P-STD-002E — Status Artifact**: 12 CLAUSE themes (8 baseline + 4 P-RES-002: execution reference schema, aggregation policy field, execution posture fields, MVAT)

**Steps**:
1. Read both integration recommendation packages in full
2. For each CLAUSE domain, consolidate the combined CLAUSE theme tables from both analyses
3. Produce a consolidated theme mapping artifact preserving theme IDs and suggested ordering (A-1..E-12). Defer final `P-STD-002-CLAUSE-###` numbering to TK002 authoring.
4. Produce CDR resolution proposal file at `prompt/artifacts/tasks/P/workspace/PH000/ST001/proposal/proposal_P-PH000-ST001-AC003-TK001_cdr-resolution.md` with recommended resolutions for all 13 binding decisions (CDR-01, CDR-02, CDR-04..CDR-14)
5. Present CDR proposal to Client for confirmation
6. Record Client confirmations/overrides in the proposal file

**Success Criteria**:
- [ ] All 54 CLAUSE themes mapped to domain + theme IDs (A-1..E-12), with no gaps
- [ ] No research recommendation from either package is unaddressed
- [ ] CDR resolution proposal produced and presented to Client
- [ ] Client confirmation recorded for all 13 binding CDR entries (CDR-01, CDR-02, CDR-04..CDR-14)

---

### Task TK001.1: Verify TK001 Deliverables — CDR Readiness Review

**Task ID**: `P-PH000-ST001-AC003-TK001.1`

**Purpose**: Confirm that TK001 deliverables (CDR resolution proposal + CLAUSE theme mapping) are complete, internally consistent, and ready to drive TK002 authoring. This task produces an evidence-first verification artifact per `guideline_workspace_verification.md`.

**Deliverable**:
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/verification/verification_P-PH000-ST001-AC003-TK001.1_cdr-review.md`

**Inputs Required**:
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/proposal/proposal_P-PH000-ST001-AC003-TK001_cdr-resolution.md` (TK001 deliverable — Client confirmation of the prior TK001 analysis inputs)
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/analysis/analysis_P-PH000-ST001-AC003-TK001_clause-theme-mapping.md` (TK001 deliverable — 54 theme mapping)
- `prompt/templates/consultant/workspace/guideline_workspace_verification.md` + `prompt/templates/consultant/workspace/template_workspace_verification.md`

**Steps**:
1. Verify the CDR proposal includes 13 binding CDR entries (CDR-01, CDR-02, CDR-04..CDR-14) with Client confirmations recorded.
2. Verify the CLAUSE theme mapping covers all 54 themes (A-1..E-12) with no gaps.
3. Produce the TK001.1 verification artifact documenting findings, verdict, and any gating conditions for TK002 authoring.

**Success Criteria**:
- [ ] TK001.1 verification artifact exists at the canonical path
- [ ] Proposal file verified as present and confirmed for all 13 binding decisions
- [ ] Theme mapping verified as complete for all 54 themes
- [ ] Verification verdict and findings are recorded with remediation guidance where required

---

### Task TK002: Draft P-STD-002 Combined File — Specification Section

**Task ID**: `P-PH000-ST001-AC003-TK002`

**Purpose**: Author the normative Specification section of P-STD-002.

**Deliverable**: `prompt/artifacts/tasks/P/standard/standard_P-STD-002_program-status-standard.md`

**Inputs Required**:
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/analysis/analysis_P-PH000-ST001-AC003-TK001_clause-theme-mapping.md` (primary — 54 themes across 5 domains)
- TK001 CDR resolution proposal with Client-confirmed decisions (primary — 13 CDR entries)
- `prompt/templates/consultant/standards/template_standard_specs.md` — Structural skeleton
- `prompt/templates/consultant/standards/guideline_standard_specs.md` — Authoring rules
- `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md` — Authority chain

**Steps**:
1. Copy `template_standard_specs.md` to deliverable path
2. Fill frontmatter: `artifact_type: 'STANDARD'`, `initiative_id: 'P'`, `std_id: 'P-STD-002'`, `governed_by: 'P-STD-001'`
3. Set heading: `# P-STD-002 — Program Status Standard`
4. Author `## Specification` with substandard headings per planned domains (P-STD-002A through P-STD-002E)
5. For each substandard, incorporate P-RES-002-originated CLAUSE themes per the combined mapping:
   - P-STD-002A: CLAUSE themes A-10 (Execution Posture Fields), A-11 (Manual-Gate Crosswalk)
   - P-STD-002B: CLAUSE theme B-7 (Allowed-Failure Health Impact Rule)
   - P-STD-002C: CLAUSE themes C-10 (Orchestration Reference Fields), C-11 (Category Taxonomy Extension)
   - P-STD-002D: CLAUSE themes D-10 (Repo-Verifiable Evidence), D-11 (Evidence Type Taxonomy Extension), D-12 (Aggregation Policy Declaration), D-13 (Silent Allowed-Failure Prohibition)
   - P-STD-002E: CLAUSE themes E-9 (Execution Reference Schema), E-10 (Aggregation Policy Field), E-11 (Execution Posture Fields), E-12 (MVAT Definition)
6. Author Specification Index per `P-STD-001-CLAUSE-002` (required if >5 CLAUSEs)
7. For each substandard, author CLAUSEs using `P-STD-002-CLAUSE-###` format per `P-STD-001-CLAUSE-018B`
8. Use `MUST`/`SHOULD`/`MAY` keywords per `P-STD-001-CLAUSE-008` (BCP 14 primary vocabulary)
9. Include subclauses where needed per `P-STD-001-CLAUSE-020`
10. Author a `### General Provisions` subsection immediately before the `### P-STD-002A` substandard heading. Include a forward-only adoption CLAUSE: "P-STD-002 requirements apply forward-only from the standard's effective date. Existing artifacts are not required to retroactively conform; conformance applies to the next status update or artifact creation event." Cite `P-ASSUM-001` as the governing assumption. (Scope gap FINDING-001 from TK001.1 review)
11. Within `P-STD-002D` authoring, after all normative CLAUSEs, include a reserved section header for theme D-9: `#### Stale-State Governance [Reserved — Phase 2]` with informative note: "Reserved for Phase 2. No normative requirements in this version. Scope: time-since-update thresholds, cadence enforcement, escalation paths." (Scope gap FINDING-003 from TK001.1 review)
12. Within `P-STD-002D` authoring of theme D-12 (Aggregation Policy Declaration), include an informative definitions table for the four aggregation policy modes: `fail_fast` (first failure terminates the evidence set), `allow_failure` (individual failures do not block the overall outcome), `continue_on_error` (failures noted but execution continues to completion), `manual_gate` (human approval required before outcome is determined). (Authoring guidance from TK001.1 OBS-004)
13. Within `P-STD-002E` authoring of theme E-4 (Ledger Schema Requirements), define the extensibility mechanism concretely: extension fields MUST use a reserved namespace prefix (e.g., `x_`) or MUST be appended to defined arrays without replacing baseline fields. Extensions MUST NOT override or redefine any baseline normative field. (Authoring guidance from TK001.1 OBS-003; CDR-11)
14. When authoring CLAUSEs for themes D-4 and D-10 (evidence validation and repo-verifiable evidence), ensure CLAUSE text explicitly distinguishes "primary recommendation" (GitHub Checks) from "required platform." Commit-status API MUST be presented as a first-class fallback for non-GitHub environments, not a footnote. CLAUSE text MUST NOT read as if GitHub is the only acceptable platform. (Authoring guidance from TK001.1 OBS-002; CDR-09)

**Success Criteria**:
- [ ] Combined file exists at canonical path
- [ ] Follows `P-STD-001-CLAUSE-001A` canonical structure (5 required sections in order)
- [ ] Specification Index present per `P-STD-001-CLAUSE-002`
- [ ] All CLAUSEs use `P-STD-002-CLAUSE-###` format
- [ ] Normative keywords follow `P-STD-001-CLAUSE-008`
- [ ] General Provisions CLAUSE present (forward-only adoption, citing P-ASSUM-001)
- [ ] D-9 reserved section header present in P-STD-002D
- [ ] Aggregation policy modes informative definitions table included in D-12 CLAUSE
- [ ] CDR-11 extensibility mechanism concretely defined in E-4 CLAUSE
- [ ] CDR-09 CLAUSE text distinguishes recommendation from required platform; commit-status fallback is first-class

---

### Task TK003: Draft P-STD-002-ADR-001

**Task ID**: `P-PH000-ST001-AC003-TK003`

**Purpose**: Author the embedded decision record capturing the rationale for P-STD-002 design choices.

**Deliverable**: `## Decision Record` section within `standard_P-STD-002_program-status-standard.md`

**Steps**:
1. Author `P-STD-002-ADR-001` body per `P-STD-001-CLAUSE-025` (DR Body Template)
2. Required subheadings: Context, Decision, Alternatives Considered, Consequences
3. Context MUST cite: P-RES-001 research findings, P-RES-002 research findings, SES001 consultation decisions (DEC-001 through DEC-012), CDR resolution proposal (13 confirmed decisions), existing analysis file as seed
4. Decision MUST document: 7-state enum choice (confirmed stable across both research streams; transition nuance per CDR-02), execution model boundary (CDR-01), unified dependency schema choice, evidence linkage normative requirement (CDR-09), aggregation policy requirement (CDR-10), evidence anchor choice (CDR-09), stale-state SLA deferral, and all other CDR-confirmed decisions
5. Alternatives MUST include: 3-state enum (minimal), initiative-specific dependency models, evidence linkage as informative-only
6. Consequences MUST include: guideline cascade requirement (positive), enum migration overhead (negative/neutral)
7. In the Consequences subheading, include a risk-mitigation traceability table mapping the 4 carry-forward risks to their CDR-based mitigations (Scope gap FINDING-002 from TK001.1 review):

   | Risk | Source | Mitigation |
   |:--|:--|:--|
   | P-RES-001-RISK-001 (overfitting to one tool) | P-RES-001 §V | CDR-04 (RACI labels keep standard role-agnostic) + CDR-09 (commit-status fallback) + Domain C interface-contract model |
   | P-RES-001-RISK-002 (narrative/ledger drift) | P-RES-001 §V | Domain E CLAUSEs: authority hierarchy (E-2), update sequence (E-6), drift prevention contract (E-7) — all normative (MUST) |
   | P-RES-002-RISK-001 (Checks-only portability) | P-RES-002 §V | CDR-09 (commit-status fallback) + platform-agnostic evidence schema (type/ref/date/by/summary) |
   | P-RES-002-RISK-002 (silent allowed failures) | P-RES-002 §V | CDR-10 (aggregation policy MUST) + D-12 (aggregation policy declaration) + D-13 (silent allowed-failure prohibition) + B-7 (allowed-failure health impact rule) |

8. In the Context subheading, include this explanation of CDR-03 treatment (authoring guidance from TK001.1 OBS-001): "CDR-03 (7-state vocabulary stability) was not elevated to a binding client-facing decision because both P-RES-001 (Topic 1, weighted score 80/90) and P-RES-002 (Topic 1 verdict) independently confirmed the vocabulary before the consolidated decision register was assembled. It is recorded as a pre-confirmed fact in the CDR proposal preamble. The CDR numbering gap (CDR-02 → CDR-04) is intentional and documented."

**Success Criteria**:
- [ ] P-STD-002-ADR-001 body present under `## Decision Record`
- [ ] Follows `P-STD-001-CLAUSE-025` template exactly
- [ ] Rationale traces to P-RES-001 and SES001 decisions
- [ ] Risk-mitigation traceability table present in Consequences section (4 risks mapped to CDR mitigations)
- [ ] CDR-03 treatment explanation present in Context section

---

### Task TK004: Validate Against P-STD-001 Authoring Rules

**Task ID**: `P-PH000-ST001-AC003-TK004`

**Purpose**: Produce the primary, evidence-first verification artifact preparing `P-PH000-ST001-AC003-GATE-001` by validating `P-STD-002` deliverables against required authoring and completeness criteria. This is a reviewer-owned verification task and MUST follow `guideline_workspace_verification.md`.

**Deliverable**:
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/verification/verification_P-PH000-ST001-AC003_gate-001.md`

**Steps**:
1. Create the verification artifact using `prompt/templates/consultant/workspace/template_workspace_verification.md`.
2. Provide an evidence list covering, at minimum:
   - `prompt/artifacts/tasks/P/standard/standard_P-STD-002_program-status-standard.md` (TK002+TK003 output)
   - `prompt/artifacts/tasks/P/workspace/PH000/ST001/proposal/proposal_P-PH000-ST001-AC003-TK001_cdr-resolution.md` (binding decision input)
   - `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/analysis/analysis_P-PH000-ST001-AC003-TK001_clause-theme-mapping.md` (54-theme input)
3. Verify required aspects (minimum):
   - Validate against `P-STD-001` authoring rules (canonical section order, Specification Index, CLAUSE formatting, DR body template, references/provenance, normative boundary hygiene).
   - Confirm completeness: 54 sequential CLAUSEs exist and `P-STD-002-ADR-001` addresses the 13 binding CDR decisions.
4. Issue a Gate Recommendation verdict and include a Gate Decision Record (GDR) section with `Client Decision: pending`.

**Success Criteria**:
- [ ] Gate verification artifact exists at the canonical path and follows the workspace verification template
- [ ] Verification includes P-STD-001 authoring-rule validation as an explicit checklist category
- [ ] Verification includes a Gate Recommendation verdict and GDR with `Client Decision: pending`

---

### Gate GATE-001: Client Acceptance of P-STD-002

**Gate ID**: `P-PH000-ST001-AC003-GATE-001`

**Entry Criteria**: TK004 verification complete (verdict issued; GDR pending)
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
| Plan (this file) | Activity Plan AC003 | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/plan_P-PH000-ST001-AC003.md` |
| Plan | Stream Plan ST001 | `prompt/artifacts/tasks/P/workspace/PH000/ST001/plan_P-PH000-ST001.md` |
| Plan | Research Stream ST004 | `prompt/artifacts/tasks/P/workspace/PH000/ST004/plan_P-PH000-ST004.md` |
| Standard | P-STD-001 (authoring authority) | `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md` |
| Standard (deliverable) | P-STD-002 (Program Status Standard) | `prompt/artifacts/tasks/P/standard/standard_P-STD-002_program-status-standard.md` |
| Guideline | Standard specs guideline | `prompt/templates/consultant/standards/guideline_standard_specs.md` |
| Template | Standard specs template | `prompt/templates/consultant/standards/template_standard_specs.md` |
| Informal Input | Relocated analysis (seed) | `prompt/artifacts/tasks/P/workspace/PH000/ST002/analysis/analysis_P-PH000-ST002_status-system-research.md` |
| Evidence | SES001 Transcript | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/snotes/raw_P-PH000-ST001-AC003-SES001.txt` |
| Research Input | P-RES-001 Integration Recommendations | `prompt/artifacts/tasks/P/workspace/PH000/ST004/analysis/analysis_P-PH000-ST004-AC001-TK003_integration-recommendations-P-RES-001.md` |
| Research Input | P-RES-002 Integration Recommendations | `prompt/artifacts/tasks/P/workspace/PH000/ST004/analysis/analysis_P-PH000-ST004-AC002-TK003_integration-recommendations-P-RES-002.md` |
| Deliverable | CDR Resolution Proposal (TK001) | `prompt/artifacts/tasks/P/workspace/PH000/ST001/proposal/proposal_P-PH000-ST001-AC003-TK001_cdr-resolution.md` |
| Deliverable | TK001 CLAUSE Theme Mapping | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/analysis/analysis_P-PH000-ST001-AC003-TK001_clause-theme-mapping.md` |
| Deliverable | TK001.1 CDR Readiness Review | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/verification/verification_P-PH000-ST001-AC003-TK001.1_cdr-review.md` |
| Deliverable (planned) | GATE-001 Verification Artifact (TK004) | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/verification/verification_P-PH000-ST001-AC003_gate-001.md` |
| Dev-report | TK002/TK003 execution | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/dev-report/dev-report_P-PH000-ST001-AC003_tk002-tk003-execution_2026-02-27.md` |

---

## V. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v0.3.2 | 2026-02-27 | Housekeeping | Updated TK002/TK003 to `completed` with evidence in Task Register; added missing TK001.1 detailed task section in §III for traceability (proposal + mapping inputs → verification output); reframed TK004 as reviewer-owned gate verification artifact task (per `guideline_workspace_verification.md`) and updated GATE-001 entry criteria; refreshed Context and Links Register to reflect implemented deliverables. Evidence: `dev-report_P-PH000-ST001-AC003_tk002-tk003-execution_2026-02-27.md`. |
| v0.3.0 | 2026-02-27 | Amendment | TK001.1 (CDR readiness review, CONDITIONAL PASS / APPROVE WITH CONDITIONS) inserted into task register; TK002 `Depends On` updated to `TK001.1`; TK002 steps 10–14 added (forward-only adoption CLAUSE, D-9 reserved section header, aggregation mode definitions table, extensibility hook mechanism, evidence anchor platform-agnostic language); TK003 steps 7–8 added (risk-mitigation traceability table, CDR-03 treatment explanation); TK002 and TK003 success criteria enriched; TK001.1 verification deliverable added to Links Register. Evidence: CDR readiness review session 2026-02-27. |
| v0.2.1 | 2026-02-27 | Amendment | QA alignment: TK001 deliverables clarified to include a 54-theme mapping artifact (A-1..E-12) and a 13-binding-decision CDR proposal (CDR-01, CDR-02, CDR-04..CDR-14). Final `P-STD-002-CLAUSE-###` numbering deferred to TK002 authoring. TK000/TK001 marked completed. |
| v0.2.0 | 2026-02-26 | Amendment | Plan amendment incorporating P-RES-002 research integration. Changes: (1) removed DRAFT banner, (2) added dual dependency on ST004-AC001 + ST004-AC002, (3) expanded TK001 scope to ingest both integration recommendation packages and produce CDR resolution proposal at `proposal/`, (4) enriched TK002 scope with 13 P-RES-002-originated CLAUSE themes (54 total), (5) enriched TK003 scope to cite both research inputs and address 13 consolidated decisions, (6) updated Links Register with research inputs and proposal deliverable. Evidence: consultant session 2026-02-26. |
| v0.1.0 | 2026-02-23 | Initial | Draft activity plan created from AC003-SES001 consultation. Task register and CLAUSE domains are draft; subject to amendment after P-RES-001 integration sign-off (P-PH000-ST004-AC001-GATE-003). Evidence: `raw_P-PH000-ST001-AC003-SES001.txt` |
