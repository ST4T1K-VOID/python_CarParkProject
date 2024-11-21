from carpark import CarPark
from display import Display
from sensor import EntrySensor, ExitSensor

car_park = CarPark("Moondalup", 100)

entry_sensor = EntrySensor(1, True, car_park)
exit_sensor = ExitSensor(2, True, car_park)

display = Display(1, car_park, "Welcome to Moondalup", True)

car_park.register(entry_sensor)
car_park.register(exit_sensor)
car_park.register(display)

print(display.message)

count = 10
while count > 0:
    entry_sensor.detect_vehicle()
    count -= 1

car_park.update_display()

count = 2
while count > 0:
    exit_sensor.detect_vehicle()
    count -= 1

car_park.update_display()