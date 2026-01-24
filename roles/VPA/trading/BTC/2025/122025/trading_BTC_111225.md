# CONTEXT: 
## TRADER CONTEXT: 
This week: Today is 11th of December 2025, we are in London session, 2 hours until US session. We have no major data/macro event released today. Refers to `MACRO CONTEXT` for the rest of the macro events this week.  

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
      H: 92.3
    major:
      H_MAJOR: 94.6
      L_MAJOR: 87.7
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
      BUY_1: 85.9
      BUY_2: 88.1
      NEUTRAL: 91.2
    session:
      PDH: 94.5
      PDL: 91.6
    active:
      H_FSB: 94.2
    inactive:
      L_BOS: 88.6
      H_FSB: 93.2

  4H:
    major:
      H_MAJOR: 94.5
      L_MAJOR: 89.5
    sr:
      {}
    poc:
      POC_1: 92.0
      POC_2: 90.2
      POC_3: 89.7
      POC_4: 87.0
      POC_5: 82.2
    zones:
      SELL_1: 93.2
      NEUTRAL: 91.9
    active:
      L_CHOCH: 91.6
    inactive:
      H_FSB: 93.3
      H_BOS: 92.3

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

### **1W – Super-HTF Structure**

* **Previous (~30 candles):** After a powerful `1M_bullish_channel`, the weekly trend weakened on `1W.inactive.L_MSB` and distributed for ~3 months beneath `ALL.ath` / `1W.major.H_MAJOR`. A low-volume `1W.inactive.H_FSB` into the ATH zone preceded a historic liquidation leg that broke `1M.inactive.H_BOS` and tagged the demand band around `1M.zones.BUY_1` → extended into `1M.poc.POC_4` / `1M.sr.SR_4`. The leg confirmed `1W.active.L_BOS` with a series of `1W_bearish_impulse_VCs`, 1W_9/21EMA bear-cross and RSI/OBV confirmation.
* **Current (~5 candles):** Bounce from `1W.major.L_MAJOR` is struggling below `1W.poc.POC_3` / `1W.poc.POC_2` overhead, with 1W_9EMA < 1W_21EMA and price still under both (bearish posture). 1W_RSI trapped sub-50, M_VWAP below price (macro support), W_VWAP ≈ price. Bias: **NEUTRAL-BEARISH** while price stays capped beneath `1W.sr.SR_2` and the `1W.zones.SELL_2` supply.

---

### **1D – HTF for intraday**

* **Previous (~30 candles):** One-way selloff into monthly support with an absorption `1D_bearish_hammer_HVC` (capitulatory context) and oversold RSI (<25) near `1W.major.L_MAJOR`. From there, price carved a `1D_ascending_wedge` with HLs; repeated rejections at `1D.major.H_MAJOR` + `1D.zones.SELL_2` and the descending 1D_21EMA.
* **Current (~5 candles):** Another test/reject at `1D.active.H_FSB` near the wedge top; roll-over back under `1D.zones.NEUTRAL` toward wedge base. 1D_9EMA < 1D_21EMA (bearish tilt) while price hovers near/above the band; W_VWAP just below price, M_VWAP well below (macro cushion). Session refs: `1D.session.PDH` / `1D.session.PDL`. OBV remains heavy with bearish divergence into `1D.zones.SELL_2`. Bias: **BEARISH inside consolidation** toward the wedge base unless `1D.major.H_MAJOR` is reclaimed.

---

### **4H – HTF for 1H**

* **Previous (~30 candles):** Up-leg from the bounce failed at the 1D range high (`1D.active.H_FSB`) and the descending 4H_200EMA/MA. A second attempt left a LH near `4H.major.H_MAJOR`, then momentum flipped with `4H.active.L_CHOCH` with OBV confirmation, sending price back through `4H.zones.NEUTRAL` toward `4H.major.L_MAJOR` (bottom of the 1D wedge).
* **Current (~5 candles):** Structure remains **NEUTRAL-BEARISH**: price below 4H_9EMA but still above 4H_21/50EMA cluster; 4H_RSI ~50. VWAP stack: price ≥ W_VWAP and ≥ M_VWAP, but rejection risk persists into `4H.zones.NEUTRAL` / `4H.poc.POC_2`. Key magnets/defenses: `4H.poc.POC_3` / `4H.poc.POC_1` above, `4H.poc.POC_4` / `4H.poc.POC_5` below.

