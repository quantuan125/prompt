# CONTEXT: 
## TRADER CONTEXT: 
Today is Thursday 30th of October 2025, we are in the US session opening hours. Due to government shutdown, we have not received any public economic data such as NFP/Unemployment/PPI for the last 3 weeks. This does means there is no looming data released today however refers to `MACRO CONTEXT` for the rest of the macro events this week. 

### BTC: 

We have officially passed September which has been notorious for a BTC and crypto pullbacks during the bull runs year and currently enter Q4 of which has been typical bullish for bitcoin bull cycle. We should favors more bullish setups while remains as cautious as possible until BTC firmly surpasses ATH. 

Last week: BTC recovered after crypto market got the biggest liquiditation sell off in the entire history, while gold has pullback significantly from its bullmarket, signaling risk-on environment supported by dovish FED and soft CPI + Inflation data print last weeks. 

This week: BTC HTF remains neutral with 1W `OVERALL_ASSESSMENT = NEUTRAL` as we are trading within this HTF range given price managed to close above the 1W range low as a confirmed `1W_L_SWEEP` and reclaimed the `1W_20EMA/MA` bull market support bands. Market seems to be respond positive to FED decisions with US equities putting new ATH and BTC recovering. This is also coupled with positive resolution on China-US tariffs news during the weekend that has haunted the market last 3 weeks. We had FOMC on Wednesday, refers to the below regarding all important details:
```markdown
* **Cut 25 bps** to a **3.75%–4.00%** fed-funds target range; **two dissents** (Miran wanted –50 bps; Schmid preferred no change).
* **Ended QT effective Dec 1**: the Committee will **stop shrinking the balance sheet** and **reinvest all principal** thereafter (Treasuries rolled over; **all agency/MBS principal reinvested into T-bills**).
* **Operating settings** (implementation note): **IORB 3.90%**, **ON RRP 3.75%**, **SRF min 4.00%**, $500B aggregate SRF limit, RRP **$160B per-counterparty**.
* **Powell’s tone**: another cut in **December is “not a foregone conclusion,”** stressing data uncertainty amid the shutdown. 
* **Context & reaction**: Statement added emphasis on **rising downside risks to employment**; markets whipsawed as traders digested the **easing + QT end** vs **no December pre-commitment**.

> Why this matters: Ending QT + a 25-bp cut = **easier financial conditions via reserves/liquidity** and **lower policy rate**, but Powell explicitly **kept optionality**, so the **path** (not the single cut) drives cross-asset pricing.
```

Sentiment: Public sentiment for October remain bullish for BTC within this year of its bullish 4 years cycle from a seasonality and historic standpoint. However price action last 2-3 weeks have liquidated millions of leveraged crypto traders and enact some fears with people hypothesizing for the top of the cycle is in for BTC, and the start of an extended bear market into 2026. `Fear & Greed Index` is currently remains at 25-30 in fear terriroty improved from extreme fear from last week. 

### ETH 
ETH is currently showing weakness after failure to breakout of the 1D descending channel and now retesting the 1D range low on ETHBTC pairs. This make sense given the sentiment and price actions from prior crypto liquidation sell off. Despite HTF on ETH remains with potential seasonality for ETH resurges during mid November, public sentiment on ETH is net bearish and entire altcoins market as a whole.  
  
## TECHNICAL CONTEXT

