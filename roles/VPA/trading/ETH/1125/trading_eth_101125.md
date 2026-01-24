# CONTEXT: 
## TRADER CONTEXT: 
Today is Monday 10th of November 2025, we are in  US session. Due to government shutdown, we have not received many major macro economic data such as NFP/Unemployment/PPI for the last month and this is expected to continue this week. Refers to `MACRO CONTEXT` for the rest of the macro events this week. 

### BTC

Last month: We have officially passed October which was supposed to be bullish month for BTC and crypto in terms of seasonality during a bull cycle year, however we got the opposite of that: largest crypto liquidation sell off after sweeping the ATH followed by choppy bearish price actions despite soft CPI + Inflation data print + resolution on China-US tariffs.

Last week: ISM data released shows mixed signal and has little effects on the market so far. All markets including equities, gold find some sort of cool-off after reaching ATH, with BTC and crypto price continued its weakness after the liquididation from last month. 

This week: BTC remains at 1W range low and find some bounces despite bearish daily trend. Given BTC 1W `OVERALL_ASSESSMENT = NEUTRAL-BEARISH`, we should remains cautious with breakout at either side of the 1W major structure and leaves room to trade mean-reversion at HTF extreme as much as possible. 

Sentiment: Public sentiment for Q4 remain bullish for BTC within its bullish 4 years cycle from a seasonality and historic standpoint. However price action last month have liquidated millions of leveraged crypto traders and enact fears with hypothesis of the top for the cycle is already set for BTC & ETH, and the start of an extended bear market into 2026. `Fear & Greed Index` worsen from 30-40 (NEUTRAL) since last month to 29 (FEAR) but improved slightly from 23 (EXTREME FEAR) since last week. 
  
## TECHNICAL CONTEXT

### KEY LEVELS 
```yaml
# ETH/USDT
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
          H: 4753
          L: 3438
        major:
          H_MAJOR: 4950
          L_MAJOR: 2167
        zones:
          BUY_2: 3538
          BUY_1: 3201
          NEUTRAL: 4106
          SELL_1: 4784
        sr:
          SR_1: 4615
          SR_2: 4152
          SR_3: 3960
          SR_4: 2870
        poc:
          POC_1: 4300
          POC_2: 3859
          POC_3: 3329
        active:
          H_BOS: 2880
        inactive:
          {}

      3D:
        major:
          H_MAJOR: 4253
          L_MAJOR: 3055
        poc:
          POC_1: 4721
          POC_2: 4469
          POC_3: 4175
          POC_4: 4007
          POC_5: 3624
        zones:
          SELL_1: 3952
        active:
          L_BOS: 3429
        inactive:
          L_SWEEP: 3817
          L_CHOCH: 3674

      12H:
        local:
          H: 3660
        major:
          H_MAJOR: 3917
          L_MAJOR: 3055
        zones:
          SELL_1: 3700
          SELL_2: 3488
          BUY_1: 3206
          BUY_2: 3357
        active:
          L_BOS: 3682
        inactive: 
          L_CHOCH: 3933
          H_MSB: 4111

      2H:
        major:
          H_MAJOR: 3661
          L_MAJOR: 3553
        zones: {}
        active:
          L_MSB: 3553
        inactive: 
          {}

# ETH/BTC
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
          H_MAJOR: 0.04329
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
        major:
          H_MAJOR: 0.03813
          L_MAJOR: 0.03196
        poc:
          POC_1: 0.03895
          POC_2: 0.03677
          POC_3: 0.03204
        zones:
          BUY_2: 0.03226
          BUY_1: 0.02964
          SELL_1: 0.04018
          SELL_2: 0.03750
          NEUTRAL: 0.03395
        active:
          L_CHOCH: 0.03804
        inactive: 
          H_MSB: 0.02975

      1D:
        major:
          H_MAJOR: 0.03692
          L_MAJOR: 0.03090
        zones:
          SELL_1: 0.03467
        active:
          H_SWEEP: 0.03706
          L_BOS: 0.03475
        inactive: 
          L_MSB: 0.03529
```

### ETH/USDT
#### **2W (Bi-Weekly – Super-HTF)**

