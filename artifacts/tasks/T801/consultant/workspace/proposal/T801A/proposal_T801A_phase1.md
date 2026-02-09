---
artifact_type: 'PROPOSAL'
initiative_id: 'T801'
epic_id: 'T801A'
epic_code: 'TTI'
version: '1.15.1'
date: '2026-01-10'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T801/consultant/workspace/plan/plan_T801A_phase0-1.md'
analysis_reference: 'prompt/artifacts/tasks/T801/consultant/workspace/analysis/analysis_T801A-SYSTEM_research-integration.md'
governance_rules: 'prompt/artifacts/tasks/T810/consultant/workspace/workspace_documentation_rules.md'
target_document: 'prompt/artifacts/tasks/T801/consultant/sps/sps_T801-TRADER.md'
target_section: 'III.C.1 (Epic: T801A)'
---

# PHASE 1 PROPOSAL: `T801A / TTI` — Epic Requirements & Governance

## I. EXECUTIVE SUMMARY

This proposal presents the Phase 1 consultancy outcomes for Epic `T801A (TTI — Timeframe Trend Identification)` and is ready for Client approval and SSOT implementation (Subphase 1.4).

**Phase Scope**: Epic Requirements & Governance Development per `plan_T801A_phase0-1.md` Section IV (Phase 1).

**Key Objectives**:
1. Develop all Epic Requirements (E-RIDs) across 6 categories: Dependencies (DEP), Constraints (CON), Assumptions (ASSUM), Quality Goals (QG), Interfaces (IF), Implementation Guidance (IG)
2. Develop Epic Governance Decision Records (E-GDRs) with paired Architectural Decision Record (E-ADR) references
3. Ensure research integration from T801-RES-001 and T801A-RES-001
4. Obtain Client approval before SSOT implementation (SPS + Concept)

**Final Phase 1 Approval Scope (Ready-to-Sign)**:
- **41 E-RIDs** (ASSUM 6, CON 4, DEP 4, IF 3, IG 16, QG 8)
- **6 E-GDRs** (index + full bodies)
- **6 E-ADRs** (index + full bodies; implemented into Concept SSOT)
- **17 Epic Issues/Risks** (8 Issues + 9 Risks; Epic-level only — exclude promoted Feature items for SPS)

**Phase 2 Implication (Preview)**: With SSOT updated, Phase 2 proceeds to Feature Request authoring for `T801A1–T801A3` with link-only wiring from SPS (no promoted Feature Issues/Risks backfilled into Epic SSOT during Subphase 1.4).

**Phase 1 Dependencies Satisfied**:
- ✅ Activity 1.0.1 (Research Integration) completed with deliverable: `analysis_T801A-SYSTEM_research-integration.md`
- ✅ Activity 1.0.2 (Proposal Initialization) completed with this proposal skeleton

**Consultation Approach**: This proposal serves as a dynamic workspace for collaborative E-RID specification development through Socratic dialogue. Content will be developed incrementally through Subphases 1.1-1.3, with full normative bodies populated before Client approval gate (Subphase 1.4).

---

## II. CANDIDATE INVENTORY (WORKING INDEX; NOT FULL BODIES)
<!-- PURPOSE: Single index of IDs we will validate; keep summaries to 1 line each. -->

### A. Assumptions (T801A-ASSUM-###)
| ID | Title | 1-line Summary | Source | Status | Spec Reference |
|:---|:------|:---------------|:-------|:-------|:---------------|
| `T801A-ASSUM-001` | Numeric Scoring Feasibility | A deterministic -2..+2 scoring system can replace qualitative TTI output while achieving acceptable accuracy | Analysis + Dialogue | Confirmed | Section III.A |
| `T801A-ASSUM-002` | PA Detection Feasibility | Algorithmic PA detection (swing-point or equivalent) can reliably identify HH/HL vs LH/LL patterns | Analysis + Dialogue | Confirmed | Section III.A |
| `T801A-ASSUM-003` | Volume Integration Value | Integrating OBV-based volume confirmation will improve TTI accuracy without unacceptable complexity | Analysis + Dialogue | Confirmed | Section III.A |
| `T801A-ASSUM-004` | External Platform Sufficiency | TradingView platform and webhook infrastructure provide sufficient reliability, rate limits, and payload capacity | Plan + Dialogue | Confirmed | Section III.A |
| `T801A-ASSUM-005` | Workflow Acceptance | Trader will functionally and experientially accept manual artifact handoff workflow per T801A-CON-003 | Plan + Dialogue | Confirmed | Section III.A |
| `T801A-ASSUM-006` | LLM Performance Stability | Adding TTI JSON artifacts to trading context will not significantly degrade LLM response quality or latency | Dialogue | Confirmed | Section III.A |

### B. Constraints (T801A-CON-###)
| ID | Title | 1-line Summary | Source | Status | Spec Reference |
|:---|:------|:---------------|:-------|:-------|:---------------|
| `T801A-CON-001` | Backward Compatibility | Development SHALL occur in isolated sandbox; production cutover requires explicit Client approval | Analysis + Dialogue | Confirmed | Section III.B |
| `T801A-CON-002` | Operational Continuity | Trading operations (entire ecosystem) MUST NOT be disrupted by development activities | Plan + Dialogue | Confirmed | Section III.B |
| `T801A-CON-003` | Manual Workflow Acceptance | MVP permits manual artifact handoff; automated delivery is explicitly deferred | Plan + Dialogue | Confirmed | Section III.B |
| `T801A-CON-004` | Complexity Management | MVP excludes automated divergence detection; RSI/MACD divergence deferred to post-MVP | Analysis + Dialogue | Confirmed | Section III.B |

### C. Quality Goals (T801A-QG-###)
| ID | Title | 1-line Summary | Source | Status | Spec Reference |
|:---|:------|:---------------|:-------|:-------|:---------------|
| `T801A-QG-001` | Deterministic Consistency & Interpretability | Same input → identical output; scoring follows transparent, documented calculation framework; results reproducible | Analysis + Dialogue | Confirmed | Section III.C |
| `T801A-QG-002` | Signal Reliability | ≥70% overall accuracy, ≥80% extreme-score precision, ≤20% false positive rate (per T801A-RES-001 §II); subject to optimization | Analysis + Dialogue | Confirmed | Section III.C |
| `T801A-QG-003` | Manual Override (Simplified) | TTI output format SHALL support human-readable manual editing for post-output override via manual workflow | Analysis + Dialogue | Confirmed | Section III.C |
| `T801A-QG-004` | Rule Maintainability | Rules/weights are configuration-driven; minimize hardcoded logic | Analysis | Confirmed | Section III.C |
| `T801A-QG-005` | Timeframe Correctness | Output only includes timeframe-appropriate indicators per the initiative matrix | Analysis | Confirmed | Section III.C |
| `T801A-QG-006` | Latency & Resource Efficiency | Target <1 min (ideal), ≤3 min (max), normal load; resource ceilings TBD at Feature level | Dialogue | Confirmed | Section III.C |
| `T801A-QG-007` | Context Sufficiency | TTI output SHALL provide sufficient market context to replace inline TTI protocol + master.csv for LLM_Trader | Dialogue | Confirmed | Section III.C |
| `T801A-QG-008` | MVP Simplicity | Feature solutions SHALL prioritize simplicity, low complexity, and speed of implementation for baseline MVP | Dialogue | Confirmed | Section III.C |

### D. Dependencies (T801A-DEP-###)
| ID | Title | 1-line Summary | Source | Status | Spec Reference |
|:---|:------|:---------------|:-------|:-------|:---------------|
| `T801A-DEP-001` | Timeframe-Correct Input | Backend TTI engine requires timeframe-correct indicator dataset; enforcement mechanism is implementation choice | Analysis + Dialogue | Confirmed | Section III.D |
| `T801A-DEP-002` | tv_ingest Backend | Deterministic engine integrates into existing tv_ingest behavioral contract; internal refactors permitted if external behavior stable | Analysis + Dialogue | Confirmed | Section III.D |
| `T801A-DEP-003` | LLM_Trader Consumption | LLM_Trader prompt consumes TTI JSON artifact instead of executing inline TTI | Analysis + Dialogue | Confirmed | Section III.D |
| `T801A-DEP-004` | Expanded Data Structure | Epic requires expanded master.csv structure supporting multi-candle historical data for PA, MA, and volume calculations | ASSUM Dialogue | Confirmed | Section III.D |

### E. Interfaces (T801A-IF-###)
| ID | Title | 1-line Summary | Source | Status | Spec Reference |
|:---|:------|:---------------|:-------|:-------|:---------------|
| `T801A-IF-001` | Webhook Input Contract | Webhook payload includes timeframe-appropriate indicators + schema version; backend validates before scoring | Analysis + Dialogue + T801A-RES-002 | Confirmed | Section III.E |
| `T801A-IF-002` | Backend Output Contract | Versioned JSON with TTI scoring + minimal market context; required fields include PA, VWAP, RSI, MA, Volume/OBV, Overall; human-readable | Analysis + Dialogue | Confirmed | Section III.E |
| `T801A-IF-003` | LLM_Trader Consumption Interface | JSON artifact is sole input per QG-007; silent override handling; replaces inline TTI protocol + master.csv | Analysis + Dialogue | Confirmed | Section III.E |

### F. Implementation Guidance (T801A-IG-###)
| ID | Title | 1-line Summary | Source | Status | Spec Reference |
|:---|:------|:---------------|:-------|:-------|:---------------|
| `T801A-IG-001` | Configuration-Driven Rules | Use config files for thresholds/weights/classification rules (avoid deep hardcoding) | Analysis + Dialogue | Confirmed | Section III.F |
| `T801A-IG-002` | Timeframe Filtering | Validate/ignore irrelevant indicators per timeframe matrix (backend enforcement) | Analysis + Dialogue | Confirmed | Section III.F |
| `T801A-IG-003` | Volume Confirmation | OBV as research baseline for trend confirmation; divergence flags optional | Analysis + Dialogue (generalized) | Confirmed | Section III.F |
| `T801A-IG-004` | Scoring Mechanism Guidance | Unified scoring: individual contributions, weights, aggregation, calibration; weighted voting as baseline | Analysis + Dialogue (expanded) | Confirmed | Section III.F |
| `T801A-IG-005` | PA Detection Approach | Deterministic HH/HL vs LH/LL recognition; swing-point as T801A-RES-001 baseline, alternatives per QG-008 | Analysis + Dialogue (generalized) | Confirmed | Section III.F |
| `T801A-IG-006` | MA Crossover Configuration | Configurable crossover pairs per IG-001; distance/slope/velocity at Feature level; T801A-RES-001 recommends 50/200 | Analysis + Dialogue (generalized) | Confirmed | Section III.F |
| `T801A-IG-007` | Initiative Matrix Reference | Backend filtering SHALL reference T801-RES-001 timeframe applicability matrix | DEP Dialogue | Confirmed | Section III.F |
| `T801A-IG-008` | Research Alignment | Implementation SHOULD align with research; deviations require documented rationale | CON Dialogue (reclassified) | Confirmed | Section III.F |
| `T801A-IG-009` | Integration Scope | Epic SHALL integrate as extension; fundamental refactors escalate to Initiative | CON Dialogue (reclassified) | Confirmed | Section III.F |
| `T801A-IG-010` | Artifact Size Guidance | JSON artifact SHOULD be optimized for LLM context budget | CON Dialogue (gap) | Confirmed | Section III.F |
| `T801A-IG-011` | Validation Guidance | Scoring SHOULD demonstrate acceptable accuracy via playground validation | CON Dialogue (gap) | Confirmed | Section III.F |
| `T801A-IG-012` | Dependency Minimization | MVP SHOULD avoid new external dependencies beyond TradingView | CON Dialogue (gap) | Confirmed | Section III.F |
| `T801A-IG-013` | Override Workflow | Manual file editing workflow for post-output override per CON-003/ASSUM-005 | QG Dialogue | Confirmed | Section III.F |
| `T801A-IG-014` | Context Content | Baseline scope (price, VWAP, indicators); full scope defined by T801A-RES-002 | QG + IF Dialogue + T801A-RES-002 | Confirmed | Section III.F |
| `T801A-IG-015` | Data Validation | Input + output validation with best-effort + error flags; covers IF-002 schema validation | QG Dialogue (expanded) | Confirmed | Section III.F |
| `T801A-IG-016` | Historical Input Format | Guidance on expanded master.csv structure for multi-candle historical data; supports DEP-004 | IF Dialogue (GAP-IF-C) | Confirmed | Section III.F |

---

## III. E-RID BODIES (NORMATIVE; POPULATED IN SUBPHASE 1.3)
<!-- PURPOSE: This section becomes the canonical spec during the phase. -->

### A. Assumptions (T801A-ASSUM-###)

**ASSUM Validation Lifecycle Summary**

