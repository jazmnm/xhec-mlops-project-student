import numpy as np
import pandas as pd
from loguru import logger
from lib.models import PredictionInput
from lib.preprocessing import encode_categorical_cols
from sklearn.base import BaseEstimator

def preprocess_input(input_data: list[PredictionInput]) -> list[dict]:
    processed_data = []
    for data in input_data:
        processed_data.append({
            "Sex": data.Sex,
            "Length": data.Length,
            "Diameter": data.Diameter,
            "Height": data.Height,
            "Whole weight": data.Whole_weight,
            "Shucked weight": data.Shucked_weight,
            "Viscera weight": data.Viscera_weight,
            "Shell weight": data.Shell_weight
        })
    return processed_data

def run_inference(input_data: list[PredictionInput], model: BaseEstimator) -> np.ndarray:
    # No need to call .dict() as input_data is already a list of dicts after preprocessing
    df = pd.DataFrame(input_data)
    print(df.columns)
    df = encode_categorical_cols(df)
    # Running inference
    y = model.predict(df)

    logger.info(f"Predicted the age of abalone:\n{y}")
    return y
