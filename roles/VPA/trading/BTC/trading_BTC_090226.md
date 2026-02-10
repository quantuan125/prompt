# CONTEXT: 
## TRADER CONTEXT: 
Today: Today is Monday 9th of February 2026, we are 30 minutes into US session open. We have no major macro data released today. Refers to `MACRO CONTEXT` for the rest of the macro events this week.  

Last month: Marked the end of Quantitative Tightening cycle from the FED and market was reacting to 25bps rate cut from FOMC. Holiday season and low volume/liquidity environment toward the end of the year. 

Last week: A return back from holiday season, and continuation of the bearish trend after the end of last year bullish cycle. Second government shutdown got resolveed and macro data are back to be released for this week. 

Directive: Price is bearish on both weekly and daily, prioritize shorts, however caution due to sell-off overextension and capitulation on the weekly and daily. 

Sentiment: With price action last year quarter that have liquidated millions of leveraged crypto traders and enact fears after failure to break ATH. In addition to being an apathetic top of this cycle, the general consensus is that this the start of the BTC bear market in 2026. `Fear & Greed Index` improve last month toward 26-40 (FEAR/NEUTRAL) however dopped back to below 15 (EXTREME FEAR) in the current week following the continued sell-off

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
      SR_5: 71.3
      SR_6: 58.7
    poc:
      POC_1: 118.0
      POC_2: 104.7
      POC_3: 96.4
      POC_4: 87.5
      POC_5: 67.0
    zones:
      SELL_1: 112.0
      SELL_2: 98.1
      BUY_1: 73.7
    active:
      H_FSB: 109.6
    inactive:
      H_BOS: 73.8

  1W:
    major:
      H_MAJOR: 97.9
      L_MAJOR: 80.6
    sr:
      SR_1: 100.9
      SR_2: 98.4
      SR_3: 86.8
      SR_4: 80.7
    poc:
      POC_1: 101.7
      POC_2: 94.4
      POC_3: 91.4
      POC_4: 84.4
      POC_5: 76.4
    zones:
      SELL_1: 90.8
      SELL_2: 85.4
    active:
      L_BOS: 80.6
    inactive:
      L_BOS: 107.3

  1D:
    major:
      H_MAJOR: 90.6
      L_MAJOR: 60.0
    sr:
      SR_1: 93.4
      SR_2: 89.5
      SR_3: 88.4
    poc:
      POC_1: 90.2
      POC_2: 82.8
      POC_3: 78.8
      POC_4: 70.8
    zones:
      SELL_1: 75.4
    session:
      PDH: 72.3
      PDL: 68.9
    active:
      L_BOS: 86.1
    inactive:
      L_MSB: 89.3

  4H:
    major:
      H_MAJOR: 72.3
      L_MAJOR: 67.3
    sr:
      {}
    poc:
      POC_1: 75.2
      POC_2: 73.8
      POC_3: 69.8
      POC_4: 68.0
      POC_5: 64.9
    zones:
      SELL_1: 72.0
      BUY_1: 62.9
      NEUTRAL: 69.8
    active:
      L_BOS: 74.6
    inactive:
      L_BOS: 86.1

  1H:
    major:
      H_MAJOR: 71.5
      L_MAJOR: 68.3
    sr: {}
    poc: {}
    zones:
      SELL_1: 70.3-70.7
      BUY_1: 68.5
    active:
      L_BOS: 70.0
    inactive:
      H_FSB: 71.6
      H_CHOCH: 70.0
  
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

### **Weekly (1W – Super-HTF Structure)**

* **Previous (~30 candles):** After the macro top at `1M.major.H_MAJOR` (**~126.2k**), BTC lost the prior bull-market support regime and rotated down into the monthly demand area around `1M.zones.BUY_1` (**~73.7k**), forming a multi-week base before a weak recovery capped into `1W.major.H_MAJOR` (**~97.9k**) (EMA band rejection). The next leg confirmed a trend-continuation breakdown with `1W.active.L_BOS` at `1W.major.L_MAJOR` (**~80.6k**), followed by a capitulation-style `1W_bearish_hammer_HVC` that **accepted below** `1M.major.L_MAJOR` (**~74.5k**) and `1M.zones.BUY_1` (**~73.7k**) — “support → resistance” conditions.
* **Current (~5 candles):** Price is still **below** the reclaimed threshold `1M.major.L_MAJOR` / `1M.zones.BUY_1` and is trading closer to monthly value support magnets (`1M.poc.POC_5` at **~67.0k**) than to any weekly resistance. Weekly momentum remains risk-off: `1W_RSI` is deeply oversold (~28.6) and the MA stack is bearish (price well below `1W_9/21/50EMA`, only holding above `1W_200EMA/MA`). Current developing action resembles a `1W_bearish_long-legged-doji_VC` (indecision after liquidation) — **no trend reversal without a confirmed structure reclaim back above `1M.major.L_MAJOR` / `1M.zones.BUY_1`.**

