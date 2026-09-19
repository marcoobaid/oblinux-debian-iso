<div align="center">

<img src="https://raw.githubusercontent.com/marcoobaid/oblinux-brand-master/13e211da2ccd43156fcc7dc7e57c3be7bb5ee47d/themes/calamares/oblinux/welcome.svg" alt="OBLinux" width="520">

### A polished, practical GNOME desktop on a Debian stable foundation

[![License: GPL-3.0](https://img.shields.io/badge/License-GPL--3.0-FF8A00.svg)](LICENSE)
[![Base: Debian 13](https://img.shields.io/badge/Base-Debian%2013-1E4D8C.svg)](https://www.debian.org/)
[![Desktop: GNOME](https://img.shields.io/badge/Desktop-GNOME-1E4D8C.svg)](https://www.gnome.org/)
[![Installer: Calamares](https://img.shields.io/badge/Installer-Calamares-0B1118.svg)](https://calamares.io/)

</div>

OBLinux is an experimental Linux distribution project focused on a cohesive,
approachable desktop. This repository, **oblinux-debian-iso**, contains the
Stable Debian implementation: a live and installable Debian 13 (`trixie`)
system with GNOME and the graphical Calamares installer.

## What is OBLinux?

The Debian edition combines Debian stable packages and updates with OBLinux
desktop defaults, installer integration, and a shared visual identity. It stays
close to Debian, using APT and small, visible configuration changes rather than
maintaining an independent package ecosystem.

## Highlights

- Debian 13 stable on `amd64`, with normal Debian updates through APT
- GNOME with user-configurable wallpapers, appearance, and application defaults
- Obsidian Horizon desktop and lock-screen defaults, plus Horizon application icons
- Shared R5 identity across boot, login, installer, and terminal presentation
- A live session for evaluation and a graphical Calamares installation workflow
- Firefox ESR, Ptyxis, Zsh, Starship, and FastFetch

Released assets from **OBLinux Brand Master** provide the shared R5 visual
identity across OBLinux editions. Debian supplies its own integration and
retains Obsidian Horizon as its desktop default. Shared artwork is maintained
upstream and consumed from immutable releases.

## Release status

OBLinux Debian **26.3.0 is released**. The following certified Stable
artifact passed installation and regression testing on both a virtual machine
and physical laptop.

- Git tag: `v26.3.0`
- Certified source commit: `8f28de66fc43c4bf1d9f76b0880810eefd6c519b`
- ISO: `oblinux-debian-26.3.0-20260918-2040-amd64.iso`
- BUILD_ID: `20260918-2040`
- SHA-256: `6af928461580ccb29be6997eeca1534010038b5c97aaf001b8fc03d4f2243db7`
- Published on SourceForge: `OBLinux-Debian-ISO/26.3.0/`

The certified release code is frozen. Later documentation updates do not change
the certified source commit or immutable release tag.

See the [release procedure](docs/RELEASING.md) for provenance and the limited
installation/hardware scope. Release status does not imply broad hardware
compatibility.

## Technology

| Component | Selection |
|---|---|
| Foundation | Debian 13 stable (`trixie`), `amd64` |
| ISO framework | Debian `live-build`, `live-boot`, and `live-config` |
| Desktop | GNOME |
| Installer | Calamares with Debian's packaged settings workflow |
| Package management | APT and `dpkg` |
| Terminal | Ptyxis with Zsh and Starship |
| Live boot | GRUB for UEFI and legacy BIOS |

## Building and trying OBLinux

This repository provides source for building the Stable live/install image.
Use an up-to-date Debian 13 `amd64` build host and follow the
[build guide](docs/BUILDING.md) for dependencies, disk requirements, and the
validated build procedure. Each ISO carries the release version and a generated
build ID, as defined in the [versioning policy](docs/VERSIONING.md).

Start testing in a VM with a disposable disk. The documented installation
baseline is an unencrypted erase-disk installation on UEFI/GPT/ext4. Other
storage layouts, dual boot, encryption, and Secure Boot remain outside the
validated installation baseline. Review the [installer guide](docs/INSTALLER.md) and
[testing strategy](docs/TESTING.md) before installing on physical hardware.

## Documentation

| Topic | Guide |
|---|---|
| Project purpose and scope | [Charter](docs/PROJECT_CHARTER.md) · [POC scope](docs/POC_SCOPE.md) |
| Current phase and remaining work | [Roadmap](docs/ROADMAP.md) |
| Building and release identity | [Building](docs/BUILDING.md) · [Versioning](docs/VERSIONING.md) |
| Release procedure and publishing | [Releasing](docs/RELEASING.md) |
| Architecture and installation | [Architecture](docs/ARCHITECTURE.md) · [Installer](docs/INSTALLER.md) |
| Desktop identity | [Brand Master integration](docs/BRAND_MASTER_INTEGRATION.md) |
| Validation and hardware | [Testing](docs/TESTING.md) · [Hardware targets](docs/HARDWARE_TARGETS.md) |
| Workstation requirements | [Daily-driver requirements](docs/DAILY_DRIVER_REQUIREMENTS.md) |
| Project records | [Decisions](docs/decisions/) · [Known issues](docs/issues/) · [Tests](docs/tests/) · [Builds](docs/builds/) |

## Contributing

Keep contributions focused and consistent with the documented Debian
architecture. Prefer upstream mechanisms, preserve user choices, and update
relevant documentation when behavior changes. Validation reports should
distinguish static checks, ISO builds, live boot, installation, and hardware
testing. Shared visual changes belong in OBLinux Brand Master.

## License

Original OBLinux code and documentation in this repository are licensed under
the [GNU General Public License version 3](LICENSE). Branding and redistributed
third-party assets retain their documented licenses and attributions; public
release requires license and source-distribution compliance review.
