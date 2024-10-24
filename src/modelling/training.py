import os
import mlflow
import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from typing import List

def train_model(
    X_train: np.ndarray, 
    y_train: np.ndarray
    ):

    pipeline = Pipeline(
        [("scaler", StandardScaler()), ("regressor", LinearRegression())]
    )

    pipeline.fit(X_train, y_train)
    return pipeline
