# OBLinux operating guide for Codex

Read this file before making changes. OBLinux is a Debian-based project; never
apply Arch Linux conventions or assume behavior from another distribution.
Consult the authoritative document for the subsystem being changed, and treat
the repository's current tracked state as authoritative where milestone prose
has become stale.

## Project identity and current phase

OBLinux is an experimental, proof-of-concept desktop distribution intended to
measure whether a polished, dependable, maintainable Debian workstation can be
sustained for daily use. It is a thin Debian derivative, not an independent
package ecosystem. The current edition is Debian 13 stable (`trixie`), `amd64`,
GNOME, built as a hybrid live/install ISO with Debian `live-build`, `live-boot`,
and `live-config`; installed systems receive normal Debian updates through APT.

The project is in Roadmap Phase 3, daily-driver candidate. Repeatable live ISO
builds and Calamares VM installations have passed, foundational branding and
the Horizon icon theme are integrated, and a ThinkPad candidate passed initial
physical installation and daily-driver testing. This is not a supported public
release or a broad hardware-support claim. Later GDM fixes and the terminal
experience have source changes and focused acceptance procedures but no newer
documented full-ISO/clean-install result; do not describe them as runtime-passed
until those tests actually succeed.

Core principles from the project charter:

- Stay close to Debian stable; prefer upstream solutions and small, visible,
  reversible OBLinux configuration or packages over downstream forks.
- Do not mix Debian testing or unstable into the POC. Backports and custom
  packages require explicit justification and testing.
- User data and installer safety outrank visual polish. Security and support
  claims require implemented policy and verification evidence.
- Keep builds reproducible from version-controlled inputs and document all
  manual intervention. Scope expands only after the GNOME edition is
  maintainable.

## Architecture and repository map

- `auto/`: authoritative `live-build` configure/build/clean wrappers.
  `auto/config` owns persistent image settings; the wrappers use `noauto` to
  avoid recursion. Do not make persistent edits to generated live-build state.
- `config/package-lists/`: packages installed in the live filesystem. GNOME is
  based on Debian's `task-gnome-desktop`; transitive contents must be verified
  from generated manifests rather than inferred from the explicit lists.
- `config/includes.chroot/`: files overlaid into the image filesystem. Some are
  persistent installed-system defaults; files owned by
  `calamares-settings-debian` are deliberately removed with that package.
- `config/hooks/live/`: ordered late chroot customization and assertions.
  Preserve hook ordering and explicit package dependencies.
- `config/bootloaders/`: live-build GRUB presentation overrides; live-build
  retains kernel discovery, menu generation, and boot mechanics.
- `branding/`: the immutable Brand Master package pin plus the separately
  maintained Horizon application icon theme. Shared R5 visual assets come from
  the pinned `oblinux-branding` package; do not duplicate or regenerate them in
  this repository.
- `packaging/` and `scripts/`: OBLinux-owned package recipes and build helpers.
  The Horizon theme is an independently versioned, locally generated Debian
  package derived reproducibly from pinned Debian Papirus input.
- `docs/decisions/`, `docs/issues/`, `docs/tests/`, and `docs/builds/`: the
  durable record of decisions, known problems, test procedures/results, and
  artifact history. Dated records describe their specific source revision and
  must not be generalized to later changes without retesting.

The initial architecture deliberately uses live-build includes and hooks while
package boundaries are learned. Persistent configuration should move into
policy-compliant OBLinux Debian packages where practical before public release.
No OBLinux APT repository is justified merely by the POC; a future repository
requires signed metadata, scoped trust, source-package handling, promotion and
key-management policy. Third-party applications require license review and
explicit vendor-repository opt-in with scoped `Signed-By` trust.

## GNOME, installer, and identity boundaries

GNOME is the only POC edition. Defaults such as wallpapers, icon theme, Ptyxis,
and terminal configuration must remain user-overridable. Keep the live-only
Calamares lock/suspend policy separate from installed-user settings, and keep
GDM greeter configuration separate from desktop wallpaper, the in-session lock
screen, account avatars, and vendor logos.

Calamares uses Debian's packaged `calamares-settings-debian` workflow. Preserve
Debian's module order and installer behavior unless a change is explicitly
designed and tested. OBLinux overrides identity-facing package-owned files and
the final APT-source helper; package-ownership checks protect the invariant that
installer-only files disappear when the settings package is removed. Recheck
that invariant whenever Debian's package changes.

The installed APT policy is Trixie stable, updates, and security with `main`,
`contrib`, `non-free`, and `non-free-firmware`; backports and `deb-src` are not
enabled by default. Package availability or a visible Calamares option does not
make a feature supported. The documented installer baseline is unencrypted
erase-disk installation to a blank UEFI/GPT/ext4 VM disk. Manual partitioning,
dual boot, encryption, existing-ESP reuse, alternative storage layouts,
interrupted-install recovery, and Secure Boot require separate approval and
tests. Use disposable VM disks for destructive scenarios; never attach host or
valuable storage.

