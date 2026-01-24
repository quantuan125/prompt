# CONTEXT: 
## TRADER CONTEXT: 
Today: Today is Tuesday 13th of January 2026, we are 30 minutes into US session. We had Inflation + CPI as macro data released today. Refers to `MACRO CONTEXT` for the rest of the macro events this week.  

Last month: Marked the end of Quantitative Tightening cycle from the FED and market was reacting to 25bps rate cut from FOMC. Holiday season and low volume/liquidity environment toward the end of the year. 

This week: A return back from holiday season. 

Directive: Price is bearish on weekly timeframe however caution due to multi-week consolidation at monthly support/demand zone within this 1W candle range. Prefers mean-reversion setup with prioritize on trade-based location rather than trend. 

Sentiment: With price action last quarter that have liquidated millions of leveraged crypto traders and enact fears, the general consensus is bearish with hypothesis of the top for the cycle is already set for BTC, and the start of an extended bear market into 2026. `Fear & Greed Index` improve since last month from around 14-20 (EXTREME FEAR) toward 26-40 (FEAR/NEUTRAL) in the current week.  

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
      POC_4: 87.5
      POC_5: 84.2
    zones:
      BUY_2: 89.5
      BUY_1: 73.7
    inactive:
      H_BOS: 109.6

  1W:
    local: 
      H: 96.0
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
      POC_1: 101.7
      POC_2: 94.4
      POC_3: 91.4
      POC_4: 67.4
    zones:
      SELL_1: 114.9
      SELL_2: 106.1
      SELL_3: 99.1
      BUY_1: 85.5
    active:
      L_BOS: 107.3
    inactive:
      L_MSB: 111.9
      H_FSB: 124.5
      L_FSB: 108.6

  1D:
    major:
      H_MAJOR: 94.8
      L_MAJOR: 89.3
    sr:
      SR_1: 93.4
      SR_2: 89.5
      SR_3: 88.4
    poc:
      POC_1: 102.0
      POC_2: 92.5
      POC_3: 90.2
      POC_4: 84.6
      POC_5: 79.7
    zones:
      SELL_1: 94.2
      BUY_1: 88.5-89.6
      BUY_2: 91.8
    session:
      PDH: 92.5
      PDL: 91.0
    active:
      H_BOS:: 96.5
    inactive:
      H_BOS:: 90.6

  4H:
    major:
      H_MAJOR: 92.5
      L_MAJOR: 90.1
    sr:
      {}
    poc:
      POC_1: 95.5
      POC_2: 93.8
      POC_3: 92.0
    zones:
      BUY_1: 93.5
    active:
      H_BOS: 92.5
    inactive:
      H_CHOCH: 91.6

  1H:
    major:
      H_MAJOR: 96.5
      L_MAJOR: 94.6
    sr: {}
    poc: {}
    zones:
      BUY_1: 95.2
      BUY_2: 95.8
    active:
      H_BOS: 94.5
    inactive:
      H_BOS: 92.7

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

* **Previous (~30 candles):** Post-`1M_bullish_channel` distribution under `ALL.ath` → failed push via `1W.inactive.H_FSB` then liquidation leg that **confirmed** `1W.active.L_BOS` (trend damage) through the `1W.major.L_MAJOR` area. Weekly structure transitioned into **range/repair** between `1W.local.L` ↔ `1W.local.H`, with supply overhead still defined by `1W.zones.SELL_3` and larger weekly SRs (`1W.sr.SR_2` / `1W.sr.SR_1`).
* **Current (~5 candles):** Multi-week consolidation inside `1W.local.L` ↔ `1W.local.H` with **weak weekly participation** (`1W_bullish_insidebar_VC`-type behavior; volume below its baseline). Price remains **below** the weekly ST trend band (`1W_9/21EMA` + `1W_50EMA`) while RSI sits **bearish/neutral** (<50), so this is still **a bounce inside a damaged HTF**, not a clean weekly reversal. Key magnets: `1W.poc.POC_3` then `1W.poc.POC_2`.

---

### **Daily (1D – HTF for intraday)**

* **Previous (~30 candles):** Selloff ended with the noted absorption `1D_bearish_hammer_HVC` into weekly/monthly demand influence (base formed above `1W.sr.SR_4` / toward `1W.zones.BUY_1` context). Holiday period compressed into a tight coil, then expansion **up** through `1D.active.H_BOS` (reclaim of prior daily structure). First push stalled under `1D.zones.SELL_1` and topped at `1D.major.H_MAJOR`, then pulled back on **lighter** volume into `1D.zones.BUY_1` (demand) and held.
* **Current (~5 candles):** Daily is **constructive**: price holds above `1D.active.H_BOS` and has reclaimed/held above daily ST MAs (`1D_9/21EMA`) with RSI > 50 (trend-supportive). However, overhead is tight: `1D.zones.SELL_1` → `1D.major.H_MAJOR` (and above that `1W.local.H`). Expect **chop/stop-runs** as liquidity builds around `1D.session.PDH` / `1D.session.PDL` and nearby `1D.poc.POC_2` / `1D.poc.POC_3`.