---

### **Daily (1D – HTF for intraday)**

* **Previous (~30 candles):** The daily rollover from `1W.major.H_MAJOR` (**~97.9k**) produced `1D.inactive.L_MSB` at **~89.3k**, then continuation with `1D.active.L_BOS` (**~86.1k**) on heavy sell pressure (series of bearish HVCs). Price then **broke decisively below** `1M.major.L_MAJOR` (**~74.5k**) + `1M.zones.BUY_1` (**~73.7k**), flushed into `1M.poc.POC_5` (**~67.0k**) and finally put in capitulation at `1D.major.L_MAJOR` (**~60.0k**) with a `1D_bearish_engulfing_SHVC` (yearly extreme) + oversold RSI context.
* **Current (~5 candles):** The recovery is now a **retest phase** into descending dynamic resistance (daily EMA/VWAP cluster) while price chops between `1D.session.PDH` (**~72.3k**) and `1D.session.PDL` (**~68.9k**) around daily value levels (`1D.poc.POC_4` at **~70.8k** nearby as a magnet). Momentum is still fragile: `1D_RSI` (~32.6) is only mildly off the floor, recovering from 17. **Bias remains bearish unless acceptance back above `1D.session.PDH` or a higher-timeframe reversal structure forms.**

---

### **4H (4H – HTF for 1H execution)**

* **Previous (~30 candles):** From the capitulation base at `1D.major.L_MAJOR` (**~60.0k**), price built a counter-trend rebound and printed a higher low at `4H.major.L_MAJOR` (**~67.3k**), then pushed into overhead supply `4H.zones.SELL_1` (**~72.0k**) and tested `4H.major.H_MAJOR` (**~72.3k**). That push failed to convert acceptance as a `4H.active.H_FSB`and rolled back under midrange value, implying the rally was corrective rather than structural.
* **Current (~5 candles):** Price is rotating around the mid `4H.zones.NEUTRAL` (**~69.8k**) and remains below the `4H_9/21EMA` + `4H_W_VWAP` cluster (bearish control overhead). Latest impulse down looked like **momentum reassertion**, while the current rebound prints as a `4H_bullish_hammer_VC` responding from the `1D.session.PDL` (**~68.9k**) area — but it’s still **only a bounce** unless `4H.zones.NEUTRAL` reclaims/holds. Downside magnets if rejection persists: `4H.poc.POC_4` (**~68.0k**) → `4H.major.L_MAJOR` (**~67.3k**) → `4H.poc.POC_5` (**~64.9k**) → `4H.zones.BUY_1` (**~62.9k**).

---

### **1H (1H – TTF / session driver)**

* **Previous (~30 candles):** Weekend recovery stayed inside the 4H range, then Asia swept the top (`4H.major.H_MAJOR` at **~72.3k**) and stalled with a `1H_bearish_inverted-hammer_HVC` (liquidity grab + rejection). The selloff confirmed `1H.active.L_BOS` at **~70.0k** (breakdown below the pivot) with a bearish `1H_9/21EMA` crossover; `1H_CVD` trended negative (≈ **-170K** on the chart), supporting distribution. Price then flushed into demand at `1H.zones.BUY_1` (**~68.5k**) and tagged `1H.major.L_MAJOR` (**~68.3k**) on a volume spike (stopping behavior).
* **Current (~5 candles):** Price is now **retesting the breakdown zone**: `4H.zones.NEUTRAL` (**~69.8k**) → `1H.active.L_BOS` (**~70.0k**) with overhead supply `1H.zones.SELL_1` (**~70.3–70.7k**). The developing candle reads like a `1H_bullish_small-body_VC` (weak rebound) while still below `1H_S_VWAP` / `1H_21EMA` and with CVD not flipping convincingly. **Until `1H.active.L_BOS` is reclaimed and defended, rallies into `1H.zones.SELL_1` are “sell-the-rip” candidates, not trend reversals.**

## MACRO CONTEXT

### LAST WEEK

* **US data flow distorted by the brief federal funding lapse (BLS delays/reschedules):**

  * **JOLTS (Dec 2025):** *Actual* **6.542M** vs *Est* **7.200M** vs *Prior* **6.928M** (released Thu).
  * **Initial Jobless Claims:** *Actual* **231K** vs *Est* **212K** vs *Prior* **209K** (released Thu).
  * **UMich Consumer Sentiment (prelim, early Feb):** *Actual* **57.3** vs *Est* **55.0** vs *Prior* **56.4** (released Fri).