---

### **1H – Trading TF (TTF)**

* **Previous (~30 candles):** Post-FOMC downtrend confirmed on `1H.active.L_BOS` with OBV confirmation; liquidity sweep through `4H.major.L_MAJOR` set `1H.major.L_MAJOR`, then a weak pre-market bounce under `1H.zones.SELL_2`.
* **Current (~5 candles):** Consolidation beneath `1H.zones.SELL_2` and the descending S_VWAP + 1H_9EMA; price < 1H_9/21EMA, but > 1H_50/200 (bearish* per VWAP stack: **S_VWAP > price > W_VWAP**). 1H_RSI sub-50 with flat to slightly negative CVD. Active structure: `1H.active.L_BOS` with nearby `1H.major.H_MAJOR` / `1H.zones.SELL_1` overhead and `1H.major.L_MAJOR` below. Bias: **BEARISH tilt**, range-trading inside 1D wedge base.
  
## MACRO CONTEXT

### LAST WEEK

* **US data, shutdown overhang & Fed expectations**

  * Core PCE for September was confirmed around 2.8% YoY in the Dec 5 release, keeping inflation above target but on a slow disinflation path.
  * Because of the long federal shutdown, a cluster of key reports (October jobs, October CPI, parts of retail sales, etc.) remained delayed or consolidated, with November CPI pushed to Dec 18 and the October+November Employment Situation to Dec 16.
  * Alt data (ADP/Chicago Fed estimates) pointed to small net job *losses* in October–November and an unemployment rate drifting around 4.4%, reinforcing expectations that the Fed would cut at the December 9–10 FOMC.

* **Risk assets & US equities**

  * Into the week ending 7 Dec, US indices extended their late-November rebound: S&P 500 and Dow posted modest gains, with the S&P hovering just below its October all-time high and small caps outperforming as traders leaned into an imminent rate-cut cycle.
  * The rally remained heavily AI-led, with large-cap tech and “AI infrastructure” names driving index performance, while breadth improved versus early-November.

* **Gold & real assets**

  * Gold stayed near record territory after a year-to-date rally of roughly 60% and a doubling in under two years, driven by heavy central-bank buying, expectations of Fed easing and ongoing concerns about Trump-era tariffs and Fed independence.
  * Market commentary increasingly framed gold as shifting from pure safe-haven to partly speculative, given strong ETF inflows and persistent retail FOMO at elevated prices.

* **Crypto market backdrop**

  * Early December saw a sharp “December reckoning” in crypto: BTC and broader majors sold off hard, with BTC briefly probing the mid-$80k area, ETF outflows picking up and volatility in crypto-linked equities spilling back into Nasdaq.
  * Structural factors remained supportive (spot ETFs, 2025 US stablecoin legislation, ongoing institutionalisation), but positioning looked washed-out after an October liquidation event and the early-December slide.

* **Structural Trump policy backdrop (carried into this week)**

  * The tariff regime introduced earlier in 2025—additional levies on imports from Canada, Mexico and China—continued to shape global trade, supporting higher goods prices, sustaining demand for real assets (gold, commodities) and keeping trade-related headline risk elevated for risk assets.

### THIS WEEK

* **Fed decision (Dec 9–10) & macro calendar**

  * The FOMC cut rates by 25 bps to 3.50–3.75%, its third consecutive cut and the lowest level in ~3 years, but the meeting was unusually *fractious* with multiple dissents (some wanted no cut, others a 50 bps move).
  * Powell explicitly linked the inflation overshoot to Trump’s import tariffs, calling the effect largely one-off, while still acknowledging inflation is above target and the labour market is weakening and more fragile than headline data suggest.
  * The Fed signalled only a very shallow path of further easing (one more cut pencilled in for 2026) and simultaneously announced a restart of T-bill purchases (~$40bn) as “technical” liquidity management after ending QT, which markets will read as a soft floor under liquidity conditions.
  * Today/tomorrow’s US releases (weekly jobless claims, PPI, retail sales and other second-tier data) are the main macro prints into the weekend, but the *big* numbers loom next week: the rescheduled November jobs/October payrolls (Dec 16) and November CPI (Dec 18).