| ID | Title | Status | Validation Method | Timing | Owner | If Invalidated | CON Cross-Ref |
|:---|:------|:-------|:------------------|:-------|:------|:--------------|:--------------|
| `T801A-ASSUM-001` | Scoring Feasibility | `Pending` | Playground validation | Feature T801A1 | Client | Escalate: revise scoring approach | — |
| `T801A-ASSUM-002` | PA Detection Feasibility | `Pending` | Manual trader review | Feature T801A1 | Client | Fallback: simplify/remove PA scoring | — |
| `T801A-ASSUM-003` | Volume Integration Value | `Pending` | Comparative analysis | Feature T801A1 | Client | Fallback: omit OBV signal | — |
| `T801A-ASSUM-004` | External Platform Sufficiency | `Pending` | Operational monitoring | Feature T801A2 | Client | Mitigate: reduce scope; escalate platform limits | — |
| `T801A-ASSUM-005` | Operational Acceptance | `Pending` | Client evaluation | Feature T801A3 | Client | Escalate: revisit workflow/integration approach | `T801A-CON-003` |
| `T801A-ASSUM-006` | LLM Performance Stability | `Pending` | Performance testing | Feature T801A3 | Client | Mitigate: reduce artifact size/prompt load | — |

* **T801A-ASSUM-001 (Numeric Scoring Feasibility)** — We assume a deterministic -2..+2 numeric scoring system can replace the current qualitative TTI output (BULLISH/NEUTRAL/BEARISH variations) while achieving acceptable accuracy for trading decisions. Validation: Playground validation with historical data demonstrating scoring system produces consistent, interpretable trend classifications. Validation timing: Feature `T801A1` development.

* **T801A-ASSUM-002 (PA Detection Feasibility)** — We assume algorithmic price action detection (swing-point algorithm or equivalent simpler approach) can reliably identify HH/HL vs LH/LL patterns for MVP trend classification. Qualitative language intentional at Epic level; quantitative thresholds defined at Feature level. Note: Feature-level research may evaluate simpler alternatives if swing-point proves overly complex. Validation: Manual trader review of sample classifications during playground testing. Validation timing: Feature `T801A1` development.

* **T801A-ASSUM-003 (Volume Integration Value)** — We assume integrating OBV-based volume confirmation into TTI scoring will improve trend identification accuracy without introducing unacceptable complexity. OBV is a new addition to TTI protocol with significant uncertainty and can introduce risk. Fallback: If validation shows negative or neutral value-add, OBV integration is deferred or removed entirely from MVP. Validation: Comparative analysis of scoring accuracy with/without OBV during `T801A1` playground testing; clear fallback to proceed without volume signal. Validation timing: Feature `T801A1` implementation.

* **T801A-ASSUM-004 (External Platform Sufficiency)** — We assume the TradingView platform and its webhook infrastructure provide sufficient reliability, rate limits, and payload capacity for consistent TTI artifact generation. Operational constraints detailed in `T801A-RES-002`. TradingView is currently the sole external data dependency per `T801A-IG-012`. Validation: Operational monitoring during sandbox development. Validation timing: Continuous during Feature `T801A2` development.

* **T801A-ASSUM-005 (Workflow Acceptance)** — We assume the trader (Client) will functionally and experientially accept the manual artifact handoff workflow permitted by `T801A-CON-003`. This includes: 
  (1) functional acceptance — trader can technically perform the workflow; 
  (2) experiential acceptance — workflow does not significantly increase cognitive load or introduce unacceptable delays. Extends `T801A-CON-003` by including override acceptance (manual file editing before LLM_Trader handoff) as part of workflow acceptance validation per `T801A-QG-003` scope simplification. Validation: Client evaluation during playground testing. Validation timing: Feature `T801A3` integration testing.

* **T801A-ASSUM-006 (LLM Performance Stability)** — We assume adding TTI JSON artifacts to trading session context (within 100k token target budget) will not significantly degrade LLM (GEMINI-PRO-3) response quality or latency. The LLM has 1M+ token context capacity, so fit is not a concern; performance impact is the key assumption. Validation: Performance testing with TTI artifacts added to representative trading prompts. Validation timing: Feature `T801A3` integration testing.

### B. Constraints (T801A-CON-###)

* **T801A-CON-001 (Backward Compatibility)** — All Epic `T801A` development SHALL occur in an isolated sandbox environment separate from production systems. Existing tv_ingest backend and LLM_Trader prompt SHALL remain fully operational and unmodified during development. Production cutover (integration of sandbox work into main system) requires explicit Client approval as a hard gate. No partial integration is permitted; changes deploy as a complete unit after extensive testing and approval.

* **T801A-CON-002 (Operational Continuity)** — Day-to-day trading operations MUST NOT be disrupted by Epic `T801A` development activities. Scope of "trading operations" includes the entire trading analysis ecosystem: LLM_Trader prompt execution, tv_ingest webhook processing, analytics dashboards, and position management workflows. Any development-related outage or degradation to these components is a constraint violation requiring immediate remediation.

* **T801A-CON-003 (Manual Workflow Acceptance)** — MVP explicitly permits manual artifact handoff between the backend TTI output and LLM_Trader consumption. Automated delivery mechanisms (file watching, triggers, API integration) are explicitly deferred to post-MVP. Per `T801A-QG-003`, the manual workflow is explicitly leveraged — override is achieved through file editing during manual handoff, not backend configuration.

* **T801A-CON-004 (Complexity Management)** — MVP explicitly excludes automated divergence detection. RSI divergence (regular and hidden) and MACD divergence are deferred to post-MVP development. Rationale per research (`T801A-RES-001` §V): 
  (1) medium-low feasibility — divergence detection requires swing point detection on both price and indicator values simultaneously; 
  (2) tuning burden — divergence thresholds require extensive calibration to avoid false positives; 
  (3) complexity management — scoring system validation must be stable before adding divergence signals. 
  MA crossovers (50/200, optionally 20/50) remain in scope as an explicit exception.

### C. Quality Goals (T801A-QG-###)

* **T801A-QG-001 (Deterministic Consistency & Interpretability)** — Backend TTI generation SHALL produce identical output for identical input data across multiple runs. Scoring algorithms SHALL be deterministic (no randomness, no LLM variance). **Additionally**, scoring calculations SHALL follow a transparent, documented calculation framework that produces interpretable (not black-box) results — the trader MUST be able to understand why a score was assigned. Results SHALL be reproducible across system updates given the same input data and configuration version. Supports `T801A-ASSUM-001` validation; calculation framework developed in Feature T801A1.

* **T801A-QG-002 (Signal Reliability)** — Extreme trend scores (+2/-2) SHALL achieve ≥80% precision in backtesting. Overall classification accuracy SHALL exceed 70% threshold. False positive rate SHALL be ≤20% for extreme scores. Reference: `T801A-RES-001` §II (Validation Methodology). **Note**: These quantitative thresholds are research-derived starting points and are subject to calibration/optimization during Feature-level validation. Threshold modifications require documented rationale and Client approval. Validates `T801A-ASSUM-001`; supported by `T801A-IG-003`, `T801A-IG-004`, `T801A-IG-011`.

* **T801A-QG-003 (Manual Override)** — TTI output format SHALL support human-readable manual editing for post-output override via manual workflow per `T801A-CON-003`. **Scope Simplification**: Backend does NOT implement override logic or validation — override is achieved through manual file editing by trader AFTER TTI output is produced, BEFORE handoff to LLM_Trader. Extends `T801A-CON-003`; supported by `T801A-ASSUM-005`; requires `T801A-IF-002` human-editable format; workflow guidance in `T801A-IG-013`.

* **T801A-QG-004 (Rule Maintainability)** — Backend rule engine SHOULD use configuration-driven rules (JSON/YAML) for indicator thresholds, scoring weights, and classification logic. Hardcoded rules SHALL be minimized. Configuration changes SHALL NOT require code deployment; parameter adjustments achievable via config file modification. Supported by `T801A-IG-001`.

* **T801A-QG-005 (Timeframe Correctness)** — TTI output SHALL only include indicators applicable to the analyzed timeframe per Initiative T801 timeframe applicability matrix (`T801-RES-001` §II). Irrelevant indicators (e.g., S_VWAP on 1D) SHALL NOT appear in output or contribute to scoring. Depends on `T801A-DEP-001`; supported by `T801A-IG-002`, `T801A-IG-007`.
  Reference: `T801-RES-001 (Indicator Design Standards)`

* **T801A-QG-006 (Latency & Resource Efficiency)** — TTI artifact generation SHOULD complete within **<1 minute (ideal), ≤3 minutes (maximum)** from webhook receipt under normal load conditions. Resource consumption (memory, CPU) SHALL remain within acceptable ceilings to be determined at Feature level via benchmarking. **Load Profile**: Normal load defined as single trading pair webhook with data for multiple timeframes; extended load scenarios (multiple pairs, high-frequency webhooks) deferred to post-MVP. **Note**: Latency targets are guidance subject to Feature-level refinement based on deployed system characteristics. Supported by `T801A-IG-010` for context budget optimization.

* **T801A-QG-007 (Context Sufficiency)** — TTI output artifact SHALL provide sufficient market context to **replace both** the inline TTI protocol execution AND the raw master.csv data currently consumed by LLM_Trader. The goal is a single JSON artifact that enables LLM_Trader to perform trading analysis without requiring additional data files or inline calculations. Impacts `T801A-IF-002` (required fields); impacts `T801A-IF-003` (sole input artifact); impacts `T801A-DEP-004` (TTI output replaces master.csv for LLM_Trader); supported by `T801A-IG-014`; pending `T801A-RES-002`.

* **T801A-QG-008 (MVP Simplicity)** — Feature-level solutions for Epic T801A SHALL prioritize simplicity, low complexity, and speed of implementation to achieve baseline MVP functionality. Assessment criteria for Feature development SHOULD weight these factors highly against alternative complex approaches. Complex solutions requiring extensive calibration, tuning, or infrastructure changes SHOULD be deferred to post-MVP unless essential for core TTI functionality. Supported by `T801A-IG-012`; informs all Feature-level development prioritization.

### D. Dependencies (T801A-DEP-###)

* **T801A-DEP-001 (Timeframe-Correct Input)** — Backend TTI scoring engine MUST receive timeframe-correct indicator dataset where only timeframe-appropriate indicators are included per the Initiative `T801` timeframe applicability matrix. The enforcement mechanism (PineScript filtering OR backend filtering) is an implementation choice to be determined during Feature-level design; the dependency is on the correctness of the final dataset, not the specific enforcement location. Development occurs within sandbox per `T801A-CON-001`; platform reliability per `T801A-ASSUM-004`.

* **T801A-DEP-002 (tv_ingest Backend)** — Epic `T801A` requires the existing `tv_ingest` backend component's behavioral contract (webhook ingestion → data processing → CSV storage). Backend integration MUST maintain this behavioral contract stability; internal refactors are acceptable as long as external behavior (webhook acceptance, data storage outputs) remains stable. Development MUST occur in isolated sandbox environment per operational continuity constraint.

* **T801A-DEP-003 (LLM_Trader Consumption)** — Epic T801A requires modification of the LLM_Trader system prompt (`prompt/roles/VPA/main_v2.1.md`) to consume the generated TTI JSON artifact as authoritative input instead of executing the TTI protocol inline. The prompt modification includes:
  (1) removing inline TTI execution logic,
  (2) adding JSON artifact parsing and interpretation,
  (3) surfacing manual override flags for trader visibility.
Fallback to inline TTI format is acceptable during transition if artifact is missing or stale. Manual workflow per `T801A-CON-003`; workflow acceptance per `T801A-ASSUM-005`.

* **T801A-DEP-004 (Expanded Data Structure)** — Epic `T801A` requires an expanded `master.csv` data structure supporting multi-candle historical data for accurate price action, volume calculations and indicator values such as moving averages as input for TTI calculation. Current structure limitations and historical depth specifications detailed in `T801A-RES-002`. Per `T801A-QG-007`, the TTI output artifact replaces the need to deliver raw master.csv to LLM_Trader — the JSON artifact provides sufficient market context. No file consolidation required; TTI JSON is the sole LLM_Trader input artifact. `T801A-IG-016`, `T801A-RES-002` Topic 5

### E. Interfaces (T801A-IF-###)

* **T801A-IF-001 (Webhook Input Contract)** — Webhook payload interface from TradingView PineScript exporter (`nmaq_exporter.pine`) to tv_ingest backend.

  **Contract Type**: Base (20-column) — canonical per `T801A-RES-002`.

  **Delimiter Rules**:
  - Rows separated by newline `\n`
  - Columns separated by semicolon `;`
  - No header row; no explicit quoting/escaping

  **Field Schema (20 columns)**:
  | # | Field | Type | Example |
  |---:|:------|:-----|:--------|
  | 1 | `symbol` | string | `BINANCE:BTCUSDT` |
  | 2 | `time` | datetime string | `2025-12-23 22:00:00` |
  | 3-6 | `open,high,low,close` | float | `88620.79` |
  | 7 | `volume` | float | `12804.02886` |
  | 8-9 | `vol_ma20,vol_ma30` | float | `15679.57` |
  | 10-13 | `ema9,ema21,ema50,ema200` | float | `88184.41` |
  | 14 | `sma200` | float | `107773.37` |
  | 15-16 | `rsi,rsi_ma14` | float | `43.3861` |
  | 17-19 | `vwap_session,vwap_week,vwap_month` | float | `87753.21` |
  | 20 | `tf` | string code | `60`, `D`, `W` |

  **Multi-Timeframe Semantics**:
  - Chart timeframe: up to 5 rows per alert (configurable via `exportRows`)
  - Additional timeframes: 1 row each (latest only)

  **TradingView Platform Constraints (Environmental)**:
  - Port restrictions: Only 80/443 accepted
  - Processing timeout: ~3 seconds before TradingView cancels
  - Resend on 5xx: Up to 3 retries (max 4 deliveries per trigger)
  - Message body cap: 40,960 characters
  - Timestamp timezone: `str.format()` always UTC+0

  **Schema Versioning**: Deferred to Feature T801A1/T801A2 coordination. Current contract unversioned.

  Supports `T801A-DEP-001`, `T801A-IG-007`, `T801A-IG-015`, `T801A-RES-002`.

