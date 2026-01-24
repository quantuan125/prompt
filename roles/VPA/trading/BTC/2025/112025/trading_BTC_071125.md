# CONTEXT: 
## TRADER CONTEXT: 
Today is Friday 7th of November 2025, we are in London session, 4 hours until US session. We have no major macro data released today. Due to government shutdown, we have not received many major macro economic data such as NFP/Unemployment/PPI for the last month and this is expected to continue this week. Refers to `MACRO CONTEXT` for the rest of the macro events this week. 

Last month: We have officially passed October which was supposed to be bullish month for BTC and crypto in terms of seasonality during a bull cycle year, however we got the opposite of that: largest crypto liquidation sell off after sweeping the ATH followed by choppy bearish price actions despite soft CPI + Inflation data print. 

Last week: Market seems to be responded positive to FED decisions coupled with positive resolution on China-US tariffs news which allow US equities putting new ATH, BTC recovering and cool-off on gold hyperbolic bullruns, signaling a potential risk-off environment. We also had FOMC last Wednesday in which the key details are outlined below:
```markdown
* **Cut 25 bps** to a **3.75%–4.00%** fed-funds target range; **two dissents** (Miran wanted –50 bps; Schmid preferred no change).
* **Ended QT effective Dec 1**: the Committee will **stop shrinking the balance sheet** and **reinvest all principal** thereafter (Treasuries rolled over; **all agency/MBS principal reinvested into T-bills**).
* **Operating settings** (implementation note): **IORB 3.90%**, **ON RRP 3.75%**, **SRF min 4.00%**, $500B aggregate SRF limit, RRP **$160B per-counterparty**.
* **Powell’s tone**: another cut in **December is “not a foregone conclusion,”** stressing data uncertainty amid the shutdown. 
* **Context & reaction**: Statement added emphasis on **rising downside risks to employment**; markets whipsawed as traders digested the **easing + QT end** vs **no December pre-commitment**.

> Why this matters: Ending QT + a 25-bp cut = **easier financial conditions via reserves/liquidity** and **lower policy rate**, but Powell explicitly **kept optionality**, so the **path** (not the single cut) drives cross-asset pricing.
```

This week: ISM data released this week shows mixed signal and has little effects on the market so far. Price continued to sold off after the liquididation from last month, however despite bearish trend, given BTC 1W `OVERALL_ASSESSMENT = NEUTRAL-BEARISH`, we should remains cautious with breakout at either side of the 1W major structure and leaves room to trade mean-reversion at HTF extreme as much as possible. 

Sentiment: Public sentiment for Q4 remain bullish for BTC within its bullish 4 years cycle from a seasonality and historic standpoint. However price action last month have liquidated millions of leveraged crypto traders and enact fears with hypothesis of the top for the cycle is already set for BTC, and the start of an extended bear market into 2026. `Fear & Greed Index` is currently sitting at 23 (EXTREME FEAR) continued to worsen from 30-40 (FEAR) since last week. 

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
      POC_2: 111.2
      POC_3: 109.6
      POC_4: 103.8
    zones:
      SELL_1: 119.4
      SELL_2: 115.8
      BUY_1: 106.1
      NEUTRAL: 112.6
    active:
      L_SWEEP: 108.6
    inactive:
      L_MSB: 111.9
      H_SWEEP: 124.5

  1D:
    major:
      H_MAJOR: 116.4
      L_MAJOR: 103.5
    sr:
      SR_1: 114.3
      SR_2: 110.5
      SR_3: 106.4
    poc:
      POC_1: 115.8
      POC_2: 112.9
      POC_3: 110.0
      POC_4: 108.2
      POC_5: 106.9
      POC_6: 101.9
    zones:
      SELL_1: 109.3
      SELL_2: 107.7
    session:
      PDH: 104.2
      PDL: 100.3
    active:
      L_BOS: 103.5
    inactive:
      H_SWEEP: 116.0

  4H:
    local:
      H: 102.5
      L: 100.3
    major:
      H_MAJOR: 104.5
      L_MAJOR: 98.9
    sr:
      SR_1: 116.4
    poc:
      POC_1: 110.8
      POC_2: 107.7
      POC_3: 104.5
      POC_4: 101.3
    zones:
      SELL_1: 106.0
      SELL_2: 104.7
      NEUTRAL: 102.4
      BUY_1: 100.8
    active:
      L_CHOCH: 102.7
    inactive:
      H_CHOCH: 111.2
      L_BOS: 106.7

  1H:
    major:
      H_MAJOR: 102.5
      L_MAJOR: 100.3
    sr: {}
    poc: {}
    zones:
      SELL_1: 101.7
      SELL_2: 102.8
      NEUTRAL: 101.4
    active:
      L_CHOCH: 101.6
    inactive:
      L_BOS: 102.4
      H_SWEEP: 102.5

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

