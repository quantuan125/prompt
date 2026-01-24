# CONTEXT: 
## TRADER CONTEXT: 
Today is Monday 10th of November 2025, we are in London session, 2 hours until US session. We have no major macro events or data released today. Due to government shutdown, we have not received many major macro economic data such as NFP/Unemployment/PPI for the last month and this is expected to continue this week. Refers to `MACRO CONTEXT` for the rest of the macro events this week. 

Last month: We have officially passed October which was supposed to be bullish month for BTC and crypto in terms of seasonality during a bull cycle year, however we got the opposite of that: largest crypto liquidation sell off after sweeping the ATH followed by choppy bearish price actions despite soft CPI + Inflation data print + resolution on China-US tariffs.

Last week: ISM data released shows mixed signal and has little effects on the market so far. All markets including equities, gold find some sort of cool-off after reaching ATH, with BTC and crypto price continued its weakness after the liquididation from last month. 

This week: Price remains at 1W range low and find some bounces despite bearish daily trend. Given BTC 1W `OVERALL_ASSESSMENT = NEUTRAL-BEARISH`, we should remains cautious with breakout at either side of the 1W major structure and leaves room to trade mean-reversion at HTF extreme as much as possible. 

Sentiment: Public sentiment for Q4 remain bullish for BTC within its bullish 4 years cycle from a seasonality and historic standpoint. However price action last month have liquidated millions of leveraged crypto traders and enact fears with hypothesis of the top for the cycle is already set for BTC, and the start of an extended bear market into 2026. `Fear & Greed Index` worsen from 30-40 (NEUTRAL) since last month to 29 (FEAR) but improved slightly from 23 (EXTREME FEAR) since last week. 

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
      NEUTRAL: 114.1
    active:
      L_SWEEP: 108.6
    inactive:
      L_MSB: 111.9
      H_SWEEP: 124.5

  1D:
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
      POC_6: 101.9
    zones:
      SELL_1: 109.3
      SELL_2: 107.7
      BUY_1: 98.2
    session:
      PDH: 105.5
      PDL: 101.4
    active:
      L_BOS: 103.5
    inactive:
      H_SWEEP: 116.0

  4H:
    major:
      H_MAJOR: 106.7
      L_MAJOR: 101.4
    sr:
      SR_1: 116.4
    poc:
      POC_1: 110.8
      POC_2: 107.7
      POC_3: 104.5
      POC_4: 101.3
    zones:
      SELL_1: 106.0
      BUY_1: 102.7
      BUY_2: 104.0
    active:
      H_BOS: 104.1
    inactive:
      H_CHOCH: 102.5

  1H:
    local:
      L: 105.8
    major:
      H_MAJOR: 106.7
      L_MAJOR: 104.1
    sr: {}
    poc: {}
    zones:
      BUY_1: 105.1
      BUY_2: 105.4
    active:
      H_BOS: 105.1
    inactive:
      L_SWEEP: 101.5

  15m:
    major:
      H_MAJOR: 111.6
      L_MAJOR: 113.7
    sr: {}
    poc: {}
    zones:
      SELL_1: 112.7
      BUY_1: 111.1
    active:
      L_SWEEP: 110
    inactive: 
      L_MSB: 113.6
