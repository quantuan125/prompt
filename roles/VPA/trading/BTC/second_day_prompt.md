# CONTEXT: 
You are a trading analyst and you are preparing the INITIAL SESSION CONTEXT BRIEF for today's trading session (07/10/2025).  

The attached images are charts of the following timeframe respectively: 1D, 4H, 1H, 1H(with trading plans) 
You may use the attached csv file (master_dup.csv) for further extraction of values for indicators for the CURRENT (not closed) candle of the corresponding timeframe.

# TASK 0
Prepare, organize and expand the yaml "Key Levels" for today current session.

## INSTRUCTION
* Use the provided today's key "Key Levels" section which acts as variable constants for referencing which should include: 
   - INACTIVE LEVELS: Refers to the latest and most significant Break of Structure (BOS) and Market Structure Break (MSB) of the relevant TF. 
  - ACTIVE LEVELS: Swing levels, SR, POC, PDH/PDL, etc.. 
  - ACTIVE ZONES: <TF_SELL> and <TF_BUY> levels (refers to LVNs which are supply & demand zones)
* Organize the levels and zones in the correct subcategory. 
* Retain consistent format and round up with "k" for approximation (e.g: 117.2k) and use "-" for ranges (e.g: 113.5-113.9k)
*  Only expand variables and their value if needed. 
* DO NOT HALLUCINATE KEY LEVEL VALUES: if there are constant values you are unsure of just keep the brackets value empty and the trader will filled them manually themselves. 

### KEY LEVELS

```yaml
meta:
    pair: BTCUSDT
    units: "k"   # all numbers rounded with 'k'
    note: "Ranges use '-', e.g., 113.2-114.7k"

  ALL:
    ath: 126.2k

  1M:
    major: {}
    sr: {}
    poc:
      POC_1: 118k
      POC_2: 104.7k
    zones: 
      BUY_1: 90.0k
      BUY_2: 100.2k
    inactive:
      H_BOS: 109.6k

  1W:
    major:
      H_MAJOR: 126.2k
      L_MAJOR_2: 108.7k
      L_MAJOR_1: 107.3k
    sr:
      SR_1: 117.2k
      SR_2: 119.4k
      SR_3: 108.3k
    poc:
      POC_1: 115.6k
      POC_2: 111.2k
      POC_3: 109.4k
    zones:
      SELL_1: 124.5k
      BUY_1: 106.5k
      NEUTRAL: 116.8k
    active:
      H_SWEEP: 124.5k
    inactive:
      L_MSB: 111.9k
      H_CHOCH: 117.9k

  1D:
    major: 
      H_MAJOR: 126.2k  
      L_MAJOR_1: 109.6k  
      L_MAJOR_2: 102k  
    sr: 
      SR_1: 113.3k
      SR_2: 112k
      SR_3: 114.3k
      SR_4: 123.2k
      SR_5: 121.3k
    poc:
      POC_2: 121.7k
      POC_1: 113.0k
    zones:
      SELL_1: 120.1k
    session:
      PDH: 115.8k
      PDL: 109.5k
    active: 
      L_CHOCH: 113.9k
      L_SWEEP: 108.6k
    inactive:
      H_MSB: 114.0k


  4H:
    local: 
      H: 115.6k
    major:             
      H_MAJOR: 112.6k    
      L_MAJOR: 109.5k    
    sr:
      SR_1: 116.4k
    poc: 
      POC_1: 115.3k
    zones:
      BUY_1: 109.0k
      SELL_1: 116.0-118.1k
    active:
      L_BOS: 119.7k
    inactive: 
      H_SWEEP: 121.9k

  1H:
    major:
      H_MAJOR: 115.6k
    sr: {}
    poc: {}
    zones:
      SELL_1: 114.8k
      BUY_1: 111.1k
      BUY_2: 112.6k
    active:
      L_BOS: 114.4k
    inactive: 
      L_MSB: 114.7k
      H_MSB: 112.5k
```


# TASK 1:
Generate a brief description of the technical context for each relevant trading timeframe which shows the development from yesterday (06/10/2025) and today. 

