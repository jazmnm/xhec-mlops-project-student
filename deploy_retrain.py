import os

from prefect.client.schemas.schedules import CronSchedule

from config import DATA_DIRPATH, MODELS_DIRPATH
from orchestration import train_model_workflow

# Define the deployment for daily model training
train_model_workflow.serve(
    name="daily-train-model",
    schedules=[
        CronSchedule(
            cron="0 0 * * *",  # Every day at midnight
            timezone="Europe/Paris",
        )
    ],
)

if __name__ == "__main__":
    # Optionally, trigger the flow to run manually for testing
    train_model_workflow(
        train_filepath=os.path.join(DATA_DIRPATH, "abalone.csv"),
        artifacts_filepath=os.path.join(MODELS_DIRPATH),
    )
