# Initial Architecture

## System model

OBLinux begins as a thin Debian derivative rather than an independent package
ecosystem.

```text
Debian stable repositories
          |
          v
Versioned live-build configuration
          |
          +-- common package lists and hooks
          +-- GNOME flavor configuration
          +-- OBLinux branding and defaults
          +-- installer configuration
          |
          v
Hybrid live/install ISO
          |
          +-- VM validation
          +-- physical-hardware validation
          v
Installed system using normal Debian updates
```

## Base

- Release: Debian 13 stable (`trixie`)
- Initial architecture: `amd64`
- Image framework: Debian `live-build`, `live-boot`, and `live-config`
- Desktop: GNOME from Debian stable
- Package management: APT and `dpkg`

Testing and unstable packages must not be mixed into the POC. Backports require
a documented need and should be explicitly selected rather than globally
preferred.

## Configuration layers

The future build tree should separate:

1. Common base configuration
2. GNOME-specific package selection and settings
3. Live-session behavior
4. Installer configuration
5. Branding assets
6. OBLinux-owned packages
7. Build and verification scripts

This structure leaves room for later flavors without requiring them during the
POC.

## OBLinux packages

Defaults that must survive installation and updates should ultimately be
delivered as small Debian packages. Likely examples include:

- `oblinux-base`
- `oblinux-archive-keyring`
- `oblinux-desktop-gnome`
- `oblinux-branding`
- `oblinux-calamares-settings`

These names are provisional. The POC may initially use live-build includes and
hooks while the correct package boundaries are discovered. Before public
release, persistent changes should be migrated into policy-compliant packages
where practical.

## Installer

Calamares is the initial graphical-installer candidate because Debian packages
both Calamares and Debian-oriented settings. It must still be treated as a
separate integration project. The POC installer specification will identify
supported partitioning, encryption, bootloader, locale, user-creation, and
failure-recovery scenarios.

The first tests should use disposable virtual disks. Installation on physical
hardware must not begin until the exact storage layout and recovery path are
documented.

## Package repository

The POC should avoid operating an OBLinux repository until at least one custom
package needs independent updates. Local packages can initially be included in
the ISO build.

When a repository becomes necessary, it must have signed metadata, scoped APT
trust using `Signed-By`, versioned suites, source-package handling, promotion
between development and stable channels, key backup, and key-rotation
procedures. A development repository must not be presented as production-ready.

## Artifact hosting

GitHub is intended to hold source, documentation, issues, and release metadata.
An ISO may use GitHub Releases only while it fits the per-asset size limit.
Artifact storage and the APT repository should remain replaceable components so
that larger images or public traffic do not force a source-repository redesign.

## Build host

The dedicated build machine should run a supported Debian release and produce
images inside clean, disposable build environments. Its state must not be the
only record of how an image was created. Required packages, commands, inputs,
logs, manifests, checksums, and output names must be generated or documented by
the repository.

## Deferred production architecture

The following require separate designs before public release:

- Secure Boot key and shim strategy
- Production archive signing and offline key custody
- Public artifact hosting and mirrors
- Vulnerability response and security advisories
- Major-version upgrades
- Source redistribution and license compliance
- Automated release CI and provenance attestations

