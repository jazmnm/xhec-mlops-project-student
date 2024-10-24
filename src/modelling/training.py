import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def load_data(data_path: str) -> pd.DataFrame:
    return pd.read_csv(data_path)


def train_pipeline(X_train: np.ndarray, y_train: np.ndarray):
    pipeline = Pipeline(
        [("scaler", StandardScaler()), ("regressor", LinearRegression())]
    )

    pipeline.fit(X_train, y_train)
    return pipeline
