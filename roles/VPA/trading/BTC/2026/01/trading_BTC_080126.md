# CONTEXT: 
## TRADER CONTEXT: 
Today: Today is Thursday 8th of January 2026, we are in London session, 1 hours until US session. We have no major data/macro event released today. Refers to `MACRO CONTEXT` for the rest of the macro events this week.  

Last month: Marked the end of Quantitative Tightening cycle from the FED and market was reacting to 25bps rate cut from FOMC. Holiday season and low volume/liquidity environment toward the end of the year. 

This week: A return back from holiday season. We have major macro data released today as outlined in MACRO CONTEXT section. All eyes are on NFP + Unemployment numbers on Friday. 

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
      POC_4: 87.5
      POC_5: 67.4
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
      L_MAJOR: 86.4
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
      BUY_1: 88.5-89.6
    session:
      PDH: 93.7
      PDL: 90.7
    active:
      H_BOS:: 90.6
    inactive:
      H_FSB: 90.3

  4H:
    major:
      H_MAJOR: 94.4
      L_MAJOR: 90.9
    sr:
      {}
    poc:
      POC_1: 92.5
      POC_2: 88.1
      POC_3: 86.4
      POC_4: 82.2
    zones:
      SELL_1: 93.3
      SELL_2: 92.1
    active:
      L_BOS: 91.3
    inactive:
      L_CHOCH: 93.1
      H_BOS: 91.8

  1H:
    local: 
      H: 90.9
    major:
      H_MAJOR: 91.7
      L_MAJOR: 89.6
    sr: {}
    poc: {}
    zones:
      SELL_1: 90.7-90.9
    active:
      L_BOS: 90.7
    inactive:
      L_BOS: 91.3

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

* **Previous (~30 candles):** After the late-’24 `1M_bullish_channel`, weekly momentum weakened with `1W.inactive.L_MSB` under `ALL.ath` / `1M.major.H_MAJOR`, then an ATH probe (`1W.inactive.H_FSB`) failed and flipped into the liquidation selloff. The down leg confirmed `1W.active.L_BOS` (breakdown from the prior bull structure) and drove price below `1W.major.L_MAJOR` into the monthly demand band `1M.zones.BUY_2`, extending toward `1M.poc.POC_4` + `1M.sr.SR_4`. Trend confirmation: current price is still below `1W_9/21EMA` (bearish separation), below `1W_W/M_VWAP`, and `1W_RSI` remains sub-50 (bearish regime).
* **Current (~5 candles):** Multi-week compression inside the weekly range `1W.local.L` ↔ `1W.local.H`, with price capped well below `1W.zones.SELL_3` and rotating around `1W.poc.POC_3` / `1W.poc.POC_4`. Current weekly candle is a low-volume `1W_bearish_impulse_VC` (no trend ignition yet), so bias remains **neutral-bearish** unless we see a weekly acceptance back above `1W.poc.POC_3` and sustained reclaim of `1W_9EMA`.

---

### **Daily (1D – HTF for intraday)**

* **Previous (~30 candles):** Selloff base formed at `1W.local.L` with the absorption `1D_bearish_hammer_HVC` (capitulation-style volume + deeply oversold RSI per your note), followed by holiday consolidation around `1W.poc.POC_4`. The breakout above `1D.active.H_BOS` occurred on lighter participation, ran into `1D.zones.SELL_1` / `1W.local.H`, topped at `1D.major.H_MAJOR`, then rolled over (failed follow-through at supply).
* **Current (~5 candles):** Price is now back below `1D.session.PDL` and testing the `1D.active.H_BOS` reclaim zone from underneath, rotating near `1D.poc.POC_3` magnet. Daily structure is **fragile**: price sits below `1D_9EMA`, beneath `1D_W_VWAP` / `1D_M_VWAP`, and `1D_RSI` is hovering around 50 but slipping under `1D_RSI-MA` (momentum cooling). Acceptance below `1D.active.H_BOS` keeps pressure on for an extension into `1D.zones.BUY_1`.

---

### **4H (4H – HTF for 1H)**

