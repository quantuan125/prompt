# Development Plan: Refactor `svc_tv_ingest.py` and Introduce Data Models

**Version:** 1.1.0
**Component:** `tv_ingest`
**Author:** Gemini (Technical Program Manager)

## 1. Objective

This plan outlines a two-part initiative to significantly improve the `tv_ingest` component, bringing it in line with the project's "gold standard" architecture.

1.  **Introduce Data Models:** Replace raw dictionaries and untyped data structures with strongly-typed `dataclass` models. This will enhance type safety, serve as living documentation, and improve maintainability.
2.  **Refactor Service Layer:** Refactor the `TvIngestService` into a lean orchestrator that focuses exclusively on high-level business logic, delegating data access and processing tasks to the appropriate components.

The successful execution of this plan will result in a more robust, testable, and architecturally consistent component.

## 2. Implementation Plan

### Part 1: Introduce Core Data Models

The foundational step is to establish a set of structured, typed data models for all data flowing through the `tv_ingest` component.

**Task 1.1: Create `models_tv_ingest.py`**

A new file will be created to house all the data models, ensuring a single source of truth for the component's data structures.

-   **Action:** Create the file `components/tv_ingest/models/models_tv_ingest.py`.
-   **Content:** Populate the new file with the following dataclasses.

```python
"""
Data models for TradingView Ingest component.
Provides structured data classes for type safety and clarity.
"""
from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Dict, Any, Optional, Union, Tuple
from pathlib import Path
import pandas as pd
from enum import Enum


# Enums for controlled values
class TimeFrame(str, Enum):
    """Supported timeframes."""
    M1 = "1m"
    M3 = "3m"
    M5 = "5m"
    M15 = "15m"
    M30 = "30m"
    H1 = "1H"
    H4 = "4H"
    D1 = "1D"
    W1 = "1W"
    MN1 = "1M"


class StorageMode(str, Enum):
    """Data storage modes."""
    OVERRIDE = "override"
    APPEND = "append"


class PriceSelection(str, Enum):
    """Price selection methods."""
    MANUAL = "Manual"
    STOP_LOSS = "Stop Loss"
    TAKE_PROFIT = "Take Profit"


# Webhook-related models
@dataclass
class RawWebhookData:
    """Raw data received from TradingView webhook."""
    symbol: str
    time: datetime
    open: float
    high: float
    low: float
    close: float
    volume: float
    vol_ma20: float
    vol_ma30: float
    ema9: float
    ema21: float
    ema50: float
    ema200: float
    sma200: float
    rsi: float
    rsi_ma14: float
    vwap_session: Optional[float]
    vwap_week: Optional[float]
    vwap_month: Optional[float]
    tf: str  # Raw timeframe code
    
    @property
    def timeframe(self) -> TimeFrame:
        """Convert raw tf to TimeFrame enum."""
        from ..utils.constant import TF_MAPPING
        mapped = TF_MAPPING.get(self.tf, self.tf)
        return TimeFrame(mapped)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for DataFrame operations."""
        return {k: v for k, v in self.__dict__.items() if not k.startswith('_')}


@dataclass
class EnhancedData:
    """Data enhanced with delta calculations."""
    raw_data: RawWebhookData
    # Price vs EMAs deltas
    delta_close_ema9: Optional[float] = None
    pct_close_ema9: Optional[float] = None
    delta_close_ema21: Optional[float] = None
    pct_close_ema21: Optional[float] = None
    delta_close_ema50: Optional[float] = None
    pct_close_ema50: Optional[float] = None
    delta_close_ema200: Optional[float] = None
    pct_close_ema200: Optional[float] = None
    # Price vs SMA deltas
    delta_close_sma200: Optional[float] = None
    pct_close_sma200: Optional[float] = None
    # Price vs VWAP deltas
    delta_close_vwap_session: Optional[float] = None
    pct_close_vwap_session: Optional[float] = None
    delta_close_vwap_week: Optional[float] = None
    pct_close_vwap_week: Optional[float] = None
    delta_close_vwap_month: Optional[float] = None
    pct_close_vwap_month: Optional[float] = None
    # Volume deltas
    delta_volume_ma20: Optional[float] = None
    pct_volume_ma20: Optional[float] = None
    delta_volume_ma30: Optional[float] = None
    pct_volume_ma30: Optional[float] = None
    delta_volume_prev: Optional[float] = None
    pct_volume_prev: Optional[float] = None
    # RSI deltas
    delta_rsi_prev: Optional[float] = None
    delta_rsi_ma14: Optional[float] = None
    
    def to_dataframe_row(self) -> Dict[str, Any]:
        """Convert to flat dictionary for DataFrame."""
        result = self.raw_data.to_dict()
        # Add all delta fields
        for field_name in self.__dataclass_fields__:
            if field_name != 'raw_data' and hasattr(self, field_name):
                result[field_name] = getattr(self, field_name)
        return result


# Processing result models
@dataclass
class ProcessingResult:
    """Result of webhook data processing."""
    status: str  # "success" or "error"
    processing_stats: 'ProcessingStats'
    storage_results: 'StorageResults'
    config_used: Dict[str, Any]
    error: Optional[str] = None
    error_type: Optional[str] = None
    
    def to_response_dict(self) -> Dict[str, Any]:
        """Convert to webhook response format."""
        if self.status == "error":
            return {
                "status": self.status,
                "message": self.error,
                "error_type": self.error_type
            }
        
        return {
            "status": self.status,
            **self.processing_stats.to_dict(),
            "symbol_breakdown": self.storage_results.symbols_processed,
            "global_master_file": self.storage_results.global_master_file
        }


@dataclass
class ProcessingStats:
    """Statistics from data processing."""
    received_rows: int
    processed_rows: int
    symbols_processed: int
    symbols: List[str]
    total_files_updated: int
    latest_time: str
    storage_mode: StorageMode
    enhancements: Dict[str, Any]
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            "received_rows": self.received_rows,
            "processed_rows": self.processed_rows,
            "symbols_processed": self.symbols_processed,
            "symbols": self.symbols,
            "total_files_updated": self.total_files_updated,
            "latest_time": self.latest_time,
            "storage_mode": self.storage_mode.value,
            "enhancements": self.enhancements
        }


@dataclass
class StorageResults:
    """Results from storage operations."""
    total_rows: int
    symbols_processed: Dict[str, 'SymbolStorageResult']
    global_files_updated: List[str]
    total_files_updated: int
    storage_mode: StorageMode
    global_master_file: Optional[Dict[str, Any]] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            "total_rows": self.total_rows,
            "symbols_processed": {k: v.to_dict() for k, v in self.symbols_processed.items()},
            "global_files_updated": self.global_files_updated,
            "total_files_updated": self.total_files_updated,
            "storage_mode": self.storage_mode.value,
            "global_master_file": self.global_master_file
        }


@dataclass
class SymbolStorageResult:
    """Storage result for a specific symbol."""
    symbol: str
    total_rows: int
    timeframes: Dict[str, 'TimeframeStorageResult']
    files_updated: List[str]
    storage_mode: StorageMode
    enhancements_applied: Dict[str, bool]
    symbol_master_file: Optional[Dict[str, Any]] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            "symbol": self.symbol,
            "total_rows": self.total_rows,
            "timeframes": {k: v.to_dict() for k, v in self.timeframes.items()},
            "files_updated": self.files_updated,
            "storage_mode": self.storage_mode.value,
            "enhancements_applied": self.enhancements_applied,
            "symbol_master_file": self.symbol_master_file
        }


@dataclass
class TimeframeStorageResult:
    """Storage result for a specific timeframe."""
    rows: int
    file: str
    latest_time: str
    mode_used: StorageMode
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            "rows": self.rows,
            "file": self.file,
            "latest_time": self.latest_time,
            "mode_used": self.mode_used.value
        }


# Server and infrastructure models
@dataclass
class ServerStatus:
    """Webhook server status."""
    is_running: bool
    port: int
    local_url: Optional[str]
    webhook_url: Optional[str]
    data_directory: str
    export_master_file: bool
    export_global_master: bool
    max_rows_per_symbol: int
    data_storage_mode: StorageMode
    ngrok_status: 'NgrokStatus'
    supported_columns: int
    base_columns: int
    delta_columns: int
    allowed_timeframes: List[str]
    enhancements: Dict[str, bool]
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for API response."""
        return {
            "is_running": self.is_running,
            "port": self.port,
            "local_url": self.local_url,
            "webhook_url": self.webhook_url,
            "data_directory": self.data_directory,
            "export_master_file": self.export_master_file,
            "export_global_master": self.export_global_master,
            "max_rows_per_symbol": self.max_rows_per_symbol,
            "data_storage_mode": self.data_storage_mode.value,
            "ngrok_status": self.ngrok_status.to_dict(),
            "supported_columns": self.supported_columns,
            "base_columns": self.base_columns,
            "delta_columns": self.delta_columns,
            "allowed_timeframes": self.allowed_timeframes,
            "enhancements": self.enhancements
        }


@dataclass
class NgrokStatus:
    """Ngrok tunnel status."""
    is_running: bool
    public_url: Optional[str]
    local_port: int
    domain: Optional[str]
    has_auth_token: bool
    ngrok_path: Optional[str]
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return self.__dict__.copy()


@dataclass
class ProcessorStatus:
    """Data processor status."""
    webhook_processor: Dict[str, Any]
    delta_calculator: Dict[str, Any]
    vwap_filter: Dict[str, Any]
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return self.__dict__.copy()


# Data summary models
@dataclass
class DataSummary:
    """Summary of stored data."""
    symbols: List[str]
    symbol_count: int
    file_info: 'FileInfo'
    total_size: int
    exists: bool
    last_updated: Optional[datetime] = None
    timeframe_breakdown: Optional[Dict[str, int]] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            "symbols": self.symbols,
            "symbol_count": self.symbol_count,
            "file_info": self.file_info.to_dict(),
            "total_size": self.total_size,
            "exists": self.exists,
            "last_updated": self.last_updated.isoformat() if self.last_updated else None,
            "timeframe_breakdown": self.timeframe_breakdown
        }


@dataclass
class FileInfo:
    """File information for stored data."""
    exists: bool
    symbols: Dict[str, 'SymbolFileInfo'] = field(default_factory=dict)
    total_size: int = 0
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            "exists": self.exists,
            "symbols": {k: v.to_dict() for k, v in self.symbols.items()},
            "total_size": self.total_size
        }


@dataclass
class SymbolFileInfo:
    """File information for a specific symbol."""
    exists: bool
    files: Dict[str, 'FileDetail']
    total_size: int
    file_count: int
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            "exists": self.exists,
            "files": {k: v.to_dict() for k, v in self.files.items()},
            "total_size": self.total_size,
            "file_count": self.file_count
        }


@dataclass
class FileDetail:
    """Details of a specific file."""
    size: int
    modified: datetime
    path: str
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            "size": self.size,
            "modified": self.modified.isoformat(),
            "path": self.path
        }


# Configuration models
@dataclass
class ProcessingConfig:
    """Configuration for data processing."""
    export_master_file: bool = True
    export_global_master: bool = True
    enable_delta_calculations: bool = True
    enable_vwap_filtering: bool = True
    data_storage_mode: StorageMode = StorageMode.APPEND
    max_rows_per_symbol: int = 50
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            "export_master_file": self.export_master_file,
            "export_global_master": self.export_global_master,
            "enable_delta_calculations": self.enable_delta_calculations,
            "enable_vwap_filtering": self.enable_vwap_filtering,
            "data_storage_mode": self.data_storage_mode.value,
            "max_rows_per_symbol": self.max_rows_per_symbol
        }


# Service layer models
@dataclass
class WebhookPayload:
    """Validated webhook payload."""
    symbol: str
    timeframe: str
    timestamp: Union[str, datetime]
    open: float
    high: float
    low: float
    close: float
    volume: float
    
    def validate(self) -> Tuple[bool, Optional[str]]:
        """Validate payload data."""
        if not self.symbol:
            return False, "Symbol is required"
        if not self.timeframe:
            return False, "Timeframe is required"
        if self.open <= 0 or self.high <= 0 or self.low <= 0 or self.close <= 0:
            return False, "Price values must be positive"
        if self.volume < 0:
            return False, "Volume cannot be negative"
        return True, None
```

