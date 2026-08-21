# OBLinux icon-theme package test 01

- Date: 2026-08-20
- Host: Installed OBLinux test VM
- Package: `oblinux-icon-theme` `0.1.0-1`
- Status: Construction and initial system installation passed; visual,
  upgrade, removal, and reinstallation tests pending

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

- Visual confirmation from the system-installed package
- Light and dark system-package rendering
- Same-version reinstall
- Higher-revision upgrade simulation
- Removal, cache cleanup, and rollback
- Clean reinstallation

## Initial installation results

The final artifact was installed through APT from the test user's home
directory. APT emitted an `_apt` sandbox warning because the user's home
directory is private; APT intentionally fell back to reading the local package
as root. Package unpacking and configuration completed successfully.

- Installed package/version: `oblinux-icon-theme 0.1.0-1`
- `dpkg --audit`: clean
- Failed systemd units: 0
- Theme files: root-owned and readable
- Light and dark icon caches: present
- Broken system-theme symlinks: 0
- Existing explicit preference remained `Adwaita`: passed
- In-memory system/default preference is `OBLinux-Horizon-Dark`: passed
- Per-user Horizon directories absent during verification: passed

After these checks, the test account was explicitly switched to the packaged
`OBLinux-Horizon-Dark` theme for visual review.
