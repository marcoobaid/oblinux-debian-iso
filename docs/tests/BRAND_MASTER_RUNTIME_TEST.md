# Brand Master v1.0.4 runtime test

Use a disposable VM with UEFI, a blank virtual disk, and the exact candidate ISO
(Dev before promotion; Stable before release). Record its filename, VERSION,
BUILD_ID, SHA-256, tested commit, and environment before beginning. See
[release evidence requirements](../RELEASING.md).

## Live journey

- GRUB visibly identifies OBLinux with the proportional R5 lockup, readable
  white text, and orange selection.
- Plymouth displays a centered, crisp R5 symbol and animated five-dot
  white/orange progress indicator without legacy artwork.
- GNOME starts with Obsidian Horizon in both light and dark appearance modes.
- Settings lists Obsidian Horizon variants and the complete Brand Master
  wallpaper collection.
- GNOME About identifies OBLinux using Debian's vendor-emblem alternative and
  the documented 192-pixel variant of the shared hicolor SVG. Check light/dark
  appearance and scaling; `LOGO=oblinux-logo` alone does not verify this path.
- The installer launcher uses the R5 installer icon.
- Calamares shows the proportional R5 lockup, navy/blue sidebar with readable
  white/orange navigation, seven canonical R5 slides, and completion state.
- FastFetch displays the higher-fidelity 30×15 shared R5 symbol in OBLinux blue
  and orange, without the legacy OB wordmark, missing-file errors, or alignment
  problems. Its curved outer geometry, orange internal form, and negative
  spaces should read more clearly as R5 than the v1.0.3 rendition.
- FastFetch retains the concise Debian system summary, including package count,
  and remains readable at normal terminal dimensions.

## Installed journey

- Complete the documented blank-disk installation baseline and reboot.
- Installed GRUB retains normal and advanced/recovery entries and R5 styling.
- Plymouth renders during boot, shutdown, and reboot.
- GDM retains the supported OBLinux dark gradient and product identity.
- `/etc/os-release` reports OBLinux with `ID_LIKE=debian`.
- GNOME retains Obsidian Horizon as its light/dark and lock-screen default and
  retains the hicolor icons.
- `/etc/issue`, `/etc/issue.net`, and `/etc/motd` use restrained OBLinux text.
- `/etc/xdg/fastfetch/config.jsonc` references
  `/usr/share/oblinux/terminal/fastfetch/logo.txt` and applies to new users
  without a seeded per-user configuration. No legacy `oblinux.txt` is seeded.
- A user's own `~/.config/fastfetch/config.jsonc` overrides the system default.
- An existing user's customized FastFetch configuration is not overwritten by
  the package upgrade.
- No legacy OBLinux or unintended Debian product artwork appears.

Do not record a pass for any surface that was not directly observed.
