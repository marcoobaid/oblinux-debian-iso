#!/bin/sh
set -eu

data_root=${XDG_DATA_HOME:-"$HOME/.local/share"}
state_root=${XDG_STATE_HOME:-"$HOME/.local/state"}/oblinux-icon-theme-trial
icon_root=$data_root/icons
state_file=$state_root/original-icon-theme

test -r "$state_file" || {
    echo "ERROR: no active OBLinux icon-theme trial state was found" >&2
    exit 1
}

original=$(sed -n '1p' "$state_file")
test -n "$original" || {
    echo "ERROR: saved original icon theme is empty" >&2
    exit 1
}

gsettings set org.gnome.desktop.interface icon-theme "$original"
rm -rf -- \
    "$icon_root/OBLinux-Horizon" \
    "$icon_root/OBLinux-Horizon-Dark"
rm -f -- "$state_file"
rmdir "$state_root" 2>/dev/null || true

echo "PASS: restored icon theme: $original"
echo "PASS: removed the per-user OBLinux Horizon pilot"

