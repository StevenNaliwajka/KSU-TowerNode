import sys
from pathlib import Path

# Ensure the project root is in sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from generic_file_io.core.generic_create_folder import generic_create_folder

def file_io_setup():
    generic_create_folder()
    pass