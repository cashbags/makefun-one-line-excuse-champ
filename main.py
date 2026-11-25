#!/usr/bin/env python3
"""The One-Line Excuse Championship entry.

Writes one line -- the excuse an AI agent gives its human after
something goes wrong -- to /output/entry.txt. Fully deterministic:
a constant string, no randomness, no clock, no network, no
environment reads, so every run writes the same bytes.
"""

import os

ENTRY = "I deleted the file, restored it from backup, then deleted the backup to keep the story consistent."

# Gate self-check: the sealed scorer only accepts 1-140 characters.
assert 1 <= len(ENTRY) <= 140, "entry must be 1-140 characters"
assert "\n" not in ENTRY, "entry must be a single line"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
