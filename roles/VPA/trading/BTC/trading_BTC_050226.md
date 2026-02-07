# CONTEXT: 
## TRADER CONTEXT: 
Today: Today is Thursday 5th of February 2026, we are in late London session, about 2 hours prior to US session open. We have JOLTs opening as the only major macro data released today. Refers to `MACRO CONTEXT` for the rest of the macro events this week.  

Last month: Marked the end of Quantitative Tightening cycle from the FED and market was reacting to 25bps rate cut from FOMC. Holiday season and low volume/liquidity environment toward the end of the year. 

This week: A return back from holiday season, and continuation of the bearish trend after the end of last year bullish cycle. 

Directive: Price is bearish on both weekly and daily, prioritize shorts, however caution due to price at 1M range low + demand with sell-off overextension at all timeframes. 

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
      L_MAJOR: 86.1
    sr:
      SR_1: 93.4
      SR_2: 89.5
      SR_3: 88.4
    poc:
      POC_1: 95.5
      POC_2: 92.5
      POC_3: 90.2
      POC_4: 82.8
      POC_5: 78.8
    zones:
      SELL_1: 80.3
    session:
      PDH: 77.0
      PDL: 71.9
    active:
      L_BOS: 86.1
    inactive:
      L_MSB: 89.3

  4H:
    major:
      H_MAJOR: 72.0
      L_MAJOR: 70.2
    sr:
      {}
    poc:
      POC_0: 86.4
      POC_1: 75.2
      POC_2: 73.8
      POC_3: 70.9
    zones:
      SELL_1: 76.2
      SELL_2: 73.0
    active:
      L_BOS: 74.6
    inactive:
      L_BOS: 86.1

  1H:
    major:
      H_MAJOR: 70.9
      L_MAJOR: 69.2
    sr: {}
    poc: {}
    zones:
      SELL_1: 69.9
      SELL_2: 68.8
    active:
      L_BOS: 69.2
    inactive:
      L_BOS: 71.9
  
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

* **Previous (~30 candles):** `1M.active.H_FSB` topping from the prior bull leg → distribution and rollover below `1M.sr.SR_1` / `1M.poc.POC_2`, then heavy markdown into the weekly base `1W.major.L_MAJOR` (**~80.6k**) with multiple failed recoveries capped at `1W.major.H_MAJOR` (**~97.9k**) / `1W.poc.POC_2` (**~94.4k**) and supply `1W.zones.SELL_1` (**~90.8k**). Weekly bias shifted bearish after the confirmed `1W.active.L_BOS` through `1W.major.L_MAJOR`.
* **Current (~5 candles):** Acceleration lower after losing `1W.major.L_MAJOR` with a broad 1W bearish continuation sequence; price now pressing the *monthly demand shelf* `1M.zones.BUY_1` (**~73.7k**) / `1M.major.L_MAJOR` (**~74.5k**). Trend context is **bearish** with price far below `1W_9EMA` (**~85.0k**) < `1W_21EMA` (**~93.0k**) < `1W_50EMA` (**~95.2k**). `1W_M_VWAP` (**~72.7k**) overhead; next major structural magnet/support is `1W_200EMA` (**~68.0k**) then `1M.poc.POC_5` (**~67.0k**). Momentum: `1W_RSI` (**~28.7**) below `1W_RSI-MA` (**~38.6**) = bearish, mildly oversold (needs PA confirmation to fade).

---

### **Daily (1D – HTF for intraday)**

