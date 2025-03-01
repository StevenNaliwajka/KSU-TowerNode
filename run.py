from Codebase.Generic_VENV_Manger.generic_venv_manager.venv_util import VENVUtil
from Codebase.Paths.get_project_root import get_project_root


def run():
    VENVUtil.run_with_venv(get_project_root(), get_project_root)

if __name__ == '__main__':
    run()