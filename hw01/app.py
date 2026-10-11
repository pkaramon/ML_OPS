from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from typing import Annotated, TypedDict

from fastapi import Depends, FastAPI, Request

from api.models.sentiment import PredictRequest, PredictResponse
from inference import Predictor


class State(TypedDict):
    predictor: Predictor


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[State]:
    yield {"predictor": Predictor()}


def get_predictor(request: Request) -> Predictor:
    predictor: Predictor = request.state.predictor
    return predictor


app = FastAPI(lifespan=lifespan)


@app.post("/predict")
def predict(
    body: PredictRequest,
    predictor: Annotated[Predictor, Depends(get_predictor)],
) -> PredictResponse:
    return PredictResponse(prediction=predictor.predict(body.text))
