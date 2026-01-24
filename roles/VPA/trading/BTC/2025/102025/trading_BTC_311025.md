# CONTEXT: 
## TRADER CONTEXT: 
Today is Friday 31st of October 2025, we are in London session, 3 hours until US session. Due to government shutdown, we have not received many major macro economic data such as NFP/Unemployment/PPI for the last 3 week and this is expected to continue this week. Refers to `MACRO CONTEXT` for the rest of the macro events this week. 

We have officially passed September which has been notorious for a BTC and crypto pullbacks during the bull runs year and currently enter Q4 of which has been typical bullish for bitcoin bull cycle. We should favors more bullish setups while remains as cautious as possible until BTC firmly surpasses ATH. 

Last week: BTC recovered after crypto market got the biggest liquiditation sell off in the entire history, while gold has pullback significantly from its bullmarket, signaling risk-on environment supported by dovish FED and soft CPI + Inflation data print last weeks. 

This week: BTC HTF remains neutral with 1W `OVERALL_ASSESSMENT = NEUTRAL` as we are trading within this HTF range given price managed to close above the 1W range low as a confirmed `1W_L_SWEEP` and reclaimed the `1W_20EMA/MA` bull market support bands. Market seems to be respond positive to FED decisions with US equities putting new ATH and BTC recovering. This is also coupled with positive resolution on China-US tariffs news during the weekend that has haunted the market last 3 weeks. We had FOMC on Wednesday, refers to the below regarding all important details:
```markdown
* **Cut 25 bps** to a **3.75%–4.00%** fed-funds target range; **two dissents** (Miran wanted –50 bps; Schmid preferred no change).
* **Ended QT effective Dec 1**: the Committee will **stop shrinking the balance sheet** and **reinvest all principal** thereafter (Treasuries rolled over; **all agency/MBS principal reinvested into T-bills**).
* **Operating settings** (implementation note): **IORB 3.90%**, **ON RRP 3.75%**, **SRF min 4.00%**, $500B aggregate SRF limit, RRP **$160B per-counterparty**.
* **Powell’s tone**: another cut in **December is “not a foregone conclusion,”** stressing data uncertainty amid the shutdown. 
* **Context & reaction**: Statement added emphasis on **rising downside risks to employment**; markets whipsawed as traders digested the **easing + QT end** vs **no December pre-commitment**.

> Why this matters: Ending QT + a 25-bp cut = **easier financial conditions via reserves/liquidity** and **lower policy rate**, but Powell explicitly **kept optionality**, so the **path** (not the single cut) drives cross-asset pricing.
```

Sentiment: Public sentiment for October remain bullish for BTC within this year of its bullish 4 years cycle from a seasonality and historic standpoint. However price action last 2-3 weeks have liquidated millions of leveraged crypto traders and enact some fears with people hypothesizing for the top of the cycle is in for BTC, and the start of an extended bear market into 2026. `Fear & Greed Index` is currently remains at 25-30 in fear terriroty improved from extreme fear from last week. 

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
      SELL_1: 113.9k
      BUY_1: 107.3k
      NEUTRAL: 110.0k
    session:
      PDH: 111.6k
      PDL: 106.3k
    active: 
      H_SWEEP: 116.0k
    inactive:
      H_CHOCH: 114.0k
      L_BOS: 109.6k


  4H:
    major:                 
      H_MAJOR: 113.6k    
      L_MAJOR: 106.3k    
    sr:
      SR_1: 116.4k
    poc: 
      POC_1: 110.8k
      POC_2: 112.5k
      POC_3: 113.6k
      POC_4: 115.0k
    zones:
      SELL_1: 111.9k
      SELL_2: 110.2k
    active:
      L_BOS: 112.1k
    inactive: 
      L_CHOCH: 114.5k
      L_MSB: 112.9k

  1H:
    local:
      H: 110.2k
      L: 108.6k
    major:
      H_MAJOR: 111.6k
      L_MAJOR: 106.3k
    sr: {}
    poc: {}
    zones:
      SELL_1: 109.6k
      BUY_1: 108.6k
    active:
      H_CHOCH: 110.1k
    inactive: 
      L_BOS: 109.2k

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

