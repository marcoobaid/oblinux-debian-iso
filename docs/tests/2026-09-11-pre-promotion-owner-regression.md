# Pre-promotion regression confirmation

## Baseline and result

Recorded on 2026-09-11 (America/Chicago) from the supplied documentation-task
instructions. Regression testing was reported successful on both:

- Virtual machines
- Physical hardware

The functional tested baseline before documentation normalization is
`e8f22901cefad1bd0b8d9353d161dd88cacf5cf2`. At task start, branch `main`, local
HEAD, and local `origin/main` all identified that commit, and the working tree
was clean. Documentation commits after this baseline do not represent new
functional ISO changes.

The current implementation is approved for stable promotion subject to
documentation, version, and repository checks. This confirmation does not
authorize performing promotion in this documentation task.

## Evidence limits

This is a reported regression result; testing was not rerun as part of the
documentation update. The confirmation does not supply an ISO filename,
checksum, build ID, hardware inventory, test dates, or per-check command output.
Do not infer those details or mark every historical checklist item passed.
Earlier dated build/test records retain their artifact-specific results,
including superseded-artifact warnings.

The confirmation supersedes general statements that the current functional
baseline still awaits VM or physical regression acceptance. It does not
expand supported installation scenarios, claim broad hardware support, or
establish public production readiness.

## Promotion handoff

- Authoritative policy: [VERSIONING.md](../VERSIONING.md)
- Current development version: `26.3.0-dev` (September 2026, Q3)
- Planned stable promotion version: `26.3.0`
- Subsequent development version: `26.4.0-dev`, only after promotion
- Brand Master pin: `v1.0.4`, package `oblinux-branding` `1.0.4-1`

No product-version change is needed for this documentation task. Stable
promotion must intentionally remove `-dev` in the stable repository and verify
release metadata, ISO identity, and the final repository checks. The existing
release policy requires passing CI before a release tag; this development
repository currently contains no tracked CI workflow. The promotion task must
establish how that gate is satisfied rather than claim a CI pass.

`BUILD_ID` uses builder-local `YYYYMMDD-HHMM` time. Its minute resolution is not
a globally unique identifier; retain artifact checksums alongside it. The build
wrapper refuses to overwrite an existing ISO of the same name.
