# CONTEXT: 
## TRADER CONTEXT: 
Today: Today is Monday 15th of December 2025, we are in London session, 1 hours until US session. We have no major data/macro event released today. Refers to `MACRO CONTEXT` for the rest of the macro events this week.  

Last month: We have officially passed October + November which was supposed to be bullish month for BTC and crypto in terms of seasonality during a bull cycle year, however we got the opposite of that: largest crypto liquidation sell off and continuation of weekly downtrend breaking bullish structure for the cycle despite soft CPI + Inflation data print + resolution on China-US tariffs.

Last week: Marked the end of Quantitative Tightening cycle from the FED. Market pricing in and reacting to 25bps rate cut from FOMC last week.

Directive: Price is bearish on weekly timeframe howvever favor mean-reversion within daily consolidation pattern with short are prioritize however caution due to bearish extension into monthly support/demand zone with prior oversold signals. 

Sentiment: With price action last month that have liquidated millions of leveraged crypto traders and enact fears, the general consensus is bearish with hypothesis of the top for the cycle is already set for BTC, and the start of an extended bear market into 2026. `Fear & Greed Index` worsen from 30-40 (NEUTRAL) since last month to 14-19 (EXTREME FEAR) last week and improving toward 16-20 (FEAR) this week as price temporarily stall on the weekly downtrend.   

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
    active:
      L_BOS: 107.3
    inactive:
      L_MSB: 111.9
      H_FSB: 124.5
      L_FSB: 108.6

  1D:
    local:
      H: 92.3
      L: 89.2
    major:
      H_MAJOR: 94.6
      L_MAJOR: 87.7
    sr:
      SR_1: 93.4
      SR_2: 89.5
      SR_3: 88.4
    poc:
      POC_1: 103.4
      POC_2: 95.7
      POC_3: 90.2
      POC_4: 84.6
      POC_5: 79.7
    zones:
      SELL_1: 98.5
      SELL_2: 94.2
      SELL_3: 89.9-91.0
      BUY_1: 85.9
      BUY_2: 88.1
    session:
      PDH: 90.0
      PDL: 85.2
    active:
      L_BOS: 87.7
    inactive:
      H_FSB: 94.2
      L_CHOCH: 89.2

  4H:
    major:
      H_MAJOR: 90.1
      L_MAJOR: 87.6
    sr:
      {}
    poc:
      POC_1: 95.0
      POC_2: 92.4
      POC_3: 86.4
      POC_4: 82.2
    zones:
      SELL_1: 87.6-88.2
    active:
      L_BOS: 87.5
    inactive:
      L_BOS: 89.3

  1H:
    local: 
      H: 86.6
      L: 85.3
    major:
      H_MAJOR: 86.6
      L_MAJOR: 85.2
    sr: {}
    poc: {}
    zones:
      BUY_1: 85.5
      SELL_1: 86.6
      NEUTRAL: 85.9
    active:
      H_FSB: 86.6
    inactive:
      L_BOS: 87.6

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

* **Previous (~30 candles):** After the late ’24 `1M_bullish_channel`, weekly momentum weakened with `1W.inactive.L_MSB` while distributing under `ALL.ath` / `1M.major.H_MAJOR`. A brief ATH probe (`1W.inactive.H_FSB`) failed, then the liquidation leg drove a confirmed `1W.active.L_BOS` through `1W.inactive.L_FSB` with a run of `1W_bearish_trend_VC/HVC` (impulse volume > pullback volume), and a bearish `1W_9/21EMA` regime. The selloff broke below the historic bull-market band (prior support around `1M.inactive.H_BOS` → `1W.poc.POC_1`) and flushed into monthly demand `1M.zones.BUY_2`, extending toward `1M.poc.POC_4` / `1M.sr.SR_4`, where downside progress started stalling.
* **Current (~5 candles):** Basing attempt is forming **inside the monthly demand area** `1M.zones.BUY_2` with weekly support nearby at `1W.sr.SR_3` and weekly magnet `1W.poc.POC_4`. Trend context remains **bearish** while price is below `1W.zones.SELL_2` / `1W.sr.SR_1` and under the falling `1W_9/21EMA` (current 1W candle is **very low volume** vs `1W_vol_ma20`, and `1W_RSI` remains < 50).

---

### **Daily (1D – HTF for intraday)**

