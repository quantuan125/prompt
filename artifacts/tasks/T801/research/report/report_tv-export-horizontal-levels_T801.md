Below is a complete research brief you can drop into your repository. I’ve answered the Specific Questions explicitly, then provided the deliverables (matrix, constraints, patterns with code, and recommendations).

---

# RESEARCH BRIEF: TradingView Pine Script Export of Horizontal Levels/Zones via Alerts (v1.0.0 — 2025-09-28)

## I. Executive Summary

* **Key constraint:** Pine Script **cannot read or enumerate user-drawn objects** (manual Horizontal Line, Ray, Box/Rectangle, etc.) that you place with the chart’s drawing tools. Script-created objects and user-drawn objects are distinct; there is **no API to read properties of saved drawings** (name, text, coords, color, visibility filters) from Pine. ([TradingView][1])
* **What *is* possible:** A Pine v5 indicator/strategy can **create and manage its own lines/boxes/labels** (`line.new`, `hline`, `box.new`, `label.new`) and **export their data** via `alert()` to a webhook. You can retrieve coordinates with getters like `line.get_price()`, `line.get_y1()`, `box.get_top()/get_bottom()`, and serialize to compact lines. ([TradingView][2])
* **Alert/Webhook constraints:**

  * Alerts stop if **>15 triggers in 3 minutes** (per alert). Design batching/debouncing accordingly. ([TradingView][3])
  * **Retries:** If your endpoint returns **HTTP 5xx**, TV retries up to **3 times** (≈5s spacing), so a single trigger can be sent **up to 4 times** — plan idempotency. ([TradingView][4])
  * **Message size:** TradingView does not publish an explicit “alert message limit”, but Pine **strings now support up to 40,960 encoded characters** (Aug-2025). That upper-bounds `alert()` message size you can construct in-script; still, use conservative payloads (≤4–8 KB) for reliability. ([TradingView][5])
* **Drawing-alerts:** You can set alerts **on drawings manually** in the UI, and use **standard placeholders** like `{{ticker}}`, `{{exchange}}`, `{{close}}`; however there is **no official placeholder to inject a drawing’s user-entered text/name automatically** into the payload. Traders must duplicate that text into the alert’s message if needed. ([TradingView][6])
* **MTF parity:** Use `request.security()` to **compute** HTF levels (not to draw them in `security()`), then create objects in the chart context; keep to **≤40 unique `request.*()` calls** per script. ([TradingView][7])
* **Compliance:** Using `alert()` and **webhooks** from TradingView’s UI is **sanctioned**. Accessing saved drawings via scraping/private APIs is **not supported**. ([TradingView][8])

**Bottom line:** To export levels/zones + labels reliably, **manage the levels inside the script** (inputs or programmatic detection), attach canonical tags, and **batch-serialize** to a webhook via `alert()` once per bar. Manual drawings can participate only through **manual alert messages**; they are not machine-readable by Pine.

---

## II. Specific Questions — Direct Answers

1. **Can Pine read a user-drawn Horizontal Line’s label text and price?**
   **No.** Pine cannot access properties of user-drawn drawings. Closest compliant workarounds: (a) replicate each level inside the script via `input.*` fields and render a matching `hline`/`line`; (b) use script-rendered objects with user-editable inputs; (c) for manual drawings, create **drawing alerts** and copy the desired label into the alert message template by hand. ([TradingView][1])

2. **For script-created objects, what APIs retrieve values?**

* `hline`: treat the configured price as a stored constant you manage; there’s no `hline.get_price()`, so persist your value in a `float` and reuse.
* `line.new`: `line.get_price(id, bar_index)`, `line.get_y1(id)`, `line.get_y2(id)`; also `line.get_x1/x2`. ([TradingView][2])
* `box.new`: `box.get_top(id)`, `box.get_bottom(id)`, `box.get_left(id)`, `box.get_right(id)`. ([Trading Code][9])
* `label.new`: `label.get_text(id)` and positional getters if needed. ([TradingView][10])

