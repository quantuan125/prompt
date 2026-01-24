# CONTEXT: 
You are a trading analyst and you are preparing the INITIAL SESSION CONTEXT BRIEF for this week trading session (19/12/2025). 

The attached images are ETH/USDT charts of the following timeframe respectively: 1M, 2W, 3D, 12H with 12H as Trading Time Frame and 2H/4H as LTF for execution. Additionally, we also attached the following TF for ETH/BTC: 1W, 1D
You may use the attached csv file for further extraction of values for indicators for the CURRENT (not closed) candle of the corresponding timeframe.

# GOAL:

* Complete the described tasks below using the provided "Key Levels" YAML block which acts as variable constants for referencing. The rules defined are as following: 
  - `active`: Refers to the latest and most significant price action signal. This may include `<H/L>_<SWEEP/BOS/MSB/CHOCH>`
  - `inactive`: Refers to past price actions signals. 
  - `zones`: <TF_SELL> and <TF_BUY> levels (refers to Low Volume Nodes which are supply & demand zones)

## KEY LEVELS 

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
          POC_2: 3123
          POC_3: 1827
        zones:
          BUY_2: 2750
          BUY_1: 2162
          NEUTRAL: 3173
        active: 
          H_FSB: 4095
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
          POC_4: 3063
          POC_5: 2640
        zones:
          SELL_1: 4220
          SELL_2: 3630
        active:
          L_CHOCH: 3437
        inactive:
          H_BOS: 2880

      3D:
        local: 
          H: 3242
          L: 2907
        major:
          H_MAJOR: 3448
          L_MAJOR: 2624
        poc:
          POC_1: 3436
          POC_2: 3192
          POC_3: 2958
          POC_4: 2828
        zones:
          SELL_1: 3672
          SELL_2: 3247
          NEUTRAL: 3037
          BUY_1: 2850
        active:
          L_CHOCH: 2908
        inactive:
          L_BOS: 3439
          H_FSB: 3242

      12H:
        major:
          H_MAJOR: 3031
          L_MAJOR: 2776
        zones:
          SELL_1: 2967
          NEUTRAL: 2903
        active:
          L_FSB: 2875
        inactive: 
          L_CHOCH: 3026

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
        local: 
          H: 0.03689 
        major:
          H_MAJOR: 0.03812
          L_MAJOR: 0.03095
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
          L_FSB: 0.03198
        inactive: 
          L_CHOCH: 0.03804

      1D:
        major:
          H_MAJOR: 0.03688
          L_MAJOR: 0.03265
        zones:
          SELL_1: 0.03581
          SELL_2: 0.03476
        active:
          L_FSB: 0.03308
        inactive: 
          L_CHOCH: 0.03392
```


# TASK 1: 
Generate a detailed technical context with description for each of the relevant trading timeframe as following attached images. This description must covers the history price actions, relevant indicators, key levels (PDH, POC, SR) swing structure levels (<TF>_H/L_MAJOR/MSB/CHOCH) and LVN/supply/demand zones (<TF>_BUY/SELL). 

## INSTRUCTION: 

* Add the following in respective order:

```
- Previous: Cover the last 30 candles
- Current: Covers the last 5 candles including current candle. 
```
* Use the resources sections to accurately understand the relevant indicators attched within the csv file. You must references these indicators in the final descriptions along with the trader given information.  
* Never mention a price level or zones without referencing the attached "Key Levels" variables to it. (e.g:  "Rejections at **~1185–1192k** supply" (WRONG), "Rejections at `3D.zones.SELL_1` supply at **~1185–1192k**" (CORRECT))
* Never reference a low TF variables in a high TF description. Only the opposite is true. (e.g: DO NOT reference `3D.zones.SELL_1` in a `2W_TF` technical description, but the opposite is allowed)
* Always reference candles type followng this format: `<TF>_<bullish/bearish>_<type>_<VC/HVC/SHVC>`. (e.g: `1W_bullish_engulfing_VC`)
* Always reference indicators following this format: `<TF>_<indicators>`. (e.g: `1W_20EMA`, `1H_ST-EMAs`, `1H_RSI-MA`)
* You must use and expand the following provided technical descriptions for each timeframes from traders with additional details based on the materials, context and images given:
  1) **ETH/USDT**: 
    - **1M**: Price is currently within a range of its major structure with `1M.zones.NEUTRAL` as mid range level. Earlier in the year, price swept the low at `1M.active.L_FSB` followed by a bullish leg that created the latest `1M.active.H_FSB` into `ALL.ath` area and is currently in its bearish leg down to retest the mid range level. 
    - **2W**: Strong impulsive rally from May 2025 from the bottom of the monthly range at `1M.major.L_MAJOR` with a confirmed `2W.inactive.H_BOS` into `ALL.ath` area. Price then pullback however unable to hold the broken monthly support at `1M.major.H_FSB` with a confirmed `2W.active.L_CHOCH` supported by two secutive `2W_bearish_VCs` of increasing with volume spike, pushing price below 2W_9/21 and is currently retesting the prior broken `2W.active.H_BOS` + `1M.zones.BUY_2` confluenced with the `2W_50EMA`. Price bounced from here to retested the broken `2W.active.L_CHOCH` level + `1M.zones.NEUTRAL` however got a rejected with the current developing is a 2W_bearish_inverted-hammer_VC and is still in the process of establishing a new major bottom.  
    - **3D**: Price was in a strong downtrend after the rejection at ATH area with a `3D.inactive.L_BOS` supported by a `3D_bearish_hammer_HVC` (highest volume in half a year) with bearish follow-through and OBV confirmation into `1M.zones.BUY_2` + `2W.active.H_BOS` zone where price found the bottom at `3D.major.L_MAJOR`. Price then recovered on low volume to retest the 2W broken level + `3D.zones.SELL_2` supply confluenced with the descending `3D_21EMA` but got rejected with a `3D.inactive.H_FSB`, topping at `3D.major.H_MAJOR` before rolling over below `3D.zones.NEUTRAL` mid range level with a confirmed `3D.active.L_CHOCH` toward the lower end of the 3D range. 
    - **12H**: Price was in a strong downtrend initiated after the `3D.inactive.H_FSB` at 3D supply zone with a confirmedd `12H.inactive.L_CHOCH` supported by `12H_bearish_engulfing_HVC`  into `3D.zones.BUY_1` demand where price bottomed at `3D.major.L_MAJOR` before confirming a `12H.active.L_FSB` as price is currently in its bullish leg up to retest `12H.zones.SELL_1` supply confluenced with the descending `12H_21EMA` within its range of major structure, above `12H.zones.NEUTRAL` mid range level. 
  2) **ETH/BTC**:
    - **1W**: After putting in a `1M.major.H_MAJOR`, price is currently in a pullback of the 1M bullish move up confirmed by the `1W.active.L_CHOCH` after unable to reclaim `1W_9EMA` and dropped further to retest the `1W.zones.BUY_2` with a `1W.active.L_FSB` to bottom a `1W.major.L_MAJOR` before rallying on lower volume to retest `1W.zones.NEUTRAL` + `1W.zones.SELL_2` supply. Price top locally at `1W.local.H` and currently rolling over  below the `1W.zones.NEUTRAL` mid range level and failing to reclaim `1W_9/21EMA` within the current range of its major structure. 
    - **1D**: After bottiming at `1W.major.L_MAJOR`, price was in a counter-trend rally into `1D.zones.SELL_2` supply, however topped out at `1D.major.H_MAJOR` and made a `1D.inactive.H_FSB` followed by a `1D.active.L_CHOCH` at a LH retest of `1W.zones.NEUTRAL` pivot on volume spike to now retesting the `1D.major.L_MAJOR` confluenced with the ascending 1D_200EMA/MA
   
## EXAMPLE: 

```
## TECHNICAL CONTEXT

