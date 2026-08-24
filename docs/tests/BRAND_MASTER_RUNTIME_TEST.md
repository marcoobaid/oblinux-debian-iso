# Brand Master v1.0.0 runtime test

Use a disposable VM with UEFI, a blank virtual disk, and the generated dev ISO.
Record the ISO SHA-256 and tested commit before beginning.

## Live journey

- GRUB uses the R5 background, readable white text, and orange selection.
- Plymouth displays a centered, crisp R5 symbol without legacy artwork.
- GNOME starts with Default Light or Default Dark according to appearance.
- Settings lists the complete OBLinux wallpaper collection.
- GNOME About identifies OBLinux and resolves `oblinux-logo`.
- The installer launcher uses the R5 installer icon.
- Calamares shows the R5 lockup, sidebar styling, seven slides, and completion state.

## Installed journey

- Complete the documented blank-disk installation baseline and reboot.
- Installed GRUB retains normal and advanced/recovery entries and R5 styling.
- Plymouth renders during boot, shutdown, and reboot.
- GDM retains the supported OBLinux dark gradient and product identity.
- `/etc/os-release` reports OBLinux with `ID_LIKE=debian`.
- GNOME retains paired light/dark wallpaper defaults and the hicolor icons.
- `/etc/issue`, `/etc/issue.net`, and `/etc/motd` use restrained OBLinux text.
- No legacy OBLinux or unintended Debian product artwork appears.

Do not record a pass for any surface that was not directly observed.
