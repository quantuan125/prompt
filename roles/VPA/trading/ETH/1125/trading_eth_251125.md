# CONTEXT: 
## TRADER CONTEXT: 

### BTC
This week: Today is Tuesday 25th of November 2025, we are in London Session, 3.5 hours until US session. We have PPI + Retail Sales MoM in 2.5 hours as major macro events/data released today. Refers to `MACRO CONTEXT` for the rest of the macro events this week.  

Last month: We have officially passed October which was supposed to be bullish month for BTC and crypto in terms of seasonality during a bull cycle year, however we got the opposite of that: largest crypto liquidation sell off after sweeping the ATH followed by choppy bearish price actions despite soft CPI + Inflation data print + resolution on China-US tariffs.

Last week: Government shutdown resolved and we got the mixed NFP + Unemployment September data released and market seems to be pricing in hawkish FED into December FOMC. 

Directive: Price is bearish across daily and weekly timeframe, short are prioritize however caution due to bearish extension into monthly demand zone. 

Sentiment: With price action last month that have liquidated millions of leveraged crypto traders and enact fears, the general consensus is bearish with hypothesis of the top for the cycle is already set for BTC, and the start of an extended bear market into 2026. `Fear & Greed Index` worsen from 30-40 (NEUTRAL) since last month to 25 (FEAR) last week now to 14-19 (EXTREME FEAR) this week.  


### ETH
ETH remains relatively weak against BTC for the last month during this entire sell-off however there is some relatively strength and stablization within last week as price defending above the range low on ETHBTC pair. Remains safe to short ETH as long as BTC continues to shows weakness. Longs are only consider with breakout of the daily range from ETHBTC pairs. 
  
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
          H_MAJOR: 4956
          L_MAJOR: 1389
        sr:
          SR_1: 3745
          SR_2: 2767
        poc:
          POC_1: 2523
          POC_2: 3429
        zones:
          BUY_2: 2750
          BUY_1: 2162
        active: 
          H_MSB: 4095
        inactive:
          L_FSB: 2115

      2W:
        major:
          H_MAJOR: 4757
          L_MAJOR: 2167
        sr:
          SR_1: 4615
          SR_2: 4152
          SR_3: 3960
          SR_4: 2870
        poc:
          POC_1: 4300
          POC_2: 3859
          POC_3: 3329
          POC_4: 2640
        zones:
          BUY_1: 3235
          SELL_1: 4220
        active:
          L_CHOCH: 3437
        inactive:
          H_BOS: 2880

      3D:
        major:
          H_MAJOR: 4253
          L_MAJOR: 2624
        poc:
          POC_1: 3624
          POC_2: 3171
          POC_3: 3027
          POC_4: 2880
        zones:
          SELL_1: 3672
          SELL_2: 3247
        active:
          L_BOS: 3439
        inactive:
          H_FSB: 4112
          L_CHOCH: 3674

      12H:
        local:
          H: 2887
          L: 2763
        major:
          H_MAJOR: 3172
          L_MAJOR: 2625
        zones:
          SELL_1: 3035
          SELL_2: 2963
          BUY_1: 2762
        active:
          H_CHOCH: 2889
        inactive: 
          L_BOS: 3682

      2H:
        major:
          H_MAJOR: 2986
          L_MAJOR: 2763
        zones: {}
        active:
          H_BOS: 2885
        inactive: 
          H_BOS: 2858

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
          SELL_1: 0.04761
          SELL_2: 0.04236
        active:
          L_BOS: 0.04469
        inactive: {}

      1W:
        major:
          H_MAJOR: 0.03812
          L_MAJOR: 0.03198
        poc:
          POC_1: 0.03895
          POC_2: 0.03677
          POC_3: 0.03412
          POC_4: 0.03254
        zones:
          BUY_2: 0.03250
          BUY_1: 0.02964
          SELL_1: 0.04018
          SELL_2: 0.03700
          NEUTRAL: 0.03500
        active:
          L_CHOCH: 0.03804
        inactive: 
          H_MSB: 0.02975

      1D:
        local:
          H: 0.03394
          L: 0.03213
        major:
          H_MAJOR: 0.03442
          L_MAJOR: 0.03090
        zones:
          SELL_1: 0.03467
          NEUTRAL: 0.03327
        active:
          L_FSB: 0.03213
        inactive: 
          L_BOS: 0.03476
