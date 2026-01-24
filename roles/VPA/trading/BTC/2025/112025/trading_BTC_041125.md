# CONTEXT: 
## TRADER CONTEXT: 
Today is Wednesday 5th of November 2025, we are in London session, 3 hours until US session. We have no major macro events or data released today. Due to government shutdown, we have not received many major macro economic data such as NFP/Unemployment/PPI for the last 3 week and this is expected to continue this week.  Refers to `MACRO CONTEXT` for the rest of the macro events this week. 

Last month: We have officially passed October which was supposed to be bullish month for BTC and crypto in terms of seasonality during a bull cycle year, however we got the opposite of that: largest historic liquidation sell off after sweeping the ATH followed by choppy price actions at the bottom of the 1W range despite soft CPI + Inflation data print. 

Last week: Market seems to be responded positive to FED decisions coupled with positive resolution on China-US tariffs news which allow US equities putting new ATH, BTC recovering and cool-off on gold hyperbolic bullruns, signaling a potential risk-off environment. We also had FOMC last Wednesday in which the key details are outlined below:
```markdown
* **Cut 25 bps** to a **3.75%–4.00%** fed-funds target range; **two dissents** (Miran wanted –50 bps; Schmid preferred no change).
* **Ended QT effective Dec 1**: the Committee will **stop shrinking the balance sheet** and **reinvest all principal** thereafter (Treasuries rolled over; **all agency/MBS principal reinvested into T-bills**).
* **Operating settings** (implementation note): **IORB 3.90%**, **ON RRP 3.75%**, **SRF min 4.00%**, $500B aggregate SRF limit, RRP **$160B per-counterparty**.
* **Powell’s tone**: another cut in **December is “not a foregone conclusion,”** stressing data uncertainty amid the shutdown. 
* **Context & reaction**: Statement added emphasis on **rising downside risks to employment**; markets whipsawed as traders digested the **easing + QT end** vs **no December pre-commitment**.

> Why this matters: Ending QT + a 25-bp cut = **easier financial conditions via reserves/liquidity** and **lower policy rate**, but Powell explicitly **kept optionality**, so the **path** (not the single cut) drives cross-asset pricing.
```

This week/Trader Directive: Despite bearish trend, given BTC 1W `OVERALL_ASSESSMENT = NEUTRAL-BEARISH`, we should remains cautious with breakout at either side of the 1W major structure and leaves room to trade mean-reversion at extreme as much as possible. 

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
      SR_5: 100.9k
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
      POC_4: 108.2k
      POC_5: 106.9k
    zones:
      SELL_1: 113.2k
      BUY_1: 107.3k
      NEUTRAL: 110.0k
    session:
      PDH: 110.8k
      PDL: 105.3k
    active: 
      H_SWEEP: 116.0k
    inactive:
      H_CHOCH: 114.0k
      L_BOS: 109.6k


  4H:
    major:                 
      H_MAJOR: 108.3k    
      L_MAJOR: 106.7k    
    sr:
      SR_1: 116.4k
    poc: 
      POC_1: 110.8k
      POC_2: 107.7k
      POC_3: 104.5k
    zones:
      SELL_1: 107.7-108.6k
    active:
      L_BOS: 106.7k
    inactive: 
      H_CHOCH: 111.2k
      L_BOS: 108.7k

  1H:
    major:
      H_MAJOR: 107.3k
      L_MAJOR: 106.9k
    sr: {}
    poc: {}
    zones:
      SELL_1: 105.5-106.1k
    active:
      L_BOS: 105.3k
    inactive: 
      H_SWEEP: 107.3k
      L_MSB: 106.7k

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

### **Weekly (1W — Super-HTF structure)**

* **Previous (~30 candles):** Strong uptrend from late ’24 into the **ATH** `ALL.ath` with range building below `1W.major.H_MAJOR`. A corrective leg confirmed `1W.inactive.L_MSB`, tagging the reclaimed `1M.inactive.H_BOS` + the weekly EMA band to set a range low near `1W.major.L_MAJOR`. Multiple range sweeps followed: the recent `1W.inactive.H_SWEEP` at the upper band and, last month, the **`1W.active.L_SWEEP`** printed as a **`1W_bearish_hammer_HVC`** (capitulation/liquidation spike) that extended the range-low extreme into `1W.major.L_MAJOR` / overlap with `1W.zones.BUY_1` (**~106.1k**).
* **Current (~5 candles):** The bounce from `1W.zones.BUY_1` stalled at `1W.zones.NEUTRAL` (**~114.1k**) / `1W.poc.POC_1` (**~115.3k**); failure to reclaim `1W_20EMA/MA` turned price back toward the lower third of the range. Structure remains a broad weekly range **`1W.major.L_MAJOR` ↔ `1W.major.H_MAJOR`** with a bearish lean while below `1W.sr.SR_1/0` (**114.2k/119.4k**). Weekly dynamic support to watch on approach: `1W_50EMA/MA` cluster (historic bull-market band ~**101–103k**).

