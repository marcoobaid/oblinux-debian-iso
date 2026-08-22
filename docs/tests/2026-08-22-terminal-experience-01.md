# Terminal Experience Runtime Test 01

## Result

- Status: Partially passed; installed-user shell fix confirmed, light-mode
  presentation remains open
- Test date: 2026-08-22 America/Chicago
- Source under test: commit `aa690a0`
- Environment: Oracle VirtualBox live session and clean Calamares installation
- ISO SHA-256: Not recorded in the supplied test report

## Calamares installed-user shell

Passed. After a clean Calamares installation, the created user uses Zsh as the
default shell. This confirms the `aa690a0` correction from the obsolete flat
Calamares `userShell` setting to the nested `user.shell` setting.

The installed-system Fastfetch output also reports Zsh 5.9. The explicit
installed-user shell result was reported by the tester; no claim is made here
for checklist commands whose output was not supplied.

## Presentation finding

The overall terminal-experience acceptance does not pass yet. In both the live
and installed systems, Ptyxis can initially open in GNOME light appearance with
low-contrast light-gray text. Switching to dark and back to light refreshes the
foreground to readable black. Fastfetch also needs restrained OBLinux color
accents rather than an almost entirely black or white presentation.

See [Issue 0004](../issues/0004-ptyxis-light-mode-contrast.md) for evidence and
acceptance criteria.

## Disposition

The Calamares/Zsh functional fix in `aa690a0` is runtime-confirmed. Keep Issue
0004 open and do not mark the complete terminal experience accepted until a
new correction passes both live-session and clean installed-system light/dark
testing.