### Part 2: Refactor `TvIngestService` and Integrate Models

With the models in place, the service layer will be refactored to be a lean orchestrator that uses these new, typed data structures.

**Task 2.1: Refactor `svc_tv_ingest.py`**

-   **File:** `components/tv_ingest/service/svc_tv_ingest.py`
-   **Actions:**
    1.  **Update Imports:** Import the new models required by the service.
        ```python
        from ..models.models_tv_ingest import WebhookPayload, ProcessingResult
        ```
    2.  **Remove Delegated Methods:** To make the service a true orchestrator, remove all methods that are simple wrappers for `CsvRepository` or `TvIngestDataProcessor`. The frontend builder will be updated to call these components directly. The following methods must be **removed** from the service:
        -   `get_available_symbols`
        -   `get_available_timeframes`
        -   `get_data`
        -   `export_data_as_csv`
        -   `clear_data`
        -   `backup_data`
        -   `get_data_summary`
        -   `validate_webhook_payload`
        -   `get_processor_status`
        -   `format_data_for_display`
        -   `get_latest_data`
        -   `export_to_csv`
        -   `export_to_json`
        -   `get_file_info`
        -   `get_llm_context_data`
    3.  **Update Method Signatures:** Modify the remaining core methods to use the new data models for their inputs and outputs.
        ```python
        # Modify the ingest_webhook signature
        def ingest_webhook(self, payload: WebhookPayload) -> ProcessingResult:
            """Process and store webhook data using structured models."""
            # The implementation must be updated to work with and return these models.
            # It will call the data processor and repository, then construct a 
            # ProcessingResult model from the outcomes.
            ...

        # The render() method will remain, but the frontend it calls will be updated.
        def render(self):
            ...
        ```

