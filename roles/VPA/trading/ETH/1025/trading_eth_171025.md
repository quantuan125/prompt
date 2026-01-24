# CONTEXT: 
## TRADER CONTEXT: 
Today is Friday 17th of October 2025, we are in 2 hours into US session. Due to government shutdown, we have not received any public economic data such as NFP/Unemployment/PPI for the last 3 weeks. This does means there is no looming data released today however refers to `MACRO CONTEXT` for the rest of the macro events this week. 

### BTC: 

On Tuesday, we had Fed Chair Powell's Speech which is generally shown dovish FED however tariffs news resurged between Trump and China is causing uncertainty to the broader risk-on markets (BTC & Stocks), wherease risk-off market such as gold and silver is in hyperbolic bullish trend. Due to government 

We have officially passed September which has been notorious for a BTC and crypto pullbacks during the bull runs year and currently enter Q4 of which has been typical bullish for bitcoin bull cycle. We should favors more bullish setups while remains as cautious as possible until BTC firmly surpasses ATH. 

Last week: Crypto market got the biggest liquiditation sell off and for BTC particularly, down to retest the integrity of the bullish structure of the entire cycle at the bottom of 1W range after failing to firmly closed above ATH zone but instead sweep it. Price has remains in a 1W range for about 3 months in a row which shows concern for the bulls for this cycle. For our trader specifically, 1W `OVERALL_ASSESSMENT` for BTC has flipped to `NEUTRAL` to `NEUTRAL-BEARISH` first time in half a year.    

Sentiment: Public sentiment for October remain bullish for BTC within this year of its bullish 4 years cycle from a seasonality and historic standpoint. However price action last week have liquidated millions of leveraged crypto traders and enact some fears with people hypothesizing for the top of the cycle is in for BTC, and the start of an extended bear market into 2026. `Fear & Greed Index` currently ranging between 22-28 in fear/extreme fear territory after swinging from above 60 (greed) last two weeks. 

ETH: ETH remains undermined by BTC price actions despite bouncing form 2W demand zone and remains in consolidation while showing strength on ETHBTC pairs by remaining in range for this pair despite BTC weakness. IF BTC hold 1W range, then ETH is able to rally to and continue strength against BTC and rally to ATH on USD pair given the 2W bullish trend. 
  
## TECHNICAL CONTEXT

### KEY LEVELS 

```yaml
# ETH/USDT
meta:
  pair: ETHUSDT
  units: "USDT"   # all numbers in full USDT format
  note: "Ranges use '-', e.g., 4200-4300"
  levels:
    ALL:
      ath: 4956

    1M:
      major:
        L_MAJOR: 1389
      sr:
        SR_1: 3745
        SR_2: 2767
      poc:
        POC_1: 2523
      zones:
        BUY_1: 2750
        BUY_2: 2162
      active: 
        H_MSB: 4095
      inactive:
        L_BOS: 2113

    2W:
      local: 
        L: 3438
      major:
        H_MAJOR: 4950
        L_MAJOR: 2167
      zones:
        BUY_2: 3538
        BUY_1: 3201
        SELL_1: 4784
      sr:
        SR_3: 4615
        SR_2: 3960
        SR_1: 2870
      poc:
        POC_1: 4300
        POC_2: 3338
      active:
        H_BOS: 2880
      inactive:
        {}

    3D:
      major:
        H_MAJOR: 4755
        L_MAJOR: 3817
      poc:
        POC_1: 4721
        POC_2: 4469
        POC_3: 4175
        POC_4: 4011
        POC_5: 3645
      zones:
        SELL_1: 4423
        BUY_1: 4034
        NEUTRAL: 4250
      active:
        L_SWEEP: 4061
      inactive:
        H_SWEEP: 4790

    12H:
      local:
        H: 4292
      major:
        H_MAJOR: 4756
        L_MAJOR_1: 3644
        L_MAJOR_2: 3437
      zones:
        SELL_1: 4220
        BUY_1: 3675
        BUY_2: 3865
      active:
        L_SWEEP: 3817
      inactive: 
        L_CHOCH: 4413

    2H:
      major:
        H_MAJOR: 4220
        L_MAJOR: 4042
      zones:
          BUY_2: 4255
          BUY_1: 4046
      active:
        L_SWEEP: 4081
        L_CHOCH: 4116
      inactive: 
        H_BOS: 3866

# ETH/BTC
meta:
  pair: ETHBTC
  units: "decimal"   # decimal format for BTC pairs
  note: "Ranges use '-', precision to 5 decimals"
  levels:
    ALL:
      ath: 0.04326

    1M:
      major:
        H_MAJOR: 0.06132
        L_MAJOR: 0.01762
      sr:
        SR_1: 0.03974
        SR_2: 0.03562
      poc:
        POC_1: 0.03113
      zones:
        SELL_1: 0.05045
        SELL_2: 0.03956
      active:
        L_BOS: 0.04469
      inactive: {}

    1W:
      local:
        H: 0.04113
      major:
        H_MAJOR: 0.04326
        L_MAJOR: 0.03196
      poc:
        POC_1: 0.03895
        POC_2: 0.03677
        POC_3: 0.03204
      zones:
        BUY_2: 0.03226
        BUY_1: 0.02964
        SELL_1: 0.0417
        SELL_2: 0.03767
      active:
        L_CHOCH: 0.03804
      inactive: 
        H_MSB: 0.02975

    1D:
      major:
        H_MAJOR: 0.03718
        L_MAJOR_1: 0.03196
        L_MAJOR_2: 0.03529
      zones:
        SELL_1: 0.03657
        SELL_2: 0.03503
        BUY_1: 0.03322
      active:
        H_SWEEP: 0.03706
      inactive: 
        L_BOS: 0.03518

```

