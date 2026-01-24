# CONTEXT: 
## TRADER CONTEXT: 
This week: Today is Monday 24th of November 2025, we are 30 minutes into US session. We have no major macro events or data released today. Refers to `MACRO CONTEXT` for the rest of the macro events this week.  

Last month: We have officially passed October which was supposed to be bullish month for BTC and crypto in terms of seasonality during a bull cycle year, however we got the opposite of that: largest crypto liquidation sell off after sweeping the ATH followed by choppy bearish price actions despite soft CPI + Inflation data print + resolution on China-US tariffs.

Last week: Government shutdown resolved and we got the mixed NFP + Unemployment September data released and market seems to be pricing in hawkish FED into December FOMC. 

Directive: Price is bearish across daily and weekly timeframe, short are prioritize however caution due to bearish extension into monthly demand zone. 

Sentiment: With price action last month that have liquidated millions of leveraged crypto traders and enact fears, the general consensus is bearish with hypothesis of the top for the cycle is already set for BTC, and the start of an extended bear market into 2026. `Fear & Greed Index` worsen from 30-40 (NEUTRAL) since last month to 25 (FEAR) last week now to 11-14 (EXTREME FEAR) this week.    

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
      BUY_1: 90.0
      BUY_2: 100.3
      BUY_3: 73.7
    inactive:
      H_BOS: 109.6

  1W:
    major:
      H_MAJOR: 116.4
      L_MAJOR: 102.0
    sr:
      SR_1: 108.3
      SR_2: 100.9
      SR_3: 86.1
      SR_4: 80.7
      SR_5: 78.4
    poc:
      POC_1: 108.2
      POC_2: 106.8
      POC_3: 103.4
      POC_4: 101.8
      POC_5: 94.6
      POC_6: 87.3
      POC_7: 67.4
    zones:
      SELL_1: 120.5
      SELL_2: 106.1
      SELL_3: 98.4
    active:
      L_BOS: 102.0
    inactive:
      L_MSB: 111.9
      H_FSB: 124.5
      L_FSB: 108.6

  1D:
    major:
      H_MAJOR: 93.2
      L_MAJOR: 80.6
    sr:
      SR_1: 114.3
      SR_2: 110.5
      SR_3: 106.4
    poc:
      POC_1: 103.4
      POC_2: 95.7
      POC_3: 91.5
      POC_4: 86.9
      POC_5: 84.6
      POC_6: 79.7
    zones:
      SELL_1: 94.0
    session:
      PDH: 88.1
      PDL: 84.7
    active:
      L_BOS: 88.6
    inactive:
      L_BOS: 98.9

  4H:
    local:
      L: 85.3
    major:
      H_MAJOR: 88.1
      L_MAJOR: 80.6
    sr:
      {}
    poc:
      POC_1: 91.9
      POC_2: 90.0
      POC_3: 86.0
      POC_4: 82.2
    zones:
      SELL_1: 88.4
      BUY_1: 83.5
      BUY_2: 85.3
    active:
      H_CHOCH: 85.6
    inactive:
      L_BOS: 88.6

  1H:
    major:
      H_MAJOR: 86.7
      L_MAJOR: 85.3
    sr: {}
    poc: {}
    zones:
      BUY_1: 86.3
      SELL_1: 87.2
      NEUTRAL: 86.9
    active:
      H_MSB: 86.6
    inactive:
      L_FSB: 85.7

  15m:
    major:
      H_MAJOR: 87.7
      L_MAJOR: 85.9
    sr: {}
    poc: {}
    zones:
      {}
    active:
      H_BOS: 86.7
    inactive: 
      L_FSB: 85.9
