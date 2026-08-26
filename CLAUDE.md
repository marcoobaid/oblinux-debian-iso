# CLAUDE.md

This file is the Claude Code entry point for this repository. **AGENTS.md is
the authoritative repository operating guide. CLAUDE.md supplements it for
Claude Code and must not establish competing repository policy.**

## Before doing any work

1. Read `AGENTS.md` at the repository root in full before making changes.
2. Treat it as authoritative for repository role, architecture, ownership,
   validation, Git safety, and promotion rules — this file does not repeat
   that content, and if anything here ever appears to conflict with it,
   AGENTS.md wins.
3. Follow the documentation routing table in AGENTS.md and consult the
   specific authoritative document for the subsystem being changed (e.g.
   `docs/BUILDING.md`, `docs/INSTALLER.md`, `docs/TESTING.md`,
   `docs/ARCHITECTURE.md`) before modifying it. Do not assume behavior from
   another OBLinux repository; preserve this repository's own architecture.

## Hard boundaries

- This repository (`oblinux-debian-iso`) is the **stable/production**
  baseline. Development, integration, and ISO validation happen in
  `oblinux-debian-iso-dev`; shared branding is owned upstream in
  `oblinux-brand-master`. Respect these boundaries exactly as AGENTS.md
  defines them.
- Never promote development changes into this stable repository without
  explicit owner approval. A successful dev build is not approval.
- Never merge, rebase, reset, cherry-pick, or otherwise synchronize changes
  from another repository into this one outside an authorized promotion.
- Never force-push or rewrite published Git history unless the owner
  explicitly authorizes it for a specific recovery situation.
- Never claim a build, validation, runtime, or visual test passed unless it
  was actually executed against the stated artifact and environment. Report
  what was actually run, including failures and skipped steps.

## Git Commit Policy

When Claude Code creates Git commits in this repository:

- Use only the repository's configured Git author identity. Do not modify
  Git author or committer identity to represent Claude or Anthropic.
- Do not add `Co-Authored-By` trailers for Claude, Anthropic, or any AI
  system, and do not add `Generated-By`, `Assisted-By`, `AI-Generated`, or
  similar AI-attribution trailers.
- Do not mention Claude, Anthropic, Claude Code, AI assistance, or automated
  generation anywhere in the commit message.
- Do not add Claude or Anthropic as a contributor.
- Do not add any attribution trailer unless the owner explicitly requests
  one for a specific commit.
- Write normal, professional commit messages describing the actual change,
  following the Conventional Commit-style conventions already used in this
  repository's history (`feat:`, `fix:`, `docs:`, `test:`, `build:`,
  `design:`).

Example — correct:

```
Integrate Brand Master v1.0.2
```

Example — incorrect (do not do this):

```
Integrate Brand Master v1.0.2

Co-Authored-By: Claude Sonnet <noreply@anthropic.com>
```

This policy applies to every commit Claude Code creates in this repository,
without exception, unless the owner explicitly instructs otherwise for a
specific commit.
