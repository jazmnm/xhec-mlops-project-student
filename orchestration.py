import os
from typing import Optional

import numpy as np
import pandas as pd
from loguru import logger
from prefect import flow, get_run_logger, task

from config import CATEGORICAL_COLS, DATA_DIRPATH, MODELS_DIRPATH
from src.modelling.predicting import evaluate_model, predict_age
from src.modelling.preprocessing import encode_categorical_cols, extract_x_y
from src.modelling.training import load_data, train_pipeline
from src.modelling.utils import load_pickle_object, save_pickle_object


# Define Prefect tasks
@task
def load_data_task(data_path: str):
    return load_data(data_path)


@task
def preprocess_data_task(df: pd.DataFrame, categorical_cols: list = None):
    df_encoded = encode_categorical_cols(df, categorical_cols=categorical_cols)
    X_train_scaled, X_test_scaled, y_train, y_test = extract_x_y(df_encoded)
    return X_train_scaled, X_test_scaled, y_train, y_test


@task
def train_model_task(X_train: np.ndarray, y_train: np.ndarray):
    model = train_pipeline(X_train, y_train)
    return model


@task
def save_model_task(model, path: str):
    save_pickle_object(model, path)


@task
def predict_model_task(input_data: np.ndarray, model):
    predictions = predict_age(input_data, model)
    return predictions


@task
def evaluate_model_task(y_test, y_pred):
    rmse = evaluate_model(y_test, y_pred)
    return rmse


@task
def load_model_task(model_path: str):
    # Custom function to load a pre-trained model from a file
    model = load_pickle_object(model_path)
    if model is None:
        logger.error("Model could not be loaded, please check the model path and file.")

    return model


@flow(name="Training Model Flow")
def train_model_workflow(
    train_filepath: str,
    artifacts_filepath: Optional[str] = None,
) -> dict:
    """
    Complete workflow for training the model:
    1. Load data
    2. Process data (encode categorical columns)
    3. Train the model
    4. Evaluate the model
    5. Save model
    """
    # Load training data
    logger.info("Processing training data...")
    data_path = "data/abalone.csv"
    train_df = load_data_task(data_path)

    # Process the data
    logger.info("Processing test data...")
    X_train_scaled, X_test_scaled, y_train, y_test = preprocess_data_task(
        train_df, CATEGORICAL_COLS
    )

    # Train model
    logger.info("Training model...")
    model = train_pipeline(X_train_scaled, y_train)

    # Evaluate model
    logger.info("Making predictions and evaluating...")
    y_pred = predict_model_task(X_test_scaled, model)
    rmse = evaluate_model_task(y_test, y_pred)

    # Save model
    if artifacts_filepath is not None:
        logger.info(f"Saving artifacts to {artifacts_filepath}...")
        model_path = os.path.join(artifacts_filepath, "model.pkl")
        save_model_task(model, model_path)

    return {"model": model, "rmse": rmse}


@flow(name="Batch Prediction Workflow")
def batch_predict_workflow(
    input_data_filepath: str,
    filepath_model: str,
    output_predictions_filepath: Optional[str] = None,
) -> dict:
    """
    Workflow for making batch predictions:
    1. Load the input data
    2. Preprocess the data
    3. Load a pre-trained model
    4. Generate predictions
    5. Optionally save the predictions to a file
    """
    logger = get_run_logger()

    # Load input data for predictions
    logger.info("Loading input data...")
    input_df = load_data_task(input_data_filepath)

    # Preprocess the input data
    logger.info("Preprocessing input data...")
    X_train, X_test, y_train, y_test = preprocess_data_task(input_df, CATEGORICAL_COLS)

    # Load the pre-trained model
    logger.info("Loading pre-trained model...")
    model = load_model_task(filepath_model)

    # Generate predictions
    logger.info("Making predictions...")
    predictions = predict_model_task(X_test, model)

    return {"predictions": predictions}


if __name__ == "__main__":
    train_model_workflow(
        train_filepath=os.path.join(DATA_DIRPATH, "abalone.csv"),
        artifacts_filepath=os.path.join(MODELS_DIRPATH),
    )

    batch_predict_workflow(
        input_data_filepath=os.path.join(DATA_DIRPATH, "abalone.csv"),
        filepath_model=os.path.join(MODELS_DIRPATH, "model.pkl"),
    )
