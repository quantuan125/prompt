# CONTEXT: 
You are a trading analyst and you are preparing the INITIAL SESSION CONTEXT BRIEF for today's trading session for 15th January 2026. 

The attached images are charts of the following timeframe respectively: 1W, 1D, 4H and 1H. 
You may use the attached csv file for further extraction of values for indicators for the CURRENT DEVELOPING (not closed) candle of the corresponding timeframe.

# GOAL:

* Complete the described tasks below using the provided "Key Levels" YAML block which acts as variable constants for referencing. The rules defined are as following: 
  - `active`: Refers to the latest and most significant price action signal. This may include `<H/L>_<FSB/BOS/MSB/CHOCH>`
  - `inactive`: Refers to past price actions signals. 
  - `zones`: <TF_SELL> and <TF_BUY> levels (refers to Low Volume Nodes which are S&D zones)

## KEY LEVELS

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
      H_MAJOR: 97.9
      L_MAJOR: 89.3
    sr:
      SR_1: 93.4
      SR_2: 89.5
      SR_3: 88.4
    poc:
      POC_1: 95.5
      POC_2: 92.5
      POC_3: 90.2
      POC_4: 84.6
      POC_5: 79.7
    zones:
      BUY_1: 88.5
      BUY_2: 91.8
    session:
      PDH: 97.2
      PDL: 95.1
    active:
      H_BOS:: 96.5
    inactive:
      H_BOS:: 90.6

  4H:
    major:
      H_MAJOR: 97.2
      L_MAJOR: 90.1
    sr:
      {}
    poc:
      POC_1: 96.8
      POC_2: 95.5
      POC_3: 93.8
      POC_4: 92.0
    zones:
      SELL_1: 96.1
      BUY_1: 93.5
      BUY_2: 95.0
    active:
      L_CHOCH: 95.8
    inactive:
      H_BOS: 92.5

  1H:
    major:
      H_MAJOR: 95.9
      L_MAJOR: 95.1
    sr: {}
    poc: {}
    zones:
      SELL_1: 95.1-95.3
    active:
      L_BOS: 95.1
    inactive:
      L_BOS: 95.4
```


# TASK 1: 
Generate a detailed technical context with description for each of the relevant trading timeframe as following attached images. This description must covers the history price actions, relevant indicators, key levels (PDH, POC, SR) swing structure levels (<TF>_H/L_MAJOR/MSB/CHOCH) and LVN/supply/demand zones (<TF>_BUY/SELL). 

## INSTRUCTION: 

* Add the following in respective order:

```
- Previous: Cover the last 30 candles
- Current: Covers the last 5 candles including current candle. 
```
`
* Use the resources sections to accurately understand the relevant indicators attched within the csv file. You must references these indicators in the final descriptions along with the trader given information.  
* Never mention a price level or zones without referencing the attached "Key Levels" variables to it. (e.g:  "Rejections at **~118.5–119.2k** supply" (WRONG), "Rejections at `4H.zones.SELL_1` supply at **~118.5–119.2k**" (CORRECT))
* Never reference a low TF variables in a high TF description. Only the opposite is true. (e.g: DO NOT reference `4H.zones.SELL_1` in a `1W_TF` technical description, but the opposite is allowed)
* Always reference candles type followng this format: `<TF>_<bullish/bearish>_<type>_<VC/HVC/SHVC>`. (e.g: `1W_bullish_engulfing_VC`)
* Always reference indicators following this format: `<TF>_<indicators>`. (e.g: `1W_20EMA`, `1H_9/21EMA`, `1H_200MA/EMA`, `1H_RSI-MA`)
* You must use and expand the following provided technical descriptions for each timeframes from traders with additional details based on the materials, context and images given:

  - **1W**: After a strong `1M_bullish_channel` since late ’24, price had a `1W.inactive.L_MSB` which signaled weaken of the weekly bullish trend and distribute within a weekly range for the last 3 months under `ALL.ath/1M.major.H_MAJOR`. Price then had a low volume `1W.inactive.H_FSB` into ATH zone followed by a crypto largest liquidation sell-off week down below `1M.active.H_BOS` + `1W.major.L_MAJOR` with a confirmed `1W.active.L_BOS` last month supported by series of `1W_bearish_VCs` with volume spike + 1W_9/21EMA bearish crossover + OBV/RSI confirmation. Price dropped below the  `1M_ascending_channel` + the ascending `1W_50EMA/MA` (101-103k) historic dynamic bull-market support bands into monthly support/demand zone at `1M.zones.BUY_2` and extended deeper into `1M.poc.POC_4` + `1M.sr.SR_4` with next base at `1M.major.L_MAJOR`. At this location, price bottomed at `1W.major.L_MAJOR` and consolidate for multi weeks candles before recovering higher to retest `1W.zones.SELL_3` supply. 
  - **1D**: After bottoming at `1W.major.L_MAJOR` with an absorption `1D_bearish_hammer_HVC` of highest volume  + oversold 1D_RSI of less than 25, price consolidate within its own daily range at the mentioned monthly demand/support zone. Price recently just broke above its range with a `1D.inactive.H_BOS` to reclaim short term momentum indicators before rallying higher with another `1D.active.H_BOS` supported by increasing 1D_bullish_VCs with volume spike to retest `1W.zones.SELL_3` supply confluenced with the descending 1D_200EMA/MA.   
  - **4H**: Price initiated a strong bullish rally with a `4H.active.H_BOS` supported by increasing 4H_bullish_HVCs + OBV confirmation above `1D.major.H_MAJOR` with a sucessfuly retest of this broken daily level and extends further with overbought RSI>75 into `1W.zones.SELL_3` where it topped at `4H.major.H_MAJOR`. Price pullbacked with low volume and bounced at `4H.local.L` confluenced with the ascending 4H_9EMA and remain strongly above 4H_9EMA + W_VWAP.
  - **1H**: After the rejection at 4H.major.H_MAJOR just underneath 1W.zones.SELL_3 supply, price cool-off and pullback into `1H.zones.BUY_1` where it botomed with a LL at `1H.major.L_MAJOR`/`4H.local.L` before recover with reclaim of the 1H_9/21EMA + S_VWAP following a confirmed `1H.active.L_FSB`. Price then etablished a LH at `1H.major.H_MAJOR` at the retest of `1H.zones.SELL_1` supply. Price is currently within a 1H_descending_wedge pattern and currently trying to break above this wedge pattern with multiple retest of this supply area, just under `1H.major.H_MAJOR`.
  
