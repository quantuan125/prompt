# CONTEXT: 
## TRADER CONTEXT: 
This week: Today is 1st of December 2025, we are in London Session, 1 hours until US session. We have ISM Manufacturing PMI 1.5 hours as major macro events/data released today. The start of this month marks the end of Quantitative Tightening cycle from the FED. Refers to `MACRO CONTEXT` for the rest of the macro events this week.  

Last month: We have officially passed October which was supposed to be bullish month for BTC and crypto in terms of seasonality during a bull cycle year, however we got the opposite of that: largest crypto liquidation sell off after sweeping the ATH followed by choppy bearish price actions despite soft CPI + Inflation data print + resolution on China-US tariffs.

Last week: Holiday/short week with soft September PPI released as the market is trying price in a 0.25bps rate cut with >85% odd for December by the FED. 

Directive: Price is bearish across daily and weekly timeframe, short are prioritize however caution due to bearish extension into monthly support/demand zone with oversold signals. 

Sentiment: With price action last month that have liquidated millions of leveraged crypto traders and enact fears, the general consensus is bearish with hypothesis of the top for the cycle is already set for BTC, and the start of an extended bear market into 2026. `Fear & Greed Index` worsen from 30-40 (NEUTRAL) since last month to 14-19 (EXTREME FEAR) last week and improving toward 20-25 (FEAR) this week.    

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
    major:
      H_MAJOR: 116.4
      L_MAJOR: 102.0
    sr:
      SR_1: 108.3
      SR_2: 100.9
      SR_3: 86.1
      SR_4: 80.7
      SR_5: 78.4
    poc:
      POC_1: 108.2
      POC_2: 106.8
      POC_3: 103.4
      POC_4: 101.8
      POC_5: 94.6
      POC_6: 91.4
      POC_7: 87.3
      POC_8: 67.4
    zones:
      SELL_1: 120.5
      SELL_2: 106.1
      SELL_3: 98.4
    active:
      L_BOS: 102.0
    inactive:
      L_MSB: 111.9
      H_FSB: 124.5
      L_FSB: 108.6

  1D:
    local:
      H: 93.1
    major:
      H_MAJOR: 93.2
      L_MAJOR: 80.6
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
      SELL_1: 94.0
    session:
      PDH: 92.0
      PDL: 90.3
    active:
      L_BOS: 88.6
    inactive:
      L_BOS: 98.9

  4H:
    major:
      H_MAJOR: 92.0
      L_MAJOR: 86.1
    sr:
      {}
    poc:
      POC_1: 91.9
      POC_2: 90.0
      POC_3: 86.9
      POC_4: 82.2
    zones:
      SELL_1: 89.4-90.4
      SELL_2: 88.0
      BUY_1: 85.3
    active:
      L_CHOCH: 90.2
    inactive:
      H_BOS: 89.2

  1H:
    H_MAJOR: 86.9
    L_MAJOR: 85.6
    sr: {}
    poc: {}
    zones:
      SELL_1: 86.4
    active:
      L_MSB: 91.0
    inactive:
      H_FSB: 91.6

  15m:
    major:
      H_MAJOR: 87.3
      L_MAJOR: 86.7
    sr: {}
    poc: {}
    zones:
      {}
    active:
      H_CHOCH: 86.9
    inactive: 
      L_BOS: 86.8
