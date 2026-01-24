# CONTEXT: 
## TRADER CONTEXT: 
Today is Thursday 13rd of November 2025, we are in London session, 2 hours until US session. We have no major macro events or data released today. Due to government shutdown, we have not received many major macro economic data such as NFP/Unemployment/PPI for the last month and this is expected to continue this week. Refers to `MACRO CONTEXT` for the rest of the macro events this week. 

Last month: We have officially passed October which was supposed to be bullish month for BTC and crypto in terms of seasonality during a bull cycle year, however we got the opposite of that: largest crypto liquidation sell off after sweeping the ATH followed by choppy bearish price actions despite soft CPI + Inflation data print + resolution on China-US tariffs.

Last week: ISM data released shows mixed signal and has little effects on the market so far. All markets including equities, gold find some sort of cool-off after reaching ATH, with BTC and crypto price continued its weakness after the liquididation from last month. 

This week: All macro data including PPI + CPI will NOT be released this week. Refers to the following below:
```markdown
* The Senate approved a stopgap bill on **Nov 10**; the **House passed it today**, and the White House is expected to sign it, ending the shutdown through (roughly) January. 

* **Oct CPI (was Thu, Nov 13, 8:30 ET):** The White House says **October jobs & inflation reports are unlikely to be released at all**, even after reopening, due to data-collection gaps during the shutdown. In other words, **no CPI print today**. 
* **Oct PPI (was Fri, Nov 14):** Also **subject to delay**. BLS operations have been suspended; outlets tracking the calendar warn PPI won’t publish on schedule. Expect either cancellation or a reschedule once agencies restart. 

**What to expect next:**

* Agencies will prioritize **November** data and any near-complete **September** items; **October** will likely remain a **permanent blind spot** for several series. Watch for revised calendars after the bill is signed and agencies fully reopen. ([Reuters][4])
```

Directive: Price remains at 1W range low + HTF support/demand area and find some bounces despite bearish daily trend. Given BTC 1W `OVERALL_ASSESSMENT = NEUTRAL-BEARISH`, we should remains cautious with breakout at either side of the 1W major structure and leaves room to trade mean-reversion at HTF extreme as much as possible. 

Sentiment: Public sentiment for Q4 remain bullish for BTC within its bullish 4 years cycle from a seasonality and historic standpoint. However price action last month have liquidated millions of leveraged crypto traders and enact fears with hypothesis of the top for the cycle is already set for BTC, and the start of an extended bear market into 2026. `Fear & Greed Index` worsen from 30-40 (NEUTRAL) since last month to 15 (EXTREME FEAR) - 29 (FEAR).  

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
    sr: {}
    poc:
      POC_1: 118
      POC_2: 104.7
      POC_3: 96.4
    zones:
      BUY_1: 90.1
      BUY_2: 100.3
    inactive:
      H_BOS: 109.6

  1W:
    major:
      H_MAJOR: 126.2
      L_MAJOR: 102.0
    sr:
      SR_0: 119.4
      SR_1: 114.2
      SR_2: 102.7
      SR_3: 105.6
      SR_4: 108.3
      SR_5: 100.9
    poc:
      POC_1: 115.3
      POC_2: 111.0
      POC_3: 109.6
      POC_4: 103.9
      POC_4: 101.8
    zones:
      SELL_1: 119.4
      SELL_2: 115.8
      BUY_1: 106.1
      NEUTRAL: 114.1
    active:
      L_SWEEP: 108.6
    inactive:
      L_MSB: 111.9
      H_SWEEP: 124.5

  1D:
    local: 
      H: 107.5
    major:
      H_MAJOR: 116.4
      L_MAJOR: 98.9
    sr:
      SR_1: 114.3
      SR_2: 110.5
      SR_3: 106.4
    poc:
      POC_1: 115.8
      POC_2: 112.9
      POC_3: 110.0
      POC_4: 108.2
      POC_5: 106.8
      POC_6: 103.4
    zones:
      SELL_1: 109.3
      SELL_2: 107.7
      BUY_1: 98.2
    session:
      PDH: 105.3
      PDL: 100.8
    active:
      L_BOS: 103.5
    inactive:
      H_SWEEP: 116.0

  4H:
    major:
      H_MAJOR: 105.3
      L_MAJOR: 100.8
    sr:
      SR_1: 116.4
    poc:
      POC_1: 110.8
      POC_2: 107.7
      POC_3: 106.0
      POC_4: 104.5
      POC_5: 101.3
    zones:
      SELL_1: 105.8
      NEUTRAL: 104.2
      BUY_1: 102.9
    active:
      L_BOS: 102.5
    inactive:
      H_SWEEP: 106.7
      L_MSB: 104.7
      H_BOS: 104.1

  1H:
    major:
      H_MAJOR: 104.1
      L_MAJOR: 100.8
    sr: {}
    poc: {}
    zones:
      SELL_1: 103.6
      BUY_1: 102.4
    active:
      H_BOS: 102.6
    inactive:
      H_CHOCH: 102.0
      L_MSB: 103.0

  15m:
    major:
      H_MAJOR: 104.7
      L_MAJOR: 103.2
    sr: {}
    poc: {}
    zones:
      SELL_1: 103.3
    active:
      L_BOS: 103.2
    inactive: 
      L_BOS: 103.8