* **T801A-IF-002 (Backend Output Contract)** — TTI output artifact interface from backend TTI engine to downstream consumers (manual handoff, LLM_Trader). Artifact SHALL be JSON with versioned, human-readable schema per `T801A-QG-003` and `T801A-QG-007`.

  **REQUIRED Fields (MVP)** — derived from current TTI protocol + research findings:
  - `schema_version` — artifact schema version (semver format)
  - `generator_version` — TTI engine version
  - `asset` — trading pair identifier
  - `timeframe` — analyzed timeframe
  - `trend_score` — numeric -2 to +2 per `T801A-GDR-002`
  - `trend_label` — text label (Strong Uptrend/Uptrend/Neutral/Downtrend/Strong Downtrend)
  - `signals` object containing:
    - `htf_reference` — higher timeframe assessment reference (e.g., "4H: BEARISH")
    - `price_action` — PA assessment (HH/HL, LH/LL patterns, breakout signals, caution flags)
    - `vwap` — VWAP position assessments (S_VWAP, D_VWAP, W_VWAP, M_VWAP values + position relative to price)
    - `rsi` — RSI + RSI_MA values and assessment
    - `moving_averages` — MA values (EMA_9, EMA_21, EMA_50, EMA_200, SMA_200) and position assessment
    - `volume` — OBV trend direction and confirmation assessment per `T801A-IG-003`
  - `overall_assessment` — final trend assessment with caution indicators (e.g., "BULLISH*")

  **Feature-Level Expansion (Deferred)**: Each major signal field MAY include additional indicator calculations (e.g., MA crossover signals, slope calculations, distance from price) as explored in Feature T801A1. These additional fields contribute to both market context and final TTI output assessment.
  - `manual_override` — boolean flag (sufficient for MVP per dialogue)
  - `as_of` — generation timestamp

  **Context Scope (Option B)**: TTI scoring fields + minimal market context. "Minimal market context" definition to be determined by `T801A-RES-002` research per `T801A-IG-014`. Initial scope includes current price, VWAP levels, and key indicator values as reference points.

  **OPTIONAL Fields (Future Extension)**:
  - `override_note`, `override_by`, `override_timestamp` — full audit trail
  - Extended market context fields per `T801A-QG-007` Option C exploration

  Supports `T801A-QG-003`, `T801A-QG-007`, `T801A-IG-013`, `T801A-IG-014`, `T801A-IG-015`, `T801A-RES-002`.

* **T801A-IF-003 (LLM_Trader Consumption Interface)** — Interface contract for LLM_Trader prompt consumption of TTI JSON artifact. LLM_Trader prompt (`prompt/roles/VPA/main_v2.1.md`) SHALL consume `T801A-IF-002` JSON artifact as **sole authoritative input** per `T801A-QG-007`.

  **Consumption Contract**:
  - Artifact **replaces both**: (1) inline TTI protocol execution; (2) raw master.csv data delivery
  - LLM_Trader SHALL parse JSON artifact and interpret trend signals for trading analysis
  - **Override Handling**: Silent (Option A per dialogue) — process TTI as-is; trader responsible for noting override context if relevant
  - **Fallback**: Per `T801A-DEP-003`, fallback to inline TTI format acceptable during transition if artifact missing/stale

  **Prompt Modification Requirements**:
  - Remove inline TTI execution logic
  - Add JSON artifact parsing and interpretation
  - Reference `T801A-IF-002` schema for field consumption

  Supports `T801A-DEP-003`, `T801A-QG-007`; workflow guidance in `T801A-IG-013`, `T801A-IG-014`.

### F. Implementation Guidance (T801A-IG-###)

* **T801A-IG-001 (Configuration-Driven Rules)** — Backend rule engine SHOULD use configuration files (JSON/YAML) to define indicator thresholds, timeframe-specific weights, scoring parameters, and classification logic. Hardcoded rules SHALL be minimized. Configuration changes SHALL NOT require code deployment; parameter adjustments achievable via config file modification. Supports `T801A-QG-004`.

* **T801A-IG-002 (Timeframe Filtering)** — Backend SHALL validate incoming indicator set against timeframe applicability matrix. Irrelevant indicators (e.g., S_VWAP on 1D timeframe) SHALL be ignored in scoring calculation. Validation occurs after webhook ingestion, before scoring engine execution. Supports `T801A-QG-005`; references `T801A-RES-001` §II.

* **T801A-IG-003 (Volume Confirmation)** — Backend SHOULD include volume confirmation methodology in trend scoring. Research baseline: OBV (On-Balance Volume) trend direction as confirmation signal — rising OBV + uptrend = confidence boost; falling OBV + uptrend = divergence flag. Divergence flags are optional for MVP. Alternative volume methodologies MAY be explored at Feature level. Supports `T801A-QG-002`; references `T801A-RES-001` §III (OBV recommendation).

* **T801A-IG-004 (Scoring Mechanism Guidance)** — Backend SHOULD implement transparent scoring calculation where: (1) individual indicators contribute weighted scores per documented methodology; (2) composite score aggregation follows documented formula; (3) weights are configuration-driven per `T801A-IG-001`; (4) calibration methodology documented for ongoing optimization per `T801A-IG-011`. Research baseline: Weighted voting ensemble approach per `T801A-RES-001` §II. Alternative scoring methodologies MAY be explored at Feature level per `T801A-QG-008`. Supports `T801A-QG-001`, `T801A-QG-002`.

* **T801A-IG-005 (PA Detection Approach)** — Backend SHOULD implement deterministic price action pattern recognition for HH/HL (Higher High/Higher Low) vs LH/LL (Lower High/Lower Low) classification. Research baseline: Swing-point algorithm with configurable confirmation bars per `T801A-RES-001` §IV. Alternative approaches (simpler or more robust) MAY be explored at Feature level per `T801A-QG-008`. Complex patterns (head-and-shoulders, triangles, wedges) are explicitly deferred to post-MVP. Supports `T801A-ASSUM-002`.

* **T801A-IG-006 (MA Crossover Configuration)** — MA crossover detection SHOULD be configurable per `T801A-IG-001`. Research baseline: 50/200 crossover (Golden Cross/Death Cross) for longer-term trend confirmation per `T801A-RES-001` §V. Additional configurations (20/50 crossover, distance-to-price, slope, velocity calculations) MAY be explored at Feature level. Crossover events SHALL include event date in artifact per `T801A-IF-002`. References `T801A-RES-001` §V.

* **T801A-IG-007 (Initiative Matrix Reference)** — Backend filtering logic SHALL reference `T801A-RES-001` timeframe applicability matrix as authoritative source for indicator inclusion/exclusion rules. Matrix defines relevance (High/Medium/Low) per indicator × timeframe combination. "Low" relevance indicators SHOULD be excluded from scoring; "High" relevance indicators SHOULD have primary weight. Supports `T801A-DEP-001`, `T801A-IG-002`.

* **T801A-IG-008 (Research Alignment)** — Implementation SHOULD align with research outcomes from `T801-RES-001` and `T801A-RES-001`. Deviations from research recommendations require: (1) documented rationale explaining why deviation is necessary; (2) explicit Client approval before implementation. Research recommendations serve as design choice baselines, not absolute prescriptions.
  Reference: `T801-RES-001 (Indicator Design Standards)`

* **T801A-IG-009 (Integration Scope)** — Epic T801A SHALL integrate as extension to existing `tv_ingest` backend component per `T801A-DEP-002`. Fundamental architecture changes (new service patterns, database additions, external API integrations) SHOULD be escalated as separate Initiative work requiring Client decision. Internal refactors are acceptable if external behavioral contract remains stable. CON dialogue reclassification; supports `T801A-CON-001`.

* **T801A-IG-010 (Artifact Size Guidance)** — JSON artifact SHOULD be optimized for LLM context budget. Exact size thresholds to be determined via Feature-level research based on: (1) typical artifact field count and nesting depth; (2) LLM token consumption analysis; (3) context window utilization patterns. Initial guidance: prefer lean schema with essential fields; defer extended context to post-MVP. Supports `T801A-ASSUM-006`.

* **T801A-IG-011 (Validation Guidance)** — Scoring system SHOULD demonstrate acceptable accuracy via playground validation before production deployment. Quantitative thresholds (≥70% accuracy, ≥80% extreme-score precision) defined at Feature level per `T801A-QG-002`. Validation methodology: historical data simulation with stratified regime sampling per `T801A-RES-001` §II. Supports `T801A-ASSUM-001`, `T801A-CON-001`.

* **T801A-IG-012 (Dependency Minimization)** — MVP SHOULD avoid introducing new external service dependencies beyond established TradingView integration. New dependencies (cloud services, databases, external APIs) require: (1) documented necessity rationale; (2) Client approval; (3) operational continuity assessment per `T801A-CON-002`. TradingView webhook remains sole external data dependency. Supports `T801A-QG-008`.

* **T801A-IG-013 (Override Workflow)** — Manual file editing workflow for post-output override per `T801A-CON-003` and `T801A-ASSUM-005`. Backend does NOT implement override logic or validation — override is achieved through manual JSON file editing by trader AFTER TTI output is produced, BEFORE handoff to LLM_Trader. Workflow: (1) backend produces TTI JSON; (2) trader edits JSON if override needed (sets `manual_override: true`); (3) trader provides edited JSON to LLM_Trader. Supports `T801A-QG-003`.

* **T801A-IG-014 (Context Content)** — Guidance on "minimal market context" content for TTI JSON artifact per `T801A-QG-007` Option B selection.

  **Minimal Market Context Specification** (per T801A-RES-002):

  **Required Structure**:
  - `schema_version`: Context schema version (e.g., `tv_ingest_context/0.1.0`)
  - `symbol`: Trading pair identifier (e.g., `BINANCE:BTCUSDT`)
  - `as_of`: Generation timestamp (datetime string)
  - `time_source`: Timezone/format metadata for timestamp interpretation
  - `timeframes`: Object containing per-timeframe context data

  **Per-Timeframe Context Fields**:
  - `tf_code`: Raw timeframe code (e.g., `60`, `D`, `W`)
  - `close`: Current close price
  - `ema`: Object with EMA values (9, 21, 50, 200)
  - `sma200`: SMA 200 value (where applicable per timeframe matrix)
  - `rsi`: RSI value
  - `rsi_ma14`: RSI MA14 value
  - `vwap`: Object with applicable VWAP values (session, week, month per timeframe matrix)

  **Optional Chart Timeframe History**:
  - `chart_tf_bars`: Array of recent bars (up to 5) for chart timeframe only
  - Each bar: `time`, `open`, `high`, `low`, `close`, `volume`

  **Size Guidance**:
  - Target: ~1500-2000 characters (~375-500 tokens)
  - Satisfies `T801A-QG-007` without exceeding `T801A-IG-010` context budget

  **Exclusions from Minimal Context**:
  - Delta columns (not emitted by current Pine)
  - VWAP values masked by backend filtering (include only applicable per matrix)
  - Historical bars for non-chart timeframes

* **T801A-IG-015 (Data Validation)** — Backend SHALL implement validation at two stages:

  **Input Validation**: Validate webhook payload against `T801A-IF-001`. Handle malformed/missing data per Option D (best-effort processing + error flags): (1) attempt calculation with available data; (2) flag missing/invalid fields in output; (3) continue processing rather than rejecting entirely.

  **HTTP Response Code Guidance** (per T801A-RES-002): Return HTTP 4xx for client validation errors (column count mismatch, malformed data) to prevent TradingView resend loop. Avoid HTTP 5xx for validation failures — TradingView retries 5xx up to 3 times, creating duplicates.

  **Output Validation**: Validate TTI artifact against `T801A-IF-002` schema before delivery. Reject/flag artifacts that fail schema validation per `T801A-IF-002` "machine-validated" clause.

  Backend SHALL NOT crash on validation failures but produce error artifact or fallback output per `T801A-QG-008`. Supports `T801A-IF-001`, `T801A-IF-002`

  **Input Validation Behavior** (per `T801A-IF-001`):
  - Column count mismatch → validation error (return 4xx not 5xx)
  - Malformed/missing data → best-effort processing + error flags
  - Backend validates before scoring; does not validate row count

