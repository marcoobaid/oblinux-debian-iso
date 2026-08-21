#!/bin/sh
set -eu

if test "$#" -ne 2; then
    echo "Usage: $0 PAPIRUS_ICON_ROOT OUTPUT_DIRECTORY" >&2
    exit 2
fi

package_version=${PACKAGE_VERSION:-0.1.0-2}
papirus_root=$1
output_root=$2
script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
repository_root=$(CDPATH= cd -- "$script_dir/../.." && pwd)
generator=$repository_root/branding/icon-theme/source/build_papirus_derivative.py
overlay=$repository_root/branding/icon-theme/pilot/OBLinux-Horizon
notice=$repository_root/branding/icon-theme/PAPIRUS-NOTICE.md
license=$repository_root/LICENSE
source_date_epoch=${SOURCE_DATE_EPOCH:-946684800}
export SOURCE_DATE_EPOCH=$source_date_epoch

case "$package_version" in
    *[!0-9A-Za-z.+:~\-]*|'')
        echo "ERROR: invalid Debian package version: $package_version" >&2
        exit 2
        ;;
esac

for required in \
    "$papirus_root/Papirus/index.theme" \
    "$papirus_root/Papirus-Dark/index.theme" \
    "$generator" \
    "$overlay/index.theme" \
    "$notice" \
    "$license"; do
    if test ! -r "$required"; then
        echo "ERROR: required input is missing: $required" >&2
        exit 1
    fi
done

command -v python3 >/dev/null 2>&1 || {
    echo "ERROR: python3 is required" >&2
    exit 1
}
command -v dpkg-deb >/dev/null 2>&1 || {
    echo "ERROR: dpkg-deb is required" >&2
    exit 1
}

mkdir -p "$output_root"
work_root=$(mktemp -d "${TMPDIR:-/tmp}/oblinux-icon-package.XXXXXX")
trap 'rm -rf -- "$work_root"' EXIT HUP INT TERM
payload=$work_root/payload
generated=$work_root/generated

mkdir -p \
    "$payload/DEBIAN" \
    "$payload/usr/share/icons" \
    "$payload/usr/share/glib-2.0/schemas" \
    "$payload/usr/share/doc/oblinux-icon-theme"

python3 "$generator" --overlay "$overlay" "$papirus_root" "$generated"
cp -a "$generated/OBLinux-Horizon" "$payload/usr/share/icons/"
cp -a "$generated/OBLinux-Horizon-Dark" "$payload/usr/share/icons/"
cp "$script_dir/90_oblinux-icon-theme.gschema.override" \
    "$payload/usr/share/glib-2.0/schemas/"
cp "$notice" "$payload/usr/share/doc/oblinux-icon-theme/PAPIRUS-NOTICE.md"
cp "$license" "$payload/usr/share/doc/oblinux-icon-theme/copyright"
cp "$script_dir/postinst" "$payload/DEBIAN/postinst"
cp "$script_dir/postrm" "$payload/DEBIAN/postrm"
chmod 0755 "$payload/DEBIAN/postinst" "$payload/DEBIAN/postrm"

installed_size=$(du -sk "$payload/usr" | awk '{print $1}')
sed \
    -e "s/@VERSION@/$package_version/" \
    "$script_dir/control.in" > "$payload/DEBIAN/control"
printf 'Installed-Size: %s\n' "$installed_size" >> "$payload/DEBIAN/control"

find "$payload" -exec touch -h -d "@$source_date_epoch" {} +
artifact=$output_root/oblinux-icon-theme_${package_version}_all.deb
DPKG_DEB_THREADS_MAX=1 dpkg-deb --root-owner-group -Zxz --build "$payload" "$artifact"
sha256sum "$artifact" > "$artifact.sha256"
echo "Built $artifact"
