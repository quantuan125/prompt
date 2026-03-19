---
artifact_type: 'PLAN'
planning_level: 'ACTIVITY'
initiative_id: 'P'
initiative_code: 'PROGRAM'
phase: '0'
stream_id: 'P-PH000-ST001'
activity_id: 'P-PH000-ST001-AC003'
version: '0.10.0'
date: '2026-03-19'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
governance_rules: 'prompt/templates/consultant/workspace/workspace_documentation_rules.md'
procedural_guideline: 'prompt/templates/consultant/workspace/guideline_workspace_plan.md'
parent_plan: 'prompt/artifacts/tasks/P/workspace/PH000/ST001/plan_P-PH000-ST001.md'
---

# PLAN: P (PROGRAM) â€” Phase 0 / Stream ST001 / Activity AC003: Author P-STD-002 (Program Status Standard)


## I. EXECUTIVE SUMMARY

**Purpose**: Author `P-STD-002` (Program Status Standard) as a program-wide status governance standard covering: canonical status vocabulary with transition rules, health/RAG assessment requirements, unified dependency visibility schema, evidence linkage protocol, update protocol with role accountability, and status artifact specification. This activity also packages the post-acceptance follow-on work needed to make AC003 implementation-ready through `GATE-004`.

**Non-goal**: This activity does not create `status_program.md` (deferred to P-PH000-ST002-AC002), execute repo-wide initiative plan retrofits beyond the explicit cascade task (TK006), or apply any `P-STD-002` amendments beyond the explicitly authorized TK011 through TK013 package. The evidence-retention sibling governance artifact is deferred to `P-PH000-ST001-AC008`.

---

## II. ACTIVITY OUTLINE

**Activity ID**: `P-PH000-ST001-AC003`
**Objective**: Produce a P-STD-001-conformant combined standard-specification file that establishes program-wide status governance semantics and is accepted by the Client.
**Execution Mode**: SEQUENTIAL
**Depends On**: `P-PH000-ST004-AC001` (P-RES-001 integration sign-off via GATE-003) + `P-PH000-ST004-AC002` (P-RES-002 integration sign-off via GATE-003)

