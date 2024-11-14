class Sensor:
    def __init__(self, id, is_active, carpark):
        self.id = id
        self.is_active = is_active
        self.carpark = carpark

    def __str__(self):
        return f'Sensor {self.id} | Status >>> {self.is_active}'