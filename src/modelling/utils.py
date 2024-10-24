import pickle
from pathlib import Path
from typing import Any

import pandas as pd
import numpy as np


def save_pickle_object(obj: Any, path: str) -> None:
    try:
        with open(path, "wb") as f:
            pickle.dump(obj, f)
        print(f"Object successfully pickled and saved to {path}")
    except Exception as e:
        print(f"Error pickling the object: {e}")