3. **Can alerts created on drawing tools include the drawing’s label automatically?**
   No official placeholder exists for a drawing’s text/name. Available placeholders are **standard** (`{{ticker}}`, `{{exchange}}`, `{{close}}`, etc.) and **plot/strategy** placeholders, not drawing-specific label text. Traders must duplicate text manually into the alert message. ([TradingView][11])

4. **Current maximum alert message size & safe limit?**
   TV doesn’t publish a hard “alert message length” limit. As of Aug-2025, Pine **string size** increased to **40,960 encoded characters**, which constrains what `alert()` can send. We recommend **≤4–8 KB per alert** as a practical ceiling to avoid UI or transport quirks; batch if larger. ([TradingView][5])

5. **Known issues with multi-line payloads/webhooks; encoding quirks?**
   Multi-line bodies are commonly used (e.g., JSON/CSV). Ensure your receiver accepts `text/plain` POST bodies. For reliability: (a) prefer ASCII/UTF-8; (b) escape braces if your downstream templater parses them; (c) plan for **retries and potential delays** (25–45s delays are considered normal by some integrators). ([TradingView][4])

6. **Use `request.security()` to gather HTF values for script-managed objects?**
   Yes. Compute HTF series with `request.security()` (observe **≤40 unique requests**) and **draw in chart context** (outside `security()`). Avoid repaint by using **confirmed data** and lookahead-safe patterns. ([TradingView][7])

7. **Any supported API/export for chart “saved drawings”?**
   No supported API. Pine **cannot** access or export saved drawings. ([TradingView][1])

8. **Reference implementations close to this use case:**

* **Pine docs: Alerts & placeholders** (end-to-end overview). ([TradingView][12])
* **Lines & boxes getters** (official docs with examples). ([TradingView][2])
* **Multi-TF + alerts sample scripts** (community/public examples using `alert()` and `request.security()` within limits). ([TradingView][13])

---

## III. Capability Matrix (object support vs. exportability)

| Object Type (source)             |                Readable by Pine? | Editable by Pine? |                         Exportable via `alert()` with label? |                              MTF-aware in export? |
| -------------------------------- | -------------------------------: | ----------------: | -----------------------------------------------------------: | ------------------------------------------------: |
| **Horizontal Line (user-drawn)** |                           **No** |                No | Only via **manual** drawing-alert; label not auto-includable |                                               N/A |
| **Ray/Trend line (user-drawn)**  |                           **No** |                No |                                    Manual drawing-alert only |                                               N/A |
| **Box/Rectangle (user-drawn)**   |                           **No** |                No |                                    Manual drawing-alert only |                                               N/A |
| **Text/Label (user-drawn)**      |                           **No** |                No |                                    Manual drawing-alert only |                                               N/A |
| **`hline` (script)**             | n/a (treat as your stored value) |    Yes (via code) |                             **Yes** (compose message string) |     **Yes** (`request.security()` for HTF values) |
| **`line.new` (script)**          |           **Yes** (`line.get_*`) |               Yes |                **Yes** (compose message; include custom tag) | **Yes** (values sourced via `request.security()`) |
| **`box.new` (script)**           |            **Yes** (`box.get_*`) |               Yes |               **Yes** (serialize TOP/BOT/LEFT/RIGHT + label) | **Yes** (values sourced via `request.security()`) |
| **`label.new` (script)**         |       **Yes** (`label.get_text`) |               Yes |                                       **Yes** (include text) |                          **Yes** (if you tag HTF) |

Official limitation for user-drawn objects highlighted above. ([TradingView][1])

---

## IV. Alert/Webhook Constraints Report

