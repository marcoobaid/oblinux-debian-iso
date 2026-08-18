# POC Build 001 VirtualBox Live-Boot Test

## Result

- Status: Passed
- Test date: 2026-08-17 America/Chicago
- Image: `oblinux-debian-gnome-amd64.hybrid.iso`
- Image build record: [POC Build 001](../builds/2026-08-17-poc-001.md)
- Hypervisor: Oracle VirtualBox on a Linux host
- Test type: Manual live-session boot

This test validates booting and using the live image. It is not a disk
installation test because POC Build 001 intentionally contains no installer.

## Reported observations

The manual test passed the following checks:

- The ISO was accepted and started by VirtualBox.
- The boot menu appeared successfully.
- The live session logged in automatically.
- GNOME reached a usable desktop.
- The applications included in the image were present and launched
  successfully during the test.

No blocking failure was reported during the recorded boot process.

## Evidence

- Recording: `OBL-DEBIAN-TEST-screen0.webm`
- Recording size: 2,269,051 bytes
- Recording SHA-256:
  `f888efa35b7bcf130ffa358c1b9ea2a288dd391f21fd58c22f7ca62fe24cdd5a`

The recording is retained outside Git because binary test evidence does not
belong in source history. The filename and checksum provide a stable reference
to the evidence reviewed for this test.

## Scope limitations

This first manual test does not yet establish:

- Installation to a virtual disk
- Persistence across live-session reboots
- BIOS-mode boot
- Secure Boot compatibility
- Physical hardware compatibility
- Printing or Bluetooth behavior
- Suspend and resume
- Long-running stability
- Recovery behavior

## Next step

The next image milestone adds and validates a graphical installer. Before that
work begins, any observed cosmetic or functional issues from the first live
session should be recorded as issues so installer integration does not obscure
live-desktop defects.

