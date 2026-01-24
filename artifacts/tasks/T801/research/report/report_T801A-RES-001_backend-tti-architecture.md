---
artifact_type: 'REPORT'
initiative_id: 'T801'
epic_id: 'T801A'
research_id: 'T801A-RES-001'
version: '1.0.0'
iteration: '1'
date: '2025-11-23'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
---

# Backend Timeframe Trend Identification (TTI) Architecture

## I. Executive Summary

This report addresses four architectural unknowns for the LLM_Trader TTI (Trend & Technical Indicator) migration. For each topic – Numeric Scoring, Output File Format, Price Action (PA) Signals, and Divergence/Crossover Signals – we compare industry-standard approaches and provide recommendations tailored to LLM integration and deterministic backend design. Key findings and decisions include:

- **Numeric Trend Scoring**: A 5-point symmetric scale (-2 to +2) is recommended for trend strength, mapping to Strong Downtrend through Strong Uptrend. This approach aligns with common analyst ratings (e.g. TradingView's Strong Sell to Strong Buy categories), offering intuitive labels for the LLM while retaining a deterministic numeric basis. We define clear formula thresholds (e.g. +2 = higher highs/lows confirmed and high trend-momentum indicator value) to ensure consistency.

- **Output File Format**: Use structured JSON for TTI outputs, with a defined schema for trend scores and signals. JSON offers strict schema enforcement and easy parsing, supporting traceability and governance needs. While JSON is verbose, we mitigate token overhead by keeping the schema lean (only key fields). A sample JSON schema is provided, illustrating fields for the numeric score, textual trend label, and detected signals. This format ensures the LLM reliably ingests analysis results as context.

- **Price Action Signal Detection**: Implement algorithmic detection of fundamental price action patterns (focus on swing highs/lows and simple breakout logic) as the MVP. Fully coding complex patterns is feasible but would require sophisticated rules to avoid false signals. We prioritize a deterministic swing-point algorithm – identifying higher-highs/higher-lows for uptrends and vice versa – as a basis for trend detection. Breakouts are flagged when price exceeds the last swing high/low. This "partial algorithmic" approach covers core PA signals with low complexity, and yields consistent outputs. Advanced pattern recognition can be added iteratively or with hybrid methods in later phases.

- **Divergence & Crossover Signals**: Moving average crossovers (e.g. golden/death crosses) will be supported in MVP due to their clear, rule-based nature (one line crossing another) and high determinism. In contrast, bullish/bearish divergence detection is deferred for MVP – it's technically possible to auto-detect (price making new low while oscillator doesn't, etc.), but is relatively subjective and prone to interpretation. Excluding divergence initially preserves system determinism and reduces complexity. The scoring system will treat crossover signals as contributing factors (e.g. a bullish crossover reinforces an uptrend score), whereas divergences can be noted qualitatively in future when reliably detectable.

- **Cross-Topic Integration**: The numeric score (Topic 1) directly informs the JSON schema (Topic 2) – the output file will include fields like "trend_score": 2 and "trend_label": "Strong Uptrend" for LLM-friendly interpretation. PA signals (Topic 3) and crossover signals (Topic 4) populate a structured "signals" section of the JSON with boolean or categorical entries (e.g. "higher_highs": true, "MA_50_200": "bullish_cross"). These signals also influence the trend score: for example, a bullish crossover and consistent higher highs would result in a +2 score (strong uptrend), whereas a detected bearish divergence in an uptrend might cap the score or flag a caution. The final architecture (see Figure below) cleanly separates data processing and LLM logic – a webhook triggers the TTI engine to generate the JSON file, which is then fed into the LLM prompt, ensuring a governed, repeatable flow from raw market data to LLM output.

---

## II. Numeric Scoring System for Trend Strength

**Objective**: Determine an optimal numeric scale to represent trend strength (bullish/bearish) that is easily interpreted by the LLM and generated consistently by the backend. We compare common scales: small symmetric integer ranges, percentage/100-point scales, and purely ordinal categories.

### Industry Practices

Technical analysis often reduces trend outlooks to categorical ratings or numeric scores. For example, the Chande Trend Meter (CTM) condenses multiple indicators into a 0–100 score, with defined bands: 90–100 = very strong uptrend, 20–60 = flat/weak downtrend, 0–20 = strong downtrend. Another approach is used by TradingView's technical rating, which averages indicator signals into a continuous -1 to +1 value, then maps to five ratings from Strong Sell to Strong Buy. Many analyst and quant systems use 5-tier ordinal scales (e.g. strong buy, buy, hold, sell, strong sell), effectively a symmetric five-point scheme. The need for directionality often leads to negative values indicating bearish trends and positive for bullish – for instance, one could attach a sign to a strength metric like ADX (Average Directional Index) to get a -100 to +100 scale (ADX itself is 0–100 measuring strength but non-directional).

### Scale Options Comparison

| Scale Option | Description & Examples | LLM Interpretability | Determinism & Precision |
|---|---|---|---|
| **Symmetric 5-Point** (e.g. -2, -1, 0, +1, +2) | Small integer scale with explicit direction. Example: -2 = Strong Downtrend, 0 = Neutral, +2 = Strong Uptrend. Often mapped to labels (e.g. TradingView "Strong Sell"=-1, "Strong Buy"=+1 averaging scheme). | High: Very easy for an LLM to reason about five distinct values and their meanings (especially if accompanied by labels). Coarse scale avoids subtle numeric ambiguity. | High: Deterministic thresholds can be set for each integer. Less granularity, but each step can be tied to clear rules (e.g. +2 requires multiple bullish criteria). Simpler to test and audit. |
| **Continuous 0–100** (or -100 to +100 with sign) | Fine-grained percentage or index-style score. Examples: ADX trend strength uses 0–100 (no direction); CTM computes 0–100 and defines bands. A signed variant could apply direction to such an index. | Medium: LLM can handle numeric scales but may not innately know what (say) "72" means without context. Would require prompt context to map ranges to concepts. | High (resolution): Captures nuanced differences. Deterministic if formula is defined, but risk of overfitting small changes. Needs mapping of numeric ranges to categories for communication (introducing more rules). |
| **Ordinal Categories** (Discrete Labels) | Qualitative levels with implicit order. Example: {Strong Downtrend, Downtrend, Sideways, Uptrend, Strong Uptrend}. Often used in narratives and analyst reports. | High (natural): Very intuitive for LLM – categories are plain language. No numeric parsing needed. | Medium: Backend must still derive these via rules (effectively a hidden numeric or criteria set). Directly outputting text is deterministic if rules are clear, but harder to quantify changes or combine with numeric thresholds without an underlying scoring mechanism. |