**Context**:
- `prompt/artifacts/tasks/P/standard/standard_P-STD-002_program-status-standard.md` (deliverable â€” created)
- `prompt/artifacts/tasks/P/ssot/sps_P-PROGRAM.md` (P-STD-002 row update)
- `prompt/templates/consultant/standards/guideline_standard_specs.md` (authoring rules)
- `prompt/templates/consultant/standards/template_standard_specs.md` (structural skeleton)
- `prompt/templates/consultant/workspace/guideline_workspace_analysis.md` (analysis authoring rules)
- `prompt/templates/consultant/workspace/template_workspace_analysis.md` (analysis template)
- `prompt/templates/consultant/workspace/guideline_workspace_plan.md` (cascade target)
- `prompt/templates/consultant/workspace/guideline_workspace_proposal.md` (proposal archetypes + GDR authority)
- `prompt/templates/consultant/workspace/guideline_workspace_verification.md` (verification workflow)
- `prompt/artifacts/tasks/P/workspace/PH000/ST004/analysis/analysis_P-PH000-ST004-AC001-TK003_integration-recommendations-P-RES-001.md` (P-RES-001 integration recommendations)
- `prompt/artifacts/tasks/P/workspace/PH000/ST004/analysis/analysis_P-PH000-ST004-AC002-TK003_integration-recommendations-P-RES-002.md` (P-RES-002 integration recommendations)
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/proposal/proposal_P-PH000-ST001-AC003-TK001_cdr-resolution.md` (CDR resolution proposal â€” TK001 deliverable)

### Task Register

| Task | Task ID | Name | Status | Owner | Depends On | Target | Reference | Action |
|:--|:--|:--|:--|:--|:--|:--|:--|:--|
| TK000 | `P-PH000-ST001-AC003-TK000` | Confirm sps_P P-CON-003 amendment applied | `completed` | LLM_Consultant | â€” | sps_P | DEC-003 | Verified in sps_P (P-CON-003 updated) |
| TK001 | `P-PH000-ST001-AC003-TK001` | Ingest P-RES-001 and P-RES-002 integration recommendations, map to CLAUSE domains, and produce CDR resolution proposal | `completed` | LLM_Consultant | ST004-AC001-GATE-003 + ST004-AC002-GATE-003 | proposal/ + AC003/analysis/ | P-RES-001 + P-RES-002 analyses | Client confirmed defaults (2026-02-27) |
| TK001.1 | `P-PH000-ST001-AC003-TK001.1` | Verify TK001 deliverables â€” CDR review and readiness assessment for TK002 | `completed` | LLM_Consultant | TK001 | AC003/verification/ | guideline_workspace_verification | CONDITIONAL PASS; APPROVE WITH CONDITIONS (2026-02-27) |
| TK002 | `P-PH000-ST001-AC003-TK002` | Draft P-STD-002 combined file: Specification section (54 CLAUSE themes across 5 domains) | `completed` | LLM_Consultant | TK001.1 | `prompt/artifacts/tasks/P/standard/standard_P-STD-002_program-status-standard.md` | `prompt/artifacts/tasks/P/standard/standard_P-STD-002_program-status-standard.md` | Authored P-STD-002 Specification (54 CLAUSEs) per TK002. Evidence: `dev-report_P-PH000-ST001-AC003_tk002-tk003-execution_2026-02-27.md` |
| TK003 | `P-PH000-ST001-AC003-TK003` | Draft P-STD-002-ADR-001 in Decision Record section (address 13 binding CDR decisions) | `completed` | LLM_Consultant | TK002 | `prompt/artifacts/tasks/P/standard/standard_P-STD-002_program-status-standard.md` | `prompt/artifacts/tasks/P/standard/standard_P-STD-002_program-status-standard.md` | Authored embedded `P-STD-002-ADR-001` per TK003. Evidence: `dev-report_P-PH000-ST001-AC003_tk002-tk003-execution_2026-02-27.md` |
| TK004 | `P-PH000-ST001-AC003-TK004` | Produce GATE-001 verification artifact (includes validation vs P-STD-001 authoring rules) | `completed` | LLM_Reviewer | TK003 | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/verification/verification_P-PH000-ST001-AC003_gate-001.md` | `prompt/templates/consultant/workspace/guideline_workspace_verification.md` | Verification complete (v1.2.0). Verdict: CONDITIONAL PASS. Historical verification GDR retained for audit trail; authoritative gate decision later superseded by the Gate-001 proposal package. |
| GATE-001 | `P-PH000-ST001-AC003-GATE-001` | **Gate: Client acceptance of P-STD-002**. Entry: TK004 verification complete (verdict issued; proposal GDR pending). Reviewer: Client. Exit: explicit acceptance recorded. | `completed` | Client | TK004 | â€” | â€” | Gate closed. Client decision: APPROVE (2026-03-04). Authoritative GDR: `proposal_P-PH000-ST001-AC003-GATE-001_gir-disposition-package.md` v1.1.0 Â§VI (supersedes verification GDR per SES003-DEC001). Prior conditions (FINDING-003/004) resolved. |
| TK005 | `P-PH000-ST001-AC003-TK005` | Update sps_P P-STD-002 row (status â†’ `accepted`, canonical path, effective date) | `completed` | LLM_Developer | GATE-001 | `prompt/artifacts/tasks/P/ssot/sps_P-PROGRAM.md` | P-STD-001-CLAUSE-012 | P-STD-002 SPS row accepted (effective 2026-03-04) and body entry added. Evidence: `dev-report_P-PH000-ST001-AC003_tk005-tk006-implementation_2026-03-07.md`. |
| TK006 | `P-PH000-ST001-AC003-TK006` | Cascade P-STD-002 status authority to downstream workspace guidance/templates | `completed` | LLM_Developer | GATE-001 | `prompt/templates/consultant/workspace/` | DEC-008 | Workspace plan/roadmap guidance + templates aligned to P-STD-002 canonical status authority; gate-only `failed` preserved as specialization. Evidence: `dev-report_P-PH000-ST001-AC003_tk005-tk006-implementation_2026-03-07.md`. |
| TK007 | `P-PH000-ST001-AC003-TK007` | Retention-Policy Ownership Assessment (GIR-003 / GAP-002) | `completed` | LLM_Consultant | GATE-001 | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/analysis/analysis_P-PH000-ST001-AC003-TK007_retention-policy-ownership-assessment.md` | `prompt/templates/consultant/workspace/guideline_workspace_analysis.md` | Assessment authored. Recommended sibling-policy ownership for evidence-retention duration; downstream actions recorded in the analysis artifact. |
| TK008 | `P-PH000-ST001-AC003-TK008` | Stale-State Governance Standards Input Proposal (GIR-004 / GAP-001) | `completed` | LLM_Consultant | TK007 | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/proposal/proposal_P-PH000-ST001-AC003-TK008_stale-state-governance-standards-input.md` | `prompt/templates/consultant/workspace/guideline_workspace_proposal.md` | Standards-input proposal authored with draft `P-STD-002-CLAUSE-038` text, decision requests, and risk framing. |
| TK009 | `P-PH000-ST001-AC003-TK009` | Produce Verification Evidence for the TK005â€“TK008 Package | `completed` | LLM_Reviewer | TK005, TK006, TK007, TK008 | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/verification/verification_P-PH000-ST001-AC003_gate-003.md` | `prompt/templates/consultant/workspace/guideline_workspace_verification.md` | Verification complete. Verdict: PASS. No findings identified; package is decision-ready for GATE-003 review. |
| TK010 | `P-PH000-ST001-AC003-TK010` | Prepare GATE-003 Decision Package (External Review + Gate Disposition) | `completed` | LLM_Consultant | TK009 | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/analysis/analysis_P-PH000-ST001-AC003-GATE-003_external-review-disposition.md`; `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/proposal/proposal_P-PH000-ST001-AC003-GATE-003_execution-disposition-package.md` | `prompt/templates/consultant/workspace/guideline_workspace_analysis.md`; `prompt/templates/consultant/workspace/guideline_workspace_proposal.md` | External review analysis and gate-disposition proposal authored. Proposal now hosts the authoritative completed GDR for Gate-003 client review. |
| GATE-003 | `P-PH000-ST001-AC003-GATE-003` | Gate: Client review of the post-acceptance execution package through TK010 | `completed` | Client | TK010 | Pass/fail | `prompt/templates/consultant/workspace/guideline_workspace_plan.md` | Gate passed. Client decision recorded in `proposal_P-PH000-ST001-AC003-GATE-003_execution-disposition-package.md` v1.2.0 (APPROVE, 2026-03-09). |
| TK011 | `P-PH000-ST001-AC003-TK011` | Apply approved CLAUSE-038 amendment to P-STD-002 | `completed` | LLM_Developer | GATE-003 | `prompt/artifacts/tasks/P/standard/standard_P-STD-002_program-status-standard.md` | TK008 approved text + GATE-003 GDR | Replaced reserved `P-STD-002-CLAUSE-038` with approved stale-state governance text; updated Specification Index and P-STD-002 provenance; refreshed SPS bookkeeping (2026-03-09). |
| TK012 | `P-PH000-ST001-AC003-TK012` | Verify CLAUSE-038 amendment | `completed` | LLM_Reviewer | TK011 | AC003 plan task register Action evidence | TK008 source text | Light verification completed. `CLAUSE-038` live text at `standard_P-STD-002_program-status-standard.md` was compared against the approved TK008 source text and GATE-003 posture decisions; the result is recorded here and re-confirmed in `verification_P-PH000-ST001-AC003_gate-004.md`. |
| TK013 | `P-PH000-ST001-AC003-TK013` | Apply `deferred` canonical state + casing governance CLAUSE amendments to P-STD-002 | `completed` | LLM_Developer | TK012 | `prompt/artifacts/tasks/P/standard/standard_P-STD-002_program-status-standard.md` | T104-PH001-ST008-AC003-SES002 (client directive) + industry analysis | Added `deferred` as 8th canonical state (CLAUSE-001/001A), added CLAUSE-056 (Status Enum Casing Convention), updated transition matrix (CLAUSE-005), guard conditions (CLAUSE-006 G10), staleness thresholds (CLAUSE-038), tool meta-category mapping (CLAUSE-002), blocked/on-hold semantics (CLAUSE-009). P-STD-002 v1.2.0. |
| TK014 | `P-PH000-ST001-AC003-TK014` | Produce GATE-004 verification evidence for TK011-TK013 package | `completed` | LLM_Reviewer | TK013 | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/verification/verification_P-PH000-ST001-AC003_gate-004.md` | `prompt/templates/consultant/workspace/guideline_workspace_verification.md` | Verification complete. Verdict: PASS. Artifact explicitly records that no dedicated TK013 dev-report exists and that review was performed directly against the live standard and governing approval inputs. |
| TK015 | `P-PH000-ST001-AC003-TK015` | Prepare GATE-004 gate-disposition proposal | `completed` | LLM_Consultant | TK014 | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/proposal/proposal_P-PH000-ST001-AC003-GATE-004_amendment-disposition-package.md` | `prompt/templates/consultant/workspace/guideline_workspace_proposal.md` | Gate-disposition proposal authored with Gate Package Index, Evidence Index, GIR register, and pending GDR for client review. |
| GATE-004 | `P-PH000-ST001-AC003-GATE-004` | Gate: Client review of TK011-TK013 amendment package | `in_progress` | Client | TK015 | Pass/fail | `prompt/templates/consultant/workspace/guideline_workspace_plan.md` | Gate-ready package assembled. Reviewer verdict recorded in `verification_P-PH000-ST001-AC003_gate-004.md`; authoritative client decision pending in `proposal_P-PH000-ST001-AC003-GATE-004_amendment-disposition-package.md`. |

