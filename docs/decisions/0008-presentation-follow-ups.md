# Decision 0008: Presentation Follow-ups

## Status

Accepted for proof-of-concept validation.

## Context

Build 007 functionally passed but retained three presentation findings. The
live medium showed verbose boot output instead of graphical Plymouth, GNOME's
Dash used an old installer icon with white corners, and GNOME About rendered
the correct OBLinux symbol too large.

Investigation identified independent causes:

- The generated live kernel command line omitted Plymouth's conventional
  `quiet splash` parameters.
- The desktop launcher references `Icon=install-debian`, resolved from
  `/usr/share/pixmaps/install-debian.png`, rather than Calamares' product-logo
  file.
- Debian's original compiled vendor emblem declares a 128-by-128 intrinsic
  size, while the OBLinux replacement declared only its 500-by-360 view box.

## Decision

Build 008 will:

- Add `quiet splash` to the live kernel parameters while retaining every
  existing live-boot parameter.
- Replace the package-owned `install-debian.png` launcher asset with the same
  verified transparent OBLinux PNG used by Calamares and validate that the two
  files are byte-identical.
- Declare a 128-by-128 intrinsic size on the active OBLinux vendor SVG while
  preserving its aspect ratio, geometry, colors, view box, and Debian-style
  diversion.

## Consequences

The live system should use the already embedded OBLinux Plymouth theme instead
of exposing routine boot messages. Troubleshooting remains available by
editing the GRUB entry and removing `quiet splash`.

The live launcher and Calamares share one approved transparent raster asset.
Because the launcher path belongs to `calamares-settings-debian`, normal
installer cleanup continues to remove it from the installed system.

GNOME receives the same natural canvas size as Debian's original emblem and
can present the OBLinux symbol at a balanced scale without modifying GNOME
Control Center.
