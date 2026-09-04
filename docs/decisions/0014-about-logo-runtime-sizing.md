# Decision 0014: GNOME About Logo Runtime Sizing

## Status

Accepted for proof-of-concept validation; revised after source-level comparison
with Arch and Debian GNOME Control Center.

## Context

Both editions set `LOGO=oblinux-logo`, and Brand Master's hicolor icon files in
Debian are byte-identical to the files installed by Arch. Their scalable source
is an SVG with no intrinsic width or height and a `viewBox` of `0 0 512 512`.

The editions nevertheless use different GNOME Control Center code paths. Arch
uses upstream `setup_os_logo()`: it reads `LOGO`, resolves that name through
`GtkIconTheme`, and requests a 192-pixel `GtkIconPaintable`. Debian builds GNOME
Control Center with `DISTRIBUTOR_LOGO` set to
`/usr/share/icons/vendor/scalable/emblems/emblem-vendor.svg`; that compile-time
path bypasses `LOGO` and calls `gtk_picture_set_filename()` directly. The UI
sets `can-shrink` to false. Consequently, intrinsic file dimensions affect the
Debian presentation while Arch's icon-theme lookup explicitly constrains it to
192 pixels.

Previous Debian wrappers added transparent padding and declared a 512-pixel
intrinsic size. They did not reproduce Arch's icon-resolution contract and
runtime comparison remained inconsistent.

## Decision

Debian's scalable vendor-emblem alternative will select a generated direct-file
variant at `/usr/share/oblinux/branding/oblinux-about-gnome.svg`. The build
copies the same package-generated hicolor SVG resolved by Arch and adds only
`width="192" height="192"`, matching the explicit size requested by Arch's
GNOME Control Center code. Its `viewBox="0 0 512 512"`, paths, colors, and
transparent canvas remain unchanged. No speculative padding is added.

The normal `oblinux-logo` hicolor icon remains byte-identical to Arch and stays
selected by `LOGO=oblinux-logo`, Calamares, and the installer launcher. Raster,
symbolic, and white vendor-logo alternatives remain unchanged.

## Consequences

Static inputs now give both code paths the same artwork and a 192-pixel size
request. A rebuilt ISO must still be checked in both live and installed
sessions, at the same display resolution and scaling as the Arch comparison.
Light and dark appearance checks remain required; static equivalence is not a
claim of runtime acceptance.
