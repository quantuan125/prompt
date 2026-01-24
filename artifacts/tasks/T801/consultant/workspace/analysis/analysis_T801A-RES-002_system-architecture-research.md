---
artifact_type: 'ANALYSIS'
initiative_id: 'T801'
epic_id: 'T801A'
epic_code: 'TTI'
subphase: '1.3.1'
version: '1.0.0'
date: '2026-01-05'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
purpose: 'Integration analysis of T801A-RES-002 findings to finalize partial E-RIDs and update Phase 1 governance artifacts'
research_source: 'prompt/artifacts/tasks/T801/research/report/report_T801A-RES-002_system-architecture-research.md'
---

# INTEGRATION ANALYSIS: T801A-RES-002 System Architecture Research

## I. EXECUTIVE SUMMARY

**Purpose**
Analyze T801A-RES-002 (System Architecture Research) findings to:
1. Finalize partial E-RIDs (IF-001, IG-014, IG-016)
2. Complete partial E-ADRs (ADR-001, ADR-004)
3. Integrate new Issues & Risks into proposal Section VI
4. Assess whether existing E-RIDs/E-DRs require modification or expansion

**Research Verdict (from T801A-RES-002)**
- **GO**: Finalize IF-001 for Base 20-column webhook contract
- **NO-GO**: Enhanced 44-column contract (not emitted by Pine today)
- **RESOLVED**: IG-014 (minimal market context spec provided)
- **RESOLVED**: IG-016 (historical format clarified)
- **COMPLETE**: ADR-001 (pipeline mapping with Mermaid diagram)
- **COMPLETE**: ADR-004 (context scope confirmed)

**Key Integration Findings**
1. **TradingView Platform Constraints**: New operational constraints discovered (3s timeout, 40k char cap, 5xx resend behavior) — requires ASSUM-004 review
2. **Schema Drift Clarification**: On-disk artifacts are drift signals, NOT authoritative specs — governance by code-as-master
3. **Lean JSON Context Spec**: ~1558 chars (~390 tokens) minimal context satisfies QG-007
4. **Historical Data Format**: 5 bars chart TF + 1 bar other TFs per alert
5. **Issues/Risks Register**: 8 new Issues + 8 new Risks identified for Activity 1.3.3

**Decision Ownership**: All governance updates derived from this analysis require Client approval.

---

## II. RAW RESEARCH FINDINGS (EXTRACTED FROM T801A-RES-002)

### A. Topic 1: Pipeline Map (Current State)

**Extracted Evidence**:
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

**Artifact Inventory (from research)**:
| Artifact | Path | Producer | Consumer | Format | Notes |
|---|---|---|---|---|---|
| Webhook ingress | `POST /` | TradingView alert | FastAPI server | text/plain-ish | Headerless, semicolon-separated rows |
| Symbol timeframe file | `components/tv_ingest/data/<SYMBOL_DIR>/<TF_DISPLAY>.csv` | `WebhookProcessor` | Streamlit UI/export | CSV | Column order normalized on save |
| Symbol master | `components/tv_ingest/data/<SYMBOL_DIR>/master.csv` | `WebhookProcessor` | Streamlit UI/export | CSV | Multi-timeframe aggregate |
| Global master | `components/tv_ingest/data/global_master.csv` | `WebhookProcessor` | Streamlit UI/export | CSV | Multi-symbol + multi-timeframe aggregate |
| LLM context (text) | Export UI | Human | LLM | Text | Current export is "dataframe dump" |

**Human Workflow Handoff Points**:
1. Copy ngrok HTTPS URL into TradingView alert webhook settings (manual)
2. After data arrives, user exports context (manual) and pastes/attaches to LLM_Trader chat (manual)
3. Optional manual overrides are "human-only" step; no enforced schema/versioning on exported context

---

### B. Topic 2: Webhook Contract (IF-001)

