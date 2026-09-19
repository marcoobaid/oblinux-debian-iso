# Proof-of-Concept Scope

## POC goal

Build an installable Debian 13 stable GNOME system for personal daily use and
use it to evaluate the effort required to operate OBLinux over time.

## Public Stable 26.3.0 transition

The original POC has progressed to public Stable 26.3.0. The Stable ISO is
published on SourceForge under `OBLinux-Debian-ISO/26.3.0/`, and tag `v26.3.0`
identifies the certified source commit. Final VM and physical laptop
installation/regression testing passed. This expands distribution
scope, not hardware or installer support claims. See [RELEASING.md](RELEASING.md)
for the certified artifact details.

## In scope

- Debian 13 stable as the base distribution
- `amd64` architecture
- Debian `live-build` configuration stored in version control
- GNOME desktop
- Bootable hybrid ISO for VM and USB use
- An unprivileged, automatically logged-in live user
- Calamares using Debian's packaged installer settings
- UEFI boot on the primary target hardware
- A curated but restrained default application set
- Debian `main`, `contrib`, `non-free`, `non-free-firmware`, security, and stable updates as
  explicitly approved by project policy
- Basic OBLinux name, wallpaper, colors, and installer identity
- VM tests followed by installation on a designated physical test machine
- Package and build manifests for each image
- A documented rollback, backup, and recovery approach for daily-driver trials

## Conditionally in scope

These items are included only if required by the target hardware or daily
workload:

- Proprietary graphics drivers
- Flatpak and Flathub
- Full-disk encryption
- Windows dual boot
- Secure Boot
- A small development-only OBLinux APT repository

Each conditional item must have a recorded requirement and test case before it
is added.

## Out of scope for the first POC

- Public support commitments
- Multiple architectures
- i3, Qtile, or other flavors
- A custom control center or graphical package manager
- A complete custom icon theme
- Public mirrors or a production CDN
- Broad hardware compatibility claims
- OEM installation
- Automated upgrades between Debian major versions
- Telemetry or user analytics

## Daily-driver trial entry criteria

The physical installation may become the primary workstation only after:

1. Important data is backed up and restoration has been tested.
2. The same ISO completes at least two clean VM installations.
3. Networking, graphics, audio, storage, suspend, resume, and updates work on
   the target hardware.
4. The installer partition plan has been reviewed before execution.
5. Recovery media and a previous working operating system remain available.
6. Known limitations are recorded.

## POC completion criteria

After a meaningful daily-use trial, record:

- Build frequency and hands-on maintenance time
- Update failures and regressions
- Hardware or workflow gaps
- Installer defects
- OBLinux-specific packages that became necessary
- Documentation gaps
- Whether the project should proceed, narrow its scope, or stop
