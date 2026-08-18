# Building OBLinux

## Current milestone

The current configuration builds an experimental Debian 13 `amd64` GNOME live
ISO. It is intended only to prove that the image can be built reproducibly and
booted in a VM. It does not contain an installer and is not a supported release.

## Build host

Use an up-to-date Debian 13 `amd64` system with root access and at least 40 GB of
free working space. Sixty GB or more is recommended for repeated builds and
retained artifacts. Build on a native Linux filesystem rather than a VirtualBox
shared folder.

Install the initial build dependencies:

```bash
sudo apt update
sudo apt install \
  ca-certificates debootstrap dosfstools git grub-efi-amd64-bin grub-pc-bin \
  isolinux live-build mtools rsync squashfs-tools syslinux-utils xorriso
```

## Build procedure

Clone the repository and enter it:

```bash
git clone git@github.com:marcoobaid/oblinux-debian-iso.git
cd oblinux-debian-iso
```

Generate the live-build configuration:

```bash
lb config
```

Build the image as root:

```bash
sudo lb build
```

The generated ISO is named `oblinux-debian-gnome-amd64.hybrid.iso` unless the
installed live-build version applies a different architecture suffix. Generated
images, working directories, caches, and logs are ignored by Git.

## Clean rebuilds

For the most reliable result, clean generated state before changing fundamental
live-build options:

```bash
sudo lb clean --purge
lb config
sudo lb build
```

Do not delete or manually edit files under `config/` that are tracked by Git.
The `auto/config` script is the authoritative source for generated live-build
settings.

## First-image acceptance criteria

- `lb config` completes without errors.
- `lb build` completes and produces a hybrid ISO.
- A SHA-256 checksum is generated.
- The ISO boots in a VirtualBox UEFI VM.
- GNOME reaches the desktop.
- The live session uses the unprivileged `live` account without manual login.
- NetworkManager can establish network connectivity.
- Firefox ESR and Ptyxis launch.
- Reboot and shutdown work.

## Not included yet

- Calamares or another installer
- OBLinux visual branding
- LibreOffice and the complete daily-driver application set
- Zsh and Starship defaults
- Flatpak or third-party application repositories
- Firewall configuration
- Production signing or release automation

