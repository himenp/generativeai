"""Standardized initialization for GenAI project notebooks.

This module provides a simple init_notebook() function that:
- Detects if running in Google Colab or local environment
- Mounts Google Drive if needed
- Sets up project root and adds to sys.path
- Returns CONFIG dictionary with project_path and data_path

Usage in any notebook:
    import sys, os
    if 'google.colab' in sys.modules:
        project_root = '/content/drive/My Drive/Projects/GenAI'
    else:
        project_root = os.path.abspath(os.path.join(os.getcwd(), '..', '..'))
    if project_root not in sys.path:
        sys.path.append(project_root)
    
    from config import CONFIG
    from utils.data_loader import load_csv
"""

import sys
import os


def init_notebook():
    """Initialize notebook environment for both local and Colab execution.
    
    Returns:
        dict: Configuration dictionary with 'project_path' and 'data_path'
    """
    # Detect environment
    is_colab = 'google.colab' in sys.modules
    
    if is_colab:
        # Mount Google Drive in Colab
        try:
            from google.colab import drive
            drive.mount('/content/drive')
        except Exception as e:
            print(f"Warning: Could not mount Google Drive: {e}")
        
        project_root = '/content/drive/My Drive/Projects/GenAI'
    else:
        # Local environment - assume running from subdirectory
        # Try to find GenAI root by looking for config.py
        current = os.getcwd()
        project_root = None
        
        # Search up to 5 levels up for config.py
        for _ in range(5):
            if os.path.exists(os.path.join(current, 'config.py')):
                project_root = current
                break
            parent = os.path.dirname(current)
            if parent == current:  # reached root
                break
            current = parent
        
        # Fallback: assume two levels up from notebook location
        if project_root is None:
            project_root = os.path.abspath(os.path.join(os.getcwd(), '..', '..'))
    
    # Add project root to Python path
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
    
    # Return configuration
    config = {
        'project_path': project_root,
        'data_path': os.path.join(project_root, 'data'),
        'is_colab': is_colab
    }
    
    return config


def get_notebook_template():
    """Return the standard initialization template for notebooks.
    
    Returns:
        str: Template code to copy into notebooks
    """
    return '''import sys, os

# Setup environment for both local and Colab
if 'google.colab' in sys.modules:
    project_root = '/content/drive/My Drive/Projects/GenAI'
else:
    project_root = os.path.abspath(os.path.join(os.getcwd(), '..', '..'))
if project_root not in sys.path:
    sys.path.append(project_root)

# Import centralized configuration and utilities
from config import CONFIG
from utils.data_loader import load_csv
'''
