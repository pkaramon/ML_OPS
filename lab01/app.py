from fastapi import FastAPI

from api.models.iris import PredictResponse, PredictRequest
import inference


model = inference.load_model()

app = FastAPI()


@app.get("/")
def welcome_root():
    return {"message": "Welcome to the ML API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/predict")
def predict(body: PredictRequest) -> PredictResponse:
    prediction = inference.predict(model, body.model_dump())
    return PredictResponse(prediction=prediction)
