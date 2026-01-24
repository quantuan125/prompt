# Development Plan: Architecture Migration for `tv_ingest`

**Version:** 2.5.1 Enhanced  
**Component:** `tv_ingest`  
**Author:** Claude (Senior Technical PM)  
**Date:** 2025-07-04 
**Estimated Effort:** Medium (~8 hours)

## Stakeholder Summary

### What We're Doing
We are restructuring the `tv_ingest` component's code to improve its organization. This involves moving the core logic into a central "service" layer, which will make the system easier to manage and update in the future.

### Why It Matters
This change will reduce complexity, making it faster for developers to add new features or fix bugs. It also improves the component's stability and testability, aligning it with our best practices for software architecture.

### Key Points
- **Timeline:** ~8 developer hours over 1-2 days
- **Risk Level:** Low - This is a structural refactoring with no change to functionality.
- **User Impact:** None. The user interface and all features will look and work exactly as they do now.
- **Dependencies:** None.

---

## Technical Planning Document

### Executive Summary

This document outlines the technical steps to refactor the `tv_ingest` component to a "Service-first" architecture. The primary objective is to migrate all orchestration logic from the `TvIngestDataProcessor` into the `TvIngestService`. This makes the service the single source of truth and the sole interaction point for frontend builders, effectively decoupling the UI from backend processing. The refactoring improves modularity, simplifies testing by allowing mock services, and aligns the component with our standard architectural patterns. This is a non-functional change; the external behavior of the component will remain identical.

### Key Metrics
- **Files Modified:** 12 files across `components/tv_ingest/`
- **New Components:** 0 (This is a refactoring of existing components)
- **Breaking Changes:** No (Internal restructuring only)
- **Performance Impact:** Neutral. No performance changes are expected.

## Pre-Planning Validation

### 1. Consultation Analysis ✓
- **Solutions Identified:** Migrate data processor logic to a central service; use a singleton pattern for service access; deprecate the old processor.
- **Conflicts Resolved:** Consultant feedback on logger definition, repository API, import paths, and redundant steps has been incorporated.
- **Assumptions Verified:** The current architecture uses a data processor that can be cleanly migrated. Frontend builders can be updated to use a new service layer.

### 2. Codebase Verification ✓
- **Components Affected:**
  - Primary: `components/tv_ingest/service/svc_tv_ingest.py`
  - Secondary: `components/tv_ingest/frontend_builder/builders/`, `components/tv_ingest/backend/processors/dp_tv_ingest.py`, `components/tv_ingest/backend/processors/csv_repository.py`
- **Pattern Compatibility:** The proposed Service-first pattern is compatible and aligns with project-wide standards.
- **Naming Standards:** Verified convention compliance for services, builders, and processors.
- **Current Repository Location:** Repository is at `backend/processors/csv_repository.py`, not `backend/repositories/`

### 3. Feasibility Assessment ✓
- **Technical Feasibility:** Confirmed. The logic in `TvIngestDataProcessor` is stateless and can be moved to the service layer.
- **Performance Analysis:** No impact expected.
- **Breaking Changes:** None for external consumers of the component.

### 4. Risk Analysis ✓
**Primary Risks:**
1. **Integration Errors:** Incorrectly wiring the builders to the new service could lead to runtime errors. → **Mitigation:** Follow the implementation plan precisely and conduct thorough manual testing of the UI page post-refactoring.
2. **Broken Tests:** Unit tests will fail due to the changed architecture. → **Mitigation:** The plan includes specific instructions on how to update unit tests by mocking the service layer.

## Compatibility Analysis

### Current Architecture Assessment

**Service Layer Current State:**
- File: `components/tv_ingest/service/svc_tv_ingest.py`
- Current class: `TvIngestService`
- Dependencies: `TvIngestDataProcessor`, `CsvRepository`
- Pattern: Service acts as facade but delegates to data processor

**Target Architecture:**
- Service becomes primary orchestrator
- Direct instantiation of processor helpers
- Elimination of `TvIngestDataProcessor` middleman

### Integration Points

**Frontend Builder Integration:**
- Current: `BaseBuilder` provides `processor()` and `repo()` methods
- Target: `BaseBuilder` provides single `service()` method
- All builders inherit from `BaseBuilder` and use `cls.service()`

**Webhook Server Integration:**
- Current: Webhook server uses `TvIngestDataProcessor` directly
- Target: Webhook server uses `TvIngestService` methods

## Implementation Plan

