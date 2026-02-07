# CONTEXT: 
## TRADER CONTEXT: 
Today: Today is Friday 30th of January 2026, we are trading 1 hours prior to US session open. We had PPI MoM as the only major macro data released today as shown below. Refers to `MACRO CONTEXT` for the rest of the macro events this week.  

Last month: Marked the end of Quantitative Tightening cycle from the FED and market was reacting to 25bps rate cut from FOMC. Holiday season and low volume/liquidity environment toward the end of the year. 

This week: A return back from holiday season.

Directive: Price is bearish on both weekly and daily, prioritize shorts, however caution due to price at 1W range low. 

Sentiment: With price action last year quarter that have liquidated millions of leveraged crypto traders and enact fears after failure to break ATH. In addition to being an apathetic top of this cycle, the general consensus is that this the start of the BTC bear market in 2026. `Fear & Greed Index` improve since last month toward 26-40 (FEAR/NEUTRAL) last week however dopped back to 15-20 (EXTREME FEAR) in the current week following this week continued sell-off

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
      POC_4: 84.5
      POC_5: 79.7
    zones:
      SELL_1: 95.0
      SELL_2: 92.0
      SELL_3: 88.3
    session:
      PDH: 89.4
      PDL: 83.4
    active:
      L_BOS: 86.1
    inactive:
      L_MSB: 89.3

  4H:
    major:
      H_MAJOR: 90.6
      L_MAJOR: 86.1
    sr:
      {}
    poc:
      POC_1: 93.0
      POC_2: 89.6
      POC_3: 87.9
      POC_4: 86.4
    zones:
      SELL_1: 87.0
      SELL_2: 85.9
    active:
      L_BOS: 86.1
    inactive:
      L_BOS: 88.6

  1H:
    local: 
      H: 83.3
      L: 82.1
    major:
      H_MAJOR: 87.4
      L_MAJOR: 83.4
    sr: {}
    poc: {}
    zones:
      SELL_1: 83.8
      SELL_2: 82.9
    active:
      L_BOS: 83.4
    inactive:
      L_BOS: 87.7
  
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

* **Previous (~30 candles):** After a strong `1M_bullish_channel` since late ’24, price printed `1W.inactive.L_MSB` (weekly bull trend weakening) and distributed under `ALL.ath` / `1W.major.H_MAJOR`. The ATH sweep / failed continuation into `1W.inactive.H_FSB` was followed by the large liquidation sell-off that broke below `1M.inactive.H_BOS` and eventually based at `1W.major.L_MAJOR`. From that base, the recovery leg retested weekly supply `1W.zones.SELL_3` and topped at `1W.local.H` (confluence with declining weekly EMA band), then rotated back into the weekly range.
* **Current (~5 candles):** Weekly is rolling over from `1W.local.H` / `1W.zones.SELL_3` with last week’s `1W_bearish_engulfing_VC`, and this week continuing bearish (`1W_bearish_large-body_VC`) pressing toward the weekly demand band `1W.zones.BUY_1` and the range floor `1W.major.L_MAJOR`. **1W indicators:** price is below `1W_9EMA` (~89.95k), `1W_21EMA` (~95.84k), `1W_50EMA` (~96.52k) and below `1W_W_VWAP` (~84.83k) / `1W_M_VWAP` (~89.89k); `1W_RSI` ~35.86 is below `1W_RSI-MA` ~40.43 → **weekly bias remains bearish**.

---

### **Daily (1D – HTF for Intraday)**

