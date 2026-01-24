# CONTEXT: 
## TRADER CONTEXT: 
Today is Tuesday 11th of November 2025, we are in London session, 2 hours until US session. We have no major macro events or data released today. Due to government shutdown, we have not received many major macro economic data such as NFP/Unemployment/PPI for the last month and this is expected to continue this week. Refers to `MACRO CONTEXT` for the rest of the macro events this week. 

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
      POC_4: 103.9
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
      POC_6: 102.0
    zones:
      SELL_1: 109.3
      SELL_2: 107.7
      BUY_1: 98.2
    session:
      PDH: 106.7
      PDL: 104.3
    active:
      L_BOS: 103.5
    inactive:
      H_SWEEP: 116.0

  4H:
    major:
      H_MAJOR: 107.5
      L_MAJOR: 104.7
    sr:
      SR_1: 116.4
    poc:
      POC_1: 110.8
      POC_2: 107.7
      POC_3: 106.0
      POC_4: 104.5
      POC_5: 101.3
    zones:
      SELL_1: 105.3
      BUY_1: 102.9
      BUY_2: 104.0
      NEUTRAL: 106.1
    active:
      H_SWEEP: 106.7
      L_MSB: 104.7
    inactive:
      H_BOS: 104.1

  1H:
    major:
      H_MAJOR: 105.5
      L_MAJOR: 104.7
    sr: {}
    poc: {}
    zones:
      SELL_1: 104.6
      SELL_2: 104.1
    active:
      L_CHOCH: 105.3
      L_BOS: 104.7
    inactive:
      H_SWEEP: 106.7
      H_BOS: 105.1

  15m:
    major:
      H_MAJOR: 104.7
      L_MAJOR: 103.2
    sr: {}
    poc: {}
    zones:
      SELL_1: 103.3
    active:
      L_BOS: 103.2
    inactive: 
      L_BOS: 103.8