**Task 2.2: Update Dependent Components**

The introduction of models and the refactoring of the service requires changes in the components that interact with it.

-   **`fb_tv_ingest.py` (Frontend Builder):**
    -   This builder will now instantiate `CsvRepository` and `TvIngestDataProcessor` directly to fetch data for the UI.
    -   All calls to the removed service methods must be updated to call the repository or processor directly (e.g., `service.get_available_symbols()` becomes `repo.get_available_symbols()`).
    -   The builder will be responsible for constructing `DataSummary` or other UI-specific models from the data it fetches.

-   **`webhook_server.py`:**
    -   The `/webhook` endpoint must be updated to create a `WebhookPayload` object from the incoming JSON request before passing it to `svc_tv_ingest.ingest_webhook`.
    -   The `/status` endpoint should be updated to construct and return a `ServerStatus` model.

-   **`dp_tv_ingest.py` and `csv_repository.py`:**
    -   Update method signatures in these components to return the new models where appropriate (e.g., `csv_repository.get_file_info` should return a `FileInfo` model).

## 3. Testing Strategy

1.  **Model Tests:** Create `tests/test_models_tv_ingest.py`. Add unit tests for each data model, verifying creation, default values, any internal logic (like `to_dict` methods), and validation.
2.  **Service Tests:** Update `tests/test_svc_tv_ingest.py` to test the refactored service. Mock the data processor and repository, and verify that `ingest_webhook` correctly orchestrates the process and returns a `ProcessingResult` model.
3.  **Integration Tests:** Update integration tests to ensure the full pipeline—from `webhook_server.py` receiving a request to data being stored by `csv_repository.py`—works correctly with the new models.

## 4. Documentation

1.  **`main.md`:** Update the `main.md` file for the `tv_ingest` component to document the new, model-driven architecture and the responsibilities of the refactored service.
2.  **`change_history.md`:** Add an entry for version `v1.1.0` detailing the service layer refactoring and the introduction of data models.
