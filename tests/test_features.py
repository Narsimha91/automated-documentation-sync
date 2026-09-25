from automated_documentation_sync.features import FEATURES


def test_features_list_is_available():
    assert isinstance(FEATURES, list)
    assert len(FEATURES) > 0


def test_features_contains_expected_capstone_features():
    assert FEATURES == ["Addition", "Subtraction", "Multiplication", "Division", "Processing"]
