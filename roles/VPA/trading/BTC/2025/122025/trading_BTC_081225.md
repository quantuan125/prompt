# CONTEXT: 
## TRADER CONTEXT: 
This week: Today is 8th of December 2025, we are 30 minutes into US session. We have no major macro events/data released today, however all eyes are on FOMC meeting occuring on Wednesday this week. Refers to `MACRO CONTEXT` for the rest of the macro events this week.  

Last month: We have officially passed October + November which was supposed to be bullish month for BTC and crypto in terms of seasonality during a bull cycle year, however we got the opposite of that: largest crypto liquidation sell off and continuation of weekly downtrend breaking bullish structure for the cycle despite soft CPI + Inflation data print + resolution on China-US tariffs.

Last week: Marked the end of Quantitative Tightening cycle from the FED. Soft September PPI released with market pricing in a 25bps rate cut with >85% odd for December by the FED. 

Directive: Price is bearish on weekly timeframe howvever favor mean-reversion within daily consolidation pattern with short are prioritize however caution due to bearish extension into monthly support/demand zone with prior oversold signals. 

Sentiment: With price action last month that have liquidated millions of leveraged crypto traders and enact fears, the general consensus is bearish with hypothesis of the top for the cycle is already set for BTC, and the start of an extended bear market into 2026. `Fear & Greed Index` worsen from 30-40 (NEUTRAL) since last month to 14-19 (EXTREME FEAR) last week and improving toward 20-24 (FEAR) this week as price temporarily stall on the weekly downtrend.   

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
      BUY_1: 90.0
      BUY_2: 100.3
      BUY_3: 73.7
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
      L: 87.7
    major:
      H_MAJOR: 94.2
      L_MAJOR: 83.9
    sr:
      SR_1: 114.3
      SR_2: 110.5
      SR_3: 106.4
    poc:
      POC_1: 103.4
      POC_2: 95.7
      POC_3: 84.6
      POC_4: 79.7
    zones:
      SELL_1: 98.5
      SELL_2: 94.0
      BUY_1: 85.7
      NEUTRAL: 88.9
    session:
      PDH: 91.8
      PDL: 87.8
    active:
      H_FSB: 93.2
    inactive:
      L_BOS: 88.6

  4H:
    major:
      H_MAJOR: 92.3
      L_MAJOR: 89.0
    sr:
      {}
    poc:
      POC_1: 92.0
      POC_2: 89.7
      POC_3: 87.0
      POC_4: 82.2
    zones:
      BUY_2: 90.7
      BUY_1: 89.8
      SELL_1: 92.6
    active:
      H_BOS: 91.8
    inactive:
      H_MSB: 90.3
      L_FSB: 88.1

  1H:
    major:
      H_MAJOR: 92.3
      L_MAJOR: 89.0
    sr: {}
    poc: {}
    zones:
      BUY_1: 91.5
      BUY_2: 92.3
    active:
      L_CHOCH: 91.3
    inactive:
      H_BOS: 91.8

  15m:
    major:
      H_MAJOR: 93.5
      L_MAJOR: 92.2
    sr: {}
    poc: {}
    zones:
      {}
    active:
      H_CHOCH: 92.8
    inactive: 
      H_FSB: 93.4
