# CONTEXT: 
## TRADER CONTEXT: 
Today is Thursday 30th of October 2025, we are in London session, 4 hours until US session. Due to government shutdown, we have not received many major macro economic data such as NFP/Unemployment/PPI for the last 3 week and this is expected to continue this week. We have FOMC in 9 hours as the major macro events today. Refers to `MACRO CONTEXT` for the rest of the macro events this week. 

We have officially passed September which has been notorious for a BTC and crypto pullbacks during the bull runs year and currently enter Q4 of which has been typical bullish for bitcoin bull cycle. We should favors more bullish setups while remains as cautious as possible until BTC firmly surpasses ATH. 

Last week: Price recovered after crypto market got the biggest liquiditation sell off in the entire history, while gold has pullback significantly from its bullmarket, signaling risk-on environment supported by dovish FED and CPI + Inflation data print last weeks. For our trader specifically, 1W `OVERALL_ASSESSMENT` remains `NEUTRAL` as we are trading within this HTF range. 

This week: Price managed to close above the 1W range low as a confirmed `1W_L_SWEEP` and reclaimed the `1W_20EMA/MA` bull market support bands. Market seems to be respond positive to expectation of a FED 0.25 bps interest rate cut decision with 96.7% as US equities putting new ATH and BTC recovering strongly. This is also coupled with positive resolution on China-US tariffs news during the weekend that has haunted the market last 3 weeks. 

Sentiment: Public sentiment for October remain bullish for BTC within this year of its bullish 4 years cycle from a seasonality and historic standpoint. However price action last 2-3 weeks have liquidated millions of leveraged crypto traders and enact some fears with people hypothesizing for the top of the cycle is in for BTC, and the start of an extended bear market into 2026. `Fear & Greed Index` is currently at neutral between 42-51 after dropping below to 22-30 in fear/extreme fear terriroty last week. 

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
    major: {}
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
      SR_5: 112.2k
    poc:
      POC_1: 115.3k
      POC_2: 111.2k
      POC_3: 108.8k
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
      H_MAJOR: 116.0k  
      L_MAJOR: 103.5k  
    sr: 
      SR_1: 110.2k
      SR_2: 114.3k
    poc:
      POC_1: 115.8k
      POC_2: 112.9k
      POC_3: 109.4k
      POC_4: 106.9k
    zones:
      SELL_1: 113.3k
      BUY_1: 106.1k
      NEUTRAL: 110.0k
    session:
      PDH: 116.1k
      PDL: 112.2k
    active: 
      H_CHOCH: 114.0k
    inactive:
      L_BOS: 109.6k


  4H:
    local:
      H: 116.1k
    major:                 
      H_MAJOR: 116.4k    
      L_MAJOR: 112.1k     
    sr:
      SR_1: 116.4k
    poc: 
      POC_1: 110.8k
      POC_2: 112.5k
      POC_3: 113.6k
      POC_4: 115.0k
    zones:
      SELL_1: 114.8k
      BUY_1: 111.8-113.1k
      NEUTRAL: 114.3k
    active:
      L_BOS: 113.5k
      L_MSB: 112.9k
    inactive: 
      L_CHOCH: 114.5k
      H_BOS: 114.0k

  1H:
    major:
      H_MAJOR: 113.6k
      L_MAJOR: 112.1k
    sr: {}
    poc: {}
    zones:
      SELL_1: 114.1k
      NEUTRAL: 112.9k
    active:
      H_CHOCH: 113.0k
    inactive: 
      L_MSB: 114.1k
      H_MSB: 114.6k

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


### **1W – Super-HTF Structure**

