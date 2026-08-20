# Decision 0005: OBLinux visual identity

- Status: Accepted
- Date: 2026-08-19

## Context

The functional POC needs a coherent identity before wallpaper, boot, GNOME, and
Calamares integration begins. The identity must remain recognizable at small
sizes, work on light and dark surfaces, support one-color output, and avoid
visual dependence on Debian or generic Linux symbols.

## Decision

OBLinux adopts the **Obsidian Horizon** identity:

- A geometric `OB` symbol with complete, independently readable letters
- A Clear Cyan horizon bridge connecting the letters in full-color variants
- Obsidian Navy and Mist as the primary dark and light foundations
- Inter Display-based outlined wordmarks
- A responsive monochrome symbol below 64 pixels
- `OBLinux` as the primary wordmark
- `Debian-based Linux` as an optional descriptive line

Original branding assets use CC BY-SA 4.0. Code and general project
documentation remain under the repository's GPLv3 terms. Trademark and naming
policy remain separate future public-release work.

## Consequences

- Wallpaper, boot, GNOME, and Calamares work must follow one documented system.
- Cyan is an accent and cannot be used as normal text on light backgrounds.
- Small-size use must switch to the monochrome symbol rather than degrading the
  horizon bridge.
- Consumers use outlined wordmarks and do not require Inter at runtime.
- Changes to the approved geometry or palette require explicit design review.