* **T801A-IG-016 (Historical Input Format)** — Guidance on multi-candle historical data format for backend TTI engine per `T801A-DEP-004`.

  **Current-State Format** (per T801A-RES-002):
  - **Record shape**: Each row = one candle snapshot for one timeframe
  - **Grouping**: Group by `(symbol, tf)`; `time` is candle timestamp
  - **History depth**:
    - Chart timeframe: up to **5 bars** per alert (configurable via `exportRows`)
    - Other timeframes: **1 bar** per alert (latest only)
  - **Constraint**: No schema version tag or "snapshot id" for dedup

  **Calculation Feasibility**:
  | Calculation | Feasible? | Notes |
  |:------------|:----------|:------|
  | Trend scores | ✅ Yes | Pine provides current indicator values |
  | MA crossovers | ✅ Yes | Pine has long history |
  | Short momentum | ✅ Yes | 5 bars sufficient |
  | Complex PA (HH/HL series) | ⚠️ Limited | May require append mode |
  | RSI divergences | ⚠️ Limited | Deferred per `T801A-CON-004` |

  **Recommendation**:
  - For MVP: Accept 5-bar chart TF + 1-bar other TFs as sufficient for trend scoring
  - For enhanced PA detection: Enable append mode with `MAX_ROWS_PER_SYMBOL` limit
  - Feature T801A2 determines Pine export capabilities; Feature T801A1 consumes

  **Timestamp Caveat**: Timestamps may be formatted incorrectly or use chart TF time for all rows. Document as known limitation.

### G. Research & Notes

**Research**
| Research ID | Title | Summary | Linked To | Brief | Report |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `T801A-RES-001` | **Backend TTI Architecture** | Numeric scoring system (-2 to +2), JSON file format with lean schema, swing-point PA detection, MA crossover inclusion (divergence deferred), validation methodology | `T801A` | [brief](../../research/brief/brief_T801A-RES-001_backend-tti-architecture.md) | [report](../../research/report/report_T801A-RES-001_backend-tti-architecture.md) |
| `T801A-RES-002` | **System Architecture Research** | ⏳ **PENDING COMMISSION** — Map current tv_ingest → LLM_Trader pipeline; document I/O contracts; propose schema governance model; define "minimal market context" for `T801A-IF-002` Option B | `T801A`, `T801A-IF-001`, `T801A-IF-002`, `T801A-IG-014`, `T801A-IG-016` | TBD | TBD |

**Notes**
- `T801A-RES-002` blocks finalization of `T801A-IF-001` (schema governance) and informs `T801A-IG-014` (context content), `T801A-IG-016` (historical data format)
- Commission planned for Activity 1.3.1 (Research Commission Gate)


---

## IV. EPIC GOVERNANCE DECISIONS (E-GDR) + ARCHITECTURAL REFERENCES (E-ADR)

### A. E-GDR Index
| GDR ID | Title | Status | Owner | Effective | Supersedes | Anchor |
|:-------|:------|:-------|:------|:----------|:-----------|:-------|
| `T801A-GDR-001` | Hybrid TTI Architecture | Proposed | Client | 2026-01-03 | — | #t801a-gdr-001-hybrid-tti-architecture |
| `T801A-GDR-002` | Numeric Scoring Foundation | Proposed | Client | 2026-01-03 | — | #t801a-gdr-002-numeric-scoring-foundation |
| `T801A-GDR-003` | Playground-First Mandate | Proposed | Client | 2026-01-03 | — | #t801a-gdr-003-playground-first-mandate |
| `T801A-GDR-004` | Backend File Format Standard | Proposed | Client | 2026-01-03 | — | #t801a-gdr-004-backend-file-format-standard |
| `T801A-GDR-005` | Initiative Standard Compliance | Proposed | Client | 2026-01-03 | — | #t801a-gdr-005-initiative-standard-compliance |
| `T801A-GDR-006` | Research Baseline Adoption | Proposed | Client | 2026-01-03 | — | #t801a-gdr-006-research-baseline-adoption |

### B. E-GDR Bodies (NORMATIVE)

