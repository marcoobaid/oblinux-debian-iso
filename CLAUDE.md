# CLAUDE.md

This file is the Claude Code entry point for `oblinux-debian-iso-dev`.
Codex is the primary development agent; authorized Claude Code work follows
the same root governance.

**AGENTS.md is the authoritative repository operating guide. CLAUDE.md
supplements it for Claude Code and must not establish competing repository
policy.**

Before performing any repository work, read `AGENTS.md` in full and treat it
as authoritative for repository identity and role, architecture, ownership,
Git safety, validation, promotion, and governance. Where this file and
AGENTS.md appear to conflict, AGENTS.md controls; report the conflict rather
than resolving it silently.

## Required behavior

- Read `AGENTS.md` before making changes, and consult the specific
  authoritative document it routes to (see its "Documentation routing"
  section) before modifying the associated subsystem.
- Follow all repository-role, architecture, ownership, validation, Git
  safety, and promotion rules defined in `AGENTS.md`.
- Never claim a build, validation, runtime, or visual test passed unless it
  was actually executed successfully on the stated artifact and environment.
  Report what was actually run, including failures and skipped steps.
- Respect the boundaries between this repository (`oblinux-debian-iso-dev`,
  push-capable development/staging), the stable `oblinux-debian-iso`
  repository (read-only reference; promotion requires explicit owner
  authorization), `oblinux-brand-master` (immutable upstream releases; do not
  patch shared R5 artwork downstream), and any legacy repository, exactly as
  AGENTS.md defines them.
- Never force-push or rewrite published Git history unless the owner has
  explicitly authorized it for a specific, named recovery situation.
- Never promote development changes into a stable repository without
  explicit owner approval. Follow `docs/RELEASING.md` for the 26.3.0 manual
  regression gate and separate promotion, tagging, publication, and Dev-version
  transition authorizations; preparation alone authorizes none of these.
- Preserve this repository's own architecture and conventions; do not carry
  over assumptions from another OBLinux repository just because it looks
  similar.
- Do not commit or push unless explicitly requested (per AGENTS.md's change
  and Git discipline section).

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
