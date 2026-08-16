# Hardware Targets

## Purpose

The POC has two physical laptops and a separate Linux VirtualBox host. The
ThinkPad is the selected daily-driver target. More detailed device inventory is
still required before claiming hardware support.

## Current inventory

| System | Intended role | Status |
| --- | --- | --- |
| Lenovo ThinkPad T14s Gen 6, AMD, 32 GB RAM, 1 TB SSD | Primary physical test system and dedicated OBLinux daily driver | Selected; detailed device inventory pending |
| Microsoft Surface Laptop 3, Intel, 16 GB RAM | Secondary physical compatibility target | Selected; detailed device inventory pending |
| Linux laptop running Oracle VirtualBox | First live-boot and installation-test platform | Host distribution, resources, and VirtualBox version pending |
| Xerox B310 | Representative network or USB printer | Deferred until printing validation |
| Bluetooth headphones | Representative Bluetooth test class | Specific device not required for initial image |

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

The AMD ThinkPad is the primary target for the initial `amd64` image. It will be
a dedicated OBLinux system with no dual boot. Its 32 GB of RAM and 1 TB SSD are
more than sufficient for the daily-driver workload; disk sizing and encryption
policy still need to be finalized before physical installation.

Stock Debian must first be validated on this conventional laptop hardware.
Tests cover Wi-Fi, Bluetooth, graphics, external displays, audio, webcam,
suspend, resume, battery reporting, function keys, power profiles, docking, and
any required fingerprint reader.

## Microsoft Surface Laptop 3

The secondary target is an Intel Surface Laptop 3 with 16 GB of RAM.

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

The host operating system is Linux. Record its distribution and version, CPU
architecture, VirtualBox version, available RAM and storage, and whether nested
virtualization is involved.
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

The ThinkPad is the selected daily-driver target, but it must not be installed
until a stock Debian live environment has been tested and the backup, recovery,
encryption, and disk-layout plans are complete.