* **T801A-GDR-001 (Hybrid TTI Architecture) {#t801a-gdr-001-hybrid-tti-architecture}**

  **Context.** Current LLM-based TTI protocol (inline execution within LLM_Trader prompt) produces unreliable, inconsistent trend classifications. Timeframe-specific indicator rules are not consistently applied; qualitative outputs (BEARISH/NEUTRAL/BULLISH variations) lack determinism for algorithmic processing. Per `T801-RES-001` and `T801A-RES-001`, a hybrid architecture separating deterministic calculation from interpretive analysis addresses reliability concerns while preserving LLM contextual insight.

  **Decision.** Adopt `T801A-ADR-001 (Hybrid Integration Pattern)`, establishing hybrid TTI architecture where: (1) backend deterministic engine produces numeric trend classification per timeframe; (2) LLM_Trader consumes structured TTI output for interpretive analysis and trading decisions. Backend calculations replace inline TTI protocol execution. Integration follows file-based handoff with manual workflow per `T801A-CON-003`. Client owns governance authority for Epic T801A.

  **Consequences.**
  (+) Eliminates LLM variance and timeframe rule inconsistency via deterministic backend
  (+) Preserves LLM interpretive strengths for contextual analysis and trading judgment
  (+) Enables independent backend validation and testing per `T801A-CON-001`/`T801A-CON-003`
  (±) Requires coordinated development across T801A1 (Backend), T801A2 (PineScript), T801A3 (Integration)
  (-) Introduces integration complexity; manual handoff workflow per `T801A-CON-003`

  **References.** `T801A-DEP-002 (tv_ingest Backend)`, `T801A-DEP-003 (LLM_Trader Consumption)`, `T801A-CON-001 (Backward Compatibility)`, `T801A-CON-003 (Manual Workflow Acceptance)`, `T801A-IG-009 (Integration Scope)`, `T801-RES-001 (Indicator Design Standards)`, `T801A-RES-001 (Backend TTI Architecture)`

---

* **T801A-GDR-002 (Numeric Scoring Foundation) {#t801a-gdr-002-numeric-scoring-foundation}**

  **Context.** Existing TTI protocol outputs subjective text classifications (BEARISH, NEUTRAL, BULLISH with variations like "SLIGHTLY BEARISH"). These qualitative outputs are inconsistent across sessions and difficult to track quantitatively for validation. Per `T801A-RES-001 §II`, numeric scoring provides deterministic, comparable, and validatable trend strength classification.

  **Decision.** Adopt `T801A-ADR-002 (Scoring Algorithm Specification)`, establishing -2 to +2 symmetric 5-point scale as the foundation for Epic T801A trend classification. Scale: +2 (Strong Uptrend), +1 (Uptrend), 0 (Neutral), -1 (Downtrend), -2 (Strong Downtrend). Scoring formula follows documented deterministic calculation per `T801A-ASSUM-001` validation methodology. Client owns governance authority for Epic T801A.

  **Consequences.**
  (+) Deterministic, reproducible trend classifications enable validation and optimization
  (+) Numeric scale supports quantitative backtesting per `T801A-QG-002` (≥70% accuracy, ≥80% extreme-score precision)
  (+) Text labels preserved for human readability alongside numeric scores
  (±) Requires threshold calibration via playground validation per `T801A-IG-011`
  (-) Binary text classifications (BULLISH/BEARISH) converted to 5-point scale; may require trader adjustment period per `T801A-ASSUM-005`

  **References.** `T801A-ASSUM-001 (Numeric Scoring Feasibility)`, `T801A-QG-001 (Deterministic Consistency & Interpretability)`, `T801A-QG-002 (Signal Reliability)`, `T801A-IG-004 (Scoring Mechanism Guidance)`, `T801A-IG-011 (Validation Guidance)`, `T801A-RES-001 §II (Numeric Scoring System Design)`

---

* **T801A-GDR-003 (Playground-First Mandate) {#t801a-gdr-003-playground-first-mandate}**

  **Context.** Daily trading operations depend on current system reliability (tv_ingest webhook processing, LLM_Trader prompt execution, position management). Per `T801A-CON-001`/`T801A-CON-002`, development activities MUST NOT disrupt operational continuity. Isolated playground environment enables parallel development, comprehensive validation, and controlled production cutover.

  **Decision.** Adopt `T801A-ADR-003 (Playground Deployment Architecture)`, mandating isolated playground for all Epic T801A development. Playground operates on dedicated feature branch (`feature/t801a-tti`) separate from `main`. Production cutover requires explicit Client approval per `T801A-CON-001` as hard gate. Playground validation demonstrates acceptable accuracy per `T801A-QG-002`/`T801A-IG-011` before production deployment. Client owns governance authority for Epic T801A.

  **Consequences.**
  (+) Protects operational trading systems from development disruption per `T801A-CON-002`
  (+) Enables comprehensive validation with historical data before production deployment
  (+) Supports iterative calibration and testing without client approval for each change
  (±) Requires parallel maintenance of playground and production environments during development
  (-) Manual merge and cutover process; rollback more complex than feature flags

  **References.** `T801A-CON-001 (Backward Compatibility)`, `T801A-CON-002 (Operational Continuity)`, `T801A-QG-002 (Signal Reliability)`, `T801A-IG-011 (Validation Guidance)`, Plan §II.B (Working Assumptions)

---

* **T801A-GDR-004 (Backend File Format Standard) {#t801a-gdr-004-backend-file-format-standard}**

  **Context.** TTI output artifact file format impacts LLM consumption reliability, manual override workflow usability, and long-term maintainability. Per `T801A-RES-001 §III`, JSON provides optimal balance of schema rigidity, LLM ingestion reliability, and traceability compared to YAML or Markdown alternatives. Human-readable format required for manual override per `T801A-QG-003`.

  **Decision.** Adopt `T801A-ADR-004 (TTI File Schema)`, establishing JSON with lean, versioned schema as the Epic T801A file format standard. Schema includes: `schema_version`, `trend_score`, `trend_label`, `signals` object (PA, VWAP, RSI, MA, Volume/OBV, Overall Assessment), manual override fields, and timestamp. Format supports both machine validation (`T801A-IF-002`) and human editing (`T801A-QG-003`). Client owns governance authority for Epic T801A.

  **Consequences.**
  (+) Reliable LLM ingestion with explicit structure and schema validation per `T801A-IF-002`
  (+) Human-readable format supports manual override workflow per `T801A-QG-003`/`T801A-IG-013`
  (+) Versioning strategy enables backward compatibility and schema evolution
  (±) JSON more verbose than YAML; context budget optimization required per `T801A-IG-010`
  (-) Manual editing requires JSON syntax knowledge; validation catches errors per `T801A-IG-015`

  **References.** `T801A-IF-002 (Backend Output Contract)`, `T801A-QG-003 (Manual Override)`, `T801A-IG-010 (Artifact Size Guidance)`, `T801A-IG-013 (Override Workflow)`, `T801A-IG-015 (Data Validation)`, `T801A-RES-001 §III (Backend TTI File Format)`

---

* **T801A-GDR-005 (Initiative Standard Compliance) {#t801a-gdr-005-initiative-standard-compliance}**

  **Context.** Epic T801A operates within Initiative T801 governance framework. Per `T801-RES-001 §V`, Initiative Standards 1-6 ensure cross-epic consistency for timeframe filtering, volume indicators, confidence systems, indicator roles, performance evaluation, and integration prioritization. Epic implementations SHALL comply with Initiative standards unless variance explicitly approved per `T801A-IG-007`.

  **Decision.** Adopt `T801A-ADR-005 (Timeframe Applicability Enforcement)`, mandating Epic T801A SHALL comply with T801-RES-001 Initiative Standards 1-6. Backend filtering logic SHALL reference T801-RES-001 timeframe applicability matrix as authoritative source per `T801A-IG-007`. Deviations from Initiative standards require documented rationale and Client approval per `T801A-IG-008`. Client owns governance authority for Epic T801A.

  **Consequences.**
  (+) Ensures cross-epic consistency for future Initiative T801 work (multi-pair support, enhanced indicators)
  (+) Leverages Initiative-level research investment for Epic implementations
  (+) Prevents technical debt from Epic-specific deviations
  (±) Initiative standards may constrain Epic-level optimization; variance workflow required for exceptions
  (-) Epic T801A blocked if Initiative standards change without Epic alignment assessment

  **References.** `T801A-DEP-001 (Timeframe-Correct Input)`, `T801A-QG-005 (Timeframe Correctness)`, `T801A-IG-007 (Initiative Matrix Reference)`, `T801A-IG-008 (Research Alignment)`, `T801-RES-001 §V (Initiative Standards 1-6)`

---

* **T801A-GDR-006 (Research Baseline Adoption) {#t801a-gdr-006-research-baseline-adoption}**

  **Context.** Research recommendations from `T801-RES-001` and `T801A-RES-001` vary in prescription level. Some are mandatory baselines requiring Epic-wide compliance (e.g., -2 to +2 scale, JSON format), while others are flexible patterns permitting Feature-level alternatives (e.g., swing-point PA detection). Without explicit classification per `T801A-QG-008`, Feature development may inconsistently apply research guidance.

  **Decision.** Adopt `T801A-ADR-006 (Research Baseline Specification)`, establishing explicit baseline/flexible classification for all research recommendations. Mandatory baselines (SHALL) define non-negotiable Epic architecture; flexible guidances (SHOULD/MAY) provide research-recommended starting points permitting Feature-level alternatives per `T801A-QG-008` (MVP Simplicity). Deviations from mandatory baselines require explicit Client approval; deviations from flexible guidances require documented rationale per `T801A-IG-008`. Client owns governance authority for Epic T801A.

  **Consequences.**
  (+) Clear baseline vs flexible classification guides Feature-level development decisions
  (+) Preserves research value while permitting MVP simplicity per `T801A-QG-008`
  (+) Explicit approval workflow for baseline deviations prevents technical debt
  (±) Feature developers must consult ADR-006 specification before selecting alternatives
  (-) Baseline classifications may over-constrain if research assumptions prove incorrect

  **References.** `T801A-QG-008 (MVP Simplicity)`, `T801A-IG-008 (Research Alignment)`, `T801-RES-001 (Indicator Design Standards)`, `T801A-RES-001 (Backend TTI Architecture)`

### C. E-ADR Index (Reference Links)
| ADR ID | Title | Paired GDR | Status | Owner | Effective | Supersedes | Anchor |
|:-------|:------|:-----------|:-------|:------|:----------|:-----------|:-------|
| `T801A-ADR-001` | Hybrid Integration Pattern | `T801A-GDR-001` | Proposed | Client | 2026-01-03 | — | #t801a-adr-001-hybrid-integration-pattern |
| `T801A-ADR-002` | Scoring Algorithm Specification | `T801A-GDR-002` | Proposed | Client | 2026-01-03 | — | #t801a-adr-002-scoring-algorithm-specification |
| `T801A-ADR-003` | Playground Deployment Architecture | `T801A-GDR-003` | Proposed | Client | 2026-01-03 | — | #t801a-adr-003-playground-deployment-architecture |
| `T801A-ADR-004` | TTI File Schema | `T801A-GDR-004` | Proposed | Client | 2026-01-03 | — | #t801a-adr-004-tti-file-schema |
| `T801A-ADR-005` | Timeframe Applicability Enforcement | `T801A-GDR-005` | Proposed | Client | 2026-01-03 | — | #t801a-adr-005-timeframe-applicability-enforcement |
| `T801A-ADR-006` | Research Baseline Specification | `T801A-GDR-006` | Proposed | Client | 2026-01-03 | — | #t801a-adr-006-research-baseline-specification |

### D. E-ADR Bodies (NORMATIVE)

* **T801A-ADR-001 (Hybrid Integration Pattern) {#t801a-adr-001-hybrid-integration-pattern}**

  **Context.** Per `T801A-GDR-001`, Epic `T801A` adopts hybrid architecture separating backend deterministic calculation from LLM interpretive analysis. Integration pattern must balance reliability requirements (`T801A-QG-001`), operational continuity (`T801A-CON-002`), and MVP simplicity (`T801A-QG-008`) while enabling Feature-level development across `T801A1 (Backend)`, `T801A2 (PineScript)`, `T801A3 (Integration)`.

  **Decision.** Adopt file-based handoff integration pattern with the following workflow: 
  (1) TradingView webhook → tv_ingest processes payload per `T801A-DEP-002`; 
  (2) Backend TTI engine consumes filtered indicator data, produces JSON artifact per `T801A-ADR-004`; 
  (3) Manual handoff: trader reviews TTI artifact, applies manual override if needed per `T801A-QG-003`/`T801A-IG-013`; 
  (4) LLM_Trader prompt modified per `T801A-DEP-003` to consume TTI JSON file as authoritative input (not recompute inline). Webhook trigger initiates backend calculation; file system acts as integration boundary. 
  Complete pipeline mapping provided in `T801A-ADR-001-FR-006` per `T801A-RES-002`.

  **Specification.**
    1) **T801A-ADR-001-FR-001 (Webhook Handoff):** tv_ingest webhook processing SHALL persist filtered indicator payload to intermediate file (CSV or JSON) accessible by backend TTI engine. Payload SHALL include timeframe identifier and timestamp per `T801A-IF-001`.
    2) **T801A-ADR-001-FR-002 (Backend Trigger):** Backend TTI engine MAY be triggered manually (CLI invocation) or via file watcher monitoring webhook payload directory. Automated triggering is post-MVP scope per `T801A-QG-008`.
    3) **T801A-ADR-001-FR-003 (File-Based Output):** Backend SHALL write TTI artifact to designated output directory with naming convention `tti_{asset}_{timeframe}_{timestamp}.json` per `T801A-ADR-004` schema.
    4) **T801A-ADR-001-FR-004 (Manual Handoff Gate):** Trader SHALL review TTI artifact before LLM_Trader invocation per `T801A-CON-003`. Manual override workflow per `T801A-IG-013` preserves audit trail.
    5) **T801A-ADR-001-FR-005 (LLM Consumption):** LLM_Trader prompt SHALL reference TTI file path and ingest JSON content verbatim. Prompt SHALL NOT recompute TTI logic inline.
    6) **T801A-ADR-001-FR-006 (Pipeline Mapping):** The hybrid integration pattern follows this pipeline architecture per T801A-RES-002:
       ```mermaid
       flowchart TD
         TV[TradingView Alert<br/>Pine: NMAQ_Exporter] -->|HTTP POST<br/>body=text (rows)| NG[ngrok HTTPS public URL]
         NG --> API[FastAPI WebhookServer<br/>POST /]
         API --> PARSE[pandas.read_csv(sep=';')<br/>header=None]
         PARSE --> COLS[Column-count gate:<br/>20=BASE_COLUMNS]
         COLS --> PROC[WebhookProcessor.process_webhook_data]
         PROC --> VALIDATE[Datetime + numeric coercion]
         VALIDATE --> STORE[CSV storage:<br/>symbol_dir/tf.csv<br/>symbol_dir/master.csv<br/>global_master.csv]
         STORE --> TTI[TTI Engine<br/>(Feature T801A1)]
         TTI --> JSON[TTI JSON Artifact<br/>per `T801A-IF-002`]
         JSON --> HUMAN[Manual handoff<br/>per `T801A-CON-003`]
         HUMAN --> LLM[LLM_Trader<br/>per `T801A-IF-003`]
       ```
       **Artifact Inventory:**
       | Stage | Artifact | Format | Owner |
       |:------|:---------|:-------|:------|
       | Ingress | Webhook payload | text/plain (semicolon-separated) | T801A2 (PineScript) |
       | Storage | CSV files | CSV | tv_ingest backend |
       | Output | TTI JSON | JSON per `T801A-IF-002` | T801A1 (Backend) |
       | Handoff | Manual copy | JSON artifact | Human (`T801A-CON-003`) |

  **Consequences.**
  (+) File-based boundary enables independent development, testing, and deployment of backend vs LLM components
  (+) Manual review gate satisfies `T801A-CON-003` and `T801A-QG-003` (override-ability) per Client requirement
  (+) Clear integration contract via file schema (`T801A-ADR-004`) reduces coupling
  (±) Manual handoff introduces latency; automated triggering deferred to post-MVP
  (-) File system management required (directory structure, naming conventions, cleanup)

  **Alternatives Considered.** None

  **References.** `T801A-GDR-001 (Hybrid TTI Architecture)`, `T801A-DEP-002 (tv_ingest Backend)`, `T801A-DEP-003 (LLM_Trader Consumption)`, `T801A-CON-001 (Backward Compatibility)`, `T801A-CON-002 (Operational Continuity)`, `T801A-CON-003 (Manual Workflow Acceptance)`, `T801A-QG-001 (Deterministic Consistency)`, `T801A-QG-003 (Manual Override)`, `T801A-QG-008 (MVP Simplicity)`, `T801A-IF-001 (Webhook Input)`, `T801A-IF-002 (Backend Output)`, `T801A-IG-009 (Integration Scope)`, `T801A-IG-013 (Override Workflow)`, `T801A-RES-002 (System Architecture Research)`, `T801A-RES-001 (Backend TTI Architecture)`

  **Provenance.** 
  - `analysis_T801A-SYSTEM_research-integration.md`
  - `analysis_T801A-RES-002_system-architecture-research.md`

---

* **T801A-ADR-002 (Scoring Algorithm Specification) {#t801a-adr-002-scoring-algorithm-specification}**

  **Context.** Per `T801A-GDR-002`, Epic T801A adopts -2 to +2 symmetric 5-point scale for trend classification. Scoring algorithm specification defines how individual indicator signals combine into composite trend score, threshold calibration methodology, and validation acceptance criteria per `T801A-QG-002`.

  **Decision.** Adopt weighted voting ensemble scoring algorithm with the following components: (1) Individual Indicator Contributions: each indicator (PA, VWAP, RSI, MA crossover, Volume/OBV) votes +1 (bullish), 0 (neutral), -1 (bearish) based on deterministic rules; 
  (2) Composite Score Aggregation: weighted sum of individual contributions normalized to -2 to +2 scale; 
  (3) Threshold Calibration: weights and score-to-label thresholds calibrated via playground validation per `T801A-IG-011` to meet `T801A-QG-002` acceptance criteria (≥70% overall accuracy, ≥80% extreme-score precision); 
  (4) Contradiction Detection: opposing signals (e.g., uptrend PA with bearish RSI) reduce confidence score magnitude.

  **Specification.**
    1) **T801A-ADR-002-FR-001 (Indicator Voting Rules):** Each indicator SHALL vote per documented rule set:
       - **PA Structure:** +1 if HH/HL pattern, -1 if LH/LL pattern, 0 if neutral/range-bound per `T801A-IG-005`
       - **VWAP Position:** +1 if price > applicable VWAP, -1 if price < VWAP, 0 if within threshold per `T801A-IG-002`
       - **RSI:** +1 if RSI > 60 (overbought recovery), -1 if RSI < 40 (oversold breakdown), 0 if 40-60 range
       - **MA Crossover:** +1 if bullish crossover (golden cross), -1 if bearish crossover (death cross), 0 if no recent crossover per `T801A-IG-006`
       - **Volume Confirmation (OBV):** +1 if OBV trend aligns with PA trend (confirmation), -1 if OBV diverges (warning), 0 if neutral per `T801A-IG-003`

    2) **T801A-ADR-002-FR-002 (Weighted Aggregation):** Composite score formula: `composite_score = (w_PA × PA_vote) + (w_VWAP × VWAP_vote) + (w_RSI × RSI_vote) + (w_MA × MA_vote) + (w_OBV × OBV_vote)`. Initial weights (research baseline from T801A-RES-001): w_PA = 0.35, w_VWAP = 0.25, w_RSI = 0.15, w_MA = 0.15, w_OBV = 0.10. Weights SHALL be configuration-driven per `T801A-IG-001`.

    3) **T801A-ADR-002-FR-003 (Score Normalization):** Composite score SHALL be normalized to -2 to +2 range. Score-to-label thresholds (initial baseline): composite ≥ +1.5 → +2 (Strong Uptrend), +0.5 to +1.49 → +1 (Uptrend), -0.49 to +0.49 → 0 (Neutral), -0.5 to -1.49 → -1 (Downtrend), composite ≤ -1.5 → -2 (Strong Downtrend). Thresholds SHALL be configuration-driven per `T801A-IG-001`.

    4) **T801A-ADR-002-FR-004 (Contradiction Handling):** If opposing signals detected (e.g., PA +1 and RSI -1), composite score magnitude SHALL be reduced by contradiction penalty (initial: 0.5 reduction). Contradiction logic documented in `T801A-IG-004`.

    5) **T801A-ADR-002-FR-005 (Validation Methodology):** Scoring algorithm SHALL be validated per `T801A-ASSUM-001` acceptance criteria before production deployment: (a) Backtest with N ≥ 100 historical days stratified across market regimes; (b) Overall accuracy ≥ 70%; (c) Extreme-score precision (+2/-2) ≥ 80%; (d) False positive rate ≤ 20%; (e) Client sample approval of 20+ classifications per `T801A-IG-011`.

  **Consequences.**
  (+) Transparent, auditable scoring calculation per `T801A-QG-001` (Deterministic Consistency)
  (+) Configuration-driven weights and thresholds enable calibration without code changes per `T801A-IG-001`
  (+) Weighted voting baseline from research per T801A-RES-001; validated methodology per `T801A-QG-002`
  (±) Weight calibration required via playground validation; iterative tuning expected per `T801A-IG-011`
  (-) Simplified voting model may miss nuanced patterns; complexity deferral per `T801A-CON-002`

  **Alternatives Considered.** None

  **References.** `T801A-GDR-002 (Numeric Scoring Foundation)`, `T801A-ASSUM-001 (Numeric Scoring Viability)`, `T801A-QG-001 (Deterministic Consistency)`, `T801A-QG-002 (Signal Reliability)`, `T801A-IG-001 (Configuration-Driven Rules)`, `T801A-IG-003 (Volume Confirmation)`, `T801A-IG-004 (Scoring Mechanism Guidance)`, `T801A-IG-005 (PA Detection Approach)`, `T801A-IG-006 (MA Crossover Configuration)`, `T801A-IG-011 (Validation Guidance)`, `T801A-RES-001 §II (Numeric Scoring System Design)`, `T801A-RES-001 (Backend TTI Architecture)`

  **Provenance.** 
  - `analysis_T801A-SYSTEM_research-integration.md §III.B (Finding 4)`

