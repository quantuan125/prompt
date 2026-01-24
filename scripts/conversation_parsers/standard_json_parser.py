"""
Standard JSON Parser

This module provides parsing functionality for standard conversation JSON files,
including support for chunked prompts, drive documents/images, and conversation branching.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime

from .base_parser import BaseParser, ParseError, ValidationError
from ..conversation_models.unified_conversation import (
    FormatType, UnifiedConversation, ConversationThread, ConversationMessage,
    MessageContent, MessageRole, ContentType, ConversationMetadata
)


class StandardJsonParser(BaseParser):
    """
    Parser for standard conversation JSON format.
    
    Handles the standard consultation JSON structure with runSettings,
    systemInstruction, and chunkedPrompt sections.
    """
    
    def __init__(self, parser_version: str = "1.0.0"):
        """Initialize the standard JSON parser."""
        super().__init__(parser_version)
        self.supported_extensions = ['.json']
        self.format_indicators = {
            'required_keys': ['runSettings', 'systemInstruction'],
            'optional_keys': ['chunkedPrompt'],
            'exclusion_keys': ['comparisonPrompt']
        }
    
    def detect_format(self, file_path: str) -> FormatType:
        """
        Detect if file is standard JSON conversation format.
        
        Args:
            file_path: Path to the conversation file
            
        Returns:
            FormatType.STANDARD_JSON if detected
            
        Raises:
            FormatDetectionError: If not standard JSON format
        """
        try:
            data = self._read_json_file(file_path)
            
            # Check for required keys
            required_keys = ['runSettings', 'systemInstruction']
            if not all(key in data for key in required_keys):
                from .base_parser import FormatDetectionError
                raise FormatDetectionError(
                    f"Missing required keys for standard JSON format: {required_keys}",
                    file_path
                )
            
            # Check for exclusion keys (comparison format)
            if 'comparisonPrompt' in data:
                from .base_parser import FormatDetectionError
                raise FormatDetectionError(
                    "File contains comparisonPrompt key, not standard JSON format",
                    file_path
                )
            
            return FormatType.STANDARD_JSON
            
        except Exception as e:
            self._handle_parsing_error(e, file_path, "format detection")
    
    def validate(self, data: Any) -> bool:
        """
        Validate standard JSON conversation data structure.
        
        Args:
            data: Data to validate
            
        Returns:
            bool: True if valid standard JSON structure
        """
        try:
            if not isinstance(data, dict):
                return False
            
            # Check required top-level keys
            required_keys = ['runSettings', 'systemInstruction']
            if not all(key in data for key in required_keys):
                return False
            
            # Validate runSettings structure
            run_settings = data.get('runSettings')
            if not isinstance(run_settings, dict):
                return False
            
            # Validate systemInstruction structure
            system_instruction = data.get('systemInstruction')
            if not isinstance(system_instruction, dict) or 'text' not in system_instruction:
                return False
            
            # Validate chunkedPrompt if present
            if 'chunkedPrompt' in data:
                chunked_prompt = data['chunkedPrompt']
                if not isinstance(chunked_prompt, dict) or 'chunks' not in chunked_prompt:
                    return False
                
                chunks = chunked_prompt['chunks']
                if not isinstance(chunks, list):
                    return False
            
            return True
            
        except Exception:
            return False
    
    def parse(self, file_path: str) -> UnifiedConversation:
        """
        Parse standard JSON conversation file.
        
        Args:
            file_path: Path to the conversation file
            
        Returns:
            UnifiedConversation: Parsed conversation data
            
        Raises:
            ParseError: If parsing fails
            ValidationError: If data structure is invalid
        """
        try:
            # Read and validate JSON data
            data = self._read_json_file(file_path)
            
            if not self.validate(data):
                raise ValidationError(f"Invalid standard JSON structure", file_path)
            
            # Create base conversation object
            conversation = self._create_base_conversation(FormatType.STANDARD_JSON, file_path)
            
            # Extract metadata and settings
            self._extract_metadata(conversation, data)
            
            # Extract system prompt
            conversation.system_prompt = self._extract_system_prompt(data)
            
            # Parse conversation threads
            thread = self._parse_conversation_thread(data)
            conversation.add_conversation_thread(thread)
            
            # Calculate token counts
            total_tokens = conversation.calculate_total_tokens()
            conversation.metadata.total_tokens = total_tokens
            
            return conversation
            
        except Exception as e:
            self._handle_parsing_error(e, file_path, "standard JSON parsing")
    
    def _extract_metadata(self, conversation: UnifiedConversation, data: Dict[str, Any]) -> None:
        """Extract metadata from standard JSON data."""
        # Extract run settings
        run_settings = data.get('runSettings', {})
        conversation.metadata.run_settings = run_settings
        
        # Store format-specific data
        conversation.format_specific_data = {
            'original_structure': {
                'runSettings': run_settings,
                'systemInstruction': data.get('systemInstruction', {}),
                'chunkedPrompt': data.get('chunkedPrompt', {})
            }
        }
    
    def _extract_system_prompt(self, data: Dict[str, Any]) -> str:
        """Extract system prompt from systemInstruction."""
        system_instruction = data.get('systemInstruction', {})
        return system_instruction.get('text', '')
    
    def _parse_conversation_thread(self, data: Dict[str, Any]) -> ConversationThread:
        """Parse conversation thread from chunked prompt data."""
        thread = ConversationThread(
            thread_id="main",
            system_prompt=self._extract_system_prompt(data),
            run_settings=data.get('runSettings', {})
        )
        
        # Parse chunked prompt if present
        chunked_prompt = data.get('chunkedPrompt', {})
        if chunked_prompt and 'chunks' in chunked_prompt:
            chunks = chunked_prompt['chunks']
            thread.messages = self._parse_chunks(chunks)
        
        return thread
    
    def _parse_chunks(self, chunks: List[Dict[str, Any]]) -> List[ConversationMessage]:
        """Parse chunks into conversation messages."""
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
                chunk_type=self._determine_chunk_type(chunk),
                metadata=self._extract_chunk_metadata(chunk)
            )
            
            # Handle branching information
            if 'branchParent' in chunk:
                message.branch_parent = chunk['branchParent'].get('promptId')
                message.metadata['branch_parent_display'] = chunk['branchParent'].get('displayName')
            
            if 'branchChildren' in chunk:
                message.branch_children = [child.get('promptId') for child in chunk['branchChildren']]
            
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
    
    def _determine_chunk_type(self, chunk: Dict[str, Any]) -> str:
        """Determine the type of chunk based on its content."""
        if 'driveDocument' in chunk:
            return 'drive_document'
        elif 'driveImage' in chunk:
            return 'drive_image'
        elif 'text' in chunk:
            return 'text'
        else:
            return 'unknown'
    
    def _extract_chunk_metadata(self, chunk: Dict[str, Any]) -> Dict[str, Any]:
        """Extract metadata from chunk."""
        metadata = {}
        
        # Copy relevant metadata fields
        metadata_fields = ['tokenCount', 'role', 'pendingInputs', 'isThought']
        for field in metadata_fields:
            if field in chunk:
                metadata[field] = chunk[field]
        
        # Handle special fields
        if 'branchParent' in chunk:
            metadata['branch_parent'] = chunk['branchParent']
        
        if 'branchChildren' in chunk:
            metadata['branch_children'] = chunk['branchChildren']
        
        return metadata
    
    def get_supported_features(self) -> List[str]:
        """Get list of supported features for this parser."""
        return [
            'run_settings_extraction',
            'system_instruction_parsing',
            'chunked_prompt_support',
            'drive_document_handling',
            'drive_image_handling',
            'conversation_branching',
            'token_count_extraction',
            'metadata_preservation'
        ]
    
    def extract_drive_references(self, file_path: str) -> Dict[str, List[str]]:
        """Extract all drive document and image references from the file."""
        try:
            data = self._read_json_file(file_path)
            
            drive_docs = []
            drive_images = []
            
            chunked_prompt = data.get('chunkedPrompt', {})
            if 'chunks' in chunked_prompt:
                for chunk in chunked_prompt['chunks']:
                    if 'driveDocument' in chunk:
                        doc_id = chunk['driveDocument'].get('id')
                        if doc_id:
                            drive_docs.append(doc_id)
                    
                    if 'driveImage' in chunk:
                        img_id = chunk['driveImage'].get('id')
                        if img_id:
                            drive_images.append(img_id)
            
            return {
                'documents': drive_docs,
                'images': drive_images
            }
            
        except Exception as e:
            self._handle_parsing_error(e, file_path, "drive reference extraction")
    
    def get_conversation_summary(self, file_path: str) -> Dict[str, Any]:
        """Get a summary of the conversation without full parsing."""
        try:
            data = self._read_json_file(file_path)
            
            summary = {
                'format': 'standard_json',
                'model': data.get('runSettings', {}).get('model', 'unknown'),
                'temperature': data.get('runSettings', {}).get('temperature'),
                'system_prompt_length': len(data.get('systemInstruction', {}).get('text', '')),
                'chunk_count': 0,
                'total_tokens': 0,
                'has_drive_content': False
            }
            
            chunked_prompt = data.get('chunkedPrompt', {})
            if 'chunks' in chunked_prompt:
                chunks = chunked_prompt['chunks']
                summary['chunk_count'] = len(chunks)
                
                for chunk in chunks:
                    # Count tokens
                    if 'tokenCount' in chunk:
                        summary['total_tokens'] += chunk['tokenCount']
                    
                    # Check for drive content
                    if 'driveDocument' in chunk or 'driveImage' in chunk:
                        summary['has_drive_content'] = True
            
            return summary
            
        except Exception as e:
            self._handle_parsing_error(e, file_path, "conversation summary")