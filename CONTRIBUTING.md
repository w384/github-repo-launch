# Contributing

Thanks for helping improve github-repo-launch.

## Getting started

1. Fork the repository and clone it.
2. Install the skill into your Codex skills directory (see [README](README.md)).
3. Create a feature branch and make your changes.

## Development

The quality gate is Python 3.9+ and uses only the standard library.

Run the checks locally:

```bash
python scripts/check_repo_ready.py .        # quality gate
python -m unittest discover -s tests -v     # unit tests
```

## What to change

- `SKILL.md` — skill behavior and the six-phase workflow.
- `scripts/check_repo_ready.py` — quality gate logic and CLI.
- `assets/` / `references/` — templates and guidance.
- `README.md` / `README.zh-CN.md` / `docs/` — user-facing documentation; keep both languages in sync.
- `tests/` — add cases for any new check.

## Pull requests

- Keep commits small and descriptive.
- Update `CHANGELOG.md` under `[Unreleased]`.
- Ensure all checks above pass on Linux and Windows.
- Never commit credentials, real personal data in samples, or large binaries.

## License

By contributing, you agree that your contributions are licensed under the [MIT License](LICENSE).