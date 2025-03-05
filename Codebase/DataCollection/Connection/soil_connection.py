import re

import serial
import atexit


from Codebase.DataCollection.Data.soil_set import SoilSet
from Codebase.FileIO.CSV.create_csv import create_csv


class SoilConnection:
    def __init__(self, port:str="/dev/ttyUSB2", baudrate:int=9600) -> None:
        self.ser = serial.Serial(port, baudrate, timeout=1)
        print("Serial connection established.")

        # self.pattern = r"Soil Moisture: (\d+) \| Soil Moisture \(%\): (\d+)% \| Soil Temperature: ([\d.]+) °C"
        self.pattern = r"Set(\d+): Soil Moisture: (\d+) \| Soil Moisture \(%\): (\d+)% \| Soil Temperature: ([\d.]+) °C"

        self.set_list = []

        self.csv_type = "SoilData"

        print("Attempting to read from serial...")
        self.log_soil_data()
        # cleanup on exit
        print("Registering exit function")
        atexit.register(self.close_serial)

    def log_soil_data(self) -> None:
        try:
            print("Reading Soil Moisture Data...")
            line = self.ser.readline().decode('utf-8').strip()
            print(f"line: {line}")
            match = re.search(self.pattern, line)
            print("Data matched")

            soil_set_num = int(match.group(1)) -1
            soil_set = self.get_set(soil_set_num)
            print(f"Soil Set Number: {soil_set_num}")

            if match:
                moisture = int(match.group(2))
                print(f"Soil Moisture: {moisture}")
                moisture_percent = int(match.group(3))
                print(f"Soil Moisture Percent: {moisture_percent}")
                temperature = float(match.group(4))
                print(f"Temperature: {temperature}")
                print("updating data")
                soil_set.update_data(moisture, moisture_percent, temperature)

        except KeyboardInterrupt:
            print("Stopping script...")
        except Exception as e:
            print(f"Error: {e}")

    def get_set(self, set_num) -> SoilSet:
        try:
            soil_set = self.set_list[set_num]
            if soil_set is None:
                print("Setting not found, creating new one...")
                soil_set = self.append_set(set_num)
                return soil_set
            return soil_set
        except IndexError:
            soil_set = self.append_set(set_num)
            return soil_set

    def display(self):
        print("Displaying Soil Moisture Data...")
        for soil_set in self.set_list:
            soil_set.display()


    def append_set(self, set_num) -> SoilSet:
        while len(self.set_list) <= set_num:
            self.set_list.append(None)

        csv_path = create_csv(self.csv_type, set_num+1)
        self.set_list[set_num] = SoilSet(set_num, csv_path)
        return self.set_list[set_num]

    def close_serial(self) -> None:
        # Closes serial on end.
        if self.ser and self.ser.is_open:
            print("Closing serial connection...")
            self.ser.close()

    def data_to_csv(self):
        print("Logging Soil Moisture Data...")
        for soil_set in self.set_list:
            soil_set.log_soil_data()