---

* **T801A-ADR-003 (Playground Deployment Architecture) {#t801a-adr-003-playground-deployment-architecture}**

  **Context.** Per `T801A-GDR-003`, all Epic T801A development SHALL occur in isolated playground environment. Deployment architecture must protect operational systems (`T801A-CON-002`), enable parallel development (`T801A-CON-001`), and support comprehensive validation (`T801A-QG-002`/`T801A-IG-011`) without introducing unnecessary complexity per `T801A-QG-008`.

  **Decision.** Adopt minimal playground deployment using dedicated feature branch (`feature/t801a-tti`) with the following architecture: 
  (1) Branch Strategy: All T801A development commits to `feature/t801a-tti` branch; `main` branch remains stable and operational; 
  (2) Environment Isolation: Playground uses isolated directory structure (`/playground/t801a/`) for backend code, configuration, and output artifacts; (3) Data Isolation: Playground validation uses historical data exports; production data not modified during development; 
  (4) Validation Gates: Playground validation per `T801A-IG-011` (≥70% accuracy, ≥80% extreme-score precision) required before Client approval gate; 
  (5) Production Cutover: Manual merge to `main` after Client approval per `T801A-CON-001`; rollback via branch revert if issues detected.

  **Specification.**
    1) **T801A-ADR-003-FR-001 (Branch Strategy):** Epic T801A development SHALL use `feature/t801a-tti` branch. All Feature-level development branches (T801A1, T801A2, T801A3) SHALL branch from and merge to `feature/t801a-tti`. `main` branch SHALL NOT be modified until Client approval gate passed.

    2) **T801A-ADR-003-FR-002 (Directory Isolation):** Playground SHALL use `/playground/t801a/` directory structure: `/playground/t801a/backend/` (TTI engine code), `/playground/t801a/config/` (weights, thresholds), `/playground/t801a/data/` (test data), `/playground/t801a/output/` (TTI artifacts). Production directories SHALL NOT be modified during playground development.

    3) **T801A-ADR-003-FR-003 (Validation Data):** Playground validation SHALL use historical data exports (master.csv snapshots) spanning N ≥ 100 trading days. Data stratification SHALL include uptrend, downtrend, and neutral regimes per `T801A-ASSUM-001` validation methodology.

    4) **T801A-ADR-003-FR-004 (Client Approval Gate):** Production cutover SHALL require: (a) Playground validation metrics meet `T801A-QG-002` acceptance criteria; (b) Client sample review of 20+ classifications per `T801A-IG-011`; (c) Explicit Client approval documented in plan file or proposal file.

    5) **T801A-ADR-003-FR-005 (Rollback Procedure):** If production issues detected post-cutover, rollback SHALL revert `main` branch to pre-merge commit and reactivate prior TTI protocol until issues resolved.

  **Consequences.**
  (+) Minimal complexity per `T801A-QG-008`; branch strategy sufficient for MVP scope
  (+) Clear separation protects operational systems per `T801A-CON-002`
  (+) Independent validation before production deployment per `T801A-QG-002`/`T801A-IG-011`
  (±) Manual merge and cutover process; no automated CI/CD pipelines for MVP
  (-) Parallel environment maintenance required during development; directory structure management

  **Alternatives Considered.** None

  **References.** `T801A-GDR-003 (Playground-First Mandate)`, `T801A-ASSUM-001 (Numeric Scoring Viability)`, `T801A-CON-001 (Backward Compatibility)`, `T801A-CON-002 (Operational Continuity)`, `T801A-QG-002 (Signal Reliability)`, `T801A-QG-008 (MVP Simplicity)`, `T801A-IG-011 (Validation Guidance)`

  **Provenance.** None

---

* **T801A-ADR-004 (TTI File Schema) {#t801a-adr-004-tti-file-schema}**

  **Context.** Per `T801A-GDR-004`, Epic T801A adopts JSON format for TTI output artifacts. File schema specification defines required fields, data types, versioning strategy, and manual override fields to support machine validation (`T801A-IF-002`), LLM consumption (`T801A-DEP-003`), and manual override workflow (`T801A-QG-003`/`T801A-IG-013`). Minimal market context scope defined by T801A-RES-002 per `T801A-IG-014`.

  **Decision.** Adopt the following JSON schema for TTI output artifacts with versioned structure supporting evolution and backward compatibility. Schema includes: 
  (1) Metadata: schema_version, generator_version, asset, timeframe, analysis_timestamp; 
  (2) Trend Classification: trend_score (-2 to +2), trend_label (text); 
  (3) Signals Object: PA structure, VWAP position, RSI value, MA crossover events, Volume/OBV trend, Overall Assessment; 
  (4) Manual Override Fields: manual_override (boolean), override_note (text), override_by (trader ID), override_timestamp; 
  (5) Context Fields: current price, VWAP levels, key indicator values (baseline scope; full scope per `T801A-RES-002`).

  **Specification.**
    1) **T801A-ADR-004-FR-001 (Schema Version):** JSON artifact SHALL include `schema_version` field using semver format (e.g., "1.0.0"). Major version increments for breaking changes, minor for additive fields, patch for documentation updates.

    2) **T801A-ADR-004-FR-002 (Required Metadata):** JSON artifact SHALL include:
       ```json
       {
         "schema_version": "1.0.0",
         "generator_version": "tti-engine/0.1.0",
         "asset": "BTC-USD",
         "timeframe": "1D",
         "analysis_timestamp": "2026-01-03T12:00:00Z"
       }
       ```

    3) **T801A-ADR-004-FR-003 (Trend Classification):** JSON artifact SHALL include:
       ```json
       {
         "trend_score": 2,
         "trend_label": "Strong Uptrend"
       }
       ```
       `trend_score` SHALL be integer in range [-2, +2]. `trend_label` SHALL map to score per `T801A-ADR-002` thresholds.

    4) **T801A-ADR-004-FR-004 (Signals Object):** JSON artifact SHALL include nested `signals` object per `T801A-ADR-002` indicator voting:
       ```json
       {
         "signals": {
           "price_action": {
             "pattern": "HH/HL",
             "description": "Higher highs and higher lows confirmed"
           },
           "vwap": {
             "daily_vwap": 95000,
             "position": "above",
             "description": "Price above D_VWAP"
           },
           "rsi": {
             "value": 65,
             "interpretation": "Overbought recovery zone"
           },
           "moving_average": {
             "ma50_cross_ma200": "bullish",
             "cross_date": "2026-01-01"
           },
           "volume": {
             "obv_trend": "rising",
             "confirmation": "aligned with PA trend"
           },
           "overall_assessment": "Strong bullish alignment across indicators"
         }
       }
       ```

    5) **T801A-ADR-004-FR-005 (Manual Override Fields):** JSON artifact SHALL support manual override workflow per `T801A-IG-013`:
       ```json
       {
         "manual_override": false,
         "override_note": null,
         "override_by": null,
         "override_timestamp": null
       }
       ```
       If trader modifies TTI output, `manual_override` SHALL be set to `true` with audit trail fields populated.

    6) **T801A-ADR-004-FR-006 (Minimal Market Context Scope):** Per T801A-RES-002 Topic 4, JSON artifact SHALL include minimal market context satisfying `T801A-QG-007`. The context structure SHALL include:
       - `schema_version`: Context schema version (e.g., `tv_ingest_context/0.1.0`)
       - `symbol`: Trading pair identifier
       - `as_of`: Generation timestamp
       - `time_source`: Timezone/format metadata for timestamp interpretation
       - `timeframes`: Object containing per-timeframe context data
       **Per-Timeframe Context Fields:**
       - `tf_code`: Raw timeframe code (e.g., `60`, `D`, `W`)
       - `close`: Current close price
       - `ema`: Object with EMA values (9, 21, 50, 200)
       - `sma200`: SMA 200 value (where applicable per timeframe matrix)
       - `rsi`, `rsi_ma14`: RSI values
       - `vwap`: Object with applicable VWAP values (session, week, month per timeframe matrix)
       **Optional Chart Timeframe History:**
       - `chart_tf_bars`: Array of up to 5 recent bars for chart timeframe only
       **Size Target:** ~1500-2000 characters (~375-500 tokens) per artifact satisfying `T801A-QG-007` without exceeding `T801A-IG-010` context budget.

    7) **T801A-ADR-004-FR-007 (Validation):** Backend SHALL validate TTI artifact against schema before output per `T801A-IG-015`. LLM_Trader SHALL validate schema_version compatibility before consumption per `T801A-IF-002` "machine-validated" clause.

  **Consequences.**
  (+) Explicit schema enables machine validation and reliable LLM consumption per `T801A-IF-002`
  (+) Nested signals object supports individual indicator transparency per `T801A-QG-001`
  (+) Manual override workflow preserves audit trail per `T801A-QG-003`
  (±) Schema versioning strategy enables evolution; backward compatibility management required
  (-) JSON verbosity; context budget optimization per `T801A-IG-010` required to avoid token bloat

  **Alternatives Considered.** None

  **References.** `T801A-GDR-004 (Backend File Format Standard)`, `T801A-IF-002 (Backend Output Contract)`, `T801A-QG-001 (Deterministic Consistency)`, `T801A-QG-003 (Manual Override)`, `T801A-IG-010 (Artifact Size Guidance)`, `T801A-IG-013 (Override Workflow)`, `T801A-IG-014 (Context Content)`, `T801A-IG-015 (Data Validation)`, `T801A-RES-001 §III (Backend TTI File Format)`, `T801A-RES-002 (System Architecture Research)`

  **Provenance.** 
  - `analysis_T801A-SYSTEM_research-integration.md §III.B (Finding 5)`

---

* **T801A-ADR-005 (Timeframe Applicability Enforcement) {#t801a-adr-005-timeframe-applicability-enforcement}**

  **Context.** Per `T801A-GDR-005`, Epic T801A SHALL comply with `T801-RES-001 Initiative Standards 1-6`. Initiative Standard 1 defines timeframe applicability matrix governing which indicators are relevant per timeframe (15m, 1H, 4H, 1D). Enforcement mechanism ensures backend filtering logic references authoritative matrix and prevents irrelevant indicators from contributing to trend score per `T801A-QG-005`.

  **Decision.** Adopt backend validation enforcement pattern where: 
  (1) Timeframe Applicability Matrix: Backend references `T801-RES-001` §II matrix as authoritative source (loaded from configuration file per `T801A-IG-001`); 
  (2) Indicator Filtering: Backend validates incoming indicator set against matrix; indicators marked "Low" relevance or "Exclude" are ignored in scoring calculation; 
  (3) Matrix Compliance: PineScript enhancement (`T801A-DEP-001`) SHALL filter payload per matrix before backend consumption; backend re-validates as defense-in-depth; 
  (4) Documentation Reference: Backend configuration SHALL document Initiative Standard citation per `T801A-IG-007`.

  **Specification.**
    1) **T801A-ADR-005-FR-001 (Matrix Configuration):** Backend SHALL load timeframe applicability matrix from configuration file (JSON or YAML). Configuration SHALL reference `T801-RES-001 §II (Timeframe × Indicator Applicability Matrix)` as source of truth per `T801A-IG-007`.

    2) **T801A-ADR-005-FR-002 (Indicator Filtering Logic):** Backend SHALL implement filtering per matrix:
       ```python
       # Pseudocode
       for indicator in incoming_payload:
           relevance = matrix[timeframe][indicator]
           if relevance == "Exclude" or relevance == "Low":
               skip indicator in scoring calculation
           else:
               include indicator with priority weight per relevance level
       ```

    3) **T801A-ADR-005-FR-003 (Defense-in-Depth Validation):** Backend SHALL re-validate indicator set even if PineScript filtering (`T801A-DEP-001`) is implemented. If irrelevant indicators detected, backend SHALL log warning and skip indicator rather than reject entire payload per `T801A-IG-015` best-effort processing.

    4) **T801A-ADR-005-FR-004 (Priority Weighting):** Indicator weights in `T801A-ADR-002` scoring formula SHALL consider matrix relevance: "High" relevance indicators receive baseline weight; "Medium" relevance receive 0.8× weight adjustment. Weight adjustments SHALL be configuration-driven per `T801A-IG-001`.

    5) **T801A-ADR-005-FR-005 (Matrix Evolution):** If Initiative T801 updates timeframe applicability matrix, Epic T801A SHALL update configuration file and re-validate playground scoring per `T801A-IG-008`. Breaking changes to matrix require Client approval before production deployment.

  **Consequences.**
  (+) Ensures Epic T801A compliance with Initiative standards per `T801A-GDR-005`
  (+) Configuration-driven matrix enables updates without code changes per `T801A-IG-001`
  (+) Defense-in-depth validation prevents backend scoring errors if PineScript filtering fails
  (±) Matrix updates from Initiative T801 require Epic T801A configuration sync
  (-) Additional validation logic; performance impact minimal per small indicator set

  **Alternatives Considered.** None

  **References.** `T801A-GDR-005 (Initiative Standard Compliance)`, `T801A-DEP-001 (Timeframe-Correct Input)`, `T801A-QG-005 (Timeframe Correctness)`, `T801A-QG-008 (MVP Simplicity)`, `T801A-IG-001 (Configuration-Driven Rules)`, `T801A-IG-007 (Initiative Matrix Reference)`, `T801A-IG-008 (Research Alignment)`, `T801A-IG-015 (Data Validation)`, `T801-RES-001 (Indicator Design Standards)`, 

  **Provenance.** 
  - `analysis_T801A-SYSTEM_research-integration.md §III.A (Finding 1)`

