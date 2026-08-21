# OBLinux Horizon icon-theme runtime trial

This procedure evaluates the standalone icon pilot in an installed GNOME user
session. It does not require root, alter system packages, or rebuild the ISO.

## Safety model

The installer saves the current GNOME icon-theme preference before making a
change. It refuses to overwrite an existing trial state. The rollback script
restores that preference and removes only these exact per-user directories:

- `~/.local/share/icons/OBLinux-Horizon`
- `~/.local/share/icons/OBLinux-Horizon-Dark`

Do not manually delete the saved state while a trial is active.

## Install and inspect

From the repository root:

```bash
branding/icon-theme/trial/install-user.sh
branding/icon-theme/trial/check-user.sh
```

Open GNOME Files and Settings. Inspect folders, Home, common places, devices,
and system categories at normal zoom. Confirm that applications not supplied by
OBLinux still resolve through Papirus.

Test both variants while also changing GNOME Appearance to the corresponding
light or dark style:

```bash
branding/icon-theme/trial/select-user.sh light
branding/icon-theme/trial/select-user.sh dark
```

Check 100% and 200% display scale if available. Record missing icons, ambiguous
glyphs, poor contrast, clipping, inconsistent optical size, and icons that are
too detailed at small sizes.

## Roll back

```bash
branding/icon-theme/trial/rollback-user.sh
```

Confirm the prior icon theme is active and the two pilot directories are gone.

## Acceptance criteria

- Both variants can be selected without errors.
- OBLinux-owned icons appear on the expected GNOME surfaces.
- Missing icons fall back to the appropriate Papirus variant.
- Light and dark appearances remain legible.
- Common sizes and HiDPI rendering have no clipping or severe blur.
- Rollback restores the exact prior preference and removes the pilot.