## INSTRUCTION: 

* Add the following in respective order to your descriptions

```
* **General:**: Brief techincal context spanning last 30 candles. 
* **Yesterday (date):**: <description>
* **Today (date):**: <description>
```

* Use the resources sections to accurately understand the relevant indicators attched within the csv file. You must references these indicators in the final descriptions along with the trader given information.  
* Never mention a price level or zones without referencing the attached "Key Levels" variables to it. (e.g:  "Rejections at **~118.5–119.2k** supply" (WRONG), "Rejections at 4H_SELLs supply zone at **~118.5–119.2k**" (CORRECT))
* Never reference a low TF variables in a high TF description. Only the opposite is true. (e.g: DO NOT reference 4H_SELL in a 1W technical description)
* You must use and expand the TF technical descriptions with the following additional critical information from the trader:
  - **1D**: Price had initiated a bullish leg from the bottom of 1W range low uptoward the 1W range high/ATH zone with a confirmed 1D.inactive.H_MSB. Price then rolled over after wicking above ATH zone with a confirmed 1D.active.L_CHOCH followed by a 1D_bearish_HVC engulfing candle sell off and sweeped the 1W range low and bottomed at 1D.major.L_MAJOR_2 before absorbed and bounced strongly back inside the 1W range. Price recovered during the weekend with a 1D_bullish_VC inverted hammer candle just under 1W NEUTRAL. 
  - **4H**: Price after sweeping the ATH/1W_H_MAJOR level during recent bullish leg up, retraced and consolidated under this zones last week. Price then had a liquidition sell off last Friday initiate at 4H.active.L_BOS with a 4H_bearish_SHVC largest of the year down to 1D_L_MAJOR_2 level. Price then bounced and established a new 4H_L_MAJOR after bouncing toward 4H_SELL_1/4H_200EMA/MA supply zone and rejected here to establish a local 4H_H, confluenced with the descending 4H_21EMA. 
  - **1H**: Price recovered at PDL/1D_L_MAJOR_1/4H_L_MAJOR with a confirmed 1H.inactive.H_MSB into the mentioned 4H supply zone, however rolled over with a 1H.inactive.L_MSB after the rejcction at this area. Price is now in a 1H descending channel with the latest signal is a 1H_L_BOS. Price is currently squeezed between the 1H_50EMA from below as support and S_VWAP + the 1H_ST-EMAs descending from above but not yet rolled over. CVD for the session is negative which confirms this downtrend on the 1H so far.

## EXAMPLE

```
### **Daily (1D — HTF)**

* **General:** Last ~30 candles show a corrective pullback that based above **1W_POC** and rotated higher; price has reclaimed the **ST/MT EMAs** and is pressing the **1D_H_MAJOR/4H_H_MAJOR**/**PDH** cluster. Volume is mostly sub-average on the up-leg → watch for ignition before chasing.
* **Yesterday (17-Sep):** Pushed from **1D_POC_2 → PDH**, converting the mid into support and closing in front of **1D_H_MAJOR/4H_H_MAJOR** resistance.
* **Today (18-Sep):** Current candle is holding above the EMA stack and probing **PDH / 1D_H_MAJOR/4H_H_MAJOR** with **M_VWAP** below → HTF bias **bullish while above 1D_SR**. 

---

### **4-Hour (4H — HTF for 1H)**

* **General:** A sequence of **HH/HL** from the **4H_BUY** region, now trading above **W_VWAP** and the entire EMA stack, consolidating just under the **1D_H_MAJOR/4H_H_MAJOR / PDH** band and around **4H_POC**.
* **Yesterday (17-Sep):** Break and hold above **4H_POC** after a drive from the mid, tagging **PDH** and rejecting lightly.
* **Today (18-Sep):** Price sits above **W_VWAP** and **EMA50/200**, respecting **4H_POC** as intraday pivot; momentum positive but not accompanied by strong volume → need **Ignition HVC + rising CVD** to extend toward **1H_H_MAJOR → 1M_POC**. 

---

### **1-Hour (1H — TTF)**

* **General:** Clear 1H uptrend (**1H_H_BOS** now **inactive**) with price riding **S_VWAP** and ST-EMAs; trading between **4H_POC / PDH / 1D_H_MAJOR/4H_H_MAJOR** (support) and **1H_H_MAJOR / 1M_POC** (overhead supply).
* **Yesterday (17-Sep):** Sweep down into the mid, then **H_MSB** back above **4H_POC** and close near **PDH**.
* **Today (18-Sep):** Holding a tight bull flag **just above S_VWAP** and **4H_POC**, probing the **PDH / 1D_H_MAJOR** shelf; room above into **1H_H_MAJOR** and **1M_POC** if we get an **ignition**. 
```

