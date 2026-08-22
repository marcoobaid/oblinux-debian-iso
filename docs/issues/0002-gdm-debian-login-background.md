# GDM Retains Debian Vendor Mark

## Status

Fixed in source; ISO and installed-system verification pending.

## Discovery

The first physical ThinkPad candidate passed live, installation, hardware, and
daily-driver testing. The installed GDM login screen nevertheless displayed
the Debian 13 vendor mark at the bottom of the screen.

## Cause

GDM's Debian defaults set `org.gnome.login-screen logo` to
`/usr/share/images/vendor-logos/logo-text-version-64.png`. The parent directory
is Debian's `vendor-logos` alternative, whose only candidate was supplied by
`desktop-base`. The earlier login-background correction did not control this
independent logo setting.

This surface is distinct from both the user account avatar and GNOME's
in-session lock screen.

## Resolution

Register a complete OBLinux `vendor-logos` candidate at priority 100 and select
it during image construction. Attach the matching vendor emblems as slaves of
the same alternatives group. Debian's priority-50 candidate remains installed
and recoverable through `update-alternatives`.

## Acceptance criteria

- A clean installation reaches GDM with OBLinux artwork and no Debian 13 mark.
- The selected `vendor-logos` alternative resolves to OBLinux assets.
- User-selected avatars remain functional.
- Lock and unlock retain the expected GNOME session-lock behavior.
- Login, logout, reboot, and `desktop-base` update tests do not revert the
  selected GDM vendor mark.
