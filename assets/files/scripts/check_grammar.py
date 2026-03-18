# Checks for grammar and spelling in .rst files
# using Java-based LanguageTool

import language_tool_python
from pathlib import Path
import os

# Configuration
source_dir = Path('.')  # Root of documentation files
output_file = source_dir/'logs'/'spelling_check.log'

# Ensure the parent directory exists
output_file.parent.mkdir(parents=True, exist_ok=True)

# Delete existing output file if it exists
if output_file.exists():
    os.remove(output_file)

# # Initialise the LanguageTool. It is downloaded from the local server Downloads the latest server on first run and
# uses a local LanguageTool server
tool = language_tool_python.LanguageTool('en-GB') # remote=True)

ignored_dirs = {'_build', 'venv', '_buildinternal'}

with output_file.open('w', encoding='utf-8') as f:
    for rst_file in source_dir.rglob('*.rst'):
        # Skip files in ignored directories
        if any(part in ignored_dirs for part in rst_file.parts):
            continue

        text = rst_file.read_text(encoding='utf-8')
        matches = tool.check(text)

        for m in matches:
            # Calculate line number
            line_num = text[: m.offset].count('\n') + 1
            # Build output string
            output = f"{rst_file}: line {line_num}: {m.rule_id}: {m.message}\n"
            f.write(output)