* **Previous (~30 candles):** Strong recovery leg reclaimed the 4H_200EMA/MA band (first time in months) but the move stalled into the daily supply overhead; a `4H_bearish_impulse_HVC` printed into `4H.inactive.L_CHOCH`, then price lost the `4H_9/21EMA` (bearish crossover) + W_VWAP and followed through to `4H.active.L_BOS`. That breakdown shifted the 4H flow back into **bearish continuation / backfill**.
* **Current (~5 candles):** Price is now below `4H.active.L_BOS` and pressing under `4H.major.L_MAJOR`, with `4H_9/21EMA` overhead and `4H_W_VWAP` / `4H_M_VWAP` still above (sell-side control). Immediate downside magnet is `4H.poc.POC_2`, overlapping the daily demand `1D.zones.BUY_1`. Any bounce that cannot reclaim `4H.zones.SELL_2` → `4H.zones.SELL_1` is structurally a **sell-the-rip** until proven otherwise.

---

### **1H (1H – TTF / Execution Anchor)**

* **Previous (~30 candles):** Clean breakdown sequence into `1H.active.L_BOS` with the decisive `1H_bearish_engulfing_HVC` and continuation under `1H_9/21EMA`, while failing to reclaim `1H.zones.SELL_1` on the backtest. The sell leg tagged `1H.major.L_MAJOR`, then bounced and rolled (lower-high behavior under supply) with a LH at `1H.local.H`.
* **Current (~5 candles):** Price remains below `1H.active.L_BOS` and under `1H_S_VWAP`, with `1H_9/21EMA` above (bearish stack) and `1H_W_VWAP` far overhead (bear market VWAP alignment). `1H_RSI` is still weak (sub-50) and `1H_CVD` is negative (sell pressure persists). The market is **eligible for continuation shorts** while below `1H.active.L_BOS`; longs are **counter-trend only** unless a real 1H reversal structure forms.

## MACRO CONTEXT
### LAST WEEK

* **Liquidity / holidays**

  * **Thu Jan 1:** New Year’s Day — **US cash equity + Treasury markets closed**; year-end liquidity remained thin into Fri.
* **Fed (policy + liquidity)**

  * **Tue Dec 30 (20:00 CET):** **FOMC minutes (Dec 9–10)** confirmed a **9–3** vote to cut **25 bps** to **3.50%–3.75%** and highlighted **deep internal division** on the next steps (inflation progress vs. labor-market softening).
  * **Fed balance sheet ops (RMP):** Fed began “reserve management purchases” (technical **T-bill buying**) with an initial **~$40B** starting **Dec 12** to keep reserves “ample” (not framed as QE).
  * **Wed Dec 31:** Year-end funding squeeze: **NY Fed Standing Repo Facility usage hit $74.6B** (record), consistent with year-end liquidity needs.
* **US labor**

  * **Wed Dec 31 (14:30 CET):** **Initial jobless claims 199k** (wk ending **Dec 27**), down from **215k**, vs **~220k** expected — layoffs still low.

### THIS WEEK

* **Key theme:** Labor-market cooling signs vs. still-resilient services; tariff/legal/political headlines add tail-risk into Friday.
* **Mon Jan 5**

  * **ISM Manufacturing (Dec): 47.9** (contraction; **10th straight** month <50; lowest since Oct 2024). Tariffs cited as a drag; **Prices Paid 58.5** (still elevated); **New Orders 47.7** (still contracting).
* **Tue Jan 6**

  * **Fed internal split (discount rate):** Majority of regional Fed bank directors voted **against** the Dec discount-rate cut even though the FOMC cut policy rates — dissent referenced **AI/data-center investment strength** and expected cost pressures.
* **Wed Jan 7**

  * **ADP private payrolls (Dec): +41k** (vs **+47k** expected; prior revised **-29k**).
  * **JOLTS (Nov): openings 7.146M** (down **303k**), **hires 5.115M** (down **253k**) → softer labor demand.
  * **ISM Services (Dec): 54.4** (up from **52.6**, vs **52.3** expected). **Services employment 52.0** (back >50), **new orders 57.9**, **prices paid 64.3** (still inflationary).
* **Thu Jan 8 (today) — US data at 14:30 CET (08:30 ET)**

  * **Weekly jobless claims (wk ending Jan 3)** due.
  * **Productivity & Costs (Q3 2025, prelim)** due.
  * **Trade balance (Oct 2025, rescheduled)** due.
