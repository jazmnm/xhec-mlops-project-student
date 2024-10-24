from typing import List

import pandas as pd
from prefect import task
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

CATEGORICAL_COLS = ["Sex"]


@task(
    name="encode_categorical_columns",
    description="Encodes categorical columns in the DataFrame",
    retries=2,
    retry_delay_seconds=30,
    tags=["preprocessing", "ml"],
    log_prints=True,
    timeout_seconds=300,
)
def encode_categorical_cols(
    df: pd.DataFrame, categorical_cols: List[str] = None
) -> pd.DataFrame:
    if categorical_cols is None:
        categorical_cols = ["Sex"]
    le = LabelEncoder()
    for col in categorical_cols:
        df[col] = le.fit_transform(df[col])
    return df


@task(
    name="extract_features_and_target",
    description="Extracts features and target variable for model training",
    retries=2,
    retry_delay_seconds=30,
    tags=["data_split", "ml"],
    log_prints=True,
    timeout_seconds=300,
)
def extract_x_y(df: pd.DataFrame, categorical_cols: List[str] = None) -> pd.DataFrame:
    df = encode_categorical_cols(df)
    X, y = df.drop("Rings", axis=1), df["Rings"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=1024
    )
    return X_train, X_test, y_train, y_test
