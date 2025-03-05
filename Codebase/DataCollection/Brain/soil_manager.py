import sys
from pathlib import Path

# Dynamically find the project root, required to allow for correct imports.
folder_ct = 3  ### NOT always 2. Change to the qty of folders up before root.
PROJECT_ROOT = Path(__file__).resolve().parents[folder_ct]
sys.path.append(str(PROJECT_ROOT))

import time

from Codebase.DataCollection.Connection.soil_connection import SoilConnection


def soil_manager():
    soil_connection = SoilConnection()
    print("Soil connection established.")

    while True:
        print("Logging soil data...")
        soil_connection.log_soil_data()

        print("Displaying data...")
        soil_connection.display()

        time.sleep(1)


# Run the manager function when executing the script
if __name__ == "__main__":
    soil_manager()