```

### **1W — Super-HTF Structure**

* **Previous (~30 candles):** After a strong `1M_bullish_channel` from late ’24 into `ALL.ath` / `1M.major.H_MAJOR`, the weekly trend weakened with a confirmed `1W.inactive.L_MSB`. A low-volume push printed `1W.inactive.H_FSB` into the ATH area before a record liquidation leg flushed below `1M.inactive.H_BOS` and tested `1W.major.L_MAJOR`, confirming `1W.active.L_BOS`. That sell leg printed several **`1W_bearish_VCs/HVCs`** with a bearish `1W_9/21EMA` cross and RSI/OBV confirmation. Price broke below the `1M_ascending_channel` and the rising `1W_50EMA/MA` support band, sliding into `1M.zones.BUY_1` and deep to `1M.poc.POC_4` / `1M.sr.SR_4` with the next base at `1M.major.L_MAJOR`.
* **Current (~5 candles):** Bounced off `1W.major.L_MAJOR`, now mid-range under `1W.sr.SR_3` while probing `1W.poc.POC_3`. Structure remains **bearish** under `1W.sr.SR_1`–`SR_2`. Indicators: `1W_9EMA≈97.2k`, `1W_21EMA≈102.9k`, `1W_50EMA≈99.1k` — all **above** price (`~90.0k`). `1W_RSI≈38.7` (below `1W_RSI-MA≈49.1`). Price sits **between** `W_VWAP≈90.7k` and `M_VWAP≈89.5k` on **sub-average** weekly volume (≈0.08× `vol_ma20`). Bias: **NEUTRAL-BEARISH** while below `1W.zones.SELL_2` / `1W.sr.SR_1`.

---

### **1D — HTF for intraday**

* **Previous (~30 candles):** A month-long downtrend capped by descending `1D_9/21EMA`, culminating in `1D.inactive.L_BOS` with serial `1D_bearish_engulfing_VCs` and OBV confirmation. That leg tagged `1W.major.L_MAJOR` inside `1M.zones.BUY_1`, where an absorption **`1D_bearish_hammer_HVC`** printed at capitulation with `1D_RSI` sub-25. Price rebounded into an `1D_ascending_wedge` of HLs toward `1D.major.H_MAJOR` / `1D.zones.SELL_2` and the falling `1D_21EMA`. The latest rejection occurred at `1D.active.H_FSB` with OBV/CVD divergence, leading to a HL at `1D.local.L` after a retest of `1D.zones.NEUTRAL`.
* **Current (~5 candles):** Inside the wedge, consolidating between `1D.zones.NEUTRAL` and `1D.major.H_MAJOR`/`1D.zones.SELL_2`. Indicators: `1D_9EMA≈90.2k`, `1D_21EMA≈91.5k` above price; `1D_50EMA≈97.2k`, `1D_200EMA≈103.9k` far overhead. `1D_RSI≈43.8` (just over `RSI_MA≈41.3`). VWAPs: `W/S_VWAP≈90.7k` marginally above, `M_VWAP≈90.1k` near price. Volume is **light** (≈0.46× `vol_ma20`), consistent with a **consolidation** inside the wedge. Session levels: `1D.session.PDH 91.8k`, `1D.session.PDL 87.8k`. HTF bias: **BEARISH*** (trend down, bounce inside wedge).

---

### **4H — HTF for 1H**

* **Previous (~30 candles):** After the `1D.active.H_FSB` at daily range high, 4H sold into the bottom of the `1D_wedge_pattern` near `1D.zones.NEUTRAL`, then coiled over the weekend. A `4H.inactive.L_FSB` was followed by **`4H_bullish_VC`** with volume spike and a swift `4H.inactive.H_MSB` → impulse inside the wedge. Price then rejected `4H.zones.SELL_1` and set `4H.major.H_MAJOR`, rolling into a pullback toward demand.
* **Current (~5 candles):** Retesting `4H.zones.BUY_2 90.7k` / `4H.zones.BUY_1 89.8k` with `4H.active.H_BOS 91.8k` overhead and `4H.major.H_MAJOR 92.3k` as cap. Indicators: price ≈`90.0k` sits **below** `4H_9/21/50EMA (≈90.6–90.4k)` and well below `4H_200EMA≈94.2k`; `4H_RSI≈46.6` ~ `RSI_MA≈46.8`. VWAPs: `4H_S/W_VWAP≈91.0k` overhead; `M_VWAP≈90.0k` at price. Volume on the last impulse was **elevated** (≈1.8× `vol_ma20`), pullback volume is mixed. Bias: **NEUTRAL-BULLISH*** **inside** the daily wedge but **fading** into supply until `4H.active.H_BOS` is reclaimed.

---

### **1H — TTF**

* **Previous (~30 candles):** Trend up from the wedge floor to `1H.inactive.H_BOS` at 91.8k, then a sharp roll-over with CVD bearish divergence + **`1H_bearish_HVC`** (sell VCs out-sizing the buy VCs), losing `S_VWAP` and the `1H_9/21EMA` after rejection below 4H supply.
* **Current (~5 candles):** Confirmed `1H.active.L_CHOCH 91.3k`; price drives down toward 4H demand with base at `1H.major.L_MAJOR 89.0k` with the whole MA/VWAP stack **above**: `S_VWAP≈91.3k`, `1H_9EMA≈91.2k`, `1H_21EMA≈91.0k`, `1H_50EMA≈90.6k`, `1H_200EMA≈90.4k`. `1H_RSI≈39.8` (< `RSI_MA≈59.1`). Context: **bearish intraday** while below `1D.session.PDH` / `4H.active.H_BOS`. Nearest magnets: `1W.poc.POC_3 91.4k` overhead, `1W.poc.POC_4 87.3k` and `1W.sr.SR_3 86.1k` below.

## MACRO CONTEXT
### LAST WEEK

* **Fed cut odds surged on delayed but benign inflation data:** With agencies still clearing the backlog from the 43-day government shutdown, rescheduled data showed **PCE inflation running ~2.8% YoY in September while real consumer spending rose 0.3%**, broadly in line with forecasts and reinforcing the case for easing rather than renewed tightening. Markets ended the week pricing **~85–90% odds of a 25 bp cut at the Dec 9–10 FOMC**, and U.S. equities logged a **second straight weekly gain** with the S&P 500 up ~0.3% for the week and less than 1% from record highs.

* **Growth picture: resilient services, cooling labor market:** The **ISM Services PMI for November printed 52.6**, its highest since February and the ninth expansionary month in 2025, confirming moderate but ongoing services-sector growth. At the same time, **ADP reported U.S. private payrolls down ~32k in November**, the third decline in four months, signaling a softer labor market into year-end and giving the Fed more cover to cut even as official non-farm payrolls are delayed by the shutdown.

* **Government shutdown still distorting macro visibility:** The 43-day federal shutdown forced **cancellation of the October jobs report** and pushed the **November Employment Situation release to Dec 16**, while November CPI and real earnings won’t print until **Dec 18**. Key backlog items like **JOLTS** are being rolled into combined releases, leaving policymakers and markets to lean heavily on private surveys (ADP, PMIs, confidence) ahead of this week’s Fed decision.

* **Fed independence and the next chair became a market narrative:** Headlines last week increasingly focused on **Trump’s efforts to reshape the Fed**, including attempts to remove Governor Lisa Cook, public attacks on Powell for “slow” cuts, and growing expectations that **NEC director Kevin Hassett is now the odds-on favorite (~80% prediction-market odds) to replace Powell**. Analysts and think tanks warned that a more politicized Fed could mean **lower rates short term but higher inflation and volatility risk over the medium term**.

* **Risk assets firmed; “double-bubble” worries surfaced:** U.S. stocks extended their rally, with **equities and small caps both finishing the week higher** as rate-cut hopes outweighed growth concerns. **Gold held in the $4,200 area**, logging only a small weekly loss after a strong Friday bounce, while the **BIS warned that gold (+60% YTD) and U.S. stocks (+high-teens%) are showing “explosive” price behavior together for the first time in ~50 years**, raising the specter of a concurrent bubble in both safe-haven and risk assets.

* **Crypto re-risked with macro beta:** **Bitcoin rebounded from sub-$88k lows to stabilize above $91k**, gaining roughly **6% week-on-week**, while **ETH climbed back above $3k with double-digit weekly gains**. Sentiment shifted from “extreme fear” to “fear” as BTC consolidated in an **88–91k range**, with analysts explicitly framing BTC as a **macro-sensitive high-beta play on Fed easing**, likely to react violently to this week’s FOMC outcome.

* **Trump’s tariff politics and farm sector support stayed in focus:** Ahead of today’s event, officials trailed a **$12B “bridge” farm-aid package** funded indirectly by tariff revenues to support producers hurt by the trade war and weak crop prices. At the same time, **rumors of imminent $2,000 “tariff dividend” or stimulus checks were repeatedly debunked**, underscoring the gap between campaign-style fiscal rhetoric and what has actually been legislated.

* **International backdrop: Europe stabilizing rather than collapsing:** The **euro-area composite PMI for November rose to ~52.8**, its fastest pace in 30 months, driven by services even as manufacturing lagged. That reduces tail-risk on the global growth side but, together with U.S. data, reinforces a **“slow-growth, not recession”** narrative rather than a full-blown hard landing.

---

### THIS WEEK

* **Fed politics & independence risk (Trump/Hassett):**

  * **Fed cut vs. Fed capture:** Street houses (Nomura, JPM, MS) now formally forecast a **25 bp cut this week**, citing softer labor and benign PCE, but note the decision is “contested” with unusual dissent risk. At the same time, opinion pieces and research highlight that **Trump’s push to install Kevin Hassett as Fed chair** and his attempts to lean on regional Fed presidents **raise risk premia around long-term inflation and USD credibility**, even if near-term policy is dovish.
  * **Narrative watch:** Expect headlines all week around “Fed independence,” “politicized central banking,” and “what a Hassett Fed would look like,” which can inject **event-risk premium into gold and long-duration assets** (growth stocks, crypto) even independent of the actual cut size.

* **Trump fiscal/trade moves:**

  * **Mon, Dec 8 – ~14:00** – Trump is scheduled to **announce a $12B aid package for farmers** hit by tariffs and low crop prices at a White House roundtable. This doubles down on the idea of using **tariff revenues as quasi-fiscal tools**, a theme also seen in his talk of future “tariff dividend” checks in 2026.
  * **Tariff rhetoric vs. reality:** Fact-checks and IRS guidance continue to stress that **no $2,000 stimulus or tariff-dividend checks are authorised for December 2025**, but the ongoing messaging feeds **populist-inflation concerns** and may color markets’ interpretation of future deficits and term-premium.

* **Tech / AI and equity-valuation backdrop:**

  * **Big-tech & AI still leading:** U.S. indices remain **heavily driven by mega-cap tech and AI-linked names**, with recent news including **NextEra’s expanded Google Cloud deal and Tata’s chip partnership with Intel**, reinforcing the **“AI + reshoring + clean energy capex”** narrative that underpins the S&P and Nasdaq’s outperformance.
  * **Bubble warnings:** The **BIS quarterly review** explicitly flags **simultaneous “explosive” behavior in gold and U.S. stocks**, driven in part by retail flows and AI hype, framing this week’s Fed decision as a potential **catalyst for either a blow-off or a de-risking phase**.

* **Crypto & digital-asset calendar:**

  * No major on-chain “hard” events (e.g., halving, big protocol upgrades) are scheduled for this week in BTC/ETH, so **macro headlines (Fed, USD, real yields) and ETF/institutional flows** are expected to dominate price action. Commentary from crypto desks explicitly ties **a successful Fed cut + dovish tone to “Santa-rally” narratives toward BTC 100k**, with **$87.5k–88k highlighted as key spot support**.
  
### MACRO ANALYSIS

Broadly, we’re heading into today’s U.S. session with **markets priced for a dovish outcome (25 bp cut, further easing in 2026)** but **narrative risk skewed to Fed independence, data uncertainty, and valuation bubbles**. Stocks, gold, and BTC are all trading near the upper end of multi-year ranges at the same time, which is unusual: **equities and crypto are expressing “growth + liquidity” optimism, while gold is expressing “inflation + policy-credibility” anxiety**. The FOMC outcome will determine which side of that story dominates. For intraday trading, that means **watch cross-asset reactions to real yields and the dollar first**, then infer relative strength or fragility in BTC, S&P 500, and gold from those flows.

#### BTC & ETH

BTC has **recovered from last week’s shakeout below $88k to trade above $91k**, with ETH back over $3k and outperforming on a percentage basis. The tape and commentary both frame BTC/ETH as **macro-beta plus structural-growth**: they rally with **equities and lower yields**, but also serve as a long-term hedge against **policy error and fiat debasement**. Short term, however, they are behaving like **levered risk assets**. For today, the key is that **BTC spent much of last week digesting in an 88–91k range while Fed cut odds rose**, suggesting **positioning is already leaning long into the FOMC**. That raises **“buy the rumor, sell the news” risk**: a standard 25 bp cut with cautious language could still trigger an **initial spike higher >92k followed by a sharp fade**. On the downside, **$87.5k–88k is the key macro support**: a clean break on high volume, especially if accompanied by rising real yields and an S&P wobble, would indicate a **macro-driven de-risking rather than just local liquidation noise**. For ETH, strong weekly performance and talk of tightening exchange reserves add beta; still anchor your intraday bias to BTC’s response to the U.S. rates complex.
  
# TRADING PLAN FOR 1H_TTF (Trigger • Location • Context)
## SHORT
### **ORANGE_A — Short reversal at the daily range high**

* **Context:** If a relief rally squeezes into `1D.major.H_MAJOR 94.2k` + `1D.zones.SELL_2 94.0k`, it meets the falling daily EMA band and (likely) the `4H_200EMA/MA` cluster. Expect **weakening buy-side VPA** and potential **bearish RSI/CVD divergences** as price enters this HTF supply.
* **Location:** `1D.major.H_MAJOR` ↔ `1D.zones.SELL_2` (overlaps with `1M.poc.POC_2 104.7k` below and `1W.sr.SR_1 108.3k` above as risk bands).
* **Trigger:** Liquidity sweep with `TTF_H_FSB` at the zone → **1H_L_MSB** with sell-side VC/HVC.
* **Invalidation:** 1H acceptance **above** `1D.major.H_MAJOR` and holding, or immediate **1H_H_BOS**.
* **Setup Priority:** **A**

---

### **PURPLE_A (active) — Short fade at 4H supply**

* **Context:** The last push failed near `4H.zones.SELL_1 92.6k` with **H_FSB behavior** intraday; 1H trend is down beneath `S_VWAP`/ST-EMAs. Expect buyers to tire on retests into that band.
* **Location:** `4H.zones.SELL_1 92.6k` below `4H.major.H_MAJOR 92.3k`, with `1D.session.PDH 91.8k` as the immediate pivot.
* **Trigger:** **`TTF_H_FSB`** (wick above, close back below) → **15m_L_MSB** and sell VC; add on LH retest.
* **Invalidation:** 1H close and hold **above** `4H.major.H_MAJOR` (`1H_H_BOS` risk).
* **Setup Priority:** **B+**

---

### **PINK_A (active) — Short momentum below VWAP/EMAs**

* **Context:** Intraday flow is **bearish**: price is below `S_VWAP`, `1H_9/21/50/200EMA`. We want to join continuation after the recent `1H.active.L_CHOCH 91.3k`.
* **Location:** Below `1H.active.L_CHOCH 91.3k`, targeting the pocket toward `1H.major.L_MAJOR 89.0k` and then `1D.session.PDL 87.8k`.
* **Trigger:** **15m_L_BOS/MSB** continuation + **bearish VC/HVC** with falling CVD; sell the retest of the broken 15m structure.
* **Invalidation:** Reclaim of `S_VWAP` + **bullish** 15m MSB (trend realignment up).
* **Setup Priority:** **B**

---

### **RED_A — Short breakdown through major lows**

* **Context:** If the daily wedge fails, a decisive drive through **both** `1H.major.L_MAJOR 89.0k` / `4H.major.L_MAJOR 89.0k` and `1D.session.PDL 87.8k` opens the lower weekly band (`1W.poc.POC_4 87.3k` → `1W.sr.SR_3 86.1k`).
* **Location:** Sub-`1H/4H.major.L_MAJOR` with PDL cleared.
* **Trigger:** **`1H_L_BOS`** on a sell-side ignition VC/HVC → **low-volume** retest (ideally ≤50% pullback) → **15m_L_MSB/BOS** to re-enter.
* **Invalidation:** Swift reclaim of `1H/4H.major.L_MAJOR` and `S_VWAP` with 1H HL sequence restored.
* **Setup Priority:** **B**

---

## LONG

### **WHITE_A — Long continuation off 4H demand**

* **Context:** If sellers fade on the test of `4H.zones.BUY_2 90.7k` / `BUY_1 89.8k`, look for a reactive bounce toward `1D.session.PDH 91.8k`. This is **counter-trend** relative to the 1H down-flow—needs confirmation.
* **Location:** `4H.zones.BUY_2 → BUY_1`, ideally with the first reaction aligning with `1H_200EMA/MA` reclaim.
* **Trigger:** Sweep → **15m_H_MSB** + rising CVD; buy the retest of the MSB base.
* **Invalidation:** Acceptance below `4H.zones.BUY_1` (defer to **RED_A** path).
* **Setup Priority:** **A+**

### **BLUE_A — Long fade at 1H/4H major low (failed breakdown)**

* **Context:** A trap below `1H/4H.major.L_MAJOR 89.0k` with **L_FSB** and absorption would set a run back to PDL / PDH.
* **Location:** Sweep of `1H/4H.major.L_MAJOR` with wicks into `1D.zones.NEUTRAL 88.9k`.
* **Trigger:** **15m_H_MSB** after the sweep + reclaim of `S_VWAP`; enter on the pullback with buy VC.
* **Invalidation:** 1H candle closes **below** `1H/4H.major.L_MAJOR` with sell-side HVC.
* **Setup Priority:** **B+**

---

### **TEAL_A — Long momentum scalp on VWAP/EMA hold**

* **Context:** If price reclaims and **holds** `S_VWAP` + `1H_9EMA`, look for a momentum continuation back toward `1D.session.PDH 91.8k` / `4H.active.H_BOS 91.8k`.
* **Location:** Above `S_VWAP` with higher lows.
* **Trigger:** **15m_H_BOS/MSB** continuation + buy-side VC and rising CVD; buy the shallow retest.
* **Invalidation:** Loss of `S_VWAP` + **15m_L_MSB**.
* **Setup Priority:** **B**

---

### **YELLOW_A — Long major reversal at daily demand**

* **Context:** A deeper wash to `1D.zones.BUY_1 85.7k` (within the broader `1M.zones.BUY_1`) near `1D.major.L_MAJOR 83.9k` is a prime reversal candidate if climactic selling/absorption appears.
* **Location:** `1D.zones.BUY_1` → extension to `1D.major.L_MAJOR`.
* **Trigger:** Capitulation **SHVC** + **TTF_H_MSB** with clear CVD turn; buy the first pullback.
* **Invalidation:** Clean 1H acceptance below `1D.major.L_MAJOR`.
* **Setup Priority:** **A-**

---

### **GREEN_A — Long breakout & retest**

* **Context:** If buyers regain control and clear `1H/4H.major.H_MAJOR 92.3k`, momentum could extend toward `1D.major.H_MAJOR 94.2k` / `1D.zones.SELL_2`.
* **Location:** First retest of the broken `1H/4H.major.H_MAJOR` (now support).
* **Trigger:** **`1H_H_BOS` + buy HVC** → **low-volume** retest → **15m_H_MSB/BOS** to enter.
* **Invalidation:** Failed retest (acceptance back below `1H/4H.major.H_MAJOR`) or immediate **1H_L_CHOCH** after entry.
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
- 1W: `OVERALL-ASSESSMENT = BEARISH*`. DO NOT PERFORM TTI on the 1W_TF. 
- `PG` grades are assessed based on the plan full viability. DO NOT DEGRADE the plan based on probability/possibility.  

