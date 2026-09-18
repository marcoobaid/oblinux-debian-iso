# Debian 26.3.0 preparation: static validation

## Scope

Preparation changes in Dev, based on `f50c5f7711653873b0b7c9b962a11892834a9826`.
This record accompanies the preparation commits, not a built release artifact.
The source VERSION remains `26.3.0-dev`. Stable was not modified; no ISO was
built, promoted, tagged, or published.

The owner authorized native GNOME screenshots as the default and final VM plus
physical-hardware regression as the 26.3.0 release gate. The current procedure
is [RELEASING.md](../RELEASING.md). Earlier dated evidence remains unchanged.

## Executed checks

Performed on the macOS development workstation:

- `scripts/validate-branding-integration`: passed, including temporary Dev
  metadata rendering, branding pins, integration assertions, and hook syntax.
- Shell syntax (`sh -n` or `bash -n` according to each shebang): passed for
  15 scripts in `auto/`, `scripts/`, and `config/hooks/live/`.
- The guarded Stable command block in `RELEASING.md`: Bash syntax passed.
  Execution against the Dev checkout with its real full HEAD supplied as the
  candidate SHA rejected the Dev origin before network, sudo, cleaning, or
  building. This was an intentional negative guard test, not a build attempt.
- Isolated copy of the release renderer and template with a temporary
  `VERSION=26.3.0`: both generated os-release files matched and carried the
  expected Stable VERSION, VERSION_ID, PRETTY_NAME, and supplied test BUILD_ID.
  No repository VERSION or generated includes were changed by this check.
- Active `config/`, `auto/`, and `scripts/` search: no Flameshot references.
  Documentation describes native capture without promising annotation parity.
- Changed-document local Markdown link targets and `git diff --check`: passed.
- Reviewed the unchanged Dev origin guard, release-state/CI wording, and
  historical-record preservation.

## Limits and next validation

`lb` and ShellCheck are unavailable on this workstation. No `lb config`,
`lb config --validate`, Linux chroot hook execution, package dependency-closure
inspection, ISO build, screenshot runtime test, or VM/physical regression was
performed. Shell syntax validation is not ShellCheck or live-build validation.
The Stable procedure's positive build path still requires the authorized
post-promotion Debian builder run; its early refusal and metadata rendering
checks do not establish a successful Stable build.

Next, obtain authorization to build the Dev regression candidate with the
unchanged guarded `scripts/build-iso` on Debian 13 amd64. Record its actual
source SHA, ISO filename, VERSION, BUILD_ID, checksum, package manifests, and
log. Verify Flameshot is absent from the actual image, then complete VM and
physical regression. Promotion and the separately built Stable artifact remain
later gates; this static record does not declare release readiness.
