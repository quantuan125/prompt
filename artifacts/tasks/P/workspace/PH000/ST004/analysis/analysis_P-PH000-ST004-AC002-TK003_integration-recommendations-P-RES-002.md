---
artifact_type: 'ANALYSIS'
initiative_id: 'P'
initiative_code: 'PROGRAM'
phase: '0'
stream_id: 'P-PH000-ST004'
activity_id: 'P-PH000-ST004-AC002'
task_id: 'P-PH000-ST004-AC002-TK003'
research_id: 'P-RES-002'
version: '2.0.0'
date: '2026-02-26'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
purpose: 'Integration recommendations package for P-STD-002 CLAUSE authoring — SSOT alignment, CLAUSE domain mapping, combined research synthesis (P-RES-001 + P-RES-002), AC003/ST002 activity integration guidance, and consolidated decision register'
classification: 'formal_deliverable'
primary_inputs:
  - 'prompt/artifacts/tasks/P/research/P-RES-002/report_P-RES-002_agentic-status-research.md'
  - 'prompt/artifacts/tasks/P/research/P-RES-002/brief_P-RES-002_agentic-status-research.md'
  - 'prompt/artifacts/tasks/P/workspace/PH000/ST004/analysis/analysis_P-PH000-ST004-AC001-TK003_integration-recommendations-P-RES-001.md'
  - 'prompt/artifacts/tasks/P/ssot/sps_P-PROGRAM.md'
consumer: 'P-PH000-ST001-AC003-TK001'
---

# ANALYSIS: Integration Recommendations Package — P-RES-002 (Agentic Status Systems Research) for P-STD-002 CLAUSE Authoring

> **Boundary**: This package is **recommendations-only**. No P-STD-002 CLAUSE text is drafted. The consumer is `P-PH000-ST001-AC003-TK001`.

---

## I. EXECUTIVE SUMMARY

**Verdict**: `P-RES-002` findings are **ready for P-STD-002 v1 CLAUSE authoring** and SHOULD be incorporated as:
1) a normative **evidence linkage** basis (GitHub Checks as primary, commit statuses as fallback), and
2) a normative **execution reference submodel** (run/check/job identifiers + aggregation policy) that bridges agentic CLI and CI/CD evidence into program governance, **without** changing the canonical 7-state program status vocabulary.

**Combined research readiness**: Both P-RES-001 and P-RES-002 integration recommendation packages are now complete. All 12 P-RES-002 integration points flagged in the P-RES-001 analysis (Section VII) are resolved. The two packages produce a unified, non-conflicting recommendation set across all five P-STD-002 CLAUSE domains.

**Key integration decisions requiring Client input before or during authoring** (13 total — see Section X for consolidated register):
1. **Execution model boundary** (`P-STD-002A/E`): Whether tool execution states become part of the status enum. Recommendation: **no**; keep tool execution as non-status governed fields.
2. **Evidence anchor** (`P-STD-002D/E`): Checks API as primary evidence primitive. Recommendation: **standardize Checks as primary**; permit commit status fallback.
3. **Aggregation policy** (`P-STD-002B/D`): Define canonical parent/child rollup rules. Recommendation: **make aggregation policy explicit and required** for multi-check evidence.
4. **Manual gate semantics** (`P-STD-002A/D`): Governance mapping for "waiting approval/manual" states. Recommendation: map to `on_hold` (policy wait) vs `blocked` (unmet prerequisite).

**Package structure**:
- Section II: SSOT Alignment Checklist (10 entries)
- Section III: P-STD-002 CLAUSE Domain Mapping (5 domains, P-RES-002 specific)
- Section IV: Cross-Topic Integration Summary (P-RES-002 internal)
- Section V: Carry-Forward Issues & Risks
- Section VI: Handoff to AC003 (Consumer Guidance)
- Section VII: Combined Research Synthesis (P-RES-001 + P-RES-002 Reconciliation)
- Section VIII: AC003 Task-Level Impact & Amendment Recommendations
- Section IX: ST002 Integration Guidance
- Section X: Consolidated Decision Register (13 decisions)
- Section XI: Sources & Traceability

---

## II. SSOT ALIGNMENT CHECKLIST

Alignment is checked against `prompt/artifacts/tasks/P/ssot/sps_P-PROGRAM.md` (v0.6.0, 2026-02-25).

### A. Constraints

| SPS Entry | Title | Alignment Check | Result | Notes |
|:--|:--|:--|:--:|:--|
| `P-CON-001` | Authority Boundary | All recommendations remain within `prompt/artifacts/tasks/**` governance scope; external evidence is referenced via links/IDs rather than expanding authority. | **PASS** | Evidence pointers reference GitHub artifacts, commits, PRs; governance artifacts remain inside program workspace. |
| `P-CON-002` | Link Don't Duplicate | Evidence linkage uses pointers (URLs/IDs/paths); no recommendation requires copying external logs into normative artifacts. | **PASS** | Execution traces are optional; prefer pointer-based evidence and summaries. |
| `P-CON-003` | Artifact Format Governance | Recommends machine-readable evidence/ledger fields (permitted as non-MD artifacts when governed) alongside MD narrative summaries. | **PASS** | Any non-MD ledger format must be explicitly authorized in `P-STD-002E` citing `P-CON-003(B)`. |

### B. Assumptions

| SPS Entry | Title | Alignment Check | Result | Notes |
|:--|:--|:--|:--:|:--|
| `P-ASSUM-001` | Forward-only Adoption | Evidence linkage and execution reference fields can be adopted on next-touch, without retroactive migration of old artifacts. | **PASS** | `P-STD-002` should include a forward-only adoption clause for the new evidence/execution fields. |

