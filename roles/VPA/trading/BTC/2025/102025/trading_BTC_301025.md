# CONTEXT: 
## TRADER CONTEXT: 
Today is Thursday 30th of October 2025, we are in London session, 3 hours until US session. Due to government shutdown, we have not received many major macro economic data such as NFP/Unemployment/PPI for the last 3 week and this is expected to continue this week. We have Q3 GDP (Advance) released in 1 hour. Refers to `MACRO CONTEXT` for the rest of the macro events this week. 

We have officially passed September which has been notorious for a BTC and crypto pullbacks during the bull runs year and currently enter Q4 of which has been typical bullish for bitcoin bull cycle. We should favors more bullish setups while remains as cautious as possible until BTC firmly surpasses ATH. 

Last week: BTC recovered after crypto market got the biggest liquiditation sell off in the entire history, while gold has pullback significantly from its bullmarket, signaling risk-on environment supported by dovish FED and soft CPI + Inflation data print last weeks. 

This week: BTC HTF remains neutral with 1W `OVERALL_ASSESSMENT = NEUTRAL` as we are trading within this HTF range given price managed to close above the 1W range low as a confirmed `1W_L_SWEEP` and reclaimed the `1W_20EMA/MA` bull market support bands. Market seems to be respond positive to FED decisions with US equities putting new ATH and BTC recovering. This is also coupled with positive resolution on China-US tariffs news during the weekend that has haunted the market last 3 weeks. We had FOMC on Wednesday, refers to the below regarding all important details:
```markdown
* **Cut 25 bps** to a **3.75%–4.00%** fed-funds target range; **two dissents** (Miran wanted –50 bps; Schmid preferred no change). ([Federal Reserve][1])
* **Ended QT effective Dec 1**: the Committee will **stop shrinking the balance sheet** and **reinvest all principal** thereafter (Treasuries rolled over; **all agency/MBS principal reinvested into T-bills**). ([Federal Reserve][1])
* **Operating settings** (implementation note): **IORB 3.90%**, **ON RRP 3.75%**, **SRF min 4.00%**, $500B aggregate SRF limit, RRP **$160B per-counterparty**. ([Federal Reserve][2])
* **Powell’s tone**: another cut in **December is “not a foregone conclusion,”** stressing data uncertainty amid the shutdown. (Multiple outlets reported this line from the presser.) ([Financial Times][3])
* **Context & reaction**: Statement added emphasis on **rising downside risks to employment**; markets whipsawed as traders digested the **easing + QT end** vs **no December pre-commitment**. ([Federal Reserve][1])

> Why this matters: Ending QT + a 25-bp cut = **easier financial conditions via reserves/liquidity** and **lower policy rate**, but Powell explicitly **kept optionality**, so the **path** (not the single cut) drives cross-asset pricing.
```

Sentiment: Public sentiment for October remain bullish for BTC within this year of its bullish 4 years cycle from a seasonality and historic standpoint. However price action last 2-3 weeks have liquidated millions of leveraged crypto traders and enact some fears with people hypothesizing for the top of the cycle is in for BTC, and the start of an extended bear market into 2026. `Fear & Greed Index` is currently at neutral between 42-51 after dropping below to 22-30 in fear/extreme fear terriroty last week. 

## TECHNICAL CONTEXT
### Key Levels 

