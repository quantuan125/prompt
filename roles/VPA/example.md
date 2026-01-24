# EXAMPLE 
The following show multi-turn conversation examples involve text prompts send by users and LLM_Trader where:
- TYPE 1: TURN 1 - Session Initialization Prompt
- TYPE 2: TURN 2 + 3 - Follow-ups Prompt

This example does contains images and additional files attached but not highlighted in this file. 

## TURN 1

### USER 
```
    # CONTEXT: 
    ## TRADER CONTEXT: 
    Today: Today is Tuesday 23rd of December 2025, we are in London session, 2 hours until US session. We have Durable Goods MoM + GDP Growth Rate Estimate as major data/macro event released today with details outlined as below. Refers to `MACRO CONTEXT` for the rest of the macro events this week.  

    Last month: We have officially passed October + November which was supposed to be bullish month for BTC and crypto in terms of seasonality during a bull cycle year, however we got the opposite of that: largest crypto liquidation sell off and continuation of weekly downtrend breaking bullish structure for the cycle despite soft CPI + Inflation data print + resolution on China-US tariffs.

    This month: Marked the end of Quantitative Tightening cycle from the FED and market was reacting to 25bps rate cut from FOMC last week.

    This week: Chirstmas holiday week with macro data released for as following: 
    ```markdown
    ### Today’s key US macro prints (Tue Dec 23, 2025)

    **1) Durable Goods Orders (Oct 2025, m/m)**

    * **Headline new orders:** **-2.2%** to **$307.4B** (pullback after Sep increase).
    * **Ex-transportation:** **+0.2%**
    * **Ex-defense:** **-1.5%**
    * **Transportation equipment:** **-6.5%** to **$103.9B** (main drag).
    * Market expectation context: economists were looking for roughly **-1.5%** headline (so the print is weaker-than-expected). 

    **2) GDP “revision” (Q3 2025 — BEA Initial Estimate released today due to shutdown delays)**

    * **Real GDP (SAAR): +4.3%** (vs **+3.8%** in Q2). 
    * **Real final sales to private domestic purchasers:** **+3.0%** (cleaner demand signal than headline GDP). 
    * **Inflation inside GDP:**

    * **PCE price index:** **+2.8%**; **core PCE:** **+2.9%**
    * **Gross domestic purchases price index:** **+3.4%** 
    * BEA note: this “initial estimate” **replaces the usual advance + second estimate** because of the shutdown. 

    ---

    ## Implications for today’s trading markets (BTC/ETH, SP500, Gold)

    ### Cross-market rates impulse (the “master switch”)

    * **GDP is clearly “hot” (4.3%) and price indices inside GDP are firmer (PCE 2.8 / core 2.9; purchases 3.4)** → *rates can reprice higher* (hawkish tilt), especially if desks treat this as confirmation the economy ran stronger than assumed into Q4. 
    * **Durable goods headline is weak (-2.2%) but ex-transport is positive (+0.2%)** → mixed: looks more like **transport volatility** than broad collapse, yet still a *growth/mfg soft patch* signal. 

    Net: **macro mix is “strong growth + sticky-ish prices”** (GDP) vs **“manufacturing wobble”** (durables). In thin holiday liquidity, the **rates/FX reaction** can dominate price action more than the data itself.
    ```

    Directive: Price is bearish on weekly/daily timeframe however caution due low volume environemnt near Christmas holiday and after multi-week consolidation at monthly support/demand zone with prior daily oversold signals. Prefers mean-reversion setup with prioritize on trade-based location rather than trend. 

    Sentiment: With price action last month that have liquidated millions of leveraged crypto traders and enact fears, the general consensus is bearish with hypothesis of the top for the cycle is already set for BTC, and the start of an extended bear market into 2026. `Fear & Greed Index` worsen from 30-40 (NEUTRAL) since last month to sustaining around 14 (EXTREME FEAR) - 25 (FEAR) in the current weeks. 

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
        BUY_2: 89.5
        BUY_1: 73.7
        inactive:
        H_BOS: 109.6

    1W:
        local: 
        H: 116.4
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
        POC_1: 101.8
        POC_2: 94.6
        POC_3: 91.4
        POC_4: 87.3
        POC_5: 67.4
        zones:
        SELL_1: 114.9
        SELL_2: 106.1
        SELL_3: 98.1
        active:
        L_BOS: 107.3
        inactive:
        L_MSB: 111.9
        H_FSB: 124.5
        L_FSB: 108.6

    1D:
        major:
        H_MAJOR: 90.6
        L_MAJOR: 84.4
        sr:
        SR_1: 93.4
        SR_2: 89.5
        SR_3: 88.4
        poc:
        POC_1: 95.7
        POC_2: 93.0
        POC_3: 90.2
        POC_4: 84.6
        POC_5: 79.7
        zones:
        SELL_1: 94.2
        SELL_2: 91.1
        BUY_1: 83.5-86.0
        session:
        PDH: 90.6
        PDL: 87.9
        active:
        H_FSB: 90.4
        inactive:
        L_BOS: 87.7
        L_FSB: 85.2

    4H:
        major:
        H_MAJOR: 90.6
        L_MAJOR: 84.4
        sr:
        {}
        poc:
        POC_1: 92.4
        POC_2: 88.1
        POC_3: 86.4
        POC_4: 82.2
        zones:
        SELL_1: 88.8-89.7
        BUY_1: 85.2-86.0
        NEUTRAL: 87.7
        active:
        H_FSB: 90.4
        inactive:
        H_CHOCH: 89.4
        L_FSB: 85.2

    1H:
        major:
        H_MAJOR: 88.9
        L_MAJOR: 87.1
        sr: {}
        poc: {}
        zones:
        SELL_1: 88.5
        SELL_2: 88.0
        active:
        L_BOS: 87.9
        inactive:
        L_CHOCH: 89.4
    ```

    ### Weekly (1W – Super-HTF Structure)

    * **Previous (~30 candles):** Post-`ALL.ath` / `1M.major.H_MAJOR` distribution, then weekly trend damage via `1W.active.L_MSB` → accelerated sell-off that **confirmed** `1W.active.L_BOS` (weekly bull structure broken). That sell leg pushed price down through the historic dynamic bull support band (ascending `1W_50EMA/MA`) and into **monthly demand** at `1M.zones.BUY_2`, with acceptance toward `1M.poc.POC_4` / `1M.sr.SR_4`. Supply remains layered overhead: `1W.zones.SELL_3` then higher `1W.zones.SELL_2`.
    * **Current (~5 candles):** Multi-week basing just above/around `1W.sr.SR_3` and `1W.poc.POC_4`, still **under** `1W.zones.SELL_3`. Weekly bias remains **recovery-attempt inside a larger corrective regime** while price is below the broken bull support (`1W_50EMA/MA`) and the prior structural break `1W.active.L_BOS`. (No weekly chart provided here; this is anchored to your HTF description + key levels.)

    ---

    ### Daily (1D – HTF for intraday)

    * **Previous (~30 candles):** Strong downtrend into `1W.major.L_MAJOR` (monthly demand region) culminated in an absorption `1D_bearish_hammer_HVC` (capitulation signature) with deeply oversold `1D_RSI` (<25). From that base, price formed a `1D_ascending_wedge` recovery, then broke down with `1D.inactive.L_BOS` toward `1D.zones.BUY_1`, before reclaiming trend supports (reclaim of `1D_9EMA` + `1D_W_VWAP`) and rotating back up into the range top.
    * **Current (~5 candles):** Retest/stop-run near `1D.major.H_MAJOR` rejected via `1D.active.H_FSB` printed as `1D_bearish_doji-long-upper-wick_VC` (clear supply response). Follow-through is rotating back down toward `1D.session.PDL` and the mid/lower acceptance area around `1D.sr.SR_3` / `1D.inactive.L_BOS`, with the nearby “magnet” still being `1D.poc.POC_3` on any mean-reversion bounce. Bias: **bearish-to-neutral** while below `1D.sr.SR_2` and below the rejection complex at `1D.major.H_MAJOR`.

    ---

    ### 4H (4H – HTF for 1H)

    * **Previous (~30 candles):** Last week failed breakdown/reversal behavior from the lower range led to a low-volume drift upward into the **key confluence**: `4H/1D.major.H_MAJOR` + `1D.zones.SELL_2` + descending `4H_200MA/EMA`. Rejection printed `4H_bearish_spinning-bar_HVC` (effort + stall), then price began rotating back toward the mid-range.
    * **Current (~5 candles):** Post-rejection impulse drove into/through `4H.zones.NEUTRAL` with price now behaving as **mid-range acceptance / pivot battle**. Overhead friction: `4H.poc.POC_2` and the underside of `4H.zones.SELL_1`. Below, the next demand/acceptance shelf is `4H.poc.POC_3` then `4H.zones.BUY_1`. 4H bias: **neutral-bearish** unless reclaiming and holding above `4H.zones.NEUTRAL` with improving VPA/CVD.

    ---

    ### 1H (1H – TTF)

    * **Previous (~30 candles):** Post-rally failure at `1D/4H.major.H_MAJOR` transitioned into a strong sell sequence that produced `1H.inactive.L_CHOCH` followed by `1H.active.L_BOS`, cascading toward the mid-range pivot `4H.zones.NEUTRAL`. The sell leg found responsive buyers at `1H.major.L_MAJOR` (range low defense), but structure remains **lower-high / lower-low** biased until a confirmed bullish structure break occurs.
    * **Current (~5 candles):** Price is attempting a corrective pullback from `1H.major.L_MAJOR` back toward `1H.zones.SELL_2` → `1H.zones.SELL_1`, with confluence friction from `1H_S_VWAP` and the descending `1H_9/21EMA` band. While `1H.active.L_BOS` remains intact and price is capped below `1H.zones.SELL_1/2`, treat bounces as **sell-the-rip candidates** unless LTF prints a clean bullish reversal (MSB) and holds above `4H.zones.NEUTRAL`.

    ---

    ## MACRO CONTEXT
    ### LAST WEEK

    * **US inflation (CPI, Nov; released Thu Dec 18)**

    * Headline CPI: **+0.2% SA over the 2 months (Sep→Nov)**; **+2.7% YoY**.
    * Core CPI (ex-food/energy): **+0.2% SA over 2 months**; **+2.6% YoY**.
    * Over the same 2-month window: **Energy +1.1%**, **Food +0.1%**.
    * 12-month components highlighted in the release: **Energy +4.2% YoY**, **Food +2.6% YoY**.
    * **Data caveat:** October CPI survey collection was missed due to the federal funding lapse; CPI data collection **resumed Nov 14** → higher uncertainty/seasonality distortion risk in “holiday discount” period comparisons.
    * **US labor (Weekly Jobless Claims; released Thu Dec 18)**

    * Initial claims (wk ending **Dec 13**): **224k** (**-13k WoW**).
    * 4-wk avg initial claims: **217.5k** (**+0.5k WoW**).
    * Continuing claims (wk ending **Dec 6**): **1.897M** (**+67k WoW**).
    * **US demand (Retail Sales, Oct; released Tue Dec 16, delayed)**

    * Headline: **$732.6B**, **~0.0% m/m (virtually unchanged)**; **+3.5% YoY**.
    * Aug–Oct total sales: **+4.2% YoY**.
    * Notables: **Nonstore retailers +9.0% YoY**; **Food services & drinking places +4.1% YoY**.
    * **US activity pulse (S&P Global “flash” PMI, Dec; released Tue Dec 16)**

    * Composite: **53.0** (Nov: **54.2**).
    * Services: **52.9** (Nov: **54.1**).
    * Manufacturing: **51.8** (Nov: **52.2**).
    * **US consumer (U. Michigan final, Dec)**

    * Sentiment index: **52.9** (Nov: **51.0**).
    * Current conditions: **50.4**; Expectations: **54.6**.
    * **US housing (Existing Home Sales, Nov; released Fri Dec 19)**

    * Sales: **4.13M SAAR** (**+0.5% m/m**, **-1.0% YoY**).
    * Median price: **$409,200** (**+1.2% YoY**).
    * Inventory: **1.43M** (**-5.9% m/m**, **+7.5% YoY**); **4.2 months** supply.
    * **Global central banks (risk/FX spillovers into US session)**

    * **BoE:** Bank Rate **cut 25bp to 3.75%**.
    * **ECB:** Held policy rates (Deposit **2.00%**, Main refi **2.15%**, Marginal lending **2.40%**).
    * **BoJ:** **Raised** policy rate (overnight call rate target) to **~0.75%** (from **0.50%**).
    * **Fed / political overhang**

    * Fed speakers continued to lean **“pause/hold for months”** after the 2025 easing cycle; tariff-related inflation uncertainty remains a stated concern (Trump policy channel + data-quality caveats).

    ---

    ### THIS WEEK

    * **Holiday/market structure (liquidity + timing risk)**

    * **Wed Dec 24:** US equities **early close** (NYSE/Nasdaq) **1:00pm ET**.
    * **Thu Dec 25:** **US markets closed** (Christmas).
    * **Bond market:** recommended **2:00pm ET** close on **Dec 24**.
    * **Federal offices:** Trump ordered **federal offices closed Dec 24 and Dec 26** (markets still open) → expect thinner staffing/liquidity + headline sensitivity.
    * **Key US macro releases (all times ET)**

    * **Wed Dec 24**

        * **08:30** — **Weekly Jobless Claims** (wk ending **Dec 20**) **rescheduled** due to Christmas week.
    * **Context note:** multiple releases remain **rescheduled/condensed** from the 2025 funding lapse → higher probability of “surprise prints” and lower signal-to-noise.

    ---

    ### MACRO ANALYSIS

    Holiday liquidity + a **data-dense Tuesday (GDP/IP/Durables/Confidence)** makes today’s US session prone to **positioning-driven moves** and **outsized reactions** to surprises. The key cross-asset hinge is the **rates/USD impulse**: a hotter growth/inflation mix tends to push **yields & USD up** (headwind for **gold** and often for **high-beta risk** like **BTC/ETH**), while softer growth/confidence tends to pull **yields down** (supportive for **gold**, and can be supportive for **SPX/BTC** if the market interprets it as “Fed easing runway” rather than recession risk). Trump/tariff headlines remain an asymmetric volatility catalyst because they directly feed the **inflation risk premium**.

    #### BTC & ETH

    BTC/ETH still behave as **high-beta liquidity/risk proxies** in US hours: they tend to track **Nasdaq/SPX risk appetite** and **USD liquidity conditions**. Thin liquidity into Christmas increases the chance of **stop-runs/long wicks** around key levels, especially if Tuesday’s GDP/rates reaction is sharp. A **yields-up** impulse is the main near-term headwind; a **yields-down** impulse can help crypto rebound provided equity risk doesn’t flip into “growth scare.”

    
    # TRADING PLAN FOR 1H_TTF (Trigger • Location • Context)

    **Session stance:** 4H is **neutral-bearish** around `4H.zones.NEUTRAL`; 1H is **bearish** post `1H.active.L_BOS`. Expect thinner/liquidity-choppy conditions into the holiday window → **demand strict trigger confirmation; no chasing**.

    ---

    ### WHITE_A — Short continuation on pullback into 1H supply

    * **Context**: Aligned bearish (4H neutral-bearish + 1H bearish). Current move looks like a corrective pullback from `1H.major.L_MAJOR` back into overhead friction (`1H_9/21EMA` + `1H_S_VWAP`). Prefer weak bullish VPA on pullback (decreasing VCs) + bearish CVD rollover before engaging.
    * **Location**: PEZ at `1H.zones.SELL_2` → `1H.zones.SELL_1` (LVN supply) with dynamic resistance from `1H_9/21EMA` + `1H_S_VWAP`.
    * **Trigger**: LTF creates a bearish rejection sequence: sweep into the zone → **LTF_L_MSB** (realign down) + low-volume retest of the MSB flip zone; CVD turning down confirms.
    * **Invalidation**: Acceptance above `1H.zones.SELL_1` **and** sustained hold above `4H.poc.POC_2` (supply reclaimed → pullback thesis breaks).
    * **Setup Priority**: **A+**

    ---

    ### ORANGE_A — Short reversal from 4H supply (HTF confluence)

    * **Context**: Best “sell-the-rip” if price mean-reverts upward into the strongest HTF confluence. We require proof of absorption/weak buyers (no bullish ignition; CVD fails to confirm).
    * **Location**: `4H.zones.SELL_1` aligning with the upper rejection complex near `4H/1D.major.H_MAJOR` and the broader supply reference `1D.zones.SELL_2`.
    * **Trigger**: On the 1H/15m: print a stop-run into the zone → **TTF_L_MSB** (or decisive CHOCH failure) + bearish follow-through; pullback must be low-volume; CVD rolls over (LHs).
    * **Invalidation**: Clean acceptance above `4H.zones.SELL_1` with rising CVD and bullish ignition HVC (don’t fade strength).
    * **Setup Priority**: **A**

    ---

    ### PURPLE_A — Short fade on failed breakout (FSB at range-top complex)

    * **Context**: Range-fade inside neutral-bearish regime: only valid if the push up is **wicky** and unsupported by CVD (classic failed breakout).
    * **Location**: Failure pattern at/near `4H.zones.SELL_1` / `4H.poc.POC_2` (overhead supply shelf).
    * **Trigger**: 1H prints **H_FSB** behavior (break above then close back below) + LTF_L_MSB confirming sellers regained control; enter the retest from below.
    * **Invalidation**: 1H holds above the failed-break level and flips it to support (FSB fails → step aside).
    * **Setup Priority**: **B+**

    ---

    ### PINK_A — Short momentum scalp under VWAP/EMAs (continuation pressure)

    * **Context**: If price cannot reclaim `1H_S_VWAP` and `1H_9/21EMA` and keeps rejecting under `4H.zones.NEUTRAL`, expect momentum “push” legs and shallow retests. This is a **scalp**, not a swing.
    * **Location**: Under `4H.zones.NEUTRAL`, using the first pullback rejection under `1H_S_VWAP` / `1H_9/21EMA` as the working area.
    * **Trigger**: LTF_L_BOS (continuation) with bearish HVC + falling CVD; enter either on the BOS or the immediate shallow retest (no deep pullback required).
    * **Invalidation**: Reclaim + hold above `4H.zones.NEUTRAL` and sustained trade above `1H_S_VWAP` (momentum edge gone).
    * **Setup Priority**: **B**

    ---

    ### RED_A — Short breakdown below the 1H floor (structural continuation)

    * **Context**: “Break-and-retest” continuation if the range floor gives way. Only engage if breakdown shows **clear bearish effort** (no absorption signals at the lows).
    * **Location**: Breakdown through `1H.major.L_MAJOR` with acceptance below `4H.zones.NEUTRAL`.
    * **Trigger**: Decisive 1H continuation via **1H_L_BOS** + bearish ignition VC; then wait for a low-volume retest of the broken level from below (AEZ via LTF_L_MSB/BOS).
    * **Invalidation**: Sharp reclaim back above `1H.major.L_MAJOR` with bullish ignition + rising CVD (classic breakdown failure → don’t fight it).
    * **Setup Priority**: **B+**

    ---

    ## LONG (Counter-trend / Reversal Conditions Only)

    ### BLUE_A — Long fade at mid-range pivot (failed breakdown reclaim)

    * **Context**: Counter-trend bounce only if sellers show exhaustion near `4H.zones.NEUTRAL` and LTF prints bullish divergence with confirmation (no knife-catching).
    * **Location**: Sweep/failed breakdown around `4H.zones.NEUTRAL` and the nearby daily floor reference `1D.session.PDL`.
    * **Trigger**: LTF bullish divergence (RSI/CVD) + **LTF_H_MSB** after a sweep; confirm with reclaim/hold above `1H_S_VWAP` before entry.
    * **Invalidation**: Acceptance below `4H.zones.NEUTRAL` with bearish HVC and continued negative CVD (support not holding).
    * **Setup Priority**: **B-**

    ---

    ### TEAL_A — Long momentum scalp on reclaim of key intraday controls

    * **Context**: Only if price proves control shift intraday (reclaim VWAP + reclaim micro-structure). Treat as quick mean-reversion toward overhead HVN/POC shelves.
    * **Location**: Reclaim above `1H.active.L_BOS` plus hold above `1H_S_VWAP` and `1H_9EMA` (first sign the bounce is real).
    * **Trigger**: LTF_H_BOS/MSB on a retest that holds above reclaimed VWAP/EMA with rising CVD.
    * **Invalidation**: Immediate failure back below `1H.active.L_BOS` and `1H_S_VWAP` (reclaim was a trap).
    * **Setup Priority**: **B**

    ---

    ### YELLOW_A — Long major reversal from 4H demand (deep support play)

    * **Context**: This is the “real reversal” attempt and requires the most patience. Only consider if price reaches major demand and prints confirmed reversal structure (TTF trend death).
    * **Location**: `4H.zones.BUY_1` overlapping the daily structural base `1D.major.L_MAJOR` and the broader demand region `1D.zones.BUY_1`.
    * **Trigger**: **TTF_H_MSB** against the bearish trend (confirmed with meaningful volume) → then enter the first low-volume pullback to the flip zone on an LTF bullish trigger.
    * **Invalidation**: Continued acceptance below `4H.zones.BUY_1` with sell-side HVC and no CVD recovery (demand failing).
    * **Setup Priority**: **A-**

    ---

    ### GREEN_A — Long breakout reversal (trend-flip acceptance)

    * **Context**: Only valid if the market proves a real bull reclaim (not just a squeeze). This is the “stand aside until confirmed” reversal plan.
    * **Location**: Break/acceptance above `1H.major.H_MAJOR` (trend flip on 1H) and then continuation acceptance through the higher ceiling `1D.zones.SELL_2` (major overhead gate).
    * **Trigger**: Confirm **1H_H_MSB/BOS** with bullish ignition VC + rising CVD → then low-volume pullback retest; execute on LTF_H_MSB continuation.
    * **Invalidation**: Failed acceptance back below `1H.major.H_MAJOR` (or immediate bearish CHOCH after entry) → treat as bull trap.
    * **Setup Priority**: **B**

    
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
```

### LLM_TRADER 
```
    # 1. TTI (TIMEFRAME TREND IDENTIFICATION)

    ```
    <1D>
    HTF: BEARISH* (refers to 1W Overall Assessment)
    PA: BEARISH (price = 87,866)
    VWAP: price < S_VWAP (87,952) / W_VWAP (88,749) / M_VWAP (89,509) -> BEARISH
    RSI: RSI_MA = 43.25, RSI = 43.75 -> NEUTRAL-BEARISH
    MA: EMA_9=88,214, EMA_21=89,188, EMA_50=93,345, EMA_200=101,836, SMA_200=107,774 -> BEARISH
    OVERALL-ASSESSMENT: BEARISH
    ```

    ```
    <4H>
    HTF: BEARISH (refers to 1D Overall Assessment)
    PA: BEARISH (price = 87,866)
    VWAP: price < W_VWAP (88,848) -> BEARISH
    RSI: RSI_MA = 53.43, RSI = 46.84 -> BEARISH
    MA: EMA_9=88,234, EMA_21=88,273, EMA_50=88,338, EMA_200=90,987, SMA_200=89,092 -> BEARISH
    OVERALL-ASSESSMENT: BEARISH
    ```

    ```
    <1H>
    HTF: BEARISH (refers to 4H Overall Assessment)
    PA: NEUTRAL-BEARISH (price = 87,866)
    VWAP: price ~= S_VWAP (87,854) -> NEUTRAL
    RSI: RSI_MA = 38.77, RSI = 42.26 -> NEUTRAL-BULLISH*
    MA: EMA_9=87,811, EMA_21=88,145, EMA_50=88,384, EMA_200=88,355, SMA_200=87,702 -> NEUTRAL-BEARISH
    OVERALL-ASSESSMENT: NEUTRAL-BEARISH
    ```

    # 2. CAS (CONTEXT ANALYSIS)

    ```
    [CAS]
    Trader Context: London session is active with 2 hours until US open. It is Christmas week with thin liquidity, heightening the risk of wicks/stop-runs. Major data (GDP/Durable Goods) has just released with mixed signals ("hot" GDP vs weak Durables), likely causing chop before a directional move.
    Macro Context: The "hot" GDP (4.3%) supports a hawkish rate repricing (bearish for risk), while weak Durables suggests manufacturing softness. The net impulse is likely USD strength/Yields up, acting as a headwind for BTC.
    Technical Context: HTF (1W/1D/4H) structure is firmly bearish, with price rejected at 90.6k and trading below key VWAPs. 1H is consolidating at S_VWAP (~87.8k) but remains capped by overhead supply at 88.5k-89k.
    Aggregate: Bias=Bearish, Posture=With-trend, Risk=High, Confidence=3, Invalidation=Reclaim of 1H.major.H_MAJOR (88.9k) and W_VWAP (~88.9k).
    ```

    # 3. SPP (STRATEGIC PLANNING PROTOCOL)

    ### Plan Comparison Matrix

    | Plan | Bias | PRO (≤5) | CON (≤5) | SP | PG | Timing Window |
    | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
    | **WHITE_A** | Bearish | • Aligns with HTF/TTF bearish trend<br>• Uses overhead supply/EMA confluence<br>• High probability "sell the rip" | • Requires a bounce to 88.5k (might not reach)<br>• Holiday chop may overshoot zones | A+ | **A** | London/US |
    | **ORANGE_A** | Bearish | • Best location (HTF Supply)<br>• Strongest invalidation point<br>• High R:R potential | • Price is far away (~89k)<br>• Requires strong counter-trend rally first | A | **A** | US Session |
    | **RED_A** | Bearish | • Aligns with immediate momentum<br>• Targets weak range lows | • Breakdown plays risky in low liquidity<br>• Prone to "bear traps" / SFP | B+ | **B+** | US Open |
    | **PINK_A** | Bearish | • Capitalizes on immediate weakness<br>• Good for scalping under VWAP | • Lower R:R<br>• susceptible to intraday noise | B | **B** | London/US |
    | **BLUE_A** | Bullish | • Plays the range support defense<br>• Good R:R if range holds | • Counter-trend (HTF Bearish)<br>• Catching a falling knife risk | B- | **C+** | Any |
    | **TEAL_A** | Bullish | • Momentum scalp on reclaim | • Requires fighting dominant trend<br>• Overhead supply is very close | B | **C** | US Session |
    | **YELLOW_A** | Bullish | • Major HTF demand zone play | • Price is currently far above zone | A- | **B** | Late US |
    | **GREEN_A** | Bullish | • Confirmed reversal play | • Low probability given macro/techs | B | **C-** | N/A |
    | **PURPLE_A** | Bearish | • Fade setup on fakeout | • Requires specific FSB pattern | B+ | **B** | US Session |

    ### Ranked Shortlist

    | Rank | Plan | PG | Why Now | Key Risk | Invalidation |
    | :--- | :--- | :--- | :--- | :--- | :--- |
    | 1 | **WHITE_A** | **A** | Price is consolidating near S_VWAP; a relief bounce to 88.5k is the ideal entry for the next leg down. | Choppy overlap at EMA_21 could invalidate early entries. | Acceptance > 88.9k |
    | 2 | **ORANGE_A** | **A** | If GDP data triggers a volatility spike, this catches the exhaustion at the top of the range. | Momentum ignition through 90k. | Acceptance > 90.6k |
    | 3 | **RED_A** | **B+** | If the market digests "hot GDP" as purely bearish, support at 87.1k may break quickly. | Liquidity grab/SFP at the lows (Bear Trap). | Reclaim > 87.9k |
    | 4 | **PINK_A** | **B** | Immediate scalp if price fails to hold S_VWAP (87.8k) right now. | Whipsaw around S_VWAP. | Reclaim > 88.0k |
    | 5 | **YELLOW_A** | **B** | If RED_A triggers and extends, this is the target for the bounce. | Catching a falling knife during capitulation. | Loss of 84.4k |

    # 4. DEVIL'S ADVOCATE

    *   **Bullish Case:** The "Hot GDP" (4.3%) could be interpreted by algos as "Recession Cancelled," triggering a risk-on rally despite the rate implications, especially in a thin holiday market where positioning is heavily skewed short. If `1H.major.H_MAJOR` (88.9k) is reclaimed, the bearish thesis for the day collapses, and we could see a squeeze to 90k+.
    *   **Liquidity Trap:** With Christmas week volumes, standard technical breakdowns (like RED_A) have a high failure rate. The market may simply chop between 87k and 89k, stopping out both breakout and breakdown traders before the real move occurs next week.
    *   **Data Noise:** The divergence between GDP (Strong) and Durables (Weak) creates a "muddy" macro picture. This often leads to a "Bart Simpson" pattern—sharp move up, consolidation, sharp move down—wrecking directional bias.

    # 5. TLDR with ACTION PLAN

    **Current Status:**
    BTC is in a **Bearish** posture on HTF (1D/4H), currently consolidating around **87.8k (S_VWAP)**. The immediate trend is capped by EMAs and overhead supply. Macro data is mixed but leans hawkish (rates up), supporting the bearish technical bias.

    **Action Plan:**
    1.  **Primary Focus (Sell Rallies):** Wait for a low-volume corrective bounce into **88.5k - 88.9k** (`1H.zones.SELL_1` / `1H_21EMA`). Execute **WHITE_A** upon a confirmed 15m bearish reversal (MSB/Candle signal).
    2.  **Secondary Focus (Breakdown):** If price loses **87.1k** with volume, look for **RED_A** (break-retest) targeting 85k. *Caution: Wait for candle close to avoid holiday liquidity wicks.*
    3.  **Defensive Posture:** Do not long unless price hits major HTF demand (**85.2k**, **YELLOW_A**) or reclaims **89k** with conviction.

    **Immediate Watch:**
    Monitor reaction at **87.8k (S_VWAP)**. Losing this level opens the path to 87.1k. Holding it allows for the setup of WHITE_A.
