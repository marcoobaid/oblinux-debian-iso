# Building OBLinux

## Purpose

This guide explains both how to build OBLinux and what the Debian tools are
doing. It is maintained alongside the build configuration so that the build can
be understood, repeated, and moved to another machine without relying on
undocumented setup.

The current milestone is an experimental Debian 13 `amd64` GNOME live and
installable ISO. Three POC images have been built successfully, and the
Calamares baseline has completed repeatable VM installations. The image is not
a supported release.

## What has been completed

The following work preceded the first ISO build:

1. A private Git repository was initialized with project, architecture,
   hardware, testing, and roadmap documentation.
2. A Debian 13 build VM was prepared with 4 virtual CPUs, approximately 8 GiB
   of RAM, and sufficient initial working storage.
3. SSH public-key authentication was configured for remote administration. The
   private key remains on the administration workstation.
4. The builder was verified as Debian 13.6 `amd64`, and its CPU, memory, disk,
   SSH, and `sudo` behavior were checked without changing the system.
5. The required build packages were installed through APT by an administrator.
6. The installed Debian 13 `live-build` interface and example configuration
   were inspected rather than assuming commands from another distribution or
   Debian release.
7. A minimal GNOME live-image configuration and package list were added to the
   repository.
8. Every selected package was checked for availability in the builder's
   configured Debian repositories.
9. `lb config --validate` was run on the builder. Validation found that both
   GRUB and Syslinux had initially been selected for BIOS boot. The
   configuration was corrected to use GRUB for UEFI and BIOS, then validation
   passed.
10. A snapshot of the private Git repository was transferred to the builder as
    a Git bundle, checked out on `main`, and validated again from the permanent
    build workspace.

The build command requires root privileges, and the builder is intentionally
configured to ask the administrator for a `sudo` password. Passwords must not
be stored in scripts, logs, documentation, or the repository.

## The Debian image-building model

OBLinux uses Debian's Live Systems toolchain rather than assembling an ISO by
copying files manually.

```text
Debian repositories
        |
        v
debootstrap creates a minimal Debian filesystem
        |
        v
live-build installs selected packages into a chroot
        |
        v
the filesystem is compressed into SquashFS
        |
        v
GRUB, kernel, initramfs, and ISO metadata are assembled
        |
        v
hybrid ISO boots as optical media or from USB
```

Important Debian concepts:

- **APT** resolves and downloads signed packages from configured repositories.
- **debootstrap** creates a minimal Debian system in a directory without first
  booting that system.
- A **chroot** is a filesystem tree in which build commands operate as though
  that tree were the root filesystem. It is not a VM and shares the builder's
  kernel.
- **live-build** orchestrates bootstrap, package installation, customization,
  compression, and ISO assembly.
- **SquashFS** is the compressed, read-only filesystem stored in the live ISO.
- **live-boot** finds and mounts that filesystem during startup and adds a
  writable temporary layer in memory.
- **live-config** performs live-session setup such as hostname, locale, and live
  user configuration.
- A **hybrid ISO** can be attached as virtual optical media or written directly
  to a USB device.

Changes made while running the live environment disappear at shutdown unless a
future persistence feature is explicitly implemented.

## Build-host requirements

Use an up-to-date Debian 13 `amd64` system with root access and at least 40 GB of
free working space. Sixty GB or more is recommended for repeated builds and
retained artifacts. Build on a native Linux filesystem rather than a VirtualBox
shared folder.

The current build can run in a VM. The builder and the VM used to test the ISO
should be separate systems. Nested virtualization is not required to build an
ISO.

Install the initial build dependencies:

```bash
sudo apt update
sudo apt install \
  ca-certificates debootstrap dosfstools git grub-efi-amd64-bin grub-pc-bin \
  isolinux live-build mtools rsync squashfs-tools syslinux-utils xorriso
```

What these packages provide:

