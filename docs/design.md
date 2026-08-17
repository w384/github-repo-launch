# Design

## Why a standardized launch workflow?

Open-source visibility is decided early. Visitors judge a repository in the first seconds: does the README say what it does? Does the tree look complete? Does it run cleanly? Repositories that pass this first impression earn trust, and trust is what converts visitors into Stars.

Standardizing the launch removes the guesswork: every release follows the same phases with the same quality bar, so quality does not depend on the mood of the day.

## The six phases

| Phase | Purpose | Key artifacts |
| --- | --- | --- |
| 0. Baseline | Decide name, license, version, positioning | decisions, not files |
| 1. Skeleton | Complete, conventional repository shape | README, LICENSE, CHANGELOG, CONTRIBUTING, SECURITY, docs, CI |
| 2. README | First-screen conversion | README.md + README.zh-CN.md |
| 3. Quality gate | Automated pre-publish checks | scripts/check_repo_ready.py |
| 4. Commits and version | Clean history, semver tag | commit log, v0.1.0 |
| 5. Push and release | Ship to GitHub | origin, GitHub Release |
| 6. Visibility | Discoverability and verification | Description, Topics, post-push re-check |

## Design principles

- **Honest by default.** The gate reports what it actually found; READMEs and releases never claim unverified capability.
- **Zero dependencies.** The quality gate is Python standard library only, so it runs anywhere Python runs.
- **Safe by default.** Public publication requires explicit user authorization; the gate never uploads anything and scans for credentials before any push.
- **Templates over prose.** `assets/` holds copy-and-adapt output files; `references/` holds guidance for README writing and repository settings.

## Credential scanning

The gate scans for credential-shaped patterns (API keys, access tokens, private key blocks, common key prefixes) using regular expressions. Patterns are deliberately strict: an OpenAI key prefix must be followed by a long alphanumeric body, so ordinary words such as "task-" are not false positives. Test fixtures construct markers at runtime so the test suite itself stays clean.