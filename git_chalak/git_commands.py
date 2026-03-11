import subprocess
import sys


def run(cmd: list[str]) -> int:
    """Run a shell command, stream output, return exit code."""
    result = subprocess.run(cmd)
    return result.returncode


def git_add() -> int:
    print("📦 Staging all changes...")
    return run(["git", "add", "."])


def git_commit(message: str) -> int:
    print(f'💬 Committing with message: "{message}"')
    return run(["git", "commit", "-m", message])


def git_push() -> int:
    print("🚀 Pushing to remote...")
    return run(["git", "push"])


def git_pull() -> int:
    print("⬇️  Pulling latest changes...")
    return run(["git", "pull"])


def git_status() -> int:
    return run(["git", "status"])


def git_log() -> int:
    return run(["git", "log", "--oneline"])


def abort(code: int):
    if code != 0:
        print("❌ Command failed. Aborting.", file=sys.stderr)
        sys.exit(code)
