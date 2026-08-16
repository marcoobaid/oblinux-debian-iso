# Testing Strategy

## Purpose

Testing should answer two questions during the POC:

1. Is the current image safe and reliable enough for the next test stage?
2. How much continuing effort does OBLinux require?

## Test progression

Tests move from least destructive to most destructive:

1. Static inspection of configuration and generated manifests
2. ISO integrity and boot tests
3. Live-session tests in a VM
4. Installer tests using disposable virtual disks
5. Installed-system update and reboot tests
6. Physical live-session hardware tests
7. Spare-disk or otherwise recoverable physical installation
8. Daily-driver trial

## Initial smoke tests

- ISO boots in UEFI mode
- GNOME reaches the desktop without manual login
- Live user is not privileged by default
- Networking and DNS work
- Sound is available in the VM when supported
- Installer starts and presents the intended OBLinux identity
- Erase-disk installation completes on a disposable virtual disk
- Installed system boots without the ISO attached
- Live user and live autologin are absent from the installed system
- The created user can authenticate and use administrative elevation
- `apt update` succeeds
- Debian security updates install successfully
- The system survives update and reboot

## Physical hardware checklist

- UEFI boot
- Internal and external display behavior
- Graphics acceleration
- Wired and wireless networking
- Bluetooth
- Audio input and output
- Keyboard, touchpad, and pointing devices
- Internal and removable storage
- Suspend and resume
- Shutdown and reboot
- Battery status and power profiles, where applicable
- Webcam
- Printing and scanning, if part of the daily workload

## Installer safety

Destructive installer scenarios must use disposable VM disks until explicitly
approved for a physical test. Dual boot, manual partitioning, encryption, and
existing EFI partition reuse each require separate test cases. A successful
erase-disk test does not validate any of those scenarios.

## Daily-driver evidence

During the trial, record:

- Image and installed version
- Update history
- Defects and workarounds
- Regressions after updates
- Time spent maintaining OBLinux-specific behavior
- Missing applications or hardware support
- Recovery events
- Configuration that exists only as an undocumented manual change

An undocumented manual fix is a POC finding, not part of a reproducible build.