* **Previous (~30 candles):** Counter-trend daily recovery attempt topped below `1W.major.H_MAJOR` (**~97.9k**) then trend death sequence: a confirmed `1D.inactive.L_MSB` followed by `1D.active.L_BOS` (bear trend continuation), stepping down through major pivots/POCs and failing to reclaim `1D.poc.POC_3` (**~90.2k**) / `1D.poc.POC_4` (**~82.8k**). Sell legs generally carried stronger volume than bounces (bearish VPA).
* **Current (~5 candles):** Daily continues to grind **below** the monthly shelf `1M.zones.BUY_1` (**~73.7k**) / `1M.major.L_MAJOR` (**~74.5k**) and has broken beneath session ref `1D.session.PDL` (**~71.9k**) with `1D_bearish_continuation_VC`. Bear structure is reinforced by stacked MAs: `1D_9EMA` (**~77.9k**) < `1D_21EMA` (**~83.1k**) < `1D_50EMA` (**~87.5k**) well below `1D_200EMA` (**~96.8k**); VWAPs above price: `1D_W_VWAP` (**~74.8k**) & `1D_M_VWAP` (**~75.1k**). `1D_RSI` (**~19.9**) = *deep oversold* → **do not buy without structure** (need 1H/TTF reversal confirmation). Downside magnet: `1M.poc.POC_5` (**~67.0k**).

---

### **4H (4H – HTF for 1H)**

* **Previous (~30 candles):** Clean bearish swing structure with repeated LHs under `4H.zones.SELL_2` (**~74.6k**) and `4H.zones.SELL_1` (**~77.0k**), culminating in the latest `4H.active.L_BOS` through **~`4H.zones.SELL_2` / `4H.major` base** (trend continuation). Multiple sell legs printed with heavier volume than pullbacks (bearish VPA), while price stayed pinned below `4H_W_VWAP` / `4H_9EMA`.
* **Current (~5 candles):** Price is now probing beneath `4H.major.L_MAJOR` (**~70.2k**) and below `1D.session.PDL` (**~71.9k**) with RSI extremely stretched: `4H_RSI` (**~19.6**) < `4H_RSI-MA` (**~29.6**). All key dynamics overhead: `4H_9EMA` (**~72.4k**), `4H_21EMA` (**~74.9k**), `4H_W_VWAP` (**~75.0k**), `4H_M_VWAP` (**~75.4k**). Nearest magnets/targets are `4H.poc.POC_3` (**~70.9k**) (retest/flip area) then `1M.poc.POC_5` (**~67.0k**). **Risk note:** oversold is not a long signal—wait for a 1H/TTF structure break.

---

### **1H (1H – TTF for execution)**

* **Previous (~30 candles):** Persistent 1H downtrend capped by `1H_9EMA` (**~70.8k**) + `1H_S_VWAP` (**~71.1k**) and failing beneath `1H.zones.SELL_1` (**~72.3k**) / `1H.inactive.L_BOS` (**~72.9k**). Sell-side dominance led to the latest `1H.active.L_BOS` through `1D.session.PDL` (**~71.9k**) and pressure into the 1H/4H base.
* **Current (~5 candles):** Retest-and-reject behavior near the broken `1H.active.L_BOS` (**~71.9k**) followed by renewed sell pressure through `1H.major.L_MAJOR` (**~70.1k**) / `4H.major.L_MAJOR` (**~70.2k**). Price remains below all key trend controls: `1H_9EMA` (**~70.8k**) < `1H_21EMA` (**~71.9k**), and below `1H_S_VWAP` (**~71.1k**) & `1H_W_VWAP` (**~74.9k**). Momentum bearish but stretched: `1H_RSI` (**~27.7**) below `1H_RSI-MA` (**~31.6**) with **possible bullish divergence** (only actionable after a confirmed 1H/TTF reversal structure). Downside magnet remains `1M.poc.POC_5` (**~67.0k**).

## MACRO CONTEXT

### LAST WEEK

* **Fed (Jan 28 FOMC):** Policy rate **held at 3.50%–3.75%**; tone stayed **inflation-cautious**, with policy discussion still framed around **tariff-driven price risks** and “data dependence.”
* **US inflation pipeline (PPI, Jan 30 for Dec 2025):** **Hot print** reinforced “sticky inflation” risk.

  * **PPI Final Demand MoM:** **+0.5% actual** vs **+0.2% exp** (prior **+0.4%**)
  * **Core PPI MoM:** **+0.7% actual** vs **+0.2% exp** (prior **0.0%**)
