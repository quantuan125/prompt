---
artifact_type: 'RESEARCH_REPORT'
initiative_id: 'T801'
epic_id: 'T801A'
research_id: 'T801A-RES-002'
version: '1.0.0'
iteration: '1'
date: '2026-01-04'
status: 'draft'
author: 'LLM_Researcher'
decision_owner_role: 'Client'
---

# RESEARCH REPORT: T801A-RES-002 — System Architecture Research (tv_ingest Baseline, Code-As-Master)

## I. EXECUTIVE SUMMARY

**Context**: This research was commissioned to remove ambiguity blocking Phase 1 governance artifacts for Epic `T801A`, specifically `T801A-IF-001` (Webhook contract), `T801A-IG-014` (minimal market context), `T801A-IG-016` (historical format), and to provide current-state evidence for `T801A-ADR-001` (hybrid integration pipeline map).

**Verdict**: **GO (with clarifications)** to finalize `T801A-IF-001` for the **Base (20-column)** webhook contract as it is clearly defined by `nmaq_exporter.pine` and enforced by `webhook_server.py`. **NO-GO** to finalize an “Enhanced (44-column)” webhook contract as a required/primary path because (a) Pine currently emits the 20-column base schema and (b) stored artifacts show drift (no deltas; VWAP filtering not applied), so “enhanced” is not an observable SSOT behavior today.

**Key Findings**:
*   **Current-state pipeline is unambiguous**: TradingView (Pine alert) → ngrok HTTPS → FastAPI webhook → pandas parse → processor validate/enhance → CSV storage → Streamlit UI export → manual handoff to LLM_Trader.
*   **Webhook payload is semicolon-delimited, headerless, row-per-candle**; schema is enforced only by **column count**, not by row count or a version tag.
*   **TradingView webhook delivery has hard operational constraints**: only ports 80/443, request cancelled after ~3 seconds, and **5xx responses trigger up to 3 resends** (max 4 deliveries per trigger). This directly impacts idempotency, error code choices, and “at-least-once” assumptions in `IF-001`.
*   **Alert/webhook message body size is capped**: 40960 characters when using Pine `alert()`; this can cap feasible `(exportRows × tf_count)` without truncation/failed delivery.
*   **Pine timestamp/timezone handling is easy to get wrong**: `str.format()` always formats times as UTC+0; the recommended approach for time-zone-specific strings is `str.format_time()`. This matters for `RISK-002` and `IG-016` timestamp semantics.
*   **Observed data artifacts are drift signals**: `components/tv_ingest/data/global_master.csv` and per-symbol `master.csv` show **20 columns only**, **no delta columns**, and VWAPs present even where backend rules would filter them (e.g., `tf=W` still contains session/weekly VWAP).
*   **Multiple “internal drift” seams exist inside `components/tv_ingest/`** (legacy/unused paths, doc/test mismatches, unused config knobs), which should be logged as Issues/Risks rather than “fixed” during research.

---

## II. METHODOLOGY AUDIT

**Scope Adherence**: Stayed inside repository current-state analysis; no code changes, migrations, or refactors. External web research **was performed (2026-01-04)** to validate TradingView webhook delivery constraints, Pine alert/time semantics, and Binance market-data endpoint semantics. External sources are used only to strengthen governance implications and risk framing; **Pine + repo code remain the SSOT** for “what the system does today.”

**Source of Truth Audit**:
*   **Authoritative (Code + Pine)**:
    *   `components/tv_ingest/backend/api/webhook_server.py:100`
    *   `components/tv_ingest/backend/processors/webhook_processor.py:109`
    *   `components/tv_ingest/backend/processors/formattings/llm_context_formatter.py:1`
    *   `components/tv_ingest/backend/processors/calculations/delta_calculator.py:1`
    *   `components/tv_ingest/backend/processors/filterings/vwap_filter.py:1`
    *   `components/tv_ingest/utils/constant.py:1`
    *   `components/tv_ingest/assets/pine/nmaq_exporter.pine:1`
    *   `components/tv_ingest/assets/pine/nmaq.pine:1`
*   **Prompt compatibility context**:
    *   `prompt/roles/VPA/main_v2.1.md:1`
    *   `prompt/roles/VPA/example.md:1`
