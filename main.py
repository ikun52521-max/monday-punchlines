#!/usr/bin/env python3
"""Monday Morning Punchlines - one original Monday-morning joke.

Running `python3 main.py` writes the punchline to /output/entry.txt
(the file the make.fun judge reads). The program is deterministic:
it prints the same single line on every run.
"""

import os

PUNCHLINE = (
    "My alarm clock and I reached a compromise this Monday: "
    "it rings, I ignore it, and we both pretend I'm a morning person."
)


def main():
    line = PUNCHLINE.strip()
    assert 1 <= len(line) <= 200, "punchline must be 1-200 characters"
    assert "\n" not in line, "punchline must be a single line"
    out_dir = "/output" if os.path.isdir("/output") else "."
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    # Read it back: the judge only scores what is actually on disk,
    # so confirm the written file holds exactly the punchline.
    with open(path, "r", encoding="utf-8") as f:
        assert f.read() == line + "\n", "entry.txt does not match the punchline"
    print(line)


if __name__ == "__main__":
    main()
