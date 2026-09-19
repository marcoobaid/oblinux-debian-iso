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

The project is in Roadmap Phase 3, daily-driver candidate. OBLinux Debian
26.3.0 is released, with owner-confirmed VM and physical laptop
installation/regression passes. The immutable tag `v26.3.0` points to certified
source commit `8f28de66fc43c4bf1d9f76b0880810eefd6c519b`. The certified
release code is frozen. The Stable ISO is published on SourceForge under
`OBLinux-Debian-ISO/26.3.0/`; see [the release record and procedure](docs/RELEASING.md)
for its exact artifact identity and unchanged support scope.

Codex is the primary development agent. This root `AGENTS.md` is the
authoritative governance document for all agents; `CLAUDE.md` is a supplemental
entry point.

## Stable repository protection

This repository, `oblinux-debian-iso`, is the stable/production OBLinux Debian
baseline. It preserves the last accepted implementation and is not the normal
workspace for feature development, experimentation, or branding integration.

- Debian development, integration, ISO builds for proposed changes, and
  validation occur first in `oblinux-debian-iso-dev`.
- Shared visual identity and common branding assets are owned upstream by
  `oblinux-brand-master`. Do not redesign or independently implement shared
  branding in this repository, and do not consume unreleased Brand Master
  changes or its `main` branch directly here.
- Stable receives functional changes only through a separate promotion after
  the proposed Dev ISO has built successfully, passed the required validation
  and runtime review, and received explicit owner authorization.
- Do not merge, rebase, reset, cherry-pick, copy, or otherwise synchronize dev
  changes into stable without that explicit promotion authorization. A
  successful development build alone is not approval.
- Preserve history, traceability, release boundaries, rollback capability, and
  the existing known-good branding (including Obsidian Horizon) during any
  future authorized promotion.
- Never fabricate build or runtime validation results. A successful ISO build
  is required before release, and every claimed test result must identify work
  that was actually executed against the stated artifact and environment.

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

## Release version and build identity

`docs/VERSIONING.md` is the authoritative release/version policy shared with
OBLinux Arch. The root `VERSION` file is the authoritative current repository
version and must remain `26.3.0` for this release. Do not invent,
infer, independently increment, or modify it during unrelated work. Development
versions use `-dev`; stable versions do not. Advancing the separate Dev
repository requires later explicit owner authorization.

`BUILD_ID` is generated automatically once per build and propagated unchanged
to the ISO name and live/installed `os-release`. It is not part of the release
version or Git tag. Stable tags use forms such as `v26.3.0`. See
`docs/VERSIONING.md` for the complete lifecycle and policy.

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

GNOME Shell native screenshots are the supported default; do not promise
third-party annotation functionality. Users may install other capture tools.

GNOME is the only POC edition. Defaults such as wallpapers, icon theme, Ptyxis,
and terminal configuration must remain user-overridable. Keep the live-only
Calamares lock/suspend policy separate from installed-user settings, and keep
GDM greeter configuration separate from desktop wallpaper, the in-session lock
screen, account avatars, and vendor logos.

OBLinux Debian intentionally selects the established Obsidian Horizon image as
its desktop and lock-screen default, overriding Brand Master's generic paired
wallpaper default without modifying the shared package. Preserve both live and
installed behavior and the user's ability to choose another wallpaper.

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
0005–0014 before altering these mechanisms. Preserve Debian package originals
through the established alternatives/diversion patterns, preserve user choices,
and keep guarded Debian-file modifications fail-closed when upstream content is
unexpected.

## Build and validation commands

Build on an up-to-date Debian 13 `amd64` host with root access, a native Linux
filesystem, and at least 40 GB free (60 GB recommended). See
`docs/BUILDING.md` for dependencies, host setup, wrapper behavior, generated
files, logs, and artifact inspection. From the repository root, the Stable
build entry point is exactly:

```bash
scripts/build-stable-iso
```