*   **External references (constraints/semantics; non-SSOT)**:
    *   TradingView: “How to configure webhook alerts” (ports 80/443, 3s cancel, content-type behavior, IP allowlist, 2FA requirement): https://www.tradingview.com/support/solutions/43000529348-how-to-configure-webhook-alerts/
    *   TradingView: “Webhook resubmission” (5xx → up to 3 resends): https://www.tradingview.com/support/solutions/43000735201-webhook-resubmission/
    *   TradingView: “Alert name and message size limits” (40960 char cap for Pine `alert()`): https://www.tradingview.com/support/solutions/43000773947/
    *   TradingView: “Webhook authentication” (client certificate fields): https://www.tradingview.com/support/solutions/43000680459-webhook-authentication/
    *   TradingView Pine docs: “Concepts / Alerts” (alert frequency semantics): https://www.tradingview.com/pine-script-docs/v5/concepts/alerts/
    *   TradingView Pine docs: “Concepts / Time” (timestamps are TZ-agnostic; prefer `str.format_time()`; `str.format()` UTC+0): https://www.tradingview.com/pine-script-docs/v5/concepts/time/
    *   TradingView Pine docs: “Bar states” (note: `barstate.isconfirmed` pertains to chart, not `request.security()`): https://www.tradingview.com/pine-script-docs/v3/essential/barstate/
    *   Binance Futures API docs: Funding rate history: https://binance-docs.github.io/apidocs/futures/en/#get-funding-rate-history
    *   Binance Futures API docs: Open interest history: https://binance-docs.github.io/apidocs/futures/en/#open-interest-statistics
    *   Binance USDS-M Futures REST API docs: Kline/Candlestick data (OHLCV/backfill): https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Kline-Candlestick-Data
*   **Data Artifacts (drift signals inspected)**:
    *   `components/tv_ingest/data/global_master.csv:1`
    *   `components/tv_ingest/data/BINANCE_BTCUSDT/master.csv:1`

**Limitations**:
*   Python runtime dependencies (e.g., `pandas`) are not available in the current environment, so behavior was verified by static forensics (code + artifacts), not by executing the server end-to-end.
*   `storage/tv_ingest/` was intentionally ignored per brief.

---

## III. TOPIC FINDINGS

### Topic 1: Pipeline Map (Current State, Code-As-Master)
**Objective**: Produce a single unambiguous pipeline map and artifact inventory.

#### A. Evidence & Forensics
*   **Source**: `components/tv_ingest/assets/pine/nmaq_exporter.pine:1`
*   **Observation**: Pine constructs a headerless payload where each row is a semicolon-separated record, emitted via `alert(payload, alert.freq_once_per_bar)`.

*   **Source**: `components/tv_ingest/backend/api/webhook_server.py:100`
*   **Observation**: FastAPI `POST /` receives raw body, parses with `pd.read_csv(... sep=';')`, assigns columns based on count (20 or 44), then calls `WebhookProcessor.process_webhook_data(...)`.

*   **Source**: `components/tv_ingest/backend/processors/webhook_processor.py:60`
*   **Observation**: Processor validates/coerces types, optionally applies delta calculations and VWAP filtering, then writes symbol/timeframe files + symbol master + global master.

*   **Source**: `components/tv_ingest/frontend_builder/builders/webhook_control_builder.py:1`
*   **Observation**: Streamlit UI starts/stops the FastAPI server and surfaces the ngrok URL; user manually configures TradingView alerts to send to that URL.

*   **Source**: `components/tv_ingest/frontend_builder/builders/export_builder.py:1`
*   **Observation**: Streamlit UI exports data for manual copy/download into an LLM session (human workflow handoff).

#### B. Evidence Diagram (Mermaid)
```mermaid
flowchart TD
  TV[TradingView Alert<br/>Pine: NMAQ_Exporter] -->|HTTP POST<br/>body=text (rows)| NG[ngrok HTTPS public URL]
  NG --> API[FastAPI WebhookServer<br/>POST /]

  API --> PARSE[pandas.read_csv(sep=';')<br/>header=None]
  PARSE --> COLS[Column-count gate:<br/>20=BASE_COLUMNS, 44=CSV_COLUMNS]

  COLS --> PROC[WebhookProcessor.process_webhook_data]
  PROC --> VALIDATE[Datetime + numeric coercion]
  VALIDATE --> ENH[Enhancements (best-effort):<br/>DeltaCalculator + VWAPFilter]
  ENH --> STORE[CSV storage:<br/>symbol_dir/tf.csv<br/>symbol_dir/master.csv<br/>global_master.csv]

  STORE --> UI[Streamlit UI:<br/>Data View / Export]
  UI --> HUMAN[Manual handoff:<br/>copy/attach export]
  HUMAN --> LLM[LLM_Trader (VPA prompt)]
```

