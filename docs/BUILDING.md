# Building OBLinux

## Purpose

This guide explains both how to build OBLinux and what the Debian tools are
doing. It is maintained alongside the build configuration so that the build can
be understood, repeated, and moved to another machine without relying on
undocumented setup.

The current milestone is an experimental Debian 13 `amd64` GNOME live and
installable ISO. The current functional baseline has completed owner regression
testing on VMs and physical hardware; see the
[confirmation and evidence limits](tests/2026-09-11-pre-promotion-owner-regression.md).
This remains the development/staging repository, not a supported public release.

Release versions and exact build identities follow the policy in
[VERSIONING.md](VERSIONING.md). The root `VERSION` file is the release source
of truth.

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
  ca-certificates curl debhelper debootstrap dosfstools dpkg-dev git \
  grub-efi-amd64-bin grub-pc-bin isolinux live-build mtools rsync \
  librsvg2-bin python3 squashfs-tools syslinux-utils xorriso
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
| `curl`, `dpkg-dev`, `debhelper`, `python3`, `python3-pil`, and `librsvg2-bin` | Fetch, validate, and build the pinned Brand Master Debian package. |
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
package installation. Shared visual assets are installed by the pinned
`oblinux-branding` package instead of being duplicated here. Includes retain
Debian-specific configuration such as system identity, GDM defaults, and the
Calamares launcher.

The background schema override defines unlocked defaults. It remains in the
installed system so new users start with the OBLinux wallpaper but can change
it normally. This is deliberately separate from the package-owned Calamares
override containing live-only lock and suspend settings, which the installer
removes from the target system.

The Brand Master package supplies Calamares identity images, its descriptor,
and slideshow. A chroot hook renders Debian release URLs into the descriptor
and selects it while preserving Debian's installer settings, modules, and
helper sequence.

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
bootloader resources. The build preparation step extracts the live GRUB
background from the verified Brand Master package into an ignored generated
path. The tracked downstream theme controls only menu integration; kernel
discovery, boot parameters, utility entries, and integrity checks remain
generated by live-build.

### `auto/build`

Running `sudo lb build` automatically invokes `auto/build`. At entry, the
wrapper reads `VERSION` and generates `BUILD_ID` exactly once from local build
time in `YYYYMMDD-HHMM` form. It records those values and the image name in the
ignored `.build/oblinux-release` file, renders both `os-release` paths, and
uses live-build's `--image-name` setting for the versioned artifact. The same
wrapper stores a build-ID-named log under `build-logs/`, validates the branding
pin, prepares the pinned `oblinux-branding` package and independently versioned
`oblinux-icon-theme` package, and then executes `lb build noauto`.

Debian live-build names an `iso-hybrid` artifact with a `.hybrid.iso` suffix.
After successful assembly, the wrapper verifies that expected file and performs
a guarded rename to the public convention
`oblinux-debian-${VERSION}-${BUILD_ID}-amd64.iso`. It refuses to overwrite an
existing artifact with the same identity.

If a supported binary-only rebuild has retained `chroot/`, the wrapper also
refreshes both identity files in that generated filesystem before binary
assembly. This prevents a new filename from being paired with the prior
build's embedded `BUILD_ID`; a first or fully clean build receives the same
files through `config/includes.chroot` in the normal live-build chroot stage.

Brand Master is pinned to release `v1.0.4`, commit
`13e211da2ccd43156fcc7dc7e57c3be7bb5ee47d`, and a reviewed commit-archive
SHA-256 in `branding/brand-master.lock`. The preparation script never consumes
a moving branch. It verifies and builds `oblinux-branding` `1.0.4-1`, then
validates its metadata before making it available to live-build. See
`docs/BRAND_MASTER_INTEGRATION.md` for the immutable dependency and upgrade
process.

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
- `.build/oblinux-release` and the rendered `config/includes.chroot` copies of
  `os-release`

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

A builder with authorized read access to the private development repository can
clone it and update it directly from GitHub:

```bash
git clone <repository-url>
cd oblinux-debian-iso-dev
git pull --ff-only
```

The dedicated builder uses a repository-scoped, read-only GitHub deploy key.
Read access is sufficient for `git fetch` and `git pull`; the builder does not
need authority to push development changes. The original credential-free Git
bundle transfer was a bootstrap measure and is no longer the normal update
method.

## Configure and validate

From the repository root:

```bash
cat VERSION
lb config
lb config --validate
```

Confirm that `VERSION` is the intentionally selected release version before
building. `lb config` uses an unversioned placeholder image name because the
exact build identity does not exist yet; `auto/build` replaces that generated
setting when the build begins.

`lb config` translates `auto/config` into live-build's generated configuration
tree. `lb config --validate` checks whether the selected options form a valid
combination. Validation is valuable but cannot prove that all downloads,
package installation, boot behavior, or hardware support will succeed.

The initial validation exposed an invalid selection of two BIOS bootloaders.
OBLinux now selects `grub-efi` for UEFI and `grub-pc` for BIOS. This is an
example of why configuration validation precedes a full build.

## Run a build

For a clean, guarded build from an interactive shell, use the repository-owned
wrapper:

```bash
cd ~/oblinux-debian-iso-dev
scripts/build-iso
```

