# Decision 0006: Installed-System Identity

## Status

Accepted for proof-of-concept validation.

## Context

Build 005 proved the OBLinux live GRUB and Calamares identity but exposed four
remaining Debian-branded surfaces: GNOME About, installed GRUB, Plymouth, and
low Calamares sidebar contrast.

OBLinux must identify itself clearly without concealing its Debian base or
forking more Debian-maintained behavior than necessary.

## Decision

Build 006 will:

- Provide consistent OBLinux `/etc/os-release` and `/usr/lib/os-release` files
  with `ID=oblinux`, `ID_LIKE=debian`, an OBLinux product name, and an explicit
  Debian 13 base description.
- Install the approved OBLinux symbol through the standard hicolor icon theme
  and reference it with the os-release `LOGO` field.
- Set installed GRUB's distributor and full Obsidian Horizon theme through a
  dedicated `/etc/default/grub.d` fragment.
- Apply a guarded one-line adjustment to Debian's `10_linux` title logic so
  OBLinux is not automatically suffixed with `GNU/Linux`.
- Install and select an OBLinux Plymouth script theme using only Plymouth
  components already present in the Debian GNOME image.
- Raise the Calamares sidebar from Obsidian Navy to Slate Blue while retaining
  the approved current-step and text colors.

## Consequences

GNOME and freedesktop-compatible tools will identify the derivative as OBLinux
and can still recognize Debian compatibility through `ID_LIKE`. Debian remains
named as the base in the human-readable version fields.

The guarded GRUB script adjustment is intentionally narrow and fails the image
build if Debian changes the expected logic. A future OBLinux package should own
and reapply this integration across GRUB package upgrades; the direct POC
adjustment is not the final maintenance design.

The Plymouth theme supports normal progress, messages, password prompts, and
questions. Disk encryption remains outside the current supported installation
scope and requires separate end-to-end testing before it is claimed.
