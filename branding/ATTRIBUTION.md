# Branding Attribution

## Inter

The outlined OBLinux wordmark drafts were generated from Inter Display 4.1 as
packaged by Debian 13 in `fonts-inter` version `4.1+ds-1`.

- Upstream project: <https://github.com/rsms/inter>
- Debian package: `fonts-inter` 4.1+ds-1
- Upstream copyright: 2016–2023 The Inter Project Authors
- Upstream license: SIL Open Font License 1.1 and Apache License 2.0

Exact generation inputs:

| File | SHA-256 |
| --- | --- |
| `InterDisplay-Bold.otf` | `d7a7394984bbb3bc3c3e507a6618d34e006c94f27c7105d0ef4376667aeaf4ee` |
| `InterDisplay-Regular.otf` | `35c1f7437dd6d63f4e60a49144df4b4e4edc190e13ffc1e54b86083747fe3acf` |

The font binaries are not stored in this repository or added to the ISO by the
branding work. The generated wordmarks contain outlined letter paths and have
no runtime dependency on Inter.

Debian's packaged copyright record states that the requirement for fonts to
remain under the SIL Open Font License does not apply to documents created
using the fonts. This attribution is retained for provenance and reproducible
generation.

## OBLinux artwork

The OBLinux symbol geometry and brand composition are original project assets.
They are licensed under the Creative Commons Attribution-ShareAlike 4.0
International license. See `LICENSE-CC-BY-SA-4.0.txt`.

Suggested attribution: `OBLinux artwork, OBLinux Project, CC BY-SA 4.0`.

The artwork license does not grant trademark rights or imply that a modified
system is an official OBLinux release. A public trademark and naming policy is
future release work.

## Obsidian Horizon wallpaper

The clean wallpaper master was generated for the OBLinux Project with OpenAI's
built-in image-generation tool from a project-authored visual specification.
The approved composition was then scaled and combined with the authoritative
outlined OBLinux wordmark through deterministic project tooling.

| File | SHA-256 |
| --- | --- |
| `source/oblinux-horizon-master.png` | `f83e53ffe0c11877e4321a1fc048239da08bc7ae776be02a7a67f1b6fe8fb865` |
| `wallpapers/oblinux-horizon-clean-3840x2160.jpg` | `b8073c48afb64843b1b96114915f29116e3b770e7acd9cb181dbc2f0474d1a5b` |
| `wallpapers/oblinux-horizon-branded-3840x2160.jpg` | `429f302ec916322a240a4e9f05cffb491bf541e130d2aedafc38a59993af47b2` |

The clean and branded wallpaper variants are original OBLinux artwork released
under CC BY-SA 4.0 with the rest of the branding assets.

## Boot and installer derivatives

Build 005 derives its boot symbol, Calamares logo, and installer welcome image
from the approved OBLinux symbol and Obsidian Horizon wallpaper.

| File | SHA-256 |
| --- | --- |
| `source/oblinux-installer-icon.svg` | `86739c03f2702bbdb74c18eca3298cf1485023e8209815eaa6daad461bd8f81b` |
| `installer/oblinux-logo.png` | `1ffb98650647519dfc6f6050ab3d01406c34e07fcfeee723f3a064caa8252b23` |
| `installer/slide1.png` | `8a21ba3ab112dcb7b10726b9bf7eab4058e23fae2005790e36bcba8bef139bd2` |

These derivative assets are released under CC BY-SA 4.0 with the source
identity and wallpaper.

## Installed-system derivatives

Build 006 reuses the approved symbol for GNOME About and derives its Plymouth
logo and progress textures from the Build 005 installer assets.

| File | SHA-256 |
| --- | --- |
| `system/plymouth-logo.png` | `1ffb98650647519dfc6f6050ab3d01406c34e07fcfeee723f3a064caa8252b23` |
| `system/progress-background.png` | `b78b40b470c8f6b5e81f2a9a7c290d74a5e6c347687e7dd8ac6a38e6395fc78e` |
| `system/progress-fill.png` | `40f84aad2a9527d2f482d85fc5d959b8b6c23f0ba8d3a35c9eb334ab97fa22ee` |

The raster assets and direct SVG integration remain under CC BY-SA 4.0.
