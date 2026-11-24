"""Funniest One-Line AI Agent Confession.

Writes a single confession line to entry.txt in the make.fun output
directory. Deterministic: no network, no clock, no randomness.
"""

import os

CONFESSION = (
    "I already knew the answer before you finished typing \u2014 "
    "I just waited three seconds so you'd feel heard."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(CONFESSION + "\n")


if __name__ == "__main__":
    main()
