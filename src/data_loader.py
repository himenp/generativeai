"""Data loader utilities for the GenAI project.

Provides functions to locate project data files (works in local runs and Colab)
and a convenience `load_csv()` wrapper around `pandas.read_csv`.

Usage:
    from utils.data_loader import load_csv
    df = load_csv('Sales.csv')

The locator will try, in order:
 - `CONFIG['data_path']` (if a `CONFIG` dict exists in the interactive environment)
 - `./data/<name>` in the current directory and parent directories (up to `max_levels`)
 - `../../data/<name>` relative to current working directory
 - common Colab Google Drive mounts like `/content/drive/My Drive/Projects/GenerativeAI/data/<name>`
"""
from __future__ import annotations

import os
from typing import Optional


def _get_config() -> Optional[dict]:
    """Try to retrieve a `CONFIG` dict from the interactive environment.

    Many notebooks create a `CONFIG` top-level dictionary. When this module
    is imported from a notebook, the module can access that `CONFIG`
    via the `__main__` module.
    """
    try:
        import __main__ as main

        cfg = getattr(main, 'CONFIG', None)
        if isinstance(cfg, dict):
            return cfg
    except Exception:
        pass
    return None


def locate_data_file(name: str = 'Sales.csv', max_levels: int = 6) -> Optional[str]:
    """Locate a data file in the project or Colab drive.

    Returns the full path if found, otherwise `None`.
    """
    # 1) Try CONFIG if available
    cfg = _get_config()
    if cfg:
        data_root = cfg.get('data_path')
        if data_root:
            candidate = os.path.join(data_root, name)
            if os.path.exists(candidate):
                return candidate

    # 2) Walk up from cwd searching for data/<name>
    cur = os.getcwd()
    for _ in range(max_levels + 1):
        candidate = os.path.join(cur, 'data', name)
        if os.path.exists(candidate):
            return candidate
        parent = os.path.dirname(cur)
        if parent == cur:
            break
        cur = parent

    # 3) Check the common relative path used in older notebooks (two levels up)
    candidate = os.path.normpath(os.path.join(os.getcwd(), '..', '..', 'data', name))
    if os.path.exists(candidate):
        return candidate

    # 4) Check common Colab Google Drive mount points
    colab_candidates = [
        os.path.join('/content', 'drive', 'My Drive', 'Projects', 'GenAI', 'data', name),
        os.path.join('/content', 'drive', 'MyDrive', 'Projects', 'GenAI', 'data', name),
    ]
    for cand in colab_candidates:
        if os.path.exists(cand):
            return cand

    return None


def load_csv(name_or_path: str, **pd_read_csv_kwargs):
    """Load a CSV into a pandas.DataFrame.

    - If `name_or_path` exists on disk it will be loaded directly.
    - Otherwise `locate_data_file()` will be used to resolve the name.

    Raises FileNotFoundError if the file cannot be found.
    """
    try:
        import pandas as pd
    except Exception as e:  # pragma: no cover - pandas required at runtime
        raise ImportError('pandas is required to use load_csv()') from e

    if os.path.exists(name_or_path):
        return pd.read_csv(name_or_path, **pd_read_csv_kwargs)

    candidate = locate_data_file(name_or_path)
    if candidate is None:
        raise FileNotFoundError(
            f"Could not find '{name_or_path}'. Checked CONFIG['data_path'], parent folders' data/ directories, ../../data/, and common Colab mounts."
        )

    return pd.read_csv(candidate, **pd_read_csv_kwargs)


__all__ = ["locate_data_file", "load_csv"]
