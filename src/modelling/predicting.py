import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.metrics import root_mean_squared_error

def predict_age(input_data: np.ndarray, pipeline: Pipeline):
    return pipeline.predict(input_data)

def evaluate_model(y_pred: np.ndarray, y_test: np.ndarray):
    return root_mean_squared_error(y_test, y_pred)
