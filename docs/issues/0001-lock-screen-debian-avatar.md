# Issue 0001: Debian artwork appears as the lock-screen user avatar

- Status: Confirmed; deferred until the icon-theme milestone is complete
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

## Deferred investigation

After the icon-theme milestone, determine whether the image originates from an
AccountsService default, a distribution-provided face asset, an installed
vendor icon, or another GDM/GNOME fallback. The eventual fix must preserve
user-selected account photos and avoid assigning a project logo as if it were
the user's personal image without an explicit product decision.

No corrective change is included with this issue record.
