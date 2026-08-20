# OBLinux

OBLinux is an experimental Debian-based desktop distribution focused on a
polished, dependable, and approachable Linux experience.

The project is currently in the proof-of-concept stage. Its immediate goal is
to produce a GNOME-based live and installable system suitable for daily use by
the project's maintainer. Public distribution, additional desktop flavors, and
custom graphical administration tools are later goals.

## Current status

The project has produced repeatable Debian 13 GNOME live images and has
completed Calamares installation testing in both UEFI and legacy-BIOS VMs.
POC Build 004 passed live and installed-system verification of the OBLinux
Obsidian Horizon wallpaper integration. POC Build 005 passed live GRUB,
Calamares, installation, cleanup, and regression acceptance with four branding
follow-ups. POC Build 006 passed installation, cleanup, regression, GRUB,
Plymouth, and Calamares contrast acceptance with three presentation-only logo
follow-ups. POC Build 007 functionally passed installation and visual-polish
acceptance with three presentation follow-ups for live Plymouth, the Dash
installer icon, and GNOME About logo sizing. There is no supported public
release yet.

## Documentation

- [Project charter](docs/PROJECT_CHARTER.md)
- [Proof-of-concept scope](docs/POC_SCOPE.md)
- [Roadmap](docs/ROADMAP.md)
- [Initial architecture](docs/ARCHITECTURE.md)
- [Testing strategy](docs/TESTING.md)
- [Build instructions](docs/BUILDING.md)
- [Installer integration and test plan](docs/INSTALLER.md)
- [POC build 001 record](docs/builds/2026-08-17-poc-001.md)
- [POC build 002 installer record](docs/builds/2026-08-18-poc-002.md)
- [POC build 003 hardening record](docs/builds/2026-08-19-poc-003.md)
- [POC build 003 installation test](docs/tests/2026-08-19-poc-003-install-01.md)
- [POC build 004 branding record](docs/builds/2026-08-20-poc-004.md)
- [POC build 004 installation test](docs/tests/2026-08-20-poc-004-install-01.md)
- [POC build 005 branding record](docs/builds/2026-08-20-poc-005.md)
- [POC build 005 installation test](docs/tests/2026-08-20-poc-005-install-01.md)
- [POC build 006 installed-identity record](docs/builds/2026-08-20-poc-006.md)
- [POC build 006 installation test](docs/tests/2026-08-20-poc-006-install-01.md)
- [POC build 007 visual-polish record](docs/builds/2026-08-20-poc-007.md)
- [POC build 007 installation test](docs/tests/2026-08-20-poc-007-install-01.md)
- [POC build 002 installation test 01](docs/tests/2026-08-18-poc-002-install-01.md)
- [POC build 002 installation test 02](docs/tests/2026-08-18-poc-002-install-02.md)
- [POC build 001 VirtualBox test](docs/tests/2026-08-17-poc-001-virtualbox.md)
- [Daily-driver requirements](docs/DAILY_DRIVER_REQUIREMENTS.md)
- [Hardware targets](docs/HARDWARE_TARGETS.md)
- [Decision 0001: Debian stable and live-build](docs/decisions/0001-debian-stable-live-build.md)
- [Decision 0002: GNOME-first scope](docs/decisions/0002-gnome-first.md)
- [Decision 0003: Calamares POC installer](docs/decisions/0003-calamares-poc-installer.md)
- [Decision 0004: Installed-system APT policy](docs/decisions/0004-installed-apt-policy.md)
- [Decision 0005: OBLinux visual identity](docs/decisions/0005-oblinux-visual-identity.md)
- [Decision 0006: Installed-system identity](docs/decisions/0006-installed-system-identity.md)
- [Decision 0007: Identity asset polish](docs/decisions/0007-identity-asset-polish.md)
- [OBLinux brand guide](branding/BRAND_GUIDE.md)

## Project principles

- Stay close to Debian stable and modify as little as practical.
- Prefer configuration and small OBLinux packages over rebuilding Debian
  packages.
- Automate every build so the dedicated build machine is replaceable.
- Treat installation, updates, and recovery as core product features.
- Do not describe experimental behavior as supported or secure until tested.
- Keep documentation professional, project-focused, and free of personal names.

## License

Original OBLinux code and documentation in this repository are licensed under
the [GNU General Public License version 3](LICENSE). Branding and redistributed
third-party assets must have compatible, explicitly documented licenses before
the first public release.