* **Previous (≈30 bars):** Strong impulsive rally off mid-’25 base with confirmed **`2W.active.H_BOS` 2880** → leg into **`ALL.ath` 4956** / **`2W.major.H_MAJOR` 4950**. Pullback started from the ATH block; several holds around **`1M.sr.SR_1` 3745** and **`2W.poc.POC_2` 3859**.
* **Current (last 5):** Sequence printed a **`2W_bullish_doji_VC`** off **`2W.zones.BUY_2` 3538** then a **`2W_bearish_hammer_VC`** closing **under** `1M.active.H_MSB` **4095** and `2W_9EMA`. This candle is again probing **`2W.zones.BUY_2` 3538** with the body **below** `M_VWAP` and **above** `2W_21EMA`, i.e., inside demand but momentum soft. Range now defined by **`2W.zones.NEUTRAL` 4106** (mid) and **`2W.zones.BUY_1/2` (3201/3538)**.

**Bias:** 2W uptrend correcting; price sitting on demand. Failure to hold **`2W.zones.BUY_2` 3538** risks a full tag of **`2W.zones.BUY_1` 3201**; reclaim back above **`2W.zones.NEUTRAL` 4106** puts **`2W.poc.POC_1` 4300** back in play.

---

#### **3D (HTF for 12H)**

* **Previous:** After rejection in the **`ALL.ath` 4956** area, price formed a **3D_descending_channel** over ~3 months. A **`3D_bearish_hammer_HVC`** rotation confirmed **`3D.active.L_BOS` 3429**, converting the channel into a clearer downtrend. Liquidity wicked into **`2W.zones.BUY_2` 3538** / rising `3D_200EMA` to mark **`3D.major.L_MAJOR` 3055**, then bounced to retest the broken **`3D.active.L_BOS` 3429** from above.
* **Current (last 5):** Lower-highs under **`3D.zones.SELL_1` 3952** and **`3D.poc.POC_4` 4007**; closes remain **below** 9/21/50 EMAs, **above** 200 EMA. Price oscillates around **`M_VWAP` 3444** with weak RSI. This keeps **bearish structure** intact while acknowledging demand tailwinds from the bi-weekly zone.

**Bias:** HTF still **bearish to neutral**: sellers control below **`3D.zones.SELL_1` 3952**; acceptance back above 3952→**`2W.zones.NEUTRAL` 4106** would threaten shorts.

---

#### **12H (Primary TTF)**

* **Previous:** Breakdown from a **12H_wedge** confirmed **`12H.active.L_BOS` 3682** with a series of **12H_bearish_HVCs**, driving into **`2W.zones.BUY_2` 3538** and probing toward **`3D.major.L_MAJOR` 3055**.
* **Current (last 5):** Bounce carried price above `12H.zones.SELL_2` + `12H_9EMA` but it **stalls under** `12H_21EMA` and **under** **`12H.zones.SELL_1` 3700**; the latest candles are pulling back **into** **`12H.zones.SELL_2` 3488** / `M_VWAP` **3470.8**. Until **`12H.active.L_BOS` 3682** is reclaimed, TTF trend remains **down**.

**Bias:** **Neutral-bearish.** Expect lower-highs capped by **`12H.zones.SELL_1` 3700** / `12H_21EMA`, with magnets **`3D.active.L_BOS` 3429** and **`3D.poc.POC_5` 3624**.

---

#### **2H (Execution lens)**

* **Current:** Price put in a top at `2H.major.H_MAJOR` just below `12H.zones.SELL_1` before rolling over with a confirmed `2H.active.L_BOS` supported by a `2H_bearish_engulfing_HVC` and currently below W_VWAP/S_WVWAP + 2H_9EMA. 

**Bias:** Intraday **sell-rips** bias while price sits **below** S/W-VWAP and **`12H_21EMA`**; fades into **`M_VWAP`** or **`3D.active.L_BOS`** require confirmation (no blind longs).

### ETH/BTC

#### **1W (Super-HTF cross)**