```

### **1W (Weekly – Super-HTF Structure)**

**Previous (~30 bars):** After a strong `1M_bullish_channel` into `ALL.ath` → distribution under the ATH band, we printed a sweep at `1W.inactive.H_FSB`, then the capitulation leg drove price below `1M.inactive.H_BOS` with a deep wick `1W_bearish_hammer_HVC`. That move set a fresh range extreme at `1W.major.L_MAJOR` **102.0k**. A rebound into the falling weekly band failed beneath `1W.major.H_MAJOR` **116.4k** (LH) and was followed by a confirmed `1W.active.L_BOS` through the weekly range low.
**Current (~5 bars):** Two consecutive downside weeks, the latest a `1W_bearish_hammer_HVC` into the **monthly support cluster** `1M.poc.POC_4` **84.2k** + `1M.sr.SR_4` **82.5k**, with risk of continuation toward `1M.major.L_MAJOR` **74.5k**. Indicators: **1W_RSI < 50**, **1W_9/21/50EMA** and **1W_W/M_VWAP** are all **above price** → **HTF bias: BEARISH** and “finding a new weekly major” remains in progress.

---

### **1D (Daily – HTF for intraday)**

**Previous (~30 bars):** Rejection under `1W.major.H_MAJOR` **116.4k** started a sustained down-channel capped by the falling `1D_9/21EMA`. The leg accelerated last week with the **confirmed** `1D.active.L_BOS` **88.6k**, printed a series of `1D_bearish_engulfing_VCs`and pushed **through**`1M.zones.BUY_1` **90.0k** toward the **monthly support band** (`1M.poc.POC_4`/`1M.sr.SR_4`). A high-volume `1D_bearish_hammer_HVC`formed near that band with **daily RSI oversold (<25)**, triggering a weak rebound.   
**Current (~5 bars):** The rebound stalled **below**`1D_9EMA`and`W_VWAP`, posted a LL local top at `1D.local.H`**93.1k** under`1D.major.H_MAJOR`**93.2k**, then rolled back over. **1D_RSI ≈32** and **all EMAs (9/21/50/200) > price**;`1D.poc.POC_3`**84.6k** and`1M.poc.POC_4`**84.2k** sit as magnets beneath. Session refs:`1D.session.PDH`**92.0k**,`1D.session.PDL` **90.3k** remain overhead/failed reclaims. **Overall: BEARISH.**

---

### **4H (4-Hour – HTF for 1H)**

**Previous (~30 bars):** Post-flush, price attempted a `4H_expanding_channel` recovery into/under `1D.major.H_MAJOR` **93.2k**, then broke down with a **confirmed** `4H.active.L_CHOCH` **90.2k** on `4H_bearish_engulfing_HVC` + downside CVD, flipping momentum.
**Current (~5 bars):** Price trends below **all** `4H_9/21/50/200EMA` and **below** `W_VWAP`; **4H_RSI ≈27** (approaching oversold). We’re re-testing the **support pocket** at `4H.major.L_MAJOR` **86.1k** into `4H.zones.BUY_1`**85.3k** with downside continuity risk toward`1D.poc.POC_3`**84.6k** /`1M.poc.POC_4`**84.2k**. Overhead supply/magnets:`4H.poc.POC_3`**86.9k**,`4H.zones.SELL_2`**88.0k**, and`4H.zones.SELL_1` **89.4–90.4k**. **Overall: BEARISH.**

---

### **1H (Hourly – TTF)**

**Previous (~30 bars):** A sharp Asia-session selloff initiated the `1H.active.L_MSB` **91.0k** on `1H_bearish_engulfing_SHVC`, driving deeply oversold RSI and confirming with falling CVD. Price bounced weakly to the **descending** `1H_9EMA` + `W_VWAP` and set `1H.major.H_MAJOR` **86.9k**, then slid to `1H.major.L_MAJOR` **85.6k** near `4H.zones.BUY_1`.
**Current (~5 bars):** Structure remains **down**: price **below** `S_VWAP` & `W_VWAP`, and **below** `1H_9/21EMA`; **1H_RSI ≈24** (oversold). Immediate levels: resistance `1H.zones.SELL_1` **86.4k** / `4H.poc.POC_3` **86.9k; supports `4H.major.L_MAJOR`**86.1k** →`4H.zones.BUY_1`**85.3k** →`1D.poc.POC_3`**84.6k** /`1M.poc.POC_4` **84.2k**. 
**Overall: BEARISH; trade from supply until structure flips.**

## MACRO CONTEXT
### LAST WEEK

* **Fed, data blackout & shutdown aftershocks:** A just-ended U.S. government shutdown continued to distort the macro picture. The BEA cancelled the *advance* and *second* Q3 GDP estimates, and key BLS reports (October CPI, October jobs detail, real earnings) were scrapped or folded into later releases, leaving markets with unusually little hard data into year-end. At the same time, the Beige Book and private indicators pointed to cooling labour demand but not a collapse, keeping the “softening but not broken” narrative alive. 
* **Rate-cut odds ramp into December:** Despite the data fog, Fed cut expectations re-accelerated. By mid-week, futures priced roughly an 80–87% chance of another 25 bp cut at the December 10 FOMC meeting, helped by dovish commentary from key Fed voices and a Beige Book pointing to moderating growth. U.S. stocks strung together multiple green sessions, with the S&P 500 and Dow both logging solid weekly gains into month-end. 

* **Thanksgiving week liquidity & risk tone:** U.S. markets were closed on Thursday, November 27 for Thanksgiving, with shortened hours on Black Friday. CME futures and NYSE-listed products ran on holiday schedules, compressing liquidity on Thursday and much of Friday. Despite thinner conditions, Thanksgiving week was one of the strongest in years for the S&P 500 and Dow, historically a constructive seasonal signal. 

* **Gold squeezes higher on December-cut narrative:** After wobbling earlier in November, gold caught a strong bid into month-end as December cut odds surged. Spot prices squeezed back above the 4,100 handle and toward the 4,150–4,170 zone around November 26, helped by a weaker dollar and growing conviction that the Fed will ease again. Major banks lifted medium-term gold targets, with one large house pushing its 2026 forecast toward the mid-4,000s and sketching a path toward 5,000+ in 2027, reinforcing the “structural bull” narrative. 

* **Crypto has a brutal November:** Bitcoin and ether extended their drawdown, with BTC dropping more than 17% in November and trading below 90k by month-end, making it one of the worst months of 2025. U.S. spot bitcoin ETFs saw roughly $3.4–3.5B in net outflows—near record levels—with BlackRock’s flagship ETF taking the heaviest redemptions. ETF AUM fell over 20% month-on-month as price slumped, even as on-chain and positioning data showed some larger players accumulating into the weakness. 

* **Trump vs. the Fed stays front-and-centre:** Politically, last week sat against a backdrop of mounting pressure from President Trump for deeper and faster rate cuts before the December meeting, and a broader campaign to exert more control over the Fed. Recent attempts to reshape the Board (including efforts to remove certain governors and high-profile regional presidents announcing departures) kept markets focused on Fed independence as a risk variable, not just a background principle. 

### THIS WEEK

* **Key U.S. data (all ET) ahead of the December 10 FOMC:**

  * **Mon, Dec 1 – 10:00:** ISM Manufacturing (Nov).
  * **Wed, Dec 3 – 8:15 / 10:00:** ADP Employment (Nov); ISM Services (Nov), plus delayed trade price and industrial production prints.
  * **Fri, Dec 5 – 10:00:** Personal Income & Spending (Sep) including *PCE & core PCE*, the Fed’s preferred inflation gauge, plus preliminary December University of Michigan sentiment and later consumer credit.
    These are “catch-up” releases in a distorted calendar and will be read as key confirmation (or contradiction) of the current dovish pricing for December. 

* **Fed communication & political overhang:**

  * **Powell speaks today,** with markets primed to parse any hint on how he sees the balance between incomplete data, still-elevated inflation, and political pressure for easier policy.
  * Recent analysis flags an unusually high risk of **multiple dissents** at upcoming meetings as several FOMC voters question further cuts, even as governors lean dovish—an unusual split that could unsettle markets if December delivers a 7–5-style vote.
  * In parallel, **Fed independence is under visible political strain:** Trump has repeatedly pushed for steeper cuts and is openly mulling replacements for Powell, with White House adviser Kevin Hassett emerging as a leading candidate and saying he would be “happy to serve” as Fed chair. Markets are increasingly treating Hassett as a de-facto “shadow chair” in the run-up to Powell’s term expiry in 2026. 

* **Global risk-off open & cross-asset tone (Monday):**

  * Asian and European equities are down, **S&P 500 futures** are off around 0.6–0.8%, and the **Nikkei is down nearly 2%** after BOJ Governor Ueda signalled that a rate hike is on the table, lifting JGB yields and pressuring global carry trades.
  * **Crypto is heavy:** bitcoin is down 4–6% on the day, trading in the mid-80k region after shedding about 18k in November, with ether off ~5–6%.
  * **Gold is at a six-week high** above 4,200, silver has tagged fresh records, and the dollar is slightly softer as futures price an ~85–88% chance of a December Fed cut.
  * **Oil is firmer**, with Brent up more than $1 after OPEC+ chose to maintain output constraints into early 2026. 

* **Crypto-specific catalysts:** The November ETF bleed remains a live story—U.S. spot BTC products just logged one of their worst months on record for net flows, and fresh headlines today highlight both continued outflows and a downgrade of Tether by a major ratings agency, adding an extra layer of counterparty and liquidity concern to the crypto complex. Traders will be watching whether ETF flows stabilize or whether further redemptions keep BTC and ETH in “sell-the-bounce” mode. 

* **Tech/AI & equity sentiment:** November closed with the S&P 500 and Dow higher, but the **Nasdaq logged a monthly loss** as investors rotated out of crowded AI leaders—Nvidia in particular—into names like Alphabet, which rallied on enthusiasm over its Gemini AI model. Concerns about stretched AI valuations are now a central part of the equity narrative and are weighing disproportionately on high-beta growth—exactly the part of the S&P most correlated with BTC/ETH. 


  
### MACRO ANALYSIS
Today you’re trading **into a risk-off open** where the market is simultaneously **pricing a high probability of a December Fed cut** and **questioning growth and policy clarity**. That combination tends to favour **gold and high-quality duration** while leaving **equities and crypto as the shock-absorbers** for any negative surprise in ISM or Powell’s tone. Historically, BTC/ETH have traded as high-beta expressions of the same risk cycle that drives the Nasdaq/S&P growth complex, while gold often reacts more cleanly to the *level and credibility* of real yields and Fed independence. With Fed data visibility impaired, Trump’s pressure on the Fed rising, and ETF/flow dynamics dominating crypto, today’s session is about respecting that **macro uncertainty is high**: high-beta assets can move violently both ways around Powell and ISM, but the *default* positioning bias from macro is **long safety (gold, quality) / cautious on high-beta (SPX tech, BTC/ETH)** unless and until the data/communication confirms a benign soft-landing path.

#### BTC & ETH

BTC and ETH head into the U.S. session with **heavy technical and flow baggage**: a double-digit November drawdown, price sitting in the mid-80k / high-2k region, and one of the worst months on record for U.S. spot ETF outflows. That makes crypto particularly sensitive to any macro narrative that reinforces “risk-off + earnings/AI de-rating” in equities. Short term, the correlation with high-beta U.S. stocks and funding conditions remains tight: **weak ISM or a cautious Powell that stresses growth risks over inflation could paradoxically help BTC/ETH** if markets lean toward faster or deeper cuts and equities interpret that as supportive; **a hawkish-or-confused message that questions the December cut or Fed cohesion is more likely to hit crypto first**, especially with Tether and ETF flows already under scrutiny. For discipline: treat BTC/ETH as **macro-beta plus additional idiosyncratic flow risk** today—if S&P futures stay heavy into and after Powell, fading sharp intraday crypto spikes rather than chasing them is consistent with the current macro tape.
  
# TRADING PLAN FOR 1H_TTF (Trigger • Location • Context)
## SHORT
### **WHITE_A — Short continuation from 1H supply → 4H supply**

* **Context:** 1H/4H/1D are **bearish** with price **below** `S_VWAP`/`W_VWAP` and all EMAs; RSI oversold but **no bullish structure**. Expect “sell the rip” into nearest 1H supply as the trend resumes.
* **Location:** `1H.zones.SELL_1` **86.4k** (first tap) → extension toward `4H.zones.SELL_2` **88.0k** if squeeze. Prefer confluence with descending `W_VWAP` and `1H_9EMA`.
* **Trigger:** Liquidity sweep/weak test into the zone **then** **LTF_L_MSB → 1H_L_MSB** with **bearish CVD** and a sell-side **HVC** or clear decreasing-volume pullback followed by downside ignition.
* **Invalidation:** 1H acceptance **above** `4H.zones.SELL_2` **88.0k** **and** `W_VWAP` with rising CVD (trend check).
* **Setup Priority:** **A+**

---

### **ORANGE_A — Short reversal at 4H breakdown retest (CHOCH base)**

* **Context:** Counter-bounce into the prior breakdown area often fails when HTF is bearish. Look for stall at the `4H.active.L_CHOCH` base with **rolling-over 1H_200EMA/MA** overhead acting as dynamic supply.
* **Location:** `4H.active.L_CHOCH` **90.2k** overlapping `4H.zones.SELL_1` **89.4–90.4k** + falling `1H_200EMA/MA`.
* **Trigger:** Failed push into the band (wick-through/close back inside) **then** **LTF_L_MSB → 1H_L_MSB** with **bearish CVD divergence** / sell-side HVC.
* **Invalidation:** 1H close **above** `4H.zones.SELL_1` with CVD expansion (opens room to `1D.zones.SELL_1` **94.0k**).
* **Setup Priority:** **A**

---

### **PURPLE_A — Short fade of 1H range high (failed break)**

* **Context:** Expect range-top fakeouts while trend is down. A sweep of `1H.major.H_MAJOR` that fails is ideal to fade back into the range.
* **Location:** `1H.major.H_MAJOR` **86.9k** with overhead `4H.zones.SELL_2` **88.0k** as extension.
* **Trigger:** **1H_H_FSB** (failed break) at `1H.major.H_MAJOR` → immediate **LTF_L_MSB**; confirm with **rolling CVD** and a bearish VC on the rejection.
* **Invalidation:** 1H acceptance above `1H.major.H_MAJOR` **and** `W_VWAP`.
* **Setup Priority:** **B+**

---

### **PINK_A — Short momentum scalp below VWAP band**

* **Context:** Continuation scalp while price holds **below** `S_VWAP` + `1H_9EMA` and CVD stays heavy.
* **Location:** Any LTF pullback that retests the **VWAP/EMA band** from below while still under `1H.zones.SELL_1` **86.4k**.
* **Trigger:** **LTF_L_BOS or L_MSB** after a shallow, **low-volume** uptick into the band; enter on the retest of the LTF flip.
* **Invalidation:** Reclaim of `S_VWAP` **and** `1H_9/21EMA` with rising CVD.
* **Setup Priority:** **B**

---

### **RED_A — Breakdown through 1H/4H range low**

* **Context:** A decisive expansion lower re-asserts the bearish trend and opens the door to the **monthly support pocket**.
* **Location:** Loss of the **cluster** `4H.major.L_MAJOR` **86.1k** / `1H.major.L_MAJOR` **85.6k** → magnets `1D.poc.POC_3` **84.6k** then `1M.poc.POC_4` **84.2k**.
* **Trigger:** **1H_L_BOS** through the cluster on **strong sell VPA** + negative CVD; sell the **low-volume** retest from below with a **LTF_L_MSB/BOS**.
* **Invalidation:** Swift reclaim back above `1H.major.L_MAJOR` **85.6k** **and** `S_VWAP`.
* **Setup Priority:** **B**

---

## LONG

### **BLUE_A — Long fade on L_FSB at 4H demand (counter-trend)**

* **Context:** Knife-catch only with **stopping/absorption** evidence: capitulatory wick into HTF demand, bullish **CVD divergence**, RSI sub-25 turning up, and sellers failing to push lower.
* **Location:** `4H.zones.BUY_1` **85.3k** around `1H.major.L_MAJOR` **85.6k** with extension toward `1D.poc.POC_3` **84.6k** / `1M.poc.POC_4` **84.2k** if swept.
* **Trigger:** **L_FSB** (sweep of lows) + **15m_H_CHOCH/15m_H_MSB** and reclaim of `S_VWAP`.
* **Invalidation:** 1H close **below** `1M.poc.POC_4` **84.2k** on sell-side HVC.
* **Setup Priority:** **B-** 

---

### **TEAL_A — Long counter-trend scalp on VWAP/EMA reclaim**

* **Context:** With HTF bearish, any long is a **scalp**. We need a firm reclaim of the intraday control band.
* **Location:** Reclaim and hold above `S_VWAP` + `1H_9EMA` while still below `1H.zones.SELL_1` **86.4k**.
* **Trigger:** **15m_H_MSB** on the reclaim, then buy the **low-volume** retest with rising CVD and a bullish VC.
* **Invalidation:** Loss of `S_VWAP` after entry or immediate **1H_L_CHOCH**.
* **Setup Priority:** **B**

---

### **YELLOW_A — Long major reversal from 4H demand (structure flip required)**

* **Context:** For a real bottom, the TTF must flip up **and** hold above the first structural pivot.
* **Location:** From `4H.zones.BUY_1` **85.3k** / `4H.major.L_MAJOR` **86.1k** inside the monthly support band (`1M.poc.POC_4` **84.2k** + `1M.sr.SR_4` **82.5k**).
* **Trigger:** **1H_H_MSB** (trend-death of the 1H downtrend) + **strong bullish VPA**; confirm by **acceptance above** `1H.major.H_MAJOR` **86.9k**.
* **Invalidation:** Failure to hold above `1H.major.H_MAJOR` after flip, or sell-side HVC back into the zone.
* **Setup Priority:** **A-**

---

### **GREEN_A — Long breakout & retest of 1H high**

* **Context:** If sellers fail at the top of the 1H range, a squeeze can run to higher HTF magnets.
* **Location:** Clean break **and retest** of `1H.major.H_MAJOR` **86.9k** while reclaiming `W_VWAP`; upside magnets `4H.zones.SELL_2` **88.0k** → `4H.zones.SELL_1` **89.4–90.4k** → `1D.session.PDH` **92.0k**.
* **Trigger:** **1H_H_BOS + bullish HVC**, then a **low-volume** retest → **15m_H_MSB/BOS** with rising CVD.
* **Invalidation:** Acceptance back **below** `1H.major.H_MAJOR` or immediate **1H_L_CHOCH** after entry.
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
- 4H: `OVERALL-ASSESSMENT = NEUTRAL-BEARISH`
- 1H: `OVERALL-ASSESSMENT = NEUTRAL`
- `PG` grades are assessed based on the plan full viability. DO NOT DEGRADE the plan based on probability/possibility.  