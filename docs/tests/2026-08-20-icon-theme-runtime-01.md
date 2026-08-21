# Horizon Layer icon-theme runtime trial 01

- Date: 2026-08-20
- Host: Installed OBLinux test VM
- Scope: Per-user, reversible pilot installation
- Status: Full derived-theme trial active; structural validation passed and
  initial visual direction approved; final visual review and rollback pending

## Baseline

- Original GNOME icon theme: `Adwaita`
- GNOME color scheme: `prefer-dark`
- Failed systemd units: 0
- Pilot absent from system locations

## Installation

The 20-icon pilot was copied into the current user's XDG icon directory. The
original `Adwaita` preference was recorded in the dedicated trial state before
GNOME was switched to `OBLinux-Horizon-Dark`. No root privileges, system package
changes, or ISO rebuild were used.

## Automated results

- Per-user installation: passed
- Light theme selection: passed
- Dark theme selection: passed
- All 20 light-pilot SVGs readable: passed
- All 20 dark-pilot SVGs readable: passed
- Saved rollback preference equals `Adwaita`: passed
- Failed systemd units after activation: 0
- Current active pilot: `OBLinux-Horizon-Dark`

## Finding resolved for the isolated trial: Papirus fallback

The installed test image does not currently contain `papirus-icon-theme`.
Although the OBLinux theme metadata correctly names Papirus and Papirus Dark,
icons outside the OBLinux layer fall through to `hicolor` on this machine.

This is not an icon lookup failure in the OBLinux layer. It confirms that a
future `oblinux-icon-theme` package or ISO integration must declare and install
`papirus-icon-theme` as a dependency.

For the isolated trial, Debian's `papirus-icon-theme` version `20250501-1` was
downloaded without root privileges, extracted into the temporary trial area,
and copied into the test user's local icon directory. The three added theme
directories are recorded in the rollback state. No system package was installed
and no root-owned file changed.

GNOME was toggled through `Adwaita` and back to `OBLinux-Horizon-Dark`, and
GNOME Files was restarted. The active stack is now Horizon overrides followed
by complete Papirus Dark, Papirus, and hicolor fallback.

## Finding: active coverage is smaller than the asset count

The pilot contains 20 original assets, but only nine currently use standard
icon names that GNOME Files can request. The remaining eleven use deliberately
isolated `oblinux-*` names and are visual-language candidates rather than active
system replacements. This explains why GNOME Files visibly changes while the
application grid and most Settings surfaces do not.

The next pilot revision must inventory actual Freedesktop and GNOME lookup
names, add aliases only where semantics match, and distinguish active coverage
from concept coverage in every test record.

## Pending user-visible review

- GNOME Files folder and places presentation
- GNOME Settings and system-category presentation
- Light-appearance contrast
- Dark-appearance contrast
- Application fallback consistency
- Standard-density and HiDPI appearance, where available
- Clean rollback to `Adwaita` and removal of both pilot directories

## Full derivative extension

After the pilot exposed the visual split between Horizon folders and inherited
Papirus applications, the approved scope changed to a complete Papirus-derived
family. The reproducible generator was run against Debian's extracted Papirus
`20250501-1` package and installed per-user without root changes.

- Generated base theme: 43,463 SVG files, including 20 original identity icons
- Generated dark supplement: 3,954 SVG files
- Broken aliases after Papirus-to-Horizon retargeting: 0
- Active theme: `OBLinux-Horizon-Dark`
- Original theme retained for rollback: `Adwaita`
- Representative application treatment: approved
- GNOME Files identity layer: approved

The full theme remains active for final coverage review. It must not be selected
as the ISO default until light/dark coverage and clean rollback pass, followed
by independent Debian packaging and a fresh-image installation test.
