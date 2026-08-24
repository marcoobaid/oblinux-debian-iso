# Brand Master v1.0.1 runtime test

Use a disposable VM with UEFI, a blank virtual disk, and the generated dev ISO.
Record the ISO SHA-256 and tested commit before beginning.

## Live journey

- GRUB visibly identifies OBLinux with the proportional R5 lockup, readable
  white text, and orange selection.
- Plymouth displays a centered, crisp R5 symbol and animated five-dot
  white/orange progress indicator without legacy artwork.
- GNOME starts with Obsidian Horizon in both light and dark appearance modes.
- Settings lists Obsidian Horizon variants and the complete Brand Master
  wallpaper collection.
- GNOME About identifies OBLinux and resolves `oblinux-logo`.
- The installer launcher uses the R5 installer icon.
- Calamares shows the proportional R5 lockup, navy/blue sidebar with readable
  white/orange navigation, seven canonical R5 slides, and completion state.

## Installed journey

- Complete the documented blank-disk installation baseline and reboot.
- Installed GRUB retains normal and advanced/recovery entries and R5 styling.
- Plymouth renders during boot, shutdown, and reboot.
- GDM retains the supported OBLinux dark gradient and product identity.
- `/etc/os-release` reports OBLinux with `ID_LIKE=debian`.
- GNOME retains Obsidian Horizon as its light/dark and lock-screen default and
  retains the hicolor icons.
- `/etc/issue`, `/etc/issue.net`, and `/etc/motd` use restrained OBLinux text.
- No legacy OBLinux or unintended Debian product artwork appears.

Do not record a pass for any surface that was not directly observed.
