# CONTEXT: 
## TRADER CONTEXT: 
This week: Today is 3rd of December 2025, we are in London Session, 2.5 hours until US session. We have ISM Service PMI in 1.5 hours as major macro events/data released today. The start of this month marks the end of Quantitative Tightening cycle from the FED. Refers to `MACRO CONTEXT` for the rest of the macro events this week.  

Last month: We have officially passed October which was supposed to be bullish month for BTC and crypto in terms of seasonality during a bull cycle year, however we got the opposite of that: largest crypto liquidation sell off after sweeping the ATH followed by choppy bearish price actions despite soft CPI + Inflation data print + resolution on China-US tariffs.

Last week: Holiday/short week with soft September PPI released as the market is trying price in a 25bps rate cut with >85% odd for December by the FED. 

Directive: Price is bearish across daily and weekly timeframe, short are prioritize however caution due to bearish extension into monthly support/demand zone with oversold signals. 

Sentiment: With price action last month that have liquidated millions of leveraged crypto traders and enact fears, the general consensus is bearish with hypothesis of the top for the cycle is already set for BTC, and the start of an extended bear market into 2026. `Fear & Greed Index` worsen from 30-40 (NEUTRAL) since last month to 14-19 (EXTREME FEAR) last week and improving toward 25-29 (FEAR) this week as price temporarily stall on the weekly downtrend.   

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
      L_MAJOR: 102.0
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
      H: 93.1
      L: 83.9
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
      SELL_1: 98.5
      SELL_2: 94.0
      BUY_1: 83.5
      NEUTRAL: 87.0
    session:
      PDH: 92.3
      PDL: 86.2
    active:
      L_BOS: 88.6
    inactive:
      L_BOS: 98.9

  4H:
    major:
      H_MAJOR: 94.0
      L_MAJOR: 86.1
    sr:
      {}
    poc:
      POC_1: 91.9
      POC_2: 90.0
      POC_3: 86.9
      POC_4: 82.2
    zones:
      BUY_2: 87.7-89.5
      BUY_1: 85.3
    active:
      H_CHOCH: 86.9
    inactive:
      H_BOS: 89.2
      L_CHOCH: 90.2

  1H:
    major:
      H_MAJOR: 93.7
      L_MAJOR: 91.7
    sr: {}
    poc: {}
    zones:
      BUY_1: 91.5
      BUY_2: 92.3
      SELL_1: 93.2
      NEUTRAL: 92.7
    active:
      L_MSB: 92.7
    inactive:
      H_FSB: 93.4
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

### **1W — Super-HTF Structure**

* **Previous (~30 candles):** After a strong `1M_bullish_channel` since late ’24, the weekly trend **weakened** with a confirmed `1W.inactive.L_MSB`. A low-volume `1W.inactive.H_FSB` probed into **ATH** `ALL.ath` / `1M.major.H_MAJOR`, then a “capitulation-style” selloff drove a **confirmed** `1W.active.L_BOS` (trend-continuation down) below `1W.major.L_MAJOR` and under the broken `1M.inactive.H_BOS`. Several `1W_bearish_VCs` printed with spike volume, alongside a 1W_9/21EMA bearish crossover and OBV/RSI confirmation. Price fell out of the `1M_ascending_channel` and the rising weekly support band (`1W_50EMA/MA`) toward **monthly demand** `1M.zones.BUY_1` and deep into `1M.poc.POC_4` / `1M.sr.SR_4`, threatening a slide toward `1M.major.L_MAJOR`.
* **Current (~5 candles):** A **stall/bounce** just above `1M.zones.BUY_1` lifted price back toward the weekly HVN/POC band (`1W.poc.POC_3` → `1W.poc.POC_2`). Trend signals remain **bearish**: price is **below** `1W_9/21EMA/50EMA` (CSV: 1W_9/21/50 all above price) and `1W_RSI` ≈ **40** is **below** its `1W_RSI-MA`. Overhead supply sits at `1W.zones.SELL_2` and `1W.sr.SR_1`; downside magnets are `1W.sr.SR_3` / `1W.poc.POC_4`. Weekly bias: **bearish**, attempting to base above `1M.zones.BUY_1`.

---

### **1D — HTF for intraday**