* **Previous (~30 candles):** After the weekly base at `1W.major.L_MAJOR`, the tape showed capitulation/absorption characteristics (the described `1D_bearish_hammer_HVC` into HTF demand) followed by basing and a counter-trend push up into weekly supply `1W.zones.SELL_3`, but with momentum waning (OBV/CVD divergence risk). The rejection sequence then transitioned into a downtrend (EMA roll + structure failure), setting up the continuation breakdown path back toward `1W.major.L_MAJOR`.
* **Current (~5 candles):** Daily confirmed continuation lower via `1D.active.L_BOS` (loss of `1D.major.L_MAJOR`) and is now trading **below** `1W.zones.BUY_1`, with sell pressure pulling price under `1D.session.PDL` and keeping `1D.session.PDH` as a distant overhead reference. Overhead magnets on any rebound remain `1D.poc.POC_4` then `1D.sr.SR_3` / `1D.zones.SELL_3`, with higher resistances at `1D.zones.SELL_2` / `1D.zones.SELL_1`. **1D indicators:** price is below `1D_9EMA` (~87.38k), `1D_21EMA` (~89.23k), `1D_50EMA` (~90.74k) and below `1D_W_VWAP` (~86.50k) / `1D_M_VWAP` (~90.74k); `1D_RSI` ~30.99 (still weak, not yet “<25” extreme). The VPA framework says do **not** front-run “absorption” without PA confirmation (CHOCH/MSB) and CVD alignment. 

---

### **4H (4H – HTF for 1H)**

* **Previous (~30 candles):** 4H topped during the countertrend/FOMC bounce near `4H.major.H_MAJOR`, then rolled over and accelerated down with the described `4H.active.L_BOS` leg (multiple `4H_bearish_large-body_HVC`-type impulses) back toward the weekly range lows, keeping `4H.poc.POC_4` / `4H.poc.POC_3` and `4H.zones.SELL_2 → 4H.zones.SELL_1` as “sell-the-rip” supply on mean reversion.
* **Current (~5 candles):** 4H is attempting to base around `4H.poc.POC_5`but remains **structurally broken** below `4H.major.L_MAJOR` and still far under `4H_9EMA` (~84.41k) / `4H_21EMA` (~86.14k) and `4H_W_VWAP` (~86.38k). `4H_RSI` ~26.84 is near the oversold threshold and below `4H_RSI-MA` ~38.69 → **downtrend is extended**, so any bounce into `4H.zones.SELL_2` / `4H.poc.POC_4` must be treated as a countertrend rally until 1H/TTF structure confirms otherwise.

---

### **1H (1H – TTF Execution Context)**

* **Previous (~30 candles):** 1H remains in a strong downtrend initiated by the described `1H_bearish_engulfing_SHVC`, followed by `1H.active.L_BOS` (loss of `1H.major.L_MAJOR` and the daily breakdown context). Sell-side dominance persists while price sits under the key reclaim level `1H.active.L_BOS` / `1D.session.PDL` and below the overhead LVN supply `1H.zones.SELL_2 → 1H.zones.SELL_1`. Major upside invalidation for the current bearish regime remains a reclaim of `1H.major.H_MAJOR`.
* **Current (~5 candles):** Price is in a “pullback/base attempt” cluster of small candles (e.g., `1H_bullish_small-body_VC` / `1H_bearish_inside-bar_VC`) around `4H.poc.POC_5`, probing around the local band `1H.local.L ↔ 1H.zones.SELL_2`. **1H indicators:** price is marginally below `1H_9EMA` (~82.89k) and below `1H_21EMA` (~83.66k), but around/just above `1H_S_VWAP` (~82.60k). `1H_RSI` ~35.70 has lifted above `1H_RSI-MA` ~30.09 (a *minor* improvement), yet price is still well below `1H_W_VWAP` (~86.36k) → any rally into `1H.zones.SELL_2/SELL_1` is still a **sell-the-rip** candidate unless a **TTF MSB** prints.

## MACRO CONTEXT

### LAST WEEK

* **US growth + inflation (delayed releases due to prior shutdown):**

  * **GDP (Q3 2025, revised)**: **+4.4% SAAR** (cons **+4.3%**; prior **+3.8%**).
  * **Core PCE (Nov 2025)**: **+0.2% m/m** (cons **+0.2%**; prior **+0.2%**); **+2.8% y/y** (cons **+2.8%**; prior **+2.7%**).