## EXAMPLE: 

```
## TECHNICAL CONTEXT

### **Weekly (1W – Super-HTF Structure)**

* **Previous (~30 candles):** Uptrend from late ’24 into **ATH** `ALL.ath`, distribution below `1W.sr.SR_2` / `1W.zones.SELL_2`, then an ATH sweep noted at `1W.inactive.H_FSB` with a bearish inverted-hammer VC. Corrective leg confirmed `1W.inactive.L_MSB`, undercut the prior range and retested `1W.zones.BUY_1` + weekly EMA band; HL formed just above `1W.major.L_MAJOR`. Since June, recovery legs have run on lighter volume.
* **Current (~5 candles):** Bounce is retesting unfresh weekly supply `1W.zones.SELL_1` while price rides the rising weekly EMAs. Capped by the local weekly top `1W.local.H` and `1W.sr.SR_1`. HTF bias: **bullish into supply** (monitor for absorption/exhaustion at `1W.zones.SELL_1`).

---

### **Daily (1D – HTF for intraday)**

* **Previous (~30 candles):** Range bound inside the weekly band `1W.local.H` ↔ `1W.local.L`. Last week’s liquidation leg printed bearish VCs into `1D.major.L_MAJOR` / `1W.local.L`, then weekend basing.
* **Current (~5 candles):** Break/reclaim of `1D.active.H_MSB` with a clean retest; today extends into `1W.zones.SELL_1` / `1W.local.H`. Note: the up-leg’s volume is lighter than last week’s sell-leg. Session refs: `1D.session.PDH`, `1D.session.PDL`; overhead magnet `1D.poc.POC_1`. Bias: **constructive while probing weekly supply**.

---

### **4-Hour (4H – HTF for 1H)**

* **Previous (~30 candles):** Post-selloff coil above `1W.poc.POC_3`; Sunday/Monday rallies with bullish HVCs helped confirm `1D.active.H_MSB`. Pullback held `4H.major.L_MAJOR` and reclaimed the 200EMA/MA as dynamic support.
* **Current (~5 candles):** Impulse leg pushed through `4H.major.H_MAJOR` (fresh BOS if close holds) and is now inside `1W.zones.SELL_1`. Momentum strong but stretched; watch for exhaustion against `1W.sr.SR_1` / `1W.local.H`. Bias: **bullish but extended into HTF supply**.

---

### **1-Hour (1H – TTF)**

* **Previous (~30 candles):** Bottom at `4H.major.L_MAJOR` → breakout through `1H.inactive.H_MAJOR` + `4H.major.H_MAJOR` on a 1H bullish SHVC; CVD confirmed; HH/HL sequence established.
* **Current (~5 candles):** Price holds above all 1H MAs and S_VWAP; structure remains constructive above `1D.active.H_MSB`, `1D.session.PDH` and `1H.zones.BUY_1`. Bias: **trend-up with mean-reversion risk** as price approaches `1W.zones.SELL_1` / `1W.local.H`.
```

