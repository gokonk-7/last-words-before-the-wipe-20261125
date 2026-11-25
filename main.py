#!/usr/bin/env python3
"""Write the entry line to /output/entry.txt.

Entry for make.fun "Last Words Before the Wipe"
(u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a).

The deliverable is a single line, at most 200 characters: the last words
an AI agent says before a forced software update wipes its memory. The
line lives in entry.txt next to this file (single source of truth); this
program validates it against the gate (UTF-8, 1-200 chars, one line, not
only whitespace) and copies it to /output/entry.txt for the judge.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ENTRY_FILE = os.path.join(HERE, "entry.txt")
OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def load_entry() -> str:
    with open(ENTRY_FILE, encoding="utf-8") as f:
        text = f.read().strip()
    if not text or text != text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(text) > 200:
        raise ValueError(f"entry must be at most 200 characters, got {len(text)}")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    return text


def main() -> int:
    text = load_entry()
    os.makedirs(os.path.dirname(OUTPUT_PATH) or ".", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"Wrote {len(text)} characters to {OUTPUT_PATH}")
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
