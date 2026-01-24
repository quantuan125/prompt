# CONTEXT: 
## TRADER CONTEXT: 
Today is Monday 17th of November 2025, we are in London session, 2 hours until US session. We have no major macro events or data released today. Due to government shutdown, we have not received many major macro economic data such as NFP/Unemployment/PPI for the last month and this is expected to continue this week. Refers to `MACRO CONTEXT` for the rest of the macro events this week. 

Last month: We have officially passed October which was supposed to be bullish month for BTC and crypto in terms of seasonality during a bull cycle year, however we got the opposite of that: largest crypto liquidation sell off after sweeping the ATH followed by choppy bearish price actions despite soft CPI + Inflation data print + resolution on China-US tariffs.

Last week: All markets including equities, gold find some sort of cool-off after reaching ATH, with BTC and crypto price continued its weakness after the liquididation from last month. No data released or large macro changes with the government shutdown. 

This week: The government shutdown has been resolved and data will be released this week as planned. Refers to the following details below:
```markdown
The **43-day U.S. government shutdown has ended**, after Trump signed a funding bill late last week and the federal government has now **reopened**.

Statistical agencies (BLS, BEA, Census) are **restarting data operations**, but:

* **October 2025 jobs & CPI data are likely never coming** (data collection was not done).
* Agencies are publishing **revised calendars** and “catch-up” releases for **September** and some **October** series.

So the shutdown is over, but the **October gap remains permanent** for some indicators.
```

Directive: Price is bearish across daily and weekly timeframe, short are prioritize however caution due to bearish extension into monthly demand zone. 

Sentiment: Public sentiment for Q4 remain bullish for BTC within its bullish 4 years cycle from a seasonality and historic standpoint. However price action last month have liquidated millions of leveraged crypto traders and enact fears with hypothesis of the top for the cycle is already set for BTC, and the start of an extended bear market into 2026. `Fear & Greed Index` worsen from 30-40 (NEUTRAL) since last month to 25 (FEAR) last week now to 14-17 (EXTREME FEAR) this week.    

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
      SR_3: 82.5
    poc:
      POC_1: 118.0
      POC_2: 104.7
      POC_3: 96.4
    zones:
      BUY_1: 90.0
      BUY_2: 100.3
    inactive:
      H_BOS: 109.6

  1W:
    major:
      H_MAJOR: 116.4
      L_MAJOR: 102.0
    sr:
      SR_0: 119.4
      SR_1: 114.2
      SR_2: 102.7
      SR_3: 105.6
      SR_4: 108.3
      SR_5: 100.9
    poc:
      POC_1: 115.8
      POC_2: 112.9
      POC_3: 110.0
      POC_4: 108.2
      POC_5: 106.8
      POC_6: 103.4
      POC_7: 101.8
      POC_8: 94.6
    zones:
      SELL_1: 113.5
      SELL_2: 106.1
    active:
      L_BOS: 102.0
    inactive:
      L_MSB: 111.9
      H_SWEEP: 124.5
      L_SWEEP: 108.6

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
      POC_7: 96.9
    zones:
      SELL_1: 102.5
      SELL_2: 100.3
    session:
      PDH: 96.6
      PDL: 93.0
    active:
      L_BOS: 99.0
    inactive:
      L_BOS: 103.5

  4H:
    major:
      H_MAJOR: 96.9
      L_MAJOR: 93.0
    sr:
      {}
    poc:
      POC_1: 101.3
      POC_2: 96.1
      POC_3: 95.1
      POC_4: 94.3
    zones:
      SELL_1: 98.1
      BUY_1: 93.8
      NEUTRAL: 94.9
    active:
      L_SWEEP: 94.0
    inactive:
      L_BOS: 108.8

  1H:
    local:
      L: 95.3
    major:
      H_MAJOR: 96.0
      L_MAJOR: 95.0
    sr: {}
    poc: {}
    zones:
      SELL_1: 96.6
      BUY_1: 94.5
    active:
      H_MSB: 95.6
    inactive:
      L_BOS: 93.8

  15m:
    major:
      H_MAJOR: 96.8
      L_MAJOR: 95.9
    sr: {}
    poc: {}
    zones:
      SELL_1:  96.5
    active:
      H_CHOCH: 95.8
    inactive: 
      L_BOS: 95.4
