import numpy as np
from loguru import logger
from sklearn.base import BaseEstimator


def run_inference(input_data: np.ndarray, model: BaseEstimator) -> np.ndarray:
    """
    Run inference on a list of input data.

    Args:
        input_data (np.ndarray): The input data (features) to run inference on.
        model (BaseEstimator): The fitted pipeline

    Returns:
        np.ndarray: The predicted age of the abalone.
    """
    logger.info(f"Running inference on:\n{input_data}")
    y = model.predict(input_data)
    logger.info(f"Predicted the age of abalone:\n{y}")
    return y