#### C. Artifact Inventory (Producer/Consumer/Format)
| Artifact | Path | Producer | Consumer | Format | Notes |
|---|---|---|---|---|---|
| Webhook ingress | `POST /` | TradingView alert | FastAPI server | text/plain-ish | Headerless, semicolon-separated rows |
| Symbol timeframe file | `components/tv_ingest/data/<SYMBOL_DIR>/<TF_DISPLAY>.csv` | `WebhookProcessor` | Streamlit UI/export; downstream tools | CSV | Column order is normalized on save (`symbol`, `tf`, `time`, …) |
| Symbol master | `components/tv_ingest/data/<SYMBOL_DIR>/master.csv` | `WebhookProcessor` | Streamlit UI/export | CSV | Multi-timeframe aggregate |
| Global master | `components/tv_ingest/data/global_master.csv` | `WebhookProcessor` | Streamlit UI/export | CSV | Multi-symbol + multi-timeframe aggregate |
| LLM context (text) | Export UI | Human | LLM | Text | Current service export is “dataframe dump”; formatter exists but isn’t the UI default |

**Human workflow handoff points**:
1. Copy ngrok HTTPS URL into TradingView alert webhook settings (manual).
2. After data arrives, user exports context (manual) and pastes/attaches to LLM_Trader chat (manual).
3. Optional manual overrides are currently a “human-only” step; there is no enforced schema/versioning on exported context.

#### D. Governance Implication
*   The current-state pipeline map is sufficient as direct evidence for `T801A-ADR-001` (hybrid integration pattern) with explicit identification of the manual handoff boundary.

---

### Topic 2: Webhook Contract (IF-001)
**Objective**: Document intended webhook payload contract and failure behaviors enforced by current code + Pine.

#### A. Evidence & Forensics
*   **Source**: `components/tv_ingest/assets/pine/nmaq_exporter.pine:1`
*   **Observation**: Each row is built as: `syminfo.tickerid + ";" + timeStr + ";" + <fields> + ";" + tfLabel_curr`.

*   **Source**: `components/tv_ingest/backend/api/webhook_server.py:108`
*   **Observation**: Server parses the entire body as a semicolon-separated table; no JSON wrapper; no headers.

*   **Source**: `components/tv_ingest/backend/api/webhook_server.py:112`
*   **Observation**: Only validates **column count** (20 or 44). Any other count throws and returns a 500 error response.

*   **Source**: `components/tv_ingest/backend/processors/webhook_processor.py:128`
*   **Observation**: Numeric coercion uses strict `errors='raise'` for most numeric columns; VWAP fields use `errors='coerce'`.

#### B. Analysis

##### Base Contract (20-column) — Canonical Today (GO to finalize)
**Delimiter rules**
* Rows separated by newline `\n`
* Columns separated by semicolon `;`
* No header row
* No quoting/escaping rules are explicitly enforced beyond what `pandas.read_csv(... sep=';')` tolerates.

**Field order (Base schema, 20 columns)**  
Authoritative names and order are defined by `BASE_COLUMNS` in `components/tv_ingest/utils/constant.py:1` and must match Pine emission order:

| # | Field | Type | Example | Notes |
|---:|---|---|---|---|
| 1 | `symbol` | string | `BINANCE:BTCUSDT` | From `syminfo.tickerid`; stored raw; directory name is sanitized separately |
| 2 | `time` | datetime string | `2025-12-23 22:00:00` | Pine formats with chosen timezone, backend stores as naive |
| 3-6 | `open,high,low,close` | float | `88620.79` | |
| 7 | `volume` | float | `12804.02886` | |
| 8-9 | `vol_ma20,vol_ma30` | float | `15679.57` | |
| 10-13 | `ema9,ema21,ema50,ema200` | float | `88184.41` | |
| 14 | `sma200` | float | `107773.37` | |
| 15-16 | `rsi,rsi_ma14` | float | `43.3861` | |
| 17-19 | `vwap_session,vwap_week,vwap_month` | float | `87753.21` | Backend may later mask irrelevant VWAPs (if enabled and functioning) |
| 20 | `tf` | string code | `60`, `D`, `W` | Raw timeframe code, not the display name |

**Multi-timeframe behavior (payload composition)**
* Pine always emits **N rows (1–5)** for the *current chart timeframe* (`exportRows`, default 5).
* Pine may append **one additional row per configured extra timeframe** (1m/3m/…/2W) (not 5 rows each). This is critical for `IG-016`.

##### TradingView Webhook Delivery Constraints (External; Must Be Reflected in IF-001/ADR-001)
These constraints are not encoded in repo code, but they govern real-world reliability and must be treated as “environmental invariants” for the pipeline:
* **Port restrictions**: Only ports **80** and **443** are accepted when a port is specified in the webhook URL.
* **Processing timeout**: If the receiving server takes longer than ~**3 seconds** to process, TradingView cancels the request.
* **IPv6**: TradingView explicitly states IPv6 is not currently supported for webhooks.
* **Content-Type**: If the alert message is valid JSON, TradingView sets `Content-Type: application/json`; otherwise `text/plain`.
* **Resubmission behavior**: If the receiver responds **500–599**, TradingView resends up to **3** times after **5 seconds** each (max **4** deliveries per trigger). This means current `500` responses for validation/parse errors can create duplicates and should be treated as an at-least-once delivery risk.
* **Message body size**: The webhook request body shares the same limits as alert messages; Pine `alert()` messages are capped at **40960 characters**.
* **2FA gate**: Webhook alerts require 2-factor authentication to be enabled on the TradingView account.
* **Optional authentication via client certificate**: TradingView documents a client certificate subject/issuer that can be used for webhook authentication. This is only actionable if TLS is terminated where the application can validate the client certificate (may not be feasible behind a generic tunnel/proxy like ngrok).