### Feasibility and Design

A symmetric 5-point scale (-2 to +2) with defined thresholds is recommended as the optimal middle ground. It aligns with common 5-tier rating systems (facilitating benchmarking against industry terms) and provides directionality inherently. We will implement a rule-based point system to derive this score, ensuring determinism. For example, we can assign points for multiple trend criteria similar to known rating strategies. Industry example: the thinkorswim "Technical Score" adds one point for each criterion met (price above MA, rising moving average slope, etc.). Inspired by this, our scoring formula will aggregate signals such as:

- **Trend Direction**: +1 if an uptrend pattern of higher highs/lows is confirmed (or -1 for a confirmed downtrend). This uses price action structure as the primary trend indicator.
- **Momentum Strength**: +1 if trend momentum is strong. For instance, if an ADX or similar indicator > threshold (e.g. ADX > 25 indicates a strong trend). Extreme momentum (ADX >> 50) might be required for the highest score.
- **Signal Confirmation**: +1 for supporting technical signals (e.g. a bullish MA crossover in an uptrend, or a major resistance breakout). Conversely, -1 for bearish confirmations in a downtrend.
- **Contradictory Signals**: -1 if any opposing warning signs appear (e.g. a bearish divergence against an uptrend, or trend weakening signs), to temper an otherwise strong score.

Using these components, the maximum +2 or -2 is only reached when all bullish or all bearish factors align, respectively. For example, to output +2 (Strong Uptrend), we would require clear higher-highs/higher-lows structure, and a high trend strength reading (ADX well above 20) and at least one bullish confirmation signal (like a golden cross), with no contradictory divergence. A more moderate uptrend lacking one of these might score +1. Neutral (0) is assigned when bullish and bearish factors cancel out or none are decisive – e.g. a sideways range or mixed signals. These thresholds will be explicitly documented and coded, so that "What constitutes a 'strong uptrend'?" is answered by a transparent rule set (for instance: Score = +2 if (trendDirection==up) AND (ADX≥30) AND (MA50>MA200); Score = +1 if uptrend but ADX modest, etc.).

### Recommendation – Adopt 5-Point Scale

We will implement a -2 to +2 scoring system, outputting both the numeric score and an explanatory label for clarity. This scale is small enough for the LLM to reliably incorporate (just five categories) and ensures the backend can deterministically justify each score. By mapping multiple raw metrics into this fixed scale, we preserve interpretability (e.g. the LLM can be told "Trend Score +2 = Strong Uptrend") while using a robust multi-criterion formula under the hood for accuracy. The scoring formula will draw on industry best-practices (e.g. confirm trend by higher highs/lows, gauge strength via ADX, etc.) to ensure that the numeric scores correspond to widely-understood trend assessments.

**Threshold Example**: An illustrative mapping – +2: price in sustained uptrend, ADX > 30 (strong trend), and recent golden cross occurred; +1: mild uptrend (higher lows forming) with ADX ~20–25; 0: no clear trend (range-bound or indicators mixed); -1/-2: analogous conditions for downtrends. These specific values will be fine-tuned on historical data but serve as a starting point.

### Validation Methodology

(Insert as a new subsection under Topic 1; aligns with the requested backtesting + acceptance gate + calibration loop.)

**Backtesting Approach**

