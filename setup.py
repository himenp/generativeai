"""Setup script for GenAI project utilities."""

from setuptools import setup, find_packages

setup(
    name="genai-utils",
    version="1.0.0",
    description="Utilities for GenAI project",
    packages=find_packages(),
    install_requires=[
        "pandas>=2.0.0",
        "numpy>=1.24.0",
    ],
    python_requires=">=3.8",
)