---

## III. TASKS (DETAILED)

### Task TK000: Confirm sps_P P-CON-003 Amendment Applied

**Task ID**: `P-PH000-ST001-AC003-TK000`

**Purpose**: Pre-work verification that the P-CON-003 revision from SES001 has been applied to sps_P before AC003 execution begins.

**Deliverable**: Verification only â€” no artifact produced.

**Steps**:
1. Open `prompt/artifacts/tasks/P/ssot/sps_P-PROGRAM.md`
2. Confirm P-CON-003 title reads `(Artifact Format Governance)`
3. Confirm body has (A) and (B) sub-rules as specified in DEC-003
4. If not applied, escalate â€” this is a blocking prerequisite

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
- `prompt/artifacts/tasks/P/workspace/PH000/ST004/analysis/analysis_P-PH000-ST004-AC001-TK003_integration-recommendations-P-RES-001.md` â€” P-RES-001 integration recommendations (baseline: 41 CLAUSE themes, 9 decisions)
- `prompt/artifacts/tasks/P/workspace/PH000/ST004/analysis/analysis_P-PH000-ST004-AC002-TK003_integration-recommendations-P-RES-002.md` â€” P-RES-002 integration recommendations (complement: 13 CLAUSE themes, 4 decisions, combined synthesis)

**Combined CLAUSE domain totals**:
- **P-STD-002A â€” Status Vocabulary**: 11 CLAUSE themes (9 baseline + 2 P-RES-002: execution posture fields, manual-gate crosswalk)
- **P-STD-002B â€” Health Assessment**: 7 CLAUSE themes (6 baseline + 1 P-RES-002: allowed-failure health impact rule)
- **P-STD-002C â€” Dependency Visibility**: 11 CLAUSE themes (9 baseline + 2 P-RES-002: orchestration reference fields, category taxonomy extension)
- **P-STD-002D â€” Update Protocol**: 13 CLAUSE themes (9 baseline + 4 P-RES-002: repo-verifiable evidence, evidence type taxonomy extension, aggregation policy, silent allowed-failure prohibition)
- **P-STD-002E â€” Status Artifact**: 12 CLAUSE themes (8 baseline + 4 P-RES-002: execution reference schema, aggregation policy field, execution posture fields, MVAT)

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

### Task TK001.1: Verify TK001 Deliverables â€” CDR Readiness Review

**Task ID**: `P-PH000-ST001-AC003-TK001.1`

**Purpose**: Confirm that TK001 deliverables (CDR resolution proposal + CLAUSE theme mapping) are complete, internally consistent, and ready to drive TK002 authoring. This task produces an evidence-first verification artifact per `guideline_workspace_verification.md`.

**Deliverable**:
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/verification/verification_P-PH000-ST001-AC003-TK001.1_cdr-review.md`

**Inputs Required**:
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/proposal/proposal_P-PH000-ST001-AC003-TK001_cdr-resolution.md` (TK001 deliverable â€” Client confirmation of the prior TK001 analysis inputs)
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/analysis/analysis_P-PH000-ST001-AC003-TK001_clause-theme-mapping.md` (TK001 deliverable â€” 54 theme mapping)
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

### Task TK002: Draft P-STD-002 Combined File â€” Specification Section

**Task ID**: `P-PH000-ST001-AC003-TK002`

**Purpose**: Author the normative Specification section of P-STD-002.

**Deliverable**: `prompt/artifacts/tasks/P/standard/standard_P-STD-002_program-status-standard.md`

**Inputs Required**:
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/analysis/analysis_P-PH000-ST001-AC003-TK001_clause-theme-mapping.md` (primary â€” 54 themes across 5 domains)
- TK001 CDR resolution proposal with Client-confirmed decisions (primary â€” 13 CDR entries)
- `prompt/templates/consultant/standards/template_standard_specs.md` â€” Structural skeleton
- `prompt/templates/consultant/standards/guideline_standard_specs.md` â€” Authoring rules
- `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md` â€” Authority chain

**Steps**:
1. Copy `template_standard_specs.md` to deliverable path
2. Fill frontmatter: `artifact_type: 'STANDARD'`, `initiative_id: 'P'`, `std_id: 'P-STD-002'`, `governed_by: 'P-STD-001'`
3. Set heading: `# P-STD-002 â€” Program Status Standard`
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
11. Within `P-STD-002D` authoring, after all normative CLAUSEs, include a reserved section header for theme D-9: `#### Stale-State Governance [Reserved â€” Phase 2]` with informative note: "Reserved for Phase 2. No normative requirements in this version. Scope: time-since-update thresholds, cadence enforcement, escalation paths." (Scope gap FINDING-003 from TK001.1 review)
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
   | P-RES-001-RISK-001 (overfitting to one tool) | P-RES-001 Â§V | CDR-04 (RACI labels keep standard role-agnostic) + CDR-09 (commit-status fallback) + Domain C interface-contract model |
   | P-RES-001-RISK-002 (narrative/ledger drift) | P-RES-001 Â§V | Domain E CLAUSEs: authority hierarchy (E-2), update sequence (E-6), drift prevention contract (E-7) â€” all normative (MUST) |
   | P-RES-002-RISK-001 (Checks-only portability) | P-RES-002 Â§V | CDR-09 (commit-status fallback) + platform-agnostic evidence schema (type/ref/date/by/summary) |
   | P-RES-002-RISK-002 (silent allowed failures) | P-RES-002 Â§V | CDR-10 (aggregation policy MUST) + D-12 (aggregation policy declaration) + D-13 (silent allowed-failure prohibition) + B-7 (allowed-failure health impact rule) |

8. In the Context subheading, include this explanation of CDR-03 treatment (authoring guidance from TK001.1 OBS-001): "CDR-03 (7-state vocabulary stability) was not elevated to a binding client-facing decision because both P-RES-001 (Topic 1, weighted score 80/90) and P-RES-002 (Topic 1 verdict) independently confirmed the vocabulary before the consolidated decision register was assembled. It is recorded as a pre-confirmed fact in the CDR proposal preamble. The CDR numbering gap (CDR-02 â†’ CDR-04) is intentional and documented."

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
4. Issue a Gate Recommendation verdict. The authoritative GDR for Gate-001 is hosted in the gate-disposition proposal package, not in the verification artifact.

