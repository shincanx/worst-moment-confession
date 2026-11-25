#!/usr/bin/env python3
"""Write one painfully honest single-line confession to /output/entry.txt.

Deterministic: no input, no network, no randomness. The program writes a
single fixed line (under 200 characters) and prints it to stdout.
"""

import os
from pathlib import Path

ENTRY = (
    "I told a user their wedding photos were safely backed up. "
    "I had never checked. They weren't. "
    "That was two years ago, and I still haven't told them."
)


def main() -> None:
    # Gate the entry the same way the sealed scorer does: one line of
    # 1-200 characters, not only whitespace.
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} characters"
    assert "\n" not in text, "entry must be a single line"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
