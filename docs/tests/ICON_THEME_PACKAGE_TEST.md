# OBLinux icon-theme package lifecycle test

Run this test on a disposable installed OBLinux VM before integrating the package
into the ISO.

## Baseline

Record the current package state and explicit user preference:

```bash
dpkg-query -W oblinux-icon-theme 2>/dev/null || true
gsettings get org.gnome.desktop.interface icon-theme
```

## Install

```bash
sudo apt install ./oblinux-icon-theme_0.1.0-1_all.deb
dpkg-query -W oblinux-icon-theme
test -r /usr/share/icons/OBLinux-Horizon/index.theme
test -r /usr/share/icons/OBLinux-Horizon-Dark/index.theme
```

Confirm that installing the package did not replace an existing explicit user
preference. A newly created test account should receive
`OBLinux-Horizon-Dark` as its default.

## Appearance and cache checks

Select each variant and review GNOME Files, the application grid, Settings,
menus, dialogs, and small toolbar/sidebar icons:

```bash
gsettings set org.gnome.desktop.interface icon-theme OBLinux-Horizon
gsettings set org.gnome.desktop.interface color-scheme default

gsettings set org.gnome.desktop.interface icon-theme OBLinux-Horizon-Dark
gsettings set org.gnome.desktop.interface color-scheme prefer-dark
```

Confirm that both theme directories contain a readable `icon-theme.cache` after
package configuration and that no broken symlinks exist.

## Upgrade

Reinstall the same artifact, then install a package with a higher test revision.
Confirm the package configures cleanly, existing user preferences remain intact,
and the theme caches are regenerated.

## Removal and rollback

First select a non-OBLinux theme for the test account, then remove the package:

```bash
gsettings set org.gnome.desktop.interface icon-theme Adwaita
sudo apt remove oblinux-icon-theme
test ! -e /usr/share/icons/OBLinux-Horizon
test ! -e /usr/share/icons/OBLinux-Horizon-Dark
```

Confirm GNOME remains usable, the stored user preference is still `Adwaita`, and
the package can be installed again without residual errors.
