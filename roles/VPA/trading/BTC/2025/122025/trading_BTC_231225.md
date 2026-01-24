# CONTEXT: 
## TRADER CONTEXT: 
Today: Today is Tuesday 23rd of December 2025, we are in London session, 2 hours until US session. We have Durable Goods MoM + GDP Growth Rate Estimate as major data/macro event released today with details outlined as below. Refers to `MACRO CONTEXT` for the rest of the macro events this week.  

Last month: We have officially passed October + November which was supposed to be bullish month for BTC and crypto in terms of seasonality during a bull cycle year, however we got the opposite of that: largest crypto liquidation sell off and continuation of weekly downtrend breaking bullish structure for the cycle despite soft CPI + Inflation data print + resolution on China-US tariffs.

This month: Marked the end of Quantitative Tightening cycle from the FED and market was reacting to 25bps rate cut from FOMC last week.

This week: Chirstmas holiday week with macro data released for as following: 
```markdown
### Today’s key US macro prints (Tue Dec 23, 2025)

**1) Durable Goods Orders (Oct 2025, m/m)**

* **Headline new orders:** **-2.2%** to **$307.4B** (pullback after Sep increase).
* **Ex-transportation:** **+0.2%**
* **Ex-defense:** **-1.5%**
* **Transportation equipment:** **-6.5%** to **$103.9B** (main drag).
* Market expectation context: economists were looking for roughly **-1.5%** headline (so the print is weaker-than-expected). 

**2) GDP “revision” (Q3 2025 — BEA Initial Estimate released today due to shutdown delays)**

* **Real GDP (SAAR): +4.3%** (vs **+3.8%** in Q2). 
* **Real final sales to private domestic purchasers:** **+3.0%** (cleaner demand signal than headline GDP). 
* **Inflation inside GDP:**

  * **PCE price index:** **+2.8%**; **core PCE:** **+2.9%**
  * **Gross domestic purchases price index:** **+3.4%** 
* BEA note: this “initial estimate” **replaces the usual advance + second estimate** because of the shutdown. 

---

## Implications for today’s trading markets (BTC/ETH, SP500, Gold)

### Cross-market rates impulse (the “master switch”)

* **GDP is clearly “hot” (4.3%) and price indices inside GDP are firmer (PCE 2.8 / core 2.9; purchases 3.4)** → *rates can reprice higher* (hawkish tilt), especially if desks treat this as confirmation the economy ran stronger than assumed into Q4. 
* **Durable goods headline is weak (-2.2%) but ex-transport is positive (+0.2%)** → mixed: looks more like **transport volatility** than broad collapse, yet still a *growth/mfg soft patch* signal. 

Net: **macro mix is “strong growth + sticky-ish prices”** (GDP) vs **“manufacturing wobble”** (durables). In thin holiday liquidity, the **rates/FX reaction** can dominate price action more than the data itself.
```

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
      H_MAJOR: 90.6
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
      NEUTRAL: 87.5
    session:
      PDH: 90.6
      PDL: 87.9
    active:
      H_FSB: 90.4
    inactive:
      L_BOS: 87.7
      L_FSB: 85.2

  4H:
    major:
      H_MAJOR: 90.6
      L_MAJOR: 86.6
    sr:
      {}
    poc:
      POC_1: 92.4
      POC_2: 88.1
      POC_3: 86.4
      POC_4: 82.2
    zones:
      SELL_1: 88.8-89.7
      BUY_1: 85.2-86.0
    active:
      H_FSB: 90.4
    inactive:
      H_CHOCH: 89.4
      L_FSB: 85.2

  1H:
    major:
      H_MAJOR: 88.0
      L_MAJOR: 86.6
    sr: {}
    poc: {}
    zones:
      SELL_1: 87.9
      BUY_1: 87.0
      NEUTRAL: 87.6
    active:
      L_FSB: 87.1
    inactive:
      L_BOS: 87.9

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

### Weekly (1W – Super-HTF Structure)

* **Previous (~30 candles):** Post-`ALL.ath` / `1M.major.H_MAJOR` distribution, then weekly trend damage via `1W.active.L_MSB` → accelerated sell-off that **confirmed** `1W.active.L_BOS` (weekly bull structure broken). That sell leg pushed price down through the historic dynamic bull support band (ascending `1W_50EMA/MA`) and into **monthly demand** at `1M.zones.BUY_2`, with acceptance toward `1M.poc.POC_4` / `1M.sr.SR_4`. Supply remains layered overhead: `1W.zones.SELL_3` then higher `1W.zones.SELL_2`.
* **Current (~5 candles):** Multi-week basing just above/around `1W.sr.SR_3` and `1W.poc.POC_4`, still **under** `1W.zones.SELL_3`. Weekly bias remains **recovery-attempt inside a larger corrective regime** while price is below the broken bull support (`1W_50EMA/MA`) and the prior structural break `1W.active.L_BOS`. (No weekly chart provided here; this is anchored to your HTF description + key levels.)

---

### Daily (1D – HTF for intraday)