* **Activity + inflation pulse (survey):**

  * **S&P Global Flash US Composite PMI (Jan)**: **52.8** (prior **52.7**); **prices charged 57.2**, **inputs 59.7**, **employment 50.5** → expansion continues, price pressure still elevated.
* **Risk framing (macro narrative):**

  * Tariff/policy uncertainty remained a key driver of risk premia (rates, USD, gold) and equity sector dispersion (AI/mega-cap vs cyclicals).

### THIS WEEK

* **Mon 26 Jan — US business investment pulse (delayed):**

  * **Durable Goods Orders (Nov)**: **+5.3% m/m** (cons **+0.5%**; prior **-2.1%**).
  * **Core capital goods orders ex aircraft (Nov)**: **+0.7% m/m** (cons **+0.3%**; prior not consistently reported across sources in the same release set).
* **Tue 27 Jan — US demand sentiment shock:**

  * **Conference Board Consumer Confidence (Jan)**: **84.5** (cons **90.9**; prior **94.2**, upwardly revised).
  * **Expectations index**: **65.1** (well below the 80 level often watched as a recession-signal threshold).
* **Wed 28 Jan — FED + policy optics:**

  * **FOMC decision**: **Hold** at **3.50%–3.75%** (market expected hold). Vote included **two dissenters preferring a 25bp cut** → “hold” but with visible dovish tilt inside the committee.
  * **Crypto policy (Washington)**: White House hosted/organized engagement with **bank + crypto executives** to discuss **market-structure / stablecoin-related** legislative pathways (headline risk for crypto beta + regulatory regime expectations).
* **Thu 29 Jan — US labor + trade + manufacturing (delayed data):**

  * **Initial jobless claims**: **209k** (cons **205k**; prior **210k** revised).
  * **Continuing claims**: **1.827m** (down **38k** from the prior week).
  * **US trade balance (Nov, goods & services)**: **-$56.8B** (cons **-$40.5B**; prior **-$29.2B** revised) → sharp import-led widening (AI/data-center capex narrative resurfacing).
  * **Factory orders (Nov)**: **+2.7% m/m** (cons **+1.6%**; prior **-1.2%** revised).
* **Fri 30 Jan — TODAY’s key release + major political catalyst:**

  * **PPI (Dec, final demand)**: **+0.5% m/m** (cons **+0.2%**; prior **+0.2%**).
  * **PPI ex food/energy/trade services (Dec)**: **+0.4% m/m** (commonly watched “core” pipeline gauge; cons **+0.3%**; prior **0.0%**).
  * **PPI (12m, Dec)**: **+3.0% y/y** (cons **+2.7%**; prior **+3.0%**).
  * **Political/Fed**: **Trump announced he will nominate Kevin Warsh** to succeed Powell when Powell’s term ends **May 2026** → Fed independence / reaction-function risk premium.
  * **US government funding**: **Jan 30 deadline** to avoid a shutdown (shutdown risk can spill into liquidity + data timing; next week’s employment report was flagged by major outlets as potentially delay-sensitive under a shutdown scenario).
* **Later today (still market-relevant):**

  * **Chicago PMI (Jan)** expected around **43.5** (prior **43.5**), plus **Baker Hughes rig count** and scheduled Fed speak (can move rates/USD on a day like today with hot PPI).

## MACRO ANALYSIS

#### OVERALL CROSS-MARKETS

Today’s setup is a **rates-led cross-asset session**: the **hotter-than-expected PPI** is a direct challenge to any near-term “disinflation = easier Fed” narrative, while the **Fed chair nomination headline** injects a **political risk premium** into the long end and USD path. If yields push higher on inflation pipeline concerns, **SP500 and BTC/ETH typically de-rate together** (risk-duration correlation), while **gold** faces a tug-of-war between **higher real yields (headwind)** and **policy/independence uncertainty (bid)**. Keep sensitivity high to **USD + UST real yields** as the primary transmission mechanism across all three markets.

#### BTC & ETH

