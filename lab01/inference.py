import joblib
from sklearn.ensemble import RandomForestClassifier

from constants import MODEL_PATH


def load_model() -> RandomForestClassifier:
    try:
        return joblib.load(MODEL_PATH)
    except OSError as e:
        raise ValueError("Couldn't load the trained model") from e


CLASS_NAMES = ["setosa", "versicolor", "virginica"]


def predict(model: RandomForestClassifier, data: dict[str, float]) -> str:
    features = [
        [
            data["sepal_length"],
            data["sepal_width"],
            data["petal_length"],
            data["petal_width"],
        ]
    ]
    return CLASS_NAMES[int(model.predict(features)[0])]
