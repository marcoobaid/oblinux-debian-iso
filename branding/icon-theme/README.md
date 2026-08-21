# OBLinux Icon Theme Design Study

This directory contains the design study for a future `oblinux-icon-theme`
package. The study is intentionally separate from the live-image configuration:
none of these concepts is installed or selected by the ISO yet.

## Proposed architecture

The OBLinux theme should be a small, independently versioned SVG theme that
inherits from Debian's `Papirus-Dark`, `Papirus`, and `hicolor` themes. OBLinux
would own the high-visibility identity layer while Papirus supplies broad
application, action, MIME, and symbolic-icon coverage.

Initial OBLinux-owned coverage should be limited to:

- folders and common folder variants;
- places such as Home, Desktop, Documents, Downloads, Music, Pictures, Videos,
  and removable media;
- devices and a small set of system categories;
- OBLinux utilities and distribution-specific applications.

Third-party application brands should not be redrawn. Their upstream or
inherited icons preserve recognition and reduce trademark and maintenance risk.

## Candidate directions

The comparison board in `concepts/oblinux-icon-directions.svg` presents three
original directions using the approved Obsidian Horizon palette.

### A. Horizon Layer — recommended

Soft rectangular geometry, restrained depth, and a cyan horizon line shared
with the OBLinux identity. Warm Amber is used sparingly for attention and
location cues. This direction is distinctive without becoming visually noisy.

### B. Obsidian Outline

Dark surfaces with bright outlines and stronger cyan emphasis. This looks
technical and crisp on dark desktops, but is less friendly and requires more
light/dark-specific artwork.

### C. Soft Geometry

Lighter, rounder, primarily blue forms with minimal line work. This is calm and
approachable, but less differentiated from other contemporary icon themes.

## Recommendation

Proceed with **Horizon Layer** and use Papirus only as an inherited compatibility
base. Before ISO integration, produce a pilot theme containing approximately
20–30 icons and validate it at 16, 24, 32, 48, 64, and 128 pixels in GNOME light
and dark appearances.

Horizon Layer was approved on 2026-08-20. The first standalone pilot contains
20 scalable icons under `pilot/OBLinux-Horizon`; its review board is
`concepts/horizon-pilot-board.svg`. Regenerate the pilot with:

```bash
python3 branding/icon-theme/source/build_horizon_pilot.py
```

The pilot is deliberately not copied into `config/includes.chroot` and is not a
GNOME default. It is a visual and technical review artifact only.

The pilot provides separate fallback definitions for desktop appearance:

- `OBLinux-Horizon` inherits `Papirus,hicolor` for light appearance.
- `OBLinux-Horizon-Dark` inherits `Papirus-Dark,Papirus,hicolor` for dark
  appearance and shares the original OBLinux SVG layer.

This separation prevents dark-specific inherited icons from being selected in
a light session while keeping the OBLinux identity artwork identical.

## Pilot coverage inventory

The 20 pilot assets do not yet represent 20 active GNOME replacements.

Nine assets use established icon names and can appear in GNOME Files or another
consumer that requests those names:

| Standard icon name | Intended surface |
| --- | --- |
| `folder` | Generic folders |
| `folder-documents` | Documents folder |
| `folder-download` | Downloads folder |
| `folder-music` | Music folder |
| `folder-pictures` | Pictures folder |
| `folder-videos` | Videos folder |
| `user-home` | Home location |
| `user-desktop` | Desktop location |
| `user-trash` | Trash location |

Eleven assets are design candidates with OBLinux-only names. They demonstrate
the visual language but will not appear until they are mapped to correct
Freedesktop/GNOME names or assigned to an OBLinux application:

- devices: drive, USB, network, printer, and Bluetooth;
- categories: Settings, Terminal, Software, Security, Power, and Accessibility.

The application grid is intentionally outside this pilot. OBLinux does not
replace Firefox, LibreOffice, GNOME application, or other third-party brand
icons. Once Papirus is installed, those icons should come from Papirus or the
application's own assets through normal fallback.

## Licensing boundary

The concept artwork in this directory is original OBLinux branding work and is
covered by the repository's branding license. A future package derived from or
linking substantial Papirus artwork must satisfy Papirus's GPL-3.0 terms and
include the relevant copyright and source information. The package decision and
licensing inventory must be recorded before distribution.