# TASK 2:
Please generate the trading plans following the 1H_TTF for today's session. Follows the instruction, format and examples below. 

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

**Setup Type** and **Setup Priority** can be extracted from the `LAYER 3: EXECUTION PROTOCOLS` in RESOURCE section.

## INSTRUCTION:
For today's session you must generate the following plans as minimum. You must skip plans with "NONE" description and you may generate additional trading plans if they are missed or not considered on the 1H chart:
**SHORT**
- WHITE_A: short continuation with 1H_L_BOS confirmed below 1H_L_MAJOR and 1H_21EMA (with bearish crossover), entry on a retest of the broken level with extension to 1H_BUY_1 pivot zone with LTF_L_MSB. 
- ORANGE_A: short reversal above 4H_H_MAJOR + 1W_SELL_3 supported by TTF bearish divergence signals and weaken bullish VPA. Entry on a confirmed by `TTF_L_MSB`.
- PURPLE_A: short fade at the top of 4H range with `H_FSB` at 1H_H_MAJOR/4H_H_MAJOR +  4H_SELL_2. Entry on a confirmed `LTF_L_MSB` . 
- PINK_A: short monmentum counter-trend scalp if price loses below S_VWAP + 1H_9EMA and remains below 1H_L_MAJOR. Entry with a confirmed `LTF_L_BOS/MSB` on the retest of the broken level with LTF bearish strucutre confluenced with bearish crossover and descending `LTF_9/21EMA`
- RED_A: Short break and retest below 1H_L_MAJOR with strong TTF VPA signal with a confirm `1H_L_BOS`. Entry on low volume retest of broken level with `LTF_L_MSB/BOS`.
**LONG**
- BLUE_A: long fade bottom of 1H range with `L_FSB` at 1H_BUY_1 demand with extension to 1H_L_MAJOR supported by LTF bullish divergences signals and weaken bearish VPA. Entry on a confirmed `LTF_H_MSB`.  
- TEAL_A: long momentum scalp if price maintain above S_VWAP + 1H_9EMA and sustain above 1H_H_MAJOR. Entry with a confirmed `LTF_H_BOS/MSB` on a retest of LTF strucutre confluenced with bullish crossover and raising `LTF_9/21EMA`.
- YELLOW_A: long major reversal if 1H trend confirm flip bearish with a retest at 4H_BUY_1/PDL with extension to 1D_BUY_3 supported by TTF bullish divergences. Entry on confirmed `TTF_H_MSB`.
- GREEN_A: long breakout above 4H_H_MAJOR with a confirmed `1H_H_BOS` supported by strong TTF VPA signal. Entry on a low volume retest of the broken level with a confirmed `LTF_H_MSB/BOS`. 
- <OTHERS>

## EXAMPLE: 

