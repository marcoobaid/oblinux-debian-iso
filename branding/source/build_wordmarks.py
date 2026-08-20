#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 OBLinux Project
# SPDX-License-Identifier: GPL-3.0-or-later
"""Build deterministic OBLinux wordmark SVGs from Debian's Inter package."""

from pathlib import Path
from xml.sax.saxutils import escape

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont


ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = ROOT / "assets"
NAVY = "#111820"
CYAN = "#4CC9D8"
WHITE = "#F2F5F7"

SYMBOL = """
  <g transform="translate(0 36) scale(.8)">
    <path fill="{foreground}" fill-rule="evenodd" d="M154 52a128 128 0 1 0 0 256 128 128 0 0 0 0-256Zm0 52a76 76 0 1 1 0 152 76 76 0 0 1 0-152Z"/>
    <path fill="{foreground}" fill-rule="evenodd" d="M294 52h80c56 0 88 26 88 74 0 32-16 54-42 64 31 8 50 30 50 66 0 35-28 52-84 52h-92V52Zm52 50v54h28c23 0 34-9 34-27s-11-27-34-27h-28Zm0 116v40h40c20 0 30-7 30-20s-10-20-30-20h-40Z"/>
    <path fill="{accent}" d="M266 171h94v19h-94z"/>
  </g>"""


def outlined_text(font_path, text, x, baseline, em_size, fill, tracking=0):
    font = TTFont(font_path)
    glyph_set = font.getGlyphSet()
    cmap = font.getBestCmap()
    metrics = font["hmtx"].metrics
    scale = em_size / font["head"].unitsPerEm
    paths = []
    cursor = x

    for character in text:
        glyph_name = cmap[ord(character)]
        pen = SVGPathPen(glyph_set)
        transformed = TransformPen(
            pen, (scale, 0, 0, -scale, cursor, baseline)
        )
        glyph_set[glyph_name].draw(transformed)
        commands = pen.getCommands()
        if commands:
            paths.append(f'  <path fill="{fill}" d="{commands}"/>')
        cursor += metrics[glyph_name][0] * scale + tracking

    font.close()
    return "\n".join(paths), cursor


def svg_document(title, description, body, width, height):
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-FileCopyrightText: 2026 OBLinux Project -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
  <title id="title">{escape(title)}</title>
  <desc id="desc">{escape(description)}</desc>
{body}
</svg>
"""


def build_wordmark(bold_path, regular_path, foreground, suffix):
    symbol = SYMBOL.format(foreground=foreground, accent=CYAN)
    bold, cursor = outlined_text(
        bold_path, "OB", 430, 230, 154, foreground, tracking=-3
    )
    regular, _ = outlined_text(
        regular_path, "Linux", cursor - 8, 230, 154, foreground, tracking=-4
    )
    body = "\n".join((symbol, bold, regular))
    output = OUTPUTS / f"oblinux-wordmark-{suffix}-outlined.svg"
    output.write_text(
        svg_document(
            "OBLinux wordmark",
            "OBLinux horizon symbol and outlined OBLinux name.",
            body,
            1200,
            360,
        ),
        encoding="utf-8",
    )


def build_lockup(bold_path, regular_path):
    symbol = SYMBOL.format(foreground=NAVY, accent=CYAN)
    bold, cursor = outlined_text(
        bold_path, "OB", 430, 195, 142, NAVY, tracking=-3
    )
    regular, _ = outlined_text(
        regular_path, "Linux", cursor - 8, 195, 142, NAVY, tracking=-4
    )
    tagline, _ = outlined_text(
        regular_path, "Debian-based Linux", 435, 266, 50, "#176B87", tracking=4
    )
    body = "\n".join((symbol, bold, regular, tagline))
    output = OUTPUTS / "oblinux-lockup-color-outlined.svg"
    output.write_text(
        svg_document(
            "OBLinux descriptive lockup",
            "OBLinux horizon symbol, outlined name, and Debian-based Linux tagline.",
            body,
            1200,
            360,
        ),
        encoding="utf-8",
    )


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("bold_font", type=Path)
    parser.add_argument("regular_font", type=Path)
    args = parser.parse_args()

    build_wordmark(args.bold_font, args.regular_font, NAVY, "color")
    build_wordmark(args.bold_font, args.regular_font, WHITE, "reversed")
    build_lockup(args.bold_font, args.regular_font)


if __name__ == "__main__":
    main()
