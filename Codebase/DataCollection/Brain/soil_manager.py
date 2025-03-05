import sys
from pathlib import Path
import time

# Ensure the project root is in sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

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