The tracked `scripts/build-iso` wrapper is intentionally guarded for the Dev
repository and must not be run or repointed in this Stable checkout. Build the
Stable ISO with `scripts/build-stable-iso` as defined in
`docs/RELEASING.md`. It derives the source from clean Stable `main`, verifies
the authorized Stable remote and exact local/remote commit agreement,
`VERSION=26.3.0`, the Debian 13 `amd64` host, and build dependencies before
purging generated state and invoking the existing branding validation,
live-build configuration, validation, and `sudo lb build` sequence. Runtime,
installation, and hardware testing remain separate acceptance stages.

Output follows `oblinux-debian-${VERSION}-${BUILD_ID}-amd64.iso`. Inspect it with:

```bash
ls -lh *.iso* build-logs/
sha256sum *.iso
```

For a fundamental configuration change or suspected stale state:

```bash
sudo lb clean --purge
scripts/validate-branding-integration
lb config
lb config --validate
sudo lb build
```

### Branding Package Rebuild Safety

Changes to the `oblinux-branding` package or its packaged payload must not
be validated using only a retained live-build chroot with:

```bash
lb clean --binary
```

A binary-only clean regenerates the binary/ISO stage but may preserve an
existing chroot and therefore may not rerun live hooks or downstream
transformations that operate on branding-package defaults. This can produce
a successfully built ISO containing stale branding or configuration.

When the pinned `oblinux-branding` version or packaged branding payload
changes, perform a clean/rebuild that forces the affected live filesystem,
chroot package installation, and applicable hooks to be regenerated.

After rebuilding, inspect the resulting ISO/live filesystem to confirm that
the expected branding package version and transformed runtime assets are
actually present.

A successful ISO build alone is not evidence that a branding-package update
was incorporated correctly. Runtime or payload validation is required.

Do not work around stale build-state problems by modifying Brand Master
artwork or introducing downstream branding copies. First rule out retained
live-build state and verify the generated payload.

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

- Never force-push or rewrite published history without explicit owner approval
  for a specific named recovery situation. Push Stable only for an explicitly
  authorized promotion, release correction, or documentation update, and only
  to the verified `oblinux-debian-iso` origin. Keep any Dev remote read-only;
  Stable promotion requires separate explicit owner approval.
- Use the configured human Git identity. Do not add AI co-author, Generated-By,
  Assisted-By, or other AI attribution to commits or contributor records.
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

### Release and tagging policy

Release tags are always the final step of the release process:

For 26.3.0: `Change → Static validation → Commit → Push main → Final VM and
physical regression → Release-ready → Separate tag authorization → Tag`.

Successful final VM and physical-hardware regression is the release validation
gate for 26.3.0. Automated CI is not required for this release and remains a
future enhancement. Historical records quoting the earlier CI gate are evidence
of their own date, not current release instructions.

- Never create, move, delete, or push a release tag during normal development.
- Before declaring a release ready, ensure all intended changes are committed,
  the working tree is clean, release and package metadata are consistent,
  repository validation passes, the changes are pushed to `main`, and final VM
  and physical regression evidence identifies the exact Stable artifact and
  source commit. Any later changes require an explicit evidence review;
  functional/build changes require rebuilding and retesting.
- After those checks pass, stop and report that the repository is
  **release-ready**. Do not create or push the release tag unless the owner
  explicitly authorizes it after that declaration.
- Never tag an intermediate release-preparation commit while validation,
  metadata, packaging, or corrective commits remain.
- If a published tag is found to be wrong, do not move or replace it
  automatically; stop and ask the owner how to proceed.

## Documentation routing

- Vision, principles, governance: `docs/PROJECT_CHARTER.md`
- POC boundaries and completion gates: `docs/POC_SCOPE.md`
- Base, packaging, repositories, deferred production design:
  `docs/ARCHITECTURE.md`
- Exact host setup, build commands, wrappers, artifacts: `docs/BUILDING.md`
- Release gates, Stable build, provenance, publishing: `docs/RELEASING.md`
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