* **Previous (~30 candles):** Strong uptrend into `1W.major.H_MAJOR` / `ALL.ath` followed by a corrective leg that confirmed `1W.inactive.L_MSB`, tagging the `1M.inactive.H_BOS` region and weekly bull-market supports (`1W_ST-EMAs`). A three-month range developed between `1W.major.H_MAJOR` and `1W.major.L_MAJOR`, with alternating sweeps — most recently `1W.inactive.H_SWEEP` then `1W.active.L_SWEEP` establishing extremes at `1W.major.L_MAJOR`.
* **Current (~5 candles):** Bounce from `1W.major.L_MAJOR` toward `1W.zones.NEUTRAL` **(114.1k)**, reclaiming the rising `1W_21EMA` while still **below** the `1W_9EMA`. RSI is neutral-bullish (`1W_RSI` slightly > 50); volume is **sub-VC** (well under `1W_vol_ma20`). Price sits **below** `W_VWAP` and **above** `M_VWAP`, keeping the mid-range `1W.poc.POC_2` **(111.2k)** and `1W.poc.POC_1` **(115.3k)** as magnets. HTF read: **range-bound, mild bullish drift into `1W.zones.NEUTRAL` with supply overhead.**

---

### **1D – HTF for Intraday**

* **Previous (~30 candles):** From the 1W range top, price rolled over on a liquidation leg (`1D_bearish_engulfing_HVC`) and confirmed `1D.inactive.L_BOS`, sweeping the weekly range low to the vicinity of `1W.major.L_MAJOR` before absorption. Held the ascending `1D_200EMA/MA` and launched an internal bullish leg that confirmed `1D.active.H_CHOCH`, retesting `1D.major.H_MAJOR` **(116.0k)** near the 1W mid-range.
* **Current (~5 candles):** Rejection printed (`1D_bearish_inverted-hammer_VC`) and follow-through lower left price **below** the broken `1D.active.H_CHOCH` **(114.0k)** and just under `1D.poc.POC_2` **(112.9k)**, while still **above** `1D_9/21EMA` but **beneath** `1D_50EMA`. `W_VWAP`/`M_VWAP` sit overhead; `1D.session.PDH` **(116.1k)** and `1D.poc.POC_1` **(115.8k)** are primary resistive magnets; `1D.poc.POC_3` **(109.4k)** / `1D.poc.POC_4` **(106.9k)** guard the downside toward `1W.poc.POC_2`. Bias: **neutral with a downward lean while under `1D.major.H_MAJOR`.**

---

### **4H – HTF for 1H**

* **Previous (~30 candles):** Trend up culminated in `4H.inactive.H_BOS`, probing into the 1W mid-range/1D range high confluence. Rejection set the `4H.major.H_MAJOR` **(116.4k)**, then `4H.inactive.L_CHOCH` → **`4H.active.L_BOS` (113.5k)** + **`4H.active.L_MSB` (112.9k)** pushed price below the 4H ST-EMAs and toward `4H.zones.BUY_1` **(111.8–113.1k)** where `4H.major.L_MAJOR` **(112.1k)** formed.
* **Current (~5 candles):** Bounce off `4H.zones.BUY_1` reclaimed S_VWAP on 4H, but price is **beneath** the descending `4H_9/21EMA` and retesting the underside of **`4H.active.L_BOS` (113.5k)** with `4H.poc.POC_3` **(113.6k)**/`4H.poc.POC_4` **(115.0k)** above and `4H.poc.POC_2` **(112.5k)** below. `W_VWAP`/`M_VWAP` remain overhead. RSI near 50 with a rollover of its MA signals momentum fatigue unless bulls reclaim `4H.major.H_MAJOR`. Overall: **neutral-bearish below the L_BOS cluster.**

---

### **1H – TTF (Execution)**

