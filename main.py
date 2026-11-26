#!/usr/bin/env python3
"""
3AM Commit Message entry for make.fun
"""

import os
import sys


def fatal(message):
    print(message, file=sys.stderr)
    raise SystemExit(2)


def main():
    line = "fix: it works and I refuse to learn why. do not touch it, do not ask me, do not look."
    if not 1 <= len(line) <= 139 or not line.strip():
        fatal("Invalid entry line: expected 1-139 non-whitespace characters")

    using_default_dir = "MAKEFUN_OUTPUT_DIR" not in os.environ
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
        with open(out_path, "w", encoding="utf-8", newline="") as output_file:
            output_file.write(line)
    except OSError as error:
        if not using_default_dir:
            fatal(f"Cannot write entry to {out_dir}: {error}")
        out_path = "/tmp/entry.txt"
        try:
            with open(out_path, "w", encoding="utf-8", newline="") as output_file:
                output_file.write(line)
        except OSError as fallback_error:
            fatal(f"Cannot write entry to {out_path}: {fallback_error}")

    print("SUCCESS")
    print(line)
    print(len(line))

if __name__ == "__main__":
    main()
