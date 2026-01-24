"""Conversation Parsers Module

This module provides parsers for different conversation file formats,
all implementing a common interface defined by BaseParser.
"""

from .base_parser import (
    BaseParser,
    ParseError,
    ValidationError,
    FormatDetectionError
)
from .format_detector import FormatDetector
from .standard_json_parser import StandardJsonParser
from .comparison_json_parser import ComparisonJsonParser

__all__ = [
    'BaseParser',
    'ParseError',
    'ValidationError', 
    'FormatDetectionError',
    'FormatDetector',
    'StandardJsonParser',
    'ComparisonJsonParser'
]