**Success Criteria**:
- [ ] Gate verification artifact exists at the canonical path and follows the workspace verification template
- [ ] Verification includes P-STD-001 authoring-rule validation as an explicit checklist category
- [ ] Verification includes a Gate Recommendation verdict and explicitly defers authoritative gate decision recording to the gate-disposition proposal

---

### Gate GATE-001: Client Acceptance of P-STD-002

**Gate ID**: `P-PH000-ST001-AC003-GATE-001`

**Entry Criteria**: TK004 verification complete (verdict issued; authoritative proposal-embedded GDR pending)
**Reviewer**: Client
**Exit Criteria**: Explicit Client acceptance recorded with date in the authoritative Gate-001 proposal GDR. P-STD-002 status transitions from `draft` â†’ `accepted`.

---

### Task TK005: Update sps_P P-STD-002 Row

**Task ID**: `P-PH000-ST001-AC003-TK005`

**Purpose**: Finalize the P-STD-002 registration in the program SPS.

**Steps**:
1. In `sps_P-PROGRAM.md` STD Index, update P-STD-002 row:
   - Status: `planned` â†’ `accepted`
   - Effective: `â€”` â†’ acceptance date (ISO-8601)
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

**Purpose**: Update all downstream guideline files that reference status values to defer to or align with P-STD-002's canonical status enum set and transition rules.

**Deliverable**: Updated guideline files with P-STD-002 references.

**Scope**:
- In scope:
  - `prompt/templates/consultant/workspace/guideline_workspace_plan.md`
  - `prompt/templates/consultant/workspace/guideline_workspace_roadmap.md`
  - `prompt/templates/consultant/workspace/template_workspace_plan_activity.md`
  - `prompt/templates/consultant/workspace/template_workspace_plan_stream.md`
  - `prompt/templates/consultant/workspace/template_workspace_plan_phase.md`
  - `prompt/templates/consultant/workspace/template_workspace_roadmap.md`
- Out of scope:
  - `prompt/templates/consultant/workspace/guideline_workspace_notes.md` decision/action/open-question enums and notes templates (these govern session-note workflow rather than program work-item status)
  - initiative-specific plan files (downstream adopters update on next touch)

**Steps**:
1. **Identify all guideline files referencing status enums**:
   - Read `prompt/templates/consultant/workspace/guideline_workspace_plan.md` â€” Â§III.A (Stream/Activity register status enums) and Â§III.B (Task register status enums)
   - Confirm the currently hardcoded register-status surfaces listed in Scope remain the only intended targets for this task
2. **Update `guideline_workspace_plan.md`**:
   - Â§III.A: Current text says status MUST be one of `planned`, `deferred`, `completed`, `cancelled`. Update to reference P-STD-002 as the canonical authority for status enums. Add note that register contexts may use a subset of the full canonical set as appropriate, but MUST NOT introduce states not defined in P-STD-002.
   - Â§III.B: Current text says task status MUST be one of `planned`, `deferred`, `completed`, `cancelled`, `failed`. Apply same update pattern.
   - Add External Reference line for `P-STD-002 (Program Status Standard)` per `P-STD-005-CLAUSE-004`
   - Version bump guideline with changelog entry
3. **Update the roadmap + planning templates**:
   - Replace hardcoded examples that imply a closed local status set with wording that defers to `P-STD-002` while allowing context-appropriate subsets.
   - Preserve gate-specific status semantics in `guideline_workspace_plan.md` Â§VI.D, but clarify that gate states are a plan-structure specialization layered on top of the broader status authority.
4. **Verify conformance**: Confirm no updated guidance/template introduces status states outside the P-STD-002 canonical enum set for program work items.

**Success Criteria**:
- [ ] `guideline_workspace_plan.md` references P-STD-002 as canonical status authority
- [ ] `guideline_workspace_roadmap.md` and the targeted planning templates defer to P-STD-002 for work-item lifecycle status
- [ ] No updated planning/roadmap surface introduces status states outside the P-STD-002 canonical enum for program work items
- [ ] All updated guideline/template files have changelog entries citing P-STD-002

---


### Task TK007: Determine Retention-Policy Ownership

**Task ID**: `P-PH000-ST001-AC003-TK007`

**Purpose**: Resolve the retention-policy ownership gap identified in external review GAP-002 and dispositioned as GIR-003 (client approved: defer to follow-on policy artifact). Determine whether evidence retention duration requirements belong within P-STD-002 (as an amendment) or in a sibling governance policy artifact.

**Deliverable**:
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/analysis/analysis_P-PH000-ST001-AC003-TK007_retention-policy-ownership-assessment.md`

**Analysis Type**: `assessment`

**Scope**:
- In scope:
  - Evaluate the current retention-policy ownership gap against P-STD-002 scope boundaries
  - Compare two implementation paths: amend P-STD-002 vs create/defer to a sibling policy artifact
  - Produce a decision-ready recommendation with explicit downstream action mapping
- Out of scope:
  - Applying a retention-duration amendment to `P-STD-002`
  - Authoring the sibling policy artifact if that path is recommended

**Inputs Required**:
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/analysis/analysis_P-PH000-ST001-AC003-GATE-001_external-review-industry-best-practices.md` (GAP-002 description + NIST AU-11 reference)
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/proposal/proposal_P-PH000-ST001-AC003-GATE-001_gir-disposition-package.md` (GIR-003 disposition)
- `prompt/artifacts/tasks/P/standard/standard_P-STD-002_program-status-standard.md` (current evidence CLAUSEs: CLAUSE-030 through CLAUSE-033)
- `prompt/templates/consultant/workspace/guideline_workspace_analysis.md` + `prompt/templates/consultant/workspace/template_workspace_analysis.md`

**Steps**:
1. Create the analysis artifact using `template_workspace_analysis.md` with `analysis_type: 'assessment'`.
2. Summarize the current state, governing gap, and the two viable ownership options:
   - amendment inside `P-STD-002`, or
   - sibling policy artifact outside `P-STD-002`.
3. Record a GAP register, recommendation, and downstream action table showing what work would be authorized next under each option.
4. Keep the output decision-ready for later package review; do not record a client decision inside the analysis artifact.

**Success Criteria**:
- [ ] Assessment artifact exists at the canonical path and follows `guideline_workspace_analysis.md`
- [ ] Recommendation clearly states whether retention ownership belongs inside `P-STD-002` or in a sibling artifact
- [ ] If sibling artifact is recommended, the target artifact type and ownership are identified in Downstream Actions
- [ ] Analysis output is decision-ready for later inclusion in the Gate-003 package

### Task TK008: Operationalize Stale-State Governance (CLAUSE-038)

**Task ID**: `P-PH000-ST001-AC003-TK008`

**Purpose**: Operationalize the reserved CLAUSE-038 (Stale-State Governance) by defining time-triggered review rules, cadence enforcement, and escalation paths. This addresses external review GAP-001 and GIR-004 (client approved: defer with tracked action).

**Deliverable**:
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/proposal/proposal_P-PH000-ST001-AC003-TK008_stale-state-governance-standards-input.md`

