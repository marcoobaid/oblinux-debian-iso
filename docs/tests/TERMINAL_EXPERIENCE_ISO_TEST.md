# Terminal experience ISO acceptance test

Use this checklist for the first ISO containing the OBLinux terminal experience.

## 1. Live session

Boot the ISO normally and open Ptyxis.

Confirm:

- the live user autologs in as before;
- Ptyxis opens without an error;
- the shell is Zsh;
- the Starship prompt is visible and remains readable;
- Fastfetch displays the OBLinux ASCII wordmark once when the first terminal is opened;
- Fastfetch follows the terminal foreground in light and dark styles, without bright red fixed styling or an ANSI palette strip;
- command completion, autosuggestions, and syntax highlighting work;
- the terminal uses the OBLinux navy/cyan palette and modest transparency;
- opening another interactive shell does not print Fastfetch repeatedly.

Run:

```bash
printf 'shell=%s\n' "$SHELL"
ps -p $$ -o comm=
command -v bash zsh starship fastfetch
zsh --version
fastfetch --version
```

Expected: `$SHELL` is `/bin/zsh`, the current shell is Zsh, and every command is present.

## 2. Installed account

Complete a clean Calamares installation and boot the installed system. Open Ptyxis and repeat the visual checks above.

Run:

```bash
getent passwd "$USER" | cut -d: -f1,7
printf 'shell=%s\n' "$SHELL"
ps -p $$ -o comm=
command -v bash zsh starship fastfetch
test -r ~/.zshrc && echo 'PASS: Zsh configuration present'
test -r ~/.config/starship.toml && echo 'PASS: Starship configuration present'
test -r ~/.config/fastfetch/config.jsonc && echo 'PASS: Fastfetch configuration present'
```

Expected: the installed account and active session use `/bin/zsh`; Bash remains available; all three user configuration checks pass.

## 3. User control and regression

Confirm:

- Ptyxis profile settings can still be changed by the user;
- a new Ptyxis window retains the selected OBLinux palette;
- light and dark desktop styles keep terminal text readable;
- `bash` starts a usable Bash session and `exit` returns to Zsh;
- networking, GNOME Settings, Files, and `sudo apt update` still work;
- the installed system contains no Calamares launcher or live-only GNOME settings.

Record the ISO SHA-256, firmware mode, VM or hardware model, and pass/fail result with the build evidence.
