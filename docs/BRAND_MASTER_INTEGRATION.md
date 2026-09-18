# Brand Master integration

OBLinux Debian consumes the shared visual identity from
`oblinux-brand-master`. Shared artwork is not designed or maintained in this
repository. Visual changes must be made in Brand Master, released there, and
then adopted here through an intentional version update.

## Current pin

- Release: `v1.0.4`
- Commit: `13e211da2ccd43156fcc7dc7e57c3be7bb5ee47d`
- Commit archive SHA-256:
  `48e2985de37567838802d4d6346bb846ff8135b5488ae65d56205ed7fe85d9e1`
- Debian package: `oblinux-branding` `1.0.4-1`

The machine-readable pin is `branding/brand-master.lock`. Builds never consume
Brand Master `main` or another moving ref.

## Build integration

`scripts/prepare-branding-package` downloads the immutable commit archive,
verifies its checksum, builds Brand Master's Debian package, validates the
package metadata, and places the untracked package in `config/packages.chroot`.
Live-build installs it through the normal local-package mechanism. The same
step extracts the package-owned GRUB background for the live-media bootloader;
the extracted file is ignored by Git and is not an independently maintained
artwork copy.

Brand Master v1.0.4 supplies valid `3.0 (quilt)` Debian source metadata, so the
temporary source-format compatibility adjustment required by v1.0.0 is no
longer present downstream.

Brand Master owns the R5 masters, colors, wallpapers, hicolor product icons,
Plymouth theme, GRUB theme, and Calamares presentation. Debian-specific hooks
select those assets, render release metadata into Calamares, configure GNOME,
select Plymouth and GRUB, provide system identity, and verify package payloads.
GNOME's scalable vendor emblem resolves to a generated direct-file variant of
the same Brand Master hicolor SVG used by Arch. Debian compiles GNOME Control
Center to load the vendor emblem by filename, bypassing `LOGO`; Arch resolves
`LOGO=oblinux-logo` through the icon theme at 192 pixels. Debian therefore adds
only 192-by-192 intrinsic dimensions to the byte-identical 512-unit SVG canvas,
matching Arch's size request without padding or altering symbol geometry.
The live hook removes the inactive presentation files shipped by
`calamares-settings-debian` after selecting Brand Master's Calamares theme;
Debian's installer modules, settings, and cleanup behavior remain intact.
The separate OBLinux Horizon application icon theme remains downstream because
it is a full Papirus-derived desktop icon theme, not shared logo artwork.
Brand Master also supplies the shared FastFetch logo and reusable configuration
under `/usr/share/oblinux/terminal/fastfetch/`. Debian's system-wide default at
`/etc/xdg/fastfetch/config.jsonc` references the package-owned logo directly and
matches the Arch edition's curated module order and formatting. Debian 13's
FastFetch 2.40.4 requires ANSI true-color expressions
instead of hexadecimal color strings, so the downstream configuration expresses
the canonical blue and orange as `38;2;30;77;140` and `38;2;255;138;0`.
Existing users' FastFetch configuration remains untouched.

## Legacy migration

The previous Obsidian-era logos, boot artwork, installer rasters, generators,
and duplicated shared runtime payloads were removed. OBLinux Debian
intentionally retains the two established Obsidian Horizon wallpaper JPEGs and
selects the branded variant through later dconf and schema defaults; this
Debian-edition choice does not alter Brand Master's cross-distribution
wallpaper defaults. The neutral default account avatar, GDM's supported dconf
gradient, terminal defaults, Calamares installer behavior, and Debian
APT/installation policy also remain Debian-specific. Vendor-logo alternatives
reference icons installed by `oblinux-branding` instead of legacy generated
logo copies.

## Upgrade process

1. Review and approve a new Brand Master release.
2. Update all values in `branding/brand-master.lock`.
3. Review the package manifest and integration documentation for changes.
4. Run `scripts/validate-branding-integration`.
5. Purge retained build state and build the package and complete ISO on Debian
   13 using the [branding rebuild procedure](BUILDING.md#clean-rebuilds).
6. Perform the VM/manual journey in `docs/tests/BRAND_MASTER_RUNTIME_TEST.md`.
7. Promote only after separate review; never silently follow a moving branch.

## Validation

Static integration checks:

```bash
scripts/validate-branding-integration
```

For a branding-package update, use the complete purge rebuild sequence:

```bash
sudo lb clean --purge
scripts/validate-branding-integration
lb config
lb config --validate
sudo lb build
```

The build is followed by ISO inspection and the runtime checklist. Static
checks do not establish that GRUB, Plymouth, GNOME, GDM, or Calamares rendered
correctly at runtime.
