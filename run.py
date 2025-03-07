from pathlib import Path

from Codebase.Generic_VENV_Manger.venv_util import VENVUtil
from Codebase.Pathing.get_brain_folder import get_brain_folder
from Codebase.Pathing.get_project_root import get_project_root


def run():
    brain_folder_path = get_brain_folder()
    soil_manager_path = brain_folder_path / "soil_manager.py"
    VENVUtil.run_with_venv(get_project_root(), str(soil_manager_path))

if __name__ == '__main__':
    run()