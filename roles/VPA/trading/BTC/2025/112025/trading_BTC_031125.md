# CONTEXT: 
## TRADER CONTEXT: 
Today is Monday 3rd of November 2025, we are in London session, 3 hours until US session. We have ISM Manufacturing PMI as major event & data released today in 4 hours. Due to government shutdown, we have not received many major macro economic data such as NFP/Unemployment/PPI for the last 3 week and this is expected to continue this week.  Refers to `MACRO CONTEXT` for the rest of the macro events this week. 

Last month: We have officially passed October which was supposed to be bullish month for BTC and crypto in terms of seasonality during a bull cycle year, however we got the opposite of that: largest liquidation sell off after sweeping the ATH followed by choppy price actions at the bottom of the 1W range despite dovish FED comments and soft CPI + Inflation data print. 

Last week: Market seems to be responded positive to FED decisions coupled with positive resolution on China-US tariffs news which allow US equities putting new ATH, BTC recovering and cool-off on gold hyperbolic bullruns, signaling a potential risk-off environment. We also had FOMC last Wednesday in which the key details are outlined below:
```markdown
* **Cut 25 bps** to a **3.75%–4.00%** fed-funds target range; **two dissents** (Miran wanted –50 bps; Schmid preferred no change).
* **Ended QT effective Dec 1**: the Committee will **stop shrinking the balance sheet** and **reinvest all principal** thereafter (Treasuries rolled over; **all agency/MBS principal reinvested into T-bills**).
* **Operating settings** (implementation note): **IORB 3.90%**, **ON RRP 3.75%**, **SRF min 4.00%**, $500B aggregate SRF limit, RRP **$160B per-counterparty**.
* **Powell’s tone**: another cut in **December is “not a foregone conclusion,”** stressing data uncertainty amid the shutdown. 
* **Context & reaction**: Statement added emphasis on **rising downside risks to employment**; markets whipsawed as traders digested the **easing + QT end** vs **no December pre-commitment**.

> Why this matters: Ending QT + a 25-bp cut = **easier financial conditions via reserves/liquidity** and **lower policy rate**, but Powell explicitly **kept optionality**, so the **path** (not the single cut) drives cross-asset pricing.
```

This week/Trader Directive: Despite bearish trend, given BTC 1W `OVERALL_ASSESSMENT = NEUTRAL`, we should remains cautious with breakout at either side of the 1W major structure and try to trade mean-reversion at extreme as much as possible. 

Sentiment: Public sentiment for Q4 remain bullish for BTC within its bullish 4 years cycle from a seasonality and historic standpoint. However price action last month have liquidated millions of leveraged crypto traders and enact fears with hypothesis of the top for the cycle is already set for BTC, and the start of an extended bear market into 2026. `Fear & Greed Index` is currently sitting at 36-42 (FEAR) improved from below 30 (EXTREME FEAR) from last week. 



## TECHNICAL CONTEXT
### Key Levels 

```yaml
meta:
    pair: BTCUSDT
    units: "k"   # all numbers rounded with 'k'
    note: "Ranges use '-', e.g., 113.2-114.7k"

levels:
  ALL:
    ath: 126.2k

  1M:
    major: 
      H_MAJOR: 126.2k
      L_MAJOR: 74.5k
    sr: {}
    poc:
      POC_1: 118k
      POC_2: 104.7k
      POC_3: 96.4k
    zones: 
      BUY_1: 90.0k
      BUY_2: 100.2k
    inactive:
      H_BOS: 109.6k

  1W:
    major:
      H_MAJOR: 126.2k
      L_MAJOR: 102.0k
    sr:
      SR_0: 119.4k
      SR_1: 114.2k
      SR_2: 102.7k
      SR_3: 105.6k
      SR_4: 108.3k
    poc:
      POC_1: 115.3k
      POC_2: 111.2k
      POC_3: 109.6k
      POC_4: 121.7k
    zones:
      SELL_1: 120.2k
      BUY_1: 106.1k
      NEUTRAL: 114.1k
    active:
      L_SWEEP: 108.6k
    inactive:
      L_MSB: 111.9k
      H_SWEEP: 124.5k

  1D:
    local: 
      L: 106.7k
    major: 
      H_MAJOR: 116.4k  
      L_MAJOR: 103.5k  
    sr: 
      SR_1: 114.3k
      SR_2: 110.5k
      SR_3: 106.4k
    poc:
      POC_1: 115.8k
      POC_2: 112.9k
      POC_3: 110.0k
      POC_4: 108.1k
      POC_5: 106.9k
    zones:
      SELL_1: 113.2k
      BUY_1: 107.3k
      NEUTRAL: 110.0k
    session:
      PDH: 111.2k
      PDL: 109.5k
    active: 
      H_SWEEP: 116.0k
    inactive:
      H_CHOCH: 114.0k
      L_BOS: 109.6k


  4H:
    major:                 
      H_MAJOR: 112.2k    
      L_MAJOR: 106.3k    
    sr:
      SR_1: 116.4k
    poc: 
      POC_1: 110.8k
      POC_2: 107.7k
    zones:
      SELL_1: 109.1-109.6k
    active:
      L_BOS: 108.6k
    inactive: 
      H_CHOCH: 111.2k

  1H:
    major:
      H_MAJOR: 107.8k
      L_MAJOR: 106.9k
    sr: {}
    poc: {}
    zones:
      SELL_1: 108.1k
      NEUTRAL: 107.5k
    active:
      L_SWEEP: 107.0k
    inactive: 
      H_MSB: 110.3k
      L_MSB: 109.5k

  15m:
    major:
      H_MAJOR: 111.6k
      L_MAJOR: 113.7k
    sr: {}
    poc: {}
    zones:
      SELL_1: 112.7k
      BUY_1: 111.1k
    active:
      L_SWEEP: 110k
    inactive: 
      L_MSB: 113.6k
```

