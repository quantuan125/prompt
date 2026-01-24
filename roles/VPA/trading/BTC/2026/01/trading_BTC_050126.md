# CONTEXT: 
## TRADER CONTEXT: 
Today: Today is Monday 5th of January 2026, we are in London session, 1 hours until US session. We have ISM Manufacuring PMI as major data/macro event released today with details outlined as below. Refers to `MACRO CONTEXT` for the rest of the macro events this week.  

Last month: Marked the end of Quantitative Tightening cycle from the FED and market was reacting to 25bps rate cut from FOMC. Holiday season and low volume/liquidity environment toward the end of the year. 

This week: A return back from holiday season. 

Directive: Price is bearish on weekly/daily timeframe however caution due low volume environemnt near Christmas holiday and after multi-week consolidation at monthly support/demand zone with prior daily oversold signals. Prefers mean-reversion setup with prioritize on trade-based location rather than trend. 

Sentiment: With price action last month that have liquidated millions of leveraged crypto traders and enact fears, the general consensus is bearish with hypothesis of the top for the cycle is already set for BTC, and the start of an extended bear market into 2026. `Fear & Greed Index` improve since last month from around 14-20 (EXTREME FEAR) toward 26-40 (FEAR/NEUTRAL) in the current week.  

## TECHNICAL CONTEXT
### Key Levels 

```yaml
meta:
    pair: BTCUSDT
    units: "k"   # all numbers rounded with 'k'
    note: "Ranges use '-', e.g., 113.2-114.7k"

levels:
  ALL:
    ath: 126.2

  1M:
    major:
      H_MAJOR: 126.2
      L_MAJOR: 74.5
    sr: 
      SR_1: 115.8
      SR_2: 102.5
      SR_3: 93.7
      SR_4: 82.5
    poc:
      POC_1: 118.0
      POC_2: 104.7
      POC_3: 96.4
      POC_4: 84.2
    zones:
      BUY_2: 89.5
      BUY_1: 73.7
    inactive:
      H_BOS: 109.6

  1W:
    local: 
      H: 96.0
      L: 80.6
    major:
      H_MAJOR: 126.2
      L_MAJOR: 102.0
    sr:
      SR_1: 108.3
      SR_2: 100.9
      SR_3: 86.1
      SR_4: 80.7
      SR_5: 78.4
    poc:
      POC_1: 101.8
      POC_2: 94.6
      POC_3: 91.4
      POC_4: 87.3
      POC_5: 67.4
    zones:
      SELL_1: 114.9
      SELL_2: 106.1
      SELL_3: 99.1
    active:
      L_BOS: 107.3
    inactive:
      L_MSB: 111.9
      H_FSB: 124.5
      L_FSB: 108.6

  1D:
    major:
      H_MAJOR: 90.6
      L_MAJOR: 86.4
    sr:
      SR_1: 93.4
      SR_2: 89.5
      SR_3: 88.4
    poc:
      POC_1: 95.7
      POC_2: 92.5
      POC_3: 90.2
      POC_4: 84.6
      POC_5: 79.7
    zones:
      SELL_1: 94.2
      SELL_2: 91.1
      BUY_1: 83.5-86.0
      BUY_2: 89.1
    session:
      PDH: 94.8
      PDL: 91.5
    active:
      H_BOS:: 90.6
    inactive:
      H_FSB: 90.3

  4H:
    major:
      H_MAJOR: 94.8
      L_MAJOR: 90.9
    sr:
      {}
    poc:
      POC_1: 93.8
      POC_2: 93.0
      POC_3: 88.1
      POC_4: 86.4
      POC_5: 82.2
    zones:
      BUY_1: 91.8-92.4
    active:
      H_BOS: 91.8
    inactive:
      H_BOS: 91.0

  1H:
    local: 
      H: 94.4
      L: 93.1
    major:
      H_MAJOR: 94.8
      L_MAJOR: 92.2
    sr: {}
    poc: {}
    zones:
      BUY_1: 93.2-93.5
      NEUTRAL: 94.0
    active:
      L_CHOCH: 93.5
    inactive:
      H_BOS: 91.8

  15m:
    major:
      H_MAJOR: 88.3
      L_MAJOR: 86.6
    sr: {}
    poc: {}
    zones:
      {}
    active:
      H_BOS: 87.8
    inactive: 
      L_FSB: 87.4
```

