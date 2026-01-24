---
artifact_type: 'RESEARCH_BRIEF'
initiative_id: 'T801'
epic_id: 'T801A'
research_id: 'T801A-RES-002'
version: '1.0.0'
iteration: '2'
date: '2026-01-04'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
---

# RESEARCH BRIEF: System Architecture Research (tv_ingest Baseline, Code-As-Master)

## I. EXECUTIVE SUMMARY

This brief commissions an **internal system review** of the current Epic `T801A` implementation baseline to remove remaining uncertainty before Feature-level work and to unblock finalization of Phase 1 governance artifacts (E-RIDs + E-GDRs/E-ADRs).

**Focus split**:
*   **≈80%**: Current-state documentation (forensics: “what the system intends to be”, per code)
*   **≈20%**: Target-state feasibility + contract deltas (only where needed to bridge gaps)

**Primary blockers this research must resolve**:
*   `T801A-IF-001 (TradingView Webhook Input Contract)` — payload schema + validation behavior + governance
*   `T801A-IG-014 (Context Content)` — define “minimal market context” (relative smallest viable)
*   `T801A-IG-016 (Historical Data Input Format)` — define multi-candle structure + export constraints
*   `T801A-ADR-001 (Hybrid Integration Pattern)` — complete pipeline mapping (current-state)
*   `T801A-ADR-004 (TTI File Schema)` — confirm what “minimal market context” must include (context scope)

**Canonical master specification (non-negotiable directive)**:
*   The authoritative “Current State” is defined by the implementation under `components/tv_ingest/` **including Pine scripts**.
*   On-disk data artifacts (e.g., `components/tv_ingest/data/global_master.csv`) MUST be treated as **drift-signals** only.

**Known drift example (do not “correct” it; document it)**:
*   **Intent (master)**: `components/tv_ingest/assets/pine/nmaq_exporter.pine` and `components/tv_ingest/utils/constant.py` define an expanded schema (base + delta/VWAP fields).
*   **Reality (drift)**: existing CSV artifacts may reflect an older schema (fewer columns).

**Target deliverable**: A research report that (1) documents the intended pipeline end-to-end, (2) produces an explicit contract inventory for ingress/storage/exports, (3) proposes a **minimal market context** payload compatible with typical trading-session prompts (VPA Type 1 + Type 2), and (4) logs discovered gaps as `T801A-ISSUE-###` / `T801A-RISK-###` per `T102-ADR-007`.

---

## II. RESEARCH SCOPE & TOPICS

### Part A: Forensic Analysis (Current State)

#### Topic 1: Pipeline Map ([P1])
**Objective**: Produce a single, unambiguous pipeline map and dataflow narrative that can be cited directly by `T801A-ADR-001`.

**Specific Questions**:
*   What is the precise runtime boundary: where does TradingView data enter, and what are the persistent outputs/handoff boundaries?
*   Which modules/functions own each step (ingress, parse, validation, storage, formatting, export)?
*   What are the “human workflow handoff” points (manual review/override) and where do they occur?

**Deliverable**:
*   Pipeline diagram + step-by-step dataflow list
*   Artifact inventory table (path, purpose, producer, consumer, format)

#### Topic 2: Webhook Contract ([P2])
**Objective**: Document the intended webhook payload contract and failure behaviors as enforced by the canonical implementation.

**Specific Questions**:
*   What is the payload format and delimiter rules (e.g., semicolon rows), and what exact columns/order are expected?
*   How are `symbol` and `tf` represented on ingress, and how are they normalized?
*   What validation exists (column counts, timeframe allowlist, type casting), and what happens on failure?

**Deliverable**:
*   Webhook contract table (field list, ordering, examples)
*   Validation + error behavior summary (current behavior + documented gaps)

#### Topic 3: Storage Schema ([P3])
**Objective**: Document the intended storage schemas and explicitly characterize drift observed in on-disk artifacts.

**Specific Questions**:
*   What schemas are defined by the master spec (Pine exporter + constants), and what are the expected column counts?
*   What schemas are present on disk (e.g., `global_master.csv`, per-symbol `master.csv`) and how do they differ?
*   What is the most likely cause of drift (older artifact writer, incomplete migration, alternate path), and what is the smallest safe reconciliation path?

**Deliverable**:
*   “Intended schema” snapshot (as defined by code + Pine)
*   “Observed drift” snapshot (as seen in artifacts) with explicit “drift classification”
*   Reconciliation notes and recommended governance controls (feeds Topic 6)

### Part B: Feasibility & Gap Analysis (Target State)

#### Topic 4: Market Context Feasibility ([P4])
**Objective**: Define the **relative smallest viable** market context payload needed to support accurate LLM trading analysis, mapping VPA prompt needs to code reality.