```

### **1W — Super-HTF Structure**

* **Previous (~30 candles):** Strong uptrend from late ’24 into `1M.major.H_MAJOR` / `ALL.ath` `ALL.ath`, then a corrective leg confirmed **`1W.inactive.L_MSB`** that broke the weekly uptrend and retested the weekly EMAs around **1W_9/21EMA** and **`1M.inactive.H_BOS`** (ref. `1M.inactive.H_BOS`), establishing a multi-month consolidation under `ALL.ath`. The top-side was swept at **`1W.inactive.H_SWEEP`** (ATH sweep), followed by the large liquidation selloff down to **`1W.active.L_SWEEP`** with a **`1W_bearish_hammer_HVC`**, setting the range low at **`1W.major.L_MAJOR`**. Price bounced from **`1W.zones.BUY_1`** toward **`1W.zones.NEUTRAL`** and rejected alongside a bearish 9/21 EMA cross (**1W_9EMA < 1W_21EMA**), rolling back to the range floor.
* **Current (~5 candles):** Last week closed as **`1W_bearish_hammer_VC`** into the **`1M.zones.BUY_1`**/**`1M.zones.BUY_2`** demand band and the rising **1W_50EMA** (~**101–103k** by CSV). The current week is attempting a retest of the broken pivot **`1W.zones.BUY_1`** from below. HTF map: range bound between **`1W.major.L_MAJOR`** and overhead **`1W.sr.SR_1`→`1W.zones.SELL_1`**, with **1W_M_VWAP (~104.5k)** acting as mid-range reference.

---

### **1D — HTF for intraday**

* **Previous (~30 candles):** Post-liquidation recovery rallied into **`1D.major.H_MAJOR`** while probing **`1W.zones.NEUTRAL`**, then lost **1D_200EMA/MA** and rolled into a bearish swing. A decisive **`1D.active.L_BOS`** (supported by **`1H_bearish_engulfing_HVC`**) sent price back to the weekly floor and monthly demand, printing **`1D.major.L_MAJOR`** within that zone.
* **Current (~5 candles):** Bounce reclaimed **`1D.active.L_BOS`** with tails into **1D_9EMA + 1D_M_VWAP**, then tagged **`1D.zones.SELL_2`** (with **`1D_bearish_engulfing_VC`** on higher volume vs the bounce), setting **`1D.local.H`**. Since Tuesday, sellers re-asserted, losing **1D_W_VWAP** and fading toward **`1D.session.PDL`**/**`1W.sr.SR_5`**. Session refs remain **`1D.session.PDH`**/**`1D.session.PDL`**; overhead magnets: **`1D.poc.POC_1`→`POC_4`** stack.

---

### **4H — HTF for 1H**

* **Previous (~30 candles):** From **`1D.major.L_MAJOR`** base, a **4H_wedge_pattern** formed and broke out with **`4H.inactive.H_BOS`** on **`4H_bullish_VCs`**, then an immediate **`4H.inactive.H_SWEEP`** into **`1D.zones.SELL_2`**. Rejection triggered **`4H.inactive.L_MSB`** with a **`4H_bearish_engulfing_HVC`**, pushing below all EMAs/VWAPs and through **`4H.zones.BUY_1`**, confirming **`4H.active.L_BOS`** and setting the leg’s floor at **`4H.major.L_MAJOR`**.
* **Current (~5 candles):** Structure is a **4H_descending_channel** (LH/LLs). Latest upswing from **`4H.major.L_MAJOR`** shows **`4H_bullish_VCs`** but still lighter than the prior sell leg; price has **reclaimed** the **`4H.active.L_BOS` + `4H.zones.BUY_1`** pivot and is retesting **`4H.zones.NEUTRAL`** with **4H_9/21EMA** descending overhead and **4H_W_VWAP (~104.2k)** capping.

---

### **1H — TTF (execution)**

* **Previous (~30 candles):** Bounce from **`4H.major.L_MAJOR`** inside the 4H channel produced **`1H.active.H_BOS`**, reclaiming the **`4H.active.L_BOS` + `4H.zones.BUY_1`** pivot and then testing **`1H.zones.SELL_1`** overlapping **`4H.zones.NEUTRAL`**.
* **Current (~5 candles):** A local top printed at **`1H.major.H_MAJOR`** after a **`1H_bearish_inverted-hammer_VC`** and **`1H_bearish_engulfing_VC`** follow-through; pullback retested the pivot with **1H_9/21EMA** and **S_VWAP (~102.7k)** beneath while **1H_200EMA (~104.1k)** and **W_VWAP (~104.3k)** sit above as dynamic resistance. CVD/RSI on the hour are mid-range (RSI ~51 vs RSI_MA ~47) — watch divergence at the edges.

## MACRO CONTEXT
### LAST WEEK

* **Policy/Tariffs:** The White House flagged a US–China de-escalation path: Section 301 tariff **exclusions extended** and a one-year **suspension** of a China end-user controls rule (effective **Nov 10**), softening near-term tariff overhang even as the broader 2025 tariff regime (via July 31 EO) still looms over costs and supply chains.
* **Fed:** Fed Vice-Chair **Jefferson (Nov 7)** leaned **cautious/gradual** on future cuts, citing **limited official data** and a still-restrictive stance.
* **Data vacuum:** The **government shutdown** created a **gap in October macro data** (CPI/employment in jeopardy), forcing markets to lean on private proxies and keeping the Fed “data-light.”
* **Crypto flows:** After a rough streak into early November, **US spot BTC ETFs** briefly flipped **back to inflows** late last week; **ETH ETFs** remained more mixed/negative.
* **Gold demand tone:** WGC’s **Q3** update showed **elevated central-bank buying** and strong investment demand—supportive backdrop into year-end.

### THIS WEEK

* **Fed calendar:** **FOMC Minutes (Oct 28–29) – Wed, Nov 19, 2:00**; **Beige Book – Wed, Nov 26, 2:00**.
* **Earnings/AI:** **NVIDIA Q3 FY26 results – Wed, Nov 19 (2:00 pm PT)**; a key read-through for AI capex/risk appetite.
* **Derivatives & Liquidity:** **Monthly OPEX – Fri, Nov 21** (third Friday); potential **gamma pin/vol crush** into the close.
* **Holidays/Hours:** **Thanksgiving – Thu, Nov 27 (markets closed); Fri, Nov 28 early close (NYSE 1:00 pm ET; CME holiday schedule in effect)**—liquidity typically fades mid-to-late next week.
* **Crypto micro:** US spot **BTC ETFs posted a strong single-day net inflow (Tues)** after prior outflows; **ETH ETFs** saw **net outflows** the same day. **Solana spot ETF** (launched Oct 28) continues to attract attention, potentially diverting some alt-beta flows.

### MACRO ANALYSIS

#### BTC & ETH

Crypto beta is **toggling with US risk tone** and ETF flows. A sharp **BTC ETF inflow day** helped stabilize after October’s deleveraging; **ETH ETFs** remain softer on balance, while **SOL ETF** buzz may siphon some alt flow. For disciplined execution: let **macro prints** (Fri) set USD/liquidity tone; track **daily ETF flows** as confirmation. **BTC** tends to firm with equities/AI-beta up and real yields steady-to-lower; **ETH** likely lags if outflows persist—prefer **reaction buys** only when flows + LTF PA/CVD align.

  
# TRADING PLAN FOR 1H_TTF (Trigger • Location • Context)

### **ORANGE_A — Short reversal at 1H supply**

* **Context:** 1H bounce is pressing into overhead confluence while HTFs (1D/4H) lean **neutral-bearish** under EMAs. Expect **weakening bullish VPA** or **bearish RSI/CVD divergence** as price retests the supply shelf. Overhead dynamic resistances: **1H_200EMA (~104.1k)** and **W_VWAP (~104.3k)**.
* **Location:** `1H.zones.SELL_1` + `4H.zones.NEUTRAL` beneath `1H.major.H_MAJOR`.
* **Trigger:** Failed push/`H_SWEEP` of `1H.major.H_MAJOR` or rejection inside `1H.zones.SELL_1` → **LTF_L_MSB** with falling CVD.
* **Invalidation:** 1H acceptance **above** `1H.major.H_MAJOR` with **1H_H_BOS** and rising CVD (defer to **GREEN_A**).
* **Setup Priority:** **A-**

---

### **ORANGE_B — Short reversal at 4H cap (extension scenario)**

* **Context:** If 1H extends higher through the channel top, expect sellers near stronger HTF caps.
* **Location:** `4H.major.H_MAJOR` / extension into `4H.zones.SELL_1` if filled; watch proximity to `1D.session.PDH`.
* **Trigger:** Top-side **liquidity sweep** → **TTF_L_MSB (1H)** with bearish HVC or CVD roll.
* **Invalidation:** 1H acceptance above `4H.major.H_MAJOR` with sustained bid (higher-timeframe breakout).
* **Setup Priority:** **A**

---

### **PURPLE_A — Short fade on `H_SWEEP` of 1H high**

* **Context:** Range-fade inside the 4H channel; look for exhaustion/absorption at the 1H top.
* **Location:** `1H.major.H_MAJOR` overlapping `1H.zones.SELL_1` / `4H.zones.NEUTRAL`.
* **Trigger:** **`H_SWEEP`** and close back in range + **LTF_L_MSB** with CVD divergence.
* **Invalidation:** 1H close and hold above `1H.major.H_MAJOR`.
* **Setup Priority:** **B+**

---

### **PINK_A — Short momentum if intraday support fails**

* **Context:** Counter-trend scalp only if momentum flips down: loss of **S_VWAP (~102.7k)** and **1H_9/21EMA** while **below** `1H.active.H_BOS` and the `4H.zones.BUY_1` pivot.
* **Location:** Below the `4H.zones.BUY_1` / `4H.active.L_BOS` pivot band.
* **Trigger:** **LTF_L_BOS/MSB** with bearish HVC and negative CVD → sell the retest.
* **Invalidation:** Fast reclaim of **S_VWAP** + **1H_9/21EMA** with HL sequence restored.
* **Setup Priority:** **B**

---

### **RED_A — Breakdown of 4H/PDL floor**

* **Context:** Trend continuation short if the higher-timeframe floor gives way.
* **Location:** Clean break **below** `4H.major.L_MAJOR` / `1D.session.PDL`.
* **Trigger:** **`1H_L_MSB/BOS`** through the level on strong sell VPA and falling CVD → enter on **low-volume retest**.
* **Invalidation:** Reclaim back **above** `1D.session.PDL` with bullish HVC (structure failure).
* **Setup Priority:** **B**

---

### **BLUE_A — Long fade on `L_SWEEP` at 4H/PDL**

* **Context:** Buy the failed breakdown only if sellers exhaust at the weekly floor area; prefer RSI/CVD **bullish divergence**.
* **Location:** `4H.major.L_MAJOR` / `1D.session.PDL` with proximity to `1W.sr.SR_5`.
* **Trigger:** Stop-run (`L_SWEEP`) → **LTF_H_MSB** back into range, then reclaim **S_VWAP**.
* **Invalidation:** 1H acceptance below `4H.major.L_MAJOR` (hand off to **RED_A**).
* **Setup Priority:** **B-**

---

### **WHITE_A — Long continuation on pullback to broken pivot**

* **Context:** If buyers defend the reclaim, look for a classic pullback buy.
* **Location:** Retest of **`1H.active.H_BOS` + `4H.zones.BUY_1`** band with **1H_9EMA + S_VWAP (~102.7k)** confluence.
* **Trigger:** **LTF_H_MSB/BOS** after a **low-volume** dip; CVD turns up.
* **Invalidation:** Clean 1H close **below** the band with bearish HVC.
* **Setup Priority:** **B**

---

### **YELLOW_A — Long major reversal (deeper capitulation)**

* **Context:** If a deeper flush pushes into the extremes, we only act on decisive reversal evidence.
* **Location:** `4H.major.L_MAJOR` with extension down toward `1D.major.L_MAJOR`.
* **Trigger:** **TTF_H_MSB (1H)** after a stopping/absorption HVC and bullish CVD divergence.
* **Invalidation:** New LLs accepted below `4H.major.L_MAJOR`.
* **Setup Priority:** **A-**

---

### **GREEN_A — Long breakout & retest above 1H cap**

* **Context:** If supply is absorbed and momentum ignites, join the trend through resistance.
* **Location:** First clean break **and retest** above `1H.major.H_MAJOR` / `4H.zones.NEUTRAL`.
* **Trigger:** **`1H_H_BOS` + bullish HVC** → shallow pullback; enter on **LTF_H_BOS** with rising CVD.
* **Invalidation:** Failure retest (acceptance back below `1H.major.H_MAJOR`) or immediate **`1H_L_CHOCH`** after entry.
* **Setup Priority:** **B**


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
- 1W: `OVERALL-ASSESSMENT = NEUTRAL-BEARISH`.
- `PG` grades are assessed based on the plan full viability. DO NOT DEGRADE the plan based on probability/possibility.  
- DO NOT PERFORM TTI on the 1W_TF. 