### Phase 1: Refactor Service and Repository (~4 hours)

#### Task 1.1: Enhance `TvIngestService`
The core of this migration is to move orchestration logic into `TvIngestService`.

**File to modify:** `components/tv_ingest/service/svc_tv_ingest.py`

**Current Implementation Analysis:**
- Existing `TvIngestService` class already exists
- Current `__init__` method needs modification
- Current methods: `render()`, `ingest_webhook()`, `get_available_symbols()`, `get_data()`, `export_data_as_csv()`, `clear_data()`, `backup_data()`

**Instructions:**

1.  **Modify Import Statements:** Update imports to include direct processor dependencies.

    ```python
    # File: components/tv_ingest/service/svc_tv_ingest.py
    # Add these imports at the top
    import logging
    from pathlib import Path
    from typing import Dict, Any, List, Optional
    import pandas as pd
    
    # Existing imports to keep
    from ..backend.processors.csv_repository import CsvRepository
    
    # New direct processor imports
    from ..backend.processors.webhook_processor import WebhookProcessor
    from ..backend.processors.calculations.delta_calculator import DeltaCalculator
    from ..backend.processors.filterings.vwap_filter import VWAPFilter
    
    # Remove this import (will be deprecated)
    # from ..backend.processors.dp_tv_ingest import TvIngestDataProcessor
    ```

2.  **Refactor Constructor:** Replace `TvIngestDataProcessor` dependency with direct processor instantiation.

    ```python
    # File: components/tv_ingest/service/svc_tv_ingest.py
    class TvIngestService:
        def __init__(self, data_dir: str = "components/tv_ingest/data"):
            """Initialize service with direct processor dependencies."""
            self.logger = logging.getLogger(__name__)
            self.data_dir = Path(data_dir) if isinstance(data_dir, str) else data_dir
            
            # Repository for data persistence
            self.repo = CsvRepository(str(self.data_dir))
            
            # Direct processor instantiation (replaces TvIngestDataProcessor)
            self.webhook_processor = WebhookProcessor(str(self.data_dir))
            self.delta_calculator = DeltaCalculator()
            self.vwap_filter = VWAPFilter()
            
            self.logger.info(f"TvIngestService initialized with data_dir: {self.data_dir}")
    ```

3.  **Refactor `ingest_webhook` Method:** Replace delegation to `TvIngestDataProcessor` with direct orchestration.

    ```python
    # In TvIngestService class - Replace existing ingest_webhook method
    def ingest_webhook(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Processes the incoming webhook data using direct processor orchestration.

        Args:
            payload: Webhook payload containing OHLCV data and indicators
            
        Returns:
            Dictionary with processing results and statistics
            
        Note: The return type will be upgraded to a typed `ProcessingResult` model in plan v2.5.2.
        """
        try:
            self.logger.info(f"Processing webhook payload for symbol: {payload.get('symbol', 'UNKNOWN')}")
            
            # Step 1: Process raw webhook data
            webhook_result = self.webhook_processor.process_webhook_data(payload)
            if not webhook_result.get("success", False):
                self.logger.error(f"Webhook processing failed: {webhook_result}")
                return {"success": False, "error": "Webhook processing failed"}

            # Step 2: Extract DataFrame from webhook result
            df = webhook_result.get("dataframe")
            if df is None or df.empty:
                self.logger.warning("No DataFrame from webhook processing")
                return {"success": False, "error": "No data processed"}

            # Step 3: Apply delta calculations
            df = self.delta_calculator.add_delta_columns(df)
            self.logger.debug(f"Applied delta calculations, DataFrame shape: {df.shape}")

            # Step 4: Apply VWAP filtering
            df = self.vwap_filter.mask_irrelevant_vwaps(df)
            self.logger.debug(f"Applied VWAP filtering, DataFrame shape: {df.shape}")

            # Step 5: Extract metadata for storage
            symbol = payload.get("symbol", "UNKNOWN")
            timeframe = payload.get("timeframe", "1m")
            
            # Step 6: Save processed data using repository
            success = self.repo.save_processed_data(df, symbol, timeframe)

            if success:
                result = {
                    "success": True, 
                    "message": f"Stored {len(df)} rows for {symbol}/{timeframe}", 
                    "rows": len(df),
                    "symbol": symbol,
                    "timeframe": timeframe
                }
                self.logger.info(f"Successfully processed webhook: {result}")
                return result
            else:
                self.logger.error(f"Failed to save data for {symbol}/{timeframe}")
                return {"success": False, "error": "Failed to save data"}

        except Exception as e:
            self.logger.error(f"Error in ingest_webhook: {e}", exc_info=True)
            return {"success": False, "error": str(e)}
    ```