* **Previous (~30 candles):** Strong downtrend into `1W.major.L_MAJOR` (monthly demand region) culminated in an absorption `1D_bearish_hammer_HVC` (capitulation signature) with deeply oversold `1D_RSI` (<25). From that base, price formed a `1D_ascending_wedge` recovery, then broke down with `1D.inactive.L_BOS` toward `1D.zones.BUY_1`, before reclaiming trend supports (reclaim of `1D_9EMA` + `1D_W_VWAP`) and rotating back up into the range top.
* **Current (~5 candles):** Retest/stop-run near `1D.major.H_MAJOR` rejected via `1D.active.H_FSB` printed as `1D_bearish_doji-long-upper-wick_VC` (clear supply response). Follow-through is rotating back down toward `1D.session.PDL` and the mid/lower acceptance area around `1D.sr.SR_3` / `1D.inactive.L_BOS`, with the nearby “magnet” still being `1D.poc.POC_3` on any mean-reversion bounce. Bias: **bearish-to-neutral** while below `1D.sr.SR_2` and below the rejection complex at `1D.major.H_MAJOR`.

---

### 4H (4H – HTF for 1H)

* **Previous (~30 candles):** Failed breakdown/reversal behavior from the lower range led to a low-volume drift upward into the **key confluence**: `4H/1D.major.H_MAJOR` + `1D.zones.SELL_2` + descending `4H_200MA/EMA`. Rejection printed `4H_bearish_spinning-bar_HVC` (effort + stall), then price began rotating back toward the mid-range.
* **Current (~5 candles):** Post-rejection impulse drove into/through `4H.zones.NEUTRAL` with price now behaving as **mid-range acceptance / pivot battle**. Overhead friction: `4H.poc.POC_2` and the underside of `4H.zones.SELL_1`. Below, the next demand/acceptance shelf is `4H.poc.POC_3` then `4H.zones.BUY_1`. 4H bias: **neutral-bearish** unless reclaiming and holding above `4H.zones.NEUTRAL` with improving VPA/CVD.

---

### 1H (1H – TTF)

* **Previous (~30 candles):** Post-rally failure at `1D/4H.major.H_MAJOR` transitioned into a strong sell sequence that produced `1H.inactive.L_CHOCH` followed by `1H.active.L_BOS`, cascading toward the mid-range pivot `4H.zones.NEUTRAL`. The sell leg found responsive buyers at `1H.major.L_MAJOR` (range low defense), but structure remains **lower-high / lower-low** biased until a confirmed bullish structure break occurs.
* **Current (~5 candles):** Price is attempting a corrective pullback from `1H.major.L_MAJOR` back toward `1H.zones.SELL_2` → `1H.zones.SELL_1`, with confluence friction from `1H_S_VWAP` and the descending `1H_9/21EMA` band. While `1H.active.L_BOS` remains intact and price is capped below `1H.zones.SELL_1/2`, treat bounces as **sell-the-rip candidates** unless LTF prints a clean bullish reversal (MSB) and holds above `4H.zones.NEUTRAL`.

---

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

**Session stance:** 4H is **neutral-bearish** around `4H.zones.NEUTRAL`; 1H is **bearish** post `1H.active.L_BOS`. Expect thinner/liquidity-choppy conditions into the holiday window → **demand strict trigger confirmation; no chasing**.

---

### WHITE_A — Short continuation on pullback into 1H supply

* **Context**: Aligned bearish (4H neutral-bearish + 1H bearish). Current move looks like a corrective pullback from `1H.major.L_MAJOR` back into overhead friction (`1H_9/21EMA` + `1H_S_VWAP`). Prefer weak bullish VPA on pullback (decreasing VCs) + bearish CVD rollover before engaging.
* **Location**: PEZ at `1H.zones.SELL_2` → `1H.zones.SELL_1` (LVN supply) with dynamic resistance from `1H_9/21EMA` + `1H_S_VWAP`.
* **Trigger**: LTF creates a bearish rejection sequence: sweep into the zone → **LTF_L_MSB** (realign down) + low-volume retest of the MSB flip zone; CVD turning down confirms.
* **Invalidation**: Acceptance above `1H.zones.SELL_1` **and** sustained hold above `4H.poc.POC_2` (supply reclaimed → pullback thesis breaks).
* **Setup Priority**: **A+**

---

### ORANGE_A — Short reversal from 4H supply (HTF confluence)

* **Context**: Best “sell-the-rip” if price mean-reverts upward into the strongest HTF confluence. We require proof of absorption/weak buyers (no bullish ignition; CVD fails to confirm).
* **Location**: `4H.zones.SELL_1` aligning with the upper rejection complex near `4H/1D.major.H_MAJOR` and the broader supply reference `1D.zones.SELL_2`.
* **Trigger**: On the 1H/15m: print a stop-run into the zone → **TTF_L_MSB** (or decisive CHOCH failure) + bearish follow-through; pullback must be low-volume; CVD rolls over (LHs).
* **Invalidation**: Clean acceptance above `4H.zones.SELL_1` with rising CVD and bullish ignition HVC (don’t fade strength).
* **Setup Priority**: **A**

---

### PURPLE_A — Short fade on failed breakout (FSB at range-top complex)