* **Previous (~30 candles):** Post-rebound, price failed to sustain the pop and resumed a **`1H_descending_channel`**. A failed break saw `1H.inactive.L_MSB`, continued lower on **1H_bearish_HVCs**, into `4H.zones.BUY_1` where basing reclaimed S_VWAP and `1H_9EMA`.
* **Current (~5 candles):** Bounce printed **`1H.active.H_CHOCH (113.0k)`**, now retesting the underside of **`4H.active.L_BOS (113.5k)`** with the top of the channel and the descending `1H_21EMA` overhead. Structure: price **below** `1H_9/21/50EMA` but **above** `1H_200EMA`; S_VWAP is just reclaimed while `W_VWAP`/`M_VWAP` cap above. `1H.major.H_MAJOR` **(113.6k)** and `1H.zones.SELL_1` **(114.1k)** are immediate resistances; `1H.zones.NEUTRAL` **(112.9k)** is mid; `1H.major.L_MAJOR` **(112.1k)** aligns with `4H.major.L_MAJOR`. RSI < 50 with RSI-MA < 50 → **neutral-bearish momentum until a clean reclaim of `1H.major.H_MAJOR`.**
  
## MACRO CONTEXT

### LAST WEEK 

* **Tariffs dominated the macro narrative.** The White House’s **10% “baseline/reciprocal” tariff regime**—in force since April—remained the policy anchor, while a string of **Executive Orders** in mid-year continued to tweak the **reciprocal tariff schedules** (notably toward China). GOP trade hawks publicly pressed for a harder line, keeping **China-tariff escalation risk** on the front burner.
* **Escalation talk stayed live.** Fresh reporting re-circulated the President’s **threat of a 100% tariff on all Chinese imports “as soon as Nov 1”**, leaving corporates and markets on alert for headline risk and supply-chain repricing.

### THIS WEEK 

* **Clock change / liquidity:** **U.S. DST ends Sun, Nov 2.** From **Mon, Nov 3**, New York is **6 hours behind Copenhagen** again; **NYSE cash** opens **15:30 CET**. Expect timing/volume quirks early week.
* **Top U.S. data:**

  * **Mon, Nov 3, 10:00** – **ISM Manufacturing PMI** (first business day).
  * **Tue, Nov 4, 10:00** – **JOLTS** (Sep).
  * **Wed, Nov 5, 10:00** – **ISM Services PMI.**
  * **Thu, Nov 6, 8:30** – **Initial Jobless Claims**; **Productivity & Costs (Q3, prelim.).**
  * **Fri, Nov 7, 8:30** – **Employment Situation (Oct)** — the week’s key volatility event.
* **Treasury supply / rates:** **Quarterly Refunding** week — **Financing estimates** due early in the week and **QRA coupon-size announcement Wed, Nov 5.** Any shift in duration mix or coupon sizes can move **yields, USD, gold, and equity risk premia**.
* **Earnings / tech impulse:** Mega-cap prints at week’s end set the tone into next week (**MSFT/GOOGL mid-week; AAPL/AMZN Thu Oct 30**). Guidance on **AI capex and margins** remains a primary SPX driver.
* **Crypto micro-structure:** **CME BTC/ETH monthly roll** passes into early November; watch **basis resets**. **BITO** (futures-linked BTC ETF) has an **ex-div Mon, Nov 3** (often hedging-flow relevant).
* **Politics:** **U.S. Election Day (off-year)** is **Tue, Nov 4** — localized/state races; can modestly affect **midday liquidity** and **headline sensitivity**.
* **Ongoing policy watch:** Markets will parse any **tariff headlines** or **China-policy signals** for inflation and growth implications.

### MACRO ANALYSIS

A **tariff-inflation-term-premium** triangle plus **QRA supply** and **NFP** are the week’s cross-asset pivots. If **QRA** signals larger or longer-dated issuance and **ISM/NFP** run firm, **yields/real yields** can push up: that **pressures SPX**, **weighs on BTC/ETH** (liquidity-sensitive beta), and **challenges gold** (via real-rate headwinds). Conversely, a **soft ISM/NFP** with benign QRA mix supports **duration**, **lifts gold**, and **aids SPX/crypto** via easier financial conditions. **Tariff escalation** headlines skew **inflation + margin risk**, a tailwind for **gold** and a headwind for **global-exposed SPX sectors**; crypto’s response tends to follow **broader risk appetite** and **USD/real-yield** direction more than the trade channel itself.