* **Previous (~30 candles):** Strong advance from late ’24 into `ALL.ath` / `1W.major.H_MAJOR`, then a corrective leg confirmed **`1W.inactive.L_MSB`**, retesting `1M.inactive.H_BOS` and the weekly EMA band. That held and established the range low around `1W.major.L_MAJOR`. Since then, weeks of range trading with both-side liquidity events: **`1W.inactive.H_SWEEP`** at the top, followed **three weeks later** by **`1W.active.L_SWEEP`** near the bottom.
  *Indicators:* `1W_RSI` sits near 50 (neutral); price is **below** `1W_9/21EMA` but well **above** `1W_200EMA/SMA` (bull-market structure intact). Weekly volume is **sub-MA** (no SHVC this week).

* **Current (~5 candles incl. current):** Price bounced from `1W.major.L_MAJOR` and is working back toward the mid-range **`1W.zones.NEUTRAL`** while orbiting the weekly EMA band. Overhead magnets: `1W.poc.POC_2` → `1W.poc.POC_1`; resistance cluster higher at `1W.sr.SR_1` / `1W.poc.POC_4` / `1W.zones.SELL_1`.
  **HTF read:** *Range inside a bull market; bias constructive from `1W.zones.BUY_1` toward `1W.zones.NEUTRAL`, but weekly momentum hasn’t re-ignited yet.*

---

### **1D — HTF for intraday**

* **Previous (~30 candles):** After a push to the 1D range high at `1D.major.H_MAJOR`, price printed **`1D.active.H_SWEEP`** at that high and rolled over from the 1W mid-range with a **`1D_bearish_engulfing_HVC`** (largest sell VC in ~6 months). The dump undercut toward `1D.local.L` / `1D.zones.BUY_1`, swept the weekly range low near `1W.major.L_MAJOR`, then was absorbed and re-accepted inside the weekly range while defending the **rising `1D_200EMA/MA`**.
  *Indicators:* Today price is **below** `1D_9/21/50EMA` but **above** `1D_200EMA/SMA`; `1D_RSI` < 50 (neutral-bearish); daily volume < MA (no fresh HVC).

* **Current (~5 candles incl. current):** The rebound leg from `1D.zones.BUY_1` stalled **below** `1D.zones.NEUTRAL` and `1D.sr.SR_1`. Session refs in play: **`1D.session.PDL`** held; now pivoting between `1D.poc.POC_3` and `1D.poc.POC_2`.
  **HTF read:** *Daily is in a corrective down-leg within the weekly range; watch reactions at `1D.zones.NEUTRAL` above and `1D.zones.BUY_1`/`1D.local.L` below.*

---

### **4H — HTF for 1H**

* **Previous (~30 candles):** Weekend rally toward `1D.major.H_MAJOR` was rejected; **`4H.inactive.L_MSB`** flipped the 4H trend down and **`4H.active.L_BOS`** extended the lower-low sequence into `1D.zones.BUY_1`/`4H.major.L_MAJOR`. The sell leg carried multiple **4H_bearish_HVCs** > prior up-leg VCs.
  *Indicators:* Price is **above** `4H_9EMA` but **below** `4H_21/50/200EMA`; `4H_RSI` < 50; price **above** S-VWAP but **below** W/M-VWAP → still HTF-bearish.

* **Current (~5 candles incl. current):** Bounce off `4H.major.L_MAJOR` is a **lighter-volume** retrace into **`4H.zones.SELL_2`** / `1D.zones.NEUTRAL`, with nearby magnets `4H.poc.POC_1` and `4H.poc.POC_2`.
  **HTF read:** *Counter-trend 4H rally pressing first supply; sellers have the HTF advantage until `4H_21/50EMA` and `4H.poc.POC_2/POC_3` are reclaimed.*

