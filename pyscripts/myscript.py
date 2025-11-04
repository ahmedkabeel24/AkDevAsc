from __future__ import annotations
import sys
import argparse
import logging
from pathlib import Path
from typing import Optional

#!/usr/bin/env python3
"""
Basic Python CLI script template.

Usage examples:
    python myscript.py --file example.txt --action count
    echo "hello" | python myscript.py --action uppercase
"""



logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def read_input(file: Optional[Path]) -> str:
        if file:
                return file.read_text(encoding="utf-8")
        return sys.stdin.read()


def action_count(text: str) -> str:
        lines = text.splitlines()
        words = text.split()
        chars = len(text)
        return f"lines={len(lines)} words={len(words)} chars={chars}"


def action_reverse(text: str) -> str:
        return "\n".join(line[::-1] for line in text.splitlines())


def action_uppercase(text: str) -> str:
        return text.upper()


ACTIONS = {
        "count": action_count,
        "reverse": action_reverse,
        "uppercase": action_uppercase,
}


def parse_args(argv) -> argparse.Namespace:
        p = argparse.ArgumentParser(description="Basic text-processing script.")
        p.add_argument("--file", "-f", type=Path, help="Path to input file (defaults to stdin).")
        p.add_argument("--action", "-a", choices=ACTIONS.keys(), default="count", help="Action to perform.")
        p.add_argument("--version", action="version", version="myscript 0.1")
        return p.parse_args(argv)


def main(argv=None) -> int:
        args = parse_args(argv or sys.argv[1:])
        logging.debug("Arguments: %s", args)
        try:
                text = read_input(args.file)
        except Exception as e:
                logging.error("Failed to read input: %s", e)
                return 2

        func = ACTIONS[args.action]
        try:
                output = func(text)
        except Exception as e:
                logging.error("Action failed: %s", e)
                return 3

        if output is not None:
                print(output)
        return 0


if __name__ == "__main__":
        raise SystemExit(main())