### ETH/USDT

#### **Bi-Weekly (2W – Super-HTF Structure)**

* **Previous (≈30 bars):** Trend of **HH/HL** intact; multiple rejections below `2W.zones.SELL_1` **4784** and `2W.sr.SR_3` **4615**; value magnets remain `2W.poc.POC_1` **4300**, `2W.poc.POC_2` **3338**.
* **Current:** Active 2W bar is a **`2W_bearish_spread_VC`** closing **below** `2W_9EMA` (close **3789** < ema9 **3820**) but **above** `2W_21/50EMA` (**3380/2975**). **RSI:** 55.9 / `RSI_MA` 55.4 (still >50). **VWAPs:** M/W-VWAP ≈ **3919** **above** price → overhead dynamic resistance. **Volume:** ~0.42×–0.46× of 20/30MA (**low**, not HVC). HTF bias = **bullish uptrend in pullback** toward `2W.sr.SR_2` **3960** / `2W.zones.BUY_2` **3538**.

#### **Three-Day (3D – HTF for 12H)**

* **Previous (≈30 bars):** Rejections near `ALL.ath` **4956** and `3D.zones.SELL_1` **4423**; mid-range pivot at `3D.zones.NEUTRAL` **4250**; bids appeared at `3D.zones.BUY_1` **4034** and `3D.poc.POC_5` **3645**.
* **Current:** Grinding **below** `3D_9/21EMA` (**4177/4169**), hovering **above** `3D_50EMA` (**3748**) and far **above** `3D_200EMA` (**3020**). **RSI:** 44.6 < `RSI_MA` 55.3 (momentum soft). **VWAPs:** W-VWAP **3982** / M-VWAP **4184** **above** price. **Volume:** ~0.8× / 0.73× → sub-avg **VCs**, no HVC. HTF state = **neutral-bearish inside range**, mid pivot `3D.zones.NEUTRAL` **4250**.

#### **Twelve-Hour (12H – Trading Timeframe)**

* **Previous (≈30 bars):** Series of LH/LL with price losing ST-ribbon; repeated rejections at `12H.zones.SELL_1` **4220**; buyers defend around `12H.major.L_MAJOR_1` **3644** / `3D.poc.POC_5` **3645**.
* **Current:** **Below all EMAs** (`12H_9/21/50/200` ≈ **3945/4067/4189/3971**). **RSI:** 38.8 < `RSI_MA` 40.8 (bearish). **VWAPs:** W-VWAP **4015** / M-VWAP **4165** **above** → persistent overhead resistance. **Volume:** ~0.19× (light pullback volume). State = **bearish trend inside 3D range**; key supports `12H.major.L_MAJOR_1` **3644**, `12H.major.L_MAJOR_2` **3437**.

#### **Two-Hour (2H – LTF for execution)**
* **Current:** strong downtrend 2H descneding channel just broken below this descending channel with the latest 2H_L_BOS at 3826 and capped by S_VWAP + 2H_9EMA from above. 

### ETH/BTC

#### **Weekly (1W)**

