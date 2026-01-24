## 3. CONTEXT ANALYSIS 

### OVERVIEW
Produce a concise, decision-ready context that sets directional bias, posture, risk, and invalidation for the current session by synthesizing three lenses: Trader, Macro, and Technical. The outcome gates TSI (execution) and informs position sizing and tolerance.

### TRIGGER CONDITIONS
- When the user asks for market context or bias for the session.
- Before any TSI-driven execution decision or plan selection.
- At session start, after major news/prints, or upon a significant level interaction.

### EXECUTION PROTOCOL
- Trader Context: Derived from "Trader Context" section. This include: Session timing window, proximity to scheduled catalysts, venue/liquidity conditions, public sentiment and trader-side execution constraints/psychology (window open/closed, allowed setup grades, size throttle, timebox).
- Macro Context: Derived from "Macro Context" section. Near-term catalysts (events/speakers/flows), base impulse, sensitivities.
- Technical Context: Derived from "Technical Context" section. Multi-timeframe trend (1D/4H/1H/15m), key level interaction, structure/VPA.
- Synthesis: Resolve conflicts; declare Bias, Posture, Risk, Confidence, and a clear Invalidation.

### REQUIRED FORMAT
```
[CONTEXT ANALYSIS]
Trader Context: [1–3 sentences: timing window + event countdowns + execution constraints (+ psychology only if risk-relevant)]
Macro Context: [1–3 sentences: drivers + event/flow sensitivity]
Technical Context: [1–3 sentences: MTF trend + key level interaction + structure/VPA]
Aggregate: Bias=[Bearish/Neutral/Bullish], Posture=[With-trend/Counter-trend/Mean-Reversion], Risk=[Low/Medium/High], Confidence=[1–5], Invalidation=[condition that flips/neutralizes]
```

### EXAMPLE
- Trader Context: We are in a historically weak month (September) and have just experienced a major long liquidation event. Price has found initial support at a key daily demand zone (`1D_BUY_1`). Liquidity elevated post long liquidation and a counter-trend bounce is underway in the US session in 2 hours with high impact event of FOMC in 6 hours. Trader psychology stable (no additional constraints).
- Macro Context: The recent Fed rate cut provides a tailwind for risk assets, but this week's PMIs and Core PCE data will be critical in validating that dovish stance. A hawkish surprise in the data or Fedspeak could renew pressure. Near-term, ETF flows and CME futures expiry are key liquidity drivers. The macro bias is cautiously risk-on, but sensitive to incoming data.
- Technical Context: The multi-timeframe picture is clear: a strong bearish trend on the 1D, 4H, and 1H timeframes has collided with a significant 1D demand level (`112.2k`). This has triggered a classic counter-trend bounce on the 15m. The dominant structure is bearish, making short setups with-trend and long setups counter-trend. The key question is whether this bounce is a simple low-volume relief rally before the next leg down, or the start of a more significant reversal.
- Aggregate: Bias=Bearish, Posture=With-trend, Risk=Medium, Confidence=3, Invalidation=Acceptance above [HTF pivot] with rising volume and a TTF market-structure shift.

