"""
Format Detection System

This module provides intelligent format detection for conversation files,
supporting auto-detection with manual override options.
"""

from typing import Optional, Dict, Any, List
from pathlib import Path
import json

from ..conversation_models.unified_conversation import FormatType
from .base_parser import FormatDetectionError


class FormatDetector:
    """
    Intelligent format detection system for conversation files.
    
    This class provides multiple detection methods and can be used
    independently or as part of the parsing pipeline.
    """
    
    def __init__(self):
        """Initialize the format detector with detection rules."""
        self.detection_rules = {
            FormatType.STANDARD_JSON: {
                'extensions': ['.json'],
                'required_keys': ['runSettings', 'systemInstruction'],
                'optional_keys': ['chunkedPrompt'],
                'exclusion_keys': ['comparisonPrompt'],
                'confidence_threshold': 0.8
            },
            FormatType.COMPARISON_JSON: {
                'extensions': ['.json'],
                'required_keys': ['comparisonPrompt'],
                'indicator_keys': ['data'],
                'confidence_threshold': 0.9
            },
            FormatType.PLAIN_TEXT_LOG: {
                'extensions': ['.txt', '.log'],
                'content_patterns': [
                    'Claude Code',
                    'Welcome to Claude Code',
                    '> ',  # User commands
                    'TodoWrite',
                    'tool usage',
                    'Thinking'
                ],
                'confidence_threshold': 0.6
            }
        }
    
    def detect_format(self, file_path: str, force_format: Optional[FormatType] = None) -> FormatType:
        """
        Detect the conversation format of a file.
        
        Args:
            file_path: Path to the conversation file
            force_format: Override auto-detection with specific format
            
        Returns:
            FormatType: Detected or forced format
            
        Raises:
            FormatDetectionError: If format cannot be determined
        """
        if force_format:
            self._validate_forced_format(file_path, force_format)
            return force_format
        
        # Multiple detection strategies
        detection_results = {}
        
        # Strategy 1: File extension analysis
        ext_result = self._detect_by_extension(file_path)
        if ext_result:
            detection_results['extension'] = ext_result
        
        # Strategy 2: Content structure analysis
        content_result = self._detect_by_content_structure(file_path)
        if content_result:
            detection_results['content'] = content_result
        
        # Strategy 3: Pattern matching
        pattern_result = self._detect_by_patterns(file_path)
        if pattern_result:
            detection_results['patterns'] = pattern_result
        
        # Combine results and determine best match
        final_format = self._combine_detection_results(detection_results, file_path)
        
        if not final_format:
            raise FormatDetectionError(
                f"Unable to determine format for file: {file_path}",
                file_path,
                {"detection_results": detection_results}
            )
        
        return final_format
    
    def _detect_by_extension(self, file_path: str) -> Optional[Dict[str, Any]]:
        """Detect format based on file extension."""
        file_ext = Path(file_path).suffix.lower()
        
        candidates = []
        for format_type, rules in self.detection_rules.items():
            if file_ext in rules.get('extensions', []):
                candidates.append({
                    'format': format_type,
                    'confidence': 0.3,  # Low confidence for extension alone
                    'method': 'extension'
                })
        
        return candidates[0] if candidates else None
    
    def _detect_by_content_structure(self, file_path: str) -> Optional[Dict[str, Any]]:
        """Detect format based on content structure analysis."""
        try:
            content = self._read_file_safely(file_path)
            
            # Try JSON structure detection
            try:
                data = json.loads(content)
                if isinstance(data, dict):
                    return self._analyze_json_structure(data)
            except json.JSONDecodeError:
                pass
            
            # Try plain text analysis
            return self._analyze_text_structure(content)
            
        except Exception as e:
            # Don't fail on content analysis errors
            return None
    
    def _analyze_json_structure(self, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Analyze JSON structure to determine format."""
        for format_type, rules in self.detection_rules.items():
            if format_type in [FormatType.STANDARD_JSON, FormatType.COMPARISON_JSON]:
                confidence = self._calculate_json_confidence(data, rules)
                if confidence >= rules.get('confidence_threshold', 0.5):
                    return {
                        'format': format_type,
                        'confidence': confidence,
                        'method': 'json_structure'
                    }
        
        return None
    
    def _calculate_json_confidence(self, data: Dict[str, Any], rules: Dict[str, Any]) -> float:
        """Calculate confidence score for JSON format detection."""
        score = 0.0
        max_score = 0.0
        
        # Check required keys
        required_keys = rules.get('required_keys', [])
        if required_keys:
            max_score += 1.0
            if all(key in data for key in required_keys):
                score += 1.0
        
        # Check optional keys
        optional_keys = rules.get('optional_keys', [])
        if optional_keys:
            max_score += 0.5
            if any(key in data for key in optional_keys):
                score += 0.5
        
        # Check indicator keys
        indicator_keys = rules.get('indicator_keys', [])
        if indicator_keys:
            max_score += 0.5
            # For comparison JSON, check nested keys in comparisonPrompt
            if 'comparisonPrompt' in data and isinstance(data['comparisonPrompt'], dict):
                if any(key in data['comparisonPrompt'] for key in indicator_keys):
                    score += 0.5
            elif any(key in data for key in indicator_keys):
                score += 0.5
        
        # Check exclusion keys (negative indicators)
        exclusion_keys = rules.get('exclusion_keys', [])
        if exclusion_keys:
            if any(key in data for key in exclusion_keys):
                score -= 0.5
        
        return score / max_score if max_score > 0 else 0.0
    
    def _analyze_text_structure(self, content: str) -> Optional[Dict[str, Any]]:
        """Analyze plain text structure to determine format."""
        rules = self.detection_rules.get(FormatType.PLAIN_TEXT_LOG, {})
        patterns = rules.get('content_patterns', [])
        
        if not patterns:
            return None
        
        pattern_matches = 0
        content_lower = content.lower()
        
        for pattern in patterns:
            if pattern.lower() in content_lower:
                pattern_matches += 1
        
        confidence = pattern_matches / len(patterns)
        threshold = rules.get('confidence_threshold', 0.5)
        
        if confidence >= threshold:
            return {
                'format': FormatType.PLAIN_TEXT_LOG,
                'confidence': confidence,
                'method': 'text_patterns'
            }
        
        return None
    
    def _detect_by_patterns(self, file_path: str) -> Optional[Dict[str, Any]]:
        """Detect format using pattern matching."""
        try:
            content = self._read_file_safely(file_path)
            
            # Advanced pattern detection for each format
            pattern_scores = {}
            
            # Standard JSON patterns
            if self._has_standard_json_patterns(content):
                pattern_scores[FormatType.STANDARD_JSON] = 0.7
            
            # Comparison JSON patterns
            if self._has_comparison_json_patterns(content):
                pattern_scores[FormatType.COMPARISON_JSON] = 0.8
            
            # Plain text log patterns
            if self._has_plaintext_log_patterns(content):
                pattern_scores[FormatType.PLAIN_TEXT_LOG] = 0.6
            
            if pattern_scores:
                best_format = max(pattern_scores.items(), key=lambda x: x[1])
                return {
                    'format': best_format[0],
                    'confidence': best_format[1],
                    'method': 'pattern_matching'
                }
        
        except Exception:
            pass
        
        return None
    
    def _has_standard_json_patterns(self, content: str) -> bool:
        """Check for standard JSON conversation patterns."""
        indicators = [
            '"runSettings"',
            '"systemInstruction"',
            '"chunkedPrompt"',
            '"temperature"',
            '"model"'
        ]
        return sum(1 for indicator in indicators if indicator in content) >= 3
    
    def _has_comparison_json_patterns(self, content: str) -> bool:
        """Check for comparison JSON conversation patterns."""
        indicators = [
            '"comparisonPrompt"',
            '"data"',
            'thread',
            'comparison'
        ]
        return sum(1 for indicator in indicators if indicator in content) >= 2
    
    def _has_plaintext_log_patterns(self, content: str) -> bool:
        """Check for plain text log patterns."""
        indicators = [
            'Claude Code',
            'Welcome to',
            '> ',
            'TodoWrite',
            'tool usage',
            'Thinking',
            'Assistant:',
            'User:'
        ]
        return sum(1 for indicator in indicators if indicator in content) >= 3
    
    def _combine_detection_results(self, results: Dict[str, Dict], file_path: str) -> Optional[FormatType]:
        """Combine multiple detection results to determine final format."""
        if not results:
            return None
        
        # Weighted scoring system
        method_weights = {
            'extension': 0.2,
            'content': 0.5,
            'patterns': 0.3
        }
        
        format_scores = {}
        
        for method, result in results.items():
            if isinstance(result, dict):
                format_type = result['format']
                confidence = result['confidence']
                weight = method_weights.get(method, 0.1)
                
                if format_type not in format_scores:
                    format_scores[format_type] = 0
                format_scores[format_type] += confidence * weight
        
        if not format_scores:
            return None
        
        # Return format with highest score
        best_format = max(format_scores.items(), key=lambda x: x[1])
        
        # Require minimum confidence threshold
        if best_format[1] >= 0.4:
            return best_format[0]
        
        return None
    
    def _validate_forced_format(self, file_path: str, forced_format: FormatType) -> None:
        """Validate that forced format is reasonable for the file."""
        try:
            content = self._read_file_safely(file_path)
            
            # Basic validation - ensure format is at least plausible
            if forced_format in [FormatType.STANDARD_JSON, FormatType.COMPARISON_JSON]:
                try:
                    json.loads(content)
                except json.JSONDecodeError:
                    raise FormatDetectionError(
                        f"Forced JSON format {forced_format.value} specified, but file is not valid JSON",
                        file_path
                    )
            
        except Exception as e:
            if isinstance(e, FormatDetectionError):
                raise
            # Don't fail validation on read errors
    
    def _read_file_safely(self, file_path: str) -> str:
        """Safely read file content for analysis."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            raise FormatDetectionError(f"Cannot read file for analysis: {str(e)}", file_path)
    
    def get_format_confidence(self, file_path: str) -> Dict[FormatType, float]:
        """Get confidence scores for all formats."""
        try:
            detection_results = {}
            
            # Run all detection methods
            content_result = self._detect_by_content_structure(file_path)
            if content_result:
                detection_results['content'] = content_result
            
            pattern_result = self._detect_by_patterns(file_path)
            if pattern_result:
                detection_results['patterns'] = pattern_result
            
            # Calculate confidence for each format
            format_confidences = {}
            for format_type in FormatType:
                format_confidences[format_type] = 0.0
            
            for result in detection_results.values():
                if isinstance(result, dict):
                    format_type = result['format']
                    confidence = result['confidence']
                    format_confidences[format_type] = max(
                        format_confidences[format_type],
                        confidence
                    )
            
            return format_confidences
            
        except Exception:
            return {format_type: 0.0 for format_type in FormatType}
    
    def detect_with_fallbacks(self, file_path: str, fallback_formats: List[FormatType]) -> FormatType:
        """Detect format with fallback options."""
        try:
            return self.detect_format(file_path)
        except FormatDetectionError:
            # Try fallback formats in order
            for fallback in fallback_formats:
                try:
                    self._validate_forced_format(file_path, fallback)
                    return fallback
                except:
                    continue
            
            # If all fallbacks fail, raise original error
            raise FormatDetectionError(
                f"Format detection failed and all fallbacks exhausted for: {file_path}",
                file_path
            )