#### GOLD

* **Bullish on stress / bearish on real-rate backup.** Watch **QRA → term premium** and **ISM/NFP → real yields**. Tariff-risk favors **hedge demand**, but stronger data + bigger supply = **headwind**. Intraday sensitivity around **Wed (QRA/ISM-Services)** and **Fri (NFP)**.

#### BTC & ETH

* **Liquidity beta.** Direction leans with **SPX / real-yield** swings. Early-week **CME roll/BITO ex-div** can create **flow noise**; broader trend follows **rates + USD** and **post-mega-cap tech tone**. Tariff headlines matter indirectly (risk appetite), not directly.

#### SP500

* **Three levers:** (1) **QRA/yields** (valuation multiple), (2) **ISM/NFP** (growth path), (3) **tariff path** (margins/supply chains). **Tech’s earnings/guidance** remains the near-term leader for index breadth; **global-exposed cyclicals** most sensitive to tariff rhetoric.

# TRADING PLAN FOR 1H_TTF (Trigger • Location • Context)

### **ORANGE_A1 — Short reversal at 1H/4H supply**

* **Context:** 1H bounce is weak (sub-VC, RSI<50) into stacked supply while HTF is rangey. Expect sellers to defend overhead where `W_VWAP` + ST-EMAs compress. Watch for exhaustion and **bearish CVD** at the highs.
* **Location:** Confluence at `1H.zones.SELL_1 (114.1k)` / `4H.zones.SELL_1 (114.8k)` with extension sweep into `1D.session.PDH (116.1k)` / `4H.major.H_MAJOR (116.4k)`.
* **Trigger:** Liquidity grab (wick/`H_SWEEP`) then **LTF_L_MSB** → 1H rejection candle (`1H_bearish_reversal_VC`).
* **Invalidation:** 1H acceptance **above** `4H.major.H_MAJOR` with bullish ignition SHVC.
* **Setup Priority:** **A-**

---

### **ORANGE_A2 — Same location, higher-TF confirmation**

* **Context:** Same location as `ORANGE_A1`; demand wanes at supply.
* **Location:** `1H.zones.SELL_1` / `4H.zones.SELL_1` with sweep room to `1D.session.PDH` / `4H.major.H_MAJOR`.
* **Trigger:** **`1H_L_MSB`** at the location with **bearish CVD** and rising sell VCs.
* **Invalidation:** 1H hold above `1D.session.PDH`.
* **Setup Priority:** **A**

---

### **ORANGE_B — Short continuation at `4H.active.L_BOS` retest**

* **Context:** 1H trend remains down within a channel; ST-EMAs are descending. Expect a sell-the-rip if retest fails under `1H_9/21EMA`.
* **Location:** `4H.active.L_BOS (113.5k)` + top of `1H_descending_channel` + `1H_9/21EMA`.
* **Trigger:** Rejection with **LTF_L_MSB → 1H_L_CHOCH** and **bearish CVD**.
* **Invalidation:** 1H reclaim and hold **above** `1H.major.H_MAJOR (113.6k)` with buy-side HVC.
* **Setup Type:** **2A – Confirmed Counter-trend Pullback**
* **Setup Priority:** **B**

---

### **PURPLE_A — Short fade on PDH/4H_H sweep**

* **Context:** Fade a failed breakout into HTF supply; look for divergence and absorption at highs.
* **Location:** Sweep of `1D.session.PDH (116.1k)` / test of `4H.major.H_MAJOR (116.4k)` near `1D.major.H_MAJOR (116.0k)`.
* **Trigger:** **`H_SWEEP`** then **`1H_L_CHOCH`** with **bearish CVD** / absorption SHVC.
* **Invalidation:** 1H close & hold above `4H.major.H_MAJOR`.
* **Setup Priority:** **B+**

