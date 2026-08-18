# Decision 0003: Calamares for the POC Installer

- Status: Accepted for the POC
- Date: 2026-08-18

## Context

OBLinux needs a graphical installer launched from its GNOME live session. The
project could use Debian Installer or Calamares. Debian's official live-image
configuration uses a Debian Installer launcher, while Debian also packages and
maintains `calamares-settings-debian` for Debian live media and as an example
for derivative distributions.

The project has prior experience with Calamares, and the desired user journey is
to explore a complete graphical desktop before choosing installation.

## Decision

The POC will integrate Debian 13's packaged Calamares and unmodified
`calamares-settings-debian` configuration first. The initial supported scenario
is an unencrypted, erase-disk, ext4 installation to a blank UEFI VirtualBox
disk.

OBLinux branding and configuration overrides will not be introduced until this
baseline completes two clean installations.

## Consequences

- The first installer image will visibly use Debian branding and an `Install
  Debian` launcher.
- OBLinux benefits from a configuration maintained and exercised within Debian.
- A Qt/KDE Frameworks runtime is added to the GNOME live image because Calamares
  is a Qt application.
- The ISO will grow and may exceed GitHub Releases' 2 GiB per-asset limit.
- The installer copies the tested live filesystem rather than constructing an
  unrelated system through a separate installation path.
- Options visible in Calamares are not automatically supported by OBLinux.
- The installed system must be inspected for leftover installer packages and
  branding before creating OBLinux-specific settings.

