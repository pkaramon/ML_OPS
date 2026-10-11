import pytest

from inference import Predictor, load_classifier


def test_classifier_loads() -> None:
    classifier = load_classifier()
    assert list(classifier.classes_) == [0, 1, 2]


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("This is really great", "positive"),
        ("This is really bad", "negative"),
        ("It is Monday", "neutral"),
    ],
)
def test_predict_sample_texts(predictor: Predictor, text: str, expected: str) -> None:
    assert predictor.predict(text) == expected