* **Trump, Fed independence & trade headlines**

  * Trump publicly blasted the Fed for being too cautious, demanded steeper cuts, and openly floated replacing Powell ahead of his May 2026 term end, keeping **Fed independence risk** squarely on the macro radar.
  * On Dec 8 he threatened a new 5% tariff on all Mexican exports over a water-sharing dispute, just as Mexico’s Congress and Senate this week approved steep 2026 tariffs (up to 35–50%) on imports from China and other Asian countries without trade deals, in part seen as aligning with US pressure and the upcoming USMCA review.
  * These moves reinforce a regime of **escalating, multi-sided tariffs and supply-chain reshoring**, which supports gold and real assets, complicates inflation dynamics and adds a geopolitical risk premium to equities and EM FX.

* **Equities & AI complex**

  * US stocks **rallied hard after the Fed**: the S&P 500 gained ~0.7% on Wednesday to close just below record highs, with the Dow up ~1% and small caps (Russell 2000) making new records as traders priced a “hawkish cut” but still a supportive 2026 easing path and possible “Santa rally.”
  * At the same time, the AI story showed cracks: Oracle’s results and guidance underwhelmed, highlighting that massive AI infrastructure spend is not yet translating into proportional profits. That triggered renewed nerves around crowded AI trades and hit AI-sensitive tech and crypto more than the broad S&P.

* **Gold, silver & the BIS ‘double-bubble’ warning**

  * Gold is trading around $4,200/oz, only marginally softer after the Fed cut as the lack of clear forward guidance capped the immediate upside. Silver, by contrast, broke to fresh records above $60/oz on strong industrial demand and supply constraints.
  * The BIS’s December Quarterly Review and follow-up coverage issued a rare **“double bubble”** alert: statistical tests now flag both gold and the S&P 500 as displaying “explosive” price behaviour simultaneously for the first time in 50 years, with gold up ~60% YTD and over 150% since 2022 amid heavy central-bank and retail buying.
  * The message for traders: gold is no longer behaving as a clean hedge — it is part of the same crowded risk regime as US equities.

* **Crypto this week (BTC & ETH)**

  * After a brief rebound, **BTC has slipped back below $90k today**, down roughly 2–3% intraday and ~28% off its October ATH; ETH is underperforming with a ~4% drop, underscoring its higher beta.
  * The latest leg lower is tightly linked to **AI jitters** (Oracle’s earnings miss), a modest risk-off wobble in tech and ongoing digestion of the Fed’s rate path; Standard Chartered, one of the big bulls, has now cut its BTC targets roughly in half, citing waning corporate treasury demand and a heavier reliance on ETF flows.
  * Broader December crypto commentary highlights ETF outflows in early December, the worst month for some BTC ETFs since February, and warns that crypto is still nursing wounds from October’s cross-asset liquidation.
  * On the structural side, US crypto infrastructure continues to mature: 2025 stablecoin legislation is now law, and this week Gemini won CFTC approval to offer on-shore prediction markets, underscoring regulators’ willingness to integrate certain crypto products into the regulated perimeter.

* **Liquidity & holiday tape**

  * We are in the early phase of the year-end liquidity slowdown: research on historical flows shows market depth typically falls from late November into early January, with wider spreads and more gap-risk even in index futures.
  * There are **no US market holidays this week**, but traders are already positioning around the shortened Christmas week (early close on Dec 24) and the clustering of delayed macro data in mid-December, which can amplify moves in a thinner tape.

### MACRO ANALYSIS

Into today’s US session you are trading under a **hawkish-cut + double-bubble + tariff-risk** regime. The Fed has just delivered a 25 bps cut with deep internal splits and incomplete data because of the shutdown, while Powell explicitly pins much of the inflation overshoot on Trump’s tariff shock. At the same time, Trump is threatening fresh tariffs on Mexico and hinting at replacing Powell, and Mexico itself is hiking tariffs on Asian imports — reinforcing a structurally higher-tariff world that supports real assets and keeps inflation and Fed-independence risk alive. In markets, the S&P 500 is pressing all-time highs *together* with gold near record levels, just as the BIS flags “explosive” behaviour in both; BTC/ETH, by contrast, are sagging below $90k and under $3.3k, dragged by AI-sector jitters (Oracle) and more cautious crypto forecasts. Historically, BTC traded as high-beta SPX; now you have an awkward mix where **SPX and gold are in a crowded, bubble-like co-move, while BTC lags but remains tightly tied to AI and Fed-policy narratives.** For today, that means surprises in US PPI/retail sales, fresh Fed headlines, or further AI-earnings shocks can hit all three — SPX, gold and BTC — in the *same* direction rather than diversifying each other, with crypto likely over-reacting intraday in both directions.

