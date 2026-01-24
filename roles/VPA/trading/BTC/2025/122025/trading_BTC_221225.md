# CONTEXT: 
## TRADER CONTEXT: 
Today: Today is Monday 22th of December 2025, we are in London session, 2 hours until US session. We have no major data/macro event released today. Refers to `MACRO CONTEXT` for the rest of the macro events this week.  

Last month: We have officially passed October + November which was supposed to be bullish month for BTC and crypto in terms of seasonality during a bull cycle year, however we got the opposite of that: largest crypto liquidation sell off and continuation of weekly downtrend breaking bullish structure for the cycle despite soft CPI + Inflation data print + resolution on China-US tariffs.

This month: Marked the end of Quantitative Tightening cycle from the FED and market was reacting to 25bps rate cut from FOMC last week.

Directive: Price is bearish on weekly/daily timeframe however caution due low volume environemnt near Christmas holiday and after multi-week consolidation at monthly support/demand zone with prior daily oversold signals. Prefers mean-reversion setup with prioritize on trade-based location rather than trend. 

Sentiment: With price action last month that have liquidated millions of leveraged crypto traders and enact fears, the general consensus is bearish with hypothesis of the top for the cycle is already set for BTC, and the start of an extended bear market into 2026. `Fear & Greed Index` worsen from 30-40 (NEUTRAL) since last month to sustaining around 14 (EXTREME FEAR) - 25 (FEAR) in the current weeks. 

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
      H: 116.4
    major:
      H_MAJOR: 126.2
      L_MAJOR: 80.6
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
      SELL_3: 98.1
    active:
      L_BOS: 107.3
    inactive:
      L_MSB: 111.9
      H_FSB: 124.5
      L_FSB: 108.6

  1D:
    major:
      H_MAJOR: 90.4
      L_MAJOR: 84.4
    sr:
      SR_1: 93.4
      SR_2: 89.5
      SR_3: 88.4
    poc:
      POC_1: 95.7
      POC_2: 93.0
      POC_3: 90.2
      POC_4: 84.6
      POC_5: 79.7
    zones:
      SELL_1: 94.2
      SELL_2: 91.1
      BUY_1: 83.5-86.0
    session:
      PDH: 89.1
      PDL: 87.6
    active:
      L_FSB: 85.2
    inactive:
      H_FSB: 94.2
      L_BOS: 87.7

  4H:
    local:
      H: 89.5
    major:
      H_MAJOR: 90.4
      L_MAJOR: 84.4
    sr:
      {}
    poc:
      POC_1: 92.4
      POC_2: 88.1
      POC_3: 86.4
      POC_4: 82.2
    zones:
      SELL_1: 88.9
      BUY_1: 85.2
      NEUTRAL: 87.4
    active:
      H_CHOCH: 89.4
    inactive:
      L_BOS: 87.5
      L_FSB: 85.2

  1H:
    major:
      H_MAJOR: 89.6
      L_MAJOR: 87.9
    sr: {}
    poc: {}
    zones:
      BUY_1: 88.5
      BUY_2: 89.4
    active:
      H_CHOCH: 87.6
    inactive:
      H_BOS: 86.6

  15m:
    major:
      H_MAJOR: 92.6
      L_MAJOR: 91.9
    sr: {}
    poc: {}
    zones:
      NEUTRAL: 92.3
    active:
      L_FSB: 92.0
    inactive: 
      H_FSB: 93.4
