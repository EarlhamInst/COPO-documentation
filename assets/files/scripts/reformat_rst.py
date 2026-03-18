#!/usr/bin/env python3
import os
import textwrap
import re

ROOT_DIR = "."
WRAP_WIDTH = 79

# Matches leading whitespace and optional bullet or enumerator
LEADING_PATTERN = re.compile(r"^(\s*(?:[-*+]|\d+\.)?\s*)")


def wrap_rst_line(line):
    if line.strip() == "" or line.lstrip().startswith(".. "):
        # Leave blank lines or directives untouched
        return [line.rstrip()]

    # Detect indentation / bullets
    match = LEADING_PATTERN.match(line)
    indent = match.group(1) if match else ""
    text = line[len(indent):].strip()

    if not text:
        return [line.rstrip()]

    wrapped_lines = textwrap.fill(
        text,
        width=WRAP_WIDTH,
        initial_indent=indent,
        subsequent_indent=indent
    )
    return wrapped_lines.split("\n")


def reformat_rst_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        new_lines.extend(wrap_rst_line(line))

    new_lines = [l + "\n" for l in new_lines]

    with open(filepath, "w", encoding="utf-8") as f:
        f.writelines(new_lines)
    print(f"Reformatted: {filepath}")


def main():
    for root, _, files in os.walk(ROOT_DIR):
        for file in files:
            if file.endswith(".rst"):
                reformat_rst_file(os.path.join(root, file))


if __name__ == "__main__":
    main()