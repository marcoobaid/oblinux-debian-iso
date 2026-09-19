# Accepted Debian 26.3.0 Dev candidate

## Promotion authority

On 2026-09-18, promotion of the exact Dev source below into the Stable
repository was authorized:

- Dev repository: `oblinux-debian-iso-dev`
- Source commit: `d9289b2bbcaf1fb44a9b926fee0a7e40bf724bed`
- ISO: `oblinux-debian-26.3.0-dev-20260918-1057-amd64.iso`
- VERSION: `26.3.0-dev`
- BUILD_ID: `20260918-1057`
- SHA-256:
  `00d8e4c849304645e2062fe721b48f97facb4f4a3327cd4371cd820487b78827`

VM installation/regression, physical laptop installation/regression, and
overall functional testing passed, with no known release-blocking findings.
This is reported acceptance evidence; this promotion task did not rebuild the
artifact or independently rerun those tests.

## Evidence boundary

This record authorizes source promotion. It does not claim that a Stable ISO
was built or tested, and it does not transfer the Dev artifact's BUILD_ID to a
future Stable image. Stable must use `VERSION=26.3.0`, generate its own BUILD_ID
from the exact authorized Stable commit, and pass the final validation required
by [the release procedure](../RELEASING.md).

The `v26.3.0` tag and SourceForge publication were not authorized as part of
promotion and were pending at that time. The subsequent Stable 26.3.0 release
is complete; its separate certified artifact and tag are recorded in
[RELEASING.md](../RELEASING.md). The separate Dev repository remains at
`26.3.0-dev` until a later explicitly authorized post-release transition.
