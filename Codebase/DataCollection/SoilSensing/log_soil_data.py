import serial
import re

class SoilSensing:
    def __init__(self) -> None:

        # Regular expression pattern to extract values
        self.pattern = r"Soil Moisture: (\d+) \| Soil Moisture \(%\): (\d+)% \| Soil Temperature: ([\d.]+) °C"

    def log_soil_data(self):

        while True:
            try:
                line = self.ser.readline().decode('utf-8').strip()  # Read and decode data
                match = re.search(self.pattern, line)  # Match the pattern

                if match:
                    soil_moisture = int(match.group(1))
                    soil_moisture_percent = int(match.group(2))
                    soil_temperature = float(match.group(3))

                    print(f"Soil Moisture: {soil_moisture}")
                    print(f"Soil Moisture (%): {soil_moisture_percent}%")
                    print(f"Soil Temperature: {soil_temperature}°C")

            except KeyboardInterrupt:
                print("Stopping script...")
                break
            except Exception as e:
                print(f"Error: {e}")

    def close_serial(self):