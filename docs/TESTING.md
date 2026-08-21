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

## Build 004 wallpaper acceptance checks

Build 004 must retain all Build 003 checks and verify the wallpaper integration
in both the live and installed systems.

Confirm the files and effective GNOME defaults:

```bash
test -r /usr/share/backgrounds/oblinux/oblinux-horizon-branded-3840x2160.jpg
test -r /usr/share/backgrounds/oblinux/oblinux-horizon-clean-3840x2160.jpg

gsettings get org.gnome.desktop.background picture-uri
gsettings get org.gnome.desktop.background picture-uri-dark
gsettings get org.gnome.desktop.background picture-options
gsettings get org.gnome.desktop.screensaver picture-uri
```

The branded wallpaper must be the light, dark, and lock-screen default, with
`zoom` as the picture option. Open GNOME Settings and confirm that both OBLinux
variants appear in the background chooser.

In the live session, switch to the clean wallpaper and back to the branded
wallpaper. After installation, repeat the change as the created user and log out
and back in. The user's selection must persist. No dconf lock file may prevent
changing any background key.

Inspect the installed system and confirm that both wallpaper files, the GNOME
catalog, the OBLinux background schema override, license, and attribution remain
present. This integration is an installed-system default, unlike the live-only
lock and suspend policy that Calamares removes.

## Build 005 boot and installer branding acceptance checks

Build 005 must retain all Build 004 checks and verify the new identity-facing
integration without changing installer behavior.

Boot the ISO once in UEFI mode and once in legacy-BIOS mode. In both modes,
confirm that the GRUB menu uses the Obsidian Horizon background, displays the
`OBLinux Live` title, uses readable white and cyan menu text, starts the default
live entry successfully, and retains the utilities and media-integrity entries.

In the live session, confirm that the launcher is visibly named
`Install OBLinux` and uses the OBLinux icon. Start Calamares and verify:

- The window identifies the product as OBLinux, not Debian.
- The sidebar uses the approved Obsidian Navy, Deep Ocean Blue, and Soft White.
- The OBLinux logo and Obsidian Horizon welcome image render cleanly.
- The slideshow text says `Installing OBLinux`.
- Every previously tested page remains available and functional.

Cancel before disk changes, relaunch, and then complete a clean UEFI
installation on a disposable VM disk. Confirm the installed GRUB entry is
named OBLinux and repeat the Build 004 installed-system checks. Finally, verify
that Calamares, its live launcher, and its branding directory are absent from
the installed system after cleanup.

## Build 006 installed identity acceptance checks

Build 006 must retain all Build 005 functional checks and close its four
documented branding findings.

In Calamares, confirm that the Slate Blue sidebar is visibly lighter than Build
005 and that the bottom-left `About` control is readable. All navigation text
must retain clear contrast in normal and selected states.

In both the live and installed GNOME systems, open Settings, select System, and
inspect About. Confirm the OBLinux symbol and the name
`OBLinux Proof of Concept (Debian 13)` appear. Also run:

```bash
cat /etc/os-release
```

Confirm `ID=oblinux`, `ID_LIKE=debian`, and `LOGO=oblinux-logo` are present.

After installation, confirm the GRUB background uses Obsidian Horizon and the
primary entry is exactly `OBLinux`. The advanced submenu must be
`Advanced options for OBLinux`; neither entry may contain the automatic
`GNU/Linux` suffix.

Continue booting and confirm Plymouth uses the OBLinux symbol, dark gradient,
and cyan progress indicator with no Debian name, swirl, or artwork. Reboot and
shut down once more to verify repeatability.

Finally, repeat the Build 005 Calamares/live-package cleanup checks, run
`sudo update-grub` and `sudo update-initramfs -u`, and reboot. OBLinux GRUB and
Plymouth branding must remain after regeneration.

## Build 008 presentation acceptance checks

Build 008 must retain all Build 007 functional checks and close its three
remaining presentation findings.

Boot the ISO normally in UEFI mode. After GRUB, confirm the graphical OBLinux
Plymouth screen appears instead of verbose kernel and systemd output. Boot once
more after removing `quiet splash` temporarily from the GRUB entry and confirm
that diagnostic console output remains available.

In the live GNOME Dash, confirm the `Install OBLinux` launcher uses the clean
transparent symbol without white corners, a surrounding tile, distortion, or
clipping. Calamares must retain its already accepted logo presentation.

Open GNOME Settings About in both live and installed sessions. Confirm the
OBLinux symbol and operating-system name remain correct and that the symbol is
balanced near the scale previously occupied by Debian's emblem rather than
dominating the page. Repeat the installed Plymouth, GRUB, diversion,
regeneration, cleanup, and basic regression checks from Build 007.

## GNOME About badge acceptance checks

Open GNOME Settings About in both light and dark appearances. Confirm the
surface-specific badge has a clean rounded Obsidian Navy background, Soft White
OB letters, and Clear Cyan bridge. It must remain balanced at the accepted
Build 008 size and show no accidental white corners, clipping, stretching, or
low-contrast letterforms.

Confirm that Calamares, Plymouth, the Dash launcher, GRUB, wallpapers, and the
primary transparent symbol remain unchanged. Verify the vendor-logo diversion
and repeat the installed-system smoke checks.

## Build 007 identity-polish acceptance checks

Build 007 must retain all Build 006 functional checks and close its three
presentation findings.

In live and installed GNOME Settings About, confirm that the approved OBLinux
symbol replaces the Debian swirl. The operating-system name must remain
`OBLinux Proof of Concept (Debian 13)`. Verify the preserved Debian vendor file
and active diversion:

```bash
dpkg-divert --list \
  /usr/share/icons/vendor/scalable/emblems/emblem-vendor.svg
test -r \
  /usr/share/icons/vendor/scalable/emblems/emblem-vendor.svg.distrib
```

Open Calamares at normal and maximized sizes. Confirm its symbol has no white
corners, tile, border, stretching, or clipping and is balanced within the
sidebar.

Boot the installed system and confirm Plymouth displays the proportional
OBLinux symbol without a surrounding square or light corner artifacts. Run
`sudo update-initramfs -u`, reboot, and confirm the corrected presentation
persists. Complete the Build 006 cleanup, APT, GRUB, and basic regression checks.

## Default account avatar acceptance checks

Complete a clean Calamares installation and reach GDM with the newly created
account. Confirm that the account and lock screens show the neutral Horizon
user silhouette rather than Debian artwork or the OBLinux product mark.

After login, verify the source diversion and active skeleton default:

```bash
dpkg-divert --list /etc/skel/.face
test -r /etc/skel/.face.distrib \
  && echo "PASS: Debian skeleton avatar preserved"
cmp /etc/skel/.face \
  /usr/share/oblinux/branding/oblinux-default-avatar.svg \
  && echo "PASS: OBLinux skeleton avatar active"
test "$(readlink /etc/skel/.face.icon)" = .face \
  && echo "PASS: skeleton avatar link valid"
```

Set a custom account photo, lock the session, and confirm that the selected
photo replaces the default and remains after logout and reboot. The build must
not overwrite an existing user's `~/.face` or AccountsService image.

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