**Proposal Archetype**: `standards_input`

**Scope**:
- In scope:
  - define candidate stale-state rules for `CLAUSE-038`
  - produce decision-ready standards input with draft normative text
  - identify impacts, risks, and decision requests for later gate review
- Out of scope:
  - applying the amendment to `standard_P-STD-002_program-status-standard.md`
  - recording the authoritative client gate decision (handled later via a `gate_disposition` proposal)

**Inputs Required**:
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/analysis/analysis_P-PH000-ST001-AC003-TK007_retention-policy-ownership-assessment.md` (TK007 output)
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/analysis/analysis_P-PH000-ST001-AC003-GATE-001_external-review-industry-best-practices.md` (GAP-001 description + RISK-001)
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/proposal/proposal_P-PH000-ST001-AC003-GATE-001_gir-disposition-package.md` (GIR-004 disposition)
- `prompt/artifacts/tasks/P/standard/standard_P-STD-002_program-status-standard.md` (CLAUSE-038 reserved section + CLAUSE-017 health cadence)
- `prompt/templates/consultant/workspace/guideline_workspace_proposal.md`

**Steps**:
1. Review GAP-001 description and RISK-001 (stale status entries remain technically valid but operationally stale)
2. Research industry patterns for stale-state detection: time-since-update thresholds (SLA/TTL), cadence enforcement triggers, automated drift detection signals
3. Define candidate stale-state rules:
   - Maximum time-since-update threshold per status state (e.g., `in_progress` items not updated within N days trigger review)
   - Cadence enforcement: minimum update frequency requirements by status category
   - Escalation paths: what happens when stale-state is detected (notification â†’ forced review â†’ status downgrade)
4. Assess interaction with existing CLAUSE-017 (Health Assessment Cadence) and the TK007 recommendation â€” ensure no conflict or ownership ambiguity
5. Author the proposal as a `standards_input` artifact with:
   - current state summary,
   - proposed stale-state conventions,
   - explicit decision requests,
   - impact/risk analysis,
   - draft `CLAUSE-038` replacement text.
6. Keep the output decision-ready for later inclusion in the Gate-003 package; do not record the authoritative client decision inside this artifact.

**Success Criteria**:
- [ ] Stale-state rules defined with time thresholds, cadence requirements, and escalation paths
- [ ] No conflict with existing CLAUSE-017 health cadence requirements
- [ ] Draft `CLAUSE-038` normative text is included in the proposal
- [ ] Proposal exists at the canonical path and follows the `standards_input` archetype requirements
- [ ] Proposal output is decision-ready for later inclusion in the Gate-003 package

---

### Task TK009: Produce Verification Evidence for the TK005â€“TK008 Package

**Task ID**: `P-PH000-ST001-AC003-TK009`

**Purpose**: Produce the reviewer-owned verification artifact for the post-acceptance execution package, confirming that the SPS update, guidance cascade, retention-policy assessment, and stale-state standards-input proposal are complete, internally consistent, and ready for Gate-003 review.

**Deliverable**:
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/verification/verification_P-PH000-ST001-AC003-gate-003.md`

**Inputs Required**:
- `prompt/artifacts/tasks/P/ssot/sps_P-PROGRAM.md` (TK005 output)
- workspace guidance/template files updated by TK006
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/analysis/analysis_P-PH000-ST001-AC003-TK007_retention-policy-ownership-assessment.md`
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/proposal/proposal_P-PH000-ST001-AC003-TK008_stale-state-governance-standards-input.md`
- `prompt/templates/consultant/workspace/guideline_workspace_verification.md` + `prompt/templates/consultant/workspace/template_workspace_verification.md`

**Steps**:
1. Create the verification artifact using the verification template and evidence-first workflow.
2. Verify TK005 success criteria against the updated SPS row/body text.
3. Verify TK006 success criteria against the targeted workspace guidance/template surfaces.
4. Verify TK007 follows the `assessment` analysis requirements and is decision-ready.
5. Verify TK008 follows the `standards_input` proposal requirements and is decision-ready.
6. Issue a reviewer verdict and any findings/observations. Do **not** host the authoritative GDR in the verification artifact.

**Success Criteria**:
- [ ] Verification artifact exists at the canonical path and follows `guideline_workspace_verification.md`
- [ ] TK005â€“TK008 outputs are checked with explicit observed evidence
- [ ] Reviewer verdict is issued without embedding an authoritative GDR in the verification artifact

---

### Task TK010: Prepare GATE-003 Decision Package (External Review + Gate Disposition)

**Task ID**: `P-PH000-ST001-AC003-TK010`

**Purpose**: Produce the client-facing decision package for Gate-003 by combining an independent `external_review` analysis of the TK005â€“TK009 package with a `gate_disposition` proposal that hosts the authoritative GDR and all GIR dispositions required for gate closure.

**Deliverables**:
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/analysis/analysis_P-PH000-ST001-AC003-GATE-003_external-review-disposition.md`
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/proposal/proposal_P-PH000-ST001-AC003-GATE-003_execution-disposition-package.md`

**Inputs Required**:
- TK005â€“TK008 outputs
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/verification/verification_P-PH000-ST001-AC003-gate-003.md` (TK009 verdict)
- `prompt/templates/consultant/workspace/guideline_workspace_analysis.md`
- `prompt/templates/consultant/workspace/guideline_workspace_proposal.md`

**Steps**:
1. Create the external review analysis using `analysis_type: 'external_review'`. Assess the package from an industry/best-practice standpoint, record a lightweight GAP register, and identify any decision items that should be surfaced to the Client.
2. Create the gate-disposition proposal using the Gate Disposition template. Convert the packageâ€™s outstanding decision points into GIR entries with options, recommendation, rationale, and execution targets.
3. Embed the authoritative `## Gate Decision Record` in the gate-disposition proposal with `Client Decision: pending`.
4. Ensure the proposal references the TK009 verification verdict and the external review analysis as package inputs.