---

* **T801A-ADR-006 (Research Baseline Specification) {#t801a-adr-006-research-baseline-specification}**

  **Context.** Per `T801A-GDR-006`, Epic T801A establishes explicit baseline/flexible classification for research recommendations from `T801-RES-001` and `T801A-RES-001`. Classification guides Feature-level development by distinguishing non-negotiable Epic architecture decisions from flexible implementation patterns permitting alternatives per `T801A-QG-008`.

  **Decision.** Adopt the following baseline/flexible classification for research recommendations. Mandatory baselines (SHALL) define Epic-wide architecture requiring Client approval for deviations; flexible guidances (SHOULD/MAY) provide research-recommended starting points permitting Feature-level alternatives with documented rationale per `T801A-IG-008`.

  **Specification.**
    1) **T801A-ADR-006-FR-001 (Mandatory Baselines — SHALL Comply):** The following research recommendations are Epic-wide mandatory baselines requiring Client approval for deviations:
       - **Numeric Scoring Scale:** -2 to +2 symmetric 5-point scale per `T801A-RES-001` §II (adopted via GDR-002/ADR-002)
       - **JSON File Format:** TTI output artifact SHALL use JSON with versioned schema per `T801A-RES-001` §III (adopted via GDR-004/ADR-004)
       - **Timeframe Applicability Matrix Enforcement:** Backend SHALL comply with `T801-RES-001` §II matrix per `T801-RES-001` §V (Initiative Standard 1)` (adopted via GDR-005/ADR-005)
       - **MA Crossover Inclusion:** 50/200 MA crossover (Golden Cross/Death Cross) SHALL be included in MVP scope; divergence detection deferred per `T801A-RES-001` §V (adopted via `T801A-CON-002`, `T801A-IG-006`)

    2) **T801A-ADR-006-FR-002 (Flexible Guidances — SHOULD/MAY):** The following research recommendations are flexible guidances; Feature-level alternatives permitted with documented rationale per `T801A-IG-008`:
       - **Swing-Point PA Detection:** `T801A-RES-001` §IV recommends 2-bar confirmation swing-point algorithm for HH/HL vs LH/LL classification. Alternative approaches (simpler or more robust) MAY be explored at Feature level per `T801A-QG-008`. Rationale for deviation SHALL reference `T801A-IG-005` and document comparative analysis.
       - **OBV Volume Confirmation:** `T801-RES-001` §III recommends OBV inclusion for trend confirmation. Alternative volume indicators (CVD, A/D Line) or OBV removal MAY be considered if `T801A-ASSUM-003` invalidated. Rationale SHALL reference `T801A-IG-003`.
       - **Weighted Voting Scoring Formula:** `T801A-RES-001` §II recommends weighted voting ensemble. Alternative scoring methodologies (simple majority, threshold-based) MAY be explored at Feature level per `T801A-QG-008`. Rationale SHALL demonstrate `T801A-QG-002` validation criteria met. Reference `T801A-IG-004`.
       - **20/50 MA Crossover:** `T801A-RES-001` §V mentions 20/50 crossover as optional enhancement for lower timeframes (15m, 1H). Feature-level implementation MAY include 20/50 in addition to mandatory 50/200. Reference `T801A-IG-006`.

    3) **T801A-ADR-006-FR-003 (Deviation Workflow):**
       - **Mandatory Baseline Deviations:** Require explicit Client approval before Feature-level implementation. Document deviation rationale in Feature Request with comparative analysis.
       - **Flexible Guidance Deviations:** Require documented rationale in Feature Request per `T801A-IG-008`. Rationale SHALL include: (a) why research baseline not suitable; (b) alternative approach description; (c) validation plan demonstrating `T801A-QG-002` criteria met (if applicable).

    4) **T801A-ADR-006-FR-004 (Research Evolution):** If commissioned research (`T801A-RES-002` or future research) provides new recommendations:
       - **Additive Recommendations:** MAY be classified as flexible guidances without Client approval if non-breaking.
       - **Contradictory Recommendations:** Require Client decision to update baseline classification or retain existing baseline.
       - **Classification Changes:** Moving flexible guidance to mandatory baseline or vice versa requires Client approval and `T801A-ADR-006` revision.

  **Consequences.**
  (+) Explicit classification prevents inconsistent application of research across Features
  (+) Preserves research value while permitting MVP simplicity per `T801A-QG-008`
  (+) Clear deviation workflow balances governance control with Feature-level flexibility
  (±) Feature developers must consult `T801A-ADR-006` before selecting alternatives; requires documentation discipline
  (-) Baseline classifications may become outdated if research assumptions invalidated; requires periodic review

  **Alternatives Considered.** None

  **References.** `T801A-GDR-006 (Research Baseline Adoption)`, `T801A-ASSUM-003 (OBV Data Availability)`, `T801A-CON-002 (Complexity Management)`, `T801A-QG-002 (Signal Reliability)`, `T801A-QG-008 (MVP Simplicity)`, `T801A-IG-003 (Volume Confirmation)`, `T801A-IG-004 (Scoring Mechanism Guidance)`, `T801A-IG-005 (PA Detection Approach)`, `T801A-IG-006 (MA Crossover Configuration)`, `T801A-IG-008 (Research Alignment)`, `T801-RES-001 (Indicator Design Standards)`, `T801A-RES-001 (Backend TTI Architecture)`

  **Provenance.** 
  - `analysis_T801A-SYSTEM_research-integration.md`, 

---

## V. CONSULTANCY DIALOGUE NOTES (WORKING; NON-NORMATIVE)
<!-- PURPOSE: Capture raw dialogue so nothing is lost; convert into normative bodies above. -->

`prompt\artifacts\tasks\T801\consultant\workspace\proposal\T801A\notes_T801A_phase1.md`

## VI. ISSUES & RISKS REGISTER
**Issues**
<!-- GUIDANCE:
Status = `OPEN, IN-REVIEW, RESOLVED, BLOCKED, DEFERRED`,
priority = `Low, Medium, High`
-->
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Resolution Notes | Resolution Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `T801A-ISSUE-001` | "19 vs 20 vs 44" Schema Confusion | Code comments/UI text reference 19 columns, but base schema is 20 columns and enhanced is 44. Causes developer confusion. | LLM_Consultant (Phase 1); LLM_Developer (T801A1) | `RESOLVED` | High | 2026-01-05 | Canonical 20-column base schema documented in `T801A-IF-001` (Base 20 Field Table). Code comment/UI text cleanup deferred to T801A1 implementation scope. | 2026-01-06 |
| `T801A-ISSUE-002` | Row-Count Validation Missing | `EXPECTED_ROWS_PER_ALERT` exists but not enforced in webhook processing. | LLM_Developer | `RESOLVED` | Medium | 2026-01-05 | Row-count validation SHALL be enforced per `T801A-IG-015` (Input Validation). Implementation deferred to T801A1. | 2026-01-06 |
| `T801A-ISSUE-003` | Config Surface Not Wired | `/config` API toggles don't update running server; operator misunderstanding risk. | LLM_Developer | `DEFERRED` | Medium | 2026-01-05 | Legacy seam consolidation is a refactoring task during T801A1 per sandbox development mandate in `T801A-CON-001`. Non-blocking for Epic governance. | 2026-01-06 |
| `T801A-ISSUE-004` | Global-Master Dedup Data Loss | Dedup uses `(time, tf)` only; can erase different symbols. | LLM_Developer | `RESOLVED` | High | 2026-01-05 | Dedup key SHALL include `symbol` field `(symbol, time, tf)` per input validation requirements in `T801A-IG-015`. Implementation deferred to T801A1. | 2026-01-06 |
| `T801A-ISSUE-005` | Legacy Seams in tv_ingest | Multiple code paths inconsistent; docs/tests reference deprecated structures. | LLM_Developer | `DEFERRED` | Medium | 2026-01-05 | Legacy seam consolidation is a refactoring task during T801A1 per sandbox development mandate in `T801A-CON-001`. Non-blocking for Epic governance. | 2026-01-06 |
| `T801A-ISSUE-006` | 5xx Triggers TradingView Resend | Returns 500 for column-count mismatches; causes up to 4 deliveries creating duplicates. | LLM_Consultant (IG-015); LLM_Developer (T801A1) | `RESOLVED` | High | 2026-01-05 | HTTP 4xx for client validation errors (column-count mismatches) SHALL be returned instead of 5xx to prevent TradingView resend loop. Specified in `T801A-IG-015` (HTTP Response Code Guidance). Implementation deferred to T801A1. | 2026-01-06 |
| `T801A-ISSUE-007` | Pine Timezone Formatting Incorrect | `str.format()` always formats in UTC+0; may produce wrong timestamps. | LLM_Developer | `DEFERRED` | High | 2026-01-05 | PineScript `str.format()` UTC+0 limitation documented in `T801A-IF-001` as platform constraint. UTC-only timestamp assumption adopted for MVP. **Deferred to as `T801A2-ISSUE-001`**. | 2026-01-06 |
| `T801A-ISSUE-008` | Multi-TF Timestamp Semantics Unclear | Exporter builds `timeStr` using chart TF time, not requested TF. | LLM_Developer | `DEFERRED` | High | 2026-01-05 | Multi-TF timestamp semantics clarified in `T801A-IF-001`: non-chart TF data uses chart TF bar open time. **Deferred to as `T801A2-ISSUE-002`**. | 2026-01-06 |

**Risks**
<!-- GUIDANCE:
Status = `OPEN, MONITORED, MITIGATED, ACCEPTED, CLOSED`,
priority = `Low, Medium, High`
-->
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Mitigation Notes | Mitigation Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `T801A-RISK-001` | Unauthenticated Public Webhook | ngrok exposes write-capable endpoint without auth; spam/malicious payload risk. | Client | `ACCEPTED` | High | 2026-01-05 | Operational risk ACCEPTED for MVP per `T801A-QG-008` and `T801A-CON-001` (sandbox isolation). Auth deferred to post-MVP. Monitor for abuse during T801A1 playground testing. | 2026-01-06 |
| `T801A-RISK-002` | Timestamp Timezone Ambiguity | Pine can emit UTC or local TZ; storage is naive; breaks dedup/history keying. | LLM_Consultant | `MITIGATED` | High | 2026-01-05 | UTC-only assumption documented in `T801A-IF-001` . Backend validation per `T801A-IG-015`. Exporter fix tracked via `T801A2-ISSUE-001`. | 2026-01-06 |
| `T801A-RISK-003` | Override Storage Mode Erases History | Default `data_storage_mode="override"` can overwrite prior history. | Client | `MITIGATED` | Medium | 2026-01-05 | Append mode recommended for Phase 1; current-state constraints documented in `T801A-IG-016` and `T801A-DEP-004`. | 2026-01-06 |
| `T801A-RISK-004` | VWAP Filtering tf Code Dependency | If `tf` becomes display-form, VWAPFilter fails-open. | LLM_Developer | `MITIGATED` | Medium | 2026-01-05 | `tf` code semantics validated in `T801A-IF-001` . VWAPFilter behavior tested in T801A1. | 2026-01-06 |
| `T801A-RISK-005` | At-Least-Once Delivery Duplicates/Loss | TradingView resends on 5xx; imperfect dedup can duplicate or drop rows. | Client | `MITIGATED` | High | 2026-01-05 | HTTP 4xx for validation errors per `T801A-IG-015` prevents TradingView resend loop. Dedup key fix `(symbol, time, tf)` per ISSUE-004 resolution. Idempotent processing validated in T801A1. | 2026-01-06 |
| `T801A-RISK-006` | 3-Second Webhook Cancellation | TradingView cancels if processing exceeds ~3s; synchronous pipeline may exceed under load. | Client | `MONITORED` | Medium | 2026-01-05 | Requires `T801A1` load testing. If needed, implement async acknowledge-then-process pattern. Governed by `T801A-ASSUM-004`. **Deferred to as `T801A1-RISK-001`**. | 2026-01-06 |
| `T801A-RISK-007` | Message Body Size Limit | 40960 char cap limits feasible `(exportRows × tf_count)`. | LLM_Consultant | `MITIGATED` | Medium | 2026-01-05 | Artifact size guidance per `T801A-IG-010` (~1500-2000 chars target). 40960 char cap documented in `T801A-IF-001` . Validated exportRows×tf_count in T801A2. | 2026-01-06 |
| `T801A-RISK-008` | Repainting/Confirmation Drift | Multi-TF rows from `request.security()` can change after initial alert delivery. | LLM_Consultant | `ACCEPTED` | Medium | 2026-01-05 | Limitation documented in `T801A-IF-001` . ACCEPTED as inherent platform behavior for MVP. Confirmation delay strategy evaluation deferred to T801A2. | 2026-01-06 |
| `T801A-RISK-009` | Volume Integration Risk | OBV-based volume confirmation per `T801A-ASSUM-003` is a new addition to the TTI protocol with significant uncertainty (value-add, complexity, false positives in low-volume conditions). Impact: If realized, volume confirmation is removed from MVP scope. | Client | `MONITORED` | High | 2025-12-31 | Early comparative validation (with/without OBV) during `T801A1` playground testing; fallback to proceed without volume signal; governed by `T801A-ASSUM-003` / `T801A-IG-003`. **Deferred to as `T801A1-RISK-002`**. | 2026-01-06 |

### Feature-Level Deferred Items

**Purpose**: Aggregate Issues/Risks deferred from Epic scope to specific Feature development phases per T102-STD-007-FR-009.

#### T801A2 (PineScript) Feature Issues
<!-- GUIDANCE:
Status = `OPEN, IN-REVIEW, RESOLVED, BLOCKED, DEFERRED`,
priority = `Low, Medium, High`
-->
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Resolution Notes | Resolution Date |
|:---|:------|:------------|:------|:-------|:---------|:--------------|:-----------------|:----------------|
| `T801A2-ISSUE-001` | Pine Timezone Formatting | PineScript `str.format()` always formats in UTC+0; may produce incorrect timestamps for non-UTC users. Promoted from `T801A-ISSUE-007`. | LLM_Developer | `OPEN` | High | 2026-01-06 | — | — |
| `T801A2-ISSUE-002` | Multi-TF Timestamp Semantics | Exporter builds `timeStr` using chart TF time, not requested TF; causes timestamp ambiguity for non-chart timeframes. Promoted from `T801A-ISSUE-008`. | LLM_Developer | `OPEN` | High | 2026-01-06 | — | — |

#### T801A1 (Backend) Feature Risks
<!-- GUIDANCE:
Status = `OPEN, MONITORED, MITIGATED, ACCEPTED, CLOSED`,
priority = `Low, Medium, High`
-->
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Mitigation Notes | Mitigation Date |
|:---|:------|:------------|:------|:-------|:---------|:--------------|:-----------------|:----------------|
| `T801A1-RISK-001` | Webhook Processing Timeout | TradingView cancels if processing exceeds ~3s; synchronous pipeline may exceed under load. Promoted from `T801A-RISK-006`. | Client | `OPEN` | Medium | 2026-01-06 | — | — |
| `T801A1-RISK-002` | Volume Integration Uncertainty | OBV-based volume confirmation (ASSUM-003) has significant uncertainty (value-add, complexity, false positives in low-volume conditions). Promoted from `T801A-RISK-009`. | Client | `OPEN` | High | 2026-01-06 | — | — |

---

## VII. OPEN QUESTIONS REGISTER (WORKING)
| ID | Topic | Question | Owner | Status | Proposed Date | Resolved Date |
|:---|:------|:---------|:------|:-------|:--------------|:-------------|
| — | — | None. | — | — | — | — |


## VIII. RESEARCH & NOTES

| RES-ID | Title | Purpose | Blocking Items | Status |
|:-------|:------|:--------|:---------------|:-------|
| **T801A-RES-002** | System Architecture Research | Map current system pipeline; document I/O contracts; propose schema governance; define "minimal market context". Brief: `prompt/artifacts/tasks/T801/research/brief/brief_T801A-RES-002_system-architecture-research.md` | IF-001 finalization, IG-014, IG-016 | Completed |
| **T801A3-RES-001** | LLM_Trader Consumption Adaptation | Analyze VPA Type 1/2 trading-session prompts; specify how `T801A3 (LLM_Trader)` should consume the `T801A1` TTI JSON artifact to preserve/improve analysis quality | DEP-003, IF-003, IG-010 | 📌 Recommended (Not commissioned) |
| **T801A2-RES-001** | TradingView Payload Schema Evolution | Assess semicolon-delimited vs JSON payload formats for TradingView alerts; document PineScript export constraints; propose safe schema evolution/versioning path post-MVP | IF-001 schema evolution, post-MVP automation | 📌 Recommended (Not commissioned) |

---

## IX. APPROVAL GATE (CLIENT)
- [x] **41 E-RIDs** approved (ASSUM 6, CON 4, DEP 4, IF 3, IG 16, QG 8)
- [x] **6 E-GDRs** approved (index + full bodies)
- [x] **6 E-ADRs** approved (index + full bodies)
- [x] **17 Epic Issues/Risks** approved (8 Issues + 9 Risks; Epic-level only)
- [x] Open Questions: **None** (explicit)

> **Client Approval Statement (Single Block)**
> - **Approved by**: Client
> - **Approval date**: 2026-01-10
> - **Approved scope**: 41 E-RIDs + 6 E-GDRs + 6 E-ADRs + 17 Epic Issues/Risks (Epic-level only)

---

## X. CHANGELOG

- **v1.15.1** (2026-01-10): Client approval captured:
  - Added single approval statement block under `## IX. APPROVAL GATE (CLIENT)` (scope: 41 E-RIDs, 6 GDRs, 6 ADRs, 17 Issues/Risks)