* **Previous (~30 candles):** Persistent downtrend capped by a descending `1D_9/21EMA`, with the latest `1D.active.L_BOS` pushing into the monthly demand. A **climactic** `1D_bearish_hammer_HVC` (stopping/absorption tone) printed around `1D.major.L_MAJOR` with **oversold** RSI (<25) — first since February — and OBV confirmation. Price based above `1D.local.L`.
* **Current (~5 candles):** Recovery leg on **lighter** volume (vs. the sell leg) lifted back to `1D.major.H_MAJOR` / test of `1D.zones.SELL_2`. Today rides above `1D_9EMA` and into the **descending** `1D_21EMA` (CSV: price > 1D_9; ≈ `1D_21`), while `1D_RSI` ≈ **46** is still **below 50** (trend pressure not yet flipped). Price is possibly establishing a `1D_ascending_wedge` with HLs and horizontal resistance at 1D range high. Session marks: `1D.session.PDH` **92.3** and `1D.session.PDL` **86.2**. Above sits `1D.zones.SELL_2` **94.0** then `1D.zones.SELL_1` **98.5** / `1D.poc.POC_2` **95.7**; below the **mid** is `1D.zones.NEUTRAL` **87.0** with `1D.poc.POC_3` **84.6**. Daily bias: **bearish*** (rally into supply).

---

### **4H — HTF for 1H**

* **Previous (~30 candles):** From the 1D range low, price formed a higher low at `1D.local.L` / `4H.major.L_MAJOR`, then ignited upward with `4H_bullish_engulfing_HVC` and OBV confirmation, flipping structure with a **confirmed** `4H.active.H_CHOCH`.
* **Current (~5 candles):** Price is pressing the **HTF lid**: `4H.major.H_MAJOR` **92.0** → `1D.major.H_MAJOR` **93.2** with supply immediately above at `1D.zones.SELL_2` **94.0** and the **descending** `4H_200EMA/MA` overhead (CSV: 4H_200EMA ≈ mid-95k > price). ST trend is **up** (price above `4H_9/21/50` and `4H_RSI` > 60), but we’re advancing **into** HTF resistance. Key supports: `4H.poc.POC_1` **91.9**, `4H.poc.POC_2` **90.0**, `4H.zones.BUY_2` **87.7–89.5**. 4H bias: **neutral-bullish into resistance**.

---

### **1H — TTF**

* **Previous (~30 candles):** Strong impulsive advance from `1H.major.L_MAJOR` **90.7** into `1D` range high, with `1H_bullish_VC` sequences and **CVD/OBV** confirmation. A clean `1H.active.H_BOS` established `1H.major.H_MAJOR` **94.0** overhead.
* **Current (~5 candles):** Price is consolidating beneath `1D.major.H_MAJOR` **93.2** / inside `1D.zones.SELL_2` **94.0** after the run. It’s **above** `S_VWAP` (CSV 1H_S_VWAP ≈ 89.3) and `1H_9/21/50/200` (all below price). However, **RSI is elevated** (~74) and showing **bearish divergence risk** against the last push into the 1D range high (chart). Local map: `1H.local.H` **93.4**, `1H.local.L` **92.7**, demand band at `1H.zones.BUY_2` **92.3** and deeper `1H.zones.BUY_1` **91.5** above `1H.major.L_MAJOR` **90.7**. TTF bias: **bullish, stretched into HTF supply**.
---

## MACRO CONTEXT
### LAST WEEK