| Package | Purpose |
| --- | --- |
| `live-build` | Coordinates creation of the live filesystem and ISO. |
| `debootstrap` | Creates the initial minimal Debian filesystem. |
| `squashfs-tools` | Compresses the live root filesystem. |
| `xorriso` | Creates and manipulates ISO 9660 images. |
| `grub-efi-amd64-bin` | Provides GRUB components for 64-bit UEFI boot. |
| `grub-pc-bin` | Provides GRUB components for legacy BIOS boot. |
| `dosfstools` and `mtools` | Create and populate FAT filesystems used by EFI boot media. |
| `isolinux` and `syslinux-utils` | Supporting boot-media utilities; Syslinux is not currently the selected bootloader. |
| `ca-certificates` | Validates HTTPS certificates while downloading packages. |
| `git` and `rsync` | Version-control and file-transfer tools used by the workflow. |

`sudo apt update` refreshes local repository indexes; it does not upgrade the
system. `sudo apt install` then resolves, verifies, downloads, and installs the
requested packages and dependencies.

## Repository structure

The relevant tracked files are:

```text
auto/
├── build
├── clean
└── config
config/
└── package-lists/
    └── desktop.list.chroot
docs/
└── BUILDING.md
```

### `auto/config`

Running `lb config` automatically invokes `auto/config`. This script is the
authoritative record of the image type, Debian release, architecture,
repositories, bootloaders, live-user parameters, compression, and ISO identity.

The script calls `lb config noauto`. The `noauto` argument is essential: without
it, `lb config` would invoke `auto/config` again and recurse.

Current significant settings:

| Setting | Meaning |
| --- | --- |
| `--distribution trixie` | Build from Debian 13 stable. |
| `--architecture amd64` | Build for 64-bit Intel and AMD PCs. |
| `--binary-image iso-hybrid` | Produce an ISO usable in a VM or on USB. |
| `--archive-areas ...` | Permit Debian main, contrib, non-free, and firmware packages. |
| `--apt-secure true` | Require authenticated repository metadata. |
| `--debian-installer none` | Do not add an installer to this milestone. |
| `--firmware-binary true` | Include applicable firmware in the bootable image. |
| `--firmware-chroot true` | Include applicable firmware in the live filesystem. |
| `--bootloaders "grub-efi grub-pc"` | Use GRUB for UEFI and legacy BIOS. |
| `username=live` | Request the unprivileged live account named `live`. |
| `hostname=oblinux-live` | Set the live-session hostname. |
| `--checksums sha256` | Generate SHA-256 integrity information. |
| `--chroot-squashfs-compression-type xz` | Favor a smaller ISO at the cost of build time. |

The Secure Boot setting is currently `auto`. This permits live-build to use
Debian's available signed boot components, but it is not yet an OBLinux Secure
Boot support claim. Secure Boot must be tested separately on real hardware.

### `config/package-lists/desktop.list.chroot`

Files ending in `.list.chroot` identify packages installed inside the live
filesystem. The current list provides:

- Debian live-session integration
- Debian's GNOME desktop task
- NetworkManager and Wi-Fi support
- Firmware update support
- Firefox ESR and Ptyxis
- Firmware and CPU microcode for the initial AMD ThinkPad and Intel Surface
  targets
- Basic hardware and network diagnostic tools

The first generated package manifest showed that Debian's GNOME task also
installs LibreOffice and much of the CUPS printing stack through its dependency
graph. These components are therefore present even though they are not named in
OBLinux's short explicit list. Always use the generated package manifest to
describe the actual image contents.

Debian tasks such as `task-gnome-desktop` are curated package collections. Using
the Debian task lets Debian define the coherent GNOME baseline while OBLinux
adds only its explicit requirements.

### `config/includes.chroot`

Files under `config/includes.chroot` are copied into the image filesystem after
package installation. Build 004 uses this mechanism for the approved OBLinux
wallpapers, their GNOME catalog, licensing, and background defaults.

The background schema override defines unlocked defaults. It remains in the
installed system so new users start with the OBLinux wallpaper but can change
it normally. This is deliberately separate from the package-owned Calamares
override containing live-only lock and suspend settings, which the installer
removes from the target system.

