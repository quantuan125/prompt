# CONTEXT: 
## TRADER CONTEXT: 
Today is Monday 6th of October 2025, we are currently in London session and 1.5 hours before US session opening. We have no major data released and news event today and for the week, only FOMC minutes on Wednesday is the significant event. 

We have officially passed September which has been notorious for a BTC and crypto pullbacks during the bull runs year and currently enter Q4 of which has been typical bullish for bitcoin bull cycle. We should favors more bullish setups while remains as cautious as possible until BTC firmly surpasses ATH. 

Last week: Market consolidated in the weekend and bounced strongly with a confirmed 1D_H_MSB and with strong bullish follow through during the entire week, leading to the ATH during the weekend.

Sentiment: Public sentiment for October remain bullish for BTC within this last year of its bullish 4 years cycle from a seasonality and historic standpoint. This is further reinforced by the recent rally on the daily. 


## TECHNICAL CONTEXT
### Key Levels 

```yaml
meta:
    pair: BTCUSDT
    units: "k"   # all numbers rounded with 'k'
    note: "Ranges use '-', e.g., 113.2-114.7k"

  ALL:
    ath: 125.7k

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
      L_MAJOR: 108.7k
    sr:
      SR_1: 117.2k
      SR_2: 119.4k
      SR_3: 108.3k
    poc:
      POC_1: 115.6k
      POC_2: 111.2k
      POC_3: 108.8k
    zones:
      SELL_1: 123.7k
      BUY_1: 106.5k
    active:
      H_CHOCH: 117.9k
    inactive:
      L_MSB: 111.9k
      H_MAJOR: 124.5k
      L_MAJOR: 107.3k
      H: 117.9k

  1D:
    major: 
      L_MAJOR: 108.6k  
    sr: 
      SR_1: 113.3k
      SR_2: 112k
      SR_3: 114.3k
      SR_4: 123.3k
    poc:
      POC_1: 113k
    zones:
      BUY_1: 114.8k
      BUY_2: 117.0k
    session:
      PDH: 125.7k
      PDL: 122.1k
    active: 
      H_MSB: 113.9k
    inactive:
      L_MSB: 114.4k
      L_BOS: 111k


  4H:
    local: {}
    major:             
      H_MAJOR: 125.7k    
      L_MAJOR: 119.3k    
    sr:
      SR_1: 124.5k
      SR_2: 121.2k
      SR_3: 120.2k
    poc: 
      POC_1: 123.9k
      POC_2: 122.5k
      POC_3: 119.6k
    zones:
      BUY_1: 121.2k
      BUY_2: 122.5k
    active:
      H_BOS: 121k
    inactive: {}

  1H:
    major:
      L_MAJOR: 124.3k
    sr: {}
    poc: {}
    zones:
      BUY_2: 124.8k
      BUY_1: 124.2k
    active:
      H_BOS: 125.3k
    inactive: {}

  15m:
    local:
    major:
      H_MAJOR: 125.3k
      L_MAJOR: 1204.4k
    sr: {}
    poc: {}
    active:
      H_BOS: 125.0k
    inactive: {}
```


### 1W — Super-HTF Structure

* **Previous (last ~30 candles):** Persistent uptrend carried price from the late-’24 base toward **`ALL.ath`**, with distribution under `1W.sr.SR_2` and a prior sweep of highs. A corrective leg confirmed **`1W.inactive.L_MSB`**, retesting `1W.zones.BUY_1` and the weekly EMA band; HL formed near `1W.major.L_MAJOR`. Subsequent recovery pushed back toward **`1W.zones.SELL_1`**.
* **Current (last ~5 candles):** Last week printed a strong bullish thrust through `1W.sr.SR_1` into **`1W.zones.SELL_1`**. Price is **above W-EMA9/21/50/200** (csv), RSI ≈ **64.8** (healthy, not OB), and above W-VWAP/M-VWAP baselines. Early-week volume is naturally light vs MA20/30 (new candle). **Bias: bullish into supply**—watch for absorption/exhaustion behaviour at `1W.zones.SELL_1`.

