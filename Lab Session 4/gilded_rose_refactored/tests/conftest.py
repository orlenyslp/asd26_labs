"""conftest.py — pytest configuration for Gilded Rose test suite."""
import sys
from pathlib import Path

# Ensure the project root is on the Python path so that tests in the
# tests/ subdirectory can import gilded_rose and item directly.
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))
