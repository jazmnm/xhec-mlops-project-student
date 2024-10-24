import os
import pandas as pd
import pickle
from typing import Any

def pickle_object(obj: Any, path: str) -> None:
    try:
        with open(path, "wb") as f:
            pickle.dump(obj, f)
        print(f"Object successfully pickled and saved to {path}")
    except Exception as e:
        print(f"Error pickling the object: {e}")

def load_data(root_path: str, data_name: str):
        print(os.path.join(root_path, data_name))
        return pd.read_csv(os.path.join(root_path, data_name))