### 1D — HTF for intraday

* **Previous (last ~30 candles):** A high-energy liquidation month drove price down toward **`1D.major.L_MAJOR` / `1W.major.L_MAJOR`**, then weekend basing led to a decisive **`1D.active.H_MSB`**. Follow-through rallies with bullish VCs reclaimed stacked resistances (`1D.sr.SR_1 → SR_4`) and wicked above **`ALL.ath`** into `1W.zones.SELL_1`.
* **Current (last ~5 candles):** Price holds **above D-EMA9/21/50/200** with **RSI ~71.7 (overbought caution)**; `1D.session.PDH` equals **`ALL.ath`**, and `1D.poc.POC_1` sits as a magnet below. **Bias: bullish but extended** while probing `1W.zones.SELL_1`. Manage expectations for mean-reversion toward `1D.session.PDL` if momentum stalls.

### 4H — HTF for 1H

* **Previous (last ~30 candles):** Trend leg advanced persistently, respecting the **4H_9EMA** and confirming `1D.active.H_MSB`. Shallow pullbacks were bought near `4H.zones.BUY_2` and the ST EMA band; structure held above `4H.major.L_MAJOR`.
* **Current (last ~5 candles):** Price trades inside the overhead supply band (`1W.zones.SELL_1` / near `4H.major.H_MAJOR`), hovering around **`4H.sr.SR_1`** with **RSI ~70.9 (OB edge)** and no full test of **4H_21EMA** yet. With price **above 4H-EMA9/21/50/200**, momentum is strong but **extended**; monitor for **bearish divergence** development and response to **`4H.poc.POC_1 → POC_2`** on pullbacks.

### 1H — TTF

* **Previous (last ~30 candles):** Post-reclaim impulse established HH/HLs, rejected at **`ALL.ath` / `4H.major.H_MAJOR`**, then compressed into an **ascending wedge** just beneath **`1H.major.H_MAJOR`**, while defending **`1H.zones.BUY`**.
* **Current (last ~5 candles):** Price rides **1H ST-EMAs** and **S_VWAP** (csv shows price > S_VWAP), consolidating beneath **`1H.major.H_MAJOR`** with `1H.active.H_CHOCH` attempts. RSI ~59 (not OB). **Bias: constructive range-up** while above `1H.zones.BUY` / `1D.active.H_MSB`; be alert for wedge failure if `1H.major.L_MAJOR` gives way. CVD is raising and positive for the session which supports the recent bullish consolidaton move up. Volume is picking up as price trending toward the `1H.major.H_MAJOR`

## MACRO CONTEXT
### LAST WEEK

* **U.S. government shutdown (from Wed, Oct 1):** Federal data firehose went dark (BLS/BEA/Census paused), and **Friday’s NFP (Oct 3) was not released**. Markets leaned on private proxies; uncertainty around the macro path rose.
* **Risk assets resilient:** **S&P 500 finished the week near/all-time highs** as fund flows favored U.S. equities; the **10-yr UST hovered ~4.1%** while the **USD softened into week-end**, easing broad financial conditions.
* **Safe-haven bid intensified:** **Gold broke to fresh records (~>$3,900/oz)** as shutdown/fed-cut bets met FX tailwinds (yen slide). **Oil fell ~7–8% on supply headlines**, easing inflation worries at the margin.
* **Crypto impulse:** **U.S. spot BTC ETFs drew ~**$**3.2B net inflows on the week**, and **BTC printed a new ATH (~$125k) into the weekend**, adding a high-beta “liquidity” tailwind to risk.
* **Liquidity/holidays:** **China “Golden Week” (Oct 1–8)** kept mainland markets shut most of the week; **Germany Unity Day (Fri, Oct 3)** further thinned early-Friday European liquidity.

### THIS WEEK

* **Policy & data calendar (ET):**

  * **Wed, Oct 8 (15:00)** — **FOMC minutes (Sep 16–17 meeting)**; markets will parse easing bias and balance-sheet nuance while official data remain curtailed by the shutdown.
  * **Weekly jobless claims (Thu)** may print (depends on shutdown logistics); otherwise, **official macro releases broadly at risk of continued delay**.
