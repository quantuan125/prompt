#!/usr/bin/env python
"""
Deep Research Markdown Cleaner

Cleans markdown files exported from ChatGPT Deep Research via word2md conversion.
Removes conversion artifacts, normalizes citations, and consolidates sources.

Usage:
    # Clean default exemplar files
    python scripts/general/markdown_cleaner_deep_research.py

    # Clean specific files
    python scripts/general/markdown_cleaner_deep_research.py path/to/file1.md path/to/file2.md

Output:
    Creates *_CLEAN.md files in same directory as originals
    Never overwrites original files

TDD Approach:
    This script is developed using strict Test-Driven Development
    All functions implemented incrementally with Red-Green-Refactor cycles
"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional
import argparse
import html
import re


# ============================================================================
# PHASE 2: Core Data Structures
# ============================================================================

@dataclass
class Reference:
    """Represents a single reference/citation."""
    number: Optional[int]
    url: str
    title_hint: Optional[str] = None
    context: Optional[str] = None

    def __eq__(self, other):
        if not isinstance(other, Reference):
            return NotImplemented
        return self.url == other.url

    def __hash__(self):
        return hash(self.url)


@dataclass
class ReferenceRegistry:
    """Registry of all references found in a document."""
    by_number: dict[int, list[Reference]] = field(default_factory=dict)
    unindexed: list[Reference] = field(default_factory=list)


# ============================================================================
# PHASE 3: Helper Functions
# ============================================================================

def split_frontmatter(text: str) -> tuple[Optional[str], str]:
    """
    Split YAML frontmatter from markdown body.

    Args:
        text: Full markdown document text

    Returns:
        Tuple of (frontmatter including delimiters, body text)
        If no frontmatter, returns (None, original text)
    """
    # Check if text starts with frontmatter delimiter
    if not text.startswith("---\n"):
        return None, text

    # Find the closing delimiter (second occurrence of "---\n")
    end_index = text.find("---\n", 4)  # Start search after first "---\n"

    if end_index == -1:
        # No closing delimiter found
        return None, text

    # Extract frontmatter (including delimiters) and body
    frontmatter = text[:end_index + 4]  # Include the closing "---\n"
    body = text[end_index + 4:].lstrip("\n")  # Skip closing delimiter and trim leading newlines

    return frontmatter, body


def decode_entities_and_html(text: str) -> str:
    """
    Decode HTML entities to their plain text equivalents.

    Args:
        text: Text containing HTML entities

    Returns:
        Text with entities decoded
    """
    return html.unescape(text)


def extract_references(text: str) -> tuple[str, ReferenceRegistry]:
    """
    Extract all reference citations from markdown text and replace them.

    Finds numbered citations like [\[n\]](url), italic variants [_\[n\]_](url),
    descriptive links [label](url), and bare URLs.

    Args:
        text: Markdown text to extract references from

    Returns:
        Tuple of (modified body with replacements, ReferenceRegistry)
    """
    registry = ReferenceRegistry()
    body = text

    # Pattern for numbered citations: [\[1\]](url) and italic variant [_\[1\]_](url)
    numbered_pattern = r'\[_?\\?\[(\d+)\\?\]_?\]\(([^)]+)\)'

    for match in re.finditer(numbered_pattern, text):
        number = int(match.group(1))
        url = match.group(2).strip()

        ref = Reference(number=number, url=url)

        if number not in registry.by_number:
            registry.by_number[number] = []
        registry.by_number[number].append(ref)

        # Replace the full citation with just [n]
        body = body.replace(match.group(0), f'[{number}]')

    # Pattern for descriptive links: [label](url) - but not [n] or [\[n\]]
    # Process after numbered citations so [n] won't match
    descriptive_pattern = r'\[([^\[\]\d][^\[\]]*)\]\(([^)]+)\)'

    for match in re.finditer(descriptive_pattern, body):
        label = match.group(1).strip()
        url = match.group(2).strip()

        ref = Reference(number=None, url=url, title_hint=label)
        registry.unindexed.append(ref)

        # Replace [label](url) with just label
        body = body.replace(match.group(0), label)

    # Pattern for bare autolinks: <http...>
    autolink_pattern = r'<(https?://[^>]+)>'

    for match in re.finditer(autolink_pattern, body):
        url = match.group(1).strip()

        ref = Reference(number=None, url=url)
        registry.unindexed.append(ref)

        # Remove autolink from body
        body = body.replace(match.group(0), '')

    return body, registry


# ============================================================================
# PHASE 4: Consolidation Logic
# ============================================================================

def consolidate_references(registry: ReferenceRegistry) -> tuple[ReferenceRegistry, dict[int, int]]:
    """
    Consolidate references by merging duplicate URLs and assigning sequential numbers.

    Args:
        registry: Raw ReferenceRegistry with potentially duplicate URLs

    Returns:
        Tuple of (consolidated ReferenceRegistry, old_number -> new_number mapping)
    """
    # Track unique URLs and their first occurrence
    seen_urls: dict[str, Reference] = {}
    url_to_new_number: dict[str, int] = {}
    old_to_new_mapping: dict[int, int] = {}

    # Collect all references from by_number registry
    all_refs = []
    for number in sorted(registry.by_number.keys()):
        for ref in registry.by_number[number]:
            all_refs.append(ref)

    # Process references in order, assigning sequential numbers to unique URLs
    next_number = 1
    for ref in all_refs:
        if ref.url not in seen_urls:
            # First occurrence of this URL
            seen_urls[ref.url] = ref
            url_to_new_number[ref.url] = next_number
            next_number += 1

        # Map this reference's old number to the new number for its URL
        if ref.number is not None:
            old_to_new_mapping[ref.number] = url_to_new_number[ref.url]

    # Build consolidated registry with sequential numbering
    clean_registry = ReferenceRegistry()
    for url, new_number in url_to_new_number.items():
        first_ref = seen_urls[url]
        # Create new reference with updated number but original metadata
        clean_ref = Reference(
            number=new_number,
            url=first_ref.url,
            title_hint=first_ref.title_hint,
            context=first_ref.context
        )
        clean_registry.by_number[new_number] = [clean_ref]

    return clean_registry, old_to_new_mapping


# ============================================================================
# PHASE 5: Text Replacement & Generation
# ============================================================================

def apply_renumbering(text: str, mapping: dict[int, int]) -> str:
    """
    Replace citation numbers in text according to mapping.

    Args:
        text: Markdown text with [n] citations
        mapping: Dictionary mapping old citation numbers to new numbers

    Returns:
        Text with citations renumbered
    """
    result = text

    # Sort by descending number to avoid issues with overlapping replacements
    # e.g., replacing [1] before [10] could create issues
    for old_num in sorted(mapping.keys(), reverse=True):
        new_num = mapping[old_num]
        # Use word boundaries to match only [n] pattern, not array[n]
        # Pattern: look for [ followed by the number followed by ]
        pattern = rf'\[{old_num}\]'
        replacement = f'[{new_num}]'
        result = re.sub(pattern, replacement, result)

    return result


def generate_bibliography(registry: ReferenceRegistry) -> str:
    """
    Generate a markdown bibliography section from a reference registry.

    Args:
        registry: ReferenceRegistry with consolidated references

    Returns:
        Formatted markdown string with "## References" section
    """
    if not registry.by_number:
        return ""

    lines = ["## References\n"]

    # Sort by number and format each reference
    for number in sorted(registry.by_number.keys()):
        refs = registry.by_number[number]
        if not refs:
            continue

        ref = refs[0]  # Take first (should be only one after consolidation)

        if ref.title_hint:
            # Format as markdown link: 1. [Title](url)
            lines.append(f"{number}. [{ref.title_hint}]({ref.url})")
        else:
            # Format as bare URL: 1. <url>
            lines.append(f"{number}. <{ref.url}>")

    return "\n".join(lines)


def clean_markdown_file(input_path: Path) -> Path:
    """
    Clean a single markdown file and return output path.

    Args:
        input_path: Path to input markdown file

    Returns:
        Path to generated *_CLEAN.md file
    """
    print(f"Processing: {input_path}")

    # Read input file
    content = input_path.read_text(encoding='utf-8')

    # Split frontmatter from body
    frontmatter, body = split_frontmatter(content)

    # Decode HTML entities in body
    body = decode_entities_and_html(body)

    # Extract references (body gets [n] placeholders, registry holds URLs)
    body, raw_registry = extract_references(body)

    # Consolidate duplicate URLs and get renumbering map
    clean_registry, renumbering_map = consolidate_references(raw_registry)

    # Apply renumbering to body text
    body = apply_renumbering(body, renumbering_map)

    # Generate bibliography section
    bibliography = generate_bibliography(clean_registry)

    # Combine all parts
    output_parts = []
    if frontmatter:
        output_parts.append(frontmatter)
    output_parts.append(body)
    if bibliography:
        output_parts.append("\n\n" + bibliography)

    output_content = "\n".join(output_parts)

    # Write to *_CLEAN.md file
    output_path = input_path.parent / f"{input_path.stem}_CLEAN{input_path.suffix}"
    output_path.write_text(output_content, encoding='utf-8')

    print(f"[OK] Generated: {output_path}")
    return output_path


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(
        description="Clean markdown files from Deep Research exports",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Clean specific files
  %(prog)s report1.md report2.md

  # Clean all markdown files in directory
  %(prog)s path/to/reports/*.md
        """
    )
    parser.add_argument(
        'files',
        nargs='*',
        type=Path,
        help='Markdown files to clean (if none, processes default exemplar files)'
    )

    args = parser.parse_args()

    # Determine files to process
    if args.files:
        files_to_process = args.files
    else:
        # Default: look for exemplar files in a specific location
        # For now, require explicit file arguments
        parser.error("No input files specified. Please provide markdown files to clean.")

    # Process each file
    processed_count = 0
    for file_path in files_to_process:
        if not file_path.exists():
            print(f"[WARN] File not found: {file_path}")
            continue

        if not file_path.is_file():
            print(f"[WARN] Not a file: {file_path}")
            continue

        try:
            clean_markdown_file(file_path)
            processed_count += 1
        except Exception as e:
            print(f"[ERROR] Error processing {file_path}: {e}")
            import traceback
            traceback.print_exc()

    print(f"\n[OK] Processed {processed_count} file(s)")


if __name__ == "__main__":
    main()
