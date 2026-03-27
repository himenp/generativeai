"""Path utilities for locating project directories and data files."""

from pathlib import Path

def find_project_root(markers=("requirements.txt", "pyproject.toml", ".git")):
    """Find the project root by walking up from the current directory."""
    cwd = Path.cwd().resolve()
    for path in [cwd] + list(cwd.parents):
        if any((path / marker).exists() for marker in markers):
            return path
    raise FileNotFoundError("Project root not found. Is this running in the project directory?")


ROOT = find_project_root()
DATA_DIR = ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
INTERIM_DATA_DIR = DATA_DIR / "interim"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
OUTPUTS_DIR = DATA_DIR / "outputs"
CONFIG_DIR = ROOT / "config"
UTILS_DIR = ROOT / "utils"


def ensure_dir_exists(*paths):
    """Create directories if they don't exist."""
    for path in paths:
        Path(path).mkdir(parents=True, exist_ok=True)


# Ensure common dirs exist
ensure_dir_exists(RAW_DATA_DIR, INTERIM_DATA_DIR, PROCESSED_DATA_DIR, OUTPUTS_DIR)
