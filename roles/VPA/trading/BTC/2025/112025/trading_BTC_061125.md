# CONTEXT: 
## TRADER CONTEXT: 
Today is Thursday 6th of November 2025, we are in London session, 4 hours until US session. We have no major macro data released today. Due to government shutdown, we have not received many major macro economic data such as NFP/Unemployment/PPI for the last month and this is expected to continue this week.  Refers to `MACRO CONTEXT` for the rest of the macro events this week. 

Last month: We have officially passed October which was supposed to be bullish month for BTC and crypto in terms of seasonality during a bull cycle year, however we got the opposite of that: largest historic liquidation sell off after sweeping the ATH followed by choppy price actions at the bottom of the 1W range despite soft CPI + Inflation data print. 

Last week: Market seems to be responded positive to FED decisions coupled with positive resolution on China-US tariffs news which allow US equities putting new ATH, BTC recovering and cool-off on gold hyperbolic bullruns, signaling a potential risk-off environment. We also had FOMC last Wednesday in which the key details are outlined below:
```markdown
* **Cut 25 bps** to a **3.75%–4.00%** fed-funds target range; **two dissents** (Miran wanted –50 bps; Schmid preferred no change).
* **Ended QT effective Dec 1**: the Committee will **stop shrinking the balance sheet** and **reinvest all principal** thereafter (Treasuries rolled over; **all agency/MBS principal reinvested into T-bills**).
* **Operating settings** (implementation note): **IORB 3.90%**, **ON RRP 3.75%**, **SRF min 4.00%**, $500B aggregate SRF limit, RRP **$160B per-counterparty**.
* **Powell’s tone**: another cut in **December is “not a foregone conclusion,”** stressing data uncertainty amid the shutdown. 
* **Context & reaction**: Statement added emphasis on **rising downside risks to employment**; markets whipsawed as traders digested the **easing + QT end** vs **no December pre-commitment**.

> Why this matters: Ending QT + a 25-bp cut = **easier financial conditions via reserves/liquidity** and **lower policy rate**, but Powell explicitly **kept optionality**, so the **path** (not the single cut) drives cross-asset pricing.
```

This week: Price continued to sold off after the liquididation from last month, however despite bearish trend, given BTC 1W `OVERALL_ASSESSMENT = NEUTRAL-BEARISH`, we should remains cautious with breakout at either side of the 1W major structure and leaves room to trade mean-reversion at HTF extreme as much as possible. ISM data released this week shows mixed signal and has little effects on the market so far. 

Sentiment: Public sentiment for Q4 remain bullish for BTC within its bullish 4 years cycle from a seasonality and historic standpoint. However price action last month have liquidated millions of leveraged crypto traders and enact fears with hypothesis of the top for the cycle is already set for BTC, and the start of an extended bear market into 2026. `Fear & Greed Index` is currently sitting at 23 (EXTREME FEAR) continued to worsen from 30-40 (FEAR) since last week. 

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
      BUY_1: 90.1k
      BUY_2: 100.3k
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
      SR_5: 100.9k
    poc:
      POC_1: 115.3k
      POC_2: 111.2k
      POC_3: 109.6k
      POC_4: 103.8k
    zones:
      SELL_1: 119.4k
      SELL_2: 115.8k
      BUY_1: 106.1k
      NEUTRAL: 112.6k
    active:
      L_SWEEP: 108.6k
    inactive:
      L_MSB: 111.9k
      H_SWEEP: 124.5k

  1D:
    major: 
      H_MAJOR: 116.4k  
      L_MAJOR: 103.5k  
    sr: 
      SR_1: 114.3k
      SR_2: 110.5k
      SR_3: 106.4k
    poc:
      POC_1: 115.8k
      POC_2: 112.9k
      POC_3: 110.0k
      POC_4: 108.2k
      POC_5: 106.9k
    zones:
      SELL_1: 107.7-109.3k
    session:
      PDH: 104.5k
      PDL: 99.0k
    active: 
      L_BOS: 103.5k
    inactive:
      H_SWEEP: 116.0k

  4H:
    local: 
      H: 104.5k
      L: 102.7k
    major:                 
      H_MAJOR: 108.3k    
      L_MAJOR: 98.9k    
    sr:
      SR_1: 116.4k
    poc: 
      POC_1: 110.8k
      POC_2: 107.7k
      POC_3: 104.5k
      POC_4: 101.3k
    zones:
      SELL_1: 106.0k
      SELL_2: 104.7k
      BUY_1: 101.1k
    active:
      L_BOS: 106.7k
    inactive: 
      H_CHOCH: 111.2k
      L_BOS: 108.7k

  1H:
    major:
      H_MAJOR: 104.2k
      L_MAJOR: 102.7k
    sr: {}
    poc: {}
    zones:
      SELL_1: 104.1k
      BUY_1: 102.4k
      NEUTRAL: 103.5k
    active:
      H_SWEEP: 104.1k
    inactive: 
      H_BOS: 103.3k
      L_SWEEP: 103.3k

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