**Research Basis**:
*   Typical prompts: `prompt/roles/VPA/example.md` (Type 1 + Type 2)
*   TTI required output shape: `prompt/roles/VPA/main_v2.1.md`

**Specific Questions**:
*   Which fields are supplied by the user in Type 1/2 prompts, and which must come from system artifacts to prevent hallucination?
*   Which quantitative fields are necessary for TTI sections (price/VWAP/RSI/MAs/volume/OBV), and which can be omitted or summarized?
*   What minimal JSON structure best balances correctness vs payload size under typical trading-session usage?

**Deliverable**:
*   Minimal market context specification: MUST vs SHOULD vs MAY field lists
*   Example “lean JSON” payload (schema sketch, not implementation)
*   Explicit “size rationale” stated as relative tradeoffs (no hard token cap required)

#### Topic 5: Historical Data Constraints ([P5])
**Objective**: Define what historical data is required by the deterministic engine and whether current export/storage patterns can realistically supply it.

**Specific Questions**:
*   What history depth is needed for PA detection, MA slope calculations, volume/OBV signals, and any RSI-dependent logic?
*   How should multi-candle data be represented (rows, grouping, timeframe separation, timestamp conventions)?
*   Based on current exporter + schema intent, what is feasible now vs what requires contract/schema expansion?

**Deliverable**:
*   Historical data requirements (depth per calculation type, minimal columns)
*   “Feasible now” vs “requires change” delta summary linked to `T801A-IG-016` and `T801A-DEP-004`

### Part C: Governance (The “Bridge”)

#### Topic 6: Schema Evolution ([P6])
**Objective**: Provide decision-ready options for evolving from Part A master spec intent + drift reality into Part B requirements while preserving MVP simplicity and backward compatibility.

**Specific Questions**:
*   Who owns the schema contract boundary: backend (`T801A1`) vs Pine exporter (`T801A2`), and what is the recommended governance model?
*   What minimal versioning strategy prevents silent breakage (schema version field, compatibility rules, validation gates)?
*   What is the smallest safe migration path from drifted CSV artifacts to the intended schema (if any migration is needed pre-feature work)?

**Deliverable**:
*   Schema evolution option matrix (MVP path + post-MVP path)
*   Recommended governance model + compatibility rules for `T801A-IF-001`

---

## III. CONSTRAINTS, ASSUMPTIONS & METHODOLOGY

### A. Constraints
*   **Boundary**: Internal repository analysis only; do not propose product redesigns unrelated to `T801A`.
*   **No Implementation Work**: No code changes, migrations, or refactors in this research.
*   **Canonical Codebase**: `components/tv_ingest/` is the only authoritative implementation for analysis.
*   **Relative Minimalism**: For market context, optimize for “relative smallest viable” payload (no hard token cap required).

### B. Assumptions
*   The researcher has read access to the repo and can inspect both Python and Pine script sources.
*   The Pine scripts under `components/tv_ingest/assets/pine/` define the intended TradingView indicator and export behavior.
*   Existing CSV artifacts are not authoritative specifications; they are historical evidence of drift.

### C. Methodology “Hierarchy of Truth” (Code-As-Master)
Resolve conflicts using this precedence order:
1.  **Code + Pine Export Scripts** (`components/tv_ingest/...`, `components/tv_ingest/assets/pine/...`) — Master Specification (intended system state)
2.  **Constants / Validators** (schema lists, expected column counts, allowlists) — Contract Intent
3.  **Data Artifacts on Disk** (`components/tv_ingest/data/...`) — Drift Signals (historical reality; use only to detect mismatch)
4.  **Documentation** (`documentation/...`) — Context Only (verify against code)

---

## IV. CROSS-TOPIC INTEGRATION

The report MUST include a synthesis section that answers:
*   **Webhook ↔ Context**: Does the intended webhook contract (Topic 2) provide enough information to construct the minimal market context (Topic 4)? If not, what are the missing fields and where should they live?
*   **Schema ↔ History**: Does the intended schema (Topic 3) support the historical depth/shape required (Topic 5)? If not, what is the smallest schema delta required?
*   **Drift ↔ Governance**: Given observed drift (Topic 3), what governance controls (Topic 6) prevent regression (versioning, validation, compatibility policy)?

---

## V. INPUT PACKET (CONTEXT MAP)

### A. Core Governance
*   SSOT: `prompt/artifacts/tasks/T801/consultant/sps/sps_T801-TRADER.md`
*   Plan: `prompt/artifacts/tasks/T801/consultant/workspace/plan/plan_T801A_phase0-1.md` (Activity 1.3.1)
*   Proposal: `prompt/artifacts/tasks/T801/consultant/workspace/proposal/T801A/proposal_T801A_phase1.md` (Open Questions + Research Register)

