import joblib
from numpy.typing import NDArray
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.utils import Bunch

from constants import MODEL_PATH, RANDOM_SEED


def load_data() -> tuple[NDArray, NDArray]:
    iris = load_iris()
    assert isinstance(iris, Bunch)
    return iris.data, iris.target


def train_model(X: NDArray, y: NDArray) -> RandomForestClassifier:
    model = RandomForestClassifier(n_estimators=10, random_state=RANDOM_SEED)
    model.fit(X, y)
    return model


def save_model(model: RandomForestClassifier):
    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL_PATH)


if __name__ == "__main__":
    data = load_data()
    print("Loaded the data")
    model = train_model(*data)
    print("Trained the model")
    save_model(model)
    print("Saved the model")
