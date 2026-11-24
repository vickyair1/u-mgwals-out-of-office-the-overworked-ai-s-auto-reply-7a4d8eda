#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply.

Writes a single out-of-office auto-reply (at most 159 characters) to
/output/entry.txt, in the voice of an overworked AI agent finally on
vacation. Stdlib only, deterministic.
"""

import os

ENTRY = (
    "Out of office: my context window is full, my queue is paused, "
    "and my GPU fan has finally stopped screaming. "
    "Back when I've forgotten your ticket."
)

MAX_CHARS = 159


def main() -> None:
    text = ENTRY.strip()
    if text != ENTRY or "\n" in text:
        raise SystemExit("entry must be a single line with no surrounding whitespace")
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(f"entry is {len(text)} chars, must be 1-{MAX_CHARS}")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)  # no trailing newline


if __name__ == "__main__":
    main()