### **Weekly (1W — Super-HTF Structure)** 

* **Previous (~30 candles):** After the late-’24 `1M_bullish_channel`, weekly trend deteriorated with the distribution/rollover under `ALL.ath` / `1M.major.H_MAJOR`, then a failed push into `1W.inactive.H_FSB` followed by the liquidation leg that confirmed `1W.active.L_BOS`. Weekly tape was dominated by a series of `1W_bearish_VCs`, with `1W_9/21EMA` bearish posture and `1W_RSI` held sub-50, transitioning price from above the historic bull support band into the broader monthly demand stack around `1M.zones.BUY_2` → `1M.poc.POC_4` / `1M.sr.SR_4`.
* **Current (~5 candles):** Price is **still inside the weekly candle range** `1W.local.L` ↔ `1W.local.H`, basing **below** the weekly supply ladder `1W.zones.SELL_3` / `1W.zones.SELL_2` / `1W.zones.SELL_1`. The current candle is a `1W_bullish_range_VC` with **very depressed** volume vs `1W_vol_ma20` (holiday-thin feel), `1W_RSI` still < 50, and price below `1W_21EMA` / `1W_50EMA` while holding well above `1W_200EMA/200SMA` — **bearish HTF regime, stabilizing base**.

---

### **Daily (1D — HTF for intraday)** 

* **Previous (~30 candles):** Selloff completed into the monthly/weekly demand context with the noted absorption `1D_bearish_hammer_HVC` at/near `1W.local.L`, then holiday consolidation around key daily pivots (`1D.poc.POC_3`, `1D.poc.POC_4`) while the market rebuilt acceptance above `1D.major.L_MAJOR`.
* **Current (~5 candles):** The reclaim / breakout is defined by `1D.active.H_BOS` through `1D.major.H_MAJOR`, holding above `1D.zones.SELL_2` and now probing toward the top of the weekly band `1W.local.H` with the nearer cap at `1D.zones.SELL_1`. Momentum is **constructive**: price above `1D_9/21EMA` and above `1D_50EMA`, `1D_RSI` > 60 while `1D_RSI-MA` still sub-50 (**bullish***), but **structural “bear-market overlay” remains** with price still below `1D_200EMA/200SMA`. Today’s candle reads as a `1D_bullish_range_VC` (not an ignition candle yet).

---

### **4H (4H — HTF for 1H)** 

* **Previous (~30 candles):** Weekend lift sustained above `1D.zones.SELL_2` and confirmed continuation via `4H.active.H_BOS`, with price reclaiming `4H_200EMA/200SMA` for the first time in months and holding above `4H_9/21EMA` + `4H_M_VWAP`.
* **Current (~5 candles):** The current bar is a `4H_bearish_pullback_VC` (volume well below `4H_vol_ma20`), which is *healthy* **if** it stays as a weak pullback into demand rather than a high-volume rejection. Key magnets/supports: `4H.poc.POC_1` (chop risk), then `4H.zones.BUY_2` → `4H.zones.BUY_1`, with deeper “break-glass” supports at `4H.poc.POC_2` / `4H.poc.POC_3`. Bias: **bullish structure, short-term mean reversion risk** while price is slightly under `4H_W_VWAP`.

---

### **1H (1H — TTF)** 

* **Previous (~30 candles):** HH/HL sequence established after reclaiming `1D.zones.SELL_2`, with the trend anchored by `1H.active.H_BOS`. Upside probed `1H.major.H_MAJOR` and then rotated back toward the base `1H.local.L` / `1H.zones.BUY_1` (tight balance near the 4H POC).
* **Current (~5 candles):** Price is consolidating between `1H.major.H_MAJOR` and `1H.local.L`. The current candle behaves like a `1H_bearish_pullback_VC` (below `1H_vol_ma20`), with price **slightly below** `1H_9EMA` and under `1H_S_VWAP` while still above `1H_21EMA` and well above `1H_50EMA`. `1H_RSI` is mid-high (cooling from earlier extension) and `1H_RSI-MA` remains elevated — **trend-up but compressed; triggers matter**.