* **Previous (~30 candles):** Strong uptrend from late ’24 into **ATH** `ALL.ath (126.2k)` then a corrective leg with confirmed `1W.inactive.L_MSB` that broke the weekly uptrend. Pullback retested `1M.inactive.H_BOS (109.6k)` + **1W_20EMA/MA** and held to establish a range low. Since then, price has oscillated **3+ months** inside a broad weekly range with repeated liquidity events: the most recent **ATH sweep** `1W.inactive.H_SWEEP` at `ALL.ath`, followed by crypto’s large liquidation leg that tagged `1W.active.L_SWEEP (108.6k)` and extended to the extreme **range low** at `1W.major.L_MAJOR (102.0k)` on a **1W_bearish_hammer_HVC**.
* **Current (~5 candles):** Bounce from `1W.zones.BUY_1 (106.1k)` stalled into the mid-range `1W.zones.NEUTRAL (112.6k)` and failed to reclaim **1W_20EMA/MA**. This week’s developing candle is rolling over, retesting `1W.major.L_MAJOR (102.0k)` and already wicked into `1M.zones.BUY_2 (100.3k)`, overlapping the **1W_50EMA/MA** dynamic support band (historically supportive in bull cycles). HTF bias: **NEUTRAL-BEARISH** until the 1W reclaim of `1W.zones.NEUTRAL` or a fresh weekly reversal signal forms at `1W.major.L_MAJOR`.

---

### **1D — HTF for intraday**

* **Previous (~30 candles):** Post-liquidation rebound pushed to `1D.major.H_MAJOR (116.4k)` right into the weekly mid `1W.zones.NEUTRAL (112.6k→114.2k cluster)` and stalled. Subsequent leg down **confirmed** `1D.active.L_BOS (103.5k)` with **1D_bearish_engulfing_HVCs**, shifting the daily trend down while losing **1D_200EMA/MA** and **1D_W_VWAP**.
* **Current (~5 candles):** Price trades **below** all key MAs and VWAPs per CSV: `1D_9EMA≈105.1k`, `1D_21EMA≈108.1k`, `1D_50EMA≈110.9k`, `1D_200EMA≈108.1k`; `1D_W_VWAP≈103.33k`, `1D_S_VWAP≈101.43k` **>** price. RSI is weak (`1D_RSI≈34 < 1D_RSI-MA≈43`). After probing `1D.session.PDL (100.3k)`, price is attempting a meek bounce back toward the broken `1D.active.L_BOS (103.5k)` / `1D.poc.POC_6 (101.9k)` band. Session refs: `1D.session.PDH (104.2k)`, `1D.session.PDL (100.3k)`. HTF bias: **BEARISH** while below the daily EMA/VWAP stack and `1D.major.H_MAJOR`.

---

### **4H — HTF for 1H**

