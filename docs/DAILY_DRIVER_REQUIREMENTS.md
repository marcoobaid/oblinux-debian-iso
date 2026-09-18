# Daily-Driver Requirements

## Purpose

This document translates the initial workstation needs into testable OBLinux
POC requirements. Package choices remain provisional until tested in both the
live and installed environments.

## Workstation profile

The initial system is a GNOME developer workstation used for terminal-based and
Visual Studio Code development, office documents, presentations, spreadsheets,
web applications, Bluetooth devices, and local or network printing.

## Requirement mapping

| Need | Proposed POC implementation | Source | Acceptance criteria |
| --- | --- | --- | --- |
| Elegant, configurable terminal | Ptyxis | Debian stable | Profiles, fonts, colors, tabs, copy/paste, URLs, and shell integration work. |
| Developer shell and prompt | Zsh with Starship; Git completions and conservative aliases | Debian stable | Git and development context render quickly without prompt errors. |
| Printing | CUPS, appropriate drivers, Avahi, and `system-config-printer` | Debian stable | A supported USB or network printer can be configured and used from office and browser applications. |
| Professional documents | LibreOffice Writer | Debian stable | Create, edit, export, print, and exchange representative DOCX files with acceptable fidelity. |
| Professional spreadsheets | LibreOffice Calc | Debian stable | Create formulas and charts, export, print, and exchange representative XLSX files with acceptable fidelity. |
| Professional slides | LibreOffice Impress | Debian stable | Create and present a deck, use an external display, export, and exchange representative PPTX files with acceptable fidelity. |
| Bluetooth | BlueZ and GNOME Settings | Debian stable | Pair, reconnect, remove, and use required headsets and input devices. |
| Open browser | Firefox ESR | Debian stable | Browsing, downloads, media, printing, password storage, and hardware acceleration pass basic tests. |
| Google browser | Google Chrome stable | Google signed APT repository, opt-in | Installation and updates work through APT; repository trust is scoped and removable. |
| Easy application installation | GNOME Software; Flatpak evaluated separately | Debian stable; optional Flathub | Applications can be discovered, installed, updated, and removed graphically, with their source visible. |
| Host firewall | UFW with GUFW as the initial candidate | Debian stable | A documented default-deny-incoming policy does not break required workflows. |
| Development editor | Microsoft Visual Studio Code | Microsoft signed APT repository, opt-in | APT updates, Git, terminal, extensions, file watching, and desktop integration work. |
| Image editing | GIMP | Debian stable | GIMP launches and can create, open, edit, and export representative images. |
| USB image writing | GNOME Disks (`gnome-disk-utility`) | Debian stable | Restore Disk Image writes a test ISO to a disposable USB drive and reports completion. |
| Screenshot capture | GNOME Shell native screenshot interface | Debian stable | The standard shortcut opens the overlay; area, window, and full-screen capture, saving, and clipboard use work in live and installed GNOME Wayland sessions. |
| Lightweight games | Quadrapassel, Aisleriot, GNOME Chess with GNU Chess | Debian stable | Each game launches; GNOME Chess can start a local single-player game. |

## Terminal direction

Ptyxis fits GNOME and provides substantially more preferences than GNOME
Console. Zsh provides the interactive shell. Starship is the preferred initial
prompt because Debian packages it, it exposes useful developer context, and its
configuration can remain small and reviewable.

Oh My Zsh remains a user-installed option, but the image should not depend on a
large plugin framework or execute an unpinned network installer during a build.
Completions, history behavior, syntax highlighting, and autosuggestions should
be selected individually after package availability and startup performance are
tested.

The default login shell must not change until live-user and installed-user
creation have been tested. Bash remains available for scripts and recovery.

## Office compatibility

LibreOffice is the default office suite candidate, but "professional" must be
validated with representative work rather than assumed. The POC test set should
include:

- A styled DOCX document with headers, tables, images, tracked changes, and PDF
  export
- An XLSX workbook with formulas, charts, formatting, filters, and printing
- A PPTX presentation with themes, images, speaker notes, and an external
  display
- Required fonts and PDF output

Microsoft Office file compatibility is not exact. Web-based Microsoft 365 or
Google Workspace can be fallbacks when fidelity is critical. OBLinux must not
silently redistribute proprietary Microsoft fonts.

## Application sources

The graphical software experience should identify whether an application comes
from Debian, Flatpak, or an external vendor. The POC begins with Debian packages
and evaluates Flatpak after sandbox permissions, updates, disk use, and GNOME
Software integration are understood.

Chrome and VS Code are required daily-driver applications but are not Debian
packages. The POC should use a documented post-install opt-in that configures
each vendor's signed repository. Before public release, redistribution and
branding terms must be reviewed before offering bundled packages or one-click
installation.

## Curated desktop utilities and games

The image explicitly includes GNOME Disks as its USB ISO writer because its
Restore Disk Image workflow is maintained in Debian, fits GNOME, and avoids an
external repository or a second storage stack. GNOME Shell's native screenshot
interface is the supported default in both live and installed systems. It does
not provide an equivalent annotation workflow. Advanced users may install
other screenshot tools themselves; these are not part of default acceptance.

GIMP and the Arch-equivalent lightweight games are also explicit image
packages: `quadrapassel` for falling blocks, `aisleriot` for solitaire, and
`gnome-chess` with the `gnuchess` engine for local play. Nano and Vim receive
the same user-overridable, plugin-free editor defaults as the Arch edition.

The application image also explicitly installs the Debian equivalents of the
applications visible in the Arch edition's application grid. This includes the
core GNOME applications, LibreOffice suite, GUFW, Avahi service browsers,
printing configuration, btop++, lftp, Hardware Locality, V4L2 test utilities,
Software Token, and the GTK Vim launcher. Declaring these packages directly
prevents changes in `task-gnome-desktop` dependencies from silently removing
them from later images.

Arch's Impression application has no package in Debian 13. GNOME Disks is the
intentional Debian-native equivalent: its **Restore Disk Image** action writes
ISO images to removable media while avoiding an external repository. GNOME
Tour remains installed for normal first-login behavior on installed systems,
but is hidden and suppressed for the ephemeral live account.

## Firewall policy

The workstation should deny unsolicited incoming connections and allow
outbound traffic. Testing must cover printer discovery, local development
servers, virtual machines, containers, VPNs, and future file sharing. UFW and
GUFW are the initial candidates because their policy is understandable and can
be managed graphically. Only one high-level firewall manager should own the
host rules.

## Open decisions

- Whether Flatpak and Flathub are default, setup-time, or documented choices
- Terminal font and redistribution license
- Zsh plugins included by default
- Default browser and whether both browsers are in the live image
- Printer and Bluetooth devices used for acceptance tests
- Whether Chrome and VS Code installation is automated after explicit consent
- Required development runtimes and container tooling
- VPN, remote desktop, cloud storage, password manager, and backup requirements

## Initial peripheral test scope

Printing is not a blocker for the first bootable ISO. A Xerox B310 is available
as the initial representative printer when printing validation begins. Other
printers can expand coverage later without becoming part of the POC baseline.

No Bluetooth peripheral is required for daily use at present. Bluetooth support
will initially be validated by pairing, reconnecting, selecting an audio
profile, playing audio, and using the microphone on a representative pair of
headphones.
