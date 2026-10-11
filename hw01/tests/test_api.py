from typing import Any

import pytest
from fastapi.testclient import TestClient
from pydantic import ValidationError

from api.models.sentiment import PredictRequest


@pytest.mark.parametrize("text", ["", 123, None])
def test_request_requires_non_empty_string(text: Any) -> None:
    with pytest.raises(ValidationError):
        PredictRequest(text=text)


def test_predict_returns_valid_json(client: TestClient) -> None:
    response = client.post("/predict", json={"text": "I love this course"})

    assert response.status_code == 200
    assert response.json() == {"prediction": "positive"}


@pytest.mark.parametrize(
    "payload",
    [{"text": ""}, {"text": 123}, {}, {"txt": "hello"}],
)
def test_invalid_input_returns_error_json(
    client: TestClient, payload: dict[str, Any]
) -> None:
    response = client.post("/predict", json=payload)

    assert response.status_code == 422
    assert response.json()["detail"][0]["msg"]
