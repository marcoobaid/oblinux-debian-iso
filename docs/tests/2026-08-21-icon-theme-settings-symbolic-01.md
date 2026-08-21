# OBLinux Horizon GNOME Settings symbolic-icon validation

Date: 2026-08-21

## Scope

Validate the `oblinux-icon-theme` `0.1.0-2` correction that excludes symbolic
application icons from the regular Horizon application container.

## Result

Passed on an installed OBLinux GNOME test system.

- GNOME Settings sidebar glyphs rendered correctly in the light appearance.
- GNOME Settings sidebar glyphs rendered correctly in the dark appearance.
- Previously affected entries no longer appeared as solid black or white
  squares.
- Regular application icons retained their approved Horizon presentation.

The generator regression test also verifies that an icon below a symbolic
application directory remains unframed while a regular application icon still
receives the Horizon container.
