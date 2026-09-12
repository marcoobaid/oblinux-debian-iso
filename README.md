# OBLinux Debian — Development

### A polished, practical GNOME desktop on a Debian stable foundation

OBLinux is an experimental Linux distribution project focused on a cohesive,
approachable desktop. This repository, **oblinux-debian-iso-dev**, contains the
Debian development and staging implementation: a live and installable Debian 13
(`trixie`) system with GNOME and the graphical Calamares installer.

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

## Development status

The current version is **26.3.0-dev**. The owner has confirmed successful
regression testing of the current functional baseline on both VMs and physical
hardware and approved it for stable promotion, subject to documentation,
version, and repository checks. See the
[owner regression record](docs/tests/2026-09-11-pre-promotion-owner-regression.md)
for the exact source commit and evidence limits.

This remains a development/staging repository. The stable/production repository
is **oblinux-debian-iso**; promotion is a separate controlled operation requiring
explicit owner authorization. Regression acceptance does not establish a
supported public release or broad hardware compatibility.

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

This repository provides source for building development live/install images.
Use an up-to-date Debian 13 `amd64` build host and follow the
[build guide](docs/BUILDING.md) for dependencies, disk requirements, and the
validated build procedure. Each ISO carries the release version and a generated
build ID, as defined in the [versioning policy](docs/VERSIONING.md).

Start testing in a VM with a disposable disk. The documented installation
baseline is an unencrypted erase-disk installation on UEFI/GPT/ext4. Other
storage layouts, dual boot, encryption, and Secure Boot require separate
approval and testing. Review the [installer guide](docs/INSTALLER.md) and
[testing strategy](docs/TESTING.md) before installing on physical hardware.

## Documentation

| Topic | Guide |
|---|---|
| Project purpose and scope | [Charter](docs/PROJECT_CHARTER.md) · [POC scope](docs/POC_SCOPE.md) |
| Current phase and remaining work | [Roadmap](docs/ROADMAP.md) |
| Building and release identity | [Building](docs/BUILDING.md) · [Versioning](docs/VERSIONING.md) |
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
