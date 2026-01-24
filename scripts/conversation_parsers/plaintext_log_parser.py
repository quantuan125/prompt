"""
Plain Text Log Parser

This module handles parsing of Claude Code conversation logs and plain text
conversation formats, extracting structured conversation data.
"""

from .base_parser import BaseParser
from ..conversation_models.unified_conversation import (
    FormatType, UnifiedConversation, ConversationMetadata, ConversationThread, ConversationMessage
)

class PlainTextLogParser(BaseParser):
    """
    Parser for plain text conversation logs, particularly Claude Code conversation logs.
    """
    
    def detect_format(self, file_path: str) -> FormatType:
        """Detect if the file is a plain text log format."""
        return FormatType.PLAIN_TEXT_LOG
    
    def parse(self, file_path: str):
        """Parse a plain text log file."""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        metadata = self._extract_welcome_banner(content)
        user_messages = self._extract_user_commands(content)
        thinking_messages = self._extract_thinking_sections(content)
        messages = user_messages + thinking_messages
        conversations = [ConversationThread(
            thread_id="main_thread",
            system_prompt="",
            messages=messages
        )]
        
        return UnifiedConversation(
            format_type=FormatType.PLAIN_TEXT_LOG,
            metadata=metadata,
            system_prompt="",
            conversations=conversations,
            format_specific_data={}
        )
    
    def _extract_welcome_banner(self, content: str) -> ConversationMetadata:
        """Extract session info from welcome banner."""
        import re
        from datetime import datetime
        
        metadata = ConversationMetadata()
        session_info = {}
        
        # Look for "Welcome to Claude Code" in the content
        if "Welcome to Claude Code" in content:
            session_info['version'] = 'Claude Code'
            session_info['timestamp'] = datetime.now().isoformat()
        
        metadata.session_info = session_info
        return metadata
    
    def _extract_user_commands(self, content: str):
        """Extract user commands from content."""
        messages = []
        lines = content.split('\n')
        
        for i, line in enumerate(lines):
            if line.strip().startswith('>'):
                # Extract user command - preserve > indicator
                command_text = line.strip()  # Keep full line with > prefix
                message = ConversationMessage(
                    role='user',
                    content=command_text,
                    sequence=len(messages)
                )
                message.content_type = 'user_command'
                messages.append(message)
        
        return messages
    
    def _extract_thinking_sections(self, content: str):
        """Extract thinking sections from content."""
        messages = []
        lines = content.split('\n')
        
        for i, line in enumerate(lines):
            if line.strip().startswith('✻ Thinking'):
                # Extract thinking section
                message = ConversationMessage(
                    role='assistant',
                    content=line.strip(),
                    sequence=len(messages),
                    is_thought=True
                )
                message.content_type = 'thinking'
                messages.append(message)
            elif line.strip().startswith('●'):
                # Extract assistant response (for todo content)
                message = ConversationMessage(
                    role='assistant',
                    content=line.strip(),
                    sequence=len(messages)
                )
                message.content_type = 'model_response'
                messages.append(message)
            elif '⎿' in line.strip():
                # Extract tool usage
                message = ConversationMessage(
                    role='assistant',
                    content=line.strip(),
                    sequence=len(messages)
                )
                message.content_type = 'tool_usage'
                messages.append(message)
        
        return messages
    
    def validate(self, data) -> bool:
        """Validate plain text content."""
        if isinstance(data, bytes):
            try:
                data.decode('utf-8')
            except UnicodeDecodeError:
                return False
        
        if not isinstance(data, str):
            return False
            
        if not data.strip():
            return False
            
        return True