### KEY LEVELS 
```yaml
pairs:
  ETHUSDT:
    meta:
      pair: ETHUSDT
      units: "USDT"   # all numbers in full USDT format
      note: "Ranges use '-', e.g., 4200-4300"
    levels:
      ALL:
        ath: 4956

      1M:
        major:
          L_MAJOR: 1389
        sr:
          SR_1: 3745
          SR_2: 2767
        poc:
          POC_1: 2523
        zones:
          BUY_1: 2750
          BUY_2: 2162
        active: 
          H_MSB: 4095
        inactive:
          L_BOS: 2113

      2W:
        local: 
          L: 3438
        major:
          H_MAJOR: 4950
          L_MAJOR: 2167
        zones:
          BUY_2: 3538
          BUY_1: 3201
          SELL_1: 4784
        sr:
          SR_3: 4615
          SR_2: 3960
          SR_1: 2870
        poc:
          POC_1: 4300
          POC_2: 3338
        active:
          H_BOS: 2880
        inactive:
          {}

      3D:
        local:
          H: 4112
        major:
          H_MAJOR: 4755
          L_MAJOR: 3439
        poc:
          POC_1: 4721
          POC_2: 4469
          POC_3: 4175
          POC_4: 4007
          POC_5: 3815
          POC_6: 3645
        zones:
          SELL_1: 4423
          SELL_2: 4251
          BUY_1: 3540
          NEUTRAL: 4095
        active:
          L_SWEEP: 3817
        inactive:
          H_SWEEP: 4790

      12H:
        major:
          H_MAJOR: 4112
          L_MAJOR: 3710
        zones:
          SELL_1: 4010
          BUY_1: 3675
          NEUTRAL: 3909
        active:
          L_MSB: 3842
        inactive: 
          H_SWEEP: 4086

      2H:
        major:
          H_MAJOR: 4220
          L_MAJOR: 4042
        zones: {}
        active:
          L_MSB: 3918
        inactive: 
          H_SWEEP: 3989
          H_BOS: 3935

  ETHBTC:
    meta:
      pair: ETHBTC
      units: "decimal"   # decimal format for BTC pairs
      note: "Ranges use '-', precision to 5 decimals"
    levels:
      ALL:
        ath: 0.04326

      1M:
        major:
          H_MAJOR: 0.06132
          L_MAJOR: 0.01762
        sr:
          SR_1: 0.03974
          SR_2: 0.03562
        poc:
          POC_1: 0.03113
        zones:
          SELL_1: 0.05045
          SELL_2: 0.03956
        active:
          L_BOS: 0.04469
        inactive: {}

      1W:
        local:
          H: 0.04113
        major:
          H_MAJOR: 0.04326
          L_MAJOR: 0.03196
        poc:
          POC_1: 0.03895
          POC_2: 0.03677
          POC_3: 0.03204
        zones:
          BUY_2: 0.03226
          BUY_1: 0.02964
          SELL_1: 0.04045
          SELL_2: 0.03767
        active:
          L_CHOCH: 0.03804
        inactive: 
          H_MSB: 0.02975

      1D:
        major:
          H_MAJOR: 0.03692
          L_MAJOR: 0.03476
        zones:
          SELL_1: 0.03611
          BUY_1: 0.03325
        active:
          L_MSB: 0.03529
        inactive: 
          H_SWEEP: 0.03706
```

### ETH/USDT
### **2W (Bi-Weekly — Super-HTF)**

