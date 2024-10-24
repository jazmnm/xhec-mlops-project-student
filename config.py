from pathlib import Path

CATEGORICAL_COLS = ["Sex"]

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIRPATH = str(PROJECT_ROOT / "data")
MODELS_DIRPATH = str(PROJECT_ROOT / "models")
