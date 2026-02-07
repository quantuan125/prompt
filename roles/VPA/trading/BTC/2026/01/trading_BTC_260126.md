# CONTEXT: 
## TRADER CONTEXT: 
Today: Today is Monday 26th of January 2026, we are trading 30 minutes into US session. We have Durable Gods Order MoM as the only major macro data released today as shown below. Refers to `MACRO CONTEXT` for the rest of the macro events this week.  

Last month: Marked the end of Quantitative Tightening cycle from the FED and market was reacting to 25bps rate cut from FOMC. Holiday season and low volume/liquidity environment toward the end of the year. 

This week: A return back from holiday season.
```markdown
Today’s Durable Goods print was **growth-positive and slightly “hawkish” at the margin** because the *underlying* capex proxy also beat expectations (not just the headline).

## Near-term impact (today / next 1–2 sessions)

### What the data actually said (key numbers)

* **Durable Goods Orders (Nov): +5.3%** vs **+3.1% exp** vs **-2.1% prior**
* **Ex-Transportation: +0.5%** (removes the most volatile components)
* **Core Durable Goods: +0.5%** vs **+0.3% exp** vs **+0.2% prior**
* **Core capex proxy (Nondefense capital goods ex-aircraft): +0.7%** vs **+0.3% exp**
* Big driver: **non-defense aircraft orders +97.6%** (headline boost), but the **ex-transport + core capex beat** is what matters for macro pricing.

### Rates / USD (the transmission mechanism)

* **Bias:** Upward pressure on **yields** and **USD** (stronger growth + firmer investment pulse → less urgency for Fed easing).
* **Trading implication:** If yields and USD firm, that typically **tightens financial conditions** → headwind for **BTC** and **gold**, mixed for **SP500** (good growth vs higher discount rates).
## Short-term impact (this week into FOMC)

* This report **reduces the probability of a dovish surprise** (it strengthens the “economy still has momentum” argument).
* It increases the odds that markets focus on:

  1. **Fed tone** (hawkish hold risk), and
  2. **Real yields** as the driver of cross-asset direction.
* **Cross-market playbook for the week:**

  * **Hawkish-hold tone + yields up:** SPX choppy/down, **gold down**, **BTC down** (correlations tighten risk-off).
  * **Hold + neutral/dovish lean + yields stable/down:** SPX up, **BTC up**, gold mixed-to-up (depending on USD and risk hedging demand).
``` 

Directive: Price is bearish on both weekly and daily, prioritize shorts. 

Sentiment: With price action last year quarter that have liquidated millions of leveraged crypto traders and enact fears after failure to break ATH. In addition to being an apathetic top of this cycle, the general consensus is that this the start of the BTC bear market in 2026. `Fear & Greed Index` improve since last month from around 15 (EXTREME FEAR) toward 26-40 (FEAR/NEUTRAL) last week however dopped back to 20 (EXTREME FEAR) in the current week following last week sell-off

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
    zones:
      BUY_2: 89.5
      BUY_1: 73.7
    inactive:
      H_BOS: 109.6

  1W:
    local: 
      H: 97.9
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
      POC_4: 84.4
      POC_5: 67.4
    zones:
      SELL_1: 114.9
      SELL_2: 106.1
      SELL_3: 98.1
      BUY_1: 85.5
    active:
      L_BOS: 107.3
    inactive:
      L_MSB: 111.9
      H_FSB: 124.5

  1D:
    major:
      H_MAJOR: 97.9
      L_MAJOR: 89.3
    sr:
      SR_1: 93.4
      SR_2: 89.5
      SR_3: 88.4
    poc:
      POC_1: 95.5
      POC_2: 92.5
      POC_3: 90.2
      POC_4: 84.6
      POC_5: 79.7
    zones:
      BUY_1: 88.5
      SELL_1: 95.0
      SELL_2: 92.0
    session:
      PDH: 89.3
      PDL: 86.1
    active:
      L_MSB: 89.3
    inactive:
      H_BOS: 94.8

  4H:
    major:
      H_MAJOR: 91.2
      L_MAJOR: 86.1
    sr:
      {}
    poc:
      POC_1: 93.0
      POC_2: 89.6
      POC_3: 87.9
      POC_4: 86.4
    zones:
      SELL_1: 90.2
      SELL_2: 88.6
    active:
      L_BOS: 88.6
    inactive:
      H_FSB: 90.6

  1H:
    major:
      H_MAJOR: 88.4
      L_MAJOR: 87.5
    sr: {}
    poc: {}
    zones:
      SELL_1: 88.3
    active:
      H_CHOCH: 88.0
    inactive:
      L_BOS: 88.1

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