**Base Contract (20-column) — Canonical Today**:
| # | Field | Type | Example | Notes |
|---:|---|---|---|---|
| 1 | `symbol` | string | `BINANCE:BTCUSDT` | From `syminfo.tickerid` |
| 2 | `time` | datetime string | `2025-12-23 22:00:00` | Pine formats with chosen timezone |
| 3-6 | `open,high,low,close` | float | `88620.79` | |
| 7 | `volume` | float | `12804.02886` | |
| 8-9 | `vol_ma20,vol_ma30` | float | `15679.57` | |
| 10-13 | `ema9,ema21,ema50,ema200` | float | `88184.41` | |
| 14 | `sma200` | float | `107773.37` | |
| 15-16 | `rsi,rsi_ma14` | float | `43.3861` | |
| 17-19 | `vwap_session,vwap_week,vwap_month` | float | `87753.21` | Backend may mask irrelevant VWAPs |
| 20 | `tf` | string code | `60`, `D`, `W` | Raw timeframe code |

**Delimiter Rules**:
- Rows separated by newline `\n`
- Columns separated by semicolon `;`
- No header row
- No quoting/escaping rules explicitly enforced

**Multi-Timeframe Behavior**:
- Pine emits **N rows (1-5)** for chart timeframe (`exportRows`, default 5)
- Pine appends **1 row per additional timeframe** (not 5 rows each)

**TradingView Webhook Delivery Constraints (NEW — External)**:
| Constraint | Value | Impact |
|:-----------|:------|:-------|
| Port restrictions | Only 80/443 | ngrok already handles |
| Processing timeout | ~3 seconds | Backend must respond fast |
| Resend on 5xx | Up to 3 retries (max 4 deliveries) | Creates duplicates |
| Message size cap | 40,960 characters | Limits exportable rows |
| IPv6 | Not supported | N/A for current setup |
| Content-Type | `application/json` if valid JSON, else `text/plain` | Current is text/plain |

**Enhanced Contract (44-column) — NOT Emitted by Pine**:
- Server accepts 44 columns if payload count equals 44
- Current `nmaq_exporter.pine` emits 20-column base schema only
- Artifacts show no delta columns on disk
- Treat 44-column as "latent/optional", NOT canonical

**Current Failure/Validation Behaviors**:
- Column count mismatch → `ValueError` → HTTP 500
- Numeric parsing failures → HTTP 500
- Invalid timeframe → warns, may skip storage (not hard failure)
- Row count NOT validated despite `EXPECTED_ROWS_PER_ALERT` existing

---

### C. Topic 3: Storage Schema & Drift

**Intended Schema (Code-As-Master)**:
- `BASE_COLUMNS=20`, `DELTA_COLUMNS=24`, `CSV_COLUMNS=44`
- VWAP relevance rules exist via `VWAP_RELEVANCE` and `TF_TO_MINUTES`
- Backend designed to mask irrelevant VWAPs and compute delta columns

**Observed Drift (Artifacts on Disk)**:
- `global_master.csv` has **20 columns only** (no deltas)
- Per-symbol `master.csv` has **20 columns only**
- Weekly timeframe shows `vwap_session` and `vwap_week` even though backend rules would mask them

**Drift Classification**: "Historical artifact writer drift" (high confidence)
- Artifacts predate or bypass delta calculations and VWAP filtering
- Governance artifacts must treat on-disk CSVs as **non-authoritative**

---

### D. Topic 4: Minimal Market Context (IG-014)

**Lean JSON Payload Specification (from research)**:
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

**Size Analysis**:
- Approximate size: ~1558 characters (~390 tokens at chars/4)
- Satisfies QG-007 (Context Sufficiency) without delta columns or VWAP filtering
- Encodes timezone/naive timestamp semantics explicitly

---

### E. Topic 5: Historical Data Format (IG-016)

**Current-State Historical Format**:
- **Record shape**: Each row = one candle snapshot for one timeframe
- **Grouping**: Group by `(symbol, tf)`; `time` is candle timestamp
- **History depth**:
  - Chart timeframe: up to 5 bars per alert (configurable)
  - Other timeframes: 1 bar per alert (latest only)