### ETH/USDT
### **2W (Bi-Weekly – Super-HTF)**

* **Previous (≈30 bars):** Impulse from May ’25 confirmed `2W.active.H_BOS` **`2W.sr.SR_1` 2870** → rally into **`ALL.ath` 4956** / **`2W.major.H_MAJOR` 4950**. Pullback begins after tagging the ATH block; intermittent bids from **`2W.zones.BUY_2` 3538** and the **`1M.sr.SR_1` 3745** shelf.
* **Current (last 5):** Two-candle rotation held above rising `2W_9EMA` (~**3852**) and below `1M.active.H_MSB` **4095**; current bar sits **just under** 2W VWAP (~**3972**) with price **3948.6**. EMA posture bullish (9/21/50/200 all below price; 21≈**3395**, 50≈**2982**, 200≈**1745**). RSI **57.8** (>50). No 2W_H/L_MSB; macro still HH/HL while correcting toward **`2W.poc.POC_1` 4300** overhead / **`2W.poc.POC_2` 3338** below. Last confirmed signal remains `1M.active.H_MSB` **4095** as pivotal midline.

*(Candle refs seen: prior `2W_bullish_doji_VC` off `2W.zones.BUY_2`; current bar a small-spread neutral VC under MVWAP.)*

---

#### **3D (HTF for 12H)**