```
## TURN 2

### USER 
```
    # TRADER
    Here is PA so far and we are currently 1 hour into US session. 

    # TECHNICAL:
    4H: Price continued its bearish leg from the prior rejection at 1D range high and is currently retesting slightly below 4H.zones.NEUTRAL. We have volume picking up within this bearish legs and is much more cumulative compare to the prior bullish leg up 

    1H: Price rejected just under WHITE_A PEZ + S_VWAP/1H_9EMA and topped at fresh 1H.major.H_MAJOR at 88k, followed by a rolled over with a 1H candle closed below 1H.major.L_MAJOR/4H_NEUTRAL with OBV/RSI/CVD confirmation supported by a 1H_bearish_large-body_HVC into US session, triggering red_A position active. Price is now retest the current the broken level from below with potential upward toward new 1H_SELL_1 supply zone at 87.3-87.6k and the fresh 1H.major.H_MAJOR at 88k. 

    15m: 15m_L_BOS into US session at 87.4k with a 15m_bearish_engulfing_SHVC with CVD/RSI/OBV confirmed. Bottomed at 15m_L_MAJOR at 86.6k on oversold RSI (20) and currently recovering up to retest RED_A PEZ

    # COMMENT:
    ## 1
    Given this development context please reurn the SPP for the relevant plans, which include:
    - RED_A
    - WHITE_B (new): continuation of 1H trend with pullback to new 1H_SELL_1 supply + 4H_NEUTRAL pivot (SP = A+)
    - PURPLE_B (new): fade with H_FSB at 1H_H_MAJOR (SP = A-)
    - BLUE_A (mod): anticipating this is a failed break

    # NOTE
    Do not hallucinate SP grades 