##### Pine Alert + Time Semantics (External; Must Be Reflected in IF-001/IG-016)
* Pine `alert(message, freq)` frequency semantics are defined by TradingView (e.g., `alert.freq_once_per_bar`, `alert.freq_once_per_bar_close`, `alert.freq_all`). The exporter calls `alert(..., alert.freq_once_per_bar)` but gates alerting with `exportMode` (`barstate.isconfirmed` for “closed” mode vs `barstate.islast` for “live” mode). Governance docs should treat alert timing as **configuration-dependent** rather than assuming “bar close only.”
* **Important footnote**: TradingView documentation notes `barstate.isconfirmed` pertains to the chart’s main symbol/timeframe and “does not consider `request.security()` calls.” This means multi-timeframe rows derived via `request.security()` can still exhibit repainting/confirmation drift unless explicitly designed to avoid it.
* **Timezone formatting risk**: TradingView’s time documentation states `str.format()` always formats times in UTC+0 and recommends `str.format_time()` for timezone-specific formatting. In `nmaq_exporter.pine`, timestamps are created using `str.format("{0,time,...}", timeLocalSeries[i])`, which may produce UTC strings even when `timeZoneOpt` is set to `Europe/Copenhagen`.

##### Enhanced Contract (44-column) — Supported by Server, Not Emitted by Pine (NO-GO as required today)
* Server accepts 44 columns (`CSV_COLUMNS = BASE_COLUMNS + DELTA_COLUMNS`) if the payload column count equals 44 (`components/tv_ingest/backend/api/webhook_server.py:116`).
* Current `nmaq_exporter.pine` emits the 20-column base schema, and artifacts show no delta columns on disk; treat 44-column ingress as “latent/optional,” not as the canonical TradingView webhook contract.

##### Current Failure/Validation Behaviors
* **Column count mismatch** → raises `ValueError` and returns `status_code=500` (`components/tv_ingest/backend/api/webhook_server.py:121`).
* **Numeric parsing failures** (non-VWAP numeric fields) → processor returns error → server returns `status_code=500` (`components/tv_ingest/backend/api/webhook_server.py:130`).
* **Invalid timeframe values** → warns and may skip storage for those rows (not a hard failure) (`components/tv_ingest/backend/processors/webhook_processor.py:271`).
* **Row count is not validated** despite `EXPECTED_ROWS_PER_ALERT` existing; this is tracked as an Issue.

#### C. Governance Implication
*   `T801A-IF-001` can be finalized now for the Base (20-column) contract, with explicit notes on multi-timeframe row semantics and timestamp semantics.
*   `T801A-IF-001` should explicitly define **receiver expectations** given TradingView behavior: keep response time <3s, treat deliveries as **at-least-once**, and avoid returning 5xx for “expected/validation” errors to prevent resubmission amplification.

---

### Topic 3: Storage Schema & Drift Characterization (IG-016 input support)
**Objective**: Document intended storage schema vs observed artifacts; classify drift.

#### A. Evidence & Forensics
*   **Source**: `components/tv_ingest/utils/constant.py:1`
*   **Observation**: `BASE_COLUMNS=20`, `DELTA_COLUMNS=24`, `CSV_COLUMNS=44`. VWAP relevance rules exist via `VWAP_RELEVANCE` and `TF_TO_MINUTES`.

*   **Source**: `components/tv_ingest/backend/processors/filterings/vwap_filter.py:1`
*   **Observation**: Backend is designed to mask irrelevant VWAPs to `NaN` based on timeframe (e.g., Weekly should keep Month only).

*   **Source**: `components/tv_ingest/backend/processors/calculations/delta_calculator.py:1`
*   **Observation**: Backend is designed to compute delta and delta% columns after ingest.

*   **Source**: `components/tv_ingest/data/global_master.csv:1`
*   **Observation**: File has **20 columns** (base only), not 44.

*   **Source**: `components/tv_ingest/data/BINANCE_BTCUSDT/master.csv:1`
*   **Observation**: File has **20 columns** (base only); no delta columns present.

*   **Source**: `components/tv_ingest/data/BINANCE_BTCUSDT/master.csv:2`
*   **Observation**: For `tf=W`, both `vwap_session` and `vwap_week` are present even though backend VWAP relevance rules would mask them for weekly timeframe.

