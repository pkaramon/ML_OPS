import pytest

from inference import CLASS_NAMES, Predictor, load_classifier


def test_classifier_loads() -> None:
    classifier = load_classifier()
    assert list(classifier.classes_) == [0, 1, 2]


@pytest.mark.parametrize(
    "text",
    [
        "What a great MLOps lecture, I am very satisfied",
        "This is the worst service I have ever experienced",
        "The train leaves at 10 am",
    ],
)
def test_predict_sample_texts(predictor: Predictor, text: str) -> None:
    assert predictor.predict(text) in CLASS_NAMES
