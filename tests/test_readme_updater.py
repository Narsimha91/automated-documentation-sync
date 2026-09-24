from pathlib import Path
import pytest

from automated_documentation_sync.readme_updater import build_features_block, update_readme_features


def test_build_features_block_creates_marked_section():
    block = build_features_block(["One", "Two"])

    assert "<!-- AUTO-GENERATED-FEATURES:START -->" in block
    assert "- One" in block
    assert "- Two" in block
    assert "<!-- AUTO-GENERATED-FEATURES:END -->" in block


def test_update_readme_features_replaces_existing_block(tmp_path):
    readme_path = tmp_path / "README.md"
    readme_path.write_text(
        "# Project\n\n"
        "## Features\n\n"
        "<!-- AUTO-GENERATED-FEATURES:START -->\n"
        "- old\n"
        "<!-- AUTO-GENERATED-FEATURES:END -->\n\n"
        "## Usage\n\n"
        "Run the app.\n",
        encoding="utf-8",
    )

    result = update_readme_features(readme_path, ["New feature", "Another feature"])

    assert "- old" not in result
    assert "- New feature" in result
    assert "- Another feature" in result
    assert "## Usage" in result
    assert result.count("<!-- AUTO-GENERATED-FEATURES:START -->") == 1


def test_update_readme_features_appends_block_if_missing(tmp_path):
    readme_path = tmp_path / "README.md"
    readme_path.write_text("# Project\n\nThis is a sample README.\n", encoding="utf-8")

    result = update_readme_features(readme_path, ["Feature A"])

    assert "# Project" in result
    assert "This is a sample README." in result
    assert "<!-- AUTO-GENERATED-FEATURES:START -->" in result
    assert "- Feature A" in result

def test_update_readme_features_raises_when_only_start_marker_exists(tmp_path):
    readme_path = tmp_path / "README.md"
    readme_path.write_text(
        "# Project\n\n"
        "<!-- AUTO-GENERATED-FEATURES:START -->\n"
        "- Old feature\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="only one"):
        update_readme_features(readme_path, ["New feature"])


def test_update_readme_features_does_not_duplicate_markers(tmp_path):
    readme_path = tmp_path / "README.md"
    readme_path.write_text(
        "# Project\n\n"
        "<!-- AUTO-GENERATED-FEATURES:START -->\n"
        "- Old feature\n"
        "<!-- AUTO-GENERATED-FEATURES:END -->\n",
        encoding="utf-8",
    )

    update_readme_features(readme_path, ["New feature"])
    result = update_readme_features(readme_path, ["Latest feature"])

    assert result.count("<!-- AUTO-GENERATED-FEATURES:START -->") == 1
    assert result.count("<!-- AUTO-GENERATED-FEATURES:END -->") == 1
    assert "- Old feature" not in result
    assert "- New feature" not in result
    assert "- Latest feature" in result