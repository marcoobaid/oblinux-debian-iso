# OBLinux Horizon Icon Theme

This directory contains the approved design and reproducible source tooling for
the future `oblinux-icon-theme` package. It remains separate from the live-image
configuration until the derived theme passes packaging and ISO validation.

## Proposed architecture

The approved architecture is a complete, independently versioned derivative of
Debian's Papirus theme. The build process transforms Papirus's full application,
action, MIME, device, place, status, symbolic, and alias coverage into one
cohesive OBLinux Horizon family.

The derivative applies two treatments:

- recognizable application symbols remain recognizable, but receive consistent
  optical sizing, a Slate Blue rounded container, and the Cyan horizon detail;
- system and interface artwork receives a deterministic semantic remap into the
  Obsidian Horizon palette.

The approved original 20-icon Horizon layer is installed at the front of the
generated base theme so its folders and high-visibility identity artwork win
normal icon lookup. `hicolor` remains the standards-compliant final fallback.
The dark theme contains dark-specific Papirus coverage and inherits from the
complete Horizon base rather than duplicating application assets.

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

Proceed with **Horizon Layer** as a complete Papirus-derived family. Before ISO
integration, validate the generated theme at common sizes in GNOME light and
dark appearances, package it independently, and prove clean rollback.

Horizon Layer was approved on 2026-08-20. The first standalone pilot contains
20 scalable icons under `pilot/OBLinux-Horizon`; its review board is
`concepts/horizon-pilot-board.svg`. Regenerate the pilot with:

```bash
python3 branding/icon-theme/source/build_horizon_pilot.py
```

The pilot is deliberately not copied into `config/includes.chroot` and is not a
GNOME default. It supplies original identity artwork to the full-theme generator.

The complete generated output provides separate definitions for appearance:

- `OBLinux-Horizon` contains complete transformed Papirus coverage and inherits
  only `hicolor`.
- `OBLinux-Horizon-Dark` contains transformed Papirus Dark coverage and inherits
  `OBLinux-Horizon,hicolor`.

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

The pilot itself still excludes application icons. The full derivative generator
uses Papirus application artwork so recognizable symbols remain familiar while
their presentation belongs to the Horizon family.

## Building the full derivative

Install or extract Debian's pinned `papirus-icon-theme` source package, then run:

```bash
python3 branding/icon-theme/source/build_papirus_derivative.py \
  --overlay branding/icon-theme/pilot/OBLinux-Horizon \
  /path/to/usr/share/icons \
  /path/to/generated-output
```

The source directory must contain `Papirus` and `Papirus-Dark`. The destination
must not already contain generated themes. The command creates
`OBLinux-Horizon` and `OBLinux-Horizon-Dark`, retargets internal aliases, applies
the palette and application treatments, and prepends the approved identity
overlay. Generated themes are build artifacts and are not committed to this
repository.

## Licensing boundary

The original concept artwork in this directory is OBLinux branding work. Papirus
and all committed or generated derivatives of Papirus are GPL-3.0 licensed. A
distributed package must include Papirus's copyright notices, GPL-3.0 license,
the pinned source version, and this transformation source so recipients can
reproduce the corresponding binary package.
