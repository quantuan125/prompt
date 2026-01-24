"""
Prompt Reconstructor

A debugging tool for the LLM agent framework that reads command files
and resolves @ import statements to create fully assembled prompts.

This script takes a command file path as input and outputs the complete,
reconstructed prompt that would be sent to the LLM.

Usage:
    python prompt_reconstructor.py <command_file_path>

Example:
    python prompt_reconstructor.py .claude/commands/consultant/create-request.md
"""

import argparse
import os
import sys
from pathlib import Path
import re
import json
from datetime import datetime


class OutputPathManager:
    """
    Manages output path generation and organization for reconstructed prompts.
    
    Handles smart filename generation, role detection, directory creation,
    and path sanitization following project organizational patterns.
    """
    
    def __init__(self, project_root, output_dir=None, organize_by="flat"):
        """
        Initialize the OutputPathManager.
        
        Args:
            project_root: The root directory of the project
            output_dir: Custom output directory (optional)
            organize_by: Organization mode - "flat", "role", "type" (default: "flat")
        """
        self.project_root = Path(project_root)
        self.organize_by = organize_by
        
        # Set default output directory following project patterns (NEW: prompt/scripts/output)
        self.default_output_dir = self.project_root / "prompt" / "scripts" / "output"
        
        if output_dir:
            self.custom_output_dir = Path(output_dir)
        else:
            self.custom_output_dir = None
    
    def generate_output_path(self, command_file_path, custom_file=None):
        """
        Generate output path for reconstructed prompt based on command file path.
        
        Args:
            command_file_path: Path to the source command file
            custom_file: Custom output file path (optional)
            
        Returns:
            Path object for the output file
        """
        command_file_path = Path(command_file_path)
        
        # If custom file specified, use it directly
        if custom_file:
            return Path(custom_file)
        
        # Determine output directory
        output_dir = self.custom_output_dir or self.default_output_dir
        
        # Create organized subdirectories if needed
        if self.organize_by == "role":
            role = self._detect_role(command_file_path)
            output_dir = output_dir / role
        elif self.organize_by == "type":
            file_type = self._detect_type(command_file_path)
            output_dir = output_dir / file_type
        
        # Generate smart filename
        filename = self._generate_filename(command_file_path)
        output_path = output_dir / filename
        
        # Ensure uniqueness if file exists
        if output_path.exists():
            output_path = self.generate_unique_filename(output_path)
        
        return output_path
    
    def _detect_role(self, command_file_path):
        """
        Detect role from command file path.
        
        Args:
            command_file_path: Path to analyze
            
        Returns:
            Detected role string
        """
        path_str = str(command_file_path).lower()
        
        if "consultant" in path_str:
            return "consultant"
        elif "planner" in path_str:
            return "planner"
        elif "developer" in path_str:
            return "developer"
        elif "reviewer" in path_str:
            return "reviewer"
        elif "templates" in path_str:
            return "templates"
        else:
            return "unknown"
    
    def _detect_type(self, command_file_path):
        """
        Detect file type from command file path.
        
        Args:
            command_file_path: Path to analyze
            
        Returns:
            Detected type string
        """
        path_str = str(command_file_path).lower()
        
        if "protocol" in path_str:
            return "protocols"
        elif "template" in path_str:
            return "templates"
        elif "command" in path_str:
            return "commands"
        else:
            return "general"
    
    def _generate_filename(self, command_file_path):
        """
        Generate descriptive filename from command file path.
        
        Args:
            command_file_path: Source command file path
            
        Returns:
            Generated filename string
        """
        command_file_path = Path(command_file_path)
        
        # Get command name directly from file (simplified approach - no role detection)
        command_name = command_file_path.stem
        
        # Create timestamp for uniqueness
        timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M")
        
        # Build filename: [command-name]_[timestamp]_reconstructed.md (simplified pattern)
        filename = f"{command_name}_{timestamp}_reconstructed.md"
        
        # Sanitize filename
        return self.sanitize_filename(filename)
    
    def generate_unique_filename(self, base_path):
        """
        Generate unique filename when base path already exists.
        
        Args:
            base_path: Base file path that exists
            
        Returns:
            Unique Path object
        """
        base_path = Path(base_path)
        stem = base_path.stem
        suffix = base_path.suffix
        directory = base_path.parent
        
        # Add timestamp to make unique
        timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        unique_filename = f"{stem}_{timestamp}{suffix}"
        
        return directory / unique_filename
    
    def sanitize_filename(self, filename):
        """
        Sanitize filename by replacing invalid characters.
        
        Args:
            filename: Filename to sanitize
            
        Returns:
            Sanitized filename string
        """
        # Replace invalid characters with underscores
        invalid_chars = r'[<>:"/\\|?*]'
        sanitized = re.sub(invalid_chars, '_', filename)
        
        # Replace spaces with underscores
        sanitized = sanitized.replace(' ', '_')
        
        return sanitized
    
    def ensure_output_directory(self, output_path):
        """
        Ensure output directory exists, creating it if necessary.
        
        Args:
            output_path: Path to file or directory
        """
        output_path = Path(output_path)
        
        # If it's a file path, get the directory
        if output_path.suffix:
            directory = output_path.parent
        else:
            directory = output_path
        
        # Create directory if it doesn't exist
        directory.mkdir(parents=True, exist_ok=True)