Build 005 also uses package-owned Calamares paths under this directory to
replace only Debian's identity-facing images, descriptor, slideshow, desktop
launcher, and icon. The installer settings, modules, and helper sequence remain
Debian-maintained. A chroot hook verifies package ownership so the branding is
removed with `calamares-settings-debian` after installation.

Build 006 adds installed-system identity through an OBLinux os-release file,
hicolor icon, GRUB defaults, and Plymouth theme. Unlike the Calamares files,
these are intentional installed-system defaults and must remain after cleanup.
The identity hook validates all required fields, updates the icon cache, and
applies a guarded OBLinux-only branch to Debian's GRUB title logic. It also
compiles a dedicated GDM dconf database for an image-free Obsidian Navy to
Slate Blue greeter gradient. That database is isolated from desktop wallpaper,
session lock-screen, avatar, and vendor-mark settings.

Build 008 adds `quiet splash` to the generated live kernel command line, uses
the approved transparent Calamares symbol at the package-owned Dash launcher
icon path, and gives GNOME's diverted vendor emblem Debian's expected
128-by-128 intrinsic canvas size.

### `config/bootloaders`

Files under `config/bootloaders` override Debian live-build's corresponding
bootloader resources. Build 005 supplies an SVG background and a GRUB theme;
live-build converts the SVG and applies the same generated GRUB configuration
to UEFI and legacy-BIOS media. Kernel discovery, boot parameters, utility
entries, and integrity checks remain generated by live-build.

### `auto/build`

Running `sudo lb build` automatically invokes `auto/build`. The wrapper stores a
timestamped log under `build-logs/`, prepares the independently versioned
`oblinux-icon-theme` package, and then executes `lb build noauto`.

The preparation script downloads the explicitly pinned Debian
`papirus-icon-theme` binary package, extracts its icon sources in a temporary
directory, generates both complete OBLinux Horizon variants, and builds a local
Debian package under `config/packages.chroot/`. Live-build installs that package
into the image through its normal local-package mechanism. Generated icon trees
and `.deb` artifacts remain excluded from Git.

The default pinned inputs are:

- `papirus-icon-theme` `20250501-1`
- `oblinux-icon-theme` `0.1.0-2`

`PAPIRUS_VERSION` and `PACKAGE_VERSION` may be set for a controlled package
test, but release builds should use reviewed, documented values.

It uses Bash `pipefail` so an `lb build` failure remains a failed command even
though output is also sent through `tee`. Without `pipefail`, the successful
logging process could hide a failed build.

### `auto/clean`

Running `lb clean` invokes `auto/clean`, which delegates to `lb clean noauto`.
Cleaning removes generated build state; it does not replace the tracked source
configuration.

## Source files versus generated files

Commit these inputs:

- `auto/`
- Deliberately authored files under `config/`
- Documentation and future scripts, tests, packages, and branding sources

Do not commit these outputs:

- `chroot/`
- `binary/`
- `cache/`
- Generated ISO, image, checksum, and package-manifest files
- Generated local Debian packages under `config/packages.chroot/`
- `build-logs/`

These are excluded through `.gitignore`. An ISO should eventually be published
as a release artifact, not committed to Git history.

Some files directly under `config/` are generated by `lb config`. Do not edit
generated values to make permanent changes. Change `auto/config`, clean the
generated state when necessary, and regenerate it.

Live-build also generates standard hook links under `config/hooks/normal/` and
the `0010-disable-kexec-tools` and `0050-disable-sysvinit-tmpfs` live hooks.
These generated links are ignored; authored OBLinux hooks remain tracked.

Debian's standard `9000-remove-gnome-icon-cache` hook removes icon caches near
the end of the chroot stage. OBLinux therefore regenerates the Horizon Light
and Horizon Dark caches in its later `0130-verify-oblinux-icon-theme` hook,
then verifies them before the live filesystem is packaged. The package list
explicitly includes `libglib2.0-bin` and `gtk-update-icon-cache`; these hook
dependencies must not rely on their incidental inclusion by another package.

