from generic_file_io.csv_manager.csv_append import csv_append
from Codebase.SupportMethods.get_date_time_formated import get_date_time_formated

class SoilSet:
    def __init__(self, soil_set_num: int, csv_path: str) -> None:
        self.soil_set = soil_set_num
        self.csv_path = csv_path
        self.depth = 6
        self.moisture = None
        self.moisture_percent = None
        self.temperature = None

        self.build_csv_header()

    def update_data(self, moisture: int, moisture_percent: int, temperature: float) -> None:
        # Updates
        self.moisture = moisture
        self.moisture_percent = moisture_percent
        self.temperature = temperature

    def display(self) -> None:
        # Dispays for debugging
        print(f"For Soil Set {self.soil_set}:")
        print(f"Soil Moisture: {self.moisture}")
        print(f"Soil Moisture (%): {self.moisture_percent}%")
        print(f"Soil Temperature: {self.temperature}°C")

    def build_csv_header(self) -> None:
        # Builds headders
        data = {
            'Date': 'Date',
            'Depth': 'Depth',
            'Set Number': 'Set Number'
        }
        csv_append(self.csv_path, data)

        metadata = {
            'Date': get_date_time_formated(),
            'Depth': self.depth,
            'Set Number': self.soil_set
        }
        csv_append(self.csv_path, metadata)

        # Add blank row
        csv_append(self.csv_path, {}, separator=True)

        # Column headers for soil data
        column_headers = {
            'Timestamp': "Timestamp",
            'Soil Moisture Value': "Soil Moisture Value",
            'Soil Moisture (%)': "Soil Moisture (%)",
            'Soil Temperature (°C)': "Soil Temperature (°C)",
        }
        csv_append(self.csv_path, column_headers)

    def log_to_csv(self) -> None:
        # Logs to csv
        data = {
            'Timestamp': get_date_time_formated(),
            'Soil Moisture Value': self.moisture,
            'Soil Moisture (%)': self.moisture_percent,
            'Soil Temperature (°C)': self.temperature,
        }
        csv_append(self.csv_path, data)
