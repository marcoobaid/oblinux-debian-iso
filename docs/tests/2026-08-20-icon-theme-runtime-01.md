# Horizon Layer icon-theme runtime trial 01

- Date: 2026-08-20
- Host: Installed OBLinux test VM
- Scope: Per-user, reversible pilot installation
- Status: In progress; automated checks passed with one dependency finding,
  visual review and rollback pending

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

## Finding: Papirus fallback is absent

The installed test image does not currently contain `papirus-icon-theme`.
Although the OBLinux theme metadata correctly names Papirus and Papirus Dark,
icons outside the OBLinux layer fall through to `hicolor` on this machine.

This is not an icon lookup failure in the OBLinux layer. It confirms that a
future `oblinux-icon-theme` package or ISO integration must declare and install
`papirus-icon-theme` as a dependency. Papirus will not be installed as an
unrecorded system mutation during this trial.

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

The pilot remains active for visual inspection. It is not accepted and must not
be integrated into the ISO until the remaining checks and rollback pass.