- **Constraint**: No schema version tag or "snapshot id"

**Feasibility Assessment**:
| Calculation | Supported Now? | Notes |
|:------------|:---------------|:------|
| Trend scores | ✅ Yes | Pine provides current indicator values |
| MA crossovers | ✅ Yes | Pine has long history |
| Short momentum | ✅ Yes | 5 bars sufficient |
| Complex PA (HH/HL series) | ⚠️ Limited | May need append mode or increased `exportRows` |
| RSI divergences | ⚠️ Limited | Deferred per CON-004 anyway |

**Recommendation**: Enable append mode with defined `MAX_ROWS_PER_SYMBOL` to bridge gap for Phase 1.

---

### F. Topic 6: Schema Evolution Governance

**Minimal Governance Controls (MVP Appropriate)**:
- IF-001: Define base schema + timestamp semantics + `tf` code semantics
- IG-014: Standardize minimal context object (now resolved)
- IG-016: Document current history depth constraints

**Config Surface Gap**:
- `/config` API exists but Streamlit UI toggles don't update running server
- Risk of operator misunderstanding

---

### G. Issues & Risks Register (RAW from T801A-RES-002)

#### Issues (8 items)
| ID | Title | Description | Owner | Status | Priority |
|:---|:------|:------------|:------|:-------|:---------|
| `T801A-ISSUE-001` | "19 vs 20 vs 44" schema confusion | Code comments/UI text reference 19 columns, but base schema is 20 columns and enhanced is 44 | LLM_Consultant | OPEN | High |
| `T801A-ISSUE-002` | Row-count validation missing | `EXPECTED_ROWS_PER_ALERT` exists but not enforced | LLM_Developer | OPEN | Medium |
| `T801A-ISSUE-003` | Config surface not coherently wired | `/config` API toggles don't update running server | LLM_Developer | OPEN | Medium |
| `T801A-ISSUE-004` | Global-master append dedup may drop cross-symbol rows | Dedup uses `(time, tf)` only; can erase different symbols | LLM_Developer | OPEN | High |
| `T801A-ISSUE-005` | Internal legacy seams inside tv_ingest | Multiple code paths appear inconsistent; docs/tests reference deprecated structures | LLM_Developer | OPEN | Medium |
| `T801A-ISSUE-006` | 5xx on validation triggers TradingView resend loop | Returns 500 for column-count mismatches; causes up to 4 deliveries | LLM_Developer | OPEN | High |
| `T801A-ISSUE-007` | Pine exporter timezone formatting likely incorrect | `str.format()` always formats in UTC+0; may produce wrong timestamps | LLM_Developer | OPEN | High |
| `T801A-ISSUE-008` | Multi-timeframe timestamp semantics unclear | Exporter builds `timeStr` using chart TF time, not requested TF | LLM_Developer | OPEN | High |

#### Risks (8 items)
| ID | Title | Description | Owner | Status | Priority |
|:---|:------|:------------|:------|:-------|:---------|
| `T801A-RISK-001` | Unauthenticated public webhook | ngrok exposes write-capable endpoint without auth | Client | OPEN | High |
| `T801A-RISK-002` | Timestamp timezone ambiguity | Pine can emit UTC or local TZ; storage is naive; breaks dedup/history | LLM_Consultant | OPEN | High |
| `T801A-RISK-003` | "Override" storage mode may erase history | Default `data_storage_mode="override"` can overwrite prior history | Client | OPEN | Medium |
| `T801A-RISK-004` | VWAP filtering correctness depends on tf codes | If `tf` becomes display-form, VWAPFilter fails-open | LLM_Developer | OPEN | Medium |
| `T801A-RISK-005` | At-least-once delivery creates duplicates or loss | TradingView resends on 5xx; imperfect dedup can duplicate or drop rows | Client | OPEN | High |
| `T801A-RISK-006` | 3-second webhook cancellation risk | TradingView cancels if processing exceeds ~3s; synchronous pipeline may exceed | Client | OPEN | Medium |
| `T801A-RISK-007` | Alert/webhook message body size limit constrains export | 40960 char cap limits feasible `(exportRows × tf_count)` | LLM_Consultant | OPEN | Medium |
| `T801A-RISK-008` | Repainting/confirmation drift for `request.security()` rows | Multi-TF rows can change after initial alert delivery | LLM_Consultant | OPEN | Medium |