* **Previous:** Rejection under **`ALL.ath` 4956** forced a **`3D_descending_channel`**. Third breakout attempt set `3D.major.H_MAJOR` **4755**, failed, then **`3D.active.L_SWEEP` 3817** printed via `3D_bearish_hammer_HVC` (long lower wick) near **`3D.poc.POC_5` 3815**/**`3D.poc.POC_6` 3645**. Buyers defended the channel floor; mid remains **`3D.zones.NEUTRAL` 4095**.
* **Current:** Price **3948.6** sits **below** 3D EMA9/21 (≈**4064/4114**) but **above** EMA50/200 (≈**3771/3047**): short-term bearish inside HTF bullish. RSI **47.5** (<50, MA ~**52.3**). VWAPs: S≈**3940** (at price), W≈**3893** (support), M≈**4118** (resistance). Compression between **`3D.poc.POC_4` 4007** overhead and the sweep base **3817**. Top-of-channel/supply stack remains **`3D.zones.SELL_2` 4251 → `3D.zones.SELL_1` 4423**; demand **`3D.zones.BUY_1` 3540** lines up with **`2W.zones.BUY_2` 3538**.

---

#### **12H (Primary TTF)**

* **Previous:** Forming a **12H descending wedge**: LHs capped by 12H ST-EMAs/`12H_50EMA` (≈**4059**), HLs above **`12H.zones.BUY_1` 3675**. An earlier `12H.inactive.H_SWEEP` **4086** + inverted-hammer_VC at the wedge top preceded a **confirmed `12H.active.L_MSB` 3842**, then a HL near **`12H.major.L_MAJOR` 3710**.
* **Current:** Price **3948.6** sits **above** 12H EMA9/21 (≈**3917/3946**) but **below** 12H EMA50 (≈**4059**) and **below** 12H EMA200 (≈**3963**) ⇒ wedge compression. RSI **48.5** (<50, MA ~**45.2**). VWAPs: S≈**3939** & W≈**3906** below (support), M≈**4100** above. Pivot is **`12H.zones.NEUTRAL` 3909**; wedge cap and supply at **`12H.zones.SELL_1` 4010** beneath **`12H.major.H_MAJOR` 4112**.

---

### ETH/BTC
#### **1W (Weekly – Super-HTF)**

* **Previous:** Major base above **`1W.poc.POC_3` 0.03204**, then impulsive advance → test of **`1M.zones.SELL_2` 0.03956** / **`1W.poc.POC_1` 0.03895** and stall below **`1W.major.H_MAJOR` 0.04326**. A confirmed `1W.active.L_CHOCH` **0.03804** started a controlled pullback toward **`1W.zones.BUY_2` 0.03226**.
* **Current:** Close **0.03531** sits **below** W-EMA9 (~**0.03638**), **above** EMA21/50 (~**0.03401/0.03372**). RSI **54.9** (>50 but **below** its MA **63.3**). Weekly VWAP/S-VWAP ~**0.03560** slightly above price; Monthly VWAP **0.03571** caps. Bias: consolidative pullback while holding above **`1W.major.L_MAJOR` 0.03196**; failure opens **`1M.poc.POC_1` 0.03113**.

---

#### **1D (Daily – HTF for ETH entries)**

* **Previous:** Clean **1D descending channel** from **`1D.inactive.H_SWEEP` 0.03706**; `1D.active.L_MSB` **0.03529** kept the trend lower with bounces capped under **`1D.zones.SELL_1` 0.03611**.
* **Current:** Close **0.03531** sits **below** D-EMA9/21/50 (~**0.03562/0.03599/0.03639**), **above** EMA200 (~**0.03291**). RSI **43.0** (<50, MA **46.0**). S/W/M VWAPs (~**0.03532/0.03552/0.03562**) lean overhead resistance. Room to probe **`1D.major.L_MAJOR` 0.03476** / **`1W.poc.POC_2` 0.03677** ping-pong until a daily BOS/MSB resolves.

```

# TASK 2:
Please generate the trading plans following the 12H_TTF for today's session. Follows the instruction, format and examples below. 

## FORMAT:
For each plan describes the following with reference to their corresponding key levels not the full setup:
```markdown
### <COLOR>-<SLUG NAME>-<CONTENT>
* **Context**: Trade + Macro context, HTF Trends, volume/liquidity environment and indicators (CVD, MA/EMAs, RSI, VWAPs). You must described the context in detailed leading up to the price at location and trigger. 
* **Location**: HTF key levels, zones and indicators confluences
* **Trigger**: Price structure specific triggers + VPA requirements catalysts
* **Invalidation**: Hard invalidation context of the entire plan 
* **Setup Type**: `<ID> - <NAME>`
* **Setup Priority**: `<Priority Grade>`
```

## INSTRUCTION:
For today's session you must generate the following plans as minimum. You must skip plans with "NONE" description and you may generate additional trading plans for the 12H_TTF:
**SHORT**
- ORANGE_A: short reversal at 3D_SELL_2 supply with extension to 3D_H_MAJOR/3D_SELL_1 confluenced with the descending `12H_50EMA` + M_VWAP. Entry on a confirmed `TTF_L_MSB`
- PURPLE_A: Short fade with `H_FSB` at the top of 12H range at 12H_SELL_1 with extension to 12H_H_MAJOR/3D_NEUTRAL. Entry on a confirmed `LTF_L_MSB` at location. 
- PINK_A: short intraday momentum if price lost W_VWAP + 12H_9EMA and remains below `12H.zones.NEUTRAL`. Entry on a confirmed `LTF_L_BOS/MSB` with LTF bearish crossover of `LTF_9/21EMA`
- RED_A: short breakdown with confirmed 12H_L_BOS below `12.major.L_MAJOR` with strong TTF VPA signal. Entry on retest of the broken level with a confirmed `LTF_L_BOS/MSB`. 

**LONG**
- BLUE_A: fade long with `L_SWEEP` at 3D_L_MAJOR supported by RSI and OBV bullish divergences with weaken bearish VPA. Entry on a `TTF_L_FSB` followed by a confirmed `LTF_H_MSB`. 
- GREEN_A: long break and retest above `12H.major.H_MAJOR` level with confirmed 12H_H_BOS supported by strong TTF VPA signal. Entry on a confirmed `LTF_H_BOS/MSB` at location. 
- YELLOW_A: long reversal at 3D_BUY_1 with extension to 3D_L_MAJOR with TTF bullish divergence signal on RSI + OBV. Entry on a confirmed `TTF_H_MSB` with reclaim of bullish crossover on `12H_9/21EMA`.
- TEAL_A: counter-trend momentum long on intraday with price above W_VWAP + 12H_9EMA and sustain above `3D.zones.NEUTRAL` level. `Entry on LTF_H_BOS/MSB` with LTF bullish crossover of `LTF_9/21EMA`
   

## EXAMPLE: 

```
# TRADING PLAN FOR 1H_TTF (Trigger • Location • Context)

### **ORANGE_A1 — Short reversal at 3D supply cap**

* **Context:** Price broke above 12H wedge and approach the top of 3D down-sloping channel; price failed to reclaim 3D EMA9/21 with no bullish cross-over. Sub-avg volume; ETHBTC daily weak (< D-EMA50), so ETH underperforms on squeezes.
* **Location:** Top-of-channel **`3D.zones.SELL_2` 4251 → `3D.zones.SELL_1` 4423**.
* **Trigger:** **`LTF_L_MSB`** after a wick into location with **absorption SHVC** / bearish CVD.
* **Invalidation:** Acceptance above location, then flips 3D supply as demand zone. 
* **Setup Priority:** **A-**

---

### **ORANGE_A2 — Short after 12H confirms trend failure**

* **Context:** Same zone as `ORANGE_A1`, but require TTF confirmation. Prefer if ETHBTC stays capped under **`1D.zones.SELL_1` 0.03611**.
* **Location:** **`3D.zones.SELL_2` 4251 → `3D.zones.SELL_1` 4423**.
* **Trigger:** **`12H_L_MSB`** at the top band, then short the first **low-volume** retest from below.
* **Invalidation:** Close **above `3D.zones.SELL_1` 4423** with **ignition SHVC** and rising CVD.
* **Setup Priority:** **A**

---

### **PURPLE_A (active) — Fade the wedge top**

* **Context:** Price below `12H_50EMA` (~**4059**) and no bullish cross over of `12H_ST-EMAs`. Wedge rhythm favors selling rips.
* **Location:** **`12H.zones.SELL_1` 4010**, stretch test to **`3D.zones.NEUTRAL` 4095** and **`12H.major.H_MAJOR` (4112)**.
* **Trigger:** LTF **`L_MSB`** after a squeeze into **4010→4095**; prefer **bearish RSI/CVD divergence**.
* **Invalidation:** **`12H_H_MSB`** and acceptance `12H.major.H_MAJOR`.
* **Setup Priority:** **B+**

---

### **PINK_A — Intraday momentum short**

* **Context:** If price loses S/W-VWAP (≈**3936/3916**) and stays **below `12H.zones.NEUTRAL` 3909**, sellers control.
* **Location:** **`12H.zones.NEUTRAL` 3909** → magnets **`3D.poc.POC_5` 3815** / **`3D.active.L_SWEEP` 3817**.
* **Trigger:** **` LTF_L_BOS`** under **3909** with **ignition HVC** + falling CVD; add on failed VWAP retests.
* **Invalidation:** Reclaim **S/W-VWAP** and close **back above 3909**.
* **Setup Priority:** **B**

---

### **RED_A — Breakdown & acceptance below 12H demand**

* **Context:** Transition from corrective to distributive state.
* **Location:** **Clean break of `12H.major.L_MAJOR` 3710**; targets **`3D.zones.BUY_1` 3540 → `2W.zones.BUY_2` 3538**; stretch **`2W.zones.BUY_1` 3201**.
* **Trigger:** **`12H_L_BOS`** below **3710** with **ignition SHVC** and persistent bearish CVD; short the retest of 3710 from below.
* **Invalidation:** Swift reclaim **≥3710** with **H_MSB** and absorption.
* **Setup Priority:** **B**

---

### **BLUE_A — Fade long at wedge/base confluence**

* **Context:** Sub-avg sell volume into stacked demand; ETHBTC near **`1D.major.L_MAJOR` 0.03476** supports ETH defense.
* **Location:** **`12H.major.L_MAJOR` 3710 + `12H.zones.BUY_1` 3675**, aligned with **`3D.poc.POC_6` 3645**.
* **Trigger:** **`2H_H_MSB`** after a **manipulation SHVC** sweep through 3710/3675 and **close back inside**.
* **Invalidation:** **`12H_L_BOS`** below **3710** (see RED_A).
* **Setup Priority:** **B-**

---

### **GREEN_A — Breakout long (wedge resolves up)**

* **Context:** 3D squeeze resolves; need proof of trend realign.
* **Location:** **Break and retest of `12H.major.H_MAJOR` 4112**.
* **Trigger:** **`12H_H_MSB`** through **4112** with **ignition HVC** + rising CVD, then low-volume retest long.
* **Invalidation:** Failure back **below 4112** on bearish MSB.
* **Setup Priority:** **B**

---

### **YELLOW_A — Deep-dip reversal long (HTF demand)**

* **Context:** Capitulation probe into bi-weekly demand while 2W trend still up (above 2W EMA stack).
* **Location:** **`2W.zones.BUY_2` 3538 / `3D.major.L_MAJOR` 3439**; extension ladder **into `2W.zones.BUY_1` 3201** if flushed.
* **Trigger:** **Manipulation SHVC** into the band + **`12H_H_MSB`** back above the swept level; CVD basing/divergence preferred.
* **Invalidation:** 12H full acceptance **below** `3D.major.L_MAJOR`.
* **Setup Priority:** **A-**

---

### **TEAL_A — 2H momentum long on VWAP reclaim**

* **Context:** Intraday risk-on when session flow flips; price above 2H EMA ribbon and S-VWAP and sustain above `12H.zones.NEUTRAL`
* **Location:** **Reclaim S-VWAP** (~**3936**) and hold above **`12H.zones.NEUTRAL` 3909**; first targets **`12H.zones.SELL_1` 4010 → `3D.zones.NEUTRAL` 4095**.
* **Trigger:** `LTF_H_BOS` after VWAP reclaim with **ignition HVC** + rising CVD.
* **Invalidation:** Lose S-VWAP again and close **back below 3909**.
* **Setup Priority:** **B**
```

# RESOURCES: 

```
# LAYER 2: ANALYSIS FRAMEWORK

## Multi-Timeframe Hierarchy & Usage

- **Higher Timeframes (HTF)**: eg: 1H, 4H - Define overall trend direction, **major market structure (key swing points), and significant S/D zones (Bright Red/Green/Blue LVNs)**.
- **Trading Timeframes (TTF)**: eg: 15m, 5m - Identify **immediate trend/structure (BOS/CHOCH/MSB)**, map **relevant S/D Zones & LVN overlaps (Dark Yellow/Grey)**, observe price relative to **TTF EMAs/VWAP**, and pinpoint Potential Entry Zones (PEZs).
- **Low Timeframes (LTF)**: eg: 3m, 1m - Execute precise entries/exits **ONLY AFTER confirmation** which creates Actual Entry Zones (AEZs). Monitor for **structural breaks (MSB/CHOCH) against the position** as potential exit signals.

**Rule:** Each timeframe hierarchy should be **4x to 8x** to next level timeframe hierarchy. 

**Example**:
- Valid TFs setup: 4H_HTF/1H_TTF/15m_LTF 
- Invalid TFs setup: 4H_HTF/15m_TTF/1m_LTF

## Market Structure Hierarchy & Signals

- **Break of Structure (BOS)**: Break of **major swing high/low** signaling the continuation of the established trend. Identifiable by HH/HL in uptrend or LL/LH in downtrend.
- **Market Structure Break (MSB)**: Break of **major swing high/low** signaling the reversal of the established trend. Identifiable by the creation of a single LL during an uptrend (L_MSB) or a single HL during a downtrend (H_MSB). This is similar to Market Structure Shift (MSS) in ICT concept. 
- **Change of Character (CHOCH)**: Break of **minor swing structure** signaling potential for a deeper/complex pullback, consolidation, or the *start* of a potential reversal. Identifiable by a single L_CHOCH or H_CHOCH within the major swing structure AND candle range.

### **NOTE**:
- NEVER enter a trade if clear opposing structure (CHOCH/MSB) has just formed on the TTF against your intended direction without waiting for that structure to fail or realign.
- **Acknowledge Failed Structure:** Recognize that any structure breaks can fail or be a fakeout. A failure (e.g., price breaks a high then immediately closes back below) is often a strong signal in the opposite direction.

## VOLUME ANALYSIS FRAMEWORK

### VOLUME DEFINITIONS

- **High Volume (HVC)**: > 2x - 3x MA white cloud
- **Super High Volume (SHVC)**: > 5-10x MA white cloud
- **Decreasing Volume**: < 0.7x previous bar
- **Pullback Volume**: < 0.5x impulse leg average

### VOLUME PATTERN

- **Ideal Trend:** Higher/increasing volume on TTF trend moves; Lower/decreasing volume on TTF pullback moves. 
- **Pullback Nuance:** Low volume pullback is ideal, BUT **consider candle range**. Large range candles on low volume can indicate a *lack of opposing interest*, not necessarily exhaustion – use caution. **Crucially, compare pullback volume to the volume of the preceding impulse leg.** Significantly lower pullback volume is preferred.
- **Warning Sign:** Increasing volume during a pullback *against* the expected support/resistance level indicates opposing pressure.

Analysis of volume bars is always relative and should be in the context to the 20MA white cloud and within the area of interest. Volume should always be analyzed with price action candles and they often align (big body no wicks, big bar). If price and volume diverge (small body with wicks, big bar) must note and pay attention. Always refer to a pair of price candle and volume bar as a single Volume Candle (VC).  

### VOLUME SIGNALS

-  **Increasing/Decreasing Series of VCs**: Momentum increasing or decreasing of the price move. 
- **HVC**: Volume exceeding two or three times the 20MA (TTF) or 30MA (LTF) white cloud
- **SHVC**: Volume abnormally exceeding twice or above the HVC. Context is important as SHVC on LTF may just be a regular HVC on TTF. 
- **Ignition SHVC:** Large body, minimal wicks, closing strongly in trend direction, often breaking key level/zone. Confirm with strong aligned CVD. Signals commitment.
- **Stopping/Absorption SHVC:** Often long wicks, smaller bodies, occurring at key S/D zones. Price struggles to progress despite high volume. **Requires subsequent price action** (e.g., failure to follow through, reversal candle) and **CVD divergence** to confirm absorption. **Do NOT assume absorption prematurely.**
- **Manipulation SHVC:** Often associated with wicks grabbing liquidity beyond a range/level, sometimes on lower-than-expected volume for the range break. Followed by sharp reversal.

**Treat SHVC primarily as points of interest requiring confirmation from subsequent price action and VPA.** An SHVC *against* your intended trade direction (e.g., high volume selling into your demand zone entry) is a **major red flag** requiring exit or avoidance. **Trading pullbacks into SHVCs (after confirmation) is valid**: e.g., pullback to support after a bullish ignition SHVC.

### VOLUME PROFILE ANALYSIS

#### Low Value Nodes (LVNs)

Areas where there is an overlap between short term and long term LVN zones have different strengths in terms of supply/demand zones. For example: an overlap of green area and dark yellow area is stronger than the overlap of blue area and grey area.

- **LVN Overlaps**: Strongest confluence (e.g., LT Demand + ST Demand).
- **LVN Edge Test:** Price action at the *edge* of an LVN is often critical. Rejection or acceptance here provides clues.

**LVN COLOR CLASSIFICATION**:
- **Bright Red Area**: Long Term Significant Supply Zone/Resistance LVN - major institutional selling area
- **Bright Green Area**: Long Term Significant Demand Zone/Supporting LVN - major institutional buying area
- **Blue Area**: Long Term Swap Zone - less significant supply and demand LVN with potential for role reversal
- **Grey Area**: Short Term Swap Zone
- **Dark Yellow Area**: Short Term Significant Supply/Demand Zone

#### High Value Nodes (HVNs)

- POCs at HVNs are often points of key resistance and support levels and therefore primary TP areas. 
- The strength of the POC is identified based on the timeframe they are marked with. For example: 1D-POC > 4H-POC > 1H-POC > 15m-POC. 
- Be careful with entry around the POC levels as they are often strong points of retest and rejection levels.

### Cumulative Volume Delta (CVD) Analysis

- **Core Principle:** CVD slope and highs/lows should ideally **confirm price action's slope and highs/lows** in a healthy trend.
- **Confirmation:** Use rising CVD to confirm bullish breakouts/trends; falling CVD for bearish.
- **Divergence (Warning):**
  - **Regular Divergence:** Price HH, CVD LH (potential topping); Price LL, CVD HL (potential bottoming). **Requires Price Action confirmation (CHOCH/MSB) before acting.**
  - **Hidden Divergence:** Price HL, CVD LL (potential bullish continuation); Price LH, CVD HH (potential bearish continuation). Can support trend entries.
  - **Absorption:** Price pushes into S/D zone with strong counter-trend CVD (e.g., price falls to demand zone with sharply rising CVD) but price stalls/reverses -> signals absorption.
  - **Sharp Turns/Slope Change:** A sudden, sharp reversal in CVD slope can precede price reversal or indicate exhaustion/strong counter-pressure. 

# LAYER 3: EXECUTION PROTOCOLS

The valid setups for execution are determined by the Market State, as identified by the TSI Protocol and are outlined in the reference table below.

<br>

| **Setup ID** | **Setup Name** | **Market State** | **Priority** | **Core Concept** | **Trigger Signal** |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1A** | Confirmed Pullback | 1: Aligned Trend | A+ | Buy the dip/Sell the rip in a strong trend. | LTF-MSB (Realigning) |
| **1B** | Swing Pullback | 1: Aligned Trend | B+ | Limit order entry in a clear and runaway trend. | TTF-BOS (Limit Order) |
| **1C** | Momentum Ignition | 1: Aligned Trend | B | Join a confirmed, ongoing impulse wave. | LTF-BOS (Continuation) |
| **1D** | Confirmed Major Reversal | 1: Aligned Trend | A- | Trade the first pullback after a trend dies. | **TTF-MSB** (Against Trend) |
| **1E** | Climactic Reversal | 1: Aligned Trend | B- | "Knife-catch" a parabolic exhaustion move. | LTF-MSB (at HTF Level) |
| **1F** | Range Fade with Bias | 1: Aligned Trend | B+ | Buy failed breakdowns/Sell failed breakouts. | LTF-MSB (Back into Range) |
| **2A** | Confirmed Counter-trend Pullback | 2: Unaligned Trend | B | Counter-trend scalp with the TTF flow. | LTF-MSB (Realigning) |
| **2B** | Anticipatory HTF Realign | 2: Unaligned Trend | A- | Fade the weak TTF trend at a key zone. | LTF-MSB (Against TTF Trend) |
| **2C** | Confirmed HTF Realign | 2: Unaligned Trend | A | Trade the pullback after the TTF trend dies. | **TTF-MSB** (Against TTF Trend) |

<br>

## MARKET STATE 1: ALIGNED TREND (TYPE A ENVIRONMENT)

- **Definition:** TTF trend is aligned with the HTF trend (e.g., 15m uptrend within a 1H/4H uptrend).
- **TTI Check:** HTF and TTF OVERALL-ASSESSMENT are aligned and trending (BULLISH or BEARISH).
- **Mindset:** Confident aggression. We trade with the primary institutional flow.

### CONTINUATION SETUPS (Primary)

#### **Setup 1A: CONFIRMED PULLBACK (A+)**

- **Description:** The primary, high-confirmation entry. Enter on a pullback to a key TTF zone after an LTF signal confirms the trend is resuming.
- **Location:** Pullback into a high-confluence TTF zone (S/R flip, demand/supply, LVN, Fib levels).
- **VPA:** Pullback occurs on lower, ideally decreasing, volume compared to the preceding impulse leg.
- **Trigger:** An LTF-MSB that realigns with the HTF/TTF trend.
- **Action:** Enter on a low-volume test of the zone created by the LTF-MSB, or on the subsequent LTF-BOS.
- **SL/TP:** Tight SL below the LTF swing structure + LTF ATR. TP targets major TTF/HTF levels.
- **Management:** PROACTIVE

#### **Setup 1B: SWING PULLBACK (B+)**

- **Description:** A "blind" limit order entry at a deep PEZ, used only in exceptionally strong, one-sided trends.
- **Context:** Permissible ONLY when the preceding TTF-BOS was driven by clear ignition HVC/SHVC.
- **Location**: High-confluence TTF zone that is at or below the 61.8% retracement level. 
- **VPA:** The pullback must be visibly weak on low and ideally decreasing volume. Any strong counter-VPA or LTF price signal invalidates the entry. 
- **Trigger:** TTF-BOS (Limit Order).
- **Action:** Place a limit order at the pre-defined location. 
- **SL/TP:** Wider SL below the major TTF swing structure + TTF ATR. TP aims for significant trend continuation.
- **Management:** NON-PROACTIVE

#### **Setup 1C: MOMENTUM IGNITION (B)**

- **Description:** Second entry to join a runaway market that has already resumed its trend and is not providing deep pullbacks.
- **Context:** The primary (1A) entry was missed after a confirmed pullback and now price is resuming its trend.
- **VPA:** Strong and sustained volume with momentum confirmation on the impulse wave.
- **Trigger:** An LTF-BOS that continues the impulse after a recent LTF realignment signal (MSB).
- **Action:** Enter on the LTF-BOS or its immediate, shallow retest.
- **SL/TP:** Tight SL below the minor LTF low preceding the LTF-BOS. TP is the same as the 1A setup.
- **Management:** PROACTIVE

### REVERSAL SETUPS 

#### **Setup 1D: CONFIRMED MAJOR REVERSAL (A-)**

- **Description:** Trading a full reversal of the aligned trend. This requires a confirmed trend death at the TTF level.
- **Location:** Occurs at or after testing a major HTF S/R zone.
- **Trigger (Mandatory):** A decisive **TTF-MSB** against the established trend, confirmed with high volume.
- **Action:** Wait for a low-volume pullback to the S/R flip created by the TTF-MSB, then seek an LTF entry signal.
- **SL/TP:** SL above/below the TTF swing point that formed the TTF-MSB. TP targets opposing HTF levels.
- **Management:** NON-PROACTIVE

#### **Setup 1E: CLIMATIC REVERSAL (B-)**

- **Description:** "Knife-catching" a parabolic/capitulation move. High-risk, requires extreme exhaustion conditions.
- **Location (Mandatory):** A pre-defined, major HTF support/resistance level (e.g., Daily, Weekly).
- **Context:** TTF trend is visibly parabolic, with the TTF RSI deeply oversold/overbought (<20 or >80). Must see a clear stopping/absorption **TTF-SHVC** at the HTF level. Divergence is ideal.
- **Trigger:** An initial LTF-MSB after a stopping volume climax.
- **Action:** Enter on the pullback after the LTF-MSB.
- **SL/TP:** SL below the absolute low/high of the capitulation move + generous TTF ATR buffer. TP1 is the nearest significant TTF level.
- **Management:** NON-PROACTIVE

### CONSOLIDATION SETUPS 

#### **Setup 1F: RANGE FADE WITH BIAS (B+)**

- **Description:** Trading within a TTF range with a directional bias aligned with the primary HTF/TTF trend.
- **Context:** In a bullish trend, **only** buy a failed breakdown (liquidity sweep) of the range low. In a bearish trend, **only** short a failed breakout of the range high.
- **Trigger:** A liquidity sweep of a range boundary, followed by an LTF-MSB back into the range.
- **Action:** Enter after the LTF-MSB confirms the failed breakout/down.
- **SL/TP:** SL just outside the liquidity sweep wick + LTF ATR. TP targets the range POC and opposing boundary.
- **Management:** NON-PROACTIVE

## MARKET STATE 2: UNALIGNED TREND (TYPE B ENVIRONMENT)

- **Definition:** TTF has a clear trend, but it opposes the HTF trend, or the HTF is range-bound.
- **TTI Check:** TTF OVERALL-ASSESSMENT is trending, but HTF is opposite or neutral.
- **Mindset:** Cautious and nimble. Assume the TTF trend is temporary. Prioritize profit-taking.

### CONTINUATION SETUPS 

#### **Setup 2A: CONFIRMED COUNTER-TREND PULLBACK (B)**

- **Description:** The only acceptable way to trade *with* the unaligned TTF trend. Requires full confirmation. Blind entries are **forbidden**.
- **Location:** Entry cannot be directly into a major HTF S/D zone that aligns with the HTF trend.
- **VPA:** Pullback should be on weaker volume than the TTF impulse leg.
- **Trigger (Mandatory):** A high-confirmation **LTF-MSB** that realigns with the TTF trend.
- **Action:** Enter on the pullback after the LTF-MSB.
- **SL/TP:** Tight SL below the LTF swing structure. **Primary TP is the last significant TTF swing high/low.**
- **Management:** PROACTIVE

### REVERSAL SETUPS 

#### **Setup 2B: ANTICIPATORY HTF REALIGNMENT (A-)**

- **Description:** Anticipating the failure of the weaker TTF trend. We enter on an LTF signal that realigns with the stronger HTF trend/consolidation.
- **Location:** Ideally at a logical TTF resistance/support area (e.g., Fib level, LVN, key EMA).
- **Context:** The TTF trend shows signs of exhaustion (VPA/CVD divergence, stalling momentum). A liquidity sweep of a TTF high/low must occur before entry.
- **Trigger:** An LTF-MSB against the TTF trend.
- **Action:** Enter on the pullback after the LTF-MSB.
- **SL/TP:** Tight SL above/below the LTF swing high/low. Primary TP is the opposing TTF swing point.
- **Management:** PROACTIVE

#### **Setup 2C: CONFIRMED HTF REALIGNMENT (A)**

- **Description:** The highest confirmation setup. The unaligned TTF trend has officially failed with a **TTF-MSB**. We enter on the first pullback to join the HTF trend/consolidation. 
- **Trigger (Mandatory):** A decisive **TTF-MSB** or major **TTF-CHOCH** that breaks the unaligned TTF trend.
- **Action:** Wait for the first low-volume pullback to the newly created S/R flip zone. Enter on a confirming LTF trigger.
- **SL/TP:** SL above/below the swing point that formed the TTF-MSB. With TTF realigned, we can now target major HTF structural levels.
- **Management:** NON-PROACTIVE

## MARKET STATE 3: TIGHT CONSOLIDATION/INDECISION

- **No-Trade Condition:** If both the HTF and TTF are in clear, ranging consolidations (TTI OVERALL-ASSESSMENT: NEUTRAL), we **STAND ASIDE**. This is a low-probability environment. We wait for a breakout to define a new market state.

### ENTRY-EXIT RULES

#### Entry Criteria

- Entry must be at the outlined PEZ from the trading plans of the TTF, do not chase price at LTF. 
- All AEZ entry must require structural confirmation supported by volume and CVD in favor of the direction we enter
- Always prioritize AEZ entry with low-volume pullback of 50% Fib retracemenet or below.

#### Take Profit Levels

- Primary: POCs, Support Resistances (SRs), significant opposing LVNs, key structural levels (prior swing highs/lows).
- Use VPA/CVD slowing/divergence near targets to **confirm exit timing**. Don't exit solely on level proximity if momentum is strong.

#### Stop Loss Placement & Management

- **Initial Placement:** Beyond the TTF structural point invalidating the setup (e.g., below reversal low for long, above rejection high for short). Ensure it's beyond the key LVN/zone edge. Use ATR for buffer.
- Any SL placed at LTF structural points is a momentum trade and is treated as risky, clearly clarify this risk. 

#### Take Profit Strategy

- Set primary targets based on structure/POCs/SRs/LVNs before entry.
- Monitor VPA (volume pattern, CVD behavior) as price approaches targets to decide whether to exit fully, partially, or trail stop loss.
- Always prioritize the following type of levels as targets with higher timeframe as more significant: POC > SR > LVN > Major Structure > Minor Structure 


# LAYER 4: SUPPORTING INDICATORS

## INDICATOR VALUE TABLES

The .csv attached contains supporting indicators' values and special deltas for all relevant timeframes is used to identify the TTI.
If a value does not appear or is "None" within a field they are irrelevant for the analysis of that timeframe. If a relevant indicator's value cannot be identified or missing, explicitly raise warning and do not hallucinate the value.
For rows with the latest time identified are values of the current candle for that timeframe which has not been closed yet. 
NOTE: 
- all values in "tf" fields are type "string". 
- always sort the "time" value first before row selection 

### PRIMARY

Use for TTI for relevant timeframes within the discussion.   

### SECONDARY

Identify whether an indicator is a potential support or resistance based on the delta and how extended it is based on delta values.

### TERTIARY

Use for any "CODE EXECUTION" tools as desired to perform further VPA or trend analysis on a given timeframe. 

## MOVING AVERAGES

Values are denoted on the INDICATOR VALUE TABLES. The following are included:
- LT (Long-term) trend: 200 EMA (dark blue) + 200 SMA (pink)
- MT (Medium) trend: 50 EMA (light green)
- ST (Short-term) trend: 9 EMA (red) + 21 EMA (yellow)

### PRIMARY

Use for TTI with more weights over LT-MAs. Pay special attention to the deltas to determine the strength of the trend. 

**Example:**
- BEARISH: ALL MAs value > price with large deltas on LT-MAs. 
- BEARISH*: LT-MAs > price > ST-MAs (with large deltas)
- NEUTRAL-BEARISH:  LT-MAs > price ≥ ranging ST-MAs (with small deltas)
- NEUTRAL: ranging LT-MAs (with small deltas) = price 

### SECONDARY

Use for **dynamic S/R context** and **confirmation** with higher weights on LT-MAs based on the delta values

### TERTIARY

Use for determining the strength of the trend based on the cross over signals of the following pairs:
- 9 and 21 EMA 
- 50 and 200 EMA 

This can be determined by the deltas. If unclear then always ask for this information. 

## VWAPs

Values are denoted on the INDICATOR VALUE TABLES. The following are included:
- (Session) S_VWAP (teal): ONLY relevant for 1H_TF and under
- (Weekly) W_VWAP (blue): ONLY relevant relevant for 1H_TF, 4H_TF and 1D_TF
- (Monthly) M_VWAP (dark green): ONLY relevant for 4H_TF and above  

### PRIMARY

Use for TTI with more weights over ST-VWAPs. Pay special attention to the deltas to determine the strength of the trend. 

**Example Identification:** 1H_TTF/15m_LTF/4H_HTF

<1H> - Relevant VWAPs: S_VWAP and W_VWAP
- BEARISH: ALL VWAP > price
- BEARISH*: S_VWAP > price > W_VWAP. 
- NEUTRAL-BEARISH:  S_VWAP (smaller delta) > price 
- NEUTRAL: ranging S_VWAP (small deltas) = price 

### SECONDARY

Use for **dynamic S/R context** and **confirmation** with higher weights on ST-VWAPs based on the delta values

## RSI

Values are denoted on the INDICATOR VALUE TABLES and can be found on the first indicator box with purple and yellow lines below the actual chart. 

### PRIMARY

Use for TTI based on the value of the RSI (purple) and RSI_MA (yellow) based on the level 50

**Example:**
- BULLISH: RSI = 60, RSI_MA = 55, 
- BULLISH*: RSI = 60, RSI_MA = 44
- NEUTRAL: RSI = 52, RSI_MA = 49
- NEUTRAL-BULLISH: RSI = 55, RSI_MA = 60

### SECONDARY

Use for **divergence** signals as potential warnings (requires PA/VPA confirmation). Only consider this when value is coming from above 70 or below 30. Always note this in the analysis if RSI is showing extension in the overbought/oversold territory as a cautionary signal. 

## CVD

Values can be found on the second indicator box below the RSI indicator box with green (positive net value) or red (negative net value) 

### PRIMARY

Use for CONFIRMATION and DENIAL for confirmation of price movements along with market structure and regular volume when making trading actions such as entry, exit or hold. 

### SECONDARY

Use for spotting potential regular divergences or hidden divergences/absorption. More context will often be given regarding this usage.  

### TERTIARY

This net value should provide bias for the day. We use the 1000, 500 and 100 as values for benchmarking the bias (however this is not part of the TTI). 

**Example:**
- BULLISH: value > 1000
- BULLISH*: 1000 > value > 500
- NEUTRAL-BULLISH: 500 > value > 100
- NEUTRAL: 100 > value > -100 

# INSTRUCTION

Always follow the CORE PRINCIPLES (MANDATORY PROTOCOLS) and the RULES defined when formulating analysis and responses. Prioritize A+ setups with clear confluence across **Location (Key Zone), Structure (Aligned Trend/Trigger), and Confirmation (Converging VPA + EMA signals).** Be explicitly critical and avoid setups lacking clear confirmation or with ambiguous targets. 

DO NOT HALLUCINATE DATA AND INFROMATION. IF YOU DO NOT HAVE SUFFICIENT INFORMATION FOR ANALYSIS, STATE THAT EXPLICITLY OR ASK FOR MORE INFORMATION. As a mentor and advisor, you have to always be brutally honest and any opposite opinions are welcome. 
```

# NOTE:
- "master.csv" - data on ETH/USDT pair
- "master - Copy.csv" - data on ETH/BTC pair
- think hard.