* **Previous (~30 candles):** Strong advance from late ’24 into `1W.major.H_MAJOR` / **ATH** `ALL.ath`, then distribution and a corrective leg that **confirmed** `1W.inactive.L_MSB`, breaking the weekly uptrend. The pullback retested `1M.inactive.H_BOS` together with the **weekly EMA band** and held, defining a weekly range. Multiple liquidity events since: an `1W.inactive.H_SWEEP` at `ALL.ath`, followed by crypto’s capitulation leg that tagged `1W.active.L_SWEEP` and printed a **stopping** `1W_bearish_hammer_HVC` at `1W.major.L_MAJOR`.
* **Current (~5 candles):** Bounce off `1W.zones.BUY_1` pushed to `1W.zones.NEUTRAL` mid-range but **failed** to reclaim the **weekly EMA stack**; sellers defended and price is **rolling over**, re-testing `1W.major.L_MAJOR` and wicking into `1M.zones.BUY_2` confluenced with `1W_50EMA/MA`. Weekly trend context = **NEUTRAL-BEARISH** while below the weekly EMA band and `1W.sr.SR_4`/`SR_5`.

---

### **1D — HTF for intraday**

* **Previous (~30 candles):** From the liquidation flush into `1W.major.L_MAJOR`, price rebounded but **rejected** at `1D.major.H_MAJOR` **and** the weekly mid `1W.zones.NEUTRAL`. The rebound leg printed lighter VCs versus the preceding sell leg. Loss of the 200MA/EMA and a **decisive** `1D.active.L_BOS` shifted the 1D trend down.
* **Current (~5 candles):** Price is bouncing from the **bottom of the weekly range** (`1W.major.L_MAJOR`) and `1M.zones.BUY_2`, probing back toward the **broken** `1D.active.L_BOS` while still **below** all primary MAs/VWAPs. Session references: `1D.session.PDH` **104.5k**, `1D.session.PDL` **99.0k**. Overhead magnets: `1D.poc.POC_4`/**POC_5** and `1D.zones.SELL_1` **107.7–109.3k**. Daily bias: **BEARISH**, unless price reclaims the BOS base with **bullish HVC**.

---

### **4H — HTF for 1H**

* **Previous (~30 candles):** After `4H.inactive.H_CHOCH` failed to continue higher, the 4H trend **resumed down**, capped by a descending W_VWAP + `4H_9EMA`. A series of `4H_bearish_VCs/HVCs` broke levels into `1M.zones.BUY_2`/`1W.major.L_MAJOR`, printing `4H.active.L_BOS` and establishing `4H.major.L_MAJOR` at **98.9k**.
* **Current (~5 candles):** Reactive bounce formed several `4H_bullish_hammer_HVCs` and pushed to the underside retest of `4H.zones.SELL_2` **104.7k** and the **broken** `1D.active.L_BOS`, confluenced with W_VWAP + `4H_9EMA`, where price **stalled** at `4H.local.H` **104.5k**. Overhead: `4H.major.H_MAJOR` **108.3k** and `4H.zones.SELL_1` **106.0k**. 4H bias: **BEARISH** while rallies are capped beneath the ST-EMA band and weekly VWAP.

---

### **1H — TTF (Execution)**

* **Previous (~30 candles):** Aggressive selloff into `1W.major.L_MAJOR`/`1M.zones.BUY_2` printed a **climactic** sequence of `1H_bearish_engulfing_HVCs`, then **bottomed** at `4H.major.L_MAJOR` + `1D.session.PDL` to rebounded toward `1H.zones.SELL_1/4H.zones.SELL_2` supply. The advance showed **lighter VCs** than the sell leg.
* **Current (~5 candles):** Price is **coiling below** `1H.zones.SELL_1` **104.1k** and `4H.zones.SELL_2` **104.7k** with repeated LHs after the most recent `1H.active.H_SWEEP`. Structure sits **below** S_VWAP/W_VWAP and the `1H_9/21/50/200` stack; `1H_bearish_spinning-top_VCs` at the underside tests indicate supply. While the intraday range trades around `1H.major.L_MAJOR` ↔ `1H.major.H_MAJOR` **104.2k**, the **mid** is the `1H.zones.NEUTRAL` area. TTF bias: **BEARISH RANGE** until a clean reclaim of S_VWAP + `1H_21EMA`.

## MACRO CONTEXT
### LAST WEEK

* **Fed (Wed, Oct 29):** The FOMC **cut the policy rate by 25 bps** and signaled a **more cautious, data-dependent stance**, noting gaps in official data amidst the government shutdown. Markets leaned dovish into early November as growth concerns persisted.
* **Tariffs / Trump (Wed–Thu, Nov 5–6):** The **U.S. Supreme Court heard oral arguments** on the legality of the administration’s use of **IEEPA** to impose broad tariffs. Several justices expressed **skepticism** about the statutory basis, raising uncertainty around the durability of current tariff policy.
* **Macro data pulse (Fri, Nov 7, 14:30 CET / 08:30 ET):** The **October Employment Situation (NFP)** is due **tomorrow** (outside market hours in Europe but **before** the U.S. cash open). It lands against a backdrop of shutdown-related data disruptions noted by the Fed.
* **Crypto flows (late Oct → early Nov):** **Spot BTC/ETH ETF flows** have skewed **net outflow** in recent days, acting as a near-term headwind for crypto beta into macro prints.

### THIS WEEK

* **U.S. holiday / liquidity (Tue, Nov 11 – Veterans Day):** **U.S. equity markets remain open** on normal hours, but the **U.S. bond market observes the holiday**. Expect **patchier fixed-income liquidity** to ripple through cross-asset pricing.
* **Key U.S. data (CET / ET):**

  * **Thu, Nov 13, 14:30 / 08:30 – CPI (Oct):** Headline & core in focus for the disinflation narrative post-cut.
  * **Fri, Nov 14, 14:30 / 08:30 – PPI (Oct)** **and** **Advance Retail Sales (Oct):** Producer-price impulse + consumer demand check in the same window.
* **Fed communications:** **FOMC Minutes (Oct 28–29)** arrive the **following week** (**Wed, Nov 19, 20:00 CET / 14:00 ET**), but traders will already start positioning after CPI/PPI.
* **Tech/AI & earnings that can sway index tone:**

  * **Cisco (CSCO)** – **Wed, Nov 12 (AMC)**: Networking/AI plumbing read-through for capex and enterprise demand.
  * **Disney (DIS)** – **Thu, Nov 13 (BMO)**: U.S. consumer pulse and streaming/parks read-through ahead of Retail Sales.
  * (Week after) **NVIDIA (NVDA) – Wed, Nov 19 (AMC)**: AI-capex bellwether; likely to color broader risk sentiment into month-end.
* **Policy overhang:** **Tariff legality** remains unresolved post-arguments; any headline risk can swing **USD, rates, industrials** and **commodities** (especially where pass-through inflation is a concern).

### MACRO ANALYSIS

#### BTC & ETH

Near-term **ETF outflows** are a **headwind**, so crypto likely **tracks liquidity** and **real-yield direction** around CPI/PPI. A **cooling inflation print** → **lower real yields / softer USD** historically supports **BTC beta** (and **ETH** via higher-beta spillover). Conversely, **hot prints** + risk-off in equities can extend pressure unless **“digital gold”** narratives re-ignite on **tariff-inflation** headlines. Into Tuesday’s **bond-market holiday**, intraday **volatility pockets** are more likely.

# TRADING PLAN FOR 1H_TTF (Trigger • Location • Context)

### **ORANGE_A — Short reversal from 4H supply → 1D supply**

* **Context:** Counter-rally on TTF to HTF bias from `1M.zones.BUY_2` is fading into stacked resistance: `4H.zones.SELL_1` **106.0k** (first cap) toward `1D.zones.SELL_1` **107.7–109.3k**. 1D/4H are **bearish** (price under 9/21/50/200; RSI < 50; under W/M VWAP). Expect **exhaustion/absorption** (`1H_bearish_doji_VCs`, CVD roll) at the underside of the BOS base.
* **Location:** `4H.zones.SELL_1` → extension to `1D.zones.SELL_1`, with descending `1H_200MA/EMA` overhead.
* **Trigger:** **TTF_L_MSB** (1H) after a **liquidity sweep** above `4H.zones.SELL_1` or the lower bound of `1D.zones.SELL_1`; confirm with **bearish HVC** + **falling CVD**.
* **Invalidation:** 1H **acceptance above** `1D.zones.SELL_1` with **bullish HVC** (trend continuation) — cancel.
* **Setup Priority:** **A**

---

### **ORANGE_B — Short reversal at 1H/4H confluence**

* **Context:** Price is stalling beneath `1H.zones.SELL_1` **104.1k** / `4H.zones.SELL_2` **104.7k`with S_VWAP + W_VWAP + descending`1H_50EMA` capping. Bounce volume is **subpar** vs selloff; RSI<50. Expect a failed push into this band.
* **Location:** `1H.zones.SELL_1` → `4H.zones.SELL_2` confluence, under W_VWAP.
* **Trigger:** **LTF_L_MSB (15m)** after a **wick-through** (`LTF_H_SWEEP`) into the zone; sell the pullback to the MSB flip.
* **Invalidation:** 1H close and hold **above** `4H.zones.SELL_2` + W_VWAP.
* **Setup Priority:** **A-**

---

### **PURPLE_A — Short fade of 1H local high**

* **Context:** **Range-fade** bias while 1D/4H stay bearish. Expect **weak upticks** into `1H.major.H_MAJOR` **104.2k** / `1H.zones.SELL_1` **104.1k** to fail with **bearish RSI/CVD divergence**.
* **Location:** `1H.major.H_MAJOR` / `1H.zones.SELL_1` with `4H.zones.SELL_2` above as extension.
* **Trigger:** **LTF_H_SWEEP → LTF_L_MSB**, then sell the first underside retest.
* **Invalidation:** 1H acceptance above `1H.major.H_MAJOR` **and** S_VWAP.
* **Setup Priority:** **B+**

---

### **PINK_A — Short momentum scalp on breakdown**

* **Context:** If the intraday coil fails, momentum should expand **down** with sellers defending VWAPs/MAs.
* **Location:** **Below** `1H.major.L_MAJOR` **102.7k** (with `1H.zones.BUY_1` **102.4k** as the shelf).
* **Trigger:** **15m_L_BOS** through `1H.major.L_MAJOR` on **bearish HVC / negative CVD**; enter on the **shallow retest** into LTF 9/21EMA.
* **Invalidation:** Swift **reclaim** back above `1H.major.L_MAJOR` + S_VWAP.
* **Setup Priority:** **B**

---

### **RED_A — Short breakdown of the major 1H shelf**

* **Context:** A decisive failure of `1H.major.L_MAJOR` + `1H.zones.BUY_1` confirms the **downtrend’s resumption** toward `4H.major.L_MAJOR` **98.9k** / `1D.session.PDL` **99.0k**.
* **Location:** Loss of `1H.major.L_MAJOR` and `1H.zones.BUY_1`.
* **Trigger:** **1H_L_MSB** + **15m_L_BOS** and sell the **underside retest** of the broken level.
* **Invalidation:** Re-acceptance above `1H.major.L_MAJOR` with **bullish HVC**.
* **Setup Priority:** **A**

---

### **BLUE_A — Long fade at 1H range low + demand**

* **Context:** Counter-trend fade only at **structural** demand, looking for **absorption** at lows (regular bullish divergence ideal). Sellers are dominant, so treat as **scalp-first**.
* **Location:** `1H.major.L_MAJOR` **102.7k** into `1H.zones.BUY_1` **102.4k** (front-run wicks).
* **Trigger:** **LTF_L_SWEEP → LTF_H_MSB** with stabilizing VCs and **CVD turn up**; reclaim S_VWAP to add.
* **Invalidation:** 1H close **below** `1H.zones.BUY_1` on **bearish HVC**.
* **Setup Priority:** **B-**

---

### **TEAL_A — Long momentum scalp on reclaim**

* **Context:** If buyers reclaim **S_VWAP + 1H_9/21EMA** and hold **above** the intraday mid `1H.zones.NEUTRAL`, a squeeze toward tops is possible despite HTF bearishness.
* **Location:** Reclaim/hold above S_VWAP + `1H_9/21EMA`, then push through `1H.zones.NEUTRAL` (103.5k).
* **Trigger:** **15m_H_BOS** continuation after a prior 15m_H_MSB realign; rising VCs + **positive CVD**.
* **Invalidation:** Lose S_VWAP again or **1H_L_CHOCH** right after entry.
* **Setup Priority:** **B**

---

### **YELLOW_A — Long major reversal at 4H demand**

* **Context:** Only if price **flushes** into `4H.zones.BUY_1` **101.1k** / `1D.session.PDL` **99.0k** within the larger `1M.zones.BUY_1` and prints a **stopping SHVC** with absorption signatures. Aim for a reflexive leg back to `4H.local.H`/`1W.poc.POC_4`.
* **Location:** `4H.zones.BUY_1` → extension to `4H.major.L_MAJOR` **98.9k** (wick risk).
* **Trigger:** **TTF_H_MSB (1H)** after a sweep + absorption; buy the first **low-volume pullback** to the MSB flip.
* **Invalidation:** Clean **acceptance below** `4H.zones.BUY_1` (defer to **RED_A** path).
* **Setup Priority:** **A-**

---

### **GREEN_A — Long breakout and retest over 1H high**

* **Context:** If demand overwhelms and price **clears** `1H.major.H_MAJOR` **104.2k** (inside `4H.zones.SELL_2`), a squeeze toward `4H.zones.SELL_1` **106.0k** / `1D.zones.SELL_1` can unfold.
* **Location:** Break and **retest** of `1H.major.H_MAJOR`.
* **Trigger:** **1H_H_BOS** with **bullish HVC** → buy the **LTF_H_BOS** retest with rising CVD.
* **Invalidation:** Failure retest (acceptance back **below** `1H.major.H_MAJOR`) or immediate **1H_L_CHOCH** after entry.
* **Setup Priority:** **B**
---


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