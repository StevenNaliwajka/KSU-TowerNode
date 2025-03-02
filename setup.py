from Codebase.Generic_VENV_Manger.venv_util import VENVUtil
from Codebase.Pathing.get_project_root import get_project_root
import sys

def setup():
    VENVUtil.setup_venv(get_project_root())

if __name__ == "__main__":
    setup()