* **Earnings pulse (Q3 kick-off, U.S.):** **Constellation Brands (Mon PM), McCormick (Tue AM), Delta Air Lines (Thu AM), PepsiCo (Thu AM), Levi Strauss (Thu PM)** — first read-throughs on consumer demand, travel, and cost pressures.
* **Crypto micro-flow:** After last week’s large **spot BTC ETF inflows**, desks will monitor whether **net creations persist** (key for sustaining ATHs) amid the shutdown narrative.
* **Commodities & FX context:** **Oil attempting a rebound** after last week’s drop (OPEC+ headlines in focus). **JPY volatility** elevated post-LDP leadership outcome; **broad USD tone** still sensitive to shutdown duration and Fed path.
* **Holidays / liquidity watch:**

  * **China Golden Week continues through Wed, Oct 8** (mainland reopens Thu) → **lighter Asia hours**.
  * **U.S. Columbus Day/Indigenous Peoples’ Day (Mon, Oct 13)** next week — **U.S. bond market closed** (equities open); positioning could start Friday.

### MACRO ANALYSIS

A **data-starved U.S. tape** (shutdown) puts **positioning and flows** in the driver’s seat: **equities (SP500)** hold momentum near highs as oil’s slide eases inflation angst; **rates drift** and a **softer USD** underpin **gold’s breakout**. **BTC** benefits from the same “liquidity/debasement” bid plus **ETF inflows**, tightening its **short-term positive correlation with SPX** while **gold moves inversely to real yields**. With **FOMC minutes (Wed)** as the only definitive macro waypoint and **Asia liquidity thin (China holiday)**, today’s U.S. session likely trades **headline- and flow-driven**: watch for **equity strength → risk-on beta in BTC**, and **any USD/rates pops → tests on gold’s new highs**. Manage risk around **minutes-time swings** and **closing flows** into the holiday-affected next week.

#### GOLD

Record-high backdrop (~>$3,900/oz) supported by **shutdown uncertainty, softer USD, and rate-cut expectations**. **Pullbacks** likely eyed by dip-buyers while **UST yield pops** or a **USD bounce** are near-term risks.

#### BTC

**ATHs fueled by ~$3.2B weekly ETF inflows** and the same macro liquidity bid driving equities. Expect **beta to SPX** intraday; watch **ETF flow prints** and **minutes-time volatility**. Structural demand remains the tailwind; beware **mean-reversion** after parabolic extensions.

#### SP500

Near highs with **early-earnings reads (staples/airlines/apparel)** and **minutes** as catalysts. **Lower oil** is supportive; **data blackout** clouds macro visibility — **headline risk** (shutdown duration) can swing **rates/FX**, spilling into index levels.


# TRADING PLAN FOR 1H_TTF (Trigger • Location • Context)

### ORANGE_A — **Short reversal above tops (ATH/PDH/4H_H_MAJOR)**

* **Context:** HTF trend is strong but extended into `1W.zones.SELL_1`; 1D/4H are near/at OB RSI. We require **clear topping** and **exhaustion**.
* **Location:** Liquidity sweep above **`ALL.ath` / `1D.session.PDH` / `4H.major.H_MAJOR`**.
* **Trigger:** Sweep/fake break then **ideally 1H_L_MSB** with **bearish HVC** and **CVD rollover**.
* **Invalidation:** 1H acceptance **above** `4H.major.H_MAJOR` that holds (buy-side ignition); stand down.

---

### PURPLE_A — **Short fade at 1H_H_MAJOR (range scalp)**

* **Context:** Ascending wedge under resistance; looking to fade if momentum stalls and **RSI/CVD show LTF regular bearish divergence**.
* **Location:** **`1H.major.H_MAJOR`** with `1W.zones.SELL_1` overhead.
* **Trigger:** Rejection or wick-through and close back **below** `1H.major.H_MAJOR` + **LTF_L_MSB** on weakening VPA.
* **Invalidation:** 1H close and continuation **above** `1H.major.H_MAJOR` (convert to support).

