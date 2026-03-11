# git-chalak

> *chalak (चालाक) — clever, smart, sharp*

A minimal CLI tool that wraps common Git workflows into short, memorable commands. Built for developers who push code multiple times a day.

[![PyPI version](https://img.shields.io/pypi/v/git-chalak.svg)](https://pypi.org/project/git-chalak/)
[![Python](https://img.shields.io/pypi/pyversions/git-chalak.svg)](https://pypi.org/project/git-chalak/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## Installation

```bash
pipx install git-chalak
```

> Requires [pipx](https://pipx.pypa.io). Install it with `sudo apt install pipx` or `brew install pipx`.

---

## Commands

Both `git-chalak` and `gc` work identically.

| Command | Runs |
|---|---|
| `gc st` | `git status` |
| `gc ac` | `git add . && git commit -m "update"` |
| `gc ac "message"` | `git add . && git commit -m "message"` |
| `gc acp` | `git add . && git commit -m "update" && git push` |
| `gc acp "message"` | `git add . && git commit -m "message" && git push` |
| `gc p` | `git push` |
| `gc pl` | `git pull` |
| `gc lg` | `git log --oneline` |

---

## Usage

```bash
# Check what changed
gc st

# Stage and commit
gc ac "fix null pointer in login"

# Stage, commit, and push in one shot
gc acp "add dark mode support"

# Pull latest, then push your changes
gc pl
gc p

# Review recent commits
gc lg
```

---

## Requirements

- Python 3.9+
- Git installed and available in `PATH`

---

## License

MIT © 2026 [Sameer Tiruwa](https://github.com/sameertiruwa)
