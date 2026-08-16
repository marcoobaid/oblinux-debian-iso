# Decision 0001: Debian Stable and live-build

- Status: Accepted for the POC
- Date: 2026-08-15

## Context

OBLinux needs a reliable Debian base, a live environment, and an installable ISO.
The project also needs to learn Debian-native distribution practices instead of
carrying forward assumptions from Arch Linux or Red Hat workflows.

## Decision

The POC will use Debian 13 stable (`trixie`) on `amd64`. Images will be produced
with Debian's `live-build` framework and related live-system components from
Debian repositories.

Debian stable, security, and stable-update repositories remain the primary
package sources. Testing and unstable packages will not be mixed into the POC.

## Consequences

- The POC inherits Debian's stable package versions and security lifecycle.
- Image configuration can be stored and reviewed as code.
- Some desired desktop software may be older than upstream releases.
- Backports or custom packages require explicit justification and testing.
- The project must track Debian point releases, security information, and
  derivative-distribution guidance.

