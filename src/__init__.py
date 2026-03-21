"""Utilities package for GenAI project.

This package contains utility modules for data loading and other common tasks.
"""

__version__ = "1.0.0"

# Import commonly used functions for easy access
from .data_loader import load_csv, locate_data_file
from .notebook_init import init_notebook, get_notebook_template

__all__ = ['load_csv', 'locate_data_file', 'init_notebook', 'get_notebook_template']