---

## III. CONSULTANT SYNTHESIS — IMPACT ON E-RIDs

### A. Sufficiency Assessment (Client Q1)

**Question**: Are current E-RIDs + E-DRs sufficient, or do we need additional items?

**Assessment**: Current inventory is **sufficient with targeted updates**. No new E-RID categories or major E-DRs required. Key updates:

| Current Item | Sufficiency | Update Required |
|:-------------|:------------|:----------------|
| **IF-001** | ⚠️ Partial | ✅ Finalize with Base 20-column spec + TradingView constraints |
| **IF-002** | ✅ Sufficient | Minor — add lean JSON reference from research |
| **IF-003** | ✅ Sufficient | No change |
| **IG-014** | ⚠️ Partial | ✅ Finalize with lean JSON spec from research |
| **IG-016** | ✅ Sufficient | ✅ Update with "5 bars chart TF, 1 bar others" semantics |
| **ADR-001** | ⚠️ Partial | ✅ Finalize with pipeline diagram + artifact inventory |
| **ADR-004** | ⚠️ Partial | ✅ Finalize with lean JSON schema scope |
| **ASSUM-004** | ⚠️ Review | See Section III.B below |

**New Items Discovered**: None required at E-RID level. Research findings integrate into existing items.

---

### B. ASSUM-004 Elevation Assessment (Client Q2)

**Question**: Should ASSUM-004 (External Platform Sufficiency) be elevated to CON given TradingView constraints?

**Research Findings on TradingView Constraints**:
1. **3-second timeout**: TradingView cancels if receiver takes >3s
2. **40,960 char cap**: Pine `alert()` messages capped
3. **5xx resend**: Up to 3 retries (4 total deliveries)
4. **Timezone formatting bug**: `str.format()` always UTC+0

**Assessment**: The TradingView constraints are **platform operational realities**, not **design decisions we are making**. Per `T102-ADR-005-FR-004`:
- **CON (Constraint)**: "Non-negotiable boundary or limitation that must be respected"
- **ASSUM (Assumption)**: "Something believed true but requiring validation"

**Recommendation**: **Maintain ASSUM-004** with the following rationale:
1. TradingView constraints are **external environmental facts** we cannot negotiate or change
2. The ASSUMPTION is whether these constraints are **sufficient for our use case** — this remains validatable
3. If constraints prove insufficient during T801A2 development, ASSUM-004 is **invalidated** and we trigger the fallback strategy
4. Elevating to CON would be semantically incorrect — we're not choosing to impose these limits; they exist

**Proposed ASSUM-004 Update**:
- Add explicit documentation of TradingView operational constraints (3s timeout, 40k cap, 5xx resend, timezone behavior)
- Update validation criteria: "Constraints accommodate expected trading session frequency and payload sizes"
- Add fallback strategy: "If constraints prove insufficient, evaluate Pine export optimizations or alternative ingestion approaches"

---

### C. E-RID/E-DR Modification Assessment (Client Q2)

**Question**: Apart from PARTIAL items, do current E-RIDs/E-DRs need changes or modifications?

| Item | Category | Change Type | Description |
|:-----|:---------|:------------|:------------|
| **ASSUM-004** | ASSUM | **UPDATE** | Add TradingView constraint documentation + validation criteria |
| **DEP-002** | DEP | No change | tv_ingest behavioral contract stable |
| **DEP-004** | DEP | **CLARIFY** | Research confirms 5-bar chart TF limit; add specific depth note |
| **QG-006** | QG | **VALIDATE** | 3s TradingView timeout informs <1min target; remains achievable |
| **IG-015** | IG | **UPDATE** | Add HTTP response code guidance (avoid 5xx for validation errors) |
| **GDR-001** | GDR | No change | Hybrid architecture validated by pipeline map |
| **GDR-004** | GDR | No change | JSON format confirmed |
| **ADR-002** | ADR | No change | Scoring algorithm not affected by research |

