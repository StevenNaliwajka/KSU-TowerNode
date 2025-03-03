from datetime import time

from Codebase.DataCollection.Connection.soil_connection import SoilConnection


def soil_mananager():
    soil_connection = SoilConnection()

    while True:
        soil_connection.log_soil_data()
        soil_connection.display()
        time.sleep(1)