* **Previous (~30 candles):** Downtrend leg (OBV-confirmed per trader note) exhausted into the **monthly demand** `1M.zones.BUY_2`, printing the key absorption event `1D_bearish_hammer_HVC` with `1D_RSI` oversold (<25 at the time, per trader note). Recovery transitioned into a `1D_ascending_wedge` capped by `1D.major.H_MAJOR` / `1D.zones.SELL_2` and the descending `1D_21EMA`. The most recent rejection from `1D.inactive.H_FSB` rolled into `1D.active.L_CHOCH`, breaking the wedge base and shifting back toward the range low. Importantly: that bearish leg was **low-volume** relative to the prior impulse (supports “range/consolidation” rather than fresh trend ignition).
* **Current (~5 candles):** Price is rotating under `1D.zones.NEUTRAL` (mid-range) while repeatedly reacting around `1D.sr.SR_2` (which aligns with `1M.zones.BUY_2`). `1D_9/21EMA` is flattening (compression), `1D_W_VWAP` is acting as a nearby pivot while `1D_M_VWAP` sits overhead (dynamic resistance). Session refs: `1D.session.PDH` above and `1D.session.PDL` below; breakdown acceptance below `1D.session.PDL` risks a push toward `1D.major.L_MAJOR` / `1D.poc.POC_4`.

---

### **4H (4H – HTF for 1H)**

* **Previous (~30 candles):** Inside the daily range, sellers maintained control under the descending `4H_200EMA/MA` while the leg probed lower and confirmed `4H.active.L_BOS` (weekend). The dump extended into the **range-low complex** around `4H.major.L_MAJOR` / `1D.session.PDL` / `1D.major.L_MAJOR`, then snapped back with a `4H_bullish_engulfing_VC` (higher volume than the immediate prior bars per chart) reclaiming the broken `4H.active.L_BOS`, `4H_9EMA`, and `4H_W_VWAP`. Price put in LL however OBV has not confirmed a LL on this timeframe. 
* **Current (~5 candles):** Follow-through is **weak** (current 4H volume is low vs `4H_vol_ma20`). Price is holding above `4H_9EMA` and `4H_W_VWAP` but remains capped beneath `4H_21EMA/50EMA` and well below `4H_200EMA/MA`. Overhead supply stack: `4H.zones.SELL_2` then `4H.zones.SELL_1` (aligns with `1D.zones.NEUTRAL` overhead). 

---

### **1H (1H – TTF)**

* **Previous (~30 candles):** Weekend breakdown reclaimed liquidity below `1D.zones.NEUTRAL` and rotated down toward `1D.session.PDL` / `4H.major.L_MAJOR`. The reversal signal on the TTF is the `1H.active.H_CHOCH`, followed by a recovery reclaiming `1H_S_VWAP`/`1H_W_VWAP` and a bullish `1H_9/21EMA` posture, then a test into `1H.zones.SELL_1` (confluence with the still-descending `1H_50EMA`). CVD remains flat to slightly negative for the session. OBV remains inline with price. 
* **Current (~5 candles):** Tight consolidation between `1H.local.H` and `1H.local.L`, with price chopping below `1H.zones.SELL_1` and below the higher confluence band `1D.zones.NEUTRAL` → `4H.zones.SELL_1`. `1H_RSI` is >50 (constructive), but price is still under `1H_200MA/EMA` (macro bearish cap). CVD starting to turn negative with this recent roll-over consolidation. 

## MACRO CONTEXT
### LAST WEEK

* **Fed (FOMC Dec 9–10):** **25bp cut** to **3.50%–3.75%** with **dissent** (some wanted 50bp, others no change). Fed flagged elevated uncertainty + rising downside employment risks; also noted readiness to buy short-term Treasuries as needed to keep reserves “ample.”
* **Data distortion risk:** Ongoing **post–government shutdown** fallout kept markets trading “headline-to-headline” on **revised / incomplete** macro prints (esp. inflation/labor series).
* **Risk appetite / flows:** Post-cut tone supported **risk rotation** and **fund flows** (equity + gold/precious-metals-focused commodity funds saw notable inflows in weekly flow data).
* **Tech/AI tape:** AI leaders saw **selective de-risking** (capex/valuation worries) → potential drag on NQ/SPX beta into year-end.

### THIS WEEK

