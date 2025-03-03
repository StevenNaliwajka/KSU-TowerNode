from pathlib import Path

from Codebase.Pathing.get_project_root import get_project_root


def get_brain_folder() -> Path:
    root = Path(get_project_root())
    brain_folder = root / "CollectionBrain"
    return brain_folder