### C. Quality Goals

| SPS Entry | Title | Alignment Check | Result | Notes |
|:--|:--|:--|:--:|:--|
| `P-QG-001` | Deterministic Retrieval | Requires stable identifiers (PR number, commit SHA, check run IDs) and deterministic paths for any ledger artifacts. | **PASS** | The execution reference submodel is ID-centric; placement rules must defer to `P-STD-004` once authored. |
| `P-QG-002` | Traceability Integrity | Evidence linkage and aggregation policies explicitly support "link-don't-duplicate" traceability. | **PASS** | Terminal transitions should require evidence pointers to repo-native primitives (checks/PR/commit). |

### D. Dependencies

| SPS Entry | Title | Alignment Check | Result | Notes |
|:--|:--|:--|:--:|:--|
| `P-DEP-001` | T102 Standards Stack | Research artifacts follow `T102-STD-006`; issues/risks conform to `T102-STD-007`. | **PASS** | `P-STD-002` should reference the adopted patterns without duplicating their normative text. |

### E. Interfaces

| SPS Entry | Title | Alignment Check | Result | Notes |
|:--|:--|:--|:--:|:--|
| `P-IF-001` | Status Interface | Execution references + evidence pointers provide a practical machine-readable interface surface for agentic update protocols. | **PASS** | `P-STD-002E` should explicitly declare the "execution references" fields as part of the status interface. |

---

## III. P-STD-002 CLAUSE DOMAIN MAPPING (P-RES-002 RECOMMENDATIONS)

> This section maps P-RES-002 findings to P-STD-002 CLAUSE domains. P-RES-001 recommendations (see `analysis_P-PH000-ST004-AC001-TK003`) remain the baseline; this section defines what P-RES-002 **adds or extends**.

### Domain A: Status Vocabulary (`P-STD-002A`)

**Do not change**: the canonical 7-state program status vocabulary from the P-RES-001 baseline.

**Add governed fields (non-status)**:
1. **Execution posture** (when agentic tooling is used):
   - `approval_policy` (e.g., auto vs gated) and `sandbox_mode` (where applicable)
2. **Manual-gate semantics**:
   - `manual_gate: true/false`
   - `manual_gate_reason: policy_wait | unmet_prerequisite | human_review_required`
3. **Crosswalk guidance (informative)**:
   - Mapping of common tool/CI "waiting/manual" and "failed" conditions to program `blocked` vs `on_hold`

**Recommended CLAUSE theme additions** (extends P-RES-001 Domain A):

| # | CLAUSE Theme | Scope | Sourced From | Priority |
|--:|:--|:--|:--|:--|
| A-10 | **Execution Posture Fields (non-status)** | When agentic or CI tooling is used, status entries MAY carry governed non-status metadata: `approval_policy`, `sandbox_mode`. These are execution context, not program status. | P-RES-002 Topic 1 | Medium |
| A-11 | **Manual-Gate Crosswalk (informative)** | Informative guidance mapping tool/CI "manual gate" and "waiting for approval" states to the program's `on_hold` vs `blocked` distinction based on cause. | P-RES-002 Topic 1, Topic 7 | Medium |

**Rationale**: Tool/CI execution state is essential evidence but should not redefine program status.

---

### Domain B: Health Assessment (`P-STD-002B`)

**Add one governance rule** (extends P-RES-001 Domain B):

| # | CLAUSE Theme | Scope | Sourced From | Priority |
|--:|:--|:--|:--|:--|
| B-7 | **Allowed-Failure Health Impact Rule** | If any evidence set in a status update uses `allow_failure` or `continue_on_error` aggregation policy, the health assessment MUST reflect this explicitly (minimum: Amber unless an exception rationale is recorded and linked). Silent "green with hidden failures" is prohibited. | P-RES-002 Topic 4, Risk-002 | Critical |

**Rationale**: Prevents CI/orchestration "green pipeline with allowed failures" from misleading program governance health signals.

---

### Domain C: Dependency Visibility (`P-STD-002C`)

**Add evidence-facing orchestration references (non-status)** (extends P-RES-001 Domain C):

| # | CLAUSE Theme | Scope | Sourced From | Priority |
|--:|:--|:--|:--|:--|
| C-10 | **Orchestration Reference Fields (optional)** | Dependency edges that are materialized as CI/orchestration jobs MAY carry optional fields: `platform` (`github_actions` / `gitlab_ci` / `other`), `run_id`/`pipeline_id`, and job/step dependency identifiers. | P-RES-002 Topic 3, Topic 4 | Medium |
| C-11 | **Category Taxonomy Extension** | The permitted `category` extensions (Domain C CLAUSE 3) MAY include: `orchestration` (CI/CD job dependency), `pipeline_gate` (manual approval stage), `agent_handoff` (multi-agent delegation). | P-RES-002 Topic 4 | Low |

**Rationale**: Orchestration is graph-shaped; dependency visibility should not rely on narrative when structured references exist.

---

### Domain D: Update Protocol (`P-STD-002D`)

**Add normative evidence requirements** (extends P-RES-001 Domain D):

