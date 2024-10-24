import os
import pandas as pd
import pickle
from typing import Any
from pathlib import Path

def pickle_object(obj: Any, path: str) -> None:
    try:
        with open(path, "wb") as f:
            pickle.dump(obj, f)
        print(f"Object successfully pickled and saved to {path}")
    except Exception as e:
        print(f"Error pickling the object: {e}")
def load_data(data_path: Path) -> pd.DataFrame:
    return pd.read_csv(data_path)