* **Previous:** Reversal from `1W.major.L_MAJOR` **0.03196** pushed up but stalled beneath the `1M.sr.SR_1` **0.03974**/`1W.zones.SELL_2` **0.03767** band; repeated failures under the cap at `1W.active.L_CHOCH` **0.03804** with rotations toward the magnet at `1W.poc.POC_2` **0.03677** and shelf above `1W.poc.POC_3` **0.03204**.
* **Current (last 5):** **Close ~0.03586** prints a **`1W_bearish_spinningtop_VC`**: price **below** `1W_ema9` **0.03648** and **W-VWAP** **0.03609**, **above** `1W_ema21/ema50` **0.03381/0.03362**, well **below** `1W_ema200` **0.04487**. **RSI 56.8 < RSI_MA 63.8** (momentum cooled). **Volume** < `vol_ma20/30` (no HVC). Bias: **soft underperformance** unless reclaim of `1W.poc.POC_2` **0.03677** and `1W.active.L_CHOCH` **0.03804**; downside probes eye `1W.zones.BUY_2` **0.03226** / `1W.poc.POC_3` **0.03204**.

---

#### **Daily (1D)**

* **Previous:** Inside a `1D_descending_channel`; rallies repeatedly capped at `1D.zones.SELL_1` **0.03657**/`1D.major.H_MAJOR` **0.03718** with a failed `1D.active.H_SWEEP` **0.03706**; dips defended near `1D.major.L_MAJOR_2` **0.03529** and above `1W.poc.POC_3` **0.03204**; value gravitates around `1W.poc.POC_2` **0.03677** overhead.
* **Current (last 5):** **Close ~0.03586** is a **`1D_bearish_doji_VC`**: price **below** `1D_ema9/21/50` **0.03601/0.03639/0.03664**, **above** `1D_ema200` **0.03268**; **below** **W-VWAP** **0.03622**, **above** **M-VWAP** **0.03558** and **S-VWAP** **0.03578**. **RSI 45.3 (> RSI_MA 43.7 but <50)** ⇒ weak momentum. Immediate resistance: `1D.zones.SELL_1` **0.03657** → `1D.major.H_MAJOR` **0.03718**; supports: `1D.major.L_MAJOR_2` **0.03529** → `1D.zones.BUY_1` **0.03322** / `1W.poc.POC_3` **0.03204**. Bias: **neutral-bearish** until a daily close back above `1D.zones.SELL_1` **0.03657**.

## MACRO CONTEXT
### LAST WEEK
* **Tariff trajectory sharpened:** The White House and USTR reiterated/advanced tariff plans, with U.S. retailers warning about **100% tariffs on all Chinese imports slated for Nov 1**, while China broadened **rare-earth export controls**, intensifying supply-chain risk across semis/defense.  
* **Shutdown → data blackout:** The **federal government shutdown (from Oct 1)** curtailed major data releases and forced work-arounds (e.g., CPI timing), raising uncertainty for the Fed and markets.  
* **Crypto risk impulse peaked:** **BTC set a new ATH (~$125k) on Oct 5** alongside **record spot-ETF inflows** to start October, framing a high-beta backdrop for this week’s risk headlines.  

### THIS WEEK
* **Policy & geopolitics:**  
  * **U.S.–China trade war at sea:** Both sides **implemented tit-for-tat port fees on Oct 14**, lifting freight costs and stoking inflation pass-through risk. The **G7** flagged coordination on **China’s minerals/rare-earth controls**, and Beijing defended tighter restrictions.  
  * **Trump & tariffs:** Corporates reiterated contingency plans for the **Nov 1 100% China tariff start**, keeping margin and holiday-pricing risks front-of-mind.  
  * **Shutdown, Day 17 (Fri, Oct 17):** White House orders sought targeted pay carve-outs; airlines warned of operational drag. The **data blackout** persists, with selective releases prioritized.
* **The Fed:** October **FOMC (Oct 28–29)** in focus. Fed officials signaled preference for **–25 bp** (some pushing for **–50 bp**). Futures imply high odds of an October cut, then another into December.
* **Data (planned / shutdown-affected):**  
  * **Thu, Oct 16:** **PPI (Sep)** (scheduled).  
  * **Fri, Oct 17:** **Import/Export Prices (Sep)** (scheduled).  
  * **Fri, Oct 24:** **CPI (Sep)** (BLS prioritizing release despite shutdown).  
* **Tech/AI impulse:** **TSMC beat & raised FY guide**, ASML solid Q3, and a **$40B AI data-center deal** (BlackRock-led, Nvidia-backed) sustained AI-capex sentiment supporting megacaps.  
* **Metals & commodities:** **Gold broke above $4,300/oz (Oct 16)** on safe-haven demand + Fed cut bets; oil eased on trade/tariff growth fears.  
* **Earnings:** U.S. banks and megacap-tech adjacent names printed **mixed but resilient** results, with chips/AI stronger than financials.  
* **Calendar/holidays:** **Mon, Oct 13 – Columbus Day:** **NYSE/Nasdaq open; U.S. bond market closed/modified hours.** Canada **Thanksgiving (Oct 13)** reduced NA liquidity early week.