BTC/ETH remain **macro-beta to liquidity and risk appetite** in US hours: **hot PPI → higher yields → tighter financial conditions impulse** is typically negative for crypto, especially if it strengthens the USD. However, if the market leans into the **FOMC dissents (dovish undertone)** and treats PPI as noise, crypto can rebound alongside tech. Also watch the **Washington crypto/banking policy headlines**: even incremental progress signals can swing sentiment and perp positioning.

# TRADING PLAN FOR 1H_TTF (Trigger • Location • Context)

## SHORT

### **WHITE_A — Short continuation on retest of broken daily structure**

* **Context**: HTFs (1W/1D/4H) remain bearish and price is still below `1D.active.L_BOS` (broken daily support). 1H is attempting a weak basing/pullback while still capped by `1H_21EMA` and overhead LVN supply. Ideal continuation is a low-volume mean reversion up into supply, then sellers re-assert with falling CVD + bearish structure (per VPA rules). 
* **Location**: Retest band = `1D.active.L_BOS` confluence with `1H.zones.SELL_1` / `1H.zones.SELL_2` and descending `1H_21EMA`.
* **Trigger**: Confirmed **LTF_L_MSB** at/just below the retest zone + bearish ignition VC (HVC preferred) + CVD rolls back down; enter on the first low-volume pullback after the LTF_L_MSB.
* **Invalidation**: Acceptance + hold above `1D.sr.SR_3` (reclaim) and sustained trade above `1H.zones.SELL_1`.
* **Setup Priority**: `A+`

---

### **ORANGE_A — Short reversal after a countertrend 1H rally**

* **Context**: If 1H manages to trend up (countertrend) toward higher confluence supply, treat it as **unaligned** vs bearish 4H/1D. Look for weakening bullish VPA (rising price on fading volume) and/or bearish RSI/CVD divergence into the retest of the breakdown area, then a **TTF_L_MSB** to confirm “TTF uptrend failure → HTF realign.” 
* **Location**: `4H.zones.SELL_2` + retest of `1D.active.L_BOS`, ideally near `4H.poc.POC_4` with `4H_W_VWAP` overhead.
* **Trigger**: Liquidity sweep/failed acceptance above `1D.active.L_BOS` followed by **1H_L_MSB** (TTF) + bearish VPA confirmation; enter on low-volume pullback to the S/R flip created by the 1H_L_MSB.
* **Invalidation**: Clean acceptance and hold above `4H.zones.SELL_2` with bullish follow-through (no rejection) and CVD sustaining positive.
* **Setup Priority**: `A`

---

### **PURPLE_A — Short fade of the 1H range high**

* **Context**: Bearish bias range-fade: if price runs up into the top of the 1H major range and fails (classic liquidity grab), take only if bullish effort is weak (no ignition) and CVD/RSI diverge.
* **Location**: `1H.major.H_MAJOR` with a potential `H_FSB` and descending `1H_50EMA`.
* **Trigger**: Wick above `1H.major.H_MAJOR` then close back below + **LTF_L_MSB** back into range; enter on retest of the failure zone.
* **Invalidation**: 1H acceptance above `1H.major.H_MAJOR` (failed fade).
* **Setup Priority**: `A-`

---

### **PINK_A — Short momentum scalp on renewed breakdown**

* **Context**: If the current basing fails, we want continuation with momentum: loss of `1H_S_VWAP` and `1H_9EMA` plus acceptance below `1H.local.L` signals sellers regained control; trade must be **fast** with tight structure-based risk.
* **Location**: Breakdown/acceptance below `1H.local.L` while below `1H_S_VWAP` + `1H_9EMA`.
* **Trigger**: Confirmed **LTF_L_BOS/MSB** → low-volume retest of the broken level from below, with bearish `LTF_9/21EMA` rollover + falling CVD.
* **Invalidation**: Reclaim and hold above `1H.local.L` + sustained trade back above `1H_S_VWAP`.
* **Setup Priority**: `B+`

---