#### BTC & ETH

* BTC is trading back below $90k with ETH underperforming, in a tape defined by:

  * lingering damage from October’s cross-asset liquidation and the early-December ETF-driven crypto sell-off,
  * a “cold breeze” from big houses like Standard Chartered cutting BTC targets and emphasising that future upside depends heavily on ETF demand,
  * a Fed path that is supportive in level terms (lower rates, more liquidity) but uncertain in trajectory, and
  * **AI sentiment risk** — Oracle’s earnings and guidance have spooked the AI complex, and BTC is once again trading as a high-beta expression of AI and broader risk appetite.
* Correlation wise: 2025 saw BTC’s medium-term correlation with SPX trend higher, but we are currently in a regime where SPX is near YTD highs while BTC is down on the year — so **directional macro shocks still transmit across, but BTC is much more fragile to negative headlines and less responsive to incremental good news.**
* For today: be ready for asymmetric reactions. A positive equity/AI reaction to the Fed and data may give BTC/ETH only a modest relief rally given positioning and forecast downgrades; a downside surprise in tech or a risk-off shift after the Fed cut could trigger *outsized* further selling in BTC/ETH as weak hands are still in the process of de-levering.
  
# TRADING PLAN FOR 1H_TTF (Trigger • Location • Context)
### SHORT

**Market State:** HTF (1W/1D/4H) and TTF (1H) are broadly **bearish**, with 1H currently a downtrend inside a 1D_ascending_wedge at the lower boundary → **Market State 1: Aligned Trend** for shorts, **Market State 2: Unaligned/Counter-trend** for longs. 

---

## SHORT PLANS

### **WHITE_A – Short continuation at retest of broken 4H/1H support**

* **Context:** 1W/1D/4H/1H are all **bearish**, with the latest impulse down confirmed by `4H.active.L_CHOCH` and `1H.active.L_BOS` around **`4H.active.L_CHOCH` / `1H.active.L_BOS` (91.6k)**. That breakdown shifted the prior 1D_ascending_wedge base into resistance. A pullback into this zone would be the **first clean retest** of the S/R flip, now overlapping `4H.zones.NEUTRAL` (91.9k) and `1H.zones.SELL_1` (91.8k). Expect price to retrace on **lower volume** than the breakdown leg, with 1H price still below a descending W_VWAP and the overhead `1H_200EMA/MA` band (dynamic resistance), and 1H_RSI staying under 50 while CVD remains negative/flat (no real buy aggression). This is a textbook bearish pullback in an aligned trend.

* **Location:** Confluence supply band from **`1H.active.L_BOS` / `4H.active.L_CHOCH` (91.6k)** up into **`1H.zones.SELL_1` (91.8k)** and **`4H.zones.NEUTRAL` (91.9k)**, with descending **W_VWAP** and the overhead **`1H_200EMA/MA`** cluster acting as additional dynamic resistance.

* **Trigger:**

  * Price retests the 91.6–91.9k band and stalls *below* W_VWAP and `1H_200EMA/MA`.
  * Bearish VPA confirmation: `1H_bearish_VC_VC/HVC` rejecting the zone + **falling CVD**.
  * Entry on **LTF realignment short**: a clear **`LTF_L_MSB`** (or `LTF_L_BOS`) after a small LH forms inside the band, ideally followed by a low-volume LTF retest of that MSB/BOS base.

* **Invalidation:** 1H acceptance above the zone: firm 1H close **above `4H.zones.NEUTRAL` and `1H.zones.SELL_1`** with price reclaiming and holding over W_VWAP and `1H_200EMA/MA`, accompanied by a **`1H_H_MSB`** up and rising CVD. That signals potential 1D-wedge reclaim → cancel WHITE_A and reassess for ORANGE_A-style fade higher or long squeezes.

* **Setup Priority:** `A+`

### **ORANGE_A – Short reversal at 1D range high (4H_Sell-1 confluence)**