Branding and persistent identity span GNOME About, wallpapers, GRUB, Plymouth,
Calamares, GDM, account defaults, and the Horizon themes. Consult Decisions
0005–0012 before altering these mechanisms. Preserve Debian package originals
through the established alternatives/diversion patterns, preserve user choices,
and keep guarded Debian-file modifications fail-closed when upstream content is
unexpected.

## Build and validation commands

Build on an up-to-date Debian 13 `amd64` host with root access, a native Linux
filesystem, and at least 40 GB free (60 GB recommended). See
`docs/BUILDING.md` for dependencies, host setup, wrapper behavior, generated
files, logs, and artifact inspection. From the repository root, the primary
sequence is exactly:

```bash
scripts/validate-branding-integration
lb config
lb config --validate
sudo lb build
```

Expected output is `oblinux-debian-gnome-amd64.hybrid.iso`. Inspect it with:

```bash
ls -lh *.iso* build-logs/
sha256sum *.iso
```

For a fundamental configuration change or suspected stale state:

```bash
sudo lb clean --purge
lb config
sudo lb build
```

Do not clean immediately after a failure; preserve terminal output, the
timestamped build log, and generated state for diagnosis. Never store sudo
passwords or other secrets in scripts, environment, logs, or documentation.
Do not commit build state, logs, manifests, generated local packages or icon
trees, ISO/disk images, checksums, or secrets; follow `.gitignore` and
`docs/BUILDING.md`.

## Testing rules

Use `docs/TESTING.md` for the least-to-most-destructive progression: static
inspection, ISO integrity/boot, VM live session, disposable-disk installation,
installed update/reboot, physical live testing, recoverable physical install,
then daily-driver trial. Use the focused checklist under `docs/tests/` for each
changed subsystem and review related prior results and `docs/issues/` before
troubleshooting a known problem.

Validation must match the risk and affected surfaces. A configuration check is
not an ISO boot test; an ISO boot is not an installation test; a VM pass is not
hardware support. Preserve regression coverage for live boot, GNOME, network,
Calamares cleanup, installed APT sources and updates, GRUB/Plymouth, user
defaults and choices, reboot, and shutdown where relevant. Identity changes
must survive their documented regeneration/update paths.

Never claim a command or test passed unless it was actually executed
successfully on the stated artifact and environment. Record failures at the
exact step. Significant build/test evidence belongs in dated records using the
existing conventions; binary screenshots and logs remain outside Git, with
filenames and checksums recorded when useful.

## Change and Git discipline

- Inspect `git status` first and preserve unrelated user work. Keep the change
  narrowly scoped to the request; avoid unrelated refactoring.
- Consult the relevant authoritative document and accepted decision before
  editing a subsystem. Do not overturn established architecture unless the
  task explicitly calls for a new decision.
- Update documentation when behavior changes architecture, build procedures,
  installer behavior, support scope, or testing requirements. Record
  significant architectural/design decisions in `docs/decisions/`; do not
  leave durable knowledge only in chat.
- At the completion of each task, decide whether the work introduced or changed
  a durable instruction, architectural constraint, development convention,
  build or validation requirement, or other guidance future Codex sessions
  need. If so, update this file as part of the task. Do not update it for
  routine implementation changes, bug fixes, test or build results, or details
  that belong in existing authoritative documentation.
- Use scoped commits. Current history uses concise Conventional Commit-style
  subjects such as `feat:`, `fix:`, `docs:`, `test:`, `build:`, and `design:`.
  Git history, issues, test/build records, and decision records are the project
  record. Do not commit or push unless explicitly requested.
- Keep project-facing documentation professional and free of personal names or
  unique device identifiers; use project roles and redact serial numbers.

## Documentation routing

- Vision, principles, governance: `docs/PROJECT_CHARTER.md`
- POC boundaries and completion gates: `docs/POC_SCOPE.md`
- Base, packaging, repositories, deferred production design:
  `docs/ARCHITECTURE.md`
- Exact host setup, build commands, wrappers, artifacts: `docs/BUILDING.md`
- Calamares architecture, supported baseline, destructive controls:
  `docs/INSTALLER.md`
- Validation progression and detailed acceptance checks: `docs/TESTING.md`
- Current phase and remaining work: `docs/ROADMAP.md`
- Physical targets and support limits: `docs/HARDWARE_TARGETS.md`
- Workstation/application requirements: `docs/DAILY_DRIVER_REQUIREMENTS.md`
- Established choices: `docs/decisions/`
- Known problems and verification state: `docs/issues/`
- Reusable checklists and dated results: `docs/tests/`
- Build provenance and artifact history: `docs/builds/`

When documents conflict, do not silently select one. Verify whether one is a
historical milestone statement, inspect only the minimal current implementation
needed to resolve ambiguity, and report the conflict for correction.