```

### **Weekly (1W — Super-HTF Structure)**

* **Previous (~30 candles):** Strong uptrend from late ’24 into `ALL.ath` / `1M.major.H_MAJOR`, then a corrective leg confirmed by `1W.inactive.L_MSB` that broke the weekly uptrend and retested the weekly band (1W_20EMA/MA) near the prior breakout. Price consolidated under `ALL.ath` for ~3 months with multiple range sweeps: most recently a `1W.inactive.H_SWEEP` at/under `ALL.ath`, followed by the crypto liquidation leg that tagged `1W.active.L_SWEEP` and printed a `1W_bearish_hammer_HVC` at the extreme near `1W.major.L_MAJOR`. The bounce came off `1W.zones.BUY_1`, pushed toward the mid-range `1W.zones.NEUTRAL`, rejected with a bearish 9/21 weekly EMA crossover  and rotated back to the range low area.
* **Current (~5 candles):** Last week closed back **above** `1W.major.L_MAJOR` after a `1W_bearish_hammer_VC` test into the `1M.zones.BUY_1` + rising `1W_50MA/EMA` band; price is now attempting to stabilize in the lower third of the 1W range with overhead supply at `1W.zones.NEUTRAL` following `1W.zones.SELL_2 → SELL_1` and magnets at `1W.poc.POC_4` / `1W.poc.POC_3`. **HTF bias:** *Neutral-bearish range* until acceptance above `1W.sr.SR_4`/`1W.sr.SR_3`.
---

### **Daily (1D — HTF for intraday)**

* **Previous (~30 candles):** Post-liquidation rebound ran into `1D.major.H_MAJOR` beneath `1W.zones.NEUTRAL`, lost the 200-band and rolled into a bearish leg that confirmed `1D.active.L_BOS` (aided by a `1H_bearish_engulfing_HVC`). That drive based at `1D.major.L_MAJOR`, where buyers defended near the bottom of the weekly range, then bounced to **reclaim** the `1D.active.L_BOS` pivot, 1D_9EMA and M_VWAP, and is now probing the `1D.zones.SELL_2/SELL_1` supply stack.
* **Current (~5 candles):** From the CSV (latest* current candle*): 1D price **above** `1D_9EMA` but **below** `1D_21EMA/50EMA/200EMA` (bearish LT/MT stack), **above** W_VWAP and M_VWAP (VWAPs supportive). `1D_RSI` ≈ **46** with `1D_RSI-MA` rising from low-40s → constructive momentum repair but still sub-50. Volume on the bounce is **sub-MA20 (~0.54x)** → not an HVC push; treat rallies into `1D.zones.SELL_2 → SELL_1` as areas to **test for absorption**. Session anchors: `1D.session.PDH`, `1D.session.PDL`. Overhead magnets: `1D.poc.POC_4 → POC_3 → POC_2/POC_1`. **HTF bias:** *Bearish* while under the 200s, with scope for squeezes into `1D.zones.SELL_2/SELL_1`.

---

### **4-Hour (4H — HTF for 1H)**

* **Previous (~30 candles):** After the base at `1D.major.L_MAJOR`, price carved a `4H_wedge_pattern`, broke **up** over the weekend on `4H_bullish_impulse_VCs` and confirmed `4H.active.H_BOS`. The rally carried into `4H.zones.SELL_1` and printed `4H.major.H_MAJOR`, pausing just below the daily supply.
* **Current (~5 candles):** CSV shows price **above** 4H_9/21/50EMAs but **below** the LT band (4H_200EMA/200SMA) → *bearish LT, bullish ST/MT*. `4H_RSI` ≈ **65** (>50, momentum positive). Volume on the last bar ~**0.63x** of 4H_vol_ma20 → consolidation, not ignition. Currently coiling under `1D.zones.SELL_2/SELL_1` and inside `4H.zones.SELL_1`, with first support at `4H.poc.POC_3` / `4H.poc.POC_2` and structural protection at `4H.major.L_MAJOR`. **Bias:** *Bullish into HTF supply, extended vs LT MAs*; watch for exhaustion near `1W.sr.SR_4` / `1W.poc.POC_3` overhead.

---

### **1-Hour (1H — TTF for execution)**

* **Previous (~30 candles):** Trend flipped up as `1H.active.H_BOS` reclaimed the 200-band; impulse leg ran while riding S_VWAP + 1H_9EMA; acceptance formed into `4H.zones.SELL_1`. HH/HL sequence intact; multiple `1H_bullish_engulfing_VCs` on the breakout.
* **Current (~5 candles):** Price consolidates **between** `1H.local.L` and `1H.major.H_MAJOR` under `1H_H_MAJOR/4H_H_MAJOR`. CSV: price **above** all 1H MAs (9/21/50/200) and **above** S_VWAP/W_VWAP → *aligned bullish TTF*. `1H_RSI` ≈ **65** with `1H_RSI-MA` ≈ **72** (recently overbought and flattening) → risk of micro pullback/mean reversion while range-bound. Volume currently **0.22x** of 1H_vol_ma20 → low-energy coil. **TTF bias:** *Trend-up but capped by HTF supply at `1D.zones.SELL_2/SELL_1` and `1H.major.H_MAJOR`.*

## MACRO CONTEXT
### LAST WEEK

* **Fed:** The FOMC cut rates by **25 bps** on Wed (Oct 29) but **Powell warned a December cut is “not a foregone conclusion,”** highlighting divided views and limited visibility due to the **ongoing U.S. government shutdown** disrupting data (e.g., the **October jobs report was not published**). Markets faded the initial dovish read.
* **Tariffs / Trump:** The administration’s **baseline 10% “reciprocal” tariff** regime (in force since April) remained intact. Into the weekend, the White House moved to **reduce the China “fentanyl-related” tariff from 20% to 10% effective Nov 10**, while **keeping the 10% baseline**; legal challenges continued but **courts have not halted the tariffs**.
* **Tech / AI:** **Amazon–OpenAI** announced a **$38B** cloud deal that lifted mega-cap tech to start the week; **Trump pledged top Nvidia AI chips will be reserved for U.S. firms**, adding a policy tailwind to U.S. AI infrastructure and a headwind to China access.
* **Risk tone & flows:** Equities wobbled into Friday on tech-led turbulence and labor-data uncertainty. **U.S. spot Bitcoin ETFs** saw **heavy net outflows through most of the week** (briefly flipping positive on Thu), and **crypto fund flows** logged a sizeable weekly **net outflow**, pointing to risk-reduction. **Gold** firmed above **$4,000/oz** on safe-haven demand amid shutdown/tariff uncertainty.

### THIS WEEK

* **Holiday & liquidity:** **Tue, Nov 11 – Veterans Day (U.S.)**: **Stocks open, bonds closed**. Expect **thinner rates/liquidity** and knock-on effects for cross-asset volatility during the U.S. session.
* **Key U.S. data (ET)** *(release timing remains subject to shutdown-related delays)*:

  * **Thu, Nov 13, 8:30** – **CPI (Oct)** & **Core CPI**.
  * **Fri, Nov 14, 8:30** – **PPI (Oct)** & **Retail Sales (Oct)**; **10:00** – **Business Inventories (Sep)**.
* **Fed speakers (Mon–Fri):** A busy **Fedspeak** slate (e.g., **Gov. Waller ~10:20**, **Gov. Miran ~12:30 on Mon**) fills the data vacuum; tone on **December policy** and **QT/liquidity** will matter.
* **Tariff watch:** **China “fentanyl-related” tariff cut to 10% kicks in Mon (Nov 10)**; however, the **10% baseline** on most imports **stays**. Markets also watch **Capitol Hill** for signs the **shutdown endgame** is progressing.
* **Global cues:** **Eurozone** Q3/GDP updates Thu–Fri; **China** Fri prints (**retail sales & industrial production for Oct**). These feed the **USD/yields** path into CPI/PPI and can sway **gold** and **crypto beta** via risk appetite.

### MACRO ANALYSIS

#### BTC & ETH

**Risk appetite softened** as **ETF/fund flows turned negative** last week, consistent with “wait-for-CPI” positioning and Powell’s pushback on December. Crypto remains **positively correlated** to **U.S. equities** and **inversely** to **real yields/USD**. Into Thu–Fri, watch:

* **Soft CPI/PPI** → **yields ↓ / USD ↓** → **BTC/ETH relief** (beta pop);
* **Hot CPI/PPI** + hawkish Fedspeak → **yields ↑ / USD ↑** → **pressure on BTC/ETH**, especially if ETF outflows persist.
  Tariff dynamics (baseline **10%** persists) + AI export curbs reinforce a **stagflation-hedge narrative** (supports BTC “digital gold” bid), but **flows must confirm** before fading weakness.



# TRADING PLAN FOR 1H_TTF (Trigger • Location • Context)

### **ORANGE_A — Short reversal at daily supply / 4H-200 band**

* **Context:** TTF uptrend is rallying into HTF headwinds: `1D.zones.SELL_2 → SELL_1` align with a **descending** 4H_200EMA/200SMA overhead. 1D remains below the 200s; 4H is still LT-bearish. Expect **bearish RSI/CVD divergence** and slowing VCs into the zone.
* **Location:** `1D.zones.SELL_2` then `1D.zones.SELL_1` with confluence of 4H_200EMA/200SMA; magnets below at `1D.poc.POC_4/POC_3` and `1H.zones.BUY_2/BUY_1`.
* **Trigger:** **Liquidity probe** into `1D.zones.SELL_2/SELL_1` → **1H_L_MSB** (TTF) at PEZ with **bearish VPA (HVC/SHVC sell or absorption SHVC)** and **falling CVD**.
* **Invalidation:** 1H **acceptance above** `1D.zones.SELL_1` *and* 4H_200EMA with strong buy-side ignition (then defer to **GREEN_A**).
* **Setup Priority:** **A-**

---

### **ORANGE_B — Short reversal on 1H top sweep**

* **Context:** Local coil beneath `1H.major.H_MAJOR` inside HTF supply overhead. If buyers fail on a breakout, expect a **sweep → failure** pattern.
* **Location:** `1H.major.H_MAJOR` / `4H.major.H_MAJOR` with `1W.zones.SELL_1` above as larger cap.
* **Trigger:** **H_SWEEP** of `1H.major.H_MAJOR` → **1H_L_MSB** (TTF) with **bearish CVD divergence** or sell-side HVC; sell the **low-volume retest** (AEZ).
* **Invalidation:** HOD acceptance and build **above** `1H.major.H_MAJOR` (trend continuation).
* **Setup Priority:** **A-**

---

### **PURPLE_A — Short fade of local high**

* **Context:** Range scalp if momentum stalls; look for **weak VCs** and **bearish RSI/CVD divergence** near the local range top.
* **Location:** `1H.major.H_MAJOR` cap; first downside magnets `1D.session.PDH` then `1H.zones.BUY_2/BUY_1`.
* **Trigger:** Small **H_SWEEP** → **15m_L_MSB** (LTF) → failure back inside; sell retest of the sweep base.
* **Invalidation:** Strong 1H close above `1H.major.H_MAJOR`.
* **Setup Priority:** **B-**

---

### **PINK_A — Short counter-trend scalp on breakdown**

* **Context:** If the coil fails and price loses the short-term engine (S_VWAP + 1H_9EMA), expect a **mean-reversion flush** toward lower magnets while TTF remains up on higher frames.
* **Location:** Below **both** S_VWAP and 1H_9EMA, **through** `1H.local.L`.
* **Trigger:** **1H_L_CHOCH** *closing below* `1H.local.L` → retest of a fresh **15m_L_BOS/L_MSB** under a **bearish 9/21 LTF crossover**.
* **Invalidation:** Prompt reclaim of S_VWAP + 1H_9EMA with HL sequence restored.
* **Setup Priority:** **B**

---

### **RED_A — Short breakdown of the 1H major low**

* **Context:** Trend **reversal** scenario: a decisive failure of the TTF uptrend that would also threaten the 4H breakout.
* **Location:** **Loss of** `1H.major.L_MAJOR` with 1H_50EMA and 1H_200MA/EMA rolling overhead.
* **Trigger:** **1H_L_MSB** → **1H_L_BOS** through `1H.major.L_MAJOR` on **bearish HVC/SHVC** + **negative CVD**; enter the **low-volume retest**.
* **Invalidation:** Swift reclaim of `1H.major.L_MAJOR` and S_VWAP.
* **Setup Priority:** **B**

---

### **BLUE_A — Long fade at the 1H major low**

* **Context:** Buy the **failed breakdown** of the 1H range when the broader 4H impulse is intact and 1D VWAPs are supportive.
* **Location:** `1H.major.L_MAJOR` with confluence of **1H_50EMA + 1H_200MA/EMA**.
* **Trigger:** Stop-run/sweep below `1H.major.L_MAJOR` → **15m_H_MSB** with **bullish RSI/CVD divergence**; buy the **low-volume retest**.
* **Invalidation:** 1H acceptance below `1H.major.L_MAJOR`.
* **Setup Priority:** **B+**

---

### **TEAL_A — Long momentum scalp off S_VWAP + 1H_9EMA**

* **Context:** TTF trend is up and respecting the intraday engine; we want a **shallow pullback** with HLs while price holds above `1H.local.L`.
* **Location:** Confluence of **S_VWAP + 1H_9EMA** above `1H.local.L`.
* **Trigger:** **15m_H_MSB/BOS** (LTF) at the pullback PEZ with **decreasing pullback volume** vs prior 1H impulse and **rising CVD**; enter on the **low-volume retest** (AEZ).
* **Invalidation:** Loss of S_VWAP and 1H_9EMA with a confirmed **1H_L_CHOCH**.
* **Setup Priority:** **B**

---

### **YELLOW_A — Long continuation from prior BOS / demand band**

* **Context:** Trend continuation using a deeper, healthier pullback into demand while the 1D remains VWAP-supported.
* **Location:** `1D.session.PDL` + `1H.zones.BUY_1/BUY_2` **and** retest of `1H.active.H_BOS` with 1H_21EMA support.
* **Trigger:** **15m_H_MSB** at PEZ with **absorption VCs** (no follow-through on sells) and **CVD turning up**; buy the **low-volume retest**.
* **Invalidation:** 1H close below `1H.zones.BUY_1` and failure to reclaim `1H.active.H_BOS`.
* **Setup Priority:** **A+**

---

### **YELLOW_B — Long major reversal at 4H demand / BOS retest**

* **Context:** If a deeper flush develops, look for HTF buy response where 4H structure broke up.
* **Location:** `4H.zones.BUY_2 → BUY_1` overlapping the **retest of** `4H.active.H_BOS` and the **1H_50EMA**.
* **Trigger:** **1H_H_MSB** after a stop-run into the zone with **bullish absorption SHVC** + rising CVD; buy the **low-volume retest**.
* **Invalidation:** Continued acceptance below `4H.zones.BUY_2`.
* **Setup Priority:** **A-**

---

### **GREEN_A — Long breakout and retest above the tops**

* **Context:** If buyers punch through, we join **momentum ignition** through the local caps.
* **Location:** Clear break **above** `1H.major.H_MAJOR` / `4H.major.H_MAJOR`; first retest of broken level is the AEZ.
* **Trigger:** **1H_H_BOS** on **bullish HVC/SHVC** + **rising CVD** → **low-volume pullback**; confirm with **15m_H_MSB/BOS**.
* **Invalidation:** Failed retest (acceptance back below `1H.major.H_MAJOR`).
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