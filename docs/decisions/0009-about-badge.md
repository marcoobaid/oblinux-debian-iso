# Decision 0009: GNOME About Badge

## Status

Accepted for proof-of-concept validation.

## Context

Build 008 corrected GNOME About identity and sizing. Its Obsidian Navy letters
rendered professionally on a light background but lacked sufficient contrast
against GNOME's dark appearance.

Debian 13 compiles GNOME Control Center with one fixed distributor-logo path
for both light and dark appearances. Supplying separate theme-aware assets
would require rebuilding and maintaining an OBLinux-specific GNOME Control
Center package solely for this cosmetic distinction.

## Decision

OBLinux will use a theme-neutral badge only for GNOME Settings About:

- an intentional rounded Obsidian Navy background;
- the approved reversed Soft White OB letterforms;
- the approved Clear Cyan horizon bridge;
- the existing 128-by-128 intrinsic size expected by Debian's vendor emblem.

Regression testing later showed that the padded badge still rendered
significantly smaller than the Arch edition. The Debian presentation wrapper
therefore declares a 512-by-512 intrinsic canvas, matching Arch's scalable
product icon canvas while retaining this theme-neutral badge and its geometry.

Calamares, Plymouth, the Dash launcher, GRUB, wallpapers, and the primary
symbol assets remain unchanged.

## Consequences

GNOME About receives consistent contrast in light and dark appearances without
forking a security-sensitive Debian desktop package. The badge is a deliberate
surface-specific container, not a replacement for the primary transparent
OBLinux symbol or wordmark.