- **v1.15.0** (2026-01-10): Subphase 1.4 proposal finalization (ready-to-sign):
  - Updated executive summary to reflect final approval scope (41 E-RIDs, 6 GDRs, 6 ADRs, 17 Issues/Risks) and Phase 2 implication
  - Repaired Open Questions hygiene (no phantom OQ blockers)
  - Aligned `## IX. APPROVAL GATE (CLIENT)` checklist to the full approval scope (including ADRs + Issues/Risks)
- **v1.14.0** (2026-01-10): Task 1.3.3.3 Cross-Category Dependency Validation:
  - **Cross-Category Gaps Fixed**: Added explicit cross-references to DEP-001 (CON-001, ASSUM-004), DEP-003 (CON-003, ASSUM-005), IF-003 (IG-013, IG-014)
  - **Activity 1.3.3 Complete**: All E-RID, E-DR, and cross-category compliance verified
  - **OID Completeness**: RES, ISSUE, RISK categories complete; no NOTE items required
- **v1.13.0** (2026-01-09): Task 1.3.3.2 E-DR T102-STD-004/005 Compliance Updates:
  - **FR-001 (ADR Index)**: Added Owner, Effective, Supersedes, Anchor columns to E-ADR Index; retained Paired GDR
  - **FR-006 (T102-STD-005)**: Standardized ~85 bare ID references to fully-qualified short-hand in Section IV (GDR + ADR bodies)
  - **Alternatives Considered**: Set to "None" per consultancy QA (fabricated content removed from all 6 ADRs)
  - **Content Quality**: Trimmed verbose Context sections in GDR-005/GDR-006 (~30% reduction); trimmed ADR-001 FR-006
  - **T102-STD-004 Amendment**: FR-001 updated with separate GDR/ADR schema tables in concept file (v1.1.0)
- **v1.12.1** (2026-01-09): Task 1.3.3.1 Additional E-RID Compliance Fixes:
  - **FR-006**: Replaced all unscoped local alias references (e.g., `IF-002`, `QG-007`) with fully-qualified `T801A-...` IDs within Section III
  - **FR-006**: Added external-only `Reference:` lines for E-RIDs that cite outside-Epic IDs (QG-005, IG-008)
  - **FR-009**: Extended ASSUM table with `If Invalidated` (Fallback/Escalation/Mitigation) response column
  - **FR-005**: Renamed QG-003/QG-004/IG-016 titles to meet 2–3 word minimum/maximum
  - **Clean-up**: Removed duplicate HTTP response guidance block in IG-015
- **v1.12.0** (2026-01-08): Task 1.3.3.1 E-RID T102-STD-005 Compliance Updates:
  - **FR-005**: Shortened IF-001/IF-002 titles to ≤3 words
  - **FR-006**: Standardized 13 in-body references to short-hand format
  - **FR-009**: Added ASSUM Validation Lifecycle Summary table above Section III.A
  - **FR-011**: Content refactoring for 6 E-RIDs (ASSUM-004/005, CON-003, QG-003/007, DEP-004)
  - **IF-001 Refactor**: Moved validation behavior content to IG-015
- **v1.11.0** (2026-01-06): Activity 1.3.2 Risk Mitigation per T102-STD-007:
  - **Section VI.B (Risks) Finalized**: All 9 Epic-level Risks updated with final statuses (5 MITIGATED, 2 ACCEPTED, 2 promoted to Feature) and Mitigation Notes citing governing E-RIDs
  - **T801A1 Feature Risks Added**: RISK-006/009 promoted to `T801A1-RISK-001/002` for T801A1 (Backend) Feature scope
  - **Activity 1.3.2 Status**: Task 1.3.2.3 (Risk Mitigation) complete; proceeding to Task 1.3.2.4 (Cross-Reference Validation)
- **v1.10.0** (2026-01-06): Activity 1.3.2 Issue Resolution per T102-STD-007:
  - **Section VI.A (Issues) Finalized**: All 8 Epic-level Issues updated with final statuses (4 RESOLVED, 4 DEFERRED) and Resolution Notes citing governing E-RIDs
  - **Feature-Level Subsection Created**: New "Feature-Level Deferred Items" subsection added per T102-STD-007-FR-009
  - **T801A2 Feature Issues Added**: ISSUE-007/008 promoted to `T801A2-ISSUE-001/002` for T801A2 (PineScript) Feature scope
  - **Activity 1.3.2 Status**: Task 1.3.2.2 (Issue Resolution) complete; proceeding to Task 1.3.2.3 (Risk Mitigation)
- **v1.9.0** (2026-01-05): T801A-RES-002 research integration + Activity 1.3.1/1.3.3 completion:
  - **Section II.E Updated**: IF-001 status "Partial" → "Confirmed"; source updated to include T801A-RES-002
  - **Section II.F Updated**: IG-014 status "Partial" → "Confirmed"; source updated to include T801A-RES-002
  - **Section III.E (IF-001) Finalized**: Complete Base 20-column schema with field table, multi-timeframe semantics, TradingView platform constraints (3s timeout, 40k char cap, 5xx resend behavior, timezone formatting), validation behavior, cross-references to ISSUE-001/006/007/008
  - **Section III.F (IG-014) Finalized**: Complete minimal market context specification (~1500-2000 chars) with required structure, per-timeframe fields, optional chart TF history, size guidance
  - **Section III.F (IG-015) Updated**: Added HTTP Response Code Guidance (4xx for client errors to prevent TradingView resend loop); cross-references to ISSUE-006, RISK-005
  - **Section III.F (IG-016) Updated**: Added current-state format specifics (5 bars chart TF, 1 bar others), calculation feasibility table, timestamp caveat references to ISSUE-007/008
  - **Section III.A (ASSUM-004) Updated**: Added TradingView Operational Constraints section with 5 platform constraints, validation criteria, fallback strategy
  - **Section III.D (DEP-004) Updated**: Added historical depth specifics (5 bars chart TF, 1 bar others), feasibility assessment, cross-reference to IG-016 and T801A-RES-002
  - **Section IV.D (ADR-001) Updated**: Removed PARTIAL status from Decision; added FR-006 (Pipeline Mapping) with complete Mermaid diagram, artifact inventory table, human workflow handoff points
  - **Section IV.D (ADR-004) Updated**: Removed PARTIAL status from Context; updated FR-006 (Minimal Market Context Scope) with complete per-timeframe field specifications, size target
  - **Section VI.A (Issues) Populated**: Imported 8 Issues from T801A-RES-002 (ISSUE-001 through ISSUE-008) with full descriptions, owners, statuses (5 HIGH, 3 MEDIUM priority)
  - **Section VI.B (Risks) Expanded**: Imported 7 new Risks from T801A-RES-002 (RISK-002 through RISK-008); updated RISK-001 description for unauthenticated webhook (3 HIGH, 5 MEDIUM priority)
  - **Section V.H Added**: Complete Subphase 1.3 dialogue notes covering Activity 1.3.1 (Research Commission Completion) and Activity 1.3.3 (Issues/Risks Register Import) with research integration summary table, TradingView constraints, HIGH priority resolution strategy, ASSUM-004 elevation assessment, key outcomes
  - **Cross-References Updated**: All finalized E-RIDs now reference relevant Issues/Risks (IF-001 → ISSUE-001/006/007/008; IG-015 → ISSUE-006, RISK-005; etc.)
  - **Analysis Reference Added**: YAML header now includes `analysis_reference` pointing to T801A-RES-002 integration analysis file
  - **Subphase 1.3 Status**: Activity 1.3.1 complete; Activity 1.3.3 complete; ready for Activity 1.3.2 (Cross-Category Analysis) and 1.3.4 (Final Preparation)
