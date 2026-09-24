
from automated_documentation_sync.change_detector import (
    is_source_change,
    should_update_readme,
)


def test_python_file_counts_as_source_change():
    changed_files = ["src/app/service.py"]

    assert is_source_change(changed_files) is True
    assert should_update_readme(changed_files) is True


def test_javascript_file_counts_as_source_change():
    changed_files = ["src/app/service.js"]

    assert is_source_change(changed_files) is True


def test_readme_change_does_not_trigger_source_change():
    changed_files = ["README.md"]

    assert is_source_change(changed_files) is False
    assert should_update_readme(changed_files) is False


def test_docs_change_does_not_trigger_source_change():
    changed_files = ["docs/architecture.md"]

    assert is_source_change(changed_files) is False
    assert should_update_readme(changed_files) is False


def test_test_file_change_does_not_trigger_source_change():
    changed_files = ["tests/test_change_detector.py"]

    assert is_source_change(changed_files) is False
    assert should_update_readme(changed_files) is False


def test_github_workflow_change_does_not_trigger_source_change():
    changed_files = [".github/workflows/readme-update.yml"]

    assert is_source_change(changed_files) is False
    assert should_update_readme(changed_files) is False


def test_mixed_changes_trigger_source_change_when_source_exists():
    changed_files = [
        "README.md",
        "docs/architecture.md",
        "src/app/config.py",
    ]

    assert is_source_change(changed_files) is True
    assert should_update_readme(changed_files) is True


def test_empty_change_list_does_not_trigger_source_change():
    changed_files = []

    assert is_source_change(changed_files) is False
    assert should_update_readme(changed_files) is False