```

### LLM_TRADER 
```
    # 1. TTI (TIMEFRAME TREND IDENTIFICATION)

    ```
    <1D>
    HTF: BEARISH* (refers to 1W Overall Assessment)
    PA: BEARISH (price = 86,924)
    VWAP: price < S_VWAP (87,488) / W_VWAP (88,505) / M_VWAP (89,491) -> BEARISH
    RSI: RSI_MA = 43.09, RSI = 41.53 -> BEARISH
    MA: EMA_9=88,025, EMA_21=89,103, EMA_50=93,308, EMA_200=101,827, SMA_200=107,769 -> BEARISH
    OVERALL-ASSESSMENT: BEARISH
    ```

    ```
    <4H>
    HTF: BEARISH (refers to 1D Overall Assessment)
    PA: BEARISH (price = 86,924)
    VWAP: price < W_VWAP (88,659) -> BEARISH
    RSI: RSI_MA = 53.00, RSI = 40.82 -> BEARISH
    MA: EMA_9=88,045, EMA_21=88,187, EMA_50=88,301, EMA_200=90,977, SMA_200=89,088 -> BEARISH
    OVERALL-ASSESSMENT: BEARISH
    ```

    ```
    <1H>
    HTF: BEARISH (refers to 4H Overall Assessment)
    PA: BEARISH (price = 86,924)
    VWAP: price < S_VWAP (87,656) -> BEARISH
    RSI: RSI_MA = 35.99, RSI = 30.80 -> BEARISH (Oversold)
    MA: EMA_9=87,451, EMA_21=87,884, EMA_50=88,239, EMA_200=88,318, SMA_200=87,663 -> BEARISH
    OVERALL-ASSESSMENT: BEARISH
    ```

    # 2. CAS (CONTEXT ANALYSIS)

    ```
    [CAS]
    Trader Context: US Session is 1 hour in. "Hot GDP" data likely fueled the breakdown, driving price below the 87.1k floor. Liquidity remains thin (Christmas week), increasing the risk of "V-shape" recoveries or deep wicks.
    Macro Context: Strong GDP (4.3%) reinforces a "higher for longer" rate fear, strengthening USD and pressuring risk assets like BTC. The macro impulse aligns with the technical breakdown.
    Technical Context: 1H structure has confirmed a breakdown of `1H.major.L_MAJOR` (87.1k) with a high-volume bearish candle. Price is now in "Break & Retest" mode. 1H RSI is oversold (30.8), suggesting the current bounce is a technical relief rally into overhead resistance (87.1k-87.6k).
    Aggregate: Bias=Bearish, Posture=With-trend, Risk=Medium, Confidence=4, Invalidation=Reclaim of 88.0k (1H.major.H_MAJOR).
    ```

    # 3. SPP (STRATEGIC PLANNING PROTOCOL)

    ### Plan Comparison Matrix

    | Plan | Bias | PRO (≤5) | CON (≤5) | SP | PG | Timing Window |
    | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
    | **WHITE_B** | Bearish | • Aligns with strong 1H bearish trend<br>• Targets fresh supply + 1H_9EMA confluence<br>• Ideal R:R for continuation | • 1H RSI is oversold (30); bounce may extend<br>• Requires patience for pullback to 87.4k | A+ | **A** | US Session |
    | **RED_A** | Bearish | • Immediate retest of broken major structure<br>• Confirmed by 1H breakdown candle | • Selling into oversold conditions<br>• Risk of "Bear Trap" / SFP at 87.1k | A | **A-** | Now |
    | **PURPLE_B** | Bearish | • Strongest invalidation level (88k)<br>• Fades a "failed breakdown" recovery | • Requires price to reclaim 87.1k first<br>• Counter-momentum if trend is strong | A- | **B+** | Late US |
    | **BLUE_A** | Bullish | • Plays the SFP/Liquidity Grab thesis<br>• 15m SHVC at lows suggests absorption | • Fighting dominant trend & macro<br>• Requires reclaiming 87.6k to confirm | B- | **C+** | US Session |

    ### Ranked Shortlist

    | Rank | Plan | PG | Why Now | Key Risk | Invalidation |
    | :--- | :--- | :--- | :--- | :--- | :--- |
    | 1 | **WHITE_B** | **A** | Price is bouncing from oversold conditions; 87.3k-87.6k is the "sweet spot" where 9EMA and Supply meet. | Momentum overshoot above 87.6k. | Acceptance > 88.0k |
    | 2 | **RED_A** | **A-** | The retest of the broken floor (87.1k) is happening *now*. Immediate feedback loop. | SFP (Fake breakdown) reclaiming 87.1k. | Reclaim > 87.4k |
    | 3 | **PURPLE_B** | **B+** | If the current bounce is stronger than expected (short squeeze), this catches the trap at the range high. | Bullish ignition through 88k. | Acceptance > 88.5k |
    | 4 | **BLUE_A** | **C+** | Only valid if sellers fail to hold the breakdown level (87.1k) and price V-shapes. | Catching a falling knife. | New Low < 86.6k |

    # 4. DEVIL'S ADVOCATE

    *   **The "Oversold" Trap:** 1H RSI is at 30.8. Historically, shorting immediately when RSI < 30 on the 1H often leads to getting squeezed by a relief rally. The breakdown is real, but the *entry* timing is dangerous. A bounce to 87.5k (clearing early shorts) is highly probable before the real drop to 85k.
    *   **Holiday Liquidity:** The breakdown volume (357 on 1H) was decent but not "capitulation" level. The 15m SHVC at the low (86.6k) suggests a buyer stepped in. If this was just a stop-run on long leverage, price could snap back to 88k rapidly, invalidating the bearish immediate term.
    *   **Macro Digestion:** Markets often overreact to headlines (GDP) then reverse. If equities stabilize, BTC correlates may lift price back into the range.

    # 5. TLDR with ACTION PLAN

    **Current Status:**
    BTC has confirmed a **Bearish Breakdown** of the 87.1k floor. The 1H trend is firmly down, but RSI is oversold (30), triggering a relief bounce. We are currently retesting the breakdown zone from below.

    **Action Plan:**

    1.  **Primary Execution (WHITE_B / RED_A):**
        *   **Zone:** Monitor **87.1k - 87.6k** (Broken Floor + 1H_9EMA + New Supply).
        *   **Trigger:** Wait for the current 15m bounce to stall. Look for a **15m Bearish Candle (Engulfing/Pinbar)** or **15m_L_MSB** within this zone.
        *   **Target:** 86.6k (Low), then **85.2k** (4H Demand).
        *   **Invalidation:** Hard stop if price reclaims and holds above **88.0k**.

    2.  **Alternative (PURPLE_B):**
        *   If price blasts through 87.6k, do not chase longs. Wait for a rejection at **88.0k** (Prior High) to fade the move.

    3.  **Defensive:**
        *   **BLUE_A** is low probability. Only consider longs if price reclaims **87.6k** AND holds it as support, proving the breakdown was a trap.

    **Immediate Watch:**
    Price is approaching **87.1k - 87.3k**. Watch 15m CVD. If CVD remains flat/down while price rises (Bearish Divergence), execute the Short Plan.