### MACRO ANALYSIS 
A tariff-and-shutdown-driven **risk-off + duration** mix is colliding with **AI-capex risk-on**, producing cross-asset chop: **gold surges** on policy/geopolitical risk and cut odds; **BTC** is swinging with risk sentiment and ETF flows (debasement hedge bid vs. VaR-cuts when equities wobble); **S&P 500** is bifurcated (AI strength vs. tariff/financials drag). Today, traders should expect **headline-sensitive tape**: port-fee/tariff updates and shutdown headlines can **lift gold / weigh cyclicals & crypto**, while **AI beats** can **cushion SPX** and spill over to crypto beta if yields drift lower.

#### GOLD
Record highs above **$4.3k** reflect **safe-haven demand + high cut odds + trade escalation**. Near-term asymmetry skews to **buy-dips** on tariff/shutdown headlines; watch **real yields**—any sharp drop on dovish repricing should extend gold’s momentum.

#### BTC & ETH
After early-Oct **ATH/strong ETF inflows**, crypto showed **risk sensitivity** to U.S.–China tensions and liquidation waves. Intraday tone hinges on **U.S. rates (cut odds)** and **ETF flow prints**: falling yields/supportive flows favor rebounds; tariff shocks/sharp equity drawdowns risk **beta-led air-pockets**.

#### SP500
**AI/semis** buoyed by TSMC/ASML and AI-DC deals, but **financials/retail/cyclicals** face margin and NIM pressure (**tariffs, shutdown**). Expect **sector dispersion**; indices stay **headline-reactive**. Watch **import/producer-price prints** (if posted) and **regional-bank tape** for risk appetite cues.

# TRADING PLAN FOR 12H_TTF (Trigger • Location • Context)

### **RED_A1 — Short on breakdown & retest of 12H range low**

* **BTC / ETHBTC:** Prefer ETHBTC **weak** (stuck below `1D.zones.SELL_1` **0.03657** / `1W.poc.POC_2` **0.03677**).
* **Context:** 12H bear-trend inside 3D range; price below all 12H EMAs & W/M-VWAPs.
* **Location:** Break **below** `12H.major.L_MAJOR_2` **3437** toward `2W.poc.POC_2` **3338**.
* **Trigger:** Confirmed **`12H_L_BOS`** under **3437** with **ignition HVC** + **falling CVD**, then **2H L-MSB** on a **low-volume retest** of 3437 from below.
* **Invalidation:** Acceptance **back above** `12H.major.L_MAJOR_2` **3437** **and** `2H_50EMA` (~**3974**) with **rising CVD**.
* **Setup Priority:** B

### **RED_A2 — Short deeper pullback to newly formed 12H supply**

* **BTC / ETHBTC:** Want ETHBTC **weak or failing** at `1D.zones.SELL_1` **0.03657**.
* **Context:** After confirmed **`12H_L_BOS`** below `12H.major.L_MAJOR_2`, wait for **deeper** pullback.
* **Location:** Retest into **new 12H supply** created by the BOS (around broken **3437 → 3644** pocket) with 12H_ST-EMAs + W_VWAP as confluenced; first resistance check is **prior breakdown shelf** near **3437–3644**.
* **Trigger:** **`2H_L_MSB`** inside the pullback zone + **bearish CVD**; volume on pullback **<** impulse.
* **Invalidation:** **Close back above** `12H.major.L_MAJOR_1` **3644** **and** hold `3D.zones.NEUTRAL` **4250**.
* **Setup Priority:** A+

### **PURPLE_A — Fade short at 12H/3D pivot stack**

* **BTC / ETHBTC:** Neutral→soft ETHBTC (below **0.03657**).
* **Context:** Counter-trend **squeeze** into resistance within a 12H down-swing.
* **Location:** Confluence at **`12H.local.H` 4292 / `3D.zones.NEUTRAL` 4250 / `12H.zones.SELL_1` 4220**.
* **Trigger:** **Liquidity sweep** into 4250–4292 with **absorption SHVC** + **`2H_L_MSB`** back below **4250**; CVD **bearish** / RSI **divergence** preferred.
* **Invalidation:** **Acceptance above** `12H.local.H` **4292** and push toward `3D.zones.SELL_1` **4423**.
* **Setup Priority:** B+

