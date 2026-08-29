# Calamares Welcome lockup remediation

## Result

- Status: successful purge build; static and payload verification passed
- Runtime visual status: pending owner boot test
- ISO: `oblinux-debian-gnome-amd64.hybrid.iso`
- Size: `2183526400` bytes
- SHA-256:
  `f6e4a03ccc3cfc05e650c443979c1f9a3d9f2c2f3d1b44f0ae485038e68ffbe9`
- Build log:
  `/home/marco/oblinux-debian-iso-dev/build-logs/build-20260829T014338Z.log`

## Root cause

The earlier v1.0.4 ISO reused a retained chroot after `lb clean --binary`, so
the downstream Calamares activation hook did not run. The ISO therefore
contained Brand Master's package defaults: a native-size Welcome image and
unresolved descriptor tokens. See
[Issue 0006](../issues/0006-calamares-welcome-lockup-stale-chroot.md).

## Changes and build

- Preserved Brand Master v1.0.4 and its R5 artwork byte-for-byte.
- Retained Calamares' proportional `FixedAspectRatioLabel` path by activating
  `welcomeExpandingLogo: true`.
- Replaced optional versioned display names with the primary `OBLinux` product
  identity; the expected heading is `Welcome to the OBLinux installer`.
- Added fail-closed assertions for the four version fields.
- Documented that branding-package updates require `lb clean --purge` and
  artifact-level descriptor inspection.
- Ran `sudo lb clean --purge`, `lb config`, `lb config --validate`, and a full
  `sudo lb build` on the Debian 13 amd64 builder.

The build executed the Brand Master activation, Calamares branding, installed
identity, Horizon icon, and terminal hooks successfully. Brand Master's own
validation passed with 27 required assets and 40 SVGs.

## Payload verification

Read-only inspection of the ISO's SquashFS confirmed:

- `calamares` `3.3.14-1`, `calamares-settings-debian` `13.0.13-1`, and
  `oblinux-branding` `1.0.4-1`;
- `welcomeExpandingLogo: true`;
- empty optional `version` and `shortVersion` values;
- `versionedName: OBLinux` and `shortVersionedName: OBLinux`;
- no unresolved `@TOKEN@` value in `branding.desc`;
- the accepted navy, white, and orange sidebar colors remain unchanged; and
- the ISO and package copies of `welcome.svg` share SHA-256
  `0f1369646943183fa22b15f8fa2999cf88fb48b50c8c9d6705f26110f76b9ee9`.

## Size-path validation

Source inspection of Debian's Calamares 3.3.14 implementation confirmed that
the activated setting scales the Welcome pixmap to the available label content
rectangle using `Qt::KeepAspectRatio`. This bounds both width and height,
centers the label, and cannot crop or stretch the image as the installer window
changes size. The same invariant was checked for 1024x768, 1280x800, and
1920x1080 viewports; the initial 900x600 window also fits within each viewport.

This is static implementation and payload validation, not a visual boot test.
The builder has no offscreen X server and Codex did not boot the ISO in a VM.
Owner runtime confirmation of the Welcome page at normal and maximized sizes
remains required before the regression is marked runtime-passed.