* **Previous (~30 candles):** Persistent downtrend after the failed upside attempt `4H.inactive.H_CHOCH (111.2k)` → continued selloff capped by descending **4H_9EMA** and **4H_W_VWAP**, with a sequence of **4H_bearish_HVCs** driving into the 1M/1W demand area around `1M.zones.BUY_2 (100.3k)` and the weekly range low, establishing `4H.major.L_MAJOR (98.9k)`. A relief bounce retested `4H.zones.SELL_2 (104.7k)` overlapping the broken `1D.active.L_BOS (103.5k)` and failed; **4H.active.L_CHOCH (102.7k)** confirmed the lower-high roll.
* **Current (~5 candles):** Price sits **below** the entire 4H stack (CSV): `4H_9EMA≈102.05k`, `4H_21EMA≈103.28k`, `4H_50EMA≈105.82k`, `4H_200EMA≈110.28k`; **VWAPs:** `4H_S_VWAP≈101.72k`, `4H_W_VWAP≈103.44k`, `4H_M_VWAP≈104.25k` — all **above** price. RSI is weak (`4H_RSI≈32.9 < RSI-MA≈36.3`). Current push faded from `4H.zones.NEUTRAL (102.4k)` and the 9EMA cap; path of least resistance remains toward `4H.zones.BUY_1 (100.8k)` → `4H.major.L_MAJOR (98.9k)` if `1D.session.PDL (100.3k)` gives way.

---

### **1H — TTF (execution)**

* **Previous (~30 candles):** Yesterday’s low formed at `1H.major.L_MAJOR (100.3k)` confluent with `1D.session.PDL (100.3k)`, then a grind higher into `4H.zones.NEUTRAL (102.4k)` stalled. A small **1H.inactive.H_SWEEP (102.5k)** failed and rolled into **`1H.active.L_CHOCH (101.6k)`**, pushing back under `1H.zones.NEUTRAL (101.4k)`.
* **Current (~5 candles):** Trend and tools are stacked bearishly (CSV): `1H_9EMA≈101.66k`, `1H_21EMA≈101.88k`, `1H_50EMA≈102.50k`, `1H_200EMA≈105.93k`; `1H_S_VWAP≈101.70k` and `1H_W_VWAP≈103.44k` both **above** price. `1H_RSI≈39 < RSI-MA≈44`. CVD for the session is rolling **negative** (≈-400 as noted), confirming sell-side control. Price is trading below `1H.zones.NEUTRAL (101.4k)` and threatening a retest of `1H.major.L_MAJOR (100.3k)` within the broader 1W/1M demand envelope.

## MACRO CONTEXT
### LAST WEEK

* **Fed (Wed, Oct 29 decision; into Nov 3–7):** The FOMC delivered a **25 bps cut to 3.75%–4.00%** and signaled that a **December cut is “not a foregone conclusion”** amid elevated uncertainty and scarce official data during the shutdown. Markets spent this week digesting the mixed message and a pause-leaning tone from Powell’s presser.
* **Policy & tariffs (late Oct → this week):** The administration announced a **partial tariff rollback tied to “fentanyl-related” lines (effective Nov 10)** even as the **Supreme Court began hearings on the legality of the broader tariff regime**—keeping trade policy a live macro overhang.
* **Shutdown overhang:** The **federal shutdown continued**, limiting official releases; private proxies filled the gap (e.g., **Chicago Fed unemployment estimate edging to ~4.4% for Oct**). Liquidity and confidence were periodically hit by “data-vacuum” headlines.
* **Treasury refunding (Wed):** Treasury’s **quarterly refunding kept coupon sizes steady** and teed up next week’s 3Y/10Y/30Y auctions—another focal point for term premia and cross-asset risk.
* **Crypto flows & cross-asset tone:** **Spot BTC ETF flows were choppy with notable outflows early week and stabilization later; ETH ETFs improved late week.** Risk assets whipsawed around policy headlines; **gold faded mid-week after a strong October but stayed near the $3.9–4.0k zone** as real-rate swings and Fed-independence worries tugged in both directions.

### THIS WEEK

* **Key U.S. prints (ET → CET):**

  * **Thu, Nov 13, 08:30 ET (14:30 CET)** – **CPI (Oct)**; **Real Earnings (Oct)**.
  * **Fri, Nov 14, 08:30 ET (14:30 CET)** – **PPI (Oct)** & **Retail Sales (Oct, Census)** (Retail Sales timing per Census calendar).
  * Note: Release logistics remain **shutdown-contingent**, but agencies have published calendars.