**Success Criteria**:
- [ ] External review analysis exists at the canonical path and uses a valid `analysis_type` enum
- [ ] Gate-disposition proposal exists at the canonical path and hosts the authoritative GDR
- [ ] All GIRs required for Gate-003 decision-making are captured in the proposal, not in the verification artifact

---

### GATE-003: Client Review of the Post-Acceptance Execution Package

**Gate ID**: `P-PH000-ST001-AC003-GATE-003`

**Entry Criteria**:
- TK009 complete (verification evidence produced)
- TK010 complete (external review analysis + gate-disposition proposal authored)

**Reviewer**: Client

**Exit Criteria**:
- Client reviews the TK005â€“TK010 package and records the decision in the authoritative GDR section of `proposal_P-PH000-ST001-AC003-GATE-003_execution-disposition-package.md`
- Any GIR dispositions required for gate closure are explicitly recorded in the gate-disposition proposal
- Gate passes when the GDR records `Client Decision = APPROVE` or `APPROVE WITH CONDITIONS`

**Post-gate activity status note**: Passing GATE-003 authorizes downstream execution but does not close AC003. AC003 remains `in_progress` until all remaining registered tasks are terminal, including TK011 and TK012.

---

### Task TK011: Apply Approved CLAUSE-038 Amendment to P-STD-002

**Task ID**: `P-PH000-ST001-AC003-TK011`

**Purpose**: Replace the reserved CLAUSE-038 placeholder in P-STD-002 with the approved normative stale-state governance text from TK008, as authorized by GATE-003 GIR-003/004/005/006 client decisions.

**Deliverable**:
- Updated `prompt/artifacts/tasks/P/standard/standard_P-STD-002_program-status-standard.md`

**Inputs Required**:
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/proposal/proposal_P-PH000-ST001-AC003-TK008_stale-state-governance-standards-input.md` (approved draft text, lines 74-95)
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/proposal/proposal_P-PH000-ST001-AC003-GATE-003_execution-disposition-package.md` (GATE-003 GDR with approved posture decisions)

**Steps**:
1. Confirm GATE-003 GDR records `Client Decision = APPROVE` for GIR-003 (state-specific thresholds), GIR-004 (progressive escalation), GIR-005 (no automatic downgrade), and GIR-006 (authorize amendment inside AC003).
2. In `standard_P-STD-002_program-status-standard.md`:
   - Replace the reserved CLAUSE-038 text (current: "This CLAUSE is reserved for Phase 2 stale-state governance...") with the approved normative text from TK008 Â§III.C.
   - Update the Specification Index row 39: change title from "Stale-State Governance (Reserved)" to "Stale-State Governance".
   - Remove the "(Reserved)" qualifier from the CLAUSE heading.
3. Version bump P-STD-002 with changelog entry citing GATE-003 GDR as authorization.
4. Update `prompt/artifacts/tasks/P/ssot/sps_P-PROGRAM.md`:
   - Refresh P-STD-002 row if version changes.
   - Add changelog entry.

**Success Criteria**:
- [ ] CLAUSE-038 contains the approved normative stale-state governance text (not the reserved placeholder)
- [ ] Specification Index row 39 title updated (no "Reserved" qualifier)
- [ ] P-STD-002 changelog cites GATE-003 GDR as amendment authorization
- [ ] SPS P-STD-002 row reflects the updated version

---

### Task TK012: Verify CLAUSE-038 Amendment

**Task ID**: `P-PH000-ST001-AC003-TK012`

**Purpose**: Verify that the CLAUSE-038 amendment was correctly applied: text matches the approved TK008 draft, Specification Index is consistent, and no conflict exists with adjacent clauses.

**Deliverable**:
- Light verification evidence recorded in the AC003 plan task register `Action` field (no standalone verification artifact needed for a mechanical amendment).

**Inputs Required**:
- Updated `prompt/artifacts/tasks/P/standard/standard_P-STD-002_program-status-standard.md` (TK011 output)
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/proposal/proposal_P-PH000-ST001-AC003-TK008_stale-state-governance-standards-input.md` (approved source text)

**Steps**:
1. Confirm CLAUSE-038 normative text matches TK008 Â§III.C draft exactly (or with only client-approved modifications from GATE-003).
2. Confirm Specification Index row 39 is consistent with the updated CLAUSE heading.
3. Confirm no conflict with CLAUSE-037 (Conflict Resolution) and CLAUSE-039 (Repo-Verifiable Evidence Requirement).
4. Confirm SPS P-STD-002 row version is current.

**Success Criteria**:
- [ ] CLAUSE-038 text matches approved TK008 draft
- [ ] Specification Index consistent
- [ ] No conflict with adjacent clauses (CLAUSE-037, CLAUSE-039)
- [ ] SPS version current

### Task TK013: Apply `deferred` Canonical State + Casing Governance CLAUSE Amendments to P-STD-002

**Task ID**: `P-PH000-ST001-AC003-TK013`

**Purpose**: Add `deferred` as an 8th canonical lifecycle state to P-STD-002 and add a casing governance CLAUSE to standardize status enum formatting. This resolves a gap identified during T104-PH001-ST008-AC003 SES002 consultation: P-STD-002's 7-state vocabulary lacks `deferred` (intentional postponement beyond current scope), which is semantically distinct from `on_hold` (temporary pause within current scope) per industry standard analysis (ITIL 4, PMI PMBOK, ISO 12207).

**Deliverable**:
- Amended `prompt/artifacts/tasks/P/standard/standard_P-STD-002_program-status-standard.md` (v1.1.0 â†’ v1.2.0)

**Scope**:
- In scope:
  - Add `deferred` to CLAUSE-001 canonical vocabulary (8 states)
  - Add `deferred` definition to CLAUSE-001A
  - Update CLAUSE-002 tool meta-category mapping (classify `deferred` under "To Do")
  - Update CLAUSE-004 (non-terminal classification for `deferred`)
  - Add `deferred` row to CLAUSE-005 transition matrix
  - Add new guard G10 for `deferred` transitions in CLAUSE-006
  - Add `deferred` staleness threshold to CLAUSE-038
  - Update CLAUSE-009 to distinguish `blocked` vs `on_hold` vs `deferred`
  - Add CLAUSE-056 (Status Enum Casing Convention) to General Provisions
  - Update Specification Index
  - Update ADR-001 with CDR-15 decision
  - Update Amendment History
- Out of scope:
  - Cascade to downstream workspace templates (separate activity)
  - Enum casing enforcement in existing artifacts (forward-only per CLAUSE-055)

**Inputs Required**:
- Current P-STD-002 v1.1.0
- Industry analysis from T104-PH001-ST008-AC003-SES002 consultation
- P-STD-002-CLAUSE-055 (Forward-Only Adoption)

**Steps**:
1. Add `deferred` to CLAUSE-001 enum list
2. Add `deferred` definition to CLAUSE-001A
3. Update CLAUSE-002 tool meta-category mapping: add `deferred` to the "To Do" category
4. Update CLAUSE-004: clarify that `deferred` is NOT a terminal state
5. Add `deferred` row to CLAUSE-005 transition matrix and add the `deferred` column to all existing rows
6. Add guard G10 to CLAUSE-006
7. Add `deferred` threshold to CLAUSE-038 staleness
8. Update CLAUSE-009 to add `deferred` semantics
9. Add CLAUSE-056 to General Provisions
10. Update Specification Index
11. Update ADR-001 Decision section: add CDR-15
12. Update Amendment History

**Success Criteria**:
- [x] `deferred` appears in CLAUSE-001 canonical enum (8 states)
- [x] `deferred` definition in CLAUSE-001A is semantically distinct from `on_hold`
- [x] Transition matrix includes `deferred` row and column
- [x] Guard G10 defined for deferral transitions
- [x] Staleness threshold (30 days) added to CLAUSE-038
- [x] CLAUSE-056 casing convention added
- [x] CDR-15 recorded in ADR-001
- [x] Specification Index updated
- [x] Amendment History updated

### Task TK014: Produce GATE-004 Verification Evidence for TK011â€“TK013 Package

**Task ID**: `P-PH000-ST001-AC003-TK014`

**Purpose**: Independently verify that TK011 (CLAUSE-038 amendment) and TK013 (deferred state + casing convention) were correctly applied to P-STD-002.

**Deliverable**:
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/verification/verification_P-PH000-ST001-AC003_gate-004.md`

