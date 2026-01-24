"""
Comparison JSON Parser

This module provides parsing functionality for comparison conversation JSON files,
which contain multiple parallel conversation threads for A/B testing analysis.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime

from .base_parser import BaseParser, ParseError, ValidationError
from ..conversation_models.unified_conversation import (
    FormatType, UnifiedConversation, ConversationThread, ConversationMessage,
    MessageContent, MessageRole, ContentType, ConversationMetadata, ComparisonAnalysis
)


class ComparisonJsonParser(BaseParser):
    """
    Parser for comparison conversation JSON format.
    
    Handles parallel conversation analysis format with multiple threads,
    supporting comparison of different system prompts, parameters, and responses.
    """
    
    def __init__(self, parser_version: str = "1.0.0"):
        """Initialize the comparison JSON parser."""
        super().__init__(parser_version)
        self.supported_extensions = ['.json']
        self.format_indicators = {
            'required_keys': ['comparisonPrompt'],
            'indicator_keys': ['data']
        }
    
    def detect_format(self, file_path: str) -> FormatType:
        """
        Detect if file is comparison JSON conversation format.
        
        Args:
            file_path: Path to the conversation file
            
        Returns:
            FormatType.COMPARISON_JSON if detected
            
        Raises:
            FormatDetectionError: If not comparison JSON format
        """
        try:
            data = self._read_json_file(file_path)
            
            # Check for required comparisonPrompt key
            if 'comparisonPrompt' not in data:
                from .base_parser import FormatDetectionError
                raise FormatDetectionError(
                    "Missing comparisonPrompt key for comparison JSON format",
                    file_path
                )
            
            # Validate basic structure
            comparison_prompt = data['comparisonPrompt']
            if not isinstance(comparison_prompt, dict):
                from .base_parser import FormatDetectionError
                raise FormatDetectionError(
                    "comparisonPrompt must be an object",
                    file_path
                )
            
            return FormatType.COMPARISON_JSON
            
        except Exception as e:
            self._handle_parsing_error(e, file_path, "format detection")
    
    def validate(self, data: Any) -> bool:
        """
        Validate comparison JSON conversation data structure.
        
        Args:
            data: Data to validate
            
        Returns:
            bool: True if valid comparison JSON structure
        """
        try:
            if not isinstance(data, dict):
                return False
            
            # Check required comparisonPrompt key
            if 'comparisonPrompt' not in data:
                return False
            
            comparison_prompt = data['comparisonPrompt']
            if not isinstance(comparison_prompt, dict):
                return False
            
            # Require data array to be present for comparison format
            if 'data' not in comparison_prompt:
                return False
            
            comparison_data = comparison_prompt['data']
            if not isinstance(comparison_data, list):
                return False
            
            # Should have at least one thread for comparison
            if len(comparison_data) == 0:
                return False
            
            # Validate each thread structure
            for thread_data in comparison_data:
                if not isinstance(thread_data, dict):
                    return False
                
                # Each thread should have basic structure
                if 'chunkedPrompt' in thread_data:
                    chunked_prompt = thread_data['chunkedPrompt']
                    if not isinstance(chunked_prompt, dict):
                        return False
            
            return True
            
        except Exception:
            return False
    
    def parse(self, file_path: str) -> UnifiedConversation:
        """
        Parse comparison JSON conversation file.
        
        Args:
            file_path: Path to the conversation file
            
        Returns:
            UnifiedConversation: Parsed conversation data with multiple threads
            
        Raises:
            ParseError: If parsing fails
            ValidationError: If data structure is invalid
        """
        try:
            # Read and validate JSON data
            data = self._read_json_file(file_path)
            
            if not self.validate(data):
                raise ValidationError(f"Invalid comparison JSON structure", file_path)
            
            # Create base conversation object
            conversation = self._create_base_conversation(FormatType.COMPARISON_JSON, file_path)
            
            # Extract metadata
            self._extract_metadata(conversation, data)
            
            # Parse comparison threads
            comparison_prompt = data['comparisonPrompt']
            if 'data' in comparison_prompt:
                threads = self._parse_comparison_threads(comparison_prompt['data'])
                for thread in threads:
                    conversation.add_conversation_thread(thread)
            
            # Perform comparison analysis
            self._analyze_threads(conversation)
            
            # Calculate total tokens
            total_tokens = conversation.calculate_total_tokens()
            conversation.metadata.total_tokens = total_tokens
            
            return conversation
            
        except Exception as e:
            self._handle_parsing_error(e, file_path, "comparison JSON parsing")
    
    def _extract_metadata(self, conversation: UnifiedConversation, data: Dict[str, Any]) -> None:
        """Extract metadata from comparison JSON data."""
        comparison_prompt = data.get('comparisonPrompt', {})
        
        # Store format-specific data
        conversation.format_specific_data = {
            'comparison_prompt': comparison_prompt,
            'original_structure': data
        }
        
        # Count threads
        if 'data' in comparison_prompt:
            conversation.metadata.thread_count = len(comparison_prompt['data'])
    
    def _parse_comparison_threads(self, threads_data: List[Dict[str, Any]]) -> List[ConversationThread]:
        """Parse multiple conversation threads from comparison data."""
        threads = []
        
        for i, thread_data in enumerate(threads_data):
            thread = self._parse_single_thread(thread_data, i)
            if thread:
                threads.append(thread)
        
        return threads
    
    def _parse_single_thread(self, thread_data: Dict[str, Any], thread_index: int) -> Optional[ConversationThread]:
        """Parse a single conversation thread."""
        try:
            # Create thread with ID
            thread = ConversationThread(
                thread_id=f"thread_{thread_index}",
                run_settings=thread_data.get('runSettings', {}),
                metadata={'thread_index': thread_index}
            )
            
            # Extract system prompt
            if 'systemInstruction' in thread_data:
                system_instruction = thread_data['systemInstruction']
                thread.system_prompt = system_instruction.get('text', '')
            
            # Parse chunked prompt
            if 'chunkedPrompt' in thread_data:
                chunked_prompt = thread_data['chunkedPrompt']
                if 'chunks' in chunked_prompt:
                    thread.messages = self._parse_chunks(chunked_prompt['chunks'])
            
            return thread
            
        except Exception as e:
            # Log error but continue parsing other threads
            return None
    
    def _parse_chunks(self, chunks: List[Dict[str, Any]]) -> List[ConversationMessage]:
        """Parse chunks into conversation messages (reusing standard JSON logic)."""
        messages = []
        
        for i, chunk in enumerate(chunks):
            message = self._parse_chunk(chunk, i)
            if message:
                messages.append(message)
        
        return messages
    
    def _parse_chunk(self, chunk: Dict[str, Any], sequence: int) -> Optional[ConversationMessage]:
        """Parse a single chunk into a conversation message."""
        try:
            # Determine role
            role_str = chunk.get('role', 'user')
            role = self._map_role(role_str)
            
            # Parse content based on chunk type
            content_items = []
            
            # Handle text content
            if 'text' in chunk:
                content_items.append(MessageContent(
                    content_type=ContentType.TEXT,
                    text=chunk['text']
                ))
            
            # Handle drive documents
            if 'driveDocument' in chunk:
                drive_doc = chunk['driveDocument']
                content_items.append(MessageContent(
                    content_type=ContentType.DRIVE_DOCUMENT,
                    drive_document_id=drive_doc.get('id'),
                    metadata={'drive_document': drive_doc}
                ))
            
            # Handle drive images
            if 'driveImage' in chunk:
                drive_img = chunk['driveImage']
                content_items.append(MessageContent(
                    content_type=ContentType.DRIVE_IMAGE,
                    drive_image_id=drive_img.get('id'),
                    metadata={'drive_image': drive_img}
                ))
            
            # Create message
            message = ConversationMessage(
                role=role,
                content=content_items,
                sequence=sequence,
                token_count=chunk.get('tokenCount'),
                metadata=self._extract_chunk_metadata(chunk)
            )
            
            return message
            
        except Exception as e:
            # Log error but continue parsing
            return None
    
    def _map_role(self, role_str: str) -> MessageRole:
        """Map string role to MessageRole enum."""
        role_mapping = {
            'user': MessageRole.USER,
            'model': MessageRole.MODEL,
            'assistant': MessageRole.ASSISTANT,
            'system': MessageRole.SYSTEM
        }
        return role_mapping.get(role_str.lower(), MessageRole.USER)
    
    def _extract_chunk_metadata(self, chunk: Dict[str, Any]) -> Dict[str, Any]:
        """Extract metadata from chunk."""
        metadata = {}
        
        # Copy relevant metadata fields
        metadata_fields = ['tokenCount', 'role', 'finishReason']
        for field in metadata_fields:
            if field in chunk:
                metadata[field] = chunk[field]
        
        return metadata
    
    def _analyze_threads(self, conversation: UnifiedConversation) -> None:
        """Perform comparison analysis between threads."""
        if len(conversation.conversations) < 2:
            return
        
        # Analyze parameter differences
        parameter_diffs = self._analyze_parameter_differences(conversation.conversations)
        
        # Analyze response variations
        response_variations = self._analyze_response_variations(conversation.conversations)
        
        # Create comparison analysis
        analysis = ComparisonAnalysis(
            parameter_differences=parameter_diffs,
            response_variations=response_variations,
            thread_comparison=self._compare_threads(conversation.conversations)
        )
        
        conversation.set_comparison_analysis(analysis)
    
    def _analyze_parameter_differences(self, threads: List[ConversationThread]) -> Dict[str, Any]:
        """Analyze differences in run settings between threads."""
        if not threads:
            return {}
        
        # Compare run settings
        reference_settings = threads[0].run_settings
        differences = {}
        
        for i, thread in enumerate(threads[1:], 1):
            thread_diffs = {}
            thread_settings = thread.run_settings
            
            # Find differences
            all_keys = set(reference_settings.keys()) | set(thread_settings.keys())
            for key in all_keys:
                ref_value = reference_settings.get(key)
                thread_value = thread_settings.get(key)
                
                if ref_value != thread_value:
                    thread_diffs[key] = {
                        'reference': ref_value,
                        'thread': thread_value
                    }
            
            if thread_diffs:
                differences[f'thread_{i}_vs_reference'] = thread_diffs
        
        return differences
    
    def _analyze_response_variations(self, threads: List[ConversationThread]) -> List[Dict[str, Any]]:
        """Analyze variations in responses between threads."""
        variations = []
        
        if len(threads) < 2:
            return variations
        
        # Compare model responses at each step
        max_messages = max(len(thread.messages) for thread in threads)
        
        for msg_index in range(max_messages):
            variation = {
                'message_index': msg_index,
                'responses': []
            }
            
            for thread_index, thread in enumerate(threads):
                if msg_index < len(thread.messages):
                    message = thread.messages[msg_index]
                    if message.role in [MessageRole.MODEL, MessageRole.ASSISTANT]:
                        response_text = ""
                        for content in message.content:
                            if content.content_type == ContentType.TEXT:
                                response_text += content.text or ""
                        
                        variation['responses'].append({
                            'thread_id': thread.thread_id,
                            'response_text': response_text[:200] + "..." if len(response_text) > 200 else response_text,
                            'token_count': message.token_count,
                            'full_length': len(response_text)
                        })
            
            if len(variation['responses']) > 1:
                variations.append(variation)
        
        return variations
    
    def _compare_threads(self, threads: List[ConversationThread]) -> Dict[str, Any]:
        """Generate overall comparison between threads."""
        comparison = {
            'thread_count': len(threads),
            'thread_summaries': []
        }
        
        for thread in threads:
            summary = {
                'thread_id': thread.thread_id,
                'message_count': len(thread.messages),
                'total_tokens': sum(msg.token_count or 0 for msg in thread.messages),
                'system_prompt_length': len(thread.system_prompt or ''),
                'model': thread.run_settings.get('model', 'unknown'),
                'temperature': thread.run_settings.get('temperature')
            }
            comparison['thread_summaries'].append(summary)
        
        return comparison
    
    def get_supported_features(self) -> List[str]:
        """Get list of supported features for this parser."""
        return [
            'multi_thread_parsing',
            'parameter_comparison',
            'response_variation_analysis',
            'comparative_analysis',
            'run_settings_comparison',
            'system_prompt_comparison',
            'thread_isolation',
            'cross_thread_analysis'
        ]
    
    def extract_thread_count(self, file_path: str) -> int:
        """Extract the number of comparison threads without full parsing."""
        try:
            data = self._read_json_file(file_path)
            comparison_prompt = data.get('comparisonPrompt', {})
            return len(comparison_prompt.get('data', []))
        except Exception:
            return 0
    
    def get_comparison_summary(self, file_path: str) -> Dict[str, Any]:
        """Get a summary of the comparison without full parsing."""
        try:
            data = self._read_json_file(file_path)
            
            summary = {
                'format': 'comparison_json',
                'thread_count': 0,
                'models_used': set(),
                'parameter_variations': {},
                'total_chunks': 0
            }
            
            comparison_prompt = data.get('comparisonPrompt', {})
            if 'data' in comparison_prompt:
                threads = comparison_prompt['data']
                summary['thread_count'] = len(threads)
                
                for i, thread in enumerate(threads):
                    # Track models
                    model = thread.get('runSettings', {}).get('model', 'unknown')
                    summary['models_used'].add(model)
                    
                    # Track parameter variations
                    run_settings = thread.get('runSettings', {})
                    for param, value in run_settings.items():
                        if param not in summary['parameter_variations']:
                            summary['parameter_variations'][param] = set()
                        summary['parameter_variations'][param].add(str(value))
                    
                    # Count chunks
                    chunked_prompt = thread.get('chunkedPrompt', {})
                    if 'chunks' in chunked_prompt:
                        summary['total_chunks'] += len(chunked_prompt['chunks'])
            
            # Convert sets to lists for JSON serialization
            summary['models_used'] = list(summary['models_used'])
            for param in summary['parameter_variations']:
                summary['parameter_variations'][param] = list(summary['parameter_variations'][param])
            
            return summary
            
        except Exception as e:
            self._handle_parsing_error(e, file_path, "comparison summary")