### B. Canonical Codebase (Authoritative)
*   `components/tv_ingest/backend/api/webhook_server.py`
*   `components/tv_ingest/backend/processors/webhook_processor.py`
*   `components/tv_ingest/backend/processors/formattings/llm_context_formatter.py`
*   `components/tv_ingest/utils/constant.py`
*   `components/tv_ingest/assets/pine/nmaq.pine`
*   `components/tv_ingest/assets/pine/nmaq_exporter.pine`

### C. Prompt Compatibility Context (Type 1 + Type 2)
*   `prompt/roles/VPA/example.md`
*   `prompt/roles/VPA/main_v2.1.md`

### D. Documentation (Context Only; Validate vs Code)
*   `documentation/tv_ingest/main.md`
*   `documentation/tv_ingest/architecture.md`
*   `documentation/tv_ingest/change_history.md`

**Usage Guidance (for Researcher)**:
*   Use these documents to quickly orient on the intended component boundaries and vocabulary, then validate claims against code/Pine.
*   If documentation conflicts with `components/tv_ingest/` implementation, treat docs as non-authoritative and record the mismatch as a `T801A-ISSUE-###` or `T801A-RISK-###` (Owner: Client + LLM_Developer).
*   Do not propose documentation rewrites as part of this research; log issues/risks only.

### E. Reference Data / Artifacts (Drift Signals Only)
*   `components/tv_ingest/data/global_master.csv`
*   `components/tv_ingest/data/*/master.csv`

### F. Anti-Patterns / Exclusions
*   **IGNORE**: `storage/tv_ingest/` (backup/legacy; not authoritative)

---

## VI. DELIVERABLE FORMAT REQUIREMENTS

The research report MUST use the standard template located at:
> `prompt\templates\researcher\template_research_report.md`

**Specific Mapping Instructions for this Brief**:
1.  **Section I (Exec Summary)**: Must include a clear verdict on whether `IF-001` (Webhook Contract) can be finalized or requires further negotiation.
2.  **Section III (Topic Findings)**:
    *   **Topic 1 (Pipeline)**: Diagrams must be ASCII or Mermaid format pasted into "Evidence".
    *   **Topic 4 (Context)**: The "Lean JSON" payload example should be in "Evidence" with token count analysis in "Analysis".
3.  **Section VI (Source Material)**: Explicitly list the `components/tv_ingest/...` files that were treated as authoritative.
4.  **Completeness**: Do NOT delete empty sections. If a topic has no implications, explicitly state "None".

---

## VII. ISSUES & RISKS REGISTER (T102-ADR-007)

The research report MUST include an “Issues & Risks” section that implements `T102-ADR-007 (Issues & Risks Index)` exactly and mints IDs scoped to this Epic (`T801A-ISSUE-###`, `T801A-RISK-###`).

**Issues**
<!-- GUIDANCE:
Status = `OPEN, IN-REVIEW, RESOLVED, BLOCKED, DEFERRED`,
priority = `Low, Medium, High`
-->
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Resolution Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

**Risks**
<!-- GUIDANCE:
Status = `OPEN, MONITORED, MITIGATED, ACCEPTED, CLOSED`,
priority = `Low, Medium, High`
-->
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Mitigation Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

---

## VIII. CRITICAL DEPENDENCIES (E-RID MAPPING)

| Topic | Primary Outputs | Informs / Unblocks |
|:---|:---|:---|
| Topic 1 | Pipeline map, artifact inventory | `T801A-ADR-001`, `T801A-GDR-001` (supporting evidence) |
| Topic 2 | Webhook input contract + validation behaviors | `T801A-IF-001`, `OQ-001` |
| Topic 3 | Intended schema + drift characterization | `T801A-IF-001`, `T801A-IG-016`, `OQ-003` |
| Topic 4 | Minimal market context spec | `T801A-IG-014`, `T801A-ADR-004`, `OQ-002` |
| Topic 5 | Historical format + feasibility delta | `T801A-IG-016`, `T801A-DEP-004`, `OQ-003` |
| Topic 6 | Schema evolution governance | `T801A-IF-001`, `T801A-CON-001` |

---

## IX. SUCCESS CRITERIA

This research is successful if:
1. `T801A-IF-001`, `T801A-IG-014`, and `T801A-IG-016` can be finalized without remaining ambiguity.
2. The pipeline mapping is complete enough to remove “partial” status from `T801A-ADR-001` (Phase 1 artifacts).
3. The minimal market context spec is VPA Type 1/2 compatible and clearly justified as “smallest viable”.
4. Drift between code intent and stored artifacts is explicitly documented and translated into actionable Issues/Risks with IDs.
