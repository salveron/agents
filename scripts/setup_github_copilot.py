#!/usr/bin/env python3
"""Make this repo's agents, skills, and rosters visible to GitHub Copilot in a project.

Symlinks every ``agents/*.agent.md`` file and every ``skills/<name>/`` directory, plus
``AGENTS.md`` and the ``rosters/`` directory it links into, into a target project's
``.github/`` directory. GitHub Copilot has no known machine-wide config directory, so
this must be pointed at each project that should see this repo's roster. Safe to re-run
any time.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from _linking import (
    RepoContents,
    SymlinkInstaller,
    SymlinkSpec,
    install_and_report,
)

REPO_ROOT = Path(__file__).resolve().parent.parent


def parse_args() -> argparse.Namespace:
    """Parse the required target project root.

    :returns: The parsed arguments, with ``project_root`` pointing at the project whose
        ``.github/`` directory should see this roster.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "project_root",
        type=Path,
        help="Root of the project whose .github/ directory should see this roster "
        "(use '.' for this repo itself)",
    )
    return parser.parse_args()


def main() -> None:
    """Run the idempotent GitHub Copilot linking steps and print a summary."""
    github_dir = parse_args().project_root / ".github"
    contents = RepoContents(root=REPO_ROOT)
    installer = SymlinkInstaller()

    specs = (
        [
            SymlinkSpec(source=path, target=github_dir / "agents" / path.name)
            for path in contents.agent_files
        ]
        + [
            SymlinkSpec(source=path, target=github_dir / "skills" / path.name)
            for path in contents.skill_dirs
        ]
        + [
            SymlinkSpec(source=REPO_ROOT / "AGENTS.md", target=github_dir / "AGENTS.md"),
            SymlinkSpec(source=contents.rosters_dir, target=github_dir / "rosters"),
        ]
    )
    sys.exit(0 if install_and_report(installer, specs) else 1)


if __name__ == "__main__":
    main()
