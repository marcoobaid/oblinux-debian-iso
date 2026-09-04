# Decision 0013: GNOME About Icon Arch Parity

## Status

Superseded by Decision 0014 after runtime validation.

## Context

Decision 0009 selected a padded, theme-neutral badge and later increased its
intrinsic dimensions to address an apparent scale difference. Runtime
comparison with the Arch edition showed that the 1536-by-1536 padded canvas
and explicit 512-by-512 intrinsic size instead reserve excessive space in
GNOME Control Center and still render the visible symbol differently.

The Debian image already generates
`/usr/share/icons/hicolor/scalable/apps/oblinux-logo.svg` from the pinned Brand
Master release. Its bytes, 512-by-512 viewBox, geometry, and colors match the
icon used by the Arch edition.

## Decision

Debian's scalable vendor-emblem alternative will point directly to the
package-generated `oblinux-logo.svg`. It will not generate a Debian-specific
About wrapper or modify shared Brand Master artwork.

The raster, symbolic, and white vendor-logo alternatives remain unchanged for
their existing consumers. Calamares, Plymouth, the Dash launcher, GRUB,
wallpapers, and account avatars remain outside this decision.

## Consequences

GNOME About uses the same primary product symbol and canvas as Arch, avoiding
the wrapper-induced layout gap and inconsistent visual scale. Light and dark
appearance checks remain required because Debian's GNOME Control Center uses
one fixed scalable vendor-emblem path for both appearances.