* **Trigger frequency limit:** Alert **stops** if it fires **>15 times in 3 minutes**. Use debouncing/aggregation; “Once per minute” can help. ([TradingView][14])
* **Retries / delivery:** On **HTTP 5xx**, TradingView **retries 3×** (≈5s cadence); total up to **4 sends** for one trigger. **No ordering guarantees**, so include sequence/nonce and design idempotency. ([TradingView][4])
* **Delays:** Integrators report **25–45s “normal” delays** sometimes; build tolerance and avoid chaining. (Vendor observation, not official SLA.) ([docs.traderspost.io][15])
* **Message size:** Pine string max **40,960 encoded chars** (Aug-2025). Keep messages compact; prefer **one alert per bar** with **batched lines**. ([TradingView][5])
* **Alert creation:** Alerts must be created from the **UI**; Pine code only creates **alert *events*** (`alertcondition`, `alert()`). ([TradingView][12])
* **Placeholders:** Standard placeholders (`{{ticker}}`, `{{exchange}}`, `{{close}}`, etc.). **No placeholder for a drawing’s user-entered text**. For indicators/strategies you can also use **plot/strategy** placeholders. ([TradingView][11])
* **Plan limits:** Active alert counts are plan-bound (e.g., Premium up to **800**, split by price/technical types). ([TradingView][16])

---

## V. Pattern Catalogue (with Pine v5 examples)

> Notes
> • Keep `alert()` calls **bar-scoped** and **debounced**; aggregate per-bar to avoid 15/3min cutoff.
> • Don’t call drawing functions inside `request.security()`; **compute HTF**, then **draw/export** in chart context. ([TradingView][7])

### A) Script-managed horizontal levels (single price) with tag

```pinescript
//@version=5
indicator("T800 Exporter — HLine", overlay=true, max_lines_count=500)

// Inputs
tf_export   = input.timeframe("", "HTF for value (blank = chart)")
lvl_price   = input.float(100000.0, "Level Price")
lvl_label   = input.string("1D:SELL", "Level Label")
emit_yaml   = input.bool(true, "Emit YAML alert")

// Manage hline via stored value
var float L = na
if barstate.isfirst
    L := lvl_price

// Draw (optional)
hline(L, "HLINE:"+lvl_label, color=color.new(color.red, 0))

// Build export line
float src = (tf_export == "") ? L : request.security(syminfo.tickerid, tf_export, L)
string row = str.format("TF={0};TYPE=LEVEL;LABEL={1};PRICE={2}", (tf_export==""? timeframe.period: tf_export), lvl_label, str.tostring(src, format.mintick))

// Batch & send once per bar close
var string batch = ""
if barstate.isconfirmed
    batch := row + "\n"
    if emit_yaml
        alert(batch, alert.freq_once_per_bar_close)  // webhook enabled in UI
```

### B) Zones modeled as `box.new` with TOP/BOT and tag

```pinescript
//@version=5
indicator("T800 Exporter — Zone", overlay=true, max_boxes_count=200)

tf_tag     = input.timeframe("240", "Zone TF tag")
top_in     = input.float(113200.0, "Zone Top")
bot_in     = input.float(111800.0, "Zone Bottom")
label_in   = input.string("4H:BUY", "Zone Label")
emit_yaml  = input.bool(true, "Emit YAML alert")

// Create/maintain a box spanning recent bars
var box z = na
if na(z)
    z := box.new(left=bar_index-100, top=top_in, right=bar_index, bottom=bot_in, border_color=color.new(color.teal,0), bgcolor=color.new(color.teal,85))
else
    box.set_right(z, bar_index) // extend

// Read values
float ztop = box.get_top(z)
float zbot = box.get_bottom(z)

// Serialize
string row = str.format("TF={0};TYPE=ZONE;LABEL={1};TOP={2};BOT={3}", tf_tag, label_in, str.tostring(ztop, format.mintick), str.tostring(zbot, format.mintick))

if barstate.isconfirmed and emit_yaml
    alert(row, alert.freq_once_per_bar_close)
```

### C) Lines with `line.get_price()` at the current bar (for sloped levels)

```pinescript
//@version=5
indicator("T800 Exporter — Sloped Line", overlay=true, max_lines_count=300)

L1_y = input.float(98000.0, "Point1 price")
L2_y = input.float(102000.0, "Point2 price")
tag  = input.string("1H:TREND", "Label")
emit = input.bool(true, "Emit alert")

var line ln = na
if na(ln)
    ln := line.new(bar_index-100, L1_y, bar_index, L2_y, extend=extend.right, color=color.orange)

// price of the sloped line at current bar
float y_now = line.get_price(ln, bar_index)
string row = str.format("TF={0};TYPE=SR;LABEL={1};PRICE={2}", timeframe.period, tag, str.tostring(y_now, format.mintick))

if barstate.isconfirmed and emit
    alert(row, alert.freq_once_per_bar_close)
```

