# Brand Master integration

OBLinux Debian consumes the shared visual identity from
`oblinux-brand-master`. Shared artwork is not designed or maintained in this
repository. Visual changes must be made in Brand Master, released there, and
then adopted here through an intentional version update.

## Current pin

- Release: `v1.0.0`
- Commit: `5f8e1d89ce69847f4cca60f82741ff0c779b25b3`
- Commit archive SHA-256:
  `526aadce93f95468b795c2d8c4040b031afb3bea77def98f47e7717fd247785c`
- Debian package: `oblinux-branding` `1.0.0-1`

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

Brand Master v1.0.0 combines Debian source format `3.0 (native)` with package
version `1.0.0-1`. Debian rejects a native source package that has a Debian
revision, so the preparation script changes only the temporary build tree to
`3.0 (quilt)` before its binary-only build. The verified archive, locked visual
files, binary payload, and upstream tag remain unchanged. A future Brand Master
release should correct its source metadata, after which this compatibility step
can be removed during an intentional pin update.

Brand Master owns the R5 masters, colors, wallpapers, hicolor product icons,
Plymouth theme, GRUB theme, and Calamares presentation. Debian-specific hooks
select those assets, render release metadata into Calamares, configure GNOME,
select Plymouth and GRUB, provide system identity, and verify package payloads.
The live hook removes the inactive presentation files shipped by
`calamares-settings-debian` after selecting Brand Master's Calamares theme;
Debian's installer modules, settings, and cleanup behavior remain intact.
The separate OBLinux Horizon application icon theme remains downstream because
it is a full Papirus-derived desktop icon theme, not shared logo artwork.

## Legacy migration

The previous Obsidian Horizon logos, wallpapers, boot artwork, installer
rasters, generators, and duplicated runtime payloads were removed. The neutral
default account avatar, GDM's supported dconf gradient, terminal defaults,
Calamares installer behavior, and Debian APT/installation policy remain as
Debian-specific integration. Vendor-logo alternatives now reference icons
installed by `oblinux-branding` instead of legacy generated logo copies.

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