#### B. Analysis
**Drift Type**: “Historical artifact writer drift” (high confidence).  
Artifacts appear to predate or bypass (a) delta calculations and (b) VWAP filtering.

**Impact**:
* Governance artifacts must treat on-disk CSVs as **non-authoritative**; they cannot be used to infer the enforced schema or filtering behavior.
* Any contract/spec derived from artifacts will conflict with code-as-master.

**Additional Context (Evolutionary Drift)**:
This drift likely stems from a prior schema transition (Pine v1 to v2) where indicator coverage (RSI, Vol MAs) and multi-timeframe tagging were expanded without a corresponding backfill of existing CSV artifacts. The absence of the `tf` column in older files indicates they likely captured only the chart-timeframe at that time, whereas the current schema uses the `tf` field explicitly to allow multi-timeframe data to co-exist in normalized master files.

#### C. Governance Implication
*   `T801A-ADR-004` must explicitly separate “intended schema (code)” from “observed schema (drift)” and avoid inferring contracts from drift artifacts.

---

### Topic 4: Minimal Market Context Feasibility (IG-014)
**Objective**: Define the “relative smallest viable” market context payload to support VPA Type 1/2 usage, aligned to current data realities.

#### A. Evidence & Forensics
*   **Source**: `prompt/roles/VPA/main_v2.1.md:1`
*   **Observation**: TTI protocol requires (per timeframe): price, VWAP values, RSI + RSI_MA, EMA9/21/50/200, SMA200.

*   **Source**: `components/tv_ingest/assets/pine/nmaq_exporter.pine:1`
*   **Observation**: Webhook provides those numeric inputs (plus OHLCV/vol MAs) but does not provide PA labels like MSB/CHOCH/BOS.

*   **Source (External)**: Binance USDS-M Futures REST API — Kline/Candlestick data
*   **Observation**: Binance provides a canonical OHLCV source keyed by `symbol`, `interval`, and **open time**; this is a natural choice for (a) backfilling historical candles, (b) reconciling timezone/close semantics, and (c) validating TradingView-derived candles when needed.

*   **Source (External)**: Binance Futures API — Funding rate history
*   **Observation**: Funding rate history provides time-indexed funding rates that can be joined to candle windows to improve “market regime” reasoning for perpetuals.

*   **Source (External)**: Binance Futures API — Open interest statistics
*   **Observation**: Open interest history provides time-indexed OI measures (e.g., aggregated open interest and value) for a symbol and period.

#### B. Evidence (Lean JSON Payload Example)
```json
{
  "schema_version":"tv_ingest_context/0.1.0",
  "symbol":"BINANCE:BTCUSDT",
  "as_of":"2025-12-23 22:00:00",
  "time_source":{"format":"YYYY-MM-DD HH:mm:ss","timezone":"Europe/Copenhagen","stored":"naive"},
  "timeframes":{
    "1D":{"tf_code":"D","close":87717.73,"ema":{"9":88184.416,"21":89175.272,"50":93339.197,"200":101835.455},"sma200":107773.374,"rsi":43.386,"rsi_ma14":43.227,"vwap":{"week":88438.885,"month":89474.378}},
    "4H":{"tf_code":"240","close":87717.73,"ema":{"9":88184.416,"21":89175.272,"50":93339.197,"200":101835.455},"sma200":107773.374,"rsi":43.386,"rsi_ma14":43.227,"vwap":{"week":88438.885,"month":89474.378}},
    "1H":{"tf_code":"60","close":87717.73,"ema":{"9":88184.416,"21":89175.272,"50":93339.197,"200":101835.455},"sma200":107773.374,"rsi":43.386,"rsi_ma14":43.227,"vwap":{"session":87753.21,"week":88438.885}},
    "15m":{"tf_code":"15","close":87717.73,"ema":{"9":88184.416,"21":89175.272},"rsi":43.386,"rsi_ma14":43.227,"vwap":{"session":87753.21}},
    "chart_tf_bars":{"tf_code":"15","bars":[{"time":"2025-12-23 21:00:00","open":88000,"high":88500,"low":87500,"close":87700,"volume":1000}]}
  }
}
```

#### C. Analysis
* Approximate size: ~1558 characters (~390 tokens at chars/4).
* “Smallest viable” because it satisfies the TTI numeric requirements without requiring delta columns or relying on VWAP filtering being reflected in stored artifacts.
* Encodes timezone/naive timestamp semantics explicitly to avoid implicit drift.
* External enrichment should be treated as a **separate, pull-based channel** (e.g., periodic fetch keyed to `symbol` + timeframe) rather than being added to the TradingView webhook contract; this keeps `IF-001` stable while enabling `IG-014` extensions.