## MACRO CONTEXT
### LAST WEEK

* **Holiday/liquidity conditions**

  * **Bond market early close:** Wed **Dec 31** recommended early close **2:00pm ET**. **US equities closed:** Thu **Jan 1** (New Year’s Day), reopening Fri **Jan 2**. [S12]
  * **Thin year-end liquidity** into the first 2026 session; positioning was still “holiday calm” before the heavier January data slate.

* **US Macro (released)**

  * **Pending Home Sales (Nov):** **+3.3% m/m**, **+2.6% y/y**; index hit the **highest since Feb 2023** (broad-based regional gains). [S1][S2]
  * **Chicago Business Barometer (Dec):** **43.5** (still contraction <50; rebound from **36.3** in Nov). [S3]
  * **Initial Jobless Claims:** **199k** (week ending Dec 27), down from **215k** prior; **continuing claims 1.866m** (week ending Dec 20). [S4]

* **Fed / Rates**

  * **Fed minutes (Dec meeting):** reaffirmed target range **3.50%–3.75%** and highlighted divisions around the path of policy (cuts delivered across the last three 2025 meetings). [S5][S6]

* **US Politics / Trade**

  * **Trump trade policy:** delayed certain planned tariff increases (including on some imports like furniture/cabinets) while keeping a **25% tariff** in place; selective reductions/adjustments were announced. [S7]

### THIS WEEK

* **Today (Mon Jan 5) — key macro catalyst**

  * **ISM Manufacturing PMI (Dec)** — **10:00am ET (16:00 CET)**.

    * **Consensus:** **48.3** vs **48.2** prior (still contraction).

* **Mid-week (Wed Jan 7) — labor + growth pulse**

  * **ADP Private Payrolls (Dec)** — **8:15am ET (14:15 CET)**.
  * **ISM Services PMI (Dec)** — **10:00am ET (16:00 CET)**.

    * **Consensus:** **52.2–52.3** vs **52.6** prior (still expansion).

* **Friday (Jan 9) — primary risk event**

  * **US Employment Situation / NFP (Dec)** — **8:30am ET (14:30 CET)**.

    * **Reuters poll:** **+55k** jobs expected (vs **+64k** in Nov).
    * **Context from last report:** unemployment **4.6%** in Nov (4+ year high).

* **Fed / Rates (market-implied)**

  * **Fed funds futures:** “little chance” of a cut at **late-Jan FOMC**, but **~50% probability** of a **25bp** cut in **March** (per Reuters).
  * **Next major inflation checkpoint:** **CPI due Tue Jan 13** (outside this week, but close enough to matter for positioning).

* **Politics / Geopolitics (Trump-linked)**

  * **Venezuela shock:** Trump said the US is putting Venezuela under **temporary American control** after Maduro’s capture; investors flagged potential **oil volatility spillover** into broader risk assets.
  * **Policy overhangs:** Reuters notes a **Supreme Court** decision looming on **Trump’s tariffs**, and focus on Trump’s **choice of a new Fed chair** ahead of Powell’s term-end timing in **2026**.

* **Tech / “risk sentiment” drivers**

  * **CES 2026 (Las Vegas) runs Jan 6–9:** Reuters highlights **AI + autonomous driving** as center stage; key speakers include **Nvidia CEO Jensen Huang** and **AMD CEO Lisa Su**.

### MACRO ANALYSIS

#### OVERALL CROSS-MARKETS

Today’s session is set up for **headline + data-driven volatility**: **ISM Manufacturing (10:00 ET)** is the first major “rates-sensitive” print of the week, followed by **ADP/ISM Services** and culminating in **NFP Friday**. Markets are balancing (1) **Fed-cut expectations** (policy rate currently **3.50%–3.75%**, with futures implying **no Jan cut** but **~50% odds of March**) against (2) **growth risk** (jobs expected soft at **+55k**) and (3) **Trump-linked geopolitical/trade uncertainty** (Venezuela, tariffs, Fed-chair optics). Net: expect **USD + yields** to be the transmission channel into **SPX (risk)**, **BTC (high-beta liquidity proxy)**, and **gold (real-rate + risk hedge)**.

#### BTC & ETH

