# TradingView Custom Symbol Payload Handling – TDD Implementation Plan (Backend Only)

## 1. Situation Summary
- Problem: TradingView custom pair payloads (e.g., `BINANCE:LINKUSDT/BINANCE:AAVEUSDT`) sometimes arrive embedded in a non-standard, JSON-like wrapper (often starting with `=` and using underscores instead of colons) and are passed unmodified into directory creation. This produces invalid Windows paths and raises `WinError 123` during storage.
- Root cause: The `symbol` value flows into `_ensure_symbol_directory` without normalization. Current `sanitize_symbol_for_filename` only replaces `:`, `/`, and `\`, but the raw string may still contain `{`, `}`, quotes, commas, and `=`.
- Scope: Focus only on parsing and safely storing custom symbols in the backend ingestion pipeline. Do not change or depend on Delta or VWAP processing.

Relevant error excerpt (trimmed to the custom symbol issue):
```
INFO:components.tv_ingest.backend.api.webhook_server:Received base 19-column format, will add enhancements
INFO:components.tv_ingest.backend.processors.webhook_processor:Starting webhook data processing: 3 rows, mode: override
ERROR:components.tv_ingest.backend.processors.webhook_processor:Error in webhook data processing: [WinError 123] The filename, directory name, or volume label syntax is incorrect: 'components\tv_ingest\data\={"adjustment"_"splits","symbol"_"BINANCE_LINKUSDT_BINANCE_AAVEUSDT"}'
ERROR:components.tv_ingest.backend.processors.webhook_processor:Traceback: ... in _ensure_symbol_directory
ERROR:components.tv_ingest.backend.api.webhook_server:Data processing failed: [WinError 123] The filename, directory name, or volume label syntax is incorrect: 'components\tv_ingest\data\={"adjustment"_"splits","symbol"_"BINANCE_LINKUSDT_BINANCE_AAVEUSDT"}'
```

## 2. Desired Outcomes
1. Parsing: Extract a clean TradingView symbol from wrapper strings so `BINANCE:LINKUSDT/BINANCE:AAVEUSDT` is recovered.
2. Sanitization: Convert the parsed symbol to a Windows-safe directory name (e.g., `BINANCE_LINKUSDT_BINANCE_AAVEUSDT`).
3. Backward compatibility: Standard symbols (e.g., `BINANCE:BTCUSDT`) keep existing behavior and sanitize to `BINANCE_BTCUSDT`.
4. Confidence: New pytest suite under `tests/components/tv_ingest` drives and guards behavior (Red → Green → Refactor).

## 3. Preparation & References
- Documentation: `documentation/testing/tdd/tdd_onboarding_guide.md` (follow Red → Green → Refactor).
- Test style: mirror conventions from `tests/prompt` (fixtures, markers, naming).
- Code references:
  - `components/tv_ingest/utils/helpers.py` (existing `TV_Ingest_Helpers`, `sanitize_symbol_for_filename`).
  - `components/tv_ingest/backend/processors/webhook_processor.py` (directory creation in `_ensure_symbol_directory`).
- Environment: Use project venv; run tests with `pytest` (see `pytest.ini`).

## 4. High‑Level TDD Roadmap
Execute stages in order. Each stage follows Red → Green → Refactor.

### Stage 0 – Test Harness Setup (Red)
1. Create test package:
   - `tests/components/tv_ingest/__init__.py` (empty)
   - `tests/components/tv_ingest/unit/__init__.py` (empty)
   - Optional shared config: `tests/components/tv_ingest/conftest.py` (can be empty initially)
2. Verify discovery: `pytest tests/components/tv_ingest -k nothing` should report “collected 0 items”.

### Stage 1 – Symbol Parsing Helper (Red → Green → Refactor)
Goal: From raw wrapper strings (e.g., `={"adjustment"_"splits","symbol"_"BINANCE:LINKUSDT/BINANCE:AAVEUSDT"}`) extract the inner symbol.

1) Write failing tests (Red):
- Add `tests/components/tv_ingest/unit/test_symbol_parsing.py` (mark as unit via `pytestmark = pytest.mark.unit`). Cover:
  - Plain symbol: `BINANCE:BTCUSDT` → unchanged.
  - JSON-like wrapper with leading equals and underscore separators: `={"adjustment"_"splits","symbol"_"BINANCE:LINKUSDT/BINANCE:AAVEUSDT"}` → returns `BINANCE:LINKUSDT/BINANCE:AAVEUSDT`.
  - JSON string with braces/quotes: `{"symbol":"BINANCE:LINKUSDT"}` → `BINANCE:LINKUSDT`.
  - Whitespace/noise tolerance: trims surrounding spaces.
  - Malformed/no symbol key: falls back to trimmed original.
- Expect function as a static method on `TV_Ingest_Helpers`: `parse_tradingview_symbol(raw_symbol: str) -> str`.
- Run the single test module → RED (function missing).

2) Implement minimal code (Green):
- Add `@staticmethod TV_Ingest_Helpers.parse_tradingview_symbol(raw_symbol: str) -> str` in `components/tv_ingest/utils/helpers.py` next to existing helpers. Implementation guidance for novices:
  - If `raw_symbol` is falsy: return `""`.
  - `s = raw_symbol.strip()`; if `s.startswith('=')`, strip the leading `=` and whitespace.
  - Try `json.loads(s)` if it looks like JSON (starts with `{` and contains `"symbol"`). If success and `symbol` in obj: return `obj['symbol'].strip()`.
  - If not valid JSON: regex search for `"symbol"\s*[:_]\s*"([^"]+?)"` and return the first capture if found.
  - Else return `s`.
