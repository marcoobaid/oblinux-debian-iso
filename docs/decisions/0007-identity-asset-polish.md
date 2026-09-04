# Decision 0007: Identity Asset Polish

## Status

Accepted for proof-of-concept validation.

## Context

Build 006 passed functional acceptance but exposed three presentation defects.
GNOME Settings displayed the correct OBLinux name with Debian's logo, while the
Calamares and Plymouth logos showed white corner artifacts.

Inspection established two distinct causes:

- Debian 13 compiles GNOME Control Center with
  `/usr/share/icons/vendor/scalable/emblems/emblem-vendor.svg` as a fixed
  distributor-logo path. That build-time setting takes precedence over the
  `LOGO` value in `os-release`.
- The Calamares and Plymouth PNGs were fully opaque. Rasterizing the rounded
  application-icon source flattened its outside corners to white instead of
  preserving transparency.

## Decision

Build 007 will:

- Preserve Debian's package-provided vendor emblem with a local
  `dpkg-divert`, then install the approved OBLinux color symbol at GNOME Control
  Center's compiled distributor-logo path.
- Continue publishing `LOGO=oblinux-logo` and the hicolor icon for software
  that follows the standard `os-release` lookup.
- Generate Calamares branding from the approved reversed symbol rather than
  the rounded application-icon tile.
- Tightly crop the rendered symbol, fit it proportionally within a transparent
  square for Calamares, and reject source images without transparent pixels.
- Give Plymouth a tightly cropped transparent logo and scale it without
  changing its aspect ratio.

## Consequences

GNOME About can show OBLinux without rebuilding or binary-patching Debian's
GNOME Control Center package. The diversion preserves Debian's original file
and prevents package upgrades from silently replacing the OBLinux identity.
A future OBLinux identity package should own this diversion and asset.

Calamares and Plymouth retain the approved symbol geometry and palette while
allowing their native backgrounds to show through every unused pixel. The
asset-generation checks make recurrence of the opaque-corner defect less
likely.

## Later GNOME 48 refinement

The About-specific mapping described in this section was later superseded by
Decision 0013 after side-by-side runtime testing with the Arch edition.

Runtime testing of the R5 v1.0.2 integration confirmed the earlier stable
mechanism: Debian's GNOME Control Center uses its compiled scalable vendor
emblem and honors that SVG's intrinsic size. The Debian edition derives a
256-by-256 presentation wrapper from Brand Master's padded About asset, twice
the runtime-tested stable baseline, and
retains `oblinux-logo` as the normal `os-release` and application icon. This
refines the consumer mapping without changing the original artwork decision.
