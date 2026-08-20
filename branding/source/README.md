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