* **Fedspeak/Events:** Select regional bank events mid-week (e.g., New York Fed/Williams remarks posted Nov 7). Markets remain sensitive to any hints on **balance-sheet stance** and the **bar for further cuts** after Oct’s meeting.
* **UST supply (all at 13:00 ET / 19:00 CET):** **Mon, Nov 10 – 3Y**; **Wed, Nov 12 – 10Y**; **Thu, Nov 13 – 30Y**. Coupon sizes held steady in the refunding.
* **Holidays/Liquidity:** **Tue, Nov 11 – Veterans Day.** **NYSE/Nasdaq OPEN**, but **U.S. bond market CLOSED** (SIFMA). Expect **dented rates-liquidity Tue** and **auction-related rate moves Wed–Thu**.
* **Global cues:** **Germany ZEW (Tue)**; **Eurozone Industrial Production (Wed/Thu)**; **UK monthly GDP (Thu pre-US)**. In tech policy, **U.S.–China AI chip restrictions** remain in focus for semis and AI-beta equities.
* **Tariffs/legal risk:** **Supreme Court tariff hearings** and **Fed-independence litigation (Lisa Cook case)** stay in the headlines—binary headline risk for **USD, rates term premium, gold**, and broader risk appetite.

### MACRO ANALYSIS

#### BTC & ETH

Crypto beta remains **rates-sensitive**: **UST supply (Wed/Thu) + CPI (Thu)** are the key catalysts. **ETF flow breadth** matters—**BTC spot ETFs showed early-week outflows**, while **ETH flows improved late week**; sustained net-inflows would support **risk-on follow-through** post-CPI. Trade-policy headlines can swing **USD/liquidity** and thus **BTC correlation** near the U.S. equity open. Base case: **range until CPI**, then directional impulse with **USD/real-rate**. **ETH** may **outperform on improved flow tone** if macro is benign; a **hawkish CPI + heavy auctions** likely re-correlates crypto **negatively** with stocks.

# TRADING PLAN FOR 1H_TTF (Trigger • Location • Context)

### **ORANGE_A — Short reversal after failed break of the 1H top**

* **Context:** With HTF/TTF aligned **bearish** (price below **1H/4H/1D** EMAs & VWAPs), a squeeze into the 1H top is vulnerable to failure. Expect a wick/failed acceptance through `1H.major.H_MAJOR (102.5k)` inside the sell band.
* **Location:** `1H.zones.SELL_1 (101.7k)` → `1H.zones.SELL_2 (102.8k)` surrounding `1H.major.H_MAJOR (102.5k)`; overhead resistances: `4H.zones.NEUTRAL (102.4k)` / `1D.poc.POC_4 (108.2k)` with **W_VWAP** still above.
* **Trigger:** **LTF_H_SWEEP → TTF_L_MSB** back below `1H.major.H_MAJOR` with **bearish CVD turn** and a **1H_bearish_ignition_HVC** rejecting the band.
* **Invalidation:** 1H acceptance and hold **above** `1H.zones.SELL_2 (102.8k)` with rising CVD (then stand aside / reassess).
* **Setup Priority:** **A-**

---

### **ORANGE_B — Short continuation on pullback to 1H mid**

* **Context:** Downtrend intact; we want the classic sell-the-rip. Price below `1H_S_VWAP` and `1H_9/21EMA`, CVD negative.
* **Location:** Pullback to `1H.zones.NEUTRAL (101.4k)` overlapping `1H_9/21EMA` + `S_VWAP`.
* **Trigger:** **`1H_L_CHOCH` present → sell the retest** via **`LTF_L_MSB`** + decreasing pullback volume; resume lower-highs sequence.
* **Invalidation:** Reclaim and hold above `1H.zones.NEUTRAL (101.4k)` and `S_VWAP` with bullish CVD.
* **Setup Priority:** **A+**

---

### **PURPLE_A — Short fade from 1H mid to top of range**

* **Context:** If price grinds up but VPA/CVD show stall, fade the upper band of the 1H range.
* **Location:** From `1H.zones.NEUTRAL (101.4k)` up into `1H.zones.SELL_1 (101.7k)` / test of `1H.major.H_MAJOR (102.5k)`.
* **Trigger:** **`LTF_H_SWEEP` of `1H.zones.SELL_1` → `LTF_L_CHOCH`** back inside with falling CVD.
* **Invalidation:** 1H close above `1H.major.H_MAJOR (102.5k)` that converts to support.
* **Setup Priority:** **B+**