* **Context:** If price stages a strong short-covering bounce from `1H/4H.major.L_MAJOR` back toward the daily range top, that move will be against the prevailing weekly/daily downtrend and into a heavy supply stack. This zone is defined by `4H.zones.SELL_1` overlapping `1D.major.H_MAJOR`, `1D.zones.SELL_2`, `1D.session.PDH` and the descending 4H_200EMA/MA. Expect 1H_RSI to push toward or above 60 with 1H_CVD stalling/diverging on approach, and 4H/1H volume to taper relative to the prior impulse up.
* **Location:** Confluence band: `4H.zones.SELL_1` → `1D.zones.SELL_2` / `1D.major.H_MAJOR` around the prior `1D.active.H_FSB` and `4H.inactive.H_FSB`.
* **Trigger:** Liquidity sweep or failed breakout above `4H.zones.SELL_1` / `1D.session.PDH` followed by a decisive **`1H_L_MSB`** (TTF structure flipping back down) with **bearish CVD** and a `1H_bearish_VC_HVC` rejecting the zone. Execute on low-volume LTF (15m/5m) retest of the MSB base with `LTF_L_MSB` realigning short.
* **Invalidation:** 1H acceptance and hold above `1D.major.H_MAJOR` with 1H_RSI and CVD trending up and 1H price reclaiming and holding above 4H_200EMA/MA → treat as possible 1D wedge breakout; cancel short bias.
* **Setup Priority:** `A Priority`.

---

### **PINK_A – Short momentum scalp from 1H_SELL_2**

* **Context:** Within the current bear flag beneath HTF supply, a shallow corrective bounce into intraday supply allows a momentum continuation short. Here, `1H.zones.SELL_2` aligns with descending S_VWAP, W_VWAP overhead and the rolling-over `1H_9EMA`. The broader HTF trend is down, and the 1D wedge is currently breaking lower. Expect the bounce into `1H.zones.SELL_2` to occur on **decreasing volume**, with 1H_RSI failing to break back above 50 and LTF CVD flattening or diverging.
* **Location:** `1H.zones.SELL_2` (local supply) with S_VWAP / `1H_9EMA` overhead and `1H.zones.SELL_1` as secondary resistance.
* **Trigger:** Rejection from `1H.zones.SELL_2` while **still below W_VWAP and `1H_9EMA`**, confirmed by **`LTF_L_BOS` or `LTF_L_MSB`** after a small local LH. Look for a `1H_bearish_VC_VC/HVC` rejecting the EMA/VWAP band and CVD turning down.
* **Invalidation:** 1H close above `1H.zones.SELL_2` that converts it into support, with S_VWAP reclaimed and 1H_9/21EMA crossing upward (short-term trend shift).
* **Setup Priority:** `B Priority`.

---

### **RED_A – Short breakdown below 1H/4H_L_MAJOR**

* **Context:** A clean loss of the wedge base transforms the environment into full continuation mode for the larger downtrend. A decisive `1H_L_BOS` through both `1H.major.L_MAJOR` and `4H.major.L_MAJOR` would confirm the failure of 1D wedge support and open the path toward `1D.zones.BUY_1` / deeper monthly demand. Expect the breakdown to occur on strong sell-side VPA (`1H_bearish_VC_HVC` or SHVC) and sharply negative CVD.
* **Location:** Break and retest zone around `1H.major.L_MAJOR` / `4H.major.L_MAJOR`, with `4H.poc.POC_4` and `4H.poc.POC_5` below as magnets and `1D.zones.BUY_1` as ultimate downside target.
* **Trigger:** First, a high-energy **`1H_L_BOS`** closing well below `1H.major.L_MAJOR` / `4H.major.L_MAJOR` with ignition-style volume and CVD. Then, enter on a **low-volume retest from below** with confirming `LTF_L_MSB/BOS` and rejection of the reclaimed level (failure to get back above the BOS base).
* **Invalidation:** 1H acceptance back above `1H.major.L_MAJOR` after the BOS, with price reclaiming S_VWAP and printing a `1H_H_MSB` – that would signal trap/failed breakdown and shift focus to BLUE_A / YELLOW_A long paths instead.
* **Setup Priority:** `B Priority`.

---

## LONG PLANS (Counter-trend / HTF Realign)

### **BLUE_A – Long fade at 1H/4H_L_MAJOR (bottom of 1D_ascending_wedge)**

