# Code with FastAPI (app = FastAPI(...))
from app_config import APP_DESCRIPTION, APP_TITLE, PATH_TO_MODEL
from fastapi import FastAPI
from lib.inference import run_inference
from lib.models import PredictionInput, PredictionOutput
from utils import load_project

app = FastAPI(title=APP_TITLE, description=APP_DESCRIPTION)


@app.get("/")
def home() -> dict:
    return {"health_check": "App up and running!"}


@app.post("/predict", response_model=PredictionOutput, status_code=201)
def predict(payload: PredictionInput) -> dict:
    model = load_project(PATH_TO_MODEL)
    y = run_inference([payload], model)
    return {"prediction": y}