**Summary**: 4 items require updates (ASSUM-004, DEP-004, IG-015, + partial items). No items require complete replacement.

---

### D. Issues/Risks Integration Plan (Per Client Answer 3)

**Approach**: Import all 16 items (8 Issues + 8 Risks) to proposal Section VI with priority on HIGH items. Update Activity 1.3.3 in plan file with specific resolution tasks.

**HIGH Priority Items (Immediate Focus)**:
| ID | Title | Resolution Approach |
|:---|:------|:--------------------|
| ISSUE-001 | Schema confusion (19/20/44) | Document canonical 20-column in IF-001; update code comments in Feature T801A1 |
| ISSUE-004 | Global-master dedup data loss | Log for Feature T801A1 fix; add dedup key `(symbol, time, tf)` |
| ISSUE-006 | 5xx triggers resend loop | Add IG-015 guidance: return 4xx for client validation errors |
| ISSUE-007 | Pine timezone bug | Log for Feature T801A2 fix; document as known limitation until fixed |
| ISSUE-008 | Multi-TF timestamp semantics | Log for Feature T801A2 fix; pairs with ISSUE-007 |
| RISK-001 | Unauthenticated webhook | Log as accepted operational risk; auth deferred post-MVP per QG-008 |
| RISK-002 | Timestamp timezone ambiguity | Pairs with ISSUE-007/008; document UTC-only assumption until resolved |
| RISK-005 | At-least-once delivery | Add IG-015 guidance on idempotent processing; log for Feature T801A1 |

---

## IV. E-RID FINALIZATION SPECIFICATIONS

### A. IF-001 Finalization (TradingView Webhook Input Contract)

**Current Status**: ⚠️ Partial (pending T801A-RES-002)

**Finalization Content**:

```markdown
* **T801A-IF-001 (TradingView Webhook Input Contract)** — Webhook payload interface from TradingView PineScript exporter (`nmaq_exporter.pine`) to tv_ingest backend.

  **Contract Type**: Base (20-column) — canonical per T801A-RES-002.

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
  - Timestamp timezone: `str.format()` always UTC+0 (see ISSUE-007)

  **Validation Behavior**:
  - Column count mismatch → validation error (per IG-015, return 4xx not 5xx)
  - Malformed/missing data → best-effort processing + error flags per IG-015
  - Backend validates before scoring; does not validate row count

  **Schema Versioning**: Deferred to Feature T801A1/T801A2 coordination. Current contract unversioned.

  Cross-reference: `DEP-001`, `IG-007`, `IG-015`, `ISSUE-001`, `ISSUE-006`, `ISSUE-007`, `ISSUE-008`
```

---

### B. IG-014 Finalization (Context Content)

**Current Status**: ⚠️ Partial (pending T801A-RES-002)

**Finalization Content**:

```markdown
* **T801A-IG-014 (Context Content)** — Guidance on "minimal market context" content for TTI JSON artifact per `T801A-QG-007 (Context Sufficiency)` Option B selection.

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
  - Satisfies QG-007 without exceeding IG-010 context budget

  **Exclusions from Minimal Context**:
  - Delta columns (not emitted by current Pine)
  - VWAP values masked by backend filtering (include only applicable per matrix)
  - Historical bars for non-chart timeframes

  Cross-reference: `IF-002`, `QG-007`, `IG-010`, `T801A-RES-002 Topic 4`
```

---

### C. IG-016 Update (Historical Data Input Format)

**Current Status**: Confirmed (update with research specifics)

**Update Content**:

