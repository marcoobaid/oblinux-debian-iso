# GDM Background Is Inconsistent With OBLinux

## Status

Fixed in source; ISO and installed-system verification pending.

## Discovery

After the Debian vendor mark was replaced successfully, the installed GDM
greeter still used a nearly flat neutral background. It was functional but did
not visually align with the dark navy and slate treatment used by the OBLinux
lock screen and other identity surfaces.

## Scope

The correction is limited to the GDM greeter background. It must not change:

- the user's desktop wallpaper;
- GNOME's in-session lock screen;
- account avatars; or
- the existing OBLinux GDM vendor mark.

## Resolution

Create a dedicated GDM dconf profile and system database. Set an image-free
vertical gradient from Obsidian Navy (`#111820`) to Slate Blue (`#1B2836`) and
compile the database during image construction. Retain GDM's packaged defaults
as the lower-priority file database.

## Acceptance criteria

- A clean installation reaches GDM with the approved vertical gradient.
- GDM displays no background image or Debian artwork.
- The existing OBLinux vendor mark remains active.
- User wallpaper changes remain functional.
- Lock and unlock retain the normal GNOME session-lock appearance.
- User-selected account photos remain functional.
- Logout and reboot preserve the GDM-only background treatment.
