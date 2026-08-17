#!/usr/bin/env python3
"""Pre-publish quality gate for an open-source GitHub repository.

Usage: python check_repo_ready.py <repo-dir>
Exit: 0 = no FAIL; 1 = at least one FAIL (WARN items are advisory).
Zero third-party dependencies (stdlib only).
"""
import os
import re
import subprocess
import sys

# Credential-shaped patterns. Deliberately strict to avoid false positives
# on ordinary words (e.g. "task-" must not match an "sk-" key prefix).
SECRET_PATTERNS = [
    re.compile(r"api[_-]?key\s*=\s*\S+", re.IGNORECASE),
    re.compile(r"password\s*=\s*\S+", re.IGNORECASE),
    re.compile(r"passwd\s*=\s*\S+", re.IGNORECASE),
    re.compile(r"secret\s*=\s*\S+", re.IGNORECASE),
    re.compile(r"access[_-]?token\s*=\s*\S+", re.IGNORECASE),
    re.compile(r"BEGIN [A-Z0-9 ]*PRIVATE KEY", re.IGNORECASE),
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"ghp_[A-Za-z0-9]{20,}"),
    re.compile(r"\bsk-[A-Za-z0-9]{20,}"),
]
SKIP_DIRS = {".git", "node_modules", ".venv", "__pycache__", "dist", "build"}
SKIP_BIN_EXT = {".pyc", ".png", ".jpg", ".jpeg", ".gif", ".pdf", ".docx", ".xlsx", ".aep", ".zip", ".ico", ".woff", ".woff2"}


def walk_files(repo):
    for dirpath, dirnames, filenames in os.walk(repo):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            yield os.path.join(dirpath, fn)


def check_required(repo):
    required = ["README.md", "LICENSE", ".gitignore"]
    out = []
    for name in required:
        ok = os.path.isfile(os.path.join(repo, name))
        out.append((ok, "PASS" if ok else "FAIL", "required file " + name))
    return out


def check_secrets(repo):
    hits = []
    for fp in walk_files(repo):
        if os.path.splitext(fp)[1].lower() in SKIP_BIN_EXT:
            continue
        try:
            with open(fp, "r", encoding="utf-8", errors="ignore") as fh:
                content = fh.read()
        except Exception:
            continue
        if any(p.search(content) for p in SECRET_PATTERNS):
            hits.append(os.path.relpath(fp, repo))
    if hits:
        return (False, "FAIL", "credential-like pattern in: " + ", ".join(hits[:5]))
    return (True, "PASS", "no credential-like patterns")


def check_large_files(repo, limit=50 * 1024 * 1024):
    big = []
    for fp in walk_files(repo):
        try:
            if os.path.getsize(fp) > limit:
                big.append(os.path.relpath(fp, repo))
        except OSError:
            pass
    if big:
        return (False, "FAIL", "files >50MB (use Git LFS or Release): " + ", ".join(big[:5]))
    return (True, "PASS", "no files >50MB")


def check_versions(repo):
    versions = []
    pyproject = os.path.join(repo, "pyproject.toml")
    if os.path.isfile(pyproject):
        m = re.search(r"^version\s*=\s*[\x22\x27]([^\x22\x27]+)[\x22\x27]", open(pyproject, encoding="utf-8").read(), re.M)
        if m:
            versions.append(("pyproject", m.group(1)))
    pkg = os.path.join(repo, "package.json")
    if os.path.isfile(pkg):
        m = re.search(r"\"version\"\s*:\s*\"([^\"]+)\"", open(pkg, encoding="utf-8").read())
        if m:
            versions.append(("package.json", m.group(1)))
    if len(versions) >= 2:
        if len(set(v for _, v in versions)) > 1:
            return (False, "FAIL", "version mismatch: " + ", ".join(k + "=" + v for k, v in versions))
        return (True, "PASS", "versions consistent: " + versions[0][1])
    if versions:
        return (True, "PASS", "single version manifest: " + versions[0][0] + "=" + versions[0][1])
    return (True, "WARN", "no version manifests found (pyproject.toml / package.json)")


def check_git(repo):
    try:
        out = subprocess.run(["git", "-C", repo, "status", "--porcelain"], capture_output=True, text=True, timeout=10)
        dirty = [ln for ln in out.stdout.splitlines() if ln.strip()]
        if dirty:
            return (False, "WARN", "git working tree not clean (" + str(len(dirty)) + " entries)")
        return (True, "PASS", "git working tree clean")
    except Exception as exc:
        return (True, "WARN", "cannot run git status: " + str(exc))


def main():
    repo = sys.argv[1] if len(sys.argv) > 1 else "."
    checks = []
    checks += check_required(repo)
    checks.append(check_secrets(repo))
    checks.append(check_large_files(repo))
    checks.append(check_versions(repo))
    checks.append(check_git(repo))
    failed = False
    for ok, status, msg in checks:
        print("[" + status + "] " + msg)
        if status == "FAIL":
            failed = True
    print("RESULT: " + ("FAIL" if failed else "PASS (review WARN items)"))
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()