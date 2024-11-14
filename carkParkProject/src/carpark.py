from display import *
from sensor import *


class CarPark:
    def __init__(self, location='unknown', capacity=20, plates=None, sensors=None, displays=None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []

    def register(self, component):
        if not isinstance(component, (Sensor or Display)):
            raise TypeError('Component must be a Sensor or a Display')

        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)

    def __str__(self):
        return f'CarPark at {self.location} with a capacity of {self.capacity} bays'
    