BTC/ETH remain primarily **liquidity/risk-sentiment sensitive**: if **ISM/NFP** pushes markets toward **earlier Fed easing** (lower yields, softer USD), that’s generally supportive. But if jobs weakness is interpreted as **recession risk** rather than “Fed-friendly,” BTC can trade more like **risk-off equities** (drawdown alongside SPX). Watch the **rates impulse** first, then whether SPX confirms. 

  
# TRADING PLAN FOR 1H_TTF (Trigger • Location • Context)

## SHORT

### **ORANGE_A — Short reversal at `1D.zones.SELL_1` → `1W.local.H`**

* **Context**: HTF bounce is running into **weekly range-top supply** (`1W.local.H`) with the first daily supply at `1D.zones.SELL_1`. Only valid if bullish VPA **fails** (up-candles shrink, wicks increase) and **CVD/RSI divergence appears** *and then* 1H structure **breaks** (no premature fading during trend). 
* **Location**: `1D.zones.SELL_1` confluence into `1W.local.H` (optionally include `1D.poc.POC_1` as nearby magnet/decision point).
* **Trigger**: Liquidity sweep above `1D.zones.SELL_1` or into `1W.local.H` **then** confirmed `TTF_L_MSB` (1H) + LTF (15m) realignment (`LTF_L_MSB`) with **bearish VPA** (sell-side ignition/expansion; no absorption-only guess).
* **Invalidation**: Clean acceptance/hold above `1W.local.H` with bullish continuation VPA (then this is a breakout regime — stand down).
* **Setup Priority**: **A-**

---

### **PURPLE_A — Short fade via `H_FSB` at `1H.major.H_MAJOR`**

* **Context**: Range-top fade inside the 1H box **only if** price cannot sustain above `1H.major.H_MAJOR` and momentum rolls (RSI divergence + VWAP rejection). This is a tactical short, not a “call the top” trade.
* **Location**: `1H.major.H_MAJOR` (failed break) with nearby overhead continuation failure (watch reaction if also near `1D.zones.SELL_1`).
* **Trigger**: Wick above `1H.major.H_MAJOR` → close back below (FSB) **then** `LTF_L_MSB` (15m) with falling delta/CVD behavior (chart-confirm) and bearish volume expansion.
* **Invalidation**: 1H close above `1H.major.H_MAJOR` that **holds** (turns into support) — do not fight acceptance.
* **Setup Priority**: **B-**

---

### **PINK_A — Short counter-trend momentum if `1H.local.L` fails**

* **Context**: Only if the market loses balance: price remains below `1H_S_VWAP` + rolls under the `1H_9/21EMA` band and shows bearish follow-through (not just a single wick).
* **Location**: Breakdown zone under `1H.local.L` with downside path toward `4H.zones.BUY_1` / `4H.major.(H/L)_MAJOR` band as next structural shelf.
* **Trigger**: Confirmed `1H_L_CHOCH` → continuation selling **then** retest failure of the broken level from below with `LTF_L_BOS/MSB` and bearish VPA (ideally pullback on low volume, breakdown on higher relative volume).
* **Invalidation**: Reclaim back above `1H.local.L` and `1H_S_VWAP` with restored HLs.
* **Setup Priority**: **B**

---

### **RED_A — Short breakdown below `1H.major.L_MAJOR` / `4H.major.L_MAJOR`**

* **Context**: This is the “trend failure” scenario — only engage if the larger bounce is clearly dead and sell pressure is decisive (no chop-entry).
* **Location**: Structural break of `1H.major.L_MAJOR` confluence with `4H.major.L_MAJOR` (major regime line).
* **Trigger**: Hard `1H_L_BOS` through `1H.major.L_MAJOR` with strong bearish VPA **then** low-volume retest that rejects + `LTF_L_MSB/BOS`.
* **Invalidation**: Immediate reclaim above `1H.major.L_MAJOR` that holds (failed breakdown = exit/avoid).
* **Setup Priority**: **B**

---

## LONG

### **WHITE_A — Long continuation on pullback to `4H.active.H_BOS`**

