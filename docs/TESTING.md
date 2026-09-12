# Testing Strategy

## Purpose

Testing should answer two questions during the POC:

1. Is the current image safe and reliable enough for the next test stage?
2. How much continuing effort does OBLinux require?

## Current acceptance

The [pre-promotion owner regression record](tests/2026-09-11-pre-promotion-owner-regression.md)
confirms the current functional baseline passed owner testing on VMs and
physical hardware. Historical records below describe their own artifacts;
checklists remain procedures and are not automatically marked passed.

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

- Root `VERSION` uses the policy in [VERSIONING.md](VERSIONING.md)
- Generated ISO name contains that exact version and one `BUILD_ID`
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

## Release and build identity regression

Run this for every normal development, stable, and maintenance image. Before
building, inspect the authoritative release identity:

```bash
cat VERSION
```

Require `YY.QUARTER.MAINTENANCE-dev` for a development build and the same form
without `-dev` for a stable or maintenance release. After building, compare
the generated filename with `.build/oblinux-release`. It must have the form:

```text
oblinux-debian-${VERSION}-${BUILD_ID}-amd64.iso
```

Boot that exact ISO and run:

```bash
cat /etc/os-release
```

Require all of the following:

- `VERSION` exactly equals the root `VERSION` file.
- `VERSION_ID` exactly equals the root `VERSION` file.
- `BUILD_ID` uses `YYYYMMDD-HHMM` and exactly matches the ISO filename.
- Development versions include `-dev`; stable and maintenance versions do not.

Install that ISO with Calamares onto a new disposable VM disk, detach the ISO,
boot the installed system, and run `cat /etc/os-release` again. Its `VERSION`,
`VERSION_ID`, and `BUILD_ID` must exactly match the live system and the ISO
used for installation. A matching release version with a different build ID is
a failure because it cannot identify the tested image exactly.

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

## Live desktop and application regression

On a freshly built ISO with networking enabled:

- Open Calamares and confirm its initial timezone follows the test network's
  location (test at least one non-Eastern location); then disconnect networking
  and confirm the page remains usable with its documented fallback.
- In the erase-disk workflow, confirm the swap selector offers **No swap** and
  **Swap (no Hibernate)** and defaults to **No swap**. Complete separate installs
  with each choice on disposable VM disks. Confirm the no-swap installation has
  no active swap; confirm the swap installation has an active swap partition
  and a matching `/etc/fstab` entry after reboot.
- Confirm the desktop shows Home, Trash, and a trusted `Install OBLinux`
  shortcut. Confirm the shortcut and dock installer icon use the OBLinux logo
  and launch Calamares. Confirm there is no second shortcut named
  `calamares-install-debian.desktop`.
- Confirm GNOME Tour does not open or appear in the application grid in the
  live session. After installation, confirm a newly created user retains
  GNOME's normal one-time welcome flow.
- Confirm the dash order is Files, Firefox, Terminal, Install OBLinux, followed
  by GNOME's Show Applications control.
- Open Settings > System > About in light and dark appearances and compare the
  OBLinux badge with the Arch edition. Require identical symbol geometry,
  visual scale, and surrounding layout space.
- Launch Nano and Vim against representative shell, Python, and Markdown files;
  inspect syntax colors, line numbers, indentation, search, and readability in
  both terminal appearances.
- Launch Quadrapassel, Aisleriot, GNOME Chess, GIMP, GNOME Disks, and Flameshot.
  Start a local chess game, capture and annotate a screenshot, and use GNOME
  Disks to write the ISO to a disposable USB device.
- Compare the application grid with the Arch reference screenshots. Open each
  top-level application and the Utilities/System folders; confirm Contacts,
  Weather, Clocks, the Avahi browsers, Document Scanner, btop++, Calculator,
  Characters, Calendar, Document Viewer, Extensions, Eye of GNOME, GUFW,
  Firmware, Hardware Locality, lftp, the complete LibreOffice suite, printing
  configuration, both Qt V4L2 launchers, Software Token, Text Editor, Videos,
  and Vim launch successfully. GNOME Disks intentionally replaces Impression
  on Debian and must provide its Restore Disk Image workflow.

After a clean Calamares installation, repeat the application/editor checks and
confirm the live desktop shortcut and enabled Desktop Icons NG state were not
copied into the installed user's profile.

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

These Build 005–009 sections are historical acceptance records for the legacy
repository-owned identity. Current Brand Master v1.0.4 acceptance is defined in
`docs/tests/BRAND_MASTER_RUNTIME_TEST.md`; use that checklist for new images.

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
Open GNOME Settings System/About and confirm that the centered R5 symbol uses
the same scalable product icon, visual scale, and surrounding layout spacing
as the Arch edition.

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
dominating the page. Repeat the installed Plymouth, GRUB, identity,
regeneration, cleanup, and basic regression checks from Build 007.

## GNOME About badge acceptance checks

Open GNOME Settings About in both light and dark appearances. Confirm the
primary transparent OBLinux symbol matches the Arch edition's geometry and
scale. It must show no accidental white corners, clipping, stretching, excess
layout spacing, or low-contrast details.

Confirm that Calamares, Plymouth, the Dash launcher, GRUB, wallpapers, and the
primary transparent symbol remain unchanged. Verify the vendor-logo selection
and repeat the installed-system smoke checks.

## Build 007 identity-polish acceptance checks

Build 007 must retain all Build 006 functional checks and close its three
presentation findings.

In live and installed GNOME Settings About, confirm that the approved OBLinux
symbol replaces the Debian swirl. The operating-system name must remain
`OBLinux Proof of Concept (Debian 13)`. Verify the active OBLinux vendor-logo
alternative and the retained Debian candidate:

```bash
update-alternatives --display vendor-logos
test "$(readlink -f /usr/share/images/vendor-logos)" = \
  /usr/share/oblinux/vendor-logos
test -d /usr/share/desktop-base/debian-logos
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

## GDM vendor-mark acceptance checks

After a clean installation, log out or reboot to GDM. Confirm that the login
screen displays the OBLinux vendor mark and does not display the Debian 13
mark. Confirm separately that the account avatar remains the neutral Horizon
default or the user's selected photo.

Verify the alternatives registration and active target:

```bash
update-alternatives --display vendor-logos
test "$(readlink -f \
  /usr/share/images/vendor-logos)" = \
  /usr/share/oblinux/vendor-logos \
  && echo "PASS: OBLinux GDM vendor mark active"
```

Switch the user avatar, lock and unlock the active session, log out, log back
in, and reboot. The avatar choice and normal session lock screen must remain
functional. Run `sudo apt update`, reinstall or upgrade `desktop-base` when a
safe test update is available, and confirm that the OBLinux alternative stays
selected.

## GDM background acceptance checks

After a clean installation, reboot or log out to GDM. Confirm that the greeter
uses a subtle vertical dark-navy-to-slate gradient without a background image.
The existing OBLinux vendor mark must remain visible, and no Debian artwork may
appear.

Verify the dedicated GDM profile, source values, and compiled database:

```bash
sed -n '1,80p' /etc/dconf/profile/gdm
sed -n '1,80p' /etc/dconf/db/gdm.d/01-oblinux-background
test -s /etc/dconf/db/gdm \
  && echo "PASS: GDM background database compiled"
```

Change the user's desktop wallpaper, then lock and unlock the session. Confirm
that the selected wallpaper and normal GNOME lock screen still work. Log out
again and confirm that GDM retains its own gradient and existing OBLinux vendor
mark. This test guards the intended separation between greeter and user-session
settings.

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
