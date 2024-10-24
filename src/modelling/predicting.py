import numpy as np
from sklearn.pipeline import Pipeline


def predict_age(input_data: np.ndarray, pipeline: Pipeline):
    return pipeline.predict(input_data)


def evaluate_model(y_test, y_pred):
    mse = np.mean((y_test - y_pred) ** 2)
    rmse = np.sqrt(mse)
    return rmse
