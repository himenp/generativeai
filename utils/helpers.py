"""Helper utilities for notebooks and scripts."""

import random
from pathlib import Path
import pandas as pd  # pylint: disable=import-error


def set_seed(seed=42):
    """Set random seed for reproducibility."""
    random.seed(seed)
    import numpy as np  # pylint: disable=import-error,import-outside-toplevel
    np.random.seed(seed)
    try:
        import torch  # pylint: disable=import-error,import-outside-toplevel
        torch.manual_seed(seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(seed)
    except ImportError:
        pass


def load_csv(path: Path | str, **kwargs) -> pd.DataFrame:
    """Load CSV file with automatic path resolution to data/raw/."""
    path = Path(path)
    if not path.is_absolute():
        from utils.paths import RAW_DATA_DIR  # pylint: disable=import-outside-toplevel
        path = RAW_DATA_DIR / path
    return pd.read_csv(path, **kwargs)


def save_csv(df: pd.DataFrame, path: Path | str, **kwargs) -> None:
    """Save DataFrame to CSV in data/raw/."""
    path = Path(path)
    if not path.is_absolute():
        from utils.paths import RAW_DATA_DIR  # pylint: disable=import-outside-toplevel
        path = RAW_DATA_DIR / path
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False, **kwargs)


def load_parquet(path: Path | str, **kwargs) -> pd.DataFrame:
    """Load Parquet file from data/raw/."""
    path = Path(path)
    if not path.is_absolute():
        from utils.paths import RAW_DATA_DIR  # pylint: disable=import-outside-toplevel
        path = RAW_DATA_DIR / path
    return pd.read_parquet(path, **kwargs)


def save_parquet(df: pd.DataFrame, path: Path | str, **kwargs) -> None:
    """Save DataFrame to Parquet in data/raw/."""
    path = Path(path)
    if not path.is_absolute():
        from utils.paths import RAW_DATA_DIR  # pylint: disable=import-outside-toplevel
        path = RAW_DATA_DIR / path
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(path, index=False, **kwargs)
