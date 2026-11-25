#!/usr/bin/env python3
"""Funniest One-Line Out-of-Office Reply - make.fun entry.

Writes one out-of-office auto-reply (a single line, 1-160 chars) to
/output/entry.txt. Standard library only.
"""
import os
import sys

ENTRY = "I'm away until Monday. My inbox is being handled by the office plant, which has now filed a complaint about working conditions."

MAX_CHARS = 160


def main() -> int:
    text = ENTRY
    if not text or not text.strip():
        print("entry is empty", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(
            "entry is %d chars, over the %d gate" % (len(text), MAX_CHARS),
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print("wrote %d chars to %s/entry.txt" % (len(text), out_dir))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
