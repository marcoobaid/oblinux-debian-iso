# Branding Source

`build_wordmarks.py` converts the approved OBLinux wordmark lettering into
deterministic SVG paths. It requires Python 3 and FontTools.

The approved generation inputs are Inter Display Bold and Regular 4.1 from
Debian 13's `fonts-inter` package version `4.1+ds-1`. Verify their SHA-256
checksums against `../ATTRIBUTION.md` before generation.

Run from the repository root:

```bash
branding/source/build_wordmarks.py \
  /path/to/InterDisplay-Bold.otf \
  /path/to/InterDisplay-Regular.otf
```

The command replaces the three outlined wordmark files under `../assets/`.
Generated output must pass XML validation and visual review before commit.

`oblinux-wordmark-editable.svg` retains editable text for design reference. It
depends on installed fonts and is not an approved release asset.

## Wallpaper generation

`oblinux-horizon-master.png` is the approved clean image-generation output.
`build_wallpapers.py` scales it to the 4K delivery size and composites an exact
transparent rendering of the approved reversed SVG wordmark.

```bash
branding/source/build_wallpapers.py \
  branding/source/oblinux-horizon-master.png \
  /path/to/rendered-reversed-wordmark.png \
  branding/wallpapers
```

Render the wordmark from
`../assets/oblinux-wordmark-reversed-outlined.svg` at 461 pixels wide with a
standards-compliant SVG renderer. The builder used Debian's `rsvg-convert` from
`librsvg2-bin` 2.60.0 for the approved output.

## Installer asset generation

Render `../assets/oblinux-symbol-reversed.svg` at its native 500 by 360 aspect
ratio with a transparent background and a standards-compliant SVG renderer.
Then run:

```bash
branding/source/build_installer_assets.py \
  branding/wallpapers/oblinux-horizon-branded-3840x2160.jpg \
  /path/to/rendered-reversed-symbol.png \
  branding/installer
```

The command tightly crops the rendered symbol, fits it within a transparent
256-pixel canvas, and produces the 800 by 450 welcome image. It rejects the
opaque rounded-square treatment previously used by Build 006. Copy approved
outputs into the corresponding package-owned paths under
`config/includes.chroot` when updating the integration.

## Installed-system asset generation

Build the Plymouth logo and progress textures from the approved installer icon:

```bash
branding/source/build_system_assets.py \
  branding/installer/oblinux-logo.png \
  branding/system
```

Copy the approved outputs into the OBLinux Plymouth theme under
`config/includes.chroot`. The GNOME About icon uses the approved color symbol
SVG directly and does not require another raster export.

## GDM vendor-logo generation

Build the complete Debian-compatible `vendor-logos` alternative from the
approved transparent system symbol and installer badge:

```bash
branding/source/build_vendor_logos.py \
  branding/system/plymouth-logo.png \
  branding/installer/oblinux-logo.png \
  config/includes.chroot/usr/share/oblinux
```

The text and version variants use the transparent OBLinux symbol displayed by
GDM. The square logo and vendor-emblem variants use the approved badge. The
installed-identity hook registers all outputs as one alternatives group so
Debian's package-owned candidate remains available.
