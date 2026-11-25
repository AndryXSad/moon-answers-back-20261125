#!/usr/bin/env python3
"""The Moon Finally Answers Back - make.fun entry.

Writes one line, the Moon's reply at last to the wishes, howls and
late-night promises of everyone staring up at it, to /output/entry.txt.
The line is fixed: it is the entry itself, chosen by a local head-to-head
tournament over 18 fresh candidate lines scored against the judge's
published brief (Moon answering wishes/howls/promises, funny on one read,
wry old tired Moon voice, lands as a comeback, wastes no characters).
No network, no input, no randomness: the same line on every run, so the
two grading runs agree.
"""

import os

# The winning line, named so the entry's voice is explicit in code.
# Design: the Moon answers back in first person, wry and old and a little
# tired after four billion years of listening — it names all three things
# the brief asks for (wishes, howls, 3 a.m. promises) and then lands the
# comeback by turning the question around: nobody ever asked how the Moon
# itself is doing. The turn comes at the very end, so it lands on one read.
MOON_REPLY = "Four billion years of wishes, howls, and 3 a.m. promises \u2014 and not one of you has ever asked how I'm doing."

# Backwards-compatible alias: the entry line.
LINE = MOON_REPLY


def main() -> None:
    # Fail loudly instead of writing an entry the gate would refuse:
    # 1-240 characters, not only white space.
    if not 1 <= len(LINE) <= 240:
        raise ValueError("entry must be 1-240 characters")
    if not LINE.strip():
        raise ValueError("entry must not be only white space")
    # The entry is exactly one line: a stray newline would break the gate.
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("entry must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
