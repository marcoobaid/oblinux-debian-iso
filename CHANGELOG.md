# Changelog

## Unreleased

## 26.3.0

- Enable location-aware Calamares timezone detection through KDE's Calamares
  GeoIP service while retaining an offline fallback.
- Add Arch-parity Calamares swap selection for automated installs, offering
  No swap and bounded Swap (no Hibernate) choices with No swap as the default.
- Align the live desktop shortcuts and GNOME dash with the Arch edition.
- Replace Evolution with Ptyxis in the persistent GNOME dock defaults, matching
  Arch while keeping the Calamares favorite exclusive to the live session.
- Mask Debian's generic Calamares desktop-icon autostart to prevent it from
  creating a duplicate installer shortcut in the live session.
- Suppress GNOME Tour for the ephemeral live user while retaining the normal
  first-login welcome flow for installed users.
- Match Arch's GNOME About input using the identical hicolor SVG and its
  explicit 192-pixel lookup size; Debian's compiled vendor-emblem path bypasses
  `LOGO`, so a direct-file variant supplies the same intrinsic size without
  speculative padding or artwork changes.
- Add Arch-parity Nano and Vim defaults and the Quadrapassel, Aisleriot, and
  GNOME Chess game set.
- Match Arch's Nano color rendering by using Ptyxis's native system-following
  palette instead of the Debian-only custom ANSI palette.
- Install the Arch Fastfetch configuration byte-for-byte at the same
  system-wide XDG path, matching its module list, formatting, and colors for
  live and installed users.
- Add GIMP and GNOME Disks for graphical USB ISO writing.
- Remove Flameshot from the default package set and application assertions;
  GNOME Shell native screenshots are the supported default. Annotation is not
  provided as an equivalent native feature; other tools remain user-installable.
- Document the 26.3.0 manual regression gate, guarded Stable build procedure,
  SourceForge publication model, and artifact provenance requirements.
- Explicitly include the Debian equivalents of the Arch application-grid set,
  including core GNOME apps, LibreOffice, GUFW, Avahi browsers, printing and
  hardware utilities, V4L2 tools, Software Token, and graphical Vim; retain
  GNOME Disks as the Debian-native substitute for unavailable Impression.
