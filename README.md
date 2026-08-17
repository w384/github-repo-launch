# GitHub Repo Launch 🚀

Turn any local project — codebase, Codex skill, internal tool — into a polished, Star-friendly open-source GitHub repository and publish it: bilingual README, quality gates, semantic versioning, and release-ready settings in one repeatable workflow.

[简体中文](README.zh-CN.md)

![version](https://img.shields.io/badge/version-0.1.0-blue) ![license](https://img.shields.io/badge/license-MIT-green) ![python](https://img.shields.io/badge/python-3.9%2B-blue) ![CI](https://github.com/w384/github-repo-launch/actions/workflows/ci.yml/badge.svg)

## Why a launch workflow?

A good idea is not enough. Before a repository reaches GitHub it must look complete, run clean, and explain itself in the first 15 seconds — that is what earns trust, and trust is what earns Stars. This skill standardizes the process so every release looks intentional instead of improvised.

## Workflow

```text
0. Baseline       — name, license, version, positioning
1. Skeleton       — README, LICENSE, CHANGELOG, CONTRIBUTING, SECURITY, docs, CI
2. README         — Star-friendly first screen, bilingual
3. Quality gate   — scripts/check_repo_ready.py must PASS
4. Commits & tag  — Conventional Commits, v0.1.0
5. Push & release — push origin, GitHub Release with notes
6. Visibility     — Description, Topics, post-push verification
```

## Features

- Six-phase workflow from baseline to post-publish verification.
- Dependency-free quality gate (`scripts/check_repo_ready.py`, Python stdlib only): required files, credential scan, large-file check, version consistency, clean git state.
- Bilingual README guidance with copy-and-adapt templates in `assets/`.
- Honest by default: no claims without evidence; nothing is published without explicit authorization.
- Reference implementation: [thread-archive-restart](https://github.com/w384/thread-archive-restart).

## Quick Start

### As a Codex skill (recommended)

```bash
git clone https://github.com/w384/github-repo-launch "${CODEX_HOME:-$HOME/.codex}/skills/github-repo-launch"
```

Windows PowerShell:

```powershell
$codexHome = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME '.codex' }
git clone https://github.com/w384/github-repo-launch (Join-Path $codexHome 'skills\github-repo-launch')
```

Restart Codex — `SKILL.md` is auto-discovered. Then ask: *"Use github-repo-launch to publish this project as a polished open-source repository."*

### Quality gate on any repository

```bash
python scripts/check_repo_ready.py /path/to/repo
```

Exit code `0` means no FAIL; a `WARN` item is advisory.

## Documentation

- [Design](docs/design.md) — why and how the workflow works.
- [Demo](docs/demo.md) — worked example of publishing a Codex skill.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT](LICENSE)

## Acknowledgements

Thanks to everyone who makes this project possible.