* **Context**: Range-fade inside neutral-bearish regime: only valid if the push up is **wicky** and unsupported by CVD (classic failed breakout).
* **Location**: Failure pattern at/near `4H.zones.SELL_1` / `4H.poc.POC_2` (overhead supply shelf).
* **Trigger**: 1H prints **H_FSB** behavior (break above then close back below) + LTF_L_MSB confirming sellers regained control; enter the retest from below.
* **Invalidation**: 1H holds above the failed-break level and flips it to support (FSB fails → step aside).
* **Setup Priority**: **B+**

---

### PINK_A — Short momentum scalp under VWAP/EMAs (continuation pressure)

* **Context**: If price cannot reclaim `1H_S_VWAP` and `1H_9/21EMA` and keeps rejecting under `4H.zones.NEUTRAL`, expect momentum “push” legs and shallow retests. This is a **scalp**, not a swing.
* **Location**: Under `4H.zones.NEUTRAL`, using the first pullback rejection under `1H_S_VWAP` / `1H_9/21EMA` as the working area.
* **Trigger**: LTF_L_BOS (continuation) with bearish HVC + falling CVD; enter either on the BOS or the immediate shallow retest (no deep pullback required).
* **Invalidation**: Reclaim + hold above `4H.zones.NEUTRAL` and sustained trade above `1H_S_VWAP` (momentum edge gone).
* **Setup Priority**: **B**

---

### RED_A — Short breakdown below the 1H floor (structural continuation)

* **Context**: “Break-and-retest” continuation if the range floor gives way. Only engage if breakdown shows **clear bearish effort** (no absorption signals at the lows).
* **Location**: Breakdown through `1H.major.L_MAJOR` with acceptance below `4H.zones.NEUTRAL`.
* **Trigger**: Decisive 1H continuation via **1H_L_BOS** + bearish ignition VC; then wait for a low-volume retest of the broken level from below (AEZ via LTF_L_MSB/BOS).
* **Invalidation**: Sharp reclaim back above `1H.major.L_MAJOR` with bullish ignition + rising CVD (classic breakdown failure → don’t fight it).
* **Setup Priority**: **B+**

---

## LONG (Counter-trend / Reversal Conditions Only)

### BLUE_A — Long fade at mid-range pivot (failed breakdown reclaim)

* **Context**: Counter-trend bounce only if sellers show exhaustion near `4H.zones.NEUTRAL` and LTF prints bullish divergence with confirmation (no knife-catching).
* **Location**: Sweep/failed breakdown around `4H.zones.NEUTRAL` and the nearby daily floor reference `1D.session.PDL`.
* **Trigger**: LTF bullish divergence (RSI/CVD) + **LTF_H_MSB** after a sweep; confirm with reclaim/hold above `1H_S_VWAP` before entry.
* **Invalidation**: Acceptance below `4H.zones.NEUTRAL` with bearish HVC and continued negative CVD (support not holding).
* **Setup Priority**: **B-**

---

### TEAL_A — Long momentum scalp on reclaim of key intraday controls

* **Context**: Only if price proves control shift intraday (reclaim VWAP + reclaim micro-structure). Treat as quick mean-reversion toward overhead HVN/POC shelves.
* **Location**: Reclaim above `1H.active.L_BOS` plus hold above `1H_S_VWAP` and `1H_9EMA` (first sign the bounce is real).
* **Trigger**: LTF_H_BOS/MSB on a retest that holds above reclaimed VWAP/EMA with rising CVD.
* **Invalidation**: Immediate failure back below `1H.active.L_BOS` and `1H_S_VWAP` (reclaim was a trap).
* **Setup Priority**: **B**

---

### YELLOW_A — Long major reversal from 4H demand (deep support play)

* **Context**: This is the “real reversal” attempt and requires the most patience. Only consider if price reaches major demand and prints confirmed reversal structure (TTF trend death).
* **Location**: `4H.zones.BUY_1` overlapping the daily structural base `1D.major.L_MAJOR` and the broader demand region `1D.zones.BUY_1`.
* **Trigger**: **TTF_H_MSB** against the bearish trend (confirmed with meaningful volume) → then enter the first low-volume pullback to the flip zone on an LTF bullish trigger.
* **Invalidation**: Continued acceptance below `4H.zones.BUY_1` with sell-side HVC and no CVD recovery (demand failing).
* **Setup Priority**: **A-**

---

### GREEN_A — Long breakout reversal (trend-flip acceptance)

* **Context**: Only valid if the market proves a real bull reclaim (not just a squeeze). This is the “stand aside until confirmed” reversal plan.
* **Location**: Break/acceptance above `1H.major.H_MAJOR` (trend flip on 1H) and then continuation acceptance through the higher ceiling `1D.zones.SELL_2` (major overhead gate).
* **Trigger**: Confirm **1H_H_MSB/BOS** with bullish ignition VC + rising CVD → then low-volume pullback retest; execute on LTF_H_MSB continuation.
* **Invalidation**: Failed acceptance back below `1H.major.H_MAJOR` (or immediate bearish CHOCH after entry) → treat as bull trap.
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