```

### **1W – Super-HTF Structure**

**Previous (~30 candles):**
After a strong `1M_bullish_channel` since late ’24, price distributed for ~3 months under `ALL.ath` **126.2k** / `1M.major.H_MAJOR` **126.2k**. We printed an ATH sweep at `1W.inactive.H_FSB` (under `1W.zones.SELL_1` **120.5k**) and then a historic liquidation leg through `1M.active.H_BOS` **109.6k**, tagging `1W.inactive.L_FSB` last month via a `1W_bearish_hammer_HVC`. That established the lower bound at `1W.major.L_MAJOR` **102.0k**. The rebound into the midrange failed at a LH near `1W.major.H_MAJOR` **116.4k** (confluence with the bearish cross of `1W_9/21EMA`) and we confirmed `1W.active.L_BOS` **102.0k** below the former weekly range low + the ascending `1W_50EMA/MA`. Follow-through sold down into the monthly supports `1M.poc.POC_4` **84.2k** + `1M.sr.SR_4` **82.5k**, with risk of extension toward `1M.major.L_MAJOR` **74.5k**.

**Current (~5 candles):**

* Last two weeks: `1W_bearish_engulfing_VC` → `1W_bearish_hammer_HVC` into `1M.sr.SR_4`. This week is an inside, small-body drift (so far) below `1W.active.L_BOS` **102.0k**.
* **Indicators (current candle from csv):** Price **86.5k** sits **below** `1W_9EMA` **100.4k**, `1W_21EMA` **105.2k**, `1W_50EMA` **99.7k`; RSI 35.6 < `1W_RSI-MA`51.2;`M_VWAP` **95.9k** above price ⇒ **bearish** posture.
* **Nearby refs:** `1W.sr.SR_3` **86.1k** / `1W.poc.POC_6` **87.3k** act as local magnet/resistance; downside air until `1W.sr.SR_4` **80.7k** / `1W.sr.SR_5` **78.4k**.
  **Bias:** HTF **bearish** while below `1W.active.L_BOS` **102.0k**; sellers control unless we reclaim weekly supply `1W.zones.SELL_3` **98.4k** → `1W.zones.SELL_2` **106.1k**.

---

### **1D – HTF for intraday**

**Previous (~30 candles):**
Post-rejection at `1W.major.H_MAJOR` **116.4k**, a daily down-trend formed under descending `1D_9/21EMA`. Last week accelerated with `1D.active.L_BOS` **88.6k**, multiple `1D_bearish_engulfing_VCs` (with OBV/CVD confirming on-chart), pushing below `1M.zones.BUY_1` **90.0k** into monthly support blocks. A capitulative tag at `1D.major.L_MAJOR` **80.6k** printed a `1D_bearish_hammer_HVC` (largest vol of the sell-off) with RSI sub-25, then a weekend rebound toward the broken `1D.active.L_BOS` **88.6k** / `1M.zones.BUY_1` **90.0k** pivot.

**Current (~5 candles):**

* Two-day bounce stalled beneath `1D.poc.POC_4` **86.9k** and `1D.poc.POC_1` **103.4k** remains far overhead.
* **Session refs:** `1D.session.PDH` **88.1k**, `1D.session.PDL` **84.7k**.
* **Indicators (current candle from csv):** Price **86.5k** < `1D_9EMA` **89.2k** < `1D_21EMA` **94.9k** < `1D_50EMA` **102.3k; `1D_200EMA/SMA` **106.0/110.1k** well above; RSI 28.3 with`RSI-MA`30.4 (still **oversold** but curling).`W_VWAP`**86.8k** ≈ overhead.   
  **Bias:** **Bearish*** (oversold rebound potential) below`1D.active.L_BOS`**88.6k** /`1M.zones.BUY_1`**90.0k**. Failure to reclaim`1D.session.PDH`**88.1k** favors rotation back to`1D.poc.POC_5`**84.6k** →`1D.poc.POC_6` **79.7k**.

---

### **4H – HTF for 1H**

**Previous (~30 candles):**
Downtrend all last week under `W_VWAP` with `4H.inactive.L_BOS` prints. A capitulation into `1D.major.L_MAJOR` **80.6k** formed a `4H_bullish_spinning-bar_SHVC` (largest in the leg), initiating recovery. Structure confirmed `4H.active.H_CHOCH` **85.6k** up to `4H.zones.SELL_1` **88.4k** / `1D.active.L_BOS` **88.6k**, topping at `4H.major.H_MAJOR` **88.1k** (confluent with descending weekly VWAP), then a low-volume roll-down to retest `4H.zones.BUY_2` **85.3–85.8k**.

**Current (~5 candles):**

