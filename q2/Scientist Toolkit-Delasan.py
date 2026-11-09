from abc import ABC, abstractmethod

class Sensor(ABC):
    @abstractmethod
    def get_reading(self):
        pass

class TempSensor(Sensor):
    def get_reading(self):
        return 24.5

class PHSensor(Sensor):
    def get_reading(self):
        return 7.2

print("--- Lab Inventory System ---")
print(f"[pH Sensor] Reading: {PHSensor().get_reading()}pH (Neutral)")
print(f"[Temperature Sensor] Reading: {TempSensor().get_reading()}°C")
print("----------------------------")

my_sensor = Sensor()