* **Risk assets & gold staged a post-selloff rebound:** Global equities recovered with the S&P 500 pushing back toward the mid-6800s (futures/index level used in that source) and gold reclaiming the ~$4,100 area, while the dollar eased. Bitcoin also bounced back toward the $90k zone after the November liquidation shock, helping reset risk sentiment into month-end.
* **Fed cut odds surged on dovish rhetoric and softer data:** Mixed U.S. data (retail sales, PPI, jobless claims, industrial output) plus dovish comments from key Fed officials (Waller, Williams) pushed market-implied odds of a **Dec 9–10 Fed rate cut** into the ~75–80% range. The backdrop is complicated by missing October CPI and jobs data (after the long shutdown), meaning the Fed heads into the final meeting of the year with a “data visibility gap.”
* **Trump’s tariff regime stayed a key macro overhang:** The U.S. remained in a high-tariff environment (10–60% broad import tariffs plus sectoral surcharges), even after early-November tweaks that trimmed some China-focused “fentanyl” tariffs back to 10%. Corporates and regional Fed surveys continued to flag tariffs as a drag on margins and capex, reinforcing stagflation-style risks (higher costs, softer activity).
* **Crypto: brutal November, but late-month ETF stabilization:** By Nov 21, BTC was down roughly **31% from its $126k ATH** and ETH ~35% off recent highs amid >$1.3T in lost crypto market cap, driven by rising global yields, Fed uncertainty and AI-equity weakness. Spot BTC ETFs saw about **$3.5B in net outflows** and ETH spot ETFs about **$1.4B** in November, but the final days of the month flipped to a modest **+$70M net inflow** and BTC held the mid-$80k area, hinting at seller exhaustion rather than full-on capitulation.
* **Holiday & microstructure noise:** U.S. Thanksgiving (Thu **Nov 27**) fully closed NYSE/Nasdaq with a shortened **Black Friday (Nov 28)** session, keeping liquidity thin. On top of that, a cooling issue at a key data center forced a temporary trading halt across many CME markets on Nov 28, adding execution risk and irregular order-book conditions into month-end futures trading.

---

### THIS WEEK

* **Heavy U.S. data slate (all times ET):**

  * **Mon Dec 1:** S&P Global & ISM Manufacturing PMIs, plus a key **Powell speech** that helped frame the 2026 rate-cut path.
  * **Tue Dec 2:** **Eurozone CPI (Nov)** and **U.S. JOLTS job openings** – both critical for global inflation and labor-tightness narratives.
  * **Today Wed Dec 3:** **ADP employment**, **S&P Global Services PMI**, **ISM Services PMI & prices**, and **crude oil inventories** – a dense cluster that can reprice growth and inflation expectations intraday.
  * **Thu Dec 4:** **Initial jobless claims** – early read on any labor-market cooling.
  * **Fri Dec 5:** **Core PCE (MoM & YoY)** – the Fed’s preferred inflation gauge and arguably the single most important print heading into the Dec 9–10 FOMC.
* **Fed: final 2025 meeting, high cut odds, and independence risk:**

  * Markets are pricing **~80% odds of a 25 bp cut on Dec 9–10**, but FOMC members are visibly split, and the committee must make this call **without October CPI** due to the earlier shutdown.
  * Trump has openly pressured the Fed (including the attempted removal of Governor Lisa Cook) and is now signalling he will **name a new Fed chair in early 2026** as Powell’s term ends, with candidates skewing more dovish on rates. This raises headline risk around Fed independence and the path of future easing.
  * Reuters and others flag a likely **wave of dissents** at upcoming meetings as regional presidents and governors diverge on how fast to cut – a political as well as market risk.
* **Trump, tariffs & courts: legal and policy volatility:**

  * The emergency-tariff regime introduced earlier this year under IEEPA (10–60% tariffs on most trading partners) is now being **formally challenged**: Costco filed a large lawsuit on **Nov 28**, seeking a full refund of duties and arguing the tariffs are unlawful. The Supreme Court is already reviewing the underlying authority and several justices have signalled skepticism.
  * A ruling (likely by mid-2026, but oral arguments and interim orders can land earlier) could either **entrench high tariffs** (inflationary, supportive for gold, negative for global growth) or **force partial unwinds** (disinflationary, supportive for risk assets but potentially USD-negative). Headlines around this case can move USD, rates, and equities.
* **Tech / AI complex and equity leadership:**

  * Last week’s **6–9% drops in Nvidia and AMD** after reports that Meta may buy Google’s AI chips crystallised concerns that AI capex may spread beyond the current chip leaders. Given the “Magnificent Seven” still hold ~30% of S&P 500 weight, AI-chip sentiment remains a primary driver of index-level risk.
  * This week continues to see **AI/semiconductor rotation**, with some flows into defensives and value as traders reassess how much of the AI story is already priced in. Macro data that affects real yields (PMIs, labor, PCE) will feed directly into the discount rate applied to high-duration tech.
