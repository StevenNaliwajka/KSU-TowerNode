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

    failure_count = 0  # Track consecutive failures

    while True:
        try:
            result = soil_connection.log_soil_data()  # Call log function

            if not result:
                failure_count += 1  # Increase failure count on bad data
            else:
                failure_count = 0  # Reset on success

            # Restart connection if too many failures
            if failure_count > 5:
                print("Too many failed readings. Restarting serial connection...")
                soil_connection.restart_serial()
                failure_count = 0  # Reset failure count

            # Dump valid data to CSV
            soil_connection.data_to_csv()

        except KeyboardInterrupt:
            print("Stopping script...")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")
            failure_count += 1  # Count unknown errors

        time.sleep(1)  # Pause between reads


# Run the manager function when executing the script
if __name__ == "__main__":
    soil_manager()
