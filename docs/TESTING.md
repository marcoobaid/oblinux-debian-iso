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

## Build 003 acceptance checks

Build 003 must retain all Build 002 smoke tests and add the checks below.

In the live GNOME session, verify the effective settings:

```bash
gsettings get org.gnome.desktop.lockdown disable-lock-screen
gsettings get org.gnome.desktop.screensaver lock-enabled
gsettings get org.gnome.desktop.session idle-delay
gsettings get org.gnome.settings-daemon.plugins.power sleep-inactive-ac-type
gsettings get org.gnome.settings-daemon.plugins.power sleep-inactive-battery-type
```

The expected values are `true`, `false`, `uint32 0`, `'nothing'`, and
`'nothing'`. Start Calamares, leave the VM untouched for at least 20 minutes,
and confirm that the session neither locks nor suspends.

Check time synchronization in both the live and installed systems:

```bash
timedatectl show \
  --property=NTP \
  --property=NTPSynchronized \
  --property=SystemClockSynchronized
systemctl is-enabled systemd-timesyncd.service
systemctl is-active systemd-timesyncd.service
```

With working networking, NTP must be enabled and active and the clock must
eventually report synchronization. A newly booted VM may need a short interval
before the synchronized state changes to `yes`.

After a clean installation, inspect `/etc/apt/sources.list` and files under
`/etc/apt/sources.list.d/`. Only Debian Trixie stable, updates, and security
should be enabled by OBLinux. Each must contain `main`, `contrib`, `non-free`,
and `non-free-firmware`; backports, source-package entries, and live-media
sources must be absent. Finish with `sudo apt update` and confirm success.

Finally, confirm `calamares-settings-debian` is absent from the installed
system and that the installed user's normal lock and suspend controls remain
available. The live-only policy must not weaken the installed system.

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
