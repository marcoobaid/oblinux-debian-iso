#!/usr/bin/env python3
"""Prototype Horizon application treatment on selected Papirus SVG icons.

This is a design-review tool, not the production derivative builder. It keeps
the recognizable Papirus application symbol, normalizes its optical size, and
places it on the approved Horizon application container.
"""

from pathlib import Path
import argparse
import re


OPEN_SVG = re.compile(r"(<svg\b[^>]*>)", re.IGNORECASE)
CLOSE_SVG = re.compile(r"</svg>\s*$", re.IGNORECASE)


def transform(source: str) -> str:
    match = OPEN_SVG.search(source)
    if not match or not CLOSE_SVG.search(source):
        raise ValueError("input is not a complete SVG document")

    content_start = match.end()
    content_end = CLOSE_SVG.search(source).start()
    content = source[content_start:content_end]
    container = '''
  <rect x="2" y="2" width="60" height="60" rx="15" fill="#1B2836"/>
  <path d="M9 43c13-8 24 8 37 0 8-5 14-3 19-1" fill="none" stroke="#4CC9D8" stroke-width="2.4" stroke-linecap="round" opacity=".72"/>
  <g transform="translate(7.7 6.2) scale(.76)">
'''
    closing = "\n  </g>\n"
    return source[:content_start] + container + content + closing + source[content_end:]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    args = parser.parse_args()
    args.destination.mkdir(parents=True, exist_ok=True)

    count = 0
    for source in sorted(args.source.glob("*.svg")):
        result = transform(source.read_text(encoding="utf-8"))
        (args.destination / source.name).write_text(result, encoding="utf-8")
        count += 1
    print(f"Generated {count} Horizon application prototypes")


if __name__ == "__main__":
    main()
