# ThinkPad Live-Test Candidate 01

## Purpose

This image is the first OBLinux candidate designated for non-destructive live
hardware testing on the Lenovo ThinkPad T14s Gen 6 AMD. It is not a public
release and is not yet approved for installation on the ThinkPad.

## Provenance

| Property | Value |
| --- | --- |
| Build date | 2026-08-21 15:13:26 America/Chicago |
| Source commit | `93aca338f40efa7821c845e0c5965168cc6b95f3` |
| Source state | Clean and synchronized with `origin/main` before build |
| Architecture | `amd64` |
| Build result | Successful |

## Artifact

| Property | Value |
| --- | --- |
| Filename | `oblinux-debian-gnome-amd64.hybrid.iso` |
| Exact size | 2,164,258,816 bytes |
| Approximate size | 2.02 GiB / 2.16 GB |
| SHA-256 | `1fcc398d7cc66aaef3a5433b2ee3d3984b120a64f104a1df6fe7b74f8b066aea` |

Verify a copied artifact before use:

```bash
sha256sum oblinux-debian-gnome-amd64.hybrid.iso
```

The reported checksum must exactly match the value above.

## Acceptance gate

Before installation, boot this image from USB without modifying the internal
disk and complete the ThinkPad live-hardware checklist. At minimum, validate:

- UEFI boot and OBLinux boot presentation
- AMD graphics, native resolution, brightness controls, and external display
- Internal keyboard, TrackPoint, touchpad, and function keys
- Wi-Fi connectivity and Bluetooth discovery, pairing, audio, and reconnection
- Speakers, headphone output, microphones, and webcam
- Battery reporting, charging state, and available power profiles
- Suspend and resume on battery and AC power
- Cold boot, restart, shutdown, and system clock
- Internal NVMe visibility without mounting or modifying its filesystems
- GNOME, Horizon Layer icons, default applications, and installer launch

Installation remains gated on successful live testing, a current backup,
recovery media, and explicit disk-layout and encryption decisions.
