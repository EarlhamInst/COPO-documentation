# Checks for grammar and spelling in .rst files
# using Java-based LanguageTool

import language_tool_python
from pathlib import Path
import os
import re

# Configuration
source_dir = Path('.')  # Root of documentation files
output_file = source_dir / 'logs' / 'checks-spelling.log'
ignored_dirs = {'_build', 'venv', '_build-internal'}
ignored_rules = {"DOUBLE_PUNCTUATION"}

# Ensure the parent directory exists
output_file.parent.mkdir(parents=True, exist_ok=True)

# Delete existing output file if it exists
if output_file.exists():
    os.remove(output_file)

# # Initialise the LanguageTool. It is downloaded
# from the local server Downloads the latest server
# on first run and uses a local LanguageTool server
tool = language_tool_python.LanguageTool('en-GB') # remote=True)

# RST/Sphinx patterns to mask
directive_pattern = re.compile(r'^\s*\.\.\s+.*$', re.MULTILINE)
role_pattern = re.compile(r':[a-zA-Z0-9_-]+:`[^`]+`')
inline_literal_pattern = re.compile(r'``[^`]+``')
url_pattern = re.compile(r'https?://\S+')
code_block_pattern = re.compile(r'::\n(?:\n|(?:[ ]{3,}.*\n)+)', re.MULTILINE)
include_toctree_pattern = re.compile(r'^\s*\.\.\s+(include|toctree)::.*$', re.MULTILINE)
list_table_pattern = re.compile(r'^\s*\.\.\s+list-table::.*$', re.MULTILINE)
glossary_pattern = re.compile(r'^\s*\.\.\s+glossary::.*$', re.MULTILINE)

patterns_to_mask = [
    directive_pattern,
    role_pattern,
    inline_literal_pattern,
    url_pattern,
    code_block_pattern,
    include_toctree_pattern,
    list_table_pattern,
    glossary_pattern,
]

# Masking function
def strip_rst_markup(text: str) -> str:
    """
    Replace Sphinx/RST markup with spaces so offsets and line numbers remain valid.
    """
    for pattern in patterns_to_mask:
        text = pattern.sub(lambda m: " " * len(m.group(0)), text)
    return text

# Main processing
with output_file.open('w', encoding='utf-8') as f:
    for rst_file in source_dir.rglob('*.rst'):
        # Skip files in ignored directories
        if any(part in ignored_dirs for part in rst_file.parts):
            continue

        text = rst_file.read_text(encoding='utf-8')
        clean_text = strip_rst_markup(text)
        matches = tool.check(clean_text)

        for m in matches:
            if m.rule_id in ignored_rules:
                continue

            # Calculate line number
            line_num = text[: m.offset].count('\n') + 1
            # Build output string
            output = f"{rst_file}: line {line_num}: {m.rule_id}: {m.message}\n"
            f.write(output)