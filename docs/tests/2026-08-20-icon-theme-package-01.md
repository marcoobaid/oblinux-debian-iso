# OBLinux icon-theme package test 01

- Date: 2026-08-20
- Host: Installed OBLinux test VM
- Package: `oblinux-icon-theme` `0.1.0-1`
- Status: Package construction passed; installation lifecycle pending

## Construction results

- Package built without root privileges using Debian's `dpkg-deb`.
- Artifact size: approximately 21 MB compressed.
- Installed size declared by the package: approximately 228 MB.
- Architecture: `all`.
- Both `OBLinux-Horizon` and `OBLinux-Horizon-Dark` are present.
- The GNOME schema default override is present.
- Papirus notice and GPL-3.0 license are present.
- Maintainer scripts are executable and included in the control archive.
- Generated `icon-theme.cache` files are excluded from the package payload.
- Two complete corrected builds were byte-identical after exporting
  `SOURCE_DATE_EPOCH` to `dpkg-deb`.

## Final pre-install artifact

- Filename: `oblinux-icon-theme_0.1.0-1_all.deb`
- SHA-256:
  `c92aaa02ca8b5c9b08759eeb05aa9497003d8f132a4c2673a251f20f1f904a89`

The final hash differs from the initial reproducibility proof because the final
payload intentionally excludes inherited icon caches and adds exact cache
cleanup during package removal.

## Pending

- System installation through APT
- Confirmation that an existing explicit user preference is preserved
- Confirmation that a new user receives the Horizon default
- Light and dark system-package rendering
- Same-version reinstall
- Higher-revision upgrade simulation
- Removal, cache cleanup, and rollback
- Clean reinstallation
