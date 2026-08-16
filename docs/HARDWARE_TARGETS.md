# Hardware Targets

## Purpose

The POC has two physical laptop families and a separate VirtualBox host. Exact
model identification is required before selecting the first daily-driver target
or claiming hardware support.

## Current inventory

| System | Intended role | Status |
| --- | --- | --- |
| Lenovo ThinkPad T14s Gen 6 | Preferred first daily-driver candidate, subject to CPU architecture | Exact variant required |
| Microsoft Surface Laptop 3 or 4 | Secondary physical compatibility target | Exact generation and Intel/AMD variant required |
| Laptop running Oracle VirtualBox | Repeatable live-boot and installation tests | Host details and VirtualBox version required |

## Required inventory

For each physical target, record:

- Product name and machine type
- CPU model and architecture
- GPU or GPUs
- RAM and storage controller
- Wi-Fi and Bluetooth adapters
- Audio devices
- Webcam and biometric devices
- Touchscreen and pen, if present
- Dock and external-display requirements
- Firmware/UEFI version and Secure Boot state
- Existing operating systems and intended disk layout

On Linux, this can be collected with `lscpu`, `lspci -nnk`, `lsusb`, `lsblk`,
`fwupdmgr get-devices`, and `/sys/class/dmi/id/product_name`. Equivalent data can
be collected from Windows. Serial numbers and other unique identifiers must be
removed before reports are committed.

## ThinkPad T14s Gen 6

CPU architecture is a gating item. A 64-bit x86 model can use the initial
`amd64` image. An ARM model requires a separate `arm64` effort outside the first
POC scope.

If it is `amd64`, the ThinkPad is the preferred first target because stock
Debian should first be validated on conventional laptop hardware. Tests must
cover Wi-Fi, Bluetooth, graphics, external displays, audio, webcam, suspend,
resume, battery reporting, function keys, power profiles, docking, and any
required fingerprint reader.

## Microsoft Surface Laptop

Surface Laptop 3 and 4 systems have materially different Intel and AMD variants
and must not be treated as one target.

Testing begins with Debian's stock kernel and `non-free-firmware`. A patched
kernel must not be added to the general OBLinux image merely because the target
is a Surface. If required functionality is absent, the `linux-surface` project
can be evaluated as a device-specific experiment, including its repository,
signing, Secure Boot, update, and support consequences.

Surface-specific checks include the built-in keyboard and touchpad in the live
environment, touch and pen if required, battery reporting, power profiles,
suspend, webcam, microphone, Wi-Fi, Bluetooth, and HiDPI scaling. A spare USB
keyboard, mouse, and hub should be available during early installation tests.
Firmware should be current before testing.

## VirtualBox test system

Record the host operating system, CPU architecture, VirtualBox version,
available RAM and storage, and whether nested virtualization is involved.
VirtualBox validates installation behavior but not physical compatibility.

The baseline VM matrix should include:

- UEFI VM with a blank virtual disk
- Legacy BIOS only if the POC elects to support it
- Live session with and without network access
- Installed system with the ISO removed
- A low-memory test after the normal baseline works
- A snapshot before every destructive installer test

QEMU/KVM remains the preferred eventual automation target on the Debian build
machine. VirtualBox provides an independent manual check using existing
hardware.

## Selection gate

No laptop becomes the daily-driver target until its exact model and CPU
architecture are recorded, a stock Debian live environment has been tested, and
the backup and recovery plan is complete.

