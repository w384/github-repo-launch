# Demo

Worked example: publishing a Codex skill as a polished open-source repository. The reference implementation is [thread-archive-restart](https://github.com/w384/thread-archive-restart) — a published skill repository that followed this workflow.

## Step 0 — Baseline

- Name: matches the directory and package name.
- License: MIT (default preference), copyright line "2026 thread-archive-restart contributors".
- Version: v0.1.0 (first release, semver).

## Step 1 — Skeleton

Repository root gets the conventional shape: README.md, README.zh-CN.md, LICENSE, CHANGELOG.md, CONTRIBUTING.md, SECURITY.md, docs/, .github/workflows/ci.yml, .gitignore, plus the skill payload (SKILL.md, agents/, scripts/, tests/).

## Step 2 — README

First screen within 15 lines: name, one-line value proposition, badges, quick start. Both languages stay in sync.

## Step 3 — Quality gate

```bash
python scripts/check_repo_ready.py .
```

All checks PASS, including a clean git state and a credential scan of the whole tree.

## Step 4 — Commits and version

Conventional Commits, then `git tag v0.1.0`.

## Step 5 — Push and release

```bash
git push -u origin main
git push --tags
```

Then a GitHub Release for v0.1.0 with notes mirroring CHANGELOG.md.

## Step 6 — Visibility

Repository Description (one sentence with keywords), 5-8 Topics, and a post-push verification pass: README rendering, badge links, CI status, Release notes, and a final credential scan.