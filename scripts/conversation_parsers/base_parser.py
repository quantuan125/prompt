"""
Base Parser Abstract Class

This module defines the abstract base class for all conversation parsers,
providing a common interface and error handling patterns.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
from pathlib import Path
import json
import time

from ..conversation_models.unified_conversation import (
    UnifiedConversation, FormatType, ConversationMetadata
)


class ParseError(Exception):
    """Base exception for parsing errors"""
    def __init__(self, message: str, file_path: Optional[str] = None, details: Optional[Dict[str, Any]] = None):
        self.message = message
        self.file_path = file_path
        self.details = details or {}
        super().__init__(self.message)


class ValidationError(ParseError):
    """Exception raised when validation fails"""
    pass


class FormatDetectionError(ParseError):
    """Exception raised when format detection fails"""
    pass


class BaseParser(ABC):
    """
    Abstract base class for conversation parsers.
    
    All concrete parser implementations must inherit from this class
    and implement the required abstract methods.
    """
    
    def __init__(self, parser_version: str = "1.0.0"):
        """
        Initialize the base parser.
        
        Args:
            parser_version: Version identifier for this parser implementation
        """
        self.parser_version = parser_version
        self.supported_extensions = []
        self.format_indicators = {}
    
    @abstractmethod
    def detect_format(self, file_path: str) -> FormatType:
        """
        Detect the conversation format of the given file.
        
        Args:
            file_path: Path to the conversation file
            
        Returns:
            FormatType: The detected format type
            
        Raises:
            FormatDetectionError: If format cannot be determined
            ParseError: If file cannot be read or processed
        """
        pass
    
    @abstractmethod
    def parse(self, file_path: str) -> UnifiedConversation:
        """
        Parse a conversation file into unified format.
        
        Args:
            file_path: Path to the conversation file
            
        Returns:
            UnifiedConversation: Parsed conversation data
            
        Raises:
            ParseError: If parsing fails
            ValidationError: If parsed data is invalid
        """
        pass
    
    @abstractmethod
    def validate(self, data: Any) -> bool:
        """
        Validate conversation data structure.
        
        Args:
            data: Data to validate (can be dict, str, etc.)
            
        Returns:
            bool: True if valid, False otherwise
        """
        pass
    
    def _read_file(self, file_path: str) -> str:
        """
        Safely read file content.
        
        Args:
            file_path: Path to the file to read
            
        Returns:
            str: File content
            
        Raises:
            ParseError: If file cannot be read
        """
        try:
            file_path_obj = Path(file_path)
            if not file_path_obj.exists():
                raise ParseError(f"File not found: {file_path}", file_path)
            
            if not file_path_obj.is_file():
                raise ParseError(f"Path is not a file: {file_path}", file_path)
            
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if not content.strip():
                raise ParseError(f"File is empty: {file_path}", file_path)
            
            return content
            
        except UnicodeDecodeError as e:
            raise ParseError(f"File encoding error: {str(e)}", file_path, {"encoding_error": str(e)})
        except PermissionError as e:
            raise ParseError(f"Permission denied: {str(e)}", file_path, {"permission_error": str(e)})
        except Exception as e:
            raise ParseError(f"Error reading file: {str(e)}", file_path, {"read_error": str(e)})
    
    def _read_json_file(self, file_path: str) -> Dict[str, Any]:
        """
        Safely read and parse JSON file.
        
        Args:
            file_path: Path to the JSON file
            
        Returns:
            Dict[str, Any]: Parsed JSON data
            
        Raises:
            ParseError: If file cannot be read or JSON is invalid
        """
        content = self._read_file(file_path)
        
        try:
            data = json.loads(content)
            if not isinstance(data, dict):
                raise ParseError(f"JSON root must be an object, got {type(data).__name__}", file_path)
            return data
        except json.JSONDecodeError as e:
            raise ParseError(f"Invalid JSON: {str(e)}", file_path, {"json_error": str(e)})
    
    def _create_base_conversation(self, format_type: FormatType, file_path: str) -> UnifiedConversation:
        """
        Create a base UnifiedConversation with metadata.
        
        Args:
            format_type: The detected format type
            file_path: Source file path
            
        Returns:
            UnifiedConversation: Base conversation object
        """
        metadata = ConversationMetadata(
            source_file=file_path,
            parser_version=self.parser_version
        )
        
        return UnifiedConversation(
            format_type=format_type,
            metadata=metadata
        )
    
    def _validate_file_extension(self, file_path: str, expected_extensions: list) -> bool:
        """
        Validate file extension.
        
        Args:
            file_path: Path to the file
            expected_extensions: List of expected extensions (with dots)
            
        Returns:
            bool: True if extension matches
        """
        file_path_obj = Path(file_path)
        return file_path_obj.suffix.lower() in expected_extensions
    
    def _detect_format_by_content(self, content: str) -> Optional[FormatType]:
        """
        Attempt to detect format by analyzing content.
        
        Args:
            content: File content to analyze
            
        Returns:
            Optional[FormatType]: Detected format or None if unknown
        """
        # Try JSON format detection
        try:
            data = json.loads(content)
            if isinstance(data, dict):
                # Check for comparison format indicators
                if 'comparisonPrompt' in data:
                    return FormatType.COMPARISON_JSON
                
                # Check for standard format indicators
                if 'runSettings' in data and ('systemInstruction' in data or 'chunkedPrompt' in data):
                    return FormatType.STANDARD_JSON
        except json.JSONDecodeError:
            pass
        
        # Check for plain text log patterns
        plain_text_indicators = [
            'Claude Code',
            'Welcome to Claude Code',
            '> ',  # User commands
            '\u25B6',   # Unicode symbols common in logs
            'Thinking',
            'TodoWrite',
            'tool usage'
        ]
        
        content_lower = content.lower()
        if any(indicator.lower() in content_lower for indicator in plain_text_indicators):
            return FormatType.PLAIN_TEXT_LOG
        
        return None
    
    def _handle_parsing_error(self, error: Exception, file_path: str, context: str = "parsing") -> None:
        """
        Handle and re-raise parsing errors with proper context.
        
        Args:
            error: Original exception
            file_path: File being parsed
            context: Context where error occurred
            
        Raises:
            ParseError: Enhanced error with context
        """
        if isinstance(error, (ParseError, ValidationError, FormatDetectionError)):
            raise error
        
        error_details = {
            "original_error": str(error),
            "error_type": type(error).__name__,
            "context": context
        }
        
        raise ParseError(f"Error during {context}: {str(error)}", file_path, error_details)
    
    def parse_with_timing(self, file_path: str) -> UnifiedConversation:
        """
        Parse conversation file with timing information.
        
        Args:
            file_path: Path to the conversation file
            
        Returns:
            UnifiedConversation: Parsed conversation with timing metadata
        """
        start_time = time.time()
        
        try:
            result = self.parse(file_path)
            processing_time = time.time() - start_time
            result.metadata.processing_time = processing_time
            return result
        except Exception as e:
            self._handle_parsing_error(e, file_path, "timed parsing")
    
    def validate_and_parse(self, file_path: str) -> UnifiedConversation:
        """
        Validate file and parse if valid.
        
        Args:
            file_path: Path to the conversation file
            
        Returns:
            UnifiedConversation: Parsed conversation data
            
        Raises:
            ValidationError: If file validation fails
            ParseError: If parsing fails
        """
        # Pre-validation
        if not Path(file_path).exists():
            raise ValidationError(f"File does not exist: {file_path}", file_path)
        
        # Detect format first
        try:
            detected_format = self.detect_format(file_path)
        except Exception as e:
            self._handle_parsing_error(e, file_path, "format detection")
        
        # Parse with detected format
        try:
            result = self.parse(file_path)
            
            # Post-validation
            if not result.conversations:
                raise ValidationError("No conversations found in parsed data", file_path)
            
            return result
        except Exception as e:
            self._handle_parsing_error(e, file_path, "validated parsing")
    
    def get_parser_info(self) -> Dict[str, Any]:
        """
        Get information about this parser.
        
        Returns:
            Dict[str, Any]: Parser information
        """
        return {
            "parser_class": self.__class__.__name__,
            "parser_version": self.parser_version,
            "supported_extensions": self.supported_extensions,
            "format_indicators": self.format_indicators
        }