---

### **4H (4H – HTF for 1H_TTF)**

* **Previous (~30 candles):** Post-rejection from `1D.major.H_MAJOR`, bearish continuation printed into the retest area, then base built above `4H.zones.BUY_1`/`4H.major.L_MAJOR`. Structure shifted with `4H.active.H_CHOCH` and price reclaimed `4H_9/21EMA` + `W_VWAP`, establishing the rising 4H channel bias while holding above `4H.zones.NEUTRAL`.
* **Current (~5 candles):** Current advance is supported by **bullish participation** (`4H_bullish_impulse_HVC`) and RSI > 60, with price above `4H_9/21EMA`, `4H_50EMA`, and VWAPs. But location is **sensitive**: price is pressing the top-of-range node `4H.major.H_MAJOR` / `4H.poc.POC_1` while sitting inside/near `4H.zones.SELL_2`, and the next heavy cap is `4H.zones.SELL_1` (then `1D.zones.SELL_1`). This is **bullish into supply** → prioritize confirmation over anticipation.

---

### **1H (1H – TTF Execution Context)**

* **Previous (~30 candles):** Uptrend from `1H.inactive.L_FSB` → reclaim of `4H.zones.NEUTRAL` and `1H.active.H_CHOCH` confirmed the bullish leg. Price has respected `1H_9/21EMA` and session VWAP (S_VWAP) as dynamic support; pullbacks have generally shown **weaker volume** than pushes (healthy trend behavior).
* **Current (~5 candles):** Price is **compressing** under the 4H ceiling: repeated tests around `4H.major.H_MAJOR` / `1D.session.PDH` with a near-term wick-rejection suggests liquidity grab risk. Trend remains intact while holding above `1H.major.L_MAJOR` and staying supported by `4H.zones.NEUTRAL`, but the immediate environment is **mean-reversion prone** (top-of-range + nearby sell LVNs).


## MACRO CONTEXT
### LAST WEEK

**(Mon Jan 5 → Fri Jan 9, 2026)**

* **Macro data quality caveat:** Post–43-day U.S. federal shutdown data backlog + imputation effects kept “clean signal” confidence lower across inflation/labor prints.
* **Growth/PMIs (U.S.):**

  * **ISM Manufacturing (Dec): 47.9** (prior **49.4**) → contraction.
  * **ISM Services (Dec): 54.4** (prior **52.1**) → expansion.
* **Labor (U.S.):**

  * **ADP private payrolls (Dec): +41k**
  * **JOLTS job openings (Nov): 7.46M** (prior **7.73M**)
  * **Initial jobless claims (wk ending Jan 3): 208k**
  * **Nonfarm payrolls (Dec): +50k; Unemployment: 4.4%**

    * **Avg hourly earnings:** **+0.3% m/m**, **+3.8% y/y**
* **Demand/Inventories:**

  * **Wholesale inventories (Nov): -0.2% m/m**; **wholesale sales: +0.6% m/m**
* **Sentiment / inflation psychology:**

  * **U. Michigan consumer sentiment (prelim Jan): 54.0** (Dec **52.9**)
  * **Inflation expectations:** **1Y 4.2%**, **5Y 3.1%**
* **Policy risk overhang:** Supreme Court signaled **Jan 14** as a potential rulings day while Trump tariff legality remained unresolved → risk premium supported.

### THIS WEEK

**(Mon Jan 12 → Fri Jan 16, 2026; plus next market-closure)**

* **Political / policy risk (Trump vs Fed):**

  * **Fed Chair Powell** disclosed **grand jury subpoenas** threatening indictment tied to testimony on **$2.5B** Fed HQ renovation cost overruns → market focus on **Fed independence risk** and USD credibility premium.
  * **Trump:** countries doing business with **Iran** face a **25% tariff on all trade with the U.S.** (details/legal basis not yet clarified publicly) → trade-war tail risk + potential oil/inflation impulse channel.
* **Inflation (U.S.) — key for rates, USD, and cross-asset risk:**

  * **CPI (Dec, released Tue Jan 13):** **+0.3% m/m**, **+2.7% y/y**
  * **Core CPI (Dec):** **+0.2% m/m**, **+2.6% y/y**
  * Context: prior shutdown distortions expected to unwind; markets anchor on “Fed likely on hold” near-term.