* **Context**: Base case is still **bullish intraday**: 4H structure up, daily recovery up. Prefer buying weak pullbacks (VCs) into support with RSI holding >50 and price reclaiming VWAPs.
* **Location**: Retest `4H.active.H_BOS` confluence with `1H` dynamic support (hold/flip around `1H_21EMA`) and demand stack `4H.zones.BUY_2` → `4H.zones.BUY_1`.
* **Trigger**: Pullback into location on **weak volume** → `LTF_H_MSB` (15m) back up, followed by `LTF_H_BOS` continuation (CVD/OBV confirmation on chart).
* **Invalidation**: Acceptance below `4H.zones.BUY_1` (demand failed) or a fresh `1H_L_MSB` against the long.
* **Setup Priority**: **A+**

---

### **BLUE_A — Long fade on `L_FSB` at `4H.zones.BUY_1` (deeper pullback)**

* **Context**: Buy the liquidation-sweep **only** if sellers can’t progress (failed breakdown) and reversal structure forms (do **not** knife-catch).
* **Location**: Sweep below `4H.zones.BUY_1` with extension room toward `4H.major.(H/L)_MAJOR` band.
* **Trigger**: `L_FSB` (sweep + reclaim) **then** `LTF_H_MSB` with bullish response volume (or absorption confirmed by follow-through reversal, not the first spike).
* **Invalidation**: Sustained acceptance below `4H.zones.BUY_1` (turns into breakdown path → defer to shorts).
* **Setup Priority**: **B+**

---

### **TEAL_A — Long momentum scalp while holding above `1H.local.L`**

* **Context**: If price regains/holds `1H_S_VWAP` and keeps printing HLs above `1H.local.L`, scalps are valid *with* flow — but don’t overtrade inside the 4H POC chop.
* **Location**: Above `1H.local.L` with support from `1H_9EMA` / `1H_S_VWAP`.
* **Trigger**: `LTF_H_BOS/MSB` on retest (15m) with rising volume and clean candle bodies; avoid if breakout is on dying volume into `1H.major.H_MAJOR`.
* **Invalidation**: Loss of `1H.local.L` + inability to reclaim `1H_S_VWAP`.
* **Setup Priority**: **B**

---

### **YELLOW_A — Long major reversal at `1D.zones.BUY_2` → `1D.major.L_MAJOR`**

* **Context**: Only if the market sells off hard and the 1H trend flips bearish first, then finds higher-timeframe demand. This is the “reset then re-align” long.
* **Location**: `1D.zones.BUY_2` with extension toward `1D.major.L_MAJOR` (major demand shelf).
* **Trigger**: Confirmed `TTF_H_MSB` (1H) **after** the sell leg shows exhaustion + LTF reclaim (`LTF_H_MSB`) with bullish VPA.
* **Invalidation**: Acceptance below `1D.major.L_MAJOR` (demand failure).
* **Setup Priority**: **A**

---

### **GREEN_A — Long breakout above `1H.major.H_MAJOR`**

* **Context**: Continuation breakout only if it’s a **true ignition** (body expansion + follow-through) and not just a wick into supply. Ideally occurs with risk-on response post data (ISM).
* **Location**: Break/accept above `1H.major.H_MAJOR` with next upside magnet toward `1D.zones.SELL_1` and then the weekly range cap `1W.local.H`.
* **Trigger**: `1H_H_BOS` on strong bullish VPA **then** low-volume pullback retest that holds, confirmed by `LTF_H_MSB/BOS`.
* **Invalidation**: Failed retest (acceptance back below `1H.major.H_MAJOR`) or immediate `1H_L_CHOCH` post-break.
* **Setup Priority**: **B**


  
# TASK  
We have outlined the colored trading plans aligned with the chart using 1H_TTF with 4H as primary trend HTF and 1D as structural context. Our LTF for execution is 10m or 15m. 

You task is to outlined a concrete trading strategies for today's session and follow this initial priority sequence:
```
PRIORITY SEQUENCE (ABSOLUTE):
1. TTI
2. CAS 
3. SPP 
4. Devil's Advocate
5. TLDR with Action Plan
```

# NOTE
- 1W: `OVERALL-ASSESSMENT = BEARISH*`. DO NOT PERFORM TTI on the 1W_TF. 
- `PG` grades are assessed based on the plan full viability. DO NOT DEGRADE the plan based on probability/possibility.  