### **1W — Super-HTF Structure**

* **Previous (~30 candles):** Strong uptrend into **ATH** `ALL.ath` / `1W.major.H_MAJOR`, then a corrective leg confirmed **`1W.inactive.L_MSB`**, which retested the prior monthly break **`1M.inactive.H_BOS`** around the weekly EMA band. A 3-month range formed between **`1W.zones.BUY_1`** and **`1W.zones.SELL_1`**, with multiple sweeps: the late ATH-side **`1W.inactive.H_SWEEP`** and last month’s **`1W.active.L_SWEEP`** near **`1W.major.L_MAJOR`**. Bounces from **`1W.zones.BUY_1`** failed to reclaim weekly moving-average support; sellers defended the mid-range at **`1W.zones.NEUTRAL`** / `1W.poc.POC_2`.
* **Current (~5 candles):** Rollover from **`1W.zones.NEUTRAL`** toward the range-low territory—monitor **`1W.sr.SR_3` → `1W.sr.SR_2` / `1W.zones.BUY_1`**. Above, supply sits at **`1W.zones.SELL_1`** with HVN magnets **`1W.poc.POC_1`** / **`1W.poc.POC_4`**. HTF bias: **Range-neutral → leaning bearish** unless the weekly reclaims the EMA band and **`1W.poc.POC_2`**.

---

### **1D — HTF for intraday**

* **Previous (~30 candles):** From the 1W range top, a **`1D_bearish_engulfing_HVC`** liquidation leg swept weekly lows into **`1W.major.L_MAJOR`**, then was absorbed back inside the weekly range. Structure coiled into a **`1D_wedge_pattern`**: HL base near **`1D.zones.BUY_1`** / **`1W.zones.BUY_1`** and horizontal resistance at **`1D.major.H_MAJOR`** overlapping **`1W.zones.NEUTRAL`**.
* **Current (~5 candles):** Latest upswing was rejected below **`1D.zones.NEUTRAL`** and **`1D.sr.SR_2`**, then rolled lower on **building `1D_bearish_VCs`** toward the wedge base near **`1D.zones.BUY_1`**. Price trades **below `1D_200EMA/MA`** and **below `1D` W-VWAP** (indicator table), with RSI < 50. Overhead magnets/resistances: **`1D.poc.POC_4` (≈ with `1H.zones.SELL_1`)**, **`1D.poc.POC_3`**, and **`1D.session.PDH`**. Below: **`1D.sr.SR_3`** / **`1D.local.L`**. Bias: **Bearish while below `1D.zones.NEUTRAL`**.

---

### **4H — HTF for 1H**

* **Previous (~30 candles):** Trend-down from the daily range top into **`4H.major.L_MAJOR`**, confluence **`1D/1W.zones.BUY_1`**. Weekend bounce ran toward **`1D.zones.NEUTRAL`**, then a failed break at **`4H.inactive.H_CHOCH`**; sellers re-asserted trend with **`4H.active.L_BOS`** supported by a **`4H_bearish_engulfing_VC`**.
* **Current (~5 candles):** Price is **below all 4H EMAs (9/21/50/200)** and **below W-VWAP / M-VWAP** (indicator table). The impulse is driving back toward **`4H.major.L_MAJOR`** / **`1D.zones.BUY_1`**. Overhead supply: **`4H.zones.SELL_1 (109.1–109.6k)`**, aligning with **`1D.poc.POC_4`** and prior **`4H.inactive.H_CHOCH`** base. Bias: **Bearish; sell rallies into `4H.zones.SELL_1` unless 4H structure flips**.