```

### ETH/USDT
### **2W (Bi-Weekly – Super-HTF)**

* **Previous (≈30 bars):** Impulsive advance from the monthly base at `1M.major.L_MAJOR` **1389** toward the ATH cluster (`ALL.ath` **4956**, `2W.major.H_MAJOR` **4757**), confirming the earlier `2W.inactive.H_BOS` **2880** and the `1M.active.H_MSB` **4095**. After tagging the ATH area, sellers pushed a corrective leg that slid under `2W.sr.SR_2` **4152** and `2W.sr.SR_3` **3960**, culminating in a **confirmed** `2W.active.L_CHOCH` **3437**. The pullback reached into `1M.zones.BUY_2` **2750** while testing the former `2W.inactive.H_BOS` **2880** from above.
* **Current (last 5):** Retest phase: price oscillates around `2W.sr.SR_4` **2870** / `2W.poc.POC_4` **2640** with attempts to reclaim the broken shelf. Indicators: `2W_ema9` **3478.90**, `2W_ema21` **3328.47**, `2W_ema50` **3000.48**, `2W_ema200` **1786.37** (price **2891.01** sits **below 9/21/50**, above 200). `2W_vwap_month` **3015.69** caps; `2W_vwap_week` **2880.34** is near price. Momentum soft: `2W_RSI` **46.07** (<50; `RSI_MA` **56.22**). Price is attempting to form a fresh swing low (working on a new **2W_L_MAJOR**) inside the broader monthly up-cycle.

---

### **3D (HTF for 12H)**

* **Previous (≈30 bars):** Post-`ALL.ath` **4956** rejection, 3-month bearish consolidation broke down via `3D.active.L_BOS` **3439** on a `3D_bearish_hammer_HVC` with bearish follow-through, driving into `1M.zones.BUY_2` **2750** + prior `2W.inactive.H_BOS` **2880** confluence; local structure established at `3D.major.L_MAJOR` **2624**. Bears kept control beneath `3D.zones.SELL_1` **3672** / `3D.zones.SELL_2` **3247**.
* **Current (last 5):** Price is pinned under the EMA stack: `3D_ema9` **3173.92**, `3D_ema21` **3539.54**, `3D_ema50` **3594.50**, `3D_ema200` **3068.53** with `3D_close` **2891.01**. `3D_vwap_month` **3015.69** / `3D_vwap_week` **2880.34** sandwich price; `3D.poc.POC_4` **2880** is the immediate magnet. Momentum weak: `3D_RSI` **33.45** (bearish). HTF bias remains corrective-to-bearish until `3D.zones.SELL_2` **3247** is reclaimed.

---

### **12H (Primary TTF)**

* **Previous (≈30 bars):** Persistent downtrend from `3D.zones.SELL_1` **3672** with sequences of `12H_bearish_HVCs`; last confirmed `12H.inactive.L_BOS` (per trader note) preceded a capitulation into `3D.major.L_MAJOR` **2624**. A relief rally then printed `12H.active.H_CHOCH` **2889** with a `12H_bullish_engulfing_VC` with volume spike + OBV confirmation and reclaimed `12H_9EMA` + W_VWAP, but remained capped beneath the falling `12H_21EMA` and LVN band `12H.zones.SELL_2` **2963** / `12H.zones.SELL_1` **3035**.
  
* **Current (last 5):** Price **2891.01** sits **above** `12H_9EMA` **2871.61**, **below** `12H_21EMA` **2964.44**; `12H_50EMA` **3223.74**, `12H_ema200` **3670.32** overhead; `V_WAP` **2877.19** supports, `12H_vwap_session` **2903.16** slightly caps, `12H_vwap_month` **3227.90** well above. Momentum muted: `12H_RSI` **42.22** (below 50; `RSI_MA` **35.55** curling up). Local structure: `12H.local.H` **2887**, `12H.local.L` **2763**; demand first at `12H.zones.BUY_1` **2762**.

---

### **2H (Execution & LTF Confirmation)**

* **Previous (≈30 bars):** Counter-trend grind from `3D.major.L_MAJOR` **2624** produced `2H.active.H_BOS` **2885** and a local peak at `2H.major.H_MAJOR` **2986** inside the 12H supply shelf, consistent with a bear-flag look on 12H/3D.
* **Current (last 5):** Price **2891.01** hovers **below** `2H_9EMA` **2900.33**, **above** `2H_21EMA` **2880.79** and `2H_50EMA` **2868.54. `2H_ema200` 3097.03** and `2H_vwap_month` **3225.76** remain far overhead;`2H_vwap_week`**2880.47** offers intraday support;`2H_vwap_session`**2908.18** is near-term resistance. Momentum balanced:`2H_RSI`**53.71** (just >50;`RSI_MA` **58.35**). Net: bounce is fragile into 12H supply.

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

* **Trump vs Fed & data blackout**

  * The 43-day U.S. government shutdown (Oct 1–Nov 12) left **October CPI and the full October jobs report cancelled**, forcing the Fed to head into its Dec 9–10 meeting without a clean read on inflation or unemployment. Officials have described policy as “driving in the fog,” relying on partial September data and surveys.
  * This data gap matters for all risk assets (SP500, BTC/ETH) and safe havens (gold) because it **amplifies the impact of every incoming data point** and Fed communication.

* **Fed split on a December rate cut**

  * The Fed funds range is currently **3.75–4.00%** after an October cut.
  * **Cleveland Fed’s Beth Hammack (Nov 20)** warned that *further cuts risk prolonging above-target inflation and stoking financial-stability risks*, citing easy financial conditions and rich asset prices.
  * **NY Fed’s John Williams (Nov 21)** said there is **room for a “near-term” cut** without jeopardizing the 2% inflation target, pushing market odds of a **December 25 bps cut back up toward ~60–70%**.
  * Net: the **“cut vs no-cut” battle** inside the Fed is now a front-and-center driver of rates, gold and high-beta risk (SP500, BTC).

* **Trump, Powell and Fed independence**

  * **Nov 19:** At a U.S.–Saudi investment forum, Trump said he’d “**love to fire**” Fed Chair Powell and called him “grossly incompetent,” while pressing Treasury Secretary Bessent to speed up the search for Powell’s successor before his term ends in May 2026.
  * Courts have already blocked Trump’s attempt to remove Fed Governor Lisa Cook, but the **rhetorical escalation against Powell and the Board** is raising **Fed-independence risk premium**, supportive for gold and structurally negative for the dollar’s “institutional credibility” narrative.

* **Tariffs: from broad hikes to food rollbacks**

  * **Nov 14:** Trump signed an executive order **cutting tariffs on ~200 food imports** (beef, coffee, bananas, tomatoes, etc.), partially reversing his earlier **10% across-the-board base tariff** regime. This is framed as a response to **public anger over grocery inflation** and affordability, and trade partners (e.g., Australia, Switzerland and several Latin American countries) have welcomed the change.
  * Markets are now **re-pricing medium-term inflation slightly lower** at the margin (bullish bonds, gold-supportive via rate-cut odds), but note that **most non-food tariffs remain in place**, so the broader “Trump-tariff inflation impulse” isn’t gone.

* **AI, tech and Trump’s draft AI order**

  * Last week leaks showed the White House drafting an executive order that would **preempt state-level AI laws** by authorizing federal lawsuits and conditioning funding—essentially giving big AI firms a lighter, national standard.
  * **Nov 21:** Reporting then indicated the order has been **put on hold** after bipartisan backlash over states’ rights and child-safety/job-loss concerns. The result is **regulatory uncertainty for mega-cap AI/tech**, key to the SP500 and to “tech beta” sentiment that often spills into crypto.

* **Market reaction across assets**

  * **Equities / SP500:** The week to Nov 21 was volatile. Nvidia’s blow-out earnings initially sparked an AI-led rally, but **AI-bubble fears and mixed jobs data** triggered a sharp reversal: the SP500 and Nasdaq slid to their lowest closes since early September before **bouncing on Friday** as Williams’ dovish comments lifted December-cut odds.
  * **Crypto:** Bitcoin saw **heavy de-risking**, with prices dropping more than 20% from the October high and printing **seven-month lows**, alongside **record outflows (~$500m+) from BlackRock’s IBIT spot ETF**. Flows signalled **rotation away from speculative crypto exposure** after the Fed’s late-October hawkish tone.
  * **Gold:** Gold **slipped modestly on the week but stayed above $4,000/oz**, notably **more resilient than BTC**. Some flows appear to be rotating from Bitcoin into gold as a “cleaner” macro hedge while the Fed’s path and data blackout remain uncertain.

---

### THIS WEEK

* **U.S. data dump: delayed September reports + surveys**

  * Because of the shutdown, **several September releases arrive together this week**. Focus is on how they rebalance December cut odds:
  * **Tue, Nov 25 (ET)**

    * **08:30** – **September Retail Sales** (delayed).
    * **08:30** – **PPI & Core PPI (September)** (delayed).
    * **09:00** – **S&P CoreLogic Case-Shiller Home Price Index (September)**.
    * **10:00** – **Pending Home Sales (October)**; **Business Inventories (September)**.
    * **10:00** – **Conference Board Consumer Confidence (November)**.
  * **Wed, Nov 26 (ET)**

    * **08:30** – **Weekly Initial Jobless Claims** (week ending Nov 21).
    * **08:30** – **Durable Goods Orders (September)** (delayed).
    * **08:30** – **Q3 2025 GDP (revision)**.
    * **09:45** – **Chicago PMI (November)**.
    * **14:00** – **Fed Beige Book** (qualitative read on activity, inflation and labor).
  * **No major reports** are scheduled for Thursday (markets closed) or Friday (early close).

* **Fed narrative this week**

  * Markets come in pricing a **meaningful probability of a December cut** after Williams’ comments, while Hammack and other hawks warn about financial-stability risks from further easing.
  * The **missing October CPI and full October jobs data** increases the weight on this week’s **September PPI/retail/ durable goods + November confidence/claims**; any upside surprises on inflation or growth can quickly knock back cut odds and hit SP500/BTC, while soft prints should support **gold and duration-sensitive growth assets**.

* **Trump, tariffs & trade**

  * **Food-tariff rollback:** Implementation of the **Nov 14 food-tariff cuts** continues; markets are watching for any early impact on **inflation expectations and consumer-confidence surveys**.
  * **U.S.–EU trade tensions (steel & digital rules):**

    * **Nov 24:** The U.S. told EU ministers it wants **“more balanced” EU digital-platform rules** in exchange for fully implementing the July trade deal that would **cut steep U.S. tariffs on EU steel and aluminium** and ease duties on EU goods like wine and spirits.
    * EU officials fear that with **50% tariffs still on metals and threats of new levies on trucks, critical minerals and clean-tech gear**, the deal could be hollowed out. This keeps a **tail-risk overhang for global industrials and European risk assets**, supportive for defensive flows (USD, gold) on any escalation.
  * **Semiconductor tariffs:** Reporting last week suggested Trump’s plan for **new semiconductor import tariffs may be delayed**, reducing immediate headline risk for chip stocks but keeping the **tech-trade-war narrative alive**, especially relevant for AI-heavy SP500 names and, by proxy, crypto beta.

* **AI policy & tech**

  * The administration’s **draft AI executive order** that would **override state AI regulations** via federal lawsuits and funding threats is **currently paused**, but not dead. Combined with January’s **Executive Order 14179 (“Removing Barriers to American Leadership in AI”)**, this keeps:

    * **Regulatory risk** elevated for big AI platforms (key drivers of SP500).
    * **Narrative support** for AI investment and chip demand, even as markets worry about an **AI-bubble in valuations**.

* **Current macro tone in markets (into today)**

  * **Gold:** Has extended its rebound early this week to around **$4,140/oz**, its highest since mid-November, as traders **ramp December cut odds** and hedge against both inflation uncertainty and political interference with the Fed.
  * **Bitcoin & crypto:** After last week’s crash and record ETF outflows, BTC has **stabilized and bounced modestly** (high-70Ks/80Ks region vs >120K peak in October), but remains in a **fast bear-market dynamic** with volatility elevated and macro-data sensitivity high.
  * **SP500:** Opened Thanksgiving week with a **cautiously bullish tone**, helped by renewed cut bets and bullish 2026 targets from major banks, but **AI-bubble worries and rich valuations** in mega-cap tech limit the upside.
  
### MACRO ANALYSIS

#### BTC & ETH

BTC and ETH sit at the intersection of **macro rates, tech sentiment and liquidity**:

* **Macro link:**

  * The Fed’s **late-October hawkish pivot** triggered a **sharp BTC drawdown**, aided by **record outflows from major spot BTC ETFs** and deleveraging of “AI + crypto” growth baskets.
  * By contrast, **gold held up**, underscoring that **BTC is trading more as a high-beta risk asset than a pure inflation hedge** right now.
  * The bounce after Williams’ dovish comments shows BTC is **highly sensitive to changes in December cut odds**, much like high-duration tech stocks.

* **Cross-asset & correlation:**

  * **Short-term:** BTC/ETH correlate **positively with SP500/Nasdaq** and AI sentiment; risk-on in equities often aligns with crypto bounces.
  * **Versus gold:** When markets fear **policy error + financial-stability risk**, flows can **rotate from BTC into gold**, especially after big crypto drawdowns.
  * With the **U.S.–EU steel/digital spat and AI-EO uncertainty**, any tech-led SP500 wobble can **spill into BTC/ETH** even if crypto-specific news is quiet.

* **Trading implications (today):**

  * Treat BTC/ETH as **leveraged plays on today’s U.S. data and Fed repricing**:

    * **Soft data / dovish narrative** → support for **relief bounces** in BTC/ETH alongside SP500.
    * **Hot data / cut odds drop** → renewed **downside / liquidity air-pockets**, especially given recent ETF outflows.
  * Given the holiday week and recent volatility, **respect reduced depth and whipsaw risk around the 08:30 ET releases**; from a VPA point of view, you want **clear trend volume on breaks** rather than fading noisy spikes.
  
# TRADING PLAN FOR 12H_TTF (Trigger • Location • Context)
## SHORT

### WHITE_A — Short continuation from 12H supply

* **Context:** 12H downtrend intact beneath `12H_21EMA` **2964.44** / `12H_50EMA` **3223.74** with `3D` bearish. Bounce into supply shows **decreasing buy VCs** vs prior sell leg; ETHBTC weekly/daily both soft.
* **Location:** `12H.zones.SELL_2` **2963** → `12H.zones.SELL_1` **3035** (cap), aligned with falling `12H_21EMA`.
* **Trigger:** **`LTF_L_MSB`** after a wick into `2963–3035`, with **bearish CVD** and a **12H/2H absorption HVC** at the LVN edge.
* **Invalidation:** 12H acceptance above `12H.zones.SELL_1` **3035** **and** a `12H_H_MSB` through `12H.major.H_MAJOR` **3172**.
* **Setup Priority:** **A+**

---

### ORANGE_A — Short reversal at 3D key flip

* **Context:** Retest of `3D.active.L_BOS` **3439** from below inside the higher shelf `3D.zones.SELL_2` **3247** → stretch to `3D.zones.SELL_1` **3672**. Expect sellers to defend HTF breakdown with headwinds from ETHBTC.
* **Location:** First touch into `3D.zones.SELL_2` **3247**; stretch fill toward `3D.zones.SELL_1` **3672** if a squeeze.
* **Trigger:** **`TTF_L_MSB` (12H)** printed at location; enter the **first low-volume retest**.
* **Invalidation:** 12H close **above** `3D.zones.SELL_1` **3672** on **ignition SHVC** with rising CVD.
* **Setup Priority:** **A**

---

### PURPLE_A — Aggressive short at 3D supply (fade first, then confirm)

* **Context:** Same zone as `ORANGE_A` but earlier entry using a failure at the tip of the squeeze.
* **Location:** `3D.zones.SELL_2` **3247** → probe toward `3D.zones.SELL_1` **3672**.
* **Trigger:** **`LTF_H_FSB`** (failed breakout) at the edge, **then** `LTF_L_MSB` to confirm. Prefer **bearish RSI/CVD divergence**.
* **Invalidation:** Acceptance back **above** the FSB wick high and `3D.zones.SELL_1` **3672**.
* **Setup Priority:** **A-**

---

### PINK_A — Intraday momentum short (lose supports)

* **Context:** If price **loses** `12H_9EMA` **2871.61** and weekly VWAP support (`V_WAP` **2877.19**) **and** fails to hold above `12H.active.H_CHOCH` **2889**, momentum should rotate down with 3D trend.
* **Location:** Break back below `12H.active.H_CHOCH` **2889** toward `3D.poc.POC_4` **2880** then into `12H.zones.BUY_1` **2762**.
* **Trigger:** **`LTF_L_BOS/MSB`** under **2889** with **ignition HVC** + falling CVD; add on failed retest of 2889/2880.
* **Invalidation:** Reclaim `12H_9EMA` and hold back **above** `12H.active.H_CHOCH` **2889** with bullish CVD.
* **Setup Priority:** **B+**

---

### RED_A — Breakdown & retest beneath the HTF floor

* **Context:** Transition from corrective to distributive if the market takes out the HTF base.
* **Location:** Clean break of `3D.major.L_MAJOR` **2624**. Targets ladder to `2W.poc.POC_4` **2640** (fast), then open air toward `1M.sr.SR_2` **2767**/**1M.poc.POC_1` **2523**.
* **Trigger:** **`12H_L_BOS`** below **2624** with **SHVC** and persistent bearish CVD; **short the retest** of **2624** from below.
* **Invalidation:** Swift reclaim of **2624** with a `12H_H_MSB` and absorption.
* **Setup Priority:** **B**