* **Crypto vs gold vs bonds – early-December cross-asset reset:**

  * A **BoJ rate hike and global bond sell-off** at the start of the week triggered another leg lower in Treasuries and crypto, while **gold spiked to a six-week high** on safe-haven demand as Fed-cut bets remained elevated.
  * As of the last 24–48 hours, commentaries highlight **silver and Bitcoin rebounding**, oil softening on oversupply fears, and continued focus on whether ETF flows stay mildly positive into December as liquidity thins.
* **Seasonality & liquidity:**

  * The U.S. just exited the Thanksgiving travel/holiday window with record airport passenger counts, confirming strong nominal demand but also signalling that a lot of discretionary activity was pulled into the last 10 days.
  * There are **no U.S. market holidays this week**; however, we’re entering the period where **funds start locking in YTD performance**, VAR limits tighten, and depth in futures/ETFs gradually thins into Christmas. That means macro surprises (today’s services data, Friday’s PCE, next week’s FOMC) can trigger **outsized moves on smaller flow**.

---

### MACRO ANALYSIS

The cross-asset message into today’s U.S. session is “soft landing, but fragile”: a cooling labour market (negative ADP), delayed but still-elevated inflation (Friday’s PCE), and a deeply split Fed heading into a likely December cut. That combination keeps U.S. yields and the dollar biased lower, which is supportive for both gold and crypto, while also backstopping risk appetite in the S&P 500—especially AI/tech. At the same time, Fed independence worries, Trump-era political pressure on the central bank, and BoE warnings about an AI-driven equity bubble create tail-risk scenarios where a hawkish shock (hot PCE or hawkish Fed language) could hit equities and BTC together, with gold acting as the primary safety valve. For today, the ADP miss leans dovish and should keep the base case as: gold supported on dips, BTC trading like high-beta risk tied to ETF flows and Fed expectations, and the S&P 500 attempting to hold its AI-driven rebound while watching PCE and the looming FOMC very closely.

#### BTC & ETH

BTC and ETH enter today’s U.S. session in **post-crash repair mode**: November’s 30–35% drawdown, massive forced liquidations and **multi-billion-dollar ETF outflows** have flushed leverage, but also proved that **spot ETFs now set the marginal price**. Late-month flows flipping slightly positive and BTC holding the mid-$80k region suggest **seller exhaustion**, not macro resolution. Crypto is trading as **high-beta equity / AI-beta**, not as an inflation hedge: when semis and growth stocks sold off on AI-chip competition, BTC and ETH followed; when Fed cut odds rose and yields backed off, crypto bounced with tech. For today, **ADP + ISM Services + rates** are the main risk: a “Goldilocks” combo (modest growth, easing inflation pressures) likely supports a **rotation back into high-beta risk**, which is constructive for BTC/ETH alongside S&P. Conversely, a hawkish surprise (strong labor + sticky services inflation) can easily re-ignite ETF outflows and push BTC back toward the lower end of its November range. In other words: **treat crypto as leveraged SPX/Nasdaq exposure with extra sensitivity to Fed and ETF headlines.**
  
# TRADING PLAN FOR 1H_TTF (Trigger • Location • Context)
## SHORT
### **ORANGE_A — Short reversal at 1D range high / 1D_SELL_2**

* **Context:** 1H up-leg is extended into HTF supply with **elevated RSI** and tiring VPA. Watch for weakening push and **bearish RSI/CVD divergence** as price tests `1D.major.H_MAJOR` **93.2** → `1D.zones.SELL_2` **94.0** beneath a **descending** `4H_200EMA/MA`.
* **Location:** `1D.major.H_MAJOR` **93.2** → `1D.zones.SELL_2` **94.0** with `4H_200EMA/MA` overhead; magnet below at `4H.poc.POC_1` **91.9**.
* **Trigger:** **TTF_L_MSB** (15m/1H) after a wick/sweep of `1D.major.H_MAJOR` / `1D.zones.SELL_2`; confirm with **bearish HVC** or CVD roll-over.
* **Invalidation:** 1H acceptance **above** `1H.major.H_MAJOR` **94.0** that holds; strong bullish HVC through `1D.zones.SELL_2`.
* **Setup Priority:** **A**

---

