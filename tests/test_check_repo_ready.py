import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "check_repo_ready.py"


def run_check(repo_dir):
    return subprocess.run(
        [sys.executable, str(SCRIPT), str(repo_dir)],
        capture_output=True,
        text=True,
    )


class CheckRepoReadyTests(unittest.TestCase):
    def test_repo_root_passes(self):
        proc = run_check(REPO)
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)

    def test_missing_required_file_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            proc = run_check(tmp)
            self.assertNotEqual(proc.returncode, 0)
            self.assertIn("required file README.md", proc.stdout)

    def test_credential_like_marker_fails(self):
        marker = "".join(["pass", "word=", "demo123"])
        with tempfile.TemporaryDirectory() as tmp:
            Path(tmp, "leak.txt").write_text(marker + "\n", encoding="utf-8")
            proc = run_check(tmp)
            self.assertNotEqual(proc.returncode, 0)
            self.assertIn("credential-like pattern", proc.stdout)

    def test_plain_words_are_not_flagged(self):
        # A key prefix must not match ordinary words such as "task-".
        with tempfile.TemporaryDirectory() as tmp:
            Path(tmp, "notes.txt").write_text("a task- and risky- word\n", encoding="utf-8")
            proc = run_check(tmp)
            self.assertEqual(proc.returncode, 0, proc.stdout)

    def test_large_file_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            Path(tmp, "README.md").write_text("# x\n", encoding="utf-8")
            Path(tmp, "LICENSE").write_text("MIT\n", encoding="utf-8")
            Path(tmp, ".gitignore").write_text("", encoding="utf-8")
            with open(Path(tmp, "big.bin"), "wb") as fh:
                fh.write(b"0" * (50 * 1024 * 1024 + 1))
            proc = run_check(tmp)
            self.assertNotEqual(proc.returncode, 0)
            self.assertIn(">50MB", proc.stdout)


if __name__ == "__main__":
    unittest.main()