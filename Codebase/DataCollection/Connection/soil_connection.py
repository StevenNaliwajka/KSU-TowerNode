import re
import traceback
import serial
import atexit

from Codebase.DataCollection.Data.soil_set import SoilSet
from Codebase.FileIO.CSV.create_csv import create_csv


class SoilConnection:
    def __init__(self, port: str = "/dev/ttyUSB2", baudrate: int = 9600) -> None:
        try:
            self.ser = serial.Serial(port, baudrate, timeout=2)  # Increased timeout
            print("Soil Serial connection established.")
        except serial.SerialException as e:
            print(f"Error: Could not establish serial connection: {e}")
            self.ser = None
            return

        self.pattern = r"Set(\d{1,3}): Soil Moisture: (\d+) \| Soil Moisture \(%\): (\d+)% \| Soil Temperature:\s*([\d.]+)\s*°C"
        self.set_list = []
        self.csv_type = "SoilData"
        self.corrupt_count = 0

        # Start logging soil data
        self.log_soil_data()

        # Cleanup on exit
        atexit.register(self.close_serial)

    def log_soil_data(self) -> bool:
        if not self.ser or not self.ser.is_open:
            print("Serial connection lost. Attempting to reopen...")
            try:
                self.ser.open()
                print("Serial connection restored.")
            except serial.SerialException as e:
                print(f"Error: Unable to reopen serial connection: {e}")
                return False  # Return failure so soil_manager can restart serial

        try:
            self.ser.flush()
            raw_data = self.ser.read_until(b'\n')

            try:
                line = raw_data.decode('utf-8', errors='ignore').strip()
            except UnicodeDecodeError:
                self.corrupt_count += 1
                print(f"Warning: Corrupt data received: {raw_data}")
                if self.corrupt_count > 3:
                    self.restart_serial()
                return False  # Indicate failure

            if not line.startswith("Set"):
                print(f"Skipping malformed data: {line}")
                return False  # Indicate failure

            match = re.search(self.pattern, line)
            if not match:
                print(f"Skipping unrecognized format: {line}")
                return False  # Indicate failure

            soil_set_num = int(match.group(1))
            if soil_set_num > 1000:
                print(f"Invalid set number detected ({soil_set_num}), ignoring...")
                return False  # Indicate failure

            soil_set = self.get_set(soil_set_num)

            moisture = int(match.group(2))
            moisture_percent = int(match.group(3))
            temperature = float(match.group(4))

            if not self.validate_data(moisture, moisture_percent, temperature):
                print(f"Skipping invalid data: {line}")
                return False  # Indicate failure

            soil_set.update_data(moisture, moisture_percent, temperature)
            self.corrupt_count = 0  # Reset error counter
            return True  # Indicate success

        except KeyboardInterrupt:
            print("Stopping script...")
        except serial.SerialException as e:
            print(f"Serial error: {e}")
            self.restart_serial()
            return False
        except Exception as e:
            print(f"Error: {e}")
            traceback.print_exc()
            return False

    def validate_data(self, moisture, moisture_percent, temperature) -> bool:
        # validates soil data
        if not (0 <= moisture <= 1023):
            print(f"Invalid moisture value: {moisture}")
            return False
        if not (0 <= moisture_percent <= 100):
            print(f"Invalid moisture percentage: {moisture_percent}")
            return False
        if not (-50 <= temperature <= 100):
            print(f"Invalid temperature: {temperature}")
            return False
        return True

    def get_set(self, set_num) -> SoilSet:
        if set_num > 1000:
            print(f"Error: Too many soil sets. Ignoring request.")
            return None

        try:
            soil_set = self.set_list[set_num]
            if soil_set is None:
                soil_set = self.append_set(set_num)
            return soil_set
        except IndexError:
            return self.append_set(set_num)

    def append_set(self, set_num) -> SoilSet:
        # Prevent memory overflow
        if set_num > 1000:
            print(f"Error: Attempted to create set {set_num}, which is too large. Ignoring request.")
            return None

        print(f"Soil set {set_num} not found, creating new one...")

        while len(self.set_list) <= set_num:
            self.set_list.append(None)

        csv_path = create_csv(self.csv_type, set_num)
        self.set_list[set_num] = SoilSet(set_num, csv_path)
        return self.set_list[set_num]

    def close_serial(self) -> None:
        # closes serial when closing program
        if self.ser and self.ser.is_open:
            print("Closing serial connection...")
            self.ser.close()

    def restart_serial(self):
        # restarts serial after cascade of errors
        print("Restarting serial connection...")
        self.close_serial()
        try:
            self.ser.open()
            print("Serial connection restarted.")
            # Reset error counter
            self.corrupt_count = 0
        except serial.SerialException as e:
            print(f"Error: Unable to reopen serial connection: {e}")

    def data_to_csv(self):
        for soil_set in filter(None, self.set_list):
            try:
                soil_set.log_to_csv()
            except Exception as e:
                print(f"Error writing to CSV: {e}")
