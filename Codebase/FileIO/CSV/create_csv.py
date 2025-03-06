from Codebase.Pathing.get_csv_out_folder import get_csv_out_folder
from Codebase.SupportMethods.get_date_time_formated import get_date_time_formated
from generic_file_io.csv_manager.csv_create import csv_create

def create_csv(collection_type, number) -> str:
    current_day_time = get_date_time_formated()
    filename = f"{collection_type}_instance{number}_{current_day_time}.csv"

    # build path
    file_path = get_csv_out_folder() / filename

    # create CSV
    csv_create(str(file_path))

    # return str of path
    return str(file_path)
