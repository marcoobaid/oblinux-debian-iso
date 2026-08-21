#!/bin/sh
set -eu

data_root=${XDG_DATA_HOME:-"$HOME/.local/share"}
icon_root=$data_root/icons
light_theme=OBLinux-Horizon
dark_theme=OBLinux-Horizon-Dark

for theme in "$light_theme" "$dark_theme"; do
    test -r "$icon_root/$theme/index.theme" || {
        echo "FAIL: missing $theme" >&2
        exit 1
    }
done

test -L "$icon_root/$dark_theme/scalable" || {
    echo "FAIL: dark pilot does not share the OBLinux SVG layer" >&2
    exit 1
}

test -r "$icon_root/$dark_theme/scalable/places/folder.svg"
test "$(find "$icon_root/$light_theme/scalable" -type f -name '*.svg' | wc -l | tr -d ' ')" = 20

printf 'Active icon theme: '
gsettings get org.gnome.desktop.interface icon-theme
printf 'GNOME color scheme: '
gsettings get org.gnome.desktop.interface color-scheme
echo "PASS: both pilot variants and all 20 source icons are readable"

