# Decision 0004: Installed-system APT policy

- Status: Accepted
- Date: 2026-08-19

## Context

Build 002 used the final-source helper from `calamares-settings-debian`. It
enabled `main` and `non-free-firmware`, included source-package repositories,
and enabled Debian backports by default. The live image itself was built from
`main`, `contrib`, `non-free`, and `non-free-firmware`, so the installed system
did not retain access to every component used to compose it.

OBLinux needs an explicit, conservative policy that remains understandable to
users and does not silently depend on Debian helper defaults.

## Decision

The installed system will enable the Debian 13 stable, stable-updates, and
security repositories with these components:

- `main`
- `contrib`
- `non-free`
- `non-free-firmware`

Backports will not be enabled by default. Source-package entries will not be
enabled by default. Advanced users may add either intentionally when needed.

The first implementation overrides Debian's `calamares-sources-final` helper
inside the live image. This keeps the already-tested Debian Calamares sequence
while making the resulting source list an OBLinux-owned configuration.

## Consequences

- Installed systems can resolve packages from every Debian component used by
  the image build.
- Routine upgrades remain on Debian stable, updates, and security suites.
- Backports cannot unexpectedly become an installation candidate source.
- Users who need source packages or backports must enable them explicitly.
- The override must be checked whenever `calamares-settings-debian` changes.
- A future OBLinux settings package should own this helper instead of relying
  on a file overlay.