| # | CLAUSE Theme | Scope | Sourced From | Priority |
|--:|:--|:--|:--|:--|
| D-10 | **Repo-Verifiable Evidence Requirement** | Terminal transitions (`completed`, `cancelled`) MUST cite at least one repo-verifiable evidence pointer: GitHub Check run, PR/MR, commit SHA, or workflow/pipeline run. | P-RES-002 Topic 5, Topic 6 | Critical |
| D-11 | **Evidence Type Taxonomy Extension** | Extend P-RES-001 evidence type taxonomy (Domain D CLAUSE 2) with: `check` (GitHub Check run), `workflow_run` (CI pipeline execution), `execution_trace` (optional, for structured JSONL/JSON output). | P-RES-002 Topic 5, Topic 6 | High |
| D-12 | **Aggregation Policy Declaration** | When a status update references nested/parallel evidence (multiple checks, jobs, steps), the update MUST declare the aggregation policy used: `fail_fast`, `allow_failure`, `continue_on_error`, or `manual_gate`. | P-RES-002 Topic 2, Topic 4 | Critical |
| D-13 | **Silent Allowed-Failure Prohibition** | Status transitions to `completed` MUST NOT rely on evidence sets containing allowed failures without explicit exception rationale linked to the transition record. | P-RES-002 Topic 4, Risk-002 | Critical |

**Rationale**: Makes automated and human evidence validation deterministic.

---

### Domain E: Status Artifact (`P-STD-002E`)

**Add/require schema elements** (extends P-RES-001 Domain E):

| # | CLAUSE Theme | Scope | Sourced From | Priority |
|--:|:--|:--|:--|:--|
| E-9 | **Execution Reference Schema** | The ledger schema MUST support optional execution reference entries: `{platform, run_id, check_run_id, url, status, conclusion, started_at, completed_at}`. These are evidence-bearing, not status-bearing. | P-RES-002 Topic 1, Topic 5 | High |
| E-10 | **Aggregation Policy Field** | The ledger schema MUST support an `aggregation_policy` field per status entry when the evidence set is nested/parallel. | P-RES-002 Topic 2, Topic 4 | High |
| E-11 | **Execution Posture Fields (optional)** | The ledger schema MAY include `approval_posture` and `sandbox_mode` fields to record the agentic execution context at time of status update. | P-RES-002 Topic 1 | Medium |
| E-12 | **Minimum Viable Audit Trail (MVAT)** | Define the minimum required fields per status ledger entry: program status (7-state) + timestamp + author role + evidence pointer(s) + aggregation policy (if multi-evidence) + rationale pointer (narrative link). | P-RES-002 Topic 6 | High |

**Format guidance** (consistent with `P-CON-003`):
* Narrative status remains Markdown; machine ledger MAY be YAML/JSON if explicitly authorized under `P-CON-003(B)`.

---

## IV. CROSS-TOPIC INTEGRATION SUMMARY (P-RES-002 INTERNAL)

1. **CLI (Topic 1) ↔ CI (Topic 3)**: Both are best bridged via repo-native primitives (checks, PRs, commits). CLI-specific internal states should be captured as execution posture/evidence, not as the program status enum.
2. **Nested execution (Topic 2) ↔ Orchestration aggregation (Topic 4)**: Use one canonical governance aggregation policy vocabulary (`fail_fast` / `allow_failure` / `continue_on_error` / `manual_gate`) applied consistently to both agentic substeps and CI job graphs.
3. **Repo-native surfacing (Topic 5) ↔ Audit trails (Topic 6)**: Prefer Checks as the primary evidence anchor because it supports rich output/annotations and deterministic linking.

**vNext (Topic 7)**:
* Bridging patterns beyond minimal evidence/execution references (e.g., cross-initiative rollups, multi-repo aggregation services) should be treated as informational and deferred unless explicitly commissioned.

---

## V. CARRY-FORWARD ISSUES & RISKS (FROM P-RES-002)

**Issues**
* `P-RES-002-ISSUE-001` — Agentic CLI run status enums are not standardized in official docs across vendors; standardize cross-tool primitives (approval state, sandbox state, event streams) instead of vendor-specific enums.
* `P-RES-002-ISSUE-002` — GitHub docs/version drift; pin citations to specific doc sources and avoid undocumented status/conclusion values.

**Risks**
* `P-RES-002-RISK-001` — Checks-only evidence might reduce portability; mitigate via fallback to commit statuses + API-agnostic minimum evidence-pointer schema.
* `P-RES-002-RISK-002` — Silent allowed failures degrade governance; mitigate via explicit aggregation policy requirement and health impact rule (Domain B CLAUSE B-7).

---

## VI. HANDOFF TO AC003 (CONSUMER GUIDANCE)

When executing `P-PH000-ST001-AC003-TK001` (map research to CLAUSE domains), integrate `P-RES-002` as:
1) **Evidence linkage foundation** (P-STD-002D/E), and
2) **Execution reference schema** (P-STD-002E) + aggregation vocabulary (P-STD-002B/D),
without altering the canonical 7-state program status enum (`P-STD-002A`).

Consumer must ingest **both** integration recommendation packages:
- `analysis_P-PH000-ST004-AC001-TK003_integration-recommendations-P-RES-001.md` (baseline)
- `analysis_P-PH000-ST004-AC002-TK003_integration-recommendations-P-RES-002.md` (this file)

Section VII below reconciles the two packages into a unified view.

---

## VII. COMBINED RESEARCH SYNTHESIS (P-RES-001 + P-RES-002)

> This section reconciles the P-RES-002 integration points flagged in the P-RES-001 analysis with actual P-RES-002 findings. All 12 flagged integration points are resolved below.

### A. Domain-by-Domain Reconciliation

#### Domain A: Status Vocabulary (`P-STD-002A`)

**P-RES-001 flagged integration points**:
1. *"Agentic CLI task/run lifecycle statuses may suggest additional mapping rules or nuances for `blocked` vs `on_hold` in automated contexts (e.g., a 'waiting_for_input' state common in agent tools)."*
2. *"P-STD-002A CLAUSE 9 (Blocked/On-Hold semantics) may benefit from P-RES-002 evidence on how agentic tools distinguish impediment types."*

