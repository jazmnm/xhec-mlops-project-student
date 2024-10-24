# This module is the training flow:
# it reads the data, preprocesses it, trains a model and saves it.
import argparse
import pickle
from pathlib import Path

from preprocessing import extract_x_y
from training import train_model
from utils import load_data


def main(trainset_path: Path) -> None:
    """
    Train a model using the data at the given path and save the model (pickle).
    """

    train_df = load_data(trainset_path)

    # Preprocess data
    X_train, X_test, y_train, y_test = extract_x_y(train_df)

    # Train model
    model = train_model(X_train, y_train)

    """
    Pickle model -->
    # Save the model in pkl format
    # in the `src/web_service/local_objects` folder
    """

    with open("src/web_service/local_objects/model.pkl", "wb") as f:
        pickle.dump(model, f)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Train a model using the data at the given path."
    )
    parser.add_argument("trainset_path", type=str, help="Path to the training set")

    args = parser.parse_args()

    main(Path(args.trainset_path))
