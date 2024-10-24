from typing import List

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


def encode_categorical_cols(
    df: pd.DataFrame, categorical_cols: List[str] = None
) -> pd.DataFrame:
    if categorical_cols is None:
        categorical_cols = ["Sex"]
    le = LabelEncoder()
    for col in categorical_cols:
        df[col] = le.fit_transform(df[col])
    return df


def extract_x_y(df: pd.DataFrame, categorical_cols: List[str] = None) -> pd.DataFrame:
    df = encode_categorical_cols(df)
    X, y = df.drop("Rings", axis=1), df["Rings"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=1024
    )
    return X_train, X_test, y_train, y_test