class FileOutputManager:
    """
    Manages file output operations for reconstructed prompts.
    
    Handles file writing, override modes, metadata creation,
    and error handling for file operations.
    """
    
    def __init__(self, project_root):
        """
        Initialize the FileOutputManager.
        
        Args:
            project_root: The root directory of the project
        """
        self.project_root = Path(project_root)
    
    def save_reconstructed_prompt(self, content, output_path, override_mode="confirm", 
                                 source_command=None, create_metadata=False):
        """
        Save reconstructed prompt content to file.
        
        Args:
            content: The reconstructed prompt content
            output_path: Path where to save the file
            override_mode: How to handle existing files ("confirm", "skip", "force")
            source_command: Source command file path (for metadata)
            create_metadata: Whether to create metadata file
            
        Returns:
            True if file was saved, False otherwise
        """
        output_path = Path(output_path)
        
        # Handle existing files based on override mode
        if output_path.exists():
            if override_mode == "skip":
                return False
            elif override_mode == "confirm":
                if not self._confirm_override(output_path):
                    return False
            # "force" mode continues without prompting
        
        try:
            # Ensure output directory exists
            output_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Write content to file
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            # Create metadata if requested
            if create_metadata and source_command:
                self._create_metadata_file(output_path, source_command)
            
            return True
            
        except (PermissionError, IOError, OSError) as e:
            print(f"Error saving file to {output_path}: {e}")
            return False
    
    def _confirm_override(self, output_path):
        """
        Prompt user to confirm file override.
        
        Args:
            output_path: Path of existing file
            
        Returns:
            True if user confirms override, False otherwise
        """
        response = input(f"File {output_path} exists. Overwrite? (y/n): ").lower().strip()
        return response in ['y', 'yes']
    
    def _create_metadata_file(self, output_path, source_command):
        """
        Create metadata file alongside output file.
        
        Args:
            output_path: Path to the output file
            source_command: Source command file path
        """
        metadata_path = output_path.with_suffix('.metadata.json')
        
        metadata = {
            "source_command": str(source_command),
            "output_path": str(output_path),
            "created_date": datetime.now().isoformat(),
            "file_size": output_path.stat().st_size,
            "reconstructor_version": "2.0.0"  # Version with file output
        }
        
        try:
            with open(metadata_path, 'w', encoding='utf-8') as f:
                json.dump(metadata, f, indent=2)
        except (PermissionError, IOError, OSError) as e:
            print(f"Warning: Could not create metadata file: {e}")


