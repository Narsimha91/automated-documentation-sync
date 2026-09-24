"""Simple sync logic for keeping the generated README features block in sync."""

from __future__ import annotations

from pathlib import Path

from .features import FEATURES
from .readme_updater import update_readme_features


def sync_readme(readme_path: str | Path | None = None) -> str:
    """Update the repo README using the current feature list.

    By default this resolves the repository README from the project root. It is kept
    easy to test by allowing callers to pass a custom README path.
    """
    if readme_path is None:
        readme_path = Path(__file__).resolve().parents[2] / "README.md"

    return update_readme_features(readme_path, FEATURES)