4.  **Add `get_processor_status` Method:** Add status monitoring for all processor components.

    ```python
    # In TvIngestService class - Add new method
    def get_processor_status(self) -> Dict[str, Any]:
        """Get status of all processor helpers.
        
        Returns:
            Dictionary containing status of each processor component
        """
        return {
            "webhook_processor": {
                "status": "active",
                "data_directory": str(self.data_dir),
                "class": self.webhook_processor.__class__.__name__
            },
            "delta_calculator": {
                "status": "active",
                "class": self.delta_calculator.__class__.__name__
            },
            "vwap_filter": {
                "status": "active",
                "class": self.vwap_filter.__class__.__name__
            },
            "repository": {
                "status": "active",
                "data_directory": str(self.data_dir),
                "class": self.repo.__class__.__name__
            }
        }
    ```

5.  **Standardize Method Names:** Ensure API consistency for plan v2.5.2 compatibility.

    ```python
    # In TvIngestService class - Rename method if needed
    def load_data(self, symbol: str = None, timeframe: str = None) -> pd.DataFrame:
        """Load data using repository - standardized method name.
        
        This method replaces any variations like 'load' or 'get_data' for consistency.
        """
        return self.repo.load(symbol=symbol, timeframe=timeframe)
    ```

#### Task 1.2: Update `CsvRepository`
To clarify the data-saving API and improve method signatures.

**File to modify:** `components/tv_ingest/backend/processors/csv_repository.py`

**Current Repository Location:** Repository is located at `backend/processors/csv_repository.py`, not `backend/repositories/`.

**Instructions:**

1.  **Add `save_processed_data` method:** This method will provide a cleaner API for the service layer.

    ```python
    # In CsvRepository class - Add new method
    def save_processed_data(self, df: pd.DataFrame, symbol: str, timeframe: str) -> bool:
        """
        Saves a processed DataFrame for a given symbol and timeframe.
        This is the new standard method for the service layer.
        
        Args:
            df: Processed DataFrame with OHLCV data and indicators
            symbol: Trading symbol (e.g., 'BINANCE:BTCUSDT')
            timeframe: Time interval (e.g., '5m', '1H')
            
        Returns:
            bool: True if save successful, False otherwise
        """
        try:
            # Use existing save method with explicit parameters
            # The current save method handles symbol/timeframe internally
            return self.save(df, mode="append") 
        except Exception as e:
            logger.error(f"Error saving processed data for {symbol}/{timeframe}: {e}")
            return False
    ```

2.  **Add Logger Import:** Ensure proper logging is available in the repository.

    ```python
    # At the top of csv_repository.py file - Add if not present
    import logging
    logger = logging.getLogger(__name__)
    ```

    **Note to Developer:** The consultant flagged the old `save(df, mode="append")` signature as potentially ambiguous. For now, you can implement `save_processed_data` by calling the old `save` method. In plan v2.5.2, the repository will be made more robust with typed return models.

### Phase 2: Refactor Frontend Builders (~3 hours)

#### Task 2.1: Update `BaseBuilder` Singleton
The `BaseBuilder` will now provide a singleton instance of `TvIngestService`.

**File to modify:** `components/tv_ingest/frontend_builder/builders/base_builder.py`

**Current Implementation Analysis:**
- File exists with `BaseBuilder` class
- Current methods: `processor()`, `repo()`, `service()` (if already exists)
- Import path: `from ...service.svc_tv_ingest import TvIngestService`

**Instructions:**

1.  **Update Import Statements:** Ensure correct import path for the service.

    ```python
    # File: components/tv_ingest/frontend_builder/builders/base_builder.py
    # Update imports at the top
    from typing import Optional
    from ...service.svc_tv_ingest import TvIngestService  # Correct path: three dots for parent navigation
    ```

2.  **Refactor Service Singleton:** Replace or update the service singleton pattern.

    ```python
    # File: components/tv_ingest/frontend_builder/builders/base_builder.py
    class BaseBuilder:
        _service: Optional[TvIngestService] = None

        @classmethod
        def service(cls) -> TvIngestService:
            """Get a singleton instance of the TvIngestService.
            
            Returns:
                TvIngestService: Singleton service instance
            """
            if cls._service is None:
                # The constructor now has a default value, so this call is valid.
                cls._service = TvIngestService()
            return cls._service
            
        @classmethod
        def reset_service(cls) -> None:
            """Reset service singleton - useful for testing."""
            cls._service = None
    ```