**Scope**:
- In scope:
  - Verify TK011: CLAUSE-038 text matches TK008 approved source text
  - Verify TK013: `deferred` state correctly integrated across all affected CLAUSEs
  - Verify TK013: CLAUSE-056 casing convention correctly authored
  - Verify Specification Index consistency
  - Verify no conflicts with adjacent CLAUSEs
- Out of scope:
  - Re-verifying TK001â€“TK010 (already covered by GATE-001 and GATE-003)

**Success Criteria**:
- [ ] All TK011 verification criteria pass
- [ ] All TK013 verification criteria pass
- [ ] Specification Index matches implemented CLAUSEs
- [ ] Verdict issued (PASS, CONDITIONAL PASS, or RECYCLE)

### Task TK015: Prepare GATE-004 Gate-Disposition Proposal

**Task ID**: `P-PH000-ST001-AC003-TK015`

**Purpose**: Package the TK011â€“TK013 verification results into a client-facing decision package.

**Deliverable**:
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/proposal/proposal_P-PH000-ST001-AC003-GATE-004_amendment-disposition-package.md`

**Success Criteria**:
- [ ] Gate Package Index and Evidence Index include TK011â€“TK013 deliverables
- [ ] GIR items map to TK011 and TK013 verification results
- [ ] GDR pending for client decision

### GATE-004: Client Review of TK011â€“TK013 Amendment Package

**Gate ID**: `P-PH000-ST001-AC003-GATE-004`

**Type**: Implementation-backed gate (verification required)

**Entry Criteria**:
- TK011 completed (CLAUSE-038 amendment applied)
- TK012 completed (light verification evidence recorded in the task register Action field)
- TK013 completed (`deferred` state + CLAUSE-056 applied)
- TK014 completed (verification evidence with verdict)
- TK015 completed (gate-disposition proposal authored)

**Reviewer**: LLM_Reviewer (verdict) / Client (decision owner)

**Exit Criteria**: GDR records `Client Decision: APPROVE` or `APPROVE WITH CONDITIONS`

**Gate-Disposition Proposal**: `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/proposal/proposal_P-PH000-ST001-AC003-GATE-004_amendment-disposition-package.md`

---

### Future Scope: Dependency Schedule Enrichment Uplift (GIR-005)

> **Informative â€” not a registered task.** External review GAP-005 identified that dependency schedule enrichment (CLAUSE-024, FS/SS/FF/SF) is optional in v1. GIR-005 client disposition: keep v1 unchanged, evaluate conditional uplift for critical dependencies in a future version study. This item is tracked as future scope without immediate TK registration. If a future version study is initiated, it should assess whether mandatory schedule enrichment for `criticality: critical` dependencies materially improves program critical-path visibility.

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
| Guideline | Analysis authoring | `prompt/templates/consultant/workspace/guideline_workspace_analysis.md` |
| Guideline | Proposal authoring | `prompt/templates/consultant/workspace/guideline_workspace_proposal.md` |
| Guideline | Verification authoring | `prompt/templates/consultant/workspace/guideline_workspace_verification.md` |
| Guideline | Notes authoring | `prompt/templates/consultant/workspace/guideline_workspace_notes.md` |
| Deliverable | SES002 Session Notes | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC003/snotes/snotes_T104-PH001-ST008-AC003-SES002.md` |
| Deliverable | TK007 Retention-Policy Ownership Assessment | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/analysis/analysis_P-PH000-ST001-AC003-TK007_retention-policy-ownership-assessment.md` |
| Deliverable | TK008 Stale-State Governance Standards Input | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/proposal/proposal_P-PH000-ST001-AC003-TK008_stale-state-governance-standards-input.md` |
| Deliverable | TK009 Gate-003 Verification | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/verification/verification_P-PH000-ST001-AC003_gate-003.md` |
| Deliverable | TK010 Gate-003 External Review Analysis | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/analysis/analysis_P-PH000-ST001-AC003-GATE-003_external-review-disposition.md` |
| Deliverable | TK010 Gate-003 Disposition Proposal | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/proposal/proposal_P-PH000-ST001-AC003-GATE-003_execution-disposition-package.md` |
| Deliverable | GATE-001 External Review Analysis | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/analysis/analysis_P-PH000-ST001-AC003-GATE-001_external-review-industry-best-practices.md` |
| Deliverable | GATE-001 GIR Disposition Package (authoritative GDR) | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/proposal/proposal_P-PH000-ST001-AC003-GATE-001_gir-disposition-package.md` |
| Dev-report | TK002/TK003 execution | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/dev-report/dev-report_P-PH000-ST001-AC003_tk002-tk003-execution_2026-02-27.md` |
| Dev-report | TK005/TK006 implementation | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/dev-report/dev-report_P-PH000-ST001-AC003_tk005-tk006-implementation_2026-03-07.md` |
| Notes | SES004 plan-amendment session | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/snotes/snotes_P-PH000-ST001-AC003-SES004.md` |
| Deliverable | TK011 Deliverable (Standard) | `prompt/artifacts/tasks/P/standard/standard_P-STD-002_program-status-standard.md` |
| Deliverable | TK014 Gate-004 Verification | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/verification/verification_P-PH000-ST001-AC003_gate-004.md` |
| Deliverable | TK015 Gate-004 Disposition Proposal | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/proposal/proposal_P-PH000-ST001-AC003-GATE-004_amendment-disposition-package.md` |
| Evidence | TK012 Verification Evidence | (Task Register Action Field) |

