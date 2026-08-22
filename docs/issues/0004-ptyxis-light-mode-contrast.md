# Issue 0004: Ptyxis initializes light mode with stale low-contrast text

- Status: Resolved; live VM and physical installation passed
- First observed: 2026-08-22
- Source under test: commit `aa690a0`
- Corrected by: commit `2e35277`
- Verified from: commit `4884aa4` (includes `2e35277`)
- Surface: Ptyxis initial light appearance and Fastfetch color treatment
- Severity: Usability and presentation

## Observation

Commit `aa690a0` correctly removed the fixed bright-red Fastfetch treatment and
made the output follow the terminal foreground. However, both the live ISO and
a clean installed system can initially open Ptyxis in GNOME's light appearance
with a very light gray foreground on a near-white background. Fastfetch and
ordinary terminal text are then unacceptably low-contrast.

Switching GNOME to dark appearance and then back to light causes Ptyxis to
refresh the foreground to readable black. Dark appearance is readable without
the reported workaround. This points to an initialization or appearance-refresh
defect rather than an inherently unusable final light palette; the root cause
is in Ptyxis 48.5's initial appearance sequencing.

The remaining problem is that Fastfetch becomes almost entirely monochrome:
black in light mode and white in dark mode. This loses too much of the intended
OBLinux terminal identity. Fastfetch should retain restrained, readable color
accents in both appearances without returning to a fixed color that has poor
contrast on one background.

## Scope

The initialization defect is reproduced in both the live session and a clean
Calamares-installed system. The dark-to-light appearance toggle is only a
workaround, not an acceptable default experience.

The same installed-system test confirms that Calamares now assigns Zsh as the
created user's default shell. That functional correction is recorded separately
in [Terminal Experience Runtime Test 01](../tests/2026-08-22-terminal-experience-01.md)
and is not blocked by this presentation issue.

The request for restrained Fastfetch color is a related presentation
requirement, but it is distinct from the initialization defect: after the
workaround, Fastfetch becomes almost entirely black in light mode and white in
dark mode. A correction must solve the initial contrast failure first, then add
readable OBLinux accents without recoloring all ordinary terminal output.

## Root cause

Debian 13 packages Ptyxis 48.5. The observed behavior is consistent with its
startup sequence: during terminal construction, Ptyxis applies
the selected palette using libadwaita's appearance state and then subscribes to
later appearance changes. The final system-following appearance can settle
after that first palette application without producing the notification needed
to repaint the initial terminal. Changing appearance later emits the signal and
corrects the foreground, which matches the observed workaround.

## Prepared correction

The OBLinux Zsh startup configuration now refreshes Ptyxis's appearance before
Fastfetch runs, but only when all of these are true:

- the shell is an interactive top-level terminal;
- Ptyxis's interface style is still `system`; and
- the required GSettings schemas are available.

The refresh briefly selects the explicit appearance matching GNOME and then
resets Ptyxis to its normal `system` default. Explicit user-selected `light` or
`dark` Ptyxis preferences are not changed. This is a scoped Debian 13 POC
compatibility workaround and should be removed when the packaged Ptyxis no
longer needs it.

Fastfetch now uses the palette's adaptive cyan for its large ASCII logo and
adaptive blue for its title and field labels. Values remain on the terminal
foreground so the output gains restrained OBLinux identity without recoloring
every line.

## Evidence

Four screenshots were supplied outside Git:

- Initial light-mode observation, SHA-256
  `ee1b35fda8b54cb460def00181eeb84fee61ace1d0400e9ad02b56e1e0d0ab9f`
- Dark mode, SHA-256
  `78cbda5e47f9e06de584dbf4172dc0b8678f6820b099625b0fa6c773937d128d`
- Confirmed readable black light-mode output, SHA-256
  `f422671da0cb711b803577cadca91e1494d8458f3763d437abda49479b5d2281`
- Installed-system initial light-mode failure, SHA-256
  `6af0ad3c570e8b423880aa7694d85601e9f6373e894bb2b58b0072a9933743bd`

The installed-system screenshot confirms the same initial low-contrast state
seen in the live session. The readable black light-mode screenshot shows the
state after appearance switching, and the dark screenshot provides the readable
dark comparison.

## Resolution verification

The tester pulled commit `4884aa4`, built a new ISO, and booted it in an Oracle
VirtualBox live session. On the first light-mode Ptyxis launch, terminal text
was readable without an appearance toggle; Fastfetch used the intended cyan
logo and blue title/label accents; and Zsh was present and active. The supplied
post-correction screenshot is retained outside Git with SHA-256
`864ee366118bd400a62f56447883f3d3d1efa672e352eec82cde9a3d219df659`.

The tester subsequently reported that physical installation and installed-
system testing passed. The ISO SHA-256, physical hardware model, firmware mode,
and individual checklist command output were not supplied, so this record does
not infer those details. See
[Terminal Experience Runtime Test 02](../tests/2026-08-22-terminal-experience-02.md).

## Acceptance criteria

- On first opening Ptyxis directly in GNOME light appearance, ordinary terminal
  text and Fastfetch are clearly readable without toggling appearances or
  changing the palette manually.
- Opening in dark appearance and switching repeatedly between light and dark
  preserve correct, readable foreground/background combinations.
- Fastfetch uses restrained OBLinux color accents in both appearances rather
  than rendering entirely black or white.
- Prompt and semantic command colors remain distinguishable in both
  appearances and ordinary terminal output remains readable.
- Fastfetch remains free of the fixed bright-red styling and generic ANSI
  palette strip addressed by `aa690a0`.
- The live session and a clean Calamares-installed user are both tested.
- User-selected Ptyxis palette and appearance settings remain overridable.
- The temporary refresh is removed if a future Debian stable Ptyxis update
  makes it unnecessary.