* **Fed policy frame (rates / forward path):**

  * Current fed funds target range: **3.50%–3.75%**
  * NY Fed’s **Williams**: policy “closer to neutral,” **no near-term reason to cut**; sees **2026 GDP 2.5%–2.75%**, inflation peaking **2.75%–3.0%** in 1H26, easing toward **~2.5%** over 2026; **2% in 2027**.
* **High-impact scheduled events (this week):**

  * **Wed Jan 14:** **PPI (Nov)** release (data backlog catch-up).
  * **Wed Jan 14:** **Retail Sales (Nov)** release (data backlog catch-up).
  * **Wed Jan 14:** Supreme Court sits; tariff legality decisions remain a potential “headline shock.”
  * **Thu Jan 15 (10:00 AM ET):** Senate Banking **markup/executive session** on crypto market structure framework (CLARITY / H.R.3633 discussion point) → can shift BTC/ETH regulatory-risk premium intraday.
  * **Thu Jan 15:** **TSMC earnings** (AI/semis bellwether; risk-on sensitivity via Nasdaq/SPX complex).
* **Earnings / positioning:**

  * Street expects **S&P 500 Q4 earnings +8.8% y/y**; earnings season “kickoff” effect amplifies equity index sensitivity to beats/misses (especially banks + AI complex).
* **Precious metals stress signal (risk premium):**

  * **Gold** printed record territory (Mon Jan 12): spot **$4,609.58** (intraday record **$4,629.94**); Feb futures settlement **$4,614.70** — consistent with safe-haven demand on Fed-independence + tariff uncertainty.
* **Holiday / market liquidity:**

  * **Mon Jan 19, 2026: NYSE closed (Martin Luther King Jr. Day)** → expect liquidity effects into Fri Jan 16 close + potential gap risk into Tue reopen.

### MACRO ANALYSIS

#### OVERALL CROSS-MARKETS

For today’s U.S. session (Tue **Jan 13, 2026**), the “base case” is **rates-on-hold** after an in-line **Dec CPI (2.7% y/y; core 2.6% y/y)**, but the **dominant tail risk** is political: **Fed independence under direct pressure** (Powell subpoena/indictment threat) plus **fresh tariff escalation** (Iran-linked **25%** tariff threat) with **Supreme Court tariff legality** potentially surfacing **Jan 14**. Historically this creates a **barbell**: safe-haven bid (gold, sometimes BTC when USD confidence is questioned) alongside fragile risk-on (SP500/crypto) that can unwind fast if headlines push **real yields up** or trigger broad de-risking.

#### BTC & ETH

* **Macro-sensitive but narrative-flexible:** tends to trade **risk-on with equities** during stable policy regimes, yet can behave like a **USD-alternative** during credibility shocks (Fed/policy crisis).
* **This week’s crypto-specific macro catalyst:** Senate Banking **Thu Jan 15** CLARITY/market-structure action can **reduce regulatory overhang** (bullish impulse) or inject uncertainty depending on amendments/headlines.
* **Primary risk:** sudden equity de-risking from tariff/legal shocks tends to spill into BTC/ETH via correlated risk books.

  
# TRADING PLAN FOR 1H_TTF (Trigger • Location • Context)

## SHORT

### **ORANGE_A — Short reversal at 4H sell LVN (extension trap)**

* **Context**: Intraday trend is up, but we’re trading **into stacked HTF supply** (`4H.zones.SELL_1` → `1D.zones.SELL_1` → `1D.major.H_MAJOR`). If the push into that band shows **weak follow-through** (stalling bodies, rising sell-pressure on CVD, RSI divergence), we treat it as distribution/absorption (do **not** front-run).
* **Location**: `4H.zones.SELL_1` confluence with daily cap `1D.zones.SELL_1` / `1D.major.H_MAJOR`.
* **Trigger**: **TTF_L_MSB** (1H major swing break down) after a sweep/failed hold at the location + bearish VPA (sell-side HVC/SHVC or clear absorption then breakdown).
* **Invalidation**: Clean acceptance/hold above `4H.zones.SELL_1` with bullish ignition behavior.
* **Setup Priority**: `A-`

---

### **PURPLE_A — Short fade of 4H top (failed break)**

* **Context**: Range fade *only if* the 1H uptrend **fails to convert** the ceiling into support. We want a clear **H_FSB** style event: wick above `4H.major.H_MAJOR` / `1H.major.H_MAJOR` then close back below with CVD rolling over.
* **Location**: `4H.major.H_MAJOR` + `1H.major.H_MAJOR` with `4H.zones.SELL_2` acting as the “line in the sand” for acceptance vs rejection.
* **Trigger**: Sweep → return below the level → **LTF_L_MSB** (15m/5m) confirming lower-high structure; bonus if bearish 9/21EMA roll + loss of S_VWAP.
* **Invalidation**: Reclaim and hold above `1H.major.H_MAJOR` and then hold above `4H.major.H_MAJOR` (no fade).
* **Setup Priority**: `B-`