* **Previous (~30 candles):** After the late ’24 `1M_bullish_channel`, weekly momentum weakened with `1W.inactive.L_MSB`, then an ATH sweep (`1W.inactive.H_FSB`) and the liquidation leg that undercut `1M.inactive.H_BOS` and confirmed `1W.active.L_BOS`. The selloff pierced the historic bull-market support bands and rotated into the monthly demand complex (`1M.zones.BUY_2` → `1M.poc.POC_4` / `1M.sr.SR_4`), basing above `1W.major.L_MAJOR`. Recovery topped at `1W.local.H` after retesting `1W.zones.SELL_3`, then rolled back with last week’s `1W_bearish_engulfing_VC`.
* **Current (~5 candles):** Weekly is rotating back down inside the range toward `1W.sr.SR_3` and the demand edge at `1W.zones.BUY_1`. Trend health is still **bearish / neutral-bearish**: price remains below `1W_9/21EMA` and `1W_50EMA`, while still above `1W_200EMA/200SMA` (long-term up, medium-term distribution). `1W_RSI` sits sub-50 and `1W_M_VWAP` overhead keeps rallies “sell-rip” until acceptance back above `1W.poc.POC_3` and `1W.poc.POC_2`.

---

### **Daily (1D – HTF for intraday)**

* **Previous (~30 candles):** Bottoming at `1W.major.L_MAJOR` printed the absorption `1D_bearish_hammer_HVC` (sell climax + oversold), then a counter-trend push produced `1D.inactive.H_BOS` into `1W.zones.SELL_3` but on OBV divergence. The roll-over from `1W.local.H` printed multiple `1D_bearish_body_VC`s, broke `1D.zones.BUY_1`, and confirmed `1D.active.L_MSB` with `1D_9/21EMA` + `1D_M_VWAP` rolling bearish.
* **Current (~5 candles):** Price is trading **below** the broken daily floor `1D.active.L_MSB` / `1D.major.L_MAJOR` and below `1D_9/21EMA`, with `1D_RSI` sub-50 (risk-on bounce is still corrective). Session refs: `1D.session.PDH` overhead is now “sell-first” and `1D.session.PDL` is the immediate defense; a clean loss of `1D.session.PDL` exposes the next daily HVN magnet at `1D.poc.POC_4`, with `1W.zones.BUY_1` as the key HTF demand shelf.

---

### **4H (4H – HTF for 1H)**

* **Previous (~30 candles):** Weekend bearish consolidation printed `4H.inactive.H_FSB`, then `4H.active.L_BOS` established the LL where price bottomed at `4H.major.L_MAJOR`. This sell-off printed `4H_bearish_engulfing_HVC`; momentum is still structurally bearish (lower highs under `4H_21EMA`), but the LL occurred on oversold RSI + bullish divergence (warning: sellers may be tiring).
* **Current (~5 candles):** The pullback is attempting to reclaim `4H_W_VWAP`/`4H_9EMA` and is back-testing the breakdown zone at `4H.active.L_BOS` which overlaps `4H.zones.SELL_2`. Bias remains **bearish until proven otherwise**: acceptance back above `4H.zones.SELL_2` is needed to neutralize the breakdown; rejection here reopens `4H.major.L_MAJOR` with potential extension into `1W.zones.BUY_1`.

---

### **1H (1H – TTF / execution anchor)**

* **Previous (~30 candles):** After bottoming at `4H.major.L_MAJOR`, price staged a counter-trend bounce with reclaim attempts of `1H_9/21EMA` + `1H_S_VWAP`. A `1H.active.H_CHOCH` preceded the rally into the upper band, then price reverted into a balancing range centered around `4H.poc.POC_3`.
* **Current (~5 candles):** 1H is **range-bound** between `1H.major.H_MAJOR` and `1H.major.L_MAJOR`, with price hovering around the `4H.poc.POC_3` “magnet.” Trend posture is **neutral-bearish**: price have multiple attempts at retesting the 1H range high and until 1H breaks/accepts below `1H.major.L_MAJOR`, the selloff is also not “free-flowing” (chop risk).