---

## LONG

### BLUE_A — Fade long at 3D_L_MAJOR sweep

* **Context:** A liquidity **`L_SWEEP`** through `3D.major.L_MAJOR` **2624** into `1M.zones.BUY_2` **2750** / `2W.poc.POC_4` **2640** with **weakening sell VPA** can mark a tradable low.
* **Location:** Wick below `3D.major.L_MAJOR` **2624**, close back above **2624–2640**.
* **Trigger:** `TTF_L_FSB` at the sweep → confirm with **`LTF_H_MSB`**; prefer **RSI/OBV bullish divergence**.
* **Invalidation:** 12H **acceptance below** **2624** (see `RED_A`).
* **Setup Priority:** **B+**

---

### GREEN_A — Break & retest long at the 12H flip

* **Context:** If buyers convert the recent structural pivot, we can ride the bounce to upper LVNs against a still-bearish 3D. Confirmation mandatory.
* **Location:** Break → retest of `12H.active.H_CHOCH` **2889** **and hold above** `12H_9EMA` **2871.61** / `V_WAP` **2877.19**.
* **Trigger:** **`LTF_H_BOS/MSB`** on the retest with rising CVD.
* **Invalidation:** Failure back below **2889** and `12H_9EMA` with bearish MSB.
* **Setup Priority:** **B**

