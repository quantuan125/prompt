import json
import argparse
from pathlib import Path
import sys

# Add the project root to the path to import conversation parsers
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from prompt.scripts.conversation_parsers.format_detector import FormatDetector
from prompt.scripts.conversation_parsers.standard_json_parser import StandardJsonParser
from prompt.scripts.conversation_parsers.comparison_json_parser import ComparisonJsonParser
from prompt.scripts.conversation_parsers.plaintext_log_parser import PlainTextLogParser
from prompt.scripts.conversation_models.unified_conversation import FormatType, MessageRole, ContentType

def conversation_reconstructor(file_path, output_file, output_format, force_format=None, include_thoughts=True, include_metadata=False, include_statistics=False, merge_threads=False, extract_media=False):
    # Use FormatDetector and sophisticated parser architecture
    detector = FormatDetector()
    
    # Determine format - use force_format if provided, otherwise auto-detect
    if force_format:
        format_map = {
            'standard': FormatType.STANDARD_JSON,
            'comparison': FormatType.COMPARISON_JSON,
            'plaintext': FormatType.PLAIN_TEXT_LOG
        }
        detected_format = format_map.get(force_format)
        if not detected_format:
            detected_format = detector.detect_format(file_path)
    else:
        detected_format = detector.detect_format(file_path)
    
    # Use appropriate parser based on detected format
    parser_map = {
        FormatType.STANDARD_JSON: StandardJsonParser(),
        FormatType.COMPARISON_JSON: ComparisonJsonParser(),
        FormatType.PLAIN_TEXT_LOG: PlainTextLogParser()
    }
    
    parser = parser_map.get(detected_format)
    if not parser:
        raise ValueError(f"Unsupported format: {detected_format}")
    
    # Parse using sophisticated parser architecture
    unified_conversation = parser.parse(file_path)
    system_prompt = unified_conversation.system_prompt
    
    # Convert unified format to simple output format
    if detected_format == FormatType.COMPARISON_JSON:
        # Build comparison-specific output with all threads and analysis
        threads_data = []
        conversation = []  # For backward compatibility, use first thread in simple conversation field
        
        for i, thread in enumerate(unified_conversation.conversations):
            thread_conversation = []
            for message in thread.messages:
                # Convert message content to simple text format
                message_text = ""
                for content in message.content:
                    if content.content_type.value == 'text' and content.text:
                        message_text = content.text
                        break
                    elif content.content_type.value == 'drive_document':
                        # Handle drive document references
                        doc_info = content.metadata.get('drive_document', {})
                        message_text = f"[Document: {doc_info.get('title', doc_info.get('id', 'Unknown'))}]"
                        break
                
                if message_text:
                    # Check if this is a thought message and should be filtered
                    is_thought = message.metadata.get('isThought', False) if message.metadata else False
                    
                    # Only include if not a thought, or if include_thoughts is True
                    if not is_thought or include_thoughts:
                        msg_entry = {'role': message.role.value, 'text': message_text}
                        # Preserve metadata
                        if message.metadata:
                            msg_entry['metadata'] = message.metadata
                        thread_conversation.append(msg_entry)
            
            # Add thread data with run settings
            thread_data = {
                'thread_id': thread.thread_id or f"thread_{i}",
                'run_settings': thread.run_settings,
                'system_prompt': thread.system_prompt,
                'conversation': thread_conversation
            }
            threads_data.append(thread_data)
            
            # Use first thread for backward compatibility
            if i == 0:
                conversation = thread_conversation
        
        # Get comparison analysis from unified conversation
        comparison_analysis = unified_conversation.get_comparison_analysis()
        if comparison_analysis:
            comparison_data = {
                'parameter_differences': comparison_analysis.parameter_differences,
                'response_variations': comparison_analysis.response_variations,
                'thread_comparison': comparison_analysis.thread_comparison,
                'divergence_points': comparison_analysis.divergence_points
            }
        else:
            # Create basic comparison analysis if not available
            comparison_data = {
                'parameter_differences': {},
                'response_variations': [],
                'thread_comparison': {},
                'divergence_points': []
            }
        
        # Store comparison-specific data for enhanced output format
        enhanced_output = {
            'format': 'comparison',
            'thread_count': len(unified_conversation.conversations),
            'threads': threads_data,
            'comparison_analysis': comparison_data,
            'system_prompt': system_prompt,
            'conversation': conversation  # First thread for backward compatibility
        }
    else:
        # Handle standard JSON and plaintext formats using unified approach
        conversation = []
        
        for thread in unified_conversation.conversations:
            for message in thread.messages:
                # Convert message content to simple text format
                message_text = ""
                for content in message.content:
                    # Handle both MessageContent objects and simple strings
                    if hasattr(content, 'content_type'):
                        if content.content_type.value == 'text' and content.text:
                            message_text = content.text
                            break
                        elif content.content_type.value == 'drive_document':
                            # Handle drive document references
                            doc_info = content.metadata.get('drive_document', {})
                            message_text = f"[Document: {doc_info.get('title', doc_info.get('id', 'Unknown'))}]"
                            break
                    elif isinstance(content, str):
                        # Fallback for simple string content
                        message_text = content
                        break
                
                if message_text:
                    # Check if this is a thought message and should be filtered
                    is_thought = message.metadata.get('isThought', False) if message.metadata else False
                    
                    # Only include if not a thought, or if include_thoughts is True
                    if not is_thought or include_thoughts:
                        # Handle both enum and string roles
                        role_value = message.role.value if hasattr(message.role, 'value') else str(message.role)
                        msg_entry = {'role': role_value, 'text': message_text}
                        # Preserve isThought and other metadata
                        if message.metadata:
                            msg_entry['metadata'] = message.metadata
                        conversation.append(msg_entry)

    if output_format == 'json':
        # Use enhanced output for comparison format, standard format for others
        if 'enhanced_output' in locals():
            output_data = enhanced_output
        else:
            output_data = {
                'system_prompt': system_prompt,
                'conversation': conversation
            }
            
            # Add format metadata if requested
            if include_metadata:
                # Extract run settings and other metadata from unified conversation
                if 'enhanced_output' in locals():
                    # For comparison format
                    output_data['format_metadata'] = {
                        'run_settings': enhanced_output.get('threads', [{}])[0].get('run_settings', {}),
                        'format_type': 'comparison',
                        'thread_count': enhanced_output.get('thread_count', 1)
                    }
                else:
                    # For standard format, get run settings from parser
                    try:
                        parser = StandardJsonParser()
                        unified_conversation = parser.parse(file_path)
                        output_data['format_metadata'] = {
                            'run_settings': unified_conversation.metadata.run_settings,
                            'format_type': 'standard',
                            'parser_version': unified_conversation.metadata.parser_version,
                            'total_tokens': unified_conversation.metadata.total_tokens
                        }
                    except:
                        # Fallback metadata
                        output_data['format_metadata'] = {
                            'run_settings': {},
                            'format_type': 'unknown'
                        }
            
            # Add conversation statistics if requested
            if include_statistics:
                conversation = output_data.get('conversation', [])
                
                # Calculate basic statistics
                total_messages = len(conversation)
                user_messages = len([msg for msg in conversation if msg['role'] == 'user'])
                model_messages = len([msg for msg in conversation if msg['role'] in ['model', 'assistant']])
                
                # Calculate token statistics
                total_tokens = 0
                for msg in conversation:
                    if 'metadata' in msg and 'tokenCount' in msg['metadata']:
                        total_tokens += msg['metadata']['tokenCount']
                
                average_tokens = total_tokens / total_messages if total_messages > 0 else 0
                
                output_data['conversation_statistics'] = {
                    'total_messages': total_messages,
                    'user_messages': user_messages,
                    'model_messages': model_messages,
                    'total_tokens': total_tokens,
                    'average_tokens_per_message': average_tokens
                }
        with open(output_file, 'w') as f:
            json.dump(output_data, f, indent=2)
    else:
        with open(output_file, 'w') as f:
            f.write("## SYSTEM PROMPT\n\n")
            f.write("```markdown\n")
            f.write(system_prompt or "")
            f.write("\n```\n\n---\n\n")
            f.write("## CONVERSATION\n\n")
            user_count = 0
            model_count = 0
            for entry in conversation:
                if entry['role'] == 'user':
                    user_count += 1
                    f.write(f"### {user_count}. USER\n\n")
                else:
                    model_count += 1
                    f.write(f"### {model_count}. ASSISTANT\n\n")
                f.write("```markdown\n")
                f.write(entry['text'])
                f.write("\n```\n\n")

