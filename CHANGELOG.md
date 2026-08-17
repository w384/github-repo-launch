# Changelog

All notable changes to this project are documented in this file.

The format follows the spirit of [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and version numbers follow [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

- No unreleased changes yet.

## [0.1.0] - 2026-08-18

### Added

- Initial GitHub Repo Launch Codex skill: six-phase workflow (baseline, skeleton, README, quality gate, commits and version, push and release, visibility and verification).
- Dependency-free quality gate CLI `scripts/check_repo_ready.py` (Python stdlib only) with regex-based credential scanning that avoids false positives on ordinary words.
- Reusable templates in `assets/` (bilingual README, MIT license, .gitignore) and guidance in `references/` (README template, badges and repository settings).
- GitHub Actions CI: quality-gate self-check and unit tests on Linux and Windows (Python 3.9 / 3.12).
- Unit test suite for the quality gate (stdlib unittest).
- Bilingual README (English / 中文), design notes, demo walkthrough, contributing and security docs.

[Unreleased]: https://github.com/w384/github-repo-launch/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/w384/github-repo-launch/releases/tag/v0.1.0