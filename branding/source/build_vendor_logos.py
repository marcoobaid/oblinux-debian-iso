#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 OBLinux Project
# SPDX-License-Identifier: GPL-3.0-or-later
"""Build deterministic OBLinux assets for Debian's vendor-logos alternative."""

import argparse
from pathlib import Path

from PIL import Image


def contain(source, height):
    width = round(source.width * height / source.height)
    return source.resize((width, height), Image.Resampling.LANCZOS)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("wordmark", type=Path)
    parser.add_argument("badge", type=Path)
    parser.add_argument("output_directory", type=Path)
    args = parser.parse_args()

    logos = args.output_directory / "vendor-logos"
    emblems = args.output_directory / "vendor-emblems"
    logos.mkdir(parents=True, exist_ok=True)
    emblems.mkdir(parents=True, exist_ok=True)

    wordmark = Image.open(args.wordmark).convert("RGBA")
    badge = Image.open(args.badge).convert("RGBA")
    if wordmark.getchannel("A").getextrema()[0] != 0:
        raise ValueError("Vendor wordmark must have transparent pixels")
    if badge.size != (256, 256):
        raise ValueError("Vendor badge source must be 256 by 256 pixels")

    for size in (64, 128, 256):
        symbol = contain(wordmark, size)
        symbol.save(logos / f"logo-text-{size}.png", optimize=True)
        symbol.save(logos / f"logo-text-version-{size}.png", optimize=True)

        emblem = badge.resize((size, size), Image.Resampling.LANCZOS)
        emblem.save(logos / f"logo-{size}.png", optimize=True)
        emblem.save(emblems / f"emblem-vendor-{size}.png", optimize=True)
        emblem.save(
            emblems / f"emblem-vendor-symbolic-{size}.png", optimize=True
        )
        emblem.save(emblems / f"emblem-vendor-white-{size}.png", optimize=True)


if __name__ == "__main__":
    main()
