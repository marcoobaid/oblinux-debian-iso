# Decision 0002: GNOME-first scope

- Status: Accepted for the POC
- Date: 2026-08-15

## Context

OBLinux may eventually offer GNOME, i3, Qtile, and other flavors. Supporting
multiple editions immediately would multiply package selection, configuration,
installer, documentation, and test work before the basic release process is
understood.

## Decision

GNOME is the only POC edition. The eventual build layout should permit common
and flavor-specific layers, but no other flavor will be built or supported until
the GNOME edition is maintainable.

## Consequences

- Early work can focus on the build, live session, installer, updates, and
  physical hardware.
- Branding and workflow decisions can be tested in one coherent desktop.
- Other flavors remain future work rather than implicit POC commitments.
- Lessons from GNOME should inform the common/flavor boundary before additional
  editions are introduced.

