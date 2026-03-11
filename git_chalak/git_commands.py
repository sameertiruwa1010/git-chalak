import subprocess
import sys


def run(cmd: list[str]) -> int:
    """Run a shell command, stream output, return exit code."""
    result = subprocess.run(cmd)
    return result.returncode


def get_current_branch() -> str:
    """Return the current branch name."""
    result = subprocess.run(
        ["git", "branch", "--show-current"],
        capture_output=True,
        text=True
    )
    return result.stdout.strip()


def has_upstream() -> bool:
    """Check if current branch has a remote upstream set."""
    result = subprocess.run(
        ["git", "rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{u}"],
        capture_output=True,
        text=True
    )
    return result.returncode == 0


def git_add() -> int:
    print("📦 Staging all changes...")
    return run(["git", "add", "."])


def git_commit(message: str) -> int:
    print(f'💬 Committing with message: "{message}"')
    return run(["git", "commit", "-m", message])


def git_push() -> int:
    print("🚀 Pushing to remote...")

    if has_upstream():
        # Normal push — upstream already set
        return run(["git", "push"])
    else:
        # First push — set upstream automatically
        branch = get_current_branch()
        print(f"   Setting upstream: origin/{branch}")
        return run(["git", "push", "--set-upstream", "origin", branch])


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