## MACRO CONTEXT

### LAST WEEK

* **Macro/policy regime (still dominated by “rates + politics”)**

  * **Fed:** Market focus shifted from “when cuts” to **Fed independence/leadership risk** into this week’s FOMC.
  * **US data quality caveat:** The **prior 43-day shutdown distorted/lagged key releases** (some inflation inputs missing; BEA had to impute). Q4 GDP (advance) and December personal income/outlays were **officially pushed to Feb 20**, keeping “hard data” uncertainty elevated.

* **Top US data (actual vs exp vs prior)**

  * **Personal Spending (Nov):** **+0.5%** vs **+0.5%** vs **+0.5%**
  * **Personal Income (Nov):** **+0.3%** vs **+0.4%** vs **+0.1%**
  * **PCE inflation (Nov):**

    * **PCE m/m:** **+0.2%** vs **+0.2%** vs **+0.2%**
    * **PCE y/y:** **+2.8%** vs **+2.8%** vs **+2.7%**
    * **Core PCE y/y:** **+2.8%** vs **+2.8%** vs **+2.7%**
  * **Initial Jobless Claims (wk):** **200K** vs **209K** vs **199K**
  * **Pending Home Sales (Dec):** **-9.3%** vs **-0.3%** vs **+3.3%** (housing re-softened)
  * **S&P Global Flash PMIs (Jan):**

    * **Manufacturing:** **51.9** vs **51.9** vs **51.8**
    * **Services:** **52.5** vs **52.9** vs **52.5**
    * **Composite:** **52.8** vs *(n/a)* vs **52.7**
    * Price pressure narrative stayed tied to **tariffs/cost pass-through** in surveys.
  * **U. Michigan Sentiment (Jan final):** **56.4** vs **54.0** vs **52.9**; **1Y inflation expectations 4.0%** (down from 4.2%).

* **Cross-asset tape that matters for today**

  * **Gold:** Continued **safe-haven bid**, with fresh record levels above **$5,100/oz** amid geopolitics and policy uncertainty.
  * **Equities/crypto:** Risk sentiment was increasingly headline-driven (tariffs, shutdown risk, Fed politics) into a **mega-cap earnings + FOMC** week.

---

### THIS WEEK

* **Key theme:** **FOMC + “Fed independence” headlines + mega-cap earnings + Jan 30 funding deadline** = elevated event risk and gap risk.

* **US economic calendar (actual / forecast / prior where available)**

  * **Mon Jan 26**

    * **Durable Goods Orders (Nov):** **+5.3%** vs **+3.1%** vs **-2.1%**
    * **Core Durable Goods (Nov):** **+0.5%** vs **+0.3%** vs **+0.2%**
    * **Core capex proxy (Nondef ex-air, Nov):** **+0.7%** vs **+0.3%** (business investment pulse)
    * **Chicago Fed National Activity Index (Nov):** **-0.04** vs *(n/a)* vs **-0.24**

  * **Tue Jan 27**

    * **CB Consumer Confidence (Jan):** **90.1** *(forecast)* vs **89.1** *(prior)*
    * **Earnings focus:** “Mag-7” week accelerates; positioning can dominate index flows.

  * **Wed Jan 28**

    * **FOMC rate decision / statement:** **2:00pm ET**; **press conference 2:30pm ET**
    * **Consensus:** **Hold at 3.50%–3.75%**, with focus on tone and any Fed leadership commentary
    * **Earnings (after close):** Microsoft, Meta, and Tesla highlighted as key index and AI-beta drivers

  * **Thu Jan 29**

    * **Initial Jobless Claims:** **202K** *(forecast)* vs **200K** *(prior)*
    * **Factory Orders (Nov):** **+0.5%** *(forecast)* vs **-1.3%** *(prior)*
    * **Wholesale Inventories (Nov):** **+0.2%** *(forecast)* vs **+0.5%** *(prior)*
    * **Important schedule exception:** **Q4 GDP (advance) and December income/outlays remain scheduled for Feb 20**
    * **Earnings:** Apple slated later in the week (potentially market-moving)

  * **Fri Jan 30**

    * **Chicago PMI (Jan):** **43.3** *(forecast)* vs **42.7** *(prior)*
    * **US funding deadline:** Current government funding **expires Jan 30**, with shutdown-risk headlines capable of spiking volatility into the close