---

### **1H — Trading Timeframe (TTF)**

* **Previous (~30 candles):** From the 4H bottom at `4H.major.L_MAJOR`, price staged a sharp rebound with **`1H.active.H_CHOCH`**, reclaiming `1H_9/21EMA`, `1H_50EMA`, and S-VWAP. Structure rotated to HH/HL locally while price held above `1H.zones.BUY_1`. Session CVD showed a **rising slope** on the push (confirmation).

* **Current (~5 candles incl. current):** Price is testing the confluence **`1D.zones.NEUTRAL` + `4H.zones.SELL_2` + `1H.zones.SELL_1`**, with `1H.major.H_MAJOR` / `1D.session.PDH` overhead as the next inflection. `1H_RSI` > 50; price still **below** `1H_200EMA` and **well below** W/M-VWAP → the 1H bounce is **counter-trend** vs 4H/1D.
  **TTF read:** *Short-term bullish momentum into HTF supply; fade setups at the confluence are valid if structure/VPAs turn down; otherwise counter-trend longs can continue while S-VWAP/`1H_9/21EMA` hold.*
  
## MACRO CONTEXT
### LAST WEEK

* **Fed cut & guidance:** The FOMC lowered the policy rate by **25 bps to 3.75–4.00% (Oct 29)** and signaled **no pre-commitment** to a December cut given elevated inflation and limited official data during the shutdown. Minutes for the **Oct 28–29** meeting are slated for **Nov 19**.
* **Trump, tariffs & China:** The **U.S. Senate voted 51–47 to nullify the administration’s global “reciprocal” tariffs** (symbolic for now given House dynamics). Separately, at the **Trump–Xi meeting in Korea**, the U.S. **trimmed China tariffs (headline cut cited as 57% → 47%)** alongside Chinese commitments on agriculture/rare earths; the U.S. also **paused for one year the planned expansion (“50% affiliates rule”) of certain export-control restrictions**, de-escalating near-term tech/trade tension.
* **Shutdown overhang & data:** The **federal government shutdown** persisted into the 4th week, impairing some data releases and forcing reliance on private proxies; weekly claims were estimated lower by sell-side trackers.
* **Inflation print due today:** **Sep PCE/CORE PCE (Oct 31)** on deck—key for near-term rate expectations.
* **Treasury supply watch:** Treasury reaffirmed its schedule for next week’s **Quarterly Refunding Announcement (QRA)**.

### THIS WEEK

* **Clock change & hours:** **U.S. Daylight Saving Time ends Sun, Nov 2.** From **Mon, Nov 3**, U.S. cash equities reopen at **9:30 ET = 15:30 CET** (back to the normal 6-hour gap for Copenhagen).
* **Key U.S. macro (ET → CET):**

  * **Mon, Nov 3, 10:00 → 16:00** – **ISM Manufacturing (Oct)**.
  * **Tue, Nov 4, 10:00 → 16:00** – **JOLTS (Sep)**; **Election Day (state/local, off-year)** – markets open, but watch for headline risk/occasional liquidity pockets.
  * **Wed, Nov 5** – **ADP Employment (8:15 → 14:15)**; **ISM Services (10:00 → 16:00)**; **U.S. Treasury QRA** (announcement Wednesday per Treasury).
  * **Thu, Nov 6, 8:30 → 14:30** – **Initial Jobless Claims** (ongoing data quality caveats from shutdown period).
  * **Fri, Nov 7, 8:30 → 14:30** – **Nonfarm Payrolls (Oct)**.
* **Policy & tech tapes:** Watch follow-through from **Senate tariff rebuke** (House unlikely to act near-term), **Trump–Xi de-escalation** headlines, and the **one-year pause** on the export-control “50% rule.” Ongoing **TikTok U.S. ownership** negotiations also sit in the backdrop for mega-cap tech sentiment.