* **Context:** This is a **counter-trend fade** into the bottom of the 1D_ascending_wedge and major intraday support. `1H.major.L_MAJOR` and `4H.major.L_MAJOR` coincide with the wedge base and sit just above the 1D demand band `1D.zones.BUY_2` → `1D.zones.BUY_1`. After the heavy liquidation down, follow-through has started to slow: expect `1H_RSI` approaching or briefly dipping below the 30 band, local sellers failing to push significantly below `1H/4H.major.L_MAJOR`, and LTF/TTF CVD starting to form HLs against LLs in price (bullish divergence). Bearish VPA should **weaken** (smaller `1H_bearish_VCs`, lower relative volume) on each new probe of the lows.
* **Location:** Primary demand at `1H.major.L_MAJOR` / `4H.major.L_MAJOR`, with extension into `1D.zones.BUY_2`–`1D.zones.BUY_1` if volatility spikes.
* **Trigger:** Liquidity sweep below `1H.major.L_MAJOR` and/or `4H.major.L_MAJOR` that is quickly reclaimed, followed by an **`LTF_H_MSB`** back above the swept low and a `1H_bullish_VC_VC/HVC` showing buyers stepping in. Ideally accompanied by bullish LTF RSI/CVD divergence.
* **Invalidation:** 1H close well **below** `4H.major.L_MAJOR` with strong sell-side volume (ignition SHVC) and no bullish divergence – this suggests transition to the RED_A breakdown scenario; fade is cancelled.
* **Setup Priority:** `B- Priority`.

---

### **TEAL_A – Long counter-trend scalp on reclaim of 1H_SELL_2**

* **Context:** If sellers fail to push price lower and instead 1H starts to reclaim intraday resistance, a short-term counter-trend squeeze can develop. This happens when price reclaims `1H.zones.SELL_2` and holds above S_VWAP and `1H_9EMA`, with 1H_RSI crossing back above 50 and CVD turning up from depressed levels while 4H/1D remain bearish. Objective is a **scalp** into overhead resistance (not a trend change).
* **Location:** Reclaimed resistance at `1H.zones.SELL_2` with S_VWAP and `1H_9EMA` turning from resistance into dynamic support; upside magnets are `1H.zones.SELL_1` and the lower edge of `4H.zones.SELL_1`.
* **Trigger:** Clear 1H close back above `1H.zones.SELL_2` and S_VWAP, followed by a **`LTF_H_BOS` or `LTF_H_MSB`** on a pullback holding that level as support, ideally with a `1H_bullish_VC_VC` confirming demand and rising CVD.
* **Invalidation:** 1H failure pattern where `1H.zones.SELL_2` is lost again after the reclaim (close back below S_VWAP with `LTF_L_MSB`), signalling that the squeeze has failed – revert to short-bias plans.
* **Setup Priority:** `B`.

---

### **YELLOW_A – Long major reversal from 1H/4H_L_MAJOR toward 1D_BUY_1 / monthly demand**

* **Context:** This is the **highest-conviction reversal long**, requiring that the current 1H downtrend fully dies and realigns with higher-timeframe support. It builds from BLUE_A, but here we demand a full **`1H_H_MSB`** (TTF trend change) at or near `1H.major.L_MAJOR` / `4H.major.L_MAJOR`, supported by strong bullish divergence and exhausted sell-side VPA. The move should originate from the general area of monthly support: `1M.zones.BUY_1` with extension toward `1D.zones.BUY_1`, where weekly/daily structure and LVNs overlap. Expect a stopping `1H_bearish_to_bullish_VC_SHVC` or strong absorption SHVC, sharp CVD reversal, and 1H_RSI lifting from oversold into a sustained up-slope.
* **Location:** Structural base around `1H.major.L_MAJOR` / `4H.major.L_MAJOR` / `1D.major.L_MAJOR`, inside the broader `1M.zones.BUY_1` + `1M.poc.POC_4` demand cluster, targeting first `1D.zones.NEUTRAL` then `1D.zones.SELL_2`/`1D.major.H_MAJOR`.
* **Trigger:** A decisive **`1H_H_MSB`** off the lows (break of prior 1H LH), followed by a *low-volume* pullback to the MSB S/R flip zone where an `LTF_H_MSB` prints with supportive CVD and a `1H_bullish_VC_HVC` or strong VC confirming demand.
* **Invalidation:** Failure of the MSB structure – i.e., a new `1H_L_BOS` that undercuts the MSB origin low, or heavy sell-side SHVC into the same zone – would invalidate the reversal thesis and re-activate RED_A bearish continuation.
* **Setup Priority:** `A`.
  
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