* Run the scoring formula on **N ≥ 100 trading days** per asset/timeframe (recommend stratifying across regimes: low-vol, high-vol, trending, ranging).
* Compare `trend_score` (-2…+2) to **subsequent realized movement** over a fixed horizon (e.g., next 5 / 10 / 20 bars) and/or to **human-labeled TTI classifications** (trader review set).
* Metrics: confusion matrix per class, precision/recall for extreme classes (+2/-2), and agreement score vs traders (e.g., % agreement; optionally Cohen's kappa if you maintain multi-rater labels).

**Acceptance Criteria (initial cutover gates)**

* **Minimum:** ≥ 70% overall classification accuracy across classes.
* **Strong-signal:** ≥ 80% precision for extreme outputs (+2 / -2).
* **False positives:** ≤ 20% for any extreme class (e.g., `+2` followed by materially negative returns over the chosen horizon).

**Ongoing Calibration**

* Monthly drift check; quarterly threshold review if metrics fall below gates.
* Feedback loop: allow traders to flag "incorrect TTI" samples for targeted rule/threshold refinement.

**Production Cutover Gate**

* Meets criteria on a rolling 30+ day window; trader review approves a minimum sample (e.g., 20 recent classifications) including high-volatility segments.

---

## III. File Format for TTI Output

**Objective**: Decide on an output file format (JSON, YAML, Markdown, or a hybrid approach) for the TTI engine's results that balances schema rigidity, LLM ingestion reliability, traceability, and ease of rendering.

### Considerations

The output will contain structured data (trend score, signal flags, etc.) that must be passed into the LLM's context. A structured format (JSON/YAML) offers clear schema and machine-readability, but the LLM is ultimately a text-based consumer – thus, format can affect token usage and the model's ability to interpret the content.

- **JSON (JavaScript Object Notation)**: Widely used for structured data. **Pros**: Rigid schema enforcement (ideal for validation and governance); easy for downstream systems to parse or even for LLM if guided (the model sees explicit keys and values). Integrates well with tools (and possible future function calling interfaces). **Cons**: Verbose syntax (curly braces, quotes) adds overhead – tests show JSON can inflate token count by ~15–20% vs. Markdown for equivalent content. Pure JSON is less human-readable; if the LLM is expected to reason over it, it might require a system message hint to "parse the JSON above". However, modern LLMs were trained on plenty of JSON-like data, so they can handle it, albeit in a "technical" mode. There's a risk that the model focusing on JSON might treat it like code and lose some nuance, but for factual data this is acceptable.

- **YAML (YAML Ain't Markup Language)**: A human-friendly data format that can represent the same structures as JSON (and can be converted to JSON). **Pros**: Less syntactic clutter (no quotes/braces for every field), so slightly more concise than JSON in tokens. Readable to humans (indentation-based). **Cons**: Indentation sensitivity could be problematic if an LLM were generating or modifying it (but here the backend produces it, so that's controllable). The LLM parsing it is similar to JSON parsing in complexity. YAML also has features like references, aliases which we wouldn't use – effectively we'd use it as "JSON-lite". Traceability and schema enforcement are slightly weaker (no ubiquitous JSON Schema analog, though one can define expected fields). Overall, YAML shares many of JSON's trade-offs, with minor improvements in readability at the cost of an extra parser layer.

- **Markdown**: A lightweight markup language for text that can include structure (headings, bullet lists, tables). **Pros**: Highly readable and natural for LLMs – Markdown is essentially how models see a lot of formatted text (and is more token-efficient). It can present data in tables or lists, which the LLM can understand narratively. It's also easy to render for end users (e.g. viewing the file as a report). **Cons**: Lacks strict schema – the format is free-form. Ensuring the presence or correctness of specific fields is harder (no easy automated validation that "trend_score" was output). The LLM might misunderstand or ignore a piece of data if it's not clearly delineated. For traceability, comparing Markdown outputs or enforcing consistency might be challenging (one run might phrase something differently). In short, Markdown is flexible but not deterministic enough for a backend-to-LLM data exchange where every field matters.

- **Hybrid Approaches**: This could mean outputting structured data embedded in a Markdown report – for instance, a JSON code block within a Markdown document, or a Markdown table of key signals. A hybrid could try to get the best of both: machine-parseable core data plus human-readable commentary. **Pros**: Can present critical data in a strict format and also provide a narrative summary for the LLM to read naturally. For example, a top section in JSON (for the model to parse with certainty), followed by a plain-language interpretation that the model could also draw on. **Cons**: Increases complexity – essentially maintaining two synced representations. Might be overkill for MVP, and there's risk the LLM gives more weight to one representation. Also requires the backend to produce both formats correctly.

### Format Options Comparison

| Format | Schema Flexibility | LLM Ingestion Reliability | Traceability & Validation | Ease of Human Reading |
|---|---|---|---|---|
| **JSON** | Rigid schema (exact fields/types enforced). Supports nested structures and strict typing. | Reliable if prompt directs the LLM to parse it – the structure is explicit, though model might treat it as code-like content. Some overhead (~15% more tokens). | Excellent: easily diff-able, and can apply JSON Schema for validation. Provenance of each field is clear. | Medium: Not friendly to read raw (requires tools or mental parsing). |
| **YAML** | Rigid (like JSON) – same data models. Allows comments (could embed notes). | Similar to JSON for the LLM; slightly less overhead (no quotes). Model must interpret indentation but should be able to if formatted properly. | Good: human diff-able, though validating format needs YAML parser. No robust schema standard by default, but can convert to JSON for validation. | High: Easier to skim than JSON due to minimal syntax. |
| **Markdown** | Low formal schema – structure via headings or lists, but not enforceable. | Very high by default – LLM reads it as normal text, so no risk of format confusion. However, model might miss details if not carefully formatted (e.g. buried in paragraph). | Weak: Hard to verify all required data present. Changes in phrasing can hide differences. Not machine-validated easily. | Very high: Optimized for readability. Can be directly shown to users or written in report style. |
| **Hybrid** (JSON + Markdown) | Combines structured core with free-form explanation. | High, if model is instructed properly. The JSON part guarantees data presence; the narrative aids understanding. Slight increase in prompt size. | High: core data is still JSON (or YAML) which is traceable; the rest is supplementary. | High: JSON part still less readable, but the added narrative improves clarity for users. |

### Recommendation – Use JSON with Lean Schema

We recommend JSON as the primary output format, given its determinism and compatibility with future automated pipelines. This choice prioritizes structural reliability – the LLM prompt can explicitly include "Here is a JSON technical analysis" and the model can be guided to utilize it. To address JSON's verbosity and the LLM's token limits, we will keep the schema minimal and include a concise textual label alongside numeric values for clarity. (We opt not to use pure Markdown for the data exchange, but the LLM's final answer to users can of course be in rich text/Markdown format, interpreting the JSON data.)

**Justification**: JSON's benefits in traceability and error-proofing outweigh the token cost in this context. As noted by practitioners, structured outputs enable simpler integration and reduce misinterpretation. While JSON can introduce some prompt overhead and push the model into a "formatting mode," this is mitigated by the fact that our JSON is relatively small (a few dozen lines at most) and factual. Moreover, OpenAI and other LLM providers now support function calling and structured prompts where JSON input is expected – using JSON positions us to leverage those features (and even hard enforce structure) in the future. To ensure the LLM handles the JSON properly, we will provide instructions or examples in the system prompt (e.g. "You are given technical analysis data in JSON format. Extract the insights and…"). In testing, if we observe any issues with direct JSON, we might consider slight hybridization (for example, wrapping the JSON in a Markdown code block, or adding a one-line summary above it for the model's benefit).

For governance, the JSON output serves as an audit artifact: it can be stored, version-controlled, and compared across runs to detect any changes in the analysis logic. Each field can be traced back to input data and rules, aiding explainability.

### Sample Schema

Below is a sample JSON output structure incorporating the trend score and various signals (topics 1, 3, 4). This example illustrates how information will be organized for an instrument (e.g. "BTC-USD" on a daily timeframe):

```json
{
  "asset": "BTC-USD",
  "timeframe": "1D",
  "trend_score": 2,
  "trend_label": "Strong Uptrend",
  "signals": {
    "price_action": {
      "higher_highs": true,
      "higher_lows": true,
      "breakout": "Above last 30-day high"
    },
    "moving_average": {
      "MA50_cross_MA200": "bullish", 
      "cross_date": "2025-11-29"
    },
    "divergence": {
      "RSI_bearish_divergence": false
    }
  },
  "as_of": "2025-11-29"
}
```

**Example**: In this JSON, the trend score of 2 is paired with the label "Strong Uptrend" for clarity. Under signals: the price_action subsection confirms the market is making higher highs and lows, and even notes a breakout above a recent 30-day high. The moving_average field indicates a bullish 50/200-day MA crossover (a golden cross) occurred on 2025-11-29. No bearish RSI divergence was found (false). An as_of timestamp is included for traceability.

This structured output is both human-interpretable (with plain labels) and machine-precise. The LLM will receive something similar to the above (likely embedded in the system or user prompt), and it can reliably pick out that the trend is Strong Uptrend, supported by specific signals. In sum, JSON meets our needs for unambiguous, governable data exchange, setting the stage for the LLM to do its higher-level narrative or decision-making tasks with the right facts in hand.

### Versioning Strategy

(Insert after the "Sample Schema" block.)

**Schema Version Tracking**

* Add `"schema_version": "1.0.0"` to every output file.
* **Major** bump (2.0.0): breaking changes (field removal, type changes).
* **Minor** bump (1.1.0): additive optional fields.
* **Patch** bump (1.0.1): documentation or non-structural clarifications.

**Backward Compatibility**

* New fields MUST be optional; consumers ignore unknown fields.
* Deprecated fields retained for **2 major versions** before removal.
* Maintain a schema changelog for auditability.

### Manual Override Workflow

(Insert as a new subsection in Section III.)

**Editing Process**

1. Trader opens the generated TTI JSON (text editor or UI).
2. Trader edits allowable fields (e.g., `trend_score`, `trend_label`, or specific signal flags).
3. Trader sets `"manual_override": true` and adds `"override_note": "reason"`.

**Validation Before LLM Ingestion**

* JSON syntax validation + required-field presence (`trend_score`, `trend_label`, `as_of`, `schema_version`).
* Schema-version compatibility check.
* Optional: "allowed-fields" rule (prevent edits to provenance fields like raw OHLC references).

**Override Audit Trail**

* Add `"override_by": "trader_id"` and `"override_timestamp": "ISO-8601"`.
* Archive the original machine-generated file alongside the overridden version for diffing.

**LLM Consumption**

* If `manual_override: true`, LLM must explicitly note: *"TTI includes manual trader adjustment."*

### (Recommended) Schema Additions to Support Patches 2A/2B

Minimal additions to your sample JSON (fields are small but unlock versioning + override controls):

```json
{
  "schema_version": "1.0.0",
  "generator_version": "tti-engine/0.1.0",
  "asset": "BTC-USD",
  "timeframe": "1D",
  "trend_score": 2,
  "trend_label": "Strong Uptrend",
  "signals": { /* unchanged */ },
  "as_of": "2025-11-29",
  "manual_override": false,
  "override_note": null,
  "override_by": null,
  "override_timestamp": null
}
```

---

## IV. Price Action Signal Detection (PA)

**Objective**: Evaluate how to algorithmically detect price action signals – specifically classic trend-defining patterns like higher highs and higher lows, swing points, and breakouts – in a way that's accurate yet implementable for MVP. We compare a fully algorithmic approach (covering many patterns), a minimal swing-point approach, and a hybrid approach, considering accuracy and development effort.

### Scope of PA Signals

The primary signals in this category are derived from raw price behavior:

- **Higher Highs & Higher Lows (HH/HL)**: A series of rising peaks and troughs signifies an uptrend (conversely, lower highs & lower lows for a downtrend). This is a Dow Theory fundamental for trend identification.
- **Swing Points**: Local maxima or minima in price, around which trend changes can be identified. Often defined by a price peak flanked by lower highs on each side (swing high), or a trough flanked by higher lows (swing low).
- **Breakouts**: Price moving above a defined resistance (like a previous swing high or a range boundary) or below support. Breakouts often signal a new trend leg starting.
- **(Other patterns** like head-and-shoulders, triangles, etc., also fall under price action but are more complex; for MVP we focus on the basics that feed trend scoring.)

Detecting these signals can be done via rule-based algorithms scanning the price series. The challenge is balancing sensitivity (catching genuine signals) with specificity (avoiding noise/false signals).

### Approach Options

1. **Fully Algorithmic (Comprehensive Pattern Detection)**: Attempt to code detection for a wide array of patterns (multiple swing confirmations, breakout patterns, maybe even classical chart patterns). This could include multi-bar pattern logic and possibly heuristics for things like consolidation ranges before breakouts.

2. **Partial Algorithmic – Swing Points Only**: Focus on detecting swing highs/lows and deducing simple trend signals (HH/HL sequences) and obvious breakouts (price exceeding last swing high/low). Essentially implement the minimal logic required to determine trend direction and a breakout flag.

3. **Hybrid Approach**: Use algorithms for the basics (like swings and trend direction), but rely on an LLM or heuristic templates for more complex or contextual patterns (e.g. an LLM might look at the price history description and "interpret" if a pattern like a wedge or head-and-shoulders is present). Hybrid could also mean combining algorithmic output with some rule-based interpretations that aren't strictly hard-coded (like a rules engine that infers pattern from swings).

### Comparison of Approaches

| Detection Strategy | Implementation Complexity | Signals Covered | Accuracy & False Signals | Determinism |
|---|---|---|---|---|
| **Fully Algorithmic** (Comprehensive) | High – must program multiple pattern rules (swing structure, breakout logic, possibly pattern recognition). Requires handling many edge cases. | Broad: could include complex patterns (flags, triangles, etc.) in addition to HH/HL and breakouts. | Moderate: Well-defined rules give consistent results, but complex patterns are prone to false-positives if criteria aren't tuned (e.g. minor peaks might be mis-tagged as breakouts). More patterns = more points of potential error or contradiction. | High in theory (code is deterministic), but maintaining determinism across many patterns is tricky if rules conflict. |
| **Partial Algorithmic** (Swing points & basic trend) | Low – implement local high/low detection and simple comparisons. Easier to test and debug. | Core signals only: identifies uptrend/downtrend (via recent HH/HL), and straightforward breakouts (e.g. price > last swing high = breakout up). Complex patterns not explicitly detected. | High for included signals: Focusing on clear definitions (e.g. a swing high defined by two lower highs on either side) reduces noise. Fewer false signals because it waits for confirmation (two candles on each side for swing). Some nuance lost (complex patterns will be ignored, not misidentified). | Very High: Simple rules yield consistent output. Minimal ambiguity. The result is a clear yes/no on trend and breakout questions, improving trustworthiness for LLM input. |
| **Hybrid** (Algorithm + LLM) | Medium – need the basic algorithm plus prompt engineering for the LLM part. The LLM could examine raw price series or the swing points to identify advanced patterns. | Potentially broad: basic trend via code, advanced context from LLM (like "trend losing momentum despite HH/HL" or detecting an unusual pattern). | Variable: LLM could provide rich insights, but not guaranteed consistent – the same data might yield slightly different descriptions each run. Risk of non-determinism and difficulty validating outputs. Also, LLM could "hallucinate" a pattern that isn't formally defined. | Lower: The involvement of LLM means results aren't 100% reproducible unless the prompt is extremely constrained. Harder to govern under strict rules (would need checking of LLM's interpretation). |

### Feasibility

Given MVP needs and the desire for determinism, fully algorithmic detection of every pattern is not necessary initially (and could significantly slow development). Many complex patterns can be broken down into combinations of swings and breakouts anyway. A partial algorithmic approach focusing on swing highs/lows and basic trend signals is very feasible: identifying local extrema is a classic algorithm (iterate through price points and mark those higher than neighbors for swing highs, etc.), and determining an uptrend just means the last few swing highs are successively higher. Breakout detection can be as simple as checking if the latest price > previous swing high (or a recent range high over N days).

Such rule-based methods are easy to test with known scenarios and yield explainable results (e.g. "Uptrend=True because the high on Nov 20 exceeded the high on Nov 10, and the low on Nov 21 was higher than the low on Nov 11"). This level of transparency is valuable for debugging and for the LLM to potentially explain the signals.

### Example – Pseudocode for Swing/Trend Detection

```python
# Identify swing highs/lows in price series
swing_highs = []
swing_lows = []
for i in range(2, len(price)-2):
    if price[i] > price[i-1] and price[i] > price[i-2] and price[i] >= price[i+1] and price[i] >= price[i+2]:
        swing_highs.append((i, price[i]))
    if price[i] < price[i-1] and price[i] < price[i-2] and price[i] <= price[i+1] and price[i] <= price[i+2]:
        swing_lows.append((i, price[i]))

# Determine latest trend direction
trend_direction = "Neutral"
if len(swing_highs) >= 2 and len(swing_lows) >= 2:
    last_high, prev_high = swing_highs[-1][1], swing_highs[-2][1]
    last_low, prev_low   = swing_lows[-1][1], swing_lows[-2][1]
    if last_high > prev_high and last_low > prev_low:
        trend_direction = "Uptrend"
    elif last_high < prev_high and last_low < prev_low:
        trend_direction = "Downtrend"

# Detect breakout above last swing high (if current price exceeds it)
recent_swing_high = swing_highs[-1][1] if swing_highs else None
breakout_up = (price[-1] > recent_swing_high) if recent_swing_high else False
```

This pseudo-code finds swing highs/lows by looking for a price point higher (or lower) than two neighbors on each side. Then it checks the two most recent swing highs and lows: if both highs and lows are increasing, we label an Uptrend (Downtrend if both decreasing). Finally, it flags a breakout_up if the latest price exceeds the last swing high. A similar check can be done for downside breakouts (price dropping below the last swing low). These logical steps will form the backbone of our PA signal detection.

### Accuracy Considerations

This method is robust for clear trends and avoids premature signals. By requiring at least two swing points, we naturally filter out one-day spikes or noise (a single higher high doesn't flip trend to uptrend unless accompanied by a higher low). The use of confirmed swings (two lower highs around a peak) means we wait for structure to form before signaling, which should reduce false trend flips. Breakouts are identified only when price truly exceeds prior key levels, which is straightforward and unambiguous.

There are edge cases – e.g. in a choppy market, we might get rapid alternation of trend direction signals if swing points form without follow-through. We can mitigate this by, say, requiring a minimum price move or time distance between swing points, or by buffering the neutral state (only go to Uptrend if it was neutral or up before, not straight from downtrend without a neutral stage). These refinements can be added as needed.

### Recommendation – Algorithmic Swing/Breakout Detection

For MVP, proceed with partial algorithmic PA detection centered on swing highs/lows and breakouts. This covers the essential information needed for trend scoring: it will tell us if a clear uptrend or downtrend is in place and if a recent breakout has occurred (valuable for scoring strength). The implementation is straightforward and implementation-ready using well-known methods. It provides a deterministic, traceable set of signals: the output might say, for example, "higher_highs": true, "higher_lows": true, "breakout": "Above 30-day range" as seen in the JSON example, which the LLM can then translate to "The asset is making higher highs and higher lows, and has broken out above its recent range, indicating a strong uptrend."

We will defer complex pattern recognition (flags, triangles, etc.) to future iterations or possibly treat them qualitatively. Not only does this keep the system simpler, it also avoids us hard-coding interpretations that might overlap with what the LLM can infer from context if needed. In later versions, if higher sophistication is required, we can either expand the algorithmic library of patterns or allow the LLM to ingest price data more directly for pattern finding – but that's out of MVP scope. For now, the chosen approach ensures we capture the vital signs of price action in a reliable manner.

---

## V. Divergence and Crossover Signal Detection

**Objective**: Assess adding detection for momentum divergences (bullish/bearish divergence typically between price and an oscillator like RSI or MACD) and moving average crossovers (e.g. golden cross, death cross). Determine which of these signals to include in the MVP, balancing feasibility and determinism.

### Signals Defined

- **Bullish/Bearish Divergence**: A bullish divergence occurs when price makes a lower low but an oscillator (e.g. RSI) makes a higher low – indicating weakening downside momentum, often before an upward reversal. A bearish divergence is the opposite (price high higher, oscillator high lower). Divergences are valuable as early warnings but can be subjective – one must choose which highs/lows to compare on price vs indicator. They come in classes (A, B, C) depending on strength, further adding nuance.

- **Moving Average (MA) Crossovers**: A crossover happens when a shorter-term MA crosses above or below a longer-term MA. The classic Golden Cross is a bullish signal where (for example) the 50-day MA crosses above the 200-day MA. The Death Cross is the bearish counterpart (short MA crosses below long MA). Crossovers give clear trade signals and are very popular in trend-following strategies.

### Feasibility Analysis

- **Divergence Detection**: Algorithmically detecting divergence requires identifying peaks and troughs in both price and an indicator and then comparing their relative movement. This is similar to swing detection but on two series. It's feasible: one could reuse the swing-finding algorithm on price and on, say, RSI values, then see if price made lower low while RSI made higher low within roughly the same time window. However, tuning is needed: how far apart can the lows be and still count as the "same" event? What minimum difference constitutes a meaningful divergence versus normal oscillation? These involve judgment calls. There's also a risk of many minor divergences being found unless filtered (e.g. require RSI to move out of overbought/oversold extremes to qualify). In short, an algorithm can catch divergences, but ensuring they're the significant ones (Class A divergences in technical terms) can be complex. Still, divergence rules can be made deterministic – e.g. "Flag bullish divergence if: in last 14 days price made a new low 2% below prior low, and RSI at that new low was at least 5 points higher than at prior low, and RSI was <30 at first low" – but these parameters might need tweaking per asset or timeframe. On the LLM interpretive side, divergence is something an LLM could notice if given both price and indicator data, but it's safer to compute it than rely on the LLM, as it's a precise technical condition.

- **MA Crossover Detection**: This is straightforward. The backend can compute moving averages for the chosen periods (we will likely focus on one or two key sets, e.g. 50/200-day for long-term trend shifts, and perhaps a shorter MA cross like 20/50 for shorter trend). A crossover event is simply when the ordering of the MAs changes from one day to the next. For example, yesterday MA_short <= MA_long and today MA_short > MA_long means a bullish crossover occurred today. This is a single-step deterministic check with no ambiguity (aside from the rare case of MAs being exactly equal, which is negligible). Crossovers are highly deterministic and unambiguous – exactly the kind of signal suited for algorithmic detection. They are also widely recognized signals of trend confirmation or reversal, which aligns with our trend scoring (e.g. a golden cross strongly supports an uptrend score).

### Trade-off Analysis Table

(Add directly under Topic 4 narrative; required deliverable.)

| Pattern                    | Backend Feasibility                     | LLM Interpretive Value             | Implementation Cost    | Recommendation   |
| :------------------------- | :-------------------------------------- | :--------------------------------- | :--------------------- | :--------------- |
| **MA Crossover (50/200)**  | High (deterministic, single check)      | Medium (LLM explains significance) | Low                    | ✅ Include in MVP |
| **MA Crossover (20/50)**   | High (same logic as 50/200)             | Medium (short-term confirmation)   | Low                    | ✅ Include in MVP |
| **Regular RSI Divergence** | Medium (swing detection on RSI + price) | High (LLM adds context)            | Medium (tuning needed) | ❌ Defer post-MVP |
| **Hidden RSI Divergence**  | Low (subjective, false positives)       | High (nuanced interpretation)      | High                   | ❌ Defer post-MVP |
| **MACD Divergence**        | Medium (similar to RSI divergence)      | High (momentum confirmation)       | Medium                 | ❌ Defer post-MVP |

**Rationale Summary**

* **MA Crossovers:** high feasibility + low cost + deterministic → MVP.
* **Divergences:** medium/low feasibility + tuning burden + higher false-positive risk → defer until scoring validation is stable.

### MVP Inclusion Recommendation

We propose to include MA crossovers in the MVP signal set, and defer divergence detection for now. The rationale:

- **Crossovers are easy to implement and interpret.** They will provide concrete signals to strengthen or weaken the trend score. For example, if an asset is in an uptrend and a golden cross occurs, that's an extra point of confirmation towards a strong uptrend. Conversely, if in a downtrend and a death cross occurs (or golden cross in a downtrend context), we might adjust scoring or flag it as a mixed signal. In terms of output, we can simply output fields like "MA50_cross_MA200": "bullish" or "bearish" with a date. This is exactly as shown in the sample JSON (Topic 2) where "MA50_cross_MA200": "bullish", "cross_date": "2025-11-29" indicates a golden cross on that date. The deterministic nature means we can trust this data and the LLM can too.

- **Divergences on the other hand, while valuable, add significant complexity and potential non-determinism.** If we implement it in code, we'd need to choose parameters (which might end up somewhat arbitrary without extensive backtesting). If we involve the LLM to identify divergences, we lose determinism and risk inconsistent identification. Additionally, divergence signals, especially on indicators like RSI or MACD, can be frequent and not all are actionable – including them without a robust filter could clutter the output or confuse the LLM ("multiple small divergences detected" doesn't clearly tell if the trend is ending or just pausing). Given MVP focus, it's safer to exclude or perhaps implement only the most obvious divergence cases (for instance, maybe check just the last major swing vs oscillator). We can document this as a known gap and plan to add it later once trend scoring and other basics are validated.

### Impact on Scoring

By deferring divergence, we ensure that the trend score remains purely a function of clear factors (price action, momentum, crossovers) for now. Divergence typically serves as a caution flag – e.g. in a strong uptrend, a bearish divergence might suggest momentum waning. Since we're not coding divergence at MVP, the LLM won't get an automated flag about it. However, if the underlying momentum indicator (like RSI) is included in data, the LLM might still "see" it (though we're not explicitly giving raw RSI values in the JSON, only possibly a note if we choose). We could mitigate missing divergence by a conservative approach to scoring: e.g. don't give +2 unless momentum is strong and no obvious weakness. This way, a situation that would have a divergence likely just results in a +1 instead of +2, implicitly accounting for it. In any case, excluding divergence keeps our system simpler and we can rely on the LLM's general knowledge to some extent (the LLM, when formulating a response, might mention "momentum is not fully confirming the trend" if it sees a high RSI or such – but we won't depend on that).

### Pseudo-Code – MA Crossover Detection

(to be integrated in the engine)

```python
# Assuming we have series: MA_short[i], MA_long[i] for each time index i
cross_signal = None
cross_date = None
if MA_short[-2] < MA_long[-2] and MA_short[-1] > MA_long[-1]:
    cross_signal = "bullish"   # Golden cross
    cross_date = current_date
elif MA_short[-2] > MA_long[-2] and MA_short[-1] < MA_long[-1]:
    cross_signal = "bearish"   # Death cross
    cross_date = current_date
# Else, no new cross today.
```

This check looks at the last two days ([-2] being yesterday, [-1] today for instance). It sets a cross_signal if a crossing occurred. We will likely maintain a state to know if a crossover happened recently, so we can report "just happened" versus "already in a crossed state." For output, we only need to report when a crossover event occurs or has occurred in the recent period relevant to analysis. In many cases, we might output the last significant crossover on record (e.g. if a golden cross happened 10 days ago and still holds, it's relevant).

### Feasibility

Implementation of MA is straightforward (we already compute MAs for trend strength anyway, e.g. to check price above MA or slope). Computationally trivial. Divergence code would be more involved, but since we're deferring it, no immediate work is needed there.

### Recommendation – Include Crossovers, Defer Divergence

We will integrate MA crossover detection (at least for one prominent pair of MAs, 50/200 for long-term trend, possibly 20/50 for intermediate – we will decide which are most meaningful for our use case). The output will explicitly note any bullish or bearish crossovers. We will not include automated divergence detection in the MVP. This keeps the system deterministic and focused. As a result, Topic 4 signals influencing Topic 1 scoring will primarily be the crossover signals: e.g., a bullish crossover will boost confidence in an uptrend score (or might be required to achieve a +2 in some cases), whereas the absence of any crossover in a supposed uptrend might keep the score at +1 if other factors aren't as strong. If divergence were included later, it would serve to dampen the score (e.g. detect bearish divergence in an uptrend -> maybe drop score from +2 to +1, reflecting caution). For now, we simply note that divergence handling is deferred to a future iteration or expert review. Any critical momentum issues should still be somewhat captured by our use of ADX/RSI in the trend strength logic (e.g. if momentum is low, we wouldn't score a +2 anyway).

In summary, moving average crossovers offer a deterministic, interpretable signal we can confidently add to the backend now, whereas divergences – being interpretive by nature – are best left out of the initial deterministic system to avoid uncertainty. This decision ensures that every signal our backend produces can be trusted and easily explained.

---

## VI. Integration & Unified Architecture

Having addressed each component individually, we now consider how they interoperate in the backend and how they collectively feed into the LLM pipeline.

**Figure**: Proposed backend architecture integrating the TTI engine into the LLM workflow.

In the architecture above, the flow is as follows:

**Webhook → TTI Engine → JSON Generate → Validate → (Optional Manual Override) → Re-Validate → LLM Consumption**

1. **Webhook Trigger**: An external event (e.g. a scheduled time or a user request) triggers the TTI Engine. This could be a webhook carrying a payload like "analyze BTC-USD on daily timeframe" or a simple scheduled job. The webhook ensures the process starts in a controlled manner (and could pass any necessary parameters or data references).

2. **TTI Engine (Backend Analysis)**: This is the core computation module. It retrieves the latest price data (and any indicator data needed, like for MA or RSI) for the asset/timeframe in question. It then applies the algorithms and rules we've defined:
   - Computes trend strength score based on price action and indicators (Topic 1 logic). E.g., determine trend direction via swings, compute ADX or similar to gauge strength, check for MA crossover, etc., then aggregate into the -2 to +2 score.
   - Detects signals: higher highs/lows, breakout status (Topic 3), moving average crossovers (Topic 4). (In MVP it will not detect divergence signals – leaving that part empty or null in the output.)
   - As it computes these, it populates a structured data object (following the JSON schema). All rules here are deterministic, so given the same input data, the output file will be identical every time.
   - This step is purely backend (no LLM logic yet), ensuring we separate fact generation from interpretation.

3. **File Generation & Validation**: The TTI Engine then outputs the analysis file – in our chosen JSON format – either writing to a storage or directly passing it along. This JSON contains fields like in the sample: the numeric score, a textual label, and sub-objects for each category of signals. Each entry is filled based on the engine's findings (or left null/false if not applicable).
   - For example, after analysis the engine might produce: "trend_score": 2, "trend_label": "Strong Uptrend", "higher_highs": true, "higher_lows": true, "breakout": "Above last 30-day high", "MA50_cross_MA200": "bullish", "cross_date": "2025-11-29", etc., exactly as demonstrated earlier.
   - The generated file undergoes validation (JSON syntax, required fields, schema version compatibility) before proceeding.
   - This file can be logged for audit (fulfilling governance needs: one can later open this file to see on what basis the LLM was prompted).

3a. **(Optional Manual Override)**: If a trader needs to adjust the TTI output, they can manually edit the JSON file, setting `manual_override: true` and adding an `override_note`. The modified file is then re-validated before LLM consumption. The original machine-generated file is archived alongside the override for auditability.

4. **LLM Input Integration**: The validated JSON output (whether original or manually overridden) is then fed into the LLM's context. There are a couple of ways to do this:
   - The simplest is to insert the JSON content into the system or user prompt for the LLM. For instance, the system prompt might say: "You are a trading assistant. You are given technical analysis data in JSON format. Use it to answer the user's question." Then include the JSON. The LLM will parse the JSON (which it's capable of doing given proper instruction) and internalize those facts.
   - Alternatively, if using an LLM API with function calling, the JSON could be passed as a function result. But for our scope, we assume it's part of the prompt text.
   - Because we included human-readable labels in the JSON, the LLM sees not just numbers but context (e.g. it sees "trend_label": "Strong Uptrend", which it can directly incorporate into a sentence like "The trend is a strong uptrend."). This improves interpretability.
   - The LLM ingestion reliability is high here because the input is structured and unambiguous. We avoid the LLM having to perform any heavy analysis itself – it just has to read the analysis. This partition of labor (backend does analysis, LLM does explanation/generation) is key to a deterministic yet flexible system.

5. **LLM Processing and Output**: Finally, the LLM (with its full prompt including the analysis data and possibly a user query or task instruction) generates the output (e.g. a paragraph of insights, answering a question like "What is the trend and why?"). The LLM's output is informed by the JSON data: it will likely mention the trend score or label and the supporting signals. For instance, it might produce: "The technical analysis indicates a Strong Uptrend – the stock has been consistently making higher highs and higher lows, and it even broke out above its recent 30-day high. Furthermore, the 50-day moving average has crossed above the 200-day (a bullish golden cross on 2025-11-29), adding confirmation to the positive trend. No major bearish divergences are noted, so the uptrend momentum appears intact." This kind of narrative is exactly what we want the LLM to do, and it can do so confidently because the facts are provided and were derived deterministically.

### How Topic 1 influences Topic 2

The numeric scoring choice directly shaped the JSON schema. We decided to include both a numeric field and a descriptive label. The label is essentially an LLM helper – since we chose a discrete scale, we can attach a short descriptor (e.g. Strong Uptrend) that the LLM can read without needing to interpret the number on its own. If we had chosen a 0–100 scale, we might instead provide ranges or multiple fields (score and maybe a normalized percentage). By using -2 to +2, we keep the schema simple (one score field) and just add a label for clarity. This ensures determinism (score is fixed) but also interpretability (LLM sees a familiar phrase). The backend determinism of Topic 1 means the same inputs will always yield the same trend_label, so the LLM's behavior will be consistent too.

### How Topics 3 & 4 appear in the output (Topic 2)

All the signals detected (price action trends, breakouts, MA crosses) are included in the JSON under logical groupings. We saw this in the sample: a "price_action" object containing flags like higher_highs, etc., and a "moving_average" object for crossover info. If, say, no crossover had occurred recently, the engine might either omit that field or mark it as null/false (depending on schema choices). The LLM will either ignore missing fields or interpret null as "no signal". For example, if "MA50_cross_MA200" was absent or null, the LLM wouldn't mention any crossover. By explicitly showing each signal's presence or absence, the format ensures the LLM doesn't hallucinate a signal – it only knows what is flagged. This structured presentation also makes it easy to extend; e.g., if in future we add divergence, we'd introduce a "divergence" section. In the current MVP, since divergence is not auto-detected, the JSON shows "RSI_bearish_divergence": false (as in sample) or we might even exclude the divergence section entirely. In either case, the LLM will understand that no divergence was found, meaning nothing to worry about on that front.

### How Topic 4 signals influence Topic 1 scoring

The integration of crossover signals into the score was designed from the start. In the trend scoring rules, a bullish crossover is considered a reinforcing factor for an uptrend. Concretely, if the engine detects "MA50_cross_MA200": "bullish", it likely already added a point to the trend_score or at least used it to justify moving from +1 to +2 (depending on other conditions). Similarly, if we had a bearish crossover in what otherwise was an uptrend, the engine might downgrade the score or flag the trend as weakening. Because this logic lives in the backend, by the time the JSON is produced, the trend_score already reflects those signals. The LLM then sees a consistent picture – e.g. trend_label "Strong Uptrend" alongside a bullish crossover signal; it won't encounter a contradiction like a strong uptrend label but a bearish crossover flag, because our rules would prevent that (if a bearish crossover happened, likely the trend_score wouldn't be +2). This consistency is crucial; it means the LLM doesn't have to reconcile conflicting data, making its job easier and output more coherent.

Finally, the unified architecture diagram (above) encapsulates this entire process. It highlights the separation of concerns:

- The **Backend (TTI Engine)** deals with data and rules: obtaining market data, applying technical analysis formulas, and producing a factual, structured report.
- The **LLM** deals with language and reasoning: it takes the factual report and turns it into useful output (be it a written summary, a trading decision rationale, or answers to user queries about the trend).

This design is governable – any change in analysis logic changes the JSON output which is easy to review (governance artifact), and the LLM will automatically follow suit in its outputs. It's also scalable – multiple assets or timeframes can be processed in parallel by the engine, generating JSON for each, and the LLM can consume whichever is needed on demand.

In summary, by addressing the four topics with carefully chosen solutions – a clear trend scoring system, a structured output format, reliable price action and crossover detection, and deferring fuzzy signals – we achieve a robust backend that feeds the LLM timely and trustworthy insights. This allows the LLM_Trader system to provide interpretations and decisions that are both well-grounded in deterministic analysis and communicated in the rich, flexible manner that LLMs excel at. The architectural synergy ensures that as market data flows in via the webhook, it flows out as intelligent output, with each component of the pipeline playing a well-defined role in that transformation.

---

## Sources

- **Investopedia** – ADX: The Trend Strength Indicator (trend strength thresholds); Bullish & Bearish Divergences (momentum divergence definition)
- **StockCharts ChartSchool** – Chande Trend Meter (numeric trend scoring and categories); Golden Cross (moving average crossover interpretation)
- **TradingView Support** – Technical Ratings in Screener (5-category rating mapping from numeric scale)
- **LuxAlgo Blog** – Swing Highs and Lows (swing point definition and trend inference)
- **thinkorswim (Markos Katsanos)** – Technical Stock Rating (multi-criteria point scoring example)
- **OpenAI/PromptLayer** – JSON vs Markdown for LLM (token efficiency and structured output considerations)
- **TradersPost Blog** – Chart Pattern Recognition (on complexity of pattern-detection algorithms)
