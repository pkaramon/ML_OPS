from pathlib import Path

import joblib
from sentence_transformers import SentenceTransformer
from sklearn.linear_model import LogisticRegression

CLASSIFIER_PATH = Path("./model/classifier.joblib")
TRANSFORMER_PATH = Path("./model/sentence_transformer.model")


def load_classifier() -> LogisticRegression:
    try:
        return joblib.load(CLASSIFIER_PATH)
    except OSError as e:
        raise ValueError("Could not load the classifier model") from e


def load_transformer() -> SentenceTransformer:
    return SentenceTransformer(str(TRANSFORMER_PATH))


CLASS_NAMES = ["negative", "neutral", "positive"]


class Predictor:
    def __init__(self) -> None:
        self.classifier = load_classifier()
        self.transformer = load_transformer()

    def predict(self, text: str) -> str:
        embedding = self.transformer.encode(text)
        sentiment_idx = self.classifier.predict([embedding])[0]
        return CLASS_NAMES[int(sentiment_idx)]