* **Political / legal (Trump-sensitive)**

  * **Fed leadership headline risk:** Trump has reiterated he will announce his **Fed Chair pick “early” 2026** (Powell chair term ends **May 2026**) and has signaled a preference for faster rate cuts.
  * **Fri Jan 9:** **US Supreme Court rulings day**; a central market focus is the pending decision on legality of Trump’s **IEEPA tariffs** (refund + fiscal/yields implications). Figures cited around **>$133.5B** of tariffs at risk of refund and **$150–$200B** possible refunds (timing uncertain).
  * **Defense/fiscal impulse:** Trump called for **$1.5T** military budget for **FY2027** (vs **$901B** approved for FY2026) → adds a **fiscal / issuance** angle to rate-sensitive markets.
* **Fri Jan 9 (tomorrow) — US Employment Report at 14:30 CET (08:30 ET)**

  * Reuters consensus referenced in market coverage: **Nonfarm payrolls +60k** expected; **unemployment rate 4.5%** expected (down from 4.6% in Nov, which was distorted by shutdown effects). Some sell-side previews look for **AHE ~+0.3% m/m** and **~3.6% y/y**.

### MACRO ANALYSIS

**Today’s US session is mainly about positioning into Friday’s high-volatility cluster (NFP + Supreme Court tariff ruling risk) while digesting mixed growth signals: services are firm (supports SPX risk-on), but labor indicators (ADP/JOLTS) are cooling (supports “lower yields / easier Fed” narratives). In cross-asset terms: a softer data tape typically pressures yields/USD and helps GOLD; BTC often benefits from easier-liquidity expectations but can underperform GOLD in genuine risk-off. A tariff ruling shock can reprice both inflation expectations and Treasury issuance assumptions, making rates the key transmission channel into SPX, GOLD, and BTC.**

#### OVERALL CROSS-MARKETS

* **Rates are the hub:** softer labor → lower yields / weaker USD → usually **supports GOLD** and can **support BTC + equities** if recession fear stays contained.
* **Tail-risk catalyst:** **SCOTUS tariff decision** can swing **inflation path + fiscal/issuance expectations** (yields) and **risk sentiment** quickly.
* **Fed liquidity backdrop:** ongoing technical support from Fed reserve management operations + standing repo backstop reduces funding-stress risk, but doesn’t remove macro-vol around Friday.

#### BTC & ETH

* Base case: still trades as a **high-beta liquidity proxy**; tends to like **easier Fed expectations** and **USD weakness**.
* Key risk: a true **risk-off shock** (tariff ruling surprises, yields spike, USD bid) can hit BTC harder than GOLD even if “rate-cut odds” rise. 

  
# TRADING PLAN FOR 1H_TTF (Trigger • Location • Context)

## SHORT

### **WHITE_A — Pullback continuation into 1H supply**

* **Context**: 1H + 4H remain aligned bearish (price under `1H_S_VWAP`, bearish `1H_9/21EMA`, and below `4H.active.L_BOS`). We only sell **weak pullbacks** (lower pullback volume vs prior impulse) and require CVD to roll back down on trigger.
* **Location**: Pullback into `1H.zones.SELL_1` + `1H.local.H`, ideally confluenced with the descending `1H_21EMA`.
* **Trigger**: LTF prints a pullback completion (often a liquidity sweep into `1H.zones.SELL_1`) then **bearish realignment**: LTF structure flips back down (MSB/BOS) **with bearish HVC** and CVD rollover.
* **Invalidation**: 1H acceptance above `1H.major.H_MAJOR` (pullback becomes trend reversal).
* **Setup Priority**: `A+`

---

### **ORANGE_A — Short reversal at 4H supply (sell the relief rally)**

* **Context**: This is the “HTF realign” short if price relief-rallies into stronger supply while higher-timeframe VWAPs remain above. We need **signs of exhaustion** (stalling VPA / bearish divergence) before acting—no front-running.
* **Location**: `4H.zones.SELL_1` with extension toward `1D.major.H_MAJOR`, ideally while price is still below `1D_W_VWAP`.
* **Trigger**: A clear **TTF trend death** on 1H: `TTF_L_MSB` after a sweep/failed breakout at location, followed by a low-volume pullback to the new S/R flip (then LTF entry).
* **Invalidation**: Sustained acceptance above `1D.major.H_MAJOR` (reversal has failed).
* **Setup Priority**: `A`

---

### **PURPLE_A — Fade a failed break at 1H major high**

* **Context**: In a bearish session, we only fade **failed breakouts** into resistance (classic bull-trap). Must see lack of follow-through + bearish CVD shift.
* **Location**: `1H.major.H_MAJOR` (look for `H_FSB`) with potential extension into `4H.zones.SELL_2` where `1H_50EMA` often aligns as dynamic resistance.
* **Trigger**: Sweep above `1H.major.H_MAJOR` then immediate close back below + LTF bearish MSB (confirmation), preferably on a bearish HVC/SHVC “rejection” candle.
* **Invalidation**: Acceptance and hold above `4H.zones.SELL_2`.
* **Setup Priority**: `B+`