* **Previous (~30 bars):** May ’25 impulse confirmed **`2W.active.H_BOS` 2880**, then trend extended into **`ALL.ath` 4956** / **`2W.major.H_MAJOR` 4950**. Sellers defended the ATH shelf and a corrective leg started, with responsive bids near **`2W.zones.BUY_2` 3538** and the monthly shelf **`1M.sr.SR_1` 3745**. We also rotated around **`2W.poc.POC_1` 4300** before momentum cooled.
* **Current (last 5):** The last closed bar was a **`2W_bullish_doji_VC`** off **`2W.zones.BUY_2` 3538**. The **developing** bar sits **below** **`1M.active.H_MSB` 4095** and under **`2W_9EMA` ≈ 3,869**, with RSI **55.3** (RSI-MA **56.9**). Monthly VWAP ≈ **4,017** caps; 2W VWAP ≈ **3,917** is overhead; price **≈3,771** is sandwiched beneath **`2W.sr.SR_3` 3960** and above **`2W.poc.POC_2` 3806**/**`2W.poc.POC_3` 3338**. Structure remains HH/HL on 2W; we’re in a pullback below the pivotal **`1M.active.H_MSB` 4095**.

---

### **3D (HTF for 12H)**

* **Previous (~30 bars):** Post-ATH consolidation formed a **3D descending channel**. A **`3D.inactive.L_SWEEP` 3817`** printed via **`3D_bearish_hammer_HVC`** at the channel floor near **`3D.poc.POC_5` 3645**, prompting a bounce to the mid/upper stack: **`3D.zones.NEUTRAL`4095 →`3D.zones.SELL_2` 4251** under **`3D.major.H_MAJOR` 4253**.
* **Current (last 5):** Price **≈3,771** is **below** 3D EMA9/21 (**≈4,033/4,097**) and **near** EMA50 (**≈3,777**) with RSI **44.5** (MA **51.4**). 3D VWAPs: W≈**3,891** (just above), M≈**4,099** (firm resistance). The supply cap remains **`3D.zones.SELL_2` 4251 → `3D.zones.SELL_1` 4423**; demand is stacked at **`3D.zones.BUY_1` 3540** aligning with **`2W.zones.BUY_2` 3538**. Recent bar: **`3D_bearish_engulfing_VC`** back into the channel body.

---

### **12H (Primary TTF)**

* **Previous (~30 bars):** A **12H descending wedge** developed. Attempts to lift into **`3D.zones.NEUTRAL` 4095** stalled; the earlier **`12H.inactive.H_MSB`** preceded a rotation back inside the wedge.
* **Current (last 5):** We have a confirmed **`12H.active.L_CHOCH` 3933** and price is sitting **under** the 12H EMA stack (EMA9/21/50 ≈ **3,940/3,969/4,040**) with EMA200 ≈ **3,967** almost flat; RSI **37.2** (MA **50.1**). 12H VWAPs: W≈**4,008** and M≈**4,088** are **above**; session VWAP on the intraday ladder ≈ **3,839**. Midline **`12H.zones.NEUTRAL` 3981** is overhead; local supply **`12H.zones.SELL_1` 4050** sits below **`3D.zones.NEUTRAL` 4095**; base demand **`12H.zones.BUY_1` 3675** sits just above **`3D.poc.POC_5` 3645**. Net: corrective/range behavior **inside** wedge; sellers control while < **`12H.major.H_MAJOR` 4254**.

---

### **2H (LTF for execution)**

* **Current (last 5):** Price **≈3,771** is below EMA9/21/50/200 (**≈3,834/3,905/3,969/4,010**). RSI **30.8** (MA **37.9**). S-VWAP ≈ **3,844**, W-VWAP ≈ **4,021**, M-VWAP ≈ **4,099** — all above. Price is currently in a strong downtrend from the sell off from top of 12H/3D range and now currently approaching the 12H demand zone + 12H bottom of the wedge pattern. CVD for the last few days supported this entire bearish move. 

### ETH/BTC

#### **1W (Weekly – Super-HTF)**

* **Previous:** Major base above **`1W.poc.POC_3` 0.03204**, then impulsive advance → test of **`1M.zones.SELL_2` 0.03956** / **`1W.poc.POC_1` 0.03895** and stall below **`1W.major.H_MAJOR` 0.04326**. A confirmed `1W.active.L_CHOCH` **0.03804** started a controlled pullback toward **`1W.zones.BUY_2` 0.03226**.
* **Current:** Close **0.03531** sits **below** W-EMA9 (~**0.03638**), **above** EMA21/50 (~**0.03401/0.03372**). RSI **54.9** (>50 but **below** its MA **63.3**). Weekly VWAP/S-VWAP ~**0.03560** slightly above price; Monthly VWAP **0.03571** caps. Bias: consolidative pullback while holding above **`1W.major.L_MAJOR` 0.03196**; failure opens **`1M.poc.POC_1` 0.03113**.

---

#### **1D (Daily – HTF for ETH entries)**

* **Previous:** Clean **1D descending channel** from **`1D.inactive.H_SWEEP` 0.03706**; `1D.active.L_MSB` **0.03529** kept the trend lower with bounces capped under **`1D.zones.SELL_1` 0.03611**.
* **Current:** Close **0.03531** sits **below** D-EMA9/21/50 (~**0.03562/0.03599/0.03639**), **above** EMA200 (~**0.03291**). RSI **43.0** (<50, MA **46.0**). S/W/M VWAPs (~**0.03532/0.03552/0.03562**) lean overhead resistance. Room to probe **`1D.major.L_MAJOR` 0.03476** / **`1W.poc.POC_2` 0.03677** ping-pong until a daily BOS/MSB resolves.

## MACRO CONTEXT
### LAST WEEK

* **Fed cut & guidance:** The FOMC lowered the policy rate by **25 bps to 3.75–4.00% (Oct 29)** and signaled **no pre-commitment** to a December cut given elevated inflation and limited official data during the shutdown. Minutes for the **Oct 28–29** meeting are slated for **Nov 19**.
* **Trump, tariffs & China:** The **U.S. Senate voted 51–47 to nullify the administration’s global “reciprocal” tariffs** (symbolic for now given House dynamics). Separately, at the **Trump–Xi meeting in Korea**, the U.S. **trimmed China tariffs (headline cut cited as 57% → 47%)** alongside Chinese commitments on agriculture/rare earths; the U.S. also **paused for one year the planned expansion (“50% affiliates rule”) of certain export-control restrictions**, de-escalating near-term tech/trade tension.
* **Shutdown overhang & data:** The **federal government shutdown** persisted into the 4th week, impairing some data releases and forcing reliance on private proxies; weekly claims were estimated lower by sell-side trackers.
* **Inflation print due today:** **Sep PCE/CORE PCE (Oct 31)** on deck—key for near-term rate expectations.
* **Treasury supply watch:** Treasury reaffirmed its schedule for next week’s **Quarterly Refunding Announcement (QRA)**.

### THIS WEEK

* **Clock change & hours:** **U.S. Daylight Saving Time ends Sun, Nov 2.** From **Mon, Nov 3**, U.S. cash equities reopen at **9:30 ET = 15:30 CET** (back to the normal 6-hour gap for Copenhagen).
* **Key U.S. macro (ET → CET):**

  * **Mon, Nov 3, 10:00 → 16:00** – **ISM Manufacturing (Oct)**.
  * **Tue, Nov 4, 10:00 → 16:00** – **JOLTS (Sep)**; **Election Day (state/local, off-year)** – markets open, but watch for headline risk/occasional liquidity pockets.
  * **Wed, Nov 5** – **ADP Employment (8:15 → 14:15)**; **ISM Services (10:00 → 16:00)**; **U.S. Treasury QRA** (announcement Wednesday per Treasury).
  * **Thu, Nov 6, 8:30 → 14:30** – **Initial Jobless Claims** (ongoing data quality caveats from shutdown period).
  * **Fri, Nov 7, 8:30 → 14:30** – **Nonfarm Payrolls (Oct)**.
* **Policy & tech tapes:** Watch follow-through from **Senate tariff rebuke** (House unlikely to act near-term), **Trump–Xi de-escalation** headlines, and the **one-year pause** on the export-control “50% rule.” Ongoing **TikTok U.S. ownership** negotiations also sit in the backdrop for mega-cap tech sentiment.

### MACRO ANALYSIS

#### BTC & ETH

Crypto beta typically **tracks liquidity and rates**: a **dovish-leaning Fed** + reduced trade-war stress is supportive for **risk appetite**, but **shutdown-distorted data** raises event volatility around **PCE (today) → ISM/ADP/JOLTS → NFP**. Watch **U.S. session 15:30 CET** re-sync for flow timing. Tech-policy de-escalation (chip-rule pause/TikTok progress) is a **sentiment tailwind** for AI/tech equities—historically constructive for BTC/ETH via cross-asset risk.

# TRADING PLAN FOR 12H_TTF (Trigger • Location • Context)

**Environment read:** 12H trend is corrective-bearish (price < EMA50/200; RSI < 50; VWAPs overhead). ETHBTC daily is weak relative to its EMA stack — **favors selling rips / buying only at HTF demand with confirmation**. CVD usage: require **bearish CVD** for shorts; **rising CVD + absorption** for longs.

---

### **ORANGE_A — Short reversal at mid-stack (wedge cap test)**

* **Context:** Rallies into the 12H midline occur against a bearish EMA posture (12H EMA9/21/50 all above). ETHBTC underperforms (< D-EMA50). Expect sellers to defend the wedge cap beneath 3D supply when CVD flattens/rolls.
* **Location:** **`12H.zones.NEUTRAL` 3981** → extension into **`3D.zones.NEUTRAL` 4095** / **`12H.zones.SELL_1` 4050** cluster.
* **Trigger:** **LTF_L_MSB/CHOCH** after a wick into 3981→4050 with **absorption HVC/SHVC** and **bearish CVD divergence**.
* **Invalidation:** 12H acceptance back above **`3D.zones.NEUTRAL` 4095** with **ignition HVC** and rising CVD.
* **Setup Priority:** **A+**

---

### **PURPLE_A — Short fade the 12H/3D high-cap**

* **Context:** Top-of-range tests into HTF supply while 12H remains below EMA50/200. Ideal if the bounce is on **decreasing VCs** into location.
* **Location:** **`12H.major.H_MAJOR` 4254 / `3D.major.H_MAJOR` 4253**, stretch to **`3D.zones.SELL_2` 4251 → `3D.zones.SELL_1` 4423**.
* **Trigger:** **LTF_L_MSB** (failure back inside) after a sweep/tap; prefer **RSI/CVD regular divergence**.
* **Invalidation:** Acceptance above **`3D.zones.SELL_1` 4423** (bullish ignition).
* **Setup Priority:** **B+**

---

### **PINK_A — Intraday momentum short (retest fail at 12H mid)**

* **Context:** If a bounce retests **`12H.zones.NEUTRAL` 3981** while VWAPs (2H S-VWAP / 12H W/M-VWAP) stay overhead, expect momentum continuation lower.
* **Location:** **`12H.zones.NEUTRAL` 3981** rejection → magnets **`3D.poc.POC_5` 3645** / **`12H.zones.BUY_1` 3675**.
* **Trigger:** **LTF_L_BOS** through intraday structure with **ignition HVC** and falling CVD; add on failed VWAP retests from below.
* **Invalidation:** Reclaim and hold above **3981** with bullish CVD.
* **Setup Priority:** **B**

---

### **RED_A — Breakdown & retest short (lose 12H base)**

* **Context:** Trend transition from corrective to distributive if base gives way.
* **Location:** Clean break **below `12H.major.L_MAJOR` 3710** → target **`12H.zones.BUY_1` 3675 → `3D.zones.BUY_1` 3540** (confluence with **`2W.zones.BUY_2` 3538**).
* **Trigger:** **`12H_L_BOS`** beneath **3710** with **ignition SHVC** + bearish CVD, then short the **low-volume** retest of 3710 from below.
* **Invalidation:** Swift **`12H_H_MSB`** reclaim back above 3710.
* **Setup Priority:** **B**

---

### **BLUE_A — Fade long at wedge/base confluence**

* **Context:** Deep tests into stacked demand while selling pressure shows **decelerating VCs**. ETHBTC close to **`1D.major.L_MAJOR` 0.03476** improves odds of ETH defense.
* **Location:** **`12H.major.L_MAJOR` 3710 + `12H.zones.BUY_1` 3675** with ladder to **`3D.poc.POC_5` 3645**.
* **Trigger:** **LTF_H_MSB** after a **manipulation SHVC** sweep into 3710/3675 and **close back above** the swept level; confirm with rising CVD.
* **Invalidation:** A confirmed **`12H_L_BOS`** below **3710** (then see RED_A).
* **Setup Priority:** **B-**

---

### **GREEN_A — Breakout long (TTF realigns up)**

* **Context:** 12H wedge resolves higher and the 3D channel top gives way. Need **evidence** of trend realign (volume + CVD).
* **Location:** Break & retest of **`12H.major.H_MAJOR` 4254** (confluent with **`3D.major.H_MAJOR` 4253**).
* **Trigger:** **`12H_H_BOS`** through **4254** on **ignition HVC** + rising CVD, then long the **low-volume** retest.
* **Invalidation:** Failure back **below 4254** on a bearish **`12H_L_MSB`**.
* **Setup Priority:** **B**

---

### **YELLOW_A — Deep-dip reversal long (HTF demand)**

* **Context:** Capitulative probe into bi-weekly demand while 2W trend is still up over its EMA stack (9/21/50 all below price on the broader look).
* **Location:** **`2W.zones.BUY_2` 3538 / `3D.major.L_MAJOR` 3439**; stretch ladder toward **`2W.zones.BUY_1` 3201** if flushed.
* **Trigger:** **Manipulation SHVC** into the band + **`12H_H_MSB`** back above the swept level with CVD basing/divergence.
* **Invalidation:** Full **12H acceptance** below **`3D.major.L_MAJOR` 3439**.
* **Setup Priority:** **A-**

---

### **TEAL_A — Intraday momentum long (VWAP reclaim)**

* **Context:** Day flips risk-on if intraday VWAP is reclaimed while 12H remains range-bound.
* **Location:** **Reclaim intraday VWAP** on 2H and hold **back above `12H.zones.NEUTRAL` 3981**; targets **`12H.zones.SELL_1` 4050 → `3D.zones.NEUTRAL` 4095**.
* **Trigger:** **LTF_H_BOS** after VWAP reclaim with **ignition HVC** + rising CVD.
* **Invalidation:** Lose VWAP again and close **below 3981**.
* **Setup Priority:** **B**

# TASK  
We have outlined the colored trading plans aligned with the chart using 12H_TTF with 3D as primary trend HTF and 2W as Super HTF + structural context. Our LTF for execution is 2H or 4H. 

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
- 2W: `HTF = BULLISH*`.
- `PG` grades are assessed based on the plan full viability. DO NOT DEGRADE the plan based on probability/possibility.  
- DO NOT PERFORM TTI ON the ETH/BTC pairs. 