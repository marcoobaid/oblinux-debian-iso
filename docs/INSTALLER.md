# Installer Integration

## Objective

The installer milestone turns the proven GNOME live image into an image that
can install OBLinux onto a disposable virtual disk. The first goal is not to
support every storage layout. It is to prove one safe, repeatable installation
path before adding complexity.

## Installer selection

OBLinux uses Calamares for the POC. Debian 13 packages both Calamares and
`calamares-settings-debian`. The settings package is maintained by Debian's Live
Team for Debian live media and is also intended as an example for derivatives.

Debian's official live-image configuration currently uses the Debian Installer
launcher rather than Calamares. OBLinux is making a deliberate derivative
choice: Calamares integrates naturally with the already-running GNOME live
desktop and matches the intended graphical exploration-and-install workflow.

See [Decision 0003](decisions/0003-calamares-poc-installer.md) for the decision
and tradeoffs.

## First supported scenario

POC Build 002 supports only this acceptance path:

- Oracle VirtualBox
- 64-bit x86 VM
- UEFI enabled
- Blank disposable virtual disk of at least 32 GiB
- Entire disk erased by the installer
- GPT partition table
- EFI System Partition created by the installer
- Ext4 root filesystem
- No disk encryption
- No dual boot or pre-existing operating system
- One regular user with administrative access through `sudo`
- Hostname, locale, keyboard, and timezone selected interactively
- GRUB installed for 64-bit UEFI
- Installation performed from the live session without requiring network access

Anything outside this list is experimental and must not be used on important
storage during this milestone.

## Explicitly unsupported in Build 002

- Installation on either physical laptop
- Manual partitioning
- Reusing an existing EFI System Partition
- Windows or Linux dual boot
- BIOS-mode installation
- LUKS encryption
- Btrfs or another non-ext4 root filesystem
- LVM, RAID, or network storage
- Secure Boot as a tested claim
- Upgrading an existing installation
- Recovery after an interrupted installation

Calamares may display options that are not yet in the supported test scope. A
visible option is not the same as an OBLinux-tested feature.

## Debian package integration

The tracked file `config/package-lists/installer.list.chroot` adds:

- `calamares-settings-debian`, which depends on Calamares and its required
  runtime helpers
- GRUB packages for an installed 64-bit UEFI system
- Debian-signed GRUB and shim components
- `efibootmgr` for creating firmware boot entries
- FAT and ext filesystem utilities used during partitioning and formatting

Because APT recommendations are enabled, Calamares also pulls recommended
filesystem support such as `btrfs-progs`. Its presence does not make Btrfs a
supported Build 002 installation path.

## What Debian's settings do

The packaged workflow:

1. Shows welcome, locale, keyboard, partitioning, user, and summary pages.
2. Partitions and mounts the target disk.
3. Copies `/run/live/medium/live/filesystem.squashfs` to the target using the
   Calamares `unpackfs` module.
4. Replaces live-media APT sources with installed-system sources.
5. Creates machine identity, users, locale, keyboard, timezone, and filesystem
   configuration.
6. Configures the display manager and system services.
7. Installs and configures GRUB.
8. Removes Debian live-session packages and the Debian Calamares settings
   package from the installed system.
9. Regenerates the initramfs and unmounts the target.
10. Offers to restart into the installed system.

Builds 002 through 004 deliberately retained Debian branding and the
`Install Debian` launcher while the unmodified Debian-maintained workflow was
being proven. Build 005 replaces only the identity-facing branding content,
images, palette, slideshow, and launcher metadata. Debian's module sequence,
helpers, and installer behavior remain unchanged.

The overrides use paths owned by `calamares-settings-debian`. When Calamares
removes that package from the target system, it therefore also removes the
installer-only OBLinux branding and launcher. This avoids leaving a separate,
unowned Calamares configuration directory on the installed system. A build
hook verifies that Debian still owns every overridden path and fails the build
if that cleanup invariant changes.

One expected inspection item is whether the generic `calamares` package remains
installed after the settings package removes itself. The installed-system
package manifest must be checked rather than assuming cleanup behavior.

## Destructive-action controls

The first installer tests must use a newly created virtual disk containing no
valuable data. Before clicking the final installation confirmation:

1. Confirm the test VM, not a physical machine, is active.
2. Confirm the displayed disk capacity matches the disposable virtual disk.
3. Confirm the erase-disk choice.
4. Review the summary page and expected EFI and ext4 partitions.
5. Capture a screenshot of the summary.
6. Do not attach host disks, raw disks, or shared block devices to the VM.

The installer should be tested first without another operating system present.

## Build 002 test procedure

### Live environment

- Boot the ISO in a new UEFI VirtualBox VM.
- Confirm the existing live-boot tests still pass.
- Confirm the installer launcher appears.
- Start and cancel the installer before any disk changes.
- Start it again and confirm there is no stale or corrupted state.

### Installation

- Select locale, keyboard, timezone, erase disk, user, hostname, and password.
- Capture the summary page.
- Complete installation and retain the Calamares log.
- Restart when offered.
- Detach the ISO before the VM boots again.

### Installed system

- Confirm GRUB starts the installed system.
- Confirm no live autologin occurs.
- Log in as the created user.
- Confirm the user can run `sudo`.
- Confirm hostname, locale, keyboard, and timezone.
- Confirm networking, GNOME, Firefox ESR, Ptyxis, and LibreOffice.
- Run `sudo apt update` and install available updates.
- Confirm live packages and credentials are absent.
- Inspect whether Calamares or Debian installer branding remains.
- Reboot and shut down successfully.

The entire process must pass twice using freshly created virtual disks before
installer work advances to encryption, manual partitioning, or physical
hardware.

## Build 003 hardening

Build 002 completed two clean UEFI installation passes and one additional
legacy-BIOS installation pass. Build 003 keeps the proven Calamares workflow
and addresses findings from those tests:

- The live-only GNOME schema override disables idle blanking, screen locking,
  and automatic suspend on both AC and battery power. It replaces a file owned
  by `calamares-settings-debian`, so removing that package during installation
  also removes the live-only defaults from the installed system.
- `systemd-timesyncd` provides automatic network time synchronization in the
  live and installed environments.
- An OBLinux-owned final-source helper writes the installed APT policy. It
  enables Debian stable, updates, and security with `main`, `contrib`,
  `non-free`, and `non-free-firmware`; backports and source-package entries are
  not enabled by default.

See [Decision 0004](decisions/0004-installed-apt-policy.md) for the repository
policy and its tradeoffs.

These changes require a new ISO and must be verified in both the live session
and a clean installed system. They do not retroactively modify Build 002.

## Evidence to retain

- ISO checksum
- VirtualBox configuration summary
- Partition-summary screenshot
- Calamares installation log
- Installed disk layout from `lsblk -f`
- EFI boot entries from `efibootmgr -v`
- Installed package checks for live and Calamares packages
- Results of `apt update` and the first reboot
- Any failure message and the exact step at which it occurred

Binary recordings and screenshots remain outside Git. Test reports record their
filenames and SHA-256 checksums.
