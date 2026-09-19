# Issue 0006: Calamares welcome branding skipped in retained chroot

## Status

Fixed in source. The current baseline has since passed VM and physical
regression testing; see the [pre-promotion confirmation](../tests/2026-09-11-pre-promotion-owner-regression.md).
That confirmation supplies no individual checklist results; the acceptance
criteria and historical diagnosis below remain for future regression testing.

## Symptom

The Calamares Welcome page displayed the 1100-by-320 R5 OBLinux lockup at its
native size, clipping it at the right edge, and showed the literal heading
`Welcome to the OBLinux @VERSION@ installer`. The sidebar presentation was
correct.

## Root cause and ownership

This was a downstream live-build state-reuse defect, not a Brand Master asset
or shared Calamares-theme defect. Brand Master v1.0.4 correctly packages the
R5 `welcome.svg` with a proportional `viewBox="0 0 1100 320"` and no fixed
width or height. Its descriptor deliberately contains release placeholders and
has `welcomeExpandingLogo: false` for downstream activation.

The v1.0.4 ISO was regenerated after `lb clean --binary` from a retained
chroot. That rebuilt the SquashFS and ISO but did not rerun
`0110-verify-oblinux-calamares-branding.hook.chroot`. Direct inspection of the
affected ISO found the unactivated package defaults: `welcomeExpandingLogo:
false` and unresolved `@VERSION@`, URL, support, and bug-report tokens.

Calamares 3.3.14 implements the Welcome page as Qt widgets, not a
branding-supplied QML page. With `welcomeExpandingLogo: true`, it uses
`FixedAspectRatioLabel`, whose resize path scales the pixmap to the label's
content rectangle with `Qt::KeepAspectRatio`. With the false package default,
it uses a plain `QLabel` and the SVG's native dimensions, which caused the
observed clipping.

## Correction

The existing downstream hook continues to enable Calamares' proportional
expanding-label path. It now also sets empty optional version strings and both
versioned product names to `OBLinux`, so the primary heading is `Welcome to the
OBLinux installer` without hard-coding a release number. Assertions fail the
build unless those values are present.

The build guide now requires `lb clean --purge` for branding-package updates
and requires direct SquashFS inspection of the activated Calamares descriptor.
A purge rebuild reran every live hook and produced a corrected artifact.

No R5 geometry, SVG, slideshow, completion page, sidebar asset, palette, or
installer module was changed.
