#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 OBLinux Project
# SPDX-License-Identifier: GPL-3.0-or-later
"""Build deterministic OBLinux Plymouth raster assets."""

import argparse
from pathlib import Path

from PIL import Image


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("logo", type=Path)
    parser.add_argument("output_directory", type=Path)
    args = parser.parse_args()

    args.output_directory.mkdir(parents=True, exist_ok=True)

    logo = Image.open(args.logo).convert("RGBA")
    logo = logo.resize((256, 256), Image.Resampling.LANCZOS)
    logo.save(args.output_directory / "plymouth-logo.png", optimize=True)

    Image.new("RGB", (8, 8), "#1B2836").save(
        args.output_directory / "progress-background.png",
        optimize=True,
    )
    Image.new("RGB", (8, 8), "#4CC9D8").save(
        args.output_directory / "progress-fill.png",
        optimize=True,
    )


if __name__ == "__main__":
    main()
