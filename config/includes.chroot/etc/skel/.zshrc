# OBLinux interactive Zsh defaults. This file belongs to the user after
# account creation and may be edited or replaced without affecting the system.

autoload -Uz compinit
compinit

HISTFILE="${ZDOTDIR:-$HOME}/.zsh_history"
HISTSIZE=10000
SAVEHIST=10000
setopt append_history share_history hist_ignore_dups hist_reduce_blanks
setopt auto_cd interactive_comments

bindkey -e
bindkey '^[[H' beginning-of-line
bindkey '^[[F' end-of-line
bindkey '^[[3~' delete-char

if [[ -r /usr/share/zsh-autosuggestions/zsh-autosuggestions.zsh ]]; then
  source /usr/share/zsh-autosuggestions/zsh-autosuggestions.zsh
fi

if command -v starship >/dev/null 2>&1; then
  eval "$(starship init zsh)"
fi

# Debian 13's Ptyxis 48.5 can construct its first terminal before the final
# system appearance reaches its palette listener. Refresh the system-following
# style once so a light session cannot retain the dark face's foreground.
# Explicit user-selected light or dark Ptyxis styles are never changed.
if [[ -o interactive && -t 1 && ${SHLVL:-1} -eq 1 ]] \
    && command -v gsettings >/dev/null 2>&1 \
    && [[ $(gsettings get org.gnome.Ptyxis interface-style 2>/dev/null) \
        == "'system'" ]]; then
  case $(gsettings get org.gnome.desktop.interface color-scheme 2>/dev/null) in
    "'prefer-dark'")
      gsettings set org.gnome.Ptyxis interface-style dark
      ;;
    *)
      gsettings set org.gnome.Ptyxis interface-style light
      ;;
  esac
  gsettings reset org.gnome.Ptyxis interface-style
fi

# Show the branded system summary once per top-level interactive terminal.
# Set OBLINUX_FASTFETCH=0 in the environment or comment this block to disable.
if [[ -o interactive && -t 1 && ${SHLVL:-1} -eq 1 \
    && ${OBLINUX_FASTFETCH:-1} != 0 ]] \
    && command -v fastfetch >/dev/null 2>&1; then
  fastfetch
fi

# Syntax highlighting must be loaded after other Zsh integrations.
if [[ -r /usr/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh ]]; then
  source /usr/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
fi
