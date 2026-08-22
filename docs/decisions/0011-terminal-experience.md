# Decision 0011: OBLinux terminal experience

- Status: Accepted for implementation
- Date: 2026-08-22

## Context

OBLinux is intended to be a practical developer workstation as well as a user-friendly desktop. The terminal should therefore be useful immediately, visually consistent with the OBLinux identity, and understandable to maintain without depending on a network-fetched shell framework.

The live environment and the system installed by Calamares must also behave consistently. Live-session conveniences must not be copied accidentally as hidden installer state.

## Decision

OBLinux will provide the following terminal defaults:

- Zsh is the default interactive shell for the live account, the account created by Calamares, and future locally created users.
- Bash remains installed and available as a recovery and compatibility shell.
- Starship supplies a compact developer prompt with Git state, command duration, exit status, and the OBLinux navy/cyan palette.
- Debian-packaged `zsh-autosuggestions` and `zsh-syntax-highlighting` provide interactive assistance.
- Fastfetch displays a small OBLinux ASCII wordmark and a concise system summary when the first interactive shell starts.
- Ptyxis receives an OBLinux Horizon palette with modest transparency and uses the user's login shell.

Reusable user defaults live under `/etc/skel`. The build explicitly configures Calamares to assign `/bin/zsh`; it does not rely on a live-session side effect. System dconf defaults establish the initial Ptyxis profile but remain user-overridable.

## Consequences

- New users receive a coherent terminal on first login.
- Existing users can replace or remove any shell, prompt, Fastfetch, or terminal preference in their own home directory.
- OBLinux does not use Oh My Zsh by default, avoiding an additional network-delivered framework and its maintenance surface.
- Changes to the terminal defaults require both live-session and installed-system regression testing.