### D) Multi-timeframe switches (mirror your `nmaq_exporter.pine` toggles)

```pinescript
//@version=5
indicator("T800 Exporter — MTF bundle", overlay=false)

use_1W = input.bool(true, "Export 1W")
use_1D = input.bool(true, "Export 1D")
use_4H = input.bool(true, "Export 4H")

float wk_hi = request.security(syminfo.tickerid, "1W", ta.highest(high, 1))
float d_poc = request.security(syminfo.tickerid, "1D", ta.vwma(close, volume)) // placeholder for “POC”
float h4_lo = request.security(syminfo.tickerid, "240", ta.lowest(low, 1))

var string out = ""
out := ""
if use_1W
    out += str.format("TF=1W;TYPE=LEVEL;LABEL=MAJOR;PRICE={0}\n", str.tostring(wk_hi, format.mintick))
if use_1D
    out += str.format("TF=1D;TYPE=POC;LABEL=1D:POC;PRICE={0}\n", str.tostring(d_poc, format.mintick))
if use_4H
    out += str.format("TF=4H;TYPE=LEVEL;LABEL=4H:LOW;PRICE={0}\n", str.tostring(h4_lo, format.mintick))

if barstate.isconfirmed and str.length(out) > 0
    alert(out, alert.freq_once_per_bar_close)
```

### E) Example standardized **drawing-tool** alert message (manual)

If a trader adds a **Horizontal Line** and creates a **drawing alert**, suggest a **manual** template:

```
SYMBOL={{exchange}}:{{ticker}}
TF={{interval}}
TYPE=LEVEL
LABEL=MANUAL:SR
PRICE={{close}}
NOTE=Copy line name: "<your label here>"
```

This uses standard placeholders; the line’s “Name/Text” **cannot** auto-populate. ([TradingView][11])

---

## VI. Labeling & Taxonomy Conventions

Adopt a strict, parse-friendly scheme:

* **Prefix with TF:** `1W:`, `1D:`, `4H:`, `1H:`; allow `ALL:` for cross-TF constants (e.g., ATH).
* **Category tokens:** `SELL`, `BUY`, `POC`, `SR`, `MAJOR`, `LOCAL`, `INACTIVE`.
* **Indexed labels:** `POC_1`, `POC_2` for multiple per TF.
* **Sanitization:** Uppercase A–Z, digits, `_` and `:` only; replace spaces with `_`.
* **Collision handling:** If duplicate `(TF, TYPE, LABEL)` seen in a bar, append `_#` counter in the payload.

Example payload lines (to transform into YAML):

```
TF=1D;TYPE=ZONE;LABEL=SELL;TOP=113200;BOT=111800
TF=1H;TYPE=LEVEL;LABEL=H_MAJOR;PRICE=111000
TF=ALL;TYPE=LEVEL;LABEL=ATH;PRICE=123456
```

---

## VII. Data Volume & Reliability Guidance

* **Batching:** Accumulate **all lines for the bar** and fire **one `alert()` per bar**. Keeps well under **15/3min** and preserves ordering at your ingress layer. ([TradingView][14])
* **Idempotency:** Add `TS={{time}}` or script-side `SEQ=<bar_index>`; your `tv_ingest` should **dedupe** by `(symbol, timeframe, seq)` because TradingView may retry on 5xx. ([TradingView][4])
* **Size budgeting:** Aim for ≤4 KB per message; if more, split by TF families (e.g., `HTF` vs `LTF`). Pine now allows larger strings, but smaller is safer operationally. ([TradingView][5])
* **Delays:** Design your pipeline to tolerate tens of seconds of delay and possible bursty retries. ([docs.traderspost.io][15])

---

## VIII. Compliance & Terms

* **Allowed:** Creating alerts in the UI; enabling **webhook** delivery; constructing messages with placeholders or `alert()` is within TV’s supported features. ([TradingView][8])
* **Not supported / avoid:** Any attempt to programmatically access **saved drawings** or UI object trees from Pine or scripts. ([TradingView][1])

