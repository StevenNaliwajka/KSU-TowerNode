from Codebase.SupportMethods.get_current_date import get_current_date
from Codebase.SupportMethods.get_current_time import get_current_time
import csv


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
        self.csv_append(self.csv_path, data)

        metadata = {
            'Date': get_current_date(),
            'Depth': self.depth,
            'Set Number': self.soil_set
        }
        self.csv_append(self.csv_path, metadata)

        # Add blank row
        # csv_append(self.csv_path, {}, separator=True)

        # Column headers for soil data
        column_headers = {
            'Date (Year-Mon-Day)': "Date (Year-Mon-Day)",
            'Time (Hour-Min-Sec)': "Time (Hour-Min-Sec)",
            'Soil Moisture Value': "Soil Moisture Value",
            'Soil Moisture (%)': "Soil Moisture (%)",
            'Soil Temperature (°C)': "Soil Temperature (°C)",
        }
        self.csv_append(self.csv_path, column_headers)

    def log_to_csv(self) -> None:
        time = get_current_time()
        print(f"({time}) Logging SoilData to CSV : {self.csv_path}")

        try:
            # Logs to csv
            data = {
                'Date (Year-Mon-Day)': get_current_date(),
                'Time (Hour-Min-Sec)': get_current_time(),
                'Soil Moisture Value': self.moisture,
                'Soil Moisture (%)': self.moisture_percent,
                'Soil Temperature (°C)': self.temperature,
            }
            self.csv_append(self.csv_path, data)
            print("Logging SoilData to CSV Complete")

        except Exception as e:
            print(f"Error logging SoilData to CSV: {e}")
            import traceback
            traceback.print_exc()

    def csv_append(self, file_path: str, row: dict, separator: bool = False) -> None:
        # If separator is requested, write a blank row
        if separator:
            with open(file_path, 'a', newline='') as f:
                f.write("\n")
            return

        # Append the row
        with open(file_path, 'a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=row.keys())

            # Write header only if file is empty
            if f.tell() == 0:
                writer.writeheader()

            writer.writerow(row)


