import click
from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("git-chalak")
except PackageNotFoundError:
    __version__ = "1.0.1"

from git_chalak.git_commands import (
    abort,
    git_add,
    git_commit,
    git_log,
    git_pull,
    git_push,
    git_status,
)

DEFAULT_MSG = "update"

BANNER = f"""
 ██████╗ ██╗████████╗      ██████╗██╗  ██╗ █████╗ ██╗      █████╗ ██╗  ██╗
██╔════╝ ██║╚══██╔══╝     ██╔════╝██║  ██║██╔══██╗██║     ██╔══██╗██║ ██╔╝
██║  ███╗██║   ██║   █████╗██║     ███████║███████║██║     ███████║█████╔╝ 
██║   ██║██║   ██║   ╚════╝██║     ██╔══██║██╔══██║██║     ██╔══██║██╔═██╗ 
╚██████╔╝██║   ██║         ╚██████╗██║  ██║██║  ██║███████╗██║  ██║██║  ██╗
 ╚═════╝ ╚═╝   ╚═╝          ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝
                                                               v{__version__}
"""


@click.group(invoke_without_command=True)
@click.version_option(__version__, "-v", "--version", message="git-chalak v%(version)s")
@click.pass_context
def cli(ctx):
    """⚡ git-chalak — Supercharge your Git workflow.

    \b
    COMMANDS:
      st           git status
      ac  [msg]    add + commit
      acp [msg]    add + commit + push
      p            git push
      pl           git pull
      lg           git log --oneline

    \b
    EXAMPLES:
      git-chalak acp "fix login bug"
      gc st
      gc lg
    """
    if ctx.invoked_subcommand is None:
        click.echo(BANNER)
        click.echo(ctx.get_help())


@cli.command()
def st():
    """Show git status."""
    abort(git_status())


@cli.command()
@click.argument("message", default=DEFAULT_MSG, required=False)
def ac(message):
    """Add all changes and commit.

    \b
    USAGE:
      git-chalak ac              # commits with "update"
      git-chalak ac "my message" # commits with custom message
    """
    abort(git_add())
    abort(git_commit(message))
    click.echo("✅ Done!")


@cli.command()
@click.argument("message", default=DEFAULT_MSG, required=False)
def acp(message):
    """Add all changes, commit, and push.

    \b
    USAGE:
      git-chalak acp              # add, commit "update", push
      git-chalak acp "my message" # add, commit with message, push
    """
    abort(git_add())
    abort(git_commit(message))
    abort(git_push())
    click.echo("✅ Done!")


@cli.command()
def p():
    """Push current branch to remote."""
    abort(git_push())
    click.echo("✅ Done!")


@cli.command()
def pl():
    """Pull latest changes from remote."""
    abort(git_pull())
    click.echo("✅ Done!")


@cli.command()
def lg():
    """Show compact git log (--oneline)."""
    abort(git_log())
