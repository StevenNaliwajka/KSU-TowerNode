import sys
from pathlib import Path


# Dynamically find the project root (assuming it's 3 levels up)
PROJECT_ROOT = Path(__file__).resolve().parents[2]  # Adjust the number if needed
sys.path.append(str(PROJECT_ROOT))

from generic_file_io.core.generic_create_folder import generic_create_folder

def file_io_setup():
    generic_create_folder()
    pass
