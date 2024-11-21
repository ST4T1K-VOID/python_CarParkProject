from display import Display
from sensor import Sensor
import datetime
import json
from pathlib import Path

class CarPark:
    def __init__(self, location='unknown', capacity=20, plates=None, sensors=None, displays=None, config_file=Path("config.json")):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []
        self.config_file = config_file if isinstance(config_file, Path) else Path(config_file)
        self.config_file.touch(exist_ok=True)

    def register(self, component):
        if not isinstance(component, (Sensor or Display)):
            raise TypeError('Component must be a Sensor or a Display')

        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)

    @property
    def available_bays(self):
        if len(self.plates) > self.capacity:
            return 0
        return (self.capacity-len(self.plates))

    def add_car(self, plate):
        self.plates.append(plate)
        self.update_display()

    def remove_car(self, plate):
        for plate_item in self.plates:
            if plate_item == plate:
                self.plates.remove(plate)
                return
        raise KeyError('plate not found')

    def update_display(self):
        display_info = {"available bays": self.available_bays, "Temperature": 25, "Time": {datetime.datetime.now()}}
        for display in self.displays:
            display.update(display_info)

    def write_config(self):
        with (self.config_file.open('W')) as file:
              json.dump({"Location": self.location, "Capacity": self.capacity},file)

    @classmethod
    def from_config(cls, file_path="config.json"):
        file_path = (file_path if isinstance(file_path, Path) else Path(file_path))
        with file_path.open("R") as file:
            config = json.load(file)
            return cls(config["Location"], config["Capacity"])

    def __str__(self):
        return f'CarPark at {self.location} with a capacity of {self.capacity} bays'
    