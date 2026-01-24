"""
Unified Conversation Data Model

This module defines the unified data structures for representing conversations
across different input formats (Standard JSON, Comparison JSON, Plain Text Log).
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional, Union
from datetime import datetime
from enum import Enum


class FormatType(Enum):
    """Enumeration of supported conversation formats"""
    STANDARD_JSON = "standard_json"
    COMPARISON_JSON = "comparison_json"
    PLAIN_TEXT_LOG = "plain_text_log"


class MessageRole(Enum):
    """Enumeration of message roles"""
    USER = "user"
    ASSISTANT = "assistant"
    MODEL = "model"
    SYSTEM = "system"


class ContentType(Enum):
    """Enumeration of content types within messages"""
    TEXT = "text"
    DRIVE_DOCUMENT = "drive_document"
    DRIVE_IMAGE = "drive_image"
    TOOL_USAGE = "tool_usage"
    THINKING = "thinking"
    USER_COMMAND = "user_command"
    MODEL_RESPONSE = "model_response"


@dataclass
class MessageContent:
    """Represents the content of a single message"""
    content_type: ContentType
    text: Optional[str] = None
    drive_document_id: Optional[str] = None
    drive_image_id: Optional[str] = None
    tool_name: Optional[str] = None
    tool_args: Optional[Dict[str, Any]] = None
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ConversationMessage:
    """Represents a single message in a conversation"""
    role: MessageRole
    content: List[MessageContent]
    sequence: Optional[int] = None
    timestamp: Optional[datetime] = None
    token_count: Optional[int] = None
    is_thought: bool = False
    chunk_type: Optional[str] = None
    branch_parent: Optional[str] = None
    branch_children: Optional[List[str]] = None
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ConversationThread:
    """Represents a single conversation thread"""
    thread_id: Optional[str] = None
    system_prompt: Optional[str] = None
    messages: List[ConversationMessage] = field(default_factory=list)
    run_settings: Dict[str, Any] = field(default_factory=dict)
    branch_parent: Optional[str] = None
    branch_children: Optional[List[str]] = None
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ConversationMetadata:
    """Metadata about the conversation and parsing process"""
    source_file: Optional[str] = None
    parsed_at: Optional[datetime] = None
    parser_version: Optional[str] = None
    session_info: Dict[str, Any] = field(default_factory=dict)
    run_settings: Dict[str, Any] = field(default_factory=dict)
    thread_count: int = 1
    session_boundaries: List[Dict[str, Any]] = field(default_factory=list)
    session_count: int = 1
    total_tokens: Optional[int] = None
    processing_time: Optional[float] = None
    
    def get(self, key: str, default=None):
        """Dictionary-style get method for test compatibility"""
        return getattr(self, key, default)


@dataclass
class ComparisonAnalysis:
    """Analysis data specific to comparison format conversations"""
    parameter_differences: Dict[str, Any] = field(default_factory=dict)
    response_variations: List[Dict[str, Any]] = field(default_factory=list)
    thread_comparison: Dict[str, Any] = field(default_factory=dict)
    divergence_points: List[Dict[str, Any]] = field(default_factory=list)


@dataclass
class UnifiedConversation:
    """
    Unified representation of a conversation regardless of input format.
    
    This class provides a consistent interface for accessing conversation data
    while preserving format-specific information in the format_specific_data field.
    """
    format_type: FormatType
    conversations: List[ConversationThread] = field(default_factory=list)
    system_prompt: Optional[str] = None
    metadata: ConversationMetadata = field(default_factory=ConversationMetadata)
    format_specific_data: Dict[str, Any] = field(default_factory=dict)
    
    def __post_init__(self):
        """Initialize default metadata after creation"""
        if self.metadata.parsed_at is None:
            self.metadata.parsed_at = datetime.now()
    
    def get_all_messages(self) -> List[ConversationMessage]:
        """Get all messages from all conversation threads"""
        all_messages = []
        for conversation in self.conversations:
            all_messages.extend(conversation.messages)
        return all_messages
    
    def get_messages_by_role(self, role: MessageRole) -> List[ConversationMessage]:
        """Get all messages from a specific role"""
        return [msg for msg in self.get_all_messages() if msg.role == role]
    
    def get_user_messages(self) -> List[ConversationMessage]:
        """Get all user messages"""
        return self.get_messages_by_role(MessageRole.USER)
    
    def get_assistant_messages(self) -> List[ConversationMessage]:
        """Get all assistant/model messages"""
        assistant_msgs = self.get_messages_by_role(MessageRole.ASSISTANT)
        model_msgs = self.get_messages_by_role(MessageRole.MODEL)
        return assistant_msgs + model_msgs
    
    def get_thinking_messages(self) -> List[ConversationMessage]:
        """Get all thinking/internal reasoning messages"""
        return [msg for msg in self.get_all_messages() if msg.is_thought]
    
    def calculate_total_tokens(self) -> int:
        """Calculate total token count across all messages"""
        total = 0
        for message in self.get_all_messages():
            if message.token_count:
                total += message.token_count
        return total
    
    def get_thread_by_id(self, thread_id: str) -> Optional[ConversationThread]:
        """Get a specific conversation thread by ID"""
        for conversation in self.conversations:
            if conversation.thread_id == thread_id:
                return conversation
        return None
    
    def add_conversation_thread(self, thread: ConversationThread) -> None:
        """Add a new conversation thread"""
        self.conversations.append(thread)
        self.metadata.thread_count = len(self.conversations)
    
    def get_comparison_analysis(self) -> Optional[ComparisonAnalysis]:
        """Get comparison analysis if this is a comparison format conversation"""
        if self.format_type == FormatType.COMPARISON_JSON:
            comparison_data = self.format_specific_data.get('comparison_analysis')
            if comparison_data and isinstance(comparison_data, dict):
                return ComparisonAnalysis(**comparison_data)
        return None
    
    def set_comparison_analysis(self, analysis: ComparisonAnalysis) -> None:
        """Set comparison analysis data"""
        if self.format_type == FormatType.COMPARISON_JSON:
            self.format_specific_data['comparison_analysis'] = {
                'parameter_differences': analysis.parameter_differences,
                'response_variations': analysis.response_variations,
                'thread_comparison': analysis.thread_comparison,
                'divergence_points': analysis.divergence_points
            }
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation"""
        return {
            'format_type': self.format_type.value,
            'system_prompt': self.system_prompt,
            'conversations': [
                {
                    'thread_id': conv.thread_id,
                    'system_prompt': conv.system_prompt,
                    'run_settings': conv.run_settings,
                    'messages': [
                        {
                            'role': msg.role.value,
                            'content': [
                                {
                                    'content_type': content.content_type.value,
                                    'text': content.text,
                                    'drive_document_id': content.drive_document_id,
                                    'drive_image_id': content.drive_image_id,
                                    'tool_name': content.tool_name,
                                    'tool_args': content.tool_args,
                                    'metadata': content.metadata
                                } for content in msg.content
                            ],
                            'sequence': msg.sequence,
                            'timestamp': msg.timestamp.isoformat() if msg.timestamp else None,
                            'token_count': msg.token_count,
                            'is_thought': msg.is_thought,
                            'chunk_type': msg.chunk_type,
                            'branch_parent': msg.branch_parent,
                            'branch_children': msg.branch_children,
                            'metadata': msg.metadata
                        } for msg in conv.messages
                    ],
                    'branch_parent': conv.branch_parent,
                    'branch_children': conv.branch_children,
                    'metadata': conv.metadata
                } for conv in self.conversations
            ],
            'metadata': {
                'source_file': self.metadata.source_file,
                'parsed_at': self.metadata.parsed_at.isoformat() if self.metadata.parsed_at else None,
                'parser_version': self.metadata.parser_version,
                'session_info': self.metadata.session_info,
                'run_settings': self.metadata.run_settings,
                'thread_count': self.metadata.thread_count,
                'session_boundaries': self.metadata.session_boundaries,
                'session_count': self.metadata.session_count,
                'total_tokens': self.metadata.total_tokens,
                'processing_time': self.metadata.processing_time
            },
            'format_specific_data': self.format_specific_data
        }