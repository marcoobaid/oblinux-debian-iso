# OBLinux

OBLinux is an experimental Debian-based desktop distribution focused on a
polished, dependable, and approachable Linux experience.

The project is currently in the proof-of-concept stage. Its immediate goal is
to produce a GNOME-based live and installable system suitable for daily use by
the project's maintainer. Public distribution, additional desktop flavors, and
custom graphical administration tools are later goals.

## Current status

No ISO or supported release exists yet. The current work is limited to project
definition and planning.

## Documentation

- [Project charter](docs/PROJECT_CHARTER.md)
- [Proof-of-concept scope](docs/POC_SCOPE.md)
- [Roadmap](docs/ROADMAP.md)
- [Initial architecture](docs/ARCHITECTURE.md)
- [Testing strategy](docs/TESTING.md)
- [Build instructions](docs/BUILDING.md)
- [POC build 001 record](docs/builds/2026-08-17-poc-001.md)
- [POC build 001 VirtualBox test](docs/tests/2026-08-17-poc-001-virtualbox.md)
- [Daily-driver requirements](docs/DAILY_DRIVER_REQUIREMENTS.md)
- [Hardware targets](docs/HARDWARE_TARGETS.md)
- [Decision 0001: Debian stable and live-build](docs/decisions/0001-debian-stable-live-build.md)
- [Decision 0002: GNOME-first scope](docs/decisions/0002-gnome-first.md)

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
