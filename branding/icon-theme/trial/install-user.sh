#!/bin/sh
set -eu

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
theme_root=$(dirname -- "$script_dir")/pilot
data_root=${XDG_DATA_HOME:-"$HOME/.local/share"}
state_root=${XDG_STATE_HOME:-"$HOME/.local/state"}/oblinux-icon-theme-trial
icon_root=$data_root/icons
light_theme=OBLinux-Horizon
dark_theme=OBLinux-Horizon-Dark

for theme in "$light_theme" "$dark_theme"; do
    test -r "$theme_root/$theme/index.theme" || {
        echo "ERROR: missing pilot theme: $theme_root/$theme" >&2
        exit 1
    }
done

if test -e "$state_root/original-icon-theme"; then
    echo "ERROR: an OBLinux icon-theme trial is already active" >&2
    echo "Run rollback-user.sh before starting another trial." >&2
    exit 1
fi

mkdir -p "$state_root" "$icon_root"
original=$(gsettings get org.gnome.desktop.interface icon-theme)
original=${original#\'}
original=${original%\'}
printf '%s\n' "$original" > "$state_root/original-icon-theme"

for theme in "$light_theme" "$dark_theme"; do
    target=$icon_root/$theme
    test ! -e "$target" || {
        echo "ERROR: target already exists: $target" >&2
        exit 1
    }
    cp -R "$theme_root/$theme" "$target"
    if command -v gtk-update-icon-cache >/dev/null 2>&1; then
        gtk-update-icon-cache --force --ignore-theme-index "$target" >/dev/null
    fi
done

scheme=$(gsettings get org.gnome.desktop.interface color-scheme)
case "$scheme" in
    *prefer-dark*) selected=$dark_theme ;;
    *) selected=$light_theme ;;
esac
gsettings set org.gnome.desktop.interface icon-theme "$selected"

echo "PASS: installed the OBLinux Horizon pilot for the current user"
echo "Previous theme: $original"
echo "Selected theme: $selected"
echo "Rollback script: $script_dir/rollback-user.sh"