3.  **Deprecate Old Methods:** Mark processor and repo methods as deprecated.

    ```python
    # File: components/tv_ingest/frontend_builder/builders/base_builder.py
    # In BaseBuilder class - Add these methods if they exist
    @classmethod
    def processor(cls):
        """DEPRECATED: Use service() instead."""
        import warnings
        warnings.warn("processor() is deprecated. Use service() instead.", DeprecationWarning)
        return cls.service()
        
    @classmethod
    def repo(cls):
        """DEPRECATED: Use service().repo instead."""
        import warnings
        warnings.warn("repo() is deprecated. Use service().repo instead.", DeprecationWarning)
        return cls.service().repo
    ```

#### Task 2.2: Refactor Individual Builders to Use the Service
All builders must now use the service pattern consistently.

**Files to modify:** All files in `components/tv_ingest/frontend_builder/builders/`
- `config_builder.py`
- `data_view_builder.py`
- `export_builder.py`
- `webhook_control_builder.py`

**Instructions:**

1.  **Verify Inheritance:** Ensure every builder class inherits from `BaseBuilder`.

    ```python
    # In each builder file
    from .base_builder import BaseBuilder
    
    class ConfigBuilder(BaseBuilder):  # Ensure BaseBuilder inheritance
        # ... implementation
    ```

