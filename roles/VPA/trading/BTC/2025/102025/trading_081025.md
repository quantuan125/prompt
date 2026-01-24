# CONTEXT: 
## TRADER CONTEXT: 
Today is Wednesday 8th of October 2025, we are currently in London session, 4 hours before US session opening. We have FOMC Minutes as the major data released and news event today in 10 hours and this is the only significant event of the week. 

We have officially passed September which has been notorious for a BTC and crypto pullbacks during the bull runs year and currently enter Q4 of which has been typical bullish for bitcoin bull cycle. We should favors more bullish setups while remains as cautious as possible until BTC firmly surpasses ATH. 

Last week: Market consolidated in the weekend and bounced strongly with a confirmed 1D_H_MSB and with strong bullish follow through during the entire week, leading to the ATH during the weekend.

This week: Price levergaing daily momentum and tried to pushes firmly above ATH both in the weekend and on Monday but failed twice and sweeped twice before rolling over. Price just confirmed a fresh 1D.major.H_MAJOR level and had a daily pullback at the 1W range high. 

Sentiment: Public sentiment for October remain bullish for BTC within this year of its bullish 4 years cycle from a seasonality and historic standpoint. This is further reinforced by the recent rally on the daily. 


## TECHNICAL CONTEXT
### Key Levels 

```yaml
meta:
    pair: BTCUSDT
    units: "k"   # all numbers rounded with 'k'
    note: "Ranges use '-', e.g., 113.2-114.7k"

  ALL:
    ath: 126.2k

  1M:
    major: {}
    sr: {}
    poc:
      POC_1: 118k
      POC_2: 104.7k
    zones: 
      BUY_1: 90.0k
      BUY_2: 100.2k
    inactive:
      H_BOS: 109.6k

  1W:
    major:
      H_MAJOR: 124.5k
      L_MAJOR_2: 108.7k
      L_MAJOR_1: 107.3k
    sr:
      SR_1: 117.2k
      SR_2: 119.4k
      SR_3: 108.3k
    poc:
      POC_1: 115.6k
      POC_2: 111.2k
      POC_3: 108.8k
    zones:
      SELL_1: 123.7k
      BUY_1: 106.5k
      NEUTRAL: 116.8k
    active:
      H_CHOCH: 117.9k
    inactive:
      L_MSB: 111.9k
      H_SWEEP: 123.2k

  1D:
    major: 
      H_MAJOR: 126.2k  
      L_MAJOR: 108.6k  
    sr: 
      SR_1: 113.3k
      SR_2: 112k
      SR_3: 114.3k
      SR_4: 123.3k
    poc:
      POC_1: 113k
    zones:
      BUY_1: 114.8k
      BUY_2: 117.4k
    session:
      PDH: 125.1k
      PDL: 120.6k
    active: 
      H_MSB: 113.9k
    inactive:
      L_MSB: 114.4k
      L_BOS: 111k


  4H:
    local: {}
    major:             
      H_MAJOR: 126.2k    
      L_MAJOR: 120.6k    
    sr:
      SR_1: 124.5k
      SR_2: 121.2k
      SR_3: 120.2k
    poc: 
      POC_1: 123.9k
      POC_2: 123.0k
      POC_3: 119.6k
    zones:
      BUY_1: 121.2k
      SELL_1: 123.4-124.1k
    active:
      L_MSB: 122.3k
      H_CHOCH: 122.3k
    inactive: 
      H_SWEEP: 127.7k 

  1H:
    major:
      H_MAJOR: 123.2k
      L_MAJOR: 121.7k
    sr: {}
    poc: {}
    zones:
      BUY_1: 121.5-121.8k
    active:
      H_MSB: 122.3k
    inactive: 
      L_BOS: 123.3k

  15m:
    local:
    major:
      H_MAJOR: 123.2k
      L_MAJOR: 121.7k
    sr: {}
    poc: {}
    active:
      H_MSB: 124.0k
    inactive: 
      {}
```



### 1W — Super-HTF Structure

* **Previous (last ~30 candles):** Persistent uptrend into the **ATH** `ALL.ath` and repeated tests of weekly supply `1W.zones.SELL_1`, distribution under `1W.sr.SR_2`, then an **ATH sweep** (1W bearish VC inverted hammer) and corrective leg that **confirmed** `1W.inactive.L_MSB`. That undercut the range low and retested `1W.zones.BUY_1` with support from 1W EMA band, locating `1W.major.L_MAJOR_1`. Subsequent rally created a lower weekly high and then a **HL** at `1W.major.L_MAJOR_2` just above the rising EMA9/21.
* **Current (last ~5 candles):** Strong **bullish engulfing** last week on elevated volume broke back above `1W.poc.POC_1 → 1W.sr.SR_1`, and this week is **retesting** the `1W.zones.SELL_1` / `1W.sr.SR_2` band while price hovers just **below** weekly VWAP cluster (~123.2k). Bias: **Bullish into supply**; watch for absorption vs ignition at `1W.zones.SELL_1`.

