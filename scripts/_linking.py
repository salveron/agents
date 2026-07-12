"""Shared helpers for idempotently wiring this repo's content into a tool's config."""

from __future__ import annotations

import enum
from dataclasses import dataclass
from pathlib import Path


class LinkStatus(enum.Enum):
    """Outcome of one idempotent linking action."""

    CREATED = "CREATED"
    ALREADY_PRESENT = "ALREADY PRESENT"
    SKIPPED_EXISTING = "SKIPPED (exists, not ours)"


@dataclass(frozen=True)
class SymlinkSpec:
    """A single symlink this repo wants to exist.

    :param source: The real file or directory this repo owns.
    :param target: The path where a tool expects to find it.
    """

    source: Path
    target: Path


class SymlinkInstaller:
    """Creates symlinks without ever touching content it doesn't own."""

    def install(self, spec: SymlinkSpec) -> LinkStatus:
        """Ensure ``spec.target`` is a symlink to ``spec.source``.

        The created link records an absolute source, so re-run after moving the repo to
        repair links that would otherwise dangle.

        :param spec: The source/target pair to link.
        :returns: The action taken, or that one was skipped to avoid clobbering
            unrelated content already at that path.
        :raises OSError: If the link cannot be created (e.g. a permissions problem, or a
            platform without symlink support).
        """
        if spec.target.is_symlink() and spec.target.resolve() == spec.source.resolve():
            return LinkStatus.ALREADY_PRESENT
        if spec.target.exists() or spec.target.is_symlink():
            return LinkStatus.SKIPPED_EXISTING
        spec.target.parent.mkdir(parents=True, exist_ok=True)
        spec.target.symlink_to(spec.source, target_is_directory=spec.source.is_dir())
        return LinkStatus.CREATED


class ImportLineEnsurer:
    """Appends a line to a Markdown file exactly once."""

    def ensure(self, file: Path, line: str) -> LinkStatus:
        """Ensure ``line`` is present in ``file``, appending it if missing.

        A leading newline is inserted when the existing content lacks a trailing one, so
        the line is never glued onto the file's last line.

        :param file: The Markdown file to update (created if it doesn't exist).
        :param line: The exact line to guarantee is present.
        :returns: Whether the line was just added or was already there.
        """
        file.parent.mkdir(parents=True, exist_ok=True)
        file.touch(exist_ok=True)
        content = file.read_text(encoding="utf-8")
        if line in content.splitlines():
            return LinkStatus.ALREADY_PRESENT
        separator = "\n" if content and not content.endswith("\n") else ""
        with file.open("a", encoding="utf-8") as handle:
            handle.write(f"{separator}{line}\n")
        return LinkStatus.CREATED


STATUS_WIDTH = max(len(status.value) for status in LinkStatus)


def install_and_report(installer: SymlinkInstaller, specs: list[SymlinkSpec]) -> bool:
    """Install every spec, printing one aligned status line each.

    :param installer: The installer to apply to each spec.
    :param specs: The symlinks to create.
    :returns: ``True`` if every spec succeeded; ``False`` if any raised an OS error
        (e.g. a permissions problem, or a platform without symlink support).
    """
    all_succeeded = True
    for spec in specs:
        try:
            status = installer.install(spec)
        except OSError as error:
            all_succeeded = False
            print(f"{'FAILED':<{STATUS_WIDTH}} {spec.target}: {error}")
            continue
        print(f"{status.value:<{STATUS_WIDTH}} {spec.target} -> {spec.source}")
    return all_succeeded


@dataclass(frozen=True)
class RepoContents:
    """Enumerates this repo's linkable content.

    :param root: The agents repo's root directory.
    """

    root: Path

    @property
    def agent_files(self) -> list[Path]:
        """Every ``agents/*.agent.md`` file, sorted by name."""
        return sorted((self.root / "agents").glob("*.agent.md"))

    @property
    def skill_dirs(self) -> list[Path]:
        """Every ``skills/<name>/`` directory, sorted by name."""
        return sorted(p for p in (self.root / "skills").iterdir() if p.is_dir())
