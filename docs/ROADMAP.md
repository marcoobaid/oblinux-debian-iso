# OBLinux Roadmap

This roadmap is ordered by learning value. Dates should be assigned only after
the first local build establishes realistic effort.

## Phase 0: Foundation

- [x] Record the initial project charter
- [x] Define the POC boundary and completion criteria
- [x] Record the initial base and desktop decisions
- [x] Initialize the primary GitHub repository
- [x] Select the original code and documentation license
- [ ] Select branding and redistributed-asset licenses
- [x] Define the primary physical test machine
- [x] Record the initial daily-driver applications and hardware inventory
- [x] Identify target CPU architectures and select the primary test machine
- [ ] Capture detailed device and firmware inventory for the target machines
- [x] Define the minimal first-image GNOME package set
- [ ] Decide the POC firmware, Flatpak, encryption, dual-boot, and Secure Boot
  policies

Exit condition: the target hardware, workload, and initial package policy are
known well enough to build without guessing.

## Phase 1: Bootable live image

- [x] Prepare a clean Debian build environment
- [x] Create and validate the minimal `live-build` configuration
- [ ] Build a stock Debian 13 GNOME hybrid ISO
- [ ] Configure the unprivileged live user and autologin
- [ ] Add basic OBLinux identity and wallpaper
- [ ] Generate checksums, package manifests, and build logs
- [ ] Boot-test the ISO under QEMU/KVM

Exit condition: a documented command produces a GNOME live ISO that boots and
provides a functional live session.

## Phase 2: Installable POC

- [ ] Write the initial installer requirements
- [ ] Integrate Debian's Calamares packages and configuration
- [ ] Test UEFI erase-disk installation on disposable VM disks
- [ ] Verify user creation, locale, keyboard, timezone, and bootloader behavior
- [ ] Verify that live-only packages and credentials do not leak into the
  installed system
- [ ] Collect useful installer logs on failure
- [ ] Repeat clean installation from the same ISO

Exit condition: the ISO completes two repeatable VM installations and the
installed systems update normally.

## Phase 3: Daily-driver candidate

- [ ] Validate graphics, networking, audio, Bluetooth, storage, suspend, resume,
  printing, and external displays on the target machine
- [ ] Finalize the required application set
- [ ] Test backup and restoration
- [ ] Document recovery and reinstallation
- [ ] Complete a non-destructive physical test or spare-disk installation
- [ ] Record all known limitations
- [ ] Begin the daily-use trial only after its entry criteria pass

Exit condition: the system is used for normal work for an agreed trial period,
with maintenance effort and failures recorded.

## Phase 4: Maintainability review

- [ ] Review build and update effort from the trial
- [ ] Convert persistent configuration into appropriate OBLinux packages
- [ ] Determine whether an OBLinux APT repository is now justified
- [ ] Automate smoke tests and artifact generation
- [ ] Decide whether to proceed toward a private alpha or narrow the project

Exit condition: a written proceed, revise, or stop decision is supported by POC
evidence.

## Future public-release work

- Project governance and contribution policy
- Public security contact and vulnerability handling
- Production repository signing and key rotation
- Secure Boot support, if claimed
- License and source-distribution compliance
- Public artifact hosting
- Broader hardware and installer test matrices
- Accessibility and localization review
- Support lifecycle and major-version upgrades
- Public branding system and asset licensing
- Release notes, user guide, troubleshooting, and support channels
- Additional desktop flavors after the GNOME edition is maintainable
