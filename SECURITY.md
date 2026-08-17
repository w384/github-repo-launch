# Security

## Reporting a vulnerability

Please do not open a public issue for security problems. Report privately via the repository Security tab, or contact the maintainer directly.

## Scope

- The quality gate (`scripts/check_repo_ready.py`) runs entirely offline: it reads files in a local directory and prints findings. It makes no network calls and uploads nothing.
- Before publishing, the gate scans the tree for common credential patterns, large files, and version inconsistencies. Passing the gate is a necessary but not sufficient condition for a safe release — always re-check the rendered repository after push.
- This skill never publishes anything by itself: creating a public repository requires explicit user authorization.