## Getting the source onto a builder

A builder with authorized access to the private repository can clone it:

```bash
git clone <repository-url>
cd oblinux-debian-iso
```

The initial builder was deliberately not given GitHub credentials. Instead, an
administrator created a Git bundle from `main`, copied it to the builder, cloned
the bundle, and checked out its `main` reference. A bundle is a transportable
snapshot of Git objects and history, not an ongoing connection to GitHub.

Consequently, `git pull` on that initial builder is not currently the supported
update method. Later revisions can be transferred as new bundles, synchronized
from the administration workstation, or fetched after a narrowly scoped GitHub
deploy key is configured.

## Configure and validate

From the repository root:

```bash
lb config
lb config --validate
```

`lb config` translates `auto/config` into live-build's generated configuration
tree. `lb config --validate` checks whether the selected options form a valid
combination. Validation is valuable but cannot prove that all downloads,
package installation, boot behavior, or hardware support will succeed.

The initial validation exposed an invalid selection of two BIOS bootloaders.
OBLinux now selects `grub-efi` for UEFI and `grub-pc` for BIOS. This is an
example of why configuration validation precedes a full build.

## Run a build

From an interactive shell on the builder:

```bash
cd ~/oblinux-debian-iso
sudo lb build
```

Or start it from an administration workstation over SSH:

```bash
ssh -t <builder> \
  'cd ~/oblinux-debian-iso && sudo lb build'
```

The `-t` option allocates a terminal so `sudo` can ask for the administrator's
password. Do not place a password in the command, documentation, environment,
or repository.

During the build, live-build will roughly perform these stages:

1. Download the pinned Papirus input and build the local OBLinux icon package.
2. Bootstrap a minimal Trixie filesystem.
3. Configure Debian package repositories inside the chroot.
4. Install the kernel, live components, GNOME, firmware, selected apps, and the
   local OBLinux icon package.
5. Apply configured hooks and included OBLinux files.
6. Verify both Horizon themes, their caches, aliases, package status, and GNOME
   default.
7. Remove temporary package data as appropriate.
8. Compress the live filesystem into SquashFS.
9. Assemble GRUB boot files and the hybrid ISO.
10. Generate checksums and package/file metadata.

The first build can take 20–60 minutes depending on network and compression
speed. The generated ISO is expected to be named
`oblinux-debian-gnome-amd64.hybrid.iso`, although live-build controls the final
architecture suffix.

## Inspect results

After a successful build:

```bash
ls -lh *.iso* build-logs/
sha256sum *.iso
```

The checksum produced by `sha256sum` can be compared after copying the ISO to
another machine. A matching checksum proves that the file was transferred
without changing; it does not by itself establish who produced the ISO.

Do not clean immediately after a failure. Preserve the final terminal output,
the timestamped build log, and generated state until the cause is understood.

## Clean rebuilds

A package-list change can often reuse cached downloads, but fundamental
configuration changes should receive a clean build:

```bash
sudo lb clean --purge
lb config
sudo lb build
```

`--purge` removes more cached state and causes additional downloads. Use it when
reproducibility matters or stale state is suspected, not reflexively after every
failure.

## Image acceptance criteria

- `lb config` and `lb config --validate` complete without errors.
- `lb build` completes and produces a hybrid ISO.
- A SHA-256 checksum is generated.
- The ISO boots in a VirtualBox UEFI VM.
- GNOME reaches the desktop.
- The live session uses the unprivileged `live` account without manual login.
- NetworkManager establishes network connectivity.
- Firefox ESR and Ptyxis launch.
- `oblinux-icon-theme` is installed and Horizon Dark is the GNOME default.
- Reboot and shutdown work.

## Not included yet

- The remaining daily-driver application set and explicit default policies
- Zsh and Starship defaults
- Flatpak or third-party application repositories
- Firewall configuration
- Production signing or release automation
