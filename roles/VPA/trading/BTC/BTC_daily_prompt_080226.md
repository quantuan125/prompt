# TRADER
Today is **Sunday the 8th of February 2026**. We are currently in the orange A position, and we are trying to manage within the low volume and liquidity environment. Refer to the macro context below for any additional news.

# MACRO
Yes — since **Sat Feb 7, 2026**, the main *additional* macro-relevant headlines that could matter for **BTC/ETH, S&P 500, and Gold** are:

* **Japan “Super Poll Sunday” election (today):** markets are watching for spillover into **JPY volatility / rates expectations** going into the new week (Asia open risk).
* **Ukraine sanctions escalation (today):** Zelenskiy announced new sanctions targeting foreign suppliers of components for Russian missiles/drones; he also referenced sanctions hitting entities supporting **Russia’s crypto market & mining** (potential incremental friction for crypto rails / mining-related flows).
* **Energy/inflation channel (today):** Indian refiners are reportedly **avoiding Russian oil purchases for April delivery** as part of a push toward a U.S. trade pact — potentially relevant for **oil pricing**, and therefore **inflation expectations → yields → Gold / risk assets**.
* **Risk appetite tone (today):** Reuters notes investors are rotating toward **cheaper/smaller equities** while reassessing exposure to **volatile assets** after recent whipsaws — a setup that can keep **BTC/ETH and tech-heavy indices** sensitive to sentiment shifts.
* **Fed/White House narrative (fresh weekend context):** A new economist poll pushed back on the idea that an **AI productivity boom** would quickly justify easier policy under Fed-chair nominee **Kevin Warsh** — relevant insofar as it influences **rate-path / balance-sheet** expectations and therefore **USD/yields** (key for SPX, Gold, BTC).

# TECHNICAL
**1D**: Price closes as a `1D_bearish_spinning-bar_HVC` (more than average volume), as it is trying to recover from oversold extension from last week's sell-off and trying to reclaim the descending `W_VWAP` + `M_VWAP` with the gap closing significant to the descending `1D_9EMA`.

**4H**: Price bottomed at `4H.local.L` from yesterday's sell-off, but then managed to quickly reclaim `4H_9EMA` and currently trying to recover back inside `4H.zones.SELL_1` and trying to reclaim `4H_21EMA` + `W_VWAP`. However this recovery is on low volume as expected with flattening **OBV**.

**1H**: Price actually, after bottoming at `4H.local.L`, recovered and reclaimed `S_VWAP` + `1H_9/21EMA` with bullish crossover with a confirmed `1H.active.H_CHOCH` and setting a higher low at `1H.major.L_MAJOR`. Price is now trying to break above `1H.zones.SELL_1`, which is where our entry of the **ORANGE_A** position is. And this move occurred with volume spike with **CVD** + **OBV** raising confirmation and price had a successful LTF retest at the broken `1H.active.H_CHOCH` level and currently trying to push higher.

# TASK
## 1
Please run the **TEA protocol** to create our execution of the **ORANGE_A** position with the following setup. Our stop loss is at `4H.local.H`. Our thesis is the continuation of the bearish trend on the **1D** and **4H**, and our soft invalidation is a `1H.active.H_CHOCH` confirmed. Our entry is on a low-volume pullback to the broken level, `1H.inactive.L_MSB` prior, confluence with `1H.zones.SELL_1`. And our FTA is at `1H.major.L_MAJOR`, with targets as set from the prior TMI.

## 2
Please update the **TMI** to reflect our strategy and management for this **ORANGE_A** position, and determine whether if we should cut the loss or initiate another position or add more position to this **ORANGE_A**.

# RESOURCE
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
      SR_5: 71.3
    poc:
      POC_1: 118.0
      POC_2: 104.7
      POC_3: 96.4
      POC_4: 87.5
      POC_5: 67.0
    zones:
      SELL_1: 112.0
      SELL_2: 98.1
      BUY_1: 73.7
    active:
      H_FSB: 109.6
    inactive:
      H_BOS: 73.8

  1W:
    major:
      H_MAJOR: 97.9
      L_MAJOR: 80.6
    sr:
      SR_1: 100.9
      SR_2: 98.4
      SR_3: 86.8
      SR_4: 80.7
    poc:
      POC_1: 101.7
      POC_2: 94.4
      POC_3: 91.4
      POC_4: 84.4
      POC_5: 76.4
    zones:
      SELL_1: 90.8
      SELL_2: 85.4
    active:
      L_BOS: 80.6
    inactive:
      L_BOS: 107.3

  1D:
    major:
      H_MAJOR: 90.6
      L_MAJOR: 86.1
    sr:
      SR_1: 93.4
      SR_2: 89.5
      SR_3: 88.4
    poc:
      POC_1: 90.2
      POC_2: 82.8
      POC_3: 78.8
      POC_4: 70.8
      POC_5: 68.1
    zones:
      SELL_1: 75.4
    session:
      PDH: 71.7
      PDL: 67.3
    active:
      L_BOS: 86.1
    inactive:
      L_MSB: 89.3

  4H:
    local: 
      H: 71.8
      L: 67.3
    major:
      H_MAJOR: 79.4
      L_MAJOR: 70.2
    sr:
      {}
    poc:
      POC_1: 86.4
      POC_2: 75.2
      POC_3: 73.8
      POC_4: 66.0
      POC_5: 69.4
    zones:
      SELL_1: 69.2-72.0
    active:
      L_BOS: 74.6
    inactive:
      L_BOS: 86.1

  1H:
    major:
      H_MAJOR: 71.8
      L_MAJOR: 68.3
    sr: {}
    poc: {}
    zones:
      SELL_1: 70.7
      SELL_2: 69.6
      BUY_1: 63.0
      BUY_2: 66.9
    active:
      H_CHOCH: 70.0
    inactive:
      H_FSB: 71.5
      L_MSB: 69.3
```