---

### RED_A — **Short breakdown of 1H major range low (wedge failure)**

* **Context:** Bearish regime flip on TTF if major structure breaks. Strong VPA signal supported bearish breakdown.
* **Location:** Clean loss of **`1H.major.L_MAJOR`** with 1H_50EMA rolling over.
* **Trigger:** **1H_L_BOS** through `1H.major.L_MAJOR` on strong sell HVC and negative CVD; sell the **low-volume retest** from below.
* **Invalidation:** Swift reclaim of `1H.major.L_MAJOR` and S_VWAP with HLs restored.

---

### BLUE_A — **Long fade at 1H range low**

* **Context:** Buy the range until it breaks; trend support from ST-EMAs and S_VWAP below price.
* **Location:** **`1H.major.L_MAJOR`** (check note vs `1D.sr.SR_4`) with `1H.zones.BUY` just beneath.
* **Trigger:** Liquidity sweep + **15m_H_MSB** and **bullish divergence (RSI/CVD)**; reclaim S_VWAP to confirm.
* **Invalidation:** Acceptance below `1H.major.L_MAJOR` (defer to **RED_A** path).

---

### TEAL_A — **Long momentum reclaim (ACTIVE)**

* **Context:** Price is **above S_VWAP** and ST-EMAs (csv); trend intact.
* **Location:** At 4H_POC_1 where the mid range level of the 1H lies with reclaim/hold of **S_VWAP** after shallow dip.
* **Trigger:** **15m/1H continuation BOS** with buy-side HVC and rising CVD; enter on pullback to S_VWAP/EMA9.
* **Invalidation:** Lose S_VWAP and fail retest while CVD turns down.

---

### YELLOW_A — **Long reversal at 4H demand + PDL**

* **Context:** Deeper dip buy if range fails; look for **oversold + bullish divergence** on TTF.
* **Location:** **`4H.zones.BUY_1`** confluence with **`1D.session.PDL`** and rising **4H_21EMA**.
* **Trigger:** Stop-run into the zone → **15m_H_MSB / 1H_H_CHOCH** with absorption SHVC and CVD uptick.
* **Invalidation:** 1H close **below** `4H.zones.BUY_1` with persistent sell HVC.


### YELLOW_B — **Long reversal at 1H demand**

* **Context:** Deeper dip buy if range fails; look for **oversold + bullish divergence** on LTF.
* **Location:** **`1H.zones.BUY_1`** confluence with S_VWAP and raising 1H_50EMA 
* **Trigger:** Stop-run into the zone → **LTF_H_MSB** with absorption SHVC and CVD uptick.
* **Invalidation:** 1H close **below** `1H.major.L_MAJOR` with persistent sell HVC.

---

### GREEN_A — **Long breakout & retest of 1H_H_MAJOR**

* **Context:** Continuation if the wedge resolves up.
* **Location:** First clean retest of **`1H.major.H_MAJOR`** after **1H_H_BOS**.
* **Trigger:** Breakout HVC + rising CVD → buy the **low-volume retest**; maintain HH/HL.
* **Invalidation:** Failure retest (acceptance back below `1H.major.H_MAJOR`) or immediate **1H_L_CHOCH**.

---

### GREEN_B — **Long breakout & retest of 4H_H_MAJOR/ATH cluster**

* **Context:** True HTF ignition beyond supply.
* **Location:** Retest of **`4H.major.H_MAJOR` / `ALL.ath` / `1D.session.PDH`** after a decisive break.
* **Trigger:** **1H_H_BOS** with buy-side SHVC + CVD expansion; enter on controlled pullback.
* **Invalidation:** Rejection back inside `1W.zones.SELL_1` and **1H_L_CHOCH** post-entry.

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
- OVERALL-ASSESSMENT for the 1W is BULLISH. DO NOT PERFORM TTI on the 1W_TF.
- `PG` grades are assessed based on the plan full viability. DO NOT DEGRADE the plan based on probability/possibility.  