---

### **Daily (1D — HTF for intraday)**

* **Previous (~30 candles):** Rebound from the weekly range low progressed into `1D.major.H_MAJOR` (**~116.4k**) / `1W.zones.NEUTRAL` (**~114.1k**) where sellers re-asserted. The subsequent leg rolled over through `1D.zones.NEUTRAL` (**~110.0k**) with a sequence of **`1D_bearish_marubozu_HVC`** bars. Session refs tightened around `1D.session.PDH` (**~110.8k**) and `1D.session.PDL` (**~105.3k**).
* **Current (~5 candles):** Price is driving into the lower band of the weekly range, sitting above **but probing** `1D.major.L_MAJOR` (**~103.5k**) and well below `1D.poc.POC_4/5` (**~108.2k/106.9k**). Indicators (CSV): **1D_RSI ≈ 35 < RSI-MA ≈ 45**, price < `1D_9/21/50/200EMA`, and < `W_VWAP` / `M_VWAP`—confirming bearish HTF conditions. Daily bias: **bearish into support**; watch response at `1D.major.L_MAJOR` toward `1W.major.L_MAJOR` (**~102.0k**).

---

### **4-Hour (4H — HTF for the 1H TTF)**

* **Previous (~30 candles):** A failed attempt to turn up at **`4H.inactive.H_CHOCH`** led to persistent selling. Each rally into `4H.poc.POC_1` (**~110.8k**) / `4H.sr.SR_1` (**~116.4k**) faded, culminating in the latest **`4H.active.L_BOS`** (continuation to the downside) that broke the **`4H.major.L_MAJOR`** (**~106.7k**) and drove toward `4H.poc.POC_3` (**~104.5k**).
* **Current (~5 candles):** Price sits in the lower tail of the composite, capped by the descending `4H_9EMA` and `W_VWAP`. CSV confirms **RSI ≈ 29 (oversold)** with price **below all 4H MAs**, `W_VWAP` and `M_VWAP`. Overhead supply to watch: `4H.zones.SELL_1` (**~107.7–108.6k**) layering with `1D.poc.POC_3` (**~110.0k**) and `1W.poc.POC_3` (**~109.6k**). Bias: **bearish while below `4H_21EMA` and `4H.zones.SELL_1`**.

---

### **1-Hour (1H — TTF)**

* **Previous (~30 candles):** A clean **`1H_descending_channel`** developed after repeated failures beneath `1H.major.H_MAJOR` (**~107.3k**). Asia’s move extended lower with a **`1H.active.L_BOS`** through `1D.session.PDL` (**~105.3k**) and a cluster of **`1H_bearish_marubozu_HVC`** bars.
* **Current (~5 candles):** Retests from below into `S_VWAP` (**~105.3k**, CSV) and the falling `1H_9/21EMA` continue to fail. CSV: **price < `1H_9/21/50/200EMA`**, **< `S_VWAP` & `W_VWAP`**, **RSI ≈ 31 (< RSI-MA ≈ 38)**. CVD for today is **negative (~-500)** but **flattening**—diverging from price (early caution for shorts; still needs PA confirmation). Local magnets: `1D.poc.POC_5` (**~106.9k**), `1H.zones.SELL_1` (**~105.5–106.1k**), and the open gap toward `1W.sr.SR_5` (**~100.9k**) if breakdown accelerates. TTF bias: **bearish**, scouting responsive buys only at **major** supports with confirmation.

## MACRO CONTEXT
### LAST WEEK

* **Fed (Wed, Oct 29):** The FOMC **cut the fed funds target by 25 bps to 3.75–4.00%** and said it would **end balance-sheet runoff on Dec 1** (QT wind-down), with Powell signaling a cautious, data-dependent path. Rates rose at the long end on “hawkish cut” read-through.
* **Growth & inflation prints (Thu–Fri, Oct 30–31):** **Q3 GDP “advance” timing was disrupted by the federal shutdown**, leaving Nowcast proxies in focus. **September PCE** was published with site updates constrained by the shutdown; Core PCE YoY most recently showed **~2.9% in Aug** ahead of the Sept release.
* **Tariffs & Trump:** Markets priced **policy headline risk** as **SCOTUS slated tariff oral arguments for this week**; administration officials continued to frame the **10% “universal/reciprocal” baseline tariffs** and China-specific measures as central to policy, while lower-court rulings against IEEPA-based tariffs remained **stayed** pending the Supreme Court review.
* **Manufacturing pulse (Mon, Nov 3 print for Oct):** **ISM Manufacturing fell further into contraction (48.7)** with tariff-linked input frictions cited; services PMI due mid-week.
* **Crypto flows:** **U.S. spot-BTC ETFs flipped to small **net outflows** late week (Oct 29–31) and **again Nov 3**, while **ETH spot-ETFs were mixed/slightly positive**—a near-term headwind to BTC beta.
* **Gold:** After whipsaws into the decision, **gold reclaimed ~$4k intraday on Oct 30** on the rate cut before easing as the dollar firmed; safe-haven bid tempered by **trade-talk optimism** headlines.