**P-RES-002 resolution**: **Both resolved — no structural change to Domain A**.
- P-RES-002 Topic 1 confirms agentic tools use "manual gate" and "waiting for approval" states, but these are session-level execution controls, not program status states.
- P-RES-002 Topic 7 recommends a crosswalk: map `manual_gate` by cause — `policy_wait` → `on_hold`; `unmet_prerequisite` → `blocked`; `human_review_required` → `on_hold`.
- This resolves into CLAUSE theme A-11 (Manual-Gate Crosswalk, informative) without changing the 7-state enum or the Domain A CLAUSE structure from P-RES-001.

**Unified recommendation**: P-RES-001's 9 CLAUSE themes for Domain A stand as baseline. Add CLAUSE themes A-10 (execution posture, non-status) and A-11 (manual-gate crosswalk, informative). Total: **11 CLAUSE themes**.

---

#### Domain B: Health Assessment (`P-STD-002B`)

**P-RES-001 flagged integration point**:
1. *"Agentic orchestration patterns may suggest health dimensions specific to automated pipeline execution (e.g., 'reliability' or 'throughput'). Flag: CLAUSE 5 (initiative configuration) already permits optional additional dimensions, so P-RES-002 recommendations can be absorbed without structural changes."*

**P-RES-002 resolution**: **Resolved — one governance rule added, no new dimensions**.
- P-RES-002 does not recommend new health dimensions. Instead, it identifies a gap: CI/orchestration systems can report "green" with silently allowed failures (Topic 4, GitLab `allow_failure` observation).
- P-RES-002 recommends a governance rule: allowed-failure evidence must result in minimum Amber health unless an explicit exception rationale is documented.
- P-RES-001's existing CLAUSE 5 (initiative configuration) is sufficient for any future dimension additions.

**Unified recommendation**: P-RES-001's 6 CLAUSE themes for Domain B stand as baseline. Add CLAUSE theme B-7 (allowed-failure health impact rule). Total: **7 CLAUSE themes**.

---

#### Domain C: Dependency Visibility (`P-STD-002C`)

**P-RES-001 flagged integration points**:
1. *"GitHub Actions job/step dependency DAGs may inform the graph-first schema design (particularly hierarchical/nested dependency patterns)."*
2. *"Multi-agent orchestration status aggregation patterns may extend the `category` taxonomy (e.g., `agent_handoff`, `pipeline_gate`)."*
3. *"Cross-repo dependency patterns from GitHub ecosystem may extend the `external` category with specific sub-types."*

**P-RES-002 resolution**: **All resolved — optional extensions, no structural change to schema**.
- P-RES-002 Topics 3-4 confirm CI/CD DAG patterns are graph-shaped, validating P-RES-001's graph-first schema recommendation. No schema structural change needed.
- P-RES-002 recommends optional orchestration reference fields (`platform`, `run_id`, `pipeline_id`) on dependency edges where CI/CD materializes them.
- Category taxonomy extensions (`orchestration`, `pipeline_gate`, `agent_handoff`) fit within P-RES-001's existing CLAUSE 3 extensibility model.
- Cross-repo dependencies are implicitly covered by `external` category; no new sub-type taxonomy is required for P-STD-002 v1.

**Unified recommendation**: P-RES-001's 9 CLAUSE themes for Domain C stand as baseline. Add CLAUSE themes C-10 (orchestration reference fields, optional) and C-11 (category taxonomy extensions). Total: **11 CLAUSE themes**.

---

#### Domain D: Update Protocol (`P-STD-002D`)

**P-RES-001 flagged integration points**:
1. *"Agentic CLI audit trail patterns may suggest automated evidence capture (e.g., session telemetry or tool output as evidence type). Flag: CLAUSE 2 (evidence type taxonomy) may benefit from P-RES-002 evidence on what constitutes 'evidence' in agentic workflows."*
2. *"Repo-native audit patterns (Git commits, PR links, GitHub Checks) may inform the evidence type taxonomy and validation rules."*
3. *"GitHub-based orchestration status patterns may suggest additional update protocol conventions for automated status transitions."*

**P-RES-002 resolution**: **All resolved — taxonomy extended, aggregation policy added**.
- P-RES-002 Topics 5-6 provide concrete evidence for extending the evidence type taxonomy with: `check` (GitHub Check run — the richest, most governance-suitable repo-native primitive, scored 89/95), `workflow_run` (CI pipeline execution), and `execution_trace` (optional, for structured JSONL/JSON output from Codex CLI or Gemini CLI).
- P-RES-002 Topics 2 and 4 identify a critical gap: nested/parallel evidence sets (multiple checks, matrix jobs, parallel agents) require an explicit aggregation policy declaration to make status computation deterministic. Without this, parent-level status becomes ambiguous.
- P-RES-002 Topic 5 recommends GitHub Checks as the primary evidence anchor (vs commit statuses as fallback), scored on the evaluation rubric (Checks: 89/95 vs Commit Status: 65/95).

**Unified recommendation**: P-RES-001's 9 CLAUSE themes for Domain D stand as baseline. Add CLAUSE themes D-10 (repo-verifiable evidence requirement), D-11 (evidence type taxonomy extension), D-12 (aggregation policy declaration), and D-13 (silent allowed-failure prohibition). Total: **13 CLAUSE themes**.

**Decision surface interaction**: P-RES-002 decision RES2-DEC-1 (Checks as primary) reinforces and extends P-RES-001 decision D-DEC-1 (evidence validation normative). These are consolidated as CDR-09 in Section X.