```

## TURN 3

### USER
```
# TRADER
We are currently 2.5 hours into US session. We have made a RED_A position but failed and executed the WHITE_B position after price made a deeper retest. 

# TEHNICAL:
Price made a much deeper pullback than expected and currently retesting the 15m_L_BOS level confluenced with 15m_9/21EMA after surging above 1H_L_MAJOR broken level on lower and decreasing 15m volume. 

# COMMENT
## 1
Please run TEA to grade execution + TMI on management with all TP tiers and corresponding percentage for the WHITE_A position with the following setup:
- Thesis on 1H bearish trend continuation following a confirmed break of 1H.major.L_MAJOR with high volume. This is a 1H swing position. 
- Execution on a 3m_H_FSB with CVD beairsh divergence signals at WHITE_B PEZ followed by a rejection with CVD confirmation. 
- SL at 1H_H_MAJOR at 88k. 
- Soft invalidation on a 1H_H_CHOCH/15m_H_MSB. 
- FTA at 15m_L_MAJOR.

## 2
What is the biggest risk toward this position and how do we manage this moving forward? When or should we look to add to this position?
 

```

### LLM_TRADER
```
# 1. TTI (TIMEFRAME TREND IDENTIFICATION)

```
<1H>
HTF: BEARISH (refers to 4H Overall Assessment)
PA: BEARISH (price = 87,390)
VWAP: price < S_VWAP (87,640) -> BEARISH
RSI: RSI_MA = 36.64, RSI = 39.90 -> BEARISH
MA: EMA_9=87,544, EMA_21=87,926, EMA_50=88,257, EMA_200=88,323, SMA_200=87,665 -> BEARISH
OVERALL-ASSESSMENT: BEARISH
```