```markdown
* **T801A-IG-016 (Historical Data Input Format)** — Guidance on multi-candle historical data format for backend TTI engine per `T801A-DEP-004 (Expanded Data Structure)`.

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
  | RSI divergences | ⚠️ Limited | Deferred per CON-004 |

  **Recommendation**:
  - For MVP: Accept 5-bar chart TF + 1-bar other TFs as sufficient for trend scoring
  - For enhanced PA detection: Enable append mode with `MAX_ROWS_PER_SYMBOL` limit
  - Feature T801A2 determines Pine export capabilities; Feature T801A1 consumes

  **Timestamp Caveat**: Per ISSUE-007/ISSUE-008, timestamps may be formatted incorrectly or use chart TF time for all rows. Document as known limitation.

  Cross-reference: `DEP-004`, `IF-001`, `ISSUE-007`, `ISSUE-008`, `T801A-RES-002 Topic 5`
```

---

## V. E-ADR FINALIZATION SPECIFICATIONS

### A. ADR-001 Finalization (Hybrid Integration Pattern)

**Current Status**: ⚠️ Partial (pipeline mapping pending)

**Specification Update**:

Add to ADR-001 Specification section:

```markdown
**T801A-ADR-001-FR-003 (Pipeline Mapping)**:

The hybrid integration pattern follows this pipeline architecture per T801A-RES-002:

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
  TTI --> JSON[TTI JSON Artifact<br/>per IF-002]
  JSON --> HUMAN[Manual handoff<br/>per CON-003]
  HUMAN --> LLM[LLM_Trader<br/>per IF-003]
```

**Artifact Inventory**:
| Stage | Artifact | Format | Owner |
|:------|:---------|:-------|:------|
| Ingress | Webhook payload | text/plain (semicolon-separated) | T801A2 (PineScript) |
| Storage | CSV files | CSV | tv_ingest backend |
| Output | TTI JSON | JSON per IF-002 | T801A1 (Backend) |
| Handoff | Manual copy | JSON artifact | Human (CON-003) |

**Human Workflow Handoff Points**:
1. Configure ngrok URL in TradingView (manual)
2. Export/copy TTI JSON after generation (manual)
3. Attach to LLM_Trader session (manual)
```

---

### B. ADR-004 Finalization (TTI File Schema)

**Current Status**: ⚠️ Partial (context scope pending)

**Specification Update**:

Add to ADR-004 Specification section:

```markdown
**T801A-ADR-004-FR-004 (Minimal Market Context Scope)**:

Per T801A-RES-002 Topic 4, the TTI JSON schema includes minimal market context satisfying QG-007:

**Context Fields (per timeframe)**:
- `tf_code`: Raw timeframe code
- `close`: Current close price
- `ema`: Object with EMA values (9, 21, 50, 200)
- `sma200`: SMA 200 value (where applicable)
- `rsi`, `rsi_ma14`: RSI values
- `vwap`: Object with applicable VWAP values per timeframe matrix

**Optional Historical Context** (chart timeframe only):
- `chart_tf_bars`: Array of up to 5 recent bars with OHLCV

**Size Target**: ~1500-2000 characters (~375-500 tokens) per artifact

**Schema Versioning**:
- `schema_version` field required in every artifact
- Version format: `tv_ingest_context/<semver>` (e.g., `tv_ingest_context/0.1.0`)
- Backward compatibility: New fields optional; deprecated fields retained 2 major versions
```

---

## VI. ACTIVITY 1.3.3 UPDATE SPECIFICATION

Per Client direction, update plan file Activity 1.3.3 with specific resolution tasks:

### Activity 1.3.3: Risk & Open Issue Assessment (UPDATED)

```markdown
#### Activity 1.3.3: Risk & Open Issue Assessment

**Purpose**: Consolidate and assess all Issues & Risks from T801A-RES-002, prioritize resolution approaches, and integrate into proposal Section VI.

##### Task 1.3.3.1: Import Issues/Risks Register

