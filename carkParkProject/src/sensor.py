from abc import ABC, abstractmethod
import random

class Sensor(ABC):
    def __init__(self, id, is_active, carpark):
        self.id = id
        self.is_active = is_active
        self.carpark = carpark

    @abstractmethod
    def update_carpark_status(self, plate):
        pass

    def detect_vehicle(self, plate):
        plate = self._scan_plate()
        self.update_carpark_status(plate)

    def _scan_plate(self):
        rdm = random.Random()
        return (f"PL8-{rdm.randint(0,9)}{rdm.randint(0,9)}{rdm.randint(0,9)}{rdm.randint(0,9)}{rdm.randint(0,9)}{rdm.randint(0,9)}")

    def __str__(self):
        return f'Sensor {self.id} | Status >>> {self.is_active}'


class EntrySensor(Sensor):
    def __init__(self, id, is_active, carpark):
        super().__init__(id, is_active, carpark)

    def update_carpark_status(self, plate):
        self.carpark.add_car(plate)

        print(f"<<Incoming vehicle>>\n<<Detected Plate: {plate}>>")


class ExitSensor(Sensor):
    def __init__(self, id, is_active, carpark):
        super().__init__(id, is_active, carpark)

    def update_carpark_status(self, plate):
        self.carpark.remove_car(plate)

        print(f"<<Outgoing vehicle>>\n<<Detected Plate: {plate}>>")
        
    def _scan_plate(self):
        return random.choice(self.carpark.plates)