### 1D — HTF for intraday

* **Previous (last ~30 candles):** A month ago, the **year’s largest daily liquidation** printed bearish VCs into `1D.major.L_MAJOR` (confluent with `1W.major.L_MAJOR_2`) then **1D.active.H_MSB** triggered a sharp rally. That move printed **bullish VCs** through `1D.sr.SR_4` and wicked above `1D.major.H_MAJOR` / `1W.zones.SELL_1`.
* **Current (last ~5 candles):** A **1D_bearish_VC** rejection at `1D.major.H_MAJOR`/`1W.zones.SELL_1` established a fresh **1D_H_MAJOR** and pulled back toward **EMA9 (~120.8k)** and **M-VWAP (~121.7k)** while still above `1D.active.H_MSB`. Session boundaries are `1D.session.PDH` / `1D.session.PDL`. Overhead magnets: `1W.sr.SR_2` and `4H.poc.POC_1`. Bias: **Constructive but extended into weekly supply**; hold above EMA9/M-VWAP keeps control with upside tests back into `1W.zones.SELL_1`.

### 4H — HTF for 1H

* **Previous (last ~30 candles):** Trend rode **4H EMA9** into `4H.major.H_MAJOR`/`1W.zones.SELL_1` with bullish HVCs, while RSI signaled **overbought divergence**. Price **swept** `4H.inactive.H_SWEEP` near `1D.major.H_MAJOR`/ATH and **reversed**, confirming `4H.active.L_MSB`. The pullback **held** `4H.zones.BUY_1` (confluence with M-VWAP) and set a new `4H.major.L_MAJOR`.
* **Current (last ~5 candles):** Bouncing off `4H.major.L_MAJOR` toward **rolling ST-EMAs** and **retest of `4H.active.L_MSB`**. Price sits **below W-VWAP (~123.36k)** and inside the lower half of `4H.zones.SELL_1 (123.4–124.1k)`. Bias: **Neutral-bullish recovery** while above `4H.major.L_MAJOR`; sellers likely defend the mid/upper `4H.zones.SELL_1`.

### 1H — TTF

* **Previous (last ~30 candles):** Yesterday’s selloff printed `1H.inactive.L_BOS` and a sequence of bearish HVCs that helped form `4H.active.L_MSB`. After bottoming near `4H.major.L_MAJOR`, price **coiled** in a descending wedge just under `1H.major.H_MAJOR`.
* **Current (last ~5 candles):** Breakout from the wedge delivered a **fresh `1H.active.H_MSB`**, reclaiming **S-VWAP (~121.8k)** and 1H ST-EMAs; this move is supported by 1H_bullishVC spike with raising **CVD**. Price now retests the **top of the 1H range at `1H.major.H_MAJOR` / `1H.zones.SELL_1`**, with **1H_50EMA (~122.8k)** descending as overhead dynamic resistance. Bias: **Bullish momentum vs. local supply**; need acceptance above `1H.zones.SELL_1` to open `4H.sr.SR_1 → 4H.poc.POC_1`.

## MACRO CONTEXT

### LAST WEEK

* **U.S. gov’t shutdown began (Wed, Oct 1):** Federal data pipelines (BLS, BEA) were suspended, postponing the Sept **jobs report** and risking delays to **CPI/PPI**—a key visibility hit for rates, USD, and risk assets.
* **Labor pulse (private & surveys):** **ADP** showed **–32k** Sept private payrolls (largest drop in ~2.5 years). **JOLTS (Aug)** held near **7.23M** openings while **hiring fell**, signaling cooling demand. **ISM Services (Sep)** printed **50.0** with **Prices 69.4**, implying sticky services inflation alongside weak employment.
* **Risk tone:** The **S&P 500** eked out a **record close on Fri (Oct 3)** on cut hopes/AI momentum despite shutdown risk. **Gold** surged toward fresh records into the weekend as safe-haven demand intensified.
* **Crypto flows (late week):** U.S. **spot BTC ETFs** saw strong inflows Oct 1–3, setting up a powerful start to October.
* **Global calendar:** **China Golden Week (Oct 1–7/8)** kept mainland markets shut most of the week—liquidity thinner in Asia and catch-up flows expected at reopening.