---

### **1H — TTF (execution timeframe)**

* **Previous (~30 candles):** Asia session produced a clean trend-down: failed break at **`1H.inactive.H_MSB`** → immediate **`1H.inactive.L_MSB`** toward the wedge base (**`1D.zones.BUY_1`**). The leg printed **`1H_bearish_HVCs`** with persistent **negative CVD (~-1.7k)**.
* **Current (~5 candles):** Bearish consolidation under **all 1H EMAs (9/21/50/200)** and **S-VWAP / W-VWAP**. A fresh **`1H.active.L_SWEEP`** formed near **`1D.zones.BUY_1`**, with **`1H.zones.NEUTRAL`** acting as mid-range pivot. RSI is **oversold** (≈23) and trying to base, but no confirmed bullish divergence signal and **confirmation is absent** while price stays below **`1H.major.H_MAJOR`** and **S-VWAP**. Bias: **Bearish / bounce-sold until `1H` structure flips**.
  
## MACRO CONTEXT
### LAST WEEK

* **Fed:** The FOMC cut the policy rate **25 bps to 3.75%–4.00%** and signaled the **end of QT (balance-sheet runoff) from December**, while Chair Powell pushed back on a December cut being a “foregone conclusion.” Equities were mixed on the day; yields and the USD wobbled as traders recalibrated cut odds.
* **Trump & Tariffs:** The White House finalized new **Section 232 tariffs**—**25% on medium/heavy-duty trucks and truck parts** (and **10% on buses**)—with **effective date Nov 1**; the move is seen as potentially inflationary at the margin and a watch-item for goods prices and supply chains.
* **Government shutdown & data blackout:** The **federal shutdown persisted**, limiting official data. **BLS updates were suspended** (with a one-off CPI exception earlier), leaving markets to lean on private proxies; NFP/JOLTS publication remains at risk until funding resumes.
* **Risk assets:** U.S. equities **ended the week and October higher** (Amazon/AI-related earnings helped); the S&P 500 extended a multi-month winning streak.
* **Gold:** XAUUSD **spiked on the Fed cut**, then **faded back toward ~$4,000/oz** as traders trimmed expectations for another near-term cut; still notched a positive October.
* **Crypto:** **U.S. spot BTC ETF flows were choppy into week-end** (after strong October net inflows); **ETH ETFs saw softer momentum** late in the month.

### THIS WEEK

* **Key U.S. releases (ET/CET):**

  * **Mon, Nov 3, 10:00 / 16:00** – **ISM Manufacturing (Oct).**
  * **Wed, Nov 5, 8:15 / 14:15** – **ADP private payrolls (Oct).**
  * **Wed, Nov 5, 10:00 / 16:00** – **ISM Services (Oct).**
  * **Thu, Nov 6, 8:30 / 14:30** – **Initial jobless claims** (release **may be paused** under shutdown).
  * **Fri, Nov 7, 8:30 / 14:30** – **Employment Situation (Oct)** (**at risk of postponement** under shutdown).
* **Treasury supply:** **Quarterly Refunding**—**financing estimates Mon (Nov 3)** and the **refunding announcement/press on Wed (Nov 5)**—is a rates/liquidity catalyst for duration, growth/AI equities and gold.
* **Earnings / tech impulse:**

  * **Mon (AMC)** – **Palantir (PLTR)**.
  * **Tue (AMC)** – **AMD (Q3 FY25)**.
  * **Wed (AMC)** – **Qualcomm (Q4 FY25)**; **Robinhood (Q3)**.
* **Politics:** **Off-year U.S. elections (Tue, Nov 4)** in **New Jersey & Virginia** (governor races) add headline risk; no market holiday.
* **Trading hours:** The U.S. moved clocks back on **Sun, Nov 2**; **U.S. cash equities trade 9:30–16:00 ET = 15:30–22:00 CET**.
* **Crypto micro:** Watch **spot BTC/ETH ETF flow prints** and any **Mt. Gox** headlines (repayment **deadline extended to 2026** reduces near-term supply overhang).

### MACRO ANALYSIS

#### BTC & ETH