* Pauses below `4H.major.H_MAJOR` **88.1k** and above `4H.local.L` **83.5k**.
* **Indicators (current candle from csv):** Price **86.5k** ~ `4H_9EMA` **86.5k**, < `4H_21EMA` **86.7k`; `4H_50EMA` **89.3k` and `4H_200EMA` **99.5k`overhead; RSI 46.8;`W_VWAP`**86.8k** slightly above;`M_VWAP` **96.6k** far above.
* **Profile magnets:** `4H.poc.POC_3` **86.9k** and `4H.poc.POC_4` **85.7k**; deeper → `4H.poc.POC_5` **82.2k**.
  **Bias:** **Bearish** while below `4H.zones.SELL_1` **88.4k** / `1D.active.L_BOS` **88.6k**; rallies are for fading unless we break and hold above that supply.

---

### **1H – TTF**

**Previous (~30 candles):**
Weekend recovery delivered `1H.inactive.H_BOS`, but rejection at `4H.major.H_MAJOR` **88.1k** just below `4H.zones.SELL_1` **88.4k** + `1D.active.L_BOS` **88.6k** flipped the tape. A `1H.inactive.L_MSB` loss of S_VWAP and the 9/21/50 EMAs followed, breaking through `1H.zones.BUY_1` **86.5k** with CVD rolling over (OBV not yet full confirmation on-chart). Another push down failed to expand, printing a `1H.active.L_FSB` near `4H.zones.BUY_2` **85.3–85.8k**. A `1H_descending_channel` is now in play with LHs/LLs; midline is `1H.zones.NEUTRAL` **86.9k**.

**Current (~5 candles):**

* Price retests the underside of `1H_9/21EMA` with a bearish crossover, below S_VWAP/W_VWAP **~86.8k**, hovering between `1H.zones.BUY_1` **86.5k** and `1H.major.L_MAJOR` **85.7k**.
* **Indicators (current candle from csv):** Price **86.5k** ≈ `1H_9EMA` **86.5k** < `1H_21EMA` **86.6k**; `1H_50EMA` **86.4k; `1H_200EMA/SMA`**89.5/89.4k** above; RSI 49.2 <`RSI-MA`51.3; S_VWAP/W_VWAP **86.8k** above.   
  **Bias:** **TTF bearish** inside a descending channel while below`1H.zones.NEUTRAL` **86.9k** and S_VWAP.

## MACRO CONTEXT
### LAST WEEK

* **Fed: minutes, data and a split committee (policy uncertainty high):**

  * The **October 28–29 FOMC minutes** (released Wed 19 Nov) showed broad support for **ending quantitative tightening on Dec 1** but a *fractured* debate on further rate cuts, with many policymakers pushing back against another cut in December and stressing tariff-related upside risks to inflation.
  * A shutdown-delayed **September jobs report** landed Thu 20 Nov: **+119k jobs, unemployment up to 4.4%**, with sizeable downward revisions to prior months – a cooling but not collapsing labour market that doesn’t scream “urgent cuts.” 
  * Fed **Governor Waller** doubled down in a London speech on calling for **another 25 bps cut in December** to insure against labour weakness, while **Vice Chair Jefferson** and Cleveland Fed President **Hammack** cautioned against moving too fast, warning about inflation and financial-stability risks from easier policy and frothy markets.
  * Vice Chair Jefferson separately gave a high-profile speech on **AI, the economy and financial stability**, underscoring that AI is a structural force but that the Fed must still prioritise its dual mandate and guard against new systemic risks – reinforcing the sense that the Fed is **data-dependent but nervous**. 

* **Government shutdown aftershocks:**

  * The **43-day federal shutdown ending 12 Nov** has left big gaps and distortions in official data, making it harder for the Fed and markets to read the economy; CBO and private research note a temporary hit to **Q4 growth (-1–2 ppts annualised)** with some rebound expected in early 2026.

* **Trump, tariffs and trade (China, chips and Europe):**

  * Earlier in November, a **Trump–Xi deal** saw the U.S. roll back its specialised **“fentanyl” tariff on Chinese goods from 20% to 10% and extend a 10% reciprocal tariff for another year**, while China agreed to suspend a wide swath of retaliatory tariffs on U.S. farm goods – easing but not ending trade tensions. 
  * At the same time, the administration’s threat of a **~100% tariff on imported semiconductors** has been **pushed back**, with officials debating timing and design; policy analysis highlights Trump’s parallel move to allow Nvidia/AMD to sell *tuned-down* AI chips to China if they pay a **15% levy to the U.S. Treasury** – effectively a new tariff-tax on AI hardware. 
  * China retaliated on the tech front by ordering **state-funded data centres to use only domestic AI chips**, banning foreign chips such as Nvidia’s from new projects; U.S. senators simultaneously urged Trump to **keep strict export controls on advanced AI chips**, keeping the U.S.–China tech war firmly in play. 
  * In the **EU–US relationship**, the EU spent the week preparing to demand that Washington **honour the August/July EU–US trade deal** which had set a 15% baseline on most EU imports but left a **50% U.S. tariff on steel and aluminium** in place; officials warned that delays and threats of additional Trump tariffs undermine the deal and create fresh uncertainty for industrials and autos.

* **Gold: pullback but still elevated, central banks buying:**

  * After spiking to an October record near **$4,381/oz**, gold spent last week in a **4-day losing streak**, briefly dipping toward **$4,000** as a stronger dollar, fading odds of a December Fed cut and unwinds of speculative positioning hit the metal; weekly losses were roughly **2½–3%**, with spot closing near **$4,050–4,080** on Friday. 
  * At the same time, **central banks have been heavy buyers**, with estimates of about **64 tonnes purchased in September versus 21 tonnes in August**, and some banks (including Goldman Sachs and Deutsche Bank research) projecting **gold above $4,000 on average and potentially near $4,900 by end-2026**, reinforcing a structural bullish backdrop despite the short-term shake-out. 

* **Equities, AI and the “everything sell-off”:**

  * Early in the week, markets saw a **broad risk-off move** where tech, crypto and gold sold off together; a widely cited piece described a **“market rout intensifying, sweeping up everything from tech to crypto to gold”**, with the S&P 500 and Nasdaq breaking below their 50-day moving averages and the VIX jumping to its highest level since April tariff headlines. 
  * **Nvidia’s blockbuster earnings** (revenue ~$57B, huge data-centre beat) briefly steadied sentiment mid-week, but the stock still sold off on **AI-bubble fears**, and major indices ended the week lower even after a strong Friday rebound driven by renewed December cut hopes. 
  * Bank of America flow data showed tech funds still on track for a **record $75B in 2025 inflows**, even as the week saw a sizeable tech drawdown – highlighting crowded positioning and the risk that any further Fed-hawkish or tariff headlines can spark outsized de-risking in high-beta names. 

* **Crypto: deleveraging, ETF outflows, macro-driven:**

  * **Bitcoin dropped to the low $80Ks–90Ks region**, its **lowest level in ~7 months** and roughly **30% below its early-October record above $120K**, with November alone seeing a >20% slide and over **$1T in crypto market value wiped out**, including one day in October with **$19B of leveraged positions liquidated**. 

  * Spot **Bitcoin ETFs have bled a record ~$3.8B in November**, with more than **$900M in outflows on one day** and **BlackRock’s IBIT losing a record $523M in a single session** last week; Ether ETFs have also seen record outflows around **$1.8B**, underlining an institutional **risk-off rotation out of BTC/ETH** even as some alt-coin ETFs (e.g. Solana, XRP) still attract niche inflows.

---

### THIS WEEK

* **Fed & policy backdrop into the December meeting:**

  * Markets start the week **debating the odds of a 10 Dec cut**: Waller’s call for another 25 bps easing and Williams’ suggestion there is “room for further adjustment” are being weighed against Hammack’s warning that further cuts could extend above-target inflation and encourage risk-taking.
  * The October minutes’ emphasis on **tariff-driven inflation risks** and the mixed September jobs report mean **PPI, Retail Sales and claims this week are pivotal**: strong prints would validate the more hawkish voices and pressure risk assets; soft prints would support Waller’s camp and re-energise “cut in December or early 2026” hopes.
  * Note that the **FOMC blackout period** starts on **Sat 29 Nov**, so this is effectively the last full week for data-driven repricing before communications go quiet.

* **Trump, tariffs & geopolitical/tech risk this week:**

  * **Mon 24 Nov (today):** Senior U.S. trade officials meet EU ministers in Brussels for the first time since taking office. The **EU has already said it does not expect a deal today** to lower U.S. steel and aluminium tariffs and will push Washington to fully implement the July/August trade accord (including cutting the 50% steel tariff and removing some duties on wine and spirits). The White House is simultaneously reported to be **preparing backup tariff plans** in case its emergency-powers authority is constrained by the courts.
  * On **China and chips**, Trump’s threatened **100% semiconductor tariff** remains on ice while details are hammered out, but the **15% levy on tuned-down AI chips exported to China** and Beijing’s ban on foreign AI chips in state-funded data centres are already in play. That keeps **AI supply chains and mega-cap tech valuations tightly linked to policy risk**, a key driver for both the S&P and crypto beta. 

* **Crypto policy & flows:**

  * There are **no major scheduled U.S. crypto legislative events** this week, but markets remain focused on **ETF flows and the implementation of the GENIUS stablecoin Act**, which continues to shape how large institutions use stablecoins in trading and settlement. The ongoing **record outflows from BTC and ETH spot ETFs in November** keep the risk that any further macro shock or tariff headline triggers *additional* forced selling.
  
* **Cross-asset tone and seasonality:**

  * Last week ended with **indexes jumping on revived rate-cut bets**, but still logging **their worst week since April** as AI-bubble concerns persisted; analysts highlight that **Bitcoin, AI tech and even gold** were at the centre of the de-risking.
  * Thanksgiving week usually brings **lower volumes and a slight bullish seasonal bias**, but with **tariff headlines, noisy post-shutdown data and a split Fed**, any pre-holiday “drift higher” in the S&P could coexist with sharp intraday spikes in volatility – especially in thinly traded names and leveraged products (including some crypto and gold derivatives).
  
### MACRO ANALYSIS

#### BTC & ETH

BTC and ETH are trading in a **macro-driven deleveraging environment** where they behave less like “digital gold” and more like **high-beta proxies for AI/tech risk and dollar liquidity**. Last week’s sell-off – **BTC down into the low $80Ks–90Ks with record ETF outflows and seven-month lows** – occurred alongside broad risk pressure on AI names and rising doubts about further Fed cuts, all while Trump’s tariff and chip policies raised uncertainty around global growth and technology capex. For this week, the key cross-asset drivers are **U.S. data and equity sentiment**: soft PPI/Retail Sales/claims and a calm equity tape could allow a **short-covering bounce** in BTC/ETH, especially in thin pre-holiday books, whereas any upside inflation surprise or renewed AI/tech rout can easily trigger **another wave of ETF- and derivatives-driven selling**. From a trading-discipline standpoint, treat BTC/ETH as **leveraged expressions of S&P/tech and Fed expectations** rather than as independent macro hedges: watch U.S. yields, the dollar and intraday S&P/NDX tone first, and avoid chasing extremes in low-liquidity conditions where wicks and stop-hunts will be common.
  
# TRADING PLAN FOR 1H_TTF (Trigger • Location • Context)
## SHORT
### **WHITE_A — Short continuation from mid-band**

* **Context:** TTF down-trend within 4H bearish structure. Price below S_VWAP/W_VWAP (**~86.8k**) with `1H_9<21` crossover and RSI<MA. Expect LHs to form in the `1H_descending_channel`.
* **Location:** Confluence at `1H.zones.NEUTRAL` **86.9k** + `1H.zones.SELL_1` **87.2–87.5k** (under `1H.major.H_MAJOR` **88.1k**).
* **Trigger:** **15m_L_MSB → 1H_L_MSB** at the band with **bearish CVD** and a bearish VC/HVC rejection of S_VWAP.
* **Invalidation:** 1H acceptance **above** `1H.zones.SELL_1` **87.2–87.5k** and S_VWAP with rising CVD (defer to **GREEN_A**).
* **Setup Priority:** **A+**

---

### **ORANGE_A — Short reversal at 1D/4H cap**

* **Context:** Any squeeze into HTF supply should fade: overhead stack = `1D.active.L_BOS` **88.6k** + `4H.zones.SELL_1` **88.4k** + `4H.major.H_MAJOR` **88.1k** + `1H_200EMA` **~89.5k**. Look for weakening buying (lighter VCs) and **bearish RSI/CVD divergence** on the push.
* **Location:** The 88–89k shelf: `1D.active.L_BOS` **88.6k** / `4H.zones.SELL_1` **88.4k** / `4H.major.H_MAJOR` **88.1k**.
* **Trigger:** Liquidity sweep of the zone → **15m/5m_L_MSB** confirmation; failing retest under S_VWAP.
* **Invalidation:** Strong acceptance back above `1D.active.L_BOS` **88.6k** with bullish HVC and CVD (trend realignment risk).
* **Setup Priority:** **A-**

---

### **PURPLE_A — Short fade on failed breakout**

* **Context:** Range-fade with bearish bias at local tops of the channel. Expect a wick through `1H/4H` highs that **fails**.
* **Location:** `1H.major.H_MAJOR` **88.1k** / (overlap with) `4H.major.H_MAJOR` **88.1k**.
* **Trigger:** **H_FSB** at the level then **15m_L_CHOCH → L_MSB** with CVD rolling over.
* **Invalidation:** 1H close above `1H.major.H_MAJOR` **88.1k** that holds as support.
* **Setup Priority:** **B+**

---

### **PINK_A — Short momentum scalp under VWAP**

* **Context:** When price stays **below** S_VWAP + `1H_9EMA` + `1H.zones.NEUTRAL` **86.9k**, momentum favors breakdowns.
* **Location:** Sub-`1H.zones.NEUTRAL` **86.9k**, ideally a failed retest of S_VWAP.
* **Trigger:** **5m/3m_L_BOS or L_MSB** + bearish crossover of `LTF_9/21EMA` with sell-side VC/HVC.
* **Invalidation:** Reclaim of S_VWAP and `1H_21EMA` **~86.6k** with rising CVD.
* **Setup Priority:** **B**

---

### **RED_A — Short breakdown of major low**

* **Context:** Bears in full control if we lose the base.
* **Location:** Clean break of `1H.major.L_MAJOR` **85.7k** (overlap `4H.zones.BUY_2` **85.3–85.8k**).
* **Trigger:** **1H_L_BOS** with strong sell VPA/CVD → **sell the low-volume retest** back into 85.7–85.8k (`LTF_L_MSB/BOS`).
* **Invalidation:** Swift reclaim above `1H.major.L_MAJOR` **85.7k** and S_VWAP.
* **Setup Priority:** **B+**

---

## LONG

### **BLUE_A — Long fade at 1H range low + demand**

* **Context:** Counter-trend fade leaning on prior `1H.active.L_FSB` at the bottom of 1H descending channel. Seek **bullish divergences** + sellers’ exhaustion.
* **Location:** `1H.major.L_MAJOR` **85.7k** + `4H.zones.BUY_2` **85.3–85.8k**.
* **Trigger:** Stop-run into the band → **15m_H_CHOCH / H_MSB** + absorption VC and CVD turn; reclaim of S_VWAP to confirm.
* **Invalidation:** Acceptance below `4H.zones.BUY_2` **85.3–85.8k** (hand off to **RED_A**).
* **Setup Priority:** **B-**

---

### **TEAL_A — Long counter-trend if VWAP is reclaimed**

* **Context:** Only if price **reclaims and holds** S_VWAP + `1H_9EMA`, turning `1H.zones.NEUTRAL/BUY_1` **86.9k** into support.
* **Location:** Above `1H.zones.NEUTRAL/BUY_1` **86.9k** after reclaim.
* **Trigger:** Pullback to the flip → **LTF_H_MSB** with rising CVD and a series of bullish VCs.
* **Invalidation:** Lose S_VWAP again or print a fresh **1H_L_CHOCH**.
* **Setup Priority:** **B**

---

### **YELLOW_A — Long major reversal at deeper 4H demand**

* **Context:** If liquidation extends into deeper demand, look for a structural regime change.
* **Location:** `4H.zones.BUY_2` **85.3–85.8k** stretching to `4H.zones.BUY_1` **83.5k** near `1M.poc.POC_4` **84.2k** / `1M.sr.SR_4` **82.5k** and above `1D.major.L_MAJOR` **80.6k**.
* **Trigger:** **1H_H_MSB (TTF)** after a stopping/absorption SHVC; then buy the first low-volume pullback.
* **Invalidation:** Failure of the MSB base or acceptance below `1D.major.L_MAJOR` **80.6k**.
* **Setup Priority:** **A-**

---

### **GREEN_A — Long breakout + retest**

* **Context:** Bear trend fails if we clear the supply stack.
* **Location:** Break and hold **above** `ORANGE_A/PURPLE_A` PEZ — i.e., `4H.zones.SELL_1` **88.4k** / `1D.active.L_BOS` **88.6k** / `1H.major.H_MAJOR` **88.1k**.
* **Trigger:** **1H_H_BOS + bullish HVC** with positive CVD → buy the **low-volume retest** (**LTF_H_MSB/BOS**).
* **Invalidation:** Acceptance back **below** `1H.major.H_MAJOR` **88.1k** or immediate **1H_L_CHOCH** after entry.
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
- 1W: `OVERALL-ASSESSMENT = BEARISH*`. DO NOT PERFORM TTI on the 1W_TF. 
- `PG` grades are assessed based on the plan full viability. DO NOT DEGRADE the plan based on probability/possibility.  