### **PURPLE_A — Short fade of 1H local high (H_FSB)**

* **Context:** Intraday range scalp: expect **failed break** around `1H.local.H` as momentum stalls under the 1D lid.
* **Location:** `1H.local.H` **93.4** with overhead probe toward `1H.major.H_MAJOR` **94.0** (wick risk).
* **Trigger:** **TTF_H_FSB** (liquidity grab above `1H.local.H`), then **LTF_L_MSB** to rotate down.
* **Invalidation:** 1H close and hold **above** `1H.major.H_MAJOR` **94.0**.
* **Setup Priority:** **B+**

---

### **PINK_A — Short momentum if trend slips below ST baselines**

* **Context:** Counter-trend scalp only if the intraday mean fails.
* **Location:** Below **both** `S_VWAP` and `1H_9EMA` (CSV: S_VWAP ≈ 89.3; 1H_9EMA ≈ 90.9), targeting `1H.local.L` **92.7** → `1H.zones.BUY_1` **91.5** / `1H.major.L_MAJOR` **90.7**.
* **Trigger:** **1H_L_CHOCH** below `1H.local.L` **92.7**, then **LTF_L_BOS/MSB** on the retest with **bearish EMA 9/21 cross-down** on LTF.
* **Invalidation:** Fast reclaim of `S_VWAP` + `1H_9EMA` with HL sequence restored.
* **Setup Priority:** **B**

---

### **RED_A — Short breakdown of 1H/4H major lows**

* **Context:** If structure truly fails, we realign with the weekly/daily downtrend.
* **Location:** Loss of `1H.major.L_MAJOR` **90.7** opens `4H.poc.POC_2` **90.0** then `4H.major.L_MAJOR` **86.1** / `4H.poc.POC_3` **86.9**.
* **Trigger:** **1H_L_BOS** through `1H.major.L_MAJOR` with **sell-side HVC** and falling CVD; sell the **low-volume retest** (LTF_L_MSB/BOS).
* **Invalidation:** Swift reclaim **back above** `1H.major.L_MAJOR` and `S_VWAP`.
* **Setup Priority:** **B**

---

## LONG

### **WHITE_A — Long continuation on pullback to broken 1H_H_BOS / demand**

* **Context:** Ride the intraday trend **only** on clean pullbacks with confirming flow.
* **Location:** `1H.zones.BUY_2` **92.3** at the **broken** `1H.active.H_BOS` (**92.3**). First support is `1H.local.L` **92.7**; deeper add is `1H.zones.BUY_1` **91.5**.
* **Trigger:** **LTF_H_MSB** + sustained **reclaim of S_VWAP**; prefer **decreasing pullback volume** vs. prior impulse.
* **Invalidation:** 1H close below `1H.zones.BUY_1` **91.5** or failure to hold `S_VWAP`.
* **Setup Priority:** **A+**

### **BLUE_A — Long fade at 1H range low (L_FSB)**

* **Context:** Range-fade with bullish bias while 1H trend holds.
* **Location:** `1H.zones.BUY_1` **91.5** → extension sweep into `1H.major.L_MAJOR` **90.7**.
* **Trigger:** Liquidity sweep → **TTF_H_CHOCH / LTF_H_MSB** with **bullish RSI/CVD divergence**; reclaim `S_VWAP` to confirm.
* **Invalidation:** Acceptance below `1H.major.L_MAJOR` **90.7** (hand off to **RED_A**).
* **Setup Priority:** **B+**

---

### **TEAL_A — Long momentum while above intraday baselines**

* **Context:** Continuation scalp if price **holds above** `S_VWAP` + `1H_9EMA` and local HLs persist.
* **Location:** Over `S_VWAP` / `1H_9EMA`, targeting `1H.local.H` **93.4** → `1H.major.H_MAJOR` **94.0**.
* **Trigger:** **LTF_H_BOS/MSB** on the shallow retest, with rising CVD and a series of **bullish VCs**.
* **Invalidation:** 1H close back **below** `S_VWAP`.
* **Setup Priority:** **B**

---

### **YELLOW_A — Long major reversal at deep HTF demand**

