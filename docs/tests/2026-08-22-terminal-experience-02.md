# Terminal Experience Runtime Test 02

## Result

- Status: Passed based on tester-reported live and installed-system results
- Test date: 2026-08-22 America/Chicago
- Source under test: commit `4884aa4` (includes terminal fix `2e35277`)
- Environments: Oracle VirtualBox live session and physical installation
- ISO SHA-256: Not recorded in the supplied test report
- Physical hardware and firmware mode: Not recorded in the supplied test report

## Live-session result

Passed. After pulling the source and building a new ISO, the tester booted the
live image in Oracle VirtualBox. Ptyxis opened directly in GNOME light mode with
readable foreground text; the previous faded-gray startup state did not recur.
Fastfetch displayed a cyan OBLinux logo, blue title and field-label accents, and
readable foreground-colored values. Zsh was reported installed and active in
the live session.

The supplied screenshot is stored outside Git with SHA-256
`864ee366118bd400a62f56447883f3d3d1efa672e352eec82cde9a3d219df659`.

## Installed-system result

Passed. The tester subsequently reported that physical installation and
installed-system testing completed successfully. This confirms the correction
on the installed-system path at the level of the supplied report.

No physical model, firmware mode, ISO checksum, screenshots, or individual
checklist command outputs were supplied. Accordingly, this record does not make
more specific hardware-support or per-command claims.

## Disposition

Issue 0004 is resolved. The earlier Calamares installed-user Zsh correction and
the Ptyxis/Fastfetch light-mode correction now both have reported runtime
success. Retain the temporary Ptyxis 48.5 startup refresh until a Debian stable
update is explicitly tested and shown to make it unnecessary.