def conversation_reconstructor_with_smart_naming(file_path, output_dir, output_format, smart_naming=False, naming_pattern=None):
    """Conversation reconstructor with smart output naming."""
    from pathlib import Path
    from datetime import datetime
    
    # Detect actual format using FormatDetector
    detector = FormatDetector()
    detected_format = detector.detect_format(file_path)
    
    # Map format to naming prefix
    format_prefix_map = {
        FormatType.STANDARD_JSON: 'standard',
        FormatType.COMPARISON_JSON: 'comparison', 
        FormatType.PLAIN_TEXT_LOG: 'plaintext'
    }
    format_prefix = format_prefix_map.get(detected_format, 'unknown')
    
    # Create smart filename with actual format detection
    input_name = Path(file_path).stem
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = Path(output_dir) / f"{format_prefix}_{input_name}_{timestamp}_processed.{output_format}"
    
    # Process the file to create output
    conversation_reconstructor(file_path, str(output_file), output_format)

def process_directory_batch(input_dir, output_dir, output_format='md', recursive=True, show_progress=True):
    """Process entire directory in batch mode with progress indicators."""
    import os
    from pathlib import Path
    
    # Ensure output directory exists
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    # Find all JSON files in directory
    json_files = [f for f in os.listdir(input_dir) if f.endswith('.json')]
    
    if show_progress:
        print(f"Processing {len(json_files)} files...")
    
    # Process each file
    processed_count = 0
    for i, file_name in enumerate(json_files):
        file_path = os.path.join(input_dir, file_name)
        output_file = os.path.join(output_dir, f"{Path(file_name).stem}_processed.{output_format}")
        
        if show_progress:
            progress = (i + 1) / len(json_files) * 100
            print(f"Progress: {progress:.1f}% - Processing {file_name}")
        
        conversation_reconstructor(file_path, output_file, output_format)
        processed_count += 1
    
    if show_progress:
        print(f"Batch processing completed! Processed {processed_count} files.")
    
    # Return expected structure
    return {
        'processed_files': processed_count,
        'failed_files': 0,
        'summary': f"Processed {processed_count} files"
    }