---

### **PINK_A — Momentum scalp while pinned below the breakdown**

* **Context**: Only valid if price stays suppressed under `1H_S_VWAP` + `1H_9EMA` and continues respecting `1H.active.L_BOS` as resistance (bearish “pin”).
* **Location**: Retest underside of `1H.active.L_BOS` / `1H.zones.SELL_1`.
* **Trigger**: LTF retest → bearish continuation signal (LTF BOS/MSB down) with **ignition-style** bearish volume + falling CVD.
* **Invalidation**: Clean reclaim/acceptance above `1H.active.L_BOS` with support holds.
* **Setup Priority**: `B`

---

### **RED_A — Breakdown continuation below 1H major low**

* **Context**: Only take if breakdown is **real** (range expands + volume increases + CVD accelerates). Otherwise it’s a trap risk into demand.
* **Location**: Loss of `1H.major.L_MAJOR` with runway into `1D.zones.BUY_1` / `4H.poc.POC_2`.
* **Trigger**: `1H_L_BOS` through `1H.major.L_MAJOR` on bearish HVC/SHVC, then a **low-volume retest** of `1H.major.L_MAJOR` from below with LTF bearish confirmation.
* **Invalidation**: Sharp reclaim above `1H.major.L_MAJOR` that holds as support.
* **Setup Priority**: `B`

---

## LONG

### **BLUE_A — Counter-trend fade at demand (only if exhaustion shows)**

* **Context**: This is a **high-discipline** counter-trend attempt. Do not buy just because it’s “cheap.” You need clear seller exhaustion (stopping/absorption behavior + divergence) and then structure reclaim.
* **Location**: Sweep/hold attempt at `1H.major.L_MAJOR` with possible wick extension into `1D.zones.BUY_1`.
* **Trigger**: `L_FSB` behavior at demand + LTF bullish MSB, then reclaim and hold above `1H.active.L_BOS` (trendline reset) with CVD turning up.
* **Invalidation**: Acceptance below `1D.zones.BUY_1` with continued bearish HVC.
* **Setup Priority**: `B-`

---

### **TEAL_A — Relief-rally momentum scalp (counter-trend)**

* **Context**: Fast, nimble long only if price reclaims key intraday controls (VWAP + ST EMA). Treat as a scalp until 1H structure flips.
* **Location**: Reclaim/hold above `1H_S_VWAP` + `1H_9EMA` while sustaining above `1H.active.L_BOS`.
* **Trigger**: LTF bullish BOS/MSB on a retest of `1H.active.L_BOS` from above, with bullish HVC and rising CVD.
* **Invalidation**: Loss back below `1H.active.L_BOS` and `1H_S_VWAP`.
* **Setup Priority**: `B`

---

### **YELLOW_A — Major reversal long at daily demand**

* **Context**: Only activates if the bearish 1H trend **dies** at higher-timeframe demand (clean reversal conditions). This is the “permissioned” long.
* **Location**: Retest / defense of `1D.zones.BUY_1` (expect wicks) with downside capped well above `1D.major.L_MAJOR`.
* **Trigger**: Confirmed `TTF_H_MSB` on 1H (trend death) supported by bullish VPA (preferably HVC) + CVD shift, then first low-volume pullback to the new S/R flip with LTF confirmation.
* **Invalidation**: Acceptance below `1D.zones.BUY_1` (demand fails).
* **Setup Priority**: `A-`

---

### **GREEN_A — Breakout long only after structure flips**

* **Context**: Longs are lower probability until the tape proves reversal. This is acceptable only if breakout has **real participation** (no thin, low-volume squeeze).
* **Location**: Break and hold above `1H.major.H_MAJOR` (first step toward reversing), with overhead magnets at `4H.poc.POC_1` / `4H.zones.SELL_2`.
* **Trigger**: `1H_H_BOS` on bullish ignition (HVC/SHVC) + CVD expansion → low-volume retest of `1H.major.H_MAJOR` with LTF bullish confirmation.
* **Invalidation**: Failed retest (acceptance back below `1H.major.H_MAJOR` and back under `1H.zones.SELL_1`).
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