The wrapper requires a clean `main` worktree, verifies the development remote,
uses `git pull --ff-only`, requires `HEAD` to equal `origin/main`, checks the
Debian 13 `amd64` host and required commands, obtains sudo authorization, runs
the full purge and validation sequence, and verifies the resulting ISO, build
record, log, release identity, boot metadata, checksum, and final Git state. It
does not delete a failed build's diagnostic state, push commits, boot the ISO,
or claim runtime or installation acceptance.

It can be started from an administration workstation over SSH with a terminal
so `sudo` can prompt if necessary:

```bash
ssh -t <builder> \
  'cd ~/oblinux-debian-iso-dev && scripts/build-iso'
```

The `-t` option allocates a terminal so `sudo` can ask for the administrator's
password. Do not place a password in the command, documentation, environment,
or repository.

During the build, live-build will roughly perform these stages:

1. Read `VERSION`, generate one `BUILD_ID`, render the two `os-release` files,
   and configure the versioned live-build image name.
2. Validate the Brand Master integration and build its pinned local Debian
   package from the checksum-verified immutable source archive.
3. Download the pinned Papirus input and build the local OBLinux icon package.
4. Bootstrap a minimal Trixie filesystem.
5. Configure Debian package repositories inside the chroot.
6. Install the kernel, live components, GNOME, firmware, selected apps, and the
   local OBLinux branding and icon packages.
7. Apply configured hooks and included OBLinux files.
8. Verify the release/build identity, Brand Master payload/activation, and both
   Horizon themes, their caches, aliases, package status, and GNOME default.
9. Remove temporary package data as appropriate.
10. Compress the live filesystem into SquashFS.
11. Assemble GRUB boot files and the hybrid ISO.
12. Generate checksums and package/file metadata, then apply the guarded public
    filename.

The first build can take 20–60 minutes depending on network and compression
speed. The generated ISO is named
`oblinux-debian-${VERSION}-${BUILD_ID}-amd64.iso`.

## Inspect results

After a successful build:

```bash
ls -lh *.iso* build-logs/
sha256sum *.iso
cat .build/oblinux-release
```

The record and ISO filename must agree. Boot that ISO and check the embedded
identity:

```bash
cat /etc/os-release
```

`VERSION` and `VERSION_ID` must equal the repository `VERSION`; `BUILD_ID` must
equal the filename and `.build/oblinux-release`. Calamares unpacks the same
SquashFS into the target and does not remove these OBLinux-owned files. After a
clean installation, run the same command and require identical values. This is
the acceptance evidence that an installed system can be traced to its source
ISO; the copy-based mechanism alone is not a substitute for testing.

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
scripts/validate-branding-integration
lb config
lb config --validate
sudo lb build
```

`--purge` removes more cached state and causes additional downloads. Use it when
reproducibility matters or stale state is suspected, not reflexively after every
failure.

Use the following complete procedure whenever the pinned `oblinux-branding`
version, its packaged payload, or package-owned branding assets change, or when
hooks and downstream transformations that depend on package defaults must run
again:

```bash
sudo lb clean --purge
scripts/validate-branding-integration
lb config
lb config --validate
sudo lb build
```

This is the supported branding-package rebuild procedure confirmed during the
Brand Master v1.0.4 recovery. It regenerates the live filesystem and retained
chroot state, reinstalls the package, reruns applicable live hooks and
downstream transformations, and rebuilds the final binary/ISO stage.
`lb clean --binary` may be used for a change confined to binary assembly, but
it is insufficient when a branding package must be reinstalled or processed
inside the live filesystem.

After the build, inspect the final ISO's SquashFS rather than trusting build
success alone. Confirm the installed `oblinux-branding` version, expected
package-owned files, downstream-transformed configuration, and absence of
stale assets or obsolete downstream copies. Apparent branding regressions must
first be checked for retained build state; do not edit or duplicate Brand
Master artwork downstream to compensate for a stale chroot.

Payload inspection does not replace runtime visual acceptance. Boot the ISO
and validate affected visual surfaces such as GRUB, Plymouth, GNOME,
FastFetch, and Calamares according to the applicable checklist under
`docs/tests/`.

## Image acceptance criteria

- `VERSION` contains the intentional development or stable release identity.
- The ISO filename, build record, live `os-release`, and installed `os-release`
  agree on one `VERSION` and one `BUILD_ID`.
- `lb config` and `lb config --validate` complete without errors.
- `lb build` completes and produces a hybrid ISO.
- A SHA-256 checksum is generated.
- The ISO boots in a VirtualBox UEFI VM.
- GNOME reaches the desktop.
- The live session uses the unprivileged `live` account without manual login.
- NetworkManager establishes network connectivity.
- Firefox ESR and Ptyxis launch.
- `oblinux-icon-theme` is installed and Horizon Dark is the GNOME default.
- `oblinux-branding` `1.0.4-1` is installed and its GNOME, Calamares, GRUB,
  Plymouth, product-icon, and system-template payloads pass the integration
  checks in `docs/tests/BRAND_MASTER_RUNTIME_TEST.md`.
- Reboot and shutdown work.

## Not included yet

- The remaining daily-driver application set and explicit default policies
- Flatpak or third-party application repositories
- Firewall configuration
- Production signing or release automation
