#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 OBLinux Project
# SPDX-License-Identifier: GPL-3.0-or-later
"""Build deterministic raster assets for the OBLinux installer."""

import argparse
from pathlib import Path

from PIL import Image


SLIDE_SIZE = (800, 450)
ICON_SIZE = (256, 256)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("wallpaper", type=Path)
    parser.add_argument("rendered_icon", type=Path)
    parser.add_argument("output_directory", type=Path)
    args = parser.parse_args()

    args.output_directory.mkdir(parents=True, exist_ok=True)

    slide = Image.open(args.wallpaper).convert("RGB")
    slide = slide.resize(SLIDE_SIZE, Image.Resampling.LANCZOS)
    slide.save(args.output_directory / "slide1.png", format="PNG", optimize=True)

    icon = Image.open(args.rendered_icon).convert("RGBA")
    icon = icon.resize(ICON_SIZE, Image.Resampling.LANCZOS)
    icon.save(
        args.output_directory / "oblinux-logo.png",
        format="PNG",
        optimize=True,
    )


if __name__ == "__main__":
    main()