```yaml
meta:
    pair: BTCUSDT
    units: "k"   # all numbers rounded with 'k'
    note: "Ranges use '-', e.g., 113.2-114.7k"

levels:
  ALL:
    ath: 126.2k

  1M:
    major: 
      H_MAJOR: 126.2k
      L_MAJOR: 74.5k
    sr: {}
    poc:
      POC_1: 118k
      POC_2: 104.7k
      POC_3: 96.4k
    zones: 
      BUY_1: 90.0k
      BUY_2: 100.2k
    inactive:
      H_BOS: 109.6k

  1W:
    major:
      H_MAJOR: 126.2k
      L_MAJOR: 102.0k
    sr:
      SR_0: 119.4k
      SR_1: 114.2k
      SR_2: 102.7k
      SR_3: 105.6k
      SR_4: 108.3k
      SR_5: 112.2k
    poc:
      POC_1: 115.3k
      POC_2: 111.2k
      POC_3: 108.8k
      POC_4: 121.7k
    zones:
      SELL_1: 120.2k
      BUY_1: 106.1k
      NEUTRAL: 114.1k
    active:
      L_SWEEP: 108.6k
    inactive:
      L_MSB: 111.9k
      H_SWEEP: 124.5k

  1D:
    local: 
      L: 106.7k
    major: 
      H_MAJOR: 116.4k  
      L_MAJOR: 103.5k  
    sr: 
      SR_1: 110.2k
      SR_2: 114.3k
    poc:
      POC_1: 115.8k
      POC_2: 112.9k
      POC_3: 109.4k
      POC_4: 106.9k
    zones:
      SELL_1: 114.3k
      BUY_1: 107.3k
      NEUTRAL: 110.0k
    session:
      PDH: 113.6k
      PDL: 109.2k
    active: 
      H_SWEEP: 116.0k
    inactive:
      H_CHOCH: 114.0k
      L_BOS: 109.6k


  4H:
    major:                 
      H_MAJOR: 113.6k    
      L_MAJOR: 107.9k    
    sr:
      SR_1: 116.4k
    poc: 
      POC_1: 110.8k
      POC_2: 112.5k
      POC_3: 113.6k
      POC_4: 115.0k
    zones:
      SELL_1: 111.5-112.2k
    active:
      L_BOS: 112.1k
    inactive: 
      L_CHOCH: 114.5k
      L_MSB: 112.9k

  1H:
    major:
      H_MAJOR: 112.0k
      L_MAJOR: 107.9k
    sr: {}
    poc: {}
    zones:
      SELL_1: 111.0k
      NEUTRAL: 110.0k
    active:
      L_BOS: 109.2k
    inactive: 
      H_SWEEP: 113.6k
      L_BOS: 112.7k

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

* **Previous (~30 candles):** Strong uptrend from late ’24 into **ATH** `ALL.ath` / `1W.major.H_MAJOR`, then a corrective leg confirmed `1W.inactive.L_MSB` that broke the weekly up-sequence. The pullback retested the monthly breakout `1M.inactive? → 1M.active.H_BOS` area and the weekly EMA band, forming a base toward `1W.major.L_MAJOR` **102.0k**. For ~3 months, price ranged within the major structure, printing multiple range-edge liquidity events — most recently a **top** `1W.inactive.H_SWEEP` followed by a **bottom** `1W.active.L_SWEEP` near `1W.sr.SR_4`/`1W.poc.POC_3` **108.3–108.8k**.

* **Current (~5 candles):** Bounce from the sweep low is rotating back toward mid-range `1W.zones.NEUTRAL` **114.1k** while grinding around the EMA band — last week reclaimed the band; this week is **retesting from below/around** `1W_21EMA (≈111.1k)` with `M_VWAP` still overhead **112.1k**. HTF bias: **neutral → constructive into mid-range**, while below `1W.poc.POC_1` **115.3k** / `1W.sr.SR_1` **114.2k** supply.

---

### **1D — HTF for intraday**

* **Previous (~30 candles):** After rolling over from the weekly mid-range, a sharp liquidation sold off with a `1D_bearish_engulfing_HVC`, swept the weekly range low and based above `1W.major.L_MAJOR` **102.0k** before closing back into the weekly range and holding the rising `1D_200EMA` **108.3k**. Internal up-leg produced `1D.inactive.H_CHOCH`, retested `1D.major.H_MAJOR` **116.4k** (confluence with `1W.zones.NEUTRAL` **114.1k** → `1D.zones.SELL_1` **114.3k** overhead band).

* **Current (~5 candles):** A `1D.active.H_SWEEP` **116.0k** preceded a rollover via `1D_bearish_inverted-hammer_VC`. Price is now in a **bearish leg down** from the 1D range high, retesting `1D.zones.NEUTRAL` **110.0k** with the ascending `1D_200EMA` **108.3k** just below. Daily bias: **neutral-bearish** while below `1D.poc.POC_2` **112.9k** / `1D.zones.SELL_1` **114.3k**.

---

### **4H — HTF for 1H**

* **Previous (~30 candles):** Weekend leg rallied toward `1D.major.H_MAJOR` **116.4k**, then rejection initiated a downtrend: `4H.inactive.L_MSB` flipped structure, followed by `4H.active.L_BOS` **112.1k** to push back to the 1D mid-range (`1D.zones.NEUTRAL` **110.0k**). The bearish leg printed multiple `4H_bearish_HVCs` relative to the prior up-leg.

* **Current (~5 candles):** Price sits **under all momentum MAs** and trades below `4H.poc.POC_1` **110.8k**. Overhead supply is concentrated at `4H.zones.SELL_1` **111.5–112.2k** with `4H.major.H_MAJOR` **113.6k** / `1D.session.PDH` **113.6k** above. Bias: **bearish**, favoring sell-rallies into `4H.zones.SELL_1`.

---

### **1H — TTF (execution)**

* **Previous (~30 candles):** Persistent 1H downtrend with increasing `1H_bearish_HVCs`, climaxing into `1H.major.L_MAJOR` **107.9k** via `1H_bearish_engulfing_HVC`. Bounce reclaimed `S_VWAP` briefly on lower `1H_bullish_LVCs`, then rejected from the confluence `1H.zones.SELL_1` **111.0k** / `4H.zones.SELL_1` **111.5–112.2k** and rolled back below descending `1H_9/21EMA`. Price remains within a range of its 1H major structure with `1H.zones.NEUTRAL` as potential mid-range level. 

* **Current (~5 candles):** Price oscillates around `1D.zones.NEUTRAL` **110.0k** confluenced with `1H.zones.NEUTRAL` with lower highs under `S_VWAP`. Short-term bias: **bearish within a local 1H range**, with magnets at `4H.poc.POC_1` **110.8k** (overhead) and `1D.poc.POC_3` **109.4k** / `1D.session.PDL` **109.2k** below.
  
## MACRO CONTEXT
### LAST WEEK

* **Policy overhang – Trump & tariffs:** Legal uncertainty persisted around the administration’s **“reciprocal” 10% baseline tariffs** (IEEPA cases stayed pending appeal), while a **new 25% tariff on medium/heavy trucks & parts** was proclaimed (effective **Nov 1**). These headlines kept supply-chain and goods-inflation risks on the radar.
* **Government shutdown:** The federal shutdown (began **Oct 1**) dragged on, raising **data-blackout / delay risk** (especially BLS) and a small but rising **growth hit** into Q4.
* **Fed watch (setup):** Markets leaned to a **25bp cut** at the Oct 29 FOMC, with heightened sensitivity to guidance given patchy official data.
* **Crypto flows tone:** US **spot BTC ETFs** saw **net inflows** mid-to-late week (e.g., **Oct 27–28**), providing a constructive backdrop into this week.

### THIS WEEK

* **Fed (Oct 29):** FOMC **cut 25bp** to **3.75%–4.00%**; Powell stressed **“December is not a foregone conclusion.”** Vote **10–2** (one for –50bp, one for no cut). Markets refocused on data scarcity and the path of labor softness vs inflation stickiness.
* **Key US data & dates (ET):**

  * **Thu, Oct 30, 08:30** – **Q3 GDP (Advance)**.
  * **Fri, Oct 31, 08:30** – **PCE & Core PCE (Sep)**.
  * **Mon, Nov 3, 10:00** – **ISM Manufacturing (Oct)**.
  * **Fri, Nov 7, 08:30** – **Employment Situation (Oct)** *(scheduled; shutdown could still complicate)*.
* **Treasury supply & term-premium risk:**

  * **Mon, Nov 3, 15:00** – **Financing estimates** (Treasury).
  * **Wed, Nov 5, 08:30** – **Quarterly Refunding Announcement (QRA)** (coupon sizes, mix).
* **Tariffs – new effective date:** **25% tariff on medium/heavy trucks** & parts **takes effect Sat, Nov 1** (first full US session impact Mon, Nov 3).
* **Big Tech earnings impulse:** **MSFT & GOOGL beat (Oct 29); AAPL & AMZN report after-hours Oct 30.** AI-capex momentum vs margin guidance is steering risk appetite and factor leadership.
* **Crypto ETF flows near-term:** **BTC ETFs flipped to notable outflows on Oct 29** after the Fed; **ETH ETF flows remain choppy** (brief inflow streak faded).
* **Calendar / liquidity:** **US DST ends Sun, Nov 2** → from **Mon, Nov 3** the **NYSE opens 15:30 CET** (back to the usual Copenhagen offset). **US off-year elections Tue, Nov 4** may modestly affect risk and intraday liquidity.

### MACRO ANALYSIS

In the near term, **rates path + Treasury supply** dominate: the **25bp cut** supports **risk & gold** at the margin, but Powell’s **non-commitment on December** and next week’s **QRA** keep **yields and USD** volatile. **Tariff implementation (Nov 1)** adds a mild **goods-inflation / supply-chain** tail risk. **Big Tech beats** bolster **SPX** breadth on AI-capex, which often **lifts crypto beta** when yields are steady; however, **BTC ETF outflows post-FOMC** warn of **two-way risk** around GDP/PCE and QRA. **Gold** benefits from **cuts & shutdown angst**, but can **fade** if **term premium** rises on heavier refunding.

#### BTC & ETH

* **Flows turned mixed**: inflows early in week → **outflows on Oct 29** post-FOMC; **ETH flows choppy**.
* **Correlation lens**: positive beta to **SPX/Big Tech** when yields calm; **inverse to real yields** if QRA lifts term premium.
* Tactically: respect **event risk** (GDP, PCE, ISM, Jobs, QRA). Fade euphoric spikes into supply if **CVD diverges** and **MSB/CHOCH** confirms.

# TRADING PLAN FOR 1H_TTF (Trigger • Location • Context)

> **Environment:** 1H and 4H are **bearish**, 1D is **neutral-bearish** (below 9/21/50 but above 200). Preference: **sell rallies into HTF supply**. Only take longs on **confirmed** sweeps/MSBs at major lows. **CVD must confirm direction**; avoid entries against fresh SHVC.

---

### ORANGE_A — Short pullback into 1H/4H sell bands

* **Context:** After `1H.active.L_BOS` **109.2k**, expect counter-trend bounce toward `1H_21EMA` **110.9k**. With 4H/1H MAs stacked bearishly and CVD soft (~-300), expect supply to reload on shallow rallies.
* **Location:** `1H.zones.SELL_1` **111.0k** → extension into `4H.zones.SELL_1` **111.5–112.2k** and cap at `1H.major.H_MAJOR` **112.0k**.
* **Trigger:** **15m_L_MSB** (realign down) after a wick/failed hold above `S_VWAP` or the band; bearish VC/HVC preferred with falling CVD.
* **Invalidation:** 1H close **above** `4H.zones.SELL_1` **112.2k** and acceptance above `1H.major.H_MAJOR` **112.0k**.
* **Setup Priority:** **A+**

---

### ORANGE_B — Short reversal at PDH/4H_H_MAJOR

* **Context:** If a squeeze pushes into the top of the 4H range, monitor for exhaustion; 1D remains below `1D.zones.SELL_1`.
* **Location:** Confluence at `1D.session.PDH` **113.6k** = `4H.major.H_MAJOR` **113.6k** beneath `1D.zones.SELL_1` **114.3k**.
* **Trigger:** **15m/1H_L_MSB** after **H_SWEEP** of PDH; look for sell-side HVC or CVD roll-over.
* **Invalidation:** Acceptance **above** `1D.zones.SELL_1` **114.3k** (trend ignition risk).
* **Setup Priority:** **A-**

---

### PURPLE_A — Short fade with H_SWEEP at 1H_H_MAJOR

* **Context:** Local 1H range; repeated failures below `1H.major.H_MAJOR`.
* **Location:** `1H.major.H_MAJOR` **112.0k** (with `4H.zones.SELL_1` just above).
* **Trigger:** **LTF H-sweep** of `1H.major.H_MAJOR` → **15m_L_CHOCH** back inside; confirm with weakening CVD.
* **Invalidation:** 1H acceptance above **112.0k** and hold.
* **Setup Priority:** **B+**

---

### PURPLE_B — Short fade with H_SWEEP at PDH/4H_H_MAJOR

* **Context:** Same thesis as ORANGE_B but requires explicit sweep; patience needed.
* **Location:** `1D.session.PDH` **113.6k** / `4H.major.H_MAJOR` **113.6k**.
* **Trigger:** **TTF_L_CHOCH** after the sweep; add on **15m_L_MSB** with bearish VC.
* **Invalidation:** Strong acceptance above **113.6k**, or immediate **1H_H_BOS**.
* **Setup Priority:** **B-**

---

### PINK_A — Momentum short if VWAP/neutral gives way

* **Context:** Price is struggling under `S_VWAP` **110.1k** and `1D.zones.NEUTRAL` **110.0k**; momentum build below these opens the door to PDL sweep.
* **Location:** Breakdown **below** `1H.zones.NEUTRAL` **110.0k** and `S_VWAP` **110.1k**, targeting `1D.poc.POC_3` **109.4k** / `1D.session.PDL` **109.2k**.
* **Trigger:** **LTF_L_BOS** with bearish HVC and falling CVD; add on the low-volume retest of **110.0k** from below.
* **Invalidation:** Reclaim and hold **above** `S_VWAP` **110.1k** + `1H_21EMA` **110.9k**.
* **Setup Priority:** **B**

---

### RED_A — Breakdown & retest of major range low

* **Context:** A flush through structural lows would align all TFs bearish and challenge the daily 200 band.
* **Location:** **Loss of** `1H/4H.major.L_MAJOR` **107.9k** → first retest from below; extension toward `1D.zones.BUY_1` **107.3k**.
* **Trigger:** **1H_L_BOS** through **107.9k** on strong sell VPA + negative CVD → **LTF_L_MSB** on retest.
* **Invalidation:** Swift reclaim back above **107.9k** with bullish VC/CVD.
* **Setup Priority:** **A**

---

### BLUE_A — Long fade with L_SWEEP at 1H/4H_L_MAJOR

* **Context:** Counter-move only if sellers climax into the floor; must see exhaustion + reversal signal + bullish divergences. 
* **Location:** `1H/4H.major.L_MAJOR` **107.9k** (wick room to `1D.poc.POC_4` **106.9k** / `1D.zones.BUY_1` **107.3k**).
* **Trigger:** **TTF_H_CHOCH** after a clean **L_SWEEP**, ideally with CVD HL divergence and low-volume pullback.
* **Invalidation:** 1H acceptance **below** **107.9k** (then hand off to **RED_A**).
* **Setup Priority:** **B-**

---

### TEAL_A — Counter-trend long above VWAP & mid

* **Context:** Tactical scalp only if price **reclaims and sustains** above `S_VWAP` **110.1k** and `1H.zones.NEUTRAL` **110.0k** with CVD turning up.
* **Location:** Pullback into the reclaimed band (VWAP + mid) with `1H_9/21EMA` curling up.
* **Trigger:** **LTF_H_BOS** after the reclaim; avoid if buy VCs stall under `4H.poc.POC_1` **110.8k**.
* **Invalidation:** Lose `S_VWAP` again on sell-side HVC.
* **Setup Priority:** **B**

---

### YELLOW_A — Long reversal at 4H_L_MAJOR to HTF demand

* **Context:** A stronger reversal path if 1H/4H sell swing completes into 4H floor and daily buyers defend.
* **Location:** `4H.major.L_MAJOR` **107.9k** with room to `1D.zones.BUY_1`  **107.3k**.
* **Trigger:** **1H_H_MSB** (TTF trend death) after a sweep/absorption SHVC; enter on the first pullback.
* **Invalidation:** Failure of MSB zone (lower low through **107.9k**).
* **Setup Priority:** **A**

---

### YELLOW_B — Long after breakout & deeper pullback

* **Context:** If price **breaks above** `1H.major.H_MAJOR` **112.0k** and confirms a TTF trend change.
* **Location:** Retest of the **new** 1H demand created by the breakout (above **112.0k**), with `4H.zones.SELL_1` acting as pivot below.
* **Trigger:** **1H_H_MSB** then deeper pullback → **LTF_H_MSB** in the demand.
* **Invalidation:** Acceptance back **below 112.0k** (failed breakout).
* **Setup Priority:** **A-**

---

### GREEN_A — Long breakout & retest of 1H range high

* **Context:** Momentum continuation if buyers ignite through resistance.
* **Location:** Clean **break and retest** of `1H.major.H_MAJOR` **112.0k** → first objective `4H.poc.POC_2` **112.5k** then `4H.major.H_MAJOR` / `PDH` **113.6k**.
* **Trigger:** **1H_H_BOS** with bullish VC/CVD → **LTF_H_MSB** on shallow retest.
* **Invalidation:** Failure back under **112.0k** or immediate **1H_L_CHOCH** after entry.
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
- 1W: `OVERALL-ASSESSMENT = NEUTRAL`.
- `PG` grades are assessed based on the plan full viability. DO NOT DEGRADE the plan based on probability/possibility.  
- DO NOT PERFORM TTI on the 1W_TF. 