* **Latest inflation pipeline print (most recent PPI m/m):**

  * **US PPI (Dec 2025, released Fri Jan 30):** *Actual* **+0.5% m/m** vs *Est* **+0.2%** vs *Prior* **+0.2%**; **+3.0% y/y**.
  * **Important for today:** there was **no new US PPI release today**; the **next US PPI (Jan 2026 reference period)** is **delayed** (see “This Week”).

* **Fed / politics (Trump-Fed tension remains a macro overhang):**

  * Fed messaging leaned **“wait-and-see”** on further cuts amid **stalled disinflation** concerns and tariff-related uncertainty (policy rate still **3.50%–3.75%**).
  * Political pressure narrative remains active: markets sensitive to any headlines implying **Fed independence risk** (chair succession, legal challenges involving Fed officials, etc.).

### THIS WEEK

* **Key US macro releases (rescheduled by BLS) — the main catalysts for rates, USD, equities, gold, crypto:**

  * **Wed Feb 11 (08:30 ET) — Employment Situation (Jan 2026):**

    * **Nonfarm Payrolls:** *Est* **+70K** vs *Prior* **+50K**
    * **Unemployment Rate:** *Est* **4.4%** vs *Prior* **4.4%**
    * **Avg Hourly Earnings:** *Est* **+0.3% m/m** & **+3.6% y/y** vs *Prior* **+3.8% y/y**
  * **Fri Feb 13 (08:30 ET) — CPI + Real Earnings (Jan 2026):**

    * **Headline CPI:** *Est* **+0.3% m/m** vs *Prior (Dec)* **+0.3% m/m**
    * **Core CPI:** *Est* **+0.3% m/m** vs *Prior (Dec)* **+0.2% m/m**
    * **Prior (Dec CPI details):** **2.7% y/y** headline; **2.6% y/y** core.

* **PPI note (because you flagged “PPI m/m today”):**

  * **US PPI (Jan 2026)** is **not today** — it is **rescheduled to Fri Feb 27 (08:30 ET)**.

* **Rates / liquidity & event-risk around Treasury supply (can move real yields intraday):**

  * **Treasury coupon auctions:** **3Y (Tue Feb 10)**, **10Y (Wed Feb 11)**, **30Y (Thu Feb 12)**.
  * **Holiday ahead:** **Mon Feb 16 (Washington’s Birthday)** can affect settlement/liquidity conditions around mid-month.

* **Fed communication this week (headline sensitivity for “cuts vs inflation” pricing):**

  * Multiple Fed speakers scheduled across the week (including **Jefferson/Waller** early-week, plus others) — watch for any shift in emphasis between **inflation credibility** vs **labor-market cooling**.

* **Policy/administration signals relevant to rates:**

  * Weekend commentary highlighted that major **Fed balance sheet** changes are unlikely to be immediate; discussion continues on the tradeoff between **lower mortgage rates** goals vs **tightening via balance sheet shrinkage**.

* **Global macro (secondary, but can spill into USD/rates/risk and commodities):**

  * **China inflation** expected to cool (headline CPI roughly **~0.3–0.4% y/y** range flagged by major outlets) while producer-price deflation continues — relevant for broad risk tone and industrial/commodity narrative.
  * Heavy US earnings week (large consumer/tech names) keeps **risk sentiment** reactive — important because BTC often “beta-trades” equity risk appetite during data-heavy weeks.

### MACRO ANALYSIS

#### OVERALL CROSS-MARKETS

Today’s session is essentially **positioning ahead of two rescheduled US macro bombs (Jobs Wed, CPI Fri)**, with **Treasury supply** and **Fed speakers** as the main *intraday* drivers for **yields/real yields**. Last week’s **JOLTS miss** (cooling demand) and **higher jobless claims** lean **slightly dovish** for growth/risk, but the macro “tug-of-war” is that **inflation progress is not clean** (recent **PPI surprise** + tariff/pass-through uncertainty + seasonal inflation risk flagged by major desks). Practically: **real yields up = headwind** for both **SPX and BTC**; **real yields down = tailwind** for both, while **gold** tends to like **lower real yields** and/or **policy uncertainty**.

#### BTC & ETH