# 2. CAS (CONTEXT ANALYSIS)

```
[CAS]
Trader Context: US Session is 2.5 hours in. Liquidity is thinning as the initial "Hot GDP" volatility settles. The market is digesting the breakdown of 87.1k with a deep technical retest.
Macro Context: The macro impulse remains bearish (Rates/USD up), but the initial shock has passed, leading to a standard technical mean-reversion (pullback) before trend resumption.
Technical Context: 1H trend is bearish, but price has wicked back above the breakdown level (87.1k) to test the `1H_9EMA` (87.5k) and `15m_21EMA`. This is a critical "make or break" retest zone. Volume on the pullback is decreasing, suggesting corrective action rather than a reversal.
Aggregate: Bias=Bearish, Posture=With-trend, Risk=Medium, Confidence=4, Invalidation=Acceptance above 87.6k (1H Supply start).
```

# 3. TEA (TRADE EXECUTION ASSESSMENT)

### SG Reasoning Notes
```
[WHITE_B - Executed]
Context: A — Aligned with 1H bearish breakdown and macro headwinds. Pullback into supply is the standard entry model.
Confluence: B+ — Price is testing the 1H_9EMA (87.5k) and the underside of the 15m breakdown origin. It has pierced the 87.1k level (slightly messy) but remains below S_VWAP (87.6k).
Catalyst: A — 3m_H_FSB + Bearish CVD Divergence provides a precise, low-risk entry trigger at the top of the pullback.
SG Result: A- — Strong setup, though the deep pierce of 87.1k requires careful monitoring.
```