### THIS WEEK

* **Fed minutes (Today, Wed Oct 8, 2:00 pm ET):** Minutes from the **Sep 16–17 FOMC** (which cut 25 bps) are due; with the data blackout from the shutdown, markets will mine them for guidance ahead of **Oct 28–29 FOMC**.
* **Data vacuum continues:** **Weekly claims, NFP, CPI** and other federal releases are **paused** while the shutdown persists—elevating reliance on private surveys and market-based indicators.
* **AI/Tech impulse:** Reports that **xAI** is raising up to **$20B** with **NVIDIA** participation, plus fresh **OpenAI–AMD** supply deals, are supporting AI-capex sentiment and broader equity risk.
* **Crypto & metals:** **BTC** notched **new ATHs (Oct 5–6)** as **ETF inflows** accelerated (**>$1.2B** on Oct 6 alone, per fund tallies). **Gold** **broke above $4,000/oz (Oct 8)** on haven demand and rate-cut bets.
* **Geopolitics:** **Gaza** ceasefire talks continue; **Ukraine** energy-infrastructure strikes add winter fuel risk—both supportive of haven assets.
* **Holidays/liquidity:** **U.S. Columbus Day (Mon, Oct 13):** **U.S. bond market closed** (SIFMA); **NYSE open**; **CME** on holiday schedule → expect liquidity fade into/around the long weekend.
* **Asia reopens:** **China Golden Week** ends **Oct 7–8**; mainland cash markets reopen with potential catch-up volatility.

### MACRO ANALYSIS

A rare mix of **data blackout + dovish expectations + AI-capex buzz** is pushing correlations around: **yields/ USD softness** from cut hopes and shutdown uncertainty are **tailwinds for Gold** (classic haven) and **BTC** (risk-on/high-beta with “digital-gold” overtones when liquidity is loose). **SP500** is balancing AI-led strength against policy fog—**Fed minutes** are the day’s catalyst. If minutes lean dovish and the **dollar eases**, expect **Gold↑ & BTC↑** and **SPX** supported by megacap tech; a hawkish read or disorderly yield pop could pressure **SPX**, cool **BTC**, but still keep **Gold** resilient on haven flows. Watch **ETF flow tape** (BTC) and **Treasury/dollar** into the **Columbus Day** liquidity pocket.

# TRADING PLAN FOR 1H_TTF (Trigger • Location • Context)

### ORANGE_A — **Short reversal at 4H_SELL_1**

* **Context:** 1H/4H rebounds into **HTF supply** with price below **W-VWAP (~123.4k)**. Expect waning VPA as price enters `4H.zones.SELL_1 (123.4–124.1k)` beneath `4H.sr.SR_1` and LTF bearish divergence signal
* **Location:** `4H.zones.SELL_1` ≈ `4H.sr.SR_1` / `4H.poc.POC_1`.
* **Trigger:** **Liquidity sweep/failure** inside `4H.zones.SELL_1` → **15m_L_MSB**, with **bearish CVD roll** and sell-side HVC.
* **Invalidation:** 1H acceptance **above** `4H.zones.SELL_1` and **W-VWAP**, or a clean 1H **H_BOS** that converts `4H.sr.SR_1` to support.

---

### ORANGE_B — **Short reversal at PDH → 4H_H_MAJOR/ATH**

* **Context:** If momentum extends, price can probe `1D.session.PDH` and the `4H.major.H_MAJOR` near `ALL.ath`. Into that band, look for TTF **bearish divergence** on RSI/CVD and VPA **exhaustion**.
* **Location:** `1D.session.PDH` → `4H.major.H_MAJOR` / `1D.major.H_MAJOR` / `ALL.ath`.
* **Trigger:** **Double-top / failed breakout** of `1D.session.PDH` or `4H.major.H_MAJOR` → **15m_L_MSB**, ideally **1H_L_MSB**, with sell-side ignition.
* **Invalidation:** Acceptance above `4H.major.H_MAJOR` that holds on retest (trend ignition towards `1W.zones.SELL_1` extremes).

---

### PURPLE_A — **Short fade at 1H_H_MAJOR / 1H_SELL_1 (mean-reversion) confluenced with 4H_L_MSB**

