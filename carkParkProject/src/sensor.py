from abc import ABC, abstractmethod
import random

class Sensor(ABC):
    def __init__(self, id, is_active, carpark):
        self.id = id
        self.is_active = is_active
        self.carpark = carpark

    @abstractmethod
    def detect_vehicle(self, plate):
        pass



    def __str__(self):
        return f'Sensor {self.id} | Status >>> {self.is_active}'


class EntrySensor(Sensor):
    pass


class ExitSensor(Sensor):
    pass