BTC/ETH remain most sensitive to **liquidity expectations** (rates path, balance sheet, real yields) and **equity risk sentiment**. A **soft jobs + contained CPI** mix supports the “easier policy later” narrative → typically constructive for crypto (often alongside equities). A **hot CPI** (or wage-driven upside surprise) risks repricing the front end hawkishly → tighter liquidity expectations → usually bearish for BTC/ETH near-term. Keep in mind: crypto can sometimes catch a secondary “inflation hedge” bid, but in practice the dominant impulse is still **liquidity/tightness**.

# TRADING PLAN FOR 1H_TTF (Trigger • Location • Context)

## SHORT

### **WHITE_A — Short continuation (sell-the-retest ladder)**

* **Context**: 4H/1H remain **bearish-aligned** (price below VWAP/EMA clusters), with a weak rebound into value. Expect sellers to defend breakdown pivots; ideal is **low-volume pullback** into resistance followed by bearish continuation with CVD rolling over.
* **Location**: Retest band `4H.zones.NEUTRAL` (**~69.8k**) → `1H.active.L_BOS` (**~70.0k**) → extension into `1H.zones.SELL_1` (**~70.3–70.7k**).
* **Trigger**: Rejection at the band + **15m_L_MSB** (LTF) on a pullback (prefer bearish HVC/ignition + falling CVD).
* **Invalidation**: Acceptance + hold above `1H.zones.SELL_1` (**~70.3–70.7k**) with bullish follow-through (failed rejection).
* **Setup Priority**: `A+`

---

### **PINK_A — Short momentum scalp (below VWAP/EMA lid)**

* **Context**: If price stays pinned below `1H.active.L_BOS` with weak bids, scalps favor continuation down to liquidity below. Must see **bearish impulse volume > pullback volume** and CVD not diverging bullish.
* **Location**: Under `4H.zones.NEUTRAL` (**~69.8k**) while below `1H.active.L_BOS` (**~70.0k**).
* **Trigger**: **15m_L_BOS** (or fast **15m_L_MSB**) after a weak retest into `1H.active.L_BOS` (low-volume test → bearish continuation).
* **Invalidation**: Reclaim and hold above `1H.active.L_BOS` (**~70.0k**) that converts to support (kills scalp edge).
* **Setup Priority**: `B`

---

### **PURPLE_A — Short fade (failed breakout at the session top zone)**

* **Context**: Range behavior inside the 4H band: if buyers sweep highs but can’t convert acceptance, fade the failure with bearish CVD turn (classic FSB behavior).
* **Location**: Failure/sweep region at `1H.major.H_MAJOR` (**~71.5k**) with overhead confluence from `4H.major.H_MAJOR` (**~72.3k**) and supply `4H.zones.SELL_1` (**~72.0k**).
* **Trigger**: Sweep above `1H.major.H_MAJOR` then close back below + **15m_L_MSB** back into range (bearish reversal candle ideally HVC).
* **Invalidation**: Clean acceptance above `4H.major.H_MAJOR` (**~72.3k**) (breakout holds → don’t fade).
* **Setup Priority**: `B+`

---

### **RED_A — Breakdown & retest (major support failure path)**

* **Context**: If sellers regain dominance and take out the local floor, continuation shorts are valid **only** if the break is impulsive (bearish ignition HVC) and the retest is weak (low-volume).
* **Location**: Breakdown through `1H.major.L_MAJOR` (**~68.3k**) with demand `1H.zones.BUY_1` (**~68.5k**) failing to hold.
* **Trigger**: Confirmed `1H_L_BOS` through `1H.major.L_MAJOR` + low-volume retest into the broken level, then **15m_L_MSB/BOS** continuation.
* **Invalidation**: Sharp reclaim back above `1H.zones.BUY_1` (**~68.5k**) and hold (failed breakdown).
* **Setup Priority**: `B`

---

### **ORANGE_A — Short reversal after bullish counter-trend dies (re-align to HTF bearish)**

* **Context**: Only relevant **if** price runs a bullish counter-trend push above `4H.major.H_MAJOR` and into higher supply, but VPA weakens (stalling spreads, worsening CVD). We wait for the bullish attempt to **fail structurally** first.
* **Location**: Reversal area into `4H.major.H_MAJOR` (**~72.3k**) / `4H.zones.SELL_1` (**~72.0k**) with higher HTF overhead from `1D.zones.SELL_1` (**~75.4k**) / `1M.major.L_MAJOR` (**~74.5k**) acting as “ceiling if reached.”
* **Trigger**: Confirmed **1H_L_MSB** (TTF) against the bullish attempt → pullback to the new S/R flip → **15m_L_MSB** entry with bearish CVD.
* **Invalidation**: Acceptance above `1D.zones.SELL_1` (**~75.4k**) (trend ignition up; don’t fight).
* **Setup Priority**: `A`

