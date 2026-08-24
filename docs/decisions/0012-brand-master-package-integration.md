# Decision 0012: consume Brand Master as a pinned package

## Status

Accepted for development integration.

## Decision

The Debian ISO repository consumes shared visual identity from an immutable
OBLinux Brand Master release and installs its versioned `oblinux-branding`
Debian package. The exact release, commit, archive SHA-256, and package version
are recorded in `branding/brand-master.lock`; moving branches are prohibited.

Debian-specific hooks may select, configure, and verify package assets, but may
not redraw or maintain copies of locked R5 artwork. The extracted live-media
GRUB background is an ignored build product from the same verified package.
The independent Papirus-derived Horizon application icon theme remains owned
by this repository because it is not part of Brand Master's product artwork.

## Consequences

Downstream Debian and Arch implementations can consume the same versioned
identity without Brand Master depending on either ISO repository. Updating the
identity requires an explicit pin review, package build, complete ISO build,
and runtime acceptance. Historical repository-owned visual assets are removed
to prevent divergent sources of truth.
