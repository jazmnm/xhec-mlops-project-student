import os
import pickle
from typing import Any


def save_pickle_object(obj: Any, path: str) -> None:
    try:
        with open(path, "wb") as f:
            pickle.dump(obj, f)
        print(f"Object successfully pickled and saved to {path}")
    except Exception as e:
        print(f"Error pickling the object: {e}")


def load_pickle_object(path: str) -> Any:
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "rb") as f:
            obj = pickle.load(f)
        print(f"Object successfully loaded from {path}")
        return obj
    except Exception as e:
        print(f"Error loading the object: {e}")
        return None
