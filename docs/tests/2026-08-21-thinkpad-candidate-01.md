# ThinkPad Candidate 01 Hardware Test

## Result

- Status: Passed with one presentation finding
- Test date: 2026-08-21 America/Chicago
- Target: Lenovo ThinkPad T14s Gen 6, AMD, 32 GB RAM, 1 TB SSD
- Image commit: `93aca338f40efa7821c845e0c5965168cc6b95f3`
- ISO SHA-256: `1fcc398d7cc66aaef3a5433b2ee3d3984b120a64f104a1df6fe7b74f8b066aea`
- Installation mode: Dedicated OBLinux system; no dual boot

## Live test

The candidate booted successfully from USB on the physical ThinkPad. The
planned live checks completed without a reported functional failure, including
the desktop, built-in input, display, networking, Bluetooth, audio, power,
storage visibility, branding, and installer launch surfaces.

## Installation and daily-driver test

Calamares completed installation successfully. The installed system booted and
remained functional through the rest-of-day daily-driver evaluation. No
hardware or application defect was reported during this period.

## Finding

The installed GDM login screen retained Debian 13 vendor artwork. The account
avatar itself remained a separate, functional surface. The finding is tracked
in [Issue 0002](../issues/0002-gdm-debian-login-background.md).

## Disposition

ThinkPad functional hardware acceptance passes for this proof-of-concept
candidate. Public-release readiness is not implied. The GDM presentation fix
requires a new image and clean-install verification before the finding can be
closed.