* **Context:** If the market flushes, fade the extreme only at strong HTF demand.
* **Location:** `4H.zones.BUY_2` **87.7–89.5** + `1D.zones.NEUTRAL` **87.0**, sitting just beneath `1M.zones.BUY_1` **90.0**.
* **Trigger:** **TTF_H_MSB** after a sharp stop-run / **absorption SHVC**; confirm with bullish divergence.
* **Invalidation:** 1H acceptance below `4H.zones.BUY_2` (trend-resumption down).
* **Setup Priority:** **A-**

---

### **GREEN_A — Long breakout & retest**

* **Context:** If buyers **overrun** the 1D lid, we can play continuation with tight risk.
* **Location:** Clean break above `1H.major.H_MAJOR` **94.0** (which also pressures `1D.zones.SELL_2` **94.0**).
* **Trigger:** **1H_H_BOS** on **buy-side HVC**, then a **low-volume retest** → **LTF_H_MSB/BOS** with rising CVD.
* **Invalidation:** Failure retest (acceptance back **below** 94.0) or immediate **1H_L_CHOCH** post-entry.
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




# TRADER:
We are currently 1 hour into US session. We got the major data released for today outlined in MACRO CONTEXT

# MACRO CONTEXT
### 1. What just dropped today (3 Dec 2025, US session focus)

**ISM Services PMI – November (released today)**
Official ISM Services PMI (aka Non-Manufacturing) came in at **52.6 vs 52.4 in October**, ninth expansion month this year and slightly above its 12-month average (51.7).

Key internals:

* **Business Activity:** 54.5 (54.3 prior) – activity still solidly expanding.
* **New Orders:** 52.9 (down from 56.2) – still expansion, but clear cooling in forward demand.
* **Employment:** 48.9 (up from 48.2) – *still contracting*, but the slowest contraction since May; labour demand is soft but not collapsing.
* **Prices Paid:** 65.4 (down from 70.0, but >60 for 12th straight month) – **inflation pressure is easing at the margin but still hot**.
* **Supplier Deliveries:** 54.1 – slower deliveries, with ISM linking this partly to **tariffs + shutdown-related customs delays and logistics disruption**.
* **Backlog of Orders:** 49.1, up sharply from 40.8 – backlog still technically contracting but improving, hinting at a possible early recovery phase in services demand.

Big picture: **services = modest expansion**, but with **soft jobs and sticky prices**; manufacturing (in the same table) is still in contraction with a **Manufacturing PMI of 48.2**.

---

**S&P Global US Services PMI – November (final)**

* S&P Global’s separate survey shows **US Services PMI at 54.1 vs 55 expected**, Composite PMI 54.2 – still healthy expansion, but a bit softer than flash estimates.

This broadly *confirms* ISM: services are growing, but not roaring.

---

**ADP Private Payrolls – November (also today)**

* **ADP private payrolls: –32,000 jobs vs +10k expected**, after +47k in October (revised). That’s the **third decline in four months** and a clear surprise to the downside.
* ADP + commentary flag **tariffs and uncertainty** as reasons firms are in “no hire, no fire” paralysis.

This is *labour-market softening* right into the Fed meeting, while we still don’t have the official BLS report because of the shutdown delays.

---

**Rates, Fed odds, USD & risk tone**

* 10-year UST yield: ~**4.06%**, 2-year ~**3.49%**, both **down a few bps today** after the weak ADP print.
* Fed funds futures now price roughly an **85–90% chance of a 25 bps cut at the Dec 9–10 FOMC**.
* The **dollar index is on a multi-day losing streak**, with EUR and JPY firmer as markets lean into a dovish Fed path.
* Equities: US futures and cash indices are **up modestly**, with S&P 500 hovering just below its record as markets bet on “soft landing + cuts”. 

**Fed politics / Trump angle**

* Markets increasingly expect **Kevin Hassett** (Trump economic adviser) to replace Powell next year; he’s seen as more dovish and aligned with Trump’s growth agenda. 
* Minutes from the last Fed meeting show **“many” officials thought a December cut was “not appropriate”**, so there’s visible internal tension between political pressure and inflation still near ~3%.

**Gold & Crypto levels / flows context**

