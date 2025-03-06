from Codebase.Pathing.get_csv_out_folder import get_csv_out_folder
from Codebase.SupportMethods.get_current_date import get_current_date
from generic_file_io.csv_manager.csv_create import csv_create

from Codebase.SupportMethods.get_file_time import get_file_time


def create_csv(collection_type, number) -> str:
    date = get_current_date()
    time = get_file_time()
    filename = f"{collection_type}_instance{number}_{date}_{time}.csv"

    # build path
    file_path = get_csv_out_folder() / filename

    # create CSV
    csv_create(str(file_path))

    # return str of path
    return str(file_path)
