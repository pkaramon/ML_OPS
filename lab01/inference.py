import joblib
from sklearn.ensemble import RandomForestClassifier

from constants import MODEL_PATH

CLASS_NAMES = ["setosa", "versicolor", "virginica"]


def load_model() -> RandomForestClassifier:
    return joblib.load(MODEL_PATH)


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