* **Political / geopolitical / tech headlines to monitor**

  * **Tariffs / trade escalation risk:** Trump tariff threats (e.g., **100% Canada tariff** headlines) add inflation and risk-premium sensitivity into FOMC.
  * **Fed independence storyline:** Ongoing Trump–Fed friction remains a macro catalyst impacting rates term premium, USD, and gold.

---

### MACRO ANALYSIS

#### OVERALL CROSS-MARKETS

Event risk is tightly clustered around **FOMC (Wed)**, **mega-cap earnings**, and the **Jan 30 funding deadline**, which can override normal data-driven reactions. The dominant macro tension is **tariff-driven inflation risk versus signs of labor market cooling**, compounded by **institutional and political risk premiums** around the Fed. This backdrop favors **higher volatility**, reduced risk appetite, tighter SPX–BTC correlation intraday, and continued **support for gold under uncertainty**.

#### BTC & ETH

BTC continues to trade primarily as a **risk and liquidity-sensitive asset**. It generally benefits from **dovish rate expectations** and stable equity sentiment, while remaining vulnerable to **rising real yields, a stronger USD, or equity drawdowns**. For today, **positioning ahead of FOMC and mega-cap earnings** is likely to dominate. Sustained upside likely requires either a clear risk-on impulse from equities or a rates narrative that pulls yields meaningfully lower.

# TRADING PLAN FOR 1H_TTF (Trigger • Location • Context)

## SHORT

### **WHITE_A — Breakdown continuation below 1H range low**

* **Context**: HTF (`1D`, `4H`) remains bearish; 1H bounce is corrective while price is capped under `1H_9/21EMA` + `1H_S_VWAP`. Expect liquidity to hunt below `1H.major.L_MAJOR` if sellers reassert with expanding spreads and rising sell-volume.
* **Location**: Loss/retest zone around `1H.major.L_MAJOR` aligned with `4H.active.L_BOS` / `4H.zones.SELL_2` (key S/R flip cluster).
* **Trigger**: **Confirmed `1H_L_BOS`** through `1H.major.L_MAJOR` on bearish VPA (ideally ignition `1H_bearish_body_HVC/SHVC`) → then low-volume retest from below + `15m_L_MSB` continuation.
* **Invalidation**: Sharp reclaim and acceptance back above `1H.major.L_MAJOR` **and** `1H_S_VWAP` (range recapture).
* **Setup Priority**: A+

---

### **ORANGE_A — Short reversal at 4H supply (realign with HTF bearish)**

* **Context**: If the 1H bounce extends, it is still counter-trend against `4H` bearish structure; watch for weakening bullish VPA + bearish divergence (RSI/CVD) into resistance while `4H_21EMA` remains descending.
* **Location**: Rejection/sweep area at `4H.zones.SELL_1` + `4H.major.H_MAJOR` (major HTF supply cap).
* **Trigger**: Liquidity sweep above the local top → **TTF `1H_L_MSB`** confirmed (break of a *major* 1H swing low) with bearish CVD turn + bearish VC expansion; enter on the first low-volume pullback to the flip.
* **Invalidation**: Acceptance above `4H.major.H_MAJOR` (buyers converting HTF supply).
* **Setup Priority**: A

---

### **PURPLE_A — Short fade of 1H range high (failed breakout)**

* **Context**: Range conditions; prefer shorts at the top because HTF bias is bearish. Look for “pop and fail” (no follow-through) and rolling `1H_RSI-MA` under 50.
* **Location**: `1H.major.H_MAJOR` confluence with `1H.zones.SELL_1` and dynamic cap from descending `1H_50EMA`.
* **Trigger**: Wick-through / sweep then close back below (`1H_bearish_rejection_VC`) + `15m_L_MSB` back into range (classic FSB behavior).
* **Invalidation**: Clean hold above `1H.major.H_MAJOR` that flips it to support.
* **Setup Priority**: B+

---

### **PINK_A — Counter-trend momentum short (if bounce dies early)**