---

#### Domain E: Status Artifact (`P-STD-002E`)

**P-RES-001 flagged integration points**:
1. *"Agentic CLI status artifact patterns (e.g., how Claude Code / Codex CLI persist task/run state) may inform the ledger schema design — particularly hierarchical task representation."*
2. *"GitHub Checks API / commit status patterns may suggest status surfacing conventions that influence the narrative template."*
3. *"Repo-native status file patterns may validate or challenge the dual-artifact model."*

**P-RES-002 resolution**: **All resolved — schema enriched, dual-artifact model validated**.
- P-RES-002 Topic 1 shows agentic CLIs do not publish a single comparable "status artifact" — they publish session-level controls (approvals, sandboxing) and event streams. This validates P-RES-001's ledger-based approach as the program's canonical model (tools contribute evidence; program governs status).
- P-RES-002 Topics 5-6 identify concrete schema enrichments: execution references (check run IDs, workflow run IDs, URLs), aggregation policy fields, and optional execution posture fields. These fit naturally into P-RES-001's CLAUSE theme E-4 (Ledger Schema Requirements).
- P-RES-002 Topic 6 defines a Minimum Viable Audit Trail (MVAT) pattern that aligns with P-RES-001's dual-artifact authority hierarchy. The MVAT can serve as the baseline specification for what a ledger entry MUST contain.
- The dual-artifact model is confirmed, not challenged. No repo-native pattern from P-RES-002 suggests a different cardinality.

**Unified recommendation**: P-RES-001's 8 CLAUSE themes for Domain E stand as baseline. Add CLAUSE themes E-9 (execution reference schema), E-10 (aggregation policy field), E-11 (execution posture fields, optional), and E-12 (MVAT definition). Total: **12 CLAUSE themes**.

---

### B. Combined Recommendation Totals

| Domain | P-RES-001 Baseline | P-RES-002 Additions | Combined Total | Structural Change? |
|:--|--:|--:|--:|:--|
| P-STD-002A (Status Vocabulary) | 9 | 2 | **11** | No (7-state stable) |
| P-STD-002B (Health Assessment) | 6 | 1 | **7** | No (governance rule only) |
| P-STD-002C (Dependency Visibility) | 9 | 2 | **11** | No (optional fields) |
| P-STD-002D (Update Protocol) | 9 | 4 | **13** | Yes (aggregation policy is new normative concept) |
| P-STD-002E (Status Artifact) | 8 | 4 | **12** | Yes (execution reference schema is new schema section) |
| **Totals** | **41** | **13** | **54** | — |

**Observation**: P-RES-002 introduces 13 additional CLAUSE themes (32% increase) across all five domains. The two domains with structural impact (D and E) are the most operationally significant — they define how evidence flows into governance. This aligns with P-RES-002's core verdict: "execution reference submodel + evidence linkage."

---

### C. Non-Conflicting Confirmation

No P-RES-002 recommendation contradicts any P-RES-001 recommendation. The two packages are fully complementary:
- P-RES-001 defines the **governance model** (status vocabulary, health dimensions, dependency schema, update protocol, artifact specification).
- P-RES-002 defines the **evidence bridge** (what constitutes evidence in an agentic/CI ecosystem, how to link it, and how to aggregate it).

Both independently align with all SSOT constraints (Section II in each package).

---

## VIII. AC003 TASK-LEVEL IMPACT & AMENDMENT RECOMMENDATIONS

> This section provides specific task-register amendment proposals for `P-PH000-ST001-AC003` (Author P-STD-002) based on combined research findings. These proposals are intended as input to the AC003 plan amendment session per `guideline_workspace_plan.md`.

### A. Dependency Update

**Current AC003 dependency**: `P-PH000-ST004-AC001` (P-RES-001 integration sign-off via GATE-003)

**Required amendment**: Add explicit dependency on `P-PH000-ST004-AC002-GATE-003` (P-RES-002 integration sign-off).

**Rationale**: ST004 dependency notes (Section IV) state: *"P-PH000-ST001-AC003 depends on BOTH AC001 GATE-003 and AC002 GATE-003 sign-off."* This dependency is currently implicit in the stream plan but not explicit in the AC003 activity plan or task register.

### B. Task-Level Amendment Proposals

#### TK001: Ingest Research Recommendations

**Current scope**: Ingest P-RES-001 report recommendations and map to CLAUSE domains.

**Proposed amendment**: Expand to ingest **both** P-RES-001 and P-RES-002 integration recommendation packages (this file + the P-RES-001 analysis). Use the combined CLAUSE theme tables (Section VII.B, 54 total themes) and the consolidated decision register (Section X, 13 decisions) as the working input for CLAUSE domain mapping.

**Proposed TK001 inputs** (amended):
- `analysis_P-PH000-ST004-AC001-TK003_integration-recommendations-P-RES-001.md` — P-RES-001 baseline
- `analysis_P-PH000-ST004-AC002-TK003_integration-recommendations-P-RES-002.md` — P-RES-002 complement (this file)

**Proposed TK001 deliverable** (amended): Combined CLAUSE domain mapping with all 54 themes assigned to specific `P-STD-002-CLAUSE-###` slots and all 13 consolidated decisions resolved.

#### TK002: Draft P-STD-002 Specification

**Proposed scope enrichment**: The Specification section must now incorporate the following P-RES-002-originated content beyond the P-RES-001 baseline:

| P-STD-002 Domain | P-RES-002 Content to Author | CLAUSE Themes |
|:--|:--|:--|
| A (Status Vocabulary) | Execution posture fields (non-status) + manual-gate crosswalk (informative) | A-10, A-11 |
| B (Health Assessment) | Allowed-failure health impact rule | B-7 |
| C (Dependency Visibility) | Orchestration reference fields (optional) + category taxonomy extensions | C-10, C-11 |
| D (Update Protocol) | Repo-verifiable evidence requirement + evidence type taxonomy extension + aggregation policy declaration + silent allowed-failure prohibition | D-10, D-11, D-12, D-13 |
| E (Status Artifact) | Execution reference schema + aggregation policy field + execution posture fields (optional) + MVAT definition | E-9, E-10, E-11, E-12 |

**Note**: CLAUSE numbering (`P-STD-002-CLAUSE-###`) will be determined during TK002 authoring. The theme numbers above (e.g., A-10) are mapping identifiers from this analysis, not CLAUSE IDs.

#### TK003: Draft P-STD-002-ADR-001

**Proposed scope enrichment**: The embedded decision record must cite **both** P-RES-001 and P-RES-002 research findings as context. The Decision section must address all 13 consolidated decisions (Section X), particularly:
- CDR-01 (execution model boundary) — the fundamental architectural decision
- CDR-09 (evidence anchor + validation) — the key operational decision
- CDR-10 (aggregation policy) — the key agentic/CI-specific addition

#### TK004 through TK006: No P-RES-002-specific amendments required

These tasks (validation, SPS update, guideline cascade) do not require P-RES-002-specific scope changes. TK004 validation will naturally cover the P-RES-002-originated CLAUSEs. TK006 guideline cascade may need to reference aggregation policy vocabulary if any guideline files reference evidence patterns, but this is determined during TK006 execution.

---

### C. Proposed AC003 Task Register (Amended View)

> This is a recommendation for the AC003 plan amendment session, not a direct amendment to the AC003 plan.

| Task | Task ID | Name | Status | Depends On | Amendment Type |
|:--|:--|:--|:--|:--|:--|
| TK000 | `P-PH000-ST001-AC003-TK000` | Confirm sps_P P-CON-003 amendment applied | `planned` | — | No change |
| TK001 | `P-PH000-ST001-AC003-TK001` | Ingest P-RES-001 **and P-RES-002** report recommendations and map to CLAUSE domains | `planned` | ST004-AC001-GATE-003 **+ ST004-AC002-GATE-003** | **Scope expanded**: dual-package ingestion; 54 CLAUSE themes; 13 consolidated decisions |
| TK002 | `P-PH000-ST001-AC003-TK002` | Draft P-STD-002 combined file: Specification section | `planned` | TK001 | **Scope enriched**: 13 additional CLAUSE themes from P-RES-002 |
| TK003 | `P-PH000-ST001-AC003-TK003` | Draft P-STD-002-ADR-001 in Decision Record section | `planned` | TK002 | **Scope enriched**: cite both research inputs; address 13 consolidated decisions |
| TK004 | `P-PH000-ST001-AC003-TK004` | Validate P-STD-002 against P-STD-001 authoring rules | `planned` | TK003 | No change |
| GATE-001 | `P-PH000-ST001-AC003-GATE-001` | Gate: Client acceptance of P-STD-002 | `planned` | TK004 | No change |
| TK005 | `P-PH000-ST001-AC003-TK005` | Update sps_P P-STD-002 row | `planned` | GATE-001 | No change |
| TK006 | `P-PH000-ST001-AC003-TK006` | Cascade P-STD-002 status enums to downstream guideline files | `planned` | GATE-001 | Minor: may cascade aggregation policy vocabulary if guideline files reference evidence patterns |

---

## IX. ST002 INTEGRATION GUIDANCE

> This section addresses how `P-PH000-ST002` (Program Status System) activities should absorb combined research findings.

### A. ST002-AC001: Schema + Protocol (Informative Seed)

**Current state**: ST002-AC001 defines an informative seed schema (YAML frontmatter + `initiatives:` payload) with a locked update protocol. Per SES001-DEC-002, this schema is explicitly annotated as *"informative seed input only"* — the authoritative contract resides in `P-STD-002` once accepted.

**Combined research impact**:
1. The seed schema captures the minimum structural concept (initiative → phase → streams → status). This is **still valid** as a starting point.
2. P-STD-002 will **supersede** the seed schema with enriched requirements including:
   - Evidence pointers per status entry (P-RES-001 Domain D + P-RES-002 Domain D extensions)
   - Health dimensions per the 6-dimension RAG model (P-RES-001 Domain B)
   - Dependency edges per the graph-first schema (P-RES-001 Domain C + P-RES-002 optional orchestration references)
   - Execution references (P-RES-002 Domain E additions: check run IDs, workflow run IDs)
   - Aggregation policy per status entry (P-RES-002 Domain D/E additions)
3. The update protocol concept (canonical-first, version-controlled, changelog) is **validated** by both research packages.

**Recommendation**: No amendment to ST002-AC001 is needed at this time. The seed serves its purpose as a conceptual anchor. When ST002-AC002 (create `status_program.md`) is executed post-AC003, it will implement the P-STD-002E-governed schema, which will be substantially richer than the seed but architecturally consistent with it.

### B. ST002-AC002: Author `status_program.md` (Deferred)

**Current state**: Deferred implementation activity, depends on P-PH000-ST001-AC003 (P-STD-002 acceptance).