* **Context:** Post-breakout pause beneath **descending 1H_50EMA (~122.8k)**; expect stalling as price tags `1H.major.H_MAJOR` / `1H.zones.SELL_1` while W-VWAP remains overhead. Fading the current 1H_H_MSB to go back to range. 
* **Location:** `1H.major.H_MAJOR` ≈ `1H.zones.SELL_1` confluenced with 1H_50EMA descending and the prior 4H_L_MSB level
* **Trigger:** **Wick-through + close back inside** below `1H.major.H_MAJOR` with **15m_L_MSB** and CVD roll; or a clean rejection from the 50EMA cap.
* **Invalidation:** 1H acceptance above `1H.major.H_MAJOR` **and** 1H_50EMA with rising CVD.

---

### RED_A — **Breakdown below 4H_L_MAJOR cluster**

* **Context:** Bias flips if the market loses the structural floor: `4H.major.L_MAJOR (120.6k)` to / **1H_200EMA (~120.6k)** / **4H_50EMA (~120.7k)**. Continuation of 4H bearish trend and 1D pullback. 
* **Location:** `4H.major.L_MAJOR` zone aligned with those MAs.
* **Trigger:** **1H_L_BOS** through `4H.major.L_MAJOR` on **bearish HVC** + falling CVD; add on weak retest from below.
* **Invalidation:** Swift reclaim of `4H.major.L_MAJOR` and S-VWAP with **1H_H_MSB**.

---

### BLUE_A — **Long fade at 1H/4H range low**

* **Context:** Pro-trend buy if pullback retests structural supports with raising 1H_200EMA/MA + M-VWAP below price.
* **Location:** `1H.major.L_MAJOR (121.1k)` → `4H.major.L_MAJOR (120.6k)` around `1D.session.PDL (120.6k)`.
* **Trigger:** **Stop-run sweep** into the band + **15m_H_MSB** and **CVD HL**; reclaim **S-VWAP (~121.8k)** to confirm.
* **Invalidation:** 1H acceptance below `4H.major.L_MAJOR`.

---

### TEAL_A — **Long momentum reclaim above range high**

* **Context:** If buyers maintain thrust and acceptance above 1H_SELL_1 zone, wait for **raising S-VWAP to catch up** with price driving through the range high sets continuation.
* **Location:** `1H.zones.SELL_1 / 1H.major.H_MAJOR (122.3k)` confluenced with 1H_ST-EMAs S_VWAP raising. 
* **Trigger:** **1H close above** `1H.major.H_MAJOR/1H_SELL_1` with **bullish HVC + rising CVD**, then buy first shallow pullback while **S-VWAP** holds as support.
* **Invalidation:** Failure back **below** `1H.major.H_MAJOR` and S-VWAP with **1H_L_CHOCH**.

---

### YELLOW_A — **Long deeper pullback at 1H_BUY_1 + 1H_L_MAJOR**

* **Context:** Mean-reversion long if intraday sells deepen but trend context remains intact and S-VWAP begins **rolling up**.
* **Location:** `1H.zones.BUY_1 (121.5–121.8k)` with extension to `1H.major.L_MAJOR (121.1k)`.
* **Trigger:** **Absorption tell** (stalling wicks) + **15m/1H_H_MSB**; confirm S-VWAP curl up and CVD turn positive.
* **Invalidation:** Close below `1H.major.L_MAJOR` or a sell-side SHVC through the band, proceed to blue_A plan instead. 

---

### GREEN_A — **Long retest of breakout at 1H_H_MAJOR** (ACTIVE)

* **Context:** Classic break-retest-go if price first clears and then **retests** the former cap at the broken 1H_H_BOS level. 
* **Location:** `1H.major.H_MAJOR (122.3k)`.
* **Trigger:** **Reclaim → Low-volume retest** → **15m_H_MSB** while CVD holds higher lows.
* **Invalidation:** Loss of `1H.major.H_MAJOR` on closing basis with **1H_L_CHOCH**.

---

### GREEN_B — **Long retest after 4H_H_MAJOR/ATH breakout**

* **Context:** If buyers push through the HTF lid, expect the first pullback to be defended.
* **Location:** `4H.major.H_MAJOR (126.2k)` / `1D.major.H_MAJOR` / `ALL.ath`.
* **Trigger:** **Breakout HVC** → first **low-volume retest** with **LTF_H_MSB** + rising CVD.
* **Invalidation:** Acceptance back **below** `4H.major.H_MAJOR` or immediate **1H_L_CHOCH** after entry.
  
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
- 1D: `HTF = BULLISH*`. 
- 4H: `PRICE = BEARISH*`; `OVERALL-ASSESSMENT = NEUTRAL-BEARISH`
- `PG` grades are assessed based on the plan full viability. DO NOT DEGRADE the plan based on probability/possibility.  
- DO NOT PERFORM TTI on the 1W_TF. 