### **ORANGE_A — HTF reversal short at 3D supply**

* **BTC / ETHBTC:** Favor if ETHBTC stalls under `1D.major.H_MAJOR` **0.03718**.
* **Context:** `12H_H_CHOCH` above 12H_H countertrend into test of the **top of `3D_descending_channel`** into supply.
* **Location:** `3D.zones.SELL_1` **4423** (first trouble area above `3D.zones.NEUTRAL` **4250**).
* **Trigger:** **`2H_L_MSB`** after a **wick or sweep** of **4423** with **absorption SHVC** at the level.
* **Invalidation:** **2H H-BOS** and **12H acceptance** above `3D.zones.SELL_1` toward `3D.poc.POC_1` **4721**.
* **Setup Priority:** A-

### **PINK_A — 2H momentum short with S-VWAP resistance**

* **BTC / ETHBTC:** Prefer ETHBTC **sliding** toward `1W.poc.POC_3` **0.03204**.
* **Context:** Intraday momentum continuation while 12H remains below all EMAs.
* **Location:** Reject at **2H S-VWAP** (~`2H.vwap_session` **3787**) or at `2H_21/50EMA` **3892/3974**.
* **Trigger:** **`2H_L_BOS`** continuation from lower high with **ignition HVC** + **falling CVD**.
* **Invalidation:** **Reclaim** of W-VWAP **4011** and `2H_200EMA` **4158**.
* **Setup Priority:** B

### **BLUE_A — Fade long at 3D range low (ACTIVE)**

* **BTC / ETHBTC:** Only if ETHBTC **stabilizes** (holds above `1D.BUY_1` **0.03322**) or improves.
* **Context:** Mean-reversion off major 12H/3D supports.
* **Location:** `12H.zones.BUY_1` with extension to `12H.major.L_MAJOR_1` **3644** 
* **Trigger:** `2H_H_CHOCH` with strong bullish **absorption SHVC** and follow through at location; CVD turns **up**.
* **Invalidation:** Clean 12H close below `12H.major.L_MAJOR_2` **3437**.
* **Setup Priority:** B+

### **GREEN_A — Long on breakout & retest of 12H pivot**

* **BTC / ETHBTC:** Needs ETHBTC **firming** (reclaim `1D.zones.SELL_1` **0.03657**).
* **Context:** Attempted **TTF realignment** vs soft 3D; higher risk.
* **Location:** Breakout **above** `12H.local.H` **4292** / **`3D.zones.NEUTRAL` 4250**.
* **Trigger:** **`12H_H_CHOCH`** > **4292**, then **retest** holding with **`2H_H_MSB`** and **rising CVD**.
* **Invalidation:** **Failure back below** **4250**.
* **Setup Priority:** B

### **YELLOW_A — Reversal long at first 12H demand**

* **BTC / ETHBTC:** Require ETHBTC **not making new lows** (prefer > **0.03322**).
* **Context:** Counter-trend scalp from demand; take profits fast into overhead POCs.
* **Location:** `12H.zones.BUY_1` **3675** / `12H.major.L_MAJOR_1` **3644**.
* **Trigger:** **Manipulation SHVC** flush into the band → **`2H_H_MSB`** back above **3644–3675** with **CVD** flipping positive.
* **Invalidation:** **Acceptance below** `12H.major.L_MAJOR_1` **3644**.
* **Setup Priority:** A

### **TEAL_A — Intraday momentum long on S-VWAP reclaim**

* **BTC / ETHBTC:** Prefer ETHBTC **firm** (pushing toward `1W.poc.POC_1` **0.03895**).
* **Context:** Tactical momentum reversal day.
* **Location:** **Reclaim** of **2H S-VWAP** (~**3787**) with room to `2H_21/50EMA` **3892/3974** then `3D.zones.NEUTRAL` **4250**.
* **Trigger:** **`2H_H_BOS`** through S-VWAP with **ignition HVC** + **rising CVD**, then shallow retest.
* **Invalidation:** Lose S-VWAP again with **`2H_L_MSB`**.
* **Setup Priority:** B

# TASK  
We have outlined the colored trading plans aligned with the chart using 12H_TTF with 3D as primary trend HTF and 2W as Super HTF + structural context. Our LTF for execution is 2H or 4H. 

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
- 2W: `HTF = BULLISH*`.
- `PG` grades are assessed based on the plan full viability. DO NOT DEGRADE the plan based on probability/possibility.  
- DO NOT PERFORM TTI ON the ETH/BTC pairs. 