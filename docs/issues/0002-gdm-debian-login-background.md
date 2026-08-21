# GDM Retains Debian Login Background

## Status

Fixed in source; ISO and installed-system verification pending.

## Discovery

The first physical ThinkPad candidate passed live, installation, hardware, and
daily-driver testing. The installed GDM login screen nevertheless displayed
Debian 13 artwork at the bottom of the screen.

## Cause

Debian's `desktop-base` package manages GDM vendor artwork through the
`desktop-login-background` alternatives group. OBLinux branded the desktop,
bootloader, Plymouth, GNOME About, installer, icons, and default account avatar
but had not supplied a candidate for this alternatives group. GDM therefore
resolved the Debian active-theme background.

This surface is distinct from both the user account avatar and GNOME's
in-session lock screen.

## Resolution

Register the existing branded Obsidian Horizon 3840-by-2160 wallpaper as the
OBLinux `desktop-login-background` candidate with priority 100 and select it
explicitly during image construction. Debian's packaged backgrounds remain
installed and recoverable through `update-alternatives`.

## Acceptance criteria

- A clean installation reaches GDM with OBLinux artwork and no Debian 13 mark.
- The selected alternative resolves to the branded OBLinux wallpaper.
- User-selected avatars remain functional.
- Lock and unlock retain the expected GNOME session-lock behavior.
- Login, logout, reboot, and `desktop-base` update tests do not revert the
  selected GDM background.
