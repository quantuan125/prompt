"""Conversation Models Module

This module provides unified data structures for representing conversations
across different input formats.
"""

from .unified_conversation import (
    FormatType,
    MessageRole,
    ContentType,
    MessageContent,
    ConversationMessage,
    ConversationThread,
    ConversationMetadata,
    ComparisonAnalysis,
    UnifiedConversation
)

__all__ = [
    'FormatType',
    'MessageRole', 
    'ContentType',
    'MessageContent',
    'ConversationMessage',
    'ConversationThread',
    'ConversationMetadata',
    'ComparisonAnalysis',
    'UnifiedConversation'
]