---

## LONG

### **TEAL_A — Counter-trend scalp (reclaim pivot back above value)**

* **Context**: This is a **counter-trend** long inside a bearish regime: must be quick and fully confirmed. We require reclaim of the breakdown pivot + improving CVD (no “hope longs”).
* **Location**: Reclaim/hold back above `4H.zones.NEUTRAL` (**~69.8k**) and `1H.active.L_BOS` (**~70.0k**).
* **Trigger**: **15m_H_MSB/BOS** (LTF) after reclaim, then a low-volume retest holding above `1H.active.L_BOS`.
* **Invalidation**: Acceptance back below `4H.zones.NEUTRAL` (**~69.8k**) (reclaim fails).
* **Setup Priority**: `B`

### **BLUE_A — Long fade (failed breakdown at 1H demand)**

* **Context**: This is **counter-trend** versus the prevailing 1H/4H bearish control (price under `S_VWAP` and under `1H_21EMA`; current `1H_RSI` is mid (~45) so **no automatic “oversold” edge**). Only take if sellers **fail to follow through** below demand and CVD/OBV stop making new lows (absorption → reversal). Current 1H developing VC is **below average volume** (vs 1H vol MA), so we need a **real** stopping/absorption signal first (do not front-run).
* **Location**: Sweep/fail zone at `1H.major.L_MAJOR` (**~68.3k**) + `1H.zones.BUY_1` (**~68.5k**) with extension target/mean-reversion toward `4H.major.L_MAJOR` (**~67.3k**) if wicky before reversal.
* **Trigger**: Liquidity sweep below `1H.major.L_MAJOR` then reclaim back above `1H.zones.BUY_1` on a **stopping/absorption VC** (e.g., `15m_bullish_hammer_SHVC` or `15m_bullish_engulfing_HVC`) + **confirmed `LTF_H_MSB`** (15m) and **rising CVD**.
* **Invalidation**: Acceptance below `1H.major.L_MAJOR` (**~68.3k**) with bearish follow-through (series of bearish HVCs) — no bounce attempt.
* **Setup Priority**: `B-`

---

### **YELLOW_A — Long major reversal at 4H demand (deep mean reversion)**

* **Context**: Only if the bearish trend **dies structurally** (mandatory). We need a **true TTF reversal**: `1H_H_MSB` against the downtrend + improving `1H_CVD`. This plan assumes a deeper liquidation leg into major 4H demand where sellers exhaust.
* **Location**: `4H.zones.BUY_1` demand (**~62.9k**) with potential wick extension toward `1D.major.L_MAJOR` (**~60.0k**) as the “max pain” flush.
* **Trigger**: At/inside `4H.zones.BUY_1`, print stopping volume (e.g., `1H_bullish_hammer_SHVC`) then **confirmed `1H_H_MSB`**; enter on pullback to the new S/R flip (value zone) with **`LTF_H_MSB`** confirmation and CVD turning up.
* **Invalidation**: Acceptance below `4H.zones.BUY_1` (**~62.9k**) without reclaim (bear trend intact → stand down).
* **Setup Priority**: `A-`

---

### **GREEN_A — Long breakout & retest (range-high flip)**

* **Context**: This is a **counter-trend breakout** vs 1D bearish pressure, so it must be **ignition-quality**. You want buyers to reclaim the 4H range high and hold above VWAP/EMAs (1H back above `S_VWAP` and EMA stack improving). No “soft” breakouts.
* **Location**: Break & hold above `4H.major.H_MAJOR` (**~72.3k**) through `4H.zones.SELL_1` (**~72.0k**) with first retest as support.
* **Trigger**: **Confirmed `1H_H_BOS`** through `4H.major.H_MAJOR` with `1H_bullish_marubozu_HVC` (or similar ignition) + rising CVD; then **low-volume retest** holding above `4H.major.H_MAJOR` and `LTF_H_MSB/BOS` entry confirmation.
* **Invalidation**: Failed retest (acceptance back below `4H.major.H_MAJOR` **~72.3k**) or immediate `1H_L_CHOCH` after the breakout attempt.
* **Setup Priority**: `B`

---
  
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
- 1W: `OVERALL-ASSESSMENT = BEARISH`. DO NOT PERFORM TTI on the 1W_TF. 
- `PG` grades are assessed based on the plan full viability. DO NOT DEGRADE the plan based on probability/possibility. (e.g:  Zone is too far (72-75k) is not a valid CON or reason to degrade the PG of a plan) 