**Combined research impact**:
1. **Dependency is unchanged**: AC002 correctly depends on P-STD-002 acceptance.
2. **Schema implementation will be richer**: The implementer should expect to create a ledger artifact with:
   - 7-state status per initiative/stream (P-RES-001 Domain A)
   - 6 health dimensions with RAG values (P-RES-001 Domain B)
   - Dependency edges with required fields (P-RES-001 Domain C)
   - Evidence pointer arrays per status entry (P-RES-001 Domain D + P-RES-002 extensions)
   - Optional execution reference entries (P-RES-002 Domain E)
   - Aggregation policy field when multi-evidence (P-RES-002 Domain D)
   - MVAT-compliant minimum fields per entry (P-RES-002 Domain E)
3. **Dual-artifact model**: ST002-AC002 must produce both the canonical ledger (primary) and a derived Markdown narrative (secondary), per P-RES-001 Domain E recommendations.

**Recommendation**: No plan amendment needed for ST002-AC002 at this time. The activity is correctly deferred and correctly dependent. When activated, it should reference the accepted P-STD-002 as its normative authority, not the seed schema in ST002-AC001.

### C. Combined Dependency Chain (Verified)

```
P-PH000-ST004-AC001-GATE-003 (P-RES-001 integration sign-off)  ──┐
P-PH000-ST004-AC002-GATE-003 (P-RES-002 integration sign-off)  ──┼── P-PH000-ST001-AC003 (Author P-STD-002)
                                                                  │         │
                                                                  │         ▼
                                                                  │   P-PH000-ST002-AC002 (Create status_program.md)
                                                                  │
                                                                  └── P-PH000-ST002-AC001 (Seed schema — informative only, no gate dependency)
```

---

## X. CONSOLIDATED DECISION REGISTER

> Merges all Client-facing decisions from P-RES-001 analysis (9 decisions) and P-RES-002 analysis (4 decisions) into a single prioritized surface for AC003 consumption. Decisions are ordered by priority (Critical → High → Medium → Low) and sequenced for logical dependency within each priority tier.

### A. Critical Decisions (must resolve before or during TK002)

| CDR # | Source ID(s) | Domain(s) | Decision | Options | Recommendation | Rationale | Cross-Ref |
|:--:|:--|:--|:--|:--|:--|:--|:--|
| CDR-01 | RES2-DEC-4 | A, E | Should tool execution states (approval_policy, sandbox_mode, run lifecycle) become part of the 7-state program status enum? | (a) Add to enum; (b) Keep as non-status governed fields | **(b) Non-status fields** | Tool execution is evidence context, not program status. Adding vendor-specific lifecycle states to the program enum creates vocabulary drift. P-RES-002 Finding 1: "Tool-level execution state ≠ program-level status." | Governs CDR-02, CDR-04 scope |
| CDR-02 | A-DEC-1 | A | Should `planned` → `in_progress` (skipping `ready`) be a permitted transition? | (a) Permitted with guard; (b) Disallowed | **(b) Disallowed** | `ready` serves as a readiness gate preventing work from starting without minimum preparation. The v2 transition matrix from P-RES-001 Topic 2 disallows this path. | Transition matrix CLAUSE |
| CDR-03 | — | A | Confirm: 7-state canonical vocabulary is stable across both research inputs? | (a) Stable (confirmed); (b) Needs revision | **(a) Stable** | Both P-RES-001 (Topic 1, weighted score 80/90) and P-RES-002 (Topic 1, verdict) independently confirm the 7-state vocabulary. No evidence from either research stream suggests adding or removing states. | Foundational — affects all domains |
| CDR-09 | D-DEC-1 + RES2-DEC-1 | D | Should evidence validation be normative (MUST) and should GitHub Checks be the primary evidence anchor? | (a) MUST + Checks primary with fallback; (b) SHOULD + any evidence; (c) MUST + no platform preference | **(a) MUST + Checks primary** | Broken evidence pointers undermine traceability (P-QG-002). Checks API scored 89/95 vs Commit Status API 65/95 (P-RES-002 Topic 5). Checks offers richer audit metadata. Commit status fallback preserves portability. | CLAUSE D-4 + D-10 |
| CDR-10 | RES2-DEC-2 | B, D | Should aggregation policy (fail-fast / allow-failure / continue-on-error / manual-gate) be explicitly declared and required for multi-evidence status updates? | (a) Required (MUST); (b) Recommended (SHOULD); (c) Optional (MAY) | **(a) Required** | Without explicit aggregation, parent-level status is ambiguous for both agents and humans. P-RES-002 Finding 3 and Risk-002 document the governance gap. | CLAUSE D-12, B-7 |
| CDR-11 | E-DEC-1 | E | Should P-STD-002E prescribe a normative ledger schema or defer to a companion guideline? | (a) Normative schema; (b) Schema principles only, guideline for details; (c) Schema with extensibility hooks | **(c) Schema with extensibility** | Normative baseline provides interoperability; extensibility hooks allow initiative-specific enrichment. Avoids indirection cost of a separate guideline while remaining adaptable. | CLAUSE E-4 depth |

### B. High Decisions (should resolve before TK002)

