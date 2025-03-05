from pathlib import Path

from Codebase.Pathing.get_project_root import get_project_root


def get_file_io_folder() -> Path:
    root = Path(get_project_root())
    file_io_folder = root / "Codebase" / "FileIO"
    return file_io_folder

if __name__ == "__main__":
    print(get_file_io_folder())