### SG Decision Table
| Plan | PG | SG | Overall | Verdict | Why | Next Check |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **WHITE_B** | **A** | **A-** | **A-** | **HOLD** | Valid entry on LTF trigger at key resistance (`1H_9EMA`); volume dropping on pullback. | Price must lose **87.1k** to confirm thesis. |

# 4. TMI (TRADE MANAGEMENT IDENTIFICATION)

```
TRADE MANAGEMENT IDENTIFICATION:
Current Position: SHORT (WHITE_B)
Trade Setup Type: Continuation (Swing)
Trade Timeframe: 1H_TTF – 15m_LTF – 4H_HTF
Trade Thesis: PLANNED – WHITE_B – Bearish continuation following the 1H breakdown of 87.1k. The current move is viewed as a bearish retest of the 1H_9EMA/Supply.
Management Rules: PROACTIVE
Management Plan:
  • Exit Playbook:
    - TP1 (30%): 86.6k (Today's Low / 15m_L_MAJOR). Secure bank to finance the risk.
    - TP2 (40%): 85.2k (4H Demand / 1D.zones.BUY_1). Major structural target.
    - TP3 (30%): 84.4k (1D.major.L_MAJOR). Runner for the breakdown extension.
  • FTA Objectives: 86.6k (15m_L_MAJOR). Expect a reaction/bounce here; move SL to Breakeven once TP1 is hit.
  • Add-On Criteria: 
    - Condition: Price must close back below 87.1k (1H.major.L_MAJOR) on the 15m timeframe.
    - Trigger: A fresh 15m_Bearish_Candle closing below 87.1k with increasing sell volume.
  • Invalidation Triggers:
    - Hard Invalidation: 88.0k (1H.major.H_MAJOR). Structural trend flip.
    - Soft Invalidation: A 15m close above 87.6k (Reclaiming S_VWAP and 1H_9EMA) with rising CVD. This suggests the breakdown was a trap.
  • Active Risk Adjustments: If price stalls at 87.1k and prints a 15m_H_MSB (Bullish), cut risk by 50% or close early.
  • Psychology Check: The deep retest above 87.1k is uncomfortable. Trust the SL at 88k and the decreasing volume on this rise. Do not panic exit unless soft invalidation hits.
```