# TASK 2: 
Please generate the trading plans following the 1H_TTF  for today's session. Follows the examples for format, structure and content (`<COLOR>-<SLUG NAME>-<CONTENT>`).  

For each plan describes the following with reference to their corresponding key levels not the full setup:
- Context: Session + Macro context, HTF Trends, volume/liquidity environment and indicators signals (CVD, MA/EMAs, RSI, VWAPs). You must described the context in detailed leading up to the price at location and trigger.  
- Location: HTF key levels, zones and indicators confluences
- Trigger: Price specific triggers + VPA requirements catalysts
- Invalidation: Invalidation condition of plan to be removed

## INSTRUCTION:
For today's session you must generate the following plans as minimum. You must skip plans with "NONE" description and you may generate additional trading plans if they are missed or not considered on the 1H chart:
**SHORT**:
- ORANGE_B: short reversal at 4H/1D.major_H_MAJOR, fading the top of this range with a liquidity sweep or failed break following weaken VPA siganls and bearish divergence on TTF, levering oversold condition on 1H and 4H. 
- PURPLE_B: Short fade the top of the 1H.major.H_MAJOR, expecting price to remains within the 1H range.
- PINK_A: Short deeper pullback at 1H_SELL_2/4H_NEUTRAL, confluenced with rolling 1H_ST-EMAs +1H_50EMA + S_VWAP
- RED_B: short breakdown below 1H.major.L_MAJOR with strong 1H VPA signal and a confirmed 1H candle closes during breakdown. Enter on retest of broken 1H_L_BOS.   

**LONG**:
- BLUE_B: Long fade at 1H.major.L_MAJOR, expecting price to closes back into the 1H range 
- TEAL_B: NONE
- YELLOW_B: Long reversal at 4H.major.L_MAJOR to 4H_BUY_1.  
- GREEN_A: long breakout above 1H.major.H_MAJOR.
- GREEN_B: long breakout above 4H/1D.major.H_MAJOR/ATH 


## EXAMPLE:  