* **Tue Dec 16 (08:30 ET): Employment Situation (Nov 2025)** — delayed release; includes **Oct establishment survey data** (Oct household unemployment rate **not** available).
* **Thu Dec 18 (08:30 ET): CPI (Nov 2025) + Real Earnings (Nov 2025)** — **Oct CPI headline/core not published**; Nov CPI release has **missing 1-month % changes** where Oct data are absent.
* **Shutdown aftershocks (ongoing):** Several BLS series canceled/rescheduled; expect **higher noise / lower signal** and faster narrative swings around each release.
* **Policy / politics (tariffs):** Supreme Court legal risk around tariff authority remains an overhang; administration signals it can replicate tariff revenue even if legal basis is struck.
* **Market microstructure:** **Triple witching Fri Dec 19** → elevated index/vol flows; more “pinning/whipsaw” risk around key levels.
* **Crypto-regulation catalyst:** US regulators moving toward deeper integration (e.g., trust-bank approvals) → sentiment tailwind vs. “policy shock” risk.

### MACRO ANALYSIS

Cross-market setup for **today (Mon Dec 15)**: last week’s **Fed cut** supports **risk assets** (SP500 + high-beta crypto) *unless* this week’s **delayed labor/CPI** prints reprice the path (hawkish inflation read → higher real yields/USD → risk-off). The key macro trap is **data quality**: shutdown-related gaps can create **false trend signals**, so treat breakouts as more failure-prone and size/hold time accordingly. Watch **USD + real yields** as the “master switch”: rising real yields typically pressure **GOLD** and often **BTC/ETH** (via liquidity/risk), while easing yields can reflate both—BTC/ETH usually as “high beta Nasdaq,” gold as “real-rate hedge.”

#### BTC & ETH

* Bull case: easing liquidity expectations + constructive regulatory headlines → supports dip-buying (risk-on correlation).
* Bear case: hot/uncertain CPI + whipsaw labor data → higher vol + risk-off; treat moves as **fragile** until yields confirm.
  
# TRADING PLAN FOR 1H_TTF (Trigger • Location • Context)

## SHORT

### **ORANGE_A — Short reversal at 1D mid-range supply**

* **Context**: HTF bias still leans bearish (`1W.active.L_BOS` + daily compression after `1D.active.L_CHOCH`). The current 1H bounce is corrective unless it can accept above `1D.zones.NEUTRAL`. Expect weakening bullish VPA into overhead supply (pushes on **decreasing** volume; pullbacks on **increasing** volume = red flag). Require bearish CVD shift (chart-confirm) + loss of `1H_S_VWAP` to validate sellers.
* **Location**: `1D.zones.NEUTRAL` confluence with `4H.zones.SELL_1` and dynamic cap from `4H_200EMA/MA` (plus `1H_200MA/EMA` overhead context).
* **Trigger**: Sweep/hesitation into the band → **TTF_L_MSB** (1H major LH break) + bearish VPA (sell VCs expanding; failed bullish follow-through).
* **Invalidation**: Clean acceptance and hold above `1D.zones.NEUTRAL` (then this becomes long-biased / stand aside).
* **Setup Priority**: `A`

---

### **WHITE_A — Short continuation on pullback into 1H supply (ACTIVE)**

* **Context**: Best “sell-the-rip” if the bounce remains corrective under the 1H/4H MA stack. We want **weak pullback volume** into `1H.zones.SELL_1`, then sellers show up (bearish VCs) with CVD rolling over (chart-confirm). No entry if price is still holding above `1H_S_VWAP` with improving VPA.
* **Location**: `1H.zones.SELL_1` + descending `1H_50EMA` (and below `4H.zones.SELL_2` / `1D.zones.NEUTRAL` overhead).
* **Trigger**: LTF (15m/5m) **L_MSB** after rejection (prefer a `1H_bearish_rejection_VC` or `1H_bearish_engulfing_HVC` at the zone edge).
* **Invalidation**: 1H acceptance above `1H.zones.SELL_1` that flips to support (and holds above `1H.local.H`).
* **Setup Priority**: `A+`

---

### **PURPLE_A — Short fade of 1H range high (failed break)**

* **Context**: Pure range play: only short if buyers fail to break/hold the top (classic FSB behavior). Ideal: push into highs on **waning** volume + bearish divergence signals on chart tools (CVD/RSI), then snap back below VWAP.
* **Location**: `1H.local.H` → extension toward `1H.major.H_MAJOR` with confluence from `1D.session.PDH` and `4H.zones.SELL_2`.
* **Trigger**: Wick-through/sweep then close back inside range + LTF **L_MSB** back below `1H.local.H`.
* **Invalidation**: 1H close above `1H.major.H_MAJOR` with follow-through (range breaks = no fade).
* **Setup Priority**: `B+`

---

### **PINK_A — Short momentum scalp on breakdown of local range**