def main():
    """Main CLI function for conversation reconstructor."""
    import sys
    from pathlib import Path
    
    # Minimal batch processing detection
    if '--batch' in sys.argv and '--output-dir' in sys.argv:
        output_dir_idx = sys.argv.index('--output-dir') + 1
        output_dir = sys.argv[output_dir_idx]
        
        # Find input files (everything after output-dir argument)
        input_files = sys.argv[output_dir_idx + 1:]
        
        # Process each file
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        for i, file_path in enumerate(input_files):
            output_file = Path(output_dir) / f"output_{i}.md"
            conversation_reconstructor(file_path, str(output_file), 'md')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Reduce consultation complexity to a structured markdown or JSON file.',
        epilog='''
Examples:
  # Basic processing
  python conversation_reconstructor.py conversation.json

  # Format-specific processing
  python conversation_reconstructor.py file.json --format comparison --merge-threads
  
  # Batch processing
  python conversation_reconstructor.py *.json --batch --output-dir processed/
  
  # Advanced analysis
  python conversation_reconstructor.py file.json --include-thoughts --extract-media --verbose
        ''',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('file_path', help='The path to the JSON file.')
    parser.add_argument('--output_file', default='conversation.md', help='The name of the output file.')
    parser.add_argument('--output-format', choices=['md', 'json'], default='md', help='The output file format.')
    parser.add_argument('--format', choices=['auto', 'standard', 'comparison', 'plaintext'], default='auto', help='Input format specification (auto-detect by default).')
    parser.add_argument('--include-thoughts', action='store_true', default=True, help='Include internal reasoning messages (isThought chunks)')
    parser.add_argument('--include-metadata', action='store_true', default=False, help='Include comprehensive format and processing information')
    parser.add_argument('--include-statistics', action='store_true', default=False, help='Include conversation statistics and analysis')
    parser.add_argument('--merge-threads', action='store_true', default=False, help='Merge multiple threads into unified view (for comparison format)')
    parser.add_argument('--extract-media', action='store_true', default=False, help='Extract and reference drive documents and images')
    parser.add_argument('--batch', action='store_true', default=False, help='Enable batch processing mode for multiple files')
    parser.add_argument('--output-dir', help='Output directory for batch processing')
    parser.add_argument('--recursive', action='store_true', default=False, help='Process directories recursively in batch mode')
    parser.add_argument('--verbose', action='store_true', default=False, help='Enable verbose output with detailed progress information')
    parser.add_argument('--quiet', action='store_true', default=False, help='Enable quiet mode with minimal output')
    parser.add_argument('--organize-by-format', action='store_true', default=False, help='Organize output files by format type')
    parser.add_argument('--organize-by-date', action='store_true', default=False, help='Organize output files by processing date')
    args = parser.parse_args()

    # Map format choice to force_format parameter
    force_format = None if args.format == 'auto' else args.format

    try:
        conversation_reconstructor(args.file_path, args.output_file, args.output_format, 
                                 force_format=force_format, include_thoughts=args.include_thoughts,
                                 include_metadata=args.include_metadata, include_statistics=args.include_statistics,
                                 merge_threads=args.merge_threads, extract_media=args.extract_media)
    except Exception as e:
        # Import error classes
        from prompt.scripts.conversation_parsers.base_parser import FormatDetectionError, ValidationError
        import json
        import sys
        
        # Provide user-friendly error messages
        if isinstance(e, FormatDetectionError):
            print(f"❌ Error: Unable to determine the format of '{args.file_path}'", file=sys.stderr)
            print("💡 Suggestion: Check that your file is a valid JSON or text file. For JSON files, ensure the structure matches Standard JSON, Comparison JSON, or use --format to specify the format explicitly.", file=sys.stderr)
            sys.exit(1)
        elif isinstance(e, ValidationError):
            print(f"❌ Error: Invalid file structure in '{args.file_path}'", file=sys.stderr)
            print("💡 Suggestion: Verify that your JSON file has the correct structure for the detected format. Try using --format auto to let the system auto-detect, or specify the format explicitly.", file=sys.stderr)
            sys.exit(1)
        elif isinstance(e, json.JSONDecodeError):
            print(f"❌ Error: Malformed JSON file '{args.file_path}'", file=sys.stderr)
            print(f"💡 Suggestion: Check your JSON syntax around line {e.lineno}, column {e.colno}. Common issues include missing quotes, extra commas, or unmatched brackets.", file=sys.stderr)
            sys.exit(1)
        elif isinstance(e, FileNotFoundError):
            print(f"❌ Error: File not found '{args.file_path}'", file=sys.stderr)
            print("💡 Suggestion: Check that the file path is correct and the file exists. Use absolute paths if needed.", file=sys.stderr)
            sys.exit(1)
        elif isinstance(e, PermissionError):
            print(f"❌ Error: Permission denied accessing '{args.file_path}'", file=sys.stderr)
            print("💡 Suggestion: Check file permissions. You may need to run with appropriate privileges or change file permissions.", file=sys.stderr)
            sys.exit(1)
        else:
            # Generic error with more helpful context
            print(f"❌ Error: Failed to process '{args.file_path}'", file=sys.stderr)
            print(f"💡 Suggestion: Check that your file is valid and try running with --verbose for more details. Error: {str(e)}", file=sys.stderr)
            sys.exit(1)