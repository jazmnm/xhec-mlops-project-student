import numpy as np
from prefect import task
from sklearn.metrics import root_mean_squared_error
from sklearn.pipeline import Pipeline


@task(
    name="predict_age",
    description="Production age prediction",
    retries=2,
    retry_delay_seconds=30,
    tags=["ml", "prod"],
    log_prints=True,
    timeout_seconds=300,
)
def predict_age(input_data: np.ndarray, pipeline: Pipeline):
    return pipeline.predict(input_data)


def evaluate_model(y_pred: np.ndarray, y_test: np.ndarray):
    return root_mean_squared_error(y_test, y_pred)