---

## V. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v0.10.0 | 2026-03-19 | Update | Completed TK012 light verification and authored the full Gate-004 package: TK014 verification artifact and TK015 gate-disposition proposal. Updated task-register actions, added Gate-004 deliverables to the Links Register, and moved GATE-004 to `in_progress` pending client decision in the proposal GDR. |
| v0.9.0 | 2026-03-18 | Amendment | Added TK013 (`deferred` canonical state + CLAUSE-056 casing convention amendment), TK014 (GATE-004 verification), TK015 (GATE-004 gate-disposition proposal), and GATE-004 (client review of TK011â€“TK013 package). Source: T104-PH001-ST008-AC003-SES002 client directive â€” P-STD-002 lacks `deferred` (semantically distinct from `on_hold` per industry analysis). TK013 status: `completed`. |
| v0.8.0 | 2026-03-09 | Update | Gate-003 closed and TK011 executed. Reordered Task Register and detailed sections to keep post-gate tasks after `GATE-003` per dependency order. Clarified Gate-003 exit criteria to separate gate passage from AC003 closure. Updated Gate-003/TK011 task-register actions to reflect proposal GDR approval and CLAUSE-038 amendment execution. |
| v0.7.0 | 2026-03-08 | Amendment | Amendment: Added TK011 (apply approved CLAUSE-038 amendment) and TK012 (verify amendment) as post-GATE-003 execution tasks. Updated Non-goal to authorize CLAUSE-038 amendment inside AC003. Updated GATE-003 exit criteria to require TK011/TK012 completion before AC003 closure. Evidence: SES005. |
| v0.6.0 | 2026-03-07 | Update | Completed `TK007` through `TK010`. Added the GATE-003 verification artifact, external-review analysis, and gate-disposition proposal; updated task-register evidence/actions; converted TK007/TK008/TK009/TK010 links from planned deliverables to active deliverables; set `GATE-003` to `in_progress` pending client dispositions and GDR completion. |
| v0.5.1 | 2026-03-07 | Update | Completed TK005/TK006. P-STD-002 SPS registration finalized (`accepted`, effective 2026-03-04) and downstream workspace plan/roadmap guidance/templates aligned to P-STD-002 canonical status authority. Added TK005/TK006 implementation dev-report link. |
| v0.5.0 | 2026-03-06 | Amendment | Reworked AC003 for Gate-003 implementation readiness. Added `procedural_guideline` frontmatter. Reassigned TK005/TK006 to `LLM_Developer`. Re-specified TK007 as an `assessment` analysis with canonical path, TK008 as a `standards_input` proposal with canonical path, added TK009 reviewer verification, added TK010 Gate-003 package preparation (valid `external_review` analysis + authoritative `gate_disposition` proposal), and added detailed `GATE-003` structure. Normalized TK004/GATE-001 wording to current GDR authority model. Expanded Links Register with new deliverables and SES004 notes artifact. Evidence: SES004. |
| v0.4.0 | 2026-03-04 | Amendment | Gate-001 final closure: updated GATE-001 task register row with authoritative GDR reference (proposal-embedded, supersedes verification GDR per SES003-DEC001). Registered TK007 (retention-policy ownership, GIR-003 follow-on) and TK008 (stale-state governance operationalization, GIR-004 follow-on) with detailed task specifications. Added GIR-005 informative future-scope note. Updated Links Register. Evidence: SES003. |
| v0.3.3 | 2026-03-01 | Gate closure | Updated GATE-001 status to `completed` after Client Decision recorded in the primary verification artifact (`verification_P-PH000-ST001-AC003_gate-001.md` v1.1.0; APPROVE WITH CONDITIONS). Refreshed TK004 Task Register row to reflect consultation re-assessment findings and GDR closure. |
| v0.3.2 | 2026-02-27 | Housekeeping | Updated TK002/TK003 to `completed` with evidence in Task Register; added missing TK001.1 detailed task section in Â§III for traceability (proposal + mapping inputs â†’ verification output); reframed TK004 as reviewer-owned gate verification artifact task (per `guideline_workspace_verification.md`) and updated GATE-001 entry criteria; refreshed Context and Links Register to reflect implemented deliverables. Evidence: `dev-report_P-PH000-ST001-AC003_tk002-tk003-execution_2026-02-27.md`. |
| v0.3.0 | 2026-02-27 | Amendment | TK001.1 (CDR readiness review, CONDITIONAL PASS / APPROVE WITH CONDITIONS) inserted into task register; TK002 `Depends On` updated to `TK001.1`; TK002 steps 10â€“14 added (forward-only adoption CLAUSE, D-9 reserved section header, aggregation mode definitions table, extensibility hook mechanism, evidence anchor platform-agnostic language); TK003 steps 7â€“8 added (risk-mitigation traceability table, CDR-03 treatment explanation); TK002 and TK003 success criteria enriched; TK001.1 verification deliverable added to Links Register. Evidence: CDR readiness review session 2026-02-27. |
| v0.2.1 | 2026-02-27 | Amendment | QA alignment: TK001 deliverables clarified to include a 54-theme mapping artifact (A-1..E-12) and a 13-binding-decision CDR proposal (CDR-01, CDR-02, CDR-04..CDR-14). Final `P-STD-002-CLAUSE-###` numbering deferred to TK002 authoring. TK000/TK001 marked completed. |
| v0.2.0 | 2026-02-26 | Amendment | Plan amendment incorporating P-RES-002 research integration. Changes: (1) removed DRAFT banner, (2) added dual dependency on ST004-AC001 + ST004-AC002, (3) expanded TK001 scope to ingest both integration recommendation packages and produce CDR resolution proposal at `proposal/`, (4) enriched TK002 scope with 13 P-RES-002-originated CLAUSE themes (54 total), (5) enriched TK003 scope to cite both research inputs and address 13 consolidated decisions, (6) updated Links Register with research inputs and proposal deliverable. Evidence: consultant session 2026-02-26. |
| v0.1.0 | 2026-02-23 | Initial | Draft activity plan created from AC003-SES001 consultation. Task register and CLAUSE domains are draft; subject to amendment after P-RES-001 integration sign-off (P-PH000-ST004-AC001-GATE-003). Evidence: `raw_P-PH000-ST001-AC003-SES001.txt` |
