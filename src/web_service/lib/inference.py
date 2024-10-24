import numpy as np
import pandas as pd
from lib.models import PredictionInput
from lib.preprocessing import encode_categorical_cols
from loguru import logger
from sklearn.base import BaseEstimator


def preprocess_input(input_data: list[PredictionInput]) -> list[dict]:
    processed_data = []
    for data in input_data:
        processed_data.append(
            {
                "Sex": data.Sex,
                "Length": data.Length,
                "Diameter": data.Diameter,
                "Height": data.Height,
                "Whole weight": data.Whole_weight,
                "Shucked weight": data.Shucked_weight,
                "Viscera weight": data.Viscera_weight,
                "Shell weight": data.Shell_weight,
            }
        )
    return processed_data


def run_inference(
    input_data: list[PredictionInput], model: BaseEstimator
) -> np.ndarray:
    input_data = preprocess_input(input_data)
    df = pd.DataFrame(input_data)
    df = encode_categorical_cols(df)
    # Running inference
    y = model.predict(df)
    logger.info(f"Predicted the age of abalone:\n{y}")
    print(y)
    return y
