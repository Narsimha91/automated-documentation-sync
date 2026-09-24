"""Automated documentation sync package."""

__all__ = ["is_source_change", "should_update_readme"]

from .change_detector import is_source_change, should_update_readme
