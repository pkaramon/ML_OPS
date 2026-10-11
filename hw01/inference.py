from pathlib import Path

import joblib
from cleantext import clean
from sentence_transformers import SentenceTransformer
from sklearn.linear_model import LogisticRegression

MODEL_DIR = Path(__file__).parent / "model"
CLASSIFIER_PATH = MODEL_DIR / "classifier.joblib"
TRANSFORMER_PATH = MODEL_DIR / "sentence_transformer.model"
CLASS_NAMES = ["negative", "neutral", "positive"]


def load_classifier() -> LogisticRegression:
    return joblib.load(CLASSIFIER_PATH)


def load_transformer() -> SentenceTransformer:
    return SentenceTransformer(str(TRANSFORMER_PATH))


class Predictor:
    def __init__(self) -> None:
        self.classifier = load_classifier()
        self.transformer = load_transformer()

    def predict(self, text: str) -> str:
        embedding = self.transformer.encode(clean(text))
        sentiment_idx = self.classifier.predict([embedding])[0]
        return CLASS_NAMES[int(sentiment_idx)]