```

### **1W — Super-HTF Structure**

* **Previous (~30 candles):** Strong advance from late ’24 into `ALL.ath` / `1W.major.H_MAJOR`, then distribution and a corrective leg that **confirmed** `1W.inactive.L_MSB`, breaking the weekly up-sequence. Pullback retested the `1M.inactive.H_BOS` area with confluence from **1W_20EMA/MA** and held, establishing a multi-month consolidation under `ALL.ath`. Multiple liquidity events followed, including `1W.inactive.H_SWEEP` at the ATH and last month’s capitulation to `1W.active.L_SWEEP` that printed a **`1W_bearish_hammer_HVC`** at the range-low extreme near `1W.major.L_MAJOR`.
  **Indicators:** Price **below** `1W_9/21EMA` (9≈110.35k, 21≈110.07k) but **above** `1W_50EMA` (≈101.19k). `1W_RSI` 47 < `RSI_MA` 55 → momentum **soft**. `W_VWAP` ≈ 105.7k marginally above price; `M_VWAP` ≈ 104.9k below.

* **Current (~5 candles):** Bounce from `1W.zones.BUY_1` toward the mid-range `1W.zones.NEUTRAL`, rejected near the **bearish crossover** band (`1W_9/21EMAs`) and rolled back to re-test the range low. Last week closed above `1W.major.L_MAJOR` with a **`1W_bearish_hammer_VC`** into `1M.zones.BUY_1`, defended by the rising `1W_50EMA`. This week so far is an inside/retest bar holding **between** `M_VWAP` and `W_VWAP`.
  **HTF read:** **NEUTRAL-BEARISH** while sub `1W_9/21EMA`, constructive as long as `1W.major.L_MAJOR` holds.

---

### **1D — HTF for intraday**

* **Previous (~30 candles):** Post-liquidation recovery leg pushed toward `1D.major.H_MAJOR` and the weekly mid `1W.zones.NEUTRAL`, then **failed**, losing `1D_200EMA/MA` and confirming **`1D.active.L_BOS`** as price rotated back to the 1W range low. A base formed at `1D.major.L_MAJOR` and we reclaimed the **`1D.active.L_BOS`** level.
  **Indicators:** Price **above** `1D_9EMA` (≈105.13k) but **below** `1D_21/50/200EMA` (≈107.15k / 110.05k / 108.00k). `1D_RSI` 44 < 50 with `RSI_MA` ≈41 → **bearish** bias but upticking. `S_VWAP` and `W_VWAP` both **above** price; `M_VWAP` below.

* **Current (~5 candles):** Rebound leg is probing daily supply **`1D.zones.SELL_2 → SELL_1`** confluenced with descending `1D_21EMA` while riding the reclaimed `1D_9EMA`. Yesterday’s session references sit at `1D.session.PDH` and `1D.session.PDL`. Expect push-pull around `1D.poc.POC_5`/`POC_4` on tests.
  **HTF read:** **BEARISH* into supply** — buyers must convert `1D.zones.SELL_2/SELL_1` to sustain further upside.

---

### **4H — HTF for 1H**

* **Previous (~30 candles):** After the base at `1D.major.L_MAJOR`, price coiled in a **4H wedge** then broke out with clustered **`4H_bullish_VCs`**, tagging `4H.zones.SELL_1` and accepting a range whose mid sits at **`4H.zones.NEUTRAL`**. A wick into `1D.zones.SELL_1` printed **`4H.active.H_SWEEP`**, and we closed back **inside** the 4H range.
  **Indicators:** Price ≈ `4H_9EMA` and **above** `4H_21/50EMA`, **well below** `4H_200EMA` (≈108.9k). `4H_RSI` 55 > 50 but rolling under `RSI_MA` 58. `W_VWAP` slightly above price; `M_VWAP` below.

* **Current (~5 candles):** Retesting the lower half of the range near `4H.major.L_MAJOR`/`4H.poc.POC_4`, with the reclaimed `4H_50EMA` acting as first dynamic support. Acceptance back above **`4H.zones.NEUTRAL`** would re-open the bracket top toward `4H.major.H_MAJOR`; failure risks a drive to `4H.zones.BUY_2 → BUY_1`.
  **HTF read:** **NEUTRAL** (range), slight bullish tilt while above `4H_21/50EMA`.

---

### **1H — TTF (execution)**

* **Previous (~30 candles):** Trend leg up reclaimed `1H_200EMA/MA` culminating in **`1H.inactive.H_BOS`**. Asia session swept the 4H range high into `1D.zones.SELL_1` with a **`1H_bearish_inverted-hammer_HVC`**, then **`1H.active.L_CHOCH`** flipped the local tape, sliding **below** `S_VWAP` and `1H_9/21EMA`, back under `1H.zones.BUY_1`. A HL printed at `1H.major.L_MAJOR` with help from rising `1H_50/200EMA`.
  **Indicators (current):** Price **below** `S_VWAP` and `W_VWAP`, **below** `1H_9/21EMA`, **above** `1H_50/200EMA`. `1H_RSI` 48 < `RSI_MA` 51 → lack of momentum.

* **Current (~5 candles):** Retesting the pivot **`1H.zones.BUY_1`** from underneath while the **`1H.active.L_CHOCH`** remains the key local inflection. Acceptance back above `S_VWAP`/`1H_9/21EMA` would set a momentum reclaim; failure keeps pressure toward `1H.major.L_MAJOR` and `4H.zones.BUY_2`.
  **TTF read:** **NEUTRAL-BEARISH** below `S_VWAP`/`1H_9/21EMA`; reactive tape inside a 4H range.

## MACRO CONTEXT
### LAST WEEK

* **Shutdown & data blackout:** The U.S. government shutdown (since Oct 1) continued to distort macro visibility. Some essential private proxies filled gaps (e.g., **ADP** showed a modest Oct payroll gain), while official BLS labor data were not released. The Senate **passed a funding bill late Mon, Nov 10** to end the shutdown; it now awaits House approval and the President’s signature.
* **Fed focus—policy path & independence:** With the Oct 28–29 **FOMC** meeting behind us and minutes due **Nov 19**, markets traded rate-cut expectations on incomplete data. Separately, legal action around the attempted removal of **Fed Gov. Lisa Cook** kept Fed independence in headlines (appeals courts have blocked removal; emergency petitions are pending at SCOTUS).
* **Tariffs—China truce tweaks, baseline stays:** The administration **kept the 10% “reciprocal” baseline tariff** in place and **temporarily cut the China “fentanyl” tariff from 20% to 10% effective Nov 10**, framing it as part of a limited truce while maintaining broader tariff posture.
* **Growth pulse:** **ISM Services (Oct)** returned to expansion (52.4), a constructive signal amid the data blackout and shutdown.
* **Flows & risk tone:** U.S. equity funds saw sizeable **inflows** into large-cap/tech. In crypto, **U.S. spot BTC & ETH ETFs posted heavy weekly net outflows**—risk appetite wavered in the data vacuum.
* **Gold:** Bid higher into the week on **rate-cut hopes + shutdown resolution**, with bullion printing a ~2–3-week high by Mon/Tue.

### THIS WEEK

* **Key U.S. data (ET / CET):**

  * **Thu, Nov 13, 8:30 ET (14:30 CET)** – **CPI (Oct)** (BLS calendar shows on-time; final publication still contingent on shutdown resolution logistics).
  * **Fri, Nov 14, 8:30 ET (14:30 CET)** – **PPI (Oct)**; **Retail Sales (Oct)** (Census schedule).
  * **Fed:** **FOMC Minutes (Oct 28–29)** due **Wed, Nov 19, 2:00 ET (20:00 CET)**—*next week*, but markets will pre-position this week.
* **Policy & politics:**

  * **Shutdown endgame:** Senate passed a funding deal (Nov 10); **watch House vote + White House signature timing**—headlines can move USD, yields, gold, and beta.
  * **Tariffs:** Limited **China tariff easing** (fentanyl component to 10%) is **now in effect**; the **10% baseline tariff** remains in force and has been **extended into 2026**—trade headlines remain a tail-risk for equities, USD/CNH, metals, and semis.
  * **Fed independence storyline:** Ongoing court actions around **Gov. Cook** are a volatility overhang for rates if headlines escalate.
* **Tech/AI earnings impulse:** **NVIDIA Q3 FY26** results **Wed, Nov 19 (after market)**—*next week*, but guidance/AI-capex expectations can influence this week’s SPX/Nasdaq risk taking.
* **Market plumbing / calendars:**

  * **Veterans Day (Tue, Nov 11):** U.S. **equities open; bonds closed**—watch liquidity.
  * **Options:** **Monthly OPEX Fri, Nov 21**—positioning dynamics may start to influence skew & intraday flows late this week.
  * **NYSE holiday cadence:** Next full U.S. market holiday is **Thanksgiving Thu, Nov 27** (early close Fri, Nov 28).

### MACRO ANALYSIS

**Bottom line:** Into **CPI/PPI/Retail Sales**, the market is trading a **“soft-data + shutdown-resolution”** narrative: lower yields and improving liquidity are **supportive for SPX and gold**, while **crypto beta is more sensitive to flows and policy-headline volatility**. If CPI is benign and shutdown ends smoothly, **yields likely stay capped**, favoring **gold on dips** and **SPX/AI high-beta** into NVDA next week; conversely, a hot CPI or renewed policy friction (tariffs/Fed independence) risks a **USD/yield pop** that **pressures BTC/ETH and rich tech multiples** while **gold dips are bought**.

#### BTC & ETH

* **Bias:** **Two-way, flow-led.** ETF **outflows** last week weakened topside follow-through; shutdown resolution + benign CPI could stabilize risk.
* **Drivers:** CPI/PPI, **USD/yields**, **ETF flows**, and any **tariff/Fed independence** headlines.
* **Tactical:** Respect **flow regimes**: if BTC/ETH spot ETFs flip back to net **inflows**, lean into **TTF pullbacks** to **AEZ**; if outflows persist alongside a USD pop, prioritize **defense**, fade weak bounces toward **LVN/SR** with clear invalidations.

  
# TRADING PLAN FOR 1H_TTF (Trigger • Location • Context)

### **ORANGE_A — Short reversal at daily supply**

* **Context:** Counter-trend fade of the rebound. 1H sits below `S_VWAP`/`1H_9/21EMA`; 4H remains capped by the falling `4H_200EMA`. Expect buyer fatigue if price tags daily supply. Watch for **bearish RSI/CVD divergence** and slowing buy VCs into level.
* **Location:** `1D.zones.SELL_2` → `1D.zones.SELL_1`, overlapping `4H_200EMA` and magnets at `1D.poc.POC_4/POC_3`.
* **Trigger:** **`TTF_L_MSB`** (15m→1H cascade) after a **sweep/failed break** into `1D.zones.SELL_2/SELL_1` with **absorption/ignition HVC** down.
* **Invalidation:** 1H acceptance **above** `1D.zones.SELL_1` with rising CVD and a fresh **1H_H_BOS**.
* **Setup Priority:** **A-**

---

### **PURPLE_A — Short fade of 4H range top**

* **Context:** Range trade. If price pops to the 4H top and stalls, we fade the failure. Expect wicks and **bearish CVD divergence** near the top edge.
* **Location:** `1H.zones.SELL_1` with extension to `4H.major.H_MAJOR`; overhead sellers also align with `4H.zones.SELL_1`.
* **Trigger:** **H-sweep** of `1H.zones.SELL_1` / tickle `4H.major.H_MAJOR` → **`LTF_L_MSB`** back inside.
* **Invalidation:** 1H close and hold **above** `4H.major.H_MAJOR`.
* **Setup Priority:** **B+**

---

### **PINK_A — Short momentum scalp below mid-range**

* **Context:** Momentum path while 1H trades **below** `S_VWAP` + `1H_9/21EMA` and **under** `4H.zones.NEUTRAL`. The active **`1H_L_CHOCH`** favors a push to the range lows if buyers fail to reclaim.
* **Location:** Below `4H.zones.NEUTRAL` and `1H.zones.BUY_1` (flip zone).
* **Trigger:** Maintain rejection under bands → **`1H_L_CHOCH` continuation** with **`LTF_L_BOS/MSB`** on the retest, ideally on **decreasing** pullback volume.
* **Invalidation:** Full reclaim of `S_VWAP` + `1H_9/21EMA` with CVD turning up (then consider **TEAL_A**).
* **Setup Priority:** **B**

---

### **RED_A — Breakdown of major range low**

* **Context:** Structural flip if the lower band fails. That would align a fresh 1H down-sequence against the 4H base and threaten the daily bounce.
* **Location:** **Break/loss** of `1H.major.L_MAJOR` / `4H.major.L_MAJOR` with `4H.poc.POC_4` just beneath.
* **Trigger:** **`1H_L_MSB`** through `1H.major.L_MAJOR` on **bearish HVC** + negative CVD → **sell the low-volume retest** with `LTF_L_BOS/MSB`.
* **Invalidation:** Fast reclaim back above `1H.major.L_MAJOR` and `1H_50EMA`.
* **Setup Priority:** **A**

---

### **BLUE_A — Long fade at the 1H/4H demand shelf**

* **Context:** Buy the 4H range low if sellers tire. Look for **bullish RSI/CVD divergence** and **weakening sell VCs** into the shelf.
* **Location:** `1H.major.L_MAJOR` / `4H.major.L_MAJOR` with confluence from `1H_50EMA` + `1H_200EMA` and `4H.poc.POC_4`.
* **Trigger:** **Liquidity sweep** below the shelf → **`LTF_H_MSB`** back inside; confirm with reclaim of the 1H ST-EMAs.
* **Invalidation:** Acceptance below `4H.major.L_MAJOR` with sell-side HVC.
* **Setup Priority:** **B-**

---

### **TEAL_A — Long momentum reclaim**

* **Context:** Counter the local dip only **after** buyers retake control. We need a reclaim of `S_VWAP` + `1H_9/21EMA` and price holding **above** `1H.active.L_CHOCH`.
* **Location:** `S_VWAP`/`1H_9/21EMA` band reclaimed, anchored to `1H.active.L_CHOCH`.
* **Trigger:** **`LTF_H_BOS/MSB`** through the band, then buy the **shallow retest** if pullback volume is light and CVD rises.
* **Invalidation:** Loss of `1H.active.L_CHOCH` after entry or immediate bearish HVC back through the band.
* **Setup Priority:** **B**

---

### **YELLOW_A — Long major reversal at 4H demand / BOS retest**

* **Context:** Best-reward reversal if the market backfills the weekend breakout base.
* **Location:** `4H.zones.BUY_2` → `4H.zones.BUY_1` **around** the prior `4H.inactive.H_BOS`.
* **Trigger:** **`TTF_H_MSB`** after a stop-run into the zone with **absorption SHVC** and CVD turn; reclaim the nearest 1H ST-EMA to confirm.
* **Invalidation:** 1H close **below** the BOS base / `4H.zones.BUY_1`.
* **Setup Priority:** **A-**

---

### **GREEN_A — Long breakout & retest**

* **Context:** Continuation if buyers clear the range top.
* **Location:** Clean break **above** `1H.major.H_MAJOR` / `4H.major.H_MAJOR` with nearby targets at `1D.poc.POC_4` → `1D.poc.POC_3`.
* **Trigger:** **`1H_H_BOS` + bullish HVC** → buy the **low-volume retest** with `LTF_H_MSB/BOS` and rising CVD.
* **Invalidation:** Failure retest (acceptance back **below** `4H.major.H_MAJOR`) or immediate **`1H_L_CHOCH`** against.
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