# Dynamically find the project root, required to allow for correct imports.
import sys
from pathlib import Path

folder_ct = 3  ### NOT always 2. Change to the qty of folders up before root.
PROJECT_ROOT = Path(__file__).resolve().parents[folder_ct]
sys.path.append(str(PROJECT_ROOT))

from generic_file_io.core.csv_manager.support.csv_append import csv_append

from Codebase.SupportMethods.get_date_time_formated import get_date_time_formated


class SoilSet:
    def __init__(self, soil_set_num: int, csv_path: str) -> None:
        self.soil_set = soil_set_num
        self.csv_path = csv_path
        ## UPDATE THIS
        self.depth = 6
        self.moisture = None
        self.moisture_percent = None
        self.temperature = None

        self.build_csv_header()

    def update_data(self, moisture: int, moisture_percent: int, temperature: float) -> None:
        self.moisture = moisture
        self.moisture_percent = moisture_percent
        self.temperature = temperature

    def display(self) -> None:
        print(f"For Soil Set{self.soil_set}:")
        print(f"Soil Moisture: {self.moisture}")
        print(f"Soil Moisture (%): {self.moisture_percent}%")
        print(f"Soil Temperature: {self.temperature}°C")

    def build_csv_header(self) -> None:
        # T1 Header
        data = ['Date', 'Depth', 'Set Number']
        csv_append(self.csv_path, data)
        data = [get_date_time_formated(), self.depth, self.soil_set]
        csv_append(self.csv_path, data)

        # T2 Header
        data = ['Timestamp', 'Soil Moisture Value', 'Soil Moisture (%)', 'Soil Temperature (°C)']
        csv_append(self.csv_path, data)

    def log_to_csv(self) -> None:
        data = [get_date_time_formated(), self.moisture, self.moisture_percent, self.temperature]
        csv_append(self.csv_path, data)
