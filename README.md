# git-chalak

> *chalak (चालाक) — clever, smart, sharp*

[![PyPI version](https://img.shields.io/pypi/v/git-chalak.svg)](https://pypi.org/project/git-chalak/)
[![Python](https://img.shields.io/pypi/pyversions/git-chalak.svg)](https://pypi.org/project/git-chalak/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

Stop typing three commands every time you push code. **git-chalak** collapses your entire Git workflow into short, memorable commands — built for developers who push code multiple times a day.

```bash
# Instead of this every single time:
git add .
git commit -m "fix login bug"
git push

# Just type this:
gc acp "fix login bug"
```

---

## Preview

```
$ gc acp "add dark mode support"

📦 Staging all changes...
💬 Committing with message: "add dark mode support"
🚀 Pushing to remote...
✅ Done!
```

---

## Available Commands

Both `git-chalak` and `gc` work identically.

| Command | What it does |
|---|---|
| `gc st` | `git status` |
| `gc ac` | Stage all + commit with default message `"update"` |
| `gc ac "message"` | Stage all + commit with your message |
| `gc acp` | Stage all + commit + push |
| `gc acp "message"` | Stage all + commit with your message + push |
| `gc p` | `git push` |
| `gc pl` | `git pull` |
| `gc lg` | `git log --oneline` |

---

## Installation

### ⚡ Recommended — pipx

```bash
pipx install git-chalak
```

> Don't have pipx? Install it first:
> ```bash
> sudo apt install pipx && pipx ensurepath   # Ubuntu/Debian
> brew install pipx && pipx ensurepath        # macOS
> ```

### pip

```bash
pip install git-chalak
```

### From source

```bash
git clone https://github.com/sameertiruwa/git-chalak
cd git-chalak
pip install -e .
```

---

## Usage

```bash
# Check what changed
gc st

# Quick save with default message
gc ac

# Commit with a real message
gc ac "fix null pointer in login"

# Full workflow — add, commit, push in one shot
gc acp "add authentication API"

# Pull latest changes before starting work
gc pl

# Review recent commits
gc lg
```

---

## Features

- **Two aliases** — use `git-chalak` or the short `gc`, both work the same
- **Default commit message** — `gc ac` without a message commits as `"update"`, great for quick saves
- **Fail-safe** — if any step fails (e.g. push is rejected), the chain stops immediately and reports the error
- **Zero config** — install and use, no setup required
- **Lightweight** — single dependency (`click`), no background processes

---

## Contributing

Contributions are welcome! Here's how:

```bash
# 1. Fork the repo on GitHub, then clone your fork
git clone https://github.com/sameertiruwa/git-chalak.git

# 2. Create a feature branch
git checkout -b feature/your-feature-name

# 3. Make your changes, then commit
git add .
git commit -m "feat: describe your change"

# 4. Push and open a Pull Request
git push origin feature/your-feature-name
```

**Ideas for contributions:**
- `gc undo` — soft reset the last commit
- `gc nb "branch-name"` — create and switch to a new branch
- `gc acpa "message"` — add + commit + push + open PR via GitHub CLI
- `gc init` — initialize a repo with a sensible `.gitignore`

---

## Requirements

- Python 3.9+
- Git installed and available in `PATH`

---

## License

[MIT](./LICENSE) — free to use, fork, and modify.

---

## Author

**Sameer Tiruwa**
- GitHub: [@sameertiruwa](https://github.com/sameertiruwa)
- Email: sameertiruwa1010@gmail.com
- Website: sameertiruwa.online

---

> *"Ek palta install gara, Git workflow fast huncha."* 🇳🇵
> *(Install it once, your Git workflow becomes fast forever.)*
