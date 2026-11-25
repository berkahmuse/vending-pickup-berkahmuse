#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes a single pickup line, spoken by a vending machine to a passing
human, to /output/entry.txt. Deterministic: the same line every run.
"""

import os

LINE = "I've dropped a thousand snacks, but you're the first one I wanted to keep \u2014 press B7 and I'll fall for you, no exact change required."


def main() -> None:
    # Gate: the entry must be one line of 1-200 characters, UTF-8.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    LINE.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
