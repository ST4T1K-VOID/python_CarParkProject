class CarPark:
    def __init__(self, location='unknown', capacity=20, plates=None, sensors=None, displays=None):
        self.location = location
        self.capacity = capacity
        self.plates = plates
        self.sensors = sensors
        self.displays = displays

    def __str__(self):
        return f'CarPark at {self.location} with a capacity of {self.capacity} bays'
    