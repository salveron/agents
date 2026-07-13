#!/usr/bin/env python3
"""Make this repo's agents, skills, and rosters visible to Claude Code.

Symlinks every ``agents/*.agent.md`` file, every ``skills/<name>/`` directory, and the
``rosters/`` directory into a Claude Code config directory (``~/.claude`` by default, so
they are visible from every project on this machine) and imports ``AGENTS.md`` into that
directory's ``CLAUDE.md``. Safe to re-run any time (e.g. after a new agent or skill is
added).
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from _linking import (
    STATUS_WIDTH,
    ImportLineEnsurer,
    RepoContents,
    SymlinkInstaller,
    SymlinkSpec,
    install_and_report,
)

REPO_ROOT = Path(__file__).resolve().parent.parent


def parse_args() -> argparse.Namespace:
    """Parse the optional target Claude Code config directory.

    :returns: The parsed arguments, with ``claude_dir`` defaulting to ``~/.claude``.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "claude_dir",
        nargs="?",
        type=Path,
        default=Path.home() / ".claude",
        help="Claude Code config directory to link into (default: ~/.claude)",
    )
    return parser.parse_args()


def main() -> None:
    """Run the idempotent Claude Code linking steps and print a summary."""
    claude_dir = parse_args().claude_dir
    contents = RepoContents(root=REPO_ROOT)
    installer = SymlinkInstaller()

    specs = (
        [
            SymlinkSpec(source=path, target=claude_dir / "agents" / path.name)
            for path in contents.agent_files
        ]
        + [
            SymlinkSpec(source=path, target=claude_dir / "skills" / path.name)
            for path in contents.skill_dirs
        ]
        + [SymlinkSpec(source=contents.rosters_dir, target=claude_dir / "rosters")]
    )
    all_succeeded = install_and_report(installer, specs)

    agents_md = REPO_ROOT / "AGENTS.md"
    claude_md = claude_dir / "CLAUDE.md"
    status = ImportLineEnsurer().ensure(claude_md, f"@{agents_md}")
    print(f"{status.value:<{STATUS_WIDTH}} {claude_md} imports {agents_md}")

    print(f"\nDone. Restart Claude Code if {claude_dir} did not exist before.")
    sys.exit(0 if all_succeeded else 1)


if __name__ == "__main__":
    main()