**Action**: Populate proposal Section VI with all 16 items from T801A-RES-002:
- 8 Issues (ISSUE-001 to ISSUE-008)
- 8 Risks (RISK-001 to RISK-008)

**Format**: Per T102-ADR-007 schema.

##### Task 1.3.3.2: HIGH Priority Resolution Planning

**ISSUE-001 (Schema Confusion)**:
- Resolution: Document canonical 20-column in finalized IF-001
- Owner: LLM_Consultant (Phase 1); LLM_Developer (Feature T801A1 code comments)
- Status: IN-REVIEW

**ISSUE-004 (Global-master Dedup Data Loss)**:
- Resolution: Log for Feature T801A1; add `symbol` to dedup key
- Owner: LLM_Developer
- Status: OPEN (deferred to Feature)

**ISSUE-006 (5xx Triggers Resend Loop)**:
- Resolution: Add IG-015 guidance for 4xx on validation errors
- Owner: LLM_Consultant (IG-015 update); LLM_Developer (implementation)
- Status: IN-REVIEW

**ISSUE-007 (Pine Timezone Bug)**:
- Resolution: Document as known limitation; log for Feature T801A2 fix
- Owner: LLM_Developer
- Status: OPEN (deferred to Feature)

**ISSUE-008 (Multi-TF Timestamp Semantics)**:
- Resolution: Pairs with ISSUE-007; log for Feature T801A2
- Owner: LLM_Developer
- Status: OPEN (deferred to Feature)

**RISK-001 (Unauthenticated Webhook)**:
- Resolution: Accept as operational risk per QG-008 (MVP Simplicity); auth deferred post-MVP
- Owner: Client
- Status: ACCEPTED

**RISK-002 (Timestamp Timezone Ambiguity)**:
- Resolution: Pairs with ISSUE-007/008; document UTC-only assumption until resolved
- Owner: LLM_Consultant
- Status: OPEN (mitigated by documentation)

**RISK-005 (At-least-once Delivery Duplicates/Loss)**:
- Resolution: Add IG-015 guidance on idempotent processing; log for Feature T801A1
- Owner: LLM_Developer
- Status: OPEN (deferred to Feature)

##### Task 1.3.3.3: MEDIUM Priority Review

**ISSUE-002 (Row-count Validation Missing)**:
- Resolution: Log for Feature T801A1 validation enhancement
- Owner: LLM_Developer
- Status: DEFERRED

**ISSUE-003 (Config Surface Not Wired)**:
- Resolution: Log for Feature T801A1 cleanup
- Owner: LLM_Developer
- Status: DEFERRED

**ISSUE-005 (Legacy Seams in tv_ingest)**:
- Resolution: Log for Feature T801A1 cleanup
- Owner: LLM_Developer
- Status: DEFERRED

**RISK-003 (Override Storage Mode History Erasure)**:
- Resolution: Document in IG-016; recommend append mode for Phase 1
- Owner: Client
- Status: MONITORED

**RISK-004 (VWAP Filtering tf Code Dependency)**:
- Resolution: Validate tf codes in IF-001 finalization
- Owner: LLM_Developer
- Status: MONITORED

**RISK-006 (3-Second Cancellation Risk)**:
- Resolution: Note in ASSUM-004; monitor during T801A1 testing
- Owner: Client
- Status: MONITORED

**RISK-007 (Message Body Size Limit)**:
- Resolution: Note in IF-001; validate exportRows × tf_count in T801A2
- Owner: LLM_Consultant
- Status: MONITORED

**RISK-008 (Repainting/Confirmation Drift)**:
- Resolution: Note in IF-001 multi-TF semantics; document limitation
- Owner: LLM_Consultant
- Status: MONITORED

##### Task 1.3.3.4: Cross-Category Consistency Check

