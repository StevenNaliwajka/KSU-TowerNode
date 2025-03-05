import sys
from pathlib import Path

# Dynamically find the project root
folder_ct = 2
PROJECT_ROOT = Path(__file__).resolve().parents[folder_ct]
sys.path.append(str(PROJECT_ROOT))

from Codebase.Pathing.get_project_root import get_project_root

from generic_file_io.core.generic_create_folder import generic_create_folder

def file_io_setup():
    print("File IO Setup is running...")
    root = Path(get_project_root())
    csv_output = root / "CSVOutput"
    generic_create_folder(csv_output)
    print(f"CSV output folder created: {csv_output}")

if __name__ == "__main__":
    file_io_setup()