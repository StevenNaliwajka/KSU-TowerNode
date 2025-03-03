from Codebase.SupportMethods.get_date_time_formated import get_date_time_formated


class SoilSensingData:
    def __init__(self, moisture: str, moisture_percent: str, temperature: str) -> None:
        self.moisture = int(moisture)
        self.moisture_percent = int(moisture_percent)
        self.temperature = int(temperature)

        current_date_time = get_date_time_formated()
        self.csv_path = f"SoilSensingData{current_date_time}.csv";
        ## CREATE CSV WITH GENERIC CSV TOOL


    def update_data(self, moisture: str, moisture_percent: str, temperature: str) -> None:
        self.moisture = int(moisture)
        self.moisture_percent = int(moisture_percent)
        self.temperature = int(temperature)

    def log_data(self, csv_file_path: str) -> None:
        # Takes in csv path and using generic csv manager updates info
        pass

    def display(self) -> None:
        print(f"Soil Moisture: {self.moisture}")
        print(f"Soil Moisture (%): {self.moisture_percent}%")
        print(f"Soil Temperature: {self.temperature}°C")

    def parse_serial_data(line):
        """ Parses serial data and returns a SensorData object """
        pattern = r"Soil Moisture: (\d+) \| Soil Moisture \(%\): (\d+)% \| Soil Temperature: ([\d.]+) °C"
        match = re.search(pattern, line)

        if match:
            return SensorData(match.group(1), match.group(2), match.group(3))
        return None