### MACRO ANALYSIS

#### BTC & ETH

Crypto beta typically **tracks liquidity and rates**: a **dovish-leaning Fed** + reduced trade-war stress is supportive for **risk appetite**, but **shutdown-distorted data** raises event volatility around **PCE (today) → ISM/ADP/JOLTS → NFP**. Watch **U.S. session 15:30 CET** re-sync for flow timing. Tech-policy de-escalation (chip-rule pause/TikTok progress) is a **sentiment tailwind** for AI/tech equities—historically constructive for BTC/ETH via cross-asset risk.

# TRADING PLAN FOR 1H_TTF (Trigger • Location • Context)

### **ORANGE_A — Short pullback into daily mid (1D_NEUTRAL)**

* **Context:** 1H bounce is counter-trend vs 4H/1D. Into `1D.zones.NEUTRAL` the 1H up-leg shows slowing VCs under the 20-MA cloud; look for CVD to stall/roll.
* **Location:** Confluence band **`1D.zones.NEUTRAL` + `1H.zones.SELL_1` + `4H.zones.SELL_2`**, with overhead `1D.sr.SR_1`.
* **Trigger:** **`1H_L_MSB`** (trend-death on TTF) after a wick/failed acceptance inside that band **with bearish CVD**.
* **Invalidation:** 1H acceptance **above** `1D.sr.SR_1` and hold.
* **Setup Priority:** **A**

---

### **ORANGE_B — Short reversal at prior 4H L_BOS / PDH / 1H_H_MAJOR**

* **Context:** If price extends, the next heavy cluster sits at **`4H.active.L_BOS` retest + `1D.session.PDH` + `1H.major.H_MAJOR`**. Expect a liquidity run and fade if momentum fails.
* **Location:** **`4H.active.L_BOS`** zone into **`1D.session.PDH` / `1H.major.H_MAJOR`** with nearby `4H.poc.POC_2`.
* **Trigger:** **`1H_L_MSB`** after an **H sweep**/failed breakout and **bearish HVC** or clear CVD roll.
* **Invalidation:** Strong 1H acceptance above `1H.major.H_MAJOR` that converts to support.
* **Setup Priority:** **A**

---

### **PURPLE_A — Short fade on H sweep at `1D.zones.NEUTRAL`**
* **Context:** Range-fade idea while 4H remains down; seek exhaustion into the first supply.
* **Location:** **`1D.zones.NEUTRAL` + `1H.zones.SELL_1` + `4H.zones.SELL_2`**.
* **Trigger:** **H-liquidity sweep** of the band → **15m_L_MSB** (LTF) with **bearish CVD divergence**.
* **Invalidation:** 1H close & hold **above** `1D.sr.SR_1`.
* **Setup Priority:** **A-**

---

### **PURPLE_B — Short fade on H sweep at `4H.active.L_BOS` / `1H.major.H_MAJOR`**

* **Context:** Second fade higher if ORANGE_A fails and the push tags the upper cluster.
* **Location:** **`4H.active.L_BOS` + `1D.session.PDH` + `1H.major.H_MAJOR`**.
* **Trigger:** **H sweep** of `1H.major.H_MAJOR` → **15m_L_MSB** with sell-side VC.
* **Invalidation:** Acceptance above `1H.major.H_MAJOR`.
* **Setup Priority:** **A-**

---

### **PURPLE_C — Short fade on H sweep at `4H.major.H_MAJOR` / `1D.zones.SELL_1`**

* **Context:** Stretch target if trend squeezes; bigger fade with wider stop.
* **Location:** **`4H.major.H_MAJOR`** into **`1D.zones.SELL_1`** with `4H.poc.POC_3/POC_4` overhead.
* **Trigger:** **H sweep** → **15m_L_MSB** with clear absorption (stalling VCs + CVD divergence).
* **Invalidation:** 1H acceptance above `1D.zones.SELL_1`.
* **Setup Priority:** **B-**

