import unittest

import sensor
from sensor import Sensor, EntrySensor, ExitSensor
from carpark import CarPark

class TestEntrySensor(unittest.TestCase):
    def setUp(self):
        self.sensor = EntrySensor(1, True, CarPark())

    def test_init(self):
        self.assertIsInstance(self.sensor, EntrySensor)
        self.assertEqual(self.sensor.id, 1)
        self.assertEqual(self.sensor.is_active, True)
        self.assertIsInstance(self.sensor.carpark, CarPark)

    def test_scan_plate(self):
        self.assertEqual(len(self.sensor._scan_plate()), 10)

    def test_detect_vehicle(self):
        expected_length = (self.sensor.carpark.available_bays - 1)
        self.sensor.detect_vehicle()
        self.assertEqual(self.sensor.carpark.available_bays, expected_length)

class TestExitSensor(unittest.TestCase):
    def setUp(self):
        self.sensor = ExitSensor(1, True, CarPark(plates=["PL8-1","PL8-2","PL8-3","PL8-4"]))

    def test_init(self):
        self.assertIsInstance(self.sensor, ExitSensor)
        self.assertEqual(self.sensor.id, 1)
        self.assertEqual(self.sensor.is_active, True)
        self.assertIsInstance(self.sensor.carpark, CarPark)

    def test_detect_vehicle(self):
        expected_length = (self.sensor.carpark.available_bays + 1)

        self.sensor.detect_vehicle()

        self.assertEqual(expected_length, self.sensor.carpark.available_bays)
