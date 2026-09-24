from automated_documentation_sync.features import FEATURES
from automated_documentation_sync.sync import sync_readme


def test_sync_readme_writes_current_features_to_generated_section(tmp_path):
    readme_path = tmp_path / "README.md"
    readme_path.write_text(
        "# Project\n\n"
        "## Features\n\n"
        "<!-- AUTO-GENERATED-FEATURES:START -->\n"
        "- Old feature\n"
        "<!-- AUTO-GENERATED-FEATURES:END -->\n\n"
        "## Usage\n\n"
        "Run the app.\n",
        encoding="utf-8",
    )

    result = sync_readme(readme_path)

    assert "## Features" in result
    assert "<!-- AUTO-GENERATED-FEATURES:START -->" in result
    assert "<!-- AUTO-GENERATED-FEATURES:END -->" in result
    assert "- Addition" in result
    assert "- Subtraction" in result
    assert "- Multiplication" in result
    assert "- Division" in result
    assert "- Old feature" not in result
    assert "## Usage" in result
    assert "Run the app." in result


def test_sync_readme_preserves_existing_readme_content(tmp_path):
    readme_path = tmp_path / "README.md"
    readme_path.write_text(
        "# Sample Project\n\n"
        "This is an existing README.\n\n"
        "## Notes\n\n"
        "Keep this text.\n",
        encoding="utf-8",
    )

    result = sync_readme(readme_path)

    assert "# Sample Project" in result
    assert "This is an existing README." in result
    assert "## Notes" in result
    assert "Keep this text." in result

    for feature in FEATURES:
        assert f"- {feature}" in result