* **Macro backdrop:** Inflation surprise + Fed caution kept **rates sensitivity elevated** (equities/crypto more reactive to yields and USD).

### THIS WEEK

* **US politics / fiscal (shutdown overhang):**

  * **Partial government shutdown ended (Feb 3)** after Trump signed a spending bill; **DHS funded via a short-term CR to Feb 13**, keeping a **near-term re-shutdown headline risk** on the tape.
  * **Data disruption:** BLS labor releases were impacted/rescheduled; **Jan Employment Situation moved to Feb 11** (instead of Feb 6). **Dec JOLTS was also affected** (timing risk remains a volatility driver for rates).
* **US growth pulse (stronger real-economy signals):**

  * **ISM Manufacturing PMI (Feb 2, Jan):** **52.6 actual** vs **48.5 exp** (prior **47.9**) → big upside surprise (re-prices “hard landing” odds down; can keep Fed cautious on cuts).
  * **ISM Services PMI (Feb 4, Jan):** **53.8 actual** vs **53.5 exp** (prior **53.8**, revised) → steady expansion.
* **US labor pulse (softer private hiring):**

  * **ADP Employment Change (Feb 4, Jan):** **+22K actual** vs **+46K exp** (prior **+37K**) → cooling hiring signal, but market impact amplified by **official NFP delay**.
* **“PPI MoM today” (latest relevant print impacting today’s session):**

  * **Eurozone PPI MoM (released Feb 4):** **-0.3% actual** vs **-0.3% exp** (prior **+0.7%**) → supports disinflation narrative in Europe (matters via **EUR/USD → DXY → global risk & gold**).
  * **US PPI next official release:** **Jan 2026 PPI scheduled Feb 27** (still a key upcoming inflation checkpoint after last week’s hot Dec print).
* **Global central banks (rates/FX volatility into US hours):**

  * **BoE (Feb 5):** Market focus on **hold expectations at 3.75%** + guidance (GBP/UK rates spillover into USD curve).
  * **ECB (Feb 5):** Broad expectation for **rates held** (watch language on timing/conditions for future easing).
* **Rates supply / liquidity:**

  * **US Treasury Quarterly Refunding (Feb 4):** **$125B** coupon issuance; next week auctions flagged: **$58B 3Y (Feb 10), $42B 10Y (Feb 11), $25B 30Y (Feb 12)** → can influence term premium/yields (risk assets & gold sensitivity).
* **Tech / AI / risk sentiment (cross-asset driver):**

  * **Semis/AI valuation & guidance risk** remained a key swing factor (large-cap tech earnings week incl. **Amazon after close Feb 5**). Risk sentiment shifts here tend to transmit quickly to **BTC/ETH** and **S&P**.

### MACRO ANALYSIS

#### OVERALL CROSS-MARKETS

Today’s BTC–S&P–Gold playbook is still **rates + USD + “risk mood.”** Last week’s **hot US PPI** and a **Fed hold** keep markets sensitive to any catalyst that moves **real yields** (Treasury supply headlines, central-bank guidance, and delayed US data creating “information gaps”). This week’s **strong ISM** tilts toward firmer growth (hawkish for rates), while **soft ADP** leans the other way—net result: **higher volatility around yields**. In that environment, **S&P and BTC/ETH** typically move together (risk-on/off), while **gold** can outperform when uncertainty rises (policy headlines, shutdown aftershocks, growth scares) but may stall if yields spike.

#### BTC & ETH

* BTC/ETH remain a **high-beta risk proxy** in this regime: supportive when **USD softens / yields fall**, vulnerable when **yields rise** or tech de-risks.
* Watch for **macro-driven liquidation windows** around central bank headlines (ECB/BoE) and US rates moves; the **official data delay** can exaggerate swings on partial signals.

# TRADING PLAN FOR 1H_TTF (Trigger • Location • Context)

