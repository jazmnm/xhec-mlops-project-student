# Code with FastAPI (app = FastAPI(...))
from app_config import (
    APP_DESCRIPTION,
    APP_TITLE,
    APP_VERSION,
    MODEL_VERSION,
    PATH_TO_MODEL
)

from fastapi import FastAPI

from lib.inference import run_inference
from lib.models import PredictionInput
from utils import load_project

# Other imports

app = FastAPI(title=APP_TITLE, description=APP_DESCRIPTION,version=APP_VERSION)


@app.get("/")
def home() -> dict:
    return {"health_check": "App up and running!","model_version": MODEL_VERSION}


@app.post("/predict", response_model=PredictionOutput, status_code=201)
def predict(payload: PredictionInput) -> dict:
    model = load_project(PATH_TO_MODEL)
    y = run_inference([payload], model)
    return {"albane_age_prediction": y[0]}