* **Gold:** Spot trading **around $4,200/oz**, supported by falling real yields, weak USD and rate-cut bets. 
* **Bitcoin:** Rebounded from sub-$85k earlier this week to **back above $90k, low–mid $90k range**, improving risk sentiment and lifting crypto-linked equities. 
* Structural: central banks and large allocators **still favor gold over BTC as the primary reserve / collateral asset**, despite ETF-driven crypto adoption. 

---

### 2. Macro takeaways – what this actually *means*

**Growth:**

* The US economy is **services-led and still expanding**, but both ISM and S&P PMI show a **slow, grinding growth phase**, not a boom. 
* Manufacturing is in **prolonged contraction**, tariffs and the shutdown have hurt trade and logistics, and the labour market is **clearly cooling** (ADP). 

**Inflation:**

* Services **prices index at 65.4** tells you inflation pressure is **still present**, but the drop from 70.0 is a step in the right direction.
* Markets are basically betting on **“disinflation with no hard landing”** – that’s the narrative powering both S&P and the simultaneous rally in gold *and* BTC.

**Policy:**

* With **soft jobs + modest services + contracting manufacturing + shutdown hangover**, the **path of least resistance is a December cut** – and maybe more into 2026 if data stay weak. 
* But because prices are still hot and Fed minutes show pushback, there is real risk of:

  > **Hawkish surprise / slower easing → yields spike → hit S&P & BTC, initially boost USD, pressure gold short term.**

**Political overlay (Trump & Fed):**

* Market is pricing a **more politically aligned, dovish Fed chair (Hassett)** under Trump, which reinforces the longer-term **“easier money / weaker USD”** bias. 
* Tariffs and shutdown effects are **directly mentioned** in ISM as drags on supply chains and costs – that’s the structural macro regime we’re trading in. 

---

# TECHNICAL 

4H: Price put in a confirmed new `4H.major.H_MAJOR` at 94k at the top of the 1D range high after stalling with multiple small body long upper wicks candles land now currently seem to be rolling over with the developing `4H_bearish_spinning-bar_VC` with volume spike into US session at this location. 

1H: Price retested WHITE_A PEZ first time and rallied but produced a `1H.inactive.H_FSB` ath 1H range high to established a fresh `1H.major.H_MAJOR` followed by a `1H.active.L_MSB`  into US session through a single 1H_bearish_spinning-bar-large-body_HVC, pushing price below 1H_9EMA + S_VWAP. Price is now trying to hold the WHITE_A PEZ the second time confluenced with the ascending 1H_21EMA and now currently under an even tighter range between its major structure with `1H.zones.NEUTRAL` as mid range level

15m: 15m_H_FSB into US session opening and now dropped back inside the 1H range and retesting the broken 1H_L_MAJOR/1H_L_MSB/1H_NEUTRAL level from underneath. 

# COMMENT 1:
Please rerun the SPP for all the relevant plans which includes the following:
- PINK_A: trade the retest of the 1H_L_MSB level. SL at LTF structure above retest level
- PURLE_A (active): Trade the pullback to the prior 1H_H_FSB. SL at 1H_H_MAJOR
- WHITE_A 
- BLUE_A
- RED_A: Wait for price to confirmed 1H_L_BOS below the 1H_L_MAJOR


# COMMENT 2:
What are our trading plans and bias for the rest of this session? 


# RESOURCE:

```yaml
meta:
    pair: BTCUSDT
    units: "k"   # all numbers rounded with 'k'
    note: "Ranges use '-', e.g., 113.2-114.7k"

levels:
  ALL:
    ath: 126.2

  4H:
      major:
        H_MAJOR: 94.0
        L_MAJOR: 86.1
      sr:
        {}
      poc:
        POC_1: 91.9
        POC_2: 90.0
        POC_3: 86.9
        POC_4: 82.2
      zones:
        BUY_2: 87.7-89.5
        BUY_1: 85.3
      active:
        H_CHOCH: 86.9
      inactive:
        H_BOS: 89.2
        L_CHOCH: 90.2

    1H:
      major:
        H_MAJOR: 93.7
        L_MAJOR: 91.7
      sr: {}
      poc: {}
      zones:
        BUY_1: 91.5
        BUY_2: 92.3
      active:
        L_MSB: 92.7
      inactive:
        H_FSB: 93.4
        H_BOS: 92.3
```