---

### **PINK_A — Short momentum scalp (loss of VWAP/EMA support)**

* **Context**: Only triggers if the “trend supports” fail (S_VWAP + `1H_9EMA`) **and** price stays heavy below `4H.zones.NEUTRAL` / `1H.major.L_MAJOR` (meaning the dip is not being bought). Expect bearish VPA (increasing red volume on breaks, weak bounces).
* **Location**: Breakdown acceptance below `4H.zones.NEUTRAL` and `1H.major.L_MAJOR`.
* **Trigger**: **LTF_L_BOS/MSB** on the break → low-volume retest from below → continuation with bearish CVD slope.
* **Invalidation**: Sharp reclaim back above `4H.zones.NEUTRAL` and re-hold above S_VWAP (failed breakdown).
* **Setup Priority**: `B`

---

### **RED_A — Breakdown & retest below 1H range low**

* **Context**: This is the “bias flips” short: we need a real structural failure, not chop. Requires decisive sell commitment (bearish HVC/SHVC) and inability to reclaim.
* **Location**: `1H.major.L_MAJOR` with downside magnets at `4H.poc.POC_2` / `4H.major.L_MAJOR` (then `4H.zones.BUY_1`).
* **Trigger**: Confirmed **1H_L_BOS** → low-volume retest of `1H.major.L_MAJOR` from below → **LTF_L_MSB/BOS** continuation.
* **Invalidation**: Reclaim and hold back above `1H.major.L_MAJOR` (especially if it reclaims `4H.zones.NEUTRAL`).
* **Setup Priority**: `B`

---

## LONG

### **WHITE_A — Trend continuation on deep pullback (best RR)**

* **Context**: Primary plan while 4H remains constructive. We want a **controlled pullback** (lower volume vs the prior impulse) into a stacked demand shelf, then realignment.
* **Location**: `1H.major.L_MAJOR` + `1H.zones.BUY_1` + `4H.zones.NEUTRAL` confluence, supported by rising `1H_21/50EMA`.
* **Trigger**: Sweep/hold in the zone → **LTF_H_MSB** (15m/5m) → enter on the low-volume retest / first LTF_BOS up with rising CVD.
* **Invalidation**: Acceptance below `4H.zones.NEUTRAL` and sustained trade below `1H.major.L_MAJOR`.
* **Setup Priority**: `A-`

---

### **BLUE_A — Long fade at 4H demand (failed breakdown)**

* **Context**: Only if we get a liquidation-style push into demand that **fails to follow through** (selling climax → stabilization → reversal structure). Must see bullish divergence/absorption cues *then* structure confirmation (no blind catching).
* **Location**: `4H.zones.BUY_1` with extension space toward `4H.major.L_MAJOR` / `1D.session.PDL`, and deeper contingency into `1D.zones.BUY_1`.
* **Trigger**: Liquidity sweep below the level → reclaim → **LTF_H_MSB** back into range; prefer a clear reduction in sell volume on the retest.
* **Invalidation**: Acceptance below `4H.major.L_MAJOR` (then this becomes a “wait for YELLOW_A” environment).
* **Setup Priority**: `B+`

---

### **TEAL_A — Long momentum scalp (hold above VWAP/EMA)**

* **Context**: Only valid if price remains supported above S_VWAP and `1H_9EMA` and keeps holding above `4H.zones.NEUTRAL`. This is a **continuation scalp**, but do not chase into the ceiling—enter only on pullback + confirmation.
* **Location**: Pullback support while above `4H.zones.NEUTRAL`, aiming back toward `4H.major.H_MAJOR` (and potentially `1H.major.H_MAJOR` if breakout conditions appear).
* **Trigger**: **LTF_H_BOS/MSB** on a pullback reclaim (bullish 9/21EMA alignment) + rising CVD; ideally lower pullback volume than the prior push.
* **Invalidation**: Loss of S_VWAP + failure to reclaim `4H.zones.NEUTRAL`.
* **Setup Priority**: `B`

---

### **GREEN_A — Breakout & retest above 1H/4H highs**

* **Context**: Continuation requires *real* buy commitment (ignition VPA + CVD confirmation). Given overhead daily supply, this is **high selectivity**: breakout must hold and backtest must be weak (no heavy sell response).
* **Location**: Break/acceptance above `1H.major.H_MAJOR` and `4H.major.H_MAJOR`, then first retest from above.
* **Trigger**: Confirmed **1H_H_BOS** + bullish HVC/SHVC → low-volume pullback → **LTF_H_MSB/BOS** continuation entry.
* **Invalidation**: Failed retest (acceptance back below `4H.major.H_MAJOR`) or immediate 1H bearish structure flip.
* **Setup Priority**: `B`

  
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

