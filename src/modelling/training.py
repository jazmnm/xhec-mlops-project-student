import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def train_model(X_train: np.ndarray, y_train: np.ndarray):
    pipeline = Pipeline(
        [("scaler", StandardScaler()), ("regressor", LinearRegression())]
    )

    pipeline.fit(X_train, y_train)
    return pipeline
