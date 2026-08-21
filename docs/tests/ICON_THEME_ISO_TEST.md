# OBLinux Horizon ISO integration test

Use this checklist after building an ISO that includes the independently
packaged OBLinux Horizon icon theme.

## Build checks

- `scripts/prepare-icon-theme-package` downloads the pinned Debian
  `papirus-icon-theme` package and builds `oblinux-icon-theme` before
  `lb build` starts.
- The generated `.deb` is under `config/packages.chroot/` and remains ignored
  by Git.
- The image build prints
  `OBLinux Horizon icon-theme package verification passed`.
- `lb build` completes successfully.

## Live-session checks

Boot the ISO in UEFI mode and confirm:

- The live user autologs in successfully.
- The application grid, dock, Files, Settings, and symbolic interface icons use
  the cohesive Horizon treatment.
- The active icon theme is `OBLinux-Horizon-Dark`.
- Both light and dark Horizon themes are available system-wide.
- Switching to `OBLinux-Horizon` and the light color scheme renders correctly.
- Switching back to `OBLinux-Horizon-Dark` renders correctly.
- Calamares remains functional and visually unchanged by this integration.

Run:

```bash
dpkg-query -W oblinux-icon-theme
gsettings get org.gnome.desktop.interface icon-theme
test -r /usr/share/icons/OBLinux-Horizon/index.theme
test -r /usr/share/icons/OBLinux-Horizon-Dark/index.theme
test -r /usr/share/icons/OBLinux-Horizon/icon-theme.cache
test -r /usr/share/icons/OBLinux-Horizon-Dark/icon-theme.cache
find -L /usr/share/icons/OBLinux-Horizon \
  /usr/share/icons/OBLinux-Horizon-Dark -type l -print
```

The final `find` command must print nothing.

## Installed-system checks

Complete a clean Calamares installation and confirm:

- Installation and first boot succeed.
- The installed user receives `OBLinux-Horizon-Dark` as the default icon theme.
- The complete application grid and Files use Horizon consistently.
- Light/dark switching works as it did in the live session.
- `oblinux-icon-theme` remains registered with `dpkg`.
- Both icon caches remain present.
- Calamares and live-only files are still removed by the existing cleanup.
- GRUB, Plymouth, wallpaper, GNOME identity, networking, time synchronization,
  and APT regression checks continue to pass.

## Preference-preservation check

Change the installed user's icon theme to `Adwaita`, then reinstall the package:

```bash
gsettings set org.gnome.desktop.interface icon-theme Adwaita
sudo apt install --reinstall oblinux-icon-theme
gsettings get org.gnome.desktop.interface icon-theme
```

The final command must still report `Adwaita`. Package installation must define
the default for new users without rewriting an existing user's stored choice.
