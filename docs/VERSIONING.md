# OBLinux Versioning and Build Identification

## Policy

OBLinux Debian and OBLinux Arch share one public release cycle and versioning
policy. Their build implementations differ, but the meanings of `VERSION`,
`VERSION_ID`, and `BUILD_ID`, the promotion lifecycle, and Git tags do not.

The release version uses `YY.QUARTER.MAINTENANCE`:

- `YY` is the last two digits of the release year.
- `QUARTER` is `1`, `2`, `3`, or `4` for the planned calendar quarter.
- `MAINTENANCE` is `0` for the quarterly release and increments for bug-fix
  releases based on that quarterly release.
- Development versions append `-dev`; stable and maintenance releases do not.

Examples are `26.3.0-dev`, `26.3.0`, `26.3.1`, `26.4.0-dev`, `26.4.0`, and
`27.1.0-dev`.

The root [`VERSION`](../VERSION) file is the sole machine-readable source for
the repository's current release version. Version changes are intentional
release-management actions. Builds and unrelated changes must read this file,
not duplicate, infer, or increment its value.

## Exact build identity

Each invocation of the supported build entry point generates one `BUILD_ID`
from the builder's local time in `YYYYMMDD-HHMM` form. For example,
`20260903-1419` identifies the build started at 14:19 local time on 3 September
2026. The build wrapper generates it once, records it in the ignored
`.build/oblinux-release` file, and reuses it for every output of that build.
It requires neither manual maintenance nor network access.

On a clean build, live-build copies the rendered files through
`config/includes.chroot`. If a binary-only clean deliberately retains the
generated chroot, the wrapper refreshes the same paths there before assembly,
preventing stale build identity from crossing builds.

`VERSION` is the release identity; `BUILD_ID` distinguishes exact images of
that version. Multiple builds can therefore be:

```text
26.3.0-dev / 20260903-0915
26.3.0-dev / 20260903-1210
26.3.0-dev / 20260903-1419
```

The ISO naming convention is:

```text
oblinux-debian-${VERSION}-${BUILD_ID}-amd64.iso
```

Examples include `oblinux-debian-26.3.0-dev-20260903-1419-amd64.iso`,
`oblinux-debian-26.3.0-20260915-0900-amd64.iso`, and
`oblinux-debian-26.3.1-20261001-1830-amd64.iso`. Example timestamps are
illustrative, never configured values.

## System identity and installation

The build renders `/etc/os-release` and `/usr/lib/os-release` from the tracked
template using the authoritative `VERSION` and the build's single `BUILD_ID`.
For a development image, the significant fields are:

```text
NAME="OBLinux"
VERSION="26.3.0-dev"
VERSION_ID="26.3.0-dev"
PRETTY_NAME="OBLinux 26.3.0-dev"
BUILD_ID="20260903-1419"
```

The files retain OBLinux's Debian compatibility, codename, logo, and variant
metadata. Debian's Calamares configuration installs by unpacking the exact
live `filesystem.squashfs`. These OBLinux-owned files are not part of the
installer-only settings package removed from the target, so the same release
and build identity survives installation. A tester must still verify the live
and installed files against the ISO filename during acceptance testing.

## Current Stable candidate and tags

The current repository state is:

```text
oblinux-debian-iso:       VERSION = 26.3.0
promoted Dev source:      d9289b2bbcaf1fb44a9b926fee0a7e40bf724bed
future Git tag:           v26.3.0 (not created)
SourceForge publication:  not performed

AFTER RELEASE, WITH SEPARATE OWNER AUTHORIZATION
oblinux-debian-iso-dev:   VERSION = 26.4.0-dev
```

Promotion removed `-dev` as an intentional Stable metadata change. The Stable
artifact must be built from the exact authorized Stable `main` commit and must
receive its own generated `BUILD_ID`; the accepted Dev artifact cannot be
renamed or represented as the Stable build. Complete the final VM and physical-
hardware regression gate before declaring release readiness. Automated CI is
not a prerequisite for this release; it remains a future enhancement. Record
the tested source commit, ISO identity, checksum, and results under
[RELEASING.md](RELEASING.md). Tagging then requires separate owner
authorization, as defined in
[AGENTS.md](../AGENTS.md#release-and-tagging-policy). The stable tag is `v` followed by the
stable version. A maintenance release such as `26.3.1` receives tag `v26.3.1`.
`BUILD_ID` never changes the release version or Git tag.

The promotion, tag, publication, and subsequent development-version advance are
separate authorized operations. This document does not authorize tagging,
publication, or advancing the development version.
