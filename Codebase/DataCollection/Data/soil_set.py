class SoilSet:
    def __init__(self, soil_set_num: int, csv_path: str) -> None:
        self.soil_set = soil_set_num
        self.csv_path = csv_path
        self.moisture = None
        self.moisture_percent = None
        self.temperature = None

    def update_data(self, moisture: int, moisture_percent: int, temperature: float) -> None:
        self.moisture = moisture
        self.moisture_percent = moisture_percent
        self.temperature = temperature

    def display(self) -> None:
        print(f"For Soil Set{self.soil_set}:")
        print(f"Soil Moisture: {self.moisture}")
        print(f"Soil Moisture (%): {self.moisture_percent}%")
        print(f"Soil Temperature: {self.temperature}°C")