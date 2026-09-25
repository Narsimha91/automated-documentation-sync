from automated_documentation_sync.features import FEATURES


def test_features_list_is_available():
    assert isinstance(FEATURES, list)
    assert len(FEATURES) > 0


def test_features_contains_expected_capstone_features():
    assert FEATURES == ["Addition", "Subtraction", "Multiplication", "Division", "Processing", "Feature 1", "Feature 2"]

def test_temporary_failure_for_ci_validation():
    assert False, "Intentional failure for GitHub Actions validation"