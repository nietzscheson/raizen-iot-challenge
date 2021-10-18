import csv
import os
from model import Sensor
from database import session

if __name__ == "__main__":
    with open(f"{os.getcwd()}/sensor-data.csv") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:

            sensor = Sensor()
            sensor.time = row["time"]
            sensor.power = row["power"]
            sensor.temp = row["temp"]
            sensor.humidity = row["humidity"]
            sensor.light = row["light"]
            sensor.CO2 = row["CO2"]
            sensor.dust = row["dust"]

            session.add(sensor)

            print(
                "Importing: >>> ",
                f"time: {row['time']}",
                f"Power: {row['power']}",
                f"Temperature: {row['temp']}",
                f"Humidity: {row['humidity']}",
                f"Light: {row['light']}",
                f"CO2: {row['CO2']}",
                f"dust: {row['dust']}",
            )

        session.commit()
