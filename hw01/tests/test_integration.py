from fastapi.testclient import TestClient

from app import app


def test_predict_end_to_end() -> None:
    with TestClient(app) as client:
        response = client.post(
            "/predict",
            json={"text": "What a great MLOps lecture, I am very satisfied"},
        )

    assert response.status_code == 200
    assert response.json() == {"prediction": "positive"}
