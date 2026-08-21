# Issue 0001: Debian artwork appears as the lock-screen user avatar

- Status: Resolved and runtime-validated
- First observed: 2026-08-20
- Surface: Installed-system GNOME lock screen
- Severity: Presentation only

## Observation

When an installed user's session locks, GNOME displays a red circular Debian
swirl above the account name instead of an OBLinux identity or a neutral user
avatar. The Debian artwork has not been observed on the normal GNOME desktop
or the already-correct GNOME Settings About surface.

Evidence was supplied from an installed system using a personal account. A
personal account name must not be embedded in project configuration or generic
documentation examples.

## Expected result

The lock screen should show either:

- the user's explicitly chosen account image;
- an approved OBLinux default avatar; or
- GNOME's neutral generated-user avatar.

It must not present Debian artwork as OBLinux's primary identity.

## Root cause

Debian's `desktop-base` package owns `/etc/skel/.face` and the accompanying
`.face.icon` link. Calamares creates the installed account from `/etc/skel`, so
the package-provided Debian face is copied byte-for-byte to the new user's
home as `~/.face`. GDM and the GNOME lock screen then display that file.

## Prepared correction

The installed-identity hook locally diverts the package-owned skeleton face,
preserving it as `/etc/skel/.face.distrib`, and installs the approved neutral
Horizon user silhouette at `/etc/skel/.face`. This changes only the default for
accounts created afterward. It does not inspect or overwrite existing home
directories, and any user-selected account photo continues to take precedence.

Runtime validation on 2026-08-21 confirmed that the neutral Horizon avatar is
shown on the lock screen when no custom image is selected. Selecting a custom
account photo through GNOME Settings then replaced the default at GDM after
logout, confirming that normal user control retains precedence.