- Re‑run tests → GREEN.

3) Refactor:
- Ensure docstring + type hints; keep logic small and defensive.

### Stage 2 – Filename Sanitization Hardening (Red → Green → Refactor)
Goal: Guarantee Windows‑safe directory names after parsing.

1) Add tests (Red):
- Create `tests/components/tv_ingest/unit/test_symbol_sanitization.py` with parameterized cases using `TV_Ingest_Helpers.sanitize_symbol_for_filename` and the full chain via a new normalizer (see Stage 3):
  - `BINANCE:BTCUSDT` → `BINANCE_BTCUSDT` (backward compatibility).
  - Parsed custom pair → `BINANCE_LINKUSDT_BINANCE_AAVEUSDT`.
  - Strings containing Windows‑invalid chars `< > : " / \ | ? *` are converted to safe characters (underscores) and multiple underscores collapse to one.
- Run tests → RED (current sanitizer only replaces `:`, `/`, `\`).

2) Update production code (Green):
- Strengthen `TV_Ingest_Helpers.sanitize_symbol_for_filename`:
  - Replace any character not in `[A-Za-z0-9._-]` with `_`.
  - Collapse repeated `_` and strip leading/trailing `_`.
- Re‑run tests → GREEN.

3) Refactor:
- Keep the rule centralized and documented; avoid overfitting to one payload.

### Stage 3 – Ingestion Integration (Red → Green → Refactor)
Goal: Use parsing + sanitization before filesystem access, without involving other processing (Delta/VWAP).

1) Write failing test (Red):
- Add `tests/components/tv_ingest/unit/test_webhook_processor_symbol_handling.py` (unit mark). Use `tmp_path` to avoid real filesystem writes.
- Construct `WebhookProcessor(data_dir=str(tmp_path))`.
- Call its private `_ensure_symbol_directory(raw_symbol)` directly with the failing example `={"adjustment"_"splits","symbol"_"BINANCE_LINKUSDT_BINANCE_AAVEUSDT"}` and with a spread like `={"adjustment"_"splits","symbol"_"BINANCE:LINKUSDT/BINANCE:AAVEUSDT"}`.
- Assert the directory exists and its name equals the sanitized version (`BINANCE_LINKUSDT_BINANCE_AAVEUSDT`). Ensure no exception is raised. Do not call `process_webhook_data` to avoid unrelated concerns.
- Run tests → RED (uses raw symbol today).

2) Implement minimal integration (Green):
- Add a new static helper: `TV_Ingest_Helpers.normalize_symbol_for_storage(raw_symbol: str) -> str` that does: `parsed = parse_tradingview_symbol(raw_symbol)` then `return sanitize_symbol_for_filename(parsed)`.
- Update `TV_Ingest_Helpers.get_symbol_directory(symbol)` to delegate to `normalize_symbol_for_storage(symbol)` so all callers (including `_ensure_symbol_directory`) benefit.
- Alternatively (if preferred), update `_ensure_symbol_directory` to call the normalizer explicitly. Consistency is key; prefer centralizing in `get_symbol_directory`.
- Re‑run tests → GREEN.

3) Refactor & safety notes:
- Keep grouping keys (`df['symbol']`) unchanged to avoid broader behavior shifts; normalization is used only for filesystem paths.
- Log both raw and normalized symbol at directory creation if useful for debugging (optional).

### Stage 4 – Regression & Acceptance
1. Run `pytest -q` or `pytest -m unit` to ensure all new tests pass and nothing else regresses.
2. Optional manual check: start the ingest flow and simulate a POST with a custom pair payload; confirm directories are created under the configured `data_dir` without errors.

## 5. Risks & Mitigations
- Malformed payloads: Parser must never raise; always fallback to trimmed original string.
- Cross‑platform safety: Sanitizer excludes Windows‑invalid characters and non‑alphanumerics; tests cover the set `< > : " / \ | ? *`.
- Reversibility limits: The status endpoint currently reconstructs symbols by replacing `_` with `:`, which is lossy. This task does not change UI; document limitation. A follow‑up could persist original symbol in `meta.json` per directory.

## 6. Deliverables & File Touchpoints
- Tests under `tests/components/tv_ingest`:
  - `unit/test_symbol_parsing.py`
  - `unit/test_symbol_sanitization.py`
  - `unit/test_webhook_processor_symbol_handling.py`
- Helper updates in `components/tv_ingest/utils/helpers.py`:
  - Add `parse_tradingview_symbol` and `normalize_symbol_for_storage` as `@staticmethod`s on `TV_Ingest_Helpers`.
  - Harden `sanitize_symbol_for_filename` per Stage 2.
- Processor uses normalized directory names via `get_symbol_directory` or direct normalizer call in `_ensure_symbol_directory`.
- All tests green via project `pytest` command.

—
Follow Red → Green → Refactor strictly. Commit after each Green/Refactor cycle per repository guidelines.