#### D. Governance Implication
*   This payload provides a concrete candidate for `T801A-IG-014` that can be finalized independent of drift in stored CSVs.
*   If Phase 1 requires “market regime” variables not present in TradingView payloads (e.g., funding rate, open interest), Binance Futures provides canonical endpoints (`/fapi/v1/fundingRate`, open interest history) that should be added as a **separate ingestion channel** rather than overloading the TradingView webhook contract.

---

### Topic 5: Historical Data Input Format (IG-016)
**Objective**: Define the “multi-candle structure + export constraints” implied by current Pine + server behavior.

#### A. Evidence & Forensics
*   **Source**: `components/tv_ingest/assets/pine/nmaq_exporter.pine:1`
*   **Observation**: Pine emits up to `exportRows` candles (1–5) for the chart timeframe only, plus single rows for additional timeframes.

*   **Source**: `components/tv_ingest/backend/api/webhook_server.py:108`
*   **Observation**: Server accepts variable row counts; treats each row as an observation keyed by the `tf` column.

#### B. Analysis
**Current-State Historical Format Spec**
* **Record shape**: Each row = one candle snapshot for one timeframe.
* **Grouping**: Group by `(symbol, tf)`; `time` is the candle timestamp (string parsed to datetime).
* **History depth**:
  * Chart timeframe: up to 5 bars per alert (configurable).
  * Other timeframes: 1 bar per alert (latest only).
* **Constraint**: No schema version tag or “snapshot id”; dedup/order relies on time and timeframe.

**Feasible vs Requires Change Summary**:
*   **Feasible Now**: Trend score calculations, MA crossovers (since Pine provides the current values based on long TradingView history), and short-term momentum signals are supported by the current 5-bar (chart TF) and single-bar (other TFs) depth.
*   **Requires Change**: Complex Price Action (PA) pattern detection (e.g., Higher Highs/Lower Lows over many bars) or RSI divergences require either increasing Pine's `exportRows` (limited by TradingView's 40k character cap) or, more reliably, switching the backend to 'append mode' to accumulate history in the Symbol Master files over multiple alerts. 
*   **Recommendation**: Enable append mode with a defined `MAX_ROWS_PER_SYMBOL` to bridge this gap for Phase 1 without changing the webhook contract.

#### C. Governance Implication
*   `T801A-IG-016` can be finalized with “chart TF history, others snapshot” semantics as the current master behavior.

---

### Topic 6: Schema Evolution Governance (CON-001 / IF-001 stabilization)
**Objective**: Identify minimal governance controls to prevent drift regression and clarify contracts.

#### A. Evidence & Forensics
*   **Source**: `components/tv_ingest/backend/api/webhook_server.py:281`
*   **Observation**: `/config` endpoint exists and can toggle enhancement behavior and storage mode, but Streamlit UI “config” is not wired to call this endpoint (drift seam).

*   **Source**: `components/tv_ingest/backend/processors/webhook_processor.py:562`
*   **Observation**: Append-mode dedup rules exist, but global-master dedup currently ignores `symbol` (risk of cross-symbol row loss).

#### B. Analysis
**Minimal governance controls (Phase 1 appropriate)**
* `T801A-IF-001` should explicitly define base schema, timestamp semantics, `tf` code semantics, and multi-timeframe row composition.
* `T801A-IG-014` should standardize a minimal context object so LLM sessions remain stable independent of drift artifacts.
* `T801A-IG-016` should document current history depth constraints unless/until Pine export changes.

#### C. Governance Implication
*   Contract finalization should be based on Pine + server enforcement, with artifacts used only as drift signals and logged via Issues/Risks.

---

## IV. ISSUE & RISK REGISTER (T102-STD-007)

