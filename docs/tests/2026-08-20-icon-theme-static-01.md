# Horizon Layer icon-theme static review 01

- Date: 2026-08-20
- Scope: Standalone pilot only
- Result: Static preflight passed; GNOME runtime review pending

## Inputs

- 20 original scalable SVG icons
- Light fallback theme: `OBLinux-Horizon`
- Dark fallback theme: `OBLinux-Horizon-Dark`
- Review sizes: 16, 24, 32, 48, 64, and 128 pixels

## Checks completed

- All 20 source icons are well-formed XML.
- The pilot generator recreates the expected icon count.
- The light theme inherits `Papirus,hicolor`.
- The dark theme inherits `Papirus-Dark,Papirus,hicolor`.
- Both appearances share the same original OBLinux identity layer.
- Representative folder, device, place, and system-category icons render on
  light and dark review surfaces.
- The base folder silhouette and cyan horizon remain recognizable at 16 pixels.
- High-detail folder glyphs remain recognizable at 24 pixels but will require
  special attention during runtime review and may need size-specific variants.
- No files are present under `config/includes.chroot`; the pilot cannot affect
  the current ISO.

## Pending acceptance work

- Install the pilot in an isolated test session.
- Verify icon-name coverage and Papirus fallback in GNOME Files and Settings.
- Review light and dark appearances at standard density and HiDPI.
- Check selected, disabled, symbolic, and high-contrast states.
- Decide whether 16- and 24-pixel folder variants need simplified artwork.
- Confirm clean installation, theme switching, removal, and preference rollback.

The pilot must not become the ISO default until those checks pass.
