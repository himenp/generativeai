"""Configuration utilities for loading and managing application settings."""

from pathlib import Path
import yaml  # pylint: disable=import-error
from utils.paths import CONFIG_DIR


def load_yaml(path: Path):
    """Load a YAML file."""
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_config(filename="config.yaml"):
    """Load config from config/ directory."""
    config_path = CONFIG_DIR / filename
    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")
    return load_yaml(config_path)


def get_config_value(key_path: str, default=None, config_dict=None):
    """Get a nested config value using dot notation.

    Args:
        key_path: Dot-separated path to config value (e.g., "model.random_state")
        default: Default value if key not found
        config_dict: Config dictionary to search (uses load_config() if None)

    Returns:
        Config value or default if not found
    """
    if config_dict is None:
        config_dict = load_config()

    keys = key_path.split(".")
    value = config_dict

    for key in keys:
        if isinstance(value, dict):
            value = value.get(key)
            if value is None:
                return default
        else:
            return default

    return value