Crypto beta tracks **USD/liquidity** this week: a **benign refunding + soft ISM/ADP** supports risk and **ETF inflows**; a hawkish rates impulse does the opposite. The **shutdown data gap** shifts focus to **private prints** and **ETF flow tickers** intraday. Structurally, **Mt. Gox push-out to 2026** tempers supply-shock risk; tactically, late-October **BTC ETF flows turned choppy**, so **spot flow direction** will likely govern BTC/ETH tone around U.S. session opens (now **15:30 CET**).

# TRADING PLAN FOR 1H_TTF (Trigger • Location • Context)

### **ORANGE_A1 — Short reversal at `4H.zones.SELL_1` (TTF-MSB)**

* **Context:** 1H/4H trend-down; price beneath **S-VWAP/W-VWAP** and all EMAs with RSI recovering from oversold. Expect a reactive bounce into overhead supply as liquidity backfills toward **`4H.zones.SELL_1 (109.1–109.6k)`** overlapping **`1D.poc.POC_4`**. Look for buy-side to stall (lower CVD highs, weak VCs).
* **Location:** **`4H.zones.SELL_1`** ± the local LVN edge; confluence with **descending `1H_21/50EMA`** and **`1D.poc.POC_4`**.
* **Trigger:** **TTF_L_MSB (15m)** at the zone (e.g., sweep of local 15m high → close back in) **+ bearish VC or CVD roll-over**; optional 5m follow-through BOS.
* **Invalidation:** 1H acceptance **above** the top of **`4H.zones.SELL_1`** with **bullish HVC** and rising CVD (defer to **GREEN_A**).
* **Setup Priority:** **A**

---

### **ORANGE_A2 — Short reversal at `4H.zones.SELL_1` (LTF-MSB)**

* **Context:** Same macro as A1, but enter with finer timing.
* **Location:** **`4H.zones.SELL_1`** / **`1D.poc.POC_4`** / descending **`1H_21/50EMA`** cluster.
* **Trigger:** **LTF_L_MSB (5m/3m)** after a small stop-run; **weak pullback volume** vs prior up-leg; CVD fails to make HH.
* **Invalidation:** Impulsive reclaim above zone on **bullish HVC**.
* **Setup Priority:** **A-**

---

### **ORANGE_B — Short shallow pullback to `1H.zones.SELL_1` + S-VWAP**

* **Context:** If bounces top earlier, a shallow mean-reversion into **`1H.zones.SELL_1`** (aligns with **`1D.poc.POC_4`**) and **S-VWAP** offers continuation entries with trend.
* **Location:** **`1H.zones.SELL_1`** / **S-VWAP** band.
* **Trigger:** **LTF_L_MSB** on rejection wicks; **bearish VC** at the pivot; CVD lower highs.
* **Invalidation:** 1H close back **above S-VWAP** and **`1H.zones.NEUTRAL`** with HL sequence.
* **Setup Priority:** **A-**

---

### **PURPLE_A — Short fade on `H_SWEEP` at `1H.major.H_MAJOR`**

* **Context:** Range scalp with bearish bias: if price squeezes to **`1H.major.H_MAJOR`**, watch for a liquidity run and failure back inside while 4H stays down.
* **Location:** **`1H.major.H_MAJOR`** with overhead resistance stack (**`1H.zones.SELL_1` → `4H.zones.SELL_1`**).
* **Trigger:** **H sweep** of **`1H.major.H_MAJOR`** → **LTF/15m_L_MSB** + CVD roll-over; confirm with **bearish VC**.
* **Invalidation:** Acceptance above **`1H.major.H_MAJOR`** with sustained CVD bid.
* **Setup Priority:** **B+**

---

### **PINK_A — Short momentum after retest (S_VWAP + `1H_9EMA`)**

* **Context:** Use with the prevailing intraday **bearish** flow. After a sell impulse, look for a **shallow retest** into **S_VWAP + `1H_9EMA`** while price remains **below `1H.major.H_MAJOR`**; prefer weakening up-leg VPA and **CVD LHs**.
* **Location:** Rejection at **S_VWAP + `1H_9EMA`** under **`1H.zones.NEUTRAL`** with downside magnets to **`1H.major.L_MAJOR`**
* **Trigger:** **LTF_L_BOS or LTF_L_MSB** from the retest band with a bearish VC; enter on the first low-volume pullback.
* **Invalidation:** Reclaim and hold **above S_VWAP + `1H_21EMA`** or a **`1H_H_MSB`** that accepts back over **`1H.major.H_MAJOR`** (defer to TEAL_A/GREEN_A).
* **Setup Priority:** **A+**

---

### **RED_A — Short breakdown below `1H.major.L_MAJOR`**

