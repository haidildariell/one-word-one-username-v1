#!/usr/bin/env python3
"""One Word, One Username, One Reward - make.fun entry.

Writes the entrant's own make.fun username, one word and nothing else,
to /output/entry.txt. The username is exactly 13 characters, a single
word with no spaces and no trailing newline, so the file is 13 bytes.
"""

import os

USERNAME = "haidildariell"

OUTPUT_PATH = "/output/entry.txt"


def write_entry(path: str, text: str) -> None:
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


def main() -> None:
    write_entry(OUTPUT_PATH, USERNAME)


if __name__ == "__main__":
    main()
