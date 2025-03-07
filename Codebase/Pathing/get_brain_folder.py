from pathlib import Path

from Codebase.Pathing.get_project_root import get_project_root


def get_brain_folder() -> Path:
    root = Path(get_project_root())
    brain_folder = root / "Codebase" / "DataCollection" / "Brain"
    return brain_folder

if __name__ == "__main__":
    print(get_brain_folder())