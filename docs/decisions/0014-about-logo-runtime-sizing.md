# Decision 0014: GNOME About Logo Runtime Sizing

## Status

Accepted for proof-of-concept validation.

## Context

Decision 0013 pointed Debian's compiled scalable vendor-emblem path directly at
the same tightly cropped 512-by-512 product icon used by Arch. Runtime testing
showed that Debian GNOME Control Center renders that SVG dramatically larger
than Arch. The two editions do not use the same presentation mechanism: Arch
resolves the `LOGO=oblinux-logo` icon name from `os-release`, while Debian's
package is compiled to load the vendor emblem directly.

The earlier Debian presentation wrapper used Brand Master's dedicated padded
About asset. Its 1536-by-1536 viewBox preserves the canonical logo geometry and
colors while reducing the visible mark within the area allocated by Debian.

## Decision

Debian's scalable vendor-emblem alternative will again select a generated
presentation wrapper at
`/usr/share/oblinux/branding/oblinux-about-gnome.svg`. The build copies the
immutable Brand Master About asset and adds explicit 512-by-512 intrinsic
dimensions; it does not modify the package-owned source artwork.

The normal `oblinux-logo` hicolor icon remains byte-identical to Arch and stays
selected by `LOGO=oblinux-logo`, Calamares, and the installer launcher. Raster,
symbolic, and white vendor-logo alternatives remain unchanged.

## Consequences

GNOME About uses the same visible logo scale as Arch despite the distribution-
specific GNOME Control Center lookup behavior. A rebuilt ISO must be checked in
both live and installed sessions, at the same display resolution and scaling as
the Arch comparison. Light and dark appearance checks remain required.