---

## IX. Recommendation Brief

### Feasible Paths (ranked)

1. **Primary (Recommended): Script-managed registry**

   * Maintain levels/zones as **inputs** or **computed** values per TF. Draw with `hline/line/box`, tag with a strict label scheme, and **batch-export** via `alert()` once per bar.
   * **Pros:** Fully automatable; consistent labels; MTF parity; webhooks ready.
   * **Cons:** Traders must either enter values in inputs or rely on the script’s detection logic; manual drawings are out-of-band.

2. **Hybrid (Optional): Manual drawing alerts with standard template**

   * For ad-hoc levels, let traders create **drawing alerts** using a copy-paste template. Your backend parses standard placeholders but treats the **label** as manual free-text.
   * **Pros:** Works today for discretionary marks.
   * **Cons:** Error-prone (typos), no automatic capture of drawing’s “Name/Text”; not scalable.

3. **Table UI / checklist in Pine (Not viable for submission)**

   * Pine tables are **display-only**; they cannot “submit” to webhooks. Keep them for UX hints only. (No official source states tables can emit; they cannot.)
   * **Pros:** Nice UI. **Cons:** No output channel; still need alerts.

### Risks & Mitigations

| Risk                       | Impact             | Mitigation                                                                                                                       |
| -------------------------- | ------------------ | -------------------------------------------------------------------------------------------------------------------------------- |
| Alert stop (15/3min)       | Missed exports     | **Batch once per bar**; debounce intrabar alerts. ([TradingView][14])                                                            |
| Webhook retries/duplicates | Duplicate writes   | **Idempotent** `tv_ingest` with `(symbol, ts, seq)` keys; ignore duplicates. ([TradingView][4])                                  |
| Payload bloat              | Delivery/UI issues | Cap messages; split TF families; compress field names if needed. ([TradingView][5])                                              |
| Repaint (MTF)              | Wrong levels       | Use confirmed/offset series; avoid lookahead; compute in `request.security()` but draw/export in chart scope. ([TradingView][7]) |
| Manual workflow errors     | Wrong labels       | Enforce **strict label schema**; add input dropdowns; validate before export.                                                    |

---

## X. Backend Payload Examples → YAML

**Alert body (batched lines):**

```
SYMBOL={{exchange}}:{{ticker}}
TF_CHART={{interval}}
SEQ={{bar_index}}
TS={{time}}

TF=1D;TYPE=ZONE;LABEL=SELL;TOP=113200;BOT=111800
TF=1H;TYPE=LEVEL;LABEL=H_MAJOR;PRICE=111000
TF=ALL;TYPE=LEVEL;LABEL=ATH;PRICE=123456
```

(Placeholders populated by TradingView only for the header lines; the per-line export comes from `alert()`.) ([TradingView][11])

**Transformed YAML (server-side):**

```yaml
symbol: BINANCE:BTCUSDT
chart_tf: 1H
seq: 123456
ts: 2025-09-28T12:00:00Z
levels:
  1D:
    zones:
      - label: SELL
        top: 113200
        bottom: 111800
  1H:
    sr:
      - label: H_MAJOR
        price: 111000
  ALL:
    major:
      - label: ATH
        price: 123456
```

---

## XI. Secondary: Alternative UX Patterns (if user-drawn access is required)

* **Input-driven mapping:** Provide **input.float** fields per level and a **dropdown** for category; render matching objects visibly so traders see parity between script & chart.
* **“Pick-list + stamp” mode:** Supply a list of canonical labels (`1D:SELL`, `1H:H_MAJOR`, etc.) and “stamp” a script-managed object at cursor price via a **hotkey input** (approximate; Pine cannot read cursor but can respond to toggles).
* **Manual drawing alert template:** Pre-fill the message template for traders to paste; backend treats these as **ad-hoc** (non-canonical) entries.

---

## XII. Methodology & Sources

* **Primary docs** (Pine User/Reference Manuals, Help Center) for capabilities/limits. ([TradingView][1])
* **Community exemplars** to validate MTF + alerts patterns. ([TradingView][13])
* **Operational behavior** (delays, retries) cross-checked via vendor docs. ([docs.traderspost.io][15])

