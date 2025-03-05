from pathlib import Path

from Codebase.Generic_VENV_Manger.venv_util import VENVUtil
from Codebase.Pathing.get_file_io_folder import get_file_io_folder
from Codebase.Pathing.get_project_root import get_project_root
import sys

def setup():
    # Creates VENV
    VENVUtil.setup_venv(get_project_root())

    # Creates fileIO stack. Configs & OutFiles
    file_io_folder = Path(get_file_io_folder())
    setup_path = file_io_folder / 'file_io_setup.py'
    VENVUtil.run_with_venv(get_project_root(), str(setup_path))

if __name__ == "__main__":
    setup()
