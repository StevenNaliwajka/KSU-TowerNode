import serial

def make_soil_sensing_serial():
    ser = serial.Serial('/dev/ttyUSB1', 9600, timeout=1)