# 5. RISK & STRATEGY ANALYSIS

### **Biggest Risk: The "SFP" (Swing Failure Pattern) / Bear Trap**
The primary risk is that the breakdown below `87.1k` was a liquidity grab (manipulation) rather than a genuine trend continuation.
*   **The Sign:** Price is currently trading *above* the broken level (87.39k > 87.1k). If it holds here and grinds higher, reclaiming `S_VWAP` (87.6k), the market will view the earlier drop as a "Bear Trap."
*   **The Consequence:** A rapid short squeeze targeting the range highs (88k - 89k) as late shorts (like this position) are forced to cover.

### **Management Strategy**
1.  **The "Line in the Sand" (87.6k):** You are short against the `1H_9EMA` and `S_VWAP`. As long as price stays below **87.6k**, the bearish thesis is valid. If 15m closes above 87.6k, the probability of a squeeze skyrockets—**exit immediately** (Soft Invalidation).
2.  **The Confirmation (87.1k):** The trade is currently "offside" regarding the specific level (87.1k). You need to see price **accept back below 87.1k** within the next 1-2 candles (30 mins).
    *   *Action:* If price hovers at 87.3k-87.5k for >1 hour without dropping, the momentum is fading. Tighten SL to 87.8k to reduce exposure.

### **Adding to the Position**
**DO NOT ADD HERE.** Adding during a deep retest that has pierced the breakdown level is gambling.
*   **When to Add:** Only add **Pyramid Units** once the market proves the "Bear Trap" thesis is wrong.
*   **Specific Trigger:** Wait for a **15m Candle Close < 87.1k** with a bearish volume spike. This confirms that the current rise was just a pullback and sellers have regained control of the floor.

# 6. TLDR with ACTION PLAN

**Current Status:**
Short executed on `WHITE_B`. Price is in a deep retest phase, trading slightly above the broken floor (87.1k) but capped by the `1H_9EMA` (87.5k). Volume is decreasing on the rise (Bearish confirmation).

**Immediate Actions:**
1.  **Hold:** Maintain position with Hard SL at **88.0k**.
2.  **Watch 87.6k:** If 15m closes above **87.6k**, manually close/reduce risk (Soft Invalidation).
3.  **Watch 87.1k:** Look for a drop back below this level to confirm the trade is working.
4.  **TP1:** Set limit buy at **86.6k**.

**Next Check:**
Reassess on the next 1H close. If it closes as a **Bullish Hammer** above 87.1k, the risk of a reversal increases significantly.
```