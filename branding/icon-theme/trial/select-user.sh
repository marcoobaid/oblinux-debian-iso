#!/bin/sh
set -eu

case ${1:-} in
    light) theme=OBLinux-Horizon ;;
    dark) theme=OBLinux-Horizon-Dark ;;
    *) echo "Usage: $0 light|dark" >&2; exit 2 ;;
esac

data_root=${XDG_DATA_HOME:-"$HOME/.local/share"}
test -r "$data_root/icons/$theme/index.theme" || {
    echo "ERROR: $theme is not installed for the current user" >&2
    exit 1
}
gsettings set org.gnome.desktop.interface icon-theme "$theme"
echo "Selected $theme"

