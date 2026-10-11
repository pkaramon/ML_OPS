from collections.abc import Iterator

import pytest
from fastapi.testclient import TestClient

from app import app, get_predictor
from inference import Predictor


class FakePredictor:
    def predict(self, text: str) -> str:
        return "positive"


@pytest.fixture(scope="session")
def predictor() -> Predictor:
    return Predictor()


@pytest.fixture
def client() -> Iterator[TestClient]:
    app.dependency_overrides[get_predictor] = FakePredictor
    yield TestClient(app)
    app.dependency_overrides.clear()