### **RED_A — Breakdown continuation below weekly range floor**

* **Context**: This is the “risk-off extension” plan: only act if a decisive sell impulse breaks the weekly floor with strong VPA (bearish ignition HVC/SHVC + CVD flush), otherwise **do not** short blindly into support.
* **Location**: Below `1W.major.L_MAJOR` (with nearby weekly supports `1W.sr.SR_4` then `1W.sr.SR_5` as the next references).
* **Trigger**: **1H_L_BOS** through `1W.major.L_MAJOR` on strong bearish VPA → enter on low-volume retest of `1W.major.L_MAJOR` from below with confirming **LTF_L_MSB/BOS**.
* **Invalidation**: Sharp reclaim and hold back above `1W.major.L_MAJOR` (breakdown failure / trap).
* **Setup Priority**: `B`

---

## LONG

### **BLUE_A — Long fade at weekly range floor (failed breakdown)**

* **Context**: Countertrend “floor hold” attempt only at HTF support: require evidence sellers are exhausting (weakened bearish VPA + bullish RSI/CVD divergence) and a **failed break** (FSB) rather than guessing. 
* **Location**: `1W.major.L_MAJOR` (watch extension risk toward `1W.sr.SR_5`).
* **Trigger**: Sweep below `1W.major.L_MAJOR` then reclaim + **LTF_H_MSB** and improving CVD; enter on the pullback after the LTF_H_MSB.
* **Invalidation**: Continued acceptance below `1W.major.L_MAJOR` (defer to **RED_A**).
* **Setup Priority**: `B-`

---

### **TEAL_A — Countertrend scalp on reclaim of broken 1H structure**

* **Context**: A tactical bounce is acceptable only if 1H reclaims the breakdown pivot (`1H.active.L_BOS`) and holds above `1H_S_VWAP` + `1H_9EMA`, showing the pullback buyers can defend. Keep targets conservative into overhead supply.
* **Location**: Reclaim zone around `1H.active.L_BOS` with immediate overhead friction at `1H.zones.SELL_2 → 1H.zones.SELL_1`.
* **Trigger**: **LTF_H_BOS/MSB** on the retest of the reclaimed level + bullish VPA (rising CVD, stronger volume on upswings than pullbacks).
* **Invalidation**: Failure to hold above `1H.active.L_BOS` and loss back below `1H_S_VWAP`.
* **Setup Priority**: `B`

---

### **YELLOW_A — Major reversal attempt at weekly floor (deeper macro washout path)**

* **Context**: This is the “trend-dies” long: only valid if the bearish 1H trend **breaks** (TTF MSB) with meaningful demand response and divergences; otherwise it’s knife-catching. If it triggers, upside is a larger mean reversion; if it fails, downside can extend toward `1M.zones.BUY_1` / `1M.major.L_MAJOR`.
* **Location**: Base area `1W.major.L_MAJOR`, with failure-extension risk toward `1M.zones.BUY_1` / `1M.major.L_MAJOR`.
* **Trigger**: **1H_H_MSB** (TTF) + pullback to the value zone created by the MSB on weakening sell volume; enter on LTF confirmation at that pullback.
* **Invalidation**: Fresh **1H_L_BOS** that cleanly accepts below `1W.major.L_MAJOR`.
* **Setup Priority**: `A-`

---

### **GREEN_A — Long breakout & retest (only after structure flips)**

* **Context**: Only consider this if price has already stabilized (no new lows) and buyers can reclaim the key breakdown area, turning former supply into support with strong bullish VPA + CVD confirmation; otherwise it’s a trap rally into HTF supply.
* **Location**: Break and hold above `1D.active.L_BOS` with continuation through `1H.major.H_MAJOR`.
* **Trigger**: **1H_H_BOS** supported by bullish ignition VC → low-volume retest of the broken level, then **LTF_H_MSB/BOS** to execute.
* **Invalidation**: Acceptance back below `1D.active.L_BOS` after the breakout (failed reclaim).
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