---

### **PINK_A — Short scalp momentum (below S_VWAP + 1H_9EMA)**

* **Context:** Intraday momentum remains down; we want to join continuation on shallow retests of the ST-EMAs while below `S_VWAP`.
* **Location:** Under `1H_S_VWAP` and `1H_9EMA` during a weak bounce.
* **Trigger:** Retest of **LTF_9/21EMA** that fails with **`LTF_L_BOS`** + sell-side **VC/HVC** and negative CVD.
* **Invalidation:** Swift reclaim of `S_VWAP` **and** `1H_21EMA` with HLs forming.
* **Setup Priority:** **B**

---

### **RED_A — Short breakdown of 1H major low + PDL**

* **Context:** A decisive failure of the base aligns with HTF bearishness and opens the door to `4H.major.L_MAJOR`.
* **Location:** Clean break **below** `1H.major.L_MAJOR (100.3k)` / `1D.session.PDL (100.3k)`.
* **Trigger:** **`1H_L_MSB`** on a **1H_bearish_ignition_HVC** and falling CVD → sell the **low-volume retest** (**`LTF_L_CHOCH`**).
* **Invalidation:** Swift reclaim back above `1H.major.L_MAJOR (100.3k)` with a **TTF_H_CHOCH**.
* **Setup Priority:** **B**

---

### **BLUE_A — Long fade at 1H base (counter-trend)**

* **Context:** If sellers exhaust into the higher-timeframe demand shelf, look for a liquidity sweep and absorption. Expect **regular bullish divergence** on LTF RSI/CVD.
* **Location:** `1H.major.L_MAJOR (100.3k)` + `1D.session.PDL (100.3k)` with proximity to `4H.zones.BUY_1 (100.8k)` and `1M.zones.BUY_2 (100.3k)`.
* **Trigger:** **`LTF_L_SWEEP` → `LTF_H_MSB`** with absorption VC (wicky candle, CVD uptick), then reclaim of `S_VWAP`.
* **Invalidation:** Acceptance below `1H.major.L_MAJOR (100.3k)` on a sell-side **HVC/SHVC** (defer to **RED_A**).
* **Setup Priority:** **B-** 

---

### **TEAL_A — Long momentum scalp on reclaim of S_VWAP + 1H_9/21EMA**

* **Context:** A sharp reclaim signals TTF realignment even while HTF is still heavy; treat as tactical.
* **Location:** Back above `S_VWAP` and `1H.zones.NEUTRAL (101.4k)` with HLs.
* **Trigger:** **`LTF_H_BOS`** after a fresh **`LTF_H_MSB`** that flips the band, with rising CVD and series of bullish **VC/HVC**.
* **Invalidation:** Loss of `S_VWAP` and `1H_9EMA` immediately after entry.
* **Setup Priority:** **B**

---

### **YELLOW_A — Long confirmed reversal at 4H demand**

* **Context:** If breakdown extends into deeper HTF demand, look for a confirmed major reversal.
* **Location:** `4H.zones.BUY_1 (100.8k)` → extension into `4H.major.L_MAJOR (98.9k)` within `1M.zones.BUY_2 (100.3k)`.
* **Trigger:** Clear **`TTF_H_MSB`** (15m/1H) after a stopping/absorption **HVC/SHVC**, then buy the first pullback.
* **Invalidation:** Continued acceptance below `4H.major.L_MAJOR (98.9k)` with heavy sell VPA.
* **Setup Priority:** **A-**

---

### **GREEN_A — Long breakout & retest above the 1H top**

* **Context:** Only if buyers win back control.
* **Location:** Clean break and retest of `1H.major.H_MAJOR (102.5k)` while reclaiming `1H_S_VWAP` and ST-EMAs.
* **Trigger:** **`1H_H_BOS`** with buy-side ignition **HVC** → **`LTF_H_CHOCH`** on the first retest, rising CVD.
* **Invalidation:** Failure retest (acceptance back below `1H.major.H_MAJOR`) or immediate **`1H_L_CHOCH`**.
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