---

## XIII. Appendices

### A) Quick facts you can quote to stakeholders

* **No access to saved drawings** from Pine (hard limitation). ([TradingView][1])
* **≤40 unique `request.*()`** calls per script. ([TradingView][7])
* Alerts stop at **>15 triggers in 3 minutes**. ([TradingView][14])
* Pine strings max **40,960** chars as of Aug-2025 (practical ceiling for `alert()` messages). ([TradingView][5])
* **Webhook retries up to 3×** on 5xx (total 4 sends). ([TradingView][4])

---

## XIV. Conclusion

Exporting levels/zones + labels **is feasible today** when the script **owns the objects and labels**. Treat manual drawings as discretionary overlays (optional manual alerts) and move toward a **canonical, script-managed taxonomy** that your backend can parse deterministically.

---

## Clarifying questions (to finalize the engineering spike)

1. Do you want **manual drawings** to feed the system at all, or should we **standardize on script-managed** levels and offer only a manual fallback template?
2. For batching, would you prefer **one combined alert per bar** (all TFs) or **per-TF alerts** (e.g., HTF vs LTF) to keep payloads smaller?
3. Which **label taxonomy** do we lock in for v1 (e.g., `{TF}:{TYPE}_{index}`), and which fields are **mandatory** in the YAML (e.g., `LABEL`, `TYPE`, `TF`, `PRICE`/`TOP/BOT`)?

[1]: https://www.tradingview.com/pine-script-docs/visuals/lines-and-boxes/?utm_source=chatgpt.com "Visuals / Lines and boxes"
[2]: https://www.tradingview.com/pine-script-docs/v5/concepts/lines-and-boxes/?utm_source=chatgpt.com "Concepts / Lines and boxes"
[3]: https://www.tradingview.com/support/solutions/43000597494-alerts-on-alert-function/?utm_source=chatgpt.com "Alerts on alert() function"
[4]: https://www.tradingview.com/support/solutions/43000735201-webhook-resubmission/?utm_source=chatgpt.com "Webhook resubmission"
[5]: https://www.tradingview.com/pine-script-docs/release-notes/?utm_source=chatgpt.com "Release notes"
[6]: https://www.tradingview.com/support/solutions/43000595315-how-to-set-up-alerts/?utm_source=chatgpt.com "How to set up alerts"
[7]: https://www.tradingview.com/pine-script-docs/concepts/other-timeframes-and-data/?utm_source=chatgpt.com "Concepts / Other timeframes and data"
[8]: https://www.tradingview.com/support/solutions/43000529348-how-to-configure-webhook-alerts/?utm_source=chatgpt.com "How to configure webhook alerts"
[9]: https://www.tradingcode.net/tradingview/get-box-top-border/?utm_source=chatgpt.com "Get box top border with Pine Script"
[10]: https://www.tradingview.com/pine-script-docs/visuals/text-and-shapes/?utm_source=chatgpt.com "Visuals / Text and shapes"
[11]: https://www.tradingview.com/support/solutions/43000531021-how-to-use-a-variable-value-in-alert/?utm_source=chatgpt.com "How to use a variable value in alert"
[12]: https://www.tradingview.com/pine-script-docs/concepts/alerts/?utm_source=chatgpt.com "Concepts / Alerts"
[13]: https://www.tradingview.com/script/zdi9PMcW-Custom-Multi-Timeframe-Screener-with-Alerts/?utm_source=chatgpt.com "Custom Multi-Timeframe Screener with Alerts"
[14]: https://www.tradingview.com/support/solutions/43000690939-alert-was-triggered-too-often-and-stopped/?utm_source=chatgpt.com "Alert was triggered too often and stopped"
[15]: https://docs.traderspost.io/docs/learn/signal-sources/tradingview?utm_source=chatgpt.com "TradingView | Documentation - TradersPost"
[16]: https://www.tradingview.com/blog/en/more-alerts-for-each-plan-31701/?utm_source=chatgpt.com "It's doubled now: more alerts for each plan!"