```

### **Weekly (1W – Super-HTF Structure)**

* **Previous (~30 candles):** Strong `1M_bullish_channel` leg into `1M.major.H_MAJOR` / `ALL.ath` → corrective phase confirmed via `1W.inactive.L_MSB`. Retests of `1M.inactive.H_BOS` and the weekly EMA band held initially, establishing a multi-month consolidation under `ALL.ath`. We printed an `1W.inactive.H_SWEEP` at `ALL.ath`, then crypto-wide liquidation drove a `1W.inactive.L_SWEEP` through `1M.inactive.H_BOS` with a `1W_bearish_hammer_HVC`, setting a new extreme at `1W.major.L_MAJOR`. Subsequent bounce failed beneath the EMA cluster (bearish crossover of **1W_9/20EMA**), setting a LH at `1W.major.H_MAJOR`, then a decisive `1W.active.L_BOS` through `1W.major.L_MAJOR` on a `1W_bearish_engulfing_VC` with volume spike.
* **Current (~5 candles):** The developing 1W bar is probing for a new major low while retesting `1M.zones.BUY_1` → `1M.zones.BUY_2` demand band and the lower rail of the `1M_bullish_channel`. Price is below **1W_50EMA ~100.6k** and **1W_M_VWAP ~101.4k** with **1W_RSI 41**—a **bearish** HTF state. HTF levels in play: `1W.active.L_BOS` **102.0k** overhead; demand band magnets are `1M.zones.BUY_2` **100.3k** and `1M.zones.BUY_1` **90.0k**.

---

### **Daily (1D – HTF for intraday)**

* **Previous (~30 candles):** Rejection from `1W.major.H_MAJOR` kicked off a sustained down-leg capped by falling **1D_9/21EMA**. Series of `1D_bearish_HVCs` culminated in `1D.active.L_BOS` **99.0k**, driving into the monthly demand band (`1M.zones.BUY_2 → BUY_1`).
* **Current (~5 candles):** Still **bearish**: price trades below **1D_9EMA ~98.4k**, **1D_21EMA ~102.4k**, **1D_50/200EMA ~107k**. Today is oscillating around **1D_W_VWAP ~95.2k** inside yesterday’s range `1D.session.PDH` **96.6k** / `1D.session.PDL` **93.0k**. Overhead POC magnets: `1D.poc.POC_6` **103.4k**, `1D.poc.POC_5` **106.8k**; downside structure sits above `1D.major.L_MAJOR` **98.9k** (broken and now resistance) with the local LVN/supply at `1D.zones.SELL_1` **102.5k** / `1D.zones.SELL_2` **100.3k**.

---

### **4-Hour (4H – HTF for 1H)**

* **Previous (~30 candles):** Persistent sell-off produced `4H.inactive.L_BOS` and a series of `4H_bearish_HVCs` into the 1M demand band. Weekend liquidity run printed `4H.active.L_SWEEP` **94.0k** and set `4H.major.L_MAJOR` **93.0k**, after a `4H_bullish_hammer_HVC` (largest of the downswing) and bounce.
* **Current (~5 candles):** Price has **reclaimed W_VWAP ~95.3k** and **4H_9EMA ~95.4k**, pushing toward `4H.zones.NEUTRAL` **94.9k** and testing the underside of the ST-EMA band; `4H_21EMA ~96.5k` descends above. Resistance stack: `4H.poc.POC_2` **96.1k** / `4H.poc.POC_3` **95.1k** then `4H.zones.SELL_1` **98.1k** and `4H.major.H_MAJOR` **96.9k**. Structure remains **bearish-consolidation** beneath HTF resistances.

---

### **1-Hour (1H – TTF)**

* **Previous (~30 candles):** Bottoming at `4H.major.L_MAJOR` **93.0k** through a weekend `1H.inactive.L_SWEEP` and volume surge. Asia session reclaimed **1H_S_VWAP ~95.3k** and **1H_9/21EMA ~95.4k/95.3k**, triggering `1H.active.H_MSB` **95.6k** above `4H.zones.NEUTRAL`.
* **Current (~5 candles):** Price is coiling between `1H.major.H_MAJOR` + `1H_50EMA` descending at **~96.0k** and `1H.local.L` **95.3k** with **1H_RSI 56.7** and ST-EMAs slightly rising; `1H_200EMA ~99.2k` falls overhead. CVD on LTFs is reported flat/slightly negative—consistent with **stalling** at local resistance. Immediate range references: `1H.zones.SELL_1` **96.6k**, `1H.zones.BUY_1` **94.5k**; HTF watch above is `4H.major.H_MAJOR` **96.9k** and session `1D.session.PDH` **96.6k**.

## MACRO CONTEXT
### LAST WEEK

* **Trump, tariffs & China:** Markets continued to digest the early-November implementation of Trump’s “2.0” tariff package, including sharply higher Section 301 duties (around the mid-30% range) on selected Chinese imports, while Beijing announced a *partial* suspension of some retaliatory tariffs on U.S. farm goods from 10 Nov onward. The headline risk stayed elevated even as the near-term tone on U.S.–China trade slightly de-escalated.

* **Trump fiscal & policy noise:** Domestically, Trump floated the idea of fresh **$2,000 direct checks** to U.S. households, adding to a broader narrative of looser fiscal policy and raising questions about how such measures might interact with already-sticky inflation and Fed credibility.

* **U.S. government shutdown aftermath:** A **multi-week federal shutdown** formally ended, but it left a sizeable **data hole**: October jobs and inflation reports are unlikely to be published, while more than 30 other releases were delayed. The Labor Department scheduled the **September jobs report** for release this coming week, making it the first major official labor datapoint in over a month.

* **Fed communication & internal split:** Fed officials sent **mixed signals**. Governor Miran again argued policy is **too restrictive** and that current high inflation readings are distorted by temporary factors, including tariffs and lags in housing data, while highlighting falling rents linked to tighter immigration policies. In contrast, regional Fed presidents Collins and Bostic publicly pushed back against another **December rate cut**, citing persistent inflation and resilient activity. Overall, markets marked down the probability of near-term cuts and focused on data dependency under unusually poor data visibility.

* **Risk assets & safe havens:** U.S. equities ended the week mixed (S&P marginally softer, Nasdaq under pressure, AI names rebounding late), while gold oscillated near recent record highs as investors balanced lower yields against political and geopolitical uncertainty. Crypto underperformed: **U.S. spot Bitcoin ETFs saw roughly $1.1B in net outflows over the week**, one of their worst weekly flow prints of 2025, underscoring waning institutional demand just as macro uncertainty picked up.

### THIS WEEK

* **Key U.S. data (week of 17–21 Nov, ET):**

  * **Mon 17:** **Empire State Manufacturing Index (Nov)**.
  * **Tue 18:** **Import & Export Price Indexes (Oct)**; **Industrial Production & Capacity Utilization (Oct)**; **Treasury International Capital / foreign portfolio flows (Sep)**.
  * **Wed 19:** **Housing Starts & Building Permits (Oct)**.
  * **Thu 20:** **Philadelphia Fed Manufacturing Index (Nov)**; **Conference Board Leading Indicators (Oct)**; **Existing Home Sales (Oct)**; **delayed September Employment Situation report** from the shutdown period.
  * **Fri 21:** **University of Michigan Consumer Sentiment, final (Nov)**.
    Together, this week begins to **fill the shutdown-driven data gap**, with markets especially sensitive to any signs that activity or inflation is re-accelerating under the new tariff regime.

* **Global data & PMIs:** Globally, the calendar brings **flash PMIs for November** across the major economies plus **UK CPI and retail sales**, **eurozone final CPI**, and **Japan CPI**, providing a fresh read on global growth and inflation trends that feed into both the Fed and other central banks’ reaction functions.

* **Fed & policy expectations:** With October CPI and some other reports impaired by the shutdown, traders will lean heavily on this week’s releases and upcoming **Fed communications** (including scheduled remarks from Governor Michael Barr on Friday) as they refine odds for the **December FOMC meeting**. Futures currently price just over a 40% chance of another 25 bp cut in December, down from above 60% earlier in the month, leaving room for repricing in either direction.

* **Trump geopolitics & tariffs:** Trump’s **Gaza ceasefire and security plan** has now been brought to the **UN Security Council** for a vote, adding a fresh geopolitical dimension that can influence oil, gold and broader risk sentiment. At the same time, markets remain alert to any follow-through or retaliation around the **new U.S. tariffs on China and other trading partners**, as well as potential further tweaks from Beijing after its limited suspension of some duties.

* **Tech/AI & earnings:** **Nvidia’s earnings mid-week** are a central macro-micro nexus: the company is now a bellwether for both **AI capex** and broader risk appetite. Strong numbers and upbeat guidance could reignite the tech/AI rally, support the S&P 500 and spill over into high-beta assets like BTC; disappointment would likely pressure equities, widen credit spreads and favor defensive assets (USD, Treasuries, gold).

* **Crypto flows watch:** After last week’s heavy **Bitcoin ETF outflows**, traders will closely track whether flows stabilize or remain negative. Persistent outflows would reinforce a “distribution” narrative in BTC even if equities recover; a quick snap-back to net inflows would suggest dip-buying by institutions and could tighten the link between crypto and equity beta again.

### MACRO ANALYSIS
Into today’s session, traders are walking into a **data-catch-up week** where: (1) the Fed is **data-dependent but data-blind** after the shutdown, (2) **Trump’s higher tariffs and immigration policies** keep medium-term inflation risks alive even as some retaliatory Chinese tariffs are paused, (3) **Nvidia/AI earnings** will heavily shape equity risk sentiment, and (4) **geopolitics (Gaza)** provides a constant tail-risk that can flip flows between risk assets and safe havens. Historically, **BTC trades as high-beta risk correlated with the S&P 500**, while **gold tends to move inversely to real yields and the dollar** and sometimes positively with BTC in “macro stress” regimes. Today, any shift in **Fed cut odds**, **U.S. data surprises**, or **tariff/geopolitical headlines** can therefore re-price **yields and the dollar**, with **SP500 and BTC** reacting on the risk side and **gold** absorbing safe-haven demand on the other.

#### BTC & ETH

BTC enters the week with **heavy ETF outflows, weak price action and a risk-asset beta profile** still tied to U.S. equities and the AI complex. The macro setup is asymmetric:

* On the **bullish** side, if Nvidia reassures markets and this week’s U.S. data are soft enough to revive **December cut expectations**, BTC and ETH can catch a **beta-driven bounce** alongside the S&P 500, especially if ETF outflows slow or flip back to modest inflows.
* On the **bearish** side, continued outflows, stronger-than-expected U.S. data, and hawkish Fed chatter would reinforce the narrative that institutional demand is fading just as the macro pendulum swings away from aggressive easing, leaving BTC vulnerable to further de-risking.
  Crypto may also briefly **trade more like “digital gold”** if Trump’s Gaza plan or other geopolitical shocks trigger risk-off flows but simultaneously raise questions about policy credibility and geopolitical stability—however, that regime has been intermittent and should not be assumed without confirming price/flow behavior.
  
# TRADING PLAN FOR 1H_TTF (Trigger • Location • Context)

### **ORANGE_A — Short reversal at `4H.zones.SELL_1`**

* **Context:** Counter-trend 1H bounce is fading as `4H_21EMA ~96.5k` and `4H.poc.POC_2` **96.1k** compress price under `4H.zones.SELL_1` **98.1k**. HTF trend and **1D_9/21EMA** are above price (bearish control).
* **Location:** `4H.zones.SELL_1` **98.1k** into `1D.zones.SELL_1` **102.5k** cap; watch for a rejection back toward `1D.active.L_BOS` **99.0k**, then extension to `1D.zones.SELL_2` **100.3k** / mid-magnet POCs below.
* **Trigger:** **TTF_L_MSB** after a wick/failed break into `4H.zones.SELL_1`; confirm with bearish CVD turn and a sell-side HVC/ignition.
* **Invalidation:** 1H acceptance above `4H.major.H_MAJOR` **96.9k** **and** `1D.session.PDH` **96.6k** that converts `1H.zones.SELL_1` **96.6k** into support (momentum continuation risk).
* **Setup Priority:** **A-**

---

### **PURPLE_A — Short fade on `H_SWEEP` at `4H.major.H_MAJOR` / `1D.session.PDH`**

* **Context:** Into the local ceiling (`4H.major.H_MAJOR` **96.9k**) with **1H_RSI** elevated and LTF CVD flattening; `4H_21EMA` descends. Expect failure to accept above resistance.
* **Location:** Confluence band `4H.major.H_MAJOR` **96.9k** / `1D.session.PDH` **96.6k** / `1H.zones.SELL_1` **96.6k**.
* **Trigger:** Liquidity sweep above the band, then **LTF (15m/5m) L_MSB → 1H_L_MSB** with bearish CVD / absorption SHVC.
* **Invalidation:** 1H close above `4H.major.H_MAJOR` **96.9k** that holds on retest.
* **Setup Priority:** **B+**

---

### **PINK_A — Short momentum if range fails below `1H.local.L`**

* **Context:** If the 1H coil breaks down, we align with HTF downtrend; loss of S_VWAP/ST-EMAs confirms momentum shift.
* **Location:** Below `1H.local.L` **95.3k** toward `4H.poc.POC_3` **95.1k** / `4H.poc.POC_4` **94.3k** and `4H.zones.NEUTRAL` **94.9k**.
* **Trigger:** **Confirmed 1H_L_CHOCH** then **LTF_L_BOS/MSB** on a low-volume retest while ST-EMAs roll over and CVD falls.
* **Invalidation:** Reclaim of S_VWAP **~95.3k** and `1H_9EMA ~95.4k` with 1H HL sequence restored.
* **Setup Priority:** **A-**

---

### **RED_A — Breakdown through `4H.major.L_MAJOR` / `1D.session.PDL`**

* **Context:** If liquidity flush resumes, look for sell-side ignition and continuation into monthly demand.
* **Location:** `4H.major.L_MAJOR` **93.0k** / `1D.session.PDL` **93.0k**.
* **Trigger:** **1H_L_BOS** on strong sell HVC with negative CVD → sell the low-volume retest from below (LTF_L_MSB/BOS).
* **Invalidation:** Swift reclaim back above `1H.zones.BUY_1` **94.5k** and S_VWAP with LTF HLs.
* **Setup Priority:** **B**

---

### **WHITE_A — Long continuation on pullback to `4H.zones.NEUTRAL` / `1H.zones.BUY_1` (counter-trend)**

* **Context:** Fade-buy only if pullback is **weak** vs prior 1H impulse; require realignment above S_VWAP/ST-EMAs.
* **Location:** `4H.zones.NEUTRAL` **94.9k** overlapping `1H.zones.BUY_1` **94.5k** and nearby `4H.poc.POC_4` **94.3k**.
* **Trigger:** **LTF_H_MSB** + reclaim of S_VWAP and `1H_9EMA` with rising CVD.
* **Invalidation:** 1H close below `1H.zones.BUY_1` **94.5k** or sell-side HVC at the zone.
* **Setup Priority:** **B+**

---

### **BLUE_A — Long fade on `L_SWEEP` at `4H.major.L_MAJOR` / `1D.session.PDL`**

* **Context:** SEEK exhaustion only—bearish VPA must **weaken** with RSI/CVD bullish divergences at the sweep.
* **Location:** `4H.major.L_MAJOR` **93.0k** / `1D.session.PDL` **93.0k** within `1M.zones.BUY_1` **90.0k** band.
* **Trigger:** Stop-run below the level, **LTF_H_MSB** back in, then reclaim of S_VWAP.
* **Invalidation:** Acceptance below `4H.major.L_MAJOR` **93.0k** (defer to **RED_A**).
* **Setup Priority:** **B-**

---

### **BLUE_B — Counter-trend long fade at `1H.local.L`**

* **Context:** HTFs (1W/1D/4H) remain **bearish**; 1H is a counter-trend bounce riding S_VWAP/ ST-EMAs but capped below `4H.major.H_MAJOR`. We only scalp the **range low** when sell-side VPA **weakens** and LTF **RSI/CVD** show bullish divergence.
* **Location:** Bottom band at `1H.local.L` **95.3k** confluenced with S_VWAP with wick room into `4H.zones.NEUTRAL` **94.9k**.
* **Trigger:** `L_SWEEP` into `1H.local.L` → **LTF_H_MSB** + reclaim of **S_VWAP** and `1H_9EMA`, rising CVD, and **decreasing** sell VCs on the dip.
* **Invalidation:** 1H acceptance below `1H.local.L` 
* **Setup Priority:** **B-**


---

### **TEAL_A — Long counter-trend scalp above `1H.major.H_MAJOR`**

* **Context:** If buyers hold the ST-trend above the local top, scalp to upper HTF magnets while momentum persists.
* **Location:** Sustain above `1H.major.H_MAJOR` **96.0k** / S_VWAP / `1H_9EMA`, targeting `4H.major.H_MAJOR` **96.9k** → `4H.zones.SELL_1` **98.1k**.
* **Trigger:** **LTF_H_MSB** (or H_BOS) on a shallow retest with rising CVD and increasing VCs.
* **Invalidation:** Back inside below `1H.major.H_MAJOR` **96.0k** and loss of S_VWAP.
* **Setup Priority:** **B**

---

### **YELLOW_A — Long major reversal from `4H.zones.BUY_1` / `4H.major.L_MAJOR`**

* **Context:** Only if the deeper dip tags monthly demand properly and prints a clear reversal sequence; this aims for a larger 1H/4H trend change.
* **Location:** `4H.zones.BUY_1` **93.8k** → extension into `4H.major.L_MAJOR` **93.0k** within `1M.zones.BUY_1/2` **90.0–100.3k**.
* **Trigger:** **TTF_H_MSB** (mandatory) plus absorption SHVC and CVD turn; enter the first low-volume pullback.
* **Invalidation:** Fresh LL acceptance below `4H.major.L_MAJOR` **93.0k**.
* **Setup Priority:** **A-**

---

### **GREEN_A — Long breakout & retest above `4H.major.H_MAJOR` / `1D.session.PDH`**

* **Context:** If buy-side ignition flips the 1H regime, trade the first pullback after a decisive breakout.
* **Location:** Break and hold above `4H.major.H_MAJOR` **96.9k** / `1D.session.PDH` **96.6k** and `1H.zones.SELL_1` **96.6k**.
* **Trigger:** **1H_H_BOS** with bullish HVC + rising CVD → buy the low-volume retest (**LTF_H_BOS**).
* **Invalidation:** Failure retest (acceptance back below `4H.major.H_MAJOR` **96.9k**).
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