```

### **Weekly (1W – Super-HTF Structure)**

* **Previous (~30 candles):** After the `1M_bullish_channel` run, weekly trend weakened with `1W.inactive.L_MSB`, then an ATH sweep (`1W.inactive.H_FSB`) and a liquidation leg that **confirmed** `1W.active.L_BOS` under `1M.inactive.H_BOS`, aligned with a bearish `1W_9/21EMA` flip and bearish momentum confirmation (RSI/OBV per trader notes). Price then broke the historic bull support band (weekly mid MAs) and sold into monthly demand `1M.zones.BUY_2`, stalling for weeks under `1W.zones.SELL_3`. Notable sequence: multiple `1W_bearish_long_body_HVC` / `1W_bearish_engulfing_HVC` into the breakdown, followed by basing `1W_doji_VC` / `1W_spinning_top_VC` around `1W.major.L_MAJOR`.
* **Current (~5 candles):** Bounce remains corrective inside a **weekly bearish regime**: current developing candle is a `1W_bullish_spinning_top_VC` (very low relative volume vs `1W_vol_ma20`; `1W_RSI` ~39.8 below `1W_RSI-MA` ~46.2). Price is still **below** `1W_9EMA/21EMA/50EMA` while holding above the long-term weekly MAs and **above** `1W_W_VWAP/M_VWAP` (risk-on bounce, but not a weekly trend reversal). Key overhead magnets/supplies remain `1W.poc.POC_4` → `1W.poc.POC_3` and higher `1W.zones.SELL_3` / `1W.sr.SR_3`.

---

### **Daily (1D – HTF for intraday)**

* **Previous (~30 candles):** Selloff bottomed at `1W.major.L_MAJOR` with a stopping/absorption-style `1D_bearish_hammer_HVC` (per trader notes) + deeply oversold RSI (<25 at the trough), then recovered into a `1D_ascending_wedge` before breaking down on volume via `1D.inactive.L_BOS` toward `1D.zones.BUY_1`. The downside failed to follow through and `1D.active.L_FSB` was confirmed as price reclaimed `1D_9EMA` + `1D_W_VWAP`.
* **Current (~5 candles):** Current developing candle reads as `1D_bullish_spinning_top_VC` (sub-average volume vs `1D_vol_ma20`). Structure is a **range retest**: price is pushing from mid-range back toward `1D.major.H_MAJOR`, now approaching supply `1D.zones.SELL_2` (next `1D.zones.SELL_1`). Indicators: price **above** `1D_9EMA/21EMA` and **above** `1D_W_VWAP/M_VWAP`, but still **below** `1D_50EMA` and far **below** `1D_200EMA/SMA200` → bounce is constructive, yet still corrective versus the larger daily downtrend. Session refs: `1D.session.PDH` / `1D.session.PDL` as reaction pivots; nearby magnets include `1D.poc.POC_3`.

---

### **4H (4H – HTF for 1H)**

* **Previous (~30 candles):** Post-failed breakdown at the daily range low / `1D.zones.BUY_1`, price based then ground higher on relatively weaker volume (healthy if sellers are absent), regaining acceptance over `4H.zones.NEUTRAL`. The reclaim leg established `4H.active.H_CHOCH` (early structural shift) while consolidating around/above `4H.zones.SELL_1` (role-flip behavior).
* **Current (~5 candles):** Price is now retesting the **range high cluster**: `4H.major.H_MAJOR` ↔ `1D.major.H_MAJOR`, with immediate overhead friction from the descending `4H_200EMA` (price still slightly below it). Current candle behavior is a `4H_bullish_spinning_top_VC` (not ignition yet). Momentum: `4H_RSI` ~66.5 above `4H_RSI-MA` ~56.1, and price is **above** `4H_9/21/50EMA` and **above** `4H_W_VWAP/M_VWAP` → bullish attempt, but at a “decision point” into HTF resistance.

---

### **1H (1H – TTF)**

* **Previous (~30 candles):** Weekend consolidation transitioned into a trend leg up, reclaiming/holding above `4H.zones.SELL_1` and then breaking through `1H.major.H_MAJOR` (HH/HL sequence), with buyers defending pullbacks above `1H.zones.BUY_2` (overlaps `4H.active.H_CHOCH` zone).
* **Current (~5 candles):** Impulse has carried price into `4H.major.H_MAJOR` / `1D.major.H_MAJOR` retest. Current developing candle prints as `1H_bullish_spinning_top_HVC` (volume >2x `1H_vol_ma20`) **but with topping wick risk** → watch for absorption/exhaustion. Indicators: price is **above** `1H_9/21EMA`, **above** `1H_50EMA`, and **above** `1H_200EMA/SMA200` + `1H_S_VWAP/W_VWAP`; however `1H_RSI` ~76.7 (overbought) warns of mean-reversion risk into `1D.zones.SELL_2`. This is a “trend-up but stretched into HTF supply” tape.

## MACRO CONTEXT
### LAST WEEK

* **US inflation (CPI, Nov; released Thu Dec 18)**

  * Headline CPI: **+0.2% SA over the 2 months (Sep→Nov)**; **+2.7% YoY**.
  * Core CPI (ex-food/energy): **+0.2% SA over 2 months**; **+2.6% YoY**.
  * Over the same 2-month window: **Energy +1.1%**, **Food +0.1%**.
  * 12-month components highlighted in the release: **Energy +4.2% YoY**, **Food +2.6% YoY**.
  * **Data caveat:** October CPI survey collection was missed due to the federal funding lapse; CPI data collection **resumed Nov 14** → higher uncertainty/seasonality distortion risk in “holiday discount” period comparisons.
* **US labor (Weekly Jobless Claims; released Thu Dec 18)**

  * Initial claims (wk ending **Dec 13**): **224k** (**-13k WoW**).
  * 4-wk avg initial claims: **217.5k** (**+0.5k WoW**).
  * Continuing claims (wk ending **Dec 6**): **1.897M** (**+67k WoW**).
* **US demand (Retail Sales, Oct; released Tue Dec 16, delayed)**

  * Headline: **$732.6B**, **~0.0% m/m (virtually unchanged)**; **+3.5% YoY**.
  * Aug–Oct total sales: **+4.2% YoY**.
  * Notables: **Nonstore retailers +9.0% YoY**; **Food services & drinking places +4.1% YoY**.
* **US activity pulse (S&P Global “flash” PMI, Dec; released Tue Dec 16)**

  * Composite: **53.0** (Nov: **54.2**).
  * Services: **52.9** (Nov: **54.1**).
  * Manufacturing: **51.8** (Nov: **52.2**).
* **US consumer (U. Michigan final, Dec)**

  * Sentiment index: **52.9** (Nov: **51.0**).
  * Current conditions: **50.4**; Expectations: **54.6**.
* **US housing (Existing Home Sales, Nov; released Fri Dec 19)**

  * Sales: **4.13M SAAR** (**+0.5% m/m**, **-1.0% YoY**).
  * Median price: **$409,200** (**+1.2% YoY**).
  * Inventory: **1.43M** (**-5.9% m/m**, **+7.5% YoY**); **4.2 months** supply.
* **Global central banks (risk/FX spillovers into US session)**

  * **BoE:** Bank Rate **cut 25bp to 3.75%**.
  * **ECB:** Held policy rates (Deposit **2.00%**, Main refi **2.15%**, Marginal lending **2.40%**).
  * **BoJ:** **Raised** policy rate (overnight call rate target) to **~0.75%** (from **0.50%**).
* **Fed / political overhang**

  * Fed speakers continued to lean **“pause/hold for months”** after the 2025 easing cycle; tariff-related inflation uncertainty remains a stated concern (Trump policy channel + data-quality caveats).

---

### THIS WEEK

* **Holiday/market structure (liquidity + timing risk)**

  * **Wed Dec 24:** US equities **early close** (NYSE/Nasdaq) **1:00pm ET**.
  * **Thu Dec 25:** **US markets closed** (Christmas).
  * **Bond market:** recommended **2:00pm ET** close on **Dec 24**.
  * **Federal offices:** Trump ordered **federal offices closed Dec 24 and Dec 26** (markets still open) → expect thinner staffing/liquidity + headline sensitivity.
* **Key US macro releases (all times ET)**

  * **Tue Dec 23**

    * **08:30** — **GDP (Q3 2025, “advance/initial” estimate)** + Corporate Profits (preliminary) *(shutdown-delayed GDP cycle; high sensitivity for rates/USD)*.
    * **08:30** — **Durable Goods (Oct, advance report)** *(shutdown-shifted release date)*.
    * **09:15** — **Industrial Production & Capacity Utilization (Oct & Nov estimates)** *(shutdown catch-up; watch cyclicals / real yields)*.
    * **10:00** — **Conference Board Consumer Confidence (Dec)** (last published: **Nov 88.7**; Present Situation **126.9**, Expectations **63.2**).
  * **Wed Dec 24**

    * **08:30** — **Weekly Jobless Claims** (wk ending **Dec 20**) **rescheduled** due to Christmas week.
* **Context note:** multiple releases remain **rescheduled/condensed** from the 2025 funding lapse → higher probability of “surprise prints” and lower signal-to-noise.

---

### MACRO ANALYSIS

Holiday liquidity + a **data-dense Tuesday (GDP/IP/Durables/Confidence)** makes today’s US session prone to **positioning-driven moves** and **outsized reactions** to surprises. The key cross-asset hinge is the **rates/USD impulse**: a hotter growth/inflation mix tends to push **yields & USD up** (headwind for **gold** and often for **high-beta risk** like **BTC/ETH**), while softer growth/confidence tends to pull **yields down** (supportive for **gold**, and can be supportive for **SPX/BTC** if the market interprets it as “Fed easing runway” rather than recession risk). Trump/tariff headlines remain an asymmetric volatility catalyst because they directly feed the **inflation risk premium**.

#### BTC & ETH

BTC/ETH still behave as **high-beta liquidity/risk proxies** in US hours: they tend to track **Nasdaq/SPX risk appetite** and **USD liquidity conditions**. Thin liquidity into Christmas increases the chance of **stop-runs/long wicks** around key levels, especially if Tuesday’s GDP/rates reaction is sharp. A **yields-up** impulse is the main near-term headwind; a **yields-down** impulse can help crypto rebound provided equity risk doesn’t flip into “growth scare.”

  
# TRADING PLAN FOR 1H_TTF (Trigger • Location • Context)

## SHORT

### **ORANGE_A — Short reversal at `1D.zones.SELL_2` → extension to `1D.zones.SELL_1`**

* **Context**: Weekly is still bearish (price below `1W_9/21/50EMA`, weak `1W_RSI`), while 1H/4H are rallying into the **daily supply band**. The daily up-leg is on lighter relative volume (`1D_VC` vs `1D_vol_ma20`), and 1H is **overbought** (`1H_RSI` ~76.7) → prime conditions for a **confirmed** reversal *only after* structure breaks.
* **Location**: First reaction zone `1D.zones.SELL_2`, stretch target `1D.zones.SELL_1` (and watch interaction with descending `1D_50EMA` overhead).
* **Trigger**: **Mandatory** `1H_L_MSB` (TTF trend death) after a failed push into `1D.zones.SELL_2` (ideally sweep + close back below), confirmed by bearish CVD shift + bearish VPA (sell-side ignition HVC on the break). 
* **Invalidation**: Acceptance/hold above `1D.zones.SELL_1` (failed reversal thesis).
* **Setup Priority**: **A**

---

### **PURPLE_A — Short fade with `H_FSB` at `4H.major.H_MAJOR` / `1D.major.H_MAJOR` → extension to `1D.zones.SELL_2`**

* **Context**: This is a **range-high fade**: price is pressing into `4H.major.H_MAJOR` / `1D.major.H_MAJOR` with elevated 1H RSI and potential waning follow-through. We do *not* short strength—only after a failed break (FSB) confirms lack of commitment.
* **Location**: Failure zone = wick/sweep above `4H.major.H_MAJOR` / `1D.major.H_MAJOR` then close back below; first downside magnet `1D.zones.SELL_2` (as a “return-to-band” area).
* **Trigger**: `1H_H_FSB` (or clear 15m failed breakout) + LTF bearish divergence, then `15m_L_MSB` back into prior range; enter on the retest of the failed-break level with weak buy volume.
* **Invalidation**: Clean acceptance above `4H.major.H_MAJOR` followed by continued HH/HL on 1H (do not fight ignition).
* **Setup Priority**: **A-**

---

### **PINK_A — Short momentum scalp below `1H_S_VWAP` + `1H_9/21EMA` after failed retest near the “BOS gate”**

* **Context**: Fast tactical short only if the market flips from trend-up into **intra-session risk-off**: loss of `1H_S_VWAP` + `1H_9/21EMA` with rolling momentum and CVD sell pressure. **Note:** `1D.active.H_BOS` is not provided in Key Levels; treat the nearest actionable “gate” as the `1D.major.H_MAJOR` / `4H.major.H_MAJOR` rejection cluster.
* **Location**: Below `1H_S_VWAP` with price failing to reclaim `1H.major.H_MAJOR` (as the nearest major pivot).
* **Trigger**: `15m_L_BOS/MSB` → confirms bearish continuation; enter on the first weak retest into `1H_S_VWAP` / `1H_9/21EMA` from below (bearish crossover preferred).
* **Invalidation**: Reclaim and hold back above `1H_S_VWAP` + `1H_9/21EMA` (scalp thesis dead).
* **Setup Priority**: **B**

---

### **RED_A — Short breakdown below `1H.major.L_MAJOR` / `1D.session.PDL` / `4H.zones.NEUTRAL`**

* **Context**: This is the “trend failure” path. If price loses the mid-range supports, the bounce is likely over and downside continuation becomes probable. We require **strong bearish VPA** (sell ignition HVC) and CVD confirmation—no guessing.
* **Location**: Breakdown cluster `1H.major.L_MAJOR` + `1D.session.PDL` + `4H.zones.NEUTRAL`.
* **Trigger**: `1H_L_BOS` through the cluster on bearish HVC + falling CVD → enter on a low-volume retest from below with LTF confirm (`15m_L_MSB/BOS`).
* **Invalidation**: Sharp reclaim back above `4H.zones.NEUTRAL` and `1D.session.PDL` with bullish structure restoration (stand down).
* **Setup Priority**: **B**

---

## LONG

### **WHITE_A — Long continuation on deeper pullback to `1H.zones.BUY_1/2` while above `1H_50EMA`**

* **Context**: Primary “buy-the-dip” plan while 1H trend remains intact and price holds above `1H_50EMA`, `1H_S_VWAP`, and supportive 4H structure (`4H.active.H_CHOCH`). Given current extension/RSI, the *disciplined* play is waiting for a pullback, not chasing highs.
* **Location**: Demand band `1H.zones.BUY_2` → `1H.zones.BUY_1`, with confluence from the reclaimed higher-TF pivot (`4H.active.H_CHOCH`) and VWAP support zone.
* **Trigger**: Pullback on **decreasing** volume (vs the impulse), then `15m_H_MSB` realigning bullish; enter on the low-volume retest of the LTF flip / first `15m_H_BOS` continuation with rising CVD.
* **Invalidation**: Acceptance below `4H.zones.NEUTRAL` / `1D.session.PDL` (trend structure compromised → defer to RED_A/YELLOW_A paths).
* **Setup Priority**: **A+**

---

### **BLUE_A — Long fade on `L_FSB` at `1H.major.L_MAJOR` / `1D.session.PDL` → extension to `4H.zones.NEUTRAL`**

* **Context**: Only if we see a **stop-run** below support that fails to follow through (classic liquidity sweep). This keeps you out of emotional dip-buying and forces confirmation.
* **Location**: Sweep zone around `1H.major.L_MAJOR` and `1D.session.PDL`, with rebound targeting `4H.zones.NEUTRAL` as first mean-reversion magnet.
* **Trigger**: Wick below then reclaim (FSB) + `15m_H_MSB` back above the swept level; confirm with bullish divergence / CVD turn; enter on the first successful retest of reclaimed support.
* **Invalidation**: Acceptance below `1H.major.L_MAJOR` (no reclaim) → do not fade; switch to breakdown playbook.
* **Setup Priority**: **B+**

---

### **TEAL_A — Long momentum scalp while holding above `1H_S_VWAP` + `1H_9EMA` and the breakout pivot**

* **Context**: Tactical continuation only if momentum remains clean: price holds above VWAP/EMAs and pullbacks stay weak (low volume). **Note:** `1H.active.H_BOS` isn’t defined; use the nearest actionable continuation pivot = hold above `1H.major.H_MAJOR` while VWAP/EMAs rise.
* **Location**: Above `1H.major.H_MAJOR` with `1H_S_VWAP` support; aim is continuation into/through the `4H.major.H_MAJOR` / `1D.major.H_MAJOR` cluster.
* **Trigger**: `15m_H_BOS/MSB` on a retest of the pivot with bullish VPA (ignition HVC preferred) + rising CVD; enter on shallow retest (no deep backfill).
* **Invalidation**: Loss of `1H_S_VWAP` + loss of `1H_9/21EMA` with bearish structure (stand down; don’t “hope-hold”).
* **Setup Priority**: **B**

---

### **GREEN_A — Long breakout above `1D/4H.major.H_MAJOR` and sustain above `1D.zones.SELL_2`**

* **Context**: Continuation breakout trade **only** if we get true commitment (not a wick). Because we’re near HTF resistance, we demand bullish ignition + CVD confirmation and then a clean retest.
* **Location**: Break/acceptance above `4H.major.H_MAJOR` + `1D.major.H_MAJOR`, holding above `1D.zones.SELL_2`.
* **Trigger**: `1H_H_BOS` close/acceptance with bullish HVC and rising CVD → low-volume retest; enter after `15m_H_MSB/BOS` confirms the retest is defended.
* **Invalidation**: Failed retest (acceptance back below `4H.major.H_MAJOR` / `1D.major.H_MAJOR`) or immediate bearish `1H_CHOCH` after entry.
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

