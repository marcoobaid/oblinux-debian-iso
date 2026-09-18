# OBLinux Project Charter

## Vision

OBLinux aims to become a free, elegant, functional, secure, reliable, and
maintainable Debian-based desktop operating system. It should offer an
approachable alternative for users accustomed to mainstream commercial desktop
operating systems without concealing the strengths of Linux or Debian.

## Current objective

The current objective is a proof of concept that can become the maintainer's
daily-driver system. The POC measures the real engineering and
maintenance effort; the project is now preparing its first public Stable
release under the explicitly limited scope below.

The first successful outcome is not a broadly supported product. It is a
repeatable build that boots into a useful GNOME live session, installs safely in
the tested scenarios, receives Debian updates normally, and works reliably on
the maintainer's chosen virtual and physical hardware.

## Intended evolution

The current authorized direction is preparation for public Stable 26.3.0,
with final VM and physical regression and the limited scope described in
[RELEASING.md](RELEASING.md). The release is not yet complete. Later work may
include other desktop or window-manager flavors, a signed OBLinux package
repository, and graphical tools for common customization and administration
tasks.

## Principles

1. Debian stable is the source of truth for the base operating system.
2. OBLinux-specific changes remain small, visible, reversible, and documented.
3. Builds are automated and repeatable from version-controlled inputs.
4. User data and installer safety take priority over visual polish.
5. Security claims require an implemented policy and verification evidence.
6. Upstream solutions are preferred over permanent downstream patches.
7. Scope expands only after the existing edition is maintainable.
8. Documentation is treated as part of the product.

## Initial target user

During the POC, the target user is an experienced Linux user running a modern
64-bit PC who wants a stable GNOME workstation for everyday use. This permits
technical recovery and manual diagnosis during early development while still
requiring a comfortable graphical daily experience.

A broader public-user persona must be defined before public beta testing.

## Success measures

The POC is successful when:

- A clean build environment produces the documented ISO without undocumented
  manual modifications.
- The ISO boots in the target VM and physical machine.
- The live environment logs in automatically as an unprivileged live user.
- The system can be installed through a graphical installer in the approved
  test scenarios.
- The installed system boots reliably and supports normal daily workloads.
- Debian security and stable updates install through APT without breaking
  OBLinux configuration.
- Recovery or reinstallation is understood, documented, and tested.
- Maintaining the system for a trial period is judged sustainable.

## Governance during the POC

Git history, issues, milestones, and architecture decision records are the
project record. Decisions should describe their context, outcome, and
consequences. Personal names should not appear in user-facing or project-policy
documentation; project roles such as maintainer, contributor, and release
manager should be used instead.