* **Context**: Only if the current tight range resolves down and aligns back with HTF bearish pressure. Must see sell-side initiative: expanding bearish VCs and (chart-confirm) negative CVD impulse; avoid if breakdown happens on “no volume” and instantly reclaims VWAP (likely fakeout).
* **Location**: Breakdown below `1H.local.L`, while price remains below `1H_S_VWAP` and `1H_9/21EMA` flips bearish.
* **Trigger**: **TTF_L_CHOCH** (loss of `1H.local.L`) → LTF **L_BOS/MSB** on retest of the broken range floor.
* **Invalidation**: Reclaim `1H.local.L` + hold back above `1H_S_VWAP`.
* **Setup Priority**: `B+`

---

### **RED_A — Short breakdown of the daily range low complex**

* **Context**: High-conviction continuation only if the major supports fail with **sell ignition** (bearish HVC/SHVC relative to TTF MA cloud) and CVD confirms. Expect the best entry on the **low-volume retest** after the break.
* **Location**: Loss of `1D.session.PDL` / `4H.major.L_MAJOR` / `1D.major.L_MAJOR`.
* **Trigger**: Confirmed `1H_L_BOS` through the complex → low-volume retest from below + LTF **L_MSB/BOS** continuation.
* **Invalidation**: Sharp reclaim back above `1D.session.PDL` with bullish VPA (failed breakdown).
* **Setup Priority**: `B`

---

## LONG

### **BLUE_A — Long fade at the range-low complex (failed breakdown)**

* **Context**: Wait for a second sweep of 1D range low. Counter-trend fade **only** if sellers fail to hold below the complex (FSB). Need clear stopping behavior: sell impulse loses range expansion, follow-up candles can’t continue, and chart-confirm CVD stops falling / turns up. 
* **Location**: `1H.major.L_MAJOR` / `4H.major.L_MAJOR` / `1D.session.PDL` (and first upside magnet back to `1H.zones.SELL_1`).
* **Trigger**: Sweep below then reclaim + LTF **H_MSB** back above the level (prefer a strong bullish reversal VC).
* **Invalidation**: Acceptance below `1D.session.PDL` (then defer to **RED_A**).
* **Setup Priority**: `B-`

### BLUE_A (ACTIVE NOW)
Similar setup Long based on the 1H_H_CHOCH signal off the first sweep of the 1D_L_MAJOR prior. Entry on a low volume retest at broken level `1H.active.L_CHOCH` + `1H.zones.BUY_1`
---

### **TEAL_A — Long counter-trend scalp on reclaim of local high**

* **Context**: Only take if buyers show real initiative (bullish VCs expanding, pullbacks weak) and price can hold above `1H_S_VWAP`. This is a scalp because HTF still caps overhead.
* **Location**: Reclaim/acceptance above `1H.local.H` while holding above `1H_S_VWAP` and rising `1H_9EMA`.
* **Trigger**: LTF **H_BOS/MSB** on retest of the breakout base (do not chase the first spike).
* **Invalidation**: Immediate failure back below `1H.local.H` and `1H_S_VWAP`.
* **Setup Priority**: `B`

---

### **YELLOW_A — Long major reversal from monthly demand**

* **Context**: This is the “real reversal” path: we only act if the market prints a **TTF trend-death** signal against the bearish pressure (per protocol). We want bullish divergence + buyers defending the monthly demand band, then a decisive 1H reversal structure with improving VPA (bullish impulse volume > pullback volume).
* **Location**: Retest of `1D.major.L_MAJOR` / `1D.zones.BUY_2` with possible extension toward `1D.zones.BUY_1`, all within the broader monthly demand `1M.zones.BUY_2`.
* **Trigger**: **TTF_H_MSB** (1H breaks a major swing high) → low-volume retest of the new S/R flip.
* **Invalidation**: Continued acceptance below `1D.major.L_MAJOR` (no reversal structure = no trade).
* **Setup Priority**: `A-`

---

### **GREEN_A — Long breakout above the 1H range high**

* **Context**: Only valid if the range resolves upward with **buy ignition** and CVD confirms (chart). This would shift the session from “bounce” to “breakout attempt,” but we still respect HTF overhead until acceptance proves otherwise.
* **Location**: Break/accept above `1H.major.H_MAJOR` and `1D.sesssion.PDH`.
* **Trigger**: Confirmed `1H_H_BOS` through the ceiling with bullish HVC → **low-volume retest** + LTF **H_MSB/BOS** continuation.
* **Invalidation**: Failed retest (acceptance back below `1H.major.H_MAJOR` and `1D.sesssion.PDH`).
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

