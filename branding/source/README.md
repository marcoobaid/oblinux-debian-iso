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
