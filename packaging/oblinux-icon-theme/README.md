# oblinux-icon-theme Debian package

This directory builds the independently versioned OBLinux Horizon icon-theme
package. The generated icon trees are build artifacts and are not stored in Git.

## Build

The source icon root must contain the `Papirus` and `Papirus-Dark` directories
from Debian's pinned `papirus-icon-theme` package.

```bash
packaging/oblinux-icon-theme/build-package.sh \
  /path/to/usr/share/icons \
  /path/to/output
```

The build produces `oblinux-icon-theme_0.1.0-1_all.deb`. Set
`SOURCE_DATE_EPOCH` to reproduce a release with a chosen timestamp. A controlled
test revision may be selected with `PACKAGE_VERSION`; the default remains the
reviewed package version in `build-package.sh`.

For ISO builds, `scripts/prepare-icon-theme-package` obtains the pinned Papirus
input and writes the generated package to `config/packages.chroot/` before
live-build begins. Do not commit that generated binary package or the complete
generated icon trees.

## Default behavior

The package installs both `OBLinux-Horizon` and `OBLinux-Horizon-Dark`. Its GLib
schema override selects the dark variant as the GNOME default because the
approved dark theme has sufficient contrast in both GNOME appearances. The
override changes the system default only; it does not rewrite an existing
user's explicit `gsettings` value during installation or upgrade.

Maintainer scripts rebuild the two icon caches and the system GLib schema cache
after installation, upgrade, or removal. Failures in optional cache tools do not
make package configuration or removal fail.

## Publishing gate

The proof package is assembled directly with `dpkg-deb`, which is available on
a minimal Debian build host. Before publication in an OBLinux APT repository,
convert this source to a normal Debian source package built by `debhelper`, and
repeat the lifecycle tests through APT.