### THIS WEEK

* **Key U.S. data & times (ET → CET):**

  * **Wed, Nov 5, 10:00 (16:00 CET)** – **ISM Services (Oct)**.
  * **Fri, Nov 7, 8:30 (14:30 CET)** – **Employment Situation (Oct)**; publication **subject to shutdown-related contingencies**.
  * **All week:** With the **Fed blackout over**, **speeches** resume; market sensitivity to guidance is elevated post “hawkish cut.”
  * **Treasury supply:** **Quarterly Refunding** docs released **Mon, Nov 3 (15:00 ET)**; **auction mix guidance Wed, Nov 5 (08:30 ET)** with focus on **steady coupons, heavier T-bills, and buybacks** interplay versus the Fed’s QT wind-down.
* **Politics & tariffs:** **Supreme Court oral arguments on Trump tariff authority** **Wed, Nov 5 (10:00 ET)**—a key legal overhang for risk, USD, and inflation-sensitive assets.
* **Elections/Calendar:** **U.S. off-year Election Day is Tue, Nov 4** (state & local races; sentiment read-throughs possible). **Veterans Day Tue, Nov 11:** **U.S. stock market open; bond market closed**; expect liquidity distortions around rates that day.
* **Tech/Earnings impulse:** **Apple and Amazon reported last week**, feeding mega-cap positioning; focus shifts to macro and to later-November **AI/semis** prints.
* **Logistics:** **U.S. ended DST on Sun, Nov 2** → **New York is EST (UTC−5)**; **8:30 ET releases = 14:30 CET (Copenhagen)**.

### MACRO ANALYSIS

#### BTC & ETH

**Crypto beta** is leaning cautious near-term as **BTC spot-ETF flows** turned **negative** late last week/Mon while **ETH flows** were steadier. Liquidity conditions hinge on **rates and refunding**: the Fed’s cut and QT wind-down **support liquidity**, but a **hawkish reaction in yields** and **coupon/bill mix** can still weigh on risk. **Tariff-driven inflation risk** would be **USD-supportive** (near-term headwind to BTC), while any **legal curb on tariff authority** is **risk-positive** and could aid **ETH relative strength** given recent flow skew.


# TRADING PLAN FOR 1H_TTF (Trigger • Location • Context)

### **ORANGE_A — Short continuation at `1H.zones.SELL_1` pullback**

* **Context:** Dominant downtrend on 1H/4H (price below all ST/MT/LT MAs & VWAPs; 1H RSI ~31). After the `1H.active.L_BOS` below `1D.session.PDL`, expect mean-reversion tests into the band of `S_VWAP` + falling `1H_21EMA`.
* **Location:** `1H.zones.SELL_1` **~105.5–106.1k** overlapping `S_VWAP` (**~105.3k**) and just above the broken **`1H.active.L_BOS`** (**~105.3k**).
* **Trigger:** **LTF_L_MSB** (realign short) after a low-volume pullback; bearish HVC/ignition from the zone + **falling/confirming CVD**.
* **Invalidation:** 1H acceptance back above `1D.poc.POC_5` (**~106.9k**) or a decisive reclaim of `S_VWAP` **and** `1H_21EMA` with **LTF_H_BOS**.
* **Setup Priority:** **A+**

---

### **ORANGE_B — Short reversal at `4H.zones.SELL_1`**

* **Context:** Any counter-trend squeeze toward **`4H.zones.SELL_1` ~107.7–108.6k** targets the descending `4H_21EMA` and clustered POCs above (`1D.poc.POC_3` **~110.0k**, `1W.poc.POC_3` **~109.6k**). Expect exhaustion/absorption into this LVN edge.
* **Location:** `4H.zones.SELL_1` (**~107.7–108.6k**) ± `4H_21EMA`.
* **Trigger:** Liquidity grab or failed break (wick/close back in) → **LTF_L_MSB** with **bearish CVD turn** and a sell-side HVC.
* **Invalidation:** 1H close **above** `4H.zones.SELL_1` and holding over `1W.poc.POC_3` (**~109.6k**).
* **Setup Priority:** **A-**

---

### **PURPLE_A — Short fade on `1H.major.H_MAJOR` sweep**

