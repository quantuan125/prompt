# CONTEXT: 
## TRADER CONTEXT: 
Today: Today is Thursday 15th of January 2026, we are 30 minutes before US session. We have no major macro data released today. Refers to `MACRO CONTEXT` for the rest of the macro events this week.  

Last month: Marked the end of Quantitative Tightening cycle from the FED and market was reacting to 25bps rate cut from FOMC. Holiday season and low volume/liquidity environment toward the end of the year. 

This week: A return back from holiday season. 

Directive: Price is bearish on weekly timeframe however caution due to daily bullish breakout after multi-week consolidation at monthly support/demand zone.

Sentiment: With price action last quarter that have liquidated millions of leveraged crypto traders and enact fears, the general consensus is bearish with hypothesis of the top for the cycle is already set for BTC, and the start of an extended bear market into 2026. `Fear & Greed Index` improve since last month from around 14-20 (EXTREME FEAR) toward 26-40 (FEAR/NEUTRAL) in the current week.  

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
      POC_4: 87.5
      POC_5: 84.2
    zones:
      BUY_2: 89.5
      BUY_1: 73.7
    inactive:
      H_BOS: 109.6

  1W:
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
      POC_1: 101.7
      POC_2: 94.4
      POC_3: 91.4
      POC_4: 67.4
    zones:
      SELL_1: 114.9
      SELL_2: 106.1
      SELL_3: 98.1
      BUY_1: 85.5
    active:
      L_BOS: 107.3
    inactive:
      L_MSB: 111.9
      H_FSB: 124.5

  1D:
    major:
      H_MAJOR: 94.8
      L_MAJOR: 89.3
    sr:
      SR_1: 93.4
      SR_2: 89.5
      SR_3: 88.4
    poc:
      POC_1: 102.0
      POC_2: 92.5
      POC_3: 90.2
      POC_4: 84.6
      POC_5: 79.7
    zones:
      BUY_1: 88.5
      BUY_2: 91.8
      BUY_3: 93.6
    session:
      PDH: 97.9
      PDL: 94.6
    active:
      H_BOS:: 96.5
    inactive:
      H_BOS:: 90.6

  4H:
    local:
      L: 95.8
    major:
      H_MAJOR: 97.9
      L_MAJOR: 90.1
    sr:
      {}
    poc:
      POC_1: 96.8
      POC_2: 95.5
      POC_3: 93.8
      POC_4: 92.0
    zones:
      BUY_1: 93.5
      BUY_2: 95.0
    active:
      H_BOS: 92.5
    inactive:
      H_CHOCH: 91.6

  1H:
    major:
      H_MAJOR: 97.2
      L_MAJOR: 95.8
    sr: {}
    poc: {}
    zones:
      SELL_1: 97.1
      BUY_1: 96.1
    active:
      H_CHOCH: 96.6
    inactive:
      L_FSB: 96.2

  15m:
    major:
      H_MAJOR: 88.3
      L_MAJOR: 86.6
    sr: {}
    poc: {}
    zones:
      {}
    active:
      H_BOS: 87.8
    inactive: 
      L_FSB: 87.4