---

### YELLOW_A — Reversal long from 12H demand

* **Context:** Sell-leg extension into demand with **TTF bullish divergence** is a candidate for rotation inside the 3D down-channel.
* **Location:** `12H.zones.BUY_1` **2762** (first base); stretch to a defensive spike near `3D.major.L_MAJOR` **2624**.
* **Trigger:** **`TTF_H_MSB`** after a sweep of **2762** with **decelerating sell VCs** and rising CVD/OBV.
* **Invalidation:** 12H **close below** **2762** or failure after MSB.
* **Setup Priority:** **A-**

---

### TEAL_A — Intraday momentum long on VWAP/CHOCH hold

* **Context:** Risk-on only if price sustains **above** `12H.active.H_CHOCH` **2889**, `V_WAP` **2877.19** and `12H_9EMA` **2871.61**, with ETHBTC **not** making fresh daily lows.
* **Location:** Reclaim and hold **≥2889**; first upside magnets `12H.zones.SELL_2` **2963** then `12H.zones.SELL_1` **3035**.
* **Trigger:** `LTF_H_BOS/MSB` after VWAP/EMA reclaim with **ignition HVC** + rising CVD.
* **Invalidation:** Lose **2889** again and close back under `V_WAP` **2877.19**.
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
- 2W: `HTF = NEUTRAL-BULLISH`.
- `PG` grades are assessed based on the plan full viability. DO NOT DEGRADE the plan based on probability/possibility.  
- DO NOT PERFORM TTI ON the ETH/BTC pairs. 