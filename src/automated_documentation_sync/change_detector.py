"""Utilities for identifying meaningful source changes."""

from __future__ import annotations

SOURCE_EXTENSIONS = {
    ".py",
    ".js",
    ".ts",
    ".tsx",
    ".java",
    ".cs",
    ".go",
    ".rb",
}

NON_SOURCE_PATHS = {
    "README.md",
    "requirements.md",
    ".github",
    "docs/",
    "docs",
}


def is_source_change(changed_files: list[str]) -> bool:
    """Return True when at least one changed file under src/ is source code."""
    if not changed_files:
        return False

    for item in changed_files:
        lowered = item.lower()

        if not lowered.startswith("src/"):
            continue

        if any(lowered.endswith(ext) for ext in SOURCE_EXTENSIONS):
            return True

    return False


def should_update_readme(changed_files: list[str]) -> bool:
    """Determine whether a source-related change should prompt README review."""
    return is_source_change(changed_files)
