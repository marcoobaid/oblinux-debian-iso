# CLAUDE.md

This file is the Claude Code entry point for `oblinux-debian-iso`, the
stable/production OBLinux Debian repository. Codex is the primary development
agent; authorized Claude Code work follows the same root governance.

**AGENTS.md is the authoritative repository operating guide. CLAUDE.md
supplements it for Claude Code and must not establish competing repository
policy.**

Before performing repository work, read `AGENTS.md` in full and follow its
documentation routing. Treat it as authoritative for repository identity and
role, architecture, ownership, Git safety, validation, promotion, and release
governance. Report any apparent conflict instead of resolving it silently.

## Required behavior

- This repository is the Stable baseline. Development and integration occur in
  `oblinux-debian-iso-dev`; shared branding is released by
  `oblinux-brand-master`. Preserve those boundaries.
- Never synchronize Dev into Stable without explicit promotion authorization.
  Preserve both histories with the approved strategy; do not rebase, squash,
  force-push, or rewrite published history.
- Follow `docs/RELEASING.md` for the 26.3.0 manual regression gate, guarded
  Stable build, provenance, and separate tagging, publication, and Dev-version
  transition authorizations.
- Never claim a build, validation, runtime, visual, publication, or checksum
  result unless it was actually executed against the stated artifact and
  environment. Report failures and skipped checks.
- Preserve this repository's Debian-specific architecture and conventions.
  Do not import another OBLinux edition's implementation mechanically.
- Do not commit or push unless explicitly requested by the owner.

## Git Commit Policy

When Claude Code creates Git commits in this repository:

- Use only the repository's configured Git author identity. Do not modify
  Git author or committer identity to represent Claude or Anthropic.
- Do not add `Co-Authored-By` trailers for Claude, Anthropic, or any AI
  system.
- Do not add `Generated-By`, `Assisted-By`, `AI-Generated`, or similar AI
  attribution trailers.
- Do not mention Claude, Anthropic, Claude Code, AI assistance, or automated
  generation anywhere in the commit message.
- Do not add Claude or Anthropic as a contributor.
- Do not add any attribution trailer unless the owner explicitly requests one
  for a specific commit.
- Write normal, professional commit messages describing the actual repository
  change, following AGENTS.md's Conventional Commit-style convention (`feat:`,
  `fix:`, `docs:`, `test:`, `build:`, `design:`, etc.).

The repository's configured human Git identity is the sole commit
attribution unless the owner explicitly instructs otherwise.
