# OBLinux icon-theme package test 01

- Date: 2026-08-20
- Host: Installed OBLinux test VM
- Package: `oblinux-icon-theme` `0.1.0-1`
- Status: Construction, initial system installation, light/dark visual tests,
  and same-version reinstallation passed; upgrade, removal, and clean
  reinstallation tests pending

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

## Visual results

The complete application grid and GNOME Files were inspected using the themes
installed by the Debian package, with no per-user Horizon theme directories
present to shadow the system installation.

- `OBLinux-Horizon-Dark` application-grid rendering: passed
- `OBLinux-Horizon-Dark` application containers and horizon accents: passed
- `OBLinux-Horizon` application-grid rendering: passed
- `OBLinux-Horizon` GNOME Files rendering: passed
- Light folder colors and symbolic toolbar/sidebar icons: passed
- Application identity remains recognizable in both variants: passed
- Visual consistency between applications, folders, and the dock: passed

GNOME's Activities and application overview retains a dark shell background
when the light desktop color scheme is selected. This is GNOME Shell behavior,
not evidence that `OBLinux-Horizon-Dark` remains active. GNOME Files visibly
used the light interface and light Horizon assets during the test.

## Same-version reinstallation results

APT reinstalled `oblinux-icon-theme 0.1.0-1` over the installed copy using the
local package artifact. The `_apt` sandbox warning was expected because the
artifact resides in a private home directory; unpacking and configuration
completed successfully.

- Installed package/version remains `0.1.0-1`: passed
- Explicit `OBLinux-Horizon` user preference preserved: passed
- Light and dark system theme directories present: passed
- Light and dark icon caches regenerated and present: passed
- Broken system-theme symlinks: 0
- Non-root-owned system-theme entries: 0
- `dpkg --audit`: clean
- Failed systemd units: 0

## Pending

- Higher-revision upgrade simulation
- Removal, cache cleanup, and rollback
- Clean reinstallation