*Indicators (current):* Price **0.03361**; `W_9/21/50EMA` **0.03545 / 0.03416 / 0.03383** (price **below** all), `W_200EMA` **0.04449**; `W_RSI` **50.1**; `M_VWAP` **0.03352**.
*Key levels:* **`1W.active.L_CHOCH` 0.03804**, **`1W.major.L_MAJOR` 0.03196**, **mid `1W.zones.NEUTRAL` 0.03395`**, buys **`1W.zones.BUY_2`0.03226 /`BUY_1` 0.02964`**, sells **`1W.zones.SELL_2` 0.03750 / `SELL_1` 0.04018`**, POCs **`1W.poc.POC_2`0.03677 /`POC_3` 0.03204`**.

* **Previous:** After failing to hold above `W_9EMA`, a confirmed **`1W.active.L_CHOCH` 0.03804** kicked off a controlled pullback toward **`1W.zones.BUY_2` 0.03226**.
* **Current (last 5):** Lower-highs under 9/21 EMAs; defending above **`1W.poc.POC_3` 0.03204** and **`1W.major.L_MAJOR` 0.03196**.

**Read-through to ETHUSDT:** ETH still **underperforms BTC on pops** while ETHBTC is below its 9/21/50 EMAs — this **strengthens short-the-rip** logic on ETHUSDT unless ETHBTC reclaims **`1D.zones.SELL_1` 0.03467**/**`1W.zones.NEUTRAL` 0.03395**.

---

#### **1D (Cross for timing)**

*Indicators (current):* Price **0.03361**; `D_9/21/50EMA` **0.03375 / 0.03443 / 0.03536** (all **above**), `D_200EMA` **0.03313** (below); `D_RSI` **41.99**; VWAPs clustered **~0.0335–0.0356** overhead.
*Key levels:* **`1D.active.L_BOS` 0.03475**, **`1D.active.H_SWEEP` 0.03706**, **`1D.zones.SELL_1` 0.03467**, **`1D.major.L_MAJOR` 0.03090**.

* **Previous:** Persistent **1D_descending_channel**. A sweep of highs (**`1D.active.H_SWEEP` 0.03706**) preceded the breakdown (**`1D.active.L_BOS` 0.03475**), driving into the weekly demand shelf.
* **Current (last 5):** Basing attempts above `D_200EMA` but still **below** `D_9/21/50EMA` and **under** **`1D.zones.SELL_1` 0.03467**.

**Read-through:** ETHBTC daily still a headwind for sustained ETHUSDT squeezes until **0.03467–0.03475** is reclaimed.

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

### ORANGE_A — Short continuation from 12H supply

* **Context:** 12H trend remains **down** under **`12H_21EMA` 3562.5** and **`12H.active.L_BOS` 3682** with ETHBTC weak. Expect sellers to defend rallies while `W_VWAP` **3586.7** caps.
* **Location:** **`12H.zones.SELL_2` 3488 → `12H.zones.SELL_1` 3700** (prefer entries near 3560–3700 when `12H_21EMA` tags).
* **Trigger:** **`LTF_L_MSB`** after a wick into location + **bearish CVD** / absorption HVC.
* **Invalidation:** 12H acceptance **above `12H.active.L_BOS` 3682** and hold over `12H_21EMA`.
* **Setup Priority:** **A+**

---

### ORANGE_B — Short reversal at HTF cap

* **Context:** If squeeze extends, 3D supply controls.
* **Location:** **`3D.zones.SELL_1` 3952** into **`2W.zones.NEUTRAL` 4106** (overhead cap) with `12H_200EMA` **3887.1** rolling down beneath.
* **Trigger:** **`TTF_L_MSB`** (12H) at the cap, then short first low-volume retest.
* **Invalidation:** Close & hold **above `2W.zones.NEUTRAL` 4106`**; then plan is void.
* **Setup Priority:** **A**

---

### PURPLE_A — Fade the 12H major high band

* **Context:** TTF under 50/200 EMA; sell the rip into major.
* **Location:** Probe toward **`12H.major.H_MAJOR` 3917** (often coincides with pushes into **`3D.poc.POC_4` 4007**).
* **Trigger:** **`LTF_L_MSB`** + **RSI/CVD bearish divergence** at the tag.
* **Invalidation:** **`12H_H_MSB`** and sustained acceptance **above `12H.major.H_MAJOR`**.
* **Setup Priority:** **B+**

---

### PINK_A — Intraday momentum short (loss of VWAP + 12H_9EMA)

* **Context:** If price **loses S-VWAP** (**2H** ~**3595.4**) **and `12H_9EMA` 3495.1** while staying **below `3D.active.L_BOS` 3429** overhead, intraday control flips decisively to sellers.
* **Location:** Rejection under S/W-VWAP; targets the valley around **`3D.active.L_BOS` 3429** → **`12H.zones.BUY_2` 3357**.
* **Trigger:** **`LTF_L_BOS/MSB`** under VWAP with **ignition HVC** and falling CVD.
* **Invalidation:** Reclaim and hold back **above** S-VWAP.
* **Setup Priority:** **B**

---

### RED_A — Breakdown & acceptance below HTF demand

* **Context:** Bearish acceleration through the floor.
* **Location:** Clean **12H break** of **`3D.major.L_MAJOR` 3055`** / **`12H.major.L_MAJOR` 3055`**; stretch to **`2W.zones.BUY_1` 3201** first, then **deeper** if structure fails.
* **Trigger:** **`12H_L_BOS`** with **SHVC** and persistent bearish CVD; short the first retest from below.
* **Invalidation:** Swift **`H_MSB`** reclaim back **above** the broken level.
* **Setup Priority:** **B**

---

### BLUE_A — Fade long on sweep of 12H/3D lows

* **Context:** Into stacked demand with selling pressure tiring; best when ETHBTC is near **`1D.major.L_MAJOR` 0.03090** and CVD diverges positively.
* **Location:** **Liquidity sweep** of **`12H.zones.BUY_2` 3357 → `12H.zones.BUY_1` 3206** or a stop run into **`3D.major.L_MAJOR` 3055**.
* **Trigger:** **`LTF_H_MSB`** after **manipulation SHVC** and quick close back inside.
* **Invalidation:** **`12H_L_BOS`** through 3206 (see RED_A).
* **Setup Priority:** **B-**

---

### **BLUE_B — (ACTIVE) Failed-break long at `3D.active.L_BOS`**

* **Context:** Looking for a **failed** break of **`3D.active.L_BOS` 3429** followed by a reclaim of `12H_9/21EMA` with a 3D candle closed above this prior bearish broken level. 
* **Location:** **`3D.active.L_BOS` 3429** test/fake-break.
* **Trigger:** **`LTF_L_SWEEP` → `LTF_H_MSB`** + rising CVD, then hold back above `12H_9EMA`.
* **Invalidation:** Acceptance **below 3429** on increasing sell volume.
* **Setup Type:** **2B – Anticipatory HTF Realign**
* **Setup Priority:** **B+**

---

### **YELLOW_A — Long reversal from 12H demand**

* **Context:** Counter-trend reversal requiring **TTF trend-death**.
* **Location:** **`12H.zones.BUY_2` 3357 / `BUY_1` 3206** with extension to retest **`3D.major.L_MAJOR` 3055** if flushed.
* **Trigger:** **`TTF_H_MSB` (12H)** and reclaim of `12H_9/21EMA`.
* **Invalidation:** Failure back below the reclaimed MSB origin.
* **Setup Priority:** **A**

---

### **TEAL_A — (ACTIVE) 2H momentum long on VWAP + 12H_9EMA reclaim**

* **Context:** Intraday risk-on reversal if ETH reclaims **S-VWAP** (**~3595.4**) and **`12H_9EMA` 3495.1**, **and** sustains **above `3D.active.L_BOS` 3429**.
* **Location:** VWAP reclaim → push toward **`12H.zones.SELL_1` 3700** then **`3D.poc.POC_4` 4007** if momentum persists.
* **Trigger:** **`LTF_H_BOS/MSB`** after the reclaim with **ignition HVC** + rising CVD.
* **Invalidation:** Lose S-VWAP again or close back **below** `12H_9EMA`.
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