```

### **Weekly (1W – Super-HTF Structure)**

* **Previous (~30 candles):** Post late-’24 `1M_bullish_channel`, weekly momentum degraded after `1W.inactive.L_MSB` (distribution below `ALL.ath` / `1M.major.H_MAJOR`). An ATH probe/failure at `1W.inactive.H_FSB` preceded the capitulation leg that ultimately confirmed `1W.active.L_BOS` (trend continuation lower in the weekly bearish leg). The selloff broke down through the bull-support band around `1W.poc.POC_1` / `1W.sr.SR_2` and rotated into `1M.zones.BUY_2` then deeper toward `1M.poc.POC_4` / `1M.sr.SR_4`, base forming above `1W.major.L_MAJOR`. Key VPA note from your history: series of `1W_bearish_trend_VC`/`1W_bearish_impulse_HVC` supported by `1W_9/21EMA` bearish alignment + weak `1W_RSI` regime.
* **Current (~5 candles):** Recovery leg is now retesting overhead weekly LVN supply `1W.zones.SELL_3` (**~98.1k**) with the next magnet/ceiling being `1W.poc.POC_1` (**~101.7k**) then `1W.sr.SR_2` (**~100.9k**). Current developing candle prints as `1W_bullish_recovery_VC` (vol ratio ~0.55x 20MA), with price **above** `1W_M_VWAP` (~93.1k) and **above** `1W_9EMA` (~93.6k) but still **below** `1W_21EMA` (~98.5k) / `1W_50EMA` (~97.6k). `1W_RSI` (~47) remains <50 → **HTF bias: neutral-bearish (counter-trend rally into supply)**.

---

### **Daily (1D – HTF for intraday)**

* **Previous (~30 candles):** Bottoming sequence at `1W.major.L_MAJOR` followed by basing within the monthly demand region (`1M.zones.BUY_2`) and then range expansion higher. Your key turning candle remains the `1D_bearish_hammer_HVC` (absorption at the base with oversold `1D_RSI`), followed by reclaim(s) culminating in the more recent break with `1D.inactive.H_BOS` then `1D.active.H_BOS`. The rally is now challenging the overhead weekly supply `1W.zones.SELL_3` and pushing into the daily LT dynamic resistance `1D_200EMA/MA` region (still overhead vs spot).
* **Current (~5 candles):** Price is consolidating just under `1D.session.PDH` (**~97.9k**) while holding above `1M.poc.POC_3` (**~96.4k**) and well above `1D.sr.SR_1` (**~93.4k**). Current developing candle is `1D_bearish_stall_VC` (vol ratio ~0.68x 20MA) with `1D_RSI` (~69) elevated (near overbought caution) and price still **below** `1D_200EMA` (~99.6k). Daily CVD on chart remains net negative (~-0.86M) despite the rally → **watch for distribution/regular divergence risk; require PA confirmation before fading**.

---

### **4H (4H – HTF for 1H)**

* **Previous (~30 candles):** Impulse phase confirmed `4H.active.H_BOS` and carried price through the daily breakout area, then extended into weekly overhead `1W.zones.SELL_3`. The advance was supported by your noted run of `4H_bullish_impulse_HVC` with momentum stretched (RSI previously >75) into the local peak at `4H.major.H_MAJOR`.
* **Current (~5 candles):** Pullback cooled into `4H.local.L` (confluence with `1H.major.L_MAJOR`) and is now stabilizing around the 4H HVN band (`4H.poc.POC_1` **~96.8k** ↔ `4H.poc.POC_2` **~95.5k**). Current developing candle reads `4H_bullish_rebound_VC` with **very low** relative volume (vol ratio ~0.36x 20MA) while price holds above `4H_9/21EMA` and above `4H_W_VWAP` (~94.3k). 4H CVD on chart remains net positive (~+1.38M) → **bullish structure intact, but capped by `4H.major.H_MAJOR` / `1W.zones.SELL_3` overhead**.

---

### **1H (1H – TTF)**

* **Previous (~30 candles):** Rejection from the HTF ceiling (`4H.major.H_MAJOR`) led to a controlled pullback that tagged demand `1H.zones.BUY_1` (**~96.1k**) and swept into `1H.major.L_MAJOR` (**~95.8k**) / `4H.local.L`. Recovery then reclaimed `1H_9/21EMA` and confirmed `1H.active.H_CHOCH` with CVD raising, but follow-through stalled into a LH sequence below `1H.major.H_MAJOR` + `1H.zones.SELL_1` (**~97.2k**).
* **Current (~5 candles):** Price is compressing under `1H.major.H_MAJOR` while balancing around `1H_S_VWAP` (~96.6k) and `1H_9EMA` (~96.7k). Current developing candle is `1H_bearish_pause_VC` (vol ratio ~0.54x 20MA). `1H_RSI` (~56) is neutral;  **bulls still in control structurally above `1H.zones.BUY_1`, but momentum is not cleanly confirming (needs CVD improvement on breaks).**

## MACRO CONTEXT
### LAST WEEK

* **US growth vs inflation mix:** Manufacturing stayed **in contraction** while services **re-accelerated**, keeping “soft-landing” hopes alive but leaving inflation risk in play.
* **Jan 5 — ISM Manufacturing PMI (Dec):** **47.9** (actual) vs **48.3** (exp) vs **48.2** (prior).
* **Jan 7 — JOLTS Job Openings (Nov):** **7.146M** (actual) vs **7.610M** (exp) vs **7.449M** (prior).
* **Jan 7 — ISM Services PMI (Dec):** **54.4** (actual) vs **52.2** (exp) vs **52.6** (prior).
* **Jan 9 — U. Michigan Sentiment (Jan prelim):** **54.0** (actual) vs **52.9** (prior). Inflation expectations: **1y 4.2%** (steady), **long-run 3.4%** (up from **3.2%**).
* **Jan 9 — US Jobs (Dec):** **+50k** payrolls (actual) vs **+60k** (exp) vs **+56k** (prior, revised). **Unemployment 4.4%** (actual) vs **4.5%** (prior). **Avg hourly earnings +0.3% m/m**; **+3.8% y/y** (vs **+3.5% y/y** prior).

### THIS WEEK

* **Political / policy volatility (Fed credibility risk):**

  * The Trump administration’s escalation around **Fed Chair Powell** (including reports of a criminal investigation / pressure) adds **policy-uncertainty premium** and can swing USD, yields, equities, gold, and crypto on headlines.
* **Trade / tech (risk + inflation channel):**

  * **Jan 15 — Trump announces a 25% tariff on select advanced/AI chips** (notably including specific high-end processors), a direct risk to semis/AI complex and a potential medium-term inflation/supply-chain narrative.
* **Key US data (with priors/expectations):**

  * **Jan 13 — CPI (Dec):**

    * **Headline CPI:** **+0.3% m/m** (actual) vs **+0.3%** (exp); **+2.7% y/y** (actual) vs **+2.7% y/y** (prior).
    * **Core CPI:** **+0.2% m/m** (actual) vs **+0.2%** (exp); **+3.1% y/y** (actual). *Note: late-2025 CPI comps were affected by the government shutdown / collection disruption; BLS referenced estimation for missing months.*
  * **Jan 14 — Retail Sales (Nov):**

    * **Headline:** **+0.6% m/m** (actual) vs **+0.4%** (exp) vs **-0.1%** (prior, revised).
    * **Ex-autos:** **+0.4%** (actual) vs **+0.3%** (exp) vs **-0.2%** (prior).
    * **“Core/control” sales:** **+0.4%** (actual) vs **+0.2%** (exp) vs **+0.1%** (prior).
  * **Jan 14 — PPI (Nov):**

    * **Headline PPI:** **+0.2% m/m** (actual) vs **+0.2%** (exp) vs **+0.1%** (prior); **+3.0% y/y** (actual) vs **+2.8% y/y** (prior).
    * **Core PPI:** **+0.2% m/m** (actual) vs **+0.2%** (prior); **+3.5% y/y** (actual) vs **+3.4% y/y** (prior).
  * **Jan 15 — Initial Jobless Claims:** **198k** (actual) vs **215k** (exp) vs **207k** (prior).
  * **Jan 15 — Existing Home Sales (Nov):** **4.35M SAAR** (actual) vs **4.21M** (exp); **+5.1% m/m** (implies prior month ≈ **4.14M** SAAR).
* **Fed / liquidity:**

  * **NY Fed Desk operations:** scheduled **>$55B** in purchases **Jan 15–Feb 12** (mix of reinvestments + reserve-management purchases), a notable near-term liquidity backdrop.
  * **Next major Fed catalyst:** **FOMC Jan 27–28** (press conference **Jan 28**).
* **Trading conditions / holidays:**

  * **Mon Jan 19 — Martin Luther King Jr. Day:** **NYSE closed**; **U.S. dollar fixed income** recommended **full close** → thinner liquidity around the long weekend (crypto still trades 24/7).

### MACRO ANALYSIS

**Today’s (Jan 15) setup:** This week delivered “**growth still hanging in + inflation not fully dead**” signals (CPI in-line but firm, PPI and retail sales stronger than expected, jobless claims lower than expected). That mix tends to **support USD and keep rate-cut urgency contained**, which is often a headwind for **SP500 duration/tech** and a mixed input for **gold** (inflation hedge vs real-yield pressure). Overlay that with **Trump–Powell/Fed-independence headlines** (volatility + potential credibility/term-premium effects) and **new AI-chip tariffs** (direct hit to semis/AI leadership + renewed supply-chain/inflation narrative), and cross-asset correlation risk rises: **equities and BTC can de-risk together on rates/headlines**, while **gold can catch bids on political/credibility risk even if yields are firm**. Add the **MLK Day liquidity hole** (Jan 19) and expect sharper intraday moves and faster regime flips.

#### OVERALL CROSS-MARKETS

* Base case is **higher headline-driven volatility**: inflation prints keep the Fed boxed in, while politics/trade injects tail risk.
* Watch for **rates-led risk-off** (SP500 ↓, BTC ↓) vs **credibility/fear-led hedging** (gold ↑, BTC can be two-way depending on “risk asset” vs “monetary hedge” framing).
* NY Fed purchase schedule is a **liquidity offset**, but it won’t “cancel” tariff/Fed-headline shocks.

#### BTC & ETH

* Near-term, BTC/ETH are most sensitive to **USD liquidity + risk sentiment** (often tracking equity/tech beta when rates spike).
* **Bullish channel:** liquidity support + any “Fed credibility” shock that increases demand for alternative stores of value.
* **Bearish channel:** stronger data → firmer rates/USD → de-risking, especially into thinner liquidity (pre-MLK).

# TRADING PLAN FOR 1H_TTF (Trigger • Location • Context)

**Environment note:** 1H/4H are bullish from the base, but 1W remains structurally bearish; treat this as **Market State 2 (Unaligned)** → no blind entries; demand **structure + VPA confirmation** per execution protocols. 

## SHORT

### **WHITE_A — Short continuation (breakdown path)**

* **Context**: Only valid if 1H momentum flips bearish (loss of `1H_S_VWAP` + `1H_9EMA` → then pressure through `1H.major.L_MAJOR`). Given 1W bearish backdrop, a clean breakdown can align with HTF flow **if** it comes with bearish ignition (HVC/SHVC) and worsening CVD (no “weak dip” shorts).
* **Location**: Breakdown/retest zone at `1H.major.L_MAJOR` (**~95.8k**) / `4H.local.L` with nearby magnets `4H.poc.POC_2` (**~95.5k**) then `1D.session.PDL` (**~94.6k**).
* **Trigger**: **Confirmed `1H_L_BOS`** below `1H.major.L_MAJOR` with `1H_bearish_ignition_HVC/SHVC`, then **low-volume retest** of the broken level + `15m_L_MSB` continuation.
* **Invalidation**: Reclaim and acceptance back above `1H.major.L_MAJOR` with `15m_H_MSB` (breakdown failed → stand down).
* **Setup Priority**: `B`

---

### **ORANGE_A — Short reversal (sweep above 4H top / weekly supply)**

* **Context**: Fade only if the market **fails** to accept above the HTF ceiling and bullish VPA weakens (stalling candles, rising sell pressure, CVD divergence). This is a reversal attempt at major supply; patience required.
* **Location**: Liquidity sweep zone into `4H.major.H_MAJOR` (**~97.9k**) → `1W.zones.SELL_3` (**~98.1k**) (also overlaps `1D.session.PDH`).
* **Trigger**: Wick/sweep above `4H.major.H_MAJOR` or into `1W.zones.SELL_3` then close back below (**`1H_bearish_reversal_VC`**), followed by **`1H_L_MSB`** (or clear `15m_L_MSB` → `1H_L_CHOCH`) with bearish CVD turn.
* **Invalidation**: Acceptance/hold above `1W.zones.SELL_3` with bullish ignition (then shorts are invalid).
* **Setup Type**: `2B - Anticipatory HTF Realign`
* **Setup Priority**: `A-`

---

### **PURPLE_A — Short fade (range-top failure under 1H high)**

* **Context**: If price repeatedly rejects `1H.major.H_MAJOR` on weakening bullish VCs while CVD bleeds, treat as range fade back toward 1H demand (do **not** short if break attempts are supported by ignition volume).
* **Location**: `1H.major.H_MAJOR` (**~97.2k**) as the range cap; mean-reversion magnets `4H.poc.POC_1` (**~96.8k**) then `1H.zones.BUY_1` (**~96.1k**).
* **Trigger**: Failed retest / double-top behavior at `1H.major.H_MAJOR` then `15m_L_MSB` with `1H_bearish_followthrough_VC` (ideally HVC) + CVD rolling over.
* **Invalidation**: 1H acceptance above `1H.major.H_MAJOR` (range breaks → abandon fade short).
* **Setup Priority**: `A-`

---

### **PINK_A — Short momentum counter-trend scalp (VWAP loss)**

* **Context**: Quick scalp only if price **loses and stays below** `1H_S_VWAP` + `1H_9EMA`, signaling intraday flow shift; keep expectations small unless `1H.major.L_MAJOR` breaks.
* **Location**: Under `1H_S_VWAP` (~96.6k) with downside pull targets `1H.zones.BUY_1` (**~96.1k**) then `1H.major.L_MAJOR` (**~95.8k**).
* **Trigger**: `15m_L_BOS/CHOCH` under VWAP, then retest failure of VWAP/EMA band with `1H_bearish_continuation_VC` (prefer HVC) + CVD down.
* **Invalidation**: Reclaim `1H_S_VWAP` with `15m_H_MSB` (momentum short invalid).
* **Setup Priority**: `B`

---

### **RED_A — Short break & retest (clean BOS below 1H range low)**

* **Context**: The higher-quality breakdown short: requires decisive sell commitment (ignition) through `1H.major.L_MAJOR`—otherwise you’ll get chopped in a range.
* **Location**: `1H.major.L_MAJOR` (**~95.8k**) / `4H.local.L` as the line-in-the-sand.
* **Trigger**: `1H_L_BOS` on `1H_bearish_ignition_HVC/SHVC` → **low-volume retest** from below → `15m_L_MSB/BOS` continuation.
* **Invalidation**: Immediate reclaim above `1H.major.L_MAJOR` (failed breakdown).
* **Setup Priority**: `B`

---

## LONG

### **BLUE_A — Long fade (defend 1H demand / range-low hold)**

* **Context**: Preferred long while 4H structure holds: pullbacks are currently low relative volume; buy only after confirmation that sell pressure is exhausted (no catching falling knives). Look for CVD to stop bleeding and turn up on reclaim.
* **Location**: `1H.zones.BUY_1` (**~96.1k**) → extension into `1H.major.L_MAJOR` (**~95.8k**) / `4H.local.L`.
* **Trigger**: Sweep/hold at demand printing `1H_bullish_reversal_VC` then **`15m_H_MSB`** back above `1H.zones.BUY_1`; best if reclaim also regains `1H_S_VWAP`.
* **Invalidation**: Acceptance below `1H.major.L_MAJOR` (defer to RED/WHITE short paths).
* **Setup Priority**: `A+`

---

### **TEAL_A — Long momentum scalp (hold above VWAP → break 1H high)**

* **Context**: Only if bulls keep price above `1H_S_VWAP` + `1H_9EMA` and volume supports the push (avoid buying a weak grind with negative CVD).
* **Location**: Break/accept above `1H.major.H_MAJOR` (**~97.2k**) with continuation potential toward `4H.major.H_MAJOR` (**~97.9k**).
* **Trigger**: `15m_H_BOS` → **`1H_H_BOS`** through `1H.major.H_MAJOR` with `1H_bullish_ignition_HVC`, then shallow/low-volume retest + `15m_H_MSB`.
* **Invalidation**: Failed break and acceptance back below `1H.major.H_MAJOR` (especially if VWAP also lost).
* **Setup Priority**: `B`

---

### **YELLOW_A — Long major reversal (deep pullback realign)**

* **Context**: Only relevant if 1H flips bearish and sells into deeper HTF demand; look for **stopping/absorption** (not continuation selling) + bullish divergence, then wait for **TTF confirmation**.
* **Location**: Confluence band `1D.session.PDL` (**~94.6k**) with `4H.zones.BUY_2` (**~95.0k**) as first response; deeper extension toward `1D.zones.BUY_3` (**~93.6k**).
* **Trigger**: After a sell climax (`1H_bearish_capitulation_SHVC` or clear absorption), require **`1H_H_MSB`** (trend death of the bearish leg) then first low-volume pullback; execute on `15m_H_MSB/BOS` alignment.
* **Invalidation**: Continued acceptance below `1D.zones.BUY_3` with persistent sell HVC (reversal thesis invalid).
* **Setup Priority**: `A`

---

### **GREEN_A — Long breakout (clear 4H top break & retest)**

* **Context**: Continuation only if breakout is **real** (ignition volume + CVD confirmation). Otherwise, `4H.major.H_MAJOR` / `1W.zones.SELL_3` is a classic bull-trap zone.
* **Location**: Break above `4H.major.H_MAJOR` (**~97.9k**) / `1D.session.PDH` into `1W.zones.SELL_3` (**~98.1k**).
* **Trigger**: `1H_H_BOS` above `4H.major.H_MAJOR` with `1H_bullish_ignition_HVC/SHVC` → **low-volume retest** holding `4H.major.H_MAJOR` → `15m_H_MSB/BOS` for AEZ.
* **Invalidation**: Failed retest (acceptance back below `4H.major.H_MAJOR`) or immediate `1H_L_CHOCH` after entry.
* **Setup Priority**: `B`

  
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