* **Context:** Range-top fade in a bearish regime. Watch for a stop run of `1H.major.H_MAJOR` (**~107.3k**) into the **W_VWAP** band and the falling `1H_50EMA`.
* **Location:** `1H.major.H_MAJOR` (**~107.3k**) with confluence of `W_VWAP` (~106.6k) / `1H_50EMA`.
* **Trigger:** **H_SWEEP** of `1H.major.H_MAJOR` → rejection → **LTF_L_MSB**; CVD rolls over (price up, CVD down = regular bear div).
* **Invalidation:** 1H acceptance above `1D.sr.SR_1` (**~114.3k**) is unnecessary here; practical invalidation is **firm 1H close above** `1H.major.H_MAJOR` that then flips to support.
* **Setup Priority:** **B+**

---

### **PINK_A — Short scalp momentum on shallow pullback to `S_VWAP` + `1H_9EMA`**

* **Context:** After a fast impulse down, shallow bounces to `S_VWAP` (**~105.3k**) / `1H_9EMA` tend to fail while RSI is sub-40 and CVD is negative.
* **Location:** `S_VWAP` + `1H_9EMA` band inside/near `1H.zones.SELL_1` (**~105.5–106.1k**).
* **Trigger:** **LTF_L_BOS** or **LTF_L_MSB** from the band with bearish VC (ignition/continuation).
* **Invalidation:** Reclaim and hold above `S_VWAP` **and** `1H_21EMA` with rising CVD.
* **Setup Priority:** **B**

---

### **RED_A — Short breakdown through `1D.major.L_MAJOR` → `1W.major.L_MAJOR`**

* **Context:** If sellers press through a new established 1H range low confluenced with `1D.major.L_MAJOR` (**~103.5k**) and the weekly floor `1W.major.L_MAJOR` (**~102.0k**), that’s a regime-shift extension.
* **Location:** Below `1D.major.L_MAJOR` toward `1W.sr.SR_5` (**~100.9k**).
* **Trigger:** **1H_L_BOS** **through** `1D.major.L_MAJOR` with a bearish HVC and falling CVD → **sell the low-volume retest** of the broken level.
* **Invalidation:** Swift reclaim of `1D.major.L_MAJOR` (1H close back above) **plus** LTF_H_MSB.
* **Setup Priority:** **B**

---

### **BLUE_A — Long fade/knife-catch on `L_SWEEP` at `1D.major.L_MAJOR`**

* **Context:** Price is extended from VWAPs/MAs with 4H RSI ~29 and 1H RSI ~31. A **capitulation-type sweep** into `1D.major.L_MAJOR` (**~103.5k**) / channel bottom can print stopping/absorption SHVC.
* **Location:** `1D.major.L_MAJOR` (**~103.5k**), extension toward `1W.major.L_MAJOR` (**~102.0k**) if overshoot.
* **Trigger:** **L_SWEEP** + **LTF_H_MSB** with **bullish divergence (CVD/RSI)** and a **stopping/absorption SHVC**. Confirm with reclaim of `S_VWAP`.
* **Invalidation:** A fresh **1H_L_BOS** that accepts **below** `1W.sr.SR_5` (**~100.9k**).
* **Setup Priority:** **B-** 

---

### **TEAL_A — Long counter-trend on reclaim of `S_VWAP` + `1H_9EMA`**

* **Context:** Counter-trend scalp only if the 1H down-leg stalls, anticipating a failed breakdown and **reclaims** the mean above the prior broken `1H_L_BOS` level + short term momentum indicator. Demand must **prove** itself (we don’t fade blindly).
* **Location:** `S_VWAP` (**~105.3k**) + `1H_9EMA` reclaim, ideally above `1H.active.L_BOS` + `1H.zones.SELL_1` rejection pocket.
* **Trigger:** **LTF_H_BOS/MSB** after the reclaim, with CVD flipping positive and pullback volume **lower** than the up-impulse.
* **Invalidation:** Lose `S_VWAP` again and roll back under `1D.session.PDL` (**~105.3k**).
* **Setup Priority:** **B**

---

### **YELLOW_A — Long reversal at range-low (`1D.major.L_MAJOR` ↔ `1W.major.L_MAJOR`)**

* **Context:** Higher-probability reversal if the zone bases and the **TTF trend dies** (clear shift).
* **Location:** `1D.major.L_MAJOR` (**~103.5k**) down to `1W.major.L_MAJOR` (**~102.0k**).
* **Trigger:** **TTF_H_MSB (1H)** after a sweep/failed breakdown, plus rising CVD; enter on the first **low-volume pullback** to the MSB flip.
* **Invalidation:** 1H acceptance below `1W.sr.SR_5` (**~100.9k**).
* **Setup Priority:** **A-**

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