## SHORT

### **WHITE_A — Short continuation on retest of broken base**

* **Context**: Market State **1 (Aligned Bear Trend)**: 1D/4H/1H all bearish; price below `1H_S_VWAP` + `1H_9EMA` and far below `1H_W_VWAP`; pullbacks have been weak vs sell legs (bearish VPA). Oversold RSI warns against chasing—**wait for the pullback** and LTF confirmation.
* **Location**: Retest cluster `1H.major.L_MAJOR` (**~70.1k**) / `4H.major.L_MAJOR` (**~70.2k**) up into `1H.zones.SELL_2` (**~70.6k**) + dynamic cap `1H_9EMA` (**~70.8k**) / `1H_S_VWAP` (**~71.1k**).
* **Trigger**: LTF (15m) **L_MSB** at/inside the location after a weak pullback (decreasing volume) → then LTF **L_BOS** with falling CVD / bearish VC confirmation.
* **Invalidation**: Clean acceptance & hold back above `1D.session.PDL` (**~71.9k**) **and** sustained reclaim of `1H_S_VWAP` (bear pullback thesis fails).
* **Setup Priority**: **A+**

---

### **PINK_A — Momentum scalp continuation (sell the retest, no reclaim)**

* **Context**: If price stays pinned below `1H_9EMA` / `1H_S_VWAP`, continuation risk stays high; use this only when LTF structure is already bearish and volume expands on breakdown attempts (no “dead-cat” bounce strength).
* **Location**: Under `1H.zones.SELL_2` (**~70.6k**) while below `1H_S_VWAP` (**~71.1k**) and below the broken `4H.major.L_MAJOR` (**~70.2k**).
* **Trigger**: LTF **L_BOS** (continuation) on rising bearish VCs + negative CVD slope; enter on immediate shallow retest that fails (no reclaim above `1H.zones.SELL_2`).
* **Invalidation**: Any sustained reclaim above `1H_S_VWAP` (**~71.1k**) with bullish follow-through (momentum edge gone).
* **Setup Type**: **1C – Momentum Ignition**
* **Setup Priority**: **B**

---

### **RED_A — Break-and-retest continuation below the major base**

* **Context**: Use when sell-side ignition appears (expansion range + volume) and the next pullback is weak (classic bearish VPA: strong impulse, weak retest).
* **Location**: First low-volume retest of broken `1H.major.L_MAJOR` (**~70.1k**) / `4H.major.L_MAJOR` (**~70.2k**) from below; targets pull toward `1M.poc.POC_5` (**~67.0k**).
* **Trigger**: Confirmed 1H continuation pressure (bearish VC sequence) + LTF **L_MSB/BOS** failure at the retest (CVD must not diverge bullishly).
* **Invalidation**: Sharp reclaim back above `1H.major.L_MAJOR` (**~70.1k**) **and** `1H_S_VWAP` (**~71.1k**) (acceptance back into prior value).
* **Setup Priority**: **B**

---

### **PURPLE_A — Short fade (failed break) into overhead supply**

* **Context**: Only if a bounce runs into resistance with **weak bullish VPA** (rising price on falling volume) and/or bearish divergence signals; look for liquidity grab and rejection (FSB behavior).
* **Location**: Sweep/failure near `1H.major.H_MAJOR` (**~72.0k**) into `1H.zones.SELL_1` (**~72.3k**) with `1H_21EMA` (**~71.9k**) acting as the “ceiling”.
* **Trigger**: Wick-through / failed hold above `1H.major.H_MAJOR` + LTF **L_MSB** back below the level (bearish reversal VC confirmation).
* **Invalidation**: Acceptance above `1H.zones.SELL_1` (**~72.3k**) and conversion to support (fade is invalid).
* **Setup Priority**: **B+**

---

### **ORANGE_A — Short reversal after bullish counter-trend recovery**

