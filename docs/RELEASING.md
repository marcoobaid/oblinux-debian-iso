# OBLinux Debian 26.3.0 release procedure

## Current state and authority

Stable `main` is the OBLinux Debian 26.3.0 release candidate. It preserves both
repository histories and contains the accepted Dev source from commit
`d9289b2bbcaf1fb44a9b926fee0a7e40bf724bed`. Stable `VERSION` is `26.3.0`.
The `v26.3.0` tag has not been created and SourceForge publication has not
occurred. Dev remains `26.3.0-dev`; advancing it to `26.4.0-dev` requires later
explicit owner authorization.

The accepted Dev artifact was
`oblinux-debian-26.3.0-dev-20260918-1057-amd64.iso`, BUILD_ID
`20260918-1057`, SHA-256
`00d8e4c849304645e2062fe721b48f97facb4f4a3327cd4371cd820487b78827`.
The owner confirmed its VM installation/regression, physical laptop
installation/regression, and overall functional testing passed with no known
release-blocking findings. This evidence authorizes source promotion; it does
not replace the exact-commit Stable build or test a Stable artifact.

The owner-approved 26.3.0 validation gate is successful final VM and
physical-hardware regression, consistent with the completed Arch release.
Automated CI is not required for this release; automation remains future work.
This supersedes the CI prerequisite quoted in the September 11 historical test
record without changing that record or implying that CI ran.

GNOME Shell's native screenshot interface is the supported default. The
Flameshot removal is an intentional product decision shared with Arch, not a
new claim that a Debian runtime failure was reproduced. Native screenshots do
not promise equivalent annotation functionality. Other capture tools remain
available for advanced users to install themselves.

## Scope and approval boundaries

26.3.0 is intended for public distribution, with Debian 13, amd64, GNOME,
Debian's Calamares workflow, and normal Debian APT updates. Public availability
does not imply broad hardware compatibility or a new OBLinux package archive.
The installation baseline remains unencrypted erase-disk UEFI/GPT/ext4, tested
on disposable VM disks and the designated recoverable physical target.
Encryption, dual boot, manual partitioning, existing-ESP reuse, alternative
storage, interrupted-install recovery, and Secure Boot require separate
approval and evidence before support is claimed.

Promotion, release tagging, SourceForge publication, and advancing Dev are
separate authorized operations. Promotion is complete. Never force-push,
squash away the promoted history, replace published tags, or relabel a Dev ISO
as Stable. Dev remains the normal development workspace.

## Release sequence

1. **Complete:** prepare and validate Dev without changing `26.3.0-dev`.
2. **Complete:** build and accept the exact Dev candidate recorded above.
3. **Complete:** preserve both histories by merging the accepted Dev commit
   into Stable and deliberately reconcile Stable governance.
4. **Complete:** set Stable `VERSION=26.3.0`, finalize the `26.3.0` changelog
   section, retain a clean `Unreleased` section, validate, commit, and push
   Stable `main`.
5. Build the exact Stable `main` commit using the guarded procedure
   below. Complete final VM and physical regression on this Stable artifact,
   including live and installed identity checks. It receives its own BUILD_ID.
6. Record results, provenance, known limitations, and the license/source-
   distribution review before declaring release-ready. Commit and push any
   evidence documentation. If only documentation changed after the build,
   record both the build-source SHA and final release SHA and verify the diff
   contains no build/runtime inputs. Any functional or build-input correction
   requires a new build and affected regression. Require a clean final Stable
   tree synchronized with `origin/main`; do not claim unexecuted checks passed.
7. Report **release-ready**, then wait for separate authorization to create and
   push immutable tag `v26.3.0` on the final Stable commit. Nothing required for
   release readiness may remain unfinished at tagging time.
8. With publication authorization, publish and verify the artifact as below.
9. After release completion and separate approval, advance Dev to
    `26.4.0-dev`, reconcile its changelog/status/versioning documentation, and
    carry back any Stable functional corrections with explicit provenance.
    Keep Stable at `26.3.0`; do not move `v26.3.0`.

## Guarded Stable build after promotion

Preserve `scripts/build-iso` unchanged as the Dev-only workflow. Stable uses
the repository's separate guarded entry point while retaining `auto/build` and
the existing live-build implementation:

```bash
cd ~/oblinux-debian-iso
./scripts/build-stable-iso
```

