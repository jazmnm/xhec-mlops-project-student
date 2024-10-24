# Utils file. TODO: add a `load_object` function to load pickle objects
import os
import pickle
from functools import lru_cache
from loguru import logger

@lru_cache
def load_project(filepath: os.PathLike):
    try:
        logger.info(f"Loading object from {filepath}")
        with open(filepath, "rb") as f:
            model = pickle.load(f)
        logger.info(f"Object successfully loaded from {filepath}")
        return model
    except Exception as e:
        logger.error(f"Error loading object from {filepath}: {e}")
        return None