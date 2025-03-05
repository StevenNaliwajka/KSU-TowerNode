from pathlib import Path

from Codebase.Pathing.get_project_root import get_project_root


def get_csv_out_folder() -> Path:
    root = Path(get_project_root())
    csv_out = root / 'CSVOutput'
    return csv_out

if __name__ == "__main__":
    print(get_csv_out_folder())