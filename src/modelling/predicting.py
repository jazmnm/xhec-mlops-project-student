import numpy as np
from sklearn.pipeline import Pipeline


def predict_age(input_data: np.ndarray, pipeline: Pipeline):

    return pipeline.predict(input_data)