class PromptReconstructor:
    """
    Reconstructs LLM prompts by resolving @ import statements in command files.
    
    This class provides the core functionality for reading command files,
    identifying import statements, loading referenced files, and assembling
    the complete prompt with proper formatting.
    """
    
    def __init__(self, project_root=None, output_dir=None, organize_by="flat"):
        """
        Initialize the PromptReconstructor.
        
        Args:
            project_root: The root directory of the project. If None, 
                         attempts to auto-detect from current working directory.
            output_dir: Custom output directory for file output (optional)
            organize_by: Organization mode for output files (default: "flat")
        """
        if project_root is None:
            self.project_root = Path.cwd()
        else:
            self.project_root = Path(project_root)
        
        # Initialize file output managers
        self.path_manager = OutputPathManager(self.project_root, output_dir, organize_by)
        self.file_manager = FileOutputManager(self.project_root)
    
    def reconstruct_prompt(self, command_file_path):
        """
        Reads a command file, resolves all @ import statements recursively,
        and returns the fully assembled prompt as a single string with debug formatting.

        Args:
            command_file_path: The path to the root command file.

        Returns:
            The fully reconstructed prompt string with debug formatting.
        """
        command_file_path = Path(command_file_path)
        
        if not command_file_path.exists():
            return f"FATAL ERROR: Command file not found at '{command_file_path}'"

        try:
            # Read the root command file content
            with open(command_file_path, 'r', encoding='utf-8') as f:
                root_content = f.read()
            
            # Process all imports recursively with debug formatting
            return self._process_imports_recursively(root_content, format_debug=True)

        except Exception as e:
            return f"FATAL ERROR: An unexpected error occurred: {e}"
    
    def reconstruct_clean_prompt(self, command_file_path):
        """
        Reads a command file, resolves all @ import statements recursively,
        and returns the fully assembled prompt as clean markdown without debug formatting.

        Args:
            command_file_path: The path to the root command file.

        Returns:
            The fully reconstructed prompt string without debug separators and annotations.
        """
        command_file_path = Path(command_file_path)
        
        if not command_file_path.exists():
            return f"FATAL ERROR: Command file not found at '{command_file_path}'"

        try:
            # Read the root command file content
            with open(command_file_path, 'r', encoding='utf-8') as f:
                root_content = f.read()
            
            # Process all imports recursively without debug formatting
            return self._process_imports_recursively(root_content, format_debug=False)

        except Exception as e:
            return f"FATAL ERROR: An unexpected error occurred: {e}"
    
    def reconstruct_and_save(self, command_file_path, output_file=None, output_dir=None, 
                           override_mode="confirm", create_metadata=False, no_stdout=True):
        """
        Reconstruct prompt and save to file with comprehensive options.
        
        Args:
            command_file_path: Path to the command file to reconstruct
            output_file: Custom output file path (optional)
            output_dir: Custom output directory (optional)
            override_mode: How to handle existing files ("confirm", "skip", "force")
            create_metadata: Whether to create metadata file
            no_stdout: If True, suppress stdout output (DEFAULT: True - silent by default)
            
        Returns:
            Path to output file if saved successfully, None otherwise
        """
        # Reconstruct the prompt using clean format for file output (no debug formatting)
        reconstructed_content = self.reconstruct_clean_prompt(command_file_path)
        
        # Generate output path
        if output_file:
            output_path = Path(output_file)
        else:
            # Update path manager if custom output directory provided
            if output_dir:
                self.path_manager.custom_output_dir = Path(output_dir)
            
            output_path = self.path_manager.generate_output_path(
                command_file_path, custom_file=output_file
            )
        
        # Ensure output directory exists
        self.path_manager.ensure_output_directory(output_path)
        
        # Save the reconstructed content
        success = self.file_manager.save_reconstructed_prompt(
            reconstructed_content, 
            output_path, 
            override_mode=override_mode,
            source_command=command_file_path,
            create_metadata=create_metadata
        )
        
        if success:
            if not no_stdout:
                print(f"Reconstructed prompt saved to: {output_path}")
            return output_path
        else:
            if not no_stdout:
                print(f"Failed to save reconstructed prompt to: {output_path}")
            return None
    
    def _is_import_line(self, line):
        """
        Check if a line is an import statement (starts with @).
        
        Args:
            line: The line to check.
            
        Returns:
            True if the line is an import statement, False otherwise.
        """
        return line.strip().startswith('@')
    
    def _is_commented_import(self, line):
        """
        Check if an import line is commented out using HTML comment syntax.
        
        Args:
            line: The line to check.
            
        Returns:
            True if the import is commented out, False otherwise.
        """
        # Check for HTML comment style: <!-- ... -->
        return '<!--' in line and '@' in line and '-->' in line
    
    def _parse_import_line(self, line):
        """
        Parse an import line to extract the import path.
        
        Args:
            line: The line containing the import statement.
            
        Returns:
            The import path without the @ symbol, or None if not a valid import.
        """
        stripped = line.strip()
        if stripped.startswith('@'):
            return stripped[1:].strip()  # Remove @ and any whitespace
        return None
    
    def _load_import_file(self, import_path):
        """
        Load the content of an import file.
        
        Args:
            import_path: The relative path to the import file.
            
        Returns:
            The content of the file, or an error message if file not found.
        """
        import_path_full = self.project_root / import_path
        
        try:
            with open(import_path_full, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            return f"!!! IMPORT ERROR: File not found at '{import_path_full}' !!!"
        except Exception as e:
            return f"!!! IMPORT ERROR: Failed to read file '{import_path_full}': {e} !!!"
    
    def _process_imports_recursively(self, content, visited_files=None, depth=0, max_depth=10, format_debug=True):
        """
        Recursively process all @ import statements in content, with circular import detection.
        
        Args:
            content: The content to process for imports
            visited_files: Set of already processed files to prevent circular imports
            depth: Current recursion depth
            max_depth: Maximum recursion depth allowed (default: 10)
            format_debug: Whether to include debug formatting (for reconstruct_prompt)
            
        Returns:
            Content with all nested imports resolved
        """
        if visited_files is None:
            visited_files = set()
        
        if depth > max_depth:
            return content + f"\n!!! IMPORT ERROR: Maximum import depth ({max_depth}) exceeded !!!\n"
        
        lines = content.split('\n')
        processed_lines = []
        
        for line in lines:
            stripped_line = line.strip()
            
            # Check for an active (not commented out) import statement
            if self._is_import_line(stripped_line) and not self._is_commented_import(line):
                import_path_relative = self._parse_import_line(stripped_line)
                if import_path_relative:
                    import_path_full = self.project_root / import_path_relative
                    import_path_str = str(import_path_full)
                    
                    # Check for circular imports
                    if import_path_str in visited_files:
                        error_msg = f"!!! IMPORT ERROR: Circular import detected for '{import_path_relative}' !!!"
                        if format_debug:
                            processed_lines.append(self._format_import_section(import_path_relative, error_msg))
                        else:
                            processed_lines.append(error_msg)
                        continue
                    
                    # Add to visited files and load content
                    visited_files.add(import_path_str)
                    import_content = self._load_import_file(import_path_relative)
                    
                    # If successful load, recursively process the imported content
                    if not import_content.startswith("!!! IMPORT ERROR"):
                        # Recursively process imports within the imported content
                        processed_import_content = self._process_imports_recursively(
                            import_content, 
                            visited_files.copy(),  # Use copy to allow different branches
                            depth + 1, 
                            max_depth, 
                            format_debug
                        )
                        
                        # Format and add the processed import section
                        if format_debug:
                            formatted_section = self._format_import_section(import_path_relative, processed_import_content)
                            processed_lines.append(formatted_section)
                        else:
                            # For clean mode, just add the content directly
                            processed_lines.append(processed_import_content)
                    else:
                        # Error loading file - add error message
                        if format_debug:
                            formatted_section = self._format_import_section(import_path_relative, import_content)
                            processed_lines.append(formatted_section)
                        else:
                            processed_lines.append(import_content)
                    
                    # Remove from visited files after processing this branch
                    visited_files.discard(import_path_str)
            
            # Handle commented out imports and other comments - keep them for context
            elif self._is_commented_import(line):
                processed_lines.append(line)
            
            # Keep blank lines for readability
            elif not stripped_line:
                processed_lines.append('')
            
            # Regular content lines
            else:
                processed_lines.append(line)
        
        return '\n'.join(processed_lines)
    
    def get_file_size(self, file_path):
        """
        Get the size of a file in bytes.
        
        Args:
            file_path: Path to the file
            
        Returns:
            Size in bytes, or None if file doesn't exist
        """
        try:
            return Path(file_path).stat().st_size
        except (FileNotFoundError, OSError):
            return None
    
    def get_reconstructed_content_size(self, command_file_path):
        """
        Get the size of reconstructed content in bytes.
        
        Args:
            command_file_path: Path to the command file to reconstruct
            
        Returns:
            Size of fully reconstructed content in bytes, or None if file doesn't exist
        """
        try:
            reconstructed_content = self.reconstruct_clean_prompt(command_file_path)
            if reconstructed_content.startswith("FATAL ERROR:"):
                return None
            return len(reconstructed_content.encode('utf-8'))
        except Exception:
            return None
    
    def _format_import_section(self, import_path, content):
        """
        Format an import section with proper separators and labels.
        
        Args:
            import_path: The path of the imported file.
            content: The content of the imported file.
            
        Returns:
            The formatted import section.
        """
        separator_line = "-" * 80
        
        formatted_parts = [
            f"\n{separator_line}\n",
            f"--- [START] Imported from: {import_path} ---\n",
            f"{separator_line}\n\n",
            content,
            f"\n\n{separator_line}\n",
            f"--- [END] Imported from: {import_path} ---\n",
            f"{separator_line}\n"
        ]
        
        return "".join(formatted_parts)


def main():
    """
    Main entry point for the command-line interface.
    
    Returns:
        Exit code: 0 for success, non-zero for failure.
    """
    parser = argparse.ArgumentParser(
        description="Reconstructs a final LLM prompt from a command file by resolving all '@' imports.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Reconstruct a consultant command
  python prompt_reconstructor.py .claude/commands/consultant/create-request.md
  
  # Reconstruct any command file
  python prompt_reconstructor.py path/to/command.md
        """
    )
    
    parser.add_argument(
        "command_file",
        nargs='?',
        help="Path to the command file to reconstruct (e.g., '.claude/commands/consultant/create-request.md')."
    )
    
    # File output options
    parser.add_argument(
        "--output-file", "-o",
        help="Custom output file path (e.g., 'custom/output.md')"
    )
    
    parser.add_argument(
        "--output-dir",
        help="Custom output directory (default: prompt/artifacts/reconstructed)"
    )
    
    parser.add_argument(
        "--override-mode",
        choices=["confirm", "skip", "force"],
        default="confirm",
        help="How to handle existing files (default: confirm)"
    )
    
    parser.add_argument(
        "--organize-by",
        choices=["flat", "role", "type"],
        default="flat",
        help="Output organization mode (default: flat)"
    )
    
    parser.add_argument(
        "--create-metadata",
        action="store_true",
        help="Create metadata file alongside output"
    )
    
    parser.add_argument(
        "--no-stdout",
        action="store_true",
        help="Suppress stdout output (file output only) - DEPRECATED: Use default behavior instead"
    )
    
    parser.add_argument(
        "--with-stdout",
        action="store_true",
        help="Show terminal output when saving to file (new flag for explicit stdout)"
    )
    
    parser.add_argument(
        "--save",
        action="store_true",
        help="Save to file (silent by default, use --with-stdout for terminal output)"
    )
    
    # Handle missing arguments
    if len(sys.argv) == 1:
        parser.print_help()
        return 1
    
    try:
        args = parser.parse_args()
        
        # Create reconstructor with enhanced options
        reconstructor = PromptReconstructor(
            output_dir=args.output_dir,
            organize_by=args.organize_by
        )
        
        # Determine if file output is requested (FIXED: removed problematic override_mode condition)
        save_to_file = (args.save or args.output_file or args.output_dir or 
                       args.create_metadata or args.no_stdout)
        
        if save_to_file:
            # Use file output mode (NEW: silent by default)
            output_path = reconstructor.reconstruct_and_save(
                args.command_file,
                output_file=args.output_file,
                output_dir=args.output_dir,
                override_mode=args.override_mode,
                create_metadata=args.create_metadata,
                no_stdout=True  # Always silent during file save itself
            )
            
            # NEW BEHAVIOR: Only output to stdout if explicitly requested with --with-stdout
            # (--no-stdout is kept for backward compatibility but is now redundant)
            if args.with_stdout:
                result = reconstructor.reconstruct_prompt(args.command_file)
                sys.stdout.write(result)
                
        else:
            # Default behavior: stdout only (no file output)
            result = reconstructor.reconstruct_prompt(args.command_file)
            sys.stdout.write(result)
        
        return 0
        
    except SystemExit as e:
        # Handle argparse SystemExit (help, version, etc.)
        return e.code if e.code is not None else 1
    except Exception as e:
        sys.stderr.write(f"Error: {e}\n")
        return 1


if __name__ == "__main__":
    sys.exit(main())