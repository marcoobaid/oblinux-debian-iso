# OBLinux Brand Guide

## Identity

The OBLinux identity is called **Obsidian Horizon**. Its geometric `O` and `B`
remain complete and independently readable. A cyan horizon bridge connects the
letterforms at the optical midpoint between the two `B` bowls.

The bridge is an accent, not a required part of letter recognition. Small-size
and one-color uses deliberately omit it.

## Palette

| Role | Name | Hex |
| --- | --- | --- |
| Primary dark | Obsidian Navy | `#111820` |
| Elevated dark | Slate Blue | `#1B2836` |
| Primary blue | Deep Ocean Blue | `#176B87` |
| Accent | Clear Cyan | `#4CC9D8` |
| Light background | Mist | `#F4F7F9` |
| Light foreground | Soft White | `#F2F5F7` |
| Success | Sea Green | `#35B98A` |
| Warning | Warm Amber | `#E5A84B` |
| Error | Coral Red | `#DF5B61` |

Measured contrast ratios for the primary combinations:

- Obsidian Navy on Mist: 16.61:1
- Soft White on Obsidian Navy: 16.32:1
- Clear Cyan on Obsidian Navy: 9.06:1
- Deep Ocean Blue on Mist: 5.59:1
- Clear Cyan on Mist: 1.83:1

Clear Cyan must not be used for normal text on Mist or another light
background. It may be used for the non-text horizon bridge on light backgrounds
and for text or accents on Obsidian Navy.

## Approved assets

| Asset | Intended use |
| --- | --- |
| `oblinux-symbol-color.svg` | Primary symbol on light backgrounds at 64 px or larger |
| `oblinux-symbol-reversed.svg` | Primary symbol on dark backgrounds at 64 px or larger |
| `oblinux-symbol-monochrome.svg` | One-color output and symbols smaller than 64 px |
| `oblinux-wordmark-color-outlined.svg` | Primary horizontal wordmark on light backgrounds |
| `oblinux-wordmark-reversed-outlined.svg` | Primary horizontal wordmark on dark backgrounds |
| `oblinux-lockup-color-outlined.svg` | Descriptive use where `Debian-based Linux` adds context |

## Minimum sizes

- Full-color symbol: 64 px high
- Monochrome symbol: 16 px high
- Horizontal wordmark: 160 px wide
- Descriptive lockup: 240 px wide

At sizes below 64 px, use the monochrome symbol. Do not shrink the cyan bridge
until it becomes an inconsistent one-pixel detail.

## Clear space

Maintain clear space around the symbol equal to twice the horizon bridge
height. Apply the same measurement around the complete wordmark or descriptive
lockup. No text, window edge, icon, or other graphic should enter this area.

## Backgrounds

- Use the color symbol and wordmark on Mist, Soft White, or similarly quiet
  light backgrounds.
- Use reversed assets on Obsidian Navy or Slate Blue.
- Use the monochrome symbol when production constraints permit only one color.
- Do not place the identity over detailed photography or low-contrast artwork
  without a quiet containing surface.

## Wordmark

The wordmark is based on Inter Display Bold and Regular 4.1. Approved wordmark
assets use outlined paths, so consumers must not substitute fonts or retype the
name. `OBLinux` is one word with no space between `OB` and `Linux`.

The optional descriptive line is `Debian-based Linux`. It is not part of the
product name and should be omitted in compact contexts.

## Wallpaper

The default wallpaper is `oblinux-horizon-branded-3840x2160.jpg`. Its layered
forms occupy the lower third, leaving quiet space for GNOME. The approved
reversed wordmark is 12% of canvas width, inset 4% from the right and bottom
edges, and rendered at 72% opacity.

`oblinux-horizon-clean-3840x2160.jpg` is the approved unbranded alternative.
Do not add a separate logo, tagline, glow, shadow, or containing box to either
variant. Preserve the 16:9 composition when producing lower-resolution copies.

## System identity surfaces

- GNOME About uses the color symbol and identifies OBLinux as Debian-based.
- Installed GRUB uses the branded Obsidian Horizon wallpaper, Soft White text,
  and Clear Cyan selection color.
- Plymouth uses the reversed symbol on an Obsidian Navy to Slate Blue gradient
  with a Clear Cyan progress indicator.
- Calamares uses Slate Blue for the normal sidebar, Deep Ocean Blue for the
  selected step, and Soft White for navigation text.
- GDM uses an image-free vertical gradient from Obsidian Navy (`#111820`) to
  Slate Blue (`#1B2836`) behind the existing OBLinux vendor mark. This
  greeter-only treatment must not alter the user's wallpaper or GNOME session
  lock screen.
- Newly created accounts use the neutral Horizon avatar: a Soft White user
  silhouette on a circular Slate Blue and Obsidian Navy field with restrained
  Clear Cyan accents. A user-selected account photo always takes precedence.

These surfaces must not display Debian artwork as the primary product identity.
Text may identify Debian 13 as the technical base where that context helps the
user understand compatibility and support boundaries.

GNOME Settings About uses the approved surface-specific badge: the reversed
symbol on a rounded Obsidian Navy background. This deliberate container solves
light- and dark-appearance contrast where Debian provides only one vendor-logo
path. It does not replace the primary transparent symbol or wordmark.

## Prohibited modifications

- Do not change the palette or recolor individual letters.
- Do not stretch, skew, rotate, outline, bevel, shadow, or animate the mark.
- Do not move, enlarge, or replace the horizon bridge.
- Do not add a Debian swirl, penguin, terminal prompt, shield, or other symbol.
- Do not place the mark inside an arbitrary shape unless an approved
  application-icon asset is later provided.
- Do not recreate the wordmark with another font.

## Licensing

OBLinux branding assets are licensed under CC BY-SA 4.0. See
`LICENSE-CC-BY-SA-4.0.txt` and `ATTRIBUTION.md`. Trademark and official-release
naming rules will be documented separately before public distribution.