* **Context**: Shorting the failed bounce: price loses `1H_S_VWAP` + `1H_9EMA` and cannot reclaim; expect sellers to press back toward the range floor.
* **Location**: Below `1H_S_VWAP` with price still capped under `1H.major.H_MAJOR`.
* **Trigger**: `15m_L_BOS/MSB` on the retest failure of `1H_S_VWAP` + bearish `15m_9/21EMA` rollover; enter only after structure confirms (no chasing).
* **Invalidation**: Reclaim + acceptance above `1H_S_VWAP` with `15m_HL` sequence restored.
* **Setup Priority**: B

---

### **RED_A — Decisive 1H range breakdown (strong VPA)**

* **Context**: “Get out of chop” scenario—only act if breakdown is **impulsive** (range expands + sell-side commitment). This is the high-conviction version of WHITE_A.
* **Location**: Breakdown below `1H.major.L_MAJOR` with follow-through opening path toward `4H.major.L_MAJOR`.
* **Trigger**: `1H_L_BOS` + bearish ignition `1H_bearish_marubozu_HVC/SHVC` → low-volume retest → `5m/15m_L_BOS` continuation.
* **Invalidation**: Immediate reclaim back above `1H.major.L_MAJOR` (failed breakdown → flip to BLUE_A logic).
* **Setup Priority**: B-

---

## LONG

### **BLUE_A — Long fade of 1H range low (failed breakdown)**

* **Context**: Counter-trend scalp only: HTF is bearish, so demand must **prove** itself (divergence + failure). Ideal if selloff into the low shows weakening VPA and buyers absorb.
* **Location**: Sweep/hold at `1H.major.L_MAJOR` (range low) with HTF shelf nearby at `1D.session.PDL`.
* **Trigger**: Liquidity sweep below range low → reclaim above `1H.major.L_MAJOR` + `15m_H_MSB` (back into range) with rising CVD; enter on pullback.
* **Invalidation**: Acceptance below `1H.major.L_MAJOR` (defer to WHITE/RED shorts).
* **Setup Priority**: B-

---

### **TEAL_A — Long momentum scalp (only if 1H flips back above VWAP/EMAs)**

* **Context**: Bounce continuation is valid **only** if 1H can hold above `1H_S_VWAP` and rebuild HH/HLs with improving VPA (pullbacks low-volume, pushes higher-volume).
* **Location**: Sustained acceptance back above `1H.major.H_MAJOR` while holding the flip zone at `4H.active.L_BOS` / `4H.zones.SELL_2`.
* **Trigger**: `15m_H_BOS/MSB` continuation after a low-volume retest of the reclaimed band; bonus if `1H_9/21EMA` turns up and CVD confirms.
* **Invalidation**: Failure back below `1H_S_VWAP` and loss of `1H.major.H_MAJOR`.
* **Setup Priority**: B

---

### **YELLOW_A — Major reversal attempt at HTF base**

* **Context**: Only consider if the selloff extends into HTF demand with **clear exhaustion** (stopping volume + divergence) and then structure flips. Patience required—no knife-catching.
* **Location**: HTF base at `4H.major.L_MAJOR` with extension into `1W.zones.BUY_1`.
* **Trigger**: **TTF `1H_H_MSB`** (bullish MSB) after exhaustion behavior, then first low-volume pullback to the flip + `15m_H_MSB` confirmation.
* **Invalidation**: Continued acceptance below `4H.major.L_MAJOR` (demand failed).
* **Setup Priority**: A-

---

### **GREEN_A — Break & retest above the 1H range high**

* **Context**: This is the “trend-change candidate” long. Must see strong bullish VPA + CVD confirmation because HTF backdrop is still bearish.
* **Location**: Break/hold above `1H.major.H_MAJOR` with acceptance above `1H.zones.SELL_1`, ideally pulling 1H back above `4H.active.L_BOS` / `4H.zones.SELL_2`.
* **Trigger**: `1H_H_BOS` on bullish expansion VC (prefer HVC) → low-volume retest holding above → `15m_H_MSB/BOS` entry trigger.
* **Invalidation**: Failed retest (acceptance back below `1H.major.H_MAJOR`) or immediate `1H_L_CHOCH` against the position.
* **Setup Priority**: B

  
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