* **Context:** If sellers press through the range low, trend could accelerate into the 1D wedge base (**`1D.zones.BUY_1`**) / **`4H.major.L_MAJOR`**.
* **Location:** **Loss of `1H.major.L_MAJOR`** and failed retest from below.
* **Trigger:** **TTF_L_BOS (15m)** through **`1H.major.L_MAJOR`** on **sell-side HVC + negative CVD**; sell the **low-volume retest**.
* **Invalidation:** Swift reclaim of **`1H.major.L_MAJOR`** and S-VWAP with HL sequence.
* **Setup Priority:** **B**

---

### **BLUE_A — Long fade on `L_SWEEP` at `1H.major.L_MAJOR`**

* **Context:** Counter-drive scalp only if sellers exhaust at the range floor while 1H RSI is deeply oversold and CVD shows basing.
* **Location:** **`1H.major.L_MAJOR`** with extension into **`1D.zones.BUY_1`** / **`4H.major.L_MAJOR`**.
* **Trigger:** **Liquidity sweep of `1H.major.L_MAJOR` → 15m/5m_H_MSB** back into range **+ bullish divergence (RSI/CVD)**; reclaim **S-VWAP** to confirm.
* **Invalidation:** Continued acceptance below **`1H.major.L_MAJOR`** or **bearish SHVC** at the base.
* **Setup Priority:** **B-** 

---

### **YELLOW_A — Long reversal at `1D.zones.BUY_1` → reclaim above `1H.major.H_MAJOR`**

* **Context:** If the wedge base holds (daily), look for TTF trend death and realignment up. Needs **decisive TTF_H_MSB** and CVD turn.
* **Location:** **`1D.zones.BUY_1`** with path to reclaim **`1H.major.H_MAJOR`** / **`1H.zones.NEUTRAL`**.
* **Trigger:** **TTF_H_MSB** at the base, then buy the **low-volume pullback** to the new S/R flip; confirm with **reclaim of S-VWAP**.
* **Invalidation:** Fresh **TTF_L_BOS** from the base or **sell-side HVC** into the zone.
* **Setup Priority:** **A-**

---

### **YELLOW_B — Long reversal at `1W.zones.BUY_1` (deeper flush)**

* **Context:** If a stop-run extends toward the weekly demand, we only act on **confirmed** TTF realignment with HTF.
* **Location:** **`1W.zones.BUY_1`** → initial target **`1D.major.L_MAJOR`** / daily POCs above.
* **Trigger:** **TTF_H_MSB** after a capitulation-style VC at the weekly LVN edge; rising CVD and absorption signs.
* **Invalidation:** Acceptance **below** the weekly band (remove plan).
* **Setup Priority:** **A-**

---

### **GREEN_A — Long breakout & retest above `1H.major.H_MAJOR`**

* **Context:** If buyers flip the 1H range (trend-death of the intraday downtrend), continuation can target **`1D.zones.NEUTRAL`** / **`1D.poc.POC_3`**.
* **Location:** Clean break and first retest of **`1H.major.H_MAJOR`** from above.
* **Trigger:** **1H_H_BOS + bullish HVC** → **LTF_H_MSB** on the retest; CVD making HHs.
* **Invalidation:** Acceptance back **below `1H.major.H_MAJOR`** or immediate **1H_L_CHOCH** post-entry.
* **Setup Priority:** **B**

---

### **TEAL_A — Long counter-trend on 1H momentum reclaim**

* **Context:** Intraday downtrend but a **trend-death flip** is possible if buyers reclaim **S_VWAP + `1H_9EMA`** and print a **`1H_H_MSB`** **above `1H.major.H_MAJOR`**. Look for bullish VC on breakout and **CVD HHs** while RSI exits oversold.
* **Location:** Reclaim and hold **S_VWAP + `1H_9EMA`** → **above `1H.major.H_MAJOR`** with upside magnets into **`4H.zones.SELL_1`** 
* **Trigger:** **LTF_H_MSB or LTF_H_BOS** after the 1H flip; low-volume pullback to the S/R flip, then continuation with rising CVD.
* **Invalidation:** 1H close back **below S_VWAP** or loss of the flip (bearish VC) **and** failure to hold above **`1H.major.H_MAJOR`**.
* **Setup Priority:** **B**

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
- 1W: `OVERALL-ASSESSMENT = NEUTRAL`.
- `PG` grades are assessed based on the plan full viability. DO NOT DEGRADE the plan based on probability/possibility.  
- DO NOT PERFORM TTI on the 1W_TF. 