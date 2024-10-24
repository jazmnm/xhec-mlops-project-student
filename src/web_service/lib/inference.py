import numpy as np
import pandas as pd
from loguru import logger
from lib.models import PredictionInput
from lib.preprocessing import encode_categorical_cols
from sklearn.base import BaseEstimator


def run_inference(input_data: list[PredictionInput], model: BaseEstimator) -> np.ndarray:
    """
    Run inference on a list of input data.

    Args:
        input_data (np.ndarray): The input data (features) to run inference on.
        model (BaseEstimator): The fitted pipeline

    Returns:
        np.ndarray: The predicted age of the abalone.
    """
    logger.info(f"Running inference on:\n{input_data}")
    df = pd.DataFrame([x.dict() for x in input_data])

    df = encode_categorical_cols(df)
    y = model.predict(df)
    logger.info(f"Predicted the age of abalone:\n{y}")
    return y
