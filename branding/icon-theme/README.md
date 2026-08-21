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

## Licensing boundary

The concept artwork in this directory is original OBLinux branding work and is
covered by the repository's branding license. A future package derived from or
linking substantial Papirus artwork must satisfy Papirus's GPL-3.0 terms and
include the relevant copyright and source information. The package decision and
licensing inventory must be recorded before distribution.

