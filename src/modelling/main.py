import argparse
from pathlib import Path

from preprocessing import extract_x_y
from training import load_data, train_pipeline
from utils import save_pickle_object


def main(trainset_path: Path) -> None:
    """
    Train a model using the data at the given path and save the model (pickle).
    """

    train_df = load_data(trainset_path)

    # Preprocess data
    X_train, X_test, y_train, y_test = extract_x_y(train_df)

    # Train model
    model = train_pipeline(X_train, y_train)

    """
    Pickle model -->
    # Save the model in pkl format
    # in the `src/web_service/local_objects` folder
    """

    pickle_save_path = "src/web_service/local_objects/model.pkl"
    save_pickle_object(model, pickle_save_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Train a model using the data at the given path."
    )
    parser.add_argument("trainset_path", type=str, help="Path to the training set")
    args = parser.parse_args()

    main(Path(args.trainset_path))