**Issues**
<!-- GUIDANCE:
Status = `OPEN, IN-REVIEW, RESOLVED, BLOCKED, DEFERRED`,
priority = `Low, Medium, High`
-->
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Resolution Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `T801A-ISSUE-001` | “19 vs 20 vs 44” schema confusion | Code comments/UI text reference 19 columns, but base schema is 20 columns and enhanced is 44; this blocks clean IF/IG writing. Evidence: `components/tv_ingest/utils/constant.py:1`, `components/tv_ingest/backend/api/webhook_server.py:112`, `components/tv_ingest/frontend_builder/fb_tv_ingest.py:1`. | LLM_Consultant | `OPEN` | High | 2026-01-04 | — |
| `T801A-ISSUE-002` | Row-count validation missing | `EXPECTED_ROWS_PER_ALERT` exists but is not enforced; webhook accepts arbitrary rows, undermining IG-016 clarity. Evidence: `components/tv_ingest/utils/constant.py:1`, `components/tv_ingest/backend/api/webhook_server.py:100`. | LLM_Developer | `OPEN` | Medium | 2026-01-04 | — |
| `T801A-ISSUE-003` | Config surface not coherently wired | `/config` API can toggle enhancements/storage mode, but Streamlit “Config” page toggles do not update the running server config; risk of operator misunderstanding. Evidence: `components/tv_ingest/backend/api/webhook_server.py:281`, `components/tv_ingest/frontend_builder/builders/config_builder.py:1`. | LLM_Developer | `OPEN` | Medium | 2026-01-04 | — |
| `T801A-ISSUE-004` | Global-master append dedup may drop cross-symbol rows | Append-mode dedup for “master files” uses `(time, tf)` only; in global master this can erase different symbols that share `(time, tf)`. Evidence: `components/tv_ingest/backend/processors/webhook_processor.py:500`. | LLM_Developer | `OPEN` | High | 2026-01-04 | — |
| `T801A-ISSUE-005` | Internal legacy seams inside tv_ingest | `create_app(...)` and `TvIngestService.ingest_webhook(...)` paths appear inconsistent with current DataFrame-based webhook processor; docs/tests reference deprecated structures. Evidence: `components/tv_ingest/backend/api/webhook_server.py:465`, `components/tv_ingest/service/svc_tv_ingest.py:33`, `components/tv_ingest/tests/test_service.py:1`, `documentation/tv_ingest/main.md:1`. | LLM_Developer | `OPEN` | Medium | 2026-01-04 | — |
| `T801A-ISSUE-006` | 5xx on validation triggers TradingView resend loop | Current webhook server returns 500 for column-count mismatches and many parse errors; TradingView resends on 5xx up to 3 times, which can create duplicate rows and confound dedup logic. Evidence: `components/tv_ingest/backend/api/webhook_server.py:121` + TradingView “Webhook resubmission” policy. | LLM_Developer | `OPEN` | High | 2026-01-04 | — |
| `T801A-ISSUE-007` | Pine exporter timezone formatting likely incorrect | TradingView docs state `str.format()` always formats times in UTC+0 and recommend `str.format_time()` for timezone-specific strings. Exporter uses `str.format("{0,time,...}", ...)` with a user “timezone” option, risking silently wrong `time` strings. Evidence: `components/tv_ingest/assets/pine/nmaq_exporter.pine:1` + TradingView “Concepts / Time”. | LLM_Developer | `OPEN` | High | 2026-01-04 | — |
| `T801A-ISSUE-008` | Multi-timeframe timestamp semantics unclear | In `f_row()`, exporter builds `timeStr` using `tLocal = time(timeframe.period, timeZoneOpt)` (chart tf) rather than the requested `_tf`; timestamps for extra timeframes may be mis-keyed. Evidence: `components/tv_ingest/assets/pine/nmaq_exporter.pine:1`. | LLM_Developer | `OPEN` | High | 2026-01-04 | — |

**Risks**
<!-- GUIDANCE:
Status = `OPEN, MONITORED, MITIGATED, ACCEPTED, CLOSED`,
priority = `Low, Medium, High`
-->
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Mitigation Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `T801A-RISK-001` | Unauthenticated public webhook | ngrok exposes a write-capable endpoint without auth/secret validation; risk of spam writes or accidental exposure. Evidence: `components/tv_ingest/backend/infrastructure/ngrok_manager.py:1`, `components/tv_ingest/backend/api/webhook_server.py:100`. | Client | `OPEN` | High | 2026-01-04 | — |
| `T801A-RISK-002` | Timestamp timezone ambiguity | Pine can emit in UTC or local TZ, but storage is naive; changing timezone can break dedup/history interpretation and LLM context reasoning. Evidence: `components/tv_ingest/assets/pine/nmaq_exporter.pine:1`, `components/tv_ingest/backend/processors/webhook_processor.py:652`. | LLM_Consultant | `OPEN` | High | 2026-01-04 | — |
| `T801A-RISK-003` | “Override” storage mode may erase history | WebhookServer default `data_storage_mode="override"` can overwrite prior history; conflicts with IG-016 expectations unless explicitly documented. Evidence: `components/tv_ingest/backend/api/webhook_server.py:52`. | Client | `OPEN` | Medium | 2026-01-04 | — |
| `T801A-RISK-004` | VWAP filtering correctness depends on tf codes | If `tf` ever becomes display-form (e.g., `1H`), VWAPFilter won’t map to minutes and will fail-open (keep all VWAPs). Evidence: `components/tv_ingest/backend/processors/filterings/vwap_filter.py:1`, `components/tv_ingest/utils/constant.py:1`. | LLM_Developer | `OPEN` | Medium | 2026-01-04 | — |
| `T801A-RISK-005` | At-least-once delivery can create duplicates or loss | TradingView resends webhooks on 5xx (max 4 deliveries/trigger). With current 500 responses and imperfect dedup (especially global master), the system can either duplicate rows or drop rows during dedup/overwrite. Evidence: `components/tv_ingest/backend/api/webhook_server.py:121`, `components/tv_ingest/backend/processors/webhook_processor.py:500` + TradingView “Webhook resubmission”. | Client | `OPEN` | High | 2026-01-04 | — |
| `T801A-RISK-006` | 3-second webhook cancellation risk | TradingView cancels webhook requests if receiver processing exceeds ~3 seconds; pandas parsing + enrichment + disk writes could exceed this in worst-case conditions, leading to silent data loss. Evidence: TradingView “How to configure webhook alerts” + current synchronous pipeline in `webhook_server.py`. | Client | `OPEN` | Medium | 2026-01-04 | — |
| `T801A-RISK-007` | Alert/webhook message body size limit constrains export design | Pine `alert()` message bodies are capped at 40960 characters; expanding export rows/timeframes can exceed the cap and cause failed webhook deliveries or truncation, undermining IG-016 assumptions. Evidence: TradingView “Alert name and message size limits” + `exportRows`/multi-TF design in `nmaq_exporter.pine`. | LLM_Consultant | `OPEN` | Medium | 2026-01-04 | — |
| `T801A-RISK-008` | Repainting/confirmation drift for `request.security()` rows | TradingView notes `barstate.isconfirmed` does not consider `request.security()` calls; multi-timeframe rows can change after initial alert delivery unless explicitly non-repainting. Evidence: TradingView “Bar states” + exporter’s multi-TF design. | LLM_Consultant | `OPEN` | Medium | 2026-01-04 | — |