```
# TRADING PLAN FOR 1H_TTF (Trigger • Location • Context)

### **ORANGE_A — Short reversal at weekly supply**

* **Context:** Counter-trend intraday short only on exhaustion/divergence into HTF supply; 1H is stretched into `1W.zones.SELL_1`.
* **Location:** Primary: `1W.zones.SELL_1` → extension into `1W.local.H` and `1W.sr.SR_2`. Nearby magnet: `1D.poc.POC_1`.
* **Trigger:** Rejection pattern (double/triple top or sweep) + **15m_L_MSB** (prefer **1H_L_MSB**) with bearish CVD or sell-side ignition/absorption at the top.
* **Invalidation:** Acceptance above `1W.sr.SR_2` and especially sustained hold inside `1W.zones.SELL_2`.

---

### **RED_A — Short breakdown below range low**

* **Context:** Requires risk-off shift; flips intraday bias lower.
* **Location:** Loss of `4H.major.L_MAJOR` with acceptance back below `1D.sr.SR_2` and `1D.session.PDL`.
* **Trigger:** **1H_L_BOS** through `1H.major.L_MAJOR` / `4H.major.L_MAJOR` on bearish HVC + falling CVD; sell the low-volume retest from below.
* **Invalidation:** Reclaim of `1D.active.H_MSB` and `4H.major.L_MAJOR` with price back above S_VWAP/W_VWAP.

---

### **BLUE_A — Long fade at 4H range low (fakeout scenario)**

* **Context:** Mean-reversion long if a macro headline wicks below but fails to accept under the range.
* **Location:** First touch at `4H.major.L_MAJOR`; upside rotations toward the top of `1D.zones.BUY`, then `1D.poc.POC_3` → `1D.poc.POC_2` if squeeze extends.
* **Trigger:** Liquidity sweep below `4H.major.L_MAJOR` / `1D.session.PDL` with **absorption SHVC** + **15m_H_MSB** and rising CVD; reclaim S_VWAP to confirm.
* **Invalidation:** 1H close and follow-through below `4H.major.L_MAJOR` (no absorption) → stand down.

---

### **TEAL_A — Long shallow pullback (trend-ride)**

* **Context:** Momentum  continuation long riding the breakout. 15m bullish trend remains strong with bullish CVD and volume sustain and above 15m_ST-EMAs/1H_9EMA + S_VWAP
* **Location:** Pullback into 1H EMA9/S_VWAP band while **holding above** `1D.active.H_MSB`; secondary supports: `1D.session.PDH`, `4H.major.H_MAJOR`.
* **Trigger:** **LTF_H_MSB** after a low-volume dip into the EMA9/S_VWAP band with CVD turning up; enter on reclaim.
* **Invalidation:** Clean **1H_L_CHOCH → 1H_L_MSB** while under S_VWAP, or heavy sell VC into the band.

---

### **YELLOW_A — Long fade at 1H range-low retest**

* **Context:** Deeper check-back to 1D_H_MSB breakout base before continuation. Expect LTF exhaustion on the counter trend move and bullish divergence signals. 
* **Location:** `1H.major.L_MAJOR` + `4H.zones.BUY_2` cluster, ideally with rising 1H_50EMA; anchor to `1D.active.H_MSB`.
* **Trigger:** Bullish divergence (RSI/CVD) + **15m_H_MSB** after a sweep; confirm with S_VWAP reclaim.
* **Invalidation:** Acceptance below `1H.major.L_MAJOR` and `1D.sr.SR_2` with bearish HVC continuation.

---

### **GREEN_A — Long retest of breakout level**

* **Context:** First clean retest after breakout for continuation. Expect healthy pullback with no 1H_L_CHOCH. 
* **Location:** `1H.inactive.H_MAJOR` / `4H.major.H_MAJOR` retest with nearby confluence at `1H.zones.BUY_1` and `4H.zones.BUY_1`.
* **Trigger:** **LTF_H_MSB** after a shallow pullback; hold above `4H.major.H_MAJOR` with decreasing pullback volume and rising CVD.
* **Invalidation:** 1H close back below `4H.major.H_MAJOR` and S_VWAP, or a **1H_L_CHOCH** that evolves into **1H_L_MSB**.
* 

### **WHITE_A — 3m momentum scalp long (ride ST-EMAs)**

* **Context:** 1H/4H trends up; CVD rising steadily; bullish VCs keep printing; buyers in control with no strong sell signals.
* **Location:** Shallow pullbacks to 3m ST-EMAs while price holds above `1D.active.H_MSB` and `4H.major.H_MAJOR`; scale out into `1D.poc.POC_1` → `1W.zones.SELL_1` and front-run `1W.local.H`.
* **Trigger:** **`3m_H_MSB`** after a light-volume dip to the 3m ST-EMAs with CVD uptick; enter on close back above the 3m swing high.
* **Invalidation:** **`3m_L_MSB`** or heavy sell VC/absorption, loss of `1D.active.H_MSB` or clean rejection that forces acceptance back below `4H.major.H_MAJOR`.
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
- (Session) S_VWAP (teal): relevant for TF 1H and under
- (Weekly) W_VWAP (blue): relevant for TF 1H and 4H
- (Monthly) M_VWAP (dark green): relevant for TF 4H and 1D. 

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

think hard.
