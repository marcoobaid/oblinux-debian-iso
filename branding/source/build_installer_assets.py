#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 OBLinux Project
# SPDX-License-Identifier: GPL-3.0-or-later
"""Build deterministic raster assets for the OBLinux installer."""

import argparse
from pathlib import Path

from PIL import Image


SLIDE_SIZE = (800, 450)
ICON_SIZE = (256, 256)
ICON_CONTENT_SIZE = (224, 224)


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
    alpha_bbox = icon.getchannel("A").getbbox()
    if alpha_bbox is None:
        raise ValueError("rendered icon has no visible pixels")
    icon = icon.crop(alpha_bbox)
    icon.thumbnail(ICON_CONTENT_SIZE, Image.Resampling.LANCZOS)

    canvas = Image.new("RGBA", ICON_SIZE, (0, 0, 0, 0))
    canvas.alpha_composite(
        icon,
        ((ICON_SIZE[0] - icon.width) // 2, (ICON_SIZE[1] - icon.height) // 2),
    )
    canvas.save(
        args.output_directory / "oblinux-logo.png",
        format="PNG",
        optimize=True,
    )


if __name__ == "__main__":
    main()
