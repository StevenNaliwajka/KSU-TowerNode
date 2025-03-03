import re

import serial
import atexit

class SoilConnection:
    def __init__(self, port:str="/dev/ttyUSB1", baudrate:int=9600) -> None:
        self.ser = serial.Serial(port, baudrate, timeout=1)
        print("Serial connection established.")

        self.pattern = r"Soil Moisture: (\d+) \| Soil Moisture \(%\): (\d+)% \| Soil Temperature: ([\d.]+) °C"


        self.moisture = None
        self.moisture_percent = None
        self.temperature = None

        self.log_soil_data()
        # Register cleanup to close the serial connection on exit
        atexit.register(self.close_serial)

    def log_soil_data(self) -> None:
        while True:
            try:
                line = self.ser.readline().decode('utf-8').strip()  # Read and decode data
                match = re.search(self.pattern, line)  # Match the pattern

                if match:
                    moisture = int(match.group(1))
                    moisture_percent = int(match.group(2))
                    temperature = float(match.group(3))
                    self.update_data(moisture, moisture_percent, temperature)

            except KeyboardInterrupt:
                print("Stopping script...")
                break
            except Exception as e:
                print(f"Error: {e}")

    def update_data(self, moisture: int, moisture_percent: int, temperature: float) -> None:
        self.moisture = moisture
        self.moisture_percent = moisture_percent
        self.temperature = temperature

    def display(self) -> None:
        print(f"Soil Moisture: {self.moisture}")
        print(f"Soil Moisture (%): {self.moisture_percent}%")
        print(f"Soil Temperature: {self.temperature}°C")

    def close_serial(self) -> None:
        """Closes the serial connection properly."""
        if self.ser and self.ser.is_open:
            print("Closing serial connection...")
            self.ser.close()

    def data_to_csv(self):
        pass