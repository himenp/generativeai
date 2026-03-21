# config.py - Centralized configuration for the GenerativeAI project
import sys
import os

# Colab environment constants
COLAB_PROJECT_ROOT = '/content/drive/My Drive/Projects/GenerativeAI'

# Auto-detect and setup environment when this module is imported
def _auto_setup():
    """Automatically setup environment when config is imported."""
    if 'google.colab' in sys.modules:
        # Colab environment
        try:
            from google.colab import drive
            drive.mount('/content/drive', force_remount=False)
        except Exception:
            pass  # Drive might already be mounted
        project_root = COLAB_PROJECT_ROOT
    else:
        # Local environment - walk up the directory tree looking for README.md
        # (a reliable project root marker that exists in GenerativeAI/)
        current = os.path.dirname(os.path.abspath(__file__))
        project_root = None

        for _ in range(6):  # Search up to 6 levels
            if os.path.exists(os.path.join(current, 'README.md')) and \
               os.path.exists(os.path.join(current, 'data')):
                project_root = current
                break
            parent = os.path.dirname(current)
            if parent == current:  # Reached filesystem root
                break
            current = parent

        # Fallback: src/ is one level below the project root
        if project_root is None:
            project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    
    return {
        'project_path': project_root,
        'data_path': os.path.join(project_root, 'data'),
        'is_colab': 'google.colab' in sys.modules
    }

# Initialize configuration when module is imported
CONFIG = _auto_setup()


def ensure_project_in_path():
    """Ensure project root is in sys.path. Call this before importing utils."""
    if CONFIG['project_path'] not in sys.path:
        sys.path.insert(0, CONFIG['project_path'])


# Bootstrap code snippet for notebooks (copy-paste into notebook cells)
NOTEBOOK_INIT = '''import sys, os
sys.path.insert(0, '{colab}' if 'google.colab' in sys.modules else os.path.abspath(os.path.join(os.getcwd(), '../..')))
from config import CONFIG
from utils.data_loader import load_csv
'''.format(colab=COLAB_PROJECT_ROOT)