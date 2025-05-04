import sys
import traceback
import serial
from pathlib import Path


# Dynamically find the project root, required to allow for correct imports.
folder_ct = 3  ### NOT always 2. Change to the qty of folders up before root.
PROJECT_ROOT = Path(__file__).resolve().parents[folder_ct]
sys.path.append(str(PROJECT_ROOT))

import time

from Codebase.DataCollection.Soil.soil_connection import SoilConnection


def soil_manager():
    print("[DEBUG] Initializing SoilConnection...")
    soil_connection = SoilConnection()
    print("[DEBUG] Soil connection established.")

    failure_count = 0  # Track consecutive failures

    while True:
        try:
            print("[DEBUG] Calling log_soil_data()...")
            result = soil_connection.log_soil_data()  # Call log function

            if not result:
                failure_count += 1  # Increase failure count on bad data
                print(f"[DEBUG] log_soil_data() failed. Failure count: {failure_count}")
            else:
                failure_count = 0  # Reset on success

            # Restart connection if too many failures
            if failure_count > 5:
                print("[DEBUG] Too many failed readings. Restarting serial connection...")
                soil_connection.restart_serial()
                failure_count = 0  # Reset failure count

            print("[DEBUG] Calling data_to_csv()...")
            soil_connection.data_to_csv()
            print("[DEBUG] CSV logging complete.")

        except KeyboardInterrupt:
            print("[DEBUG] Stopping script...")
            break
        except serial.SerialException as e:
            print(f"[DEBUG] Serial connection error: {e}")
            soil_connection.restart_serial()  # Restart the connection if serial fails
            failure_count += 1
        except Exception as e:
            print(f"[DEBUG] Unexpected error in soil_manager: {e}")
            traceback.print_exc()
            failure_count += 1

        print("[DEBUG] Sleeping for 1 second before next loop...")
        time.sleep(1)  # Pause between reads



# Run the manager function when executing the script
if __name__ == "__main__":
    soil_manager()