**Action**: Validate that Issue/Risk resolutions don't conflict with confirmed E-RIDs:
- IF-001 finalization addresses ISSUE-001, ISSUE-006, RISK-007
- IG-015 update addresses ISSUE-006, RISK-005
- IG-016 update addresses RISK-003
- ASSUM-004 update addresses RISK-006
```

---

## VII. IMPLEMENTATION PLAN

### A. Proposal File Updates (v1.9.0)

| Section | Update | Priority |
|:--------|:-------|:---------|
| **II.E (IF Index)** | Update IF-001 status from "Partial" to "Confirmed" | High |
| **II.F (IG Index)** | Update IG-014 status from "Partial" to "Confirmed" | High |
| **III.E (IF Bodies)** | Replace IF-001 body with finalization content | High |
| **III.F (IG Bodies)** | Replace IG-014 body with finalization content | High |
| **III.F (IG Bodies)** | Update IG-016 body with research specifics | High |
| **III.F (IG Bodies)** | Update IG-015 body with HTTP response guidance | Medium |
| **III.A (ASSUM Bodies)** | Update ASSUM-004 with TradingView constraints | Medium |
| **III.D (DEP Bodies)** | Update DEP-004 with specific depth note | Low |
| **IV.D (ADR Bodies)** | Add ADR-001-FR-003 (Pipeline Mapping) | High |
| **IV.D (ADR Bodies)** | Add ADR-004-FR-004 (Context Scope) | High |
| **VI (Issues/Risks)** | Import all 16 items from T801A-RES-002 | High |
| **V.H (Dialogue Notes)** | Add Activity 1.3.1/1.3.3 dialogue notes | Medium |
| **VIII (Changelog)** | Document v1.9.0 changes | Required |

### B. Plan File Updates (v1.17.0)

| Section | Update | Priority |
|:--------|:-------|:---------|
| **Activity 1.3.1** | Mark as ✅ Complete | High |
| **Activity 1.3.3** | Add detailed task breakdown (Tasks 1.3.3.1-1.3.3.4) | High |
| **Changelog** | Document v1.17.0 changes | Required |

### C. Execution Sequence

1. **Step 1**: Finalize IF-001 body in proposal Section III.E
2. **Step 2**: Finalize IG-014 body in proposal Section III.F
3. **Step 3**: Update IG-016 body in proposal Section III.F
4. **Step 4**: Update IG-015 body with HTTP response guidance
5. **Step 5**: Update ASSUM-004 body with TradingView constraints
6. **Step 6**: Update DEP-004 body with depth clarification
7. **Step 7**: Add ADR-001-FR-003 to proposal Section IV.D
8. **Step 8**: Add ADR-004-FR-004 to proposal Section IV.D
9. **Step 9**: Import Issues/Risks to proposal Section VI
10. **Step 10**: Add dialogue notes to proposal Section V.H
11. **Step 11**: Update proposal changelog (v1.9.0)
12. **Step 12**: Update plan Activity 1.3.1 status
13. **Step 13**: Update plan Activity 1.3.3 with tasks
14. **Step 14**: Update plan changelog (v1.17.0)

---

## VIII. APPENDIX

### A. Research Report Reference

| Research ID | File Path |
|:------------|:----------|
| T801A-RES-002 | `prompt/artifacts/tasks/T801/research/report/report_T801A-RES-002_system-architecture-research.md` |

### B. Context Material References

| Document | File Path |
|:---------|:----------|
| Plan File | `prompt/artifacts/tasks/T801/consultant/workspace/plan/plan_T801A_phase0-1.md` |
| Proposal File | `prompt/artifacts/tasks/T801/consultant/workspace/proposal/T801A/proposal_T801A_phase1.md` |
| Research Brief | `prompt/artifacts/tasks/T801/research/brief/brief_T801A-RES-002_system-architecture-research.md` |

### C. T102 Compliance References

| Standard | Application |
|:---------|:------------|
| T102-ADR-005 | E-RID ID construction and category definitions |
| T102-ADR-004 | E-GDR/E-ADR body format and cross-artifact linking |
| T102-ADR-007 | Issues & Risks register schema |

---

**Document Status**: Draft
**Approval Required**: Client review before proposal/plan updates
**Next Review**: Upon Client QA feedback
