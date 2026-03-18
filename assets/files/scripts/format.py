#!/usr/bin/env python3

from pathlib import Path
import re

BASE_DIR = Path(__file__).resolve().parents[3]
SOURCE_DIR = BASE_DIR #/ "submissions" / "tol" # Path(".")

assert SOURCE_DIR.exists(), f"{SOURCE_DIR} does not exist"
assert SOURCE_DIR.is_dir(), f"{SOURCE_DIR} is not a directory"

FIG_REF_RE = re.compile(r"^\.\. _(?P<name>ref-[^:]+):\s+(?P<value>\S+)", re.MULTILINE)
FIGURE_RE = re.compile(r"(\.\.\s+figure::)\s+(ref-[\w-]+_)", re.MULTILINE)
TARGET_RE = re.compile(r"(:target:)\s+(ref-[\w-]+_)", re.MULTILINE)

def process_file():
    for rst_file in SOURCE_DIR.rglob("*.rst"):
        # Skip build/venv directories if needed
        if any(part.startswith("_build") or part == "venv" for part in rst_file.parts):
            continue
        print(f"Processing: {rst_file}")

        text = rst_file.read_text(encoding="utf-8")

        # Collect reference mappings
        refs = {
            m.group("name") + "_": m.group("value")
            for m in FIG_REF_RE.finditer(text)
        }

        if not refs:
            continue

        new_text = text

        # Replace figure references
        def replace_figure(match):
            ref = match.group(2)
            return f"{match.group(1)} {refs.get(ref, ref)}"

        # Replace target references
        def replace_target(match):
            ref = match.group(2)
            return f"{match.group(1)} {refs.get(ref, ref)}"

        new_text = FIGURE_RE.sub(replace_figure, new_text)
        new_text = TARGET_RE.sub(replace_target, new_text)

        if new_text != text:
            rst_file.write_text(new_text, encoding="utf-8")
            print(f"Updated: {rst_file}")

def remove_link_declaration_and_trailing_content(rst_file: Path) -> None:
    """
    Removes the '.. Link declaration ..' block and everything after it.
    Ensures the file ends with a newline.
    """
    text = rst_file.read_text(encoding="utf-8")

    # Pattern matches:
    # ..
    #     Link declaration
    # ..
    pattern = re.compile(
        r"\n?\.\.\n\s+Link declaration\n\.\.\n.*\Z",
        re.DOTALL
    )

    new_text = re.sub(pattern, "\n", text)

    # Ensure exactly one newline at EOF
    new_text = new_text.rstrip() + "\n"

    if new_text != text:
        rst_file.write_text(new_text, encoding="utf-8")

def main():
    process_file()
    print("Processing completed")
    for rst_file in SOURCE_DIR.rglob("*.rst"):
        # Skip build/venv directories if needed
        if any(part.startswith("_build") or part == "venv" for part in rst_file.parts):
            continue
        remove_link_declaration_and_trailing_content(rst_file)
    print("Links deleted")

if __name__ == "__main__":
    main()