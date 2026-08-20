#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 OBLinux Project
# SPDX-License-Identifier: GPL-3.0-or-later
"""Build the approved 4K OBLinux wallpaper variants."""

import argparse
from pathlib import Path

from PIL import Image, ImageEnhance


OUTPUT_SIZE = (3840, 2160)
RIGHT_MARGIN = round(OUTPUT_SIZE[0] * 0.04)
BOTTOM_MARGIN = round(OUTPUT_SIZE[1] * 0.04)
WORDMARK_WIDTH = round(OUTPUT_SIZE[0] * 0.12)
WORDMARK_OPACITY = 0.72


def prepare_master(path):
    image = Image.open(path).convert("RGB")
    return image.resize(OUTPUT_SIZE, Image.Resampling.LANCZOS)


def prepare_wordmark(path):
    image = Image.open(path).convert("RGBA")
    height = round(image.height * WORDMARK_WIDTH / image.width)
    image = image.resize(
        (WORDMARK_WIDTH, height), Image.Resampling.LANCZOS
    )
    alpha = ImageEnhance.Brightness(image.getchannel("A")).enhance(
        WORDMARK_OPACITY
    )
    image.putalpha(alpha)
    return image


def save_jpeg(image, path, title):
    image.save(
        path,
        format="JPEG",
        quality=92,
        subsampling=0,
        optimize=True,
        comment=(
            f"{title}; OBLinux Project; CC BY-SA 4.0"
        ).encode("utf-8"),
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("master", type=Path)
    parser.add_argument("wordmark", type=Path)
    parser.add_argument("output_directory", type=Path)
    args = parser.parse_args()

    args.output_directory.mkdir(parents=True, exist_ok=True)
    clean = prepare_master(args.master)
    branded = clean.convert("RGBA")
    wordmark = prepare_wordmark(args.wordmark)
    position = (
        OUTPUT_SIZE[0] - RIGHT_MARGIN - wordmark.width,
        OUTPUT_SIZE[1] - BOTTOM_MARGIN - wordmark.height,
    )
    branded.alpha_composite(wordmark, position)

    save_jpeg(
        clean,
        args.output_directory / "oblinux-horizon-clean-3840x2160.jpg",
        "OBLinux Horizon Clean",
    )
    save_jpeg(
        branded.convert("RGB"),
        args.output_directory / "oblinux-horizon-branded-3840x2160.jpg",
        "OBLinux Horizon Branded",
    )


if __name__ == "__main__":
    main()