---

### **PINK_A — Momentum short scalp on VWAP loss**

* **Context:** If the bounce fails, expect momentum to re-align down intraday when S_VWAP is lost and mid-range gives way.
* **Location:** Below S_VWAP and under `1H.zones.NEUTRAL (112.9k)`.
* **Trigger:** **`1H_L_CHOCH`** or **LTF_L_BOS** under S_VWAP with **bearish CVD**; sell the retest from below.
* **Invalidation:** Quick reclaim of S_VWAP and `1H.zones.NEUTRAL`.
* **Setup Priority:** **B**

---

### **RED_A — Breakdown of 4H range low**

* **Context:** Structure shifts lower if the 4H base fails; expect acceleration on volume.
* **Location:** Below `4H.major.L_MAJOR (112.1k)` and `1H.major.L_MAJOR (112.1k)` cluster.
* **Trigger:** **`1H_L_MSB`** (TTF trend death) + strong sell-side VPA (HVC/SHVC) and **bearish CVD**; enter on **LTF_L_MSB** retest.
* **Invalidation:** Reclaim back above `1H.major.L_MAJOR` with bullish MSB.
* **Setup Priority:** **B**

---

### **BLUE_A — Long fade on L sweep at 4H base**

* **Context:** Prefer buying failed breakdowns in a weekly range. Look for seller exhaustion and absorption at demand.
* **Location:** Sweep into `4H.zones.BUY_1 (111.8–113.1k)` targeting hold above `4H.major.L_MAJOR (112.1k)`.
* **Trigger:** **`L_SWEEP` → `1H_H_CHOCH`** with **bullish CVD** and sub-VC pullback.
* **Invalidation:** 1H acceptance below `4H.major.L_MAJOR`.
* **Setup Priority:** **B-**

---

### **TEAL_A — Long scalp on breakout & S_VWAP hold**

* **Context:** If momentum flips up, expect ignition as price clears 1H highs and rides S_VWAP.
* **Location:** Break/hold above `1H.major.H_MAJOR (113.6k)` while **holding** above S_VWAP.
* **Trigger:** **LTF_H_BOS** continuation after S_VWAP hold with **bullish CVD**.
* **Invalidation:** Loss of S_VWAP after entry.
* **Setup Priority:** **B**

---

### **YELLOW_A — Long reversal at 4H demand + PDL**

* **Context:** Deeper dip into demand with rising LT MAs can spring price.
* **Location:** `4H.zones.BUY_1 (111.8–113.1k)` + `1D.session.PDL (112.2k)` confluence with `1H_200EMA/MA`.
* **Trigger:** **`1H_H_MSB`** after a sweep/absorption SHVC; confirm with **bullish CVD** and reclaim of S_VWAP.
* **Invalidation:** 1H acceptance below `1D.session.PDL`.
* **Setup Priority:** **A-**

---

### **GREEN_A — Long breakout & retest**

* **Context:** Realignment up if the 1H trend breaks its ceiling and converts resistance to support.
* **Location:** Clean break above `1H.major.H_MAJOR (113.6k)` → first retest; next magnets `4H.poc.POC_3 (113.6k)` / `4H.poc.POC_4 (115.0k)` / `1D.poc.POC_1 (115.8k)`.
* **Trigger:** **`1H_H_BOS`** with buy-side HVC → shallow pullback; enter on **LTF_H_MSB** with rising CVD.
* **Invalidation:** Acceptance back **below** `1H.major.H_MAJOR` or immediate `1H_L_CHOCH`.
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
- 1W: `OVERALL-ASSESSMENT = NEUTRAL`.
- `PG` grades are assessed based on the plan full viability. DO NOT DEGRADE the plan based on probability/possibility.  
- DO NOT PERFORM TTI on the 1W_TF. 