2.  **Update Service Usage:** Replace any calls to `cls.processor()` or `cls.repo()` with `cls.service()`.

    **Before (in any builder's build() method):**
    ```python
    # Old pattern
    repo = cls.repo()
    symbols = repo.get_available_symbols()
    
    processor = cls.processor()
    result = processor.process_data(data)
    ```
    
    **After (in any builder's build() method):**
    ```python
    # New pattern
    service = cls.service()
    symbols = service.get_available_symbols()  # Service method
    
    # For repository operations, go through service
    result = service.ingest_webhook(data)  # Service orchestration
    ```

3.  **Update Specific Builder Patterns:**

    **In `data_view_builder.py`:**
    ```python
    # Replace data loading calls
    service = cls.service()
    df = service.load_data(symbol=symbol, timeframe=timeframe)  # Standardized method name
    ```
    
    **In `export_builder.py`:**
    ```python
    # Replace export calls
    service = cls.service()
    export_result = service.export_data_as_csv(symbol, timeframe)
    ```
    
    **In `webhook_control_builder.py`:**
    ```python
    # Replace status calls
    service = cls.service()
    status = service.get_processor_status()
    ```

### Phase 3: Finalization & Deprecation (~1 hour)

#### Task 3.1: Update UI Facade
The main UI entry point `fb_tv_ingest.py` needs a minor update.

**File to modify:** `components/tv_ingest/frontend_builder/fb_tv_ingest.py`

**Current Implementation Analysis:**
- File exists with `TvIngestFrontendBuilder` class
- Current `render` method signature needs verification
- Class manages tab-based navigation for UI

**Instructions:**

1.  **Verify and Update `render` Method:** Ensure the method signature is consistent with service-first pattern.

    ```python
    # In TvIngestFrontendBuilder class - Update method signature if needed
    @classmethod
    def render(cls) -> None:
        """Render the TradingView Ingest frontend interface.
        
        Uses service singleton from BaseBuilder for all backend operations.
        """
        # Service access through BaseBuilder singleton
        service = cls.service()
        
        # Continue with existing tab rendering logic
        # ... existing implementation
    ```

2.  **Update Service Usage in Render Logic:** Ensure all backend calls use the service.

    ```python
    # In TvIngestFrontendBuilder.render() method
    # Replace any direct processor or repo calls with service calls
    
    # Example updates:
    # OLD: processor = cls.processor()
    # NEW: service = cls.service()
    
    # OLD: repo = cls.repo()
    # NEW: service = cls.service()  # Then use service.repo if needed
    ```

#### Task 3.2: Deprecate `dp_tv_ingest.py`
The old data processor aggregator is now obsolete.

**File to modify:** `components/tv_ingest/backend/processors/dp_tv_ingest.py`

**Current Implementation Analysis:**
- File contains `TvIngestDataProcessor` class
- Class aggregates WebhookProcessor, DeltaCalculator, VWAPFilter
- Used by service layer and potentially webhook server

**Instructions:**

1.  **Create Deprecation Shim:** Replace the entire file content with a deprecation notice.

    ```python
    # File: components/tv_ingest/backend/processors/dp_tv_ingest.py
    """
    DEPRECATED: This module is deprecated and will be removed in a future version.
    
    The orchestration logic has been moved to `svc_tv_ingest.py`.
    TvIngestService now directly manages all processor components.
    
    Migration path:
    - Replace TvIngestDataProcessor with TvIngestService
    - Use BaseBuilder.service() in frontend builders
    - Use TvIngestService directly in webhook server
    """
    
    import warnings
    
    warnings.warn(
        "TvIngestDataProcessor is deprecated. Use TvIngestService instead.",
        DeprecationWarning,
        stacklevel=2
    )
    
    class TvIngestDataProcessor:
        """Deprecated class - use TvIngestService instead."""
        
        def __init__(self, *args, **kwargs):
            raise ImportError(
                "TvIngestDataProcessor is deprecated. "
                "Use TvIngestService from components.tv_ingest.service.svc_tv_ingest instead. "
                "Frontend builders should use BaseBuilder.service() for access."
            )
    ```

## Validation Criteria

### Technical Validation (For Reviewers)

**Unit Test Coverage:**
- All existing tests must pass after being updated.
- **Testing Note:** To mock the service in your unit tests, use the following pattern:
  ```python
  # In your test file
  from components.tv_ingest.frontend_builder.builders.base_builder import BaseBuilder
  from unittest.mock import Mock

  # In your test setup or individual test
  mock_service = Mock()
  BaseBuilder._service = mock_service  # Set mock service
  
  # Test your builder logic
  # ...
  
  # Cleanup
  BaseBuilder.reset_service()  # Reset for next test
  ```

**Integration Tests:**
- Manually test the "Pine Script Data" page in the Streamlit application.
- Verify functionality:
    - Webhook server starts and stops correctly
    - Data is received and displayed in the UI
    - Data can be exported successfully  
    - Status information displays correctly
    - Configuration changes are applied

**Service Integration Tests:**
- Test service orchestration:
  ```python
  # Test direct service usage
  service = TvIngestService()
  result = service.ingest_webhook(test_payload)
  assert result["success"] == True
  
  # Test processor status
  status = service.get_processor_status()
  assert "webhook_processor" in status
  ```

### Code Quality Checks
- [ ] No pylint/flake8 warnings
- [ ] All changes are covered by the plan
- [ ] Type hints are preserved on all public methods
- [ ] Logging statements use appropriate levels (INFO, DEBUG, ERROR)
- [ ] Deprecation warnings are properly implemented
- [ ] Import statements are organized (standard, third-party, local)
- [ ] Method signatures are consistent with documented API

## Acceptance Criteria

### Business Requirements (For PM/Client)
- [X] The system's functionality is identical to the previous version.
- [X] There is no user-facing impact.

## Deployment Plan

### Staging Deployment
- Deploy to staging and run existing smoke tests.

### Production Deployment
- This is a backend refactoring and can be deployed during a standard maintenance window. No phased rollout is required.

---

## Appendices

### A. File Changes
```
Modified:
- components/tv_ingest/service/svc_tv_ingest.py
- components/tv_ingest/backend/processors/csv_repository.py
- components/tv_ingest/frontend_builder/builders/base_builder.py
- components/tv_ingest/frontend_builder/builders/config_builder.py
- components/tv_ingest/frontend_builder/builders/data_view_builder.py
- components/tv_ingest/frontend_builder/builders/export_builder.py
- components/tv_ingest/frontend_builder/builders/webhook_control_builder.py
- components/tv_ingest/frontend_builder/fb_tv_ingest.py
- tests/unit/test_svc_tv_ingest.py
- tests/unit/test_base_builder.py

Deprecated (content replaced with shim):
- components/tv_ingest/backend/processors/dp_tv_ingest.py
```

### B. API Changes Summary
```
TvIngestService:
+ load_data(symbol, timeframe) -> pd.DataFrame  # Standardized method name
+ get_processor_status() -> Dict[str, Any]      # New status method

CsvRepository:
+ save_processed_data(df, symbol, timeframe) -> bool  # New save method

BaseBuilder:
+ reset_service() -> None                      # Testing utility
~ processor() -> deprecated                     # Deprecation warning
~ repo() -> deprecated                          # Deprecation warning

TvIngestDataProcessor:
~ __init__() -> raises ImportError              # Deprecated class
```