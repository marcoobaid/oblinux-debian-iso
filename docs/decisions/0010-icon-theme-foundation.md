# Decision 0010: Icon-theme foundation

- Status: Accepted for full derivative implementation
- Date: 2026-08-20

## Context

Icons strongly affect perceived desktop quality, but a complete Linux icon
theme contains thousands of names, aliases, sizes, symbolic variants, and
application-specific compatibility cases. Building and maintaining all of that
coverage during the proof of concept would distract from hardware validation
and daily-driver reliability.

Debian 13 provides `papirus-icon-theme` version `20250501-1`. The package
contains Papirus, Papirus Dark, and Papirus Light SVG themes and is maintained
by the Debian Desktop Theme Team. Upstream distributes Papirus under GPL-3.0.

## Proposal

Create an independently packaged, reproducible OBLinux derivative of Papirus.
All icon classes covered by Papirus belong to the generated Horizon family.
Recognizable application symbols are retained inside a consistent Horizon
container; system artwork is remapped into the OBLinux palette. The approved
original folder/place layer remains the highest-priority identity overlay.

Three original design directions are provided for review. **Horizon Layer** is
recommended because it extends the approved Obsidian Horizon identity, remains
friendly and legible, and can work across light and dark desktop appearances
without excessive variants.

Horizon Layer and the complete-derivative architecture were approved on
2026-08-20. Static application prototypes and a reversible per-user full-theme
trial were approved. This does not yet authorize selecting the theme as the ISO
or installed desktop default; packaging and ISO validation remain separate gates.

## Acceptance gate

No icon theme will be selected as the GNOME default until:

1. the visual direction is approved;
2. a 20–30 icon pilot is reviewed at common icon sizes;
3. light, dark, standard-density, and HiDPI rendering pass;
4. fallback behavior is verified for icons the OBLinux layer does not provide;
5. packaging, copyright, and source-distribution requirements are documented;
6. installation and removal restore the previous GNOME preference cleanly.

## Sources

- Debian package: <https://packages.debian.org/trixie/papirus-icon-theme>
- Upstream project and GPL-3.0 license:
  <https://github.com/PapirusDevelopmentTeam/papirus-icon-theme>