---

### **PINK_A — Momentum short if `1H_L_CHOCH` below `1H.local.L`**

* **Context:** If the local flag fails, expect momentum reset aligning 1H with 4H downtrend.
* **Location:** **Below `1H.local.L`** and **below S-VWAP**.
* **Trigger:** **`1H_L_CHOCH` → 15m_L_BOS** on **bearish HVC**; sell the retest from below.
* **Invalidation:** Reclaim of S-VWAP and `1H_9/21EMA` with HLs.
* **Setup Priority:** **B**

---

### **RED_A — Breakdown of `4H.major.L_MAJOR`**

* **Context:** HTF continuation if the daily demand fails.
* **Location:** Clean break **below `4H.major.L_MAJOR`** (confluence with `1D.session.PDL`).
* **Trigger:** **`1H_L_BOS`** through `4H.major.L_MAJOR` on strong sell VPA → **15m_L_MSB** entry on the first retest.
* **Invalidation:** Swift reclaim back above `4H.major.L_MAJOR`.
* **Setup Priority:** **B**

---

### **BLUE_A — Long fade on L sweep at `4H.major.L_MAJOR`**

* **Context:** Range-fade while weekly structure holds; look for exhaustion into daily demand.
* **Location:** **`4H.major.L_MAJOR`** with extension to **`1D.poc.POC_4` / `1D.zones.BUY_1`** if wicky.
* **Trigger:** **L-liquidity sweep** → **15m_H_MSB** + CVD turn; reclaim S-VWAP to confirm.
* **Invalidation:** 1H close **below** the zone on sell-side HVC.
* **Setup Priority:** **B-**

---

### **TEAL_A — (ACTIVE) Counter-trend long continuation**

* **Context:** Current 1H leg up above S-VWAP and `1H_9/21EMA` while 4H remains bearish. Treat as scalp-continuation only.
* **Location:** Pullbacks to **S-VWAP / `1H_9/21EMA`** inside **`1H.zones.BUY_1`**.
* **Trigger:** **15m_H_BOS** after a **low-volume** dip with rising CVD.
* **Invalidation:** Loss of S-VWAP **and** `1H_9/21EMA`, or **`1H_L_CHOCH`**.
* **Setup Priority:** **B**

---

### **YELLOW_A — Long reversal after sweep of `1H.local.L`**

* **Context:** Liquidity grab below the local base inside the daily demand band.
* **Location:** **Sweep of `1H.local.L`** toward **`1D.poc.POC_4` / `1D.zones.BUY_1`**.
* **Trigger:** **`1H_H_BOS` or `1H_H_MSB`** after the sweep + CVD HL; enter on low-volume pullback.
* **Invalidation:** Acceptance below `1D.zones.BUY_1`.
* **Setup Priority:** **A-**

---

### **YELLOW_B — Long at retest of `4H.major.L_MAJOR` (role-reversal)**

* **Context:** If we pull back after a higher 1H high, buy the first clean retest of the base.
* **Location:** **`4H.major.L_MAJOR`** retest, with magnets `1D.poc.POC_3` → `1D.zones.NEUTRAL`.
* **Trigger:** **15m_H_MSB** with absorption SHVC at the edge; reclaim S-VWAP.
* **Invalidation:** 1H close back below `4H.major.L_MAJOR`.
* **Setup Priority:** **A-**

---

### **GREEN_A — Long breakout & retest above `1H.major.H_MAJOR`**

* **Context:** If buy-side ignition flips 1H/4H back up, join on the retest.
* **Location:** **Break and retest of `1H.major.H_MAJOR`**, then aim toward **`1D.session.PDH` → `4H.poc.POC_2` → `1W.poc.POC_1`**.
* **Trigger:** **`1H_H_BOS` + bullish HVC**, then **15m_H_MSB** on the retest with rising CVD.
* **Invalidation:** Failed retest (acceptance back below `1H.major.H_MAJOR`).
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