Use a separate normal clone of `oblinux-debian-iso` on the Debian 13 amd64
builder, with repository-scoped read access to Stable. After promotion, prepare
that checkout at the approved Stable `main` commit. Do not reuse the Dev clone
or its chroot. The script never pulls, checks out, or selects another commit.
It derives the authorized source SHA from the clean local HEAD, requires the
locally recorded `origin/main` to match, and verifies that same SHA directly
against the current remote Stable `main` immediately before building. If remote
main advances, inspect and reconcile it first; do not silently substitute it.

The script also requires Stable `VERSION=26.3.0`, Debian 13 `amd64`, a normal
non-root builder account, and all documented build dependencies. It prints the
verified version, full source commit, remote status, and builder identity before
requesting sudo access. It then purges generated state, validates branding and
live-build configuration, and invokes `sudo lb build`; ISO generation remains
owned by the existing `auto/build` workflow. Afterward it validates the build
record, ISO, build log, boot metadata, both generated `os-release` files, Git
state, and SHA-256. Any failed check stops the workflow with an error.

`auto/build` generates one BUILD_ID from builder-local time and renders both
`os-release` paths from Stable `VERSION`. Calamares unpacks the live filesystem;
verify that the same identity survives installation. Never supply a Dev build
ID or manually edit the generated files to turn a Dev image into Stable.

After building, inspect the ISO's boot metadata with
`xorriso -indev <exact-iso> -report_el_torito plain` and verify the intended UEFI
and BIOS entries. Follow `BUILDING.md`'s final SquashFS inspection requirement,
checking both embedded `os-release` files, actual branding and
application packages, and activated Calamares metadata. The generated includes
checked above are not proof of the final ISO payload. Then boot and install
that exact ISO, compare its live/installed VERSION and BUILD_ID, and complete
the final VM and physical regression gate. A successful command block is only
a build result, not release acceptance.

## Evidence and final regression

Record a dated build and test report with:

- Repository, full source SHA, VERSION, BUILD_ID, ISO filename, size, SHA-256,
  builder timezone, package manifests, branding pin, and log references.
- VM settings and firmware mode; physical model and relevant configuration
  without personal names or unique device identifiers.
- Individual pass/fail/not-tested results, tester attribution by role, known
  limitations, and any workarounds. Preserve failures and diagnostic state.
- Live and installed `/etc/os-release` and `/usr/lib/os-release` agreement with
  the tested ISO, including `PRETTY_NAME`, VERSION, VERSION_ID, and BUILD_ID.
- Provenance linking the build SHA to any later documentation-only release SHA.

Run the full applicable progression in `TESTING.md`: UEFI boot and installation,
no-swap and bounded-swap cases, GNOME Wayland native screenshots, application
launches, terminal light/dark behavior, branding and user overrides, Calamares
cleanup, installed APT/update/reboot, GRUB/initramfs regeneration, and physical
networking, graphics, audio, storage, suspend/resume, and required peripherals.
Exercise legacy-BIOS live boot where advertised; do not extrapolate it into
unsupported storage or Secure Boot claims. Record untested peripherals honestly.
Check the manifest and live/installed inventory for unintended screenshot tools.
Keep binary logs, screenshots, manifests, ISOs, and checksum files outside Git;
record their filenames and hashes in the reports where useful.

## SourceForge publication after release authorization

Use the existing OBLinux SourceForge project and this exact directory:

```text
OBLinux-Debian-ISO/26.3.0/
```

Publish the tested Stable ISO, named
`oblinux-debian-26.3.0-${BUILD_ID}-amd64.iso`, and its SHA-256 checksum file.
Generate the checksum in the ISO's directory so its entry names the ISO without
an absolute builder path. Verify it locally with `sha256sum -c` before upload.
Do not upload an untested rebuild or rename a Dev image. Complete and document
the license/source-distribution review for the actual payload before public
upload; the presence of a repository LICENSE alone is not that review.

After publication, independently download the ISO and checksum through the
public SourceForge download interface into a separate directory. Run
`sha256sum -c`, and compare the downloaded digest with the recorded tested
artifact digest as well. Record public URLs, filename, hash, verification date,
and actual result. Do not mark publication verified until those checks pass.
GitHub retains source, immutable tag, and release metadata; SourceForge hosts
the binary download. No publication action is part of release preparation.
