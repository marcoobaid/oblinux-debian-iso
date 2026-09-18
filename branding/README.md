# OBLinux branding integration

Shared OBLinux visual assets are owned and released by the separate
`oblinux-brand-master` repository. This downstream repository does not redraw,
regenerate, or independently maintain the R5 identity.

## Structure

- `brand-master.lock`: immutable Brand Master release, commit, archive checksum,
  and Debian package version consumed by the ISO build
- `icon-theme/`: the independent Papirus-derived OBLinux application icon theme

See `docs/BRAND_MASTER_INTEGRATION.md` for the package-first integration and
upgrade procedure. Historical build records describe the legacy artwork that
was present at those revisions; they are not current asset authority.
