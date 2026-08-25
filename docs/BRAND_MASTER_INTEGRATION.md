# Brand Master integration

OBLinux Debian consumes the shared visual identity from
`oblinux-brand-master`. Shared artwork is not designed or maintained in this
repository. Visual changes must be made in Brand Master, released there, and
then adopted here through an intentional version update.

## Current pin

- Release: `v1.0.2`
- Commit: `c68c76d3847714ac66f0e3ebea1fc61984dd556d`
- Commit archive SHA-256:
  `d6fe90702787ce13e9eb67883dd6e2488f269af2a888a875fcc096f27e93e5f5`
- Debian package: `oblinux-branding` `1.0.2-1`

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

Brand Master v1.0.2 supplies valid `3.0 (quilt)` Debian source metadata, so the
temporary source-format compatibility adjustment required by v1.0.0 is no
longer present downstream.

Brand Master owns the R5 masters, colors, wallpapers, hicolor product icons,
Plymouth theme, GRUB theme, and Calamares presentation. Debian-specific hooks
select those assets, render release metadata into Calamares, configure GNOME,
select Plymouth and GRUB, provide system identity, and verify package payloads.
The dedicated package-owned `oblinux-about.svg` is the source for GNOME's
scalable vendor emblem. Debian generates a presentation wrapper with the
256-by-256 intrinsic dimensions calibrated from the stable repository's
runtime-tested 128-by-128 baseline while keeping the source viewBox and
geometry unchanged. The normal `oblinux-logo` hicolor
application icon remains unchanged for every other consumer.
The live hook removes the inactive presentation files shipped by
`calamares-settings-debian` after selecting Brand Master's Calamares theme;
Debian's installer modules, settings, and cleanup behavior remain intact.
The separate OBLinux Horizon application icon theme remains downstream because
it is a full Papirus-derived desktop icon theme, not shared logo artwork.

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
5. Build the package and complete ISO on Debian 13.
6. Perform the VM/manual journey in `docs/tests/BRAND_MASTER_RUNTIME_TEST.md`.
7. Promote only after separate review; never silently follow a moving branch.

## Validation

Static integration checks:

```bash
scripts/validate-branding-integration
```

Complete build validation remains the standard sequence:

```bash
lb config
lb config --validate
sudo lb build
```

The build is followed by ISO inspection and the runtime checklist. Static
checks do not establish that GRUB, Plymouth, GNOME, GDM, or Calamares rendered
correctly at runtime.
