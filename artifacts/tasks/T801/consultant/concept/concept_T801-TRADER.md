---
artifact_type: 'CONCEPT'
initiative_id: 'T801'
initiative_code: 'TRADER'
version: '1.0.1'
date: '2026-01-10'
status: 'review'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
---

## III. CORE CONTENT

### A. Identity & Operating Rules
<!-- 
- Canonical header + links to governing GDRs/ADRs (inheritance table: “link-don’t-duplicate”).  <!-- T102-GDR-002/003/004/005 
- Scope & boundaries (what lives in SPS vs Request vs Design); change log.
--> 

### B.  Decision System (ADR Compendium)

#### 1. Initiative Architectural Decisions

| ADR ID | Title | Status | Effective | Supersedes | Anchor |
|--------|-------|--------|-----------|------------|--------|

#### 2. Epic Architectural Decisions

##### i. `T801A` Epic: `TTI` — Timeframe Trend Identification

| ADR ID | Title | Paired GDR | Status | Owner | Effective | Supersedes | Anchor |
|:-------|:------|:-----------|:-------|:------|:----------|:-----------|:-------|
| `T801A-ADR-001` | Hybrid Integration Pattern | `T801A-GDR-001` | Proposed | Client | 2026-01-03 | — | #t801a-adr-001-hybrid-integration-pattern |
| `T801A-ADR-002` | Scoring Algorithm Specification | `T801A-GDR-002` | Proposed | Client | 2026-01-03 | — | #t801a-adr-002-scoring-algorithm-specification |
| `T801A-ADR-003` | Playground Deployment Architecture | `T801A-GDR-003` | Proposed | Client | 2026-01-03 | — | #t801a-adr-003-playground-deployment-architecture |
| `T801A-ADR-004` | TTI File Schema | `T801A-GDR-004` | Proposed | Client | 2026-01-03 | — | #t801a-adr-004-tti-file-schema |
| `T801A-ADR-005` | Timeframe Applicability Enforcement | `T801A-GDR-005` | Proposed | Client | 2026-01-03 | — | #t801a-adr-005-timeframe-applicability-enforcement |
| `T801A-ADR-006` | Research Baseline Specification | `T801A-GDR-006` | Proposed | Client | 2026-01-03 | — | #t801a-adr-006-research-baseline-specification |

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


#### 3. Feature Architectural Decisions
| ADR ID | Title | Status | Effective | Supersedes | Anchor |
|--------|-------|--------|-----------|------------|--------|


### C. Readiness Snapshot (Lean, manual)
<!-- 
- **A. Roll-up Table** (Initiative/Epics/Features: State | Ready? | Top blockers | Next gate | Updated_at)
- **B. DoR Checklists (brief)** per tier (links to Request/Design for evidence)
- **C. Notes & Overrides** (Client approvals recorded with ID)
-->

### D. Handoff Snapshot (Authoritative)
<!-- 
- **A. Package Manifest** (immutable IDs, doc versions/SHAs)
- **B. Acceptance Signals** (Client sign-off, gate approvals)
- **C. Completeness Checklist** (ADR accepted; FRs approved; risks linked)
- **D. Links** (SPS/Request/Design anchors; no copy-paste)
-->

### E. Registers 
<!-- 
- Risks/Assumptions/Dependencies registers (pointer-based; no duplication)
-->
#### 1. Feature Register

#### 2. Design Register
| Epic ID | Feature ID | Story ID | Design Log | Status | Notes |
| :------ | :--------- | :------- | :--------- | :----- | :---- |



### F. Integration & Interfaces
<!-- 
- Planner consumption notes (schema, payload outline), cross-traceability rules.
-->


### G. Governance

<!-- 
- Local GDRs for Concept (e.g., T102C-GDR-003/005 once accepted) + change control.
-->