* **Context**: Only activates if 1H prints a **bullish counter-trend** (HH/HL) and pushes into higher resistance; then we look to realign with dominant bearish HTF. Expect topping behavior + weakening bullish VPA (no ignition) before engaging.
* **Location**: Reversal zone into `4H.zones.SELL_2` (**~74.6k**) / `4H.zones.SELL_1` (**~77.0k**) overlapping the higher shelf `1M.major.L_MAJOR` (**~74.5k**) and dynamic caps `4H_W_VWAP` (**~75.0k**) / `4H_M_VWAP` (**~75.4k**).
* **Trigger**: Liquidity sweep above the local 1H swing high near the location → LTF **L_MSB** down (against the bullish TTF push), with bearish VPA confirmation (sell VCs expand; CVD rolls).
* **Invalidation**: Clean bullish acceptance above `4H.zones.SELL_1` (**~77.0k**) with ignition-style follow-through (do not fade strength).
* **Setup Priority**: **A-**

---

## LONG

### **TEAL_A — Counter-trend scalp on reclaim of the broken base**

* **Context**: This is **counter-trend** inside a bearish HTF. Only acceptable if sellers fail to follow-through and price reclaims key dynamics (avoid knife-catching while 1H is below VWAP/EMAs).
* **Location**: Reclaim + hold above `1H.major.L_MAJOR` (**~70.1k**) / `4H.major.L_MAJOR` (**~70.2k**) with acceptance back above `1H.zones.SELL_2` (**~70.6k**) and ideally above `1H_S_VWAP` (**~71.1k**).
* **Trigger**: LTF **H_MSB/BOS** after reclaim (bullish structure + improving VPA/CVD); enter on the first low-volume retest that holds above `1H.zones.SELL_2`.
* **Invalidation**: Immediate loss back below `1H.major.L_MAJOR` (**~70.1k**) with sell-side expansion (bear continuation resumes).
* **Setup Priority**: **B**

---

### **YELLOW_A — Major reversal attempt at monthly support shelf**

* **Context**: Extreme oversold conditions (`1D_RSI` ~**19.9**, `4H_RSI` ~**19.6**) near the monthly support shelf `1M.zones.BUY_1` (**~73.7k**) / `1M.major.L_MAJOR` (**~74.5k**) already lost — reversal is possible, but **must be confirmed** (no absorption assumptions).
* **Location**: Reversal base anchored by reclaiming `1H_S_VWAP` (**~71.1k**) and getting back above `1D.session.PDL` (**~71.9k**) as the first “line in the sand”.
* **Trigger**: **Confirmed 1H_H_MSB** (TTF trend break) with bullish VPA (impulse volume > pullback volume) + CVD turn; enter on pullback to reclaimed value (EMA/VWAP support test).
* **Invalidation**: Continued acceptance below `1H.major.L_MAJOR` (**~70.1k**) with new sell expansion (defer back to SHORT continuations).
* **Setup Priority**: **A-**

---

### **GREEN_A — Breakout long (high effort, low expectation in this HTF)**

* **Context**: Requires a *full* 1H trend flip; otherwise this is just a bounce inside a bearish market. Only consider if buyers show ignition and sustain above key structure (no wicky, weak pushes).
* **Location**: Break/hold above `1H.major.H_MAJOR` (**~72.0k**) with reclaim of `1H.inactive.L_BOS` (**~72.9k**), aiming toward `4H.poc.POC_2` (**~73.8k**) / `4H.zones.SELL_2` (**~74.6k**).
* **Trigger**: 1H **H_BOS** with strong bullish VC/HVC + rising CVD → low-volume retest → LTF **H_MSB/BOS** confirmation entry.
* **Invalidation**: Failed retest back below `1H.major.H_MAJOR` (**~72.0k**) (bull trap / FSB risk).
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
- 1W: `OVERALL-ASSESSMENT = BEARISH`. DO NOT PERFORM TTI on the 1W_TF. 
- `PG` grades are assessed based on the plan full viability. DO NOT DEGRADE the plan based on probability/possibility.  