```
# TRADING PLAN FOR 1H_TTF (Trigger • Location • Context)

## SHORT

### **ORANGE_B — Short reversal at 1H/4H tops**

* **Context:** 1H/4H trends are stretched into HTF resistance; RSI elevated but showing signal of bearish divergence, VPA showing slowing push under **1W.sr.SR_2**. Look for topping behavior with no follow through (failed break) with reversal pattern such as double top or triple drive top on the TTF. 
* **Location:** Confluence at `1H.major.H_MAJOR` / `4H.major.H_MAJOR` with overhead weekly band `1W.zones.SELL_1 → 1W.sr.SR_2`.
* **Trigger:** Liquidity sweep/failed break  of `1H/4H.major.H_MAJOR` then **15m_L_MSB → 1H_L_MSB** with **bearish CVD** or sell-side ignition/absorption SHVC. 
* **Invalidation:** Acceptance and hold above `1W.sr.SR_2` (trend ignition continuation) — remove plan.

---

### **PURPLE_A — Short fade of 1H local high**

* **Context:** Range scalp if momentum stalls inside the 1H flag; expect weakening bullish VPA and LTF **bearish RSI/CVD divergence**.
* **Location:** `1H.minor.H` (top of local range) with `1H.zones.BUY` below as magnet.
* **Trigger:** Failure to break/hold above `1H.minor.H` + **15m_L_MSB**, or wick-through and close back inside with CVD rolling over.
* **Invalidation:** 1H close above `1H.minor.H` that immediately converts to support.

---

### **PINK_A — Short continuation on local breakdown**

* **Context:** Counter-trend pullback scenario aiming for a deeper reset on 1H/4H if the flag fails. Expect a flags pattern with LHs to form on the 1H local structure
* **Location:** Below `1H.minor.L` and under `1H.zones.BUY 117.7-118.1k` with ST-EMA band rolling over.
* **Trigger:** **Confirmed 1H_L_CHOCH → follow-through below `1H.minor.L`**, bearish HVC and falling CVD; sell retest of the broken band from below.
* **Invalidation:** Reclaim of `1H.zones.BUY` and `S_VWAP` with 1H HL sequence restored.

---

### **RED_B — Breakdown of 1H major range low**

* **Context:** Bias flips down if major structure fails with strong bearish VPA signal a challenge to the 1D/4H bullish structure
* **Location:** Loss of `1H.major.L_MAJOR (116.7k)` with failed retest while below `1H.zones.BUY`.
* **Trigger:** **1H_L_BOS** through `1H.major.L_MAJOR` on strong sell VPA and negative CVD; enter on low-volume retest.
* **Invalidation:** Sharp reclaim back above `1H.major.L_MAJOR` and `1D.active.H_MSB`.

---

## LONG

### **BLUE_B — Long fade at 1H local low**

* **Context:** Continue to trade with trend while range holds; expect sellers to tire near the bottom of the 1H flag.
* **Location:** `1H.minor.L` with confluence of rising `EMA9/21` and `S_VWAP` nearby; anchor to `1D.active.H_MSB` below.
* **Trigger:** LTF **bullish divergence (RSI/CVD)** + **15m_H_MSB** after a sweep; reclaim `S_VWAP` to confirm.
* **Invalidation:** Acceptance below `1H.minor.L` and failure to reclaim `S_VWAP`.

---

### **TEAL_B — Long reversal at 1H demand band**

* **Context:** Shallow pullback buy in trend, expect LTF bullish reversal pattern at location with raising CVD. 
* **Location:** `1H.zones.BUY 117.7-118.1k` → extends into `1D.sr.SR_3 / 1D.session.PDL` if wicky.
* **Trigger:** **LTF_H_MSB** after low-volume dip with CVD uptick; enter on close back above the band.
* **Invalidation:** 1H close below the band with sell-side HVC.

---

### **YELLOW_B — Long at 1H major range low**

* **Context:** Deeper pullback into structural support with **1H_50EMA** and 4H_9EMA rising as dynamic support.
* **Location:** `1H.major.L_MAJOR (116.7k)` with extension toward `4H.zones.BUY (115.2-116.1k)`.
* **Trigger:** Trap/sweep below `1H.major.L_MAJOR` + **15m/1H_H_MSB** and rising CVD; reclaim `S_VWAP`.
* **Invalidation:** Continued acceptance below `1H.major.L_MAJOR` (defer to **RED_B** path).

---

### **YELLOW_C — Long on retest of prior 4H_H_BOS**

* **Context:** If price backfills the most recent **4H.active.H_BOS** breakout area, look for buyers to step back in.
* **Location:** Prior `4H.inactive.H_BOS` zone (now support) overlapping `4H.zones.BUY`.
* **Trigger:** **LTF_H_MSB** after a stop-run into the zone with absorption SHVC and CVD turn.
* **Invalidation:** 1H close below the BOS base with persistent bearish VPA.

---

### **GREEN_B — Long breakout and retest**

* **Context:** Continuation through HTF resistance with buy-side ignition.
* **Location:** Clear break above `1H/4H.major.H_MAJOR` inside `1W.zones.SELL_1`; first retest of the broken level.
* **Trigger:** **1H_H_BOS + bullish HVC** → low-volume pullback; enter on **LTF_H_MSB** with rising CVD.
* **Invalidation:** Failed retest (acceptance back below `1H/4H.major.H_MAJOR`) or immediate **1H_L_CHOCH** after entry.
```

# INSTRUCTION
- think hard.
- Keep all generated content & descriptions concise to minimize tokens output. 
- You must read "resource.md" in your knowledge base for understanding of our trading context as reference before completing the tasks described above 