| CDR # | Source ID(s) | Domain(s) | Decision | Options | Recommendation | Rationale | Cross-Ref |
|:--:|:--|:--|:--|:--|:--|:--|:--|
| CDR-04 | A-DEC-2 + D-DEC-2 | A, D | Should role restrictions on terminal transitions name specific program roles or use generic RACI labels? | (a) Specific roles (Consultant/Planner/Developer/Reviewer); (b) Generic RACI labels | **(b) RACI labels** | Keeps P-STD-002 role-agnostic; specific role assignment deferred to SPS RACI table. | Guard conditions + role matrix CLAUSEs |
| CDR-05 | RES2-DEC-3 | A, D | How should CI/agentic "manual gate" and "waiting for approval" states map to program status? | (a) Always `on_hold`; (b) Always `blocked`; (c) Map by cause: policy wait → `on_hold`, unmet prerequisite → `blocked` | **(c) Map by cause** | Semantic accuracy: `on_hold` = deliberate suspension, `blocked` = external impediment. Both exist in agentic workflows. Crosswalk guidance as informative. | CLAUSE A-9 enrichment, A-11 |
| CDR-06 | C-DEC-1 | C | Should `owner` on a dependency edge refer to the resolution owner or the reporting owner? | (a) Resolution owner; (b) Reporting owner; (c) Both as separate fields | **(a) Resolution owner** | Primary operational need is knowing who can unblock. Reporting ownership is implicit from the `from_id` entity's owner. | CLAUSE C-1 field semantics |
| CDR-07 | C-DEC-2 | C | Should dependency status use a separate enum or re-use the 7-state vocabulary? | (a) Separate 3-state enum (`open`/`at_risk`/`resolved`); (b) Re-use 7-state | **(a) Separate enum** | Dependencies are edges, not work items. A 3-state lifecycle is cleaner and avoids semantic overloading. | CLAUSE C-5 definition |

### C. Medium Decisions (resolve during TK002)

| CDR # | Source ID(s) | Domain(s) | Decision | Options | Recommendation | Rationale | Cross-Ref |
|:--:|:--|:--|:--|:--|:--|:--|:--|
| CDR-08 | B-DEC-1 | B | Should the standard mandate specific numeric tolerance bands or leave to initiative configuration? | (a) Mandate reference bands; (b) Initiative configuration | **(b) Initiative configuration** | Numeric tolerances are context-dependent; mandating fixed percentages risks false precision. Standard requires that tolerances ARE defined, not WHAT they are. | CLAUSE B-2 specificity |
| CDR-12 | B-DEC-2 | B | Should the `benefits` dimension be required for early-stage initiatives? | (a) Required for all; (b) Required at program, MAY defer at initiative | **(b) Required at program, MAY defer** | Prevents blocking early adoption while ensuring program-level completeness. | CLAUSE B-1 normative language |
| CDR-13 | E-DEC-2 | E | Should the narrative artifact have required sections or be free-form? | (a) Required sections; (b) Free-form; (c) Recommended sections (SHOULD) | **(c) Recommended sections** | Provides consistency without over-constraining. Narrative value is contextual commentary. | Narrative template CLAUSE |

### D. Low Decisions (can defer to Phase 2 or resolve opportunistically)

| CDR # | Source ID(s) | Domain(s) | Decision | Options | Recommendation | Rationale | Cross-Ref |
|:--:|:--|:--|:--|:--|:--|:--|:--|
| CDR-14 | E-DEC-3 | E | Should the optional changelog be a separate file or appendix? | (a) Separate file; (b) Appendix; (c) Standard does not prescribe | **(c) Does not prescribe** | Changelog is optional in v1. Prescribing location before operational experience exists risks premature commitment. | Low impact in v1 |

---

## XI. SOURCES & TRACEABILITY

| Source | Path | Role |
|:--|:--|:--|
| P-RES-002 Report (Iteration 2, accepted) | `prompt/artifacts/tasks/P/research/P-RES-002/report_P-RES-002_agentic-status-research.md` | Primary research input |
| P-RES-002 Brief (v1.0.0, approved) | `prompt/artifacts/tasks/P/research/P-RES-002/brief_P-RES-002_agentic-status-research.md` | Commission baseline |
| P-RES-001 Integration Recommendations (v1.0.0) | `prompt/artifacts/tasks/P/workspace/PH000/ST004/analysis/analysis_P-PH000-ST004-AC001-TK003_integration-recommendations-P-RES-001.md` | Baseline for combined synthesis |
| Program SPS (v0.6.0) | `prompt/artifacts/tasks/P/ssot/sps_P-PROGRAM.md` | SSOT alignment target |
| AC003 Activity Plan (consumer, draft) | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/plan_P-PH000-ST001-AC003.md` | Amendment target |
| ST001 Stream Plan (v0.1.9) | `prompt/artifacts/tasks/P/workspace/PH000/ST001/plan_P-PH000-ST001.md` | AC003 parent plan |
| ST002 Stream Plan (v0.1.1) | `prompt/artifacts/tasks/P/workspace/PH000/ST002/plan_P-PH000-ST002.md` | Status system plan |
| ST004 Stream Plan (v2.0.0) | `prompt/artifacts/tasks/P/workspace/PH000/ST004/plan_P-PH000-ST004.md` | Governing plan |
| AC002 SES001 Session Notes | `prompt/artifacts/tasks/P/workspace/PH000/ST004/AC002/snotes/snotes_P-PH000-ST004-AC002-SES001.md` | Context (scope decisions) |

---

## XII. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v2.0.0 | 2026-02-26 | Structural | Major expansion: added Section VII (Combined Research Synthesis — P-RES-001 + P-RES-002 reconciliation, 12 integration points resolved), Section VIII (AC003 Task-Level Impact — dependency update + 3 task amendment proposals), Section IX (ST002 Integration Guidance — seed validation + AC002 implementation preview + dependency chain verification), Section X (Consolidated Decision Register — 13 decisions, prioritized). Updated executive summary, frontmatter, and sources. |
| v1.0.0 | 2026-02-25 | Initial | Integration recommendations package produced for TK003. SSOT alignment (10 entries, all PASS), CLAUSE domain mapping (5 domains, P-RES-002 specific), cross-topic integration, carry-forward issues/risks, and AC003 handoff guidance. |