---

## V. ARTIFACT UPDATES

| Artifact ID | Section | Action Required | Content Source |
| :--- | :--- | :--- | :--- |
| `T801A-ADR-001` | Pipeline mapping | Paste mermaid pipeline + artifact inventory | Topic 1 |
| `T801A-IF-001` | Webhook contract | Finalize Base (20-col) schema + delimiter rules + multi-timeframe row semantics + failure behaviors | Topic 2 |
| `T801A-IG-014` | Context content | Adopt “smallest viable” JSON context spec and explicitly note missing PA labels | Topic 4 |
| `T801A-IG-016` | Historical data format | Document “chart TF provides up to 5 bars; others are snapshot rows” and its implications | Topic 5 |
| `T801A-ADR-004` | Context/schema scope | Reconcile “intended 44-col enhanced storage” vs observed drift; set governance stance (code-as-master) | Topic 3 + Topic 4 |

---

## VI. SOURCE MATERIAL
*   **Brief Version**: `prompt/artifacts/tasks/T801/research/brief/brief_T801A-RES-002_system-architecture-research.md:1`
*   **Code Commit/Tag**: `6d8feb9`
*   **Files Cited**:
    *   `components/tv_ingest/backend/api/webhook_server.py:100`
    *   `components/tv_ingest/backend/processors/webhook_processor.py:109`
    *   `components/tv_ingest/utils/constant.py:1`
    *   `components/tv_ingest/assets/pine/nmaq_exporter.pine:1`
    *   `components/tv_ingest/backend/processors/filterings/vwap_filter.py:1`
    *   `components/tv_ingest/backend/processors/calculations/delta_calculator.py:1`
    *   `prompt/roles/VPA/main_v2.1.md:1`
    *   `prompt/roles/VPA/example.md:1`
    *   `components/tv_ingest/data/global_master.csv:1`
    *   `components/tv_ingest/data/BINANCE_BTCUSDT/master.csv:1`
*   **External References (2026-01-04 snapshot)**:
    *   TradingView — How to configure webhook alerts: https://www.tradingview.com/support/solutions/43000529348-how-to-configure-webhook-alerts/
    *   TradingView — Webhook resubmission: https://www.tradingview.com/support/solutions/43000735201-webhook-resubmission/
    *   TradingView — Alert name and message size limits: https://www.tradingview.com/support/solutions/43000773947/
    *   TradingView — Webhook authentication: https://www.tradingview.com/support/solutions/43000680459-webhook-authentication/
    *   TradingView Pine — Concepts / Alerts: https://www.tradingview.com/pine-script-docs/v5/concepts/alerts/
    *   TradingView Pine — Concepts / Time: https://www.tradingview.com/pine-script-docs/v5/concepts/time/
    *   TradingView Pine — Bar states (v3): https://www.tradingview.com/pine-script-docs/v3/essential/barstate/
    *   Binance Futures API — Funding rate history: https://binance-docs.github.io/apidocs/futures/en/#get-funding-rate-history
    *   Binance Futures API — Open interest statistics: https://binance-docs.github.io/apidocs/futures/en/#open-interest-statistics
    *   Binance USDS-M Futures REST API — Kline/Candlestick data: https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Kline-Candlestick-Data
