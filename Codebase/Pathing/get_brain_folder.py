from pathlib import Path

from Codebase.Pathing.get_project_root import get_project_root


def get_brain_folder() -> Path:
    root = get_project_root()
    path = Path(root)

    brain_folder = path.joinpath(root / "CollectionBrain")
    return brain_folder